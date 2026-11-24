---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:18.276437
---

# Sub Account REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/1.0.0/schema.yaml

Create and manage sub-accounts, control permissions, and transfer assets via the Sub Account API.

通过 Sub Account API 创建和管理子账户、控制权限并划转资产。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/sub-account/virtualSubAccount` — Create a Virtual Sub-account (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/futures/enable` — Enable Futures for Sub-account (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/eoptions/enable` — Enable Options for Sub-account (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/futures/positionRisk` — Get Futures Position-Risk of Sub-account (For Master Account) (USER_DATA)
- `GET /sapi/v2/sub-account/futures/positionRisk` — Get Futures Position-Risk of Sub-account V2 (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/status` — Get Sub-account's Status on Margin Or Futures (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/list` — Query Sub-account List (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/transaction-statistics` — Query Sub-account Transaction Statistics (For Master Account) (USER_DATA)
- `POST /sapi/v2/sub-account/subAccountApi/ipRestriction` — Add IP Restriction for Sub-Account API key (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/subAccountApi` — Query Sub-account API Key (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/subAccountApi` — Create Sub-account API Key (For Master Account) (USER_DATA)
- `DELETE /sapi/v1/sub-account/subAccountApi` — Delete Sub-account API Key (For Master Account) (USER_DATA)
- `POST /sapi/v2/sub-account/subAccountApi` — Create Sub-account API Key V2 (For Master Account) (USER_DATA)
- `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` — Delete IP List For a Sub-account API Key (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` — Get IP Restriction for a Sub-account API Key (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/subAccountApiPermission` — Modify Sub-account API Key Permission (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/futures/transfer` — Futures Transfer for Sub-account (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/futures/account` — Get Detail on Sub-account's Futures Account (For Master Account) (USER_DATA)
- `GET /sapi/v2/sub-account/futures/account` — Get Detail on Sub-account's Futures Account V2 (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/margin/account` — Get Detail on Sub-account's Margin Account (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/futures/move-position` — Get Move Position History for Sub-account (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/futures/move-position` — Move Position for Sub-account (For Master Account) (USER_DATA)
- `GET /sapi/v1/capital/deposit/subAddress` — Get Sub-account Deposit Address (For Master Account) (USER_DATA)
- `GET /sapi/v1/capital/deposit/subHisrec` — Get Sub-account Deposit History (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/futures/accountSummary` — Get Summary of Sub-account's Futures Account (For Master Account) (USER_DATA)
- `GET /sapi/v2/sub-account/futures/accountSummary` — Get Summary of Sub-account's Futures Account V2 (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/margin/accountSummary` — Get Summary of Sub-account's Margin Account (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/margin/transfer` — Margin Transfer for Sub-account (For Master Account) (USER_DATA)
- `GET /sapi/v3/sub-account/assets` — Query Sub-account Assets (For Master Account) (USER_DATA)
- `GET /sapi/v4/sub-account/assets` — Query Sub-account Assets V4 (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/futures/internalTransfer` — Query Sub-account Futures Asset Transfer History (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/futures/internalTransfer` — Sub-account Futures Asset Transfer (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/spotSummary` — Query Sub-account Spot Assets Summary (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/sub/transfer/history` — Query Sub-account Spot Asset Transfer History (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/universalTransfer` — Query Universal Transfer History (For Master Account) (USER_DATA)
- `POST /sapi/v1/sub-account/universalTransfer` — Universal Transfer (For Master Account) (USER_DATA)
- `GET /sapi/v1/sub-account/transfer/subUserHistory` — Sub-account Transfer History (For Sub-account) (USER_DATA)
- `POST /sapi/v1/sub-account/transfer/subToMaster` — Transfer to Master (For Sub-account) (USER_DATA)
- `POST /sapi/v1/sub-account/transfer/subToSub` — Transfer to Sub-account of Same Master (For Sub-account) (USER_DATA)
- `POST /sapi/v1/managed-subaccount/deposit` — Deposit Assets Into The Managed Sub-account (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/deposit/address` — Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/asset` — Query Managed Sub-account Asset Details (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/fetch-future-asset` — Query Managed Sub-account Futures Asset Details (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/info` — Query Managed Sub-account List (For Investor) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/marginAsset` — Query Managed Sub-account Margin Asset Details (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/accountSnapshot` — Query Managed Sub-account Snapshot (For Investor Master Account) (USER_DATA)
- `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor` — Query Managed Sub Account Transfer Log For Investor Master Account (USER_DATA)
- `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent` — Query Managed Sub Account Transfer Log For Trading Team Master Account (USER_DATA)
- `GET /sapi/v1/managed-subaccount/query-trans-log` — Query Managed Sub Account Transfer Log (For Trading Team Sub Account) (USER_DATA)
- `POST /sapi/v1/managed-subaccount/withdraw` — Withdrawl Assets From The Managed Sub-account (For Investor Master Account) (USER_DATA)

## Create a Virtual Sub-account (For Master Account) (USER_DATA)（创建虚拟子账户 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/virtualSubAccount`

Create a Virtual Sub-account

创建虚拟子账户

Operation ID: `createAVirtualSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountString | string | 是 | Please input a string. We will create a virtual email using that string for you to register<br>请输入字符串，我们将为您创建一个虚拟邮箱进行注册<br>例: `testSubAccount` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create a Virtual Sub-account / 创建虚拟子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string |  | 例: `addsdd_virtual@aasaixwqnoemail.com` |

## Enable Futures for Sub-account (For Master Account) (USER_DATA)（为子账户开通合约 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/futures/enable`

Enable Futures for Sub-account for Master Account

为子账户开通合约 (适用主账户)

Operation ID: `enableFuturesForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | 例: `123@test.com` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Futures for Sub-account / 为子账户开通合约

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string |  | 例: `123@test.com` |
| isFuturesEnabled | boolean |  | true or false<br>例: `True` |

## Enable Options for Sub-account (For Master Account) (USER_DATA)（为子账户开通期权 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/eoptions/enable`

Enable Options for Sub-account (For Master Account).

为子账户开通期权 (适用主账户)

Operation ID: `enableOptionsForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | 例: `123@test.com` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Options for Sub-account / 为子账户开通期权

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string |  | 例: `123@test.com` |
| isEOptionsEnabled | boolean |  | true or false<br>例: `True` |

## Get Futures Position-Risk of Sub-account (For Master Account) (USER_DATA)（查询子账户合约持仓信息 (仅适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/futures/positionRisk`

Get Futures Position-Risk of Sub-account

查询子账户合约持仓信息

Operation ID: `getFuturesPositionRiskOfSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Position-Risk of Sub-account / 查询子账户合约持仓风险

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].entryPrice | string |  | 例: `9975.12000` |
| [].leverage | string |  | current initial leverage<br>例: `50` |
| [].maxNotional | string |  | notional value limit of current initial leverage<br>例: `1000000` |
| [].liquidationPrice | string |  | 例: `7963.54` |
| [].markPrice | string |  | 例: `9973.50770517` |
| [].positionAmount | string |  | 例: `0.010` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].unrealizedProfit | string |  | 例: `-0.01612295` |

## Get Futures Position-Risk of Sub-account V2 (For Master Account) (USER_DATA)（查询子账户合约持仓信息V2 (仅适用主账户) (USER_DATA)）

`GET /sapi/v2/sub-account/futures/positionRisk`

Get Futures Position-Risk of Sub-account V2

查询子账户合约持仓信息

Operation ID: `getFuturesPositionRiskOfSubAccountV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| futuresType | query | integer (int64) | 是 | 1: USDT-margined Futures，2: Coin-margined Futures<br>1: USDT合约，2: 币本位合约<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Position-Risk of Sub-account V2 / 查询子账户合约持仓风险 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| futurePositionRiskVos | object[] |  |  |
| futurePositionRiskVos[].entryPrice | string |  | 例: `9975.12000` |
| futurePositionRiskVos[].leverage | string |  | current initial leverage<br>例: `50` |
| futurePositionRiskVos[].maxNotional | string |  | notional value limit of current initial leverage<br>例: `1000000` |
| futurePositionRiskVos[].liquidationPrice | string |  | 例: `7963.54` |
| futurePositionRiskVos[].markPrice | string |  | 例: `9973.50770517` |
| futurePositionRiskVos[].positionAmount | string |  | 例: `0.010` |
| futurePositionRiskVos[].symbol | string |  | 例: `BTCUSDT` |
| futurePositionRiskVos[].unrealizedProfit | string |  | 例: `-0.01612295` |
| deliveryPositionRiskVos | object[] |  |  |
| deliveryPositionRiskVos[].entryPrice | string |  | 例: `9975.12000` |
| deliveryPositionRiskVos[].markPrice | string |  | 例: `9973.50770517` |
| deliveryPositionRiskVos[].leverage | string |  | 例: `20` |
| deliveryPositionRiskVos[].isolated | string |  | 例: `false` |
| deliveryPositionRiskVos[].isolatedWallet | string |  | 例: `9973.50770517` |
| deliveryPositionRiskVos[].isolatedMargin | string |  | 例: `0.00000000` |
| deliveryPositionRiskVos[].isAutoAddMargin | string |  | 例: `false` |
| deliveryPositionRiskVos[].positionSide | string |  | 例: `BOTH` |
| deliveryPositionRiskVos[].positionAmount | string |  | 例: `1.230` |
| deliveryPositionRiskVos[].symbol | string |  | 例: `BTCUSD_201225` |
| deliveryPositionRiskVos[].unrealizedProfit | string |  | 例: `-0.01612295` |

## Get Sub-account's Status on Margin Or Futures (For Master Account) (USER_DATA)（查询子账户杠杆/合约状态 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/status`

Get Sub-account's Status on Margin Or Futures

查询子账户杠杆/合约状态

Operation ID: `getSubAccountsStatusOnMarginOrFutures`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string |  | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Sub-account's Status on Margin Or Futures / 查询子账户杠杆或合约状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].email | string |  | user email<br>例: `123@test.com` |
| [].isSubUserEnabled | boolean |  | true or false<br>例: `True` |
| [].isUserActive | boolean |  | true or false<br>例: `True` |
| [].insertTime | integer (int64) |  | sub account create time<br>例: `1570791523523` |
| [].isMarginEnabled | boolean |  | true or false for margin<br>例: `True` |
| [].isFutureEnabled | boolean |  | true or false for futures.<br>例: `True` |
| [].mobile | integer (int64) |  | user mobile number<br>例: `1570791523523` |

## Query Sub-account List (For Master Account) (USER_DATA)（查询子账户列表 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/list`

Query Sub-account List

查询子账户列表(适用主账户)

Operation ID: `querySubAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string |  | 例: `123@test.com` |
| isFreeze | query | string |  | 例: `True` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `1`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account List / 子账户列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccounts | object[] |  |  |
| subAccounts[].subUserId | integer (int64) |  | 例: `123456` |
| subAccounts[].email | string |  | 例: `testsub@gmail.com` |
| subAccounts[].remark | string |  | 例: `remark` |
| subAccounts[].isFreeze | boolean |  | 例: `False` |
| subAccounts[].createTime | integer (int64) |  | 例: `1544433328000` |
| subAccounts[].isManagedSubAccount | boolean |  | 例: `False` |
| subAccounts[].isAssetManagementSubAccount | boolean |  | 例: `False` |

## Query Sub-account Transaction Statistics (For Master Account) (USER_DATA)（查询子账户交易量统计列表 (适用母账户) (USER_DATA)）

`GET /sapi/v1/sub-account/transaction-statistics`

Query Sub-account Transaction statistics (For Master Account).

查询子账户交易量统计列表 (适用母账户)

Operation ID: `querySubAccountTransactionStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string |  | Managed sub-account email<br>托管子账户邮箱<br>例: `abc@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Transaction Statistics / 子账户交易量统计

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recent30BtcTotal | string |  | 例: `0` |
| recent30BtcFuturesTotal | string |  | 例: `0` |
| recent30BtcMarginTotal | string |  | 例: `0` |
| recent30BusdTotal | string |  | 例: `0` |
| recent30BusdFuturesTotal | string |  | 例: `0` |
| recent30BusdMarginTotal | string |  | 例: `0` |
| tradeInfoVos | object[] |  |  |
| tradeInfoVos[].userId | integer (int64) |  | 例: `1000138138384` |
| tradeInfoVos[].btc | integer (int64) |  | 例: `0` |
| tradeInfoVos[].btcFutures | integer (int64) |  | 例: `0` |
| tradeInfoVos[].btcMargin | integer (int64) |  | 例: `0` |
| tradeInfoVos[].busd | integer (int64) |  | 例: `0` |
| tradeInfoVos[].busdFutures | integer (int64) |  | 例: `0` |
| tradeInfoVos[].busdMargin | integer (int64) |  | 例: `0` |
| tradeInfoVos[].date | integer (int64) |  | 例: `1676851200000` |

## Add IP Restriction for Sub-Account API key (For Master Account) (USER_DATA)（为子账户API Key增加IP白名单 (适用母账户) (USER_DATA)）

`POST /sapi/v2/sub-account/subAccountApi/ipRestriction`

Add IP Restriction for Sub-Account API key

为子账户API Key增加IP白名单

Operation ID: `addIpRestrictionForSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | 例: `123@test.com` |
| subAccountApiKey | string | 是 | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| status | integer (int64) | 是 | IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only.<br>IP限制状态。1或不填入(null) = IP未受限。2 = 仅限受信任IP访问。<br>例: `1` |
| ipAddress | string |  | Insert static IP in batch, separated by commas.<br>可批量填入IP，以逗号区隔<br>例: `69.210.67.14` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Add IP Restriction for Sub-Account API key / 为子账户 API Key 添加 IP 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `2` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1636371437000` |
| apiKey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |

## Query Sub-account API Key (For Master Account) (USER_DATA)（查询子账户API Key (适用母账户) (USER_DATA)）

`GET /sapi/v1/sub-account/subAccountApi`

Query the API Key list of a sub-account.

查询子账户的 API Key 列表。

Operation ID: `querySubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: https://www.binance.com/en/support/faq/detail/360002502072.<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：https://www.binance.com/cn/support/faq/detail/360002502072。<br>例: `API_KEY` |
| email | query | string | 是 | Sub-account email<br>子账户邮箱<br>例: `123@test.com` |
| subAccountApiKey | query | string |  | Specify an API Key for exact match<br>指定 API Key 进行精确查询<br>例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| page | query | integer (int64) |  | Page number, default 1, minimum 1<br>页码，默认 1，最小 1<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Page size, default 30, maximum 100<br>每页数量，默认 30，最大 100<br>默认: `30`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Sub-account API Key / 查询子账户 API Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| rows | object[] |  |  |
| rows[].email | string |  | 例: `123@test.com` |
| rows[].apiName | string |  | 例: `myKey` |
| rows[].apikey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| rows[].canTrade | boolean |  | 例: `True` |
| rows[].canMarginLoanRepay | boolean |  | 例: `False` |
| rows[].canFuturesTrade | boolean |  | 例: `False` |
| rows[].canUniversalTransfer | boolean |  | 例: `False` |
| rows[].canVanillaOptions | boolean |  | 例: `False` |
| rows[].canFixApiTrading | boolean |  | 例: `True` |
| rows[].canFixApiReading | boolean |  | 例: `False` |
| rows[].timestamp | integer (int64) |  | 例: `1640000000000` |

## Create Sub-account API Key (For Master Account) (USER_DATA)（创建子账户API Key (适用母账户) (USER_DATA)）

`POST /sapi/v1/sub-account/subAccountApi`

Create a new API Key for a sub-account.

为子账户创建新的 API Key。

Operation ID: `createSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | Sub-account email<br>子账户邮箱<br>例: `123@test.com` |
| apiName | string | 是 | API Key name<br>API Key 名称<br>例: `myKey` |
| status | integer (int64) | 是 | IP restriction status. 1 = unrestricted, 2 = restricted to trusted IPs, 3 = third-party IP restriction<br>IP 限制状态。1 = 无限制，2 = 限定 IP，3 = 第三方 IP 限制<br>例: `2` |
| canTrade | boolean |  | Spot & Margin trading permission, default false<br>现货/杠杆交易权限，默认 false<br>例: `True` |
| canMarginLoanRepay | boolean |  | Margin borrow/repay permission, default false<br>杠杆借还款权限，默认 false<br>例: `False` |
| canFuturesTrade | boolean |  | Futures trading permission, default false<br>合约交易权限，默认 false<br>例: `False` |
| canUniversalTransfer | boolean |  | Universal transfer permission, default false<br>万能划转权限，默认 false<br>例: `False` |
| canVanillaOptions | boolean |  | Vanilla options permission, default false<br>欧式期权权限，默认 false<br>例: `False` |
| canFixApiTrading | boolean |  | FIX API Trading permission. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Trading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `True` |
| canFixApiReading | boolean |  | FIX API Reading permission. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Reading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `False` |
| ipAddress | string |  | Required when status=2. IP address list, max 500 chars<br>status=2 时必填。IP 地址列表，最长 500 个字符<br>例: `69.210.67.14` |
| thirdPartyName | string |  | Required when status=3. Third-party name<br>status=3 时必填。第三方名称<br>例: `thirdParty` |
| publicKey | string |  | Ed25519 public key (optional, for Ed25519 type API Key)<br>Ed25519 公钥（可选，用于 Ed25519 类型 API Key）<br>例: `` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create Sub-account API Key / 创建子账户 API Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiName | string |  | 例: `myKey` |
| apiKey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| secretKey | string |  | Secret Key. Returned only once on creation, please keep it safe.<br>Secret Key，仅创建时返回一次，请妥善保存<br>例: `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j` |
| canTrade | boolean |  | 例: `True` |
| canMarginLoanRepay | boolean |  | 例: `False` |
| canFuturesTrade | boolean |  | 例: `False` |
| canUniversalTransfer | boolean |  | 例: `False` |
| canVanillaOptions | boolean |  | 例: `False` |
| canFixApiTrading | boolean |  | 例: `True` |
| canFixApiReading | boolean |  | 例: `False` |
| status | integer (int64) |  | 例: `2` |
| ipList | string[] |  |  |

## Delete Sub-account API Key (For Master Account) (USER_DATA)（删除子账户API Key (适用母账户) (USER_DATA)）

`DELETE /sapi/v1/sub-account/subAccountApi`

Delete an API Key of a sub-account.

删除子账户的 API Key。

Operation ID: `deleteSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: https://www.binance.com/en/support/faq/detail/360002502072.<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：https://www.binance.com/cn/support/faq/detail/360002502072。<br>例: `API_KEY` |
| email | query | string | 是 | Sub-account email<br>子账户邮箱<br>例: `123@test.com` |
| subAccountApiKey | query | string | 是 | The sub-account API Key to be deleted<br>要删除的子账户 API Key<br>例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Delete Sub-account API Key / 删除子账户 API Key

```json
{}
```

## Create Sub-account API Key V2 (For Master Account) (USER_DATA)（创建子账户API Key V2 (适用母账户) (USER_DATA)）

`POST /sapi/v2/sub-account/subAccountApi`

Create a new API Key for a sub-account.

为子账户创建新的 API Key。

Operation ID: `createSubAccountApiKeyV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | Sub-account email<br>子账户邮箱<br>例: `123@test.com` |
| apiName | string | 是 | API Key name<br>API Key 名称<br>例: `my-fix-api` |
| status | integer (int64) | 是 | IP restriction status. 1 = unrestricted, 2 = restricted to trusted IPs, 3 = third-party IP restriction<br>IP 限制状态。1 = 无限制，2 = 限定 IP，3 = 第三方 IP 限制<br>例: `2` |
| canTrade | boolean |  | Spot & Margin trading permission, default false<br>现货/杠杆交易权限，默认 false<br>例: `True` |
| canMarginLoanRepay | boolean |  | Margin borrow/repay permission, default false<br>杠杆借还款权限，默认 false<br>例: `False` |
| canFuturesTrade | boolean |  | Futures trading permission, default false<br>合约交易权限，默认 false<br>例: `False` |
| canUniversalTransfer | boolean |  | Universal transfer permission, default false<br>万能划转权限，默认 false<br>例: `False` |
| canVanillaOptions | boolean |  | Vanilla options permission, default false<br>欧式期权权限，默认 false<br>例: `False` |
| canFixApiTrading | boolean |  | FIX API Trading permission. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Trading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `True` |
| canFixApiReading | boolean |  | FIX API Reading permission. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Reading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `True` |
| ipAddress | string |  | Required when status=2. IP address list, max 500 chars<br>status=2 时必填。IP 地址列表，最长 500 个字符<br>例: `1.2.3.4` |
| thirdPartyName | string |  | Required when status=3. Third-party name<br>status=3 时必填。第三方名称<br>例: `thirdParty` |
| publicKey | string |  | RSA or Ed25519 public key (optional). Must be sent in the request body; it is rejected if passed in the URL query string<br>RSA 或 Ed25519 公钥（可选）。必须放在请求体中，放在 URL 查询串中会被拒绝<br>例: `-----BEGIN PUBLIC KEY-----<br>MCowBQYDK2VwAyEAptEM59ao3nOD2baduIA830qZU4k4mqfvv7PwHVAfZhg=<br>-----END PUBLIC KEY-----` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create Sub-account API Key V2 / 创建子账户 API Key V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiName | string |  | 例: `myKey` |
| apiKey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| secretKey | string |  | Secret Key. Returned only once on creation, please keep it safe.<br>Secret Key，仅创建时返回一次，请妥善保存<br>例: `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j` |
| canTrade | boolean |  | 例: `True` |
| canMarginLoanRepay | boolean |  | 例: `False` |
| canFuturesTrade | boolean |  | 例: `False` |
| canUniversalTransfer | boolean |  | 例: `False` |
| canVanillaOptions | boolean |  | 例: `False` |
| canFixApiTrading | boolean |  | 例: `True` |
| canFixApiReading | boolean |  | 例: `False` |
| status | integer (int64) |  | 例: `2` |
| ipList | string[] |  |  |

## Delete IP List For a Sub-account API Key (For Master Account) (USER_DATA)（删除子账户API Key IP白名单 (适用母账户) (USER_DATA)）

`DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`

Delete IP List For a Sub-account API Key

删除子账户API Key IP白名单

Operation ID: `deleteIpListForASubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| subAccountApiKey | query | string | 是 | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| ipAddress | query | string | 是 | IPs to be deleted. Can be added in batches, separated by commas<br>想删除的 IP。可批量删除，用逗号分隔<br>例: `69.210.67.14` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Delete IP List For a Sub-account API Key / 删除子账户 API Key 的 IP 白名单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| ipRestrict | string |  | 例: `true` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1636371437000` |
| apiKey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |

## Get IP Restriction for a Sub-account API Key (For Master Account) (USER_DATA)（查询子账户API Key IP白名单 (适用母账户) (USER_DATA)）

`GET /sapi/v1/sub-account/subAccountApi/ipRestriction`

Get IP Restriction for a Sub-account API Key

查询子账户API Key IP白名单

Operation ID: `getIpRestrictionForASubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| subAccountApiKey | query | string | 是 | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get IP Restriction for a Sub-account API Key / 查询子账户 API Key 的 IP 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| ipRestrict | string |  | 例: `true` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1636371437000` |
| apiKey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |

## Modify Sub-account API Key Permission (For Master Account) (USER_DATA)（修改子账户API Key权限 (适用母账户) (USER_DATA)）

`POST /sapi/v1/sub-account/subAccountApiPermission`

Modify the trading permissions of a sub-account API Key.

修改子账户 API Key 的交易权限。

Operation ID: `modifySubAccountApiKeyPermission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | Sub-account email<br>子账户邮箱<br>例: `123@test.com` |
| subAccountApiKey | string | 是 | Sub-account API Key<br>子账户 API Key<br>例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| canTrade | boolean |  | Spot & Margin trading permission<br>现货/杠杆交易权限<br>例: `True` |
| canMarginLoanRepay | boolean |  | Margin borrow/repay permission<br>杠杆借还款权限<br>例: `False` |
| canFuturesTrade | boolean |  | Futures trading permission<br>合约交易权限<br>例: `True` |
| canUniversalTransfer | boolean |  | Universal transfer permission<br>万能划转权限<br>例: `False` |
| canVanillaOptions | boolean |  | Vanilla options permission<br>欧式期权权限<br>例: `False` |
| canFixApiTrading | boolean |  | FIX API Trading permission. If omitted, the existing value is unchanged. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Trading 权限。不传则不修改。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `True` |
| canFixApiReading | boolean |  | FIX API Reading permission. If omitted, the existing value is unchanged. Only supported for API Keys using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000` `Unsupported operation`<br>FIX API Reading 权限。不传则不修改。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported operation`<br>例: `False` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Sub-account API Key Permission / 修改子账户 API Key 权限

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiName | string |  | 例: `myKey` |
| apikey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| canTrade | boolean |  | 例: `True` |
| canMarginLoanRepay | boolean |  | 例: `False` |
| canFuturesTrade | boolean |  | 例: `True` |
| canUniversalTransfer | boolean |  | 例: `False` |
| canVanillaOptions | boolean |  | 例: `False` |
| canFixApiTrading | boolean |  | 例: `True` |
| canFixApiReading | boolean |  | 例: `False` |
| timestamp | integer (int64) |  | 例: `1640000000000` |

## Futures Transfer for Sub-account (For Master Account) (USER_DATA)（子账户合约划转 (仅适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/futures/transfer`

Futures Transfer for Sub-account

子账户合约划转

Operation ID: `futuresTransferForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | 例: `123@test.com` |
| asset | string | 是 | The asset being transferred<br>划转的资产<br>例: `USDT` |
| amount | number (float) | 是 | The amount to be transferred<br>划转数量<br>例: `1.0` |
| type | integer (int64) | 是 | 1: transfer from subaccount's spot account to its USDT-margined futures account 2: transfer from<br>subaccount's USDT-margined futures account to its spot account 3: transfer from subaccount's spot<br>account to its COIN-margined futures account 4: transfer from subaccount's COIN-margined futures<br>account to its spot account<br>1: 子账户现货账户划转到其 U 本位合约账户 2: 子账户 U 本位合约账户划转到其现货账户 3: 子账户现货账户划转到其币本位合约账户 4: 子账户币本位合约账户划转到其现货账户<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Transfer for Sub-account / 子账户合约划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |

## Get Detail on Sub-account's Futures Account (For Master Account) (USER_DATA)（查询子账户合约账户详情 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/futures/account`

Get Detail on Sub-account's Futures Account

查询子账户合约账户详情

Operation ID: `getDetailOnSubAccountsFuturesAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Detail on Sub-account's Futures Account / 查询子账户合约账户详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string |  | 例: `abc@test.com` |
| asset | string |  | 例: `USDT` |
| assets | object[] |  |  |
| assets[].asset | string |  | 例: `USDT` |
| assets[].initialMargin | string |  | 例: `0.00000000` |
| assets[].maintenanceMargin | string |  | 例: `0.00000000` |
| assets[].marginBalance | string |  | 例: `0.88308000` |
| assets[].maxWithdrawAmount | string |  | 例: `0.88308000` |
| assets[].openOrderInitialMargin | string |  | 例: `0.00000000` |
| assets[].positionInitialMargin | string |  | 例: `0.00000000` |
| assets[].unrealizedProfit | string |  | 例: `0.00000000` |
| assets[].walletBalance | string |  | 例: `0.88308000` |
| canDeposit | boolean |  | 例: `True` |
| canTrade | boolean |  | 例: `True` |
| canWithdraw | boolean |  | 例: `True` |
| feeTier | integer (int64) |  | 例: `2` |
| maxWithdrawAmount | string |  | 例: `0.88308000` |
| totalInitialMargin | string |  | 例: `0.00000000` |
| totalMaintenanceMargin | string |  | 例: `0.00000000` |
| totalMarginBalance | string |  | 例: `0.88308000` |
| totalOpenOrderInitialMargin | string |  | 例: `0.00000000` |
| totalPositionInitialMargin | string |  | 例: `0.00000000` |
| totalUnrealizedProfit | string |  | 例: `0.00000000` |
| totalWalletBalance | string |  | 例: `0.88308000` |
| updateTime | integer (int64) |  | 例: `1576756674610` |

## Get Detail on Sub-account's Futures Account V2 (For Master Account) (USER_DATA)（查询子账户合约账户详情 V2 (适用主账户) (USER_DATA)）

`GET /sapi/v2/sub-account/futures/account`

Get Detail on Sub-account's Futures Account

查询子账户合约账户详情

Operation ID: `getDetailOnSubAccountsFuturesAccountV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| futuresType | query | integer (int64) | 是 | 1: USDT-margined Futures，2: Coin-margined Futures<br>1: USDT合约，2: 币本位合约<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Detail on Sub-account's Futures Account V2 / 查询子账户合约账户详情 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| futureAccountResp | object |  |  |
| futureAccountResp.email | string |  | 例: `abc@test.com` |
| futureAccountResp.assets | object[] |  |  |
| futureAccountResp.assets[].asset | string |  | 例: `USDT` |
| futureAccountResp.assets[].initialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.assets[].maintenanceMargin | string |  | 例: `0.00000000` |
| futureAccountResp.assets[].marginBalance | string |  | 例: `0.88308000` |
| futureAccountResp.assets[].maxWithdrawAmount | string |  | 例: `0.88308000` |
| futureAccountResp.assets[].openOrderInitialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.assets[].positionInitialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.assets[].unrealizedProfit | string |  | 例: `0.00000000` |
| futureAccountResp.assets[].walletBalance | string |  | 例: `0.88308000` |
| futureAccountResp.canDeposit | boolean |  | 例: `True` |
| futureAccountResp.canTrade | boolean |  | 例: `True` |
| futureAccountResp.canWithdraw | boolean |  | 例: `True` |
| futureAccountResp.feeTier | integer (int64) |  | 例: `2` |
| futureAccountResp.maxWithdrawAmount | string |  | 例: `0.88308000` |
| futureAccountResp.totalInitialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.totalMaintenanceMargin | string |  | 例: `0.00000000` |
| futureAccountResp.totalMarginBalance | string |  | 例: `0.88308000` |
| futureAccountResp.totalOpenOrderInitialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.totalPositionInitialMargin | string |  | 例: `0.00000000` |
| futureAccountResp.totalUnrealizedProfit | string |  | 例: `0.00000000` |
| futureAccountResp.totalWalletBalance | string |  | 例: `0.88308000` |
| futureAccountResp.updateTime | integer (int64) |  | 例: `1576756674610` |
| deliveryAccountResp | object |  |  |
| deliveryAccountResp.email | string |  | 例: `abc@test.com` |
| deliveryAccountResp.assets | object[] |  |  |
| deliveryAccountResp.assets[].asset | string |  | 例: `BTC` |
| deliveryAccountResp.assets[].initialMargin | string |  | 例: `0.00000000` |
| deliveryAccountResp.assets[].maintenanceMargin | string |  | 例: `0.00000000` |
| deliveryAccountResp.assets[].marginBalance | string |  | 例: `0.88308000` |
| deliveryAccountResp.assets[].maxWithdrawAmount | string |  | 例: `0.88308000` |
| deliveryAccountResp.assets[].openOrderInitialMargin | string |  | 例: `0.00000000` |
| deliveryAccountResp.assets[].positionInitialMargin | string |  | 例: `0.00000000` |
| deliveryAccountResp.assets[].unrealizedProfit | string |  | 例: `0.00000000` |
| deliveryAccountResp.assets[].walletBalance | string |  | 例: `0.88308000` |
| deliveryAccountResp.canDeposit | boolean |  | 例: `True` |
| deliveryAccountResp.canTrade | boolean |  | 例: `True` |
| deliveryAccountResp.canWithdraw | boolean |  | 例: `True` |
| deliveryAccountResp.feeTier | integer (int64) |  | 例: `2` |
| deliveryAccountResp.updateTime | integer (int64) |  | 例: `1598959682001` |

## Get Detail on Sub-account's Margin Account (For Master Account) (USER_DATA)（查询子账户杠杆账户详情 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/margin/account`

Get Detail on Sub-account's Margin Account

查询子账户杠杆账户详情

Operation ID: `getDetailOnSubAccountsMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Detail on Sub-account's Margin Account / 查询子账户杠杆账户详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string |  | 例: `123@test.com` |
| marginLevel | string |  | 例: `11.64405625` |
| totalAssetOfBtc | string |  | 例: `6.82728457` |
| totalLiabilityOfBtc | string |  | 例: `0.58633215` |
| totalNetAssetOfBtc | string |  | 例: `6.24095242` |
| marginTradeCoeffVo | object |  |  |
| marginTradeCoeffVo.forceLiquidationBar | string |  | Liquidation margin ratio<br>强平风险率<br>例: `1.10000000` |
| marginTradeCoeffVo.marginCallBar | string |  | Margin call margin ratio<br>补仓风险率<br>例: `1.50000000` |
| marginTradeCoeffVo.normalBar | string |  | Initial margin ratio<br>初始风险率<br>例: `2.00000000` |
| marginUserAssetVoList | object[] |  |  |
| marginUserAssetVoList[].asset | string |  | 例: `BTC` |
| marginUserAssetVoList[].borrowed | string |  | 例: `0.00000000` |
| marginUserAssetVoList[].free | string |  | 例: `0.00499500` |
| marginUserAssetVoList[].interest | string |  | 例: `0.00000000` |
| marginUserAssetVoList[].locked | string |  | 例: `0.00000000` |
| marginUserAssetVoList[].netAsset | string |  | 例: `0.00499500` |

## Get Move Position History for Sub-account (For Master Account) (USER_DATA)（查询账户移仓历史 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/futures/move-position`

Query move position history

查询账户移仓历史

Operation ID: `getMovePositionHistoryForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| productType | query | string |  | Default UM.<br>默认 UM。<br>枚举: `UM`, `OPTION`<br>例: `UM` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) | 是 | 例: `1` |
| rows | query | integer (int64) | 是 | Max 100.<br>最大 100。<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Move Position History for Sub-account / 查询子账户移仓历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `3` |
| futureMovePositionOrderVoList | object[] |  |  |
| futureMovePositionOrderVoList[].fromUserEmail | string |  | 例: `testFrom@google.com` |
| futureMovePositionOrderVoList[].toUserEmail | string |  | 例: `testTo@google.com` |
| futureMovePositionOrderVoList[].productType | string |  | 例: `UM` |
| futureMovePositionOrderVoList[].symbol | string |  | 例: `BTCUSDT` |
| futureMovePositionOrderVoList[].price | string |  | 例: `105025.50981609` |
| futureMovePositionOrderVoList[].quantity | string |  | 例: `0.00100000` |
| futureMovePositionOrderVoList[].positionSide | string |  | 例: `BOTH` |
| futureMovePositionOrderVoList[].side | string |  | 例: `SELL` |
| futureMovePositionOrderVoList[].timeStamp | integer (int64) |  | 例: `1737544712000` |

## Move Position for Sub-account (For Master Account) (USER_DATA)（移仓功能 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/futures/move-position`

Move position between sub-master, master-sub, or sub-sub accounts when necessary

支持主账户和母账户，子账户和子账户之间的移仓

Operation ID: `movePositionForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromUserEmail | string | 是 | 例: `testFrom@google.com` |
| toUserEmail | string | 是 | 例: `testTo@google.com` |
| productType | string | 是 | A single request cannot mix UM and OPTION positions.<br>单次请求不支持 UM 和 OPTION 混合提交。<br>枚举: `UM`, `OPTION`<br>例: `UM` |
| orderArgs | object[] | 是 | Max 10 positions supported. When input request parameter,orderArgs.symbol should be STRING,<br>orderArgs.quantity should be BIGDECIMAL, and orderArgs.positionSide should be STRING, positionSide<br>support BOTH,LONG and SHORT. Each entry should be like<br>orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. Example of<br>the request parameter array: orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001<br>orderArgs[0].positionSide=BOTH orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01<br>orderArgs[1].positionSide=BOTH<br>一次最多支持 10 个仓位转移. orderArgs.symbol的参数类型为STRING, orderArgs.quantity的参数类型为BIGDECIMAL,<br>orderArgs.positionSide的参数类型为STRING, positionSide 支持 BOTH,LONG and SHORT. 请求参数格式如下<br>orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. 举例:<br>orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001 orderArgs[0].positionSide=BOTH<br>orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01 orderArgs[1].positionSide=BOTH |
| orderArgs[].symbol | string |  | 例: `BTCUSDT` |
| orderArgs[].quantity | number (float) |  | 例: `0.001` |
| orderArgs[].positionSide | string |  | Required when productType=UM. Optional and ignored when productType=OPTION (the response returns positionSide as null).<br>productType=UM 时必填；productType=OPTION 时可选且会被忽略（响应中 positionSide 返回 null）。<br>例: `BOTH` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Move Position for Sub-account / 子账户移仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| movePositionOrders | object[] |  |  |
| movePositionOrders[].fromUserEmail | string |  | 例: `testFrom@google.com` |
| movePositionOrders[].toUserEmail | string |  | 例: `testTo@google.com` |
| movePositionOrders[].productType | string |  | 例: `UM` |
| movePositionOrders[].symbol | string |  | 例: `BTCUSDT` |
| movePositionOrders[].priceType | string |  | 例: `MARK_PRICE` |
| movePositionOrders[].price | string |  | 例: `97139.00000000` |
| movePositionOrders[].quantity | string |  | 例: `0.001` |
| movePositionOrders[].positionSide | string |  | null when productType=OPTION.<br>productType=OPTION 时返回 null。<br>例: `BOTH` |
| movePositionOrders[].side | string |  | 例: `BUY` |
| movePositionOrders[].success | boolean |  | 例: `True` |

## Get Sub-account Deposit Address (For Master Account) (USER_DATA)（获取子账户充值地址 (适用主账户) (USER_DATA)）

`GET /sapi/v1/capital/deposit/subAddress`

Fetch sub-account deposit address

获取子账户充值地址

Operation ID: `getSubAccountDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| coin | query | string | 是 | 例: `BTC` |
| network | query | string |  | networks can be found in `GET /sapi/v1/capital/deposit/address`<br>网络可以在`GET /sapi/v1/capital/deposit/address`获取<br>例: `None` |
| amount | query | number (float) |  | 例: `1.0` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Sub-account Deposit Address / 获取子账户充值地址

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| address | string |  | 例: `TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV` |
| coin | string |  | 例: `USDT` |
| tag | string |  | 例: `` |
| url | string |  | 例: `https://tronscan.org/#/address/TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV` |

## Get Sub-account Deposit History (For Master Account) (USER_DATA)（获取子账户充值记录 (适用主账户) (USER_DATA)）

`GET /sapi/v1/capital/deposit/subHisrec`

Fetch sub-account deposit history

获取子账户充值记录

Operation ID: `getSubAccountDepositHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| includeSource | query | boolean |  | Default `false`, return `sourceAddress` field when set to `true`<br>默认 `false`，如果为`true`时会返回`sourceAddress`字段<br>默认: `False`<br>例: `False` |
| coin | query | string |  | 例: `BTC` |
| status | query | integer (int64) |  | Deposit status: 0=pending, 6=credited but cannot withdraw, 7=wrong deposit, 8=waiting user confirmation, 1=success.<br>充值状态：0=待处理，6=已入账但不可提币，7=错误充值，8=等待用户确认，1=成功。<br>例: `0` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| txId | query | string |  | 例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Sub-account Deposit History / 获取子账户充值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | 例: `769800519366885376` |
| [].amount | string |  | 例: `0.001` |
| [].coin | string |  | 例: `BNB` |
| [].network | string |  | 例: `BNB` |
| [].status | integer (int64) |  | Deposit status: 0=pending, 6=credited but cannot withdraw, 7=wrong deposit, 8=waiting user confirmation, 1=success.<br>充值状态：0=待处理，6=已入账但不可提币，7=错误充值，8=等待用户确认，1=成功。<br>例: `0` |
| [].address | string |  | 例: `bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23` |
| [].addressTag | string |  | 例: `101764890` |
| [].txId | string |  | 例: `98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC` |
| [].insertTime | integer (int64) |  | 例: `1661493146000` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].confirmTimes | string |  | 例: `1/1` |
| [].unlockConfirm | integer (int64) |  | 例: `0` |
| [].walletType | integer (int64) |  | 例: `0` |

## Get Summary of Sub-account's Futures Account (For Master Account) (USER_DATA)（查询子账户合约账户汇总 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/futures/accountSummary`

Get Summary of Sub-account's Futures Account

查询子账户合约账户汇总

Operation ID: `getSummaryOfSubAccountsFuturesAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| page | query | integer (int64) | 是 | 例: `1` |
| limit | query | integer (int64) | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Summary of Sub-account's Futures Account / 查询子账户合约账户汇总

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalInitialMargin | string |  | 例: `9.83137400` |
| totalMaintenanceMargin | string |  | 例: `0.41568700` |
| totalMarginBalance | string |  | 例: `23.03235621` |
| totalOpenOrderInitialMargin | string |  | 例: `9.00000000` |
| totalPositionInitialMargin | string |  | 例: `0.83137400` |
| totalUnrealizedProfit | string |  | 例: `0.03219710` |
| totalWalletBalance | string |  | 例: `22.15879444` |
| asset | string |  | The sum of BUSD and USDT<br>USDT和BUSD资产汇总<br>例: `USD` |
| subAccountList | object[] |  |  |
| subAccountList[].email | string |  | 例: `123@test.com` |
| subAccountList[].totalInitialMargin | string |  | 例: `9.00000000` |
| subAccountList[].totalMaintenanceMargin | string |  | 例: `0.00000000` |
| subAccountList[].totalMarginBalance | string |  | 例: `22.12659734` |
| subAccountList[].totalOpenOrderInitialMargin | string |  | 例: `9.00000000` |
| subAccountList[].totalPositionInitialMargin | string |  | 例: `0.00000000` |
| subAccountList[].totalUnrealizedProfit | string |  | 例: `0.00000000` |
| subAccountList[].totalWalletBalance | string |  | 例: `22.12659734` |
| subAccountList[].asset | string |  | The sum of BUSD and USDT<br>USDT和BUSD资产汇总<br>例: `USD` |

## Get Summary of Sub-account's Futures Account V2 (For Master Account) (USER_DATA)（查询子账户合约账户汇总 V2 (适用主账户) (USER_DATA)）

`GET /sapi/v2/sub-account/futures/accountSummary`

Get Summary of Sub-account's Futures Account

查询子账户合约账户汇总

Operation ID: `getSummaryOfSubAccountsFuturesAccountV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| futuresType | query | integer (int64) | 是 | 1: USDT-margined Futures，2: Coin-margined Futures<br>1: USDT合约，2: 币本位合约<br>例: `1` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Summary of Sub-account's Futures Account V2 / 查询子账户合约账户汇总 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| futureAccountSummaryResp | object |  |  |
| futureAccountSummaryResp.totalInitialMargin | string |  | 例: `9.83137400` |
| futureAccountSummaryResp.totalMaintenanceMargin | string |  | 例: `0.41568700` |
| futureAccountSummaryResp.totalMarginBalance | string |  | 例: `23.03235621` |
| futureAccountSummaryResp.totalOpenOrderInitialMargin | string |  | 例: `9.00000000` |
| futureAccountSummaryResp.totalPositionInitialMargin | string |  | 例: `0.83137400` |
| futureAccountSummaryResp.totalUnrealizedProfit | string |  | 例: `0.03219710` |
| futureAccountSummaryResp.totalWalletBalance | string |  | 例: `22.15879444` |
| futureAccountSummaryResp.asset | string |  | The sum of BUSD and USDT<br>USDT和BUSD资产汇总<br>例: `USD` |
| futureAccountSummaryResp.subAccountList | object[] |  |  |
| futureAccountSummaryResp.subAccountList[].email | string |  | 例: `123@test.com` |
| futureAccountSummaryResp.subAccountList[].totalInitialMargin | string |  | 例: `9.00000000` |
| futureAccountSummaryResp.subAccountList[].totalMaintenanceMargin | string |  | 例: `0.00000000` |
| futureAccountSummaryResp.subAccountList[].totalMarginBalance | string |  | 例: `22.12659734` |
| futureAccountSummaryResp.subAccountList[].totalOpenOrderInitialMargin | string |  | 例: `9.00000000` |
| futureAccountSummaryResp.subAccountList[].totalPositionInitialMargin | string |  | 例: `0.00000000` |
| futureAccountSummaryResp.subAccountList[].totalUnrealizedProfit | string |  | 例: `0.00000000` |
| futureAccountSummaryResp.subAccountList[].totalWalletBalance | string |  | 例: `22.12659734` |
| futureAccountSummaryResp.subAccountList[].asset | string |  | The sum of BUSD and USDT<br>USDT和BUSD资产汇总<br>例: `USD` |
| deliveryAccountSummaryResp | object |  |  |
| deliveryAccountSummaryResp.totalMarginBalanceOfBTC | string |  | 例: `25.03221121` |
| deliveryAccountSummaryResp.totalUnrealizedProfitOfBTC | string |  | 例: `0.12233410` |
| deliveryAccountSummaryResp.totalWalletBalanceOfBTC | string |  | 例: `22.15879444` |
| deliveryAccountSummaryResp.asset | string |  | 例: `BTC` |
| deliveryAccountSummaryResp.subAccountList | object[] |  |  |
| deliveryAccountSummaryResp.subAccountList[].email | string |  | 例: `123@test.com` |
| deliveryAccountSummaryResp.subAccountList[].totalMarginBalance | string |  | 例: `22.12659734` |
| deliveryAccountSummaryResp.subAccountList[].totalUnrealizedProfit | string |  | 例: `0.00000000` |
| deliveryAccountSummaryResp.subAccountList[].totalWalletBalance | string |  | 例: `22.12659734` |
| deliveryAccountSummaryResp.subAccountList[].asset | string |  | 例: `BTC` |

## Get Summary of Sub-account's Margin Account (For Master Account) (USER_DATA)（查询子账户杠杆账户汇总 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/margin/accountSummary`

Get Summary of Sub-account's Margin Account

查询子账户杠杆账户汇总

Operation ID: `getSummaryOfSubAccountsMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Summary of Sub-account's Margin Account / 查询子账户杠杆账户汇总

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAssetOfBtc | string |  | 例: `4.33333333` |
| totalLiabilityOfBtc | string |  | 例: `2.11111112` |
| totalNetAssetOfBtc | string |  | 例: `2.22222221` |
| subAccountList | object[] |  |  |
| subAccountList[].email | string |  | 例: `123@test.com` |
| subAccountList[].totalAssetOfBtc | string |  | 例: `2.11111111` |
| subAccountList[].totalLiabilityOfBtc | string |  | 例: `1.11111111` |
| subAccountList[].totalNetAssetOfBtc | string |  | 例: `1.00000000` |

## Margin Transfer for Sub-account (For Master Account) (USER_DATA)（子账户杠杆划转 (仅适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/margin/transfer`

Margin Transfer for Sub-account

子账户杠杆划转

Operation ID: `marginTransferForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| email | string | 是 | 例: `123@test.com` |
| asset | string | 是 | The asset being transferred<br>划转资产<br>例: `BTC` |
| amount | number (float) | 是 | The amount to be transferred<br>划转数量<br>例: `1.0` |
| type | integer (int64) | 是 | 1: transfer from subaccount's spot account to margin account 2: transfer from subaccount's margin<br>account to its spot account<br>1: 由子账户的现货账户划转至其杠杆账户; 2: 由子账户的杠杆账户划转至其现货账户<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Transfer for Sub-account / 子账户杠杆划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |

## Query Sub-account Assets (For Master Account) (USER_DATA)（查询子账户资产 (适用主账户) (USER_DATA)）

`GET /sapi/v3/sub-account/assets`

Fetch sub-account assets

查询子账户资产

Operation ID: `querySubAccountAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Assets / 子账户资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| balances | object[] |  |  |
| balances[].freeze | integer (int64) |  | 例: `0` |
| balances[].withdrawing | integer (int64) |  | 例: `0` |
| balances[].asset | string |  | 例: `ADA` |
| balances[].free | number (float) |  | 例: `11467.6399` |
| balances[].locked | integer (int64) |  | 例: `0` |

## Query Sub-account Assets V4 (For Master Account) (USER_DATA)（查询子账户资产 (适用主账户) (USER_DATA)）

`GET /sapi/v4/sub-account/assets`

Fetch sub-account assets

获取子账户资产

Operation ID: `querySubAccountAssetsAssetManagement`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Assets / 子账户资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| balances | object[] |  |  |
| balances[].freeze | string |  | 例: `0` |
| balances[].withdrawing | string |  | 例: `0` |
| balances[].asset | string |  | 例: `ADA` |
| balances[].free | string |  | 例: `10000` |
| balances[].locked | string |  | 例: `0` |

## Query Sub-account Futures Asset Transfer History (For Master Account) (USER_DATA)（查询子账户合约资金划转历史 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/futures/internalTransfer`

Query Sub-account Futures Asset Transfer History

查询子账户合约资金划转历史

Operation ID: `querySubAccountFuturesAssetTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `123@test.com` |
| futuresType | query | integer (int64) | 是 | 1: USDT-margined Futures，2: Coin-margined Futures<br>1: USDT合约，2: 币本位合约<br>例: `1` |
| startTime | query | integer (int64) |  | Cannot be earlier than 1 month ago<br>只能查询近一个月内历史纪录<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `50`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Futures Asset Transfer History / 查询子账户合约资产划转历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| futuresType | integer (int64) |  | 例: `2` |
| transfers | object[] |  |  |
| transfers[].from | string |  | 例: `aaa@test.com` |
| transfers[].to | string |  | 例: `bbb@test.com` |
| transfers[].asset | string |  | 例: `BTC` |
| transfers[].qty | string |  | 例: `1` |
| transfers[].tranId | integer (int64) |  | 例: `11897001102` |
| transfers[].time | integer (int64) |  | 例: `1544433328000` |

## Sub-account Futures Asset Transfer (For Master Account) (USER_DATA)（执行子账户合约资金划转 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/futures/internalTransfer`

Sub-account Futures Asset Transfer

执行子账户合约资金划转

Operation ID: `subAccountFuturesAssetTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromEmail | string | 是 | Sender email<br>发送者邮箱<br>例: `abc@test.com` |
| toEmail | string | 是 | Recipient email<br>接收者邮箱<br>例: `def@test.com` |
| futuresType | integer (int64) | 是 | 1: USDT-margined Futures，2: Coin-margined Futures<br>1: USDT合约， 2: 币本位合约<br>例: `1` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Futures Asset Transfer / 执行子账户合约资产划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| txnId | string |  | 例: `2934662589` |

## Query Sub-account Spot Assets Summary (For Master Account) (USER_DATA)（查询子账户现货资产汇总 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/spotSummary`

Get BTC valued asset summary of subaccounts.

获取BTC计价的子账户现货资产汇总。

Operation ID: `querySubAccountSpotAssetsSummary`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string |  | Managed sub-account email<br>托管子账户邮箱<br>例: `123@test.com` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Spot Assets Summary / 查询子账户现货资产汇总

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalCount | integer (int64) |  | 例: `2` |
| masterAccountTotalAsset | string |  | 例: `0.23231201` |
| spotSubUserAssetBtcVoList | object[] |  |  |
| spotSubUserAssetBtcVoList[].email | string |  | 例: `sub123@test.com` |
| spotSubUserAssetBtcVoList[].totalAsset | string |  | 例: `9999.00000000` |

## Query Sub-account Spot Asset Transfer History (For Master Account) (USER_DATA)（查询子账户现货资金划转历史 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/sub/transfer/history`

Query Sub-account Spot Asset Transfer History

查询子账户现货资金划转历史

Operation ID: `querySubAccountSpotAssetTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| fromEmail | query | string |  | 例: `aaa@test.com` |
| toEmail | query | string |  | 例: `bbb@test.com` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Spot Asset Transfer History / 查询子账户现货资产划转历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].from | string |  | 例: `aaa@test.com` |
| [].to | string |  | 例: `bbb@test.com` |
| [].asset | string |  | 例: `BTC` |
| [].qty | string |  | 例: `10` |
| [].status | string |  | 例: `SUCCESS` |
| [].tranId | integer (int64) |  | 例: `6489943656` |
| [].time | integer (int64) |  | 例: `1544433328000` |

## Query Universal Transfer History (For Master Account) (USER_DATA)（查询子母账户万能划转历史 (适用主账户) (USER_DATA)）

`GET /sapi/v1/sub-account/universalTransfer`

Query Universal Transfer History

查询子母账户万能划转历史

Operation ID: `queryUniversalTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| fromEmail | query | string |  | 例: `abctest@gmail.com` |
| toEmail | query | string |  | 例: `deftest@gmail.com` |
| clientTranId | query | string |  | 例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Universal Transfer History / 万能划转 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| result | object[] |  |  |
| result[].tranId | integer (int64) |  | 例: `92275823339` |
| result[].fromEmail | string |  | 例: `abctest@gmail.com` |
| result[].toEmail | string |  | 例: `deftest@gmail.com` |
| result[].asset | string |  | 例: `BNB` |
| result[].amount | string |  | 例: `0.01` |
| result[].createTimeStamp | integer (int64) |  | 例: `1640317374000` |
| result[].fromAccountType | string |  | 例: `USDT_FUTURE` |
| result[].toAccountType | string |  | 例: `SPOT` |
| result[].status | string |  | 例: `SUCCESS` |
| result[].clientTranId | string |  | 例: `test` |
| totalCount | integer (int64) |  | 例: `1` |

## Universal Transfer (For Master Account) (USER_DATA)（子母账户万能划转 (适用主账户) (USER_DATA)）

`POST /sapi/v1/sub-account/universalTransfer`

Universal Transfer

子母账户万能划转

Operation ID: `universalTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromEmail | string |  | 例: `abc@test.com` |
| toEmail | string |  | 例: `def@test.com` |
| fromAccountType | string | 是 | 枚举: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`, `MARGIN`, `ISOLATED_MARGIN`<br>例: `SPOT` |
| toAccountType | string | 是 | 枚举: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`, `MARGIN`, `ISOLATED_MARGIN`<br>例: `SPOT` |
| clientTranId | string |  | Must be unique<br>不可重复<br>例: `1` |
| symbol | string |  | Only supported under ISOLATED_MARGIN type<br>仅在ISOLATED_MARGIN类型下使用<br>例: `BTCUSDT` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Universal Transfer / 万能划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | 例: `11945860693` |
| clientTranId | string |  | 例: `test` |

## Sub-account Transfer History (For Sub-account) (USER_DATA)（查询子账户划转历史 (仅适用子账户) (USER_DATA)）

`GET /sapi/v1/sub-account/transfer/subUserHistory`

Sub-account Transfer History

查询子账户划转历史

Operation ID: `subAccountTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | If not sent, result of all assets will be returned<br>如不提供，返回所有asset 划转记录<br>例: `BTC` |
| type | query | integer (int64) |  | 1: transfer in, 2: transfer out<br>1: 转入，2: 转出；如不提供，返回转出方向划转记录<br>例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `10` |
| returnFailHistory | query | boolean |  | Default `False`, return PROCESS and SUCCESS status history; If `True`,return PROCESS and SUCCESS and FAILURE<br>status history<br>默认 `false`，返回 PROCESS 和 SUCCESS 状态的数据；若传 `true`，返回 PROCESS、SUCCESS、FAILURE 状态的数据。<br>默认: `False`<br>例: `False` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-account Transfer History / 查询子账户划转历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].counterParty | string |  | 例: `master` |
| [].email | string |  | 例: `master@test.com` |
| [].type | integer (int64) |  | 1 for transfer in, 2 for transfer out<br>1 for transfer in , 2 for transfer out<br>例: `1` |
| [].asset | string |  | 例: `BTC` |
| [].qty | string |  | 例: `1` |
| [].fromAccountType | string |  | 例: `SPOT` |
| [].toAccountType | string |  | 例: `SPOT` |
| [].status | string |  | status: PROCESS / SUCCESS / FAILURE<br>例: `SUCCESS` |
| [].tranId | integer (int64) |  | 例: `11798835829` |
| [].time | integer (int64) |  | 例: `1544433325000` |

## Transfer to Master (For Sub-account) (USER_DATA)（向主账户主动划转 (仅适用子账户) (USER_DATA)）

`POST /sapi/v1/sub-account/transfer/subToMaster`

Transfer to Master

向主账户主动划转

Operation ID: `transferToMaster`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Transfer to Master / 划转至主账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |

## Transfer to Sub-account of Same Master (For Sub-account) (USER_DATA)（向共同主账户下的子账户主动划转 (仅适用子账户) (USER_DATA)）

`POST /sapi/v1/sub-account/transfer/subToSub`

Transfer to Sub-account of Same Master

向共同主账户下的子账户主动划转

Operation ID: `transferToSubAccountOfSameMaster`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| toEmail | string | 是 | 例: `abc@test.com` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Transfer to Sub-account of Same Master / 划转至同一主账户下的子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |

## Deposit Assets Into The Managed Sub-account (For Investor Master Account) (USER_DATA)（投资人账户为托管子账户充值资产 (适用投资人母账户) (USER_DATA)）

`POST /sapi/v1/managed-subaccount/deposit`

Deposit Assets Into The Managed Sub-account

投资人账户为托管子账户充值资产(适用投资人母账户)

Operation ID: `depositAssetsIntoTheManagedSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| toEmail | string | 是 | 例: `abc@test.com` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Deposit Assets Into The Managed Sub-account / 投资人账户为托管子账户充值资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | 例: `66157362489` |

## Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA)（获取托管子账户充值地址 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/deposit/address`

Get investor's managed sub-account deposit address.

获取投资人之托管子账户充值地址

Operation ID: `getManagedSubAccountDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| coin | query | string | 是 | 例: `USDT` |
| network | query | string |  | networks can be found in `GET /sapi/v1/capital/deposit/address`<br>网络可以在`GET /sapi/v1/capital/deposit/address`获取<br>例: `LIGHTNING` |
| amount | query | number (float) |  | 例: `1.0` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Managed Sub-account Deposit Address / 获取托管子账户充值地址

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string |  | 例: `USDT` |
| address | string |  | 例: `0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d` |
| tag | string |  | 例: `` |
| url | string |  | 例: `https://etherscan.io/address/0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d` |

## Query Managed Sub-account Asset Details (For Investor Master Account) (USER_DATA)（投资人账户查询托管子账户资产 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/asset`

Query Managed Sub-account Asset Details

投资人账户查询托管子账户资产

Operation ID: `queryManagedSubAccountAssetDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub-account Asset Details / 查询托管子账户资产详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].coin | string |  | 例: `INJ` |
| [].name | string |  | 例: `Injective Protocol` |
| [].totalBalance | string |  | 例: `0` |
| [].availableBalance | string |  | 例: `0` |
| [].inOrder | string |  | 例: `0` |
| [].btcValue | string |  | 例: `0` |

## Query Managed Sub-account Futures Asset Details (For Investor Master Account) (USER_DATA)（投资人账户查询托管子账户期货资产 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/fetch-future-asset`

Investor can use this api to query managed sub account futures asset details

投资人可以根据此接口查询其托管子账户期货资产

Operation ID: `queryManagedSubAccountFuturesAssetDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| accountType | query | string |  | No input or input "USDT_FUTURE" to get UM Futures account details. Input "COIN_FUTURE" to get CM Futures account details.<br>不传或传入 "USDT_FUTURE" 获取 U 本位合约账户详情。传入 "COIN_FUTURE" 获取币本位合约账户详情。<br>例: `MARGIN` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub-account Futures Asset Details / 查询托管子账户合约资产详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `200` |
| message | string |  | 例: `OK` |
| snapshotVos | object[] |  |  |
| snapshotVos[].type | string |  | 例: `FUTURES` |
| snapshotVos[].updateTime | integer (int64) |  | 例: `1672893855394` |
| snapshotVos[].data | object |  |  |
| snapshotVos[].data.assets | object[] |  |  |
| snapshotVos[].data.assets[].asset | string |  | 例: `USDT` |
| snapshotVos[].data.assets[].marginBalance | integer (int64) |  | 例: `100` |
| snapshotVos[].data.assets[].walletBalance | integer (int64) |  | 例: `120` |
| snapshotVos[].data.position | object[] |  |  |
| snapshotVos[].data.position[].symbol | string |  | 例: `BTCUSDT` |
| snapshotVos[].data.position[].entryPrice | integer (int64) |  | 例: `17000` |
| snapshotVos[].data.position[].markPrice | integer (int64) |  | 例: `17000` |
| snapshotVos[].data.position[].positionAmt | number (float) |  | 例: `0.0001` |

## Query Managed Sub-account List (For Investor) (USER_DATA)（查询托管子账户列表 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/info`

Get investor's managed sub-account list.

获取投资人之托管子账户列表

Operation ID: `queryManagedSubAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string |  | 例: `abc@test.com` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `20`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub-account List / 查询托管子账户列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `3` |
| managerSubUserInfoVoList | object[] |  |  |
| managerSubUserInfoVoList[].rootUserId | integer (int64) |  | 例: `1000138475670` |
| managerSubUserInfoVoList[].managersubUserId | integer (int64) |  | 例: `1000137842513` |
| managerSubUserInfoVoList[].bindParentUserId | integer (int64) |  | 例: `1000138475669` |
| managerSubUserInfoVoList[].email | string |  | 例: `test_0_virtual@kq3kno9imanagedsub.com` |
| managerSubUserInfoVoList[].insertTimeStamp | integer (int64) |  | 例: `1678435149000` |
| managerSubUserInfoVoList[].bindParentEmail | string |  | 例: `wdyw8xsh8pey@test.com` |
| managerSubUserInfoVoList[].isSubUserEnabled | boolean |  | 例: `True` |
| managerSubUserInfoVoList[].isUserActive | boolean |  | 例: `True` |
| managerSubUserInfoVoList[].isMarginEnabled | boolean |  | 例: `False` |
| managerSubUserInfoVoList[].isFutureEnabled | boolean |  | 例: `False` |
| managerSubUserInfoVoList[].isSignedLVTRiskAgreement | boolean |  | 例: `False` |

## Query Managed Sub-account Margin Asset Details (For Investor Master Account) (USER_DATA)（投资人账户查询托管子账户杠杆资产 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/marginAsset`

Investor can use this api to query managed sub account margin asset details

投资人可以根据此接口查询其托管子账户杠杆资产

Operation ID: `queryManagedSubAccountMarginAssetDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| accountType | query | string |  | No input or input "MARGIN" to get Cross Margin account details. Input "ISOLATED_MARGIN" to get Isolated<br>Margin account details.<br>不输入或输入MARGIN，取得全仓帐户资产。 输入ISOLATED_MARGIN，取得逐仓帐户资产。<br>例: `MARGIN` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub-account Margin Asset Details / 查询托管子账户杠杆资产详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginLevel | string |  | 例: `999` |
| totalAssetOfBtc | string |  | 例: `0` |
| totalLiabilityOfBtc | string |  | 例: `0` |
| totalNetAssetOfBtc | string |  | 例: `0` |
| userAssets | object[] |  |  |
| userAssets[].asset | string |  | 例: `MATIC` |
| userAssets[].borrowed | string |  | 例: `0` |
| userAssets[].free | string |  | 例: `0` |
| userAssets[].interest | string |  | 例: `0` |
| userAssets[].locked | string |  | 例: `0` |
| userAssets[].netAsset | string |  | 例: `0` |

## Query Managed Sub-account Snapshot (For Investor Master Account) (USER_DATA)（查询托管子账户资产快照 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/accountSnapshot`

Query Managed Sub-account Snapshot

查询托管子账户资产快照

Operation ID: `queryManagedSubAccountSnapshot`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| type | query | string | 是 | 枚举: `SPOT`, `MARGIN`, `FUTURES`<br>例: `SPOT` |
| startTime | query | integer (int64) |  | Query time range must be within 30 days and only supports data within the last month.<br>查询时间范围不得超过 30 天，且仅支持最近 1 个月内的数据。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | If both startTime and endTime are omitted, records from the last 7 days are returned by default.<br>如果未同时传入 startTime 和 endTime，默认返回最近 7 天记录。<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `7`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub-account Snapshot / 托管子账户资产快照

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 200 for success; others are error codes<br>200表示返回正确，否则即为错误码<br>例: `200` |
| msg | string |  | error message<br>与错误码对应的报错信息<br>例: `` |
| snapshotVos | object[] |  |  |
| snapshotVos[].data | object |  |  |
| snapshotVos[].data.balances | object[] |  |  |
| snapshotVos[].data.balances[].asset | string |  | 例: `BTC` |
| snapshotVos[].data.balances[].free | string |  | 例: `0.09905021` |
| snapshotVos[].data.balances[].locked | string |  | 例: `0.00000000` |
| snapshotVos[].data.totalAssetOfBtc | string |  | 例: `0.09942700` |
| snapshotVos[].data.marginLevel | string |  | 例: `2748.02909813` |
| snapshotVos[].data.totalLiabilityOfBtc | string |  | 例: `0.00000100` |
| snapshotVos[].data.totalNetAssetOfBtc | string |  | 例: `0.00274750` |
| snapshotVos[].data.userAssets | object[] |  |  |
| snapshotVos[].data.userAssets[].asset | string |  | 例: `XRP` |
| snapshotVos[].data.userAssets[].borrowed | string |  | 例: `0.00000000` |
| snapshotVos[].data.userAssets[].free | string |  | 例: `1.00000000` |
| snapshotVos[].data.userAssets[].interest | string |  | 例: `0.00000000` |
| snapshotVos[].data.userAssets[].locked | string |  | 例: `0.00000000` |
| snapshotVos[].data.userAssets[].netAsset | string |  | 例: `1.00000000` |
| snapshotVos[].data.assets | object[] |  |  |
| snapshotVos[].data.assets[].asset | string |  | 例: `USDT` |
| snapshotVos[].data.assets[].marginBalance | string |  | 例: `118.99782335` |
| snapshotVos[].data.assets[].walletBalance | string |  | 例: `120.23811389` |
| snapshotVos[].data.position | object[] |  |  |
| snapshotVos[].data.position[].entryPrice | string |  | 例: `7130.41000000` |
| snapshotVos[].data.position[].markPrice | string |  | 例: `7257.66239673` |
| snapshotVos[].data.position[].positionAmt | string |  | 例: `0.01000000` |
| snapshotVos[].data.position[].symbol | string |  | 例: `BTCUSDT` |
| snapshotVos[].data.position[].unRealizedProfit | string |  | Only show the value at the time of opening the position<br>只显示开仓当时的未实现盈亏，不会实时更新，可以忽略<br>例: `1.24029054` |
| snapshotVos[].type | string |  | 例: `spot` |
| snapshotVos[].updateTime | integer (int64) |  | 例: `1576281599000` |

## Query Managed Sub Account Transfer Log For Investor Master Account (USER_DATA)（查询托管子账户的划转记录 (适用投资人母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`

Query Managed Sub Account Transfer Log For Investor Master Account

Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of
Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset
allocation and account application, while delegating trades to a professional trading team.

Please refer to
[link](https://www.binance.com/en/support/faq/how-to-get-started-with-managed-sub-account-functions-and-frequently-asked-questions-0594748722704383a7c369046e489459)

查询托管子账户的划转记录 (适用投资人母账户)

投资人可以根据此接口查询其托管子账户划转记录。此接口可供托管子账户的投资者使用。托管子账户是为重视资产配置与账户应用灵活性，并同时将交易委托专业交易团队的投资者的子账户类型。

请参阅[链接](https://www.binance.com/zh-CN/support/faq/%E6%89%98%E7%AE%A1%E5%AD%90%E8%B4%A6%E6%88%B7%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D-0594748722704383a7c369046e489459)

Operation ID: `queryManagedSubAccountTransferLogMasterAccountInvestor`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| startTime | query | integer (int64) | 是 | Start Time<br>开始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | End Time (The start time and end time interval cannot exceed half a year)<br>结束时间(开始时间结束时间间隔不能超过半年)<br>例: `1641782889000` |
| page | query | integer (int64) | 是 | Page<br>页数<br>例: `1` |
| limit | query | integer (int64) | 是 | 例: `1` |
| transfers | query | string |  | Transfer Direction (FROM/TO)<br>划转方向 (FROM/TO)<br>例: `None` |
| transferFunctionAccountType | query | string |  | 枚举: `SPOT`, `MARGIN`, `ISOLATED_MARGIN`, `USDT_FUTURE`, `COIN_FUTURE`<br>例: `SPOT` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub Account Transfer Log / 查询托管子账户划转记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| managerSubTransferHistoryVos | object[] |  |  |
| managerSubTransferHistoryVos[].fromEmail | string |  | 例: `test_0_virtual@kq3kno9imanagedsub.com` |
| managerSubTransferHistoryVos[].fromAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].toEmail | string |  | 例: `wdywl0lddakh@test.com` |
| managerSubTransferHistoryVos[].toAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].asset | string |  | 例: `BNB` |
| managerSubTransferHistoryVos[].amount | string |  | 例: `0.01` |
| managerSubTransferHistoryVos[].scheduledData | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].createTime | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].status | string |  | 例: `SUCCESS` |
| managerSubTransferHistoryVos[].tranId | integer (int64) |  | 例: `91077779` |
| count | integer (int64) |  | 例: `2` |

## Query Managed Sub Account Transfer Log For Trading Team Master Account (USER_DATA)（查询托管子账户的划转记录 (适用交易团队母账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`

Query Managed Sub Account Transfer Log For Trading Team Master Account

Trading team can use this api to query managed sub account transfer log. This endpoint is available for trading
team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in
asset allocation and account application, while delegating trades to a professional trading team.

Please refer to
[link](https://www.binance.com/en/support/faq/how-to-get-started-with-managed-sub-account-functions-and-frequently-asked-questions-0594748722704383a7c369046e489459)

查询托管子账户的划转记录 (适用交易团队母账户)

交易团队可以根据此接口查询其托管子账户划转记录。此接口可供托管子账户的交易团队使用。托管子账户是为重视资产配置与账户应用灵活性，并同时将交易委托专业交易团队的投资者的子账户类型。

请参阅[链接](https://www.binance.com/zh-CN/support/faq/%E6%89%98%E7%AE%A1%E5%AD%90%E8%B4%A6%E6%88%B7%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D-0594748722704383a7c369046e489459)

Operation ID: `queryManagedSubAccountTransferLogMasterAccountTrading`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| startTime | query | integer (int64) | 是 | Start Time<br>开始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | End Time (The start time and end time interval cannot exceed half a year)<br>结束时间(开始时间结束时间间隔不能超过半年)<br>例: `1641782889000` |
| page | query | integer (int64) | 是 | 例: `1` |
| limit | query | integer (int64) | 是 | 例: `10` |
| transfers | query | string |  | Transfer Direction (FROM/TO)<br>划转方向 (FROM/TO)<br>例: `None` |
| transferFunctionAccountType | query | string |  | 枚举: `SPOT`, `MARGIN`, `ISOLATED_MARGIN`, `USDT_FUTURE`, `COIN_FUTURE`<br>例: `SPOT` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub Account Transfer Log / 查询托管子账户划转记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| managerSubTransferHistoryVos | object[] |  |  |
| managerSubTransferHistoryVos[].fromEmail | string |  | 例: `test_0_virtual@kq3kno9imanagedsub.com` |
| managerSubTransferHistoryVos[].fromAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].toEmail | string |  | 例: `wdywl0lddakh@test.com` |
| managerSubTransferHistoryVos[].toAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].asset | string |  | 例: `BNB` |
| managerSubTransferHistoryVos[].amount | string |  | 例: `0.01` |
| managerSubTransferHistoryVos[].scheduledData | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].createTime | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].status | string |  | 例: `SUCCESS` |
| managerSubTransferHistoryVos[].tranId | integer (int64) |  | 例: `91077779` |
| count | integer (int64) |  | 例: `2` |

## Query Managed Sub Account Transfer Log (For Trading Team Sub Account) (USER_DATA)（查询托管子账户的划转记录 (适用交易团队子账户) (USER_DATA)）

`GET /sapi/v1/managed-subaccount/query-trans-log`

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

查询托管子账户的划转记录(适用交易团队子账户)

Operation ID: `queryManagedSubAccountTransferLogSubAccountTrading`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Start Time<br>开始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | End Time (The start time and end time interval cannot exceed half a year)<br>结束时间(开始时间结束时间间隔不能超过半年)<br>例: `1641782889000` |
| page | query | integer (int64) | 是 | 例: `1` |
| limit | query | integer (int64) | 是 | 例: `10` |
| transfers | query | string |  | Transfer Direction (from/to)<br>划转方向 (from/to)<br>例: `None` |
| transferFunctionAccountType | query | string |  | 枚举: `SPOT`, `MARGIN`, `ISOLATED_MARGIN`, `USDT_FUTURE`, `COIN_FUTURE`<br>例: `SPOT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Managed Sub Account Transfer Log / 查询托管子账户划转记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| managerSubTransferHistoryVos | object[] |  |  |
| managerSubTransferHistoryVos[].fromEmail | string |  | 例: `test_0_virtual@kq3kno9imanagedsub.com` |
| managerSubTransferHistoryVos[].fromAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].toEmail | string |  | 例: `wdywl0lddakh@test.com` |
| managerSubTransferHistoryVos[].toAccountType | string |  | 例: `SPOT` |
| managerSubTransferHistoryVos[].asset | string |  | 例: `BNB` |
| managerSubTransferHistoryVos[].amount | string |  | 例: `0.01` |
| managerSubTransferHistoryVos[].scheduledData | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].createTime | integer (int64) |  | 例: `1679416673000` |
| managerSubTransferHistoryVos[].status | string |  | 例: `SUCCESS` |
| managerSubTransferHistoryVos[].tranId | integer (int64) |  | 例: `91077779` |
| count | integer (int64) |  | 例: `2` |

## Withdrawl Assets From The Managed Sub-account (For Investor Master Account) (USER_DATA)（投资人账户为托管子账户提币资产 (适用投资人母账户) (USER_DATA)）

`POST /sapi/v1/managed-subaccount/withdraw`

Withdrawl Assets From The Managed Sub-account

投资人账户为托管子账户提币资产

Operation ID: `withdrawlAssetsFromTheManagedSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromEmail | string | 是 | 例: `from@test.com` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| transferDate | integer (int64) |  | Withdrawal will happen automatically on the selected date (UTC 0). If no date is selected,<br>withdrawal takes effect immediately.<br>提币会自动发生在选择的日期(UTC0)，如果没有选择日期，提币会立即生效<br>例: `None` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdrawl Assets From The Managed Sub-account / 从托管子账户提币资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | 例: `66157362489` |