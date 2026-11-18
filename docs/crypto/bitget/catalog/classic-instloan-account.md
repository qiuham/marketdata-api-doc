---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-instloan-account
api_type: REST
updated_at: 2026-11-18 08:37:51.527642
---

# Classic Inst Loan Account API

Classic account — institutional loan risk unit, LTV and transferred amount.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/ltv-convert` — Get LTV
- `POST /api/v2/spot/ins-loan/bind-uid` — Bind/Unbind Sub-account UID to Risk Unit
- `GET /api/v2/spot/ins-loan/risk-unit` — Get Risk Unit
- `GET /api/v2/spot/ins-loan/transfered` — Get transferable amount

## Get LTV

`GET /api/v2/spot/ins-loan/ltv-convert`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanAccountGetLTV`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| riskUnitId | query | string |  | Risk Sub-unit ID (Required for parent account calls, not required for risk sub-unit account calls) |

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
| data.unpaidInfo[].coin | string |  | coin |
| data.unpaidInfo[].unpaidQty | string |  | Unpaid principle |
| data.unpaidInfo[].unpaidInterest | string |  | Unpaid interest |
| data.balanceInfo | object[] |  | Asset details |
| data.balanceInfo[].coin | string |  | Margin coin |
| data.balanceInfo[].price | string |  | Margin coin price |
| data.balanceInfo[].amount | string |  | Margin coin amount |
| data.balanceInfo[].convertedUsdtAmount | string |  | Margin conversion amount (converted to USDT) |

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
    ]
  }
}
```

## Bind/Unbind Sub-account UID to Risk Unit

`POST /api/v2/spot/ins-loan/bind-uid`

Rate limit: 5 req/sec/UID

Here’s the English translation of the provided text:

*Binding:**

The `uid` and `riskUnitId` belong to the same main account.

The `uid` is not bound to any other risk unit.

*Unbinding:**

The API key used for the call must belong to the main account or a lending-exclusive sub-account UID within the risk unit.

The `uid` is within the risk unit and is not equal to `riskUnitId`.

The `uid` has a zero balance, or the `riskUnitId` has no outstanding or in-progress loan orders.

Operation ID: `classicInstloanAccountBindRiskUnit`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| riskUnitId | string |  | Risk Unit ID (Required for parent account calls, not required for risk unit account calls) |
| uid | string | 是 | Sub UID（limit 50 UIDS for one Risk Unit） |
| operate | string | 是 | `bind` Bind <br><br> `unbind` Unbind |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>"00000": success<br><br>others: fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": "success"
}
```

## Get Risk Unit

`GET /api/v2/spot/ins-loan/risk-unit`

Rate limit: 5 req/sec/UID

Only the parent account API Key can use this endpoint

Operation ID: `classicInstloanAccountGetRiskUnit`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string[] |  | Risk Unit IDs |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "riskUnitId": [
      "xxxxxxxx",
      "xxxxxxxx"
    ]
  }
}
```

## Get transferable amount

`GET /api/v2/spot/ins-loan/transfered`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanAccountGetTransferredAmountFromSpotAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| userId | query | string |  | User Id (Master account or sub-accounts) |
| coin | query | string | 是 | Coin name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin name |
| data.transfered | string |  | Transferred amount |
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

经典账户 — 机构借贷风险单元、LTV 与划转金额。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/ltv-convert` — 查询风险率
- `POST /api/v2/spot/ins-loan/bind-uid` — 绑定/解绑子账户UID至风险单元
- `GET /api/v2/spot/ins-loan/risk-unit` — 获取风险单元
- `GET /api/v2/spot/ins-loan/transfered` — 查询现货账户可转出金额

## 查询风险率

`GET /api/v2/spot/ins-loan/ltv-convert`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanAccountGetLTV`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| riskUnitId | query | string |  | 风险单元ID (母账户调用需要传，风险子单元账户调用不需要传) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.ltv | string |  | 风险率，0.6667 |
| data.subAccountUids | string[] |  | 绑定机构借贷产品的风控单元的子账号UID |
| data.usdtBalance | string |  | 总资产(保证金币种资产折算为USDT资产) |
| data.unpaidUsdtAmount | string |  | 总负债 (USDT) |
| data.unpaidInfo | object[] |  | 负债明细 |
| data.unpaidInfo[].coin | string |  | 币种 |
| data.unpaidInfo[].unpaidQty | string |  | 未还本金 |
| data.unpaidInfo[].unpaidInterest | string |  | 未还利息 |
| data.balanceInfo | object[] |  | 资产明细 |
| data.balanceInfo[].coin | string |  | 保证金币种 |
| data.balanceInfo[].price | string |  | 保证金币种价格 |
| data.balanceInfo[].amount | string |  | 保证金数量 |
| data.balanceInfo[].convertedUsdtAmount | string |  | 保证金折算金额(USDT) |

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
    ]
  }
}
```

## 绑定/解绑子账户UID至风险单元

`POST /api/v2/spot/ins-loan/bind-uid`

限速规则: 5次/1s (Uid)

绑定：

    uid 和riskUnitId 同归属一个主账户;

    uid 未绑定到其他风险单元;

解绑：

    调用接口的API key必须为主账户或风险单元内借贷专属子账户UID;

    uid 在风险单元内且不等于riskUnitId;

    uid 资产为零 或 riskUnitId 无未结清或在途的借贷订单;

Operation ID: `classicInstloanAccountBindRiskUnit`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| riskUnitId | string |  | 风险单元ID (母账户调用需要传，风险单元账户调用不需要传) |
| uid | string | 是 | 子账户UID（一个风险单元最多绑定50个UID） |
| operate | string | 是 | `bind` 绑定 <br><br> `unbind` 解绑 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 处理结果<br><br>"00000": 成功<br><br>其它: 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": "success"
}
```

## 获取风险单元

`GET /api/v2/spot/ins-loan/risk-unit`

限速规则: 5次/1s (Uid)

只能借贷主账户创建的API KEY调用

Operation ID: `classicInstloanAccountGetRiskUnit`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.riskUnitId | string[] |  | 所有风险单元内借贷专属子账户UIDs |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "riskUnitId": [
      "xxxxxxxx",
      "xxxxxxxx"
    ]
  }
}
```

## 查询现货账户可转出金额

`GET /api/v2/spot/ins-loan/transfered`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanAccountGetTransferredAmountFromSpotAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| userId | query | string |  | 用户ID (主账户或者子账户) |
| coin | query | string | 是 | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.transfered | string |  | 可划出金额 |
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