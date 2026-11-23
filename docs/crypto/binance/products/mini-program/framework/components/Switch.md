---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Switch
api_type: Guide
updated_at: 2026-11-23 18:42:36.578946
---

# Switch

Switch selector.

**Example**

js

```js
var pageData = {
  data: {
    switch1Checked: true,
    switch2Checked: false,
    switch1Style: "",
    switch2Style: "text-decoration: line-through",
  },
};
for (var i = 1; i <= 2; ++i) {
  (function (index) {
    pageData[`switch${index}Change`] = function (e) {
      console.log(`switch${index}发生change事件，携带值为`, e.detail.value);
      var obj = {};
      obj[`switch${index}Checked`] = e.detail.value;
      this.setData(obj);
      obj = {};
      obj[`switch${index}Style`] = e.detail.value ? "" : "text-decoration: line-through";
      this.setData(obj);
    };
  })(i);
}
Page(pageData);
```

bxml

```html
<view class="page">
  <view class="page__hd">
    <text class="page__title">switch</text>
    <text class="page__desc">开关</text>
  </view>
  <view class="page__bd">
    <view class="section section_gap">
      <view class="section__title">type="switch"</view>
      <view class="body-view">
        <switch checked="{{switch1Checked}}" bindchange="switch1Change" />
      </view>
    </view>

    <view class="section section_gap">
      <view class="section__title">type="checkbox"</view>
      <view class="body-view">
        <switch type="checkbox" checked="{{switch2Checked}}" bindchange="switch2Change" />
      </view>
    </view>
  </view>
</view>
```

**Bug & Tip**

- `tip`: When switching type comes with vibration feedback in iOS, can be set in the system -> Sound
  and touch -> System Tactile Feedback Shut Down

## Props

| Name       | Type      | Description                      | Default              |
| ---------- | --------- | -------------------------------- | -------------------- |
| `checked`  | `boolean` | If selected                      | `false`              |
| `disabled` | `boolean` | Is it disabled?                  | `false`              |
| `color`    | `string`  | Switch The color of css of color | `var(--bnui-primay)` |

## Events

| Name             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `bindtap`        | Tap event for the switch                                                |
| `bindtapcapture` | Tap capture event                                                       |
| `bindchange`     | checked Triggered when changed change Events, event.detail = `{ value}` |

---

# Switch

Switch selector.

**Example**

js

```js
var pageData = {
  data: {
    switch1Checked: true,
    switch2Checked: false,
    switch1Style: "",
    switch2Style: "text-decoration: line-through",
  },
};
for (var i = 1; i <= 2; ++i) {
  (function (index) {
    pageData[`switch${index}Change`] = function (e) {
      console.log(`switch${index}发生change事件，携带值为`, e.detail.value);
      var obj = {};
      obj[`switch${index}Checked`] = e.detail.value;
      this.setData(obj);
      obj = {};
      obj[`switch${index}Style`] = e.detail.value ? "" : "text-decoration: line-through";
      this.setData(obj);
    };
  })(i);
}
Page(pageData);
```

bxml

```html
<view class="page">
  <view class="page__hd">
    <text class="page__title">switch</text>
    <text class="page__desc">开关</text>
  </view>
  <view class="page__bd">
    <view class="section section_gap">
      <view class="section__title">type="switch"</view>
      <view class="body-view">
        <switch checked="{{switch1Checked}}" bindchange="switch1Change" />
      </view>
    </view>

    <view class="section section_gap">
      <view class="section__title">type="checkbox"</view>
      <view class="body-view">
        <switch type="checkbox" checked="{{switch2Checked}}" bindchange="switch2Change" />
      </view>
    </view>
  </view>
</view>
```

**Bug & Tip**

- `tip`: When switching type comes with vibration feedback in iOS, can be set in the system -> Sound
  and touch -> System Tactile Feedback Shut Down

## Props

| Name       | Type      | Description                      | Default              |
| ---------- | --------- | -------------------------------- | -------------------- |
| `checked`  | `boolean` | If selected                      | `false`              |
| `disabled` | `boolean` | Is it disabled?                  | `false`              |
| `color`    | `string`  | Switch The color of css of color | `var(--bnui-primay)` |

## Events

| Name             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `bindtap`        | Tap event for the switch                                                |
| `bindtapcapture` | Tap capture event                                                       |
| `bindchange`     | checked Triggered when changed change Events, event.detail = `{ value}` |