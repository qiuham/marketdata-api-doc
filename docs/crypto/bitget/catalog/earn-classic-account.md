---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn-classic-account
api_type: REST
updated_at: 2026-11-21 19:04:08.879105
---

# Classic Earn Account

Classic account earn account assets API.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/account/assets` — Earn Account

## Earn Account

`GET /api/v2/earn/account/assets`

Rate limit: 5/sec/UID

Get earn account assets overview. Sub-account requests are not allowed.

Operation ID: `classicEarnAccountGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Assets coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Assets list |
| data[].coin | string |  | Coin |
| data[].amount | string |  | Amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712046333409,
  "data": [
    {
      "coin": "BTC",
      "amount": "0.10000000"
    },
    {
      "coin": "USDT",
      "amount": "400.00000000"
    }
  ]
}
```


---

经典账户理财账户资产接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/account/assets` — 理财账户信息

## 理财账户信息

`GET /api/v2/earn/account/assets`

限频规则: 5次/秒/UID

获取理财账户资产信息。

禁止子账户请求。

Operation ID: `classicEarnAccountGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 资产币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 资产列表 |
| data[].coin | string |  | 币种 |
| data[].amount | string |  | 数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1712046333409,
  "data": [
    {
      "coin": "BTC",
      "amount": "0.10000000"
    },
    {
      "coin": "USDT",
      "amount": "400.00000000"
    }
  ]
}
```