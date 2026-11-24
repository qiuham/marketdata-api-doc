---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/ScrollView
api_type: Guide
updated_at: 2026-11-24 18:42:38.689065
---

# scroll-view

Scrollable view area. A view group that allows the view hierarchy placed within it to be scrolled.
When using vertical scrolling, you need to give the scroll view a fixed height.

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section-title">
      <text>scrollY Vertical Scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scrollY style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindtap="onTap" bind:longpress="onLongpress" bindscroll="onScroll">
        <view class="scroll-view-item demo-text-1"></view>
        <view class="scroll-view-item demo-text-2"></view>
        <view class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">
      <text>scroll-x="{{true}}" Horizontal Scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style=" width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scrollLeft="{{25}}">
        <view class="scroll-view-item_H demo-text-1"></view>
        <view class="scroll-view-item_H demo-text-2"></view>
        <view class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-body">
    <view class="page-section-title">
      <text>scroll-y ScrollIntoView 2 item</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scroll-into-view="{{scrollIntoView}}">
        <view id="demo1" class="scroll-view-item demo-text-1"></view>
        <view id="demo2" class="scroll-view-item demo-text-2"></view>
        <view id="demo3" class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">
      <text>scroll-x ScrollIntoView 2 item</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style="width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scroll-into-view="{{scrollIntoView}}">
        <view id="demo1" class="scroll-view-item_H demo-text-1"></view>
        <view id="demo2" class="scroll-view-item_H demo-text-2"></view>
        <view id="demo3" class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-body">
    <view class="page-section-title">
      <text>Vertical Scroll with infinite scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltolower="loadMore">
        <view bn:for="{{items}}" bn:key="index" class="scroll-view-item demo-text-{{(index % 3 + 1)}}"></view>
      </scroll-view>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">
      <text>enhanced, fastDeceleration</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style="width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" enhanced scroll-left="{{25}}" fastDeceleration>
        <view class="scroll-view-item_H demo-text-1"></view>
        <view class="scroll-view-item_H demo-text-2"></view>
        <view class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>

    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindtap="onTap" bind:longpress="onLongpress" bindscroll="onScroll" scroll-top="{{25}}" enhanced fastDeceleration>
        <view class="scroll-view-item demo-text-1"></view>
        <view class="scroll-view-item demo-text-2"></view>
        <view class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
</view>
```

bxss

```css
.page-section-spacing {
  margin-top: 30px;
}
.scroll-view_H {
  white-space: nowrap;
}
.scroll-view-item {
  height: 150px;
}
.scroll-view-item_H {
  display: inline-block;
  width: 100%;
  height: 150px;
}

.demo-text-1 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #1aad19;
  color: #ffffff;
  font-size: 18px;
}
.demo-text-1:before {
  content: "A";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.demo-text-2 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #2782d7;
  color: #ffffff;
  font-size: 18px;
}
.demo-text-2:before {
  content: "B";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.demo-text-3 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #f1f1f1;
  color: #353535;
  font-size: 18px;
}
.demo-text-3:before {
  content: "C";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

js

```js
Page({
  data: {
    items: new Array(3).fill(1),
    scrollTop: 25,
    scrollIntoView: "demo3",
  },
  onShow() {
    setTimeout(() => {
      this.setData({
        scrollTop: 50,
        scrollIntoView: "demo2",
      });
    }, 3000);
  },
  onScroll(e) {
    console.log("onScroll", e);
  },
  onScrollToUpper(e) {
    console.log("onScrollToUpper", e);
  },
  onScrollToLower(e) {
    console.log("onScrollToLower", e);
  },
  onTap(e) {
    console.log(`[scroll-view] bindtap`, e);
  },
  onLongpress(e) {
    console.log(`[scroll-view] longpress`, e);
  },
  scrollToTop() {},
  loadMore() {
    this.setData({
      items: [...this.data.items, ...new Array(3).fill(1)],
    });
  },
});
```

**Bug & Tip**

- `tip`: The priority of scroll-into-view is higher than that of scroll-top.
- `tip`: Scrolling in the scroll-view will prevent the page from bouncing back, so scrolling in the
  scroll-view cannot trigger onpulldownrefresh.
- `tip`: To use the pull-down refresh, please use the scroll of the page instead of the scroll-view,
  so that you can return to the top of the page by clicking the status bar at the top.

## Props

| Name                         | Type                     | Description                                                                                                                                                                                                                                            | Default      |
| ---------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `scroll-x`                   | `boolean`                | Allow lateral scrolling                                                                                                                                                                                                                                | `false`      |
| `scroll-y`                   | `boolean`                | Allow vertical scrolling                                                                                                                                                                                                                               | `false`      |
| `scroll-top`                 | `string` &#124; `number` | Set vertical scroll bar position                                                                                                                                                                                                                       |              |
| `scroll-left`                | `string` &#124; `number` | Set horizontal scroll bar position                                                                                                                                                                                                                     |              |
| `scroll-into-view`           | `string`                 | The value should be the ID of a child element (ID cannot start with a number). Set which direction to scroll, then scroll to the element in which direction                                                                                            |              |
| `scroll-into-view-alignment` | `string`                 | set alignment of target view when scroll into the view, support from jssdk >= 4.17.0                                                                                                                                                                   | `"start"`    |
| `upper-threshold`            | `string` &#124; `number` | When it is far from the top / left, the scrolltupper event is triggered                                                                                                                                                                                | `50`         |
| `lower-threshold`            | `string` &#124; `number` | When it is far from the bottom / right, the scrollcolor event is triggered                                                                                                                                                                             | `50`         |
| `enhanced`                   | `boolean`                | Enable the scroll view enhancement feature. After enabling, you can operate scroll view through ScrollViewContext                                                                                                                                      | `false`      |
| `fast-deceleration`          | `boolean`                | Sliding deceleration rate control (effective after the enhanced attribute is turned on at the same time)                                                                                                                                               | `false`      |
| `show-scrollbar`             | `boolean`                | Enabled when `enhanced:true`, control the scrollbar show/hide                                                                                                                                                                                          | `true`       |
| `refresher-enabled`          | `boolean`                | Enable pull-down refresh, support from jssdk >= 4.9.0                                                                                                                                                                                                  | `false`      |
| `refresher-threshold`        | `number`                 | refresher threshold to trigger refresh (in px), support from jssdk >= 4.9.0                                                                                                                                                                            | `45`         |
| `refresher-default-style`    | `string`                 | refresher default style, support from jssdk >= 4.9.0 options: black, white, none                                                                                                                                                                       | `"black"`    |
| `refresher-background`       | `string`                 | refresher background style, support from jssdk >= 4.9.0                                                                                                                                                                                                | `"#FFF"`     |
| `refresher-triggered`        | `boolean`                | is refresher triggered, support from jssdk >= 4.9.0                                                                                                                                                                                                    | `false`      |
| `scroll-anchoring`           | `boolean`                | solve the problem of content jumping from jssdk >= 4.14.0                                                                                                                                                                                              |              |
| `scroll-with-animation`      | `boolean`                | Use animation transitions when setting scroll bar position, support from jssdk >= 4.17.0                                                                                                                                                               | `false`      |
| `scroll-speed-limit`         | `number`                 | Scroll pixels per millisecond, Limit scroll speed, support from jssdk >= 4.18.0                                                                                                                                                                        | `"Infinity"` |
| `type`                       | `string`                 | Skyline props for better long list performance, support from jssdk >= 4.31.0                                                                                                                                                                           |              |
| `extra`                      | `object`                 | Business related-custom data, support from jssdk >= 4.32.0                                                                                                                                                                                             |              |
| `bounces`                    | `boolean`                |                                                                                                                                                                                                                                                        | `true`       |
| `virtual-list-buffer`        | `number`                 |                                                                                                                                                                                                                                                        | `250`        |
| `enable-back-to-top`         | `boolean`                | Enables the scroll bar to return to the top when the top status bar is tapped on iOS or the title bar is double-tapped on Android. Only vertical scrolling is supported. iOS support from jssdk >= 4.44.0, Android should support from jssdk >= 4.45.0 | `false`      |

## Events

| Name                        | Description                                                                                                                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindscroll`                | `bindscroll` Triggered when scrolling,<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth, deltaX, deltaY }`</li></ul>               |
| `bindscrollstart`           | `bindscrollstart` Triggered when scroll start, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth }`</li></ul> |
| `bindscrollend`             | `bindscrollend` Triggered when scroll end, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth }`</li></ul>     |
| `bindscrolltoupper`         | `bindscrolltoupper` Scroll to the top/Triggered on the left                                                                                                                                                                                 |
| `bindscrolltolower`         | `bindscrolltolower` Scroll to the bottom/Triggered on the right                                                                                                                                                                             |
| `bindrefresherpulling`      | `bindrefresherpulling` Triggered when pulling down                                                                                                                                                                                          |
| `bindrefresherrefresh`      | `bindrefresherrefresh` Triggered when refreshing                                                                                                                                                                                            |
| `bindrefresherrestore`      | `bindrefresherrestore` Triggered when pull-down refresher restoring                                                                                                                                                                         |
| `bindrefresherabort`        | `bindrefresherabort` Triggered when refresh aborting                                                                                                                                                                                        |
| `bindvirtuallistitemupdate` | `bindvitruallistitemupdate` Triggered when virtual list mounted item update                                                                                                                                                                 |

---

# scroll-view

Scrollable view area. A view group that allows the view hierarchy placed within it to be scrolled.
When using vertical scrolling, you need to give the scroll view a fixed height.

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section-title">
      <text>scrollY Vertical Scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scrollY style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindtap="onTap" bind:longpress="onLongpress" bindscroll="onScroll">
        <view class="scroll-view-item demo-text-1"></view>
        <view class="scroll-view-item demo-text-2"></view>
        <view class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">
      <text>scroll-x="{{true}}" Horizontal Scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style=" width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scrollLeft="{{25}}">
        <view class="scroll-view-item_H demo-text-1"></view>
        <view class="scroll-view-item_H demo-text-2"></view>
        <view class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-body">
    <view class="page-section-title">
      <text>scroll-y ScrollIntoView 2 item</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scroll-into-view="{{scrollIntoView}}">
        <view id="demo1" class="scroll-view-item demo-text-1"></view>
        <view id="demo2" class="scroll-view-item demo-text-2"></view>
        <view id="demo3" class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">
      <text>scroll-x ScrollIntoView 2 item</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style="width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" scroll-into-view="{{scrollIntoView}}">
        <view id="demo1" class="scroll-view-item_H demo-text-1"></view>
        <view id="demo2" class="scroll-view-item_H demo-text-2"></view>
        <view id="demo3" class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
  <view class="page-body">
    <view class="page-section-title">
      <text>Vertical Scroll with infinite scroll</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltolower="loadMore">
        <view bn:for="{{items}}" bn:key="index" class="scroll-view-item demo-text-{{(index % 3 + 1)}}"></view>
      </scroll-view>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">
      <text>enhanced, fastDeceleration</text>
    </view>
    <view class="page-section-spacing">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style="width: 100%;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindscroll="onScroll" enhanced scroll-left="{{25}}" fastDeceleration>
        <view class="scroll-view-item_H demo-text-1"></view>
        <view class="scroll-view-item_H demo-text-2"></view>
        <view class="scroll-view-item_H demo-text-3"></view>
      </scroll-view>
    </view>

    <view class="page-section-spacing">
      <scroll-view scroll-y="{{true}}" style="height: 150px;" bindscrolltoupper="onScrollToUpper" bindscrolltolower="onScrollToLower" bindtap="onTap" bind:longpress="onLongpress" bindscroll="onScroll" scroll-top="{{25}}" enhanced fastDeceleration>
        <view class="scroll-view-item demo-text-1"></view>
        <view class="scroll-view-item demo-text-2"></view>
        <view class="scroll-view-item demo-text-3"></view>
      </scroll-view>
    </view>
  </view>
</view>
```

bxss

```css
.page-section-spacing {
  margin-top: 30px;
}
.scroll-view_H {
  white-space: nowrap;
}
.scroll-view-item {
  height: 150px;
}
.scroll-view-item_H {
  display: inline-block;
  width: 100%;
  height: 150px;
}

.demo-text-1 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #1aad19;
  color: #ffffff;
  font-size: 18px;
}
.demo-text-1:before {
  content: "A";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.demo-text-2 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #2782d7;
  color: #ffffff;
  font-size: 18px;
}
.demo-text-2:before {
  content: "B";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.demo-text-3 {
  position: relative;
  align-items: center;
  justify-content: center;
  background-color: #f1f1f1;
  color: #353535;
  font-size: 18px;
}
.demo-text-3:before {
  content: "C";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

js

```js
Page({
  data: {
    items: new Array(3).fill(1),
    scrollTop: 25,
    scrollIntoView: "demo3",
  },
  onShow() {
    setTimeout(() => {
      this.setData({
        scrollTop: 50,
        scrollIntoView: "demo2",
      });
    }, 3000);
  },
  onScroll(e) {
    console.log("onScroll", e);
  },
  onScrollToUpper(e) {
    console.log("onScrollToUpper", e);
  },
  onScrollToLower(e) {
    console.log("onScrollToLower", e);
  },
  onTap(e) {
    console.log(`[scroll-view] bindtap`, e);
  },
  onLongpress(e) {
    console.log(`[scroll-view] longpress`, e);
  },
  scrollToTop() {},
  loadMore() {
    this.setData({
      items: [...this.data.items, ...new Array(3).fill(1)],
    });
  },
});
```

**Bug & Tip**

- `tip`: The priority of scroll-into-view is higher than that of scroll-top.
- `tip`: Scrolling in the scroll-view will prevent the page from bouncing back, so scrolling in the
  scroll-view cannot trigger onpulldownrefresh.
- `tip`: To use the pull-down refresh, please use the scroll of the page instead of the scroll-view,
  so that you can return to the top of the page by clicking the status bar at the top.

## Props

| Name                         | Type                     | Description                                                                                                                                                                                                                                            | Default      |
| ---------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `scroll-x`                   | `boolean`                | Allow lateral scrolling                                                                                                                                                                                                                                | `false`      |
| `scroll-y`                   | `boolean`                | Allow vertical scrolling                                                                                                                                                                                                                               | `false`      |
| `scroll-top`                 | `string` &#124; `number` | Set vertical scroll bar position                                                                                                                                                                                                                       |              |
| `scroll-left`                | `string` &#124; `number` | Set horizontal scroll bar position                                                                                                                                                                                                                     |              |
| `scroll-into-view`           | `string`                 | The value should be the ID of a child element (ID cannot start with a number). Set which direction to scroll, then scroll to the element in which direction                                                                                            |              |
| `scroll-into-view-alignment` | `string`                 | set alignment of target view when scroll into the view, support from jssdk >= 4.17.0                                                                                                                                                                   | `"start"`    |
| `upper-threshold`            | `string` &#124; `number` | When it is far from the top / left, the scrolltupper event is triggered                                                                                                                                                                                | `50`         |
| `lower-threshold`            | `string` &#124; `number` | When it is far from the bottom / right, the scrollcolor event is triggered                                                                                                                                                                             | `50`         |
| `enhanced`                   | `boolean`                | Enable the scroll view enhancement feature. After enabling, you can operate scroll view through ScrollViewContext                                                                                                                                      | `false`      |
| `fast-deceleration`          | `boolean`                | Sliding deceleration rate control (effective after the enhanced attribute is turned on at the same time)                                                                                                                                               | `false`      |
| `show-scrollbar`             | `boolean`                | Enabled when `enhanced:true`, control the scrollbar show/hide                                                                                                                                                                                          | `true`       |
| `refresher-enabled`          | `boolean`                | Enable pull-down refresh, support from jssdk >= 4.9.0                                                                                                                                                                                                  | `false`      |
| `refresher-threshold`        | `number`                 | refresher threshold to trigger refresh (in px), support from jssdk >= 4.9.0                                                                                                                                                                            | `45`         |
| `refresher-default-style`    | `string`                 | refresher default style, support from jssdk >= 4.9.0 options: black, white, none                                                                                                                                                                       | `"black"`    |
| `refresher-background`       | `string`                 | refresher background style, support from jssdk >= 4.9.0                                                                                                                                                                                                | `"#FFF"`     |
| `refresher-triggered`        | `boolean`                | is refresher triggered, support from jssdk >= 4.9.0                                                                                                                                                                                                    | `false`      |
| `scroll-anchoring`           | `boolean`                | solve the problem of content jumping from jssdk >= 4.14.0                                                                                                                                                                                              |              |
| `scroll-with-animation`      | `boolean`                | Use animation transitions when setting scroll bar position, support from jssdk >= 4.17.0                                                                                                                                                               | `false`      |
| `scroll-speed-limit`         | `number`                 | Scroll pixels per millisecond, Limit scroll speed, support from jssdk >= 4.18.0                                                                                                                                                                        | `"Infinity"` |
| `type`                       | `string`                 | Skyline props for better long list performance, support from jssdk >= 4.31.0                                                                                                                                                                           |              |
| `extra`                      | `object`                 | Business related-custom data, support from jssdk >= 4.32.0                                                                                                                                                                                             |              |
| `bounces`                    | `boolean`                |                                                                                                                                                                                                                                                        | `true`       |
| `virtual-list-buffer`        | `number`                 |                                                                                                                                                                                                                                                        | `250`        |
| `enable-back-to-top`         | `boolean`                | Enables the scroll bar to return to the top when the top status bar is tapped on iOS or the title bar is double-tapped on Android. Only vertical scrolling is supported. iOS support from jssdk >= 4.44.0, Android should support from jssdk >= 4.45.0 | `false`      |

## Events

| Name                        | Description                                                                                                                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindscroll`                | `bindscroll` Triggered when scrolling,<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth, deltaX, deltaY }`</li></ul>               |
| `bindscrollstart`           | `bindscrollstart` Triggered when scroll start, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth }`</li></ul> |
| `bindscrollend`             | `bindscrollend` Triggered when scroll end, support msv >= 4.36.0<br/>**Arguments**<br/><ul><li>**`event: detail: Object`** — The detail event object`Object{ scrollLeft, scrollTop, scrollHeight, scrollWidth, scrollWidth }`</li></ul>     |
| `bindscrolltoupper`         | `bindscrolltoupper` Scroll to the top/Triggered on the left                                                                                                                                                                                 |
| `bindscrolltolower`         | `bindscrolltolower` Scroll to the bottom/Triggered on the right                                                                                                                                                                             |
| `bindrefresherpulling`      | `bindrefresherpulling` Triggered when pulling down                                                                                                                                                                                          |
| `bindrefresherrefresh`      | `bindrefresherrefresh` Triggered when refreshing                                                                                                                                                                                            |
| `bindrefresherrestore`      | `bindrefresherrestore` Triggered when pull-down refresher restoring                                                                                                                                                                         |
| `bindrefresherabort`        | `bindrefresherabort` Triggered when refresh aborting                                                                                                                                                                                        |
| `bindvirtuallistitemupdate` | `bindvitruallistitemupdate` Triggered when virtual list mounted item update                                                                                                                                                                 |