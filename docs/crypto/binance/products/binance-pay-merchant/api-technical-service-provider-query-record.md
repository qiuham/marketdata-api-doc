---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-technical-service-provider-query-record
api_type: Guide
updated_at: 2026-11-28 18:33:14.047234
---

# Query Authentication Record

API used to query and view all the authentication records. <br/> \*This API is only available for
Technical Service Provider (TSP), for more information please contact us at: merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/service/provider/record
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**    | **Description** |
| -------------- | -------- | ------------ | ----------------- | --------------- |
| **page**       | int      | Y            | maximum length 32 | page            |
| **rows**       | int      | Y            | max 10            | rows            |
| **merchantId** | string   | N            |                   | merchant id     |

### Sample Request Body

```json
{
  "page": 1,
  "rows": 10
}
```

## Response Parameters

| **Attributes**   | **Type**   | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string     | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string     | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | DataObject | N            | -                                   | response body, [refer to](#DataObject)         |
| **errorMessage** | string     | N            | maximum length 256                  |                                                |

## Child Attribute

### DataObject

<span id="config-response"></span>

| **Attributes** | **Type**           | **Required** | **Limitation** | **Description**                               |
| -------------- | ------------------ | ------------ | -------------- | --------------------------------------------- |
| **total**      | long               | Y            |                | total record number                           |
| **rows**       | List[RecordObject] | Y            |                | record object list, [refer to](#RecordObject) |

### RecordObject

<span id="config-response"></span>

| **Attributes**         | **Type** | **Required** | **Limitation** | **Description**     |
| ---------------------- | -------- | ------------ | -------------- | ------------------- |
| **authorizationId**    | String   | Y            |                | Authorization ID    |
| **merchantName**       | String   | Y            |                | Merchant's Name     |
| **authorizationToken** | String   | Y            |                | Authorization Token |
| **merchantId**         | String   | Y            |                | Merchant's ID       |
| **status**             | String   | Y            |                | Status              |
| **scopes**             | List     | Y            |                | Scopes              |
| **ipWhitelist**        | List     | Y            |                | IP Whitelist        |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "total": 2,
    "rows": [
      {
        "authorizationId": "authId1",
        "merchantName": "Merchant One",
        "authorizationToken": "token1",
        "merchantId": "merchant1",
        "status": "PENDING",
        "scopes": ["CONVERT", "CHECKOUT"],
        "ipWhitelist": ["192.168.1.1", "192.168.1.2"]
      },
      {
        "authorizationId": "authId2",
        "merchantName": "Merchant Two",
        "authorizationToken": "token2",
        "merchantId": "merchant2",
        "status": "AUTHORIZED",
        "scopes": ["CONVERT", "CHECKOUT"],
        "ipWhitelist": ["192.168.2.1", "192.168.2.2"]
      }
    ]
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400003",
  "errorMessage": "Timestamp for this request is outside of the recvWindow."
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |

---

# Query Authentication Record

API used to query and view all the authentication records. <br/> \*This API is only available for
Technical Service Provider (TSP), for more information please contact us at: merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/service/provider/record
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**    | **Description** |
| -------------- | -------- | ------------ | ----------------- | --------------- |
| **page**       | int      | Y            | maximum length 32 | page            |
| **rows**       | int      | Y            | max 10            | rows            |
| **merchantId** | string   | N            |                   | merchant id     |

### Sample Request Body

```json
{
  "page": 1,
  "rows": 10
}
```

## Response Parameters

| **Attributes**   | **Type**   | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string     | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string     | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | DataObject | N            | -                                   | response body, [refer to](#DataObject)         |
| **errorMessage** | string     | N            | maximum length 256                  |                                                |

## Child Attribute

### DataObject

<span id="config-response"></span>

| **Attributes** | **Type**           | **Required** | **Limitation** | **Description**                               |
| -------------- | ------------------ | ------------ | -------------- | --------------------------------------------- |
| **total**      | long               | Y            |                | total record number                           |
| **rows**       | List[RecordObject] | Y            |                | record object list, [refer to](#RecordObject) |

### RecordObject

<span id="config-response"></span>

| **Attributes**         | **Type** | **Required** | **Limitation** | **Description**     |
| ---------------------- | -------- | ------------ | -------------- | ------------------- |
| **authorizationId**    | String   | Y            |                | Authorization ID    |
| **merchantName**       | String   | Y            |                | Merchant's Name     |
| **authorizationToken** | String   | Y            |                | Authorization Token |
| **merchantId**         | String   | Y            |                | Merchant's ID       |
| **status**             | String   | Y            |                | Status              |
| **scopes**             | List     | Y            |                | Scopes              |
| **ipWhitelist**        | List     | Y            |                | IP Whitelist        |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "total": 2,
    "rows": [
      {
        "authorizationId": "authId1",
        "merchantName": "Merchant One",
        "authorizationToken": "token1",
        "merchantId": "merchant1",
        "status": "PENDING",
        "scopes": ["CONVERT", "CHECKOUT"],
        "ipWhitelist": ["192.168.1.1", "192.168.1.2"]
      },
      {
        "authorizationId": "authId2",
        "merchantName": "Merchant Two",
        "authorizationToken": "token2",
        "merchantId": "merchant2",
        "status": "AUTHORIZED",
        "scopes": ["CONVERT", "CHECKOUT"],
        "ipWhitelist": ["192.168.2.1", "192.168.2.2"]
      }
    ]
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400003",
  "errorMessage": "Timestamp for this request is outside of the recvWindow."
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |