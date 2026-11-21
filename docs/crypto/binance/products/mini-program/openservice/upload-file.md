---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/upload-file
api_type: Guide
updated_at: 2026-11-21 18:36:44.118374
---

# UploadFile

# <a name="uploadfile"></a>UploadFile

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/files/upload

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Body**

Utilize FORM (multipart/form-data) for submissions. You can refer to the following articles for
further understanding:

- [About HTTP multipart/form-data](https://www.sobyte.net/post/2021-12/learn-about-http-multipart-form-data)
- [Using multipart in curl](https://curl.se/docs/manpage.html) (see the `-F, --form` option)

Like other requests, employ the full body for the signature.

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |

Note:

1. There is a total upload count limit for each app. Please contact us if you encounter a limit
   error.
2. Currently, we only support uploading a single file at a time.
3. This API executes asynchronously. We will conduct a security check on the uploaded file. Use the
   returned `fileId` with [GetFileStatus](/products/mini-program/openservice/get-file-status) to
   verify whether the uploaded file has passed the check.
4. The currently acceptable file content is in image format, conforming to the following rules:
   - Format: jpg or png
   - Size: Maximum 1MB
   - File name size: Maximum 60 characters (including extension)
5. We recommend an image size ratio of:
   - Width: 516
   - Height: 375

   For sku images, if an image does not match this ratio, it will be cropped by our system when
   displayed.

**Response**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "fileIds": ["f7574adb-0ccb-4281-9ed6-943f11a1e85a"]
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

---

# UploadFile

# <a name="uploadfile"></a>UploadFile

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/files/upload

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Body**

Utilize FORM (multipart/form-data) for submissions. You can refer to the following articles for
further understanding:

- [About HTTP multipart/form-data](https://www.sobyte.net/post/2021-12/learn-about-http-multipart-form-data)
- [Using multipart in curl](https://curl.se/docs/manpage.html) (see the `-F, --form` option)

Like other requests, employ the full body for the signature.

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |

Note:

1. There is a total upload count limit for each app. Please contact us if you encounter a limit
   error.
2. Currently, we only support uploading a single file at a time.
3. This API executes asynchronously. We will conduct a security check on the uploaded file. Use the
   returned `fileId` with [GetFileStatus](/products/mini-program/openservice/get-file-status) to
   verify whether the uploaded file has passed the check.
4. The currently acceptable file content is in image format, conforming to the following rules:
   - Format: jpg or png
   - Size: Maximum 1MB
   - File name size: Maximum 60 characters (including extension)
5. We recommend an image size ratio of:
   - Width: 516
   - Height: 375

   For sku images, if an image does not match this ratio, it will be cropped by our system when
   displayed.

**Response**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "fileIds": ["f7574adb-0ccb-4281-9ed6-943f11a1e85a"]
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