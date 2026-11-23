---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-contract-market
api_type: REST
updated_at: 2026-11-23 19:02:24.435077
---

# Classic Contract Market API

Classic account — futures market data.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/discount-rate` — Get Discount Rate
- `GET /api/v2/mix/market/exchange-rate` — Get Interest Exchange Rate
- `GET /api/v2/mix/market/union-interest-rate-history` — Get Interest rate history
- `GET /api/v2/mix/market/vip-fee-rate` — VIP Fee Rate
- `GET /api/v2/mix/market/merge-depth` — Get Merge Market Depth
- `GET /api/v2/mix/market/ticker` — Get Ticker
- `GET /api/v2/mix/market/tickers` — Get All Tickers
- `GET /api/v2/mix/market/fills` — Get Recent Transactions
- `GET /api/v2/mix/market/fills-history` — Get History Transactions
- `GET /api/v2/mix/market/candles` — Get Candlestick Data
- `GET /api/v2/mix/market/history-candles` — Get Historical Candlestick
- `GET /api/v2/mix/market/history-index-candles` — Get Historical Index Price Candlestick
- `GET /api/v2/mix/market/history-mark-candles` — Get Historical Mark Price Candlestick
- `GET /api/v2/mix/market/open-interest` — Get Open Interest
- `GET /api/v2/mix/market/current-fund-rate` — Get Current Funding Rate
- `GET /api/v2/mix/market/history-fund-rate` — Get Historical Funding Rates
- `GET /api/v2/mix/market/funding-time` — Get Next Funding Time
- `GET /api/v2/mix/market/symbol-price` — Get Mark/Index/Market Prices
- `GET /api/v2/mix/market/contracts` — Get Contract Config
- `GET /api/v2/mix/market/oi-limit` — Get Contract OI Limit

## Get Discount Rate

`GET /api/v2/mix/market/discount-rate`

Frequency limit:5 times/1s (IP)

Get Discount Rate

Operation ID: `classicContractMarketGetDiscountRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Assets |
| data[].userLimit | string |  | Individual limit |
| data[].totalLimit | string |  | Total platform limit |
| data[].discountRateList | object[] |  | Tier discount rate |
| data[].discountRateList[].tier | string |  | Tier |
| data[].discountRateList[].minAmount | string |  | Min |
| data[].discountRateList[].maxAmount | string |  | Max |
| data[].discountRateList[].discountRate | string |  | Discount rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725848381845,
  "data": [
    {
      "coin": "BTC",
      "userLimit": "100",
      "totalLimit": "1500",
      "discountRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "10000",
          "discountRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "10000",
          "maxAmount": "100000",
          "discountRate": "0.95"
        },
        {
          "tier": "3",
          "minAmount": "100000",
          "maxAmount": "200000",
          "discountRate": "0.9"
        },
        {
          "tier": "4",
          "minAmount": "200000",
          "maxAmount": "-1",
          "discountRate": "0.8"
        }
      ]
    },
    {
      "coin": "ETH",
      "userLimit": "50000",
      "totalLimit": "500000000",
      "discountRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "100",
          "discountRate": "0.9"
        },
        {
          "tier": "2",
          "minAmount": "100",
          "maxAmount": "5000",
          "discountRate": "0.7"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "-1",
          "discountRate": "0.5"
        }
      ]
    }
  ]
}
```

## Get Interest Exchange Rate

`GET /api/v2/mix/market/exchange-rate`

Rate limit:5 requests/sec/IP

Get Interest exchange rate

Operation ID: `classicContractMarketGetExchangeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Assets |
| data[].exchangeRateList | object[] |  | Tier exchange rate |
| data[].exchangeRateList[].tier | string |  | Tier |
| data[].exchangeRateList[].minAmount | string |  | Min |
| data[].exchangeRateList[].maxAmount | string |  | Max<br><br> `-1` means there is no limitation |
| data[].exchangeRateList[].exchangeRate | string |  | Exchange rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725948315516,
  "data": [
    {
      "coin": "BTC",
      "exchangeRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "1000",
          "exchangeRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "1000",
          "maxAmount": "5000",
          "exchangeRate": "0.98"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "10000",
          "exchangeRate": "0.97"
        },
        {
          "tier": "4",
          "minAmount": "10000",
          "maxAmount": "50000",
          "exchangeRate": "0.96"
        },
        {
          "tier": "5",
          "minAmount": "50000",
          "maxAmount": "-1",
          "exchangeRate": "0.95"
        }
      ]
    },
    {
      "coin": "ETH",
      "exchangeRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "1000",
          "exchangeRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "1000",
          "maxAmount": "5000",
          "exchangeRate": "0.98"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "10000",
          "exchangeRate": "0.97"
        },
        {
          "tier": "4",
          "minAmount": "10000",
          "maxAmount": "50000",
          "exchangeRate": "0.96"
        },
        {
          "tier": "5",
          "minAmount": "50000",
          "maxAmount": "-1",
          "exchangeRate": "0.95"
        }
      ]
    }
  ]
}
```

## Get Interest rate history

`GET /api/v2/mix/market/union-interest-rate-history`

Frequency limit:5 times/1s (IP)

Get Interest rate history

Operation ID: `classicContractMarketGetInterestRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin asset |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Assets |
| data.historyInterestRateList | object[] |  | History Interest list |
| data.historyInterestRateList[].annualInterestRate | string |  | Annual interest rate |
| data.historyInterestRateList[].dailyInterestRate | string |  | Daily interest rate |
| data.historyInterestRateList[].ts | string |  | Interest time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725948522731,
  "data": {
    "coin": "USDT",
    "historyInterestRateList": [
      {
        "ts": "1723533015946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      },
      {
        "ts": "1723446615946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      },
      {
        "ts": "1723360215946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      }
    ]
  }
}
```

## VIP Fee Rate

`GET /api/v2/mix/market/vip-fee-rate`

Rate limit:10 req/sec/IP

Get VIP fee rate

Operation ID: `classicContractMarketGetVIPFeeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].level | string |  | VIP level |
| data[].dealAmount | string |  | Total trading volume of the last 30 days, USDT |
| data[].assetAmount | string |  | Total assets, USDT |
| data[].takerFeeRate | string |  | Taker rate, '0.000425' means 4.25 with four decimal places ahead |
| data[].makerFeeRate | string |  | Maker rate, '0.00006' means 0.6 with four decimal places ahead |
| data[].btcWithdrawAmount | string |  | 24-hour withdrawal limit (BTC) |
| data[].usdtWithdrawAmount | string |  | 24-hour withdrawal limit (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794449789,
  "data": [
    {
      "level": "1",
      "dealAmount": "100000",
      "assetAmount": "50000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    },
    {
      "level": "2",
      "dealAmount": "200000",
      "assetAmount": "500000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    }
  ]
}
```

## Get Merge Market Depth

`GET /api/v2/mix/market/merge-depth`

Frequency limit: 20 times/1s (IP)

Get merge depth data

You can download historical futures depth data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetMergeDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| precision | query | string |  | Price accuracy, according to the selected accuracy as the step size to return the cumulative depth, enumeration value: <br><br>scale0/scale1/scale2/scale3<br><br>'scale0' is not merged, the default value<br><br>In general, 'scale1' is the merged depth of the transaction pair’s quotation accuracy*10<br><br>Generally, 'scale2' is the quotation precision *100<br><br>'scale3' is the quotation precision *1000<br><br>The precision corresponding to 0/1/2/3 is subject to the actual return parameter "scale". The quotation precision of each trading pair is different, and some trading pairs does not have 'scale2', and the request for a scale that does not exist for the currency pair will be processed according to the maximum scale. Example: A certain trading pair only has scale 0/1, and when scale2 is requested, it will be automatically reduced to 'scale1'. |
| limit | query | string |  | Fixed gear enumeration value: 1/5/15/50/max, the default gear is 100, passing max returns the maximum gear of the trading pair<br><br> When the actual depth does not meet the limit, return according to the actual gear . If max is passed in, the maximum level of the trading pair will be returned. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | string[][] |  | The selling price<br><br>elements are price and quantity. [Price, Quantity] |
| data.bids | string[][] |  | Buying price<br><br>The elements are price and quantity. [Price, Quantity] |
| data.precision | string |  | Requested precision |
| data.scale | string |  | Actual precision value |
| data.isMaxPrecision | string |  | YES indicates that the current accuracy is the maximum, NO indicates that it is not the maximum accuracy. |
| data.ts | string |  | Matching engine timestamp(ms), e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695870963008,
  "data": {
    "asks": [
      [
        26347.5,
        0.25
      ],
      [
        26348,
        0.16
      ]
    ],
    "bids": [
      [
        26346.5,
        0.16
      ],
      [
        26346,
        0.32
      ]
    ],
    "ts": "1695870968804",
    "scale": "0.1",
    "precision": "scale0",
    "isMaxPrecision": "NO"
  }
}
```

## Get Ticker

`GET /api/v2/mix/market/ticker`

Frequency limit: 20 times/1s (IP)

Get ticker data of the given 'productType' and 'symbol'

Operation ID: `classicContractMarketGetTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].lastPr | string |  | Last price |
| data[].askPr | string |  | Ask price |
| data[].bidPr | string |  | Bid price |
| data[].bidSz | string |  | Buying amount |
| data[].askSz | string |  | Selling amount |
| data[].high24h | string |  | 24h high |
| data[].low24h | string |  | 24h low |
| data[].ts | string |  | Milliseconds format of current data timestamp Unix, e.g. 1597026383085 |
| data[].change24h | string |  | Price increase or decrease (24 hours) |
| data[].baseVolume | string |  | Trading volume of the coin |
| data[].quoteVolume | string |  | Trading volume of quote currency |
| data[].usdtVolume | string |  | Trading volume of USDT |
| data[].openUtc | string |  | UTC0 opening price |
| data[].changeUtc24h | string |  | UTC0 24-hour price increase and decrease |
| data[].indexPrice | string |  | Index price |
| data[].fundingRate | string |  | Funding rate |
| data[].holdingAmount | string |  | Current holding positions(base coin) |
| data[].open24h | string |  | Entry price of the last 24 hours<br><br>The opening time is compared on a 24-hour basis. i.e.: Now it is 7:00 PM of the 2nd day of the month, then the corresponding opening time is 7:00 PM of the 1st day of the month. |
| data[].deliveryStartTime | string |  | Delivery start time (only for delivery contracts) |
| data[].deliveryTime | string |  | Delivery time (only for delivery contracts） |
| data[].deliveryStatus | string |  | Delivery status (only for delivery contracts; `delivery_config_period`: Newly listed currency pairs are configured<br><br>`delivery_normal`: Trading normally<br><br>`delivery_before`: 10 minutes before delivery, opening positions are prohibited<br><br>`delivery_period`: Delivery, opening, closing, and canceling orders are prohibited |
| data[].markPrice | string |  | Mark price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794095685,
  "data": [
    {
      "symbol": "ETHUSDM26",
      "lastPr": "1829.3",
      "askPr": "1829.8",
      "bidPr": "1829.3",
      "bidSz": "0.054",
      "askSz": "0.785",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794098184",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "1822.15",
      "fundingRate": "0",
      "holdingAmount": "9488.49",
      "deliveryStartTime": "1693538723186",
      "deliveryTime": "1703836799000",
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "1829"
    }
  ]
}
```

## Get All Tickers

`GET /api/v2/mix/market/tickers`

Frequency limit: 20 times/1s (IP)

Get all ticker data of the given 'productType'

Operation ID: `classicContractMarketGetAllSymbolTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].lastPr | string |  | Last price |
| data[].askPr | string |  | Ask price |
| data[].bidPr | string |  | Bid price |
| data[].bidSz | string |  | Buying amount |
| data[].askSz | string |  | Selling amount |
| data[].high24h | string |  | 24h high |
| data[].low24h | string |  | 24h low |
| data[].ts | string |  | Milliseconds format of current data timestamp Unix, e.g. 1597026383085 |
| data[].change24h | string |  | Price increase or decrease (24 hours) |
| data[].baseVolume | string |  | Trading volume of the coin |
| data[].quoteVolume | string |  | Trading volume of quote currency |
| data[].usdtVolume | string |  | Trading volume of USDT |
| data[].openUtc | string |  | UTC0 opening price |
| data[].changeUtc24h | string |  | UTC0 24-hour price increase and decrease |
| data[].indexPrice | string |  | Index price |
| data[].fundingRate | string |  | Funding rate |
| data[].holdingAmount | string |  | Current positions in the unit of number of coins traded. |
| data[].open24h | string |  | Entry price of the last 24 hours<br><br>The opening time is compared on a 24-hour basis. i.e.: Now it is 7:00 PM of the 2nd day of the month, then the corresponding opening time is 7:00 PM of the 1st day of the month. |
| data[].deliveryStartTime | string |  | Delivery start time (only for delivery contracts) |
| data[].deliveryTime | string |  | Delivery time (only for delivery contracts） |
| data[].deliveryStatus | string |  | Delivery status (only for delivery contracts; `delivery_config_period`: Newly listed currency pairs are configured<br><br>`delivery_normal`: Trading normally<br><br>`delivery_before`: 10 minutes before delivery, opening positions are prohibited<br><br>`delivery_period`: Delivery, opening, closing, and canceling orders are prohibited |
| data[].markPrice | string |  | Mark price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794269124,
  "data": [
    {
      "symbol": "BTCUSD",
      "lastPr": "29904.5",
      "askPr": "29904.5",
      "bidPr": "29903.5",
      "bidSz": "0.5091",
      "askSz": "2.2694",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794271400",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "29132.353333",
      "fundingRate": "-0.0007",
      "holdingAmount": "125.6844",
      "deliveryStartTime": null,
      "deliveryTime": null,
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "12345"
    },
    {
      "symbol": "ETHUSD_231229",
      "lastPr": "1829.3",
      "askPr": "1829.8",
      "bidPr": "1829.3",
      "bidSz": "0.054",
      "askSz": "0.785",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794271400",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "1822.15",
      "fundingRate": "0",
      "holdingAmount": "9488.49",
      "deliveryStartTime": "1693538723186",
      "deliveryTime": "1703836799000",
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "1234"
    }
  ]
}
```

## Get Recent Transactions

`GET /api/v2/mix/market/fills`

Frequency limit: 20 times/1s (IP)

Get the record of last 100 transactions<br/>You can download historical futures trades data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetRecentFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| limit | query | string |  | Number of queries: Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tradeId | string |  | Transaction ID |
| data[].price | string |  | Price |
| data[].size | string |  | Quantity |
| data[].side | string |  | Direction |
| data[].ts | string |  | Milliseconds format of current data timestamp Unix, e.g. 1597026383085 |
| data[].symbol | string |  | Trading Pair name e.g. ETHUSDT |

```json
{
  "code": "00000",
  "data": [
    {
      "tradeId": "1",
      "price": "29990.5",
      "size": "0.0166",
      "side": "sell",
      "ts": "1627116776464",
      "symbol": "BTCUSDT"
    },
    {
      "tradeId": "2",
      "price": "30007.0",
      "size": "0.0166",
      "side": "buy",
      "ts": "1627116600875",
      "symbol": "BTCUSDT"
    }
  ],
  "msg": "success",
  "requestTime": 1690313813709
}
```

## Get History Transactions

`GET /api/v2/mix/market/fills-history`

Frequency limit: 10 times/1s (IP)

Get transaction records of the last 90 days

The time interval between startTime and endTime should not exceed 7 days.

You can download historical futures trades data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetFillsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| limit | query | string |  | Number of queries: Default: 500, maximum: 1000 |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is a week. The default end time is a week if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is a week. The default start time is a week ago if no value is set for the start time. ) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tradeId | string |  | tradeId, descending order |
| data[].price | string |  | Price |
| data[].size | string |  | Amount, specific base coin |
| data[].side | string |  | Trading direction<br><br>`sell`: Sell<br><br>`buy`: Buy |
| data[].ts | string |  | Current data timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085 |
| data[].symbol | string |  | Trading pair name |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865481335,
  "data": [
    {
      "tradeId": "1",
      "price": "26372.5",
      "size": "9.25",
      "side": "Sell",
      "ts": "1695865151000",
      "symbol": "BTCUSDT"
    },
    {
      "tradeId": "2",
      "price": "26383",
      "size": "12.12",
      "side": "Buy",
      "ts": "1695865115000",
      "symbol": "BTCUSDT"
    }
  ]
}
```

## Get Candlestick Data

`GET /api/v2/mix/market/candles`

Frequency limit: 20 times/1s (IP)

By default, 100 records are returned. If there is no data, an empty array is returned. The queryable data history varies depending on the k-line granularity.

The rules are as follows:

1m, 3m, and 5m can be checked for up to one month;

15m can be checked for up to 52 days;

30m can be searched for up to 62 days;

1H can be checked for up to 83 days;

2H can be checked for up to 120 days;

4H can be checked for up to 240 days;

6H can be checked for up to 360 days<br/>You can download historical futures candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| granularity | query | string | 是 | K-line particle size<br><br>- 1m(1 minute)<br><br>- 3m(3 minutes)<br><br>- 5m(5 minutes)<br><br>- 15m(15 minutes)<br><br>- 30m(30 minutes)<br><br>- 1H( 1 hour)<br><br>- 4H(4 hours)<br><br>- 6H(6 hours)<br><br>- 12H(12 hours)<br><br>- 1D(1 day)<br><br>- 3D ( 3 days)<br><br>- 1W (1 week)<br><br>- 1M (monthly line)<br><br>- 6Hutc (UTC 6 hour line)<br><br>- 12Hutc (UTC 12 hour line)<br><br>- 1Dutc (UTC 1-day line)<br><br>- 3Dutc (UTC 3-day line)<br><br>- 1Wutc (UTC weekly line)<br><br>- 1Mutc (UTC monthly line) |
| startTime | query | string |  | The start time is to query the k-lines after this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data after this start time (the maximum time query range is 90 days) |
| endTime | query | string |  | The end time is to query the k-lines before this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data before this end time (the maximum time query range is 90 days) |
| kLineType | query | string |  | Candlestick chart types: market tick; mark mark; index index;<br><br>market by default |
| limit | query | string |  | Default: 100, maximum: 1000 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>[1] Entry price<br><br>[2] Highest price<br><br>[3] Lowest price<br><br>[4] Exit price. The latest exit price may be updated in the future. Subscribe to WebSocket to track the latest price.<br><br>[5] Trading volume of the base coin<br><br>[6] Trading volume of quote currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865615662,
  "data": [
    [
      "1695835800000",
      "26210.5",
      "26210.5",
      "26194.5",
      "26194.5",
      "26.26",
      "687897.63"
    ],
    [
      "1695836100000",
      "26194.5",
      "26194.5",
      "26171",
      "26171",
      "17.98",
      "470618.72"
    ]
  ]
}
```

## Get Historical Candlestick

`GET /api/v2/mix/market/history-candles`

Frequency limit: 20 times/1s (IP)

Query all historical K-line data and return a maximum of 200 pieces of data.

Note: If endTime goes past a candle interval boundary (even by 1 ms), the system may round up when calculating the number of candles, and the response may include one additional interval (i.e., the returned data may start one interval earlier).

You can download historical futures candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetHistoryCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| granularity | query | string | 是 | K-line particle size<br><br>- 1m(1 minute)<br><br>- 3m(3 minutes)<br><br>- 5m(5 minutes)<br><br>- 15m(15 minutes)<br><br>- 30m(30 minutes)<br><br>- 1H( 1 hour)<br><br>- 4H(4 hours)<br><br>- 6H(6 hours)<br><br>- 12H(12 hours)<br><br>- 1D(1 day)<br><br>- 3D ( 3 days)<br><br>- 1W (1 week)<br><br>- 1M (monthly line)<br><br>- 6Hutc (UTC 6 hour line)<br><br>- 12Hutc (UTC 12 hour line)<br><br>- 1Dutc (UTC 1-day line)<br><br>- 3Dutc (UTC 3-day line)<br><br>- 1Wutc (UTC weekly line)<br><br>- 1Mutc (UTC monthly line) |
| startTime | query | string |  | The start time is to query the k-lines after this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data after this start time (the maximum time query range is 90 days) |
| endTime | query | string |  | The end time is to query the k-lines before this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data before this end time (the maximum time query range is 90 days) |
| limit | query | string |  | Default: 100, maximum: 200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>[1] Entry price<br><br>[2] Highest price<br><br>[3] Lowest price<br><br>[4] Exit price(Only include the finished K line data)<br><br>[5] Trading volume of the base coin<br><br>[6] Trading volume of quote currency |

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

## Get Historical Index Price Candlestick

`GET /api/v2/mix/market/history-index-candles`

Frequency limit: 20 times/1s (IP)

Query the historical K-line data of contract index price, and return a maximum of 200 pieces of data.

You can download historical futures index price candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetHistoryIndexCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| granularity | query | string | 是 | K-line particle size<br><br>- 1m(1 minute)<br><br>- 3m(3 minutes)<br><br>- 5m(5 minutes)<br><br>- 15m(15 minutes)<br><br>- 30m(30 minutes)<br><br>- 1H( 1 hour)<br><br>- 4H(4 hours)<br><br>- 6H(6 hours)<br><br>- 12H(12 hours)<br><br>- 1D(1 day)<br><br>- 3D ( 3 days)<br><br>- 1W (1 week)<br><br>- 1M (monthly line)<br><br>- 6Hutc (UTC 6 hour line)<br><br>- 12Hutc (UTC 12 hour line)<br><br>- 1Dutc (UTC 1-day line)<br><br>- 3Dutc (UTC 3-day line)<br><br>- 1Wutc (UTC weekly line)<br><br>- 1Mutc (UTC monthly line) |
| startTime | query | string |  | The start time is to query the k-lines after this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data after this start time (the maximum time query range is 90 days) |
| endTime | query | string |  | The end time is to query the k-lines before this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data before this end time (the maximum time query range is 90 days) |
| limit | query | string |  | Default: 100, maximum: 200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>[1] Entry price<br><br>[2] Highest price<br><br>[3] Lowest price<br><br>[4] Exit price(Only include the finished K line data)<br><br>[5] Trading volume of the base coin<br><br>[6] Trading volume of quote currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695795177323,
  "data": [
    [
      "1691328900000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ],
    [
      "1691329200000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ]
  ]
}
```

## Get Historical Mark Price Candlestick

`GET /api/v2/mix/market/history-mark-candles`

Frequency limit: 20 times/1s (IP)

Get historical mark price candle data

You can download historical futures mark price candlestick data on our <a href="https://www.bitget.com/data-download">web</a>.

Operation ID: `classicContractMarketGetHistoryMarkCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| granularity | query | string | 是 | K-line particle size<br><br>- 1m(1 minute)<br><br>- 3m(3 minutes)<br><br>- 5m(5 minutes)<br><br>- 15m(15 minutes)<br><br>- 30m(30 minutes)<br><br>- 1H( 1 hour)<br><br>- 4H(4 hours)<br><br>- 6H(6 hours)<br><br>- 12H(12 hours)<br><br>- 1D(1 day)<br><br>- 3D ( 3 days)<br><br>- 1W (1 week)<br><br>- 1M (monthly line)<br><br>- 6Hutc (UTC 6 hour line)<br><br>- 12Hutc (UTC 12 hour line)<br><br>- 1Dutc (UTC 1-day line)<br><br>- 3Dutc (UTC 3-day line)<br><br>- 1Wutc (UTC weekly line)<br><br>- 1Mutc (UTC monthly line) |
| startTime | query | string |  | The start time is to query the k-lines after this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data after this start time (the maximum time query range is 90 days) |
| endTime | query | string |  | The end time is to query the k-lines before this time<br><br>According to the different time granularity, the corresponding time unit must be rounded down to be queried. <br><br>The millisecond format of the Unix timestamp, such as 1672410780000<br><br>Request data before this end time (the maximum time query range is 90 days) |
| limit | query | string |  | Default: 100, maximum: 200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>[1] Entry price<br><br>[2] Highest price<br><br>[3] Lowest price<br><br>[4] Exit price(Only include the finished K line data)<br><br>[5] Trading volume of the base coin<br><br>[6] Trading volume of quote currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695795362764,
  "data": [
    [
      "1691299500000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ],
    [
      "1691299800000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ]
  ]
}
```

## Get Open Interest

`GET /api/v2/mix/market/open-interest`

Frequency limit: 20 times/1s (IP)

Get the total positions of a certain trading pair on the platform

Operation ID: `classicContractMarketGetOpenInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.ts | string |  | Milliseconds format of data time Unix timestamp, e.g. <br><br>1672410780000 |
| data.openInterestList | object[] |  | Open interest data collection |
| data.openInterestList[].symbol | string |  | Trading pair name |
| data.openInterestList[].size | string |  | Total open interest of the platform <br><br>Specific coins, eg.: ETH in ETHUSDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695796780343,
  "data": {
    "openInterestList": [
      {
        "symbol": "BTCUSDT",
        "size": "34278.06"
      }
    ],
    "ts": "1695796781616"
  }
}
```

## Get Current Funding Rate

`GET /api/v2/mix/market/current-fund-rate`

Frequency limit: 20 times/1s (IP)

Get the current funding rate of the contract

Operation ID: `classicContractMarketGetCurrentFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].fundingRate | string |  | Current funding rates |
| data[].fundingRateInterval | string |  | Funding rate settlement period<br><br>Unit: hour. Enumeration values include 1, 2, 4, 8. 1 represents 1 hour, 2 represents 2 hours, and so on. |
| data[].nextUpdate | string |  | Next update time<br><br>Unix timestamp in milliseconds |
| data[].minFundingRate | string |  | Lower limit of funding rate <br><br>Returned in decimal form. 0.025 represents 2.5%. |
| data[].maxFundingRate | string |  | Upper limit of funding rate <br><br>Returned in decimal form. 0.025 represents 2.5%. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743054548546,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000068",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003"
    }
  ]
}
```

## Get Historical Funding Rates

`GET /api/v2/mix/market/history-fund-rate`

Frequency limit: 20 times/1s (IP)

Get the historical funding rate of the contract

Operation ID: `classicContractMarketGetHistoryFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| pageSize | query | string |  | Number of queries: Default: 20, maximum: 100. |
| pageNo | query | string |  | page number |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].fundingRate | string |  | Funding rate |
| data[].fundingTime | string |  | Settlement time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695796546319,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.0005",
      "fundingTime": "1695776400000"
    },
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000013",
      "fundingTime": "1695715200000"
    }
  ]
}
```

## Get Next Funding Time

`GET /api/v2/mix/market/funding-time`

Frequency limit: 20 times/1s (IP)

Get the next settlement time of the contract and the settlement period of the contract

Operation ID: `classicContractMarketGetSymbolNextFundingTime`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].nextFundingTime | string |  | Next settlement time(ms) |
| data[].ratePeriod | string |  | Rate settlement cycle<br><br>The unit is hour. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695796425096,
  "data": [
    {
      "symbol": "BTCUSDT",
      "nextFundingTime": "1695801600000",
      "ratePeriod": "8"
    }
  ]
}
```

## Get Mark/Index/Market Prices

`GET /api/v2/mix/market/symbol-price`

20 times/s, frequency is limited according to user ID

Get market/index/mark prices

Operation ID: `classicContractMarketGetSymbolPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].price | string |  | Latest price of the exchange |
| data[].indexPrice | string |  | Index price |
| data[].markPrice | string |  | Mark price |
| data[].ts | string |  | Milliseconds format of current data timestamp Unix, e.g. <br><br>1672410780000 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695793384294,
  "data": [
    {
      "symbol": "BTCUSDT",
      "price": "26242",
      "indexPrice": "34867",
      "markPrice": "25555",
      "ts": "1695793390482"
    }
  ]
}
```

## Get Contract Config

`GET /api/v2/mix/market/contracts`

Rate Limit: 20 req/sec/IP

Interface is used to get future contract details.

Operation ID: `classicContractMarketGetAllSymbolsContracts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair, based on the symbolName, i.e. BTCUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Product name |
| data[].baseCoin | string |  | Base currency <br><br>Specifically refers to ETH as in ETHUSDT |
| data[].quoteCoin | string |  | Quote currency<br><br>Specifically refers to USDT as in ETHUSDT |
| data[].buyLimitPriceRatio | string |  | Ratio of bid price to limit price |
| data[].sellLimitPriceRatio | string |  | Ratio of ask price to limit price |
| data[].feeRateUpRatio | string |  | Transaction fee increase ratio |
| data[].makerFeeRate | string |  | Maker rate |
| data[].takerFeeRate | string |  | Taker rate |
| data[].openCostUpRatio | string |  | Opening cost increase ratio |
| data[].supportMarginCoins | string[] |  | Supported margin coins |
| data[].minTradeNum | string |  | Minimum opening amount (base currency) |
| data[].priceEndStep | string |  | price step length |
| data[].volumePlace | string |  | Decimal places of the quantity |
| data[].pricePlace | string |  | Decimal places of the price |
| data[].sizeMultiplier | string |  | Quantity multiplier, the quantity of the order must be greater than minTradeNum and is a multiple of sizeMulti. |
| data[].symbolType | string |  | Futures types: perpetual; delivery |
| data[].minTradeUSDT | string |  | Minimum USDT transaction amount |
| data[].maxSymbolOrderNum | string |  | Maximum number of orders held-symbol dimension |
| data[].maxProductOrderNum | string |  | Maximum number of held orders-product type dimension |
| data[].maxPositionNum | string |  | Maximum number of positions held |
| data[].symbolStatus | string |  | Trading pair status<br><br>`listed` Listing symbol <br><br>`normal` trade normal <br><br>`maintain` can't open/close position <br><br>`limit_open`: can't place orders(can close position)<br><br>`restrictedAPI`:can't place orders with API <br><br>`off`: offline |
| data[].offTime | string |  | Trading halt time, '-1' means normal |
| data[].limitOpenTime | string |  | Time to open positions, '-1' means normal; other values indicate that the symbol is under maintenance or to be maintained and trading is prohibited after the specified time. |
| data[].deliveryTime | string |  | Delivery time |
| data[].deliveryStartTime | string |  | Delivery start time |
| data[].deliveryPeriod | string |  | Delivery period <br><br>`this_quarter` current quarter <br><br>`next_quarter` second quarter |
| data[].launchTime | string |  | Listing time |
| data[].fundInterval | string |  | Funding fee settlement cycle, hourly/every 8 hours |
| data[].minLever | string |  | minimum leverage |
| data[].maxLever | string |  | Maximum leverage |
| data[].posLimit | string |  | Position limits (deprecated) |
| data[].maintainTime | string |  | Maintenance time (there will be a value when the status is under maintenance/upcoming maintenance) |
| data[].maxMarketOrderQty | string |  | Maximum order quantity for a single market order<br><br> This refers to the maximum allowed quantity when placing an order using the base coin |
| data[].maxOrderQty | string |  | Maximum order quantity for a single limit order<br><br> This refers to the maximum allowed quantity when placing an order using the base coin |
| data[].isRwa | string |  | Is this an RWA Symbol <br><br>`YES` <br><br>`NO` |
| data[].openTime | string |  | This field has been deprecated |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695793701269,
  "data": [
    {
      "symbol": "BTCUSDT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "buyLimitPriceRatio": "0.9",
      "sellLimitPriceRatio": "0.9",
      "feeRateUpRatio": "0.1",
      "makerFeeRate": "0.0004",
      "takerFeeRate": "0.0006",
      "openCostUpRatio": "0.1",
      "supportMarginCoins": [
        "USDT"
      ],
      "minTradeNum": "0.01",
      "priceEndStep": "1",
      "volumePlace": "2",
      "pricePlace": "1",
      "sizeMultiplier": "0.01",
      "symbolType": "perpetual",
      "minTradeUSDT": "5",
      "maxSymbolOrderNum": "999999",
      "maxProductOrderNum": "999999",
      "maxPositionNum": "150",
      "symbolStatus": "normal",
      "offTime": "-1",
      "limitOpenTime": "-1",
      "deliveryTime": "",
      "deliveryStartTime": "",
      "deliveryPeriod": "",
      "launchTime": "",
      "fundInterval": "8",
      "minLever": "1",
      "maxLever": "125",
      "posLimit": "0.05",
      "maintainTime": "1680165535278",
      "openTime": "",
      "maxMarketOrderQty": "220",
      "maxOrderQty": "1200",
      "isRwa": "YES"
    }
  ]
}
```

## Get Contract OI Limit

`GET /api/v2/mix/market/oi-limit`

Rate Limit: 10 req/sec/IP

Interface is used to get future contract OI Limit.

Operation ID: `classicContractMarketGetContractsOi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair, based on the symbolName, i.e. BTCUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

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

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741596239587,
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "100000",
      "totalNotionalValue": "200000"
    },
    {
      "symbol": "BCHUSDT",
      "notionalValue": "100000",
      "totalNotionalValue": "200000"
    }
  ]
}
```


---

经典账户 — 合约行情数据。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/discount-rate` — 获取联合保证金折扣率
- `GET /api/v2/mix/market/exchange-rate` — 获取联合保证金兑换率
- `GET /api/v2/mix/market/union-interest-rate-history` — 获取利率记录
- `GET /api/v2/mix/market/vip-fee-rate` — 获取合约VIP费率
- `GET /api/v2/mix/market/merge-depth` — 合并深度接口
- `GET /api/v2/mix/market/ticker` — 获取单个交易对行情
- `GET /api/v2/mix/market/tickers` — 获取全部交易对行情
- `GET /api/v2/mix/market/fills` — 获取最近成交明细
- `GET /api/v2/mix/market/fills-history` — 获取成交明细
- `GET /api/v2/mix/market/candles` — 获取K线数据
- `GET /api/v2/mix/market/history-candles` — 合约历史k线
- `GET /api/v2/mix/market/history-index-candles` — 合约指数价格历史k线
- `GET /api/v2/mix/market/history-mark-candles` — 合约标记价格历史k线
- `GET /api/v2/mix/market/symbol-price` — 获取交易对市价/指数/标记价格
- `GET /api/v2/mix/market/open-interest` — 获取平台总持仓量
- `GET /api/v2/mix/market/current-fund-rate` — 获取当前资金费率
- `GET /api/v2/mix/market/history-fund-rate` — 获取历史资金费率
- `GET /api/v2/mix/market/funding-time` — 获取下次资金费结算时间
- `GET /api/v2/mix/market/contracts` — 获取合约信息
- `GET /api/v2/mix/market/oi-limit` — 获取合约OI限仓信息

## 获取联合保证金折扣率

`GET /api/v2/mix/market/discount-rate`

限速规则：5次/1s (IP)

获取联合保证金折扣率

Operation ID: `classicContractMarketGetDiscountRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].userLimit | string |  | 个人限额 |
| data[].totalLimit | string |  | 平台总限额 |
| data[].discountRateList | object[] |  | 折扣率数据 |
| data[].discountRateList[].tier | string |  | 梯度 |
| data[].discountRateList[].minAmount | string |  | 最小额度 |
| data[].discountRateList[].maxAmount | string |  | 最大额度(-1表示无限制) |
| data[].discountRateList[].discountRate | string |  | 折扣率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725848381845,
  "data": [
    {
      "coin": "BTC",
      "userLimit": "100",
      "totalLimit": "1500",
      "discountRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "10000",
          "discountRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "10000",
          "maxAmount": "100000",
          "discountRate": "0.95"
        },
        {
          "tier": "3",
          "minAmount": "100000",
          "maxAmount": "200000",
          "discountRate": "0.9"
        },
        {
          "tier": "4",
          "minAmount": "200000",
          "maxAmount": "-1",
          "discountRate": "0.8"
        }
      ]
    },
    {
      "coin": "ETH",
      "userLimit": "50000",
      "totalLimit": "500000000",
      "discountRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "100",
          "discountRate": "0.9"
        },
        {
          "tier": "2",
          "minAmount": "100",
          "maxAmount": "5000",
          "discountRate": "0.7"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "-1",
          "discountRate": "0.5"
        }
      ]
    }
  ]
}
```

## 获取联合保证金兑换率

`GET /api/v2/mix/market/exchange-rate`

限速规则：5次/1s (IP)

获取联合保证金兑换率

Operation ID: `classicContractMarketGetExchangeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].exchangeRateList | object[] |  | 兑换率数据 |
| data[].exchangeRateList[].tier | string |  | 梯度 |
| data[].exchangeRateList[].minAmount | string |  | 最小额度 |
| data[].exchangeRateList[].maxAmount | string |  | 最大额度(-1表示无限制) |
| data[].exchangeRateList[].exchangeRate | string |  | 兑换率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725948315516,
  "data": [
    {
      "coin": "BTC",
      "exchangeRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "1000",
          "exchangeRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "1000",
          "maxAmount": "5000",
          "exchangeRate": "0.98"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "10000",
          "exchangeRate": "0.97"
        },
        {
          "tier": "4",
          "minAmount": "10000",
          "maxAmount": "50000",
          "exchangeRate": "0.96"
        },
        {
          "tier": "5",
          "minAmount": "50000",
          "maxAmount": "-1",
          "exchangeRate": "0.95"
        }
      ]
    },
    {
      "coin": "ETH",
      "exchangeRateList": [
        {
          "tier": "1",
          "minAmount": "0",
          "maxAmount": "1000",
          "exchangeRate": "0.99"
        },
        {
          "tier": "2",
          "minAmount": "1000",
          "maxAmount": "5000",
          "exchangeRate": "0.98"
        },
        {
          "tier": "3",
          "minAmount": "5000",
          "maxAmount": "10000",
          "exchangeRate": "0.97"
        },
        {
          "tier": "4",
          "minAmount": "10000",
          "maxAmount": "50000",
          "exchangeRate": "0.96"
        },
        {
          "tier": "5",
          "minAmount": "50000",
          "maxAmount": "-1",
          "exchangeRate": "0.95"
        }
      ]
    }
  ]
}
```

## 获取利率记录

`GET /api/v2/mix/market/union-interest-rate-history`

限速规则：5次/秒/IP (IP)

获取利率记录

Operation ID: `classicContractMarketGetInterestRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种 |
| data.historyInterestRateList | object[] |  | 利率记录 |
| data.historyInterestRateList[].annualInterestRate | string |  | 年利率 |
| data.historyInterestRateList[].dailyInterestRate | string |  | 日利率 |
| data.historyInterestRateList[].ts | string |  | 日期 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725948522731,
  "data": {
    "coin": "USDT",
    "historyInterestRateList": [
      {
        "ts": "1723533015946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      },
      {
        "ts": "1723446615946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      },
      {
        "ts": "1723360215946",
        "annualInterestRate": "0.02555",
        "dailyInterestRate": "0.00007"
      }
    ]
  }
}
```

## 获取合约VIP费率

`GET /api/v2/mix/market/vip-fee-rate`

限速规则：10次/秒/IP

获取VIP费率

Operation ID: `classicContractMarketGetVIPFeeRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].level | string |  | VIP等级 |
| data[].dealAmount | string |  | 近30日累计成交额，USDT |
| data[].assetAmount | string |  | 资产总额，USDT |
| data[].takerFeeRate | string |  | taker费率, '0.000425' 表示 万4.25 |
| data[].makerFeeRate | string |  | maker费率, '0.00006' 表示 万0.6 |
| data[].btcWithdrawAmount | string |  | 24小时提币限额 (BTC) |
| data[].usdtWithdrawAmount | string |  | 24小时提币限额 (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794449789,
  "data": [
    {
      "level": "1",
      "dealAmount": "100000",
      "assetAmount": "50000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    },
    {
      "level": "2",
      "dealAmount": "200000",
      "assetAmount": "500000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    },
    {
      "level": "3",
      "dealAmount": "300000",
      "assetAmount": "1000000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "300",
      "usdtWithdrawAmount": "5000000"
    },
    {
      "level": "4",
      "dealAmount": "400000",
      "assetAmount": "2000000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "500",
      "usdtWithdrawAmount": "8500000"
    },
    {
      "level": "5",
      "dealAmount": "500000",
      "assetAmount": "3000000",
      "takerFeeRate": "0.0006",
      "makerFeeRate": "0.0004",
      "btcWithdrawAmount": "500",
      "usdtWithdrawAmount": "8500000"
    }
  ]
}
```

## 合并深度接口

`GET /api/v2/mix/market/merge-depth`

限速规则: 20次/1s (IP)

查询合并深度信息

合约深度历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetMergeDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对，BTCUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| precision | query | string |  | 价格精度，根据选择的精度作为步长返回累计深度，枚举值：<br><br>scale0/scale1/scale2/scale3<br><br>scale0 不合并，默认值<br><br>一般情况下，scale1为交易对报价精度*10的合并深度<br><br>一般情况下，scale2为报价精度*100<br><br>scale3为报价精度*1000<br><br>0/1/2/3对应的精度以实际返回参数“scale”为准,每个交易对的报价精度都不一样，部分币对并没有scale2，请求该币对不存在的scale将会按照最大scale处理。例：某个交易对只有scale 0/1，当请求scale2时自动降为scale1。 |
| limit | query | string |  | 固定档位枚举值：1/5/15/50/max，默认档位100，传入max返回该交易对的最大档位<br><br> 当实际深度不满足limit时，按实际档位返回。若传入max返回该交易对的最大档位 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.asks | string[][] |  | 当前价位的所有卖单<br><br>如["38084.5","0.5"] 中，"38084.5"代表深度价格，"0.5"代表基础币数量 [价格, 数量] |
| data.bids | string[][] |  | 当前价位的所有买单<br><br>如["38084.5","0.5"] 中，"38084.5"代表深度价格，"0.5"代表基础币数量 [价格, 数量] |
| data.precision | string |  | 当前档位，例：scale 1 |
| data.scale | string |  | 实际的精度值，例：0.1 |
| data.isMaxPrecision | string |  | YES 表示当前已经是最大精度，NO 非最大精度 |
| data.ts | string |  | 撮合引擎时间戳，Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695870963008,
  "data": {
    "asks": [
      [
        26347.5,
        0.25
      ],
      [
        26348,
        0.16
      ]
    ],
    "bids": [
      [
        26346.5,
        0.16
      ],
      [
        26346,
        0.32
      ]
    ],
    "ts": "1695870968804",
    "scale": "0.1",
    "precision": "scale0",
    "isMaxPrecision": "NO"
  }
}
```

## 获取单个交易对行情

`GET /api/v2/mix/market/ticker`

限速规则: 20次/1s (IP)

获取指定产品类型下，单个交易对的行情数据

Operation ID: `classicContractMarketGetTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对，BTCUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].lastPr | string |  | 最新成交价 |
| data[].askPr | string |  | 卖一价 |
| data[].bidPr | string |  | 买一价 |
| data[].bidSz | string |  | 买一量 |
| data[].askSz | string |  | 卖一量 |
| data[].high24h | string |  | 24小时最高价 |
| data[].low24h | string |  | 24小时最低价 |
| data[].ts | string |  | 当前数据时间戳 Unix时间戳的毫秒数格式，如 1597026383085 |
| data[].change24h | string |  | 24小时价格涨跌幅 |
| data[].baseVolume | string |  | 交易币交易量 |
| data[].quoteVolume | string |  | 计价币交易量 |
| data[].usdtVolume | string |  | usdt成交量 |
| data[].openUtc | string |  | 开盘价(UTC+0时区) |
| data[].changeUtc24h | string |  | 24小时价格涨跌幅(UTC+0时区) |
| data[].indexPrice | string |  | 指数价格 |
| data[].fundingRate | string |  | 资金费率 |
| data[].holdingAmount | string |  | 当前持仓, 单位是交易币(base coin)数量 |
| data[].open24h | string |  | 开盘价 24小时<br><br>开盘时间为24小时相对比，即：现在为2号19点，那么开盘时间对应为1号19点。 |
| data[].deliveryStartTime | string |  | 交割开始时间（仅限交割合约） |
| data[].deliveryTime | string |  | 交割时间（仅限交割合约） |
| data[].deliveryStatus | string |  | 交割状态, 仅限交割合约<br><br>`delivery_config_period`: 新上币对配置中<br><br>`delivery_normal`: 交易中<br><br>`delivery_before`: 交割前10分钟，禁止开仓<br><br>`delivery_period`: 交割中，禁止开平仓、撤单 |
| data[].markPrice | string |  | 标记价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794095685,
  "data": [
    {
      "symbol": "ETHUSDM26",
      "lastPr": "1829.3",
      "askPr": "1829.8",
      "bidPr": "1829.3",
      "bidSz": "0.054",
      "askSz": "0.785",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794098184",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "1822.15",
      "fundingRate": "0",
      "holdingAmount": "9488.49",
      "deliveryStartTime": "1693538723186",
      "deliveryTime": "1703836799000",
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "1829"
    }
  ]
}
```

## 获取全部交易对行情

`GET /api/v2/mix/market/tickers`

限速规则: 20次/1s (IP)

获取指定产品类型下，全部交易对的行情数据

Operation ID: `classicContractMarketGetAllSymbolTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].lastPr | string |  | 最新成交价 |
| data[].askPr | string |  | 卖一价 |
| data[].bidPr | string |  | 买一价 |
| data[].bidSz | string |  | 买一量 |
| data[].askSz | string |  | 卖一量 |
| data[].high24h | string |  | 24小时最高价 |
| data[].low24h | string |  | 24小时最低价 |
| data[].ts | string |  | 当前数据时间戳 Unix时间戳的毫秒数格式，如 1597026383085 |
| data[].change24h | string |  | 24小时价格涨跌幅 |
| data[].baseVolume | string |  | 交易币交易量 |
| data[].quoteVolume | string |  | 计价币交易量 |
| data[].usdtVolume | string |  | usdt成交量 |
| data[].openUtc | string |  | 开盘价(UTC+0时区) |
| data[].changeUtc24h | string |  | 24小时价格涨跌幅(UTC+0时区) |
| data[].indexPrice | string |  | 指数价格 |
| data[].fundingRate | string |  | 资金费率 |
| data[].holdingAmount | string |  | 当前持仓, 单位是交易币数量 |
| data[].open24h | string |  | 开盘价 24小时<br><br>开盘时间为24小时相对比，即：现在为2号19点，那么开盘时间对应为1号19点。 |
| data[].deliveryStartTime | string |  | 交割开始时间（仅限交割合约） |
| data[].deliveryTime | string |  | 交割时间（仅限交割合约） |
| data[].deliveryStatus | string |  | 交割状态, 仅限交割合约<br><br>`delivery_config_period`: 新上币对配置中<br><br>`delivery_normal`: 交易中<br><br>`delivery_before`: 交割前10分钟，禁止开仓<br><br>`delivery_period`: 交割中，禁止开平仓、撤单 |
| data[].markPrice | string |  | 标记价格 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695794269124,
  "data": [
    {
      "symbol": "BTCUSD",
      "lastPr": "29904.5",
      "askPr": "29904.5",
      "bidPr": "29903.5",
      "bidSz": "0.5091",
      "askSz": "2.2694",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794271400",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "29132.353333",
      "fundingRate": "-0.0007",
      "holdingAmount": "125.6844",
      "deliveryStartTime": null,
      "deliveryTime": null,
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "12345"
    },
    {
      "symbol": "ETHUSD_231229",
      "lastPr": "1829.3",
      "askPr": "1829.8",
      "bidPr": "1829.3",
      "bidSz": "0.054",
      "askSz": "0.785",
      "high24h": "0",
      "low24h": "0",
      "ts": "1695794271400",
      "change24h": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "usdtVolume": "0",
      "openUtc": "0",
      "changeUtc24h": "0",
      "indexPrice": "1822.15",
      "fundingRate": "0",
      "holdingAmount": "9488.49",
      "deliveryStartTime": "1693538723186",
      "deliveryTime": "1703836799000",
      "deliveryStatus": "delivery_normal",
      "open24h": "0",
      "markPrice": "1234"
    }
  ]
}
```

## 获取最近成交明细

`GET /api/v2/mix/market/fills`

限速规则: 20次/1s (IP)

获取最近100条平台成交记录<br/>合约成交历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetRecentFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| limit | query | string |  | 查询条数 默认100，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tradeId | string |  | 交易ID |
| data[].price | string |  | 价格 |
| data[].size | string |  | 数量(交易币) |
| data[].side | string |  | 交易方向<br><br>`buy`：买入<br><br>`sell`：卖出 |
| data[].ts | string |  | 当前数据时间戳 Unix时间戳的毫秒数格式，如 1597026383085 |
| data[].symbol | string |  | 币对名称，如"ETHUSDT" |

```json
{
  "code": "00000",
  "data": [
    {
      "tradeId": "1",
      "price": "29990.5",
      "size": "0.0166",
      "side": "sell",
      "ts": "1627116776464",
      "symbol": "BTCUSDT"
    },
    {
      "tradeId": "2",
      "price": "30007.0",
      "size": "0.0166",
      "side": "buy",
      "ts": "1627116600875",
      "symbol": "BTCUSDT"
    }
  ],
  "msg": "success",
  "requestTime": 1690313813709
}
```

## 获取成交明细

`GET /api/v2/mix/market/fills-history`

限速规则: 10次/1s (IP)

获取最近90天成交记录

startTime和endTime时间间隔不可超过7天

合约成交历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetFillsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| limit | query | string |  | 查询条数 默认500, 最大1000 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持一周，若不传结束时间，则默认结束时间为一周。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持一周，若不传开始时间，则默认开始时间为一周。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tradeId | string |  | tradeId, 降序排列 |
| data[].price | string |  | 价格 |
| data[].size | string |  | 数量, <br><br>特指交易币，如ETHUSDT中的ETH |
| data[].side | string |  | 交易方向<br><br>`sell`: 买入<br><br>`buy`: 卖出 |
| data[].ts | string |  | 当前数据时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085 |
| data[].symbol | string |  | 币对名称 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865481335,
  "data": [
    {
      "tradeId": "1",
      "price": "26372.5",
      "size": "9.25",
      "side": "Sell",
      "ts": "1695865151000",
      "symbol": "BTCUSDT"
    },
    {
      "tradeId": "2",
      "price": "26383",
      "size": "12.12",
      "side": "Buy",
      "ts": "1695865115000",
      "symbol": "BTCUSDT"
    }
  ]
}
```

## 获取K线数据

`GET /api/v2/mix/market/candles`

限速规则: 20次/1s (IP)

默认返回100条记录。若无数据则返回为空数组。可查询的数据历史，依据k线粒度而不同。

规则如下：

1m、3m、5m可查最久一个月 ;

15m可查最久52天;

30m可查最久62天;

1H可查最久83天;

2H可查最久120天;

4H可查最久240天;

6H可查最久360天<br/>合约K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| granularity | query | string | 是 | k线粒度<br><br>- 1m(1分钟)<br><br>- 3m(3分钟)<br><br>- 5m(5分钟)<br><br>- 15m(15分钟)<br><br>- 30m(30分钟)<br><br>- 1H(1小时)<br><br>- 4H(4小时)<br><br>- 6H(6小时)<br><br>- 12H(12小时)<br><br>- 1D(1天)<br><br>- 3D (3天)<br><br>- 1W(1周)<br><br>- 1M (月线)<br><br>- 6Hutc (零时区 6小时线)<br><br>- 12Hutc (零时区12小时线)<br><br>- 1Dutc (零时区 1日线)<br><br>- 3Dutc (零时区 3日线)<br><br>- 1Wutc (零时区 周线)<br><br>- 1Mutc (零时区 月线) |
| startTime | query | string |  | 开始时间 即查询该时间之后的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此开始时间之后的数据（最大时间查询范围为90天） |
| endTime | query | string |  | 结束时间 即查询该时间之前的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此结束时间之前的数据（最大时间查询范围为90天） |
| kLineType | query | string |  | k线类型：market 行情；mark 标记；index 指数；<br><br>默认 market |
| limit | query | string |  | 默认 100, 最大 1000 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] 时间戳, Unix时间戳的毫秒数格式，如 1597026383085<br><br>[1] 开盘价<br><br>[2] 最高价<br><br>[3] 最低价<br><br>[4] 收盘价, 最新一个收盘价可能还在持续更新，请订阅websocket跟踪最新价<br><br>[5] 交易币成交量<br><br>[6] 计价币成交量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865615662,
  "data": [
    [
      "1695835800000",
      "26210.5",
      "26210.5",
      "26194.5",
      "26194.5",
      "26.26",
      "687897.63"
    ],
    [
      "1695836100000",
      "26194.5",
      "26194.5",
      "26171",
      "26171",
      "17.98",
      "470618.72"
    ]
  ]
}
```

## 合约历史k线

`GET /api/v2/mix/market/history-candles`

限速规则: 20次/1s (IP)

查询所有的历史k线数据，最大返回200条数据。

注意：如果 endTime 超出某个 K 线周期边界（哪怕仅 1ms），系统可能会按周期向上取整计算数量，返回结果会额外包含该周期的一根 K 线（即数据起点可能会提前一个周期）。

合约K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetHistoryCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| granularity | query | string | 是 | k线粒度<br><br>- 1m(1分钟)<br><br>- 3m(3分钟)<br><br>- 5m(5分钟)<br><br>- 15m(15分钟)<br><br>- 30m(30分钟)<br><br>- 1H(1小时)<br><br>- 4H(4小时)<br><br>- 6H(6小时)<br><br>- 12H(12小时)<br><br>- 1D(1天)<br><br>- 3D (3天)<br><br>- 1W(1周)<br><br>- 1M (月线)<br><br>- 6Hutc (零时区 6小时线)<br><br>- 12Hutc (零时区12小时线)<br><br>- 1Dutc (零时区 1日线)<br><br>- 3Dutc (零时区 3日线)<br><br>- 1Wutc (零时区 周线)<br><br>- 1Mutc (零时区 月线) |
| startTime | query | string |  | 开始时间 即查询该时间之后的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此开始时间之后的数据（最大时间查询范围为90天） |
| endTime | query | string |  | 结束时间 即查询该时间之前的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此结束时间之前的数据（最大时间查询范围为90天） |
| limit | query | string |  | 默认100 最大200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] 时间戳, Unix时间戳的毫秒数格式，如 1597026383085<br><br>[1] 开盘价<br><br>[2] 最高价<br><br>[3] 最低价<br><br>[4] 收盘价（只包含已完结K线）<br><br>[5] 交易币成交量<br><br>[6] 计价币成交量 |

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

## 合约指数价格历史k线

`GET /api/v2/mix/market/history-index-candles`

限速规则: 20次/1s (IP)

查询合约指数价格历史k线数据，最大返回200条数据

合约指数价格K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetHistoryIndexCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| granularity | query | string | 是 | k线粒度<br><br>- 1m(1分钟)<br><br>- 3m(3分钟)<br><br>- 5m(5分钟)<br><br>- 15m(15分钟)<br><br>- 30m(30分钟)<br><br>- 1H(1小时)<br><br>- 4H(4小时)<br><br>- 6H(6小时)<br><br>- 12H(12小时)<br><br>- 1D(1天)<br><br>- 3D (3天)<br><br>- 1W(1周)<br><br>- 1M (月线)<br><br>- 6Hutc (零时区 6小时线)<br><br>- 12Hutc (零时区12小时线)<br><br>- 1Dutc (零时区 1日线)<br><br>- 3Dutc (零时区 3日线)<br><br>- 1Wutc (零时区 周线)<br><br>- 1Mutc (零时区 月线) |
| startTime | query | string |  | 开始时间 即查询该时间之后的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此开始时间之后的数据（最大时间查询范围为90天） |
| endTime | query | string |  | 结束时间 即查询该时间之前的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此结束时间之前的数据（最大时间查询范围为90天） |
| limit | query | string |  | 默认100 最大200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] 时间戳, Unix时间戳的毫秒数格式，如 1597026383085<br><br>[1] 开盘价<br><br>[2] 最高价<br><br>[3] 最低价<br><br>[4] 收盘价（只包含已完结K线）<br><br>[5] 交易币成交量<br><br>[6] 计价币成交量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695866039596,
  "data": [
    [
      "1691299500000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ],
    [
      "1691299800000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ]
  ]
}
```

## 合约标记价格历史k线

`GET /api/v2/mix/market/history-mark-candles`

限速规则: 20次/1s (IP)

查询合约标记价格历史k线数据，最大返回200条数据

合约标记价格K线历史数据可以通过我们官网<a href="https://www.bitget.com/zh-CN/data-download">下载</a>。

Operation ID: `classicContractMarketGetHistoryMarkCandleData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| granularity | query | string | 是 | k线粒度<br><br>- 1m(1分钟)<br><br>- 3m(3分钟)<br><br>- 5m(5分钟)<br><br>- 15m(15分钟)<br><br>- 30m(30分钟)<br><br>- 1H(1小时)<br><br>- 4H(4小时)<br><br>- 6H(6小时)<br><br>- 12H(12小时)<br><br>- 1D(1天)<br><br>- 3D (3天)<br><br>- 1W(1周)<br><br>- 1M (月线)<br><br>- 6Hutc (零时区 6小时线)<br><br>- 12Hutc (零时区12小时线)<br><br>- 1Dutc (零时区 1日线)<br><br>- 3Dutc (零时区 3日线)<br><br>- 1Wutc (零时区 周线)<br><br>- 1Mutc (零时区 月线) |
| startTime | query | string |  | 开始时间 即查询该时间之后的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此开始时间之后的数据（最大时间查询范围为90天） |
| endTime | query | string |  | 结束时间 即查询该时间之前的k线<br><br>需根据时间粒度不同，将对应时间单位向下取整来查询。<br><br>Unix时间戳的毫秒数格式，如 1672410780000<br><br>请求在此结束时间之前的数据（最大时间查询范围为90天） |
| limit | query | string |  | 默认100 最大200 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | [0] 时间戳, Unix时间戳的毫秒数格式，如 1597026383085<br><br>[1] 开盘价<br><br>[2] 最高价<br><br>[3] 最低价<br><br>[4] 收盘价（历史K线数据只包含完结K线）<br><br>[5] 交易币成交量<br><br>[6] 计价币成交量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695866282808,
  "data": [
    [
      "1691299500000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ],
    [
      "1691299800000",
      "29803",
      "29803",
      "29803",
      "29803",
      "0",
      "0"
    ]
  ]
}
```

## 获取交易对市价/指数/标记价格

`GET /api/v2/mix/market/symbol-price`

20次/S 根据ip限频

获取交易对的市价/指数/标记价格

Operation ID: `classicContractMarketGetSymbolPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].price | string |  | 最新成交价格 |
| data[].indexPrice | string |  | 指数价格 |
| data[].markPrice | string |  | 标记价格 |
| data[].ts | string |  | 当前数据时间戳 <br><br>Unix时间戳的毫秒数格式，如1672410780000 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695793384294,
  "data": [
    {
      "symbol": "BTCUSDT",
      "price": "26242",
      "indexPrice": "34867",
      "markPrice": "25555",
      "ts": "1695793390482"
    }
  ]
}
```

## 获取平台总持仓量

`GET /api/v2/mix/market/open-interest`

限速规则: 20次/1s (IP)

获取某交易对在平台的总持仓量

Operation ID: `classicContractMarketGetOpenInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.ts | string |  | 数据时间 Unix时间戳的毫秒数格式，如 <br><br>1672410780000 |
| data.openInterestList | object[] |  | 持仓量数据集合 |
| data.openInterestList[].symbol | string |  | 币对名称 |
| data.openInterestList[].size | string |  | 平台总持仓量 <br><br>特指交易币，如ETHUSDT中的ETH |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695867247823,
  "data": {
    "openInterestList": [
      {
        "symbol": "BTCUSDT",
        "size": "34207.31"
      }
    ],
    "ts": "1695867250684"
  }
}
```

## 获取当前资金费率

`GET /api/v2/mix/market/current-fund-rate`

限速规则: 20次/1s (IP)

获取合约的当前资金费率


GET /api/v2/mix/market/current-fund-rate

Operation ID: `classicContractMarketGetCurrentFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].fundingRate | string |  | 当前资金费率 |
| data[].fundingRateInterval | string |  | 资金费率结算周期<br><br>单位为小时。枚举值包括`1`,`2`,`4`,`8` `1`代表1小时，`2`代表2小时，以此类推 |
| data[].nextUpdate | string |  | 下次更新时间<br><br>Unix毫秒时间戳 |
| data[].minFundingRate | string |  | 资金费率下限<br><br>以小数形式返回。`0.025`为2.5% |
| data[].maxFundingRate | string |  | 资金费率上限<br><br>以小数形式返回。`0.025`为2.5% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743054548546,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000068",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003"
    }
  ]
}
```

## 获取历史资金费率

`GET /api/v2/mix/market/history-fund-rate`

限速规则: 20次/1s (IP)

获取合约的历史资金费率

Operation ID: `classicContractMarketGetHistoryFundingRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| pageSize | query | string |  | 查询条数 默认20，最大100。 |
| pageNo | query | string |  | 页码 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].fundingRate | string |  | 资金费率 |
| data[].fundingTime | string |  | 结算时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695796546319,
  "data": [
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.0005",
      "fundingTime": "1695776400000"
    },
    {
      "symbol": "BTCUSDT",
      "fundingRate": "0.000013",
      "fundingTime": "1695715200000"
    }
  ]
}
```

## 获取下次资金费结算时间

`GET /api/v2/mix/market/funding-time`

限速规则: 20次/1s (IP)

获取合约下一次的结算时间以及该合约的结算周期

Operation ID: `classicContractMarketGetSymbolNextFundingTime`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].nextFundingTime | string |  | 下次结算时间（毫秒） |
| data[].ratePeriod | string |  | 费率结算周期<br><br>单位为小时。 |

```json
{
  "code": "00000",
  "data": [
    {
      "symbol": "BTCUSDT",
      "nextFundingTime": "1627311600000",
      "ratePeriod": "8"
    }
  ],
  "msg": "success",
  "requestTime": 1627291915767
}
```

## 获取合约信息

`GET /api/v2/mix/market/contracts`

限频规则：20次/秒/IP

获取合约详情信息。

Operation ID: `classicContractMarketGetAllSymbolsContracts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 产品名称 |
| data[].baseCoin | string |  | 基础币 <br><br>如 ETHUSDT 中，特指ETH |
| data[].quoteCoin | string |  | 计价币<br><br>如 ETHUSDT 中，特指USDT |
| data[].buyLimitPriceRatio | string |  | 买价限价比例 |
| data[].sellLimitPriceRatio | string |  | 卖价限价比例 |
| data[].feeRateUpRatio | string |  | 手续费上浮比例 |
| data[].makerFeeRate | string |  | maker手续费率 |
| data[].takerFeeRate | string |  | taker手续费率 |
| data[].openCostUpRatio | string |  | 开仓成本上浮比例 |
| data[].supportMarginCoins | string[] |  | 支持保证金币种 |
| data[].minTradeNum | string |  | 最小开单数量(基础币) |
| data[].priceEndStep | string |  | 价格步长 |
| data[].volumePlace | string |  | 数量小数位 |
| data[].pricePlace | string |  | 价格小数位 |
| data[].sizeMultiplier | string |  | 数量乘数 下单数量要大于 minTradeNum 并且满足 sizeMulti 的倍数 |
| data[].symbolType | string |  | 合约类型 <br><br>perpetual 永续 <br><br>delivery交割 |
| data[].minTradeUSDT | string |  | 最小USDT交易额 |
| data[].maxSymbolOrderNum | string |  | 最大持有订单数（symbol维度） |
| data[].maxProductOrderNum | string |  | 最大持有订单数（产品类型维度） |
| data[].maxPositionNum | string |  | 最大持有仓位数量 |
| data[].symbolStatus | string |  | 交易对状态 <br><br>`listed` 上架 <br><br>`normal` 正常/开盘 <br><br> `maintain` 禁止交易(禁止开平仓) <br><br>`limit_open` 限制下单(可平仓)<br><br> `restrictedAPI` API限制下单<br><br> `off` 下架 |
| data[].offTime | string |  | 停盘时间, '-1' 表示正常 |
| data[].limitOpenTime | string |  | 可开仓时间, '-1' 表示正常; 其它值表示symbol正在/计划维护，指定时间后禁止交易 |
| data[].deliveryTime | string |  | 交割时间 |
| data[].deliveryStartTime | string |  | 交割开始时间 |
| data[].deliveryPeriod | string |  | 交割周期 <br><br>`this_quarter`当季 <br><br>`next_quarter`次季 |
| data[].launchTime | string |  | 上架时间 |
| data[].fundInterval | string |  | 资金费结算周期，每小时/每8小时 |
| data[].minLever | string |  | 最小杠杆 |
| data[].maxLever | string |  | 最大杠杆 |
| data[].posLimit | string |  | 持仓限制 (已废弃) |
| data[].maintainTime | string |  | 维护时间（状态处于维护/即将维护时会有值） |
| data[].maxMarketOrderQty | string |  | 单笔市价单最大下单数量<br><br> 指以基础币种下单时允许的最大数量 |
| data[].maxOrderQty | string |  | 单笔限价单最大下单数量<br><br> 指以基础币种下单时允许的最大数量 |
| data[].isRwa | string |  | 是否为RWA交易对<br><br>`YES` 是<br><br>`NO` 否 |
| data[].openTime | string |  | 该字段已废弃 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695793701269,
  "data": [
    {
      "symbol": "BTCUSDT",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "buyLimitPriceRatio": "0.9",
      "sellLimitPriceRatio": "0.9",
      "feeRateUpRatio": "0.1",
      "makerFeeRate": "0.0004",
      "takerFeeRate": "0.0006",
      "openCostUpRatio": "0.1",
      "supportMarginCoins": [
        "USDT"
      ],
      "minTradeNum": "0.01",
      "priceEndStep": "1",
      "volumePlace": "2",
      "pricePlace": "1",
      "sizeMultiplier": "0.01",
      "symbolType": "perpetual",
      "minTradeUSDT": "5",
      "maxSymbolOrderNum": "999999",
      "maxProductOrderNum": "999999",
      "maxPositionNum": "150",
      "symbolStatus": "normal",
      "offTime": "-1",
      "limitOpenTime": "-1",
      "deliveryTime": "",
      "deliveryStartTime": "",
      "deliveryPeriod": "",
      "launchTime": "",
      "fundInterval": "8",
      "minLever": "1",
      "maxLever": "125",
      "posLimit": "0.05",
      "maintainTime": "1680165535278",
      "openTime": "",
      "maxMarketOrderQty": "220",
      "maxOrderQty": "1200",
      "isRwa": "YES"
    }
  ]
}
```

## 获取合约OI限仓信息

`GET /api/v2/mix/market/oi-limit`

限频规则：10次/秒/IP

获取合约OI限仓信息。

Operation ID: `classicContractMarketGetContractsOi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易币对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

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

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741596239587,
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "100000",
      "totalNotionalValue": "200000"
    },
    {
      "symbol": "BCHUSDT",
      "notionalValue": "100000",
      "totalNotionalValue": "200000"
    }
  ]
}
```