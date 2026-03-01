# Yomitan API

[![Version](https://img.shields.io/badge/version-v1.1.3-blue)](https://github.com/Kuuuube/yomitan-api) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

The Yomitan API provides a native messaging host that allows Yomitan to interact with your local system.

## Table of Contents

- [Yomitan API](#yomitan-api)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [How to find your extension ID](#how-to-find-your-extension-id)
  - [API Paths](#api-paths)
  - [Examples](#examples)
  - [Tests](#tests)
  - [Troubleshooting](#troubleshooting)
    - [Windows: API not detected after installation](#windows-api-not-detected-after-installation)
    - [Windows: Installation fails or Registry keys missing with Windows Store Python](#windows-installation-fails-or-registry-keys-missing-with-windows-store-python)
    - [Windows: `ValueError: cannot read more than 33554432 bytes`](#windows-valueerror-cannot-read-more-than-33554432-bytes)
  - [Release Notes](#release-notes)
  - [License](#license)

---

## Installation

1. Install Python.

    - Windows: https://www.python.org/downloads/

        **On the first page of the installer, make sure to check `Add Python 3.x to PATH`.**

    - Mac: Install [Homebrew](https://brew.sh/) and run `brew install python3`.

    - Linux: Python is included in almost all distributions.

2. [Download](https://github.com/Kuuuube/yomitan-api/archive/master.zip) and extract this repository to the location you wish to install the files.

3. Run `python install_yomitan_api.py` and follow the prompts. Choose `0` (all browsers, recommended) or a specific browser by number. If you do not see any errors, it has successfully installed. **Note: Administrator privileges are normally not required**, as the installer writes to the current user's registry hive (`HKEY_CURRENT_USER`).

    **On forks of browsers such as Brave, you may need to install the API onto Chrome as well.**

    **If you have built Yomitan from source, please refer to the [How to find your extension ID](#how-to-find-your-extension-id) section below.**

4. Go to the Yomitan settings page on your browser.

5. Enable advanced options by clicking the toggle switch in the bottom left corner.

6. Go to `General` and enable `Enable Yomitan API`. Yomitan will automatically start the API every time you open your browser when this setting is enabled.

7. Click `More...` and click the `Test` button to see if the Yomitan API was installed correctly. You may need to wait a few seconds after enabling the setting for the native messaging component to start up.

[Return to Top](#table-of-contents)

## How to find your extension ID

If you have built Yomitan from source, you need to obtain the extension ID for Yomitan. If you reinstall Yomitan, you may need to get the extension ID again.

- Chrome/Chromium/Edge:

    - Open up your Yomitan settings page. The URL should look something like this:

        ![image](./docs/images/chrome_extension_id.png)

        Note: On Edge, the prefix will be `extension://`. **Make sure to change this to `chrome-extension://`, otherwise it will not work.**

    - Copy everything before `settings.html`. For example: `chrome-extension://mbclianmdhnmblbfecpefmgjhajbioip/`.

        **Make sure to remember the `chrome-extension://` AND the `/` at the end of the ID!!**

    - Rerun the script as seen above and when it displays `Add more extension IDs`, paste the extension ID URL that you got. It should work. Continue with the tutorial.

- Firefox:

    - Go to `about:debugging`, then select `This Firefox` at the sidebar.

    - Scroll until you find Yomitan. It should look like this:

        ![image](./docs/images/firefox_extension_id.png)

    - Copy the `Extension ID`. For example: `{2d13e145-294e-4ead-9bce-b4644b203a00}`.

    - Rerun the script as seen above and when it displays `Add more extension IDs`, paste the extension ID **with the brackets** in the input. It should work. Continue with the tutorial.

[Return to Top](#table-of-contents)

## API Paths

By default, the api is hosted on `http://127.0.0.1:19633`. To change this, edit `ADDR` and `PORT` in `yomitan_api.py`.

- [/serverVersion](./docs/api_paths/serverVersion.md)

- [/yomitanVersion](./docs/api_paths/yomitanVersion.md)

- [/termEntries](./docs/api_paths/termEntries.md)

- [/kanjiEntries](./docs/api_paths/kanjiEntries.md)

- [/ankiFields](./docs/api_paths/ankiFields.md)

- [/tokenize](./docs/api_paths/tokenize.md)

[Return to Top](#table-of-contents)

## Examples

[Yomitan API Request Example Python](./request_example.py)

[Return to Top](#table-of-contents)

## Tests

This project includes internal unit tests for both the installer and the API server to ensure reliability across platforms.

To run the tests, execute:

```bash
python -m unittest discover -s tests -v
```

[Return to Top](#table-of-contents)

## Troubleshooting

### Windows: API not detected after installation

If the Yomitan settings page shows "Failed to fetch" after running the installer:

1. **Re-run the installer** — make sure to run it with a standard Python install (not Windows Store Python, see below). The installer will prompt `Choose browser (default 0):` — press Enter to install for all browsers at once.

2. **Check the registry** — open `regedit` and verify that `HKEY_CURRENT_USER\SOFTWARE\<Browser>\NativeMessagingHosts\yomitan_api` exists and its `(Default)` value points to the correct `.json` file. If the key is missing after running the script, Check your antivirus or permissions for the script folder itself.

3. **Restart your browser** after installation.

### Windows: Installation fails or Registry keys missing with Windows Store Python

If Python was installed from the Microsoft Store (`WindowsApps\...` in `sys.executable`):
1. **Registry Write Failures**: Due to the UWP sandbox, the Windows Store version of Python fails to write the necessary registry keys even when run as administrator. This makes it **unsuitable for the initial setup** (`install_yomitan_api.py`).
2. **Launch Suitability**: Once the registry keys are correctly set up (using a standard Python install), the Windows Store version is **perfectly suitable for running** the API server (`yomitan_api.py`).
3. **Launch Failures**: The automated `.bat` file generation includes workarounds for Store Python App Execution Alias restrictions.

**Recommendation**: Use a standard version of Python from [python.org](https://www.python.org/downloads/) for the initial installation. Once installed, you can use any Python version to run the API.

### Windows: `ValueError: cannot read more than 33554432 bytes`

This error appears in an old version of `yomitan_api.py`. Update to v1.1.3 — it includes a guard that returns `None` instead of attempting the oversized read.

[Return to Top](#table-of-contents)

## Release Notes

[release-notes.md](./release-notes.md)

[Return to Top](#table-of-contents)

## License

[GPL v3](./LICENSE)

[Return to Top](#table-of-contents)
