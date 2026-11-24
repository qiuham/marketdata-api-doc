---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-download-balance-report
api_type: Guide
updated_at: 2026-11-24 18:34:48.478428
---

# Download Balance Report

Download Balance Report API used to download balance activities within a date range. The report
cannot query current day's data.

When report is ready, a [callback notification](webhook-balance-report.md) will be sent to
merchant's default callback URL. Or you can use the
[Query Balance Report API](api-download-balance-report-query) to query the status and retrieve the
file path to download the report.

A merchant can generate up to a maximum of 50 balance reports per month.

## EndPoint

```http request
POST /binancepay/openapi/balance-report
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                                                           | **Description**                                                                                                  |
| -------------- | -------- | ------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **reportType** | string   | Y            | Valid value is "Balance"                                                 | -                                                                                                                |
| **walletType** | string   | N            | Valid values are:"SPOT_WALLET", "FUNDING_WALLET"                         | If merchants don't specify one wallet, then Binance Pay will query all records of spot wallet and funding wallet |
| **startDate**  | string   | Y            | YYYY-MM-DD                                                               | From startDate to endDate can only support querying data within 3 months                                         |
| **endDate**    | string   | Y            | YYYY-MM-DD. **End date should not be same as start day, must be +1 day** | From startDate to endDate can only support querying data within 3 months                                         |

### Sample Request Body

Submit request for both FUNDING and SPOT wallet activities:

```json
{
  "reportType": "Balance",
  "startDate": "2022-08-20",
  "endDate": "2022-09-05"
}
```

Submit request for single wallet activities:

```json
{
  "reportType": "Balance",
  "walletType": "SPOT_WALLET",
  "startDate": "2022-08-20",
  "endDate": "2022-09-05"
}
```

## Response Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                      | **Description**                                                   |
| -------------- | -------- | ------------ | ----------------------------------- | ----------------------------------------------------------------- |
| **status**     | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                                         |
| **code**       | string   | Y            | -                                   | request result code, [refer to ](#result-code)                    |
| **data**       | string   | N            | -                                   | containing the download ID if request was submitted successfully. |

## Child Attribute

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": "Your request has been submitted successfully. Your task ID: 197430692664688640"
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

# Download Balance Report

Download Balance Report API used to download balance activities within a date range. The report
cannot query current day's data.

When report is ready, a [callback notification](webhook-balance-report.md) will be sent to
merchant's default callback URL. Or you can use the
[Query Balance Report API](api-download-balance-report-query) to query the status and retrieve the
file path to download the report.

A merchant can generate up to a maximum of 50 balance reports per month.

## EndPoint

```http request
POST /binancepay/openapi/balance-report
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                                                           | **Description**                                                                                                  |
| -------------- | -------- | ------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **reportType** | string   | Y            | Valid value is "Balance"                                                 | -                                                                                                                |
| **walletType** | string   | N            | Valid values are:"SPOT_WALLET", "FUNDING_WALLET"                         | If merchants don't specify one wallet, then Binance Pay will query all records of spot wallet and funding wallet |
| **startDate**  | string   | Y            | YYYY-MM-DD                                                               | From startDate to endDate can only support querying data within 3 months                                         |
| **endDate**    | string   | Y            | YYYY-MM-DD. **End date should not be same as start day, must be +1 day** | From startDate to endDate can only support querying data within 3 months                                         |

### Sample Request Body

Submit request for both FUNDING and SPOT wallet activities:

```json
{
  "reportType": "Balance",
  "startDate": "2022-08-20",
  "endDate": "2022-09-05"
}
```

Submit request for single wallet activities:

```json
{
  "reportType": "Balance",
  "walletType": "SPOT_WALLET",
  "startDate": "2022-08-20",
  "endDate": "2022-09-05"
}
```

## Response Parameters

| **Attributes** | **Type** | **Required** | **Limitation**                      | **Description**                                                   |
| -------------- | -------- | ------------ | ----------------------------------- | ----------------------------------------------------------------- |
| **status**     | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                                         |
| **code**       | string   | Y            | -                                   | request result code, [refer to ](#result-code)                    |
| **data**       | string   | N            | -                                   | containing the download ID if request was submitted successfully. |

## Child Attribute

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": "Your request has been submitted successfully. Your task ID: 197430692664688640"
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