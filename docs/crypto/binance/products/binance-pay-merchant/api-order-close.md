---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-order-close
api_type: Guide
updated_at: 2026-11-24 18:34:45.255925
---

# Close Order

Close order API used for merchant/partner to close order without any prior payment activities
triggered by user. The successful close result will be notified asynchronously through Order
Notification Webhook with bizStatus = "PAY_CLOSED"

## EndPoint

```http request
POST /binancepay/openapi/order/close
```

## Request Parameters

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                            | **Description**                                 |
| ------------------- | -------- | ------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **merchantTradeNo** | string   | N            | maximum length 32, letter or digit, no other symbol allowed, can not be empty if prepayId is empty        | The order id, Unique identifier for the request |
| **prepayId**        | string   | N            | maximum length 19, letter or digit, no other symbol allowed, can not be empty if merchantTradeNo is empty | Binance unique order id                         |

### Sample Request Body

Query order result by merchantTradeNo:

```json
{
  "merchantTradeNo": "9825382937292",
  "prepayId": null
}
```

Query order result by prepayId:

```json
{
  "merchantTradeNo": null,
  "prepayId": "9825382937292"
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                                                                                                                                          |
| ---------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                                                                                                                                                |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code)                                                                                                                           |
| **data**         | boolean  | N            | -                                   | equals to true when status="SUCCESS"，which is close request is accepted，and successful close result will be notified asynchronously through Order Notification Webhook |
| **errorMessage** | string   | N            | maximum length 256                  | error description when status="FAIL"                                                                                                                                     |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true,
  "errorMessage": null
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                                  | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                                     | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.               | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                                  | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                                   | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                                      | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                                            | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                               | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                                   | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                                    | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                                           |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.              |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                                       |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                                      |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                                   |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                                            |                                                                                                |
| INVALID_ORDER_STATUS               | 400204   | The Order is not applicable to close as it was paid or has any payment activity on the way. |                                                                                                |

---

# Close Order

Close order API used for merchant/partner to close order without any prior payment activities
triggered by user. The successful close result will be notified asynchronously through Order
Notification Webhook with bizStatus = "PAY_CLOSED"

## EndPoint

```http request
POST /binancepay/openapi/order/close
```

## Request Parameters

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                            | **Description**                                 |
| ------------------- | -------- | ------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **merchantTradeNo** | string   | N            | maximum length 32, letter or digit, no other symbol allowed, can not be empty if prepayId is empty        | The order id, Unique identifier for the request |
| **prepayId**        | string   | N            | maximum length 19, letter or digit, no other symbol allowed, can not be empty if merchantTradeNo is empty | Binance unique order id                         |

### Sample Request Body

Query order result by merchantTradeNo:

```json
{
  "merchantTradeNo": "9825382937292",
  "prepayId": null
}
```

Query order result by prepayId:

```json
{
  "merchantTradeNo": null,
  "prepayId": "9825382937292"
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                                                                                                                                          |
| ---------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                                                                                                                                                |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code)                                                                                                                           |
| **data**         | boolean  | N            | -                                   | equals to true when status="SUCCESS"，which is close request is accepted，and successful close result will be notified asynchronously through Order Notification Webhook |
| **errorMessage** | string   | N            | maximum length 256                  | error description when status="FAIL"                                                                                                                                     |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true,
  "errorMessage": null
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                                  | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                                     | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.               | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                                  | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                                   | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                                      | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                                            | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                               | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                                   | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                                    | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                                           |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.              |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                                       |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                                      |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                                   |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                                            |                                                                                                |
| INVALID_ORDER_STATUS               | 400204   | The Order is not applicable to close as it was paid or has any payment activity on the way. |                                                                                                |