---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-common-public
api_type: REST
updated_at: 2026-11-24 19:01:54.092123
---

# Classic Public Config API

Public endpoints — server time and trade rate.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/public/time` — Get Server Time
- `GET /api/v2/common/trade-rate` — Get Trade Rate
- `GET /api/v2/common/all-trade-rate` — Get Business Line All Symbol Trade Rate

## Get Server Time

`GET /api/v2/public/time`

Frequency limit: 20 times/1s (IP)

Getting server time,Unix millisecond timestamp

Operation ID: `classicCommonGetServerTime`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.serverTime | string |  | Server time, Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": {
    "serverTime": "1688008631614"
  }
}
```

## Get Trade Rate

`GET /api/v2/common/trade-rate`

Frequency limit:10 times/1s (UID)

Get Trade Rate

Operation ID: `classicCommonGetTradeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name, e.g. BTCUSDT |
| businessType | query | string | 是 | Business type<br><br>mix contract<br><br>spot Spot<br><br>margin leverage |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.makerFeeRate | string |  | Pending Order Handling Rates<br><br>Fractional form, i.e., 0.0002 for two parts per million |
| data.takerFeeRate | string |  | Taking Order Handling Rates<br><br>Fractional form, i.e., 0.0002 for two parts per million |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "makerFeeRate": "0.0002",
    "takerFeeRate": "0.0006"
  }
}
```

## Get Business Line All Symbol Trade Rate

`GET /api/v2/common/all-trade-rate`

Frequency limit:10 times/1s (UID)

Get Trade Rate

Operation ID: `classicCommonGetAllTradeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| businessType | query | string | 是 | Business type<br><br>mix contract<br><br>spot Spot<br><br>margin leverage |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.makerFeeRate | string |  | Pending Order Handling Rates<br><br>Fractional form, i.e., 0.0002 for two parts per million |
| data.takerFeeRate | string |  | Taking Order Handling Rates<br><br>Fractional form, i.e., 0.0002 for two parts per million |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": [
    {
      "symbol": "BTCUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    },
    {
      "symbol": "ETHUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    },
    {
      "symbol": "DOGEUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    }
  ]
}
```


---

公共接口 —— 服务器时间与交易手续费。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/public/time` — 获取服务器时间
- `GET /api/v2/common/trade-rate` — 获取交易手续费
- `GET /api/v2/common/all-trade-rate` — 获取业务线所有交易对手续费

## 获取服务器时间

`GET /api/v2/public/time`

限速规则 20次/1s (IP)

获取服务器时间，时间格式为Unix毫秒时间戳

Operation ID: `classicCommonGetServerTime`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.serverTime | string |  | 服务器时间，Unix毫秒时间戳，例如1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": {
    "serverTime": "1688008631614"
  }
}
```

## 获取交易手续费

`GET /api/v2/common/trade-rate`

限速规则 10次/1s (UID)

获取交易费率

Operation ID: `classicCommonGetTradeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，如BTCUSDT |
| businessType | query | string | 是 | 业务类型<br><br>mix合约<br><br>spot现货<br><br>margin杠杆 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.makerFeeRate | string |  | 挂单手续费率<br><br>小数形式，即0.0002代表万分之二 |
| data.takerFeeRate | string |  | 吃单手续费率<br><br>小数形式，即0.0002代表万分之二 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "makerFeeRate": "0.0002",
    "takerFeeRate": "0.0006"
  }
}
```

## 获取业务线所有交易对手续费

`GET /api/v2/common/all-trade-rate`

限速规则 10次/1s (UID)

获取交易费率

Operation ID: `classicCommonGetAllTradeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| businessType | query | string | 是 | 业务类型<br><br>mix合约<br><br>spot现货<br><br>margin杠杆 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 币对名称 |
| data.makerFeeRate | string |  | 挂单手续费率<br><br>小数形式，即0.0002代表万分之二 |
| data.takerFeeRate | string |  | 吃单手续费率<br><br>小数形式，即0.0002代表万分之二 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": [
    {
      "symbol": "BTCUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    },
    {
      "symbol": "ETHUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    },
    {
      "symbol": "DOGEUSDT",
      "makerFeeRate": "0.0001",
      "takerFeeRate": "0.0004"
    }
  ]
}
```