# `dictionaryInfo`

Returns the installed dictionaries, each with a summary as it is represented internally by Yomitan (title, revision, author, description, URL, styles and entry counts) and the options for the active profile (alias, whether it is enabled and how its definitions collapse). Yomitan shows the summary when a dictionary tag is clicked, and uses the frequency counts for the "Dictionary size" of frequency tags.

## Request Options

- Request method: `POST`

## Response Example (200)

The dictionaries are in the active profile's order. A dictionary the profile doesn't list yet comes at the bottom of the list with `options` set to `null`; lookups don't use it until it is added to the profile by the Settings page.

- The summary fields are the same in every profile. `styles` is the dictionary's CSS: Yomitan scopes it to the dictionary's entries (`[data-dictionary="<title>"]`) and adds it to the popup's custom CSS while the dictionary is enabled.

- `options`: The active profile's options for the dictionary.
    - `alias`: The name Yomitan shows for the dictionary, which is also the `dictionaryAlias` in lookup results. It's the same as the title unless it was changed in the settings.
    - `enabled`: Whether lookups use the dictionary.
    - `definitionsCollapsible`: One of `not-collapsible`, `expanded`, `collapsed`, `force-collapsed` and `force-expanded`.

Due to this being a data format used internally by Yomitan, no guarantees are made for the stability or accuracy of the responses. Long values are shortened (`…`) in this example.

```json
[
    {
        "title": "Jitendex.org [2026-10-03]",
        "revision": "2026.10.03.0",
        "sequenced": true,
        "version": 3,
        "importDate": 1794740076720,
        "prefixWildcardsSupported": false,
        "counts": {
            "terms": {"total": 436555},
            "termMeta": {"total": 0},
            "kanji": {"total": 0},
            "kanjiMeta": {"total": 0},
            "tagMeta": {"total": 8},
            "media": {"total": 236}
        },
        "styles": "span[title] {\n    cursor: help;\n}\n\nul[data-sc-content=\"sense-groups\"] {\n    list…",
        "importSuccess": true,
        "author": "Stephen Kraus",
        "url": "https://jitendex.org",
        "description": "Jitendex is updated with new content at least once a month. Click the 'Check for Updates' button in the Yomitan 'Diction…",
        "attribution": "© CC BY-SA 4.0 Stephen Kraus 2023-2026\n\nYou are free to use, modify, and redistr…",
        "sourceLanguage": "ja",
        "targetLanguage": "en",
        "isUpdatable": true,
        "indexUrl": "https://jitendex.org/static/yomitan.json",
        "downloadUrl": "https://github.com/stephenmk/stephenmk.github.io/releases/latest/download/jitendex-yomitan.zip",
        "options": {
            "alias": "Jitendex.org [2026-10-03]",
            "enabled": true,
            "definitionsCollapsible": "not-collapsible"
        }
    },
    {
        "title": "JPDBv2㋕",
        "revision": "JPDB v2.2 Frequency Kana 2024-10-13",
        "sequenced": false,
        "version": 3,
        "importDate": 1794740191591,
        "prefixWildcardsSupported": false,
        "counts": {
            "terms": {"total": 0},
            "termMeta": {"total": 338814, "freq": 338814},
            "kanji": {"total": 0},
            "kanjiMeta": {"total": 0},
            "tagMeta": {"total": 0},
            "media": {"total": 0}
        },
        "styles": "",
        "importSuccess": true,
        "author": "jpdb, Kuuube, Gecko",
        "url": "https://jpdb.io",
        "description": "Contains 99.99% of the JPDB corpus up to frequency 25000, 99.5% up to 70000, and 98.6% up to 100000.\n㋕ is used to indica…",
        "frequencyMode": "rank-based",
        "options": {
            "alias": "JPDBv2㋕",
            "enabled": true,
            "definitionsCollapsible": "not-collapsible"
        }
    }
]
```
