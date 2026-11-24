---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/WebView
api_type: Guide
updated_at: 2026-11-24 18:42:16.328834
---

# WebView

A container that hosts web pages. Will automatically cover the entire Mini Program page,**Personal
type Mini Program is not supported for the time being.**

**Example**

```js
Page({
  data: {},
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {},
  onReady() {},
  onWebViewLoad(e) {
    console.log("[WebView] onLoad", e.detail);
  },
  onWebViewError(e) {
    console.log("[WebView] onError", e.detail);
  },
  async onWebViewMessage(e) {
    await bn.showModal({
      title: "Message From WebView",
      content: JSON.stringify(e.detail.data),
    });
    bn.createSelectorQuery()
      .select(".web-view")
      .context((result) => {
        result.context.postMessage("hey!");
      })
      .exec();
  },
});
```

**Bug & Tip**

- `tip`：Inside the page iframe The domain name also needs to be configured into the domain
  whitelist.
- `tip`: On the developer tools, you can web-view Component by right-clicking - Debug, Open web-view
  Component debugging.
- `tip`: Each page can have only one web-view，web-view Automatically covers the entire page and
  overwrites other components.
- `tip`: web-view Division between web pages and Mini Programs is not supported JSSDK Provides
  communication beyond the interface provided by.
- `tip`: Avoid Chinese characters in links, and iOS There will be a problem to open the white
  screen, it is recommended to add EncodeURIComponent

## Props

| Name              | Type      | Description                                                                                 | Default |
| ----------------- | --------- | ------------------------------------------------------------------------------------------- | ------- |
| `src`             | `string`  | webview A link to a web page.                                                               |         |
| `injected`        | `unknown` | js script file to be injected before jump to any pages.                                     |         |
| `bounce`          | `boolean` |                                                                                             | `true`  |
| `loading-bar`     | `boolean` |                                                                                             | `true`  |
| `web-preferences` | `object`  |                                                                                             |         |
| `hidden`          | `boolean` | whether the webview is hidden                                                               | `false` |
| `handle-error`    | `boolean` | whether js has handled error or not. If true, native will show an error page. Default false | `false` |

---

# WebView

A container that hosts web pages. Will automatically cover the entire Mini Program page,**Personal
type Mini Program is not supported for the time being.**

**Example**

```js
Page({
  data: {},
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {},
  onReady() {},
  onWebViewLoad(e) {
    console.log("[WebView] onLoad", e.detail);
  },
  onWebViewError(e) {
    console.log("[WebView] onError", e.detail);
  },
  async onWebViewMessage(e) {
    await bn.showModal({
      title: "Message From WebView",
      content: JSON.stringify(e.detail.data),
    });
    bn.createSelectorQuery()
      .select(".web-view")
      .context((result) => {
        result.context.postMessage("hey!");
      })
      .exec();
  },
});
```

**Bug & Tip**

- `tip`：Inside the page iframe The domain name also needs to be configured into the domain
  whitelist.
- `tip`: On the developer tools, you can web-view Component by right-clicking - Debug, Open web-view
  Component debugging.
- `tip`: Each page can have only one web-view，web-view Automatically covers the entire page and
  overwrites other components.
- `tip`: web-view Division between web pages and Mini Programs is not supported JSSDK Provides
  communication beyond the interface provided by.
- `tip`: Avoid Chinese characters in links, and iOS There will be a problem to open the white
  screen, it is recommended to add EncodeURIComponent

## Props

| Name              | Type      | Description                                                                                 | Default |
| ----------------- | --------- | ------------------------------------------------------------------------------------------- | ------- |
| `src`             | `string`  | webview A link to a web page.                                                               |         |
| `injected`        | `unknown` | js script file to be injected before jump to any pages.                                     |         |
| `bounce`          | `boolean` |                                                                                             | `true`  |
| `loading-bar`     | `boolean` |                                                                                             | `true`  |
| `web-preferences` | `object`  |                                                                                             |         |
| `hidden`          | `boolean` | whether the webview is hidden                                                               | `false` |
| `handle-error`    | `boolean` | whether js has handled error or not. If true, native will show an error page. Default false | `false` |