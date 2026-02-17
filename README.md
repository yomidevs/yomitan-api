# Yomitan API

## Installation

1. Install Python.

    - Windows: https://www.python.org/downloads/

        **On the first page of the installer, make sure to check `Add Python 3.x to PATH`.**

    - Mac: Install [Homebrew](https://brew.sh/) and run `brew install python3`.

    - Linux: Python is included in almost all distributions.

2. [Download](https://github.com/Kuuuube/yomitan-api/archive/master.zip) and extract this repository to the location you wish to install the files.

3. Run `python install_yomitan_api.py` and follow the prompts. If you do not see any errors, it has successfully installed.

    **On forks of browsers such as Brave, you may need to install the API onto Chrome as well.**

    **If you have built Yomitan from source, please refer to the [How to find your extension ID](#how-to-find-your-extension-id) section below.**

4. Go to the Yomitan settings page on your browser.

5. Enable advanced options by clicking the toggle switch in the bottom left corner.

6. Go to `General` and enable `Enable Yomitan API`. Yomitan will automatically start the API every time you open your browser when this setting is enabled.

7. Click `More...` and click the `Test` button to see if the Yomitan API was installed correctly. You may need to wait a few seconds after enabling the setting for the native messaging component to start up.

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

## API Paths

By default, the api is hosted on `http://127.0.0.1:19633`. To change this, edit `ADDR` and `PORT` in `yomitan_api.py`.

- [/serverVersion](./docs/api_paths/serverVersion.md)

- [/yomitanVersion](./docs/api_paths/yomitanVersion.md)

- [/termEntries](./docs/api_paths/termEntries.md)

- [/kanjiEntries](./docs/api_paths/kanjiEntries.md)

- [/ankiFields](./docs/api_paths/ankiFields.md)

- [/tokenize](./docs/api_paths/tokenize.md)

## Examples

[Yomitan API Request Example Python](./request_example.py)
