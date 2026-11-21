---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-order-refund
api_type: Guide
updated_at: 2026-11-21 18:33:41.762901
---

# Refund Order

Refund order API used for Merchant/Partner to refund for a successful payment.

## EndPoint

```http request
POST /binancepay/openapi/order/refund
```

## Request Parameters

| **Attributes**      | **Type** | **Required** | **Limitation**                                         | **Description**                                                                                                                                                                                                        |
| ------------------- | -------- | ------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **refundRequestId** | string   | Y            | maximum length 64                                      | The unique ID assigned by the merchant to identify a refund request.The value must be same for one refund request.                                                                                                     |
| **prepayId**        | string   | Y            | maximum length 19                                      | The unique ID assigned by Binance for the original order to be refunded.                                                                                                                                               |
| **refundAmount**    | decimal  | Y            | limitation refer to Create Order API order amount      | You can perform multiple partial refunds, but their sum should not exceed the order amount.                                                                                                                            |
| **refundReason**    | string   | N            | maximum length 256                                     |                                                                                                                                                                                                                        |
| **webhookUrl**      | string   | N            | maximum length 256. Can only start with http or https. | The URL for refund order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |

### Sample Request Body

```json
{
  "refundRequestId": "68711039982968832",
  "prepayId": "383729303729303",
  "refundAmount": 25.17,
  "refundReason": ""
}
```

## Response Parameters

| **Attributes**   | **Type**     | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ------------ | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string       | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string       | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | RefundResult | N            | -                                   | response body, [refer to](#order-result)       |
| **errorMessage** | string       | N            | maximum length 256                  |                                                |

## Child Attribute

### RefundResult

<span id="refund-result"></span>

| **Attributes**         | **Type** | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                             |
| ---------------------- | -------- | ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **refundId**           | long     | Y            | -                                                 | The unique ID assigned by Binance for this refund.                                                                                                                                          |
| **refundRequestId**    | string   | Y            | maximum length 64                                 | The unique ID assigned by the merchant to identify a refund request.                                                                                                                        |
| **prepayId**           | string   | Y            | maximum length 19                                 | The unique ID assigned by Binance for the original order to be refunded.                                                                                                                    |
| **orderAmount**        | string   | Y            | limitation refer to Create Order API order amount | The total amount of prepay order.                                                                                                                                                           |
| **refundedAmount**     | string   | Y            | limitation refer to Create Order API order amount | The total refunded amount included this refund request.                                                                                                                                     |
| **refundAmount**       | string   | Y            | limitation refer to Create Order API order amount | The refund amount of this refund request.                                                                                                                                                   |
| **refundedCommission** | string   | Y            | -                                                 | The total refunded transaction fees included this refund request.                                                                                                                           |
| **refundCommission**   | string   | Y            | -                                                 | The refund transaction fees of this refund request.                                                                                                                                         |
| **remainingAttempts**  | int      | Y            | -                                                 | The remaining attempts of this original order. If this value becomes 1, then your next refund request amount will be ignored. We will refund all the remaing amount of this original order. |
| **payerOpenId**        | string   | Y            | maximum length 32                                 | The payer open id of this refund which is the merchant open id.                                                                                                                             |
| **refundStatus**       | string   | Y            | -                                                 | The status of this refund. Example: INITIAL, PENDING, CANCELLED, REFUNDED                                                                                                                   |
| **duplicateRequest**   | string   | Y            | -                                                 | The flag to mark this request refundRequestId is duplicate or not. It will be 'Y' or 'N'                                                                                                    |

### Response Parameters

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "refundId": 419936748741509122,
    "refundRequestId": "68711039982968832",
    "prepayId": "383729303729303",
    "orderAmount": "100.11",
    "refundedAmount": "10.88",
    "refundAmount": "5.00",
    "refundedCommission": "0.00001000",
    "refundCommission": "0.00001000",
    "remainingAttempts": 8,
    "payerOpenId": "dde730c2e0ea1f1780cf26343b98fd3b",
    "refundStatus": "REFUNDED",
    "duplicateRequest": "N"
  },
  "errorMessage": ""
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                 | **Code** | **Reason**                                                                      | **Solution**                                                                                   |
| ---------------------------------------- | -------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                            | 400000   | An unknown error occurred while processing the request.                         | Try again later                                                                                |
| INVALID_REQUEST                          | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.   | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                        | 400002   | Incorrect signature result                                                      | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                        | 400003   | Timestamp for this request is outside of the time window.                       | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                    | 400004   | API identity key not found or invalid.                                          | Check API identity key                                                                         |
| BAD_API_KEY_FMT                          | 400005   | API identity key format invalid.                                                | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                          | 400006   | Request method not supported.                                                   | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                 | 400007   | Media type not supported.                                                       | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                     | 400008   | Request body is not a valid json object.                                        | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED       | 400100   | A parameter was missing/empty/null, or malformed.                               |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH               | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.  |                                                                                                |
| INVALID_PARAM_WRONG_VALUE                | 400102   | A parameter was not valid, the value is out of range.                           |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR               | 400103   | A parameter was not valid, contains illegal characters                          |                                                                                                |
| INVALID_REQUEST_TOO_LARGE                | 400104   | Invalid request, content length too large                                       |                                                                                                |
| ORDER_NOT_FOUND                          | 400202   | Order not found.                                                                |                                                                                                |
| PAYMENT_ACCOUNT_NOT_FOUND                | 400601   | account not found                                                               |                                                                                                |
| PAYMENT_PAY_ORDER_NOT_FOUND              | 400602   | pay order not found                                                             |                                                                                                |
| PAYMENT_INVALID_PAY_ORDER_EXPIRED        | 400603   | The pay order is already expired                                                |                                                                                                |
| PAYMENT_TRANSACTION_INVALID_OR_NOT_FOUND | 400604   | Transaction not found or invalid                                                |                                                                                                |
| PAYMENT_REFUND_AMOUNT_PRECISION_INVALID  | 400605   | Refund amount precision is not valid                                            |                                                                                                |
| MERCHANT_REFUND_ACCESS_FORBIDDEN         | 400606   | Account has no accessibility to this function                                   |                                                                                                |
| PAYMENT_REFUND_TOO_MANY_TIMES            | 400607   | Refund too many times                                                           |                                                                                                |
| PAYMENT_REFUND_AMOUNT_INVALID            | 400608   | Refund amount is not valid                                                      |                                                                                                |
| PAYMENT_LAST_REFUND_AMOUNT_INVALID       | 400609   | Refund amount is not valid                                                      |                                                                                                |
| MERCHANT_REFUND_LIMITATION               | 400610   | This refund amount is larger than your refund limit please ask admin to approve |                                                                                                |
| PAYMENT_INSUFFICIENT_BALANCE             | 400611   | Insufficient Balance                                                            |                                                                                                |
| PAYMENT_PENDING                          | 400612   | payment in processing                                                           |                                                                                                |

---

# Refund Order

Refund order API used for Merchant/Partner to refund for a successful payment.

## EndPoint

```http request
POST /binancepay/openapi/order/refund
```

## Request Parameters

| **Attributes**      | **Type** | **Required** | **Limitation**                                         | **Description**                                                                                                                                                                                                        |
| ------------------- | -------- | ------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **refundRequestId** | string   | Y            | maximum length 64                                      | The unique ID assigned by the merchant to identify a refund request.The value must be same for one refund request.                                                                                                     |
| **prepayId**        | string   | Y            | maximum length 19                                      | The unique ID assigned by Binance for the original order to be refunded.                                                                                                                                               |
| **refundAmount**    | decimal  | Y            | limitation refer to Create Order API order amount      | You can perform multiple partial refunds, but their sum should not exceed the order amount.                                                                                                                            |
| **refundReason**    | string   | N            | maximum length 256                                     |                                                                                                                                                                                                                        |
| **webhookUrl**      | string   | N            | maximum length 256. Can only start with http or https. | The URL for refund order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |

### Sample Request Body

```json
{
  "refundRequestId": "68711039982968832",
  "prepayId": "383729303729303",
  "refundAmount": 25.17,
  "refundReason": ""
}
```

## Response Parameters

| **Attributes**   | **Type**     | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ------------ | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string       | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string       | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | RefundResult | N            | -                                   | response body, [refer to](#order-result)       |
| **errorMessage** | string       | N            | maximum length 256                  |                                                |

## Child Attribute

### RefundResult

<span id="refund-result"></span>

| **Attributes**         | **Type** | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                             |
| ---------------------- | -------- | ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **refundId**           | long     | Y            | -                                                 | The unique ID assigned by Binance for this refund.                                                                                                                                          |
| **refundRequestId**    | string   | Y            | maximum length 64                                 | The unique ID assigned by the merchant to identify a refund request.                                                                                                                        |
| **prepayId**           | string   | Y            | maximum length 19                                 | The unique ID assigned by Binance for the original order to be refunded.                                                                                                                    |
| **orderAmount**        | string   | Y            | limitation refer to Create Order API order amount | The total amount of prepay order.                                                                                                                                                           |
| **refundedAmount**     | string   | Y            | limitation refer to Create Order API order amount | The total refunded amount included this refund request.                                                                                                                                     |
| **refundAmount**       | string   | Y            | limitation refer to Create Order API order amount | The refund amount of this refund request.                                                                                                                                                   |
| **refundedCommission** | string   | Y            | -                                                 | The total refunded transaction fees included this refund request.                                                                                                                           |
| **refundCommission**   | string   | Y            | -                                                 | The refund transaction fees of this refund request.                                                                                                                                         |
| **remainingAttempts**  | int      | Y            | -                                                 | The remaining attempts of this original order. If this value becomes 1, then your next refund request amount will be ignored. We will refund all the remaing amount of this original order. |
| **payerOpenId**        | string   | Y            | maximum length 32                                 | The payer open id of this refund which is the merchant open id.                                                                                                                             |
| **refundStatus**       | string   | Y            | -                                                 | The status of this refund. Example: INITIAL, PENDING, CANCELLED, REFUNDED                                                                                                                   |
| **duplicateRequest**   | string   | Y            | -                                                 | The flag to mark this request refundRequestId is duplicate or not. It will be 'Y' or 'N'                                                                                                    |

### Response Parameters

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "refundId": 419936748741509122,
    "refundRequestId": "68711039982968832",
    "prepayId": "383729303729303",
    "orderAmount": "100.11",
    "refundedAmount": "10.88",
    "refundAmount": "5.00",
    "refundedCommission": "0.00001000",
    "refundCommission": "0.00001000",
    "remainingAttempts": 8,
    "payerOpenId": "dde730c2e0ea1f1780cf26343b98fd3b",
    "refundStatus": "REFUNDED",
    "duplicateRequest": "N"
  },
  "errorMessage": ""
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                 | **Code** | **Reason**                                                                      | **Solution**                                                                                   |
| ---------------------------------------- | -------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                            | 400000   | An unknown error occurred while processing the request.                         | Try again later                                                                                |
| INVALID_REQUEST                          | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.   | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                        | 400002   | Incorrect signature result                                                      | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                        | 400003   | Timestamp for this request is outside of the time window.                       | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                    | 400004   | API identity key not found or invalid.                                          | Check API identity key                                                                         |
| BAD_API_KEY_FMT                          | 400005   | API identity key format invalid.                                                | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                          | 400006   | Request method not supported.                                                   | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                 | 400007   | Media type not supported.                                                       | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                     | 400008   | Request body is not a valid json object.                                        | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED       | 400100   | A parameter was missing/empty/null, or malformed.                               |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH               | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.  |                                                                                                |
| INVALID_PARAM_WRONG_VALUE                | 400102   | A parameter was not valid, the value is out of range.                           |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR               | 400103   | A parameter was not valid, contains illegal characters                          |                                                                                                |
| INVALID_REQUEST_TOO_LARGE                | 400104   | Invalid request, content length too large                                       |                                                                                                |
| ORDER_NOT_FOUND                          | 400202   | Order not found.                                                                |                                                                                                |
| PAYMENT_ACCOUNT_NOT_FOUND                | 400601   | account not found                                                               |                                                                                                |
| PAYMENT_PAY_ORDER_NOT_FOUND              | 400602   | pay order not found                                                             |                                                                                                |
| PAYMENT_INVALID_PAY_ORDER_EXPIRED        | 400603   | The pay order is already expired                                                |                                                                                                |
| PAYMENT_TRANSACTION_INVALID_OR_NOT_FOUND | 400604   | Transaction not found or invalid                                                |                                                                                                |
| PAYMENT_REFUND_AMOUNT_PRECISION_INVALID  | 400605   | Refund amount precision is not valid                                            |                                                                                                |
| MERCHANT_REFUND_ACCESS_FORBIDDEN         | 400606   | Account has no accessibility to this function                                   |                                                                                                |
| PAYMENT_REFUND_TOO_MANY_TIMES            | 400607   | Refund too many times                                                           |                                                                                                |
| PAYMENT_REFUND_AMOUNT_INVALID            | 400608   | Refund amount is not valid                                                      |                                                                                                |
| PAYMENT_LAST_REFUND_AMOUNT_INVALID       | 400609   | Refund amount is not valid                                                      |                                                                                                |
| MERCHANT_REFUND_LIMITATION               | 400610   | This refund amount is larger than your refund limit please ask admin to approve |                                                                                                |
| PAYMENT_INSUFFICIENT_BALANCE             | 400611   | Insufficient Balance                                                            |                                                                                                |
| PAYMENT_PENDING                          | 400612   | payment in processing                                                           |                                                                                                |