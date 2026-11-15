# `displayOptions`

Returns the options Yomitan uses to show lookup results in popups: how entries are grouped and laid out, how tags, frequencies and pitch accents are shown, and the theme, font, scale and custom CSS.

The options always match the active profile.

## Request Options

- Request method: `POST`

- Body: None

## Response Example (200)

- `general`: Options from the profile's general settings.

- `scanning`: `enableSearchTags` is whether the tags for entry terms and readings are shown (Yomitan's "Show tags for expressions and their readings").

Due to this being a data format used internally by Yomitan, no guarantees are made for the stability or accuracy of the responses.

```json
{
    "general": {
        "language": "ja",
        "resultOutputMode": "group",
        "glossaryLayoutMode": "default",
        "compactTags": false,
        "averageFrequency": false,
        "frequencyDisplayMode": "split-tags-grouped",
        "termDisplayMode": "ruby",
        "showPitchAccentDownstepNotation": true,
        "showPitchAccentPositionNotation": true,
        "showPitchAccentGraph": false,
        "popupDisplayMode": "default",
        "popupTheme": "site",
        "popupOuterTheme": "site",
        "fontFamily": "",
        "fontSize": 14,
        "lineHeight": "1.5",
        "popupScalingFactor": 1,
        "customPopupCss": "",
        "customPopupOuterCss": "",
        "popupCurrentIndicatorMode": "triangle",
        "popupActionBarVisibility": "auto",
        "popupActionBarLocation": "top"
    },
    "scanning": {
        "enableSearchTags": false
    }
}
```
