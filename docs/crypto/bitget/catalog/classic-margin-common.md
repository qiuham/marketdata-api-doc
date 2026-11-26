---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-common
api_type: REST
updated_at: 2026-11-26 19:03:52.313853
---

# Classic Margin Common API

Classic account — margin interest rates & supported currencies.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/interest-rate-record` — Get the leverage interest rate
- `GET /api/v2/margin/currencies` — Get Support Currencies

## Get the leverage interest rate

`GET /api/v2/margin/interest-rate-record`

Frequency limit:10 times/1s (IP)

Operation ID: `classicMarginCommonInterestRateRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | coin |
| data.dailyInterestRate | string |  | Daily interest rate<br><br>Return in decimal form with 8 decimal places. |
| data.annualInterestRate | string |  | Annual interest rate<br><br>Return in decimal form with 8 decimal places. |
| data.updatedTime | string |  | Update time<br><br>In Unix timestamp format in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746692917537,
  "data": {
    "coin": "BTC",
    "dailyInterestRate": "0.00003000",
    "annualInterestRate": "0.01095000",
    "updatedTime": "1746690900381"
  }
}
```

## Get Support Currencies

`GET /api/v2/margin/currencies`

Frequency limit:10 times/1s (IP)

Operation ID: `classicMarginCommonSupportCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].baseCoin | string |  | Base currency |
| data[].quoteCoin | string |  | Quote currency |
| data[].maxCrossedLeverage | string |  | Cross margin maximum leverage multiples |
| data[].maxIsolatedLeverage | string |  | Cross margin maximum leverage multiples |
| data[].warningRiskRatio | string |  | Warning risk ratio |
| data[].liquidationRiskRatio | string |  | Liquidation risk ratio |
| data[].minTradeAmount | string |  | Minimum trading volume |
| data[].maxTradeAmount | string |  | Maximum trading volume |
| data[].takerFeeRate | string |  | Taker rates |
| data[].makerFeeRate | string |  | Maker rates |
| data[].pricePrecision | string |  | Pricing precision |
| data[].quantityPrecision | string |  | Amount precision |
| data[].minTradeUSDT | string |  | Minimum trading volume (USDT) |
| data[].~~isBorrowable~~ | string |  | Borrowable or not(ignore) |
| data[].userMinBorrow | string |  | Minimum borrowing |
| data[].status | string |  | 1: tradable 2: under temporary maintenance |
| data[].isIsolatedBaseBorrowable | string |  | isolate base coin borrowable or not? |
| data[].isIsolatedQuoteBorrowable | string |  | isolate quote coin borrowable or not? |
| data[].isCrossBorrowable | string |  | corss borrowable or not? |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679383565084,
  "data": [
    {
      "symbol": "ETHUSDT",
      "baseCoin": "ETH",
      "quoteCoin": "USDT",
      "maxCrossedLeverage": "3",
      "maxIsolatedLeverage": "10",
      "warningRiskRatio": "0.80000000",
      "liquidationRiskRatio": "1.00000000",
      "minTradeAmount": "0.00010000",
      "maxTradeAmount": "10000.00000000",
      "takerFeeRate": "0.00100000",
      "makerFeeRate": "0.00100000",
      "pricePrecision": "4",
      "quantityPrecision": "4",
      "minTradeUSDT": "5.00000000",
      "isBorrowable": true,
      "userMinBorrow": "0.00000001",
      "status": "1",
      "isIsolatedBaseBorrowable": true,
      "isIsolatedQuoteBorrowable": true,
      "isCrossBorrowable": true
    }
  ]
}
```


---

经典账户 — 杠杆利率与支持币种。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/interest-rate-record` — 获取杠杆利率
- `GET /api/v2/margin/currencies` — 获取支持杠杆的所有交易对

## 获取杠杆利率

`GET /api/v2/margin/interest-rate-record`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCommonInterestRateRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.dailyInterestRate | string |  | 日利率<br><br>小数形式返回，8位精度 |
| data.annualInterestRate | string |  | 年利率<br><br>小数形式返回，8位精度 |
| data.updatedTime | string |  | 数据更新时间<br><br>Unix毫秒时间戳格式 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746692917537,
  "data": {
    "coin": "BTC",
    "dailyInterestRate": "0.00003000",
    "annualInterestRate": "0.01095000",
    "updatedTime": "1746690900381"
  }
}
```

## 获取支持杠杆的所有交易对

`GET /api/v2/margin/currencies`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCommonSupportCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].baseCoin | string |  | 基础币 |
| data[].quoteCoin | string |  | 计价币 |
| data[].maxCrossedLeverage | string |  | 全仓最大杠杆倍数 |
| data[].maxIsolatedLeverage | string |  | 逐仓最大杠杆倍数 |
| data[].warningRiskRatio | string |  | 预警风险率 |
| data[].liquidationRiskRatio | string |  | 强平风险率 |
| data[].minTradeAmount | string |  | 最小交易金额 |
| data[].maxTradeAmount | string |  | 最大交易金额 |
| data[].takerFeeRate | string |  | 吃单方费率 |
| data[].makerFeeRate | string |  | 挂单方费率 |
| data[].pricePrecision | string |  | 价格精度 |
| data[].quantityPrecision | string |  | 数量精度 |
| data[].minTradeUSDT | string |  | 最小交易usdt |
| data[].~~isBorrowable~~ | string |  | 是否可借（可忽略） |
| data[].userMinBorrow | string |  | 最小借款 |
| data[].status | string |  | 1:可交易 2:临时维护 |
| data[].isIsolatedBaseBorrowable | string |  | 逐仓右币是否可借 |
| data[].isIsolatedQuoteBorrowable | string |  | 逐仓左币是否可借 |
| data[].isCrossBorrowable | string |  | 全仓是否可借 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679383565084,
  "data": [
    {
      "symbol": "ETHUSDT",
      "baseCoin": "ETH",
      "quoteCoin": "USDT",
      "maxCrossedLeverage": "3",
      "maxIsolatedLeverage": "10",
      "warningRiskRatio": "0.80000000",
      "liquidationRiskRatio": "1.00000000",
      "minTradeAmount": "0.00010000",
      "maxTradeAmount": "10000.00000000",
      "takerFeeRate": "0.00100000",
      "makerFeeRate": "0.00100000",
      "pricePrecision": "4",
      "quantityPrecision": "4",
      "minTradeUSDT": "5.00000000",
      "isBorrowable": true,
      "userMinBorrow": "0.00000001",
      "status": "1",
      "isIsolatedBaseBorrowable": true,
      "isIsolatedQuoteBorrowable": true,
      "isCrossBorrowable": true
    }
  ]
}
```