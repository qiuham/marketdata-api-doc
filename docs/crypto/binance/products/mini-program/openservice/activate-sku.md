---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/activate-sku
api_type: Guide
updated_at: 2026-11-28 18:36:29.021648
---

# ActivateSKU

# <a name="activateSKU"></a>ActivateSKU

Activates or deactivates a SKU by setting its availability status. This applies to both the auditing
and approved records of the SKU simultaneously.

**Host**: **dip-cb.binanceapi.com**

**PUT** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}/activate

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Body Parameters**

| **Parameter** | **Type** | **Required** | **Description**                       | **Example** |
| :------------ | :------- | :----------- | :------------------------------------ | :---------- |
| status        | boolean  | Yes          | True to activate; false to deactivate | true        |

**Request Body**

```json
​{
  "status": true
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {},
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900260    | Invalid SkuId             |

Note:

1. Activating or deactivating a SKU updates both the auditing and approved records for that SKU.

---

# ActivateSKU

# <a name="activateSKU"></a>ActivateSKU

Activates or deactivates a SKU by setting its availability status. This applies to both the auditing
and approved records of the SKU simultaneously.

**Host**: **dip-cb.binanceapi.com**

**PUT** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}/activate

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Body Parameters**

| **Parameter** | **Type** | **Required** | **Description**                       | **Example** |
| :------------ | :------- | :----------- | :------------------------------------ | :---------- |
| status        | boolean  | Yes          | True to activate; false to deactivate | true        |

**Request Body**

```json
​{
  "status": true
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {},
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900260    | Invalid SkuId             |

Note:

1. Activating or deactivating a SKU updates both the auditing and approved records for that SKU.