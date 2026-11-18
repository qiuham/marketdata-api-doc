---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-cross-record
api_type: REST
updated_at: 2026-11-18 19:01:18.518909
---

# Classic Cross Margin Records API

Classic account — cross margin loan/repay/interest/liquidation records.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/crossed/borrow-history` — Get Cross Borrow History
- `GET /api/v2/margin/crossed/repay-history` — Get Cross Repay History
- `GET /api/v2/margin/crossed/interest-history` — Get Cross Interest History
- `GET /api/v2/margin/crossed/liquidation-history` — Get Cross Liquidation History
- `GET /api/v2/margin/crossed/financial-records` — Get Cross Financial History

## Get Cross Borrow History

`GET /api/v2/margin/crossed/borrow-history`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossLoanRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanId | query | string |  | Borrowing ID (exact match of single item) |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last loanId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].loanId | string |  | ID |
| data.resultList[].coin | string |  | Borrowed coin |
| data.resultList[].borrowAmount | string |  | Borrowing amount |
| data.resultList[].borrowType | string |  | Type of borrowing<br><br>`auto_loan`: auto borrow<br><br>`manual_loan`: manual borrow |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "resultList": [
      {
        "loanId": "1",
        "coin": "USDT",
        "borrowAmount": "12.1",
        "borrowType": "manual_loan",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Cross Repay History

`GET /api/v2/margin/crossed/repay-history`

Frequency limit:10 times/1s (IP)

Operation ID: `classicMarginCrossRecordGetCrossRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| repayId | query | string |  | Repayment ID |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last repayId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].repayId | string |  | Repayment ID |
| data.resultList[].coin | string |  | Repayment coin |
| data.resultList[].repayPrincipal | string |  | Repayment principal |
| data.resultList[].repayAmount | string |  | Total repayment |
| data.resultList[].repayInterest | string |  | Repayment interest |
| data.resultList[].repayType | string |  | Repayment type<br><br>auto_repay automatic repayment<br><br>manual_repay manual repayment<br><br>liq_repay liquidate and repay<br><br>force_repay compulsory repayment |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "resultList": [
      {
        "repayId": "1",
        "coin": "USDT",
        "repayAmount": "12.1",
        "repayType": "manual_repay",
        "repayInterest": "0.0001",
        "repayPrincipal": "0.1",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Cross Interest History

`GET /api/v2/margin/crossed/interest-history`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossInterestRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last loanId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].interestId | string |  | ID |
| data.resultList[].interestAmount | string |  | Interest amount |
| data.resultList[].dailyInterestRate | string |  | Daily interest rate |
| data.resultList[].interstType | string |  | Interest type<br><br>first interest on initial borrowing<br><br>scheduled: scheduled interest |
| data.resultList[].interestCoin | string |  | Interest coin |
| data.resultList[].loanCoin | string |  | Borrowing coin |
| data.resultList[].cTime | string |  | Creation time |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "minId": "1",
    "maxId": "1",
    "resultList": [
      {
        "interestId": "1",
        "loanCoin": "USDT",
        "interestCoin": "USDT",
        "dailyInterestRate": "0.00001",
        "interestAmount": "1.2",
        "interstType": "first",
        "uTime": "1668134458717",
        "cTime": "1668134458717"
      }
    ]
  }
}
```

## Get Cross Liquidation History

`GET /api/v2/margin/crossed/liquidation-history`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossLiquidationRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last liqId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].liqId | string |  | Liquidation ID |
| data.resultList[].liqStartTime | string |  | Liquidation start time |
| data.resultList[].liqEndTime | string |  | Liquidation end time |
| data.resultList[].liqRiskRatio | string |  | Risk ratio in liquidation |
| data.resultList[].totalAssets | string |  | Total assets in liquidation<br><br>In USDT |
| data.resultList[].totalDebt | string |  | Total debt in liquidation<br><br>In USDT |
| data.resultList[].liqFee | string |  | Liquidation transaction fees |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "minId": "1",
    "maxId": "1",
    "resultList": [
      {
        "liqId": "1",
        "liqStartTime": "1356756456873",
        "liqEndTime": "1356756456873",
        "liqRiskRatio": "0.1",
        "totalAssets": "154",
        "totalDebt": "123",
        "liqFee": "31.1",
        "uTime": "1668134458717",
        "cTime": "1668134458717"
      }
    ]
  }
}
```

## Get Cross Financial History

`GET /api/v2/margin/crossed/financial-records`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossFinanceFlowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marginType | query | string |  | Capital flow type<br><br>transfer_in: assets transferred in<br><br>transfer_out: assets transferred out<br><br>borrow: borrow<br><br>repay: repay<br><br>liquidation_fee: liquidation fee<br><br>compensate: collateral shortfall compensation from risk fund<br><br>deal_in: trade and deposit (buy)<br><br>deal_out: trade and withdraw (sell)<br><br>confiscated: deduction for collateral shortfall<br><br>exchange_in: exchange income, charged from the system account<br><br>exchange_out: exchange expense, charged to the system account<br><br>sys_exchange_in: exchange income of the system account, with exchange expense appearing at the same time<br><br>sys_exchange_out: exchange expense of the system account, with exchange income appearing at the same time |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last marginId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].coin | string |  | Coin |
| data.resultList[].marginId | string |  | Capital flow ID |
| data.resultList[].marginType | string |  | Capital flow type<br><br>transfer_in: assets transferred in<br><br>transfer_out: assets transferred out<br><br>borrow: borrow<br><br>repay: repay<br><br>liquidation_fee: liquidation fee<br><br>compensate: collateral shortfall compensation from risk fund<br><br>deal_in: trade and deposit (buy)<br><br>deal_out: trade and withdraw (sell)<br><br>confiscated: deduction for collateral shortfall<br><br>exchange_in: exchange income, charged from the system account<br><br>exchange_out: exchange expense, charged to the system account<br><br>sys_exchange_in: exchange income of the system account, with exchange expense appearing at the same time<br><br>sys_exchange_out: exchange expense of the system account, with exchange income appearing at the same time |
| data.resultList[].amount | string |  | Capital flow amount |
| data.resultList[].balance | string |  | Account balance |
| data.resultList[].fee | string |  | Transaction fee details |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "minId": "1",
    "maxId": "1",
    "resultList": [
      {
        "marginId": "1",
        "amount": "10.12",
        "coin": "USDT",
        "balance": "156",
        "fee": "0",
        "marginType": "transfer_in",
        "uTime": "1668134458717",
        "cTime": "1668134458717"
      }
    ]
  }
}
```


---

经典账户 — 全仓杠杆借币、还币、计息与强平记录。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/crossed/borrow-history` — 获取全仓借款历史
- `GET /api/v2/margin/crossed/repay-history` — 获取全仓还款历史
- `GET /api/v2/margin/crossed/interest-history` — 获取全仓利息历史
- `GET /api/v2/margin/crossed/liquidation-history` — 获取全仓强平历史
- `GET /api/v2/margin/crossed/financial-records` — 获取全仓财务流水记录

## 获取全仓借款历史

`GET /api/v2/margin/crossed/borrow-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossLoanRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| loanId | query | string |  | 借款ID(单条数据精准匹配) |
| coin | query | string |  | 币种 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条loanId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].loanId | string |  | ID |
| data.resultList[].coin | string |  | 借款币种 |
| data.resultList[].borrowAmount | string |  | 借款数量 |
| data.resultList[].borrowType | string |  | 借款类型<br><br>auto_loan 自动借款<br><br>manual_loan 手动借款 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "resultList": [
      {
        "loanId": "1",
        "coin": "USDT",
        "borrowAmount": "12.1",
        "borrowType": "manual_loan",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取全仓还款历史

`GET /api/v2/margin/crossed/repay-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| repayId | query | string |  | 还款ID |
| coin | query | string |  | 币种 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条repayId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].repayId | string |  | 还款ID |
| data.resultList[].coin | string |  | 还款币种 |
| data.resultList[].repayPrincipal | string |  | 还款本金 |
| data.resultList[].repayAmount | string |  | 还款总额 |
| data.resultList[].repayInterest | string |  | 还款利息 |
| data.resultList[].repayType | string |  | 还款类型<br><br>auto_repay 自动还款<br><br>manual_repay 手动还款<br><br>liq_repay 爆仓还款<br><br>force_repay 强制还款 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "resultList": [
      {
        "repayId": "1",
        "coin": "USDT",
        "repayAmount": "12.1",
        "repayType": "manual_repay",
        "repayInterest": "0.0001",
        "repayPrincipal": "0.1",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取全仓利息历史

`GET /api/v2/margin/crossed/interest-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossInterestRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条loanId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].interestId | string |  | ID |
| data.resultList[].interestAmount | string |  | 利息金额 |
| data.resultList[].dailyInterestRate | string |  | 日利率 |
| data.resultList[].interstType | string |  | 利息类型<br><br>first 首次借贷利息<br><br>scheduled 计时利息 |
| data.resultList[].interestCoin | string |  | 利息币种 |
| data.resultList[].loanCoin | string |  | 借贷币种 |
| data.resultList[].cTime | string |  | 创建时间 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "minId": "1",
    "maxId": "1",
    "resultList": [
      {
        "interestId": "1",
        "loanCoin": "USDT",
        "interestCoin": "USDT",
        "dailyInterestRate": "0.00001",
        "interestAmount": "1.2",
        "interstType": "first",
        "uTime": "1668134458717",
        "cTime": "1668134458717"
      }
    ]
  }
}
```

## 获取全仓强平历史

`GET /api/v2/margin/crossed/liquidation-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossLiquidationRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条liqId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].liqId | string |  | 强平ID |
| data.resultList[].liqStartTime | string |  | 强平开始时间 |
| data.resultList[].liqEndTime | string |  | 强平结束时间 |
| data.resultList[].liqRiskRatio | string |  | 强平时风险率 |
| data.resultList[].totalAssets | string |  | 强平时总资产<br><br>以USDT为单位 |
| data.resultList[].totalDebt | string |  | 强平时总欠款<br><br>以USDT为单位 |
| data.resultList[].liqFee | string |  | 强平手续费 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "resultList": [
      {
        "liqId": "1",
        "liqStartTime": "1695629859821",
        "liqEndTime": "1695629890839",
        "liqRiskRatio": "-1.69",
        "totalAssets": "622796.2085",
        "totalDebt": "641700",
        "liqFee": "12834",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取全仓财务流水记录

`GET /api/v2/margin/crossed/financial-records`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossRecordGetCrossFinanceFlowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marginType | query | string |  | 流水类型<br><br>transfer_in        转入资产<br><br>transfer_out        转出资产<br><br>borrow        借款<br><br>repay        还款<br><br>liquidation_fee        强平清算费<br><br>compensate        风险基金穿仓补偿<br><br>deal_in        成交入账（买入）<br><br>deal_out        成交出账（卖出）<br><br>confiscated        穿仓扣除<br><br>exchange_in        兑换收入，由系统帐户支出<br><br>exchange_out        兑换支出，由系统帐户收入<br><br>sys_exchange_in        系统帐户兑换收入，与兑换支出同时出现<br><br>sys_exchange_out        系统帐户兑换支出，与兑换收入同时出现 |
| coin | query | string |  | 币种 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条marginId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].coin | string |  | 币种 |
| data.resultList[].marginId | string |  | 流水ID |
| data.resultList[].marginType | string |  | 流水类型<br><br>transfer_in        转入资产<br><br>transfer_out        转出资产<br><br>borrow        借款<br><br>repay        还款<br><br>liquidation_fee        强平清算费<br><br>compensate        风险基金穿仓补偿<br><br>deal_in        成交入账（买入）<br><br>deal_out        成交出账（卖出）<br><br>confiscated        穿仓扣除<br><br>exchange_in        兑换收入，由系统帐户支出<br><br>exchange_out        兑换支出，由系统帐户收入<br><br>sys_exchange_in        系统帐户兑换收入，与兑换支出同时出现<br><br>sys_exchange_out        系统帐户兑换支出，与兑换收入同时出现 |
| data.resultList[].amount | string |  | 流水金额 |
| data.resultList[].balance | string |  | 账户余额 |
| data.resultList[].fee | string |  | 手续费明细 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695637102868,
  "data": {
    "resultList": [
      {
        "coin": "BTC",
        "marginId": "1",
        "amount": "0.0207",
        "balance": "3.2675574",
        "fee": "0.0000207",
        "marginType": "deal_in",
        "cTime": "1695629859862",
        "uTime": "1695629859983"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```