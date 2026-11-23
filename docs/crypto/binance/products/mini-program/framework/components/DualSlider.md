---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/DualSlider
api_type: Guide
updated_at: 2026-11-23 18:43:42.005134
---

# DualSlider

## Props

| Name               | Type       | Description                                                    | Default                  |
| ------------------ | ---------- | -------------------------------------------------------------- | ------------------------ |
| `min`              | `number`   | Least value                                                    | `0`                      |
| `max`              | `number`   | Maximum value                                                  | `100`                    |
| `value`            | `number[]` |                                                                | `[0,0]`                  |
| `step`             | `number`   | Step size must be greater than 0 and can be(Max - Min) integer | `1`                      |
| `disabled`         | `boolean`  | Is it disabled?                                                | `false`                  |
| `show-value`       | `boolean`  | Displays current value                                         | `false`                  |
| `active-color`     | `string`   | Selected color                                                 | `\`var(--bnui-primay)\`` |
| `background-color` | `string`   | Background Bar Color                                           | `"#e9e9e9"`              |

## Events

| Name             | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `bindchange`     | `bindchange` Event triggered after completing a drag, event.detail = `{value}` |
| `bindchanging`   | `bindchaning` Event triggered during drag, event. detail = `{value}`           |
| `bindtap`        | `bindtap` Event tap                                                            |
| `bindtapcapture` | `bindtapcapture` Event tap                                                     |

---

# DualSlider

## Props

| Name               | Type       | Description                                                    | Default                  |
| ------------------ | ---------- | -------------------------------------------------------------- | ------------------------ |
| `min`              | `number`   | Least value                                                    | `0`                      |
| `max`              | `number`   | Maximum value                                                  | `100`                    |
| `value`            | `number[]` |                                                                | `[0,0]`                  |
| `step`             | `number`   | Step size must be greater than 0 and can be(Max - Min) integer | `1`                      |
| `disabled`         | `boolean`  | Is it disabled?                                                | `false`                  |
| `show-value`       | `boolean`  | Displays current value                                         | `false`                  |
| `active-color`     | `string`   | Selected color                                                 | `\`var(--bnui-primay)\`` |
| `background-color` | `string`   | Background Bar Color                                           | `"#e9e9e9"`              |

## Events

| Name             | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `bindchange`     | `bindchange` Event triggered after completing a drag, event.detail = `{value}` |
| `bindchanging`   | `bindchaning` Event triggered during drag, event. detail = `{value}`           |
| `bindtap`        | `bindtap` Event tap                                                            |
| `bindtapcapture` | `bindtapcapture` Event tap                                                     |