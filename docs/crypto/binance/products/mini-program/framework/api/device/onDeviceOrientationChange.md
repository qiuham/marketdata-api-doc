---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onDeviceOrientationChange
api_type: Guide
updated_at: 2026-11-28 18:45:25.563153
---

# bn.onDeviceOrientationChange

▸ **onDeviceOrientationChange**(`cb`): `void`

**`description`** Listens on the landscape/portrait mode switchover event.

**`example`**

```ts
bn.onDeviceOrientationChange(callback);
```

Parameters

| Name | Type                                |
| :--- | :---------------------------------- |
| `cb` | `OnDeviceOrientationChangeCallback` |

Returns

`void`

---

## OnDeviceOrientationChangeCallback

Ƭ **OnDeviceOrientationChangeCallback**: (`result`: `OnDeviceOrientationChangeCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

The callback function for the landscape/portrait mode switchover event

Parameters

| Name     | Type                                      |
| :------- | :---------------------------------------- |
| `result` | `OnDeviceOrientationChangeCallbackResult` |

Returns

`void`

---

## Interface: OnDeviceOrientationChangeCallbackResult

| Name  | Type               | Description                                                    |
| :---- | :----------------- | :------------------------------------------------------------- |
| value | `OrientationValue` | Indicates whether the screen is in landscape or portrait mode. |

---

# bn.onDeviceOrientationChange

▸ **onDeviceOrientationChange**(`cb`): `void`

**`description`** Listens on the landscape/portrait mode switchover event.

**`example`**

```ts
bn.onDeviceOrientationChange(callback);
```

Parameters

| Name | Type                                |
| :--- | :---------------------------------- |
| `cb` | `OnDeviceOrientationChangeCallback` |

Returns

`void`

---

## OnDeviceOrientationChangeCallback

Ƭ **OnDeviceOrientationChangeCallback**: (`result`: `OnDeviceOrientationChangeCallbackResult`) =>
`void`

Type declaration

▸ (`result`): `void`

The callback function for the landscape/portrait mode switchover event

Parameters

| Name     | Type                                      |
| :------- | :---------------------------------------- |
| `result` | `OnDeviceOrientationChangeCallbackResult` |

Returns

`void`

---

## Interface: OnDeviceOrientationChangeCallbackResult

| Name  | Type               | Description                                                    |
| :---- | :----------------- | :------------------------------------------------------------- |
| value | `OrientationValue` | Indicates whether the screen is in landscape or portrait mode. |