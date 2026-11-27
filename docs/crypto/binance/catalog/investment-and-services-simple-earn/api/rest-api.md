---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-simple-earn/api/rest-api
api_type: REST
updated_at: 2026-11-27 18:48:09.805259
---

# Simple Earn REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-simple-earn/api/rest-api/1.0.0/schema.yaml

Earn rewards by subscribing to flexible or locked Simple Earn products.

通过申购活期或定期 Simple Earn 产品赚取收益。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/bfusd/account` — Get BFUSD Account (USER_DATA)
- `GET /sapi/v1/bfusd/quota` — Get BFUSD Quota Details (USER_DATA)
- `GET /sapi/v1/bfusd/history/rateHistory` — Get BFUSD Rate History (USER_DATA)
- `GET /sapi/v1/bfusd/history/redemptionHistory` — Get BFUSD Redemption History (USER_DATA)
- `GET /sapi/v1/bfusd/history/rewardsHistory` — Get BFUSD Rewards History (USER_DATA)
- `GET /sapi/v1/bfusd/history/subscriptionHistory` — Get BFUSD subscription history (USER_DATA)
- `POST /sapi/v1/bfusd/redeem` — Redeem BFUSD (TRADE)
- `POST /sapi/v1/bfusd/subscribe` — Subscribe BFUSD (TRADE)
- `GET /sapi/v1/simple-earn/flexible/history/collateralRecord` — Get Collateral Record (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/personalLeftQuota` — Get Flexible Personal Left Quota (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/position` — Get Flexible Product Position (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/history/redemptionRecord` — Get Flexible Redemption Record (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/history/rewardsRecord` — Get Flexible Rewards History (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/subscriptionPreview` — Get Flexible Subscription Preview (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord` — Get Flexible Subscription Record (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/personalLeftQuota` — Get Locked Personal Left Quota (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/position` — Get Locked Product Position (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/history/redemptionRecord` — Get Locked Redemption Record (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/history/rewardsRecord` — Get Locked Rewards History (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/subscriptionPreview` — Get Locked Subscription Preview (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord` — Get Locked Subscription Record (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/history/rateHistory` — Get Rate History (USER_DATA)
- `GET /sapi/v1/simple-earn/flexible/list` — Get Simple Earn Flexible Product List (USER_DATA)
- `GET /sapi/v1/simple-earn/locked/list` — Get Simple Earn Locked Product List (USER_DATA)
- `POST /sapi/v1/simple-earn/flexible/redeem` — Redeem Flexible Product (TRADE)
- `POST /sapi/v1/simple-earn/locked/redeem` — Redeem Locked Product (TRADE)
- `POST /sapi/v1/simple-earn/flexible/setAutoSubscribe` — Set Flexible Auto Subscribe (USER_DATA)
- `POST /sapi/v1/simple-earn/locked/setAutoSubscribe` — Set Locked Auto Subscribe (USER_DATA)
- `POST /sapi/v1/simple-earn/locked/setRedeemOption` — Set Locked Product Redeem Option (USER_DATA)
- `GET /sapi/v1/simple-earn/account` — Simple Account (USER_DATA)
- `POST /sapi/v1/simple-earn/flexible/subscribe` — Subscribe Flexible Product (TRADE)
- `POST /sapi/v1/simple-earn/locked/subscribe` — Subscribe Locked Product (TRADE)
- `GET /sapi/v1/rwusd/account` — Get RWUSD Account (USER_DATA)
- `GET /sapi/v1/rwusd/quota` — Get RWUSD Quota Details (USER_DATA)
- `GET /sapi/v1/rwusd/history/rateHistory` — Get RWUSD Rate History (USER_DATA)
- `GET /sapi/v1/rwusd/history/redemptionHistory` — Get RWUSD Redemption History (USER_DATA)
- `GET /sapi/v1/rwusd/history/rewardsHistory` — Get RWUSD Rewards History (USER_DATA)
- `GET /sapi/v1/rwusd/history/subscriptionHistory` — Get RWUSD subscription history (USER_DATA)
- `POST /sapi/v1/rwusd/redeem` — Redeem RWUSD (TRADE)
- `POST /sapi/v1/rwusd/subscribe` — Subscribe RWUSD (TRADE)
- `GET /sapi/v1/earn/arena/activities` — Get Yield Arena Activities (USER_DATA)

## Get BFUSD Account (USER_DATA)（获取 BFUSD 账户信息 (USER_DATA)）

`GET /sapi/v1/bfusd/account`

Get BFUSD account information.

获取 BFUSD 账户信息。

Operation ID: `getBfusdAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD Account / 获取BFUSD 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bfusdAmount | string |  | 例: `100` |
| usdtProfit | string |  | 例: `11.00` |
| bfusdProfit | string |  | 例: `1.81` |

## Get BFUSD Quota Details (USER_DATA)（获取 BFUSD 配额详情 (USER_DATA)）

`GET /sapi/v1/bfusd/quota`

Get BFUSD quota details including subscription quota, fast redemption quota, and standard redemption quota.

获取 BFUSD 额度详情，包括申购额度、快速赎回额度和标准赎回额度。

Operation ID: `getBfusdQuotaDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD Quota Details / 获取 BFUSD 配额详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subscriptionQuota | object |  |  |
| subscriptionQuota.leftQuota | string |  | Maximum purchase limit in USDT<br>最大申购限额 (USDT)<br>例: `1000` |
| fastRedemptionQuota | object |  |  |
| fastRedemptionQuota.leftQuota | string |  | 例: `2` |
| fastRedemptionQuota.minimum | string |  | 例: `0.1` |
| fastRedemptionQuota.fee | string |  | 例: `0.001` |
| fastRedemptionQuota.freeQuota | string |  | 例: `100` |
| standardRedemptionQuota | object |  |  |
| standardRedemptionQuota.leftQuota | string |  | 例: `2` |
| standardRedemptionQuota.minimum | string |  | 例: `0.1` |
| standardRedemptionQuota.fee | string |  | 例: `0.0005` |
| standardRedemptionQuota.redeemPeriod | integer (int64) |  | 例: `3` |

## Get BFUSD Rate History (USER_DATA)（获取 BFUSD 利率历史 (USER_DATA)）

`GET /sapi/v1/bfusd/history/rateHistory`

Get BFUSD rate history sorted by descending order.

查询 BFUSD 利率历史，按时间降序排列。

Operation ID: `getBfusdRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD Rate History / 获取 BFUSD 利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].annualPercentageRate | string |  | BFUSD APR<br>例: `0.0418` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | string |  | 例: `1` |

## Get BFUSD Redemption History (USER_DATA)（获取 BFUSD 赎回历史 (USER_DATA)）

`GET /sapi/v1/bfusd/history/redemptionHistory`

Get BFUSD redemption history

查询 BFUSD 赎回历史记录。

Operation ID: `getBfusdRedemptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page.<br>查询页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD Redemption History / 获取 BFUSD 赎回历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BFUSD` |
| rows[].amount | string |  | 例: `51` |
| rows[].receiveAsset | string |  | 例: `USDT` |
| rows[].receiveAmount | string |  | 例: `50` |
| rows[].fee | string |  | 例: `1` |
| rows[].arrivalTime | integer (int64) |  | 例: `1575018510000` |
| rows[].status | string |  | PENDING, SUCCESS<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get BFUSD Rewards History (USER_DATA)（获取 BFUSD 收益历史 (USER_DATA)）

`GET /sapi/v1/bfusd/history/rewardsHistory`

Get BFUSD rewards history

查询 BFUSD 收益历史记录。

Operation ID: `getBfusdRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page.<br>查询页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD Rewards History / 获取 BFUSD 收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].rewardAsset | string |  | 例: `BFUSD` |
| rows[].rewardsAmount | string |  | 例: `1` |
| rows[].BFUSDPosition | string |  | 例: `100` |
| rows[].annualPercentageRate | string |  | 例: `0.0418` |
| total | integer (int64) |  | 例: `1` |

## Get BFUSD subscription history (USER_DATA)（获取 BFUSD 申购记录 (USER_DATA)）

`GET /sapi/v1/bfusd/history/subscriptionHistory`

Get BFUSD subscription history

查询 BFUSD 申购记录。

Operation ID: `getBfusdSubscriptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 枚举: `USDC`, `USDT`<br>例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page.<br>查询页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BFUSD subscription history / 获取 BFUSD 申购历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].amount | string |  | 例: `100` |
| rows[].receiveAsset | string |  | 例: `BFUSD` |
| rows[].receiveAmount | string |  | 例: `100` |
| rows[].status | string |  | 例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Redeem BFUSD (TRADE)（赎回BFUSD (TRADE)）

`POST /sapi/v1/bfusd/redeem`

Redeem BFUSD to USDT

赎回 BFUSD 获得 USDT

Operation ID: `redeemBfusd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in BFUSD<br>BFUSD数量<br>例: `1.0` |
| type | string | 是 | defaults to STANDARD<br>默认 STANDARD<br>枚举: `FAST`, `STANDARD`<br>例: `STANDARD` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem BFUSD / 赎回BFUSD

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| receiveAmount | string |  | 例: `0.23092091` |
| fee | string |  | 例: `0.00000012` |
| arrivalTime | integer (int64) |  | 例: `1575018510000` |

## Subscribe BFUSD (TRADE)（申购BFUSD (TRADE)）

`POST /sapi/v1/bfusd/subscribe`

Subscribe BFUSD

申购 BFUSD

Operation ID: `subscribeBfusd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| amount | number (float) | 是 | Amount<br>数量<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe BFUSD / 申购BFUSD

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| bfusdAmount | string |  | 例: `0.22091092` |

## Get Collateral Record (USER_DATA)（获取抵押物记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/history/collateralRecord`

Get Collateral Record

获取抵押物记录

Operation ID: `getCollateralRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string |  | 例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page.<br>查询页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Collateral Record / 获取抵押记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].amount | string |  | 例: `100.00000000` |
| rows[].productId | string |  | 例: `BUSD001` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].createTime | integer (int64) |  | 例: `1575018510000` |
| rows[].type | string |  | 例: `REPAY` |
| rows[].productName | string |  | 例: `USDT` |
| rows[].orderId | integer (int64) |  | 例: `26055` |
| total | string |  | 例: `1` |

## Get Flexible Personal Left Quota (USER_DATA)（查询活期个人剩余额度 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/personalLeftQuota`

Get Flexible Personal Left Quota

查询活期个人剩余额度

Operation ID: `getFlexiblePersonalLeftQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Personal Left Quota / 查询活期个人剩余额度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leftPersonalQuota | string |  | 例: `1000` |

## Get Flexible Product Position (USER_DATA)（获取活期产品持仓 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/position`

Get Flexible Product Position

获取活期产品持仓

Operation ID: `getFlexibleProductPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDC` |
| productId | query | string |  | 例: `1` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Product Position / 获取活期产品持仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].totalAmount | string |  | 例: `75.46000000` |
| rows[].tierAnnualPercentageRate | object |  |  |
| rows[].tierAnnualPercentageRate.0-5BTC | number (float) |  | 例: `0.05` |
| rows[].tierAnnualPercentageRate.5-10BTC | number (float) |  | 例: `0.03` |
| rows[].latestAnnualPercentageRate | string |  | 例: `0.02599895` |
| rows[].yesterdayAirdropPercentageRate | string |  | 例: `0.02599895` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].airDropAsset | string |  | 例: `BETH` |
| rows[].canRedeem | boolean |  | 例: `True` |
| rows[].collateralAmount | string |  | 例: `232.23123213` |
| rows[].productId | string |  | 例: `USDT001` |
| rows[].yesterdayRealTimeRewards | string |  | 例: `0.10293829` |
| rows[].cumulativeBonusRewards | string |  | 例: `0.22759183` |
| rows[].cumulativeRealTimeRewards | string |  | 例: `0.22759183` |
| rows[].cumulativeTotalRewards | string |  | 例: `0.45459183` |
| rows[].autoSubscribe | boolean |  | 例: `True` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Redemption Record (USER_DATA)（查询活期赎回记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`

Get Flexible Redemption Record

查询活期赎回记录

Operation ID: `getFlexibleRedemptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string |  | 例: `1` |
| redeemId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Redemption Record / 获取活期赎回记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].amount | string |  | 例: `10.54000000` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].time | integer (int64) |  | 例: `1577257222000` |
| rows[].projectId | string |  | 例: `USDT001` |
| rows[].redeemId | integer (int64) |  | 例: `40607` |
| rows[].destAccount | string |  | SPOT, FUNDING<br>例: `SPOT` |
| rows[].status | string |  | CREATED,PAID,FAILED<br>例: `PAID` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Rewards History (USER_DATA)（查询活期收益记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/history/rewardsRecord`

Get Flexible Rewards History

查询活期收益记录

Operation ID: `getFlexibleRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| type | query | string |  | `BONUS` - Bonus tiered APR, `REALTIME` - Real-time APR, `REWARDS` - Historical rewards, `ALL` - All types. Default: `ALL`<br>`BONUS` 额外分级收益, `REALTIME` 实时收益, `REWARDS` 历史收益, `ALL` 所有类型。默认: `ALL`<br>枚举: `BONUS`, `REALTIME`, `REWARDS`, `ALL`<br>例: `ALL` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Rewards History / 获取活期收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].asset | string |  | 例: `BUSD` |
| rows[].rewards | string |  | 例: `0.00006408` |
| rows[].projectId | string |  | 例: `USDT001` |
| rows[].type | string |  | 例: `BONUS` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | integer (int64) |  | 例: `2` |

## Get Flexible Subscription Preview (USER_DATA)（活期申购预览 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/subscriptionPreview`

Get Flexible Subscription Preview

活期申购预览

Operation ID: `getFlexibleSubscriptionPreview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string | 是 | 例: `1` |
| amount | query | number (float) | 是 | 例: `1.0` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Subscription Preview / 获取活期申购预览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAmount | string |  | 例: `1232.32230982` |
| rewardAsset | string |  | 例: `BUSD` |
| airDropAsset | string |  | 例: `BETH` |
| estDailyBonusRewards | string |  | 例: `0.22759183` |
| estDailyRealTimeRewards | string |  | 例: `0.22759183` |
| estDailyAirdropRewards | string |  | 例: `0.22759183` |

## Get Flexible Subscription Record (USER_DATA)（查询活期申购记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`

Get Flexible Subscription Record

查询活期申购记录

Operation ID: `getFlexibleSubscriptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string |  | 例: `1` |
| purchaseId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Subscription Record / 获取活期申购记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].amount | string |  | 例: `100.00000000` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].purchaseId | integer (int64) |  | 例: `26055` |
| rows[].productId | string |  | 例: `USDT001` |
| rows[].type | string |  | AUTO for auto subscribe, NORMAL for normal subscription, CONVERT for Locked to Flexible, LOAN for flexible loan collateral, AI for Auto Invest subscribe, TRANSFER for Locked Savings to Flexible<br>AUTO为自动申购，NORMAL为普通申购，CONVERT为定期转活期，LOAN为活期质押借币抵押物申购，AI为定投后申购，TRANSFER为币安宝定期转活期<br>例: `AUTO` |
| rows[].sourceAccount | string |  | SPOT, FUNDING, SPOTANDFUNDING<br>SPOT为现货账户, FUNDING为资金账户, SPOTANDFUNDING为现货和资金账户<br>例: `SPOT` |
| rows[].amtFromSpot | string |  | Display if sourceAccount is SPOTANDFUNDING<br>仅当sourceAccount为SPOTANDFUNDING时展示<br>例: `30` |
| rows[].amtFromFunding | string |  | Display if sourceAccount is SPOTANDFUNDING<br>仅当sourceAccount为SPOTANDFUNDING时展示<br>例: `70` |
| rows[].status | string |  | PURCHASING/SUCCESS/FAILED<br>PURCHASING 申购中/SUCCESS 申购成功/FAILED 申购失败<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get Locked Personal Left Quota (USER_DATA)（查询定期个人剩余额度 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/personalLeftQuota`

Get Locked Personal Left Quota

查询定期个人剩余额度

Operation ID: `getLockedPersonalLeftQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| projectId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Personal Left Quota / 查询锁仓个人剩余额度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leftPersonalQuota | string |  | 例: `1000` |

## Get Locked Product Position (USER_DATA)（获取定期产品持仓 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/position`

Get Locked Product Position

获取定期产品持仓

Operation ID: `getLockedProductPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDC` |
| positionId | query | string |  | 例: `1` |
| projectId | query | string |  | 例: `1` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Product Position / 获取锁仓产品持仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | integer (int64) |  | Locked position ID<br>定期订单ID<br>例: `123123` |
| rows[].parentPositionId | integer (int64) |  | Parent position ID<br>父订单ID<br>例: `123122` |
| rows[].projectId | string |  | Locked project ID<br>定期项目ID<br>例: `Axs*90` |
| rows[].asset | string |  | Locked asset<br>锁仓资产<br>例: `AXS` |
| rows[].amount | string |  | Locked Amount<br>锁仓数量<br>例: `122.09202928` |
| rows[].purchaseTime | integer (int64) |  | Subscription time<br>申购时间<br>例: `1646182276000` |
| rows[].duration | string |  | Lock period(days)<br>项目锁仓时间(天)<br>例: `60` |
| rows[].accrualDays | string |  | Accrue days<br>计息天数<br>例: `4` |
| rows[].rewardAsset | string |  | Earned asset<br>收益币种<br>例: `AXS` |
| rows[].APY | string |  | 例: `0.2032` |
| rows[].rewardAmt | string |  | Earned amount<br>收益数量<br>例: `5.17181528` |
| rows[].extraRewardAsset | string |  | Rewards assets of extra staking type<br>额外收益资产<br>例: `BNB` |
| rows[].extraRewardAPR | string |  | APR of extra staking type<br>额外收益的年化收益率<br>例: `0.0203` |
| rows[].estExtraRewardAmt | string |  | Rewards of extra staking type, distribute when order expires<br>额外收益数量，在项目到期时发放<br>例: `5.17181528` |
| rows[].boostRewardAsset | string |  | 例: `AXS` |
| rows[].boostApr | string |  | 例: `0.0121` |
| rows[].totalBoostRewardAmt | string |  | 例: `3.98201829` |
| rows[].nextPay | string |  | Next estimated rewards payment<br>下一次发放数量<br>例: `1.29295383` |
| rows[].nextPayDate | integer (int64) |  | Next rewards payment date<br>下一次发放日期<br>例: `1646697600000` |
| rows[].payPeriod | string |  | Payment cycle<br>发放周期<br>例: `1` |
| rows[].redeemAmountEarly | string |  | Early redemption amount<br>提前赎回数量<br>例: `2802.24068892` |
| rows[].rewardsEndDate | integer (int64) |  | Rewards accrual end date<br>计息结束日<br>例: `1651449600000` |
| rows[].deliverDate | integer (int64) |  | Redemption arrival time<br>赎回到账时间<br>例: `1651536000000` |
| rows[].redeemPeriod | string |  | Redemption interval<br>赎回周期<br>例: `1` |
| rows[].redeemingAmt | string |  | Amount under redemption<br>赎回中的数量<br>例: `232.2323` |
| rows[].redeemTo | string |  | Redeem to Flexible product or Spot wallet<br>赎回至活期产品或者现货钱包<br>例: `FLEXIBLE` |
| rows[].partialAmtDeliverDate | integer (int64) |  | Arrival time of partial redemption amount of order<br>部分赎回到账时间<br>例: `1651536000000` |
| rows[].canRedeemEarly | boolean |  | When it is true, early redemption can be operated<br>当为true时可以操作提前赎回<br>例: `True` |
| rows[].canFastRedemption | boolean |  | When it is true, fast redemption can be operated<br>当为true时可以操作快速赎回<br>例: `True` |
| rows[].autoSubscribe | boolean |  | When it is true, auto staking can be operated<br>当为true时可以操作自动申购<br>例: `True` |
| rows[].type | string |  | Order type is auto subscribe or normal<br>订单类型为普通或续期类型<br>例: `AUTO` |
| rows[].status | string |  | 例: `HOLDING` |
| rows[].canReStake | boolean |  | 例: `True` |
| total | integer (int64) |  | 例: `1` |

## Get Locked Redemption Record (USER_DATA)（查询定期赎回记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/history/redemptionRecord`

Get Locked Redemption Record

查询定期赎回记录

Operation ID: `getLockedRedemptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| positionId | query | string |  | 例: `1` |
| redeemId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Redemption Record / 获取锁仓赎回记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | integer (int64) |  | 例: `123123` |
| rows[].redeemId | integer (int64) |  | 例: `40607` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BNB` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].originalAmount | string |  | 例: `21312.23223` |
| rows[].type | string |  | MATURE for redeem to Spot Wallet, NEW_TRANSFERRED for redeem to Flexible product, AHEAD for early redemption<br>MATURE为赎回至现货账户，NEW_TRANSFERRED为赎回至活期产品，AHEAD为提前赎回类型<br>例: `MATURE` |
| rows[].deliverDate | integer (int64) |  | 例: `1575018510000` |
| rows[].lossAmount | string |  | Loss of profit on early redemption<br>提前赎回损失收益<br>例: `0.00001232` |
| rows[].isComplete | boolean |  | 例: `True` |
| rows[].rewardAsset | string |  | 例: `AXS` |
| rows[].rewardAmt | string |  | 例: `5.17181528` |
| rows[].extraRewardAsset | string |  | 例: `BNB` |
| rows[].estExtraRewardAmt | string |  | 例: `5.17181528` |
| rows[].status | string |  | 例: `PAID` |
| total | integer (int64) |  | 例: `1` |

## Get Locked Rewards History (USER_DATA)（查询定期收益记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/history/rewardsRecord`

Get Locked Rewards History

查询定期收益记录

Operation ID: `getLockedRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| positionId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Rewards History / 获取锁仓收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | integer (int64) |  | 例: `123123` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BNB` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].type | string |  | 例: `Locked Rewards` |
| total | integer (int64) |  | 例: `1` |

## Get Locked Subscription Preview (USER_DATA)（定期申购预览 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/subscriptionPreview`

Get Locked Subscription Preview

定期申购预览

Operation ID: `getLockedSubscriptionPreview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| projectId | query | string | 是 | 例: `1` |
| amount | query | number (float) | 是 | 例: `1.0` |
| autoSubscribe | query | boolean |  | default true.<br>默认true<br>例: `True` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Subscription Preview / 获取锁仓申购预览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].rewardAsset | string |  | 例: `AXS` |
| [].totalRewardAmt | string |  | 例: `5.17181528` |
| [].extraRewardAsset | string |  | 例: `BNB` |
| [].estTotalExtraRewardAmt | string |  | 例: `5.17181528` |
| [].boostRewardAsset | string |  | 例: `AXS` |
| [].estDailyRewardAmt | string |  | 例: `1.20928901` |
| [].nextPay | string |  | 例: `1.29295383` |
| [].nextPayDate | integer (int64) |  | 例: `1646697600000` |
| [].valueDate | integer (int64) |  | 例: `1646697600000` |
| [].rewardsEndDate | integer (int64) |  | 例: `1651449600000` |
| [].deliverDate | integer (int64) |  | 例: `1651536000000` |
| [].nextSubscriptionDate | integer (int64) |  | 例: `1651536000000` |

## Get Locked Subscription Record (USER_DATA)（查询定期申购记录 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`

Get Locked Subscription Record

查询定期申购记录

Operation ID: `getLockedSubscriptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| purchaseId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Locked Subscription Record / 获取锁仓申购记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | integer (int64) |  | 例: `123123` |
| rows[].purchaseId | string |  | 例: `26055` |
| rows[].projectId | string |  | 例: `Axs*90` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BNB` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].type | string |  | NORMAL for normal subscription, AUTO for auto-subscription order, ACTIVITY for activity order, TRIAL for trial fund order, RESTAKE for restake order<br>NORMAL为普通申购，AUTO为自动续期，ACTIVITY为活动类型申购，TRIAL为体验金申购，RESTAKE为续申购活动<br>例: `AUTO` |
| rows[].sourceAccount | string |  | SPOT, FUNDING, SPOTANDFUNDING<br>SPOT为现货账户, FUNDING为资金账户, SPOTANDFUNDING为现货和资金账户<br>例: `SPOT` |
| rows[].amtFromSpot | string |  | Display if sourceAccount is SPOTANDFUNDING<br>仅当sourceAccount为SPOTANDFUNDING时展示<br>例: `30` |
| rows[].amtFromFunding | string |  | Display if sourceAccount is SPOTANDFUNDING<br>仅当sourceAccount为SPOTANDFUNDING时展示<br>例: `70` |
| rows[].status | string |  | PURCHASING/SUCCESS/FAILED<br>PURCHASING 申购中/SUCCESS 申购成功/FAILED申购失败<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get Rate History (USER_DATA)（获取利率历史 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/history/rateHistory`

Get Rate History

获取利率历史

Operation ID: `getRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| productId | query | string | 是 | 例: `1` |
| aprPeriod | query | string |  | 枚举: `DAY`, `YEAR`<br>默认: `DAY`<br>例: `DAY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>查询页码<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page<br>每页返回数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Rate History / 获取利率 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].productId | string |  | 例: `BUSD001` |
| rows[].asset | string |  | 例: `BUSD` |
| rows[].annualPercentageRate | string |  | 例: `0.00006408` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | string |  | 例: `1` |

## Get Simple Earn Flexible Product List (USER_DATA)（查询赚币活期产品列表 (USER_DATA)）

`GET /sapi/v1/simple-earn/flexible/list`

Get available Simple Earn flexible product list

查询赚币活期产品列表

Operation ID: `getSimpleEarnFlexibleProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDC` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Simple Earn Flexible Product List / 获取 Simple Earn 活期产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].asset | string |  | 例: `BTC` |
| rows[].latestAnnualPercentageRate | string |  | 例: `0.05000000` |
| rows[].tierAnnualPercentageRate | object |  |  |
| rows[].tierAnnualPercentageRate.0-5BTC | number (float) |  | 例: `0.05` |
| rows[].tierAnnualPercentageRate.5-10BTC | number (float) |  | 例: `0.03` |
| rows[].airDropPercentageRate | string |  | 例: `0.05000000` |
| rows[].canPurchase | boolean |  | 例: `True` |
| rows[].canRedeem | boolean |  | 例: `True` |
| rows[].isSoldOut | boolean |  | 例: `True` |
| rows[].hot | boolean |  | 例: `True` |
| rows[].minPurchaseAmount | string |  | 例: `0.01000000` |
| rows[].productId | string |  | 例: `BTC001` |
| rows[].subscriptionStartTime | integer (int64) |  | 例: `1646182276000` |
| rows[].status | string |  | PREHEATING,PURCHASING,END<br>PREHEATING预热,PURCHASING申购中,END申购结束<br>例: `PURCHASING` |
| total | integer (int64) |  | 例: `1` |

## Get Simple Earn Locked Product List (USER_DATA)（查询赚币定期产品列表 (USER_DATA)）

`GET /sapi/v1/simple-earn/locked/list`

Get Simple Earn Locked Product List

查询赚币定期产品列表

Operation ID: `getSimpleEarnLockedProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDC` |
| current | query | integer (int64) |  | Currently querying page. Starts from 1.<br>查询页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Simple Earn Locked Product List / 获取 Simple Earn 锁仓产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].projectId | string |  | 例: `Axs*90` |
| rows[].detail | object |  |  |
| rows[].detail.asset | string |  | 例: `AXS` |
| rows[].detail.rewardAsset | string |  | 例: `AXS` |
| rows[].detail.duration | integer (int64) |  | 例: `90` |
| rows[].detail.renewable | boolean |  | 例: `True` |
| rows[].detail.isSoldOut | boolean |  | 例: `True` |
| rows[].detail.apr | string |  | 例: `1.2069` |
| rows[].detail.status | string |  | 例: `CREATED` |
| rows[].detail.subscriptionStartTime | integer (int64) |  | 例: `1646182276000` |
| rows[].detail.extraRewardAsset | string |  | 例: `BNB` |
| rows[].detail.extraRewardAPR | string |  | 例: `0.23` |
| rows[].detail.boostRewardAsset | string |  | 例: `AXS` |
| rows[].detail.boostApr | string |  | 例: `0.0121` |
| rows[].detail.boostEndTime | integer (int64) |  | 例: `1646182276000` |
| rows[].quota | object |  |  |
| rows[].quota.totalPersonalQuota | string |  | 例: `2` |
| rows[].quota.minimum | string |  | 例: `0.001` |
| total | integer (int64) |  | 例: `1` |

## Redeem Flexible Product (TRADE)（赎回活期产品 (TRADE)）

`POST /sapi/v1/simple-earn/flexible/redeem`

Redeem Flexible Product

赎回活期产品

Operation ID: `redeemFlexibleProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 例: `1` |
| redeemAll | boolean |  | 默认: `False`<br>例: `False` |
| amount | number (float) |  | if redeemAll is false, amount is mandatory<br>当 redeemAll 为 false 时，amount 为必填<br>例: `1.0` |
| destAccount | string |  | 枚举: `SPOT`, `FUND`<br>默认: `SPOT`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem Flexible Product / 赎回活期产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| redeemId | integer (int64) |  | 例: `40607` |
| success | boolean |  | 例: `True` |

## Redeem Locked Product (TRADE)（赎回定期产品 (TRADE)）

`POST /sapi/v1/simple-earn/locked/redeem`

Redeem Locked Product

赎回定期产品

Operation ID: `redeemLockedProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | Locked product position ID<br>定期产品持仓 ID<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem Locked Product / 赎回定期产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| redeemId | integer (int64) |  | 例: `40607` |
| success | boolean |  | 例: `True` |

## Set Flexible Auto Subscribe (USER_DATA)（设置活期自动申购 (USER_DATA)）

`POST /sapi/v1/simple-earn/flexible/setAutoSubscribe`

Set Flexible Auto Subscribe

为活期产品设置自动申购功能

Operation ID: `setFlexibleAutoSubscribe`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 例: `1` |
| autoSubscribe | boolean | 是 | 例: `True` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Flexible Auto Subscribe / 设置活期自动申购

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Set Locked Auto Subscribe (USER_DATA)（设置定期自动申购 (USER_DATA)）

`POST /sapi/v1/simple-earn/locked/setAutoSubscribe`

Set locked auto subscribe

为定期产品设置自动申购功能

Operation ID: `setLockedAutoSubscribe`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | 例: `1` |
| autoSubscribe | boolean | 是 | 例: `True` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Locked Auto Subscribe / 设置锁仓自动申购

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Set Locked Product Redeem Option (USER_DATA)（设置定期赎回目标账户 (USER_DATA)）

`POST /sapi/v1/simple-earn/locked/setRedeemOption`

Set redeem option for Locked product

为定期产品设置赎回目标账户，现货钱包或活期产品

Operation ID: `setLockedProductRedeemOption`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | 例: `1` |
| redeemTo | string | 是 | 枚举: `SPOT`, `FLEXIBLE`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Locked Product Redeem Option / 设置锁仓产品赎回选项

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Simple Account (USER_DATA)（赚币账户 (USER_DATA)）

`GET /sapi/v1/simple-earn/account`

Simple Account query

赚币账户

Operation ID: `simpleAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Simple Account / Simple 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAmountInBTC | string |  | 例: `0.01067982` |
| totalAmountInUSDT | string |  | 例: `77.13289230` |
| totalFlexibleAmountInBTC | string |  | 例: `0.00000000` |
| totalFlexibleAmountInUSDT | string |  | 例: `0.00000000` |
| totalLockedInBTC | string |  | 例: `0.01067982` |
| totalLockedInUSDT | string |  | 例: `77.13289230` |

## Subscribe Flexible Product (TRADE)（申购活期产品 (TRADE)）

`POST /sapi/v1/simple-earn/flexible/subscribe`

Subscribe Flexible Product

申购活期产品

Operation ID: `subscribeFlexibleProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 例: `1` |
| amount | number (float) | 是 | 例: `1.0` |
| autoSubscribe | boolean |  | 默认: `True`<br>例: `True` |
| sourceAccount | string |  | 枚举: `SPOT`, `FUND`, `ALL`<br>默认: `SPOT`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe Flexible Product / 申购活期产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| purchaseId | integer (int64) |  | 例: `40607` |
| success | boolean |  | 例: `True` |

## Subscribe Locked Product (TRADE)（申购定期产品 (TRADE)）

`POST /sapi/v1/simple-earn/locked/subscribe`

Subscribe Locked Product

申购定期产品

Operation ID: `subscribeLockedProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 例: `1` |
| amount | number (float) | 是 | 例: `1.0` |
| autoSubscribe | boolean |  | 默认: `False`<br>例: `False` |
| sourceAccount | string |  | 枚举: `SPOT`, `FUND`, `ALL`<br>默认: `SPOT`<br>例: `SPOT` |
| redeemTo | string |  | 枚举: `SPOT`, `FLEXIBLE`<br>默认: `SPOT`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe Locked Product / 申购锁仓产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| purchaseId | integer (int64) |  | 例: `40607` |
| positionId | string |  | 例: `12345` |
| success | boolean |  | 例: `True` |

## Get RWUSD Account (USER_DATA)（获取 RWUSD 账户信息 (USER_DATA)）

`GET /sapi/v1/rwusd/account`

Get RWUSD account information.

获取 RWUSD 账户信息。

Operation ID: `getRwusdAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD Account / 获取RWUSD 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rwusdAmount | string |  | 例: `100` |
| totalProfit | string |  | 例: `12.81` |

## Get RWUSD Quota Details (USER_DATA)（获取 RWUSD 配额详情 (USER_DATA)）

`GET /sapi/v1/rwusd/quota`

Get RWUSD quota details including subscription quota, fast redemption quota, and standard redemption quota.

获取 RWUSD 额度详情，包括申购额度、快速赎回额度和标准赎回额度。

Operation ID: `getRwusdQuotaDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD Quota Details / 获取 RWUSD 配额详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subscriptionQuota | object |  |  |
| subscriptionQuota.assets | string[] |  |  |
| subscriptionQuota.leftQuota | string |  | 例: `1000` |
| subscriptionQuota.minimum | string |  | 例: `0.10000000` |
| fastRedemptionQuota | object |  |  |
| fastRedemptionQuota.leftQuota | string |  | 例: `2` |
| fastRedemptionQuota.minimum | string |  | 例: `0.1` |
| fastRedemptionQuota.fee | string |  | 例: `0.0005` |
| fastRedemptionQuota.freeQuota | string |  | 例: `100` |
| standardRedemptionQuota | object |  |  |
| standardRedemptionQuota.leftQuota | string |  | 例: `2` |
| standardRedemptionQuota.minimum | string |  | 例: `0.1` |
| standardRedemptionQuota.fee | string |  | 例: `0.001` |
| standardRedemptionQuota.redeemPeriod | integer (int64) |  | 例: `3` |
| subscribeEnable | boolean |  | 例: `True` |
| redeemEnable | boolean |  | 例: `True` |

## Get RWUSD Rate History (USER_DATA)（获取 RWUSD 利率历史 (USER_DATA)）

`GET /sapi/v1/rwusd/history/rateHistory`

Get RWUSD rate history sorted by descending order.

查询 RWUSD 利率历史，按时间降序排列。

Operation ID: `getRwusdRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>查询页码，从 1 开始。默认值：1<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page<br>每页返回数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD Rate History / 获取 RWUSD 利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].annualPercentageRate | string |  | 例: `0.0418` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | string |  | 例: `1` |

## Get RWUSD Redemption History (USER_DATA)（获取 RWUSD 赎回历史 (USER_DATA)）

`GET /sapi/v1/rwusd/history/redemptionHistory`

Get RWUSD redemption history.

查询 RWUSD 赎回历史记录。

Operation ID: `getRwusdRedemptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>查询页码<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page<br>每页返回数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD Redemption History / 获取 RWUSD 赎回历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `RWUSD` |
| rows[].amount | string |  | 例: `51` |
| rows[].receiveAsset | string |  | 例: `USDC` |
| rows[].receiveAmount | string |  | 例: `50` |
| rows[].fee | string |  | 例: `1` |
| rows[].arrivalTime | integer (int64) |  | 例: `1575018510000` |
| rows[].status | string |  | PENDING, SUCCESS<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get RWUSD Rewards History (USER_DATA)（获取 RWUSD 收益历史 (USER_DATA)）

`GET /sapi/v1/rwusd/history/rewardsHistory`

Get RWUSD rewards history.

查询 RWUSD 收益历史记录。

Operation ID: `getRwusdRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>查询页码<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page<br>每页返回数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD Rewards History / 获取 RWUSD 收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].rewardsAmount | string |  | 例: `1` |
| rows[].rwusdPosition | string |  | 例: `100` |
| rows[].annualPercentageRate | string |  | 例: `0.0418` |
| total | integer (int64) |  | 例: `1` |

## Get RWUSD subscription history (USER_DATA)（获取 RWUSD 申购记录 (USER_DATA)）

`GET /sapi/v1/rwusd/history/subscriptionHistory`

Get RWUSD subscription history

查询 RWUSD 申购记录。

Operation ID: `getRwusdSubscriptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 枚举: `USDC`, `USDT`<br>例: `USDC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>查询页码<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page<br>每页返回数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000 (ms)<br>请求有效时间，单位为毫秒，且不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get RWUSD subscription history / 获取 RWUSD 申购历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `USDC` |
| rows[].amount | string |  | 例: `100` |
| rows[].receiveAsset | string |  | 例: `RWUSD` |
| rows[].receiveAmount | string |  | 例: `100` |
| rows[].status | string |  | 例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Redeem RWUSD (TRADE)（赎回RWUSD (TRADE)）

`POST /sapi/v1/rwusd/redeem`

Redeem RWUSD to USDC

赎回 RWUSD 获得 USDC

Operation ID: `redeemRwusd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in RWUSD<br>RWUSD数量<br>例: `1.0` |
| type | string | 是 | 枚举: `FAST`, `STANDARD`<br>默认: `STANDARD`<br>例: `STANDARD` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem RWUSD / 赎回RWUSD

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| receiveAmount | string |  | 例: `0.23092091` |
| fee | string |  | 例: `0.00000012` |
| arrivalTime | integer (int64) |  | 例: `1575018510000` |

## Subscribe RWUSD (TRADE)（申购RWUSD (TRADE)）

`POST /sapi/v1/rwusd/subscribe`

Subscribe RWUSD

申购 RWUSD

Operation ID: `subscribeRwusd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 枚举: `USDT`, `USDC`<br>例: `USDC` |
| amount | number (float) | 是 | Amount<br>数量<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe RWUSD / 申购RWUSD

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| rwusdAmount | string |  | 例: `0.22091092` |

## Get Yield Arena Activities (USER_DATA)（查询收益竞技场活动列表 (USER_DATA)）

`GET /sapi/v1/earn/arena/activities`

Get the list of Earn Yield Arena giveaway activities currently available to the user.

查询当前用户可参与的理财收益竞技场活动列表。

Operation ID: `getYieldArenaActivities`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| lang | header | string |  | Locale tag for `title` and `description` (e.g. `en`, `zh-CN`, `pt-BR`). Default: `en`.<br>If the value is missing, malformed, or has no translation configured, content is returned in `en`.<br>语言标签，用于指定 `title` 和 `description` 返回的语言（如 `en`、`zh-CN`、`pt-BR`）。默认值：`en`。<br>如果未传、值无法识别或对应语言暂未配置翻译，则返回英文（`en`）内容。<br>例: `en` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Yield Arena Activities / 收益竞技场活动列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| activities | object[] |  |  |
| activities[].activityId | integer (int64) |  | Activity ID.<br>活动 ID。<br>例: `10001` |
| activities[].activityType | string |  | Activity category: `AIRDROP`, `LEADERBOARD`, or `EVENT`.<br>活动类型：`AIRDROP`（空投）、`LEADERBOARD`（排行榜）、`EVENT`（通用活动）。<br>枚举: `AIRDROP`, `LEADERBOARD`, `EVENT`<br>例: `AIRDROP` |
| activities[].title | string |  | Activity title, localized via the `lang` header.<br>活动标题，按 `lang` 请求头返回对应语言。<br>例: `Hold FDUSD & Earn BNB Airdrop` |
| activities[].description | string |  | Activity description, localized via the `lang` header.<br>活动描述，按 `lang` 请求头返回对应语言。<br>例: `Subscribe to FDUSD Flexible and earn bonus BNB airdrop.` |
| activities[].rewardPoolInUsd | string |  | USD value of the reward pool.<br>奖金池的 USD 价值。<br>例: `50000` |
| activities[].rewardToken | string[] |  | Reward token symbols (e.g. `["BNB"]`); may be empty.<br>奖励代币（如 `["BNB"]`），可能为空。 |
| activities[].redirectUrl | string |  | Web URL to the activity landing page.<br>活动页面链接（Web）。<br>例: `https://www.binance.com/en/earn/arena/airdrop-123` |
| activities[].startTime | integer (int64) |  | Activity start time in milliseconds; may be null for activities that are immediately effective.<br>活动开始时间（毫秒），立即生效的活动可能为空。<br>例: `1713052800000` |
| activities[].endTime | integer (int64) |  | Activity end time in milliseconds; may be null for activities with no fixed end.<br>活动结束时间（毫秒），长期有效的活动可能为空。<br>例: `1713657600000` |