---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn-classic-loan
api_type: REST
updated_at: 2026-11-22 19:01:16.183947
---

# Classic Earn Loan

Classic account C2C loan, borrow, repay, pledge, and liquidation record APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/loan/public/coinInfos` — Get Currency List
- `GET /api/v2/earn/loan/public/hour-interest` — Get Est. Interest and Borrowable
- `POST /api/v2/earn/loan/borrow` — Borrow
- `GET /api/v2/earn/loan/ongoing-orders` — Get Loan Orders
- `POST /api/v2/earn/loan/repay` — Repay
- `GET /api/v2/earn/loan/repay-history` — Get Repay History
- `POST /api/v2/earn/loan/revise-pledge` — Modify Pledge Rate
- `GET /api/v2/earn/loan/revise-history` — Get Pledge Rate History
- `GET /api/v2/earn/loan/borrow-history` — Get Loan History
- `GET /api/v2/earn/loan/debts` — Get Debts
- `GET /api/v2/earn/loan/reduces` — Get Liquidation Records

## Get Currency List

`GET /api/v2/earn/loan/public/coinInfos`

Rate limit: 10/sec/IP

Get loan-able currency list.

Operation ID: `classicEarnLoanGetCoinInfos`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin, `BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | object[] |  | Loan infos |
| data.loanInfos[].coin | string |  | Loan coin |
| data.loanInfos[].hourRate7D | string |  | 7 days fixed rate per hour percentage |
| data.loanInfos[].rate7D | string |  | 7-day fixed rate annualized percentage |
| data.loanInfos[].hourRate30D | string |  | 30-day fixed rate hourly percentage |
| data.loanInfos[].rate30D | string |  | 30-day fixed rate annualized percentage |
| data.loanInfos[].minUsdt | string |  | Minimum Borrowable limit usdt |
| data.loanInfos[].maxUsdt | string |  | Maximum borrowing limit usdt |
| data.loanInfos[].min | string |  | Minimum borrowing limit |
| data.loanInfos[].max | string |  | Maximum borrowing limit |
| data.pledgeInfos | object[] |  | Pledge infos |
| data.pledgeInfos[].coin | string |  | Pledge coin |
| data.pledgeInfos[].initRate | string |  | Initial pledge rate percentage |
| data.pledgeInfos[].supRate | string |  | Percentage of supplementary guarantee pledge rate |
| data.pledgeInfos[].forceRate | string |  | Forced Liquidation Pledge Rate Percentage |
| data.pledgeInfos[].minUsdt | string |  | Minimum pledge limit usdt |
| data.pledgeInfos[].maxUsdt | string |  | Maximum pledge limit usdt |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433281223,
  "data": {
    "loanInfos": [
      {
        "coin": "USDT",
        "hourRate7D": "0.00000617",
        "rate7D": "0.054",
        "hourRate30D": "0.00000879",
        "rate30D": "0.077",
        "minUsdt": "200",
        "maxUsdt": "1000000",
        "min": "200",
        "max": "1000000"
      }
    ],
    "pledgeInfos": [
      {
        "coin": "MATIC",
        "initRate": "0.6",
        "supRate": "0.75",
        "forceRate": "0.83",
        "minUsdt": "0",
        "maxUsdt": "200000"
      }
    ]
  }
}
```

## Get Est. Interest and Borrowable

`GET /api/v2/earn/loan/public/hour-interest`

Rate limit: 10/sec/IP

Get estimated hourly interest rate and borrowable amount.

Operation ID: `classicEarnLoanGetHourInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanCoin | query | string | 是 | Coin to loan, `BTC` |
| pledgeCoin | query | string | 是 | Collateral coin, `ETH` |
| daily | query | string | 是 | Mortgage term<br><br>`SEVEN` 7 days<br><br>`THIRTY` 30 days<br><br>`FLEXIBLE` Flexible |
| pledgeAmount | query | string | 是 | Pledge amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hourInterest | string |  | Estimated interest amount per hour |
| data.loanAmount | string |  | Borrowable amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433739845,
  "data": {
    "hourInterest": "0.00133436",
    "loanAmount": "216.2654"
  }
}
```

## Borrow

`POST /api/v2/earn/loan/borrow`

Rate limit: 10/sec/UID

Borrow coin by pledging collateral and paying interest.

Operation ID: `classicEarnLoanBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | Coin to loan, `ETH` |
| pledgeCoin | string | 是 | Pledge coin (Collateral), `USDT` |
| daily | string | 是 | Mortgage term<br><br>`SEVEN` 7 days<br><br>`THIRTY` 30 days<br><br>`FLEXIBLE` Flexible |
| pledgeAmount | string |  | Pledge (Collateral) amount, `pledgeAmount` and `loanAmount` must send one |
| loanAmount | string |  | Loan amount, `pledgeAmount` and `loanAmount` must send one |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": {
    "orderId": "1"
  }
}
```

## Get Loan Orders

`GET /api/v2/earn/loan/ongoing-orders`

Rate limit: 10/sec/UID

Get on-going loan orders.

Operation ID: `classicEarnLoanGetOngoingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Coin to loan |
| pledgeCoin | query | string |  | Pledge (Collateral) coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | Coin to loan |
| data[].loanAmount | string |  | Loan amount |
| data[].interestAmount | string |  | Interest amount |
| data[].hourInterestRate | string |  | Hour interest rate |
| data[].pledgeCoin | string |  | Pledge (Collateral) coin |
| data[].pledgeAmount | string |  | Pledge (Collateral) amount |
| data[].pledgeRate | string |  | Pledge (Collateral) rate |
| data[].supRate | string |  | Supplementary rate |
| data[].forceRate | string |  | Forced Liquidation Pledge Rate Percentage |
| data[].borrowTime | string |  | Borrow time millseconds |
| data[].expireTime | string |  | Expire time millseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692434611622,
  "data": [
    {
      "orderId": "1",
      "loanCoin": "ETH",
      "loanAmount": "1",
      "interestAmount": "0.00000229",
      "hourInterestRate": "0.000229",
      "pledgeCoin": "USDT",
      "pledgeAmount": "2619.69231032",
      "pledgeRate": "65",
      "supRate": "75",
      "forceRate": "83",
      "borrowTime": "1692434472156",
      "expireTime": "1693036799999"
    }
  ]
}
```

## Repay

`POST /api/v2/earn/loan/repay`

Rate limit: 10/sec/UID

Repay.

Operation ID: `classicEarnLoanRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |
| amount | string |  | When `repayAll`=`no`: Repay amount |
| repayUnlock | string |  | Whether redeem after repay, default: `yes`<br><br>`yes`<br><br>`no` |
| repayAll | string | 是 | Repay all<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | Coin to loan |
| data.pledgeCoin | string |  | Pledge (Collateral) coin |
| data.repayAmount | string |  | Repay amount |
| data.payInterest | string |  | Paid interest |
| data.repayLoanAmount | string |  | Repay loan amount |
| data.repayUnlockAmount | string |  | Pledge (Collateral) redeemed amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "repayAmount": "1566.23820848",
    "payInterest": "0.1185634",
    "repayLoanAmount": "1566.22635214",
    "repayUnlockAmount": "195"
  }
}
```

## Get Repay History

`GET /api/v2/earn/loan/repay-history`

Rate limit: 10/sec/UID

Get the list of repay history.

Operation ID: `classicEarnLoanGetRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Loan coin |
| pledgeCoin | query | string |  | Pledge (Collateral) coin |
| startTime | query | string | 是 | Start time, ms, only supports querying the data of the past three months |
| endTime | query | string | 是 | End time, ms |
| pageNo | query | string |  | Page No default 1 |
| pageSize | query | string |  | Page size default 10, max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | Coin to loan |
| data[].pledgeCoin | string |  | Pledge (Collateral) coin |
| data[].repayAmount | string |  | Repay amount |
| data[].payInterest | string |  | Paid interest |
| data[].repayLoanAmount | string |  | Loan Currency Repayment of Principal Amount |
| data[].repayUnlockAmount | string |  | Pledge (Collateral) release amount |
| data[].repayTime | string |  | Repayment time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "repayAmount": "1566.23820848",
      "payInterest": "0.1185634",
      "repayLoanAmount": "1566.22635214",
      "repayUnlockAmount": "195",
      "repayTime": "1684747525424"
    }
  ]
}
```

## Modify Pledge Rate

`POST /api/v2/earn/loan/revise-pledge`

Rate limit: 10/sec/UID

Withdraw or supplement collateral.

Operation ID: `classicEarnLoanRevisePledge`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |
| amount | string | 是 | Amount to withdraw or supplement |
| pledgeCoin | string | 是 | Pledge (Collateral) coin |
| reviseType | string | 是 | Repay Type<br><br>`OUT` Withdraw collateral<br><br>`IN` supplement collateral |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | Loan coin |
| data.pledgeCoin | string |  | Pledge (Collateral) coin |
| data.afterPledgeRate | string |  | Pledge Rate Percentage after adjusted |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "afterPledgeRate": "60.5"
  }
}
```

## Get Pledge Rate History

`GET /api/v2/earn/loan/revise-history`

Rate limit: 10/sec/UID

Get pledge rate history.

Operation ID: `classicEarnLoanGetReviseHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| reviseSide | query | string |  | Revise side<br><br>`down` supplement collateral to turn down<br><br>`up` withdraw collateral to turn up |
| pledgeCoin | query | string |  | Pledge (Collateral) coin |
| startTime | query | string | 是 | Start time, ms, only supports querying the data of the past three months |
| endTime | query | string | 是 | End time, ms |
| pageNo | query | string |  | pageNo default 1 |
| pageSize | query | string |  | pageSize default 10, max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanCoin | string |  | Loan coin |
| data[].pledgeCoin | string |  | Pledge (Collateral) coin |
| data[].orderId | string |  | Order ID |
| data[].reviseTime | string |  | Adjust time |
| data[].reviseSide | string |  | Revise side<br><br>`down` supplement collateral to turn down<br><br>`up` withdraw collateral to turn up |
| data[].reviseAmount | string |  | Adjustment quantity |
| data[].afterPledgeRate | string |  | Pledge Rate Percentage after adjustment |
| data[].beforePledgeRate | string |  | Pledge rate percentage before adjustment |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436125845,
  "data": [
    {
      "loanCoin": "ETH",
      "pledgeCoin": "USDT",
      "orderId": "1",
      "reviseTime": "1692436102448",
      "reviseSide": "down",
      "reviseAmount": "10",
      "afterPledgeRate": "64.75",
      "beforePledgeRate": "65"
    }
  ]
}
```

## Get Loan History

`GET /api/v2/earn/loan/borrow-history`

Rate limit: 10/sec/UID

Get the list of loan history.

Operation ID: `classicEarnLoanGetBorrowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Loan coin |
| pledgeCoin | query | string |  | Pledge (Collateral) coin |
| status | query | string |  | Status<br><br>`ROLLBACK` failure<br><br>`FORCE` force liquidation<br><br>`REPAY` already repaid |
| startTime | query | string | 是 | Start time, ms, only supports querying the data of the past three months |
| endTime | query | string | 是 | End time, ms |
| pageNo | query | string |  | Page No default 1 |
| pageSize | query | string |  | Page size default 10, max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanCoin | string |  | Loan coin |
| data[].pledgeCoin | string |  | Pledge (Collateral) coin |
| data[].orderId | string |  | Order ID |
| data[].initPledgeAmount | string |  | Initial pledge amount |
| data[].initLoanAmount | string |  | Initial loan amount |
| data[].hourRate | string |  | hourly rate percentage |
| data[].daily | string |  | Pledge days |
| data[].borrowTime | string |  | Borrowed time |
| data[].status | string |  | Status<br><br>`ROLLBACK` failure<br><br>`FORCE` force liquidation<br><br>`REPAY` already repaid |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "initPledgeAmount": "0.757",
      "initLoanAmount": "4321321.23820848",
      "hourRate": "59.1",
      "daily": "7",
      "borrowTime": "1684747528424",
      "status": "REPAY"
    }
  ]
}
```

## Get Debts

`GET /api/v2/earn/loan/debts`

Rate limit: 10/sec/UID

Get the list of repay history.

Operation ID: `classicEarnLoanGetDebts`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | object[] |  | Loan info |
| data.loanInfos[].coin | string |  | Coin |
| data.loanInfos[].amount | string |  | Amount |
| data.loanInfos[].amountUsdt | string |  | Amount usdt |
| data.pledgeInfos | object[] |  | Pledge Info |
| data.pledgeInfos[].coin | string |  | Coin |
| data.pledgeInfos[].amount | string |  | Amount |
| data.pledgeInfos[].amountUsdt | string |  | Amount usdt |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436610750,
  "data": {
    "pledgeInfos": [
      {
        "coin": "USDT",
        "amount": "28826.61539642",
        "amountUsdt": "28826.61"
      }
    ],
    "loanInfos": [
      {
        "coin": "ETH",
        "amount": "11.00002748",
        "amountUsdt": "18730.85"
      }
    ]
  }
}
```

## Get Liquidation Records

`GET /api/v2/earn/loan/reduces`

Rate limit: 10/sec/UID

Get the list of liquidation records.

Operation ID: `classicEarnLoanGetReduces`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Loan coin |
| pledgeCoin | query | string |  | Pledge (Collateral) coin |
| status | query | string |  | Status<br><br>`COMPLETE` completed liquidation<br><br>`WAIT` liquidating |
| startTime | query | string | 是 | Start time, ms, only supports querying the data of the past three months |
| endTime | query | string | 是 | End time, ms |
| pageNo | query | string |  | Page No, default 1 |
| pageSize | query | string |  | Page size, default 10, max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | Loan coin |
| data[].pledgeCoin | string |  | Pledge (Collateral) coin |
| data[].reduceTime | string |  | Liquidated time |
| data[].pledgeRate | string |  | Pledge percentage during liquidation |
| data[].pledgePrice | string |  | Pledge price when Liquidated |
| data[].status | string |  | Status<br><br>`COMPLETE` liquidation completed<br><br>`WAIT` liquidating |
| data[].pledgeAmount | string |  | Liquidation amount of pledged coin |
| data[].reduceFee | string |  | Liquidation fee |
| data[].residueAmount | string |  | Remaining pledged amount |
| data[].runlockAmount | string |  | Released amount of pledged coin |
| data[].repayLoanAmount | string |  | Repayment amount of the loan |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "reduceTime": "0.757",
      "pledgeRate": "98.2",
      "pledgePrice": "111.4",
      "status": "COMPLETE",
      "pledgeAmount": "1213.5",
      "reduceFee": "REPAY",
      "residueAmount": "3234.2",
      "runlockAmount": "23",
      "repayLoanAmount": "53.2"
    }
  ]
}
```


---

经典账户 C2C 借贷、借币、还款、质押及强平记录接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/loan/public/coinInfos` — 查询支持质押币种
- `GET /api/v2/earn/loan/public/hour-interest` — 预估利息及可借数量
- `POST /api/v2/earn/loan/borrow` — 借币
- `GET /api/v2/earn/loan/ongoing-orders` — 查询借款中列表
- `POST /api/v2/earn/loan/repay` — 还款
- `GET /api/v2/earn/loan/repay-history` — 查询还款历史
- `POST /api/v2/earn/loan/revise-pledge` — 调整质押率
- `GET /api/v2/earn/loan/revise-history` — 查询调整质押率历史
- `GET /api/v2/earn/loan/borrow-history` — 查询借币历史
- `GET /api/v2/earn/loan/debts` — 查询资产负债
- `GET /api/v2/earn/loan/reduces` — 查询强平记录

## 查询支持质押币种

`GET /api/v2/earn/loan/public/coinInfos`

限频规则: 10次/秒/IP

查询支持质押的币种数据列表。

Operation ID: `classicEarnLoanGetCoinInfos`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种, `BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | object[] |  | 可借币种列表 |
| data.loanInfos[].coin | string |  | 已借币种 |
| data.loanInfos[].hourRate7D | string |  | 7天固定利率每小时百分比 |
| data.loanInfos[].rate7D | string |  | 7天固定利率年化百分比 |
| data.loanInfos[].hourRate30D | string |  | 30天固定利率每小时百分比 |
| data.loanInfos[].rate30D | string |  | 30天固定利率年化百分比 |
| data.loanInfos[].minUsdt | string |  | 最小可借限额 usdt |
| data.loanInfos[].maxUsdt | string |  | 最大可借限额 usdt |
| data.loanInfos[].min | string |  | 最小可借数量 |
| data.loanInfos[].max | string |  | 最大可借数量 |
| data.pledgeInfos | object[] |  | 可抵押币种列表 |
| data.pledgeInfos[].coin | string |  | 抵押币种 |
| data.pledgeInfos[].initRate | string |  | 初始质押率百分比 |
| data.pledgeInfos[].supRate | string |  | 补保质押率百分比 |
| data.pledgeInfos[].forceRate | string |  | 强平质押率百分比 |
| data.pledgeInfos[].minUsdt | string |  | 最小质押限额 usdt |
| data.pledgeInfos[].maxUsdt | string |  | 最大质押限额 usdt |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433281223,
  "data": {
    "loanInfos": [
      {
        "coin": "USDT",
        "hourRate7D": "0.00000617",
        "rate7D": "0.054",
        "hourRate30D": "0.00000879",
        "rate30D": "0.077",
        "minUsdt": "200",
        "maxUsdt": "1000000",
        "min": "200",
        "max": "1000000"
      }
    ],
    "pledgeInfos": [
      {
        "coin": "MATIC",
        "initRate": "0.6",
        "supRate": "0.75",
        "forceRate": "0.83",
        "minUsdt": "0",
        "maxUsdt": "200000"
      }
    ]
  }
}
```

## 预估利息及可借数量

`GET /api/v2/earn/loan/public/hour-interest`

限频规则: 10次/秒/IP

查询每小时预估利息及可借数量。

Operation ID: `classicEarnLoanGetHourInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanCoin | query | string | 是 | 需借币种, `BTC` |
| pledgeCoin | query | string | 是 | 质押币种, `ETH` |
| daily | query | string | 是 | 质押天数<br><br>`SEVEN` 7天<br><br>`THIRTY` 30天<br><br>`FLEXIBLE` 活期 |
| pledgeAmount | query | string | 是 | 质押数量 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hourInterest | string |  | 每小时预估利息数量 |
| data.loanAmount | string |  | 可借数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433739845,
  "data": {
    "hourInterest": "0.00133436",
    "loanAmount": "216.2654"
  }
}
```

## 借币

`POST /api/v2/earn/loan/borrow`

限频规则: 10次/秒/UID

通过质押并付出利息，借币。

Operation ID: `classicEarnLoanBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | 需借币种, `ETH` |
| pledgeCoin | string | 是 | 质押币种, `USDT` |
| daily | string | 是 | 质押天数<br><br>`SEVEN` 7天<br><br>`THIRTY` 30天<br><br>`FLEXIBLE` 活期 |
| pledgeAmount | string |  | 质押数量，与`loanAmount`二选一 |
| loanAmount | string |  | 借币数量，与`pledgeAmount`二选一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": {
    "orderId": "1"
  }
}
```

## 查询借款中列表

`GET /api/v2/earn/loan/ongoing-orders`

限频规则: 10次/秒/UID

查询借款中列表。

Operation ID: `classicEarnLoanGetOngoingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 需借币种 |
| pledgeCoin | query | string |  | 质押币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].loanCoin | string |  | 需借币种 |
| data[].loanAmount | string |  | 借币数量 |
| data[].interestAmount | string |  | 已产生利息数量 |
| data[].hourInterestRate | string |  | 小时利率百分比 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].pledgeAmount | string |  | 质押数量 |
| data[].pledgeRate | string |  | 质押率百分比 |
| data[].supRate | string |  | 补保质押率百分比 |
| data[].forceRate | string |  | 强平质押率百分比 |
| data[].borrowTime | string |  | 借币时间 毫秒时间戳 |
| data[].expireTime | string |  | 到期时间 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692434611622,
  "data": [
    {
      "orderId": "1",
      "loanCoin": "ETH",
      "loanAmount": "1",
      "interestAmount": "0.00000229",
      "hourInterestRate": "0.000229",
      "pledgeCoin": "USDT",
      "pledgeAmount": "2619.69231032",
      "pledgeRate": "65",
      "supRate": "75",
      "forceRate": "83",
      "borrowTime": "1692434472156",
      "expireTime": "1693036799999"
    }
  ]
}
```

## 还款

`POST /api/v2/earn/loan/repay`

限频规则: 10次/秒/UID

还款。

Operation ID: `classicEarnLoanRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单ID |
| amount | string |  | 还款数量 |
| repayUnlock | string |  | 是否赎回<br><br>默认`yes`<br><br>`yes`<br><br>`no` |
| repayAll | string | 是 | 是否全部还款<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | 需借币种 |
| data.pledgeCoin | string |  | 质押币种 |
| data.repayAmount | string |  | 还款数量 |
| data.payInterest | string |  | 借币币种支付利息数量 |
| data.repayLoanAmount | string |  | 借币币种归还本金数量 |
| data.repayUnlockAmount | string |  | 赎回数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "repayAmount": "1566.23820848",
    "payInterest": "0.1185634",
    "repayLoanAmount": "1566.22635214",
    "repayUnlockAmount": "195"
  }
}
```

## 查询还款历史

`GET /api/v2/earn/loan/repay-history`

限频规则: 10次/秒/UID

查询还款历史列表。

Operation ID: `classicEarnLoanGetRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 借贷币种 |
| pledgeCoin | query | string |  | 质押币种 |
| startTime | query | string | 是 | 开始时间，仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNo | query | string |  | pageNo 默认值1 |
| pageSize | query | string |  | pageSize 默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].loanCoin | string |  | 需借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].repayAmount | string |  | 还款数量 |
| data[].payInterest | string |  | 借币币种支付利息数量 |
| data[].repayLoanAmount | string |  | 借币币种归还本金数量 |
| data[].repayUnlockAmount | string |  | 赎回数量 |
| data[].repayTime | string |  | 还款时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "repayAmount": "1566.23820848",
      "payInterest": "0.1185634",
      "repayLoanAmount": "1566.22635214",
      "repayUnlockAmount": "195",
      "repayTime": "1684747525424"
    }
  ]
}
```

## 调整质押率

`POST /api/v2/earn/loan/revise-pledge`

限频规则: 10次/秒/UID

调整质押率。

Operation ID: `classicEarnLoanRevisePledge`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单ID |
| amount | string | 是 | 调整数量 |
| pledgeCoin | string | 是 | 质押币种 |
| reviseType | string | 是 | 调整类型<br><br>`OUT` 提取质押品<br><br>`IN` 补充质押品 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | 已借币种 |
| data.pledgeCoin | string |  | 质押币种 |
| data.afterPledgeRate | string |  | 调整后质押利率百分比 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "afterPledgeRate": "60.5"
  }
}
```

## 查询调整质押率历史

`GET /api/v2/earn/loan/revise-history`

限频规则: 10次/秒/UID

查询调整质押率历史列表。

Operation ID: `classicEarnLoanGetReviseHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| reviseSide | query | string |  | 调整方向<br><br>`down` 转入调低<br><br>`up` 转出调高 |
| pledgeCoin | query | string |  | 质押币种 |
| startTime | query | string | 是 | 开始时间，仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNo | query | string |  | pageNo 默认值1 |
| pageSize | query | string |  | pageSize 默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanCoin | string |  | 已借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].orderId | string |  | 订单ID |
| data[].reviseTime | string |  | 调整时间 |
| data[].reviseSide | string |  | 调整方向<br><br>`down` 转入调低<br><br>`up` 转出调高 |
| data[].reviseAmount | string |  | 调整数量 |
| data[].afterPledgeRate | string |  | 调整后质押利率百分比 |
| data[].beforePledgeRate | string |  | 调整前质押利率百分比 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436125845,
  "data": [
    {
      "loanCoin": "ETH",
      "pledgeCoin": "USDT",
      "orderId": "1",
      "reviseTime": "1692436102448",
      "reviseSide": "down",
      "reviseAmount": "10",
      "afterPledgeRate": "64.75",
      "beforePledgeRate": "65"
    }
  ]
}
```

## 查询借币历史

`GET /api/v2/earn/loan/borrow-history`

限频规则: 10次/秒/UID

查询借币历史列表。

Operation ID: `classicEarnLoanGetBorrowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 借贷币种 |
| pledgeCoin | query | string |  | 质押币种 |
| status | query | string |  | 状态<br><br>`ROLLBACK` 失败<br><br>`FORCE` 强平<br><br>`REPAY` 已还款 |
| startTime | query | string | 是 | 开始时间，仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNo | query | string |  | pageNo 默认值1 |
| pageSize | query | string |  | pageSize 默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanCoin | string |  | 已借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].orderId | string |  | 订单ID |
| data[].initPledgeAmount | string |  | 初始化质押数量 |
| data[].initLoanAmount | string |  | 初始化借币数量 |
| data[].hourRate | string |  | 每小时利率百分比 |
| data[].daily | string |  | 质押借贷天数 |
| data[].borrowTime | string |  | 借币时间 |
| data[].status | string |  | 状态<br><br>`ROLLBACK` 失败<br><br>`FORCE` 强平<br><br>`REPAY` 已还款 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "initPledgeAmount": "0.757",
      "initLoanAmount": "4321321.23820848",
      "hourRate": "59.1",
      "daily": "7",
      "borrowTime": "1684747528424",
      "status": "REPAY"
    }
  ]
}
```

## 查询资产负债

`GET /api/v2/earn/loan/debts`

限频规则: 10次/秒/UID

查询资产负债列表。

Operation ID: `classicEarnLoanGetDebts`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | object[] |  | 负债资产 |
| data.loanInfos[].coin | string |  | 币种 |
| data.loanInfos[].amount | string |  | 币种数量 |
| data.loanInfos[].amountUsdt | string |  | 估值 usdt |
| data.pledgeInfos | object[] |  | 质押资产 |
| data.pledgeInfos[].coin | string |  | 币种 |
| data.pledgeInfos[].amount | string |  | 币种数量 |
| data.pledgeInfos[].amountUsdt | string |  | 估值 usdt |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436610750,
  "data": {
    "pledgeInfos": [
      {
        "coin": "USDT",
        "amount": "28826.61539642",
        "amountUsdt": "28826.61"
      }
    ],
    "loanInfos": [
      {
        "coin": "ETH",
        "amount": "11.00002748",
        "amountUsdt": "18730.85"
      }
    ]
  }
}
```

## 查询强平记录

`GET /api/v2/earn/loan/reduces`

限频规则: 10次/秒/UID

获取强平记录列表。

Operation ID: `classicEarnLoanGetReduces`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 借贷币种 |
| pledgeCoin | query | string |  | 质押币种 |
| status | query | string |  | 强平状态<br><br>`COMPLETE` 已强平<br><br>`WAIT` 强平中 |
| startTime | query | string | 是 | 开始时间，仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNo | query | string |  | pageNo 默认值1 |
| pageSize | query | string |  | pageSize 默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].loanCoin | string |  | 已借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].reduceTime | string |  | 强平时间 |
| data[].pledgeRate | string |  | 强平时质押率百分比 |
| data[].pledgePrice | string |  | 强平时质押价格 |
| data[].status | string |  | 强平状态<br><br>`COMPLETE` 已强平<br><br>`WAIT` 强平中 |
| data[].pledgeAmount | string |  | 强平质押币数量 |
| data[].reduceFee | string |  | 强平费用 |
| data[].residueAmount | string |  | 剩余质押币数量 |
| data[].runlockAmount | string |  | 释放质押币数量 |
| data[].repayLoanAmount | string |  | 偿还借币欠款 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [
    {
      "orderId": "12121212121",
      "loanCoin": "TRX",
      "pledgeCoin": "USDT",
      "reduceTime": "0.757",
      "pledgeRate": "98.2",
      "pledgePrice": "111.4",
      "status": "COMPLETE",
      "pledgeAmount": "1213.5",
      "reduceFee": "REPAY",
      "residueAmount": "3234.2",
      "runlockAmount": "23",
      "repayLoanAmount": "53.2"
    }
  ]
}
```