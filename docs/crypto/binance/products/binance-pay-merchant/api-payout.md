---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-payout
api_type: Guide
updated_at: 2026-11-24 18:34:27.688300
---

# Batch Payout

Payout API used for Merchant/Partner to make transfers in batch.

Please refer to
[Merchant Fee Schedule](https://www.binance.com/en/support/faq/detail/6ff1944867e54b9a9576bce3109c7f7a) -
[Merchant] tab, for more information on merchant fees.

## EndPoint

```http request
POST /binancepay/openapi/payout/transfer
```

## Request Parameters

| **Attributes**         | **Type**                | **Required** | **Limitation**                                                                 | **Description**                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**          | string                  | Y            | Maximum length 32                                                              | The unique ID assigned by the merchant to identify a payout request.                                                                                                                                                                                                                                                                      |
| **bizScene**           | string                  | N            | Enum value                                                                     | Describe the business scene of this payout. Limited to: <br /> <br /> **DIRECT_TRANSFER**: the default value <br /> **CRYPTO_REWARDS**: gift or rewards payout <br /> **SETTLEMENT**: settlement or commission fee <br /> **REIMBURSEMENT**: reimburse employees <br /> **MERCHANT_PAYMENT**: payment to partners/users <br /> **OTHERS** |
| **batchName**          | string                  | Y            | Maximum length 32                                                              | The name of the batch payout.                                                                                                                                                                                                                                                                                                             |
| **currency**           | string                  | Y            | Crypto token only, fiat NOT supported. All characters must be in **uppercase** | All the transfers under this batch must use the same currency.                                                                                                                                                                                                                                                                            |
| **totalAmount**        | decimal                 | Y            | limitation refer to Create Order API order amount                              | It must be equal to the sum of all the detail transfers.                                                                                                                                                                                                                                                                                  |
| **totalNumber**        | int                     | Y            | Maximum value 500                                                              | The total number of transfers. It must be equal to the detail transfer count.                                                                                                                                                                                                                                                             |
| **transferDetailList** | list[TransferDetailReq] | Y            | Maximum size 500                                                               | Detail transfer list                                                                                                                                                                                                                                                                                                                      |
| **webhookUrl**         | string                  | N            | maximum length 256. Can only start with http or https.                         | The URL for [Payout webhook notification](webhook-payout). If `webhookUrl` is passed, the webhook URL configured on the Merchant Management Platform will not take effect, and the URL passed here will be called back first. Useful for CPs / merchants that maintain multiple endpoints.                                                |

## Child Attribute

### TransferDetailReq

| **Attributes**               | **Type** | **Required**                                           | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **merchantSendId**           | string   | Y                                                      | Maximum length 32  | The unique ID assigned by the merchant to identify a detail transfer.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **receiveType**              | string   | Y                                                      | Enum value         | Receiver's ID type <br /><br /> **BINANCE_ID**: Binance user ID.<br /> **EMAIL**: Binance user email address, support payout to non-binance users <br /> **\*Support Payout to non-binance user email for whitelisted merchant** <br /> **OPEN_ID**: Mini App / OAuth user openId. Use this to pay out to a user authorized via your OAuth / Mini App `clientId` without exposing their Binance ID. `clientId` is required when this type is used.                                                  |
| **receiver**                 | string   | Y                                                      |                    | Receiver's BINANCE_ID / EMAIL / openId, depending on the `receiveType`.<br /> **Note**: <br />- If it is a non-binance user email address, he or she needs to register a binance account to receive the payout. <br />- The amount will be automatically refunded to your wallet if receivers haven't completed the registration within 72 hours. <br />- When `receiveType=OPEN_ID`, pass the user's openId (the same one returned by OAuth / Mini App login) and provide the matching `clientId`. |
| **clientId**                 | string   | Conditional – required only when `receiveType=OPEN_ID` |                    | The OAuth / Mini App `clientId` that the openId was issued under. Binance Pay uses (`clientId`, `openId`) to look up the receiver's Binance account. The openId is rejected if it does not belong to this `clientId`.                                                                                                                                                                                                                                                                               |
| **transferAmount**           | decimal  | Y                                                      |                    | Transfer amount maximum is at 80K USD equivalent                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **transferMethod**           | string   | Y                                                      | Enum string        | Wallet to be used. Currently support: <br /> <br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** <br /> **FUNDING_AND_SPOT_WALLET**                                                                                                                                                                                                                                                                                                                                                                    |
| **remark**                   | String   | N                                                      | Maximum length 128 | Remark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **subMerchantId**            | String   | Conditional – required only for Channel Partners       | Maximum length 32  | Unique identifier assigned to the sub-merchant by Binance Pay. This field must be provided when the request is initiated by a Channel Partner; direct merchants should leave it blank. <br /> **Note: If you’re a Channel Partner and you’re placing orders for your own business, you need to create a separate sub-merchant id and pass it accordingly**                                                                                                                                          |
| **registrationEmail**        | String   | N                                                      |                    | Receiver's registration email address                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **registrationMobileNumber** | String   | N                                                      |                    | Receiver's mobile number                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **registrationMobileCode**   | String   | N                                                      |                    | Receiver's mobile code eg:971 for UAE                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Sample Request Body

```json
{
  "requestId": "samplerequest1234",
  "batchName": "sample batch test",
  "currency": "USDT",
  "totalAmount": 200.4,
  "totalNumber": 2,
  "bizScene": "SETTLEMENT",
  "webhookUrl": "https://www.example.com/payout/notify",

  "transferDetailList": [
    {
      "merchantSendId": "22231313131",
      "transferAmount": 110.3,
      "receiveType": "BINANCE_ID",
      "transferMethod": "SPOT_WALLET",
      "receiver": "400000001",
      "remark": "test1"
    },

    {
      "merchantSendId": "21231313132",
      "transferAmount": 90.1,
      "receiveType": "BINANCE_ID",
      "transferMethod": "SPOT_WALLET",
      "receiver": "400000002",
      "remark": "test2"
    }
  ]
}
```

### Sample Request Body — Payout to Mini App user via OPEN_ID

```json
{
  "requestId": "samplerequest1235",
  "batchName": "mini app payout",
  "currency": "USDT",
  "totalAmount": 5,
  "totalNumber": 1,
  "bizScene": "CRYPTO_REWARDS",

  "transferDetailList": [
    {
      "merchantSendId": "openid-detail-001",
      "transferAmount": 5,
      "receiveType": "OPEN_ID",
      "receiver": "your-mini-app-user-open-id",
      "clientId": "your-oauth-client-id",
      "transferMethod": "FUNDING_WALLET",
      "remark": "mini app reward"
    }
  ]
}
```

## Response Parameters

| **Attributes**   | **Type**               | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string                 | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string                 | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | PayoutTransferResponse | N            | -                                   | response body, [refer to](#payout-response)    |
| **errorMessage** | string                 | N            | maximum length 256                  |                                                |

## Child Attribute

### PayoutTransferResponse

<span id="payout-response"></span>

| **Attributes** | **Type** | **Required** | **Limitation**    | **Description**                                                                    |
| -------------- | -------- | ------------ | ----------------- | ---------------------------------------------------------------------------------- |
| **requestId**  | string   | Y            | Maximum length 32 | The passed-in request ID.No special characters allowed, only numbers and alphabet. |
| **status**     | string   | Y            | Enum string       | **ACCEPTED**: accepted the request, will process it soon                           |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "requestId": "samplerequest1234",
    "status": "ACCEPTED"
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

| **Name**                                | **Code** | **Reason**                                                                                                             | **Solution**                                                                                   |
| --------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                                                                | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.                                          | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                                                             | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                                                              | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                                                                 | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                                                                       | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                                                          | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                                                              | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                                                               | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                                                                      |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.                                         |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                                                                  |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters.                                                                |                                                                                                |
| INVALID_REQUEST_TOO_LARGE               | 400104   | Invalid request, content length too large.                                                                             |                                                                                                |
| INVALID_REQUEST_CURRENCY_NOT_SUPPORTED  | 400105   | Invalid request, the transfer currency is not supported or not in upper case.                                          |                                                                                                |
| PAYMENT_ACTION_TOO_FREQUENT             | 400501   | action Too Frequent, get the lock fail                                                                                 | Try again later                                                                                |
| PAYMENT_ILLEGAL_AMOUNT                  | 400701   | The amount is illegal, too small or too large                                                                          |                                                                                                |
| PAYMENT_INVALID_PARAM                   | 400702   | Invalid request parameter                                                                                              |                                                                                                |
| PAYMENT_C2C_RECEIVER_ACCOUNT_NOT_FOUND  | 400703   | Payee not found                                                                                                        |                                                                                                |
| PAYEE_ACCOUNT_LOCKED                    | 400704   | Payee account is locked                                                                                                |                                                                                                |
| PAYEE_ACCOUNT_FROZEN                    | 400705   | payee account is frozen                                                                                                |                                                                                                |
| PAYMENT_C2C_RECEIVER_ACCOUNT_INVALID    | 400706   | Payee status invalid                                                                                                   |                                                                                                |
| PAYMENT_EXCEED_MERCHANT_DAILY_LIMIT     | 400707   | Exceeds merchant's payment daily limit in USD.                                                                         |                                                                                                |
| PAYMENT_EXCEED_MERCHANT_ANNUAL_LIMIT    | 400708   | Exceeds merchant's payment annual limit in USD.                                                                        |                                                                                                |
| USER_IN_BLOCK_KYC                       | 400709   | Payee is unable to access Binance due to his/her residential region, you will not be able to proceed with the payment. |                                                                                                |
| PAYEE_KYC_NOT_PASSED                    | 400710   | We are unable to initiate the transfer as payee has not completed identity verification.                               |                                                                                                |
| RISK_HIT_REJECTED                       | 400711   | The deal is rejected and there may be risks in the current transaction                                                 |                                                                                                |
| PAYMENT_RECEIVER_EXCEED_RECEIVE_LIMIT   | 400712   | Recipient has exceeded fund receiving limit.                                                                           |                                                                                                |
| PAYMENT_C2C_HIT_RISK_RULE               | 400713   | The deal is rejected and there may be risks in the current transaction                                                 |                                                                                                |
| USER_IN_BLACK_KYC                       | 400714   | user in black kyc                                                                                                      |                                                                                                |
| USER_IN_BLACK_IP_AND_NO_KYC             | 400715   | user in black ip and no kyc                                                                                            |                                                                                                |
| USER_IN_BLACK_IP_AND_KYC                | 400716   | user in black ip                                                                                                       |                                                                                                |
| USER_IN_BLACK_DEVICE_RELATION           | 400717   | user in black device relation                                                                                          |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_KYC            | 400718   | user in black kyc                                                                                                      |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_IP_AND_NO_KYC  | 400719   | user in black ip and no kyc                                                                                            |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_IP_AND_KYC     | 400720   | user in black ip                                                                                                       |                                                                                                |
| KYC_NOT_PASSED                          | 400721   | kyc not passed                                                                                                         |                                                                                                |
| KYC_NOT_COMPLETED                       | 400722   | kyc not completed                                                                                                      |                                                                                                |
| KYC_AUDITING                            | 400723   | kyc auditing                                                                                                           |                                                                                                |
| KYC_SERVER_PUBLISHING                   | 400724   | kyc server publishing                                                                                                  |                                                                                                |
| MERCHANT_TRANSFER_SAME_ACCOUNT          | 406101   | Receiver account cannot be same with payer                                                                             |                                                                                                |
| MERCHANT_TRANSFER_INVALID_AMOUNT        | 406102   | Payout transfer amount must be greater than min usd                                                                    |                                                                                                |
| MERCHANT_TRANSFER_PAYEE_NOT_FOUND       | 406103   | payee account cannot be found in the system                                                                            |                                                                                                |
| MERCHANT_TRANSFER_CURRENCY_NOT_SUPPORT  | 406104   | Invalid request, currency is not supported                                                                             |                                                                                                |
| MERCHANT_TRANSFER_PAYEE_CANNOT_SUB_USER | 406105   | Receiver account cannot be a sub user                                                                                  |                                                                                                |
| MERCHANT_TRANSFER_RECEIVER_INVALID      | 406106   | Receiver account info is not valid, please check again                                                                 |                                                                                                |

---

# Batch Payout

Payout API used for Merchant/Partner to make transfers in batch.

Please refer to
[Merchant Fee Schedule](https://www.binance.com/en/support/faq/detail/6ff1944867e54b9a9576bce3109c7f7a) -
[Merchant] tab, for more information on merchant fees.

## EndPoint

```http request
POST /binancepay/openapi/payout/transfer
```

## Request Parameters

| **Attributes**         | **Type**                | **Required** | **Limitation**                                                                 | **Description**                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**          | string                  | Y            | Maximum length 32                                                              | The unique ID assigned by the merchant to identify a payout request.                                                                                                                                                                                                                                                                      |
| **bizScene**           | string                  | N            | Enum value                                                                     | Describe the business scene of this payout. Limited to: <br /> <br /> **DIRECT_TRANSFER**: the default value <br /> **CRYPTO_REWARDS**: gift or rewards payout <br /> **SETTLEMENT**: settlement or commission fee <br /> **REIMBURSEMENT**: reimburse employees <br /> **MERCHANT_PAYMENT**: payment to partners/users <br /> **OTHERS** |
| **batchName**          | string                  | Y            | Maximum length 32                                                              | The name of the batch payout.                                                                                                                                                                                                                                                                                                             |
| **currency**           | string                  | Y            | Crypto token only, fiat NOT supported. All characters must be in **uppercase** | All the transfers under this batch must use the same currency.                                                                                                                                                                                                                                                                            |
| **totalAmount**        | decimal                 | Y            | limitation refer to Create Order API order amount                              | It must be equal to the sum of all the detail transfers.                                                                                                                                                                                                                                                                                  |
| **totalNumber**        | int                     | Y            | Maximum value 500                                                              | The total number of transfers. It must be equal to the detail transfer count.                                                                                                                                                                                                                                                             |
| **transferDetailList** | list[TransferDetailReq] | Y            | Maximum size 500                                                               | Detail transfer list                                                                                                                                                                                                                                                                                                                      |
| **webhookUrl**         | string                  | N            | maximum length 256. Can only start with http or https.                         | The URL for [Payout webhook notification](webhook-payout). If `webhookUrl` is passed, the webhook URL configured on the Merchant Management Platform will not take effect, and the URL passed here will be called back first. Useful for CPs / merchants that maintain multiple endpoints.                                                |

## Child Attribute

### TransferDetailReq

| **Attributes**               | **Type** | **Required**                                           | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **merchantSendId**           | string   | Y                                                      | Maximum length 32  | The unique ID assigned by the merchant to identify a detail transfer.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **receiveType**              | string   | Y                                                      | Enum value         | Receiver's ID type <br /><br /> **BINANCE_ID**: Binance user ID.<br /> **EMAIL**: Binance user email address, support payout to non-binance users <br /> **\*Support Payout to non-binance user email for whitelisted merchant** <br /> **OPEN_ID**: Mini App / OAuth user openId. Use this to pay out to a user authorized via your OAuth / Mini App `clientId` without exposing their Binance ID. `clientId` is required when this type is used.                                                  |
| **receiver**                 | string   | Y                                                      |                    | Receiver's BINANCE_ID / EMAIL / openId, depending on the `receiveType`.<br /> **Note**: <br />- If it is a non-binance user email address, he or she needs to register a binance account to receive the payout. <br />- The amount will be automatically refunded to your wallet if receivers haven't completed the registration within 72 hours. <br />- When `receiveType=OPEN_ID`, pass the user's openId (the same one returned by OAuth / Mini App login) and provide the matching `clientId`. |
| **clientId**                 | string   | Conditional – required only when `receiveType=OPEN_ID` |                    | The OAuth / Mini App `clientId` that the openId was issued under. Binance Pay uses (`clientId`, `openId`) to look up the receiver's Binance account. The openId is rejected if it does not belong to this `clientId`.                                                                                                                                                                                                                                                                               |
| **transferAmount**           | decimal  | Y                                                      |                    | Transfer amount maximum is at 80K USD equivalent                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **transferMethod**           | string   | Y                                                      | Enum string        | Wallet to be used. Currently support: <br /> <br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** <br /> **FUNDING_AND_SPOT_WALLET**                                                                                                                                                                                                                                                                                                                                                                    |
| **remark**                   | String   | N                                                      | Maximum length 128 | Remark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **subMerchantId**            | String   | Conditional – required only for Channel Partners       | Maximum length 32  | Unique identifier assigned to the sub-merchant by Binance Pay. This field must be provided when the request is initiated by a Channel Partner; direct merchants should leave it blank. <br /> **Note: If you’re a Channel Partner and you’re placing orders for your own business, you need to create a separate sub-merchant id and pass it accordingly**                                                                                                                                          |
| **registrationEmail**        | String   | N                                                      |                    | Receiver's registration email address                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **registrationMobileNumber** | String   | N                                                      |                    | Receiver's mobile number                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **registrationMobileCode**   | String   | N                                                      |                    | Receiver's mobile code eg:971 for UAE                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Sample Request Body

```json
{
  "requestId": "samplerequest1234",
  "batchName": "sample batch test",
  "currency": "USDT",
  "totalAmount": 200.4,
  "totalNumber": 2,
  "bizScene": "SETTLEMENT",
  "webhookUrl": "https://www.example.com/payout/notify",

  "transferDetailList": [
    {
      "merchantSendId": "22231313131",
      "transferAmount": 110.3,
      "receiveType": "BINANCE_ID",
      "transferMethod": "SPOT_WALLET",
      "receiver": "400000001",
      "remark": "test1"
    },

    {
      "merchantSendId": "21231313132",
      "transferAmount": 90.1,
      "receiveType": "BINANCE_ID",
      "transferMethod": "SPOT_WALLET",
      "receiver": "400000002",
      "remark": "test2"
    }
  ]
}
```

### Sample Request Body — Payout to Mini App user via OPEN_ID

```json
{
  "requestId": "samplerequest1235",
  "batchName": "mini app payout",
  "currency": "USDT",
  "totalAmount": 5,
  "totalNumber": 1,
  "bizScene": "CRYPTO_REWARDS",

  "transferDetailList": [
    {
      "merchantSendId": "openid-detail-001",
      "transferAmount": 5,
      "receiveType": "OPEN_ID",
      "receiver": "your-mini-app-user-open-id",
      "clientId": "your-oauth-client-id",
      "transferMethod": "FUNDING_WALLET",
      "remark": "mini app reward"
    }
  ]
}
```

## Response Parameters

| **Attributes**   | **Type**               | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string                 | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string                 | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | PayoutTransferResponse | N            | -                                   | response body, [refer to](#payout-response)    |
| **errorMessage** | string                 | N            | maximum length 256                  |                                                |

## Child Attribute

### PayoutTransferResponse

<span id="payout-response"></span>

| **Attributes** | **Type** | **Required** | **Limitation**    | **Description**                                                                    |
| -------------- | -------- | ------------ | ----------------- | ---------------------------------------------------------------------------------- |
| **requestId**  | string   | Y            | Maximum length 32 | The passed-in request ID.No special characters allowed, only numbers and alphabet. |
| **status**     | string   | Y            | Enum string       | **ACCEPTED**: accepted the request, will process it soon                           |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "requestId": "samplerequest1234",
    "status": "ACCEPTED"
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

| **Name**                                | **Code** | **Reason**                                                                                                             | **Solution**                                                                                   |
| --------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                                                                | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.                                          | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                                                             | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                                                              | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                                                                 | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                                                                       | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                                                          | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                                                              | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                                                               | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                                                                      |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format.                                         |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                                                                  |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters.                                                                |                                                                                                |
| INVALID_REQUEST_TOO_LARGE               | 400104   | Invalid request, content length too large.                                                                             |                                                                                                |
| INVALID_REQUEST_CURRENCY_NOT_SUPPORTED  | 400105   | Invalid request, the transfer currency is not supported or not in upper case.                                          |                                                                                                |
| PAYMENT_ACTION_TOO_FREQUENT             | 400501   | action Too Frequent, get the lock fail                                                                                 | Try again later                                                                                |
| PAYMENT_ILLEGAL_AMOUNT                  | 400701   | The amount is illegal, too small or too large                                                                          |                                                                                                |
| PAYMENT_INVALID_PARAM                   | 400702   | Invalid request parameter                                                                                              |                                                                                                |
| PAYMENT_C2C_RECEIVER_ACCOUNT_NOT_FOUND  | 400703   | Payee not found                                                                                                        |                                                                                                |
| PAYEE_ACCOUNT_LOCKED                    | 400704   | Payee account is locked                                                                                                |                                                                                                |
| PAYEE_ACCOUNT_FROZEN                    | 400705   | payee account is frozen                                                                                                |                                                                                                |
| PAYMENT_C2C_RECEIVER_ACCOUNT_INVALID    | 400706   | Payee status invalid                                                                                                   |                                                                                                |
| PAYMENT_EXCEED_MERCHANT_DAILY_LIMIT     | 400707   | Exceeds merchant's payment daily limit in USD.                                                                         |                                                                                                |
| PAYMENT_EXCEED_MERCHANT_ANNUAL_LIMIT    | 400708   | Exceeds merchant's payment annual limit in USD.                                                                        |                                                                                                |
| USER_IN_BLOCK_KYC                       | 400709   | Payee is unable to access Binance due to his/her residential region, you will not be able to proceed with the payment. |                                                                                                |
| PAYEE_KYC_NOT_PASSED                    | 400710   | We are unable to initiate the transfer as payee has not completed identity verification.                               |                                                                                                |
| RISK_HIT_REJECTED                       | 400711   | The deal is rejected and there may be risks in the current transaction                                                 |                                                                                                |
| PAYMENT_RECEIVER_EXCEED_RECEIVE_LIMIT   | 400712   | Recipient has exceeded fund receiving limit.                                                                           |                                                                                                |
| PAYMENT_C2C_HIT_RISK_RULE               | 400713   | The deal is rejected and there may be risks in the current transaction                                                 |                                                                                                |
| USER_IN_BLACK_KYC                       | 400714   | user in black kyc                                                                                                      |                                                                                                |
| USER_IN_BLACK_IP_AND_NO_KYC             | 400715   | user in black ip and no kyc                                                                                            |                                                                                                |
| USER_IN_BLACK_IP_AND_KYC                | 400716   | user in black ip                                                                                                       |                                                                                                |
| USER_IN_BLACK_DEVICE_RELATION           | 400717   | user in black device relation                                                                                          |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_KYC            | 400718   | user in black kyc                                                                                                      |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_IP_AND_NO_KYC  | 400719   | user in black ip and no kyc                                                                                            |                                                                                                |
| COMPLIANCE_USER_IN_BLACK_IP_AND_KYC     | 400720   | user in black ip                                                                                                       |                                                                                                |
| KYC_NOT_PASSED                          | 400721   | kyc not passed                                                                                                         |                                                                                                |
| KYC_NOT_COMPLETED                       | 400722   | kyc not completed                                                                                                      |                                                                                                |
| KYC_AUDITING                            | 400723   | kyc auditing                                                                                                           |                                                                                                |
| KYC_SERVER_PUBLISHING                   | 400724   | kyc server publishing                                                                                                  |                                                                                                |
| MERCHANT_TRANSFER_SAME_ACCOUNT          | 406101   | Receiver account cannot be same with payer                                                                             |                                                                                                |
| MERCHANT_TRANSFER_INVALID_AMOUNT        | 406102   | Payout transfer amount must be greater than min usd                                                                    |                                                                                                |
| MERCHANT_TRANSFER_PAYEE_NOT_FOUND       | 406103   | payee account cannot be found in the system                                                                            |                                                                                                |
| MERCHANT_TRANSFER_CURRENCY_NOT_SUPPORT  | 406104   | Invalid request, currency is not supported                                                                             |                                                                                                |
| MERCHANT_TRANSFER_PAYEE_CANNOT_SUB_USER | 406105   | Receiver account cannot be a sub user                                                                                  |                                                                                                |
| MERCHANT_TRANSFER_RECEIVER_INVALID      | 406106   | Receiver account info is not valid, please check again                                                                 |                                                                                                |