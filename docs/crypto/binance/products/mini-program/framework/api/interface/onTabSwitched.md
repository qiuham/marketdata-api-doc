---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/onTabSwitched
api_type: Guide
updated_at: 2026-11-18 02:40:58.719042
---

# bn.onTabSwitched

▸ **onTabSwitched**(`cb`): `void`

**`description`** listen tab item switch event

**`example`**

```ts
bn.onTabSwitched((params) => {
  console.log("tab swtiched: ", params);
});
```

Parameters

| Name | Type                  |
| :--- | :-------------------- |
| `cb` | `TabSwtichedCallback` |

Returns

`void`

---

## TabSwtichedCallback

Ƭ **TabSwtichedCallback**: (`data`: `TabSwitchedEventData`) => `void` \| `Promise`<`void`\>

Type declaration

▸ (`data`): `void` \| `Promise`<`void`\>

Parameters

| Name   | Type                   |
| :----- | :--------------------- |
| `data` | `TabSwitchedEventData` |

Returns

`void` \| `Promise`<`void`\>

---

## TabSwitchedEventData

Ƭ **TabSwitchedEventData**: `Object`

Type declaration

| Name       | Type               | Description                                                                                       |
| :--------- | :----------------- | :------------------------------------------------------------------------------------------------ |
| `type`     | `"tap"` \| `"api"` | Action Types: - `api`: triggered by an `bn.switchTab` call. - `tap`: triggered by a manual click. |
| `pagePath` | `string`           | -                                                                                                 |
| `query`    | `string`           | -                                                                                                 |

---

# bn.onTabSwitched

▸ **onTabSwitched**(`cb`): `void`

**`description`** listen tab item switch event

**`example`**

```ts
bn.onTabSwitched((params) => {
  console.log("tab swtiched: ", params);
});
```

Parameters

| Name | Type                  |
| :--- | :-------------------- |
| `cb` | `TabSwtichedCallback` |

Returns

`void`

---

## TabSwtichedCallback

Ƭ **TabSwtichedCallback**: (`data`: `TabSwitchedEventData`) => `void` \| `Promise`<`void`\>

Type declaration

▸ (`data`): `void` \| `Promise`<`void`\>

Parameters

| Name   | Type                   |
| :----- | :--------------------- |
| `data` | `TabSwitchedEventData` |

Returns

`void` \| `Promise`<`void`\>

---

## TabSwitchedEventData

Ƭ **TabSwitchedEventData**: `Object`

Type declaration

| Name       | Type               | Description                                                                                       |
| :--------- | :----------------- | :------------------------------------------------------------------------------------------------ |
| `type`     | `"tap"` \| `"api"` | Action Types: - `api`: triggered by an `bn.switchTab` call. - `tap`: triggered by a manual click. |
| `pagePath` | `string`           | -                                                                                                 |
| `query`    | `string`           | -                                                                                                 |