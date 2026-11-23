---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-spot-block-matching/api/rest-api
api_type: REST
updated_at: 2026-11-23 18:49:40.604980
---

# Spot Block Matching REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-spot-block-matching/api/rest-api/1.0.0/schema.yaml

Execute off-exchange Spot trades with minimal market impact.

以最小的市场影响执行场外现货交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/block-match/order/cancel` — Order Cancel (TRADE)
- `POST /sapi/v1/block-match/order/extend` — Order Extend (TRADE)
- `POST /sapi/v1/block-match/order/place` — Order Place (TRADE)
- `POST /sapi/v1/block-match/order/take` — Order Take (TRADE)
- `GET /sapi/v1/block-match/order/query-open-order` — Query open order (USER_DATA)
- `GET /sapi/v1/block-match/order/query-order-history` — Query Order History (USER_DATA)
- `POST /sapi/v1/block-match/symbols` — Symbols (USER_DATA)

## Order Cancel (TRADE)（取消订单 (TRADE)）

`POST /sapi/v1/block-match/order/cancel`

Order Cancel

取消订单

Operation ID: `orderCancel`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) | 是 | Order ID<br>订单 ID<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order Cancel / 取消订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Order Extend (TRADE)（延期订单 (TRADE)）

`POST /sapi/v1/block-match/order/extend`

Extend Order Validity Period by Adding 30 Minutes to the Current Time

延期订单

Operation ID: `orderExtend`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) | 是 | Order ID<br>订单 ID<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order Extend / 延期订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Order Place (TRADE)（下单 (TRADE)）

`POST /sapi/v1/block-match/order/place`

Spot block match Place order, The order is valid for 30 minutes and will automatically expire if not executed.

现货区块匹配下单，订单有效期为 30 分钟，如不执行将自动失效。

Operation ID: `orderPlace`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading symbol, for example BTC/USDT.<br>交易对，例如 BTC/USDT。<br>例: `BTC/USDT` |
| side | string | 是 | Order side.<br>订单方向。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| price | number (float) | 是 | Order price.<br>订单价格。<br>例: `100` |
| amount | number (float) | 是 | Order amount.<br>订单数量。<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order Place / 下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `1345055237913600000` |
| settlementKey | string |  | 例: `7fc713a30e1f4835ad5d3aaea150f32b` |

## Order Take (TRADE)（接单（交易） (TRADE)）

`POST /sapi/v1/block-match/order/take`

Accept order, Complete Transaction

接受订单，完成交易

Operation ID: `orderTake`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| settlementKey | string | 是 | Settlement Key<br>结算键<br>例: `7fc713a30e1f4835ad5d3aaea150f32b` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order Take / 接单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | 例: `True` |

## Query open order (USER_DATA)（查询未结订单 (USER_DATA)）

`GET /sapi/v1/block-match/order/query-open-order`

Query User's Open Orders

查询用户的未结订单

Operation ID: `queryOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| page | query | integer (int64) | 是 | Page number.<br>页码。<br>例: `1` |
| rows | query | integer (int64) | 是 | Number of records to query.<br>查询条数。<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：open order / 未结订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `10` |
| rows | object[] |  |  |
| rows[].orderId | string |  | 例: `1345063624407670784` |
| rows[].symbol | string |  | 例: `BNB/USDT` |
| rows[].side | string |  | 例: `Buy` |
| rows[].price | string |  | 例: `600` |
| rows[].amount | string |  | 例: `0.1` |
| rows[].settlementKey | string |  | 例: `d1f921c31667417ca0bcc36a25eb681b` |
| rows[].expireTime | integer (int64) |  | 例: `1740731558000` |
| rows[].status | string |  | 例: `Open` |
| rows[].createTime | integer (int64) |  | 例: `1740729758000` |

## Query Order History (USER_DATA)（查询历史订单 (USER_DATA)）

`GET /sapi/v1/block-match/order/query-order-history`

Query User's Order History

查询用户的订单历史记录

Operation ID: `queryOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1641782889000` |
| page | query | integer (int64) | 是 | Page number.<br>页码。<br>例: `1` |
| rows | query | integer (int64) | 是 | Number of records to query.<br>查询条数。<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order History / 订单历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `10` |
| rows | object[] |  |  |
| rows[].orderId | string |  | 例: `1345073107183755264` |
| rows[].role | string |  | 例: `Maker` |
| rows[].symbol | string |  | 例: `BNB/USDT` |
| rows[].side | string |  | 例: `Buy` |
| rows[].price | string |  | 例: `600` |
| rows[].amount | string |  | 例: `0.1` |
| rows[].fee | string |  | 例: `0` |
| rows[].expireTime | integer (int64) |  | 例: `1740733819000` |
| rows[].status | string |  | 例: `Filled` |
| rows[].createTime | integer (int64) |  | 例: `1740732863000` |

## Symbols (USER_DATA)（查询交易对 (USER_DATA)）

`POST /sapi/v1/block-match/symbols`

Return Trading Symbols Supported by Block Match

返回大宗交易支持的交易对

Operation ID: `symbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Symbols / 交易对