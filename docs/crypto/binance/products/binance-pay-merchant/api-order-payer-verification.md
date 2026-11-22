---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-order-payer-verification
api_type: Guide
updated_at: 2026-11-22 18:32:59.054045
---

# Payment Payer Verification

This API is used for Merchant/Partner to verify payer’s KYC information in their system with
Binance’s before Create Order.

Merchant/Partner will pass the payer’s BID and KYC information via this API to Binance for
verification and matching.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/order/payer/verification
```

## Request Parameters

| **Attributes**  | **Type** | **Required** | **Limitation**                       | **Description**                                                                                  |
| --------------- | -------- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **binanceId**   | string   | Y            |                                      | payer's binance id                                                                               |
| **payerType**   | string   | Y            | Enum value                           | payer type <br /><br /> **INDIVIDUAL**: individual payer. <br /> **CORPORATE**: corporate payer. |
| **information** | List     | N            | elements structure in list: **Info** | information to be verified                                                                       |

### Info

| **Attributes** | **Type** | **Required** | **Limitation**  | **Description**                                                                                                                                                                                                                                                                                                                                  |
| -------------- | -------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **category**   | string   | Y            | Enum value      | For Individual: <br/>**FIRST_NAME**<br/> **LAST_NAME**<br/> **DATE_OF_BIRTH**<br/> **NATIONALITY (2-letter country code)**-optional<br/> **DOCUMENT_TYPE**-optional<br/> **DOCUMENT_NUMBER**-optional <br/><br/>For corporate:<br/>**COMPANY_NAME**<br/> **REGISTRATION_NUMBER**<br/> **REGISTRATION_COUNTRY (2-letter country code)**           |
| **value**      | string   | Y            | max length 1024 | value of information <br/> For **DOCUMENT_TYPE**, available values are: ID_CARD/PASSPORT/DRIVING_LICENSE/VISA/CPF/OTHER/BVN_NUMBER/NIN_NUMBER/PAN/BVN_NIN_NUMBER/SMILEID_NATIONAL_ID/ABN/ACN/UA_DIA <br/> For **DATE_OF_BIRTH** format: YYYY-MM-DD<br/> For **NATIONALITY** and **REGISTRATION_COUNTRY** value is based on 2-letter country code |

### Sample Request Body

```json
{
  "binanceId": "400000001",
  "payerType": "INDIVIDUAL",
  "information": [
    {
      "category": "FIRST_NAME",
      "value": "binance"
    },
    {
      "category": "LAST_NAME",
      "value": "pay"
    },
    {
      "category": "DATE_OF_BIRTH",
      "value": "1980-01-01"
    }
  ]
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Boolean  | N            | -                                   | true means matched, false means not matched    |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

### Sample Response

#### verify success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true
}
```

#### account of userId not existed

```json
{
  "status": "FAIL",
  "code": "400601",
  "errorMessage": "account not found"
}
```

#### kyc is not completed in binance side

```json
{
  "status": "FAIL",
  "code": "400722",
  "errorMessage": "kyc not completed"
}
```

#### kyc info mismatch, for example FIRST_NAME

```json
{
  "status": "FAIL",
  "code": "400102",
  "errorMessage": "Parameter information.FIRST_NAME not valid, the value is out of range."
}
```

#### too many failed request

```json
{
  "status": "FAIL",
  "code": "406108",
  "errorMessage": "Fail rate is high, please try again later"
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
| MERCHANT_TRANSFER_MERCHANT_TYPE_INVALID | 406107   | Merchant type not valid not support individual merchant                        |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TOO_FREQUENT | 406108   | Fail rate is high, please try again later                                      |                                                                                                |

---

# Payment Payer Verification

This API is used for Merchant/Partner to verify payer’s KYC information in their system with
Binance’s before Create Order.

Merchant/Partner will pass the payer’s BID and KYC information via this API to Binance for
verification and matching.

\*This API is only available for whitelisted merchants. If you need any help, you can contact us:
<merchant@binance.com>

## EndPoint

```http request
POST /binancepay/openapi/order/payer/verification
```

## Request Parameters

| **Attributes**  | **Type** | **Required** | **Limitation**                       | **Description**                                                                                  |
| --------------- | -------- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **binanceId**   | string   | Y            |                                      | payer's binance id                                                                               |
| **payerType**   | string   | Y            | Enum value                           | payer type <br /><br /> **INDIVIDUAL**: individual payer. <br /> **CORPORATE**: corporate payer. |
| **information** | List     | N            | elements structure in list: **Info** | information to be verified                                                                       |

### Info

| **Attributes** | **Type** | **Required** | **Limitation**  | **Description**                                                                                                                                                                                                                                                                                                                                  |
| -------------- | -------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **category**   | string   | Y            | Enum value      | For Individual: <br/>**FIRST_NAME**<br/> **LAST_NAME**<br/> **DATE_OF_BIRTH**<br/> **NATIONALITY (2-letter country code)**-optional<br/> **DOCUMENT_TYPE**-optional<br/> **DOCUMENT_NUMBER**-optional <br/><br/>For corporate:<br/>**COMPANY_NAME**<br/> **REGISTRATION_NUMBER**<br/> **REGISTRATION_COUNTRY (2-letter country code)**           |
| **value**      | string   | Y            | max length 1024 | value of information <br/> For **DOCUMENT_TYPE**, available values are: ID_CARD/PASSPORT/DRIVING_LICENSE/VISA/CPF/OTHER/BVN_NUMBER/NIN_NUMBER/PAN/BVN_NIN_NUMBER/SMILEID_NATIONAL_ID/ABN/ACN/UA_DIA <br/> For **DATE_OF_BIRTH** format: YYYY-MM-DD<br/> For **NATIONALITY** and **REGISTRATION_COUNTRY** value is based on 2-letter country code |

### Sample Request Body

```json
{
  "binanceId": "400000001",
  "payerType": "INDIVIDUAL",
  "information": [
    {
      "category": "FIRST_NAME",
      "value": "binance"
    },
    {
      "category": "LAST_NAME",
      "value": "pay"
    },
    {
      "category": "DATE_OF_BIRTH",
      "value": "1980-01-01"
    }
  ]
}
```

## Response Parameters

| **Attributes**   | **Type** | **Required** | **Limitation**                      | **Description**                                |
| ---------------- | -------- | ------------ | ----------------------------------- | ---------------------------------------------- |
| **status**       | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | status of the API request                      |
| **code**         | string   | Y            | -                                   | request result code, [refer to ](#result-code) |
| **data**         | Boolean  | N            | -                                   | true means matched, false means not matched    |
| **errorMessage** | string   | N            | maximum length 256                  |                                                |

### Sample Response

#### verify success

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true
}
```

#### account of userId not existed

```json
{
  "status": "FAIL",
  "code": "400601",
  "errorMessage": "account not found"
}
```

#### kyc is not completed in binance side

```json
{
  "status": "FAIL",
  "code": "400722",
  "errorMessage": "kyc not completed"
}
```

#### kyc info mismatch, for example FIRST_NAME

```json
{
  "status": "FAIL",
  "code": "400102",
  "errorMessage": "Parameter information.FIRST_NAME not valid, the value is out of range."
}
```

#### too many failed request

```json
{
  "status": "FAIL",
  "code": "406108",
  "errorMessage": "Fail rate is high, please try again later"
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
| MERCHANT_TRANSFER_MERCHANT_TYPE_INVALID | 406107   | Merchant type not valid not support individual merchant                        |                                                                                                |
| MERCHANT_TRANSFER_MERCHANT_TOO_FREQUENT | 406108   | Fail rate is high, please try again later                                      |                                                                                                |