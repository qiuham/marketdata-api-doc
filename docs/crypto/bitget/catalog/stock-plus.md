---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/stock-plus
api_type: REST
updated_at: 2026-11-18 19:01:33.596471
---

# Stock+

Stock+ US stock & ETF and option quotes, order/fill management, and assets APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/stockplus/market/option-quote` — Check Option Real-time Quote
- `GET /api/v3/stockplus/market/option-chain-info` — Check Option Chain
- `GET /api/v3/stockplus/market/option-expiry-date` — Check Option Expiry Date List
- `GET /api/v3/stockplus/market/option-volume` — Check Option Volume
- `GET /api/v3/stockplus/market/static` — Check Basic Information
- `GET /api/v3/stockplus/market/candlestick` — Check Candlestick
- `GET /api/v3/stockplus/market/history-candlestick` — Check History Candlestick
- `GET /api/v3/stockplus/market/depth` — Check Order Book
- `GET /api/v3/stockplus/market/intraday` — Check Intraday Data
- `GET /api/v3/stockplus/market/quote` — Check Real-time Quote
- `GET /api/v3/stockplus/market/trade` — Check Trade Detail
- `POST /api/v3/stockplus/trade/place-order` — Place Order
- `POST /api/v3/stockplus/trade/modify-order` — Modify Order
- `POST /api/v3/stockplus/trade/cancel-order` — Cancel Order
- `GET /api/v3/stockplus/trade/today-orders` — Check Today Orders
- `GET /api/v3/stockplus/trade/history-orders` — Check History Orders
- `GET /api/v3/stockplus/trade/order-detail` — Check Order Detail
- `GET /api/v3/stockplus/trade/max-purchase` — Estimate Max Purchase Quantity
- `GET /api/v3/stockplus/trade/today-executions` — Check Today Executions
- `GET /api/v3/stockplus/trade/history-executions` — Check History Executions
- `POST /api/v3/stockplus/asset/transfer` — Transfer
- `GET /api/v3/stockplus/asset/transfer-records` — Check Transfer Records
- `GET /api/v3/stockplus/asset/account` — Check Account
- `GET /api/v3/stockplus/asset/cash-flow` — Check Cash Flow
- `GET /api/v3/stockplus/asset/stock-position` — Check Stock Position

## Check Option Real-time Quote

`GET /api/v3/stockplus/market/option-quote`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

This interface is used to query the real-time market data of US stock option contracts in batch, including option-specific fields (implied volatility, open interest, strike price, etc.).

Note:

- Accessing option real-time quotes via the Open API requires claiming the "OPRA US Stock Option Market Data (API)" market data card first.

- OPRA option market data (API) is only available for whitelisted users. Please contact your BD to apply.

- New customers who have activated the Stock+ options trading feature, please tap "US Stocks" in the top-right corner of the APP, go to My > My Cards > Activate Now, complete the "Non-Professional User Assessment Questionnaire," and then claim the OPRA real-time market data card.

Operation ID: `stockPlusOptionsQuotesGetOptionQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol list, obtained through the option chain interface. Use `ticker.region` format, e.g. `AAPL220429P162500.US`<br><br>**Check rules:** The maximum number of symbols per request is `500` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.secuQuote | object[] |  | List of option security market data |
| data.secuQuote[].symbol | string |  | Symbol |
| data.secuQuote[].lastDone | string |  | Latest price |
| data.secuQuote[].prevClose | string |  | Previous close price |
| data.secuQuote[].open | string |  | Open price |
| data.secuQuote[].high | string |  | Highest price |
| data.secuQuote[].low | string |  | Lowest price |
| data.secuQuote[].timestamp | string |  | Timestamp of the latest trade |
| data.secuQuote[].volume | string |  | Volume |
| data.secuQuote[].turnover | string |  | Turnover |
| data.secuQuote[].tradeStatus | string |  | Trading status<br><br>`0` - Normal<br><br>`1` - Suspended<br><br>`2` - Delisted<br><br>`3` - Circuit breaker<br><br>`4` - Pending listing<br><br>`5` - Code change<br><br>`6` - Pre-market<br><br>`7` - Rebase suspension<br><br>`8` - Expired (derivatives)<br><br>`9` - Warrants pending listing<br><br>`10` - Terminated |
| data.secuQuote[].impliedVolatility | string |  | Implied volatility |
| data.secuQuote[].openInterest | string |  | Open interest |
| data.secuQuote[].expiryDate | string |  | Expiry date, format:<br><br>`YYMMDD` |
| data.secuQuote[].strikePrice | string |  | Strike price |
| data.secuQuote[].contractMultipier | string |  | Contract multiplier |
| data.secuQuote[].contractType | string |  | Contract type. `A` - American, `U` - European |
| data.secuQuote[].contractSize | string |  | Contract size |
| data.secuQuote[].direction | string |  | Direction. `P` - Put, `C` - Call |
| data.secuQuote[].historicalVolatility | string |  | Historical volatility of the underlying stock |
| data.secuQuote[].underlyingSymbol | string |  | Underlying stock symbol |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "secuQuote": [
      {
        "symbol": "AAPL220429P162500.US",
        "lastDone": "7.78",
        "prevClose": "4.13",
        "open": "4.43",
        "high": "7.80",
        "low": "4.43",
        "timestamp": "1651003200000",
        "volume": "3082",
        "turnover": "1813434.00",
        "tradeStatus": "1",
        "impliedVolatility": "0.592",
        "openInterest": "11463",
        "expiryDate": "20220429",
        "strikePrice": "162.50",
        "contractMultipier": "100",
        "contractType": "A",
        "contractSize": "100",
        "direction": "P",
        "historicalVolatility": "0.2750",
        "underlyingSymbol": "AAPL.US"
      }
    ]
  }
}
```

## Check Option Chain

`GET /api/v3/stockplus/market/option-chain-info`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

This interface is used to query all option contracts under a specific underlying symbol, grouped by expiry date.

Operation ID: `stockPlusOptionsQuotesGetOptionChainInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| expiryDate | query | string | 是 | Option expiry date, format:<br><br>`YYYYMMDD`, e.g. `20220429`. Obtained through the Expiry Date List interface |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strikePriceInfo | object[] |  | List of option strike prices for the expiry date |
| data.strikePriceInfo[].price | string |  | Strike price |
| data.strikePriceInfo[].callSymbol | string |  | CALL option symbol |
| data.strikePriceInfo[].putSymbol | string |  | PUT option symbol |
| data.strikePriceInfo[].standard | boolean |  | Whether it is a standard option |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strikePriceInfo": [
      {
        "price": "160.00",
        "callSymbol": "AAPL220429C160000.US",
        "putSymbol": "AAPL220429P160000.US",
        "standard": true
      }
    ]
  }
}
```

## Check Option Expiry Date List

`GET /api/v3/stockplus/market/option-expiry-date`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

This interface is used to query the option chain expiry date list for a specific underlying symbol.

Operation ID: `stockPlusOptionsQuotesGetOptionExpiryDate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.expiryDate | string[] |  | List of option chain expiry dates, format:<br><br>`YYMMDD` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "expiryDate": [
      "20220429",
      "20220506",
      "20220513"
    ]
  }
}
```

## Check Option Volume

`GET /api/v3/stockplus/market/option-volume`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

This interface is used to query today's call/put option volume snapshot.

Operation ID: `stockPlusOptionsQuotesGetOptionVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | US stock symbol, e.g. `AAPL.US`, `TSLA.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.c | string |  | Total call volume for today |
| data.p | string |  | Total put volume for today |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "c": "284512",
    "p": "195830"
  }
}
```

## Check Basic Information

`GET /api/v3/stockplus/market/static`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query the basic information of securities.

Operation ID: `stockPlusStockQuotesGetStaticInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol list, using `ticker.region` format, e.g. `AAPL.US`<br><br>**Check rules:** The maximum number of symbols per request is `500` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List of security basic data |
| data.list[].symbol | string |  | Symbol |
| data.list[].nameCn | string |  | Chinese simplified name |
| data.list[].nameEn | string |  | English name |
| data.list[].exchange | string |  | Exchange |
| data.list[].currency | string |  | Trading currency. `CNY`, `USD` |
| data.list[].lotSize | integer |  | Lot size |
| data.list[].totalShares | string |  | Total shares |
| data.list[].circulatingShares | string |  | Circulating shares |
| data.list[].eps | string |  | Earnings per share |
| data.list[].epsTtm | string |  | Earnings per share (TTM) |
| data.list[].bps | string |  | Book value per share |
| data.list[].dividendYield | string |  | Dividend yield |
| data.list[].stockDerivatives | string[] |  | Derivative market types. `Option` - Options |
| data.list[].board | string |  | Board |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "AAPL.US",
        "nameCn": "苹果",
        "nameEn": "Apple Inc.",
        "exchange": "NASD",
        "currency": "USD",
        "lotSize": 1,
        "totalShares": 16319441000.0,
        "circulatingShares": 16302661350,
        "eps": 5.669,
        "epsTtm": 6.0771,
        "bps": 4.40197,
        "dividendYield": 0.85,
        "stockDerivatives": [
          "Option"
        ],
        "board": "USMain"
      }
    ]
  }
}
```

## Check Candlestick

`GET /api/v3/stockplus/market/candlestick`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query the latest candlestick data of a security. Note: this interface only returns up to the latest 1000 candles; use the History Candlestick interface for longer historical data.

Operation ID: `stockPlusStockQuotesGetCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| period | query | string | 是 | K-line period<br><br>`Min_1` - 1 minute<br><br>`Min_2` - 2 minutes<br><br>`Min_3` - 3 minutes<br><br>`Min_5` - 5 minutes<br><br>`Min_10` - 10 minutes<br><br>`Min_15` - 15 minutes<br><br>`Min_20` - 20 minutes<br><br>`Min_30` - 30 minutes<br><br>`Min_45` - 45 minutes<br><br>`Min_60` - 60 minutes<br><br>`Min_120` - 120 minutes<br><br>`Min_180` - 180 minutes<br><br>`Min_240` - 240 minutes<br><br>`Day` - Daily<br><br>`Week` - Weekly<br><br>`Month` - Monthly<br><br>`Quarter` - Quarterly<br><br>`Year` - Yearly |
| count | query | integer | 是 | Data count, maximum `1000` |
| adjustType | query | string | 是 | Adjust type<br><br>`NoAdjust` - None<br><br>`ForwardAdjust` - Forward adjust |
| tradeSessions | query | string |  | Trade session<br><br>`Intraday` - Regular<br><br>`Pre` - Pre-market<br><br>`Post` - After-hours<br><br>`Overnight` - Overnight |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Candlestick data |
| data.list[].close | string |  | Close price |
| data.list[].open | string |  | Open price |
| data.list[].low | string |  | Low price |
| data.list[].high | string |  | High price |
| data.list[].volume | string |  | Volume |
| data.list[].turnover | string |  | Turnover |
| data.list[].timestamp | string |  | Timestamp |
| data.list[].tradeSession | string |  | Trade session<br><br>`Intraday` - Regular<br><br>`Pre` - Pre-market<br><br>`Post` - After-hours<br><br>`Overnight` - Overnight |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "close": "175.460",
        "open": "176.750",
        "low": "175.180",
        "high": "177.840",
        "volume": "54321000",
        "turnover": "9587654321",
        "timestamp": "1697414400",
        "tradeSession": "Intraday"
      },
      {
        "close": "176.810",
        "open": "175.580",
        "low": "174.910",
        "high": "177.110",
        "volume": "48765000",
        "turnover": "8601234567",
        "timestamp": "1697500800",
        "tradeSession": "Intraday"
      },
      {
        "close": "177.150",
        "open": "177.060",
        "low": "176.450",
        "high": "178.420",
        "volume": "42210000",
        "turnover": "7498765432",
        "timestamp": "1697587200",
        "tradeSession": "Intraday"
      }
    ]
  }
}
```

## Check History Candlestick

`GET /api/v3/stockplus/market/history-candlestick`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query historical candlestick data of a security.

Operation ID: `stockPlusStockQuotesGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| period | query | string | 是 | K-line period<br><br>`Min_1` - 1 minute<br><br>`Min_2` - 2 minutes<br><br>`Min_3` - 3 minutes<br><br>`Min_5` - 5 minutes<br><br>`Min_10` - 10 minutes<br><br>`Min_15` - 15 minutes<br><br>`Min_20` - 20 minutes<br><br>`Min_30` - 30 minutes<br><br>`Min_45` - 45 minutes<br><br>`Min_60` - 60 minutes<br><br>`Min_120` - 120 minutes<br><br>`Min_180` - 180 minutes<br><br>`Min_240` - 240 minutes<br><br>`Day` - Daily<br><br>`Week` - Weekly<br><br>`Month` - Monthly<br><br>`Quarter` - Quarterly<br><br>`Year` - Yearly |
| count | query | integer | 是 | Data count, maximum `1000` |
| adjustType | query | string | 是 | Adjust type<br><br>`NoAdjust` - None<br><br>`ForwardAdjust` - Forward adjust |
| forward | query | boolean |  | Query direction. Default `false`<br><br>`false` - Backwards<br><br>`true` - Forwards |
| time | query | string |  | Query timestamp, Unix seconds. Defaults to current time |
| tradeSessions | query | string |  | Trade session<br><br>`Intraday` - Regular<br><br>`Pre` - Pre-market<br><br>`Post` - After-hours<br><br>`Overnight` - Overnight (included in US LV1, US stocks only) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Candlestick data |
| data.list[].close | string |  | Close price |
| data.list[].open | string |  | Open price |
| data.list[].low | string |  | Low price |
| data.list[].high | string |  | High price |
| data.list[].volume | string |  | Volume |
| data.list[].turnover | string |  | Turnover |
| data.list[].timestamp | string |  | Timestamp |
| data.list[].tradeSession | string |  | Trade session<br><br>`Intraday` - Regular<br><br>`Pre` - Pre-market<br><br>`Post` - After-hours<br><br>`Overnight` - Overnight |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "close": "175.460",
        "open": "176.750",
        "low": "175.180",
        "high": "177.840",
        "volume": "54321000",
        "turnover": "9587654321",
        "timestamp": "1697414400",
        "tradeSession": "Intraday"
      },
      {
        "close": "176.810",
        "open": "175.580",
        "low": "174.910",
        "high": "177.110",
        "volume": "48765000",
        "turnover": "8601234567",
        "timestamp": "1697500800",
        "tradeSession": "Intraday"
      },
      {
        "close": "177.150",
        "open": "177.060",
        "low": "176.450",
        "high": "178.420",
        "volume": "42210000",
        "turnover": "7498765432",
        "timestamp": "1697587200",
        "tradeSession": "Intraday"
      }
    ]
  }
}
```

## Check Order Book

`GET /api/v3/stockplus/market/depth`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query the order book data of a security.

Operation ID: `stockPlusStockQuotesGetDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | object[] |  | Ask orders |
| data.asks[].position | integer |  | Position |
| data.asks[].price | string |  | Price |
| data.asks[].volume | string |  | Order quantity |
| data.asks[].orderNum | integer |  | Number of orders |
| data.bids | object[] |  | Bid orders |
| data.bids[].position | integer |  | Position |
| data.bids[].price | string |  | Price |
| data.bids[].volume | string |  | Order quantity |
| data.bids[].orderNum | integer |  | Number of orders |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "asks": [
      {
        "position": 1,
        "price": "195.900",
        "volume": "200",
        "orderNum": 5
      },
      {
        "position": 2,
        "price": "195.910",
        "volume": "500",
        "orderNum": 8
      },
      {
        "position": 3,
        "price": "195.920",
        "volume": "300",
        "orderNum": 3
      },
      {
        "position": 4,
        "price": "195.930",
        "volume": "800",
        "orderNum": 12
      },
      {
        "position": 5,
        "price": "195.940",
        "volume": "150",
        "orderNum": 2
      }
    ],
    "bids": [
      {
        "position": 1,
        "price": "195.880",
        "volume": "350",
        "orderNum": 6
      },
      {
        "position": 2,
        "price": "195.870",
        "volume": "600",
        "orderNum": 9
      },
      {
        "position": 3,
        "price": "195.860",
        "volume": "450",
        "orderNum": 7
      },
      {
        "position": 4,
        "price": "195.850",
        "volume": "200",
        "orderNum": 4
      },
      {
        "position": 5,
        "price": "195.840",
        "volume": "700",
        "orderNum": 11
      }
    ]
  }
}
```

## Check Intraday Data

`GET /api/v3/stockplus/market/intraday`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query the intraday data of a security.

Operation ID: `stockPlusStockQuotesGetIntraday`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Intraday data |
| data.list[].price | string |  | Closing price of the current minute |
| data.list[].timestamp | string |  | Start time of the current minute (ISO 8601) |
| data.list[].volume | string |  | Volume |
| data.list[].turnover | string |  | Turnover |
| data.list[].avgPrice | string |  | Average price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "price": 195.89,
        "timestamp": "2024-10-16T09:30:00Z",
        "volume": 150000.0,
        "turnover": 29383500,
        "avgPrice": 195.88
      },
      {
        "price": 195.92,
        "timestamp": "2024-10-16T09:31:00Z",
        "volume": 180000.0,
        "turnover": 35265600,
        "avgPrice": 195.91
      },
      {
        "price": 195.85,
        "timestamp": "2024-10-16T09:32:00Z",
        "volume": 120000.0,
        "turnover": 23502000.0,
        "avgPrice": 195.87
      },
      {
        "price": 195.88,
        "timestamp": "2024-10-16T09:33:00Z",
        "volume": 200000.0,
        "turnover": 39176000.0,
        "avgPrice": 195.88
      },
      {
        "price": 195.9,
        "timestamp": "2024-10-16T09:34:00Z",
        "volume": 160000.0,
        "turnover": 31344000.0,
        "avgPrice": 195.89
      }
    ]
  }
}
```

## Check Real-time Quote

`GET /api/v3/stockplus/market/quote`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query real-time market data for securities (supports all security types).

Operation ID: `stockPlusStockQuotesGetQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol list, using `ticker.region` format, e.g. `AAPL.US`<br><br>**Check rules:** The maximum number of symbols per request is `500` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List of security real-time market data |
| data.list[].symbol | string |  | Symbol |
| data.list[].lastDone | string |  | Latest price |
| data.list[].prevClose | string |  | Previous close |
| data.list[].open | string |  | Open price |
| data.list[].high | string |  | Highest price |
| data.list[].low | string |  | Lowest price |
| data.list[].timestamp | string |  | Timestamp of the latest trade (ISO 8601) |
| data.list[].volume | string |  | Volume |
| data.list[].turnover | string |  | Turnover |
| data.list[].tradeStatus | string |  | Trading status<br><br>`Normal` - Normal<br><br>`Suspended` - Suspended<br><br>`Delisted` - Delisted<br><br>`CircuitBreaker` - Circuit breaker<br><br>`PendingListing` - Pending listing<br><br>`CodeChange` - Code change<br><br>`PreMarket` - Pre-market<br><br>`RebaseSuspension` - Rebase suspension<br><br>`Expired` - Expired (derivatives)<br><br>`Terminated` - Terminated |
| data.list[].preMarketQuote | object |  | US pre-market trading data |
| data.list[].preMarketQuote.lastDone | string |  | Latest price |
| data.list[].preMarketQuote.timestamp | string |  | Timestamp of the latest trade (ISO 8601) |
| data.list[].preMarketQuote.volume | string |  | Volume |
| data.list[].preMarketQuote.turnover | string |  | Turnover |
| data.list[].preMarketQuote.high | string |  | Highest price |
| data.list[].preMarketQuote.low | string |  | Lowest price |
| data.list[].preMarketQuote.prevClose | string |  | Previous trading session close |
| data.list[].postMarketQuote | object |  | US post-market trading data |
| data.list[].postMarketQuote.lastDone | string |  | Latest price |
| data.list[].postMarketQuote.timestamp | string |  | Timestamp of the latest trade (ISO 8601) |
| data.list[].postMarketQuote.volume | string |  | Volume |
| data.list[].postMarketQuote.turnover | string |  | Turnover |
| data.list[].postMarketQuote.high | string |  | Highest price |
| data.list[].postMarketQuote.low | string |  | Lowest price |
| data.list[].postMarketQuote.prevClose | string |  | Previous trading session close |
| data.list[].overnightQuote | ['object', 'null'] |  | US overnight trading data (can be `null`) |
| data.list[].overnightQuote.lastDone | string |  | Latest price |
| data.list[].overnightQuote.timestamp | string |  | Timestamp of the latest trade (ISO 8601) |
| data.list[].overnightQuote.volume | string |  | Volume |
| data.list[].overnightQuote.turnover | string |  | Turnover |
| data.list[].overnightQuote.high | string |  | Highest price |
| data.list[].overnightQuote.low | string |  | Lowest price |
| data.list[].overnightQuote.prevClose | string |  | Previous trading session close |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "AAPL.US",
        "lastDone": 195.89,
        "prevClose": 192.53,
        "open": 193.41,
        "high": 195.93,
        "low": 192.05,
        "timestamp": "2024-10-16T20:00:00Z",
        "volume": 53502311,
        "turnover": 10409656210,
        "tradeStatus": "Normal",
        "preMarketQuote": {
          "lastDone": 193.5,
          "timestamp": "2024-10-17T09:00:00Z",
          "volume": 1250000.0,
          "turnover": 241875000.0,
          "high": 194,
          "low": 192.8,
          "prevClose": 192.53
        },
        "postMarketQuote": {
          "lastDone": 196.1,
          "timestamp": "2024-10-16T23:59:59Z",
          "volume": 980000.0,
          "turnover": 192178000.0,
          "high": 196.5,
          "low": 195.7,
          "prevClose": 195.89
        },
        "overnightQuote": null
      }
    ]
  }
}
```

## Check Trade Detail

`GET /api/v3/stockplus/market/trade`

Rate limit: 10 times/1s (UID), with up to 5 concurrent requests

Permission: Stock+ market data (read)

This interface is used to query the trade detail data of a security.

**Trade Type**

US trade types:

`` ` `` (space) - Regular sale

`B` - Average price trade

`E` - Automatic execution

`H` - Price variation trade

`I` - Odd lot trade

Operation ID: `stockPlusStockQuotesGetTradeDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| count | query | integer | 是 | Number of trade records to request. Maximum: `1000` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Trade detail data |
| data[].price | string |  | Price |
| data[].volume | string |  | Volume |
| data[].timestamp | string |  | Trade time (ISO 8601) |
| data[].tradeType | string |  | Trade type. See the Trade Type section in the description |
| data[].direction | string |  | Trade direction<br><br>`Up` - Up<br><br>`Down` - Down<br><br>`Neutral` - Neutral |
| data[].tradeSession | string |  | Trade session<br><br>`Intraday` - Regular<br><br>`Pre` - Pre-market<br><br>`Post` - After-hours<br><br>`Overnight` - Overnight |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "price": 195.89,
      "volume": 100,
      "timestamp": "2024-10-16T09:30:00Z",
      "tradeType": "I",
      "direction": "Up",
      "tradeSession": "Intraday"
    },
    {
      "price": 195.88,
      "volume": 200,
      "timestamp": "2024-10-16T09:29:55Z",
      "tradeType": "I",
      "direction": "Neutral",
      "tradeSession": "Intraday"
    },
    {
      "price": 195.89,
      "volume": 150,
      "timestamp": "2024-10-16T09:29:50Z",
      "tradeType": "I",
      "direction": "Down",
      "tradeSession": "Intraday"
    }
  ]
}
```

## Place Order

`POST /api/v3/stockplus/trade/place-order`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read and write)

This interface is used to place stock/option orders.

Operation ID: `stockPlusOrdersPlaceOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| orderType | query | string | 是 | Order type<br><br>`LO` Limit Order<br><br>`MO` Market Order<br><br>`LIT` Limit If Touched<br><br>`MIT` Market If Touched<br><br>`TSLPAMT` Trailing Stop Limit Order (Trailing Amount)<br><br>`TSLPPCT` Trailing Stop Limit Order (Trailing Percentage) |
| side | query | string | 是 | Order side<br><br>`Buy` - Buy<br><br>`Sell` - Sell |
| submittedQuantity | query | string | 是 | Order quantity, e.g. `100` |
| timeInForce | query | string | 是 | Order validity type<br><br>`Day` - Valid for the day<br><br>`GoodTilCanceled` - Valid until cancelled<br><br>`GoodTilDate` - Valid until expiry |
| submittedPrice | query | string |  | Order price, e.g. `388.5`<br><br>Required for `LO` / `LIT` orders |
| triggerPrice | query | string |  | Trigger price, e.g. `388.5`<br><br>Required for `LIT` / `MIT` orders |
| limitOffset | query | string |  | Specified spread, e.g. `1.2` means spread of 1.2 USD (for US stocks)<br><br>Required for `TSLPAMT` / `TSLPPCT` orders when `limitDepthLevel` is 0 |
| trailingAmount | query | string |  | Trailing amount<br><br>Required for `TSLPAMT` orders |
| trailingPercent | query | string |  | Trailing percentage, in percentage points, e.g. `2.5` means `2.5%`<br><br>Required for `TSLPPCT` orders |
| expireDate | query | string |  | Long-term order expiry date, format:<br><br>`YYYY-MM-DD`, e.g. `2022-12-05`<br><br>Required when `timeInForce` is `GoodTilDate` |
| outsideRth | query | string |  | Whether to allow trading outside regular trading hours. Required for US stocks<br><br>`RTHOnly` - Do not allow pre/post market<br><br>`AnyTime` - Allow pre/post market<br><br>`Overnight` - Overnight trading |
| limitDepthLevel | query | number |  | Specified bid/ask level, range -5 to 5. Negative is bid level (e.g. -1 is best bid), positive is ask level (e.g. 1 is best ask). When 0, `limitOffset` takes effect<br><br>Valid for `TSLPAMT` / `TSLPPCT` orders |
| triggerCount | query | number |  | Trigger count, range 0~3. The order is triggered after the condition is met this many times within 1 minute<br><br>Valid for `LIT` / `MIT` / `TSLPAMT` / `TSLPPCT` orders |
| monitorPrice | query | string |  | Monitor price, the order starts monitoring only when the price reaches this level<br><br>Valid for `TSLPAMT` / `TSLPPCT` orders |
| remark | query | string |  | Remark (max 64 characters) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | System order ID |
| data.clientOid | string |  | Client customized order ID. Returns empty string if not passed |
| data.symbol | string |  | Option contract symbol |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "myOrder001",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## Modify Order

`POST /api/v3/stockplus/trade/modify-order`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read and write)

This interface is used to modify the price/quantity of unfilled or partially filled orders, with cancel & replace semantics.

Operation ID: `stockPlusOrdersModifyOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |
| quantity | query | string | 是 | Modified quantity, e.g. `200` |
| price | query | string |  | Modified price, e.g. `388.5`<br><br>Required for `LO` / `LIT` orders |
| triggerPrice | query | string |  | Trigger price, e.g. `388.5`<br><br>Required for `LIT` / `MIT` orders |
| limitOffset | query | string |  | Specified spread<br><br>Required for `TSLPAMT` / `TSLPPCT` orders when `limitDepthLevel` is 0 |
| trailingAmount | query | string |  | Trailing amount<br><br>Required for `TSLPAMT` orders |
| trailingPercent | query | string |  | Trailing percentage<br><br>Required for `TSLPPCT` orders |
| limitDepthLevel | query | number |  | Specified bid/ask level. Required for `TSLPAMT` / `TSLPPCT` orders |
| triggerCount | query | number |  | Trigger count. Required for `LIT` / `MIT` / `TSLPAMT` / `TSLPPCT` orders |
| monitorPrice | query | string |  | Monitor price. Required for `TSLPAMT` / `TSLPPCT` orders |
| remark | query | string |  | Remark (max 64 characters) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | System order ID after modification |
| data.clientOid | string |  | Client customized order ID. Returns empty string if not passed |
| data.symbol | string |  | Option contract symbol |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## Cancel Order

`POST /api/v3/stockplus/trade/cancel-order`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read and write)

This interface is used to cancel unfilled or partially filled orders.

Operation ID: `stockPlusOrdersCancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Option contract symbol |
| orderId | query | string |  | System order ID. At least one of orderId and clientOid must be passed; orderId takes priority when both are passed |
| clientOid | query | string |  | Client customized order ID. At least one of orderId and clientOid must be passed |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | System order ID |
| data.clientOid | string |  | Client customized order ID. Returns empty string if not passed |
| data.symbol | string |  | Option contract symbol |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## Check Today Orders

`GET /api/v3/stockplus/trade/today-orders`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read only)

This interface is used to query today's orders and order details.

Operation ID: `stockPlusOrdersGetTodayOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| status | query | string |  | Order status, e.g. `status=Filled&status=New`<br><br>`NotReported` - Not reported<br><br>`ReplacedNotReported` - Replaced not reported<br><br>`ProtectedNotReported` - Protected not reported<br><br>`VarietiesNotReported` - Varieties not reported<br><br>`Filled` - Fully filled<br><br>`WaitToNew` - Waiting for new<br><br>`New` - New<br><br>`WaitToReplace` - Waiting for replace<br><br>`PendingReplace` - Pending replace<br><br>`Replaced` - Replaced<br><br>`PartialFilled` - Partially filled<br><br>`WaitToCancel` - Waiting for cancel<br><br>`PendingCancel` - Pending cancel<br><br>`Rejected` - Rejected<br><br>`Canceled` - Canceled<br><br>`Expired` - Expired<br><br>`PartialWithdrawal` - Partial withdrawal |
| side | query | string |  | Order side<br><br>`Buy` - Buy<br><br>`Sell` - Sell |
| market | query | string |  | Market<br><br>`US` - US stocks |
| orderId | query | string |  | Order ID for specific order query, e.g. `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orders | object[] |  | Order information |
| data.orders[].orderId | string |  | Order ID |
| data.orders[].status | string |  | Order status. See status enumeration above<br><br>`NotReported` - Not reported<br><br>`ReplacedNotReported` - Replaced not reported<br><br>`ProtectedNotReported` - Protected not reported<br><br>`VarietiesNotReported` - Varieties not reported<br><br>`Filled` - Fully filled<br><br>`WaitToNew` - Waiting for new<br><br>`New` - New<br><br>`WaitToReplace` - Waiting for replace<br><br>`PendingReplace` - Pending replace<br><br>`Replaced` - Replaced<br><br>`PartialFilled` - Partially filled<br><br>`WaitToCancel` - Waiting for cancel<br><br>`PendingCancel` - Pending cancel<br><br>`Rejected` - Rejected<br><br>`Canceled` - Canceled<br><br>`Expired` - Expired<br><br>`PartialWithdrawal` - Partial withdrawal |
| data.orders[].stockName | string |  | Stock name |
| data.orders[].quantity | string |  | Order quantity |
| data.orders[].executedQuantity | string |  | Executed quantity. `0` for unfilled orders |
| data.orders[].price | string |  | Order price. `null` when market conditional order not yet triggered |
| data.orders[].executedPrice | string |  | Executed price. `0` for unfilled orders |
| data.orders[].submittedAt | string |  | Order submission time (ISO 8601) |
| data.orders[].side | string |  | Order side. `Buy` - Buy, `Sell` - Sell |
| data.orders[].symbol | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| data.orders[].orderType | string |  | Order type<br><br>`LO` Limit Order<br><br>`MO` Market Order<br><br>`LIT` Limit If Touched<br><br>`MIT` Market If Touched<br><br>`TSLPAMT` Trailing Stop Limit Order (Trailing Amount)<br><br>`TSLPPCT` Trailing Stop Limit Order (Trailing Percentage) |
| data.orders[].lastDone | string |  | Latest traded price. `0` for unfilled orders |
| data.orders[].triggerPrice | string |  | Trigger price for `LIT`/`MIT` orders. `null` for non-conditional orders |
| data.orders[].msg | string |  | Rejection reason or remark. Empty string by default |
| data.orders[].tag | string |  | Order tag<br><br>`Normal` - Normal order<br><br>`GTC` - GTC order |
| data.orders[].timeInForce | string |  | Order validity type<br><br>`Day` - Valid for the day<br><br>`GoodTilCanceled` - Valid until cancelled<br><br>`GoodTilDate` - Valid until expiry |
| data.orders[].expireDate | string |  | Long-term order expiry date, format:<br><br>`YYYY-MM-DD`. `null` for non-GoodTilDate orders |
| data.orders[].updatedAt | string |  | Last update time (ISO 8601). `null` if never updated |
| data.orders[].triggerAt | string |  | Conditional order trigger time (ISO 8601). `null` if not triggered |
| data.orders[].trailingAmount | string |  | `TSLPAMT` order trailing amount. `null` for non-TSLPAMT orders |
| data.orders[].trailingPercent | string |  | `TSLPPCT` order trailing percentage. `null` for non-TSLPPCT orders |
| data.orders[].limitOffset | string |  | `TSLPAMT`/`TSLPPCT` order spread. `null` for non-TSLP orders |
| data.orders[].triggerStatus | string |  | Conditional order trigger status. `null` for non-conditional orders<br><br>`NOT_USED` - Not active<br><br>`DEACTIVE` - Deactivated<br><br>`ACTIVE` - Active<br><br>`RELEASED` - Triggered |
| data.orders[].currency | string |  | Settlement currency |
| data.orders[].outsideRth | string |  | Allow pre/post market trading. `UnknownOutsideRth` for non-US orders<br><br>`RTHOnly` - Do not allow<br><br>`AnyTime` - Allow<br><br>`Overnight` - Overnight |
| data.orders[].remark | string |  | Remark |
| data.orders[].limitDepthLevel | number |  | Specified bid/ask level |
| data.orders[].triggerCount | number |  | Trigger count |
| data.orders[].monitorPrice | string |  | Monitor price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orders": [
      {
        "orderId": "701276261045858304",
        "status": "Rejected",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 0,
        "price": 150,
        "executedPrice": null,
        "submittedAt": "2024-12-16T12:07:12Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T12:07:12Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "RTHOnly",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      }
    ]
  }
}
```

## Check History Orders

`GET /api/v3/stockplus/trade/history-orders`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read only)

This interface is used to query historical orders.

Operation ID: `stockPlusOrdersGetHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| status | query | string |  | Order status, e.g. `status=Filled&status=New`<br><br>`NotReported` - Not reported<br><br>`ReplacedNotReported` - Replaced not reported<br><br>`ProtectedNotReported` - Protected not reported<br><br>`VarietiesNotReported` - Varieties not reported<br><br>`Filled` - Fully filled<br><br>`WaitToNew` - Waiting for new<br><br>`New` - New<br><br>`WaitToReplace` - Waiting for replace<br><br>`PendingReplace` - Pending replace<br><br>`Replaced` - Replaced<br><br>`PartialFilled` - Partially filled<br><br>`WaitToCancel` - Waiting for cancel<br><br>`PendingCancel` - Pending cancel<br><br>`Rejected` - Rejected<br><br>`Canceled` - Canceled<br><br>`Expired` - Expired<br><br>`PartialWithdrawal` - Partial withdrawal |
| side | query | string |  | Order side. `Buy` - Buy, `Sell` - Sell |
| market | query | string |  | Market. `US` - US stocks |
| startAt | query | number |  | Start time, timestamp in seconds, e.g. `1650410999`. Defaults to 90 days before end time or current time |
| endAt | query | number |  | End time, timestamp in seconds, e.g. `1650410999`. Defaults to 90 days after start time or current time |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasMore | boolean |  | Whether there is more data. Max 1000 orders per query; hasMore is true when results exceed 1000 |
| data.orders | object[] |  | Order information |
| data.orders[].orderId | string |  | Order ID |
| data.orders[].status | string |  | Order status. See status enumeration above<br><br>`NotReported` - Not reported<br><br>`ReplacedNotReported` - Replaced not reported<br><br>`ProtectedNotReported` - Protected not reported<br><br>`VarietiesNotReported` - Varieties not reported<br><br>`Filled` - Fully filled<br><br>`WaitToNew` - Waiting for new<br><br>`New` - New<br><br>`WaitToReplace` - Waiting for replace<br><br>`PendingReplace` - Pending replace<br><br>`Replaced` - Replaced<br><br>`PartialFilled` - Partially filled<br><br>`WaitToCancel` - Waiting for cancel<br><br>`PendingCancel` - Pending cancel<br><br>`Rejected` - Rejected<br><br>`Canceled` - Canceled<br><br>`Expired` - Expired<br><br>`PartialWithdrawal` - Partial withdrawal |
| data.orders[].stockName | string |  | Stock name |
| data.orders[].quantity | string |  | Order quantity |
| data.orders[].executedQuantity | string |  | Executed quantity. `0` for unfilled orders |
| data.orders[].price | string |  | Order price. `null` when market conditional order not yet triggered |
| data.orders[].executedPrice | string |  | Executed price. `0` for unfilled orders |
| data.orders[].submittedAt | string |  | Order submission time (ISO 8601) |
| data.orders[].side | string |  | Order side. `Buy` - Buy, `Sell` - Sell |
| data.orders[].symbol | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| data.orders[].orderType | string |  | Order type<br><br>`LO` Limit Order<br><br>`MO` Market Order<br><br>`LIT` Limit If Touched<br><br>`MIT` Market If Touched<br><br>`TSLPAMT` Trailing Stop Limit Order (Trailing Amount)<br><br>`TSLPPCT` Trailing Stop Limit Order (Trailing Percentage) |
| data.orders[].lastDone | string |  | Latest traded price. `0` for unfilled orders |
| data.orders[].triggerPrice | string |  | Trigger price for `LIT`/`MIT` orders. `null` for non-conditional orders |
| data.orders[].msg | string |  | Rejection reason or remark. Empty string by default |
| data.orders[].tag | string |  | Order tag<br><br>`Normal` - Normal order<br><br>`GTC` - GTC order |
| data.orders[].timeInForce | string |  | Order validity type<br><br>`Day` - Valid for the day<br><br>`GoodTilCanceled` - Valid until cancelled<br><br>`GoodTilDate` - Valid until expiry |
| data.orders[].expireDate | string |  | Long-term order expiry date, format:<br><br>`YYYY-MM-DD`. `null` for non-GoodTilDate orders |
| data.orders[].updatedAt | string |  | Last update time (ISO 8601). `null` if never updated |
| data.orders[].triggerAt | string |  | Conditional order trigger time (ISO 8601). `null` if not triggered |
| data.orders[].trailingAmount | string |  | `TSLPAMT` order trailing amount. `null` for non-TSLPAMT orders |
| data.orders[].trailingPercent | string |  | `TSLPPCT` order trailing percentage. `null` for non-TSLPPCT orders |
| data.orders[].limitOffset | string |  | `TSLPAMT`/`TSLPPCT` order spread. `null` for non-TSLP orders |
| data.orders[].triggerStatus | string |  | Conditional order trigger status. `null` for non-conditional orders<br><br>`NOT_USED` - Not active<br><br>`DEACTIVE` - Deactivated<br><br>`ACTIVE` - Active<br><br>`RELEASED` - Triggered |
| data.orders[].currency | string |  | Settlement currency |
| data.orders[].outsideRth | string |  | Allow pre/post market trading. `UnknownOutsideRth` for non-US orders<br><br>`RTHOnly` - Do not allow<br><br>`AnyTime` - Allow<br><br>`Overnight` - Overnight |
| data.orders[].remark | string |  | Remark |
| data.orders[].limitDepthLevel | number |  | Specified bid/ask level |
| data.orders[].triggerCount | number |  | Trigger count |
| data.orders[].monitorPrice | string |  | Monitor price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "hasMore": false,
    "orders": [
      {
        "orderId": "701276261045858304",
        "status": "Canceled",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 0,
        "price": 150,
        "executedPrice": null,
        "submittedAt": "2024-12-16T12:07:12Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T12:07:23Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "RTHOnly",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      },
      {
        "orderId": "701276261045858305",
        "status": "Filled",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 1,
        "price": 80,
        "executedPrice": 10,
        "submittedAt": "2024-12-16T10:00:00Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T10:00:01Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "AnyTime",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      }
    ]
  }
}
```

## Check Order Detail

`GET /api/v3/stockplus/trade/order-detail`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read only)

This interface is used to query order detail information.

Operation ID: `stockPlusOrdersGetOrderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID, e.g. `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.status | string |  | Order status<br><br>`NotReported` - Not reported<br><br>`ReplacedNotReported` - Replaced not reported<br><br>`ProtectedNotReported` - Protected not reported<br><br>`VarietiesNotReported` - Varieties not reported<br><br>`Filled` - Fully filled<br><br>`WaitToNew` - Waiting for new<br><br>`New` - New<br><br>`WaitToReplace` - Waiting for replace<br><br>`PendingReplace` - Pending replace<br><br>`Replaced` - Replaced<br><br>`PartialFilled` - Partially filled<br><br>`WaitToCancel` - Waiting for cancel<br><br>`PendingCancel` - Pending cancel<br><br>`Rejected` - Rejected<br><br>`Canceled` - Canceled<br><br>`Expired` - Expired<br><br>`PartialWithdrawal` - Partial withdrawal |
| data.stockName | string |  | Stock name |
| data.quantity | string |  | Order quantity |
| data.executedQuantity | string |  | Executed quantity. `"0"` for unfilled orders |
| data.price | string |  | Order price. `null` when market conditional order not yet triggered |
| data.executedPrice | string |  | Executed price. `"0"` for unfilled orders |
| data.submittedAt | string |  | Order submission time |
| data.side | string |  | Order side. `Buy` - Buy, `Sell` - Sell |
| data.symbol | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| data.orderType | string |  | Order type<br><br>`LO` Limit Order<br><br>`MO` Market Order<br><br>`LIT` Limit If Touched<br><br>`MIT` Market If Touched<br><br>`TSLPAMT` Trailing Stop Limit Order (Trailing Amount)<br><br>`TSLPPCT` Trailing Stop Limit Order (Trailing Percentage) |
| data.lastDone | string |  | Latest traded price. `"0"` for unfilled orders |
| data.triggerPrice | string |  | Trigger price for `LIT`/`MIT` orders. `null` for non-conditional orders |
| data.msg | string |  | Rejection reason or remark. Empty string by default |
| data.tag | string |  | Order tag<br><br>`Normal` - Normal order<br><br>`GTC` - GTC order |
| data.timeInForce | string |  | Order validity type<br><br>`Day` - Valid for the day<br><br>`GoodTilCanceled` - Valid until cancelled<br><br>`GoodTilDate` - Valid until expiry |
| data.expireDate | string |  | Long-term order expiry date, format:<br><br>`YYYY-MM-DD`. `null` for non-GTD orders |
| data.updatedAt | string |  | Last update time (ISO 8601). `null` if never updated |
| data.triggerAt | string |  | Conditional order trigger time, timestamp (ISO 8601) |
| data.trailingAmount | string |  | `TSLPAMT` order trailing amount. `null` for non-TSLPAMT orders |
| data.trailingPercent | string |  | `TSLPPCT` order trailing percentage. `null` for non-TSLPPCT orders |
| data.limitOffset | string |  | `TSLPAMT`/`TSLPPCT` order spread. `null` for non-TSLP orders |
| data.triggerStatus | string |  | Conditional order trigger status. `null` for non-conditional orders<br><br>`NOT_USED` - Not active<br><br>`DEACTIVE` - Deactivated<br><br>`ACTIVE` - Active<br><br>`RELEASED` - Triggered |
| data.currency | string |  | Settlement currency |
| data.outsideRth | string |  | Allow pre/post market trading. `UnknownOutsideRth` for non-US orders<br><br>`RTHOnly` - Do not allow<br><br>`AnyTime` - Allow<br><br>`Overnight` - Overnight |
| data.remark | string |  | Remark |
| data.limitDepthLevel | number |  | Specified bid/ask level |
| data.triggerCount | number |  | Trigger count |
| data.monitorPrice | string |  | Monitor price |
| data.freeStatus | string |  | Commission-free status. Default `None`<br><br>`None` - None<br><br>`Calculated` - To be calculated<br><br>`Pending` - Pending<br><br>`Ready` - Completed |
| data.freeAmount | string |  | Commission-free amount. Default `null` |
| data.freeCurrency | string |  | Commission-free currency. Default `null` |
| data.deductionsStatus | string |  | Deduction/rebate status. Default `None`<br><br>`None` - Pending settlement / No data<br><br>`Pending` - Settled, pending issuance<br><br>`Done` - Settled, issued |
| data.deductionsAmount | string |  | Deduction amount. Default `null` |
| data.deductionsCurrency | string |  | Deduction currency. Default `null` |
| data.platformDeductedStatus | string |  | Platform fee deduction/rebate status. Default `None`<br><br>`None` - Pending settlement / No data<br><br>`Pending` - Settled, pending issuance<br><br>`Done` - Settled, issued |
| data.platformDeductedAmount | string |  | Platform fee deduction amount. Default `null` |
| data.platformDeductedCurrency | string |  | Platform fee deduction currency. Default `null` |
| data.history | object[] |  | Order history details |
| data.history[].price | number |  | Trade display price (for filled), submission price (for expired/cancelled/rejected) |
| data.history[].quantity | number |  | Trade display quantity (for filled), remaining quantity (for expired/cancelled/rejected) |
| data.history[].status | string |  | Order status |
| data.history[].msg | string |  | Trade or error message |
| data.history[].time | string |  | Occurrence time |
| data.chargeDetail | object |  | Order charges |
| data.chargeDetail.totalAmount | number |  | Total charges |
| data.chargeDetail.currency | string |  | Settlement currency |
| data.chargeDetail.items | object[] |  | Order charge details |
| data.chargeDetail.items[].code | string |  | Charge category code<br><br>`Broker`<br><br>`Third` |
| data.chargeDetail.items[].name | string |  | Charge category name |
| data.chargeDetail.items[].fees | object[] |  | Charge details |
| data.chargeDetail.items[].fees[].code | string |  | Charge code |
| data.chargeDetail.items[].fees[].name | string |  | Charge name |
| data.chargeDetail.items[].fees[].amount | number |  | Individual charge amount |
| data.chargeDetail.items[].fees[].currency | string |  | Charge currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "status": "Filled",
    "stockName": "Apple Inc.",
    "quantity": 1,
    "executedQuantity": 0,
    "price": 150,
    "executedPrice": null,
    "submittedAt": "2024-12-16T12:07:12Z",
    "side": "Buy",
    "symbol": "AAPL.US",
    "orderType": "LO",
    "lastDone": null,
    "triggerPrice": null,
    "msg": "",
    "tag": "Normal",
    "timeInForce": "Day",
    "expireDate": "2024-12-16",
    "updatedAt": null,
    "triggerAt": null,
    "trailingAmount": null,
    "trailingPercent": null,
    "limitOffset": null,
    "triggerStatus": null,
    "currency": "USD",
    "outsideRth": "RTHOnly",
    "remark": "remark from Java SDK",
    "limitDepthLevel": null,
    "triggerCount": null,
    "monitorPrice": null,
    "freeStatus": "None",
    "freeAmount": null,
    "freeCurrency": null,
    "deductionsStatus": "None",
    "deductionsAmount": null,
    "deductionsCurrency": null,
    "platformDeductedStatus": "None",
    "platformDeductedAmount": null,
    "platformDeductedCurrency": null,
    "history": [
      {
        "price": 10,
        "quantity": 1,
        "status": "Filled",
        "msg": "",
        "time": "2024-12-16T12:07:12Z"
      },
      {
        "price": 80,
        "quantity": 1,
        "status": "New",
        "msg": "",
        "time": "2024-12-16T12:06:55Z"
      }
    ],
    "chargeDetail": {
      "totalAmount": 0,
      "currency": "USD",
      "items": [
        {
          "code": "Broker",
          "name": "Broker Fees",
          "fees": []
        },
        {
          "code": "Third",
          "name": "Third-party Fees",
          "fees": []
        }
      ]
    }
  }
}
```

## Estimate Max Purchase Quantity

`GET /api/v3/stockplus/trade/max-purchase`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

This interface is used to query the estimated maximum purchasable quantity for stocks and options.

Note: This interface is currently only available to whitelisted users (must have completed securities account opening). Please contact your BD to apply for whitelist access.

Operation ID: `stockPlusOrdersEstimateMaxPurchase`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| orderType | query | string | 是 | Order type<br><br>`LO` Limit Order<br><br>`MO` Market Order<br><br>`LIT` Limit If Touched<br><br>`MIT` Market If Touched<br><br>`TSLPAMT` Trailing Stop Limit Order (Trailing Amount)<br><br>`TSLPPCT` Trailing Stop Limit Order (Trailing Percentage) |
| price | query | string |  | Estimated order price, e.g. `388.5` |
| side | query | string | 是 | Order side<br><br>`Buy` - Buy<br><br>`Sell` - Sell. The sell side query is only supported for US stock short selling |
| currency | query | string |  | Settlement currency |
| orderId | query | string |  | Order ID. Required when estimating the max purchasable quantity for an order modification |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cashMaxQty | string |  | Cash max purchasable quantity. Defaults to an empty string |
| data.marginMaxQty | string |  | Margin max purchasable quantity. Defaults to an empty string |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "cashMaxQty": "100",
    "marginMaxQty": "300"
  }
}
```

## Check Today Executions

`GET /api/v3/stockplus/trade/today-executions`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read only)

This interface is used to query today's order execution details.

Operation ID: `stockPlusOrdersGetTodayExecutions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| orderId | query | string |  | Order ID, e.g. `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trades | object[] |  | Execution detail information |
| data.trades[].orderId | string |  | Order ID |
| data.trades[].tradeId | string |  | Trade ID |
| data.trades[].symbol | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| data.trades[].tradeDoneAt | string |  | Trade time (ISO 8601) |
| data.trades[].quantity | number |  | Trade quantity |
| data.trades[].price | number |  | Trade price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "trades": [
      {
        "orderId": "701276261045858304",
        "tradeId": "0f40217c-a73c-410d-b599-2ff6a9ee762e",
        "symbol": "AAPL.US",
        "tradeDoneAt": "2024-12-16T12:07:12Z",
        "quantity": 1,
        "price": 150
      }
    ]
  }
}
```

## Check History Executions

`GET /api/v3/stockplus/trade/history-executions`

Rate limit: 30 times/30s (UID), minimum interval 0.02 seconds

Permission: Trade (read only)

This interface is used to query historical order execution records, including buy and sell execution records. Does not support today's execution query.

Operation ID: `stockPlusOrdersGetHistoryExecutions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| startAt | query | number |  | Start time, timestamp in seconds, e.g. `1650410999`. Defaults to 90 days before end time or current time |
| endAt | query | number |  | End time, timestamp in seconds, e.g. `1650410999`. Defaults to 90 days after start time or current time |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasMore | boolean |  | Whether there is more data. Max 1000 orders per query; hasMore is true when results exceed 1000 |
| data.trades | object[] |  | Execution detail information |
| data.trades[].orderId | string |  | Order ID |
| data.trades[].tradeId | string |  | Trade ID |
| data.trades[].symbol | string |  | Symbol, using `ticker.region` format, e.g. `AAPL.US` |
| data.trades[].tradeDoneAt | string |  | Trade time (ISO 8601) |
| data.trades[].quantity | number |  | Trade quantity |
| data.trades[].price | number |  | Trade price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "hasMore": false,
    "trades": [
      {
        "orderId": "701276261045858304",
        "tradeId": "0f40217c-a73c-410d-b599-2ff6a9ee762e",
        "symbol": "AAPL.US",
        "tradeDoneAt": "2024-12-16T12:07:12Z",
        "quantity": 1,
        "price": 150
      }
    ]
  }
}
```

## Transfer

`POST /api/v3/stockplus/asset/transfer`

Rate limit: 5 times/sec/UID

Permission: Trade (management, read and write)

This interface is used for Stock+ account deposit and withdrawal.

Operation ID: `stockPlusAssetsTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Transfer currency<br><br>Currently supports USDC and USD |
| amount | query | string |  | Transfer amount |
| direction | query | string |  | Transfer direction<br><br>`in` - Deposit to Stock+ account<br><br>`out` - Withdraw from Stock+ account<br><br>Currently only supports transfers between spot account and securities account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "123456789"
  }
}
```

## Check Transfer Records

`GET /api/v3/stockplus/asset/transfer-records`

Rate limit: 10 times/sec/UID

Permission: Trade (management, read only)

This interface is used to query Stock+ account deposit and withdrawal records.

Operation ID: `stockPlusAssetsGetTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| transferId | query | string |  | Transfer ID |
| startTime | query | string |  | Start time, timestamp in milliseconds |
| endTime | query | string |  | End time, timestamp in milliseconds |
| limit | query | string |  | Number of entries per page |
| cursor | query | string |  | Cursor ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.coin | string |  | Transfer currency<br><br>Currently supports USDC and USD |
| data.amount | string |  | Transfer amount |
| data.direction | string |  | Transfer direction<br><br>`in` - Deposit to Stock+ account<br><br>`out` - Withdraw from Stock+ account |
| data.cursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "123456789",
    "coin": "USDC",
    "amount": "100.00",
    "direction": "in",
    "cursor": "abc123"
  }
}
```

## Check Account

`GET /api/v3/stockplus/asset/account`

Permission: Trade (management, read only)

This interface is used to query available, withdrawable, frozen, pending settlement and in-transit fund (fund subscription/redemption) information for each currency.

Operation ID: `stockPlusAssetsGetAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| currency | query | string |  | Currency (USD, CNH) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Account fund information |
| data.list[].totalCash | number |  | Total cash |
| data.list[].maxFinanceAmount | number |  | Max financing amount |
| data.list[].remainingFinanceAmount | number |  | Remaining financing amount |
| data.list[].riskLevel | number |  | Risk control level<br><br>`0` - Safe<br><br>`1` - Medium risk<br><br>`2` - Warning<br><br>`3` - Danger |
| data.list[].marginCall | number |  | Margin call amount |
| data.list[].netAssets | number |  | Net assets |
| data.list[].initMargin | number |  | Initial margin |
| data.list[].maintenanceMargin | number |  | Maintenance margin |
| data.list[].currency | string |  | Currency |
| data.list[].buyPower | number |  | Buying power |
| data.list[].cashInfos | object[] |  | Cash details |
| data.list[].cashInfos[].withdrawCash | number |  | Withdrawable cash |
| data.list[].cashInfos[].availableCash | number |  | Available cash |
| data.list[].cashInfos[].frozenCash | number |  | Frozen cash |
| data.list[].cashInfos[].settlingCash | number |  | Pending settlement cash |
| data.list[].cashInfos[].currency | string |  | Currency |
| data.list[].frozenTransactionFees | object[] |  | Frozen transaction fees (can be empty array) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "totalCash": 13.88,
        "maxFinanceAmount": 0,
        "remainingFinanceAmount": 13.88,
        "riskLevel": 0,
        "marginCall": 0,
        "netAssets": 13.88,
        "initMargin": 0,
        "maintenanceMargin": 0,
        "currency": "USD",
        "buyPower": 13.88,
        "cashInfos": [
          {
            "withdrawCash": 13.88,
            "availableCash": 13.88,
            "frozenCash": 0,
            "settlingCash": 0,
            "currency": "USD"
          }
        ],
        "frozenTransactionFees": []
      }
    ]
  }
}
```

## Check Cash Flow

`GET /api/v3/stockplus/asset/cash-flow`

Permission: Trade (management, read only)

This interface is used to query cash inflow/outflow direction, fund type, amount, occurrence time, related symbol and description.

Operation ID: `stockPlusAssetsGetCashFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | number | 是 | Start time, timestamp in seconds, e.g. `1650037563` |
| endTime | query | number | 是 | End time, timestamp in seconds, e.g. `1650747581` |
| businessType | query | string |  | Fund type<br><br>`Cash` - Cash<br><br>`Stock` - Stock<br><br>`Fund` - Fund |
| symbol | query | string |  | Symbol, e.g. `AAPL.US` |
| page | query | number |  | Start page. Default: <br><br>`1`. Range: <br><br>`>=1` |
| size | query | number |  | Page size. Default: <br><br>`50`. Range: <br><br>`1~10000` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Cash flow information |
| data.list[].transactionFlowName | string |  | Flow name |
| data.list[].direction | string |  | Direction<br><br>`In` - Inflow<br><br>`Out` - Outflow |
| data.list[].businessType | string |  | Fund type<br><br>`Cash` - Cash<br><br>`Stock` - Stock<br><br>`Fund` - Fund |
| data.list[].balance | number |  | Amount |
| data.list[].currency | string |  | Currency |
| data.list[].businessTime | string |  | Business time (ISO 8601) |
| data.list[].symbol | string |  | Related symbol (can be `null`) |
| data.list[].description | string |  | Cash flow description (can be empty string) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transactionFlowName": "Buy AAPL.US",
        "direction": "Out",
        "businessType": "Unknown",
        "balance": -1500,
        "currency": "USD",
        "businessTime": "2024-12-16T10:00:00Z",
        "symbol": "AAPL.US",
        "description": "Buy 10 shares of AAPL.US"
      },
      {
        "transactionFlowName": "Deposit Cash",
        "direction": "In",
        "businessType": "Unknown",
        "balance": 100000.0,
        "currency": "USD",
        "businessTime": "2024-12-15T06:10:57Z",
        "symbol": null,
        "description": ""
      }
    ]
  }
}
```

## Check Stock Position

`GET /api/v3/stockplus/asset/stock-position`

Permission: Trade (management, read only)

This interface is used to query stock position information including account, symbol, holding quantity, available quantity, average cost price (calculated based on account settings) and currency.

Operation ID: `stockPlusAssetsGetStockPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol list, using `ticker.region` format, multiple separated by `,`, e.g. `AAPL.US,MSTR.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.channels | object[] |  | Account channel list |
| data.channels[].accountChannel | string |  | Account channel |
| data.channels[].positions | object[] |  | Position list |
| data.channels[].positions[].symbol | string |  | Symbol |
| data.channels[].positions[].symbolName | string |  | Stock name |
| data.channels[].positions[].quantity | number |  | Holding quantity |
| data.channels[].positions[].availableQuantity | number |  | Available quantity |
| data.channels[].positions[].currency | string |  | Currency |
| data.channels[].positions[].costPrice | number |  | Cost price (based on client's average buy or diluted cost setting) |
| data.channels[].positions[].market | string |  | Market |
| data.channels[].positions[].initQuantity | number |  | Initial holding before market open |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "channels": [
      {
        "accountChannel": "sg_bitget_uat",
        "positions": [
          {
            "symbol": "AAPL.US",
            "symbolName": "Apple Inc.",
            "quantity": 100,
            "availableQuantity": 80,
            "currency": "USD",
            "costPrice": 145.5,
            "market": "US",
            "initQuantity": 100
          }
        ]
      }
    ]
  }
}
```


---

Stock+ 美股/ETF 与期权行情、订单/成交管理及资产接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/stockplus/market/option-quote` — 查询期权实时报价
- `GET /api/v3/stockplus/market/option-chain-info` — 查询期权链
- `GET /api/v3/stockplus/market/option-expiry-date` — 获取到期日列表
- `GET /api/v3/stockplus/market/option-volume` — 查询期权成交量
- `GET /api/v3/stockplus/market/static` — 获取标的基本信息
- `GET /api/v3/stockplus/market/candlestick` — 获取标的K线
- `GET /api/v3/stockplus/market/history-candlestick` — 获取标的历史K线
- `GET /api/v3/stockplus/market/depth` — 获取标的盘口
- `GET /api/v3/stockplus/market/intraday` — 获取标的当日分时数据
- `GET /api/v3/stockplus/market/quote` — 获取标的实时报价
- `GET /api/v3/stockplus/market/trade` — 获取标的逐笔明细
- `POST /api/v3/stockplus/trade/place-order` — 创建订单
- `POST /api/v3/stockplus/trade/modify-order` — 修改订单
- `POST /api/v3/stockplus/trade/cancel-order` — 撤销订单
- `GET /api/v3/stockplus/trade/today-orders` — 查询当日订单
- `GET /api/v3/stockplus/trade/history-orders` — 查询历史订单
- `GET /api/v3/stockplus/trade/order-detail` — 查询订单详情
- `GET /api/v3/stockplus/trade/max-purchase` — 预估最大购买数量
- `GET /api/v3/stockplus/trade/today-executions` — 查询当日成交
- `GET /api/v3/stockplus/trade/history-executions` — 查询历史成交
- `POST /api/v3/stockplus/asset/transfer` — 资金划转
- `GET /api/v3/stockplus/asset/transfer-records` — 获取划转记录
- `GET /api/v3/stockplus/asset/account` — 查询账户资金
- `GET /api/v3/stockplus/asset/cash-flow` — 查询资金流水
- `GET /api/v3/stockplus/asset/stock-position` — 查询股票持仓

## 查询期权实时报价

`GET /api/v3/stockplus/market/option-quote`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

该接口用于批量查询美股期权合约的实时行情，包含期权特有的行情字段（隐含波动率、未平仓数、行权价等）。

注意：

- 通过 Open API 访问期权实时报价，需要先领取「OPRA 美股期权行情（API）」行情卡。

- OPRA 期权行情（API）仅针对白名单用户开放，请联系 BD 申请。

- 新开通 Stock+ 期权交易功能的客户，请点击 APP 右上角「美股」，点击 我的 > 我的卡券 > 立即激活，完成《非专业用户评估问卷》后领取 OPRA 实时行情卡。

Operation ID: `stockPlusOptionsQuotesGetOptionQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码列表，通过期权链接口获取期权标的的symbol。使用 `ticker.region` 格式，例如 `AAPL220429P162500.US`<br><br>**校验规则：** 每次请求支持传入的标的数量上限是 `500` 个 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.secuQuote | object[] |  | 期权标的行情数据列表 |
| data.secuQuote[].symbol | string |  | 标的代码 |
| data.secuQuote[].lastDone | string |  | 最新价 |
| data.secuQuote[].prevClose | string |  | 昨收价 |
| data.secuQuote[].open | string |  | 开盘价 |
| data.secuQuote[].high | string |  | 最高价 |
| data.secuQuote[].low | string |  | 最低价 |
| data.secuQuote[].timestamp | string |  | 最新成交的时间戳 |
| data.secuQuote[].volume | string |  | 成交量 |
| data.secuQuote[].turnover | string |  | 成交额 |
| data.secuQuote[].tradeStatus | string |  | 交易状态<br><br>`Normal` - 正常交易<br><br>`Suspended` - 停牌<br><br>`Delisted` - 退市<br><br>`CircuitBreaker` - 熔断<br><br>`PendingListing` - 新股待上市<br><br>`CodeChange` - 代码变更<br><br>`PreMarket` - 待开盘<br><br>`RebaseSuspension` - 拆合股暂停交易<br><br>`Expired` - 已到期 (衍生品)<br><br>`Terminated` - 终止交易 |
| data.secuQuote[].impliedVolatility | string |  | 隐含波动率 |
| data.secuQuote[].openInterest | string |  | 未平仓数 |
| data.secuQuote[].expiryDate | string |  | 到期日，格式：<br><br>`YYMMDD` |
| data.secuQuote[].strikePrice | string |  | 行权价 |
| data.secuQuote[].contractMultipier | string |  | 合约乘数 |
| data.secuQuote[].contractType | string |  | 期权类型。`A` - 美式，`U` - 欧式 |
| data.secuQuote[].contractSize | string |  | 合约规模 |
| data.secuQuote[].direction | string |  | 方向。`P` - Put, `C` - Call |
| data.secuQuote[].historicalVolatility | string |  | 对应正股的历史波动率 |
| data.secuQuote[].underlyingSymbol | string |  | 对应的正股标的代码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "secuQuote": [
      {
        "symbol": "AAPL220429P162500.US",
        "lastDone": "7.78",
        "prevClose": "4.13",
        "open": "4.43",
        "high": "7.80",
        "low": "4.43",
        "timestamp": "1651003200000",
        "volume": "3082",
        "turnover": "1813434.00",
        "tradeStatus": "1",
        "impliedVolatility": "0.592",
        "openInterest": "11463",
        "expiryDate": "20220429",
        "strikePrice": "162.50",
        "contractMultipier": "100",
        "contractType": "A",
        "contractSize": "100",
        "direction": "P",
        "historicalVolatility": "0.2750",
        "underlyingSymbol": "AAPL.US"
      }
    ]
  }
}
```

## 查询期权链

`GET /api/v3/stockplus/market/option-chain-info`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

该接口用于根据正股标的查询其下所有期权合约，按到期日分组返回。

Operation ID: `stockPlusOptionsQuotesGetOptionChainInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |
| expiryDate | query | string | 是 | 期权到期日，格式：<br><br>`YYYYMMDD`，例如：<br><br>`20220429`，通过到期日列表接口获取 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strikePriceInfo | object[] |  | 到期日期权标的列表 |
| data.strikePriceInfo[].price | string |  | 行权价 |
| data.strikePriceInfo[].callSymbol | string |  | CALL 期权标的代码 |
| data.strikePriceInfo[].putSymbol | string |  | PUT 期权标的代码 |
| data.strikePriceInfo[].standard | boolean |  | 是否标准期权 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strikePriceInfo": [
      {
        "price": "160.00",
        "callSymbol": "AAPL220429C160000.US",
        "putSymbol": "AAPL220429P160000.US",
        "standard": true
      }
    ]
  }
}
```

## 获取到期日列表

`GET /api/v3/stockplus/market/option-expiry-date`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

该接口用于获取标的的期权链到期日列表。

Operation ID: `stockPlusOptionsQuotesGetOptionExpiryDate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.expiryDate | string[] |  | 标的对应的期权链到期日列表，格式：<br><br>`YYMMDD` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "expiryDate": [
      "20220429",
      "20220506",
      "20220513"
    ]
  }
}
```

## 查询期权成交量

`GET /api/v3/stockplus/market/option-volume`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

该接口用于获取今日认购/认沽期权成交量快照。

Operation ID: `stockPlusOptionsQuotesGetOptionVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 美股标的代码，例如：<br><br>`AAPL.US`、`TSLA.US` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.c | string |  | 当日总认购期权成交量 |
| data.p | string |  | 当日总认沽期权成交量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "c": "284512",
    "p": "195830"
  }
}
```

## 获取标的基本信息

`GET /api/v3/stockplus/market/static`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的基础信息。

Operation ID: `stockPlusStockQuotesGetStaticInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码列表，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US`<br><br>**校验规则：** 每次请求支持传入的标的数量上限是 `500` 个 |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 标的基础数据列表 |
| data.list[].symbol | string |  | 标的代码 |
| data.list[].nameCn | string |  | 中文简体标的名称 |
| data.list[].nameEn | string |  | 英文标的名称 |
| data.list[].exchange | string |  | 标的所属交易所 |
| data.list[].currency | string |  | 交易币种。`CNY`、`USD` |
| data.list[].lotSize | integer |  | 每手股数 |
| data.list[].totalShares | string |  | 总股本 |
| data.list[].circulatingShares | string |  | 流通股本 |
| data.list[].eps | string |  | 每股盈利 |
| data.list[].epsTtm | string |  | 每股盈利（TTM） |
| data.list[].bps | string |  | 每股净资产 |
| data.list[].dividendYield | string |  | 股息 |
| data.list[].stockDerivatives | string[] |  | 可提供的衍生品行情类型。`Option` - 期权 |
| data.list[].board | string |  | 标的所属板块 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "AAPL.US",
        "nameCn": "苹果",
        "nameEn": "Apple Inc.",
        "exchange": "NASD",
        "currency": "USD",
        "lotSize": 1,
        "totalShares": 16319441000.0,
        "circulatingShares": 16302661350,
        "eps": 5.669,
        "epsTtm": 6.0771,
        "bps": 4.40197,
        "dividendYield": 0.85,
        "stockDerivatives": [
          "Option"
        ],
        "board": "USMain"
      }
    ]
  }
}
```

## 获取标的K线

`GET /api/v3/stockplus/market/candlestick`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的的K线数据。注意：本接口只能获取到最近 1000 根K线，如需获取较长的历史数据，请使用历史K线接口。

Operation ID: `stockPlusStockQuotesGetCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |
| period | query | string | 是 | K线周期<br><br>`Min_1` - 1分<br><br>`Min_2` - 2分<br><br>`Min_3` - 3分<br><br>`Min_5` - 5分<br><br>`Min_10` - 10分<br><br>`Min_15` - 15分<br><br>`Min_20` - 20分<br><br>`Min_30` - 30分<br><br>`Min_45` - 45分<br><br>`Min_60` - 60分<br><br>`Min_120` - 120分<br><br>`Min_180` - 180分<br><br>`Min_240` - 240分<br><br>`Day` - 日线<br><br>`Week` - 周线<br><br>`Month` - 月线<br><br>`Quarter` - 季线<br><br>`Year` - 年线 |
| count | query | integer | 是 | 数据数量，上限 `1000` |
| adjustType | query | string | 是 | K线复权类型<br><br>`NoAdjust` - 除权<br><br>`ForwardAdjust` - 前复权 |
| tradeSessions | query | string |  | 交易时段<br><br>`Intraday` - 盘中交易<br><br>`Pre` - 盘前交易<br><br>`Post` - 盘后交易<br><br>`Overnight` - 夜盘交易 |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | K线数据 |
| data.list[].close | string |  | 收盘价 |
| data.list[].open | string |  | 开盘价 |
| data.list[].low | string |  | 最低价 |
| data.list[].high | string |  | 最高价 |
| data.list[].volume | string |  | 成交量 |
| data.list[].turnover | string |  | 成交额 |
| data.list[].timestamp | string |  | 时间戳 |
| data.list[].tradeSession | string |  | 交易时段<br><br>`Intraday` - 盘中交易<br><br>`Pre` - 盘前交易<br><br>`Post` - 盘后交易<br><br>`Overnight` - 夜盘交易 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "close": "175.460",
        "open": "176.750",
        "low": "175.180",
        "high": "177.840",
        "volume": "54321000",
        "turnover": "9587654321",
        "timestamp": "1697414400",
        "tradeSession": "Intraday"
      },
      {
        "close": "176.810",
        "open": "175.580",
        "low": "174.910",
        "high": "177.110",
        "volume": "48765000",
        "turnover": "8601234567",
        "timestamp": "1697500800",
        "tradeSession": "Intraday"
      },
      {
        "close": "177.150",
        "open": "177.060",
        "low": "176.450",
        "high": "178.420",
        "volume": "42210000",
        "turnover": "7498765432",
        "timestamp": "1697587200",
        "tradeSession": "Intraday"
      }
    ]
  }
}
```

## 获取标的历史K线

`GET /api/v3/stockplus/market/history-candlestick`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的历史K线数据。

Operation ID: `stockPlusStockQuotesGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |
| period | query | string | 是 | K线周期<br><br>`Min_1` - 1分<br><br>`Min_2` - 2分<br><br>`Min_3` - 3分<br><br>`Min_5` - 5分<br><br>`Min_10` - 10分<br><br>`Min_15` - 15分<br><br>`Min_20` - 20分<br><br>`Min_30` - 30分<br><br>`Min_45` - 45分<br><br>`Min_60` - 60分<br><br>`Min_120` - 120分<br><br>`Min_180` - 180分<br><br>`Min_240` - 240分<br><br>`Day` - 日线<br><br>`Week` - 周线<br><br>`Month` - 月线<br><br>`Quarter` - 季线<br><br>`Year` - 年线 |
| count | query | integer | 是 | 数据数量，上限 `1000` |
| adjustType | query | string | 是 | K线复权类型<br><br>`NoAdjust` - 除权<br><br>`ForwardAdjust` - 前复权 |
| forward | query | boolean |  | 查询方向。默认 `false`<br><br>`false` - 向后查询<br><br>`true` - 向前查询 |
| time | query | string |  | 查询时间戳，Unix 秒。默认当前时间 |
| tradeSessions | query | string |  | 交易时段<br><br>`Intraday` - 盘中交易<br><br>`Pre` - 盘前交易<br><br>`Post` - 盘后交易<br><br>`Overnight` - 夜盘交易（包含在美股 LV1 中，仅美股有效） |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | K线数据 |
| data.list[].close | string |  | 收盘价 |
| data.list[].open | string |  | 开盘价 |
| data.list[].low | string |  | 最低价 |
| data.list[].high | string |  | 最高价 |
| data.list[].volume | string |  | 成交量 |
| data.list[].turnover | string |  | 成交额 |
| data.list[].timestamp | string |  | 时间戳 |
| data.list[].tradeSession | string |  | 交易时段<br><br>`Intraday` - 盘中交易<br><br>`Pre` - 盘前交易<br><br>`Post` - 盘后交易<br><br>`Overnight` - 夜盘交易 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "close": "175.460",
        "open": "176.750",
        "low": "175.180",
        "high": "177.840",
        "volume": "54321000",
        "turnover": "9587654321",
        "timestamp": "1697414400",
        "tradeSession": "Intraday"
      },
      {
        "close": "176.810",
        "open": "175.580",
        "low": "174.910",
        "high": "177.110",
        "volume": "48765000",
        "turnover": "8601234567",
        "timestamp": "1697500800",
        "tradeSession": "Intraday"
      },
      {
        "close": "177.150",
        "open": "177.060",
        "low": "176.450",
        "high": "178.420",
        "volume": "42210000",
        "turnover": "7498765432",
        "timestamp": "1697587200",
        "tradeSession": "Intraday"
      }
    ]
  }
}
```

## 获取标的盘口

`GET /api/v3/stockplus/market/depth`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的的盘口数据。

Operation ID: `stockPlusStockQuotesGetDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | object[] |  | 卖盘 |
| data.asks[].position | integer |  | 档位 |
| data.asks[].price | string |  | 价格 |
| data.asks[].volume | string |  | 委托量 |
| data.asks[].orderNum | integer |  | 委托订单数量 |
| data.bids | object[] |  | 买盘 |
| data.bids[].position | integer |  | 档位 |
| data.bids[].price | string |  | 价格 |
| data.bids[].volume | string |  | 委托量 |
| data.bids[].orderNum | integer |  | 委托订单数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "asks": [
      {
        "position": 1,
        "price": "195.900",
        "volume": "200",
        "orderNum": 5
      },
      {
        "position": 2,
        "price": "195.910",
        "volume": "500",
        "orderNum": 8
      },
      {
        "position": 3,
        "price": "195.920",
        "volume": "300",
        "orderNum": 3
      },
      {
        "position": 4,
        "price": "195.930",
        "volume": "800",
        "orderNum": 12
      },
      {
        "position": 5,
        "price": "195.940",
        "volume": "150",
        "orderNum": 2
      }
    ],
    "bids": [
      {
        "position": 1,
        "price": "195.880",
        "volume": "350",
        "orderNum": 6
      },
      {
        "position": 2,
        "price": "195.870",
        "volume": "600",
        "orderNum": 9
      },
      {
        "position": 3,
        "price": "195.860",
        "volume": "450",
        "orderNum": 7
      },
      {
        "position": 4,
        "price": "195.850",
        "volume": "200",
        "orderNum": 4
      },
      {
        "position": 5,
        "price": "195.840",
        "volume": "700",
        "orderNum": 11
      }
    ]
  }
}
```

## 获取标的当日分时数据

`GET /api/v3/stockplus/market/intraday`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的的当日分时数据。

Operation ID: `stockPlusStockQuotesGetIntraday`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 分时数据 |
| data.list[].price | string |  | 当前分钟的收盘价 |
| data.list[].timestamp | string |  | 当前分钟开始的时间戳（ISO 8601） |
| data.list[].volume | string |  | 成交量 |
| data.list[].turnover | string |  | 成交额 |
| data.list[].avgPrice | string |  | 均价 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "price": 195.89,
        "timestamp": "2024-10-16T09:30:00Z",
        "volume": 150000.0,
        "turnover": 29383500,
        "avgPrice": 195.88
      },
      {
        "price": 195.92,
        "timestamp": "2024-10-16T09:31:00Z",
        "volume": 180000.0,
        "turnover": 35265600,
        "avgPrice": 195.91
      },
      {
        "price": 195.85,
        "timestamp": "2024-10-16T09:32:00Z",
        "volume": 120000.0,
        "turnover": 23502000.0,
        "avgPrice": 195.87
      },
      {
        "price": 195.88,
        "timestamp": "2024-10-16T09:33:00Z",
        "volume": 200000.0,
        "turnover": 39176000.0,
        "avgPrice": 195.88
      },
      {
        "price": 195.9,
        "timestamp": "2024-10-16T09:34:00Z",
        "volume": 160000.0,
        "turnover": 31344000.0,
        "avgPrice": 195.89
      }
    ]
  }
}
```

## 获取标的实时报价

`GET /api/v3/stockplus/market/quote`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的的实时行情（支持所有类型标的）。

Operation ID: `stockPlusStockQuotesGetQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码列表，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US`<br><br>**校验规则：** 每次请求支持传入的标的数量上限是 `500` 个 |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 标的实时行情数据列表 |
| data.list[].symbol | string |  | 标的代码 |
| data.list[].lastDone | string |  | 最新价 |
| data.list[].prevClose | string |  | 昨收价 |
| data.list[].open | string |  | 开盘价 |
| data.list[].high | string |  | 最高价 |
| data.list[].low | string |  | 最低价 |
| data.list[].timestamp | string |  | 最新成交的时间戳（ISO 8601） |
| data.list[].volume | string |  | 成交量 |
| data.list[].turnover | string |  | 成交额 |
| data.list[].tradeStatus | string |  | 交易状态<br><br>`Normal` - 正常交易<br><br>`Suspended` - 停牌<br><br>`Delisted` - 退市<br><br>`CircuitBreaker` - 熔断<br><br>`PendingListing` - 新股待上市<br><br>`CodeChange` - 代码变更<br><br>`PreMarket` - 待开盘<br><br>`RebaseSuspension` - 拆合股暂停交易<br><br>`Expired` - 已到期 (衍生品)<br><br>`Terminated` - 终止交易 |
| data.list[].preMarketQuote | object |  | 美股盘前交易数据 |
| data.list[].preMarketQuote.lastDone | string |  | 最新价 |
| data.list[].preMarketQuote.timestamp | string |  | 最新成交的时间戳（ISO 8601） |
| data.list[].preMarketQuote.volume | string |  | 成交量 |
| data.list[].preMarketQuote.turnover | string |  | 成交额 |
| data.list[].preMarketQuote.high | string |  | 最高价 |
| data.list[].preMarketQuote.low | string |  | 最低价 |
| data.list[].preMarketQuote.prevClose | string |  | 上个交易时段收盘价 |
| data.list[].postMarketQuote | object |  | 美股盘后交易数据 |
| data.list[].postMarketQuote.lastDone | string |  | 最新价 |
| data.list[].postMarketQuote.timestamp | string |  | 最新成交的时间戳（ISO 8601） |
| data.list[].postMarketQuote.volume | string |  | 成交量 |
| data.list[].postMarketQuote.turnover | string |  | 成交额 |
| data.list[].postMarketQuote.high | string |  | 最高价 |
| data.list[].postMarketQuote.low | string |  | 最低价 |
| data.list[].postMarketQuote.prevClose | string |  | 上个交易时段收盘价 |
| data.list[].overnightQuote | ['object', 'null'] |  | 美股夜盘交易数据（可能为 `null`） |
| data.list[].overnightQuote.lastDone | string |  | 最新价 |
| data.list[].overnightQuote.timestamp | string |  | 最新成交的时间戳（ISO 8601） |
| data.list[].overnightQuote.volume | string |  | 成交量 |
| data.list[].overnightQuote.turnover | string |  | 成交额 |
| data.list[].overnightQuote.high | string |  | 最高价 |
| data.list[].overnightQuote.low | string |  | 最低价 |
| data.list[].overnightQuote.prevClose | string |  | 上个交易时段收盘价 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "AAPL.US",
        "lastDone": 195.89,
        "prevClose": 192.53,
        "open": 193.41,
        "high": 195.93,
        "low": 192.05,
        "timestamp": "2024-10-16T20:00:00Z",
        "volume": 53502311,
        "turnover": 10409656210,
        "tradeStatus": "Normal",
        "preMarketQuote": {
          "lastDone": 193.5,
          "timestamp": "2024-10-17T09:00:00Z",
          "volume": 1250000.0,
          "turnover": 241875000.0,
          "high": 194,
          "low": 192.8,
          "prevClose": 192.53
        },
        "postMarketQuote": {
          "lastDone": 196.1,
          "timestamp": "2024-10-16T23:59:59Z",
          "volume": 980000.0,
          "turnover": 192178000.0,
          "high": 196.5,
          "low": 195.7,
          "prevClose": 195.89
        },
        "overnightQuote": null
      }
    ]
  }
}
```

## 获取标的逐笔明细

`GET /api/v3/stockplus/market/trade`

限频规则: 1秒内不超过10次调用，并发请求数不超过5

权限: Stock+ 行情（只读）

该接口用于获取标的的成交明细数据。

**交易类型说明**

美股交易类型：

`` ` `` (space) - 普通交易

`B` - 平均价成交

`E` - 自动执行

`H` - 价格变动交易

`I` - 碎股交易

Operation ID: `stockPlusStockQuotesGetTradeDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 标的代码，使用 `ticker.region` 格式，例如：<br><br>`AAPL.US` |
| count | query | integer | 是 | 请求的逐笔成交数量。上限：<br><br>`1000` |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 逐笔成交明细数据 |
| data[].price | string |  | 成交价 |
| data[].volume | string |  | 成交量 |
| data[].timestamp | string |  | 成交时间（ISO 8601） |
| data[].tradeType | string |  | 交易类型。见描述中的交易类型说明 |
| data[].direction | string |  | 成交方向<br><br>`Up` - 外盘<br><br>`Down` - 内盘<br><br>`Neutral` - 中性盘 |
| data[].tradeSession | string |  | 交易时段<br><br>`Intraday` - 盘中交易<br><br>`Pre` - 盘前交易<br><br>`Post` - 盘后交易<br><br>`Overnight` - 夜盘交易 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "price": 195.89,
      "volume": 100,
      "timestamp": "2024-10-16T09:30:00Z",
      "tradeType": "I",
      "direction": "Up",
      "tradeSession": "Intraday"
    },
    {
      "price": 195.88,
      "volume": 200,
      "timestamp": "2024-10-16T09:29:55Z",
      "tradeType": "I",
      "direction": "Neutral",
      "tradeSession": "Intraday"
    },
    {
      "price": 195.89,
      "volume": 150,
      "timestamp": "2024-10-16T09:29:50Z",
      "tradeType": "I",
      "direction": "Down",
      "tradeSession": "Intraday"
    }
  ]
}
```

## 创建订单

`POST /api/v3/stockplus/trade/place-order`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易读写权限

该接口用于委托下单。

Operation ID: `stockPlusOrdersPlaceOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| orderType | query | string | 是 | 订单类型<br><br>`LO` 限价单<br><br>`MO` 市价单<br><br>`LIT` 触价限价单<br><br>`MIT` 触价市价单<br><br>`TSLPAMT` 跟踪止损限价单（跟踪金额）<br><br>`TSLPPCT` 跟踪止损限价单（跟踪涨跌幅） |
| side | query | string | 是 | 买卖方向<br><br>`Buy` - 买入<br><br>`Sell` - 卖出 |
| submittedQuantity | query | string | 是 | 下单数量，例如 `100` |
| timeInForce | query | string | 是 | 订单有效期类型<br><br>`Day` - 当日有效<br><br>`GoodTilCanceled` - 撤单前有效<br><br>`GoodTilDate` - 到期前有效 |
| submittedPrice | query | string |  | 下单价格，例如 `388.5`<br><br>`LO` / `LIT` 订单必填 |
| triggerPrice | query | string |  | 触发价格，例如 `388.5`<br><br>`LIT` / `MIT` 订单必填 |
| limitOffset | query | string |  | 指定价差，例如 `1.2` 表示价差 1.2 USD（如果是美股）<br><br>`TSLPAMT` / `TSLPPCT` 订单在 `limitDepthLevel` 为 0 时必填 |
| trailingAmount | query | string |  | 跟踪金额<br><br>`TSLPAMT` 订单必填 |
| trailingPercent | query | string |  | 跟踪涨跌幅，单位为百分比，例如 `2.5` 表示 `2.5%`<br><br>`TSLPPCT` 订单必填 |
| expireDate | query | string |  | 长期单过期时间，格式为 `YYYY-MM-DD`，例如 `2022-12-05`<br><br>`timeInForce` 为 `GoodTilDate` 时必填 |
| outsideRth | query | string |  | 是否允许盘前盘后，美股必填<br><br>`RTHOnly` - 不允许盘前盘后<br><br>`AnyTime` - 允许盘前盘后<br><br>`Overnight` - 夜盘 |
| limitDepthLevel | query | number |  | 指定买卖档位，取值范围为 -5 ～ 0 ～ 5，负数代表买盘档位（如 -1 表示买一），正数代表卖盘档位（如 1 表示卖一），为 0 时 `limitOffset` 参数生效<br><br>`TSLPAMT` / `TSLPPCT` 订单有效 |
| triggerCount | query | number |  | 触发次数，取值范围 0 ~ 3，表示在 1 分钟内触发多次才会触发订单<br><br>`LIT` / `MIT` / `TSLPAMT` / `TSLPPCT` 订单有效 |
| monitorPrice | query | string |  | 监控价格，需要达到该价格才会开始监控，更新参考价<br><br>`TSLPAMT` / `TSLPPCT` 订单有效 |
| remark | query | string |  | 备注（最大 64 字符） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |
| data.symbol | string |  | 期权合约代码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "myOrder001",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## 修改订单

`POST /api/v3/stockplus/trade/modify-order`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易读写权限

该接口用于修改未成交或部分成交订单的价格/数量，语义为撤单重下（cancel & replace）。

Operation ID: `stockPlusOrdersModifyOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单 ID |
| quantity | query | string | 是 | 改单数量，例如 `200` |
| price | query | string |  | 改单价格，例如 `388.5`<br><br>`LO` / `LIT` 订单必填 |
| triggerPrice | query | string |  | 触发价格，例如 `388.5`<br><br>`LIT` / `MIT` 订单必填 |
| limitOffset | query | string |  | 指定价差<br><br>`TSLPAMT` / `TSLPPCT` 订单在 `limitDepthLevel` 为 0 时必填 |
| trailingAmount | query | string |  | 跟踪金额<br><br>`TSLPAMT` 订单必填 |
| trailingPercent | query | string |  | 跟踪涨跌幅<br><br>`TSLPPCT` 订单必填 |
| limitDepthLevel | query | number |  | 指定买卖档位。`TSLPAMT` / `TSLPPCT` 订单必填 |
| triggerCount | query | number |  | 触发次数。`LIT` / `MIT` / `TSLPAMT` / `TSLPPCT` 订单必填 |
| monitorPrice | query | string |  | 监控价格。`TSLPAMT` / `TSLPPCT` 订单必填 |
| remark | query | string |  | 备注（最大 64 字符） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 修改后的系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |
| data.symbol | string |  | 期权合约代码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## 撤销订单

`POST /api/v3/stockplus/trade/cancel-order`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易读写权限

该接口用于撤销未成交或部分成交的订单。

Operation ID: `stockPlusOrdersCancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 期权合约代码 |
| orderId | query | string |  | 系统订单 ID。与 clientOid 至少传其一；同时传入时 orderId 优先 |
| clientOid | query | string |  | 客户端自定义订单 ID。与 orderId 至少传其一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |
| data.symbol | string |  | 期权合约代码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "clientOid": "",
    "symbol": "AAPL220429C150000.US"
  }
}
```

## 查询当日订单

`GET /api/v3/stockplus/trade/today-orders`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易只读权限

该接口用于获取当日订单和订单查询。

Operation ID: `stockPlusOrdersGetTodayOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| status | query | string |  | 订单状态，例如 `status=Filled&status=New`<br><br>`NotReported` - 待报<br><br>`ReplacedNotReported` - 已修改待报<br><br>`ProtectedNotReported` - 已保护待报<br><br>`VarietiesNotReported` - 品种待报<br><br>`Filled` - 全部成交<br><br>`WaitToNew` - 等待新单<br><br>`New` - 已报<br><br>`WaitToReplace` - 等待修改<br><br>`PendingReplace` - 修改中<br><br>`Replaced` - 已修改<br><br>`PartialFilled` - 部分成交<br><br>`WaitToCancel` - 等待撤销<br><br>`PendingCancel` - 撤销中<br><br>`Rejected` - 已拒绝<br><br>`Canceled` - 已撤销<br><br>`Expired` - 已过期<br><br>`PartialWithdrawal` - 部分撤单 |
| side | query | string |  | 买卖方向<br><br>`Buy` - 买入<br><br>`Sell` - 卖出 |
| market | query | string |  | 市场<br><br>`US` - 美股 |
| orderId | query | string |  | 订单 ID，用于查询特定订单，例如 `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orders | object[] |  | 订单信息 |
| data.orders[].orderId | string |  | 订单 ID |
| data.orders[].status | string |  | 订单状态。参见上文状态枚举<br><br>`NotReported` - 待报<br><br>`ReplacedNotReported` - 已修改待报<br><br>`ProtectedNotReported` - 已保护待报<br><br>`VarietiesNotReported` - 品种待报<br><br>`Filled` - 全部成交<br><br>`WaitToNew` - 等待新单<br><br>`New` - 已报<br><br>`WaitToReplace` - 等待修改<br><br>`PendingReplace` - 修改中<br><br>`Replaced` - 已修改<br><br>`PartialFilled` - 部分成交<br><br>`WaitToCancel` - 等待撤销<br><br>`PendingCancel` - 撤销中<br><br>`Rejected` - 已拒绝<br><br>`Canceled` - 已撤销<br><br>`Expired` - 已过期<br><br>`PartialWithdrawal` - 部分撤单 |
| data.orders[].stockName | string |  | 股票名称 |
| data.orders[].quantity | string |  | 委托数量 |
| data.orders[].executedQuantity | string |  | 成交数量。未成交的订单为 `0` |
| data.orders[].price | string |  | 委托价格。市价条件单未触发时为 `null` |
| data.orders[].executedPrice | string |  | 成交价格。未成交的订单为 `null` |
| data.orders[].submittedAt | string |  | 订单提交时间（ISO 8601） |
| data.orders[].side | string |  | 买卖方向。`Buy` - 买入，`Sell` - 卖出 |
| data.orders[].symbol | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| data.orders[].orderType | string |  | 订单类型<br><br>`LO` 限价单<br><br>`MO` 市价单<br><br>`LIT` 触价限价单<br><br>`MIT` 触价市价单<br><br>`TSLPAMT` 跟踪止损限价单（跟踪金额）<br><br>`TSLPPCT` 跟踪止损限价单（跟踪涨跌幅） |
| data.orders[].lastDone | string |  | 最新成交价。未成交的订单为 `null` |
| data.orders[].triggerPrice | string |  | `LIT`/`MIT` 订单触发价格。非条件单为 `null` |
| data.orders[].msg | string |  | 拒绝原因或备注。默认空字符串 |
| data.orders[].tag | string |  | 订单标签<br><br>`Normal` - 普通订单<br><br>`GTC` - GTC 订单 |
| data.orders[].timeInForce | string |  | 订单有效期类型<br><br>`Day` - 当日有效<br><br>`GoodTilCanceled` - 撤单前有效<br><br>`GoodTilDate` - 到期前有效 |
| data.orders[].expireDate | string |  | 长期单过期时间，格式为<br><br>`YYYY-MM-DD`。非 GoodTilDate 订单为 `null` |
| data.orders[].updatedAt | string |  | 最后更新时间（ISO 8601）。未更新时为 `null` |
| data.orders[].triggerAt | string |  | 条件单触发时间（ISO 8601）。未触发时为 `null` |
| data.orders[].trailingAmount | string |  | `TSLPAMT` 订单跟踪金额。非 TSLPAMT 订单为 `null` |
| data.orders[].trailingPercent | string |  | `TSLPPCT` 订单跟踪涨跌幅。非 TSLPPCT 订单为 `null` |
| data.orders[].limitOffset | string |  | `TSLPAMT`/`TSLPPCT` 订单价差。非 TSLP 订单为 `null` |
| data.orders[].triggerStatus | string |  | 条件单触发状态。非条件单为 `null`<br><br>`NOT_USED` - 未启用<br><br>`DEACTIVE` - 已失效<br><br>`ACTIVE` - 生效中<br><br>`RELEASED` - 已触发 |
| data.orders[].currency | string |  | 结算货币 |
| data.orders[].outsideRth | string |  | 是否允许盘前盘后交易。非美股订单为 `UnknownOutsideRth`<br><br>`RTHOnly` - 不允许盘前盘后<br><br>`AnyTime` - 允许盘前盘后<br><br>`Overnight` - 夜盘 |
| data.orders[].remark | string |  | 备注 |
| data.orders[].limitDepthLevel | number |  | 指定买卖档位 |
| data.orders[].triggerCount | number |  | 触发次数 |
| data.orders[].monitorPrice | string |  | 监控价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orders": [
      {
        "orderId": "701276261045858304",
        "status": "Rejected",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 0,
        "price": 150,
        "executedPrice": null,
        "submittedAt": "2024-12-16T12:07:12Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T12:07:12Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "RTHOnly",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      }
    ]
  }
}
```

## 查询历史订单

`GET /api/v3/stockplus/trade/history-orders`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易只读权限

该接口用于获取历史订单。

Operation ID: `stockPlusOrdersGetHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| status | query | string |  | 订单状态，例如 `status=Filled&status=New`<br><br>`NotReported` - 待报<br><br>`ReplacedNotReported` - 已修改待报<br><br>`ProtectedNotReported` - 已保护待报<br><br>`VarietiesNotReported` - 品种待报<br><br>`Filled` - 全部成交<br><br>`WaitToNew` - 等待新单<br><br>`New` - 已报<br><br>`WaitToReplace` - 等待修改<br><br>`PendingReplace` - 修改中<br><br>`Replaced` - 已修改<br><br>`PartialFilled` - 部分成交<br><br>`WaitToCancel` - 等待撤销<br><br>`PendingCancel` - 撤销中<br><br>`Rejected` - 已拒绝<br><br>`Canceled` - 已撤销<br><br>`Expired` - 已过期<br><br>`PartialWithdrawal` - 部分撤单 |
| side | query | string |  | 买卖方向。`Buy` - 买入，`Sell` - 卖出 |
| market | query | string |  | 市场。`US` - 美股 |
| startAt | query | number |  | 开始时间，单位为秒级时间戳，例如 `1650410999`。默认为结束时间或当前时间前 90 天 |
| endAt | query | number |  | 结束时间，单位为秒级时间戳，例如 `1650410999`。默认为开始时间或当前时间后 90 天 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasMore | boolean |  | 是否有更多数据。每次最多返回 1000 条订单；超过 1000 条时 hasMore 为 true |
| data.orders | object[] |  | 订单信息 |
| data.orders[].orderId | string |  | 订单 ID |
| data.orders[].status | string |  | 订单状态。参见上文状态枚举<br><br>`NotReported` - 待报<br><br>`ReplacedNotReported` - 已修改待报<br><br>`ProtectedNotReported` - 已保护待报<br><br>`VarietiesNotReported` - 品种待报<br><br>`Filled` - 全部成交<br><br>`WaitToNew` - 等待新单<br><br>`New` - 已报<br><br>`WaitToReplace` - 等待修改<br><br>`PendingReplace` - 修改中<br><br>`Replaced` - 已修改<br><br>`PartialFilled` - 部分成交<br><br>`WaitToCancel` - 等待撤销<br><br>`PendingCancel` - 撤销中<br><br>`Rejected` - 已拒绝<br><br>`Canceled` - 已撤销<br><br>`Expired` - 已过期<br><br>`PartialWithdrawal` - 部分撤单 |
| data.orders[].stockName | string |  | 股票名称 |
| data.orders[].quantity | string |  | 委托数量 |
| data.orders[].executedQuantity | string |  | 成交数量。未成交的订单为 `0` |
| data.orders[].price | string |  | 委托价格。市价条件单未触发时为 `null` |
| data.orders[].executedPrice | string |  | 成交价格。未成交的订单为 `null` |
| data.orders[].submittedAt | string |  | 订单提交时间（ISO 8601） |
| data.orders[].side | string |  | 买卖方向。`Buy` - 买入，`Sell` - 卖出 |
| data.orders[].symbol | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| data.orders[].orderType | string |  | 订单类型<br><br>`LO` 限价单<br><br>`MO` 市价单<br><br>`LIT` 触价限价单<br><br>`MIT` 触价市价单<br><br>`TSLPAMT` 跟踪止损限价单（跟踪金额）<br><br>`TSLPPCT` 跟踪止损限价单（跟踪涨跌幅） |
| data.orders[].lastDone | string |  | 最新成交价。未成交的订单为 `null` |
| data.orders[].triggerPrice | string |  | `LIT`/`MIT` 订单触发价格。非条件单为 `null` |
| data.orders[].msg | string |  | 拒绝原因或备注。默认空字符串 |
| data.orders[].tag | string |  | 订单标签<br><br>`Normal` - 普通订单<br><br>`GTC` - GTC 订单 |
| data.orders[].timeInForce | string |  | 订单有效期类型<br><br>`Day` - 当日有效<br><br>`GoodTilCanceled` - 撤单前有效<br><br>`GoodTilDate` - 到期前有效 |
| data.orders[].expireDate | string |  | 长期单过期时间，格式为<br><br>`YYYY-MM-DD`。非 GoodTilDate 订单为 `null` |
| data.orders[].updatedAt | string |  | 最后更新时间（ISO 8601）。未更新时为 `null` |
| data.orders[].triggerAt | string |  | 条件单触发时间（ISO 8601）。未触发时为 `null` |
| data.orders[].trailingAmount | string |  | `TSLPAMT` 订单跟踪金额。非 TSLPAMT 订单为 `null` |
| data.orders[].trailingPercent | string |  | `TSLPPCT` 订单跟踪涨跌幅。非 TSLPPCT 订单为 `null` |
| data.orders[].limitOffset | string |  | `TSLPAMT`/`TSLPPCT` 订单价差。非 TSLP 订单为 `null` |
| data.orders[].triggerStatus | string |  | 条件单触发状态。非条件单为 `null`<br><br>`NOT_USED` - 未启用<br><br>`DEACTIVE` - 已失效<br><br>`ACTIVE` - 生效中<br><br>`RELEASED` - 已触发 |
| data.orders[].currency | string |  | 结算货币 |
| data.orders[].outsideRth | string |  | 是否允许盘前盘后交易。非美股订单为 `UnknownOutsideRth`<br><br>`RTHOnly` - 不允许盘前盘后<br><br>`AnyTime` - 允许盘前盘后<br><br>`Overnight` - 夜盘 |
| data.orders[].remark | string |  | 备注 |
| data.orders[].limitDepthLevel | number |  | 指定买卖档位 |
| data.orders[].triggerCount | number |  | 触发次数 |
| data.orders[].monitorPrice | string |  | 监控价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "hasMore": false,
    "orders": [
      {
        "orderId": "701276261045858304",
        "status": "Canceled",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 0,
        "price": 150,
        "executedPrice": null,
        "submittedAt": "2024-12-16T12:07:12Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T12:07:23Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "RTHOnly",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      },
      {
        "orderId": "701276261045858305",
        "status": "Filled",
        "stockName": "Apple Inc.",
        "quantity": 1,
        "executedQuantity": 1,
        "price": 80,
        "executedPrice": 10,
        "submittedAt": "2024-12-16T10:00:00Z",
        "side": "Buy",
        "symbol": "AAPL.US",
        "orderType": "LO",
        "lastDone": null,
        "triggerPrice": null,
        "msg": "",
        "tag": "Normal",
        "timeInForce": "Day",
        "expireDate": "2024-12-16",
        "updatedAt": "2024-12-16T10:00:01Z",
        "triggerAt": null,
        "trailingAmount": null,
        "trailingPercent": null,
        "limitOffset": null,
        "triggerStatus": null,
        "currency": "USD",
        "outsideRth": "AnyTime",
        "limitDepthLevel": null,
        "triggerCount": null,
        "monitorPrice": null
      }
    ]
  }
}
```

## 查询订单详情

`GET /api/v3/stockplus/trade/order-detail`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易只读权限

该接口用于订单详情查询。

Operation ID: `stockPlusOrdersGetOrderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单 ID，例如 `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单 ID |
| data.status | string |  | 订单状态<br><br>`NotReported` - 待报<br><br>`ReplacedNotReported` - 已修改待报<br><br>`ProtectedNotReported` - 已保护待报<br><br>`VarietiesNotReported` - 品种待报<br><br>`Filled` - 全部成交<br><br>`WaitToNew` - 等待新单<br><br>`New` - 已报<br><br>`WaitToReplace` - 等待修改<br><br>`PendingReplace` - 修改中<br><br>`Replaced` - 已修改<br><br>`PartialFilled` - 部分成交<br><br>`WaitToCancel` - 等待撤销<br><br>`PendingCancel` - 撤销中<br><br>`Rejected` - 已拒绝<br><br>`Canceled` - 已撤销<br><br>`Expired` - 已过期<br><br>`PartialWithdrawal` - 部分撤单 |
| data.stockName | string |  | 股票名称 |
| data.quantity | string |  | 委托数量 |
| data.executedQuantity | string |  | 成交数量。未成交的订单为 `"0"` |
| data.price | string |  | 委托价格。市价条件单未触发时为 `null` |
| data.executedPrice | string |  | 成交价格。未成交的订单为 `null` |
| data.submittedAt | string |  | 订单提交时间 |
| data.side | string |  | 买卖方向。`Buy` - 买入，`Sell` - 卖出 |
| data.symbol | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| data.orderType | string |  | 订单类型<br><br>`LO` 限价单<br><br>`MO` 市价单<br><br>`LIT` 触价限价单<br><br>`MIT` 触价市价单<br><br>`TSLPAMT` 跟踪止损限价单（跟踪金额）<br><br>`TSLPPCT` 跟踪止损限价单（跟踪涨跌幅） |
| data.lastDone | string |  | 最新成交价。未成交的订单为 `null` |
| data.triggerPrice | string |  | `LIT`/`MIT` 订单触发价格。非条件单为 `null` |
| data.msg | string |  | 拒绝原因或备注。默认空字符串 |
| data.tag | string |  | 订单标签<br><br>`Normal` - 普通订单<br><br>`GTC` - GTC 订单 |
| data.timeInForce | string |  | 订单有效期类型<br><br>`Day` - 当日有效<br><br>`GoodTilCanceled` - 撤单前有效<br><br>`GoodTilDate` - 到期前有效 |
| data.expireDate | string |  | 长期单过期时间，格式为 `YYYY-MM-DD`。非 GTD 订单为空 |
| data.updatedAt | string |  | 最后更新时间（ISO 8601）。未更新时为 `null` |
| data.triggerAt | string |  | 条件单触发时间，单位为（ISO 8601） |
| data.trailingAmount | string |  | `TSLPAMT` 订单跟踪金额。非 TSLPAMT 订单为 `null` |
| data.trailingPercent | string |  | `TSLPPCT` 订单跟踪涨跌幅。非 TSLPPCT 订单为 `null` |
| data.limitOffset | string |  | `TSLPAMT`/`TSLPPCT` 订单价差。非 TSLP 订单为 `null` |
| data.triggerStatus | string |  | 条件单触发状态。非条件单为 `null`<br><br>`NOT_USED` - 未启用<br><br>`DEACTIVE` - 已失效<br><br>`ACTIVE` - 生效中<br><br>`RELEASED` - 已触发 |
| data.currency | string |  | 结算货币 |
| data.outsideRth | string |  | 是否允许盘前盘后交易。非美股订单为 `UnknownOutsideRth`<br><br>`RTHOnly` - 不允许盘前盘后<br><br>`AnyTime` - 允许盘前盘后<br><br>`Overnight` - 夜盘 |
| data.remark | string |  | 备注 |
| data.limitDepthLevel | number |  | 指定买卖档位 |
| data.triggerCount | number |  | 触发次数 |
| data.monitorPrice | string |  | 监控价格 |
| data.freeStatus | string |  | 免佣状态。默认 `None`<br><br>`None` - 无<br><br>`Calculated` - 待计算<br><br>`Pending` - 待发放<br><br>`Ready` - 已发放 |
| data.freeAmount | string |  | 免佣金额。默认 `null` |
| data.freeCurrency | string |  | 免佣币种。默认 `null` |
| data.deductionsStatus | string |  | 扣款/返佣状态。默认 `None`<br><br>`None` - 待结算/无数据<br><br>`Pending` - 已结算，待发放<br><br>`Done` - 已结算，已发放 |
| data.deductionsAmount | string |  | 扣款金额。默认 `null` |
| data.deductionsCurrency | string |  | 扣款币种。默认 `null` |
| data.platformDeductedStatus | string |  | 平台费扣款/返佣状态。默认 `None`<br><br>`None` - 待结算/无数据<br><br>`Pending` - 已结算，待发放<br><br>`Done` - 已结算，已发放 |
| data.platformDeductedAmount | string |  | 平台费扣款金额。默认 `null` |
| data.platformDeductedCurrency | string |  | 平台费扣款币种。默认 `null` |
| data.history | object[] |  | 订单历史详情 |
| data.history[].price | number |  | 交易展示价格（成交时），提交价格（过期/撤销/拒绝时） |
| data.history[].quantity | number |  | 交易展示数量（成交时），剩余数量（过期/撤销/拒绝时） |
| data.history[].status | string |  | 订单状态 |
| data.history[].msg | string |  | 交易或错误信息 |
| data.history[].time | string |  | 发生时间 |
| data.chargeDetail | object |  | 订单费用 |
| data.chargeDetail.totalAmount | number |  | 总费用 |
| data.chargeDetail.currency | string |  | 结算货币 |
| data.chargeDetail.items | object[] |  | 订单费用明细 |
| data.chargeDetail.items[].code | string |  | 费用类别编码<br><br>`Broker`<br><br>`Third` |
| data.chargeDetail.items[].name | string |  | 费用类别名称 |
| data.chargeDetail.items[].fees | object[] |  | 费用明细 |
| data.chargeDetail.items[].fees[].code | string |  | 费用项编码 |
| data.chargeDetail.items[].fees[].name | string |  | 费用项名称 |
| data.chargeDetail.items[].fees[].amount | number |  | 单项费用金额 |
| data.chargeDetail.items[].fees[].currency | string |  | 费用币种 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "701276261045858304",
    "status": "Filled",
    "stockName": "Apple Inc.",
    "quantity": 1,
    "executedQuantity": 0,
    "price": 150,
    "executedPrice": null,
    "submittedAt": "2024-12-16T12:07:12Z",
    "side": "Buy",
    "symbol": "AAPL.US",
    "orderType": "LO",
    "lastDone": null,
    "triggerPrice": null,
    "msg": "",
    "tag": "Normal",
    "timeInForce": "Day",
    "expireDate": "2024-12-16",
    "updatedAt": null,
    "triggerAt": null,
    "trailingAmount": null,
    "trailingPercent": null,
    "limitOffset": null,
    "triggerStatus": null,
    "currency": "USD",
    "outsideRth": "RTHOnly",
    "remark": "remark from Java SDK",
    "limitDepthLevel": null,
    "triggerCount": null,
    "monitorPrice": null,
    "freeStatus": "None",
    "freeAmount": null,
    "freeCurrency": null,
    "deductionsStatus": "None",
    "deductionsAmount": null,
    "deductionsCurrency": null,
    "platformDeductedStatus": "None",
    "platformDeductedAmount": null,
    "platformDeductedCurrency": null,
    "history": [
      {
        "price": 10,
        "quantity": 1,
        "status": "Filled",
        "msg": "",
        "time": "2024-12-16T12:07:12Z"
      },
      {
        "price": 80,
        "quantity": 1,
        "status": "New",
        "msg": "",
        "time": "2024-12-16T12:06:55Z"
      }
    ],
    "chargeDetail": {
      "totalAmount": 0,
      "currency": "USD",
      "items": [
        {
          "code": "Broker",
          "name": "Broker Fees",
          "fees": []
        },
        {
          "code": "Third",
          "name": "Third-party Fees",
          "fees": []
        }
      ]
    }
  }
}
```

## 预估最大购买数量

`GET /api/v3/stockplus/trade/max-purchase`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

该接口用于查询股票、期权的预估最大可购买数量。

注意：该接口目前仅对白名单用户开放（需已完成证券开户），请联系 BD 申请开通白名单权限。

Operation ID: `stockPlusOrdersEstimateMaxPurchase`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| orderType | query | string | 是 | 订单类型<br><br>`LO` 限价单<br><br>`MO` 市价单<br><br>`LIT` 触价限价单<br><br>`MIT` 触价市价单<br><br>`TSLPAMT` 跟踪止损限价单（跟踪金额）<br><br>`TSLPPCT` 跟踪止损限价单（跟踪涨跌幅） |
| price | query | string |  | 预估下单价格，例如 `388.5` |
| side | query | string | 是 | 买卖方向<br><br>`Buy` - 买入<br><br>`Sell` - 卖出，卖出查询仅支持美股卖空场景 |
| currency | query | string |  | 结算货币 |
| orderId | query | string |  | 订单 ID，获取改单预估最大购买数量时必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cashMaxQty | string |  | 现金可买数量，默认为空字符串 |
| data.marginMaxQty | string |  | 融资可买数量，默认为空字符串 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "cashMaxQty": "100",
    "marginMaxQty": "300"
  }
}
```

## 查询当日成交

`GET /api/v3/stockplus/trade/today-executions`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易只读权限

该接口用于获取当日订单的成交明细。

Operation ID: `stockPlusOrdersGetTodayExecutions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| orderId | query | string |  | 订单 ID，用于指定订单 ID 查询，例如 `701276261045858304` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trades | object[] |  | 成交明细信息 |
| data.trades[].orderId | string |  | 订单 ID |
| data.trades[].tradeId | string |  | 成交 ID |
| data.trades[].symbol | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| data.trades[].tradeDoneAt | string |  | 成交时间（ISO 8601） |
| data.trades[].quantity | number |  | 成交数量 |
| data.trades[].price | number |  | 成交价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "trades": [
      {
        "orderId": "701276261045858304",
        "tradeId": "0f40217c-a73c-410d-b599-2ff6a9ee762e",
        "symbol": "AAPL.US",
        "tradeDoneAt": "2024-12-16T12:07:12Z",
        "quantity": 1,
        "price": 150
      }
    ]
  }
}
```

## 查询历史成交

`GET /api/v3/stockplus/trade/history-executions`

限频规则: 30秒内累计不超过30次调用，且每两次调用之间间隔不小于0.02秒

权限: 统一账户交易只读权限

该接口用于获取历史订单的成交明细，包括买入和卖出的成交记录，不支持当日成交明细查询。

Operation ID: `stockPlusOrdersGetHistoryExecutions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| startAt | query | number |  | 开始时间，格式为时间戳（秒），例如 `1650410999`。默认取结束时间或当前时间的前 90 天 |
| endAt | query | number |  | 结束时间，格式为时间戳（秒），例如 `1650410999`。默认取开始时间或当前时间的后 90 天 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasMore | boolean |  | 是否存在更多数据。单次查询最大 1000 笔成交记录，超出时 hasMore 为 true |
| data.trades | object[] |  | 成交明细信息 |
| data.trades[].orderId | string |  | 订单 ID |
| data.trades[].tradeId | string |  | 成交 ID |
| data.trades[].symbol | string |  | 股票代码，使用 `ticker.region` 格式，例如 `AAPL.US` |
| data.trades[].tradeDoneAt | string |  | 成交时间（ISO 8601） |
| data.trades[].quantity | number |  | 成交数量 |
| data.trades[].price | number |  | 成交价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "hasMore": false,
    "trades": [
      {
        "orderId": "701276261045858304",
        "tradeId": "0f40217c-a73c-410d-b599-2ff6a9ee762e",
        "symbol": "AAPL.US",
        "tradeDoneAt": "2024-12-16T12:07:12Z",
        "quantity": 1,
        "price": 150
      }
    ]
  }
}
```

## 资金划转

`POST /api/v3/stockplus/asset/transfer`

限频规则: 5次/秒/UID

权限: 统一账户管理权限（读写）

该接口用于Stock+账户出入金。

Operation ID: `stockPlusAssetsTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 划转币种<br><br>本期支持USDC及USD |
| amount | query | string |  | 划转数量 |
| direction | query | string |  | 划转方向<br><br>`in` - 入金到Stock+账户<br><br>`out` - 从Stock+账户出金<br><br>当前仅支持现货账户与证券账户互转 |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "123456789"
  }
}
```

## 获取划转记录

`GET /api/v3/stockplus/asset/transfer-records`

限频规则: 10次/秒/UID

权限: 统一账户管理权限（只读）

该接口用于查询Stock+账户出入金记录。

Operation ID: `stockPlusAssetsGetTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| transferId | query | string |  | 划转ID |
| startTime | query | string |  | 开始时间，格式为时间戳（毫秒） |
| endTime | query | string |  | 结束时间，格式为时间戳（毫秒） |
| limit | query | string |  | 每页条数 |
| cursor | query | string |  | 游标ID |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转ID |
| data.coin | string |  | 划转币种<br><br>本期支持USDC及USD |
| data.amount | string |  | 划转数量 |
| data.direction | string |  | 划转方向<br><br>`in` - 入金到Stock+账户<br><br>`out` - 从Stock+账户出金 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "123456789",
    "coin": "USDC",
    "amount": "100.00",
    "direction": "in",
    "cursor": "abc123"
  }
}
```

## 查询账户资金

`GET /api/v3/stockplus/asset/account`

权限: 统一账户管理权限（只读）

该接口用于获取用户每个币种可用、可取、冻结、待结算金额、在途资金（基金申购赎回）信息。

Operation ID: `stockPlusAssetsGetAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| currency | query | string |  | 币种（USD、CNH） |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 账户资金信息 |
| data.list[].totalCash | number |  | 总现金 |
| data.list[].maxFinanceAmount | number |  | 最大融资额 |
| data.list[].remainingFinanceAmount | number |  | 剩余可融资额 |
| data.list[].riskLevel | number |  | 风控等级<br><br>`0` - 安全<br><br>`1` - 中度风险<br><br>`2` - 预警<br><br>`3` - 危险 |
| data.list[].marginCall | number |  | 追保金额 |
| data.list[].netAssets | number |  | 净资产 |
| data.list[].initMargin | number |  | 初始保证金 |
| data.list[].maintenanceMargin | number |  | 维持保证金 |
| data.list[].currency | string |  | 币种 |
| data.list[].buyPower | number |  | 购买力 |
| data.list[].cashInfos | object[] |  | 现金明细 |
| data.list[].cashInfos[].withdrawCash | number |  | 可提取金额 |
| data.list[].cashInfos[].availableCash | number |  | 可用金额 |
| data.list[].cashInfos[].frozenCash | number |  | 冻结金额 |
| data.list[].cashInfos[].settlingCash | number |  | 待结算金额 |
| data.list[].cashInfos[].currency | string |  | 币种 |
| data.list[].frozenTransactionFees | object[] |  | 冻结手续费（可能为空数组） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "totalCash": 13.88,
        "maxFinanceAmount": 0,
        "remainingFinanceAmount": 13.88,
        "riskLevel": 0,
        "marginCall": 0,
        "netAssets": 13.88,
        "initMargin": 0,
        "maintenanceMargin": 0,
        "currency": "USD",
        "buyPower": 13.88,
        "cashInfos": [
          {
            "withdrawCash": 13.88,
            "availableCash": 13.88,
            "frozenCash": 0,
            "settlingCash": 0,
            "currency": "USD"
          }
        ],
        "frozenTransactionFees": []
      }
    ]
  }
}
```

## 查询资金流水

`GET /api/v3/stockplus/asset/cash-flow`

权限: 统一账户管理权限（只读）

该接口用于获取资金流入/流出方向、资金类别、资金金额、发生时间、关联股票代码和资金流水说明信息。

Operation ID: `stockPlusAssetsGetCashFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | number | 是 | 开始时间，时间戳（秒），例如：<br><br>`1650037563` |
| endTime | query | number | 是 | 结束时间，时间戳（秒），例如：<br><br>`1650747581` |
| businessType | query | string |  | 资金类别<br><br>`Cash` - 现金<br><br>`Stock` - 股票<br><br>`Fund` - 基金 |
| symbol | query | string |  | 股票代码，例如：<br><br>`AAPL.US` |
| page | query | number |  | 起始页码。默认：<br><br>`1`。范围：<br><br>`>=1` |
| size | query | number |  | 每页条数。默认：<br><br>`50`。范围：<br><br>`1~10000` |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 资金流水信息 |
| data.list[].transactionFlowName | string |  | 流水名称 |
| data.list[].direction | string |  | 方向<br><br>`In` - 流入<br><br>`Out` - 流出 |
| data.list[].businessType | string |  | 资金类别<br><br>`Cash` - 现金<br><br>`Stock` - 股票<br><br>`Fund` - 基金 |
| data.list[].balance | number |  | 金额 |
| data.list[].currency | string |  | 币种 |
| data.list[].businessTime | string |  | 业务时间（ISO 8601） |
| data.list[].symbol | string |  | 关联股票代码（可能为 `null`） |
| data.list[].description | string |  | 资金流水说明（可能为空字符串） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transactionFlowName": "买入 AAPL.US",
        "direction": "Out",
        "businessType": "Unknown",
        "balance": -1500,
        "currency": "USD",
        "businessTime": "2024-12-16T10:00:00Z",
        "symbol": "AAPL.US",
        "description": "买入10股AAPL.US"
      },
      {
        "transactionFlowName": "Deposit Cash",
        "direction": "In",
        "businessType": "Unknown",
        "balance": 100000.0,
        "currency": "USD",
        "businessTime": "2024-12-15T06:10:57Z",
        "symbol": null,
        "description": ""
      }
    ]
  }
}
```

## 查询股票持仓

`GET /api/v3/stockplus/asset/stock-position`

权限: 统一账户管理权限（只读）

该接口用于获取包括账户、股票代码、持仓股数、可用股数、持仓均价（按账户设置计算均价方式）、币种在内的股票持仓信息。

Operation ID: `stockPlusAssetsGetStockPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 股票代码列表，使用 `ticker.region` 格式，多个用 `,` 分隔，例如：<br><br>`AAPL.US,MSTR.US` |

### 响应 200：请求成功

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.channels | object[] |  | 账户通道列表 |
| data.channels[].accountChannel | string |  | 账户通道 |
| data.channels[].positions | object[] |  | 持仓列表 |
| data.channels[].positions[].symbol | string |  | 股票代码 |
| data.channels[].positions[].symbolName | string |  | 股票名称 |
| data.channels[].positions[].quantity | number |  | 持仓股数 |
| data.channels[].positions[].availableQuantity | number |  | 可用股数 |
| data.channels[].positions[].currency | string |  | 币种 |
| data.channels[].positions[].costPrice | number |  | 持仓均价（按客户端的平均买入成本或摊薄成本设置计算） |
| data.channels[].positions[].market | string |  | 市场 |
| data.channels[].positions[].initQuantity | number |  | 开盘前初始持仓数 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "channels": [
      {
        "accountChannel": "sg_bitget_uat",
        "positions": [
          {
            "symbol": "AAPL.US",
            "symbolName": "Apple Inc.",
            "quantity": 100,
            "availableQuantity": 80,
            "currency": "USD",
            "costPrice": 145.5,
            "market": "US",
            "initQuantity": 100
          }
        ]
      }
    ]
  }
}
```