---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api
api_type: REST
updated_at: 2026-11-18 18:48:22.437749
---

# Wallet REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/1.0.0/schema.yaml

Query balances, manage assets, and perform wallet operations via the Binance Wallet API.

通过 Binance Wallet API 查询余额、管理资产并执行钱包操作。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/account/apiTradingStatus` — Account API Trading Status (USER_DATA)
- `GET /sapi/v1/account/info` — Account info (USER_DATA)
- `GET /sapi/v1/account/status` — Account Status (USER_DATA)
- `GET /sapi/v1/accountSnapshot` — Daily Account Snapshot (USER_DATA)
- `POST /sapi/v1/account/disableFastWithdrawSwitch` — Disable Fast Withdraw Switch (USER_DATA)
- `POST /sapi/v1/account/enableFastWithdrawSwitch` — Enable Fast Withdraw Switch (USER_DATA)
- `GET /sapi/v1/account/apiRestrictions` — Get API Key Permission (USER_DATA)
- `GET /sapi/v1/asset/assetDetail` — Asset Detail (USER_DATA)
- `GET /sapi/v1/asset/assetDividend` — Asset Dividend Record (USER_DATA)
- `POST /sapi/v1/asset/dust-convert/convert` — Dust Convert (USER_DATA)
- `POST /sapi/v1/asset/dust-convert/query-convertible-assets` — Dust Convertible Assets (USER_DATA)
- `GET /sapi/v1/asset/dribblet` — DustLog (USER_DATA)
- `POST /sapi/v1/asset/dust` — Dust Transfer (USER_DATA)
- `POST /sapi/v1/asset/get-funding-asset` — Funding Wallet (USER_DATA)
- `GET /sapi/v1/spot/asset/tags` — Get Spot Asset Tags (MARKET_DATA)
- `POST /sapi/v1/asset/dust-btc` — Get Assets That Can Be Converted Into BNB (USER_DATA)
- `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage` — Get Cloud-Mining payment and refund history (USER_DATA)
- `GET /sapi/v1/spot/open-symbol-list` — Get Open Symbol List (MARKET_DATA)
- `GET /sapi/v1/asset/custody/transfer-history` — Query User Delegation History(For Master Account) (USER_DATA)
- `GET /sapi/v1/asset/transfer` — Query User Universal Transfer History (USER_DATA)
- `POST /sapi/v1/asset/transfer` — User Universal Transfer (USER_DATA)
- `GET /sapi/v1/asset/wallet/balance` — Query User Wallet Balance (USER_DATA)
- `POST /sapi/v1/bnbBurn` — Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
- `GET /sapi/v1/asset/tradeFee` — Trade Fee (USER_DATA)
- `POST /sapi/v3/asset/getUserAsset` — User Asset (USER_DATA)
- `GET /sapi/v1/capital/config/getall` — All Coins' Information (USER_DATA)
- `GET /sapi/v1/capital/deposit/address` — Deposit Address(supporting network) (USER_DATA)
- `GET /sapi/v1/capital/deposit/hisrec` — Deposit History (supporting network) (USER_DATA)
- `GET /sapi/v1/capital/deposit/address/list` — Fetch deposit address list with network (USER_DATA)
- `GET /sapi/v1/capital/withdraw/address/list` — Fetch withdraw address list (USER_DATA)
- `GET /sapi/v1/capital/withdraw/quota` — Fetch withdraw quota (USER_DATA)
- `POST /sapi/v1/capital/deposit/credit-apply` — One click arrival deposit apply (for expired address deposit) (USER_DATA)
- `POST /sapi/v1/capital/withdraw/apply` — Withdraw (USER_DATA)
- `GET /sapi/v1/capital/withdraw/history` — Withdraw History (supporting network) (USER_DATA)
- `GET /sapi/v1/spot/delist-schedule` — Get Spot Delist Schedule (MARKET_DATA)
- `GET /sapi/v1/system/status` — System Status
- `POST /sapi/v1/localentity/broker/withdraw/apply` — Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)
- `GET /sapi/v1/localentity/questionnaire-requirements` — Check Questionnaire Requirements (for local entities that require travel rule) (supporting network) (USER_DATA)
- `GET /sapi/v1/localentity/country/list` — Get Country List (USER_DATA)
- `GET /sapi/v1/localentity/deposit/history` — Deposit History Travel Rule (for local entities that required travel rule) (supporting network) (USER_DATA)
- `GET /sapi/v2/localentity/deposit/history` — Deposit History V2 (for local entities that required travel rule) (supporting network) (USER_DATA)
- `GET /sapi/v1/addressVerify/list` — Fetch address verification list (USER_DATA)
- `GET /sapi/v1/localentity/region/list` — Get Region List (USER_DATA)
- `PUT /sapi/v1/localentity/broker/deposit/provide-info` — Submit Deposit Questionnaire Broker (For local entities that require travel rule) (supporting network) (USER_DATA)
- `PUT /sapi/v1/localentity/deposit/provide-info` — Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
- `PUT /sapi/v2/localentity/deposit/provide-info` — Submit Deposit Questionnaire V2 (For local entities that require travel rule) (supporting network) (USER_DATA)
- `GET /sapi/v1/localentity/vasp` — VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
- `GET /sapi/v1/localentity/withdraw/history` — Withdraw History Travel Rule (supporting network) (USER_DATA)
- `GET /sapi/v2/localentity/withdraw/history` — Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)
- `POST /sapi/v1/localentity/withdraw/apply` — Withdraw Travel Rule (USER_DATA)

## Account API Trading Status (USER_DATA)（账户API交易状态 (USER_DATA)）

`GET /sapi/v1/account/apiTradingStatus`

Fetch account api trading status detail.

获取 api 账户交易状态详情。

Operation ID: `accountApiTradingStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account API Trading Status / 账户 API 交易状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| data | object |  |  |
| data.isLocked | boolean |  | API trading function is locked or not<br>API交易功能是否被锁<br>例: `False` |
| data.plannedRecoverTime | integer (int64) |  | If API trading function is locked, this is the planned recover time<br>API交易功能被锁情况下的预计恢复时间<br>例: `0` |
| data.triggerCondition | object |  |  |
| data.triggerCondition.GCR | integer (int64) |  | Number of GTC orders<br>例: `150` |
| data.triggerCondition.IFER | integer (int64) |  | Number of FOK/IOC orders<br>例: `150` |
| data.triggerCondition.UFR | integer (int64) |  | Number of orders<br>例: `300` |
| data.updateTime | integer (int64) |  | 例: `1547630471725` |

## Account info (USER_DATA)（帐户信息 (USER_DATA)）

`GET /sapi/v1/account/info`

Fetch account info detail.

获取帐户信息详情。

Operation ID: `accountInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account info / 账户信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| vipLevel | integer (int64) |  | 例: `0` |
| isMarginEnabled | boolean |  | true or false for margin.<br>是否开通杠杆账户，true 或 false。<br>例: `True` |
| isFutureEnabled | boolean |  | true or false for futures.<br>是否开通合约账户，true 或 false。<br>例: `True` |
| isOptionsEnabled | boolean |  | true or false for options.<br>是否开通期权账户，true 或 false。<br>例: `True` |
| isPortfolioMarginRetailEnabled | boolean |  | true or false for portfolio margin retail.<br>是否开通统一账户（零售版），true 或 false。<br>例: `True` |

## Account Status (USER_DATA)（账户状态 (USER_DATA)）

`GET /sapi/v1/account/status`

Fetch account status detail.

账户状态(USER_DATA)

Operation ID: `accountStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Status / 账户 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| data | string |  | 例: `Normal` |

## Daily Account Snapshot (USER_DATA)（查询每日资产快照 (USER_DATA)）

`GET /sapi/v1/accountSnapshot`

Daily account snapshot

查询每日资产快照

Operation ID: `dailyAccountSnapshot`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | string | 是 | 枚举: `SPOT`, `MARGIN`, `FUTURES`<br>例: `SPOT` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `7`<br>例: `7` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Daily Account Snapshot / 每日账户快照

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
| snapshotVos[].data.assets[].marginBalance | string |  | Not real-time data, can ignore<br>不会实时更新，可以忽略<br>例: `118.99782335` |
| snapshotVos[].data.assets[].walletBalance | string |  | 例: `120.23811389` |
| snapshotVos[].data.position | object[] |  |  |
| snapshotVos[].data.position[].entryPrice | string |  | 例: `7130.41000000` |
| snapshotVos[].data.position[].markPrice | string |  | 例: `7257.66239673` |
| snapshotVos[].data.position[].positionAmt | string |  | 例: `0.01000000` |
| snapshotVos[].data.position[].symbol | string |  | 例: `BTCUSDT` |
| snapshotVos[].data.position[].unRealizedProfit | string |  | Only show the value at the time of opening the position<br>只显示开仓当时的未实现盈亏，不会实时更新，可以忽略<br>例: `1.24029054` |
| snapshotVos[].type | string |  | 例: `spot` |
| snapshotVos[].updateTime | integer (int64) |  | 例: `1576281599000` |

## Disable Fast Withdraw Switch (USER_DATA)（关闭站内划转 (USER_DATA)）

`POST /sapi/v1/account/disableFastWithdrawSwitch`

Disable Fast Withdraw Switch

关闭站内划转

Operation ID: `disableFastWithdrawSwitch`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Enable Fast Withdraw Switch (USER_DATA)（开启站内划转 (USER_DATA)）

`POST /sapi/v1/account/enableFastWithdrawSwitch`

Enable Fast Withdraw Switch (USER_DATA)

开启站内划转(USER_DATA)

Operation ID: `enableFastWithdrawSwitch`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Get API Key Permission (USER_DATA)（查询用户API Key权限 (USER_DATA)）

`GET /sapi/v1/account/apiRestrictions`

Get API Key Permission

查询用户 API Key 权限

Operation ID: `getApiKeyPermission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get API Key Permission / 查询 API Key 权限

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| ipRestrict | boolean |  | 例: `False` |
| createTime | integer (int64) |  | 例: `1623840271000` |
| enableReading | boolean |  | 例: `True` |
| enableWithdrawals | boolean |  | This option allows you to withdraw via API. You must apply the IP Access Restriction filter in order to enable withdrawals<br>此选项允许通过此api提现。开启提现选项必须添加IP访问限制过滤器<br>例: `False` |
| enableInternalTransfer | boolean |  | This option authorizes this key to transfer funds between your master account and your sub account instantly<br>此选项授权此密钥在您的母账户和子账户之间划转资金<br>例: `True` |
| enableMargin | boolean |  | This option can be adjusted after the Cross Margin account transfer is completed<br>此选项在全仓账户完成划转后可编辑<br>例: `False` |
| enableFutures | boolean |  | The Futures API cannot be used if the API key was created before the Futures account was opened, or if you have enabled portfolio margin.<br>合约交易权限，需注意开通合约账户之前创建的API Key，或已开通统一账户的API Key，不支持合约API功能<br>例: `False` |
| permitsUniversalTransfer | boolean |  | Authorizes this key to be used for a dedicated universal transfer API to transfer multiple supported currencies. Each business's own transfer API rights are not affected by this authorization<br>授权该密钥可用于专用的万向划转接口，用以操作其支持的多种类型资金划转。各业务自身的划转接口使用权限，不受本授权影响<br>例: `True` |
| enableVanillaOptions | boolean |  | Authorizes this key to Vanilla options trading<br>欧式期权交易权限<br>例: `False` |
| enableFixApiTrade | boolean |  | 例: `False` |
| enableFixReadOnly | boolean |  | 例: `True` |
| enableSpotAndMarginTrading | boolean |  | Spot and margin trading<br>现货和杠杆交易权限<br>例: `False` |
| enablePortfolioMarginTrading | boolean |  | API Key created before your activate portfolio margin does not support portfolio margin API service<br>统一账户交易权限，需注意开通统一账户之前创建的API Key不支持统一账户API功能<br>例: `True` |

## Asset Detail (USER_DATA)（上架资产详情 (USER_DATA)）

`GET /sapi/v1/asset/assetDetail`

Fetch details of assets supported on Binance.

获取上架资产详情

Operation ID: `assetDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Asset Detail / 资产 Detail

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| CTR | object |  |  |
| CTR.minWithdrawAmount | string |  | min withdraw amount<br>最小提现数量<br>例: `70.00000000` |
| CTR.depositStatus | boolean |  | deposit status (false if ALL of networks' are false)<br>是否可以充值(只有所有网络都关闭充值才为false)<br>例: `False` |
| CTR.withdrawFee | integer (int64) |  | withdraw fee<br>提现手续费<br>例: `35` |
| CTR.withdrawStatus | boolean |  | withdraw status (false if ALL of networks' are false)<br>是否开放提现(只有所有网络都关闭提币才为false)<br>例: `True` |
| CTR.depositTip | string |  | reason<br>暂停充值的原因(如果暂停才有这一项)<br>例: `Delisted, Deposit Suspended` |
| SKY | object |  |  |
| SKY.minWithdrawAmount | string |  | min withdraw amount<br>最小提现数量<br>例: `0.02000000` |
| SKY.depositStatus | boolean |  | deposit status (false if ALL of networks' are false)<br>是否可以充值(只有所有网络都关闭充值才为false)<br>例: `True` |
| SKY.withdrawFee | number (float) |  | withdraw fee<br>提现手续费<br>例: `0.01` |
| SKY.withdrawStatus | boolean |  | withdraw status (false if ALL of networks' are false)<br>是否开放提现(只有所有网络都关闭提币才为false)<br>例: `True` |

## Asset Dividend Record (USER_DATA)（资产分发记录 (USER_DATA)）

`GET /sapi/v1/asset/assetDividend`

Query asset dividend record.

获取资产分发记录。

Operation ID: `assetDividendRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `20`<br>例: `20` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Asset Dividend Record / 资产分红记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].id | integer (int64) |  | 例: `1637366104` |
| rows[].amount | string |  | 例: `10.00000000` |
| rows[].asset | string |  | 例: `BHFT` |
| rows[].divTime | integer (int64) |  | 例: `1563189166000` |
| rows[].enInfo | string |  | 例: `BHFT distribution` |
| rows[].tranId | integer (int64) |  | 例: `2968885920` |
| rows[].direction | integer (int64) |  | direction: 1 for Asset credited (inflow), -1 for Asset debited (outflow)<br>direction：1 表示资产记账入账（资产流入），-1 表示资产记账出账（资产流出）<br>例: `1` |
| total | integer (int64) |  | 例: `2` |

## Dust Convert (USER_DATA)（小额资产兑换 (USER_DATA)）

`POST /sapi/v1/asset/dust-convert/convert`

Convert dust assets

小额兑换

Operation ID: `dustConvert`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| accountType | string |  | `SPOT` or `MARGIN`, default `SPOT`<br>`SPOT` 或 `MARGIN`，默认 `SPOT`<br>例: `SPOT` |
| clientId | string |  | A unique id for the request<br>用户自定义的请求号 ｜<br>例: `1` |
| targetAsset | string |  | 例: `BTC` |
| thirdPartyClientId | string |  | 例: `1` |
| dustQuotaAssetToTargetAssetPrice | number (float) |  | 例: `1.0` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Dust Convert / 小额资产兑换

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalTransfered | string |  | 例: `3.5971223` |
| totalServiceCharge | string |  | 例: `0.0794964` |
| transferResult | object[] |  |  |
| transferResult[].tranId | integer (int64) |  | 例: `2987331510` |
| transferResult[].fromAsset | string |  | 例: `USDT` |
| transferResult[].amount | string |  | 例: `1` |
| transferResult[].transferedAmount | string |  | 例: `3.5971223` |
| transferResult[].serviceChargeAmount | string |  | 例: `0.0794964` |
| transferResult[].operateTime | integer (int64) |  | 例: `1765212029749` |

## Dust Convertible Assets (USER_DATA)（小额可以兑换的资产 (USER_DATA)）

`POST /sapi/v1/asset/dust-convert/query-convertible-assets`

Query dust convertible assets

获取小额可以兑换的资产

Operation ID: `dustConvertibleAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string |  | `SPOT` or `MARGIN`, default `SPOT`<br>`SPOT` 或 `MARGIN`，默认 `SPOT`<br>例: `SPOT` |
| targetAsset | string | 是 | 例: `BTC` |
| dustQuotaAssetToTargetAssetPrice | number (float) |  | 例: `1.0` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Dust Convertible Assets / 可兑换小额资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dribbletPercentage | string |  | 例: `0.02` |
| totalTransferQuotaAssetAmount | string |  | 例: `0.7899968` |
| totalTransferTargetAssetAmount | string |  | 例: `0.7899968` |
| dribbletBase | string |  | 例: `10` |
| details | object[] |  |  |
| details[].asset | string |  | 例: `AR` |
| details[].assetFullName | string |  | 例: `AR` |
| details[].amountFree | string |  | 例: `0.00856` |
| details[].exchange | string |  | 例: `0.00073616` |
| details[].toQuotaAssetAmount | string |  | 例: `0.036808` |
| details[].toTargetAssetAmount | string |  | 例: `0.036808` |
| details[].toTargetAssetOffExchange | string |  | 例: `0.03607184` |

## DustLog (USER_DATA)（小额资产转换BNB历史 (USER_DATA)）

`GET /sapi/v1/asset/dribblet`

Dustlog

小额资产转换BNB历史(USER_DATA)

Operation ID: `dustlog`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| accountType | query | string |  | 枚举: `SPOT`, `MARGIN`<br>例: `SPOT` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：DustLog / 小额资产兑换记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total counts of exchange<br>共计发生过的转换笔数<br>例: `8` |
| userAssetDribblets | object[] |  |  |
| userAssetDribblets[].operateTime | integer (int64) |  | 例: `1615985535000` |
| userAssetDribblets[].totalTransferedAmount | string |  | Total transfered BNB amount for this exchange.<br>本次转换所得BNB<br>例: `0.00132256` |
| userAssetDribblets[].totalServiceChargeAmount | string |  | Total service charge amount for this exchange.<br>本次转换手续费(BNB)<br>例: `0.00002699` |
| userAssetDribblets[].transId | integer (int64) |  | 例: `45178372831` |
| userAssetDribblets[].userAssetDribbletDetails | object[] |  |  |
| userAssetDribblets[].userAssetDribbletDetails[].transId | integer (int64) |  | 例: `4359321` |
| userAssetDribblets[].userAssetDribbletDetails[].serviceChargeAmount | string |  | 例: `0.000009` |
| userAssetDribblets[].userAssetDribbletDetails[].amount | string |  | 例: `0.0009` |
| userAssetDribblets[].userAssetDribbletDetails[].operateTime | integer (int64) |  | 例: `1615985535000` |
| userAssetDribblets[].userAssetDribbletDetails[].transferedAmount | string |  | 例: `0.000441` |
| userAssetDribblets[].userAssetDribbletDetails[].fromAsset | string |  | 例: `USDT` |
| userAssetDribblets[].userAssetDribbletDetails[].targetAsset | string |  | 例: `BNB` |

## Dust Transfer (USER_DATA)（小额资产转换 (USER_DATA)）

`POST /sapi/v1/asset/dust`

Convert dust assets to BNB.

小额资产转换

Operation ID: `dustTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | The asset being converted. For example: asset=BTC,USDT<br>正在转换的资产。 例如：asset=BTC,USDT<br>例: `BTC` |
| accountType | string |  | 枚举: `SPOT`, `MARGIN`<br>默认: `SPOT`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Dust Transfer / Dust 划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalServiceCharge | string |  | 例: `0.02102542` |
| totalTransfered | string |  | 例: `1.05127099` |
| transferResult | object[] |  |  |
| transferResult[].amount | string |  | 例: `0.03000000` |
| transferResult[].fromAsset | string |  | 例: `ETH` |
| transferResult[].operateTime | integer (int64) |  | 例: `1563368549307` |
| transferResult[].serviceChargeAmount | string |  | 例: `0.00500000` |
| transferResult[].tranId | integer (int64) |  | 例: `2970932918` |
| transferResult[].transferedAmount | string |  | 例: `0.25000000` |

## Funding Wallet (USER_DATA)（查询资金账户 (USER_DATA)）

`POST /sapi/v1/asset/get-funding-asset`

Query Funding Wallet

查询资金账户(USER_DATA)

Operation ID: `fundingWallet`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | 例: `BTC` |
| needBtcValuation | boolean |  | 例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Funding Wallet / 资金钱包

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | 例: `USDT` |
| [].free | string |  | avalible balance<br>可用余额<br>例: `1` |
| [].locked | string |  | locked asset<br>锁定资金<br>例: `0` |
| [].freeze | string |  | freeze asset<br>冻结资金<br>例: `0` |
| [].withdrawing | string |  | 例: `0` |
| [].btcValuation | string |  | 例: `0.00000091` |

## Get Spot Asset Tags (MARKET_DATA)（查询现货资产标签 (MARKET_DATA)）

`GET /sapi/v1/spot/asset/tags`

Get the tags configured for spot-tradable assets.

查询现货可交易资产配置的标签。

Operation ID: `getSpotAssetTags`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| tag | query | string |  | Tag filter. Supports multiple comma-separated tags with OR semantics (an asset is returned if it matches any one tag); leading/trailing whitespace around each tag is ignored. Returns all eligible assets when omitted.<br>标签过滤条件。支持逗号分隔多个标签，任一标签命中即返回；会忽略标签前后空白。未传时返回全部符合条件的资产。<br>例: `Layer1_Layer2,BSC` |

### 响应 200：Get Spot Asset Tags / 查询现货资产标签

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].assetCode | string |  | Asset code.<br>资产代码。<br>例: `BNB` |
| [].assetName | string |  | Asset name.<br>资产名称。<br>例: `BNB` |
| [].trading | boolean |  | Asset trading status. This endpoint only returns `true`.<br>资产交易状态；此接口只会返回 `true`。<br>例: `True` |
| [].tags | string[] |  | Tags configured for the asset. Returns an empty array when the asset has no tags.<br>该资产配置的标签；没有标签时返回空数组。 |

## Get Assets That Can Be Converted Into BNB (USER_DATA)（获取可以转换成BNB的小额资产 (USER_DATA)）

`POST /sapi/v1/asset/dust-btc`

Get Assets That Can Be Converted Into BNB

获取可以转换成BNB的小额资产

Operation ID: `getAssetsThatCanBeConvertedIntoBnb`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string |  | 枚举: `SPOT`, `MARGIN`<br>默认: `SPOT`<br>例: `SPOT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Assets That Can Be Converted Into BNB / 获取Assets That Can Be Converted Into BNB

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| details | object[] |  |  |
| details[].asset | string |  | 例: `ADA` |
| details[].assetFullName | string |  | 例: `ADA` |
| details[].amountFree | string |  | Convertible amount<br>可转换数量<br>例: `6.21` |
| details[].toBTC | string |  | BTC amount<br>等值BTC<br>例: `0.00016848` |
| details[].toBNB | string |  | BNB amount（Not deducted commission fee）<br>可转换BNB（未扣除手续费）<br>例: `0.01777302` |
| details[].toBNBOffExchange | string |  | BNB amount（Deducted commission fee）<br>可转换BNB（已扣除手续费）<br>例: `0.01741756` |
| details[].exchange | string |  | Commission fee<br>手续费<br>例: `0.00035546` |
| totalTransferBtc | string |  | 例: `0.00016848` |
| totalTransferBNB | string |  | 例: `0.01777302` |
| dribbletPercentage | string |  | Commission fee<br>转换手续费<br>例: `0.02` |

## Get Cloud-Mining payment and refund history (USER_DATA)（云算力历史记录分页查询 (USER_DATA)）

`GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`

The query of Cloud-Mining payment and refund history

云算力支付和退款历史分页查询

Operation ID: `getCloudMiningPaymentAndRefundHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| tranId | query | integer (int64) |  | The transaction id<br>流水号<br>例: `1` |
| clientTranId | query | string |  | The unique flag<br>外部唯一流水号<br>例: `1` |
| asset | query | string |  | If it is blank, we will query all assets<br>不传或者空字符串查全部<br>例: `BTC` |
| startTime | query | integer (int64) | 是 | inclusive, unit: ms<br>开始时间（包含），单位：毫秒<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | exclusive, unit: ms<br>结束时间（不包含），单位：毫秒<br>例: `1641782889000` |
| current | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Cloud-Mining payment and refund history / 获取云算力支付和退款历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `5` |
| rows | object[] |  |  |
| rows[].createTime | integer (int64) |  | 例: `1667880112000` |
| rows[].tranId | integer (int64) |  | 例: `121230610120` |
| rows[].type | integer (int64) |  | 例: `248` |
| rows[].asset | string |  | 例: `USDT` |
| rows[].amount | string |  | 例: `25.0068` |
| rows[].status | string |  | 例: `S` |

## Get Open Symbol List (MARKET_DATA)（查询开放币对列表 (MARKET_DATA)）

`GET /sapi/v1/spot/open-symbol-list`

Get the list of symbols that are scheduled to be opened for trading in
the market.

查询即将开放交易的币对列表。

Operation ID: `getOpenSymbolList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Get Open Symbol List / 获取未完成交易对 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].openTime | integer (int64) |  | 例: `1686161202000` |
| [].symbols | string[] |  |  |

## Query User Delegation History(For Master Account) (USER_DATA)（查询用户委托资金历史(适用主账户) (USER_DATA)）

`GET /sapi/v1/asset/custody/transfer-history`

Query User Delegation History

查询用户委托资金历史

Operation ID: `queryUserDelegationHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| email | query | string | 是 | 例: `abc@test.com` |
| startTime | query | integer (int64) | 是 | 例: `1623319461670` |
| endTime | query | integer (int64) | 是 | 例: `1641782889000` |
| type | query | string |  | 枚举: `DELEGATE`, `UNDELEGATE`<br>例: `Delegate` |
| asset | query | string |  | 例: `BTC` |
| current | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Delegation History / 用户委托历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `3316` |
| rows | object[] |  |  |
| rows[].clientTranId | string |  | 例: `293915932290879488` |
| rows[].transferType | string |  | 例: `Undelegate` |
| rows[].asset | string |  | 例: `ETH` |
| rows[].amount | string |  | 例: `1` |
| rows[].time | integer (int64) |  | 例: `1695205406000` |

## Query User Universal Transfer History (USER_DATA)（查询用户万向划转历史 (USER_DATA)）

`GET /sapi/v1/asset/transfer`

Query User Universal Transfer History

查询用户万向划转历史

Operation ID: `queryUserUniversalTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | string | 是 | 例: `None` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| fromSymbol | query | string |  | 枚举: `ISOLATEDMARGIN_MARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`<br>例: `ISOLATEDMARGIN_MARGIN` |
| toSymbol | query | string |  | 枚举: `MARGIN_ISOLATEDMARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`<br>例: `MARGIN_ISOLATEDMARGIN` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Universal Transfer History / 用户万向划转历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `2` |
| rows | object[] |  |  |
| rows[].asset | string |  | 例: `USDT` |
| rows[].amount | string |  | 例: `1` |
| rows[].type | string |  | 例: `MAIN_UMFUTURE` |
| rows[].status | string |  | status: CONFIRMED / FAILED / PENDING<br>例: `CONFIRMED` |
| rows[].tranId | integer (int64) |  | 例: `11415955596` |
| rows[].timestamp | integer (int64) |  | 例: `1544433328000` |

## User Universal Transfer (USER_DATA)（用户万向划转 (USER_DATA)）

`POST /sapi/v1/asset/transfer`

User universal transfer

用户万向划转

Operation ID: `userUniversalTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | 枚举: `MAIN_UMFUTURE`, `MAIN_CMFUTURE`, `MAIN_MARGIN`, `UMFUTURE_MAIN`, `UMFUTURE_MARGIN`, `CMFUTURE_MAIN`, `CMFUTURE_MARGIN`, `MARGIN_MAIN`, `MARGIN_UMFUTURE`, `MARGIN_CMFUTURE`, `ISOLATEDMARGIN_MARGIN`, `MARGIN_ISOLATEDMARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`, `MAIN_FUNDING`, `FUNDING_MAIN`, `FUNDING_UMFUTURE`, `UMFUTURE_FUNDING`, `MARGIN_FUNDING`, `FUNDING_MARGIN`, `FUNDING_CMFUTURE`, `CMFUTURE_FUNDING`, `MAIN_OPTION`, `OPTION_MAIN`, `UMFUTURE_OPTION`, `OPTION_UMFUTURE`, `MARGIN_OPTION`, `OPTION_MARGIN`, `FUNDING_OPTION`, `OPTION_FUNDING`, `MAIN_PORTFOLIO_MARGIN`, `PORTFOLIO_MARGIN_MAIN`<br>例: `MAIN_UMFUTURE` |
| asset | string | 是 | 例: `BTC` |
| amount | number (float) | 是 | 例: `1.0` |
| fromSymbol | string |  | 枚举: `ISOLATEDMARGIN_MARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`<br>例: `ISOLATEDMARGIN_MARGIN` |
| toSymbol | string |  | 枚举: `MARGIN_ISOLATEDMARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`<br>例: `MARGIN_ISOLATEDMARGIN` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Universal Transfer / 用户万向划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | 例: `13526853623` |

## Query User Wallet Balance (USER_DATA)（查询用户钱包余额 (USER_DATA)）

`GET /sapi/v1/asset/wallet/balance`

Query User Wallet Balance

查询用户钱包余额

Operation ID: `queryUserWalletBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| quoteAsset | query | string |  | 默认: `BTC`<br>例: `BTC` |
| needBalanceDetail | query | boolean |  | Whether to return the per-asset balance detail for each wallet. When `false` or omitted, the response is<br>unchanged from current behavior.<br>是否返回每个钱包下各币种的持仓明细。为 `false` 或不传时，响应与现有行为完全一致。<br>默认: `False`<br>例: `False` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Wallet Balance / 用户 Wallet Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].activate | boolean |  | 例: `True` |
| [].balance | string |  | 例: `0` |
| [].walletName | string |  | 例: `Spot` |
| [].assetBalances | object[] |  | Per-asset balance detail for this wallet. Only present when `needBalanceDetail=true` is passed;<br>omitted entirely otherwise.<br>该钱包下各币种的持仓明细。仅当传入 `needBalanceDetail=true` 时才会返回，否则该字段完全不出现。 |
| [].assetBalances[].asset | string |  | 例: `USDT` |
| [].assetBalances[].assetName | string |  | 例: `TetherUS` |
| [].assetBalances[].free | string |  | 例: `6.238383` |
| [].assetBalances[].locked | string |  | 例: `0` |
| [].assetBalances[].freeze | string |  | 例: `0` |
| [].assetBalances[].withdrawing | string |  | 例: `0` |
| [].assetBalances[].btcValuation | string |  | 例: `6.238383` |

## Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)（现货交易和杠杆利息BNB抵扣开关 (USER_DATA)）

`POST /sapi/v1/bnbBurn`

Toggle BNB Burn On Spot Trade And Margin Interest

现货交易和杠杆利息BNB抵扣开关

Operation ID: `toggleBnbBurnOnSpotTradeAndMarginInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| spotBNBBurn | string |  | Determines whether to use BNB to pay for trading fees on SPOT<br>是否使用BNB支付现货交易的手续费<br>例: `True` |
| interestBNBBurn | string |  | Determines whether to use BNB to pay for margin loan's interest<br>是否使用BNB支付杠杆贷款的利息<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Toggle BNB Burn On Spot Trade And Margin Interest / 切换现货交易和杠杆利息 BNB 抵扣

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| spotBNBBurn | boolean |  | 例: `True` |
| interestBNBBurn | boolean |  | 例: `False` |

## Trade Fee (USER_DATA)（交易手续费率查询 (USER_DATA)）

`GET /sapi/v1/asset/tradeFee`

Fetch trade fee

交易手续费率查询

Operation ID: `tradeFee`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `ADABNB` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Trade Fee / 交易手续费率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `ADABNB` |
| [].makerCommission | string |  | 例: `0.001` |
| [].takerCommission | string |  | 例: `0.001` |

## User Asset (USER_DATA)（用户持仓 (USER_DATA)）

`POST /sapi/v3/asset/getUserAsset`

Get user assets, just for positive data.

获取用户持仓，仅返回>0的数据。

Operation ID: `userAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | If asset is blank, then query all positive assets user have.<br>如果资产为空，则查询用户所有的正资产。<br>例: `BTC` |
| needBtcValuation | boolean |  | Whether need btc valuation or not.<br>是否需要返回兑换成BTC的估值<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Asset / 用户资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | 例: `AVAX` |
| [].free | string |  | 例: `1` |
| [].locked | string |  | 例: `0` |
| [].freeze | string |  | 例: `0` |
| [].withdrawing | string |  | 例: `0` |
| [].ipoable | string |  | 例: `0` |
| [].btcValuation | string |  | 例: `0` |

## All Coins' Information (USER_DATA)（获取所有币信息 (USER_DATA)）

`GET /sapi/v1/capital/config/getall`

Get information of coins (available for deposit and withdraw) for user.

获取针对用户的所有(Binance支持充提操作的)币种信息。

Operation ID: `allCoinsInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Coins' Information / 全部币种信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].coin | string |  | 例: `1MBABYDOGE` |
| [].depositAllEnable | boolean |  | 例: `True` |
| [].withdrawAllEnable | boolean |  | 例: `True` |
| [].name | string |  | 例: `1M x BABYDOGE` |
| [].free | string |  | 例: `34941.1` |
| [].locked | string |  | 例: `0` |
| [].freeze | string |  | 例: `0` |
| [].withdrawing | string |  | 例: `0` |
| [].ipoing | string |  | 例: `0` |
| [].ipoable | string |  | 例: `0` |
| [].storage | string |  | 例: `0` |
| [].isLegalMoney | boolean |  | 例: `False` |
| [].trading | boolean |  | 例: `True` |
| [].networkList | object[] |  |  |
| [].networkList[].network | string |  | 例: `BSC` |
| [].networkList[].coin | string |  | 例: `1MBABYDOGE` |
| [].networkList[].withdrawIntegerMultiple | string |  | 例: `0.01` |
| [].networkList[].isDefault | boolean |  | 例: `False` |
| [].networkList[].depositEnable | boolean |  | 例: `True` |
| [].networkList[].withdrawEnable | boolean |  | 例: `True` |
| [].networkList[].depositDesc | string |  | shown only when "depositEnable" is false.<br>仅在充值关闭时返回<br>例: `` |
| [].networkList[].withdrawDesc | string |  | shown only when "withdrawEnable" is false.<br>仅在提现关闭时返回<br>例: `` |
| [].networkList[].specialTips | string |  | 例: `` |
| [].networkList[].specialWithdrawTips | string |  | 例: `` |
| [].networkList[].name | string |  | 例: `BNB Smart Chain (BEP20)` |
| [].networkList[].resetAddressStatus | boolean |  | 例: `False` |
| [].networkList[].addressRegex | string |  | 例: `^(0x)[0-9A-Fa-f]{40}$` |
| [].networkList[].memoRegex | string |  | 例: `` |
| [].networkList[].withdrawFee | string |  | 例: `10` |
| [].networkList[].withdrawMin | string |  | 例: `20` |
| [].networkList[].withdrawMax | string |  | 例: `9999999999` |
| [].networkList[].withdrawInternalMin | string |  | Minimum internal transfer amount<br>内部转账最小提现数<br>例: `0.01` |
| [].networkList[].depositDust | string |  | 例: `0.01` |
| [].networkList[].minConfirm | integer (int64) |  | min number for balance confirmation<br>上账所需的最小确认数<br>例: `5` |
| [].networkList[].unLockConfirm | integer (int64) |  | confirmation number for balance unlock<br>解锁需要的确认数<br>例: `0` |
| [].networkList[].sameAddress | boolean |  | Obsoleted, recomment to use withdrawTag<br>过时字段，建议使用withdrawTag<br>例: `False` |
| [].networkList[].withdrawTag | boolean |  | If the coin needs to provide memo to withdraw<br>提现时是否需要memo<br>例: `False` |
| [].networkList[].estimatedArrivalTime | integer (int64) |  | 例: `1` |
| [].networkList[].busy | boolean |  | 例: `False` |
| [].networkList[].contractAddressUrl | string |  | 例: `https://bscscan.com/token/` |
| [].networkList[].contractAddress | string |  | 例: `0xc748673057861a797275cd8a068abb95a902e8de` |
| [].networkList[].denomination | integer (int64) |  | 1 1MBABYDOGE = 1000000 BABYDOGE<br>例: `1000000` |

## Deposit Address(supporting network) (USER_DATA)（获取充值地址(支持多网络) (USER_DATA)）

`GET /sapi/v1/capital/deposit/address`

Fetch deposit address with network.

获取充值地址

Operation ID: `depositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| coin | query | string | 是 | `coin` refers to the parent network address format that the address is using<br>币种，指该地址所使用的主网络地址格式<br>例: `BTC` |
| network | query | string |  | 例: `None` |
| amount | query | number (float) |  | 例: `1.0` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Deposit Address / 充值地址

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| address | string |  | 例: `1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv` |
| coin | string |  | 例: `BTC` |
| tag | string |  | 例: `` |
| url | string |  | 例: `https://btc.com/1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv` |

## Deposit History (supporting network) (USER_DATA)（获取充值历史 (USER_DATA)）

`GET /sapi/v1/capital/deposit/hisrec`

Fetch deposit history.

获取充值历史(支持多网络)

Operation ID: `depositHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| includeSource | query | boolean |  | return `sourceAddress` field when set to `true`<br>如果为`true`时会返回`sourceAddress`字段<br>默认: `False`<br>例: `False` |
| coin | query | string |  | 例: `BTC` |
| status | query | integer (int64) |  | 0: pending, 1: success, 2: rejected, 6: credited but cannot withdraw, 7: Wrong Deposit, 8: Waiting User confirm<br>0: 待确认, 1: 成功, 2: 已拒绝, 6: 已到账但不可提现, 7: 充值异常, 8: 等待用户确认<br>枚举: `0`, `1`, `2`, `6`, `7`, `8`<br>例: `0` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| txId | query | string |  | 例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Deposit History / 充值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | 例: `769800519366885376` |
| [].amount | string |  | 例: `0.001` |
| [].coin | string |  | 例: `BNB` |
| [].network | string |  | 例: `BNB` |
| [].status | integer (int64) |  | 例: `1` |
| [].address | string |  | 例: `bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23` |
| [].addressTag | string |  | 例: `101764890` |
| [].txId | string |  | 例: `98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC` |
| [].insertTime | integer (int64) |  | 例: `1661493146000` |
| [].completeTime | integer (int64) |  | represents deposit completion datetime, available for deposits after 6-Mar-2025.<br>代表充值完成时间，仅适用于2025年03月06日之后的充值。<br>例: `1661493146000` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].confirmTimes | string |  | 例: `1/1` |
| [].unlockConfirm | integer (int64) |  | 例: `0` |
| [].walletType | integer (int64) |  | 例: `0` |
| [].travelRuleStatus | integer (int64) |  | 0: travel rule not required OR info already provided and funds ready to use, 1: travel rule required to provide deposit info<br>例: `0` |

## Fetch deposit address list with network (USER_DATA)（查询充值地址列表 (USER_DATA)）

`GET /sapi/v1/capital/deposit/address/list`

Fetch deposit address list with network.

根据网络币种或币种获取充值地址列表

Operation ID: `fetchDepositAddressListWithNetwork`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| coin | query | string | 是 | Coin name<br>币种名称<br>例: `BTC` |
| network | query | string |  | If network is not send, return with default network of the coin. You can get network and isDefault in networkList in the response of `Get /sapi/v1/capital/config/getall`<br>如果没传网络，会返回网络对应的默认网络。可以通过后面的接口，来获取网络和 isDefault 字段，在返回的响应里`Get /sapi/v1/capital/config/getall`<br>例: `None` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch deposit address list with network / 查询充值地址列表（按网络）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].coin | string |  | coin here means network address space, ETH for all EVM-like network<br>这里 coin 实际上指 network 的地址空间, 类 ETH 网络都使用 ETH 的地址<br>例: `ETH` |
| [].address | string |  | 例: `0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4` |
| [].tag | string |  | 例: `` |
| [].isDefault | integer (int64) |  | 'isDefault' is 1 means the address is default, same as shown in the app.<br>isDefault 为 1 表示该地址为默认地址，与 App 中显示的一致。<br>例: `0` |

## Fetch withdraw address list (USER_DATA)（查询提现地址簿 (USER_DATA)）

`GET /sapi/v1/capital/withdraw/address/list`

Fetch withdraw address list

查询提现地址簿

Operation ID: `fetchWithdrawAddressList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch withdraw address list / 查询提现地址簿

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].address | string |  | 例: `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` |
| [].addressTag | string |  | 例: `` |
| [].coin | string |  | 例: `BTC` |
| [].name | string |  | is a user-defined name<br>用户自定义<br>例: `Satoshi` |
| [].network | string |  | 例: `BTC` |
| [].origin | string |  | if originType != 'others', this value is blank, otherwise the origin is manually filled in by the user<br>如果 originType != 'others'，则该值为空，否则 origin 由用户手动填写<br>例: `bla` |
| [].originType | string |  | Address source type, including but not limited to: type Exchange Address: Binance, CoinBase, HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini, Bitget, Bybit, Upbit, Gate.io;  type Wallet Address: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby Wallet, Phantom, OKX Web 3 Wallet, Coinbase Wallet, Bitget Wallet; type Others: others(multilanguage support)<br>地址来源类型，包括但不限于: 交易所地址类型: Binance, CoinBase, HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini, Bitget, Bybit, Upbit, Gate.io; 个人钱包类型: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby Wallet, Phantom, OKX Web 3 Wallet, Coinbase Wallet, Bitget Wallet; 其他 Others 类型: others(支持多语言)<br>例: `others` |
| [].whiteStatus | boolean |  | Is it whitelisted<br>是否是白名单<br>例: `True` |

## Fetch withdraw quota (USER_DATA)（获取用户提现额度 (USER_DATA)）

`GET /sapi/v1/capital/withdraw/quota`

Fetch withdraw quota

获取用户提现额度

Operation ID: `fetchWithdrawQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch withdraw quota / 获取提现额度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| wdQuota | string |  | User's total withdrawal quota in the past 24 hours (including on-chain withdrawal and internal transfer), unit in USD<br>用户过去24小时的提币额度（包含链上提币和内部转账），单位为 USD<br>例: `10000` |
| usedWdQuota | string |  | User withdrawal quota usage in the past 24 hours, unit in USD<br>用户过去24小时内已用提币额度，单位为 USD<br>例: `1000` |

## One click arrival deposit apply (for expired address deposit) (USER_DATA)（一键上账(充值到过期地址) (USER_DATA)）

`POST /sapi/v1/capital/deposit/credit-apply`

Apply deposit credit for expired address (One click arrival)

申请充值到过期地址的一键上账.

Operation ID: `oneClickArrivalDepositApply`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| depositId | integer (int64) |  | Deposit record Id, priority use<br>充值记录Id，优先使用<br>例: `1` |
| txId | string |  | Deposit txId, used when depositId is not specified<br>充值txId，当depositId没指定时使用<br>例: `1` |
| subAccountId | string |  | Sub-accountId of Cloud user<br>Cloud的子账户ID<br>例: `1` |
| subUserId | integer (int64) |  | Sub-userId of parent user<br>母账户的子账户userId<br>例: `1` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：One click arrival deposit apply / 一键充值到账申请

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | boolean |  | 例: `True` |
| success | boolean |  | 例: `True` |

## Withdraw (USER_DATA)（提币 (USER_DATA)）

`POST /sapi/v1/capital/withdraw/apply`

Submit a withdraw request

提币

Operation ID: `withdraw`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 例: `BTC` |
| withdrawOrderId | string |  | client side id for withdrawal, if provide here, can be used in GET<br>`/sapi/v1/capital/withdraw/history` for query.<br>用户自定义提币ID, 后续可以在GET `/sapi/v1/capital/withdraw/history` 中使用这个字段进行查询<br>例: `1` |
| network | string |  | Withdrawal network<br>提币网络<br>例: `None` |
| address | string | 是 | Withdrawal address<br>提币地址<br>例: `None` |
| addressTag | string |  | Secondary address identifier for coins like XRP,XMR etc.<br>某些币种例如 XRP,XMR 允许填写次级地址标签<br>例: `None` |
| amount | number (float) | 是 | Amount<br>数量<br>例: `1.0` |
| transactionFeeFlag | boolean |  | When making internal transfer, `true` for returning the fee to the destination account; `false` for<br>returning the fee back to the departure account. Default `false`.<br>当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`.<br>例: `True` |
| name | string |  | 例: `None` |
| walletType | integer (int64) |  | The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current<br>"selected wallet" under wallet->Fiat and Spot/Funding->Deposit<br>表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。<br>例: `0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdraw / 提币

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `7213fea8e94b4a5593d507237e5a555b` |

## Withdraw History (supporting network) (USER_DATA)（获取提币历史(支持多网络) (USER_DATA)）

`GET /sapi/v1/capital/withdraw/history`

Fetch withdraw history

获取提币历史 (支持多网络)

Operation ID: `withdrawHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| coin | query | string |  | 例: `BTC` |
| withdrawOrderId | query | string |  | client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for<br>query.<br>用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单<br>例: `1` |
| status | query | integer (int64) |  | 0(0: Email Sent, 2: Awaiting Approval 3: Rejected 4: Processing 6: Completed)<br>0(0:已发送确认Email, 2:等待确认 3:被拒绝 4:处理中 6 提现完成)<br>例: `0` |
| offset | query | integer (int64) |  | Default: 0<br>默认值：0<br>例: `0` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| idList | query | string |  | id list returned in the response of POST `/sapi/v1/capital/withdraw/apply`, separated by `,`<br>POST `/sapi/v1/capital/withdraw/apply` 返回的 id 列表，以 `,` 分隔<br>例: `None` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdraw History / 提币历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | Withdrawal id in Binance<br>该笔提现在币安的id<br>例: `b6ae22b3aa844210a7041aee7589627c` |
| [].amount | string |  | withdrawal amount<br>提现转出金额<br>例: `8.91000000` |
| [].transactionFee | string |  | transaction fee<br>手续费<br>例: `0.004` |
| [].coin | string |  | 例: `USDT` |
| [].status | integer (int64) |  | 例: `6` |
| [].address | string |  | 例: `0x94df8b352de7f46f64b01d3666bf6e936e44ce60` |
| [].txId | string |  | withdrawal transaction id<br>提现交易id<br>例: `0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268` |
| [].applyTime | string |  | UTC time<br>UTC 时间<br>例: `2019-10-12 11:12:02` |
| [].network | string |  | 例: `ETH` |
| [].transferType | integer (int64) |  | 1 for internal transfer, 0 for external transfer<br>1: 站内转账, 0: 站外转账<br>例: `0` |
| [].withdrawOrderId | string |  | will not be returned if there's no withdrawOrderId for this withdraw.<br>自定义ID, 如果没有则不返回该字段<br>例: `WITHDRAWtest123` |
| [].info | string |  | reason for withdrawal failure<br>提币失败原因<br>例: `The address is not valid. Please confirm with the recipient` |
| [].confirmNo | integer (int64) |  | confirm times for withdraw<br>提现确认数<br>例: `3` |
| [].walletType | integer (int64) |  | 1: Funding Wallet 0:Spot Wallet<br>1: 资金钱包 0:现货钱包<br>例: `1` |
| [].txKey | string |  | 例: `` |
| [].completeTime | string |  | complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)<br>提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回<br>例: `2023-03-23 16:52:41` |

## Get Spot Delist Schedule (MARKET_DATA)（查询现货币对的下架计划 (MARKET_DATA)）

`GET /sapi/v1/spot/delist-schedule`

Get symbols delist schedule for spot

查询现货币对的下架计划

Operation ID: `getSymbolsDelistScheduleForSpot`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |

### 响应 200：Get symbols delist schedule for spot / 查询现货下架计划

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].delistTime | integer (int64) |  | 例: `1686161202000` |
| [].symbols | string[] |  |  |

## System Status（系统状态）

`GET /sapi/v1/system/status`

Fetch system status.

获取系统状态。

Operation ID: `systemStatus`

### 响应 200：System Status / 系统状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | integer (int64) |  | 0: normal，1：system maintenance<br>例: `0` |
| msg | string |  | "normal", "system_maintenance"<br>例: `normal` |

## Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)（Broker 提币（适用于需要旅行规则的本地实体券商） (USER_DATA)）

`POST /sapi/v1/localentity/broker/withdraw/apply`

Submit a withdrawal request for brokers of local entities that required travel rule.

为需要旅行规则的本地实体券商提交提币请求。

Operation ID: `brokerWithdraw`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| address | string | 是 | 例: `None` |
| addressTag | string |  | Secondary address identifier for coins like XRP,XMR etc.<br>某些币种例如 XRP,XMR 允许填写次级地址标签<br>例: `None` |
| network | string |  | 例: `None` |
| coin | string | 是 | 例: `BTC` |
| addressName | string |  | Description of the address. Address book cap is 200, space in name should be encoded into `%20`<br>地址描述。地址簿上限为200，名称中的空格应编码为`%20`<br>例: `None` |
| amount | number (float) | 是 | 例: `1.0` |
| withdrawOrderId | string | 是 | withdrawID defined by the client (i.e. client's internal withdrawID)<br>客户端内部定义的提币ID.<br>例: `1` |
| transactionFeeFlag | boolean |  | When making internal transfer, `true` for returning the fee to the destination account; `false` for<br>returning the fee back to the departure account. Default `false`.<br>当站内转账时免手续费,`true`: 手续费归资金转入方;`false`: 手续费归资金转出方; . 默认`false`.<br>例: `True` |
| walletType | integer (int64) |  | The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current<br>"selected wallet" under wallet->Fiat and Spot/Funding->Deposit<br>表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。<br>例: `0` |
| questionnaire | string | 是 | JSON format questionnaire answers.<br>JSON 格式的问卷回答。<br>例: `None` |
| originatorPii | string | 是 | JSON format originator Pii, see StandardPii section below<br>JSON 格式的汇款人个人身份信息, 请参阅下面的标准个人身份信息部分。<br>例: `None` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Broker Withdraw / Broker 提币

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trId | integer (int64) |  | The travel rule record Id<br>Travel Rule记录ID<br>例: `123456` |
| accepted | boolean |  | Whether the withdraw request is accepted<br>提币请求是否被接受<br>例: `True` |
| info | string |  | The detailed infomation of the withdrawal result.<br>提现结果的详细信息<br>例: `Withdraw request accepted` |

## Check Questionnaire Requirements (for local entities that require travel rule) (supporting network) (USER_DATA)（检查问卷需求(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`GET /sapi/v1/localentity/questionnaire-requirements`

This API will return user-specific Travel Rule questionnaire requirement information in reference to the current
API key.

基于当前的用户的API key，接口讲返回针对改用户提交问卷所需的信息。

Operation ID: `checkQuestionnaireRequirements`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Check Questionnaire Requirements / 检查询卷要求

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| questionnaireCountryCode | string |  | 例: `AE` |

## Get Country List (USER_DATA)（国家列表 (USER_DATA)）

`GET /sapi/v1/localentity/country/list`

Query the active country list for travel rule questionnaires. Currently supports AU and BR entities.

查询旅行规则问卷使用的活跃国家列表。目前支持澳大利亚站和巴西站。

Operation ID: `getCountryList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Country list / 国家列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| countries | object[] |  |  |
| countries[].countryCode | string |  | ISO 2-digit country code, lowercase.<br>ISO 2位国家代码，小写。<br>例: `au` |
| countries[].countryName | string |  | Country display name.<br>国家显示名称。<br>例: `Australia` |
| countries[].blockType | string |  | `supported`, `limited`, or `blocked`.<br>`supported`、`limited` 或 `blocked`。<br>例: `supported` |
| countries[].depositAllowed | boolean |  | Whether deposit is allowed for this country.<br>该国家是否允许充值。<br>例: `True` |
| countries[].withdrawalAllowed | boolean |  | Whether withdrawal is allowed for this country.<br>该国家是否允许提现。<br>例: `True` |
| countries[].hasRegionRestrictions | boolean |  | Whether this country has region-level restrictions. Always `false` for the BR entity, which does not collect region/city.<br>该国家是否存在地区级别的限制。巴西站不采集地区/城市，恒为 `false`。<br>例: `False` |
| lastUpdated | integer (int64) |  | Last data update timestamp (epoch milliseconds); 0 if empty.<br>数据最后更新时间戳（毫秒级 epoch）；为空时返回 0。<br>例: `1716300000000` |

## Deposit History Travel Rule (for local entities that required travel rule) (supporting network) (USER_DATA)（获取充值历史(针对需要旅行规则的本地站) (USER_DATA)）

`GET /sapi/v1/localentity/deposit/history`

Fetch deposit history for local entities that required travel rule.

获取充值历史(针对需要旅行规则的本地站)(支持多网络)

Operation ID: `depositHistoryTravelRule`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| trId | query | string |  | Comma(,) separated list of travel rule record Ids.<br>旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| txId | query | string |  | Comma(,) separated list of transaction Ids.<br>链上TxId，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| tranId | query | string |  | Comma(,) separated list of wallet tran Ids.<br>充值记录ID，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| network | query | string |  | 例: `None` |
| coin | query | string |  | 例: `BTC` |
| travelRuleStatus | query | integer (int64) |  | 0: Completed,1: Pending,2: Failed<br>0:处理完成,1:处理中,2:请求被拒绝<br>例: `0` |
| pendingQuestionnaire | query | boolean |  | true: Only return records that pending deposit questionnaire. false/not provided: return all records.<br>true: 只返回需要回答充值问卷的记录，false/缺省:返回所有记录<br>例: `True` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| offset | query | integer (int64) |  | Default: 0<br>默认:0<br>例: `None` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Deposit History / 充值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].trId | integer (int64) |  | 例: `123451123` |
| [].tranId | integer (int64) |  | 例: `17644346245865` |
| [].amount | string |  | 例: `0.001` |
| [].coin | string |  | 例: `BNB` |
| [].network | string |  | 例: `BNB` |
| [].depositStatus | integer (int64) |  | 例: `0` |
| [].travelRuleStatus | integer (int64) |  | 例: `1` |
| [].travelRuleStatusV2 | string |  | Overall travel rule verification status (GTR + sanctions screening combined). "PASSED": verification complete, deposit released. "PENDING": verification in progress, deposit frozen. "REJECTED": verification failed.<br>旅行规则整体验证状态（GTR + 制裁筛查）。 "PASSED": 验证完成，充值已释放。 "PENDING": 验证进行中，充值已冻结。 "REJECTED": 验证失败。<br>例: `PENDING` |
| [].address | string |  | 例: `bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23` |
| [].addressTag | string |  | 例: `101764890` |
| [].txId | string |  | 例: `98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC` |
| [].insertTime | integer (int64) |  | 例: `1661493146000` |
| [].completeTime | integer (int64) |  | Timestamp when the deposit was fully completed/credited (epoch ms).<br>充值完成时间戳（毫秒）。<br>例: `1661493206000` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].confirmTimes | string |  | 例: `1/1` |
| [].requireQuestionnaire | boolean |  | true: This deposit require user to answer questionnaire to get it credited, false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified<br>true: 该充值需要用户回答问卷才能入账, false: 该充值不需要用户回答问卷，已完成或信息已验证<br>例: `False` |
| [].questionnaire | string |  | 例: `{"question1":"answer1","question2":"answer2"}` |

## Deposit History V2 (for local entities that required travel rule) (supporting network) (USER_DATA)（获取充值历史V2(针对需要旅行规则的本地站) (USER_DATA)）

`GET /sapi/v2/localentity/deposit/history`

Fetch deposit history for local entities that with required travel rule information.

获取充值历史(针对需要旅行规则的本地站)(支持多网络)

Operation ID: `depositHistoryV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| depositId | query | integer (int64) |  | Comma(,) separated list of wallet tran Ids.<br>入金记录ID，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| txId | query | string |  | Comma(,) separated list of transaction Ids.<br>链上TxId，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| network | query | string |  | 例: `None` |
| coin | query | string |  | 例: `BTC` |
| retrieveQuestionnaire | query | boolean |  | true: return `questionnaire` within response.<br>true:返回的记录中带有问卷内容，false/缺省.<br>例: `True` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Deposit History V2 / 充值历史 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].depositId | string |  | 例: `4615328107052018945` |
| [].amount | string |  | 例: `0.01` |
| [].network | string |  | 例: `AVAXC` |
| [].coin | string |  | 例: `AVAX` |
| [].depositStatus | integer (int64) |  | 例: `1` |
| [].travelRuleReqStatus | integer (int64) |  | 0:PASS,2:REJECTED,3:PENDING,-1:FAILED<br>例: `0` |
| [].address | string |  | 例: `0x0010627ab66d69232f4080d54e0f838b4dc3894a` |
| [].addressTag | string |  | 例: `` |
| [].txId | string |  | 例: `0xdde578983015741eed764e7ca10defb5a2caafdca3db5f92872d24a96beb1879` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].confirmTimes | string |  | 例: `12/12` |
| [].requireQuestionnaire | boolean |  | true: This deposit require user to answer questionnaire to get it credited, false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified<br>例: `False` |
| [].questionnaire | object |  |  |
| [].questionnaire.vaspName | string |  | 例: `BINANCE` |
| [].questionnaire.depositOriginator | integer (int64) |  | 例: `0` |
| [].insertTime | integer (int64) |  | 例: `1753053392000` |

## Fetch address verification list (USER_DATA)（获取address verification 列表 (USER_DATA)）

`GET /sapi/v1/addressVerify/list`

Fetch address verification list for user to check on status and other details for the addresses stored in
Address Book.

获取地址验证列表，以便用户检查地址簿中存储的地址的状态和其他详细信息。

Operation ID: `fetchAddressVerificationList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch address verification list / 获取地址验证列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].status | string |  | 例: `PENDING` |
| [].token | string |  | 例: `AVAX` |
| [].network | string |  | 例: `AVAXC` |
| [].walletAddress | string |  | 例: `0xc03a6aa728a8dde7464c33828424ede7553a0021` |
| [].addressQuestionnaire | object |  |  |
| [].addressQuestionnaire.sendTo | integer (int64) |  | 例: `1` |
| [].addressQuestionnaire.satoshiToken | string |  | 例: `AVAX` |
| [].addressQuestionnaire.isAddressOwner | integer (int64) |  | 例: `1` |
| [].addressQuestionnaire.verifyMethod | integer (int64) |  | 例: `1` |

## Get Region List (USER_DATA)（地区列表 (USER_DATA)）

`GET /sapi/v1/localentity/region/list`

Query the active region/city list for a given country. Currently, only supports AU entity.

查询指定国家下的活跃地区/城市列表。目前仅支持澳大利亚站。

Operation ID: `getRegionList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| countryCode | query | string | 是 | ISO 2-digit country code (from Country List API).<br>ISO 2位国家代码（来自国家列表接口）。<br>例: `au` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Region list / 地区列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| countryCode | string |  | Echoed country code (lowercase).<br>回显查询的国家代码（小写）。<br>例: `au` |
| regions | object[] |  |  |
| regions[].regionName | string |  | Region/city display name (use this value in questionnaire answers).<br>地区/城市显示名称（问卷答案中使用此值）。<br>例: `New South Wales` |
| regions[].blockType | string |  | `supported`, `limited`, or `blocked`.<br>`supported`、`limited` 或 `blocked`。<br>例: `supported` |
| regions[].depositAllowed | boolean |  | Whether deposit is allowed for this region.<br>该地区是否允许充值。<br>例: `True` |
| regions[].withdrawalAllowed | boolean |  | Whether withdrawal is allowed for this region.<br>该地区是否允许提现。<br>例: `True` |
| lastUpdated | integer (int64) |  | Last data update timestamp (epoch milliseconds); 0 if empty.<br>数据最后更新时间戳（毫秒级 epoch）；为空时返回 0。<br>例: `1716300000000` |

## Submit Deposit Questionnaire Broker (For local entities that require travel rule) (supporting network) (USER_DATA)（提交充值问卷（Broker，适用于需要旅行规则的本地实体，支持网络） (USER_DATA)）

`PUT /sapi/v1/localentity/broker/deposit/provide-info`

Submit questionnaire for brokers of local entities that require travel rule.
The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not
yet onboarded with GTR.

为需要旅行规则的本地实体券商提交问卷。
该问卷仅适用于来自非托管钱包或尚未接入 GTR 的 VASP 的交易。

Operation ID: `submitDepositQuestionnaire`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | External user ID.<br>外部UID<br>例: `1` |
| depositId | integer (int64) | 是 | Wallet deposit ID.<br>充值记录ID.<br>例: `1` |
| questionnaire | string | 是 | JSON format questionnaire answers.<br>JSON 格式的问卷回答。<br>例: `None` |
| beneficiaryPii | string | 是 | JSON format beneficiary Pii, see StandardPii section below<br>JSON 格式的收款人个人身份信息, 请参阅下面的标准个人身份信息部分。<br>例: `None` |
| network | string |  | 例: `None` |
| coin | string |  | 例: `BTC` |
| amount | number (float) |  | 例: `1.0` |
| address | string |  | 例: `None` |
| addressTag | string |  | 例: `None` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Submit Deposit Questionnaire / 提交充值问卷

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trId | integer (int64) |  | 例: `765127651` |
| accepted | boolean |  | 例: `True` |
| info | string |  | 例: `Deposit questionnaire accepted.` |

## Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)（提交充值问卷(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`PUT /sapi/v1/localentity/deposit/provide-info`

Submit questionnaire for local entities that require travel rule.
The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not
yet onboarded with GTR.

提交充值问卷(针对需要旅行规则的本地站)。
只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。

Operation ID: `submitDepositQuestionnaireTravelRule`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) | 是 | Wallet tran ID<br>充值记录ID<br>例: `1` |
| questionnaire | string | 是 | JSON format questionnaire answers.<br>JSON 格式问卷内容<br>例: `None` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Submit Deposit Questionnaire / 提交充值问卷

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trId | integer (int64) |  | 例: `765127651` |
| accepted | boolean |  | 例: `True` |
| info | string |  | 例: `Deposit questionnaire accepted.` |

## Submit Deposit Questionnaire V2 (For local entities that require travel rule) (supporting network) (USER_DATA)（提交充值问卷V2(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`PUT /sapi/v2/localentity/deposit/provide-info`

Submit questionnaire for local entities that require travel rule.
The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not
yet onboarded with GTR.

提交充值问卷(针对需要旅行规则的本地站)。
只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。

Operation ID: `submitDepositQuestionnaireV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| depositId | integer (int64) | 是 | Wallet deposit ID<br>充值记录ID<br>例: `1` |
| questionnaire | string | 是 | JSON format questionnaire answers.<br>JSON 格式问卷内容<br>例: `None` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Submit Deposit Questionnaire V2 / 提交充值问卷 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trId | integer (int64) |  | 例: `765127651` |
| accepted | boolean |  | 例: `True` |
| info | string |  | 例: `Deposit questionnaire accepted.` |

## VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)（获取VASP列表(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`GET /sapi/v1/localentity/vasp`

Fetch the VASP list for local entities.

获取旅行规则的本地站的VASP列表。

Operation ID: `vaspList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：VASP list / VASP 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].vaspName | string |  | 例: `Binance` |
| [].vaspCode | string |  | 例: `BINANCE` |
| [].identifier | string |  | For populating the `vasp` field in the deposit/withdrawal questionnaire<br>用于填写充值/提现问卷中的 `vasp` 字段<br>例: `xxx` |

## Withdraw History Travel Rule (supporting network) (USER_DATA)（获取提币历史(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`GET /sapi/v1/localentity/withdraw/history`

Fetch withdraw history for local entities that required travel rule.

获取需要旅行规则的本地站的提币历史记录

Operation ID: `withdrawHistoryV1`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| trId | query | string |  | Comma(,) separated list of travel rule record Ids.<br>旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| txId | query | string |  | Comma(,) separated list of transaction Ids.<br>链上TxId，支持多条查询，以半角逗号(,) 分隔.<br>例: `1` |
| withdrawOrderId | query | string |  | client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for<br>query.<br>用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单<br>例: `1` |
| network | query | string |  | 例: `None` |
| coin | query | string |  | 例: `BTC` |
| travelRuleStatus | query | integer (int64) |  | 0: Completed,1: Pending,2: Failed<br>0:处理完成,1:处理中,2:请求被拒绝<br>例: `0` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdraw History / 提币历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | Withdrawal id in Binance<br>该笔提现在币安的id, 只在sAPI提现的记录中返回<br>例: `b6ae22b3aa844210a7041aee7589627c` |
| [].trId | integer (int64) |  | Travel rule record id<br>旅行规则记录Id<br>例: `1234456` |
| [].amount | string |  | withdrawal amount<br>提现转出金额<br>例: `8.91000000` |
| [].transactionFee | string |  | only available for sAPI requests<br>手续费, 只在sAPI提现的记录中返回<br>例: `0.004` |
| [].coin | string |  | 例: `USDT` |
| [].withdrawalStatus | integer (int64) |  | Capital withdrawal status, only available for sAPI requests<br>提币状态, 只在sAPI提现的记录中返回<br>例: `6` |
| [].travelRuleStatus | integer (int64) |  | Travel rule status.<br>旅行规则处理状态，处理完成(0)之后才会继续提币流程<br>例: `0` |
| [].address | string |  | 例: `0x94df8b352de7f46f64b01d3666bf6e936e44ce60` |
| [].txId | string |  | withdrawal transaction id<br>提现交易id<br>例: `0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268` |
| [].applyTime | string |  | UTC time<br>UTC 时间<br>例: `2019-10-12 11:12:02` |
| [].network | string |  | 例: `ETH` |
| [].transferType | integer (int64) |  | 1 for internal transfer, 0 for external transfer, only available for sAPI requests<br>1: 站内转账, 0: 站外转账, 只在sAPI提现的记录中返回<br>例: `0` |
| [].withdrawOrderId | string |  | will not be returned if there's no withdrawOrderId for this withdraw, only available for sAPI requests<br>自定义ID, 如果没有则不返回该字段, 只在sAPI提现的记录中返回<br>例: `WITHDRAWtest123` |
| [].info | string |  | reason for withdrawal failure, only available for sAPI requests<br>提币失败原因, 只在sAPI提现的记录中返回<br>例: `The address is not valid. Please confirm with the recipient` |
| [].confirmNo | integer (int64) |  | confirm times for withdraw, only available for sAPI requests<br>提现确认数, 只在sAPI提现的记录中返回<br>例: `3` |
| [].walletType | integer (int64) |  | 1: Funding Wallet 0:Spot Wallet, only available for sAPI requests<br>1: 资金钱包 0:现货钱包, 只在sAPI提现的记录中返回<br>例: `1` |
| [].txKey | string |  | only available for sAPI requests<br>只在sAPI提现的记录中返回<br>例: `` |
| [].questionnaire | string |  | The answers of the questionnaire<br>问卷回答<br>例: `{"question1":"answer1","question2":"answer2"}` |
| [].completeTime | string |  | complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)<br>提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回<br>例: `2023-03-23 16:52:41` |

## Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)（获取提币历史V2(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)）

`GET /sapi/v2/localentity/withdraw/history`

Fetch withdraw history for local entities that required travel rule.

获取需要旅行规则的本地站的提币历史记录

Operation ID: `withdrawHistoryV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| trId | query | string |  | Comma(,) separated list of travel rule record Ids.<br>旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔<br>例: `1` |
| txId | query | string |  | Comma(,) separated list of transaction Ids.<br>链上TxId，支持多条查询，以半角逗号(,) 分隔.<br>例: `1` |
| withdrawOrderId | query | string |  | client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for<br>query.<br>用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单<br>例: `1` |
| network | query | string |  | 例: `None` |
| coin | query | string |  | 例: `None` |
| travelRuleStatus | query | integer (int64) |  | 0: Completed,1: Pending,2: Failed<br>0:处理完成,1:处理中,2:请求被拒绝<br>例: `0` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| limit | query | integer (int64) |  | 默认: `1000`<br>例: `1000` |
| startTime | query | integer (int64) |  | Default: 90 days from current timestamp<br>默认当前时间90天前的时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认当前时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdraw History V2 / 提币历史 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | Withdrawal id in Binance<br>该笔提现在币安的id, 只在sAPI提现的记录中返回<br>例: `b6ae22b3aa844210a7041aee7589627c` |
| [].trId | integer (int64) |  | Travel rule record id<br>旅行规则记录Id<br>例: `1234456` |
| [].amount | string |  | withdrawal amount<br>提现转出金额<br>例: `8.91000000` |
| [].transactionFee | string |  | only available for sAPI requests<br>手续费, 只在sAPI提现的记录中返回<br>例: `0.004` |
| [].coin | string |  | 例: `USDT` |
| [].withdrawalStatus | integer (int64) |  | Capital withdrawal status, only available for sAPI requests<br>提币状态, 只在sAPI提现的记录中返回<br>例: `6` |
| [].travelRuleStatus | integer (int64) |  | Travel rule status.<br>旅行规则处理状态，处理完成(0)之后才会继续提币流程<br>例: `0` |
| [].address | string |  | 例: `0x94df8b352de7f46f64b01d3666bf6e936e44ce60` |
| [].txId | string |  | withdrawal transaction id<br>提现交易id<br>例: `0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268` |
| [].applyTime | string |  | UTC time<br>UTC 时间<br>例: `2019-10-12 11:12:02` |
| [].network | string |  | 例: `ETH` |
| [].transferType | integer (int64) |  | 1 for internal transfer, 0 for external transfer, only available for sAPI requests<br>1: 站内转账, 0: 站外转账, 只在sAPI提现的记录中返回<br>例: `0` |
| [].withdrawOrderId | string |  | will not be returned if there's no withdrawOrderId for this withdraw, only available for sAPI requests<br>自定义ID, 如果没有则不返回该字段, 只在sAPI提现的记录中返回<br>例: `WITHDRAWtest123` |
| [].info | string |  | reason for withdrawal failure, only available for sAPI requests<br>提币失败原因, 只在sAPI提现的记录中返回<br>例: `The address is not valid. Please confirm with the recipient` |
| [].confirmNo | integer (int64) |  | confirm times for withdraw, only available for sAPI requests<br>提现确认数, 只在sAPI提现的记录中返回<br>例: `3` |
| [].walletType | integer (int64) |  | 1: Funding Wallet 0:Spot Wallet, only available for sAPI requests<br>1: 资金钱包 0:现货钱包, 只在sAPI提现的记录中返回<br>例: `1` |
| [].txKey | string |  | only available for sAPI requests<br>只在sAPI提现的记录中返回<br>例: `` |
| [].questionnaire | string |  | The answers of the questionnaire<br>问卷回答<br>例: `{"question1":"answer1","question2":"answer2"}` |
| [].completeTime | string |  | complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)<br>提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回<br>例: `2023-03-23 16:52:41` |

## Withdraw Travel Rule (USER_DATA)（提币(针对需要旅行规则的本地站) (USER_DATA)）

`POST /sapi/v1/localentity/withdraw/apply`

Submit a withdrawal request for local entities that required travel rule.

向需要旅行规则的本地站发起提币请求

Operation ID: `withdrawTravelRule`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 例: `BTC` |
| withdrawOrderId | string |  | withdrawID defined by the client (i.e. client's internal withdrawID)<br>客户端内部定义的提币ID.<br>例: `1` |
| network | string |  | Withdrawal network<br>提币网络<br>例: `None` |
| address | string | 是 | Withdrawal address<br>提币地址<br>例: `None` |
| addressTag | string |  | Secondary address identifier for coins like XRP,XMR etc.<br>某些币种例如 XRP,XMR 允许填写次级地址标签<br>例: `None` |
| amount | number (float) | 是 | Amount<br>数量<br>例: `1.0` |
| transactionFeeFlag | boolean |  | When making internal transfer, `true` for returning the fee to the destination account; `false` for<br>returning the fee back to the departure account. Default `false`.<br>当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`.<br>例: `True` |
| name | string |  | 例: `None` |
| walletType | integer (int64) |  | The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current<br>"selected wallet" under wallet->Fiat and Spot/Funding->Deposit<br>表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。<br>例: `0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| questionnaire | string | 是 | JSON format questionnaire answers.<br>JSON 格式的问卷回答。<br>例: `None` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Withdraw / 提币

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trId | integer (int64) |  | The travel rule record Id<br>Travel Rule记录ID<br>例: `123456` |
| accepted | boolean |  | Whether the withdraw request is accepted<br>提币请求是否被接受<br>例: `True` |
| info | string |  | The detailed infomation of the withdrawal result.<br>提现结果的详细信息<br>例: `Withdraw request accepted` |