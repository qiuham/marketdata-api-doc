---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-common-apidata
api_type: REST
updated_at: 2026-11-23 19:02:21.439506
---

# Classic Trading Insights API

Public trading insights endpoints — long/short ratios, fund flow, and margin data.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/account-long-short` — Get Futures Active Long Short Account Data
- `GET /api/v2/spot/market/fund-net-flow` — Get Spot 24H Net Capital Inflow Info
- `GET /api/v2/spot/market/support-symbols` — Get Trade data support symbols
- `GET /api/v2/spot/market/fund-flow` — Get spot fund flow
- `GET /api/v2/mix/market/long-short` — Get Futures Long and Short Ratio Data
- `GET /api/v2/margin/market/isolated-borrow-rate` — Get Isolated margin borrowing ratio Data
- `GET /api/v2/margin/market/loan-growth` — Get Margin loan growth rate Data
- `GET /api/v2/margin/market/long-short-ratio` — Get Leveraged long-short ratio Data
- `GET /api/v2/mix/market/position-long-short` — Get Futures Active Long Short Position Data
- `GET /api/v2/mix/market/taker-buy-sell` — Get Futures Active Buy Sell Volume Data
- `GET /api/v2/spot/market/whale-net-flow` — Get Spot Whale Net Flow Data

## Get Futures Active Long Short Account Data

`GET /api/v2/mix/market/account-long-short`

Rate limit: 1 req/s (IP)

Operation ID: `classicCommonApidataAccountLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | - default:5m, support:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longAccountRatio | string |  | Long Account Ratio |
| data[].shortAccountRatio | string |  | Short Account Ratio |
| data[].longShortAccountRatio | string |  | Long Short Account Ratio |
| data[].ts | string |  | Millseconds time |

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
    },
    {
      "longAccountRatio": "0.01",
      "shortAccountRatio": "0.12",
      "longShortAccountRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Spot 24H Net Capital Inflow Info

`GET /api/v2/spot/market/fund-net-flow`

Rate limit: 1 req/s (IP)

Operation ID: `classicCommonApidataFundNetFlow`

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
| data[].ts | string |  | Millseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    }
  ]
}
```

## Get Trade data support symbols

`GET /api/v2/spot/market/support-symbols`

Rate limit: 1 req/1s (IP)

Operation ID: `classicCommonApidataGetBigDataSymbol`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.spotList | string[] |  | Spot data symbols |
| data.futureList | string[] |  | Futures data symbols |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "spotList": [
      "BTCUSDT",
      "ETHUSDT"
    ],
    "futureList": [
      "BTCUSDT",
      "ETHUSDT"
    ]
  }
}
```

## Get spot fund flow

`GET /api/v2/spot/market/fund-flow`

Rate limit: 1 req/1s (IP)

Operation ID: `classicCommonApidataGetSpotFundFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, BTCUSDT |
| period | query | string |  | Query period: 15m(default),30m,1h,2h,4h,1d |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.whaleBuyVolume | string |  | Whale buy volume |
| data.dolphinBuyVolume | string |  | Dolphin Buy Volume |
| data.fishBuyVolume | string |  | Fish Buy Volume |
| data.whaleSellVolume | string |  | Whale Sell Volume |
| data.dolphinSellVolume | string |  | Dolphin Sell Volume |
| data.fishSellVolume | string |  | Fish Sell Volume |
| data.whaleBuyRatio | string |  | Whale Buy Ratio |
| data.dolphinBuyRatio | string |  | Dolphin Buy Ratio |
| data.fishBuyRatio | string |  | Fish Buy Ratio |
| data.whaleSellRatio | string |  | Whale Sell Ratio |
| data.dolphinSellRatio | string |  | Dolphin Sell Ratio |
| data.fishSellRatio | string |  | Fish Sell Ratio |

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

## Get Futures Long and Short Ratio Data

`GET /api/v2/mix/market/long-short`

Rate limit: 1 req/1s (IP)

Operation ID: `classicCommonApidataLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | - default:5m, support:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1Dutc` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longRatio | string |  | Long Ratio |
| data[].shortRatio | string |  | Short Ratio |
| data[].longShortRatio | string |  | Long Short Ratio |
| data[].ts | string |  | Millseconds time |

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
    },
    {
      "longRatio": "0.01",
      "shortRatio": "0.12",
      "longShortRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Isolated margin borrowing ratio Data

`GET /api/v2/margin/market/isolated-borrow-rate`

Frequency limit: 1 times/1s (IP)

The ratio of borrowed amount in the base currency (left) and borrowed amount in the quote currency (right) in isolated margin accounts, converted to USDT.

Operation ID: `classicCommonApidataMarginIsoBorrowRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:`24h`, support: <br><br> `24h`<br><br> `30d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].borrowRate | string |  | borrow ratio |
| data[].ts | string |  | Millseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "borrowRate": "-0.96"
    },
    {
      "ts": "1713942000000",
      "borrowRate": "-0.96"
    }
  ]
}
```

## Get Margin loan growth rate Data

`GET /api/v2/margin/market/loan-growth`

Frequency limit: 1 times/1s (IP)

The growth rate of borrowed funds for a specific coin in cross and isolated margin accounts.

Operation ID: `classicCommonApidataMarginLoanGrowth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:`24h`, support: <br><br> `24h`<br><br> `30d` |
| coin | query | string |  | Base coin or quete coin, default: base coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].growthRate | string |  | growth ratio |
| data[].ts | string |  | Millseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "growthRate": "-0.96"
    },
    {
      "ts": "1713942000000",
      "growthRate": "-0.96"
    }
  ]
}
```

## Get Leveraged long-short ratio Data

`GET /api/v2/margin/market/long-short-ratio`

Frequency limit: 1 times/1s (IP)

The long-short position ratio for a specific coin in cross and isolated margin accounts.

Operation ID: `classicCommonApidataMarginLsRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | Default:`24h`, support: <br><br> `24h`<br><br> `30d` |
| coin | query | string |  | Base coin or quete coin, default: base coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longShortRatio | string |  | long short ratio |
| data[].ts | string |  | Millseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "longShortRatio": "-0.96"
    },
    {
      "ts": "1713942000000",
      "longShortRatio": "-0.96"
    }
  ]
}
```

## Get Futures Active Long Short Position Data

`GET /api/v2/mix/market/position-long-short`

Rate limit: 1 req/s (IP)

Operation ID: `classicCommonApidataPositionLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | - default:5m, support:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longPositionRatio | string |  | Long Position Ratio |
| data[].shortPositionRatio | string |  | Short Position Ratio |
| data[].longShortPositionRatio | string |  | Long Short Position Ratio |
| data[].ts | string |  | Millseconds time |

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
    },
    {
      "longPositionRatio": "0.01",
      "shortPositionRatio": "0.12",
      "longShortPositionRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Futures Active Buy Sell Volume Data

`GET /api/v2/mix/market/taker-buy-sell`

Rate limit: 1 req/s (IP)

Operation ID: `classicCommonApidataTakerBuySell`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| period | query | string |  | - default:5m, support:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].buyVolume | string |  | Buy volume |
| data[].sellVolume | string |  | Sell Volume |
| data[].ts | string |  | Millseconds time |

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
    },
    {
      "buyVolume": "0.01",
      "sellVolume": "0.12",
      "ts": "1714020600000"
    }
  ]
}
```

## Get Spot Whale Net Flow Data

`GET /api/v2/spot/market/whale-net-flow`

Rate limit: 1 req/s (IP)

Operation ID: `classicCommonApidataWhaleNetFlow`

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
| data[].date | string |  | Millseconds time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    }
  ]
}
```


---

公共交易大数据接口 —— 多空比、资金流向与杠杆借贷数据。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/account-long-short` — 获取合约大户账户多空比信息
- `GET /api/v2/spot/market/fund-net-flow` — 获取现货24小时资金净流入信息
- `GET /api/v2/spot/market/support-symbols` — 获取交易行情数据支持交易对信息
- `GET /api/v2/spot/market/fund-flow` — 获取现货资金流向信息
- `GET /api/v2/mix/market/long-short` — 获取合约多空比信息
- `GET /api/v2/margin/market/isolated-borrow-rate` — 获取杠杆逐仓借贷比信息
- `GET /api/v2/margin/market/loan-growth` — 获取杠杆借贷存量增速信息
- `GET /api/v2/margin/market/long-short-ratio` — 获取杠杆多空对比信息
- `GET /api/v2/mix/market/position-long-short` — 获取合约大户持仓量多空比信息
- `GET /api/v2/mix/market/taker-buy-sell` — 获取合约主动买卖量信息
- `GET /api/v2/spot/market/whale-net-flow` — 获取现货每日大单净流入信息

## 获取合约大户账户多空比信息

`GET /api/v2/mix/market/account-long-short`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataAccountLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | - 默认值5m, 支持:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

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
| data[].ts | string |  | 时间 |

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
    },
    {
      "longAccountRatio": "0.01",
      "shortAccountRatio": "0.12",
      "longShortAccountRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取现货24小时资金净流入信息

`GET /api/v2/spot/market/fund-net-flow`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataFundNetFlow`

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
| data | object[] |  |  |
| data[].netFlow | string |  | 买入卖出量(左币) |
| data[].ts | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    },
    {
      "netFlow": "-1.1",
      "ts": "1713942000000"
    }
  ]
}
```

## 获取交易行情数据支持交易对信息

`GET /api/v2/spot/market/support-symbols`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataGetBigDataSymbol`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.spotList | string[] |  | 现货交易对列表 |
| data.futureList | string[] |  | 合约交易对列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "spotList": [
      "BTCUSDT",
      "ETHUSDT"
    ],
    "futureList": [
      "BTCUSDT",
      "ETHUSDT"
    ]
  }
}
```

## 获取现货资金流向信息

`GET /api/v2/spot/market/fund-flow`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataGetSpotFundFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
| period | query | string |  | 查询周期：支持15m（默认），30m，1h，2h，4h，1d |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.whaleBuyVolume | string |  | 大单买入量 |
| data.dolphinBuyVolume | string |  | 中单买入量 |
| data.fishBuyVolume | string |  | 小单买入量 |
| data.whaleSellVolume | string |  | 大单卖出量 |
| data.dolphinSellVolume | string |  | 中单卖出量 |
| data.fishSellVolume | string |  | 小单卖出量 |
| data.whaleBuyRatio | string |  | 大单买入占比 |
| data.dolphinBuyRatio | string |  | 中单买入占比 |
| data.fishBuyRatio | string |  | 小单买入占比 |
| data.whaleSellRatio | string |  | 大单卖出占比 |
| data.dolphinSellRatio | string |  | 中单卖出占比 |
| data.fishSellRatio | string |  | 小单卖出占比 |

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

## 获取合约多空比信息

`GET /api/v2/mix/market/long-short`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | - 默认值5m, 支持:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1Dutc` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longRatio | string |  | 多仓人数比例 |
| data[].shortRatio | string |  | 空仓人数比例 |
| data[].longShortRatio | string |  | 多空比 |
| data[].ts | string |  | 时间 |

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
    },
    {
      "longRatio": "0.01",
      "shortRatio": "0.12",
      "longShortRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取杠杆逐仓借贷比信息

`GET /api/v2/margin/market/isolated-borrow-rate`

限速规则 1次/1s (IP)

逐仓账户中基础币（左币）借贷量与计价币（右币）借贷量转换为USDT 后的比值

Operation ID: `classicCommonApidataMarginIsoBorrowRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | 默认值: `24h`, 支持:<br><br> `24h`<br><br> `30d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].borrowRate | string |  | 借贷比 |
| data[].ts | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "borrowRate": "-0.96"
    },
    {
      "ts": "1713942000000",
      "borrowRate": "-0.96"
    }
  ]
}
```

## 获取杠杆借贷存量增速信息

`GET /api/v2/margin/market/loan-growth`

限速规则 1次/1s (IP)

获取杠杆借贷存量增速信息

Operation ID: `classicCommonApidataMarginLoanGrowth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | 默认值: `24h`, 支持:<br><br> `24h`<br><br> `30d` |
| coin | query | string |  | 基础币或计价币。若不填写，则默认为基础币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].growthRate | string |  | 存量增长率 |
| data[].ts | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "growthRate": "-0.96"
    },
    {
      "ts": "1713942000000",
      "growthRate": "-0.96"
    }
  ]
}
```

## 获取杠杆多空对比信息

`GET /api/v2/margin/market/long-short-ratio`

限速规则 1次/1s (IP)

获取杠杆多空对比信息

Operation ID: `classicCommonApidataMarginLsRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | 默认值: `24h`, 支持:<br><br> `24h`<br><br> `30d` |
| coin | query | string |  | 基础币或计价币。若不填写，则默认为基础币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longShortRatio | string |  | 多空比例 |
| data[].ts | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "ts": "1713942000000",
      "longShortRatio": "-0.96"
    },
    {
      "ts": "1713942000000",
      "longShortRatio": "-0.96"
    }
  ]
}
```

## 获取合约大户持仓量多空比信息

`GET /api/v2/mix/market/position-long-short`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataPositionLongShort`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | - 默认值5m, 支持:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].longPositionRatio | string |  | 多仓仓位比例 |
| data[].shortPositionRatio | string |  | 空仓仓位比例 |
| data[].longShortPositionRatio | string |  | 多空仓位比 |
| data[].ts | string |  | 时间 |

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
    },
    {
      "longPositionRatio": "0.01",
      "shortPositionRatio": "0.12",
      "longShortPositionRatio": "1.2",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取合约主动买卖量信息

`GET /api/v2/mix/market/taker-buy-sell`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataTakerBuySell`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| period | query | string |  | - 默认值5m, 支持:<br><br> `5m`<br><br> `15m`<br><br> `30m`<br><br> `1h`<br><br> `2h`<br><br> `4h`<br><br> `6h`<br><br> `12h`<br><br>  `1d` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].buyVolume | string |  | 主动买入量(左币) |
| data[].sellVolume | string |  | 主动卖出量(左币) |
| data[].ts | string |  | 时间 |

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
    },
    {
      "buyVolume": "0.01",
      "sellVolume": "0.12",
      "ts": "1714020600000"
    }
  ]
}
```

## 获取现货每日大单净流入信息

`GET /api/v2/spot/market/whale-net-flow`

限速规则 1次/1s (IP)

Operation ID: `classicCommonApidataWhaleNetFlow`

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
| data | object[] |  |  |
| data[].volume | string |  | 买入卖出量(左币) |
| data[].date | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": [
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    },
    {
      "volume": "-1.1",
      "date": "1713942000000"
    }
  ]
}
```