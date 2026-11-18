---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/get-user-pay-id
api_type: Guide
updated_at: 2026-11-18 18:36:32.962851
---

# GetUserPayId

# <a name="_cqdutfa2s32u"></a>GetUserPayId

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/users?openId=query_open_id

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**                                         |
| :------------ | :------------------------------------------------------ |
| appId         | The AppId of the mini program **(required)**            |
| openId        | The openId of the user you wish to query **(required)** |

Note:

1. Please make sure to call this API by attaching a JWT token in the header under
   `X-Mp-Open-Api-Token`. For the method of generating JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature)

**Request Example**

```
​{
  "appId": "insert-your-app-id-from-workspace",
  "openId": "insert-user’s-openId-for-query",
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "payId": 26238454
  },
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |

---

# GetUserPayId

# <a name="_cqdutfa2s32u"></a>GetUserPayId

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/users?openId=query_open_id

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**                                         |
| :------------ | :------------------------------------------------------ |
| appId         | The AppId of the mini program **(required)**            |
| openId        | The openId of the user you wish to query **(required)** |

Note:

1. Please make sure to call this API by attaching a JWT token in the header under
   `X-Mp-Open-Api-Token`. For the method of generating JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature)

**Request Example**

```
​{
  "appId": "insert-your-app-id-from-workspace",
  "openId": "insert-user’s-openId-for-query",
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "payId": 26238454
  },
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |