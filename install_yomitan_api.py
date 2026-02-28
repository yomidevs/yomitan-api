#!/usr/bin/env -S python3 -u

import copy
import json
import os
import shutil
import sys
import re

DIR = os.path.realpath(os.path.dirname(__file__))

NAME = "yomitan_api"

MANIFEST_TEMPLATE = {
    "name": "yomitan_api",
    "description": "Yomitan API",
    "type": "stdio",
}

BROWSER_DATA = {
    "firefox": {
        "extension_id_key": "allowed_extensions",
        "extension_ids": ["{6b733b82-9261-47ee-a595-2dda294a4d08}"],
        "extension_id_format": r"{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx} or testextension@example.com",
        "regex_test": r"(?:\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}|[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+)"
    },
    "chrome": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
        "extension_id_format": "chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/",
        "regex_test": r"chrome-extension:\/\/[a-p]{32}\/"
    },
    "chromium": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
        "extension_id_format": "chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/",
        "regex_test": r"chrome-extension:\/\/[a-p]{32}\/"
    },
    "edge": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
        "extension_id_format": "chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/",
        "regex_test": r"chrome-extension:\/\/[a-p]{32}\/"
    },
    "brave": {
        "extension_id_key": "allowed_origins",
        "extension_ids": ["chrome-extension://likgccmbimhjbgkjambclfkhldnlhbnn/"],
        "extension_id_format": "chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/",
        "regex_test": r"chrome-extension:\/\/[a-p]{32}\/"
    },
}

PLATFORM_DATA = {
    "linux": {
        "platform_aliases": ["linux", "linux2", "riscos", "freebsd7", "freebsd8", "freebsdN", "openbsd6"],
        "manifest_install_data": {
            "firefox": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.mozilla/native-messaging-hosts/"),
            },
            "chrome": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.config/google-chrome/NativeMessagingHosts/"),
            },
            "chromium": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.config/chromium/NativeMessagingHosts/"),
            },
            "brave": {
                "methods": ["file"],
                "path": os.path.expanduser("~/.config/BraveSoftware/Brave-Browser/NativeMessagingHosts/"),
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
                "path": os.path.expanduser("~/Library/Application Support/Mozilla/NativeMessagingHosts/"),
            },
            "chrome": {
                "methods": ["file"],
                "path": os.path.expanduser("~/Library/Application Support/Google/Chrome/NativeMessagingHosts/"),
            },
            "chromium": {
                "methods": ["file"],
                "path": os.path.expanduser("~/Library/Application Support/Chromium/NativeMessagingHosts/"),
            },
            "brave": {
                "methods": ["file"],
                "path": os.path.expanduser("~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts/"),
            },
        },
    },
}

def valid_extension_id(browser:str, extension_id:str) -> bool:
    return bool(re.fullmatch(BROWSER_DATA[browser]["regex_test"], extension_id))

def platform_data_get() -> dict:
    for platform_name in PLATFORM_DATA:
        data = copy.deepcopy(PLATFORM_DATA[platform_name])
        data["platform"] = platform_name
        if sys.platform in data["platform_aliases"]:
            return data
    msg = f"Unsupported platform: {sys.platform}"
    raise Exception(msg)  # noqa: TRY002

def manifest_get(browser: dict, messaging_host_path: str, additional_ids: list) -> str:
    manifest = copy.deepcopy(MANIFEST_TEMPLATE)
    data = BROWSER_DATA[browser]
    manifest["path"] = messaging_host_path
    manifest[data["extension_id_key"]] = []
    for extension_id in data["extension_ids"] + additional_ids:
        manifest[data["extension_id_key"]].append(extension_id)
    return json.dumps(manifest, indent=4)

def manifest_install_file(manifest: str, path: str) -> None:
    os.makedirs(path, exist_ok = True)
    with open(os.path.join(path, NAME + ".json"), "w") as f:
        f.write(manifest)

platform_data = platform_data_get()

# choose browser
browsers = list(platform_data["manifest_install_data"].keys())
for i, browser in enumerate(browsers):
    print(f"{i + 1}: {browser}")
browser = browsers[int(input("Choose browser: ")) - 1]

expected_extension_id_format = BROWSER_DATA[browser]["extension_id_format"]

# generate manifest
print()
print(f"Using default Yomitan extension ID for {browser}.")
print(f"Input extension IDs in the following format: `{expected_extension_id_format}`")
print("Add more extension IDs, or press enter to continue")
additional_extension_ids = []
while True:
    extension_id = input("Extension ID: ")
    if not extension_id:
        break
    
    if not valid_extension_id(browser, extension_id):
        print(f"Invalid extension ID! Please provide extension ID in the following format: `{expected_extension_id_format}`")
        continue

    additional_extension_ids.append(extension_id)
script_path = os.path.join(DIR, "yomitan_api.py")
if platform_data["platform"] == "windows":
    bat_path = os.path.join(DIR, "yomitan_api.bat")
    with open(bat_path, "w") as f:
        f.write(f'@echo off\n"{sys.executable}" -u "{script_path}"')
    script_path = bat_path
manifest_install_data = platform_data["manifest_install_data"][browser]
# fix macOS user dictionary permission issue
if platform_data["platform"] == "mac":
    script_path = os.path.join(manifest_install_data["path"], "yomitan_api.py")
    try:
        shutil.copy(os.path.join(DIR, "yomitan_api.py"), script_path)
        print(f'File copied from {os.path.join(DIR, "yomitan_api.py")} to {script_path}')
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:  # noqa: BLE001
        print(f"An error occurred: {e}")
manifest = manifest_get(browser, script_path, additional_extension_ids)
for method in manifest_install_data["methods"]:
    if method == "file":
        manifest_install_file(manifest, manifest_install_data["path"])
    if method == "registry":
        import winreg

        winreg.CreateKey(winreg.HKEY_CURRENT_USER, manifest_install_data["registry_path"])
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, manifest_install_data["registry_path"], 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "", 0, winreg.REG_SZ, os.path.join(manifest_install_data["path"], NAME + ".json"))
        winreg.CloseKey(registry_key)
