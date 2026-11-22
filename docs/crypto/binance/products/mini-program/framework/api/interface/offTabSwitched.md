---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/offTabSwitched
api_type: Guide
updated_at: 2026-11-22 18:43:52.695476
---

# bn.offTabSwitched

▸ **offTabSwitched**(`cb`): `void`

**`description`** remove tab item switch listener

**`example`**

```ts
const handler = (params) => {
  console.log("tab swtiched: ", params);
};
bn.onTabSwitched(handler);
bn.offTabSwitched(handler);
```

Parameters

| Name | Type                  |
| :--- | :-------------------- |
| `cb` | `TabSwtichedCallback` |

Returns

`void`

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

# bn.offTabSwitched

▸ **offTabSwitched**(`cb`): `void`

**`description`** remove tab item switch listener

**`example`**

```ts
const handler = (params) => {
  console.log("tab swtiched: ", params);
};
bn.onTabSwitched(handler);
bn.offTabSwitched(handler);
```

Parameters

| Name | Type                  |
| :--- | :-------------------- |
| `cb` | `TabSwtichedCallback` |

Returns

`void`

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