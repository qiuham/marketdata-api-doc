---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-caas/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:19.922689
---

# Crypto-As-A-Service (CAAS) REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-caas/api/rest-api/1.0.0/schema.yaml

Manage CAAS accounts, assets, and commission data via the Binance Link CAAS API.

通过 Binance Link CAAS API 管理 CAAS 账户、资产和佣金数据。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`

## 接口列表

- `POST /sapi/v1/broker/subAccountApi/permission` — Change Sub Account API Permission
- `GET /sapi/v1/broker/subAccount` — Query Sub Account
- `POST /sapi/v1/broker/subAccount` — Create a Sub Account
- `DELETE /sapi/v1/broker/subAccount` — Delete Sub Account
- `GET /sapi/v1/broker/subAccountApi` — Query Sub Account Api Key
- `POST /sapi/v1/broker/subAccountApi` — Create Api Key for Sub Account
- `DELETE /sapi/v1/broker/subAccountApi` — Delete Sub Account Api Key
- `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList` — Delete IP Restriction for Sub Account API Key
- `POST /sapi/v1/broker/subAccount/futures` — Enable Futures for Sub Account
- `POST /sapi/v1/broker/subAccount/bnbBurn/marginInterest` — Enable Or Disable BNB Burn for Sub Account Margin Interest
- `POST /sapi/v1/broker/subAccount/bnbBurn/spot` — Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN
- `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer` — Enable Universal Transfer Permission for Sub Account API Key
- `GET /sapi/v1/broker/subAccount/bnbBurn/status` — Get BNB Burn Status for Sub Account
- `GET /sapi/v1/broker/subAccountApi/ipRestriction` — Get IP Restriction for Sub Account API Key
- `GET /sapi/v1/broker/info` — Link Account Information (USER_DATA)
- `POST /sapi/v2/broker/subAccountApi/ipRestriction` — Update IP Restriction for Sub-Account API Key (For Master Account) (USER_DATA)
- `POST /sapi/v1/broker/futures/accountTransfer` — Futures Transfer for Link Sub Account (For Master Account) (USER_DATA)
- `GET /sapi/v1/broker/subAccount/depositHist` — Get Sub Account Deposit History
- `GET /sapi/v2/broker/subAccount/depositHist` — Get Sub Account Deposit History V2
- `GET /sapi/v3/broker/subAccount/futuresSummary` — Query Sub Account Futures Asset Info (V3)
- `GET /sapi/v1/broker/subAccount/marginSummary` — Query Sub Account Margin Asset Info
- `GET /sapi/v1/broker/subAccount/spotSummary` — Query Sub Account Spot Asset Info
- `GET /sapi/v1/broker/transfer/futures` — Query Sub Account Transfer History（FUTURES）
- `POST /sapi/v1/broker/transfer/futures` — Sub Account Transfer（FUTURES）
- `GET /sapi/v1/broker/transfer` — Query Sub Account Transfer History（SPOT）
- `POST /sapi/v1/broker/transfer` — Sub Account Transfer（SPOT）
- `GET /sapi/v1/broker/universalTransfer` — Query Universal Transfer History
- `POST /sapi/v1/broker/universalTransfer` — Universal Transfer
- `GET /sapi/v1/broker/subAccountApi/commission/coinFutures` — Query Sub Account COIN-Ⓜ Futures Commission Adjustment
- `POST /sapi/v1/broker/subAccountApi/commission/coinFutures` — Change Sub Account COIN-Ⓜ Futures Commission Adjustment
- `POST /sapi/v1/broker/subAccountApi/commission` — Change Sub Account Commission
- `GET /sapi/v1/broker/subAccountApi/commission/futures` — Query Sub Account USDT-Ⓜ Futures Commission Adjustment
- `POST /sapi/v1/broker/subAccountApi/commission/futures` — Change Sub Account USDT-Ⓜ Futures Commission Adjustment
- `GET /sapi/v1/broker/rebate/recentRecord` — Query Spot Commission Rebate Recent Record
- `GET /sapi/v1/broker/rebate/futures/recentRecord` — Query Broker Futures Commission Rebate Record

## Change Sub Account API Permission（修改子账户 API 权限）

`POST /sapi/v1/broker/subAccountApi/permission`

Change Sub Account API Permission

修改子账户 API 权限

Operation ID: `changeSubAccountApiPermission`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| subAccountApiKey | string | 是 | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| canTrade | boolean | 是 | 例: `True` |
| marginTrade | boolean | 是 | 例: `True` |
| futuresTrade | boolean | 是 | 例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Sub Account API Permission / 修改子账户 API 权限

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| apikey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| canTrade | boolean |  | 例: `True` |
| marginTrade | boolean |  | 例: `True` |
| futuresTrade | boolean |  | 例: `True` |

## Query Sub Account（查询子账户）

`GET /sapi/v1/broker/subAccount`

Query Sub Account

查询子账户

Operation ID: `querySubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account / 子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].subaccountId | string |  | 例: `1` |
| [].email | string |  | 例: `vai_42038996_47411276_brokersubuser@lac.info` |
| [].tag | string |  | 例: `bob123` |
| [].makerCommission | number (float) |  | 例: `0.001` |
| [].takerCommission | number (float) |  | 例: `0.001` |
| [].marginMakerCommission | integer (int64) |  | 例: `-1` |
| [].marginTakerCommission | integer (int64) |  | 例: `-1` |
| [].createTime | integer (int64) |  | 例: `1544433328000` |

## Create a Sub Account（创建子账户）

`POST /sapi/v1/broker/subAccount`

Create a Link Sub-account

创建 a链接子账户

Operation ID: `createASubAccount`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tag | string |  | tag length should be less than 32<br>tag 长度应小于 32<br>例: `bob123d` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create a Sub Account / 创建子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| email | string |  | 例: `vai_42038996_47411276_brokersubuser@lac.info` |
| tag | string |  | 例: `bob123d` |

## Delete Sub Account（删除子账户）

`DELETE /sapi/v1/broker/subAccount`

Delete Sub Account
Caution:
  * The operation will delete a sub account under your brokerage master account.
  * Please transfer out all funds from the sub account and delete API key of the sub account before deleting it.
  * The deleted sub account CANNOT be reverted.
  * The daily deletion limit for a broker Master is 20 sub accounts.
  * You need to enable "trade" option for the api key which requests this endpoint.
  * This endpoint requires user to be whitelisted. Please contact Binance Link team.

删除子账户
注意：
  * 该操作将删除您经纪商主账户下的一个子账户。
  * 删除前请先将子账户资金全部转出，并删除该子账户的 API Key。
  * 删除后的子账户无法恢复。
  * 经纪商主账户每日最多可删除 20 个子账户。
  * 发起该请求的 API Key 需要启用 "trade" 权限。
  * 该接口要求用户在白名单中，请联系 Binance Link 团队。

Operation ID: `deleteSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Query Sub Account Api Key（查询子账户 API Key）

`GET /sapi/v1/broker/subAccountApi`

Query Sub Account Api Key

查询子账户 API Key

Operation ID: `querySubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| subAccountApiKey | query | string |  | 例: `vmP*************` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Api Key / 子账户 API Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].apikey | string |  | 例: `vmP*************` |
| [].subaccountId | string |  | 例: `1` |
| [].canTrade | boolean |  | 例: `True` |
| [].marginTrade | boolean |  | 例: `True` |
| [].futuresTrade | boolean |  | 例: `False` |

## Create Api Key for Sub Account（为子账户创建 API Key）

`POST /sapi/v1/broker/subAccountApi`

Create Api Key for Sub Account

为子账户创建 API Key

Operation ID: `createApiKeyForSubAccount`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| publicKey | string |  | The public key for asymmetrical key type(Ed25519 and RSA). Please see<br>https://www.binance.com/en/support/faq/detail/6b9a63f1e3384cf48a2eedb82767a69a<br>非对称密钥类型（Ed25519 和 RSA）的公钥。请参考：<br>https://www.binance.com/en/support/faq/detail/6b9a63f1e3384cf48a2eedb82767a69a<br>例: `None` |
| canTrade | boolean | 是 | spot trade<br>现货 交易<br>例: `True` |
| marginTrade | boolean |  | margin trade<br>杠杆 交易<br>例: `True` |
| futuresTrade | boolean |  | futures trade<br>合约 交易<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create Api Key for Sub Account / 为子账户创建 API Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| apiKey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| secretKey | string |  | Returned only for HMAC API Keys, that is when `publicKey` is not supplied. It is returned<br>once on creation and cannot be retrieved again, so store it securely. When `publicKey` is<br>supplied the API Key is asymmetric (Ed25519 or RSA), the private key never leaves your<br>side, and this field is omitted from the response.<br>仅在创建 HMAC 类型 API Key（即未传 `publicKey`）时返回。该字段仅在创建时返回一次，<br>无法再次获取，请妥善保存。当传入 `publicKey` 时，创建的是非对称（Ed25519 或 RSA）<br>API Key，私钥始终保留在客户端，响应中不会返回该字段。<br>例: `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0` |
| canTrade | boolean |  | 例: `True` |
| marginTrade | boolean |  | 例: `False` |
| futuresTrade | boolean |  | 例: `False` |

## Delete Sub Account Api Key（删除子账户 API Key）

`DELETE /sapi/v1/broker/subAccountApi`

Delete Sub Account Api Key

Caution:
  * This request will delete a api key for a sub account
  * You need to enable "trade" option for the api key which requests this endpoint
  * You can only delete 1 api key for each sub account per second

删除子账户 API Key

注意：
  * 此请求将删除一个子账户 API Key
  * 发起该请求的 API Key 需要启用 "trade" 权限
  * 每个子账户每秒仅可删除 1 个 API Key

Operation ID: `deleteSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| subAccountApiKey | query | string | 是 | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Delete IP Restriction for Sub Account API Key（删除子账户 API Key 的 IP 限制）

`DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList`

Delete IP Restriction for Sub Account API Key

删除子账户 API Key 的 IP 限制

Operation ID: `deleteIpRestrictionForSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| subAccountApiKey | query | string | 是 | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| ipAddress | query | string |  | 例: `54.128.193.28` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Delete IP Restriction for Sub Account API Key / 删除子账户 API Key 的 IP 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| apikey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1544433328000` |

## Enable Futures for Sub Account（启用合约 用于 子账户）

`POST /sapi/v1/broker/subAccount/futures`

Enable Futures for Sub Account

启用合约 用于 子账户

Operation ID: `enableFuturesForSubAccount`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| futures | string | 是 | only `true` for now<br>当前仅支持 `true`<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Futures for Sub Account / 启用合约 用于 子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| enableFutures | boolean |  | 例: `True` |
| updateTime | integer (int64) |  | 例: `1570801523523` |

## Enable Or Disable BNB Burn for Sub Account Margin Interest（启用或禁用子账户杠杆利息 BNB 燃烧）

`POST /sapi/v1/broker/subAccount/bnbBurn/marginInterest`

Enable Or Disable BNB Burn for Sub Account Margin Interest

启用或禁用子账户杠杆利息 BNB 燃烧

Operation ID: `enableOrDisableBnbBurnForSubAccountMarginInterest`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| interestBNBBurn | boolean | 是 | "true" or "false", margin loan whether uses BNB to pay for margin interest or not<br>"true" 或 "false"，是否使用 BNB 支付杠杆利息。<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Or Disable BNB Burn for Sub Account Margin Interest / 启用或禁用子账户杠杆利息 BNB 燃烧

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | integer (int64) |  | 例: `1` |
| interestBNBBurn | boolean |  | 例: `True` |

## Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN（启用或禁用子账户现货与杠杆 BNB 燃烧）

`POST /sapi/v1/broker/subAccount/bnbBurn/spot`

Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN

启用或禁用子账户现货与杠杆 BNB 燃烧

Operation ID: `enableOrDisableBnbBurnForSubAccountSpotAndMargin`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| spotBNBBurn | boolean | 是 | "true" or "false", spot and margin whether use BNB to pay for transaction fees or not<br>"true" 或 "false"，现货和杠杆交易是否使用 BNB 支付手续费。<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN / 启用或禁用子账户现货与杠杆 BNB 燃烧

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | integer (int64) |  | 例: `1` |
| spotBNBBurn | boolean |  | 例: `True` |

## Enable Universal Transfer Permission for Sub Account API Key（为子账户 API Key 启用万能划转权限）

`POST /sapi/v1/broker/subAccountApi/permission/universalTransfer`

Enable Universal Transfer Permission for Sub Account API Key

为子账户 API Key 启用万能划转权限

Operation ID: `enableUniversalTransferPermissionForSubAccountApiKey`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| subAccountApiKey | string | 是 | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| canUniversalTransfer | boolean | 是 | true or false<br>true 或 false<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Universal Transfer Permission for Sub Account API Key / 为子账户 API Key 启用万能划转权限

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| apikey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| canUniversalTransfer | boolean |  | 例: `True` |

## Get BNB Burn Status for Sub Account（获取子账户 BNB 燃烧状态）

`GET /sapi/v1/broker/subAccount/bnbBurn/status`

Get BNB Burn Status for Sub Account

获取子账户 BNB 燃烧状态

Operation ID: `getBnbBurnStatusForSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BNB Burn Status for Sub Account / 获取子账户 BNB 燃烧状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | integer (int64) |  | 例: `1` |
| spotBNBBurn | boolean |  | 例: `True` |
| interestBNBBurn | boolean |  | 例: `True` |

## Get IP Restriction for Sub Account API Key（获取子账户 API Key 的 IP 限制）

`GET /sapi/v1/broker/subAccountApi/ipRestriction`

Get IP Restriction for Sub Account API Key

获取子账户 API Key 的 IP 限制

Operation ID: `getIpRestrictionForSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| subAccountApiKey | query | string | 是 | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get IP Restriction for Sub Account API Key / 获取子账户 API Key 的 IP 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountId | string |  | 例: `1` |
| ipRestrict | boolean |  | 例: `True` |
| apikey | string |  | 例: `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1544433328000` |

## Link Account Information (USER_DATA)（链接账户信息 (USER_DATA)）

`GET /sapi/v1/broker/info`

Get link account information.

获取链接账户信息。

Operation ID: `linkAccountInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Link Account Information / 链接账户信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| maxMakerCommission | number (float) |  | Maximum maker commission rate<br>最大挂单手续费率<br>例: `0.002` |
| minMakerCommission | number (float) |  | Minimum maker commission rate<br>最小挂单手续费率<br>例: `0.001` |
| maxTakerCommission | number (float) |  | Maximum taker commission rate<br>最大吃单手续费率<br>例: `0.002` |
| minTakerCommission | number (float) |  | Minimum taker commission rate<br>最小吃单手续费率<br>例: `0.001` |
| subAccountQty | integer (int64) |  | Current number of sub-accounts<br>当前子账户数量<br>例: `400` |
| maxSubAccountQty | integer (int64) |  | Maximum allowed sub-accounts<br>最大允许子账户数量<br>例: `1000` |

## Update IP Restriction for Sub-Account API Key (For Master Account) (USER_DATA)（更新子账户 API Key 的 IP 限制（主账户） (USER_DATA)）

`POST /sapi/v2/broker/subAccountApi/ipRestriction`

Update IP Restriction for Sub-Account API Key

更新子账户 API Key 的 IP 限制

Operation ID: `updateIpRestrictionForSubAccountApiKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| subAccountApiKey | string | 是 | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |
| status | integer (int64) | 是 | IP restriction status. 1 = IP unrestricted. 2 = Restrict access to trusted IPs only.<br>IP 限制状态。1 = 不限制 IP；2 = 仅允许受信任 IP 访问。<br>例: `1` |
| ipAddress | string |  | Insert static IP in batch, separated by commas.<br>批量填写静态 IP，多个 IP 用逗号分隔。<br>例: `24.156.99.202` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Update IP Restriction for Sub-Account API Key / 更新子账户 API Key 的 IP 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `2` |
| ipList | string[] |  |  |
| updateTime | integer (int64) |  | 例: `1636371437000` |
| apiKey | string |  | 例: `k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf` |

## Futures Transfer for Link Sub Account (For Master Account) (USER_DATA)（Link 子账户合约划转（主账户） (USER_DATA)）

`POST /sapi/v1/broker/futures/accountTransfer`

Futures Transfer for Link Sub Account

Link 子账户合约划转。

Operation ID: `futuresTransferForLinkSubAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| asset | string | 是 | The asset being transferred, e.g., USDT<br>划转资产，例如 USDT<br>例: `USDT` |
| amount | number (float) | 是 | The amount to be transferred<br>划转数量<br>例: `1` |
| type | integer (int64) | 是 | 1: transfer from subaccount's spot account to its USDT-margined futures account 2: transfer from<br>subaccount's USDT-margined futures account to its spot account 3: transfer from subaccount's spot<br>account to its COIN-margined futures account 4: transfer from subaccount's COIN-margined futures<br>account to its spot account<br>1: 从子账户现货账户划转到其 U 本位合约账户<br>2: 从子账户 U 本位合约账户划转到其现货账户<br>3: 从子账户现货账户划转到其币本位合约账户<br>4: 从子账户币本位合约账户划转到其现货账户<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Transfer for Link Sub Account / Link 子账户合约划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |

## Get Sub Account Deposit History（获取子账户充值历史）

`GET /sapi/v1/broker/subAccount/depositHist`

Get Sub Account Deposit History

获取子账户充值历史

Operation ID: `getSubAccountDepositHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| coin | query | string |  | 例: `USDT` |
| status | query | integer (int64) |  | 0(0: pending,6: credited but cannot withdraw, 1: success)<br>0：处理中，6：已入账但不可提现，1：成功<br>例: `0` |
| startTime | query | integer (int64) |  | Default: 7 days from current timestamp<br>默认：从当前时间戳往前 7 天<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认：当前时间戳<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Sub Account Deposit History / 获取子账户充值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].depositId | integer (int64) |  | 例: `1234567890123` |
| [].subAccountId | string |  | 例: `1` |
| [].address | string |  | 例: `0xddc66e4313fd6c737b6cae67cad90bb4e0ac7092` |
| [].addressTag | string |  | 例: `` |
| [].amount | string |  | 例: `139.04370000` |
| [].coin | string |  | 例: `USDT` |
| [].insertTime | integer (int64) |  | 例: `1566791463000` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].network | string |  | 例: `ETH` |
| [].status | integer (int64) |  | 例: `1` |
| [].txId | string |  | 例: `0x5759dfe9983a4c7619bce9bc736bb6c26f804091753bf66fa91e7cd5cfeebafd` |
| [].sourceAddress | string |  | 例: `xxxxxxxxxxxxxx` |
| [].confirmTimes | string |  | 例: `12/12` |
| [].selfReturnStatus | integer (int64) |  | 例: `0` |
| [].travelRuleStatus | integer (int64) |  | 0: travel rule not required or information already provided and funds are ready to use, 1:<br>travel rule requires additional deposit information<br>0: 不需要 travel rule 或已提供信息且资金可用，1: 需要根据 travel rule 补充入金信息<br>例: `0` |

## Get Sub Account Deposit History V2（获取子账户充值历史 V2）

`GET /sapi/v2/broker/subAccount/depositHist`

Get Sub Account Deposit History V2

获取子账户充值历史 V2

Operation ID: `getSubAccountDepositHistoryV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| depositId | query | string | 是 | 例: `1` |
| subAccountId | query | string | 是 | 例: `1` |
| limit | query | integer (int64) |  | 默认: `50`<br>例: `50` |
| offset | query | integer (int64) |  | 默认: `0`<br>例: `0` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Sub Account Deposit History V2 / 获取子账户充值历史 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].depositId | integer (int64) |  | 例: `1234567890123` |
| [].subAccountId | string |  | 例: `1` |
| [].address | string |  | 例: `0xddc66e4313fd6c737b6cae67cad90bb4e0ac7092` |
| [].addressTag | string |  | 例: `` |
| [].amount | string |  | 例: `139.04370000` |
| [].coin | string |  | 例: `USDT` |
| [].insertTime | integer (int64) |  | 例: `1566791463000` |
| [].transferType | integer (int64) |  | 例: `0` |
| [].network | string |  | 例: `ETH` |
| [].status | integer (int64) |  | 例: `3` |
| [].txId | string |  | 例: `0x5759dfe9983a4c7619bce9bc736bb6c26f804091753bf66fa91e7cd5cfeebafd` |
| [].sourceAddress | string |  | Source address of the deposit<br>充值来源地址<br>例: `xxxxxxxxxxxxxx` |
| [].confirmTimes | string |  | 例: `12/12` |
| [].selfReturnStatus | integer (int64) |  | 例: `0` |
| [].travelRuleStatus | integer (int64) |  | 例: `0` |

## Query Sub Account Futures Asset Info (V3)（查询子账户合约资产信息 (V3)）

`GET /sapi/v3/broker/subAccount/futuresSummary`

Query Sub Account Futures Asset Info

查询子账户合约资产信息

Operation ID: `querySubAccountFuturesAssetInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| futuresType | query | integer (int64) | 是 | 1: USDT Futures, 2: Coin Futures<br>1: U本位合约, 2: 币本位合约<br>例: `1` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Futures Asset Info / 子账户 合约 资产 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| data | object[] |  |  |
| data[].subAccountId | string |  | 例: `1` |
| data[].totalInitialMargin | string |  | 例: `0.0000000000` |
| data[].totalMaintenanceMargin | string |  | 例: `0.0000000000` |
| data[].totalWalletBalance | string |  | 例: `577.6799732808` |
| data[].totalUnrealizedProfit | string |  | 例: `0.0000000000` |
| data[].totalMarginBalance | string |  | 例: `577.6799732808` |
| data[].totalPositionInitialMargin | string |  | 例: `0.0000000000` |
| data[].totalOpenOrderInitialMargin | string |  | 例: `0.0000000000` |
| data[].futuresEnable | boolean |  | 例: `True` |
| data[].asset | string |  | 例: `USD` |
| data[].totalWalletBalanceOfUsdt | string |  | 例: `6.73252085685700` |
| data[].totalUnrealizedProfitOfUsdt | string |  | 例: `0.00000000000000` |
| data[].totalMarginBalanceOfUsdt | string |  | 例: `6.73252085685700` |
| timestamp | integer (int64) |  | 例: `1583127900000` |

## Query Sub Account Margin Asset Info（查询子账户杠杆资产信息）

`GET /sapi/v1/broker/subAccount/marginSummary`

Query Sub Account Margin Asset Info

查询子账户杠杆资产信息

Operation ID: `querySubAccountMarginAssetInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Margin Asset Info / 子账户 杠杆 资产 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| data | object[] |  |  |
| data[].marginEnable | boolean |  | 例: `True` |
| data[].subAccountId | string |  | 例: `367537027503425913` |
| data[].totalAssetOfBtc | string |  | 例: `0.03558520` |
| data[].totalLiabilityOfBtc | string |  | 例: `0.34585210` |
| data[].totalNetAssetOfBtc | string |  | 例: `0.23334213` |
| data[].marginLevel | string |  | 例: `0.009` |
| timestamp | integer (int64) |  | 例: `1583127900000` |

## Query Sub Account Spot Asset Info（查询子账户现货资产信息）

`GET /sapi/v1/broker/subAccount/spotSummary`

Query Sub Account Spot Asset Info

查询子账户现货资产信息

Operation ID: `querySubAccountSpotAssetInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Spot Asset Info / 子账户 现货 资产 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| data | object[] |  |  |
| data[].subAccountId | string |  | 例: `367537027503425913` |
| data[].totalBalanceOfBtc | string |  | 例: `0.0355852154360000` |
| timestamp | integer (int64) |  | 例: `1583432900000` |

## Query Sub Account Transfer History（FUTURES）（查询子账户 划转 历史（合约））

`GET /sapi/v1/broker/transfer/futures`

Query Sub Account Transfer History（FUTURES）

查询子账户 划转 历史（合约）

Operation ID: `querySubAccountTransferHistoryFutures`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| futuresType | query | integer (int64) | 是 | 1: USDT Futures, 2: Coin Futures<br>1: U本位合约, 2: 币本位合约<br>例: `1` |
| clientTranId | query | string |  | 例: `1` |
| startTime | query | integer (int64) |  | Default: 30 days from current timestamp<br>默认：从当前时间戳往前 30 天<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认：当前时间戳<br>例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `50`<br>例: `50` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Transfer History（FUTURES） / 子账户 划转 历史（合约）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| futuresType | integer (int64) |  | 例: `2` |
| transfers | object[] |  |  |
| transfers[].from | string |  | 例: `` |
| transfers[].to | string |  | 例: `2` |
| transfers[].asset | string |  | 例: `BTC` |
| transfers[].qty | string |  | 例: `1` |
| transfers[].tranId | string |  | 例: `12137888538` |
| transfers[].clientTranId | string |  | 例: `a123` |
| transfers[].time | integer (int64) |  | 例: `1544433328000` |
| transfers[].fromId | string |  | 例: `1` |
| transfers[].toId | string |  | 例: `2` |

## Sub Account Transfer（FUTURES）（子账户 划转（合约））

`POST /sapi/v1/broker/transfer/futures`

Sub Account Transfer（FUTURES）

子账户 划转（合约）

Operation ID: `subAccountTransferFutures`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromId | string |  | 例: `1` |
| toId | string |  | 例: `1` |
| futuresType | integer (int64) | 是 | 1: USDT Futures,2: COIN Futures<br>1: U本位合约,2: COIN 合约<br>例: `1` |
| asset | string | 是 | 例: `BTCUSDT` |
| amount | number (float) | 是 | 例: `1` |
| clientTranId | string |  | Client transfer ID<br>客户端划转 ID<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Transfer（FUTURES） / 子账户 划转（合约）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |
| txnId | string |  | 例: `2966662589` |
| clientTranId | string |  | 例: `a123` |

## Query Sub Account Transfer History（SPOT）（查询子账户 划转 历史（现货））

`GET /sapi/v1/broker/transfer`

Query Sub Account Transfer History（SPOT）

查询子账户 划转 历史（现货）

Operation ID: `querySubAccountTransferHistorySpot`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromId | query | string |  | 例: `1` |
| toId | query | string |  | 例: `1` |
| clientTranId | query | string |  | Client transfer ID<br>客户端划转 ID<br>例: `1` |
| showAllStatus | query | boolean |  | 例: `True` |
| startTime | query | integer (int64) |  | Default: 7 days from current timestamp<br>默认：从当前时间戳往前 7 天<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认：当前时间戳<br>例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Transfer History（SPOT） / 子账户 划转 历史（现货）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].fromId | string |  | 例: `1` |
| [].toId | string |  | 例: `2` |
| [].asset | string |  | 例: `BTC` |
| [].qty | string |  | 例: `1` |
| [].time | integer (int64) |  | 例: `1544433328000` |
| [].txnId | string |  | 例: `2966662589` |
| [].clientTranId | string |  | 例: `abc` |
| [].status | string |  | 例: `SUCCESS` |

## Sub Account Transfer（SPOT）（子账户 划转（现货））

`POST /sapi/v1/broker/transfer`

Sub Account Transfer（SPOT）

子账户 划转（现货）

Operation ID: `subAccountTransferSpot`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromId | string |  | 例: `1` |
| toId | string |  | 例: `1` |
| clientTranId | string |  | Client transfer ID. Must be unique.<br>客户端划转 ID，必须唯一。<br>例: `1` |
| asset | string | 是 | 例: `BTCUSDT` |
| amount | number (float) | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account Transfer（SPOT） / 子账户 划转（现货）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | string |  | 例: `2966662589` |
| clientTranId | string |  | 例: `abc` |

## Query Universal Transfer History（查询万能划转 历史）

`GET /sapi/v1/broker/universalTransfer`

Query Universal Transfer History

查询万能划转 历史

Operation ID: `queryUniversalTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromId | query | string |  | 例: `1` |
| toId | query | string |  | 例: `1` |
| clientTranId | query | string |  | Client transfer ID<br>客户端划转 ID<br>例: `1` |
| startTime | query | integer (int64) |  | Default: 7 days from current timestamp<br>默认：从当前时间戳往前 7 天<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认：当前时间戳<br>例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| showAllStatus | query | boolean |  | 例: `True` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Universal Transfer History / 万能划转 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].toId | string |  | 例: `444016824578949121` |
| [].asset | string |  | 例: `BTC` |
| [].qty | string |  | 例: `0.1` |
| [].time | integer (int64) |  | 例: `1544433328000` |
| [].status | string |  | 例: `SUCCESS` |
| [].txnId | string |  | 例: `12831078279` |
| [].clientTranId | string |  | 例: `abc` |
| [].fromAccountType | string |  | 例: `SPOT` |
| [].toAccountType | string |  | 例: `USDT_FUTURE` |

## Universal Transfer（万能划转）

`POST /sapi/v1/broker/universalTransfer`

Universal Transfer

万能划转

Operation ID: `universalTransfer`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromId | string |  | 例: `1` |
| toId | string |  | 例: `1` |
| fromAccountType | string | 是 | 枚举: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`<br>例: `SPOT` |
| toAccountType | string | 是 | 枚举: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`<br>例: `SPOT` |
| clientTranId | string |  | Client transfer ID. Must be unique.<br>客户端划转 ID，必须唯一。<br>例: `1` |
| asset | string | 是 | 例: `BTCUSDT` |
| amount | number (float) | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Universal Transfer / 万能划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txnId | integer (int64) |  | 例: `12831061179` |
| clientTranId | string |  | 例: `abc` |

## Query Sub Account COIN-Ⓜ Futures Commission Adjustment（查询子账户 COIN-Ⓜ 合约 手续费 调整）

`GET /sapi/v1/broker/subAccountApi/commission/coinFutures`

Query Sub Account COIN-Ⓜ Futures Commission Adjustment

* The sub-account's COIN-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the
sub-account's fee tier plus the commission adjustment.

查询子账户 COIN-Ⓜ 合约手续费调整。
* 子账户某个交易对的 COIN-Ⓜ 合约手续费 = 该交易对在该子账户费率等级对应的基础手续费 + 手续费调整值。

Operation ID: `querySubAccountCoinFuturesCommissionAdjustment`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| pair | query | string | 是 | 例: `BTCUSD` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account COIN-Ⓜ Futures Commission Adjustment / 子账户 COIN-Ⓜ 合约 手续费 调整

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].subAccountId | integer (int64) |  | 例: `1` |
| [].pair | string |  | 例: `BTCUSD` |
| [].makerCommission | integer (int64) |  | 例: `450` |
| [].takerCommission | integer (int64) |  | 例: `550` |

## Change Sub Account COIN-Ⓜ Futures Commission Adjustment（修改子账户 COIN-Ⓜ 合约 手续费 调整）

`POST /sapi/v1/broker/subAccountApi/commission/coinFutures`

* This request will change the COIN-Ⓜ futures commission for a sub account.

* You need to enable "trade" option for the api key which requests this endpoint.

* The sub-account's COIN-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the
sub-account's fee tier plus the commission adjustment.

* 此请求将修改子账户的 COIN-Ⓜ 合约手续费。
* 发起该请求的 API Key 需要启用 "trade" 权限。
* 子账户某个交易对的 COIN-Ⓜ 合约手续费 = 该交易对在该子账户费率等级对应的基础手续费 + 手续费调整值。

Operation ID: `changeSubAccountCoinFuturesCommissionAdjustment`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| pair | string | 是 | 例: `BTCUSD` |
| makerAdjustment | integer (int64) | 是 | Integer, where `100` is 0.01%. Minimum `0`, maximum `100` (0.01%), inclusive.<br>整数，`100` 表示 0.01%。最小 `0`，最大 `100`（0.01%），含边界。<br>例: `100` |
| takerAdjustment | integer (int64) | 是 | Integer, where `100` is 0.01%. Minimum `0`, maximum `500` (0.05%), inclusive.<br>整数，`100` 表示 0.01%。最小 `0`，最大 `500`（0.05%），含边界。<br>例: `100` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Sub Account COIN-Ⓜ Futures Commission Adjustment / 修改子账户 COIN-Ⓜ 合约 手续费 调整

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | integer (int64) |  | 例: `1` |
| pair | string |  | 例: `BTCUSD` |
| makerAdjustment | integer (int64) |  | 例: `150` |
| takerAdjustment | integer (int64) |  | 例: `150` |
| makerCommission | integer (int64) |  | 例: `450` |
| takerCommission | integer (int64) |  | 例: `550` |

## Change Sub Account Commission（修改子账户 手续费）

`POST /sapi/v1/broker/subAccountApi/commission`

* This request will change the commission for a sub account.
* You need to enable "trade" option for the api key which requests this endpoint.

* 此请求将修改子账户手续费。
* 发起该请求的 API Key 需要启用 "trade" 权限。

Operation ID: `changeSubAccountCommission`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| makerCommission | number (float) | 是 | Decimal fraction. Minimum `0.001` (0.1%), maximum `0.002` (0.2%), inclusive.<br>小数形式。最小 `0.001`（0.1%），最大 `0.002`（0.2%），含边界。<br>例: `0.001` |
| takerCommission | number (float) | 是 | Decimal fraction. Minimum `0.001` (0.1%), maximum `0.002` (0.2%), inclusive.<br>小数形式。最小 `0.001`（0.1%），最大 `0.002`（0.2%），含边界。<br>例: `0.002` |
| marginMakerCommission | number (float) |  | Decimal fraction. Minimum `0.001` (0.1%), maximum `0.002` (0.2%), inclusive.<br>小数形式。最小 `0.001`（0.1%），最大 `0.002`（0.2%），含边界。<br>例: `0.001` |
| marginTakerCommission | number (float) |  | Decimal fraction. Minimum `0.001` (0.1%), maximum `0.002` (0.2%), inclusive.<br>小数形式。最小 `0.001`（0.1%），最大 `0.002`（0.2%），含边界。<br>例: `0.002` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Sub Account Commission / 修改子账户 手续费

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string |  | 例: `1` |
| makerCommission | number (float) |  | 例: `0.001` |
| takerCommission | number (float) |  | 例: `0.002` |
| marginMakerCommission | number (float) |  | 例: `0.001` |
| marginTakerCommission | number (float) |  | 例: `0.002` |

## Query Sub Account USDT-Ⓜ Futures Commission Adjustment（查询子账户 USDT-Ⓜ 合约 手续费 调整）

`GET /sapi/v1/broker/subAccountApi/commission/futures`

Query Sub Account USDT-Ⓜ Futures Commission Adjustment

* The sub-account's USDT-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the
sub-account's fee tier plus the commission adjustment.

查询子账户 USDT-Ⓜ 合约手续费调整

- 子账户某交易对的 USDT-Ⓜ 合约手续费 = 该交易对在该子账户费率等级对应的基础手续费 + 手续费调整值。

Operation ID: `querySubAccountUsdtFuturesCommissionAdjustment`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string | 是 | 例: `1` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Account USDT-Ⓜ Futures Commission Adjustment / 子账户 USDT-Ⓜ 合约 手续费 调整

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].subAccountId | integer (int64) |  | 例: `1` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].makerCommission | integer (int64) |  | 例: `450` |
| [].takerCommission | integer (int64) |  | 例: `550` |

## Change Sub Account USDT-Ⓜ Futures Commission Adjustment（修改子账户 USDT-Ⓜ 合约 手续费 调整）

`POST /sapi/v1/broker/subAccountApi/commission/futures`

* This request will change the USDT-Ⓜ futures commission for a sub account.

* You need to enable "trade" option for the api key which requests this endpoint.

* The sub-account's USDT-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the
sub-account's fee tier plus the commission adjustment.

* 此请求将修改子账户的 USDT-Ⓜ 合约手续费。
* 发起该请求的 API Key 需要启用 "trade" 权限。
* 子账户某个交易对的 USDT-Ⓜ 合约手续费 = 该交易对在该子账户费率等级对应的基础手续费 + 手续费调整值。

Operation ID: `changeSubAccountUsdtFuturesCommissionAdjustment`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | string | 是 | 例: `1` |
| symbol | string | 是 | 例: `BTCUSDT` |
| makerAdjustment | integer (int64) | 是 | Integer, where `100` is 0.01%. Minimum `0`, maximum `200` (0.02%), inclusive.<br>整数，`100` 表示 0.01%。最小 `0`，最大 `200`（0.02%），含边界。<br>例: `100` |
| takerAdjustment | integer (int64) | 是 | Integer, where `100` is 0.01%. Minimum `0`, maximum `400` (0.04%), inclusive.<br>整数，`100` 表示 0.01%。最小 `0`，最大 `400`（0.04%），含边界。<br>例: `100` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Sub Account USDT-Ⓜ Futures Commission Adjustment / 修改子账户 USDT-Ⓜ 合约 手续费 调整

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountId | integer (int64) |  | 例: `1` |
| symbol | string |  | 例: `BTCUSDT` |
| makerAdjustment | integer (int64) |  | 例: `150` |
| takerAdjustment | integer (int64) |  | 例: `150` |
| makerCommission | integer (int64) |  | 例: `450` |
| takerCommission | integer (int64) |  | 例: `550` |

## Query Spot Commission Rebate Recent Record（查询现货手续费返佣近期记录）

`GET /sapi/v1/broker/rebate/recentRecord`

Query Spot Commission Rebate Recent Record

查询现货手续费返佣近期记录

Operation ID: `querySpotCommissionRebateRecentRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountId | query | string |  | 例: `1` |
| startTime | query | integer (int64) |  | Default: 7 days from current timestamp<br>默认：从当前时间戳往前 7 天<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Default: present timestamp<br>默认：当前时间戳<br>例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Spot Commission Rebate Recent Record / 现货手续费返佣近期记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].subaccountId | string |  | 例: `1` |
| [].income | string |  | 例: `0.02063898` |
| [].asset | string |  | 例: `BTC` |
| [].symbol | string |  | 例: `ETHBTC` |
| [].tradeId | integer (int64) |  | 例: `123456` |
| [].time | integer (int64) |  | 例: `1544433328000` |
| [].status | integer (int64) |  | 例: `1` |

## Query Broker Futures Commission Rebate Record（查询经纪商合约 手续费 返佣 记录）

`GET /sapi/v1/broker/rebate/futures/recentRecord`

Query Broker Futures Commission Rebate Record

查询经纪商合约 手续费 返佣 记录

Operation ID: `queryBrokerFuturesCommissionRebateRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| futuresType | query | integer (int64) | 是 | 1: USDT Futures, 2: Coin Futures<br>1: U本位合约, 2: 币本位合约<br>例: `1` |
| startTime | query | integer (int64) | 是 | 例: `1623319461670` |
| endTime | query | integer (int64) | 是 | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| filterResult | query | boolean |  | 默认: `False`<br>例: `False` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Broker Futures Commission Rebate Record / 经纪商合约 手续费 返佣 记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].subaccountId | string |  | 例: `1` |
| [].income | string |  | 例: `0.02063898` |
| [].asset | string |  | 例: `USDT` |
| [].symbol | string |  | 例: `ETHUSDT` |
| [].tradeId | integer (int64) |  | 例: `123456` |
| [].time | integer (int64) |  | 例: `1544433328000` |
| [].status | integer (int64) |  | 例: `1` |