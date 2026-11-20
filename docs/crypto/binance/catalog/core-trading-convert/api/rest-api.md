---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api
api_type: REST
updated_at: 2026-11-20 18:50:29.658652
---

# Convert REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/1.0.0/schema.yaml

Request quotes and execute cryptocurrency conversions via the Convert REST API.

通过 Convert REST API 请求报价并执行加密货币兑换。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/convert/exchangeInfo` — List All Convert Pairs
- `GET /sapi/v1/convert/assetInfo` — Query order quantity precision per asset (USER_DATA)
- `POST /sapi/v1/convert/acceptQuote` — Accept Quote (TRADE)
- `POST /sapi/v1/convert/limit/cancelOrder` — Cancel limit order (TRADE)
- `GET /sapi/v1/convert/tradeFlow` — Get Convert Trade History (USER_DATA)
- `GET /sapi/v1/convert/orderStatus` — Order status (USER_DATA)
- `POST /sapi/v1/convert/limit/placeOrder` — Place limit order (TRADE)
- `GET /sapi/v1/convert/limit/queryOpenOrders` — Query limit open orders (USER_DATA)
- `POST /sapi/v1/convert/getQuote` — Send Quote Request (TRADE)

## List All Convert Pairs（查询可交易币对信息）

`GET /sapi/v1/convert/exchangeInfo`

Query for all convertible token pairs and the tokens’ respective
upper/lower limits

查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。

Operation ID: `listAllConvertPairs`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromAsset | query | string |  | User spends coin<br>用户售出币种<br>例: `BTC` |
| toAsset | query | string |  | User receives coin<br>用户买入币种<br>例: `USDT` |

### 响应 200：List All Convert Pairs / 查询可交易币对信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].fromAsset | string |  | 例: `BTC` |
| [].toAsset | string |  | 例: `USDT` |
| [].fromAssetMinAmount | string |  | 例: `0.0004` |
| [].fromAssetMaxAmount | string |  | 例: `50` |
| [].toAssetMinAmount | string |  | 例: `20` |
| [].toAssetMaxAmount | string |  | 9E+24 signals that this symbol has a very large upper limit close to infinity<br>9E+24 表示该交易对的最大上限非常大，可视为接近无穷大<br>例: `2500000` |

## Query order quantity precision per asset (USER_DATA)（查询可交易币种精度 (USER_DATA)）

`GET /sapi/v1/convert/assetInfo`

Query for supported asset’s precision information

查询每个可交易币种的精度信息

Operation ID: `queryOrderQuantityPrecisionPerAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：order quantity precision per asset / 查询可交易币种精度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | 例: `BTC` |
| [].fraction | integer (int64) |  | 例: `8` |

## Accept Quote (TRADE)（接受报价 (TRADE)）

`POST /sapi/v1/convert/acceptQuote`

Accept the offered quote by quote ID.

通过 quote ID 来接受报价。

Operation ID: `acceptQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| quoteId | string | 是 | 例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Accept Quote / 接受报价

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `933256278426274426` |
| createTime | integer (int64) |  | 例: `1623381330472` |
| orderStatus | string |  | Order processing status<br>订单处理状态<br>枚举: `PROCESS`, `ACCEPT_SUCCESS`, `SUCCESS`, `FAIL`<br>例: `PROCESS` |

## Cancel limit order (TRADE)（取消闪兑限价单 (TRADE)）

`POST /sapi/v1/convert/limit/cancelOrder`

Enable users to cancel a limit order

用户取消闪兑限价单

Operation ID: `cancelLimitOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) | 是 | The orderId from `placeOrder` api<br>orderId 在 `placeOrder`接口响应中获得<br>例: `1603680255057330400` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel limit order / 取消闪兑限价单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `1603680255057330400` |
| status | string |  | 例: `CANCELED` |

## Get Convert Trade History (USER_DATA)（获取闪兑交易记录 (USER_DATA)）

`GET /sapi/v1/convert/tradeFlow`

Get Convert Trade History

获取闪兑交易记录

Operation ID: `getConvertTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | 例: `1623319461670` |
| endTime | query | integer (int64) | 是 | 例: `1641782889000` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Convert Trade History / 获取闪兑交易记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| list | object[] |  |  |
| list[].quoteId | string |  | 例: `f3b91c525b2644c7bc1e1cd31b6e1aa6` |
| list[].orderId | integer (int64) |  | 例: `940708407462087200` |
| list[].orderStatus | string |  | Order status<br>订单状态<br>例: `SUCCESS` |
| list[].fromAsset | string |  | Source asset<br>闪兑前币种<br>例: `USDT` |
| list[].fromAmount | string |  | Source amount<br>闪兑前金额<br>例: `20` |
| list[].toAsset | string |  | Destination asset<br>闪兑后币种<br>例: `BNB` |
| list[].toAmount | string |  | Destination amount<br>闪兑后金额<br>例: `0.06154036` |
| list[].ratio | string |  | Price ratio<br>价格<br>例: `0.00307702` |
| list[].inverseRatio | string |  | Inverse price ratio<br>反向价格<br>例: `324.99` |
| list[].createTime | integer (int64) |  | 例: `1624248872184` |
| startTime | integer (int64) |  | 例: `1623824139000` |
| endTime | integer (int64) |  | 例: `1626416139000` |
| limit | integer (int64) |  | 例: `100` |
| moreData | boolean |  | 例: `False` |

## Order status (USER_DATA)（查询订单状态 (USER_DATA)）

`GET /sapi/v1/convert/orderStatus`

Query order status by order ID.

通过 order ID 来查询订单状态。

Operation ID: `orderStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string |  | Either orderId or quoteId is required<br>orderId 和quoteId需要填其中一个<br>例: `1` |
| quoteId | query | string |  | Either orderId or quoteId is required<br>orderId 和quoteId需要填其中一个<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order status / 查询订单状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `933256278426274400` |
| orderStatus | string |  | 例: `SUCCESS` |
| fromAsset | string |  | 例: `BTC` |
| fromAmount | string |  | 例: `0.00054414` |
| toAsset | string |  | 例: `USDT` |
| toAmount | string |  | 例: `20` |
| ratio | string |  | 例: `36755` |
| inverseRatio | string |  | 例: `0.00002721` |
| createTime | integer (int64) |  | 例: `1623381330472` |

## Place limit order (TRADE)（创建闪兑限价单 (TRADE)）

`POST /sapi/v1/convert/limit/placeOrder`

Enable users to place a limit order

用户创建闪兑限价单

Operation ID: `placeLimitOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| baseAsset | string | 是 | base asset (use the response `fromIsBase` from `GET /sapi/v1/convert/exchangeInfo` api to check<br>which one is baseAsset )<br>基础资产（可通过 `GET /sapi/v1/convert/exchangeInfo` 接口中的 `fromIsBase` 字段判断）<br>例: `BTC` |
| quoteAsset | string | 是 | quote asset<br>报价资产<br>例: `USDT` |
| limitPrice | number (float) | 是 | Symbol limit price (from baseAsset to quoteAsset)<br>币对限价 (从`baseAsset` 到 `quoteAsset`)<br>例: `1` |
| baseAmount | number (float) |  | Base asset amount. (One of `baseAmount` or `quoteAmount` is required)<br>Base asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)<br>例: `1` |
| quoteAmount | number (float) |  | Quote asset amount. (One of `baseAmount` or `quoteAmount` is required)<br>Quote asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)<br>例: `1` |
| side | string | 是 | `BUY` or `SELL`<br>`BUY` 或者`SELL`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| walletType | string |  | Wallet to use for payment. Supported values: `SPOT`, `FUNDING`, `EARN`.<br>Combined wallets also supported: `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`. Default is `SPOT`.<br>这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，<br>如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。<br>枚举: `SPOT`, `FUNDING`, `EARN`, `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`<br>默认: `SPOT`<br>例: `SPOT` |
| expiredType | string | 是 | Order expiry duration. 1_D, 3_D, 7_D, 30_D (D means day)<br>订单过期时长。1_D, 3_D, 7_D, 30_D (D 指天)<br>枚举: `1_D`, `3_D`, `7_D`, `30_D`<br>例: `1_D` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Place limit order / 创建闪兑限价单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `1603680255057330400` |
| status | string |  | 例: `PROCESS` |

## Query limit open orders (USER_DATA)（查询闪兑限价单 (USER_DATA)）

`GET /sapi/v1/convert/limit/queryOpenOrders`

Query current open limit orders

查询闪兑限价单

Operation ID: `queryLimitOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：limit open orders / 闪兑限价未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| list | object[] |  |  |
| list[].quoteId | string |  | 例: `18sdf87kh9df` |
| list[].orderId | integer (int64) |  | 例: `1150901289839` |
| list[].orderStatus | string |  | 例: `SUCCESS` |
| list[].fromAsset | string |  | 例: `BNB` |
| list[].fromAmount | string |  | 例: `10` |
| list[].toAsset | string |  | 例: `USDT` |
| list[].toAmount | string |  | 例: `2317.89` |
| list[].ratio | string |  | 例: `231.789` |
| list[].inverseRatio | string |  | 例: `0.00431427` |
| list[].createTime | integer (int64) |  | 例: `1614089498000` |
| list[].expiredTimestamp | integer (int64) |  | 例: `1614099498000` |

## Send Quote Request (TRADE)（发送获取报价请求 (TRADE)）

`POST /sapi/v1/convert/getQuote`

Request a quote for the requested token pairs

对所需的币对发送获取报价请求

Operation ID: `sendQuoteRequest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromAsset | string | 是 | 例: `BTC` |
| toAsset | string | 是 | 例: `USDT` |
| fromAmount | number (float) |  | When specified, it is the amount you will be debited after the conversion<br>这是成交后将被扣除的金额<br>例: `1` |
| toAmount | number (float) |  | When specified, it is the amount you will be credited after the conversion<br>这是成交后将会获得的金额<br>例: `1` |
| walletType | string |  | Wallet to use for payment. Supported values: `SPOT`, `FUNDING`, `EARN`.<br>Combined wallets also supported: `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`. Default is `SPOT`.<br>这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，<br>如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。<br>枚举: `SPOT`, `FUNDING`, `EARN`, `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`<br>默认: `SPOT`<br>例: `SPOT` |
| validTime | string |  | Quote valid duration. Supported values: 10s, 30s, 1m. Default is 10s.<br>可以支持10s、30s、1m等值，默认值为 10s<br>枚举: `10s`, `30s`, `1m`<br>默认: `10s`<br>例: `10s` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Send Quote Request / 发送获取报价请求

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| quoteId | string |  | 例: `12415572564` |
| ratio | string |  | 例: `38163.7` |
| inverseRatio | string |  | 例: `0.0000262` |
| validTimestamp | integer (int64) |  | 例: `1623319461670` |
| toAmount | string |  | 例: `3816.37` |
| fromAmount | string |  | 例: `0.1` |