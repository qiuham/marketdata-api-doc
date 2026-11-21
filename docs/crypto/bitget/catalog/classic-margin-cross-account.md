---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-cross-account
api_type: REST
updated_at: 2026-11-21 19:03:59.585982
---

# Classic Cross Margin Account API

Classic account — cross margin borrow/repay & assets.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/crossed/account/assets` — Get Cross Account Assets
- `POST /api/v2/margin/crossed/account/borrow` — Cross Borrow
- `POST /api/v2/margin/crossed/account/repay` — Cross Repay
- `GET /api/v2/margin/crossed/account/risk-rate` — Get Cross Risk Rate
- `GET /api/v2/margin/crossed/account/max-borrowable-amount` — Get Cross Max Borrowable
- `GET /api/v2/margin/crossed/account/max-transfer-out-amount` — Get Cross Max Transferable
- `GET /api/v2/margin/crossed/interest-rate-and-limit` — Get Cross Interest Rate and Max Borrowable
- `GET /api/v2/margin/crossed/tier-data` — Get Cross Tier Configuration
- `POST /api/v2/margin/crossed/account/flash-repay` — Cross Flash Repay
- `POST /api/v2/margin/crossed/account/query-flash-repay-status` — Get Cross Flash Repay Result

## Get Cross Account Assets

`GET /api/v2/margin/crossed/account/assets`

Frequency limit: 10 times/1s (UID)

Getting account asset

Operation ID: `classicMarginCrossAccountGetCrossAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin, like USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].totalAmount | string |  | Total amount |
| data[].available | string |  | Available amount |
| data[].frozen | string |  | Assets frozen |
| data[].borrow | string |  | Borrow |
| data[].interest | string |  | Interest, Interest-only payments with a minimum payment of interest. |
| data[].net | string |  | Net assets = available + frozen &minus; borrow &minus; interest. Liquidation is triggered when the Maintenance Margin Ratio (MMR) is reached. |
| data[].coupon | string |  | Trading bonus |
| data[].cTime | string |  | Creation time |
| data[].uTime | string |  | Update time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": [
    {
      "coin": "USDT",
      "totalAmount": "12",
      "available": "2",
      "frozen": "0",
      "borrow": "0.1",
      "interest": "0.000001",
      "net": "0.1",
      "cTime": "1734567744432",
      "uTime": "1734567744432",
      "coupon": "0"
    }
  ]
}
```

## Cross Borrow

`POST /api/v2/margin/crossed/account/borrow`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginCrossAccountCrossBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Borrowing coin |
| borrowAmount | string | 是 | Borrowing amount (up to 8 decimal places) |
| clientOid | string |  | Client customized ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.loanId | string |  | Loan order ID |
| data.coin | string |  | Borrowing coin |
| data.borrowAmount | string |  | Borrowing amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": {
    "loanId": "2342332432",
    "coin": "USDT",
    "borrowAmount": "1.00000000"
  }
}
```

## Cross Repay

`POST /api/v2/margin/crossed/account/repay`

Frequency limit: 10 times/1s (UID)

Repay

Operation ID: `classicMarginCrossAccountCrossRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Repayment coin |
| repayAmount | string | 是 | Number of repayments (up to 8 decimal places) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.remainDebtAmount | string |  | Remaining borrowings |
| data.repayId | string |  | repay ID |
| data.coin | string |  | Coin |
| data.repayAmount | string |  | Repayment amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "repayId": "12313123213",
    "remainDebtAmount": "0.2",
    "repayAmount": "0.1"
  }
}
```

## Get Cross Risk Rate

`GET /api/v2/margin/crossed/account/risk-rate`

Frequency limit: 10 times/1s (UID)

Get cross risk rate

Operation ID: `classicMarginCrossAccountGetCrossRiskRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskRateRatio | string |  | Risk ratio (total assets/total liabilities under cross mode) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "riskRateRatio": "0"
  }
}
```

## Get Cross Max Borrowable

`GET /api/v2/margin/crossed/account/max-borrowable-amount`

Frequency limit: 10 times/1s (UID)

Get max borrowable

Operation ID: `classicMarginCrossAccountCrossMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Borrowing coins, such as BTC |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxBorrowableAmount | string |  | Maximum borrow amount (amount changes in real time) |
| data.coin | string |  | Coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "maxBorrowableAmount": "3976070.21616"
  }
}
```

## Get Cross Max Transferable

`GET /api/v2/margin/crossed/account/max-transfer-out-amount`

Frequency limit: 10 times/1s (UID)

Get max transferable

Operation ID: `classicMarginCrossAccountGetCrossMaxTransferOutAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Token name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin |
| data.maxTransferOutAmount | string |  | Maximum transferable amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "maxTransferOutAmount": "11"
  }
}
```

## Get Cross Interest Rate and Max Borrowable

`GET /api/v2/margin/crossed/interest-rate-and-limit`

Frequency limit:10 times/1s (IP)

This interface will determine the user's VIP level based on the User ID sending the request, and then return information such as interest rates and limits based on the VIP level.

Operation ID: `classicMarginCrossAccountGetCrossMarginInterestRateAndBorrowable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Trading pairs, like BTC,  ETH |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coins, such as BTC, ETH |
| data[].leverage | string |  | Leverage <br><br>The default value is 3, and it has three tiers: 3, 5, and 10. |
| data[].transferable | boolean |  | Transfer supported?<br><br>true: Transferable<br><br>false: Not transferable |
| data[].borrowable | boolean |  | Borrowable or not?<br><br>true: Borrowable<br><br>false: Not borrowable |
| data[].dailyInterestRate | string |  | Non-VIP daily interest rate |
| data[].annualInterestRate | string |  | Non-VIP APR |
| data[].maxBorrowableAmount | string |  | Maximum borrow |
| data[].vipList | object[] |  | VIP level |
| data[].vipList[].level | string |  | VIP level |
| data[].vipList[].limit | string |  | VIP limit |
| data[].vipList[].dailyInterestRate | string |  | VIP daily interest rate |
| data[].vipList[].annualInterestRate | string |  | VIP APR |
| data[].vipList[].discountRate | string |  | VIP discount: 1 is for 100%, i.e. no discount; 0.97 is for 97% of the original rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695167748916,
  "data": [
    {
      "transferable": true,
      "leverage": "3",
      "coin": "ETH",
      "borrowable": true,
      "dailyInterestRate": "0.0005",
      "annualInterestRate": "0.05",
      "maxBorrowableAmount": "100000",
      "vipList": [
        {
          "level": "0",
          "limit": "1000",
          "dailyInterestRate": "0.00001",
          "annualInterestRate": "0.01",
          "discountRate": "1"
        }
      ]
    }
  ]
}
```

## Get Cross Tier Configuration

`GET /api/v2/margin/crossed/tier-data`

Frequency limit:10 times/1s (IP)

This interface will determine the user's VIP level based on the User ID sending the request, and then return the tier information based on the VIP level.

Operation ID: `classicMarginCrossAccountCrossTierData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].tier | string |  | Tier |
| data[].leverage | string |  | Effective leverage, global default: 3x |
| data[].coin | string |  | Coin |
| data[].maxBorrowableAmount | string |  | Maximum borrow |
| data[].maintainMarginRate | string |  | Maintenance margin rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695167748916,
  "data": [
    {
      "tier": "1",
      "leverage": "3",
      "coin": "ETH",
      "maxBorrowableAmount": "6",
      "maintainMarginRate": "0.05"
    }
  ]
}
```

## Cross Flash Repay

`POST /api/v2/margin/crossed/account/flash-repay`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginCrossAccountCrossFlashRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string |  | Repayment coin for the cross margin<br><br>If you don't fill it, then cross margin account will be fully repaid. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.repayId | string |  | Repayment id |
| data.coin | string |  | Repayment coin. In case of full repayment, the coin will be returned with no residual value. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695619576187,
  "data": {
    "repayId": "3423423",
    "coin": "ETH"
  }
}
```

## Get Cross Flash Repay Result

`POST /api/v2/margin/crossed/account/query-flash-repay-status`

Frequency limit: 10 times/1s (UID)

Operation ID: `classicMarginCrossAccountQueryCrossFlashRepayStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| idList | string[] | 是 | Set of ids for close position requests (Max. 100 ids) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | Repayment ID |
| data[].status | string |  | Repayment result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": [
    {
      "repayId": "2342332432",
      "status": "FINISH"
    }
  ]
}
```


---

经典账户 — 全仓杠杆借币还币与资产。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/margin/crossed/account/assets` — 获取全仓杠杆账户资产
- `POST /api/v2/margin/crossed/account/borrow` — 全仓借款
- `POST /api/v2/margin/crossed/account/repay` — 全仓还款
- `GET /api/v2/margin/crossed/account/risk-rate` — 全仓风险率
- `GET /api/v2/margin/crossed/account/max-borrowable-amount` — 全仓最大可借数量
- `GET /api/v2/margin/crossed/account/max-transfer-out-amount` — 全仓最大可转出数量
- `GET /api/v2/margin/crossed/interest-rate-and-limit` — 全仓利率与最大可借数量配置
- `GET /api/v2/margin/crossed/tier-data` — 全仓档位梯度配置
- `POST /api/v2/margin/crossed/account/flash-repay` — 全仓一键还款
- `POST /api/v2/margin/crossed/account/query-flash-repay-status` — 获取全仓还款结果

## 获取全仓杠杆账户资产

`GET /api/v2/margin/crossed/account/assets`

限速规则 10次/1s (IP)

获取账户资产

Operation ID: `classicMarginCrossAccountGetCrossAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种，如USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].totalAmount | string |  | 总金额 |
| data[].available | string |  | 可用金额 |
| data[].frozen | string |  | 冻结资产 |
| data[].borrow | string |  | 借款 |
| data[].interest | string |  | 利息，还款时先息后本，最小还款为利息 |
| data[].net | string |  | 净资产 = available + frozen - borrow - interest, 到了mmr(维持保证金率)就爆仓 |
| data[].coupon | string |  | 体验金 |
| data[].cTime | string |  | 创建时间 |
| data[].uTime | string |  | 更新时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": [
    {
      "coin": "USDT",
      "totalAmount": "12",
      "available": "2",
      "frozen": "0",
      "borrow": "0.1",
      "interest": "0.000001",
      "net": "0.1",
      "cTime": "1734567744432",
      "uTime": "1734567744432",
      "coupon": "0"
    }
  ]
}
```

## 全仓借款

`POST /api/v2/margin/crossed/account/borrow`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountCrossBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 借出币种 |
| borrowAmount | string | 是 | 借出数量（最长8位小数） |
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

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": {
    "loanId": "1",
    "coin": "USDT",
    "borrowAmount": "1.00000000"
  }
}
```

## 全仓还款

`POST /api/v2/margin/crossed/account/repay`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountCrossRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 还款币种 |
| repayAmount | string | 是 | 还款数量 （最长为8位小数） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.remainDebtAmount | string |  | 剩余欠款 |
| data.repayId | string |  | 还款ID |
| data.coin | string |  | 币种 |
| data.repayAmount | string |  | 还款金额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "repayId": "12313123213",
    "remainDebtAmount": "0.2",
    "repayAmount": "0.1"
  }
}
```

## 全仓风险率

`GET /api/v2/margin/crossed/account/risk-rate`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountGetCrossRiskRate`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskRateRatio | string |  | 风险率 （全仓总资产/全仓总负债） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "riskRateRatio": "0"
  }
}
```

## 全仓最大可借数量

`GET /api/v2/margin/crossed/account/max-borrowable-amount`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountCrossMaxBorrowableAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 借出币种，如BTC |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxBorrowableAmount | string |  | 最大可借数量 （数值会实时变化） |
| data.coin | string |  | 币种 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "maxBorrowableAmount": "3976070.21616"
  }
}
```

## 全仓最大可转出数量

`GET /api/v2/margin/crossed/account/max-transfer-out-amount`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountGetCrossMaxTransferOutAmount`

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
| data.coin | string |  | 币种 |
| data.maxTransferOutAmount | string |  | 最大可转出数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636742119,
  "data": {
    "coin": "USDT",
    "maxTransferOutAmount": "11"
  }
}
```

## 全仓利率与最大可借数量配置

`GET /api/v2/margin/crossed/interest-rate-and-limit`

限速规则 10次/1s (IP)

该接口会根据请求的UID判断用户VIP等级，再根据VIP等级返回利率、限额等信息

Operation ID: `classicMarginCrossAccountGetCrossMarginInterestRateAndBorrowable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种，如BTC,ETH |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种，如BTC、ETH |
| data[].leverage | string |  | 杠杆倍数 <br><br>默认值为3，包含三个档位3、5、10. |
| data[].transferable | boolean |  | 是否可转入<br><br>true 可转入<br><br>false 不可转入 |
| data[].borrowable | boolean |  | 是否可借<br><br>true 可借<br><br>false 不可借 |
| data[].dailyInterestRate | string |  | 非VIP的日利率 |
| data[].annualInterestRate | string |  | 非VIP的年利率 |
| data[].maxBorrowableAmount | string |  | 最大可借 |
| data[].vipList | object[] |  | vip 等级对象 |
| data[].vipList[].level | string |  | VIP 等级 |
| data[].vipList[].limit | string |  | VIP 限额 |
| data[].vipList[].dailyInterestRate | string |  | VIP 日利率 |
| data[].vipList[].annualInterestRate | string |  | VIP 年利率 |
| data[].vipList[].discountRate | string |  | VIP 折扣，1代表100%，即无折扣；0.97代表折后利率为原利率的97% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695167759584,
  "data": [
    {
      "coin": "ETH",
      "leverage": "3",
      "transferable": true,
      "borrowable": true,
      "dailyInterestRate": "0.1",
      "annualInterestRate": "36.5",
      "maxBorrowableAmount": "6",
      "vipList": [
        {
          "level": "0",
          "limit": "",
          "dailyInterestRate": "0.1",
          "annualInterestRate": "36.5",
          "discountRate": "1"
        },
        {
          "level": "1",
          "limit": "",
          "dailyInterestRate": "0.098",
          "annualInterestRate": "35.77",
          "discountRate": "0.98"
        },
        {
          "level": "2",
          "limit": "",
          "dailyInterestRate": "0.093",
          "annualInterestRate": "33.945",
          "discountRate": "0.93"
        },
        {
          "level": "3",
          "limit": "",
          "dailyInterestRate": "0.089",
          "annualInterestRate": "32.485",
          "discountRate": "0.89"
        },
        {
          "level": "4",
          "limit": "",
          "dailyInterestRate": "0.076",
          "annualInterestRate": "27.74",
          "discountRate": "0.76"
        },
        {
          "level": "5",
          "limit": "",
          "dailyInterestRate": "0.067",
          "annualInterestRate": "24.455",
          "discountRate": "0.67"
        }
      ]
    }
  ]
}
```

## 全仓档位梯度配置

`GET /api/v2/margin/crossed/tier-data`

限速规则 10次/1s (IP)

该接口需要根据请求的UID判断用户VIP等级，再根据VIP等级返回档位梯度信息

Operation ID: `classicMarginCrossAccountCrossTierData`

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
| data | object[] |  |  |
| data[].tier | string |  | 档位 |
| data[].leverage | string |  | 有效杠杆倍数，全局默认3倍 |
| data[].coin | string |  | 币种 |
| data[].maxBorrowableAmount | string |  | 最大可借 |
| data[].maintainMarginRate | string |  | 维持保证金率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695167748916,
  "data": [
    {
      "tier": "1",
      "leverage": "3",
      "coin": "ETH",
      "maxBorrowableAmount": "6",
      "maintainMarginRate": "0.05"
    }
  ]
}
```

## 全仓一键还款

`POST /api/v2/margin/crossed/account/flash-repay`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountCrossFlashRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string |  | 全仓还款币种<br><br>不传则是全仓所有币种全部还款 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.repayId | string |  | 还款id |
| data.coin | string |  | 还款币种，如果是还全部，则coin没有值返回 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695619576187,
  "data": {
    "repayId": "3423423",
    "coin": "ETH"
  }
}
```

## 获取全仓还款结果

`POST /api/v2/margin/crossed/account/query-flash-repay-status`

限速规则 10次/1s (IP)

Operation ID: `classicMarginCrossAccountQueryCrossFlashRepayStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| idList | string[] | 是 | 发起平仓单请求id集合(最大100个id) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].repayId | string |  | 还款ID |
| data[].status | string |  | 还款结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679384491703,
  "data": [
    {
      "repayId": "1",
      "status": "FINISH"
    }
  ]
}
```