---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onAccelerometerChange
api_type: Guide
updated_at: 2026-11-18 02:42:57.784482
---

# bn.onAccelerometerChange

▸ **onAccelerometerChange**(`cb`): `void`

**`description`** Listen for acceleration data events. Frequency basis bn.startAccelerometer() of
interval Parameters, Interface calls automatically start listening.

**`example`**

```ts
bn.onAccelerometerChange(callback);
```

Parameters

| Name | Type                            |
| :--- | :------------------------------ |
| `cb` | `OnAccelerometerChangeCallback` |

Returns

`void`

---

## OnAccelerometerChangeCallback

Ƭ **OnAccelerometerChangeCallback**: (`result`: `OnAccelerometerChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Acceleration Data Event Callback Function

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `result` | `OnAccelerometerChangeCallbackResult` |

Returns

`void`

---

## Interface: OnAccelerometerChangeCallbackResult

| Name | Type     | Description |
| :--- | :------- | :---------- |
| x    | `number` | X axis      |
| y    | `number` | Y axis      |
| z    | `number` | Z axis      |

---

# bn.onAccelerometerChange

▸ **onAccelerometerChange**(`cb`): `void`

**`description`** Listen for acceleration data events. Frequency basis bn.startAccelerometer() of
interval Parameters, Interface calls automatically start listening.

**`example`**

```ts
bn.onAccelerometerChange(callback);
```

Parameters

| Name | Type                            |
| :--- | :------------------------------ |
| `cb` | `OnAccelerometerChangeCallback` |

Returns

`void`

---

## OnAccelerometerChangeCallback

Ƭ **OnAccelerometerChangeCallback**: (`result`: `OnAccelerometerChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Acceleration Data Event Callback Function

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `result` | `OnAccelerometerChangeCallbackResult` |

Returns

`void`

---

## Interface: OnAccelerometerChangeCallbackResult

| Name | Type     | Description |
| :--- | :------- | :---------- |
| x    | `number` | X axis      |
| y    | `number` | Y axis      |
| z    | `number` | Z axis      |