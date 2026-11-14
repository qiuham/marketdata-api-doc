---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/alpha/websocket-market-data
api_type: WebSocket
updated_at: 2026-11-13 20:31:32.529950
---

# WebSocket Market Data API

## Basic Info

  * The base URL for all WSS endpoints listed in this document is: `wss://nbstream.binance.com/w3w/wsa/stream`



## Subscribe / Unsubscribe Streams in Real Time

  * You can subscribe to or unsubscribe from streams by sending messages over WebSocket. Examples are shown below.
  * The `id` in the request is used as a unique identifier to correlate request/response messages. The following formats are accepted:
    * 64-bit signed integer
    * Alphanumeric string; max length 36
    * null
  * If `result` in the corresponding response is `null`, it indicates the request was sent successfully.



### Subscribe to a stream

Request
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["came@allTokens@ticker24"],
      "id": 1
    }

Response
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

* * *

### Unsubscribe from a stream

Request
    
    
    Code
    
    {
      "method": "UNSUBSCRIBE",
      "params": ["came@allTokens@ticker24"],
      "id": 1
    }

Response
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

* * *

### List current subscriptions

Request
    
    
    Code
    
    {
      "method": "LIST_SUBSCRIPTION",
      "id": 3
    }

Response
    
    
    Code
    
    {
      "result": ["came@allTokens@ticker24"],
      "id": 3
    }

* * *

## Streams

### came@allTokens@ticker24
    
    
    Code
    
    {
      "data": {
        "d": [
          {
            "ca": "0x8fce7206e3043dd360f115afa956ee31b90b787c@56", // Contract address@Chain ID
            "cnt24": 10426, // Number of trades in the last 24h
            "fdv": "72834145.18711072", // Fully Diluted Valuation (FDV)
            "hc": "6822", // Number of holders
            "liq": "1442996.98151177662835", // Liquidity
            "mc": "13542034.24008014", // Market cap
            "p": "0.072849536538593663", // Current price
            "pc24": "-2.32", // 24h price change %
            "s": "1",
            "t": 1771825733000, // Timestamp (ms)
            "vol24": "12930712.213702157742688594285" // 24h volume
          }
        ],
        "e": "tickerList"
      },
      "stream": "came@allTokens@ticker24"
    }

* * *

### <symbol>@aggTrade
    
    
    Code
    
    {
      "data": {
        "E": 1771828569861, // Event time (ms)
        "T": 1771828569702, // Trade time (ms)
        "a": 2684294, // Aggregated trade ID
        "e": "aggTrade", // Event type
        "f": 2684294, // First trade ID in the aggregation
        "l": 2684294, // Last trade ID in the aggregation
        "m": false, // Is the buyer the market maker
        "p": "0.08530000", // Price
        "q": "879.24000000", // Quantity
        "s": "ALPHA_474USDT" // Symbol
      },
      "stream": "alpha_474usdt@aggTrade"
    }

* * *

### <symbol>@fulldepth@<interval>

interval: 0ms, 100ms, 500ms  
This stream returns all available depth, which includes UI and API orders.
    
    
    Code
    
    {
      "data": {
        "E": 1771828614381, // Event time (ms)
        "T": 1771828614258, // Matching time (ms)
        "U": 42648947917, // First updateId in this event
        "a": [
          ["0.07680652", "0.00000000"],
          ["0.08529794", "0.00000000"]
        ],
        "b": [
          ["0.08513788", "0.00000000"],
          ["0.08520502", "23.47000000"],
          ["0.08521196", "320.94000000"],
          ["0.08529880", "0.00000000"],
          ["0.08529885", "0.00000000"]
        ],
        "e": "depthUpdate",
        "pu": 42648947321, // Previous updateId from the last push
        "s": "ALPHA_474USDT",
        "u": 42648948229 // Last updateId in this event
      },
      "stream": "alpha_474usdt@fulldepth@500ms"
    }

* * *

### came@contractAddress@chainId@kline_<interval>

interval: 1s, 1m, 5m, 15m, 1h, 4h, 1d
    
    
    Code
    
    {
      "data": {
        "ca": "G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501", // Contract address@Chain ID
        "e": "kline",
        "k": {
          "c": "0.15584957424118055058", // Close price
          "ct": 1771828656000, // Kline close time
          "h": "0.15584957424118055058", // High price
          "i": "1s", // Interval
          "l": "0.15584372258086979622", // Low price
          "o": "0.15584372258086979622", // Open price
          "ot": 1771828655000, // Kline open time
          "v": "2.8584092999332775480" // Volume
        }
      },
      "stream": "came@G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501@kline_1s"
    }

* * *

### <symbol>@bookTicker
    
    
    Code
    
    {
      "data": {
        "A": "2.00353200", // ask1Quantity
        "B": "0.91076900", // bid1Quantity
        "E": 1773108379067, // eventTime
        "T": 1773108379054, // transactionTime
        "a": "9.30000000", // ask1Price
        "b": "8.30000000", // bid1Price
        "e": "bookTicker", // eventType
        "s": "ALPHA_116USDT", // symbol
        "u": 6663207693 // updateId
      },
      "stream": "alpha_116usdt@bookTicker"
    }

* * *

### !bookTicker
    
    
    Code
    
    {
      "data": {
        "A": "2.00353200", // ask1Quantity
        "B": "0.91076900", // bid1Quantity
        "E": 1773108379067, // eventTime
        "T": 1773108379054, // transactionTime
        "a": "9.30000000", // ask1Price
        "b": "8.30000000", // bid1Price
        "e": "bookTicker", // eventType
        "s": "ALPHA_116USDT", // symbol
        "u": 6663207693 // updateId
      },
      "stream": "!bookTicker"
    }

* * *

### <symbol>@miniTicker
    
    
    Code
    
    {
      "data": {
        "E": 1773109449908, // eventTime
        "c": "8.40000000", // closePrice
        "e": "24hrMiniTicker", // eventType
        "h": "8.50000000", // highPrice
        "l": "8.30000000", // lowPrice
        "o": "8.40000000", // openPrice
        "q": "543810.36005090", // quoteVolume
        "s": "ALPHA_116USDT", // symbol
        "v": "64739.03978900" // volume
      },
      "stream": "alpha_116usdt@miniTicker"
    }

* * *

### !miniTicker@arr
    
    
    Code
    
    {
      "data": {
        "E": 1773109449908, // eventTime
        "c": "8.40000000", // closePrice
        "e": "24hrMiniTicker", // eventType
        "h": "8.50000000", // highPrice
        "l": "8.30000000", // lowPrice
        "o": "8.40000000", // openPrice
        "q": "543810.36005090", // quoteVolume
        "s": "ALPHA_116USDT", // symbol
        "v": "64739.03978900" // volume
      },
      "stream": "!miniTicker@arr"
    }

* * *

### <symbol>@ticker
    
    
    Code
    
    {
      "data": {
        "C": 1773109631555, // endTime
        "E": 1773109631569, // eventTime
        "F": 19847634, // firstTradeId
        "L": 19911287, // lastTradeId
        "O": 1773023220000, // startTime
        "P": "0.00", // priceChangePercent
        "Q": "0.49293200", // lastTradeVolume
        "c": "8.40000000", // closePrice
        "e": "24hrTicker", // eventType
        "h": "8.50000000", // highPrice
        "l": "8.30000000", // lowPrice
        "n": 217505, // tradeNum
        "o": "8.40000000", // openPrice
        "p": "0.00000000", // priceChange
        "q": "543907.35169250", // quoteVolume
        "s": "ALPHA_116USDT", // symbol
        "v": "64750.63418500", // volume
        "w": "8.40003127" // averagePrice
      },
      "stream": "alpha_116usdt@ticker"
    }

* * *

### !ticker@arr
    
    
    Code
    
    {
      "data": {
        "C": 1773109631555, // endTime
        "E": 1773109631569, // eventTime
        "F": 19847634, // firstTradeId
        "L": 19911287, // lastTradeId
        "O": 1773023220000, // startTime
        "P": "0.00", // priceChangePercent
        "Q": "0.49293200", // lastTradeVolume
        "c": "8.40000000", // closePrice
        "e": "24hrTicker", // eventType
        "h": "8.50000000", // highPrice
        "l": "8.30000000", // lowPrice
        "n": 217505, // tradeNum
        "o": "8.40000000", // openPrice
        "p": "0.00000000", // priceChange
        "q": "543907.35169250", // quoteVolume
        "s": "ALPHA_116USDT", // symbol
        "v": "64750.63418500", // volume
        "w": "8.40003127" // averagePrice
      },
      "stream": "!ticker@arr"
    }

* * *

### <symbol>@trade
    
    
    Code
    
    {
      "data": {
        "E": 1773110023891, // eventTime
        "T": 1773110023877, // tradeTime
        "e": "trade", // eventType
        "m": false, // isBuyerMaker
        "p": "8.40000000", // fillPrice
        "q": "0.97915700", // fillQty
        "s": "ALPHA_116USDT", // symbol
        "t": 19911650 // tradeId
      },
      "stream": "alpha_116usdt@trade"
    }

* * *

### <symbol>@depth<levels>@<interval>

levels: optional, available values: [5, 10, 20]  
interval: optional, available values: [0ms, 100ms, 500ms]  
Please note that only UI orders will be shown.
    
    
    Code
    
    {
      "data": {
        "E": 1773110222878, // eventTime
        "T": 1773110222767, // transactionTime
        "U": 6663367135, // firstUpdateId
        "a": [
          [
            "8.30000000", // price
            "8.02776700" // qty
          ]
        ],
        "b": [
          [
            "8.40000000", // price
            "1266.84789600" // qty
          ]
        ],
        "e": "depthUpdate", // eventType
        "pu": 6663366971, // previousUpdateId
        "s": "ALPHA_116USDT", // symbol
        "u": 6663367147 // lastUpdateId
      },
      "stream": "alpha_116usdt@depth"
    }

* * *

### <symbol>@kline_<interval>

available values: [1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M]
    
    
    Code
    
    {
      "data": {
        "E": 1773111055144, // eventTime
        "e": "kline", // eventType
        "k": {
          "B": "0", // ignore
          "L": 19912765, // lastTradeId
          "Q": "534.64960920", // takerBuyQuoteAssetVolume
          "T": 1773111059999, // endTime
          "V": "63.64876300", // takerBuyBaseAssetVolume
          "c": "8.40000000", // closePrice
          "f": 19912696, // firstTradeId
          "h": "8.40000000", // highPrice
          "i": "1m", // interval
          "l": "8.40000000", // lowPrice
          "n": 218, // tradeNum
          "o": "8.40000000", // openPrice
          "q": "534.64960920", // quoteAssetVolume
          "s": "ALPHA_116USDT", // symbol
          "t": 1773111000000, // startTime
          "v": "63.64876300", // volume
          "x": false // klineComplete
        },
        "s": "ALPHA_116USDT" // symbol
      },
      "stream": "alpha_116usdt@kline_1m"
    }

* * *

## How to maintain a local order book copy

The `<symbol>@fulldepth@<interval>` stream and the [Full Depth] snapshot share the same update ID space (`U` / `u` / `pu` / `lastUpdateId`), so a local order book copy can be built and maintained as follows:

  1. Open a stream to `wss://nbstream.binance.com/w3w/wsa/stream` and subscribe to `<symbol>@fulldepth@<interval>` (e.g. `alpha_111usdt@fulldepth@100ms`) by sending: `{"method":"SUBSCRIBE","params":["alpha_111usdt@fulldepth@100ms"],"id":1}`
  2. Buffer the events you receive from the stream. For the same price, the latest received update covers the previous one.
  3. Get a depth snapshot from `GET https://www.binance.com/bapi/defi/v1/public/alpha-trade/fullDepth?symbol=ALPHA_111USDT&limit=1000` (public endpoint, no authentication required; valid `limit` values: 5, 10, 20, 50, 100, 500, 1000, default 500).
  4. Drop any event where `u` is < `lastUpdateId` in the snapshot.
  5. The first processed event should have `pu` <= `lastUpdateId` AND `u` >= `lastUpdateId`. Note that `lastUpdateId` frequently falls between `pu` and `U` of that event — this is normal (see the notes below); do NOT require `U` <= `lastUpdateId`.
  6. While listening to the stream, each new event's `pu` should be equal to the previous event's `u`, otherwise re-initialize the process from step 3.
  7. The data in each event is the ABSOLUTE quantity for a price level.
  8. If the quantity is 0, REMOVE the price level.
  9. Receiving an event that removes a price level that is not in your local order book can happen and is normal.



Note — Differences from Spot/Futures depth streams:

  * U is not gap-free. Between consecutive events, `U` is generally greater than the previous event's `u` \+ 1 (gaps ranging from tens to thousands of update IDs are routinely observed). The `U == previous u + 1` continuity check used for Spot/Futures depth streams does NOT apply to Alpha. Use `pu` (step 6) as the only continuity anchor.
  * Do not mix depth views. `@fulldepth@<interval>` events and the `fullDepth` snapshot include both UI and API orders, while the `<symbol>@depth<levels>@<interval>` stream includes UI orders only. Building a book from the `@depth` stream on top of a `fullDepth` snapshot produces inconsistent results.
  * Include the interval suffix. The documented stream name is `<symbol>@fulldepth@<interval>` (0ms, 100ms, 500ms).
  * Quiet periods. For low-activity symbols the order book may stay unchanged for many seconds: the snapshot `lastUpdateId` stops advancing and no events are pushed. Do not treat the absence of events alone as a disconnection — rely on the `pu` check on the next received event plus standard WebSocket ping/pong.



Was this page helpful?

Last modified on November 12, 2026

[General Info](/en/docs/products/alpha/general-info)[Quick Start](/en/docs/products/alpha/quick-start)

---

# WebSocket 行情接口

## 基本信息

  * 本篇所列出的所有wss接口的baseurl为: `wss://nbstream.binance.com/w3w/wsa/stream`



## 实时订阅/取消数据流

  * 以下数据可以通过 WebSocket 发送以实现订阅或取消订阅数据流。示例如下.
  * 请求中的id被用作唯一标识来区分来回传递的消息。以下格式被接受:
    * 64位有符号整数
    * 字母数字字符串；最大长度36
    * null
  * 如果相应内容中的result 为 null，表示请求发送成功。



### 订阅一个信息流

请求
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["came@allTokens@ticker24"],
      "id": 1
    }

响应
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

* * *

### 取消订阅一个信息流

请求
    
    
    Code
    
    {
      "method": "UNSUBSCRIBE",
      "params": ["came@allTokens@ticker24"],
      "id": 1
    }

响应
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

* * *

### 已订阅信息流

请求
    
    
    Code
    
    {
      "method": "LIST_SUBSCRIPTION",
      "id": 3
    }

响应
    
    
    Code
    
    {
      "result": ["came@allTokens@ticker24"],
      "id": 3
    }

* * *

## Streams

### came@allTokens@ticker24
    
    
    Code
    
    {
      "data": {
        "d": [
          {
            "ca": "0x8fce7206e3043dd360f115afa956ee31b90b787c@56", // 合约地址@链ID
            "cnt24": 10426, // 24小时成交笔数
            "fdv": "72834145.18711072", // 完全稀释市值 (FDV)
            "hc": "6822", // 持有者数量
            "liq": "1442996.98151177662835", // 流动性
            "mc": "13542034.24008014", // 市值
            "p": "0.072849536538593663", // 当前价格
            "pc24": "-2.32", // 24小时价格变化%
            "s": "1",
            "t": 1771825733000, // 时间戳 (ms)
            "vol24": "12930712.213702157742688594285" // 24小时交易量
          }
        ],
        "e": "tickerList"
      },
      "stream": "came@allTokens@ticker24"
    }

* * *

### <symbol>@aggTrade
    
    
    Code
    
    {
      "data": {
        "E": 1771828569861, // 事件时间 (ms)
        "T": 1771828569702, // 成交时间 (ms)
        "a": 2684294, // 聚合交易ID
        "e": "aggTrade", // 事件类型
        "f": 2684294, // 被归集的首个交易ID
        "l": 2684294, // 末个交易ID
        "m": false, // 是否为做市方
        "p": "0.08530000", // 成交价格
        "q": "879.24000000", // 成交数量
        "s": "ALPHA_474USDT" // 交易对符号
      },
      "stream": "alpha_474usdt@aggTrade"
    }

* * *

### <symbol>@fulldepth@<interval>

interval: 0ms, 100ms, 500ms  
这条数据流会返回所有可用的深度信息，其中包括 UI 和 API 的订单
    
    
    Code
    
    {
      "data": {
        "E": 1771828614381, // 事件时间 (ms)
        "T": 1771828614258, // 撮合时间 (ms)
        "U": 42648947917, // 本次更新首个updateId
        "a": [
          ["0.07680652", "0.00000000"],
          ["0.08529794", "0.00000000"]
        ],
        "b": [
          ["0.08513788", "0.00000000"],
          ["0.08520502", "23.47000000"],
          ["0.08521196", "320.94000000"],
          ["0.08529880", "0.00000000"],
          ["0.08529885", "0.00000000"]
        ],
        "e": "depthUpdate",
        "pu": 42648947321, // 上次推送的updateId
        "s": "ALPHA_474USDT",
        "u": 42648948229 // 本次更新末个updateId
      },
      "stream": "alpha_474usdt@fulldepth@500ms"
    }

* * *

### came@contractAddress@chainId@kline_<interval>

interval: 1s, 1m, 5m, 15m, 1h, 4h, 1d
    
    
    Code
    
    {
      "data": {
        "ca": "G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501", // 合约地址@链ID
        "e": "kline",
        "k": {
          "c": "0.15584957424118055058", // 收盘价
          "ct": 1771828656000, // k线结束时间
          "h": "0.15584957424118055058", // 最高价
          "i": "1s", // interval
          "l": "0.15584372258086979622", // 最低价
          "o": "0.15584372258086979622", // 开盘价
          "ot": 1771828655000, // k线开始时间
          "v": "2.8584092999332775480" // 成交量
        }
      },
      "stream": "came@G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501@kline_1s"
    }

* * *

### <symbol>@bookTicker
    
    
    Code
    
    {
      "data": {
        "A": "2.00353200", // 卖一数量
        "B": "0.91076900", // 买一数量
        "E": 1773108379067, // 事件时间
        "T": 1773108379054, // 成交时间/交易时间
        "a": "9.30000000", // 卖一价格
        "b": "8.30000000", // 买一价格
        "e": "bookTicker", // 事件类型
        "s": "ALPHA_116USDT", // 交易对
        "u": 6663207693 // 更新 ID
      },
      "stream": "alpha_116usdt@bookTicker"
    }

* * *

### !bookTicker
    
    
    Code
    
    {
      "data": {
        "A": "2.00353200", // 卖一数量
        "B": "0.91076900", // 买一数量
        "E": 1773108379067, // 事件时间
        "T": 1773108379054, // 成交时间/交易时间
        "a": "9.30000000", // 卖一价格
        "b": "8.30000000", // 买一价格
        "e": "bookTicker", // 事件类型
        "s": "ALPHA_116USDT", // 交易对
        "u": 6663207693 // 更新 ID
      },
      "stream": "!bookTicker"
    }

* * *

### <symbol>@miniTicker
    
    
    Code
    
    {
      "data": {
        "E": 1773109449908, // 事件时间
        "c": "8.40000000", // 收盘价
        "e": "24hrMiniTicker", // 事件类型
        "h": "8.50000000", // 最高价
        "l": "8.30000000", // 最低价
        "o": "8.40000000", // 开盘价
        "q": "543810.36005090", // 计价资产成交额
        "s": "ALPHA_116USDT", // 交易对
        "v": "64739.03978900" // 基础资产成交量
      },
      "stream": "alpha_116usdt@miniTicker"
    }

* * *

### !miniTicker@arr
    
    
    Code
    
    {
      "data": {
        "E": 1773109449908, // 事件时间
        "c": "8.40000000", // 收盘价
        "e": "24hrMiniTicker", // 事件类型
        "h": "8.50000000", // 最高价
        "l": "8.30000000", // 最低价
        "o": "8.40000000", // 开盘价
        "q": "543810.36005090", // 计价资产成交额
        "s": "ALPHA_116USDT", // 交易对
        "v": "64739.03978900" // 基础资产成交量
      },
      "stream": "!miniTicker@arr"
    }

* * *

### <symbol>@ticker
    
    
    Code
    
    {
      "data": {
        "C": 1773109631555, // 统计结束时间
        "E": 1773109631569, // 事件时间
        "F": 19847634, // 首笔成交 ID
        "L": 19911287, // 末笔成交 ID
        "O": 1773023220000, // 统计开始时间
        "P": "0.00", // 涨跌幅
        "Q": "0.49293200", // 最近一笔成交量
        "c": "8.40000000", // 收盘价
        "e": "24hrTicker", // 事件类型
        "h": "8.50000000", // 最高价
        "l": "8.30000000", // 最低价
        "n": 217505, // 成交笔数
        "o": "8.40000000", // 开盘价
        "p": "0.00000000", // 涨跌额
        "q": "543907.35169250", // 计价资产成交额
        "s": "ALPHA_116USDT", // 交易对
        "v": "64750.63418500", // 基础资产成交量
        "w": "8.40003127" // 平均价
      },
      "stream": "alpha_116usdt@ticker"
    }

* * *

### !ticker@arr
    
    
    Code
    
    {
      "data": {
        "C": 1773109631555, // 统计结束时间
        "E": 1773109631569, // 事件时间
        "F": 19847634, // 首笔成交 ID
        "L": 19911287, // 末笔成交 ID
        "O": 1773023220000, // 统计开始时间
        "P": "0.00", // 涨跌幅
        "Q": "0.49293200", // 最近一笔成交量
        "c": "8.40000000", // 收盘价
        "e": "24hrTicker", // 事件类型
        "h": "8.50000000", // 最高价
        "l": "8.30000000", // 最低价
        "n": 217505, // 成交笔数
        "o": "8.40000000", // 开盘价
        "p": "0.00000000", // 涨跌额
        "q": "543907.35169250", // 计价资产成交额
        "s": "ALPHA_116USDT", // 交易对
        "v": "64750.63418500", // 基础资产成交量
        "w": "8.40003127" // 平均价
      },
      "stream": "!ticker@arr"
    }

* * *

### <symbol>@trade
    
    
    Code
    
    {
      "data": {
        "E": 1773110023891, // 事件时间
        "T": 1773110023877, // 成交时间
        "e": "trade", // 事件类型
        "m": false, // 是否为买方挂单成交
        "p": "8.40000000", // 成交价
        "q": "0.97915700", // 成交量
        "s": "ALPHA_116USDT", // 交易对
        "t": 19911650 // 成交 ID
      },
      "stream": "alpha_116usdt@trade"
    }

* * *

### <symbol>@depth<levels>@<interval>

levels：可选，取值：[5, 10, 20]  
interval：可选，取值：[0ms, 100ms, 500ms]  
请注意：这里只会展示 UI 订单。
    
    
    Code
    
    {
      "data": {
        "E": 1773110222878, // 事件时间
        "T": 1773110222767, // 成交时间/交易时间
        "U": 6663367135, // 首个更新 ID
        "a": [
          [
            "8.30000000", // 价格
            "8.02776700" // 数量
          ]
        ],
        "b": [
          [
            "8.40000000", // 价格
            "1266.84789600" // 数量
          ]
        ],
        "e": "depthUpdate", // 事件类型
        "pu": 6663366971, // 上一个更新 ID
        "s": "ALPHA_116USDT", // 交易对
        "u": 6663367147 // 最后更新 ID
      },
      "stream": "alpha_116usdt@depth"
    }

* * *

### <symbol>@kline_<interval>

可选 interval 取值：[1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M]
    
    
    Code
    
    {
      "data": {
        "E": 1773111055144, // 事件时间
        "e": "kline", // 事件类型
        "k": {
          "B": "0", // 忽略
          "L": 19912765, // 末笔成交 ID
          "Q": "534.64960920", // 主动买入成交额
          "T": 1773111059999, // K 线结束时间
          "V": "63.64876300", // 主动买入成交量
          "c": "8.40000000", // 收盘价
          "f": 19912696, // 首笔成交 ID
          "h": "8.40000000", // 最高价
          "i": "1m", // K 线周期
          "l": "8.40000000", // 最低价
          "n": 218, // 成交笔数
          "o": "8.40000000", // 开盘价
          "q": "534.64960920", // 成交额
          "s": "ALPHA_116USDT", // 交易对
          "t": 1773111000000, // K 线开始时间
          "v": "63.64876300", // 成交量
          "x": false // K 线是否已完结
        },
        "s": "ALPHA_116USDT" // 交易对
      },
      "stream": "alpha_116usdt@kline_1m"
    }

* * *

## 如何正确在本地维护一个 order book 副本

`<symbol>@fulldepth@<interval>` 流与 [Full Depth] 快照共享同一套 update ID 空间（`U` / `u` / `pu` / `lastUpdateId`），可以按以下步骤构建并维护本地 order book 副本：

  1. 连接 `wss://nbstream.binance.com/w3w/wsa/stream` 并订阅 `<symbol>@fulldepth@<interval>`（如 `alpha_111usdt@fulldepth@100ms`），发送： `{"method":"SUBSCRIBE","params":["alpha_111usdt@fulldepth@100ms"],"id":1}`
  2. 缓冲从流中收到的事件。同一价格以最后收到的更新为准。
  3. 通过快照接口获取深度：`GET https://www.binance.com/bapi/defi/v1/public/alpha-trade/fullDepth?symbol=ALPHA_111USDT&limit=1000`（公开接口，无需鉴权；`limit` 有效值：5、10、20、50、100、500、1000，默认 500）。
  4. 丢弃任何 `u` < 快照 `lastUpdateId` 的事件。
  5. 第一个被处理的事件应满足 `pu` <= `lastUpdateId` 且 `u` >= `lastUpdateId`。注意：`lastUpdateId` 经常落在该事件的 `pu` 与 `U` 之间——这是正常现象（见下方说明），不要要求 `U` <= `lastUpdateId`。
  6. 持续监听流时，每个新事件的 `pu` 应等于上一个事件的 `u`；否则从步骤 3 重新初始化。
  7. 每个事件中的数据是该价格档位的绝对数量。
  8. 数量为 0 时，移除该价格档位。
  9. 收到移除本地 order book 中不存在档位的事件是正常现象。



Note — 与 Spot / 合约 depth 流的差异：

  * U 并非连续递增。相邻事件之间 `U` 通常大于上一事件的 `u` \+ 1（实测常见几十到几千的 update ID 间隔）。Spot / 合约 depth 流使用的 `U == 上一事件 u + 1` 连续性检查在 Alpha 不适用，请以 `pu`（步骤 6）作为唯一的连续性锚点。
  * 不要混用深度视图。`@fulldepth@<interval>` 事件与 `fullDepth` 快照同时包含 UI 和 API 订单，而 `<symbol>@depth<levels>@<interval>` 流仅包含 UI 订单。用 `@depth` 流叠加 `fullDepth` 快照构建订单簿会产生不一致的结果。
  * 订阅时请带 interval 后缀。文档化的流名为 `<symbol>@fulldepth@<interval>`（0ms、100ms、500ms）。
  * 静默期。低活跃交易对的订单簿可能连续数秒无变化：快照 `lastUpdateId` 停止推进、也无事件推送。不要仅凭"没收到事件"判定断连——应结合下一个事件到达时的 `pu` 校验以及标准 WebSocket ping/pong 判断。



此页面是否有帮助？

Last modified on November 12, 2026

[通用信息](/zh-CN/docs/products/alpha/general-info)[快速开始](/zh-CN/docs/products/alpha/quick-start)