---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/NestedScrollView
api_type: Guide
updated_at: 2026-11-21 18:42:18.493963
---

# nested-scroll-view

Nested scroll view component, supports nested scrolling and sticky header

**Example**

```html
<view class="page-body">
  <nested-scroll-view style="height: 100vh; width: 100%;" scroll-y="true" scroll-top="{{scrollTop}}" scroll-into-view="{{scrollIntoView}}" upper-threshold="50" lower-threshold="50" show-scrollbar="true" scroll-with-animation="true" bindscroll="onScroll" bindscrollstart="onScrollStart" bindscrollend="onScrollEnd" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower">
    <nested-scroll-header>
      <sticky-header offset-top="0">
        <view class="header">Sticky Header</view>
      </sticky-header>
    </nested-scroll-header>
    <nested-scroll-header>
      <view class="header">Unsticky Header</view>
    </nested-scroll-header>
    <nested-scroll-body>
      <nested-scroll-view scroll-y="true" style="height: calc(100vh - 100px); width: 100%;">
        <!-- Your content here -->
        <view class="nested-scroll-item" id="nested-item-1">1</view>
        <view class="nested-scroll-item" id="nested-item-2">2</view>
      </nested-scroll-view>
    </nested-scroll-body>
  </nested-scroll-view>
  <button bindtap="onScrollToTop" style="position: fixed; bottom: 20px; left: 20px;">Scroll to Top</button>
  <button bindtap="onScrollToView" style="position: fixed; bottom: 20px; right: 20px;">Scroll to View</button>
</view>
```

**Example**

```js
Page({
  data: {
    scrollTop: 0,
    scrollIntoView: "",
    upperThreshold: 50,
    lowerThreshold: 50,
    enhanced: true,
    showScrollbar: true,
    scrollWithAnimation: true,
  },
  onScroll(e) {
    console.log("Scroll event:", e.detail);
  },
  onScrollStart(e) {
    console.log("Scroll start event:", e.detail);
  },
  onScrollEnd(e) {
    console.log("Scroll end event:", e.detail);
  },
  onScrollToUpper(e) {
    console.log("Scrolled to upper threshold:", e.detail);
  },
  onScrollToLower(e) {
    console.log("Scrolled to lower threshold:", e.detail);
  },
  onScrollToView(e) {
    this.setData({
      scrollIntoView: "nested-item-1", // Change to the ID of the element you want to scroll to
    });
  },
  onScrollToTop() {
    this.setData({
      scrollTop: 0,
    });
  },
});
```

## Props

| Name                    | Type                     | Description                                                                                                                                                 | Default |
| ----------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `scroll-y`              | `boolean`                | Allow vertical scrolling, currently only supports vertical scrolling                                                                                        | `false` |
| `scroll-top`            | `string` &#124; `number` | Set vertical scroll bar position                                                                                                                            |         |
| `scroll-into-view`      | `string`                 | The value should be the ID of a child element (ID cannot start with a number). Set which direction to scroll, then scroll to the element in which direction |         |
| `upper-threshold`       | `string` &#124; `number` | When it is far from the top, the scrolltupper event is triggered                                                                                            | `50`    |
| `lower-threshold`       | `string` &#124; `number` | When it is far from the bottom, the scrollcolor event is triggered                                                                                          | `50`    |
| `enhanced`              | `boolean`                | Enable the scroll view enhancement feature. After enabling, you can operate scroll view through ScrollViewContext                                           | `false` |
| `show-scrollbar`        | `boolean`                | Enabled when `enhanced:true`, control the scrollbar show/hide                                                                                               | `true`  |
| `scroll-with-animation` | `boolean`                | Use animation transitions when setting scroll bar position                                                                                                  | `false` |
| `active`                | `boolean`                | Set horizontal scroll bar position                                                                                                                          | `true`  |

## Events

| Name                | Description                                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bindscroll`        | `bindscroll` Triggered when scrolling,<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY }`</li></ul>               |
| `bindscrollstart`   | `bindscrollstart` Triggered when scroll start, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth }`</li></ul> |
| `bindscrollend`     | `bindscrollend` Triggered when scroll end, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth }`</li></ul>     |
| `bindscrolltoupper` | `bindscrolltoupper` Scroll to the top/Triggered on the left                                                                                                                                                                    |
| `bindscrolltolower` | `bindscrolltolower` Scroll to the bottom/Triggered on the right                                                                                                                                                                |

---

# nested-scroll-view

Nested scroll view component, supports nested scrolling and sticky header

**Example**

```html
<view class="page-body">
  <nested-scroll-view style="height: 100vh; width: 100%;" scroll-y="true" scroll-top="{{scrollTop}}" scroll-into-view="{{scrollIntoView}}" upper-threshold="50" lower-threshold="50" show-scrollbar="true" scroll-with-animation="true" bindscroll="onScroll" bindscrollstart="onScrollStart" bindscrollend="onScrollEnd" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower">
    <nested-scroll-header>
      <sticky-header offset-top="0">
        <view class="header">Sticky Header</view>
      </sticky-header>
    </nested-scroll-header>
    <nested-scroll-header>
      <view class="header">Unsticky Header</view>
    </nested-scroll-header>
    <nested-scroll-body>
      <nested-scroll-view scroll-y="true" style="height: calc(100vh - 100px); width: 100%;">
        <!-- Your content here -->
        <view class="nested-scroll-item" id="nested-item-1">1</view>
        <view class="nested-scroll-item" id="nested-item-2">2</view>
      </nested-scroll-view>
    </nested-scroll-body>
  </nested-scroll-view>
  <button bindtap="onScrollToTop" style="position: fixed; bottom: 20px; left: 20px;">Scroll to Top</button>
  <button bindtap="onScrollToView" style="position: fixed; bottom: 20px; right: 20px;">Scroll to View</button>
</view>
```

**Example**

```js
Page({
  data: {
    scrollTop: 0,
    scrollIntoView: "",
    upperThreshold: 50,
    lowerThreshold: 50,
    enhanced: true,
    showScrollbar: true,
    scrollWithAnimation: true,
  },
  onScroll(e) {
    console.log("Scroll event:", e.detail);
  },
  onScrollStart(e) {
    console.log("Scroll start event:", e.detail);
  },
  onScrollEnd(e) {
    console.log("Scroll end event:", e.detail);
  },
  onScrollToUpper(e) {
    console.log("Scrolled to upper threshold:", e.detail);
  },
  onScrollToLower(e) {
    console.log("Scrolled to lower threshold:", e.detail);
  },
  onScrollToView(e) {
    this.setData({
      scrollIntoView: "nested-item-1", // Change to the ID of the element you want to scroll to
    });
  },
  onScrollToTop() {
    this.setData({
      scrollTop: 0,
    });
  },
});
```

## Props

| Name                    | Type                     | Description                                                                                                                                                 | Default |
| ----------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `scroll-y`              | `boolean`                | Allow vertical scrolling, currently only supports vertical scrolling                                                                                        | `false` |
| `scroll-top`            | `string` &#124; `number` | Set vertical scroll bar position                                                                                                                            |         |
| `scroll-into-view`      | `string`                 | The value should be the ID of a child element (ID cannot start with a number). Set which direction to scroll, then scroll to the element in which direction |         |
| `upper-threshold`       | `string` &#124; `number` | When it is far from the top, the scrolltupper event is triggered                                                                                            | `50`    |
| `lower-threshold`       | `string` &#124; `number` | When it is far from the bottom, the scrollcolor event is triggered                                                                                          | `50`    |
| `enhanced`              | `boolean`                | Enable the scroll view enhancement feature. After enabling, you can operate scroll view through ScrollViewContext                                           | `false` |
| `show-scrollbar`        | `boolean`                | Enabled when `enhanced:true`, control the scrollbar show/hide                                                                                               | `true`  |
| `scroll-with-animation` | `boolean`                | Use animation transitions when setting scroll bar position                                                                                                  | `false` |
| `active`                | `boolean`                | Set horizontal scroll bar position                                                                                                                          | `true`  |

## Events

| Name                | Description                                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bindscroll`        | `bindscroll` Triggered when scrolling,<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY }`</li></ul>               |
| `bindscrollstart`   | `bindscrollstart` Triggered when scroll start, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth }`</li></ul> |
| `bindscrollend`     | `bindscrollend` Triggered when scroll end, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth }`</li></ul>     |
| `bindscrolltoupper` | `bindscrolltoupper` Scroll to the top/Triggered on the left                                                                                                                                                                    |
| `bindscrolltolower` | `bindscrolltolower` Scroll to the bottom/Triggered on the right                                                                                                                                                                |