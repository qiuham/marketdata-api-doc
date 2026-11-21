---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-download-balance-report-query
api_type: Guide
updated_at: 2026-11-21 18:33:58.849072
---

# Query Balance Report

Query Balance Report API used to query the downloaded report status and get the file path of the
report.

## EndPoint

```http request
POST /binancepay/openapi/balance-report/query
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                 |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------- |
| **downloadId** | string   | Y            | -              | the data retuned at download balance report API |

### Sample Request Body

```json
{
  "downloadId": "1232213"
}
```

## Response Parameters

| **Attributes**  | **Type** | **Required** | **Limitation** | **Description**                   |
| --------------- | -------- | ------------ | -------------- | --------------------------------- |
| **exist**       | boolean  | Y            | -              | exist or not                      |
| **status**      | string   | Y            | -              | PROCESSING FAILED EXPIRED SUCCESS |
| **downloadUrl** | string   | N            | -              | the doanload url                  |

## Child Attribute

### Sample Response

```json
{
  "exist": true,
  "downloadUrl": "",
  "status": "PROCESSING"
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
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                               |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |

---

# Query Balance Report

Query Balance Report API used to query the downloaded report status and get the file path of the
report.

## EndPoint

```http request
POST /binancepay/openapi/balance-report/query
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                 |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------- |
| **downloadId** | string   | Y            | -              | the data retuned at download balance report API |

### Sample Request Body

```json
{
  "downloadId": "1232213"
}
```

## Response Parameters

| **Attributes**  | **Type** | **Required** | **Limitation** | **Description**                   |
| --------------- | -------- | ------------ | -------------- | --------------------------------- |
| **exist**       | boolean  | Y            | -              | exist or not                      |
| **status**      | string   | Y            | -              | PROCESSING FAILED EXPIRED SUCCESS |
| **downloadUrl** | string   | N            | -              | the doanload url                  |

## Child Attribute

### Sample Response

```json
{
  "exist": true,
  "downloadUrl": "",
  "status": "PROCESSING"
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
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                               |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |