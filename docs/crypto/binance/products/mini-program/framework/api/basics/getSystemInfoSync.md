---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getSystemInfoSync
api_type: Guide
updated_at: 2026-11-23 18:48:45.566033
---

# bn.getSystemInfoSync

▸ **getSystemInfoSync**(): `SystemInfo`

**`description`** The api to get app info synchronously

**`example`**

```ts
try {
  const res = bn.getSystemInfoSync();
  console.log(res);
} catch (error) {
  // From the something when catch error
}
```

Returns

`SystemInfo`

SystemInfo

---

## SystemInfo

Ƭ **SystemInfo**: `Object`

Type declaration

| Name                | Type                                                                                                                     | Description                                                                                                                                                                                    |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `brand`             | `string`                                                                                                                 | Equipment brand                                                                                                                                                                                |
| `model`             | `string`                                                                                                                 | Device model. New models will show unknown for a while, BN will adapt as soon as possible.                                                                                                     |
| `devicePixelRatio`  | `number`                                                                                                                 | Device pixel ratio                                                                                                                                                                             |
| `pixelRatio`        | `number`                                                                                                                 | Screen width, in px                                                                                                                                                                            |
| `screenWidth`       | `number`                                                                                                                 | Screen width, in px                                                                                                                                                                            |
| `screenHeight`      | `number`                                                                                                                 | Screen height, in px                                                                                                                                                                           |
| `windowWidth`       | `number`                                                                                                                 | Available window width, unit px                                                                                                                                                                |
| `windowHeight`      | `number`                                                                                                                 | Available window height, in px                                                                                                                                                                 |
| `statusBarHeight`   | `number`                                                                                                                 | Height of status bar in px                                                                                                                                                                     |
| `language`          | `string`                                                                                                                 | Language of BN settings                                                                                                                                                                        |
| `version`           | `string`                                                                                                                 | BN version number                                                                                                                                                                              |
| `SDKVersion`        | `string`                                                                                                                 | The SDK version of current MP/MG                                                                                                                                                               |
| `system`            | `string`                                                                                                                 | Operating System and Version                                                                                                                                                                   |
| `platform`          | `string`                                                                                                                 | Client platform                                                                                                                                                                                |
| `deviceOrientation` | `"portrait"` \| `"landscape"`                                                                                            | Device orientation, support portrait or landscape                                                                                                                                              |
| `safeArea`          | { `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` ; `width`: `number` ; `height`: `number` } | A safe area in the positive direction of the vertical screen                                                                                                                                   |
| `safeArea.left`     | `number`                                                                                                                 | Upper left abscissa of security area                                                                                                                                                           |
| `safeArea.right`    | `number`                                                                                                                 | Security area lower right abscissa                                                                                                                                                             |
| `safeArea.top`      | `number`                                                                                                                 | Top-left ordinate of security area                                                                                                                                                             |
| `safeArea.bottom`   | `number`                                                                                                                 | Lower right ordinate of security area                                                                                                                                                          |
| `safeArea.width`    | `number`                                                                                                                 | Width of security area, unit logical pixels                                                                                                                                                    |
| `safeArea.height`   | `number`                                                                                                                 | Height of Safe Area, Unit Logical Pixels                                                                                                                                                       |
| `theme?`            | `Theme`                                                                                                                  | The current theme of the system, the value is `light` or `dark`, it can be obtained only when `"darkmode":true` is configured globally, otherwise it is undefined (does not support mini-game) |
| `host`              | `HostInfo`                                                                                                               | Host environment for current Mini Programs                                                                                                                                                     |

---

## Theme

Ƭ **Theme**: `"light"` \| `"dark"`

## HostInfo

Ƭ **HostInfo**: `Object`

Type declaration

| Name             | Type     | Description        |
| :--------------- | :------- | :----------------- |
| `appId`          | `string` | host appid         |
| `hostAppId`      | `string` | host app id        |
| `hostAppName`    | `string` | host app name      |
| `hostAppVersion` | `string` | host app version   |
| `mpVersion`      | `string` | mp version         |
| `routeUrl`       | `string` | host app route url |

---

# bn.getSystemInfoSync

▸ **getSystemInfoSync**(): `SystemInfo`

**`description`** The api to get app info synchronously

**`example`**

```ts
try {
  const res = bn.getSystemInfoSync();
  console.log(res);
} catch (error) {
  // From the something when catch error
}
```

Returns

`SystemInfo`

SystemInfo

---

## SystemInfo

Ƭ **SystemInfo**: `Object`

Type declaration

| Name                | Type                                                                                                                     | Description                                                                                                                                                                                    |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `brand`             | `string`                                                                                                                 | Equipment brand                                                                                                                                                                                |
| `model`             | `string`                                                                                                                 | Device model. New models will show unknown for a while, BN will adapt as soon as possible.                                                                                                     |
| `devicePixelRatio`  | `number`                                                                                                                 | Device pixel ratio                                                                                                                                                                             |
| `pixelRatio`        | `number`                                                                                                                 | Screen width, in px                                                                                                                                                                            |
| `screenWidth`       | `number`                                                                                                                 | Screen width, in px                                                                                                                                                                            |
| `screenHeight`      | `number`                                                                                                                 | Screen height, in px                                                                                                                                                                           |
| `windowWidth`       | `number`                                                                                                                 | Available window width, unit px                                                                                                                                                                |
| `windowHeight`      | `number`                                                                                                                 | Available window height, in px                                                                                                                                                                 |
| `statusBarHeight`   | `number`                                                                                                                 | Height of status bar in px                                                                                                                                                                     |
| `language`          | `string`                                                                                                                 | Language of BN settings                                                                                                                                                                        |
| `version`           | `string`                                                                                                                 | BN version number                                                                                                                                                                              |
| `SDKVersion`        | `string`                                                                                                                 | The SDK version of current MP/MG                                                                                                                                                               |
| `system`            | `string`                                                                                                                 | Operating System and Version                                                                                                                                                                   |
| `platform`          | `string`                                                                                                                 | Client platform                                                                                                                                                                                |
| `deviceOrientation` | `"portrait"` \| `"landscape"`                                                                                            | Device orientation, support portrait or landscape                                                                                                                                              |
| `safeArea`          | { `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` ; `width`: `number` ; `height`: `number` } | A safe area in the positive direction of the vertical screen                                                                                                                                   |
| `safeArea.left`     | `number`                                                                                                                 | Upper left abscissa of security area                                                                                                                                                           |
| `safeArea.right`    | `number`                                                                                                                 | Security area lower right abscissa                                                                                                                                                             |
| `safeArea.top`      | `number`                                                                                                                 | Top-left ordinate of security area                                                                                                                                                             |
| `safeArea.bottom`   | `number`                                                                                                                 | Lower right ordinate of security area                                                                                                                                                          |
| `safeArea.width`    | `number`                                                                                                                 | Width of security area, unit logical pixels                                                                                                                                                    |
| `safeArea.height`   | `number`                                                                                                                 | Height of Safe Area, Unit Logical Pixels                                                                                                                                                       |
| `theme?`            | `Theme`                                                                                                                  | The current theme of the system, the value is `light` or `dark`, it can be obtained only when `"darkmode":true` is configured globally, otherwise it is undefined (does not support mini-game) |
| `host`              | `HostInfo`                                                                                                               | Host environment for current Mini Programs                                                                                                                                                     |

---

## Theme

Ƭ **Theme**: `"light"` \| `"dark"`

## HostInfo

Ƭ **HostInfo**: `Object`

Type declaration

| Name             | Type     | Description        |
| :--------------- | :------- | :----------------- |
| `appId`          | `string` | host appid         |
| `hostAppId`      | `string` | host app id        |
| `hostAppName`    | `string` | host app name      |
| `hostAppVersion` | `string` | host app version   |
| `mpVersion`      | `string` | mp version         |
| `routeUrl`       | `string` | host app route url |