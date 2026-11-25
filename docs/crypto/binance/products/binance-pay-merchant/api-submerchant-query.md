---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-submerchant-query
api_type: Guide
updated_at: 2026-11-25 18:34:03.000968
---

# Query SubMerchant

Query submerchant for management purpose. This is available for Partner only.

## EndPoint

```http request
POST /binancepay/openapi/submerchant/query
```

## Request Parameters

Exactly **one** of `subMerchantId` and `subMerchantName` must be provided. Passing both, or passing
neither, will return an `INVALID_PARAM_WRONG_VALUE` error.

| **Attributes**      | **Type** | **Required**                         | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | -------- | ------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**   | string   | Conditional (exactly one of the two) | maximum length 128 | Sub-merchant ID to query.                                                                                                                                                                                                                                                                                                                                  |
| **subMerchantName** | string   | Conditional (exactly one of the two) | maximum length 128 | Sub-merchant name to query. The lookup is scoped to the caller's `mainMerchantId`, and the name is unique within that scope (see `subMerchantName` uniqueness contract in [SubMerchant Add](./api-submerchant-add)). Typical use case: before bulk-creating sub-merchants, check whether a given name is already taken so the caller can rename and retry. |

### Sample Request Body — Query by ID

```json
{
  "subMerchantId": "1234567"
}
```

### Sample Request Body — Query by Name

```json
{
  "subMerchantName": "Acme Coffee Shop"
}
```

## Response Parameters

When querying by `subMerchantName`, if no sub-merchant with the given name exists under the caller's
main merchant, the response returns success with `data: null` — the name is available for a
subsequent `submerchant/add` call. Querying by `subMerchantId` with a non-existent id returns
`INVALID_PARAM_WRONG_VALUE` (existing behavior, unchanged).

## Response Parameters

| **Attributes**                | **Type** | **Required** | **Limitation** | **Description**                                                                                                                                                                                       |
| ----------------------------- | -------- | ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **merchantName**              | string   | Y            |                | The sub merchant name maximum length 128, unique under one mainMerchantId.                                                                                                                            |
| **storeType**                 | int      | Y            |                | 0=Online , 1=Physical, -1=Online&Physical                                                                                                                                                             |
| **merchantMcc**               | string   | Y            |                | four-digit number that classifies the business. Get from [here](#MCC)                                                                                                                                 |
| **merchantType**              | int      | N            |                | 2=solo proprietor、 3=Partnership、4=Private company、5=Others company                                                                                                                                |
| **country**                   | string   | Y            |                | Country/Region of Business Operation,Can be multiple, split by "," eg:"AR,MX". Refer to link(https://merchant.binance.com/en/application-guidelines-merchant) for restricted countries of operations. |
| **siteUrl**                   | string   | N            |                | For Online stores, the URL field is required. (If your online store is an APP, please pass its link in the app store )                                                                                |
| **address**                   | string   | N            |                | For Physical stores, the address field is required.                                                                                                                                                   |
| **payIndustryDescription**    | string   | N            |                | Mandatory if merchantMcc is 9999. Please specify the industry of this sub merchant here.                                                                                                              |
| **subPayMccCode**             | string   | N            |                | four-digit number that classifies the business. Get from [here](#MCC)                                                                                                                                 |
| **subPayIndustryDescription** | string   | N            |                | Mandatory if subPayMccCode is 9999. Please specify the industry of this sub merchant here.                                                                                                            |
| **brandLogo**                 | string   | N            |                | sub merchant logo url                                                                                                                                                                                 |
| **companyName**               | string   | N            |                | The legal name that is used in the registration.                                                                                                                                                      |
| **registrationNumber**        | string   | Y            |                | Registration number/Company tax ID                                                                                                                                                                    |
| **registrationCountry**       | string   | Y            |                | Country of Registration                                                                                                                                                                               |
| **registrationAddress**       | string   | N            |                | Address of Registration. Refer to link(https://merchant.binance.com/en/application-guidelines-merchant) for restricted registration addresses.                                                        |
| **incorporationDate**         | long     | N            |                | The date when the business registration is in effective.                                                                                                                                              |
| **certificateType**           | int      | N            |                | 1=ID 2=Passport                                                                                                                                                                                       |
| **certificateCountry**        | string   | N            |                | Certificate country                                                                                                                                                                                   |
| **certificateNumber**         | string   | N            |                | Certificate number                                                                                                                                                                                    |
| **certificateValidDate**      | long     | N            |                | Certificate Valid Date                                                                                                                                                                                |
| **contractTimeIsv**           | long     | N            |                | Contract date with ISV                                                                                                                                                                                |
| **blockKybUserPayment**       | boolean  | N            |                | block kyb users to pay this sub merchant, default false                                                                                                                                               |
| **businessRegistrationType**  | string   | N            |                | The type of business registration certificate 'UPLOAD' or 'SITE'                                                                                                                                      |
| **businessRegistrationValue** | string   | N            |                | The value of business registration certificate url                                                                                                                                                    |

### Sample Response

```json
{
  "merchantName": "Sub Merchant",
  "storeType": 1,
  "merchantMcc": "5411",
  "merchantType": 1,
  "country": "US",
  "siteUrl": "http://example.com",
  "address": "123 Main St, Anytown, USA",
  "payIndustryDescription": "Retail Industry",
  "subPayMccCode": "5411",
  "subPayIndustryDescription": "Retail Industry",
  "brandLogo": "http://example.com/logo.png",
  "companyName": "Company Name",
  "registrationNumber": "123456789",
  "registrationCountry": "US",
  "registrationAddress": "123 Main St, Anytown, USA",
  "incorporationDate": "2023-01-01T00:00:00Z",
  "certificateType": 1,
  "certificateCountry": "US",
  "certificateNumber": "Cert123",
  "certificateValidDate": "2023-01-01T00:00:00Z",
  "contractTimeIsv": "2023-01-01T00:00:00Z",
  "blockKybUserPayment": false,
  "businessRegistrationType": "SITE",
  "businessRegistrationValue": "http://www.example.com"
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                                                                                                  |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                                                                                               |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                                                                                                              |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements.                                                                                |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                                                                                                             |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                                                                                                        |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                                                                                                       |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                  | Check Request method.                                                                                                                                                         |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                                                                                                     |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                                                                                                            |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                                                                                               |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                                                                                               |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          | Returned when both `subMerchantId` and `subMerchantName` are provided, when neither is provided, or when the `subMerchantId` does not exist under the caller's main merchant. |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                                                                                               |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                                                                                               |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                                                                                               |
| SUB_MERCHANT_EXISTS                | 400205   | Sub-merchant already exists.                                                   | Please check merchant name                                                                                                                                                    |
| PAYMENT_MERCHANT_NOT_FOUND         | 400208   | Merchant not found.                                                            | Please check your merchantId                                                                                                                                                  |
| PAYMENT_ACTION_TOO_FREQUENT        | 400501   | action Too Frequent, get the lock fail                                         | Try again later                                                                                                                                                               |

```

```

---

# Query SubMerchant

Query submerchant for management purpose. This is available for Partner only.

## EndPoint

```http request
POST /binancepay/openapi/submerchant/query
```

## Request Parameters

Exactly **one** of `subMerchantId` and `subMerchantName` must be provided. Passing both, or passing
neither, will return an `INVALID_PARAM_WRONG_VALUE` error.

| **Attributes**      | **Type** | **Required**                         | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | -------- | ------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **subMerchantId**   | string   | Conditional (exactly one of the two) | maximum length 128 | Sub-merchant ID to query.                                                                                                                                                                                                                                                                                                                                  |
| **subMerchantName** | string   | Conditional (exactly one of the two) | maximum length 128 | Sub-merchant name to query. The lookup is scoped to the caller's `mainMerchantId`, and the name is unique within that scope (see `subMerchantName` uniqueness contract in [SubMerchant Add](./api-submerchant-add)). Typical use case: before bulk-creating sub-merchants, check whether a given name is already taken so the caller can rename and retry. |

### Sample Request Body — Query by ID

```json
{
  "subMerchantId": "1234567"
}
```

### Sample Request Body — Query by Name

```json
{
  "subMerchantName": "Acme Coffee Shop"
}
```

## Response Parameters

When querying by `subMerchantName`, if no sub-merchant with the given name exists under the caller's
main merchant, the response returns success with `data: null` — the name is available for a
subsequent `submerchant/add` call. Querying by `subMerchantId` with a non-existent id returns
`INVALID_PARAM_WRONG_VALUE` (existing behavior, unchanged).

## Response Parameters

| **Attributes**                | **Type** | **Required** | **Limitation** | **Description**                                                                                                                                                                                       |
| ----------------------------- | -------- | ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **merchantName**              | string   | Y            |                | The sub merchant name maximum length 128, unique under one mainMerchantId.                                                                                                                            |
| **storeType**                 | int      | Y            |                | 0=Online , 1=Physical, -1=Online&Physical                                                                                                                                                             |
| **merchantMcc**               | string   | Y            |                | four-digit number that classifies the business. Get from [here](#MCC)                                                                                                                                 |
| **merchantType**              | int      | N            |                | 2=solo proprietor、 3=Partnership、4=Private company、5=Others company                                                                                                                                |
| **country**                   | string   | Y            |                | Country/Region of Business Operation,Can be multiple, split by "," eg:"AR,MX". Refer to link(https://merchant.binance.com/en/application-guidelines-merchant) for restricted countries of operations. |
| **siteUrl**                   | string   | N            |                | For Online stores, the URL field is required. (If your online store is an APP, please pass its link in the app store )                                                                                |
| **address**                   | string   | N            |                | For Physical stores, the address field is required.                                                                                                                                                   |
| **payIndustryDescription**    | string   | N            |                | Mandatory if merchantMcc is 9999. Please specify the industry of this sub merchant here.                                                                                                              |
| **subPayMccCode**             | string   | N            |                | four-digit number that classifies the business. Get from [here](#MCC)                                                                                                                                 |
| **subPayIndustryDescription** | string   | N            |                | Mandatory if subPayMccCode is 9999. Please specify the industry of this sub merchant here.                                                                                                            |
| **brandLogo**                 | string   | N            |                | sub merchant logo url                                                                                                                                                                                 |
| **companyName**               | string   | N            |                | The legal name that is used in the registration.                                                                                                                                                      |
| **registrationNumber**        | string   | Y            |                | Registration number/Company tax ID                                                                                                                                                                    |
| **registrationCountry**       | string   | Y            |                | Country of Registration                                                                                                                                                                               |
| **registrationAddress**       | string   | N            |                | Address of Registration. Refer to link(https://merchant.binance.com/en/application-guidelines-merchant) for restricted registration addresses.                                                        |
| **incorporationDate**         | long     | N            |                | The date when the business registration is in effective.                                                                                                                                              |
| **certificateType**           | int      | N            |                | 1=ID 2=Passport                                                                                                                                                                                       |
| **certificateCountry**        | string   | N            |                | Certificate country                                                                                                                                                                                   |
| **certificateNumber**         | string   | N            |                | Certificate number                                                                                                                                                                                    |
| **certificateValidDate**      | long     | N            |                | Certificate Valid Date                                                                                                                                                                                |
| **contractTimeIsv**           | long     | N            |                | Contract date with ISV                                                                                                                                                                                |
| **blockKybUserPayment**       | boolean  | N            |                | block kyb users to pay this sub merchant, default false                                                                                                                                               |
| **businessRegistrationType**  | string   | N            |                | The type of business registration certificate 'UPLOAD' or 'SITE'                                                                                                                                      |
| **businessRegistrationValue** | string   | N            |                | The value of business registration certificate url                                                                                                                                                    |

### Sample Response

```json
{
  "merchantName": "Sub Merchant",
  "storeType": 1,
  "merchantMcc": "5411",
  "merchantType": 1,
  "country": "US",
  "siteUrl": "http://example.com",
  "address": "123 Main St, Anytown, USA",
  "payIndustryDescription": "Retail Industry",
  "subPayMccCode": "5411",
  "subPayIndustryDescription": "Retail Industry",
  "brandLogo": "http://example.com/logo.png",
  "companyName": "Company Name",
  "registrationNumber": "123456789",
  "registrationCountry": "US",
  "registrationAddress": "123 Main St, Anytown, USA",
  "incorporationDate": "2023-01-01T00:00:00Z",
  "certificateType": 1,
  "certificateCountry": "US",
  "certificateNumber": "Cert123",
  "certificateValidDate": "2023-01-01T00:00:00Z",
  "contractTimeIsv": "2023-01-01T00:00:00Z",
  "blockKybUserPayment": false,
  "businessRegistrationType": "SITE",
  "businessRegistrationValue": "http://www.example.com"
}
```

## Result Code

<span id="result-code"></span>

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                                                                                                  |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                      | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                                                                                               |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                                                                                                              |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements.                                                                                |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                                                                                                             |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                                                                                                        |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                                                                                                       |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported.                                                  | Check Request method.                                                                                                                                                         |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported.                                                      | Check Request Media type.                                                                                                                                                     |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object.                                       | Check Request body                                                                                                                                                            |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                                                                                               |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                                                                                               |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          | Returned when both `subMerchantId` and `subMerchantName` are provided, when neither is provided, or when the `subMerchantId` does not exist under the caller's main merchant. |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                                                                                               |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                                                                                               |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                                                                                               |
| SUB_MERCHANT_EXISTS                | 400205   | Sub-merchant already exists.                                                   | Please check merchant name                                                                                                                                                    |
| PAYMENT_MERCHANT_NOT_FOUND         | 400208   | Merchant not found.                                                            | Please check your merchantId                                                                                                                                                  |
| PAYMENT_ACTION_TOO_FREQUENT        | 400501   | action Too Frequent, get the lock fail                                         | Try again later                                                                                                                                                               |

```

```