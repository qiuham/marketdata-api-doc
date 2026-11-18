---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-18 18:48:26.720321
---

# Stocks Trading WebSocket Streams

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/1.0.0/schema.yaml

WebSocket stream definitions for Binance Stocks Trading. Base URL: wss://nbstream.binance.com/equity

Binance 股票交易的 WebSocket 流定义。基础 URL：wss://nbstream.binance.com/equity

版本: 1.0.0

## 服务地址

- `wss://nbstream.binance.com/equity`

## 接口列表

- `price` — Price Stream
- `{symbol}@quote` — Quote Stream
- `{symbol}@kline_{interval}` — Kline Stream
- `calendar` — Calendar Stream
- `{symbol}@tradability` — Tradability Stream
- `{symbol}@tradingStatus` — Trading Status Stream
- `{listenKey}@orderReport` — Order Report Stream

## Price Stream（价格流）

流名称: `price`

Push-all price snapshot, polled every 3 seconds. One message carries the latest price for every active US-equity symbol. Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

全量价格快照，每 3 秒推送一次。每条消息包含所有活跃美股 symbol 的最新价格。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `priceStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "price"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Price Stream / 价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"price"`.<br>事件类型，固定为 `"price"`。<br>例: `price` |
| rates | object[] |  | One entry per symbol.<br>每个 symbol 一条记录。 |
| rates[].s | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| rates[].ac | string |  | Internal asset code, `EQ_{symbol}`. Reference only; do not use as a trading identifier.<br>内部资产代码 `EQ_{symbol}`，仅供参考，不用作交易标识符。<br>例: `EQ_AAPL` |
| rates[].p | string |  | Latest price, trailing-zero stripped.<br>最新价格，末尾零已去除。<br>例: `182.5` |
| rates[].t | integer (int64) |  | Price time (epoch milliseconds UTC); may be null.<br>价格时间（UTC epoch 毫秒），可能为 null。<br>例: `1710320400000` |
| rates[].pc | string |  | Previous trading day's close price; absent when unknown.<br>上一交易日收盘价，不可知时不存在。<br>例: `181.2000` |
| rates[].tc | string |  | Today's close price; absent before After-Hours.<br>当天收盘价，盘后前不存在。<br>例: `182.0000` |
| rates[].lrc | string |  | Final close price of the most recent completed RTH trading day. Rolls forward only once the next trading day enters Post-Market and the 1-minute kline for the minute before that day's RTH close is available; while unavailable, the previous `lrc`/`prc` pair is retained.<br>最近一个已完成 RTH 交易日的最终收盘价。仅在下一交易日进入盘后，且当天 RTH 收盘前一分钟的 1 分钟 K 线可用时才会滚动；不可用时保留上一组 `lrc`/`prc`。<br>例: `182.0000` |
| rates[].prc | string |  | Final close price of the trading day before the `lrc` trading day. `null` when the symbol has only one completed RTH trading day (e.g. a new IPO).<br>`lrc` 对应交易日的前一交易日最终收盘价。仅有一个已完成 RTH 交易日时（如新上市 IPO）为 `null`。<br>例: `181.2000` |
| rates[].mp | string |  | Per-symbol market phase: `C` Closed, `ON` Overnight, `PRE` Pre-Market, `O` Market Open, `POST` Post-Market.<br>每 symbol 市场阶段：`C` 已收市、`ON` 夜盘、`PRE` 盘前、`O` 盘中、`POST` 盘后。<br>枚举: `C`, `True`, `PRE`, `O`, `POST`<br>例: `O` |

```json
{
  "e": "price",
  "rates": [
    {
      "s": "AAPL",
      "ac": "EQ_AAPL",
      "p": "182.5",
      "t": 1710320400000,
      "pc": "181.2000",
      "tc": "182.0000",
      "lrc": "182.0000",
      "prc": "181.2000",
      "mp": "O"
    }
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `price` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"price"`.<br>事件类型，固定为 `"price"`。<br>例: `price` |
| data.rates | object[] |  | One entry per symbol.<br>每个 symbol 一条记录。 |
| data.rates[].s | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| data.rates[].ac | string |  | Internal asset code, `EQ_{symbol}`. Reference only; do not use as a trading identifier.<br>内部资产代码 `EQ_{symbol}`，仅供参考，不用作交易标识符。<br>例: `EQ_AAPL` |
| data.rates[].p | string |  | Latest price, trailing-zero stripped.<br>最新价格，末尾零已去除。<br>例: `182.5` |
| data.rates[].t | integer (int64) |  | Price time (epoch milliseconds UTC); may be null.<br>价格时间（UTC epoch 毫秒），可能为 null。<br>例: `1710320400000` |
| data.rates[].pc | string |  | Previous trading day's close price; absent when unknown.<br>上一交易日收盘价，不可知时不存在。<br>例: `181.2000` |
| data.rates[].tc | string |  | Today's close price; absent before After-Hours.<br>当天收盘价，盘后前不存在。<br>例: `182.0000` |
| data.rates[].lrc | string |  | Final close price of the most recent completed RTH trading day. Rolls forward only once the next trading day enters Post-Market and the 1-minute kline for the minute before that day's RTH close is available; while unavailable, the previous `lrc`/`prc` pair is retained.<br>最近一个已完成 RTH 交易日的最终收盘价。仅在下一交易日进入盘后，且当天 RTH 收盘前一分钟的 1 分钟 K 线可用时才会滚动；不可用时保留上一组 `lrc`/`prc`。<br>例: `182.0000` |
| data.rates[].prc | string |  | Final close price of the trading day before the `lrc` trading day. `null` when the symbol has only one completed RTH trading day (e.g. a new IPO).<br>`lrc` 对应交易日的前一交易日最终收盘价。仅有一个已完成 RTH 交易日时（如新上市 IPO）为 `null`。<br>例: `181.2000` |
| data.rates[].mp | string |  | Per-symbol market phase: `C` Closed, `ON` Overnight, `PRE` Pre-Market, `O` Market Open, `POST` Post-Market.<br>每 symbol 市场阶段：`C` 已收市、`ON` 夜盘、`PRE` 盘前、`O` 盘中、`POST` 盘后。<br>枚举: `C`, `True`, `PRE`, `O`, `POST`<br>例: `O` |

```json
{
  "stream": "price",
  "data": {
    "e": "price",
    "rates": [
      {
        "s": "AAPL",
        "ac": "EQ_AAPL",
        "p": "182.5",
        "t": 1710320400000,
        "pc": "181.2000",
        "tc": "182.0000",
        "lrc": "182.0000",
        "prc": "181.2000",
        "mp": "O"
      }
    ]
  }
}
```

## Quote Stream（报价流）

流名称: `{symbol}@quote`

Per-symbol real-time best-bid / best-ask. Each symbol has its own stream. Per-symbol throttle: at most one push per symbol every 200 ms. Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

每个 symbol 的实时最优买一 / 卖一报价，每只 symbol 独立 stream。每 symbol 限速：每 200 ms 最多推送一次。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `quoteStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | US-equity ticker (UPPERCASE), e.g. `AAPL`.<br>美股 ticker（大写），如 `AAPL`。<br>例: `AAPL` |

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
    "AAPL@quote"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Quote Stream / 报价流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"quote"`.<br>事件类型，固定为 `"quote"`。<br>例: `quote` |
| E | integer (int64) |  | Event time — epoch milliseconds when the server pushed the message.<br>事件时间——服务端推送消息时的 epoch 毫秒数。<br>例: `1710320400000` |
| s | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| bp | string |  | Best bid price.<br>最优买一价。<br>例: `182.50` |
| ap | string |  | Best ask price.<br>最优卖一价。<br>例: `182.55` |
| bs | integer |  | Best bid size (shares).<br>最优买一量（股数）。<br>例: `100` |
| as | integer |  | Best ask size (shares).<br>最优卖一量（股数）。<br>例: `200` |
| T | integer (int64) |  | Source quote timestamp (epoch milliseconds); may be null.<br>上游报价时间戳（epoch 毫秒），可能为 null。<br>例: `1710320399500` |

```json
{
  "e": "quote",
  "E": 1710320400000,
  "s": "AAPL",
  "bp": "182.50",
  "ap": "182.55",
  "bs": 100,
  "as": 200,
  "T": 1710320399500
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `AAPL@quote` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"quote"`.<br>事件类型，固定为 `"quote"`。<br>例: `quote` |
| data.E | integer (int64) |  | Event time — epoch milliseconds when the server pushed the message.<br>事件时间——服务端推送消息时的 epoch 毫秒数。<br>例: `1710320400000` |
| data.s | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| data.bp | string |  | Best bid price.<br>最优买一价。<br>例: `182.50` |
| data.ap | string |  | Best ask price.<br>最优卖一价。<br>例: `182.55` |
| data.bs | integer |  | Best bid size (shares).<br>最优买一量（股数）。<br>例: `100` |
| data.as | integer |  | Best ask size (shares).<br>最优卖一量（股数）。<br>例: `200` |
| data.T | integer (int64) |  | Source quote timestamp (epoch milliseconds); may be null.<br>上游报价时间戳（epoch 毫秒），可能为 null。<br>例: `1710320399500` |

```json
{
  "stream": "AAPL@quote",
  "data": {
    "e": "quote",
    "E": 1710320400000,
    "s": "AAPL",
    "bp": "182.50",
    "ap": "182.55",
    "bs": 100,
    "as": 200,
    "T": 1710320399500
  }
}
```

## Kline Stream（K 线流）

流名称: `{symbol}@kline_{interval}`

Per-symbol candlestick updates. One stream per (symbol, interval) combination. Supported intervals: 5m, 1h, 1d, 1w, 1M. Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

每个 symbol 的 K 线更新，每个（symbol, 周期）组合一个 stream。支持周期：5m、1h、1d、1w、1M。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `klineStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | US-equity ticker (UPPERCASE), e.g. `AAPL`.<br>美股 ticker（大写），如 `AAPL`。<br>例: `AAPL` |
| interval | path | string | 是 | Kline interval — `5m` / `1h` / `1d` / `1w` / `1M`.<br>K 线周期——`5m` / `1h` / `1d` / `1w` / `1M`。<br>例: `5m` |

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
    "AAPL@kline_5m"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Kline Stream / K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"kline"`.<br>事件类型，固定为 `"kline"`。<br>例: `kline` |
| E | integer (int64) |  | Event time (epoch milliseconds); server-side system time when the message is pushed.<br>事件时间（epoch 毫秒），服务端推送消息时的系统时间。<br>例: `1710320400000` |
| s | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| k | object |  | Candlestick payload.<br>K 线数据。 |
| k.t | integer (int64) |  | Open time (epoch milliseconds).<br>开盘时间（epoch 毫秒）。<br>例: `1710316800000` |
| k.ct | integer (int64) |  | Close time (epoch milliseconds). For fixed intervals: `openTime + duration − 1ms`. For `1M`: last day of month at 23:59:59.999 UTC.<br>收盘时间（epoch 毫秒）。固定周期：`openTime + 时长 − 1ms`；`1M`：当月最后一天 23:59:59.999 UTC。<br>例: `1710317099999` |
| k.s | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| k.i | string |  | Interval — `"5m"` / `"1h"` / `"1d"` / `"1w"` / `"1M"`.<br>周期——`"5m"` / `"1h"` / `"1d"` / `"1w"` / `"1M"`。<br>枚举: `5m`, `1h`, `1d`, `1w`, `1M`<br>例: `5m` |
| k.o | string |  | Open price.<br>开盘价。<br>例: `182.50` |
| k.c | string |  | Close price (latest print within the interval).<br>收盘价（区间内最新成交价）。<br>例: `183.20` |
| k.h | string |  | High price.<br>最高价。<br>例: `183.50` |
| k.l | string |  | Low price.<br>最低价。<br>例: `182.30` |
| k.v | string |  | Volume (shares), default `"0"`.<br>成交量（股数），默认 `"0"`。<br>例: `15000` |
| k.n | integer |  | Trade count; absent when upstream did not populate.<br>成交笔数，上游未填充时不存在。<br>例: `120` |
| k.x | boolean |  | Candle is closed — `true` once the interval has ended.<br>K 线是否已收盘——区间结束后为 `true`。<br>例: `False` |
| k.vw | string |  | VWAP (volume-weighted average price); absent when upstream did not populate.<br>VWAP（成交量加权平均价），上游未填充时不存在。<br>例: `182.95` |

```json
{
  "e": "kline",
  "E": 1710320400000,
  "s": "AAPL",
  "k": {
    "t": 1710316800000,
    "ct": 1710317099999,
    "s": "AAPL",
    "i": "5m",
    "o": "182.50",
    "c": "183.20",
    "h": "183.50",
    "l": "182.30",
    "v": "15000",
    "n": 120,
    "x": false,
    "vw": "182.95"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `AAPL@kline_5m` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"kline"`.<br>事件类型，固定为 `"kline"`。<br>例: `kline` |
| data.E | integer (int64) |  | Event time (epoch milliseconds); server-side system time when the message is pushed.<br>事件时间（epoch 毫秒），服务端推送消息时的系统时间。<br>例: `1710320400000` |
| data.s | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| data.k | object |  | Candlestick payload.<br>K 线数据。 |
| data.k.t | integer (int64) |  | Open time (epoch milliseconds).<br>开盘时间（epoch 毫秒）。<br>例: `1710316800000` |
| data.k.ct | integer (int64) |  | Close time (epoch milliseconds). For fixed intervals: `openTime + duration − 1ms`. For `1M`: last day of month at 23:59:59.999 UTC.<br>收盘时间（epoch 毫秒）。固定周期：`openTime + 时长 − 1ms`；`1M`：当月最后一天 23:59:59.999 UTC。<br>例: `1710317099999` |
| data.k.s | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| data.k.i | string |  | Interval — `"5m"` / `"1h"` / `"1d"` / `"1w"` / `"1M"`.<br>周期——`"5m"` / `"1h"` / `"1d"` / `"1w"` / `"1M"`。<br>枚举: `5m`, `1h`, `1d`, `1w`, `1M`<br>例: `5m` |
| data.k.o | string |  | Open price.<br>开盘价。<br>例: `182.50` |
| data.k.c | string |  | Close price (latest print within the interval).<br>收盘价（区间内最新成交价）。<br>例: `183.20` |
| data.k.h | string |  | High price.<br>最高价。<br>例: `183.50` |
| data.k.l | string |  | Low price.<br>最低价。<br>例: `182.30` |
| data.k.v | string |  | Volume (shares), default `"0"`.<br>成交量（股数），默认 `"0"`。<br>例: `15000` |
| data.k.n | integer |  | Trade count; absent when upstream did not populate.<br>成交笔数，上游未填充时不存在。<br>例: `120` |
| data.k.x | boolean |  | Candle is closed — `true` once the interval has ended.<br>K 线是否已收盘——区间结束后为 `true`。<br>例: `False` |
| data.k.vw | string |  | VWAP (volume-weighted average price); absent when upstream did not populate.<br>VWAP（成交量加权平均价），上游未填充时不存在。<br>例: `182.95` |

```json
{
  "stream": "AAPL@kline_5m",
  "data": {
    "e": "kline",
    "E": 1710320400000,
    "s": "AAPL",
    "k": {
      "t": 1710316800000,
      "ct": 1710317099999,
      "s": "AAPL",
      "i": "5m",
      "o": "182.50",
      "c": "183.20",
      "h": "183.50",
      "l": "182.30",
      "v": "15000",
      "n": 120,
      "x": false,
      "vw": "182.95"
    }
  }
}
```

## Calendar Stream（日历流）

流名称: `calendar`

Single-stream broadcast of market-phase transitions. One message per transition; no periodic heartbeat payload. Server polls every 5 seconds. Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

广播市场阶段切换事件，每次切换推送一条消息，无定时心跳。服务端每 5 秒轮询一次。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `calendarStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "calendar"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Calendar Stream / 日历流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"calendar"`.<br>事件类型，固定为 `"calendar"`。<br>例: `calendar` |
| from | string |  | Previous market phase.<br>切换前的市场阶段。<br>枚举: `MARKET_CLOSED`, `OVERNIGHT`, `PRE_MARKET`, `MARKET_OPEN`, `POST_MARKET`<br>例: `PRE_MARKET` |
| to | string |  | New market phase.<br>切换后的新市场阶段。<br>枚举: `MARKET_CLOSED`, `OVERNIGHT`, `PRE_MARKET`, `MARKET_OPEN`, `POST_MARKET`<br>例: `MARKET_OPEN` |
| ts | integer (int64) |  | Event timestamp (epoch milliseconds UTC) when the transition was detected.<br>切换被检测到时的事件时间戳（UTC epoch 毫秒）。<br>例: `1710334200000` |

```json
{
  "e": "calendar",
  "from": "PRE_MARKET",
  "to": "MARKET_OPEN",
  "ts": 1710334200000
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `calendar` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"calendar"`.<br>事件类型，固定为 `"calendar"`。<br>例: `calendar` |
| data.from | string |  | Previous market phase.<br>切换前的市场阶段。<br>枚举: `MARKET_CLOSED`, `OVERNIGHT`, `PRE_MARKET`, `MARKET_OPEN`, `POST_MARKET`<br>例: `PRE_MARKET` |
| data.to | string |  | New market phase.<br>切换后的新市场阶段。<br>枚举: `MARKET_CLOSED`, `OVERNIGHT`, `PRE_MARKET`, `MARKET_OPEN`, `POST_MARKET`<br>例: `MARKET_OPEN` |
| data.ts | integer (int64) |  | Event timestamp (epoch milliseconds UTC) when the transition was detected.<br>切换被检测到时的事件时间戳（UTC epoch 毫秒）。<br>例: `1710334200000` |

```json
{
  "stream": "calendar",
  "data": {
    "e": "calendar",
    "from": "PRE_MARKET",
    "to": "MARKET_OPEN",
    "ts": 1710334200000
  }
}
```

## Tradability Stream（可交易方向流）

流名称: `{symbol}@tradability`

Per-symbol push whenever the tradable direction of a symbol changes. Pushed only when the value actually changes (new value ≠ old value). Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

每当 symbol 的可交易方向发生变化时推送。仅在值实际变化时推送（新值 ≠ 旧值）。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `tradabilityStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | US-equity ticker (UPPERCASE), e.g. `AAPL`.<br>美股 ticker（大写），如 `AAPL`。<br>例: `AAPL` |

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
    "AAPL@tradability"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Tradability Stream / 可交易方向流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"tradability"`.<br>事件类型，固定为 `"tradability"`。<br>例: `tradability` |
| symbol | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| assetCode | string |  | Internal asset code `EQ_{symbol}`; reference only. May be null for symbols not yet in the symbol dictionary.<br>内部资产代码 `EQ_{symbol}`，仅供参考。对尚未加入 symbol 字典的 symbol 可能为 null。<br>例: `EQ_AAPL` |
| tradability | string |  | The new tradability value. `OFFMARKET` and `DELISTING` are protected states — trading-status events will not transition a symbol out of them.<br>新的可交易方向值。`OFFMARKET` 和 `DELISTING` 为保护状态——交易状态事件不能将 symbol 从这两个状态转出。<br>枚举: `BUY_SELL`, `BUY`, `SELL`, `NONE`, `OFFMARKET`, `DELISTING`<br>例: `BUY_SELL` |
| t | integer (int64) |  | Push time (epoch milliseconds UTC).<br>推送时间（UTC epoch 毫秒）。<br>例: `1712345678000` |

```json
{
  "e": "tradability",
  "symbol": "AAPL",
  "assetCode": "EQ_AAPL",
  "tradability": "BUY_SELL",
  "t": 1712345678000
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `AAPL@tradability` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"tradability"`.<br>事件类型，固定为 `"tradability"`。<br>例: `tradability` |
| data.symbol | string |  | Symbol (UPPERCASE ticker).<br>Symbol（大写 ticker）。<br>例: `AAPL` |
| data.assetCode | string |  | Internal asset code `EQ_{symbol}`; reference only. May be null for symbols not yet in the symbol dictionary.<br>内部资产代码 `EQ_{symbol}`，仅供参考。对尚未加入 symbol 字典的 symbol 可能为 null。<br>例: `EQ_AAPL` |
| data.tradability | string |  | The new tradability value. `OFFMARKET` and `DELISTING` are protected states — trading-status events will not transition a symbol out of them.<br>新的可交易方向值。`OFFMARKET` 和 `DELISTING` 为保护状态——交易状态事件不能将 symbol 从这两个状态转出。<br>枚举: `BUY_SELL`, `BUY`, `SELL`, `NONE`, `OFFMARKET`, `DELISTING`<br>例: `BUY_SELL` |
| data.t | integer (int64) |  | Push time (epoch milliseconds UTC).<br>推送时间（UTC epoch 毫秒）。<br>例: `1712345678000` |

```json
{
  "stream": "AAPL@tradability",
  "data": {
    "e": "tradability",
    "symbol": "AAPL",
    "assetCode": "EQ_AAPL",
    "tradability": "BUY_SELL",
    "t": 1712345678000
  }
}
```

## Trading Status Stream（交易状态流）

流名称: `{symbol}@tradingStatus`

Per-symbol trading-status transitions (halts, resumes, SSR, LULD pauses, etc.). Events that do not match a known status/reason rule are not pushed. Also reachable via the SUBSCRIBE/UNSUBSCRIBE RPC — see [Subscribing via RPC](https://developers.binance.com/en/docs/products/stocks/websocket-streams-general-info#subscribing-via-rpc).

每个 symbol 的交易状态切换（停牌、恢复、SSR、LULD 暂停等）。不符合已知状态 / 原因规则的事件不推送。也可以通过 SUBSCRIBE/UNSUBSCRIBE RPC 获取——见[通过 RPC 订阅](https://developers.binance.com/zh-CN/docs/products/stocks/websocket-streams-general-info#通过-rpc-订阅)。

Operation ID: `tradingStatusStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | US-equity ticker (UPPERCASE), e.g. `AAPL`.<br>美股 ticker（大写），如 `AAPL`。<br>例: `AAPL` |

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
    "AAPL@tradingStatus"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Trading Status Stream / 交易状态流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"tradingStatus"`.<br>事件类型，固定为 `"tradingStatus"`。<br>例: `tradingStatus` |
| symbol | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| assetCode | string |  | Internal asset code `EQ_{symbol}`; reference only.<br>内部资产代码 `EQ_{symbol}`，仅供参考。<br>例: `EQ_AAPL` |
| status | string |  | Trading status.<br>交易状态。<br>枚举: `TRADING_HALTED`, `TRADING_PAUSED`, `SHORT_SALE_RESTRICTED`, `TRADING_RESUMED`, `QUOTATION_RESUMED`, `TRADING_SUSPENDED`, `UNAVAILABLE`<br>例: `TRADING_HALTED` |
| msg | string |  | Reason code.<br>原因码。<br>例: `MATERIAL_NEWS` |
| time | integer (int64) |  | Status-effective time (epoch milliseconds UTC). May be in the future.<br>状态生效时间（UTC epoch 毫秒），可能是未来时间。<br>例: `1614021300000` |
| z | string |  | Tape designation: `C` = CTA (NYSE / AMEX), `N` = UTP (Nasdaq).<br>Tape 标识：`C` = CTA（NYSE / AMEX），`N` = UTP（Nasdaq）。<br>枚举: `C`, `N`<br>例: `C` |
| tradability | string |  | Tradability after the status change: `BUY_SELL` / `BUY` / `SELL` / `NONE`.<br>状态变化后的可交易方向：`BUY_SELL` / `BUY` / `SELL` / `NONE`。<br>枚举: `BUY_SELL`, `BUY`, `SELL`, `NONE`<br>例: `NONE` |

```json
{
  "e": "tradingStatus",
  "symbol": "AAPL",
  "assetCode": "EQ_AAPL",
  "status": "TRADING_HALTED",
  "msg": "MATERIAL_NEWS",
  "time": 1614021300000,
  "z": "C",
  "tradability": "NONE"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `AAPL@tradingStatus` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"tradingStatus"`.<br>事件类型，固定为 `"tradingStatus"`。<br>例: `tradingStatus` |
| data.symbol | string |  | Symbol (UPPERCASE ticker), e.g. `"AAPL"`.<br>Symbol（大写 ticker），例如 `"AAPL"`。<br>例: `AAPL` |
| data.assetCode | string |  | Internal asset code `EQ_{symbol}`; reference only.<br>内部资产代码 `EQ_{symbol}`，仅供参考。<br>例: `EQ_AAPL` |
| data.status | string |  | Trading status.<br>交易状态。<br>枚举: `TRADING_HALTED`, `TRADING_PAUSED`, `SHORT_SALE_RESTRICTED`, `TRADING_RESUMED`, `QUOTATION_RESUMED`, `TRADING_SUSPENDED`, `UNAVAILABLE`<br>例: `TRADING_HALTED` |
| data.msg | string |  | Reason code.<br>原因码。<br>例: `MATERIAL_NEWS` |
| data.time | integer (int64) |  | Status-effective time (epoch milliseconds UTC). May be in the future.<br>状态生效时间（UTC epoch 毫秒），可能是未来时间。<br>例: `1614021300000` |
| data.z | string |  | Tape designation: `C` = CTA (NYSE / AMEX), `N` = UTP (Nasdaq).<br>Tape 标识：`C` = CTA（NYSE / AMEX），`N` = UTP（Nasdaq）。<br>枚举: `C`, `N`<br>例: `C` |
| data.tradability | string |  | Tradability after the status change: `BUY_SELL` / `BUY` / `SELL` / `NONE`.<br>状态变化后的可交易方向：`BUY_SELL` / `BUY` / `SELL` / `NONE`。<br>枚举: `BUY_SELL`, `BUY`, `SELL`, `NONE`<br>例: `NONE` |

```json
{
  "stream": "AAPL@tradingStatus",
  "data": {
    "e": "tradingStatus",
    "symbol": "AAPL",
    "assetCode": "EQ_AAPL",
    "status": "TRADING_HALTED",
    "msg": "MATERIAL_NEWS",
    "time": 1614021300000,
    "z": "C",
    "tradability": "NONE"
  }
}
```

## Order Report Stream（订单回报流）

流名称: `{listenKey}@orderReport`

Real-time push of the authenticated user's order state transitions — both open-state updates (`ORDER_UPDATE`) and terminal-state notifications (`ORDER_TERMINAL`). Prerequisite: obtain a `listenKey` via the Listen Key endpoint first.

实时推送认证用户的订单状态变化——包括开放状态更新（`ORDER_UPDATE`）和终态通知（`ORDER_TERMINAL`）。前提：先通过 Listen Key 接口获取 `listenKey`。

Operation ID: `orderReportStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| listenKey | path | string | 是 | User data listen key obtained from the Listen Key endpoint.<br>从 Listen Key 接口获取的用户数据 listenKey。<br>例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s6af0dkfj2a97b8a91d` |

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
    "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s6af0dkfj2a97b8a91d@orderReport"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Order Report Stream / 订单回报流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, always `"orderReport"`.<br>事件类型，固定为 `"orderReport"`。<br>例: `orderReport` |
| E | integer (int64) |  | Event time (epoch milliseconds); server push time.<br>事件时间（epoch 毫秒）；服务端推送时间。<br>例: `1710000000000` |
| x | string |  | Execution type: `"ORDER_UPDATE"` (still open) or `"ORDER_TERMINAL"` (reached terminal state).<br>执行类型：`"ORDER_UPDATE"`（仍开放）或 `"ORDER_TERMINAL"`（已到达终态）。<br>枚举: `ORDER_UPDATE`, `ORDER_TERMINAL`<br>例: `ORDER_UPDATE` |
| i | string |  | Order ID (UUID).<br>订单 ID（UUID）。<br>例: `b0b6dd9d-8b9b-48a9-ba46-b9d54906e415` |
| ai | string |  | Asset ID (internal identifier).<br>资产 ID（内部标识）。<br>例: `4ce9353c-66d1-46c2-898f-fce867ab0247` |
| b | string |  | Base asset — the internal asset code with an `EQ_` prefix (e.g. `"EQ_AAPL"`), not the bare ticker used in REST responses / order input. Strip the `EQ_` prefix to match a symbol used elsewhere.<br>基础资产——带 `EQ_` 前缀的内部资产代码（如 `"EQ_AAPL"`），而非 REST 响应/下单入参里用的裸 ticker。如需与别处的 symbol 匹配，请去掉 `EQ_` 前缀。<br>例: `EQ_AAPL` |
| q | string |  | Quote currency, e.g. `"USD"`.<br>计价货币，例如 `"USD"`。<br>例: `USD` |
| S | string |  | Order side: `"buy"` or `"sell"`. Note: lowercase, unlike REST responses.<br>订单方向：`"buy"` 或 `"sell"`。注意：为小写，与 REST 响应不同。<br>例: `buy` |
| o | string |  | Order type: `"market"` / `"limit"` / `"stop"` / `"stop_limit"` / `"trailing_stop"`. Note: lowercase.<br>订单类型：`"market"` / `"limit"` / `"stop"` / `"stop_limit"` / `"trailing_stop"`。注意：为小写。<br>例: `limit` |
| p | number |  | Limit price; null for market orders.<br>限价；市价单为 null。<br>例: `185.5` |
| Q | number |  | Order quantity (shares); `0` when the order was submitted as notional.<br>订单数量（股数）；按名义金额下单时为 `0`。<br>例: `10` |
| N | number |  | Order notional; set when the order was submitted as notional (market buy), null when submitted as quantity.<br>订单名义金额；按名义金额下单（市价买入）时填充，按数量下单时为 null。<br>例: `None` |
| fq | number |  | Filled quantity.<br>已成交数量。<br>例: `5` |
| FN | number |  | Filled notional (= filledQty × filledAvgPrice).<br>已成交名义金额（= 成交数量 × 均价）。<br>例: `927.5` |
| tc | number |  | Total cost — cumulative buy-in cost including the commission fee.<br>总成本（含手续费的累计买入成本）。<br>例: `1856.2` |
| Z | number |  | Fill progress percentage (0–100, 2 dp). By notional: `FN / N × 100`. By qty: `fq / Q × 100`.<br>成交进度百分比（0–100，2 位小数）。按名义金额：`FN / N × 100`；按数量：`fq / Q × 100`。<br>例: `50` |
| n | string |  | Trading session label, e.g. `"Regular"`, `"24 Hours Trading"`.<br>交易时段标签，例如 `"Regular"`、`"24 Hours Trading"`。<br>例: `Regular` |
| s | string |  | Order status, e.g. `"accepted"`, `"partially_filled"`, `"filled"`, `"canceled"`. Note: lowercase, unlike REST responses.<br>订单状态，例如 `"accepted"`、`"partially_filled"`、`"filled"`、`"canceled"`。注意：为小写，与 REST 响应不同。<br>例: `partially_filled` |
| T | integer (int64) |  | Order create time (epoch milliseconds).<br>订单创建时间（epoch 毫秒）。<br>例: `1710000000000` |
| U | integer (int64) |  | Order update time (epoch milliseconds).<br>订单更新时间（epoch 毫秒）。<br>例: `1710000060000` |

```json
{
  "e": "orderReport",
  "E": 1710000000000,
  "x": "ORDER_UPDATE",
  "i": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "ai": "4ce9353c-66d1-46c2-898f-fce867ab0247",
  "b": "EQ_AAPL",
  "q": "USD",
  "S": "buy",
  "o": "limit",
  "p": 185.5,
  "Q": 10,
  "N": null,
  "fq": 5,
  "FN": 927.5,
  "tc": 1856.2,
  "Z": 50,
  "n": "Regular",
  "s": "partially_filled",
  "T": 1710000000000,
  "U": 1710000060000
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s6af0dkfj2a97b8a91d@orderReport` |
| data | object | 是 |  |
| data.e | string |  | Event type, always `"orderReport"`.<br>事件类型，固定为 `"orderReport"`。<br>例: `orderReport` |
| data.E | integer (int64) |  | Event time (epoch milliseconds); server push time.<br>事件时间（epoch 毫秒）；服务端推送时间。<br>例: `1710000000000` |
| data.x | string |  | Execution type: `"ORDER_UPDATE"` (still open) or `"ORDER_TERMINAL"` (reached terminal state).<br>执行类型：`"ORDER_UPDATE"`（仍开放）或 `"ORDER_TERMINAL"`（已到达终态）。<br>枚举: `ORDER_UPDATE`, `ORDER_TERMINAL`<br>例: `ORDER_UPDATE` |
| data.i | string |  | Order ID (UUID).<br>订单 ID（UUID）。<br>例: `b0b6dd9d-8b9b-48a9-ba46-b9d54906e415` |
| data.ai | string |  | Asset ID (internal identifier).<br>资产 ID（内部标识）。<br>例: `4ce9353c-66d1-46c2-898f-fce867ab0247` |
| data.b | string |  | Base asset — the internal asset code with an `EQ_` prefix (e.g. `"EQ_AAPL"`), not the bare ticker used in REST responses / order input. Strip the `EQ_` prefix to match a symbol used elsewhere.<br>基础资产——带 `EQ_` 前缀的内部资产代码（如 `"EQ_AAPL"`），而非 REST 响应/下单入参里用的裸 ticker。如需与别处的 symbol 匹配，请去掉 `EQ_` 前缀。<br>例: `EQ_AAPL` |
| data.q | string |  | Quote currency, e.g. `"USD"`.<br>计价货币，例如 `"USD"`。<br>例: `USD` |
| data.S | string |  | Order side: `"buy"` or `"sell"`. Note: lowercase, unlike REST responses.<br>订单方向：`"buy"` 或 `"sell"`。注意：为小写，与 REST 响应不同。<br>例: `buy` |
| data.o | string |  | Order type: `"market"` / `"limit"` / `"stop"` / `"stop_limit"` / `"trailing_stop"`. Note: lowercase.<br>订单类型：`"market"` / `"limit"` / `"stop"` / `"stop_limit"` / `"trailing_stop"`。注意：为小写。<br>例: `limit` |
| data.p | number |  | Limit price; null for market orders.<br>限价；市价单为 null。<br>例: `185.5` |
| data.Q | number |  | Order quantity (shares); `0` when the order was submitted as notional.<br>订单数量（股数）；按名义金额下单时为 `0`。<br>例: `10` |
| data.N | number |  | Order notional; set when the order was submitted as notional (market buy), null when submitted as quantity.<br>订单名义金额；按名义金额下单（市价买入）时填充，按数量下单时为 null。<br>例: `None` |
| data.fq | number |  | Filled quantity.<br>已成交数量。<br>例: `5` |
| data.FN | number |  | Filled notional (= filledQty × filledAvgPrice).<br>已成交名义金额（= 成交数量 × 均价）。<br>例: `927.5` |
| data.tc | number |  | Total cost — cumulative buy-in cost including the commission fee.<br>总成本（含手续费的累计买入成本）。<br>例: `1856.2` |
| data.Z | number |  | Fill progress percentage (0–100, 2 dp). By notional: `FN / N × 100`. By qty: `fq / Q × 100`.<br>成交进度百分比（0–100，2 位小数）。按名义金额：`FN / N × 100`；按数量：`fq / Q × 100`。<br>例: `50` |
| data.n | string |  | Trading session label, e.g. `"Regular"`, `"24 Hours Trading"`.<br>交易时段标签，例如 `"Regular"`、`"24 Hours Trading"`。<br>例: `Regular` |
| data.s | string |  | Order status, e.g. `"accepted"`, `"partially_filled"`, `"filled"`, `"canceled"`. Note: lowercase, unlike REST responses.<br>订单状态，例如 `"accepted"`、`"partially_filled"`、`"filled"`、`"canceled"`。注意：为小写，与 REST 响应不同。<br>例: `partially_filled` |
| data.T | integer (int64) |  | Order create time (epoch milliseconds).<br>订单创建时间（epoch 毫秒）。<br>例: `1710000000000` |
| data.U | integer (int64) |  | Order update time (epoch milliseconds).<br>订单更新时间（epoch 毫秒）。<br>例: `1710000060000` |

```json
{
  "stream": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s6af0dkfj2a97b8a91d@orderReport",
  "data": {
    "e": "orderReport",
    "E": 1710000000000,
    "x": "ORDER_UPDATE",
    "i": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
    "ai": "4ce9353c-66d1-46c2-898f-fce867ab0247",
    "b": "EQ_AAPL",
    "q": "USD",
    "S": "buy",
    "o": "limit",
    "p": 185.5,
    "Q": 10,
    "N": null,
    "fq": 5,
    "FN": 927.5,
    "tc": 1856.2,
    "Z": 50,
    "n": "Regular",
    "s": "partially_filled",
    "T": 1710000000000,
    "U": 1710000060000
  }
}
```