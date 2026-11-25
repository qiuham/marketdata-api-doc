---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/FlutterVideo
api_type: Guide
updated_at: 2026-11-25 18:43:08.921002
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

| Name                               | Type            | Description                                                                                                                                                                                                                                  | Default     |
| ---------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `id`                               | `string`        |                                                                                                                                                                                                                                              |             |
| `src` _required_                   | `string`        | Resource address to play video, support network path, local temporary path                                                                                                                                                                   |             |
| `duration`                         | `number`        |                                                                                                                                                                                                                                              |             |
| `controls`                         | `boolean`       | Whether to display the default playback controls/Pause on, playback progress, time)                                                                                                                                                          | `true`      |
| `autoplay`                         | `boolean`       | Whether to autoplay                                                                                                                                                                                                                          | `false`     |
| `loop`                             | `boolean`       | Whether to play on a loop                                                                                                                                                                                                                    | `false`     |
| `muted`                            | `boolean`       | Mute Play                                                                                                                                                                                                                                    | `false`     |
| `danmu-list`                       | `array`         | Unsupported properties, comment out default values to avoid Dart initialization errors.                                                                                                                                                      |             |
| `danmu-btn`                        | `boolean`       |                                                                                                                                                                                                                                              |             |
| `enable-danmu`                     | `boolean`       |                                                                                                                                                                                                                                              |             |
| `init-time`                        | `number`        |                                                                                                                                                                                                                                              |             |
| `page-gesture`                     | `boolean`       |                                                                                                                                                                                                                                              |             |
| `direction`                        | `DirectionType` |                                                                                                                                                                                                                                              |             |
| `show-progress`                    | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-fullscreen-btn`              | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-play-btn`                    | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-center-play-btn`             | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `enable-progress-gesture`          | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `object-fit`                       | `string`        | When the video size is the same as the video When the container size is inconsistent, the presentation of the video                                                                                                                          | `"contain"` |
| `poster`                           | `string`        |                                                                                                                                                                                                                                              |             |
| `show-mute-btn`                    | `boolean`       |                                                                                                                                                                                                                                              |             |
| `title`                            | `string`        |                                                                                                                                                                                                                                              |             |
| `play-btn-position`                | `string`        |                                                                                                                                                                                                                                              |             |
| `enable-play-gesture`              | `boolean`       |                                                                                                                                                                                                                                              |             |
| `auto-pause-if-navigate`           | `boolean`       | When jumping to other pages of this applet, whether to automatically suspend video playback on this page                                                                                                                                     |             |
| `auto-pause-if-open-native`        | `boolean`       | When jumping to other WeChat native pages, whether to automatically suspend the video on this page                                                                                                                                           |             |
| `vslide-gesture`                   | `boolean`       | Under non-full-screen mode, whether to turn on the brightness and volume adjustment gesture                                                                                                                                                  |             |
| `vslide-gesture-in-fullscreen`     | `boolean`       | In full -screen mode, whether to turn on the brightness and volume adjustment gesture                                                                                                                                                        |             |
| `show-bottom-progress`             | `boolean`       | Whether to show the bottom progress bar                                                                                                                                                                                                      | `true`      |
| `show-casting-button`              | `boolean`       | Display screen button. Android takes effect under the same layer to support the DLNA protocol; iOS supports AirPlay and DLNA protocols. It can be operated through the correlation method of VideoContext.                                   | `false`     |
| `picture-in-picture-mode`          | `array`         | Set the small window mode: Push, POP, empty string, or set multiple modes in the form of an array (such as: [push "," pop "])                                                                                                                | `[]`        |
| `picture-in-picture-init-position` | `string`        | The initial display position of the small window in the small window mode is the format (alignment, y), where Alignment indicates that the left side of the small window adsorption screen is still the right side or right side. percentage |             |
| `enable-auto-rotation`             | `boolean`       | Whether to open the full screen when the mobile phone is turned on, and take effect when the system is set to turn on the automatic rotation                                                                                                 |             |
| `show-screen-lock-button`          | `boolean`       | Whether the lock screen button is displayed, only displayed in full screen, the operation of the control bar after the lock screen                                                                                                           |             |
| `show-snapshot-button`             | `boolean`       | Whether to display a screenshot button, only display when it is full screen                                                                                                                                                                  |             |
| `show-background-playback-button`  | `boolean`       | Whether to show the background audio play button                                                                                                                                                                                             |             |
| `background-poster`                | `string`        | The notification bar icon after entering the background audio playback (Android is unique)                                                                                                                                                   | &nbsp;      |

## Events

| Name                        | Description                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindplay`                  | When it starts/Triggers play event while continuing playback                                                                                |
| `bindpause`                 | Triggered when playback is paused pause event                                                                                               |
| `bindended`                 | Triggered when playback is paused pause event                                                                                               |
| `bindtimeupdate`            | Triggered when playback progress changes, event. detail = {currentTime, duration} Trigger frequency. 250ms first                            |
| `bindfullscreenchange`      | Triggered when video enters and exits full-screen, event.detail = {fullScreen, direction},direction Valid values are vertical or horizontal |
| `binderror`                 | Triggered when video playback goes wrong                                                                                                    |
| `bindwaiting`               |                                                                                                                                             |
| `bindprogress`              |                                                                                                                                             |
| `bindloadedmetadata`        |                                                                                                                                             |
| `bindcontrolstoggle`        |                                                                                                                                             |
| `bindenterpictureinpicture` |                                                                                                                                             |
| `bindleavepictureinpicture` |                                                                                                                                             |
| `bindseekcomplete`          |                                                                                                                                             |
| `bindcastinguserselect`     |                                                                                                                                             |
| `bindcastingstatechange`    |                                                                                                                                             |
| `bindcastinginterrupt`      | Triggered when the screen is interrupted                                                                                                    |

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

| Name                               | Type            | Description                                                                                                                                                                                                                                  | Default     |
| ---------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `id`                               | `string`        |                                                                                                                                                                                                                                              |             |
| `src` _required_                   | `string`        | Resource address to play video, support network path, local temporary path                                                                                                                                                                   |             |
| `duration`                         | `number`        |                                                                                                                                                                                                                                              |             |
| `controls`                         | `boolean`       | Whether to display the default playback controls/Pause on, playback progress, time)                                                                                                                                                          | `true`      |
| `autoplay`                         | `boolean`       | Whether to autoplay                                                                                                                                                                                                                          | `false`     |
| `loop`                             | `boolean`       | Whether to play on a loop                                                                                                                                                                                                                    | `false`     |
| `muted`                            | `boolean`       | Mute Play                                                                                                                                                                                                                                    | `false`     |
| `danmu-list`                       | `array`         | Unsupported properties, comment out default values to avoid Dart initialization errors.                                                                                                                                                      |             |
| `danmu-btn`                        | `boolean`       |                                                                                                                                                                                                                                              |             |
| `enable-danmu`                     | `boolean`       |                                                                                                                                                                                                                                              |             |
| `init-time`                        | `number`        |                                                                                                                                                                                                                                              |             |
| `page-gesture`                     | `boolean`       |                                                                                                                                                                                                                                              |             |
| `direction`                        | `DirectionType` |                                                                                                                                                                                                                                              |             |
| `show-progress`                    | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-fullscreen-btn`              | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-play-btn`                    | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `show-center-play-btn`             | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `enable-progress-gesture`          | `boolean`       |                                                                                                                                                                                                                                              | `true`      |
| `object-fit`                       | `string`        | When the video size is the same as the video When the container size is inconsistent, the presentation of the video                                                                                                                          | `"contain"` |
| `poster`                           | `string`        |                                                                                                                                                                                                                                              |             |
| `show-mute-btn`                    | `boolean`       |                                                                                                                                                                                                                                              |             |
| `title`                            | `string`        |                                                                                                                                                                                                                                              |             |
| `play-btn-position`                | `string`        |                                                                                                                                                                                                                                              |             |
| `enable-play-gesture`              | `boolean`       |                                                                                                                                                                                                                                              |             |
| `auto-pause-if-navigate`           | `boolean`       | When jumping to other pages of this applet, whether to automatically suspend video playback on this page                                                                                                                                     |             |
| `auto-pause-if-open-native`        | `boolean`       | When jumping to other WeChat native pages, whether to automatically suspend the video on this page                                                                                                                                           |             |
| `vslide-gesture`                   | `boolean`       | Under non-full-screen mode, whether to turn on the brightness and volume adjustment gesture                                                                                                                                                  |             |
| `vslide-gesture-in-fullscreen`     | `boolean`       | In full -screen mode, whether to turn on the brightness and volume adjustment gesture                                                                                                                                                        |             |
| `show-bottom-progress`             | `boolean`       | Whether to show the bottom progress bar                                                                                                                                                                                                      | `true`      |
| `show-casting-button`              | `boolean`       | Display screen button. Android takes effect under the same layer to support the DLNA protocol; iOS supports AirPlay and DLNA protocols. It can be operated through the correlation method of VideoContext.                                   | `false`     |
| `picture-in-picture-mode`          | `array`         | Set the small window mode: Push, POP, empty string, or set multiple modes in the form of an array (such as: [push "," pop "])                                                                                                                | `[]`        |
| `picture-in-picture-init-position` | `string`        | The initial display position of the small window in the small window mode is the format (alignment, y), where Alignment indicates that the left side of the small window adsorption screen is still the right side or right side. percentage |             |
| `enable-auto-rotation`             | `boolean`       | Whether to open the full screen when the mobile phone is turned on, and take effect when the system is set to turn on the automatic rotation                                                                                                 |             |
| `show-screen-lock-button`          | `boolean`       | Whether the lock screen button is displayed, only displayed in full screen, the operation of the control bar after the lock screen                                                                                                           |             |
| `show-snapshot-button`             | `boolean`       | Whether to display a screenshot button, only display when it is full screen                                                                                                                                                                  |             |
| `show-background-playback-button`  | `boolean`       | Whether to show the background audio play button                                                                                                                                                                                             |             |
| `background-poster`                | `string`        | The notification bar icon after entering the background audio playback (Android is unique)                                                                                                                                                   | &nbsp;      |

## Events

| Name                        | Description                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `bindplay`                  | When it starts/Triggers play event while continuing playback                                                                                |
| `bindpause`                 | Triggered when playback is paused pause event                                                                                               |
| `bindended`                 | Triggered when playback is paused pause event                                                                                               |
| `bindtimeupdate`            | Triggered when playback progress changes, event. detail = {currentTime, duration} Trigger frequency. 250ms first                            |
| `bindfullscreenchange`      | Triggered when video enters and exits full-screen, event.detail = {fullScreen, direction},direction Valid values are vertical or horizontal |
| `binderror`                 | Triggered when video playback goes wrong                                                                                                    |
| `bindwaiting`               |                                                                                                                                             |
| `bindprogress`              |                                                                                                                                             |
| `bindloadedmetadata`        |                                                                                                                                             |
| `bindcontrolstoggle`        |                                                                                                                                             |
| `bindenterpictureinpicture` |                                                                                                                                             |
| `bindleavepictureinpicture` |                                                                                                                                             |
| `bindseekcomplete`          |                                                                                                                                             |
| `bindcastinguserselect`     |                                                                                                                                             |
| `bindcastingstatechange`    |                                                                                                                                             |
| `bindcastinginterrupt`      | Triggered when the screen is interrupted                                                                                                    |