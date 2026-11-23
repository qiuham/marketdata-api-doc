---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-isolated-record
api_type: REST
updated_at: 2026-11-23 19:02:33.601135
---

# Classic Isolated Margin Records API

Classic account — isolated margin loan/repay/interest/liquidation records.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/isolated/repay-history` — Get Isolated Repayment History
- `GET /api/v2/margin/isolated/borrow-history` — Get Isolated Borrow History
- `GET /api/v2/margin/isolated/interest-history` — Get Isolated Interest History
- `GET /api/v2/margin/isolated/liquidation-history` — Get Isolated Liquidation History
- `GET /api/v2/margin/isolated/financial-records` — Get Isolated Financial History

## Get Isolated Repayment History

`GET /api/v2/margin/isolated/repay-history`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, BTCUSDT |
| repayId | query | string |  | Repayment ID |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps<br><br>Maximum interval between start and end times is 90 days |
| limit | query | string |  | Number of queries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. No setting is needed when querying for the first time. Set to to smallest repayId returned from the last query when searching for data in the second page and other paged. Data smaller than the repayId entered will be returned. This is designed to shorten the query response time. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | List |
| data.resultList[].symbol | string |  | Trading pair |
| data.resultList[].repayId | string |  | ID |
| data.resultList[].coin | string |  | Coin |
| data.resultList[].repayPrincipal | string |  | Repayment principal |
| data.resultList[].repayAmount | string |  | Total repayment |
| data.resultList[].repayInterest | string |  | Repayment interest |
| data.resultList[].repayType | string |  | Repayment type<br><br>auto_repay: Automatic repayment<br><br>manual_repay: Manual repayment<br><br>liq_repay: Liquidation repayment<br><br>force_repay: Forced repayment |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624627000.0,
  "data": {
    "resultList": [
      {
        "repayId": "1",
        "coin": "BTC",
        "repayAmount": "1",
        "repayType": "manual_repay",
        "repayInterest": "0.01",
        "repayPrincipal": "0.99",
        "symbol": "BTCUSDT",
        "cTime": "1695624616058",
        "uTime": "1695624616058"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Isolated Borrow History

`GET /api/v2/margin/isolated/borrow-history`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedLoanRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, BTCUSDT |
| loanId | query | string |  | Borrowing ID (accurate matching of single entry) |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps<br><br>Maximum interval between start and end times is 90 days |
| limit | query | string |  | Number of queries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. No setting is needed when querying for the first time. Set to to smallest loanId returned from the last query when searching for data in the second page and other paged. Data smaller than the loanId entered will be returned. This is designed to shorten the query response time. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | List |
| data.resultList[].symbol | string |  | Trading pair |
| data.resultList[].loanId | string |  | ID |
| data.resultList[].coin | string |  | Borrowed coin |
| data.resultList[].borrowAmount | string |  | Borrowed amount |
| data.resultList[].borrowType | string |  | Type of borrowing<br><br>auto_loan: Auto-loan<br><br>manual_loan: manual_loan |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624081817,
  "data": {
    "resultList": [
      {
        "loanId": "1",
        "coin": "USDT",
        "borrowAmount": "1",
        "borrowType": "manual_loan",
        "symbol": "BTCUSDT",
        "cTime": "1695624061276",
        "uTime": "1695624061276"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Isolated Interest History

`GET /api/v2/margin/isolated/interest-history`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedInterestRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps<br><br>Maximum interval between start and end times is 90 days |
| limit | query | string |  | Number of queries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. No setting is needed when querying for the first time. Set to to smallest interestId returned from the last query when searching for data in the second page and other paged. Data smaller than the interestId entered will be returned. This is designed to shorten the query response time. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | List |
| data.resultList[].symbol | string |  | Trading pair |
| data.resultList[].interestId | string |  | Interest ID |
| data.resultList[].interestAmount | string |  | Amount of interest |
| data.resultList[].dailyInterestRate | string |  | Daily interest rate |
| data.resultList[].interstType | string |  | Type of interest<br><br>first: Interest on initial borrowing<br><br>scheduled: scheduled interest |
| data.resultList[].interestCoin | string |  | Interest coin |
| data.resultList[].loanCoin | string |  | Borrowing coin |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624945382,
  "data": {
    "resultList": [
      {
        "interestId": "1",
        "interestCoin": "USDT",
        "dailyInterestRate": "0.24",
        "loanCoin": "USDT",
        "interestAmount": "0.01",
        "interstType": "first",
        "symbol": "BTCUSDT",
        "cTime": "1695624061276",
        "uTime": "1695624061276"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Isolated Liquidation History

`GET /api/v2/margin/isolated/liquidation-history`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedLiquidationRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps<br><br>Maximum interval between start and end times is 90 days |
| limit | query | string |  | Number of queries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. No setting is needed when querying for the first time. Set to to smallest liqId returned from the last query when searching for data in the second page and other paged. Data smaller than the liqId entered will be returned. This is designed to shorten the query response time. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | List |
| data.resultList[].symbol | string |  | Trading pair |
| data.resultList[].liqId | string |  | Liquidation ID |
| data.resultList[].liqStartTime | string |  | Start time of liquidation |
| data.resultList[].liqEndTime | string |  | Liquidation end time |
| data.resultList[].liqRiskRatio | string |  | Risk ratio at liquidation |
| data.resultList[].totalAssets | string |  | Total assets at liquidation<br><br>in USDT |
| data.resultList[].totalDebt | string |  | Total borrowings at liquidation<br><br>in USDT |
| data.resultList[].liqFee | string |  | Liquidation fees |
| data.resultList[].cTime | string |  | Creation time, millisecond timestamp |
| data.resultList[].uTime | string |  | Update time, millisecond timestamp |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624945382,
  "data": {
    "resultList": [
      {
        "liqId": "123",
        "symbol": "BTCUSDT",
        "liqStartTime": "1653453245342",
        "liqEndTime": "16312423423432",
        "liqRiskRatio": "1.01",
        "totalAssets": "1242.34",
        "totalDebt": "1100",
        "liqFee": "1.2",
        "cTime": "1653453245342",
        "uTime": "1692690126000"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Isolated Financial History

`GET /api/v2/margin/isolated/financial-records`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedFinanceHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, BTCUSDT |
| marginType | query | string |  | Capital flow type<br><br>transfer_in: inbound transfer<br><br>transfer_out: outbound transfer<br><br>borrow: Borrowings<br><br>repay: Repayment<br><br>liquidation_fee: Liquidation fee<br><br>compensate: Risk fund compensation for collateral shortfall<br><br>deal_in: buy<br><br>deal_out: sell<br><br>confiscated: Deducted for collateral shortfall<br><br>exchange_in: Exchange income, charged to the system account<br><br>exchange_out: Exchange spending, received by the system account<br><br>sys_exchange_in: exchange income of the system account, with exchange spending appearing at the same time<br><br>sys_exchange_out: exchange spending of the system account, with exchange income appearing at the same time |
| coin | query | string |  | Coin |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps<br><br>Maximum interval between start and end times is 90 days |
| limit | query | string |  | Number of queries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. No setting is needed when querying for the first time. Set to to smallest marginId returned from the last query when searching for data in the second page and other paged. Data smaller than the marginId entered will be returned. This is designed to shorten the query response time. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | List |
| data.resultList[].symbol | string |  | Trading pair |
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
  "requestTime": 1695625219083,
  "data": {
    "resultList": [
      {
        "coin": "BTC",
        "symbol": "BTCUSDT",
        "marginId": "1",
        "amount": "-1",
        "balance": "199999.0036963",
        "fee": "0",
        "marginType": "repay",
        "cTime": "1695624616058",
        "uTime": "1695624616058"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```


---

经典账户 — 逐仓杠杆借币、还币、计息与强平记录。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/isolated/repay-history` — 获取逐仓还款历史
- `GET /api/v2/margin/isolated/borrow-history` — 获取逐仓借款历史
- `GET /api/v2/margin/isolated/interest-history` — 获取逐仓利息历史
- `GET /api/v2/margin/isolated/liquidation-history` — 获取逐仓强平历史
- `GET /api/v2/margin/isolated/financial-records` — 获取逐仓财务记录

## 获取逐仓还款历史

`GET /api/v2/margin/isolated/repay-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
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
| data.resultList | object[] |  | 列表 |
| data.resultList[].symbol | string |  | 交易对名称 |
| data.resultList[].repayId | string |  | ID |
| data.resultList[].coin | string |  | 币种 |
| data.resultList[].repayPrincipal | string |  | 还款本金 |
| data.resultList[].repayAmount | string |  | 还款总额 |
| data.resultList[].repayInterest | string |  | 还款利息 |
| data.resultList[].repayType | string |  | 还款类型<br><br>auto_repay 自动还款<br><br>manual_repay 手动还款<br><br>liq_repay 爆仓还款<br><br>force_repay 强制还款 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 本次查询结果最大的ID |
| data.minId | string |  | 本次查询结果最小的ID，下次查询时入参使用本值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624627000.0,
  "data": {
    "resultList": [
      {
        "repayId": "1",
        "coin": "BTC",
        "repayAmount": "1",
        "repayType": "manual_repay",
        "repayInterest": "0.01",
        "repayPrincipal": "0.99",
        "symbol": "BTCUSDT",
        "cTime": "1695624616058",
        "uTime": "1695624616058"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取逐仓借款历史

`GET /api/v2/margin/isolated/borrow-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedLoanRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
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
| data.resultList | object[] |  | 列表 |
| data.resultList[].symbol | string |  | 交易对名称 |
| data.resultList[].loanId | string |  | ID |
| data.resultList[].coin | string |  | 借款币种 |
| data.resultList[].borrowAmount | string |  | 借款数量 |
| data.resultList[].borrowType | string |  | 借款类型<br><br>auto_loan 自动借款<br><br>manual_loan 手动借款 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 本次查询结果最大的ID |
| data.minId | string |  | 本次查询结果最小的ID，下次查询时入参使用本值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624081817,
  "data": {
    "resultList": [
      {
        "loanId": "1",
        "coin": "USDT",
        "borrowAmount": "1",
        "borrowType": "manual_loan",
        "symbol": "BTCUSDT",
        "cTime": "1695624061276",
        "uTime": "1695624061276"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取逐仓利息历史

`GET /api/v2/margin/isolated/interest-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedInterestRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
| coin | query | string |  | 币种 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条interestId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 列表 |
| data.resultList[].symbol | string |  | 交易对名称 |
| data.resultList[].interestId | string |  | 利息ID |
| data.resultList[].interestAmount | string |  | 利息金额 |
| data.resultList[].dailyInterestRate | string |  | 日利率 |
| data.resultList[].interstType | string |  | 利息类型<br><br>first 首次借贷利息<br><br>scheduled 计时利息 |
| data.resultList[].interestCoin | string |  | 利息币种 |
| data.resultList[].loanCoin | string |  | 借贷币种 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 本次查询结果最大的ID |
| data.minId | string |  | 本次查询结果最小的ID，下次查询时入参使用本值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624945382,
  "data": {
    "resultList": [
      {
        "interestId": "1",
        "interestCoin": "USDT",
        "dailyInterestRate": "0.24",
        "loanCoin": "USDT",
        "interestAmount": "0.01",
        "interstType": "first",
        "symbol": "BTCUSDT",
        "cTime": "1695624061276",
        "uTime": "1695624061276"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取逐仓强平历史

`GET /api/v2/margin/isolated/liquidation-history`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedLiquidationRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对 |
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
| data.resultList | object[] |  | 列表 |
| data.resultList[].symbol | string |  | 交易对名称 |
| data.resultList[].liqId | string |  | 强平ID |
| data.resultList[].liqStartTime | string |  | 强平开始时间 |
| data.resultList[].liqEndTime | string |  | 强平结束时间 |
| data.resultList[].liqRiskRatio | string |  | 强平时风险率 |
| data.resultList[].totalAssets | string |  | 强平时总资产<br><br>以USDT为单位 |
| data.resultList[].totalDebt | string |  | 强平时总欠款<br><br>以USDT为单位 |
| data.resultList[].liqFee | string |  | 强平手续费 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.maxId | string |  | 本次查询结果最大的ID |
| data.minId | string |  | 本次查询结果最小的ID，下次查询时入参使用本值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695624945382,
  "data": {
    "resultList": [
      {
        "liqId": "1",
        "symbol": "BTCUSDT",
        "liqStartTime": "1653453245342",
        "liqEndTime": "16312423423432",
        "liqRiskRatio": "1.01",
        "totalAssets": "1242.34",
        "totalDebt": "1100",
        "liqFee": "1.2",
        "cTime": "1653453245342",
        "uTime": "1692690126000"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## 获取逐仓财务记录

`GET /api/v2/margin/isolated/financial-records`

限速规则 10次/1s (UID)

Operation ID: `classicMarginIsolatedRecordGetIsolatedFinanceHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
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
| data.resultList | object[] |  | 列表 |
| data.resultList[].symbol | string |  | 交易对名称 |
| data.resultList[].coin | string |  | 币种 |
| data.resultList[].marginId | string |  | 流水ID |
| data.resultList[].marginType | string |  | 流水类型<br><br>transfer_in        转入资产<br><br>transfer_out        转出资产<br><br>borrow        借款<br><br>repay        还款<br><br>liquidation_fee        强平清算费<br><br>compensate        风险基金穿仓补偿<br><br>deal_in        成交入账（买入）<br><br>deal_out        成交出账（卖出）<br><br>confiscated        穿仓扣除<br><br>exchange_in        兑换收入，由系统帐户支出<br><br>exchange_out        兑换支出，由系统帐户收入<br><br>sys_exchange_in        系统帐户兑换收入，与兑换支出同时出现<br><br>sys_exchange_out        系统帐户兑换支出，与兑换收入同时出现 |
| data.resultList[].amount | string |  | 流水金额 |
| data.resultList[].balance | string |  | 账户余额 |
| data.resultList[].fee | string |  | 手续费明细 |
| data.resultList[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.resultList[].uTime | string |  | 更新时间, ms |
| data.maxId | string |  | 本次查询结果最大的ID |
| data.minId | string |  | 本次查询结果最小的ID，下次查询时入参使用本值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695625219083,
  "data": {
    "resultList": [
      {
        "coin": "BTC",
        "symbol": "BTCUSDT",
        "marginId": "1",
        "amount": "-1",
        "balance": "199999.0036963",
        "fee": "0",
        "marginType": "repay",
        "cTime": "1695624616058",
        "uTime": "1695624616058"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```