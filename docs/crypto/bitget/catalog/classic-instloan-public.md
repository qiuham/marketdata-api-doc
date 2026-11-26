---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-instloan-public
api_type: REST
updated_at: 2026-11-26 19:03:52.196658
---

# Classic Inst Loan Public API

Classic account — institutional loan products, symbols and margin coins.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/product-infos` — Get Product Info
- `GET /api/v2/spot/ins-loan/ensure-coins-convert` — Get Margin Coin Info
- `GET /api/v2/spot/ins-loan/symbols` — Get Spot Symbols

## Get Product Info

`GET /api/v2/spot/ins-loan/product-infos`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanPublicGetProductInfo`

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
| data.leverage | string |  | The maximum leverage for this loan product. 2x/4x |
| data.transferLine | string |  | Restrict line for transfer, eg: 0.6667 |
| data.spotBuyLine | string |  | Restrict line for Spot buy, eg: 0.8 |
| data.liquidationLine | string |  | Line for liquidation, eg: 0.9 |
| data.stopLiquidationLine | string |  | Line for stop liquidation, eg: 0.75 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697573019,
  "data": {
    "productId": "xxxxxxxx",
    "leverage": "2",
    "transferLine": "0.6667",
    "spotBuyLine": "0.8",
    "liquidationLine": "0.9",
    "stopLiquidationLine": "0.75"
  }
}
```

## Get Margin Coin Info

`GET /api/v2/spot/ins-loan/ensure-coins-convert`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanPublicGetMarginCoinInfo`

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
| data.coinInfo[].maxConvertValue | string |  | Maximum convert value(USDT) |

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
        "maxConvertValue": "1000"
      },
      {
        "coin": "USDT",
        "convertRatio": "1",
        "maxConvertValue": "1000"
      },
      {
        "coin": "BTC",
        "convertRatio": "0.99",
        "maxConvertValue": "1000"
      },
      {
        "coin": "ETH",
        "convertRatio": "0.99",
        "maxConvertValue": "1000"
      }
    ]
  }
}
```

## Get Spot Symbols

`GET /api/v2/spot/ins-loan/symbols`

Rate limit: 5 req/sec/UID

Operation ID: `classicInstloanPublicGetSpotSymbols`

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

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "productId": "xxxxxxxx",
    "spotSymbols": [
      "BTCUSDT",
      "ETHUSDT"
    ]
  }
}
```


---

经典账户 — 机构借贷产品、交易对与保证金币种。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/ins-loan/product-infos` — 查询产品信息
- `GET /api/v2/spot/ins-loan/ensure-coins-convert` — 查询保证金币种信息
- `GET /api/v2/spot/ins-loan/symbols` — 查询支持现货交易对信息

## 查询产品信息

`GET /api/v2/spot/ins-loan/product-infos`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanPublicGetProductInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID,保证唯一性 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.leverage | string |  | 该借贷产品的最大杠杆倍数，2 或 4 |
| data.transferLine | string |  | 限制划转线，举例：0.6667 |
| data.spotBuyLine | string |  | 限制现货买入线，举例：0.8 |
| data.liquidationLine | string |  | 强平减仓线，举例：0.9 |
| data.stopLiquidationLine | string |  | 停止强平线，举例：0.75 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697573019,
  "data": {
    "productId": "xxxxxxxx",
    "leverage": "2",
    "transferLine": "0.6667",
    "spotBuyLine": "0.8",
    "liquidationLine": "0.9",
    "stopLiquidationLine": "0.75"
  }
}
```

## 查询保证金币种信息

`GET /api/v2/spot/ins-loan/ensure-coins-convert`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanPublicGetMarginCoinInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID,保证唯一性 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.coinInfo | object[] |  | 现货保证金币种信息 |
| data.coinInfo[].coin | string |  | 保证金币种 |
| data.coinInfo[].convertRatio | string |  | 保证金折算率 |
| data.coinInfo[].maxConvertValue | string |  | 最大折算金额（USDT） |

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
        "maxConvertValue": "1000"
      },
      {
        "coin": "USDT",
        "convertRatio": "1",
        "maxConvertValue": "1000"
      },
      {
        "coin": "BTC",
        "convertRatio": "0.99",
        "maxConvertValue": "1000"
      },
      {
        "coin": "ETH",
        "convertRatio": "0.99",
        "maxConvertValue": "1000"
      }
    ]
  }
}
```

## 查询支持现货交易对信息

`GET /api/v2/spot/ins-loan/symbols`

限速规则: 5次/1s (Uid)

Operation ID: `classicInstloanPublicGetSpotSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品ID,保证唯一性 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品ID |
| data.spotSymbols | string[] |  | 现货交易对列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1711697588556,
  "data": {
    "productId": "xxxxxxxx",
    "spotSymbols": [
      "BTCUSDT",
      "ETHUSDT"
    ]
  }
}
```