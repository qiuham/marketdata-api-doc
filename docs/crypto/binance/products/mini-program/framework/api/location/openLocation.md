---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/location/openLocation
api_type: Guide
updated_at: 2026-11-18 18:45:04.734780
---

# bn.openLocation

▸ **openLocation**(`options`): `Promise`<{}\>

**`description`** Check location in map

Parameters

| Name      | Type                  | Description           |
| :-------- | :-------------------- | :-------------------- |
| `options` | `OpenLocationOptions` | Open location options |

Returns

`Promise`<{}\>

---

## OpenLocationOptions

Ƭ **OpenLocationOptions**: `Object`

Type declaration

| Name        | Type     | Description                                                                                                 |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| `latitude`  | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| `longitude` | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| `scale?`    | `number` | Scale, Range 5 ~ 18                                                                                         |
| `name?`     | `string` | Location name                                                                                               |
| `address?`  | `string` | A detailed explaination of the address                                                                      |

---

---

# bn.openLocation

▸ **openLocation**(`options`): `Promise`<{}\>

**`description`** Check location in map

Parameters

| Name      | Type                  | Description           |
| :-------- | :-------------------- | :-------------------- |
| `options` | `OpenLocationOptions` | Open location options |

Returns

`Promise`<{}\>

---

## OpenLocationOptions

Ƭ **OpenLocationOptions**: `Object`

Type declaration

| Name        | Type     | Description                                                                                                 |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| `latitude`  | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| `longitude` | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| `scale?`    | `number` | Scale, Range 5 ~ 18                                                                                         |
| `name?`     | `string` | Location name                                                                                               |
| `address?`  | `string` | A detailed explaination of the address                                                                      |

---