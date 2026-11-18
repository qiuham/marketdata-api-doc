---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-tech-service-provider
api_type: Guide
updated_at: 2026-11-18 18:32:15.134376
---

# Tech Service Provider Notification

## Webhook Endpoints

Binance Pay will send tech service provider events to partner for notification. You will be able to
configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

\*This is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

In situation where event was auth agree/reject/changed/disabled, the webhook will retry up to 6
times to resend the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                                                                               |
| -------------- | -------- | ------------ | -------------- | ------------------------------------------------------------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;TECH_PROVIDER&#34;                                                                                       |
| **bizId**      | long     | Y            | -              | tech provider id                                                                                              |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                                                                              |
| **bizStatus**  | string   | Y            | -              | &#34;SUBMIT_AUTH_AGREE&#34;,&#34;SUBMIT_AUTH_REJECT&#34;,&#34;TP_AUTH_CHANGED&#34;,&#34;TP_AUTH_DISABLED&#34; |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data)                                                      |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**         | **Type**     | **Required** | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | ------------ | ------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **authorizationId**    | string       | Y            | -                  | authorization Id                                                                                                                                                                                                                                                                                                                                                           |
| **authorizationToken** | string       | Y            | -                  | authorization token                                                                                                                                                                                                                                                                                                                                                        |
| **merchantId**         | long         | Y            | -                  | merchant id                                                                                                                                                                                                                                                                                                                                                                |
| **merchantName**       | string       | Y            | maximum length 128 | merchant name                                                                                                                                                                                                                                                                                                                                                              |
| **scopes**             | list[string] | N            | Enum string list   | **CONVERT**: all convert APIs. <br /> **REFUND**: [refund order api](api-order-refund). <br /> **CHECKOUT**: all order related APIs except refund order api. <br /> **PAYOUT**: all payout related APIs. <br /> **REPORT**: all reporting related APIs. <br /> **INTERNAL_TRANSFER**: all transfer fund related APIs. <br /> **BALANCE**: all wallet balance related APIs. |

### Sample Payload

#### AUTH AGREE

```json
{
  "bizType": "TECH_PROVIDER",
  "data": "{\"authorizationId\":\"210462863998500864\",\"authorizationToken\":\"4f92a76767a948d8b5ab60abd8ca2e15\",\"merchantId\":1000135331248,\"merchantName\":\"Test\",\"scopes\":[\"CONVERT\"]}",
  "bizIdStr": "210462863998500864",
  "bizId": 210462863998500864,
  "bizStatus": "SUBMIT_AUTH_AGREE"
}
```

#### AUTH REJECT

```json
{
  "bizType": "TECH_PROVIDER",
  "data": "{\"authorizationId\":\"210459190727720960\",\"authorizationToken\":\"ac97fa06614247f0a0d45d50c2cd5937\",\"merchantId\":1000135331248,\"merchantName\":\"Test\",\"scopes\":[\"BALANCE\"]}",
  "bizIdStr": "210459190727720960",
  "bizId": 210459190727720960,
  "bizStatus": "SUBMIT_AUTH_REJECT"
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

# Tech Service Provider Notification

## Webhook Endpoints

Binance Pay will send tech service provider events to partner for notification. You will be able to
configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

\*This is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

In situation where event was auth agree/reject/changed/disabled, the webhook will retry up to 6
times to resend the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                                                                               |
| -------------- | -------- | ------------ | -------------- | ------------------------------------------------------------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;TECH_PROVIDER&#34;                                                                                       |
| **bizId**      | long     | Y            | -              | tech provider id                                                                                              |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                                                                              |
| **bizStatus**  | string   | Y            | -              | &#34;SUBMIT_AUTH_AGREE&#34;,&#34;SUBMIT_AUTH_REJECT&#34;,&#34;TP_AUTH_CHANGED&#34;,&#34;TP_AUTH_DISABLED&#34; |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data)                                                      |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**         | **Type**     | **Required** | **Limitation**     | **Description**                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | ------------ | ------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **authorizationId**    | string       | Y            | -                  | authorization Id                                                                                                                                                                                                                                                                                                                                                           |
| **authorizationToken** | string       | Y            | -                  | authorization token                                                                                                                                                                                                                                                                                                                                                        |
| **merchantId**         | long         | Y            | -                  | merchant id                                                                                                                                                                                                                                                                                                                                                                |
| **merchantName**       | string       | Y            | maximum length 128 | merchant name                                                                                                                                                                                                                                                                                                                                                              |
| **scopes**             | list[string] | N            | Enum string list   | **CONVERT**: all convert APIs. <br /> **REFUND**: [refund order api](api-order-refund). <br /> **CHECKOUT**: all order related APIs except refund order api. <br /> **PAYOUT**: all payout related APIs. <br /> **REPORT**: all reporting related APIs. <br /> **INTERNAL_TRANSFER**: all transfer fund related APIs. <br /> **BALANCE**: all wallet balance related APIs. |

### Sample Payload

#### AUTH AGREE

```json
{
  "bizType": "TECH_PROVIDER",
  "data": "{\"authorizationId\":\"210462863998500864\",\"authorizationToken\":\"4f92a76767a948d8b5ab60abd8ca2e15\",\"merchantId\":1000135331248,\"merchantName\":\"Test\",\"scopes\":[\"CONVERT\"]}",
  "bizIdStr": "210462863998500864",
  "bizId": 210462863998500864,
  "bizStatus": "SUBMIT_AUTH_AGREE"
}
```

#### AUTH REJECT

```json
{
  "bizType": "TECH_PROVIDER",
  "data": "{\"authorizationId\":\"210459190727720960\",\"authorizationToken\":\"ac97fa06614247f0a0d45d50c2cd5937\",\"merchantId\":1000135331248,\"merchantName\":\"Test\",\"scopes\":[\"BALANCE\"]}",
  "bizIdStr": "210459190727720960",
  "bizId": 210459190727720960,
  "bizStatus": "SUBMIT_AUTH_REJECT"
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