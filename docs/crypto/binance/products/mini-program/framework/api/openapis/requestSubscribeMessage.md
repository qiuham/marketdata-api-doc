---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/requestSubscribeMessage
api_type: Guide
updated_at: 2026-11-19 18:46:51.051507
---

# bn.requestSubscribeMessage

▸ **requestSubscribeMessage**(`option`): `Promise`<`RequestSubscribeMessageSuccessCallbackResult`\>

**`remark`** support jssdk >= 3.13.0

**`description`** Set up the client Mini Program subscription message interface and return the
result of user subscription message.

**`example`**

```ts
// usage
const res = await bn.requestSubscribeMessage({
  tmplIds: ["tmplid-1afXeq4c", "tmplid-unDYd3gc"],
});
Object.entries(res).forEach(([id, result]) => {
  if (result.type === "accept") {
    console.log(id, result.token);
  }
});
```

Parameters

| Name     | Type                            | Description                                   |
| :------- | :------------------------------ | :-------------------------------------------- |
| `option` | `RequestSubscribeMessageOption` | an option object include tmplIds to subscribe |

Returns

`Promise`<`RequestSubscribeMessageSuccessCallbackResult`\>

A result object which key is a tmplId and value is the subscribe result for the tmplId.

## Interface: RequestSubscribeMessageOption

| Name    | Type       | Description                           |
| :------ | :--------- | :------------------------------------ |
| tmplIds | `string`[] | the list of template ids to subscribe |

## Interface: RequestSubscribeMessageSuccessCallbackResult

| Name | Type | Description |
| :--- | :--- | :---------- |

---

# bn.requestSubscribeMessage

▸ **requestSubscribeMessage**(`option`): `Promise`<`RequestSubscribeMessageSuccessCallbackResult`\>

**`remark`** support jssdk >= 3.13.0

**`description`** Set up the client Mini Program subscription message interface and return the
result of user subscription message.

**`example`**

```ts
// usage
const res = await bn.requestSubscribeMessage({
  tmplIds: ["tmplid-1afXeq4c", "tmplid-unDYd3gc"],
});
Object.entries(res).forEach(([id, result]) => {
  if (result.type === "accept") {
    console.log(id, result.token);
  }
});
```

Parameters

| Name     | Type                            | Description                                   |
| :------- | :------------------------------ | :-------------------------------------------- |
| `option` | `RequestSubscribeMessageOption` | an option object include tmplIds to subscribe |

Returns

`Promise`<`RequestSubscribeMessageSuccessCallbackResult`\>

A result object which key is a tmplId and value is the subscribe result for the tmplId.

## Interface: RequestSubscribeMessageOption

| Name    | Type       | Description                           |
| :------ | :--------- | :------------------------------------ |
| tmplIds | `string`[] | the list of template ids to subscribe |

## Interface: RequestSubscribeMessageSuccessCallbackResult

| Name | Type | Description |
| :--- | :--- | :---------- |