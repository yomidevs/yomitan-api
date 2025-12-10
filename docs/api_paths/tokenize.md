# `tokenize`

Returns tokenized text segments for input text, including readings.

## Request Options

- Request method: `POST`

- Body:

    - `text` (`string`): The text to tokenize and parse.

    - `scanLength` (`number`): Maximum length to scan for each segment. Lower values provide faster processing while higher values can capture longer compound words.

## Request Example

```json
{
    "text": "ヨナグニサンはすごく大きいとかわいい、ガの触角最高",
    "scanLength": 10
}
```

## Response Example (200)

The response contains an array with parsing results from Yomitan's internal `parseText` method. Each element in the content array represents a parsed segment with its reading(s) and text.

```json
[
    {
        "id": "scan",
        "source": "scanning-parser",
        "dictionary": null,
        "content": [
            [
                {
                    "text": "ヨナグニサン",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "はす",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "ごく",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "大",
                    "reading": "おお"
                },
                {
                    "text": "きい",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "とか",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "わい",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "い",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "、",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "ガ",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "の",
                    "reading": ""
                }
            ],
            [
                {
                    "text": "触角",
                    "reading": "しょっかく"
                }
            ],
            [
                {
                    "text": "最高",
                    "reading": "さいこう"
                }
            ]
        ]
    }
]
```
