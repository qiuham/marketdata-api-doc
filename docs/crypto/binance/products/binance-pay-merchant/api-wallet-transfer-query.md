---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-wallet-transfer-query
api_type: Guide
updated_at: 2026-11-19 18:35:33.773536
---

# Query Transfer Result

Query Transfer Result API used for merchant/partner to query transfer result.

## EndPoint

```http request
POST /binancepay/openapi/wallet/transfer/query
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                       |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------------- |
| **tranId**     | string   | Y            | -              | the value of requestId of provoking Transfer Fund API |

### Sample Request Body

```json
{
  "tranId": "100002021071407140001"
}
```

## Response Parameters

| **Attributes**   | **Type**       | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string         | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string         | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | TransferResult | N            | -                                   | response body, [refer to](#transfer-result)    |
| **errorMessage** | string         | N            | maximum length 256                  |                                                |

## Child Attribute

### TransferResult

<span id="transfer-result"></span>

| **Attributes** | **Type** | **Required** | **Limitation**                | **Description**                                                                                                                                                                                                            |
| -------------- | -------- | ------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **tranId**     | string   | Y            | -                             | Used to query the transfer status, query the necessary fields for the transfer status                                                                                                                                      |
| **status**     | string   | Y            | SUCCESS OR FAILURE OR PROCESS | SUCCESS (indicating that the transfer is completely successful), FAILURE (indicating that the transfer has failed, it may be that the transferor has a problem with the transferee), PROCESS (the transfer is in progress) |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "tranId": "100002021071407140001",
    "status": "SUCCESS"
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
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |
| TRANSFER_TRAN_ID_NOT_FOUND         | 400401   | can not find the transfer                                                      |                                                                                                |

---

# Query Transfer Result

Query Transfer Result API used for merchant/partner to query transfer result.

## EndPoint

```http request
POST /binancepay/openapi/wallet/transfer/query
```

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                       |
| -------------- | -------- | ------------ | -------------- | ----------------------------------------------------- |
| **tranId**     | string   | Y            | -              | the value of requestId of provoking Transfer Fund API |

### Sample Request Body

```json
{
  "tranId": "100002021071407140001"
}
```

## Response Parameters

| **Attributes**   | **Type**       | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string         | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string         | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | TransferResult | N            | -                                   | response body, [refer to](#transfer-result)    |
| **errorMessage** | string         | N            | maximum length 256                  |                                                |

## Child Attribute

### TransferResult

<span id="transfer-result"></span>

| **Attributes** | **Type** | **Required** | **Limitation**                | **Description**                                                                                                                                                                                                            |
| -------------- | -------- | ------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **tranId**     | string   | Y            | -                             | Used to query the transfer status, query the necessary fields for the transfer status                                                                                                                                      |
| **status**     | string   | Y            | SUCCESS OR FAILURE OR PROCESS | SUCCESS (indicating that the transfer is completely successful), FAILURE (indicating that the transfer has failed, it may be that the transferor has a problem with the transferee), PROCESS (the transfer is in progress) |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "tranId": "100002021071407140001",
    "status": "SUCCESS"
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
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |
| TRANSFER_TRAN_ID_NOT_FOUND         | 400401   | can not find the transfer                                                      |                                                                                                |