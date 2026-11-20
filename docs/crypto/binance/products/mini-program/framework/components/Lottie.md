---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Lottie
api_type: Guide
updated_at: 2026-11-20 18:44:04.713398
---

# lottie

Lottie component, used to integrate and display Lottie animations in mini programs. Lottie animation
is an animation library developed by Airbnb, which uses JSON format animation data and can run on
various platforms such as web pages and mobile applications.

**Example**

you can refer to the following example to configure the webpack config file.

- pika.config/webpack.config.js

```js
const CopyPlugin = require("copy-webpack-plugin");
module.exports = (config, { name, mode, webpack, resolveWebpackModule, helpers, type }) => {
  config.plugin("app/webpack-copy-plugin").use(CopyPlugin, [
    {
      patterns: [
        {
          from: "src/assets/your_lottie_file.json",
          // `to` file path is the path of <Lottie> component
          to: "pages/your_page/lottie/your_lottie_file.json",
        },
      ],
    },
  ]);
  return config;
};
```

js

```js
Page({
  data: {
    instance: null,
    renderer: "svg",
    loop: true,
    autoplay: true,
    path: "pages/your_page/lottie/your_lottie_file.json",
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  },
  onReady() {
    this.instance = bn.createLottieContext("lottie");
  },
  play() {
    this.instance.play();
  },
  pause() {
    this.instance.pause();
  },
  stop() {
    this.instance.stop();
  },
  setSpeed() {
    this.instance.setSpeed(0.25);
  },
  setDirection() {
    this.instance.setDirection(-1);
  },
  destroy() {
    this.instance.destroy();
  },
  play2() {
    this.instance2.play();
  },
  stop2() {
    this.instance2.stop();
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <head title="lottie"></head>
    <view class="page-body">
      <lottie lottie-id="lottie" bindcomplete="onComplete" bindloopcomplete="onLoopComplete" renderer="{{renderer}}" loop="{{loop}}" path="{{path}}" autoplay="{{autoplay}}" renderer-settings="{{rendererSettings}}" class="lottie"></lottie>
      <button class="play" bindtap="play">play</button>
      <button class="stop" bindtap="stop">stop</button>
      <button class="pause" bindtap="pause">pause</button>
      <button class="setSpeed" bindtap="setSpeed">setSpeed</button>
      <button class="setDirection" bindtap="setDirection">setDirection - reverse</button>
      <button class="destroy" bindtap="destroy">destroy</button>
    </view>
  </view>
</theme-context>
```

bxss

```css
.lottie {
  width: 300px;
  height: 200px;
}
```

### Events

- sdk ≥ `4.38.0`

| Event            | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `onComplete`     | trigger on Lottie animation completed without `loop: false`. |
| `onLoopComplete` | trigger on Lottie animation completed with `loop: true`.     |
| `onSegmentStart` | trigger on Lottie animation start a segment.                 |
| `onConfigReady`  | trigger on Lottie animation config ready.                    |
| `onDataReady`    | trigger on Lottie animation data ready.                      |
| `onDataFailed`   | trigger on Lottie animation data failed.                     |
| `onLoadedImages` | trigger on Lottie animation loaded images.                   |
| `onDOMLoaded`    | trigger on Lottie animation DOM loaded.                      |
| `onDestroy`      | trigger on Lottie animation destruction.                     |

- **remark** - sdk ≥ 4.38.0 pika ≥ 0.3.57 @binance/bmp-api ≥ 1.0.153

## Props

| Name                   | Type                                          | Description | Default |
| ---------------------- | --------------------------------------------- | ----------- | ------- |
| `lottie-id` _required_ | `string`                                      |             |         |
| `renderer`             | `RendererType`                                |             | `"svg"` |
| `loop`                 | `boolean`                                     |             | `true`  |
| `autoplay`             | `boolean`                                     |             | `true`  |
| `path` _required_      | `string`                                      |             |         |
| `renderer-settings`    | `AnimationConfigWithData['rendererSettings']` |             |         |
| `initial-segment`      | `AnimationSegment`                            |             | &nbsp;  |

## Events

| Name               | Description                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindcomplete`     | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'complete', _detail: e, }: object`**</li></ul>                                     |
| `bindloopcomplete` | <br/>**Arguments**<br/><ul><li>**`{ _type: 'loopcomplete', _currentTarget: this.$el, _detail: e, }: object`**</li></ul>                                 |
| `bindsegmentstart` | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'segmentstart', _detail: { animationName: this.lottieId, }, }: object`**</li></ul> |
| `bindconfigready`  | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'configready', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>  |
| `binddataready`    | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'dataready', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>    |
| `binddatafailed`   | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'datafailed', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>   |
| `bindloadedimages` | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'loadedimages', _detail: { animationName: this.lottieId, }, }: object`**</li></ul> |
| `binddomloaded`    | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'DOMLoaded', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>    |
| `binddestroy`      | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'destroy', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>      |

---

# lottie

Lottie component, used to integrate and display Lottie animations in mini programs. Lottie animation
is an animation library developed by Airbnb, which uses JSON format animation data and can run on
various platforms such as web pages and mobile applications.

**Example**

you can refer to the following example to configure the webpack config file.

- pika.config/webpack.config.js

```js
const CopyPlugin = require("copy-webpack-plugin");
module.exports = (config, { name, mode, webpack, resolveWebpackModule, helpers, type }) => {
  config.plugin("app/webpack-copy-plugin").use(CopyPlugin, [
    {
      patterns: [
        {
          from: "src/assets/your_lottie_file.json",
          // `to` file path is the path of <Lottie> component
          to: "pages/your_page/lottie/your_lottie_file.json",
        },
      ],
    },
  ]);
  return config;
};
```

js

```js
Page({
  data: {
    instance: null,
    renderer: "svg",
    loop: true,
    autoplay: true,
    path: "pages/your_page/lottie/your_lottie_file.json",
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  },
  onReady() {
    this.instance = bn.createLottieContext("lottie");
  },
  play() {
    this.instance.play();
  },
  pause() {
    this.instance.pause();
  },
  stop() {
    this.instance.stop();
  },
  setSpeed() {
    this.instance.setSpeed(0.25);
  },
  setDirection() {
    this.instance.setDirection(-1);
  },
  destroy() {
    this.instance.destroy();
  },
  play2() {
    this.instance2.play();
  },
  stop2() {
    this.instance2.stop();
  },
});
```

bxml

```html
<theme-context>
  <view class="container">
    <head title="lottie"></head>
    <view class="page-body">
      <lottie lottie-id="lottie" bindcomplete="onComplete" bindloopcomplete="onLoopComplete" renderer="{{renderer}}" loop="{{loop}}" path="{{path}}" autoplay="{{autoplay}}" renderer-settings="{{rendererSettings}}" class="lottie"></lottie>
      <button class="play" bindtap="play">play</button>
      <button class="stop" bindtap="stop">stop</button>
      <button class="pause" bindtap="pause">pause</button>
      <button class="setSpeed" bindtap="setSpeed">setSpeed</button>
      <button class="setDirection" bindtap="setDirection">setDirection - reverse</button>
      <button class="destroy" bindtap="destroy">destroy</button>
    </view>
  </view>
</theme-context>
```

bxss

```css
.lottie {
  width: 300px;
  height: 200px;
}
```

### Events

- sdk ≥ `4.38.0`

| Event            | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `onComplete`     | trigger on Lottie animation completed without `loop: false`. |
| `onLoopComplete` | trigger on Lottie animation completed with `loop: true`.     |
| `onSegmentStart` | trigger on Lottie animation start a segment.                 |
| `onConfigReady`  | trigger on Lottie animation config ready.                    |
| `onDataReady`    | trigger on Lottie animation data ready.                      |
| `onDataFailed`   | trigger on Lottie animation data failed.                     |
| `onLoadedImages` | trigger on Lottie animation loaded images.                   |
| `onDOMLoaded`    | trigger on Lottie animation DOM loaded.                      |
| `onDestroy`      | trigger on Lottie animation destruction.                     |

- **remark** - sdk ≥ 4.38.0 pika ≥ 0.3.57 @binance/bmp-api ≥ 1.0.153

## Props

| Name                   | Type                                          | Description | Default |
| ---------------------- | --------------------------------------------- | ----------- | ------- |
| `lottie-id` _required_ | `string`                                      |             |         |
| `renderer`             | `RendererType`                                |             | `"svg"` |
| `loop`                 | `boolean`                                     |             | `true`  |
| `autoplay`             | `boolean`                                     |             | `true`  |
| `path` _required_      | `string`                                      |             |         |
| `renderer-settings`    | `AnimationConfigWithData['rendererSettings']` |             |         |
| `initial-segment`      | `AnimationSegment`                            |             | &nbsp;  |

## Events

| Name               | Description                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindcomplete`     | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'complete', _detail: e, }: object`**</li></ul>                                     |
| `bindloopcomplete` | <br/>**Arguments**<br/><ul><li>**`{ _type: 'loopcomplete', _currentTarget: this.$el, _detail: e, }: object`**</li></ul>                                 |
| `bindsegmentstart` | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'segmentstart', _detail: { animationName: this.lottieId, }, }: object`**</li></ul> |
| `bindconfigready`  | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'configready', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>  |
| `binddataready`    | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'dataready', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>    |
| `binddatafailed`   | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'datafailed', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>   |
| `bindloadedimages` | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'loadedimages', _detail: { animationName: this.lottieId, }, }: object`**</li></ul> |
| `binddomloaded`    | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'DOMLoaded', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>    |
| `binddestroy`      | <br/>**Arguments**<br/><ul><li>**`{ _currentTarget: this.$el, _type: 'destroy', _detail: { animationName: this.lottieId, }, }: object`**</li></ul>      |