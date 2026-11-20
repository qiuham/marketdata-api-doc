---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/off
api_type: Guide
updated_at: 2026-11-20 18:49:27.778516
---

# bn.off

▸ **off**(`eventName`, `handler`): `void`

**`description`** Un-listen on custom event.

**`example`**

```ts
const handler = () => {};
bn.off("private-BIDS-example-event-progress", handler);
```

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `eventName` | `string`             |
| `handler`   | `CustomEventHandler` |

Returns

`void`

---

## CustomEventHandler

Ƭ **CustomEventHandler**: (`payload`: `Data`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type   |
| :-------- | :----- |
| `payload` | `Data` |

Returns

`void`

## Data

Ƭ **Data**: `Object`

---

---

# bn.off

▸ **off**(`eventName`, `handler`): `void`

**`description`** Un-listen on custom event.

**`example`**

```ts
const handler = () => {};
bn.off("private-BIDS-example-event-progress", handler);
```

Parameters

| Name        | Type                 |
| :---------- | :------------------- |
| `eventName` | `string`             |
| `handler`   | `CustomEventHandler` |

Returns

`void`

---

## CustomEventHandler

Ƭ **CustomEventHandler**: (`payload`: `Data`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type   |
| :-------- | :----- |
| `payload` | `Data` |

Returns

`void`

## Data

Ƭ **Data**: `Object`

---