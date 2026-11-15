# `dictionaryMedia`

Returns media files (such as images) from dictionaries. Entries from `/termEntries` and `/kanjiEntries` refer to them in their structured content, by dictionary and path.

## Request Options

- Request method: `POST`

- Body:

    - `targets` (`array<object>`): The files to return.

        - `dictionary` (`string`): The title of the dictionary the file is in.

        - `path` (`string`): The path of the file in the dictionary.

## Request Example

- Request method: `POST`

- Body:
    ```json
    {
        "targets": [
            {
                "dictionary": "Test Dictionary",
                "path": "image.gif"
            }
        ]
    }
    ```

## Response Example (200)

The files that were found, with their content in base64. Files that are not found are left out. The content is shortened (`…`) in this example.

```json
[
    {
        "content": "R0lGODdhBwAHAIABAAAAAP///ywAAAAABwAHAAAC…",
        "dictionary": "Test Dictionary",
        "height": 7,
        "mediaType": "image/gif",
        "path": "image.gif",
        "width": 7
    }
]
```
