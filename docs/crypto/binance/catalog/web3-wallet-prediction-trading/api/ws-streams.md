---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/web3-wallet-prediction-trading/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-23 18:49:47.132505
---

# Prediction Trading Streams

Schema: https://developers.binance.com/en/docs/catalog/web3-wallet-prediction-trading/api/ws-streams/1.0.0/schema.yaml

Binance Web3 Prediction pushes 14 kinds of real-time events over the Binance SApi WebSocket channel, covering market and limit trading, reward claims, fund transfers and market resolution, plus order book (bid/ask) quotes per market. Trading events go only to the user they belong to; order book quotes go to everyone subscribed. A message may occasionally be missed, order is not guaranteed, and nothing is stored while you are offline — after reconnecting, fetch the latest state from the REST API and drop duplicates using `pushId` (business events) or `marketId` + `updateTimestampMs` (order book).

Binance Web3 Prediction（預測市場）通過 Binance SApi WebSocket 通道即時推送 14 種事件，涵蓋市價 / 限價交易、收益領取、資金劃轉與市場結算，並按市場推送訂單簿（bid/ask）行情。交易類事件僅推送給對應使用者；訂單簿行情推送給所有訂閱方。訊息可能偶爾丟失、不保證順序，離線期間也不快取——重連後請通過 REST API 拉取最新狀態，並用 `pushId`（業務事件）或 `marketId` + `updateTimestampMs`（訂單簿）去重。

版本: 1.0.0

## 服务地址

- `wss://api.binance.com/sapi/wss`

## 接口列表

- `web3_prediction_orderbook_{marketId}` — Prediction Order Book by marketId
- `web3_prediction_pm_claim_fail` — Reward claim failed
- `web3_prediction_pm_claim_partial_success` — Batch claim partially succeeded
- `web3_prediction_pm_claim_success` — Reward claim succeeded
- `web3_prediction_pm_limit_order_filled` — Limit order fully filled
- `web3_prediction_pm_limit_order_partial_fill` — Limit order partially filled
- `web3_prediction_pm_limit_submit_fail` — Limit order submission failed
- `web3_prediction_pm_limit_submit_success` — Limit order submitted successfully
- `web3_prediction_pm_market_buy_fail` — Market buy order failed / expired
- `web3_prediction_pm_market_buy_success` — Market buy order fully filled
- `web3_prediction_pm_market_sell_fail` — Market sell order failed / expired
- `web3_prediction_pm_market_sell_success` — Market sell order fully filled
- `web3_prediction_pm_transfer_fail` — Fund transfer failed
- `web3_prediction_pm_transfer_success` — Fund transfer succeeded
- `web3_prediction_pm_market_close` — Market resolution notification

## Prediction Order Book by marketId（預測訂單簿（按 marketId））

流名称: `web3_prediction_orderbook_{marketId}`

Order book (bid/ask) updates for one market. Only active markets are pushed.

指定 marketId 的訂單簿（bid/ask）更新，僅推送活躍市場。

更新速度: Real-time

Operation ID: `predictionOrderBookByMarketId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marketId | path | string | 是 | Market ID to subscribe to — the `marketId` inside `markets[]` returned by `market/list`<br>or `market/detail`. It is **not** `marketTopicId` and **not** `externalId`. A wrong id is<br>never rejected: subscribing with `marketTopicId`, `externalId`, or with a closed or<br>resolved market returns the same successful `COMMAND` reply as a correct id and then<br>pushes nothing at all, so a stream that stays silent is far more likely a wrong id than<br>a broken connection.<br>要訂閱的 market ID，取 `market/list` 或 `market/detail` 回應中 `markets[]` 裡的<br>`marketId`；**不是** `marketTopicId`，也**不是** `externalId`。錯誤的 id 不會被拒絕：使用<br>`marketTopicId`、`externalId` 或已關閉、已結算的市場訂閱時，會收到與正確 id 相同的成功<br>`COMMAND` 響應，之後卻沒有任何推送；因此流一直靜默，更可能是 id 用錯，而不是連線故障。<br>例: `8859231` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_orderbook_8859231` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_orderbook_8859231"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msgType | string |  | Message type, always `orderbook`.<br>訊息型別，固定為 `orderbook`。<br>例: `orderbook` |
| marketId | integer (int64) |  | Market ID of this order book, the same `markets[].marketId` used by the REST<br>API.<br>本訂單簿對應的 market ID，與 REST API 中 `markets[].marketId` 一致。<br>例: `8859231` |
| updateTimestampMs | integer (int64) |  | Quote update time in milliseconds (UTC). Messages for the same market may arrive<br>out of order, so discard anything older than the snapshot you already have.<br>行情更新時間（毫秒，UTC）。同一市場的訊息可能亂序到達，請丟棄早於當前快照的訊息。<br>例: `1717420800123` |
| asks | oneOf[][] |  | Ask levels sorted by price **ascending**, usually the top 50 or fewer; an empty<br>array means no asks. Values may carry floating-point noise (e.g.<br>`6865.999999999999`), so round them before display.<br>賣單檔位列表，按 price **升序**排列，通常為前 50 檔以內；空陣列表示無賣單。數值可能帶浮點誤差（如<br>`6865.999999999999`），展示前請自行取整。 |
| bids | oneOf[][] |  | Bid levels sorted by price **descending**, usually the top 50 or fewer; an empty<br>array means no bids. Values may carry floating-point noise (e.g.<br>`6865.999999999999`), so round them before display.<br>買單檔位列表，按 price **降序**排列，通常為前 50 檔以內；空陣列表示無買單。數值可能帶浮點誤差（如<br>`6865.999999999999`），展示前請自行取整。 |

```json
{
  "msgType": "orderbook",
  "marketId": 8859231,
  "updateTimestampMs": 1717420800123,
  "asks": [
    [
      0.32,
      500
    ],
    [
      0.33,
      1200.5
    ]
  ],
  "bids": [
    [
      0.31,
      800
    ],
    [
      0.3,
      2000
    ]
  ]
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_orderbook_8859231` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"msgType":"orderbook","marketId":8859231,"updateTimestampMs":1717420800123,"asks":[[0.32,500],[0.33,1200.5]],"bids":[[0.31,800],[0.3,2000]]}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_orderbook_8859231",
  "data": "{\"msgType\":\"orderbook\",\"marketId\":8859231,\"updateTimestampMs\":1717420800123,\"asks\":[[0.32,500],[0.33,1200.5]],\"bids\":[[0.31,800],[0.3,2000]]}"
}
```

## Reward claim failed（收益領取失敗）

流名称: `web3_prediction_pm_claim_fail`

Pushed when a claim fails completely — a single claim, or every item of a batch. For a batch,
only the first failed item's amount and outcome are included.

領取完全失敗（單筆失敗，或批次全部失敗）時推送。批次失敗時只取第一筆的金額與 outcome。

更新速度: Real-time

Operation ID: `rewardClaimFailed`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_claim_fail` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_claim_fail"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3` |
| amount | string |  | Amount of the **first failed claim**. Rounded down to 2 decimals; shown as<br>`<0.01` if smaller.<br>**首筆失敗領取**的金額。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `10.00` |
| outcome | string |  | Outcome name of the **first failed claim**, such as `Yes` or `No`; empty if<br>unavailable.<br>**首筆失敗領取**對應的 outcome 名稱，如 `Yes` / `No`；資料缺失時為空字串。<br>例: `Yes` |

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3",
  "amount": "10.00",
  "outcome": "Yes"
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_claim_fail` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3","amount":"10.00","outcome":"Yes"}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_claim_fail",
  "data": "{\"pushId\":\"pm_CLAIM_BATCH_20260528002_pm_claim_fail_d0e1f2a3\",\"amount\":\"10.00\",\"outcome\":\"Yes\"}"
}
```

## Batch claim partially succeeded（收益批次領取部分成功）

流名称: `web3_prediction_pm_claim_partial_success`

Pushed when only part of a batch claim succeeds. Only `pushId` is included — call the REST
API for details.

批次領取部分成功、部分失敗時推送。本場景僅有 `pushId`，詳情請調 REST API 查詢。

更新速度: Real-time

Operation ID: `batchClaimPartiallySucceeded`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_claim_partial_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_claim_partial_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4` |

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4"
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_claim_partial_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4"}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_claim_partial_success",
  "data": "{\"pushId\":\"pm_CLAIM_BATCH_20260528003_pm_claim_partial_success_e1f2a3b4\"}"
}
```

## Reward claim succeeded（收益領取成功）

流名称: `web3_prediction_pm_claim_success`

Pushed when a claim fully succeeds — a single claim, or every item of a batch. Only the total
is reported; no market title or outcome is included.

領取完全成功（單筆成功，或批次全部成功）時推送。僅顯示總額，不含市場標題與 outcome。

更新速度: Real-time

Operation ID: `rewardClaimSucceeded`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_claim_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_claim_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2` |
| amount | string |  | Total USDT claimed. Rounded down to 2 decimals; shown as `<0.01` if smaller.<br>合計到賬的 USDT。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `50.00` |

```json
{
  "pushId": "pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2",
  "amount": "50.00"
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_claim_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2","amount":"50.00"}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_claim_success",
  "data": "{\"pushId\":\"pm_CLAIM_BATCH_20260528001_pm_claim_success_c9d0e1f2\",\"amount\":\"50.00\"}"
}
```

## Limit order fully filled（限價單完全成交）

流名称: `web3_prediction_pm_limit_order_filled`

Pushed when a **limit order** is fully filled.

**限價單**完全成交時推送。

更新速度: Real-time

Operation ID: `limitOrderFullyFilled`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_limit_order_filled` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_limit_order_filled"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0` |
| amount | string |  | Filled amount in USDT — paid for a buy, received after fees for a sell. Rounded<br>down to 2 decimals; shown as `<0.01` if smaller.<br>成交金額（USDT）——買入為支付金額，賣出為扣除手續費後的到賬金額。2 位小數向下截斷；小於 0.01 時顯示為<br>`<0.01`。<br>例: `100.00` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_limit_order_filled` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0","amount":"100.00","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_limit_order_filled",
  "data": "{\"pushId\":\"pm_PM2026052812347_pm_limit_order_filled_a7b8c9d0\",\"amount\":\"100.00\",\"topic\":\"BTC will hi..\"}"
}
```

## Limit order partially filled（限價單部分成交）

流名称: `web3_prediction_pm_limit_order_partial_fill`

Pushed on each new partial fill of a **limit order**. One order can be pushed several times,
so always remove duplicates by `pushId`.

**限價單**每次新增部分成交時推送。同一筆限價單可能多次推送，請務必用 `pushId` 去重。

更新速度: Real-time

Operation ID: `limitOrderPartiallyFilled`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_limit_order_partial_fill` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_limit_order_partial_fill"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1` |
| amount | string |  | **Total** filled so far in USDT, not just this fill — paid for a buy, received<br>after fees for a sell. Rounded down to 2 decimals; shown as `<0.01` if smaller.<br>截至本次的**累計**成交金額（USDT），非單次增量——買入為支付金額，賣出為扣除手續費後的到賬金額。2<br>位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `30.00` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1",
  "amount": "30.00",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_limit_order_partial_fill` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1","amount":"30.00","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_limit_order_partial_fill",
  "data": "{\"pushId\":\"pm_PM2026052812347_pm_limit_order_partial_fill_b8c9d0e1\",\"amount\":\"30.00\",\"topic\":\"BTC will hi..\"}"
}
```

## Limit order submission failed（限價單掛單失敗）

流名称: `web3_prediction_pm_limit_submit_fail`

Pushed when a **limit order** is rejected when placed. No `amount` is included.

**限價單**在掛單階段被拒絕時推送。本場景不含 `amount` 欄位。

更新速度: Real-time

Operation ID: `limitOrderSubmissionFailed`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_limit_submit_fail` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_limit_submit_fail"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_limit_submit_fail` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_limit_submit_fail",
  "data": "{\"pushId\":\"pm_PM2026052812347_pm_limit_submit_fail_f6a7b8c9\",\"topic\":\"BTC will hi..\"}"
}
```

## Limit order submitted successfully（限價單掛單成功）

流名称: `web3_prediction_pm_limit_submit_success`

Pushed when the user's **limit order** is successfully placed on the order book.

使用者的**限價單**成功掛到訂單簿時推送。

更新速度: Real-time

Operation ID: `limitOrderSubmittedSuccessfully`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_limit_submit_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_limit_submit_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8` |
| amount | string |  | Total order amount in USDT, before fees. Rounded down to 2 decimals; shown as<br>`<0.01` if smaller.<br>限價單總額（USDT，未扣手續費）。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `100.00` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8",
  "amount": "100.00",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_limit_submit_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8","amount":"100.00","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_limit_submit_success",
  "data": "{\"pushId\":\"pm_PM2026052812347_pm_limit_submit_success_e5f6a7b8\",\"amount\":\"100.00\",\"topic\":\"BTC will hi..\"}"
}
```

## Market buy order failed / expired（市價買單失敗 / 過期）

流名称: `web3_prediction_pm_market_buy_fail`

Pushed when the user's **market buy order** fails or expires.

使用者的**市價買單**失敗或過期時推送。

更新速度: Real-time

Operation ID: `marketBuyOrderFailed`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_market_buy_fail` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_market_buy_fail"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5` |
| amount | string |  | Original order amount in USDT — **not** actually charged. Rounded down to 2<br>decimals; shown as `<0.01` if smaller.<br>原下單的 USDT 金額（**未實際扣款**）。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `12.34` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_market_buy_fail` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5","amount":"12.34","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_buy_fail",
  "data": "{\"pushId\":\"pm_PM2026052812345_pm_market_buy_fail_b2c3d4e5\",\"amount\":\"12.34\",\"topic\":\"BTC will hi..\"}"
}
```

## Market buy order fully filled（市價買單完全成交）

流名称: `web3_prediction_pm_market_buy_success`

Pushed when the user's **market buy order** is fully filled.

使用者的**市價買單**完全成交時推送。

更新速度: Real-time

Operation ID: `marketBuyOrderFullyFilled`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_market_buy_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_market_buy_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812345_pm_market_buy_success_a1b2c3d4` |
| amount | string |  | USDT the user paid. Rounded down to 2 decimals; shown as `<0.01` if smaller.<br>使用者支付的 USDT。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `12.34` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_PM2026052812345_pm_market_buy_success_a1b2c3d4",
  "amount": "12.34",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_market_buy_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812345_pm_market_buy_success_a1b2c3d4","amount":"12.34","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_buy_success",
  "data": "{\"pushId\":\"pm_PM2026052812345_pm_market_buy_success_a1b2c3d4\",\"amount\":\"12.34\",\"topic\":\"BTC will hi..\"}"
}
```

## Market sell order failed / expired（市價賣單失敗 / 過期）

流名称: `web3_prediction_pm_market_sell_fail`

Pushed when the user's **market sell order** fails or expires.

使用者的**市價賣單**失敗或過期時推送。

更新速度: Real-time

Operation ID: `marketSellOrderFailedExpired`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_market_sell_fail` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_market_sell_fail"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7` |
| amount | string |  | USDT the user would have received after fees — **not** credited. Rounded down to<br>2 decimals; shown as `<0.01` if smaller.<br>失敗前預期扣除手續費後到賬的 USDT（**未實際入賬**）。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `10.50` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `ETH price..` |

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_market_sell_fail` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7","amount":"10.50","topic":"ETH price.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_sell_fail",
  "data": "{\"pushId\":\"pm_PM2026052812346_pm_market_sell_fail_d4e5f6a7\",\"amount\":\"10.50\",\"topic\":\"ETH price..\"}"
}
```

## Market sell order fully filled（市價賣單完全成交）

流名称: `web3_prediction_pm_market_sell_success`

Pushed when the user's **market sell order** is fully filled.

使用者的**市價賣單**完全成交時推送。

更新速度: Real-time

Operation ID: `marketSellOrderFullyFilled`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_market_sell_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_market_sell_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_PM2026052812346_pm_market_sell_success_c3d4e5f6` |
| amount | string |  | USDT the user received, **after fees**. Rounded down to 2 decimals; shown as<br>`<0.01` if smaller.<br>使用者實際到手的 USDT（**已扣手續費**）。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `10.50` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `ETH price..` |

```json
{
  "pushId": "pm_PM2026052812346_pm_market_sell_success_c3d4e5f6",
  "amount": "10.50",
  "topic": "ETH price.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_market_sell_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_PM2026052812346_pm_market_sell_success_c3d4e5f6","amount":"10.50","topic":"ETH price.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_sell_success",
  "data": "{\"pushId\":\"pm_PM2026052812346_pm_market_sell_success_c3d4e5f6\",\"amount\":\"10.50\",\"topic\":\"ETH price..\"}"
}
```

## Fund transfer failed（資金劃轉失敗）

流名称: `web3_prediction_pm_transfer_fail`

Pushed when a fund transfer fails.

資金劃轉失敗時推送。

更新速度: Real-time

Operation ID: `fundTransferFailed`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_transfer_fail` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_transfer_fail"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6` |
| amount | string |  | Amount of the attempted transfer. Rounded down to 2 decimals; shown as `<0.01`<br>if smaller.<br>原劃轉數量。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `100.00` |

```json
{
  "pushId": "pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6",
  "amount": "100.00"
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_transfer_fail` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6","amount":"100.00"}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_transfer_fail",
  "data": "{\"pushId\":\"pm_TRANSFER_20260528002_pm_transfer_fail_a3b4c5d6\",\"amount\":\"100.00\"}"
}
```

## Fund transfer succeeded（資金劃轉成功）

流名称: `web3_prediction_pm_transfer_success`

Pushed when a fund transfer into or out of the prediction wallet succeeds. The direction and
the token are not included (currently USDT only).

資金轉入或轉出 prediction 錢包成功時推送。不區分轉入 / 轉出方向，也不攜帶幣種（當前僅 USDT）。

更新速度: Real-time

Operation ID: `fundTransferSucceeded`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_transfer_success` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_transfer_success"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5` |
| amount | string |  | Amount transferred. Rounded down to 2 decimals; shown as `<0.01` if smaller.<br>劃轉數量。2 位小數向下截斷；小於 0.01 時顯示為 `<0.01`。<br>例: `100.00` |

```json
{
  "pushId": "pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5",
  "amount": "100.00"
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_transfer_success` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5","amount":"100.00"}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_transfer_success",
  "data": "{\"pushId\":\"pm_TRANSFER_20260528001_pm_transfer_success_f2a3b4c5\",\"amount\":\"100.00\"}"
}
```

## Market resolution notification（市場結算關閉通知）

流名称: `web3_prediction_pm_market_close`

Pushed when a market is resolved, to every user holding a position in it, win or lose. No
amount or outcome is included — call the REST API for the user's profit and loss.

市場結算後，向所有持有該市場倉位的使用者推送（無論輸贏）。本場景不含金額與 outcome，使用者盈虧請調 REST API 查詢。

更新速度: Real-time

Operation ID: `marketResolutionNotification`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| command | string | 是 | Subscription command.<br>訂閱命令。<br>枚举: `SUBSCRIBE`, `UNSUBSCRIBE`<br>例: `SUBSCRIBE` |
| value | string | 是 | Topics to subscribe to, joined by `\|`.<br>要訂閱的 topic，多個用 `\|` 連接。<br>例: `web3_prediction_pm_market_close` |

```json
{
  "command": "SUBSCRIBE",
  "value": "web3_prediction_pm_market_close"
}
```

### 响应 Business Payload：Prediction Stream response / 預測流響應

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| pushId | string |  | Unique ID of this push. Use it to remove duplicates.<br>本次推送的唯一 ID，用於去重。<br>例: `pm_8859231_pm_market_close_b4c5d6e7` |
| topic | string |  | Market title, cut to 12 characters with `..` added when longer; empty if<br>unavailable.<br>市場標題，超過 12 字元時截斷並追加 `..`；標題缺失時為空字串。<br>例: `BTC will hi..` |

```json
{
  "pushId": "pm_8859231_pm_market_close_b4c5d6e7",
  "topic": "BTC will hi.."
}
```

### 响应 Topic Push：Gateway envelope; `data` holds the payload above as a JSON string.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Envelope type. Business pushes use `DATA`; command replies use `COMMAND`.<br>信封類型：業務推送為 `DATA`，命令響應為 `COMMAND`。<br>枚举: `DATA`<br>例: `DATA` |
| topic | string | 是 | Topic this push came from.<br>本次推送所屬的 topic。<br>例: `web3_prediction_pm_market_close` |
| data | string | 是 | Business payload as a JSON string — parse it a second time.<br>業務負載，為 JSON 字串，需要再次解析。<br>例: `{"pushId":"pm_8859231_pm_market_close_b4c5d6e7","topic":"BTC will hi.."}` |

```json
{
  "type": "DATA",
  "topic": "web3_prediction_pm_market_close",
  "data": "{\"pushId\":\"pm_8859231_pm_market_close_b4c5d6e7\",\"topic\":\"BTC will hi..\"}"
}
```