---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/onAppShow
api_type: Guide
updated_at: 2026-11-24 18:47:58.666796
---

# bn.onAppShow

• **onAppShow**: (`cb`: `AppShowCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type              |
| :--- | :---------------- |
| `cb` | `AppShowCallback` |

Returns

`void`

---

## AppShowCallback

Ƭ **AppShowCallback**: (`result`: `LaunchShowOptions`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                |
| :------- | :------------------ |
| `result` | `LaunchShowOptions` |

Returns

`void`

---

## LaunchShowOptions

Ƭ **LaunchShowOptions**: `Object`

Type declaration

| Name                      | Type                                            |
| :------------------------ | :---------------------------------------------- |
| `path`                    | `string`                                        |
| `query`                   | `Query`                                         |
| `scene`                   | `number`                                        |
| `referrerInfo?`           | { `appId?`: `string` ; `extraData?`: `object` } |
| `referrerInfo.appId?`     | `string`                                        |
| `referrerInfo.extraData?` | `object`                                        |

---

## Query

Ƭ **Query**: `Object`

---

---

# bn.onAppShow

• **onAppShow**: (`cb`: `AppShowCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type              |
| :--- | :---------------- |
| `cb` | `AppShowCallback` |

Returns

`void`

---

## AppShowCallback

Ƭ **AppShowCallback**: (`result`: `LaunchShowOptions`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                |
| :------- | :------------------ |
| `result` | `LaunchShowOptions` |

Returns

`void`

---

## LaunchShowOptions

Ƭ **LaunchShowOptions**: `Object`

Type declaration

| Name                      | Type                                            |
| :------------------------ | :---------------------------------------------- |
| `path`                    | `string`                                        |
| `query`                   | `Query`                                         |
| `scene`                   | `number`                                        |
| `referrerInfo?`           | { `appId?`: `string` ; `extraData?`: `object` } |
| `referrerInfo.appId?`     | `string`                                        |
| `referrerInfo.extraData?` | `object`                                        |

---

## Query

Ƭ **Query**: `Object`

---