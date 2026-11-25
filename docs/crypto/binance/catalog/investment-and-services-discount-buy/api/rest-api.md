---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-discount-buy/api/rest-api
api_type: REST
updated_at: 2026-11-25 18:49:41.859995
---

# Discount Buy REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-discount-buy/api/rest-api/1.0.0/schema.yaml

Query products, request quotes, and subscribe to Advanced Earn Discount Buy strategies.

查询产品、请求报价，并申购 Advanced Earn 折扣买入策略。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/accumulator/product/list` — Get Discount Buy product list
- `GET /sapi/v1/accumulator/product/sum-holding` — Check Discount Buy accounts (USER_DATA)
- `GET /sapi/v1/accumulator/product/position/list` — Get Discount Buy positions (USER_DATA)
- `POST /sapi/v1/accumulator/product/subscribe` — Subscribe Discount Buy products (USER_DATA)

## Get Discount Buy product list（获得折价买币产品列表）

`GET /sapi/v1/accumulator/product/list`

Get Discount Buy product list

获得折价买币产品列表

Operation ID: `getDiscountBuyProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| targetAsset | query | string |  | Target coin, only non-stablecoins are supported.<br>目标币种，仅支持非稳定币<br>例: `BTC` |
| investAsset | query | string |  | Subscription coin, only stablecoins are supported.<br>申购的币种，仅支持稳定币<br>例: `USDT` |
| pageSize | query | integer (int64) | 是 | Number of records per page<br>每页返回记录数<br>例: `10` |
| pageIndex | query | integer (int64) | 是 | Page index<br>页码<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |

### 响应 200：Get Discount Buy product list / 获取折价买币产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| list | object[] |  |  |
| list[].id | string |  | 例: `741590` |
| list[].investAsset | string |  | 例: `USDT` |
| list[].targetAsset | string |  | 例: `BTC` |
| list[].strikePrice | string |  | 例: `114111` |
| list[].knockoutPrice | string |  | 例: `118000` |
| list[].duration | integer (int64) |  | 例: `4` |
| list[].settleDate | integer (int64) |  | 例: `1709020800000` |
| list[].purchaseDecimal | integer (int64) |  | 例: `2` |
| list[].purchaseEndTime | integer (int64) |  | 例: `1708934400000` |
| list[].canPurchase | boolean |  | Whether the product can be subscribed to currently<br>当前该产品是否可申购<br>例: `True` |
| list[].knockOutApr | string |  | 例: `0.3` |
| list[].orderId | integer (int64) |  | 例: `8257205859` |
| list[].minAmount | string |  | 例: `0.01` |
| list[].maxAmount | string |  | 例: `100000` |
| list[].createTimestamp | integer (int64) |  | 例: `1708560084000` |

## Check Discount Buy accounts (USER_DATA)（查询折价买币产品账户 (USER_DATA)）

`GET /sapi/v1/accumulator/product/sum-holding`

Check Discount Buy accounts

查询折价买币产品账户

Operation ID: `checkDiscountBuyAccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Check Discount Buy accounts / 查询折价买币产品账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAmountInBTC | string |  | Total BTC amount in Discount Buy<br>折价买币中的 BTC 总量<br>例: `0.01067982` |
| totalAmountInUSDT | string |  | Total USDT equivalent amount in Discount Buy<br>折价买币中的 USDT 等值总量<br>例: `77.13289230` |

## Get Discount Buy positions (USER_DATA)（获得折价买币产品持仓状态 (USER_DATA)）

`GET /sapi/v1/accumulator/product/position/list`

Get Discount Buy positions

获得折价买币产品持仓状态

Operation ID: `getDiscountBuyPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| status | query | string |  | `PENDING`: Products are purchasing, will give results later;`PURCHASE_SUCCESS`: purchase<br>successfully;`SETTLED`: Products are finish settling;`PURCHASE_FAIL`: fail to purchase;`REFUNDING`: refund<br>ongoing;`REFUND_SUCCESS`: refund to spot account successfully; `SETTLING`: Products are settling. If don't<br>fill this field, will response all the position status.<br>`PENDING`:产品申购中，将稍后给出结果;`PURCHASE_SUCCESS`:申购成功;`SETTLED`:<br>产品已经结算;`PURCHASE_FAIL`:申购失败;`REFUNDING`:退款中;`REFUND_SUCCESS`:退款成功，资金返回现货账户;<br>`SETTLING`:产品正在结算中，如果不填写该字段，则返回所有持仓信息。<br>枚举: `PENDING`, `PURCHASE_SUCCESS`, `SETTLED`, `PURCHASE_FAIL`, `REFUNDING`, `REFUND_SUCCESS`, `SETTLING`<br>例: `PENDING` |
| pageSize | query | integer (int64) | 是 | Number of records per page<br>每页返回记录数<br>例: `10` |
| pageIndex | query | integer (int64) | 是 | Page index<br>页码<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Discount Buy positions / 获取折价买币持仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| list | object[] |  |  |
| list[].id | string |  | positionId<br>持仓 ID<br>例: `10160533` |
| list[].investAsset | string |  | 例: `USDT` |
| list[].targetAsset | string |  | 例: `BTC` |
| list[].depositAmount | string |  | 例: `100.12` |
| list[].strikePrice | string |  | 例: `114111` |
| list[].knockoutPrice | string |  | 例: `118000` |
| list[].duration | integer (int64) |  | 例: `4` |
| list[].settleDate | integer (int64) |  | 例: `1708416000000` |
| list[].purchaseStatus | string |  | Purchase status.<br>申购状态，<br>枚举: `PENDING`, `PURCHASE_SUCCESS`, `SETTLED`, `PURCHASE_FAIL`, `REFUNDING`, `REFUND_SUCCESS`, `SETTLING`<br>例: `PURCHASE_SUCCESS` |
| list[].knockoutApr | string |  | 例: `0.3` |
| list[].orderId | integer (int64) |  | 例: `7973677530` |

## Subscribe Discount Buy products (USER_DATA)（申购折价买币产品 (USER_DATA)）

`POST /sapi/v1/accumulator/product/subscribe`

Subscribe Discount Buy products

申购折价买币产品

Operation ID: `subscribeDiscountBuyProducts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | integer (int64) | 是 | get id from `/sapi/v1/accumulator/product/list`<br>从 `/sapi/v1/accumulator/product/list` 获得id<br>例: `1` |
| orderId | string | 是 | get orderId from `/sapi/v1/accumulator/product/list`<br>从 `/sapi/v1/accumulator/product/list` 获得orderId<br>例: `1` |
| depositAmount | number (float) | 是 | the amount for subscribing<br>申购金额<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe Discount Buy products / 申购折价买币产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | integer (int64) |  | 例: `10208824` |
| investAsset | string |  | 例: `BTC` |
| targetAsset | string |  | 例: `USDT` |
| depositAmount | string |  | 例: `100.12` |
| duration | integer (int64) |  | 例: `4` |
| strikePrice | string |  | 例: `114111` |
| knockOutPrice | string |  | 例: `118000` |
| settleDate | integer (int64) |  | 例: `1709020800000` |
| purchaseStatus | string |  | Subscription status<br>申购状态<br>枚举: `SUBSCRIBING`, `SUCCEED`, `SETTLED`, `FAILED`, `REFUNDING`, `REFUNDED`, `SETTLING`<br>例: `PURCHASE_SUCCESS` |
| knockOutApr | string |  | 例: `0.3` |
| orderId | integer (int64) |  | 例: `8259117597` |