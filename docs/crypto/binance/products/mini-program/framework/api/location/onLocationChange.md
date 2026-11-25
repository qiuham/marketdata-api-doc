---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/location/onLocationChange
api_type: Guide
updated_at: 2026-11-25 18:46:03.121056
---

# bn.onLocationChange

▸ **onLocationChange**(`cb`): `void`

**`description`** Subscribe the event of real-time location changes，used with
`bn.startLocationUpdate`

Parameters

| Name | Type                       | Description       |
| :--- | :------------------------- | :---------------- |
| `cb` | `OnLocationChangeCallback` | callback function |

Returns

`void`

---

## OnLocationChangeCallback

Ƭ **OnLocationChangeCallback**: (`result`: `LocationDetail`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type             |
| :------- | :--------------- |
| `result` | `LocationDetail` |

Returns

`void`

---

## Interface: LocationDetail

| Name               | Type     | Description                                                                                                 |
| :----------------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| accuracy           | `number` | Accuracy of position                                                                                        |
| altitude           | `number` | Height, unit m                                                                                              |
| horizontalAccuracy | `number` | Horizontal precision, unit m                                                                                |
| latitude           | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| longitude          | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| speed              | `number` | Speed, unit m/s                                                                                             |
| verticalAccuracy   | `number` | Vertical accuracy, unit m（return 0 when unable to get)                                                     |

---

# bn.onLocationChange

▸ **onLocationChange**(`cb`): `void`

**`description`** Subscribe the event of real-time location changes，used with
`bn.startLocationUpdate`

Parameters

| Name | Type                       | Description       |
| :--- | :------------------------- | :---------------- |
| `cb` | `OnLocationChangeCallback` | callback function |

Returns

`void`

---

## OnLocationChangeCallback

Ƭ **OnLocationChangeCallback**: (`result`: `LocationDetail`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type             |
| :------- | :--------------- |
| `result` | `LocationDetail` |

Returns

`void`

---

## Interface: LocationDetail

| Name               | Type     | Description                                                                                                 |
| :----------------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| accuracy           | `number` | Accuracy of position                                                                                        |
| altitude           | `number` | Height, unit m                                                                                              |
| horizontalAccuracy | `number` | Horizontal precision, unit m                                                                                |
| latitude           | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| longitude          | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| speed              | `number` | Speed, unit m/s                                                                                             |
| verticalAccuracy   | `number` | Vertical accuracy, unit m（return 0 when unable to get)                                                     |