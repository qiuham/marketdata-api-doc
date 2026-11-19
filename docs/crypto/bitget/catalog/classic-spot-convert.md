---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-convert
api_type: REST
updated_at: 2026-11-19 19:07:58.568501
---

# Classic Spot Convert API

Spot convert endpoints — quoted price, trade, and convert history.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/convert/currencies` — Get Convert Coins
- `GET /api/v2/convert/quoted-price` — Get Quoted Price
- `POST /api/v2/convert/trade` — Convert
- `GET /api/v2/convert/convert-record` — Get Convert History

## Get Convert Coins

`GET /api/v2/convert/currencies`

Frequency limit:10 times/1s (User ID)

Get a list of Flash Currencies

Operation ID: `classicSpotConvertGetConvertCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].available | string |  | Currency accounts available |
| data[].maxAmount | string |  | Maximum available quantity as fromCoin means maximum consumable quantity, as toCoin means maximum redeemable quantity. |
| data[].minAmount | string |  | Minimum usable quantity as fromCoin represents the minimum consumable quantity, as toCoin represents the minimum redeemable quantity. |

```json
{
  "code": "00000",
  "data": [
    {
      "coin": "ETH",
      "available": "0.9994",
      "maxAmount": "5",
      "minAmount": "0.0005"
    }
  ],
  "msg": "success",
  "requestTime": 1627293612502
}
```

## Get Quoted Price

`GET /api/v2/convert/quoted-price`

Frequency limit:10 times/1s (User ID)

Get Quoted Price

Operation ID: `classicSpotConvertGetQuotedPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromCoin | query | string | 是 | Quote currency |
| fromCoinSize | query | string |  | Number of quote coins. Only one of `fromCoinSize` and `toCoinSize` is allowed |
| toCoin | query | string | 是 | Target currency |
| toCoinSize | query | string |  | Number of target coins. Only one of `fromCoinSize` and `toCoinSize` is allowed |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fromCoin | string |  | Quote currency |
| data.fromCoinSize | string |  | Number of currencies |
| data.cnvtPrice | string |  | Swap price. Flash price = Quote currency price / Target currency price |
| data.toCoin | string |  | Target currency |
| data.toCoinSize | string |  | Number of target currencies |
| data.traceId | string |  | RFQ id |
| data.fee | string |  | Transaction fee |

```json
{
  "code": "00000",
  "data": {
    "fee": "0",
    "fromCoinSize": "10",
    "fromCoin": "USDT",
    "cnvtPrice": "0.0005226794534969",
    "toCoinSize": "0.23206967",
    "toCoin": "ETH",
    "traceId": "1"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## Convert

`POST /api/v2/convert/trade`

Rate limit: 5 req/sec/UID

Convert

Operation ID: `classicSpotConvertTrade`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromCoin | string | 是 | Quote currency |
| fromCoinSize | string | 是 | Number of currencies |
| cnvtPrice | string | 是 | Results obtained by request for quotation |
| toCoin | string | 是 | Target currency |
| toCoinSize | string | 是 | Number of target currencies converted |
| traceId | string | 是 | RFQ id, valid for 8 seconds |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.toCoin | string |  | Switch |
| data.toCoinSize | string |  | Coin swap amount |
| data.cnvtPrice | string |  | Swap price |
| data.ts | string |  | Conversion time, Unix millisecond timestamps |

```json
{
  "code": "00000",
  "data": {
    "ts": "1688527221603",
    "cnvtPrice": "0.00052268",
    "toCoinSize": "0.23206967",
    "toCoin": "ETH"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## Get Convert History

`GET /api/v2/convert/convert-record`

Frequency limit:10 times/1s (User ID)

Get Convert History

Operation ID: `classicSpotConvertGetConvertRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string | 是 | End time, Unix millisecond timestamps. The maximum interval between startTime and endTime is 90 days. |
| limit | query | string |  | Default 20 Maximum 100 |
| idLessThan | query | string |  | For pagination, from page 2 onward set `idLessThan` as the smallest `orderId` from the previous response. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.dataList | object[] |  | List |
| data.dataList[].id | string |  | Splash Record id |
| data.dataList[].ts | string |  | Time of generation of flash transfer records |
| data.dataList[].cnvtPrice | string |  | Coin swap price |
| data.dataList[].fee | string |  | Transaction fee |
| data.dataList[].fromCoinSize | string |  | Coin swap amount |
| data.dataList[].fromCoin | string |  | Switch |
| data.dataList[].toCoinSize | string |  | Get the number of target coins |
| data.dataList[].toCoin | string |  | Target currency |
| data.endId | string |  | Pagination |

```json
{
  "code": "00000",
  "data": {
    "dataList": [
      {
        "id": "1",
        "ts": "1688527512229",
        "cnvtPrice": "0.00052268",
        "fee": "0",
        "fromCoinSize": "100",
        "fromCoin": "USDT",
        "toCoinSize": "0.23206967",
        "toCoin": "ETH"
      }
    ],
    "endId": "1"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```


---

现货闪兑接口 —— 询价、闪兑及记录查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/convert/currencies` — 查询闪兑币种
- `GET /api/v2/convert/quoted-price` — 获取询价
- `POST /api/v2/convert/trade` — 闪兑
- `GET /api/v2/convert/convert-record` — 获取闪兑记录

## 查询闪兑币种

`GET /api/v2/convert/currencies`

限速规则 10次/1s (UID)

获取闪兑币种列表

Operation ID: `classicSpotConvertGetConvertCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].available | string |  | 币种账户可用 |
| data[].maxAmount | string |  | 最大可用数量 作为fromCoin时 代表最大可消耗数量， 作为toCoin时 代表最大可兑换数量 |
| data[].minAmount | string |  | 最小可用数量 作为fromCoin时 代表最小可消耗数量， 作为toCoin时 代表最小可兑换数量 |

```json
{
  "code": "00000",
  "data": [
    {
      "coin": "ETH",
      "available": "0.9994",
      "maxAmount": "5",
      "minAmount": "0.0005"
    }
  ],
  "msg": "success",
  "requestTime": 1627293612502
}
```

## 获取询价

`GET /api/v2/convert/quoted-price`

限速规则 10次/1s (UID)

获取询价

Operation ID: `classicSpotConvertGetQuotedPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromCoin | query | string | 是 | 询价币种 |
| fromCoinSize | query | string |  | 询价币种数量 fromCoinSize 和 toCoinSize 只允许同时传入一个 |
| toCoin | query | string | 是 | 目标币种 |
| toCoinSize | query | string |  | 目标币种数量 fromCoinSize 和 toCoinSize 只允许同时传入一个 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fromCoin | string |  | 询价币种 |
| data.fromCoinSize | string |  | 询价币种数量 |
| data.cnvtPrice | string |  | 闪兑价格。闪兑价格 = 询价币种价格 / 目标币种价格 |
| data.toCoin | string |  | 目标币种 |
| data.toCoinSize | string |  | 目标币种数量 |
| data.traceId | string |  | 询价单id |
| data.fee | string |  | 手续费 |

```json
{
  "code": "00000",
  "data": {
    "fee": "0",
    "fromCoinSize": "444",
    "fromCoin": "USDT",
    "cnvtPrice": "0.0005226794534969",
    "toCoinSize": "0.23206967",
    "toCoin": "ETH",
    "traceId": "1"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## 闪兑

`POST /api/v2/convert/trade`

限速规则: 5 次/秒/UID

闪兑

Operation ID: `classicSpotConvertTrade`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromCoin | string | 是 | 询价币种 |
| fromCoinSize | string | 是 | 询价币种数量 |
| cnvtPrice | string | 是 | 询价获取的结果 |
| toCoin | string | 是 | 目标币种 |
| toCoinSize | string | 是 | 目标币种兑换数量 |
| traceId | string | 是 | 询价单id，有效期8秒 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.toCoin | string |  | 兑换币种 |
| data.toCoinSize | string |  | 得到兑换币种数量 |
| data.cnvtPrice | string |  | 兑换价格 |
| data.ts | string |  | 兑换时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "data": {
    "ts": "1688527221603",
    "cnvtPrice": "0.00052268",
    "toCoinSize": "0.23206967",
    "toCoin": "ETH"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## 获取闪兑记录

`GET /api/v2/convert/convert-record`

限速规则 10次/1s (UID)

闪兑记录

Operation ID: `classicSpotConvertGetConvertRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string | 是 | 结束时间，Unix毫秒时间戳。startTime与endTime间隔最多为90天 |
| limit | query | string |  | 默认值20 最大100 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.dataList | object[] |  | 列表 |
| data.dataList[].id | string |  | 闪兑记录id |
| data.dataList[].ts | string |  | 闪兑记录生成时间 |
| data.dataList[].cnvtPrice | string |  | 兑换时价格 |
| data.dataList[].fee | string |  | 手续费 |
| data.dataList[].fromCoinSize | string |  | 兑换币种数量 |
| data.dataList[].fromCoin | string |  | 兑换币种 |
| data.dataList[].toCoinSize | string |  | 得到目标币种数量 |
| data.dataList[].toCoin | string |  | 目标币种 |
| data.endId | string |  | 分页使用 |

```json
{
  "code": "00000",
  "data": {
    "dataList": [
      {
        "id": "1",
        "ts": "1688527512229",
        "cnvtPrice": "0.00052268",
        "fee": "0",
        "fromCoinSize": "444",
        "fromCoin": "USDT",
        "toCoinSize": "0.23206967",
        "toCoin": "ETH"
      }
    ],
    "endId": "1"
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```