---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-convert-get-to-selector
api_type: Guide
updated_at: 2026-11-20 18:36:11.391943
---

# List All Convert Pairs

API used to list all convert pairs.

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/get-to-selector
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                       | **Description**                  |
| -------------- | -------- | ------------ | ------------------------------------ | -------------------------------- |
| **fromAsset**  | string   | Y            | Valid currency, must be in uppercase | Currency to query, for e.g, USDT |

### Sample Request Parameter

```json
{
    "fromAsset": USDT
}
```

## Response Parameters

| **Attributes**   | **Type**        | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | --------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string          | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string          | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | ConvertPairResp | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string          | N            | maximum length 256                  |                                                |

## Child Attribute

### ConvertPairResp

<span id="quote-response"></span>

| **Attributes** | **Type**        | **Required** | **Limitation** | **Description**                                |
| -------------- | --------------- | ------------ | -------------- | ---------------------------------------------- |
| **toList**     | ConvertPairData | Y            |                | Convert data, [refer to](#quote-response-data) |
| **coin**       | string          | Y            |                | Currency from the request parameter            |

### ConvertPairData

<span id="quote-response-data"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**           |
| -------------- | -------- | ------------ | -------------- | ------------------------- |
| **coin**       | string   | Y            |                | To asset                  |
| **fromMin**    | decimal  | Y            |                | From asset minimum amount |
| **fromMax**    | decimal  | Y            |                | From asset maximum amount |
| **toMin**      | decimal  | Y            |                | To asset minimum amount   |
| **toMax**      | decimal  | Y            |                | To asset maximum amount   |
| **reverse**    | boolean  | Y            |                | Reverse convert available |
| **base**       | boolean  | Y            |                | Is base                   |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "coin": "USDT",
    "toList": [
      {
        "coin": "BTC",
        "fromMin": 2e1,
        "fromMax": 7e5,
        "toMin": 0.0008,
        "toMax": 35.1,
        "reverse": true,
        "base": true
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

# List All Convert Pairs

API used to list all convert pairs.

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/get-to-selector
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                       | **Description**                  |
| -------------- | -------- | ------------ | ------------------------------------ | -------------------------------- |
| **fromAsset**  | string   | Y            | Valid currency, must be in uppercase | Currency to query, for e.g, USDT |

### Sample Request Parameter

```json
{
    "fromAsset": USDT
}
```

## Response Parameters

| **Attributes**   | **Type**        | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | --------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string          | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string          | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | ConvertPairResp | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string          | N            | maximum length 256                  |                                                |

## Child Attribute

### ConvertPairResp

<span id="quote-response"></span>

| **Attributes** | **Type**        | **Required** | **Limitation** | **Description**                                |
| -------------- | --------------- | ------------ | -------------- | ---------------------------------------------- |
| **toList**     | ConvertPairData | Y            |                | Convert data, [refer to](#quote-response-data) |
| **coin**       | string          | Y            |                | Currency from the request parameter            |

### ConvertPairData

<span id="quote-response-data"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**           |
| -------------- | -------- | ------------ | -------------- | ------------------------- |
| **coin**       | string   | Y            |                | To asset                  |
| **fromMin**    | decimal  | Y            |                | From asset minimum amount |
| **fromMax**    | decimal  | Y            |                | From asset maximum amount |
| **toMin**      | decimal  | Y            |                | To asset minimum amount   |
| **toMax**      | decimal  | Y            |                | To asset maximum amount   |
| **reverse**    | boolean  | Y            |                | Reverse convert available |
| **base**       | boolean  | Y            |                | Is base                   |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "coin": "USDT",
    "toList": [
      {
        "coin": "BTC",
        "fromMin": 2e1,
        "fromMax": 7e5,
        "toMin": 0.0008,
        "toMax": 35.1,
        "reverse": true,
        "base": true
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