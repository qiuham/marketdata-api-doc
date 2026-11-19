---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info
api_type: WebSocket
updated_at: 2026-11-19 18:30:09.536317
---

# WebSocket Streams — General Info

The Stocks Trading module ships real-time market and user data over WebSocket. All streams are
one-way push (server → client). A stream can be reached either by encoding its name in the URL path
(below), or via a subscribe/unsubscribe RPC over a bare `/ws` connection (see
[Subscribing via RPC](#subscribing-via-rpc)).

## Base URL

| Environment | Base URL                            |
| ----------- | ----------------------------------- |
| Production  | `wss://nbstream.binance.com/equity` |

The production base URL shares the standard Binance stream domain. Use the `/ws/<streamName>` and
`/stream?streams=<A>/<B>/<C>` suffixes described below.

## Single Stream

Connect to a single stream by appending the stream name to `/ws/`:

```
wss://nbstream.binance.com/equity/ws/AAPL@quote
```

The server pushes raw event payloads directly — no stream-name wrapper:

```javascript
{ "e": "quote", "E": 1710320400000, "s": "AAPL", "bp": "182.50", "ap": "182.55", "bs": 100, "as": 200, "T": 1710320399500 }
```

## Combined Stream

Connect to multiple streams on a single socket by joining them with `/` under `/stream?streams=`:

```
wss://nbstream.binance.com/equity/stream?streams=AAPL@quote/NVDA@quote/price
```

Each event is wrapped in an envelope that tells you which stream it came from:

```javascript
{
  "stream": "AAPL@quote",
  "data":   { "e": "quote", "E": 1710320400000, "s": "AAPL", "bp": "182.50", "ap": "182.55", "bs": 100, "as": 200, "T": 1710320399500 }
}
```

## Subscribing via RPC

A bare connection to `/ws` (no stream name in the path) also accepts the standard
subscribe/unsubscribe RPC used across other WebSocket products. Send a JSON request with a unique
`id`; the server echoes it back in the response.

```
wss://nbstream.binance.com/equity/ws
```

> **Request**

```json
{ "method": "SUBSCRIBE", "params": ["AAPL@quote"], "id": 1 }
```

> **Response**

```json
{ "result": null, "id": 1 }
```

The connection then pushes raw event payloads for the subscribed stream(s), the same as a
`/ws/<streamName>` connection. `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, and
`GET_PROPERTY` are recognized as well.

## Stream Name Rules

| Stream                        | Format                      | Casing              | Example                                    |
| ----------------------------- | --------------------------- | ------------------- | ------------------------------------------ |
| Price (all symbols)           | `price`                     | lowercase fixed     | `price`                                    |
| Quote (per symbol)            | `{SYMBOL}@quote`            | SYMBOL UPPERCASE    | `AAPL@quote`                               |
| Kline (per symbol + interval) | `{SYMBOL}@kline_{interval}` | SYMBOL UPPERCASE    | `AAPL@kline_5m`                            |
| Market calendar               | `calendar`                  | lowercase fixed     | `calendar`                                 |
| Trading status (per symbol)   | `{SYMBOL}@tradingStatus`    | SYMBOL UPPERCASE    | `AAPL@tradingStatus`                       |
| Tradability (per symbol)      | `{SYMBOL}@tradability`      | SYMBOL UPPERCASE    | `AAPL@tradability`                         |
| Order report (per user)       | `{listenKey}@orderReport`   | listenKey as issued | `pqia91ma19a5s61cv6a81va65...@orderReport` |

SYMBOL is always the bare US-equity ticker in UPPERCASE (`AAPL`, `NVDA`, `SPY`), matching the
[module-level symbol format](./general-info.md#symbol-format).

## Kline Intervals

| Interval  | Stream suffix |
| --------- | ------------- |
| 5 minutes | `kline_5m`    |
| 1 hour    | `kline_1h`    |
| 1 day     | `kline_1d`    |
| 1 week    | `kline_1w`    |
| 1 month   | `kline_1M`    |

`1Min` is not published over WebSocket.

## Event Type Field

Every payload carries an `e` field identifying the event. Callers fan out by `e`:

| `e` value       | Document                                                                                                              |
| --------------- | --------------------------------------------------------------------------------------------------------------------- |
| `price`         | [Price Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream)                   |
| `quote`         | [Quote Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#quote-stream)                   |
| `kline`         | [Kline Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream)                   |
| `calendar`      | [Calendar Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#calendar-stream)             |
| `tradingStatus` | [Trading Status Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#trading-status-stream) |
| `tradability`   | [Tradability Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#tradability-stream)       |
| `orderReport`   | [Order Report Stream](/catalog/advanced-trading-stocks-trading/api/ws-streams/user-streams#order-report-stream)       |

## Timestamps

All `t` / `T` / `E` / `time` / `ts` fields are epoch milliseconds UTC.

## Authentication

| Stream type                                                                     | Requires authentication?                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `price`, `*@quote`, `*@kline_*`, `calendar`, `*@tradingStatus`, `*@tradability` | No — public market data                                                                                                                                                                                                                 |
| `{listenKey}@orderReport`                                                       | Yes — obtain the listenKey via [Listen Key](/catalog/advanced-trading-stocks-trading/api/rest-api/user-data-streams). The WebSocket URL itself carries no signature; authentication is the presence of the listenKey in the stream name |

## Heartbeat & Connection Lifecycle

The server sends standard WebSocket `PING` frames; clients MUST reply with `PONG`. Connections idle
for extended periods may be closed — callers should reconnect and resubscribe on `close`.

For `orderReport`: if the underlying `listenKey` expires (the user stops renewing it via the Listen
Key endpoint), the stream will stop pushing. Renew the `listenKey` before its 60-minute TTL to keep
the stream alive.

---

# WebSocket 流基本信息

股票交易模块通过 WebSocket 推送实时行情与用户数据。所有 stream 都是单向推送（服务端 → 客户端）。可以把 stream 名称直接编码在 URL 路径上（见下文），也可以在裸连的
`/ws` 连接上通过订阅 / 取消订阅 RPC 拿到同样的 stream（见[通过 RPC 订阅](#通过-rpc-订阅)）。

## 基础 URL

| 环境 | Base URL                            |
| ---- | ----------------------------------- |
| 生产 | `wss://nbstream.binance.com/equity` |

生产基础 URL 与其他 Binance stream 共用同一域名。下面所有示例都在这个 base 后面拼 `/ws/<streamName>`
或 `/stream?streams=<A>/<B>/<C>`。

## 单 Stream 订阅

在 `/ws/` 后面直接拼 stream 名称即可：

```
wss://nbstream.binance.com/equity/ws/AAPL@quote
```

服务端推送的就是原始事件 payload，**不带外层 wrapper**：

```javascript
{ "e": "quote", "E": 1710320400000, "s": "AAPL", "bp": "182.50", "ap": "182.55", "bs": 100, "as": 200, "T": 1710320399500 }
```

## 组合 Stream 订阅

在同一条连接上订阅多个 stream，用 `/` 分隔，拼在 `/stream?streams=` 后面：

```
wss://nbstream.binance.com/equity/stream?streams=AAPL@quote/NVDA@quote/price
```

每条推送都会被包在一层 envelope 里，告诉你属于哪个 stream：

```javascript
{
  "stream": "AAPL@quote",
  "data":   { "e": "quote", "E": 1710320400000, "s": "AAPL", "bp": "182.50", "ap": "182.55", "bs": 100, "as": 200, "T": 1710320399500 }
}
```

## 通过 RPC 订阅

裸连
`/ws`（URL 路径里不带 stream 名称）同样支持其他 WebSocket 产品线通用的订阅 / 取消订阅 RPC。发送带唯一
`id` 的 JSON 请求，服务端会在响应里原样带回这个 `id`。

```
wss://nbstream.binance.com/equity/ws
```

> **请求**

```json
{ "method": "SUBSCRIBE", "params": ["AAPL@quote"], "id": 1 }
```

> **响应**

```json
{ "result": null, "id": 1 }
```

之后该连接就会开始推送已订阅 stream 的原始事件 payload，效果和直接连 `/ws/<streamName>`
一样。`UNSUBSCRIBE`、`LIST_SUBSCRIPTIONS`、`SET_PROPERTY`、`GET_PROPERTY` 同样被识别。

## Stream 名称规则

| Stream                  | 格式                        | 大小写         | 示例                                       |
| ----------------------- | --------------------------- | -------------- | ------------------------------------------ |
| 全量价格（所有 symbol） | `price`                     | 固定小写       | `price`                                    |
| 报价（按 symbol）       | `{SYMBOL}@quote`            | SYMBOL 大写    | `AAPL@quote`                               |
| K 线（symbol + 周期）   | `{SYMBOL}@kline_{interval}` | SYMBOL 大写    | `AAPL@kline_5m`                            |
| 市场阶段日历            | `calendar`                  | 固定小写       | `calendar`                                 |
| 交易状态（按 symbol）   | `{SYMBOL}@tradingStatus`    | SYMBOL 大写    | `AAPL@tradingStatus`                       |
| 可交易方向（按 symbol） | `{SYMBOL}@tradability`      | SYMBOL 大写    | `AAPL@tradability`                         |
| 订单回报（按用户）      | `{listenKey}@orderReport`   | listenKey 原样 | `pqia91ma19a5s61cv6a81va65...@orderReport` |

SYMBOL 一律是大写的美股 ticker（`AAPL`、`NVDA`、`SPY`），与[模块级 Symbol Format](./general-info_zh-CN.md#symbol-格式)
保持一致。

## K 线周期

| 周期   | Stream 后缀 |
| ------ | ----------- |
| 5 分钟 | `kline_5m`  |
| 1 小时 | `kline_1h`  |
| 1 日   | `kline_1d`  |
| 1 周   | `kline_1w`  |
| 1 月   | `kline_1M`  |

`1Min` 周期不通过 WebSocket 推送。

## 事件类型字段

所有 payload 都带 `e` 字段标识事件类型，客户端按 `e` 分发即可：

| `e` 值          | 文档                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| `price`         | [价格流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream)              |
| `quote`         | [报价流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#quote-stream)              |
| `kline`         | [K 线流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream)              |
| `calendar`      | [日历流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#calendar-stream)           |
| `tradingStatus` | [交易状态流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#trading-status-stream) |
| `tradability`   | [可交易方向流](/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#tradability-stream)  |
| `orderReport`   | [订单回报流](/catalog/advanced-trading-stocks-trading/api/ws-streams/user-streams#order-report-stream)     |

## 时间戳

所有 `t` / `T` / `E` / `time` / `ts` 字段均为 UTC epoch 毫秒数。

## 认证

| Stream 类型                                                                     | 是否需要认证                                                                                                                                                                                 |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `price`、`*@quote`、`*@kline_*`、`calendar`、`*@tradingStatus`、`*@tradability` | 不需要——公开行情数据                                                                                                                                                                         |
| `{listenKey}@orderReport`                                                       | 需要——通过 [Listen Key](/catalog/advanced-trading-stocks-trading/api/rest-api/user-data-streams) 接口获取 listenKey。WebSocket URL 本身不带签名；以 listenKey 出现在 stream 名称中为鉴权依据 |

## 心跳与连接生命周期

服务端发送标准 WebSocket `PING` 帧，客户端**必须**回复
`PONG`。长时间空闲的连接可能被关闭——调用方应在收到 `close` 后重连并重订阅。

对于 `orderReport`：若底层 `listenKey` 过期（用户停止通过 Listen
Key 接口续期），流将停止推送。请在 listenKey 60 分钟 TTL 到期前续期。