---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-payout-query
api_type: Guide
updated_at: 2026-11-27 18:34:34.562517
---

# Payout Query

Payout query API used for Merchant/Partner to query transfer status.

## EndPoint

```http request
POST /binancepay/openapi/payout/query
```

## Request Parameters

| **Attributes**   | **Type**     | **Required** | **Limitation**    | **Description**                                                                                                                                                                                                       |
| ---------------- | ------------ | ------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**    | string       | Y            | Maximum length 32 | The unique ID assigned by the merchant to identify a payout request.                                                                                                                                                  |
| **detailStatus** | list[string] | N            | Enum string list  | **ALL**: return all transfer details, default value. <br /> **PROCESSING**: only return transfers in processing. <br /> **SUCCESS**: only return successful transfers. <br /> **FAIL**: only return failed transfers. |

### Sample Request Body

```json
{
  "requestId": "payouttransfer19998"
}
```

## Response Parameters

| **Attributes**   | **Type**            | **Required** | **Limitation**                      | **Description**                                   |
| ---------------- | ------------------- | ------------ | ----------------------------------- | ------------------------------------------------- |
| **status**       | string              | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                         |
| **code**         | string              | Y            | -                                   | request result code, [refer to ](#result-code)    |
| **data**         | TransferQueryResult | N            | -                                   | response body, [refer to](#payout-query-response) |
| **errorMessage** | string              | N            | maximum length 256                  |                                                   |

## Child Attribute

### TransferQueryResult

<span id="payout-query-response"></span>

| **Attributes**         | **Type**             | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------- | -------------------- | ------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**          | string               | Y            | Maximum length 32                                 | The passed-in request ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **batchStatus**        | string               | Y            | Enum string                                       | **ACCEPTED**: accepted the request, will process it soon. <br /> **PROCESSING**: batch under processing <br /> **SUCCESS**: All payout performed successfully, user have received fund in Binance funding wallet <br /> **PART_SUCCESS**: transfers partially succeeded.<br /> Reasons: <br />1.Insufficient funds: there’s insufficient fund in your account <br /> 2.Awaiting recipient: pending user to create Binance account and perform KYC <br/> 3.Partial refund: user failed to complete KYC in 72 hours, fund will be funded to merchant account <br/> **FAILED**: all transfers failed <br /> **CANCELED**: Transfer request canceled by Binance due to unknown system errors after retry limit, will not retry further |
| **merchantId**         | long                 | Y            |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **currency**           | string               | Y            | Valid crypto currency                             | The request currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **totalAmount**        | decimal              | Y            | limitation refer to Create Order API order amount | Total transfer amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **totalPaidAmount**    | decimal              | Y            | limitation refer to Create Order API order amount | Total paid amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **totalPayoutFee**     | decimal              | Y            | limitation refer to Create Order API order amount | Total payout fee amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **totalNumber**        | int                  | Y            | Maximum length 1000                               | Total number of transfers in the batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **transferDetailList** | TransferDetailResult | Y            | Max size 1000                                     | Detail transfer result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Child Attribute

### TransferDetailResult

| **Attributes**      | **Type** | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                                                                                                                                               |
| ------------------- | -------- | ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **orderId**         | long     | Y            | Maximum length 32                                 | The passed-in request ID.                                                                                                                                                                                                                                                                                     |
| **merchantSendId**  | string   | Y            | Maximum length 32                                 | The passed-in merchantSendId.                                                                                                                                                                                                                                                                                 |
| **payerId**         | Long     | Y            |                                                   | Payer's payment account ID.                                                                                                                                                                                                                                                                                   |
| **amount**          | string   | Y            | limitation refer to Create Order API order amount | Amount transferred.                                                                                                                                                                                                                                                                                           |
| **payoutFee**       | string   | Y            | limitation refer to Create Order API order amount | Amount paid.                                                                                                                                                                                                                                                                                                  |
| **totalPaidAmount** | string   | Y            | limitation refer to Create Order API order amount | Payout Fee Amount .                                                                                                                                                                                                                                                                                           |
| **receiveType**     | string   | Y            | Enum string                                       | **PAY_ID** <br /> **BINANCE_ID**                                                                                                                                                                                                                                                                              |
| **receiver**        | string   | Y            | Maximum length 19                                 | Receiver ID from the request.                                                                                                                                                                                                                                                                                 |
| **payeeId**         | long     | Y            |                                                   | Receiver's payment account ID.                                                                                                                                                                                                                                                                                |
| **transferMethod**  | string   | Y            | Enum string                                       | **SPOT_WALLET** <br /> **FUNDING_WALLET** <br /> **FUNDING_AND_SPOT_WALLET**                                                                                                                                                                                                                                  |
| **status**          | string   | Y            | Enum string                                       | **SUCCESS:** money has been transferred successfully <br /> **FAIL**: transaction failed may case by there’s insufficient fund in your account <br /> **AWAITING_RECEIPT** pending new user create an binance account and pass KYC to receive money <br /> **REFUNDED:** new user hasn’t pass KYC in 72 hours |
| **remark**          | string   | N            |                                                   | Maximum length 128                                                                                                                                                                                                                                                                                            |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "requestId": "2222222111222",
    "batchStatus": "SUCCESS",
    "merchantId": 22222222,
    "currency": "USDC",
    "totalAmount": "114.00000000",
    "totalNumber": 1,
    "totalPaidAmount": "114.91200000",
    "totalPayoutFee": "0.912",
    "transferDetailList": [
      {
        "orderId": 349275283293014145,
        "merchantSendId": "22123",
        "payerId": 300000001,
        "amount": "114.00000000",
        "payoutFee": "0.912",
        "totalPaidAmount": "114.91200000",
        "receiveType": "BINANCE_ID",
        "receiver": "1111111",
        "payeeId": 11111111,
        "transferMethod": "SPOT_WALLET",
        "status": "SUCCESS",
        "remark": null
      }
    ]
  }
}
```

```json
{
  "status": "FAIL",
  "code": "403015",
  "errorMessage": "pay order not found"
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
| PAYMENT_PAY_ORDER_NOT_FOUND        | 400602   | Pay order not found                                                            |                                                                                                |

---

# Payout Query

Payout query API used for Merchant/Partner to query transfer status.

## EndPoint

```http request
POST /binancepay/openapi/payout/query
```

## Request Parameters

| **Attributes**   | **Type**     | **Required** | **Limitation**    | **Description**                                                                                                                                                                                                       |
| ---------------- | ------------ | ------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**    | string       | Y            | Maximum length 32 | The unique ID assigned by the merchant to identify a payout request.                                                                                                                                                  |
| **detailStatus** | list[string] | N            | Enum string list  | **ALL**: return all transfer details, default value. <br /> **PROCESSING**: only return transfers in processing. <br /> **SUCCESS**: only return successful transfers. <br /> **FAIL**: only return failed transfers. |

### Sample Request Body

```json
{
  "requestId": "payouttransfer19998"
}
```

## Response Parameters

| **Attributes**   | **Type**            | **Required** | **Limitation**                      | **Description**                                   |
| ---------------- | ------------------- | ------------ | ----------------------------------- | ------------------------------------------------- |
| **status**       | string              | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                         |
| **code**         | string              | Y            | -                                   | request result code, [refer to ](#result-code)    |
| **data**         | TransferQueryResult | N            | -                                   | response body, [refer to](#payout-query-response) |
| **errorMessage** | string              | N            | maximum length 256                  |                                                   |

## Child Attribute

### TransferQueryResult

<span id="payout-query-response"></span>

| **Attributes**         | **Type**             | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------- | -------------------- | ------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**          | string               | Y            | Maximum length 32                                 | The passed-in request ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **batchStatus**        | string               | Y            | Enum string                                       | **ACCEPTED**: accepted the request, will process it soon. <br /> **PROCESSING**: batch under processing <br /> **SUCCESS**: All payout performed successfully, user have received fund in Binance funding wallet <br /> **PART_SUCCESS**: transfers partially succeeded.<br /> Reasons: <br />1.Insufficient funds: there’s insufficient fund in your account <br /> 2.Awaiting recipient: pending user to create Binance account and perform KYC <br/> 3.Partial refund: user failed to complete KYC in 72 hours, fund will be funded to merchant account <br/> **FAILED**: all transfers failed <br /> **CANCELED**: Transfer request canceled by Binance due to unknown system errors after retry limit, will not retry further |
| **merchantId**         | long                 | Y            |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **currency**           | string               | Y            | Valid crypto currency                             | The request currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **totalAmount**        | decimal              | Y            | limitation refer to Create Order API order amount | Total transfer amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **totalPaidAmount**    | decimal              | Y            | limitation refer to Create Order API order amount | Total paid amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **totalPayoutFee**     | decimal              | Y            | limitation refer to Create Order API order amount | Total payout fee amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **totalNumber**        | int                  | Y            | Maximum length 1000                               | Total number of transfers in the batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **transferDetailList** | TransferDetailResult | Y            | Max size 1000                                     | Detail transfer result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Child Attribute

### TransferDetailResult

| **Attributes**      | **Type** | **Required** | **Limitation**                                    | **Description**                                                                                                                                                                                                                                                                                               |
| ------------------- | -------- | ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **orderId**         | long     | Y            | Maximum length 32                                 | The passed-in request ID.                                                                                                                                                                                                                                                                                     |
| **merchantSendId**  | string   | Y            | Maximum length 32                                 | The passed-in merchantSendId.                                                                                                                                                                                                                                                                                 |
| **payerId**         | Long     | Y            |                                                   | Payer's payment account ID.                                                                                                                                                                                                                                                                                   |
| **amount**          | string   | Y            | limitation refer to Create Order API order amount | Amount transferred.                                                                                                                                                                                                                                                                                           |
| **payoutFee**       | string   | Y            | limitation refer to Create Order API order amount | Amount paid.                                                                                                                                                                                                                                                                                                  |
| **totalPaidAmount** | string   | Y            | limitation refer to Create Order API order amount | Payout Fee Amount .                                                                                                                                                                                                                                                                                           |
| **receiveType**     | string   | Y            | Enum string                                       | **PAY_ID** <br /> **BINANCE_ID**                                                                                                                                                                                                                                                                              |
| **receiver**        | string   | Y            | Maximum length 19                                 | Receiver ID from the request.                                                                                                                                                                                                                                                                                 |
| **payeeId**         | long     | Y            |                                                   | Receiver's payment account ID.                                                                                                                                                                                                                                                                                |
| **transferMethod**  | string   | Y            | Enum string                                       | **SPOT_WALLET** <br /> **FUNDING_WALLET** <br /> **FUNDING_AND_SPOT_WALLET**                                                                                                                                                                                                                                  |
| **status**          | string   | Y            | Enum string                                       | **SUCCESS:** money has been transferred successfully <br /> **FAIL**: transaction failed may case by there’s insufficient fund in your account <br /> **AWAITING_RECEIPT** pending new user create an binance account and pass KYC to receive money <br /> **REFUNDED:** new user hasn’t pass KYC in 72 hours |
| **remark**          | string   | N            |                                                   | Maximum length 128                                                                                                                                                                                                                                                                                            |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "requestId": "2222222111222",
    "batchStatus": "SUCCESS",
    "merchantId": 22222222,
    "currency": "USDC",
    "totalAmount": "114.00000000",
    "totalNumber": 1,
    "totalPaidAmount": "114.91200000",
    "totalPayoutFee": "0.912",
    "transferDetailList": [
      {
        "orderId": 349275283293014145,
        "merchantSendId": "22123",
        "payerId": 300000001,
        "amount": "114.00000000",
        "payoutFee": "0.912",
        "totalPaidAmount": "114.91200000",
        "receiveType": "BINANCE_ID",
        "receiver": "1111111",
        "payeeId": 11111111,
        "transferMethod": "SPOT_WALLET",
        "status": "SUCCESS",
        "remark": null
      }
    ]
  }
}
```

```json
{
  "status": "FAIL",
  "code": "403015",
  "errorMessage": "pay order not found"
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
| PAYMENT_PAY_ORDER_NOT_FOUND        | 400602   | Pay order not found                                                            |                                                                                                |