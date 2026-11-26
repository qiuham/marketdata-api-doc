---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/callSync
api_type: Guide
updated_at: 2026-11-26 18:49:21.525476
---

# bn.callSync

▸ **callSync**<`Payload`, `Response`\>(`actionName`, `payload?`): `Response`

**`description`** Call an custom action synchronous. If the plugin of custom action not ready, it
will throw an error.

**`example`**

```ts
try {
  const response = bn.callSync("private-BIDS-social-login", {});
} catch (e) {
  console.error(e);
}
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

`Response`

---

## Data

Ƭ **Data**: `Object`

---

---

# bn.callSync

▸ **callSync**<`Payload`, `Response`\>(`actionName`, `payload?`): `Response`

**`description`** Call an custom action synchronous. If the plugin of custom action not ready, it
will throw an error.

**`example`**

```ts
try {
  const response = bn.callSync("private-BIDS-social-login", {});
} catch (e) {
  console.error(e);
}
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

`Response`

---

## Data

Ƭ **Data**: `Object`

---