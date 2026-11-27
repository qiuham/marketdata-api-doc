---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api
api_type: REST
updated_at: 2026-11-27 18:48:00.297481
---

# Copy Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api/1.0.0/schema.yaml

Automate lead trading via the Copy Trading API.

通过 Copy Trading API 自动化进行带单交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/copyTrading/futures/userStatus` — Get Futures Lead Trader Status (TRADE)
- `GET /sapi/v1/copyTrading/futures/leadSymbol` — Get Futures Lead Trading Symbol Whitelist (USER_DATA)

## Get Futures Lead Trader Status (TRADE)（查询是否为带单员身份 (TRADE)）

`GET /sapi/v1/copyTrading/futures/userStatus`

Get Futures Lead Trader Status

查询是否为带单员身份

Operation ID: `getFuturesLeadTraderStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Lead Trader Status / 查询是否为带单员身份

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `success` |
| data | object |  |  |
| data.isLeadTrader | boolean |  | Whether the user is a futures lead trader<br>用户是否为合约带单员<br>例: `True` |
| data.time | integer (int64) |  | Server timestamp in milliseconds<br>服务器时间戳（毫秒）<br>例: `1717382310843` |
| success | boolean |  | Whether request is successful<br>请求是否成功<br>例: `True` |

## Get Futures Lead Trading Symbol Whitelist (USER_DATA)（查询带单币种白名单 (USER_DATA)）

`GET /sapi/v1/copyTrading/futures/leadSymbol`

Get Futures Lead Trading Symbol Whitelist

查询带单币种白名单

Operation ID: `getFuturesLeadTradingSymbolWhitelist`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Lead Trading Symbol Whitelist / 查询带单币种白名单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `success` |
| data | object[] |  | Whitelisted symbols for futures lead trading<br>合约带单白名单交易对 |
| data[].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSDT` |
| data[].baseAsset | string |  | Base asset<br>基础资产<br>例: `BTC` |
| data[].quoteAsset | string |  | Quote asset<br>计价资产<br>例: `USDT` |