---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-convert-get-quote
api_type: Guide
updated_at: 2026-11-24 18:35:02.516041
---

# Send Quote

API used to send convert quote.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/get-quote
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                                                                        | **Description**                                                                                                 |
| -------------- | -------- | ------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **wallet**     | string   | Y            | Enum string                                                                           | Binance wallet to query, currently supported enum valus: <br /><br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** |
| **fromAsset**  | string   | Y            | Valid currency, must be in uppercase. Only require either fromAsset or toAsset.       | Currency to query, for e.g, "USDC","USDT" & "BNB"                                                               |
| **toAsset**    | string   | Y            | Valid currency, must be in uppercase. Only require either fromAsset or toAsset.       | Currency to query, for e.g, "USDC","USDT" & "BNB"                                                               |
| **fromAmount** | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | From asset amount                                                                                               |
| **toAmount**   | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | To asset amount                                                                                                 |

### Sample Request Body

```json
{
  "wallet": "FUNDING_WALLET",
  "fromAsset": "USDT",
  "toAsset": "BNB",
  "fromAmount": null,
  "toAmount": 0.8
}
```

## Response Parameters

| **Attributes**   | **Type**      | **Required** | **Limitation**                      | **Description**                                 |
| ---------------- | ------------- | ------------ | ----------------------------------- | ----------------------------------------------- |
| **status**       | string        | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                       |
| **code**         | string        | Y            | -                                   | request result code, [refer to ](#result-code)  |
| **data**         | SendQuoteResp | N            | -                                   | response body, [refer to](#send-quote-response) |
| **errorMessage** | string        | N            | maximum length 256                  |                                                 |

## Child Attribute

### SendQuoteResp

<span id="send-quote-response"></span>

| **Attributes**     | **Type** | **Required** | **Limitation** | **Description**                                                                        |
| ------------------ | -------- | ------------ | -------------- | -------------------------------------------------------------------------------------- |
| **quoteId**        | string   | N            |                | Quote ID for execute quote. If not returned, there is insufficient balance to convert. |
| **ratio**          | decimal  | Y            |                | `From:To` quote price                                                                  |
| **inverseRatio**   | decimal  | Y            |                | `To:From` quote price                                                                  |
| **validTimestamp** | decimal  | Y            |                | Expire timestamp                                                                       |
| **expireTime**     | decimal  | Y            |                | Expire time (second)                                                                   |
| **toAmount**       | decimal  | Y            |                | When specified, it is the amount you will be credited after the conversion             |
| **toCoin**         | string   | Y            |                | To Asset                                                                               |
| **fromAmount**     | decimal  | Y            |                | When specified, it is the amount you will be debited after the conversion              |
| **fromCoin**       | string   | Y            |                | From Asset                                                                             |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "quoteId": "2d7b7439c540479999ec367a701bf5f6",
    "ratio": 0.00445577,
    "inverseRatio": 224.428,
    "validTimestamp": 1666949735947,
    "expireTime": 4,
    "toAmount": 0.8,
    "toCoin": "BNB",
    "fromAmount": 179.54201695,
    "fromCoin": "USDT"
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

---

# Send Quote

API used to send convert quote.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/otc-portal/get-quote
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                                                                        | **Description**                                                                                                 |
| -------------- | -------- | ------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **wallet**     | string   | Y            | Enum string                                                                           | Binance wallet to query, currently supported enum valus: <br /><br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** |
| **fromAsset**  | string   | Y            | Valid currency, must be in uppercase. Only require either fromAsset or toAsset.       | Currency to query, for e.g, "USDC","USDT" & "BNB"                                                               |
| **toAsset**    | string   | Y            | Valid currency, must be in uppercase. Only require either fromAsset or toAsset.       | Currency to query, for e.g, "USDC","USDT" & "BNB"                                                               |
| **fromAmount** | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | From asset amount                                                                                               |
| **toAmount**   | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | To asset amount                                                                                                 |

### Sample Request Body

```json
{
  "wallet": "FUNDING_WALLET",
  "fromAsset": "USDT",
  "toAsset": "BNB",
  "fromAmount": null,
  "toAmount": 0.8
}
```

## Response Parameters

| **Attributes**   | **Type**      | **Required** | **Limitation**                      | **Description**                                 |
| ---------------- | ------------- | ------------ | ----------------------------------- | ----------------------------------------------- |
| **status**       | string        | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                       |
| **code**         | string        | Y            | -                                   | request result code, [refer to ](#result-code)  |
| **data**         | SendQuoteResp | N            | -                                   | response body, [refer to](#send-quote-response) |
| **errorMessage** | string        | N            | maximum length 256                  |                                                 |

## Child Attribute

### SendQuoteResp

<span id="send-quote-response"></span>

| **Attributes**     | **Type** | **Required** | **Limitation** | **Description**                                                                        |
| ------------------ | -------- | ------------ | -------------- | -------------------------------------------------------------------------------------- |
| **quoteId**        | string   | N            |                | Quote ID for execute quote. If not returned, there is insufficient balance to convert. |
| **ratio**          | decimal  | Y            |                | `From:To` quote price                                                                  |
| **inverseRatio**   | decimal  | Y            |                | `To:From` quote price                                                                  |
| **validTimestamp** | decimal  | Y            |                | Expire timestamp                                                                       |
| **expireTime**     | decimal  | Y            |                | Expire time (second)                                                                   |
| **toAmount**       | decimal  | Y            |                | When specified, it is the amount you will be credited after the conversion             |
| **toCoin**         | string   | Y            |                | To Asset                                                                               |
| **fromAmount**     | decimal  | Y            |                | When specified, it is the amount you will be debited after the conversion              |
| **fromCoin**       | string   | Y            |                | From Asset                                                                             |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "quoteId": "2d7b7439c540479999ec367a701bf5f6",
    "ratio": 0.00445577,
    "inverseRatio": 224.428,
    "validTimestamp": 1666949735947,
    "expireTime": 4,
    "toAmount": 0.8,
    "toCoin": "BNB",
    "fromAmount": 179.54201695,
    "fromCoin": "USDT"
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