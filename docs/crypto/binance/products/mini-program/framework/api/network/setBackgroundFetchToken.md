---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/setBackgroundFetchToken
api_type: Guide
updated_at: 2026-11-23 18:45:26.256925
---

# bn.setBackgroundFetchToken

▸ **setBackgroundFetchToken**(`options`): `Promise`<{}\>

**`description`** Set the custom login state, in the periodic pull data, to make third-party server
verification request authorized.

**`example`**

```ts
await bn.setBackgroundFetchToken({ token: "token" });
```

Parameters

| Name      | Type                   |
| :-------- | :--------------------- |
| `options` | `SetFetchTokenOptions` |

Returns

`Promise`<{}\>

---

## Interface: SetFetchTokenOptions

| Name  | Type     | Description         |
| :---- | :------- | :------------------ |
| token | `string` | Custom login states |

---

# bn.setBackgroundFetchToken

▸ **setBackgroundFetchToken**(`options`): `Promise`<{}\>

**`description`** Set the custom login state, in the periodic pull data, to make third-party server
verification request authorized.

**`example`**

```ts
await bn.setBackgroundFetchToken({ token: "token" });
```

Parameters

| Name      | Type                   |
| :-------- | :--------------------- |
| `options` | `SetFetchTokenOptions` |

Returns

`Promise`<{}\>

---

## Interface: SetFetchTokenOptions

| Name  | Type     | Description         |
| :---- | :------- | :------------------ |
| token | `string` | Custom login states |