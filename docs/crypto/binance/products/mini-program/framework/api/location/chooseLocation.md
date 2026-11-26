---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/location/chooseLocation
api_type: Guide
updated_at: 2026-11-26 18:46:13.103537
---

# bn.chooseLocation

▸ **chooseLocation**(`options`): `Promise`<`ChooseLocationResponse`\>

**`description`** Open the map and select the location

**`example`**

```js
// To get the user's location by api In the mini program, the developer needs to firstly request the user for the authorization.
bn.authorize({ scope: "scope.userLocation" })
  .then((res) => console.log(`[authorize] SUCCESS:`, res))
  .catch((err) => console.log(`[authorize] ERROR:`, err));

bn.getLocation({ type: "wgs84", altitude: false })
  .then((res) =>
    bn.showModal({
      title: "getLocation",
      content: "success" + JSON.stringify(res),
    }),
  )
  .catch((error) =>
    bn.showModal({
      title: "getLocation",
      content: "fail" + JSON.stringify(error),
    }),
  );

// Please note: the user may disable the location permissions in the open settings of the mini program. The developer can use getSetting api to have a check.
const res = await bn.getSetting();
console.log(res.authSetting["scope.userLocation"]); // boolean
// and also, the developer can open the permission panel for user to enable the setting
await bn.openSetting();
```

Parameters

| Name      | Type                    | Description             |
| :-------- | :---------------------- | :---------------------- |
| `options` | `ChooseLocationOptions` | Choose location options |

Returns

`Promise`<`ChooseLocationResponse`\>

Location information

## ChooseLocationOptions

Ƭ **ChooseLocationOptions**: `Object`

Type declaration

| Name         | Type     | Description      |
| :----------- | :------- | :--------------- |
| `latitude?`  | `number` | Target latitude  |
| `longitude?` | `number` | Target longitude |

## ChooseLocationResponse

Ƭ **ChooseLocationResponse**: `Object`

Type declaration

| Name        | Type     | Description                                                                                                 |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| `latitude`  | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| `longitude` | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| `name`      | `string` | Location name                                                                                               |
| `address`   | `string` | Detailed address                                                                                            |

---

---

# bn.chooseLocation

▸ **chooseLocation**(`options`): `Promise`<`ChooseLocationResponse`\>

**`description`** Open the map and select the location

**`example`**

```js
// To get the user's location by api In the mini program, the developer needs to firstly request the user for the authorization.
bn.authorize({ scope: "scope.userLocation" })
  .then((res) => console.log(`[authorize] SUCCESS:`, res))
  .catch((err) => console.log(`[authorize] ERROR:`, err));

bn.getLocation({ type: "wgs84", altitude: false })
  .then((res) =>
    bn.showModal({
      title: "getLocation",
      content: "success" + JSON.stringify(res),
    }),
  )
  .catch((error) =>
    bn.showModal({
      title: "getLocation",
      content: "fail" + JSON.stringify(error),
    }),
  );

// Please note: the user may disable the location permissions in the open settings of the mini program. The developer can use getSetting api to have a check.
const res = await bn.getSetting();
console.log(res.authSetting["scope.userLocation"]); // boolean
// and also, the developer can open the permission panel for user to enable the setting
await bn.openSetting();
```

Parameters

| Name      | Type                    | Description             |
| :-------- | :---------------------- | :---------------------- |
| `options` | `ChooseLocationOptions` | Choose location options |

Returns

`Promise`<`ChooseLocationResponse`\>

Location information

## ChooseLocationOptions

Ƭ **ChooseLocationOptions**: `Object`

Type declaration

| Name         | Type     | Description      |
| :----------- | :------- | :--------------- |
| `latitude?`  | `number` | Target latitude  |
| `longitude?` | `number` | Target longitude |

## ChooseLocationResponse

Ƭ **ChooseLocationResponse**: `Object`

Type declaration

| Name        | Type     | Description                                                                                                 |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| `latitude`  | `number` | Latitude, range -90 ~ 90. The negative number indicates latitude south. use gcj02 NBS coordinate system     |
| `longitude` | `number` | Longitude, range -180 ~ 180. The negative numbers indicates west longitude. use gcj02 NBS coordinate system |
| `name`      | `string` | Location name                                                                                               |
| `address`   | `string` | Detailed address                                                                                            |

---