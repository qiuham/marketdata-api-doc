---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/getPrefetchCacheSync
api_type: Guide
updated_at: 2026-11-18 18:44:22.359291
---

# bn.getPrefetchCacheSync

▸ **getPrefetchCacheSync**(`options`): `PrefetchCacheResult`

get prefetch cache data synchronously. If prefetch data is not ready, it will return `undefined`.

**`example`**

```js
let res;
try {
  res = bn.getPrefetchCacheSync?.({ url: "https://nezha-mock.fe.qa1fdg.net/order" });
} catch (e) {}
console.log(res, res.result);
```

Parameters

| Name      | Type                                                            | Description            |
| :-------- | :-------------------------------------------------------------- | :--------------------- |
| `options` | `RequestOption`<`string` \| `ArrayBuffer` \| `IUnknownObject`\> | prefetch cache options |

Returns

`PrefetchCacheResult`

prefetch cache result

## Interface: RequestOption<T\>

| Name              | Type                                                                    | Description                                                                                                                     |
| :---------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| url               | `string`                                                                | request url                                                                                                                     |
| data?             | `string` \| `ArrayBuffer` \| `IUnknownObject`                           | request params                                                                                                                  |
| header?           | `Headers`                                                               | set request header, can't set `Referer`. default value of `content-type` is `application/json`                                  |
| timeout?          | `number`                                                                | timeout of request, unit is millisecond                                                                                         |
| method?           | `"OPTIONS"` \| `"HEAD"` \| `"GET"` \| `"POST"` \| `"PUT"` \| `"DELETE"` | HTTP request method                                                                                                             |
| dataType?         | `string`                                                                | Returned data format. 'json' - the returned data is JSON. After returning, `JSON.parse` will be performed on the returned data. |
| responseType?     | `"text"` \| `"arraybuffer"`                                             | Response data type. 'text' - The response data is text; 'arraybuffer' - The response data is ArrayBuffer                        |
| usePrefetchCache? | `boolean`                                                               | using prefetched data**`remark`** support from jssdk > 4.0.0                                                                    |
| fail?             | `RequestFailCallback`                                                   | Callback function for failed interface call                                                                                     |
| success?          | `RequestSuccessCallback`<`T`\>                                          | Callback function for successful interface call                                                                                 |
| complete?         | `RequestCompleteCallback`                                               | he callback function for the end of the interface call                                                                          |
| enableCache?      | `boolean`                                                               |                                                                                                                                 |

## IUnknownObject

Ƭ **IUnknownObject**: `Object`

---

## Interface: PrefetchCacheResult

| Name   | Type     | Description         |
| :----- | :------- | :------------------ |
| result | `Object` | prefetch cache data |

---

# bn.getPrefetchCacheSync

▸ **getPrefetchCacheSync**(`options`): `PrefetchCacheResult`

get prefetch cache data synchronously. If prefetch data is not ready, it will return `undefined`.

**`example`**

```js
let res;
try {
  res = bn.getPrefetchCacheSync?.({ url: "https://nezha-mock.fe.qa1fdg.net/order" });
} catch (e) {}
console.log(res, res.result);
```

Parameters

| Name      | Type                                                            | Description            |
| :-------- | :-------------------------------------------------------------- | :--------------------- |
| `options` | `RequestOption`<`string` \| `ArrayBuffer` \| `IUnknownObject`\> | prefetch cache options |

Returns

`PrefetchCacheResult`

prefetch cache result

## Interface: RequestOption<T\>

| Name              | Type                                                                    | Description                                                                                                                     |
| :---------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| url               | `string`                                                                | request url                                                                                                                     |
| data?             | `string` \| `ArrayBuffer` \| `IUnknownObject`                           | request params                                                                                                                  |
| header?           | `Headers`                                                               | set request header, can't set `Referer`. default value of `content-type` is `application/json`                                  |
| timeout?          | `number`                                                                | timeout of request, unit is millisecond                                                                                         |
| method?           | `"OPTIONS"` \| `"HEAD"` \| `"GET"` \| `"POST"` \| `"PUT"` \| `"DELETE"` | HTTP request method                                                                                                             |
| dataType?         | `string`                                                                | Returned data format. 'json' - the returned data is JSON. After returning, `JSON.parse` will be performed on the returned data. |
| responseType?     | `"text"` \| `"arraybuffer"`                                             | Response data type. 'text' - The response data is text; 'arraybuffer' - The response data is ArrayBuffer                        |
| usePrefetchCache? | `boolean`                                                               | using prefetched data**`remark`** support from jssdk > 4.0.0                                                                    |
| fail?             | `RequestFailCallback`                                                   | Callback function for failed interface call                                                                                     |
| success?          | `RequestSuccessCallback`<`T`\>                                          | Callback function for successful interface call                                                                                 |
| complete?         | `RequestCompleteCallback`                                               | he callback function for the end of the interface call                                                                          |
| enableCache?      | `boolean`                                                               |                                                                                                                                 |

## IUnknownObject

Ƭ **IUnknownObject**: `Object`

---

## Interface: PrefetchCacheResult

| Name   | Type     | Description         |
| :----- | :------- | :------------------ |
| result | `Object` | prefetch cache data |