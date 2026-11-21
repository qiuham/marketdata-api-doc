---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/extended
api_type: Guide
updated_at: 2026-11-21 18:38:02.420427
---

# Extended

## Navigators

### Navigation

Navigation is the navigator component on top of the Mini Program. Using `navigationStyle: custom`,
you can replace the default navigation with a custom component.

```json
// page.json
{
  "navigationStyle": "custom"
}
```

With this configuration, the default navigation bar on the current page will be removed. You will
need to implement a component on your own page to replace it.

#### Custom Navigation Bar Example

```json
//custom-navigation-bar.json
{
  "navigationStyle": "custom"
}
```

```html
<!-- custom-navigation-bar.bxml -->
<view class="cnb-container">
  <view class="custom-nav-bar">
    <view class="custom-nav-bar-title">{title}</view>
  </view>
</view>
```

```javascript
Page({
  data: {
    title: "Hello world",
  },
});
```

```scss
//  custom-navigation-bar.bxss
.cnb-container {
  position: relative;
  padding: 0 10px;
  height: var(--mp-navigator-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #000000;
  color: white;
}
.custom-nav-bar {
  position: absolute;
  left: 95px;
  right: 95px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  display: flex;
  align-items: center;
  box-sizing: border-box;
}
```

### Tabbar

- Bxml

Configure `tabBar.custom: true` in `app.json`

```ts
"tabBar": {
  "custom": true
}
```

Add `custom-tab-bar` in root directory

```bash
custom-tab-bar
├── index.bxml
├── index.bxss
├── index.js
└── index.json
```

You will need to implement a `custom tab bar` yourself

### Disable Bounces

Set `disableBounces: true` in your `{page}.json`.

This prevents the page from sliding out of the screen area (only IOS)

```js
export default {
  disableBounces: true,
};
```

---

# Extended

## Navigators

### Navigation

Navigation is the navigator component on top of the Mini Program. Using `navigationStyle: custom`,
you can replace the default navigation with a custom component.

```json
// page.json
{
  "navigationStyle": "custom"
}
```

With this configuration, the default navigation bar on the current page will be removed. You will
need to implement a component on your own page to replace it.

#### Custom Navigation Bar Example

```json
//custom-navigation-bar.json
{
  "navigationStyle": "custom"
}
```

```html
<!-- custom-navigation-bar.bxml -->
<view class="cnb-container">
  <view class="custom-nav-bar">
    <view class="custom-nav-bar-title">{title}</view>
  </view>
</view>
```

```javascript
Page({
  data: {
    title: "Hello world",
  },
});
```

```scss
//  custom-navigation-bar.bxss
.cnb-container {
  position: relative;
  padding: 0 10px;
  height: var(--mp-navigator-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #000000;
  color: white;
}
.custom-nav-bar {
  position: absolute;
  left: 95px;
  right: 95px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  display: flex;
  align-items: center;
  box-sizing: border-box;
}
```

### Tabbar

- Bxml

Configure `tabBar.custom: true` in `app.json`

```ts
"tabBar": {
  "custom": true
}
```

Add `custom-tab-bar` in root directory

```bash
custom-tab-bar
├── index.bxml
├── index.bxss
├── index.js
└── index.json
```

You will need to implement a `custom tab bar` yourself

### Disable Bounces

Set `disableBounces: true` in your `{page}.json`.

This prevents the page from sliding out of the screen area (only IOS)

```js
export default {
  disableBounces: true,
};
```