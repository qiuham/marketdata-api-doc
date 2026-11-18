---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/w3w-prediction/websocket-streams/integration-guide
api_type: WebSocket
updated_at: 2026-11-18 02:13:15.522015
---

# Prediction Market — WebSocket Streams (Integration Guide)

## 1. Field Format Specification

### 1.1 `amount` (Money)

```
Rule: truncate to 2 decimal places (DOWN mode, towards zero)

Examples:
  2.5678 → "2.56"
  0.009  → "<0.01"      ← Unified display for amounts < 0.01
  null   → "<0.01"
  100    → "100.00"
```

**Integration tips**:

- Render the `amount` field directly to the user
- For precise numerical computation, fetch via REST API — do NOT reverse-parse this field

### 1.2 `topic` (Market Title)

```
Rule: if longer than 12 chars, truncate and append ".." (max 14 chars total)

Examples:
  "BTC will hit 100K"  → "BTC will hi.."
  "Short title"        → "Short title"
  null                 → ""
```

### 1.3 `outcome` (Outcome Name)

```
Rule: passed through as-is, not truncated

Possible values:
  "Yes" / "No"           (binary markets)
  "Trump" / "Biden" / …  (multi-outcome markets)
  ""                     (when data is missing)
```

### 1.4 `pushId` (Idempotency Key)

Format: see
[Wallet Events WebSocket Streams](https://developers.binance.com/en/docs/products/w3w-prediction/websocket-streams/wallet-events)
Section 3.3. **Present in every topic**, **strongly recommended for client-side deduplication**.

---

## 2. End-to-End Integration Example

### 2.1 Full Flow

```
1. Acquire API Key + Secret Key under user's logged-in session via REST API
2. Prepare timestamp + random
3. Sort all URL parameters alphabetically and concatenate
4. Compute signature with HMAC SHA256
5. Build the full WSS URL
6. Open WebSocket connection with header X-MBX-APIKEY
7. on('open')        → connection established; send SUBSCRIBE if not in URL
8. on('message')     → parse the message (outer JSON, then inner JSON)
9. on('close')       → trigger reconnect logic (regenerate timestamp + signature)
10. setInterval 30s  → send empty PING frame
```

### 2.2 Node.js Sample

```javascript
const WebSocket = require("ws");
const crypto = require("crypto");

const API_KEY = process.env.BINANCE_API_KEY;
const SECRET_KEY = process.env.BINANCE_SECRET_KEY;
const BASE_URL = "wss://api.binance.com/sapi/wss";

// All prediction topics to subscribe
const TOPICS = ["web3_prediction_pm_market_buy_success", "web3_prediction_pm_market_buy_fail", "web3_prediction_pm_market_sell_success", "web3_prediction_pm_market_sell_fail", "web3_prediction_pm_limit_submit_success", "web3_prediction_pm_limit_submit_fail", "web3_prediction_pm_limit_order_filled", "web3_prediction_pm_limit_order_partial_fill", "web3_prediction_pm_claim_success", "web3_prediction_pm_claim_fail", "web3_prediction_pm_claim_partial_success", "web3_prediction_pm_transfer_success", "web3_prediction_pm_transfer_fail", "web3_prediction_pm_market_close"];

function buildConnectionUrl() {
  const params = {
    random: crypto.randomBytes(16).toString("hex"),
    topic: TOPICS.join("|"),
    recvWindow: "30000",
    timestamp: Date.now().toString(),
  };
  const sortedKeys = Object.keys(params).sort();
  const payload = sortedKeys.map((k) => `${k}=${params[k]}`).join("&");
  const signature = crypto.createHmac("sha256", SECRET_KEY).update(payload).digest("hex");
  return `${BASE_URL}?${payload}&signature=${signature}`;
}

const seenPushIds = new Set(); // For production, replace with a proper LRU cache

function connect() {
  const url = buildConnectionUrl();
  const ws = new WebSocket(url, [], {
    headers: { "X-MBX-APIKEY": API_KEY },
  });

  ws.on("open", () => {
    console.log("[ws] connected");
    // Heartbeat
    setInterval(() => {
      if (ws.readyState === WebSocket.OPEN) ws.ping();
    }, 30_000);
  });

  ws.on("message", (raw) => {
    const envelope = JSON.parse(raw.toString());

    // Command response
    if (envelope.type === "COMMAND") {
      console.log("[ws] command response:", envelope);
      return;
    }

    // Business push
    if (envelope.type === "DATA") {
      const payload = JSON.parse(envelope.data); // ⚠️ data is a stringified JSON
      handlePredictionPush(envelope.topic, payload);
    }
  });

  ws.on("close", (code, reason) => {
    console.warn("[ws] closed", code, reason.toString());
    setTimeout(connect, 3_000); // Simple reconnect; use exponential backoff in production
  });

  ws.on("error", (err) => {
    console.error("[ws] error", err);
  });

  return ws;
}

function handlePredictionPush(topic, payload) {
  // 1. Idempotency
  if (seenPushIds.has(payload.pushId)) return;
  seenPushIds.add(payload.pushId);

  // 2. Extract scenarioCode (strip topic prefix)
  const scenarioCode = topic.replace("web3_prediction_", "");

  // 3. Field fallbacks
  const amount = payload.amount ?? "<0.01";
  const marketTopic = payload.topic ?? "the market";
  const outcome = payload.outcome ?? "";

  // 4. Dispatch by scenario
  switch (scenarioCode) {
    case "pm_market_buy_success":
      console.log(`Bought ${amount} USDT in ${marketTopic}`);
      break;
    case "pm_claim_success":
      console.log(`Successfully claimed ${amount} USDT.`);
      break;
    case "pm_claim_fail":
      console.log(`Failed to claim ${amount} from ${outcome}.`);
      break;
    case "pm_market_close":
      console.log(`Market ${marketTopic} resolved.`);
      break;
    // ... other 11 scenarios
    default:
      console.log(`[unknown scenario] ${scenarioCode}`, payload);
  }
}

connect();
```

### 2.3 End-to-End Business Example: Limit BUY Flow

```
T+0s   User submits a limit order
       ←  Topic: pm_limit_submit_success
       ←  data: {"pushId":"pm_O1_pm_limit_submit_success_xx","amount":"100.00","topic":"BTC will hi.."}

T+30s  Partial liquidity matched
       ←  Topic: pm_limit_order_partial_fill
       ←  data: {"pushId":"pm_O1_pm_limit_order_partial_fill_yy","amount":"30.00","topic":"BTC will hi.."}

T+5min Fully filled
       ←  Topic: pm_limit_order_filled
       ←  data: {"pushId":"pm_O1_pm_limit_order_filled_zz","amount":"100.00","topic":"BTC will hi.."}
```

---

---

# Prediction Market — WebSocket 數據流（接入指南）

## 1. 欄位格式規範

### 1.1 `amount`（金額）

```
規則：擷取到小數點後 2 位（DOWN 模式，向 0 截斷）

示例：
  2.5678 → "2.56"
  0.009  → "<0.01"      ← 小於 0.01 的統一展示
  null   → "<0.01"
  100    → "100.00"
```

**接入建議**：

- 直接用 `amount` 欄位渲染給使用者
- 如需精確數值計算，請通過業務後端 REST API 獲取，不要反向解析此欄位

### 1.2 `topic`（市場標題）

```
規則：超過 12 字元則截斷後追加 ".."（共最長 14 字元）

示例：
  "BTC will hit 100K"  → "BTC will hi.."
  "Short title"        → "Short title"
  null                 → ""
```

### 1.3 `outcome`（結果名稱）

```
規則：原樣透傳，未截斷

可能值：
  "Yes" / "No"（二元市場）
  "Trump" / "Biden" / 其他（多元市場）
  ""（資料缺失時）
```

### 1.4 `pushId`（冪等鍵）

格式見
[Wallet Events WebSocket 數據流](https://developers.binance.com/zh-CN/docs/products/w3w-prediction/websocket-streams/wallet-events)
第 3.3 節。**所有 topic 必有**，**強烈建議客戶端用此欄位做去重**。

---

## 2. 接入完整流程示例

### 2.1 完整流程

```
1. 通過 REST API 在使用者登入態獲取 API Key + Secret Key
2. 準備 timestamp + random
3. 拼接所有 URL 參數（按字母序）
4. HMAC SHA256 計算 signature
5. 構造完整 WSS URL
6. WebSocket 連線，Header 加 X-MBX-APIKEY
7. on('open')        → 連線成功，可傳送 SUBSCRIBE 命令（如未在 URL 中訂閱）
8. on('message')     → 解析訊息（先 outer JSON, 再 inner JSON）
9. on('close')       → 觸發重連邏輯（重新生成 timestamp + signature）
10. setInterval 30s  → 傳送空 PING
```

### 2.2 Node.js 示例

```javascript
const WebSocket = require("ws");
const crypto = require("crypto");

const API_KEY = process.env.BINANCE_API_KEY;
const SECRET_KEY = process.env.BINANCE_SECRET_KEY;
const BASE_URL = "wss://api.binance.com/sapi/wss";

// 訂閱的所有 prediction topics
const TOPICS = ["web3_prediction_pm_market_buy_success", "web3_prediction_pm_market_buy_fail", "web3_prediction_pm_market_sell_success", "web3_prediction_pm_market_sell_fail", "web3_prediction_pm_limit_submit_success", "web3_prediction_pm_limit_submit_fail", "web3_prediction_pm_limit_order_filled", "web3_prediction_pm_limit_order_partial_fill", "web3_prediction_pm_claim_success", "web3_prediction_pm_claim_fail", "web3_prediction_pm_claim_partial_success", "web3_prediction_pm_transfer_success", "web3_prediction_pm_transfer_fail", "web3_prediction_pm_market_close"];

function buildConnectionUrl() {
  const params = {
    random: crypto.randomBytes(16).toString("hex"),
    topic: TOPICS.join("|"),
    recvWindow: "30000",
    timestamp: Date.now().toString(),
  };
  const sortedKeys = Object.keys(params).sort();
  const payload = sortedKeys.map((k) => `${k}=${params[k]}`).join("&");
  const signature = crypto.createHmac("sha256", SECRET_KEY).update(payload).digest("hex");
  return `${BASE_URL}?${payload}&signature=${signature}`;
}

const seenPushIds = new Set(); // 簡單 LRU 推薦生產替換

function connect() {
  const url = buildConnectionUrl();
  const ws = new WebSocket(url, [], {
    headers: { "X-MBX-APIKEY": API_KEY },
  });

  ws.on("open", () => {
    console.log("[ws] connected");
    // 心跳
    setInterval(() => {
      if (ws.readyState === WebSocket.OPEN) ws.ping();
    }, 30_000);
  });

  ws.on("message", (raw) => {
    const envelope = JSON.parse(raw.toString());

    // 命令響應
    if (envelope.type === "COMMAND") {
      console.log("[ws] command response:", envelope);
      return;
    }

    // 業務推送
    if (envelope.type === "DATA") {
      const payload = JSON.parse(envelope.data); // ⚠️ data 是字串化 JSON
      handlePredictionPush(envelope.topic, payload);
    }
  });

  ws.on("close", (code, reason) => {
    console.warn("[ws] closed", code, reason.toString());
    setTimeout(connect, 3_000); // 簡單重連，生產建議指數退避
  });

  ws.on("error", (err) => {
    console.error("[ws] error", err);
  });

  return ws;
}

function handlePredictionPush(topic, payload) {
  // 1. 冪等去重
  if (seenPushIds.has(payload.pushId)) return;
  seenPushIds.add(payload.pushId);

  // 2. 提取 scenarioCode（topic 去字首）
  const scenarioCode = topic.replace("web3_prediction_", "");

  // 3. 欄位兜底
  const amount = payload.amount ?? "<0.01";
  const marketTopic = payload.topic ?? "the market";
  const outcome = payload.outcome ?? "";

  // 4. 按場景分發
  switch (scenarioCode) {
    case "pm_market_buy_success":
      console.log(`Bought ${amount} USDT in ${marketTopic}`);
      break;
    case "pm_claim_success":
      console.log(`Successfully claimed ${amount} USDT.`);
      break;
    case "pm_claim_fail":
      console.log(`Failed to claim ${amount} from ${outcome}.`);
      break;
    case "pm_market_close":
      console.log(`Market ${marketTopic} resolved.`);
      break;
    // ... 其他 11 個場景
    default:
      console.log(`[unknown scenario] ${scenarioCode}`, payload);
  }
}

connect();
```

### 2.3 端到端業務示例：限價 BUY 全流程

```
T+0s   使用者提交限價單
       ←  Topic: pm_limit_submit_success
       ←  data: {"pushId":"pm_O1_pm_limit_submit_success_xx","amount":"100.00","topic":"BTC will hi.."}

T+30s  撮合到部分流動性
       ←  Topic: pm_limit_order_partial_fill
       ←  data: {"pushId":"pm_O1_pm_limit_order_partial_fill_yy","amount":"30.00","topic":"BTC will hi.."}

T+5min 完全成交
       ←  Topic: pm_limit_order_filled
       ←  data: {"pushId":"pm_O1_pm_limit_order_filled_zz","amount":"100.00","topic":"BTC will hi.."}
```

---