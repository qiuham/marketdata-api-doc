---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/webhook-balance-report
api_type: Guide
updated_at: 2026-11-23 18:33:51.983994
---

# Binance Pay: Balance Report Notification

## Webhook Endpoints

Binance Pay will send balance report events with final status only when partner use balance report
open api for report generation. For submitting download request,
[refer here](api-download-balance-report.md).

## Request Parameters

| **Attributes** | **Type**          | **Required** | **Limitation** | **Description**     |
| -------------- | ----------------- | ------------ | -------------- | ------------------- |
| **bizType**    | string            | Y            | -              | **BALANCE**         |
| **bizId**      | long              | Y            | -              | Download ID         |
| **bizIdStr**   | string            | Y            | -              | biz id as string    |
| **bizStatus**  | string            | Y            | -              | **BALANCE_SUCCESS** |
| **data**       | BalanceReportData | Y            | -              | JSON string         |

## Child Attribute

### BalanceReportData

<span id="balance-report-data"></span>

| **Attributes**          | **Type** | **Required** | **Limitation** | **Description**                                  |
| ----------------------- | -------- | ------------ | -------------- | ------------------------------------------------ |
| **downloadType**        | string   | Y            |                | merchant_balance_download_task                   |
| **downloadId**          | long     | Y            |                | Download ID, for any issue use this ID to query. |
| **userId**              | long     | Y            |                | Spot user ID                                     |
| **status**              | string   | Y            |                | 2 = success                                      |
| **downloadLink**        | string   | Y            |                | Download URL.                                    |
| **expirationTimestamp** | long     | Y            |                | Expiration timestamp of download link.           |
| **createTime**          | string   | Y            |                | Created time of the download document.           |

### Sample Payload

```json
{
  "bizType": "BALANCE",
  "data": "{\"downloadType\":\"merchant_balance_download_task\",\"downloadId\":197620356272996352,\"userId\":100102465376,\"status\":2,\"downloadLink\":\"https://sampleurl.com/file1\",\"expirationTimestamp\":1669947455000,\"createTime\":\"2022-12-01 02:15:50\",\"callbackUrl\":\"https://callbackurl.com\"}",
  "bizIdStr": "197620356272996352",
  "bizId": 197620356272996352,
  "bizStatus": "BALANCE_SUCCESS"
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

# Binance Pay: Balance Report Notification

## Webhook Endpoints

Binance Pay will send balance report events with final status only when partner use balance report
open api for report generation. For submitting download request,
[refer here](api-download-balance-report.md).

## Request Parameters

| **Attributes** | **Type**          | **Required** | **Limitation** | **Description**     |
| -------------- | ----------------- | ------------ | -------------- | ------------------- |
| **bizType**    | string            | Y            | -              | **BALANCE**         |
| **bizId**      | long              | Y            | -              | Download ID         |
| **bizIdStr**   | string            | Y            | -              | biz id as string    |
| **bizStatus**  | string            | Y            | -              | **BALANCE_SUCCESS** |
| **data**       | BalanceReportData | Y            | -              | JSON string         |

## Child Attribute

### BalanceReportData

<span id="balance-report-data"></span>

| **Attributes**          | **Type** | **Required** | **Limitation** | **Description**                                  |
| ----------------------- | -------- | ------------ | -------------- | ------------------------------------------------ |
| **downloadType**        | string   | Y            |                | merchant_balance_download_task                   |
| **downloadId**          | long     | Y            |                | Download ID, for any issue use this ID to query. |
| **userId**              | long     | Y            |                | Spot user ID                                     |
| **status**              | string   | Y            |                | 2 = success                                      |
| **downloadLink**        | string   | Y            |                | Download URL.                                    |
| **expirationTimestamp** | long     | Y            |                | Expiration timestamp of download link.           |
| **createTime**          | string   | Y            |                | Created time of the download document.           |

### Sample Payload

```json
{
  "bizType": "BALANCE",
  "data": "{\"downloadType\":\"merchant_balance_download_task\",\"downloadId\":197620356272996352,\"userId\":100102465376,\"status\":2,\"downloadLink\":\"https://sampleurl.com/file1\",\"expirationTimestamp\":1669947455000,\"createTime\":\"2022-12-01 02:15:50\",\"callbackUrl\":\"https://callbackurl.com\"}",
  "bizIdStr": "197620356272996352",
  "bizId": 197620356272996352,
  "bizStatus": "BALANCE_SUCCESS"
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