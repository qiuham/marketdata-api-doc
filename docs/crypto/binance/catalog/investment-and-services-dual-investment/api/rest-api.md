---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-dual-investment/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:23.923124
---

# Dual Investment REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-dual-investment/api/rest-api/1.0.0/schema.yaml

Query products, request quotes, and subscribe to Advanced Earn Dual Investment strategies. The auto-compound setting is no longer managed via API — it must be toggled by the user in the Binance Web UI.

查询产品、请求报价，并申购 Advanced Earn 双币投资策略。自动复投设置已不再支持通过 API 管理，需在 Binance 网页端手动切换。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/dci/product/list` — Get Dual Investment product list
- `GET /sapi/v1/dci/product/accounts` — Check Dual Investment accounts (USER_DATA)
- `GET /sapi/v1/dci/product/positions` — Get Dual Investment positions (USER_DATA)
- `POST /sapi/v1/dci/product/subscribe` — Subscribe Dual Investment products (USER_DATA)

## Get Dual Investment product list（获得双币产品列表）

`GET /sapi/v1/dci/product/list`

Get Dual Investment product list

获得双币产品列表

Operation ID: `getDualInvestmentProductList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| optionType | query | string | 是 | Input CALL or PUT<br>输入CALL 或者 PUT<br>枚举: `CALL`, `PUT`<br>例: `CALL` |
| exercisedCoin | query | string | 是 | Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you should input:<br>`optionType: CALL`, `exercisedCoin: USDT`, `investCoin: BNB`; if you subscribe to a low buy product (put<br>option), you should input: `optionType: PUT`, `exercisedCoin: BNB`, `investCoin: USDT`<br>行权币种，例如：如果您认购高卖产品（看涨期权），您应该输入:`optionType: CALL`,`exercisedCoin: USDT`,`investCoin: BNB`;<br>如果您认购低买产品（看跌期权），您应该输入: `optionType: PUT`,`exercisedCoin: BNB`,`investCoin: USDT`<br>例: `USDT` |
| investCoin | query | string | 是 | Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you should input:<br>`optionType: CALL`, `exercisedCoin: USDT`, `investCoin: BNB`; if you subscribe to a low buy product (put<br>option), you should input: `optionType: PUT`, `exercisedCoin: BNB`, `investCoin: USDT`<br>申购币种，例如：如果您认购高卖产品（看涨期权），您应该输入:`optionType: CALL`,`exercisedCoin: USDT`,`investCoin: BNB`;<br>如果您认购低买产品（看跌期权），您应该输入: `optionType: PUT`,`exercisedCoin: BNB`,`investCoin: USDT`<br>例: `BNB` |
| pageSize | query | integer (int64) |  | Number of records per page<br>每页返回记录数<br>默认: `10`<br>例: `10` |
| pageIndex | query | integer (int64) |  | Page index<br>页码<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |

### 响应 200：Get Dual Investment product list / 获取双币产品列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| list | object[] |  |  |
| list[].id | string |  | 例: `741590` |
| list[].investCoin | string |  | 例: `USDT` |
| list[].exercisedCoin | string |  | 例: `BNB` |
| list[].strikePrice | string |  | 例: `380` |
| list[].duration | integer (int64) |  | 例: `4` |
| list[].settleDate | integer (int64) |  | 例: `1709020800000` |
| list[].purchaseDecimal | integer (int64) |  | 例: `8` |
| list[].purchaseEndTime | integer (int64) |  | 例: `1708934400000` |
| list[].canPurchase | boolean |  | Whether the product can be subscribed to currently<br>当前该产品是否可申购<br>例: `True` |
| list[].apr | string |  | 例: `0.6076` |
| list[].orderId | integer (int64) |  | 例: `8257205859` |
| list[].minAmount | string |  | 例: `0.1` |
| list[].maxAmount | string |  | 例: `25265.7` |
| list[].createTimestamp | integer (int64) |  | 例: `1708560084000` |
| list[].optionType | string |  | 例: `PUT` |
| list[].isAutoCompoundEnable | boolean |  | Whether auto-compound is enabled for this product<br>该产品是否开启自动复投<br>例: `True` |
| list[].autoCompoundPlanList | string[] |  | Available auto-compound plans for this product<br>该产品可选的自动复投计划 |

## Check Dual Investment accounts (USER_DATA)（查询双币产品账户 (USER_DATA)）

`GET /sapi/v1/dci/product/accounts`

Check Dual Investment accounts

查询双币产品账户

Operation ID: `checkDualInvestmentAccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Check Dual Investment accounts / 查询双币产品账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalAmountInBTC | string |  | Total BTC amount in Dual Investment<br>双币投资中的 BTC 总量<br>例: `0.01067982` |
| totalAmountInUSDT | string |  | Total USDT equivalent amount in Dual Investment<br>双币投资中的 USDT 等值总量<br>例: `77.13289230` |

## Get Dual Investment positions (USER_DATA)（获得双币产品持仓状态 (USER_DATA)）

`GET /sapi/v1/dci/product/positions`

Get Dual Investment positions (batch)

获得双币产品持仓状态(批量接口)

Operation ID: `getDualInvestmentPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| status | query | string |  | `PENDING`: Products are purchasing, will give results later; `PURCHASE_SUCCESS`: purchase successfully;<br>`SETTLED`: Products are finish settling; `PURCHASE_FAIL`: fail to purchase; `REFUNDING`: refund ongoing;<br>`REFUND_SUCCESS`: refund to spot account successfully; `SETTLING`: Products are settling. If don't fill this<br>field, will response all the position status.<br>`PENDING`:产品申购中，将稍后给出结果;`PURCHASE_SUCCESS`:申购成功;`SETTLED`:<br>产品已经结算;`PURCHASE_FAIL`:申购失败;`REFUNDING`:退款中;`REFUND_SUCCESS`:退款成功，资金返回现货账户;<br>`SETTLING`:产品正在结算中，如果不填写该字段，则返回所有持仓信息。<br>枚举: `PENDING`, `PURCHASE_SUCCESS`, `SETTLED`, `PURCHASE_FAIL`, `REFUNDING`, `REFUND_SUCCESS`, `SETTLING`<br>例: `PENDING` |
| pageSize | query | integer (int64) |  | Number of records per page<br>每页返回记录数<br>默认: `10`<br>例: `10` |
| pageIndex | query | integer (int64) |  | Page index<br>页码<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Dual Investment positions / 获取双币产品持仓

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| list | object[] |  |  |
| list[].id | string |  | positionId<br>持仓 ID<br>例: `10160533` |
| list[].investCoin | string |  | 例: `USDT` |
| list[].exercisedCoin | string |  | 例: `BNB` |
| list[].subscriptionAmount | string |  | 例: `0.5` |
| list[].strikePrice | string |  | 例: `330` |
| list[].duration | integer (int64) |  | 例: `4` |
| list[].settleDate | integer (int64) |  | 例: `1708416000000` |
| list[].purchaseStatus | string |  | Purchase status. Possible values include PENDING, PURCHASE_SUCCESS, SETTLED,<br>PURCHASE_FAIL, REFUNDING, REFUND_SUCCESS, and SETTLING.<br>申购状态，可选值包括 PENDING、PURCHASE_SUCCESS、SETTLED、PURCHASE_FAIL、REFUNDING、REFUND_SUCCESS、<br>SETTLING。<br>例: `PURCHASE_SUCCESS` |
| list[].apr | string |  | 例: `0.0365` |
| list[].orderId | integer (int64) |  | 例: `7973677530` |
| list[].purchaseEndTime | integer (int64) |  | 例: `1708329600000` |
| list[].optionType | string |  | 例: `PUT` |
| list[].autoCompoundPlan | string |  | NULL, STANDARD, ADVANCED<br>NULL、STANDARD、ADVANCED<br>例: `STANDARD` |
| list[].subscriptionTime | integer (int64) |  | 例: `1708243200000` |

## Subscribe Dual Investment products (USER_DATA)（申购双币产品 (USER_DATA)）

`POST /sapi/v1/dci/product/subscribe`

Subscribe Dual Investment products

申购双币产品

Operation ID: `subscribeDualInvestmentProducts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | get id from `/sapi/v1/dci/product/list`<br>从 `/sapi/v1/dci/product/list` 获得id<br>例: `741590` |
| orderId | string | 是 | get orderId from `/sapi/v1/dci/product/list`<br>从 `/sapi/v1/dci/product/list` 获得orderId<br>例: `8257205859` |
| depositAmount | number (float) | 是 | the amount for subscribing<br>申购金额<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Subscribe Dual Investment products / 申购双币产品

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | integer (int64) |  | 例: `10208824` |
| investCoin | string |  | 例: `BNB` |
| exercisedCoin | string |  | 例: `USDT` |
| subscriptionAmount | string |  | 例: `0.002` |
| duration | integer (int64) |  | 例: `4` |
| autoCompoundPlan | string |  | STANDARD, ADVANCED, this field won't display when autocompound is set to None<br>STANDARD、ADVANCED；当自动复投设为 NONE 时不返回该字段<br>例: `STANDARD` |
| strikePrice | string |  | 例: `380` |
| settleDate | integer (int64) |  | 例: `1709020800000` |
| purchaseStatus | string |  | 例: `PURCHASE_SUCCESS` |
| apr | string |  | 例: `0.7397` |
| orderId | integer (int64) |  | 例: `8259117597` |
| purchaseTime | integer (int64) |  | 例: `1708677583874` |
| optionType | string |  | 例: `CALL` |