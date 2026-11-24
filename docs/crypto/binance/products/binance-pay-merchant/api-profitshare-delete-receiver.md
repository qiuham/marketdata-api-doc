---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-profitshare-delete-receiver
api_type: Guide
updated_at: 2026-11-24 18:34:24.849220
---

# Delete Receiver

API used to delete receiver.

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/del-receiver
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                       |
| -------------- | -------- | ------------ | -------------- | ------------------------------------- |
| **account**    | string   | Y            |                | Binance ID of receiver to be deleted. |

### Sample Request Parameter

```json
{
  "account": "123456789"
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Response | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

## Child Attribute

### Response

<span id="quote-response"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                |
| -------------- | -------- | ------------ | -------------- | ------------------------------ |
| **account**    | string   | Y            |                | Account from the request body. |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "account": "123456789"
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400000",
  "errorMessage": "An unknown error occurred while processing the request."
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
| PAYMENT_ACCOUNT_NOT_FOUND          | 400601   | Account not found                                                              |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |

---

# Delete Receiver

API used to delete receiver.

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/del-receiver
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                       |
| -------------- | -------- | ------------ | -------------- | ------------------------------------- |
| **account**    | string   | Y            |                | Binance ID of receiver to be deleted. |

### Sample Request Parameter

```json
{
  "account": "123456789"
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Response | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

## Child Attribute

### Response

<span id="quote-response"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                |
| -------------- | -------- | ------------ | -------------- | ------------------------------ |
| **account**    | string   | Y            |                | Account from the request body. |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "account": "123456789"
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400000",
  "errorMessage": "An unknown error occurred while processing the request."
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
| PAYMENT_ACCOUNT_NOT_FOUND          | 400601   | Account not found                                                              |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |