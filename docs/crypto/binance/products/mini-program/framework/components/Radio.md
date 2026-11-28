---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Radio
api_type: Guide
updated_at: 2026-11-28 18:41:07.709037
---

# radio

Radio item

**Example**

bxml

```html
<view class="page-body">
  <view class="page-section">
    <view class="page-section-title">default style</view>
    <label class="radio"> <radio value="r1" checked="true" /> checked </label>
    <label class="radio"> <radio value="r2" /> unchecked </label>
    <label class="radio"> <radio value="r3" disabled /> disabled <radio value="r4" color="#333" /> custom color </label>
  </view>
</view>
```

## Props

| Name       | Type      | Description                                                                                        | Default                  |
| ---------- | --------- | -------------------------------------------------------------------------------------------------- | ------------------------ |
| `checked`  | `boolean` | When the radio is selected, the change event of the radio-group will carry the value of the radio. | `false`                  |
| `value`    | `string`  | Currently selected or not.                                                                         |                          |
| `disabled` | `boolean` | Disabled or not.                                                                                   | `false`                  |
| `color`    | `string`  | The color of the radio, just like css color.                                                       | `\`var(--bnui-primay)\`` |

## Events

| Name             | Description |
| ---------------- | ----------- |
| `bindtap`        |             |
| `bindtapcapture` | &nbsp;      |

---

# radio

Radio item

**Example**

bxml

```html
<view class="page-body">
  <view class="page-section">
    <view class="page-section-title">default style</view>
    <label class="radio"> <radio value="r1" checked="true" /> checked </label>
    <label class="radio"> <radio value="r2" /> unchecked </label>
    <label class="radio"> <radio value="r3" disabled /> disabled <radio value="r4" color="#333" /> custom color </label>
  </view>
</view>
```

## Props

| Name       | Type      | Description                                                                                        | Default                  |
| ---------- | --------- | -------------------------------------------------------------------------------------------------- | ------------------------ |
| `checked`  | `boolean` | When the radio is selected, the change event of the radio-group will carry the value of the radio. | `false`                  |
| `value`    | `string`  | Currently selected or not.                                                                         |                          |
| `disabled` | `boolean` | Disabled or not.                                                                                   | `false`                  |
| `color`    | `string`  | The color of the radio, just like css color.                                                       | `\`var(--bnui-primay)\`` |

## Events

| Name             | Description |
| ---------------- | ----------- |
| `bindtap`        |             |
| `bindtapcapture` | &nbsp;      |