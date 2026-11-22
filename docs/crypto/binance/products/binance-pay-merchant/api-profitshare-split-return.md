---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-profitshare-split-return
api_type: Guide
updated_at: 2026-11-22 18:32:42.737836
---

# Split Return

API used to return splited assets

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/return
```

## Request Parameters

| **Attributes**              | **Type** | **Required** | **Limitation**                                          | **Description**                                                                                                        |
| --------------------------- | -------- | ------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **prepayOrderId**           | string   | Y            |                                                         | it's Pre Pay order ID                                                                                                  |
| **splitOrderNo**            | string   | N            | must pass splitOrderNo or originMerchantRequestId to us | The unique ID that is assigned by Binance Pay to identify a profit-sharing request from merchants or service providers |
| **originMerchantRequestId** | string   | N            | must pass splitOrderNo or originMerchantRequestId to us | The unique ID that is assigned by the merchant/SP to identify a profit-sharing request.                                |
| **merchantReturnNo**        | string   | Y            | 1 <= length <= 32                                       | The unique ID that is assigned by the merchant/SP to identify a profit-return request.                                 |
| **transferOutAccount**      | string   | Y            |                                                         | Binance ID, the one that the merchant wants to collect fund back                                                       |
| **returnAmount**            | decimal  | Y            |                                                         | the amount that want to collect back                                                                                   |
| **description**             | string   | N            | 1 <= length <= 128                                      |                                                                                                                        |
| **webhookUrl**              | string   | N            | 1 <= length <= 256                                      | Can only start with http or https.                                                                                     |

### Sample Request Parameter

```json
{
  "prepayOrderId": "215324856789557248",
  "splitOrderNo": "224313347535298560",
  "originMerchantRequestId": "521134231",
  "merchantReturnNo": "520cczhong9",
  "transferOutAccount": "1000135827517",
  "returnAmount": "0.01",
  "description": "jojo",
  "webhookUrl": "http://www.aaa.com/settle/query-merchant-info"
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

| **Attributes**              | **Type** | **Required** | **Limitation** | **Description**                   |
| --------------------------- | -------- | ------------ | -------------- | --------------------------------- |
| **prepayOrderId**           | string   | Y            |                |                                   |
| **splitOrderNo**            | string   | Y            |                |                                   |
| **originMerchantRequestId** | string   | Y            |                |                                   |
| **merchantReturnNo**        | string   | Y            |                |                                   |
| **transferOutAccount**      | string   | Y            |                |                                   |
| **returnAmount**            | decimal  | Y            |                |                                   |
| **returnOrderNo**           | string   | Y            |                | Binance return order no           |
| **status**                  | int      | Y            |                | PROCESSING(1),SUCCESS(2),FAIL(3); |
| **failReason**              | string   | N            |                |                                   |
| **finishTime**              | long     | Y            |                | unix_timestamp (seconds)          |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "prepayOrderId": "233178711799922688",
    "splitOrderNo": "233178716105637888",
    "originMerchantRequestId": "IecscqYJMLtPoazKFeHfQNVDmyUeverE",
    "merchantReturnNo": "520cczhong100",
    "transferOutAccount": "1000136964356",
    "returnAmount": 0.01,
    "returnOrderNo": "233343189633785856",
    "status": 2,
    "failReason": "",
    "finishTime": 1686495703
  }
}
}
```

```json
{
  "status": "FAIL",
  "code": "400209",
  "errorMessage": "order not found or order status is not success"
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
| ORDER_STATUS_INVALID               | 400209   | Order not found or order status is not success                                 |                                                                                                |
| NO_PROFIT_SHARE_MARK               | 400210   | Order can not split revenue                                                    |                                                                                                |
| PROFIT_SPLIT_AMOUNT_INVALID        | 400211   | Split amount larger than the max rate                                          |                                                                                                |
| ORDER_STATUS_NOT_END               | 400212   | Exists frozen amount, can not split                                            |                                                                                                |
| SAME_ACCOUNT                       | 400213   | Same account repeated                                                          |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |
| NO_AVAILABLE_SPLIT_AMOUNT          | 400215   | No available split amount                                                      |                                                                                                |
| REQ_ID_ALREADY_EXISTS              | 400216   | RequestId has been submitted                                                   |                                                                                                |
| SPLITTING_ORDER_EXIST              | 400217   | Has order that is splitting                                                    |                                                                                                |
| RECEIVER_NOT_SPLIT                 | 400218   | Hasn't split for this receiver                                                 |                                                                                                |
| RETURN_SPLIT_REST_ZERO_AMOUNT      | 400219   | All amount has returned                                                        |                                                                                                |
| LARGER_THAN_MAX_TIMES              | 400220   | Larger than max return times 10                                                |                                                                                                |
| LARGER_THAN_MAX_INTERVAL           | 400221   | Larger than max interval 180 days                                              |                                                                                                |
| SPLIT_NOT_SUCCESS                  | 400222   | Split has not been success for this account                                    |                                                                                                |
| INVALID_VOUCHER_STATUS             | 400223   | Invalid voucher status                                                         |                                                                                                |

---

# Split Return

API used to return splited assets

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/return
```

## Request Parameters

| **Attributes**              | **Type** | **Required** | **Limitation**                                          | **Description**                                                                                                        |
| --------------------------- | -------- | ------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **prepayOrderId**           | string   | Y            |                                                         | it's Pre Pay order ID                                                                                                  |
| **splitOrderNo**            | string   | N            | must pass splitOrderNo or originMerchantRequestId to us | The unique ID that is assigned by Binance Pay to identify a profit-sharing request from merchants or service providers |
| **originMerchantRequestId** | string   | N            | must pass splitOrderNo or originMerchantRequestId to us | The unique ID that is assigned by the merchant/SP to identify a profit-sharing request.                                |
| **merchantReturnNo**        | string   | Y            | 1 <= length <= 32                                       | The unique ID that is assigned by the merchant/SP to identify a profit-return request.                                 |
| **transferOutAccount**      | string   | Y            |                                                         | Binance ID, the one that the merchant wants to collect fund back                                                       |
| **returnAmount**            | decimal  | Y            |                                                         | the amount that want to collect back                                                                                   |
| **description**             | string   | N            | 1 <= length <= 128                                      |                                                                                                                        |
| **webhookUrl**              | string   | N            | 1 <= length <= 256                                      | Can only start with http or https.                                                                                     |

### Sample Request Parameter

```json
{
  "prepayOrderId": "215324856789557248",
  "splitOrderNo": "224313347535298560",
  "originMerchantRequestId": "521134231",
  "merchantReturnNo": "520cczhong9",
  "transferOutAccount": "1000135827517",
  "returnAmount": "0.01",
  "description": "jojo",
  "webhookUrl": "http://www.aaa.com/settle/query-merchant-info"
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

| **Attributes**              | **Type** | **Required** | **Limitation** | **Description**                   |
| --------------------------- | -------- | ------------ | -------------- | --------------------------------- |
| **prepayOrderId**           | string   | Y            |                |                                   |
| **splitOrderNo**            | string   | Y            |                |                                   |
| **originMerchantRequestId** | string   | Y            |                |                                   |
| **merchantReturnNo**        | string   | Y            |                |                                   |
| **transferOutAccount**      | string   | Y            |                |                                   |
| **returnAmount**            | decimal  | Y            |                |                                   |
| **returnOrderNo**           | string   | Y            |                | Binance return order no           |
| **status**                  | int      | Y            |                | PROCESSING(1),SUCCESS(2),FAIL(3); |
| **failReason**              | string   | N            |                |                                   |
| **finishTime**              | long     | Y            |                | unix_timestamp (seconds)          |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "prepayOrderId": "233178711799922688",
    "splitOrderNo": "233178716105637888",
    "originMerchantRequestId": "IecscqYJMLtPoazKFeHfQNVDmyUeverE",
    "merchantReturnNo": "520cczhong100",
    "transferOutAccount": "1000136964356",
    "returnAmount": 0.01,
    "returnOrderNo": "233343189633785856",
    "status": 2,
    "failReason": "",
    "finishTime": 1686495703
  }
}
}
```

```json
{
  "status": "FAIL",
  "code": "400209",
  "errorMessage": "order not found or order status is not success"
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
| ORDER_STATUS_INVALID               | 400209   | Order not found or order status is not success                                 |                                                                                                |
| NO_PROFIT_SHARE_MARK               | 400210   | Order can not split revenue                                                    |                                                                                                |
| PROFIT_SPLIT_AMOUNT_INVALID        | 400211   | Split amount larger than the max rate                                          |                                                                                                |
| ORDER_STATUS_NOT_END               | 400212   | Exists frozen amount, can not split                                            |                                                                                                |
| SAME_ACCOUNT                       | 400213   | Same account repeated                                                          |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |
| NO_AVAILABLE_SPLIT_AMOUNT          | 400215   | No available split amount                                                      |                                                                                                |
| REQ_ID_ALREADY_EXISTS              | 400216   | RequestId has been submitted                                                   |                                                                                                |
| SPLITTING_ORDER_EXIST              | 400217   | Has order that is splitting                                                    |                                                                                                |
| RECEIVER_NOT_SPLIT                 | 400218   | Hasn't split for this receiver                                                 |                                                                                                |
| RETURN_SPLIT_REST_ZERO_AMOUNT      | 400219   | All amount has returned                                                        |                                                                                                |
| LARGER_THAN_MAX_TIMES              | 400220   | Larger than max return times 10                                                |                                                                                                |
| LARGER_THAN_MAX_INTERVAL           | 400221   | Larger than max interval 180 days                                              |                                                                                                |
| SPLIT_NOT_SUCCESS                  | 400222   | Split has not been success for this account                                    |                                                                                                |
| INVALID_VOUCHER_STATUS             | 400223   | Invalid voucher status                                                         |                                                                                                |