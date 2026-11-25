---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onGyroscopeChange
api_type: Guide
updated_at: 2026-11-25 18:47:31.738236
---

# bn.onGyroscopeChange

▸ **onGyroscopeChange**(`cb`): `void`

**`description`** Monitor gyro data change events. Frequency basis bn.startGyroscope() of interval
Parameters. Can be used bn.stopGyroscope() Stop listening.

**`example`**

```ts
bn.onGyroscopeChange(callback);
```

Parameters

| Name | Type                        |
| :--- | :-------------------------- |
| `cb` | `OnGyroscopeChangeCallback` |

Returns

`void`

---

## OnGyroscopeChangeCallback

Ƭ **OnGyroscopeChangeCallback**: (`result`: `OnGyroscopeChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

A callback function for gyro data change events

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnGyroscopeChangeCallbackResult` |

Returns

`void`

---

## Interface: OnGyroscopeChangeCallbackResult

| Name | Type     | Description                 |
| :--- | :------- | :-------------------------- |
| x    | `number` | x Angular velocity of shaft |
| y    | `number` | y Angular velocity of shaft |
| z    | `number` | z Angular velocity of shaft |

---

# bn.onGyroscopeChange

▸ **onGyroscopeChange**(`cb`): `void`

**`description`** Monitor gyro data change events. Frequency basis bn.startGyroscope() of interval
Parameters. Can be used bn.stopGyroscope() Stop listening.

**`example`**

```ts
bn.onGyroscopeChange(callback);
```

Parameters

| Name | Type                        |
| :--- | :-------------------------- |
| `cb` | `OnGyroscopeChangeCallback` |

Returns

`void`

---

## OnGyroscopeChangeCallback

Ƭ **OnGyroscopeChangeCallback**: (`result`: `OnGyroscopeChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

A callback function for gyro data change events

Parameters

| Name     | Type                              |
| :------- | :-------------------------------- |
| `result` | `OnGyroscopeChangeCallbackResult` |

Returns

`void`

---

## Interface: OnGyroscopeChangeCallbackResult

| Name | Type     | Description                 |
| :--- | :------- | :-------------------------- |
| x    | `number` | x Angular velocity of shaft |
| y    | `number` | y Angular velocity of shaft |
| z    | `number` | z Angular velocity of shaft |