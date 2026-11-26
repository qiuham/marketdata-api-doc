---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-profitshare-query-receiver
api_type: Guide
updated_at: 2026-11-26 18:35:10.565612
---

# Query Receiver

API used to query list of receivers.

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/query-receiver
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                 |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------- |
| **pageNum**    | int      | Y            |                | Pagination number. Starts from 1.               |
| **pageSize**   | int      | Y            |                | Pagination size, number of receivers in a page. |

### Sample Request Parameter

```json
{
  "pageNum": 1,
  "pageSize": 20
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Response | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

## Child Attribute

### Response

<span id="quote-response"></span>

| **Attributes**      | **Type**     | **Required** | **Limitation** | **Description**                          |
| ------------------- | ------------ | ------------ | -------------- | ---------------------------------------- |
| **accountList**     | List(String) | Y            |                | List of accounts registered as receiver. |
| **totalPageNum**    | int          | Y            |                | Total amount of pages                    |
| **totalRecordNum**  | long         | Y            |                | Total amount of records                  |
| **currentPageNum**  | int          | Y            |                | Current page number                      |
| **currentPageSize** | int          | Y            |                | Current page size                        |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "accountList": ["12345", "67890"],
    "totalPageNum": 1,
    "totalRecordNum": 2,
    "currentPageNum": 1,
    "currentPageSize": 20
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400000",
  "errorMessage": "An unknown error occurred while processing the request."
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
| PAYMENT_ACCOUNT_NOT_FOUND          | 400601   | Account not found                                                              |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |

---

# Query Receiver

API used to query list of receivers.

## EndPoint

```http request
POST /binancepay/openapi/profitsharing/v1/query-receiver
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                 |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------- |
| **pageNum**    | int      | Y            |                | Pagination number. Starts from 1.               |
| **pageSize**   | int      | Y            |                | Pagination size, number of receivers in a page. |

### Sample Request Parameter

```json
{
  "pageNum": 1,
  "pageSize": 20
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Response | N            | -                                   | response body, [refer to](#quote-response)     |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

## Child Attribute

### Response

<span id="quote-response"></span>

| **Attributes**      | **Type**     | **Required** | **Limitation** | **Description**                          |
| ------------------- | ------------ | ------------ | -------------- | ---------------------------------------- |
| **accountList**     | List(String) | Y            |                | List of accounts registered as receiver. |
| **totalPageNum**    | int          | Y            |                | Total amount of pages                    |
| **totalRecordNum**  | long         | Y            |                | Total amount of records                  |
| **currentPageNum**  | int          | Y            |                | Current page number                      |
| **currentPageSize** | int          | Y            |                | Current page size                        |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "accountList": ["12345", "67890"],
    "totalPageNum": 1,
    "totalRecordNum": 2,
    "currentPageNum": 1,
    "currentPageSize": 20
  }
}
```

```json
{
  "status": "FAIL",
  "code": "400000",
  "errorMessage": "An unknown error occurred while processing the request."
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
| PAYMENT_ACCOUNT_NOT_FOUND          | 400601   | Account not found                                                              |                                                                                                |
| RECEIVER_INVALID                   | 400214   | Receiver not bind                                                              |                                                                                                |