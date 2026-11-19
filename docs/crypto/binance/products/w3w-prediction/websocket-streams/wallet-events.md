---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/w3w-prediction/websocket-streams/wallet-events
api_type: WebSocket
updated_at: 2026-11-19 18:37:35.059212
---

# Wallet Events WebSocket Streams

## 1. Overview

### 1.1 Business Description

Binance Web3 Prediction pushes 14 types of business events to **individual users** in real time via
the **Binance SApi WebSocket channel**, covering 4 major categories: trading (market / limit),
reward claim, fund transfer, and market resolution.

### 1.2 Channel Characteristics

| Item               | Description                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Protocol           | WebSocket (WSS)                                                                            |
| Gateway            | Binance SApi WSS (shares the same connection infrastructure with Spot / USD-M SApi)        |
| Routing            | Exact `(topic, userId)` match — only the matching user receives the push                   |
| Delivery semantics | **at-most-once** (no retransmission guarantee)                                             |
| Ordering           | **No strict ordering** is guaranteed for the same user/topic; use `pushId` for idempotency |
| Offline messages   | **Not cached** — please pull the latest state via REST API after reconnect                 |
| Latency            | Delivered within < 500 ms after the business event triggers (excluding network)            |
| Per-message size   | < 2 KB                                                                                     |

### 1.3 Target Audience

- Wallet clients integrating Prediction business
- Third-party agent trading parties
- Data analytics / risk-control systems

---

## 2. WebSocket Connection

> The basic connection specification fully follows
> [Binance CMS General Info](https://developers.binance.com/docs/cms/general-info). This section
> excerpts the key points and adds Prediction-specific examples.

### 2.1 Connection URL

**Base URL**:

```
wss://api.binance.com/sapi/wss
```

**Full connection URL format**:

```
wss://api.binance.com/sapi/wss?random={random}&topic={topic}&recvWindow={recvWindow}&timestamp={timestamp}&signature={signature}
```

**Example (subscribing to the prediction buy success topic)**:

```
wss://api.binance.com/sapi/wss?random=56724ac693184379ae23ffe5e910063c&topic=web3_prediction_pm_market_buy_success&recvWindow=30000&timestamp=1753244327210&signature=341098eff29e3ef395ed4ea85035bd7fe9e9356d2b0d4f1f97655c74516a2d65
```

### 2.2 URL Parameters

| Param        | Required | Description                                                                   |
| ------------ | -------- | ----------------------------------------------------------------------------- |
| `random`     | ✅       | Random string or number, ≤ 32 chars recommended; ensures signature uniqueness |
| `topic`      | ✅       | Topics to subscribe; multiple topics joined by `&#124;`                       |
| `recvWindow` | ✅       | Time window (ms), max 60000                                                   |
| `timestamp`  | ✅       | Millisecond UTC timestamp at request time                                     |
| `signature`  | ✅       | HMAC SHA256 signature (see below)                                             |

### 2.3 Authentication

#### Header

```
X-MBX-APIKEY: <your_api_key>
```

#### Signature Steps

1. Collect all URL parameters (**excluding `signature` itself**)
2. Sort parameters by name in **alphabetical order** and join into a query string
3. Apply **HMAC SHA256** with the Secret Key on this string

**Payload example**:

```
random=56724ac693184379ae23ffe5e910063c&recvWindow=30000&timestamp=1753244327210&topic=web3_prediction_pm_market_buy_success
```

**Bash verification**:

```bash
echo -n "random=56724ac693184379ae23ffe5e910063c&recvWindow=30000&timestamp=1753244327210&topic=web3_prediction_pm_market_buy_success" \
  | openssl dgst -sha256 -hmac "<YOUR_SECRET_KEY>"
```

### 2.4 Time Window

The server validates: `server_time <= timestamp + recvWindow`. Requests outside this window are
rejected. Clients are advised to periodically sync local time with Binance Server Time.

### 2.5 Connection Lifecycle

| Item                           | Rule                                                          |
| ------------------------------ | ------------------------------------------------------------- |
| Max single connection lifetime | **24 hours**                                                  |
| After timeout                  | Client must reconnect, **regenerating timestamp + signature** |
| Server heartbeat timeout       | Disconnects if no PING received for 1 minute                  |

### 2.6 Subscribe / Unsubscribe / Heartbeat / Rate Limits

> Fully follows
> [Binance CMS General Specification](https://developers.binance.com/docs/cms/general-info). Not
> duplicated here.

Quick reference:

- Subscribe at connect time via URL parameter `topic=topic1|topic2`
- After connection, dynamically subscribe / unsubscribe via JSON command
  `{"command":"SUBSCRIBE","value":"..."}`
- Client must send a PING (empty payload) every 30 seconds
- Per-connection rate limit: 5 messages/second; exceeding causes disconnection, repeated violations
  cause **IP ban**

For detailed fields, response structures, error codes, and reconnection guidance, refer to the CMS
document.

---

## 3. Common Push Message Structure

### 3.1 Envelope

Each business push is delivered by the SApi gateway following the SApi push specification. **The
business payload is a JSON string inside the `data` field**:

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_buy_success",
  "data": "{\"pushId\":\"pm_PM2026052812345_pm_market_buy_success_a1b2c3d4\",\"amount\":\"12.34\",\"topic\":\"BTC will hi..\"}"
}
```

> Note: the `data` field is a **stringified JSON** — requires a second `JSON.parse`.

### 3.2 Common Business Payload Fields

```json
{
  "pushId": "pm_<refId>_<scenarioCode>_<8hex>",
  "<businessField1>": "...",
  "<businessField2>": "..."
}
```

| Field                 | Type   | Required  | Description                                |
| --------------------- | ------ | --------- | ------------------------------------------ |
| `pushId`              | string | ✅        | Unique push ID, **present in every topic** |
| Other business fields | string | per-topic | See Section 4; all values are stringified  |

### 3.3 `pushId` Format

```
pm_<refId>_<scenarioCode>_<8hex>

Example: pm_PM2026052812345_pm_market_buy_success_a1b2c3d4
```

| Segment          | Description                                                                           |
| ---------------- | ------------------------------------------------------------------------------------- |
| `pm_`            | Fixed prefix                                                                          |
| `<refId>`        | Business reference ID (orderId / claimBatchId / transferId / marketId, see Section 4) |
| `<scenarioCode>` | Scenario code, identical to the topic suffix                                          |
| `<8hex>`         | 8 random hex chars to ensure uniqueness                                               |

---

## 4. Topic List & Detailed Payloads

> All 14 topics are prefixed with `web3_prediction_`. Subscribe as needed.

### 4.0 Topic Summary

| #   | scenarioCode                  | Topic                                         | Trigger                            |
| --- | ----------------------------- | --------------------------------------------- | ---------------------------------- |
| 1   | `pm_market_buy_success`       | `web3_prediction_pm_market_buy_success`       | Market buy order fully filled      |
| 2   | `pm_market_buy_fail`          | `web3_prediction_pm_market_buy_fail`          | Market buy order failed / expired  |
| 3   | `pm_market_sell_success`      | `web3_prediction_pm_market_sell_success`      | Market sell order fully filled     |
| 4   | `pm_market_sell_fail`         | `web3_prediction_pm_market_sell_fail`         | Market sell order failed / expired |
| 5   | `pm_limit_submit_success`     | `web3_prediction_pm_limit_submit_success`     | Limit order submitted successfully |
| 6   | `pm_limit_submit_fail`        | `web3_prediction_pm_limit_submit_fail`        | Limit order submission failed      |
| 7   | `pm_limit_order_filled`       | `web3_prediction_pm_limit_order_filled`       | Limit order fully filled           |
| 8   | `pm_limit_order_partial_fill` | `web3_prediction_pm_limit_order_partial_fill` | Limit order partially filled       |
| 9   | `pm_claim_success`            | `web3_prediction_pm_claim_success`            | Reward claim succeeded             |
| 10  | `pm_claim_fail`               | `web3_prediction_pm_claim_fail`               | Reward claim failed                |
| 11  | `pm_claim_partial_success`    | `web3_prediction_pm_claim_partial_success`    | Batch claim partially succeeded    |
| 12  | `pm_transfer_success`         | `web3_prediction_pm_transfer_success`         | Fund transfer succeeded            |
| 13  | `pm_transfer_fail`            | `web3_prediction_pm_transfer_fail`            | Fund transfer failed               |
| 14  | `pm_market_close`             | `web3_prediction_pm_market_close`             | Market resolution notification     |

---

### 4.1 `web3_prediction_pm_market_buy_success`

#### Trigger

User's **market buy order** is fully filled (`OrderStatus = FILLED`).

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_success_a1b2c3d4",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                                    | Description                                        |
| -------- | ------ | -------- | ----------------------------------------- | -------------------------------------------------- |
| `pushId` | string | ✅       | System-generated                          | Unique ID                                          |
| `amount` | string | ✅       | `OrderHistory.amountIn`                   | USDT amount the user paid, truncated to 2 decimals |
| `topic`  | string | ✅       | `MarketTopic.title` truncated to 12 chars | Market title                                       |

#### Copy Template

> Bought ${amount} USDT in ${topic}

---

### 4.2 `web3_prediction_pm_market_buy_fail`

#### Trigger

Market buy order transitions to `FAILED` or `EXPIRED`.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                  | Description                                            |
| -------- | ------ | -------- | ----------------------- | ------------------------------------------------------ |
| `pushId` | string | ✅       | System-generated        |                                                        |
| `amount` | string | ✅       | `OrderHistory.amountIn` | Original order USDT amount (**not actually deducted**) |
| `topic`  | string | ✅       | Truncated market title  |                                                        |

---

### 4.3 `web3_prediction_pm_market_sell_success`

#### Trigger

User's **market sell order** is fully filled (`FILLED`).

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_success_c3d4e5f6",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

| Field    | Type   | Required | Source                 | Description                                |
| -------- | ------ | -------- | ---------------------- | ------------------------------------------ |
| `pushId` | string | ✅       | System-generated       |                                            |
| `amount` | string | ✅       | `amountOut − totalFee` | USDT actually received (**fees deducted**) |
| `topic`  | string | ✅       | Truncated market title |                                            |

---

### 4.4 `web3_prediction_pm_market_sell_fail`

#### Trigger

Market sell order transitions to `FAILED` or `EXPIRED`.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

| Field    | Type   | Required | Source                 | Description                                                  |
| -------- | ------ | -------- | ---------------------- | ------------------------------------------------------------ |
| `pushId` | string | ✅       | System-generated       |                                                              |
| `amount` | string | ✅       | `amountOut − totalFee` | Expected receivable amount before failure (**not credited**) |
| `topic`  | string | ✅       | Truncated market title |                                                              |

---

### 4.5 `web3_prediction_pm_limit_submit_success`

#### Trigger

User's **limit order** is successfully placed on the order book.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                              | Description              |
| -------- | ------ | -------- | ----------------------------------- | ------------------------ |
| `pushId` | string | ✅       | System-generated                    |                          |
| `amount` | string | ✅       | BUY: `amountIn` / SELL: `amountOut` | Total limit order amount |
| `topic`  | string | ✅       | Truncated market title              |                          |

---

### 4.6 `web3_prediction_pm_limit_submit_fail`

#### Trigger

Limit order submission rejected at submission time.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                 | Description |
| -------- | ------ | -------- | ---------------------- | ----------- |
| `pushId` | string | ✅       | System-generated       |             |
| `topic`  | string | ✅       | Truncated market title |             |

> ⚠️ **Note**: this scenario does **not** carry the `amount` field.

#### Copy Template

> Failed to submit your limit order for ${topic}. Please try again.

---

### 4.7 `web3_prediction_pm_limit_order_filled`

#### Trigger

A previously placed limit order is **fully filled**.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                                         | Description                  |
| -------- | ------ | -------- | ---------------------------------------------- | ---------------------------- |
| `pushId` | string | ✅       | System-generated                               |                              |
| `amount` | string | ✅       | BUY: `amountIn` / SELL: `amountOut − totalFee` | USDT amount of the full fill |
| `topic`  | string | ✅       | Truncated market title                         |                              |

---

### 4.8 `web3_prediction_pm_limit_order_partial_fill`

#### Trigger

Limit order **partially filled** (`PARTIALLY_FILLED`). Each new partial fill triggers a push.

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1",
  "amount": "30.00",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                                         | Description                                                             |
| -------- | ------ | -------- | ---------------------------------------------- | ----------------------------------------------------------------------- |
| `pushId` | string | ✅       | System-generated                               |                                                                         |
| `amount` | string | ✅       | BUY: `amountIn` / SELL: `amountOut − totalFee` | **Cumulative** filled amount after this partial fill, NOT the increment |
| `topic`  | string | ✅       | Truncated market title                         |                                                                         |

> ⚠️ A single limit order may trigger multiple pushes; clients **must use `pushId` for
> deduplication**.

---

### 4.9 `web3_prediction_pm_claim_success`

#### Trigger

A claim **fully succeeds** (single success or batch all succeed).

#### refId

`<refId>` = `batchId` (claim batch ID)

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2",
  "amount": "50.00"
}
```

| Field    | Type   | Required | Source                    | Description        |
| -------- | ------ | -------- | ------------------------- | ------------------ |
| `pushId` | string | ✅       | System-generated          |                    |
| `amount` | string | ✅       | `SUM(dataItems[].amount)` | Total claimed USDT |

> ⚠️ This scenario does **not** include `topic` / `outcome` fields (even single-claim shows only the
> total).

#### Copy Template

> Successfully claimed ${amount} USDT.

---

### 4.10 `web3_prediction_pm_claim_fail`

#### Trigger

Claim entirely fails (single fail or batch all fail).

#### refId

`<refId>` = `batchId`

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3",
  "amount": "10.00",
  "outcome": "Yes"
}
```

| Field     | Type   | Required | Source                      | Description                                                               |
| --------- | ------ | -------- | --------------------------- | ------------------------------------------------------------------------- |
| `pushId`  | string | ✅       | System-generated            |                                                                           |
| `amount`  | string | ✅       | `dataItems[0].amount`       | Amount of the **first failed claim**                                      |
| `outcome` | string | ✅       | `dataItems[0].outcome.name` | Outcome name (e.g. `Yes`/`No`) of the **first failed claim**; may be `""` |

> ⚠️ Even if multiple claims fail in a batch, only the **first one's** amount/outcome is included.

#### Copy Template

> Failed to claim ${amount} from ${outcome}. Please try again.

---

### 4.11 `web3_prediction_pm_claim_partial_success`

#### Trigger

A batch claim is **partially successful** (some succeed, some fail).

#### refId

`<refId>` = `batchId`

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4"
}
```

| Field    | Type   | Required | Source           | Description |
| -------- | ------ | -------- | ---------------- | ----------- |
| `pushId` | string | ✅       | System-generated |             |

> ⚠️ This scenario contains **only `pushId`** — no business fields. Query REST API for details.

#### Copy Template

> Partially claimed. Please try again to collect the remaining.

---

### 4.12 `web3_prediction_pm_transfer_success`

#### Trigger

Fund transfer succeeds (deposit into prediction wallet / withdraw out).

#### refId

`<refId>` = `FundTransferOrder.transferId`

#### Payload

```json
{
  "pushId": "pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5",
  "amount": "100.00"
}
```

| Field    | Type   | Required | Source                              | Description              |
| -------- | ------ | -------- | ----------------------------------- | ------------------------ |
| `pushId` | string | ✅       | System-generated                    |                          |
| `amount` | string | ✅       | `FundTransferOrder.fromTokenAmount` | Token amount transferred |

> ⚠️ Direction (deposit/withdraw) is not distinguished, and token type is not carried (currently
> USDT only).

---

### 4.13 `web3_prediction_pm_transfer_fail`

#### Trigger

Fund transfer fails.

#### refId

`<refId>` = `transferId`

#### Payload

```json
{
  "pushId": "pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6",
  "amount": "100.00"
}
```

| Field    | Type   | Required | Source                              | Description              |
| -------- | ------ | -------- | ----------------------------------- | ------------------------ |
| `pushId` | string | ✅       | System-generated                    |                          |
| `amount` | string | ✅       | `FundTransferOrder.fromTokenAmount` | Original transfer amount |

---

### 4.14 `web3_prediction_pm_market_close`

#### Trigger

After a market is resolved (`Market.status = RESOLVED`), pushed to **every user holding any
outcome** in that market (regardless of win or loss).

#### refId

`<refId>` = `marketId` (note: NOT outcomeId)

#### Payload

```json
{
  "pushId": "pm_8859231_pm_market_close_b4c5d6e7",
  "topic": "BTC will hi.."
}
```

| Field    | Type   | Required | Source                 | Description |
| -------- | ------ | -------- | ---------------------- | ----------- |
| `pushId` | string | ✅       | System-generated       |             |
| `topic`  | string | ✅       | Truncated market title |             |

> ⚠️ This scenario does **not** include `amount` / `outcome` / `isWinner`. To display user PnL,
> query REST API after receiving the push.

#### Copy Template

> Market ${topic} has been resolved. Please claim your winnings.

---

### 4.15 Field Matrix Quick Reference

| Scenario                     | `pushId` | `amount` | `topic` | `outcome` | refId Type |
| ---------------------------- | :------: | :------: | :-----: | :-------: | ---------- |
| pm_market_buy_success        |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_buy_fail           |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_sell_success       |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_sell_fail          |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_limit_submit_success      |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| **pm_limit_submit_fail**     |    ✅    |    ❌    |   ✅    |     —     | orderId    |
| pm_limit_order_filled        |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_limit_order_partial_fill  |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| **pm_claim_success**         |    ✅    |    ✅    |   ❌    |    ❌     | batchId    |
| **pm_claim_fail**            |    ✅    |    ✅    |   ❌    |    ✅     | batchId    |
| **pm_claim_partial_success** |    ✅    |    ❌    |   ❌    |    ❌     | batchId    |
| pm_transfer_success          |    ✅    |    ✅    |   ❌    |    ❌     | transferId |
| pm_transfer_fail             |    ✅    |    ✅    |   ❌    |    ❌     | transferId |
| **pm_market_close**          |    ✅    |    ❌    |   ✅    |    ❌     | marketId   |

---

---

# 預測市場錢包事件 WebSocket 數據流

## 1. 概覽

### 1.1 業務說明

Binance Web3 Prediction（預測市場）通過 **Binance SApi
WebSocket 通道**向**單個使用者**即時推送 14 種業務事件，覆蓋交易（市價/限價）、收益領取（claim）、資金劃轉、市場結算 4 大類。

### 1.2 通道特性

| 項       | 說明                                                            |
| -------- | --------------------------------------------------------------- |
| 協議     | WebSocket（WSS）                                                |
| 閘道器   | Binance SApi WSS（與現貨 / U本位 SApi 共用同一連線基礎設施）    |
| 路由維度 | `(topic, userId)` 精確匹配，僅推送給匹配使用者                  |
| 投遞語義 | **at-most-once**（最多一次，不保證重發）                        |
| 順序性   | 同一 user 同一 topic **不保證嚴格順序**，建議用 `pushId` 做冪等 |
| 離線訊息 | **不快取**，重連後請通過 REST API 拉取最新狀態                  |
| 時延     | 業務事件觸發後 < 500 ms 投遞（不含網路）                        |
| 單條大小 | < 2 KB                                                          |

### 1.3 適用受眾

- 整合 Prediction 業務的錢包客戶端
- 第三方代理交易（agent trading）方
- 資料分析 / 風控類系統

---

## 2. WebSocket 連線

> 基礎連線規範完全遵循
> [Binance CMS General Info](https://developers.binance.com/docs/cms/general-info)。本節摘錄關鍵內容並補充 Prediction 特定示例。

### 2.1 連線 URL

**Base URL**:

```
wss://api.binance.com/sapi/wss
```

**完整連線 URL 格式**:

```
wss://api.binance.com/sapi/wss?random={random}&topic={topic}&recvWindow={recvWindow}&timestamp={timestamp}&signature={signature}
```

**示例（訂閱 prediction buy success topic）**:

```
wss://api.binance.com/sapi/wss?random=56724ac693184379ae23ffe5e910063c&topic=web3_prediction_pm_market_buy_success&recvWindow=30000&timestamp=1753244327210&signature=341098eff29e3ef395ed4ea85035bd7fe9e9356d2b0d4f1f97655c74516a2d65
```

### 2.2 URL 參數

| 參數         | 必填 | 說明                                               |
| ------------ | ---- | -------------------------------------------------- |
| `random`     | ✅   | 隨機字串或數字，建議 ≤ 32 字元，用於保證簽名唯一性 |
| `topic`      | ✅   | 訂閱的 topic，多個 topic 用豎線 `&#124;` 分隔      |
| `recvWindow` | ✅   | 時間視窗（ms），最大 60000                         |
| `timestamp`  | ✅   | 客戶端發起請求的毫秒級 UTC 時間戳                  |
| `signature`  | ✅   | HMAC SHA256 簽名（見下文）                         |

### 2.3 鑑權

#### Header

```
X-MBX-APIKEY: <your_api_key>
```

#### 簽名生成步驟

1. 收集所有 URL 參數（**不含 `signature`**）
2. 按參數名**字母升序**排列後拼接為 query string
3. 使用 Secret Key 對該字串 **HMAC SHA256**

**Payload 示例**:

```
random=56724ac693184379ae23ffe5e910063c&recvWindow=30000&timestamp=1753244327210&topic=web3_prediction_pm_market_buy_success
```

**Bash 驗證**:

```bash
echo -n "random=56724ac693184379ae23ffe5e910063c&recvWindow=30000&timestamp=1753244327210&topic=web3_prediction_pm_market_buy_success" \
  | openssl dgst -sha256 -hmac "<YOUR_SECRET_KEY>"
```

### 2.4 時間視窗

服務端校驗：`server_time <= timestamp + recvWindow`，超出則拒絕連線。建議客戶端定期校準本機時間與 Binance
Server Time。

### 2.5 連線生命週期

| 項                 | 規則                                               |
| ------------------ | -------------------------------------------------- |
| 單連線最長有效期   | **24 小時**                                        |
| 超時後             | 客戶端需重連，並**重新生成 timestamp + signature** |
| 服務端心跳超時斷連 | 1 分鐘未收到 PING                                  |

### 2.6 訂閱、取消訂閱、心跳、限流

> 完全遵循
> [Binance CMS 通用規範](https://developers.binance.com/docs/cms/general-info)，本文不重複列舉。

簡要要點：

- 連線時通過 URL 參數 `topic=topic1|topic2` 訂閱
- 連線後可通過 JSON 命令 `{"command":"SUBSCRIBE","value":"..."}` 動態訂閱 / 取消訂閱
- 客戶端需每 30 秒傳送一次 PING（空 payload）
- 單連線 5 條/秒訊息上限，超限斷連，反覆超限 IP 封禁

詳細欄位、響應結構、錯誤碼、重連建議請參考 CMS 文件。

---

## 3. 推送訊息通用結構

### 3.1 信封

每條業務推送由 SApi 閘道器投遞，整體結構遵循 SApi 推送規範，**業務 payload 即為 `data`
欄位中的 JSON 字串**：

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_buy_success",
  "data": "{\"pushId\":\"pm_PM2026052812345_pm_market_buy_success_a1b2c3d4\",\"amount\":\"12.34\",\"topic\":\"BTC will hi..\"}"
}
```

> 注意 `data` 欄位是**字串化的 JSON**，需要二次 `JSON.parse`。

### 3.2 業務 Payload 通用欄位

```json
{
  "pushId": "pm_<refId>_<scenarioCode>_<8hex>",
  "<businessField1>": "...",
  "<businessField2>": "..."
}
```

| 欄位         | 型別   | 必填     | 說明                             |
| ------------ | ------ | -------- | -------------------------------- |
| `pushId`     | string | ✅       | 推送唯一 ID，**所有 topic 都有** |
| 其他業務欄位 | string | 視 topic | 詳見第 4 節，型別統一為 string   |

### 3.3 `pushId` 格式

```
pm_<refId>_<scenarioCode>_<8hex>

示例：pm_PM2026052812345_pm_market_buy_success_a1b2c3d4
```

| 段               | 說明                                                                          |
| ---------------- | ----------------------------------------------------------------------------- |
| `pm_`            | 固定字首                                                                      |
| `<refId>`        | 業務關聯 ID（訂單 ID / claimBatchId / transferId / marketId 等，詳見第 4 節） |
| `<scenarioCode>` | 場景碼，與 topic 字尾一致                                                     |
| `<8hex>`         | 隨機 8 位 hex，保證唯一性                                                     |

---

## 4. Topic 列表與詳細 Payload

> 14 個 topic 全部以 `web3_prediction_` 為字首。第三方按需訂閱。

### 4.0 Topic 總覽

| #   | scenarioCode                  | Topic                                         | 觸發時機             |
| --- | ----------------------------- | --------------------------------------------- | -------------------- |
| 1   | `pm_market_buy_success`       | `web3_prediction_pm_market_buy_success`       | 市價買單完全成交     |
| 2   | `pm_market_buy_fail`          | `web3_prediction_pm_market_buy_fail`          | 市價買單失敗 / 過期  |
| 3   | `pm_market_sell_success`      | `web3_prediction_pm_market_sell_success`      | 市價賣單完全成交     |
| 4   | `pm_market_sell_fail`         | `web3_prediction_pm_market_sell_fail`         | 市價賣單失敗 / 過期  |
| 5   | `pm_limit_submit_success`     | `web3_prediction_pm_limit_submit_success`     | 限價單掛單成功       |
| 6   | `pm_limit_submit_fail`        | `web3_prediction_pm_limit_submit_fail`        | 限價單掛單失敗       |
| 7   | `pm_limit_order_filled`       | `web3_prediction_pm_limit_order_filled`       | 限價單完全成交       |
| 8   | `pm_limit_order_partial_fill` | `web3_prediction_pm_limit_order_partial_fill` | 限價單部分成交       |
| 9   | `pm_claim_success`            | `web3_prediction_pm_claim_success`            | 收益領取成功         |
| 10  | `pm_claim_fail`               | `web3_prediction_pm_claim_fail`               | 收益領取失敗         |
| 11  | `pm_claim_partial_success`    | `web3_prediction_pm_claim_partial_success`    | 收益批次領取部分成功 |
| 12  | `pm_transfer_success`         | `web3_prediction_pm_transfer_success`         | 資金劃轉成功         |
| 13  | `pm_transfer_fail`            | `web3_prediction_pm_transfer_fail`            | 資金劃轉失敗         |
| 14  | `pm_market_close`             | `web3_prediction_pm_market_close`             | 市場結算關閉通知     |

---

### 4.1 `web3_prediction_pm_market_buy_success`

#### 觸發條件

使用者的**市價買單**（Market Order BUY）完全成交（`OrderStatus = FILLED`）。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_success_a1b2c3d4",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源                         | 說明                                     |
| -------- | ------ | ---- | -------------------------------- | ---------------------------------------- |
| `pushId` | string | ✅   | 系統生成                         | 唯一 ID                                  |
| `amount` | string | ✅   | `OrderHistory.amountIn`          | 使用者支付的 USDT 金額，2 位小數向下截斷 |
| `topic`  | string | ✅   | `MarketTopic.title` 截斷 12 字元 | 市場標題                                 |

#### 文案模版

> Bought ${amount} USDT in ${topic}

---

### 4.2 `web3_prediction_pm_market_buy_fail`

#### 觸發條件

市價買單狀態變為 `FAILED` 或 `EXPIRED`。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源                | 說明                               |
| -------- | ------ | ---- | ----------------------- | ---------------------------------- |
| `pushId` | string | ✅   | 系統生成                |                                    |
| `amount` | string | ✅   | `OrderHistory.amountIn` | 原下單 USDT 金額（**非實際扣款**） |
| `topic`  | string | ✅   | 市場標題截斷            |                                    |

---

### 4.3 `web3_prediction_pm_market_sell_success`

#### 觸發條件

使用者的**市價賣單**（Market Order SELL）完全成交（`FILLED`）。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_success_c3d4e5f6",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

| 欄位     | 型別   | 必填 | 資料來源               | 說明                                  |
| -------- | ------ | ---- | ---------------------- | ------------------------------------- |
| `pushId` | string | ✅   | 系統生成               |                                       |
| `amount` | string | ✅   | `amountOut − totalFee` | 使用者實際到手 USDT（**已扣手續費**） |
| `topic`  | string | ✅   | 市場標題截斷           |                                       |

---

### 4.4 `web3_prediction_pm_market_sell_fail`

#### 觸發條件

市價賣單 `FAILED` 或 `EXPIRED`。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

| 欄位     | 型別   | 必填 | 資料來源               | 說明                                 |
| -------- | ------ | ---- | ---------------------- | ------------------------------------ |
| `pushId` | string | ✅   | 系統生成               |                                      |
| `amount` | string | ✅   | `amountOut − totalFee` | 失敗前預期到賬金額（**未實際入賬**） |
| `topic`  | string | ✅   | 市場標題截斷           |                                      |

---

### 4.5 `web3_prediction_pm_limit_submit_success`

#### 觸發條件

使用者的**限價單**成功掛入訂單簿。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源                            | 說明       |
| -------- | ------ | ---- | ----------------------------------- | ---------- |
| `pushId` | string | ✅   | 系統生成                            |            |
| `amount` | string | ✅   | BUY: `amountIn` / SELL: `amountOut` | 限價單總額 |
| `topic`  | string | ✅   | 市場標題截斷                        |            |

---

### 4.6 `web3_prediction_pm_limit_submit_fail`

#### 觸發條件

限價單掛單失敗（提交時即被拒絕）。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源     | 說明 |
| -------- | ------ | ---- | ------------ | ---- |
| `pushId` | string | ✅   | 系統生成     |      |
| `topic`  | string | ✅   | 市場標題截斷 |      |

> ⚠️ **特別注意**：本場景**不攜帶** `amount` 欄位。

#### 文案模版

> Failed to submit your limit order for ${topic}. Please try again.

---

### 4.7 `web3_prediction_pm_limit_order_filled`

#### 觸發條件

已掛入訂單簿的限價單**完全成交**。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源                                       | 說明                |
| -------- | ------ | ---- | ---------------------------------------------- | ------------------- |
| `pushId` | string | ✅   | 系統生成                                       |                     |
| `amount` | string | ✅   | BUY: `amountIn` / SELL: `amountOut − totalFee` | 全部成交對應的 USDT |
| `topic`  | string | ✅   | 市場標題截斷                                   |                     |

---

### 4.8 `web3_prediction_pm_limit_order_partial_fill`

#### 觸發條件

限價單**部分成交**（`PARTIALLY_FILLED`）。每次新一筆部分成交都會推送。

#### refId

`<refId>` = `OrderHistory.orderId`

#### Payload

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1",
  "amount": "30.00",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源                                       | 說明                                   |
| -------- | ------ | ---- | ---------------------------------------------- | -------------------------------------- |
| `pushId` | string | ✅   | 系統生成                                       |                                        |
| `amount` | string | ✅   | BUY: `amountIn` / SELL: `amountOut − totalFee` | **本次部分成交後累計**金額，非單次增量 |
| `topic`  | string | ✅   | 市場標題截斷                                   |                                        |

> ⚠️ 同一筆限價單可能多次推送，客戶端**務必用 `pushId` 去重**。

---

### 4.9 `web3_prediction_pm_claim_success`

#### 觸發條件

使用者領取（claim）收益**全部成功**：單筆成功 或 批次全部成功。

#### refId

`<refId>` = `batchId`（claim 批次 ID）

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2",
  "amount": "50.00"
}
```

| 欄位     | 型別   | 必填 | 資料來源                  | 說明              |
| -------- | ------ | ---- | ------------------------- | ----------------- |
| `pushId` | string | ✅   | 系統生成                  |                   |
| `amount` | string | ✅   | `SUM(dataItems[].amount)` | 多筆合計到賬 USDT |

> ⚠️ 本場景**不含** `topic` / `outcome` 欄位（即使是單筆 claim 也只顯示總額）。

#### 文案模版

> Successfully claimed ${amount} USDT.

---

### 4.10 `web3_prediction_pm_claim_fail`

#### 觸發條件

claim 全部失敗（單筆失敗或批次全部失敗）。

#### refId

`<refId>` = `batchId`

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3",
  "amount": "10.00",
  "outcome": "Yes"
}
```

| 欄位      | 型別   | 必填 | 資料來源                    | 說明                                                               |
| --------- | ------ | ---- | --------------------------- | ------------------------------------------------------------------ |
| `pushId`  | string | ✅   | 系統生成                    |                                                                    |
| `amount`  | string | ✅   | `dataItems[0].amount`       | **首筆失敗 claim** 的金額                                          |
| `outcome` | string | ✅   | `dataItems[0].outcome.name` | **首筆失敗 claim** 對應的 outcome 名（如 `Yes`/`No`，可能為 `""`） |

> ⚠️ 即使批次多筆失敗，也**只取第一筆**的 amount/outcome。

#### 文案模版

> Failed to claim ${amount} from ${outcome}. Please try again.

---

### 4.11 `web3_prediction_pm_claim_partial_success`

#### 觸發條件

批次 claim **部分成功部分失敗**。

#### refId

`<refId>` = `batchId`

#### Payload

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4"
}
```

| 欄位     | 型別   | 必填 | 資料來源 | 說明 |
| -------- | ------ | ---- | -------- | ---- |
| `pushId` | string | ✅   | 系統生成 |      |

> ⚠️ 本場景**僅有 `pushId`，無任何業務欄位**。詳情請客戶端調 REST API 查詢。

#### 文案模版

> Partially claimed. Please try again to collect the remaining.

---

### 4.12 `web3_prediction_pm_transfer_success`

#### 觸發條件

資金劃轉成功（充值進 prediction 錢包 / 提現出 prediction 錢包）。

#### refId

`<refId>` = `FundTransferOrder.transferId`

#### Payload

```json
{
  "pushId": "pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5",
  "amount": "100.00"
}
```

| 欄位     | 型別   | 必填 | 資料來源                            | 說明            |
| -------- | ------ | ---- | ----------------------------------- | --------------- |
| `pushId` | string | ✅   | 系統生成                            |                 |
| `amount` | string | ✅   | `FundTransferOrder.fromTokenAmount` | 劃轉 token 數量 |

> ⚠️ 不區分充值/提現方向，也不攜帶 token 型別（當前業務上僅 USDT）。

---

### 4.13 `web3_prediction_pm_transfer_fail`

#### 觸發條件

資金劃轉失敗。

#### refId

`<refId>` = `transferId`

#### Payload

```json
{
  "pushId": "pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6",
  "amount": "100.00"
}
```

| 欄位     | 型別   | 必填 | 資料來源                            | 說明       |
| -------- | ------ | ---- | ----------------------------------- | ---------- |
| `pushId` | string | ✅   | 系統生成                            |            |
| `amount` | string | ✅   | `FundTransferOrder.fromTokenAmount` | 原劃轉金額 |

---

### 4.14 `web3_prediction_pm_market_close`

#### 觸發條件

市場結算（`Market.status = RESOLVED`）後，對**所有持有該市場任意 outcome 倉位**的使用者推送（無論持倉是否 win）。

#### refId

`<refId>` = `marketId`（注意：不是 outcomeId）

#### Payload

```json
{
  "pushId": "pm_8859231_pm_market_close_b4c5d6e7",
  "topic": "BTC will hi.."
}
```

| 欄位     | 型別   | 必填 | 資料來源     | 說明 |
| -------- | ------ | ---- | ------------ | ---- |
| `pushId` | string | ✅   | 系統生成     |      |
| `topic`  | string | ✅   | 市場標題截斷 |      |

> ⚠️ 本場景**不含** `amount` / `outcome` / `isWinner`。展示使用者持倉盈虧請收到推送後調 REST
> API 查詢。

#### 文案模版

> Market ${topic} has been resolved. Please claim your winnings.

---

### 4.15 欄位矩陣速查

| Scenario                     | `pushId` | `amount` | `topic` | `outcome` | refId 型別 |
| ---------------------------- | :------: | :------: | :-----: | :-------: | ---------- |
| pm_market_buy_success        |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_buy_fail           |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_sell_success       |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_market_sell_fail          |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_limit_submit_success      |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| **pm_limit_submit_fail**     |    ✅    |    ❌    |   ✅    |     —     | orderId    |
| pm_limit_order_filled        |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| pm_limit_order_partial_fill  |    ✅    |    ✅    |   ✅    |     —     | orderId    |
| **pm_claim_success**         |    ✅    |    ✅    |   ❌    |    ❌     | batchId    |
| **pm_claim_fail**            |    ✅    |    ✅    |   ❌    |    ✅     | batchId    |
| **pm_claim_partial_success** |    ✅    |    ❌    |   ❌    |    ❌     | batchId    |
| pm_transfer_success          |    ✅    |    ✅    |   ❌    |    ❌     | transferId |
| pm_transfer_fail             |    ✅    |    ✅    |   ❌    |    ❌     | transferId |
| **pm_market_close**          |    ✅    |    ❌    |   ✅    |    ❌     | marketId   |

---