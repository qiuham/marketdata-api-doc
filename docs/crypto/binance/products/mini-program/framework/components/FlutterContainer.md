---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/FlutterContainer
api_type: Guide
updated_at: 2026-11-26 18:44:00.401233
---

# Container

Container.

After the container component is set to visible to true for the first time, the internal components
are cached. Avoid duplicate rendering of pages and keep internal component states updated.

**Example**

js

```js
Page({
  data: {
    visible: false,
  },
  toggle() {
    this.setData({
      visible: !this.data.visible,
    });
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <head title="Container"></head>
    <view class="page-body">
      <container visible="{{visible}}">
        <view>your page A</view>
      </container>
      <container visible="{{!visible}}">
        <view>your page B</view>
      </container>
      <button ontap="toggle">toggle visible</button>
    </view>
  </view>
</theme-context>
```

## Props

| Name      | Type      | Description | Default |
| --------- | --------- | ----------- | ------- |
| `visible` | `boolean` |             | `false` |

---

# Container

Container.

After the container component is set to visible to true for the first time, the internal components
are cached. Avoid duplicate rendering of pages and keep internal component states updated.

**Example**

js

```js
Page({
  data: {
    visible: false,
  },
  toggle() {
    this.setData({
      visible: !this.data.visible,
    });
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <head title="Container"></head>
    <view class="page-body">
      <container visible="{{visible}}">
        <view>your page A</view>
      </container>
      <container visible="{{!visible}}">
        <view>your page B</view>
      </container>
      <button ontap="toggle">toggle visible</button>
    </view>
  </view>
</theme-context>
```

## Props

| Name      | Type      | Description | Default |
| --------- | --------- | ----------- | ------- |
| `visible` | `boolean` |             | `false` |