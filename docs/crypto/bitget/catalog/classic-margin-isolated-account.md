---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-isolated-account
api_type: REST
updated_at: 2026-11-18 08:37:59.722349
---

# Classic Isolated Margin Account API

Classic account — isolated margin borrow/repay & assets.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/isolated/account/assets` — Get Isolated Account Asset
- `POST /api/v2/margin/isolated/account/borrow` — Isolated Borrow
- `POST /api/v2/margin/isolated/account/repay` — Isolated Repay
- `GET /api/v2/margin/isolated/account/risk-rate` — Get Isolated Risk Rate
- `GET /api/v2/margin/isolated/interest-rate-and-limit` — Get Isolated Interest Rate and Max Borrowable
- `GET /api/v2/margin/isolated/tier-data` — Get Isolated Tier Configuration
- `GET /api/v2/margin/isolated/account/max-borrowable-amount` — Get Isolated Max Borrowable
- `GET /api/v2/margin/isolated/account/max-transfer-out-amount` — Get Isolated Max Transferable
- `POST /api/v2/margin/isolated/account/flash-repay` — Isolated Flash Repay
- `POST /api/v2/margin/isolated/account/query-flash-repay-status` — Query Isolated Flash Repayment Result

## Get Isolated Account Asset

`GET /api/v2/margin/isolated/account/assets`

Frequency limit: 10 times/1s (UID)

Getting account asset

Operation ID: `classicMarginIsolatedAccountGetIsolatedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pairs, like BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].symbol | string |  | Trading pair name |
| data[].totalAmount | string |  | Total amount |
| data[].available | string |  | Available amount |
| data[].frozen | string |  | Assets frozen |
| data[].borrow | string |  | Borrow |
| data[].interest | string |  | Interest, Interest-only payments with a minimum payment of interest. |
| data[].net | string |  | Net assets = available + frozen &minus; borrow &minus; interest. Liquidation is triggered when the risk ratio is reached 1. |
| data[].coupon | string |  | Trading bonus |
| data[].cTime | string |  | Creation time |
| data[].uTime | string |  | Update time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694588056713,
  "data": [
    {
      "symbol": "BTCUSDT",
      "coin": "BTC",
      "totalAmount": "19876.1798394",
      "available": "19876.1798394",
      "frozen": "0",
      "borrow": "0",
      "interest": "0",
      "net": "19876.1798394",
      "coupon": "0",
      "cTime": "1692085312298",
      "uTime": "1694569802151"
    }
  ]
}
```

## Isolated Borrow

`POST /api/v2/margin/isolated/account/borrow`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Borrowing trading pairs, like BTCUSDT |
| coin | string | 是 | Borrowing coins, such as BTC |
| borrowAmount | string | 是 | Borrowing amount (up to 8 decimal places) |
| clientOid | string |  | Client customized ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanId | string |  | Loan ID |
| data.coin | string |  | Borrowing coin |
| data.borrowAmount | string |  | Borrowing amount |
| data.symbol | string |  | Borrowing trading pair |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": {
    "loanId": "123412412452345",
    "symbol": "BTCUSDT",
    "coin": "USDT",
    "borrowAmount": "1.00000000"
  }
}
```

## Isolated Repay

`POST /api/v2/margin/isolated/account/repay`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayAmount | string | 是 | Number of repayments, up to 8 decimal places |
| coin | string | 是 | Repayment coin |
| symbol | string | 是 | Repayment trading pairs, like BTCUSDT |
| clientOid | string |  | Client customized ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.remainDebtAmount | string |  | Remaining borrowings |
| data.repayId | string |  | Repayment ID |
| data.symbol | string |  | Trading pair |
| data.coin | string |  | Coin |
| data.repayAmount | string |  | Repayment amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694588859956,
  "data": {
    "remainDebtAmount": "0",
    "symbol": "BTCUSDT",
    "repayId": "1234234234234",
    "coin": "USDT",
    "repayAmount": "1"
  }
}
```

## Get Isolated Risk Rate

`GET /api/v2/margin/isolated/account/risk-rate`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedRiskRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pairs, like BTCUSDT |
| pageNum | query | string |  | Page number, Default: 1 |
| pageSize | query | string |  | Size per page, default 100, maximum 500 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].riskRateRatio | string |  | Risk ratio (total assets/total liabilities under isolated mode) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694590583906,
  "data": [
    {
      "symbol": "BTCUSDT",
      "riskRateRatio": "0"
    }
  ]
}
```

## Get Isolated Interest Rate and Max Borrowable

`GET /api/v2/margin/isolated/interest-rate-and-limit`

Frequency limit:10 times/1s (UID)

This interface will determine the user's VIP level based on the User ID sending the request, and then return information such as interest rates and limits based on the VIP level.

Operation ID: `classicMarginIsolatedAccountIsolatedMarginInterestRateAndMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].baseCoin | string |  | Base currency |
| data[].leverage | string |  | Leverage: default: 10 |
| data[].baseTransferable | boolean |  | Is the base currency transferable?<br><br>true: Transferable<br><br>false: Not transferable |
| data[].baseBorrowable | boolean |  | Whether or not the base currency can be borrowed?<br><br>true: Borrowable<br><br>false: Not borrowable |
| data[].baseDailyInterestRate | string |  | Non-VIP daily interest rate of the base currency |
| data[].baseAnnuallyInterestRate | string |  | Non-VIP APR of the base currency |
| data[].baseMaxBorrowableAmount | string |  | Maximum borrow in base currency |
| data[].baseVipList | object[] |  | Base currency VIP |
| data[].baseVipList[].level | string |  | VIP level |
| data[].baseVipList[].limit | string |  | VIP limit |
| data[].baseVipList[].dailyInterestRate | string |  | VIP daily interest rate |
| data[].baseVipList[].annuallyInterestRate | string |  | VIP APR |
| data[].baseVipList[].discountRate | string |  | VIP discount: 1 is for 100%, i.e. no discount; 0.97 is for 97% of the original rate |
| data[].quoteCoin | string |  | Quote currency |
| data[].quoteTransferable | boolean |  | Whether the quote currency is transferable |
| data[].quoteBorrowable | boolean |  | Whether the quote currency is borrowable |
| data[].quoteDailyInterestRate | string |  | Non-VIP daily interest rate of the quote currency |
| data[].quoteAnnuallyInterestRate | string |  | Non-VIP APR of the quote currency |
| data[].quoteMaxBorrowableAmount | string |  | Non-VIP maximum borrow in quote currency |
| data[].quoteList | object[] |  | Quote currency VIP |
| data[].quoteList[].level | string |  | VIP level |
| data[].quoteList[].limit | string |  | VIP limit |
| data[].quoteList[].dailyInterestRate | string |  | VIP daily interest rate |
| data[].quoteList[].annuallyInterestRate | string |  | VIP APR |
| data[].quoteList[].discountRate | string |  | VIP discount: 1 is for 100%, i.e. no discount; 0.97 is for 97% of the original rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694579779768,
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "5",
      "baseCoin": "BTC",
      "baseTransferable": true,
      "baseBorrowable": true,
      "baseDailyInterestRate": "0.00007113",
      "baseAnnuallyInterestRate": "0.02596245",
      "baseMaxBorrowableAmount": "0",
      "baseVipList": [
        {
          "level": "0",
          "dailyInterestRate": "0.00007333",
          "limit": "0",
          "annuallyInterestRate": "0.02676545",
          "discountRate": "1"
        }
      ],
      "quoteCoin": "USDT",
      "quoteTransferable": true,
      "quoteBorrowable": true,
      "quoteDailyInterestRate": "0.00011963",
      "quoteAnnuallyInterestRate": "0.04366495",
      "quoteMaxBorrowableAmount": "0",
      "quoteList": [
        {
          "level": "0",
          "dailyInterestRate": "0.00012333",
          "limit": "0",
          "annuallyInterestRate": "0.04501545",
          "discountRate": "1"
        }
      ]
    }
  ]
}
```

## Get Isolated Tier Configuration

`GET /api/v2/margin/isolated/tier-data`

Frequency limit:10 times/1s (UID)

This interface will determine the user's VIP level based on the User ID sending the request, and then return the tier information based on the VIP level.

Operation ID: `classicMarginIsolatedAccountIsolatedTierData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tier | string |  | Tier |
| data[].symbol | string |  | Trading pair |
| data[].leverage | string |  | Effective leverage, global default: 10x |
| data[].baseCoin | string |  | Base currency |
| data[].quoteCoin | string |  | Quote currency |
| data[].baseMaxBorrowableAmount | string |  | Maximum borrow in base currency |
| data[].quoteMaxBorrowableAmount | string |  | Maximum borrow in quote currency |
| data[].maintainMarginRate | string |  | Maintenance margin rate |
| data[].initRate | string |  | Initial margin rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694583297872,
  "data": [
    {
      "tier": "1",
      "symbol": "BTCUSDT",
      "leverage": "5",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "baseMaxBorrowableAmount": "0",
      "quoteMaxBorrowableAmount": "0",
      "maintainMarginRate": "0.1",
      "initRate": "0.25"
    }
  ]
}
```

## Get Isolated Max Borrowable

`GET /api/v2/margin/isolated/account/max-borrowable-amount`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.baseCoin | string |  | Left coin |
| data.baseCoinMaxBorrowAmount | string |  | Maximum borrow amount of left coins (amount changes in real time) |
| data.quoteCoin | string |  | Right coin |
| data.quoteCoinMaxBorrowAmount | string |  | Maximum borrow amount of right coins |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "symbol": "ETHUSDT",
    "baseCoin": "ETH",
    "baseCoinMaxBorrowAmount": "10.1401916",
    "quoteCoin": "USDT",
    "quoteCoinMaxBorrowAmount": "3976070.21616"
  }
}
```

## Get Isolated Max Transferable

`GET /api/v2/margin/isolated/account/max-transfer-out-amount`

Frequency limit: 10 times/1s (UID)

Get Isolated Max Transferable Amount

Operation ID: `classicMarginIsolatedAccountGetIsolatedMaxTransferOutAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.baseCoin | string |  | Base coin |
| data.symbol | string |  | Trading pair |
| data.baseCoinMaxTransferOutAmount | string |  | Maximum transferable amount for base coin |
| data.quoteCoin | string |  | Quote coin |
| data.quoteCoinMaxTransferOutAmount | string |  | Maximum transferable amount for quote coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695618856403,
  "data": {
    "baseCoin": "BTC",
    "symbol": "BTCUSDT",
    "baseCoinMaxTransferOutAmount": "199999",
    "quoteCoin": "USDT",
    "quoteCoinMaxTransferOutAmount": "1000000"
  }
}
```

## Isolated Flash Repay

`POST /api/v2/margin/isolated/account/flash-repay`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedFlashRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] |  | Trading pair array under isolated mode<br><br>If it is not filled, all trading pair will be confirmed by default.<br><br>Up to 100 trading pairs in one request |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | Repayment id |
| data[].symbol | string |  | Spot margin trading pairs |
| data[].result | string |  | success Repayment request successful<br><br>failure Failure to repay |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695619576187,
  "data": [
    {
      "repayId": "3423423",
      "symbol": "ETHUSDT",
      "result": "success"
    }
  ]
}
```

## Query Isolated Flash Repayment Result

`POST /api/v2/margin/isolated/account/query-flash-repay-status`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedAccountQueryIsolatedFlashRepayStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| idList | string[] | 是 | Repayment ID list under isolated mode<br><br>Up to 100 trading pairs in one request |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | Repayment ID |
| data[].status | string |  | Repayment result status |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "repayId": "13423423",
      "status": "FINISH"
    }
  ]
}
```


---

经典账户 — 逐仓杠杆借币还币与资产。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/isolated/account/assets` — 获取逐仓杠杆账户资产
- `POST /api/v2/margin/isolated/account/borrow` — 逐仓借款
- `POST /api/v2/margin/isolated/account/repay` — 逐仓还款
- `GET /api/v2/margin/isolated/account/risk-rate` — 逐仓风险率
- `GET /api/v2/margin/isolated/interest-rate-and-limit` — 逐仓利率与最大可借数量配置
- `GET /api/v2/margin/isolated/tier-data` — 逐仓档位梯度配置
- `GET /api/v2/margin/isolated/account/max-borrowable-amount` — 逐仓最大可借数量
- `GET /api/v2/margin/isolated/account/max-transfer-out-amount` — 逐仓最大可转出数量
- `POST /api/v2/margin/isolated/account/flash-repay` — 逐仓一键还款
- `POST /api/v2/margin/isolated/account/query-flash-repay-status` — 获取逐仓还款结果

## 获取逐仓杠杆账户资产

`GET /api/v2/margin/isolated/account/assets`

限速规则 10次/1s (UID)

获取账户资产

Operation ID: `classicMarginIsolatedAccountGetIsolatedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对，如BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].symbol | string |  | 交易对名称 |
| data[].totalAmount | string |  | 总金额 |
| data[].available | string |  | 可用金额 |
| data[].frozen | string |  | 冻结资产 |
| data[].borrow | string |  | 借款 |
| data[].interest | string |  | 利息，还款时先息后本，最小还款为利息 |
| data[].net | string |  | 净资产 = available + frozen - borrow - interest, 风险率达到1就爆仓 |
| data[].coupon | string |  | 体验金 |
| data[].cTime | string |  | 创建时间 |
| data[].uTime | string |  | 更新时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694588056713,
  "data": [
    {
      "symbol": "BTCUSDT",
      "coin": "BTC",
      "totalAmount": "19876.1798394",
      "available": "19876.1798394",
      "frozen": "0",
      "borrow": "0",
      "interest": "0",
      "net": "19876.1798394",
      "coupon": "0",
      "cTime": "1692085312298",
      "uTime": "1694569802151"
    }
  ]
}
```

## 逐仓借款

`POST /api/v2/margin/isolated/account/borrow`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 借出交易对，如BTCUSDT |
| coin | string | 是 | 借出币种，如BTC |
| borrowAmount | string | 是 | 借出数量（最长为8位小数） |
| clientOid | string |  | 客户自定义订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanId | string |  | 借款ID |
| data.coin | string |  | 借出币种 |
| data.borrowAmount | string |  | 借出数量 |
| data.symbol | string |  | 借出交易对 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": {
    "loanId": "123412412452345",
    "symbol": "BTCUSDT",
    "coin": "USDT",
    "borrowAmount": "1.00000000"
  }
}
```

## 逐仓还款

`POST /api/v2/margin/isolated/account/repay`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayAmount | string | 是 | 还款数量，最长为8位小数 |
| coin | string | 是 | 还款币种 |
| symbol | string | 是 | 还款交易对，如BTCUSDT |
| clientOid | string |  | 客户自定义订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.remainDebtAmount | string |  | 剩余欠款 |
| data.repayId | string |  | 客户端唯一标识 （暂时不支持） |
| data.symbol | string |  | 交易对 |
| data.coin | string |  | 币种 |
| data.repayAmount | string |  | 还款金额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694588859956,
  "data": {
    "remainDebtAmount": "0",
    "symbol": "BTCUSDT",
    "repayId": "1234234234234",
    "coin": "USDT",
    "repayAmount": "1"
  }
}
```

## 逐仓风险率

`GET /api/v2/margin/isolated/account/risk-rate`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedRiskRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对，如BTCUSDT |
| pageNum | query | string |  | 页码，默认1 |
| pageSize | query | string |  | 每页大小，默认100，最大500 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对 |
| data[].riskRateRatio | string |  | 风险率 （逐仓总资产/逐仓总负债） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694590583906,
  "data": [
    {
      "symbol": "BTCUSDT",
      "riskRateRatio": "0"
    }
  ]
}
```

## 逐仓利率与最大可借数量配置

`GET /api/v2/margin/isolated/interest-rate-and-limit`

限速规则 10次/1s (UID)

该接口需要根据请求的UID判断用户VIP等级，再根据VIP等级返回利率、限额等信息

Operation ID: `classicMarginIsolatedAccountIsolatedMarginInterestRateAndMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对 |
| data[].baseCoin | string |  | 基础币币种 |
| data[].leverage | string |  | 杠杆倍数，默认 10 |
| data[].baseTransferable | boolean |  | 基础币是否可转入<br><br>true 可转入<br><br>false 不可转入 |
| data[].baseBorrowable | boolean |  | 基础币是否可借<br><br>true 可借<br><br>false 不可借 |
| data[].baseDailyInterestRate | string |  | 基础币非VIP的日利率 |
| data[].baseAnnuallyInterestRate | string |  | 基础币非VIP的年利率 |
| data[].baseMaxBorrowableAmount | string |  | 基础币最大可借 |
| data[].baseVipList | object[] |  | 基础币vip |
| data[].baseVipList[].level | string |  | VIP 等级 |
| data[].baseVipList[].limit | string |  | VIP 限额 |
| data[].baseVipList[].dailyInterestRate | string |  | VIP 日利率 |
| data[].baseVipList[].annuallyInterestRate | string |  | VIP 年利率 |
| data[].baseVipList[].discountRate | string |  | VIP 折扣，1代表100%，即无折扣；0.97代表折后利率为原利率的97% |
| data[].quoteCoin | string |  | 计价币币种 |
| data[].quoteTransferable | boolean |  | 计价币是否可转入 |
| data[].quoteBorrowable | boolean |  | 计价币是否可借 |
| data[].quoteDailyInterestRate | string |  | 计价币非VIP日利率 |
| data[].quoteAnnuallyInterestRate | string |  | 计价币非VIP年利率 |
| data[].quoteMaxBorrowableAmount | string |  | 计价币非VIP最大可借 |
| data[].quoteList | object[] |  | 计价币vip |
| data[].quoteList[].level | string |  | VIP 等级 |
| data[].quoteList[].limit | string |  | VIP 限额 |
| data[].quoteList[].dailyInterestRate | string |  | VIP 日利率 |
| data[].quoteList[].annuallyInterestRate | string |  | VIP 年利率 |
| data[].quoteList[].discountRate | string |  | VIP 折扣，1代表100%，即无折扣；0.97代表折后利率为原利率的97% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694579779768,
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "5",
      "baseCoin": "BTC",
      "baseTransferable": true,
      "baseBorrowable": true,
      "baseDailyInterestRate": "0.00007113",
      "baseAnnuallyInterestRate": "0.02596245",
      "baseMaxBorrowableAmount": "0",
      "baseVipList": [
        {
          "level": "0",
          "dailyInterestRate": "0.00007333",
          "limit": "0",
          "annuallyInterestRate": "0.02676545",
          "discountRate": "1"
        }
      ],
      "quoteCoin": "USDT",
      "quoteTransferable": true,
      "quoteBorrowable": true,
      "quoteDailyInterestRate": "0.00011963",
      "quoteAnnuallyInterestRate": "0.04366495",
      "quoteMaxBorrowableAmount": "0",
      "quoteList": [
        {
          "level": "0",
          "dailyInterestRate": "0.00012333",
          "limit": "0",
          "annuallyInterestRate": "0.04501545",
          "discountRate": "1"
        }
      ]
    }
  ]
}
```

## 逐仓档位梯度配置

`GET /api/v2/margin/isolated/tier-data`

限速规则 10次/1s (UID)

该接口需要根据请求的UID判断用户VIP等级，再根据VIP等级返回档位梯度信息

Operation ID: `classicMarginIsolatedAccountIsolatedTierData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tier | string |  | 档位 |
| data[].symbol | string |  | 交易对 |
| data[].leverage | string |  | 有效杠杆倍数，全局默认10倍 |
| data[].baseCoin | string |  | 基础币币种 |
| data[].quoteCoin | string |  | 计价币币种 |
| data[].baseMaxBorrowableAmount | string |  | 基础币最大可借 |
| data[].quoteMaxBorrowableAmount | string |  | 计价币最大可借 |
| data[].maintainMarginRate | string |  | 维持保证金率 |
| data[].initRate | string |  | 初始保证金率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694583297872,
  "data": [
    {
      "tier": "1",
      "symbol": "BTCUSDT",
      "leverage": "5",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "baseMaxBorrowableAmount": "0",
      "quoteMaxBorrowableAmount": "0",
      "maintainMarginRate": "0.1",
      "initRate": "0.25"
    }
  ]
}
```

## 逐仓最大可借数量

`GET /api/v2/margin/isolated/account/max-borrowable-amount`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，如BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对 |
| data.baseCoin | string |  | 左币 |
| data.baseCoinMaxBorrowAmount | string |  | 左币最大可借数量 （数值会实时变化） |
| data.quoteCoin | string |  | 右币 |
| data.quoteCoinMaxBorrowAmount | string |  | 右币最大可借数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "symbol": "ETHUSDT",
    "baseCoin": "ETH",
    "baseCoinMaxBorrowAmount": "10.1401916",
    "quoteCoin": "USDT",
    "quoteCoinMaxBorrowAmount": "3976070.21616"
  }
}
```

## 逐仓最大可转出数量

`GET /api/v2/margin/isolated/account/max-transfer-out-amount`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountGetIsolatedMaxTransferOutAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，例如：BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.baseCoin | string |  | 基础币币种 |
| data.symbol | string |  | 交易对 |
| data.baseCoinMaxTransferOutAmount | string |  | 最大基础币可转出数量 |
| data.quoteCoin | string |  | 计价币币种 |
| data.quoteCoinMaxTransferOutAmount | string |  | 最大计价币可转出数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695618856403,
  "data": {
    "baseCoin": "BTC",
    "symbol": "BTCUSDT",
    "baseCoinMaxTransferOutAmount": "199999",
    "quoteCoin": "USDT",
    "quoteCoinMaxTransferOutAmount": "1000000"
  }
}
```

## 逐仓一键还款

`POST /api/v2/margin/isolated/account/flash-repay`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountIsolatedFlashRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] |  | 逐仓交易对数组<br><br>如不传，则默认全部交易对<br><br>一次请求最多传100个交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | 还款id |
| data[].symbol | string |  | 杠杆交易对 |
| data[].result | string |  | success 还款请求成功<br><br>failure 还款失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695619576187,
  "data": [
    {
      "repayId": "3423423",
      "symbol": "ETHUSDT",
      "result": "success"
    }
  ]
}
```

## 获取逐仓还款结果

`POST /api/v2/margin/isolated/account/query-flash-repay-status`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedAccountQueryIsolatedFlashRepayStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| idList | string[] | 是 | 逐仓还款ID列表<br><br>单次查询最多支持100条 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | 还款ID |
| data[].status | string |  | 还款结果状态 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "repayId": "13423423",
      "status": "FINISH"
    }
  ]
}
```