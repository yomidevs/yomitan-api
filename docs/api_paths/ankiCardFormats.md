# `ankiCardFormats`

Returns all card formats for the specified profile.

## Request Options

- Request method: `POST`

- Body:

    - `profileIndex` (`int`): (Optional) The profile index to fetch the Anki Card Formats. Uses the active profile by default.

## Request Example

- Request method: `POST`

- Body:
    ```json
    {
        "profileIndex": 0
    }
    ```

## Response Example (200)

```json
[
    {
        "name": "Expression",
        "icon": "big-circle",
        "deck": "Backlog",
        "model": "ExpressionModel",
        "fields": {
            "Expression": {
                "value": "{expression}",
                "overwriteMode": "coalesce"
            },
            "ExpressionFurigana": {
                "value": "{furigana-plain}",
                "overwriteMode": "coalesce"
            },
            "ExpressionReading": {
                "value": "{reading}",
                "overwriteMode": "coalesce"
            },
            "ExpressionAudio": {
                "value": "{audio}",
                "overwriteMode": "coalesce"
            },
            "SelectionText": {
                "value": "{popup-selection-text}",
                "overwriteMode": "coalesce"
            },
            "MainDefinition": {
                "value": "{glossary}",
                "overwriteMode": "coalesce"
            }
        },
        "type": "term"
    },
    {
        "name": "Reading",
        "icon": "small-circle",
        "deck": "Reading",
        "model": "ReadingModel",
        "fields": {
            "Expression": {
                "value": "{expression}",
                "overwriteMode": "coalesce"
            },
            "Definition": {
                "value": "{glossary}",
                "overwriteMode": "coalesce"
            }
        },
        "type": "term"
    },
    {
        "name": "Kanji",
        "icon": "big-circle",
        "deck": "Kanji",
        "model": "KanjiModel",
        "fields": {
            "Character": {
                "value": "{character}",
                "overwriteMode": "coalesce"
            },
            "Kunyomi": {
                "value": "{kunyomi}",
                "overwriteMode": "coalesce"
            },
            "Onyomi": {
                "value": "{onyomi}",
                "overwriteMode": "coalesce"
            },
            "Definition": {
                "value": "{glossary}",
                "overwriteMode": "coalesce"
            },
            "Frequency": {
                "value": "{frequencies}",
                "overwriteMode": "coalesce"
            }
        },
        "type": "kanji"
    }
]
```
