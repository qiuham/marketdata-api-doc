---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/call
api_type: Guide
updated_at: 2026-11-27 18:47:31.314640
---

# bn.call

▸ **call**<`Payload`, `Response`\>(`actionName`, `payload?`): `Promise`<`Response`\>

**`description`** Call an custom action.

**`example`**

```ts
const response = await bn.call("private-BIDS-social-login", {});
```

Type parameters

| Name       | Type                     |
| :--------- | :----------------------- |
| `Payload`  | extends `Data`           |
| `Response` | extends `void` \| `Data` |

Parameters

| Name         | Type      |
| :----------- | :-------- |
| `actionName` | `string`  |
| `payload?`   | `Payload` |

Returns

`Promise`<`Response`\>

---

## Data

Ƭ **Data**: `Object`

---

---

# bn.call

▸ **call**<`Payload`, `Response`\>(`actionName`, `payload?`): `Promise`<`Response`\>

**`description`** Call an custom action.

**`example`**

```ts
const response = await bn.call("private-BIDS-social-login", {});
```

Type parameters

| Name       | Type                     |
| :--------- | :----------------------- |
| `Payload`  | extends `Data`           |
| `Response` | extends `void` \| `Data` |

Parameters

| Name         | Type      |
| :----------- | :-------- |
| `actionName` | `string`  |
| `payload?`   | `Payload` |

Returns

`Promise`<`Response`\>

---

## Data

Ƭ **Data**: `Object`

---