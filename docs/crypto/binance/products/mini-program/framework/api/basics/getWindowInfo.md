---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getWindowInfo
api_type: Guide
updated_at: 2026-11-19 18:50:43.225856
---

# bn.getWindowInfo

▸ **getWindowInfo**(): `WindowInfo`

**`description`** The api to get system window info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const windowInfo = bn.getWindowInfo();
console.log(windowInfo.pixelRatio);
console.log(windowInfo.screenWidth);
console.log(windowInfo.screenHeight);
console.log(windowInfo.windowWidth);
console.log(windowInfo.windowHeight);
console.log(windowInfo.statusBarHeight);
console.log(windowInfo.safeArea);
```

Returns

`WindowInfo`

WindowInfo

---

## WindowInfo

Ƭ **WindowInfo**: `Object`

Type declaration

| Name              | Type                                                                                                                     | Description                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| `pixelRatio`      | `number`                                                                                                                 | device pixel ratio                                           |
| `screenWidth`     | `number`                                                                                                                 | Screen width, in px                                          |
| `screenHeight`    | `number`                                                                                                                 | Screen height, in px                                         |
| `windowWidth`     | `number`                                                                                                                 | Available window width, unit px                              |
| `windowHeight`    | `number`                                                                                                                 | Available window height, in px                               |
| `statusBarHeight` | `number`                                                                                                                 | Height of status bar in px                                   |
| `safeArea`        | { `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` ; `width`: `number` ; `height`: `number` } | A safe area in the positive direction of the vertical screen |
| `safeArea.left`   | `number`                                                                                                                 | Upper left abscissa of security area                         |
| `safeArea.right`  | `number`                                                                                                                 | Security area lower right abscissa                           |
| `safeArea.top`    | `number`                                                                                                                 | Top-left ordinate of security area                           |
| `safeArea.bottom` | `number`                                                                                                                 | Lower right ordinate of security area                        |
| `safeArea.width`  | `number`                                                                                                                 | Width of security area, unit logical pixels                  |
| `safeArea.height` | `number`                                                                                                                 | Height of Safe Area, Unit Logical Pixels                     |

---

---

# bn.getWindowInfo

▸ **getWindowInfo**(): `WindowInfo`

**`description`** The api to get system window info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const windowInfo = bn.getWindowInfo();
console.log(windowInfo.pixelRatio);
console.log(windowInfo.screenWidth);
console.log(windowInfo.screenHeight);
console.log(windowInfo.windowWidth);
console.log(windowInfo.windowHeight);
console.log(windowInfo.statusBarHeight);
console.log(windowInfo.safeArea);
```

Returns

`WindowInfo`

WindowInfo

---

## WindowInfo

Ƭ **WindowInfo**: `Object`

Type declaration

| Name              | Type                                                                                                                     | Description                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| `pixelRatio`      | `number`                                                                                                                 | device pixel ratio                                           |
| `screenWidth`     | `number`                                                                                                                 | Screen width, in px                                          |
| `screenHeight`    | `number`                                                                                                                 | Screen height, in px                                         |
| `windowWidth`     | `number`                                                                                                                 | Available window width, unit px                              |
| `windowHeight`    | `number`                                                                                                                 | Available window height, in px                               |
| `statusBarHeight` | `number`                                                                                                                 | Height of status bar in px                                   |
| `safeArea`        | { `left`: `number` ; `right`: `number` ; `top`: `number` ; `bottom`: `number` ; `width`: `number` ; `height`: `number` } | A safe area in the positive direction of the vertical screen |
| `safeArea.left`   | `number`                                                                                                                 | Upper left abscissa of security area                         |
| `safeArea.right`  | `number`                                                                                                                 | Security area lower right abscissa                           |
| `safeArea.top`    | `number`                                                                                                                 | Top-left ordinate of security area                           |
| `safeArea.bottom` | `number`                                                                                                                 | Lower right ordinate of security area                        |
| `safeArea.width`  | `number`                                                                                                                 | Width of security area, unit logical pixels                  |
| `safeArea.height` | `number`                                                                                                                 | Height of Safe Area, Unit Logical Pixels                     |

---