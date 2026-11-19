---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-bgb-convert
api_type: REST
updated_at: 2026-11-19 19:07:57.925869
---

# Classic Spot BGB Convert API

Spot BGB convert endpoints — convert small balances to BGB and query records.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/convert/bgb-convert` — Convert BGB
- `GET /api/v2/convert/bgb-convert-coin-list` — Get BGB Convert Coins
- `GET /api/v2/convert/bgb-convert-records` — Get BGB Convert History

## Convert BGB

`POST /api/v2/convert/bgb-convert`

Frequency limit:10 times/1s (User ID)

Convert BGB

Operation ID: `classicSpotBgbConvertBgbConvert`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coinList | string[] | 是 | swap coins |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  |  |
| data.orderList[].coin | string |  | Coin swap |
| data.orderList[].orderId | string |  | swap order Id |

```json
{
  "code": "00000",
  "data": {
    "orderList": [
      {
        "coin": "EOS",
        "orderId": "1233431213"
      },
      {
        "coin": "GROK",
        "orderId": "1233431213"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## Get BGB Convert Coins

`GET /api/v2/convert/bgb-convert-coin-list`

Frequency limit:10 times/1s (User ID)

Get a list of Convert Bgb Currencies

Operation ID: `classicSpotBgbConvertGetBgbConvertCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coinList | object[] |  |  |
| data.coinList[].coin | string |  | Token name |
| data.coinList[].available | string |  | Currency accounts available |
| data.coinList[].bgbEstAmount | string |  | Expected number of BGB redeemable |
| data.coinList[].precision | string |  | bgb scale |
| data.coinList[].feeDetail | object[] |  | fee detail |
| data.coinList[].feeDetail[].feeRate | string |  | fee rate |
| data.coinList[].feeDetail[].fee | string |  | fee |
| data.coinList[].cTime | string |  | Currently Time (time stamp in milliseconds) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1703831563264,
  "data": {
    "coinList": [
      {
        "coin": "SEAM",
        "available": "0.00303329",
        "bgbEstAmount": "0.03794680",
        "precision": "8",
        "feeDetail": [
          {
            "feeRate": "0.02",
            "fee": "0.00075893"
          }
        ],
        "cTime": "1703831563514"
      }
    ]
  }
}
```

## Get BGB Convert History

`GET /api/v2/convert/bgb-convert-records`

Frequency limit:10 times/1s (User ID)

Get BGB Convert History

Operation ID: `classicSpotBgbConvertGetBgbConvertRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Splash Record id |
| startTime | query | string |  | Start time, Unix millisecond timestamps |
| endTime | query | string |  | End time, Unix millisecond timestamps. The maximum interval between startTime and endTime is 90 days. |
| limit | query | string |  | Default 20 Maximum 100 |
| idLessThan | query | string |  | For pagination, from page 2 onward set `idLessThan` as the smallest `orderId` from the previous response. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Splash Record id |
| data[].fromCoin | string |  | Switch Coin |
| data[].fromAmount | string |  | Switch amount |
| data[].fromCoinPrice | string |  | Coin swap price |
| data[].toCoin | string |  | Target currency |
| data[].toAmount | string |  | Target currency Amount |
| data[].toCoinPrice | string |  | Get the price of target coins |
| data[].feeDetail | object[] |  | swap fee detail |
| data[].feeDetail[].fee | string |  | fee |
| data[].feeDetail[].feeCoin | string |  | fee coin |
| data[].status | string |  | swap status |
| data[].ctime | string |  | Time of generation of flash transfer records |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1703835442804,
  "data": [
    {
      "orderId": "xxxx",
      "fromCoin": "ROOT",
      "fromAmount": "64.99837000",
      "fromCoinPrice": "0.02954000",
      "toCoin": "BGB",
      "toAmount": "3.55072001",
      "toCoinPrice": "0.54075000",
      "feeDetail": [
        {
          "feeCoin": "BGB",
          "fee": "0.07101441"
        }
      ],
      "status": "success",
      "ctime": "1700837066186"
    }
  ]
}
```


---

现货兑换BGB接口 —— 小额兑换BGB及记录查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/convert/bgb-convert` — 兑换BGB
- `GET /api/v2/convert/bgb-convert-coin-list` — 查询兑换BGB币种
- `GET /api/v2/convert/bgb-convert-records` — 获取BGB兑换记录

## 兑换BGB

`POST /api/v2/convert/bgb-convert`

限速规则 10次/1s (UID)

小额兑换bgb

Operation ID: `classicSpotBgbConvertBgbConvert`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coinList | string[] | 是 | 兑换币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  |  |
| data.orderList[].coin | string |  | 兑换币种 |
| data.orderList[].orderId | string |  | 兑换订单Id |

```json
{
  "code": "00000",
  "data": {
    "orderList": [
      {
        "coin": "BTC",
        "orderId": "1233431213"
      },
      {
        "coin": "ETH",
        "orderId": "1233431213"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293612502
}
```

## 查询兑换BGB币种

`GET /api/v2/convert/bgb-convert-coin-list`

限速规则 10次/1s (UID)

获取小额兑换bgb 币种列表

Operation ID: `classicSpotBgbConvertGetBgbConvertCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coinList | object[] |  |  |
| data.coinList[].coin | string |  | 币种名称 |
| data.coinList[].available | string |  | 币种账户可用 |
| data.coinList[].bgbEstAmount | string |  | 预期可兑换BGB数量 |
| data.coinList[].precision | string |  | 兑换精度 固定值 |
| data.coinList[].feeDetail | object[] |  | 手续费明细 |
| data.coinList[].feeDetail[].feeRate | string |  | 手续费率 |
| data.coinList[].feeDetail[].fee | string |  | 手续费数额 |
| data.coinList[].cTime | string |  | 当前时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1703831563264,
  "data": {
    "coinList": [
      {
        "coin": "SEAM",
        "available": "0.00303329",
        "bgbEstAmount": "0.03794680",
        "precision": "8",
        "feeDetail": [
          {
            "feeRate": "0.02",
            "fee": "0.00075893"
          }
        ],
        "cTime": "1703831563514"
      }
    ]
  }
}
```

## 获取BGB兑换记录

`GET /api/v2/convert/bgb-convert-records`

限速规则 10次/1s (UID)

小额兑换BGB记录

Operation ID: `classicSpotBgbConvertGetBgbConvertRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 兑换订单Id |
| startTime | query | string |  | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳。startTime与endTime间隔最多为90天 |
| limit | query | string |  | 默认值20 最大100 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 闪兑记录id |
| data[].fromCoin | string |  | 兑换币种 |
| data[].fromAmount | string |  | 兑换数量 |
| data[].fromCoinPrice | string |  | 兑换时价格 |
| data[].toCoin | string |  | 得到币种 |
| data[].toAmount | string |  | 得到币种数量 |
| data[].toCoinPrice | string |  | 得到目标币种价格 |
| data[].feeDetail | object[] |  | 手续费明细 |
| data[].feeDetail[].fee | string |  | 手续费数额 |
| data[].feeDetail[].feeCoin | string |  | 手续费币种 |
| data[].status | string |  | 兑换状态 |
| data[].ctime | string |  | 兑换时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1703835442804,
  "data": [
    {
      "orderId": "xxxxx",
      "fromCoin": "ROOT",
      "fromAmount": "64.99837000",
      "fromCoinPrice": "0.02954000",
      "toCoin": "BGB",
      "toAmount": "3.55072001",
      "toCoinPrice": "0.54075000",
      "feeDetail": [
        {
          "feeCoin": "BGB",
          "fee": "0.07101441"
        }
      ],
      "status": "success",
      "ctime": "1700837066186"
    }
  ]
}
```