---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/callAnotherApp
api_type: Guide
updated_at: 2026-11-23 18:49:10.788247
---

# bn.callAnotherApp

▸ **callAnotherApp**<`T`\>(`options`): `Promise`<`T`\>

**`description`** Used for cross mini-app communication. Need permission to use. The target app must
be currently running and register the action.

**`remark`** supported jssdk > 4.26.0

**`example`**

```ts
const res = await bn.callAnotherApp({ action: "aciton" });
```

Type parameters

| Name | Type  |
| :--- | :---- |
| `T`  | `any` |

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `CallAnotherAppOptions` |

Returns

`Promise`<`T`\>

---

## Interface: CallAnotherAppOptions

| Name     | Type                       | Description |
| :------- | :------------------------- | :---------- |
| action   | `string`                   |             |
| payload? | `Record`<`string`, `any`\> |             |
| id?      | `string`                   |             |

---

# bn.callAnotherApp

▸ **callAnotherApp**<`T`\>(`options`): `Promise`<`T`\>

**`description`** Used for cross mini-app communication. Need permission to use. The target app must
be currently running and register the action.

**`remark`** supported jssdk > 4.26.0

**`example`**

```ts
const res = await bn.callAnotherApp({ action: "aciton" });
```

Type parameters

| Name | Type  |
| :--- | :---- |
| `T`  | `any` |

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `CallAnotherAppOptions` |

Returns

`Promise`<`T`\>

---

## Interface: CallAnotherAppOptions

| Name     | Type                       | Description |
| :------- | :------------------------- | :---------- |
| action   | `string`                   |             |
| payload? | `Record`<`string`, `any`\> |             |
| id?      | `string`                   |             |