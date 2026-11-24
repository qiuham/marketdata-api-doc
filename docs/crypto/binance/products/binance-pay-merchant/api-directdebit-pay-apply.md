---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-directdebit-pay-apply
api_type: Guide
updated_at: 2026-11-24 18:34:56.121798
---

# Direct Debit/Pre Authorization Payment

This API is used for Merchant/Partner to apply for payment (like periodic and non-periodic debit),
requests will be processed asynchronously and result will be notified via webhook.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/pay/apply
```

## Request Parameters

| **Attributes**        | **Type** | **Required** | **Limitation**                                              | **Description**                                                                                                                                                                                                 |
| --------------------- | -------- | ------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**     | string   | N            | maximum length 19                                           | The sub merchant account id, issued when sub merchant been created at Binance, The parameter subMerchantId is required when configuring show subMerchant info.                                                  |
| **merchantRequestId** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The order id, Unique identifier for the request, idempotent result will be returned for same requestId                                                                                                          |
| **tradeMode**         | string   | Y            | &#34;DIRECT_DEBIT&#34;                                      |
| **bizId**             | Long     | Y            | number                                                      | business orderId like contractId                                                                                                                                                                                |
| **preBizId**          | Long     | N            | number                                                      | prerequisite orderId like pay notification orderId for periodic debit scenario                                                                                                                                  |
| **amount**            | decimal  | Y            | Max Unit Range: 8 decimal places                            | Amount to be deducted, please ensure the amount do not exceed the singleUpperLimit of the contract.                                                                                                             |
| **productType**       | string   | N            | maximum length 16                                           | product type                                                                                                                                                                                                    |
| **productName**       | string   | Y            | maximum length 256                                          | product name                                                                                                                                                                                                    |
| **productDetail**     | string   | N            | maximum length 256                                          | product detail                                                                                                                                                                                                  |
| **webhookUrl**        | string   | N            | maximum length 256. Can only start with http or https.      | The URL for order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |
| **orderTags**         | Object   | N            |                                                             | order tags [refer to](#order-tags)                                                                                                                                                                              |

### orderTags

<span id="order-tags"></span>

| **Attributes**      | **Type** | **Required** | **Limitation** | **Description**                                               |
| ------------------- | -------- | ------------ | -------------- | ------------------------------------------------------------- |
| **ifProfitSharing** | boolean  | N            |                | if specified and true, order will be tagged as profitsharing. |

### Sample Request Body

```json
{
  "subMerchantId": 123,
  "merchantRequestId": "abcd",
  "tradeMode": "DIRECT_DEBIT",
  "bizId": 123,
  "productName": "test payment",
  "amount": 6,
  "webhookUrl": "https://abc.com"
}
```

## Response Parameters

| **Attributes**   | **Type**   | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string     | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string     | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | DataObject | N            | -                                   | response body, [refer to](#data-object)        |
| **errorMessage** | string     | N            | maximum length 256                  |                                                |

## Child Attribute

### DataObject

<span id="data-object"></span>

| **Attributes**        | **Type** | **Required** | **Limitation**                                                                  | **Description**                                                                              |
| --------------------- | -------- | ------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **orderId**           | string   | Y            | maximum length 19                                                               | unique id generated by binance                                                               |
| **prepayId**          | string   | Y            | maximum length 19                                                               | prepay id, the same as returned by the create order API, tracking order status, refund, etc. |
| **merchantRequestId** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                     | The order id, Unique identifier for the request                                              |
| **appliedTime**       | long     | Y            | -                                                                               | transaction time in milli seconds                                                            |
| **status**            | string   | Y            | &#34;SUCCESS&#34; or &#34;FAILED&#34; or &#34;INIT&#34; or &#34;PROCESSING&#34; | status of the order                                                                          |

### Sample Response

#### applied success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "merchantRequestId": "abcd",
    "orderId": "1111",
    "prepayId": "1112",
    "appliedTime": 1672755315849,
    "status": "INIT"
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TYPE_INVALID | 406107   | Merchant type not valid not support individual merchant                        |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TOO_FREQUENT | 406108   | Fail rate is high, please try again later                                      |                                                                                                |

---

# Direct Debit/Pre Authorization Payment 

This API is used for Merchant/Partner to apply for payment (like periodic and non-periodic debit),
requests will be processed asynchronously and result will be notified via webhook.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/pay/apply
```

## Request Parameters

| **Attributes**        | **Type** | **Required** | **Limitation**                                              | **Description**                                                                                                                                                                                                 |
| --------------------- | -------- | ------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**     | string   | N            | maximum length 19                                           | The sub merchant account id, issued when sub merchant been created at Binance, The parameter subMerchantId is required when configuring show subMerchant info.                                                  |
| **merchantRequestId** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The order id, Unique identifier for the request, idempotent result will be returned for same requestId                                                                                                          |
| **tradeMode**         | string   | Y            | &#34;DIRECT_DEBIT&#34;                                      |
| **bizId**             | Long     | Y            | number                                                      | business orderId like contractId                                                                                                                                                                                |
| **preBizId**          | Long     | N            | number                                                      | prerequisite orderId like pay notification orderId for periodic debit scenario                                                                                                                                  |
| **amount**            | decimal  | Y            | Max Unit Range: 8 decimal places                            | Amount to be deducted, please ensure the amount do not exceed the singleUpperLimit of the contract.                                                                                                             |
| **productType**       | string   | N            | maximum length 16                                           | product type                                                                                                                                                                                                    |
| **productName**       | string   | Y            | maximum length 256                                          | product name                                                                                                                                                                                                    |
| **productDetail**     | string   | N            | maximum length 256                                          | product detail                                                                                                                                                                                                  |
| **webhookUrl**        | string   | N            | maximum length 256. Can only start with http or https.      | The URL for order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |
| **orderTags**         | Object   | N            |                                                             | order tags [refer to](#order-tags)                                                                                                                                                                              |

### orderTags

<span id="order-tags"></span>

| **Attributes**      | **Type** | **Required** | **Limitation** | **Description**                                               |
| ------------------- | -------- | ------------ | -------------- | ------------------------------------------------------------- |
| **ifProfitSharing** | boolean  | N            |                | if specified and true, order will be tagged as profitsharing. |

### Sample Request Body

```json
{
  "subMerchantId": 123,
  "merchantRequestId": "abcd",
  "tradeMode": "DIRECT_DEBIT",
  "bizId": 123,
  "productName": "test payment",
  "amount": 6,
  "webhookUrl": "https://abc.com"
}
```

## Response Parameters

| **Attributes**   | **Type**   | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string     | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string     | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | DataObject | N            | -                                   | response body, [refer to](#data-object)        |
| **errorMessage** | string     | N            | maximum length 256                  |                                                |

## Child Attribute

### DataObject

<span id="data-object"></span>

| **Attributes**        | **Type** | **Required** | **Limitation**                                                                  | **Description**                                                                              |
| --------------------- | -------- | ------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **orderId**           | string   | Y            | maximum length 19                                                               | unique id generated by binance                                                               |
| **prepayId**          | string   | Y            | maximum length 19                                                               | prepay id, the same as returned by the create order API, tracking order status, refund, etc. |
| **merchantRequestId** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                     | The order id, Unique identifier for the request                                              |
| **appliedTime**       | long     | Y            | -                                                                               | transaction time in milli seconds                                                            |
| **status**            | string   | Y            | &#34;SUCCESS&#34; or &#34;FAILED&#34; or &#34;INIT&#34; or &#34;PROCESSING&#34; | status of the order                                                                          |

### Sample Response

#### applied success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "merchantRequestId": "abcd",
    "orderId": "1111",
    "prepayId": "1112",
    "appliedTime": 1672755315849,
    "status": "INIT"
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TYPE_INVALID | 406107   | Merchant type not valid not support individual merchant                        |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TOO_FREQUENT | 406108   | Fail rate is high, please try again later                                      |                                                                                                |