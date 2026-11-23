---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/market
api_type: REST
updated_at: 2026-11-23 19:02:44.888685
---

# Market

Public market data, derivatives & funding rate, trading statistics, trading & risk rules, and public configuration APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/market/instruments` — Get Instruments
- `GET /api/v3/market/rpi-symbols` — Get RPI Symbols
- `GET /api/v3/market/tickers` — Get Tickers
- `GET /api/v3/market/orderbook` — Get Order Book
- `GET /api/v3/market/rpi-orderbook` — Get RPI Order Book
- `GET /api/v3/market/fills` — Get Recent Public Fills
- `GET /api/v3/market/candles` — Get Kline/Candlestick
- `GET /api/v3/market/history-candles` — Get Kline/Candlestick History
- `GET /api/v3/market/time` — Get Server Time
- `GET /api/v3/market/coins` — Get Coins
- `GET /api/v3/public/annoucements` — Get Announcements
- `GET /api/v3/market/open-interest` — Get Open Interest (OI)
- `GET /api/v3/market/open-interest-history` — Get Open Interest History
- `GET /api/v3/market/liquidations` — Get Liquidations History
- `GET /api/v3/market/current-fund-rate` — Get Current Funding Rate
- `GET /api/v3/market/history-fund-rate` — Get Funding Rate History
- `GET /api/v3/market/index-components` — Get Index Price Components
- `GET /api/v3/market/proof-of-reserves` — Get Proof Of Reserves
- `GET /api/v3/market/score-weights` — Get Market Maker Score Weight
- `GET /api/v3/market/fee-group` — Get Institution Fee Group
- `GET /api/v3/market/cash-dividend-records` — Get Cash Dividend Records
- `GET /api/v3/market/split-records` — Get Split Records
- `GET /api/v3/market/risk-reserve` — Get Risk Reserve(Daily)
- `GET /api/v3/market/risk-reserve-hour` — Get Risk Reserve(Hourly)
- `GET /api/v3/market/risk-reserve-all` — Get Risk Reserve All
- `GET /api/v3/market/margin-loans` — Get Margin Loan
- `GET /api/v3/market/margin-loans-all` — Get All Margin Loans
- `GET /api/v3/market/interest-rate-history` — Get Interest Rate History
- `GET /api/v3/market/position-tier` — Get Position Tier
- `GET /api/v3/market/oi-limit` — Get Open Interest Limit
- `GET /api/v3/market/discount-rate` — Get Discount Rate
- `GET /api/v3/market/spot-whale-flow` — Get Spot Whale Net Flow Data
- `GET /api/v3/market/spot-fund-flow` — Get Spot Fund Flow Data
- `GET /api/v3/market/spot-net-flow` — Get Spot 24H Net Capital Inflow Data
- `GET /api/v3/market/margin-long-short` — Get Margin Long Short Ratio Data
- `GET /api/v3/market/margin-loan-growth` — Get Margin Loan Growth Rate Data
- `GET /api/v3/market/margin-isolated-borrow` — Get Isolated Margin Borrowing Ratio Data
- `GET /api/v3/market/futures-active-buy-sell` — Get Futures Active Buy Sell Volume Data
- `GET /api/v3/market/futures-long-short` — Get Futures Long Short Ratio Data
- `GET /api/v3/market/futures-position-long-short` — Get Futures Active Long Short Position Data
- `GET /api/v3/market/futures-account-long-short` — Get Futures Active Long Short Account Data

## Get Instruments

`GET /api/v3/market/instruments`

Rate limit: 20/sec/IP

Query the specifications for online trading pair instruments.

Operation ID: `marketGetInstruments`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name, e.g. BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data[].symbol | string |  | Symbol name |
| data[].isRwa | string |  | Is this an RWA symbol<br><br>`YES` / `NO`<br><br>Only for contract |
| data[].isReality | string |  | Reality identifier<br><br>`yes` Reality stock token<br><br>`no` Non-Reality stock token<br><br>Only for spot |
| data[].baseCoin | string |  | Base coin, e.g. BTC in BTCUSDT |
| data[].quoteCoin | string |  | Quote coin, e.g. USDT in BTCUSDT |
| data[].buyLimitPriceRatio | string |  | Buy price limit ratio<br><br>The ratio of the buy limit price to the market price, determining the maximum price at which a buy order will be placed |
| data[].sellLimitPriceRatio | string |  | Sell price limit ratio<br><br>The ratio of the sell limit price to the market price, determining the minimum price at which a sell order will be placed |
| data[].feeRateUpRatio | string |  | Fee markup ratio<br><br>The percentage by which the actual fee is increased relative to the base fee<br><br>Only for futures |
| data[].makerFeeRate | string |  | Maker fee rate, in decimal form, e.g. 0.0002 represents 0.02%<br><br>Only for futures |
| data[].takerFeeRate | string |  | Taker fee rate, in decimal form, e.g. 0.0002 represents 0.02%<br><br>Only for futures |
| data[].openCostUpRatio | string |  | Opening cost markup ratio<br><br>The percentage by which the cost of opening a trading position is increased relative to the base or standard cost<br><br>Only for futures |
| data[].minOrderQty | string |  | Minimum order quantity, in terms of the base coin<br><br>For spot/margin, please refer to <a href="https://www.bitget.com/zh-CN/trade-info/trade-rule">Trading Rules</a>. |
| data[].maxOrderQty | string |  | Maximum order quantity for a single limit order, in terms of the base coin<br><br>For spot/margin, please refer to <a href="https://www.bitget.com/zh-CN/trade-info/trade-rule">Trading Rules</a>.<br><br>A value of 0 indicates no limit. |
| data[].pricePrecision | string |  | Price precision, the number of decimal places allowed for the price |
| data[].quantityPrecision | string |  | Quantity precision, the number of decimal places allowed for the quantity |
| data[].quotePrecision | string |  | Market order precision, the number of decimal places allowed for the price of the quote coin |
| data[].priceMultiplier | string |  | Price multiplier, used for futures orders together with pricePrecision. e.g. pricePrecision 2 & priceMultiplier 0.02: the order price must be a multiple of priceMultiplier and have two decimal places<br><br>Only for futures |
| data[].quantityMultiplier | string |  | Quantity multiplier, used for futures orders together with quantityPrecision<br><br>Only for futures |
| data[].type | string |  | Futures type<br><br>`perpetual` Perpetual<br><br>`delivery` Delivery<br><br>Only for futures |
| data[].minOrderAmount | string |  | Minimum order amount<br><br>Unit: USDT |
| data[].maxSymbolOrderNum | string |  | Maximum order number in terms of the trading pair(deprecated, no such limit) |
| data[].maxProductOrderNum | string |  | Maximum order number in terms of the product line |
| data[].maxPositionNum | string |  | Maximum position number in terms of the trading pair<br><br>Only for futures/margin |
| data[].status | string |  | Trading pair status<br><br>`listed` Listed (not yet open)<br><br>`online` Normal<br><br>`limit_open` Restrict opening positions<br><br>`limit_close` Restrict closing positions<br><br>`offline` Delisted/under maintenance<br><br>`restrictedAPI` API restricted |
| data[].offTime | string |  | Trading halt time. If not configured, it returns ""<br><br>Only for futures |
| data[].limitOpenTime | string |  | Restricted open time. If not configured, it returns ""; other values indicate symbol is under/expected maintenance and trading is prohibited after a specified time<br><br>Only for futures |
| data[].deliveryTime | string |  | Delivery time<br><br>Only for deliveries |
| data[].deliveryStartTime | string |  | Delivery start time<br><br>Only for deliveries |
| data[].deliveryPeriod | string |  | Delivery period<br><br>`this_quarter` This quarter<br><br>`next_quarter` Next quarter<br><br>Only for deliveries |
| data[].launchTime | string |  | Launch time, Unix millisecond timestamp indicating when the trading pair was launched |
| data[].fundInterval | string |  | Funding interval<br><br>`1` Every 1 hour<br><br>`8` Every 8 hours<br><br>Only for futures |
| data[].minLeverage | string |  | Minimum leverage<br><br>Only for futures |
| data[].maxLeverage | string |  | Maximum leverage<br><br>Only for futures/margin |
| data[].maintainTime | string |  | Maintenance time. If not configured, it returns ""<br><br>Only for futures |
| data[].symbolType | string |  | Symbol type (Deprecated)<br><br>`crypto` cryptocurrency<br><br>`metal` precious metals<br><br>`stock` stocks<br><br>`commodity` commodities |
| data[].fullName | string |  | Full name, including the trading pair name, company name, ETF name, etc., and may carry an ADR/ST/QUANTO identifier<br><br>e.g., for symbol `SKHYUSDT`, `fullName` is "SK Hylix ADR"<br><br>Returned for both spot and futures trading pairs |
| data[].instrumentType | string |  | Instrument type<br><br>`metal`<br><br>`energy`<br><br>`stock`<br><br>`etf`<br><br>`crypto`<br><br>Returned for both spot and futures trading pairs |
| data[].marketRegion | string |  | Market region code<br><br>Applicable to trading pairs related to traditional finance<br><br>`US` United States<br><br>`CN` China<br><br>`HK` Hong Kong<br><br>`KR` South Korea<br><br>`JP` Japan<br><br>Returned for both spot and futures trading pairs |
| data[].isin | string |  | International Securities Identification Number (ISIN), used to uniquely identify financial securities such as stocks, bonds, funds, and warrants<br><br>Format: 2-letter country/region code + 9-character local security identifier + 1 check digit |
| data[].maxMarketOrderQty | string |  | Maximum order quantity for a single market order, in terms of the base coin<br><br>Only for futures |
| data[].isIsolatedBaseBorrowable | string |  | Base coin borrowable status<br><br>Only for margin trading |
| data[].isIsolatedQuotedBorrowable | string |  | Quote coin borrowable status<br><br>Only for margin trading |
| data[].warningRiskRatio | string |  | Warning risk ratio<br><br>Only for margin trading |
| data[].liquidationRiskRatio | string |  | Liquidation risk ratio<br><br>Only for margin trading |
| data[].maxCrossedLeverage | string |  | Maximum leverage for cross margin<br><br>Only for margin trading |
| data[].maxIsolatedLeverage | string |  | Maximum leverage for isolated margin<br><br>Only for margin trading |
| data[].userMinBorrow | string |  | Minimum borrowable amount<br><br>Only for margin trading |
| data[].areaSymbol | string |  | Area symbol `YES`/`NO`<br><br>Only for spot trading; only returned for pairs where the value is YES |
| data[].unrealizedProfitLimit | string |  | Unrealized profit limit<br><br>`yes` Restricted: the trading pair restricts increasing positions and withdrawals while there is unrealized profit<br><br>`no` Not restricted |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770531248742,
  "data": [
    {
      "symbol": "BTCUSDT",
      "category": "SPOT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "isRwa": "NO",
      "isReality": "no",
      "buyLimitPriceRatio": "0.02",
      "sellLimitPriceRatio": "0.02",
      "minOrderQty": "0.000001",
      "maxOrderQty": "0",
      "pricePrecision": "2",
      "quantityPrecision": "6",
      "quotePrecision": "8",
      "minOrderAmount": "1",
      "maxSymbolOrderNum": "",
      "maxProductOrderNum": "400",
      "status": "online",
      "maintainTime": "",
      "maxPositionNum": "200",
      "symbolType": "crypto",
      "fullName": "",
      "instrumentType": "crypto",
      "marketRegion": "",
      "isin": "",
      "launchTime": "1532454360000",
      "unrealizedProfitLimit": "yes"
    }
  ]
}
```

## Get RPI Symbols

`GET /api/v3/market/rpi-symbols`

Rate limit: 10/sec/IP

Query the list of trading pairs that support RPI (Retail Price Improvement).

Operation ID: `marketGetRpiSymbols`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | Business line<br><br>`spot` Spot<br><br>`usdt-futures` USDT futures<br><br>`coin-futures` Coin-M futures<br><br>`usdc-futures` USDC futures |
| data[].symbol | string |  | Symbol that supports RPI |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "category": "spot",
      "symbol": "BTCUSDT"
    },
    {
      "category": "usdt-futures",
      "symbol": "BTCUSDT"
    }
  ]
}
```

## Get Tickers

`GET /api/v3/market/tickers`

Rate limit: 20/sec/IP

Query real-time market data, including the latest price, 24-hour high/low, volume, bid, ask, and price change for available trading pairs.

Operation ID: `marketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name, e.g. BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Symbol name, e.g. BTCUSDT |
| data[].category | string |  | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data[].lastPrice | string |  | Latest price |
| data[].openPrice24h | string |  | Market price 24 hours ago |
| data[].lowPrice24h | string |  | Lowest price in the last 24 hours |
| data[].highPrice24h | string |  | Highest price in the last 24 hours |
| data[].ask1Price | string |  | Best ask price |
| data[].bid1Price | string |  | Best bid price |
| data[].bid1Size | string |  | Best bid quantity |
| data[].ask1Size | string |  | Best ask quantity |
| data[].price24hPcnt | string |  | 24-hour price change percentage |
| data[].turnover24h | string |  | 24-hour turnover |
| data[].volume24h | string |  | 24-hour volume |
| data[].indexPrice | string |  | Index price<br><br>Only for futures |
| data[].markPrice | string |  | Mark price<br><br>Only for futures |
| data[].fundingRate | string |  | Funding rate<br><br>Only for futures |
| data[].openInterest | string |  | Open interest<br><br>Only for futures |
| data[].deliveryStartTime | string |  | Delivery start time<br><br>Only for deliveries |
| data[].deliveryTime | string |  | Delivery time<br><br>Only for deliveries |
| data[].deliveryStatus | string |  | Delivery status<br><br>`delivery_config_period` New pair configuration<br><br>`delivery_normal` Trading<br><br>`delivery_before` 10 minutes before delivery, no new orders<br><br>`delivery_period` During delivery, no opening or closing of positions, and no order cancellation<br><br>Only for deliveries |
| data[].platformTurnover24h | string |  | 24-hour platform turnover<br><br>Only available for rtoken |
| data[].ts | string |  | The timestamp that the system generated the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1765444397411,
  "data": [
    {
      "category": "SPOT",
      "symbol": "BTCUSDT",
      "lastPrice": "90253.5",
      "openPrice24h": "92590.86",
      "highPrice24h": "94475.75",
      "lowPrice24h": "89394.71",
      "ask1Price": "90253.5",
      "bid1Price": "90253.49",
      "bid1Size": "2.368684",
      "ask1Size": "0.402938",
      "price24hPcnt": "-0.02524",
      "volume24h": "7386.014738",
      "turnover24h": "677732572.225658",
      "platformTurnover24h": "677732572.225658",
      "ts": "1765444395778"
    }
  ]
}
```

## Get Order Book

`GET /api/v3/market/orderbook`

Rate limit: 20/sec/IP

Query order book depth data.

You can download historical depth data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `marketGetOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| limit | query | string |  | Depth level. Default: 5. Maximum: 1000<br>默认: `5` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.a | array |  | Sell (ask) depth. Sorted by price in ascending order.<br><br>Each entry: [price, quantity] |
| data.b | array |  | Buy (bid) depth. Sorted by price in descending order.<br><br>Each entry: [price, quantity] |
| data.ts | string |  | The timestamp that the system generated the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969017897,
  "data": {
    "a": [
      [
        73000.0,
        0.007
      ],
      [
        74000.0,
        0.007
      ],
      [
        75000.0,
        0.007
      ],
      [
        75123,
        5.615
      ]
    ],
    "b": [
      [
        71213.8,
        1.836
      ],
      [
        71213.3,
        10
      ],
      [
        71212.8,
        10
      ]
    ],
    "ts": "1730969017964"
  }
}
```

## Get RPI Order Book

`GET /api/v3/market/rpi-orderbook`

Rate limit: 10/sec/IP

Query RPI (Retail Price Improvement) order book depth data. This endpoint returns the full depth including both RPI and non-RPI quantities separately for each price level.

Operation ID: `marketGetRpiOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| limit | query | string |  | Depth level<br><br>`SPOT`: Default 5, Maximum 1000<br><br>`USDT-FUTURES`, `COIN-FUTURES`, `USDC-FUTURES`: Default 5, Maximum 1000<br>默认: `5` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.a | array |  | Sell (ask) depth. Sorted by price in ascending order.<br><br>Each entry: [price, non-RPI quantity, RPI quantity] |
| data.b | array |  | Buy (bid) depth. Sorted by price in descending order.<br><br>Each entry: [price, non-RPI quantity, RPI quantity] |
| data.ts | string |  | The timestamp that the system generated the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969017897,
  "data": {
    "a": [
      [
        3366.8,
        9,
        1
      ],
      [
        3367,
        0,
        1
      ],
      [
        3368,
        8,
        2
      ]
    ],
    "b": [
      [
        3366.1,
        7,
        1
      ],
      [
        3366,
        6,
        1
      ]
    ],
    "ts": "1730969017964"
  }
}
```

## Get Recent Public Fills

`GET /api/v3/market/fills`

Rate limit: 20/sec/IP

Query recent public fill data on Bitget.

You can download historical trades data on our <a href="https://www.bitget.com/data-download">web</a>.

This endpoint now also returns Bitget-platform fills for Reality (rtoken) trading pairs. This was not supported previously.

Operation ID: `marketGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| limit | query | string |  | Limit per page. Default: 100. Maximum: 100<br>默认: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].execId | string |  | Fill execution ID |
| data[].execLinkId | string |  | Execution correlation ID |
| data[].price | string |  | Fill price |
| data[].size | string |  | Fill size<br><br>`COIN-FUTURES`: the unit is quote coin<br><br>Others: the unit is base coin |
| data[].side | string |  | Trade side<br><br>`sell` / `buy` |
| data[].ts | string |  | Fill timestamp<br><br>A Unix timestamp in milliseconds |
| data[].isRPI | string |  | Whether it is an RPI fill<br><br>`yes` Yes<br><br>`no` No |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1690313813709,
  "data": [
    {
      "execId": "1",
      "execLinkId": "12345877111",
      "price": "29990.5",
      "size": "0.0166",
      "side": "sell",
      "ts": "1627116776464",
      "isRPI": "no"
    },
    {
      "execId": "2",
      "execLinkId": "12345877112",
      "price": "30007.0",
      "size": "0.0166",
      "side": "buy",
      "ts": "1627116600875",
      "isRPI": "yes"
    }
  ]
}
```

## Get Kline/Candlestick

`GET /api/v3/market/candles`

Rate limit: 20/sec/IP

Query kline/candlestick data. This endpoint allows retrieving up to 1,000 candlesticks.

You can download historical candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Notes for Reality stock (rtoken) symbols:

- Only the `market` candlestick type is supported. Passing `mark`, `index`, or `premium` falls back to `market` without returning an error.

- Only the `1m`, `5m`, `15m`, `1H`, `4H`, `1D` intervals are supported. Passing an unsupported interval returns a parameter error.

Operation ID: `marketGetCandles`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| interval | query | string | 是 | Granularity<br><br>`1m`,`3m`,`5m`,`15m`,`30m`,`1H`,`4H`,`6H`,`12H`,`1D` |
| startTime | query | string |  | Start timestamp. A Unix millisecond timestamp, e.g. 1672410780000 |
| endTime | query | string |  | End timestamp. A Unix millisecond timestamp, e.g. 1672410781000 |
| type | query | string |  | Candlestick type<br><br>`market`, `mark`, `index`, `premium`. Default: market<br>默认: `market` |
| limit | query | string |  | Limit per page. Default: 1000. Maximum: 1000<br>默认: `1000` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | array |  | Each entry: [timestamp, open, high, low, close, base coin volume, quote coin turnover] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865864944,
  "data": [
    [
      "1687708800000",
      "27176.93",
      "27177.43",
      "27166.93",
      "27177.43",
      "2990.08",
      "81246917.3294"
    ],
    [
      "1688313600000",
      "27177.43",
      "27177.43",
      "24000",
      "24001",
      "2989.1",
      "72450031.0448"
    ]
  ]
}
```

## Get Kline/Candlestick History

`GET /api/v3/market/history-candles`

Rate limit: 20/sec/IP

You can retrieve historical candlestick data from more than 90 days ago.

Note: If endTime goes past a candle interval boundary (even by 1 ms), the system may round up when calculating the number of candles, and the response may include one additional interval (i.e. the returned data may start one interval earlier).

You can download historical candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Notes for Reality stock (rtoken) symbols:

- Only the `market` candlestick type is supported. Passing `mark`, `index`, or `premium` falls back to `market` without returning an error.

- Only the `1m`, `5m`, `15m`, `1H`, `4H`, `1D` intervals are supported. Passing an unsupported interval returns a parameter error.

Operation ID: `marketGetHistoryCandles`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| interval | query | string | 是 | Granularity<br><br>`1m`,`3m`,`5m`,`15m`,`30m`,`1H`,`4H`,`6H`,`12H`,`1D` |
| startTime | query | string |  | Start timestamp. A Unix millisecond timestamp, e.g. 1672410780000. Request data after this start time (the maximum time query range is 90 days) |
| endTime | query | string |  | End timestamp. A Unix millisecond timestamp, e.g. 1672410781000. Request data before this end time (the maximum time query range is 90 days) |
| type | query | string |  | Candlestick type<br><br>`market`, `mark`, `index`, `premium`. Default: market<br>默认: `market` |
| limit | query | string |  | Limit per page. Default: 100. Maximum: 100<br>默认: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | array |  | Each entry: [timestamp, open, high, low, close, base coin volume, quote coin turnover] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865864944,
  "data": [
    [
      "1687708800000",
      "27176.93",
      "27177.43",
      "27166.93",
      "27177.43",
      "2990.08",
      "81246917.3294"
    ],
    [
      "1688313600000",
      "27177.43",
      "27177.43",
      "24000",
      "24001",
      "2989.1",
      "72450031.0448"
    ]
  ]
}
```

## Get Server Time

`GET /api/v3/market/time`

Get the current server time.

- Rate limit: 20/sec/IP

Operation ID: `marketGetServerTime`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.serverTime | string |  | Server time, Unix **millisecond** timestamp, e.g. `1690196141868` |
| data.serverTimeMicros | string |  | Server time, Unix **microsecond** timestamp, e.g. `1690196141868000` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1690196141868,
  "data": {
    "serverTime": "1690196141868",
    "serverTimeMicros": "1690196141868000"
  }
}
```

## Get Coins

`GET /api/v3/market/coins`

Get coin information, supporting both individual and full queries.

- Rate limit: 20/sec/IP

Operation ID: `marketGetCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name, e.g. `BTC`<br><br>If this field is left blank, all coin information is returned by default |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].transfer | string |  | Transferability |
| data[].chains | object[] |  | Supported chain list |
| data[].chains[].chain | string |  | Chain name |
| data[].chains[].needTag | string |  | Whether a tag is required |
| data[].chains[].withdrawable | string |  | Whether withdrawal is supported |
| data[].chains[].rechargeable | string |  | Whether deposit is supported |
| data[].chains[].withdrawFee | string |  | Withdrawal fee |
| data[].chains[].extraWithdrawFee | string |  | Extra charge for on-chain transaction destruction, e.g. `0.1` means `10%` |
| data[].chains[].depositConfirm | string |  | Deposit confirmation blocks |
| data[].chains[].withdrawConfirm | string |  | Withdrawal confirmation blocks |
| data[].chains[].minDepositAmount | string |  | Minimum deposit amount |
| data[].chains[].minWithdrawAmount | string |  | Minimum withdrawal amount |
| data[].chains[].browserUrl | string |  | Blockchain explorer address |
| data[].chains[].contractAddress | string |  | Coin contract address |
| data[].chains[].withdrawStep | string |  | Withdrawal count step<br><br>If non-zero, the withdrawal amount must be a multiple of this value. If `0`, there is no such restriction. |
| data[].chains[].withdrawMinScale | string |  | Decimal places of the withdrawal amount |
| data[].chains[].congestion | string |  | Chain network congestion status<br><br>`normal`: normal<br><br>`congested`: congested |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    {
      "coin": "BTC",
      "transfer": "true",
      "chains": [
        {
          "chain": "BTC",
          "needTag": "false",
          "withdrawable": "true",
          "rechargeable": "true",
          "withdrawFee": "0.005",
          "extraWithdrawFee": "0",
          "depositConfirm": "1",
          "withdrawConfirm": "1",
          "minDepositAmount": "0.001",
          "minWithdrawAmount": "0.001",
          "browserUrl": "https://blockchair.com/bitcoin/testnet/transaction/",
          "contractAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
          "withdrawStep": "0",
          "withdrawMinScale": "8",
          "congestion": "normal"
        }
      ]
    }
  ]
}
```

## Get Announcements

`GET /api/v3/public/annoucements`

Search for announcements.

Description of the announcement sub-type (the announcement sub-type matches the announcement type):

- annType=`latest_news`
  - `announcements` Latest announcement
  - `news` Bitget news
- annType=`coin_listings`
  - `spot`
  - `futures`
  - `margin`
  - `copy_trading`
- annType=`product_updates`
  - `spot`
  - `futures`
  - `margin`
  - `copy_trading`
- annType=`security`
  - `security_information`
- annType=`api_trading`
  - `api_announcement`
- annType=`symbol_delisting`
  - `trading_pair_delisting`
- annType=`maintenance_system_updates`
  - `asset_maintenance`
  - `system_updates`
  - `spot_maintenance`
  - `futures_maintenance`

- Rate limit: 20/sec/IP

Operation ID: `publicGetAnnouncements`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| annType | query | string |  | Announcement type<br><br>`latest_news`: Latest events<br><br>`coin_listings`: New coin listings<br><br>`product_updates`: Product update<br><br>`security`: Security<br><br>`api_trading`: Api trading<br><br>`maintenance_system_updates`: maintenance/system upgrades<br><br>`symbol_delisting`: Delisting information |
| startTime | query | string |  | Start time of the query, Unix millisecond timestamp, e.g. 1690196141868<br><br>Search by announcement display time |
| endTime | query | string |  | End time of the query, Unix millisecond timestamp, e.g. 1690196141868<br><br>Search by announcement display time |
| cursor | query | string |  | Cursor ID<br><br>It is not required for the first call. For subsequent calls, pass the last `annId` from the previous response. |
| limit | query | string |  | Number of entries per page<br><br>By default, it is 10 entries, and the maximum is 10 entries. |
| language | query | string | 是 | Language type<br><br>`zh_CN`: Chinese<br><br>`en_US`: English<br><br>Returns English if the language selected is not supported |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].annId | string |  | Announcement ID |
| data[].annTitle | string |  | Announcement title |
| data[].language | string |  | Language type |
| data[].annUrl | string |  | Announcement URL |
| data[].annType | string |  | Announcement type<br><br>`latest_news`: Latest events<br><br>`coin_listings`: New coin listings<br><br>`product_updates`: Product update<br><br>`security`: Security<br><br>`api_trading`: Api trading<br><br>`maintenance_system_updates`: maintenance/system upgrades<br><br>`symbol_delisting`: Delisting information |
| data[].annSubType | string |  | Announcement sub-type |
| data[].createdTime | string |  | Announcement release time<br><br>A Unix millisecond timestamp. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": [
    {
      "annId": "1",
      "annTitle": "test0629",
      "language": "zh_CN",
      "annUrl": "https://www.bitget.com/zh_CN/support/articles/23685",
      "annType": "maintenance_system_updates",
      "annSubType": "asset_maintenance",
      "createdTime": "1688008040000"
    }
  ]
}
```

## Get Open Interest (OI)

`GET /api/v3/market/open-interest`

Rate limit: 20/sec/IP

Query the open interest of a trading pair (calculated as the sum of long and short positions).

Operation ID: `derivativesGetOpenInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product Type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name, e.g. `BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  |  |
| data.list[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data.list[].openInterest | string |  | Open interest (in base currency) |
| data.ts | string |  | The timestamp that the system generated the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969652387,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "openInterest": "2243.019"
      }
    ],
    "ts": "1730969652411"
  }
}
```

## Get Open Interest History

`GET /api/v3/market/open-interest-history`

Query the historical open interest for futures trading pairs.

- Rate limit: 10/sec/IP

Operation ID: `derivativesGetOpenInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol name |
| period | query | string | 是 | Time granularity<br><br>Default `5m`<br><br>Supports `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Open interest data set |
| data.list[].symbol | string |  | Symbol name |
| data.list[].openInterest | string |  | Open interest<br><br>Unit: base coin |
| data.list[].oneSideOpenInterest | string |  | Open interest (one-way)<br><br>Unit: base coin |
| data.list[].openInterestValue | string |  | Open interest value<br><br>Unit: quote coin<br><br>`openInterestValue = openInterest * markPrice` |
| data.list[].oneSideOpenInterestValue | string |  | Open interest value (one-way)<br><br>Unit: quote coin |
| data.list[].timestamp | string |  | End timestamp of this period<br><br>A Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1756616400000.0,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "openInterest": "2243.019",
        "oneSideOpenInterest": "1121.5095",
        "openInterestValue": "193486281.47",
        "oneSideOpenInterestValue": "96743140.735",
        "timestamp": "1756616400000"
      }
    ]
  }
}
```

## Get Liquidations History

`GET /api/v3/market/liquidations`

Rate limit: 5/sec/IP

Query historical liquidation order data. Only the data from the last 3 days is available. There may be some delay in the data.

Operation ID: `derivativesGetLiquidations`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product Type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name, e.g. `BTCUSDT` |
| limit | query | string |  | Items per page<br><br>Default: 100. Maximum: 100 |
| cursor | query | string |  | Cursor ID<br><br>Pass the `cursor` from the last query response for paginated queries |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  |  |
| data.list[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data.list[].side | string |  | Position direction<br><br>`buy` Long position liquidation<br><br>`sell` Short position liquidation |
| data.list[].price | string |  | Liquidation price |
| data.list[].amount | string |  | Liquidation amount (in base currency) |
| data.list[].ts | string |  | Liquidation time<br><br>A Unix timestamp in milliseconds |
| data.cursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "side": "buy",
        "price": "29990.5",
        "amount": "0.5",
        "ts": "1690313813709"
      }
    ],
    "cursor": "1690313813709"
  },
  "msg": "success",
  "requestTime": 1690313813709
}
```

## Get Current Funding Rate

`GET /api/v3/market/current-fund-rate`

Rate limit: 20/sec/IP

Get current funding rate.

Operation ID: `derivativesGetCurrentFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Trading pair name, e.g. BTCUSDT<br><br>`category` and `symbol` cannot both be empty |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data[].fundingRate | string |  | [Current funding rate](https://www.bitget.com/trade-info/funding_rate). In decimal form, e.g. 0.000088 represents 0.0088% |
| data[].fundingRateInterval | string |  | Funding rate settlement period, unit: hour<br><br>1 represents 1 hour, 2 represents 2 hours, and so on |
| data[].nextUpdate | string |  | Next update time of the funding rate<br><br>Unix millisecond timestamp |
| data[].minFundingRate | string |  | Lower limit of funding rate<br><br>Returned in decimal form, e.g. 0.025 represents 2.5% |
| data[].maxFundingRate | string |  | Upper limit of funding rate<br><br>Returned in decimal form, e.g. 0.025 represents 2.5% |
| data[].lastFundingRate | string |  | Last funding rate<br/>In decimal form, e.g. 0.000088 represents 0.0088 |
| data[].nextFundingRate | string |  | Next funding rate<br/>In decimal form, e.g. 0.000088 represents 0.0088 |
| data[].baseInterestRate | string |  | Base interest rate<br/>In decimal form, e.g. 0.0001 represents 0.01% |
| data[].impactMarginNotional | string |  | Impact margin notional<br/>Unit: quote coin |
| data[].cashDividend | string |  | Per-share cash dividend, unit: USDT. Only has a value when there is a cash dividend event<br><br>Cash dividend paid by RWA stock contracts to eligible holders. For details, refer to [this article](https://www.bitget.com/support/articles/12560603884677) |
| data[].cashDividendNextUpdate | string |  | Next update time of the cash dividend. Only has a value when there is a cash dividend event<br><br>Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743059269376,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000071",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003",
      "lastFundingRate": "0.000071",
      "nextFundingRate": "0.000088",
      "baseInterestRate": "0.0001",
      "impactMarginNotional": "20000",
      "cashDividend": null,
      "cashDividendNextUpdate": null
    }
  ]
}
```

## Get Funding Rate History

`GET /api/v3/market/history-fund-rate`

Rate limit: 20/sec/IP

Get historical funding rate records for the contract (last 90 days). The funding settlement time varies by trading pair.

Operation ID: `derivativesGetHistoryFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product Type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| cursor | query | string |  | Page cursor, used for pagination<br><br>Maximum: 100. Default: 1 |
| limit | query | string |  | Items per page<br><br>Maximum: 100. Default: 20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  |  |
| data.resultList[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data.resultList[].fundingRate | string |  | Funding rate<br><br>In decimal form, e.g. 0.000074 represents 0.0074% |
| data.resultList[].fundingRateTimestamp | string |  | Settlement time<br><br>Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1754908278922,
  "data": {
    "resultList": [
      {
        "symbol": "BTCUSDT",
        "fundingRate": "0.0001",
        "fundingRateTimestamp": "1754899200000"
      },
      {
        "symbol": "BTCUSDT",
        "fundingRate": "0.0001",
        "fundingRateTimestamp": "1754870400000"
      }
    ]
  }
}
```

## Get Index Price Components

`GET /api/v3/market/index-components`

Rate limit: 10/sec/IP

Get index price components.

Operation ID: `derivativesGetIndexComponents`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair, e.g. BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.componentList | object[] |  |  |
| data.componentList[].exchange | string |  | Exchange |
| data.componentList[].spotPair | string |  | Spot trading pair name |
| data.componentList[].equivalentPrice | string |  | Equivalent price |
| data.componentList[].weight | string |  | Calculation weight<br><br>Decimal format, e.g., 0.5 represents 50% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767159256214,
  "data": {
    "symbol": "BTCUSDT",
    "componentList": [
      {
        "exchange": "BITGET_FUTURE",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88432.1",
        "weight": "0.4696"
      },
      {
        "exchange": "GATEIO",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88467",
        "weight": "0.164"
      },
      {
        "exchange": "BINANCE",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88456.65",
        "weight": "0.1434"
      },
      {
        "exchange": "MEXC",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88457.1",
        "weight": "0.0992"
      },
      {
        "exchange": "BITGET",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88469.77",
        "weight": "0.0768"
      },
      {
        "exchange": "OKX",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88463",
        "weight": "0.0468"
      }
    ]
  }
}
```

## Get Proof Of Reserves

`GET /api/v3/market/proof-of-reserves`

Rate limit: 20/sec/IP

Get Proof Of Reserves

Operation ID: `publicConfigGetProofOfReserves`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.merkleRootHash | string |  | Merkle root hash |
| data.totalReserveRatio | string |  | Total reserve ratio<br>Returned in percentage format. |
| data.list | object[] |  | List |
| data.list[].coin | string |  | Currency name |
| data.list[].platformAssets | string |  | Platform funds<br>Precision is two decimal places, with the unit being the corresponding currency (coin) |
| data.list[].userAssets | string |  | User funds<br>Precision is two decimal places, with the unit being the corresponding currency (coin) |
| data.list[].reserveRatio | string |  | Reserve ratio<br>Returned in percentage format. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753845058586,
  "data": {
    "merkleRootHash": "e0dff99bbe2c2dcb",
    "totalReserveRatio": "175%",
    "list": [
      {
        "coin": "BTC",
        "userAssets": "9530.89",
        "platformAssets": "29679.59",
        "reserveRatio": "311%"
      },
      {
        "coin": "USDT",
        "userAssets": "1948633388.98",
        "platformAssets": "1985576297.93",
        "reserveRatio": "102%"
      },
      {
        "coin": "ETH",
        "userAssets": "195465.81",
        "platformAssets": "294561.45",
        "reserveRatio": "151%"
      },
      {
        "coin": "USDC",
        "userAssets": "58830275.64",
        "platformAssets": "157216065.76",
        "reserveRatio": "267%"
      }
    ]
  }
}
```

## Get Market Maker Score Weight

`GET /api/v3/market/score-weights`

Rate limit: 5/sec/IP

Used by market makers to query the market-making score weights for each symbol

Operation ID: `publicConfigGetScoreWeights`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Business line type<br>`SPOT`<br>`FUTURES`<br>If not filled in, all business lines will be returned by default. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | Business line type<br>`SPOT`<br>`FUTURES` |
| data[].label | string |  | Label |
| data[].symbol | string |  | Symbol name<br>e.g: ETHUSDT |
| data[].requiredSpread | string |  | Required maker-order spread rate<br>For example, 0.0005 means 0.05% |
| data[].minMakerVolume | string |  | Cumulative minimum maker-order amount<br>Positive integer, e.g. 5000, 10000<br>unit: USDT |
| data[].weight | string |  | Weight (in decimal form) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1772524004421,
  "data": [
    {
      "category": "SPOT",
      "label": "usdt",
      "symbol": "LUMIAUSDT",
      "requiredSpread": "0.0005",
      "minMakerVolume": "500",
      "weight": "50"
    }
  ]
}
```

## Get Institution Fee Group

`GET /api/v3/market/fee-group`

Rate limit: 5/sec/IP

Used to query the system's preset institution fee rate tiers and grouping parameters.

Operation ID: `publicConfigGetFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Business line type<br>`SPOT`<br>`FUTURES` |
| group | query | string |  | Group type<br>Spot:<br>`GROUP_A` Core mainstream<br>`GROUP_B` High-potential<br>`DEFAULT` Default<br>Futures:<br>`GROUP_A` Core mainstream<br>`GROUP_B` High-potential<br>`GROUP_C` Cold start<br>`DEFAULT` Default<br>If not provided, the fee rate configurations for all groups will be returned by default. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | Business line type<br>`SPOT`<br>`FUTURES` |
| data[].group | string |  | Group type<br>Spot:<br>`GROUP_A` Core mainstream<br>`GROUP_B` High-potential<br>`DEFAULT` Default<br>Futures:<br>`GROUP_A` Core mainstream<br>`GROUP_B` High-potential<br>`GROUP_C` Cold start<br>`DEFAULT` Default |
| data[].labelList | object[] |  | Label List |
| data[].labelList[].weight | string |  | weight<br>Two decimal places of precision. |
| data[].labelList[].label | string |  | Label |
| data[].labelList[].symbols | string[] |  | List of symbols included under the label<br>e.g. ["ETHUSDT","SOLUSDT","BTCUSDT"] |
| data[].tierList | object[] |  | Fee tier list |
| data[].tierList[].level | string |  | User level:<br>MM1/MM2/MM3/MM4/MM5/PRO1/PRO2/PRO3/PRO4/PRO5/PRO6 |
| data[].tierList[].makerFeeRate | string |  | Maker fee rate in decimal form<br>e.g. 0.0001 means 0.01% |
| data[].tierList[].takerFeeRate | string |  | Taker fee rate in decimal form<br>e.g. 0.0001 means 0.01%<br>Only applicable to PRO levels (PRO1~PRO6); absent for MM levels |
| data[].tierList[].rpiMakerFeeRate | string |  | RPI maker fee rate in decimal form<br>e.g. `0.0001` means 0.01%<br>Applies to market maker users and only available for trading pairs with RPI enabled |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1772462728068,
  "data": [
    {
      "category": "SPOT",
      "group": "GROUP_A",
      "labelList": [
        {
          "weight": "1.00",
          "label": "core_mainstream",
          "symbols": [
            "DOGEUSDT",
            "XRPUSDT",
            "BTCUSDT",
            "ETHUSDT",
            "SOLUSDT",
            "BGBUSDT"
          ]
        }
      ],
      "tierList": [
        {
          "level": "MM1",
          "makerFeeRate": "-0.0001"
        },
        {
          "level": "MM2",
          "makerFeeRate": "-0.00008"
        },
        {
          "level": "MM3",
          "makerFeeRate": "-0.00004"
        },
        {
          "level": "MM4",
          "makerFeeRate": "-0.00001"
        },
        {
          "level": "MM5",
          "makerFeeRate": "0"
        },
        {
          "level": "PRO1",
          "makerFeeRate": "0.00025",
          "takerFeeRate": "0.0004"
        },
        {
          "level": "PRO2",
          "makerFeeRate": "0.0002",
          "takerFeeRate": "0.000375"
        },
        {
          "level": "PRO3",
          "makerFeeRate": "0.000175",
          "takerFeeRate": "0.000313"
        },
        {
          "level": "PRO4",
          "makerFeeRate": "0.00015",
          "takerFeeRate": "0.000288"
        },
        {
          "level": "PRO5",
          "makerFeeRate": "0.0001",
          "takerFeeRate": "0.000238"
        },
        {
          "level": "PRO6",
          "makerFeeRate": "0.0001",
          "takerFeeRate": "0.000219"
        }
      ]
    }
  ]
}
```

## Get Cash Dividend Records

`GET /api/v3/market/cash-dividend-records`

Rate limit: 10/sec/IP

Get cash dividend records for RWA stock futures contracts.

Operation ID: `publicConfigGetCashDividendRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name |
| type | query | string | 是 | Dividend type<br>`pending` Upcoming dividend<br>`paid` Paid dividend |
| cursor | query | string |  | Pagination cursor<br>Used for pagination; maximum 100, default is 1<br>默认: `1` |
| limit | query | string |  | Number of entries per page<br>Maximum 100, default is 20<br>默认: `20` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].exDividendDate | string |  | Ex-dividend date |
| data[].cashDividendPerShare | string |  | Cash dividend per share<br>Unit: USDT |
| data[].cashDividendTimestamp | string |  | Cash dividend settlement time<br>Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1749484800000.0,
  "data": [
    {
      "symbol": "AAPLXRPUSDT",
      "exDividendDate": "2026-06-09",
      "cashDividendPerShare": "0.25",
      "cashDividendTimestamp": "1749484800000"
    }
  ]
}
```

## Get Split Records

`GET /api/v3/market/split-records`

Get RWA stock split/reverse split records.
- Rate limit: 5/sec/IP

Operation ID: `publicConfigGetSplitRecords`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name, e.g. KORUUSDT |
| data[].type | string |  | Split type<br>`split` Stock split<br>`reverse_split` Reverse stock split |
| data[].status | string |  | Split status<br>`pending` Upcoming split<br>`ongoing` Split in progress<br>`completed` Split completed |
| data[].adjustmentRatio | string |  | Adjustment ratio<br>For a split, the value is greater than 1, e.g. `20` means 1-for-20 split<br>For a reverse split, the value is less than 1, e.g. `0.1` means 10-for-1 reverse split |
| data[].exDividendDate | string |  | Ex-dividend date<br>Format: yyyy-MM-dd |
| data[].exDividendDateTimezone | string |  | Timezone of the ex-dividend date, always returns `ET` |
| data[].tradingHaltStartTime | string |  | Trading halt start time<br>Unix timestamp in milliseconds |
| data[].tradingHaltEndTime | string |  | Trading halt end time<br>Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1749484800000.0,
  "data": [
    {
      "symbol": "KORUUSDT",
      "type": "split",
      "status": "pending",
      "adjustmentRatio": "20",
      "exDividendDate": "2026-06-09",
      "exDividendDateTimezone": "ET",
      "tradingHaltStartTime": "1749484800000",
      "tradingHaltEndTime": "1749488400000"
    }
  ]
}
```

## Get Risk Reserve(Daily)

`GET /api/v3/market/risk-reserve`

Rate limit: 20/sec/IP

Query risk reserve data for the last 30 days (daily granularity).

Operation ID: `tradingRiskRulesGetRiskReserve`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| marginCoin | query | string |  | Margin coin, It is required when the category is COIN-FUTURES |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalBalance | string |  | Total balance of the risk reserve fund (Deprecated) |
| data.coin | string |  | Settlement coin |
| data.riskReserveRecords | object[] |  | Risk reserve records |
| data.riskReserveRecords[].type | string |  | Operation type (Deprecated) |
| data.riskReserveRecords[].amount | string |  | Fund adjustment amount |
| data.riskReserveRecords[].balance | string |  | The balance of the risk reserve fund |
| data.riskReserveRecords[].ts | string |  | The timestamp that the system records the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "totalBalance": "",
    "coin": "USDT",
    "riskReserveRecords": [
      {
        "type": "",
        "amount": "9.8470265278770000",
        "balance": "95815.6773460800020000",
        "ts": "1753718400000"
      },
      {
        "type": "",
        "amount": "0.4328615782800000",
        "balance": "95805.8303195521250000",
        "ts": "1753632000000"
      }
    ]
  }
}
```

## Get Risk Reserve(Hourly)

`GET /api/v3/market/risk-reserve-hour`

Rate limit: 20/sec/IP

Query risk reserve data for the last 30 hours (hourly granularity).

Operation ID: `tradingRiskRulesGetRiskReserveHour`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string | 是 | Symbol name, e.g. BTCUSDT |
| marginCoin | query | string |  | Margin coin, It is required when the category is COIN-FUTURES |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Settlement coin |
| data.riskReserveRecords | object[] |  | Risk reserve records |
| data.riskReserveRecords[].amount | string |  | Fund adjustment amount |
| data.riskReserveRecords[].balance | string |  | The balance of the risk reserve fund |
| data.riskReserveRecords[].ts | string |  | The timestamp that the system records the data<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "coin": "USDT",
    "riskReserveRecords": [
      {
        "amount": "9.8470265278770000",
        "balance": "95815.6773460800020000",
        "ts": "1753718400000"
      },
      {
        "amount": "0.4328615782800000",
        "balance": "95805.8303195521250000",
        "ts": "1753632000000"
      }
    ]
  }
}
```

## Get Risk Reserve All

`GET /api/v3/market/risk-reserve-all`

Rate limit: 3/sec/IP

Get all current insurance funds.

Independent insurance pool data is refreshed every 1 minute, while the aggregate insurance pool data is refreshed every 1 hour.

Operation ID: `tradingRiskRulesGetRiskReserveAll`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Insurance fund list |
| data.list[].symbols | string[] |  | Symbol<br><br>For symbol-aggregated insurance funds, multiple symbols will be returned<br><br>for an independent insurance fund, only one symbol will be returned |
| data.list[].coin | string |  | Insurance fund currency name |
| data.list[].balance | string |  | Insurance fund currency balance |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "list": [
      {
        "symbols": [
          "BTCUSDT"
        ],
        "coin": "USDT",
        "balance": "95815.6773460800020000"
      }
    ]
  }
}
```

## Get Margin Loan

`GET /api/v3/market/margin-loans`

Rate limit: 20/sec/IP

Query interest rates for margin loans.

Operation ID: `tradingRiskRulesGetMarginLoans`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name, e.g. BTC |
| level | query | string |  | User level<br/>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br/>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br/>Default: `vip0` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.dailyInterest | string |  | Daily interest rate |
| data.annualInterest | string |  | Annual interest rate |
| data.limit | string |  | Loan limit |
| data.masterSubLimit | string |  | Master/sub account limit |
| data.platformRemaingQuota | string |  | Platform remaining quota |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730912814587,
  "data": {
    "dailyInterest": "0.1",
    "annualInterest": "0.00416667",
    "limit": "3000",
    "masterSubLimit": "1000",
    "platformRemaingQuota": "500000"
  }
}
```

## Get All Margin Loans

`GET /api/v3/market/margin-loans-all`

Rate limit: 20/sec/IP

Query the margin loan information of all coins. When `coin` is not provided, the information of all supported coins is returned.

Operation ID: `tradingRiskRulesGetMarginLoansAll`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name, e.g. `BTC`<br/>If not provided, the information of all supported coins is returned |
| level | query | string |  | User level<br/>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br/>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br/>Default: `vip0` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].dailyInterest | string |  | Daily interest rate |
| data[].annualInterest | string |  | Annual interest rate |
| data[].limit | string |  | Loan limit |
| data[].masterSubLimit | string |  | Master/sub account limit |
| data[].platformRemaingQuota | string |  | Platform remaining quota |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1792646640213,
  "data": [
    {
      "coin": "rWELL",
      "dailyInterest": "0.0000085680",
      "annualInterest": "0.0031273200",
      "limit": "0",
      "masterSubLimit": "0",
      "platformRemaingQuota": "0"
    }
  ]
}
```

## Get Interest Rate History

`GET /api/v3/market/interest-rate-history`

Query the historical margin borrowing interest rate for a specified coin and VIP tier. Used for backtesting borrowing costs, reconciling historical position interest, or estimating the interest savings from a VIP tier upgrade.

Data granularity is fixed at 1 hour, with the most recent 1 month retained.

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `tradingRiskRulesGetInterestRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name, e.g. `USDT`<br><br>Only coins with margin borrowing enabled are supported; an unsupported coin returns an error |
| startTime | query | string |  | Start time, a Unix millisecond timestamp<br><br>Only data from the most recent 1 month is supported |
| endTime | query | string |  | End time, a Unix millisecond timestamp<br><br>Must not be more than 30 days apart from `startTime`<br><br>If no time parameters are provided, returns the most recent `limit` entries counting back from now |
| level | query | string |  | User tier<br><br>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br><br>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br><br>Default: `vip0` |
| limit | query | string |  | Number of entries per page<br><br>Default: `10`. Maximum: `500` |
| cursor | query | string |  | Pagination cursor<br><br>Pass the `cursor` from the previous page's response |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cursor | string |  | Cursor for the next page<br><br>Empty indicates there is no more data |
| data.list | object[] |  | Interest rate history data set |
| data.list[].coin | string |  | Coin name |
| data.list[].dailyInterestRate | string |  | Daily interest rate<br><br>In decimal form, e.g. `0.01` represents `1%` |
| data.list[].annualInterestRate | string |  | Annual interest rate<br><br>In decimal form, e.g. `0.01` represents `1%` |
| data.list[].ts | string |  | Interest rate effective time<br><br>A Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1756616400000.0,
  "data": {
    "cursor": "1756594800000",
    "list": [
      {
        "coin": "USDT",
        "dailyInterestRate": "0.00007704",
        "annualInterestRate": "0.0281",
        "ts": "1756616400000"
      },
      {
        "coin": "USDT",
        "dailyInterestRate": "0.00007728",
        "annualInterestRate": "0.0282",
        "ts": "1756609200000"
      }
    ]
  }
}
```

## Get Position Tier

`GET /api/v3/market/position-tier`

Rate limit: 20/sec/IP

Query the position tier info.

Operation ID: `tradingRiskRulesGetPositionTier`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name, e.g. BTCUSDT, applies to Futures |
| coin | query | string |  | Coin name, e.g. BTC, applies to Margin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tier | string |  | Position tier |
| data[].leverage | string |  | Leverage |
| data[].minTierValue | string |  | Minimum value of current tier<br><br>Available only for futures |
| data[].maxTierValue | string |  | Maximum value of current tier<br><br>Available only for futures |
| data[].mmr | string |  | Maintenance margin ratio<br><br>When the margin rate of the position falls below the maintenance margin rate, forced liquidation or position reduction will be triggered |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1731146663643,
  "data": [
    {
      "tier": "1",
      "minTierValue": "0",
      "maxTierValue": "100000",
      "leverage": "125",
      "mmr": "0.004"
    }
  ]
}
```

## Get Open Interest Limit

`GET /api/v3/market/oi-limit`

Rate limit: 10/sec/IP

Interface is used to get future contract OI Limit.

Operation ID: `tradingRiskRulesGetOiLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair, based on the symbolName, i.e. BTCUSDT |
| category | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Product name |
| data[].notionalValue | string |  | Individual User Position Notional Value |
| data[].totalNotionalValue | string |  | Sub-account and Main-account Position Notional Value |
| data[].singlePositionRatio | string |  | Single UID contract position ratio<br/>Returned as a decimal, e.g. `0.1` represents 10% |
| data[].totalPositionRatio | string |  | Master/sub-account contract position ratio<br/>Returned as a decimal, e.g. `0.1` represents 10% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741665165571,
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "1000000",
      "totalNotionalValue": "5000000",
      "singlePositionRatio": "0.1",
      "totalPositionRatio": "0.2"
    },
    {
      "symbol": "ETHUSDT",
      "notionalValue": "1000000",
      "totalNotionalValue": "5000000",
      "singlePositionRatio": "0.1",
      "totalPositionRatio": "0.2"
    }
  ]
}
```

## Get Discount Rate

`GET /api/v3/market/discount-rate`

Rate limit: 20/sec/IP

Query discount rate applied to margin loans.

Operation ID: `tradingRiskRulesGetDiscountRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name, e.g. BTC |
| data[].list | object[] |  | List |
| data[].list[].tierStartValue | string |  | Tier start value<br><br>e.g., [0,10000 U): tierStartValue=0<br><br>[10000 U,20000 U): tierStartValue=10000<br><br>[20000 U,∞): tierStartValue=20000 |
| data[].list[].discountRate | string |  | Discount rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730911874605,
  "data": [
    {
      "coin": "ETH",
      "list": [
        {
          "tierStartValue": "0",
          "discountRate": "0.99"
        },
        {
          "tierStartValue": "40000",
          "discountRate": "0.98"
        }
      ]
    }
  ]
}
```

## Get Spot Whale Net Flow Data

`GET /api/v3/market/spot-whale-flow`

Rate limit: 1/sec/IP

Get spot whale net flow data.

Operation ID: `tradingStatsGetSpotWhaleNetFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].volume | string |  | Whale buy sell volume |
| data[].date | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "volume": "-1.1",
      "date": "1713942000000"
    }
  ]
}
```

## Get Spot Fund Flow Data

`GET /api/v3/market/spot-fund-flow`

Rate limit: 1/sec/IP

Get spot fund flow data.

Operation ID: `tradingStatsGetSpotFundFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair, e.g. BTCUSDT |
| period | query | string |  | Query period:<br><br>15m (default), 30m, 1h, 2h, 4h, 1d<br>默认: `15m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.whaleBuyVolume | string |  | Whale buy volume |
| data.dolphinBuyVolume | string |  | Dolphin buy volume |
| data.fishBuyVolume | string |  | Fish buy volume |
| data.whaleSellVolume | string |  | Whale sell volume |
| data.dolphinSellVolume | string |  | Dolphin sell volume |
| data.fishSellVolume | string |  | Fish sell volume |
| data.whaleBuyRatio | string |  | Whale buy ratio |
| data.dolphinBuyRatio | string |  | Dolphin buy ratio |
| data.fishBuyRatio | string |  | Fish buy ratio |
| data.whaleSellRatio | string |  | Whale sell ratio |
| data.dolphinSellRatio | string |  | Dolphin sell ratio |
| data.fishSellRatio | string |  | Fish sell ratio |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "whaleBuyVolume": "50.901579",
    "dolphinBuyVolume": "1.506897",
    "fishBuyVolume": "0.529853",
    "whaleSellVolume": "50.635982",
    "dolphinSellVolume": "1.429034",
    "fishSellVolume": "0.344032",
    "whaleBuyRatio": "50.901579",
    "dolphinBuyRatio": "1.506897",
    "fishBuyRatio": "0.529853",
    "whaleSellRatio": "50.635982",
    "dolphinSellRatio": "1.429034",
    "fishSellRatio": "0.344032"
  }
}
```

## Get Spot 24H Net Capital Inflow Data

`GET /api/v3/market/spot-net-flow`

Rate limit: 1/sec/IP

Get spot 24H net capital inflow data.

Operation ID: `tradingStatsGetSpotNetFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].netFlow | string |  | Whale fund net flow |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    }
  ]
}
```

## Get Margin Long Short Ratio Data

`GET /api/v3/market/margin-long-short`

Rate limit: 1/sec/IP

Get the long-short position ratio for a specific coin in cross and isolated margin accounts.

Operation ID: `tradingStatsGetMarginLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>24h, support: 24h, 30d<br>默认: `24h` |
| coin | query | string |  | Base coin or quote coin, default: base coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longShortRatio | string |  | Long short ratio |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longShortRatio": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## Get Margin Loan Growth Rate Data

`GET /api/v3/market/margin-loan-growth`

Rate limit: 1/sec/IP

Get the growth rate of borrowed funds for a specific coin in cross and isolated margin accounts.

Operation ID: `tradingStatsGetMarginLoanGrowth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>24h, support: 24h, 30d<br>默认: `24h` |
| coin | query | string |  | Base coin or quote coin, default: base coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].growthRate | string |  | Growth rate |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "growthRate": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## Get Isolated Margin Borrowing Ratio Data

`GET /api/v3/market/margin-isolated-borrow`

Rate limit: 1/sec/IP

Get the ratio of borrowed amount in the base currency and borrowed amount in the quote currency in isolated margin accounts, converted to USDT.

Operation ID: `tradingStatsGetMarginIsolatedBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>24h, support: 24h, 30d<br>默认: `24h` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].borrowRate | string |  | Borrow ratio |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "borrowRate": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## Get Futures Active Buy Sell Volume Data

`GET /api/v3/market/futures-active-buy-sell`

Rate limit: 1/sec/IP

Get futures active buy sell volume data.

Operation ID: `tradingStatsGetFuturesActiveBuySell`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>5m, support: 5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].buyVolume | string |  | Buy volume |
| data[].sellVolume | string |  | Sell volume |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "buyVolume": "0.01",
      "sellVolume": "0.12",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Futures Long Short Ratio Data

`GET /api/v3/market/futures-long-short`

Rate limit: 1/sec/IP

Get futures long short ratio data.

Operation ID: `tradingStatsGetFuturesLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>5m, support: 5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1Dutc<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longRatio | string |  | Long ratio |
| data[].shortRatio | string |  | Short ratio |
| data[].longShortRatio | string |  | Long short ratio |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longRatio": "0.01",
      "shortRatio": "0.12",
      "longShortRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Futures Active Long Short Position Data

`GET /api/v3/market/futures-position-long-short`

Rate limit: 1/sec/IP

Get futures active long short position data.

Operation ID: `tradingStatsGetFuturesPositionLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>5m, support: 5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longPositionRatio | string |  | Long position ratio |
| data[].shortPositionRatio | string |  | Short position ratio |
| data[].longShortPositionRatio | string |  | Long short position ratio |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longPositionRatio": "0.01",
      "shortPositionRatio": "0.12",
      "longShortPositionRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Futures Active Long Short Account Data

`GET /api/v3/market/futures-account-long-short`

Rate limit: 1/sec/IP

Get futures active long short account data.

Operation ID: `tradingStatsGetFuturesAccountLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:<br><br>5m, support: 5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longAccountRatio | string |  | Long account ratio |
| data[].shortAccountRatio | string |  | Short account ratio |
| data[].longShortAccountRatio | string |  | Long short account ratio |
| data[].ts | string |  | Milliseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longAccountRatio": "0.01",
      "shortAccountRatio": "0.12",
      "longShortAccountRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```


---

公共行情数据、衍生品与资金费率、交易统计数据、交易与风控规则及公共配置接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/market/instruments` — 获取交易产品信息
- `GET /api/v3/market/rpi-symbols` — 获取RPI交易对列表
- `GET /api/v3/market/tickers` — 获取行情数据
- `GET /api/v3/market/orderbook` — 获取深度数据
- `GET /api/v3/market/rpi-orderbook` — 获取RPI深度数据
- `GET /api/v3/market/fills` — 获取平台近期成交数据
- `GET /api/v3/market/candles` — K线数据
- `GET /api/v3/market/history-candles` — 历史K线数据
- `GET /api/v3/market/time` — 获取服务器时间
- `GET /api/v3/market/coins` — 获取币种信息
- `GET /api/v3/public/annoucements` — 获取公告
- `GET /api/v3/market/open-interest` — 获取未平仓合约持仓量(OI)
- `GET /api/v3/market/open-interest-history` — 获取合约持仓量历史
- `GET /api/v3/market/liquidations` — 获取历史爆仓数据
- `GET /api/v3/market/current-fund-rate` — 实时资金费率
- `GET /api/v3/market/history-fund-rate` — 历史资金费率
- `GET /api/v3/market/index-components` — 获取指数价格成分
- `GET /api/v3/market/proof-of-reserves` — 获取储备金证明
- `GET /api/v3/market/score-weights` — 获取做市分数权重
- `GET /api/v3/market/fee-group` — 获取机构费率分组
- `GET /api/v3/market/cash-dividend-records` — 获取现金派息记录
- `GET /api/v3/market/split-records` — 获取拆合股记录
- `GET /api/v3/market/risk-reserve` — 获取风险准备金(天)
- `GET /api/v3/market/risk-reserve-hour` — 获取风险准备金(小时)
- `GET /api/v3/market/risk-reserve-all` — 获取当前全部风险准备金
- `GET /api/v3/market/margin-loans` — 获取杠杆借币信息
- `GET /api/v3/market/margin-loans-all` — 获取杠杆借币信息（全部）
- `GET /api/v3/market/interest-rate-history` — 获取借币利率历史
- `GET /api/v3/market/position-tier` — 获取仓位档位信息
- `GET /api/v3/market/oi-limit` — 获取合约OI限仓信息
- `GET /api/v3/market/discount-rate` — 获取币种折扣率
- `GET /api/v3/market/spot-whale-flow` — 获取现货大户净流入信息
- `GET /api/v3/market/spot-fund-flow` — 获取现货资金流向信息
- `GET /api/v3/market/spot-net-flow` — 获取现货24小时资金净流入信息
- `GET /api/v3/market/margin-long-short` — 获取杠杆多空对比信息
- `GET /api/v3/market/margin-loan-growth` — 获取杠杆借贷存量增速信息
- `GET /api/v3/market/margin-isolated-borrow` — 获取杠杆逐仓借贷比信息
- `GET /api/v3/market/futures-active-buy-sell` — 获取合约主动买卖量信息
- `GET /api/v3/market/futures-long-short` — 获取合约多空比信息
- `GET /api/v3/market/futures-position-long-short` — 获取合约大户持仓量多空比信息
- `GET /api/v3/market/futures-account-long-short` — 获取合约大户账户多空比信息

## 获取交易产品信息

`GET /api/v3/market/instruments`

限频规则: 20次/秒/IP

查询在线交易币对信息

Operation ID: `marketGetInstruments`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，例如：BTCUSDT |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data[].symbol | string |  | 交易对名称 |
| data[].isRwa | string |  | 是否为RWA交易对<br><br>`YES` 是<br><br>`NO` 否<br><br>仅合约返回 |
| data[].isReality | string |  | Reality标识<br><br>`yes` Reality股票代币<br><br>`no` 非Reality股票代币<br><br>仅现货返回 |
| data[].baseCoin | string |  | 交易币种，例如：BTCUSDT中的BTC |
| data[].quoteCoin | string |  | 计价币种，例如：BTCUSDT中的USDT |
| data[].buyLimitPriceRatio | string |  | 买价限价比例<br><br>买入限价与市场价格的比率，决定买单下单时的最高价格 |
| data[].sellLimitPriceRatio | string |  | 卖价限价比例<br><br>卖出限价与市场价格的比率，决定卖单下单时的最低价格 |
| data[].feeRateUpRatio | string |  | 手续费上浮比例<br><br>实际费用相对于基础费用增加的百分比<br><br>仅合约返回 |
| data[].makerFeeRate | string |  | 挂单手续费率，小数形式，即0.0002代表万分之二<br><br>仅合约返回 |
| data[].takerFeeRate | string |  | 吃单手续费率，小数形式，即0.0002代表万分之二<br><br>仅合约返回 |
| data[].openCostUpRatio | string |  | 开仓成本上浮比例<br><br>开仓的成本相对于基础或标准成本增加的百分比<br><br>仅合约返回 |
| data[].minOrderQty | string |  | 最小开单数量，以基础币种计<br><br>现货/杠杆请参考<a href="https://www.bitget.com/zh-CN/trade-info/trade-rule">交易规则</a> |
| data[].maxOrderQty | string |  | 单笔限价单最大下单数量，以基础币种计<br><br>现货/杠杆请参考<a href="https://www.bitget.com/zh-CN/trade-info/trade-rule">交易规则</a><br><br>为0表示不限制 |
| data[].pricePrecision | string |  | 价格精度，价格允许的小数位数 |
| data[].quantityPrecision | string |  | 数量精度，数量允许的小数位数 |
| data[].quotePrecision | string |  | 市价下单精度，计价币价格允许的小数位数 |
| data[].priceMultiplier | string |  | 价格乘数，合约下单使用，配合pricePrecision<br><br>仅合约返回 |
| data[].quantityMultiplier | string |  | 数量乘数，合约下单使用，配合quantityPrecision<br><br>仅合约返回 |
| data[].type | string |  | 合约类型<br><br>`perpetual` 永续<br><br>`delivery` 交割<br><br>仅合约返回 |
| data[].minOrderAmount | string |  | 最小下单额<br><br>单位：USDT |
| data[].maxSymbolOrderNum | string |  | 交易对维度最大委托数量(废弃，无此限制） |
| data[].maxProductOrderNum | string |  | 业务线维度最大委托数量 |
| data[].maxPositionNum | string |  | 最大持有仓位数量（交易对维度）<br><br>仅合约/杠杆返回 |
| data[].status | string |  | 交易对状态<br><br>`listed` 上架(未开盘)<br><br>`online` 正常交易/开盘<br><br>`limit_open` 限制交易(合约禁止开仓)<br><br>`limit_close` 限制交易(合约禁止平仓)<br><br>`offline` 下架/维护<br><br>`restrictedAPI` API限制下单 |
| data[].offTime | string |  | 停盘时间，未配置则返回""<br><br>仅合约返回 |
| data[].limitOpenTime | string |  | 限制开仓时间，未配置则返回""；其它值表示symbol正在/计划维护，指定时间后禁止交易<br><br>仅合约返回 |
| data[].deliveryTime | string |  | 交割时间<br><br>仅交割合约返回 |
| data[].deliveryStartTime | string |  | 交割币对开始时间<br><br>仅交割合约返回 |
| data[].deliveryPeriod | string |  | 交割周期<br><br>`this_quarter` 当季<br><br>`next_quarter` 次季<br><br>仅交割合约返回 |
| data[].launchTime | string |  | 上线时间，Unix毫秒时间戳，表示交易对的上线时间 |
| data[].fundInterval | string |  | 资金费结算周期<br><br>`1` 每小时<br><br>`8` 每8小时<br><br>仅合约返回 |
| data[].minLeverage | string |  | 最小杠杆<br><br>仅合约返回 |
| data[].maxLeverage | string |  | 最大杠杆<br><br>仅合约/杠杆返回 |
| data[].maintainTime | string |  | 币对维护时间（状态处于维护/即将维护时会有值），未配置则返回""<br><br>仅合约返回 |
| data[].symbolType | string |  | 交易对类别(已废弃)<br><br>`crypto` 加密货币<br><br>`metal` 贵金属<br><br>`stock` 股票<br><br>`commodity` 大宗 |
| data[].fullName | string |  | 完整名称，包括交易对名称、企业名称、ETF名称等，可能带ADR/ST/QUANTO标识<br><br>例如symbol为`SKHYUSDT`，fullName为"SK Hylix ADR"<br><br>现货合约均有该字段 |
| data[].instrumentType | string |  | 交易产品类型<br><br>`metal` 贵金属<br><br>`energy` 能源<br><br>`stock` 股票<br><br>`etf` ETF<br><br>`crypto` 加密货币<br><br>现货合约均有该字段 |
| data[].marketRegion | string |  | 市场区域码<br><br>适用于传统金融相关的交易对<br><br>`US` 美国<br><br>`CN` 中国<br><br>`HK` 香港<br><br>`KR` 韩国<br><br>`JP` 日本<br><br>现货合约均有该字段 |
| data[].isin | string |  | 国际证券识别码（ISIN），用来唯一标识股票、债券、基金、权证等金融证券的国际标准化代码<br><br>格式为：前两位为国家/地区代码，中间九位为本地证券识别码，最后一位为校验码 |
| data[].maxMarketOrderQty | string |  | 单笔市价单最大下单数量，以基础币种计<br><br>仅合约返回 |
| data[].isIsolatedBaseBorrowable | string |  | 逐仓左币是否可以借<br><br>仅适用于杠杆交易 |
| data[].isIsolatedQuotedBorrowable | string |  | 逐仓右币是否可以借<br><br>仅适用于杠杆交易 |
| data[].warningRiskRatio | string |  | 预警风险率<br><br>仅适用于杠杆交易 |
| data[].liquidationRiskRatio | string |  | 强平风险率<br><br>仅适用于杠杆交易 |
| data[].maxCrossedLeverage | string |  | 全仓最大杠杆倍数<br><br>仅适用于杠杆交易 |
| data[].maxIsolatedLeverage | string |  | 逐仓最大杠杆倍数<br><br>仅适用于杠杆交易 |
| data[].userMinBorrow | string |  | 最小可借<br><br>仅适用杠杆交易 |
| data[].areaSymbol | string |  | 是否区域币对 `YES`/`NO`<br><br>仅适用于现货交易，只有为YES的币对才返回该参数 |
| data[].unrealizedProfitLimit | string |  | 浮盈限制<br><br>`yes` 限制：该币对在存在浮盈时限制加仓与提币<br><br>`no` 不限制 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770531248742,
  "data": [
    {
      "symbol": "BTCUSDT",
      "category": "SPOT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "isRwa": "NO",
      "isReality": "no",
      "buyLimitPriceRatio": "0.02",
      "sellLimitPriceRatio": "0.02",
      "minOrderQty": "0.000001",
      "maxOrderQty": "0",
      "pricePrecision": "2",
      "quantityPrecision": "6",
      "quotePrecision": "8",
      "minOrderAmount": "1",
      "maxSymbolOrderNum": "",
      "maxProductOrderNum": "400",
      "status": "online",
      "maintainTime": "",
      "maxPositionNum": "200",
      "symbolType": "crypto",
      "fullName": "",
      "instrumentType": "crypto",
      "marketRegion": "",
      "isin": "",
      "launchTime": "1532454360000",
      "unrealizedProfitLimit": "yes"
    }
  ]
}
```

## 获取RPI交易对列表

`GET /api/v3/market/rpi-symbols`

限频规则: 10次/秒/IP

查询支持RPI（零售价格优化）的交易对列表

Operation ID: `marketGetRpiSymbols`

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | 业务线<br><br>`spot` 现货<br><br>`usdt-futures` U本位合约<br><br>`coin-futures` 币本位合约<br><br>`usdc-futures` USDC合约 |
| data[].symbol | string |  | 支持RPI的交易对 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "category": "spot",
      "symbol": "BTCUSDT"
    },
    {
      "category": "usdt-futures",
      "symbol": "BTCUSDT"
    }
  ]
}
```

## 获取行情数据

`GET /api/v3/market/tickers`

限频规则: 20次/秒/IP

查询实时市场数据，包括最新成交价格、24小时最高/最低价格、成交量、买一、卖一和交易对的价格变化。

Operation ID: `marketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，例如：BTCUSDT |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称，例如：BTCUSDT |
| data[].category | string |  | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data[].lastPrice | string |  | 最新价 |
| data[].openPrice24h | string |  | 24小时前的市场价格 |
| data[].lowPrice24h | string |  | 最近24小时最低价 |
| data[].highPrice24h | string |  | 最近24小时最高价 |
| data[].ask1Price | string |  | 卖一价格 |
| data[].bid1Price | string |  | 买一价格 |
| data[].bid1Size | string |  | 买一数量 |
| data[].ask1Size | string |  | 卖一数量 |
| data[].price24hPcnt | string |  | 24小时价格涨跌幅 |
| data[].turnover24h | string |  | 24小时成交额 |
| data[].volume24h | string |  | 24小时成交量 |
| data[].indexPrice | string |  | 指数价格<br><br>仅适用于合约 |
| data[].markPrice | string |  | 标记价格<br><br>仅适用于合约 |
| data[].fundingRate | string |  | 当前资金费率<br><br>仅适用于合约 |
| data[].openInterest | string |  | 当前币对平台总持仓量<br><br>仅适用于合约 |
| data[].deliveryStartTime | string |  | 交割开始时间<br><br>仅适用于交割币对 |
| data[].deliveryTime | string |  | 交割时间<br><br>仅适用于交割币对 |
| data[].deliveryStatus | string |  | 交割状态（只有币对进入交割时才有值）<br><br>`delivery_config_period` 新上币对配置中<br><br>`delivery_normal` 交易中<br><br>`delivery_before` 交割前10分钟，禁止开仓<br><br>`delivery_period` 交割中，禁止开平仓、撤单<br><br>仅适用于交割币对 |
| data[].platformTurnover24h | string |  | 24小时平台成交额<br><br>仅rtoken有值 |
| data[].ts | string |  | 系统生成数据时的时间戳，Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1765444397411,
  "data": [
    {
      "category": "SPOT",
      "symbol": "BTCUSDT",
      "lastPrice": "90253.5",
      "openPrice24h": "92590.86",
      "highPrice24h": "94475.75",
      "lowPrice24h": "89394.71",
      "ask1Price": "90253.5",
      "bid1Price": "90253.49",
      "bid1Size": "2.368684",
      "ask1Size": "0.402938",
      "price24hPcnt": "-0.02524",
      "volume24h": "7386.014738",
      "turnover24h": "677732572.225658",
      "platformTurnover24h": "677732572.225658",
      "ts": "1765444395778"
    }
  ]
}
```

## 获取深度数据

`GET /api/v3/market/orderbook`

限频规则: 20次/秒/IP

查询订单簿深度数据

深度历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `marketGetOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称 |
| limit | query | string |  | 深度档位，默认值：5，最大：1000<br>默认: `5` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.a | array |  | 卖方深度，按价格升序排序。<br><br>每项：[价格, 数量] |
| data.b | array |  | 买方深度，按价格降序排序。<br><br>每项：[价格, 数量] |
| data.ts | string |  | 系统生成数据时的时间戳，Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969017897,
  "data": {
    "a": [
      [
        73000.0,
        0.007
      ],
      [
        74000.0,
        0.007
      ],
      [
        75000.0,
        0.007
      ],
      [
        75123,
        5.615
      ]
    ],
    "b": [
      [
        71213.8,
        1.836
      ],
      [
        71213.3,
        10
      ],
      [
        71212.8,
        10
      ]
    ],
    "ts": "1730969017964"
  }
}
```

## 获取RPI深度数据

`GET /api/v3/market/rpi-orderbook`

限频规则: 10次/秒/IP

查询RPI（零售价格优化）订单簿深度数据。该接口返回包含RPI和非RPI数量分别展示的完整深度数据。

Operation ID: `marketGetRpiOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| limit | query | string |  | 深度档位<br><br>`SPOT`：默认值5，最大1000<br><br>`USDT-FUTURES`、`COIN-FUTURES`、`USDC-FUTURES`：默认值5，最大1000<br>默认: `5` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.a | array |  | 卖方深度，按价格升序排序。<br><br>每项：[价格, 非RPI数量, RPI数量] |
| data.b | array |  | 买方深度，按价格降序排序。<br><br>每项：[价格, 非RPI数量, RPI数量] |
| data.ts | string |  | 系统生成数据时的时间戳，Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969017897,
  "data": {
    "a": [
      [
        3366.8,
        9,
        1
      ],
      [
        3367,
        0,
        1
      ],
      [
        3368,
        8,
        2
      ]
    ],
    "b": [
      [
        3366.1,
        7,
        1
      ],
      [
        3366,
        6,
        1
      ]
    ],
    "ts": "1730969017964"
  }
}
```

## 获取平台近期成交数据

`GET /api/v3/market/fills`

限频规则: 20次/秒/IP

查询平台近期公开成交数据

成交历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

该接口现已支持返回 Reality（rtoken）交易对的 Bitget 平台成交数据，此前不支持。

Operation ID: `marketGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| limit | query | string |  | 每页条目数，默认值为100，最大值为100<br>默认: `100` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].execId | string |  | 成交ID |
| data[].execLinkId | string |  | 成交关联ID |
| data[].price | string |  | 成交价格 |
| data[].size | string |  | 成交数量<br><br>币本位合约：单位为quote coin<br><br>其他：单位为base coin |
| data[].side | string |  | 交易方向<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data[].ts | string |  | 成交时间，Unix毫秒时间戳 |
| data[].isRPI | string |  | 是否为RPI类型成交<br><br>`yes` 是<br><br>`no` 否 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1690313813709,
  "data": [
    {
      "execId": "1",
      "execLinkId": "12345877111",
      "price": "29990.5",
      "size": "0.0166",
      "side": "sell",
      "ts": "1627116776464",
      "isRPI": "no"
    },
    {
      "execId": "2",
      "execLinkId": "12345877112",
      "price": "30007.0",
      "size": "0.0166",
      "side": "buy",
      "ts": "1627116600875",
      "isRPI": "yes"
    }
  ]
}
```

## K线数据

`GET /api/v3/market/candles`

限频规则: 20次/秒/IP

获取K线数据，该接口可查询指定交易对和粒度的最近1000条数据

K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Reality 股票（rtoken）symbol 说明：

- K线类型仅支持 `market`（市场成交价K线）。传入 `mark`、`index`、`premium` 时默认走 `market`，不报错。

- 仅支持 `1m`、`5m`、`15m`、`1H`、`4H`、`1D` 时间粒度，传入不支持的粒度将返回参数错误。

Operation ID: `marketGetCandles`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| interval | query | string | 是 | 时间粒度<br><br>`1m`,`3m`,`5m`,`15m`,`30m`,`1H`,`4H`,`6H`,`12H`,`1D` |
| startTime | query | string |  | 开始时间，即查询该时间之后的K线，Unix时间戳的毫秒数格式，如1672410780000 |
| endTime | query | string |  | 结束时间，即查询该时间之前的K线，Unix时间戳的毫秒数格式，如1672410781000 |
| type | query | string |  | K线类型<br><br>`market` 行情；`mark` 标记；`index` 指数；`premium` 溢价<br><br>默认 market<br>默认: `market` |
| limit | query | string |  | 每页条目数，默认值为1000，最大值为1000<br>默认: `1000` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | array |  | 每项：[时间戳, 开盘价, 最高价, 最低价, 收盘价, 交易币成交量(base coin), 计价币成交量(quote coin)] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865864944,
  "data": [
    [
      "1687708800000",
      "27176.93",
      "27177.43",
      "27166.93",
      "27177.43",
      "2990.08",
      "81246917.3294"
    ],
    [
      "1688313600000",
      "27177.43",
      "27177.43",
      "24000",
      "24001",
      "2989.1",
      "72450031.0448"
    ]
  ]
}
```

## 历史K线数据

`GET /api/v3/market/history-candles`

限频规则: 20次/秒/IP

可以获取90天以前的历史K线数据

注意：如果endTime超出某个K线周期边界（哪怕仅1ms），系统可能会按周期向上取整计算数量，返回结果会额外包含该周期的一根K线（即数据起点可能会提前一个周期）。

K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Reality 股票（rtoken）symbol 说明：

- K线类型仅支持 `market`（市场成交价K线）。传入 `mark`、`index`、`premium` 时默认走 `market`，不报错。

- 仅支持 `1m`、`5m`、`15m`、`1H`、`4H`、`1D` 时间粒度，传入不支持的粒度将返回参数错误。

Operation ID: `marketGetHistoryCandles`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易币对，例如：BTCUSDT |
| interval | query | string | 是 | 时间粒度<br><br>`1m`,`3m`,`5m`,`15m`,`30m`,`1H`,`4H`,`6H`,`12H`,`1D` |
| startTime | query | string |  | 开始时间，即查询该时间之后的K线，Unix时间戳的毫秒数格式，如1672410780000。请求在此开始时间之后的数据（最大时间查询范围为90天） |
| endTime | query | string |  | 结束时间，即查询该时间之前的K线，Unix时间戳的毫秒数格式，如1672410781000。请求在此结束时间之前的数据（最大时间查询范围为90天） |
| type | query | string |  | K线类型<br><br>`market` 行情；`mark` 标记；`index` 指数；`premium` 溢价<br><br>默认 market<br>默认: `market` |
| limit | query | string |  | 每页条目数，默认值为100，最大值为100<br>默认: `100` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | array |  | 每项：[时间戳, 开盘价, 最高价, 最低价, 收盘价, 交易币成交量(base coin), 计价币成交量(quote coin)] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865864944,
  "data": [
    [
      "1687708800000",
      "27176.93",
      "27177.43",
      "27166.93",
      "27177.43",
      "2990.08",
      "81246917.3294"
    ],
    [
      "1688313600000",
      "27177.43",
      "27177.43",
      "24000",
      "24001",
      "2989.1",
      "72450031.0448"
    ]
  ]
}
```

## 获取服务器时间

`GET /api/v3/market/time`

获取当前服务器时间。

- 限频规则: 20次/秒/IP

Operation ID: `marketGetServerTime`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.serverTime | string |  | 服务器时间，Unix **毫秒**时间戳，如 `1690196141868` |
| data.serverTimeMicros | string |  | 服务器时间，Unix **微秒**时间戳，如 `1690196141868000` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1690196141868,
  "data": {
    "serverTime": "1690196141868",
    "serverTimeMicros": "1690196141868000"
  }
}
```

## 获取币种信息

`GET /api/v3/market/coins`

获取币种信息，支持单个及全量查询。

- 限频规则: 20次/秒/IP

Operation ID: `marketGetCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如`BTC`<br><br>如不填写，默认返回全部币种信息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].transfer | string |  | 是否可以划转 |
| data[].chains | object[] |  | 支持的链列表 |
| data[].chains[].chain | string |  | 链名称 |
| data[].chains[].needTag | string |  | 是否需要tag |
| data[].chains[].withdrawable | string |  | 是否可提现 |
| data[].chains[].rechargeable | string |  | 是否可充值 |
| data[].chains[].withdrawFee | string |  | 提现手续费 |
| data[].chains[].extraWithdrawFee | string |  | 额外收取（链上转账销毁），如`0.1`表示`10%` |
| data[].chains[].depositConfirm | string |  | 充值确认块数 |
| data[].chains[].withdrawConfirm | string |  | 提现确认块数 |
| data[].chains[].minDepositAmount | string |  | 最小充值数 |
| data[].chains[].minWithdrawAmount | string |  | 最小提现数 |
| data[].chains[].browserUrl | string |  | 区块浏览器地址 |
| data[].chains[].contractAddress | string |  | 币种合约地址 |
| data[].chains[].withdrawStep | string |  | 提币步长<br><br>非`0`，代表提币数量需满足该步长的倍数；为`0`，代表没有步长倍数的限制 |
| data[].chains[].withdrawMinScale | string |  | 提币数量精度 |
| data[].chains[].congestion | string |  | 链网络拥堵情况<br><br>`normal`: 正常<br><br>`congested`: 拥堵 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    {
      "coin": "BTC",
      "transfer": "true",
      "chains": [
        {
          "chain": "BTC",
          "needTag": "false",
          "withdrawable": "true",
          "rechargeable": "true",
          "withdrawFee": "0.005",
          "extraWithdrawFee": "0",
          "depositConfirm": "1",
          "withdrawConfirm": "1",
          "minDepositAmount": "0.001",
          "minWithdrawAmount": "0.001",
          "browserUrl": "https://blockchair.com/bitcoin/testnet/transaction/",
          "contractAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
          "withdrawStep": "0",
          "withdrawMinScale": "8",
          "congestion": "normal"
        }
      ]
    }
  ]
}
```

## 获取公告

`GET /api/v3/public/annoucements`

查询公告信息。

公告子类型说明（公告子类型与公告类型相对应）：

- annType=`latest_news`
  - `announcements` 最新公告
  - `news` Bitget资讯
- annType=`coin_listings`
  - `spot`
  - `futures`
  - `margin`
  - `copy_trading`
- annType=`product_updates`
  - `spot`
  - `futures`
  - `margin`
  - `copy_trading`
- annType=`security`
  - `security_information`
- annType=`api_trading`
  - `api_announcement`
- annType=`symbol_delisting`
  - `trading_pair_delisting`
- annType=`maintenance_system_updates`
  - `asset_maintenance`
  - `system_updates`
  - `spot_maintenance`
  - `futures_maintenance`

- 限频规则: 20次/秒/IP

Operation ID: `publicGetAnnouncements`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| annType | query | string |  | 公告类型<br><br>`latest_news`最新活动<br><br>`coin_listings`新币上线<br><br>`product_updates`产品更新<br><br>`security`安全<br><br>`api_trading`API交易<br><br>`maintenance_system_updates`维护/系统升级<br><br>`symbol_delisting`下架资讯 |
| startTime | query | string |  | 查询的开始时间，Unix毫秒时间戳，例如1690196141868<br><br>按照公告展示时间查询 |
| endTime | query | string |  | 查询的结束时间，Unix毫秒时间戳，例如1690196141868<br><br>按照公告展示时间查询 |
| cursor | query | string |  | 游标ID<br><br>首次调用不需要，后续调用传上次响应中最后一个`annId` |
| limit | query | string |  | 每页条目数<br><br>默认10条，最大10条 |
| language | query | string | 是 | 语言类型<br><br>`zh_CN`中文<br><br>`en_US`英文<br><br>如果传入的语言类型不支持，则返回英文 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].annId | string |  | 公告ID |
| data[].annTitle | string |  | 公告标题 |
| data[].language | string |  | 语言类型 |
| data[].annUrl | string |  | 链接 |
| data[].annType | string |  | 公告类型<br><br>`latest_news`最新活动<br><br>`coin_listings`新币上线<br><br>`product_updates`产品更新<br><br>`security`安全<br><br>`api_trading`API交易<br><br>`maintenance_system_updates`维护/系统升级<br><br>`symbol_delisting`下架资讯 |
| data[].annSubType | string |  | 公告子类型 |
| data[].createdTime | string |  | 公告发布时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": [
    {
      "annId": "1",
      "annTitle": "test0629",
      "language": "zh_CN",
      "annUrl": "https://www.bitget.com/zh_CN/support/articles/23685",
      "annType": "maintenance_system_updates",
      "annSubType": "asset_maintenance",
      "createdTime": "1688008040000"
    }
  ]
}
```

## 获取未平仓合约持仓量(OI)

`GET /api/v3/market/open-interest`

限频规则: 20次/秒/IP

获取某交易对未平仓合约持仓量(按多空持仓总和计算)。

Operation ID: `derivativesGetOpenInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，例如：`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  |  |
| data.list[].symbol | string |  | 交易对名称，例如：`BTCUSDT` |
| data.list[].openInterest | string |  | 未平仓合约持仓量(基础币) |
| data.ts | string |  | 记录生成时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730969652387,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "openInterest": "2243.019"
      }
    ],
    "ts": "1730969652411"
  }
}
```

## 获取合约持仓量历史

`GET /api/v3/market/open-interest-history`

查询合约交易对的历史持仓量数据。

- 限频规则: 10次/秒/IP

Operation ID: `derivativesGetOpenInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string | 是 | 时间粒度<br><br>默认`5m`<br><br>支持`5m`、`15m`、`30m`、`1h`、`2h`、`4h`、`6h`、`12h`、`1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 持仓量数据集合 |
| data.list[].symbol | string |  | 币对名称 |
| data.list[].openInterest | string |  | 未平仓合约持仓量<br><br>单位为交易币 |
| data.list[].oneSideOpenInterest | string |  | 未平仓合约持仓量（单边）<br><br>单位为交易币 |
| data.list[].openInterestValue | string |  | 未平仓合约持仓价值<br><br>单位为计价币<br><br>`openInterestValue = openInterest * markPrice` |
| data.list[].oneSideOpenInterestValue | string |  | 未平仓合约持仓价值（单边）<br><br>单位为计价币 |
| data.list[].timestamp | string |  | 该周期的结束时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1756616400000.0,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "openInterest": "2243.019",
        "oneSideOpenInterest": "1121.5095",
        "openInterestValue": "193486281.47",
        "oneSideOpenInterestValue": "96743140.735",
        "timestamp": "1756616400000"
      }
    ]
  }
}
```

## 获取历史爆仓数据

`GET /api/v3/market/liquidations`

限频规则: 5次/秒/IP

查询历史爆仓订单数据，仅返回最近三天的数据，数据会有一些延迟。

Operation ID: `derivativesGetLiquidations`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，如`BTCUSDT` |
| limit | query | string |  | 每页条目数<br><br>默认值为100，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>传入上次查询响应中的`cursor`用于分页查询 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  |  |
| data.list[].symbol | string |  | 交易对名称，如`BTCUSDT` |
| data.list[].side | string |  | 仓位方向<br><br>`buy` 多仓强平<br><br>`sell` 空仓强平 |
| data.list[].price | string |  | 强平价格 |
| data.list[].amount | string |  | 强平数量(基础币) |
| data.list[].ts | string |  | 强平时间<br><br>Unix毫秒时间戳 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "side": "buy",
        "price": "29990.5",
        "amount": "0.5",
        "ts": "1690313813709"
      }
    ],
    "cursor": "1690313813709"
  },
  "msg": "success",
  "requestTime": 1690313813709
}
```

## 实时资金费率

`GET /api/v3/market/current-fund-rate`

限频规则: 20次/秒/IP

获取合约实时资金费率接口。

Operation ID: `derivativesGetCurrentFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 业务线<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，例如：BTCUSDT<br><br> `category`和`symbol`不可同时为空 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称，例如`BTCUSDT` |
| data[].fundingRate | string |  | [当前资金费率](https://www.bitget.com/zh-CN/trade-info/funding_rate)。小数形式，0.000088即代表0.0088% |
| data[].fundingRateInterval | string |  | 资金费率结算周期,单位为小时<br><br>数字1代表1小时，2代表2小时，以此类推 |
| data[].nextUpdate | string |  | 资金费率下次更新时间<br><br>Unix毫秒时间戳 |
| data[].minFundingRate | string |  | 资金费率下限<br><br>以小数形式返回，例如：0.025为2.5% |
| data[].maxFundingRate | string |  | 资金费率上限<br><br>以小数形式返回，例如：0.025为2.5% |
| data[].lastFundingRate | string |  | 上次资金费率<br/>小数形式返回，如 0.000088 表示 0.0088 |
| data[].nextFundingRate | string |  | 下次资金费率<br/>小数形式返回，如 0.000088 表示 0.0088 |
| data[].baseInterestRate | string |  | 基础利率<br/>小数形式返回，如 0.0001 表示 0.01% |
| data[].impactMarginNotional | string |  | 冲击保证金影响额<br/>单位：计价币 |
| data[].cashDividend | string |  | 每股现金派息，单位为USDT，只在有现金派息行为的时候有值<br><br>RWA股票合约向符合条件的持有人支付的现金分红，具体请参考[这里](https://www.bitget.com/zh-CN/support/articles/12560603884677) |
| data[].cashDividendNextUpdate | string |  | 现金派息下次更新时间，只在有现金派息行为的时候有值<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743059269376,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000071",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003",
      "lastFundingRate": "0.000071",
      "nextFundingRate": "0.000088",
      "baseInterestRate": "0.0001",
      "impactMarginNotional": "20000",
      "cashDividend": null,
      "cashDividendNextUpdate": null
    }
  ]
}
```

## 历史资金费率

`GET /api/v3/market/history-fund-rate`

限频规则: 20次/秒/IP

获取合约的历史资金费率(最近90天)。资金结算时间会因不同交易对而不同。

Operation ID: `derivativesGetHistoryFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| cursor | query | string |  | 分页游标，用于翻页<br><br>最大支持100，默认为1 |
| limit | query | string |  | 每页条目数<br><br>最大支持100，默认20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  |  |
| data.resultList[].symbol | string |  | 交易对名称，例如`BTCUSDT` |
| data.resultList[].fundingRate | string |  | 资金费率<br><br>小数形式，例如：0.000074代表0.0074% |
| data.resultList[].fundingRateTimestamp | string |  | 结算时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1754908278922,
  "data": {
    "resultList": [
      {
        "symbol": "BTCUSDT",
        "fundingRate": "0.0001",
        "fundingRateTimestamp": "1754899200000"
      },
      {
        "symbol": "BTCUSDT",
        "fundingRate": "0.0001",
        "fundingRateTimestamp": "1754870400000"
      }
    ]
  }
}
```

## 获取指数价格成分

`GET /api/v3/market/index-components`

限频规则：10次/秒/IP

获取指数价格成分。

Operation ID: `derivativesGetIndexComponents`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对名称 |
| data.componentList | object[] |  |  |
| data.componentList[].exchange | string |  | 交易所 |
| data.componentList[].spotPair | string |  | 现货交易对名称 |
| data.componentList[].equivalentPrice | string |  | 等值价格 |
| data.componentList[].weight | string |  | 计算权重<br><br>小数形式，如0.5代表50% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767159256214,
  "data": {
    "symbol": "BTCUSDT",
    "componentList": [
      {
        "exchange": "BITGET_FUTURE",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88432.1",
        "weight": "0.4696"
      },
      {
        "exchange": "GATEIO",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88467",
        "weight": "0.164"
      },
      {
        "exchange": "BINANCE",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88456.65",
        "weight": "0.1434"
      },
      {
        "exchange": "MEXC",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88457.1",
        "weight": "0.0992"
      },
      {
        "exchange": "BITGET",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88469.77",
        "weight": "0.0768"
      },
      {
        "exchange": "OKX",
        "spotPair": "BTC/USDT",
        "equivalentPrice": "88463",
        "weight": "0.0468"
      }
    ]
  }
}
```

## 获取储备金证明

`GET /api/v3/market/proof-of-reserves`

限频规则: 20次/秒/IP

获取储备金证明接口

Operation ID: `publicConfigGetProofOfReserves`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.merkleRootHash | string |  | 默克尔树根哈希 |
| data.totalReserveRatio | string |  | 总储备金率<br>百分比形式返回 |
| data.list | object[] |  | 列表 |
| data.list[].coin | string |  | 币种名称 |
| data.list[].platformAssets | string |  | 平台资金<br>精度为两位小数，单位为币种coin |
| data.list[].userAssets | string |  | 用户资金<br>精度为两位小数，单位为币种coin |
| data.list[].reserveRatio | string |  | 储备金率<br>百分比形式返回 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753845058586,
  "data": {
    "merkleRootHash": "e0dff99bbe2c2dcb",
    "totalReserveRatio": "175%",
    "list": [
      {
        "coin": "BTC",
        "userAssets": "9530.89",
        "platformAssets": "29679.59",
        "reserveRatio": "311%"
      },
      {
        "coin": "USDT",
        "userAssets": "1948633388.98",
        "platformAssets": "1985576297.93",
        "reserveRatio": "102%"
      },
      {
        "coin": "ETH",
        "userAssets": "195465.81",
        "platformAssets": "294561.45",
        "reserveRatio": "151%"
      },
      {
        "coin": "USDC",
        "userAssets": "58830275.64",
        "platformAssets": "157216065.76",
        "reserveRatio": "267%"
      }
    ]
  }
}
```

## 获取做市分数权重

`GET /api/v3/market/score-weights`

限频规则：5次/秒/IP

用于做市商查询各交易对的做市分数权重。

Operation ID: `publicConfigGetScoreWeights`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 业务线类型<br>`SPOT`现货<br>`FUTURES`合约<br>如不填,则默认返回全部业务线 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | 业务线类型<br>`SPOT`现货<br>`FUTURES`合约 |
| data[].label | string |  | 标签 |
| data[].symbol | string |  | 交易对名称<br>如 ETHUSDT |
| data[].requiredSpread | string |  | 达标挂单价差率<br>如0.0005代表0.05% |
| data[].minMakerVolume | string |  | 累计最小挂单额<br>正整数,如 5000 10000<br>单位为USDT |
| data[].weight | string |  | 权重<br>小数形式 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1772524004421,
  "data": [
    {
      "category": "SPOT",
      "label": "usdt",
      "symbol": "LUMIAUSDT",
      "requiredSpread": "0.0005",
      "minMakerVolume": "500",
      "weight": "50"
    }
  ]
}
```

## 获取机构费率分组

`GET /api/v3/market/fee-group`

限频规则：5次/秒/IP

用于查询系统预设的机构费率梯度及分组参数。

Operation ID: `publicConfigGetFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线类型<br>`SPOT`现货<br>`FUTURES`合约 |
| group | query | string |  | 分组类型<br>现货<br>`GROUP_A` 核心主流<br>`GROUP_B` 潜力放量<br>`DEFAULT` 默认<br>合约<br>`GROUP_A` 核心主流<br>`GROUP_B` 潜力放量<br>`GROUP_C` 冷启动<br>`DEFAULT` 默认<br>如不传，则默认返回全部分组的费率配置 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].category | string |  | 业务线类型<br>`SPOT`现货<br>`FUTURES`合约 |
| data[].group | string |  | 分组类型<br>现货<br>`GROUP_A` 核心主流<br>`GROUP_B` 潜力放量<br>`DEFAULT` 默认<br>合约<br>`GROUP_A` 核心主流<br>`GROUP_B` 潜力放量<br>`GROUP_C` 冷启动<br>`DEFAULT` 默认 |
| data[].labelList | object[] |  | 标签数组 |
| data[].labelList[].weight | string |  | 权重<br>精度为两位小数 |
| data[].labelList[].label | string |  | 标签 |
| data[].labelList[].symbols | string[] |  | 标签内包含的交易对数组<br>如["ETHUSDT","SOLUSDT","BTCUSDT"] |
| data[].tierList | object[] |  | 费率梯度列表 |
| data[].tierList[].level | string |  | 用户等级<br>MM1/MM2/MM3/MM4/MM5/PRO1/PRO2/PRO3/PRO4/PRO5/PRO6 |
| data[].tierList[].makerFeeRate | string |  | 挂单手续费率<br>小数形式，如0.0001代表0.01% |
| data[].tierList[].takerFeeRate | string |  | 吃单手续费率<br>小数形式，如0.0001代表0.01%<br>仅适用于 PRO 等级（PRO1~PRO6），MM 等级无此字段 |
| data[].tierList[].rpiMakerFeeRate | string |  | RPI挂单手续费率<br>小数形式，如`0.0001`代表0.01%<br>面向做市商用户且仅适用于开放RPI的交易对 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1772462728068,
  "data": [
    {
      "category": "SPOT",
      "group": "GROUP_A",
      "labelList": [
        {
          "weight": "1.00",
          "label": "core_mainstream",
          "symbols": [
            "DOGEUSDT",
            "XRPUSDT",
            "BTCUSDT",
            "ETHUSDT",
            "SOLUSDT",
            "BGBUSDT"
          ]
        }
      ],
      "tierList": [
        {
          "level": "MM1",
          "makerFeeRate": "-0.0001"
        },
        {
          "level": "MM2",
          "makerFeeRate": "-0.00008"
        },
        {
          "level": "MM3",
          "makerFeeRate": "-0.00004"
        },
        {
          "level": "MM4",
          "makerFeeRate": "-0.00001"
        },
        {
          "level": "MM5",
          "makerFeeRate": "0"
        },
        {
          "level": "PRO1",
          "makerFeeRate": "0.00025",
          "takerFeeRate": "0.0004"
        },
        {
          "level": "PRO2",
          "makerFeeRate": "0.0002",
          "takerFeeRate": "0.000375"
        },
        {
          "level": "PRO3",
          "makerFeeRate": "0.000175",
          "takerFeeRate": "0.000313"
        },
        {
          "level": "PRO4",
          "makerFeeRate": "0.00015",
          "takerFeeRate": "0.000288"
        },
        {
          "level": "PRO5",
          "makerFeeRate": "0.0001",
          "takerFeeRate": "0.000238"
        },
        {
          "level": "PRO6",
          "makerFeeRate": "0.0001",
          "takerFeeRate": "0.000219"
        }
      ]
    }
  ]
}
```

## 获取现金派息记录

`GET /api/v3/market/cash-dividend-records`

限频规则: 10次/秒/IP

获取RWA股票合约的现金派息记录。

Operation ID: `publicConfigGetCashDividendRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| type | query | string | 是 | 派息类型<br>`pending` 将派息<br>`paid` 已派息 |
| cursor | query | string |  | 分页游标<br>用于翻页，最大支持100，默认为1<br>默认: `1` |
| limit | query | string |  | 每页条目数<br>最大支持100，默认20<br>默认: `20` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].exDividendDate | string |  | 除息日 |
| data[].cashDividendPerShare | string |  | 每股派息<br>单位为USDT |
| data[].cashDividendTimestamp | string |  | 现金派息结算时间<br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1749484800000.0,
  "data": [
    {
      "symbol": "AAPLXRPUSDT",
      "exDividendDate": "2026-06-09",
      "cashDividendPerShare": "0.25",
      "cashDividendTimestamp": "1749484800000"
    }
  ]
}
```

## 获取拆合股记录

`GET /api/v3/market/split-records`

获取RWA股票拆股/合股记录。
- 限频规则: 5次/秒/IP

Operation ID: `publicConfigGetSplitRecords`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称，如KORUUSDT |
| data[].type | string |  | 拆合股类型<br>`split` 拆股<br>`reverse_split` 合股 |
| data[].status | string |  | 拆合股状态<br>`pending` 将拆合股<br>`ongoing` 拆合股中<br>`completed` 已拆合股 |
| data[].adjustmentRatio | string |  | 调整比率<br>拆股时该值大于1，如`20`表示1拆20<br>合股时该值小于1，如`0.1`表示10合1 |
| data[].exDividendDate | string |  | 除权日<br>格式：yyyy-MM-dd |
| data[].exDividendDateTimezone | string |  | 除权日所属时区，固定返回`ET` |
| data[].tradingHaltStartTime | string |  | 停盘开始时间<br>Unix毫秒时间戳 |
| data[].tradingHaltEndTime | string |  | 停盘结束时间<br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1749484800000.0,
  "data": [
    {
      "symbol": "KORUUSDT",
      "type": "split",
      "status": "pending",
      "adjustmentRatio": "20",
      "exDividendDate": "2026-06-09",
      "exDividendDateTimezone": "ET",
      "tradingHaltStartTime": "1749484800000",
      "tradingHaltEndTime": "1749488400000"
    }
  ]
}
```

## 获取风险准备金(天)

`GET /api/v3/market/risk-reserve`

限频规则: 20次/秒/IP

查询风险准备金(最近30天记录)

Operation ID: `tradingRiskRulesGetRiskReserve`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| marginCoin | query | string |  | 保证金币种，当 category 为 COIN-FUTURES 币本位合约时必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalBalance | string |  | 风险准备金总余额(已废弃) |
| data.coin | string |  | 风险准备金结算币种 |
| data.riskReserveRecords | object[] |  | 风险准备金记录 |
| data.riskReserveRecords[].type | string |  | 风险准备金记录类型 (已废弃) |
| data.riskReserveRecords[].amount | string |  | 风险准备金变动数量 |
| data.riskReserveRecords[].balance | string |  | 风险准备金余额 |
| data.riskReserveRecords[].ts | string |  | 风险准备金变动时间<br><br>Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "totalBalance": "",
    "coin": "USDT",
    "riskReserveRecords": [
      {
        "type": "",
        "amount": "9.8470265278770000",
        "balance": "95815.6773460800020000",
        "ts": "1753718400000"
      },
      {
        "type": "",
        "amount": "0.4328615782800000",
        "balance": "95805.8303195521250000",
        "ts": "1753632000000"
      }
    ]
  }
}
```

## 获取风险准备金(小时)

`GET /api/v3/market/risk-reserve-hour`

限频规则: 20次/秒/IP

查询最近30小时风险准备金数据(小时级别)

Operation ID: `tradingRiskRulesGetRiskReserveHour`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易对名称，例如：BTCUSDT |
| marginCoin | query | string |  | 保证金币种，当 category 为 COIN-FUTURES 币本位合约时必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 风险准备金结算币种 |
| data.riskReserveRecords | object[] |  | 风险准备金记录 |
| data.riskReserveRecords[].amount | string |  | 风险准备金变动数量 |
| data.riskReserveRecords[].balance | string |  | 风险准备金余额 |
| data.riskReserveRecords[].ts | string |  | 风险准备金变动时间<br><br>Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "coin": "USDT",
    "riskReserveRecords": [
      {
        "amount": "9.8470265278770000",
        "balance": "95815.6773460800020000",
        "ts": "1753718400000"
      },
      {
        "amount": "0.4328615782800000",
        "balance": "95805.8303195521250000",
        "ts": "1753632000000"
      }
    ]
  }
}
```

## 获取当前全部风险准备金

`GET /api/v3/market/risk-reserve-all`

限频规则: 3次/秒/IP

获取当前全部风险准备金

独立保险池数据每 1 分钟 更新一次，聚合保险池数据每 1 小时 更新一次。

Operation ID: `tradingRiskRulesGetRiskReserveAll`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 保险池列表 |
| data.list[].symbols | string[] |  | 交易对<br><br>聚合保险池会返回多个交易对<br><br>独立保险池则仅返回一个交易对 |
| data.list[].coin | string |  | 保险池币种名称 |
| data.list[].balance | string |  | 保险池币种余额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753793743942,
  "data": {
    "list": [
      {
        "symbols": [
          "BTCUSDT"
        ],
        "coin": "USDT",
        "balance": "95815.6773460800020000"
      }
    ]
  }
}
```

## 获取杠杆借币信息

`GET /api/v3/market/margin-loans`

限频规则: 20次/秒/IP

获取杠杆借币的利率数据

Operation ID: `tradingRiskRulesGetMarginLoans`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称，例如：BTC |
| level | query | string |  | 用户等级<br/>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br/>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br/>默认值为`vip0` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.dailyInterest | string |  | 日利率 |
| data.annualInterest | string |  | 年利率 |
| data.limit | string |  | 限额 |
| data.masterSubLimit | string |  | 母子账户限额 |
| data.platformRemaingQuota | string |  | 平台剩余额度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730912814587,
  "data": {
    "dailyInterest": "0.1",
    "annualInterest": "0.00416667",
    "limit": "3000",
    "masterSubLimit": "1000",
    "platformRemaingQuota": "500000"
  }
}
```

## 获取杠杆借币信息（全部）

`GET /api/v3/market/margin-loans-all`

限频规则: 20次/秒/IP

查询全部币种的杠杆借币信息。不传 `coin` 时返回全部支持币种的信息。

Operation ID: `tradingRiskRulesGetMarginLoansAll`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如：`BTC`<br/>不传则返回全部支持币种的信息 |
| level | query | string |  | 用户等级<br/>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br/>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br/>默认：`vip0` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].dailyInterest | string |  | 日利率 |
| data[].annualInterest | string |  | 年利率 |
| data[].limit | string |  | 借币限额 |
| data[].masterSubLimit | string |  | 母子账户限额 |
| data[].platformRemaingQuota | string |  | 平台剩余额度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1792646640213,
  "data": [
    {
      "coin": "rWELL",
      "dailyInterest": "0.0000085680",
      "annualInterest": "0.0031273200",
      "limit": "0",
      "masterSubLimit": "0",
      "platformRemaingQuota": "0"
    }
  ]
}
```

## 获取借币利率历史

`GET /api/v3/market/interest-rate-history`

查询指定币种、指定 VIP 档位的杠杆借币历史利率序列，用于回测借贷成本、核算历史持仓利息、测算 VIP 升级的利息节省。

数据粒度固定 1 小时，保留最近 1 个月。

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读权限

Operation ID: `tradingRiskRulesGetInterestRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种，如`USDT`<br><br>仅支持已开放杠杆借贷的币种，未开放币种返回错误 |
| startTime | query | string |  | 开始时间，Unix毫秒时间戳<br><br>仅支持最近 1 个月内的数据 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>与`startTime`间隔不超过30天<br><br>不传时间参数时返回当前时间往前的`limit`条 |
| level | query | string |  | 用户等级<br><br>`vip0`/`vip1`/`vip2`/`vip3`/`vip4`/`vip5`/`vip6`/`vip7`<br><br>`pro1`/`pro2`/`pro3`/`pro4`/`pro5`/`pro6`<br><br>默认值为`vip0` |
| limit | query | string |  | 每页条目数<br><br>默认`10`，最大`500` |
| cursor | query | string |  | 分页游标<br><br>取上一页响应的`cursor` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cursor | string |  | 下一页游标<br><br>为空表示无更多数据 |
| data.list | object[] |  | 利率历史数据集合 |
| data.list[].coin | string |  | 币种 |
| data.list[].dailyInterestRate | string |  | 日利率<br><br>小数形式，如`0.01`代表`1%` |
| data.list[].annualInterestRate | string |  | 年利率<br><br>小数形式，如`0.01`代表`1%` |
| data.list[].ts | string |  | 利率生效时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1756616400000.0,
  "data": {
    "cursor": "1756594800000",
    "list": [
      {
        "coin": "USDT",
        "dailyInterestRate": "0.00007704",
        "annualInterestRate": "0.0281",
        "ts": "1756616400000"
      },
      {
        "coin": "USDT",
        "dailyInterestRate": "0.00007728",
        "annualInterestRate": "0.0282",
        "ts": "1756609200000"
      }
    ]
  }
}
```

## 获取仓位档位信息

`GET /api/v3/market/position-tier`

限频规则: 20次/秒/IP

获取仓位档位梯度信息

Operation ID: `tradingRiskRulesGetPositionTier`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`MARGIN` 杠杆<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称，例如：BTCUSDT，当业务线为合约时，该字段必填 |
| coin | query | string |  | 币种名称，例如：BTC，当业务线为杠杆时，该字段必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tier | string |  | 档位 |
| data[].leverage | string |  | 有效杠杆倍数 |
| data[].minTierValue | string |  | 当前档位最小价值<br><br>仅在合约档位梯度信息返回 |
| data[].maxTierValue | string |  | 当前档位最大价值<br><br>仅在合约档位梯度信息返回 |
| data[].mmr | string |  | 维持保证金率<br><br>持仓档位对应的数值。当仓位的保证金率小于维持保证金率时，将会触发强制减仓或爆仓 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1731146663643,
  "data": [
    {
      "tier": "1",
      "minTierValue": "0",
      "maxTierValue": "100000",
      "leverage": "125",
      "mmr": "0.004"
    }
  ]
}
```

## 获取合约OI限仓信息

`GET /api/v3/market/oi-limit`

限频规则：10次/秒/IP

获取合约OI限仓信息。

Operation ID: `tradingRiskRulesGetOiLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易币对 |
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 产品名称 |
| data[].notionalValue | string |  | 单用户持仓名义价值 |
| data[].totalNotionalValue | string |  | 子母账户持仓名义价值 |
| data[].singlePositionRatio | string |  | 单 UID 合约持仓占比<br/>小数形式返回，如 `0.1` 代表 10% |
| data[].totalPositionRatio | string |  | 子母账户合约持仓占比<br/>小数形式返回，如 `0.1` 代表 10% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741665165571,
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "1000000",
      "totalNotionalValue": "5000000",
      "singlePositionRatio": "0.1",
      "totalPositionRatio": "0.2"
    },
    {
      "symbol": "ETHUSDT",
      "notionalValue": "1000000",
      "totalNotionalValue": "5000000",
      "singlePositionRatio": "0.1",
      "totalPositionRatio": "0.2"
    }
  ]
}
```

## 获取币种折扣率

`GET /api/v3/market/discount-rate`

限频规则: 20次/秒/IP

获取不同档位的币种折扣率信息

Operation ID: `tradingRiskRulesGetDiscountRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称，例如：BTC |
| data[].list | object[] |  | 档位列表 |
| data[].list[].tierStartValue | string |  | 档位起始价值<br><br>例如：[0,10000 U): tierStartValue=0<br><br>[10000 U,20000 U): tierStartValue=10000<br><br>[20000 U,∞): tierStartValue=20000 |
| data[].list[].discountRate | string |  | 折扣率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730911874605,
  "data": [
    {
      "coin": "ETH",
      "list": [
        {
          "tierStartValue": "0",
          "discountRate": "0.99"
        },
        {
          "tierStartValue": "40000",
          "discountRate": "0.98"
        }
      ]
    }
  ]
}
```

## 获取现货大户净流入信息

`GET /api/v3/market/spot-whale-flow`

限频规则: 1次/秒/IP

获取现货大户净流入信息。

Operation ID: `tradingStatsGetSpotWhaleNetFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].volume | string |  | 大户买卖净流入量 |
| data[].date | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "volume": "-1.1",
      "date": "1713942000000"
    }
  ]
}
```

## 获取现货资金流向信息

`GET /api/v3/market/spot-fund-flow`

限频规则: 1次/秒/IP

获取现货资金流向信息。

Operation ID: `tradingStatsGetSpotFundFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如 BTCUSDT |
| period | query | string |  | 查询周期：<br><br>15m（默认）, 30m, 1h, 2h, 4h, 1d<br>默认: `15m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.whaleBuyVolume | string |  | 大户买入量 |
| data.dolphinBuyVolume | string |  | 中户买入量 |
| data.fishBuyVolume | string |  | 散户买入量 |
| data.whaleSellVolume | string |  | 大户卖出量 |
| data.dolphinSellVolume | string |  | 中户卖出量 |
| data.fishSellVolume | string |  | 散户卖出量 |
| data.whaleBuyRatio | string |  | 大户买入占比 |
| data.dolphinBuyRatio | string |  | 中户买入占比 |
| data.fishBuyRatio | string |  | 散户买入占比 |
| data.whaleSellRatio | string |  | 大户卖出占比 |
| data.dolphinSellRatio | string |  | 中户卖出占比 |
| data.fishSellRatio | string |  | 散户卖出占比 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "whaleBuyVolume": "50.901579",
    "dolphinBuyVolume": "1.506897",
    "fishBuyVolume": "0.529853",
    "whaleSellVolume": "50.635982",
    "dolphinSellVolume": "1.429034",
    "fishSellVolume": "0.344032",
    "whaleBuyRatio": "50.901579",
    "dolphinBuyRatio": "1.506897",
    "fishBuyRatio": "0.529853",
    "whaleSellRatio": "50.635982",
    "dolphinSellRatio": "1.429034",
    "fishSellRatio": "0.344032"
  }
}
```

## 获取现货24小时资金净流入信息

`GET /api/v3/market/spot-net-flow`

限频规则: 1次/秒/IP

获取现货24小时资金净流入信息。

Operation ID: `tradingStatsGetSpotNetFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].netFlow | string |  | 大户资金净流入 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    }
  ]
}
```

## 获取杠杆多空对比信息

`GET /api/v3/market/margin-long-short`

限频规则: 1次/秒/IP

获取全仓及逐仓杠杆账户中特定币种的多空持仓比例。

Operation ID: `tradingStatsGetMarginLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>24h，支持：24h, 30d<br>默认: `24h` |
| coin | query | string |  | 基础币或计价币，默认：基础币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longShortRatio | string |  | 多空比 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longShortRatio": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## 获取杠杆借贷存量增速信息

`GET /api/v3/market/margin-loan-growth`

限频规则: 1次/秒/IP

获取全仓及逐仓杠杆账户中特定币种借贷资金的增长速率。

Operation ID: `tradingStatsGetMarginLoanGrowth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>24h，支持：24h, 30d<br>默认: `24h` |
| coin | query | string |  | 基础币或计价币，默认：基础币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].growthRate | string |  | 增长速率 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "growthRate": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## 获取杠杆逐仓借贷比信息

`GET /api/v3/market/margin-isolated-borrow`

限频规则: 1次/秒/IP

获取逐仓杠杆账户中基础币借入量与计价币借入量（均折算为USDT）的比例。

Operation ID: `tradingStatsGetMarginIsolatedBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>24h，支持：24h, 30d<br>默认: `24h` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].borrowRate | string |  | 借贷比 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "borrowRate": "-0.96",
      "ts": "1713942000000"
    }
  ]
}
```

## 获取合约主动买卖量信息

`GET /api/v3/market/futures-active-buy-sell`

限频规则: 1次/秒/IP

获取合约主动买卖量信息。

Operation ID: `tradingStatsGetFuturesActiveBuySell`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>5m，支持：5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].buyVolume | string |  | 主动买入量 |
| data[].sellVolume | string |  | 主动卖出量 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "buyVolume": "0.01",
      "sellVolume": "0.12",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取合约多空比信息

`GET /api/v3/market/futures-long-short`

限频规则: 1次/秒/IP

获取合约多空比信息。

Operation ID: `tradingStatsGetFuturesLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>5m，支持：5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1Dutc<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longRatio | string |  | 多仓比例 |
| data[].shortRatio | string |  | 空仓比例 |
| data[].longShortRatio | string |  | 多空比 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longRatio": "0.01",
      "shortRatio": "0.12",
      "longShortRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取合约大户持仓量多空比信息

`GET /api/v3/market/futures-position-long-short`

限频规则: 1次/秒/IP

获取合约大户持仓量多空比信息。

Operation ID: `tradingStatsGetFuturesPositionLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>5m，支持：5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longPositionRatio | string |  | 多仓持仓量比例 |
| data[].shortPositionRatio | string |  | 空仓持仓量比例 |
| data[].longShortPositionRatio | string |  | 多空持仓量比 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longPositionRatio": "0.01",
      "shortPositionRatio": "0.12",
      "longShortPositionRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取合约大户账户多空比信息

`GET /api/v3/market/futures-account-long-short`

限频规则: 1次/秒/IP

获取合约大户账户多空比信息。

Operation ID: `tradingStatsGetFuturesAccountLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| period | query | string |  | 默认：<br><br>5m，支持：5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h, 1d<br>默认: `5m` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longAccountRatio | string |  | 多仓账户比例 |
| data[].shortAccountRatio | string |  | 空仓账户比例 |
| data[].longShortAccountRatio | string |  | 多空账户比 |
| data[].ts | string |  | 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "longAccountRatio": "0.01",
      "shortAccountRatio": "0.12",
      "longShortAccountRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```