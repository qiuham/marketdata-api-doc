---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-shareinfo-account-id
api_type: Guide
updated_at: 2026-11-18 02:06:50.890856
---

# Share Account Id Notification

## Webhook Endpoints

Binance Pay will send "Share Account ID" events to partners for notification. You will be able to
configure webhook endpoints via the Binance Merchant Portal. You will be able to configure webhook
endpoints via the [Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

In situation where event is user agrees to share account id, the webhook will retry up to 6 times to
resend the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                          |
| -------------- | -------- | ------------ | -------------- | -------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;SHARE_ACCOUNT_ID&#34;                               |
| **bizId**      | long     | Y            | -              | id                                                       |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                         |
| **bizStatus**  | string   | Y            | -              | &#34;SUCCESS&#34;                                        |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data) |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**    | **Type** | **Required** | **Limitation**                                              | **Description**                                                                |
| ----------------- | -------- | ------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **requestId**     | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The unique ID assigned by the merchant to identify a share account id request. |
| **userBinanceId** | string   | Y            | maximum length 19                                           | user binance id                                                                |
| **userName**      | string   | N            | -                                                           | user nickname, nullable                                                        |

### Sample Payload

#### userName is not null

```json
{
  "bizType": "SHARE_ACCOUNT_ID",
  "data": "{\"requestId\":\"9109c2bd482ef6bccc819c45af104a78\",\"userBinanceId\":\"100103397765\",\"userName\":\"xxx\"}",
  "bizIdStr": "219014596974616576",
  "bizId": 219014596974616576,
  "bizStatus": "SUCCESS"
}
```

#### userName is null

```json
{
  "bizType": "SHARE_ACCOUNT_ID",
  "data": "{\"requestId\":\"9109c2bd482ef6bccc819c45af104a78\",\"userBinanceId\":\"1000011371416\"}",
  "bizIdStr": "219014596974616576",
  "bizId": 219014596974616576,
  "bizStatus": "SUCCESS"
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
{
  "returnCode": "SUCCESS",
  "returnMessage": null
}
```

---

# Share Account Id Notification

## Webhook Endpoints

Binance Pay will send "Share Account ID" events to partners for notification. You will be able to
configure webhook endpoints via the Binance Merchant Portal. You will be able to configure webhook
endpoints via the [Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

In situation where event is user agrees to share account id, the webhook will retry up to 6 times to
resend the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                          |
| -------------- | -------- | ------------ | -------------- | -------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;SHARE_ACCOUNT_ID&#34;                               |
| **bizId**      | long     | Y            | -              | id                                                       |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                         |
| **bizStatus**  | string   | Y            | -              | &#34;SUCCESS&#34;                                        |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data) |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**    | **Type** | **Required** | **Limitation**                                              | **Description**                                                                |
| ----------------- | -------- | ------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **requestId**     | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The unique ID assigned by the merchant to identify a share account id request. |
| **userBinanceId** | string   | Y            | maximum length 19                                           | user binance id                                                                |
| **userName**      | string   | N            | -                                                           | user nickname, nullable                                                        |

### Sample Payload

#### userName is not null

```json
{
  "bizType": "SHARE_ACCOUNT_ID",
  "data": "{\"requestId\":\"9109c2bd482ef6bccc819c45af104a78\",\"userBinanceId\":\"100103397765\",\"userName\":\"xxx\"}",
  "bizIdStr": "219014596974616576",
  "bizId": 219014596974616576,
  "bizStatus": "SUCCESS"
}
```

#### userName is null

```json
{
  "bizType": "SHARE_ACCOUNT_ID",
  "data": "{\"requestId\":\"9109c2bd482ef6bccc819c45af104a78\",\"userBinanceId\":\"1000011371416\"}",
  "bizIdStr": "219014596974616576",
  "bizId": 219014596974616576,
  "bizStatus": "SUCCESS"
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
{
  "returnCode": "SUCCESS",
  "returnMessage": null
}
```