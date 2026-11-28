---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/getUserOpenid
api_type: Guide
updated_at: 2026-11-28 18:43:08.104876
---

# bn.getUserOpenid

▸ **getUserOpenid**(): `Promise`<`GetUserOpenidResponse`\>

**`description`** Get user’s openid for the mini program.

**`remark`** support jssdk >= 4.7.0

**`example`**

```ts
const response = await bn.getUserOpenid();
```

Returns

`Promise`<`GetUserOpenidResponse`\>

GetUserOpenidResponse

---

## Interface: GetUserOpenidResponse

| Name    | Type     | Description                                                         |
| :------ | :------- | :------------------------------------------------------------------ |
| openId? | `string` | user’s openid(Native does not return the openId field after 4.10.0) |
| token   | `string` | encrypted token                                                     |

---

# bn.getUserOpenid

▸ **getUserOpenid**(): `Promise`<`GetUserOpenidResponse`\>

**`description`** Get user’s openid for the mini program.

**`remark`** support jssdk >= 4.7.0

**`example`**

```ts
const response = await bn.getUserOpenid();
```

Returns

`Promise`<`GetUserOpenidResponse`\>

GetUserOpenidResponse

---

## Interface: GetUserOpenidResponse

| Name    | Type     | Description                                                         |
| :------ | :------- | :------------------------------------------------------------------ |
| openId? | `string` | user’s openid(Native does not return the openId field after 4.10.0) |
| token   | `string` | encrypted token                                                     |