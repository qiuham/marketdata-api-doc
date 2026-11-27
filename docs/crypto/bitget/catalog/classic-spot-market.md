---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-market
api_type: REST
updated_at: 2026-11-27 19:02:48.689191
---

# Classic Spot Market API

Spot market data endpoints — symbols, tickers, order book, candles, trades, and coin info.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/public/symbols` — Get Symbol Info
- `GET /api/v2/spot/public/coins` — Get Coin Info
- `GET /api/v2/spot/market/tickers` — Get Ticker Information
- `GET /api/v2/spot/market/orderbook` — Get OrderBook Depth
- `GET /api/v2/spot/market/merge-depth` — Get Merge Depth
- `GET /api/v2/spot/market/fills` — Get Recent Trades
- `GET /api/v2/spot/market/fills-history` — Get Market Trades
- `GET /api/v2/spot/market/candles` — Get Candlestick Data
- `GET /api/v2/spot/market/history-candles` — Get History Candlestick Data
- `GET /api/v2/spot/market/auction` — Get Call Auction information
- `GET /api/v2/spot/market/vip-fee-rate` — Get VIP Fee Rate

## Get Symbol Info

`GET /api/v2/spot/public/symbols`

Frequency limit: 20 times/1s (IP)

Get spot trading pair information,supporting both individual and full queries

Operation ID: `classicSpotMarketGetSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | trading pair name, e.g. BTCUSDT. If the field is left blank, all trading pair information will be returned by default |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].baseCoin | string |  | Base currency, e.g. "BTC" in the pair "BTCUSDT". |
| data[].quoteCoin | string |  | Quoting currency, e.g. "USDT" in the trading pair "BTCUSDT". |
| data[].minTradeAmount | string |  | Minimum order(obsolete). Please refer to `minTradeUSDT` |
| data[].maxTradeAmount | string |  | Maximum order(obsolete). The maximum quantity is generally unlimited |
| data[].takerFeeRate | string |  | Default taker transaction fee, can be overridden by individual transaction fee |
| data[].makerFeeRate | string |  | Default maker transaction fee, can be overridden by individual transaction fee |
| data[].pricePrecision | string |  | Pricing precision |
| data[].quantityPrecision | string |  | Amount precision |
| data[].quotePrecision | string |  | Quote coin precision |
| data[].minTradeUSDT | string |  | Minimum trading volume (USDT) |
| data[].status | string |  | Symbol status. `offline`: offline / `gray`: grey scale / `online`: normal / `halt`: suspend trading |
| data[].buyLimitPriceRatio | string |  | Percentage spread between bid and ask, in decimal form. E.g. 0.05 means 5% |
| data[].sellLimitPriceRatio | string |  | Percentage spread between sell and current price, in decimal form. E.g. 0.05 means 5% |
| data[].orderQuantity | string |  | The maximum number of orders allowed for the current symbol |
| data[].areaSymbol | string |  | Area symbol. `yes`, `no` |
| data[].maxLimitOrderValue | string |  | Maximum single limit order value. Unit: USDT |
| data[].maxMarketOrderValue | string |  | Maximum single market order value. Unit: USDT |
| data[].offTime | string |  | Symbol off time, e.g: 1744797600000 |
| data[].openTime | string |  | This field has been deprecated |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744276707885,
  "data": [
    {
      "symbol": "BTCUSDT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "minTradeAmount": "0",
      "maxTradeAmount": "900000000000000000000",
      "takerFeeRate": "0.002",
      "makerFeeRate": "0.002",
      "pricePrecision": "2",
      "quantityPrecision": "6",
      "quotePrecision": "8",
      "status": "online",
      "minTradeUSDT": "1",
      "buyLimitPriceRatio": "0.05",
      "sellLimitPriceRatio": "0.05",
      "areaSymbol": "no",
      "maxLimitOrderValue": "500000",
      "maxMarketOrderValue": "50000",
      "orderQuantity": "200",
      "openTime": "1532454360000",
      "offTime": ""
    }
  ]
}
```

## Get Coin Info

`GET /api/v2/spot/public/coins`

Frequency limit: 3 times/1s (IP)

Get spot coin information,supporting both individual and full queries.

Operation ID: `classicSpotMarketGetCoinList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name, If the field is left blank, all coin information will be returned by default |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coinId | string |  | Currency ID |
| data[].coin | string |  | Token name |
| data[].transfer | string |  | Transferability |
| data[].chains | object[] |  | Support chain list |
| data[].chains[].chain | string |  | Chain name |
| data[].chains[].needTag | string |  | Need tag |
| data[].chains[].withdrawable | string |  | Withdrawal supported |
| data[].chains[].rechargeable | string |  | Deposit supported |
| data[].chains[].withdrawFee | string |  | Withdrawal transaction fee |
| data[].chains[].extraWithdrawFee | string |  | Extra charge. On chain destruction: `0.1` means `10%` |
| data[].chains[].depositConfirm | string |  | Deposit confirmation blocks |
| data[].chains[].withdrawConfirm | string |  | Withdrawal confirmation blocks |
| data[].chains[].minDepositAmount | string |  | Minimum deposit amount |
| data[].chains[].minWithdrawAmount | string |  | Minimum withdrawal amount |
| data[].chains[].browserUrl | string |  | Blockchain explorer address |
| data[].chains[].contractAddress | string |  | coin contract address |
| data[].chains[].withdrawStep | string |  | withdrawal count step. If the value is not 0, it indicates that the withdrawal size should be multiple of the value. if it's 0, that means there is no the limit above. |
| data[].chains[].withdrawMinScale | string |  | Decimal places of withdrawal amount |
| data[].chains[].congestion | string |  | chain network status. `normal`: normal / `congested`: congestion |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    {
      "coinId": "1",
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

## Get Ticker Information

`GET /api/v2/spot/market/tickers`

Frequency limit: 20 times/1s (IP)

Get Ticker Information,Supports both single and batch queries

Operation ID: `classicSpotMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | trading pair name, e.g. BTCUSDT. If the field is left blank, all trading pair information will be returned by default |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].high24h | string |  | 24h highest price |
| data[].open | string |  | 24h open price |
| data[].lastPr | string |  | Latest price |
| data[].low24h | string |  | 24h lowest price |
| data[].quoteVolume | string |  | Trading volume in quote currency |
| data[].baseVolume | string |  | Trading volume in base currency |
| data[].usdtVolume | string |  | Trading volume in USDT |
| data[].bidPr | string |  | Bid 1 price |
| data[].askPr | string |  | Ask 1 price |
| data[].bidSz | string |  | Buying 1 amount |
| data[].askSz | string |  | selling 1 amount |
| data[].openUtc | string |  | UTC±00:00 Entry price |
| data[].ts | string |  | Current time Unix millisecond timestamp, e.g. 1690196141868 |
| data[].changeUtc24h | string |  | Change at UTC+0, 0.01 means 1%. |
| data[].change24h | string |  | 24-hour change, 0.01 means 1%. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "symbol": "BTCUSDT",
      "high24h": "37775.65",
      "open": "35134.2",
      "low24h": "34413.1",
      "lastPr": "34413.1",
      "quoteVolume": "0",
      "baseVolume": "0",
      "usdtVolume": "0",
      "bidPr": "0",
      "askPr": "0",
      "bidSz": "0.0663",
      "askSz": "0.0119",
      "openUtc": "23856.72",
      "ts": "1625125755277",
      "changeUtc24h": "0.00301",
      "change24h": "0.00069"
    }
  ]
}
```

## Get OrderBook Depth

`GET /api/v2/spot/market/orderbook`

Frequency limit: 20 times/1s (IP)

Get OrderBook Depth<br/>You can download historical spot depth data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketGetOrderbook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| type | query | string |  | Default：step0： The value enums：step0，step1，step2，step3，step4，step5 |
| limit | query | string |  | Number of queries: Default: 150, maximum: 150 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | string[][] |  | Ask depth. e.g. ["38084.5","0.5"]，"38084.5" is price，"0.5" is base coin volume |
| data.bids | string[][] |  | Bid depth |
| data.ts | string |  | Matching engine timestamp(ms), e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698303884579,
  "data": {
    "asks": [
      [
        "34567.15",
        "0.0131"
      ],
      [
        "34567.25",
        "0.0144"
      ]
    ],
    "bids": [
      [
        "34567",
        "0.2917"
      ],
      [
        "34566.85",
        "0.0145"
      ]
    ],
    "ts": "1698303884584"
  }
}
```

## Get Merge Depth

`GET /api/v2/spot/market/merge-depth`

Frequency limit: 20 times/1s (IP)

Get Merge Depth<br/>You can download historical spot depth data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketMergeOrderbook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| precision | query | string |  | Price precision, return the cumulative depth according to the selected precision as the step size, enumeration value: scale0/scale1/scale2/scale3, scale0 does not merge, the default value, generally speaking, scale1 is the merged depth of the trading pair quotation accuracy * 10, generally under normal circumstances, scale2 is the quotation accuracy * 100. Under normal circumstances, scale3 is the quotation accuracy * 1000. Under normal circumstances, the accuracy corresponding to 0/1/2/3 is based on the actual return parameter "scale". Each trading pair the quotation accuracy is different. Some currency pairs do not have scale 2. Requests for scales that do not exist for the currency pair will be processed according to the maximum scale. Example: A certain trading pair only has scale 0/1, and when scale2 is requested, it is automatically reduced to scale1. |
| limit | query | string |  | Fixed gear enumeration value：1/5/15/50/max，default:100，When the actual depth does not meet the limit, return according to the actual gear, and pass in max to return the maximum gear of the trading pair. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | array[] |  | Ask depth. e.g. [38084.5, 0.5]，38084.5 is price，0.5 is base coin volume |
| data.bids | array[] |  | Bid depth |
| data.precision | string |  | Current gear, e.g. "scale1" |
| data.scale | string |  | Actual precision value, e.g. "0.1" |
| data.isMaxPrecision | string |  | Is max precision. YES:yes / NO:no |
| data.ts | string |  | Matching engine timestamp(ms), e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "asks": [
      [
        38084.5,
        0.0039
      ],
      [
        38085.7,
        0.0018
      ],
      [
        38086.7,
        0.031
      ],
      [
        38088.2,
        0.5303
      ]
    ],
    "bids": [
      [
        38073.7,
        0.4993
      ],
      [
        38073.4,
        0.45
      ],
      [
        38073.3,
        0.1179
      ],
      [
        38071.5,
        0.2162
      ]
    ],
    "ts": "1622102974025",
    "scale": "0.1",
    "precision": "scale0",
    "isMaxPrecision": "YES"
  }
}
```

## Get Recent Trades

`GET /api/v2/spot/market/fills`

Frequency limit: 10 times/1s (IP)

Get Recent Trades<br/>You can download historical spot trades data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketGetRecentTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name, e.g. BTCUSDT |
| limit | query | string |  | Default: 100, maximum: 500 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].tradeId | string |  | Order ID. Descending |
| data[].side | string |  | Direction. Buy / Sell |
| data[].price | string |  | Order price |
| data[].size | string |  | Filled quantity |
| data[].ts | string |  | Transaction time, Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "symbol": "BFTUSDT",
      "tradeId": "1",
      "side": "buy",
      "price": "2.38735",
      "size": "2470.6224",
      "ts": "1622097282536"
    },
    {
      "symbol": "BFTUSDT",
      "tradeId": "2",
      "side": "sell",
      "price": "2.38649",
      "size": "3239.7976",
      "ts": "1622097280642"
    }
  ]
}
```

## Get Market Trades

`GET /api/v2/spot/market/fills-history`

Rate limit: 10 req/sec/IP

Get Market Trades. - The time interval between startTime and endTime should not exceed 7 days. - It supports to get the data within 90days. You can download the older data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketGetMarketTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name, e.g. BTCUSDT |
| limit | query | string |  | number of data returned. Default: 500, maximum: 1000 |
| idLessThan | query | string |  | Order ID, returns records less than the specified 'tradeId'. |
| startTime | query | string |  | startTime, Unix millisecond timestamp e.g. 1690196141868. startTime and endTime should be within 7days. |
| endTime | query | string |  | endTime, Unix millisecond timestamp e.g. 1690196141868. startTime and endTime should be within 7days. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].tradeId | string |  | Order ID. Descending |
| data[].side | string |  | Direction. `Buy` / `Sell` |
| data[].price | string |  | Order price |
| data[].size | string |  | Filled quantity |
| data[].ts | string |  | Transaction time(second level). Unix millisecond timestamp, e.g. 1744275603000 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744275754521,
  "data": [
    {
      "symbol": "ETHUSDT",
      "tradeId": "1294151170843025500",
      "side": "Buy",
      "price": "1592.58",
      "size": "2.1982",
      "ts": "1744275603000"
    },
    {
      "symbol": "ETHUSDT",
      "tradeId": "1294151170834636801",
      "side": "Sell",
      "price": "1592.57",
      "size": "0.0045",
      "ts": "1744275603000"
    }
  ]
}
```

## Get Candlestick Data

`GET /api/v2/spot/market/candles`

Frequency limit: 20 times/1s (IP)

Get Candlestick Data<br/>You can download historical spot candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketGetCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair e.g.BTCUSDT |
| granularity | query | string | 是 | Time interval of charts. For the corresponding relationship between granularity and value, refer to the list below. minute: 1min,3min,5min,15min,30min; hour: 1h,4h,6h,12h; day: 1day,3day; week: 1week; month: 1M; hour in UTC:6Hutc,12Hutc; day in UTC:1Dutc,3Dutc; week in UTC:1Wutc; month in UTC: 1Mutc; 1m, 3m, 5m can query for one month,15m can query for 52 days,30m can query for 62 days,1H can query for 83 days,2H can query for 120 days,4H can query for 240 days,6H can query for 360 days. |
| startTime | query | string |  | The time start point of the chart data, i.e., to get the chart data after this time stamp. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The time end point of the chart data, i.e., get the chart data before this time stamp. Unix millisecond timestamp, e.g. 1690196141868 |
| limit | query | string |  | Number of queries: Default: 100, maximum: 1000. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [timestamp, open, high, low, close, base volume, USDT volume, quote volume] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695800278693,
  "data": [
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ],
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ]
  ]
}
```

## Get History Candlestick Data

`GET /api/v2/spot/market/history-candles`

Frequency limit: 20 times/1s (IP)

Get History Candlestick Data<br/>You can download historical spot candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicSpotMarketGetHistoryCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| granularity | query | string | 是 | Time interval of charts. For the corresponding relationship between granularity and value, refer to the list below. minute: 1min,3min,5min,15min,30min; hour: 1h,4h,6h,12h; day: 1day,3day; week: 1week; month: 1M; hour in UTC:6Hutc,12Hutc; day in UTC:1Dutc,3Dutc; week in UTC:1Wutc; month in UTC: 1Mutc |
| endTime | query | string | 是 | The time end point of the chart data, i.e., get the chart data before this time stamp. Unix millisecond timestamp, e.g. 1690196141868 |
| limit | query | string |  | Number of queries: Default: 100, maximum: 200. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [timestamp, open, high, low, close, base volume, USDT volume, quote volume] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    [
      "1646064000000",
      "43500.8",
      "48207.2",
      "38516",
      "46451.9",
      "2581.4668",
      "118062073.82644",
      "118062073.82644"
    ],
    [
      "1648742400000",
      "46451.9",
      "55199.6",
      "15522.1",
      "38892.5",
      "42331329.5473",
      "1726993402150.991724",
      "1726993402150.991724"
    ],
    [
      "1654012800000",
      "38892.5",
      "38892.5",
      "38892.5",
      "38892.5",
      "0",
      "0",
      "0"
    ],
    [
      "1654012800000",
      "39270.4",
      "39270.4",
      "37834.5",
      "37834.5",
      "42.444",
      "1619934.779",
      "1619934.779"
    ],
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ]
  ]
}
```

## Get Call Auction information

`GET /api/v2/spot/market/auction`

Frequency limit: 20 times/1s (IP)

Get Call Auction information

Operation ID: `classicSpotMarketGetAuction`

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
| data | object |  |  |
| data.stage | string |  | Call Auction: `pre_market` pre market / `stage_1` Auction 1 / `stage_2` Auction 2 / `stage_3` Auction 3 / `success` Auction success / `failure` Auction failed |
| data.stageEndTime | string |  | Current phase end time, milliseconds |
| data.estOpeningPrice | ['string', 'null'] |  | Estimated Opening Price |
| data.matchedVolume | ['string', 'null'] |  | Matched Volume, base coin |
| data.auctionEndTime | string |  | Call Auction end time, milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728875148294,
  "data": {
    "stage": "stage_1",
    "stageEndTime": "1728876900000",
    "estOpeningPrice": null,
    "matchedVolume": null,
    "auctionEndTime": "1728877500000"
  }
}
```

## Get VIP Fee Rate

`GET /api/v2/spot/market/vip-fee-rate`

Frequency limit: 10 times/1s (IP)

Get VIP Fee Rate

Operation ID: `classicSpotMarketGetVipFeeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].level | string |  | VIP level |
| data[].dealAmount | string |  | Total trading volume in last 30 days, USDT |
| data[].assetAmount | string |  | Total assets in USDT |
| data[].takerFeeRate | string |  | Taker fee. Refer to the official announcement for the real rate when 0 is shown. |
| data[].makerFeeRate | string |  | Maker fee. Refer to the official announcement for the real rate when 0 is shown. |
| data[].btcWithdrawAmount | string |  | 24-hour withdrawal limit in BTC |
| data[].usdtWithdrawAmount | string |  | 24-hour withdrawal limit in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1675759699382,
  "data": [
    {
      "level": "1",
      "dealAmount": "1000000",
      "assetAmount": "50000",
      "takerFeeRate": "0",
      "makerFeeRate": "0",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    }
  ]
}
```


---

现货市场数据接口 —— 交易对、行情、深度、K线、成交与币种信息。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/public/symbols` — 获取交易对信息
- `GET /api/v2/spot/public/coins` — 获取币种信息
- `GET /api/v2/spot/market/tickers` — 获取行情信息
- `GET /api/v2/spot/market/orderbook` — 获取交易深度
- `GET /api/v2/spot/market/merge-depth` — 获取合并交易深度
- `GET /api/v2/spot/market/fills` — 获取最近成交数据
- `GET /api/v2/spot/market/fills-history` — 获取历史成交数据
- `GET /api/v2/spot/market/candles` — 获取K线数据
- `GET /api/v2/spot/market/history-candles` — 获取历史K线数据
- `GET /api/v2/spot/market/auction` — 获取集合竞价信息
- `GET /api/v2/spot/market/vip-fee-rate` — 获取现货VIP费率

## 获取交易对信息

`GET /api/v2/spot/public/symbols`

限速规则 20次/1s (IP)

获取交易对信息，支持单个及全量查询

Operation ID: `classicSpotMarketGetSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称，如"BTCUSDT"。如不填写，默认返回全部交易对信息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].baseCoin | string |  | 基础币，如交易对"BTCUSDT"中的"BTC" |
| data[].quoteCoin | string |  | 计价货币，例如交易对"BTCUSDT"中的"USDT" |
| data[].minTradeAmount | string |  | 最小交易数量(废弃请忽略)，参考最小USDT交易额 |
| data[].maxTradeAmount | string |  | 最大交易数量(废弃请忽略)，最大数量一般无限制 |
| data[].takerFeeRate | string |  | 默认吃单手续费率，可被个人交易手续费率覆盖 |
| data[].makerFeeRate | string |  | 默认挂单手续费率，可被个人交易手续费率覆盖 |
| data[].pricePrecision | string |  | 价格精度 |
| data[].quantityPrecision | string |  | 数量精度 |
| data[].quotePrecision | string |  | 右币精度 |
| data[].minTradeUSDT | string |  | 最小USDT交易额 |
| data[].status | string |  | 上架状态。`offline`: 下架 / `gray`: 灰度 / `online`: 上线 / `halt`: 停盘 |
| data[].buyLimitPriceRatio | string |  | 买入与现价的价差百分比, 小数形式，如 0.05 表示: 5% |
| data[].sellLimitPriceRatio | string |  | 卖出与现价的价差百分比, 小数形式，如 0.05 表示: 5% |
| data[].orderQuantity | string |  | 当前币对最多允许订单数量 |
| data[].areaSymbol | string |  | 区域币对。`yes`: 是；`no`: 否 |
| data[].maxLimitOrderValue | string |  | 限价最大单笔交易金额，单位为USDT |
| data[].maxMarketOrderValue | string |  | 市价最大单笔交易金额，单位为USDT |
| data[].offTime | string |  | 下架时间，例如：1744797600000 |
| data[].openTime | string |  | 该字段已废弃 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744276707885,
  "data": [
    {
      "symbol": "BTCUSDT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "minTradeAmount": "0",
      "maxTradeAmount": "900000000000000000000",
      "takerFeeRate": "0.002",
      "makerFeeRate": "0.002",
      "pricePrecision": "2",
      "quantityPrecision": "6",
      "quotePrecision": "8",
      "status": "online",
      "minTradeUSDT": "1",
      "buyLimitPriceRatio": "0.05",
      "sellLimitPriceRatio": "0.05",
      "areaSymbol": "no",
      "maxLimitOrderValue": "500000",
      "maxMarketOrderValue": "50000",
      "orderQuantity": "200",
      "openTime": "1532454360000",
      "offTime": ""
    }
  ]
}
```

## 获取币种信息

`GET /api/v2/spot/public/coins`

限速规则 3次/1s (IP)

获取平台币种信息，支持单个或全量查询。该接口可获取到的币种与现货账户支持的币种一致

Operation ID: `classicSpotMarketGetCoinList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如"BTC"。如不填写，默认返回全部币种信息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coinId | string |  | 币种ID |
| data[].coin | string |  | 币种名称 |
| data[].transfer | string |  | 是否可以划转 |
| data[].chains | object[] |  | 支持的链列表 |
| data[].chains[].chain | string |  | 链名称 |
| data[].chains[].needTag | string |  | 是否需要tag |
| data[].chains[].withdrawable | string |  | 是否可提现 |
| data[].chains[].rechargeable | string |  | 是否可充值 |
| data[].chains[].withdrawFee | string |  | 提现手续费 |
| data[].chains[].extraWithdrawFee | string |  | 额外收取, 链上转账销毁，`0.1`表示`10%` |
| data[].chains[].depositConfirm | string |  | 充值确认块数 |
| data[].chains[].withdrawConfirm | string |  | 提现确认块数 |
| data[].chains[].minDepositAmount | string |  | 最小充值数 |
| data[].chains[].minWithdrawAmount | string |  | 最小提现数 |
| data[].chains[].browserUrl | string |  | 区块浏览器地址 |
| data[].chains[].contractAddress | string |  | 币种合约地址 |
| data[].chains[].withdrawStep | string |  | 提币步长，非0，代表提币数量需满足步长倍数；为0，代表没有步长倍数的限制 |
| data[].chains[].withdrawMinScale | string |  | 提币数量精度 |
| data[].chains[].congestion | string |  | 链网络拥堵情况。`normal`: 正常 / `congested`: 拥堵 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    {
      "coinId": "1",
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

## 获取行情信息

`GET /api/v2/spot/market/tickers`

限速规则 20次/1s (IP)

获取公共行情信息，支持单个及批量查询

Operation ID: `classicSpotMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称列表，如BTCUSDT。如不填写，默认返回全部交易对信息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].high24h | string |  | 24小时最高价 |
| data[].open | string |  | 24小时开盘价 |
| data[].lastPr | string |  | 最新成交价 |
| data[].low24h | string |  | 24小时最低价 |
| data[].quoteVolume | string |  | 计价币成交额 |
| data[].baseVolume | string |  | 基础币成交额 |
| data[].usdtVolume | string |  | USDT成交额 |
| data[].bidPr | string |  | 买一价 |
| data[].askPr | string |  | 卖一价 |
| data[].bidSz | string |  | 买一量 |
| data[].askSz | string |  | 卖一量 |
| data[].openUtc | string |  | 零时区 开盘价 |
| data[].ts | string |  | 当前时间。Unix毫秒时间戳，例如1690196141868 |
| data[].changeUtc24h | string |  | UTC0时涨跌幅, 0.01表示1% |
| data[].change24h | string |  | 24小时涨跌幅, 0.01表示1% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "symbol": "BTCUSDT",
      "high24h": "37775.65",
      "open": "35134.2",
      "low24h": "34413.1",
      "lastPr": "34413.1",
      "quoteVolume": "0",
      "baseVolume": "0",
      "usdtVolume": "0",
      "bidPr": "0",
      "askPr": "0",
      "bidSz": "0.0663",
      "askSz": "0.0119",
      "openUtc": "23856.72",
      "ts": "1625125755277",
      "changeUtc24h": "0.00301",
      "change24h": "0.00069"
    }
  ]
}
```

## 获取交易深度

`GET /api/v2/spot/market/orderbook`

限速规则 20次/1s (IP)

获取交易深度<br/>现货深度历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketGetOrderbook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| type | query | string |  | 默认：step0： 取值：step0，step1，step2，step3，step4，step5 |
| limit | query | string |  | 查询条数 默认150, 最大150 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | string[][] |  | 卖方深度，如["38084.5","0.5"] 中，"38084.5"代表深度价格，"0.5"代表基础币数量 |
| data.bids | string[][] |  | 买方深度 |
| data.ts | string |  | 撮合引擎时间戳，Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698303884579,
  "data": {
    "asks": [
      [
        "34567.15",
        "0.0131"
      ],
      [
        "34567.25",
        "0.0144"
      ]
    ],
    "bids": [
      [
        "34567",
        "0.2917"
      ],
      [
        "34566.85",
        "0.0145"
      ]
    ],
    "ts": "1698303884584"
  }
}
```

## 获取合并交易深度

`GET /api/v2/spot/market/merge-depth`

限速规则 20次/1s (IP)

获取交易深度<br/>现货深度历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketMergeOrderbook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| precision | query | string |  | 价格精度，根据选择的精度作为步长返回累计深度。枚举值：scale0/scale1/scale2/scale3。一般情况下，scale0 代表不合并，为该参数的默认值；scale1为交易对报价精度*10的合并深度；scale2为报价精度*100；scale3为报价精度*1000。一般情况下，0/1/2/3对应的精度以实际返回参数"scale"为准，每个交易对的报价精度都不一样，部分币对并没有scale 2。请求该币对不存在的scale将会按照最大scale处理。例：某个交易对只有scale 0/1，当请求scale2时自动降为scale1 |
| limit | query | string |  | 固定档位枚举值：1/5/15/50/max，默认档位100，当实际深度不满足limit时，按实际档位返回，传入max返回该交易对的最大档位 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | array[] |  | 卖方深度，如[38084.5, 0.5] 中，38084.5 代表深度价格，0.5 代表基础币数量 |
| data.bids | array[] |  | 买方深度 |
| data.precision | string |  | 当前档位，例如"scale1" |
| data.scale | string |  | 实际精度值，例如"0.1" |
| data.isMaxPrecision | string |  | 是否为最大精度。YES 表示当前已经是最大精度 / NO 表示当前非最大精度 |
| data.ts | string |  | 撮合引擎时间戳，Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "asks": [
      [
        38084.5,
        0.0039
      ],
      [
        38085.7,
        0.0018
      ],
      [
        38086.7,
        0.031
      ],
      [
        38088.2,
        0.5303
      ]
    ],
    "bids": [
      [
        38073.7,
        0.4993
      ],
      [
        38073.4,
        0.45
      ],
      [
        38073.3,
        0.1179
      ],
      [
        38071.5,
        0.2162
      ]
    ],
    "ts": "1622102974025",
    "scale": "0.1",
    "precision": "scale0",
    "isMaxPrecision": "YES"
  }
}
```

## 获取最近成交数据

`GET /api/v2/spot/market/fills`

限速规则 10次/1s (IP)

获取最近成交数据<br/>现货成交历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketGetRecentTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，如BTCUSDT |
| limit | query | string |  | 默认100，最大500 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].tradeId | string |  | 成交单ID，降序排列 |
| data[].side | string |  | 交易方向，buy买入 / sell卖出 |
| data[].price | string |  | 成交价格，数值保留两位小数 |
| data[].size | string |  | 成交数量 |
| data[].ts | string |  | 成交时间，Unix毫秒时间戳，例如1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "symbol": "BFTUSDT",
      "tradeId": "1",
      "side": "buy",
      "price": "2.38735",
      "size": "2470.6224",
      "ts": "1622097282536"
    },
    {
      "symbol": "BFTUSDT",
      "tradeId": "2",
      "side": "sell",
      "price": "2.38649",
      "size": "3239.7976",
      "ts": "1622097280642"
    }
  ]
}
```

## 获取历史成交数据

`GET /api/v2/spot/market/fills-history`

限速规则 10次/1s (IP)

以交易对维度获取历史成交数据。startTime和endTime时间间隔不可超过7天。仅支持获取90天内数据。90天以上数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketGetMarketTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，如"BTCUSDT" |
| limit | query | string |  | 查询条数，默认500，最大1000 |
| idLessThan | query | string |  | 成交ID，返回小于指定'tradeId'的记录 |
| startTime | query | string |  | 成交数据的时间起始点，即获取该时间戳以后的历史成交数据。Unix毫秒时间戳格式，例如1690196141868 |
| endTime | query | string |  | 成交数据的时间终止点，即获取该时间戳以前的历史成交数据。Unix毫秒时间戳格式，例如1690196141868 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].tradeId | string |  | 成交单ID，降序排列 |
| data[].side | string |  | 交易方向，buy 买入 / sell 卖出 |
| data[].price | string |  | 成交价格，数值保留两位小数 |
| data[].size | string |  | 成交数量 |
| data[].ts | string |  | 成交时间（秒级），Unix毫秒时间戳，例如1744275244000 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744275754521,
  "data": [
    {
      "symbol": "ETHUSDT",
      "tradeId": "1294151170843025500",
      "side": "Buy",
      "price": "1592.58",
      "size": "2.1982",
      "ts": "1744275603000"
    },
    {
      "symbol": "ETHUSDT",
      "tradeId": "1294151170834636801",
      "side": "Sell",
      "price": "1592.57",
      "size": "0.0045",
      "ts": "1744275603000"
    }
  ]
}
```

## 获取K线数据

`GET /api/v2/spot/market/candles`

限速规则 20次/1s (IP)

获取K线数据<br/>现货K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketGetCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，如BTCUSDT |
| granularity | query | string | 是 | K线的时间颗粒度。分钟：1min，5min，15min，30min；小时：1h，4h，6h，12h；天：1day，3day；周：1week；月：1M；零时区小时线：6Hutc，12Hutc；零时区日线：1Dutc ，3Dutc；零时区周线：1Wutc；零时区月线：1Mutc；1m、3m、5m可以查一个月;15m可以查52天; 30m查62天; 1H可以查83天; 2H可以查120天; 4H可以查240天; 6H可以查360天 |
| startTime | query | string |  | K线数据的时间起始点，即获取该时间戳以后的K线数据。Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string |  | K线数据的时间终止点，即获取该时间戳以前的K线数据。Unix毫秒时间戳，例如1690196141868 |
| limit | query | string |  | 查询条数，默认100，最大1000 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [系统时间戳, 开盘价格, 最高价格, 最低价格, 收盘价格, 基础币成交量, USDT成交量, 计价币成交量] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695800278693,
  "data": [
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ],
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ]
  ]
}
```

## 获取历史K线数据

`GET /api/v2/spot/market/history-candles`

限速规则 20次/1s (IP)

获取历史K线数据<br/>现货K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicSpotMarketGetHistoryCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| granularity | query | string | 是 | K线的时间间隔。分钟：1min，5min，15min，30min；小时：1h，4h，6h，12h；天：1day，3day；周：1week；月：1M；零时区小时线：6Hutc，12Hutc；零时区日线：1Dutc ，3Dutc；零时区周线：1Wutc；零时区月线：1Mutc |
| endTime | query | string | 是 | K线数据的时间终止点，即获取该时间戳以前的K线数据。Unix毫秒时间戳，例如1690196141868 |
| limit | query | string |  | 查询条数 默认100，最大200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [系统时间戳, 开盘价格, 最高价格, 最低价格, 收盘价格, 基础币成交量, USDT成交量, 计价币成交量] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695799900330,
  "data": [
    [
      "1646064000000",
      "43500.8",
      "48207.2",
      "38516",
      "46451.9",
      "2581.4668",
      "118062073.82644",
      "118062073.82644"
    ],
    [
      "1648742400000",
      "46451.9",
      "55199.6",
      "15522.1",
      "38892.5",
      "42331329.5473",
      "1726993402150.991724",
      "1726993402150.991724"
    ],
    [
      "1654012800000",
      "38892.5",
      "38892.5",
      "38892.5",
      "38892.5",
      "0",
      "0",
      "0"
    ],
    [
      "1654012800000",
      "39270.4",
      "39270.4",
      "37834.5",
      "37834.5",
      "42.444",
      "1619934.779",
      "1619934.779"
    ],
    [
      "1656604800000",
      "37834.5",
      "37849.5",
      "37773.5",
      "37773.5",
      "428.3462",
      "16198849.1079",
      "16198849.1079"
    ]
  ]
}
```

## 获取集合竞价信息

`GET /api/v2/spot/market/auction`

限速规则 20次/1s (IP)

获取集合竞价信息

Operation ID: `classicSpotMarketGetAuction`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.stage | string |  | 集合竞价阶段: `pre_market` 盘前 / `stage_1` 第一阶段 / `stage_2` 第二阶段 / `stage_3` 第三阶段 / `success` 竞价成功 / `failure` 竞价失败 |
| data.stageEndTime | string |  | 当前阶段结束时间 Unix毫秒时间戳 |
| data.estOpeningPrice | ['string', 'null'] |  | 预估开盘价 |
| data.matchedVolume | ['string', 'null'] |  | 撮合量 单位为集合竞价币种 |
| data.auctionEndTime | string |  | 集合竞价结束时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728875148294,
  "data": {
    "stage": "stage_1",
    "stageEndTime": "1728876900000",
    "estOpeningPrice": null,
    "matchedVolume": null,
    "auctionEndTime": "1728877500000"
  }
}
```

## 获取现货VIP费率

`GET /api/v2/spot/market/vip-fee-rate`

限速规则 10次/1s (IP)

获取所有VIP等级的费率信息

Operation ID: `classicSpotMarketGetVipFeeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].level | string |  | VIP等级 |
| data[].dealAmount | string |  | 近30日累计成交额，单位为USDT |
| data[].assetAmount | string |  | 资产总额，单位为USDT |
| data[].takerFeeRate | string |  | taker费率, 0值时真实费率请参考官方公告 |
| data[].makerFeeRate | string |  | maker费率, 0值时真实费率请参考官方公告 |
| data[].btcWithdrawAmount | string |  | 24小时提币限额，单位为BTC |
| data[].usdtWithdrawAmount | string |  | 24小时提币限额，单位为USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1675759699382,
  "data": [
    {
      "level": "1",
      "dealAmount": "1000000",
      "assetAmount": "50000",
      "takerFeeRate": "0",
      "makerFeeRate": "0",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    }
  ]
}
```