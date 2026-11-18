---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/get-file-status
api_type: Guide
updated_at: 2026-11-18 18:36:37.563941
---

# GetFileStatus

# <a name="getFileStatus"></a>GetFileStatus

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/files/\{fileId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                                        |
| :------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. For generation method, please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**                                                                             |
| :------------ | :------------------------------------------------------------------------------------------ |
| appId         | The AppId of the mini program                                                               |
| fileId        | The fileId returned by the [UploadFile](/products/mini-program/openservice/upload-file) API |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "status": "FAILED"
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
| 900231    | Rate Limit                |

Note:

1. The `status` could be either: "CHECKING", "SUCCESS", or "FAILED".
2. If the `status` is "FAILED", ensure your file is both secure and valid before re-uploading.
3. The complete file security check process takes a maximum of 10 minutes post-upload. Therefore,
   the status gets finalized after 10 minutes of upload.

---

# GetFileStatus

# <a name="getFileStatus"></a>GetFileStatus

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/files/\{fileId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                                        |
| :------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. For generation method, please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**                                                                             |
| :------------ | :------------------------------------------------------------------------------------------ |
| appId         | The AppId of the mini program                                                               |
| fileId        | The fileId returned by the [UploadFile](/products/mini-program/openservice/upload-file) API |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "status": "FAILED"
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
| 900231    | Rate Limit                |

Note:

1. The `status` could be either: "CHECKING", "SUCCESS", or "FAILED".
2. If the `status` is "FAILED", ensure your file is both secure and valid before re-uploading.
3. The complete file security check process takes a maximum of 10 minutes post-upload. Therefore,
   the status gets finalized after 10 minutes of upload.