# `ankiFields`

Returns rendered Anki handlebars for dictionary entries found for search text.

## Request Options

- Request method: `POST`

- Body:

    - `text` (`string`): Contains the text to search for.

    - `type` (`string`): The type of dictionary to search in: `term` or `kanji`.

    - `markers` (`array<string>`): The markers (often called handlebars) to return. Do not include handlebars brackets (`{}`).

        A list of available handlebars can be found in Yomitan's settings. Open the settings, navigate to the `Anki` category, open `Configure Anki flashcards…`, and click `Help`.

        The Yomitan Wiki also has a list on the [Anki page](https://yomitan.wiki/anki/) under `Markers for Term Cards` or `Markers for Kanji Cards`.

    - `maxEntries` (`int`): The number of search entries to render markers for.

    - `includeMedia` (`bool`): Whether to return data such as images and audio.

    - `profileIndex` (`int`): (Optional) The profile whose dictionaries, Anki field templates and audio sources are used. Uses the active profile by default.

## Request Example

- Request method: `POST`

- Body:
    ```json
    {
        "text": "わかる",
        "type": "term",
        "markers": ["expression", "glossary", "audio"],
        "maxEntries": 2,
        "includeMedia": true
    }
    ```

## Response Example (200)

Glossary and media content have been truncated in this example.

Media content is provided in base64 encoding.

```json
{
    "fields": [
        {
            "expression": "分かる",
            "glossary": "<div style=\"text-align: left;\" class=\"yomitan-glossary\"><i>(priority form, ★, Jitendex.org [2025-05-13])</i> <span><ul style=\"list-style-type:&quot;＊&quot;\" lang=\"ja\"><li><span title=\"Godan verb with 'ru' ending\"...",
            "audio": "[sound:yomitan_audio_2025-06-12-04-12-35-107.mp3]"
        },
        {
            "expression": "解る",
            "glossary": "<div style=\"text-align: left;\" class=\"yomitan-glossary\"><i>(priority form, ★, Jitendex.org [2025-05-13])</i> <span><ul style=\"list-style-type:&quot;＊&quot;\" lang=\"ja\"><li><span title=\"Godan verb with 'ru' ending\"...",
            "audio": "[sound:yomitan_audio_2025-06-12-04-12-35-107.mp3]"
        }
    ],
    "dictionaryMedia": [
        {
            "dictionary": "Example Dictionary",
            "path": "assets/dictionary-logo.png",
            "mediaType": "image/png",
            "width": 180,
            "height": 180,
            "content": "iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAMAAAAKE...",
            "ankiFilename": "yomitan_dictionary_media_0_2025-06-12-02-45-04-307.png"
        }
    ],
    "audioMedia": [
        {
            "term": "分かる",
            "reading": "わかる",
            "mediaType": "audio/mpeg",
            "content": "//OExAAAAAAAAAAAAFhpbmcAAAAPAAAAIQAACLgA...",
            "ankiFilename": "yomitan_audio_2025-06-12-04-12-35-107.mp3"
        }
    ]
}
```
