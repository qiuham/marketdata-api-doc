---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-download-report
api_type: Guide
updated_at: 2026-11-26 18:35:33.109410
---

# Download Report

API used to download transaction and settlement report.

- This API is only available for whitelisted merchants. If you need help, please contact us at
  merchant@binance.com along with your Merchant ID and background

## EndPoint

```http request
POST /binancepay/openapi/report/get-file
```

## Request Parameters

| **Attributes**      | **Type**    | **Required** | **Limitation**             | **Description**                                                                                                                                                                                                                                             |
| ------------------- | ----------- | ------------ | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **reportType**      | enum string | Y            | "Transaction" "Settlement" | Report type can be either "Settlement" or "Transaction". Please note the parameter is cap sensitive.                                                                                                                                                        |
| **transactionType** | enum string | N            | "Payment" "Payout"         | transactionType refers to the transaction information you wish to generate.Please note the parameter is cap sensitive.If the reportType is "Settlement", this can be null If the reportType is "Transaction" field is required, either "Payment" or Payout" |
| **startDate**       | string      | Y            | dd/MM/yyyy                 | Start date                                                                                                                                                                                                                                                  |
| **endDate**         | string      | Y            | dd/MM/yyyy                 | End date. from startDate to endDate can only support querying data within 3 months                                                                                                                                                                          |

### Sample Request Parameter

```json
{
  "reportType": "Settlement",
  "transactionType": "",
  "startDate": "01/10/2022",
  "endDate": "29/10/2022"
}
```

## Response Parameters

| **Attributes**   | **Type**                      | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ----------------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string                        | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string                        | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | list[MerchantDailyReportData] | N            | -                                   | response body, [refer to](#report-data)        |
| **errorMessage** | string                        | N            | maximum length 256                  |                                                |

## Child Attribute

### MerchantDailyReportData

<span id="report-data"></span>

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                  | **Description**                                                                                                                                                                                                                                               |
| ------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **reportType**      | string   | Y            |                                                                                                 | Report type                                                                                                                                                                                                                                                   |
| **transactionType** | string   | Y            |                                                                                                 | Transaction or Settlement                                                                                                                                                                                                                                     |
| **transactionDate** | string   | Y            |                                                                                                 | When reportType is Transaction, then the transactionType is Payment or Payout（the list contains one type File depends on the request param, when reportType is Settlement, then the transactionType is Payment or Refund （the list contains two type File） |
| **fileName**        | string   | Y            | T_Payment_yyyyMMdd.xls / T_Payout_yyyyMMdd.xls / S_Payment_yyyyMMdd.xls / S_Refund_yyyyMMdd.xls | Report file name                                                                                                                                                                                                                                              |
| **downloadUrl**     | string   | Y            |                                                                                                 | Download URL                                                                                                                                                                                                                                                  |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": [
    {
      "reportType": "Settlement",
      "transactionType": "Refund",
      "transactionDate": "29/10/2022",
      "fileName": "S_Refund_29102022.xlsx",
      "downloadUrl": "https://<bucket-name>.s3.ap-northeast-1.amazonaws.com/dailyReport/<merchantId>/S_Refund_29102022.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221031T025922Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIAXXXXXXXXXXXXXXXX%2F20221031%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=<signature>"
    },
    {
      "reportType": "Settlement",
      "transactionType": "Payment",
      "transactionDate": "29/10/2022",
      "fileName": "S_Payment_29102022.xlsx",
      "downloadUrl": "https://<bucket-name>.s3.ap-northeast-1.amazonaws.com/dailyReport/<merchantId>/S_Payment_29102022.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221031T025922Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAXXXXXXXXXXXXXXXX%2F20221031%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=<signature>"
    }
  ]
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

# Download Report

API used to download transaction and settlement report.

- This API is only available for whitelisted merchants. If you need help, please contact us at
  merchant@binance.com along with your Merchant ID and background

## EndPoint

```http request
POST /binancepay/openapi/report/get-file
```

## Request Parameters

| **Attributes**      | **Type**    | **Required** | **Limitation**             | **Description**                                                                                                                                                                                                                                             |
| ------------------- | ----------- | ------------ | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **reportType**      | enum string | Y            | "Transaction" "Settlement" | Report type can be either "Settlement" or "Transaction". Please note the parameter is cap sensitive.                                                                                                                                                        |
| **transactionType** | enum string | N            | "Payment" "Payout"         | transactionType refers to the transaction information you wish to generate.Please note the parameter is cap sensitive.If the reportType is "Settlement", this can be null If the reportType is "Transaction" field is required, either "Payment" or Payout" |
| **startDate**       | string      | Y            | dd/MM/yyyy                 | Start date                                                                                                                                                                                                                                                  |
| **endDate**         | string      | Y            | dd/MM/yyyy                 | End date. from startDate to endDate can only support querying data within 3 months                                                                                                                                                                          |

### Sample Request Parameter

```json
{
  "reportType": "Settlement",
  "transactionType": "",
  "startDate": "01/10/2022",
  "endDate": "29/10/2022"
}
```

## Response Parameters

| **Attributes**   | **Type**                      | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ----------------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string                        | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string                        | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | list[MerchantDailyReportData] | N            | -                                   | response body, [refer to](#report-data)        |
| **errorMessage** | string                        | N            | maximum length 256                  |                                                |

## Child Attribute

### MerchantDailyReportData

<span id="report-data"></span>

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                  | **Description**                                                                                                                                                                                                                                               |
| ------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **reportType**      | string   | Y            |                                                                                                 | Report type                                                                                                                                                                                                                                                   |
| **transactionType** | string   | Y            |                                                                                                 | Transaction or Settlement                                                                                                                                                                                                                                     |
| **transactionDate** | string   | Y            |                                                                                                 | When reportType is Transaction, then the transactionType is Payment or Payout（the list contains one type File depends on the request param, when reportType is Settlement, then the transactionType is Payment or Refund （the list contains two type File） |
| **fileName**        | string   | Y            | T_Payment_yyyyMMdd.xls / T_Payout_yyyyMMdd.xls / S_Payment_yyyyMMdd.xls / S_Refund_yyyyMMdd.xls | Report file name                                                                                                                                                                                                                                              |
| **downloadUrl**     | string   | Y            |                                                                                                 | Download URL                                                                                                                                                                                                                                                  |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": [
    {
      "reportType": "Settlement",
      "transactionType": "Refund",
      "transactionDate": "29/10/2022",
      "fileName": "S_Refund_29102022.xlsx",
      "downloadUrl": "https://<bucket-name>.s3.ap-northeast-1.amazonaws.com/dailyReport/<merchantId>/S_Refund_29102022.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221031T025922Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIAXXXXXXXXXXXXXXXX%2F20221031%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=<signature>"
    },
    {
      "reportType": "Settlement",
      "transactionType": "Payment",
      "transactionDate": "29/10/2022",
      "fileName": "S_Payment_29102022.xlsx",
      "downloadUrl": "https://<bucket-name>.s3.ap-northeast-1.amazonaws.com/dailyReport/<merchantId>/S_Payment_29102022.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221031T025922Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAXXXXXXXXXXXXXXXX%2F20221031%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=<signature>"
    }
  ]
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