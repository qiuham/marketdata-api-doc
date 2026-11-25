---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-oms/api/rest-api
api_type: REST
updated_at: 2026-11-25 18:49:37.361714
---

# OMS Toolkit REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-oms/api/rest-api/1.0.0/schema.yaml

Place and manage Spot and Futures trades for linked accounts via the Binance Link API.

通过 Binance Link API 为关联账户下达和管理现货及合约交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://fapi.binance.com`

## 接口列表

- `GET /sapi/v1/apiReferral/userCustomization` — Get User’s Customize Id (Spot) (USER_DATA)
- `POST /sapi/v1/apiReferral/userCustomization` — Customize Id For Spot Client (USER_DATA)
- `GET /sapi/v1/apiReferral/customization` — Get Client Email Customized Id (USER_DATA)
- `POST /sapi/v1/apiReferral/customization` — Partner Customize Id For Client (USER_DATA)
- `GET /sapi/v1/apiReferral/ifNewUser` — Query Client If The New User (Spot) (USER_DATA)
- `GET /sapi/v1/apiReferral/kickback/recentRecord` — Query Rebate Recent Record
- `GET /sapi/v1/apiReferral/rebate/recentRecord` — Query Partner Rebate Recent Record
- `GET /papi/v1/apiReferral/userCustomization` — Get User Customize Id (PAPI)
- `POST /papi/v1/apiReferral/userCustomization` — Customize Id For PAPI Client (USER_DATA)
- `GET /fapi/v1/apiReferral/userCustomization` — Get User's Customize Id (Futures) (USER_DATA)
- `POST /fapi/v1/apiReferral/userCustomization` — Customize Id For Futures Client (USER_DATA)
- `GET /fapi/v1/apiReferral/customization` — Get Futures Client Email Customized Id (USER_DATA)
- `POST /fapi/v1/apiReferral/customization` — Partner Customize Id For Futures Client (USER_DATA)
- `GET /fapi/v1/income` — Get Income History (USER_DATA)
- `GET /fapi/v1/apiReferral/overview` — Get Rebate Data Overview (USER_DATA)
- `GET /fapi/v1/apiReferral/rebateVol` — Get Rebate Volume (USER_DATA)
- `GET /fapi/v1/apiReferral/traderSummary` — Get Trader Detail (USER_DATA)
- `GET /fapi/v1/apiReferral/traderNum` — Get Trader Number (USER_DATA)
- `GET /fapi/v1/apiReferral/tradeVol` — Get User Trade Volume (USER_DATA)
- `GET /papi/v1/apiReferral/ifNewUser` — Query PAPI Client New User Status (USER_DATA)
- `GET /fapi/v1/apiReferral/ifNewUser` — Query Futures Client New User Status (USER_DATA)
- `POST /v1/api-key/create` — Create API key for User
- `GET /v1/api-key/user-status` — Get User Status

## Get User’s Customize Id (Spot) (USER_DATA)（查询用户定制 ID（现货） (USER_DATA)）

`GET /sapi/v1/apiReferral/userCustomization`

Get User’s Customize Id (Spot)

查询用户定制 ID（现货）

Operation ID: `getUserSCustomizeId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| apiAgentCode | query | string | 是 | 例: `brokerId` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User’s Customize Id / 获取用户自定义 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string |  | 例: `abc123` |

## Customize Id For Spot Client (USER_DATA)（用户为自己所在的 API Agent 定制 ID（现货） (USER_DATA)）

`POST /sapi/v1/apiReferral/userCustomization`

Customize Id For Spot Client

用户为自己所在的 API Agent 定制 ID（现货）

Operation ID: `customizeIdForSpotClient`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string | 是 | 例: `1` |
| apiAgentCode | string | 是 | API agent code<br>API Agent 标识<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Customize Id For Client / 为用户定制 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string |  | 例: `abc123` |

## Get Client Email Customized Id (USER_DATA)（查询用户邮箱和定制 ID（现货） (USER_DATA)）

`GET /sapi/v1/apiReferral/customization`

Get Client Email Customized Id

查询用户邮箱和定制 ID（Spot）

Operation ID: `getClientEmailCustomizedId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| customerId | query | string |  | 例: `1` |
| email | query | string |  | 例: `test12345@126.com` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Client Email Customized Id / 获取用户邮箱与自定义 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].customerId | string |  | 例: `abc123` |
| [].email | string |  | 例: `test12345@126.com` |

## Partner Customize Id For Client (USER_DATA)（为用户定制 ID（现货，仅支持 brokerId 拥有者） (USER_DATA)）

`POST /sapi/v1/apiReferral/customization`

Partner Customize Id For Client

为用户定制 ID（现货，仅支持 brokerId 持有者）

Operation ID: `partnerCustomizeIdForClient`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string | 是 | 例: `1` |
| email | string | 是 | 例: `test12345@126.com` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Customize Id For Client / 为用户定制 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string |  | 例: `abc123` |
| email | string |  | 例: `test12345@126.com` |

## Query Client If The New User (Spot) (USER_DATA)（查询是否属于新用户 (USER_DATA)）

`GET /sapi/v1/apiReferral/ifNewUser`

Query Client If The New User (Spot)

查询是否属于新用户

Operation ID: `queryClientIfTheNewUser`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| apiAgentCode | query | string | 是 | 例: `brokerId` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Client If The New User / 新用户状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiAgentCode | string |  | 例: `ABCD1234` |
| rebateWorking | boolean |  | 例: `False` |
| ifNewUser | boolean |  | 例: `True` |
| referrerId | integer (int64) |  | 例: `39472261` |

## Query Rebate Recent Record（获取反佣详情历史记录）

`GET /sapi/v1/apiReferral/kickback/recentRecord`

Query Rebate Recent Record

获取反佣详情历史记录

Operation ID: `queryRebateRecentRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Rebate Recent Record / 返佣近期记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].income | string |  | 例: `0.02063898` |
| [].asset | string |  | 例: `BTC` |
| [].symbol | string |  | 例: `ETHBTC` |
| [].time | integer (int64) |  | 例: `1544433328000` |

## Query Partner Rebate Recent Record（获取返佣详情历史记录（合作方））

`GET /sapi/v1/apiReferral/rebate/recentRecord`

Query Partner Rebate Recent Record

获取返佣详情历史记录（合作方）

Operation ID: `queryPartnerRebateRecentRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| customerId | query | string |  | 例: `1` |
| startTime | query | integer (int64) | 是 | 例: `1623319461670` |
| endTime | query | integer (int64) | 是 | 例: `1641782889000` |
| limit | query | integer (int64) | 是 | 例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Rebate Recent Record （USER DATA） / 返佣近期记录（用户数据）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].customerId | string |  | 例: `` |
| [].email | string |  | 例: `om***@***.com` |
| [].income | string |  | 例: `0.00240635` |
| [].asset | string |  | 例: `USDC` |
| [].symbol | string |  | 例: `BNBUSDC` |
| [].time | integer (int64) |  | 例: `1764000370000` |
| [].orderId | integer (int64) |  | 例: `54321678` |
| [].tradeId | integer (int64) |  | 例: `12349876` |
| [].distributeTime | integer (int64) |  | 例: `1764004848000` |
| [].commissionAsset | string |  | 例: `BNB` |
| [].commission | string |  | 例: `0.00000284` |
| [].convertPrice | string |  | 例: `847.30952410` |

## Get User Customize Id (PAPI)（查询用户定制 ID）

`GET /papi/v1/apiReferral/userCustomization`

Get User Customize Id (PAPI)

查询用户定制 Id

Operation ID: `getUserCustomizeId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| brokerId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User’s Customize Id / 获取用户自定义 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| customerId | string |  | 例: `abc123` |

## Customize Id For PAPI Client (USER_DATA)（用户为自己所在的 API Agent 定制 ID（PAPI） (USER_DATA)）

`POST /papi/v1/apiReferral/userCustomization`

Customize Id For PAPI Client

用户为自己所在的 API Agent 定制 ID（PAPI）

Operation ID: `customizeIdForPapiClient`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string | 是 | 例: `1` |
| brokerId | string | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Customize Id For Client / 为用户定制 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| customerId | string |  | 例: `abc123` |

## Get User's Customize Id (Futures) (USER_DATA)（查询用户定制 ID (USER_DATA)）

`GET /fapi/v1/apiReferral/userCustomization`

Get User's Customize Id (Futures)

查询用户定制 Id

Operation ID: `getUsersCustomizeId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| brokerId | query | string | 是 | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User's Customize Id / 获取用户定制 Id

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| customerId | string |  | 例: `abc123` |

## Customize Id For Futures Client (USER_DATA)（用户为自己所在的 API Agent 定制 ID（合约） (USER_DATA)）

`POST /fapi/v1/apiReferral/userCustomization`

Customize Id For Futures Client

用户为自己所在的 API Agent 定制 ID（合约）

Operation ID: `customizeIdForFuturesClient`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string | 是 | 例: `1` |
| brokerId | string | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Customize Id For Client / 为用户定制 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| customerId | string |  | 例: `abc123` |

## Get Futures Client Email Customized Id (USER_DATA)（查询用户邮箱和定制 ID（合约） (USER_DATA)）

`GET /fapi/v1/apiReferral/customization`

Get Futures Client Email Customized Id

查询用户邮箱和定制 ID（Futures）

Operation ID: `getFuturesClientEmailCustomizedId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| customerId | query | string |  | 例: `1` |
| email | query | string |  | 例: `None` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `None` |
| limit | query | integer (int64) |  | 默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Client Email Customized Id / 获取用户邮箱与自定义 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].customerId | string |  | 例: `abc123` |
| [].email | string |  | 例: `test12345@126.com` |

## Partner Customize Id For Futures Client (USER_DATA)（为用户定制 ID（合约，仅支持 brokerId 持有者） (USER_DATA)）

`POST /fapi/v1/apiReferral/customization`

Partner Customize Id For Futures Client

为用户定制 ID（合约，仅支持 brokerId 拥有者）

Operation ID: `partnerCustomizeIdForFuturesClient`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string | 是 | 例: `1` |
| email | string | 是 | 例: `None` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Customize Id For Client / 为用户定制 ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| customerId | string |  | 例: `abc123` |
| email | string |  | 例: `test12345@126.com` |

## Get Income History (USER_DATA)（获取账户损益资金流水 (USER_DATA)）

`GET /fapi/v1/income`

Get Income History

获取账户损益资金流水

Operation ID: `getIncomeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| incomeType | query | string |  | 枚举: `TRANSFER`, `WELCOME_BONUS`, `REALIZED_PNL`, `FUNDING_FEE`, `COMMISSION`, `INSURANCE_CLEAR`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Income History / 获取收益历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].incomeType | string |  | 例: `TRANSFER` |
| [].income | string |  | 例: `-0.37500000` |
| [].asset | string |  | 例: `USDT` |
| [].info | string |  | 例: `` |
| [].time | integer (int64) |  | 例: `1570608000000` |

## Get Rebate Data Overview (USER_DATA)（获取返佣数据总览 (USER_DATA)）

`GET /fapi/v1/apiReferral/overview`

Get Rebate Data Overview

获取返佣数据总览

Operation ID: `getRebateDataOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Rebate Data Overview / 获取返佣数据总览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| newTraderRebateCommission | string |  | 例: `0.30000000` |
| oldTraderRebateCommission | string |  | 例: `0.20000000` |
| totalTradeUser | integer (int64) |  | 例: `13` |
| unit | string |  | 例: `USDT` |
| totalTradeVol | string |  | 例: `405.54379000` |
| totalRebateVol | string |  | 例: `0.01833800` |
| time | integer (int64) |  | 例: `1597708800000` |

## Get Rebate Volume (USER_DATA)（获取每天返佣金额 (USER_DATA)）

`GET /fapi/v1/apiReferral/rebateVol`

Get Rebate Volume

获取每天返佣金额

Operation ID: `getRebateVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Rebate Volume / 获取返佣金额

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].unit | string |  | 例: `USDT` |
| [].rebateVol | string |  | 例: `0.00023200` |
| [].time | integer (int64) |  | 例: `1586736000000` |

## Get Trader Detail (USER_DATA)（获取交易者每天交易明细 (USER_DATA)）

`GET /fapi/v1/apiReferral/traderSummary`

Get Trader Detail

获取交易者每天交易明细

Operation ID: `getTraderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| customerId | query | string |  | 例: `1` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Trader Detail / 获取交易者明细

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].customerId | string |  | 例: `sde001` |
| [].unit | string |  | 例: `USDT` |
| [].tradeVol | string |  | 例: `9.57083000` |
| [].rebateVol | string |  | 例: `0.00035400` |
| [].time | integer (int64) |  | 例: `1586736000000` |

## Get Trader Number (USER_DATA)（获取交易者数量 (USER_DATA)）

`GET /fapi/v1/apiReferral/traderNum`

Get Trader Number

获取交易者数量

Operation ID: `getTraderNumber`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Trader Number / 获取交易者数量

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].newTrader | string |  | 例: `1` |
| [].oldTrader | string |  | 例: `2` |
| [].time | integer (int64) |  | 例: `1586736000000` |

## Get User Trade Volume (USER_DATA)（获取用户每天交易量 (USER_DATA)）

`GET /fapi/v1/apiReferral/tradeVol`

Get User Trade Volume

获取用户每天交易量

Operation ID: `getUserTradeVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User Trade Volume / 获取用户交易量

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].unit | string |  | 例: `USDT` |
| [].tradeVol | string |  | 例: `53.60756000` |
| [].time | integer (int64) |  | 例: `1586736000000` |

## Query PAPI Client New User Status (USER_DATA)（查询是否属于新用户 (USER_DATA)）

`GET /papi/v1/apiReferral/ifNewUser`

Query PAPI Client New User Status

查询是否属于新用户

Operation ID: `queryPapiClientNewUserStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| brokerId | query | string | 是 | 例: `1` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Client If The New User / 新用户状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| rebateWorking | boolean |  | 例: `False` |
| ifNewUser | boolean |  | 例: `True` |

## Query Futures Client New User Status (USER_DATA)（查询是否属于新用户 (USER_DATA)）

`GET /fapi/v1/apiReferral/ifNewUser`

Query Futures Client New User Status

查询是否属于新用户

Operation ID: `queryFuturesClientNewUserStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| brokerId | query | string | 是 | 例: `1` |
| type | query | integer (int64) |  | 1: USDT-margined Futures, 2: Coin-margined Futures<br>1：U本位合约，2：币本位合约<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Client If The New User / 查询是否属于新用户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| brokerId | string |  | 例: `ABCD1234` |
| rebateWorking | boolean |  | 例: `False` |
| ifNewUser | boolean |  | 例: `True` |

## Create API key for User（为用户创建 API Key）

`POST /v1/api-key/create`

Create API key for User

为用户创建 API Key

Operation ID: `createApiKeyForUser`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| Authorization | header | string | 是 | Bearer access token.<br>Bearer 访问令牌。<br>例: `Bearer {access_token}` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiName | string | 是 | custom api name, can be repeated<br>自定义 API 名称，可重复。<br>例: `my-api-name` |
| enableTrade | boolean | 是 | `true` or `false`.<br>`true` 或 `false`。<br>例: `True` |
| enableFutureTrade | boolean | 是 | `true` or `false`.<br>`true` 或 `false`。<br>例: `True` |
| enableMargin | boolean |  | If it's not sent or the user doesn't have Margin account, it will be false by<br>default.<br>若未传入或用户没有杠杆账户，则默认为 false。<br>例: `False` |
| enableEuropeanOptions | boolean |  | If it's not sent or the user doesn't have Options account, it will be false by<br>default.<br>若未传入或用户没有期权账户，则默认为 false。<br>例: `False` |
| status | string |  | `1` or `null` = Access IP unrestricted, `2` = Trusted IPs only, `3` = Trusted Third Party IPs only.<br>If you want to enable any Trade permission(including Spot, Margin or Futures), you must restrict the<br>IP access.<br>`1` 或 `null` 表示不限制访问 IP；`2` 表示仅受信任 IP；`3` 表示仅受信任第三方 IP。若要启用任意交易权限（现货/杠杆/合约），必须限制 IP 访问。<br>例: `1` |
| ipAddress | string |  | Trusted IPs. Can be added in batches, separated by commas. Max 30 for an API key<br>受信任 IP 列表。可批量添加，以逗号分隔。单个 API Key 最多 30 个 IP。<br>例: `54.128.193.28` |
| thirdPartyName | string |  | Third party name must match the name in the server side.<br>第三方名称必须与服务端配置的名称一致。<br>例: `None` |
| publicKey | string | 是 | Your custom public key. The server side will use it to encrypt the apikey, and client decrypts with<br>a private key. Use RSA algorithm, the keysize is customized with client, usually 1024 or 2048<br>([Reference](https://www.devglan.com/online-tools/rsa-encryption-decryption)).<br>自定义公钥。服务端将使用该公钥加密 API Key，客户端使用私钥解密。使用 RSA 算法，密钥长度通常为 1024 或 2048。<br>例: `PUBLIC_KEY` |
| apiKeyPublicKey | string |  | The public key for asymmetrical key type(Ed25519 and RSA). Please see<br>https://www.binance.com/en/support/faq/detail/6b9a63f1e3384cf48a2eedb82767a69a<br>用于非对称密钥类型（Ed25519 和 RSA）的公钥。请参考相关 FAQ 文档。<br>例: `API_KEY_PUBLIC_KEY` |

### 响应 200：Create API key for User / 为用户创建 API Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| data | object |  |  |
| data.apiKey | string |  | 例: `ZN02rGiWOE6*****yjOZg==` |
| data.apiName | string |  | 例: `testoauth1` |
| data.secretKey | string |  | 例: `rH1cO1374UhZXfn2*********3EJjg/JT6gg==` |
| data.enableTrade | boolean |  | 例: `True` |
| data.enableFutureTrade | boolean |  | 例: `True` |
| data.enableMargin | boolean |  | 例: `False` |
| data.enableEuropeanOptions | boolean |  | 例: `True` |
| data.createTime | integer (int64) |  | 例: `1717746281067` |
| success | boolean |  | 例: `True` |

## Get User Status（获取用户状态）

`GET /v1/api-key/user-status`

Get User Status

获取用户状态

Operation ID: `getUserStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| Authorization | header | string | 是 | Bearer access token.<br>Bearer 访问令牌。<br>例: `Bearer {access_token}` |

### 响应 200：Get User Status / 获取用户状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| data | object |  |  |
| data.isExistFutureAccount | boolean |  | 例: `True` |
| success | boolean |  | 例: `True` |