---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/crypto-loans
api_type: REST
updated_at: 2026-11-18 19:01:26.612787
---

# Crypto Loans

Collateralized crypto lending — borrow, repay, adjust collateral, and query loan/collateral history.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/loan/coins` — Get Loan Coins
- `GET /api/v3/loan/interest` — Get Loan Interest
- `POST /api/v3/loan/borrow` — Borrow Coins
- `GET /api/v3/loan/borrow-ongoing` — Get Borrow Ongoing
- `GET /api/v3/loan/borrow-history` — Get Borrow History
- `POST /api/v3/loan/repay` — Repay Coins
- `GET /api/v3/loan/repay-history` — Get Repay History
- `POST /api/v3/loan/revise-pledge` — Revise Pledge
- `GET /api/v3/loan/pledge-rate-history` — Get Pledge Rate History
- `GET /api/v3/loan/reduces` — Get Loan Reduces
- `GET /api/v3/loan/debts` — Get Loan Debts

## Get Loan Coins

`GET /api/v3/loan/coins`

Rate limit: 10/sec/UID

Get Loan Coins

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetLoanCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | string[] |  | List of borrowable coins |
| data.>coin | string |  | Borrowable coin |
| data.>hourRateFlexible | string |  | Flexible hourly interest rate (percentage) |
| data.>rateFlexible | string |  | Flexible APR (annualized percentage) |
| data.>hourRate7D | string |  | 7-day fixed hourly interest rate (pct.) |
| data.>rate7D | string |  | 7-day fixed APR (annualized percentage) |
| data.>hourRate30D | string |  | 30-day fixed hourly interest rate (pct.) |
| data.>rate30D | string |  | 30-day fixed APR (annualized percentage) |
| data.>minBorrowLimit | string |  | Minimum borrow limit (in USDT) |
| data.>maxBorrowLimit | string |  | Maximum borrow limit (in USDT) |
| data.>minBorrowAmount | string |  | Minimum borrow amount |
| data.>maxBorrowAmount | string |  | Maximum borrow amount |
| data.pledgeInfos | string[] |  | List of collateralizable coins |
| data.>initRate | string |  | Initial collateral ratio (percentage) |
| data.>supRate | string |  | Margin call (top-up) collateral ratio (pct.) |
| data.>forceRate | string |  | Liquidation collateral ratio (pct.) |
| data.>minPledgeAmount | string |  | Minimum collateral limit (in USDT) |
| data.>maxPledgeAmount | string |  | Maximum collateral limit (in USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770092353766,
  "data": {
    "loanInfos": [
      {
        "coin": "USDT",
        "hourRateFlexible": "0.00000349",
        "rateFlexible": "0.0305",
        "hourRate7D": "0.00000366",
        "rate7D": "0.032024937",
        "hourRate30D": "0.00000383",
        "rate30D": "0.033549934",
        "minBorrowAmount": "1",
        "maxBorrowAmount": "20000000",
        "minBorrowLimit": "1",
        "maxBorrowLimit": "20000000"
      }
    ],
    "pledgeInfos": [
      {
        "coin": "BGB",
        "initRate": "0.65",
        "supRate": "0.75",
        "forceRate": "0.91",
        "minPledgeAmount": "0",
        "maxPledgeAmount": "400000"
      }
    ]
  }
}
```

## Get Loan Interest

`GET /api/v3/loan/interest`

Rate limit: 10/sec/UID

Get Loan Interest

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetLoanInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanCoin | query | string | 是 | Coin to borrow <br><br>e.g.`BTC` |
| pledgeCoin | query | string | 是 | Collateral coin <br><br>e.g.`ETH` |
| daily | query | string | 是 | Pledge term:<br><br>`SEVEN` 7 days<br><br>`THIRTY` 30 days<br><br>`FLEXIBLE` flexible |
| pledgeAmount | query | string | 是 | Pledge Amount |

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
  "requestTime": 1770094037638,
  "data": {
    "hourInterest": "0.00000001",
    "loanAmount": "0.01935842"
  }
}
```

## Borrow Coins

`POST /api/v3/loan/borrow`

Rate limit: 10/sec/UID

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `cryptoLoansBorrowCoins`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | Coin to borrow <br><br>e.g.`BTC` |
| pledgeCoin | string | 是 | Collateral coin <br><br>e.g.`ETH` |
| daily | string | 是 | Pledge term:<br><br>`SEVEN` 7 days<br><br>`THIRTY` 30 days<br><br>`FLEXIBLE` flexible |
| pledgeAmount | string |  | Collateral amount <br><br>choose one of `pledgeAmount` or `loanAmount` |
| loanAmount | string |  | Borrow amount<br><br>choose one of `loanAmount` or `pledgeAmount` |

```json
{
  "loanCoin": "BTC",
  "pledgeCoin": "ETH",
  "daily": "SEVEN",
  "pledgeAmount": "1"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order Id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1745725444960,
  "data": {
    "orderId": "12345678"
  }
}
```

## Get Borrow Ongoing

`GET /api/v3/loan/borrow-ongoing`

Rate limit: 10/sec/UID

Get Borrow Ongoing

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetBorrowOngoing`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Borrowed coin |
| pledgeCoin | query | string |  | Collateral coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Ongoing borrow order list |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | borrowed coin |
| data[].loanAmount | string |  | borrowed amount |
| data[].interestAmount | string |  | Accrued interest amount |
| data[].hourInterestRate | string |  | Hourly interest rate |
| data[].pledgeCoin | string |  | Collateral coin |
| data[].pledgeAmount | string |  | Collateral amount |
| data[].pledgeRate | string |  | Collateral ratio |
| data[].supRate | string |  | Margin call (top-up) collateral ratio (pct.) |
| data[].forceRate | string |  | Liquidation collateral ratio (pct.) |
| data[].borrowTime | string |  | Borrow time<br><br>Unix timestamp in milliseconds |
| data[].expireTime | string |  | Expiry time<br><br>Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770185712179,
  "data": [
    {
      "orderId": "123456789010111",
      "loanCoin": "USDT",
      "loanAmount": "1.00032276",
      "interestAmount": "0.00000339",
      "hourInterestRate": "0.000338",
      "pledgeCoin": "BGB",
      "pledgeAmount": "0.42325892",
      "pledgeRate": "77.97",
      "supRate": "85",
      "forceRate": "91",
      "borrowTime": "1770185278083",
      "expireTime": "0"
    }
  ]
}
```

## Get Borrow History

`GET /api/v3/loan/borrow-history`

Rate limit: 10/sec/UID

Get Borrow History

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetBorrowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Borrowed coin |
| pledgeCoin | query | string |  | Collateral coin |
| status | query | string |  | Status<br><br>`ROLLBACK`: failed<br><br>`FORCE`: liquidated<br><br>`REPAY`: repaid |
| startTime | query | string | 是 | Start time<br><br>only supports querying data from the last 3 months |
| endTime | query | string | 是 | End time |
| pageNum | query | string |  | Page number<br><br>default is 1 |
| pageSize | query | string |  | Items per page<br><br>default is 10, maximum is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Borrow history list |
| data[].loanCoin | string |  | Borrowed coin |
| data[].pledgeCoin | string |  | Collateral coin |
| data[].orderId | string |  | Order ID |
| data[].initPledgeAmount | string |  | Initial collateral amount |
| data[].initLoanAmount | string |  | Initial borrowed amount |
| data[].hourRate | string |  | Hourly interest rate |
| data[].pledgeDays | string |  | Pledge/loan term in days |
| data[].borrowTime | string |  | Borrow time |
| data[].status | string |  | Status<br><br>`ROLLBACK`: failed<br><br>`FORCE`: liquidated<br><br>`REPAY`: repaid |
| data[].daily | string |  | Loan term type<br><br>`FLEXIBLE` Flexible loan |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770185989134,
  "data": [
    {
      "orderId": "12353453556666555111",
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "initPledgeAmount": "0.42325892",
      "initLoanAmount": "1.00032276",
      "hourRate": "0.000338",
      "daily": "FLEXIBLE",
      "borrowTime": "1770185278083",
      "status": "repay"
    }
  ]
}
```

## Repay Coins

`POST /api/v3/loan/repay`

Rate limit: 10/sec/UID

Repay Coins

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `cryptoLoansRepayCoins`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |
| repayAll | string | 是 | Repay in full<br><br>`yes`<br><br>`no`<br><br>If `yes`, the repayment `amount` will be ignored |
| amount | string |  | Repayment amount <br><br>Required when `repayAll=no` |
| repayUnlock | string |  | Whether to redeem collateral<br><br>`yes`redeem<br><br>`no`do not redeem<br><br>Default is `no` if omitted.<br><br>Not effective when `repayAll=yes` |

```json
{
  "orderId": "BTC",
  "repayAll": "yes"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | Borrowed coin |
| data.pledgeCoin | string |  | Collateral coin |
| data.repayAmount | string |  | Repayment amount |
| data.payInterest | string |  | Interest paid (in the borrowed coin) |
| data.repayLoanAmount | string |  | Principal repaid (in the borrowed coin) |
| data.repayUnlockAmount | string |  | Redeemed (unlocked) amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770191055753,
  "data": {
    "loanCoin": "USDT",
    "pledgeCoin": "BGB",
    "repayAmount": "1.00000713",
    "payInterest": "0.00000712",
    "repayLoanAmount": "1.00000001",
    "repayUnlockAmount": "0.50791233"
  }
}
```

## Get Repay History

`GET /api/v3/loan/repay-history`

Rate limit: 10/sec/UID

Get Repay History

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Borrowed coin |
| pledgeCoin | query | string |  | Collateral coin |
| startTime | query | string | 是 | Start time<br><br>only supports querying data from the last 3 months |
| endTime | query | string | 是 | End time |
| pageNum | query | string |  | Page number<br><br>default is 1 |
| pageSize | query | string |  | Items per page<br><br>default is 10, maximum is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Repay history list |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | Borrowed coin |
| data[].pledgeCoin | string |  | Collateral coin |
| data[].repayAmount | string |  | Repayment amount |
| data[].payInterest | string |  | Interest paid (in the borrowed coin) |
| data[].repayLoanAmount | string |  | Principal repaid (in the borrowed coin) |
| data[].repayUnlockAmount | string |  | Redeemed (unlocked) amount |
| data[].repayTime | string |  | Repayment time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770191679104,
  "data": [
    {
      "orderId": "1402828485131935745",
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "repayAmount": "1.00000713",
      "payInterest": "0.00000712",
      "repayLoanAmount": "1.00000001",
      "repayUnlockAmount": "0.50791233",
      "repayTime": "1770191055789"
    }
  ]
}
```

## Revise Pledge

`POST /api/v3/loan/revise-pledge`

Rate limit: 10/sec/UID

Revise Pledge

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `cryptoLoansRevisePledge`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |
| amount | string | 是 | Adjustment amount |
| pledgeCoin | string | 是 | Collateral coin |
| reviseType | string |  | Adjustment type<br><br>`OUT`: withdraw collateral<br><br>`IN` add collateral |

```json
{
  "orderId": "123456788661",
  "amount": "1",
  "pledgeCoin": "USDT",
  "reviseType": "IN"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | Borrowed coin |
| data.pledgeCoin | string |  | Collateral coin |
| data.afterPledgeRate | string |  | Post-adjustment collateral ratio (percentage) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770258559506,
  "data": {
    "loanCoin": "USDT",
    "pledgeCoin": "BGB",
    "afterPledgeRate": "0.15171614"
  }
}
```

## Get Pledge Rate History

`GET /api/v3/loan/pledge-rate-history`

Rate limit: 10/sec/UID

Get Pledge Rate History

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetPledgeRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| reviseSide | query | string |  | Adjustment direction <br><br>`down`: transfer in, decrease <br><br>`up`: transfer out, increase |
| pledgeCoin | query | string |  | Collateral coin |
| startTime | query | string | 是 | Start time<br><br>only supports querying data from the last 3 months |
| endTime | query | string | 是 | End time |
| pageNum | query | string |  | Page number<br><br>default is 1 |
| pageSize | query | string |  | Items per page<br><br>default is 10, maximum is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Pledge rate adjustment history list |
| data[].loanCoin | string |  | Borrowed coin |
| data[].pledgeCoin | string |  | Collateral coin |
| data[].orderId | string |  | Order ID |
| data[].reviseTime | string |  | Adjustment time |
| data[].reviseSide | string |  | Adjustment direction <br><br>`down`: transfer in, decrease <br><br>`up`: transfer out, increase |
| data[].reviseAmount | string |  | Adjustment amount |
| data[].afterPledgeRate | string |  | Post-adjustment collateral ratio (percentage) |
| data[].beforePledgeRate | string |  | Pre-adjustment collateral ratio (percentage) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770266423848,
  "data": [
    {
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "orderId": "1403131499696791555",
      "reviseTime": "1770258582049",
      "reviseSide": "up",
      "reviseAmount": "1.7",
      "afterPledgeRate": "64.97",
      "beforePledgeRate": "15.17"
    }
  ]
}
```

## Get Loan Reduces

`GET /api/v3/loan/reduces`

Rate limit: 10/sec/UID

Get Loan Reduces

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetLoanReduces`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| loanCoin | query | string |  | Borrowed coin |
| pledgeCoin | query | string |  | Collateral coin |
| status | query | string |  | Liquidation status<br><br>`COMPLETE` liquidated<br><br>`WAIT` liquidation |
| startTime | query | string | 是 | Start time<br><br>only supports querying data from the last 3 months |
| endTime | query | string | 是 | End time |
| pageNum | query | string |  | Page number<br><br>default is 1 |
| pageSize | query | string |  | Items per page<br><br>default is 10, maximum is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Liquidation record list |
| data[].orderId | string |  | Order ID |
| data[].loanCoin | string |  | Borrowed coin |
| data[].pledgeCoin | string |  | Collateral coin |
| data[].reduceTime | string |  | Liquidation time |
| data[].pledgeRate | string |  | Collateral ratio at liquidation (percentage) |
| data[].pledgePrice | string |  | Collateral price at liquidation |
| data[].status | string |  | Liquidation status<br><br>`COMPLETE` liquidated<br><br>`WAIT` liquidation |
| data[].pledgeAmount | string |  | Liquidated collateral amount |
| data[].reduceFee | string |  | Liquidation fee |
| data[].residueAmount | string |  | Remaining collateral amount |
| data[].runlockAmount | string |  | Released (unlocked) collateral amount |
| data[].repayLoanAmount | string |  | Repaid loan debt amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "loanCoin": "ETH",
      "reduceTime": "1765274978412",
      "pledgeRate": "60",
      "pledgeCoin": "USDT",
      "pledgePrice": "0.00016108",
      "status": "complete",
      "pledgeAmount": "100",
      "reduceFee": "0.00030606",
      "residueAmount": "0",
      "runlockAmount": "0",
      "repayLoanAmount": "0.0096652",
      "orderId": "1382228549318361088"
    }
  ]
}
```

## Get Loan Debts

`GET /api/v3/loan/debts`

Rate limit: 10/sec/UID

Get Loan Debts

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `cryptoLoansGetLoanDebts`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | string[] |  | Liability assets |
| data.>coin | string |  | Liability coin |
| data.>amount | string |  | Liability amount (denominated in `coin`) |
| data.>amountUsdt | string |  | Liability value (in `USDT`) |
| data.pledgeInfos | string[] |  | Collateral assets |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770266637419,
  "data": {
    "pledgeInfos": [
      {
        "coin": "BGB",
        "amount": "1.02556765",
        "amountUsdt": "3.03"
      }
    ],
    "loanInfos": [
      {
        "coin": "USDT",
        "amount": "2.00009297",
        "amountUsdt": "2.01"
      }
    ]
  }
}
```


---

质押借贷接口 — 借币、还币、调整质押率与借贷/质押历史查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/loan/coins` — 查询支持质押币种
- `GET /api/v3/loan/interest` — 查询预估利息及可借数量
- `POST /api/v3/loan/borrow` — 借币
- `GET /api/v3/loan/borrow-ongoing` — 查询当前借币
- `GET /api/v3/loan/borrow-history` — 查询借币历史
- `POST /api/v3/loan/repay` — 还款
- `GET /api/v3/loan/repay-history` — 查询还款历史
- `POST /api/v3/loan/revise-pledge` — 调整质押率
- `GET /api/v3/loan/pledge-rate-history` — 查询质押率历史
- `GET /api/v3/loan/reduces` — 查询强平记录
- `GET /api/v3/loan/debts` — 查询资产负债

## 查询支持质押币种

`GET /api/v3/loan/coins`

限频规则: 10次/秒/UID

查询支持质押币种

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读

Operation ID: `cryptoLoansGetLoanCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | string[] |  | 可借币种列表 |
| data.>coin | string |  | 可借币种 |
| data.>hourRateFlexible | string |  | 活期利率每小时百分比 |
| data.>rateFlexible | string |  | 活期利率年化百分比 |
| data.>hourRate7D | string |  | 7天固定利率每小时百分比 |
| data.>rate7D | string |  | 7天固定利率年化百分比 |
| data.>hourRate30D | string |  | 30天固定利率每小时百分比 |
| data.>rate30D | string |  | 30天固定利率年化百分比 |
| data.>minBorrowLimit | string |  | 最小可借限额<br><br>单位为USDT |
| data.>maxBorrowLimit | string |  | 最大可借限额<br><br>单位为USDT |
| data.>minBorrowAmount | string |  | 最小可借数量 |
| data.>maxBorrowAmount | string |  | 最大可借数量 |
| data.pledgeInfos | string[] |  | 可抵押币种列表 |
| data.>initRate | string |  | 初始质押率百分比 |
| data.>supRate | string |  | 补保质押率百分比 |
| data.>forceRate | string |  | 强平质押率百分比 |
| data.>minPledgeAmount | string |  | 最小质押限额<br><br>单位为USDT |
| data.>maxPledgeAmount | string |  | 最大质押限额<br><br>单位为USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770092353766,
  "data": {
    "loanInfos": [
      {
        "coin": "USDT",
        "hourRateFlexible": "0.00000349",
        "rateFlexible": "0.0305",
        "hourRate7D": "0.00000366",
        "rate7D": "0.032024937",
        "hourRate30D": "0.00000383",
        "rate30D": "0.033549934",
        "minBorrowAmount": "1",
        "maxBorrowAmount": "20000000",
        "minBorrowLimit": "1",
        "maxBorrowLimit": "20000000"
      }
    ],
    "pledgeInfos": [
      {
        "coin": "BGB",
        "initRate": "0.65",
        "supRate": "0.75",
        "forceRate": "0.91",
        "minPledgeAmount": "0",
        "maxPledgeAmount": "400000"
      }
    ]
  }
}
```

## 查询预估利息及可借数量

`GET /api/v3/loan/interest`

限频规则: 10次/秒/UID

查询预估利息及可借数量

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读

Operation ID: `cryptoLoansGetLoanInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanCoin | query | string | 是 | 需借币种 <br><br>如`BTC` |
| pledgeCoin | query | string | 是 | 质押币种<br><br>如`ETH` |
| daily | query | string | 是 | 质押天数<br><br>`SEVEN` 7天<br><br>`THIRTY`30天<br><br>`FLEXIBLE`活期 |
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
  "requestTime": 1770094037638,
  "data": {
    "hourInterest": "0.00000001",
    "loanAmount": "0.01935842"
  }
}
```

## 借币

`POST /api/v3/loan/borrow`

限频规则: 10次/秒/UID

- 限频规则: 10次/秒/UID

- 需要统一账户管理读写权限

Operation ID: `cryptoLoansBorrowCoins`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | 需借币种 <br><br>如`BTC` |
| pledgeCoin | string | 是 | 质押币种<br><br>如`ETH` |
| daily | string | 是 | 质押天数<br><br>`SEVEN` 7天<br><br>`THIRTY`30天<br><br>`FLEXIBLE`活期 |
| pledgeAmount | string |  | 质押数量<br><br>与loanAmount二选一 |
| loanAmount | string |  | 借币数量<br><br>与pledgeAmount二选一 |

```json
{
  "loanCoin": "BTC",
  "pledgeCoin": "ETH",
  "daily": "SEVEN",
  "pledgeAmount": "1"
}
```

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
  "requestTime": 1745725444960,
  "data": {
    "orderId": "12345678"
  }
}
```

## 查询当前借币

`GET /api/v3/loan/borrow-ongoing`

限频规则: 10次/秒/UID

查询当前借币

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetBorrowOngoing`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 负债币种 |
| pledgeCoin | query | string |  | 质押币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 当前借币列表 |
| data[].orderId | string |  | 订单ID |
| data[].loanCoin | string |  | 负债币种 |
| data[].loanAmount | string |  | 负债数量 |
| data[].interestAmount | string |  | 已产生利息数量 |
| data[].hourInterestRate | string |  | 小时利率百分比 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].pledgeAmount | string |  | 质押数量 |
| data[].pledgeRate | string |  | 质押率百分比 |
| data[].supRate | string |  | 补保质押率百分比 |
| data[].forceRate | string |  | 强平质押率百分比 |
| data[].borrowTime | string |  | 借币时间<br><br>Unix毫秒时间戳 |
| data[].expireTime | string |  | 到期时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770185712179,
  "data": [
    {
      "orderId": "123456789010111",
      "loanCoin": "USDT",
      "loanAmount": "1.00032276",
      "interestAmount": "0.00000339",
      "hourInterestRate": "0.000338",
      "pledgeCoin": "BGB",
      "pledgeAmount": "0.42325892",
      "pledgeRate": "77.97",
      "supRate": "85",
      "forceRate": "91",
      "borrowTime": "1770185278083",
      "expireTime": "0"
    }
  ]
}
```

## 查询借币历史

`GET /api/v3/loan/borrow-history`

限频规则: 10次/秒/UID

查询借币历史

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetBorrowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 负债币种 |
| pledgeCoin | query | string |  | 质押币种 |
| status | query | string |  | 状态<br><br>`ROLLBACK`: 失败<br><br>`FORCE`: 强平<br><br>`REPAY`: 已还款 |
| startTime | query | string | 是 | 开始时间<br><br>仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNum | query | string |  | 页码<br><br>默认值1 |
| pageSize | query | string |  | 每页条目数<br><br>默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 借币历史列表 |
| data[].loanCoin | string |  | 已借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].orderId | string |  | 订单ID |
| data[].initPledgeAmount | string |  | 初始化质押数量 |
| data[].initLoanAmount | string |  | 初始化借币数量 |
| data[].hourRate | string |  | 每小时利率百分比 |
| data[].pledgeDays | string |  | 质押借贷天数 |
| data[].borrowTime | string |  | 借币时间 |
| data[].status | string |  | 状态<br><br>`ROLLBACK`: 失败<br><br>`FORCE`: 强平<br><br>`REPAY`: 已还款 |
| data[].daily | string |  | 借贷类型<br><br>`FLEXIBLE` 活期借贷 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770185989134,
  "data": [
    {
      "orderId": "12353453556666555111",
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "initPledgeAmount": "0.42325892",
      "initLoanAmount": "1.00032276",
      "hourRate": "0.000338",
      "daily": "FLEXIBLE",
      "borrowTime": "1770185278083",
      "status": "repay"
    }
  ]
}
```

## 还款

`POST /api/v3/loan/repay`

限频规则: 10次/秒/UID

还款

- 限频规则: 10次/秒/UID

- 需要统一账户管理读写权限

Operation ID: `cryptoLoansRepayCoins`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单ID |
| repayAll | string | 是 | 是否全部还款<br><br>`yes`是<br><br>`no`否<br><br>如果选择全部还款，则忽略还款数量 |
| amount | string |  | 还款数量 <br><br>`repayAll=no`时，该字段必填 |
| repayUnlock | string |  | 是否取回抵押品<br><br>`yes`取回<br><br>`no`不取回<br><br>如不填写，默认值为`no`<br><br>当`repayAll=yes`时，该参数不生效 |

```json
{
  "orderId": "BTC",
  "repayAll": "yes"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanCoin | string |  | 借款币种 |
| data.pledgeCoin | string |  | 质押币种 |
| data.repayAmount | string |  | 还款数量 |
| data.payInterest | string |  | 借币币种支付利息数量 |
| data.repayLoanAmount | string |  | 借币币种归还本金数量 |
| data.repayUnlockAmount | string |  | 赎回数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770191055753,
  "data": {
    "loanCoin": "USDT",
    "pledgeCoin": "BGB",
    "repayAmount": "1.00000713",
    "payInterest": "0.00000712",
    "repayLoanAmount": "1.00000001",
    "repayUnlockAmount": "0.50791233"
  }
}
```

## 查询还款历史

`GET /api/v3/loan/repay-history`

限频规则: 10次/秒/UID

查询还款历史

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 负债币种 |
| pledgeCoin | query | string |  | 质押币种 |
| startTime | query | string | 是 | 开始时间<br><br>仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNum | query | string |  | 页码<br><br>默认值1 |
| pageSize | query | string |  | 每页条目数<br><br>默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 还款历史列表 |
| data[].orderId | string |  | 订单ID |
| data[].loanCoin | string |  | 已借币种 |
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
  "requestTime": 1770191679104,
  "data": [
    {
      "orderId": "1402828485131935745",
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "repayAmount": "1.00000713",
      "payInterest": "0.00000712",
      "repayLoanAmount": "1.00000001",
      "repayUnlockAmount": "0.50791233",
      "repayTime": "1770191055789"
    }
  ]
}
```

## 调整质押率

`POST /api/v3/loan/revise-pledge`

限频规则: 10次/秒/UID

调整质押率

- 限频规则: 10次/秒/UID

- 需要统一账户管理读写权限

Operation ID: `cryptoLoansRevisePledge`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单ID |
| amount | string | 是 | 调整数量 |
| pledgeCoin | string | 是 | 质押币种 |
| reviseType | string |  | 调整类型<br><br>`OUT`: 提取质押品<br><br>`IN` 补充质押品 |

```json
{
  "orderId": "123456788661",
  "amount": "1",
  "pledgeCoin": "USDT",
  "reviseType": "IN"
}
```

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
  "requestTime": 1770258559506,
  "data": {
    "loanCoin": "USDT",
    "pledgeCoin": "BGB",
    "afterPledgeRate": "0.15171614"
  }
}
```

## 查询质押率历史

`GET /api/v3/loan/pledge-rate-history`

限频规则: 10次/秒/UID

查询质押率历史

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetPledgeRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| reviseSide | query | string |  | 调整方向 <br><br>`down`: 转入调低 <br><br>`up`: 转出调高 |
| pledgeCoin | query | string |  | 质押币种 |
| startTime | query | string | 是 | 开始时间<br><br>仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNum | query | string |  | 页码<br><br>默认值1 |
| pageSize | query | string |  | 每页条目数<br><br>默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 质押率调整历史列表 |
| data[].loanCoin | string |  | 已借币种 |
| data[].pledgeCoin | string |  | 质押币种 |
| data[].orderId | string |  | 订单ID |
| data[].reviseTime | string |  | 调整时间 |
| data[].reviseSide | string |  | 调整方向 <br><br>`down`: 转入调低 <br><br>`up`: 转出调高 |
| data[].reviseAmount | string |  | 调整数量 |
| data[].afterPledgeRate | string |  | 调整后质押利率百分比 |
| data[].beforePledgeRate | string |  | 调整前质押利率百分比 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770266423848,
  "data": [
    {
      "loanCoin": "USDT",
      "pledgeCoin": "BGB",
      "orderId": "1403131499696791555",
      "reviseTime": "1770258582049",
      "reviseSide": "up",
      "reviseAmount": "1.7",
      "afterPledgeRate": "64.97",
      "beforePledgeRate": "15.17"
    }
  ]
}
```

## 查询强平记录

`GET /api/v3/loan/reduces`

限频规则: 10次/秒/UID

查询强平记录

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetLoanReduces`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID |
| loanCoin | query | string |  | 借贷币种 |
| pledgeCoin | query | string |  | 质押币种 |
| status | query | string |  | 强平状态<br><br>`COMPLETE` 已强平<br><br>`WAIT` 强平中 |
| startTime | query | string | 是 | 开始时间<br><br>仅支持查询近三个月数据 |
| endTime | query | string | 是 | 结束时间 |
| pageNum | query | string |  | 页码<br><br>默认值1 |
| pageSize | query | string |  | 每页条目数<br><br>默认值10，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 强平记录列表 |
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
  "requestTime": 1711697588556,
  "data": [
    {
      "loanCoin": "ETH",
      "reduceTime": "1765274978412",
      "pledgeRate": "60",
      "pledgeCoin": "USDT",
      "pledgePrice": "0.00016108",
      "status": "complete",
      "pledgeAmount": "100",
      "reduceFee": "0.00030606",
      "residueAmount": "0",
      "runlockAmount": "0",
      "repayLoanAmount": "0.0096652",
      "orderId": "1382228549318361088"
    }
  ]
}
```

## 查询资产负债

`GET /api/v3/loan/debts`

限频规则: 10次/秒/UID

查询资产负债

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `cryptoLoansGetLoanDebts`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanInfos | string[] |  | 负债资产 |
| data.>coin | string |  | 负债币种 |
| data.>amount | string |  | 负债币种数量<br><br>单位为`coin` |
| data.>amountUsdt | string |  | 负债币种价值<br><br>单位为`USDT` |
| data.pledgeInfos | string[] |  | 质押资产 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1770266637419,
  "data": {
    "pledgeInfos": [
      {
        "coin": "BGB",
        "amount": "1.02556765",
        "amountUsdt": "3.03"
      }
    ],
    "loanInfos": [
      {
        "coin": "USDT",
        "amount": "2.00009297",
        "amountUsdt": "2.01"
      }
    ]
  }
}
```