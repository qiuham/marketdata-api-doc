---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/location/getLocation
api_type: Guide
updated_at: 2026-11-19 18:48:20.330120
---

# bn.getLocation

▸ **getLocation**(`options`): `Promise`<`LocationDetail`\>

**`description`** Gets the current location and speed

Parameters

| Name      | Type                 | Description          |
| :-------- | :------------------- | :------------------- |
| `options` | `GetLocationOptions` | Get location options |

Returns

`Promise`<`LocationDetail`\>

Location information

---

## GetLocationOptions

Ƭ **GetLocationOptions**: `Object`

Type declaration

| Name        | Type      | Description                                                                                                                     |
| :---------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `type?`     | `string`  | Coordinates type: 'gcj02'; 'wgs84'                                                                                              |
| `altitude?` | `boolean` | Set `true` to return altitude. This option may slow down the interface due to the high precision is required to obtain altitude |

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

# bn.getLocation

▸ **getLocation**(`options`): `Promise`<`LocationDetail`\>

**`description`** Gets the current location and speed

Parameters

| Name      | Type                 | Description          |
| :-------- | :------------------- | :------------------- |
| `options` | `GetLocationOptions` | Get location options |

Returns

`Promise`<`LocationDetail`\>

Location information

---

## GetLocationOptions

Ƭ **GetLocationOptions**: `Object`

Type declaration

| Name        | Type      | Description                                                                                                                     |
| :---------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `type?`     | `string`  | Coordinates type: 'gcj02'; 'wgs84'                                                                                              |
| `altitude?` | `boolean` | Set `true` to return altitude. This option may slow down the interface due to the high precision is required to obtain altitude |

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