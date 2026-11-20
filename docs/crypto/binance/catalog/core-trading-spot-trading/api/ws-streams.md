---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-20 18:50:20.056859
---

# Spot WebSocket Market Streams

Schema: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/1.0.0/schema.yaml

Access market data, manage accounts, and trade on Binance Spot.

访问市场数据、管理账户，并在 Binance 现货市场交易。

版本: 1.0.0

## 服务地址

- `wss://stream.binance.com:9443`
- `wss://stream.binance.com:443`
- `wss://demo-stream.binance.com:9443`
- `wss://demo-stream.binance.com:443`
- `wss://stream.testnet.binance.vision`

## 接口列表

- `{symbol}@aggTrade` — Aggregate Trade Streams
- `!ticker_{windowSize}@arr` — All Market Rolling Window Statistics Streams
- `!miniTicker@arr` — All Market Mini Tickers Stream
- `{symbol}@avgPrice` — Average Price
- `{symbol}@bookTicker` — Individual Symbol Book Ticker Streams
- `{symbol}@depth@{updateSpeed}` — Diff. Depth Stream
- `{symbol}@kline_{interval}` — Kline/Candlestick Streams for UTC
- `{symbol}@kline_{interval}@+08:00` — Kline/Candlestick Streams with timezone offset
- `{symbol}@miniTicker` — Individual Symbol Mini Ticker Stream
- `{symbol}@depth{levels}@{updateSpeed}` — Partial Book Depth Streams
- `{symbol}@referencePrice` — Reference Price Streams
- `{symbol}@ticker_{windowSize}` — Individual Symbol Rolling Window Statistics Streams
- `{symbol}@ticker` — Individual Symbol Ticker Streams
- `{symbol}@trade` — Trade Streams
- `{symbol}@blockTrade` — Block Trade Streams

## Aggregate Trade Streams（归集交易）

流名称: `{symbol}@aggTrade`

The Aggregate Trade Streams push trade information that is aggregated
for a single taker order.

归集交易与逐笔交易的区别在于，同一个taker在同一价格与多个maker成交时，会被归集为一笔成交。

更新速度: Real-time / 实时

Operation ID: `aggTrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@aggTrade"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Aggregate Trade Streams / 归集交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| a | integer (int64) |  | Aggregate trade ID<br>归集交易ID<br>例: `12345` |
| p | string |  | Price<br>成交价格<br>例: `0.001` |
| q | string |  | Quantity<br>成交数量<br>例: `100` |
| f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `100` |
| l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `105` |
| T | integer (int64) |  | Trade time<br>成交时间<br>例: `1672515782136` |
| m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| M | boolean |  | Ignore<br>请忽略该字段<br>例: `True` |

```json
{
  "e": "aggTrade",
  "E": 1672515782136,
  "s": "BNBBTC",
  "a": 12345,
  "p": "0.001",
  "q": "100",
  "f": 100,
  "l": 105,
  "T": 1672515782136,
  "m": true,
  "M": true
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@aggTrade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.a | integer (int64) |  | Aggregate trade ID<br>归集交易ID<br>例: `12345` |
| data.p | string |  | Price<br>成交价格<br>例: `0.001` |
| data.q | string |  | Quantity<br>成交数量<br>例: `100` |
| data.f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `100` |
| data.l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `105` |
| data.T | integer (int64) |  | Trade time<br>成交时间<br>例: `1672515782136` |
| data.m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| data.M | boolean |  | Ignore<br>请忽略该字段<br>例: `True` |

```json
{
  "stream": "bnbusdt@aggTrade",
  "data": {
    "e": "aggTrade",
    "E": 1672515782136,
    "s": "BNBBTC",
    "a": 12345,
    "p": "0.001",
    "q": "100",
    "f": 100,
    "l": 105,
    "T": 1672515782136,
    "m": true,
    "M": true
  }
}
```

## All Market Rolling Window Statistics Streams（全市场滚动窗口统计）

流名称: `!ticker_{windowSize}@arr`

Rolling window ticker statistics for all market symbols, computed over
multiple windows.

Note that only tickers that have changed will be present in the array.

全市场symbols的滚动窗口ticker统计，计算于多个窗口。

注意：有变动的ticker才会推送。

更新速度: 1000ms

Operation ID: `allMarketRollingWindowTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| windowSize | path | string | 是 | 枚举: `1h`, `4h`, `1d`<br>例: `1h` |

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
    "!ticker_1h@arr"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：All Market Rolling Window Statistics Streams / 全市场滚动窗口统计

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `1hTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| [].s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| [].p | string |  | Price change<br>价格变化<br>例: `0.0015` |
| [].P | string |  | Price change percent<br>价格变化百分比<br>例: `250.00` |
| [].o | string |  | Open price<br>开盘价<br>例: `0.0010` |
| [].h | string |  | High price<br>最高价<br>例: `0.0025` |
| [].l | string |  | Low price<br>最低价<br>例: `0.0010` |
| [].c | string |  | Last price<br>最新价<br>例: `0.0025` |
| [].w | string |  | Weighted average price<br>加权平均价格<br>例: `0.0018` |
| [].v | string |  | Total traded base asset volume<br>总成交基础资产量<br>例: `10000` |
| [].q | string |  | Total traded quote asset volume<br>总成交计价资产量<br>例: `18` |
| [].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| [].C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| [].F | integer (int64) |  | First trade ID<br>第一笔成交ID<br>例: `0` |
| [].L | integer (int64) |  | Last trade Id<br>最后一笔成交ID<br>例: `18150` |
| [].n | integer (int64) |  | Total number of trades<br>总成交笔数<br>例: `18151` |

```json
[
  {
    "e": "1hTicker",
    "E": 1672515782136,
    "s": "BNBBTC",
    "p": "0.0015",
    "P": "250.00",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "c": "0.0025",
    "w": "0.0018",
    "v": "10000",
    "q": "18",
    "O": 0,
    "C": 1675216573749,
    "F": 0,
    "L": 18150,
    "n": 18151
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!ticker_1h@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `1hTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data[].p | string |  | Price change<br>价格变化<br>例: `0.0015` |
| data[].P | string |  | Price change percent<br>价格变化百分比<br>例: `250.00` |
| data[].o | string |  | Open price<br>开盘价<br>例: `0.0010` |
| data[].h | string |  | High price<br>最高价<br>例: `0.0025` |
| data[].l | string |  | Low price<br>最低价<br>例: `0.0010` |
| data[].c | string |  | Last price<br>最新价<br>例: `0.0025` |
| data[].w | string |  | Weighted average price<br>加权平均价格<br>例: `0.0018` |
| data[].v | string |  | Total traded base asset volume<br>总成交基础资产量<br>例: `10000` |
| data[].q | string |  | Total traded quote asset volume<br>总成交计价资产量<br>例: `18` |
| data[].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| data[].C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| data[].F | integer (int64) |  | First trade ID<br>第一笔成交ID<br>例: `0` |
| data[].L | integer (int64) |  | Last trade Id<br>最后一笔成交ID<br>例: `18150` |
| data[].n | integer (int64) |  | Total number of trades<br>总成交笔数<br>例: `18151` |

```json
{
  "stream": "!ticker_1h@arr",
  "data": [
    {
      "e": "1hTicker",
      "E": 1672515782136,
      "s": "BNBBTC",
      "p": "0.0015",
      "P": "250.00",
      "o": "0.0010",
      "h": "0.0025",
      "l": "0.0010",
      "c": "0.0025",
      "w": "0.0018",
      "v": "10000",
      "q": "18",
      "O": 0,
      "C": 1675216573749,
      "F": 0,
      "L": 18150,
      "n": 18151
    }
  ]
}
```

## All Market Mini Tickers Stream（全市场所有Symbol的精简Ticker）

流名称: `!miniTicker@arr`

24hr rolling window mini-ticker statistics for all symbols that changed
in an array. These are NOT the statistics of the UTC day, but a 24hr
rolling window for the previous 24hrs. Note that only tickers that have
changed will be present in the array.

所有交易对的24小时滚动窗口迷你行情统计，以数组形式推送。这些不是UTC日统计数据，而是过去24小时的滚动窗口。注意，只有发生变化的行情才会出现在数组中。

更新速度: 1000ms

Operation ID: `allMiniTicker`

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
    "!miniTicker@arr"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：All Market Mini Tickers Stream / All Market Mini 行情s Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| [].s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| [].c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| [].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| [].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| [].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| [].v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| [].q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |

```json
[
  {
    "e": "24hrMiniTicker",
    "E": 1672515782136,
    "s": "BNBBTC",
    "c": "0.0025",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18"
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!miniTicker@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data[].c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| data[].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| data[].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data[].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data[].v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| data[].q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |

```json
{
  "stream": "!miniTicker@arr",
  "data": [
    {
      "e": "24hrMiniTicker",
      "E": 1672515782136,
      "s": "BNBBTC",
      "c": "0.0025",
      "o": "0.0010",
      "h": "0.0025",
      "l": "0.0010",
      "v": "10000",
      "q": "18"
    }
  ]
}
```

## Average Price（平均价格）

流名称: `{symbol}@avgPrice`

Average price streams push changes in the average price over a fixed time interval.

平均价格流推送在固定时间间隔内的平均价格变动。

更新速度: 1000ms

Operation ID: `avgPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@avgPrice"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Average Price / 平均价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `avgPrice` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1693907033000` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| i | string |  | Average price interval<br>平均价格间隔<br>例: `5m` |
| w | string |  | Average price<br>平均价格<br>例: `25776.86000000` |
| T | integer (int64) |  | Last trade time<br>最后成交时间<br>例: `1693907032213` |

```json
{
  "e": "avgPrice",
  "E": 1693907033000,
  "s": "BTCUSDT",
  "i": "5m",
  "w": "25776.86000000",
  "T": 1693907032213
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@avgPrice` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `avgPrice` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1693907033000` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.i | string |  | Average price interval<br>平均价格间隔<br>例: `5m` |
| data.w | string |  | Average price<br>平均价格<br>例: `25776.86000000` |
| data.T | integer (int64) |  | Last trade time<br>最后成交时间<br>例: `1693907032213` |

```json
{
  "stream": "bnbusdt@avgPrice",
  "data": {
    "e": "avgPrice",
    "E": 1693907033000,
    "s": "BTCUSDT",
    "i": "5m",
    "w": "25776.86000000",
    "T": 1693907032213
  }
}
```

## Individual Symbol Book Ticker Streams（按Symbol的最优挂单信息）

流名称: `{symbol}@bookTicker`

Pushes any update to the best bid or ask's price or quantity in
real-time for a specified symbol.

Multiple `<symbol>@bookTicker` streams can be subscribed to over one
connection.

实时推送指定交易对最优挂单信息
多个 `<symbol>@bookTicker` 可以订阅在一个WebSocket连接上

更新速度: Real-time / 实时

Operation ID: `bookTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@bookTicker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Book Ticker Streams / 按Symbol的最优挂单信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| u | integer (int64) |  | Order book updateId<br>order book updateId<br>例: `400900217` |
| s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| b | string |  | Best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |

```json
{
  "u": 400900217,
  "s": "BNBUSDT",
  "b": "25.35190000",
  "B": "31.21000000",
  "a": "25.36520000",
  "A": "40.66000000"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@bookTicker` |
| data | object | 是 |  |
| data.u | integer (int64) |  | Order book updateId<br>order book updateId<br>例: `400900217` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data.b | string |  | Best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| data.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| data.a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| data.A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |

```json
{
  "stream": "bnbusdt@bookTicker",
  "data": {
    "u": 400900217,
    "s": "BNBUSDT",
    "b": "25.35190000",
    "B": "31.21000000",
    "a": "25.36520000",
    "A": "40.66000000"
  }
}
```

## Diff. Depth Stream（增量深度信息stream）

流名称: `{symbol}@depth@{updateSpeed}`

Order book price and quantity depth updates used to locally manage an order book.

每秒推送orderbook的变化部分（如果有）

更新速度: 1000ms or 100ms / 1000ms 或者 100ms

Operation ID: `diffBookDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |
| updateSpeed | path | string |  | Optional stream update speed suffix<br>可选的推送速度后缀<br>枚举: `100ms`<br>例: `100ms` |

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
    "bnbusdt@depth@100ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Diff. Depth Stream / 增量深度信息stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `157` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `160` |
| b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |

```json
{
  "e": "depthUpdate",
  "E": 1672515782136,
  "s": "BNBBTC",
  "U": 157,
  "u": 160,
  "b": [
    [
      "0.0024",
      "10"
    ]
  ],
  "a": [
    [
      "0.0026",
      "100"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@depth@100ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `157` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `160` |
| data.b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| data.a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |

```json
{
  "stream": "bnbusdt@depth@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1672515782136,
    "s": "BNBBTC",
    "U": 157,
    "u": 160,
    "b": [
      [
        "0.0024",
        "10"
      ]
    ],
    "a": [
      [
        "0.0026",
        "100"
      ]
    ]
  }
}
```

## Kline/Candlestick Streams for UTC（UTC K线）

流名称: `{symbol}@kline_{interval}`

The Kline/Candlestick Stream push updates to the current
klines/candlestick every second in `UTC+0` timezone

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+0` 时区的。

更新速度: 1000ms for `1s`, 2000ms for the other intervals / `1s` 1000ms，其它间隔 2000ms

Operation ID: `kline`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |
| interval | path | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |

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
    "bnbusdt@kline_1s"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Kline/Candlestick Streams for UTC / UTC K线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `kline` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| k | object |  | Kline payload<br>K线数据 |
| k.t | integer (int64) |  | Kline start time<br>该K线的起始时间<br>例: `1672515780000` |
| k.T | integer (int64) |  | Kline close time<br>该K线的结束时间<br>例: `1672515839999` |
| k.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | First trade ID<br>该K线期间第一笔成交ID<br>例: `100` |
| k.L | integer (int64) |  | Last trade ID<br>该K线期间末一笔成交ID<br>例: `200` |
| k.o | string |  | Open price<br>该K线期间第一笔成交价<br>例: `0.0010` |
| k.c | string |  | Close price<br>该K线期间末一笔成交价<br>例: `0.0020` |
| k.h | string |  | High price<br>该K线期间最高成交价<br>例: `0.0025` |
| k.l | string |  | Low price<br>该K线期间最低成交价<br>例: `0.0015` |
| k.v | string |  | Base asset volume<br>该K线期间成交量<br>例: `1000` |
| k.n | integer (int64) |  | Number of trades<br>该K线期间成交数量<br>例: `100` |
| k.x | boolean |  | Is this kline closed?<br>该K线是否完结（是否已经开始下一根K线）<br>例: `False` |
| k.q | string |  | Quote asset volume<br>该K线期间成交额<br>例: `1.0000` |
| k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "e": "kline",
  "E": 1672515782136,
  "s": "BNBBTC",
  "k": {
    "t": 1672515780000,
    "T": 1672515839999,
    "s": "BNBBTC",
    "i": "1m",
    "f": 100,
    "L": 200,
    "o": "0.0010",
    "c": "0.0020",
    "h": "0.0025",
    "l": "0.0015",
    "v": "1000",
    "n": 100,
    "x": false,
    "q": "1.0000",
    "V": "500",
    "Q": "0.500",
    "B": "123456"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@kline_1s` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `kline` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.k | object |  | Kline payload<br>K线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>该K线的起始时间<br>例: `1672515780000` |
| data.k.T | integer (int64) |  | Kline close time<br>该K线的结束时间<br>例: `1672515839999` |
| data.k.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | First trade ID<br>该K线期间第一笔成交ID<br>例: `100` |
| data.k.L | integer (int64) |  | Last trade ID<br>该K线期间末一笔成交ID<br>例: `200` |
| data.k.o | string |  | Open price<br>该K线期间第一笔成交价<br>例: `0.0010` |
| data.k.c | string |  | Close price<br>该K线期间末一笔成交价<br>例: `0.0020` |
| data.k.h | string |  | High price<br>该K线期间最高成交价<br>例: `0.0025` |
| data.k.l | string |  | Low price<br>该K线期间最低成交价<br>例: `0.0015` |
| data.k.v | string |  | Base asset volume<br>该K线期间成交量<br>例: `1000` |
| data.k.n | integer (int64) |  | Number of trades<br>该K线期间成交数量<br>例: `100` |
| data.k.x | boolean |  | Is this kline closed?<br>该K线是否完结（是否已经开始下一根K线）<br>例: `False` |
| data.k.q | string |  | Quote asset volume<br>该K线期间成交额<br>例: `1.0000` |
| data.k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| data.k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| data.k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "stream": "bnbusdt@kline_1s",
  "data": {
    "e": "kline",
    "E": 1672515782136,
    "s": "BNBBTC",
    "k": {
      "t": 1672515780000,
      "T": 1672515839999,
      "s": "BNBBTC",
      "i": "1m",
      "f": 100,
      "L": 200,
      "o": "0.0010",
      "c": "0.0020",
      "h": "0.0025",
      "l": "0.0015",
      "v": "1000",
      "n": 100,
      "x": false,
      "q": "1.0000",
      "V": "500",
      "Q": "0.500",
      "B": "123456"
    }
  }
}
```

## Kline/Candlestick Streams with timezone offset（带有时区偏移量的K线）

流名称: `{symbol}@kline_{interval}@+08:00`

The Kline/Candlestick Stream push updates to the current
klines/candlestick every second in `UTC+8` timezone

**Kline/Candlestick chart intervals:**

Supported intervals: See Kline/Candlestick chart intervals

**UTC+8 timezone offset:**

- Kline intervals open and close in the `UTC+8` timezone. For example the `1d` klines will open at the beginning of the `UTC+8` day, and close at the end of the `UTC+8` day.
- Note that `E` (event time), `t` (start time) and `T` (close time) in the payload are Unix timestamps, which are always interpreted in UTC.

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+8` 时区的。

**订阅Kline需要提供的间隔参数:**

参考 `Kline所支持的间隔参数`

**UTC+8 时区偏移量：**

- K线间隔的开始和结束时间会基于 `UTC+8` 时区。例如， `1d` K线将在 `UTC+8` 当天开始，并在 `UTC+8` 当日完结时随之结束。
- 请注意，Payload中的 `E`（event time），`t`（start time）和 `T`（close time）是 Unix 时间戳，它们始终以 UTC 格式解释。

更新速度: 1000ms for `1s`, 2000ms for the other intervals / `1s` 1000ms，其它间隔 2000ms

Operation ID: `klineOffset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |
| interval | path | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |

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
    "bnbusdt@kline_1s@+08:00"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Kline/Candlestick Streams with timezone offset / 带有时区偏移量的K线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `kline` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| k | object |  | Kline payload<br>K线数据 |
| k.t | integer (int64) |  | Kline start time<br>该K线的起始时间<br>例: `1672515780000` |
| k.T | integer (int64) |  | Kline close time<br>该K线的结束时间<br>例: `1672515839999` |
| k.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | First trade ID<br>该K线期间第一笔成交ID<br>例: `100` |
| k.L | integer (int64) |  | Last trade ID<br>该K线期间末一笔成交ID<br>例: `200` |
| k.o | string |  | Open price<br>该K线期间第一笔成交价<br>例: `0.0010` |
| k.c | string |  | Close price<br>该K线期间末一笔成交价<br>例: `0.0020` |
| k.h | string |  | High price<br>该K线期间最高成交价<br>例: `0.0025` |
| k.l | string |  | Low price<br>该K线期间最低成交价<br>例: `0.0015` |
| k.v | string |  | Base asset volume<br>该K线期间成交量<br>例: `1000` |
| k.n | integer (int64) |  | Number of trades<br>该K线期间成交数量<br>例: `100` |
| k.x | boolean |  | Is this kline closed?<br>该K线是否完结（是否已经开始下一根K线）<br>例: `False` |
| k.q | string |  | Quote asset volume<br>该K线期间成交额<br>例: `1.0000` |
| k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "e": "kline",
  "E": 1672515782136,
  "s": "BNBBTC",
  "k": {
    "t": 1672515780000,
    "T": 1672515839999,
    "s": "BNBBTC",
    "i": "1m",
    "f": 100,
    "L": 200,
    "o": "0.0010",
    "c": "0.0020",
    "h": "0.0025",
    "l": "0.0015",
    "v": "1000",
    "n": 100,
    "x": false,
    "q": "1.0000",
    "V": "500",
    "Q": "0.500",
    "B": "123456"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@kline_1s@+08:00` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `kline` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.k | object |  | Kline payload<br>K线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>该K线的起始时间<br>例: `1672515780000` |
| data.k.T | integer (int64) |  | Kline close time<br>该K线的结束时间<br>例: `1672515839999` |
| data.k.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | First trade ID<br>该K线期间第一笔成交ID<br>例: `100` |
| data.k.L | integer (int64) |  | Last trade ID<br>该K线期间末一笔成交ID<br>例: `200` |
| data.k.o | string |  | Open price<br>该K线期间第一笔成交价<br>例: `0.0010` |
| data.k.c | string |  | Close price<br>该K线期间末一笔成交价<br>例: `0.0020` |
| data.k.h | string |  | High price<br>该K线期间最高成交价<br>例: `0.0025` |
| data.k.l | string |  | Low price<br>该K线期间最低成交价<br>例: `0.0015` |
| data.k.v | string |  | Base asset volume<br>该K线期间成交量<br>例: `1000` |
| data.k.n | integer (int64) |  | Number of trades<br>该K线期间成交数量<br>例: `100` |
| data.k.x | boolean |  | Is this kline closed?<br>该K线是否完结（是否已经开始下一根K线）<br>例: `False` |
| data.k.q | string |  | Quote asset volume<br>该K线期间成交额<br>例: `1.0000` |
| data.k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| data.k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| data.k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "stream": "bnbusdt@kline_1s@+08:00",
  "data": {
    "e": "kline",
    "E": 1672515782136,
    "s": "BNBBTC",
    "k": {
      "t": 1672515780000,
      "T": 1672515839999,
      "s": "BNBBTC",
      "i": "1m",
      "f": 100,
      "L": 200,
      "o": "0.0010",
      "c": "0.0020",
      "h": "0.0025",
      "l": "0.0015",
      "v": "1000",
      "n": 100,
      "x": false,
      "q": "1.0000",
      "V": "500",
      "Q": "0.500",
      "B": "123456"
    }
  }
}
```

## Individual Symbol Mini Ticker Stream（按Symbol的精简Ticker）

流名称: `{symbol}@miniTicker`

24hr rolling window mini-ticker statistics. These are NOT the statistics
of the UTC day, but a 24hr rolling window for the previous 24hrs.

按Symbol逐秒刷新的24小时精简ticker信息

更新速度: 1000ms

Operation ID: `miniTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@miniTicker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Mini Ticker Stream / 按Symbol的精简Ticker

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |

```json
{
  "e": "24hrMiniTicker",
  "E": 1672515782136,
  "s": "BNBBTC",
  "c": "0.0025",
  "o": "0.0010",
  "h": "0.0025",
  "l": "0.0010",
  "v": "10000",
  "q": "18"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@miniTicker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| data.o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data.v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| data.q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |

```json
{
  "stream": "bnbusdt@miniTicker",
  "data": {
    "e": "24hrMiniTicker",
    "E": 1672515782136,
    "s": "BNBBTC",
    "c": "0.0025",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18"
  }
}
```

## Partial Book Depth Streams（有限档深度信息）

流名称: `{symbol}@depth{levels}@{updateSpeed}`

Top **\<levels\>** bids and asks, pushed every second. Valid **\<levels\>** are 5, 10, or 20.

每秒推送有限档深度信息。levels 表示几档买卖单信息, 可选 5/10/20档

更新速度: 1000ms or 100ms / 1000ms 或者 100ms

Operation ID: `partialBookDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |
| levels | path | string | 是 | 枚举: `5`, `10`, `20`<br>例: `5` |
| updateSpeed | path | string |  | Optional stream update speed suffix<br>可选的推送速度后缀<br>枚举: `100ms`<br>例: `100ms` |

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
    "bnbusdt@depth5@100ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Partial Book Depth Streams / 有限档深度信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| lastUpdateId | integer (int64) |  | Last update ID<br>末次更新ID<br>例: `160` |
| bids | oneOf[][] |  | Bids to be updated<br>买单 |
| asks | oneOf[][] |  | Asks to be updated<br>卖单 |

```json
{
  "lastUpdateId": 160,
  "bids": [
    [
      "0.0024",
      "10"
    ]
  ],
  "asks": [
    [
      "0.0026",
      "100"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@depth5@100ms` |
| data | object | 是 |  |
| data.lastUpdateId | integer (int64) |  | Last update ID<br>末次更新ID<br>例: `160` |
| data.bids | oneOf[][] |  | Bids to be updated<br>买单 |
| data.asks | oneOf[][] |  | Asks to be updated<br>卖单 |

```json
{
  "stream": "bnbusdt@depth5@100ms",
  "data": {
    "lastUpdateId": 160,
    "bids": [
      [
        "0.0024",
        "10"
      ]
    ],
    "asks": [
      [
        "0.0026",
        "100"
      ]
    ]
  }
}
```

## Reference Price Streams（参考价格数据流）

流名称: `{symbol}@referencePrice`

Reference price stream for a symbol.

推送交易对参考价格信息。

更新速度: 1000ms

Operation ID: `referencePrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bazusd` |

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
    "bazusd@referencePrice"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Reference Price Streams / 参考价格数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `referencePrice` |
| s | string |  | Symbol<br>交易对<br>例: `BAZUSD` |
| r | string |  | Reference price (null if no reference price)<br>参考价格（如果无参考价格则为 null）<br>例: `1.00` |
| t | integer (int64) |  | Engine timestamp when reference price was valid<br>参考价格生效时的撮合引擎时间<br>例: `1770313263917` |

```json
{
  "e": "referencePrice",
  "s": "BAZUSD",
  "r": "1.00",
  "t": 1770313263917
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bazusd@referencePrice` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `referencePrice` |
| data.s | string |  | Symbol<br>交易对<br>例: `BAZUSD` |
| data.r | string |  | Reference price (null if no reference price)<br>参考价格（如果无参考价格则为 null）<br>例: `1.00` |
| data.t | integer (int64) |  | Engine timestamp when reference price was valid<br>参考价格生效时的撮合引擎时间<br>例: `1770313263917` |

```json
{
  "stream": "bazusd@referencePrice",
  "data": {
    "e": "referencePrice",
    "s": "BAZUSD",
    "r": "1.00",
    "t": 1770313263917
  }
}
```

## Individual Symbol Rolling Window Statistics Streams（按Symbol的滚动窗口统计）

流名称: `{symbol}@ticker_{windowSize}`

Rolling window ticker statistics for a single symbol, computed over
multiple windows.

**Note:** This stream is different from the `<symbol>@ticker` stream. The open time `"O"` always starts on a minute, while the closing time `"C"` is the current time
of the update. As such, the effective window might be up to 59999ms wider than `<windowSize>`.

单个symbol的滚动窗口统计, 支持多个时间窗口。

**注意:**

- 该数据流和 `<symbol>@ticker` 不一样。
- `O` (`open time`) 会在每分钟整点开始, 而 `C` (`closing time`)是当前更新时间。
- 实际统计的时间范围会比 `<windowSize>` 多不超过59999ms。

更新速度: 1000ms

Operation ID: `rollingWindowTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |
| windowSize | path | string | 是 | 枚举: `1h`, `4h`, `1d`<br>例: `1h` |

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
    "bnbusdt@ticker_1h"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Rolling Window Statistics Streams / 按Symbol的滚动窗口统计

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `1hTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| p | string |  | Price change<br>价格变化<br>例: `0.0015` |
| P | string |  | Price change percent<br>价格变化百分比<br>例: `250.00` |
| o | string |  | Open price<br>开盘价<br>例: `0.0010` |
| h | string |  | High price<br>最高价<br>例: `0.0025` |
| l | string |  | Low price<br>最低价<br>例: `0.0010` |
| c | string |  | Last price<br>最新价<br>例: `0.0025` |
| w | string |  | Weighted average price<br>加权平均价格<br>例: `0.0018` |
| v | string |  | Total traded base asset volume<br>总成交基础资产量<br>例: `10000` |
| q | string |  | Total traded quote asset volume<br>总成交计价资产量<br>例: `18` |
| O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| F | integer (int64) |  | First trade ID<br>第一笔成交ID<br>例: `0` |
| L | integer (int64) |  | Last trade Id<br>最后一笔成交ID<br>例: `18150` |
| n | integer (int64) |  | Total number of trades<br>总成交笔数<br>例: `18151` |

```json
{
  "e": "1hTicker",
  "E": 1672515782136,
  "s": "BNBBTC",
  "p": "0.0015",
  "P": "250.00",
  "o": "0.0010",
  "h": "0.0025",
  "l": "0.0010",
  "c": "0.0025",
  "w": "0.0018",
  "v": "10000",
  "q": "18",
  "O": 0,
  "C": 1675216573749,
  "F": 0,
  "L": 18150,
  "n": 18151
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@ticker_1h` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `1hTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.p | string |  | Price change<br>价格变化<br>例: `0.0015` |
| data.P | string |  | Price change percent<br>价格变化百分比<br>例: `250.00` |
| data.o | string |  | Open price<br>开盘价<br>例: `0.0010` |
| data.h | string |  | High price<br>最高价<br>例: `0.0025` |
| data.l | string |  | Low price<br>最低价<br>例: `0.0010` |
| data.c | string |  | Last price<br>最新价<br>例: `0.0025` |
| data.w | string |  | Weighted average price<br>加权平均价格<br>例: `0.0018` |
| data.v | string |  | Total traded base asset volume<br>总成交基础资产量<br>例: `10000` |
| data.q | string |  | Total traded quote asset volume<br>总成交计价资产量<br>例: `18` |
| data.O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| data.C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| data.F | integer (int64) |  | First trade ID<br>第一笔成交ID<br>例: `0` |
| data.L | integer (int64) |  | Last trade Id<br>最后一笔成交ID<br>例: `18150` |
| data.n | integer (int64) |  | Total number of trades<br>总成交笔数<br>例: `18151` |

```json
{
  "stream": "bnbusdt@ticker_1h",
  "data": {
    "e": "1hTicker",
    "E": 1672515782136,
    "s": "BNBBTC",
    "p": "0.0015",
    "P": "250.00",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "c": "0.0025",
    "w": "0.0018",
    "v": "10000",
    "q": "18",
    "O": 0,
    "C": 1675216573749,
    "F": 0,
    "L": 18150,
    "n": 18151
  }
}
```

## Individual Symbol Ticker Streams（按Symbol的完整Ticker）

流名称: `{symbol}@ticker`

24hr rolling window ticker statistics for a single symbol. These are NOT
the statistics of the UTC day, but a 24hr rolling window for the
previous 24hrs.

按Symbol逐秒刷新的24小时完整ticker信息

更新速度: 1000ms

Operation ID: `ticker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@ticker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Ticker Streams / 按Symbol的完整Ticker

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| P | string |  | Price change percent<br>24小时价格变化（百分比）<br>例: `250.00` |
| w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| x | string |  | First trade(F)-1 price (first trade before the 24hr rolling window)<br>整整24小时之前，向前数的最后一次成交价格<br>例: `0.0009` |
| c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| Q | string |  | Last quantity<br>最新成交交易的成交量<br>例: `10` |
| b | string |  | Best bid price<br>目前最高买单价<br>例: `0.0024` |
| B | string |  | Best bid quantity<br>目前最高买单价的挂单量<br>例: `10` |
| a | string |  | Best ask price<br>目前最低卖单价<br>例: `0.0026` |
| A | string |  | Best ask quantity<br>目前最低卖单价的挂单量<br>例: `100` |
| o | string |  | Open price<br>整整24小时前，向后数的第一次成交价格<br>例: `0.0010` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |

```json
{
  "e": "24hrTicker",
  "E": 1672515782136,
  "s": "BNBBTC",
  "p": "0.0015",
  "P": "250.00",
  "w": "0.0018",
  "x": "0.0009",
  "c": "0.0025",
  "Q": "10",
  "b": "0.0024",
  "B": "10",
  "a": "0.0026",
  "A": "100",
  "o": "0.0010",
  "h": "0.0025",
  "l": "0.0010",
  "v": "10000",
  "q": "18",
  "O": 0,
  "C": 1675216573749,
  "F": 0,
  "L": 18150,
  "n": 18151
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@ticker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| data.P | string |  | Price change percent<br>24小时价格变化（百分比）<br>例: `250.00` |
| data.w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| data.x | string |  | First trade(F)-1 price (first trade before the 24hr rolling window)<br>整整24小时之前，向前数的最后一次成交价格<br>例: `0.0009` |
| data.c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| data.Q | string |  | Last quantity<br>最新成交交易的成交量<br>例: `10` |
| data.b | string |  | Best bid price<br>目前最高买单价<br>例: `0.0024` |
| data.B | string |  | Best bid quantity<br>目前最高买单价的挂单量<br>例: `10` |
| data.a | string |  | Best ask price<br>目前最低卖单价<br>例: `0.0026` |
| data.A | string |  | Best ask quantity<br>目前最低卖单价的挂单量<br>例: `100` |
| data.o | string |  | Open price<br>整整24小时前，向后数的第一次成交价格<br>例: `0.0010` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data.v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| data.q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| data.O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| data.C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1675216573749` |
| data.F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| data.L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| data.n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |

```json
{
  "stream": "bnbusdt@ticker",
  "data": {
    "e": "24hrTicker",
    "E": 1672515782136,
    "s": "BNBBTC",
    "p": "0.0015",
    "P": "250.00",
    "w": "0.0018",
    "x": "0.0009",
    "c": "0.0025",
    "Q": "10",
    "b": "0.0024",
    "B": "10",
    "a": "0.0026",
    "A": "100",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18",
    "O": 0,
    "C": 1675216573749,
    "F": 0,
    "L": 18150,
    "n": 18151
  }
}
```

## Trade Streams（逐笔交易）

流名称: `{symbol}@trade`

The Trade Streams push raw trade information; each trade has a unique
buyer and seller.

逐笔交易推送每一笔成交的信息。**成交**，或者说交易的定义是仅有一个吃单者与一个挂单者相互交易。

更新速度: Real-time / 实时

Operation ID: `trade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@trade"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Trade Streams / 逐笔交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `trade` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| t | integer (int64) |  | Trade ID<br>交易ID<br>例: `12345` |
| p | string |  | Price<br>成交价格<br>例: `0.001` |
| q | string |  | Quantity<br>成交数量<br>例: `100` |
| T | integer (int64) |  | Trade time<br>成交时间<br>例: `1672515782136` |
| m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| M | boolean |  | Ignore<br>请忽略该字段<br>例: `True` |

```json
{
  "e": "trade",
  "E": 1672515782136,
  "s": "BNBBTC",
  "t": 12345,
  "p": "0.001",
  "q": "100",
  "T": 1672515782136,
  "m": true,
  "M": true
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@trade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `trade` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1672515782136` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.t | integer (int64) |  | Trade ID<br>交易ID<br>例: `12345` |
| data.p | string |  | Price<br>成交价格<br>例: `0.001` |
| data.q | string |  | Quantity<br>成交数量<br>例: `100` |
| data.T | integer (int64) |  | Trade time<br>成交时间<br>例: `1672515782136` |
| data.m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| data.M | boolean |  | Ignore<br>请忽略该字段<br>例: `True` |

```json
{
  "stream": "bnbusdt@trade",
  "data": {
    "e": "trade",
    "E": 1672515782136,
    "s": "BNBBTC",
    "t": 12345,
    "p": "0.001",
    "q": "100",
    "T": 1672515782136,
    "m": true,
    "M": true
  }
}
```

## Block Trade Streams（大宗交易）

流名称: `{symbol}@blockTrade`

Block Trade Streams push block trade information in real-time.

大宗交易推送实时的大宗交易信息。

更新速度: Real-time / 实时

Operation ID: `blockTrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Symbol to query<br>要查询的交易对<br>例: `bnbusdt` |

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
    "bnbusdt@blockTrade"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Block Trade Streams / 大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `blockTrade` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1772506983582` |
| s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| t | integer (int64) |  | Block Trade ID<br>大宗交易ID<br>例: `582` |
| p | string |  | Price<br>成交价格<br>例: `0.052` |
| q | string |  | Quantity<br>成交数量<br>例: `5838` |
| T | integer (int64) |  | Trade time<br>成交时间<br>例: `1772506983321` |
| m | boolean |  | Is the buyer the maker?<br>买方是否是做市方。<br>例: `True` |

```json
{
  "e": "blockTrade",
  "E": 1772506983582,
  "s": "BNBBTC",
  "t": 582,
  "p": "0.052",
  "q": "5838",
  "T": 1772506983321,
  "m": true
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `bnbusdt@blockTrade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `blockTrade` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1772506983582` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBBTC` |
| data.t | integer (int64) |  | Block Trade ID<br>大宗交易ID<br>例: `582` |
| data.p | string |  | Price<br>成交价格<br>例: `0.052` |
| data.q | string |  | Quantity<br>成交数量<br>例: `5838` |
| data.T | integer (int64) |  | Trade time<br>成交时间<br>例: `1772506983321` |
| data.m | boolean |  | Is the buyer the maker?<br>买方是否是做市方。<br>例: `True` |

```json
{
  "stream": "bnbusdt@blockTrade",
  "data": {
    "e": "blockTrade",
    "E": 1772506983582,
    "s": "BNBBTC",
    "t": 582,
    "p": "0.052",
    "q": "5838",
    "T": 1772506983321,
    "m": true
  }
}
```