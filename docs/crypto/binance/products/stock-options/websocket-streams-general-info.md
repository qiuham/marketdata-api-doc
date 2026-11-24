---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stock-options/websocket-streams-general-info
api_type: WebSocket
updated_at: 2026-11-24 18:28:44.055134
---

# WebSocket Streams — General Info

Option order updates are pushed over the stock user data stream. Option orders are pushed on
`<listenKey>@orderReportV2`, **not** on `<listenKey>@orderReport`.

## Base URL

| Environment | Base URL                            |
| ----------- | ----------------------------------- |
| Production  | `wss://nbstream.binance.com/equity` |

## Listen Key

Obtain a `listenKey` via
[Create / Renew Listen Key](/catalog/advanced-trading-stock-option-trading/api/rest-api/user-data-streams).

- Valid for 1 hour. Calling the endpoint again renews it and returns the same key; renewing every 30
  minutes is recommended. After expiry a new key is issued and you must resubscribe with it.
- Options and stocks share one key. `/sapi/v1/equity/option/listenKey` and
  `/sapi/v1/equity/listenKey` return the same key.

## Connecting

| Mode            | URL                                                                          |
| --------------- | ---------------------------------------------------------------------------- |
| Single stream   | `wss://nbstream.binance.com/equity/ws/<listenKey>@orderReportV2`             |
| Combined stream | `wss://nbstream.binance.com/equity/stream?streams=<listenKey>@orderReportV2` |

You can also connect to `wss://nbstream.binance.com/equity/stream` and then subscribe:

> **Request**

```json
{ "method": "SUBSCRIBE", "params": ["<listenKey>@orderReportV2"], "id": 1 }
```

> **Response**

```json
{ "result": null, "id": 1 }
```

On a single stream, each message is the event itself. On a combined stream, the event is wrapped as
`{"stream": "<listenKey>@orderReportV2", "data": {...}}`.

## Choosing a Stream

| Stream                      | Content                                                |
| --------------------------- | ------------------------------------------------------ |
| `<listenKey>@orderReportV2` | US stocks and **US stock options**, told apart by `ac` |
| `<listenKey>@orderReport`   | US stocks only, **no options**, and no `ac` field      |

To process option orders only, subscribe to `orderReportV2` and handle events where `ac` =
`us_option`.

| `ac`        | Asset class      |
| ----------- | ---------------- |
| `us_option` | US stock options |
| `us_equity` | US stocks        |

## When Events Are Pushed

| `x`              | When                                                                                    | Possible `s`                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `ORDER_UPDATE`   | The order is open (new, accepted by the broker, partially filled, cancel pending, etc.) | `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace` |
| `ORDER_TERMINAL` | The order reached a terminal state; it will not be pushed again                         | `filled` / `canceled` / `expired` / `rejected` / `replaced`                                    |

- **Pushes are best-effort and not guaranteed**: a failed push is not retried; the terminal state of
  an order is pushed only once; events during a period when the `listenKey` is invalid are not
  replayed; an order never pushed in an open state (e.g. rejected immediately) may not get a
  terminal push. After reconnecting, call Current Open Option Orders for a full snapshot, then apply
  pushes as increments.
- Nothing is pushed when nothing changes (e.g. for queries).
- Fill-level details (price of each fill) are not pushed; use Option Order Detail or Option Trade
  History.

## Example (`ac` = `us_option`)

A buy-to-open limit order accepted by the broker:

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

When the same order is canceled, `x` = `ORDER_TERMINAL` and `s` = `canceled`; other fields keep the
same meaning. See
[Order Report V2 Stream](/catalog/advanced-trading-stock-option-trading/api/ws-streams/user-streams)
for every field.

## Differences from REST

The stream is shared with the Binance App, and its format takes precedence:

- **Keys are abbreviated.** The field reference maps each key to its REST field.
- **Enum values are lowercase** (`buy`, `limit`, `accepted`, `buy_to_open`); REST uses uppercase.
  Compare case-insensitively.
- **Numbers are JSON numbers**, not strings, with a variable number of decimals (trailing zeros
  possible). Parse them with a decimal type; do not compare them as floating point.
- **Empty fields are kept as `null`**, not omitted. Stock and option events have the same set of
  keys; fields that do not apply are pushed as `null`.
- **Expiration-day auto-liquidation orders by the broker** (`o` = `market`) may have `null` in `p`,
  `b`, `q`, `tc`, `u`, `ct`, `sp` and `ed`; get the contract details by calling Option Exchange Info
  with `os`.

## Connection Lifecycle

If the `listenKey` expires, the stream stops pushing. Renew it before its 1-hour validity ends, and
after reconnecting, call Current Open Option Orders for a full snapshot before applying pushes.

---

# WebSocket 流基本信息

期权订单更新通过美股用户数据流推送。期权订单推送在 `<listenKey>@orderReportV2` 上，**不在**
`<listenKey>@orderReport` 上。

## Base URL

| 环境     | Base URL                            |
| -------- | ----------------------------------- |
| 生产环境 | `wss://nbstream.binance.com/equity` |

## Listen Key

通过[创建 / 续期 Listen Key](/catalog/advanced-trading-stock-option-trading/api/rest-api/user-data-streams)
获取 `listenKey`。

- 有效期 1 小时。重复调用即续期并返回同一个 key，建议每 30 分钟调用一次。过期后再调用会签发新 key，需用新 key 重新订阅。
- 期权与美股共用同一个 key。`/sapi/v1/equity/option/listenKey` 与 `/sapi/v1/equity/listenKey`
  返回的是同一个 key。

## 连接方式

| 方式   | 地址                                                                         |
| ------ | ---------------------------------------------------------------------------- |
| 单流   | `wss://nbstream.binance.com/equity/ws/<listenKey>@orderReportV2`             |
| 组合流 | `wss://nbstream.binance.com/equity/stream?streams=<listenKey>@orderReportV2` |

也可以先连 `wss://nbstream.binance.com/equity/stream`，再发送订阅消息：

> **请求**

```json
{ "method": "SUBSCRIBE", "params": ["<listenKey>@orderReportV2"], "id": 1 }
```

> **响应**

```json
{ "result": null, "id": 1 }
```

单流模式下收到的消息即事件本身；组合流模式下外层包一层
`{"stream": "<listenKey>@orderReportV2", "data": {...}}`。

## 选哪条流

| 流名                        | 内容                                   |
| --------------------------- | -------------------------------------- |
| `<listenKey>@orderReportV2` | 美股、**美股期权**，按 `ac` 字段区分   |
| `<listenKey>@orderReport`   | 仅美股，**不含期权**，也没有 `ac` 字段 |

只关心期权的调用方：订阅 `orderReportV2`，只处理 `ac` = `us_option` 的事件。

| `ac`        | 资产类别 |
| ----------- | -------- |
| `us_option` | 美股期权 |
| `us_equity` | 美股     |

## 推送时机

| `x`              | 时机                                                           | `s` 可能的取值                                                                                 |
| ---------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `ORDER_UPDATE`   | 订单处于 open 状态（新建、被券商接受、部分成交、撤单处理中等） | `new` / `pending_new` / `accepted` / `partially_filled` / `pending_cancel` / `pending_replace` |
| `ORDER_TERMINAL` | 订单进入终态，此后不会再推送该订单                             | `filled` / `canceled` / `expired` / `rejected` / `replaced`                                    |

- **推送是尽力而为，不保证送达**：推送失败不重试；同一订单的终态只推一次；listenKey 失效期间的事件不会补推；从未以 open 状态推送过的订单（如直接被拒）可能不推终态。断线重连后请先调「当前挂单」拉一次全量，再用推送做增量更新。
- 不发生上述变化（如只是查询）不会推送。
- 推送不包含成交明细（每笔成交价）；需要时用「订单详情」或「成交历史」查询。

## 推送示例（`ac` = `us_option`）

买入开仓限价单被券商接受：

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

同一笔订单被撤销（终态）时，`x` = `ORDER_TERMINAL`、`s` = `canceled`，其余字段含义不变。全部字段见
[订单回报 V2 流](/catalog/advanced-trading-stock-option-trading/api/ws-streams/user-streams)。

## 与 REST 的格式差异

推送流与 Binance App 共用，格式以推送流为准：

- **键名为缩写**，字段说明中给出了每个键对应的 REST 字段。
- **枚举值为小写**（`buy`、`limit`、`accepted`、`buy_to_open`），REST 为大写。比较时请忽略大小写。
- **数值为 JSON
  number**，不是字符串，小数位数不固定（可能带末尾 0）。请用十进制类型解析，不要转成浮点数后比较。
- **空值字段保留为 `null`**，不会省略。美股与期权事件的键集合完全相同，不适用的字段推 `null`。
- **到期日券商自动强平单**（`o` = `market`）的 `p`、`b`、`q`、`tc`、`u`、`ct`、`sp`、`ed` 可能为
  `null`，合约信息请按 `os` 调「合约交易规则」获取。

## 连接生命周期

`listenKey`
过期后推送会停止，请在 1 小时有效期结束前续期。断线重连后，请先调「当前挂单」拉一次全量，再用推送做增量更新。