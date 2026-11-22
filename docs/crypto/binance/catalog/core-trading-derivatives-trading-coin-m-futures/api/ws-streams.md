---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-22 18:46:06.294099
---

# Futures (COIN-M) WebSocket Market Streams

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/1.0.0/schema.yaml

Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.

访问市场数据、管理账户，并交易 COIN-M 永续合约和交割合约。

版本: 1.0.0

## 服务地址

- `wss://dstream.binance.com`
- `wss://dstream.binancefuture.com`

## 接口列表

- `{symbol}@aggTrade` — Aggregate Trade Streams
- `!bookTicker` — All Book Tickers Stream
- `!forceOrder@arr` — All Market Liquidation Order Streams
- `!miniTicker@arr` — All Market Mini Tickers Stream
- `!ticker@arr` — All Market Tickers Streams
- `{pair}_{contractType}@continuousKline_{interval}` — Continuous Contract Kline/Candlestick Streams
- `!contractInfo` — Contract Info Stream
- `{symbol}@depth@{updateSpeed}` — Diff. Book Depth Streams
- `{pair}@indexPriceKline_{interval}` — Index Kline/Candlestick Streams
- `{pair}@indexPrice@{updateSpeed}` — Index Price Stream
- `{symbol}@bookTicker` — Individual Symbol Book Ticker Streams
- `{symbol}@miniTicker` — Individual Symbol Mini Ticker Stream
- `{symbol}@ticker` — Individual Symbol Ticker Streams
- `{symbol}@kline_{interval}` — Kline/Candlestick Streams
- `{symbol}@forceOrder` — Market Liquidation Order Streams
- `{symbol}@markPriceKline_{interval}` — Mark Price Kline/Candlestick Streams
- `{pair}@markPrice@{updateSpeed}` — Mark Price of All Symbols of a Pair
- `{symbol}@markPrice@{updateSpeed}` — Mark Price Stream
- `{symbol}@depth{levels}@{updateSpeed}` — Partial Book Depth Streams

## Aggregate Trade Streams（归集交易）

流名称: `{symbol}@aggTrade`

The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

归集成交流推送市场成交信息, 每100毫秒为一个时间窗口, 将同一价格和买卖方向的成交进行归集。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 100ms

Operation ID: `aggregateTradeStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `aggTrade`<br>例: `aggTrade` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261134288` |
| a | integer (int64) |  | Aggregate trade ID<br>归集成交ID<br>例: `424951` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| p | string |  | Price<br>成交价格<br>例: `9643.5` |
| q | string |  | Quantity<br>成交量<br>例: `2` |
| f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `606073` |
| l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `606073` |
| T | integer (int64) |  | Trade time<br>成交时间<br>例: `1591261134199` |
| m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true,则此次成交是一个主动卖出单,否则是一个主动买入单。<br>例: `False` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "aggTrade",
  "E": 1591261134288,
  "a": 424951,
  "s": "BTCUSD_200626",
  "p": "9643.5",
  "q": "2",
  "f": 606073,
  "l": 606073,
  "T": 1591261134199,
  "m": false,
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@aggTrade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `aggTrade`<br>例: `aggTrade` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261134288` |
| data.a | integer (int64) |  | Aggregate trade ID<br>归集成交ID<br>例: `424951` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.p | string |  | Price<br>成交价格<br>例: `9643.5` |
| data.q | string |  | Quantity<br>成交量<br>例: `2` |
| data.f | integer (int64) |  | First trade ID<br>被归集的首个交易ID<br>例: `606073` |
| data.l | integer (int64) |  | Last trade ID<br>被归集的末次交易ID<br>例: `606073` |
| data.T | integer (int64) |  | Trade time<br>成交时间<br>例: `1591261134199` |
| data.m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true,则此次成交是一个主动卖出单,否则是一个主动买入单。<br>例: `False` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@aggTrade",
  "data": {
    "e": "aggTrade",
    "E": 1591261134288,
    "a": 424951,
    "s": "BTCUSD_200626",
    "p": "9643.5",
    "q": "2",
    "f": 606073,
    "l": 606073,
    "T": 1591261134199,
    "m": false,
    "st": 1
  }
}
```

## All Book Tickers Stream（全市场最优挂单信息）

流名称: `!bookTicker`

Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

实时推送所有交易对的最优挂单价格或数量的任何更新。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: Real-time

Operation ID: `allBookTickersStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `bookTicker`<br>例: `bookTicker` |
| u | integer (int64) |  | Order book update Id<br>更新ID<br>例: `17242169` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| b | string |  | Best bid price<br>买单最优挂单价格<br>例: `9548.1` |
| B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `52` |
| a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `9548.5` |
| A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `11` |
| T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591268628155` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268628166` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "bookTicker",
  "u": 17242169,
  "s": "BTCUSD_200626",
  "b": "9548.1",
  "B": "52",
  "a": "9548.5",
  "A": "11",
  "T": 1591268628155,
  "E": 1591268628166,
  "ps": "BTCUSD",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!bookTicker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `bookTicker`<br>例: `bookTicker` |
| data.u | integer (int64) |  | Order book update Id<br>更新ID<br>例: `17242169` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.b | string |  | Best bid price<br>买单最优挂单价格<br>例: `9548.1` |
| data.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `52` |
| data.a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `9548.5` |
| data.A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `11` |
| data.T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591268628155` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268628166` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!bookTicker",
  "data": {
    "e": "bookTicker",
    "u": 17242169,
    "s": "BTCUSD_200626",
    "b": "9548.1",
    "B": "52",
    "a": "9548.5",
    "A": "11",
    "T": 1591268628155,
    "E": 1591268628166,
    "ps": "BTCUSD",
    "st": 1
  }
}
```

## All Market Liquidation Order Streams（全市场强平订单）

流名称: `!forceOrder@arr`

The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

全市场强平订单快照流推送全市场所有交易对的强平订单信息。每个交易对在 1000ms 内只会推送最新的一笔强平订单作为快照，如果 1000ms 内没有发生强平，则不会推送任何流。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 1000ms

Operation ID: `allMarketLiquidationOrderStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |

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
| e | string |  | Event Type<br>事件类型<br>枚举: `forceOrder`<br>例: `forceOrder` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591154240950` |
| o | object |  | Order Type<br>订单类型 |
| o.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| o.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| o.q | string |  | Original Quantity<br>订单数量<br>例: `1` |
| o.p | string |  | Price<br>订单价格<br>例: `9425.5` |
| o.ap | string |  | Average Price<br>平均价格<br>例: `9496.5` |
| o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `1` |
| o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `1` |
| o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1591154240949` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "forceOrder",
  "E": 1591154240950,
  "o": {
    "s": "BTCUSD_200925",
    "ps": "BTCUSD",
    "S": "SELL",
    "o": "LIMIT",
    "f": "IOC",
    "q": "1",
    "p": "9425.5",
    "ap": "9496.5",
    "X": "FILLED",
    "l": "1",
    "z": "1",
    "T": 1591154240949
  },
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!forceOrder@arr` |
| data | object | 是 |  |
| data.e | string |  | Event Type<br>事件类型<br>枚举: `forceOrder`<br>例: `forceOrder` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591154240950` |
| data.o | object |  | Order Type<br>订单类型 |
| data.o.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| data.o.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| data.o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| data.o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| data.o.q | string |  | Original Quantity<br>订单数量<br>例: `1` |
| data.o.p | string |  | Price<br>订单价格<br>例: `9425.5` |
| data.o.ap | string |  | Average Price<br>平均价格<br>例: `9496.5` |
| data.o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| data.o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `1` |
| data.o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `1` |
| data.o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1591154240949` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!forceOrder@arr",
  "data": {
    "e": "forceOrder",
    "E": 1591154240950,
    "o": {
      "s": "BTCUSD_200925",
      "ps": "BTCUSD",
      "S": "SELL",
      "o": "LIMIT",
      "f": "IOC",
      "q": "1",
      "p": "9425.5",
      "ap": "9496.5",
      "X": "FILLED",
      "l": "1",
      "z": "1",
      "T": 1591154240949
    },
    "st": 1
  }
}
```

## All Market Mini Tickers Stream（全市场的精简Ticker）

流名称: `!miniTicker@arr`

24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

所有交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 1000ms

Operation ID: `allMarketMiniTickersStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |

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
| [].e | string |  | Event type<br>事件类型<br>枚举: `24hrMiniTicker`<br>例: `24hrMiniTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1591267704450` |
| [].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| [].ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].c | string |  | Close price<br>最新成交价格<br>例: `9561.7` |
| [].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `9580.9` |
| [].h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| [].l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| [].v | string |  | Total traded volume<br>24小时成交量<br>例: `487476` |
| [].q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `33264343847.22378500` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "24hrMiniTicker",
    "E": 1591267704450,
    "s": "BTCUSD_200626",
    "ps": "BTCUSD",
    "c": "9561.7",
    "o": "9580.9",
    "h": "10000.0",
    "l": "7000.0",
    "v": "487476",
    "q": "33264343847.22378500",
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!miniTicker@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>枚举: `24hrMiniTicker`<br>例: `24hrMiniTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1591267704450` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data[].ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data[].c | string |  | Close price<br>最新成交价格<br>例: `9561.7` |
| data[].o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `9580.9` |
| data[].h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| data[].l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| data[].v | string |  | Total traded volume<br>24小时成交量<br>例: `487476` |
| data[].q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `33264343847.22378500` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!miniTicker@arr",
  "data": [
    {
      "e": "24hrMiniTicker",
      "E": 1591267704450,
      "s": "BTCUSD_200626",
      "ps": "BTCUSD",
      "c": "9561.7",
      "o": "9580.9",
      "h": "10000.0",
      "l": "7000.0",
      "v": "487476",
      "q": "33264343847.22378500",
      "st": 1
    }
  ]
}
```

## All Market Tickers Streams（全市场的完整Ticker）

流名称: `!ticker@arr`

24hr rolling window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

24小时滚动窗口的所有交易对的Ticker统计。这些不是UTC日的统计，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 1000ms

Operation ID: `allMarketTickersStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |

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
| [].e | string |  | Event type<br>事件类型<br>枚举: `24hrTicker`<br>例: `24hrTicker` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268262453` |
| [].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| [].p | string |  | Price change<br>24小时价格变化<br>例: `-43.4` |
| [].P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `-0.452` |
| [].w | string |  | Weighted average price<br>24小时平均价格<br>例: `0.00147974` |
| [].c | string |  | Last price<br>最新成交价格<br>例: `9548.5` |
| [].Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `2` |
| [].o | string |  | Open price<br>24小时前第一笔成交价格<br>例: `9591.9` |
| [].h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| [].l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| [].v | string |  | Total traded volume<br>24小时成交量<br>例: `487850` |
| [].q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `32968676323.46222700` |
| [].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1591181820000` |
| [].C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `1591268262442` |
| [].F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `512014` |
| [].L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `615289` |
| [].n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `103272` |
| [].ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "24hrTicker",
    "E": 1591268262453,
    "s": "BTCUSD_200626",
    "p": "-43.4",
    "P": "-0.452",
    "w": "0.00147974",
    "c": "9548.5",
    "Q": "2",
    "o": "9591.9",
    "h": "10000.0",
    "l": "7000.0",
    "v": "487850",
    "q": "32968676323.46222700",
    "O": 1591181820000,
    "C": 1591268262442,
    "F": 512014,
    "L": 615289,
    "n": 103272,
    "ps": "BTCUSD",
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!ticker@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>枚举: `24hrTicker`<br>例: `24hrTicker` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268262453` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data[].p | string |  | Price change<br>24小时价格变化<br>例: `-43.4` |
| data[].P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `-0.452` |
| data[].w | string |  | Weighted average price<br>24小时平均价格<br>例: `0.00147974` |
| data[].c | string |  | Last price<br>最新成交价格<br>例: `9548.5` |
| data[].Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `2` |
| data[].o | string |  | Open price<br>24小时前第一笔成交价格<br>例: `9591.9` |
| data[].h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| data[].l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| data[].v | string |  | Total traded volume<br>24小时成交量<br>例: `487850` |
| data[].q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `32968676323.46222700` |
| data[].O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1591181820000` |
| data[].C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `1591268262442` |
| data[].F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `512014` |
| data[].L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `615289` |
| data[].n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `103272` |
| data[].ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!ticker@arr",
  "data": [
    {
      "e": "24hrTicker",
      "E": 1591268262453,
      "s": "BTCUSD_200626",
      "p": "-43.4",
      "P": "-0.452",
      "w": "0.00147974",
      "c": "9548.5",
      "Q": "2",
      "o": "9591.9",
      "h": "10000.0",
      "l": "7000.0",
      "v": "487850",
      "q": "32968676323.46222700",
      "O": 1591181820000,
      "C": 1591268262442,
      "F": 512014,
      "L": 615289,
      "n": 103272,
      "ps": "BTCUSD",
      "st": 1
    }
  ]
}
```

## Continuous Contract Kline/Candlestick Streams（连续合约K线）

流名称: `{pair}_{contractType}@continuousKline_{interval}`

Kline update every second

> **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

K线每秒更新

> **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 250ms

Operation ID: `continuousContractKlineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| pair | path | string | 是 | The pair parameter<br>交易对参数<br>例: `btcusdt` |
| contractType | path | string | 是 | The contractType parameter<br>The contract 类型 parameter<br>枚举: `perpetual`, `current_quarter`, `next_quarter`<br>例: `next_quarter` |
| interval | path | string | 是 | The interval parameter<br>间隔 参数<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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

### 响应 Raw Stream：Continuous Contract Kline/Candlestick Streams / 连续合约 K线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>枚举: `continuous_kline`<br>例: `continuous_kline` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1591261542539` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| ct | string |  | Contract type<br>合约类型<br>例: `NEXT_QUARTER` |
| k | object |  | Kline payload<br>K 线数据 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591261500000` |
| k.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1591261559999` |
| k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| k.f | integer (int64) |  | First update ID<br>第一个更新 ID<br>例: `606400` |
| k.L | integer (int64) |  | Last update ID<br>最后一个更新 ID<br>例: `606430` |
| k.o | string |  | openPrice<br>开盘价<br>例: `9638.9` |
| k.c | string |  | closePrice<br>收盘价<br>例: `9639.8` |
| k.h | string |  | highPrice<br>最高价<br>例: `9639.8` |
| k.l | string |  | lowPrice<br>最低价<br>例: `9638.6` |
| k.v | string |  | volume<br>基础资产成交量<br>例: `156` |
| k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `31` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | quoteVolume<br>计价资产成交额<br>例: `1.61836886` |
| k.V | string |  | Taker buy volume<br>无意义字段<br>例: `73` |
| k.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.75731156` |
| k.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `0` |

```json
{
  "e": "continuous_kline",
  "E": 1591261542539,
  "ps": "BTCUSD",
  "ct": "NEXT_QUARTER",
  "k": {
    "t": 1591261500000,
    "T": 1591261559999,
    "i": "1m",
    "f": 606400,
    "L": 606430,
    "o": "9638.9",
    "c": "9639.8",
    "h": "9639.8",
    "l": "9638.6",
    "v": "156",
    "n": 31,
    "x": false,
    "q": "1.61836886",
    "V": "73",
    "Q": "0.75731156",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt_next_quarter@continuousKline_1m` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>枚举: `continuous_kline`<br>例: `continuous_kline` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1591261542539` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.ct | string |  | Contract type<br>合约类型<br>例: `NEXT_QUARTER` |
| data.k | object |  | Kline payload<br>K 线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591261500000` |
| data.k.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1591261559999` |
| data.k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| data.k.f | integer (int64) |  | First update ID<br>第一个更新 ID<br>例: `606400` |
| data.k.L | integer (int64) |  | Last update ID<br>最后一个更新 ID<br>例: `606430` |
| data.k.o | string |  | openPrice<br>开盘价<br>例: `9638.9` |
| data.k.c | string |  | closePrice<br>收盘价<br>例: `9639.8` |
| data.k.h | string |  | highPrice<br>最高价<br>例: `9639.8` |
| data.k.l | string |  | lowPrice<br>最低价<br>例: `9638.6` |
| data.k.v | string |  | volume<br>基础资产成交量<br>例: `156` |
| data.k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `31` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | quoteVolume<br>计价资产成交额<br>例: `1.61836886` |
| data.k.V | string |  | Taker buy volume<br>无意义字段<br>例: `73` |
| data.k.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.75731156` |
| data.k.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `0` |

```json
{
  "stream": "btcusdt_next_quarter@continuousKline_1m",
  "data": {
    "e": "continuous_kline",
    "E": 1591261542539,
    "ps": "BTCUSD",
    "ct": "NEXT_QUARTER",
    "k": {
      "t": 1591261500000,
      "T": 1591261559999,
      "i": "1m",
      "f": 606400,
      "L": 606430,
      "o": "9638.9",
      "c": "9639.8",
      "h": "9639.8",
      "l": "9638.6",
      "v": "156",
      "n": 31,
      "x": false,
      "q": "1.61836886",
      "V": "73",
      "Q": "0.75731156",
      "B": "0"
    }
  }
}
```

## Contract Info Stream（交易对信息信息流）

流名称: `!contractInfo`

ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). bks field only shows up when bracket gets updated.

> **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).

ContractInfo 流在合约信息更新时推送（上架/结算/分层更新）。当分层更新时才会出现 bks 字段。

> **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: Real-time

Operation ID: `contractInfoStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |

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

### 响应 Raw Stream：Contract Info Stream / Contract Info 流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event Type<br>事件类型<br>枚举: `contractInfo`<br>例: `contractInfo` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1669647330375` |
| s | string |  | Symbol<br>交易对<br>例: `APTUSD_PERP` |
| ps | string |  | Pair<br>交易对标的<br>例: `APTUSD` |
| ct | string |  | Contract type<br>合约类型<br>例: `PERPETUAL` |
| dt | integer (int64) |  | Delivery date time<br>结算时间<br>例: `4133404800000` |
| ot | integer (int64) |  | onboard date time<br>上架时间<br>例: `1666594800000` |
| cs | string |  | Contract status<br>交易对状态<br>例: `TRADING` |
| bks | object[] |  | Bracket list.<br>分层列表. |
| bks[].bs | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| bks[].bnf | integer (int64) |  | Floor notional of this bracket<br>该层对应的名义价值下限<br>例: `0` |
| bks[].bnc | integer (int64) |  | Cap notional of this bracket<br>该层对应的名义价值上限<br>例: `500000` |
| bks[].mmr | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.0065` |
| bks[].cf | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `75` |
| bks[].mi | integer (int64) |  | Min leverage for this bracket<br>该层杠杆下界<br>例: `51` |
| bks[].ma | integer (int64) |  | Max leverage for this bracket<br>该层杠杆上界<br>例: `75` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "contractInfo",
  "E": 1669647330375,
  "s": "APTUSD_PERP",
  "ps": "APTUSD",
  "ct": "PERPETUAL",
  "dt": 4133404800000,
  "ot": 1666594800000,
  "cs": "TRADING",
  "bks": [
    {
      "bs": 1,
      "bnf": 0,
      "bnc": 500000,
      "mmr": 0.0065,
      "cf": 75,
      "mi": 51,
      "ma": 75
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
| data.e | string |  | Event Type<br>事件类型<br>枚举: `contractInfo`<br>例: `contractInfo` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1669647330375` |
| data.s | string |  | Symbol<br>交易对<br>例: `APTUSD_PERP` |
| data.ps | string |  | Pair<br>交易对标的<br>例: `APTUSD` |
| data.ct | string |  | Contract type<br>合约类型<br>例: `PERPETUAL` |
| data.dt | integer (int64) |  | Delivery date time<br>结算时间<br>例: `4133404800000` |
| data.ot | integer (int64) |  | onboard date time<br>上架时间<br>例: `1666594800000` |
| data.cs | string |  | Contract status<br>交易对状态<br>例: `TRADING` |
| data.bks | object[] |  | Bracket list.<br>分层列表. |
| data.bks[].bs | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| data.bks[].bnf | integer (int64) |  | Floor notional of this bracket<br>该层对应的名义价值下限<br>例: `0` |
| data.bks[].bnc | integer (int64) |  | Cap notional of this bracket<br>该层对应的名义价值上限<br>例: `500000` |
| data.bks[].mmr | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.0065` |
| data.bks[].cf | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `75` |
| data.bks[].mi | integer (int64) |  | Min leverage for this bracket<br>该层杠杆下界<br>例: `51` |
| data.bks[].ma | integer (int64) |  | Max leverage for this bracket<br>该层杠杆上界<br>例: `75` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "!contractInfo",
  "data": {
    "e": "contractInfo",
    "E": 1669647330375,
    "s": "APTUSD_PERP",
    "ps": "APTUSD",
    "ct": "PERPETUAL",
    "dt": 4133404800000,
    "ot": 1666594800000,
    "cs": "TRADING",
    "bks": [
      {
        "bs": 1,
        "bnf": 0,
        "bnc": 500000,
        "mmr": 0.0065,
        "cf": 75,
        "mi": 51,
        "ma": 75
      }
    ],
    "st": 1
  }
}
```

## Diff. Book Depth Streams（增量深度信息stream）

流名称: `{symbol}@depth@{updateSpeed}`

Bids and asks, pushed every 250 milliseconds, 500 milliseconds, or 100 milliseconds

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

买单和卖单，每 250ms、500ms 或 100ms 推送一次

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 250ms or 500ms or 100ms

Operation ID: `diffBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
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
| e | string |  | Event type<br>事件类型<br>枚举: `depthUpdate`<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591270260907` |
| T | integer (int64) |  | Transction time<br>撮合时间<br>例: `1591270260891` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `17285681` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `17285702` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `17285675` |
| b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "depthUpdate",
  "E": 1591270260907,
  "T": 1591270260891,
  "s": "BTCUSD_200626",
  "ps": "BTCUSD",
  "U": 17285681,
  "u": 17285702,
  "pu": 17285675,
  "b": [
    [
      "9517.6",
      "10"
    ]
  ],
  "a": [
    [
      "9518.5",
      "45"
    ]
  ],
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth@100ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `depthUpdate`<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591270260907` |
| data.T | integer (int64) |  | Transction time<br>撮合时间<br>例: `1591270260891` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `17285681` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `17285702` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `17285675` |
| data.b | oneOf[][] |  | Bids to be updated<br>变动的买单深度 |
| data.a | oneOf[][] |  | Asks to be updated<br>变动的卖单深度 |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@depth@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1591270260907,
    "T": 1591270260891,
    "s": "BTCUSD_200626",
    "ps": "BTCUSD",
    "U": 17285681,
    "u": 17285702,
    "pu": 17285675,
    "b": [
      [
        "9517.6",
        "10"
      ]
    ],
    "a": [
      [
        "9518.5",
        "45"
      ]
    ],
    "st": 1
  }
}
```

## Index Kline/Candlestick Streams（价格指数K线）

流名称: `{pair}@indexPriceKline_{interval}`

Index Kline/Candlestick Streams

> **After CM migration**, both `fstream` and `dstream` may subscribe to CM symbols on this stream.

价格指数K线

> **迁移后**,`fstream` 与 `dstream` 都可订阅 CM 的 symbol。

更新速度: 250ms

Operation ID: `indexKlineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| pair | path | string | 是 | The pair parameter<br>交易对参数<br>例: `btcusdt` |
| interval | path | string | 是 | The interval parameter<br>间隔 参数<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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
    "btcusdt@indexPriceKline_1m"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Index Kline/Candlestick Streams / 指数 K线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>枚举: `indexPrice_kline`<br>例: `indexPrice_kline` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1591267070033` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| k | object |  | Kline payload<br>K 线数据 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591267020000` |
| k.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1591267079999` |
| k.s | string |  | symbol<br>交易对<br>例: `0` |
| k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| k.f | integer (int64) |  | Ignore<br>忽略<br>例: `1591267020000` |
| k.L | integer (int64) |  | Ignore<br>忽略<br>例: `1591267070000` |
| k.o | string |  | openPrice<br>开盘价<br>例: `9542.21900000` |
| k.c | string |  | closePrice<br>收盘价<br>例: `9542.50440000` |
| k.h | string |  | highPrice<br>最高价<br>例: `9542.71640000` |
| k.l | string |  | lowPrice<br>最低价<br>例: `9542.21040000` |
| k.v | string |  | volume<br>基础资产成交量<br>例: `0` |
| k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `51` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | quoteVolume<br>计价资产成交额<br>例: `0` |
| k.V | string |  | Taker buy volume<br>无意义字段<br>例: `0` |
| k.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0` |
| k.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `0` |

```json
{
  "e": "indexPrice_kline",
  "E": 1591267070033,
  "ps": "BTCUSD",
  "k": {
    "t": 1591267020000,
    "T": 1591267079999,
    "s": "0",
    "i": "1m",
    "f": 1591267020000,
    "L": 1591267070000,
    "o": "9542.21900000",
    "c": "9542.50440000",
    "h": "9542.71640000",
    "l": "9542.21040000",
    "v": "0",
    "n": 51,
    "x": false,
    "q": "0",
    "V": "0",
    "Q": "0",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@indexPriceKline_1m` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>枚举: `indexPrice_kline`<br>例: `indexPrice_kline` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1591267070033` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.k | object |  | Kline payload<br>K 线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591267020000` |
| data.k.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1591267079999` |
| data.k.s | string |  | symbol<br>交易对<br>例: `0` |
| data.k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| data.k.f | integer (int64) |  | Ignore<br>忽略<br>例: `1591267020000` |
| data.k.L | integer (int64) |  | Ignore<br>忽略<br>例: `1591267070000` |
| data.k.o | string |  | openPrice<br>开盘价<br>例: `9542.21900000` |
| data.k.c | string |  | closePrice<br>收盘价<br>例: `9542.50440000` |
| data.k.h | string |  | highPrice<br>最高价<br>例: `9542.71640000` |
| data.k.l | string |  | lowPrice<br>最低价<br>例: `9542.21040000` |
| data.k.v | string |  | volume<br>基础资产成交量<br>例: `0` |
| data.k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `51` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | quoteVolume<br>计价资产成交额<br>例: `0` |
| data.k.V | string |  | Taker buy volume<br>无意义字段<br>例: `0` |
| data.k.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0` |
| data.k.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `0` |

```json
{
  "stream": "btcusdt@indexPriceKline_1m",
  "data": {
    "e": "indexPrice_kline",
    "E": 1591267070033,
    "ps": "BTCUSD",
    "k": {
      "t": 1591267020000,
      "T": 1591267079999,
      "s": "0",
      "i": "1m",
      "f": 1591267020000,
      "L": 1591267070000,
      "o": "9542.21900000",
      "c": "9542.50440000",
      "h": "9542.71640000",
      "l": "9542.21040000",
      "v": "0",
      "n": 51,
      "x": false,
      "q": "0",
      "V": "0",
      "Q": "0",
      "B": "0"
    }
  }
}
```

## Index Price Stream（最新现货指数价格）

流名称: `{pair}@indexPrice@{updateSpeed}`

Index Price Stream

最新现货指数价格

更新速度: 3000ms OR 1000ms

Operation ID: `indexPriceStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| pair | path | string | 是 | The pair parameter<br>交易对参数<br>例: `btcusdt` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 流更新速度<br>枚举: `1s`<br>例: `1s` |

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
    "btcusdt@indexPrice@1s"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Index Price Stream / 指数价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>枚举: `indexPriceUpdate`<br>例: `indexPriceUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261236000` |
| i | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| p | string |  | Index Price<br>指数价格<br>例: `9636.57860000` |

```json
{
  "e": "indexPriceUpdate",
  "E": 1591261236000,
  "i": "BTCUSD",
  "p": "9636.57860000"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@indexPrice@1s` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `indexPriceUpdate`<br>例: `indexPriceUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261236000` |
| data.i | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.p | string |  | Index Price<br>指数价格<br>例: `9636.57860000` |

```json
{
  "stream": "btcusdt@indexPrice@1s",
  "data": {
    "e": "indexPriceUpdate",
    "E": 1591261236000,
    "i": "BTCUSD",
    "p": "9636.57860000"
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
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `bookTicker`<br>例: `bookTicker` |
| u | integer (int64) |  | Order book update Id<br>更新ID<br>例: `17242169` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| b | string |  | Best bid price<br>买单最优挂单价格<br>例: `9548.1` |
| B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `52` |
| a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `9548.5` |
| A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `11` |
| T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591268628155` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268628166` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `2` |

```json
{
  "e": "bookTicker",
  "u": 17242169,
  "s": "BTCUSD_200626",
  "b": "9548.1",
  "B": "52",
  "a": "9548.5",
  "A": "11",
  "T": 1591268628155,
  "E": 1591268628166,
  "ps": "BTCUSD",
  "st": 2
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@bookTicker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `bookTicker`<br>例: `bookTicker` |
| data.u | integer (int64) |  | Order book update Id<br>更新ID<br>例: `17242169` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.b | string |  | Best bid price<br>买单最优挂单价格<br>例: `9548.1` |
| data.B | string |  | Best bid qty<br>买单最优挂单数量<br>例: `52` |
| data.a | string |  | Best ask price<br>卖单最优挂单价格<br>例: `9548.5` |
| data.A | string |  | Best ask qty<br>卖单最优挂单数量<br>例: `11` |
| data.T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591268628155` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268628166` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `2` |

```json
{
  "stream": "btcusdt@bookTicker",
  "data": {
    "e": "bookTicker",
    "u": 17242169,
    "s": "BTCUSD_200626",
    "b": "9548.1",
    "B": "52",
    "a": "9548.5",
    "A": "11",
    "T": 1591268628155,
    "E": 1591268628166,
    "ps": "BTCUSD",
    "st": 2
  }
}
```

## Individual Symbol Mini Ticker Stream（按Symbol的精简Ticker）

流名称: `{symbol}@miniTicker`

24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

单个交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计，而是从requestTime到24小时前的24小时滚动窗口。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 500ms

Operation ID: `individualSymbolMiniTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `24hrMiniTicker`<br>例: `24hrMiniTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591267704450` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| c | string |  | Close price<br>最新成交价格<br>例: `9561.7` |
| o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `9580.9` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| v | string |  | Total traded volume<br>24小时成交量<br>例: `487476` |
| q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `33264343847.22378500` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "24hrMiniTicker",
  "E": 1591267704450,
  "s": "BTCUSD_200626",
  "ps": "BTCUSD",
  "c": "9561.7",
  "o": "9580.9",
  "h": "10000.0",
  "l": "7000.0",
  "v": "487476",
  "q": "33264343847.22378500",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@miniTicker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `24hrMiniTicker`<br>例: `24hrMiniTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591267704450` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.c | string |  | Close price<br>最新成交价格<br>例: `9561.7` |
| data.o | string |  | Open price<br>24小时前开始第一笔成交价格<br>例: `9580.9` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| data.v | string |  | Total traded volume<br>24小时成交量<br>例: `487476` |
| data.q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `33264343847.22378500` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@miniTicker",
  "data": {
    "e": "24hrMiniTicker",
    "E": 1591267704450,
    "s": "BTCUSD_200626",
    "ps": "BTCUSD",
    "c": "9561.7",
    "o": "9580.9",
    "h": "10000.0",
    "l": "7000.0",
    "v": "487476",
    "q": "33264343847.22378500",
    "st": 1
  }
}
```

## Individual Symbol Ticker Streams（按Symbol的完整Ticker）

流名称: `{symbol}@ticker`

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

24小时滚动窗口的单个交易对的行情统计。这些不是UTC日的统计，而是从requestTime到24小时前的24小时滚动窗口。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 500ms

Operation ID: `individualSymbolTickerStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `24hrTicker`<br>例: `24hrTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268262453` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| p | string |  | Price change<br>24小时价格变化<br>例: `-43.4` |
| P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `-0.452` |
| w | string |  | Weighted average price<br>24小时平均价格<br>例: `0.00147974` |
| c | string |  | Last price<br>最新成交价格<br>例: `9548.5` |
| Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `2` |
| o | string |  | Open price<br>24小时前第一笔成交价格<br>例: `9591.9` |
| h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| v | string |  | Total traded volume<br>24小时成交量<br>例: `487850` |
| q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `32968676323.46222700` |
| O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1591181820000` |
| C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `1591268262442` |
| F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `512014` |
| L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `615289` |
| n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `103272` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "24hrTicker",
  "E": 1591268262453,
  "s": "BTCUSD_200626",
  "p": "-43.4",
  "P": "-0.452",
  "w": "0.00147974",
  "c": "9548.5",
  "Q": "2",
  "o": "9591.9",
  "h": "10000.0",
  "l": "7000.0",
  "v": "487850",
  "q": "32968676323.46222700",
  "O": 1591181820000,
  "C": 1591268262442,
  "F": 512014,
  "L": 615289,
  "n": 103272,
  "ps": "BTCUSD",
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@ticker` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `24hrTicker`<br>例: `24hrTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591268262453` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.p | string |  | Price change<br>24小时价格变化<br>例: `-43.4` |
| data.P | string |  | Price change percent<br>24小时价格变化(百分比)<br>例: `-0.452` |
| data.w | string |  | Weighted average price<br>24小时平均价格<br>例: `0.00147974` |
| data.c | string |  | Last price<br>最新成交价格<br>例: `9548.5` |
| data.Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `2` |
| data.o | string |  | Open price<br>24小时前第一笔成交价格<br>例: `9591.9` |
| data.h | string |  | High price<br>24小时内最高成交价<br>例: `10000.0` |
| data.l | string |  | Low price<br>24小时内最低成交价<br>例: `7000.0` |
| data.v | string |  | Total traded volume<br>24小时成交量<br>例: `487850` |
| data.q | string |  | Total traded base asset volume<br>24小时成交额(标的数量)<br>例: `32968676323.46222700` |
| data.O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1591181820000` |
| data.C | integer (int64) |  | Statistics close time<br>统计关闭时间<br>例: `1591268262442` |
| data.F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `512014` |
| data.L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `615289` |
| data.n | integer (int64) |  | Total number of trades<br>24小时内成交数<br>例: `103272` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@ticker",
  "data": {
    "e": "24hrTicker",
    "E": 1591268262453,
    "s": "BTCUSD_200626",
    "p": "-43.4",
    "P": "-0.452",
    "w": "0.00147974",
    "c": "9548.5",
    "Q": "2",
    "o": "9591.9",
    "h": "10000.0",
    "l": "7000.0",
    "v": "487850",
    "q": "32968676323.46222700",
    "O": 1591181820000,
    "C": 1591268262442,
    "F": 512014,
    "L": 615289,
    "n": 103272,
    "ps": "BTCUSD",
    "st": 1
  }
}
```

## Kline/Candlestick Streams（K线）

流名称: `{symbol}@kline_{interval}`

The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).

> **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

K线流每250毫秒推送当前K线更新（如果有）.

> **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 250ms

Operation ID: `klineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| interval | path | string | 是 | The interval parameter<br>间隔 参数<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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

### 响应 Raw Stream：Kline/Candlestick Streams / K线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>枚举: `kline`<br>例: `kline` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261542539` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| k | object |  | Kline payload<br>K 线数据 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591261500000` |
| k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1591261559999` |
| k.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | First trade ID<br>这根K线期间第一笔成交ID<br>例: `606400` |
| k.L | integer (int64) |  | Last trade ID<br>这根K线期间末一笔成交ID<br>例: `606430` |
| k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `9638.9` |
| k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `9639.8` |
| k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `9639.8` |
| k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `9638.6` |
| k.v | string |  | volume<br>这根K线期间成交量<br>例: `156` |
| k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `31` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | Base asset volume<br>这根K线期间成交额(标的数量)<br>例: `1.61836886` |
| k.V | string |  | Taker buy volume<br>主动买入的成交量<br>例: `73` |
| k.Q | string |  | Taker buy base asset volume<br>主动买入的成交额(标的数量)<br>例: `0.75731156` |
| k.B | string |  | Ignore<br>忽略此参数<br>例: `0` |

```json
{
  "e": "kline",
  "E": 1591261542539,
  "s": "BTCUSD_200626",
  "k": {
    "t": 1591261500000,
    "T": 1591261559999,
    "s": "BTCUSD_200626",
    "i": "1m",
    "f": 606400,
    "L": 606430,
    "o": "9638.9",
    "c": "9639.8",
    "h": "9639.8",
    "l": "9638.6",
    "v": "156",
    "n": 31,
    "x": false,
    "q": "1.61836886",
    "V": "73",
    "Q": "0.75731156",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@kline_1m` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `kline`<br>例: `kline` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591261542539` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.k | object |  | Kline payload<br>K 线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591261500000` |
| data.k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1591261559999` |
| data.k.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | First trade ID<br>这根K线期间第一笔成交ID<br>例: `606400` |
| data.k.L | integer (int64) |  | Last trade ID<br>这根K线期间末一笔成交ID<br>例: `606430` |
| data.k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `9638.9` |
| data.k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `9639.8` |
| data.k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `9639.8` |
| data.k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `9638.6` |
| data.k.v | string |  | volume<br>这根K线期间成交量<br>例: `156` |
| data.k.n | integer (int64) |  | Number of trades<br>这根K线期间成交笔数<br>例: `31` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | Base asset volume<br>这根K线期间成交额(标的数量)<br>例: `1.61836886` |
| data.k.V | string |  | Taker buy volume<br>主动买入的成交量<br>例: `73` |
| data.k.Q | string |  | Taker buy base asset volume<br>主动买入的成交额(标的数量)<br>例: `0.75731156` |
| data.k.B | string |  | Ignore<br>忽略此参数<br>例: `0` |

```json
{
  "stream": "btcusdt@kline_1m",
  "data": {
    "e": "kline",
    "E": 1591261542539,
    "s": "BTCUSD_200626",
    "k": {
      "t": 1591261500000,
      "T": 1591261559999,
      "s": "BTCUSD_200626",
      "i": "1m",
      "f": 606400,
      "L": 606430,
      "o": "9638.9",
      "c": "9639.8",
      "h": "9639.8",
      "l": "9638.6",
      "v": "156",
      "n": 31,
      "x": false,
      "q": "1.61836886",
      "V": "73",
      "Q": "0.75731156",
      "B": "0"
    }
  }
}
```

## Market Liquidation Order Streams（强平订单）

流名称: `{symbol}@forceOrder`

The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

强平订单快照流推送特定交易对的强平订单信息。对于每个交易对，在1000ms内只会推送最新的一笔强平订单作为快照。如果在1000ms的时间间隔内没有发生强平，则不会推送任何流。

更新速度: 1000ms

Operation ID: `marketLiquidationOrderStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
| e | string |  | Event Type<br>事件类型<br>枚举: `forceOrder`<br>例: `forceOrder` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591154240950` |
| o | object |  | Order Type<br>订单类型 |
| o.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| o.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| o.q | string |  | Original Quantity<br>订单数量<br>例: `1` |
| o.p | string |  | Price<br>订单价格<br>例: `9425.5` |
| o.ap | string |  | Average Price<br>平均价格<br>例: `9496.5` |
| o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `1` |
| o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `1` |
| o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1591154240949` |

```json
{
  "e": "forceOrder",
  "E": 1591154240950,
  "o": {
    "s": "BTCUSD_200925",
    "ps": "BTCUSD",
    "S": "SELL",
    "o": "LIMIT",
    "f": "IOC",
    "q": "1",
    "p": "9425.5",
    "ap": "9496.5",
    "X": "FILLED",
    "l": "1",
    "z": "1",
    "T": 1591154240949
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@forceOrder` |
| data | object | 是 |  |
| data.e | string |  | Event Type<br>事件类型<br>枚举: `forceOrder`<br>例: `forceOrder` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591154240950` |
| data.o | object |  | Order Type<br>订单类型 |
| data.o.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| data.o.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.o.S | string |  | Side<br>订单方向<br>例: `SELL` |
| data.o.o | string |  | Order Type<br>订单类型<br>例: `LIMIT` |
| data.o.f | string |  | Time in Force<br>有效方式<br>例: `IOC` |
| data.o.q | string |  | Original Quantity<br>订单数量<br>例: `1` |
| data.o.p | string |  | Price<br>订单价格<br>例: `9425.5` |
| data.o.ap | string |  | Average Price<br>平均价格<br>例: `9496.5` |
| data.o.X | string |  | Order Status<br>订单状态<br>例: `FILLED` |
| data.o.l | string |  | Order Last Filled Quantity<br>订单最近成交量<br>例: `1` |
| data.o.z | string |  | Order Filled Accumulated Quantity<br>订单累计成交量<br>例: `1` |
| data.o.T | integer (int64) |  | Order Trade Time<br>交易时间<br>例: `1591154240949` |

```json
{
  "stream": "btcusdt@forceOrder",
  "data": {
    "e": "forceOrder",
    "E": 1591154240950,
    "o": {
      "s": "BTCUSD_200925",
      "ps": "BTCUSD",
      "S": "SELL",
      "o": "LIMIT",
      "f": "IOC",
      "q": "1",
      "p": "9425.5",
      "ap": "9496.5",
      "X": "FILLED",
      "l": "1",
      "z": "1",
      "T": 1591154240949
    }
  }
}
```

## Mark Price Kline/Candlestick Streams（标记价格K线）

流名称: `{symbol}@markPriceKline_{interval}`

Mark Price Kline/Candlestick Streams

> **After CM migration**, both `fstream` and `dstream` may subscribe to CM symbols on this stream.

标记价格K线

> **迁移后**,`fstream` 与 `dstream` 都可订阅 CM 的 symbol。

更新速度: 250ms

Operation ID: `markPriceKlineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| interval | path | string | 是 | The interval parameter<br>间隔 参数<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

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
    "btcusdt@markPriceKline_1m"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Mark Price Kline/Candlestick Streams / 标记价格 K线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event Name<br>事件类型<br>枚举: `markPrice_kline`<br>例: `markPrice_kline` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591267398004` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| k | object |  | Kline payload<br>K 线数据 |
| k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591267380000` |
| k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1591267439999` |
| k.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | ignore<br>无意义字段<br>例: `1591267380000` |
| k.L | integer (int64) |  | ignore<br>无意义字段<br>例: `1591267398000` |
| k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `9539.67161333` |
| k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `9540.82761333` |
| k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `9540.82761333` |
| k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `9539.66961333` |
| k.v | string |  | ignore<br>无意义字段<br>例: `0` |
| k.n | integer (int64) |  | Number of basic data<br>这根K线更新期间数据数量<br>例: `19` |
| k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | ignore<br>无意义字段<br>例: `0` |
| k.V | string |  | ignore<br>无意义字段<br>例: `0` |
| k.Q | string |  | ignore<br>无意义字段<br>例: `0` |
| k.B | string |  | ignore<br>无意义字段<br>例: `0` |

```json
{
  "e": "markPrice_kline",
  "E": 1591267398004,
  "ps": "BTCUSD",
  "k": {
    "t": 1591267380000,
    "T": 1591267439999,
    "s": "BTCUSD_200626",
    "i": "1m",
    "f": 1591267380000,
    "L": 1591267398000,
    "o": "9539.67161333",
    "c": "9540.82761333",
    "h": "9540.82761333",
    "l": "9539.66961333",
    "v": "0",
    "n": 19,
    "x": false,
    "q": "0",
    "V": "0",
    "Q": "0",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@markPriceKline_1m` |
| data | object | 是 |  |
| data.e | string |  | Event Name<br>事件类型<br>枚举: `markPrice_kline`<br>例: `markPrice_kline` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1591267398004` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.k | object |  | Kline payload<br>K 线数据 |
| data.k.t | integer (int64) |  | Kline start time<br>这根K线的起始时间<br>例: `1591267380000` |
| data.k.T | integer (int64) |  | Kline close time<br>这根K线的结束时间<br>例: `1591267439999` |
| data.k.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.k.i | string |  | Interval<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | ignore<br>无意义字段<br>例: `1591267380000` |
| data.k.L | integer (int64) |  | ignore<br>无意义字段<br>例: `1591267398000` |
| data.k.o | string |  | Open price<br>这根K线期间第一笔成交价<br>例: `9539.67161333` |
| data.k.c | string |  | Close price<br>这根K线期间末一笔成交价<br>例: `9540.82761333` |
| data.k.h | string |  | High price<br>这根K线期间最高成交价<br>例: `9540.82761333` |
| data.k.l | string |  | Low price<br>这根K线期间最低成交价<br>例: `9539.66961333` |
| data.k.v | string |  | ignore<br>无意义字段<br>例: `0` |
| data.k.n | integer (int64) |  | Number of basic data<br>这根K线更新期间数据数量<br>例: `19` |
| data.k.x | boolean |  | Is this kline closed?<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | ignore<br>无意义字段<br>例: `0` |
| data.k.V | string |  | ignore<br>无意义字段<br>例: `0` |
| data.k.Q | string |  | ignore<br>无意义字段<br>例: `0` |
| data.k.B | string |  | ignore<br>无意义字段<br>例: `0` |

```json
{
  "stream": "btcusdt@markPriceKline_1m",
  "data": {
    "e": "markPrice_kline",
    "E": 1591267398004,
    "ps": "BTCUSD",
    "k": {
      "t": 1591267380000,
      "T": 1591267439999,
      "s": "BTCUSD_200626",
      "i": "1m",
      "f": 1591267380000,
      "L": 1591267398000,
      "o": "9539.67161333",
      "c": "9540.82761333",
      "h": "9540.82761333",
      "l": "9539.66961333",
      "v": "0",
      "n": 19,
      "x": false,
      "q": "0",
      "V": "0",
      "Q": "0",
      "B": "0"
    }
  }
}
```

## Mark Price of All Symbols of a Pair（特定pair最新MarkPrice）

流名称: `{pair}@markPrice@{updateSpeed}`

Mark Price of All Symbols of a Pair

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

特定pair最新MarkPrice

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 3000ms OR 1000ms

Operation ID: `markPriceOfAllSymbolsOfAPair`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| pair | path | string | 是 | The pair parameter<br>交易对参数<br>例: `btcusdt` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 流更新速度<br>枚举: `1s`<br>例: `1s` |

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

### 响应 Raw Stream：Mark Price of All Symbols of a Pair / 某个标的交易对下所有合约的标记价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>枚举: `markPriceUpdate`<br>例: `markPriceUpdate` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1596095725000` |
| [].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_201225` |
| [].p | string |  | Mark Price<br>标记价格<br>例: `10934.62615417` |
| [].P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `10962.17178236` |
| [].i | string |  | Index Price<br>指数价格<br>例: `10933.62615417` |
| [].r | string |  | funding rate for perpetual symbol, "" will be shown for delivery symbol<br>资金费率，对非永续合约显示""<br>例: `` |
| [].T | integer (int64) |  | next funding time for perpetual symbol, 0 will be shown for delivery symbol<br>下个资金时间,对非永续合约显示0<br>例: `0` |
| [].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
[
  {
    "e": "markPriceUpdate",
    "E": 1596095725000,
    "s": "BTCUSD_201225",
    "p": "10934.62615417",
    "P": "10962.17178236",
    "i": "10933.62615417",
    "r": "",
    "T": 0,
    "st": 1
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@markPrice@1s` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>枚举: `markPriceUpdate`<br>例: `markPriceUpdate` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1596095725000` |
| data[].s | string |  | Symbol<br>交易对<br>例: `BTCUSD_201225` |
| data[].p | string |  | Mark Price<br>标记价格<br>例: `10934.62615417` |
| data[].P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `10962.17178236` |
| data[].i | string |  | Index Price<br>指数价格<br>例: `10933.62615417` |
| data[].r | string |  | funding rate for perpetual symbol, "" will be shown for delivery symbol<br>资金费率，对非永续合约显示""<br>例: `` |
| data[].T | integer (int64) |  | next funding time for perpetual symbol, 0 will be shown for delivery symbol<br>下个资金时间,对非永续合约显示0<br>例: `0` |
| data[].st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@markPrice@1s",
  "data": [
    {
      "e": "markPriceUpdate",
      "E": 1596095725000,
      "s": "BTCUSD_201225",
      "p": "10934.62615417",
      "P": "10962.17178236",
      "i": "10933.62615417",
      "r": "",
      "T": 0,
      "st": 1
    }
  ]
}
```

## Mark Price Stream（最新MarkPrice）

流名称: `{symbol}@markPrice@{updateSpeed}`

Mark price update stream

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.

标记价格更新流

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。

更新速度: 3000ms OR 1000ms

Operation ID: `markPriceStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| updateSpeed | path | string |  | WebSocket stream update speed<br>WebSocket 流更新速度<br>枚举: `1s`<br>例: `1s` |

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
| e | string |  | Event type<br>事件类型<br>枚举: `markPriceUpdate`<br>例: `markPriceUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1596095725000` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_201225` |
| p | string |  | Mark Price<br>标记价格<br>例: `10934.62615417` |
| P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `10962.17178236` |
| i | string |  | Index Price<br>指数价格<br>例: `10933.62615417` |
| r | string |  | funding rate for perpetual symbol, "" will be shown for delivery symbol<br>资金费率，对非永续合约显示""<br>例: `` |
| T | integer (int64) |  | next funding time for perpetual symbol, 0 will be shown for delivery symbol<br>下个资金时间,对非永续合约显示0<br>例: `0` |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "markPriceUpdate",
  "E": 1596095725000,
  "s": "BTCUSD_201225",
  "p": "10934.62615417",
  "P": "10962.17178236",
  "i": "10933.62615417",
  "r": "",
  "T": 0,
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@markPrice@1s` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `markPriceUpdate`<br>例: `markPriceUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1596095725000` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_201225` |
| data.p | string |  | Mark Price<br>标记价格<br>例: `10934.62615417` |
| data.P | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在结算前最后一小时有参考价值<br>例: `10962.17178236` |
| data.i | string |  | Index Price<br>指数价格<br>例: `10933.62615417` |
| data.r | string |  | funding rate for perpetual symbol, "" will be shown for delivery symbol<br>资金费率，对非永续合约显示""<br>例: `` |
| data.T | integer (int64) |  | next funding time for perpetual symbol, 0 will be shown for delivery symbol<br>下个资金时间,对非永续合约显示0<br>例: `0` |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@markPrice@1s",
  "data": {
    "e": "markPriceUpdate",
    "E": 1596095725000,
    "s": "BTCUSD_201225",
    "p": "10934.62615417",
    "P": "10962.17178236",
    "i": "10933.62615417",
    "r": "",
    "T": 0,
    "st": 1
  }
}
```

## Partial Book Depth Streams（有限档深度信息）

流名称: `{symbol}@depth{levels}@{updateSpeed}`

Top levels bids and asks.

> **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).

买卖双方前几档的深度信息。

> **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。

更新速度: 250ms, 500ms or 100ms

Operation ID: `partialBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | string |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID.<br>例: `e9d6b4349871b40611412680b3445fac` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| levels | path | string | 是 | The levels parameter<br>levels 参数<br>枚举: `5`, `10`, `20`<br>例: `10` |
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
    "btcusdt@depth10@100ms"
  ],
  "id": "e9d6b4349871b40611412680b3445fac"
}
```

### 响应 Raw Stream：Partial Book Depth Streams / 部分深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>枚举: `depthUpdate`<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1591269996801` |
| T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591269996646` |
| s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `17276694` |
| u | integer (int64) |  | updateId<br>更新 ID<br>例: `17276701` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `17276678` |
| b | string[][] |  | Bids to be updated<br>买方 |
| a | string[][] |  | Asks to be updated<br>卖方 |
| st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "e": "depthUpdate",
  "E": 1591269996801,
  "T": 1591269996646,
  "s": "BTCUSD_200626",
  "ps": "BTCUSD",
  "U": 17276694,
  "u": 17276701,
  "pu": 17276678,
  "b": [
    [
      "9523.0"
    ]
  ],
  "a": [
    [
      "9524.6"
    ]
  ],
  "st": 1
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth10@100ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>枚举: `depthUpdate`<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1591269996801` |
| data.T | integer (int64) |  | Transaction time<br>撮合时间<br>例: `1591269996646` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| data.ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `17276694` |
| data.u | integer (int64) |  | updateId<br>更新 ID<br>例: `17276701` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `17276678` |
| data.b | string[][] |  | Bids to be updated<br>买方 |
| data.a | string[][] |  | Asks to be updated<br>卖方 |
| data.st | integer |  | (After CM migration) Symbol type: 1 = UM, 2 = CM<br>(迁移后新增) Symbol 类型:1 = UM,2 = CM<br>例: `1` |

```json
{
  "stream": "btcusdt@depth10@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1591269996801,
    "T": 1591269996646,
    "s": "BTCUSD_200626",
    "ps": "BTCUSD",
    "U": 17276694,
    "u": 17276701,
    "pu": 17276678,
    "b": [
      [
        "9523.0"
      ]
    ],
    "a": [
      [
        "9524.6"
      ]
    ],
    "st": 1
  }
}
```