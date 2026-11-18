---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-broker-commission
api_type: REST
updated_at: 2026-11-18 08:37:33.553477
---

# Classic Broker Commission API

Classic account — broker order commission and rebate queries.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/broker/total-commission` — Get Total Commission
- `GET /api/v3/broker/total-commission` — Get Total Commission
- `GET /api/v3/broker/order-commission` — Get Order Commission
- `GET /api/v3/broker/rebate-info` — Get Rebate Info
- `GET /api/v2/broker/order-commission` — Get Order Commission
- `GET /api/v2/broker/rebate-info` — Get Rebate Info

## Get Total Commission

`GET /api/v2/broker/total-commission`

Rate limit: 20/sec/UID

Data retention: 365 days

Historical data available from: 2025/6/1

Data granularity: daily

Data update granularity: daily, previous day’s data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both left unset

This API supports retrieving data within the past 365 days (data is available starting from 2025/6/1 at the earliest)

If startTime and endTime are not set in the request, the default returned information will be for yesterday (00:00-23:

  59 UTC+8)

Data update frequency: T+1 (UTC+8)

Operation ID: `classicBrokerCommissionGetTotalCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | Commission date |
| data[].totalTradingVolume | string |  | Broker’s total trading volume for the day |
| data[].totalActiveTraders | string |  | Number of active traders for the broker that day |
| data[].totalCommission | string |  | Total commission earned by the broker (USDT) |
| data[].spot | object |  | Spot data |
| data[].spot.spotTradingVolume | string |  | Spot trading volume (USDT) |
| data[].spot.spotTradingFee | string |  | Actual spot trading fee collected (USDT) |
| data[].spot.spotPureTradingFee | string |  | Net spot trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation) |
| data[].spot.spotCommission | string |  | Spot commission (USDT) |
| data[].futures | object |  | Futures data |
| data[].futures.futuresTradingVolume | string |  | Futures trading volume (USDT) |
| data[].futures.futuresTradingFee | string |  | Actual futures trading fee collected (USDT) |
| data[].futures.futuresPureTradingFee | string |  | Net futures trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation） |
| data[].futures.futuresCommission | string |  | Futures commission (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```

## Get Total Commission

`GET /api/v3/broker/total-commission`

Rate limit: 20/sec/UID

Data retention: 365 days

Historical data available from: 2025/6/1

Data granularity: daily

Data update granularity: daily, previous day’s data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both left unset

This API supports retrieving data within the past 365 days (data is available starting from 2025/6/1 at the earliest)

If startTime and endTime are not set in the request, the default returned information will be for yesterday (00:00-23:

  59 UTC+8)

Data update frequency: T+1 (UTC+8)

Operation ID: `classicBrokerCommissionGetTotalCommissionV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | Commission date |
| data[].totalTradingVolume | string |  | Broker’s total trading volume for the day |
| data[].totalActiveTraders | string |  | Number of active traders for the broker that day |
| data[].totalCommission | string |  | Total commission earned by the broker (USDT) |
| data[].spot | object |  | Spot data |
| data[].spot.spotTradingVolume | string |  | Spot trading volume (USDT) |
| data[].spot.spotTradingFee | string |  | Actual spot trading fee collected (USDT) |
| data[].spot.spotPureTradingFee | string |  | Net spot trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation) |
| data[].spot.spotCommission | string |  | Spot commission (USDT) |
| data[].futures | object |  | Futures data |
| data[].futures.futuresTradingVolume | string |  | Futures trading volume (USDT) |
| data[].futures.futuresTradingFee | string |  | Actual futures trading fee collected (USDT) |
| data[].futures.futuresPureTradingFee | string |  | Net futures trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation） |
| data[].futures.futuresCommission | string |  | Futures commission (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```

## Get Order Commission

`GET /api/v3/broker/order-commission`

Rate limit: 20/sec/UID

Data storage: 30 days

Historical data backtracking: 2025/9/1

Data granularity: daily

Data update frequency: daily, previous day's data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both not set

The maximum time span supported for startTime and endTime is 30 days

This API supports retrieving data within the past 30 days

If startTime and endTime are not set in the request, the default return will be information for yesterday (00:00-23:59

  UTC+8)

This API data is updated on a T+1 basis

Transaction details only show those marked with broker channel id

Operation ID: `classicBrokerCommissionGetOrderCommissionV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| limit | query | string |  | Pagination limit. Maximum: 500, Default: 500 |
| uid | query | string |  | UID |
| orderid | query | string |  | Order ID |
| idLessThan | query | string |  | Cursor ID for pagination. Do not pass this parameter for the first request; for subsequent requests, use the endId value from the previous response to paginate. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | Rebate (commission) list |
| data.commissionlist[].fillId | string |  | Fill ID |
| data.commissionlist[].orderId | string |  | Order ID |
| data.commissionlist[].ts | string |  | Fill timestamp |
| data.commissionlist[].clientOid | string |  | Custom order ID |
| data.commissionlist[].bizType | string |  | Transaction type<br><br>`spot`Spot<br><br>`futures`Futures |
| data.commissionlist[].subBizType | string |  | Sub-transaction type<br><br>`spot_trade`Spot trading<br><br>`spot_margin`Spot margin<br><br>`usdt_futures`usdt futures<br><br>`coin_futures`coin futures<br><br>`usdc_futures`usdc futures |
| data.commissionlist[].symbol | string |  | Symbol |
| data.commissionlist[].volume | string |  | Trade amount<br><br> unit: USDT, with full precision |
| data.commissionlist[].fee | string |  | Total fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].pureFee | string |  | Net fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].rebateAmount | string |  | Broker commission<br><br>unit: USDT, with full precision |
| data.endId | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## Get Rebate Info

`GET /api/v3/broker/rebate-info`

Rate limit: 20/sec/UID

Data retention: 30 days

Real-time data

Operation ID: `classicBrokerCommissionGetRebateInfoV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | Type of rebate relationship<br><br>`affiliate`Client channel<br><br>`official` Official (website) channel |
| data.userLevel | string |  | User level<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | Spot trading rebate ratio available to the user |
| data.clientFuturesRebateRatio | string |  | Futures trading rebate ratio available to the user |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```

## Get Order Commission

`GET /api/v2/broker/order-commission`

Rate limit: 20/sec/UID

Data storage: 30 days

Historical data backtracking: 2025/9/1

Data granularity: daily

Data update frequency: daily, previous day's data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both not set

The maximum time span supported for startTime and endTime is 30 days

This API supports retrieving data within the past 30 days

If startTime and endTime are not set in the request, the default return will be information for yesterday (00:00-23:59

  UTC+8)

This API data is updated on a T+1 basis

Transaction details only show those marked with broker channel id

Operation ID: `classicBrokerCommissionGetOrderCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| limit | query | string |  | Pagination limit. Maximum: 500, Default: 500 |
| uid | query | string |  | UID |
| orderid | query | string |  | Order ID |
| idLessThan | query | string |  | Cursor ID for pagination. Do not pass this parameter for the first request; for subsequent requests, use the endId value from the previous response to paginate. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | Rebate (commission) list |
| data.commissionlist[].fillId | string |  | Fill ID |
| data.commissionlist[].orderId | string |  | Order ID |
| data.commissionlist[].ts | string |  | Fill timestamp |
| data.commissionlist[].clientOid | string |  | Custom order ID |
| data.commissionlist[].bizType | string |  | Transaction type<br><br>`spot`Spot<br><br>`futures`Futures |
| data.commissionlist[].subBizType | string |  | Sub-transaction type<br><br>`spot_trade`Spot trading<br><br>`spot_margin`Spot margin<br><br>`usdt_futures`usdt futures<br><br>`coin_futures`coin futures<br><br>`usdc_futures`usdc futures |
| data.commissionlist[].symbol | string |  | Symbol |
| data.commissionlist[].volume | string |  | Trade amount<br><br> unit: USDT, with full precision |
| data.commissionlist[].fee | string |  | Total fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].pureFee | string |  | Net fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].rebateAmount | string |  | Broker commission<br><br>unit: USDT, with full precision |
| data.endId | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## Get Rebate Info

`GET /api/v2/broker/rebate-info`

Rate limit: 20/sec/UID

Data retention: 30 days

Real-time data

Operation ID: `classicBrokerCommissionGetRebateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | Type of rebate relationship<br><br>`affiliate`Client channel<br><br>`official` Official (website) channel |
| data.userLevel | string |  | User level<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | Spot trading rebate ratio available to the user |
| data.clientFuturesRebateRatio | string |  | Futures trading rebate ratio available to the user |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```


---

经典账户 — 经纪商订单佣金与返佣查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/broker/order-commission` — 获取经纪商订单返佣数据
- `GET /api/v3/broker/rebate-info` — 获取用户的经纪商返佣信息
- `GET /api/v3/broker/total-commission` — 获取经纪商佣金数据
- `GET /api/v2/broker/order-commission` — 获取经纪商订单返佣数据
- `GET /api/v2/broker/rebate-info` — 获取用户的经纪商返佣信息
- `GET /api/v2/broker/total-commission` — 获取经纪商佣金数据

## 获取经纪商订单返佣数据

`GET /api/v3/broker/order-commission`

限速规则 20次/1s (UID)

数据存储：30天

历史数据回溯：2025/9/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为30天

该接口支持获取30天内数据

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

该接口数据更新信息是T+1的

成交明细只展示broker channel id标记的成交明细信息

Operation ID: `classicBrokerCommissionGetOrderCommissionV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| limit | query | string |  | 分页限制 最大:500,默认: 500 |
| uid | query | string |  | 查询用户的uid |
| orderid | query | string |  | 订单id |
| idLessThan | query | string |  | 游标ID<br><br> 用于分页<br><br>首次不传。后续传参上次响应的endId进行翻页 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | 返佣列表 |
| data.commissionlist[].fillId | string |  | 成交ID |
| data.commissionlist[].orderId | string |  | 订单id |
| data.commissionlist[].ts | string |  | 成交时间 |
| data.commissionlist[].clientOid | string |  | 自定义订单ID |
| data.commissionlist[].bizType | string |  | 交易类型<br><br>`spot`现货<br><br>`futures`合约 |
| data.commissionlist[].subBizType | string |  | 子交易类型<br><br>`spot_trade`现货币币<br><br>`spot_margin`现货杠杆<br><br>`usdt_futures`U本位合约<br><br>`coin_futures`币本位合约<br><br>`usdc_futures`USDC合约 |
| data.commissionlist[].symbol | string |  | 交易对 |
| data.commissionlist[].volume | string |  | 交易金额<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].fee | string |  | 总手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].pureFee | string |  | 净手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].rebateAmount | string |  | 经纪商佣金<br><br>单位：USDT，精度不截断 |
| data.endId | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## 获取用户的经纪商返佣信息

`GET /api/v3/broker/rebate-info`

限速规则 20次/1s (UID)

数据存储：30天

实时的数据

Operation ID: `classicBrokerCommissionGetRebateInfoV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | 用户的uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | 返佣关系的情况<br><br>`affiliate`客户渠道<br><br>`official` 官网渠道 |
| data.userLevel | string |  | 用户等级用户等级<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | 交易用户可获取现货返佣比例 |
| data.clientFuturesRebateRatio | string |  | 交易用户可获取合约返佣比例 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```

## 获取经纪商佣金数据

`GET /api/v3/broker/total-commission`

限速规则 20次/1s (UID)

数据存储：365天

历史数据回溯：2025/6/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

该接口支持获取365天内数据（最早提供2025/6/1起的数据）

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

数据更新频率：T+1 (UTC +8)

Operation ID: `classicBrokerCommissionGetTotalCommissionV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | 返佣日期 |
| data[].totalTradingVolume | string |  | 经纪商当日交易量 |
| data[].totalActiveTraders | string |  | 经纪商当日交易人数 |
| data[].totalCommission | string |  | 经纪商总返佣（USDT） |
| data[].spot | object |  | 现货数据 |
| data[].spot.spotTradingVolume | string |  | 现货交易量（USDT） |
| data[].spot.spotTradingFee | string |  | 现货实际收取手续费（USDT） |
| data[].spot.spotPureTradingFee | string |  | 现货净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].spot.spotCommission | string |  | 现货返佣（USDT） |
| data[].futures | object |  | 合约数据 |
| data[].futures.futuresTradingVolume | string |  | 合约交易量（USDT） |
| data[].futures.futuresTradingFee | string |  | 合约实际收取手续费（USDT） |
| data[].futures.futuresPureTradingFee | string |  | 合约净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].futures.futuresCommission | string |  | 合约返佣（USDT） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```

## 获取经纪商订单返佣数据

`GET /api/v2/broker/order-commission`

限速规则 20次/1s (UID)

数据存储：30天

历史数据回溯：2025/9/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为30天

该接口支持获取30天内数据

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

该接口数据更新信息是T+1的

成交明细只展示broker channel id标记的成交明细信息

Operation ID: `classicBrokerCommissionGetOrderCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| limit | query | string |  | 分页限制 最大:500,默认: 500 |
| uid | query | string |  | 查询用户的uid |
| orderid | query | string |  | 订单id |
| idLessThan | query | string |  | 游标ID<br><br> 用于分页<br><br>首次不传。后续传参上次响应的endId进行翻页 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | 返佣列表 |
| data.commissionlist[].fillId | string |  | 成交ID |
| data.commissionlist[].orderId | string |  | 订单id |
| data.commissionlist[].ts | string |  | 成交时间 |
| data.commissionlist[].clientOid | string |  | 自定义订单ID |
| data.commissionlist[].bizType | string |  | 交易类型<br><br>`spot`现货<br><br>`futures`合约 |
| data.commissionlist[].subBizType | string |  | 子交易类型<br><br>`spot_trade`现货币币<br><br>`spot_margin`现货杠杆<br><br>`usdt_futures`U本位合约<br><br>`coin_futures`币本位合约<br><br>`usdc_futures`USDC合约 |
| data.commissionlist[].symbol | string |  | 交易对 |
| data.commissionlist[].volume | string |  | 交易金额<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].fee | string |  | 总手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].pureFee | string |  | 净手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].rebateAmount | string |  | 经纪商佣金<br><br>单位：USDT，精度不截断 |
| data.endId | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## 获取用户的经纪商返佣信息

`GET /api/v2/broker/rebate-info`

限速规则 20次/1s (UID)

数据存储：30天

实时的数据

Operation ID: `classicBrokerCommissionGetRebateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | 用户的uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | 返佣关系的情况<br><br>`affiliate`客户渠道<br><br>`official` 官网渠道 |
| data.userLevel | string |  | 用户等级用户等级<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | 交易用户可获取现货返佣比例 |
| data.clientFuturesRebateRatio | string |  | 交易用户可获取合约返佣比例 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```

## 获取经纪商佣金数据

`GET /api/v2/broker/total-commission`

限速规则 20次/1s (UID)

数据存储：365天

历史数据回溯：2025/6/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

该接口支持获取365天内数据（最早提供2025/6/1起的数据）

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

数据更新频率：T+1 (UTC +8)

Operation ID: `classicBrokerCommissionGetTotalCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | 返佣日期 |
| data[].totalTradingVolume | string |  | 经纪商当日交易量 |
| data[].totalActiveTraders | string |  | 经纪商当日交易人数 |
| data[].totalCommission | string |  | 经纪商总返佣（USDT） |
| data[].spot | object |  | 现货数据 |
| data[].spot.spotTradingVolume | string |  | 现货交易量（USDT） |
| data[].spot.spotTradingFee | string |  | 现货实际收取手续费（USDT） |
| data[].spot.spotPureTradingFee | string |  | 现货净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].spot.spotCommission | string |  | 现货返佣（USDT） |
| data[].futures | object |  | 合约数据 |
| data[].futures.futuresTradingVolume | string |  | 合约交易量（USDT） |
| data[].futures.futuresTradingFee | string |  | 合约实际收取手续费（USDT） |
| data[].futures.futuresPureTradingFee | string |  | 合约净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].futures.futuresCommission | string |  | 合约返佣（USDT） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```