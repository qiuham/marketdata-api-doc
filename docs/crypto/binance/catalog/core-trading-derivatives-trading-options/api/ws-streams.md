---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams
api_type: WebSocket Streams
updated_at: 2026-11-19 18:51:39.816937
---

# Options WebSocket Market Streams

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/1.0.0/schema.yaml

Access market data, manage accounts, and trade Binance Options.

访问市场数据、管理账户，并交易 Binance 期权。

版本: 1.0.0

## 服务地址

- `wss://fstream.binance.com`
- `wss://fstream.binancefuture.com`

## 接口列表

- `!index@arr` — Index Price Streams
- `{symbol}@kline_{interval}` — Kline/Candlestick Streams
- `{underlying}@optionMarkPrice` — Option Mark Price
- `!optionSymbol` — New Symbol Info
- `{underlying}@openInterest@{expirationDate}` — Open Interest
- `{symbol}@depth@{updateSpeed}` — Diff Book Depth Streams
- `{symbol}@bookTicker` — Individual Symbol Book Ticker Streams
- `{symbol}@depth{level}@{updateSpeed}` — Partial Book Depth Streams
- `{symbol}@optionTicker{expirationDate}` — 24-hour TICKER
- `{symbol}@optionTrade` — Trade Streams

## Index Price Streams（指数价格）

流名称: `!index@arr`

Underlying(e.g ETHUSDT) index stream.

指数价格

更新速度: 1000ms

Operation ID: `indexPriceStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |

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
    "!index@arr"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Index Price Streams / 指数价格流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | event type<br>事件类型<br>例: `indexPrice` |
| [].E | integer (int64) |  | time<br>时间<br>例: `1763092572229` |
| [].s | string |  | underlying symbol<br>标的交易对<br>例: `ETHUSDT` |
| [].p | string |  | index price<br>指数价格<br>例: `3224.51976744` |

```json
[
  {
    "e": "indexPrice",
    "E": 1763092572229,
    "s": "ETHUSDT",
    "p": "3224.51976744"
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!index@arr` |
| data | object[] | 是 |  |
| data[].e | string |  | event type<br>事件类型<br>例: `indexPrice` |
| data[].E | integer (int64) |  | time<br>时间<br>例: `1763092572229` |
| data[].s | string |  | underlying symbol<br>标的交易对<br>例: `ETHUSDT` |
| data[].p | string |  | index price<br>指数价格<br>例: `3224.51976744` |

```json
{
  "stream": "!index@arr",
  "data": [
    {
      "e": "indexPrice",
      "E": 1763092572229,
      "s": "ETHUSDT",
      "p": "3224.51976744"
    }
  ]
}
```

## Kline/Candlestick Streams（K线）

流名称: `{symbol}@kline_{interval}`

The Kline/Candlestick Stream push updates to the current klines/candlestick every 1000 milliseconds (if existing).

K线流每1000毫秒推送当前K线更新（如果存在）。

更新速度: 1000ms

Operation ID: `klineCandlestickStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| interval | path | string | 是 | The interval parameter<br>间隔参数<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`, `3d`, `1w`<br>例: `1m` |

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
    "btcusdt@kline_1m"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Kline/Candlestick Streams / K 线流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `kline` |
| E | integer (int64) |  | event time<br>事件时间<br>例: `1638747660000` |
| s | string |  | Option trading symbol<br>交易对<br>例: `BTC-200630-9000-P` |
| k | object |  | k<br>K 线数据 |
| k.t | integer (int64) |  | kline start time<br>这根K线的起始时间<br>例: `1638747660000` |
| k.T | integer (int64) |  | kline end time<br>这根K线的结束时间<br>例: `1638747719999` |
| k.s | string |  | Option trading symbol<br>交易对<br>例: `BTC-200630-9000-P` |
| k.i | string |  | candle period<br>K线间隔<br>例: `1m` |
| k.f | integer (int64) |  | first trade ID<br>这根K线期间第一笔成交ID<br>例: `0` |
| k.L | integer (int64) |  | last trade ID<br>这根K线期间末一笔成交ID<br>例: `0` |
| k.o | string |  | open<br>这根K线期间第一笔成交价<br>例: `1000` |
| k.c | string |  | close<br>这根K线期间末一笔成交价<br>例: `1000` |
| k.h | string |  | high<br>这根K线期间最高成交价<br>例: `1000` |
| k.l | string |  | low<br>这根K线期间最低成交价<br>例: `1000` |
| k.v | string |  | volume(in contracts)<br>这根K线期间成交量<br>例: `0` |
| k.n | integer (int64) |  | number of trades<br>这根K线期间成交笔数<br>例: `0` |
| k.x | boolean |  | current candle has been completed Y/N<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| k.q | string |  | completed trade amount   (in quote asset)<br>这根K线期间成交额<br>例: `0` |
| k.V | string |  | taker completed trade volume (in contracts)<br>主动买入的成交额<br>例: `0` |
| k.Q | string |  | taker trade amount(in quote asset)<br>主动买入的成交量<br>例: `0` |

```json
{
  "e": "kline",
  "E": 1638747660000,
  "s": "BTC-200630-9000-P",
  "k": {
    "t": 1638747660000,
    "T": 1638747719999,
    "s": "BTC-200630-9000-P",
    "i": "1m",
    "f": 0,
    "L": 0,
    "o": "1000",
    "c": "1000",
    "h": "1000",
    "l": "1000",
    "v": "0",
    "n": 0,
    "x": false,
    "q": "0",
    "V": "0",
    "Q": "0"
  }
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@kline_1m` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `kline` |
| data.E | integer (int64) |  | event time<br>事件时间<br>例: `1638747660000` |
| data.s | string |  | Option trading symbol<br>交易对<br>例: `BTC-200630-9000-P` |
| data.k | object |  | k<br>K 线数据 |
| data.k.t | integer (int64) |  | kline start time<br>这根K线的起始时间<br>例: `1638747660000` |
| data.k.T | integer (int64) |  | kline end time<br>这根K线的结束时间<br>例: `1638747719999` |
| data.k.s | string |  | Option trading symbol<br>交易对<br>例: `BTC-200630-9000-P` |
| data.k.i | string |  | candle period<br>K线间隔<br>例: `1m` |
| data.k.f | integer (int64) |  | first trade ID<br>这根K线期间第一笔成交ID<br>例: `0` |
| data.k.L | integer (int64) |  | last trade ID<br>这根K线期间末一笔成交ID<br>例: `0` |
| data.k.o | string |  | open<br>这根K线期间第一笔成交价<br>例: `1000` |
| data.k.c | string |  | close<br>这根K线期间末一笔成交价<br>例: `1000` |
| data.k.h | string |  | high<br>这根K线期间最高成交价<br>例: `1000` |
| data.k.l | string |  | low<br>这根K线期间最低成交价<br>例: `1000` |
| data.k.v | string |  | volume(in contracts)<br>这根K线期间成交量<br>例: `0` |
| data.k.n | integer (int64) |  | number of trades<br>这根K线期间成交笔数<br>例: `0` |
| data.k.x | boolean |  | current candle has been completed Y/N<br>这根K线是否完结(是否已经开始下一根K线)<br>例: `False` |
| data.k.q | string |  | completed trade amount   (in quote asset)<br>这根K线期间成交额<br>例: `0` |
| data.k.V | string |  | taker completed trade volume (in contracts)<br>主动买入的成交额<br>例: `0` |
| data.k.Q | string |  | taker trade amount(in quote asset)<br>主动买入的成交量<br>例: `0` |

```json
{
  "stream": "btcusdt@kline_1m",
  "data": {
    "e": "kline",
    "E": 1638747660000,
    "s": "BTC-200630-9000-P",
    "k": {
      "t": 1638747660000,
      "T": 1638747719999,
      "s": "BTC-200630-9000-P",
      "i": "1m",
      "f": 0,
      "L": 0,
      "o": "1000",
      "c": "1000",
      "h": "1000",
      "l": "1000",
      "v": "0",
      "n": 0,
      "x": false,
      "q": "0",
      "V": "0",
      "Q": "0"
    }
  }
}
```

## Option Mark Price（标记价格）

流名称: `{underlying}@optionMarkPrice`

The mark price for all option symbols on specific underlying asset. E.g.[btcusdt@optionMarkPrice](wss://fstream.binance.com/market/stream?streams=btcusdt@optionMarkPrice)

特定标的资产的所有期权交易对的标记价格。例如：[btcusdt@optionMarkPrice](wss://fstream.binance.com/market/stream?streams=btcusdt@optionMarkPrice)

更新速度: 1000ms

Operation ID: `optionMarkPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| underlying | path | string | 是 | The underlying parameter<br>标的资产参数<br>例: `btcusdt` |

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
    "btcusdt@optionMarkPrice"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Mark Price / 标记价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].s | string |  | Symbol<br>交易对<br>例: `BTC-251120-126000-C` |
| [].mp | string |  | Mark price<br>标记价格<br>例: `770.543` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1762867543321` |
| [].e | string |  | Event type<br>事件类型<br>例: `markPrice` |
| [].i | string |  | Index price<br>指数价格<br>例: `104334.60217391` |
| [].P | string |  | Estimated Settle Price, only useful in the 0.5 hour before the settlement starts<br>预估结算价，结算前半小时有效<br>例: `0.000` |
| [].bo | string |  | The best buy price<br>买一价格<br>例: `0.000` |
| [].ao | string |  | The best sell price<br>卖一价格<br>例: `900.000` |
| [].bq | string |  | The best buy quantity<br>买一数量<br>例: `0.0000` |
| [].aq | string |  | The best sell quantity<br>卖一数量<br>例: `0.2000` |
| [].b | string |  | BuyImplied volatility<br>买一隐含波动率<br>例: `-1.0` |
| [].a | string |  | SellImplied volatility<br>卖一隐含波动率<br>例: `0.98161161` |
| [].hl | string |  | Buy Maximum price<br>最高买价<br>例: `924.652` |
| [].ll | string |  | Sell Minimum price<br>最低卖价<br>例: `616.435` |
| [].vo | string |  | volatility<br>隐含波动率<br>例: `0.9408058` |
| [].rf | string |  | risk free rate<br>无风险利率<br>例: `0.0` |
| [].d | string |  | delta<br>德尔塔<br>例: `0.11111964` |
| [].t | string |  | theta<br>西塔<br>例: `-164.26702615` |
| [].g | string |  | gamma<br>伽马<br>例: `0.00001245` |
| [].v | string |  | vega<br>维加<br>例: `30.63855919` |

```json
[
  {
    "s": "BTC-251120-126000-C",
    "mp": "770.543",
    "E": 1762867543321,
    "e": "markPrice",
    "i": "104334.60217391",
    "P": "0.000",
    "bo": "0.000",
    "ao": "900.000",
    "bq": "0.0000",
    "aq": "0.2000",
    "b": "-1.0",
    "a": "0.98161161",
    "hl": "924.652",
    "ll": "616.435",
    "vo": "0.9408058",
    "rf": "0.0",
    "d": "0.11111964",
    "t": "-164.26702615",
    "g": "0.00001245",
    "v": "30.63855919"
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@optionMarkPrice` |
| data | object[] | 是 |  |
| data[].s | string |  | Symbol<br>交易对<br>例: `BTC-251120-126000-C` |
| data[].mp | string |  | Mark price<br>标记价格<br>例: `770.543` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1762867543321` |
| data[].e | string |  | Event type<br>事件类型<br>例: `markPrice` |
| data[].i | string |  | Index price<br>指数价格<br>例: `104334.60217391` |
| data[].P | string |  | Estimated Settle Price, only useful in the 0.5 hour before the settlement starts<br>预估结算价，结算前半小时有效<br>例: `0.000` |
| data[].bo | string |  | The best buy price<br>买一价格<br>例: `0.000` |
| data[].ao | string |  | The best sell price<br>卖一价格<br>例: `900.000` |
| data[].bq | string |  | The best buy quantity<br>买一数量<br>例: `0.0000` |
| data[].aq | string |  | The best sell quantity<br>卖一数量<br>例: `0.2000` |
| data[].b | string |  | BuyImplied volatility<br>买一隐含波动率<br>例: `-1.0` |
| data[].a | string |  | SellImplied volatility<br>卖一隐含波动率<br>例: `0.98161161` |
| data[].hl | string |  | Buy Maximum price<br>最高买价<br>例: `924.652` |
| data[].ll | string |  | Sell Minimum price<br>最低卖价<br>例: `616.435` |
| data[].vo | string |  | volatility<br>隐含波动率<br>例: `0.9408058` |
| data[].rf | string |  | risk free rate<br>无风险利率<br>例: `0.0` |
| data[].d | string |  | delta<br>德尔塔<br>例: `0.11111964` |
| data[].t | string |  | theta<br>西塔<br>例: `-164.26702615` |
| data[].g | string |  | gamma<br>伽马<br>例: `0.00001245` |
| data[].v | string |  | vega<br>维加<br>例: `30.63855919` |

```json
{
  "stream": "btcusdt@optionMarkPrice",
  "data": [
    {
      "s": "BTC-251120-126000-C",
      "mp": "770.543",
      "E": 1762867543321,
      "e": "markPrice",
      "i": "104334.60217391",
      "P": "0.000",
      "bo": "0.000",
      "ao": "900.000",
      "bq": "0.0000",
      "aq": "0.2000",
      "b": "-1.0",
      "a": "0.98161161",
      "hl": "924.652",
      "ll": "616.435",
      "vo": "0.9408058",
      "rf": "0.0",
      "d": "0.11111964",
      "t": "-164.26702615",
      "g": "0.00001245",
      "v": "30.63855919"
    }
  ]
}
```

## New Symbol Info（新增交易对信息推送）

流名称: `!optionSymbol`

New symbol listing stream.

新增交易对信息推送

更新速度: 50ms

Operation ID: `newSymbolInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |

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
    "!optionSymbol"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：New Symbol Info / 新增交易对信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event Type<br>事件类型<br>例: `optionSymbol` |
| E | integer (int64) |  | Event Time<br>事件时间<br>例: `1669356423908` |
| s | string |  | Symbol<br>交易对<br>例: `BTC-250926-140000-C` |
| ps | string |  | Underlying index of the contract<br>标的资产<br>例: `BTCUSDT` |
| qa | string |  | Quotation asset<br>计价资产<br>例: `USDT` |
| d | string |  | Option type<br>期权类型<br>例: `CALL` |
| sp | string |  | Strike price<br>行权价格<br>例: `21000` |
| dt | integer (int64) |  | Delivery date time<br>行权时间<br>例: `4133404800000` |
| u | integer (int64) |  | unit, the quantity of the underlying asset represented by a single contract.<br>一张合约代表的标的数量<br>例: `1` |
| ot | integer (int64) |  | onboard date time<br>上币时间<br>例: `1569398400000` |
| cs | string |  | Contract status<br>合约状态<br>例: `TRADING` |

```json
{
  "e": "optionSymbol",
  "E": 1669356423908,
  "s": "BTC-250926-140000-C",
  "ps": "BTCUSDT",
  "qa": "USDT",
  "d": "CALL",
  "sp": "21000",
  "dt": 4133404800000,
  "u": 1,
  "ot": 1569398400000,
  "cs": "TRADING"
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `!optionSymbol` |
| data | object | 是 |  |
| data.e | string |  | Event Type<br>事件类型<br>例: `optionSymbol` |
| data.E | integer (int64) |  | Event Time<br>事件时间<br>例: `1669356423908` |
| data.s | string |  | Symbol<br>交易对<br>例: `BTC-250926-140000-C` |
| data.ps | string |  | Underlying index of the contract<br>标的资产<br>例: `BTCUSDT` |
| data.qa | string |  | Quotation asset<br>计价资产<br>例: `USDT` |
| data.d | string |  | Option type<br>期权类型<br>例: `CALL` |
| data.sp | string |  | Strike price<br>行权价格<br>例: `21000` |
| data.dt | integer (int64) |  | Delivery date time<br>行权时间<br>例: `4133404800000` |
| data.u | integer (int64) |  | unit, the quantity of the underlying asset represented by a single contract.<br>一张合约代表的标的数量<br>例: `1` |
| data.ot | integer (int64) |  | onboard date time<br>上币时间<br>例: `1569398400000` |
| data.cs | string |  | Contract status<br>合约状态<br>例: `TRADING` |

```json
{
  "stream": "!optionSymbol",
  "data": {
    "e": "optionSymbol",
    "E": 1669356423908,
    "s": "BTC-250926-140000-C",
    "ps": "BTCUSDT",
    "qa": "USDT",
    "d": "CALL",
    "sp": "21000",
    "dt": 4133404800000,
    "u": 1,
    "ot": 1569398400000,
    "cs": "TRADING"
  }
}
```

## Open Interest（合约持仓量）

流名称: `{underlying}@openInterest@{expirationDate}`

Option open interest for specific underlying asset on specific expiration date. E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

特定标的资产特定到期日的期权合约持仓量。如[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

更新速度: 60s

Operation ID: `openInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| underlying | path | string | 是 | The underlying parameter<br>标的资产参数<br>例: `btcusdt` |
| expirationDate | path | string | 是 | The expirationDate parameter<br>到期日参数。<br>例: `220930` |

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
    "btcusdt@openInterest@220930"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Open Interest / 合约持仓量

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].e | string |  | Event type<br>事件类型<br>例: `openInterest` |
| [].E | integer (int64) |  | Event time<br>事件时间<br>例: `1668759300045` |
| [].s | string |  | Option symbol<br>交易对<br>例: `ETH-221125-2700-C` |
| [].o | string |  | Open interest in contracts<br>持仓量（以张数计）<br>例: `1580.87` |
| [].h | string |  | Open interest in USDT<br>持仓量（以USDT计）<br>例: `1912992.178168204` |

```json
[
  {
    "e": "openInterest",
    "E": 1668759300045,
    "s": "ETH-221125-2700-C",
    "o": "1580.87",
    "h": "1912992.178168204"
  }
]
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@openInterest@220930` |
| data | object[] | 是 |  |
| data[].e | string |  | Event type<br>事件类型<br>例: `openInterest` |
| data[].E | integer (int64) |  | Event time<br>事件时间<br>例: `1668759300045` |
| data[].s | string |  | Option symbol<br>交易对<br>例: `ETH-221125-2700-C` |
| data[].o | string |  | Open interest in contracts<br>持仓量（以张数计）<br>例: `1580.87` |
| data[].h | string |  | Open interest in USDT<br>持仓量（以USDT计）<br>例: `1912992.178168204` |

```json
{
  "stream": "btcusdt@openInterest@220930",
  "data": [
    {
      "e": "openInterest",
      "E": 1668759300045,
      "s": "ETH-221125-2700-C",
      "o": "1580.87",
      "h": "1912992.178168204"
    }
  ]
}
```

## Diff Book Depth Streams（增量深度信息）

流名称: `{symbol}@depth@{updateSpeed}`

Bids and asks, pushed every 500 milliseconds, 100 milliseconds (if existing)

买卖盘，每 500 毫秒推送一次，100 毫秒（如果存在）

更新速度: 100ms or 500ms

Operation ID: `diffBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| updateSpeed | path | string | 是 | WebSocket stream update speed<br>WebSocket 流更新速度。<br>枚举: `100ms`, `500ms`<br>例: `100ms` |

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
    "btcusdt@depth@100ms"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Diff Book Depth Streams / 增量深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | event time<br>事件时间<br>例: `1762866729459` |
| T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1762866729358` |
| s | string |  | Option symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `465` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `465` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `464` |
| b | oneOf[][] |  | Buy order<br>买方 |
| a | oneOf[][] |  | Sell order<br>卖方 |

```json
{
  "e": "depthUpdate",
  "E": 1762866729459,
  "T": 1762866729358,
  "s": "BTC-251123-126000-C",
  "U": 465,
  "u": 465,
  "pu": 464,
  "b": [
    [
      "1100.000",
      "0.6000"
    ]
  ],
  "a": [
    [
      "1300.000",
      "0.6000"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth@100ms` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | event time<br>事件时间<br>例: `1762866729459` |
| data.T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1762866729358` |
| data.s | string |  | Option symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `465` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `465` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `464` |
| data.b | oneOf[][] |  | Buy order<br>买方 |
| data.a | oneOf[][] |  | Sell order<br>卖方 |

```json
{
  "stream": "btcusdt@depth@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1762866729459,
    "T": 1762866729358,
    "s": "BTC-251123-126000-C",
    "U": 465,
    "u": 465,
    "pu": 464,
    "b": [
      [
        "1100.000",
        "0.6000"
      ]
    ],
    "a": [
      [
        "1300.000",
        "0.6000"
      ]
    ]
  }
}
```

## Individual Symbol Book Ticker Streams（按Symbol的最优挂单信息）

流名称: `{symbol}@bookTicker`

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

实时推送指定交易对的最优挂单价格或数量的任何更新。

更新速度: Real-Time

Operation ID: `individualSymbolBookTickerStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
    "btcusdt@bookTicker"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Individual Symbol Book Ticker Streams / 单个交易对最优挂单流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| u | integer (int64) |  | order book updateId<br>更新ID<br>例: `2472` |
| s | string |  | symbol<br>交易对<br>例: `BTC-251226-110000-C` |
| b | string |  | best bid price<br>买单最优挂单价格<br>例: `5000.000` |
| B | string |  | bid bid quantity<br>买单最优挂单数量<br>例: `0.2000` |
| a | string |  | best ask price<br>卖单最优挂单价格<br>例: `5100.000` |
| A | string |  | best ask quantity<br>卖单最优挂单数量<br>例: `0.1000` |
| T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1763041762942` |
| E | integer (int64) |  | event time<br>事件推送时间<br>例: `1763041762942` |

```json
{
  "e": "bookTicker",
  "u": 2472,
  "s": "BTC-251226-110000-C",
  "b": "5000.000",
  "B": "0.2000",
  "a": "5100.000",
  "A": "0.1000",
  "T": 1763041762942,
  "E": 1763041762942
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@bookTicker` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `bookTicker` |
| data.u | integer (int64) |  | order book updateId<br>更新ID<br>例: `2472` |
| data.s | string |  | symbol<br>交易对<br>例: `BTC-251226-110000-C` |
| data.b | string |  | best bid price<br>买单最优挂单价格<br>例: `5000.000` |
| data.B | string |  | bid bid quantity<br>买单最优挂单数量<br>例: `0.2000` |
| data.a | string |  | best ask price<br>卖单最优挂单价格<br>例: `5100.000` |
| data.A | string |  | best ask quantity<br>卖单最优挂单数量<br>例: `0.1000` |
| data.T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1763041762942` |
| data.E | integer (int64) |  | event time<br>事件推送时间<br>例: `1763041762942` |

```json
{
  "stream": "btcusdt@bookTicker",
  "data": {
    "e": "bookTicker",
    "u": 2472,
    "s": "BTC-251226-110000-C",
    "b": "5000.000",
    "B": "0.2000",
    "a": "5100.000",
    "A": "0.1000",
    "T": 1763041762942,
    "E": 1763041762942
  }
}
```

## Partial Book Depth Streams（有限档深度信息）

流名称: `{symbol}@depth{level}@{updateSpeed}`

Top <levels> bids and asks. Valid <levels> are 5, 10, 20.

前 <levels> 档买卖盘。有效档位为 5、10、20。

更新速度: 100ms or 500ms

Operation ID: `partialBookDepthStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| level | path | string | 是 | The level parameter<br>level 参数<br>枚举: `5`, `10`, `20`<br>例: `5` |
| updateSpeed | path | string | 是 | WebSocket stream update speed<br>WebSocket 流更新速度。<br>枚举: `100ms`, `500ms`<br>例: `100ms` |

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
    "btcusdt@depth5@100ms"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Partial Book Depth Streams / 有限档深度流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `depthUpdate` |
| E | integer (int64) |  | event time<br>事件时间<br>例: `1762866729459` |
| T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1762866729358` |
| s | string |  | Option symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `465` |
| u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `465` |
| pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `464` |
| b | string[][] |  | Buy order<br>买方 |
| a | string[][] |  | Sell order<br>卖方 |

```json
{
  "e": "depthUpdate",
  "E": 1762866729459,
  "T": 1762866729358,
  "s": "BTC-251123-126000-C",
  "U": 465,
  "u": 465,
  "pu": 464,
  "b": [
    [
      "1100.000"
    ]
  ],
  "a": [
    [
      "1300.000"
    ]
  ]
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@depth5@100ms` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `depthUpdate` |
| data.E | integer (int64) |  | event time<br>事件时间<br>例: `1762866729459` |
| data.T | integer (int64) |  | transaction time<br>撮合时间<br>例: `1762866729358` |
| data.s | string |  | Option symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| data.U | integer (int64) |  | First update ID in event<br>从上次推送至今新增的第一个 update Id<br>例: `465` |
| data.u | integer (int64) |  | Final update ID in event<br>从上次推送至今新增的最后一个 update Id<br>例: `465` |
| data.pu | integer (int64) |  | Final update Id in last stream(ie `u` in last stream)<br>上次推送的最后一个update Id(即上条消息的‘u’)<br>例: `464` |
| data.b | string[][] |  | Buy order<br>买方 |
| data.a | string[][] |  | Sell order<br>卖方 |

```json
{
  "stream": "btcusdt@depth5@100ms",
  "data": {
    "e": "depthUpdate",
    "E": 1762866729459,
    "T": 1762866729358,
    "s": "BTC-251123-126000-C",
    "U": 465,
    "u": 465,
    "pu": 464,
    "b": [
      [
        "1100.000"
      ]
    ],
    "a": [
      [
        "1300.000"
      ]
    ]
  }
}
```

## 24-hour TICKER（按交易对的Ticker）

流名称: `{symbol}@optionTicker{expirationDate}`

24hr ticker info for all symbols. Only symbols whose ticker info changed will be sent.

所有交易对的24小时Ticker信息。只有Ticker信息发生变化的交易对才会被发送。

更新速度: 1000ms

Operation ID: `hour24Ticker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |
| expirationDate | path | string |  | The expiration date parameter<br>到期日参数<br>例: `251230` |

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
    "btcusdt@optionTicker251230"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：24-hour TICKER / 24小时Ticker

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| E | integer (int64) |  | Event time<br>事件时间<br>例: `1764080707933` |
| s | string |  | Symbol<br>交易对<br>例: `ETH-251226-3000-C` |
| p | string |  | Price change<br>价格变化<br>例: `0.0000` |
| P | string |  | Price change percent<br>价格变化百分比<br>例: `0.00` |
| w | string |  | Weighted average price<br>平均价格<br>例: `200.0000` |
| c | string |  | Last price<br>最新价<br>例: `200.0000` |
| Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `1.0000` |
| o | string |  | Open price<br>开盘价<br>例: `200.0000` |
| h | string |  | High price<br>最高价<br>例: `200.0000` |
| l | string |  | Low price<br>最低价<br>例: `200.0000` |
| v | string |  | Trading volume(in contracts)<br>成交量张数<br>例: `9.0000` |
| q | string |  | trade amount(in quote asset)<br>成交金额<br>例: `1800.0000` |
| O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1764051060000` |
| C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1764080707933` |
| F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `1` |
| L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `22` |
| n | integer (int64) |  | Total number of trade<br>24小时内成交数<br>例: `9` |

```json
{
  "e": "24hrTicker",
  "E": 1764080707933,
  "s": "ETH-251226-3000-C",
  "p": "0.0000",
  "P": "0.00",
  "w": "200.0000",
  "c": "200.0000",
  "Q": "1.0000",
  "o": "200.0000",
  "h": "200.0000",
  "l": "200.0000",
  "v": "9.0000",
  "q": "1800.0000",
  "O": 1764051060000,
  "C": 1764080707933,
  "F": 1,
  "L": 22,
  "n": 9
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@optionTicker251230` |
| data | object | 是 |  |
| data.e | string |  | Event type<br>事件类型<br>例: `24hrTicker` |
| data.E | integer (int64) |  | Event time<br>事件时间<br>例: `1764080707933` |
| data.s | string |  | Symbol<br>交易对<br>例: `ETH-251226-3000-C` |
| data.p | string |  | Price change<br>价格变化<br>例: `0.0000` |
| data.P | string |  | Price change percent<br>价格变化百分比<br>例: `0.00` |
| data.w | string |  | Weighted average price<br>平均价格<br>例: `200.0000` |
| data.c | string |  | Last price<br>最新价<br>例: `200.0000` |
| data.Q | string |  | Last quantity<br>最新成交价格上的成交量<br>例: `1.0000` |
| data.o | string |  | Open price<br>开盘价<br>例: `200.0000` |
| data.h | string |  | High price<br>最高价<br>例: `200.0000` |
| data.l | string |  | Low price<br>最低价<br>例: `200.0000` |
| data.v | string |  | Trading volume(in contracts)<br>成交量张数<br>例: `9.0000` |
| data.q | string |  | trade amount(in quote asset)<br>成交金额<br>例: `1800.0000` |
| data.O | integer (int64) |  | Statistics open time<br>统计开始时间<br>例: `1764051060000` |
| data.C | integer (int64) |  | Statistics close time<br>统计结束时间<br>例: `1764080707933` |
| data.F | integer (int64) |  | First trade ID<br>24小时内第一笔成交交易ID<br>例: `1` |
| data.L | integer (int64) |  | Last trade Id<br>24小时内最后一笔成交交易ID<br>例: `22` |
| data.n | integer (int64) |  | Total number of trade<br>24小时内成交数<br>例: `9` |

```json
{
  "stream": "btcusdt@optionTicker251230",
  "data": {
    "e": "24hrTicker",
    "E": 1764080707933,
    "s": "ETH-251226-3000-C",
    "p": "0.0000",
    "P": "0.00",
    "w": "200.0000",
    "c": "200.0000",
    "Q": "1.0000",
    "o": "200.0000",
    "h": "200.0000",
    "l": "200.0000",
    "v": "9.0000",
    "q": "1800.0000",
    "O": 1764051060000,
    "C": 1764080707933,
    "F": 1,
    "L": 22,
    "n": 9
  }
}
```

## Trade Streams（最新交易）

流名称: `{symbol}@optionTrade`

The Trade Streams push raw trade information for specific symbol or underlying asset. E.g.[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

交易流推送特定交易对或标的资产的原始交易信息。例如[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

更新速度: 50ms

Operation ID: `tradeStreams`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| id | query | integer (int32) |  | Unique WebSocket request ID.<br>唯一 WebSocket 请求 ID。<br>例: `532601580` |
| symbol | path | string | 是 | The symbol parameter<br>交易对参数<br>例: `btcusdt` |

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
    "btcusdt@optionTrade"
  ],
  "id": 532601580
}
```

### 响应 Raw Stream：Trade Streams / 成交流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| e | string |  | event type<br>事件类型<br>例: `trade` |
| E | integer (int64) |  | event time<br>事件时间<br>例: `1762856064204` |
| T | integer (int64) |  | trade completed time<br>成交完成时间<br>例: `1762856064203` |
| s | string |  | Option trading symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| t | integer (int64) |  | trade ID<br>交易ID<br>例: `4` |
| p | string |  | price<br>交易价格<br>例: `1300.000` |
| q | string |  | quantity, always positive<br>交易数量<br>例: `0.1000` |
| X | string |  | trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade<br>交易类型，"MARKET" 代表订单薄交易, "BLOCK"代表大宗交易<br>例: `MARKET` |
| S | string |  | direction<br>方向<br>例: `BUY` |
| m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `False` |

```json
{
  "e": "trade",
  "E": 1762856064204,
  "T": 1762856064203,
  "s": "BTC-251123-126000-C",
  "t": 4,
  "p": "1300.000",
  "q": "0.1000",
  "X": "MARKET",
  "S": "BUY",
  "m": false
}
```

### 响应 Combined Stream：Stream payload with stream name.

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stream | string | 是 | 例: `btcusdt@optionTrade` |
| data | object | 是 |  |
| data.e | string |  | event type<br>事件类型<br>例: `trade` |
| data.E | integer (int64) |  | event time<br>事件时间<br>例: `1762856064204` |
| data.T | integer (int64) |  | trade completed time<br>成交完成时间<br>例: `1762856064203` |
| data.s | string |  | Option trading symbol<br>交易对<br>例: `BTC-251123-126000-C` |
| data.t | integer (int64) |  | trade ID<br>交易ID<br>例: `4` |
| data.p | string |  | price<br>交易价格<br>例: `1300.000` |
| data.q | string |  | quantity, always positive<br>交易数量<br>例: `0.1000` |
| data.X | string |  | trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade<br>交易类型，"MARKET" 代表订单薄交易, "BLOCK"代表大宗交易<br>例: `MARKET` |
| data.S | string |  | direction<br>方向<br>例: `BUY` |
| data.m | boolean |  | Is the buyer the market maker?<br>买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。<br>例: `False` |

```json
{
  "stream": "btcusdt@optionTrade",
  "data": {
    "e": "trade",
    "E": 1762856064204,
    "T": 1762856064203,
    "s": "BTC-251123-126000-C",
    "t": 4,
    "p": "1300.000",
    "q": "0.1000",
    "X": "MARKET",
    "S": "BUY",
    "m": false
  }
}
```