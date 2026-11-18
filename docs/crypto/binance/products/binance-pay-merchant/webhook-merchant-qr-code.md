---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-merchant-qr-code
api_type: Guide
updated_at: 2026-11-18 02:07:10.180575
---

# Merchant QR Code Notification

Binance Pay pushes a _Merchant QR Code_ event to the webhook endpoint configured in the Merchant
Management Platform each time a Binance user scans a merchant-owned QR code in the Binance App.

If the merchant endpoint does **not** return HTTP 200 OK (or the delivery fails), Binance Pay
retries up to **6** times.

**This is exclusively for Binance Pay official partnering partners. If you are interested, please
contact your BD contact or email us at merchant@binance.com**

---

## QR Code Types

| Type                | Description                                                                           |
| ------------------- | ------------------------------------------------------------------------------------- |
| `FIXED_AMOUNT`      | Fixed amount QR code, amount preset by merchant                                       |
| `USER_INPUT_AMOUNT` | User input amount QR code, requires user to manually input amount and select currency |

---

## Request Body

| Attribute | Type   | Required | Description                                                |
| --------- | ------ | -------- | ---------------------------------------------------------- |
| bizType   | string | Y        | Constant **`MERCHANT_QR_CODE`**                            |
| bizId     | long   | Y        | Unique identifier of this QR-scan event (equals `referId`) |
| bizIdStr  | string | Y        | `bizId` in string format                                   |
| bizStatus | string | Y        | Constant **`MERCHANT_QR_CODE_SCANED`**                     |
| data      | object | Y        | See **Data Object**                                        |

### Data Object

| Attribute  | Type   | Required    | Description                                                                                                                                                              |
| ---------- | ------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| qrContent  | string | Y           | Plain text extracted from the scanned QR code (usually a URL or payment string)                                                                                          |
| referId    | string | Y           | The same value as `bizIdStr`. Pass this value to the _Create Prepay Order V3_ API parameter **`qrCodeReferId`** so that Binance Pay can link the scan event to the order |
| qrCodeType | string | Y           | QR code type. Values: `FIXED_AMOUNT` or `USER_INPUT_AMOUNT`                                                                                                              |
| amount     | string | Conditional | User-inputted amount. Only present when `qrCodeType` is `USER_INPUT_AMOUNT`                                                                                              |
| currency   | string | Conditional | User-selected currency (e.g., "USDT", "BTC"). Only present when `qrCodeType` is `USER_INPUT_AMOUNT`                                                                      |

### Sample Payloads

#### Scenario A: FIXED_AMOUNT QR Code

```json
{
  "bizType": "MERCHANT_QR_CODE",
  "bizId": 368899096379834368,
  "bizIdStr": "368899096379834368",
  "bizStatus": "MERCHANT_QR_CODE_SCANED",
  "data": {
    "qrContent": "https://pay.partner.com/xx",
    "referId": "368899096379834368",
    "qrCodeType": "FIXED_AMOUNT"
  }
}
```

#### Scenario B: USER_INPUT_AMOUNT QR Code

Webhook is sent **after** user submits amount.

```json
{
  "bizType": "MERCHANT_QR_CODE",
  "bizId": 368899096379834368,
  "bizIdStr": "368899096379834368",
  "bizStatus": "MERCHANT_QR_CODE_SCANED",
  "data": {
    "qrContent": "https://pay.partner.com/xx",
    "referId": "368899096379834368",
    "qrCodeType": "USER_INPUT_AMOUNT",
    "amount": "100.50",
    "currency": "KGS"
  }
}
```

---

## Handling the Notification

1. Receive the notification and parse `qrContent` and `referId`.
2. Create a payment order through **Create Prepay Order V3** and put  
   `referId` into the request parameter **`qrCodeReferId`**. One qrCodeReferId only can be used
   once.
3. Reply to the webhook with HTTP 200 OK and the following body:

### Response Body

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message [refer to](#returnMessage)                                       |

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": null
}
```

If `returnCode` is not **`SUCCESS`** (or the HTTP status is not 200), Binance Pay will retry
delivery up to 6 times.

#### ReturnMessage Object For Error Case

<span id="returnMessage"></span>

| Attribute | Type   | Required | Description                                                                              |
| --------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| status    | string | Y        | Status of the operation. In error cases, this value is typically "REJECTED"              |
| code      | string | Y        | Error code that identifies the specific type of error (e.g., "AMOUNT_EXCEEDS_THRESHOLD") |

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": {
    "status": "REJECTED",
    "code": "AMOUNT_EXCEEDS_THRESHOLD"
  }
}
```

#### Error Codes

| Error Code                   | Description                                                                     | Binance Pay Behavior                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AMOUNT_EXCEEDS_THRESHOLD** | The payment amount exceeds the merchant's threshold limit                       | Binance Pay will prompt the user to use their device's native camera app to scan the QR code.                                                              |
| **UNSUPPORTED_QR_CODE**      | The scanned QR code is not supported by merchant right now                      | Binance Pay will prompt the user: order details are still being processed, please scan the QR code again shortly.                                          |
| **EXPIRED**                  | QR has expired, cashier will need to regenerate another QR for user to scan     | Display error message: "QR code has expired. Please contact the merchant to generate a new QR code for scanning." with a "Retry" button.                   |
| **BPAY_UNSUPPORTED**         | Binance Pay not supported for the QR code scanned                               | Display error message: "The QR code is not supported." with a "Done" button.                                                                               |
| **GENERAL_ERROR**            | Service unavailable error                                                       | Display error message: "Merchant service temporarily unavailable, please try again shortly or contact the merchant for assistance." with a "Retry" button. |
| **QR_PAID**                  | QR code scanned is PAID                                                         | Display error message: "The order has been paid, please contact the merchant for assistance." with a "Done" button.                                        |
| **UNSUPPORTED_STATIC_QR**    | Static QR (user manual input amount) is not supported, user to use merchant app | Display error message: "This QR code cannot be processed. Please scan the QR with a supported app to continue with payment." with a "Done" button.         |
| **INVALID_AMOUNT**           | The amount is invalid or out of acceptable range                                | Display error message: "Invalid amount. Please try again." with a "Retry" button.                                                                          |
| **INVALID_CURRENCY**         | The currency is not supported                                                   | Display error message: "Currency not supported. Please select a different currency." with a "Retry" button.                                                |

---

## Event Life-cycle Diagram

### Flow A: Fixed Amount (FIXED_AMOUNT)

```
User scan QR → Binance Pay → Merchant Webhook
                           ↘ receives (qrContent, referId, qrCodeType=FIXED_AMOUNT)
                            Merchant creates order
                            Create Prepay Order V3 (qrCodeReferId = referId)
```

### Flow B: User Input Amount (USER_INPUT_AMOUNT)

```
User scan QR → Binance Pay → Return currency list to user
                           ↘ User inputs amount + selects currency
                            User submits amount
                           → Binance Pay → Merchant Webhook
                                         ↘ receives (qrContent, referId, qrCodeType=USER_INPUT_AMOUNT, amount, currency)
                                          Merchant creates order based on amount
                                          Create Prepay Order V3 (qrCodeReferId = referId)
```

---

---

# Merchant QR Code Notification

Binance Pay pushes a _Merchant QR Code_ event to the webhook endpoint configured in the Merchant
Management Platform each time a Binance user scans a merchant-owned QR code in the Binance App.

If the merchant endpoint does **not** return HTTP 200 OK (or the delivery fails), Binance Pay
retries up to **6** times.

**This is exclusively for Binance Pay official partnering partners. If you are interested, please
contact your BD contact or email us at merchant@binance.com**

---

## QR Code Types

| Type                | Description                                                                           |
| ------------------- | ------------------------------------------------------------------------------------- |
| `FIXED_AMOUNT`      | Fixed amount QR code, amount preset by merchant                                       |
| `USER_INPUT_AMOUNT` | User input amount QR code, requires user to manually input amount and select currency |

---

## Request Body

| Attribute | Type   | Required | Description                                                |
| --------- | ------ | -------- | ---------------------------------------------------------- |
| bizType   | string | Y        | Constant **`MERCHANT_QR_CODE`**                            |
| bizId     | long   | Y        | Unique identifier of this QR-scan event (equals `referId`) |
| bizIdStr  | string | Y        | `bizId` in string format                                   |
| bizStatus | string | Y        | Constant **`MERCHANT_QR_CODE_SCANED`**                     |
| data      | object | Y        | See **Data Object**                                        |

### Data Object

| Attribute  | Type   | Required    | Description                                                                                                                                                              |
| ---------- | ------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| qrContent  | string | Y           | Plain text extracted from the scanned QR code (usually a URL or payment string)                                                                                          |
| referId    | string | Y           | The same value as `bizIdStr`. Pass this value to the _Create Prepay Order V3_ API parameter **`qrCodeReferId`** so that Binance Pay can link the scan event to the order |
| qrCodeType | string | Y           | QR code type. Values: `FIXED_AMOUNT` or `USER_INPUT_AMOUNT`                                                                                                              |
| amount     | string | Conditional | User-inputted amount. Only present when `qrCodeType` is `USER_INPUT_AMOUNT`                                                                                              |
| currency   | string | Conditional | User-selected currency (e.g., "USDT", "BTC"). Only present when `qrCodeType` is `USER_INPUT_AMOUNT`                                                                      |

### Sample Payloads

#### Scenario A: FIXED_AMOUNT QR Code

```json
{
  "bizType": "MERCHANT_QR_CODE",
  "bizId": 368899096379834368,
  "bizIdStr": "368899096379834368",
  "bizStatus": "MERCHANT_QR_CODE_SCANED",
  "data": {
    "qrContent": "https://pay.partner.com/xx",
    "referId": "368899096379834368",
    "qrCodeType": "FIXED_AMOUNT"
  }
}
```

#### Scenario B: USER_INPUT_AMOUNT QR Code

Webhook is sent **after** user submits amount.

```json
{
  "bizType": "MERCHANT_QR_CODE",
  "bizId": 368899096379834368,
  "bizIdStr": "368899096379834368",
  "bizStatus": "MERCHANT_QR_CODE_SCANED",
  "data": {
    "qrContent": "https://pay.partner.com/xx",
    "referId": "368899096379834368",
    "qrCodeType": "USER_INPUT_AMOUNT",
    "amount": "100.50",
    "currency": "KGS"
  }
}
```

---

## Handling the Notification

1. Receive the notification and parse `qrContent` and `referId`.
2. Create a payment order through **Create Prepay Order V3** and put  
   `referId` into the request parameter **`qrCodeReferId`**. One qrCodeReferId only can be used
   once.
3. Reply to the webhook with HTTP 200 OK and the following body:

### Response Body

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message [refer to](#returnMessage)                                       |

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": null
}
```

If `returnCode` is not **`SUCCESS`** (or the HTTP status is not 200), Binance Pay will retry
delivery up to 6 times.

#### ReturnMessage Object For Error Case

<span id="returnMessage"></span>

| Attribute | Type   | Required | Description                                                                              |
| --------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| status    | string | Y        | Status of the operation. In error cases, this value is typically "REJECTED"              |
| code      | string | Y        | Error code that identifies the specific type of error (e.g., "AMOUNT_EXCEEDS_THRESHOLD") |

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": {
    "status": "REJECTED",
    "code": "AMOUNT_EXCEEDS_THRESHOLD"
  }
}
```

#### Error Codes

| Error Code                   | Description                                                                     | Binance Pay Behavior                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AMOUNT_EXCEEDS_THRESHOLD** | The payment amount exceeds the merchant's threshold limit                       | Binance Pay will prompt the user to use their device's native camera app to scan the QR code.                                                              |
| **UNSUPPORTED_QR_CODE**      | The scanned QR code is not supported by merchant right now                      | Binance Pay will prompt the user: order details are still being processed, please scan the QR code again shortly.                                          |
| **EXPIRED**                  | QR has expired, cashier will need to regenerate another QR for user to scan     | Display error message: "QR code has expired. Please contact the merchant to generate a new QR code for scanning." with a "Retry" button.                   |
| **BPAY_UNSUPPORTED**         | Binance Pay not supported for the QR code scanned                               | Display error message: "The QR code is not supported." with a "Done" button.                                                                               |
| **GENERAL_ERROR**            | Service unavailable error                                                       | Display error message: "Merchant service temporarily unavailable, please try again shortly or contact the merchant for assistance." with a "Retry" button. |
| **QR_PAID**                  | QR code scanned is PAID                                                         | Display error message: "The order has been paid, please contact the merchant for assistance." with a "Done" button.                                        |
| **UNSUPPORTED_STATIC_QR**    | Static QR (user manual input amount) is not supported, user to use merchant app | Display error message: "This QR code cannot be processed. Please scan the QR with a supported app to continue with payment." with a "Done" button.         |
| **INVALID_AMOUNT**           | The amount is invalid or out of acceptable range                                | Display error message: "Invalid amount. Please try again." with a "Retry" button.                                                                          |
| **INVALID_CURRENCY**         | The currency is not supported                                                   | Display error message: "Currency not supported. Please select a different currency." with a "Retry" button.                                                |

---

## Event Life-cycle Diagram

### Flow A: Fixed Amount (FIXED_AMOUNT)

```
User scan QR → Binance Pay → Merchant Webhook
                           ↘ receives (qrContent, referId, qrCodeType=FIXED_AMOUNT)
                            Merchant creates order
                            Create Prepay Order V3 (qrCodeReferId = referId)
```

### Flow B: User Input Amount (USER_INPUT_AMOUNT)

```
User scan QR → Binance Pay → Return currency list to user
                           ↘ User inputs amount + selects currency
                            User submits amount
                           → Binance Pay → Merchant Webhook
                                         ↘ receives (qrContent, referId, qrCodeType=USER_INPUT_AMOUNT, amount, currency)
                                          Merchant creates order based on amount
                                          Create Prepay Order V3 (qrCodeReferId = referId)
```

---