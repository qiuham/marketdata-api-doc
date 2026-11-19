---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-instloan-orders
api_type: REST
updated_at: 2026-11-19 19:07:52.257185
---

# Classic Inst Loan Orders API

Classic account — institutional loan and repayment order queries.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/loan-order` — Get Loan Orders
- `GET /api/v2/spot/ins-loan/repaid-history` — Get Repayment Orders

## Get Loan Orders

`GET /api/v2/spot/ins-loan/loan-order`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanOrdersGetLoanOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Loan order id<br><br>If not passed, then return all orders, sort by loanTime in descend |
| startTime | query | string |  | The start timestamp (ms) <br><br>  （The maximum time span supported is 30 days. If the start time is not provided, it defaults to the current time minus 30 days.） |
| endTime | query | string |  | The end timestamp (ms) <br><br> （The maximum time span supported is 30 days. If the end time is not provided, the default end time is 30 days from the start.） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanInfo | object[] |  | Loan orders information |
| data[].loanInfo[].orderId | string |  | Loan order ID |
| data[].loanInfo[].orderProductId | string |  | Product Id |
| data[].loanInfo[].uid | string |  | The designated UID that is used to bind INS loan product, loan and repayment |
| data[].loanInfo[].loanTime | string |  | Loan timestamp, in milliseconds |
| data[].loanInfo[].loanCoin | string |  | Loan coin |
| data[].loanInfo[].loanAmount | string |  | Loan amount |
| data[].loanInfo[].unpaidAmount | string |  | Unpaid principal |
| data[].loanInfo[].unpaidInterest | string |  | Unpaid interest |
| data[].loanInfo[].repaidAmount | string |  | Repaid principal |
| data[].loanInfo[].repaidInterest | string |  | Repaid interest |
| data[].loanInfo[].status | string |  | Status<br><br>`not_paid_off`: Not paid off<br><br>`paid_off`: paid off |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "orderId": "xxxxxxx",
      "orderProductId": "xxxxxx",
      "uid": "xxxxxx",
      "loanTime": "1713645576789",
      "loanCoin": "USDT",
      "unpaidAmount": "1",
      "unpaidInterest": "1",
      "loanAmount": "1",
      "status": "paid_off",
      "repaidAmount": "1",
      "repaidInterest": "1.1"
    }
  ]
}
```

## Get Repayment Orders

`GET /api/v2/spot/ins-loan/repaid-history`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanOrdersGetRepaymentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | The start timestamp (ms) |
| endTime | query | string |  | The end timestamp (ms) |
| limit | query | string |  | Limit default 100;  max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayOrderId | string |  | Repaid order ID |
| data[].repaidTime | string[] |  | Repaid timestamp (ms) |
| data[].coin | string |  | Repaid coin |
| data[].repayAmount | string |  | Repaid principle |
| data[].repayInterest | string |  | Repaid interest |
| data[].repayType | string |  | Repaid type<br><br>`all`: All repayment<br><br>`part`: partial repayment |
| data[].businessType | string |  | Business type<br><br>`normal`: normal repayment<br><br>`liquidation`: repaid by liquidation |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "repayOrderId": "xxxxxxx",
      "businessType": "normal",
      "repayType": "all",
      "repaidTime": "1713645576789",
      "coin": "USDT",
      "repaidAmount": "1",
      "repaidInterest": "1.1"
    }
  ]
}
```


---

经典账户 — 机构借贷借款与还款订单查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/loan-order` — 查询借贷订单信息
- `GET /api/v2/spot/ins-loan/repaid-history` — 查询还款订单信息

## 查询借贷订单信息

`GET /api/v2/spot/ins-loan/loan-order`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanOrdersGetLoanOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 借贷订单ID。若不传，则返回全部。按照loanTime降序排列 |
| startTime | query | string |  | 开始时间戳 (毫秒) <br><br>（时间跨度最大支持30天，若不传开始时间，则默认为当前时间减去30天。） |
| endTime | query | string |  | 结束时间戳 (毫秒) <br><br> （时间跨度最大支持30天，若不传结束时间，则默认结束时间为30天。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].loanInfo | object[] |  | 借贷订单信息 |
| data[].loanInfo[].orderId | string |  | 借贷订单ID |
| data[].loanInfo[].orderProductId | string |  | 产品ID |
| data[].loanInfo[].uid | string |  | 机构借贷放款和还款UID |
| data[].loanInfo[].loanTime | string |  | 放款时间戳（毫秒） |
| data[].loanInfo[].loanCoin | string |  | 借款币种 |
| data[].loanInfo[].loanAmount | string |  | 借款金额 |
| data[].loanInfo[].unpaidAmount | string |  | 未还本金 |
| data[].loanInfo[].unpaidInterest | string |  | 未还利息 |
| data[].loanInfo[].repaidAmount | string |  | 已还本金 |
| data[].loanInfo[].repaidInterest | string |  | 已还利息 |
| data[].loanInfo[].status | string |  | 状态<br><br>未还清 `not_paid_off`<br><br>已还清 `paid_off` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "orderId": "xxxxxxx",
      "orderProductId": "xxxxxx",
      "uid": "xxxxxx",
      "loanTime": "1713645576789",
      "loanCoin": "USDT",
      "unpaidAmount": "1",
      "unpaidInterest": "1",
      "loanAmount": "1",
      "status": "paid_off",
      "repaidAmount": "1",
      "repaidInterest": "1.1"
    }
  ]
}
```

## 查询还款订单信息

`GET /api/v2/spot/ins-loan/repaid-history`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanOrdersGetRepaymentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳 (毫秒) |
| endTime | query | string |  | 结束时间戳 (毫秒) |
| limit | query | string |  | 返回数量限制。\[1, 100\], 默认: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayOrderId | string |  | 还款订单号 |
| data[].repaidTime | string[] |  | 还款时间（毫秒） |
| data[].coin | string |  | 还款币种 |
| data[].repayAmount | string |  | 还款本金 |
| data[].repayInterest | string |  | 还款利息 |
| data[].repayType | string |  | 还款类型<br><br>`all`: 全部还款<br><br> `part`: 部分还款 |
| data[].businessType | string |  | 还款方式<br><br>`normal`: 正常还款<br><br>`liquidation`: 系统强平还款 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "repayOrderId": "xxxxxxx",
      "businessType": "normal",
      "repayType": "all",
      "repaidTime": "1713645576789",
      "coin": "USDT",
      "repaidAmount": "1",
      "repaidInterest": "1.1"
    }
  ]
}
```