---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-18 02:46:52.865610
---

# Alpha WebSocket Market Streams

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/1.0.0/schema.yaml

Access Alpha market streams over WebSocket.

通过 WebSocket 访问 Alpha 行情数据流。

版本: 1.0.0

## 服务地址

- `wss://nbstream.binance.com/w3w/wsa/stream`

## 接口列表

- `{symbol}@aggTrade` — Aggregate Trade Stream
- `!bookTicker` — All Book Ticker Stream
- `!miniTicker@arr` — All Mini Ticker Stream
- `!ticker@arr` — All Ticker Stream
- `came@allTokens@ticker24` — All Tokens 24h Ticker Stream
- `{symbol}@bookTicker` — Book Ticker Stream
- `{symbol}@depth{levels}@{interval}` — Partial Depth Stream
- `{symbol}@fulldepth@{interval}` — Full Depth Stream
- `{symbol}@kline_{interval}` — Kline Stream
- `came@{contractAddress}@{chainId}@kline_{interval}` — Contract Kline Stream
- `{symbol}@miniTicker` — Mini Ticker Stream
- `{symbol}@ticker` — Ticker Stream
- `{symbol}@trade` — Trade Stream

## Aggregate Trade Stream（聚合成交流）

流名称: `{symbol}@aggTrade`

Pushes aggregate trade updates for a symbol.

推送指定交易对的聚合成交更新。

Operation ID: `aggregateTradeStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@aggTrade"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Aggregate Trade Stream / 聚合成交流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| E | integer (int64) |  | Event time (ms)<br>事件时间 (ms)<br>例: `1771828569861` |
| T | integer (int64) |  | Trade time (ms)<br>成交时间 (ms)<br>例: `1771828569702` |
| a | integer (int64) |  | Aggregated trade ID<br>聚合交易ID<br>例: `2684294` |
| f | integer (int64) |  | First trade ID in the aggregation<br>被归集的首个交易ID<br>例: `2684294` |
| l | integer (int64) |  | Last trade ID in the aggregation<br>末个交易ID<br>例: `2684294` |
| m | boolean |  | Is the buyer the market maker<br>是否为做市方<br>例: `False` |
| p | string |  | Price<br>成交价格<br>例: `0.08530000` |
| q | string |  | Quantity<br>成交数量<br>例: `879.24000000` |
| s | string |  | Symbol<br>交易对符号<br>例: `ALPHA_474USDT` |

```json
{
  "e": "aggTrade",
  "E": 1771828569861,
  "T": 1771828569702,
  "a": 2684294,
  "f": 2684294,
  "l": 2684294,
  "m": false,
  "p": "0.08530000",
  "q": "879.24000000",
  "s": "ALPHA_474USDT"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@aggTrade` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `aggTrade` |
| data.E | integer (int64) |  | Event time (ms)<br>事件时间 (ms)<br>例: `1771828569861` |
| data.T | integer (int64) |  | Trade time (ms)<br>成交时间 (ms)<br>例: `1771828569702` |
| data.a | integer (int64) |  | Aggregated trade ID<br>聚合交易ID<br>例: `2684294` |
| data.f | integer (int64) |  | First trade ID in the aggregation<br>被归集的首个交易ID<br>例: `2684294` |
| data.l | integer (int64) |  | Last trade ID in the aggregation<br>末个交易ID<br>例: `2684294` |
| data.m | boolean |  | Is the buyer the market maker<br>是否为做市方<br>例: `False` |
| data.p | string |  | Price<br>成交价格<br>例: `0.08530000` |
| data.q | string |  | Quantity<br>成交数量<br>例: `879.24000000` |
| data.s | string |  | Symbol<br>交易对符号<br>例: `ALPHA_474USDT` |

```json
{
  "stream": "alpha_116usdt@aggTrade",
  "data": {
    "e": "aggTrade",
    "E": 1771828569861,
    "T": 1771828569702,
    "a": 2684294,
    "f": 2684294,
    "l": 2684294,
    "m": false,
    "p": "0.08530000",
    "q": "879.24000000",
    "s": "ALPHA_474USDT"
  }
}
```

## All Book Ticker Stream（全市场最优挂单流）

流名称: `!bookTicker`

Pushes best bid/ask updates for all symbols.

推送全市场一档买卖盘更新。

Operation ID: `allBookTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "!bookTicker"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：All Book Ticker Stream / 全市场最优挂单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `bookTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773108379067` |
| T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773108379054` |
| u | integer (int64) |  | updateId<br>更新 ID<br>例: `6663207693` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| b | string |  | bid1Price<br>买一价格<br>例: `8.30000000` |
| B | string |  | bid1Quantity<br>买一数量<br>例: `0.91076900` |
| a | string |  | ask1Price<br>卖一价格<br>例: `9.30000000` |
| A | string |  | ask1Quantity<br>卖一数量<br>例: `2.00353200` |

```json
{
  "e": "bookTicker",
  "E": 1773108379067,
  "T": 1773108379054,
  "u": 6663207693,
  "s": "ALPHA_116USDT",
  "b": "8.30000000",
  "B": "0.91076900",
  "a": "9.30000000",
  "A": "2.00353200"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!bookTicker` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `bookTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773108379067` |
| data.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773108379054` |
| data.u | integer (int64) |  | updateId<br>更新 ID<br>例: `6663207693` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.b | string |  | bid1Price<br>买一价格<br>例: `8.30000000` |
| data.B | string |  | bid1Quantity<br>买一数量<br>例: `0.91076900` |
| data.a | string |  | ask1Price<br>卖一价格<br>例: `9.30000000` |
| data.A | string |  | ask1Quantity<br>卖一数量<br>例: `2.00353200` |

```json
{
  "stream": "!bookTicker",
  "data": {
    "e": "bookTicker",
    "E": 1773108379067,
    "T": 1773108379054,
    "u": 6663207693,
    "s": "ALPHA_116USDT",
    "b": "8.30000000",
    "B": "0.91076900",
    "a": "9.30000000",
    "A": "2.00353200"
  }
}
```

## All Mini Ticker Stream（全市场简略行情流）

流名称: `!miniTicker@arr`

Pushes mini ticker statistics for all symbols.

推送全市场简略行情统计。

Operation ID: `allMiniTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "!miniTicker@arr"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：All Mini Ticker Stream / 全市场简略行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `24hrMiniTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109449908` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| v | string |  | volume<br>基础资产成交量<br>例: `64739.03978900` |
| q | string |  | quoteVolume<br>计价资产成交额<br>例: `543810.36005090` |

```json
{
  "e": "24hrMiniTicker",
  "E": 1773109449908,
  "s": "ALPHA_116USDT",
  "c": "8.40000000",
  "o": "8.40000000",
  "h": "8.50000000",
  "l": "8.30000000",
  "v": "64739.03978900",
  "q": "543810.36005090"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!miniTicker@arr` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `24hrMiniTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109449908` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| data.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| data.h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| data.l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| data.v | string |  | volume<br>基础资产成交量<br>例: `64739.03978900` |
| data.q | string |  | quoteVolume<br>计价资产成交额<br>例: `543810.36005090` |

```json
{
  "stream": "!miniTicker@arr",
  "data": {
    "e": "24hrMiniTicker",
    "E": 1773109449908,
    "s": "ALPHA_116USDT",
    "c": "8.40000000",
    "o": "8.40000000",
    "h": "8.50000000",
    "l": "8.30000000",
    "v": "64739.03978900",
    "q": "543810.36005090"
  }
}
```

## All Ticker Stream（全市场完整行情流）

流名称: `!ticker@arr`

Pushes full ticker statistics for all symbols.

推送全市场完整行情统计。

Operation ID: `allTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "!ticker@arr"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：All Ticker Stream / 全市场完整行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `24hrTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109631569` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| p | string |  | priceChange<br>涨跌额<br>例: `0.00000000` |
| P | string |  | priceChangePercent<br>涨跌幅<br>例: `0.00` |
| w | string |  | averagePrice<br>平均价<br>例: `8.40003127` |
| c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.49293200` |
| o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| v | string |  | volume<br>基础资产成交量<br>例: `64750.63418500` |
| q | string |  | quoteVolume<br>计价资产成交额<br>例: `543907.35169250` |
| O | integer (int64) |  | startTime<br>统计开始时间<br>例: `1773023220000` |
| C | integer (int64) |  | endTime<br>统计结束时间<br>例: `1773109631555` |
| F | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19847634` |
| L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19911287` |
| n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `217505` |

```json
{
  "e": "24hrTicker",
  "E": 1773109631569,
  "s": "ALPHA_116USDT",
  "p": "0.00000000",
  "P": "0.00",
  "w": "8.40003127",
  "c": "8.40000000",
  "Q": "0.49293200",
  "o": "8.40000000",
  "h": "8.50000000",
  "l": "8.30000000",
  "v": "64750.63418500",
  "q": "543907.35169250",
  "O": 1773023220000,
  "C": 1773109631555,
  "F": 19847634,
  "L": 19911287,
  "n": 217505
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!ticker@arr` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `24hrTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109631569` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.p | string |  | priceChange<br>涨跌额<br>例: `0.00000000` |
| data.P | string |  | priceChangePercent<br>涨跌幅<br>例: `0.00` |
| data.w | string |  | averagePrice<br>平均价<br>例: `8.40003127` |
| data.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| data.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.49293200` |
| data.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| data.h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| data.l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| data.v | string |  | volume<br>基础资产成交量<br>例: `64750.63418500` |
| data.q | string |  | quoteVolume<br>计价资产成交额<br>例: `543907.35169250` |
| data.O | integer (int64) |  | startTime<br>统计开始时间<br>例: `1773023220000` |
| data.C | integer (int64) |  | endTime<br>统计结束时间<br>例: `1773109631555` |
| data.F | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19847634` |
| data.L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19911287` |
| data.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `217505` |

```json
{
  "stream": "!ticker@arr",
  "data": {
    "e": "24hrTicker",
    "E": 1773109631569,
    "s": "ALPHA_116USDT",
    "p": "0.00000000",
    "P": "0.00",
    "w": "8.40003127",
    "c": "8.40000000",
    "Q": "0.49293200",
    "o": "8.40000000",
    "h": "8.50000000",
    "l": "8.30000000",
    "v": "64750.63418500",
    "q": "543907.35169250",
    "O": 1773023220000,
    "C": 1773109631555,
    "F": 19847634,
    "L": 19911287,
    "n": 217505
  }
}
```

## All Tokens 24h Ticker Stream（全部代币 24 小时行情流）

流名称: `came@allTokens@ticker24`

Pushes 24h ticker-like metrics for all tokens.

推送全部代币的 24 小时行情指标。

Operation ID: `allTokens24hTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "came@allTokens@ticker24"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：All Tokens 24h Ticker Stream / 全部代币 24 小时行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `tickerList` |
| d | object[] |  | Per-token 24-hour ticker metrics<br>按代币维度的 24 小时行情指标 |
| d[].ca | string |  | Contract address@chain ID<br>合约地址@链 ID<br>例: `0x8fce...@56` |
| d[].cnt24 | integer (int64) |  | Number of trades in the last 24 hours<br>过去 24 小时成交笔数<br>例: `10426` |
| d[].fdv | string |  | Fully diluted valuation<br>完全稀释估值<br>例: `72834145.18711072` |
| d[].hc | string |  | Number of holders<br>持有人数量<br>例: `6822` |
| d[].liq | string |  | Liquidity<br>流动性<br>例: `1442996.98151177662835` |
| d[].mc | string |  | Market cap<br>市值<br>例: `13542034.24008014` |
| d[].p | string |  | Current price<br>当前价格<br>例: `0.072849536538593663` |
| d[].pc24 | string |  | 24-hour price change percent<br>24 小时价格涨跌幅<br>例: `-2.32` |
| d[].s | string |  | Token short identifier<br>代币短标识<br>例: `1` |
| d[].t | integer (int64) |  | Event timestamp in milliseconds<br>事件时间戳（毫秒）<br>例: `1771825733000` |
| d[].vol24 | string |  | 24-hour volume<br>24 小时成交量<br>例: `12930712.213702157742688594285` |

```json
{
  "e": "tickerList",
  "d": [
    {
      "ca": "0x8fce...@56",
      "cnt24": 10426,
      "fdv": "72834145.18711072",
      "hc": "6822",
      "liq": "1442996.98151177662835",
      "mc": "13542034.24008014",
      "p": "0.072849536538593663",
      "pc24": "-2.32",
      "s": "1",
      "t": 1771825733000,
      "vol24": "12930712.213702157742688594285"
    }
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `came@allTokens@ticker24` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `tickerList` |
| data.d | object[] |  | Per-token 24-hour ticker metrics<br>按代币维度的 24 小时行情指标 |
| data.d[].ca | string |  | Contract address@chain ID<br>合约地址@链 ID<br>例: `0x8fce...@56` |
| data.d[].cnt24 | integer (int64) |  | Number of trades in the last 24 hours<br>过去 24 小时成交笔数<br>例: `10426` |
| data.d[].fdv | string |  | Fully diluted valuation<br>完全稀释估值<br>例: `72834145.18711072` |
| data.d[].hc | string |  | Number of holders<br>持有人数量<br>例: `6822` |
| data.d[].liq | string |  | Liquidity<br>流动性<br>例: `1442996.98151177662835` |
| data.d[].mc | string |  | Market cap<br>市值<br>例: `13542034.24008014` |
| data.d[].p | string |  | Current price<br>当前价格<br>例: `0.072849536538593663` |
| data.d[].pc24 | string |  | 24-hour price change percent<br>24 小时价格涨跌幅<br>例: `-2.32` |
| data.d[].s | string |  | Token short identifier<br>代币短标识<br>例: `1` |
| data.d[].t | integer (int64) |  | Event timestamp in milliseconds<br>事件时间戳（毫秒）<br>例: `1771825733000` |
| data.d[].vol24 | string |  | 24-hour volume<br>24 小时成交量<br>例: `12930712.213702157742688594285` |

```json
{
  "stream": "came@allTokens@ticker24",
  "data": {
    "e": "tickerList",
    "d": [
      {
        "ca": "0x8fce...@56",
        "cnt24": 10426,
        "fdv": "72834145.18711072",
        "hc": "6822",
        "liq": "1442996.98151177662835",
        "mc": "13542034.24008014",
        "p": "0.072849536538593663",
        "pc24": "-2.32",
        "s": "1",
        "t": 1771825733000,
        "vol24": "12930712.213702157742688594285"
      }
    ]
  }
}
```

## Book Ticker Stream（最优挂单流）

流名称: `{symbol}@bookTicker`

Pushes best bid/ask updates for a symbol.

推送指定交易对的一档买卖盘更新。

Operation ID: `bookTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@bookTicker"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Book Ticker Stream / 最优挂单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `bookTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773108379067` |
| T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773108379054` |
| u | integer (int64) |  | updateId<br>更新 ID<br>例: `6663207693` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| b | string |  | bid1Price<br>买一价格<br>例: `8.30000000` |
| B | string |  | bid1Quantity<br>买一数量<br>例: `0.91076900` |
| a | string |  | ask1Price<br>卖一价格<br>例: `9.30000000` |
| A | string |  | ask1Quantity<br>卖一数量<br>例: `2.00353200` |

```json
{
  "e": "bookTicker",
  "E": 1773108379067,
  "T": 1773108379054,
  "u": 6663207693,
  "s": "ALPHA_116USDT",
  "b": "8.30000000",
  "B": "0.91076900",
  "a": "9.30000000",
  "A": "2.00353200"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@bookTicker` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `bookTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773108379067` |
| data.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773108379054` |
| data.u | integer (int64) |  | updateId<br>更新 ID<br>例: `6663207693` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.b | string |  | bid1Price<br>买一价格<br>例: `8.30000000` |
| data.B | string |  | bid1Quantity<br>买一数量<br>例: `0.91076900` |
| data.a | string |  | ask1Price<br>卖一价格<br>例: `9.30000000` |
| data.A | string |  | ask1Quantity<br>卖一数量<br>例: `2.00353200` |

```json
{
  "stream": "alpha_116usdt@bookTicker",
  "data": {
    "e": "bookTicker",
    "E": 1773108379067,
    "T": 1773108379054,
    "u": 6663207693,
    "s": "ALPHA_116USDT",
    "b": "8.30000000",
    "B": "0.91076900",
    "a": "9.30000000",
    "A": "2.00353200"
  }
}
```

## Partial Depth Stream（部分深度流）

流名称: `{symbol}@depth{levels}@{interval}`

Pushes partial depth updates (UI orders only).

推送部分深度更新（仅 UI 订单）。

Operation ID: `partialDepthStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |
| levels | path | string | 是 | Depth levels.<br>深度档位。<br>枚举: `5`, `10`, `20`<br>例: `5` |
| interval | path | string | 是 | Update interval.<br>更新间隔。<br>枚举: `0ms`, `100ms`, `500ms`<br>例: `100ms` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@depth5@100ms"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Partial Depth Stream / 部分深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773110222878` |
| T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773110222767` |
| U | integer (int64) |  | firstUpdateId<br>首个更新 ID<br>例: `6663367135` |
| u | integer (int64) |  | lastUpdateId<br>最后更新 ID<br>例: `6663367147` |
| pu | integer (int64) |  | previousUpdateId<br>上一个更新 ID<br>例: `6663366971` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| b | string[][] |  | bids to be updated<br>需要更新的买单 |
| a | string[][] |  | asks to be updated<br>需要更新的卖单 |

```json
{
  "e": "depthUpdate",
  "E": 1773110222878,
  "T": 1773110222767,
  "U": 6663367135,
  "u": 6663367147,
  "pu": 6663366971,
  "s": "ALPHA_116USDT",
  "b": [
    [
      "0.16479999",
      "0"
    ],
    [
      "0.16480000",
      "18.68000000"
    ]
  ],
  "a": [
    [
      "0.16490000",
      "500.00000000"
    ],
    [
      "0.16500000",
      "0"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@depth5@100ms` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773110222878` |
| data.T | integer (int64) |  | transactionTime<br>成交时间/交易时间<br>例: `1773110222767` |
| data.U | integer (int64) |  | firstUpdateId<br>首个更新 ID<br>例: `6663367135` |
| data.u | integer (int64) |  | lastUpdateId<br>最后更新 ID<br>例: `6663367147` |
| data.pu | integer (int64) |  | previousUpdateId<br>上一个更新 ID<br>例: `6663366971` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.b | string[][] |  | bids to be updated<br>需要更新的买单 |
| data.a | string[][] |  | asks to be updated<br>需要更新的卖单 |

```json
{
  "stream": "alpha_116usdt@depth5@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1773110222878,
    "T": 1773110222767,
    "U": 6663367135,
    "u": 6663367147,
    "pu": 6663366971,
    "s": "ALPHA_116USDT",
    "b": [
      [
        "0.16479999",
        "0"
      ],
      [
        "0.16480000",
        "18.68000000"
      ]
    ],
    "a": [
      [
        "0.16490000",
        "500.00000000"
      ],
      [
        "0.16500000",
        "0"
      ]
    ]
  }
}
```

## Full Depth Stream（全量深度流）

流名称: `{symbol}@fulldepth@{interval}`

Returns all available depth, including UI and API orders.

返回所有可用深度信息，包含 UI 与 API 订单。

Operation ID: `fullDepthStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |
| interval | path | string | 是 | Update interval.<br>更新间隔。<br>枚举: `0ms`, `100ms`, `500ms`<br>例: `500ms` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@fulldepth@500ms"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Full Depth Stream / 全量深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | Event time (ms)<br>事件时间 (ms)<br>例: `1771828614381` |
| T | integer (int64) |  | Matching time (ms)<br>撮合时间 (ms)<br>例: `1771828614258` |
| U | integer (int64) |  | First updateId in this event<br>本次更新首个updateId<br>例: `42648947917` |
| u | integer (int64) |  | Last updateId in this event<br>本次更新末个updateId<br>例: `42648948229` |
| pu | integer (int64) |  | Previous updateId from the last push<br>上次推送的updateId<br>例: `42648947321` |
| s | string |  | Symbol<br>交易对<br>例: `ALPHA_474USDT` |
| b | string[][] |  | bids to be updated<br>需要更新的买单 |
| a | string[][] |  | asks to be updated<br>需要更新的卖单 |

```json
{
  "e": "depthUpdate",
  "E": 1771828614381,
  "T": 1771828614258,
  "U": 42648947917,
  "u": 42648948229,
  "pu": 42648947321,
  "s": "ALPHA_474USDT",
  "b": [
    [
      "0.16479999",
      "0"
    ],
    [
      "0.16480000",
      "18.68000000"
    ]
  ],
  "a": [
    [
      "0.16490000",
      "500.00000000"
    ],
    [
      "0.16500000",
      "0"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@fulldepth@500ms` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | Event time (ms)<br>事件时间 (ms)<br>例: `1771828614381` |
| data.T | integer (int64) |  | Matching time (ms)<br>撮合时间 (ms)<br>例: `1771828614258` |
| data.U | integer (int64) |  | First updateId in this event<br>本次更新首个updateId<br>例: `42648947917` |
| data.u | integer (int64) |  | Last updateId in this event<br>本次更新末个updateId<br>例: `42648948229` |
| data.pu | integer (int64) |  | Previous updateId from the last push<br>上次推送的updateId<br>例: `42648947321` |
| data.s | string |  | Symbol<br>交易对<br>例: `ALPHA_474USDT` |
| data.b | string[][] |  | bids to be updated<br>需要更新的买单 |
| data.a | string[][] |  | asks to be updated<br>需要更新的卖单 |

```json
{
  "stream": "alpha_116usdt@fulldepth@500ms",
  "data": {
    "e": "depthUpdate",
    "E": 1771828614381,
    "T": 1771828614258,
    "U": 42648947917,
    "u": 42648948229,
    "pu": 42648947321,
    "s": "ALPHA_474USDT",
    "b": [
      [
        "0.16479999",
        "0"
      ],
      [
        "0.16480000",
        "18.68000000"
      ]
    ],
    "a": [
      [
        "0.16490000",
        "500.00000000"
      ],
      [
        "0.16500000",
        "0"
      ]
    ]
  }
}
```

## Kline Stream（K 线流）

流名称: `{symbol}@kline_{interval}`

Pushes kline updates for a symbol.

推送指定交易对 K 线更新。

Operation ID: `klineStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |
| interval | path | string | 是 | Kline interval.<br>K 线间隔。<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@kline_1m"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Kline Stream / K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `kline` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773111055144` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| k | object |  |  |
| k.t | integer (int64) |  | startTime<br>K 线开始时间<br>例: `1773111000000` |
| k.T | integer (int64) |  | endTime<br>K 线结束时间<br>例: `1773111059999` |
| k.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| k.f | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19912696` |
| k.L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19912765` |
| k.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| k.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| k.h | string |  | highPrice<br>最高价<br>例: `8.40000000` |
| k.l | string |  | lowPrice<br>最低价<br>例: `8.40000000` |
| k.v | string |  | volume<br>成交量<br>例: `63.64876300` |
| k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `218` |
| k.x | boolean |  | klineComplete<br>K 线是否已完结<br>例: `False` |
| k.q | string |  | quoteAssetVolume<br>成交额<br>例: `534.64960920` |
| k.V | string |  | takerBuyBaseAssetVolume<br>主动买入成交量<br>例: `63.64876300` |
| k.Q | string |  | takerBuyQuoteAssetVolume<br>主动买入成交额<br>例: `534.64960920` |
| k.B | string |  | ignore<br>忽略<br>例: `0` |

```json
{
  "e": "kline",
  "E": 1773111055144,
  "s": "ALPHA_116USDT",
  "k": {
    "t": 1773111000000,
    "T": 1773111059999,
    "s": "ALPHA_116USDT",
    "i": "1m",
    "f": 19912696,
    "L": 19912765,
    "o": "8.40000000",
    "c": "8.40000000",
    "h": "8.40000000",
    "l": "8.40000000",
    "v": "63.64876300",
    "n": 218,
    "x": false,
    "q": "534.64960920",
    "V": "63.64876300",
    "Q": "534.64960920",
    "B": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@kline_1m` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `kline` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773111055144` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.k | object |  |  |
| data.k.t | integer (int64) |  | startTime<br>K 线开始时间<br>例: `1773111000000` |
| data.k.T | integer (int64) |  | endTime<br>K 线结束时间<br>例: `1773111059999` |
| data.k.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.k.i | string |  | interval<br>K 线周期<br>例: `1m` |
| data.k.f | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19912696` |
| data.k.L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19912765` |
| data.k.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| data.k.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| data.k.h | string |  | highPrice<br>最高价<br>例: `8.40000000` |
| data.k.l | string |  | lowPrice<br>最低价<br>例: `8.40000000` |
| data.k.v | string |  | volume<br>成交量<br>例: `63.64876300` |
| data.k.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `218` |
| data.k.x | boolean |  | klineComplete<br>K 线是否已完结<br>例: `False` |
| data.k.q | string |  | quoteAssetVolume<br>成交额<br>例: `534.64960920` |
| data.k.V | string |  | takerBuyBaseAssetVolume<br>主动买入成交量<br>例: `63.64876300` |
| data.k.Q | string |  | takerBuyQuoteAssetVolume<br>主动买入成交额<br>例: `534.64960920` |
| data.k.B | string |  | ignore<br>忽略<br>例: `0` |

```json
{
  "stream": "alpha_116usdt@kline_1m",
  "data": {
    "e": "kline",
    "E": 1773111055144,
    "s": "ALPHA_116USDT",
    "k": {
      "t": 1773111000000,
      "T": 1773111059999,
      "s": "ALPHA_116USDT",
      "i": "1m",
      "f": 19912696,
      "L": 19912765,
      "o": "8.40000000",
      "c": "8.40000000",
      "h": "8.40000000",
      "l": "8.40000000",
      "v": "63.64876300",
      "n": 218,
      "x": false,
      "q": "534.64960920",
      "V": "63.64876300",
      "Q": "534.64960920",
      "B": "0"
    }
  }
}
```

## Contract Kline Stream（合约地址 K 线流）

流名称: `came@{contractAddress}@{chainId}@kline_{interval}`

Pushes kline updates by contractAddress@chainId.

按 contractAddress@chainId 推送 K 线更新。

Operation ID: `contractKlineStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| contractAddress | path | string | 是 | Contract address.<br>合约地址。<br>例: `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` |
| chainId | path | string | 是 | Chain ID.<br>链 ID。<br>例: `CT_501` |
| interval | path | string | 是 | Kline interval.<br>K 线间隔。<br>枚举: `1s`, `1m`, `5m`, `15m`, `1h`, `4h`, `1d`<br>例: `1s` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Contract Kline Stream / 合约地址 K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| ca | string |  | Contract address@Chain ID<br>合约地址@链ID<br>例: `G7vQW...@CT_501` |
| e | string |  | Event type<br>事件类型<br>例: `kline` |
| k | object |  | Kline payload<br>K 线数据 |
| k.o | string |  | Open price<br>开盘价<br>例: `0.15584372258086979622` |
| k.c | string |  | Close price<br>收盘价<br>例: `0.15584957424118055058` |
| k.h | string |  | High price<br>最高价<br>例: `0.15584957424118055058` |
| k.l | string |  | Low price<br>最低价<br>例: `0.15584372258086979622` |
| k.v | string |  | Volume<br>成交量<br>例: `2.8584092999332775480` |
| k.ot | integer (int64) |  | Kline open time<br>k线开始时间<br>例: `1771828655000` |
| k.ct | integer (int64) |  | Kline close time<br>k线结束时间<br>例: `1771828656000` |
| k.i | string |  | Interval<br>周期<br>例: `1s` |

```json
{
  "ca": "G7vQW...@CT_501",
  "e": "kline",
  "k": {
    "o": "0.15584372258086979622",
    "c": "0.15584957424118055058",
    "h": "0.15584957424118055058",
    "l": "0.15584372258086979622",
    "v": "2.8584092999332775480",
    "ot": 1771828655000,
    "ct": 1771828656000,
    "i": "1s"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s` |
| data | object | 是 |  |
| data.ca | string |  | Contract address@Chain ID<br>合约地址@链ID<br>例: `G7vQW...@CT_501` |
| data.e | string |  | Event type<br>事件类型<br>例: `kline` |
| data.k | object |  | Kline payload<br>K 线数据 |
| data.k.o | string |  | Open price<br>开盘价<br>例: `0.15584372258086979622` |
| data.k.c | string |  | Close price<br>收盘价<br>例: `0.15584957424118055058` |
| data.k.h | string |  | High price<br>最高价<br>例: `0.15584957424118055058` |
| data.k.l | string |  | Low price<br>最低价<br>例: `0.15584372258086979622` |
| data.k.v | string |  | Volume<br>成交量<br>例: `2.8584092999332775480` |
| data.k.ot | integer (int64) |  | Kline open time<br>k线开始时间<br>例: `1771828655000` |
| data.k.ct | integer (int64) |  | Kline close time<br>k线结束时间<br>例: `1771828656000` |
| data.k.i | string |  | Interval<br>周期<br>例: `1s` |

```json
{
  "stream": "came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s",
  "data": {
    "ca": "G7vQW...@CT_501",
    "e": "kline",
    "k": {
      "o": "0.15584372258086979622",
      "c": "0.15584957424118055058",
      "h": "0.15584957424118055058",
      "l": "0.15584372258086979622",
      "v": "2.8584092999332775480",
      "ot": 1771828655000,
      "ct": 1771828656000,
      "i": "1s"
    }
  }
}
```

## Mini Ticker Stream（简略行情流）

流名称: `{symbol}@miniTicker`

Pushes 24h rolling mini ticker statistics.

推送 24 小时滚动简略行情统计。

Operation ID: `miniTickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@miniTicker"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Mini Ticker Stream / 简略行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `24hrMiniTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109449908` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| v | string |  | volume<br>基础资产成交量<br>例: `64739.03978900` |
| q | string |  | quoteVolume<br>计价资产成交额<br>例: `543810.36005090` |

```json
{
  "e": "24hrMiniTicker",
  "E": 1773109449908,
  "s": "ALPHA_116USDT",
  "c": "8.40000000",
  "o": "8.40000000",
  "h": "8.50000000",
  "l": "8.30000000",
  "v": "64739.03978900",
  "q": "543810.36005090"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@miniTicker` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `24hrMiniTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109449908` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| data.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| data.h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| data.l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| data.v | string |  | volume<br>基础资产成交量<br>例: `64739.03978900` |
| data.q | string |  | quoteVolume<br>计价资产成交额<br>例: `543810.36005090` |

```json
{
  "stream": "alpha_116usdt@miniTicker",
  "data": {
    "e": "24hrMiniTicker",
    "E": 1773109449908,
    "s": "ALPHA_116USDT",
    "c": "8.40000000",
    "o": "8.40000000",
    "h": "8.50000000",
    "l": "8.30000000",
    "v": "64739.03978900",
    "q": "543810.36005090"
  }
}
```

## Ticker Stream（完整行情流）

流名称: `{symbol}@ticker`

Pushes full 24h rolling ticker statistics.

推送完整 24 小时滚动行情统计。

Operation ID: `tickerStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@ticker"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Ticker Stream / 完整行情流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `24hrTicker` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109631569` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| p | string |  | priceChange<br>涨跌额<br>例: `0.00000000` |
| P | string |  | priceChangePercent<br>涨跌幅<br>例: `0.00` |
| w | string |  | averagePrice<br>平均价<br>例: `8.40003127` |
| c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.49293200` |
| o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| v | string |  | volume<br>基础资产成交量<br>例: `64750.63418500` |
| q | string |  | quoteVolume<br>计价资产成交额<br>例: `543907.35169250` |
| O | integer (int64) |  | startTime<br>统计开始时间<br>例: `1773023220000` |
| C | integer (int64) |  | endTime<br>统计结束时间<br>例: `1773109631555` |
| F | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19847634` |
| L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19911287` |
| n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `217505` |

```json
{
  "e": "24hrTicker",
  "E": 1773109631569,
  "s": "ALPHA_116USDT",
  "p": "0.00000000",
  "P": "0.00",
  "w": "8.40003127",
  "c": "8.40000000",
  "Q": "0.49293200",
  "o": "8.40000000",
  "h": "8.50000000",
  "l": "8.30000000",
  "v": "64750.63418500",
  "q": "543907.35169250",
  "O": 1773023220000,
  "C": 1773109631555,
  "F": 19847634,
  "L": 19911287,
  "n": 217505
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@ticker` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `24hrTicker` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773109631569` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.p | string |  | priceChange<br>涨跌额<br>例: `0.00000000` |
| data.P | string |  | priceChangePercent<br>涨跌幅<br>例: `0.00` |
| data.w | string |  | averagePrice<br>平均价<br>例: `8.40003127` |
| data.c | string |  | closePrice<br>收盘价<br>例: `8.40000000` |
| data.Q | string |  | lastTradeVolume<br>最近一笔成交量<br>例: `0.49293200` |
| data.o | string |  | openPrice<br>开盘价<br>例: `8.40000000` |
| data.h | string |  | highPrice<br>最高价<br>例: `8.50000000` |
| data.l | string |  | lowPrice<br>最低价<br>例: `8.30000000` |
| data.v | string |  | volume<br>基础资产成交量<br>例: `64750.63418500` |
| data.q | string |  | quoteVolume<br>计价资产成交额<br>例: `543907.35169250` |
| data.O | integer (int64) |  | startTime<br>统计开始时间<br>例: `1773023220000` |
| data.C | integer (int64) |  | endTime<br>统计结束时间<br>例: `1773109631555` |
| data.F | integer (int64) |  | firstTradeId<br>首笔成交 ID<br>例: `19847634` |
| data.L | integer (int64) |  | lastTradeId<br>末笔成交 ID<br>例: `19911287` |
| data.n | integer (int64) |  | tradeNum<br>成交笔数<br>例: `217505` |

```json
{
  "stream": "alpha_116usdt@ticker",
  "data": {
    "e": "24hrTicker",
    "E": 1773109631569,
    "s": "ALPHA_116USDT",
    "p": "0.00000000",
    "P": "0.00",
    "w": "8.40003127",
    "c": "8.40000000",
    "Q": "0.49293200",
    "o": "8.40000000",
    "h": "8.50000000",
    "l": "8.30000000",
    "v": "64750.63418500",
    "q": "543907.35169250",
    "O": 1773023220000,
    "C": 1773109631555,
    "F": 19847634,
    "L": 19911287,
    "n": 217505
  }
}
```

## Trade Stream（逐笔成交流）

流名称: `{symbol}@trade`

Pushes raw trade updates for a symbol.

推送指定交易对的逐笔成交更新。

Operation ID: `tradeStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | Symbol to subscribe, in lowercase stream format.<br>要订阅的交易对（流中使用小写格式）。<br>例: `alpha_116usdt` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| method | string | 是 | WebSocket Streams method name.<br>WebSocket 数据流方法名称。<br>枚举: `SUBSCRIBE`<br>例: `SUBSCRIBE` |
| params | string[] | 是 | List of streams to subscribe to.<br>要订阅的数据流列表。 |
| id | integer (int32) | 是 | Unique WebSocket request ID.<br>唯一的 WebSocket 请求 ID。<br>例: `532601580` |

```json
{
  "method": "SUBSCRIBE",
  "params": [
    "alpha_116usdt@trade"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Trade Stream / 逐笔成交流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | eventType<br>事件类型<br>例: `trade` |
| E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773110023891` |
| T | integer (int64) |  | tradeTime<br>成交时间<br>例: `1773110023877` |
| s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| t | integer (int64) |  | tradeId<br>成交 ID<br>例: `19911650` |
| p | string |  | fillPrice<br>成交价<br>例: `8.40000000` |
| q | string |  | fillQty<br>成交量<br>例: `0.97915700` |
| m | boolean |  | isBuyerMaker<br>是否为买方挂单成交<br>例: `False` |

```json
{
  "e": "trade",
  "E": 1773110023891,
  "T": 1773110023877,
  "s": "ALPHA_116USDT",
  "t": 19911650,
  "p": "8.40000000",
  "q": "0.97915700",
  "m": false
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `alpha_116usdt@trade` |
| data | object | 是 |  |
| data.e | string |  | eventType<br>事件类型<br>例: `trade` |
| data.E | integer (int64) |  | eventTime<br>事件时间<br>例: `1773110023891` |
| data.T | integer (int64) |  | tradeTime<br>成交时间<br>例: `1773110023877` |
| data.s | string |  | symbol<br>交易对<br>例: `ALPHA_116USDT` |
| data.t | integer (int64) |  | tradeId<br>成交 ID<br>例: `19911650` |
| data.p | string |  | fillPrice<br>成交价<br>例: `8.40000000` |
| data.q | string |  | fillQty<br>成交量<br>例: `0.97915700` |
| data.m | boolean |  | isBuyerMaker<br>是否为买方挂单成交<br>例: `False` |

```json
{
  "stream": "alpha_116usdt@trade",
  "data": {
    "e": "trade",
    "E": 1773110023891,
    "T": 1773110023877,
    "s": "ALPHA_116USDT",
    "t": 19911650,
    "p": "8.40000000",
    "q": "0.97915700",
    "m": false
  }
}
```