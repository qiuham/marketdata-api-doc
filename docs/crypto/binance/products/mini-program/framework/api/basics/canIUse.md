---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/canIUse
api_type: Guide
updated_at: 2026-11-21 18:48:23.353825
---

# bn.canIUse

▸ **canIUse**(`schema`): `boolean`

**`description`** Determine if Mini Programs' APIs, callbacks, parameters, components, etc are
available in the current version. Parameter schema: - \${API}.\${method}.\${param}.\${option}

**`example`**

```ts
bn.canIUse("console.log");
bn.canIUse("getSystemInfoSync");
```

Parameters

| Name     | Type     |
| :------- | :------- |
| `schema` | `string` |

Returns

`boolean`

---

# bn.canIUse

▸ **canIUse**(`schema`): `boolean`

**`description`** Determine if Mini Programs' APIs, callbacks, parameters, components, etc are
available in the current version. Parameter schema: - \${API}.\${method}.\${param}.\${option}

**`example`**

```ts
bn.canIUse("console.log");
bn.canIUse("getSystemInfoSync");
```

Parameters

| Name     | Type     |
| :------- | :------- |
| `schema` | `string` |

Returns

`boolean`