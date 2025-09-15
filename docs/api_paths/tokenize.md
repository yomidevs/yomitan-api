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
    "text": "自民党の臨時の総裁選挙が実施されるかどうか",
    "scanLength": 10
}
```

## Response Example (200)

The response contains an array with parsing results from Yomitan's internal `parseText` method. Each element in the content array represents a parsed segment with its reading(s) and text.

```json
[
  {
    "content": [
      [{ "reading": "じみんとう", "text": "自民党"}],
      [{ "reading": "", "text": "の"}],
      [{ "reading": "りんじ", "text": "臨時"}],
      [{ "reading": "", "text": "の"}],
      [{ "reading": "そうさい", "text": "総裁"}],
      [{ "reading": "せん", "text": "選"}],
      [{ "reading": "きょ", "text": "挙"}],
      [{ "reading": "", "text": "が"}],
      [{ "reading": "じっし", "text": "実施"}],
      [{ "reading": "", "text": "される"}],
      [{ "reading": "", "text": "かどうか"}],
    ],
    "dictionary": null,
    "id": "scan",
    "source": "scanning-parser"
  }
]
```
