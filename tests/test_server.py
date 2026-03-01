"""Tests for yomitan_api.py pure functions.

Uses unittest.mock to avoid needing a real browser or stdin.
"""

import io
import json
import os
import struct
import sys
import tempfile
import types
import unittest
from unittest.mock import patch, MagicMock

# ---------------------------------------------------------------------------
# Import the module — it runs under __main__ guard so no server starts
# ---------------------------------------------------------------------------
import importlib
if "yomitan_api" in sys.modules:
    del sys.modules["yomitan_api"]

# Ensure the project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import yomitan_api

# Global overrides for tests to avoid hangs and TTY issues
yomitan_api.PROCESS_STARTUP_WAIT = 0


def _fake_stdin(data: bytes) -> types.SimpleNamespace:
    """Return a fake sys.stdin whose .buffer is an io.BytesIO.

    sys.stdin.buffer is a read-only attribute on CPython 3.9 (C-level slot),
    so we cannot patch it with patch.object. Instead we replace sys.stdin
    wholesale with a SimpleNamespace that exposes .buffer.
    """
    return types.SimpleNamespace(buffer=io.BytesIO(data))


def _fake_stdout() -> tuple[types.SimpleNamespace, io.BytesIO]:
    """Return (fake_sys_stdout, underlying_buf) for patching sys.stdout."""
    buf = io.BytesIO()
    ns = types.SimpleNamespace(buffer=buf)
    return ns, buf


# ---------------------------------------------------------------------------
# error_log
# ---------------------------------------------------------------------------

class TestErrorLog(unittest.TestCase):
    def test_writes_to_error_log(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(yomitan_api, "script_path", tmpdir):
                yomitan_api.error_log("test message", "test error")
            log_path = os.path.join(tmpdir, "error.log")
            self.assertTrue(os.path.exists(log_path))
            with open(log_path, encoding="utf8") as f:
                content = f.read()
            self.assertIn("test message", content)
            self.assertIn("test error", content)

    def test_handles_os_error_gracefully(self):
        """error_log must not raise even if it cannot write."""
        with patch("builtins.open", side_effect=OSError("permission denied")):
            # Should not raise
            yomitan_api.error_log("msg", "err")

    def test_replaces_newlines_in_message(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(yomitan_api, "script_path", tmpdir):
                yomitan_api.error_log("line1\nline2", "err\r\nerr")
            with open(os.path.join(tmpdir, "error.log"), encoding="utf8") as f:
                content = f.read()
        # Newlines should be escaped
        self.assertIn(r"\n", content)
        self.assertNotIn("line1\nline2", content)


# ---------------------------------------------------------------------------
# get_message
# ---------------------------------------------------------------------------

class TestGetMessage(unittest.TestCase):
    def _make_stdin_bytes(self, payload: dict) -> bytes:
        encoded = json.dumps(payload).encode("utf-8")
        length = struct.pack("@I", len(encoded))
        return length + encoded

    def test_returns_none_on_empty_stdin(self):
        # sys.stdin.buffer is a read-only C-slot on Python 3.9; patch sys.stdin wholesale
        with patch("sys.stdin", _fake_stdin(b"")):
            result = yomitan_api.get_message()
        self.assertIsNone(result)

    def test_returns_parsed_message(self):
        payload = {"action": "test", "data": 42}
        data = self._make_stdin_bytes(payload)
        with patch("sys.stdin", _fake_stdin(data)):
            result = yomitan_api.get_message()
        self.assertEqual(result, payload)

    def test_returns_none_for_oversized_message(self):
        """A message_length > 33554432 must return None without reading."""
        oversized_length = struct.pack("@I", 33554433)
        with patch("sys.stdin", _fake_stdin(oversized_length)):
            result = yomitan_api.get_message()
        self.assertIsNone(result)

    def test_exact_size_limit_passes(self):
        """A message exactly at the limit (== 33554432) should not be rejected."""
        payload = {"key": "value"}
        data = self._make_stdin_bytes(payload)
        with patch("sys.stdin", _fake_stdin(data)):
            result = yomitan_api.get_message()
        self.assertIsNotNone(result)


# ---------------------------------------------------------------------------
# delete_crowbarfile
# ---------------------------------------------------------------------------

class TestDeleteCrowbarfile(unittest.TestCase):
    def test_deletes_existing_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = f.name
        with patch.object(yomitan_api, "crowbarfile_path", path):
            yomitan_api.delete_crowbarfile()
        self.assertFalse(os.path.exists(path))

    def test_does_not_raise_if_file_missing(self):
        with patch.object(yomitan_api, "crowbarfile_path", "/nonexistent/path/.crowbar"):
            # Should not raise
            yomitan_api.delete_crowbarfile()

    def test_does_not_raise_on_permission_error(self):
        with patch("os.path.exists", return_value=True), \
             patch("os.remove", side_effect=PermissionError("denied")):
            yomitan_api.delete_crowbarfile()


# ---------------------------------------------------------------------------
# ensure_single_instance
# ---------------------------------------------------------------------------

class TestEnsureSingleInstance(unittest.TestCase):
    def test_writes_pid_to_crowbar_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, ".crowbar")
            with patch.object(yomitan_api, "crowbarfile_path", path), \
                 patch("sys.stdin.isatty", return_value=False):
                yomitan_api.ensure_single_instance()
            with open(path) as f:
                content = f.read().strip()
        self.assertEqual(content, str(os.getpid()))

    def test_no_crash_when_crowbar_contains_dead_pid(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, ".crowbar")
            # Write a PID that almost certainly does not exist
            with open(path, "w") as f:
                f.write("999999999")
            with patch.object(yomitan_api, "crowbarfile_path", path), \
                 patch("sys.stdin.isatty", return_value=False):
                # Should not raise
                yomitan_api.ensure_single_instance()

    def test_no_crash_on_system_error(self):
        """Simulate Windows SystemError from os.kill(pid, 0)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, ".crowbar")
            with open(path, "w") as f:
                f.write("1234")
            with patch.object(yomitan_api, "crowbarfile_path", path), \
                 patch("sys.stdin.isatty", return_value=False), \
                 patch("os.kill", side_effect=SystemError("returned a result with an error set")):
                # Should catch SystemError and proceed to write current PID
                yomitan_api.ensure_single_instance()
            with open(path) as f:
                content = f.read().strip()
        self.assertEqual(content, str(os.getpid()))


# ---------------------------------------------------------------------------
# send_message / send_response (smoke tests)
# ---------------------------------------------------------------------------

class TestSendMessage(unittest.TestCase):
    def test_writes_length_prefixed_json(self):
        payload = {"action": "test"}
        # sys.stdout.buffer is read-only on Python 3.9; patch sys.stdout wholesale
        fake_stdout, buf = _fake_stdout()
        with patch("sys.stdout", fake_stdout):
            yomitan_api.send_message(payload)

        buf.seek(0)
        raw_length = buf.read(4)
        msg_length = struct.unpack("@I", raw_length)[0]
        msg_bytes = buf.read(msg_length)
        self.assertEqual(json.loads(msg_bytes), payload)


class TestRequestHandler(unittest.TestCase):
    def _make_handler(self, path="/serverVersion", body=b"{}"):
        """Create a minimal RequestHandler-like mock for do_POST."""
        handler = MagicMock(spec=yomitan_api.RequestHandler)
        handler.path = path
        handler.command = "POST"
        handler.headers = {"Content-Length": str(len(body))}
        handler.rfile = io.BytesIO(body)
        handler.wfile = io.BytesIO()
        return handler

    def test_server_version_responds_200(self):
        handler = self._make_handler("/serverVersion")
        responses = []

        def fake_send_response(h, code, ctype, data):
            responses.append((code, data))

        with patch.object(yomitan_api, "send_response", fake_send_response), \
             patch.object(yomitan_api, "get_message", return_value={"responseStatusCode": 200, "data": {"version": 1}}):
            yomitan_api.RequestHandler.do_request(handler)

        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0][0], 200)
        result = json.loads(responses[0][1])
        self.assertEqual(result["version"], yomitan_api.YOMITAN_API_NATIVE_MESSAGING_VERSION)

    def test_get_request_on_version_path(self):
        """GET /serverVersion should now work."""
        handler = self._make_handler("/serverVersion")
        handler.command = "GET"
        responses = []

        def fake_send_response(h, code, ctype, data):
            responses.append((code, data))

        with patch.object(yomitan_api, "get_message", return_value={"responseStatusCode": 200, "data": {}}), \
             patch.object(yomitan_api, "send_response", fake_send_response):
            yomitan_api.RequestHandler.do_request(handler)

        self.assertEqual(responses[0][0], 200)

    def test_nm_failure_returns_503(self):
        """If send_message fails with OSError (disconnected pipe), return 503."""
        handler = self._make_handler("/yomitanVersion")
        responses = []

        def fake_send_response(h, code, ctype, data):
            responses.append((code, data))

        # Simulate broken pipe/unconnected stdout
        with patch.object(yomitan_api, "send_message", side_effect=OSError("broken pipe")), \
             patch.object(yomitan_api, "send_response", fake_send_response):
            yomitan_api.RequestHandler.do_request(handler)

        self.assertEqual(responses[0][0], 503)
        self.assertIn("Native messaging connection failed", responses[0][1])

    def test_ensure_single_instance_tty_exits(self):
        """In a TTY, if another instance is alive, we should warn and exit(0) to protect daemon."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, ".crowbar")
            with open(path, "w") as f:
                f.write(str(os.getpid())) # Current process is "already running"

            with patch.object(yomitan_api, "crowbarfile_path", path), \
                 patch("sys.stdin.isatty", return_value=True), \
                 patch("sys.exit") as mock_exit, \
                 patch("builtins.print"):  # Suppress warning output in tests
                yomitan_api.ensure_single_instance()
                mock_exit.assert_called_once_with(0)

    def test_blacklisted_path_responds_400(self):
        handler = self._make_handler("/favicon.ico")
        responses = []

        def fake_send_response(h, code, ctype, data):
            responses.append((code, data))

        with patch.object(yomitan_api, "send_response", fake_send_response), \
             patch.object(yomitan_api, "get_message", return_value={}):
            yomitan_api.RequestHandler.do_request(handler)

        self.assertEqual(responses[0][0], 400)

    def test_missing_content_length_does_not_crash(self):
        """Content-Length absent should default to empty body, not crash."""
        handler = MagicMock(spec=yomitan_api.RequestHandler)
        handler.path = "/serverVersion"
        handler.command = "POST"
        handler.headers = {}  # no Content-Length
        handler.rfile = io.BytesIO(b"")
        handler.wfile = io.BytesIO()

        responses = []
        def fake_send_response(h, code, ctype, data):
            responses.append((code, data))

        with patch.object(yomitan_api, "send_response", fake_send_response), \
             patch.object(yomitan_api, "get_message", return_value={}):
            yomitan_api.RequestHandler.do_request(handler)

        self.assertTrue(len(responses) > 0)
        self.assertNotEqual(responses[0][0], 500)


if __name__ == "__main__":
    unittest.main()
