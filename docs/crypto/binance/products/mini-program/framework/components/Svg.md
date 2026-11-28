---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Svg
api_type: Guide
updated_at: 2026-11-28 18:40:50.495222
---

# svg

builtin svg component, will render raw svg tag

**Example**

js

```js
Page({
  data: {
    localImage: "pages/tabbar/component/resources/pic/1.jpg",
    remoteImage: "https://static.devfdg.net/image/julia/pie-chart-currentcolor.svg",
    colorChanged: false,
    svgStyle: "",
    colorClassChanged: false,
    colorClass: "",
    boxattrsChanged: false,
    boxattrs: { width: "48px", height: "48px" },
  },
  onChangeColor(e) {
    console.log(`[Svg] onChangeColor `, e);
    if (!this.data.colorChanged) {
      this.setData({ colorChanged: true, svgStyle: "color: #d22f2f;" });
    } else {
      this.setData({ colorChanged: false, svgStyle: "" });
    }
  },
  onChangeBoxAttr() {
    if (!this.data.boxattrsChanged) {
      this.setData({
        boxattrsChanged: true,
        boxattrs: { width: "96px", height: "96px" },
      });
    } else {
      this.setData({
        boxattrsChanged: false,
        boxattrs: { width: "48px", height: "48px" },
      });
    }
  },
});
```

bxml

```html
<view class="section-title">color change</view>
<view class="userinfo">
  <button bindtap="onChangeColor">Change Color</button>
</view>
<view class="image-container">
  <svg src="{{localImage}}" style="{{svgStyle}}"></svg>
</view>

<view class="section-title">box attributes</view>
<button bindtap="onChangeBoxAttr">Change Box Attributes</button>
<view class="image-container">
  <svg src="{{localImage}}" style="{{svgStyle}}" width="{{boxattrs.width}}" height="{{boxattrs.height}}"></svg>
</view>
<view>boxattrs: {{ boxattrs }}</view>

<view class="section-title">box attributes priority</view>
<view>set width & height at attribute with 48px</view>
<view>set width & height at style with 96px</view>
<view>svg will be 96px;</view>
<view class="image-container">
  <svg src="{{localImage}}" style="width: 96px; height: 96px;" width="48px" height="48px"></svg>
</view>
<view>set width & height at attribute with 96px</view>
<view>svg will be 96px;</view>
<view class="image-container">
  <svg src="{{localImage}}" width="96px" height="96px"></svg>
</view>

<view class="section-title">data url demo</view>
<view class="image-container">
  <svg src="{{dataUrlDemo}}"></svg>
</view>
```

### Bug & Tip

- `tip`: for keep same code between webview and flutter, recommand not use class to custom svg style
- `tip`: not support fully svg feature (document not ready)
- `tip`: could use data-url format and pass by `src`. supported schema `text/html`, `image/svg+xml`
  (don't forget encode url content)
- `tip`: style `width` and `height` have more priority than attribute `width` and `height`
- `tip`: for `padding` and `margin`, we recommand only use `margin` for better compatibility in
  webview and flutter

:::warn cannot direct receive svg content as child, eg `<svg><path>xxxx</path></svg>`, use `src`
instead :::

- **remark** - required jssdk >= 4.37.6
- **remark** - required bundlerversion >= 3.0.112
- **remark** - if use from uikit, need config RootProvider's `iconConfig` with `svgTag: true`

## Props

| Name             | Type      | Description                                                        | Default |
| ---------------- | --------- | ------------------------------------------------------------------ | ------- |
| `style`          | `string`  | container style                                                    | `""`    |
| `svg-style`      | `string`  | inner svg tag style                                                | `""`    |
| `src` _required_ | `string`  | resource url, could be remote or local                             |         |
| `width`          | `string`  | fit svg tag `width` attribute, lower priority than `style.width`   |         |
| `height`         | `string`  | fit svg tag `height` attribute, lower priority than `style.height` |         |
| `no-sanitize`    | `boolean` | determine should skip sanitize                                     | &nbsp;  |

---

# svg

builtin svg component, will render raw svg tag

**Example**

js

```js
Page({
  data: {
    localImage: "pages/tabbar/component/resources/pic/1.jpg",
    remoteImage: "https://static.devfdg.net/image/julia/pie-chart-currentcolor.svg",
    colorChanged: false,
    svgStyle: "",
    colorClassChanged: false,
    colorClass: "",
    boxattrsChanged: false,
    boxattrs: { width: "48px", height: "48px" },
  },
  onChangeColor(e) {
    console.log(`[Svg] onChangeColor `, e);
    if (!this.data.colorChanged) {
      this.setData({ colorChanged: true, svgStyle: "color: #d22f2f;" });
    } else {
      this.setData({ colorChanged: false, svgStyle: "" });
    }
  },
  onChangeBoxAttr() {
    if (!this.data.boxattrsChanged) {
      this.setData({
        boxattrsChanged: true,
        boxattrs: { width: "96px", height: "96px" },
      });
    } else {
      this.setData({
        boxattrsChanged: false,
        boxattrs: { width: "48px", height: "48px" },
      });
    }
  },
});
```

bxml

```html
<view class="section-title">color change</view>
<view class="userinfo">
  <button bindtap="onChangeColor">Change Color</button>
</view>
<view class="image-container">
  <svg src="{{localImage}}" style="{{svgStyle}}"></svg>
</view>

<view class="section-title">box attributes</view>
<button bindtap="onChangeBoxAttr">Change Box Attributes</button>
<view class="image-container">
  <svg src="{{localImage}}" style="{{svgStyle}}" width="{{boxattrs.width}}" height="{{boxattrs.height}}"></svg>
</view>
<view>boxattrs: {{ boxattrs }}</view>

<view class="section-title">box attributes priority</view>
<view>set width & height at attribute with 48px</view>
<view>set width & height at style with 96px</view>
<view>svg will be 96px;</view>
<view class="image-container">
  <svg src="{{localImage}}" style="width: 96px; height: 96px;" width="48px" height="48px"></svg>
</view>
<view>set width & height at attribute with 96px</view>
<view>svg will be 96px;</view>
<view class="image-container">
  <svg src="{{localImage}}" width="96px" height="96px"></svg>
</view>

<view class="section-title">data url demo</view>
<view class="image-container">
  <svg src="{{dataUrlDemo}}"></svg>
</view>
```

### Bug & Tip

- `tip`: for keep same code between webview and flutter, recommand not use class to custom svg style
- `tip`: not support fully svg feature (document not ready)
- `tip`: could use data-url format and pass by `src`. supported schema `text/html`, `image/svg+xml`
  (don't forget encode url content)
- `tip`: style `width` and `height` have more priority than attribute `width` and `height`
- `tip`: for `padding` and `margin`, we recommand only use `margin` for better compatibility in
  webview and flutter

:::warn cannot direct receive svg content as child, eg `<svg><path>xxxx</path></svg>`, use `src`
instead :::

- **remark** - required jssdk >= 4.37.6
- **remark** - required bundlerversion >= 3.0.112
- **remark** - if use from uikit, need config RootProvider's `iconConfig` with `svgTag: true`

## Props

| Name             | Type      | Description                                                        | Default |
| ---------------- | --------- | ------------------------------------------------------------------ | ------- |
| `style`          | `string`  | container style                                                    | `""`    |
| `svg-style`      | `string`  | inner svg tag style                                                | `""`    |
| `src` _required_ | `string`  | resource url, could be remote or local                             |         |
| `width`          | `string`  | fit svg tag `width` attribute, lower priority than `style.width`   |         |
| `height`         | `string`  | fit svg tag `height` attribute, lower priority than `style.height` |         |
| `no-sanitize`    | `boolean` | determine should skip sanitize                                     | &nbsp;  |