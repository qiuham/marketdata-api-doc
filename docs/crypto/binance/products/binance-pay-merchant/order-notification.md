---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/order-notification
api_type: Guide
updated_at: 2026-11-18 18:32:32.222009
---

# Binance Pay: Order Notification

## Webhook Endpoints

Binance Pay will send order events with final status to partner for notification. You will be able
to configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard). Result of the orders
that are close will be notified to you through this webhook with bizStatus =
"PAY_CLOSED".<font color=red>\*</font>

<font color=red>\*If you don't want to receive "PAY_CLOSED" notifications anymore, you can login MMP
and select Developer menu -> Notification to turn it off.</font>

In situation where event was failed to send, the webhook will retry up to 6 times to resend the
event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                          |
| -------------- | -------- | ------------ | -------------- | -------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;PAY&#34;                                            |
| **bizId**      | long     | Y            | -              | Prepay order id                                          |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                         |
| **bizStatus**  | string   | Y            | -              | &#34;PAY_SUCCESS&#34;,&#34;PAY_CLOSED&#34;               |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data) |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                                       |
| ------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **merchantTradeNo** | string   | Y            | letter or digit, no other symbol allowed                                                                      | The order id, Unique identifier for the request                       |
| **productType**     | string   | Y            | maximum length 16                                                                                             | product type                                                          |
| **productName**     | string   | Y            | maximum length 256                                                                                            | product name                                                          |
| **transactTime**    | long     | Y            | -                                                                                                             | transaction time                                                      |
| **tradeType**       | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                                                      |
| **totalFee**        | decimal  | Y            | -                                                                                                             | order amount                                                          |
| **currency**        | string   | Y            | -                                                                                                             | order currency                                                        |
| **transactionId**   | string   | N            | -                                                                                                             | debit transaction id                                                  |
| **openUserId**      | string   | N            | -                                                                                                             | payer unique id                                                       |
| **passThroughInfo** | string   | N            | -                                                                                                             | pass through info, from the create order api                          |
| **commission**      | decimal  | Y            | -                                                                                                             | Transaction fees charged. Please refer to your contract for more info |
| **paymentInfo**     | object   | N            | -                                                                                                             | payment information, [refer to](#paymentInfo-data)                    |

### PaymentInfo Data

<span id="paymentInfo-data"></span>

| **Attributes**          | **Type**                 | **Required** | **Limitation** | **Description**                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------ | ------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **payMethod**           | string                   | Y            | -              | pay method                                                                                                                                                                                                                                                                                         |
| **paymentInstructions** | list[PaymentInstruction] | Y            | -              | payment instruction list, [refer to](#paymentInstruction-data)                                                                                                                                                                                                                                     |
| **channel**             | string                   | N            | -              | channel                                                                                                                                                                                                                                                                                            |
| **subChannel**          | string                   | N            | -              | sub channel                                                                                                                                                                                                                                                                                        |
| **payerDetail**         | string                   | N            | -              | encrypted payer identity information for merchant compliance purposes without compromising privacy and security. Decryption instructions please [refer to](authentication#decryption-instructions-for-merchant-data-sharing). <br/> **This function is only available for whitelisted merchants.** |

### PaymentInstruction Data

<span id="paymentInstruction-data"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**  |
| -------------- | -------- | ------------ | -------------- | ---------------- |
| **currency**   | string   | Y            | -              | payment currency |
| **amount**     | decimal  | Y            | -              | currency amount  |
| **price**      | decimal  | Y            | -              | currency price   |

### Sample Payload

#### PAY SUCCESS

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"xr6wYe8ATWE6thS5Sc7ezMihMFGKn6\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"transactTime\":1619508939664,\"tradeType\":\"APP\",\"totalFee\":0.88000000,\"currency\":\"USDT\",\"transactionId\":\"M_R_282737362839373\",\"openUserId\":\"1211HS10K81f4273ac031\",\"commission\":0.0088,\"paymentInfo\":{\"payMethod\":\"funding\",\"paymentInstructions\":[{\"currency\":\"USDT\",\"amount\":0.88000000,\"price\":1}],\"channel\":\"DEFAULT\"}}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_SUCCESS"
}
```

#### PAY FAIL

PAY_FAIL order status is only applicable to Direct Debit order. Normal C2B orders will only receive
PAY_SUCCESS or PAY_CLOSE status.

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"USDT\",\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\"}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_FAIL"
}
```

## Response Parameters

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message                                                                  |

### Sample Response

**After receiving a webhook with your endpoint, please respond with an HTTP 200 OK.**

```json
{ "returnCode": "SUCCESS", "returnMessage": null }
```

---

# Binance Pay: Order Notification

## Webhook Endpoints

Binance Pay will send order events with final status to partner for notification. You will be able
to configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard). Result of the orders
that are close will be notified to you through this webhook with bizStatus =
"PAY_CLOSED".<font color=red>\*</font>

<font color=red>\*If you don't want to receive "PAY_CLOSED" notifications anymore, you can login MMP
and select Developer menu -> Notification to turn it off.</font>

In situation where event was failed to send, the webhook will retry up to 6 times to resend the
event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                          |
| -------------- | -------- | ------------ | -------------- | -------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;PAY&#34;                                            |
| **bizId**      | long     | Y            | -              | Prepay order id                                          |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                         |
| **bizStatus**  | string   | Y            | -              | &#34;PAY_SUCCESS&#34;,&#34;PAY_CLOSED&#34;               |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data) |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**      | **Type** | **Required** | **Limitation**                                                                                                | **Description**                                                       |
| ------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **merchantTradeNo** | string   | Y            | letter or digit, no other symbol allowed                                                                      | The order id, Unique identifier for the request                       |
| **productType**     | string   | Y            | maximum length 16                                                                                             | product type                                                          |
| **productName**     | string   | Y            | maximum length 256                                                                                            | product name                                                          |
| **transactTime**    | long     | Y            | -                                                                                                             | transaction time                                                      |
| **tradeType**       | string   | Y            | &#34;WEB&#34;, &#34;APP&#34;, &#34;WAP&#34;, &#34;MINI_PROGRAM&#34;, &#34;PAYMENT_LINK&#34;, &#34;OTHERS&#34; | operate entrance                                                      |
| **totalFee**        | decimal  | Y            | -                                                                                                             | order amount                                                          |
| **currency**        | string   | Y            | -                                                                                                             | order currency                                                        |
| **transactionId**   | string   | N            | -                                                                                                             | debit transaction id                                                  |
| **openUserId**      | string   | N            | -                                                                                                             | payer unique id                                                       |
| **passThroughInfo** | string   | N            | -                                                                                                             | pass through info, from the create order api                          |
| **commission**      | decimal  | Y            | -                                                                                                             | Transaction fees charged. Please refer to your contract for more info |
| **paymentInfo**     | object   | N            | -                                                                                                             | payment information, [refer to](#paymentInfo-data)                    |

### PaymentInfo Data

<span id="paymentInfo-data"></span>

| **Attributes**          | **Type**                 | **Required** | **Limitation** | **Description**                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------ | ------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **payMethod**           | string                   | Y            | -              | pay method                                                                                                                                                                                                                                                                                         |
| **paymentInstructions** | list[PaymentInstruction] | Y            | -              | payment instruction list, [refer to](#paymentInstruction-data)                                                                                                                                                                                                                                     |
| **channel**             | string                   | N            | -              | channel                                                                                                                                                                                                                                                                                            |
| **subChannel**          | string                   | N            | -              | sub channel                                                                                                                                                                                                                                                                                        |
| **payerDetail**         | string                   | N            | -              | encrypted payer identity information for merchant compliance purposes without compromising privacy and security. Decryption instructions please [refer to](authentication#decryption-instructions-for-merchant-data-sharing). <br/> **This function is only available for whitelisted merchants.** |

### PaymentInstruction Data

<span id="paymentInstruction-data"></span>

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**  |
| -------------- | -------- | ------------ | -------------- | ---------------- |
| **currency**   | string   | Y            | -              | payment currency |
| **amount**     | decimal  | Y            | -              | currency amount  |
| **price**      | decimal  | Y            | -              | currency price   |

### Sample Payload

#### PAY SUCCESS

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"xr6wYe8ATWE6thS5Sc7ezMihMFGKn6\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"transactTime\":1619508939664,\"tradeType\":\"APP\",\"totalFee\":0.88000000,\"currency\":\"USDT\",\"transactionId\":\"M_R_282737362839373\",\"openUserId\":\"1211HS10K81f4273ac031\",\"commission\":0.0088,\"paymentInfo\":{\"payMethod\":\"funding\",\"paymentInstructions\":[{\"currency\":\"USDT\",\"amount\":0.88000000,\"price\":1}],\"channel\":\"DEFAULT\"}}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_SUCCESS"
}
```

#### PAY FAIL

PAY_FAIL order status is only applicable to Direct Debit order. Normal C2B orders will only receive
PAY_SUCCESS or PAY_CLOSE status.

```json
{
  "bizType": "PAY",
  "data": "{\"merchantTradeNo\":\"9825382937292\",\"totalFee\":0.88000000,\"transactTime\":1619508939664,\"currency\":\"USDT\",\"openUserId\":\"1211HS10K81f4273ac031\",\"productType\":\"Food\",\"productName\":\"Ice Cream\",\"tradeType\":\"WEB\"}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
  "bizStatus": "PAY_FAIL"
}
```

## Response Parameters

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message                                                                  |

### Sample Response

**After receiving a webhook with your endpoint, please respond with an HTTP 200 OK.**

```json
{ "returnCode": "SUCCESS", "returnMessage": null }
```