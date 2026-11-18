---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Icon
api_type: Guide
updated_at: 2026-11-18 02:31:25.285374
---

# icon

Icon.

## Props

| Property | Type          | Default Value | Required | Description                                                                                                                                                                                                                                                                                |
| -------- | ------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type     | String        |               | yes      | Type of icon, valid value: circle,download,info,safe-success, safe-warn,success,success-circle,success-no-circle,waiting,waiting-circle,warn,info-circle,cancel,search,clear, back,delete,success-no-circle-thin,arrow,arrow-bold,back-arrow,back-arrow-thin,close,close-thin,back-circle. |
| size     | number/string | 23            | no       | The size of the icon.                                                                                                                                                                                                                                                                      |
| color    | String        |               | no       | Icon color, with css color.                                                                                                                                                                                                                                                                |

**Example**

js

```js
Page({
  data: {
    iconSize: [20, 30, 40, 50, 60, 70],
    iconColor: ["red", "orange", "yellow", "green", "rgb(0,255,255)", "blue", "purple"],
    iconType: ["circle", "download", "info", "safe-success", "safe-warn", "success", "success-circle", "success-no-circle", "waiting", "waiting-circle", "warn", "info-circle", "cancel", "search", "clear", "back", " delete", "success-no-circle-thin", "arrow", "arrow-bold", "back-arrow", "back-arrow-thin", "close", "close-thin", "back-circle"],
  },
});
```

bxml

```html
<view class="group">
  <block bn:for="{{iconSize}}">
    <icon type="success" size="{{item}}" />
  </block>
</view>

<view class="group">
  <block bn:for="{{iconType}}">
    <icon type="{{item}}" size="40" />
  </block>
</view>

<view class="group">
  <block bn:for="{{iconColor}}">
    <icon type="success" size="40" color="{{item}}" />
  </block>
</view>
```

bxss

```css
.intro {
  margin: 30px;
  text-align: center;
}
```

## Props

| Name              | Type                     | Description | Default   |
| ----------------- | ------------------------ | ----------- | --------- |
| `type` _required_ | `string`                 |             |           |
| `size`            | `string` &#124; `number` |             | `23`      |
| `color`           | `string`                 |             | `"black"` |

---

# icon

Icon.

## Props

| Property | Type          | Default Value | Required | Description                                                                                                                                                                                                                                                                                |
| -------- | ------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type     | String        |               | yes      | Type of icon, valid value: circle,download,info,safe-success, safe-warn,success,success-circle,success-no-circle,waiting,waiting-circle,warn,info-circle,cancel,search,clear, back,delete,success-no-circle-thin,arrow,arrow-bold,back-arrow,back-arrow-thin,close,close-thin,back-circle. |
| size     | number/string | 23            | no       | The size of the icon.                                                                                                                                                                                                                                                                      |
| color    | String        |               | no       | Icon color, with css color.                                                                                                                                                                                                                                                                |

**Example**

js

```js
Page({
  data: {
    iconSize: [20, 30, 40, 50, 60, 70],
    iconColor: ["red", "orange", "yellow", "green", "rgb(0,255,255)", "blue", "purple"],
    iconType: ["circle", "download", "info", "safe-success", "safe-warn", "success", "success-circle", "success-no-circle", "waiting", "waiting-circle", "warn", "info-circle", "cancel", "search", "clear", "back", " delete", "success-no-circle-thin", "arrow", "arrow-bold", "back-arrow", "back-arrow-thin", "close", "close-thin", "back-circle"],
  },
});
```

bxml

```html
<view class="group">
  <block bn:for="{{iconSize}}">
    <icon type="success" size="{{item}}" />
  </block>
</view>

<view class="group">
  <block bn:for="{{iconType}}">
    <icon type="{{item}}" size="40" />
  </block>
</view>

<view class="group">
  <block bn:for="{{iconColor}}">
    <icon type="success" size="40" color="{{item}}" />
  </block>
</view>
```

bxss

```css
.intro {
  margin: 30px;
  text-align: center;
}
```

## Props

| Name              | Type                     | Description | Default   |
| ----------------- | ------------------------ | ----------- | --------- |
| `type` _required_ | `string`                 |             |           |
| `size`            | `string` &#124; `number` |             | `23`      |
| `color`           | `string`                 |             | `"black"` |