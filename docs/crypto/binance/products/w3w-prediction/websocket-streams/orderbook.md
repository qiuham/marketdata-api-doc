---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/w3w-prediction/websocket-streams/orderbook
api_type: WebSocket
updated_at: 2026-11-20 18:37:03.838606
---

# Prediction Market — Orderbook WebSocket Streams (Overview)

## 1. Overview

### 1.1 Business Description

The Prediction service pulls real-time orderbook (bid/ask) data from upstream market makers
(Predict.fun) and broadcasts it via the **Binance SApi WebSocket channel** to all subscribers. Use
cases include:

- Client display of top-N bid/ask depth
- Trading terminals computing best execution price in real time
- Third-party market making / arbitrage strategies
- Data analytics platform feeds

### 1.2 Channel Characteristics

| Item               | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| Protocol           | WebSocket (WSS)                                                                                                |
| Gateway            | Binance SApi WSS                                                                                               |
| **Routing mode**   | **Broadcast by topic** (any connection subscribed to the topic receives it; **NOT routed by userId**)          |
| Delivery semantics | at-most-once                                                                                                   |
| Ordering           | **No strict ordering** is guaranteed for the same marketId; **use the `updateTimestampMs` field for ordering** |
| Offline messages   | Not cached — fetch the latest snapshot via REST API after reconnect                                            |
| Latency            | Delivered within < 200 ms after upstream event triggers (excluding network)                                    |
| Per-message size   | < 4 KB (typical markets ~0.5–2 KB)                                                                             |

### 1.3 Business Constraints

| Constraint             | Description                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| Active markets only    | Only continuously updating active markets are pushed; resolved / closed markets are not pushed       |
| Upstream dependency    | Quotes come from Predict.fun; if upstream disconnects, this channel pauses (no empty data is pushed) |
| Price / Size precision | `price` ∈ `(0, 1)` (2–6 decimals), `size` > 0 and may include decimals; both are JSON numbers        |

---

## 2. WebSocket Connection

> The basic connection specification fully follows
> [Binance CMS General Info](https://developers.binance.com/docs/cms/general-info). This section
> only lists orderbook-specific examples.

### 2.1 Connection URL Examples

Subscribe to a single market's orderbook:

```
wss://api.binance.com/sapi/wss?random={random}&topic=web3_prediction_orderbook_8859231&recvWindow=30000&timestamp={timestamp}&signature={signature}
```

Subscribe to multiple markets (separated by `|`):

```
?topic=web3_prediction_orderbook_8859231|web3_prediction_orderbook_8859232
```

### 2.2 Authentication & Signature

Identical to user event push (refer to the auth section in
[Binance CMS General Info](https://developers.binance.com/docs/cms/general-info)):

- Header: `X-MBX-APIKEY: <api_key>`
- Signature: HMAC SHA256(query string, secret_key)
- query string sorted alphabetically by parameter name

### 2.3 Subscribe / Heartbeat / Rate Limit

Fully follow CMS spec, not duplicated here:

- Client sends PING every 30 seconds
- Per-connection rate limit: 5 messages/second
- Single connection valid for 24h then must reconnect

---

## 3. Push Message Structure

### 3.1 Envelope

Each orderbook push is delivered by the SApi gateway. **The business payload is a JSON string inside
the `data` field**:

```json
{
  "type": "DATA",
  "topic": "web3_prediction_orderbook_8859231",
  "data": "{\"msgType\":\"orderbook\",\"marketId\":8859231,\"updateTimestampMs\":1717420800123,\"asks\":[[0.32,500],[0.33,1200]],\"bids\":[[0.31,800],[0.3,2000]]}"
}
```

> ⚠️ The `data` field is a **stringified JSON**. Requires a second `JSON.parse`.

### 3.2 Full Business Payload

```json
{
  "msgType": "orderbook",
  "marketId": 8859231,
  "updateTimestampMs": 1717420800123,
  "asks": [
    [0.32, 500],
    [0.33, 1200],
    [0.34, 300]
  ],
  "bids": [
    [0.31, 800],
    [0.3, 2000],
    [0.28, 1500]
  ]
}
```

### 3.3 Field Definitions

| Field               | Type          | Required | Description                                                                            |
| ------------------- | ------------- | -------- | -------------------------------------------------------------------------------------- |
| `msgType`           | string        | ✅       | Fixed value `"orderbook"`, used by clients to dispatch message types                   |
| `marketId`          | number (long) | ✅       | **Binance internal market ID** (mapped from upstream vendor ID), aligned with REST API |
| `updateTimestampMs` | number (long) | ✅       | Quote update millisecond UTC timestamp; **use this for out-of-order detection**        |
| `asks`              | array         | ✅       | List of ask levels, sorted by price **ascending**; empty array means no asks           |
| `bids`              | array         | ✅       | List of bid levels, sorted by price **descending**; empty array means no bids          |

### 3.4 Level Data Structure (asks / bids)

Each level is a **2-element array** of **JSON numbers**:

```
[<price>, <size>]
```

| Index | Field | Type   | Description                                                                      |
| ----- | ----- | ------ | -------------------------------------------------------------------------------- |
| `[0]` | price | number | Price ∈ `(0, 1)`, in outcome share/USDT ratio, e.g. `0.32` means 0.32 USDT/share |
| `[1]` | size  | number | Quantity (outcome shares), may include decimals, e.g. `500` / `500.5`            |

#### Notes

- **Values may carry floating-point noise** (e.g. `6865.999999999999`). Round before displaying or
  comparing.
- **`size = 0` does not appear**: upstream filters empty levels; size is always > 0.
- **Depth**: typically top N levels (the value depends on upstream policy, generally ≤ 50).

---

## 4. Topic

Each market has its own topic:

```
web3_prediction_orderbook_{marketId}
```

| Item         | Description                                                                         |
| ------------ | ----------------------------------------------------------------------------------- |
| Naming rule  | Prefix `web3_prediction_orderbook_` + market internal ID                            |
| Example      | `web3_prediction_orderbook_8859231`                                                 |
| Use case     | Orderbook components, single-market arbitrage, any client watching specific markets |
| Many markets | Concatenate topics with `&#124;` in one subscribe (mind the 5 msg/s limit)          |

---

## 5. Push Frequency & Recommendations

### 5.1 Push Frequency

| Item                      | Value                                                                |
| ------------------------- | -------------------------------------------------------------------- |
| Per-market update peak    | ~10 messages/sec (when upstream pushes full depth on active markets) |
| Per-market update average | ~1-3 messages/sec                                                    |

### 5.2 Client Processing Recommendations

| Item                    | Recommendation                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Throttling / debouncing | Debounce UI rendering at 100ms to avoid blocking the rendering thread                                                 |
| Out-of-order detection  | **Must** compare `updateTimestampMs` and discard messages older than the current snapshot                             |
| Reconnect compensation  | After reconnect, **first fetch a snapshot via REST API**, then apply WSS deltas (CMS does not cache offline messages) |
| Price / size parsing    | Values are JSON numbers; round them for display instead of printing them raw                                          |
| Empty market filtering  | Both `asks` and `bids` empty means no orders (paused / about-to-resolve markets); decide whether to render            |

### 5.3 Rate Limit Protection

```
If subscribing to N topics at once:
  - Use a single SUBSCRIBE command concatenating all topics (separated by |) to avoid hitting 5 msg/s
  - When switching many topics, use UNSUBSCRIBE to release unrelated markets and control bandwidth
  - Use ONE WSS connection for all prediction business (user events + orderbook); do NOT open separate connections per topic
```

---

---

# Prediction Market — Orderbook WebSocket 數據流（基本資訊）

## 1. 概覽

### 1.1 業務說明

Prediction 業務從上游做市商（Predict.fun）即時拉取行情盤口（訂單簿 bid/ask）資料，並通過 **Binance
SApi WebSocket 通道**廣播給所有訂閱方，用於：

- 客戶端展示買賣五檔 / 十檔深度
- 交易終端即時計算最優執行價
- 第三方做市 / 套利策略接入
- 資料分析平臺採集行情

### 1.2 通道特性

| 項           | 說明                                                                         |
| ------------ | ---------------------------------------------------------------------------- |
| 協議         | WebSocket (WSS)                                                              |
| 閘道器       | Binance SApi WSS                                                             |
| **路由模式** | **按 topic 廣播**（任何訂閱了該 topic 的連線都會收到，**不按 userId 路由**） |
| 投遞語義     | at-most-once                                                                 |
| 順序性       | 同一 marketId **不保證嚴格順序**；**用 `updateTimestampMs` 欄位排序**        |
| 離線訊息     | 不快取，重連後請通過 REST API 拉取最新快照                                   |
| 時延         | 上游事件觸發後 < 200 ms 投遞（不含網路）                                     |
| 單條大小     | < 4 KB（典型市場約 0.5–2 KB）                                                |

### 1.3 業務限制

| 限制            | 說明                                                                         |
| --------------- | ---------------------------------------------------------------------------- |
| 僅活躍市場      | 僅訂單簿持續更新的活躍市場會推送，已結算 / 已關閉市場不推送                  |
| 上游依賴        | 行情來源為 Predict.fun，上游斷連時本通道也會暫停推送（不會推空資料）         |
| 價格 / 數量精度 | price 範圍 `(0, 1)`（2~6 位小數），size > 0 且可能含小數；兩者均為 JSON 數字 |

---

## 2. WebSocket 連線

> 基礎連線規範完全遵循
> [Binance CMS General Info](https://developers.binance.com/docs/cms/general-info)。本節僅列示行情訂閱相關示例。

### 2.1 連線 URL 示例

訂閱單個市場的 orderbook：

```
wss://api.binance.com/sapi/wss?random={random}&topic=web3_prediction_orderbook_8859231&recvWindow=30000&timestamp={timestamp}&signature={signature}
```

訂閱多個市場（管道符 `|` 分隔）：

```
?topic=web3_prediction_orderbook_8859231|web3_prediction_orderbook_8859232
```

### 2.2 鑑權與簽名

完全等同於使用者事件推送（參考
[Binance CMS General Info](https://developers.binance.com/docs/cms/general-info) 的鑑權章節）：

- Header: `X-MBX-APIKEY: <api_key>`
- 簽名：HMAC SHA256(query string, secret_key)
- query string 按參數名字母升序拼接

### 2.3 訂閱、心跳、限流

完全遵循 CMS 規範，本文不重複列舉：

- 客戶端每 30 秒傳送 PING
- 單連線 5 條/秒訊息上限
- 單連線 24h 後需重連

---

## 3. 推送訊息結構

### 3.1 信封

每條 orderbook 推送由 SApi 閘道器投遞，**業務 payload 即 `data` 欄位中的 JSON 字串**：

```json
{
  "type": "DATA",
  "topic": "web3_prediction_orderbook_8859231",
  "data": "{\"msgType\":\"orderbook\",\"marketId\":8859231,\"updateTimestampMs\":1717420800123,\"asks\":[[0.32,500],[0.33,1200]],\"bids\":[[0.31,800],[0.3,2000]]}"
}
```

> ⚠️ `data` 欄位為**字串化的 JSON**，需要二次 `JSON.parse`。

### 3.2 業務 Payload 完整結構

```json
{
  "msgType": "orderbook",
  "marketId": 8859231,
  "updateTimestampMs": 1717420800123,
  "asks": [
    [0.32, 500],
    [0.33, 1200],
    [0.34, 300]
  ],
  "bids": [
    [0.31, 800],
    [0.3, 2000],
    [0.28, 1500]
  ]
}
```

### 3.3 欄位定義

| 欄位                | 型別          | 必填 | 說明                                                                    |
| ------------------- | ------------- | ---- | ----------------------------------------------------------------------- |
| `msgType`           | string        | ✅   | 固定為 `"orderbook"`，用於客戶端區分訊息型別                            |
| `marketId`          | number (long) | ✅   | **Binance 內部 market ID**（已從上游 vendor ID 對映），與 REST API 一致 |
| `updateTimestampMs` | number (long) | ✅   | 行情更新的毫秒級 UTC 時間戳，**用於亂序判定**                           |
| `asks`              | array         | ✅   | 賣單檔位列表，按 price **升序**排列；空陣列表示無賣單                   |
| `bids`              | array         | ✅   | 買單檔位列表，按 price **降序**排列；空陣列表示無買單                   |

### 3.4 檔位（asks / bids）資料結構

每個檔位是一個**長度為 2 的陣列**，元素均為 **JSON 數字**：

```
[<price>, <size>]
```

| 位置  | 欄位  | 型別   | 說明                                                                                  |
| ----- | ----- | ------ | ------------------------------------------------------------------------------------- |
| `[0]` | price | number | 價格，範圍 `(0, 1)`，單位為 outcome share/USDT 比率，例如 `0.32` 表示 0.32 USDT/share |
| `[1]` | size  | number | 數量（outcome shares），可能含小數，例如 `500` / `500.5`                              |

#### 注意點

- **數值可能帶浮點誤差**（如 `6865.999999999999`），展示或比較前請自行取整
- **`size = 0` 不會出現**：上游會過濾空檔位，size 始終 > 0
- **檔位深度**：通常返回前 N 檔（具體值隨上游策略調整，一般 ≤ 50 檔）

---

## 4. Topic

每個市場有各自的 topic：

```
web3_prediction_orderbook_{marketId}
```

| 項       | 說明                                                         |
| -------- | ------------------------------------------------------------ |
| 命名規則 | 字首 `web3_prediction_orderbook_` + 市場 internal ID         |
| 示例     | `web3_prediction_orderbook_8859231`                          |
| 適用     | 訂單簿元件、單 market 套利策略，或任何只關心特定市場的客戶端 |
| 多個市場 | 訂閱時用 `&#124;` 一次拼接多個 topic（注意 5 msg/s 限流）    |

---

## 5. 推送頻率與建議

### 5.1 推送頻率

| 項             | 數值                                |
| -------------- | ----------------------------------- |
| 單市場更新峰值 | ~10 條/秒（活躍市場上游全量推送時） |
| 單市場更新均值 | ~1-3 條/秒                          |

### 5.2 客戶端處理建議

| 項              | 建議                                                                                   |
| --------------- | -------------------------------------------------------------------------------------- |
| 節流 / 防抖     | UI 渲染建議 100ms 防抖，避免高頻更新拖累渲染執行緒                                     |
| 亂序判定        | **必須**用 `updateTimestampMs` 比對，丟棄比當前快照舊的訊息                            |
| 重連補償        | 重連後**先調 REST API 拉一次盤口快照**，再以 WSS 增量更新（CMS 不快取離線訊息）        |
| 價格 / 數量解析 | 均為 JSON 數字，展示前請自行取整，不要直接原樣輸出                                     |
| 異常市場過濾    | `asks` 和 `bids` 都為空陣列時表示無掛單（停擺 / 即將結算市場），客戶端自行決定是否展示 |

### 5.3 限流防護

```
若 N 個 topic 一次性訂閱，建議：
  - 用單條 SUBSCRIBE 命令拼接所有 topic（用 | 分隔），避免連發多條命令觸發 5 msg/s 限流
  - 大量 topic 切換時使用 UNSUBSCRIBE 釋放無關市場，控制頻寬
  - 同一連線全部 prediction 業務（使用者事件 + orderbook）只用一個 WSS 連線，不要每個 topic 獨立連
```

---