---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/FlutterSwiper
api_type: Guide
updated_at: 2026-11-22 18:40:40.325947
---

# swiper

swiper item container. Only the swiper-item component can be placed in it, otherwise it will cause
undefined problem.

**Example**

bxml

```html
<view class="page-body">
  <view class="page-section page-section-gap">
    <view class="page-section-title">Default Style</view>
    <view class="body-view"></view>
    <swiper indicator-dots="{{indicatorDots}}" autoplay="{{isAutoplay}}" indicator-color="{{indicatorColor}}" indicator-active-color="{{indicatorActiveColor}}" current="{{current}}" easing-function="{{easingFunction}}" interval="{{interval}}" duration="{{duration}}" circular="{{circular}}" vertical="{{vertical}}" display-multiple-items="{{displayMultipleItems}}" bindchange="onChange" bindtransition="onTransition" bindanimationfinish="onAnimationfinish">
      <block bn:for="{{bgColorGroups}}" bn:key="*this">
        <swiper-item style="{{'background-color:' + item}}">
          <view> {{item}} </view>
        </swiper-item>
      </block>
    </swiper>

    <view class="options_line" style="margin-top: 10px;">
      <button class="options_btn" bindtap="onAutoPlayChange">{{isAutoplay ? "stop automatically" : "play automatically"}}</button>
    </view>

    <view class="options_line">
      <button class="options_btn" bindtap="onCircularChange">{{circular ? "stop circular" : "play circular"}}</button>
    </view>
    <view class="options_line">
      <button class="options_btn" bindtap="onVerticalChange">{{vertical ? "horizontal" : "vertical"}}</button>
    </view>

    <view class="options_line">
      <button class="options_btn" bindtap="onIndicatorDotsChange">{{indicatorDots ? `hide indicatorDots` : `show indicatorDots`}}</button>
    </view>
    <view class="options_line">
      indicatorColor:
      <input class="options_input" value="{{indicatorColorInput}}" bindinput="onIndicatorColorInput" placeholder="Please input indicatorColor" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onIndicatorColorClick">update</button>
    </view>

    <view class="options_line">
      indicatorActiveColor:
      <input class="options_input" value="{{indicatorActiveColorInput}}" bindinput="onIndicatorActiveColorInput" placeholder="Please input indicatorColor" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onindicatorActiveColorClick">update</button>
    </view>

    <view class="options_line">
      current:
      <input class="options_input" value="{{currentInput}}" bindinput="onCurrentinputInput" placeholder="Please input current" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onCurrentinputClick">update</button>
    </view>

    <view class="options_line">
      easingFunction:
      <input class="options_input" value="{{easingFunctionInput}}" bindinput="onEasingFunctioninputInput" placeholder="Please input easingFunction" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onEasingFunctioninputClick">update</button>
    </view>

    <view class="options_line">
      interval:
      <input class="options_input" value="{{intervalInput}}" bindinput="onIntervalinputInput" placeholder="Please input interval" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onIntervalinputClick">update</button>
    </view>

    <view class="options_line">
      duration:
      <input class="options_input" value="{{durationInput}}" bindinput="onDurationinputInput" placeholder="Please input duration" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onDurationinputClick">update</button>
    </view>

    <view class="options_line">
      displayMultipleItems:
      <input class="options_input" value="{{displayMultipleItemsInput}}" bindinput="onDisplayMultipleItemsinputInput" placeholder="Please input displayMultipleItems" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onDisplayMultipleItemsinputClick">update</button>
    </view>

    <view class="options_line" bindtap="onAddBgColorGroupsClick">
      <button class="options_btn">add a black swiper item</button>
    </view>

    <view class="options_line" bindtap="onRemoveBgColorGroupsClick">
      <button class="options_btn">remove the last swiper item</button>
    </view>
  </view>
</view>
```

bxss:

```css
.bn-swiper-item {
  background: red;
}
.options_line {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.options_btn {
  margin-top: 0;
}
* .options_input {
  width: 100px;
  border: 1px solid #282828;
  border-radius: 4px;
  padding: 2px 12px;
  line-height: 1.6;
  font-size: 14px;
  font-weight: normal;
  box-sizing: border-box;
}
```

js

```js
Page({
  data: {
    bgColorGroups: ["yellow", "red", "orange", "green"],
    indicatorDots: true,
    isAutoplay: false,
    circular: true,
    vertical: false,
    indicatorColor: "white",
    indicatorActiveColor: "black", // *
    current: 0,
    easingFunction: this.easingFunction,
    displayMultipleItems: 1,
    indicatorColorInput: "white",
    indicatorActiveColorInput: "black",
    currentInput: 0,
    easingFunctionInput: "linear",
    interval: 3000,
    intervalInput: 3000,
    duration: 200,
    durationInput: 200,
    displayMultipleItemsInput: 1,
  },
  onLoad(query) {
    console.log("onload", this, query);
  },

  onShow() {
    console.log("onShow", this.data);
  },
  onReady() {
    console.log("onReady");
  },
  onHide() {
    console.log("onHide");
  },
  onTabItemTap(payload) {
    console.log("onTabItemTap", payload);
  },
  // swiper page method
  onAutoPlayChange: function () {
    this.setData({ isAutoplay: !this.data.isAutoplay });
  },
  onCircularChange() {
    this.setData({ circular: !this.data.circular });
  },
  onVerticalChange() {
    this.setData({ vertical: !this.data.vertical });
  },
  onIndicatorDotsChange() {
    this.setData({ indicatorDots: !this.data.indicatorDots });
  },
  onIndicatorColorInput(e) {
    this.setData({ indicatorColorInput: e.detail.value });
  },
  onIndicatorColorClick() {
    this.setData({
      indicatorColor: this.data.indicatorColorInput,
    });
  },
  onIndicatorActiveColorInput(e) {
    this.setData({ indicatorActiveColorInput: e.detail.value });
  },
  onindicatorActiveColorClick() {
    this.setData({
      indicatorActiveColor: this.data.indicatorActiveColorInput,
    });
  },
  onCurrentinputInput(e) {
    this.setData({ currentInput: Number(e.detail.value) });
  },
  onCurrentinputClick() {
    this.setData({
      current: this.data.currentInput,
    });
  },
  onEasingFunctioninputInput(e) {
    this.setData({ easingFunctionInput: e.detail.value });
  },
  onEasingFunctioninputClick() {
    this.setData({
      easingFunction: this.data.easingFunctionInput,
    });
  },
  onIntervalinputInput(e) {
    this.setData({ intervalInput: Number(e.detail.value) });
  },
  onIntervalinputClick() {
    this.setData({
      interval: this.data.intervalInput,
    });
  },
  onDurationinputInput(e) {
    this.setData({ durationInput: Number(e.detail.value) });
  },
  onDurationinputClick() {
    this.setData({
      duration: this.data.durationInput,
    });
  },
  onDisplayMultipleItemsinputInput(e) {
    this.setData({ displayMultipleItemsInput: e.detail.value });
  },
  onDisplayMultipleItemsinputClick() {
    this.setData({
      displayMultipleItems: this.data.displayMultipleItemsInput,
    });
  },
  onAddBgColorGroupsClick() {
    const newBgColorGroups = [...this.data.bgColorGroups];
    newBgColorGroups.push("black");
    this.setData({ bgColorGroups: newBgColorGroups });
  },
  onRemoveBgColorGroupsClick() {
    const newBgColorGroups = [...this.data.bgColorGroups];
    newBgColorGroups.length > 0 && newBgColorGroups.pop();
    this.setData({ bgColorGroups: newBgColorGroups });
  },

  onChange(e) {
    console.log("[View] onClick", e);
  },
  onTransition(e) {
    console.log("[View] onLongPress", e);
  },
  onAnimationfinish(e) {
    console.log("[View] onTouchStart", e);
  },
});
```

## Props

| Name                     | Type                 | Description                                                                                                                                                                                                      | Default               |
| ------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `indicator-dots`         | `boolean`            | whether to display panel indicator points                                                                                                                                                                        | `false`               |
| `indicator-color`        | `string`             | color of indicator                                                                                                                                                                                               | `"rgba(0, 0, 0, .3)"` |
| `indicator-active-color` | `string`             | color of active indicator                                                                                                                                                                                        | `"#000000"`           |
| `autoplay`               | `boolean`            | autoplay or not                                                                                                                                                                                                  | `false`               |
| `current`                | `number`             | the index of current swiper                                                                                                                                                                                      | `0`                   |
| `interval`               | `number`             | interval when using autoplay                                                                                                                                                                                     | `5000`                |
| `duration`               | `number`             | swipe animation duration                                                                                                                                                                                         | `500`                 |
| `circular`               | `boolean`            | when last one finished, whether turn to the first one                                                                                                                                                            | `false`               |
| `vertical`               | `boolean`            | vertical or not(horizontal)                                                                                                                                                                                      | `false`               |
| `previous-margin`        | `string`             | exposing a small part of the previous item (child element setting width/height: 100%; set img's width/height: inherit)                                                                                           | `"0px"`               |
| `next-margin`            | `string`             | exposing a small part of the next item (child element setting width/height: 100%; set img's width/height: inherit)                                                                                               | `"0px"`               |
| `snap-to-edge`           | `boolean`            | When the number of swiper-items is greater than or equal to 2, circular is turned off and previous-margin or next-margin is turned on, you can specify that this margin is applied to the first and last element | `false`               |
| `display-multiple-items` | `number`             |                                                                                                                                                                                                                  | `1`                   |
| `easing-function`        | `EasingFunctionName` | currently supported easingFunction: default,linear,easeInCubic,easeOutCubic,easeInOutCubic                                                                                                                       | `"default"`           |
| `layout-type`            | `string`             | rendering mode of swiper                                                                                                                                                                                         | `"normal"`            |
| `transform-type`         | `string`             |                                                                                                                                                                                                                  | `"scaleAndFade"`      |
| `indicator-type`         | `string`             |                                                                                                                                                                                                                  | `"normal"`            |
| `indicator-margin`       | `number`             |                                                                                                                                                                                                                  | `10`                  |
| `indicator-spacing`      | `number`             |                                                                                                                                                                                                                  | `4`                   |
| `indicator-radius`       | `number`             |                                                                                                                                                                                                                  | `4`                   |
| `indicator-width`        | `number`             |                                                                                                                                                                                                                  | `8`                   |
| `indicator-height`       | `number`             |                                                                                                                                                                                                                  | `8`                   |
| `indicator-alignment`    | `boolean`            |                                                                                                                                                                                                                  | `"auto"`              |
| `indicator-offset`       | `number[]`           |                                                                                                                                                                                                                  | `[0,0]`               |
| `scroll-with-animation`  | `boolean`            |                                                                                                                                                                                                                  | `true`                |
| `cache-extent`           | `number`             |                                                                                                                                                                                                                  | `0`                   |
| `rtl`                    | `boolean`            | TODO: Right-to-left sliding mode default value is false                                                                                                                                                          | `false`               |

## Events

| Name                         | Description                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `bindchange`                 | The change event is fired when the current changes，event.detail = {current, source}                            |
| `bindtransition`             | The transition event is triggered when the position of the swiper-item changes，event.detail = {dx: dx, dy: dy} |
| `bindanimationfinish`        | Triggered when the animation finished，event.detail = {current, source}                                         |
| `bindworklet:onscrollstart`  | triggered at the beginning of sliding only supporting worklet as a callback event.detail= {dx: dx, dy: dy}      |
| `bindworklet:onscrollupdate` | triggered when the sliding position is updated only supportinglets are supported event.detail= {dx: dx, dy: dy} |
| `bindworklet:onscrollend`    | triggered when the sliding ends only supporting worklet as a callback event.detail= {dx: dx, dy: dy}            |

---

# swiper

swiper item container. Only the swiper-item component can be placed in it, otherwise it will cause
undefined problem.

**Example**

bxml

```html
<view class="page-body">
  <view class="page-section page-section-gap">
    <view class="page-section-title">Default Style</view>
    <view class="body-view"></view>
    <swiper indicator-dots="{{indicatorDots}}" autoplay="{{isAutoplay}}" indicator-color="{{indicatorColor}}" indicator-active-color="{{indicatorActiveColor}}" current="{{current}}" easing-function="{{easingFunction}}" interval="{{interval}}" duration="{{duration}}" circular="{{circular}}" vertical="{{vertical}}" display-multiple-items="{{displayMultipleItems}}" bindchange="onChange" bindtransition="onTransition" bindanimationfinish="onAnimationfinish">
      <block bn:for="{{bgColorGroups}}" bn:key="*this">
        <swiper-item style="{{'background-color:' + item}}">
          <view> {{item}} </view>
        </swiper-item>
      </block>
    </swiper>

    <view class="options_line" style="margin-top: 10px;">
      <button class="options_btn" bindtap="onAutoPlayChange">{{isAutoplay ? "stop automatically" : "play automatically"}}</button>
    </view>

    <view class="options_line">
      <button class="options_btn" bindtap="onCircularChange">{{circular ? "stop circular" : "play circular"}}</button>
    </view>
    <view class="options_line">
      <button class="options_btn" bindtap="onVerticalChange">{{vertical ? "horizontal" : "vertical"}}</button>
    </view>

    <view class="options_line">
      <button class="options_btn" bindtap="onIndicatorDotsChange">{{indicatorDots ? `hide indicatorDots` : `show indicatorDots`}}</button>
    </view>
    <view class="options_line">
      indicatorColor:
      <input class="options_input" value="{{indicatorColorInput}}" bindinput="onIndicatorColorInput" placeholder="Please input indicatorColor" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onIndicatorColorClick">update</button>
    </view>

    <view class="options_line">
      indicatorActiveColor:
      <input class="options_input" value="{{indicatorActiveColorInput}}" bindinput="onIndicatorActiveColorInput" placeholder="Please input indicatorColor" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onindicatorActiveColorClick">update</button>
    </view>

    <view class="options_line">
      current:
      <input class="options_input" value="{{currentInput}}" bindinput="onCurrentinputInput" placeholder="Please input current" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onCurrentinputClick">update</button>
    </view>

    <view class="options_line">
      easingFunction:
      <input class="options_input" value="{{easingFunctionInput}}" bindinput="onEasingFunctioninputInput" placeholder="Please input easingFunction" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onEasingFunctioninputClick">update</button>
    </view>

    <view class="options_line">
      interval:
      <input class="options_input" value="{{intervalInput}}" bindinput="onIntervalinputInput" placeholder="Please input interval" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onIntervalinputClick">update</button>
    </view>

    <view class="options_line">
      duration:
      <input class="options_input" value="{{durationInput}}" bindinput="onDurationinputInput" placeholder="Please input duration" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onDurationinputClick">update</button>
    </view>

    <view class="options_line">
      displayMultipleItems:
      <input class="options_input" value="{{displayMultipleItemsInput}}" bindinput="onDisplayMultipleItemsinputInput" placeholder="Please input displayMultipleItems" maxlength="{{-1}}" />
      <button class="options_btn" bindtap="onDisplayMultipleItemsinputClick">update</button>
    </view>

    <view class="options_line" bindtap="onAddBgColorGroupsClick">
      <button class="options_btn">add a black swiper item</button>
    </view>

    <view class="options_line" bindtap="onRemoveBgColorGroupsClick">
      <button class="options_btn">remove the last swiper item</button>
    </view>
  </view>
</view>
```

bxss:

```css
.bn-swiper-item {
  background: red;
}
.options_line {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.options_btn {
  margin-top: 0;
}
* .options_input {
  width: 100px;
  border: 1px solid #282828;
  border-radius: 4px;
  padding: 2px 12px;
  line-height: 1.6;
  font-size: 14px;
  font-weight: normal;
  box-sizing: border-box;
}
```

js

```js
Page({
  data: {
    bgColorGroups: ["yellow", "red", "orange", "green"],
    indicatorDots: true,
    isAutoplay: false,
    circular: true,
    vertical: false,
    indicatorColor: "white",
    indicatorActiveColor: "black", // *
    current: 0,
    easingFunction: this.easingFunction,
    displayMultipleItems: 1,
    indicatorColorInput: "white",
    indicatorActiveColorInput: "black",
    currentInput: 0,
    easingFunctionInput: "linear",
    interval: 3000,
    intervalInput: 3000,
    duration: 200,
    durationInput: 200,
    displayMultipleItemsInput: 1,
  },
  onLoad(query) {
    console.log("onload", this, query);
  },

  onShow() {
    console.log("onShow", this.data);
  },
  onReady() {
    console.log("onReady");
  },
  onHide() {
    console.log("onHide");
  },
  onTabItemTap(payload) {
    console.log("onTabItemTap", payload);
  },
  // swiper page method
  onAutoPlayChange: function () {
    this.setData({ isAutoplay: !this.data.isAutoplay });
  },
  onCircularChange() {
    this.setData({ circular: !this.data.circular });
  },
  onVerticalChange() {
    this.setData({ vertical: !this.data.vertical });
  },
  onIndicatorDotsChange() {
    this.setData({ indicatorDots: !this.data.indicatorDots });
  },
  onIndicatorColorInput(e) {
    this.setData({ indicatorColorInput: e.detail.value });
  },
  onIndicatorColorClick() {
    this.setData({
      indicatorColor: this.data.indicatorColorInput,
    });
  },
  onIndicatorActiveColorInput(e) {
    this.setData({ indicatorActiveColorInput: e.detail.value });
  },
  onindicatorActiveColorClick() {
    this.setData({
      indicatorActiveColor: this.data.indicatorActiveColorInput,
    });
  },
  onCurrentinputInput(e) {
    this.setData({ currentInput: Number(e.detail.value) });
  },
  onCurrentinputClick() {
    this.setData({
      current: this.data.currentInput,
    });
  },
  onEasingFunctioninputInput(e) {
    this.setData({ easingFunctionInput: e.detail.value });
  },
  onEasingFunctioninputClick() {
    this.setData({
      easingFunction: this.data.easingFunctionInput,
    });
  },
  onIntervalinputInput(e) {
    this.setData({ intervalInput: Number(e.detail.value) });
  },
  onIntervalinputClick() {
    this.setData({
      interval: this.data.intervalInput,
    });
  },
  onDurationinputInput(e) {
    this.setData({ durationInput: Number(e.detail.value) });
  },
  onDurationinputClick() {
    this.setData({
      duration: this.data.durationInput,
    });
  },
  onDisplayMultipleItemsinputInput(e) {
    this.setData({ displayMultipleItemsInput: e.detail.value });
  },
  onDisplayMultipleItemsinputClick() {
    this.setData({
      displayMultipleItems: this.data.displayMultipleItemsInput,
    });
  },
  onAddBgColorGroupsClick() {
    const newBgColorGroups = [...this.data.bgColorGroups];
    newBgColorGroups.push("black");
    this.setData({ bgColorGroups: newBgColorGroups });
  },
  onRemoveBgColorGroupsClick() {
    const newBgColorGroups = [...this.data.bgColorGroups];
    newBgColorGroups.length > 0 && newBgColorGroups.pop();
    this.setData({ bgColorGroups: newBgColorGroups });
  },

  onChange(e) {
    console.log("[View] onClick", e);
  },
  onTransition(e) {
    console.log("[View] onLongPress", e);
  },
  onAnimationfinish(e) {
    console.log("[View] onTouchStart", e);
  },
});
```

## Props

| Name                     | Type                 | Description                                                                                                                                                                                                      | Default               |
| ------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `indicator-dots`         | `boolean`            | whether to display panel indicator points                                                                                                                                                                        | `false`               |
| `indicator-color`        | `string`             | color of indicator                                                                                                                                                                                               | `"rgba(0, 0, 0, .3)"` |
| `indicator-active-color` | `string`             | color of active indicator                                                                                                                                                                                        | `"#000000"`           |
| `autoplay`               | `boolean`            | autoplay or not                                                                                                                                                                                                  | `false`               |
| `current`                | `number`             | the index of current swiper                                                                                                                                                                                      | `0`                   |
| `interval`               | `number`             | interval when using autoplay                                                                                                                                                                                     | `5000`                |
| `duration`               | `number`             | swipe animation duration                                                                                                                                                                                         | `500`                 |
| `circular`               | `boolean`            | when last one finished, whether turn to the first one                                                                                                                                                            | `false`               |
| `vertical`               | `boolean`            | vertical or not(horizontal)                                                                                                                                                                                      | `false`               |
| `previous-margin`        | `string`             | exposing a small part of the previous item (child element setting width/height: 100%; set img's width/height: inherit)                                                                                           | `"0px"`               |
| `next-margin`            | `string`             | exposing a small part of the next item (child element setting width/height: 100%; set img's width/height: inherit)                                                                                               | `"0px"`               |
| `snap-to-edge`           | `boolean`            | When the number of swiper-items is greater than or equal to 2, circular is turned off and previous-margin or next-margin is turned on, you can specify that this margin is applied to the first and last element | `false`               |
| `display-multiple-items` | `number`             |                                                                                                                                                                                                                  | `1`                   |
| `easing-function`        | `EasingFunctionName` | currently supported easingFunction: default,linear,easeInCubic,easeOutCubic,easeInOutCubic                                                                                                                       | `"default"`           |
| `layout-type`            | `string`             | rendering mode of swiper                                                                                                                                                                                         | `"normal"`            |
| `transform-type`         | `string`             |                                                                                                                                                                                                                  | `"scaleAndFade"`      |
| `indicator-type`         | `string`             |                                                                                                                                                                                                                  | `"normal"`            |
| `indicator-margin`       | `number`             |                                                                                                                                                                                                                  | `10`                  |
| `indicator-spacing`      | `number`             |                                                                                                                                                                                                                  | `4`                   |
| `indicator-radius`       | `number`             |                                                                                                                                                                                                                  | `4`                   |
| `indicator-width`        | `number`             |                                                                                                                                                                                                                  | `8`                   |
| `indicator-height`       | `number`             |                                                                                                                                                                                                                  | `8`                   |
| `indicator-alignment`    | `boolean`            |                                                                                                                                                                                                                  | `"auto"`              |
| `indicator-offset`       | `number[]`           |                                                                                                                                                                                                                  | `[0,0]`               |
| `scroll-with-animation`  | `boolean`            |                                                                                                                                                                                                                  | `true`                |
| `cache-extent`           | `number`             |                                                                                                                                                                                                                  | `0`                   |
| `rtl`                    | `boolean`            | TODO: Right-to-left sliding mode default value is false                                                                                                                                                          | `false`               |

## Events

| Name                         | Description                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `bindchange`                 | The change event is fired when the current changes，event.detail = {current, source}                            |
| `bindtransition`             | The transition event is triggered when the position of the swiper-item changes，event.detail = {dx: dx, dy: dy} |
| `bindanimationfinish`        | Triggered when the animation finished，event.detail = {current, source}                                         |
| `bindworklet:onscrollstart`  | triggered at the beginning of sliding only supporting worklet as a callback event.detail= {dx: dx, dy: dy}      |
| `bindworklet:onscrollupdate` | triggered when the sliding position is updated only supportinglets are supported event.detail= {dx: dx, dy: dy} |
| `bindworklet:onscrollend`    | triggered when the sliding ends only supporting worklet as a callback event.detail= {dx: dx, dy: dy}            |