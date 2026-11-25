---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/on
api_type: Guide
updated_at: 2026-11-25 18:48:08.723068
---

# bn.on

▸ **on**(`eventName`, `handler`): `void`

**`description`** Listen on custom event.

**`example`**

```ts
const supportEvent = await bn.canIUseCustom({
  event: "private-BIDS-example-event-progress", // native version >= 2.49
});
if (supportEvent) {
  // 1. on-demand subscription, native start to send to events to js
  bn.on("private-BIDS-example-event-progress", () => {});
}
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

# bn.on

▸ **on**(`eventName`, `handler`): `void`

**`description`** Listen on custom event.

**`example`**

```ts
const supportEvent = await bn.canIUseCustom({
  event: "private-BIDS-example-event-progress", // native version >= 2.49
});
if (supportEvent) {
  // 1. on-demand subscription, native start to send to events to js
  bn.on("private-BIDS-example-event-progress", () => {});
}
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