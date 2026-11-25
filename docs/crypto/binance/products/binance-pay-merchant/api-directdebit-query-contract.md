---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-directdebit-query-contract
api_type: Guide
updated_at: 2026-11-25 18:34:42.760859
---

# Direct Debit/Pre Authorization Query Contract

This API used for merchant/partner to query direct debit/ pre authorization contract for user
authorization.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/direct-debit/contract/query
```

## Request Parameters

| **Attributes**           | **Type** | **Required** | **Limitation**                                                                                      | **Description**                                                                                               |
| ------------------------ | -------- | ------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **merchantContractCode** | string   | N            | letter or digit, no other symbol allowed, maximum length 32, can not be empty if contractId is null | The merchant contract code, unique identifier for the request. Will be ignored if contractId already provided |
| **contractId**           | long     | N            | number, can not be null if merchantTradeNo is empty                                                 | The unique contract id, which is obtained through webhook after the user signs the contract.                  |

### Sample Request Body

Query contract by merchantContractCode:

```json
{
  "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5"
}
```

Query contract by contractId:

```json
{
  "contractId": "205611460060250112"
}
```

## Response Parameters

| **Attributes**   | **Type**            | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string              | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string              | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | QueryContractResult | N            | -                                   | response body, [refer to](#contract-result)    |
| **errorMessage** | string              | Y            | -                                   |                                                |

## Child Attribute

### QueryContractResult

<span id="contract-result"></span>

| **Attributes**              | **Type** | **Required** | **Limitation**                                                                                          | **Description**                                                                                                 |
| --------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **bizStatus**               | string   | Y            | &#34;INITIAL&#34;, &#34;CONTRACT_SIGNED&#34;, &#34;CONTRACT_TERMINATED&#34;, &#34;CONTRACT_EXPIRED&#34; | contract status                                                                                                 |
| **merchantContractCode**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                                             | The unique ID assigned by the merchant to identify a direct debit contract request.                             |
| **contractId**              | Long     | N            | maximum length 19                                                                                       | contract id                                                                                                     |
| **serviceName**             | string   | Y            | maximum length 32                                                                                       | service name                                                                                                    |
| **openUserId**              | string   | N            | -                                                                                                       | signer unique id                                                                                                |
| **merchantAccountNo**       | string   | N            | maximum length 64                                                                                       | the userID/user account in merchant side e.g. xxx@gmail.com                                                     |
| **singleUpperLimit**        | decimal  | Y            | Max Unit Range: 8 decimal places                                                                        | upper limit                                                                                                     |
| **currency**                | string   | Y            | -                                                                                                       | currency                                                                                                        |
| **contractTerminationWay**  | int      | N            | -                                                                                                       | 0-by user, 1-auto expire, 2-by operation team, 3-by merchant openapi. only &#34;CONTRACT_TERMINATED&#34; status |
| **contractTerminationTime** | Long     | N            | -                                                                                                       | only &#34;CONTRACT_TERMINATED&#34; status                                                                       |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "bizStatus": "CONTRACT_SIGNED",
    "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5",
    "contractId": "205611460060250112",
    "serviceName": "Tra Direct Debit",
    "openUserId": "eb6b287a44dd73dd81645a3cbcfee162",
    "merchantAccountNo": "sss@gmail.com",
    "currency": "USDT",
    "singleUpperLimit": "30"
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| PAYMENT_INVALID_PARAM                   | 400702   | Invalid request parameter                                                      |                                                                                                |
| MERCHANT_ACCESS_FORBIDDEN               | 400606   | Account has no accessibility to this function                                  |                                                                                                |
| PAYMENT_DIRECT_DEBIT_CONTRACT_NOT_FOUND | 406207   | Contract not found                                                             |                                                                                                |

---

# Direct Debit/Pre Authorization Query Contract

This API used for merchant/partner to query direct debit/ pre authorization contract for user
authorization.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

## EndPoint

```http request
POST /binancepay/openapi/direct-debit/contract/query
```

## Request Parameters

| **Attributes**           | **Type** | **Required** | **Limitation**                                                                                      | **Description**                                                                                               |
| ------------------------ | -------- | ------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **merchantContractCode** | string   | N            | letter or digit, no other symbol allowed, maximum length 32, can not be empty if contractId is null | The merchant contract code, unique identifier for the request. Will be ignored if contractId already provided |
| **contractId**           | long     | N            | number, can not be null if merchantTradeNo is empty                                                 | The unique contract id, which is obtained through webhook after the user signs the contract.                  |

### Sample Request Body

Query contract by merchantContractCode:

```json
{
  "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5"
}
```

Query contract by contractId:

```json
{
  "contractId": "205611460060250112"
}
```

## Response Parameters

| **Attributes**   | **Type**            | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | ------------------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string              | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string              | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | QueryContractResult | N            | -                                   | response body, [refer to](#contract-result)    |
| **errorMessage** | string              | Y            | -                                   |                                                |

## Child Attribute

### QueryContractResult

<span id="contract-result"></span>

| **Attributes**              | **Type** | **Required** | **Limitation**                                                                                          | **Description**                                                                                                 |
| --------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **bizStatus**               | string   | Y            | &#34;INITIAL&#34;, &#34;CONTRACT_SIGNED&#34;, &#34;CONTRACT_TERMINATED&#34;, &#34;CONTRACT_EXPIRED&#34; | contract status                                                                                                 |
| **merchantContractCode**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32                                             | The unique ID assigned by the merchant to identify a direct debit contract request.                             |
| **contractId**              | Long     | N            | maximum length 19                                                                                       | contract id                                                                                                     |
| **serviceName**             | string   | Y            | maximum length 32                                                                                       | service name                                                                                                    |
| **openUserId**              | string   | N            | -                                                                                                       | signer unique id                                                                                                |
| **merchantAccountNo**       | string   | N            | maximum length 64                                                                                       | the userID/user account in merchant side e.g. xxx@gmail.com                                                     |
| **singleUpperLimit**        | decimal  | Y            | Max Unit Range: 8 decimal places                                                                        | upper limit                                                                                                     |
| **currency**                | string   | Y            | -                                                                                                       | currency                                                                                                        |
| **contractTerminationWay**  | int      | N            | -                                                                                                       | 0-by user, 1-auto expire, 2-by operation team, 3-by merchant openapi. only &#34;CONTRACT_TERMINATED&#34; status |
| **contractTerminationTime** | Long     | N            | -                                                                                                       | only &#34;CONTRACT_TERMINATED&#34; status                                                                       |

### Sample Response

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": {
    "bizStatus": "CONTRACT_SIGNED",
    "merchantContractCode": "c0ecfb465e454560a5d8e307bbc407c5",
    "contractId": "205611460060250112",
    "serviceName": "Tra Direct Debit",
    "openUserId": "eb6b287a44dd73dd81645a3cbcfee162",
    "merchantAccountNo": "sss@gmail.com",
    "currency": "USDT",
    "singleUpperLimit": "30"
  }
}
```

## Result Code

<span id="result-code"></span>

| **Name**                                | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| --------------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                           | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                         | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                       | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                       | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                   | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                         | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                         | 400006   | Request method not supported.                                                  | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED                | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                    | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                             |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED      | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH              | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE               | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR              | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| PAYMENT_INVALID_PARAM                   | 400702   | Invalid request parameter                                                      |                                                                                                |
| MERCHANT_ACCESS_FORBIDDEN               | 400606   | Account has no accessibility to this function                                  |                                                                                                |
| PAYMENT_DIRECT_DEBIT_CONTRACT_NOT_FOUND | 406207   | Contract not found                                                             |                                                                                                |