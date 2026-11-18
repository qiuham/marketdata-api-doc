---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/collection-notification
api_type: Guide
updated_at: 2026-11-18 18:32:39.774573
---

# Collection Notification

Once the collection has been paid, Binance Pay will send notification through the endpoint url
provided when creating collection.

# Request Parameters

| Attributes    | Type   | Required | Description |
| ------------- | ------ | -------- | ----------- |
| orderId       | Long   | YES      |
| clientTradeNo | String | YES      |
| status        | String | YES      | "PAID"      |

## Response Parameters

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message                                                                  |

### Sample Response

```json
{ "returnCode": "SUCCESS", "returnMessage": null }
```

---

# Collection Notification

Once the collection has been paid, Binance Pay will send notification through the endpoint url
provided when creating collection.

# Request Parameters

| Attributes    | Type   | Required | Description |
| ------------- | ------ | -------- | ----------- |
| orderId       | Long   | YES      |
| clientTradeNo | String | YES      |
| status        | String | YES      | "PAID"      |

## Response Parameters

| **Attributes**    | **Type** | **Required** | **Limitation**                      | **Description**                                                                 |
| ----------------- | -------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| **returnCode**    | string   | Y            | &#34;SUCCESS&#34; or &#34;FAIL&#34; | result code of notification processing, if process fail, Binance Pay will retry |
| **returnMessage** | string   | N            | -                                   | return message                                                                  |

### Sample Response

```json
{ "returnCode": "SUCCESS", "returnMessage": null }
```