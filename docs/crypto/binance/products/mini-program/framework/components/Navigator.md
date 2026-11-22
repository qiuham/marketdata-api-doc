---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/components/Navigator
api_type: Guide
updated_at: 2026-11-22 18:40:23.552896
---

# navigator

Navigator.

**Example**

index.bxml

```html
<view>
  <navigator url="/navigate/navigate?title=navigate" hover-class="navigator-hover">jump to new page</navigator>
  <navigator url="../redirect/redirect?title=redirect" open-type="redirect" hover-class="other-navigator-hover">open in current page</navigator>
</view>
```

/navigate/navigate.bxml

```html
<view> Click on the upper left corner to return to the previous page </view>
```

/redirect/redirect.bxml

```html
<view> Click on the upper left corner to return to the previous page </view>
```

**Bug & Tip**

- `tip`: `navigator-hover` Default is `{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}`,
  navigator Child node background color should be transparent

## Props

| Name         | Type                  | Description                                                                                                                                                          | Default       |
| ------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `target`     | `Target`              | On which target to jump, default current Mini Program                                                                                                                | `"self"`      |
| `url`        | `string`              | Jump links within the current Mini Program                                                                                                                           |               |
| `app-id`     | `string`              | When target="miniProgram" The Mini Program that you want to open appId                                                                                               |               |
| `path`       | `string`              | When target="miniProgram" Open the page path, if empty then open the home page                                                                                       |               |
| `extra-data` | `object`              | When target="miniProgram" data that needs to be passed to the target Mini Program, which is available in the App.onLaunch()，App.onShow() Get this data from.details |               |
| `version`    | `NavigationMPChannel` | When target="miniProgram" version of the Mini Program to be opened                                                                                                   | `"published"` |
| `type`       | `NavigationMPType`    | defined in Nezha deeplink                                                                                                                                            | `"app"`       |
| `rev`        | `string`              |                                                                                                                                                                      | &nbsp;        |

## Events

| Name           | Description |
| -------------- | ----------- |
| `bindsuccess`  |             |
| `bindfail`     |             |
| `bindcomplete` |             |
| `bindtap`      | &nbsp;      |

---

# navigator

Navigator.

**Example**

index.bxml

```html
<view>
  <navigator url="/navigate/navigate?title=navigate" hover-class="navigator-hover">jump to new page</navigator>
  <navigator url="../redirect/redirect?title=redirect" open-type="redirect" hover-class="other-navigator-hover">open in current page</navigator>
</view>
```

/navigate/navigate.bxml

```html
<view> Click on the upper left corner to return to the previous page </view>
```

/redirect/redirect.bxml

```html
<view> Click on the upper left corner to return to the previous page </view>
```

**Bug & Tip**

- `tip`: `navigator-hover` Default is `{background-color: rgba(0, 0, 0, 0.1) opacity: 0.7}`,
  navigator Child node background color should be transparent

## Props

| Name         | Type                  | Description                                                                                                                                                          | Default       |
| ------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `target`     | `Target`              | On which target to jump, default current Mini Program                                                                                                                | `"self"`      |
| `url`        | `string`              | Jump links within the current Mini Program                                                                                                                           |               |
| `app-id`     | `string`              | When target="miniProgram" The Mini Program that you want to open appId                                                                                               |               |
| `path`       | `string`              | When target="miniProgram" Open the page path, if empty then open the home page                                                                                       |               |
| `extra-data` | `object`              | When target="miniProgram" data that needs to be passed to the target Mini Program, which is available in the App.onLaunch()，App.onShow() Get this data from.details |               |
| `version`    | `NavigationMPChannel` | When target="miniProgram" version of the Mini Program to be opened                                                                                                   | `"published"` |
| `type`       | `NavigationMPType`    | defined in Nezha deeplink                                                                                                                                            | `"app"`       |
| `rev`        | `string`              |                                                                                                                                                                      | &nbsp;        |

## Events

| Name           | Description |
| -------------- | ----------- |
| `bindsuccess`  |             |
| `bindfail`     |             |
| `bindcomplete` |             |
| `bindtap`      | &nbsp;      |