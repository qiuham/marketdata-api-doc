---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-common-account
api_type: REST
updated_at: 2026-11-27 19:02:34.320891
---

# Classic Assets API

Public assets endpoints — all-account balance, bot assets, and funding assets.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/account/all-account-balance` — Assets overview
- `GET /api/v2/account/bot-assets` — Bot account
- `GET /api/v2/account/funding-assets` — Funding Assets

## Assets overview

`GET /api/v2/account/all-account-balance`

Frequency limit: 1 times/1s (User ID)

Operation ID: `classicCommonAccountAllAccountBalance`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.data | string[] |  | assetsList |
| data.> accountType | string |  | account Type |
| data.> usdtBalance | string |  | USDT amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712129301188,
  "data": [
    {
      "accountType": "spot",
      "usdtBalance": "326883.9190752508"
    },
    {
      "accountType": "futures",
      "usdtBalance": "280108.503808983783"
    },
    {
      "accountType": "funding",
      "usdtBalance": "0"
    },
    {
      "accountType": "earn",
      "usdtBalance": "142313.7"
    },
    {
      "accountType": "bots",
      "usdtBalance": "210.585022843422"
    },
    {
      "accountType": "margin",
      "usdtBalance": "54616.35774218"
    }
  ]
}
```

## Bot account

`GET /api/v2/account/bot-assets`

Frequency limit: 10 times/1s (User ID)

Operation ID: `classicCommonAccountBotAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | bot account type <br><br>futures <br><br>spot |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.data | string[] |  | assetsList |
| data.> coin | string |  | coin |
| data.> available | string |  | available |
| data.> equity | string |  | account assets |
| data.> bonus | string |  | trading bonuses |
| data.> frozen | string |  | in orders |
| data.> usdtValue | string |  | USDT values |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712131247803,
  "data": [
    {
      "coin": "USDT",
      "available": "84.61136285",
      "equity": "140.94936285",
      "bonus": "0",
      "frozen": "0",
      "usdtValue": "140.949362850622"
    }
  ]
}
```

## Funding Assets

`GET /api/v2/account/funding-assets`

Frequency limit: 10 times/1s (User ID)

Sub-account requests are not allowed for the funding account.

Operation ID: `classicCommonAccountFundingAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | default all coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.data | string[] |  | assets List |
| data.> coin | string |  | coin |
| data.> available | string |  | available |
| data.> frozen | string |  | forzen |
| data.> usdtValue | string |  | USDT value |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712129301188,
  "data": [
    {
      "coin": "USDT",
      "available": "326",
      "frozen": "",
      "usdtValue": "326"
    }
  ]
}
```


---

公共资产接口 —— 资产概览、策略账户、资金账户。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/account/all-account-balance` — 资产概览
- `GET /api/v2/account/bot-assets` — 策略账户
- `GET /api/v2/account/funding-assets` — 资金账户

## 资产概览

`GET /api/v2/account/all-account-balance`

限速规则 1次/1s (UID)

Operation ID: `classicCommonAccountAllAccountBalance`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.accountType | string |  | 账户类型 |
| data.usdtBalance | string |  | USDT数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712129301188,
  "data": [
    {
      "accountType": "spot",
      "usdtBalance": "326883.9190752508"
    },
    {
      "accountType": "futures",
      "usdtBalance": "280108.503808983783"
    },
    {
      "accountType": "funding",
      "usdtBalance": "0"
    },
    {
      "accountType": "earn",
      "usdtBalance": "142313.7"
    },
    {
      "accountType": "bots",
      "usdtBalance": "210.585022843422"
    },
    {
      "accountType": "margin",
      "usdtBalance": "54616.35774218"
    }
  ]
}
```

## 策略账户

`GET /api/v2/account/bot-assets`

限速规则 10次/1s (UID)

Operation ID: `classicCommonAccountBotAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | 策略账户类型<br><br>futures<br><br>spot |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种 |
| data.available | string |  | 可用 |
| data.equity | string |  | 账户权益<br><br>accountType 为 futures 显示 |
| data.bonus | string |  | 体验金<br><br>accountType 为 futures 显示 |
| data.frozen | string |  | 委托中 |
| data.usdtValue | string |  | USDT估值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712131247803,
  "data": [
    {
      "coin": "USDT",
      "available": "84.61136285",
      "equity": "140.94936285",
      "bonus": "0",
      "frozen": "0",
      "usdtValue": "140.949362850622"
    }
  ]
}
```

## 资金账户

`GET /api/v2/account/funding-assets`

限速规则 10次/1s (UID)

资金账户不支持子账户请求。

Operation ID: `classicCommonAccountFundingAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 默认所有币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种 |
| data.available | string |  | 可用 |
| data.frozen | string |  | 冻结 |
| data.usdtValue | string |  | USDT估值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712129301188,
  "data": [
    {
      "coin": "USDT",
      "available": "326",
      "frozen": "",
      "usdtValue": "326"
    }
  ]
}
```