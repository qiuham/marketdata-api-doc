---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/request
api_type: Guide
updated_at: 2026-11-19 18:47:28.322668
---

# bn.request

▸ **request**(`options`): `RequestTask`

Initiates an HTTPS request.

**`example`**

```js
bn.request({
  url: "https://nezha-mock.fe.qa1fdg.net/order",
  responseType: "text",
  dataType: "json",
  success: (res) => {
    console.log(res);
  },
});
```

Parameters

| Name      | Type                                                                                           | Description     |
| :-------- | :--------------------------------------------------------------------------------------------- | :-------------- |
| `options` | `RequestOption`<`string` \| `ArrayBuffer` \| `IUnknownObject`\> & { `signal?`: `AbortSignal` } | request options |

Returns

`RequestTask`

request task

---

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

## Interface: RequestTask

| Name               | Type                  | Description                                                                                   |
| :----------------- | :-------------------- | :-------------------------------------------------------------------------------------------- |
| abort              | (): `void`            | Interrupt request task                                                                        |
| offHeadersReceived | (`callback?`): `void` | Cancel listening for HTTP Response Header event                                               |
| onHeadersReceived  | (`callback`): `void`  | Listen to the HTTP Response Header event. Will be earlier than the requested completion event |

### abort

▸ **abort**(): `void`

Interrupt request task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

Cancel listening for HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

Listen to the HTTP Response Header event. Will be earlier than the requested completion event

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

## OffHeadersReceivedCallback

Ƭ **OffHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## Interface: OnHeadersReceivedCallbackResult

| Name   | Type      | Description          |
| :----- | :-------- | :------------------- |
| header | `Headers` | HTTP Response Header |

## OnHeadersReceivedCallback

Ƭ **OnHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

---

# bn.request

▸ **request**(`options`): `RequestTask`

Initiates an HTTPS request.

**`example`**

```js
bn.request({
  url: "https://nezha-mock.fe.qa1fdg.net/order",
  responseType: "text",
  dataType: "json",
  success: (res) => {
    console.log(res);
  },
});
```

Parameters

| Name      | Type                                                                                           | Description     |
| :-------- | :--------------------------------------------------------------------------------------------- | :-------------- |
| `options` | `RequestOption`<`string` \| `ArrayBuffer` \| `IUnknownObject`\> & { `signal?`: `AbortSignal` } | request options |

Returns

`RequestTask`

request task

---

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

## Interface: RequestTask

| Name               | Type                  | Description                                                                                   |
| :----------------- | :-------------------- | :-------------------------------------------------------------------------------------------- |
| abort              | (): `void`            | Interrupt request task                                                                        |
| offHeadersReceived | (`callback?`): `void` | Cancel listening for HTTP Response Header event                                               |
| onHeadersReceived  | (`callback`): `void`  | Listen to the HTTP Response Header event. Will be earlier than the requested completion event |

### abort

▸ **abort**(): `void`

Interrupt request task

Returns

`void`

---

### offHeadersReceived

▸ **offHeadersReceived**(`callback?`): `void`

Cancel listening for HTTP Response Header event

Parameters

| Name        | Type                         |
| :---------- | :--------------------------- |
| `callback?` | `OffHeadersReceivedCallback` |

Returns

`void`

---

### onHeadersReceived

▸ **onHeadersReceived**(`callback`): `void`

Listen to the HTTP Response Header event. Will be earlier than the requested completion event

Parameters

| Name       | Type                        |
| :--------- | :-------------------------- |
| `callback` | `OnHeadersReceivedCallback` |

Returns

`void`

## OffHeadersReceivedCallback

Ƭ **OffHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---

## Interface: OnHeadersReceivedCallbackResult

| Name   | Type      | Description          |
| :----- | :-------- | :------------------- |
| header | `Headers` | HTTP Response Header |

## OnHeadersReceivedCallback

Ƭ **OnHeadersReceivedCallback**: (`result`: `OnHeadersReceivedCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnHeadersReceivedCallbackResult` |

Returns

`void`

---