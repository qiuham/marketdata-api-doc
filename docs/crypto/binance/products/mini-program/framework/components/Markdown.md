---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Markdown
api_type: Guide
updated_at: 2026-11-24 18:42:55.684211
---

# markdown

**Example**

```bxml
 <markdown
   content="{{content}}"
   bind:taplink="onTapLink"
 >
</markdown>
```

```js
Page({
  data: {
    content: "## Hello World\n\nThis is a markdown editor\n**bold**\n*italic*\n\n[link: tiptap-markdown](https://github.com/aguingand/tiptap-markdown)\n\n[deeplink](bnc://app.binance.com/mp/app?appId=bqpqWKnedCqoZ3wVcx4z98)\n![](https://public.bnbstatic.com/static/images/common/ogImage.jpg)",
    editorStyle: "height: calc(100% - 50px)",
  },
  onLoad() {},
  onTapLink(e) {
    console.log("onTapLink ===>", e);
  },
});
```

- **remark** - sdk >= 4.35.0

## Props

| Name      | Type     | Description |
| --------- | -------- | ----------- |
| `content` | `string` | &nbsp;      |

## Events

| Name          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `bindtaplink` | when the link has clicked, `taplink` will be emitted |

---

# markdown

**Example**

```bxml
 <markdown
   content="{{content}}"
   bind:taplink="onTapLink"
 >
</markdown>
```

```js
Page({
  data: {
    content: "## Hello World\n\nThis is a markdown editor\n**bold**\n*italic*\n\n[link: tiptap-markdown](https://github.com/aguingand/tiptap-markdown)\n\n[deeplink](bnc://app.binance.com/mp/app?appId=bqpqWKnedCqoZ3wVcx4z98)\n![](https://public.bnbstatic.com/static/images/common/ogImage.jpg)",
    editorStyle: "height: calc(100% - 50px)",
  },
  onLoad() {},
  onTapLink(e) {
    console.log("onTapLink ===>", e);
  },
});
```

- **remark** - sdk >= 4.35.0

## Props

| Name      | Type     | Description |
| --------- | -------- | ----------- |
| `content` | `string` | &nbsp;      |

## Events

| Name          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `bindtaplink` | when the link has clicked, `taplink` will be emitted |