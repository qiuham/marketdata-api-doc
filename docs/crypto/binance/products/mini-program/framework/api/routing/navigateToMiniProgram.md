---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/routing/navigateToMiniProgram
api_type: Guide
updated_at: 2026-11-19 18:46:37.002436
---

# bn.navigateToMiniProgram

▸ **navigateToMiniProgram**(`options`): `Promise`<`void`\>

**`description`** Opens another Mini Program

**`example`**

```js
bn.navigateToMiniProgram({
  appId: "",
  path: "page/1",
  extraData: {
    foo: "bar",
  },
  envVersion: "published",
  type: "app",
  rev: "006a05ebf14db3e4a8e69cb6bc8b2589",
});
```

Parameters

| Name      | Type                           | Description         |
| :-------- | :----------------------------- | :------------------ |
| `options` | `NavigateToMiniProgramOptions` | Navigate to options |

Returns

`Promise`<`void`\>

---

## Interface: NavigateToMiniProgramOptions

| Name         | Type                  | Description                                                                                                                                                                                                                                |
| :----------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type?        | `NavigationMPType`    | The type of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                           |
| appId        | `string`              | The appId of the Mini Program to be opened                                                                                                                                                                                                 |
| rev?         | `string`              | The rev of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                            |
| envVersion?  | `NavigationMPChannel` | The channel of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                        |
| extraData?   | `Object`              | The data that needs to be passed to the target Mini Program. The target Mini Program can obtain this data from App.onLaunch and App.onShow                                                                                                 |
| path?        | `string`              | The path of the page to be opened. If it is empty, the homepage is opened. Content following the question mark (?) in the path becomes a query                                                                                             |
| mpModalType? | `"replace"`           | **`description`** behavior type of the current app after navigateToMiniProgram is called**`remark`** supported jssdk >= 4.3.0. only support "replace" by now. With this type, the app where navigateToMiniProgram is called will be closed |

---

# bn.navigateToMiniProgram

▸ **navigateToMiniProgram**(`options`): `Promise`<`void`\>

**`description`** Opens another Mini Program

**`example`**

```js
bn.navigateToMiniProgram({
  appId: "",
  path: "page/1",
  extraData: {
    foo: "bar",
  },
  envVersion: "published",
  type: "app",
  rev: "006a05ebf14db3e4a8e69cb6bc8b2589",
});
```

Parameters

| Name      | Type                           | Description         |
| :-------- | :----------------------------- | :------------------ |
| `options` | `NavigateToMiniProgramOptions` | Navigate to options |

Returns

`Promise`<`void`\>

---

## Interface: NavigateToMiniProgramOptions

| Name         | Type                  | Description                                                                                                                                                                                                                                |
| :----------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type?        | `NavigationMPType`    | The type of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                           |
| appId        | `string`              | The appId of the Mini Program to be opened                                                                                                                                                                                                 |
| rev?         | `string`              | The rev of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                            |
| envVersion?  | `NavigationMPChannel` | The channel of the Mini Program to be opened. It is valid when target="miniProgram"                                                                                                                                                        |
| extraData?   | `Object`              | The data that needs to be passed to the target Mini Program. The target Mini Program can obtain this data from App.onLaunch and App.onShow                                                                                                 |
| path?        | `string`              | The path of the page to be opened. If it is empty, the homepage is opened. Content following the question mark (?) in the path becomes a query                                                                                             |
| mpModalType? | `"replace"`           | **`description`** behavior type of the current app after navigateToMiniProgram is called**`remark`** supported jssdk >= 4.3.0. only support "replace" by now. With this type, the app where navigateToMiniProgram is called will be closed |