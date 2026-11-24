---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/getBackgroundFetchToken
api_type: Guide
updated_at: 2026-11-24 18:45:18.227017
---

# bn.getBackgroundFetchToken

▸ **getBackgroundFetchToken**(): `Promise`<`SetFetchTokenOptions`\>

**`description`** Gets the custom login state that has been set. If not, the promise will be
rejected.

**`example`**

```ts
const { token } = bn.getBackgroundFetchToken();
```

Returns

`Promise`<`SetFetchTokenOptions`\>

---

## Interface: SetFetchTokenOptions

| Name  | Type     | Description         |
| :---- | :------- | :------------------ |
| token | `string` | Custom login states |

---

# bn.getBackgroundFetchToken

▸ **getBackgroundFetchToken**(): `Promise`<`SetFetchTokenOptions`\>

**`description`** Gets the custom login state that has been set. If not, the promise will be
rejected.

**`example`**

```ts
const { token } = bn.getBackgroundFetchToken();
```

Returns

`Promise`<`SetFetchTokenOptions`\>

---

## Interface: SetFetchTokenOptions

| Name  | Type     | Description         |
| :---- | :------- | :------------------ |
| token | `string` | Custom login states |