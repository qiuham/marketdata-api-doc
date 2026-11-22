---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getAppBaseInfo
api_type: Guide
updated_at: 2026-11-22 18:45:30.592696
---

# bn.getAppBaseInfo

▸ **getAppBaseInfo**(): `AppBaseInfo`

**`description`** The api to get app info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const appBaseInfo = bn.getAppBaseInfo();
console.log(appBaseInfo.SDKVersion);
console.log(appBaseInfo.enableDebug);
console.log(appBaseInfo.host);
console.log(appBaseInfo.language);
console.log(appBaseInfo.version);
```

Returns

`AppBaseInfo`

AppBaseInfo

---

## AppBaseInfo

Ƭ **AppBaseInfo**: `Object`

Type declaration

| Name         | Type       | Description          |
| :----------- | :--------- | :------------------- |
| `SDKVersion` | `string`   | sdk version          |
| `host`       | `HostInfo` | host app info        |
| `language`   | `string`   | binance app language |
| `version`    | `string`   | binance app version  |
| `theme?`     | `Theme`    | Not supported in mg  |

---

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

## Theme

Ƭ **Theme**: `"light"` \| `"dark"`

---

# bn.getAppBaseInfo

▸ **getAppBaseInfo**(): `AppBaseInfo`

**`description`** The api to get app info

**`remark`** supported jssdk >= 4.0.0

**`example`**

```ts
const appBaseInfo = bn.getAppBaseInfo();
console.log(appBaseInfo.SDKVersion);
console.log(appBaseInfo.enableDebug);
console.log(appBaseInfo.host);
console.log(appBaseInfo.language);
console.log(appBaseInfo.version);
```

Returns

`AppBaseInfo`

AppBaseInfo

---

## AppBaseInfo

Ƭ **AppBaseInfo**: `Object`

Type declaration

| Name         | Type       | Description          |
| :----------- | :--------- | :------------------- |
| `SDKVersion` | `string`   | sdk version          |
| `host`       | `HostInfo` | host app info        |
| `language`   | `string`   | binance app language |
| `version`    | `string`   | binance app version  |
| `theme?`     | `Theme`    | Not supported in mg  |

---

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

## Theme

Ƭ **Theme**: `"light"` \| `"dark"`