---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Video
api_type: Guide
updated_at: 2026-11-20 18:43:29.980451
---

# Video

Video support Same-layer rendering. Related api: bn.createVideoContext

**Example**

```js
Page({
  data: {
    id: "myVideo",
  },
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {
    console.log(`[LifeCycle][Textarea] useEffect`);
    setTimeout(() => {
      if (!this.videoContext) throw new Error("Missing VideoContext");
      this.videoContext.play();
    }, 500);
  },
  onReady() {
    this.videoContext = bn.createVideoContext("myVideo");
  },

  onPlay(e) {
    console.log("[video] onPlay", e);
  },
  onPause(e) {
    console.log("[video] onPause", e);
  },
  onEnded(e) {
    console.log("[video] onEnded", e);
  },
  onTimeupdate(e) {
    console.log("[video] onTimeupdate", e);
  },
  onFullscreenchange(e) {
    console.log("[video] onFullscreenchange", e);
  },
  onLoadedmetadata(e) {
    console.log("[video] onLoadedmetadata", e);
  },
  onError(e) {
    console.log("[video] onError", e);
  },
});
```

**Bug & Tip**

- tip：video Default width 300px, altitude 225px, available via bxss Set the width and height.

## Props

| Name             | Type      | Description                                                                         | Default |
| ---------------- | --------- | ----------------------------------------------------------------------------------- | ------- |
| `id`             | `string`  |                                                                                     |         |
| `src` _required_ | `string`  | Resource address to play video, support network path, local temporary path          |         |
| `playsinline`    | `boolean` | Whether to play inline                                                              | `false` |
| `controls`       | `boolean` | Whether to display the default playback controls/Pause on, playback progress, time) | `true`  |
| `autoplay`       | `boolean` | Whether to autoplay                                                                 | `false` |
| `loop`           | `boolean` | Whether to play on a loop                                                           | `false` |
| `muted`          | `boolean` | Mute Play                                                                           | `false` |
| `poster`         | `string`  | The image displayed before playing the video                                        | `""`    |

## Events

| Name                   | Description                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindplay`             | When it starts/Triggers play event while continuing playback                                                                                |
| `bindpause`            | Triggered when playback is paused pause event                                                                                               |
| `bindended`            | Triggered when playback is paused pause event                                                                                               |
| `bindtimeupdate`       | Triggered when playback progress changes, event. detail = {currentTime, duration} Trigger frequency. 250ms first                            |
| `bindfullscreenchange` | Triggered when video enters and exits full-screen, event.detail = {fullScreen, direction},direction Valid values are vertical or horizontal |
| `binderror`            | Triggered when video playback goes wrong                                                                                                    |

---

# Video

Video support Same-layer rendering. Related api: bn.createVideoContext

**Example**

```js
Page({
  data: {
    id: "myVideo",
  },
  onLoad(query) {
    console.log("onload", this, query);
  },
  onShow() {
    console.log(`[LifeCycle][Textarea] useEffect`);
    setTimeout(() => {
      if (!this.videoContext) throw new Error("Missing VideoContext");
      this.videoContext.play();
    }, 500);
  },
  onReady() {
    this.videoContext = bn.createVideoContext("myVideo");
  },

  onPlay(e) {
    console.log("[video] onPlay", e);
  },
  onPause(e) {
    console.log("[video] onPause", e);
  },
  onEnded(e) {
    console.log("[video] onEnded", e);
  },
  onTimeupdate(e) {
    console.log("[video] onTimeupdate", e);
  },
  onFullscreenchange(e) {
    console.log("[video] onFullscreenchange", e);
  },
  onLoadedmetadata(e) {
    console.log("[video] onLoadedmetadata", e);
  },
  onError(e) {
    console.log("[video] onError", e);
  },
});
```

**Bug & Tip**

- tip：video Default width 300px, altitude 225px, available via bxss Set the width and height.

## Props

| Name             | Type      | Description                                                                         | Default |
| ---------------- | --------- | ----------------------------------------------------------------------------------- | ------- |
| `id`             | `string`  |                                                                                     |         |
| `src` _required_ | `string`  | Resource address to play video, support network path, local temporary path          |         |
| `playsinline`    | `boolean` | Whether to play inline                                                              | `false` |
| `controls`       | `boolean` | Whether to display the default playback controls/Pause on, playback progress, time) | `true`  |
| `autoplay`       | `boolean` | Whether to autoplay                                                                 | `false` |
| `loop`           | `boolean` | Whether to play on a loop                                                           | `false` |
| `muted`          | `boolean` | Mute Play                                                                           | `false` |
| `poster`         | `string`  | The image displayed before playing the video                                        | `""`    |

## Events

| Name                   | Description                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindplay`             | When it starts/Triggers play event while continuing playback                                                                                |
| `bindpause`            | Triggered when playback is paused pause event                                                                                               |
| `bindended`            | Triggered when playback is paused pause event                                                                                               |
| `bindtimeupdate`       | Triggered when playback progress changes, event. detail = {currentTime, duration} Trigger frequency. 250ms first                            |
| `bindfullscreenchange` | Triggered when video enters and exits full-screen, event.detail = {fullScreen, direction},direction Valid values are vertical or horizontal |
| `binderror`            | Triggered when video playback goes wrong                                                                                                    |