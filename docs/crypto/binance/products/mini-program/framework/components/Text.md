---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Text
api_type: Guide
updated_at: 2026-11-20 18:43:32.688051
---

# Text

Text component for mp

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-spacing">
      <view class="text-box" scroll-y="true" scroll-top="{{scrollTop}}">
        <text>{{text}}</text>
      </view>
      <button disabled="{{!canAdd}}" bindtap="add">add line</button>
      <button disabled="{{!canRemove}}" bindtap="remove">remove line</button>
    </view>
  </view>
</view>
```

js

```js
const texts = ["2017 we created a new world", "2018 we have a group of people", "2019 we have become a family", "2020 most of us are happy"];
Page({
  onShareAppMessage() {
    return {
      title: "text",
      path: "page/component/pages/text/text",
    };
  },
  data: {
    text: "",
    canAdd: true,
    canRemove: false,
  },
  extraLine: [],
  add() {
    this.extraLine.push(texts[this.extraLine.length % 12]);
    this.setData({
      text: this.extraLine.join("\n"),
      canAdd: this.extraLine.length < 12,
      canRemove: this.extraLine.length > 0,
    });
    setTimeout(() => {
      this.setData({
        scrollTop: 99999,
      });
    }, 0);
  },
  remove() {
    if (this.extraLine.length > 0) {
      this.extraLine.pop();
      this.setData({
        text: this.extraLine.join("\n"),
        canAdd: this.extraLine.length < 12,
        canRemove: this.extraLine.length > 0,
      });
    }
    setTimeout(() => {
      this.setData({
        scrollTop: 99999,
      });
    }, 0);
  },
});
```

##### `Tips` & `Bug`:

- Decode can be parsed with `&nbsp` `&lt` `&gt` `&amp` `&apos` `&ensp` `&emsp`
- The standard of whitespace is not consistent across operating systems.

## Props

| Name          | Type                                     | Description                                                                                 | Default |
| ------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| `user-select` | `boolean`                                | Whether the text is optional, this property causes the text node to display as inline-block | `false` |
| `decode`      | `boolean`                                | Whether to decode                                                                           | `false` |
| `space`       | `'ensp'` &#124; `'emsp'` &#124; `'nbsp'` | Display continuous spaces                                                                   | &nbsp;  |

## Events

| Name       | Description |
| ---------- | ----------- |
| `bindcopy` | &nbsp;      |

---

# Text

Text component for mp

**Example**

bxml

```html
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-spacing">
      <view class="text-box" scroll-y="true" scroll-top="{{scrollTop}}">
        <text>{{text}}</text>
      </view>
      <button disabled="{{!canAdd}}" bindtap="add">add line</button>
      <button disabled="{{!canRemove}}" bindtap="remove">remove line</button>
    </view>
  </view>
</view>
```

js

```js
const texts = ["2017 we created a new world", "2018 we have a group of people", "2019 we have become a family", "2020 most of us are happy"];
Page({
  onShareAppMessage() {
    return {
      title: "text",
      path: "page/component/pages/text/text",
    };
  },
  data: {
    text: "",
    canAdd: true,
    canRemove: false,
  },
  extraLine: [],
  add() {
    this.extraLine.push(texts[this.extraLine.length % 12]);
    this.setData({
      text: this.extraLine.join("\n"),
      canAdd: this.extraLine.length < 12,
      canRemove: this.extraLine.length > 0,
    });
    setTimeout(() => {
      this.setData({
        scrollTop: 99999,
      });
    }, 0);
  },
  remove() {
    if (this.extraLine.length > 0) {
      this.extraLine.pop();
      this.setData({
        text: this.extraLine.join("\n"),
        canAdd: this.extraLine.length < 12,
        canRemove: this.extraLine.length > 0,
      });
    }
    setTimeout(() => {
      this.setData({
        scrollTop: 99999,
      });
    }, 0);
  },
});
```

##### `Tips` & `Bug`:

- Decode can be parsed with `&nbsp` `&lt` `&gt` `&amp` `&apos` `&ensp` `&emsp`
- The standard of whitespace is not consistent across operating systems.

## Props

| Name          | Type                                     | Description                                                                                 | Default |
| ------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| `user-select` | `boolean`                                | Whether the text is optional, this property causes the text node to display as inline-block | `false` |
| `decode`      | `boolean`                                | Whether to decode                                                                           | `false` |
| `space`       | `'ensp'` &#124; `'emsp'` &#124; `'nbsp'` | Display continuous spaces                                                                   | &nbsp;  |

## Events

| Name       | Description |
| ---------- | ----------- |
| `bindcopy` | &nbsp;      |