---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/canIUseCustom
api_type: Guide
updated_at: 2026-11-28 18:46:34.971979
---

# bn.canIUseCustom

▸ **canIUseCustom**(`options`): `Promise`<`boolean`\>

**`description`** Check if a custom action or event is usable. parameter { action?: string, event?:
string }

**`example`**

```ts
const result = await bn.canIUseCustom({ action: "bnlive-test" });
```

Parameters

| Name      | Type            |
| :-------- | :-------------- |
| `options` | `CanUseOptions` |

Returns

`Promise`<`boolean`\>

---

## CanUseOptions

Ƭ **CanUseOptions**: `Object`

Type declaration

| Name      | Type     |
| :-------- | :------- |
| `action?` | `string` |
| `event?`  | `string` |

---

---

# bn.canIUseCustom

▸ **canIUseCustom**(`options`): `Promise`<`boolean`\>

**`description`** Check if a custom action or event is usable. parameter { action?: string, event?:
string }

**`example`**

```ts
const result = await bn.canIUseCustom({ action: "bnlive-test" });
```

Parameters

| Name      | Type            |
| :-------- | :-------------- |
| `options` | `CanUseOptions` |

Returns

`Promise`<`boolean`\>

---

## CanUseOptions

Ƭ **CanUseOptions**: `Object`

Type declaration

| Name      | Type     |
| :-------- | :------- |
| `action?` | `string` |
| `event?`  | `string` |

---