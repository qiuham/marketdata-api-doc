---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/callAll
api_type: Guide
updated_at: 2026-11-25 18:48:55.951284
---

# bn.callAll

▸ **callAll**(`actions`): `Promise`<`CallAllResponse`\>

**`description`** Call multiple custom actions in sequence and return all results.

**`example`**

```ts
const results = await bn.callAll([
  { action: "action1", payload: { data: "test1" } },
  { action: "action2", payload: { data: "test2" } },
]);
console.log(results);
{
  results: [{ result: { data: "test1" } }, { error: "error", result: null }];
}
```

Parameters

| Name      | Type                                         |
| :-------- | :------------------------------------------- |
| `actions` | { `action`: `string` ; `payload?`: `any` }[] |

Returns

`Promise`<`CallAllResponse`\>

## Interface: CallAllResponse

| Name    | Type                                    | Description |
| :------ | :-------------------------------------- | :---------- |
| results | { `error?`: `any` ; `result`: `any` }[] |             |

---

# bn.callAll

▸ **callAll**(`actions`): `Promise`<`CallAllResponse`\>

**`description`** Call multiple custom actions in sequence and return all results.

**`example`**

```ts
const results = await bn.callAll([
  { action: "action1", payload: { data: "test1" } },
  { action: "action2", payload: { data: "test2" } },
]);
console.log(results);
{
  results: [{ result: { data: "test1" } }, { error: "error", result: null }];
}
```

Parameters

| Name      | Type                                         |
| :-------- | :------------------------------------------- |
| `actions` | { `action`: `string` ; `payload?`: `any` }[] |

Returns

`Promise`<`CallAllResponse`\>

## Interface: CallAllResponse

| Name    | Type                                    | Description |
| :------ | :-------------------------------------- | :---------- |
| results | { `error?`: `any` ; `result`: `any` }[] |             |