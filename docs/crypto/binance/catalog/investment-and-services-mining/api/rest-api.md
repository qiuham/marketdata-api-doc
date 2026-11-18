---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-mining/api/rest-api
api_type: REST
updated_at: 2026-11-18 02:46:58.521606
---

# Mining REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-mining/api/rest-api/1.0.0/schema.yaml

Query mining status, earnings, and account data via the Binance Pool API.

通过 Binance Pool API 查询挖矿状态、收益和账户数据。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/mining/statistics/user/list` — Account List (USER_DATA)
- `GET /sapi/v1/mining/pub/algoList` — Acquiring Algorithm (MARKET_DATA)
- `GET /sapi/v1/mining/pub/coinList` — Acquiring CoinName (MARKET_DATA)
- `POST /sapi/v1/mining/hash-transfer/config/cancel` — Cancel hashrate resale configuration (USER_DATA)
- `GET /sapi/v1/mining/payment/list` — Earnings List (USER_DATA)
- `GET /sapi/v1/mining/payment/other` — Extra Bonus List (USER_DATA)
- `GET /sapi/v1/mining/hash-transfer/profit/details` — Hashrate Resale Detail (USER_DATA)
- `GET /sapi/v1/mining/hash-transfer/config/details/list` — Hashrate Resale List (USER_DATA)
- `POST /sapi/v1/mining/hash-transfer/config` — Hashrate Resale Request (USER_DATA)
- `GET /sapi/v1/mining/payment/uid` — Mining Account Earning (USER_DATA)
- `GET /sapi/v1/mining/worker/detail` — Request for Detail Miner List (USER_DATA)
- `GET /sapi/v1/mining/worker/list` — Request for Miner List (USER_DATA)
- `GET /sapi/v1/mining/statistics/user/status` — Statistic List (USER_DATA)

## Account List (USER_DATA)（账号列表 (USER_DATA)）

`GET /sapi/v1/mining/statistics/user/list`

Query Account List

查询账号列表

Operation ID: `accountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm name.<br>算法名称。<br>例: `sha256` |
| userName | query | string | 是 | Mining account<br>挖矿用户名<br>例: `test` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account List / 账号列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object[] |  |  |
| data[].type | string |  | Type of hashrate bucket<br>算力类型<br>例: `H_hashrate` |
| data[].userName | string |  | Mining account<br>账户名<br>例: `test` |
| data[].list | object[] |  |  |
| data[].list[].time | integer (int64) |  | Time<br>时间<br>例: `1585267200000` |
| data[].list[].hashrate | string |  | Hashrate<br>算力<br>例: `0.00000000` |
| data[].list[].reject | string |  | Rejection rate<br>拒绝率<br>例: `0.00000000` |

## Acquiring Algorithm (MARKET_DATA)（获取算法 (MARKET_DATA)）

`GET /sapi/v1/mining/pub/algoList`

Acquiring Algorithm

获取算法

Operation ID: `acquiringAlgorithm`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Acquiring Algorithm / 获取算法

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object[] |  |  |
| data[].algoName | string |  | Algorithm name<br>算法名称<br>例: `SHA256-BTC` |
| data[].algoId | integer (int64) |  | Algorithm ID<br>算法id<br>例: `1` |
| data[].poolIndex | integer (int64) |  | Sequence<br>序列<br>例: `100` |
| data[].unit | string |  | Unit<br>单位<br>例: `h/s` |

## Acquiring CoinName (MARKET_DATA)（获取币种 (MARKET_DATA)）

`GET /sapi/v1/mining/pub/coinList`

Acquiring CoinName

获取币种

Operation ID: `acquiringCoinname`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Acquiring CoinName / 获取币种

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object[] |  |  |
| data[].coinName | string |  | Currency name<br>币种名称<br>例: `BTC` |
| data[].coinId | integer (int64) |  | ID<br>id<br>例: `1` |
| data[].poolIndex | integer (int64) |  | Sort<br>排序<br>例: `0` |
| data[].algoId | integer (int64) |  | Algorithm<br>所属算法<br>例: `1` |
| data[].algoName | string |  | Name of algorithm<br>所属算法名称<br>例: `SHA256-BTC` |

## Cancel hashrate resale configuration (USER_DATA)（取消算力转让设置 (USER_DATA)）

`POST /sapi/v1/mining/hash-transfer/config/cancel`

Cancel hashrate resale configuration

取消算力转让设置

Operation ID: `cancelHashrateResaleConfiguration`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| configId | integer (int64) | 是 | Mining ID<br>配置的id<br>例: `168` |
| userName | string | 是 | Mining Account<br>挖矿用户名<br>例: `test` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel hashrate resale configuration / 取消算力转让设置

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | boolean |  | 例: `True` |

## Earnings List (USER_DATA)（收益列表 (USER_DATA)）

`GET /sapi/v1/mining/payment/list`

Query Earnings List

收益列表

Operation ID: `earningsList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm name.<br>算法名称。<br>例: `sha256` |
| userName | query | string | 是 | Mining account.<br>挖矿用户名。<br>例: `test` |
| coin | query | string |  | Coin name<br>币种名称<br>例: `BTC` |
| startDate | query | integer (int64) |  | Search start time in milliseconds.<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| endDate | query | integer (int64) |  | Search end time in milliseconds.<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Number of rows per page.<br>分页数量,最小10,最大200<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Earnings List / 收益列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.accountProfits | object[] |  |  |
| data.accountProfits[].time | integer (int64) |  | Mining date<br>时间<br>例: `1586188800000` |
| data.accountProfits[].type | integer (int64) |  | 0: Mining Wallet, 5: Mining Address, 7: Pool Savings, 8: Transferred, 31: Income<br>Transfer, 32: Hashrate Resale-Mining Wallet, 33: Hashrate Resale-Pool Savings<br>0: 矿池钱包, 5: 地址挖矿, 7: 矿池宝, 8: 已转让, 31: 收益转让, 32: 算力转让-矿池钱包, 33:<br>算力转让-矿池宝<br>例: `31` |
| data.accountProfits[].hashTransfer | integer (int64) |  | Transferred hashrate<br>已转让算力<br>例: `200000000000` |
| data.accountProfits[].transferAmount | number (float) |  | Transferred income<br>已转让收益<br>例: `0.02180958` |
| data.accountProfits[].dayHashRate | integer (int64) |  | Daily hashrate<br>算力<br>例: `129129903378244` |
| data.accountProfits[].profitAmount | number (float) |  | Earnings amount<br>奖励数量<br>例: `8.6083060304` |
| data.accountProfits[].coinName | string |  | Coin type<br>奖励币种<br>例: `BTC` |
| data.accountProfits[].status | integer (int64) |  | Status: 0 Unpaid, 1 Paying, 2 Paid<br>支付状态: 0 待支付, 1 支付中, 2 已支付<br>例: `2` |
| data.totalNum | integer (int64) |  | Total rows<br>总条数<br>例: `3` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页数量<br>例: `20` |

## Extra Bonus List (USER_DATA)（其他收益列表 (USER_DATA)）

`GET /sapi/v1/mining/payment/other`

Extra Bonus List

其他收益列表

Operation ID: `extraBonusList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Transfer algorithm<br>算法名称<br>例: `sha256` |
| userName | query | string | 是 | Mining account<br>挖矿用户名<br>例: `test` |
| coin | query | string |  | Coin name<br>币种名称<br>例: `BTC` |
| startDate | query | integer (int64) |  | Search start time in milliseconds.<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| endDate | query | integer (int64) |  | Search end time in milliseconds.<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Number of rows per page.<br>分页数量,最小10,最大200<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Extra Bonus List / 其他收益列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.otherProfits | object[] |  |  |
| data.otherProfits[].time | integer (int64) |  | Mining date<br>时间<br>例: `1607443200000` |
| data.otherProfits[].coinName | string |  | Coin name<br>奖励币种<br>例: `BTC` |
| data.otherProfits[].type | integer (int64) |  | 1: Merged Mining, 2: Activity Bonus, 3: Rebate, 4: Smart Pool, 6: Income Transfer, 7:<br>Pool Savings<br>1: 联合挖矿, 2: 活动奖励, 3: 返点, 4: 机枪奖励, 6: 收益转让, 7: 矿池宝<br>例: `4` |
| data.otherProfits[].profitAmount | number (float) |  | Amount<br>奖励数量<br>例: `0.0011859` |
| data.otherProfits[].status | integer (int64) |  | Status: 0 Unpaid, 1 Paying, 2 Paid<br>支付状态: 0 待支付, 1 支付中, 2 已支付<br>例: `2` |
| data.totalNum | integer (int64) |  | Total rows<br>总条数<br>例: `3` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页数量<br>例: `20` |

## Hashrate Resale Detail (USER_DATA)（算力转让详情 (USER_DATA)）

`GET /sapi/v1/mining/hash-transfer/profit/details`

Hashrate Resale Detail(USER_DATA)

算力转让详情

Operation ID: `hashrateResaleDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| configId | query | integer (int64) | 是 | Configuration ID.<br>配置 ID。<br>例: `168` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Number of rows per page.<br>分页数量,最小10,最大200<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Hashrate Resale Detail / 算力转让详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.profitTransferDetails | object[] |  |  |
| data.profitTransferDetails[].poolUsername | string |  | Transfer-out sub-account<br>转出子账户<br>例: `test4001` |
| data.profitTransferDetails[].toPoolUsername | string |  | Transfer-in sub-account<br>转入子账户<br>例: `pop` |
| data.profitTransferDetails[].algoName | string |  | Transfer algorithm name<br>转让算法名称<br>例: `sha256` |
| data.profitTransferDetails[].hashRate | integer (int64) |  | Transferred hashrate<br>转让算力<br>例: `200000000000` |
| data.profitTransferDetails[].day | integer (int64) |  | Transfer date<br>转让日期<br>例: `20201213` |
| data.profitTransferDetails[].amount | number (float) |  | Transferred income<br>转让收益<br>例: `0.2256872` |
| data.profitTransferDetails[].coinName | string |  | Income coin<br>收益币种<br>例: `BTC` |
| data.totalNum | integer (int64) |  | Total rows<br>总条数<br>例: `8` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页数量<br>例: `200` |

## Hashrate Resale List (USER_DATA)（算力转让列表 (USER_DATA)）

`GET /sapi/v1/mining/hash-transfer/config/details/list`

Hashrate Resale List

算力转让列表

Operation ID: `hashrateResaleList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Number of rows per page.<br>分页数量,最小10,最大200<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Hashrate Resale List / 算力转让列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.configDetails | object[] |  |  |
| data.configDetails[].configId | integer (int64) |  | Configuration ID<br>该配置的id<br>例: `168` |
| data.configDetails[].poolUsername | string |  | Transfer-out sub-account<br>转出子账户<br>例: `123` |
| data.configDetails[].toPoolUsername | string |  | Transfer-in sub-account<br>转入子账户<br>例: `user1` |
| data.configDetails[].algoName | string |  | Transfer algorithm name<br>转让算法名称<br>例: `Ethash` |
| data.configDetails[].hashRate | integer (int64) |  | Transferred hashrate<br>转让算力<br>例: `5000000` |
| data.configDetails[].startDay | integer (int64) |  | Start date<br>开始时间<br>例: `20201210` |
| data.configDetails[].endDay | integer (int64) |  | End date<br>结束时间<br>例: `20210405` |
| data.configDetails[].status | integer (int64) |  | Status: 0 Processing, 1 Cancelled, 2 Terminated<br>状态: 0 进行中, 1 已取消, 2 已终止<br>例: `1` |
| data.configDetails[].type | integer (int64) |  | Type: 0 Hashrate transfer record, 1 Hashrate receive record<br>类型: 0 算力转让记录, 1 算力接收记录<br>例: `0` |
| data.totalNum | integer (int64) |  | Total rows<br>总条数<br>例: `21` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页数量<br>例: `200` |

## Hashrate Resale Request (USER_DATA)（算力转让请求 (USER_DATA)）

`POST /sapi/v1/mining/hash-transfer/config`

Hashrate Resale Request

算力转让请求

Operation ID: `hashrateResaleRequest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| userName | string | 是 | Mining Account<br>挖矿用户名<br>例: `test` |
| algo | string | 是 | Transfer algorithm<br>算法名称<br>例: `sha256` |
| endDate | integer (int64) | 是 | Resale End Time (Millisecond timestamp)<br>转让结束时间(毫秒时间戳)<br>例: `1770736694138` |
| startDate | integer (int64) | 是 | Resale Start Time(Millisecond timestamp)<br>转让开始时间(毫秒时间戳)<br>例: `1770736694138` |
| toPoolUser | string | 是 | Mining Account<br>挖矿用户名<br>例: `S19pro` |
| hashRate | integer (int64) | 是 | Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than<br>500000)<br>转让算力h/s必传(BTC 大于 500000000000 ETH大于 500000)<br>例: `100000000` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Hashrate Resale Request / 算力转让请求

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | integer (int64) |  | Configuration ID<br>该配置的id<br>例: `171` |

## Mining Account Earning (USER_DATA)（矿池账户收益列表 (USER_DATA)）

`GET /sapi/v1/mining/payment/uid`

Mining Account Earning

矿池账户收益列表

Operation ID: `miningAccountEarning`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm<br>算法名称<br>例: `sha256` |
| startDate | query | integer (int64) |  | Millisecond timestamp<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| endDate | query | integer (int64) |  | Millisecond timestamp<br>搜索日期 毫秒时间戳，同时为空查询所有<br>例: `1770736694138` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Number of rows per page.<br>分页数量,最小10,最大200<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Mining Account Earning / 矿池账户收益列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.accountProfits | object[] |  |  |
| data.accountProfits[].time | integer (int64) |  | Time<br>时间<br>例: `1607443200000` |
| data.accountProfits[].coinName | string |  | Coin<br>币种<br>例: `BTC` |
| data.accountProfits[].type | integer (int64) |  | 0: Referral, 1: Refund, 2: Rebate<br>0: 邀请返佣, 1: 邀请返现, 2: 返点<br>例: `2` |
| data.accountProfits[].puid | integer (int64) |  | Mining sub-account ID<br>挖矿子账户id<br>例: `59985472` |
| data.accountProfits[].subName | string |  | Mining account<br>挖矿账户名<br>例: `vdvaghani` |
| data.accountProfits[].amount | number (float) |  | Amount<br>数量<br>例: `0.09186957` |
| data.totalNum | integer (int64) |  | Total records<br>总条数<br>例: `3` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页数量<br>例: `20` |

## Request for Detail Miner List (USER_DATA)（请求矿工列表明细 (USER_DATA)）

`GET /sapi/v1/mining/worker/detail`

Request for Detail Miner List

请求矿工列表明细

Operation ID: `requestForDetailMinerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm<br>算法名称<br>例: `sha256` |
| userName | query | string | 是 | Mining account<br>挖矿用户名<br>例: `test` |
| workerName | query | string | 是 | Miner name.<br>矿工用户名，必传<br>例: `bhdc1.16A10404B` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Request for Detail Miner List / 请求矿工列表明细

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object[] |  |  |
| data[].workerName | string |  | Mining account name<br>挖矿用户名<br>例: `bhdc1.16A10404B` |
| data[].type | string |  | Type of hashrate bucket<br>算力类型<br>例: `H_hashrate` |
| data[].hashrateDatas | object[] |  |  |
| data[].hashrateDatas[].time | integer (int64) |  | Time<br>时间<br>例: `1587902400000` |
| data[].hashrateDatas[].hashrate | string |  | Hashrate<br>算力<br>例: `0` |
| data[].hashrateDatas[].reject | integer (int64) |  | Rejection rate<br>拒绝率<br>例: `0` |

## Request for Miner List (USER_DATA)（请求矿工列表 (USER_DATA)）

`GET /sapi/v1/mining/worker/list`

Request for Miner List

请求矿工列表

Operation ID: `requestForMinerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm<br>算法名称<br>例: `sha256` |
| userName | query | string | 是 | Mining account<br>挖矿用户名<br>例: `test` |
| pageIndex | query | integer (int64) |  | Page number, starting from 1.<br>页码，为空默认第一页，从1开始<br>默认: `1`<br>例: `1` |
| sort | query | integer (int64) |  | Sort order. 0 for ascending, 1 for descending.<br>排序方向(为空默认为0): 0 正序，1 倒序<br>默认: `0`<br>例: `0` |
| sortColumn | query | integer (int64) |  | Sort by: 1 miner name, 2 real-time hashrate, 3 daily average hashrate, 4 real-time rejection<br>rate, 5 last submission time<br>排序规则(默认为1): 1 矿工姓名, 2 实时算力, 3 日均算力, 4 实时拒绝率, 5 最后提交时间<br>默认: `1`<br>例: `1` |
| workerStatus | query | integer (int64) |  | Miner status. 0 all, 1 valid, 2 invalid, 3 failure.<br>矿机状态(默认为0)：0 全部，1 有效， 2 无效， 3 失效<br>默认: `0`<br>例: `0` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Request for Miner List / 请求矿工列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.workerDatas | object[] |  |  |
| data.workerDatas[].workerId | string |  | Miner ID<br>矿工id<br>例: `1420554439452400131` |
| data.workerDatas[].workerName | string |  | Miner name<br>矿工姓名<br>例: `2X73` |
| data.workerDatas[].status | integer (int64) |  | Status: 1 Valid, 2 Invalid, 3 No longer valid<br>状态: 1 有效, 2 无效, 3 失效<br>例: `3` |
| data.workerDatas[].hashRate | integer (int64) |  | Real-time rate<br>实时速率<br>例: `0` |
| data.workerDatas[].dayHashRate | number (float) |  | 24H hashrate<br>日均算力<br>例: `12697781298013.66` |
| data.workerDatas[].rejectRate | integer (int64) |  | Real-time rejection rate<br>实时拒绝率<br>例: `0` |
| data.workerDatas[].lastShareTime | integer (int64) |  | Last share time<br>最后提交时间<br>例: `1587712919000` |
| data.totalNum | integer (int64) |  | Total amount<br>总数量<br>例: `18530` |
| data.pageSize | integer (int64) |  | Rows per page<br>每页条数<br>例: `20` |

## Statistic List (USER_DATA)（统计列表 (USER_DATA)）

`GET /sapi/v1/mining/statistics/user/status`

Statistic List

统计列表

Operation ID: `statisticList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algo | query | string | 是 | Algorithm<br>算法名称<br>例: `sha256` |
| userName | query | string | 是 | Mining account<br>挖矿用户名<br>例: `test` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Statistic List / 统计列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `` |
| data | object |  |  |
| data.fifteenMinHashRate | string |  | 15-minute hashrate<br>15分钟算力<br>例: `457835490067496409.00000000` |
| data.dayHashRate | string |  | 24H hashrate<br>日均算力<br>例: `214289268068874127.65000000` |
| data.validNum | integer (int64) |  | Effective quantity<br>有效数量<br>例: `0` |
| data.invalidNum | integer (int64) |  | Invalid quantity<br>无效数量<br>例: `17562` |
| data.profitToday | object |  | Today's estimate. Keys are coin symbols (e.g. BTC, BSV, BCH), values are earning amounts as strings.<br>今日预估。键为币种符号（如 BTC、BSV、BCH），值为收益金额字符串。 |
| data.profitYesterday | object |  | Yesterday's earnings. Keys are coin symbols (e.g. BTC, BSV, BCH), values are earning amounts as strings.<br>昨日收益。键为币种符号（如 BTC、BSV、BCH），值为收益金额字符串。 |
| data.userName | string |  | Mining account<br>挖矿账户<br>例: `test` |
| data.unit | string |  | Unit<br>单位<br>例: `h/s` |
| data.algo | string |  | Algorithm<br>所属算法<br>例: `sha256` |