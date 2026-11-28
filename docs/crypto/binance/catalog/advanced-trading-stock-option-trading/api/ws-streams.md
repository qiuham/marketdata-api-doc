---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-stock-option-trading/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-28 18:47:09.685181
---

# Stock Option Trading WebSocket Streams

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-stock-option-trading/api/ws-streams/1.0.0/schema.yaml

WebSocket stream definitions for Binance Stock Option Trading. Base URL: wss://nbstream.binance.com/equity

Binance 股票期权交易的 WebSocket 流定义。基础 URL：wss://nbstream.binance.com/equity

版本: 1.0.0

## 服务地址

- `wss://nbstream.binance.com/equity`

## 接口列表

- `{listenKey}@orderReportV2` — Order Report V2 Stream

## Order Report V2 Stream（订单回报 V2 流）

流名称: `{listenKey}@orderReportV2`

Real-time push of the user's order updates. Option orders are pushed on `orderReportV2`, **not** on `orderReport`.

`orderReportV2` carries both US stock and US stock option orders; tell them apart with the `ac` field. To process option orders only, subscribe to `orderReportV2` and handle events where `ac` = `us_option`.

A push is sent once when an open order changes (`x` = `ORDER_UPDATE`) and once when it reaches a terminal state (`x` = `ORDER_TERMINAL`). Pushes are best-effort: a failed push is not retried, events while the `listenKey` is invalid are not replayed, and an order never pushed in an open state (e.g. rejected immediately) may not get a terminal push. After reconnecting, call Current Open Option Orders for a full snapshot first. Fill-level details are not pushed; use Option Order Detail or Option Trade History.

For expiration-day auto-liquidation orders by the broker (`o` = `market`), `p`, `b`, `q`, `tc`, `u`, `ct`, `sp` and `ed` may be `null`; get contract details from Option Exchange Info by `os`.

Prerequisite: obtain a `listenKey` via the Listen Key endpoint first.

实时推送用户的订单变化。期权订单推送在 `orderReportV2` 上，**不在** `orderReport` 上。

`orderReportV2` 同时推送美股与美股期权订单，按 `ac` 字段区分。只关心期权的调用方：订阅 `orderReportV2`，只处理 `ac` = `us_option` 的事件。

订单在 open 状态下发生变化时推送一次（`x` = `ORDER_UPDATE`），进入终态时推送一次（`x` = `ORDER_TERMINAL`）。推送是尽力而为：失败不重试；listenKey 失效期间的事件不会补推；从未以 open 状态推送过的订单（如直接被拒）可能不推终态。断线重连后请先调用「当前挂单」拉一次全量。推送不包含逐笔成交明细，需要时请用「订单详情」或「成交历史」查询。

到期日券商自动强平单（`o` = `market`）的 `p`、`b`、`q`、`tc`、`u`、`ct`、`sp`、`ed` 可能为 `null`，合约信息请按 `os` 调「合约交易规则」获取。

前提：先通过 Listen Key 接口获取 `listenKey`。

Operation ID: `orderReportV2Stream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| listenKey | path | string | 是 | User data listen key obtained from the Listen Key endpoint.<br>从 Listen Key 接口获取的用户数据 listenKey。<br>例: `3f9a1c2e-7b4d-4e8a-9c61-0d2f5b7e8a13` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | string | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "3f9a1c2e-7b4d-4e8a-9c61-0d2f5b7e8a13@orderReportV2"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Order Report V2 Stream / 订单回报 V2 流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"orderReportV2"`.<br>事件类型，固定为 `"orderReportV2"`。<br>例: `orderReportV2` |
| E | integer (int64) |  | Push time (ms).<br>推送时间（毫秒）。<br>例: `1792679109312` |
| x | string |  | `ORDER_UPDATE`: the order is open (new, accepted by the broker, partially filled, cancel pending, etc.). `ORDER_TERMINAL`: the order reached a terminal state and will not be pushed again.<br>`ORDER_UPDATE`：订单处于 open 状态（新建、被券商接受、部分成交、撤单处理中等）。`ORDER_TERMINAL`：订单进入终态，此后不会再推送该订单。<br>枚举: `ORDER_UPDATE`, `ORDER_TERMINAL`<br>例: `ORDER_UPDATE` |
| i | string |  | Order ID. REST field `orderId`.<br>订单 ID，对应 REST 字段 `orderId`。<br>例: `b0b6dd9d-8b9b-48a9-ba46-b9d54906e415` |
| ci | string |  | Client order ID. REST field `clientOrderId`.<br>客户端订单 ID，对应 REST 字段 `clientOrderId`。<br>例: `6a1f3c2e-90b4-4d7e-a1c5-2f8e7d6b5a40` |
| ai | string |  | Broker-side asset ID. Not needed by callers.<br>券商侧资产 ID，调用方无需使用。<br>例: `8d3f2a61-5c7e-4b90-9e1d-3a6c4f2b7e18` |
| b | string |  | Internal asset code (e.g. `EQ_SPCX`). Not needed by callers; read the underlying from `u`. May be `null` for expiration-day auto-liquidation orders.<br>内部资产代码（如 `EQ_SPCX`），调用方无需使用；标的请读 `u`。到期日券商自动强平单可能为 `null`。<br>例: `EQ_SPCX` |
| q | string |  | Quote asset; `USDC` for options. REST field `quoteAsset`. May be `null` for expiration-day auto-liquidation orders.<br>计价资产，期权为 `USDC`，对应 REST 字段 `quoteAsset`。到期日券商自动强平单可能为 `null`。<br>例: `USDC` |
| S | string |  | Side: `"buy"` / `"sell"`. Note: lowercase, unlike REST `side`.<br>方向：`"buy"` / `"sell"`。注意：为小写，REST 字段 `side` 为大写。<br>例: `buy` |
| o | string |  | Order type, lowercase: `"limit"` for user orders; `"market"` for expiration-day auto-liquidation orders by the broker. REST `orderType` is uppercase.<br>订单类型（小写）：用户下单恒为 `"limit"`；到期日券商自动强平单为 `"market"`。REST 字段 `orderType` 为大写。<br>例: `limit` |
| p | number |  | Limit price (premium per share). REST field `limitPrice`. May be `null` for expiration-day auto-liquidation orders.<br>每股权利金限价，对应 REST 字段 `limitPrice`。到期日券商自动强平单可能为 `null`。<br>例: `0.57` |
| Q | number |  | Order quantity (contracts). REST field `qty`.<br>委托张数，对应 REST 字段 `qty`。<br>例: `1` |
| N | number |  | Order notional. Always `null` for options.<br>委托名义金额，期权恒为 `null`。<br>例: `None` |
| fq | number |  | Cumulative filled quantity (contracts). REST field `filledQty`.<br>累计成交张数，对应 REST 字段 `filledQty`。<br>例: `0` |
| FN | number |  | Cumulative filled amount (USD) = average fill price × filled contracts × multiplier. REST field `filledNotional`.<br>累计成交金额（USD）= 成交均价 × 成交张数 × 乘数，对应 REST 字段 `filledNotional`。<br>例: `0` |
| tc | number |  | Amount locked from the wallet at placement: premium plus fees for buy to open and buy to close (covered call); for buy to close (cash-secured put), only the shortfall after the collateral is released (usually `0`); the collateral for sell to open (shares for a covered call, cash for a cash-secured put); `0` for sell to close. REST field `totalCost`. May be `null` for expiration-day auto-liquidation orders.<br>下单时从钱包锁定的金额：买入开仓、买入平仓 covered call 为权利金加手续费；买入平仓 cash-secured put 只锁释放抵押后仍不足的差额（通常为 `0`）；卖出开仓为抵押品（covered call 为正股股数，cash-secured put 为现金）；卖出平仓为 `0`。对应 REST 字段 `totalCost`。到期日券商自动强平单可能为 `null`。<br>例: `57.66` |
| Z | number |  | Fill progress percentage (0–100, 2 dp) = `fq` / `Q` × 100. REST field `filledPercent`.<br>成交进度百分比（0–100，2 位小数）= `fq` / `Q` × 100，对应 REST 字段 `filledPercent`。<br>例: `0` |
| n | string |  | Trading session; always `RTH` for options.<br>交易时段，期权恒为 `RTH`。<br>例: `RTH` |
| s | string |  | Order status, lowercase. With `ORDER_UPDATE`: `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace`. With `ORDER_TERMINAL`: `filled` / `canceled` / `expired` / `rejected` / `replaced`. REST field `status` is uppercase.<br>订单状态（小写）。`ORDER_UPDATE` 时为 `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace`；`ORDER_TERMINAL` 时为 `filled` / `canceled` / `expired` / `rejected` / `replaced`。REST 字段 `status` 为大写。<br>例: `accepted` |
| T | integer (int64) |  | Order creation time (ms). REST field `createdAt`.<br>订单创建时间（毫秒），对应 REST 字段 `createdAt`。<br>例: `1792679109000` |
| U | integer (int64) |  | Order last update time (ms). REST field `updatedAt`.<br>订单最近一次更新时间（毫秒），对应 REST 字段 `updatedAt`。<br>例: `1792679109000` |
| ac | string |  | Asset class: `us_option` (US stock options) / `us_equity` (US stocks).<br>资产类别：`us_option`（美股期权）/ `us_equity`（美股）。<br>枚举: `us_option`, `us_equity`<br>例: `us_option` |
| os | string |  | OCC contract symbol. REST field `symbol`.<br>OCC 合约代码，对应 REST 字段 `symbol`。<br>例: `SPCX261023C00005000` |
| u | string |  | Underlying US-equity ticker. REST field `underlyingSymbol`. May be `null` for expiration-day auto-liquidation orders.<br>标的美股 ticker，对应 REST 字段 `underlyingSymbol`。到期日券商自动强平单可能为 `null`。<br>例: `SPCX` |
| rs | string |  | OCC root; differs from `u` for contracts adjusted by a corporate action. REST field `rootSymbol`.<br>OCC root；公司行动调整后与 `u` 不同。对应 REST 字段 `rootSymbol`。<br>例: `SPCX` |
| ct | string |  | `CALL` / `PUT`. REST field `contractType`. May be `null` for expiration-day auto-liquidation orders.<br>`CALL` / `PUT`，对应 REST 字段 `contractType`。到期日券商自动强平单可能为 `null`。<br>例: `CALL` |
| sp | number |  | Strike price. REST field `strikePrice`. May be `null` for expiration-day auto-liquidation orders.<br>行权价，对应 REST 字段 `strikePrice`。到期日券商自动强平单可能为 `null`。<br>例: `5` |
| ed | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day, same as REST `expirationDate`. May be `null` for expiration-day auto-liquidation orders.<br>到期日当天 12:00 ET 的毫秒时间戳，与 REST 字段 `expirationDate` 口径一致。到期日券商自动强平单可能为 `null`。<br>例: `1792771200000` |
| m | number |  | Contract multiplier. REST field `multiplier`.<br>合约乘数，对应 REST 字段 `multiplier`。<br>例: `100` |
| pi | string |  | Position intent, lowercase: `buy_to_open` / `sell_to_close` / `sell_to_open` / `buy_to_close`. REST field `positionIntent` is uppercase.<br>持仓意图（小写）：`buy_to_open` / `sell_to_close` / `sell_to_open` / `buy_to_close`。REST 字段 `positionIntent` 为大写。<br>例: `buy_to_open` |

```json
{
  "e": "orderReportV2",
  "E": 1792679109312,
  "x": "ORDER_UPDATE",
  "i": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "ci": "6a1f3c2e-90b4-4d7e-a1c5-2f8e7d6b5a40",
  "ai": "8d3f2a61-5c7e-4b90-9e1d-3a6c4f2b7e18",
  "b": "EQ_SPCX",
  "q": "USDC",
  "S": "buy",
  "o": "limit",
  "p": 0.57,
  "Q": 1,
  "N": null,
  "fq": 0,
  "FN": 0,
  "tc": 57.66,
  "Z": 0,
  "n": "RTH",
  "s": "accepted",
  "T": 1792679109000,
  "U": 1792679109000,
  "ac": "us_option",
  "os": "SPCX261023C00005000",
  "u": "SPCX",
  "rs": "SPCX",
  "ct": "CALL",
  "sp": 5,
  "ed": 1792771200000,
  "m": 100,
  "pi": "buy_to_open"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `3f9a1c2e-7b4d-4e8a-9c61-0d2f5b7e8a13@orderReportV2` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"orderReportV2"`.<br>事件类型，固定为 `"orderReportV2"`。<br>例: `orderReportV2` |
| data.E | integer (int64) |  | Push time (ms).<br>推送时间（毫秒）。<br>例: `1792679109312` |
| data.x | string |  | `ORDER_UPDATE`: the order is open (new, accepted by the broker, partially filled, cancel pending, etc.). `ORDER_TERMINAL`: the order reached a terminal state and will not be pushed again.<br>`ORDER_UPDATE`：订单处于 open 状态（新建、被券商接受、部分成交、撤单处理中等）。`ORDER_TERMINAL`：订单进入终态，此后不会再推送该订单。<br>枚举: `ORDER_UPDATE`, `ORDER_TERMINAL`<br>例: `ORDER_UPDATE` |
| data.i | string |  | Order ID. REST field `orderId`.<br>订单 ID，对应 REST 字段 `orderId`。<br>例: `b0b6dd9d-8b9b-48a9-ba46-b9d54906e415` |
| data.ci | string |  | Client order ID. REST field `clientOrderId`.<br>客户端订单 ID，对应 REST 字段 `clientOrderId`。<br>例: `6a1f3c2e-90b4-4d7e-a1c5-2f8e7d6b5a40` |
| data.ai | string |  | Broker-side asset ID. Not needed by callers.<br>券商侧资产 ID，调用方无需使用。<br>例: `8d3f2a61-5c7e-4b90-9e1d-3a6c4f2b7e18` |
| data.b | string |  | Internal asset code (e.g. `EQ_SPCX`). Not needed by callers; read the underlying from `u`. May be `null` for expiration-day auto-liquidation orders.<br>内部资产代码（如 `EQ_SPCX`），调用方无需使用；标的请读 `u`。到期日券商自动强平单可能为 `null`。<br>例: `EQ_SPCX` |
| data.q | string |  | Quote asset; `USDC` for options. REST field `quoteAsset`. May be `null` for expiration-day auto-liquidation orders.<br>计价资产，期权为 `USDC`，对应 REST 字段 `quoteAsset`。到期日券商自动强平单可能为 `null`。<br>例: `USDC` |
| data.S | string |  | Side: `"buy"` / `"sell"`. Note: lowercase, unlike REST `side`.<br>方向：`"buy"` / `"sell"`。注意：为小写，REST 字段 `side` 为大写。<br>例: `buy` |
| data.o | string |  | Order type, lowercase: `"limit"` for user orders; `"market"` for expiration-day auto-liquidation orders by the broker. REST `orderType` is uppercase.<br>订单类型（小写）：用户下单恒为 `"limit"`；到期日券商自动强平单为 `"market"`。REST 字段 `orderType` 为大写。<br>例: `limit` |
| data.p | number |  | Limit price (premium per share). REST field `limitPrice`. May be `null` for expiration-day auto-liquidation orders.<br>每股权利金限价，对应 REST 字段 `limitPrice`。到期日券商自动强平单可能为 `null`。<br>例: `0.57` |
| data.Q | number |  | Order quantity (contracts). REST field `qty`.<br>委托张数，对应 REST 字段 `qty`。<br>例: `1` |
| data.N | number |  | Order notional. Always `null` for options.<br>委托名义金额，期权恒为 `null`。<br>例: `None` |
| data.fq | number |  | Cumulative filled quantity (contracts). REST field `filledQty`.<br>累计成交张数，对应 REST 字段 `filledQty`。<br>例: `0` |
| data.FN | number |  | Cumulative filled amount (USD) = average fill price × filled contracts × multiplier. REST field `filledNotional`.<br>累计成交金额（USD）= 成交均价 × 成交张数 × 乘数，对应 REST 字段 `filledNotional`。<br>例: `0` |
| data.tc | number |  | Amount locked from the wallet at placement: premium plus fees for buy to open and buy to close (covered call); for buy to close (cash-secured put), only the shortfall after the collateral is released (usually `0`); the collateral for sell to open (shares for a covered call, cash for a cash-secured put); `0` for sell to close. REST field `totalCost`. May be `null` for expiration-day auto-liquidation orders.<br>下单时从钱包锁定的金额：买入开仓、买入平仓 covered call 为权利金加手续费；买入平仓 cash-secured put 只锁释放抵押后仍不足的差额（通常为 `0`）；卖出开仓为抵押品（covered call 为正股股数，cash-secured put 为现金）；卖出平仓为 `0`。对应 REST 字段 `totalCost`。到期日券商自动强平单可能为 `null`。<br>例: `57.66` |
| data.Z | number |  | Fill progress percentage (0–100, 2 dp) = `fq` / `Q` × 100. REST field `filledPercent`.<br>成交进度百分比（0–100，2 位小数）= `fq` / `Q` × 100，对应 REST 字段 `filledPercent`。<br>例: `0` |
| data.n | string |  | Trading session; always `RTH` for options.<br>交易时段，期权恒为 `RTH`。<br>例: `RTH` |
| data.s | string |  | Order status, lowercase. With `ORDER_UPDATE`: `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace`. With `ORDER_TERMINAL`: `filled` / `canceled` / `expired` / `rejected` / `replaced`. REST field `status` is uppercase.<br>订单状态（小写）。`ORDER_UPDATE` 时为 `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace`；`ORDER_TERMINAL` 时为 `filled` / `canceled` / `expired` / `rejected` / `replaced`。REST 字段 `status` 为大写。<br>例: `accepted` |
| data.T | integer (int64) |  | Order creation time (ms). REST field `createdAt`.<br>订单创建时间（毫秒），对应 REST 字段 `createdAt`。<br>例: `1792679109000` |
| data.U | integer (int64) |  | Order last update time (ms). REST field `updatedAt`.<br>订单最近一次更新时间（毫秒），对应 REST 字段 `updatedAt`。<br>例: `1792679109000` |
| data.ac | string |  | Asset class: `us_option` (US stock options) / `us_equity` (US stocks).<br>资产类别：`us_option`（美股期权）/ `us_equity`（美股）。<br>枚举: `us_option`, `us_equity`<br>例: `us_option` |
| data.os | string |  | OCC contract symbol. REST field `symbol`.<br>OCC 合约代码，对应 REST 字段 `symbol`。<br>例: `SPCX261023C00005000` |
| data.u | string |  | Underlying US-equity ticker. REST field `underlyingSymbol`. May be `null` for expiration-day auto-liquidation orders.<br>标的美股 ticker，对应 REST 字段 `underlyingSymbol`。到期日券商自动强平单可能为 `null`。<br>例: `SPCX` |
| data.rs | string |  | OCC root; differs from `u` for contracts adjusted by a corporate action. REST field `rootSymbol`.<br>OCC root；公司行动调整后与 `u` 不同。对应 REST 字段 `rootSymbol`。<br>例: `SPCX` |
| data.ct | string |  | `CALL` / `PUT`. REST field `contractType`. May be `null` for expiration-day auto-liquidation orders.<br>`CALL` / `PUT`，对应 REST 字段 `contractType`。到期日券商自动强平单可能为 `null`。<br>例: `CALL` |
| data.sp | number |  | Strike price. REST field `strikePrice`. May be `null` for expiration-day auto-liquidation orders.<br>行权价，对应 REST 字段 `strikePrice`。到期日券商自动强平单可能为 `null`。<br>例: `5` |
| data.ed | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day, same as REST `expirationDate`. May be `null` for expiration-day auto-liquidation orders.<br>到期日当天 12:00 ET 的毫秒时间戳，与 REST 字段 `expirationDate` 口径一致。到期日券商自动强平单可能为 `null`。<br>例: `1792771200000` |
| data.m | number |  | Contract multiplier. REST field `multiplier`.<br>合约乘数，对应 REST 字段 `multiplier`。<br>例: `100` |
| data.pi | string |  | Position intent, lowercase: `buy_to_open` / `sell_to_close` / `sell_to_open` / `buy_to_close`. REST field `positionIntent` is uppercase.<br>持仓意图（小写）：`buy_to_open` / `sell_to_close` / `sell_to_open` / `buy_to_close`。REST 字段 `positionIntent` 为大写。<br>例: `buy_to_open` |

```json
{
  "stream": "3f9a1c2e-7b4d-4e8a-9c61-0d2f5b7e8a13@orderReportV2",
  "data": {
    "e": "orderReportV2",
    "E": 1792679109312,
    "x": "ORDER_UPDATE",
    "i": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
    "ci": "6a1f3c2e-90b4-4d7e-a1c5-2f8e7d6b5a40",
    "ai": "8d3f2a61-5c7e-4b90-9e1d-3a6c4f2b7e18",
    "b": "EQ_SPCX",
    "q": "USDC",
    "S": "buy",
    "o": "limit",
    "p": 0.57,
    "Q": 1,
    "N": null,
    "fq": 0,
    "FN": 0,
    "tc": 57.66,
    "Z": 0,
    "n": "RTH",
    "s": "accepted",
    "T": 1792679109000,
    "U": 1792679109000,
    "ac": "us_option",
    "os": "SPCX261023C00005000",
    "u": "SPCX",
    "rs": "SPCX",
    "ct": "CALL",
    "sp": 5,
    "ed": 1792771200000,
    "m": 100,
    "pi": "buy_to_open"
  }
}
```