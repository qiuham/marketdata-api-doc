---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-directdebit-create-contract
api_type: Guide
updated_at: 2026-11-25 18:34:47.262956
---

# Direct Debit/Pre Authorization Create Contract

This API is for merchant/partner to create direct debit/ pre authorization contract for user
authorization.

- This API is only available for whitelisted merchants. You may apply for direct debit on the
  [merchant dashboard](https://merchant.binance.com/en/dashboard/debit-management) under Products >
  Debit Management. Alternatively, you may contact us at merchant@binance.com, along with your
  Merchant ID, background and use case.

## EndPoint

```http request
POST /binancepay/openapi/direct-debit/contract
```

## Request Parameters

| **Attributes**           | **Type** | **Required** | **Limitation**                                                                 | **Description**                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | -------- | ------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**        | string   | N            | maximum length 19                                                              | The sub merchant account id, issued when sub merchant been created at Binance.                                                                                                                                                                                                                                                                                |
| **merchantContractCode** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                    | The unique ID assigned by the merchant to identify a direct debit contract request.                                                                                                                                                                                                                                                                           |
| **serviceName**          | string   | Y            | maximum length 32                                                              | service name                                                                                                                                                                                                                                                                                                                                                  |
| **scenarioCode**         | string   | Y            | eg. General_Travel, for more please [refer to](#scenario-code)                 |
| **singleUpperLimit**     | decimal  | Y            | Max Unit Range: 8 decimal places                                               | upper limit related to scenarioCode, for more please [refer to](#scenario-code)                                                                                                                                                                                                                                                                               |
| **currency**             | string   | Y            | only "USDT" or "USDC" is accepted and "USDC" for mica user, fiat not supported | Order currency also the settlement currency                                                                                                                                                                                                                                                                                                                   |
| **periodic**             | boolean  | Y            | true/false                                                                     | this contract support periodic debit or not                                                                                                                                                                                                                                                                                                                   |
| **cycleDebitFixed**      | boolean  | N            | true/false                                                                     | mandatory if periodic = true. true = fixed amount, false = variable amount                                                                                                                                                                                                                                                                                    |
| **cycleType**            | string   | N            | MONTH or DAY                                                                   | mandatory if periodic = true. Values: MONTH or DAY                                                                                                                                                                                                                                                                                                            |
| **cycleValue**           | integer  | N            | -                                                                              | mandatory if periodic = true. Values: if cycleType=MONTH: 1~24, cycleType=DAY: interval days >7 <br/><br/> Combining with another parameter cycleType to determine the deduction period, for example, cycleType is DAY, cycleValue=30, then the deduction period is 30 days; cycleType is MONTH, cycleValue=3, then the deduction period is 3 natural months. |
| **firstDeductTime**      | long     | N            | -                                                                              | mandatory if periodic = true. first deduct time, must be a future time in milli seconds. if cycleType=MONTH, the firstDeductTime is not allowed to pass the date after the 28th UTC (can pass the 28th)                                                                                                                                                       |
| **merchantAccountNo**    | string   | N            | maximum length 64                                                              | the userID/user account in merchant side e.g. xxx@gmail.com                                                                                                                                                                                                                                                                                                   |
| **requestExpireTime**    | long     | N            | -                                                                              | If not specified, requestExpireTime will be 1 hour. maximum is 1 hour in milliseconds.                                                                                                                                                                                                                                                                        |
| **contractEndTime**      | long     | N            | -                                                                              | If not specified, contractEndTime will be the time after 1095 days (about 3 years). maximum is 1095 days in milliseconds.                                                                                                                                                                                                                                     |
| **returnUrl**            | string   | N            | maximum length 256                                                             | The URL to redirect to when the contract is signed successfully. **Only available to whitelisted merchant.**                                                                                                                                                                                                                                                  |
| **cancelUrl**            | string   | N            | maximum length 256                                                             | The URL to redirect to when the contract signing fails. **Only available to whitelisted merchant.** ｜                                                                                                                                                                                                                                                        |

### scenario-code

| **Scenario Code**          | **Default Upper limit** |
| -------------------------- | ----------------------- |
| General_Ecommerce_Platform | 50 USD equivalent       |
| General_Travel             | 50 USD equivalent       |
| Car_Rental                 | 50 USD equivalent       |
| Car_Parking                | 50 USD equivalent       |
| Lease                      | 50 USD equivalent       |
| Catering                   | 50 USD equivalent       |
| Digital_Media              | 50 USD equivalent       |
| Membership                 | 50 USD equivalent       |
| Utility                    | 50 USD equivalent       |
| Repayment                  | 50 USD equivalent       |
| Investment                 | 50 USD equivalent       |
| Ticket                     | 50 USD equivalent       |
| Mobile_Communication       | 50 USD equivalent       |
| Virtual_Goods              | 50 USD equivalent       |
| Others                     | 50 USD equivalent       |

### Sample Request Body

```json
{
  "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5",
  "serviceName": "Tra Direct Debit",
  "scenarioCode": "Membership",
  "currency": "USDT",
  "singleUpperLimit": "30",
  "periodic": true,
  "cycleDebitFixed": true,
  "cycleType": "DAY",
  "cycleValue": 8,
  "firstDeductTime": 1677628800000,
  "merchantAccountNo": "sss@gmail.com"
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

| **Attributes**        | **Type** | **Required** | **Limitation**     | **Description**                               |
| --------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **merchantId**        | Long     | Y            | number             | merchant Id in binance                        |
| **preContractId**     | string   | Y            | maximum length 19  | unique id generated by binance                |
| **contractEndTime**   | long     | Y            | -                  | contract will be expired at this time         |
| **requestExpireTime** | long     | Y            | -                  | user can not sign contract after this time    |
| **qrContent**         | string   | Y            | maximum length 256 | qr content info                               |
| **qrcodeLink**        | string   | Y            | maximum length 256 | qr code img link                              |
| **deeplink**          | string   | Y            | maximum length 256 | deeplink to open binance app to sign contract |

### Sample Response

#### applied success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "merchantId": 1000000002,
    "preContractId": "203616506788478976",
    "requestExpireTime": 1672656724308,
    "contractEndTime": 1767261124308,
    "qrContent": "https://app.binance.com/qr/xxx",
    "qrcodeLink": "https://public.bnbstatic.com/static/payment/20230405/xxx.jpg",
    "deeplink": "bnc://app.binance.com/mp/app?appId=V6tETccUyFTfoyMsGYH6aK&startPagePath=cGFnZXMvY29udHJhY3Qtc2lnbi9pbmRleA&startPageQuery=cHJlQ29udHJhY3RJZD0yMDM2MTY1MDY3ODg0Nzg5NzY="
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                      | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                                 | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                               | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                             | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                             | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                         | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                               | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                               | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                      | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                          | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED            | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH                    | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE                     | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR                    | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| PAYMENT_INVALID_PARAM                         | 400702   | Invalid request parameter                                                      |                                                                                                |
| MERCHANT_ACCESS_FORBIDDEN                     | 400606   | Account has no accessibility to this function                                  |                                                                                                |
| INVALID_REQUEST_CURRENCY_NOT_SUPPORTED        | 400105   | Invalid request, currency is not supported                                     |                                                                                                |
| PAYMENT_DIRECT_DEBIT_EXCEED_LIMIT             | 406200   | The singleUpperLimit exceed direct debit limit                                 |                                                                                                |
| PAYMENT_DIRECT_DEBIT_CONTRACT_CODE_INVALID    | 406201   | merchantContractCode is invalid or duplicated                                  |                                                                                                |
| PAYMENT_DIRECT_DEBIT_AMOUNT_PRECISION_INVALID | 406202   | The singleUpperLimit precision is not valid                                    |                                                                                                |

---

# Direct Debit/Pre Authorization Create Contract

This API is for merchant/partner to create direct debit/ pre authorization contract for user
authorization.

- This API is only available for whitelisted merchants. You may apply for direct debit on the
  [merchant dashboard](https://merchant.binance.com/en/dashboard/debit-management) under Products >
  Debit Management. Alternatively, you may contact us at merchant@binance.com, along with your
  Merchant ID, background and use case.

## EndPoint

```http request
POST /binancepay/openapi/direct-debit/contract
```

## Request Parameters

| **Attributes**           | **Type** | **Required** | **Limitation**                                                                 | **Description**                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | -------- | ------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**        | string   | N            | maximum length 19                                                              | The sub merchant account id, issued when sub merchant been created at Binance.                                                                                                                                                                                                                                                                                |
| **merchantContractCode** | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                    | The unique ID assigned by the merchant to identify a direct debit contract request.                                                                                                                                                                                                                                                                           |
| **serviceName**          | string   | Y            | maximum length 32                                                              | service name                                                                                                                                                                                                                                                                                                                                                  |
| **scenarioCode**         | string   | Y            | eg. General_Travel, for more please [refer to](#scenario-code)                 |
| **singleUpperLimit**     | decimal  | Y            | Max Unit Range: 8 decimal places                                               | upper limit related to scenarioCode, for more please [refer to](#scenario-code)                                                                                                                                                                                                                                                                               |
| **currency**             | string   | Y            | only "USDT" or "USDC" is accepted and "USDC" for mica user, fiat not supported | Order currency also the settlement currency                                                                                                                                                                                                                                                                                                                   |
| **periodic**             | boolean  | Y            | true/false                                                                     | this contract support periodic debit or not                                                                                                                                                                                                                                                                                                                   |
| **cycleDebitFixed**      | boolean  | N            | true/false                                                                     | mandatory if periodic = true. true = fixed amount, false = variable amount                                                                                                                                                                                                                                                                                    |
| **cycleType**            | string   | N            | MONTH or DAY                                                                   | mandatory if periodic = true. Values: MONTH or DAY                                                                                                                                                                                                                                                                                                            |
| **cycleValue**           | integer  | N            | -                                                                              | mandatory if periodic = true. Values: if cycleType=MONTH: 1~24, cycleType=DAY: interval days >7 <br/><br/> Combining with another parameter cycleType to determine the deduction period, for example, cycleType is DAY, cycleValue=30, then the deduction period is 30 days; cycleType is MONTH, cycleValue=3, then the deduction period is 3 natural months. |
| **firstDeductTime**      | long     | N            | -                                                                              | mandatory if periodic = true. first deduct time, must be a future time in milli seconds. if cycleType=MONTH, the firstDeductTime is not allowed to pass the date after the 28th UTC (can pass the 28th)                                                                                                                                                       |
| **merchantAccountNo**    | string   | N            | maximum length 64                                                              | the userID/user account in merchant side e.g. xxx@gmail.com                                                                                                                                                                                                                                                                                                   |
| **requestExpireTime**    | long     | N            | -                                                                              | If not specified, requestExpireTime will be 1 hour. maximum is 1 hour in milliseconds.                                                                                                                                                                                                                                                                        |
| **contractEndTime**      | long     | N            | -                                                                              | If not specified, contractEndTime will be the time after 1095 days (about 3 years). maximum is 1095 days in milliseconds.                                                                                                                                                                                                                                     |
| **returnUrl**            | string   | N            | maximum length 256                                                             | The URL to redirect to when the contract is signed successfully. **Only available to whitelisted merchant.**                                                                                                                                                                                                                                                  |
| **cancelUrl**            | string   | N            | maximum length 256                                                             | The URL to redirect to when the contract signing fails. **Only available to whitelisted merchant.** ｜                                                                                                                                                                                                                                                        |

### scenario-code

| **Scenario Code**          | **Default Upper limit** |
| -------------------------- | ----------------------- |
| General_Ecommerce_Platform | 50 USD equivalent       |
| General_Travel             | 50 USD equivalent       |
| Car_Rental                 | 50 USD equivalent       |
| Car_Parking                | 50 USD equivalent       |
| Lease                      | 50 USD equivalent       |
| Catering                   | 50 USD equivalent       |
| Digital_Media              | 50 USD equivalent       |
| Membership                 | 50 USD equivalent       |
| Utility                    | 50 USD equivalent       |
| Repayment                  | 50 USD equivalent       |
| Investment                 | 50 USD equivalent       |
| Ticket                     | 50 USD equivalent       |
| Mobile_Communication       | 50 USD equivalent       |
| Virtual_Goods              | 50 USD equivalent       |
| Others                     | 50 USD equivalent       |

### Sample Request Body

```json
{
  "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5",
  "serviceName": "Tra Direct Debit",
  "scenarioCode": "Membership",
  "currency": "USDT",
  "singleUpperLimit": "30",
  "periodic": true,
  "cycleDebitFixed": true,
  "cycleType": "DAY",
  "cycleValue": 8,
  "firstDeductTime": 1677628800000,
  "merchantAccountNo": "sss@gmail.com"
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

| **Attributes**        | **Type** | **Required** | **Limitation**     | **Description**                               |
| --------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **merchantId**        | Long     | Y            | number             | merchant Id in binance                        |
| **preContractId**     | string   | Y            | maximum length 19  | unique id generated by binance                |
| **contractEndTime**   | long     | Y            | -                  | contract will be expired at this time         |
| **requestExpireTime** | long     | Y            | -                  | user can not sign contract after this time    |
| **qrContent**         | string   | Y            | maximum length 256 | qr content info                               |
| **qrcodeLink**        | string   | Y            | maximum length 256 | qr code img link                              |
| **deeplink**          | string   | Y            | maximum length 256 | deeplink to open binance app to sign contract |

### Sample Response

#### applied success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "merchantId": 1000000002,
    "preContractId": "203616506788478976",
    "requestExpireTime": 1672656724308,
    "contractEndTime": 1767261124308,
    "qrContent": "https://app.binance.com/qr/xxx",
    "qrcodeLink": "https://public.bnbstatic.com/static/payment/20230405/xxx.jpg",
    "deeplink": "bnc://app.binance.com/mp/app?appId=V6tETccUyFTfoyMsGYH6aK&startPagePath=cGFnZXMvY29udHJhY3Qtc2lnbi9pbmRleA&startPageQuery=cHJlQ29udHJhY3RJZD0yMDM2MTY1MDY3ODg0Nzg5NzY="
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                      | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                                 | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                               | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                             | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                             | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                         | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                               | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                               | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                      | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                          | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED            | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH                    | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE                     | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR                    | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| PAYMENT_INVALID_PARAM                         | 400702   | Invalid request parameter                                                      |                                                                                                |
| MERCHANT_ACCESS_FORBIDDEN                     | 400606   | Account has no accessibility to this function                                  |                                                                                                |
| INVALID_REQUEST_CURRENCY_NOT_SUPPORTED        | 400105   | Invalid request, currency is not supported                                     |                                                                                                |
| PAYMENT_DIRECT_DEBIT_EXCEED_LIMIT             | 406200   | The singleUpperLimit exceed direct debit limit                                 |                                                                                                |
| PAYMENT_DIRECT_DEBIT_CONTRACT_CODE_INVALID    | 406201   | merchantContractCode is invalid or duplicated                                  |                                                                                                |
| PAYMENT_DIRECT_DEBIT_AMOUNT_PRECISION_INVALID | 406202   | The singleUpperLimit precision is not valid                                    |                                                                                                |