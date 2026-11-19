---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-order-create
api_type: Guide
updated_at: 2026-11-19 18:36:10.127020
---

# Create Order (Deprecated)

**The API is deprecated, please migrate to [Create Order V2](api-order-create-v2) ASAP**

Create order API used for merchant/partner to initiate acquiring order.

## EndPoint

```http request
POST /binancepay/openapi/order
```

## Request Parameters

| **Attributes**         | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                                                                                                                                                                                 |
| ---------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**      | string   | N            | maximum length 19                                                                                             | The sub merchant account id, issued when sub merchant been created at Binance, The parameter subMerchantId is required when configuring show subMerchant info.                                                  |
| **merchantTradeNo**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                                                   | The order id, Unique identifier for the request                                                                                                                                                                 |
| **tradeType**          | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                                                                                                                                                                                                |
| **totalFee**           | decimal  | Y            | Amount Range: 0.01 - 20000; Max Unit Range: 8 decimal places                                                  | order amount                                                                                                                                                                                                    |
| **currency**           | string   | Y            | only "BUSD","USDT","MBOX" can be accepted, fiat NOT supported.                                                | order currency                                                                                                                                                                                                  |
| **productType**        | string   | N            | maximum length 16                                                                                             | product type                                                                                                                                                                                                    |
| **productName**        | string   | N            | maximum length 256                                                                                            | product name                                                                                                                                                                                                    |
| **productDetail**      | string   | N            | maximum length 256                                                                                            | product detail                                                                                                                                                                                                  |
| **returnUrl**          | string   | N            | maximum length 256                                                                                            | The URL to redirect to when the payment is successful                                                                                                                                                           |
| **cancelUrl**          | string   | N            | maximum length 256                                                                                            | The URL to redirect to when payment is failed                                                                                                                                                                   |
| **orderExpireTime**    | long     | N            | maximum order time is 1 hour                                                                                  | OrderExpireTime is the time at which order will expire. Please input orderExpireTime in Epoch timestamp in milliseconds. If not specified, order time will be 1 hour                                            |
| **supportPayCurrency** | string   | N            | maximum length 1024. Input to be separated by commas, e.g. "BUSD,BNB"                                         | SupportPayCurrency determines the currencies that a customer is allowed to use to pay for the order. If not specified, all Binance Pay supported currencies will be allowed.                                    |
| **universalUrlAttach** | string   | N            | maximum length 120. e.g. "countryCode=1&phone=1234567"                                                        | the attachment parameter for the response field "universalUrl"                                                                                                                                                  |
| **passThroughInfo**    | string   | N            | maximum length 512                                                                                            | pass through info, returned as-is in query order API and payment webhook notification                                                                                                                           |
| **webhookUrl**         | string   | N            | maximum length 256. Can only start with http or https.                                                        | The URL for order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |

### Sample Request Body

```json
{
  "subMerchantId": "98765987",
  "merchantTradeNo": "9825382937292",
  "totalFee": 25.17,
  "productDetail": "Greentea ice cream cone",
  "currency": "USDT",
  "returnUrl": "",
  "cancelUrl": "",
  "tradeType": "APP",
  "productType": "Food",
  "productName": "Ice Cream"
}
```

## Response Parameters

| **Attributes**   | **Type**    | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ----------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string      | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string      | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | OrderResult | N            | -                                   | response body, [refer to](#order-result)       |
| **errorMessage** | string      | N            | maximum length 256                  |                                                |

## Child Attribute

### OrderResult

<span id="order-result"></span>

| **Attributes**   | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                |
| ---------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **prepayId**     | string   | Y            | maximum length 19                                                                                             | unique id generated by binance                 |
| **tradeType**    | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                               |
| **expireTime**   | long     | Y            | -                                                                                                             | expire time in milli seconds                   |
| **qrcodeLink**   | string   | Y            | maximum length 256                                                                                            | qr code img link                               |
| **qrContent**    | string   | Y            | maximum length 256                                                                                            | qr content info                                |
| **checkoutUrl**  | string   | Y            | maximum length 256                                                                                            | binance hosted checkout page url               |
| **deeplink**     | string   | Y            | maximum length 256                                                                                            | deeplink to open binance app to finish payment |
| **universalUrl** | string   | Y            | maximum length 512                                                                                            | universal url to finish the payment            |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "prepayId": "29383937493038367292",
    "tradeType": "APP",
    "expireTime": 121123232223,
    "qrcodeLink": "https://qrservice.dev.com/en/qr/dplkb005181944f84b84aba2430e1177012b.jpg",
    "qrContent": "https://qrservice.dev.com/en/qr/dplk12121112b",
    "checkoutUrl": "https://pay.binance.com/checkout/dplk12121112b",
    "deeplink": "bnc://app.binance.com/payment/secpay/xxxxxx",
    "universalUrl": "https://app.binance.com/payment/secpay?_dp=xxx=&linkToken=xxx"
  },
  "errorMessage": ""
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
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |
| SUB_MERCHANT_INVALID               | 400206   | The sub merchant does not exist or is in an unavailable state.                 |                                                                                                |

---

# Create Order (Deprecated)

**The API is deprecated, please migrate to [Create Order V2](api-order-create-v2) ASAP**

Create order API used for merchant/partner to initiate acquiring order.

## EndPoint

```http request
POST /binancepay/openapi/order
```

## Request Parameters

| **Attributes**         | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                                                                                                                                                                                 |
| ---------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**      | string   | N            | maximum length 19                                                                                             | The sub merchant account id, issued when sub merchant been created at Binance, The parameter subMerchantId is required when configuring show subMerchant info.                                                  |
| **merchantTradeNo**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                                                   | The order id, Unique identifier for the request                                                                                                                                                                 |
| **tradeType**          | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                                                                                                                                                                                                |
| **totalFee**           | decimal  | Y            | Amount Range: 0.01 - 20000; Max Unit Range: 8 decimal places                                                  | order amount                                                                                                                                                                                                    |
| **currency**           | string   | Y            | only "BUSD","USDT","MBOX" can be accepted, fiat NOT supported.                                                | order currency                                                                                                                                                                                                  |
| **productType**        | string   | N            | maximum length 16                                                                                             | product type                                                                                                                                                                                                    |
| **productName**        | string   | N            | maximum length 256                                                                                            | product name                                                                                                                                                                                                    |
| **productDetail**      | string   | N            | maximum length 256                                                                                            | product detail                                                                                                                                                                                                  |
| **returnUrl**          | string   | N            | maximum length 256                                                                                            | The URL to redirect to when the payment is successful                                                                                                                                                           |
| **cancelUrl**          | string   | N            | maximum length 256                                                                                            | The URL to redirect to when payment is failed                                                                                                                                                                   |
| **orderExpireTime**    | long     | N            | maximum order time is 1 hour                                                                                  | OrderExpireTime is the time at which order will expire. Please input orderExpireTime in Epoch timestamp in milliseconds. If not specified, order time will be 1 hour                                            |
| **supportPayCurrency** | string   | N            | maximum length 1024. Input to be separated by commas, e.g. "BUSD,BNB"                                         | SupportPayCurrency determines the currencies that a customer is allowed to use to pay for the order. If not specified, all Binance Pay supported currencies will be allowed.                                    |
| **universalUrlAttach** | string   | N            | maximum length 120. e.g. "countryCode=1&phone=1234567"                                                        | the attachment parameter for the response field "universalUrl"                                                                                                                                                  |
| **passThroughInfo**    | string   | N            | maximum length 512                                                                                            | pass through info, returned as-is in query order API and payment webhook notification                                                                                                                           |
| **webhookUrl**         | string   | N            | maximum length 256. Can only start with http or https.                                                        | The URL for order notification. If the webhookUrl is passed in the parameter, the webhook url configured on the merchant platform will not take effect, and the currently passed url will be called back first. |

### Sample Request Body

```json
{
  "subMerchantId": "98765987",
  "merchantTradeNo": "9825382937292",
  "totalFee": 25.17,
  "productDetail": "Greentea ice cream cone",
  "currency": "USDT",
  "returnUrl": "",
  "cancelUrl": "",
  "tradeType": "APP",
  "productType": "Food",
  "productName": "Ice Cream"
}
```

## Response Parameters

| **Attributes**   | **Type**    | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ----------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string      | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string      | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | OrderResult | N            | -                                   | response body, [refer to](#order-result)       |
| **errorMessage** | string      | N            | maximum length 256                  |                                                |

## Child Attribute

### OrderResult

<span id="order-result"></span>

| **Attributes**   | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                |
| ---------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **prepayId**     | string   | Y            | maximum length 19                                                                                             | unique id generated by binance                 |
| **tradeType**    | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                               |
| **expireTime**   | long     | Y            | -                                                                                                             | expire time in milli seconds                   |
| **qrcodeLink**   | string   | Y            | maximum length 256                                                                                            | qr code img link                               |
| **qrContent**    | string   | Y            | maximum length 256                                                                                            | qr content info                                |
| **checkoutUrl**  | string   | Y            | maximum length 256                                                                                            | binance hosted checkout page url               |
| **deeplink**     | string   | Y            | maximum length 256                                                                                            | deeplink to open binance app to finish payment |
| **universalUrl** | string   | Y            | maximum length 512                                                                                            | universal url to finish the payment            |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "prepayId": "29383937493038367292",
    "tradeType": "APP",
    "expireTime": 121123232223,
    "qrcodeLink": "https://qrservice.dev.com/en/qr/dplkb005181944f84b84aba2430e1177012b.jpg",
    "qrContent": "https://qrservice.dev.com/en/qr/dplk12121112b",
    "checkoutUrl": "https://pay.binance.com/checkout/dplk12121112b",
    "deeplink": "bnc://app.binance.com/payment/secpay/xxxxxx",
    "universalUrl": "https://app.binance.com/payment/secpay?_dp=xxx=&linkToken=xxx"
  },
  "errorMessage": ""
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
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |
| SUB_MERCHANT_INVALID               | 400206   | The sub merchant does not exist or is in an unavailable state.                 |                                                                                                |