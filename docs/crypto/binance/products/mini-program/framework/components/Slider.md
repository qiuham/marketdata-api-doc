---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Slider
api_type: Guide
updated_at: 2026-11-19 18:44:44.994195
---

# slider

Slider.

**Example**

bxml:

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section-title">Set step</view>
      <view class="body-view">
        <slider value="{{60}}" bindchange="sliderChange" step="{{5}}" bindtap="sliderClick" onLongPress="sliderLonePress"></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">disabled</view>
      <view class="body-view">
        <slider value="{{60}}" bindchange="sliderChange" step="{{5}}" disabled></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">Display current value</view>
      <view class="body-view">
        <slider value="{{50}}" bindchange="sliderChange" show-value="{{true}}"></slider>
      </view>
    </view>
    <view class="page-section page-section-gap">
      <view class="page-section-title">Set min/max value</view>
      <view class="body-view">
        <slider value="{{100}}" bindchange="sliderChange" min="{{50}}" max="{{200}}" show-value="{{true}}"></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">controlled</view>
      <view class="body-view">
        <slider value="{{controlledValue}}" bindchange="onControlledValueChange" min="{{50}}" max="{{200}}" show-value="{{true}}" />

        <slider value="{{controlledValue}}" bindchange="onControlledValueChange" min="{{50}}" max="{{200}}" show-value="{{true}}" />
      </view>
    </view>
  </view>

  <view style="margin: 24px;">
    normal Taroslider
    <slider />
  </view>
  <view style="position: relative;margin: 24; ">
    with position: relative
    <slider />
  </view>
</view>
```

js

```js
Page({
  data: {
    controlledValue: 50,
  },
  sliderChange(e) {
    console.log("slider fire change event，value:", e.detail.value);
  },
  sliderClick(e) {
    console.log("slider fire click event，value:", e.detail.value);
  },
  sliderLonePress(e) {
    console.log("slider fire lonePress event，value:", e.detail.value);
  },
  onControlledValueChange(e) {
    console.log("slider fire change event，value:", e.detail.value);
    this.setData({
      controlledValue: e.detail.value,
    });
  },
});
```

## Props

| Name               | Type      | Description                                                    | Default                  |
| ------------------ | --------- | -------------------------------------------------------------- | ------------------------ |
| `min`              | `number`  | Least value                                                    | `0`                      |
| `max`              | `number`  | Maximum value                                                  | `100`                    |
| `step`             | `number`  | Step size must be greater than 0 and can be(Max - Min) integer | `1`                      |
| `disabled`         | `boolean` | Is it disabled?                                                | `false`                  |
| `value`            | `number`  | Current value                                                  |                          |
| `show-value`       | `boolean` | Displays current value                                         | `false`                  |
| `active-color`     | `string`  | Selected color                                                 | `\`var(--bnui-primay)\`` |
| `background-color` | `string`  | Background Bar Color                                           | `"#e9e9e9"`              |

## Events

| Name             | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `bindchange`     | `bindchange` Event triggered after completing a drag, event.detail = `{value}` |
| `bindchanging`   | `bindchaning` Event triggered during drag, event. detail = `{value}`           |
| `bindtap`        | `bindtap` Event tap                                                            |
| `bindtapcapture` | `bindtapcapture` Event tap                                                     |

---

# slider

Slider.

**Example**

bxml:

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section-title">Set step</view>
      <view class="body-view">
        <slider value="{{60}}" bindchange="sliderChange" step="{{5}}" bindtap="sliderClick" onLongPress="sliderLonePress"></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">disabled</view>
      <view class="body-view">
        <slider value="{{60}}" bindchange="sliderChange" step="{{5}}" disabled></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">Display current value</view>
      <view class="body-view">
        <slider value="{{50}}" bindchange="sliderChange" show-value="{{true}}"></slider>
      </view>
    </view>
    <view class="page-section page-section-gap">
      <view class="page-section-title">Set min/max value</view>
      <view class="body-view">
        <slider value="{{100}}" bindchange="sliderChange" min="{{50}}" max="{{200}}" show-value="{{true}}"></slider>
      </view>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">controlled</view>
      <view class="body-view">
        <slider value="{{controlledValue}}" bindchange="onControlledValueChange" min="{{50}}" max="{{200}}" show-value="{{true}}" />

        <slider value="{{controlledValue}}" bindchange="onControlledValueChange" min="{{50}}" max="{{200}}" show-value="{{true}}" />
      </view>
    </view>
  </view>

  <view style="margin: 24px;">
    normal Taroslider
    <slider />
  </view>
  <view style="position: relative;margin: 24; ">
    with position: relative
    <slider />
  </view>
</view>
```

js

```js
Page({
  data: {
    controlledValue: 50,
  },
  sliderChange(e) {
    console.log("slider fire change event，value:", e.detail.value);
  },
  sliderClick(e) {
    console.log("slider fire click event，value:", e.detail.value);
  },
  sliderLonePress(e) {
    console.log("slider fire lonePress event，value:", e.detail.value);
  },
  onControlledValueChange(e) {
    console.log("slider fire change event，value:", e.detail.value);
    this.setData({
      controlledValue: e.detail.value,
    });
  },
});
```

## Props

| Name               | Type      | Description                                                    | Default                  |
| ------------------ | --------- | -------------------------------------------------------------- | ------------------------ |
| `min`              | `number`  | Least value                                                    | `0`                      |
| `max`              | `number`  | Maximum value                                                  | `100`                    |
| `step`             | `number`  | Step size must be greater than 0 and can be(Max - Min) integer | `1`                      |
| `disabled`         | `boolean` | Is it disabled?                                                | `false`                  |
| `value`            | `number`  | Current value                                                  |                          |
| `show-value`       | `boolean` | Displays current value                                         | `false`                  |
| `active-color`     | `string`  | Selected color                                                 | `\`var(--bnui-primay)\`` |
| `background-color` | `string`  | Background Bar Color                                           | `"#e9e9e9"`              |

## Events

| Name             | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `bindchange`     | `bindchange` Event triggered after completing a drag, event.detail = `{value}` |
| `bindchanging`   | `bindchaning` Event triggered during drag, event. detail = `{value}`           |
| `bindtap`        | `bindtap` Event tap                                                            |
| `bindtapcapture` | `bindtapcapture` Event tap                                                     |