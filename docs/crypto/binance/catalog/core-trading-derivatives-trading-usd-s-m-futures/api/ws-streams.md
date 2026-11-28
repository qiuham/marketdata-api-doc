---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-28 18:46:59.207170
---

# Futures (USDⓈ-M) WebSocket Market Streams

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-streams/1.0.0/schema.yaml

Access market data, manage accounts, and trade USDⓈ-M perpetual futures.

访问市场数据、管理账户，并交易 USDⓈ-M 永续合约。

版本: 1.0.0

## 服务地址

- `wss://fstream.binance.com`
- `wss://stream.binancefuture.com`

## 接口列表

- `{symbol}@aggTrade` — Aggregate Trade Streams
- `!forceOrder@arr` — All Market Liquidation Order Streams
- `!miniTicker@arr` — All Market Mini Tickers Stream
- `!ticker@arr` — All Market Tickers Streams
- `{symbol}@compositeIndex` — Composite Index Symbol Information Streams
- `{pair}_{contractType}@continuousKline_{interval}` — Continuous Contract Kline/Candlestick Streams
- `!contractInfo` — Contract Info Stream
- `{symbol}@miniTicker` — Individual Symbol Mini Ticker Stream
- `{symbol}@ticker` — Individual Symbol Ticker Streams
- `{symbol}@kline_{interval}` — Kline/Candlestick Streams
- `{symbol}@forceOrder` — Liquidation Order Streams
- `{symbol}@markPrice@{updateSpeed}` — Mark Price Stream
- `!markPrice@arr@{updateSpeed}` — Mark Price Stream for All market
- `!assetIndex@arr` — Multi-Assets Mode Asset Index
- `tradingSession` — Trading Session Stream
- `!bookTicker` — All Book Tickers Stream
- `{symbol}@depth@{updateSpeed}` — Diff. Book Depth Streams
- `{symbol}@bookTicker` — Individual Symbol Book Ticker Streams
- `{symbol}@depth{levels}@{updateSpeed}` — Partial Book Depth Streams
- `{symbol}@rpiDepth@500ms` — RPI Diff. Book Depth Streams

## Aggregate Trade Streams（归集交易）

流名称: `{symbol}@aggTrade`

The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds. Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

归集交易流每100毫秒推送一次市场交易信息，这些信息是针对相同价格和方向的成交进行归集的。只有市场交易会被归集，保险基金交易和ADL交易不会被归集。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 100ms

Operation ID: `aggregateTradeStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@aggTrade"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Aggregate Trade Streams / 归集成交流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| a | integer (int64) |  | Aggregate trade ID<br>归集成交 ID<br>例: `5933014` |
| p | string |  | Price<br>成交价格<br>例: `0.001` |
| q | string |  | Quantity with all the market trades<br>成交量，包含RPI订单数据<br>例: `100` |
| nq | string |  | Normal quantity without the trades involving RPI orders<br>普通订单成交量，不包含RPI订单数据<br>例: `100` |
| f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `100` |
| l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `105` |
| T | integer (int64) |  | Trade time<br>成交时间<br>例: `123456785` |
| m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "aggTrade",
  "E": 123456789,
  "s": "BNBUSDT",
  "a": 5933014,
  "p": "0.001",
  "q": "100",
  "nq": "100",
  "f": 100,
  "l": 105,
  "T": 123456785,
  "m": true,
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@aggTrade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data.a | integer (int64) |  | Aggregate trade ID<br>归集成交 ID<br>例: `5933014` |
| data.p | string |  | Price<br>成交价格<br>例: `0.001` |
| data.q | string |  | Quantity with all the market trades<br>成交量，包含RPI订单数据<br>例: `100` |
| data.nq | string |  | Normal quantity without the trades involving RPI orders<br>普通订单成交量，不包含RPI订单数据<br>例: `100` |
| data.f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `100` |
| data.l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `105` |
| data.T | integer (int64) |  | Trade time<br>成交时间<br>例: `123456785` |
| data.m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `True` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@aggTrade",
  "data": {
    "e": "aggTrade",
    "E": 123456789,
    "s": "BNBUSDT",
    "a": 5933014,
    "p": "0.001",
    "q": "100",
    "nq": "100",
    "f": 100,
    "l": 105,
    "T": 123456785,
    "m": true,
    "st": 1
  }
}
```

## All Market Liquidation Order Streams（全市场强平订单）

流名称: `!forceOrder@arr`

The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market. For each symbol，only the largest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

全市场强平订单快照流推送市场上所有交易对的强平订单信息。对于每个交易对，在1000毫秒内只会推送最大的一笔强平订单作为快照。如果在1000毫秒的时间间隔内没有发生强平，则不会推送任何流。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 1000ms

Operation ID: `allMarketLiquidationOrderStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "!forceOrder@arr"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：All Market Liquidation Order Streams / 全市场强平订单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event Type<br>事件类型<br>例: `forceOrder` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1568014460893` |
| o | object |  | Order Type<br>订单类型 |
| o.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| o.q | string |  | Original Quantity<br>订单数量<br>例: `0.014` |
| o.p | string |  | Price<br>订单价格<br>例: `9910` |
| o.ap | string |  | Average Price<br>平均价格<br>例: `9910` |
| o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `0.014` |
| o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `0.014` |
| o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1568014460893` |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "forceOrder",
  "E": 1568014460893,
  "o": {
    "s": "BTCUSDT",
    "S": "SELL",
    "o": "LIMIT",
    "f": "IOC",
    "q": "0.014",
    "p": "9910",
    "ap": "9910",
    "X": "FILLED",
    "l": "0.014",
    "z": "0.014",
    "T": 1568014460893
  },
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!forceOrder@arr` |
| data | object | 是 |  |
| data.e | string |  | Event Type<br>事件类型<br>例: `forceOrder` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1568014460893` |
| data.o | object |  | Order Type<br>订单类型 |
| data.o.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| data.o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| data.o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| data.o.q | string |  | Original Quantity<br>订单数量<br>例: `0.014` |
| data.o.p | string |  | Price<br>订单价格<br>例: `9910` |
| data.o.ap | string |  | Average Price<br>平均价格<br>例: `9910` |
| data.o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| data.o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `0.014` |
| data.o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `0.014` |
| data.o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1568014460893` |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!forceOrder@arr",
  "data": {
    "e": "forceOrder",
    "E": 1568014460893,
    "o": {
      "s": "BTCUSDT",
      "S": "SELL",
      "o": "LIMIT",
      "f": "IOC",
      "q": "0.014",
      "p": "9910",
      "ap": "9910",
      "X": "FILLED",
      "l": "0.014",
      "z": "0.014",
      "T": 1568014460893
    },
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## All Market Mini Tickers Stream（全市场的精简Ticker）

流名称: `!miniTicker@arr`

24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

所有交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 1000ms

Operation ID: `allMarketMiniTickersStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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

### 响应 Raw Stream：All Market Mini Tickers Stream / 全市场精简行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间(毫秒)<br>例: `123456789` |
| [].s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| [].c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| [].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| [].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| [].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| [].v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| [].q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |
| [].ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "24hrMiniTicker",
    "E": 123456789,
    "s": "BNBUSDT",
    "c": "0.0025",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18",
    "ps": "BTCUSDT",
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!miniTicker@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间(毫秒)<br>例: `123456789` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data[].c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| data[].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| data[].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data[].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data[].v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| data[].q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |
| data[].ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!miniTicker@arr",
  "data": [
    {
      "e": "24hrMiniTicker",
      "E": 123456789,
      "s": "BNBUSDT",
      "c": "0.0025",
      "o": "0.0010",
      "h": "0.0025",
      "l": "0.0010",
      "v": "10000",
      "q": "18",
      "ps": "BTCUSDT",
      "st": 1
    }
  ]
}
```

## All Market Tickers Streams（全市场的完整Ticker）

流名称: `!ticker@arr`

24hr rolling window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

所有交易对的24小时滚动窗口完整Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 1000ms

Operation ID: `allMarketTickersStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "!ticker@arr"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：All Market Tickers Streams / 全市场行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| [].s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| [].p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| [].P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `250.00` |
| [].w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| [].c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| [].Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `10` |
| [].o | string |  | Open price<br>24小时内第一比成交的价格<br>例: `0.0010` |
| [].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| [].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| [].v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| [].q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| [].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| [].C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `86400000` |
| [].F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| [].L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| [].n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |
| [].ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "24hrTicker",
    "E": 123456789,
    "s": "BNBUSDT",
    "p": "0.0015",
    "P": "250.00",
    "w": "0.0018",
    "c": "0.0025",
    "Q": "10",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18",
    "O": 0,
    "C": 86400000,
    "F": 0,
    "L": 18150,
    "n": 18151,
    "ps": "BTCUSDT",
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!ticker@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data[].p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| data[].P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `250.00` |
| data[].w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| data[].c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| data[].Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `10` |
| data[].o | string |  | Open price<br>24小时内第一比成交的价格<br>例: `0.0010` |
| data[].h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data[].l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data[].v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| data[].q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| data[].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| data[].C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `86400000` |
| data[].F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| data[].L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| data[].n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |
| data[].ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!ticker@arr",
  "data": [
    {
      "e": "24hrTicker",
      "E": 123456789,
      "s": "BNBUSDT",
      "p": "0.0015",
      "P": "250.00",
      "w": "0.0018",
      "c": "0.0025",
      "Q": "10",
      "o": "0.0010",
      "h": "0.0025",
      "l": "0.0010",
      "v": "10000",
      "q": "18",
      "O": 0,
      "C": 86400000,
      "F": 0,
      "L": 18150,
      "n": 18151,
      "ps": "BTCUSDT",
      "st": 1
    }
  ]
}
```

## Composite Index Symbol Information Streams（综合指数交易对信息流）

流名称: `{symbol}@compositeIndex`

Composite index information for index symbols pushed every second.

综合指数交易对的指数信息，每秒推送一次。

更新速度: 1000ms

Operation ID: `compositeIndexSymbolInformationStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@compositeIndex"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Composite Index Symbol Information Streams / 复合指数交易对信息流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `compositeIndex` |
| E | integer (int64) |  | Event time<br>事件事件<br>例: `1602310596000` |
| s | string |  | Symbol<br>交易对<br>例: `DEFIUSDT` |
| p | string |  | Price<br>价格<br>例: `554.41604065` |
| C | string |  | Base asset category.<br>基础资产类别。<br>例: `baseAsset` |
| c | object[] |  | Composition<br>成分信息 |
| c[].b | string |  | Base asset<br>基础资产<br>例: `BAL` |
| c[].q | string |  | Quote asset<br>报价资产<br>例: `USDT` |
| c[].w | string |  | Weight in quantity<br>权重(数量)<br>例: `1.04884844` |
| c[].W | string |  | Weight in percentage<br>权重(比例)<br>例: `0.01457800` |
| c[].i | string |  | Index price<br>指数价格<br>例: `24.33521021` |

```json
{
  "e": "compositeIndex",
  "E": 1602310596000,
  "s": "DEFIUSDT",
  "p": "554.41604065",
  "C": "baseAsset",
  "c": [
    {
      "b": "BAL",
      "q": "USDT",
      "w": "1.04884844",
      "W": "0.01457800",
      "i": "24.33521021"
    }
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@compositeIndex` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `compositeIndex` |
| data.E | integer (int64) |  | Event time<br>事件事件<br>例: `1602310596000` |
| data.s | string |  | Symbol<br>交易对<br>例: `DEFIUSDT` |
| data.p | string |  | Price<br>价格<br>例: `554.41604065` |
| data.C | string |  | Base asset category.<br>基础资产类别。<br>例: `baseAsset` |
| data.c | object[] |  | Composition<br>成分信息 |
| data.c[].b | string |  | Base asset<br>基础资产<br>例: `BAL` |
| data.c[].q | string |  | Quote asset<br>报价资产<br>例: `USDT` |
| data.c[].w | string |  | Weight in quantity<br>权重(数量)<br>例: `1.04884844` |
| data.c[].W | string |  | Weight in percentage<br>权重(比例)<br>例: `0.01457800` |
| data.c[].i | string |  | Index price<br>指数价格<br>例: `24.33521021` |

```json
{
  "stream": "btcusdt@compositeIndex",
  "data": {
    "e": "compositeIndex",
    "E": 1602310596000,
    "s": "DEFIUSDT",
    "p": "554.41604065",
    "C": "baseAsset",
    "c": [
      {
        "b": "BAL",
        "q": "USDT",
        "w": "1.04884844",
        "W": "0.01457800",
        "i": "24.33521021"
      }
    ]
  }
}
```

## Continuous Contract Kline/Candlestick Streams（连续合约K线）

流名称: `{pair}_{contractType}@continuousKline_{interval}`

Continuous Contract Kline/Candlestick Streams

> **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

连续合约K线

> **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 250ms

Operation ID: `continuousContractKlineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| pair | path | string | 是 | 例: `btcusdt` |
| contractType | path | string | 是 | 枚举: `perpetual`, `current_quarter`, `next_quarter`, `tradifi_perpetual`<br>例: `next_quarter` |
| interval | path | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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
    "btcusdt_next_quarter@continuousKline_1m"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Continuous Contract Kline/Candlestick Streams / 连续合约 K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `continuous_kline` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1607443058651` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSDT` |
| ct | string |  | Contract type<br>合约类型<br>例: `PERPETUAL` |
| k | object |  | Kline payload.<br>K 线数据。 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1607443020000` |
| k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1607443079999` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | First updateId<br>这根K线期间第一笔更新ID<br>例: `116467658886` |
| k.L | integer (int64) |  | Last updateId<br>这根K线期间末一笔更新ID<br>例: `116468012423` |
| k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `18787.00` |
| k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `18804.04` |
| k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `18804.04` |
| k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `18786.54` |
| k.v | string |  | volume<br>这根K线期间成交量<br>例: `197.664` |
| k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `543` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | Quote asset volume<br>这根K线期间成交额<br>例: `3715253.19494` |
| k.V | string |  | Taker buy volume<br>主动买入的成交量<br>例: `184.769` |
| k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `3472925.84746` |
| k.B | string |  | Ignore<br>忽略此参数<br>例: `0` |

```json
{
  "e": "continuous_kline",
  "E": 1607443058651,
  "ps": "BTCUSDT",
  "ct": "PERPETUAL",
  "k": {
    "t": 1607443020000,
    "T": 1607443079999,
    "i": "1m",
    "f": 116467658886,
    "L": 116468012423,
    "o": "18787.00",
    "c": "18804.04",
    "h": "18804.04",
    "l": "18786.54",
    "v": "197.664",
    "n": 543,
    "x": false,
    "q": "3715253.19494",
    "V": "184.769",
    "Q": "3472925.84746",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt_next_quarter@continuousKline_1m` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `continuous_kline` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1607443058651` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSDT` |
| data.ct | string |  | Contract type<br>合约类型<br>例: `PERPETUAL` |
| data.k | object |  | Kline payload.<br>K 线数据。 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1607443020000` |
| data.k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1607443079999` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | First updateId<br>这根K线期间第一笔更新ID<br>例: `116467658886` |
| data.k.L | integer (int64) |  | Last updateId<br>这根K线期间末一笔更新ID<br>例: `116468012423` |
| data.k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `18787.00` |
| data.k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `18804.04` |
| data.k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `18804.04` |
| data.k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `18786.54` |
| data.k.v | string |  | volume<br>这根K线期间成交量<br>例: `197.664` |
| data.k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `543` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | Quote asset volume<br>这根K线期间成交额<br>例: `3715253.19494` |
| data.k.V | string |  | Taker buy volume<br>主动买入的成交量<br>例: `184.769` |
| data.k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `3472925.84746` |
| data.k.B | string |  | Ignore<br>忽略此参数<br>例: `0` |

```json
{
  "stream": "btcusdt_next_quarter@continuousKline_1m",
  "data": {
    "e": "continuous_kline",
    "E": 1607443058651,
    "ps": "BTCUSDT",
    "ct": "PERPETUAL",
    "k": {
      "t": 1607443020000,
      "T": 1607443079999,
      "i": "1m",
      "f": 116467658886,
      "L": 116468012423,
      "o": "18787.00",
      "c": "18804.04",
      "h": "18804.04",
      "l": "18786.54",
      "v": "197.664",
      "n": 543,
      "x": false,
      "q": "3715253.19494",
      "V": "184.769",
      "Q": "3472925.84746",
      "B": "0"
    }
  }
}
```

## Contract Info Stream（合约信息流）

流名称: `!contractInfo`

ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). bks field only shows up when bracket gets updated.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

当合约信息更新（上新/结算/档位更新）时推送；`bks` 字段仅在档位更新时出现。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: Real-time

Operation ID: `contractInfoStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "!contractInfo"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Contract Info Stream / 合约信息流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type.<br>事件类型。<br>例: `contractInfo` |
| E | integer (int64) |  | Event time.<br>事件时间。<br>例: `1669356423908` |
| s | string |  | Symbol.<br>交易对。<br>例: `IOTAUSDT` |
| ct | string |  | Contract type.<br>合约类型。<br>例: `PERPETUAL` |
| dt | integer (int64) |  | Delivery date time.<br>交割时间。<br>例: `4133404800000` |
| ot | integer (int64) |  | Onboard date time.<br>上线时间。<br>例: `1569398400000` |
| cs | string |  | Contract status.<br>合约状态。<br>例: `TRADING` |
| bks | object[] |  | Notional bracket updates.<br>名义价值档位更新。 |
| bks[].bs | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| bks[].bnf | integer (int64) |  | Floor notional of this bracket<br>该层对应的名义价值下限<br>例: `0` |
| bks[].bnc | integer (int64) |  | Cap notional of this bracket<br>该层对应的名义价值上限<br>例: `5000` |
| bks[].mmr | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.01` |
| bks[].cf | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `0` |
| bks[].mi | integer (int64) |  | Min leverage for this bracket<br>该层杠杆下界<br>例: `21` |
| bks[].ma | integer (int64) |  | Max leverage for this bracket<br>该层杠杆上界<br>例: `50` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "contractInfo",
  "E": 1669356423908,
  "s": "IOTAUSDT",
  "ct": "PERPETUAL",
  "dt": 4133404800000,
  "ot": 1569398400000,
  "cs": "TRADING",
  "bks": [
    {
      "bs": 1,
      "bnf": 0,
      "bnc": 5000,
      "mmr": 0.01,
      "cf": 0,
      "mi": 21,
      "ma": 50
    }
  ],
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!contractInfo` |
| data | object | 是 |  |
| data.e | string |  | Event type.<br>事件类型。<br>例: `contractInfo` |
| data.E | integer (int64) |  | Event time.<br>事件时间。<br>例: `1669356423908` |
| data.s | string |  | Symbol.<br>交易对。<br>例: `IOTAUSDT` |
| data.ct | string |  | Contract type.<br>合约类型。<br>例: `PERPETUAL` |
| data.dt | integer (int64) |  | Delivery date time.<br>交割时间。<br>例: `4133404800000` |
| data.ot | integer (int64) |  | Onboard date time.<br>上线时间。<br>例: `1569398400000` |
| data.cs | string |  | Contract status.<br>合约状态。<br>例: `TRADING` |
| data.bks | object[] |  | Notional bracket updates.<br>名义价值档位更新。 |
| data.bks[].bs | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| data.bks[].bnf | integer (int64) |  | Floor notional of this bracket<br>该层对应的名义价值下限<br>例: `0` |
| data.bks[].bnc | integer (int64) |  | Cap notional of this bracket<br>该层对应的名义价值上限<br>例: `5000` |
| data.bks[].mmr | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.01` |
| data.bks[].cf | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `0` |
| data.bks[].mi | integer (int64) |  | Min leverage for this bracket<br>该层杠杆下界<br>例: `21` |
| data.bks[].ma | integer (int64) |  | Max leverage for this bracket<br>该层杠杆上界<br>例: `50` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!contractInfo",
  "data": {
    "e": "contractInfo",
    "E": 1669356423908,
    "s": "IOTAUSDT",
    "ct": "PERPETUAL",
    "dt": 4133404800000,
    "ot": 1569398400000,
    "cs": "TRADING",
    "bks": [
      {
        "bs": 1,
        "bnf": 0,
        "bnc": 5000,
        "mmr": 0.01,
        "cf": 0,
        "mi": 21,
        "ma": 50
      }
    ],
    "st": 1
  }
}
```

## Individual Symbol Mini Ticker Stream（按交易对的精简Ticker）

流名称: `{symbol}@miniTicker`

24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

单交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 2s

Operation ID: `individualSymbolMiniTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@miniTicker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Mini Ticker Stream / 单交易对精简行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| E | integer (int64) |  | Event time<br>事件时间(毫秒)<br>例: `123456789` |
| s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "24hrMiniTicker",
  "E": 123456789,
  "s": "BNBUSDT",
  "c": "0.0025",
  "o": "0.0010",
  "h": "0.0025",
  "l": "0.0010",
  "v": "10000",
  "q": "18",
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@miniTicker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `24hrMiniTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间(毫秒)<br>例: `123456789` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data.c | string |  | Close price<br>最新成交价格<br>例: `0.0025` |
| data.o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `0.0010` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data.v | string |  | Total traded base asset volume<br>成交量<br>例: `10000` |
| data.q | string |  | Total traded quote asset volume<br>成交额<br>例: `18` |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@miniTicker",
  "data": {
    "e": "24hrMiniTicker",
    "E": 123456789,
    "s": "BNBUSDT",
    "c": "0.0025",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18",
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## Individual Symbol Ticker Streams（按Symbol的完整Ticker）

流名称: `{symbol}@ticker`

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

单交易对的24小时滚动窗口完整Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 2000ms

Operation ID: `individualSymbolTickerStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@ticker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Ticker Streams / 单交易对行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `250.00` |
| w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `10` |
| o | string |  | Open price<br>24小时内第一比成交的价格<br>例: `0.0010` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `86400000` |
| F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "24hrTicker",
  "E": 123456789,
  "s": "BNBUSDT",
  "p": "0.0015",
  "P": "250.00",
  "w": "0.0018",
  "c": "0.0025",
  "Q": "10",
  "o": "0.0010",
  "h": "0.0025",
  "l": "0.0010",
  "v": "10000",
  "q": "18",
  "O": 0,
  "C": 86400000,
  "F": 0,
  "L": 18150,
  "n": 18151,
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@ticker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data.p | string |  | Price change<br>24小时价格变化<br>例: `0.0015` |
| data.P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `250.00` |
| data.w | string |  | Weighted average price<br>平均价格<br>例: `0.0018` |
| data.c | string |  | Last price<br>最新成交价格<br>例: `0.0025` |
| data.Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `10` |
| data.o | string |  | Open price<br>24小时内第一比成交的价格<br>例: `0.0010` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `0.0025` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `0.0010` |
| data.v | string |  | Total traded base asset volume<br>24小时内成交量<br>例: `10000` |
| data.q | string |  | Total traded quote asset volume<br>24小时内成交额<br>例: `18` |
| data.O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `0` |
| data.C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `86400000` |
| data.F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `0` |
| data.L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `18150` |
| data.n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `18151` |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@ticker",
  "data": {
    "e": "24hrTicker",
    "E": 123456789,
    "s": "BNBUSDT",
    "p": "0.0015",
    "P": "250.00",
    "w": "0.0018",
    "c": "0.0025",
    "Q": "10",
    "o": "0.0010",
    "h": "0.0025",
    "l": "0.0010",
    "v": "10000",
    "q": "18",
    "O": 0,
    "C": 86400000,
    "F": 0,
    "L": 18150,
    "n": 18151,
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## Kline/Candlestick Streams（K线）

流名称: `{symbol}@kline_{interval}`

The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).

> **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。推送间隔250毫秒(如有刷新)

> **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 250ms

Operation ID: `klineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |
| interval | path | string | 是 | The interval parameter<br>时间间隔参数。<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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
    "btcusdt@kline_1m"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Kline/Candlestick Streams / K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `kline` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1638747660000` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| k | object |  | Kline payload.<br>K 线数据。 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1638747660000` |
| k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1638747719999` |
| k.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | First trade ID<br>这根K线期间第一笔成交ID<br>例: `100` |
| k.L | integer (int64) |  | Last trade ID<br>这根K线期间末一笔成交ID<br>例: `200` |
| k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `0.0010` |
| k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `0.0020` |
| k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `0.0025` |
| k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `0.0015` |
| k.v | string |  | Base asset volume<br>这根K线期间成交量<br>例: `1000` |
| k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `100` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | Quote asset volume<br>这根K线期间成交额<br>例: `1.0000` |
| k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "e": "kline",
  "E": 1638747660000,
  "s": "BTCUSDT",
  "k": {
    "t": 1638747660000,
    "T": 1638747719999,
    "s": "BTCUSDT",
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
| stream | string | 是 | 例: `btcusdt@kline_1m` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `kline` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1638747660000` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.k | object |  | Kline payload.<br>K 线数据。 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1638747660000` |
| data.k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1638747719999` |
| data.k.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | First trade ID<br>这根K线期间第一笔成交ID<br>例: `100` |
| data.k.L | integer (int64) |  | Last trade ID<br>这根K线期间末一笔成交ID<br>例: `200` |
| data.k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `0.0010` |
| data.k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `0.0020` |
| data.k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `0.0025` |
| data.k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `0.0015` |
| data.k.v | string |  | Base asset volume<br>这根K线期间成交量<br>例: `1000` |
| data.k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `100` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | Quote asset volume<br>这根K线期间成交额<br>例: `1.0000` |
| data.k.V | string |  | Taker buy base asset volume<br>主动买入的成交量<br>例: `500` |
| data.k.Q | string |  | Taker buy quote asset volume<br>主动买入的成交额<br>例: `0.500` |
| data.k.B | string |  | Ignore<br>忽略此参数<br>例: `123456` |

```json
{
  "stream": "btcusdt@kline_1m",
  "data": {
    "e": "kline",
    "E": 1638747660000,
    "s": "BTCUSDT",
    "k": {
      "t": 1638747660000,
      "T": 1638747719999,
      "s": "BTCUSDT",
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

## Liquidation Order Streams（强平订单）

流名称: `{symbol}@forceOrder`

The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol. For each symbol，only the largest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

强平订单快照流推送特定交易对的强平订单信息。对于每个交易对，在1000毫秒内只会推送最大的一笔强平订单作为快照。如果在1000毫秒的时间间隔内没有发生强平，则不会推送任何流。

更新速度: 1000ms

Operation ID: `liquidationOrderStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@forceOrder"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Liquidation Order Streams / 强平订单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event Type<br>事件类型<br>例: `forceOrder` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1568014460893` |
| o | object |  | Order Type<br>订单类型 |
| o.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| o.q | string |  | Original Quantity<br>订单数量<br>例: `0.014` |
| o.p | string |  | Price<br>订单价格<br>例: `9910` |
| o.ap | string |  | Average Price<br>平均价格<br>例: `9910` |
| o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `0.014` |
| o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `0.014` |
| o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1568014460893` |

```json
{
  "e": "forceOrder",
  "E": 1568014460893,
  "o": {
    "s": "BTCUSDT",
    "S": "SELL",
    "o": "LIMIT",
    "f": "IOC",
    "q": "0.014",
    "p": "9910",
    "ap": "9910",
    "X": "FILLED",
    "l": "0.014",
    "z": "0.014",
    "T": 1568014460893
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@forceOrder` |
| data | object | 是 |  |
| data.e | string |  | Event Type<br>事件类型<br>例: `forceOrder` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1568014460893` |
| data.o | object |  | Order Type<br>订单类型 |
| data.o.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| data.o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| data.o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| data.o.q | string |  | Original Quantity<br>订单数量<br>例: `0.014` |
| data.o.p | string |  | Price<br>订单价格<br>例: `9910` |
| data.o.ap | string |  | Average Price<br>平均价格<br>例: `9910` |
| data.o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| data.o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `0.014` |
| data.o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `0.014` |
| data.o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1568014460893` |

```json
{
  "stream": "btcusdt@forceOrder",
  "data": {
    "e": "forceOrder",
    "E": 1568014460893,
    "o": {
      "s": "BTCUSDT",
      "S": "SELL",
      "o": "LIMIT",
      "f": "IOC",
      "q": "0.014",
      "p": "9910",
      "ap": "9910",
      "X": "FILLED",
      "l": "0.014",
      "z": "0.014",
      "T": 1568014460893
    }
  }
}
```

## Mark Price Stream（最新标记价格）

流名称: `{symbol}@markPrice@{updateSpeed}`

Mark price and funding rate for a single symbol pushed every 3 seconds or every second.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

单交易对的标记价格和资金费率，每 3 秒或每秒推送一次。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

Operation ID: `markPriceStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 推送更新速度。<br>枚举: `1s`<br>例: `1s` |

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
    "btcusdt@markPrice@1s"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Mark Price Stream / 标记价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `markPriceUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1562305380000` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| p | string |  | Mark price<br>标记价格<br>例: `11794.15000000` |
| i | string |  | Index price<br>现货指数价格<br>例: `11784.62659091` |
| P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `11784.25641265` |
| r | string |  | Funding rate<br>资金费率<br>例: `0.00038167` |
| ap | string |  | Mark price moving average<br>标记价格移动平均值<br>例: `11794.15000000` |
| T | integer (int64) |  | Next funding time<br>下次资金时间<br>例: `1562306400000` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "markPriceUpdate",
  "E": 1562305380000,
  "s": "BTCUSDT",
  "p": "11794.15000000",
  "i": "11784.62659091",
  "P": "11784.25641265",
  "r": "0.00038167",
  "ap": "11794.15000000",
  "T": 1562306400000,
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@markPrice@1s` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `markPriceUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1562305380000` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.p | string |  | Mark price<br>标记价格<br>例: `11794.15000000` |
| data.i | string |  | Index price<br>现货指数价格<br>例: `11784.62659091` |
| data.P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `11784.25641265` |
| data.r | string |  | Funding rate<br>资金费率<br>例: `0.00038167` |
| data.ap | string |  | Mark price moving average<br>标记价格移动平均值<br>例: `11794.15000000` |
| data.T | integer (int64) |  | Next funding time<br>下次资金时间<br>例: `1562306400000` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@markPrice@1s",
  "data": {
    "e": "markPriceUpdate",
    "E": 1562305380000,
    "s": "BTCUSDT",
    "p": "11794.15000000",
    "i": "11784.62659091",
    "P": "11784.25641265",
    "r": "0.00038167",
    "ap": "11794.15000000",
    "T": 1562306400000,
    "st": 1
  }
}
```

## Mark Price Stream for All market（全市场最新标记价格）

流名称: `!markPrice@arr@{updateSpeed}`

Mark price and funding rate for all symbols pushed every 3 seconds or every second.

**Note:**
- TradFi symbols will be pushed through a seperate message.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

全市场交易对的标记价格与资金费率，每 3 秒或每 1 秒推送一次。

**注意：**
- TradFi 交易对会通过独立消息推送。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 3s or 1s

Operation ID: `markPriceStreamForAllMarket`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 推送更新速度。<br>枚举: `1s`<br>例: `1s` |

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
    "!markPrice@arr@1s"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Mark Price Stream for All market / 全市场标记价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `markPriceUpdate` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1562305380000` |
| [].s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| [].p | string |  | Mark price<br>标记价格<br>例: `11185.87786614` |
| [].i | string |  | Index price<br>现货指数价格<br>例: `11784.62659091` |
| [].P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `11784.25641265` |
| [].r | string |  | Funding rate<br>资金费率<br>例: `0.00030000` |
| [].ap | string |  | Mark price moving average<br>标记价格移动平均值<br>例: `11185.87786614` |
| [].T | integer (int64) |  | Next funding time<br>下个资金时间<br>例: `1562306400000` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "markPriceUpdate",
    "E": 1562305380000,
    "s": "BTCUSDT",
    "p": "11185.87786614",
    "i": "11784.62659091",
    "P": "11784.25641265",
    "r": "0.00030000",
    "ap": "11185.87786614",
    "T": 1562306400000,
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!markPrice@arr@1s` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `markPriceUpdate` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1562305380000` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data[].p | string |  | Mark price<br>标记价格<br>例: `11185.87786614` |
| data[].i | string |  | Index price<br>现货指数价格<br>例: `11784.62659091` |
| data[].P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `11784.25641265` |
| data[].r | string |  | Funding rate<br>资金费率<br>例: `0.00030000` |
| data[].ap | string |  | Mark price moving average<br>标记价格移动平均值<br>例: `11185.87786614` |
| data[].T | integer (int64) |  | Next funding time<br>下个资金时间<br>例: `1562306400000` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!markPrice@arr@1s",
  "data": [
    {
      "e": "markPriceUpdate",
      "E": 1562305380000,
      "s": "BTCUSDT",
      "p": "11185.87786614",
      "i": "11784.62659091",
      "P": "11784.25641265",
      "r": "0.00030000",
      "ap": "11185.87786614",
      "T": 1562306400000,
      "st": 1
    }
  ]
}
```

## Multi-Assets Mode Asset Index（多资产模式资产指数）

流名称: `!assetIndex@arr`

Asset index price. Subscribe with `!assetIndex@arr` for all assets, or `<assetSymbol>@assetIndex` for a specific asset.

> **CM-UM Integration (Effective 2026-06-30):** Renamed from *Multi-Assets Mode Asset Index*. The stream `!assetIndex@arr` now additionally pushes COIN-M settlement-asset price index entries (e.g., `BTCUSD`, `ETHUSD`, `BNBUSD`). The on-the-wire stream key is unchanged; existing subscriptions continue to work.

资产汇率指数。使用 `!assetIndex@arr` 订阅所有资产，或使用 `<assetSymbol>@assetIndex` 订阅指定资产。

> **币本位/U本位整合迁移(2026-06-30 生效):** Stream 名由 *多资产模式资产汇率指数* 变更为 *资产汇率指数*。Stream `!assetIndex@arr` 现在**额外推送**币本位结算资产的价格指数(如 `BTCUSD`、`ETHUSD`、`BNBUSD`)。订阅键不变,已有订阅继续可用。

更新速度: 1s

Operation ID: `assetIndex`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "!assetIndex@arr"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Multi-Assets Mode Asset Index / 多资产模式资产指数

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type.<br>事件类型。<br>例: `assetIndexUpdate` |
| [].E | integer (int64) |  | Event time.<br>事件时间。<br>例: `1686749230000` |
| [].s | string |  | Asset index symbol.<br>资产指数交易对。<br>例: `ADAUSD` |
| [].i | string |  | Index price.<br>指数价格。<br>例: `0.27462452` |
| [].b | string |  | Bid buffer.<br>买方缓冲值。<br>例: `0.10000000` |
| [].a | string |  | Ask buffer.<br>卖方缓冲值。<br>例: `0.10000000` |
| [].B | string |  | Bid rate.<br>买方汇率。<br>例: `0.24716207` |
| [].A | string |  | Ask rate.<br>卖方汇率。<br>例: `0.30208698` |
| [].q | string |  | Auto exchange bid buffer.<br>自动兑换买方缓冲值。<br>例: `0.05000000` |
| [].g | string |  | Auto exchange ask buffer.<br>自动兑换卖方缓冲值。<br>例: `0.05000000` |
| [].Q | string |  | Auto exchange bid rate.<br>自动兑换买方汇率。<br>例: `0.26089330` |
| [].G | string |  | Auto exchange ask rate.<br>自动兑换卖方汇率。<br>例: `0.28835575` |

```json
[
  {
    "e": "assetIndexUpdate",
    "E": 1686749230000,
    "s": "ADAUSD",
    "i": "0.27462452",
    "b": "0.10000000",
    "a": "0.10000000",
    "B": "0.24716207",
    "A": "0.30208698",
    "q": "0.05000000",
    "g": "0.05000000",
    "Q": "0.26089330",
    "G": "0.28835575"
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!assetIndex@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type.<br>事件类型。<br>例: `assetIndexUpdate` |
| data[].E | integer (int64) |  | Event time.<br>事件时间。<br>例: `1686749230000` |
| data[].s | string |  | Asset index symbol.<br>资产指数交易对。<br>例: `ADAUSD` |
| data[].i | string |  | Index price.<br>指数价格。<br>例: `0.27462452` |
| data[].b | string |  | Bid buffer.<br>买方缓冲值。<br>例: `0.10000000` |
| data[].a | string |  | Ask buffer.<br>卖方缓冲值。<br>例: `0.10000000` |
| data[].B | string |  | Bid rate.<br>买方汇率。<br>例: `0.24716207` |
| data[].A | string |  | Ask rate.<br>卖方汇率。<br>例: `0.30208698` |
| data[].q | string |  | Auto exchange bid buffer.<br>自动兑换买方缓冲值。<br>例: `0.05000000` |
| data[].g | string |  | Auto exchange ask buffer.<br>自动兑换卖方缓冲值。<br>例: `0.05000000` |
| data[].Q | string |  | Auto exchange bid rate.<br>自动兑换买方汇率。<br>例: `0.26089330` |
| data[].G | string |  | Auto exchange ask rate.<br>自动兑换卖方汇率。<br>例: `0.28835575` |

```json
{
  "stream": "!assetIndex@arr",
  "data": [
    {
      "e": "assetIndexUpdate",
      "E": 1686749230000,
      "s": "ADAUSD",
      "i": "0.27462452",
      "b": "0.10000000",
      "a": "0.10000000",
      "B": "0.24716207",
      "A": "0.30208698",
      "q": "0.05000000",
      "g": "0.05000000",
      "Q": "0.26089330",
      "G": "0.28835575"
    }
  ]
}
```

## Trading Session Stream（当前交易时段）

流名称: `tradingSession`

Trading session information for the underlying assets of TradFi Perpetual contracts, covering the U.S. equity market, Korean equity market, Hong Kong equity market, China equity market, the commodity market, and the FX market, is updated every second. Trading session information for different underlying markets is pushed in separate messages.

**Event type:**

- `EquityUpdate`: Session types for the U.S. equity market include "PRE_MARKET", "REGULAR", "AFTER_MARKET", "OVERNIGHT", and "NO_TRADING".
- `CommodityUpdate`: Session types for the commodity market include "REGULAR" and "NO_TRADING".
- `KR_EquityUpdate`: Session types for the Korean equity market include "REGULAR" and "NO_TRADING".
- `HK_EquityUpdate`: Session types for the Hong Kong equity market include "REGULAR" and "NO_TRADING".
- `CN_EquityUpdate`: Session types for the China equity market include "REGULAR" and "NO_TRADING".
- `FXUpdate`: Session types for the FX market include "REGULAR" and "NO_TRADING".

每秒返回传统金融合约标的资产（美股市场、韩国股票市场、香港股票市场、中国股票市场、大宗商品市场及外汇市场）的当前交易时段信息。不同标的市场的交易时段信息由不同消息推送。

**事件类型：**

- `EquityUpdate`：美股市场的时段类型包括 "PRE_MARKET"、"REGULAR"、"AFTER_MARKET"、"OVERNIGHT" 和 "NO_TRADING"。
- `CommodityUpdate`：大宗商品市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。
- `KR_EquityUpdate`：韩国股票市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。
- `HK_EquityUpdate`：香港股票市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。
- `CN_EquityUpdate`：中国股票市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。
- `FXUpdate`：外汇市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。

更新速度: 1s

Operation ID: `tradingSessionStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "tradingSession"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Trading Session Stream / 交易时段流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type, can also be CommodityUpdate, KR_EquityUpdate, HK_EquityUpdate, CN_EquityUpdate or FXUpdate<br>事件类型, 也可以是CommodityUpdate、KR_EquityUpdate、HK_EquityUpdate、CN_EquityUpdate或FXUpdate<br>例: `EquityUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1765244143062` |
| t | integer (int64) |  | Session start time<br>交易时段开始时间<br>例: `1765242000000` |
| T | integer (int64) |  | Session end time<br>交易时段结束时间<br>例: `1765270800000` |
| S | string |  | Session type<br>交易时段类型<br>例: `OVERNIGHT` |

```json
{
  "e": "EquityUpdate",
  "E": 1765244143062,
  "t": 1765242000000,
  "T": 1765270800000,
  "S": "OVERNIGHT"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `tradingSession` |
| data | object | 是 |  |
| data.e | string |  | Event type, can also be CommodityUpdate, KR_EquityUpdate, HK_EquityUpdate, CN_EquityUpdate or FXUpdate<br>事件类型, 也可以是CommodityUpdate、KR_EquityUpdate、HK_EquityUpdate、CN_EquityUpdate或FXUpdate<br>例: `EquityUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1765244143062` |
| data.t | integer (int64) |  | Session start time<br>交易时段开始时间<br>例: `1765242000000` |
| data.T | integer (int64) |  | Session end time<br>交易时段结束时间<br>例: `1765270800000` |
| data.S | string |  | Session type<br>交易时段类型<br>例: `OVERNIGHT` |

```json
{
  "stream": "tradingSession",
  "data": {
    "e": "EquityUpdate",
    "E": 1765244143062,
    "t": 1765242000000,
    "T": 1765270800000,
    "S": "OVERNIGHT"
  }
}
```

## All Book Tickers Stream（全市场最优挂单信息）

流名称: `!bookTicker`

Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

实时推送所有交易对的最优挂单价格或数量的任何更新。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 5s

Operation ID: `allBookTickersStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |

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
    "!bookTicker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：All Book Tickers Stream / 全市场最优挂单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| u | integer (int64) |  | order book updateId<br>更新ID<br>例: `400900217` |
| E | integer (int64) |  | event time<br>事件推送时间<br>例: `1568014460893` |
| T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1568014460891` |
| s | string |  | symbol<br>交易对<br>例: `BNBUSDT` |
| b | string |  | best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| B | string |  | best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| a | string |  | best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| A | string |  | best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "bookTicker",
  "u": 400900217,
  "E": 1568014460893,
  "T": 1568014460891,
  "s": "BNBUSDT",
  "b": "25.35190000",
  "B": "31.21000000",
  "a": "25.36520000",
  "A": "40.66000000",
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!bookTicker` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| data.u | integer (int64) |  | order book updateId<br>更新ID<br>例: `400900217` |
| data.E | integer (int64) |  | event time<br>事件推送时间<br>例: `1568014460893` |
| data.T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1568014460891` |
| data.s | string |  | symbol<br>交易对<br>例: `BNBUSDT` |
| data.b | string |  | best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| data.B | string |  | best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| data.a | string |  | best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| data.A | string |  | best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!bookTicker",
  "data": {
    "e": "bookTicker",
    "u": 400900217,
    "E": 1568014460893,
    "T": 1568014460891,
    "s": "BNBUSDT",
    "b": "25.35190000",
    "B": "31.21000000",
    "a": "25.36520000",
    "A": "40.66000000",
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## Diff. Book Depth Streams（增量深度信息）

流名称: `{symbol}@depth@{updateSpeed}`

Bids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing).

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

买卖盘，每 250 毫秒、500 毫秒、100 毫秒推送一次（如果存在）。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 250ms, 500ms, 100ms

Operation ID: `diffBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | Trading pair symbol.<br>交易对。<br>例: `btcusdt` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 流更新速度<br>枚举: `100ms`, `500ms`<br>例: `100ms` |

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
    "btcusdt@depth@100ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Diff. Book Depth Streams / 增量深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type.<br>事件类型。<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time.<br>事件时间。<br>例: `123456789` |
| T | integer (int64) |  | Transaction time.<br>成交时间。<br>例: `123456788` |
| s | string |  | Symbol.<br>交易对。<br>例: `BNBUSDT` |
| U | integer (int64) |  | First update ID in the event.<br>本次事件中的首个更新 ID。<br>例: `157` |
| u | integer (int64) |  | Final update ID in the event.<br>本次事件中的末尾更新 ID。<br>例: `160` |
| pu | integer (int64) |  | Final update ID in the previous stream event.<br>上一个事件中的末尾更新 ID。<br>例: `149` |
| b | oneOf[][] |  | Bid updates.<br>买盘更新。 |
| a | oneOf[][] |  | Ask updates.<br>卖盘更新。 |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "depthUpdate",
  "E": 123456789,
  "T": 123456788,
  "s": "BNBUSDT",
  "U": 157,
  "u": 160,
  "pu": 149,
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
  ],
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth@100ms` |
| data | object | 是 |  |
| data.e | string |  | Event type.<br>事件类型。<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time.<br>事件时间。<br>例: `123456789` |
| data.T | integer (int64) |  | Transaction time.<br>成交时间。<br>例: `123456788` |
| data.s | string |  | Symbol.<br>交易对。<br>例: `BNBUSDT` |
| data.U | integer (int64) |  | First update ID in the event.<br>本次事件中的首个更新 ID。<br>例: `157` |
| data.u | integer (int64) |  | Final update ID in the event.<br>本次事件中的末尾更新 ID。<br>例: `160` |
| data.pu | integer (int64) |  | Final update ID in the previous stream event.<br>上一个事件中的末尾更新 ID。<br>例: `149` |
| data.b | oneOf[][] |  | Bid updates.<br>买盘更新。 |
| data.a | oneOf[][] |  | Ask updates.<br>卖盘更新。 |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@depth@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 123456789,
    "T": 123456788,
    "s": "BNBUSDT",
    "U": 157,
    "u": 160,
    "pu": 149,
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
    ],
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## Individual Symbol Book Ticker Streams（按Symbol的最优挂单信息）

流名称: `{symbol}@bookTicker`

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

实时推送指定交易对的最优挂单价格或数量的任何更新。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: Real-time

Operation ID: `individualSymbolBookTickerStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@bookTicker"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Individual Symbol Book Ticker Streams / 单交易对最优挂单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| u | integer (int64) |  | order book updateId<br>更新ID<br>例: `400900217` |
| E | integer (int64) |  | event time<br>事件推送时间<br>例: `1568014460893` |
| T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1568014460891` |
| s | string |  | symbol<br>交易对<br>例: `BNBUSDT` |
| ps | string |  | pair (After CM migration)<br>标的交易对（迁移后新增）<br>例: `BNBUSDT` |
| b | string |  | best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| B | string |  | best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| a | string |  | best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| A | string |  | best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "bookTicker",
  "u": 400900217,
  "E": 1568014460893,
  "T": 1568014460891,
  "s": "BNBUSDT",
  "ps": "BNBUSDT",
  "b": "25.35190000",
  "B": "31.21000000",
  "a": "25.36520000",
  "A": "40.66000000",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@bookTicker` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| data.u | integer (int64) |  | order book updateId<br>更新ID<br>例: `400900217` |
| data.E | integer (int64) |  | event time<br>事件推送时间<br>例: `1568014460893` |
| data.T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1568014460891` |
| data.s | string |  | symbol<br>交易对<br>例: `BNBUSDT` |
| data.ps | string |  | pair (After CM migration)<br>标的交易对（迁移后新增）<br>例: `BNBUSDT` |
| data.b | string |  | best bid price<br>买单最优挂单价格<br>例: `25.35190000` |
| data.B | string |  | best bid qty<br>买单最优挂单数量<br>例: `31.21000000` |
| data.a | string |  | best ask price<br>卖单最优挂单价格<br>例: `25.36520000` |
| data.A | string |  | best ask qty<br>卖单最优挂单数量<br>例: `40.66000000` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@bookTicker",
  "data": {
    "e": "bookTicker",
    "u": 400900217,
    "E": 1568014460893,
    "T": 1568014460891,
    "s": "BNBUSDT",
    "ps": "BNBUSDT",
    "b": "25.35190000",
    "B": "31.21000000",
    "a": "25.36520000",
    "A": "40.66000000",
    "st": 1
  }
}
```

## Partial Book Depth Streams（有限档深度信息）

流名称: `{symbol}@depth{levels}@{updateSpeed}`

Top <levels> bids and asks

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

前 <levels> 档买卖盘深度。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 250ms or 500ms or 100ms

Operation ID: `partialBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |
| levels | path | string | 是 | The levels parameter<br>档位参数。<br>枚举: `5`, `10`, `20`<br>例: `10` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 推送更新速度。<br>枚举: `100ms`, `500ms`<br>例: `100ms` |

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
    "btcusdt@depth10@100ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Partial Book Depth Streams / 部分深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1571889248277` |
| T | integer (int64) |  | Transaction time<br>交易时间<br>例: `1571889248276` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `390497796` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `390497878` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `390497794` |
| b | string[][] |  | Bids to be updated<br>买方 |
| a | string[][] |  | Asks to be updated<br>卖方 |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "depthUpdate",
  "E": 1571889248277,
  "T": 1571889248276,
  "s": "BTCUSDT",
  "U": 390497796,
  "u": 390497878,
  "pu": 390497794,
  "b": [
    [
      "7403.89"
    ]
  ],
  "a": [
    [
      "7405.96"
    ]
  ],
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth10@100ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1571889248277` |
| data.T | integer (int64) |  | Transaction time<br>交易时间<br>例: `1571889248276` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `390497796` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `390497878` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `390497794` |
| data.b | string[][] |  | Bids to be updated<br>买方 |
| data.a | string[][] |  | Asks to be updated<br>卖方 |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@depth10@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1571889248277,
    "T": 1571889248276,
    "s": "BTCUSDT",
    "U": 390497796,
    "u": 390497878,
    "pu": 390497794,
    "b": [
      [
        "7403.89"
      ]
    ],
    "a": [
      [
        "7405.96"
      ]
    ],
    "ps": "BTCUSDT",
    "st": 1
  }
}
```

## RPI Diff. Book Depth Streams（RPI增量深度信息）

流名称: `{symbol}@rpiDepth@500ms`

Bids and asks including RPI orders, pushed every 500 milliseconds

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM) and a new `ps` field (pair symbol).

买卖盘增量深度（包含RPI订单），每500毫秒推送一次

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)以及 `ps`(pair symbol)字段。

更新速度: 500ms

Operation ID: `rpiDiffBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数。<br>例: `btcusdt` |

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
    "btcusdt@rpiDepth@500ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：RPI Diff. Book Depth Streams / RPI 增量深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `123456788` |
| s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `157` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `160` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `149` |
| b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |
| ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "depthUpdate",
  "E": 123456789,
  "T": 123456788,
  "s": "BNBUSDT",
  "U": 157,
  "u": 160,
  "pu": 149,
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
  ],
  "ps": "BTCUSDT",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@rpiDepth@500ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `123456789` |
| data.T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `123456788` |
| data.s | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `157` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `160` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `149` |
| data.b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| data.a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |
| data.ps | string |  | (After CM migration) Pair symbol<br>(迁移后新增) 标的交易对<br>例: `BTCUSDT` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@rpiDepth@500ms",
  "data": {
    "e": "depthUpdate",
    "E": 123456789,
    "T": 123456788,
    "s": "BNBUSDT",
    "U": 157,
    "u": 160,
    "pu": 149,
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
    ],
    "ps": "BTCUSDT",
    "st": 1
  }
}
```