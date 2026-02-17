# `termEntries`

Returns term dictionary entries for search text as they are represented internally by Yomitan.

## Request Options

- Request method: `POST`

- Body:

    - `term` (`string`): The term to return data for.

## Request Example

- Request method: `POST`

- Body:
    ```json
    {
        "term": "分かる"
    }
    ```

## Response Example (200)

Due to this being a data format used internally by Yomitan, no guarantees are made for the stability or accuracy of the responses.

<details>
<summary>Expand to view response</summary>

```json
{
  "dictionaryEntries": [
    {
      "type": "term",
      "isPrimary": true,
      "textProcessorRuleChainCandidates": [
        []
      ],
      "inflectionRuleChainCandidates": [
        {
          "source": "algorithm",
          "inflectionRules": []
        }
      ],
      "score": 200,
      "frequencyOrder": 0,
      "dictionaryIndex": 0,
      "dictionaryAlias": "",
      "sourceTermExactMatchCount": 0,
      "matchPrimaryReading": false,
      "maxOriginalTextLength": 3,
      "headwords": [
        {
          "index": 0,
          "headwordIndex": 0,
          "term": "分かる",
          "reading": "わかる",
          "sources": [
            {
              "originalText": "わかる",
              "transformedText": "わかる",
              "deinflectedText": "わかる",
              "matchType": "exact",
              "matchSource": "reading",
              "isPrimary": true
            }
          ],
          "tags": [],
          "wordClasses": [
            "v5"
          ]
        }
      ],
      "definitions": [
        {
          "index": 0,
          "headwordIndices": [
            0
          ],
          "dictionary": "Jitendex.org [2025-05-13]",
          "dictionaryIndex": 0,
          "dictionaryAlias": "Jitendex.org [2025-05-13]",
          "id": 137394,
          "score": 200,
          "frequencyOrder": 0,
          "sequences": [
            1606560
          ],
          "isPrimary": true,
          "tags": [
            {
              "name": "priority form",
              "category": "frequent",
              "order": 1,
              "score": 1,
              "content": [
                "high priority spelling or reading of this term"
              ],
              "dictionaries": [
                "Jitendex.org [2025-05-13]"
              ],
              "redundant": false
            },
            {
              "name": "★",
              "category": "popular",
              "order": 2,
              "score": 2,
              "content": [
                "high priority entry"
              ],
              "dictionaries": [
                "Jitendex.org [2025-05-13]"
              ],
              "redundant": false
            }
          ],
          "entries": [
            {
              "type": "structured-content",
              "content": [
                {
                  "tag": "ul",
                  "lang": "ja",
                  "style": {
                    "listStyleType": "\"＊\""
                  },
                  "content": [
                    {
                      "tag": "li",
                      "content": [
                        {
                          "tag": "span",
                          "title": "Godan verb with 'ru' ending",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "v5r"
                          },
                          "content": "5-dan"
                        },
                        {
                          "tag": "span",
                          "title": "intransitive verb",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "vi"
                          },
                          "content": "intransitive"
                        },
                        {
                          "tag": "span",
                          "title": "word usually written using kana alone",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "brown",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "uk"
                          },
                          "content": "kana"
                        },
                        {
                          "tag": "ol",
                          "content": [
                            {
                              "tag": "li",
                              "style": {
                                "listStyleType": "\"①\"",
                                "paddingLeft": "0.25em"
                              },
                              "data": {
                                "sense-number": "1"
                              },
                              "content": [
                                {
                                  "tag": "ul",
                                  "data": {
                                    "content": "glossary"
                                  },
                                  "content": [
                                    {
                                      "tag": "li",
                                      "content": "to understand"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to comprehend"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to grasp"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to see"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to get"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to follow"
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "style": {
                                    "marginLeft": "0.5em"
                                  },
                                  "data": {
                                    "content": "extra-info"
                                  },
                                  "content": {
                                    "tag": "div",
                                    "content": {
                                      "tag": "div",
                                      "style": {
                                        "borderStyle": "none none none solid",
                                        "padding": "0.5rem",
                                        "borderRadius": "0.4rem",
                                        "borderWidth": "calc(3em / var(--font-size-no-units, 14))",
                                        "marginTop": "0.5rem",
                                        "marginBottom": "0.5rem",
                                        "borderColor": "var(--text-color, var(--fg, #333))",
                                        "backgroundColor": "color-mix(in srgb, var(--text-color, var(--fg, #333)) 5%, transparent)"
                                      },
                                      "data": {
                                        "content": "example-sentence",
                                        "sentence-key": "分かる",
                                        "source": "236205",
                                        "source-type": "tat"
                                      },
                                      "content": [
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "1.3em"
                                          },
                                          "data": {
                                            "content": "example-sentence-a"
                                          },
                                          "content": [
                                            "「",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "博",
                                                {
                                                  "tag": "rt",
                                                  "content": "ひろし"
                                                }
                                              ]
                                            },
                                            "、",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "君",
                                                {
                                                  "tag": "rt",
                                                  "content": "きみ"
                                                }
                                              ]
                                            },
                                            "の",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "気",
                                                {
                                                  "tag": "rt",
                                                  "content": "き"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "持",
                                                {
                                                  "tag": "rt",
                                                  "content": "も"
                                                }
                                              ]
                                            },
                                            "ちは",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "color": "color-mix(in srgb, lime, var(--text-color, var(--fg, #333)))"
                                              },
                                              "data": {
                                                "content": "example-keyword"
                                              },
                                              "content": [
                                                {
                                                  "tag": "ruby",
                                                  "content": [
                                                    "分",
                                                    {
                                                      "tag": "rt",
                                                      "content": "わ"
                                                    }
                                                  ]
                                                },
                                                "かる"
                                              ]
                                            },
                                            "よ」とマイクが",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "言",
                                                {
                                                  "tag": "rt",
                                                  "content": "い"
                                                }
                                              ]
                                            },
                                            "います。"
                                          ]
                                        },
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "0.8em"
                                          },
                                          "data": {
                                            "content": "example-sentence-b"
                                          },
                                          "content": [
                                            "\"I understand how you feel, Hiroshi,\" says Mike.",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "fontSize": "0.8em",
                                                "marginLeft": "0.25rem",
                                                "color": "#777",
                                                "verticalAlign": "top"
                                              },
                                              "data": {
                                                "content": "attribution-footnote"
                                              },
                                              "content": "[1]"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  }
                                }
                              ]
                            },
                            {
                              "tag": "li",
                              "style": {
                                "listStyleType": "\"②\"",
                                "paddingLeft": "0.25em"
                              },
                              "data": {
                                "sense-number": "2"
                              },
                              "content": [
                                {
                                  "tag": "ul",
                                  "data": {
                                    "content": "glossary"
                                  },
                                  "content": [
                                    {
                                      "tag": "li",
                                      "content": "to become clear"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be known"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be discovered"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be realized"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be realised"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be found out"
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "style": {
                                    "marginLeft": "0.5em"
                                  },
                                  "data": {
                                    "content": "extra-info"
                                  },
                                  "content": {
                                    "tag": "div",
                                    "content": {
                                      "tag": "div",
                                      "style": {
                                        "borderStyle": "none none none solid",
                                        "padding": "0.5rem",
                                        "borderRadius": "0.4rem",
                                        "borderWidth": "calc(3em / var(--font-size-no-units, 14))",
                                        "marginTop": "0.5rem",
                                        "marginBottom": "0.5rem",
                                        "borderColor": "var(--text-color, var(--fg, #333))",
                                        "backgroundColor": "color-mix(in srgb, var(--text-color, var(--fg, #333)) 5%, transparent)"
                                      },
                                      "data": {
                                        "content": "example-sentence",
                                        "sentence-key": "わかります",
                                        "source": "119408",
                                        "source-type": "tat"
                                      },
                                      "content": [
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "1.3em"
                                          },
                                          "data": {
                                            "content": "example-sentence-a"
                                          },
                                          "content": [
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "彼",
                                                {
                                                  "tag": "rt",
                                                  "content": "かれ"
                                                }
                                              ]
                                            },
                                            "が",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "有",
                                                {
                                                  "tag": "rt",
                                                  "content": "ゆう"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "名",
                                                {
                                                  "tag": "rt",
                                                  "content": "めい"
                                                }
                                              ]
                                            },
                                            "な",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "人",
                                                {
                                                  "tag": "rt",
                                                  "content": "じん"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "物",
                                                {
                                                  "tag": "rt",
                                                  "content": "ぶつ"
                                                }
                                              ]
                                            },
                                            "だというのが",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "color": "color-mix(in srgb, lime, var(--text-color, var(--fg, #333)))"
                                              },
                                              "content": "わかります"
                                            },
                                            "。"
                                          ]
                                        },
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "0.8em"
                                          },
                                          "data": {
                                            "content": "example-sentence-b"
                                          },
                                          "content": [
                                            "I understand that he's something of a famous personality.",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "fontSize": "0.8em",
                                                "marginLeft": "0.25rem",
                                                "color": "#777",
                                                "verticalAlign": "top"
                                              },
                                              "data": {
                                                "content": "attribution-footnote"
                                              },
                                              "content": "[2]"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  }
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "tag": "li",
                      "style": {
                        "marginTop": "0.5em"
                      },
                      "content": [
                        {
                          "tag": "span",
                          "title": "interjection (kandoushi)",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "int"
                          },
                          "content": "interjection"
                        },
                        {
                          "tag": "ol",
                          "content": {
                            "tag": "li",
                            "style": {
                              "listStyleType": "\"③\"",
                              "paddingLeft": "0.25em"
                            },
                            "data": {
                              "sense-number": "3"
                            },
                            "content": {
                              "tag": "ul",
                              "data": {
                                "content": "glossary"
                              },
                              "content": [
                                {
                                  "tag": "li",
                                  "content": "I know!"
                                },
                                {
                                  "tag": "li",
                                  "content": "I think so too!"
                                }
                              ]
                            }
                          }
                        }
                      ]
                    },
                    {
                      "tag": "li",
                      "style": {
                        "marginTop": "0.5rem"
                      },
                      "data": {
                        "content": "forms"
                      },
                      "content": [
                        {
                          "tag": "span",
                          "title": "spelling and reading variants",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "content": "forms"
                        },
                        {
                          "tag": "ul",
                          "style": {
                            "fontSize": "1.3em"
                          },
                          "content": [
                            {
                              "tag": "li",
                              "content": "分かる"
                            },
                            {
                              "tag": "li",
                              "content": "解る"
                            },
                            {
                              "tag": "li",
                              "content": "判る"
                            },
                            {
                              "tag": "li",
                              "content": "分る"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                {
                  "tag": "div",
                  "style": {
                    "fontSize": "0.7em",
                    "textAlign": "right"
                  },
                  "data": {
                    "content": "attribution"
                  },
                  "content": [
                    {
                      "tag": "a",
                      "href": "https://www.edrdg.org/jmwsgi/entr.py?svc=jmdict&q=1606560",
                      "content": "JMdict"
                    },
                    " | Tatoeba ",
                    {
                      "tag": "a",
                      "href": "https://tatoeba.org/en/sentences/show/236205",
                      "content": "[1]"
                    },
                    {
                      "tag": "a",
                      "href": "https://tatoeba.org/en/sentences/show/119408",
                      "content": "[2]"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "pronunciations": [],
      "frequencies": [
        {
          "index": 0,
          "headwordIndex": 0,
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
          "index": 1,
          "headwordIndex": 0,
          "dictionary": "JPDBv2㋕",
          "dictionaryIndex": 2,
          "dictionaryAlias": "JPDBv2㋕",
          "hasReading": true,
          "frequencyMode": "rank-based",
          "frequency": 465,
          "displayValue": "465",
          "displayValueParsed": false
        },
        {
          "index": 2,
          "headwordIndex": 0,
          "dictionary": "BCCWJ",
          "dictionaryIndex": 3,
          "dictionaryAlias": "BCCWJ",
          "hasReading": true,
          "frequencyMode": "rank-based",
          "frequency": 85,
          "displayValue": null,
          "displayValueParsed": false
        },
        {
          "index": 3,
          "headwordIndex": 0,
          "dictionary": "BCCWJ",
          "dictionaryIndex": 3,
          "dictionaryAlias": "BCCWJ",
          "hasReading": true,
          "frequencyMode": "rank-based",
          "frequency": 105,
          "displayValue": null,
          "displayValueParsed": false
        }
      ]
    },
    {
      "type": "term",
      "isPrimary": true,
      "textProcessorRuleChainCandidates": [
        []
      ],
      "inflectionRuleChainCandidates": [
        {
          "source": "algorithm",
          "inflectionRules": []
        }
      ],
      "score": 199,
      "frequencyOrder": 0,
      "dictionaryIndex": 0,
      "dictionaryAlias": "",
      "sourceTermExactMatchCount": 0,
      "matchPrimaryReading": false,
      "maxOriginalTextLength": 3,
      "headwords": [
        {
          "index": 0,
          "headwordIndex": 0,
          "term": "解る",
          "reading": "わかる",
          "sources": [
            {
              "originalText": "わかる",
              "transformedText": "わかる",
              "deinflectedText": "わかる",
              "matchType": "exact",
              "matchSource": "reading",
              "isPrimary": true
            }
          ],
          "tags": [],
          "wordClasses": [
            "v5"
          ]
        }
      ],
      "definitions": [
        {
          "index": 0,
          "headwordIndices": [
            0
          ],
          "dictionary": "Jitendex.org [2025-05-13]",
          "dictionaryIndex": 0,
          "dictionaryAlias": "Jitendex.org [2025-05-13]",
          "id": 137395,
          "score": 199,
          "frequencyOrder": 0,
          "sequences": [
            1606560
          ],
          "isPrimary": true,
          "tags": [
            {
              "name": "priority form",
              "category": "frequent",
              "order": 1,
              "score": 1,
              "content": [
                "high priority spelling or reading of this term"
              ],
              "dictionaries": [
                "Jitendex.org [2025-05-13]"
              ],
              "redundant": false
            },
            {
              "name": "★",
              "category": "popular",
              "order": 2,
              "score": 2,
              "content": [
                "high priority entry"
              ],
              "dictionaries": [
                "Jitendex.org [2025-05-13]"
              ],
              "redundant": false
            }
          ],
          "entries": [
            {
              "type": "structured-content",
              "content": [
                {
                  "tag": "ul",
                  "lang": "ja",
                  "style": {
                    "listStyleType": "\"＊\""
                  },
                  "content": [
                    {
                      "tag": "li",
                      "content": [
                        {
                          "tag": "span",
                          "title": "Godan verb with 'ru' ending",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "v5r"
                          },
                          "content": "5-dan"
                        },
                        {
                          "tag": "span",
                          "title": "intransitive verb",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "vi"
                          },
                          "content": "intransitive"
                        },
                        {
                          "tag": "span",
                          "title": "word usually written using kana alone",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "brown",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "uk"
                          },
                          "content": "kana"
                        },
                        {
                          "tag": "ol",
                          "content": [
                            {
                              "tag": "li",
                              "style": {
                                "listStyleType": "\"①\"",
                                "paddingLeft": "0.25em"
                              },
                              "data": {
                                "sense-number": "1"
                              },
                              "content": [
                                {
                                  "tag": "ul",
                                  "data": {
                                    "content": "glossary"
                                  },
                                  "content": [
                                    {
                                      "tag": "li",
                                      "content": "to understand"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to comprehend"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to grasp"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to see"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to get"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to follow"
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "style": {
                                    "marginLeft": "0.5em"
                                  },
                                  "data": {
                                    "content": "extra-info"
                                  },
                                  "content": {
                                    "tag": "div",
                                    "content": {
                                      "tag": "div",
                                      "style": {
                                        "borderStyle": "none none none solid",
                                        "padding": "0.5rem",
                                        "borderRadius": "0.4rem",
                                        "borderWidth": "calc(3em / var(--font-size-no-units, 14))",
                                        "marginTop": "0.5rem",
                                        "marginBottom": "0.5rem",
                                        "borderColor": "var(--text-color, var(--fg, #333))",
                                        "backgroundColor": "color-mix(in srgb, var(--text-color, var(--fg, #333)) 5%, transparent)"
                                      },
                                      "data": {
                                        "content": "example-sentence",
                                        "sentence-key": "分かる",
                                        "source": "236205",
                                        "source-type": "tat"
                                      },
                                      "content": [
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "1.3em"
                                          },
                                          "data": {
                                            "content": "example-sentence-a"
                                          },
                                          "content": [
                                            "「",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "博",
                                                {
                                                  "tag": "rt",
                                                  "content": "ひろし"
                                                }
                                              ]
                                            },
                                            "、",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "君",
                                                {
                                                  "tag": "rt",
                                                  "content": "きみ"
                                                }
                                              ]
                                            },
                                            "の",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "気",
                                                {
                                                  "tag": "rt",
                                                  "content": "き"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "持",
                                                {
                                                  "tag": "rt",
                                                  "content": "も"
                                                }
                                              ]
                                            },
                                            "ちは",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "color": "color-mix(in srgb, lime, var(--text-color, var(--fg, #333)))"
                                              },
                                              "data": {
                                                "content": "example-keyword"
                                              },
                                              "content": [
                                                {
                                                  "tag": "ruby",
                                                  "content": [
                                                    "分",
                                                    {
                                                      "tag": "rt",
                                                      "content": "わ"
                                                    }
                                                  ]
                                                },
                                                "かる"
                                              ]
                                            },
                                            "よ」とマイクが",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "言",
                                                {
                                                  "tag": "rt",
                                                  "content": "い"
                                                }
                                              ]
                                            },
                                            "います。"
                                          ]
                                        },
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "0.8em"
                                          },
                                          "data": {
                                            "content": "example-sentence-b"
                                          },
                                          "content": [
                                            "\"I understand how you feel, Hiroshi,\" says Mike.",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "fontSize": "0.8em",
                                                "marginLeft": "0.25rem",
                                                "color": "#777",
                                                "verticalAlign": "top"
                                              },
                                              "data": {
                                                "content": "attribution-footnote"
                                              },
                                              "content": "[1]"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  }
                                }
                              ]
                            },
                            {
                              "tag": "li",
                              "style": {
                                "listStyleType": "\"②\"",
                                "paddingLeft": "0.25em"
                              },
                              "data": {
                                "sense-number": "2"
                              },
                              "content": [
                                {
                                  "tag": "ul",
                                  "data": {
                                    "content": "glossary"
                                  },
                                  "content": [
                                    {
                                      "tag": "li",
                                      "content": "to become clear"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be known"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be discovered"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be realized"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be realised"
                                    },
                                    {
                                      "tag": "li",
                                      "content": "to be found out"
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "style": {
                                    "marginLeft": "0.5em"
                                  },
                                  "data": {
                                    "content": "extra-info"
                                  },
                                  "content": {
                                    "tag": "div",
                                    "content": {
                                      "tag": "div",
                                      "style": {
                                        "borderStyle": "none none none solid",
                                        "padding": "0.5rem",
                                        "borderRadius": "0.4rem",
                                        "borderWidth": "calc(3em / var(--font-size-no-units, 14))",
                                        "marginTop": "0.5rem",
                                        "marginBottom": "0.5rem",
                                        "borderColor": "var(--text-color, var(--fg, #333))",
                                        "backgroundColor": "color-mix(in srgb, var(--text-color, var(--fg, #333)) 5%, transparent)"
                                      },
                                      "data": {
                                        "content": "example-sentence",
                                        "sentence-key": "わかります",
                                        "source": "119408",
                                        "source-type": "tat"
                                      },
                                      "content": [
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "1.3em"
                                          },
                                          "data": {
                                            "content": "example-sentence-a"
                                          },
                                          "content": [
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "彼",
                                                {
                                                  "tag": "rt",
                                                  "content": "かれ"
                                                }
                                              ]
                                            },
                                            "が",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "有",
                                                {
                                                  "tag": "rt",
                                                  "content": "ゆう"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "名",
                                                {
                                                  "tag": "rt",
                                                  "content": "めい"
                                                }
                                              ]
                                            },
                                            "な",
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "人",
                                                {
                                                  "tag": "rt",
                                                  "content": "じん"
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "ruby",
                                              "content": [
                                                "物",
                                                {
                                                  "tag": "rt",
                                                  "content": "ぶつ"
                                                }
                                              ]
                                            },
                                            "だというのが",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "color": "color-mix(in srgb, lime, var(--text-color, var(--fg, #333)))"
                                              },
                                              "content": "わかります"
                                            },
                                            "。"
                                          ]
                                        },
                                        {
                                          "tag": "div",
                                          "style": {
                                            "fontSize": "0.8em"
                                          },
                                          "data": {
                                            "content": "example-sentence-b"
                                          },
                                          "content": [
                                            "I understand that he's something of a famous personality.",
                                            {
                                              "tag": "span",
                                              "style": {
                                                "fontSize": "0.8em",
                                                "marginLeft": "0.25rem",
                                                "color": "#777",
                                                "verticalAlign": "top"
                                              },
                                              "data": {
                                                "content": "attribution-footnote"
                                              },
                                              "content": "[2]"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  }
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "tag": "li",
                      "style": {
                        "marginTop": "0.5em"
                      },
                      "content": [
                        {
                          "tag": "span",
                          "title": "interjection (kandoushi)",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "data": {
                            "code": "int"
                          },
                          "content": "interjection"
                        },
                        {
                          "tag": "ol",
                          "content": {
                            "tag": "li",
                            "style": {
                              "listStyleType": "\"③\"",
                              "paddingLeft": "0.25em"
                            },
                            "data": {
                              "sense-number": "3"
                            },
                            "content": {
                              "tag": "ul",
                              "data": {
                                "content": "glossary"
                              },
                              "content": [
                                {
                                  "tag": "li",
                                  "content": "I know!"
                                },
                                {
                                  "tag": "li",
                                  "content": "I think so too!"
                                }
                              ]
                            }
                          }
                        }
                      ]
                    },
                    {
                      "tag": "li",
                      "style": {
                        "marginTop": "0.5rem"
                      },
                      "data": {
                        "content": "forms"
                      },
                      "content": [
                        {
                          "tag": "span",
                          "title": "spelling and reading variants",
                          "style": {
                            "fontSize": "0.8em",
                            "fontWeight": "bold",
                            "padding": "0.2em 0.3em",
                            "wordBreak": "keep-all",
                            "borderRadius": "0.3em",
                            "verticalAlign": "text-bottom",
                            "backgroundColor": "#565656",
                            "color": "white",
                            "cursor": "help",
                            "marginRight": "0.25em"
                          },
                          "content": "forms"
                        },
                        {
                          "tag": "ul",
                          "style": {
                            "fontSize": "1.3em"
                          },
                          "content": [
                            {
                              "tag": "li",
                              "content": "分かる"
                            },
                            {
                              "tag": "li",
                              "content": "解る"
                            },
                            {
                              "tag": "li",
                              "content": "判る"
                            },
                            {
                              "tag": "li",
                              "content": "分る"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                {
                  "tag": "div",
                  "style": {
                    "fontSize": "0.7em",
                    "textAlign": "right"
                  },
                  "data": {
                    "content": "attribution"
                  },
                  "content": [
                    {
                      "tag": "a",
                      "href": "https://www.edrdg.org/jmwsgi/entr.py?svc=jmdict&q=1606560",
                      "content": "JMdict"
                    },
                    " | Tatoeba ",
                    {
                      "tag": "a",
                      "href": "https://tatoeba.org/en/sentences/show/236205",
                      "content": "[1]"
                    },
                    {
                      "tag": "a",
                      "href": "https://tatoeba.org/en/sentences/show/119408",
                      "content": "[2]"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "pronunciations": [],
      "frequencies": [
        {
          "index": 0,
          "headwordIndex": 0,
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
          "index": 1,
          "headwordIndex": 0,
          "dictionary": "JPDBv2㋕",
          "dictionaryIndex": 2,
          "dictionaryAlias": "JPDBv2㋕",
          "hasReading": true,
          "frequencyMode": "rank-based",
          "frequency": 8354,
          "displayValue": "8354",
          "displayValueParsed": false
        }
      ]
    }
  ],
  "originalTextLength": 3
}
```

</details>