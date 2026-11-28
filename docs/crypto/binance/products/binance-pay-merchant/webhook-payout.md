---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-payout
api_type: Guide
updated_at: 2026-11-28 18:32:48.470451
---

# Batch Payout Notification

Binance Pay will send the status of Payout order event to partner/merchant webhook endpoint
configure on the Merchant Management Platform.

In situations where an event notification receives sending failure, the webhook will retry up to 6
times to resend the event. This is applicable to if the merchant/partner did not return HTTP 200
SUCCESS to the webhook as well.

## Webhook Endpoints

## Request Parameters

| **Attributes** | **Type**            | **Required** | **Limitation** | **Description**                  |
| -------------- | ------------------- | ------------ | -------------- | -------------------------------- |
| **bizType**    | string              | Y            | -              | **PAYOUT**                       |
| **bizId**      | long                | Y            | -              | Payout ID                        |
| **bizIdStr**   | string              | Y            | -              | biz id as string                 |
| **bizStatus**  | string              | Y            | -              | Same as Payout Query batchStatus |
| **data**       | TransferQueryResult | Y            | -              | JSON string                      |

## Child Attribute

### TransferQueryResult

<span id="payout-query-response"></span>

| **Attributes**  | **Type** | **Required** | **Limitation**        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------- | ------------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**   | string   | Y            | Maximum length 32     | The passed-in request ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **batchStatus** | string   | Y            | Enum string           | **ACCEPTED**: accepted the request, will process it soon. <br /> **PROCESSING**: batch under processing <br /> **SUCCESS**: All payout performed successfully, user have received fund in Binance funding wallet <br /> **PART_SUCCESS**: transfers partially succeeded.<br /> Reasons: <br />1.Insufficient funds: there’s insufficient fund in your account <br /> 2.Awaiting recipient: pending user to create Binance account and perform KYC <br/> 3.Partial refund: user failed to complete KYC in 72 hours, fund will be funded to merchant account <br/> **FAILED**: all transfers failed <br /> **CANCELED**: Transfer request canceled by Binance due to unknown system errors after retry limit, will not retry further |
| **merchantId**  | long     | Y            |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **currency**    | string   | Y            | Valid crypto currency | The request currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **totalAmount** | decimal  | Y            |                       | Total transfer amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **totalNumber** | int      | Y            | Maximum length 1000   | Total number of transfers in the batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Sample Payload

```json
{
  "bizType": "PAYOUT",
  "data": "{\"batchStatus\":\"SUCCESS\",\"currency\":\"USDT\",\"merchantId\":100000000003,\"requestId\":\"gg8127129\",\"totalAmount\":2.00000000,\"totalNumber\":2}",
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

# Batch Payout Notification

Binance Pay will send the status of Payout order event to partner/merchant webhook endpoint
configure on the Merchant Management Platform.

In situations where an event notification receives sending failure, the webhook will retry up to 6
times to resend the event. This is applicable to if the merchant/partner did not return HTTP 200
SUCCESS to the webhook as well.

## Webhook Endpoints

## Request Parameters

| **Attributes** | **Type**            | **Required** | **Limitation** | **Description**                  |
| -------------- | ------------------- | ------------ | -------------- | -------------------------------- |
| **bizType**    | string              | Y            | -              | **PAYOUT**                       |
| **bizId**      | long                | Y            | -              | Payout ID                        |
| **bizIdStr**   | string              | Y            | -              | biz id as string                 |
| **bizStatus**  | string              | Y            | -              | Same as Payout Query batchStatus |
| **data**       | TransferQueryResult | Y            | -              | JSON string                      |

## Child Attribute

### TransferQueryResult

<span id="payout-query-response"></span>

| **Attributes**  | **Type** | **Required** | **Limitation**        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------- | ------------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **requestId**   | string   | Y            | Maximum length 32     | The passed-in request ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **batchStatus** | string   | Y            | Enum string           | **ACCEPTED**: accepted the request, will process it soon. <br /> **PROCESSING**: batch under processing <br /> **SUCCESS**: All payout performed successfully, user have received fund in Binance funding wallet <br /> **PART_SUCCESS**: transfers partially succeeded.<br /> Reasons: <br />1.Insufficient funds: there’s insufficient fund in your account <br /> 2.Awaiting recipient: pending user to create Binance account and perform KYC <br/> 3.Partial refund: user failed to complete KYC in 72 hours, fund will be funded to merchant account <br/> **FAILED**: all transfers failed <br /> **CANCELED**: Transfer request canceled by Binance due to unknown system errors after retry limit, will not retry further |
| **merchantId**  | long     | Y            |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **currency**    | string   | Y            | Valid crypto currency | The request currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **totalAmount** | decimal  | Y            |                       | Total transfer amount in this batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **totalNumber** | int      | Y            | Maximum length 1000   | Total number of transfers in the batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Sample Payload

```json
{
  "bizType": "PAYOUT",
  "data": "{\"batchStatus\":\"SUCCESS\",\"currency\":\"USDT\",\"merchantId\":100000000003,\"requestId\":\"gg8127129\",\"totalAmount\":2.00000000,\"totalNumber\":2}",
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