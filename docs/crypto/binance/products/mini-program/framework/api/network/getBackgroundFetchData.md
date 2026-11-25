---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/getBackgroundFetchData
api_type: Guide
updated_at: 2026-11-25 18:45:24.068651
---

# bn.getBackgroundFetchData

▸ **getBackgroundFetchData**(`options`): `Promise`<`GetBackgroundFetchDataResult`\>

**`description`** Get backgroundFetch cache. If current request is still ongoing this api will
return previous cache. If no cache at all this api will reject.

**`example`**

```ts
const { fetchedData, timeStamp, errMsg, path, query, scene } = bn.getBackgroundFetchData({
  fetchType: "pre",
});
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `GetFetchDataOptions` |

Returns

`Promise`<`GetBackgroundFetchDataResult`\>

---

## GetFetchDataOptions

Ƭ **GetFetchDataOptions**: `Object`

Type declaration

| Name        | Type                    | Description                                          |
| :---------- | :---------------------- | :--------------------------------------------------- |
| `fetchType` | `"periodic"` \| `"pre"` | Cache data category, with a value of periodic or pre |

---

## Interface: GetBackgroundFetchDataResult

| Name        | Type     | Description                                     |
| :---------- | :------- | :---------------------------------------------- |
| fetchedData | `string` | Cache data                                      |
| timeStamp   | `number` | The timestamp of client getting the cached data |
| errMsg      | `string` | Error message if there's an error               |
| path?       | `string` | The route path of mini program                  |
| query?      | `string` | The query data passed to the page               |
| scene?      | `number` | Scene value of entering page                    |

---

# bn.getBackgroundFetchData

▸ **getBackgroundFetchData**(`options`): `Promise`<`GetBackgroundFetchDataResult`\>

**`description`** Get backgroundFetch cache. If current request is still ongoing this api will
return previous cache. If no cache at all this api will reject.

**`example`**

```ts
const { fetchedData, timeStamp, errMsg, path, query, scene } = bn.getBackgroundFetchData({
  fetchType: "pre",
});
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `GetFetchDataOptions` |

Returns

`Promise`<`GetBackgroundFetchDataResult`\>

---

## GetFetchDataOptions

Ƭ **GetFetchDataOptions**: `Object`

Type declaration

| Name        | Type                    | Description                                          |
| :---------- | :---------------------- | :--------------------------------------------------- |
| `fetchType` | `"periodic"` \| `"pre"` | Cache data category, with a value of periodic or pre |

---

## Interface: GetBackgroundFetchDataResult

| Name        | Type     | Description                                     |
| :---------- | :------- | :---------------------------------------------- |
| fetchedData | `string` | Cache data                                      |
| timeStamp   | `number` | The timestamp of client getting the cached data |
| errMsg      | `string` | Error message if there's an error               |
| path?       | `string` | The route path of mini program                  |
| query?      | `string` | The query data passed to the page               |
| scene?      | `number` | Scene value of entering page                    |