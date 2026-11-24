---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-payout-non-binance
api_type: Guide
updated_at: 2026-11-24 18:33:39.700134
---

# Payout Non-binance user Notification

Binance Pay will send the final status of Payout order event to non-Binance email to
partner/merchant webhook endpoint configure on the Merchant Management Platform. The final event to
non-Binance email refers to

- Email created Binance account and perform KYC within 72 hours to receive fund
- Email holder did not create account nor complete KYC within 72 hours resulting in fund being
  refunded back to merchant/partner account

In situations where an event notification receives sending failure, the webhook will retry up to 6
times to resend the event. This is applicable to if the merchant/partner did not return HTTP 200
SUCCESS to the webhook as well.

## Webhook Endpoints

## Request Parameters

| **Attributes** | **Type**          | **Required** | **Limitation** | **Description**                          |
| -------------- | ----------------- | ------------ | -------------- | ---------------------------------------- |
| **bizType**    | string            | Y            | -              | **PAYOUT_NON_BN**                        |
| **bizId**      | long              | Y            | -              | Payout ID                                |
| **bizIdStr**   | string            | Y            | -              | biz id as string                         |
| **bizStatus**  | string            | Y            | -              | Same as Payout Query detail order status |
| **data**       | PayoutOrderDetail | Y            | -              | JSON string                              |

## Child Attribute

### PayoutOrderDetail

<span id="payout-order-detail"></span>

| **Attributes**     | **Type** | **Required** | **Limitation** | **Description**                                                                                                        |
| ------------------ | -------- | ------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **merchantSendId** | string   | Y            | -              | Unique identifier for the merchant sending the payout.                                                                 |
| **orderId**        | string   | Y            | -              | Unique identifier for the order associated with this payout.                                                           |
| **batchId**        | string   | Y            | -              | Batch identifier grouping multiple payouts.                                                                            |
| **status**         | string   | Y            | -              | Same as Payout Query detail order status                                                                               |
| **currency**       | string   | Y            | -              | The currency in which the payout is made.                                                                              |
| **amount**         | decimal  | Y            | -              | The total amount of the payout.                                                                                        |
| **receiveType**    | string   | Y            | Enum value     | Receiver's ID type only will be Email<br /> **EMAIL**: Binance user email address, support payout to non-binance users |
| **receiver**       | string   | Y            | -              | The email of this receiver                                                                                             |

### Sample Payload

```json
{
  "bizType": "PAYOUT",
  "data": "{\"merchantSendId\":\"XXXIDXXX\",\"orderId\":\"284838578405933060\",\"batchId\":\"284838578405933040\",\"status\":\"SUCCESS\",\"currency\":\"USDT\",\"amount\":\"1\",\"receiveType\":\"EMAIL\",\"receiver\":\"xxxxx@gmail.com\"}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
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
{ "returnCode": "SUCCESS", "returnMessage": null }
```

---

# Payout Non-binance user Notification

Binance Pay will send the final status of Payout order event to non-Binance email to
partner/merchant webhook endpoint configure on the Merchant Management Platform. The final event to
non-Binance email refers to

- Email created Binance account and perform KYC within 72 hours to receive fund
- Email holder did not create account nor complete KYC within 72 hours resulting in fund being
  refunded back to merchant/partner account

In situations where an event notification receives sending failure, the webhook will retry up to 6
times to resend the event. This is applicable to if the merchant/partner did not return HTTP 200
SUCCESS to the webhook as well.

## Webhook Endpoints

## Request Parameters

| **Attributes** | **Type**          | **Required** | **Limitation** | **Description**                          |
| -------------- | ----------------- | ------------ | -------------- | ---------------------------------------- |
| **bizType**    | string            | Y            | -              | **PAYOUT_NON_BN**                        |
| **bizId**      | long              | Y            | -              | Payout ID                                |
| **bizIdStr**   | string            | Y            | -              | biz id as string                         |
| **bizStatus**  | string            | Y            | -              | Same as Payout Query detail order status |
| **data**       | PayoutOrderDetail | Y            | -              | JSON string                              |

## Child Attribute

### PayoutOrderDetail

<span id="payout-order-detail"></span>

| **Attributes**     | **Type** | **Required** | **Limitation** | **Description**                                                                                                        |
| ------------------ | -------- | ------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **merchantSendId** | string   | Y            | -              | Unique identifier for the merchant sending the payout.                                                                 |
| **orderId**        | string   | Y            | -              | Unique identifier for the order associated with this payout.                                                           |
| **batchId**        | string   | Y            | -              | Batch identifier grouping multiple payouts.                                                                            |
| **status**         | string   | Y            | -              | Same as Payout Query detail order status                                                                               |
| **currency**       | string   | Y            | -              | The currency in which the payout is made.                                                                              |
| **amount**         | decimal  | Y            | -              | The total amount of the payout.                                                                                        |
| **receiveType**    | string   | Y            | Enum value     | Receiver's ID type only will be Email<br /> **EMAIL**: Binance user email address, support payout to non-binance users |
| **receiver**       | string   | Y            | -              | The email of this receiver                                                                                             |

### Sample Payload

```json
{
  "bizType": "PAYOUT",
  "data": "{\"merchantSendId\":\"XXXIDXXX\",\"orderId\":\"284838578405933060\",\"batchId\":\"284838578405933040\",\"status\":\"SUCCESS\",\"currency\":\"USDT\",\"amount\":\"1\",\"receiveType\":\"EMAIL\",\"receiver\":\"xxxxx@gmail.com\"}",
  "bizIdStr": "29383937493038367292",
  "bizId": 29383937493038367292,
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
{ "returnCode": "SUCCESS", "returnMessage": null }
```