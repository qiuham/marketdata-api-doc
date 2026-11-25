---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/RichText
api_type: Guide
updated_at: 2026-11-25 18:42:45.318413
---

# rich-text

rich text component.

**Example**

bxml

```html
<view class="container">
  <head title="rich-text"></head>
  <view class="page-section tc">
    <view class="page-body">
      <view class="rich-text-picker">
        <picker mode="selector" range="{{SPACE_RANGE}}" value="{{rangeIndex}}" bindchange="onPickChange">
          <view class="bnui-input"> Select a space:&nbsp; {{space || "default"}} </view>
        </picker>
      </view>

      <view class="page-section">
        <view class="page-section-title">HTML string</view>
        <view class="rich-text-textarea-wrapper">
          <textarea value="{{html}}" bindinput="onTextareaInput" maxlength="{{3000}}" />
        </view>
        <view class="rich-text-wrp">
          <rich-text nodes="{{html}}" space="{{space}}" bindtap="onRichTextTap" bind:longpress="onRichTextLongPress"></rich-text>
        </view>
      </view>

      <view class="page-section">
        <view class="page-section-title">Nodes</view>
        <view class="rich-text-textarea-wrapper">
          <textarea value="{{nodesStr}}" bindinput="onNodesChange" maxlength="{{3000}}" />
        </view>
        <view class="rich-text-wrp">
          <rich-text nodes="{{nodes}}" space="{{space || undefined}}"></rich-text>
        </view>
      </view>
    </view>
  </view>
</view>
```

js

```js
Page({
  data: {
    SPACE_RANGE: ["", "nbsp", "ensp", "emsp"],
    rangeIndex: 1,
    space: "nbsp",
    html: `<span>
      <div
        class="div_class"
        style="line-height: 16px; color: red;"
        id="div"
      >
        Hello&nbsp;World!1&emsp;2&ensp;3
      </div>
      <ol start="10">
        <li>ol with 'start=10'</li>
      </ol>
      <tr colspan="1" rowSpan="2">case-insensitive</tr>
      <img src="https://github.githubassets.com/images/icons/emoji/tada.png" style="width: 20px">
    </span>`,
    nodes: [
      {
        name: "div",
        attrs: {
          class: "div_class",
          style: "line-height: 16px; color: red;",
          id: "div",
        },
        children: [
          {
            type: "text",
            text: "Hello&nbsp;World!1&emsp;2&ensp;3",
          },
        ],
      },
    ],
    nodesStr: JSON.stringify(
      [
        {
          name: "div",
          attrs: {
            class: "div_class",
            style: "line-height: 16px; color: red;",
            id: "div",
          },
          children: [
            {
              type: "text",
              text: "Hello&nbsp;World!1&emsp;2&ensp;3",
            },
          ],
        },
      ],
      null,
      2,
    ),
  },
  onPickChange(e) {
    console.log("[rich-text] onPickChange", e);
    const space = this.data.SPACE_RANGE[e.detail.value];
    this.setData({
      space,
      rangeIndex: e.detail.value,
    });
  },
  onTextareaInput(e) {
    this.setData({
      html: e.detail.value,
    });
  },
  onRichTextTap() {
    console.log(`[rich-text] bindtap`, e);
  },
  onRichTextLongPress() {
    console.log(`[rich-text] onLongPress`, e);
  },
  onNodesChange(e) {
    try {
      const nodes = JSON.parse(e.detail.value);
      console.log("[rich-text] onNodesChange", nodes);
      this.setData({
        nodes,
        nodesStr: e.detail.value,
      });
    } catch (error) {
      console.log(error);
    }
  },
});
```

## Props

| Property | Type         | Default Value | Required | Description               |
| -------- | ------------ | ------------- | -------- | ------------------------- |
| nodes    | array/string | []            | true     | Node list/HTML String     |
| space    | string       | `text`        | false    | Display continuous spaces |

### Valid values of `nodes`

Now supports two types of nodes, distinguished by type, namely element nodes and text nodes, the
default is element nodes, HTML nodes displayed in the rich text area.

#### type = node

| Value      | Type   | Description               |
| ---------- | ------ | ------------------------- |
| `name`     | string | tag name                  |
| `attrs`    | Object | attributes                |
| `children` | array  | children of this element. |

#### type = text

| Value  | Type   | Description |
| ------ | ------ | ----------- |
| `text` | string | text        |

**Bug & Tip**

- `tip`: nodes Not recommended. String Type, performance will drop.
- `tip`: Masking all node events within a component.
- `tip`: attrs Property is not supported id Support class.
- `tip`: name Property is not case sensitive.
- `tip`: If an untrusted HTML node is used, the node and all its children are removed.
- `tip`: img Tags only support web pictures
- `tip`: If you use the rich-text Component, then only the custom component s wxss Style pair
  rich-text to hit the target class Entry into force.

---

# rich-text

rich text component.

**Example**

bxml

```html
<view class="container">
  <head title="rich-text"></head>
  <view class="page-section tc">
    <view class="page-body">
      <view class="rich-text-picker">
        <picker mode="selector" range="{{SPACE_RANGE}}" value="{{rangeIndex}}" bindchange="onPickChange">
          <view class="bnui-input"> Select a space:&nbsp; {{space || "default"}} </view>
        </picker>
      </view>

      <view class="page-section">
        <view class="page-section-title">HTML string</view>
        <view class="rich-text-textarea-wrapper">
          <textarea value="{{html}}" bindinput="onTextareaInput" maxlength="{{3000}}" />
        </view>
        <view class="rich-text-wrp">
          <rich-text nodes="{{html}}" space="{{space}}" bindtap="onRichTextTap" bind:longpress="onRichTextLongPress"></rich-text>
        </view>
      </view>

      <view class="page-section">
        <view class="page-section-title">Nodes</view>
        <view class="rich-text-textarea-wrapper">
          <textarea value="{{nodesStr}}" bindinput="onNodesChange" maxlength="{{3000}}" />
        </view>
        <view class="rich-text-wrp">
          <rich-text nodes="{{nodes}}" space="{{space || undefined}}"></rich-text>
        </view>
      </view>
    </view>
  </view>
</view>
```

js

```js
Page({
  data: {
    SPACE_RANGE: ["", "nbsp", "ensp", "emsp"],
    rangeIndex: 1,
    space: "nbsp",
    html: `<span>
      <div
        class="div_class"
        style="line-height: 16px; color: red;"
        id="div"
      >
        Hello&nbsp;World!1&emsp;2&ensp;3
      </div>
      <ol start="10">
        <li>ol with 'start=10'</li>
      </ol>
      <tr colspan="1" rowSpan="2">case-insensitive</tr>
      <img src="https://github.githubassets.com/images/icons/emoji/tada.png" style="width: 20px">
    </span>`,
    nodes: [
      {
        name: "div",
        attrs: {
          class: "div_class",
          style: "line-height: 16px; color: red;",
          id: "div",
        },
        children: [
          {
            type: "text",
            text: "Hello&nbsp;World!1&emsp;2&ensp;3",
          },
        ],
      },
    ],
    nodesStr: JSON.stringify(
      [
        {
          name: "div",
          attrs: {
            class: "div_class",
            style: "line-height: 16px; color: red;",
            id: "div",
          },
          children: [
            {
              type: "text",
              text: "Hello&nbsp;World!1&emsp;2&ensp;3",
            },
          ],
        },
      ],
      null,
      2,
    ),
  },
  onPickChange(e) {
    console.log("[rich-text] onPickChange", e);
    const space = this.data.SPACE_RANGE[e.detail.value];
    this.setData({
      space,
      rangeIndex: e.detail.value,
    });
  },
  onTextareaInput(e) {
    this.setData({
      html: e.detail.value,
    });
  },
  onRichTextTap() {
    console.log(`[rich-text] bindtap`, e);
  },
  onRichTextLongPress() {
    console.log(`[rich-text] onLongPress`, e);
  },
  onNodesChange(e) {
    try {
      const nodes = JSON.parse(e.detail.value);
      console.log("[rich-text] onNodesChange", nodes);
      this.setData({
        nodes,
        nodesStr: e.detail.value,
      });
    } catch (error) {
      console.log(error);
    }
  },
});
```

## Props

| Property | Type         | Default Value | Required | Description               |
| -------- | ------------ | ------------- | -------- | ------------------------- |
| nodes    | array/string | []            | true     | Node list/HTML String     |
| space    | string       | `text`        | false    | Display continuous spaces |

### Valid values of `nodes`

Now supports two types of nodes, distinguished by type, namely element nodes and text nodes, the
default is element nodes, HTML nodes displayed in the rich text area.

#### type = node

| Value      | Type   | Description               |
| ---------- | ------ | ------------------------- |
| `name`     | string | tag name                  |
| `attrs`    | Object | attributes                |
| `children` | array  | children of this element. |

#### type = text

| Value  | Type   | Description |
| ------ | ------ | ----------- |
| `text` | string | text        |

**Bug & Tip**

- `tip`: nodes Not recommended. String Type, performance will drop.
- `tip`: Masking all node events within a component.
- `tip`: attrs Property is not supported id Support class.
- `tip`: name Property is not case sensitive.
- `tip`: If an untrusted HTML node is used, the node and all its children are removed.
- `tip`: img Tags only support web pictures
- `tip`: If you use the rich-text Component, then only the custom component s wxss Style pair
  rich-text to hit the target class Entry into force.