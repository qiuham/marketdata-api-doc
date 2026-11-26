---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/RadioGroup
api_type: Guide
updated_at: 2026-11-26 18:43:18.842608
---

# radio-group

Use radio-group to compose many radios by putting radios inside radio-group.

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section page-section-gap">
        <view class="page-section-title">Default Style</view>
        <radio value="cb" checked bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>
        <radio value="cb" bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>

        <view class="page-section-title">With label</view>
        <label class="radio" bindtap="onLabelClick">
          <radio value="cb" checked bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>
          Checked
        </label>
        <label class="radio"> <radio value="cb"></radio>Unchecked </label>
        <view class="page-section-title">disabled</view>
        <label class="radio"> <radio value="cb" disabled checked></radio>Checked </label>
        <label class="radio"> <radio value="cb" disabled></radio>Unchecked </label>

        <view class="page-section-title">Controlled</view>
        <label class="radio" bindtap="onControlledLabelTap">
          <radio value="cb" checked="{{checked}}"></radio>
          Checked
        </label>
        <button bindtap="onControlledButtonTap">Toggle checked</button>
      </view>
    </view>
    <view class="page-section">
      <view class="page-section-title">Recommended Styl</view>
      <view class="bnui-cells bnui-cells_after-title">
        <radio-group bindchange="radioChange" bindtap="onRadioGroupTap">
          <label class="bnui-cell bnui-check__label" bn:for="{{items}}" bn:key="index" bindtap="onLabelClick">
            <view class="bnui-cell__hd">
              <radio value="{{item.value}}" checked="{{item.checked}}" bindtap="onItemsRadioTap" bind:longpress="onItemsRadioLongpress"></radio>
            </view>
            <view class="bnui-cell__bd">{{item.name}}</view>
          </label>
        </radio-group>
      </view>
    </view>
  </view>
</view>
```

bxss

```css
.radio {
  margin-right: 20px;
}
```

js

```js
Page({
  data: {
    items: [
      { value: "USA", name: "USA" },
      { value: "CHN", name: "CHN", checked: true },
      { value: "BRA", name: "BRA" },
      { value: "JPN", name: "JPN" },
      { value: "ENG", name: "ENG" },
      { value: "FRA", name: "FRA" },
    ],
    checked: false,
  },
  onRadioTap(e) {
    console.log("[Click] radio", e);
  },
  onRadioLongPress(e) {
    console.log("[Click] radio bind:longpress", e);
  },
  onLabelClick(e) {
    console.log("[Click] label", e);
  },
  onControlledLabelTap() {
    this.setData({ checked: !this.data.checked });
  },
  onControlledButtonTap() {
    this.setData({ checked: !this.data.checked });
  },
  radioChange(e) {
    console.log("[RadioGroup] radio fires change event，value:", e.detail.value);
    const items = this.data.items;
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value;
    }
    this.setData({
      items,
    });
  },
  onRadioGroupTap(e) {
    console.log("[Click] RadioGroup", e);
  },
  onItemsRadioTap(e) {
    console.log("[Click] radio", e);
  },
  onItemsRadioLongpress(e) {
    console.log("[Click] radio bind:longpress", e);
  },
});
```

## Events

| Name         | Description                                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `bindchange` | The change event is triggered when the selected item in the radio-group changes, detail = {value:[array of values of the selected radio]} |

---

# radio-group

Use radio-group to compose many radios by putting radios inside radio-group.

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section page-section-gap">
        <view class="page-section-title">Default Style</view>
        <radio value="cb" checked bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>
        <radio value="cb" bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>

        <view class="page-section-title">With label</view>
        <label class="radio" bindtap="onLabelClick">
          <radio value="cb" checked bindtap="onRadioTap" bind:longpress="onRadioLongPress"></radio>
          Checked
        </label>
        <label class="radio"> <radio value="cb"></radio>Unchecked </label>
        <view class="page-section-title">disabled</view>
        <label class="radio"> <radio value="cb" disabled checked></radio>Checked </label>
        <label class="radio"> <radio value="cb" disabled></radio>Unchecked </label>

        <view class="page-section-title">Controlled</view>
        <label class="radio" bindtap="onControlledLabelTap">
          <radio value="cb" checked="{{checked}}"></radio>
          Checked
        </label>
        <button bindtap="onControlledButtonTap">Toggle checked</button>
      </view>
    </view>
    <view class="page-section">
      <view class="page-section-title">Recommended Styl</view>
      <view class="bnui-cells bnui-cells_after-title">
        <radio-group bindchange="radioChange" bindtap="onRadioGroupTap">
          <label class="bnui-cell bnui-check__label" bn:for="{{items}}" bn:key="index" bindtap="onLabelClick">
            <view class="bnui-cell__hd">
              <radio value="{{item.value}}" checked="{{item.checked}}" bindtap="onItemsRadioTap" bind:longpress="onItemsRadioLongpress"></radio>
            </view>
            <view class="bnui-cell__bd">{{item.name}}</view>
          </label>
        </radio-group>
      </view>
    </view>
  </view>
</view>
```

bxss

```css
.radio {
  margin-right: 20px;
}
```

js

```js
Page({
  data: {
    items: [
      { value: "USA", name: "USA" },
      { value: "CHN", name: "CHN", checked: true },
      { value: "BRA", name: "BRA" },
      { value: "JPN", name: "JPN" },
      { value: "ENG", name: "ENG" },
      { value: "FRA", name: "FRA" },
    ],
    checked: false,
  },
  onRadioTap(e) {
    console.log("[Click] radio", e);
  },
  onRadioLongPress(e) {
    console.log("[Click] radio bind:longpress", e);
  },
  onLabelClick(e) {
    console.log("[Click] label", e);
  },
  onControlledLabelTap() {
    this.setData({ checked: !this.data.checked });
  },
  onControlledButtonTap() {
    this.setData({ checked: !this.data.checked });
  },
  radioChange(e) {
    console.log("[RadioGroup] radio fires change event，value:", e.detail.value);
    const items = this.data.items;
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value;
    }
    this.setData({
      items,
    });
  },
  onRadioGroupTap(e) {
    console.log("[Click] RadioGroup", e);
  },
  onItemsRadioTap(e) {
    console.log("[Click] radio", e);
  },
  onItemsRadioLongpress(e) {
    console.log("[Click] radio bind:longpress", e);
  },
});
```

## Events

| Name         | Description                                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `bindchange` | The change event is triggered when the selected item in the radio-group changes, detail = {value:[array of values of the selected radio]} |