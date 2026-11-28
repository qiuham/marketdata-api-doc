---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-payout-validate-receiver
api_type: Guide
updated_at: 2026-11-28 18:33:35.033470
---

# Payout Validate Receiver

Payout Receiver API is for Merchant/Partner to validate and match receiver's registration
information (email/phone no) and openUserID. Not supported for individual merchants to invoke this
API.

## EndPoint

```http request
POST /binancepay/openapi/payout/receiver/check
```

## Request Parameters

| **Attributes**               | **Type** | **Required** | **Limitation** | **Description**                                                  |
| ---------------------------- | -------- | ------------ | -------------- | ---------------------------------------------------------------- |
| **receiveType**              | string   | Y            | Enum value     | Receiver's ID type <br /><br /> **BINANCE_ID**: Binance user ID. |
| **receiverId**               | string   | Y            |                | Receiver's BINANCE_ID depends on the receiver type.<br />        |
| **registrationEmail**        | String   | N            |                | Receiver's registration email address                            |
| **registrationMobileNumber** | String   | N            |                | Receiver's mobile number                                         |
| **registrationMobileCode**   | String   | N            |                | Receiver's mobile code eg:971 for UAE                            |
| **openUserId**               | String   | N            |                | Receiver’s openUserId received in webhook notification           |

### Sample Request Body

```json
{
  "receiveType": "BINANCE_ID",
  "receiverId": "400000001",
  "registrationEmail": "xxx@gmail.com",
  "registrationMobileNumber": "322342111",
  "registrationMobileCode": "971"
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

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true
}
```

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

# Payout Validate Receiver

Payout Receiver API is for Merchant/Partner to validate and match receiver's registration
information (email/phone no) and openUserID. Not supported for individual merchants to invoke this
API.

## EndPoint

```http request
POST /binancepay/openapi/payout/receiver/check
```

## Request Parameters

| **Attributes**               | **Type** | **Required** | **Limitation** | **Description**                                                  |
| ---------------------------- | -------- | ------------ | -------------- | ---------------------------------------------------------------- |
| **receiveType**              | string   | Y            | Enum value     | Receiver's ID type <br /><br /> **BINANCE_ID**: Binance user ID. |
| **receiverId**               | string   | Y            |                | Receiver's BINANCE_ID depends on the receiver type.<br />        |
| **registrationEmail**        | String   | N            |                | Receiver's registration email address                            |
| **registrationMobileNumber** | String   | N            |                | Receiver's mobile number                                         |
| **registrationMobileCode**   | String   | N            |                | Receiver's mobile code eg:971 for UAE                            |
| **openUserId**               | String   | N            |                | Receiver’s openUserId received in webhook notification           |

### Sample Request Body

```json
{
  "receiveType": "BINANCE_ID",
  "receiverId": "400000001",
  "registrationEmail": "xxx@gmail.com",
  "registrationMobileNumber": "322342111",
  "registrationMobileCode": "971"
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

```json
{
  "status": "SUCCESS",
  "code": "000000",
  "data": true
}
```

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