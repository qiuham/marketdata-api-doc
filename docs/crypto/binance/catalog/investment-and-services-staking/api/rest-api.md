---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-staking/api/rest-api
api_type: REST
updated_at: 2026-11-20 18:50:41.072783
---

# Staking REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-staking/api/rest-api/1.0.0/schema.yaml

Subscribe to staking products, track positions, and query rewards via the Binance Staking API.

通过 Binance Staking API 申购质押产品、跟踪持仓并查询奖励。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v2/eth-staking/account` — ETH Staking account (USER_DATA)
- `GET /sapi/v1/eth-staking/eth/quota` — Get current ETH staking quota (USER_DATA)
- `GET /sapi/v1/eth-staking/eth/history/redemptionHistory` — Get ETH redemption history (USER_DATA)
- `GET /sapi/v1/eth-staking/eth/history/stakingHistory` — Get ETH staking history (USER_DATA)
- `GET /sapi/v1/eth-staking/eth/history/rateHistory` — Get WBETH Rate History (USER_DATA)
- `GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory` — Get WBETH rewards history (USER_DATA)
- `GET /sapi/v1/eth-staking/wbeth/history/unwrapHistory` — Get WBETH unwrap history (USER_DATA)
- `GET /sapi/v1/eth-staking/wbeth/history/wrapHistory` — Get WBETH wrap history (USER_DATA)
- `POST /sapi/v1/eth-staking/eth/redeem` — Redeem ETH (TRADE)
- `POST /sapi/v2/eth-staking/eth/stake` — Subscribe ETH Staking (TRADE)
- `POST /sapi/v1/eth-staking/wbeth/wrap` — Wrap BETH (TRADE)
- `GET /sapi/v1/onchain-yields/locked/personalLeftQuota` — Get On-chain Yields Locked Personal Left Quota (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/list` — Get On-chain Yields Locked Product List (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/position` — Get On-chain Yields Locked Product Position (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/history/redemptionRecord` — Get On-chain Yields Locked Redemption Record (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/history/rewardsRecord` — Get On-chain Yields Locked Rewards History (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/subscriptionPreview` — Get On-chain Yields Locked Subscription Preview (USER_DATA)
- `GET /sapi/v1/onchain-yields/locked/history/subscriptionRecord` — Get On-chain Yields Locked Subscription Record (USER_DATA)
- `GET /sapi/v1/onchain-yields/account` — On-chain Yields Account (USER_DATA)
- `POST /sapi/v1/onchain-yields/locked/redeem` — Redeem On-chain Yields Locked Product (TRADE)
- `POST /sapi/v1/onchain-yields/locked/setAutoSubscribe` — Set On-chain Yields Locked Auto Subscribe (USER_DATA)
- `POST /sapi/v1/onchain-yields/locked/setRedeemOption` — Set On-chain Yields Locked Product Redeem Option (USER_DATA)
- `POST /sapi/v1/onchain-yields/locked/subscribe` — Subscribe On-chain Yields Locked Product (TRADE)
- `GET /sapi/v1/soft-staking/list` — Get Soft Staking Product List (USER_DATA)
- `GET /sapi/v1/soft-staking/history/rewardsRecord` — Get Soft Staking Rewards History (USER_DATA)
- `GET /sapi/v1/soft-staking/set` — Set Soft Staking (USER_DATA)
- `POST /sapi/v1/sol-staking/sol/claim` — Claim Boost Rewards (TRADE)
- `GET /sapi/v1/sol-staking/sol/history/rateHistory` — Get BNSOL Rate History (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory` — Get BNSOL rewards history (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory` — Get Boost Rewards History (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/history/redemptionHistory` — Get SOL redemption history (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/history/stakingHistory` — Get SOL staking history (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/quota` — Get SOL staking quota details (USER_DATA)
- `GET /sapi/v1/sol-staking/sol/history/unclaimedRewards` — Get Unclaimed Rewards (USER_DATA)
- `POST /sapi/v1/sol-staking/sol/redeem` — Redeem SOL (TRADE)
- `GET /sapi/v1/sol-staking/account` — SOL Staking account (USER_DATA)
- `POST /sapi/v1/sol-staking/sol/stake` — Subscribe SOL Staking (TRADE)

## ETH Staking account (USER_DATA)（ETH质押账户 (USER_DATA)）

`GET /sapi/v2/eth-staking/account`

ETH Staking account

ETH质押账户

Operation ID: `ethStakingAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：ETH Staking account / ETH 质押账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| holdingInETH | string |  | 例: `1.22330928` |
| holdings | object |  |  |
| holdings.wbethAmount | string |  | 例: `1.10928781` |
| holdings.bethAmount | string |  | 例: `1.90002112` |
| thirtyDaysProfitInETH | string |  | 例: `0.22330928` |
| profit | object |  |  |
| profit.amountFromWBETH | string |  | 例: `0.12330928` |
| profit.amountFromBETH | string |  | 例: `0.1` |

## Get current ETH staking quota (USER_DATA)（查询当前ETH质押限额 (USER_DATA)）

`GET /sapi/v1/eth-staking/eth/quota`

Get current ETH staking quota

查询当前ETH质押限额

Operation ID: `getCurrentEthStakingQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get current ETH staking quota / 获取当前 ETH 质押限额

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leftStakingPersonalQuota | string |  | Show min (Daily available limit, total personal staking quota)<br>显示最小值（日可用限额，总个人质押限额）<br>例: `1000` |
| leftRedemptionPersonalQuota | string |  | Show min (Daily personal redeem quota, total redemption limit)<br>显示最小值（日个人赎回限额，总赎回限额）<br>例: `1000` |
| minStakeAmount | string |  | 例: `0.00010000` |
| minRedeemAmount | string |  | 例: `0.00000001` |
| redeemPeriod | integer (int64) |  | 例: `20` |
| stakeable | boolean |  | 例: `True` |
| redeemable | boolean |  | 例: `True` |
| commissionFee | string |  | 例: `0.05000000` |
| calculating | boolean |  | 例: `False` |

## Get ETH redemption history (USER_DATA)（查询ETH赎回记录 (USER_DATA)）

`GET /sapi/v1/eth-staking/eth/history/redemptionHistory`

Get ETH redemption history

查询ETH赎回记录

Operation ID: `getEthRedemptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| redeemId | query | integer (int64) |  | 例: `1234567` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get ETH redemption history / 获取 ETH 赎回历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].arrivalTime | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `WBETH` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].distributeAsset | string |  | 例: `ETH` |
| rows[].distributeAmount | string |  | 例: `21338.0699` |
| rows[].conversionRatio | string |  | 例: `1.00121234` |
| rows[].status | string |  | PENDING,SUCCESS,FAILED<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get ETH staking history (USER_DATA)（查询ETH质押记录 (USER_DATA)）

`GET /sapi/v1/eth-staking/eth/history/stakingHistory`

Get ETH staking history

查询ETH质押记录

Operation ID: `getEthStakingHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| purchaseId | query | integer (int64) |  | 例: `1234567` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get ETH staking history / 获取 ETH 质押历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `ETH` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].distributeAsset | string |  | 例: `WBETH` |
| rows[].distributeAmount | string |  | 例: `21286.42584` |
| rows[].conversionRatio | string |  | 例: `1.00121234` |
| rows[].status | string |  | PENDING,SUCCESS,FAILED<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get WBETH Rate History (USER_DATA)（查询WBETH汇率历史 (USER_DATA)）

`GET /sapi/v1/eth-staking/eth/history/rateHistory`

Get WBETH Rate History

查询WBETH汇率历史

Operation ID: `getWbethRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get WBETH Rate History / 获取 WBETH 利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].annualPercentageRate | string |  | BETH APR<br>例: `0.00006408` |
| rows[].exchangeRate | string |  | BETH value per 1 WBETH<br>1 WBETH等价的BETH数量<br>例: `1.00121234` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | string |  | 例: `1` |

## Get WBETH rewards history (USER_DATA)（查询WBETH收益历史 (USER_DATA)）

`GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory`

Get WBETH rewards history

查询WBETH收益历史

Operation ID: `getWbethRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get WBETH rewards history / 获取 WBETH 收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| estRewardsInETH | string |  | 例: `1.23230920` |
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].amountInETH | string |  | Estimated rewards accrued within WBETH<br>预估累计在WBETH中的收益<br>例: `0.23223` |
| rows[].holding | string |  | WBETH holding balance<br>WBETH持仓<br>例: `2.3223` |
| rows[].holdingInETH | string |  | 例: `2.4231` |
| rows[].annualPercentageRate | string |  | 例: `0.5` |
| total | integer (int64) |  | 例: `1` |

## Get WBETH unwrap history (USER_DATA)（查询WBETH去封装记录 (USER_DATA)）

`GET /sapi/v1/eth-staking/wbeth/history/unwrapHistory`

Get WBETH unwrap history

查询WBETH去封装记录

Operation ID: `getWbethUnwrapHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get WBETH unwrap history / 获取 WBETH 去封装历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].fromAsset | string |  | 例: `WBETH` |
| rows[].fromAmount | string |  | 例: `21312.23223` |
| rows[].toAsset | string |  | 例: `BETH` |
| rows[].toAmount | string |  | 例: `21312.23223` |
| rows[].exchangeRate | string |  | BETH value per 1 WBETH<br>例: `1.01243253` |
| rows[].status | string |  | PENDING,SUCCESS,FAILED<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get WBETH wrap history (USER_DATA)（查询WBETH封装记录 (USER_DATA)）

`GET /sapi/v1/eth-staking/wbeth/history/wrapHistory`

Get WBETH wrap history

查询WBETH封装记录

Operation ID: `getWbethWrapHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get WBETH wrap history / 获取 WBETH 封装历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].fromAsset | string |  | 例: `BETH` |
| rows[].fromAmount | string |  | 例: `21312.23223` |
| rows[].toAsset | string |  | 例: `WBETH` |
| rows[].toAmount | string |  | 例: `21312.23223` |
| rows[].exchangeRate | string |  | BETH amount per 1 WBETH<br>每1个WBETH对应BETH数量<br>例: `1.01243253` |
| rows[].status | string |  | PENDING,SUCCESS,FAILED<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Redeem ETH (TRADE)（赎回ETH (TRADE)）

`POST /sapi/v1/eth-staking/eth/redeem`

Redeem WBETH or BETH and get ETH

赎回WBETH或BETH并获得ETH

Operation ID: `redeemEth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in BETH, limit 8 decimals<br>BETH 数量，限制8位小数<br>例: `1.0` |
| asset | string |  | 枚举: `WBETH`, `BETH`<br>默认: `BETH`<br>例: `BETH` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem ETH / 赎回ETH

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| ethAmount | string |  | 例: `0.23092091` |
| redeemId | integer (int64) |  | 例: `1234567` |
| conversionRatio | string |  | 例: `1.00121234` |
| arrivalTime | integer (int64) |  | 例: `1575018510000` |

## Subscribe ETH Staking (TRADE)（质押ETH (TRADE)）

`POST /sapi/v2/eth-staking/eth/stake`

Subscribe ETH Staking

质押ETH

Operation ID: `subscribeEthStaking`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in ETH, limit 4 decimals<br>ETH 数量，限制4位小数<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe ETH Staking / 申购 ETH 质押

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| wbethAmount | string |  | 例: `0.23092091` |
| purchaseId | integer (int64) |  | 例: `1234567` |
| conversionRatio | string |  | ETH amount per 1 WBETH<br>每1WBETH对应ETH的数量<br>例: `1.001212342342` |

## Wrap BETH (TRADE)（封装BETH (TRADE)）

`POST /sapi/v1/eth-staking/wbeth/wrap`

Wrap BETH

封装BETH

Operation ID: `wrapBeth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in BETH, limit 4 decimals<br>BETH 数量，限制 4 位小数<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Wrap BETH / 封装BETH

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| wbethAmount | string |  | 例: `0.23092091` |
| exchangeRate | string |  | 例: `1.001212343432` |

## Get On-chain Yields Locked Personal Left Quota (USER_DATA)（查询链上赚币定期个人剩余额度 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/personalLeftQuota`

Get On-chain Yields Locked Personal Left Quota

查询链上赚币定期个人剩余额度

Operation ID: `getOnChainYieldsLockedPersonalLeftQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| projectId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Personal Left Quota / 查询链上收益锁仓个人剩余额度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leftPersonalQuota | string |  | 例: `1000` |

## Get On-chain Yields Locked Product List (USER_DATA)（查询链上赚币定期产品列表 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/list`

Get available On-chain Yields Locked product list

查询链上赚币定期产品列表

Operation ID: `getOnChainYieldsLockedProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `SOL` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Product List / 获取链上收益锁仓产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].projectId | string |  | 例: `Solv-60d` |
| rows[].detail | object |  |  |
| rows[].detail.asset | string |  | Lock up asset<br>锁仓资产<br>例: `BTC` |
| rows[].detail.rewardAsset | string |  | Earn Asset<br>收益资产<br>例: `SOLV` |
| rows[].detail.duration | integer (int64) |  | Lock period(days)<br>锁仓周期（天）<br>例: `60` |
| rows[].detail.renewable | boolean |  | Project supports renewal (auto-subscribe when maturity)<br>项目支持续期锁仓<br>例: `True` |
| rows[].detail.isSoldOut | boolean |  | 例: `True` |
| rows[].detail.apr | string |  | 0.039 stands for 3.9%<br>例: `0.039` |
| rows[].detail.status | string |  | PREHEATING,PURCHASING<br>PREHEATING:预热中,PURCHASING:申购中<br>例: `PREHEATING` |
| rows[].detail.subscriptionStartTime | integer (int64) |  | 例: `1646182276000` |
| rows[].detail.canRedeemToFlex | boolean |  | Whether redemption to simple earn flexible is supported.<br>是否支持赎回到赚币活期<br>例: `True` |
| rows[].quota | object |  |  |
| rows[].quota.totalPersonalQuota | string |  | Total Personal quota<br>个人总额度<br>例: `2` |
| rows[].quota.minimum | string |  | Minimum amount per order<br>单笔最小申购额度<br>例: `0.001` |
| total | integer (int64) |  | 例: `1` |

## Get On-chain Yields Locked Product Position (USER_DATA)（获取链上赚币定期产品持仓 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/position`

Get On-chain Yields Locked Product Position

获取链上赚币定期产品持仓

Operation ID: `getOnChainYieldsLockedProductPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| positionId | query | string |  | 例: `1` |
| projectId | query | string |  | 例: `1` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results per page.<br>每页返回数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Product Position / 获取链上收益锁仓产品持仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | string |  | Locked position ID<br>定期订单ID<br>例: `123123` |
| rows[].projectId | string |  | Locked project ID<br>定期项目ID<br>例: `Solv-60d` |
| rows[].asset | string |  | Locked asset<br>锁仓资产<br>例: `BTC` |
| rows[].amount | string |  | Locked Amount<br>锁仓数量<br>例: `122.09202928` |
| rows[].purchaseTime | string |  | Subscription time<br>申购时间<br>例: `1646182276000` |
| rows[].duration | string |  | Lock period(days)<br>项目锁仓时间(天)<br>例: `60` |
| rows[].accrualDays | string |  | Accrue days<br>计息天数<br>例: `4` |
| rows[].rewardAsset | string |  | Earned asset<br>收益资产<br>例: `SOLV` |
| rows[].APY | string |  | 例: `0.039` |
| rows[].rewardAmt | string |  | Earned amount<br>收益数量<br>例: `5.17181528` |
| rows[].nextPay | string |  | Next estimated rewards payment<br>下次发放数量<br>例: `1.29295383` |
| rows[].nextPayDate | string |  | Next rewards payment date<br>下次发放日期<br>例: `1646697600000` |
| rows[].payPeriod | string |  | Payment cycle<br>发放周期<br>例: `1` |
| rows[].rewardsPayDate | string |  | Rewards payment date when maturity<br>产品到期后收益发放日期<br>例: `1646697600000` |
| rows[].rewardsEndDate | string |  | Rewards accrual end date<br>计息结束日<br>例: `1651449600000` |
| rows[].deliverDate | string |  | Redemption arrival time(include early redemption or natural maturity; if auto-subscribe is on, not response this one)<br>赎回到账日期(包括提前赎回和到期赎回；如果自动申购打开，不会返回这条)<br>例: `1651536000000` |
| rows[].nextSubscriptionDate | string |  | Response when auto-subscribe on<br>自动申购打开时返回<br>例: `1651536000000` |
| rows[].redeemingAmt | string |  | Amount under redemption when auto-subsceibe is on but left quota is less than stake amount<br>赎回中的数量，自动申购时，剩余额度不足全额申购时返回<br>例: `232.2323` |
| rows[].redeemTo | string |  | Redeem to simple earn Flexible product or Spot wallet, "SPOT":spot wallet<br>赎回到赚币活期或者现货钱包，SPOT：现货钱包<br>例: `FLEXIBLE` |
| rows[].canRedeemEarly | boolean |  | When it is true, early redemption can be operated<br>为true时可提前赎回<br>例: `True` |
| rows[].autoSubscribe | boolean |  | When it is true, auto subscribe can be operated<br>为true时可以操作自动申购<br>例: `True` |
| rows[].type | string |  | AUTO：auto-subscribe order； NORMAL：normal-subscribe order<br>AUTO：自动申购类型； NORMAL：普通申购类型<br>例: `AUTO` |
| rows[].status | string |  | HOLDING,REDEEMING,RENEWING:auto subscribing,NEW_TRANSFERRING:Redeeming to Simple Earn flexible<br>HOLDING,REDEEMING,RENEWING:自动申购中,NEW_TRANSFERRING:正在赎回到赚币活期<br>例: `HOLDING` |
| total | integer (int64) |  | 例: `1` |

## Get On-chain Yields Locked Redemption Record (USER_DATA)（查询链上赚币定期赎回记录 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/history/redemptionRecord`

Get On-chain Yields Locked Redemption Record

查询链上赚币定期赎回记录

Operation ID: `getOnChainYieldsLockedRedemptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| positionId | query | string |  | 例: `1` |
| redeemId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Redemption Record / 获取链上收益锁仓赎回记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | string |  | 例: `123123` |
| rows[].redeemId | integer (int64) |  | 例: `40607` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BTC` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].originalAmount | string |  | 例: `21312.23223` |
| rows[].type | string |  | NORMAL for normal maturity redemption, EARLY for early redemption, CONVERT for redeem to simple earn flexible<br>NORMAL:产品到期赎回；EARLY:提前赎回；CONVERT:赎回到赚币活期<br>例: `NORMAL` |
| rows[].deliverDate | string |  | Redemption date<br>赎回到账日期<br>例: `1575018510000` |
| rows[].lossAmount | string |  | Loss of profit on early redemption<br>提前赎回扣息金额<br>例: `0.00001232` |
| rows[].isComplete | boolean |  | 例: `True` |
| rows[].rewardAsset | string |  | 例: `SOLV` |
| rows[].rewardAmt | string |  | 例: `5.17181528` |
| rows[].status | string |  | CREATED/PAID<br>CREATED:赎回中；PAID：本金&利息已到账<br>例: `PAID` |
| total | integer (int64) |  | 例: `1` |

## Get On-chain Yields Locked Rewards History (USER_DATA)（查询链上赚币定期收益记录 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/history/rewardsRecord`

Get On-chain Yields Locked Rewards History

查询定期收益记录

Operation ID: `getOnChainYieldsLockedRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| positionId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Rewards History / 获取链上收益锁仓收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | string |  | 例: `123123` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BNB` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].amount | string |  | 例: `21312.23223` |
| total | integer (int64) |  | 例: `1` |

## Get On-chain Yields Locked Subscription Preview (USER_DATA)（链上赚币定期申购预览 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/subscriptionPreview`

Get On-chain Yields Locked Subscription Preview

链上赚币定期申购预览

Operation ID: `getOnChainYieldsLockedSubscriptionPreview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| projectId | query | string | 是 | 例: `1` |
| amount | query | number (float) | 是 | 例: `1.0` |
| autoSubscribe | query | boolean |  | 默认: `True`<br>例: `True` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Subscription Preview / 获取链上收益锁仓申购预览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rewardAsset | string |  | Earned asset<br>收益资产<br>例: `SOLV` |
| totalRewardAmt | string |  | Earned amount total in locked period<br>锁仓期结束后总收益<br>例: `5.17181528` |
| nextPay | string |  | Next estimated rewards payment<br>下一次支付收益预估<br>例: `1.29295383` |
| nextPayDate | string |  | Next rewards payment date<br>下一次支付收益时间<br>例: `1646697600000` |
| rewardsPayDate | string |  | Rewards payment date<br>收益支付时间<br>例: `1646697600000` |
| valueDate | string |  | 例: `1646697600000` |
| rewardsEndDate | string |  | Rewards accrual end date<br>最后计息日<br>例: `1651449600000` |
| deliverDate | string |  | Redemption arrival time(if auto-subscribe is true, not response this one)<br>赎回到账时间(autoSubscribe=true 时不返回)<br>例: `1651536000000` |
| nextSubscriptionDate | string |  | Response if autoSubscribe is true<br>autoSubscribe=true 时返回<br>例: `1651536000000` |

## Get On-chain Yields Locked Subscription Record (USER_DATA)（查询链上赚币定期申购记录 (USER_DATA)）

`GET /sapi/v1/onchain-yields/locked/history/subscriptionRecord`

Get On-chain Yields Locked Subscription Record

查询链上赚币定期申购记录

Operation ID: `getOnChainYieldsLockedSubscriptionRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| purchaseId | query | string |  | 例: `1` |
| clientId | query | string |  | 例: `1` |
| asset | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get On-chain Yields Locked Subscription Record / 获取链上收益锁仓申购记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].positionId | string |  | 例: `123123` |
| rows[].purchaseId | string |  | 例: `26055` |
| rows[].projectId | string |  | 例: `Solv-60d` |
| rows[].clientId | string |  | 例: `ABC` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BTC` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].lockPeriod | string |  | 例: `30` |
| rows[].type | string |  | NORMAL for normal staking, AUTO for auto-subscription order<br>NORMAL 为一般申购类型；AUTO 为到期自动申购类型<br>例: `AUTO` |
| rows[].sourceAccount | string |  | SPOT, FUNDING, SPOTANDFUNDING<br>SPOT,FUNDING,SPOTANDFUNDING<br>例: `SPOT` |
| rows[].amtFromSpot | string |  | Display if sourceAccount is SPOTANDFUNDING<br>SourceAccount为SPOTANDFUNDING时返回<br>例: `30` |
| rows[].amtFromFunding | string |  | Display if sourceAccount is SPOTANDFUNDING<br>sourceAccount为SPOTANDFUNDING时返回<br>例: `70` |
| rows[].status | string |  | PURCHASING/SUCCESS/FAILED<br>PURCHASING:申购中/SUCCESS:成功/FAILED:失败<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## On-chain Yields Account (USER_DATA)（链上赚币账户 (USER_DATA)）

`GET /sapi/v1/onchain-yields/account`

On-chain Yields Account query

链上赚币账户

Operation ID: `onChainYieldsAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`<br>不能超过60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：On-chain Yields Account / 链上收益账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAmountInBTC | string |  | 例: `0.01067982` |
| totalAmountInUSDT | string |  | 例: `77.13289230` |
| totalFlexibleAmountInBTC | string |  | 例: `0.00000000` |
| totalFlexibleAmountInUSDT | string |  | 例: `0.00000000` |
| totalLockedInBTC | string |  | 例: `0.01067982` |
| totalLockedInUSDT | string |  | 例: `77.13289230` |

## Redeem On-chain Yields Locked Product (TRADE)（赎回链上赚币定期产品 (TRADE)）

`POST /sapi/v1/onchain-yields/locked/redeem`

Redeem On-chain Yields Locked Product

赎回链上赚币定期产品

Operation ID: `redeemOnChainYieldsLockedProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | Locked product position ID<br>定期产品持仓 ID<br>例: `1` |
| channelId | string |  | 例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem On-chain Yields Locked Product / 赎回链上收益锁仓产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| redeemId | integer (int64) |  | 例: `40607` |
| success | boolean |  | 例: `True` |

## Set On-chain Yields Locked Auto Subscribe (USER_DATA)（设置链上赚币定期自动申购 (USER_DATA)）

`POST /sapi/v1/onchain-yields/locked/setAutoSubscribe`

Set On-chain Yield locked auto subscribe

为链上赚币定期产品设置自动申购功能

Operation ID: `setOnChainYieldsLockedAutoSubscribe`

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

### 响应 200：Set On-chain Yields Locked Auto Subscribe / 设置链上收益锁仓自动申购

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Set On-chain Yields Locked Product Redeem Option (USER_DATA)（设置链上赚币定期赎回目标账户 (USER_DATA)）

`POST /sapi/v1/onchain-yields/locked/setRedeemOption`

Set On-chain Yields redeem option for Locked product

为链上赚币定期产品设置赎回目标账户，现货钱包或活期产品

Operation ID: `setOnChainYieldsLockedProductRedeemOption`

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

### 响应 200：Set On-chain Yields Locked Product Redeem Option / 设置链上收益锁仓产品赎回选项

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Subscribe On-chain Yields Locked Product (TRADE)（申购链上赚币定期产品 (TRADE)）

`POST /sapi/v1/onchain-yields/locked/subscribe`

Subscribe On-chain Yields Locked Product

申购链上赚币定期产品

Operation ID: `subscribeOnChainYieldsLockedProduct`

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
| redeemTo | string |  | Takes effect when Auto Subscribe is false<br>当自动申购为false时生效<br>枚举: `SPOT`, `FLEXIBLE`<br>默认: `FLEXIBLE`<br>例: `FLEXIBLE` |
| channelId | string |  | 例: `1` |
| clientId | string |  | 例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe On-chain Yields Locked Product / 申购链上收益锁仓产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| purchaseId | integer (int64) |  | 例: `40607` |
| positionId | string |  | 例: `12345` |
| amount | string |  | 例: `75.46000000` |
| success | boolean |  | 例: `True` |

## Get Soft Staking Product List (USER_DATA)（查询持币生息产品列表 (USER_DATA)）

`GET /sapi/v1/soft-staking/list`

Get the available Soft Staking product list.

查询持币生息币种列表

Operation ID: `getSoftStakingProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Soft Staking Product List / 获取软质押产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | boolean |  | 例: `True` |
| totalRewardsUsdt | string |  | 例: `3.09827182` |
| rows | object[] |  |  |
| rows[].asset | string |  | 例: `BNB` |
| rows[].minAmount | string |  | 例: `0.5` |
| rows[].maxCap | string |  | 例: `1000` |
| rows[].apr | string |  | 例: `0.0015` |
| rows[].stakedAmount | string |  | 例: `2.14` |
| rows[].totalProfit | string |  | 例: `0.00171234` |
| total | integer (int64) |  | 例: `2` |

## Get Soft Staking Rewards History (USER_DATA)（查询持币生息收益记录 (USER_DATA)）

`GET /sapi/v1/soft-staking/history/rewardsRecord`

Get Soft Staking Rewards History

查询持币生息收益记录

Operation ID: `getSoftStakingRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Soft Staking Rewards History / 获取软质押收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].asset | string |  | 例: `BNB` |
| rows[].rewards | string |  | 例: `0.00000557` |
| rows[].rewardAsset | string |  | 例: `BNB` |
| rows[].avgAmount | string |  | 例: `2.14` |
| rows[].time | integer (int64) |  | 例: `1754007978000` |
| total | integer (int64) |  | 例: `2` |

## Set Soft Staking (USER_DATA)（设置持币生息开关 (USER_DATA)）

`GET /sapi/v1/soft-staking/set`

Enable or disable Soft Staking.

持币生息功能打开或关闭

Operation ID: `setSoftStaking`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| softStaking | query | boolean | 是 | 例: `True` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Soft Staking / 设置持币生息开关

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Claim Boost Rewards (TRADE)（领取Boost空投奖励 (TRADE)）

`POST /sapi/v1/sol-staking/sol/claim`

Claim Boost APR Airdrop Rewards

领取Boost空投奖励

Operation ID: `claimBoostRewards`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Claim Boost Rewards / 领取Boost空投奖励

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Get BNSOL Rate History (USER_DATA)（查询BNSOL汇率历史 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/rateHistory`

Get BNSOL Rate History

查询BNSOL汇率历史

Operation ID: `getBnsolRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>数值不能超过60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BNSOL Rate History / 获取 BNSOL 利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].annualPercentageRate | string |  | BNSOL APR<br>例: `0.00006408` |
| rows[].exchangeRate | string |  | SOL amount per 1 BNSOL<br>1 BNSOL对应SOL数量<br>例: `1.001212343432` |
| rows[].boostRewards | object[] |  |  |
| rows[].boostRewards[].boostAPR | string |  | 例: `0.12000000` |
| rows[].boostRewards[].rewardsAsset | string |  | 例: `SOL` |
| rows[].time | integer (int64) |  | 例: `1577233578000` |
| total | string |  | 例: `1` |

## Get BNSOL rewards history (USER_DATA)（查询BNSOL收益历史 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory`

Get BNSOL rewards history

查询BNSOL收益历史

Operation ID: `getBnsolRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BNSOL rewards history / 获取 BNSOL 收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| estRewardsInSOL | string |  | 例: `1.23230920` |
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].amountInSOL | string |  | reward amount<br>收益数量<br>例: `0.23223` |
| rows[].holding | string |  | BNSOL holding balance<br>BNSOL持仓<br>例: `2.3223` |
| rows[].holdingInSOL | string |  | 例: `2.4231` |
| rows[].annualPercentageRate | string |  | 0.5 means 50% here<br>0.5 代表 50%<br>例: `0.5` |
| total | integer (int64) |  | 例: `1` |

## Get Boost Rewards History (USER_DATA)（查询Boost空投奖励历史 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory`

Get Boost rewards history

查询Boost空投奖励历史

Operation ID: `getBoostRewardsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | string | 是 | 枚举: `CLAIM`, `DISTRIBUTE`<br>默认: `CLAIM`<br>例: `CLAIM` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Boost Rewards History / 获取 Boost 奖励历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1729520680` |
| rows[].token | string |  | 例: `SOL` |
| rows[].amount | string |  | 例: `1.20291028` |
| rows[].bnsolHolding | string |  | Display if the type is "DISTRIBUTE"<br>当type是"DISTRIBUTE"的时候展示<br>例: `2.0928798` |
| rows[].status | string |  | Display if the type is "CLAIM"<br>当type是"CLAIM"的时候展示<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get SOL redemption history (USER_DATA)（查询SOL赎回记录 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/redemptionHistory`

Get SOL redemption history

查询SOL赎回记录

Operation ID: `getSolRedemptionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| redeemId | query | integer (int64) |  | 例: `1234567` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get SOL redemption history / 获取 SOL 赎回历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].arrivalTime | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `BNSOL` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].distributeAsset | string |  | 例: `SOL` |
| rows[].distributeAmount | string |  | 例: `21338.0699` |
| rows[].exchangeRate | string |  | 例: `1.00121234` |
| rows[].status | string |  | 例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get SOL staking history (USER_DATA)（查询SOL质押记录 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/stakingHistory`

Get SOL staking history

查询SOL质押记录

Operation ID: `getSolStakingHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| purchaseId | query | integer (int64) |  | 例: `1234567` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Currently querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get SOL staking history / 获取 SOL 质押历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| rows[].asset | string |  | 例: `SOL` |
| rows[].amount | string |  | 例: `21312.23223` |
| rows[].distributeAsset | string |  | 例: `BNSOL` |
| rows[].distributeAmount | string |  | 例: `21286.42584` |
| rows[].exchangeRate | string |  | 例: `1.00121234` |
| rows[].status | string |  | 例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get SOL staking quota details (USER_DATA)（查询SOL质押限额信息 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/quota`

Get SOL staking quota

查询SOL质押限额

Operation ID: `getSolStakingQuotaDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>不可以超过60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get SOL staking quota details / 获取 SOL 质押限额详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leftStakingPersonalQuota | string |  | 例: `1000` |
| leftRedemptionPersonalQuota | string |  | 例: `1000` |
| minStakeAmount | string |  | 例: `0.01000000` |
| minRedeemAmount | string |  | 例: `0.00000001` |
| redeemPeriod | integer (int64) |  | 例: `4` |
| stakeable | boolean |  | 例: `True` |
| redeemable | boolean |  | 例: `True` |
| soldOut | boolean |  | 例: `False` |
| commissionFee | string |  | 例: `0.25000000` |
| nextEpochTime | integer (int64) |  | 例: `725993969475` |
| calculating | boolean |  | 例: `False` |

## Get Unclaimed Rewards (USER_DATA)（查询未领取的Boost空投奖励 (USER_DATA)）

`GET /sapi/v1/sol-staking/sol/history/unclaimedRewards`

Get Unclaimed rewards

查询未领取的Boost空投奖励

Operation ID: `getUnclaimedRewards`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Unclaimed Rewards / 获取未领取奖励

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amount | string |  | 例: `1.00000011` |
| [].rewardsAsset | string |  | 例: `SOL` |

## Redeem SOL (TRADE)（赎回SOL (TRADE)）

`POST /sapi/v1/sol-staking/sol/redeem`

Redeem BNSOL get SOL

赎回BNSOL并获得SOL

Operation ID: `redeemSol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in BNSOL, limit 8 decimals<br>BNSOL 数量，限制8位小数<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem SOL / 赎回SOL

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| solAmount | string |  | 例: `0.23092091` |
| redeemId | integer (int64) |  | 例: `1234567` |
| exchangeRate | string |  | 例: `1.00121234` |
| arrivalTime | integer (int64) |  | 例: `1575018510000` |

## SOL Staking account (USER_DATA)（SOL质押账户 (USER_DATA)）

`GET /sapi/v1/sol-staking/account`

SOL Staking account

SOL质押账户

Operation ID: `solStakingAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>不可以超过60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：SOL Staking account / SOL 质押账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bnsolAmount | string |  | 例: `1.10928781` |
| holdingInSOL | string |  | 例: `1.22330928` |
| thirtyDaysProfitInSOL | string |  | 例: `0.22330928` |

## Subscribe SOL Staking (TRADE)（质押SOL (TRADE)）

`POST /sapi/v1/sol-staking/sol/stake`

Subscribe SOL Staking

质押SOL

Operation ID: `subscribeSolStaking`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | Amount in SOL.<br>SOL 数量<br>例: `1.0` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe SOL Staking / 申购 SOL 质押

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| bnsolAmount | string |  | 例: `0.23092091` |
| purchaseId | integer (int64) |  | 例: `1234567` |
| exchangeRate | string |  | SOL amount per 1 BNSOL<br>每1BNSOL对应SOL的数量<br>例: `1.001212342342` |