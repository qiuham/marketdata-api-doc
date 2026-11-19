---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-convert-execute-quote
api_type: Guide
updated_at: 2026-11-19 18:36:33.877382
---

# Execute Quote

API used to execute convert quote.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/execute-quote
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**            |
| -------------- | -------- | ------------ | -------------- | -------------------------- |
| **quoteId**    | string   | Y            |                | Quote ID for execute quote |

### Sample Request Body

```json
{
  "quoteId": "e53bb5ea9a384277b4ed971235816a9f"
}
```

## Response Parameters

| **Attributes**   | **Type**        | **Required** | **Limitation**                      | **Description**                                   |
| ---------------- | --------------- | ------------ | ----------------------------------- | ------------------------------------------------- |
| **status**       | string          | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                         |
| **code**         | string          | Y            | -                                   | request result code, [refer to ](#result-code)    |
| **data**         | AcceptQuoteResp | N            | -                                   | response body, [refer to](#accept-quote-response) |
| **errorMessage** | string          | N            | maximum length 256                  |                                                   |

## Child Attribute

### AcceptQuoteResp

<span id="accept-quote-response"></span>

| **Attributes**     | **Type** | **Required** | **Limitation**       | **Description**                         |
| ------------------ | -------- | ------------ | -------------------- | --------------------------------------- |
| **orderId**        | string   | Y            |                      | Order ID of the executed convert order. |
| **createTime**     | decimal  | Y            |                      | Timestamp order created                 |
| **orderStatus**    | string   | Y            | SUCCESS/FAIL/PROCESS | Order status                            |
| **quotePrice**     | decimal  | Y            |                      | `From:To` quote price                   |
| **inversePrice**   | decimal  | Y            |                      | `To:From` quote price                   |
| **fromCoin**       | string   | Y            |                      | From Asset                              |
| **fromCoinAmount** | decimal  | Y            |                      | Amount debited                          |
| **toCoin**         | string   | Y            |                      | To Asset                                |
| **toCoinAmount**   | decimal  | Y            |                      | Amount credited                         |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "orderId": "1309477640981204290",
    "createTime": 1667179261865,
    "orderStatus": "PROCESS",
    "quotePrice": 0.00445577,
    "inversePrice": 224.428,
    "fromCoin": "USDT",
    "fromCoinAmount": 179.54201695,
    "toCoin": "BNB",
    "toCoinAmount": 0.8
  }
}
```

```json
{
  "status": "FAIL",
  "code": "345231",
  "errorMessage": "System failed to execute the quote, which has expired. Please request for quote again."
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                            | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| TIME_OUT                           | 345231   | System failed to execute the quote, which has expired. Please request for quote again |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                               | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.         | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                            | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                             | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                                | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                                      | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                         | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                             | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                              | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                                     |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.        |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                                 |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                                |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                             |                                                                                                |

---

# Execute Quote

API used to execute convert quote.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/execute-quote
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**            |
| -------------- | -------- | ------------ | -------------- | -------------------------- |
| **quoteId**    | string   | Y            |                | Quote ID for execute quote |

### Sample Request Body

```json
{
  "quoteId": "e53bb5ea9a384277b4ed971235816a9f"
}
```

## Response Parameters

| **Attributes**   | **Type**        | **Required** | **Limitation**                      | **Description**                                   |
| ---------------- | --------------- | ------------ | ----------------------------------- | ------------------------------------------------- |
| **status**       | string          | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                         |
| **code**         | string          | Y            | -                                   | request result code, [refer to ](#result-code)    |
| **data**         | AcceptQuoteResp | N            | -                                   | response body, [refer to](#accept-quote-response) |
| **errorMessage** | string          | N            | maximum length 256                  |                                                   |

## Child Attribute

### AcceptQuoteResp

<span id="accept-quote-response"></span>

| **Attributes**     | **Type** | **Required** | **Limitation**       | **Description**                         |
| ------------------ | -------- | ------------ | -------------------- | --------------------------------------- |
| **orderId**        | string   | Y            |                      | Order ID of the executed convert order. |
| **createTime**     | decimal  | Y            |                      | Timestamp order created                 |
| **orderStatus**    | string   | Y            | SUCCESS/FAIL/PROCESS | Order status                            |
| **quotePrice**     | decimal  | Y            |                      | `From:To` quote price                   |
| **inversePrice**   | decimal  | Y            |                      | `To:From` quote price                   |
| **fromCoin**       | string   | Y            |                      | From Asset                              |
| **fromCoinAmount** | decimal  | Y            |                      | Amount debited                          |
| **toCoin**         | string   | Y            |                      | To Asset                                |
| **toCoinAmount**   | decimal  | Y            |                      | Amount credited                         |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "orderId": "1309477640981204290",
    "createTime": 1667179261865,
    "orderStatus": "PROCESS",
    "quotePrice": 0.00445577,
    "inversePrice": 224.428,
    "fromCoin": "USDT",
    "fromCoinAmount": 179.54201695,
    "toCoin": "BNB",
    "toCoinAmount": 0.8
  }
}
```

```json
{
  "status": "FAIL",
  "code": "345231",
  "errorMessage": "System failed to execute the quote, which has expired. Please request for quote again."
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                            | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| TIME_OUT                           | 345231   | System failed to execute the quote, which has expired. Please request for quote again |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                               | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.         | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                            | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                             | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                                | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                                      | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                         | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                             | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                              | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                                     |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.        |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                                 |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                                |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                             |                                                                                                |