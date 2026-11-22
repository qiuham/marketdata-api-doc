---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Image
api_type: Guide
updated_at: 2026-11-22 18:40:30.691926
---

# image

Image.

**Example**

js

```js
Page({
  data: {
    imageUrl: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
    lazyImageUrl: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
    localImage: "pages/tabbar/component/resources/pic/1.jpg",
    array: [
      {
        mode: "scaleToFill",
        text: "scaleToFill",
      },
      {
        mode: "aspectFit",
        text: "aspectFit",
      },
      {
        mode: "aspectFill",
        text: "aspectFill",
      },
      {
        mode: "widthFix",
        text: "widthFix",
      },
      {
        mode: "heightFix",
        text: "heightFix",
      },
      {
        mode: "top",
        text: "top",
      },
      {
        mode: "bottom",
        text: "bottom",
      },
      {
        mode: "center",
        text: "center",
      },
      {
        mode: "left",
        text: "left",
      },
      {
        mode: "right",
        text: "right",
      },
      {
        mode: "top left",
        text: "top left",
      },
      {
        mode: "top right",
        text: "top right",
      },
      {
        mode: "bottom left",
        text: "bottom left",
      },
      {
        mode: "bottom right",
        text: "bottom right",
      },
    ],
  },
  onClick(e) {
    console.log(`[Image] onClick`, e);
  },
  onLongPress(e) {
    console.log(`[Image] onLongPress`, e);
  },
  onLoad(e) {
    console.log(`[Image] onLoad`, e);
  },
  onError(e) {
    console.log(`[Image] onError`, e);
  },
});
```

bxml

```html
<view class="page">
  <view class="page__hd">
    <text class="page__title">image</text>
    <text class="page__desc">picture</text>
  </view>
  <view class="page__bd">
    <view class="section section_gap" bn:for-items="{{array}}" bn:for-item="item">
      <view class="section__title">{{item.text}}</view>
      <view class="section__ctn">
        <image style="width: 200px; height: 200px; background-color: #eeeeee;" mode="{{item.mode}}" src="{{src}}"></image>
      </view>
    </view>
  </view>
</view>
```

bxss

```css
.section__ctn {
  text-align: center;
}
```

**Bug & Tip**

- `tip`: Image component default width 320px, height 240px
- `tip`: QR code in image component/Mini Program code image does not support long press recognition.
  Long press recognition is supported only in wx.preview Image

---

# image

Image.

**Example**

js

```js
Page({
  data: {
    imageUrl: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
    lazyImageUrl: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
    localImage: "pages/tabbar/component/resources/pic/1.jpg",
    array: [
      {
        mode: "scaleToFill",
        text: "scaleToFill",
      },
      {
        mode: "aspectFit",
        text: "aspectFit",
      },
      {
        mode: "aspectFill",
        text: "aspectFill",
      },
      {
        mode: "widthFix",
        text: "widthFix",
      },
      {
        mode: "heightFix",
        text: "heightFix",
      },
      {
        mode: "top",
        text: "top",
      },
      {
        mode: "bottom",
        text: "bottom",
      },
      {
        mode: "center",
        text: "center",
      },
      {
        mode: "left",
        text: "left",
      },
      {
        mode: "right",
        text: "right",
      },
      {
        mode: "top left",
        text: "top left",
      },
      {
        mode: "top right",
        text: "top right",
      },
      {
        mode: "bottom left",
        text: "bottom left",
      },
      {
        mode: "bottom right",
        text: "bottom right",
      },
    ],
  },
  onClick(e) {
    console.log(`[Image] onClick`, e);
  },
  onLongPress(e) {
    console.log(`[Image] onLongPress`, e);
  },
  onLoad(e) {
    console.log(`[Image] onLoad`, e);
  },
  onError(e) {
    console.log(`[Image] onError`, e);
  },
});
```

bxml

```html
<view class="page">
  <view class="page__hd">
    <text class="page__title">image</text>
    <text class="page__desc">picture</text>
  </view>
  <view class="page__bd">
    <view class="section section_gap" bn:for-items="{{array}}" bn:for-item="item">
      <view class="section__title">{{item.text}}</view>
      <view class="section__ctn">
        <image style="width: 200px; height: 200px; background-color: #eeeeee;" mode="{{item.mode}}" src="{{src}}"></image>
      </view>
    </view>
  </view>
</view>
```

bxss

```css
.section__ctn {
  text-align: center;
}
```

**Bug & Tip**

- `tip`: Image component default width 320px, height 240px
- `tip`: QR code in image component/Mini Program code image does not support long press recognition.
  Long press recognition is supported only in wx.preview Image