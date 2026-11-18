---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/View
api_type: Guide
updated_at: 2026-11-18 02:29:29.802715
---

# View

View container

**Example**

bxml

```html
<view bindtouchstart="touchstart"> {{msg}} </view>
```

js

```js
Page({
  data() {
    return {
      msg: "view container",
    };
  },
  touchstart() {
    console.log("touchstart");
  },
});
```

## Props

| Name                     | Type      | Description                                                                                        | Default  |
| ------------------------ | --------- | -------------------------------------------------------------------------------------------------- | -------- |
| `hover-class`            | `string`  | Specifies the style class to press down on. when hover-class="none" There is no click state effect | `"none"` |
| `hover-stop-propagation` | `boolean` | Specifies whether to prevent this node's ancestor from clicking                                    | `false`  |
| `hover-start-time`       | `number`  | How long does it take to click, in milliseconds?                                                   | `50`     |
| `hover-stay-time`        | `number`  | Click hold time after finger release, in milliseconds                                              | `400`    |
| `catch-move`             | `boolean` | prevent scroll event's propagation                                                                 | `false`  |
| `no-drag-propagation`    | `boolean` | prevent scroll event's propagation jssdk > 4.33.0                                                  | `false`  |

## Events

| Name             | Description            |
| ---------------- | ---------------------- |
| `bindtouchstart` | Touch start event trap |

---

# View

View container

**Example**

bxml

```html
<view bindtouchstart="touchstart"> {{msg}} </view>
```

js

```js
Page({
  data() {
    return {
      msg: "view container",
    };
  },
  touchstart() {
    console.log("touchstart");
  },
});
```

## Props

| Name                     | Type      | Description                                                                                        | Default  |
| ------------------------ | --------- | -------------------------------------------------------------------------------------------------- | -------- |
| `hover-class`            | `string`  | Specifies the style class to press down on. when hover-class="none" There is no click state effect | `"none"` |
| `hover-stop-propagation` | `boolean` | Specifies whether to prevent this node's ancestor from clicking                                    | `false`  |
| `hover-start-time`       | `number`  | How long does it take to click, in milliseconds?                                                   | `50`     |
| `hover-stay-time`        | `number`  | Click hold time after finger release, in milliseconds                                              | `400`    |
| `catch-move`             | `boolean` | prevent scroll event's propagation                                                                 | `false`  |
| `no-drag-propagation`    | `boolean` | prevent scroll event's propagation jssdk > 4.33.0                                                  | `false`  |

## Events

| Name             | Description            |
| ---------------- | ---------------------- |
| `bindtouchstart` | Touch start event trap |