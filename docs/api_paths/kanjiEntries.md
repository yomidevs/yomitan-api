# `kanjiEntries`

Returns kanji dictionary entries for search text as they are represented internally by Yomitan.

## Request Options

- Request method: `POST`

- Body:

    - `character` (`string`): The character to return data for.

    - `profileIndex` (`int`): (Optional) The profile whose dictionaries are searched. Uses the active profile by default.

## Request Example

- Request method: `POST`

- Body:
    ```json
    {
        "character": "分"
    }
    ```

## Response Example (200)

Due to this being a data format used internally by Yomitan, no guarantees are made for the stability or accuracy of the responses.

<details>
<summary>Expand to view response</summary>

```json
[
  {
    "type": "kanji",
    "character": "分",
    "dictionary": "KANJIDIC [2025-145]",
    "dictionaryIndex": 1,
    "dictionaryAlias": "KANJIDIC [2025-145]",
    "onyomi": [
      "ブン",
      "フン",
      "ブ"
    ],
    "kunyomi": [
      "わ.ける",
      "わ.け",
      "わ.かれる",
      "わ.かる",
      "わ.かつ"
    ],
    "tags": [
      {
        "name": "jouyou",
        "category": "frequent",
        "order": -5,
        "score": 0,
        "content": [
          "included in list of regular-use characters"
        ],
        "dictionaries": [
          "KANJIDIC [2025-145]"
        ],
        "redundant": false
      }
    ],
    "stats": {
      "index": [
        {
          "name": "gakken",
          "category": "index",
          "content": "A  New Dictionary of Kanji Usage",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "35"
        },
        {
          "name": "henshall3",
          "category": "index",
          "content": "A Guide To Reading and Writing Japanese",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "218"
        },
        {
          "name": "sakade",
          "category": "index",
          "content": "A Guide To Reading and Writing Japanese",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "133"
        },
        {
          "name": "henshall",
          "category": "index",
          "content": "A Guide To Remembering Japanese Characters",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "199"
        },
        {
          "name": "moro",
          "category": "index",
          "content": "Daikanwajiten",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "1853"
        },
        {
          "name": "oneill_kk",
          "category": "index",
          "content": "Essential Kanji",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "35"
        },
        {
          "name": "busy_people",
          "category": "index",
          "content": "Japanese For Busy People",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2.2"
        },
        {
          "name": "jf_cards",
          "category": "index",
          "content": "Japanese Kanji Flashcards",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "22"
        },
        {
          "name": "oneill_names",
          "category": "index",
          "content": "Japanese Names",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "64"
        },
        {
          "name": "sh_kk",
          "category": "index",
          "content": "Kanji and Kana",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "38"
        },
        {
          "name": "sh_kk2",
          "category": "index",
          "content": "Kanji and Kana",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "38"
        },
        {
          "name": "kanji_in_context",
          "category": "index",
          "content": "Kanji in Context",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "26"
        },
        {
          "name": "halpern_kkld",
          "category": "index",
          "content": "Kanji Learners Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "1247"
        },
        {
          "name": "halpern_kkld_2ed",
          "category": "index",
          "content": "Kanji Learners Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "1713"
        },
        {
          "name": "kodansha_compact",
          "category": "index",
          "content": "Kodansha Compact Kanji Guide",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "180"
        },
        {
          "name": "halpern_kkd",
          "category": "index",
          "content": "Kodansha Kanji Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2466"
        },
        {
          "name": "maniette",
          "category": "index",
          "content": "Les Kanjis dans la tete",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "788"
        },
        {
          "name": "nelson_c",
          "category": "index",
          "content": "Modern Reader's Japanese-English Character Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "578"
        },
        {
          "name": "halpern_njecd",
          "category": "index",
          "content": "New Japanese-English Character Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "1972"
        },
        {
          "name": "heisig",
          "category": "index",
          "content": "Remembering The  Kanji",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "781"
        },
        {
          "name": "heisig6",
          "category": "index",
          "content": "Remembering The  Kanji, Sixth Ed.",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "844"
        },
        {
          "name": "crowley",
          "category": "index",
          "content": "The Kanji Way to Japanese Language Power",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "28"
        },
        {
          "name": "nelson_n",
          "category": "index",
          "content": "The New Nelson Japanese-English Character Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "454"
        },
        {
          "name": "tutt_cards",
          "category": "index",
          "content": "Tuttle Kanji Cards",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "101"
        }
      ],
      "class": [
        {
          "name": "deroo",
          "category": "class",
          "content": "2001 Kanji",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2045"
        },
        {
          "name": "four_corner",
          "category": "class",
          "content": "Four corner code",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "8022.7"
        },
        {
          "name": "skip",
          "category": "class",
          "content": "SKIP code",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2-2-2"
        },
        {
          "name": "sh_desc",
          "category": "class",
          "content": "The Kanji Dictionary",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2o2.1"
        }
      ],
      "misc": [
        {
          "name": "freq",
          "category": "misc",
          "content": "Frequency",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "24"
        },
        {
          "name": "grade",
          "category": "misc",
          "content": "Grade level",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "2"
        },
        {
          "name": "jlpt",
          "category": "misc",
          "content": "JLPT level",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "4"
        },
        {
          "name": "strokes",
          "category": "misc",
          "content": "Stroke count",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "4"
        }
      ],
      "code": [
        {
          "name": "jis208",
          "category": "code",
          "content": "JIS X 0208-1997 kuten code",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "1-42-12"
        },
        {
          "name": "ucs",
          "category": "code",
          "content": "Unicode hex code",
          "order": 0,
          "score": 0,
          "dictionary": "KANJIDIC [2025-145]",
          "value": "5206"
        }
      ]
    },
    "definitions": [
      "part",
      "minute of time",
      "segment",
      "share",
      "degree",
      "one's lot",
      "duty",
      "understand",
      "know",
      "rate",
      "1%",
      "chances",
      "shaku/100"
    ],
    "frequencies": []
  }
]
```

</details>