---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onNetworkStatusChange
api_type: Guide
updated_at: 2026-11-26 18:48:00.805512
---

# bn.onNetworkStatusChange

▸ **onNetworkStatusChange**(`cb`): `void`

Listens on the network status change event.

Parameters

| Name | Type                            | Description                                                |
| :--- | :------------------------------ | :--------------------------------------------------------- |
| `cb` | `OnNetworkStatusChangeCallback` | The callback function for the network status change event. |

Returns

`void`

---

## OnNetworkStatusChangeCallback

Ƭ **OnNetworkStatusChangeCallback**: (`result`: `OnNetworkStatusChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `result` | `OnNetworkStatusChangeCallbackResult` |

Returns

`void`

---

## Interface: OnNetworkStatusChangeCallbackResult

| Name        | Type          | Description                                      |
| :---------- | :------------ | :----------------------------------------------- |
| isConnected | `boolean`     | Indicates whether it is connected to the network |
| networkType | `NetworkType` | Network type                                     |

---

# bn.onNetworkStatusChange

▸ **onNetworkStatusChange**(`cb`): `void`

Listens on the network status change event.

Parameters

| Name | Type                            | Description                                                |
| :--- | :------------------------------ | :--------------------------------------------------------- |
| `cb` | `OnNetworkStatusChangeCallback` | The callback function for the network status change event. |

Returns

`void`

---

## OnNetworkStatusChangeCallback

Ƭ **OnNetworkStatusChangeCallback**: (`result`: `OnNetworkStatusChangeCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                                  |
| :------- | :------------------------------------ |
| `result` | `OnNetworkStatusChangeCallbackResult` |

Returns

`void`

---

## Interface: OnNetworkStatusChangeCallbackResult

| Name        | Type          | Description                                      |
| :---------- | :------------ | :----------------------------------------------- |
| isConnected | `boolean`     | Indicates whether it is connected to the network |
| networkType | `NetworkType` | Network type                                     |