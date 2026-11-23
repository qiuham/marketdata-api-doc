---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/institutional-loan
api_type: REST
updated_at: 2026-11-23 19:02:43.783064
---

# Institutional Loan

Institutional lending (risk unit) APIs — bind UIDs, risk units, LTV, products, orders and repayments.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/ins-loan/bind-uid` — Bind/Unbind UID to Risk Unit
- `GET /api/v3/ins-loan/ensure-coins-convert` — Get Margin Coin Info
- `GET /api/v3/ins-loan/ltv-convert` — Get LTV
- `GET /api/v3/ins-loan/loan-order` — Get Loan Orders
- `GET /api/v3/ins-loan/product-infos` — Get Product Info
- `GET /api/v3/ins-loan/repaid-history` — Get Repayment Orders
- `GET /api/v3/ins-loan/risk-unit` — Get Risk Unit
- `GET /api/v3/ins-loan/symbols` — Get Trade Symbols
- `GET /api/v3/ins-loan/transfered` — Get Transferred Quantity

## Bind/Unbind UID to Risk Unit

`POST /api/v3/ins-loan/bind-uid`

Rate limit: 3/sec/UID

Binding:

- The uid and riskUnitId belong to the same main account.

- The uid is not bound to any other risk unit.

Unbinding:

- The API key used for the call must belong to the main account or the lending-exclusive sub-account UID within the risk unit.

- The uid is within the risk unit and is not equal to riskUnitId.

- The uid has a zero balance, or the riskUnitId has not_paid_off or in_progress loan orders.

The account mode must be set to Multi-Asset Margin Mode; Stablecoin Margin Mode is not supported.

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanBindUid`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| riskUnitId | string |  | Risk Unit ID (Required for parent account calls, not required for risk unit account calls) |
| uid | string | 是 | Sub UID (limit 50 UIDs for one Risk Unit) |
| operate | string | 是 | `bind` Bind <br><br>`unbind` Unbind |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string |  | Risk Unit ID |
| data.uid | string |  | Bind or unbind the UID of the sub-account to the risk unit.<br><br>Bind: the UID and the riskUnitId belong to the same main account; the UID is not bound to other risk units.<br><br>Unbind: the API key for invoking the interface must be the UID of the exclusive sub-account for borrowing and lending within the main account or the risk unit; the UID is within the risk unit and is not equal to the riskUnitId; the assets of the UID are zero, or there are no outstanding or in-transit borrowing and lending orders for the riskUnitId. |
| data.operate | string |  | `bind` Bind <br><br>`unbind` Unbind |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1745725444960,
  "data": {
    "riskUnitId": "12345678",
    "uid": "12345678",
    "operate": "bind"
  }
}
```

## Get Margin Coin Info

`GET /api/v3/ins-loan/ensure-coins-convert`

Rate limit: 3/sec/UID

Get Margin Coin Info

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetMarginCoinInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | Product Id |
| data.coinInfo | object[] |  | Spot margin coin |
| data.coinInfo[].coin | string |  | Margin coin |
| data.coinInfo[].convertRatio | string |  | Margin coin convert ratio |
| data.coinInfo[].maxConvertValue | string |  | Maximum convert value (USDT) |
| data.coinInfo[].convertRatioList | object[] |  | Tiered conversion rate |
| data.coinInfo[].convertRatioList[].ladder | string |  | Ladder |
| data.coinInfo[].convertRatioList[].convertRatio | string |  | Margin coin convert ratio |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697581815,
  "data": {
    "productId": "xxxxxxxx",
    "coinInfo": [
      {
        "coin": "USDC",
        "convertRatio": "1",
        "maxConvertValue": "1000",
        "convertRatioList": [
          {
            "ladder": "0-100000000",
            "convertRatio": "1"
          },
          {
            "ladder": "100000000-200000000",
            "convertRatio": "0.99"
          }
        ]
      },
      {
        "coin": "USDT",
        "convertRatio": "1",
        "maxConvertValue": "1000",
        "convertRatioList": [
          {
            "ladder": "0-100000000",
            "convertRatio": "1"
          },
          {
            "ladder": "100000000-200000000",
            "convertRatio": "0.99"
          }
        ]
      }
    ]
  }
}
```

## Get LTV

`GET /api/v3/ins-loan/ltv-convert`

Rate limit: 3/sec/UID

Get LTV

1. If the riskUnitId parameter is not passed in, the account calling the interface must be an institutional exclusive lending unit account.

2. If this parameter has been provided, the UID carried in the parameter must belong to an institutional lending exclusive unit account, and the account calling the API must be the primary account.

3. Update frequency: 1s

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetLTV`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| riskUnitId | query | string |  | Risk Unit ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.ltv | string |  | Risk rate, 0.6667 |
| data.subAccountUids | string[] |  | Sub-accounts user ID in Risk Unit |
| data.usdtBalance | string |  | Total assets (margin coins converted to USDT) |
| data.unpaidUsdtAmount | string |  | Total debt (converted to USDT) |
| data.unpaidInfo | object[] |  | Debt details |
| data.unpaidInfo[].coin | string |  | Coin |
| data.unpaidInfo[].unpaidQty | string |  | Unpaid principle |
| data.unpaidInfo[].unpaidInterest | string |  | Unpaid interest |
| data.balanceInfo | object[] |  | Asset details |
| data.balanceInfo[].coin | string |  | Margin coin |
| data.balanceInfo[].price | string |  | Margin coin price |
| data.balanceInfo[].amount | string |  | Margin coin equity |
| data.balanceInfo[].convertedUsdtAmount | string |  | Margin conversion amount (converted to USDT) |
| data.delta | string |  | Current risk unit Delta (Hedge only; empty for HFT) |
| data.leverageRatio | string |  | Current position leverage ratio (Hedge only; empty for HFT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "ltv": "0.6667",
    "subAccountUids": [
      "xxxxxxxxxx",
      "xxxxxxxxxx"
    ],
    "unpaidUsdtAmount": "1.12",
    "usdtBalance": "1223",
    "unpaidInfo": [
      {
        "coin": "USDT",
        "unpaidQty": "12",
        "unpaidInterest": "1.2"
      }
    ],
    "balanceInfo": [
      {
        "coin": "USDT",
        "price": "12",
        "amount": "1.2",
        "convertedUsdtAmount": "12"
      }
    ],
    "delta": "0.375",
    "leverageRatio": "1.38"
  }
}
```

## Get Loan Orders

`GET /api/v3/ins-loan/loan-order`

Rate limit: 3/sec/UID

Get Loan Orders

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetLoanOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Loan order id. If not passed, then return all orders, sort by `loanTime` in descend |
| startTime | query | string |  | The start timestamp (ms) |
| endTime | query | string |  | The end timestamp (ms) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Loan details |
| data[].orderId | string |  | Loan order ID |
| data[].orderProductId | string |  | Product Id |
| data[].uid | string |  | The designated UID that is used to bind INS loan product, loan and repayment |
| data[].loanTime | string |  | Loan timestamp, in milliseconds |
| data[].loanCoin | string |  | Loan coin |
| data[].loanAmount | string |  | Loan amount |
| data[].unpaidAmount | string |  | Unpaid principal |
| data[].unpaidInterest | string |  | Unpaid interest |
| data[].repaidAmount | string |  | Repaid principal |
| data[].repaidInterest | string |  | Repaid interest |
| data[].reserve | string |  | Reserve amount |
| data[].status | string |  | Not paid off `not_paid_off`;<br><br>Paid off `paid_off` |

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
      "loanAmount": "8400",
      "unpaidAmount": "8400",
      "unpaidInterest": "0",
      "repaidAmount": "1",
      "repaidInterest": "1.1",
      "reserve": "168",
      "status": "not_paid_off"
    }
  ]
}
```

## Get Product Info

`GET /api/v3/ins-loan/product-infos`

Rate limit: 3/sec/UID

Get Product Info

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetProductInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product Id |
| clientType | query | string |  | Client type: Hedge/HFT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | Product Id |
| data.leverage | string |  | The maximum leverage for this loan product. 2x/4x |
| data.supportUsdtContract | string |  | Whether USDT-M Futures are supported. YES/NO |
| data.supportCoinContract | string |  | Whether Coin-M Futures are supported. YES/NO |
| data.supportUsdcContract | string |  | Whether USDC-M Futures are supported. YES/NO |
| data.transferLine | string |  | Restrict line for transfer, eg: 0.6667 |
| data.spotBuyLine | string |  | Restrict line for Spot buy, eg: 0.8 |
| data.usdtContractOpenLine | string |  | Restrict line for USDT-M Futures open position, eg: 0.8 |
| data.coinContractOpenLine | string |  | Restrict line for Coin-M Futures open position, eg: 0.8 |
| data.usdcContractOpenLine | string |  | Restrict line for USDC-M Futures open position, eg: 0.8 |
| data.liquidationLine | string |  | Line for liquidation, eg: 0.9 |
| data.stopLiquidationLine | string |  | Line for stop liquidation, eg: 0.75 |
| data.deltaThreshold | string |  | Delta exceed threshold (Hedge only), eg: 0.5 |
| data.leverageThreshold | string |  | Position leverage ratio threshold (Hedge only), eg: 5 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697573019,
  "data": {
    "productId": "xxxxxxxx",
    "leverage": "2",
    "supportUsdtContract": "YES",
    "supportCoinContract": "YES",
    "supportUsdcContract": "YES",
    "transferLine": "0.6667",
    "spotBuyLine": "0.8",
    "usdtContractOpenLine": "0.8",
    "coinContractOpenLine": "0.8",
    "usdcContractOpenLine": "0.8",
    "liquidationLine": "0.9",
    "stopLiquidationLine": "0.75",
    "deltaThreshold": "0.5",
    "leverageThreshold": "5"
  }
}
```

## Get Repayment Orders

`GET /api/v3/ins-loan/repaid-history`

Rate limit: 3/sec/UID

Get Repayment Orders

- By default, query the data of the past two years.

- At most, support querying the data of the past two years.

- Only display the data of successfully repaid orders.

- Only display the repayment orders under the unified account. The orders under the spot account can be queried through the v2 version.

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetRepaymentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | The start timestamp (ms) |
| endTime | query | string |  | The end timestamp (ms) |
| limit | query | string |  | Limit default 100; max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Repayment orders |
| data[].repayOrderId | string |  | Repaid order ID |
| data[].repaidTime | string |  | Repaid timestamp (ms) |
| data[].coin | string |  | Repaid coin |
| data[].repayAmount | string |  | Repaid principle |
| data[].repayInterest | string |  | Repaid interest |
| data[].repayType | string |  | Repaid type: `all` All repayment; `part` partial repayment |
| data[].businessType | string |  | Business type: `normal` normal repayment; `liquidation` repaid by liquidation |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "repayOrderId": "xxxxxxx",
      "businessType": "liquidation",
      "repayType": "part",
      "repaidTime": "1745654869294",
      "coin": "USDT",
      "repayAmount": "5092.45423168",
      "repayInterest": "0"
    },
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

## Get Risk Unit

`GET /api/v3/ins-loan/risk-unit`

Rate limit: 3/sec/UID

Get Risk Unit, only the parent account API Key can use this endpoint

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetRiskUnit`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string[] |  | All Risk Unit Ids |
| data.riskUnitList | object[] |  | Risk unit list, each with its client type |
| data.riskUnitList[].unitId | string |  | Risk Unit Id |
| data.riskUnitList[].clientType | string |  | Client type: Hedge/HFT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1745725444960,
  "data": {
    "riskUnitId": [
      "1222222222",
      "1222222223"
    ],
    "riskUnitList": [
      {
        "unitId": "1222222222",
        "clientType": "HFT"
      },
      {
        "unitId": "1222222223",
        "clientType": "Hedge"
      }
    ]
  }
}
```

## Get Trade Symbols

`GET /api/v3/ins-loan/symbols`

Rate limit: 3/sec/UID

Get Trade Symbols

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetTradeSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | Product Id |
| data.spotSymbols | string[] |  | Spot trading pairs |
| data.marginLeverage | string |  | The allowable maximum leverage for Spot margin trading |
| data.usdtContractLeverage | string |  | The allowed default leverage for USDT-M Futures |
| data.coinContractLeverage | string |  | The allowed default leverage for Coin-M Futures |
| data.usdcContractLeverage | string |  | The allowed default leverage for USDC-M Futures |
| data.usdtContractSymbols | object[] |  | USDT-M Futures Object <br><br>If `supportUsdtContract`=`NO`, then it returns "[]" <br><br>If there are whitelist symbols, it returns those whitelist data |
| data.usdtContractSymbols[].symbol | string |  | Symbol name |
| data.usdtContractSymbols[].leverage | string |  | Maximum leverage |
| data.coinContractSymbols | object[] |  | Coin-M Futures Object <br><br>If `supportCoinContract`=`NO`, then it returns "[]" <br><br>If there are whitelist symbols, it returns those whitelist data |
| data.coinContractSymbols[].symbol | string |  | Symbol name |
| data.coinContractSymbols[].leverage | string |  | Maximum leverage |
| data.usdcContractSymbols | object[] |  | USDC-M Futures Object <br><br>If `supportUsdcContract`=`NO`, then it returns "[]" <br><br>If there are whitelist symbols, it returns those whitelist data |
| data.usdcContractSymbols[].symbol | string |  | Symbol name |
| data.usdcContractSymbols[].leverage | string |  | Maximum leverage |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "productId": "xxxxxxxx",
    "spotSymbols": [
      "USDCUSDT",
      "BTCUSDT",
      "ETHUSDT",
      "BGBUSDT"
    ],
    "marginLeverage": "",
    "usdtContractLeverage": "3",
    "coinContractLeverage": "3",
    "usdcContractLeverage": "3",
    "usdtContractSymbols": [
      {
        "symbol": "BTCUSDT",
        "leverage": "15"
      },
      {
        "symbol": "ETHUSDT",
        "leverage": "5"
      }
    ],
    "coinContractSymbols": [],
    "usdcContractSymbols": [
      {
        "symbol": "BTCUSD",
        "leverage": "5"
      }
    ]
  }
}
```

## Get Transferred Quantity

`GET /api/v3/ins-loan/transfered`

Rate limit: 3/sec/UID

Get Amount Transferable Out of the Risk Unit

- Rate limit: 3/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `institutionalLoanGetTransferredQuantity`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| userId | query | string |  | User Id (Master account or sub-accounts) |
| coin | query | string | 是 | Coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin name |
| data.transfered | string |  | Transferred quantity |
| data.userId | string |  | User Id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "coin": "USDT",
    "transfered": "1223",
    "userId": "xxxxxxxxxx"
  }
}
```


---

机构借贷（风险单元）接口 — UID 绑定、风险单元、风险率、产品、借贷订单与还款。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/ins-loan/bind-uid` — 绑定/解绑UID
- `GET /api/v3/ins-loan/ensure-coins-convert` — 查询保证金币种信息
- `GET /api/v3/ins-loan/ltv-convert` — 查询风险率
- `GET /api/v3/ins-loan/loan-order` — 查询借贷订单信息
- `GET /api/v3/ins-loan/product-infos` — 查询产品信息
- `GET /api/v3/ins-loan/repaid-history` — 查询还款订单信息
- `GET /api/v3/ins-loan/risk-unit` — 查询风险单元
- `GET /api/v3/ins-loan/symbols` — 查询支持交易对信息
- `GET /api/v3/ins-loan/transfered` — 查询可划出金额

## 绑定/解绑UID

`POST /api/v3/ins-loan/bind-uid`

限频规则: 3次/秒/UID

对于机构借贷产品，您可以自行绑定新的子账户UID到风险单元内或者解绑某个UID

注意：

- 风险单元的主UID，即借贷专属子账户不支持解绑

- 每个风险单元 50个子账户数量限制

1. riskUnitId 校验

- 必须是借贷专属子账户

- 必须和调用接口的API key 账户有母子关系

2. uid 校验：

- 若riskUnitId填写：

  - 绑定：uid 和riskUnitId 都为调用接口的API key的账户的子账户；uid 未绑定到其他风险单元

  - 解绑：uid 和riskUnitId 都为调用接口的API key的账户的子账户；uid 在 riskUnitId 风险单元内；uid 资产为零 或 riskUnitId 无未结清或在途的借贷订单

- 若riskUnitId不填写：

  - 绑定：调用接口的API key的账户为借贷专属子账户；uid 未绑定到其他风险单元

  - 解绑：调用接口的API key的账户为借贷专属子账户；uid 在 riskUnitId 风险单元内；uid 资产为零 或 riskUnitId 无未结清或在途的借贷订单

3. 绑定到风险单元的子账户UID 打标签：机构借贷子账户，风险单元 50个子账户数量限制，50个后端可配置

4. 从风险单元解绑的子账户UID的机构借贷子账户标签删除，和风险单元的关联关系删除

5. 账户模式必须为多币种保证金模式，不支持稳定币保证金模式

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanBindUid`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| riskUnitId | string |  | 风险单元ID，即借贷专属子账户UID |
| uid | string | 是 | 绑定或解绑到风险单元的子账户UID |
| operate | string | 是 | bind 绑定 <br><br>unbind 解绑 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string |  | 风险单元ID，即借贷专属子账户UID |
| data.uid | string |  | 绑定或解绑到风险单元的子账户UID<br><br>绑定：uid 和riskUnitId 同归属一个主账户；uid 未绑定到其他风险单元；<br><br>解绑：调用接口的API key必须为主账户或风险单元内借贷专属子账户UID；uid 在风险单元内且不等于riskUnitId；uid 资产为零 或 riskUnitId 无未结清或在途的借贷订单 |
| data.operate | string |  | bind 绑定 <br><br>unbind 解绑 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1745725444960,
  "data": {
    "riskUnitId": "12345678",
    "uid": "12345678",
    "operate": "bind"
  }
}
```

## 查询保证金币种信息

`GET /api/v3/ins-loan/ensure-coins-convert`

限频规则: 3次/秒/UID

查询保证金币种信息

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetMarginCoinInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID，保证唯一性 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.coinInfo | object[] |  | 保证金币种信息 |
| data.coinInfo[].coin | string |  | 保证金币种 |
| data.coinInfo[].convertRatio | string |  | 保证金折算率 |
| data.coinInfo[].maxConvertValue | string |  | 最大折算金额（USDT） |
| data.coinInfo[].convertRatioList | object[] |  | 阶梯折算率 |
| data.coinInfo[].convertRatioList[].ladder | string |  | 阶梯上下限 |
| data.coinInfo[].convertRatioList[].convertRatio | string |  | 折算率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697581815,
  "data": {
    "productId": "xxxxxxxx",
    "coinInfo": [
      {
        "coin": "USDC",
        "convertRatio": "1",
        "maxConvertValue": "1000",
        "convertRatioList": [
          {
            "ladder": "0-100000000",
            "convertRatio": "1"
          },
          {
            "ladder": "100000000-200000000",
            "convertRatio": "0.99"
          }
        ]
      },
      {
        "coin": "USDT",
        "convertRatio": "1",
        "maxConvertValue": "1000",
        "convertRatioList": [
          {
            "ladder": "0-100000000",
            "convertRatio": "1"
          },
          {
            "ladder": "100000000-200000000",
            "convertRatio": "0.99"
          }
        ]
      }
    ]
  }
}
```

## 查询风险率

`GET /api/v3/ins-loan/ltv-convert`

限频规则: 3次/秒/UID

查询风险率

1. 若未传入 riskUnitId 参数，则调用接口的账号须为机构借贷专属单元账号。

2. 若已传入该参数，则参数中所携带的 UID 必须属于机构借贷专属单元账号，且调用接口的账号须为主账户。

3. 更新频率：1s

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetLTV`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| riskUnitId | query | string |  | 风险单元内，借贷专属子账户UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.ltv | string |  | 风险率, 0.6667 |
| data.subAccountUids | string[] |  | 绑定机构借贷产品的风险单元的子账号UID，包括借贷专属子账户 |
| data.usdtBalance | string |  | 总资产(保证金币种资产折算为USDT资产)，小数点后8位，截位取值 |
| data.unpaidUsdtAmount | string |  | 总负债 (USDT) |
| data.unpaidInfo | object[] |  | 负债明细 |
| data.unpaidInfo[].coin | string |  | 币种 |
| data.unpaidInfo[].unpaidQty | string |  | 未还本金，小数点后8位，截位取值 |
| data.unpaidInfo[].unpaidInterest | string |  | 未还利息，小数点后8位，截位取值 |
| data.balanceInfo | object[] |  | 资产明细 |
| data.balanceInfo[].coin | string |  | 保证金币种 |
| data.balanceInfo[].price | string |  | 保证金币种价格 |
| data.balanceInfo[].amount | string |  | 保证金权益，小数点后8位，截位取值 |
| data.balanceInfo[].convertedUsdtAmount | string |  | 保证金折算金额(USDT)小数点后8位，截位取值 |
| data.delta | string |  | 当前风险单元 Delta 值（仅 Hedge 用户返回值；HFT 用户返回空） |
| data.leverageRatio | string |  | 当前仓位杠杆倍数（仅 Hedge 用户返回值；HFT 用户返回空） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "ltv": "0.6667",
    "subAccountUids": [
      "xxxxxxxxxx",
      "xxxxxxxxxx"
    ],
    "unpaidUsdtAmount": "1.12",
    "usdtBalance": "1223",
    "unpaidInfo": [
      {
        "coin": "USDT",
        "unpaidQty": "12",
        "unpaidInterest": "1.2"
      }
    ],
    "balanceInfo": [
      {
        "coin": "USDT",
        "price": "12",
        "amount": "1.2",
        "convertedUsdtAmount": "12"
      }
    ],
    "delta": "0.375",
    "leverageRatio": "1.38"
  }
}
```

## 查询借贷订单信息

`GET /api/v3/ins-loan/loan-order`

限频规则: 3次/秒/UID

查询借贷订单信息

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetLoanOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 借贷订单ID。若不传，则返回全部。按照loanTime降序排列 |
| startTime | query | string |  | 开始时间戳 (毫秒) |
| endTime | query | string |  | 结束时间戳 (毫秒) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 借贷详情 |
| data[].orderId | string |  | 借贷订单ID |
| data[].orderProductId | string |  | 产品ID |
| data[].uid | string |  | 机构借贷放款和还款UID |
| data[].loanTime | string |  | 放款时间戳（毫秒） |
| data[].loanCoin | string |  | 借款币种 |
| data[].loanAmount | string |  | 借款金额 |
| data[].unpaidAmount | string |  | 未还本金 |
| data[].unpaidInterest | string |  | 未还利息 |
| data[].repaidAmount | string |  | 已还本金 |
| data[].repaidInterest | string |  | 已还利息 |
| data[].reserve | string |  | 备付金 |
| data[].status | string |  | 未还清 `not_paid_off`；<br><br>已还清 `paid_off` |

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
      "loanAmount": "8400",
      "unpaidAmount": "8400",
      "unpaidInterest": "0",
      "repaidAmount": "1",
      "repaidInterest": "1.1",
      "reserve": "168",
      "status": "not_paid_off"
    }
  ]
}
```

## 查询产品信息

`GET /api/v3/ins-loan/product-infos`

限频规则: 3次/秒/UID

查询产品信息

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetProductInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID，保证唯一性 |
| clientType | query | string |  | 客户类型：Hedge / HFT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.leverage | string |  | 该借贷产品的最大杠杆倍数，2 或 4 |
| data.supportUsdtContract | string |  | 是否支持U本位合约交易：YES 是；NO 否 |
| data.supportCoinContract | string |  | 是否支持币本位合约交易：YES 是；NO 否 |
| data.supportUsdcContract | string |  | 是否支持USDC合约交易：YES 是；NO 否 |
| data.transferLine | string |  | 限制划转线，举例：0.6667 |
| data.spotBuyLine | string |  | 限制现货买入线，举例：0.8 |
| data.usdtContractOpenLine | string |  | 限制U本位合约开仓线，举例：0.8 |
| data.coinContractOpenLine | string |  | 限制币本位合约开仓线，举例：0.8 |
| data.usdcContractOpenLine | string |  | 限制USDC合约开仓线，举例：0.8 |
| data.liquidationLine | string |  | 强平还款线，举例：0.9 |
| data.stopLiquidationLine | string |  | 停止强平线，举例：0.75 |
| data.deltaThreshold | string |  | Delta 超限阈值（仅 Hedge 用户），举例：0.5 |
| data.leverageThreshold | string |  | 仓位杠杆倍数阈值（仅 Hedge 用户），举例：5 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697573019,
  "data": {
    "productId": "xxxxxxxx",
    "leverage": "2",
    "supportUsdtContract": "YES",
    "supportCoinContract": "YES",
    "supportUsdcContract": "YES",
    "transferLine": "0.6667",
    "spotBuyLine": "0.8",
    "usdtContractOpenLine": "0.8",
    "coinContractOpenLine": "0.8",
    "usdcContractOpenLine": "0.8",
    "liquidationLine": "0.9",
    "stopLiquidationLine": "0.75",
    "deltaThreshold": "0.5",
    "leverageThreshold": "5"
  }
}
```

## 查询还款订单信息

`GET /api/v3/ins-loan/repaid-history`

限频规则: 3次/秒/UID

查询还款订单信息

- 默认查询过去2年的数据

- 最多支持查询过去2年的数据

- 仅展示还款成功的订单数据

- 仅展示统一账户下还款订单，现货账户下订单通过v2版本查询

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetRepaymentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳 (毫秒) |
| endTime | query | string |  | 结束时间戳 (毫秒) |
| limit | query | string |  | 返回数量限制。[1, 100], 默认: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 还款订单列表 |
| data[].repayOrderId | string |  | 还款订单号 |
| data[].repaidTime | string |  | 还款时间（毫秒） |
| data[].coin | string |  | 还款币种 |
| data[].repayAmount | string |  | 还款本金 |
| data[].repayInterest | string |  | 还款利息 |
| data[].repayType | string |  | 还款类型：<br><br>`all`: 全部还款<br><br>`part`: 部分还款 |
| data[].businessType | string |  | 还款方式: <br><br>`normal`: 正常还款<br><br>`liquidation`: 系统强平还款 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": [
    {
      "repayOrderId": "xxxxxxx",
      "businessType": "liquidation",
      "repayType": "part",
      "repaidTime": "1745654869294",
      "coin": "USDT",
      "repayAmount": "5092.45423168",
      "repayInterest": "0"
    },
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

## 查询风险单元

`GET /api/v3/ins-loan/risk-unit`

限频规则: 3次/秒/UID

查询风险单元，只能借贷主账户创建的API KEY调用

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetRiskUnit`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string[] |  | 所有风险单元 ID，即所有风险单元内借贷专属子账户UID |
| data.riskUnitList | object[] |  | 风险单元列表，携带各自对应的客户类型 |
| data.riskUnitList[].unitId | string |  | 风险单元 ID |
| data.riskUnitList[].clientType | string |  | 客户类型：Hedge / HFT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1745725444960,
  "data": {
    "riskUnitId": [
      "1222222222",
      "1222222223"
    ],
    "riskUnitList": [
      {
        "unitId": "1222222222",
        "clientType": "HFT"
      },
      {
        "unitId": "1222222223",
        "clientType": "Hedge"
      }
    ]
  }
}
```

## 查询支持交易对信息

`GET /api/v3/ins-loan/symbols`

限频规则: 3次/秒/UID

查询支持交易对信息

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetTradeSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID，保证唯一性 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.spotSymbols | string[] |  | 该现货交易对列表 |
| data.marginLeverage | string |  | 现货杠杆允许可借的最大杠杆 |
| data.usdtContractLeverage | string |  | U本位合约默认最大开仓杠杆 |
| data.coinContractLeverage | string |  | 币本位合约默认最大开仓杠杆 |
| data.usdcContractLeverage | string |  | USDC合约默认最大开仓杠杆 |
| data.usdtContractSymbols | object[] |  | U本位合约交易对列表<br><br>若`supportUsdtContract`为`NO`，则返回"[]"<br><br>若有白名单交易对，则返回白名单数据 |
| data.usdtContractSymbols[].symbol | string |  | 合约名称 |
| data.usdtContractSymbols[].leverage | string |  | 最大开仓杠杆 |
| data.coinContractSymbols | object[] |  | 币本位合约交易对列表<br><br>若`supportCoinContract`为`NO`，则返回"[]"<br><br>若有白名单交易对，则返回白名单数据 |
| data.coinContractSymbols[].symbol | string |  | 合约名称 |
| data.coinContractSymbols[].leverage | string |  | 最大开仓杠杆 |
| data.usdcContractSymbols | object[] |  | USDC合约交易对列表<br><br>若`supportUsdcContract`为`NO`，则返回"[]"<br><br>若有白名单交易对，则返回白名单数据 |
| data.usdcContractSymbols[].symbol | string |  | 合约名称 |
| data.usdcContractSymbols[].leverage | string |  | 最大开仓杠杆 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "productId": "xxxxxxxx",
    "spotSymbols": [
      "USDCUSDT",
      "BTCUSDT",
      "ETHUSDT",
      "BGBUSDT"
    ],
    "marginLeverage": "",
    "usdtContractLeverage": "3",
    "coinContractLeverage": "3",
    "usdcContractLeverage": "3",
    "usdtContractSymbols": [
      {
        "symbol": "BTCUSDT",
        "leverage": "15"
      },
      {
        "symbol": "ETHUSDT",
        "leverage": "5"
      }
    ],
    "coinContractSymbols": [],
    "usdcContractSymbols": [
      {
        "symbol": "BTCUSD",
        "leverage": "5"
      }
    ]
  }
}
```

## 查询可划出金额

`GET /api/v3/ins-loan/transfered`

限频规则: 3次/秒/UID

查询可划转出风险单元外的金额

- 限频规则: 3次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `institutionalLoanGetTransferredQuantity`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| userId | query | string |  | 用户ID (Master account or sub-accounts) |
| coin | query | string | 是 | 币种名称, 如USDT<br><br>该字段用于单币种持仓查询 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.transfered | string |  | 可划出资产数量 |
| data.userId | string |  | 用户ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "coin": "USDT",
    "transfered": "1223",
    "userId": "xxxxxxxxxx"
  }
}
```