"""Tests for install_yomitan_api.py logic.

Only pure functions are tested here. Top-level interactive code (input(), registry
writes) is excluded by patching builtins.input to return "" and sys.platform before
importing the module.
"""

import copy
import json
import os
import sys
import types
import unittest
from unittest.mock import patch, mock_open, MagicMock

# ---------------------------------------------------------------------------
# Helpers to import only the pure functions without running interactive code
# ---------------------------------------------------------------------------

def _load_install_module():
    """Import install_yomitan_api with all side-effects suppressed."""
    # We need to inject a fake winreg before the import if on non-Windows
    if sys.platform != "win32":
        fake_winreg = types.ModuleType("winreg")
        sys.modules.setdefault("winreg", fake_winreg)

    with patch("builtins.input", return_value=""), \
         patch("sys.stdin.isatty", return_value=False):
        # Suppress print output during import
        with patch("builtins.print"):
            import importlib
            if "install_yomitan_api" in sys.modules:
                del sys.modules["install_yomitan_api"]
            mod = importlib.import_module("install_yomitan_api")
    return mod


class TestPlatformDataGet(unittest.TestCase):
    def setUp(self):
        self.mod = _load_install_module()

    def test_windows_win32(self):
        with patch.object(sys, "platform", "win32"):
            data = self.mod.platform_data_get()
        self.assertEqual(data["platform"], "windows")

    def test_linux(self):
        with patch.object(sys, "platform", "linux"):
            data = self.mod.platform_data_get()
        self.assertEqual(data["platform"], "linux")

    def test_linux2(self):
        with patch.object(sys, "platform", "linux2"):
            data = self.mod.platform_data_get()
        self.assertEqual(data["platform"], "linux")

    def test_darwin_mac(self):
        with patch.object(sys, "platform", "darwin"):
            data = self.mod.platform_data_get()
        self.assertEqual(data["platform"], "mac")

    def test_unsupported_platform_raises(self):
        with patch.object(sys, "platform", "haiku"):
            with self.assertRaises(Exception) as ctx:
                self.mod.platform_data_get()
        self.assertIn("Unsupported platform", str(ctx.exception))

    def test_startswith_matching(self):
        """freebsd variants should match linux platform_aliases via startswith."""
        with patch.object(sys, "platform", "freebsd7"):
            data = self.mod.platform_data_get()
        self.assertEqual(data["platform"], "linux")


class TestManifestGet(unittest.TestCase):
    def setUp(self):
        self.mod = _load_install_module()

    def test_chrome_manifest_structure(self):
        result = self.mod.manifest_get("chrome", "/fake/path", [])
        manifest = json.loads(result)
        self.assertEqual(manifest["name"], "yomitan_api")
        self.assertEqual(manifest["type"], "stdio")
        self.assertEqual(manifest["path"], "/fake/path")
        self.assertIn("allowed_origins", manifest)
        self.assertIsInstance(manifest["allowed_origins"], list)
        self.assertTrue(len(manifest["allowed_origins"]) > 0)

    def test_firefox_manifest_structure(self):
        result = self.mod.manifest_get("firefox", "/fake/path", [])
        manifest = json.loads(result)
        self.assertIn("allowed_extensions", manifest)
        self.assertNotIn("allowed_origins", manifest)

    def test_additional_ids_appended(self):
        result = self.mod.manifest_get("chrome", "/fake/path", ["chrome-extension://custom/"])
        manifest = json.loads(result)
        self.assertIn("chrome-extension://custom/", manifest["allowed_origins"])

    def test_does_not_mutate_template(self):
        """manifest_get must not mutate MANIFEST_TEMPLATE."""
        before = copy.deepcopy(self.mod.MANIFEST_TEMPLATE)
        self.mod.manifest_get("chrome", "/fake/path", ["extra"])
        self.assertEqual(self.mod.MANIFEST_TEMPLATE, before)

    def test_edge_uses_allowed_origins(self):
        result = self.mod.manifest_get("edge", "/fake/path", [])
        manifest = json.loads(result)
        self.assertIn("allowed_origins", manifest)

    def test_brave_uses_allowed_origins(self):
        result = self.mod.manifest_get("brave", "/fake/path", [])
        manifest = json.loads(result)
        self.assertIn("allowed_origins", manifest)


class TestManifestInstallFile(unittest.TestCase):
    def setUp(self):
        self.mod = _load_install_module()

    def test_file_written_with_correct_name(self):
        m = mock_open()
        with patch("os.makedirs") as mock_makedirs, patch("builtins.open", m):
            self.mod.manifest_install_file('{"test": true}', "/some/path", "yomitan_api_chrome.json")
        mock_makedirs.assert_called_once_with("/some/path", exist_ok=True)
        # check open was called with the right filename
        call_args = m.call_args[0]
        self.assertEqual(call_args[0], os.path.join("/some/path", "yomitan_api_chrome.json"))

    def test_file_content_written(self):
        content = '{"name": "yomitan_api"}'
        m = mock_open()
        with patch("os.makedirs"), patch("builtins.open", m):
            self.mod.manifest_install_file(content, "/some/path", "yomitan_api.json")
        handle = m()
        handle.write.assert_called_once_with(content)


class TestWindowsRegistryPath(unittest.TestCase):
    """Ensure all Windows browsers have a registry_path defined."""

    def setUp(self):
        self.mod = _load_install_module()

    def test_chromium_has_registry_path(self):
        win_data = self.mod.PLATFORM_DATA["windows"]["manifest_install_data"]
        self.assertIn("registry_path", win_data["chromium"])

    def test_all_windows_browsers_have_registry_path(self):
        win_data = self.mod.PLATFORM_DATA["windows"]["manifest_install_data"]
        for browser, data in win_data.items():
            with self.subTest(browser=browser):
                self.assertIn("registry_path", data, f"{browser} missing registry_path")

    def test_registry_paths_contain_name(self):
        win_data = self.mod.PLATFORM_DATA["windows"]["manifest_install_data"]
        for browser, data in win_data.items():
            with self.subTest(browser=browser):
                self.assertIn("yomitan_api", data["registry_path"])


if __name__ == "__main__":
    unittest.main()
