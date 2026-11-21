---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Drawer
api_type: Guide
updated_at: 2026-11-21 18:42:59.448966
---

# Drawer

Drawer.

**Example**

js

```js
Page({
  data: {
    show: false,
  },
  setClose() {
    this.setData({ show: false });
  },
});
```

bxml

```html
<drawer maskClass="mask-class" visible="{{show}}" bindclose="setClose" direction="bottom" draggable="true">
  <scroll-view scrollY>
    <view>item1</view>
  </scroll-view>
</drawer>
```

bxss

```css
.mask-class {
}
```

## Props

| Name                  | Type      | Description | Default    |
| --------------------- | --------- | ----------- | ---------- |
| `direction`           | `string`  |             | `"bottom"` |
| `teleport-to`         | `string`  |             | `""`       |
| `visible`             | `boolean` |             | `false`    |
| `mask-closable`       | `boolean` |             | `true`     |
| `draggable`           | `boolean` |             | `false`    |
| `container-class`     | `string`  |             | `""`       |
| `mask-class`          | `string`  |             | `""`       |
| `content-class`       | `string`  |             | `""`       |
| `use-dark-mask`       | `boolean` |             | `false`    |
| `show-top-handle`     | `boolean` |             | `false`    |
| `transition-duration` | `number`  |             | `300`      |

## Events

| Name        | Description |
| ----------- | ----------- |
| `bindopen`  |             |
| `bindclose` | &nbsp;      |

---

# Drawer

Drawer.

**Example**

js

```js
Page({
  data: {
    show: false,
  },
  setClose() {
    this.setData({ show: false });
  },
});
```

bxml

```html
<drawer maskClass="mask-class" visible="{{show}}" bindclose="setClose" direction="bottom" draggable="true">
  <scroll-view scrollY>
    <view>item1</view>
  </scroll-view>
</drawer>
```

bxss

```css
.mask-class {
}
```

## Props

| Name                  | Type      | Description | Default    |
| --------------------- | --------- | ----------- | ---------- |
| `direction`           | `string`  |             | `"bottom"` |
| `teleport-to`         | `string`  |             | `""`       |
| `visible`             | `boolean` |             | `false`    |
| `mask-closable`       | `boolean` |             | `true`     |
| `draggable`           | `boolean` |             | `false`    |
| `container-class`     | `string`  |             | `""`       |
| `mask-class`          | `string`  |             | `""`       |
| `content-class`       | `string`  |             | `""`       |
| `use-dark-mask`       | `boolean` |             | `false`    |
| `show-top-handle`     | `boolean` |             | `false`    |
| `transition-duration` | `number`  |             | `300`      |

## Events

| Name        | Description |
| ----------- | ----------- |
| `bindopen`  |             |
| `bindclose` | &nbsp;      |