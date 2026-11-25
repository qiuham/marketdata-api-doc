---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/setNavigationBarColor
api_type: Guide
updated_at: 2026-11-25 18:46:46.402377
---

# bn.setNavigationBarColor

▸ **setNavigationBarColor**(`options`): `Promise`<{}\>

Dynamically sets the navigation bar color of the current page.

Parameters

| Name      | Type                           | Description            |
| :-------- | :----------------------------- | :--------------------- |
| `options` | `SetNavigationBarColorOptions` | navigation bar options |

Returns

`Promise`<{}\>

## SetNavigationBarColorOptions

Ƭ **SetNavigationBarColorOptions**: `Object`

Type declaration

| Name                    | Type                                                                                                | Description                                                                                                           |
| :---------------------- | :-------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `frontColor`            | `string`                                                                                            | Foreground color values, including the color of the on, title, and status bar, are supported only #ffffff and #000000 |
| `backgroundColor`       | `string`                                                                                            | Background color value, valid value is hexadecimal color                                                              |
| `animation`             | { `duration?`: `number` ; `timingFunc?`: `"linear"` \| `"easeIn"` \| `"easeOut"` \| `"easeInOut"` } | Animation effect                                                                                                      |
| `animation.duration?`   | `number`                                                                                            | Animation change time, unit ms                                                                                        |
| `animation.timingFunc?` | `"linear"` \| `"easeIn"` \| `"easeOut"` \| `"easeInOut"`                                            | Animation change mode                                                                                                 |
| `rendererId?`           | `number`                                                                                            | renderer id                                                                                                           |

---

# bn.setNavigationBarColor

▸ **setNavigationBarColor**(`options`): `Promise`<{}\>

Dynamically sets the navigation bar color of the current page.

Parameters

| Name      | Type                           | Description            |
| :-------- | :----------------------------- | :--------------------- |
| `options` | `SetNavigationBarColorOptions` | navigation bar options |

Returns

`Promise`<{}\>

## SetNavigationBarColorOptions

Ƭ **SetNavigationBarColorOptions**: `Object`

Type declaration

| Name                    | Type                                                                                                | Description                                                                                                           |
| :---------------------- | :-------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `frontColor`            | `string`                                                                                            | Foreground color values, including the color of the on, title, and status bar, are supported only #ffffff and #000000 |
| `backgroundColor`       | `string`                                                                                            | Background color value, valid value is hexadecimal color                                                              |
| `animation`             | { `duration?`: `number` ; `timingFunc?`: `"linear"` \| `"easeIn"` \| `"easeOut"` \| `"easeInOut"` } | Animation effect                                                                                                      |
| `animation.duration?`   | `number`                                                                                            | Animation change time, unit ms                                                                                        |
| `animation.timingFunc?` | `"linear"` \| `"easeIn"` \| `"easeOut"` \| `"easeInOut"`                                            | Animation change mode                                                                                                 |
| `rendererId?`           | `number`                                                                                            | renderer id                                                                                                           |