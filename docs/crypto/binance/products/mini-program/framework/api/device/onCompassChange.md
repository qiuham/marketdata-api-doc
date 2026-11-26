---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onCompassChange
api_type: Guide
updated_at: 2026-11-26 18:48:07.871586
---

# bn.onCompassChange

▸ **onCompassChange**(`cb`): `void`

**`description`** Monitor compass data changes. Frequency: 5 second/Seconds, the interface will
automatically start listening after the call, you can use the bn.stopCompass Stop listening.

**`example`**

```ts
bn.onCompassChange(callback);
```

Parameters

| Name | Type                      |
| :--- | :------------------------ |
| `cb` | `OnCompassChangeCallback` |

Returns

`void`

---

## OnCompassChangeCallback

Ƭ **OnCompassChangeCallback**: (`result`: `OnCompassChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function for compass data change events

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `OnCompassChangeCallbackResult` |

Returns

`void`

---

## Interface: OnCompassChangeCallbackResult

| Name      | Type                 | Description               |
| :-------- | :------------------- | :------------------------ |
| accuracy  | `string` \| `number` | accuracy                  |
| direction | `number`             | Degree of direction faced |

---

# bn.onCompassChange

▸ **onCompassChange**(`cb`): `void`

**`description`** Monitor compass data changes. Frequency: 5 second/Seconds, the interface will
automatically start listening after the call, you can use the bn.stopCompass Stop listening.

**`example`**

```ts
bn.onCompassChange(callback);
```

Parameters

| Name | Type                      |
| :--- | :------------------------ |
| `cb` | `OnCompassChangeCallback` |

Returns

`void`

---

## OnCompassChangeCallback

Ƭ **OnCompassChangeCallback**: (`result`: `OnCompassChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function for compass data change events

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `OnCompassChangeCallbackResult` |

Returns

`void`

---

## Interface: OnCompassChangeCallbackResult

| Name      | Type                 | Description               |
| :-------- | :------------------- | :------------------------ |
| accuracy  | `string` \| `number` | accuracy                  |
| direction | `number`             | Degree of direction faced |