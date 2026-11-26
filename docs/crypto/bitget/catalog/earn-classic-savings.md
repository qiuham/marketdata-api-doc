---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn-classic-savings
api_type: REST
updated_at: 2026-11-26 19:04:04.177670
---

# Classic Simple Earn

Classic account savings product, subscription, redemption, and record APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/savings/product` — Get Simple Earn Product List
- `GET /api/v2/earn/savings/account` — Simple Earn Account
- `GET /api/v2/earn/savings/assets` — Simple Earn Assets
- `GET /api/v2/earn/savings/records` — Simple Earn Records
- `GET /api/v2/earn/savings/subscribe-info` — Simple Earn Subscription Detail
- `POST /api/v2/earn/savings/subscribe` — Subscribe Simple Earn
- `GET /api/v2/earn/savings/subscribe-result` — Simple Earn Subscription Result
- `POST /api/v2/earn/savings/redeem` — Redeem Simple Earn
- `GET /api/v2/earn/savings/redeem-result` — Simple Earn Redemption Results

## Get Simple Earn Product List

`GET /api/v2/earn/savings/product`

Rate limit: 10/sec/UID

Get savings product list.

Operation ID: `classicEarnSavingsGetProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin e.g. BTC |
| filter | query | string |  | Filter conditions<br><br>`available` Available for subscription<br><br>`held` Held<br><br>`available_and_held` Available for subscription and held<br><br>`all` Query all including those that have been removed from the shelves |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | Product id |
| data[].coin | string |  | Simple Earn subscription coin |
| data[].periodType | string |  | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| data[].period | string |  | Period<br><br>`flexible` This value is not returned |
| data[].apyType | string |  | Interest rate type<br><br>`single` single interest rate<br><br>`ladder` ladder income |
| data[].advanceRedeem | string |  | Whether early redemption is allowed<br><br>`Yes` allowed<br><br>`No` not allowed |
| data[].settleMethod | string |  | Settlement method<br><br>`daily` daily interest and daily settlement<br><br>`maturity` repayment of principal and interest at maturity |
| data[].apyList | object[] |  | Ladder interest rate information |
| data[].apyList[].rateLevel | string |  | Rate level |
| data[].apyList[].minStepVal | string |  | Ladder minimum amount value |
| data[].apyList[].maxStepVal | string |  | Ladder maximum amount value |
| data[].apyList[].currentApy | string |  | Current tiered annual interest rate |
| data[].status | string |  | Product status<br><br>`not_started` Warming up<br><br>`in_progress` Subscribing<br><br>`paused` Paused<br><br>`completed` Ended<br><br>`sold_out` Sold out<br><br>`off_line` Off line |
| data[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696747382760,
  "data": [
    {
      "productId": "12313123",
      "coin": "BGB",
      "periodType": "flexible",
      "period": "",
      "apyType": "ladder",
      "advanceRedeem": "",
      "settleMethod": "",
      "apyList": [
        {
          "rateLevel": "0",
          "minStepVal": "0.000000",
          "maxStepVal": "200.000000",
          "currentApy": "6.00"
        },
        {
          "rateLevel": "1",
          "minStepVal": "200.000000",
          "maxStepVal": "5000.000000",
          "currentApy": "50.00"
        }
      ],
      "status": "in_progress",
      "productLevel": "normal"
    }
  ]
}
```

## Simple Earn Account

`GET /api/v2/earn/savings/account`

Rate limit: 10/sec/UID

Get savings account info.

Operation ID: `classicEarnSavingsGetAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcAmount | string |  | Estimated total asset value in BTC |
| data.usdtAmount | string |  | Estimated total asset value in USDT |
| data.btc24hEarning | string |  | 24-hour earning in BTC |
| data.usdt24hEarning | string |  | 24-hour earning in USDT |
| data.btcTotalEarning | string |  | Cumulative earning in BTC |
| data.usdtTotalEarning | string |  | Cumulative earning in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748551073,
  "data": {
    "btcAmount": "0.35821314",
    "usdtAmount": "9481.55500000",
    "btc24hEarning": "0.00000009",
    "usdt24hEarning": "0.00263912",
    "btcTotalEarning": "0.00000761",
    "usdtTotalEarning": "0.20145653"
  }
}
```

## Simple Earn Assets

`GET /api/v2/earn/savings/assets`

Rate limit: 10/sec/UID

Get savings assets.

Operation ID: `classicEarnSavingsGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| periodType | query | string | 是 | Period type<br><br>`flexible` demand deposit<br><br>`fixed` time deposit |
| startTime | query | string |  | Start timestamp<br><br>(Simple Earn creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Simple Earn creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Simple Earn assets list |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].orderId | string |  | assets order ID<br><br>only for `fixed` |
| data.resultList[].productCoin | string |  | Simple Earn subscription coin |
| data.resultList[].interestCoin | string |  | Interest earning coin |
| data.resultList[].periodType | string |  | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| data.resultList[].period | string |  | Duration<br><br>`flexible` This value is not returned |
| data.resultList[].holdAmount | string |  | Current subscription size |
| data.resultList[].lastProfit | string |  | Profit in the last day |
| data.resultList[].totalProfit | string |  | Profit in total |
| data.resultList[].holdDays | string |  | Days of holding |
| data.resultList[].status | string |  | Product Status<br><br>`in_holding` In holding |
| data.resultList[].allowRedemption | string |  | Whether early redemption is allowed<br><br>`Yes` allowed<br><br>`No` not allowed |
| data.resultList[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |
| data.resultList[].apy | object[] |  | Ladder interest rate info |
| data.resultList[].apy[].rateLevel | string |  | Rate level |
| data.resultList[].apy[].minApy | string |  | Minimum APY |
| data.resultList[].apy[].maxApy | string |  | Maximum APY |
| data.resultList[].apy[].currentApy | string |  | Current tiered APY |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748867881,
  "data": {
    "resultList": [
      {
        "productId": "123123123",
        "orderId": "xxxx",
        "productCoin": "BGB",
        "interestCoin": "BGB",
        "periodType": "flexible",
        "period": "",
        "holdAmount": "100.000",
        "lastProfit": "0.01643800",
        "totalProfit": "1.25479000",
        "holdDays": "",
        "status": "in_holding",
        "allowRedemption": "",
        "productLevel": "normal",
        "apy": [
          {
            "rateLevel": "1",
            "minApy": "0.000000",
            "maxApy": "200.000000",
            "currentApy": "6.00"
          }
        ]
      }
    ],
    "endId": "123456789"
  }
}
```

## Simple Earn Records

`GET /api/v2/earn/savings/records`

Rate limit: 10/sec/UID

Get savings records.

Operation ID: `classicEarnSavingsGetRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Subscribe coin |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| orderType | query | string |  | Record type<br><br>`subscribe` subscription<br><br>`redeem` redemption<br><br>`pay_interest` interest payment<br><br>`deduction` penalty interest (only supports regular periods) |
| startTime | query | string |  | Start timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time.) |
| endTime | query | string |  | End timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Data list |
| data.resultList[].orderId | string |  | Record id |
| data.resultList[].coinName | string |  | Product Subscribe coin |
| data.resultList[].settleCoinName | string |  | Settled coin |
| data.resultList[].productType | string |  | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| data.resultList[].period | string |  | Duration<br><br>`flexible` This value is not returned |
| data.resultList[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |
| data.resultList[].amount | string |  | Subscribe amount |
| data.resultList[].ts | string |  | Subscribe time timestamp |
| data.resultList[].orderType | string |  | Record type<br><br>`subscribe` subscription<br><br>`redeem` redemption<br><br>`pay_interest` interest payment<br><br>`deduction` penalty interest (only supports regular periods) |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696749517654,
  "data": {
    "resultList": [
      {
        "orderId": "123123123123",
        "coinName": "BGB",
        "settleCoinName": "BGB",
        "productType": "flexible",
        "period": "",
        "productLevel": "normal",
        "amount": "200.000000",
        "ts": "1695797014392",
        "orderType": "redeem"
      }
    ],
    "endId": "456456456456"
  }
}
```

## Simple Earn Subscription Detail

`GET /api/v2/earn/savings/subscribe-info`

Rate limit: 10/sec/UID

Get subscription detail before subscribe savings.

Operation ID: `classicEarnSavingsGetSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.singleMinAmount | string |  | Minimum limit for a single transaction |
| data.singleMaxAmount | string |  | Maximum limit for a single transaction |
| data.remainingAmount | string |  | Amount held remaing |
| data.subscribePrecision | string |  | Subscription precision |
| data.profitPrecision | string |  | Profit precison |
| data.subscribeTime | string |  | Subscription time, Unix millisecond timestamp |
| data.interestTime | string |  | Interest generation time, Unix millisecond timestamp |
| data.settleTime | string |  | Interest settlement time, Unix millisecond timestamp |
| data.expireTime | string |  | Expiration time, Unix millisecond timestamp |
| data.redeemTime | string |  | Redemption time, Unix millisecond timestamp |
| data.settleMethod | string |  | Settlement method |
| data.apyList | object[] |  | Ladder interest rate info |
| data.apyList[].rateLevel | string |  | Rate level |
| data.apyList[].minStepVal | string |  | Ladder minimum amount value |
| data.apyList[].maxStepVal | string |  | Ladder maximum amount value |
| data.apyList[].currentApy | string |  | Current tiered annual interest rate |
| data.redeemDelay | string |  | The number of days of delay in the redemption's arrival. The return value is D+1, which means the redemption is delayed by one day, and so on. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "singleMinAmount": "10.000000",
    "singleMaxAmount": "2000.000000",
    "remainingAmount": "4899.999990",
    "subscribePrecision": "6",
    "profitPrecision": "6",
    "subscribeTime": "1696751519451",
    "interestTime": "1696780800000",
    "settleTime": "1696867200000",
    "expireTime": "",
    "redeemTime": "",
    "settleMethod": "",
    "apyList": [
      {
        "rateLevel": "0",
        "minStepVal": "0.000000",
        "maxStepVal": "200.000000",
        "currentApy": "6.00"
      },
      {
        "rateLevel": "1",
        "minStepVal": "200.000000",
        "maxStepVal": "5000.000000",
        "currentApy": "50.00"
      }
    ],
    "redeemDelay": ""
  }
}
```

## Subscribe Simple Earn

`POST /api/v2/earn/savings/subscribe`

Rate limit: 10/sec/UID

Subscribe savings.

Operation ID: `classicEarnSavingsSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| periodType | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| amount | string | 是 | Subscribe amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Successful subscription order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1748783837837,
  "data": {
    "orderId": "1313060074239184896"
  }
}
```

## Simple Earn Subscription Result

`GET /api/v2/earn/savings/subscribe-result`

Rate limit: 10/sec/UID

Get savings subscription result.

Operation ID: `classicEarnSavingsGetSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Subscription result<br><br>`success` Success<br><br>`fail` Fail |
| data.msg | string |  | There will be an error message when the result is `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## Redeem Simple Earn

`POST /api/v2/earn/savings/redeem`

Rate limit: 10/sec/UID

Redeem savings.

The interval of each redeem should be more than 1min, or it would return error.

Operation ID: `classicEarnSavingsRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| orderId | string |  | Assets Order ID<br><br>get this for `/assets` orderId |
| periodType | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| amount | string | 是 | Subscribe amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Redemption successful order ID |
| data.status | string |  | Order status |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## Simple Earn Redemption Results

`GET /api/v2/earn/savings/redeem-result`

Rate limit: 10/sec/UID

Get savings redeem result.

Operation ID: `classicEarnSavingsGetRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Subscription order ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Redemption result<br><br>`success` Success<br><br>`fail` Fail |
| data.msg | string |  | There will be an error message when the result is `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```


---

经典账户简单赚币产品、申购、赎回与记录接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/savings/product` — 简单赚币产品列表
- `GET /api/v2/earn/savings/account` — 简单赚币账户信息
- `GET /api/v2/earn/savings/assets` — 简单赚币资产信息
- `GET /api/v2/earn/savings/records` — 简单赚币历史记录
- `GET /api/v2/earn/savings/subscribe-info` — 简单赚币申购详情
- `POST /api/v2/earn/savings/subscribe` — 简单赚币申购
- `GET /api/v2/earn/savings/subscribe-result` — 简单赚币申购结果
- `POST /api/v2/earn/savings/redeem` — 简单赚币赎回
- `GET /api/v2/earn/savings/redeem-result` — 简单赚币赎回结果

## 简单赚币产品列表

`GET /api/v2/earn/savings/product`

限频规则: 10次/秒/UID

获取简单赚币产品列表。

Operation ID: `classicEarnSavingsGetProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种 |
| filter | query | string |  | 筛选条件<br><br>`available` 可申购的<br><br>`held` 持有中<br><br>`available_and_held` 申购和持有中<br><br>`all` 查询全部 包含下架的 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | 产品Id |
| data[].coin | string |  | 产品申购币种 |
| data[].periodType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data[].apyType | string |  | 利率类型<br><br>`single` 单一利率<br><br>`ladder` 阶梯收益 |
| data[].advanceRedeem | string |  | 是否允许提前赎回<br><br>`Yes` 允许<br><br>`No` 不允许 |
| data[].settleMethod | string |  | 结算方式<br><br>`daily` 日息日结<br><br>`maturity` 到期还本付息 |
| data[].apyList | object[] |  | 阶梯利率信息 |
| data[].apyList[].rateLevel | string |  | 费率级别 |
| data[].apyList[].minStepVal | string |  | 阶梯最小金额值 |
| data[].apyList[].maxStepVal | string |  | 阶梯最大金额值 |
| data[].apyList[].currentApy | string |  | 当前阶梯年利率 |
| data[].status | string |  | 产品状态<br><br>`not_started` 预热中<br><br>`in_progress` 申购中<br><br>`paused` 已暂停<br><br>`completed` 已结束<br><br>`sold_out` 已售罄<br><br>`off_line` 已下线 |
| data[].productLevel | string |  | 产品级别<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696747382760,
  "data": [
    {
      "productId": "12313123",
      "coin": "BGB",
      "periodType": "flexible",
      "period": "",
      "apyType": "ladder",
      "advanceRedeem": "",
      "settleMethod": "",
      "apyList": [
        {
          "rateLevel": "0",
          "minStepVal": "0.000000",
          "maxStepVal": "200.000000",
          "currentApy": "6.00"
        },
        {
          "rateLevel": "1",
          "minStepVal": "200.000000",
          "maxStepVal": "5000.000000",
          "currentApy": "50.00"
        }
      ],
      "status": "in_progress",
      "productLevel": "normal"
    }
  ]
}
```

## 简单赚币账户信息

`GET /api/v2/earn/savings/account`

限频规则: 10次/秒/UID

获取简单赚币账户信息。

Operation ID: `classicEarnSavingsGetAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcAmount | string |  | BTC计价的预估资产总值 |
| data.usdtAmount | string |  | USDT计价的预估资产总值 |
| data.btc24hEarning | string |  | BTC计价的24小时收益 |
| data.usdt24hEarning | string |  | USDT计价的24小时收益 |
| data.btcTotalEarning | string |  | BTC计价的累计收益 |
| data.usdtTotalEarning | string |  | USDT计价的累计收益 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748551073,
  "data": {
    "btcAmount": "0.35821314",
    "usdtAmount": "9481.55500000",
    "btc24hEarning": "0.00000009",
    "usdt24hEarning": "0.00263912",
    "btcTotalEarning": "0.00000761",
    "usdtTotalEarning": "0.20145653"
  }
}
```

## 简单赚币资产信息

`GET /api/v2/earn/savings/assets`

限频规则: 10次/秒/UID

获取简单赚币资产信息。

Operation ID: `classicEarnSavingsGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| startTime | query | string |  | 开始时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| idLessThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 资产列表 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].orderId | string |  | 申购记录Id<br><br>定期赎回使用 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].interestCoin | string |  | 产品派息币种 |
| data.resultList[].periodType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data.resultList[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data.resultList[].holdAmount | string |  | 当前申购数量 |
| data.resultList[].lastProfit | string |  | 昨日收益 |
| data.resultList[].totalProfit | string |  | 累计收益 |
| data.resultList[].holdDays | string |  | 目前已持有天数 |
| data.resultList[].status | string |  | 产品状态<br><br>`in_holding` 持有中 |
| data.resultList[].allowRedemption | string |  | 是否允许提前赎回<br><br>`Yes` 允许<br><br>`No` 不允许 |
| data.resultList[].productLevel | string |  | 产品等级<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |
| data.resultList[].apy | object[] |  | 阶梯利率信息 |
| data.resultList[].apy[].rateLevel | string |  | 费率级别 |
| data.resultList[].apy[].minApy | string |  | 阶梯最小金额值 |
| data.resultList[].apy[].maxApy | string |  | 阶梯最大金额值 |
| data.resultList[].apy[].currentApy | string |  | 当前阶梯年利率 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748867881,
  "data": {
    "resultList": [
      {
        "productId": "123123123",
        "orderId": "xxxx",
        "productCoin": "BGB",
        "interestCoin": "BGB",
        "periodType": "flexible",
        "period": "",
        "holdAmount": "100.000",
        "lastProfit": "0.01643800",
        "totalProfit": "1.25479000",
        "holdDays": "",
        "status": "in_holding",
        "allowRedemption": "",
        "productLevel": "normal",
        "apy": [
          {
            "rateLevel": "1",
            "minApy": "0.000000",
            "maxApy": "200.000000",
            "currentApy": "6.00"
          }
        ]
      }
    ],
    "endId": "123456789"
  }
}
```

## 简单赚币历史记录

`GET /api/v2/earn/savings/records`

限频规则: 10次/秒/UID

获取简单赚币历史记录。

Operation ID: `classicEarnSavingsGetRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 申购币种 |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| orderType | query | string |  | 记录类型<br><br>`subscribe` 申购<br><br>`redeem` 赎回<br><br>`pay_interest` 利息支付<br><br>`deduction` 罚息 (仅支持定期) |
| startTime | query | string |  | 开始时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| idLessThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 记录列表 |
| data.resultList[].orderId | string |  | 记录Id |
| data.resultList[].coinName | string |  | 产品申购币种 |
| data.resultList[].settleCoinName | string |  | 结算币种 |
| data.resultList[].productType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data.resultList[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data.resultList[].productLevel | string |  | 产品级别<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |
| data.resultList[].amount | string |  | 金额 |
| data.resultList[].ts | string |  | 创建时间 时间戳 |
| data.resultList[].orderType | string |  | 订单类型<br><br>`subscribe` 申购<br><br>`redeem` 赎回<br><br>`pay_interest` 利息支付<br><br>`deduction` 罚息 (仅支持定期) |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696749517654,
  "data": {
    "resultList": [
      {
        "orderId": "123123123123",
        "coinName": "BGB",
        "settleCoinName": "BGB",
        "productType": "flexible",
        "period": "",
        "productLevel": "normal",
        "amount": "200.000000",
        "ts": "1695797014392",
        "orderType": "redeem"
      }
    ],
    "endId": "456456456456"
  }
}
```

## 简单赚币申购详情

`GET /api/v2/earn/savings/subscribe-info`

限频规则: 10次/秒/UID

获取简单赚币申购详情。

Operation ID: `classicEarnSavingsGetSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.singleMinAmount | string |  | 单笔最小限额 |
| data.singleMaxAmount | string |  | 单笔最大限额 |
| data.remainingAmount | string |  | 持有中总额 |
| data.subscribePrecision | string |  | 申购精度 |
| data.profitPrecision | string |  | 收益精度 |
| data.subscribeTime | string |  | 申购时间，Unix毫秒时间戳 |
| data.interestTime | string |  | 起息时间，Unix毫秒时间戳 |
| data.settleTime | string |  | 派息时间，Unix毫秒时间戳 |
| data.expireTime | string |  | 到期时间，Unix毫秒时间戳 |
| data.redeemTime | string |  | 赎回时间，Unix毫秒时间戳 |
| data.settleMethod | string |  | 结算方式 |
| data.apyList | object[] |  | 阶梯利率信息 |
| data.apyList[].rateLevel | string |  | 费率级别 |
| data.apyList[].minStepVal | string |  | 阶梯最小金额值 |
| data.apyList[].maxStepVal | string |  | 阶梯最大金额值 |
| data.apyList[].currentApy | string |  | 当前阶梯年利率 |
| data.redeemDelay | string |  | 赎回到账延迟时间天数<br><br>返回值为D+1，则代表延迟一天到账，以此类推 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "singleMinAmount": "10.000000",
    "singleMaxAmount": "2000.000000",
    "remainingAmount": "4899.999990",
    "subscribePrecision": "6",
    "profitPrecision": "6",
    "subscribeTime": "1696751519451",
    "interestTime": "1696780800000",
    "settleTime": "1696867200000",
    "expireTime": "",
    "redeemTime": "",
    "settleMethod": "",
    "apyList": [
      {
        "rateLevel": "0",
        "minStepVal": "0.000000",
        "maxStepVal": "200.000000",
        "currentApy": "6.00"
      },
      {
        "rateLevel": "1",
        "minStepVal": "200.000000",
        "maxStepVal": "5000.000000",
        "currentApy": "50.00"
      }
    ],
    "redeemDelay": ""
  }
}
```

## 简单赚币申购

`POST /api/v2/earn/savings/subscribe`

限频规则: 10次/秒/UID

简单赚币申购。

Operation ID: `classicEarnSavingsSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| periodType | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购成功订单Id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1748783837837,
  "data": {
    "orderId": "1313060074239184896"
  }
}
```

## 简单赚币申购结果

`GET /api/v2/earn/savings/subscribe-result`

限频规则: 10次/秒/UID

获取简单赚币申购结果。

Operation ID: `classicEarnSavingsGetSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 申购是否成功<br><br>`success` 成功<br><br>`fail` 失败 |
| data.msg | string |  | 只有失败时才会返回信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## 简单赚币赎回

`POST /api/v2/earn/savings/redeem`

限频规则: 10次/秒/UID

简单赚币赎回。

每次赎回间隔应大于1分钟，否则可能会报错。

Operation ID: `classicEarnSavingsRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| orderId | string |  | 申购记录Id<br><br>从 assets 获取 |
| periodType | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 赎回成功订单Id |
| data.status | string |  | 订单状态 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## 简单赚币赎回结果

`GET /api/v2/earn/savings/redeem-result`

限频规则: 10次/秒/UID

获取简单赚币赎回结果。

Operation ID: `classicEarnSavingsGetRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 申购订单Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 赎回是否成功<br><br>`success` 成功<br><br>`fail` 失败 |
| data.msg | string |  | 只有失败时才会返回信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```