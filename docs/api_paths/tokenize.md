# `tokenize`

Returns tokenized text segments for input text, including readings.

## Request Options

- Request method: `POST`

- Body:

    - `text` (`string|array<string>`): The text to tokenize and parse. If an array is provided, each element will be processed concurrently.

    - `scanLength` (`number`): Maximum length to scan for each segment. Lower values provide faster processing while higher values can capture longer compound words.

## Request Example

```json
{
    "text": "ヨナグニサンはすごく大きいとかわいい、ガの触角最高",
    "scanLength": 10
}
```

## Response Example (200)

The response contains an array with parsing results from Yomitan's internal `parseText` method. For each result, the `index` corresponds to the index of the input text array or `0` if a string was provided.

Each element in the content array represents a parsed segment with its reading(s) and text. The first segment of each content array entry will contain the filtered `headwords` (a partial of `/termEntries`) from all dictionaryEntries if available. This field will only contain the `term`, `reading`, `sources`, and `frequencies` where the sources are limited to `isPrimary: true`, `matchType: "exact"`, and `originalText` matching the joined text segments. The `frequencies` are from `TermDictionaryEntry.frequencies` for this `headword`. The `headwords` field will be omitted if there are no sources matching the criteria.

Note: Only a single truncated `headwords` field is shown as an example, all items in content here would have this field on its first segment entry.

```json
[
    {
        "id": "scan",
        "source": "scanning-parser",
        "dictionary": null,
        "index": 0,
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
                    "reading": "おお",
                    "headwords": [
                        [
                            {
                                "term": "大きい",
                                "reading": "おおきい",
                                "sources": [
                                    {
                                        "deinflectedText": "大きい",
                                        "isPrimary": true,
                                        "matchSource": "term",
                                        "matchType": "exact",
                                        "originalText": "大きい",
                                        "transformedText": "大きい"
                                    }
                                ],
                                "frequencies": [
                                    {
                                        "index": 0, // Not meaningful in this context
                                        "headwordIndex": 0, // Not meaningful in this context
                                        "dictionary": "JPDBv2㋕",
                                        "dictionaryIndex": 2,
                                        "dictionaryAlias": "JPDBv2㋕",
                                        "hasReading": true,
                                        "frequencyMode": "rank-based",
                                        "frequency": 455,
                                        "displayValue": "455㋕",
                                        "displayValueParsed": false
                                    },
                                    {
                                        "index": 2, // Not meaningful in this context
                                        "headwordIndex": 0, // Not meaningful in this context
                                        "dictionary": "BCCWJ",
                                        "dictionaryIndex": 3,
                                        "dictionaryAlias": "BCCWJ",
                                        "hasReading": true,
                                        "frequencyMode": "rank-based",
                                        "frequency": 85,
                                        "displayValue": null,
                                        "displayValueParsed": false
                                    },
                                ]
                            }
                        ]
                    ]
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
