#!/usr/bin/env -S python3 -u

import copy
import json
import os
import shutil
import sys
from typing import Any

DIR = os.path.realpath(os.path.dirname(__file__))

NAME = "yomitan_api"

MANIFEST_TEMPLATE: dict[str, Any] = {
    "name": "yomitan_api",
    "description": "Yomitan API",
    "type": "stdio",
}

BROWSER_DATA = {
    "firefox": {
        "extension_id_key": "allowed_extensions",
        "extension_ids": ["{6b733b82-9261-47ee-a595-2dda294a4d08}"],
    },
    "chrome": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
    },
    "chromium": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
    },
    "edge": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
    },
    "brave": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
    },
}

PLATFORM_DATA = {
    "linux": {
        "platform_aliases": [
            "linux",
            "linux2",
            "riscos",
            "freebsd7",
            "freebsd8",
            "freebsdN",
            "openbsd6",
        ],
        "manifest_install_data": {
            "firefox": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.mozilla/native-messaging-hosts/"),
            },
            "chrome": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/.config/google-chrome/NativeMessagingHosts/"
                ),
            },
            "chromium": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.config/chromium/NativeMessagingHosts/"),
            },
            "brave": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/.config/BraveSoftware/Brave-Browser/NativeMessagingHosts/"
                ),
            },
        },
    },
    "windows": {
        "platform_aliases": ["win32", "cygwin"],
        "manifest_install_data": {
            "firefox": {
                "methods": ["file", "registry"],
                "path": DIR,
                "registry_path": f"SOFTWARE\\Mozilla\\NativeMessagingHosts\\{NAME}",
            },
            "chrome": {
                "methods": ["file", "registry"],
                "path": DIR,
                "registry_path": f"SOFTWARE\\Google\\Chrome\\NativeMessagingHosts\\{NAME}",
            },
            "chromium": {
                "methods": ["file", "registry"],
                "path": DIR,
                "registry_path": f"SOFTWARE\\Chromium\\NativeMessagingHosts\\{NAME}",
            },
            "edge": {
                "methods": ["file", "registry"],
                "path": DIR,
                "registry_path": f"SOFTWARE\\Microsoft\\Edge\\NativeMessagingHosts\\{NAME}",
            },
            "brave": {
                "methods": ["file", "registry"],
                "path": DIR,
                "registry_path": f"SOFTWARE\\BraveSoftware\\Brave-Browser\\NativeMessagingHosts\\{NAME}",
            },
        },
    },
    "mac": {
        "platform_aliases": ["darwin"],
        "manifest_install_data": {
            "firefox": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/Library/Application Support/Mozilla/NativeMessagingHosts/"
                ),
            },
            "chrome": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/Library/Application Support/Google/Chrome/NativeMessagingHosts/"
                ),
            },
            "chromium": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/Library/Application Support/Chromium/NativeMessagingHosts/"
                ),
            },
            "brave": {
                "methods": ["file"],
                "path": os.path.expanduser(
                    "~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts/"
                ),
            },
        },
    },
}


def platform_data_get() -> dict:
    for platform_name in PLATFORM_DATA:
        data = copy.deepcopy(PLATFORM_DATA[platform_name])
        data["platform"] = platform_name
        if any(sys.platform.startswith(alias) for alias in data["platform_aliases"]):
            return data
    msg = f"Unsupported platform: {sys.platform}"
    raise Exception(msg)


def manifest_get(browser: str, messaging_host_path: str, additional_ids: list) -> str:
    manifest: dict[str, Any] = copy.deepcopy(MANIFEST_TEMPLATE)
    data = BROWSER_DATA[browser]
    manifest["path"] = messaging_host_path

    # Directly assign the combined list to avoid Pylance append errors
    manifest[data["extension_id_key"]] = data["extension_ids"] + additional_ids

    return json.dumps(manifest, indent=4)


def manifest_install_file(manifest: str, path: str, filename: str) -> None:
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename), "w") as f:
        f.write(manifest)


def main() -> None:
    platform_data = platform_data_get()

    browsers = list(platform_data["manifest_install_data"].keys())

    if platform_data["platform"] == "windows" and "WindowsApps" in sys.executable:
        print("-" * 50)
        print("WARNING: You are using Python from the Windows Store.")
        print("This version is unsuitable for initial setup because")
        print("it fails to write to the registry due to sandboxing.")
        print()
        print("However, it is suitable for running the API server")
        print("once the registry has been configured using a standard")
        print("Python installation from python.org.")
        print("-" * 50)
        print()

    print("0: all (recommended)")
    for i, browser in enumerate(browsers):
        print(f"{i + 1}: {browser}")

    choice = input("Choose browser (default 0): ").strip()
    selected_browsers = (
        browsers if not choice or choice == "0" else [browsers[int(choice) - 1]]
    )

    print("\nUsing default Yomitan extension IDs.")
    print("Add more extension IDs, or press enter to continue")
    additional_extension_ids: list[str] = []
    while True:
        extension_id = input("Extension ID: ").strip()
        if not extension_id:
            break
        additional_extension_ids.append(extension_id)

    script_path = os.path.join(DIR, "yomitan_api.py")

    if platform_data["platform"] == "windows":
        bat_path = os.path.join(DIR, "yomitan_api.bat")

        # Bypass Windows Store Python app execution alias restrictions
        py_exec = "python" if "WindowsApps" in sys.executable else sys.executable

        with open(bat_path, "w") as f:
            f.write(f'@echo off\n"{py_exec}" -u "{script_path}"')
        script_path = bat_path

    # Fix macOS user dictionary permission issue
    if platform_data["platform"] == "mac":
        mac_install_path = platform_data["manifest_install_data"][selected_browsers[0]][
            "path"
        ]
        script_path = os.path.join(mac_install_path, "yomitan_api.py")
        try:
            os.makedirs(mac_install_path, exist_ok=True)
            shutil.copy(os.path.join(DIR, "yomitan_api.py"), script_path)
            os.chmod(
                script_path, 0o755
            )  # Make executable, crucial for macOS Native Messaging
            print(
                f'File copied from {os.path.join(DIR, "yomitan_api.py")} to {script_path}'
            )
        except Exception as e:
            print(f"An error occurred during copying: {e}")

    for browser in selected_browsers:
        manifest_install_data = platform_data["manifest_install_data"][browser]
        manifest = manifest_get(browser, script_path, additional_extension_ids)

        # Prevent overwriting JSON on Windows if installing for multiple browsers
        manifest_filename = (
            f"{NAME}_{browser}.json"
            if platform_data["platform"] == "windows"
            else f"{NAME}.json"
        )

        for method in manifest_install_data["methods"]:
            if method == "file":
                try:
                    manifest_install_file(
                        manifest, manifest_install_data["path"], manifest_filename
                    )
                    print(f"[{browser}] Manifest file created.")
                except Exception as e:
                    print(f"[{browser}] Failed to create manifest: {e}")

            if method == "registry":
                import winreg

                try:
                    winreg.CreateKey(
                        winreg.HKEY_CURRENT_USER, manifest_install_data["registry_path"]
                    )
                    with winreg.OpenKey(
                        winreg.HKEY_CURRENT_USER,
                        manifest_install_data["registry_path"],
                        0,
                        winreg.KEY_WRITE,
                    ) as registry_key:
                        winreg.SetValueEx(
                            registry_key,
                            "",
                            0,
                            winreg.REG_SZ,
                            os.path.join(manifest_install_data["path"], manifest_filename),
                        )
                    print(f"[{browser}] Registry key added successfully.")
                except Exception as e:
                    print(f"[{browser}] Failed to add registry key: {e}")

    print("\nInstallation complete. Please restart your browser.")


if __name__ == "__main__":
    main()
