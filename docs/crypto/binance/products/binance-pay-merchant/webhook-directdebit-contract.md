---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-directdebit-contract
api_type: Guide
updated_at: 2026-11-27 18:33:50.502027
---

# Direct Debit/Pre Authorization Notification

## Webhook Endpoints

Binance Pay will send direct debit/pre authorization contract events to partner for notification.
You will be able to configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

\*This is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

In situation where event was signed to terminated, the webhook will retry up to 6 times to resend
the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                                                    |
| -------------- | -------- | ------------ | -------------- | ---------------------------------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;DIRECT_DEBIT_CT&#34;                                                          |
| **bizId**      | long     | Y            | -              | contract id                                                                        |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                                                   |
| **bizStatus**  | string   | Y            | -              | &#34;CONTRACT_SIGNED&#34;,&#34;CONTRACT_TERMINATED&#34;,&#34;CONTRACT_EXPIRED&#34; |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data)                           |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**              | **Type** | **Required** | **Limitation**                                              | **Description**                                                                          |
| --------------------------- | -------- | ------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **merchantContractCode**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The unique ID assigned by the merchant to identify a direct debit contract request.      |
| **contractId**              | Long     | Y            | maximum length 19                                           | contract id                                                                              |
| **serviceName**             | string   | Y            | maximum length 32                                           | service name                                                                             |
| **openUserId**              | string   | N            | -                                                           | payer unique id                                                                          |
| **merchantAccountNo**       | string   | N            | maximum length 64                                           | the userID/user account in merchant side e.g. xxx@gmail.com                              |
| **singleUpperLimit**        | decimal  | Y            | Max Unit Range: 8 decimal places                            | upper limit                                                                              |
| **currency**                | string   | Y            | -                                                           | currency                                                                                 |
| **contractTerminationWay**  | int      | N            | -                                                           | 0-by user, 1-auto expire, 2-by operation team. only &#34;CONTRACT_TERMINATED&#34; status |
| **contractTerminationTime** | Long     | N            | -                                                           | only &#34;CONTRACT_TERMINATED&#34; status                                                |

### Sample Payload

#### CONTRACT SIGNED

```json
{
  "bizType": "DIRECT_DEBIT_CT",
  "data": "{\"merchantContractCode\":\"a9d1deffaecba9f592aa682b5c997042\",\"contractId\":205638372306477056,\"serviceName\":\"Tra Direct Debit\",\"openUserId\":\"04fdfaf5c88d746168e3cc0a582b65d4\",\"merchantAccountNo\":\"sss@gmail.com\",\"currency\":\"USDT\",\"singleUpperLimit\":50.00000000}",
  "bizIdStr": "205638372306477056",
  "bizId": 205638372306477056,
  "bizStatus": "CONTRACT_SIGNED"
}
```

#### CONTRACT TERMINATED

```json
{
  "bizType": "DIRECT_DEBIT_CT",
  "data": "{\"merchantContractCode\":\"a9d1deffaecba9f592aa682b5c997042\",\"contractId\":205638372306477056,\"serviceName\":\"Tra Direct Debit\",\"openUserId\":\"04fdfaf5c88d746168e3cc0a582b65d4\",\"merchantAccountNo\":\"sss@gmail.com\",\"currency\":\"USDT\",\"singleUpperLimit\":50.00000000,\"contractTerminationWay\":0,\"contractTerminationTime\":1673594769902}",
  "bizIdStr": "205638372306477056",
  "bizId": 205638372306477056,
  "bizStatus": "CONTRACT_TERMINATED"
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

# Direct Debit/Pre Authorization Notification

## Webhook Endpoints

Binance Pay will send direct debit/pre authorization contract events to partner for notification.
You will be able to configure webhook endpoints via the
[Binance Merchant Admin Portal](https://merchant.binance.com/en/dashboard).

\*This is only available for whitelisted merchants. If you need any help, you can contact us:
merchant@binance.com

In situation where event was signed to terminated, the webhook will retry up to 6 times to resend
the event.

## Request Parameters

| **Attributes** | **Type** | **Required** | **Limitation** | **Description**                                                                    |
| -------------- | -------- | ------------ | -------------- | ---------------------------------------------------------------------------------- |
| **bizType**    | string   | Y            | -              | &#34;DIRECT_DEBIT_CT&#34;                                                          |
| **bizId**      | long     | Y            | -              | contract id                                                                        |
| **bizIdStr**   | string   | Y            | -              | biz id as string                                                                   |
| **bizStatus**  | string   | Y            | -              | &#34;CONTRACT_SIGNED&#34;,&#34;CONTRACT_TERMINATED&#34;,&#34;CONTRACT_EXPIRED&#34; |
| **data**       | string   | Y            | -              | JSON string, data details [refer to](#notification-data)                           |

## Child Attribute

### Notification Data

<span id="notification-data"></span>

| **Attributes**              | **Type** | **Required** | **Limitation**                                              | **Description**                                                                          |
| --------------------------- | -------- | ------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **merchantContractCode**    | string   | Y            | letter or digit, no other symbol allowed, maximum length 32 | The unique ID assigned by the merchant to identify a direct debit contract request.      |
| **contractId**              | Long     | Y            | maximum length 19                                           | contract id                                                                              |
| **serviceName**             | string   | Y            | maximum length 32                                           | service name                                                                             |
| **openUserId**              | string   | N            | -                                                           | payer unique id                                                                          |
| **merchantAccountNo**       | string   | N            | maximum length 64                                           | the userID/user account in merchant side e.g. xxx@gmail.com                              |
| **singleUpperLimit**        | decimal  | Y            | Max Unit Range: 8 decimal places                            | upper limit                                                                              |
| **currency**                | string   | Y            | -                                                           | currency                                                                                 |
| **contractTerminationWay**  | int      | N            | -                                                           | 0-by user, 1-auto expire, 2-by operation team. only &#34;CONTRACT_TERMINATED&#34; status |
| **contractTerminationTime** | Long     | N            | -                                                           | only &#34;CONTRACT_TERMINATED&#34; status                                                |

### Sample Payload

#### CONTRACT SIGNED

```json
{
  "bizType": "DIRECT_DEBIT_CT",
  "data": "{\"merchantContractCode\":\"a9d1deffaecba9f592aa682b5c997042\",\"contractId\":205638372306477056,\"serviceName\":\"Tra Direct Debit\",\"openUserId\":\"04fdfaf5c88d746168e3cc0a582b65d4\",\"merchantAccountNo\":\"sss@gmail.com\",\"currency\":\"USDT\",\"singleUpperLimit\":50.00000000}",
  "bizIdStr": "205638372306477056",
  "bizId": 205638372306477056,
  "bizStatus": "CONTRACT_SIGNED"
}
```

#### CONTRACT TERMINATED

```json
{
  "bizType": "DIRECT_DEBIT_CT",
  "data": "{\"merchantContractCode\":\"a9d1deffaecba9f592aa682b5c997042\",\"contractId\":205638372306477056,\"serviceName\":\"Tra Direct Debit\",\"openUserId\":\"04fdfaf5c88d746168e3cc0a582b65d4\",\"merchantAccountNo\":\"sss@gmail.com\",\"currency\":\"USDT\",\"singleUpperLimit\":50.00000000,\"contractTerminationWay\":0,\"contractTerminationTime\":1673594769902}",
  "bizIdStr": "205638372306477056",
  "bizId": 205638372306477056,
  "bizStatus": "CONTRACT_TERMINATED"
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