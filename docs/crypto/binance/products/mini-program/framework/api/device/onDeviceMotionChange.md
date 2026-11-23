---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onDeviceMotionChange
api_type: Guide
updated_at: 2026-11-23 18:47:48.671248
---

# bn.onDeviceMotionChange

▸ **onDeviceMotionChange**(`cb`): `void`

**`description`** Listen for device direction change events. Frequency basis
bn.startDeviceMotionListening() of interval Parameters. Can be used bn.stopDeviceMotionListening()
Stop listening.

**`example`**

```ts
bn.onDeviceMotionChange(callback);
```

Parameters

| Name | Type                           |
| :--- | :----------------------------- |
| `cb` | `OnDeviceMotionChangeCallback` |

Returns

`void`

---

## OnDeviceMotionChangeCallback

Ƭ **OnDeviceMotionChangeCallback**: (`result`: `OnDeviceMotionChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function for device orientation change event

Parameters

| Name     | Type                                 |
| :------- | :----------------------------------- |
| `result` | `OnDeviceMotionChangeCallbackResult` |

Returns

`void`

---

## Interface: OnDeviceMotionChangeCallbackResult

| Name  | Type     | Description                                                                                                                                                                                                                                                 |
| :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alpha | `number` | When Cell phone coordinates X and Earth X/And When overlapped, around. With the angle at which the axis rotates is Alpha, with a range value of [0, 2\*PI). Turning counterclockwise is positive.                                                           |
| beta  | `number` | When the phone coordinate Y/Z coincides with the earth Y/Z, around X The angle at which the axis rotates is beta。 Range values are [-1PI, PI) The top is turned positive towards the Earth's surface. It is also possible to be positive towards the user. |
| gamma | `number` | When the X/Z of the mobile phone coincides with the X/Z of the earth, the included angle of rotation around the Y axis is gamma. Range values are [-1\*PI/2, PI/2). Turning right towards the Earth's surface is positive.                                  |

---

# bn.onDeviceMotionChange

▸ **onDeviceMotionChange**(`cb`): `void`

**`description`** Listen for device direction change events. Frequency basis
bn.startDeviceMotionListening() of interval Parameters. Can be used bn.stopDeviceMotionListening()
Stop listening.

**`example`**

```ts
bn.onDeviceMotionChange(callback);
```

Parameters

| Name | Type                           |
| :--- | :----------------------------- |
| `cb` | `OnDeviceMotionChangeCallback` |

Returns

`void`

---

## OnDeviceMotionChangeCallback

Ƭ **OnDeviceMotionChangeCallback**: (`result`: `OnDeviceMotionChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Callback function for device orientation change event

Parameters

| Name     | Type                                 |
| :------- | :----------------------------------- |
| `result` | `OnDeviceMotionChangeCallbackResult` |

Returns

`void`

---

## Interface: OnDeviceMotionChangeCallbackResult

| Name  | Type     | Description                                                                                                                                                                                                                                                 |
| :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alpha | `number` | When Cell phone coordinates X and Earth X/And When overlapped, around. With the angle at which the axis rotates is Alpha, with a range value of [0, 2\*PI). Turning counterclockwise is positive.                                                           |
| beta  | `number` | When the phone coordinate Y/Z coincides with the earth Y/Z, around X The angle at which the axis rotates is beta。 Range values are [-1PI, PI) The top is turned positive towards the Earth's surface. It is also possible to be positive towards the user. |
| gamma | `number` | When the X/Z of the mobile phone coincides with the X/Z of the earth, the included angle of rotation around the Y axis is gamma. Range values are [-1\*PI/2, PI/2). Turning right towards the Earth's surface is positive.                                  |