---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn-classic-sharkfin
api_type: REST
updated_at: 2026-11-24 19:02:18.135270
---

# Classic Earn SharkFin

Classic account SharkFin product, subscription, and record APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/sharkfin/product` — Get Sharkfin Products
- `GET /api/v2/earn/sharkfin/account` — SharkFin Account
- `GET /api/v2/earn/sharkfin/assets` — SharkFin Assets
- `GET /api/v2/earn/sharkfin/records` — SharkFin Records
- `GET /api/v2/earn/sharkfin/subscribe-info` — SharkFin Subscription Detail
- `POST /api/v2/earn/sharkfin/subscribe` — Subscribe SharkFin
- `GET /api/v2/earn/sharkfin/subscribe-result` — SharkFin Subscription Result

## Get Sharkfin Products

`GET /api/v2/earn/sharkfin/product`

Rate limit: 10/sec/UID

Get sharkfin products.

Operation ID: `classicEarnSharkfinGetProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Shark coin |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Sharkfin product list info |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].productName | string |  | Sharkfin product name |
| data.resultList[].productCoin | string |  | Sharkfin product coin |
| data.resultList[].subscribeCoin | string |  | Sharkfin Subscribe coin |
| data.resultList[].farmingStartTime | string |  | Start time, Unix millisecond timestamp |
| data.resultList[].farmingEndTime | string |  | End time, Unix millisecond timestamp |
| data.resultList[].lowerRate | string |  | Minimum rate |
| data.resultList[].defaultRate | string |  | Default rate |
| data.resultList[].upperRate | string |  | Maximum rate |
| data.resultList[].period | string |  | Investment period |
| data.resultList[].interestStartTime | string |  | Interest calculation start time |
| data.resultList[].status | string |  | Product status<br><br>`not_started` Warming up<br><br>`in_progress` Subscribing<br><br>`paused` Paused<br><br>`interest_pending` Interest is accruing<br><br>`settle_pending` Pending settlement<br><br>`settled` Settled<br><br>`redeemed` redeemed<br><br>`sold_out` Sold out |
| data.resultList[].minAmount | string |  | Product minimum limit |
| data.resultList[].limitAmount | string |  | Product limit<br><br>If there is no limit, return `unlimited` |
| data.resultList[].soldAmount | string |  | Sold amount |
| data.resultList[].startTime | string |  | Start timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.resultList[].endTime | string |  | End timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696754489003,
  "data": {
    "resultList": [
      {
        "productId": "1",
        "productName": "USDT/ETH_20231009",
        "productCoin": "ETH",
        "subscribeCoin": "USDT",
        "farmingStartTime": "1696744800000",
        "farmingEndTime": "1696831200000",
        "lowerRate": "7.06",
        "defaultRate": "7",
        "upperRate": "8.8",
        "period": "7",
        "interestStartTime": "1696838400000",
        "status": "in_progress",
        "minAmount": "0.1",
        "limitAmount": "500001.0",
        "soldAmount": "310187.2",
        "endTime": "1696831200000",
        "startTime": "1696744800000"
      }
    ],
    "endId": "1"
  }
}
```

## SharkFin Account

`GET /api/v2/earn/sharkfin/account`

Rate limit: 10/sec/UID

Get sharkfin account info.

Operation ID: `classicEarnSharkfinGetAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcSubscribeAmount | string |  | Estimated total asset value in BTC |
| data.usdtSubscribeAmount | string |  | Estimated total asset value in USDT |
| data.btcHistoricalAmount | string |  | 24-hour earning in BTC |
| data.usdtHistoricalAmount | string |  | 24-hour earning in USDT |
| data.btcTotalEarning | string |  | Cumulative earning in BTC |
| data.usdtTotalEarning | string |  | Cumulative earning in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696755312297,
  "data": {
    "btcSubscribeAmount": "0.00000000",
    "usdtSubscribeAmount": "0.00",
    "btcHistoricalAmount": "0.00000000",
    "usdtHistoricalAmount": "0.00000000",
    "btcTotalEarning": "0.00000000",
    "usdtTotalEarning": "0.00000000"
  }
}
```

## SharkFin Assets

`GET /api/v2/earn/sharkfin/assets`

Rate limit: 10/sec/UID

Get sharkfin assets.

Operation ID: `classicEarnSharkfinGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| status | query | string | 是 | Shark status<br><br>`subscribed` Subscribed(default)<br><br>`settled` Settled |
| startTime | query | string |  | Start timestamp<br><br>(Sharkfin creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Sharkfin creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Sharkfin product list info |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].interestStartTime | string |  | Interest accrual start time |
| data.resultList[].interestEndTime | string |  | Interest accrual end time |
| data.resultList[].productCoin | string |  | Product subscription coin |
| data.resultList[].subscribeCoin | string |  | Subscription coin |
| data.resultList[].trend | string |  | Trend<br><br>`up` rise<br><br>`down` fall |
| data.resultList[].settleTime | string |  | Settlement time, Unix millisecond timestamp |
| data.resultList[].interestAmount | string |  | Interest amount |
| data.resultList[].productStatus | string |  | Product status<br><br>`running` Subscription<br><br>`pause` has been suspended<br><br>`wait_interest` is pending<br><br>`wait_settle` is pending settlement<br><br>`settle` has been settled<br><br>`redeem` has been redeemed<br><br>`sell_out` sold out |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696756316611,
  "data": {
    "resultList": [
      {
        "productId": "12312313",
        "interestStartTime": "1697199180000",
        "interestEndTime": "1697803980000",
        "productCoin": "BTC",
        "subscribeCoin": "USDT",
        "trend": "up",
        "settleTime": "1697803980000",
        "interestAmount": "",
        "productStatus": "running"
      }
    ],
    "endId": "456456456"
  }
}
```

## SharkFin Records

`GET /api/v2/earn/sharkfin/records`

Rate limit: 10/sec/UID

Get sharkfin records.

Operation ID: `classicEarnSharkfinGetRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Subscribe coin |
| type | query | string | 是 | Transaction type<br><br>`subscription` subscription<br><br>`redemption` redemption<br><br>`interest` interest payment |
| startTime | query | string |  | Start timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Record list |
| data.resultList[].orderId | string |  | RecordId |
| data.resultList[].product | string |  | Sharkfin productName |
| data.resultList[].period | string |  | Investment period |
| data.resultList[].amount | string |  | Subscribe amount |
| data.resultList[].ts | string |  | Create timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.resultList[].type | string |  | Transaction type<br><br>`subscription` subscription<br><br>`redemption` redemption<br><br>`interest` interest payment |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757048457,
  "data": {
    "resultList": [
      {
        "orderId": "1",
        "product": "USDT/BTC_20231013",
        "period": "7",
        "amount": "100.00000000",
        "ts": "1696756278760",
        "type": "subscription"
      }
    ],
    "endId": "1"
  }
}
```

## SharkFin Subscription Detail

`GET /api/v2/earn/sharkfin/subscribe-info`

Rate limit: 10/sec/UID

Get subscription detail before subscribe sharkfin.

Operation ID: `classicEarnSharkfinGetSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productCoin | string |  | Product coin |
| data.subscribeCoin | string |  | Subscribe coin |
| data.interestTime | string |  | Interest start date in Unix timestamp format (in milliseconds) |
| data.expirationTime | string |  | Settlement time Unix timestamp format in milliseconds |
| data.minPrice | string |  | Minimum price of price range |
| data.currentPrice | string |  | Current price |
| data.maxPrice | string |  | The maximum price of the price range |
| data.minRate | string |  | Minimum rate |
| data.defaultRate | string |  | Default rate |
| data.maxRate | string |  | Maximum rate |
| data.period | string |  | Investment period |
| data.productMinAmount | string |  | Product minimum limit |
| data.availableBalance | string |  | Available Balance |
| data.userAmount | string |  | User quota |
| data.remainingAmount | string |  | Remaining balance |
| data.profitPrecision | string |  | Interest calculation scale |
| data.subscribePrecision | string |  | Subscribe calculation scale |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757209022,
  "data": {
    "productCoin": "BTC",
    "subscribeCoin": "USDT",
    "interestTime": "1697199180000",
    "expirationTime": "1697803980000",
    "minPrice": "28000.00",
    "currentPrice": "30211.23",
    "maxPrice": "32000.00",
    "minRate": "5.00",
    "defaultRate": "1.00",
    "maxRate": "20.00",
    "period": "7",
    "productMinAmount": "0.00100000",
    "availableBalance": "788",
    "userAmount": "500.00000000",
    "remainingAmount": "400.00000000",
    "profitPrecision": "8",
    "subscribePrecision": "8"
  }
}
```

## Subscribe SharkFin

`POST /api/v2/earn/sharkfin/subscribe`

Rate limit: 10/sec/UID

Subscribe sharkfin.

Operation ID: `classicEarnSharkfinSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| amount | string | 是 | Subscription amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order Id |
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

## SharkFin Subscription Result

`GET /api/v2/earn/sharkfin/subscribe-result`

Rate limit: 5/sec/UID

Get sharkfin subscription result.

Operation ID: `classicEarnSharkfinGetSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Is the subscription successful<br><br>`success` Success<br><br>`fail` Fail |
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

经典账户鲨鱼鳍产品、申购与记录接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/sharkfin/product` — 鲨鱼鳍产品列表
- `GET /api/v2/earn/sharkfin/account` — 鲨鱼鳍账户信息
- `GET /api/v2/earn/sharkfin/assets` — 鲨鱼鳍资产信息
- `GET /api/v2/earn/sharkfin/records` — 鲨鱼鳍历史记录
- `GET /api/v2/earn/sharkfin/subscribe-info` — 鲨鱼鳍申购详情
- `POST /api/v2/earn/sharkfin/subscribe` — 鲨鱼鳍申购
- `GET /api/v2/earn/sharkfin/subscribe-result` — 鲨鱼鳍申购结果

## 鲨鱼鳍产品列表

`GET /api/v2/earn/sharkfin/product`

限频规则: 10次/秒/UID

获取鲨鱼鳍产品列表。

Operation ID: `classicEarnSharkfinGetProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种 |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| idLessThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 鲨鱼鳍产品信息 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].productName | string |  | 产品名称 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].subscribeCoin | string |  | 派息币种 |
| data.resultList[].farmingStartTime | string |  | 开始时间，Unix毫秒时间戳 |
| data.resultList[].farmingEndTime | string |  | 停止时间，Unix毫秒时间戳 |
| data.resultList[].lowerRate | string |  | 费率最小值 |
| data.resultList[].defaultRate | string |  | 费率默认值 |
| data.resultList[].upperRate | string |  | 费率最大值 |
| data.resultList[].period | string |  | 投资期限 |
| data.resultList[].interestStartTime | string |  | 计息开始时间 |
| data.resultList[].status | string |  | 产品状态<br><br>`not_started` 预热中<br><br>`in_progress` 申购中<br><br>`paused` 已暂停<br><br>`interest_pending` 计息中<br><br>`settle_pending` 待结算<br><br>`settled` 已结算<br><br>`redeemed` 已赎回<br><br>`sold_out` 已售罄 |
| data.resultList[].minAmount | string |  | 产品最小限额 |
| data.resultList[].limitAmount | string |  | 产品额度<br><br>若无限制则返回 `unlimited` |
| data.resultList[].soldAmount | string |  | 已售额度 |
| data.resultList[].startTime | string |  | 开始时间<br><br>Unix时间戳的毫秒数格式 |
| data.resultList[].endTime | string |  | 结束时间<br><br>Unix时间戳的毫秒数格式 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696754489003,
  "data": {
    "resultList": [
      {
        "productId": "1",
        "productName": "USDT/ETH_20231009",
        "productCoin": "ETH",
        "subscribeCoin": "USDT",
        "farmingStartTime": "1696744800000",
        "farmingEndTime": "1696831200000",
        "lowerRate": "7.06",
        "defaultRate": "7",
        "upperRate": "8.8",
        "period": "7",
        "interestStartTime": "1696838400000",
        "status": "in_progress",
        "minAmount": "0.1",
        "limitAmount": "500001.0",
        "soldAmount": "310187.2",
        "endTime": "1696831200000",
        "startTime": "1696744800000"
      }
    ],
    "endId": "1"
  }
}
```

## 鲨鱼鳍账户信息

`GET /api/v2/earn/sharkfin/account`

限频规则: 10次/秒/UID

获取鲨鱼鳍账户信息。

Operation ID: `classicEarnSharkfinGetAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcSubscribeAmount | string |  | BTC计价的预估资产总值 |
| data.usdtSubscribeAmount | string |  | USDT计价的预估资产总值 |
| data.btcHistoricalAmount | string |  | BTC计价的24小时收益 |
| data.usdtHistoricalAmount | string |  | USDT计价的24小时收益 |
| data.btcTotalEarning | string |  | BTC计价的累计收益 |
| data.usdtTotalEarning | string |  | USDT计价的累计收益 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696755312297,
  "data": {
    "btcSubscribeAmount": "0.00000000",
    "usdtSubscribeAmount": "0.00",
    "btcHistoricalAmount": "0.00000000",
    "usdtHistoricalAmount": "0.00000000",
    "btcTotalEarning": "0.00000000",
    "usdtTotalEarning": "0.00000000"
  }
}
```

## 鲨鱼鳍资产信息

`GET /api/v2/earn/sharkfin/assets`

限频规则: 10次/秒/UID

获取鲨鱼鳍资产信息。

Operation ID: `classicEarnSharkfinGetAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| status | query | string | 是 | 鲨鱼鳍状态<br><br>`subscribed` 已申购(默认)<br><br>`settled` 已结算 |
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
| data.resultList | object[] |  | 鲨鱼鳍产品信息 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].interestStartTime | string |  | 计息开始时间 |
| data.resultList[].interestEndTime | string |  | 计息结束时间 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].subscribeCoin | string |  | 派息币种 |
| data.resultList[].trend | string |  | 趋势<br><br>`up` 涨<br><br>`down` 跌 |
| data.resultList[].settleTime | string |  | 结算时间，Unix毫秒时间戳 |
| data.resultList[].interestAmount | string |  | 收益 |
| data.resultList[].productStatus | string |  | 产品状态<br><br>`running` 申购中<br><br>`pause` 已暂停<br><br>`wait_interest` 待起息<br><br>`wait_settle` 待结算<br><br>`settle` 已结算<br><br>`redeem` 已赎回<br><br>`sell_out` 已售罄 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696756316611,
  "data": {
    "resultList": [
      {
        "productId": "12312313",
        "interestStartTime": "1697199180000",
        "interestEndTime": "1697803980000",
        "productCoin": "BTC",
        "subscribeCoin": "USDT",
        "trend": "up",
        "settleTime": "1697803980000",
        "interestAmount": "",
        "productStatus": "running"
      }
    ],
    "endId": "456456456"
  }
}
```

## 鲨鱼鳍历史记录

`GET /api/v2/earn/sharkfin/records`

限频规则: 10次/秒/UID

获取鲨鱼鳍历史记录。

Operation ID: `classicEarnSharkfinGetRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 申购币种 |
| type | query | string | 是 | 交易类型<br><br>`subscription` 申购<br><br>`redemption` 赎回<br><br>`interest` 利息派付 |
| startTime | query | string |  | 开始时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
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
| data.resultList[].product | string |  | 产品名称 |
| data.resultList[].period | string |  | 期限时长 |
| data.resultList[].amount | string |  | 金额 |
| data.resultList[].ts | string |  | 创建时间 时间戳 |
| data.resultList[].type | string |  | 交易类型<br><br>`subscription` 申购<br><br>`redemption` 赎回<br><br>`interest` 利息派付 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757048457,
  "data": {
    "resultList": [
      {
        "orderId": "1",
        "product": "USDT/BTC_20231013",
        "period": "7",
        "amount": "100.00000000",
        "ts": "1696756278760",
        "type": "subscription"
      }
    ],
    "endId": "1"
  }
}
```

## 鲨鱼鳍申购详情

`GET /api/v2/earn/sharkfin/subscribe-info`

限频规则: 10次/秒/UID

获取鲨鱼鳍申购详情。

Operation ID: `classicEarnSharkfinGetSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productCoin | string |  | 产品币种 |
| data.subscribeCoin | string |  | 申购币种 |
| data.interestTime | string |  | 起息日期 Unix时间戳的毫秒数格式 |
| data.expirationTime | string |  | 结算时间 Unix时间戳的毫秒数格式 |
| data.minPrice | string |  | 价格区间的最小价格 |
| data.currentPrice | string |  | 当前价格 |
| data.maxPrice | string |  | 价格区间的最大价格 |
| data.minRate | string |  | 派费率最小值 |
| data.defaultRate | string |  | 费率默认值 |
| data.maxRate | string |  | 费率最大值 |
| data.period | string |  | 投资期限 |
| data.productMinAmount | string |  | 产品最小限额 |
| data.availableBalance | string |  | 可用余额 |
| data.userAmount | string |  | 单人额度 |
| data.remainingAmount | string |  | 剩余额度 |
| data.profitPrecision | string |  | 计息精度 |
| data.subscribePrecision | string |  | 申购金额精度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757209022,
  "data": {
    "productCoin": "BTC",
    "subscribeCoin": "USDT",
    "interestTime": "1697199180000",
    "expirationTime": "1697803980000",
    "minPrice": "28000.00",
    "currentPrice": "30211.23",
    "maxPrice": "32000.00",
    "minRate": "5.00",
    "defaultRate": "1.00",
    "maxRate": "20.00",
    "period": "7",
    "productMinAmount": "0.00100000",
    "availableBalance": "788",
    "userAmount": "500.00000000",
    "remainingAmount": "400.00000000",
    "profitPrecision": "8",
    "subscribePrecision": "8"
  }
}
```

## 鲨鱼鳍申购

`POST /api/v2/earn/sharkfin/subscribe`

限频规则: 10次/秒/UID

鲨鱼鳍申购。

Operation ID: `classicEarnSharkfinSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购成功订单Id |
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

## 鲨鱼鳍申购结果

`GET /api/v2/earn/sharkfin/subscribe-result`

限频规则: 5次/秒/UID

获取鲨鱼鳍申购结果。

Operation ID: `classicEarnSharkfinGetSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单Id |

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