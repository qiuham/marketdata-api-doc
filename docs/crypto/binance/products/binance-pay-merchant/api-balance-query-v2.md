---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-balance-query-v2
api_type: Guide
updated_at: 2026-11-21 18:34:17.650941
---

# Wallet Balance Query V2

API used to query one or more wallet balance.

## EndPoint

```http request
POST /binancepay/openapi/v2/balance
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                       | **Description**                                                                                                 |
| -------------- | -------- | ------------ | ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **wallet**     | string   | Y            | Enum string                          | Binance wallet to query, currently supported enum valus: <br /><br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** |
| **currency**   | string   | N            | Valid currency, must be in uppercase | Currency to query, for e.g, "USDC","USDT" & "BNB". If no currency was sent, return all assets.                  |

### Sample Request Body

```json
{
  "wallet": "SPOT_WALLET",
  "currency": "USDT"
}
```

## Response Parameters

| **Attributes**   | **Type**         | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string           | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string           | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | AssetQueryRespV2 | N            | -                                   | response body, [refer to](#balance-response)   |
| **errorMessage** | string           | N            | maximum length 256                  |                                                |

## Child Attribute

### AssetQueryRespV2

<span id="balance-response"></span>

| **Attributes** | **Type**       | **Required** | **Limitation** | **Description**                                   |
| -------------- | -------------- | ------------ | -------------- | ------------------------------------------------- |
| **balance**    | AssetQueryData | N            |                | Currency data, [refer to](#balance-response-data) |
| **wallet**     | string         | Y            |                | Wallet that contains the currencies               |
| **updateTime** | string         | Y            |                | Update time of the data                           |
| **fiat**       | string         | Y            |                | Fiat name, for fiat valuation                     |

### AssetQueryData

<span id="balance-response-data"></span>

| **Attributes**             | **Type** | **Required** | **Limitation**                                                                        | **Description**             |
| -------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------- | --------------------------- |
| **available**              | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Current balance free to use |
| **freeze**                 | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Current balance frozen      |
| **asset**                  | string   | Y            |                                                                                       | Asset/currency name         |
| **availableFiatValuation** | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Available fiat valuation    |
| **availableBtcValuation**  | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Available BTC valuation     |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "balance": [
      {
        "available": 990000.0,
        "freeze": 0e-8,
        "asset": "USDT",
        "availableFiatValuation": 989991.905166,
        "availableBtcValuation": 22.9878
      }
    ],
    "wallet": "FUNDING_WALLET",
    "updateTime": 1666937353019,
    "fiat": "USD"
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

# Wallet Balance Query V2

API used to query one or more wallet balance.

## EndPoint

```http request
POST /binancepay/openapi/v2/balance
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                       | **Description**                                                                                                 |
| -------------- | -------- | ------------ | ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **wallet**     | string   | Y            | Enum string                          | Binance wallet to query, currently supported enum valus: <br /><br /> **FUNDING_WALLET** <br /> **SPOT_WALLET** |
| **currency**   | string   | N            | Valid currency, must be in uppercase | Currency to query, for e.g, "USDC","USDT" & "BNB". If no currency was sent, return all assets.                  |

### Sample Request Body

```json
{
  "wallet": "SPOT_WALLET",
  "currency": "USDT"
}
```

## Response Parameters

| **Attributes**   | **Type**         | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ---------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string           | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string           | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | AssetQueryRespV2 | N            | -                                   | response body, [refer to](#balance-response)   |
| **errorMessage** | string           | N            | maximum length 256                  |                                                |

## Child Attribute

### AssetQueryRespV2

<span id="balance-response"></span>

| **Attributes** | **Type**       | **Required** | **Limitation** | **Description**                                   |
| -------------- | -------------- | ------------ | -------------- | ------------------------------------------------- |
| **balance**    | AssetQueryData | N            |                | Currency data, [refer to](#balance-response-data) |
| **wallet**     | string         | Y            |                | Wallet that contains the currencies               |
| **updateTime** | string         | Y            |                | Update time of the data                           |
| **fiat**       | string         | Y            |                | Fiat name, for fiat valuation                     |

### AssetQueryData

<span id="balance-response-data"></span>

| **Attributes**             | **Type** | **Required** | **Limitation**                                                                        | **Description**             |
| -------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------- | --------------------------- |
| **available**              | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Current balance free to use |
| **freeze**                 | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Current balance frozen      |
| **asset**                  | string   | Y            |                                                                                       | Asset/currency name         |
| **availableFiatValuation** | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Available fiat valuation    |
| **availableBtcValuation**  | decimal  | Y            | Amount Range: 0.00000001 - 999999999999999.99999999; Max Unit Range: 8 decimal places | Available BTC valuation     |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "balance": [
      {
        "available": 990000.0,
        "freeze": 0e-8,
        "asset": "USDT",
        "availableFiatValuation": 989991.905166,
        "availableBtcValuation": 22.9878
      }
    ],
    "wallet": "FUNDING_WALLET",
    "updateTime": 1666937353019,
    "fiat": "USD"
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