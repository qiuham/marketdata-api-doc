---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-common
api_type: Guide
updated_at: 2026-11-20 18:36:15.782520
---

# API Specification Common Rules

For Security Purpose, Binance and IPs will both ensure https-based call back endpoints. And
signature checks for APIs.

## Protocol Rules

The following specifies the rules for calling the API when accessing Binance payment.

| **Rule**                       | **Description**                                                      |
| ------------------------------ | -------------------------------------------------------------------- |
| **Transfer Mode**              | Use HTTPS for secure transactions.                                   |
| **Submit Mode**                | POST/GET, depends on the API.                                        |
| **Data Format (content-type)** | Data submitted and response are both in **application/json** format. |
| **Char Encoding**              | Use UTF-8 character encoding.                                        |
| **Signature Algorithm**        | HMAC-SHA512.                                                         |
| **Signature Requirement**      | Signature-checking is required for requesting and receiving data.    |
| **Logic Judgment**             | Determine protocol field, service field and transaction status.      |

## Request Header

| **Attributes**                | **Type** | **Required** | **Limitation**                               | **Description**                                                                                                       |
| ----------------------------- | -------- | ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **content-type**              | string   | Y            | application/json                             | content type                                                                                                          |
| **BinancePay-Timestamp**      | long     | Y            | Binance pay only process request within 1s   | UnixTimestamp in milliseconds that the requests send, guarantee the machine time is sync with the network             |
| **BinancePay-Nonce**          | string   | Y            | must be 32 digits                            | A random string with 32 bytes, e.g. random ascii decimal within a-z and A-Z and loop 32 times to form a random string |
| **BinancePay-Certificate-SN** | string   | Y            | -                                            | API identity key issued by Binance payment system                                                                     |
| **BinancePay-Signature**      | string   | Y            | this should use SHA512, and be in upper case | signature, [signature generation](#signature)                                                                         |

## Signature

<span id="signature"></span>

### Build the content

```java
String payload = timestamp + "\n" + nonce + "\n" + body + "\n";
```

### Sign the content

```java
String signature = hex(hmac("sha512", payload, secretKey)).toUpperCase()
```

---

**NOTE**

- ‘\n’ is LF, ASCII value is '0x0A'
- Parameter names are case-sensitive;
- When checking returned data or a push notification signature, the transferred sign parameter is
  excluded in this signature as it is compared with the created signature.
- When post the Json body, carefully check the quote, **'** is not same as **"**

---

## Hosts

```json
https://bpay.binanceapi.com
```

## Common Business Errors

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOW_ERROR                       | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported                                                   | Use POST http method                                                                           |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported                                                       | Add header Content-Type: application/json                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object                                        | Check the request body format                                                                  |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                               |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |

---

# API Specification Common Rules

For Security Purpose, Binance and IPs will both ensure https-based call back endpoints. And
signature checks for APIs.

## Protocol Rules

The following specifies the rules for calling the API when accessing Binance payment.

| **Rule**                       | **Description**                                                      |
| ------------------------------ | -------------------------------------------------------------------- |
| **Transfer Mode**              | Use HTTPS for secure transactions.                                   |
| **Submit Mode**                | POST/GET, depends on the API.                                        |
| **Data Format (content-type)** | Data submitted and response are both in **application/json** format. |
| **Char Encoding**              | Use UTF-8 character encoding.                                        |
| **Signature Algorithm**        | HMAC-SHA512.                                                         |
| **Signature Requirement**      | Signature-checking is required for requesting and receiving data.    |
| **Logic Judgment**             | Determine protocol field, service field and transaction status.      |

## Request Header

| **Attributes**                | **Type** | **Required** | **Limitation**                               | **Description**                                                                                                       |
| ----------------------------- | -------- | ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **content-type**              | string   | Y            | application/json                             | content type                                                                                                          |
| **BinancePay-Timestamp**      | long     | Y            | Binance pay only process request within 1s   | UnixTimestamp in milliseconds that the requests send, guarantee the machine time is sync with the network             |
| **BinancePay-Nonce**          | string   | Y            | must be 32 digits                            | A random string with 32 bytes, e.g. random ascii decimal within a-z and A-Z and loop 32 times to form a random string |
| **BinancePay-Certificate-SN** | string   | Y            | -                                            | API identity key issued by Binance payment system                                                                     |
| **BinancePay-Signature**      | string   | Y            | this should use SHA512, and be in upper case | signature, [signature generation](#signature)                                                                         |

## Signature

<span id="signature"></span>

### Build the content

```java
String payload = timestamp + "\n" + nonce + "\n" + body + "\n";
```

### Sign the content

```java
String signature = hex(hmac("sha512", payload, secretKey)).toUpperCase()
```

---

**NOTE**

- ‘\n’ is LF, ASCII value is '0x0A'
- Parameter names are case-sensitive;
- When checking returned data or a push notification signature, the transferred sign parameter is
  excluded in this signature as it is compared with the created signature.
- When post the Json body, carefully check the quote, **'** is not same as **"**

---

## Hosts

```json
https://bpay.binanceapi.com
```

## Common Business Errors

| **Name**                           | **Code** | **Reason**                                                                     | **Solution**                                                                                   |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| UNKNOW_ERROR                       | 400000   | An unknown error occurred while processing the request.                        | Try again later                                                                                |
| INVALID_REQUEST                    | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules.  | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                  | 400002   | Incorrect signature result                                                     | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                  | 400003   | Timestamp for this request is outside of the time window.                      | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP              | 400004   | API identity key not found or invalid.                                         | Check API identity key                                                                         |
| BAD_API_KEY_FMT                    | 400005   | API identity key format invalid.                                               | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                    | 400006   | Request method not supported                                                   | Use POST http method                                                                           |
| MEDIA_TYPE_NOT_SUPPORTED           | 400007   | Media type not supported                                                       | Add header Content-Type: application/json                                                      |
| INVALID_REQUEST_BODY               | 400008   | Request body is not a valid json object                                        | Check the request body format                                                                  |
| MANDATORY_PARAM_EMPTY_OR_MALFORMED | 400100   | A parameter was missing/empty/null, or malformed.                              |                                                                                                |
| INVALID_PARAM_WRONG_LENGTH         | 400101   | A parameter was not valid, was empty/null, or too long/short, or wrong format. |                                                                                                |
| INVALID_PARAM_WRONG_VALUE          | 400102   | A parameter was not valid, the value is out of range.                          |                                                                                                |
| INVALID_PARAM_ILLEGAL_CHAR         | 400103   | A parameter was not valid, contains illegal characters                         |                                                                                                |
| INVALID_REQUEST_TOO_LARGE          | 400104   | Invalid request, content length too large                                      |                                                                                                |
| INVALID_MERCHANT_TRADE_NO          | 400201   | merchantTradeNo is invalid or duplicated                                       |                                                                                                |
| ORDER_NOT_FOUND                    | 400202   | Order not found.                                                               |                                                                                                |
| INVALID_ACCOUNT_STATUS             | 400203   | Not support for this account, please check account status.                     |                                                                                                |