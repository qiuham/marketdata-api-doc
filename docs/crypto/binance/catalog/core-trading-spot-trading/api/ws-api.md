---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api
api_type: WebSocket API
updated_at: 2026-11-28 18:46:55.179584
---

# Spot WebSocket API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade on Binance Spot.

访问市场数据、管理账户，并在 Binance 现货市场交易。

版本: 1.0.0

## 服务地址

- `wss://ws-api.binance.com:443/ws-api/v3`
- `wss://demo-ws-api.binance.com:443/ws-api/v3`
- `wss://ws-api.testnet.binance.vision:443/ws-api/v3`

## 接口列表

- `POST /account.commission` — Account Commission Rates (USER_DATA)
- `POST /account.rateLimits.orders` — Unfilled Order Count (USER_DATA)
- `POST /account.status` — Account information (USER_DATA)
- `POST /allOrderLists` — Account order list history (USER_DATA)
- `POST /allOrders` — Account order history (USER_DATA)
- `POST /myAllocations` — Account allocations (USER_DATA)
- `POST /myFilters` — Query Relevant Filters (USER_DATA)
- `POST /myPreventedMatches` — Account prevented matches (USER_DATA)
- `POST /myTrades` — Account trade history (USER_DATA)
- `POST /openOrderLists.status` — Current open Order lists (USER_DATA)
- `POST /openOrders.status` — Current open orders (USER_DATA)
- `POST /order.amendments` — Query Order Amendments (USER_DATA)
- `POST /orderList.status` — Query Order list (USER_DATA)
- `POST /order.status` — Query order (USER_DATA)
- `POST /session.logon` — Log in with API key (USER_DATA)
- `POST /session.logout` — Log out of the session
- `POST /session.status` — Query session status
- `POST /exchangeInfo` — Exchange information
- `POST /executionRules` — Query Execution Rules
- `POST /ping` — Test connectivity
- `POST /time` — Check server time
- `POST /avgPrice` — Current average price
- `POST /depth` — Order book
- `POST /klines` — Klines
- `POST /ticker` — Rolling window price change statistics
- `POST /ticker.24hr` — 24hr ticker price change statistics
- `POST /ticker.book` — Symbol order book ticker
- `POST /ticker.price` — Symbol price ticker
- `POST /ticker.tradingDay` — Trading Day Ticker
- `POST /trades.aggregate` — Aggregate trades
- `POST /trades.historical` — Historical trades
- `POST /blockTrades.historical` — Historical Block Trades
- `POST /trades.recent` — Recent trades
- `POST /uiKlines` — UI Klines
- `POST /referencePrice` — Query Reference Price
- `POST /referencePrice.calculation` — Query Reference Price Calculation
- `POST /openOrders.cancelAll` — Cancel open orders (TRADE)
- `POST /order.amend.keepPriority` — Order Amend Keep Priority (TRADE)
- `POST /order.cancel` — Cancel order (TRADE)
- `POST /order.cancelReplace` — Cancel and replace order (TRADE)
- `POST /orderList.cancel` — Cancel Order list (TRADE)
- `POST /orderList.place` — Place new OCO - Deprecated (TRADE)
- `POST /orderList.place.oco` — Place new Order list - OCO (TRADE)
- `POST /orderList.place.opo` — OPO (TRADE)
- `POST /orderList.place.opoco` — OPOCO (TRADE)
- `POST /orderList.place.oto` — Place new Order list - OTO (TRADE)
- `POST /orderList.place.otoco` — Place new Order list - OTOCO (TRADE)
- `POST /order.place` — Place new order (TRADE)
- `POST /order.test` — Test new order (TRADE)
- `POST /sor.order.place` — Place new order using SOR (TRADE)
- `POST /sor.order.test` — Test new order using SOR (TRADE)
- `POST /session.subscriptions` — Listing all subscriptions
- `POST /userDataStream.subscribe` — Subscribe to User Data Stream (USER_STREAM)
- `POST /userDataStream.subscribe.signature` — Subscribe to User Data Stream through signature subscription (USER_STREAM)
- `POST /userDataStream.unsubscribe` — Unsubscribe from User Data Stream

## Account Commission Rates (USER_DATA)（账户佣金费率 (USER_DATA)）

`POST /account.commission`

Get current account commission rates.

获取当前账户的佣金费率。

Operation ID: `accountCommission`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.commission`<br>例: `account.commission` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "account.commission",
  "params": {
    "symbol": "BNBUSDT",
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account Commission Rates / 账户佣金费率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.standardCommission | object |  | Standard commission rates on trades from the order.<br>订单成交的标准佣金率。 |
| result.standardCommission.maker | string |  | 例: `0.00000010` |
| result.standardCommission.taker | string |  | 例: `0.00000020` |
| result.standardCommission.buyer | string |  | 例: `0.00000030` |
| result.standardCommission.seller | string |  | 例: `0.00000040` |
| result.specialCommission | object |  | Special commission rates from the order.<br>订单成交的特殊佣金率。 |
| result.specialCommission.maker | string |  | 例: `0.01000000` |
| result.specialCommission.taker | string |  | 例: `0.02000000` |
| result.specialCommission.buyer | string |  | 例: `0.03000000` |
| result.specialCommission.seller | string |  | 例: `0.04000000` |
| result.taxCommission | object |  | Tax commission rates on trades from the order.<br>订单成交的税费率。 |
| result.taxCommission.maker | string |  | 例: `0.00000112` |
| result.taxCommission.taker | string |  | 例: `0.00000114` |
| result.taxCommission.buyer | string |  | 例: `0.00000118` |
| result.taxCommission.seller | string |  | 例: `0.00000116` |
| result.discount | object |  | Discount on standard commissions when paying in BNB.<br>使用 BNB 支付时的标准佣金折扣信息。 |
| result.discount.enabledForAccount | boolean |  | 例: `True` |
| result.discount.enabledForSymbol | boolean |  | 例: `True` |
| result.discount.discountAsset | string |  | 例: `BNB` |
| result.discount.discount | string |  | Multiplier applied to the standard commission when paying commission in BNB (e.g. 0.75 = 75% of the standard commission is charged).<br>当用BNB支付佣金时，在标准佣金上按此比率打折。<br>例: `0.75000000` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Unfilled Order Count (USER_DATA)（查询未成交的订单计数 (USER_DATA)）

`POST /account.rateLimits.orders`

Query your current unfilled order count for all intervals.

显示用户在所有时间间隔内的未成交订单计数。

Operation ID: `accountRateLimitsOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.rateLimits.orders`<br>例: `account.rateLimits.orders` |
| params | object | 是 |  |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "account.rateLimits.orders",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Unfilled Order Count / 查询未成交的订单计数

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3783d8d-f8d1-4d2c-b8a0-b7596af5a664` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].rateLimitType | string |  | 例: `ORDERS` |
| result[].interval | string |  | 例: `SECOND` |
| result[].intervalNum | integer (int64) |  | 例: `10` |
| result[].limit | integer (int64) |  | 例: `50` |
| result[].count | integer (int64) |  | 例: `0` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `40` |

## Account information (USER_DATA)（账户信息 (USER_DATA)）

`POST /account.status`

Query information about your account.

获取当前账户信息。

Operation ID: `accountStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.status`<br>例: `account.status` |
| params | object | 是 |  |
| params.omitZeroBalances | boolean |  | When set to `true`, emits only the non-zero balances of an account. Default value: `false`.<br>如果`true`，将隐藏所有零余额。默认值：`false`。<br>默认: `False`<br>例: `False` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "account.status",
  "params": {
    "omitZeroBalances": false,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account information / 账户信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.makerCommission | integer (int64) |  | 例: `15` |
| result.takerCommission | integer (int64) |  | 例: `15` |
| result.buyerCommission | integer (int64) |  | 例: `0` |
| result.sellerCommission | integer (int64) |  | 例: `0` |
| result.canTrade | boolean |  | 例: `True` |
| result.canWithdraw | boolean |  | 例: `True` |
| result.canDeposit | boolean |  | 例: `True` |
| result.commissionRates | object |  |  |
| result.commissionRates.maker | string |  | 例: `0.00150000` |
| result.commissionRates.taker | string |  | 例: `0.00150000` |
| result.commissionRates.buyer | string |  | 例: `0.00000000` |
| result.commissionRates.seller | string |  | 例: `0.00000000` |
| result.brokered | boolean |  | 例: `False` |
| result.requireSelfTradePrevention | boolean |  | 例: `False` |
| result.preventSor | boolean |  | 例: `False` |
| result.updateTime | integer (int64) |  | 例: `1660801833000` |
| result.accountType | string |  | 例: `SPOT` |
| result.balances | object[] |  |  |
| result.balances[].asset | string |  | 例: `BNB` |
| result.balances[].free | string |  | 例: `0.00000000` |
| result.balances[].locked | string |  | 例: `0.00000000` |
| result.permissions | string[] |  |  |
| result.uid | integer (int64) |  | 例: `354937868` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Account order list history (USER_DATA)（账户订单列表历史 (USER_DATA)）

`POST /allOrderLists`

Query information about all your order lists, filtered by time range.

查询所有订单列表的信息，按时间范围过滤。

Operation ID: `allOrderLists`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `allOrderLists`<br>例: `allOrderLists` |
| params | object | 是 |  |
| params.fromId | integer |  | Order list ID to begin at<br>起始的 Order list ID<br>例: `1` |
| params.startTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.endTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.limit | integer |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "allOrderLists",
  "params": {
    "fromId": 1,
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "limit": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account order list history / 账户订单列表历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `8617b7b3-1b3d-4dec-94cd-eefd929b8ceb` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].orderListId | integer (int64) |  | 例: `1274512` |
| result[].contingencyType | string |  | 例: `OCO` |
| result[].listStatusType | string |  | 例: `EXEC_STARTED` |
| result[].listOrderStatus | string |  | 例: `EXECUTING` |
| result[].listClientOrderId | string |  | 例: `08985fedd9ea2cf6b28996` |
| result[].transactionTime | integer (int64) |  | 例: `1660801713793` |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders | object[] |  |  |
| result[].orders[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders[].orderId | integer (int64) |  | 例: `12569138901` |
| result[].orders[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Account order history (USER_DATA)（账户订单历史 (USER_DATA)）

`POST /allOrders`

Query information about all your orders – active, canceled, filled – filtered by time range.

查询所有订单（活动、已撤销、已成交）信息，并按时间范围过滤。

Operation ID: `allOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `allOrders`<br>例: `allOrders` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) |  | Order ID to begin at<br>起始订单ID<br>例: `1` |
| params.startTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.endTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.limit | integer |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "allOrders",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "limit": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account order history / 账户订单历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `734235c2-13d2-4574-be68-723e818c08f3` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].orderListId | integer (int64) |  | Present only for orders that belong to an order list.<br>仅当订单属于订单列表时返回。<br>例: `-1` |
| result[].clientOrderId | string |  | 例: `4d96324ff9d44481926157` |
| result[].price | string |  | 例: `23416.10000000` |
| result[].origQty | string |  | 例: `0.00847000` |
| result[].executedQty | string |  | 例: `0.00847000` |
| result[].cummulativeQuoteQty | string |  | 例: `198.33521500` |
| result[].status | string |  | 例: `FILLED` |
| result[].timeInForce | string |  | 例: `GTC` |
| result[].type | string |  | 例: `LIMIT` |
| result[].side | string |  | 例: `SELL` |
| result[].time | integer (int64) |  | Order placement time.<br>下单时间。<br>例: `1660801715639` |
| result[].updateTime | integer (int64) |  | Time of the last update to the order.<br>订单最后更新时间。<br>例: `1660801717945` |
| result[].isWorking | boolean |  | 例: `True` |
| result[].workingTime | integer (int64) |  | 例: `1660801715639` |
| result[].origQuoteOrderQty | string |  | Always present. Zero if the order type does not use `quoteOrderQty`.<br>始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。<br>例: `0.000000` |
| result[].selfTradePreventionMode | string |  | 例: `NONE` |
| result[].preventedMatchId | integer (int64) |  | Present only if the order expired due to STP.<br>仅当订单因 STP 过期时返回。<br>例: `0` |
| result[].preventedQuantity | string |  | Present only if the order expired due to STP.<br>仅当订单因 STP 过期时返回。<br>例: `1.200000` |
| result[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Account allocations (USER_DATA)（查询分配结果 (USER_DATA)）

`POST /myAllocations`

Retrieves allocations resulting from SOR order placement.

检索由 SOR 订单生成引起的分配结果。

Operation ID: `myAllocations`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `myAllocations`<br>例: `myAllocations` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.startTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.endTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.fromAllocationId | integer |  | Allocation ID to begin at<br>起始分配 ID<br>例: `1` |
| params.limit | integer |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.orderId | integer (int64) |  | Order ID<br>订单 ID<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "myAllocations",
  "params": {
    "symbol": "BNBUSDT",
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "fromAllocationId": 1,
    "limit": 1,
    "orderId": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account allocations / 查询分配结果

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `g4ce6a53-a39d-4f71-823b-4ab5r391d6y8` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].allocationId | integer (int64) |  | 例: `0` |
| result[].allocationType | string |  | 例: `SOR` |
| result[].orderId | integer (int64) |  | 例: `500` |
| result[].orderListId | integer (int64) |  | 例: `-1` |
| result[].price | string |  | 例: `1.00000000` |
| result[].qty | string |  | 例: `0.10000000` |
| result[].quoteQty | string |  | 例: `0.10000000` |
| result[].commission | string |  | 例: `0.00000000` |
| result[].commissionAsset | string |  | 例: `BTC` |
| result[].time | integer (int64) |  | 例: `1687319487614` |
| result[].isBuyer | boolean |  | 例: `False` |
| result[].isMaker | boolean |  | 例: `False` |
| result[].isAllocator | boolean |  | 例: `False` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Query Relevant Filters (USER_DATA)（查询相关过滤器 (USER_DATA)）

`POST /myFilters`

Retrieves the list of [filters](/products/spot/filters) relevant to an account on a given symbol. This is the only method
that shows if an account has [`MAX_ASSET`](/products/spot/filters#max_asset) filters applied to it.

用于检索一个账户上指定交易对的 [filters](/products/spot/filters) 列表。这是唯一一个目前会显示账户是否应用了
[`MAX_ASSET`](/products/spot/filters#max_asset) 过滤器的方法。

Operation ID: `myFilters`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `myFilters`<br>例: `myFilters` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "myFilters",
  "params": {
    "symbol": "BNBUSDT",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Query Relevant Filters / 查询相关过滤器

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `1758009606869` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.exchangeFilters | oneOf[] |  |  |
| result.exchangeFilters[](oneOf 1).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDERS` |
| result.exchangeFilters[](oneOf 1).maxNumOrders | integer (int64) |  | 例: `1000` |
| result.exchangeFilters[](oneOf 2).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ALGO_ORDERS` |
| result.exchangeFilters[](oneOf 2).maxNumAlgoOrders | integer (int64) |  | 例: `200` |
| result.exchangeFilters[](oneOf 3).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` |
| result.exchangeFilters[](oneOf 3).maxNumIcebergOrders | integer (int64) |  | 例: `10` |
| result.exchangeFilters[](oneOf 4).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDER_LISTS` |
| result.exchangeFilters[](oneOf 4).maxNumOrderLists | integer (int64) |  | 例: `20` |
| result.symbolFilters | oneOf[] |  |  |
| result.symbolFilters[](oneOf 1).filterType | string |  | 例: `PRICE_FILTER` |
| result.symbolFilters[](oneOf 1).priceExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 1).minPrice | string |  | 例: `0.00000100` |
| result.symbolFilters[](oneOf 1).maxPrice | string |  | 例: `100000.00000000` |
| result.symbolFilters[](oneOf 1).tickSize | string |  | 例: `0.00000100` |
| result.symbolFilters[](oneOf 2).filterType | string |  | 例: `PERCENT_PRICE` |
| result.symbolFilters[](oneOf 2).multiplierExponent | integer |  | 例: `4` |
| result.symbolFilters[](oneOf 2).multiplierUp | string |  | 例: `1.3000` |
| result.symbolFilters[](oneOf 2).multiplierDown | string |  | 例: `0.7000` |
| result.symbolFilters[](oneOf 2).avgPriceMins | integer |  | 例: `5` |
| result.symbolFilters[](oneOf 3).filterType | string |  | 例: `PERCENT_PRICE_BY_SIDE` |
| result.symbolFilters[](oneOf 3).multiplierExponent | integer |  | 例: `4` |
| result.symbolFilters[](oneOf 3).bidMultiplierUp | string |  | 例: `1.2000` |
| result.symbolFilters[](oneOf 3).bidMultiplierDown | string |  | 例: `0.8000` |
| result.symbolFilters[](oneOf 3).askMultiplierUp | string |  | 例: `1.2000` |
| result.symbolFilters[](oneOf 3).askMultiplierDown | string |  | 例: `0.8000` |
| result.symbolFilters[](oneOf 3).avgPriceMins | integer |  | 例: `5` |
| result.symbolFilters[](oneOf 4).filterType | string |  | 例: `LOT_SIZE` |
| result.symbolFilters[](oneOf 4).qtyExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 4).minQty | string |  | 例: `0.00010000` |
| result.symbolFilters[](oneOf 4).maxQty | string |  | 例: `100000.00000000` |
| result.symbolFilters[](oneOf 4).stepSize | string |  | 例: `0.00010000` |
| result.symbolFilters[](oneOf 5).filterType | string |  | 例: `MIN_NOTIONAL` |
| result.symbolFilters[](oneOf 5).priceExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 5).minNotional | string |  | 例: `10.00000000` |
| result.symbolFilters[](oneOf 5).applyToMarket | boolean |  | 例: `True` |
| result.symbolFilters[](oneOf 5).avgPriceMins | integer |  | 例: `5` |
| result.symbolFilters[](oneOf 6).filterType | string |  | 例: `NOTIONAL` |
| result.symbolFilters[](oneOf 6).priceExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 6).minNotional | string |  | 例: `10.00000000` |
| result.symbolFilters[](oneOf 6).applyMinToMarket | boolean |  | 例: `True` |
| result.symbolFilters[](oneOf 6).maxNotional | string |  | 例: `100000.00000000` |
| result.symbolFilters[](oneOf 6).applyMaxToMarket | boolean |  | 例: `False` |
| result.symbolFilters[](oneOf 6).avgPriceMins | integer |  | 例: `5` |
| result.symbolFilters[](oneOf 7).filterType | string |  | 例: `ICEBERG_PARTS` |
| result.symbolFilters[](oneOf 7).limit | integer (int64) |  | 例: `10` |
| result.symbolFilters[](oneOf 8).filterType | string |  | 例: `MARKET_LOT_SIZE` |
| result.symbolFilters[](oneOf 8).qtyExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 8).minQty | string |  | 例: `0.00000000` |
| result.symbolFilters[](oneOf 8).maxQty | string |  | 例: `1000.00000000` |
| result.symbolFilters[](oneOf 8).stepSize | string |  | 例: `0.00000000` |
| result.symbolFilters[](oneOf 9).filterType | string |  | 例: `MAX_NUM_ORDERS` |
| result.symbolFilters[](oneOf 9).maxNumOrders | integer (int64) |  | 例: `200` |
| result.symbolFilters[](oneOf 10).filterType | string |  | 例: `MAX_NUM_ALGO_ORDERS` |
| result.symbolFilters[](oneOf 10).maxNumAlgoOrders | integer (int64) |  | 例: `10` |
| result.symbolFilters[](oneOf 11).filterType | string |  | 例: `MAX_NUM_ICEBERG_ORDERS` |
| result.symbolFilters[](oneOf 11).maxNumIcebergOrders | integer (int64) |  | 例: `5` |
| result.symbolFilters[](oneOf 12).filterType | string |  | 例: `MAX_POSITION` |
| result.symbolFilters[](oneOf 12).qtyExponent | integer |  | 例: `8` |
| result.symbolFilters[](oneOf 12).maxPosition | string |  | 例: `100.00000000` |
| result.symbolFilters[](oneOf 13).filterType | string |  | 例: `TRAILING_DELTA` |
| result.symbolFilters[](oneOf 13).minTrailingAboveDelta | integer (int64) |  | 例: `10` |
| result.symbolFilters[](oneOf 13).maxTrailingAboveDelta | integer (int64) |  | 例: `2000` |
| result.symbolFilters[](oneOf 13).minTrailingBelowDelta | integer (int64) |  | 例: `10` |
| result.symbolFilters[](oneOf 13).maxTrailingBelowDelta | integer (int64) |  | 例: `2000` |
| result.symbolFilters[](oneOf 14).filterType | string |  | 例: `T_PLUS_SELL` |
| result.symbolFilters[](oneOf 14).endTime | integer (int64) |  | 例: `1741672924895` |
| result.symbolFilters[](oneOf 15).filterType | string |  | 例: `MAX_NUM_ORDER_LISTS` |
| result.symbolFilters[](oneOf 15).maxNumOrderLists | integer (int64) |  | 例: `20` |
| result.symbolFilters[](oneOf 16).filterType | string |  | 例: `MAX_NUM_ORDER_AMENDS` |
| result.symbolFilters[](oneOf 16).maxNumOrderAmends | integer (int64) |  | 例: `10` |
| result.assetFilters | oneOf[] |  |  |
| result.assetFilters[](oneOf 1).filterType | string |  | 例: `MAX_ASSET` |
| result.assetFilters[](oneOf 1).qtyExponent | integer |  | 例: `8` |
| result.assetFilters[](oneOf 1).limit | string |  | 例: `1000000.00000000` |
| result.assetFilters[](oneOf 1).asset | string |  | 例: `JPY` |
| result.rateLimits | object[] |  |  |
| result.rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| result.rateLimits[].interval | string |  | 例: `MINUTE` |
| result.rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| result.rateLimits[].limit | integer (int64) |  | 例: `6000` |
| result.rateLimits[].count | integer (int64) |  | 例: `40` |

## Account prevented matches (USER_DATA)（账户的 Prevented Matches (USER_DATA)）

`POST /myPreventedMatches`

Displays the list of orders that were expired due to STP.

These are the combinations supported:

* `symbol` + `preventedMatchId`
* `symbol` + `orderId`
* `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
* `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

获取因 STP 而过期的订单列表。

这些是支持的组合：

* `symbol` + `preventedMatchId`
* `symbol` + `orderId`
* `symbol` + `orderId` + `fromPreventedMatchId` (`limit`  默认为 500)
* `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

权重: Case                            | Weight
----                            | -----
If `symbol` is invalid          | 2
Querying by `preventedMatchId`  | 2
Querying by `orderId`           | 20

Operation ID: `myPreventedMatches`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `myPreventedMatches`<br>例: `myPreventedMatches` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.preventedMatchId | integer (int64) |  | Prevented match ID<br>例: `1` |
| params.orderId | integer (int64) |  | Order ID<br>订单 ID<br>例: `1` |
| params.fromPreventedMatchId | integer (int64) |  | Prevented match ID to begin at<br>起始 prevented match ID<br>例: `1` |
| params.limit | integer |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "myPreventedMatches",
  "params": {
    "symbol": "BNBUSDT",
    "preventedMatchId": 1,
    "orderId": 1,
    "fromPreventedMatchId": 1,
    "limit": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account prevented matches / 账户的 Prevented Matches

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `g4ce6a53-a39d-4f71-823b-4ab5r391d6y8` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].preventedMatchId | integer (int64) |  | 例: `1` |
| result[].takerOrderId | integer (int64) |  | 例: `5` |
| result[].makerSymbol | string |  | 例: `BTCUSDT` |
| result[].makerOrderId | integer (int64) |  | 例: `3` |
| result[].tradeGroupId | integer (int64) |  | 例: `1` |
| result[].selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| result[].price | string |  | 例: `1.100000` |
| result[].makerPreventedQuantity | string |  | 例: `1.300000` |
| result[].transactTime | integer (int64) |  | 例: `1669101687094` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Account trade history (USER_DATA)（账户成交历史 (USER_DATA)）

`POST /myTrades`

Query information about all your trades, filtered by time range.

获取账户指定交易对的成交历史，按时间范围过滤。

权重: Condition| Weight|
---| ---
|Without orderId|20|
|With orderId|5|

Operation ID: `myTrades`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `myTrades`<br>例: `myTrades` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) |  | This can only be used in combination with `symbol`.<br>必须要和参数`symbol`一起使用。<br>例: `1` |
| params.startTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.endTime | integer (int64) |  | Timestamp in ms<br>毫秒时间戳<br>例: `1735693200000` |
| params.fromId | integer |  | First trade ID to query<br>起始交易 ID<br>例: `1` |
| params.limit | integer |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "myTrades",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "fromId": 1,
    "limit": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account trade history / 账户成交历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `f4ce6a53-a29d-4f70-823b-4ab59391d6e8` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].id | integer (int64) |  | 例: `1650422481` |
| result[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].orderListId | integer (int64) |  | 例: `-1` |
| result[].price | string |  | 例: `23416.10000000` |
| result[].qty | string |  | 例: `0.00635000` |
| result[].quoteQty | string |  | 例: `148.69223500` |
| result[].commission | string |  | 例: `0.00000000` |
| result[].commissionAsset | string |  | 例: `BNB` |
| result[].time | integer (int64) |  | 例: `1660801715793` |
| result[].isBuyer | boolean |  | 例: `False` |
| result[].isMaker | boolean |  | 例: `True` |
| result[].isBestMatch | boolean |  | 例: `True` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Current open Order lists (USER_DATA)（查询订单列表挂单 (USER_DATA)）

`POST /openOrderLists.status`

Query execution status of all open order lists.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

* [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) if on an authenticated session
* [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature) if subscribing through signature subscription

查询所有订单列表挂单的执行状态。

如果您需要持续监控订单状态更新，请考虑使用 WebSocket Streams：

* 如果会话已通过验证，请使用 [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
* 如果通过签名订阅的方式订阅，请使用 [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)

Operation ID: `openOrderListsStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `openOrderLists.status`<br>例: `openOrderLists.status` |
| params | object | 是 |  |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "openOrderLists.status",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Current open Order lists / 查询订单列表挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `3a4437e2-41a3-4c19-897c-9cadc5dce8b6` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].orderListId | integer (int64) |  | 例: `0` |
| result[].contingencyType | string |  | 例: `OCO` |
| result[].listStatusType | string |  | 例: `EXEC_STARTED` |
| result[].listOrderStatus | string |  | 例: `EXECUTING` |
| result[].listClientOrderId | string |  | 例: `08985fedd9ea2cf6b28996` |
| result[].transactionTime | integer (int64) |  | 例: `1660801713793` |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders | object[] |  |  |
| result[].orders[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders[].orderId | integer (int64) |  | 例: `4` |
| result[].orders[].clientOrderId | string |  | 例: `CUhLgTXnX5n2c0gWiLpV4d` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `6` |

## Current open orders (USER_DATA)（当前挂单 (USER_DATA)）

`POST /openOrders.status`

Query execution status of all open orders.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

* [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) if on an authenticated session
* [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature) if subscribing through signature subscription

查询所有挂订单的执行状态。

如果您需要持续监控订单状态更新，请考虑使用 WebSocket Streams：

* 如果会话已通过验证，请使用 [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
* 如果通过签名订阅的方式订阅，请使用 [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)

权重: | Parameter | Weight |
| --------- | ------ |
| `symbol`  |      6 |
| none      |     80 |

Operation ID: `openOrdersStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `openOrders.status`<br>例: `openOrders.status` |
| params | object | 是 |  |
| params.symbol | string |  | If omitted, open orders for all symbols are returned<br>如果省略，则返回所有交易对的挂单<br>例: `BNBUSDT` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "openOrders.status",
  "params": {
    "symbol": "BNBUSDT",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Current open orders / 当前挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `55f07876-4f6f-4c47-87dc-43e5fff3f2e7` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].orderListId | integer (int64) |  | Present only for orders that belong to an order list.<br>仅当订单属于订单列表时返回。<br>例: `-1` |
| result[].clientOrderId | string |  | 例: `4d96324ff9d44481926157` |
| result[].price | string |  | 例: `23416.10000000` |
| result[].origQty | string |  | 例: `0.00847000` |
| result[].executedQty | string |  | 例: `0.00720000` |
| result[].origQuoteOrderQty | string |  | Always present. Zero if the order type does not use `quoteOrderQty`.<br>始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。<br>例: `0.000000` |
| result[].cummulativeQuoteQty | string |  | 例: `172.43931000` |
| result[].status | string |  | 例: `PARTIALLY_FILLED` |
| result[].timeInForce | string |  | 例: `GTC` |
| result[].type | string |  | 例: `LIMIT` |
| result[].side | string |  | 例: `SELL` |
| result[].time | integer (int64) |  | Order placement time.<br>下单时间。<br>例: `1660801715639` |
| result[].updateTime | integer (int64) |  | Time of the last update to the order.<br>订单最后更新时间。<br>例: `1660801717945` |
| result[].isWorking | boolean |  | 例: `True` |
| result[].workingTime | integer (int64) |  | 例: `1660801715639` |
| result[].selfTradePreventionMode | string |  | 例: `NONE` |
| result[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `6` |

## Query Order Amendments (USER_DATA)（查询改单 (USER_DATA)）

`POST /order.amendments`

Queries all amendments of a single order.

查询对一个订单的所有改单操作。

Operation ID: `orderAmendments`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.amendments`<br>例: `order.amendments` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) | 是 | Order ID<br>订单 ID<br>例: `1` |
| params.fromExecutionId | integer (int64) |  | Execution ID to begin at<br>起始执行 ID<br>例: `1` |
| params.limit | integer (int64) |  | Default: 500; Maximum: 1000<br>默认值: 500; 最大值: 1000<br>默认: `500`<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.amendments",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "fromExecutionId": 1,
    "limit": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Query Order Amendments / 查询改单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `6f5ebe91-01d9-43ac-be99-57cf062e0e30` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orderId | integer (int64) |  | 例: `23` |
| result[].executionId | integer (int64) |  | 例: `60` |
| result[].origClientOrderId | string |  | 例: `my_pending_order` |
| result[].newClientOrderId | string |  | 例: `xbxXh5SSwaHS7oUEOCI88B` |
| result[].origQty | string |  | 例: `7.00000000` |
| result[].newQty | string |  | 例: `5.00000000` |
| result[].time | integer (int64) |  | 例: `1741924229819` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `4` |

## Query Order list (USER_DATA)（查询订单列表 (USER_DATA)）

`POST /orderList.status`

Check execution status of an Order list.

For execution status of individual orders, use `order.status`.

检查订单列表的执行状态。

对于单个订单的执行状态，使用 `order.status`。

Operation ID: `orderListStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.status`<br>例: `orderList.status` |
| params | object | 是 |  |
| params.origClientOrderId | string |  | Query order list by `listClientOrderId`. `orderListId` or `origClientOrderId` must be provided.<br>通过 `listClientOrderId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。<br>例: `08985fedd9ea2cf6b28996` |
| params.orderListId | integer |  | Query order list by `orderListId`. `orderListId` or `origClientOrderId` must be provided.<br>通过 `orderListId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。<br>例: `1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.status",
  "params": {
    "origClientOrderId": "08985fedd9ea2cf6b28996",
    "orderListId": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Query Order list / 查询订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `b53fd5ff-82c7-4a04-bd64-5f9dc42c2100` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `1274512` |
| result.contingencyType | string |  | 例: `OCO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `08985fedd9ea2cf6b28996` |
| result.transactionTime | integer (int64) |  | 例: `1660801713793` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `BTCUSDT` |
| result.orders[].orderId | integer (int64) |  | 例: `12569138901` |
| result.orders[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `4` |

## Query order (USER_DATA)（查询订单 (USER_DATA)）

`POST /order.status`

Check execution status of an order.

查询订单状态。

Operation ID: `orderStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.status`<br>例: `order.status` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) |  | Lookup order by `orderId`<br>按 `orderId` 查找订单<br>例: `1` |
| params.origClientOrderId | string |  | Lookup order by `clientOrderId`<br>按 `clientOrderId` 查找订单<br>例: `myOrder1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.status",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "origClientOrderId": "myOrder1",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Query order / 查询订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `aa62318a-5a97-4f3b-bdc7-640bbe33b291` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orderId | integer (int64) |  | 例: `12569099453` |
| result.orderListId | integer (int64) |  | Present only for orders that belong to an order list.<br>仅当订单属于订单列表时返回。<br>例: `-1` |
| result.clientOrderId | string |  | 例: `4d96324ff9d44481926157` |
| result.price | string |  | 例: `23416.10000000` |
| result.origQty | string |  | 例: `0.00847000` |
| result.executedQty | string |  | 例: `0.00847000` |
| result.origQuoteOrderQty | string |  | Always present. Zero if the order type does not use `quoteOrderQty`.<br>始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。<br>例: `0.000000` |
| result.cummulativeQuoteQty | string |  | 例: `198.33521500` |
| result.status | string |  | 例: `FILLED` |
| result.timeInForce | string |  | 例: `GTC` |
| result.type | string |  | 例: `LIMIT` |
| result.side | string |  | 例: `SELL` |
| result.stopPrice | string |  | Always present. Zero if the order type does not use `stopPrice`.<br>始终返回；若订单类型不使用 `stopPrice` 则为 0。<br>例: `0.00000000` |
| result.trailingDelta | integer (int64) |  | Present only if `trailingDelta` was set on the order.<br>仅当订单设置了 `trailingDelta` 时返回。<br>例: `10` |
| result.trailingTime | integer (int64) |  | Present only if `trailingDelta` was set on the order.<br>仅当订单设置了 `trailingDelta` 时返回。<br>例: `-1` |
| result.icebergQty | string |  | Always present. Zero for non-iceberg orders.<br>始终返回；非冰山订单为 0。<br>例: `0.00000000` |
| result.time | integer (int64) |  | Order placement time.<br>下单时间。<br>例: `1660801715639` |
| result.updateTime | integer (int64) |  | Time of the last update to the order.<br>订单最后更新时间。<br>例: `1660801717945` |
| result.isWorking | boolean |  | 例: `True` |
| result.workingTime | integer (int64) |  | 例: `1660801715639` |
| result.strategyId | integer (int64) |  | Present only if `strategyId` was set on the order.<br>仅当订单设置了 `strategyId` 时返回。<br>例: `37463720` |
| result.strategyType | integer (int64) |  | Present only if `strategyType` was set on the order.<br>仅当订单设置了 `strategyType` 时返回。<br>例: `1000000` |
| result.selfTradePreventionMode | string |  | 例: `NONE` |
| result.preventedMatchId | integer (int64) |  | Present only if the order expired due to STP.<br>仅当订单因 STP 过期时返回。<br>例: `0` |
| result.preventedQuantity | string |  | Present only if the order expired due to STP.<br>仅当订单因 STP 过期时返回。<br>例: `1.200000` |
| result.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `4` |

## Log in with API key (USER_DATA)（用API key登录 (USER_DATA)）

`POST /session.logon`

Authenticate WebSocket connection using the provided API key.

After calling `session.logon`, you can omit `apiKey` and `signature` parameters for future requests that require them.

Note that only one API key can be authenticated.

Calling `session.logon` multiple times changes the current authenticated API key.

**Note:** Only Ed25519 keys are supported for this feature.

使用提供的API密钥进行WebSocket连接身份验证。

在调用`session.logon`后，将来的需要`apiKey`和`signature`参数的请求可以省略它们。

请注意，只能认证一个API密钥。
多次调用`session.logon`将更改当前已认证的API密钥。

**注意：** 仅支持 Ed25519 密钥用于此功能。

Operation ID: `sessionLogon`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `session.logon`<br>例: `session.logon` |
| params | object | 是 |  |
| params.recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "session.logon",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Log in with API key / 用API key登录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `c174a2b1-3f51-4580-b200-8528bd237cb7` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.apiKey | string |  | 例: `YOUR_API_KEY` |
| result.authorizedSince | integer (int64) |  | 例: `1649729878532` |
| result.connectedSince | integer (int64) |  | 例: `1649729873021` |
| result.returnRateLimits | boolean |  | 例: `False` |
| result.serverTime | integer (int64) |  | 例: `1649729878630` |
| result.userDataStream | boolean |  | Is User Data Stream subscription active?<br>User Data Stream 订阅是否有效？<br>例: `False` |

## Log out of the session（退出会话）

`POST /session.logout`

Forget the API key previously authenticated. If the connection is not authenticated, this request does nothing.

Note that the WebSocket connection stays open after `session.logout` request. You can continue using the connection, but now you will have to explicitly provide the `apiKey` and `signature` parameters where needed.

忘记之前认证的API密钥。
如果连接未经身份验证，此请求不会有任何作用。

请注意，`session.logout`请求后，WebSocket连接仍然保持打开状态。
你可以继续使用连接，但现在必须在需要的地方明确提供`apiKey`和`signature`参数。

Operation ID: `sessionLogout`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `session.logout`<br>例: `session.logout` |
| params | object |  |  |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "session.logout"
}
```

### 响应 Successful Response：Log out of the session / 退出会话

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `c174a2b1-3f51-4580-b200-8528bd237cb7` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.apiKey | string |  | 例: `None` |
| result.authorizedSince | integer (int64) |  | 例: `None` |
| result.connectedSince | integer (int64) |  | 例: `1649729873021` |
| result.returnRateLimits | boolean |  | 例: `False` |
| result.serverTime | integer (int64) |  | 例: `1649730611671` |
| result.userDataStream | boolean |  | Is User Data Stream subscription active?<br>User Data Stream 订阅是否有效？<br>例: `False` |

## Query session status（查询会话状态）

`POST /session.status`

Query the status of the WebSocket connection,
inspecting which API key (if any) is used to authorize requests.

查询WebSocket连接的状态，检查用于授权请求的API密钥（如果有的话）。

Operation ID: `sessionStatus`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `session.status`<br>例: `session.status` |
| params | object |  |  |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "session.status"
}
```

### 响应 Successful Response：Query session status / 查询会话状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `b50c16cd-62c9-4e29-89e4-37f10111f5bf` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.apiKey | string |  | `null` if the connection is not authenticated.<br>如果连接未经过身份验证，则为 `null`。<br>例: `YOUR_API_KEY` |
| result.authorizedSince | integer (int64) |  | `null` if the connection is not authenticated.<br>如果连接未经过身份验证，则为 `null`。<br>例: `1649729878532` |
| result.connectedSince | integer (int64) |  | 例: `1649729873021` |
| result.returnRateLimits | boolean |  | 例: `False` |
| result.serverTime | integer (int64) |  | 例: `1649730611671` |
| result.userDataStream | boolean |  | Is User Data Stream subscription active?<br>User Data Stream 订阅是否有效？<br>例: `True` |

## Exchange information（交易规范信息）

`POST /exchangeInfo`

Query current exchange trading rules, rate limits, and symbol
information.

获取交易规则，速率限制，和交易对信息。

Operation ID: `exchangeInfo`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `exchangeInfo`<br>例: `exchangeInfo` |
| params | object |  |  |
| params.symbol | string |  | Describe a single symbol<br>描述单个交易对<br>例: `BNBUSDT` |
| params.symbols | string[] |  | Describe multiple symbols<br>描述多个交易对 |
| params.permissions | string[] |  | Filter symbols by permissions<br>按权限过滤交易对 |
| params.showPermissionSets | boolean |  | Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true`.<br>控制 `permissionSets` 字段的内容是否填充。默认为 `true`。<br>默认: `True`<br>例: `True` |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`. Cannot be used in combination with `symbol` or `symbols`.<br>过滤具有此 `tradingStatus` 的交易对。有效值：`TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`。不能与 `symbol` 或 `symbols` 组合使用。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "exchangeInfo",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "permissions": [
      "SPOT"
    ],
    "showPermissionSets": true,
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Exchange information / 交易规范信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `5494febb-d167-46a2-996d-70533eb4d976` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.timezone | string |  | 例: `UTC` |
| result.serverTime | integer (int64) |  | 例: `1655969291181` |
| result.rateLimits | object[] |  | Global rate limits. See "Rate limits" section.<br>全局速率限制。请参阅 "速率限制" 部分。 |
| result.rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| result.rateLimits[].interval | string |  | 例: `MINUTE` |
| result.rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| result.rateLimits[].limit | integer (int64) |  | 例: `6000` |
| result.rateLimits[].count | integer (int64) |  | 例: `40` |
| result.exchangeFilters | oneOf[] |  | Exchange filters are explained on the "Filters" page:<br>/products/spot/filters.md<br>All exchange filters are optional.<br>交易所级别过滤器在 "过滤器" 页面上进行了说明：<br>/products/spot/filters.md<br>全部交易过滤器是可选的。 |
| result.exchangeFilters[](oneOf 1).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDERS` |
| result.exchangeFilters[](oneOf 1).maxNumOrders | integer (int64) |  | 例: `1000` |
| result.exchangeFilters[](oneOf 2).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ALGO_ORDERS` |
| result.exchangeFilters[](oneOf 2).maxNumAlgoOrders | integer (int64) |  | 例: `200` |
| result.exchangeFilters[](oneOf 3).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` |
| result.exchangeFilters[](oneOf 3).maxNumIcebergOrders | integer (int64) |  | 例: `10` |
| result.exchangeFilters[](oneOf 4).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDER_LISTS` |
| result.exchangeFilters[](oneOf 4).maxNumOrderLists | integer (int64) |  | 例: `20` |
| result.symbols | object[] |  |  |
| result.symbols[].symbol | string |  | 例: `BNBBTC` |
| result.symbols[].status | string |  | 例: `TRADING` |
| result.symbols[].baseAsset | string |  | 例: `BNB` |
| result.symbols[].baseAssetPrecision | integer (int64) |  | 例: `8` |
| result.symbols[].quoteAsset | string |  | 例: `BTC` |
| result.symbols[].quotePrecision | integer (int64) |  | 例: `8` |
| result.symbols[].quoteAssetPrecision | integer (int64) |  | 例: `8` |
| result.symbols[].baseCommissionPrecision | integer (int64) |  | 例: `8` |
| result.symbols[].quoteCommissionPrecision | integer (int64) |  | 例: `8` |
| result.symbols[].orderTypes | string[] |  |  |
| result.symbols[].icebergAllowed | boolean |  | 例: `True` |
| result.symbols[].ocoAllowed | boolean |  | 例: `True` |
| result.symbols[].otoAllowed | boolean |  | 例: `True` |
| result.symbols[].opoAllowed | boolean |  | 例: `True` |
| result.symbols[].quoteOrderQtyMarketAllowed | boolean |  | 例: `True` |
| result.symbols[].allowTrailingStop | boolean |  | 例: `True` |
| result.symbols[].cancelReplaceAllowed | boolean |  | 例: `True` |
| result.symbols[].amendAllowed | boolean |  | 例: `False` |
| result.symbols[].pegInstructionsAllowed | boolean |  | 例: `True` |
| result.symbols[].marketQuoteNotionalLimitAllowed | boolean |  | 例: `True` |
| result.symbols[].limitQuoteNotionalLimitAllowed | boolean |  | 例: `True` |
| result.symbols[].isSpotTradingAllowed | boolean |  | 例: `True` |
| result.symbols[].isMarginTradingAllowed | boolean |  | 例: `True` |
| result.symbols[].filters | oneOf[] |  | Symbol filters are explained on the "Filters" page:<br>/products/spot/filters.md<br>All symbol filters are optional.<br>交易对过滤器在"过滤器"页面上进行了说明：<br>/products/spot/filters.md<br>全部交易对过滤器是可选的。 |
| result.symbols[].filters[](oneOf 1).filterType | string |  | 例: `PRICE_FILTER` |
| result.symbols[].filters[](oneOf 1).priceExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 1).minPrice | string |  | 例: `0.00000100` |
| result.symbols[].filters[](oneOf 1).maxPrice | string |  | 例: `100000.00000000` |
| result.symbols[].filters[](oneOf 1).tickSize | string |  | 例: `0.00000100` |
| result.symbols[].filters[](oneOf 2).filterType | string |  | 例: `PERCENT_PRICE` |
| result.symbols[].filters[](oneOf 2).multiplierExponent | integer |  | 例: `4` |
| result.symbols[].filters[](oneOf 2).multiplierUp | string |  | 例: `1.3000` |
| result.symbols[].filters[](oneOf 2).multiplierDown | string |  | 例: `0.7000` |
| result.symbols[].filters[](oneOf 2).avgPriceMins | integer |  | 例: `5` |
| result.symbols[].filters[](oneOf 3).filterType | string |  | 例: `PERCENT_PRICE_BY_SIDE` |
| result.symbols[].filters[](oneOf 3).multiplierExponent | integer |  | 例: `4` |
| result.symbols[].filters[](oneOf 3).bidMultiplierUp | string |  | 例: `1.2000` |
| result.symbols[].filters[](oneOf 3).bidMultiplierDown | string |  | 例: `0.8000` |
| result.symbols[].filters[](oneOf 3).askMultiplierUp | string |  | 例: `1.2000` |
| result.symbols[].filters[](oneOf 3).askMultiplierDown | string |  | 例: `0.8000` |
| result.symbols[].filters[](oneOf 3).avgPriceMins | integer |  | 例: `5` |
| result.symbols[].filters[](oneOf 4).filterType | string |  | 例: `LOT_SIZE` |
| result.symbols[].filters[](oneOf 4).qtyExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 4).minQty | string |  | 例: `0.00010000` |
| result.symbols[].filters[](oneOf 4).maxQty | string |  | 例: `100000.00000000` |
| result.symbols[].filters[](oneOf 4).stepSize | string |  | 例: `0.00010000` |
| result.symbols[].filters[](oneOf 5).filterType | string |  | 例: `MIN_NOTIONAL` |
| result.symbols[].filters[](oneOf 5).priceExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 5).minNotional | string |  | 例: `10.00000000` |
| result.symbols[].filters[](oneOf 5).applyToMarket | boolean |  | 例: `True` |
| result.symbols[].filters[](oneOf 5).avgPriceMins | integer |  | 例: `5` |
| result.symbols[].filters[](oneOf 6).filterType | string |  | 例: `NOTIONAL` |
| result.symbols[].filters[](oneOf 6).priceExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 6).minNotional | string |  | 例: `10.00000000` |
| result.symbols[].filters[](oneOf 6).applyMinToMarket | boolean |  | 例: `True` |
| result.symbols[].filters[](oneOf 6).maxNotional | string |  | 例: `100000.00000000` |
| result.symbols[].filters[](oneOf 6).applyMaxToMarket | boolean |  | 例: `False` |
| result.symbols[].filters[](oneOf 6).avgPriceMins | integer |  | 例: `5` |
| result.symbols[].filters[](oneOf 7).filterType | string |  | 例: `ICEBERG_PARTS` |
| result.symbols[].filters[](oneOf 7).limit | integer (int64) |  | 例: `10` |
| result.symbols[].filters[](oneOf 8).filterType | string |  | 例: `MARKET_LOT_SIZE` |
| result.symbols[].filters[](oneOf 8).qtyExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 8).minQty | string |  | 例: `0.00000000` |
| result.symbols[].filters[](oneOf 8).maxQty | string |  | 例: `1000.00000000` |
| result.symbols[].filters[](oneOf 8).stepSize | string |  | 例: `0.00000000` |
| result.symbols[].filters[](oneOf 9).filterType | string |  | 例: `MAX_NUM_ORDERS` |
| result.symbols[].filters[](oneOf 9).maxNumOrders | integer (int64) |  | 例: `200` |
| result.symbols[].filters[](oneOf 10).filterType | string |  | 例: `MAX_NUM_ALGO_ORDERS` |
| result.symbols[].filters[](oneOf 10).maxNumAlgoOrders | integer (int64) |  | 例: `10` |
| result.symbols[].filters[](oneOf 11).filterType | string |  | 例: `MAX_NUM_ICEBERG_ORDERS` |
| result.symbols[].filters[](oneOf 11).maxNumIcebergOrders | integer (int64) |  | 例: `5` |
| result.symbols[].filters[](oneOf 12).filterType | string |  | 例: `MAX_POSITION` |
| result.symbols[].filters[](oneOf 12).qtyExponent | integer |  | 例: `8` |
| result.symbols[].filters[](oneOf 12).maxPosition | string |  | 例: `100.00000000` |
| result.symbols[].filters[](oneOf 13).filterType | string |  | 例: `TRAILING_DELTA` |
| result.symbols[].filters[](oneOf 13).minTrailingAboveDelta | integer (int64) |  | 例: `10` |
| result.symbols[].filters[](oneOf 13).maxTrailingAboveDelta | integer (int64) |  | 例: `2000` |
| result.symbols[].filters[](oneOf 13).minTrailingBelowDelta | integer (int64) |  | 例: `10` |
| result.symbols[].filters[](oneOf 13).maxTrailingBelowDelta | integer (int64) |  | 例: `2000` |
| result.symbols[].filters[](oneOf 14).filterType | string |  | 例: `T_PLUS_SELL` |
| result.symbols[].filters[](oneOf 14).endTime | integer (int64) |  | 例: `1741672924895` |
| result.symbols[].filters[](oneOf 15).filterType | string |  | 例: `MAX_NUM_ORDER_LISTS` |
| result.symbols[].filters[](oneOf 15).maxNumOrderLists | integer (int64) |  | 例: `20` |
| result.symbols[].filters[](oneOf 16).filterType | string |  | 例: `MAX_NUM_ORDER_AMENDS` |
| result.symbols[].filters[](oneOf 16).maxNumOrderAmends | integer (int64) |  | 例: `10` |
| result.symbols[].permissions | string[] |  |  |
| result.symbols[].permissionSets | string[][] |  |  |
| result.symbols[].defaultSelfTradePreventionMode | string |  | 例: `NONE` |
| result.symbols[].allowedSelfTradePreventionModes | string[] |  |  |
| result.sors | object[] |  | Optional field. Present only when SOR is available.<br>/products/spot/faqs/sor_faq.md<br>可选字段，仅当 SOR 可用时才会被显示出来。<br>/products/spot/faqs/sor_faq.md |
| result.sors[].baseAsset | string |  | 例: `BTC` |
| result.sors[].symbols | string[] |  |  |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Query Execution Rules（查询执行规则）

`POST /executionRules`

Query execution rules for symbols.

查询交易对的执行规则。

权重: Parameter | Weight
--- | ---
`symbol` | 2
`symbols` | 2 for each `symbol`, capped at a max of 40
`symbolStatus` | 40
None | 40

Operation ID: `executionRules`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `executionRules`<br>例: `executionRules` |
| params | object |  |  |
| params.symbol | string |  | Query for specified symbol.<br>查询指定的交易对。<br>例: `BAZUSD` |
| params.symbols | string[] |  | Query for multiple symbols.<br>查询多个交易对。 |
| params.symbolStatus | string |  | Query for all symbols with the specified status. Supported values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>查询指定状态的所有交易对。支持的值：`TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "executionRules",
  "params": {
    "symbol": "BAZUSD",
    "symbols": [
      "BAZUSD"
    ],
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Query Execution Rules / 查询执行规则

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `5162affb-0aba-4821-b475-f2625006eb43` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.symbolRules | object[] |  |  |
| result.symbolRules[].symbol | string |  | 例: `BAZUSD` |
| result.symbolRules[].rules | object[] |  |  |
| result.symbolRules[].rules[].ruleType | string |  | 例: `PRICE_RANGE` |
| result.symbolRules[].rules[].bidLimitMultUp | string |  | 例: `1.0001` |
| result.symbolRules[].rules[].bidLimitMultDown | string |  | 例: `0.9999` |
| result.symbolRules[].rules[].askLimitMultUp | string |  | 例: `1.0001` |
| result.symbolRules[].rules[].askLimitMultDown | string |  | 例: `0.9999` |

## Test connectivity（测试连通性）

`POST /ping`

Test connectivity to the WebSocket API.

Note: You can use regular WebSocket ping frames to test connectivity as well, WebSocket API will respond with pong frames as soon as possible. ping request along with time is a safe way to test request-response handling in your application.

测试能否联通 WebSocket API。

**注意:**

您也可以使用常规 WebSocket ping 帧来测试连通性，
WebSocket API 将尽快以 pong 帧响应。
`ping` 请求和 `time` 是在应用程序中测试请求-响应处理的安全方法。

Operation ID: `ping`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ping`<br>例: `ping` |
| params | object |  |  |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ping"
}
```

### 响应 Successful Response：Test connectivity / 测试连通性

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `922bcc6e-9de8-440d-9e84-7c80933a8d0d` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Check server time（检查服务器时间）

`POST /time`

Test connectivity to the WebSocket API and get the current server time.

测试与 WebSocket API 的连通性并获取当前服务器时间。

Operation ID: `time`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `time`<br>例: `time` |
| params | object |  |  |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "time"
}
```

### 响应 Successful Response：Check server time / 检查服务器时间

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `187d3cb2-942d-484c-8271-4e2141bbadb1` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.serverTime | integer (int64) |  | 例: `1656400526260` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Current average price（当前平均价格）

`POST /avgPrice`

Get current average price for a symbol.

获取交易对的当前平均价格

Operation ID: `avgPrice`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `avgPrice`<br>例: `avgPrice` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "avgPrice",
  "params": {
    "symbol": "BNBUSDT"
  }
}
```

### 响应 Successful Response：Current average price / 当前平均价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `ddbfb65f-9ebf-42ec-8240-8f0f91de0867` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.mins | integer (int64) |  | Average price interval (in minutes)<br>平均价格间隔（以分钟为单位）<br>例: `5` |
| result.price | string |  | Average price<br>平均价格<br>例: `0.01378135` |
| result.closeTime | integer (int64) |  | Last trade time<br>最近成交时间<br>例: `1694061154503` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Order book（订单簿深度信息）

`POST /depth`

Get current order book.

Note that this request returns limited market depth.

If you need to continuously monitor order book updates, please consider using WebSocket Streams:
  * `<symbol>@depth<levels>`
  * `<symbol>@depth`

You can use `depth` request together with `<symbol>@depth` streams to [maintain a local order book](/products/spot/web-socket-streams#how-to-manage-a-local-order-book-correctly).

获取当前深度信息。

请注意，此请求返回有限的市场深度。

如果需要持续监控深度信息更新，请考虑使用 WebSocket Streams：
  * `<symbol>@depth<levels>`
  * `<symbol>@depth`

如果需要[维护本地orderbook](/products/spot/web-socket-streams#how-to-maintain-orderbook)，您可以将 `depth` 请求与 `<symbol>@depth` streams 一起使用。

权重: Adjusted based on the limit:

|Limit|Request Weight
------|-------
1-100|  5
101-500| 25
501-1000| 50
1001-5000| 250
5001-7500| 500

Operation ID: `depth`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `depth`<br>例: `depth` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.limit | integer |  | If limit > 7500, only 7500 entries will be returned.<br>如果 limit > 7500, 最多返回7500条数据。<br>默认: `100`<br>例: `1` |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`.<br>A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br>过滤具有此 `tradingStatus` 的交易对。<br>如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "depth",
  "params": {
    "symbol": "BNBUSDT",
    "limit": 1,
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Order book / 订单簿深度信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `51e2affb-0aba-4821-ba75-f2625006eb43` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.lastUpdateId | integer (int64) |  | 例: `2731179239` |
| result.bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量] |
| result.asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量] |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Klines（K线数据）

`POST /klines`

Get klines (candlestick bars).

Klines are uniquely identified by their open & close time.

If you need access to real-time kline updates, please consider using WebSocket Streams:
  * `<symbol>@kline_<interval>`

If you need historical kline data, please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#klines).

获取K线数据。

Klines 由其开盘时间和收盘时间为唯一标识。

如果您需要访问实时 kline 更新，请考虑使用 WebSocket Streams：
  * `<symbol>@kline_<interval>`

如果需要历史K线数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/#klines)。

Operation ID: `klines`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `klines`<br>例: `klines` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.interval | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |
| params.startTime | integer (int64) |  | 例: `1735693200000` |
| params.endTime | integer (int64) |  | 例: `1735693200000` |
| params.timeZone | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>例: `0` |
| params.limit | integer |  | 默认: `500`<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "klines",
  "params": {
    "symbol": "BNBUSDT",
    "interval": "1s",
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "timeZone": "0",
    "limit": 1
  }
}
```

### 响应 Successful Response：Klines / K线数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b` |
| status | integer (int64) |  | 例: `200` |
| result | oneOf[][] |  |  |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Rolling window price change statistics（滚动窗口价格变动统计）

`POST /ticker`

Get rolling window price change statistics with a custom window.

This request is similar to [`ticker.24hr`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker-24hr) but statistics are computed on demand using the arbitrary window you specify.

**Note:** Window size precision is limited to 1 minute.
While the `closeTime` is the current time of the request, `openTime` always start on a minute boundary.
As such, the effective window might be up to 59999 ms wider than the requested `windowSize`.

<details>
<summary>Window computation example</summary>

For example, a request for `"windowSize": "7d"` might result in the following window:

```javascript
{
    "openTime": 1659580020000,
    "closeTime": 1660184865291
}
```

Time of the request – `closeTime` – is 1660184865291 (August 11, 2022 02:27:45.291).
Requested window size should put the `openTime` 7 days before that – August 4, 02:27:45.291 –
but due to limited precision it ends up a bit earlier: 1659580020000 (August 4, 2022 02:27:00),
exactly at the start of a minute.
</details>

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:
  * `<symbol>@ticker_<window_size>` or `!ticker_<window-size>@arr`

使用自定义窗口获取滚动窗口价格变化统计信息。

这个请求类似于 [`ticker.24hr`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker-24hr)，但统计数据是使用指定的任意窗口按需计算的。

**注意：** 窗口大小精度限制为1分钟。
虽然 `closeTime` 是请求的当前时间，`openTime` 总是从分钟边界开始。
因此，有效窗口可能比请求的 `windowSize` 宽59999毫秒。

<details>
<summary>窗口计算示例</summary>

例如，对 `"windowSize": "7d"` 的请求可能会导致以下窗口：

```javascript
{
    "openTime": 1659580020000,
    "closeTime": 1660184865291
}
```

请求的时间 - `closeTime` - 是 1660184865291（2022年8月11日 02:27:45.291）。
请求的窗口大小应将 `openTime` 设置为7天之前 – 8月4日，02:27:45.291 – 但由于精度有限，它最终会提前一点：1659580020000（2022年8月4日 02:27:00），正好在一分钟开始。
</details>

如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:
  * `<symbol>@ticker_<window_size>` 或者 `!ticker_<window-size>@arr`

权重: Adjusted based on the number of requested symbols:

| Symbols | Weight |
|:-------:|:------:|
|    1–50 | 4 per symbol |
|  51–100 |    200 |

Operation ID: `ticker`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker`<br>例: `ticker` |
| params | object |  |  |
| params.symbol | string |  | Query ticker of a single symbol<br>获取单个交易对的ticker<br>例: `BNBUSDT` |
| params.symbols | string[] |  | Query ticker for multiple symbols<br>获取多个交易对的ticker |
| params.type | string |  | Ticker type. Supported values: FULL (default) or MINI<br>Ticker 类型: FULL (默认) 或者 MINI<br>枚举: `FULL`, `MINI`<br>例: `FULL` |
| params.windowSize | string |  | Defaults to 1d if no parameter provided.<br>默认为 1d<br>枚举: `1m`, `2m`, `3m`, `4m`, `5m`, `6m`, `7m`, `8m`, `9m`, `10m`, `11m`, `12m`, `13m`, `14m`, `15m`, `16m`, `17m`, `18m`, `19m`, `20m`, `21m`, `22m`, `23m`, `24m`, `25m`, `26m`, `27m`, `28m`, `29m`, `30m`, `31m`, `32m`, `33m`, `34m`, `35m`, `36m`, `37m`, `38m`, `39m`, `40m`, `41m`, `42m`, `43m`, `44m`, `45m`, `46m`, `47m`, `48m`, `49m`, `50m`, `51m`, `52m`, `53m`, `54m`, `55m`, `56m`, `57m`, `58m`, `59m`, `1h`, `2h`, `3h`, `4h`, `5h`, `6h`, `7h`, `8h`, `9h`, `10h`, `11h`, `12h`, `13h`, `14h`, `15h`, `16h`, `17h`, `18h`, `19h`, `20h`, `21h`, `22h`, `23h`, `1d`, `2d`, `3d`, `4d`, `5d`, `6d`, `7d`<br>例: `1d` |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ticker",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "type": "FULL",
    "windowSize": "1d",
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Rolling window price change statistics / 滚动窗口价格变动统计

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `bdb7c503-542c-495c-b797-4d2ee2e91173` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BNBBTC` |
| (oneOf 1).result.priceChange | string |  | Absolute price change<br>价格变化<br>例: `0.00061500` |
| (oneOf 1).result.priceChangePercent | string |  | Relative price change in percent<br>价格变化百分比<br>例: `4.735` |
| (oneOf 1).result.weightedAvgPrice | string |  | QuoteVolume / Volume<br>QuoteVolume / 成交量<br>例: `0.01368242` |
| (oneOf 1).result.openPrice | string |  | 例: `0.01298900` |
| (oneOf 1).result.highPrice | string |  | 例: `0.01418800` |
| (oneOf 1).result.lowPrice | string |  | 例: `0.01296000` |
| (oneOf 1).result.lastPrice | string |  | 例: `0.01360400` |
| (oneOf 1).result.volume | string |  | 例: `587179.23900000` |
| (oneOf 1).result.quoteVolume | string |  | Sum of (price * volume) for all trades<br>此k线内所有交易的price(价格) x volume(交易量)的总和<br>例: `8034.03382165` |
| (oneOf 1).result.openTime | integer (int64) |  | Open time for ticker window<br>ticker的开始时间<br>例: `1659580020000` |
| (oneOf 1).result.closeTime | integer (int64) |  | Close time for ticker window<br>ticker的结束时间<br>例: `1660184865291` |
| (oneOf 1).result.firstId | integer (int64) |  | Trade IDs<br>统计时间内的第一笔trade id<br>例: `192977765` |
| (oneOf 1).result.lastId | integer (int64) |  | 例: `195365758` |
| (oneOf 1).result.count | integer (int64) |  | Number of trades in the interval<br>统计时间内交易笔数<br>例: `2387994` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `4` |
| (oneOf 2).id | string |  | 例: `bdb7c503-542c-495c-b797-4d2ee2e91173` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | 例: `BNBBTC` |
| (oneOf 2).result.openPrice | string |  | 例: `0.01298900` |
| (oneOf 2).result.highPrice | string |  | 例: `0.01418800` |
| (oneOf 2).result.lowPrice | string |  | 例: `0.01296000` |
| (oneOf 2).result.lastPrice | string |  | 例: `0.01360400` |
| (oneOf 2).result.volume | string |  | 例: `587179.23900000` |
| (oneOf 2).result.quoteVolume | string |  | Sum of (price * volume) for all trades<br>此k线内所有交易的price(价格) x volume(交易量)的总和<br>例: `8034.03382165` |
| (oneOf 2).result.openTime | integer (int64) |  | Open time for ticker window<br>ticker的开始时间<br>例: `1659580020000` |
| (oneOf 2).result.closeTime | integer (int64) |  | Close time for ticker window<br>ticker的结束时间<br>例: `1660184865291` |
| (oneOf 2).result.firstId | integer (int64) |  | First trade ID<br>第一个交易 ID<br>例: `192977765` |
| (oneOf 2).result.lastId | integer (int64) |  | Last trade ID<br>最后交易 ID<br>例: `195365758` |
| (oneOf 2).result.count | integer (int64) |  | Number of trades<br>成交笔数<br>例: `2387994` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | Number of trades<br>成交笔数<br>例: `4` |
| (oneOf 3).id | string |  | 例: `f4b3b507-c8f2-442a-81a6-b2f12daa030f` |
| (oneOf 3).status | integer (int64) |  | 例: `200` |
| (oneOf 3).result | object[] |  |  |
| (oneOf 3).result[].symbol | string |  | 例: `BNBBTC` |
| (oneOf 3).result[].priceChange | string |  | Absolute price change<br>价格变化<br>例: `0.00061500` |
| (oneOf 3).result[].priceChangePercent | string |  | Relative price change in percent<br>价格变化百分比<br>例: `4.735` |
| (oneOf 3).result[].weightedAvgPrice | string |  | QuoteVolume / Volume<br>QuoteVolume / 成交量<br>例: `0.01368242` |
| (oneOf 3).result[].openPrice | string |  | 例: `0.01298900` |
| (oneOf 3).result[].highPrice | string |  | 例: `0.01418800` |
| (oneOf 3).result[].lowPrice | string |  | 例: `0.01296000` |
| (oneOf 3).result[].lastPrice | string |  | 例: `0.01360400` |
| (oneOf 3).result[].volume | string |  | 例: `587169.48600000` |
| (oneOf 3).result[].quoteVolume | string |  | Sum of (price * volume) for all trades<br>此k线内所有交易的price(价格) x volume(交易量)的总和<br>例: `8033.90114517` |
| (oneOf 3).result[].openTime | integer (int64) |  | Open time for ticker window<br>ticker的开始时间<br>例: `1659580020000` |
| (oneOf 3).result[].closeTime | integer (int64) |  | Close time for ticker window<br>ticker的结束时间<br>例: `1660184820927` |
| (oneOf 3).result[].firstId | integer (int64) |  | Trade IDs<br>统计时间内的第一笔trade id<br>例: `192977765` |
| (oneOf 3).result[].lastId | integer (int64) |  | 例: `195365700` |
| (oneOf 3).result[].count | integer (int64) |  | Number of trades in the interval<br>统计时间内交易笔数<br>例: `2387936` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `8` |

## 24hr ticker price change statistics（24hr 价格变动情况）

`POST /ticker.24hr`

Get 24-hour rolling window price change statistics.

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:

* [`<symbol>@ticker`](/products/spot/web-socket-streams#individual-symbol-ticker-streams) or `!ticker@arr`

* [`<symbol>@miniTicker`](/products/spot/web-socket-streams#individual-symbol-mini-ticker-stream) or [`!miniTicker@arr`](/products/spot/web-socket-streams#all-market-mini-tickers-stream)

If you need different window sizes,

use the [`ticker`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker) request.

24 小时滚动窗口价格变动数据。
如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:

* [`<symbol>@ticker`](/products/spot/web-socket-streams#individual-symbol-ticker-streams)
* [`<symbol>@miniTicker`](/products/spot/web-socket-streams#individual-symbol-mini-ticker-stream) 或者 [`!miniTicker@arr`](/products/spot/web-socket-streams#all-market-mini-tickers-stream)

如果你想用不同的窗口数量，可以用 [`ticker`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker) 请求。

权重: Adjusted based on the number of requested symbols:

|Parameter|Symbols Provided|Weight|
|---|---|---|
|symbol| 1 |2|
| |omitted| 80|
|symbols| 1-20 |2|
| | 21-100 |40|
| | 101+ |80|
| |omitted| 80|

Operation ID: `ticker24hr`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.24hr`<br>例: `ticker.24hr` |
| params | object |  |  |
| params.symbol | string |  | 例: `BNBUSDT` |
| params.symbols | string[] |  |  |
| params.type | string |  | Ticker type. Supported values: FULL (default) or MINI<br>Ticker 类型: FULL (默认) 或者 MINI<br>枚举: `FULL`, `MINI`<br>例: `FULL` |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ticker.24hr",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "type": "FULL",
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：24hr ticker price change statistics / 24hr 价格变动情况

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `9fa2a91b-3fca-4ed7-a9ad-58e3b67483de` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | Symbol Name<br>交易对<br>例: `BNBBTC` |
| (oneOf 1).result.priceChange | string |  | 例: `0.00013900` |
| (oneOf 1).result.priceChangePercent | string |  | 例: `1.020` |
| (oneOf 1).result.weightedAvgPrice | string |  | 例: `0.01382453` |
| (oneOf 1).result.prevClosePrice | string |  | 例: `0.01362800` |
| (oneOf 1).result.lastPrice | string |  | Closing price of the interval<br>间隔收盘价<br>例: `0.01376700` |
| (oneOf 1).result.lastQty | string |  | 例: `1.78800000` |
| (oneOf 1).result.bidPrice | string |  | 例: `0.01376700` |
| (oneOf 1).result.bidQty | string |  | 例: `4.64600000` |
| (oneOf 1).result.askPrice | string |  | 例: `0.01376800` |
| (oneOf 1).result.askQty | string |  | 例: `14.31400000` |
| (oneOf 1).result.openPrice | string |  | Opening price of the Interval<br>间隔开盘价<br>例: `0.01362800` |
| (oneOf 1).result.highPrice | string |  | Highest price in the interval<br>间隔最高价<br>例: `0.01414900` |
| (oneOf 1).result.lowPrice | string |  | Lowest  price in the interval<br>间隔最低价<br>例: `0.01346600` |
| (oneOf 1).result.volume | string |  | Total trade volume (in base asset)<br>总交易量 (base asset)<br>例: `69412.40500000` |
| (oneOf 1).result.quoteVolume | string |  | Total trade volume (in quote asset)<br>总交易量 (quote asset)<br>例: `959.59411487` |
| (oneOf 1).result.openTime | integer (int64) |  | Start of the ticker interval<br>ticker间隔的开始时间<br>例: `1660014164909` |
| (oneOf 1).result.closeTime | integer (int64) |  | End of the ticker interval<br>ticker间隔的结束时间<br>例: `1660100564909` |
| (oneOf 1).result.firstId | integer (int64) |  | First tradeId<br>首笔成交id<br>例: `194696115` |
| (oneOf 1).result.lastId | integer (int64) |  | Last tradeId<br>末笔成交id<br>例: `194968287` |
| (oneOf 1).result.count | integer (int64) |  | Trade count<br>成交笔数<br>例: `272173` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `9fa2a91b-3fca-4ed7-a9ad-58e3b67483de` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | Symbol Name<br>交易对<br>例: `BNBBTC` |
| (oneOf 2).result.openPrice | string |  | Opening price of the Interval<br>间隔开盘价<br>例: `0.01362800` |
| (oneOf 2).result.highPrice | string |  | Highest price in the interval<br>间隔最高价<br>例: `0.01414900` |
| (oneOf 2).result.lowPrice | string |  | Lowest  price in the interval<br>间隔最低价<br>例: `0.01346600` |
| (oneOf 2).result.lastPrice | string |  | Closing price of the interval<br>间隔收盘价<br>例: `0.01376700` |
| (oneOf 2).result.volume | string |  | Total trade volume (in base asset)<br>总交易量 (base asset)<br>例: `69412.40500000` |
| (oneOf 2).result.quoteVolume | string |  | Total trade volume (in quote asset)<br>总交易量 (quote asset)<br>例: `959.59411487` |
| (oneOf 2).result.openTime | integer (int64) |  | Start of the ticker interval<br>ticker间隔的开始时间<br>例: `1660014164909` |
| (oneOf 2).result.closeTime | integer (int64) |  | End of the ticker interval<br>ticker间隔的结束时间<br>例: `1660100564909` |
| (oneOf 2).result.firstId | integer (int64) |  | First trade ID<br>第一个交易 ID<br>例: `194696115` |
| (oneOf 2).result.lastId | integer (int64) |  | Last trade ID<br>最后一个交易ID<br>例: `194968287` |
| (oneOf 2).result.count | integer (int64) |  | Number of trades<br>成交笔数<br>例: `272173` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | Number of trades<br>成交笔数<br>例: `2` |
| (oneOf 3).id | string |  | 例: `901be0d9-fd3b-45e4-acd6-10c580d03430` |
| (oneOf 3).status | integer (int64) |  | 例: `200` |
| (oneOf 3).result | object[] |  |  |
| (oneOf 3).result[].symbol | string |  | Symbol Name<br>交易对<br>例: `BNBBTC` |
| (oneOf 3).result[].priceChange | string |  | 例: `0.00016500` |
| (oneOf 3).result[].priceChangePercent | string |  | 例: `1.213` |
| (oneOf 3).result[].weightedAvgPrice | string |  | 例: `0.01382508` |
| (oneOf 3).result[].prevClosePrice | string |  | 例: `0.01360800` |
| (oneOf 3).result[].lastPrice | string |  | Closing price of the interval<br>间隔收盘价<br>例: `0.01377200` |
| (oneOf 3).result[].lastQty | string |  | 例: `1.01400000` |
| (oneOf 3).result[].bidPrice | string |  | 例: `0.01377100` |
| (oneOf 3).result[].bidQty | string |  | 例: `7.55700000` |
| (oneOf 3).result[].askPrice | string |  | 例: `0.01377200` |
| (oneOf 3).result[].askQty | string |  | 例: `4.37900000` |
| (oneOf 3).result[].openPrice | string |  | Opening price of the Interval<br>间隔开盘价<br>例: `0.01360700` |
| (oneOf 3).result[].highPrice | string |  | Highest price in the interval<br>间隔最高价<br>例: `0.01414900` |
| (oneOf 3).result[].lowPrice | string |  | Lowest  price in the interval<br>间隔最低价<br>例: `0.01346600` |
| (oneOf 3).result[].volume | string |  | Total trade volume (in base asset)<br>总交易量 (base asset)<br>例: `69376.27900000` |
| (oneOf 3).result[].quoteVolume | string |  | Total trade volume (in quote asset)<br>总交易量 (quote asset)<br>例: `959.13277091` |
| (oneOf 3).result[].openTime | integer (int64) |  | Start of the ticker interval<br>ticker间隔的开始时间<br>例: `1660014615517` |
| (oneOf 3).result[].closeTime | integer (int64) |  | End of the ticker interval<br>ticker间隔的结束时间<br>例: `1660101015517` |
| (oneOf 3).result[].firstId | integer (int64) |  | First tradeId<br>首笔成交id<br>例: `194697254` |
| (oneOf 3).result[].lastId | integer (int64) |  | Last tradeId<br>末笔成交id<br>例: `194969483` |
| (oneOf 3).result[].count | integer (int64) |  | Trade count<br>成交笔数<br>例: `272230` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `2` |

## Symbol order book ticker（当前最优挂单）

`POST /ticker.book`

Get the current best price and quantity on the order book.

If you need access to real-time order book ticker updates, please
consider using WebSocket Streams:

* [`<symbol>@bookTicker`](/products/spot/web-socket-streams#individual-symbol-book-ticker-streams)

在订单簿获取当前最优价格和数量。

如果您需要访问实时订单簿 ticker 更新，请考虑使用 WebSocket Streams:

* [`<symbol>@bookTicker`](/products/spot/web-socket-streams#individual-symbol-book-ticker-streams)

权重: Adjusted based on the number of requested symbols:

|Parameter|Symbols Provided|Weight|
|---|---|---|
|symbol| 1 |2|
| |omitted| 4|
|symbols| Any |4|

Operation ID: `tickerBook`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.book`<br>例: `ticker.book` |
| params | object |  |  |
| params.symbol | string |  | Query ticker for a single symbol<br>获取单个交易对的ticker<br>例: `BNBUSDT` |
| params.symbols | string[] |  | Query ticker for multiple symbols<br>获取多个交易对的ticker |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ticker.book",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Symbol order book ticker / 当前最优挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `9d32157c-a556-4d27-9866-66760a174b57` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BNBBTC` |
| (oneOf 1).result.bidPrice | string |  | best bid price.<br>最优买单价<br>例: `0.01358000` |
| (oneOf 1).result.bidQty | string |  | bid/ask qty.<br>挂单量<br>例: `12.53400000` |
| (oneOf 1).result.askPrice | string |  | best ask price.<br>最优卖单价<br>例: `0.01358100` |
| (oneOf 1).result.askQty | string |  | bid/ask qty.<br>挂单量<br>例: `17.83700000` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `057deb3a-2990-41d1-b58b-98ea0f09e1b4` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object[] |  |  |
| (oneOf 2).result[].symbol | string |  | 例: `BNBBTC` |
| (oneOf 2).result[].bidPrice | string |  | best bid price.<br>最优买单价<br>例: `0.01358000` |
| (oneOf 2).result[].bidQty | string |  | bid/ask qty.<br>挂单量<br>例: `12.53400000` |
| (oneOf 2).result[].askPrice | string |  | best ask price.<br>最优卖单价<br>例: `0.01358100` |
| (oneOf 2).result[].askQty | string |  | bid/ask qty.<br>挂单量<br>例: `17.83700000` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `4` |

## Symbol price ticker（最新价格）

`POST /ticker.price`

Get the latest market price for a symbol.

If you need access to real-time price updates, please consider using
WebSocket Streams:

* `<symbol>@aggTrade`

* `<symbol>@trade`

获取交易对最新价格

如果需要访问实时价格更新，请考虑使用 WebSocket Streams:

* `<symbol>@aggTrade`
* `<symbol>@trade`

权重: Adjusted based on the number of requested symbols:

|Parameter|Symbols Provided|Weight|
|---|---|---|
|symbol| 1 |2|
| |omitted| 4|
|symbols| Any |4|

Operation ID: `tickerPrice`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.price`<br>例: `ticker.price` |
| params | object |  |  |
| params.symbol | string |  | Query price for a single symbol<br>获取单个交易对的价格<br>例: `BNBUSDT` |
| params.symbols | string[] |  | Query price for multiple symbols<br>获取多个交易对的价格 |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ticker.price",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Symbol price ticker / 最新价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `043a7cf2-bde3-4888-9604-c8ac41fcba4d` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BNBBTC` |
| (oneOf 1).result.price | string |  | 例: `0.01361900` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `e739e673-24c8-4adf-9cfa-b81f30330b09` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object[] |  |  |
| (oneOf 2).result[].symbol | string |  | 例: `BNBBTC` |
| (oneOf 2).result[].price | string |  | 例: `0.01363700` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `4` |

## Trading Day Ticker（交易日行情(Ticker)）

`POST /ticker.tradingDay`

Price change statistics for a trading day.

交易日价格变动统计。

权重: 4 for each requested symbol regardless of windowSize. The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

Operation ID: `tickerTradingDay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.tradingDay`<br>例: `ticker.tradingDay` |
| params | object |  |  |
| params.symbol | string |  | 例: `BNBUSDT` |
| params.symbols | string[] |  |  |
| params.timeZone | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>例: `0` |
| params.type | string |  | Ticker type. Supported values: FULL (default) or MINI<br>Ticker 类型: FULL (默认) 或者 MINI<br>枚举: `FULL`, `MINI`<br>例: `FULL` |
| params.symbolStatus | string |  | Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "ticker.tradingDay",
  "params": {
    "symbol": "BNBUSDT",
    "symbols": [
      "BTCUSDT"
    ],
    "timeZone": "0",
    "type": "FULL",
    "symbolStatus": "TRADING"
  }
}
```

### 响应 Successful Response：Trading Day Ticker / Trading Day 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `f4b3b507-c8f2-442a-81a6-b2f12daa030f` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.priceChange | string |  | Absolute price change<br>绝对价格变动<br>例: `-83.13000000` |
| (oneOf 1).result.priceChangePercent | string |  | Relative price change in percent<br>相对价格变动百分比<br>例: `-0.317` |
| (oneOf 1).result.weightedAvgPrice | string |  | quoteVolume / volume<br>报价成交量 / 成交量<br>例: `26234.58803036` |
| (oneOf 1).result.openPrice | string |  | 例: `26304.80000000` |
| (oneOf 1).result.highPrice | string |  | 例: `26397.46000000` |
| (oneOf 1).result.lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 1).result.lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 1).result.volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 1).result.quoteVolume | string |  | 例: `485217905.04210480` |
| (oneOf 1).result.openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 1).result.closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 1).result.firstId | integer (int64) |  | 例: `3220151555` |
| (oneOf 1).result.lastId | integer (int64) |  | 例: `3220849281` |
| (oneOf 1).result.count | integer (int64) |  | 例: `697727` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `4` |
| (oneOf 2).id | string |  | 例: `f4b3b507-c8f2-442a-81a6-b2f12daa030f` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object[] |  |  |
| (oneOf 2).result[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result[].priceChange | string |  | Absolute price change<br>绝对价格变动<br>例: `-83.13000000` |
| (oneOf 2).result[].priceChangePercent | string |  | Relative price change in percent<br>相对价格变动百分比<br>例: `-0.317` |
| (oneOf 2).result[].weightedAvgPrice | string |  | quoteVolume / volume<br>报价成交量 / 成交量<br>例: `26234.58803036` |
| (oneOf 2).result[].openPrice | string |  | 例: `26304.80000000` |
| (oneOf 2).result[].highPrice | string |  | 例: `26397.46000000` |
| (oneOf 2).result[].lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 2).result[].lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 2).result[].volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 2).result[].quoteVolume | string |  | Volume in quote asset<br>报价资产的成交量<br>例: `485217905.04210480` |
| (oneOf 2).result[].openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 2).result[].closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 2).result[].firstId | integer (int64) |  | Trade ID of the first trade in the interval<br>区间内的第一个交易的交易ID<br>例: `3220151555` |
| (oneOf 2).result[].lastId | integer (int64) |  | Trade ID of the last trade in the interval<br>区间内的最后一个交易的交易ID<br>例: `3220849281` |
| (oneOf 2).result[].count | integer (int64) |  | Number of trades in the interval<br>区间内的交易数量<br>例: `697727` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `8` |
| (oneOf 3).id | string |  | 例: `f4b3b507-c8f2-442a-81a6-b2f12daa030f` |
| (oneOf 3).status | integer (int64) |  | 例: `200` |
| (oneOf 3).result | object |  |  |
| (oneOf 3).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 3).result.openPrice | string |  | 例: `26304.80000000` |
| (oneOf 3).result.highPrice | string |  | 例: `26397.46000000` |
| (oneOf 3).result.lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 3).result.lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 3).result.volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 3).result.quoteVolume | string |  | Volume in quote asset<br>报价资产的成交量<br>例: `485217905.04210480` |
| (oneOf 3).result.openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 3).result.closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 3).result.firstId | integer (int64) |  | Trade ID of the first trade in the interval<br>区间内的第一个交易的交易ID<br>例: `3220151555` |
| (oneOf 3).result.lastId | integer (int64) |  | Trade ID of the last trade in the interval<br>区间内的最后一个交易的交易ID<br>例: `3220849281` |
| (oneOf 3).result.count | integer (int64) |  | Number of trades in the interval<br>区间内的交易数量<br>例: `697727` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `4` |
| (oneOf 4).id | string |  | 例: `f4b3b507-c8f2-442a-81a6-b2f12daa030f` |
| (oneOf 4).status | integer (int64) |  | 例: `200` |
| (oneOf 4).result | object[] |  |  |
| (oneOf 4).result[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 4).result[].openPrice | string |  | 例: `26304.80000000` |
| (oneOf 4).result[].highPrice | string |  | 例: `26397.46000000` |
| (oneOf 4).result[].lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 4).result[].lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 4).result[].volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 4).result[].quoteVolume | string |  | Volume in quote asset<br>报价资产的成交量<br>例: `485217905.04210480` |
| (oneOf 4).result[].openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 4).result[].closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 4).result[].firstId | integer (int64) |  | Trade ID of the first trade in the interval<br>区间内的第一个交易的交易ID<br>例: `3220151555` |
| (oneOf 4).result[].lastId | integer (int64) |  | Trade ID of the last trade in the interval<br>区间内的最后一个交易的交易ID<br>例: `3220849281` |
| (oneOf 4).result[].count | integer (int64) |  | Number of trades in the interval<br>区间内的交易数量<br>例: `697727` |
| (oneOf 4).rateLimits | object[] |  |  |
| (oneOf 4).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 4).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 4).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 4).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 4).rateLimits[].count | integer (int64) |  | 例: `8` |

## Aggregate trades（归集交易）

`POST /trades.aggregate`

Get aggregate trades.

An *aggregate trade* (aggtrade) represents one or more individual
trades.

Trades that fill at the same time, from the same taker order, with the
same price –

those trades are collected into an aggregate trade with total quantity
of the individual trades.

If you need access to real-time trading activity, please consider using
WebSocket Streams:

* `<symbol>@aggTrade`

If you need historical aggregate trade data, please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades).

获取归集交易。

一个 *归集交易* (aggtrade) 代表一个或多个单独的交易。

同时间，同 taker 订单和同价格的执行交易会被聚合为一条归集交易。

如果需要访问实时交易活动，请考虑使用 WebSocket Streams：

* `<symbol>@aggTrade`

如果需要历史总交易数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades)。

Operation ID: `tradesAggregate`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `trades.aggregate`<br>例: `trades.aggregate` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.fromId | integer (int64) |  | Aggregate trade ID to begin at<br>起始归集交易ID<br>例: `1` |
| params.startTime | integer (int64) |  | Timestamp in ms to get aggregate trades from INCLUSIVE.<br>从该时刻之后的成交记录开始返回结果<br>例: `1735693200000` |
| params.endTime | integer (int64) |  | Timestamp in ms to get aggregate trades until INCLUSIVE.<br>返回该时刻为止的成交记录<br>例: `1735693200000` |
| params.limit | integer |  | 默认: `500`<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "trades.aggregate",
  "params": {
    "symbol": "BNBUSDT",
    "fromId": 1,
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "limit": 1
  }
}
```

### 响应 Successful Response：Aggregate trades / 归集交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `189da436-d4bd-48ca-9f95-9f613d621717` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].a | integer (int64) |  | Aggregate tradeId<br>归集成交ID<br>例: `50000000` |
| result[].p | string |  | Price<br>成交价<br>例: `0.00274100` |
| result[].q | string |  | Quantity<br>成交量<br>例: `57.19000000` |
| result[].f | integer (int64) |  | First tradeId<br>被归集的首个成交ID<br>例: `59120167` |
| result[].l | integer (int64) |  | Last tradeId<br>被归集的末个成交ID<br>例: `59120170` |
| result[].T | integer (int64) |  | Timestamp<br>成交时间<br>例: `1565877971222` |
| result[].m | boolean |  | Was the buyer the maker?<br>是否为主动卖出单<br>例: `True` |
| result[].M | boolean |  | Was the trade the best price match?<br>是否为最优撮合单(可忽略，目前总为最优撮合)<br>例: `True` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `4` |

## Historical trades（历史交易）

`POST /trades.historical`

Get historical trades.

获取历史交易。

Operation ID: `tradesHistorical`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `trades.historical`<br>例: `trades.historical` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.fromId | integer (int64) |  | Trade ID to begin at<br>起始交易ID<br>例: `1` |
| params.limit | integer |  | 默认: `500`<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "trades.historical",
  "params": {
    "symbol": "BNBUSDT",
    "fromId": 1,
    "limit": 1
  }
}
```

### 响应 Successful Response：Historical trades / 历史交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `cffc9c7d-4efc-4ce0-b587-6b87448f052a` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].id | integer (int64) |  | 例: `0` |
| result[].price | string |  | 例: `0.00005000` |
| result[].qty | string |  | 例: `40.00000000` |
| result[].quoteQty | string |  | 例: `0.00200000` |
| result[].time | integer (int64) |  | 例: `1500004800376` |
| result[].isBuyerMaker | boolean |  | 例: `True` |
| result[].isBestMatch | boolean |  | 例: `True` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `25` |

## Historical Block Trades（查询历史大宗交易）

`POST /blockTrades.historical`

Get block trades.

获取大宗交易记录。

Operation ID: `blockTradesHistorical`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `blockTrades.historical`<br>例: `blockTrades.historical` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBBTC` |
| params.fromId | integer (int64) | 是 | Block trade ID to fetch from<br>从该大宗交易ID开始查询<br>例: `582` |
| params.limit | integer (int64) |  | Default: 500; Maximum: 1000<br>默认: 500; 最大: 1000<br>默认: `500`<br>例: `500` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "blockTrades.historical",
  "params": {
    "symbol": "BNBBTC",
    "fromId": 582,
    "limit": 500
  }
}
```

### 响应 Successful Response：Historical Block Trades / 历史大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `cffc9c7d-4efc-4ce0-b587-6b87448f052a` |
| status | integer |  | 例: `200` |
| result | object[] |  |  |
| result[].id | integer (int64) |  | 例: `582` |
| result[].price | string |  | 例: `0.052` |
| result[].qty | string |  | 例: `5838` |
| result[].quoteQty | string |  | 例: `303.576` |
| result[].time | integer (int64) |  | 例: `1772506983321` |
| result[].isBuyerMaker | boolean |  | 例: `True` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer |  | 例: `1` |
| rateLimits[].limit | integer |  | 例: `6000` |
| rateLimits[].count | integer |  | 例: `10` |

## Recent trades（最近的交易）

`POST /trades.recent`

Get recent trades.

If you need access to real-time trading activity, please consider using
WebSocket Streams:

* `<symbol>@trade`

获取最近的交易

如果您需要访问实时交易活动，请考虑使用 WebSocket Streams：

* `<symbol>@trade`

Operation ID: `tradesRecent`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `trades.recent`<br>例: `trades.recent` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.limit | integer |  | 默认: `500`<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "trades.recent",
  "params": {
    "symbol": "BNBUSDT",
    "limit": 1
  }
}
```

### 响应 Successful Response：Recent trades / 最近的交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `409a20bd-253d-41db-a6dd-687862a5882f` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].id | integer (int64) |  | 例: `194686783` |
| result[].price | string |  | 例: `0.01361000` |
| result[].qty | string |  | 例: `0.01400000` |
| result[].quoteQty | string |  | 例: `0.00019054` |
| result[].time | integer (int64) |  | 例: `1660009530807` |
| result[].isBuyerMaker | boolean |  | 例: `True` |
| result[].isBestMatch | boolean |  | 例: `True` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `25` |

## UI Klines（UI K线数据）

`POST /uiKlines`

Get klines (candlestick bars) optimized for presentation.

This request is similar to `klines`, having the same parameters and response. `uiKlines` return modified kline data, optimized for presentation of candlestick charts.

请求参数和响应字段与`k线`接口相同。
uiKlines 是返回修改后的k线数据，针对k线图的呈现进行了优化。

Operation ID: `uiKlines`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `uiKlines`<br>例: `uiKlines` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.interval | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |
| params.startTime | integer (int64) |  | 例: `1735693200000` |
| params.endTime | integer (int64) |  | 例: `1735693200000` |
| params.timeZone | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>例: `0` |
| params.limit | integer |  | 默认: `500`<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "uiKlines",
  "params": {
    "symbol": "BNBUSDT",
    "interval": "1s",
    "startTime": 1735693200000,
    "endTime": 1735693200000,
    "timeZone": "0",
    "limit": 1
  }
}
```

### 响应 Successful Response：UI Klines / UI K线数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `b137468a-fb20-4c06-bd6b-625148eec958` |
| status | integer (int64) |  | 例: `200` |
| result | oneOf[][] |  |  |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Query Reference Price（查询参考价格）

`POST /referencePrice`

Query Reference Price

查询参考价格

Operation ID: `referencePrice`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `referencePrice`<br>例: `referencePrice` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BAZUSD` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "referencePrice",
  "params": {
    "symbol": "BAZUSD"
  }
}
```

### 响应 Successful Response：Query Reference Price / 查询参考价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `ddbfb65f-9ebf-42ec-8240-8f0f91de0867` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BAZUSD` |
| (oneOf 1).result.referencePrice | string |  | 例: `0.00501900` |
| (oneOf 1).result.timestamp | integer (int64) |  | Timestamp when the reference price was valid<br>参考价格生效的时间<br>例: `1770946889251` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `5132affb-0aba-4821-b475-f262504556b43` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | 例: `BAZUSD` |
| (oneOf 2).result.referencePrice |  |  | 例: `None` |
| (oneOf 2).result.timestamp | integer (int64) |  | Timestamp when the reference price was valid<br>参考价格生效的时间<br>例: `1770946889251` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 3).id | string |  | 例: `5132affa-0aba-4831-b475-f262504556b41` |
| (oneOf 3).status | integer (int64) |  | 例: `200` |
| (oneOf 3).result | object |  |  |
| (oneOf 3).result.code | integer (int64) |  | 例: `-2043` |
| (oneOf 3).result.msg | string |  | 例: `This symbol doesn't have a reference price.` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `2` |

## Query Reference Price Calculation（查询参考价格计算方式）

`POST /referencePrice.calculation`

Query Reference Price Calculation

查询参考价格计算方式

Operation ID: `referencePriceCalculation`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `referencePrice.calculation`<br>例: `referencePrice.calculation` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BAZUSD` |
| params.symbolStatus | string |  | 枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `BAZUSD` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "referencePrice.calculation",
  "params": {
    "symbol": "BAZUSD",
    "symbolStatus": "BAZUSD"
  }
}
```

### 响应 Successful Response：Query Reference Price Calculation / 查询参考价格计算方式

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `ddbfb65f-9ebf-42ec-8240-8f0f91de0867` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BAZUSD` |
| (oneOf 1).result.calculationType | string |  | 例: `ARITHMETIC_MEAN` |
| (oneOf 1).result.bucketCount | integer (int64) |  | If the reference price is being calculated by the matching engine as an arithmetic mean<br>如果参考价格由撮合引擎以算术平均数计算<br>例: `10` |
| (oneOf 1).result.bucketWidthMs | integer (int64) |  | If the reference price is being calculated by the matching engine as an arithmetic mean<br>如果参考价格由撮合引擎以算术平均数计算<br>例: `1000` |
| (oneOf 1).result.externalCalculationId | integer (int64) |  | If the reference price is being calculated outside the matching engine<br>如果参考价格由撮合引擎外部计算<br>例: `42` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `5132affa-0aba-4831-b475-f262504556b41` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | 例: `BAZUSD` |
| (oneOf 2).result.calculationType | string |  | 例: `EXTERNAL` |
| (oneOf 2).result.externalCalculationId | integer (int64) |  | If the reference price is being calculated outside the matching engine<br>如果参考价格由撮合引擎外部计算<br>例: `42` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `2` |

### 响应 Unsuccessful Response (400)：The symbol does not have a reference price / 该交易对没有参考价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `5132affa-0aba-4831-b475-f262504556b41` |
| status | integer (int64) |  | 例: `400` |
| error | object |  |  |
| error.code | integer (int64) |  | 例: `-2043` |
| error.msg | string |  | 例: `This symbol doesn't have a reference price.` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Cancel open orders (TRADE)（撤销单一交易对的所有挂单 (TRADE)）

`POST /openOrders.cancelAll`

Cancel all open orders on a symbol.
This includes orders that are part of an order list.

撤销单一交易对的所有挂单,包括交易组。

Operation ID: `openOrdersCancelAll`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `openOrders.cancelAll`<br>例: `openOrders.cancelAll` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "openOrders.cancelAll",
  "params": {
    "symbol": "BNBUSDT",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel open orders / 撤销单一交易对的所有挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `778f938f-9041-4b88-9914-efbf64eeacc8` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].orderListId | integer (int64) |  | 例: `-1` |
| result[].contingencyType | string |  | 例: `OCO` |
| result[].listStatusType | string |  | 例: `ALL_DONE` |
| result[].listOrderStatus | string |  | 例: `ALL_DONE` |
| result[].listClientOrderId | string |  | 例: `iuVNVJYYrByz6C4yGOPPK0` |
| result[].transactionTime | integer (int64) |  | 例: `1660803702431` |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders | object[] |  |  |
| result[].orders[].symbol | string |  | 例: `BTCUSDT` |
| result[].orders[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].orders[].clientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| result[].orderReports | object[] |  |  |
| result[].orderReports[].symbol | string |  | 例: `BTCUSDT` |
| result[].orderReports[].origClientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| result[].orderReports[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].orderReports[].orderListId | integer (int64) |  | 例: `19431` |
| result[].orderReports[].clientOrderId | string |  | 例: `OFFXQtxVFZ6Nbcg4PgE2DA` |
| result[].orderReports[].transactTime | integer (int64) |  | 例: `1684804350068` |
| result[].orderReports[].price | string |  | 例: `23450.50000000` |
| result[].orderReports[].origQty | string |  | 例: `0.00850000` |
| result[].orderReports[].executedQty | string |  | 例: `0.00000000` |
| result[].orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result[].orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result[].orderReports[].status | string |  | 例: `CANCELED` |
| result[].orderReports[].timeInForce | string |  | 例: `GTC` |
| result[].orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| result[].orderReports[].side | string |  | 例: `BUY` |
| result[].orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result[].orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result[].orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result[].orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result[].orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result[].orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result[].orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result[].orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result[].orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result[].orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result[].orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result[].orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result[].orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result[].orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result[].orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result[].orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| result[].origClientOrderId | string |  | 例: `4d96324ff9d44481926157` |
| result[].orderId | integer (int64) |  | 例: `12569099453` |
| result[].clientOrderId | string |  | 例: `91fe37ce9e69c90d6358c0` |
| result[].transactTime | integer (int64) |  | 例: `1684804350068` |
| result[].price | string |  | 例: `23416.10000000` |
| result[].origQty | string |  | 例: `0.00847000` |
| result[].executedQty | string |  | 例: `0.00001000` |
| result[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result[].cummulativeQuoteQty | string |  | 例: `0.23416100` |
| result[].status | string |  | 例: `CANCELED` |
| result[].timeInForce | string |  | 例: `GTC` |
| result[].type | string |  | 例: `LIMIT` |
| result[].side | string |  | 例: `SELL` |
| result[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result[].selfTradePreventionMode | string |  | 例: `NONE` |
| result[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Order Amend Keep Priority (TRADE)（修改订单并保留优先级 (TRADE)）

`POST /order.amend.keepPriority`

Reduce the quantity of an existing open order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [Order Amend Keep Priority FAQ](/products/spot/faqs/order_amend_keep_priority) to learn more.

由客户发送以减少其现有当前挂单的原始数量。

这个请求会把0个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

请阅读 [保留优先权的修改订单常见问题](/products/spot/faqs/order_amend_keep_priority) 了解更多信息。

Operation ID: `orderAmendKeepPriority`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.amend.keepPriority`<br>例: `order.amend.keepPriority` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) |  | `orderId` or `origClientOrderId` must be sent<br>需提供 `orderId` 或 `origClientOrderId`。<br>例: `1` |
| params.origClientOrderId | string |  | `orderId` or `origClientOrderId` must be sent<br>需提供 `orderId` 或 `origClientOrderId`。<br>例: `myOrder1` |
| params.newClientOrderId | string |  | The new client order ID for the order after being amended. <br> If not sent, one will be randomly generated. <br> It is possible to reuse the current clientOrderId by sending it as the `newClientOrderId`.<br>订单在被修改后被赋予的新 client order ID。 <br> 如果未发送则自动生成。 <br> 可以将当前 clientOrderId 作为 `newClientOrderId` 发送来重用当前 clientOrderId 的值。<br>例: `myOrder2` |
| params.newQty | number (float) | 是 | `newQty` must be greater than 0 and less than the order's quantity.<br>交易的新数量。 `newQty` 必须大于0, 但是必须比订单的原始数量小。<br>例: `5` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.amend.keepPriority",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "origClientOrderId": "myOrder1",
    "newClientOrderId": "myOrder2",
    "newQty": 5,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Order Amend Keep Priority / 修改订单并保留优先级

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `56374a46-3061-486b-a311-89ee972eb648` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.transactTime | integer (int64) |  | 例: `1741923284382` |
| (oneOf 1).result.executionId | integer (int64) |  | 例: `16` |
| (oneOf 1).result.amendedOrder | object |  |  |
| (oneOf 1).result.amendedOrder.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.amendedOrder.orderId | integer (int64) |  | 例: `12` |
| (oneOf 1).result.amendedOrder.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 1).result.amendedOrder.origClientOrderId | string |  | 例: `my_test_order1` |
| (oneOf 1).result.amendedOrder.clientOrderId | string |  | 例: `4zR9HFcEq8gM1tWUqPEUHc` |
| (oneOf 1).result.amendedOrder.price | string |  | 例: `5.00000000` |
| (oneOf 1).result.amendedOrder.qty | string |  | 例: `5.00000000` |
| (oneOf 1).result.amendedOrder.executedQty | string |  | 例: `0.00000000` |
| (oneOf 1).result.amendedOrder.preventedQty | string |  | 例: `0.00000000` |
| (oneOf 1).result.amendedOrder.quoteOrderQty | string |  | 例: `0.00000000` |
| (oneOf 1).result.amendedOrder.cumulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 1).result.amendedOrder.status | string |  | 例: `NEW` |
| (oneOf 1).result.amendedOrder.timeInForce | string |  | 例: `GTC` |
| (oneOf 1).result.amendedOrder.type | string |  | 例: `LIMIT` |
| (oneOf 1).result.amendedOrder.side | string |  | 例: `BUY` |
| (oneOf 1).result.amendedOrder.workingTime | integer (int64) |  | 例: `1741923284364` |
| (oneOf 1).result.amendedOrder.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `56374b46-3061-486b-a311-89ee972eb648` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.transactTime | integer (int64) |  | 例: `1741924229819` |
| (oneOf 2).result.executionId | integer (int64) |  | 例: `60` |
| (oneOf 2).result.amendedOrder | object |  |  |
| (oneOf 2).result.amendedOrder.symbol | string |  | 例: `BTUCSDT` |
| (oneOf 2).result.amendedOrder.orderId | integer (int64) |  | 例: `23` |
| (oneOf 2).result.amendedOrder.orderListId | integer (int64) |  | 例: `4` |
| (oneOf 2).result.amendedOrder.origClientOrderId | string |  | 例: `my_pending_order` |
| (oneOf 2).result.amendedOrder.clientOrderId | string |  | 例: `xbxXh5SSwaHS7oUEOCI88B` |
| (oneOf 2).result.amendedOrder.price | string |  | 例: `1.00000000` |
| (oneOf 2).result.amendedOrder.qty | string |  | 例: `5.00000000` |
| (oneOf 2).result.amendedOrder.executedQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.amendedOrder.preventedQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.amendedOrder.quoteOrderQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.amendedOrder.cumulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.amendedOrder.status | string |  | 例: `NEW` |
| (oneOf 2).result.amendedOrder.timeInForce | string |  | 例: `GTC` |
| (oneOf 2).result.amendedOrder.type | string |  | 例: `LIMIT` |
| (oneOf 2).result.amendedOrder.side | string |  | 例: `BUY` |
| (oneOf 2).result.amendedOrder.workingTime | integer (int64) |  | 例: `1741924204920` |
| (oneOf 2).result.amendedOrder.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).result.amendedOrder.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| (oneOf 2).result.amendedOrder.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| (oneOf 2).result.amendedOrder.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| (oneOf 2).result.amendedOrder.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| (oneOf 2).result.amendedOrder.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| (oneOf 2).result.amendedOrder.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| (oneOf 2).result.amendedOrder.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| (oneOf 2).result.amendedOrder.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| (oneOf 2).result.amendedOrder.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| (oneOf 2).result.amendedOrder.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| (oneOf 2).result.amendedOrder.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| (oneOf 2).result.amendedOrder.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| (oneOf 2).result.amendedOrder.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| (oneOf 2).result.amendedOrder.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| (oneOf 2).result.amendedOrder.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| (oneOf 2).result.listStatus | object |  |  |
| (oneOf 2).result.listStatus.orderListId | integer (int64) |  | 例: `4` |
| (oneOf 2).result.listStatus.contingencyType | string |  | 例: `OTO` |
| (oneOf 2).result.listStatus.listOrderStatus | string |  | 例: `EXECUTING` |
| (oneOf 2).result.listStatus.listClientOrderId | string |  | 例: `8nOGLLawudj1QoOiwbroRH` |
| (oneOf 2).result.listStatus.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.listStatus.orders | object[] |  |  |
| (oneOf 2).result.listStatus.orders[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.listStatus.orders[].orderId | integer (int64) |  | 例: `22` |
| (oneOf 2).result.listStatus.orders[].clientOrderId | string |  | 例: `g04EWsjaackzedjC9wRkWD` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `4` |

## Cancel order (TRADE)（撤销订单 (TRADE)）

`POST /order.cancel`

Cancel an active order.

取消有效订单。

Operation ID: `orderCancel`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.cancel`<br>例: `order.cancel` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderId | integer (int64) |  | 例: `1` |
| params.origClientOrderId | string |  | 例: `myOrder1` |
| params.newClientOrderId | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `cancelMyOrder1` |
| params.cancelRestrictions | string |  | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).<br>支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。<br>枚举: `ONLY_NEW`, `ONLY_PARTIALLY_FILLED`<br>例: `ONLY_NEW` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.cancel",
  "params": {
    "symbol": "BNBUSDT",
    "orderId": 1,
    "origClientOrderId": "myOrder1",
    "newClientOrderId": "cancelMyOrder1",
    "cancelRestrictions": "ONLY_NEW",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel order / 撤销订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `5633b6a2-90a9-4192-83e7-925c90b6a2fd` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.origClientOrderId | string |  | clientOrderId that was canceled<br>被取消的 clientOrderId<br>例: `4d96324ff9d44481926157` |
| (oneOf 1).result.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 1).result.orderListId | integer (int64) |  | set only for legs of an order list<br>订单列表的ID，不然就是 -1<br>例: `-1` |
| (oneOf 1).result.clientOrderId | string |  | newClientOrderId from request<br>请求的 newClientOrderId<br>例: `91fe37ce9e69c90d6358c0` |
| (oneOf 1).result.transactTime | integer (int64) |  | 例: `1684804350068` |
| (oneOf 1).result.price | string |  | 例: `23416.10000000` |
| (oneOf 1).result.origQty | string |  | 例: `0.00847000` |
| (oneOf 1).result.executedQty | string |  | 例: `0.00001000` |
| (oneOf 1).result.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 1).result.cummulativeQuoteQty | string |  | 例: `0.23416100` |
| (oneOf 1).result.status | string |  | 例: `CANCELED` |
| (oneOf 1).result.timeInForce | string |  | 例: `GTC` |
| (oneOf 1).result.type | string |  | 例: `LIMIT` |
| (oneOf 1).result.side | string |  | 例: `SELL` |
| (oneOf 1).result.stopPrice | string |  | present only if stopPrice set for the order<br>如果订单设置了 stopPrice 会出现<br>例: `0.00000000` |
| (oneOf 1).result.trailingDelta | integer (int64) |  | present only if trailingDelta set for the order<br>如果订单设置了 trailingDelta 会出现<br>例: `0` |
| (oneOf 1).result.icebergQty | string |  | present only if icebergQty set for the order<br>如果订单设置了 icebergQty 会出现<br>例: `0.00000000` |
| (oneOf 1).result.strategyId | integer (int64) |  | present only if strategyId set for the order<br>如果订单设置了 strategyId 会出现<br>例: `37463720` |
| (oneOf 1).result.strategyType | integer (int64) |  | present only if strategyType set for the order<br>如果订单设置了 strategyType 会出现<br>例: `1000000` |
| (oneOf 1).result.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `16eaf097-bbec-44b9-96ff-e97e6e875870` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.origClientOrderId | string |  | 例: `4d96324ff9d44481926157` |
| (oneOf 2).result.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 2).result.orderListId | integer (int64) |  | 例: `19431` |
| (oneOf 2).result.clientOrderId | string |  | 例: `91fe37ce9e69c90d6358c0` |
| (oneOf 2).result.transactTime | integer (int64) |  | 例: `1684804350068` |
| (oneOf 2).result.price | string |  | 例: `23416.10000000` |
| (oneOf 2).result.origQty | string |  | 例: `0.00847000` |
| (oneOf 2).result.executedQty | string |  | 例: `0.00001000` |
| (oneOf 2).result.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 2).result.cummulativeQuoteQty | string |  | 例: `0.23416100` |
| (oneOf 2).result.status | string |  | 例: `CANCELED` |
| (oneOf 2).result.timeInForce | string |  | 例: `GTC` |
| (oneOf 2).result.type | string |  | 例: `LIMIT` |
| (oneOf 2).result.side | string |  | 例: `SELL` |
| (oneOf 2).result.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| (oneOf 2).result.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| (oneOf 2).result.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| (oneOf 2).result.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| (oneOf 2).result.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| (oneOf 2).result.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).result.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| (oneOf 2).result.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| (oneOf 2).result.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| (oneOf 2).result.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| (oneOf 2).result.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| (oneOf 2).result.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| (oneOf 2).result.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| (oneOf 2).result.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| (oneOf 2).result.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| (oneOf 2).result.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| (oneOf 2).result.contingencyType | string |  | 例: `OCO` |
| (oneOf 2).result.listStatusType | string |  | 例: `ALL_DONE` |
| (oneOf 2).result.listOrderStatus | string |  | 例: `ALL_DONE` |
| (oneOf 2).result.listClientOrderId | string |  | 例: `iuVNVJYYrByz6C4yGOPPK0` |
| (oneOf 2).result.transactionTime | integer (int64) |  | 例: `1660803702431` |
| (oneOf 2).result.orders | object[] |  |  |
| (oneOf 2).result.orders[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.orders[].orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 2).result.orders[].clientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| (oneOf 2).result.orderReports | object[] |  | order list order's status format is the same as for individual orders.<br>订单列表的状态格式与单个订单相同。 |
| (oneOf 2).result.orderReports[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.orderReports[].origClientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| (oneOf 2).result.orderReports[].orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 2).result.orderReports[].orderListId | integer (int64) |  | 例: `19431` |
| (oneOf 2).result.orderReports[].clientOrderId | string |  | 例: `OFFXQtxVFZ6Nbcg4PgE2DA` |
| (oneOf 2).result.orderReports[].transactTime | integer (int64) |  | 例: `1684804350068` |
| (oneOf 2).result.orderReports[].price | string |  | 例: `23450.50000000` |
| (oneOf 2).result.orderReports[].origQty | string |  | 例: `0.00850000` |
| (oneOf 2).result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 2).result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.orderReports[].status | string |  | 例: `CANCELED` |
| (oneOf 2).result.orderReports[].timeInForce | string |  | 例: `GTC` |
| (oneOf 2).result.orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| (oneOf 2).result.orderReports[].side | string |  | 例: `BUY` |
| (oneOf 2).result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| (oneOf 2).result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| (oneOf 2).result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| (oneOf 2).result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| (oneOf 2).result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| (oneOf 2).result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| (oneOf 2).result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| (oneOf 2).result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| (oneOf 2).result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| (oneOf 2).result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| (oneOf 2).result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| (oneOf 2).result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| (oneOf 2).result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| (oneOf 2).result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| (oneOf 2).result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `1` |

## Cancel and replace order (TRADE)（撤消挂单再下单 (TRADE)）

`POST /order.cancelReplace`

* Cancel an existing order and immediately place a new order instead of the canceled one.
* A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.
* You can only cancel an individual order from an orderList using this method, but the result is the same as canceling the entire orderList.

* 撤消一个现有订单，并立即重新下单。
* 即使新订单未被尝试（即 `newOrderResult: NOT_ATTEMPTED`），未成交订单数量仍会增加1。
* 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。

Operation ID: `orderCancelReplace`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.cancelReplace`<br>例: `order.cancelReplace` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.cancelReplaceMode | string | 是 | The allowed values are: <br/> `STOP_ON_FAILURE` - If the cancel request fails, the new order placement will not be attempted. <br/> `ALLOW_FAILURE` - new order placement will be attempted even if cancel request fails.<br>指定类型：`STOP_ON_FAILURE` - 如果撤消订单失败将不会继续重新下单。<br/> `ALLOW_FAILURE` - 不管撤消订单是否成功都会继续重新下单。<br>枚举: `STOP_ON_FAILURE`, `ALLOW_FAILURE`<br>例: `STOP_ON_FAILURE` |
| params.cancelOrderId | integer (int64) |  | Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br>If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br>If both conditions are not met the request will be rejected.<br>必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。<br>例: `1` |
| params.cancelOrigClientOrderId | string |  | Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br> If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br> If both conditions are not met the request will be rejected.<br>必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。<br>例: `myOrder1` |
| params.cancelNewClientOrderId | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的id，如空缺系统会自动赋值<br>例: `cancelMyOrder1` |
| params.side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| params.timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.price | number (float) |  | 例: `1` |
| params.quantity | number (float) |  | 例: `1` |
| params.quoteOrderQty | number (float) |  | 例: `1` |
| params.newClientOrderId | string |  | Used to identify the new order.<br>用于辨识新订单。<br>例: `myOrder2` |
| params.newOrderRespType | string |  | Allowed values: <br/> `ACK`, `RESULT`, `FULL` <br/> `MARKET` and `LIMIT` orders types default to `FULL`; all other orders default to `ACK`<br>指定响应类型: <br/> 指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`， 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。<br>例: `1` |
| params.trailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参考 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| params.strategyId | integer (int64) |  | 例: `1` |
| params.strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/products/spot/enums#stpmodes).<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.cancelRestrictions | string |  | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).<br>支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。<br>枚举: `ONLY_NEW`, `ONLY_PARTIALLY_FILLED`<br>例: `ONLY_NEW` |
| params.orderRateLimitExceededMode | string |  | Supported values: <br> `DO_NOTHING` (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit<br> `CANCEL_ONLY` - will always cancel the order<br>支持的值： <br></br> `DO_NOTHING`（默认值）- 仅在账户未超过未成交订单频率限制时，会尝试取消订单。<br></br> `CANCEL_ONLY` - 将始终取消订单。<br>枚举: `DO_NOTHING`, `CANCEL_ONLY`<br>例: `DO_NOTHING` |
| params.pegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG` <br> See Pegged Orders<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 <br> 参阅 关于挂钩订单参数的注意事项<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pegOffsetValue | integer |  | Price level to peg the price to (max: 100) <br> See Pegged Orders<br>用于挂钩的价格水平（最大值：100）。 <br> 参阅 关于挂钩订单参数的注意事项<br>例: `1` |
| params.pegOffsetType | string |  | Only `PRICE_LEVEL` is supported <br> See Pegged Orders<br>仅支持 `PRICE_LEVEL`。 <br> 参阅 关于挂钩订单参数的注意事项<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.quoteNotionalLimit | number (float) |  | For replacement orders on the BUY side only. Maximum quote-asset notional the replacement order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单方向的新订单。新订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.cancelReplace",
  "params": {
    "symbol": "BNBUSDT",
    "cancelReplaceMode": "STOP_ON_FAILURE",
    "cancelOrderId": 1,
    "cancelOrigClientOrderId": "myOrder1",
    "cancelNewClientOrderId": "cancelMyOrder1",
    "side": "BUY",
    "type": "MARKET",
    "timeInForce": "GTC",
    "price": 1,
    "quantity": 1,
    "quoteOrderQty": 1,
    "newClientOrderId": "myOrder2",
    "newOrderRespType": "ACK",
    "stopPrice": 1,
    "trailingDelta": 1,
    "icebergQty": 1,
    "strategyId": 1,
    "strategyType": 1,
    "selfTradePreventionMode": "NONE",
    "cancelRestrictions": "ONLY_NEW",
    "orderRateLimitExceededMode": "DO_NOTHING",
    "pegPriceType": "PRIMARY_PEG",
    "pegOffsetValue": 1,
    "pegOffsetType": "PRICE_LEVEL",
    "quoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel and replace order / 撤消挂单再下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `99de1036-b5e2-4e0f-9b5c-13d751c93a1a` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.cancelResult | string |  | 例: `SUCCESS` |
| result.newOrderResult | string |  | 例: `SUCCESS` |
| result.cancelResponse | object |  | Format is identical to "order.cancel" format.<br>Some fields are optional and are included only for orders that set them.<br>格式与 "order.cancel" 格式相同。<br>某些字段是可选的，仅在订单中有设置它们时才包括。 |
| result.cancelResponse.symbol | string |  | 例: `BTCUSDT` |
| result.cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `4d96324ff9d44481926157` |
| result.cancelResponse.orderId | integer (int64) |  | 例: `125690984230` |
| result.cancelResponse.orderListId | integer (int64) |  | 例: `-1` |
| result.cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `91fe37ce9e69c90d6358c0` |
| result.cancelResponse.transactTime | integer (int64) |  | 例: `1684804350068` |
| result.cancelResponse.price | string |  | 例: `23450.00000000` |
| result.cancelResponse.origQty | string |  | 例: `0.00847000` |
| result.cancelResponse.executedQty | string |  | 例: `0.00001000` |
| result.cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| result.cancelResponse.cummulativeQuoteQty | string |  | 例: `0.23450000` |
| result.cancelResponse.status | string |  | 例: `CANCELED` |
| result.cancelResponse.timeInForce | string |  | 例: `GTC` |
| result.cancelResponse.type | string |  | 例: `LIMIT` |
| result.cancelResponse.side | string |  | 例: `SELL` |
| result.cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| result.cancelResponse.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.cancelResponse.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.cancelResponse.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.cancelResponse.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result.cancelResponse.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.cancelResponse.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.cancelResponse.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.cancelResponse.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.cancelResponse.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.cancelResponse.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.cancelResponse.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.cancelResponse.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.cancelResponse.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.cancelResponse.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.cancelResponse.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| result.newOrderResponse | object |  | Format is identical to "order.place" format, affected by "newOrderRespType".<br>Some fields are optional and are included only for orders that set them.<br>格式与 "order.place" 格式相同, 受 "newOrderRespType" 影响。<br>某些字段是可选的，仅在订单中有设置它们时才包括。 |
| result.newOrderResponse.symbol | string |  | 例: `BTCUSDT` |
| result.newOrderResponse.orderId | integer (int64) |  | 例: `12569099453` |
| result.newOrderResponse.orderListId | integer (int64) |  | 例: `-1` |
| result.newOrderResponse.clientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| result.newOrderResponse.transactTime | integer (int64) |  | 例: `1660813156959` |
| result.newOrderResponse.price | string |  | 例: `23416.10000000` |
| result.newOrderResponse.origQty | string |  | 例: `0.00847000` |
| result.newOrderResponse.executedQty | string |  | 例: `0.00000000` |
| result.newOrderResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| result.newOrderResponse.cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.newOrderResponse.status | string |  | 例: `NEW` |
| result.newOrderResponse.timeInForce | string |  | 例: `GTC` |
| result.newOrderResponse.type | string |  | 例: `LIMIT` |
| result.newOrderResponse.side | string |  | 例: `SELL` |
| result.newOrderResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| result.newOrderResponse.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.newOrderResponse.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.newOrderResponse.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.newOrderResponse.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result.newOrderResponse.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.newOrderResponse.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.newOrderResponse.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.newOrderResponse.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.newOrderResponse.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.newOrderResponse.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.newOrderResponse.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.newOrderResponse.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.newOrderResponse.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.newOrderResponse.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.newOrderResponse.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

### 响应 Unsuccessful Response (400)：Order cancel-replace failed / 撤消挂单再下单失败

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `27e1bf9f-0539-4fb0-85c6-06183d36f66c` |
| (oneOf 1).status | integer (int64) |  | 例: `400` |
| (oneOf 1).error | object |  |  |
| (oneOf 1).error.code | integer (int64) |  | 例: `-2022` |
| (oneOf 1).error.msg | string |  | 例: `Order cancel-replace failed.` |
| (oneOf 1).error.data | object |  |  |
| (oneOf 1).error.data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 1).error.data.newOrderResult | string |  | 例: `NOT_ATTEMPTED` |
| (oneOf 1).error.data.cancelResponse | object |  |  |
| (oneOf 1).error.data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 1).error.data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 1).error.data.newOrderResponse |  |  | 例: `None` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `3b3ac45c-1002-4c7d-88e8-630c408ecd87` |
| (oneOf 2).status | integer (int64) |  | 例: `400` |
| (oneOf 2).error | object |  |  |
| (oneOf 2).error.code | integer (int64) |  | 例: `-2022` |
| (oneOf 2).error.msg | string |  | 例: `Order cancel-replace failed.` |
| (oneOf 2).error.data | object |  |  |
| (oneOf 2).error.data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 2).error.data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 2).error.data.cancelResponse | object |  |  |
| (oneOf 2).error.data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 2).error.data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 2).error.data.newOrderResponse | object |  |  |
| (oneOf 2).error.data.newOrderResponse.code | integer (int64) |  | 例: `-2010` |
| (oneOf 2).error.data.newOrderResponse.msg | string |  | 例: `Order would immediately match and take.` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `1` |

### 响应 Unsuccessful Response (409)：Order cancel-replace partially failed / 撤消挂单再下单部分失败

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `b220edfe-f3c4-4a3a-9d13-b35473783a25` |
| (oneOf 1).status | integer (int64) |  | 例: `409` |
| (oneOf 1).error | object |  |  |
| (oneOf 1).error.code | integer (int64) |  | 例: `-2021` |
| (oneOf 1).error.msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 1).error.data | object |  |  |
| (oneOf 1).error.data.cancelResult | string |  | 例: `SUCCESS` |
| (oneOf 1).error.data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 1).error.data.cancelResponse | object |  |  |
| (oneOf 1).error.data.cancelResponse.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).error.data.cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `4d96324ff9d44481926157` |
| (oneOf 1).error.data.cancelResponse.orderId | integer (int64) |  | 例: `125690984230` |
| (oneOf 1).error.data.cancelResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 1).error.data.cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `91fe37ce9e69c90d6358c0` |
| (oneOf 1).error.data.cancelResponse.transactTime | integer (int64) |  | 例: `1684804350068` |
| (oneOf 1).error.data.cancelResponse.price | string |  | 例: `23450.00000000` |
| (oneOf 1).error.data.cancelResponse.origQty | string |  | 例: `0.00847000` |
| (oneOf 1).error.data.cancelResponse.executedQty | string |  | 例: `0.00001000` |
| (oneOf 1).error.data.cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 1).error.data.cancelResponse.cummulativeQuoteQty | string |  | 例: `0.23450000` |
| (oneOf 1).error.data.cancelResponse.status | string |  | 例: `CANCELED` |
| (oneOf 1).error.data.cancelResponse.timeInForce | string |  | 例: `GTC` |
| (oneOf 1).error.data.cancelResponse.type | string |  | 例: `LIMIT` |
| (oneOf 1).error.data.cancelResponse.side | string |  | 例: `SELL` |
| (oneOf 1).error.data.cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 1).error.data.newOrderResponse | object |  |  |
| (oneOf 1).error.data.newOrderResponse.code | integer (int64) |  | 例: `-2010` |
| (oneOf 1).error.data.newOrderResponse.msg | string |  | 例: `Order would immediately match and take.` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `ce641763-ff74-41ac-b9f7-db7cbe5e93b1` |
| (oneOf 2).status | integer (int64) |  | 例: `409` |
| (oneOf 2).error | object |  |  |
| (oneOf 2).error.code | integer (int64) |  | 例: `-2021` |
| (oneOf 2).error.msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 2).error.data | object |  |  |
| (oneOf 2).error.data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 2).error.data.newOrderResult | string |  | 例: `SUCCESS` |
| (oneOf 2).error.data.cancelResponse | object |  |  |
| (oneOf 2).error.data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 2).error.data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 2).error.data.newOrderResponse | object |  |  |
| (oneOf 2).error.data.newOrderResponse.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).error.data.newOrderResponse.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 2).error.data.newOrderResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 2).error.data.newOrderResponse.clientOrderId | string |  | 例: `bX5wROblo6YeDwa9iTLeyY` |
| (oneOf 2).error.data.newOrderResponse.transactTime | integer (int64) |  | 例: `1660813156959` |
| (oneOf 2).error.data.newOrderResponse.price | string |  | 例: `23416.10000000` |
| (oneOf 2).error.data.newOrderResponse.origQty | string |  | 例: `0.00847000` |
| (oneOf 2).error.data.newOrderResponse.executedQty | string |  | 例: `0.00000000` |
| (oneOf 2).error.data.newOrderResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 2).error.data.newOrderResponse.cummulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 2).error.data.newOrderResponse.status | string |  | 例: `NEW` |
| (oneOf 2).error.data.newOrderResponse.timeInForce | string |  | 例: `GTC` |
| (oneOf 2).error.data.newOrderResponse.type | string |  | 例: `LIMIT` |
| (oneOf 2).error.data.newOrderResponse.side | string |  | 例: `SELL` |
| (oneOf 2).error.data.newOrderResponse.workingTime | integer (int64) |  | 例: `1669693344508` |
| (oneOf 2).error.data.newOrderResponse.fills | array |  |  |
| (oneOf 2).error.data.newOrderResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 3).id | string |  | 例: `3b3ac45c-1002-4c7d-88e8-630c408ecd87` |
| (oneOf 3).status | integer (int64) |  | 例: `409` |
| (oneOf 3).error | object |  |  |
| (oneOf 3).error.code | integer (int64) |  | 例: `-2021` |
| (oneOf 3).error.msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 3).error.data | object |  |  |
| (oneOf 3).error.data.cancelResult | string |  | 例: `SUCCESS` |
| (oneOf 3).error.data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 3).error.data.cancelResponse | object |  |  |
| (oneOf 3).error.data.cancelResponse.symbol | string |  | 例: `LTCBNB` |
| (oneOf 3).error.data.cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `GKt5zzfOxRDSQLveDYCTkc` |
| (oneOf 3).error.data.cancelResponse.orderId | integer (int64) |  | 例: `64` |
| (oneOf 3).error.data.cancelResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 3).error.data.cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `loehOJF3FjoreUBDmv739R` |
| (oneOf 3).error.data.cancelResponse.transactTime | integer (int64) |  | 例: `1715779007228` |
| (oneOf 3).error.data.cancelResponse.price | string |  | 例: `1.00` |
| (oneOf 3).error.data.cancelResponse.origQty | string |  | 例: `10.00000000` |
| (oneOf 3).error.data.cancelResponse.executedQty | string |  | 例: `0.00000000` |
| (oneOf 3).error.data.cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 3).error.data.cancelResponse.cummulativeQuoteQty | string |  | 例: `0.00` |
| (oneOf 3).error.data.cancelResponse.status | string |  | 例: `CANCELED` |
| (oneOf 3).error.data.cancelResponse.timeInForce | string |  | 例: `GTC` |
| (oneOf 3).error.data.cancelResponse.type | string |  | 例: `LIMIT` |
| (oneOf 3).error.data.cancelResponse.side | string |  | 例: `SELL` |
| (oneOf 3).error.data.cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 3).error.data.newOrderResponse | object |  |  |
| (oneOf 3).error.data.newOrderResponse.code | integer (int64) |  | 例: `-1015` |
| (oneOf 3).error.data.newOrderResponse.msg | string |  | 例: `Too many orders placed without trading; current limit is 50 non-trading orders per 10 SECOND. Unable to place new orders until trades occur or window resets.` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `50` |

### 响应 Unsuccessful Response (429)：Too many new orders / 新订单过多

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `3b3ac45c-1002-4c7d-88e8-630c408ecd87` |
| status | integer (int64) |  | 例: `429` |
| error | object |  |  |
| error.code | integer (int64) |  | 例: `-1015` |
| error.msg | string |  | 例: `Too many orders placed without trading; current limit is 50 non-trading orders per 10 SECOND. Unable to place new orders until trades occur or window resets.` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| rateLimits[].interval | string |  | 例: `SECOND` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| rateLimits[].limit | integer (int64) |  | 例: `50` |
| rateLimits[].count | integer (int64) |  | 例: `50` |

## Cancel Order list (TRADE)（撤销订单列表订单 (TRADE)）

`POST /orderList.cancel`

Cancel an active order list.

取消整个订单列表。

Operation ID: `orderListCancel`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.cancel`<br>例: `orderList.cancel` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.orderListId | integer |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| params.listClientOrderId | string |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `C3wyj4WVEktd7u9aVBRXcN` |
| params.newClientOrderId | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `cancelMyOrder1` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.cancel",
  "params": {
    "symbol": "BNBUSDT",
    "orderListId": 1,
    "listClientOrderId": "C3wyj4WVEktd7u9aVBRXcN",
    "newClientOrderId": "cancelMyOrder1",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel Order list / 撤销订单列表订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `c5899911-d3f4-47ae-8835-97da553d27d0` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `1274512` |
| result.contingencyType | string |  | 例: `OCO` |
| result.listStatusType | string |  | 例: `ALL_DONE` |
| result.listOrderStatus | string |  | 例: `ALL_DONE` |
| result.listClientOrderId | string |  | 例: `6023531d7edaad348f5aff` |
| result.transactionTime | integer (int64) |  | 例: `1660801720215` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `BTCUSDT` |
| result.orders[].orderId | integer (int64) |  | 例: `12569138901` |
| result.orders[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `BTCUSDT` |
| result.orderReports[].orderId | integer (int64) |  | 例: `12569138901` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `1274512` |
| result.orderReports[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1660801720215` |
| result.orderReports[].price | string |  | 例: `23410.00000000` |
| result.orderReports[].origQty | string |  | 例: `0.00650000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `CANCELED` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| result.orderReports[].side | string |  | 例: `SELL` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `23405.00000000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Place new OCO - Deprecated (TRADE)（OCO下单 - 已弃用 (TRADE)）

`POST /orderList.place`

Send in a new one-cancels-the-other (OCO) pair:
`LIMIT_MAKER` + `STOP_LOSS`/`STOP_LOSS_LIMIT` orders (called *legs*),
where activation of one order immediately cancels the other.

This adds 1 order to `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter

发送新的OCO(one-cancels-the-other) 订单:
`LIMIT_MAKER` 订单 + `STOP_LOSS`/`STOP_LOSS_LIMIT` 订单(称呼为 *legs*), 其中一个订单的激活会立即取消另一个订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderListPlace`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place`<br>例: `orderList.place` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.price | number (float) | 是 | 例: `1` |
| params.quantity | number (float) | 是 | 例: `1` |
| params.listClientOrderId | string |  | A unique Id for the entire orderList<br>整个orderList的唯一ID<br>例: `08985fedd9ea2cf6b28996` |
| params.limitClientOrderId | string |  | A unique Id for the limit order<br>限价单的唯一ID<br>例: `limitOrder1` |
| params.limitIcebergQty | number (float) |  | Used to make the `LIMIT_MAKER` leg an iceberg order.<br>用于使 `LIMIT_MAKER` 腿单成为冰山订单。<br>例: `1` |
| params.limitStrategyId | integer (int64) |  | 例: `1` |
| params.limitStrategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`<br>例: `1` |
| params.stopPrice | number (float) |  | 例: `1` |
| params.trailingDelta | integer |  | 例: `1` |
| params.stopClientOrderId | string |  | A unique Id for the stop loss/stop loss limit leg<br>止损/止损限价单的唯一ID<br>例: `stopOrder1` |
| params.stopLimitPrice | number (float) |  | If provided, `stopLimitTimeInForce` is required.<br>如果提供，须配合提交`stopLimitTimeInForce`<br>例: `1` |
| params.stopLimitTimeInForce | string |  | Valid values are `GTC`/`FOK`/`IOC`<br>有效值 `GTC`/`FOK`/`IOC`<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.stopIcebergQty | number (float) |  | Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.<br>与 `STOP_LOSS_LIMIT` 腿单一起使用，使其成为冰山订单。<br>例: `1` |
| params.stopStrategyId | integer (int64) |  | 例: `1` |
| params.stopStrategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`<br>例: `1` |
| params.newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place",
  "params": {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "price": 1,
    "quantity": 1,
    "listClientOrderId": "08985fedd9ea2cf6b28996",
    "limitClientOrderId": "limitOrder1",
    "limitIcebergQty": 1,
    "limitStrategyId": 1,
    "limitStrategyType": 1,
    "stopPrice": 1,
    "trailingDelta": 1,
    "stopClientOrderId": "stopOrder1",
    "stopLimitPrice": 1,
    "stopLimitTimeInForce": "GTC",
    "stopIcebergQty": 1,
    "stopStrategyId": 1,
    "stopStrategyType": 1,
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new OCO - Deprecated / OCO下单 - 已弃用

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `57833dc0-e3f2-43fb-ba20-46480973b0aa` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `1274512` |
| result.contingencyType | string |  | 例: `OCO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `08985fedd9ea2cf6b28996` |
| result.transactionTime | integer (int64) |  | 例: `1660801713793` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `BTCUSDT` |
| result.orders[].orderId | integer (int64) |  | 例: `12569138901` |
| result.orders[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `BTCUSDT` |
| result.orderReports[].orderId | integer (int64) |  | 例: `12569138901` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `1274512` |
| result.orderReports[].clientOrderId | string |  | 例: `BqtFCj5odMoWtSqGk2X9tU` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1660801713793` |
| result.orderReports[].price | string |  | 例: `23410.00000000` |
| result.orderReports[].origQty | string |  | 例: `0.00650000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| result.orderReports[].side | string |  | 例: `SELL` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `-1` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `23405.00000000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Place new Order list - OCO (TRADE)（发送新 OCO 订单 (TRADE)）

`POST /orderList.place.oco`

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

* An OCO has 2 orders called the **above order** and **below order**.

* One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be
`STOP_LOSS` or `STOP_LOSS_LIMIT` order.

* Price restrictions:
  * If the OCO is on the `SELL` side:
    * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT`
`stopPrice`
    * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT
stopPrice`
  * If the OCO is on the `BUY` side:
    * `LIMIT_MAKER` `price` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
*  OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

* OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单**。
* 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
* 针对价格限制：
  * 如果 OCO 订单方向是 `SELL`：
    * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT`
`stopPrice`
    * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
  * 如果 OCO 订单方向是 `BUY`：
    * `LIMIT_MAKER` `price` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
* OCO 将**2 个订单**添加到 `EXCHANGE_MAX_ORDERS`过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderListPlaceOco`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place.oco`<br>例: `orderList.place.oco` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowClientOrderId`.<br>整个 OCO order list 的唯一ID。 如果未发送则自动生成。 仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。 `listClientOrderId` 与 `aboveClientOrderId` 和 `belowClientOrderId` 不同。<br>例: `cKPMnDCbcLQILtDYM4f4fX` |
| params.side | string | 是 | `BUY` or `SELL`<br>订单方向：`BUY` or `SELL`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.quantity | number (float) | 是 | Quantity for both orders of the order list.<br>两个订单的数量。<br>例: `1` |
| params.aboveType | string | 是 | 枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| params.aboveClientOrderId | string |  | Arbitrary unique ID among open orders for the above order. Automatically generated if not sent.<br>上方订单的唯一ID。 如果未发送则自动生成。<br>例: `aboveOrder1` |
| params.aboveIcebergQty | number (float) |  | Note that this can only be used if `aboveTimeInForce` is `GTC`.<br>请注意，只有当 `aboveTimeInForce` 为 `GTC` 时才能使用。<br>例: `1` |
| params.abovePrice | number (float) |  | Can be used if `aboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1.5` |
| params.aboveStopPrice | number (float) |  | Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.<br>如果 `aboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `aboveStopPrice` 或 `aboveTrailingDelta` 或两者。<br>例: `1.50000001` |
| params.aboveTrailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.aboveTimeInForce | string |  | Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `aboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.aboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the above order within an order strategy.<br>订单策略中上方订单的 ID。<br>例: `1` |
| params.aboveStrategyType | integer |  | Arbitrary numeric value identifying the above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>上方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.abovePegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.abovePegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.abovePegOffsetValue | integer |  | 例: `1` |
| params.belowType | string | 是 | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持值：`STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`。<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| params.belowClientOrderId | string |  | Arbitrary unique ID among open orders for the below order. Automatically generated if not sent.<br>下方订单的唯一ID。 如果未发送则自动生成。<br>例: `belowOrder1` |
| params.belowIcebergQty | number (float) |  | Note that this can only be used if `belowTimeInForce` is `GTC`.<br>请注意，只有当 `belowTimeInForce` 为 `GTC` 时才能使用。<br>例: `1` |
| params.belowPrice | number (float) |  | Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1.49999999` |
| params.belowStopPrice | number (float) |  | Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.<br>如果 `belowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `belowStopPrice` 或 `belowTrailingDelta` 或两者。<br>例: `1.50000001` |
| params.belowTrailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.belowTimeInForce | string |  | Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `belowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.belowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the below order within an order strategy.<br>订单策略中下方订单的 ID。<br>例: `1` |
| params.belowStrategyType | integer |  | Arbitrary numeric value identifying the below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>下方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.belowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.belowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.belowPegOffsetValue | integer |  | 例: `1` |
| params.newOrderRespType | string |  | Select response format: `ACK`, `RESULT`, `FULL`.<br>响应格式可选值: `ACK`, `RESULT`, `FULL`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对上的配置。 支持值：[STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.aboveQuoteNotionalLimit | number (float) |  | Quote notional limit for the above order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.belowQuoteNotionalLimit | number (float) |  | Quote notional limit for the below order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place.oco",
  "params": {
    "symbol": "BNBUSDT",
    "listClientOrderId": "cKPMnDCbcLQILtDYM4f4fX",
    "side": "BUY",
    "quantity": 1,
    "aboveType": "STOP_LOSS_LIMIT",
    "aboveClientOrderId": "aboveOrder1",
    "aboveIcebergQty": 1,
    "abovePrice": 1.5,
    "aboveStopPrice": 1.50000001,
    "aboveTrailingDelta": 1,
    "aboveTimeInForce": "GTC",
    "aboveStrategyId": 1,
    "aboveStrategyType": 1,
    "abovePegPriceType": "PRIMARY_PEG",
    "abovePegOffsetType": "PRICE_LEVEL",
    "abovePegOffsetValue": 1,
    "belowType": "STOP_LOSS",
    "belowClientOrderId": "belowOrder1",
    "belowIcebergQty": 1,
    "belowPrice": 1.49999999,
    "belowStopPrice": 1.50000001,
    "belowTrailingDelta": 1,
    "belowTimeInForce": "GTC",
    "belowStrategyId": 1,
    "belowStrategyType": 1,
    "belowPegPriceType": "PRIMARY_PEG",
    "belowPegOffsetType": "PRICE_LEVEL",
    "belowPegOffsetValue": 1,
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "aboveQuoteNotionalLimit": 100,
    "belowQuoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new Order list - OCO / 发送新 OCO 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `56374a46-3261-486b-a211-99ed972eb648` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `2` |
| result.contingencyType | string |  | 例: `OCO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `cKPMnDCbcLQILtDYM4f4fX` |
| result.transactionTime | integer (int64) |  | 例: `1711062760648` |
| result.symbol | string |  | 例: `LTCBNB` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `LTCBNB` |
| result.orders[].orderId | integer (int64) |  | 例: `2` |
| result.orders[].clientOrderId | string |  | 例: `0m6I4wfxvTUrOBSMUl0OPU` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `LTCBNB` |
| result.orderReports[].orderId | integer (int64) |  | 例: `2` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `2` |
| result.orderReports[].clientOrderId | string |  | 例: `0m6I4wfxvTUrOBSMUl0OPU` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1711062760648` |
| result.orderReports[].price | string |  | 例: `1.50000000` |
| result.orderReports[].origQty | string |  | 例: `1.000000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| result.orderReports[].side | string |  | 例: `BUY` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `-1` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `1.50000001` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## OPO (TRADE)（新订单列表 - OPO (TRADE)）

`POST /orderList.place.opo`

Place an [OPO](/products/spot/faqs/opo).

* The working order must be `LIMIT` or `LIMIT_MAKER`.
* OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.

发送一个 [OPO](/products/spot/faqs/opo) 订单。

* 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
* OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。

Operation ID: `orderListPlaceOpo`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place.opo`<br>例: `orderList.place.opo` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。<br>例: `OiOgqvRagBefpzdM5gjYX3` |
| params.newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值：`LIMIT`，`LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `workingOrder1` |
| params.workingPrice | number (float) | 是 | Price for the working order.<br>生效订单价格<br>例: `1` |
| params.workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>设置生效订单的数量<br>例: `1` |
| params.workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| params.workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>用于标识订单策略中生效订单的任意数字值<br>例: `1` |
| params.workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| params.workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.workingPegOffsetValue | integer |  | 例: `1` |
| params.pendingType | string | 是 | Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using `quoteOrderQty` are not supported.<br>支持的数值：[订单类型](/products/spot/enums#ordertypes)。注意，不支持使用 `quoteOrderQty` 的 `MARKET` 订单。<br>枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.pendingClientOrderId | string |  | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>待处理订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingOrder1` |
| params.pendingPrice | number (float) |  | Price for the pending order.<br>待处理订单价格<br>例: `1` |
| params.pendingStopPrice | number (float) |  | Stop price for the pending order.<br>待处理订单止损价格<br>例: `1` |
| params.pendingTrailingDelta | number (float) |  | Trailing delta for the pending order.<br>待处理订单跟踪止损差值<br>例: `1` |
| params.pendingIcebergQty | number (float) |  | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.<br>仅当 `pendingTimeInForce` 为 `GTC` 或 `pendingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| params.pendingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending order within an order strategy.<br>用于标识订单策略中待处理订单的任意数字值<br>例: `1` |
| params.pendingStrategyType | integer |  | Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| params.pendingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingPegOffsetValue | integer |  | 例: `1` |
| params.workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place.opo",
  "params": {
    "symbol": "BNBUSDT",
    "listClientOrderId": "OiOgqvRagBefpzdM5gjYX3",
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingClientOrderId": "workingOrder1",
    "workingPrice": 1,
    "workingQuantity": 1,
    "workingIcebergQty": 1,
    "workingTimeInForce": "GTC",
    "workingStrategyId": 1,
    "workingStrategyType": 1,
    "workingPegPriceType": "PRIMARY_PEG",
    "workingPegOffsetType": "PRICE_LEVEL",
    "workingPegOffsetValue": 1,
    "pendingType": "LIMIT",
    "pendingSide": "BUY",
    "pendingClientOrderId": "pendingOrder1",
    "pendingPrice": 1,
    "pendingStopPrice": 1,
    "pendingTrailingDelta": 1,
    "pendingIcebergQty": 1,
    "pendingTimeInForce": "GTC",
    "pendingStrategyId": 1,
    "pendingStrategyType": 1,
    "pendingPegPriceType": "PRIMARY_PEG",
    "pendingPegOffsetType": "PRICE_LEVEL",
    "pendingPegOffsetValue": 1,
    "workingQuoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：OPO / 请参见英文说明：OPO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `eabb220d-1c53-4f8a-8bca-a1cd3594b3ce` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `2` |
| result.contingencyType | string |  | 例: `OTO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `OiOgqvRagBefpzdM5gjYX3` |
| result.transactionTime | integer (int64) |  | 例: `1762941318142` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `BTCUSDT` |
| result.orders[].orderId | integer (int64) |  | 例: `2` |
| result.orders[].clientOrderId | string |  | 例: `pUzhKBbc0ZVdMScIRAqitH` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `BTCUSDT` |
| result.orderReports[].orderId | integer (int64) |  | 例: `2` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `2` |
| result.orderReports[].clientOrderId | string |  | 例: `pUzhKBbc0ZVdMScIRAqitH` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1762941318142` |
| result.orderReports[].price | string |  | 例: `101496.00000000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `LIMIT` |
| result.orderReports[].side | string |  | 例: `BUY` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `1762941318142` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].origQty | string |  | 例: `0.00070000` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## OPOCO (TRADE)（新订单列表 - OPOCO (TRADE)）

`POST /orderList.place.opoco`

Place an [OPOCO](/products/spot/faqs/opo).

* The working order must be `LIMIT` or `LIMIT_MAKER`.

发送一个 [OPOCO](/products/spot/faqs/opo) 订单。

* 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。

Operation ID: `orderListPlaceOpoco`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place.opoco`<br>例: `orderList.place.opoco` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.<br>订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。<br>例: `TVbG6ymkYMXTj7tczbOsBf` |
| params.newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值：`LIMIT`，`LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `workingOrder1` |
| params.workingPrice | number (float) | 是 | Price for the working order.<br>生效订单价格<br>例: `1` |
| params.workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>设置生效订单的数量<br>例: `1` |
| params.workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| params.workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>用于标识订单策略中生效订单的任意数字值<br>例: `1` |
| params.workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| params.workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.workingPegOffsetType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.workingPegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| params.pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.pendingAboveType | string | 是 | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| params.pendingAboveClientOrderId | string |  | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>待处理"上方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingAboveOrder1` |
| params.pendingAbovePrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingAboveType` 为 `STOP_LOSS_LIMIT`、`LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。<br>例: `1` |
| params.pendingAboveStopPrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.<br>当 `pendingAboveType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT`、`TAKE_PROFIT_LIMIT` 时可用。<br>例: `1` |
| params.pendingAboveTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.pendingAboveIcebergQty | number (float) |  | This can only be used if `pendingAboveTimeInForce` is `GTC` or `pendingAboveType` is `LIMIT_MAKER`.<br>仅当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时可用。<br>例: `1` |
| params.pendingAboveTimeInForce | string |  | Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingAboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending above order within an order strategy.<br>用于标识订单策略中待处理上方订单的任意数字值。<br>例: `1` |
| params.pendingAboveStrategyType | integer |  | Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理上方订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| params.pendingAbovePegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingAbovePegOffsetType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingAbovePegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| params.pendingBelowType | string |  | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值：`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| params.pendingBelowClientOrderId | string |  | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>待处理"下方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingBelowOrder1` |
| params.pendingBelowPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。<br>例: `1` |
| params.pendingBelowStopPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.<br>当 `pendingBelowType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 时可用。`pendingBelowStopPrice`、`pendingBelowTrailingDelta` 或两者之一必须被指定。<br>例: `1` |
| params.pendingBelowTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.pendingBelowIcebergQty | number (float) |  | This can only be used if `pendingBelowTimeInForce` is `GTC` or `pendingBelowType` is `LIMIT_MAKER`.<br>仅当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时可用。<br>例: `1` |
| params.pendingBelowTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingBelowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending below order within an order strategy.<br>用于标识订单策略中待处理下方订单的任意数字值。<br>例: `1` |
| params.pendingBelowStrategyType | integer |  | Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理下方订单策略的任意数字值。小于 `1000000` 为保留值，不能使用。<br>例: `1` |
| params.pendingBelowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingBelowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingBelowPegOffsetValue | integer |  | 例: `1` |
| params.workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place.opoco",
  "params": {
    "symbol": "BNBUSDT",
    "listClientOrderId": "TVbG6ymkYMXTj7tczbOsBf",
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingClientOrderId": "workingOrder1",
    "workingPrice": 1,
    "workingQuantity": 1,
    "workingIcebergQty": 1,
    "workingTimeInForce": "GTC",
    "workingStrategyId": 1,
    "workingStrategyType": 1,
    "workingPegPriceType": "PRIMARY_PEG",
    "workingPegOffsetType": "PRICE_LEVEL",
    "workingPegOffsetValue": 1,
    "pendingSide": "BUY",
    "pendingAboveType": "STOP_LOSS_LIMIT",
    "pendingAboveClientOrderId": "pendingAboveOrder1",
    "pendingAbovePrice": 1,
    "pendingAboveStopPrice": 1,
    "pendingAboveTrailingDelta": 1,
    "pendingAboveIcebergQty": 1,
    "pendingAboveTimeInForce": "GTC",
    "pendingAboveStrategyId": 1,
    "pendingAboveStrategyType": 1,
    "pendingAbovePegPriceType": "PRIMARY_PEG",
    "pendingAbovePegOffsetType": "PRICE_LEVEL",
    "pendingAbovePegOffsetValue": 1,
    "pendingBelowType": "STOP_LOSS",
    "pendingBelowClientOrderId": "pendingBelowOrder1",
    "pendingBelowPrice": 1,
    "pendingBelowStopPrice": 1,
    "pendingBelowTrailingDelta": 1,
    "pendingBelowIcebergQty": 1,
    "pendingBelowTimeInForce": "GTC",
    "pendingBelowStrategyId": 1,
    "pendingBelowStrategyType": 1,
    "pendingBelowPegPriceType": "PRIMARY_PEG",
    "pendingBelowPegOffsetType": "PRICE_LEVEL",
    "pendingBelowPegOffsetValue": 1,
    "workingQuoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：OPOCO / 请参见英文说明：OPOCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `606063bf-43ea-40a6-a463-5c66fbd53b56` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `1` |
| result.contingencyType | string |  | 例: `OTO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `TVbG6ymkYMXTj7tczbOsBf` |
| result.transactionTime | integer (int64) |  | 例: `1763000139104` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `BTCUSDT` |
| result.orders[].orderId | integer (int64) |  | 例: `6` |
| result.orders[].clientOrderId | string |  | 例: `3czuJSeyjPwV9Xo28j1Dv3` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `BTCUSDT` |
| result.orderReports[].orderId | integer (int64) |  | 例: `6` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `1` |
| result.orderReports[].clientOrderId | string |  | 例: `3czuJSeyjPwV9Xo28j1Dv3` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1763000139104` |
| result.orderReports[].price | string |  | 例: `102496.00000000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `LIMIT` |
| result.orderReports[].side | string |  | 例: `BUY` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `1763000139104` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `10100.00000000` |
| result.orderReports[].origQty | string |  | 例: `0.00170000` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## Place new Order list - OTO (TRADE)（发送新订单列表 - OTO (TRADE)）

`POST /orderList.place.oto`

Places an OTO.

* An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.

* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the
working order goes on the order book.

* The second order is called the **pending order**. It can be any order type except for `MARKET` orders using
parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets
**fully filled**.

* If either the working order or the pending order is cancelled individually, the other order in the order list
will also be canceled or expired.

* When the order list is placed, if the working order gets **immediately fully filled**, the placement response
will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to
query the status of the pending order again to see its updated status.

* OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 OTO 订单。


* 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.

* 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。

* 第二个订单被称为**待处理订单**。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET` 订单。只有当生效订单**完全成交**时，待处理订单才会被自动下单。

* 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。

* 如果生效订单在下订单列表后**立即完全成交**，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为
`PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。

* `OTO` 订单将**2 个订单**添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderListPlaceOto`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place.oto`<br>例: `orderList.place.oto` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。 `listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。<br>例: `KA4EBjGnzvSwSCQsDdTrlf` |
| params.newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值： `LIMIT`， `LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>用于标识生效订单的唯一ID。 如果未发送则自动生成。<br>例: `workingOrder1` |
| params.workingPrice | number (float) | 是 | 例: `1` |
| params.workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>用于设置生效订单的数量。<br>例: `1` |
| params.workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。<br>例: `1` |
| params.workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>订单策略中用于标识生效订单的 ID。<br>例: `1` |
| params.workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.workingPegOffsetValue | integer |  | 例: `1` |
| params.pendingType | string | 是 | Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using `quoteOrderQty` are not supported.<br>支持的数值： [订单类型](/products/spot/enums#ordertypes) 请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。<br>枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.pendingClientOrderId | string |  | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>用于标识待处理订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingOrder1` |
| params.pendingPrice | number (float) |  | 例: `1` |
| params.pendingStopPrice | number (float) |  | 例: `1` |
| params.pendingTrailingDelta | number (float) |  | 例: `1` |
| params.pendingQuantity | number (float) | 是 | Sets the quantity for the pending order.<br>用于设置待处理订单的数量。<br>例: `1` |
| params.pendingIcebergQty | number (float) |  | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.<br>只有当 `pendingTimeInForce` 为 `GTC` 或者当 `pendingType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| params.pendingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending order within an order strategy.<br>订单策略中用于标识待处理订单的 ID。<br>例: `1` |
| params.pendingStrategyType | integer |  | Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.pendingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingPegOffsetValue | integer |  | 例: `1` |
| params.workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.pendingQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place.oto",
  "params": {
    "symbol": "BNBUSDT",
    "listClientOrderId": "KA4EBjGnzvSwSCQsDdTrlf",
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingClientOrderId": "workingOrder1",
    "workingPrice": 1,
    "workingQuantity": 1,
    "workingIcebergQty": 1,
    "workingTimeInForce": "GTC",
    "workingStrategyId": 1,
    "workingStrategyType": 1,
    "workingPegPriceType": "PRIMARY_PEG",
    "workingPegOffsetType": "PRICE_LEVEL",
    "workingPegOffsetValue": 1,
    "pendingType": "LIMIT",
    "pendingSide": "BUY",
    "pendingClientOrderId": "pendingOrder1",
    "pendingPrice": 1,
    "pendingStopPrice": 1,
    "pendingTrailingDelta": 1,
    "pendingQuantity": 1,
    "pendingIcebergQty": 1,
    "pendingTimeInForce": "GTC",
    "pendingStrategyId": 1,
    "pendingStrategyType": 1,
    "pendingPegOffsetType": "PRICE_LEVEL",
    "pendingPegPriceType": "PRIMARY_PEG",
    "pendingPegOffsetValue": 1,
    "workingQuoteNotionalLimit": 100,
    "pendingQuoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new Order list - OTO / 发送新订单列表 - OTO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `1712544395950` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `626` |
| result.contingencyType | string |  | 例: `OTO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `KA4EBjGnzvSwSCQsDdTrlf` |
| result.transactionTime | integer (int64) |  | 例: `1712544395981` |
| result.symbol | string |  | 例: `LTCBNB` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `LTCBNB` |
| result.orders[].orderId | integer (int64) |  | 例: `13` |
| result.orders[].clientOrderId | string |  | 例: `YiAUtM9yJjl1a2jXHSp9Ny` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `LTCBNB` |
| result.orderReports[].orderId | integer (int64) |  | 例: `13` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `626` |
| result.orderReports[].clientOrderId | string |  | 例: `YiAUtM9yJjl1a2jXHSp9Ny` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1712544395981` |
| result.orderReports[].price | string |  | 例: `1.00000000` |
| result.orderReports[].origQty | string |  | 例: `1.000000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `LIMIT` |
| result.orderReports[].side | string |  | 例: `SELL` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `1712544395981` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Place new Order list - OTOCO (TRADE)（发送新订单列表 - OTOCO (TRADE)）

`POST /orderList.place.otoco`

Place an OTOCO.

* An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  * The behavior of the working order is the same as the [OTO](#order-list-place-oto).
* OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**.
  * The rules of the pending above and pending below follow the same rules as the [Order list OCO](/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oco).
* OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 OTOCO 订单。

* 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
* 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
  * 生效订单的行为与此一致 [OTO](#orderList-place-oto)
* 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交**时，待处理订单们才会被自动下单。
  * 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [OrderList OCO](/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oco)。
* `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单**。

Operation ID: `orderListPlaceOtoco`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `orderList.place.otoco`<br>例: `orderList.place.otoco` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.<br>整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。 `listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。<br>例: `GaeJHjZPasPItFj4x7Mqm6` |
| params.newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值： `LIMIT`， `LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| params.workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>用于标识生效订单的唯一ID。 如果未发送则自动生成。<br>例: `workingOrder1` |
| params.workingPrice | number (float) | 是 | 例: `1` |
| params.workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>用于设置生效订单的数量。<br>例: `1` |
| params.workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。<br>例: `1` |
| params.workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>订单策略中用于标识生效订单的 ID。<br>例: `1` |
| params.workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.workingPegOffsetValue | integer |  | 例: `1` |
| params.pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.pendingQuantity | number (float) | 是 | Sets the quantity for the pending orders.<br>用于设置待处理订单的数量。<br>例: `1` |
| params.pendingAboveType | string | 是 | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| params.pendingAboveClientOrderId | string |  | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>用于标识待处理上方订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingAboveOrder1` |
| params.pendingAbovePrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingAboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1` |
| params.pendingAboveStopPrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。<br>例: `1` |
| params.pendingAboveTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.pendingAboveIcebergQty | number (float) |  | This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.<br>只有当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| params.pendingAboveTimeInForce | string |  | Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingAboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending above order within an order strategy.<br>订单策略中用于标识待处理上方订单的 ID。<br>例: `1` |
| params.pendingAboveStrategyType | integer |  | Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理上方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.pendingAbovePegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingAbovePegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingAbovePegOffsetValue | integer |  | 例: `1` |
| params.pendingBelowType | string |  | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值： `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| params.pendingBelowClientOrderId | string |  | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>用于标识待处理下方订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingBelowOrder1` |
| params.pendingBelowPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1` |
| params.pendingBelowStopPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.<br>如果 `pendingBelowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `pendingBelowStopPrice` 或 `pendingBelowTrailingDelta` 或两者。<br>例: `1` |
| params.pendingBelowTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.pendingBelowIcebergQty | number (float) |  | This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.<br>只有当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| params.pendingBelowTimeInForce | string |  | Required if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.pendingBelowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending below order within an order strategy.<br>订单策略中用于标识待处理下方订单的 ID。<br>例: `1` |
| params.pendingBelowStrategyType | integer |  | Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理下方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| params.pendingBelowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pendingBelowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.pendingBelowPegOffsetValue | integer |  | 例: `1` |
| params.workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.pendingAboveQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending above order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.pendingBelowQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending below order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "orderList.place.otoco",
  "params": {
    "symbol": "BNBUSDT",
    "listClientOrderId": "GaeJHjZPasPItFj4x7Mqm6",
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "NONE",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingClientOrderId": "workingOrder1",
    "workingPrice": 1,
    "workingQuantity": 1,
    "workingIcebergQty": 1,
    "workingTimeInForce": "GTC",
    "workingStrategyId": 1,
    "workingStrategyType": 1,
    "workingPegPriceType": "PRIMARY_PEG",
    "workingPegOffsetType": "PRICE_LEVEL",
    "workingPegOffsetValue": 1,
    "pendingSide": "BUY",
    "pendingQuantity": 1,
    "pendingAboveType": "STOP_LOSS_LIMIT",
    "pendingAboveClientOrderId": "pendingAboveOrder1",
    "pendingAbovePrice": 1,
    "pendingAboveStopPrice": 1,
    "pendingAboveTrailingDelta": 1,
    "pendingAboveIcebergQty": 1,
    "pendingAboveTimeInForce": "GTC",
    "pendingAboveStrategyId": 1,
    "pendingAboveStrategyType": 1,
    "pendingAbovePegPriceType": "PRIMARY_PEG",
    "pendingAbovePegOffsetType": "PRICE_LEVEL",
    "pendingAbovePegOffsetValue": 1,
    "pendingBelowType": "STOP_LOSS",
    "pendingBelowClientOrderId": "pendingBelowOrder1",
    "pendingBelowPrice": 1,
    "pendingBelowStopPrice": 1,
    "pendingBelowTrailingDelta": 1,
    "pendingBelowIcebergQty": 1,
    "pendingBelowTimeInForce": "GTC",
    "pendingBelowStrategyId": 1,
    "pendingBelowStrategyType": 1,
    "pendingBelowPegPriceType": "PRIMARY_PEG",
    "pendingBelowPegOffsetType": "PRICE_LEVEL",
    "pendingBelowPegOffsetValue": 1,
    "workingQuoteNotionalLimit": 100,
    "pendingAboveQuoteNotionalLimit": 100,
    "pendingBelowQuoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new Order list - OTOCO / 发送新订单列表 - OTOCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `1712544408508` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderListId | integer (int64) |  | 例: `629` |
| result.contingencyType | string |  | 例: `OTO` |
| result.listStatusType | string |  | 例: `EXEC_STARTED` |
| result.listOrderStatus | string |  | 例: `EXECUTING` |
| result.listClientOrderId | string |  | 例: `GaeJHjZPasPItFj4x7Mqm6` |
| result.transactionTime | integer (int64) |  | 例: `1712544408537` |
| result.symbol | string |  | 例: `LTCBNB` |
| result.orders | object[] |  |  |
| result.orders[].symbol | string |  | 例: `LTCBNB` |
| result.orders[].orderId | integer (int64) |  | 例: `23` |
| result.orders[].clientOrderId | string |  | 例: `OVQOpKwfmPCfaBTD0n7e7H` |
| result.orderReports | object[] |  |  |
| result.orderReports[].symbol | string |  | 例: `LTCBNB` |
| result.orderReports[].orderId | integer (int64) |  | 例: `23` |
| result.orderReports[].orderListId | integer (int64) |  | 例: `629` |
| result.orderReports[].clientOrderId | string |  | 例: `OVQOpKwfmPCfaBTD0n7e7H` |
| result.orderReports[].transactTime | integer (int64) |  | 例: `1712544408537` |
| result.orderReports[].price | string |  | 例: `1.50000000` |
| result.orderReports[].origQty | string |  | 例: `1.000000` |
| result.orderReports[].executedQty | string |  | 例: `0.00000000` |
| result.orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result.orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| result.orderReports[].status | string |  | 例: `NEW` |
| result.orderReports[].timeInForce | string |  | 例: `GTC` |
| result.orderReports[].type | string |  | 例: `LIMIT` |
| result.orderReports[].side | string |  | 例: `BUY` |
| result.orderReports[].workingTime | integer (int64) |  | 例: `1712544408537` |
| result.orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| result.orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result.orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result.orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result.orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.500000` |
| result.orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result.orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result.orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result.orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result.orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result.orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result.orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result.orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result.orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result.orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result.orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Place new order (TRADE)（下新的订单 (TRADE)）

`POST /order.place`

Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

下新的订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderPlace`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.place`<br>例: `order.place` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| params.timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.price | number (float) |  | 例: `1` |
| params.quantity | number (float) |  | 例: `1` |
| params.quoteOrderQty | number (float) |  | 例: `1` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。<br>例: `myOrder1` |
| params.newOrderRespType | string |  | `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.<br>`MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。<br>例: `1` |
| params.trailingDelta | integer |  | See Trailing Stop order FAQ<br>参见 追踪止盈止损(Trailing Stop)订单常见问题<br>例: `1` |
| params.icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| params.strategyId | integer (int64) |  | 例: `1` |
| params.strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol.<br>允许的 ENUM 取决于交易对的配置。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.pegPriceType | string |  | See Pegged Orders Info<br>参阅 关于挂钩订单参数的注意事项<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pegOffsetValue | integer |  | Price level to peg the price to (max: 100). See Pegged Orders Info<br>用于挂钩的价格水平（最大值：100）。参阅 关于挂钩订单参数的注意事项<br>例: `1` |
| params.pegOffsetType | string |  | Only `PRICE_LEVEL` is supported. See Pegged Orders Info<br>仅支持 `PRICE_LEVEL`。参阅 关于挂钩订单参数的注意事项<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.quoteNotionalLimit | number (float) |  | For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.place",
  "params": {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "MARKET",
    "timeInForce": "GTC",
    "price": 1,
    "quantity": 1,
    "quoteOrderQty": 1,
    "newClientOrderId": "myOrder1",
    "newOrderRespType": "ACK",
    "stopPrice": 1,
    "trailingDelta": 1,
    "icebergQty": 1,
    "strategyId": 1,
    "strategyType": 1,
    "selfTradePreventionMode": "NONE",
    "pegPriceType": "PRIMARY_PEG",
    "pegOffsetValue": 1,
    "pegOffsetType": "PRICE_LEVEL",
    "quoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new order / 下新的订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `56374a46-3061-486b-a311-99ee972eb648` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 1).result.orderListId | integer (int64) |  | always -1 for singular orders<br>单个订单会一直是 -1<br>例: `-1` |
| (oneOf 1).result.clientOrderId | string |  | 例: `4d96324ff9d44481926157ec08158a40` |
| (oneOf 1).result.transactTime | integer (int64) |  | 例: `1660801715639` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `56374a46-3061-486b-a311-99ee972eb648` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 2).result.orderListId | integer (int64) |  | always -1 for singular orders<br>单个订单会一直是 -1<br>例: `-1` |
| (oneOf 2).result.clientOrderId | string |  | 例: `4d96324ff9d44481926157ec08158a40` |
| (oneOf 2).result.transactTime | integer (int64) |  | 例: `1660801715639` |
| (oneOf 2).result.price | string |  | 例: `23416.10000000` |
| (oneOf 2).result.origQty | string |  | 例: `0.00847000` |
| (oneOf 2).result.executedQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 2).result.cummulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 2).result.status | string |  | 例: `NEW` |
| (oneOf 2).result.timeInForce | string |  | 例: `GTC` |
| (oneOf 2).result.type | string |  | 例: `LIMIT` |
| (oneOf 2).result.side | string |  | 例: `SELL` |
| (oneOf 2).result.workingTime | integer (int64) |  | 例: `1660801715639` |
| (oneOf 2).result.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `SECOND` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `50` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 3).id | string |  | 例: `56374a46-3061-486b-a311-99ee972eb648` |
| (oneOf 3).status | integer (int64) |  | 例: `200` |
| (oneOf 3).result | object |  |  |
| (oneOf 3).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 3).result.orderId | integer (int64) |  | 例: `12569099453` |
| (oneOf 3).result.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 3).result.clientOrderId | string |  | 例: `4d96324ff9d44481926157ec08158a40` |
| (oneOf 3).result.transactTime | integer (int64) |  | 例: `1660801715793` |
| (oneOf 3).result.price | string |  | 例: `23416.10000000` |
| (oneOf 3).result.origQty | string |  | 例: `0.00847000` |
| (oneOf 3).result.executedQty | string |  | 例: `0.00847000` |
| (oneOf 3).result.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 3).result.cummulativeQuoteQty | string |  | 例: `198.33521500` |
| (oneOf 3).result.status | string |  | 例: `FILLED` |
| (oneOf 3).result.timeInForce | string |  | 例: `GTC` |
| (oneOf 3).result.type | string |  | 例: `LIMIT` |
| (oneOf 3).result.side | string |  | 例: `SELL` |
| (oneOf 3).result.workingTime | integer (int64) |  | 例: `1660801715639` |
| (oneOf 3).result.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 3).result.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| (oneOf 3).result.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| (oneOf 3).result.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| (oneOf 3).result.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| (oneOf 3).result.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| (oneOf 3).result.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| (oneOf 3).result.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| (oneOf 3).result.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| (oneOf 3).result.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| (oneOf 3).result.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| (oneOf 3).result.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| (oneOf 3).result.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| (oneOf 3).result.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| (oneOf 3).result.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| (oneOf 3).result.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| (oneOf 3).result.fills | object[] |  | FULL response is identical to RESULT response, with the same optional fields<br>based on the order type and parameters. FULL response additionally includes<br>the list of trades which immediately filled the order.<br>FULL 响应与 RESULT 响应相同，具有相同的可选字段基于订单类型和参数。FULL响应还包括立即完成订单的交易列表。 |
| (oneOf 3).result.fills[].price | string |  | 例: `23416.10000000` |
| (oneOf 3).result.fills[].qty | string |  | 例: `0.00635000` |
| (oneOf 3).result.fills[].commission | string |  | 例: `0.00000000` |
| (oneOf 3).result.fills[].commissionAsset | string |  | 例: `BNB` |
| (oneOf 3).result.fills[].tradeId | integer (int64) |  | 例: `1650422481` |
| (oneOf 3).rateLimits | object[] |  |  |
| (oneOf 3).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 3).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 3).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 3).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 3).rateLimits[].count | integer (int64) |  | 例: `1` |

## Test new order (TRADE)（测试下单 (TRADE)）

`POST /order.test`

Test order placement.

Validates new order parameters and verifies your signature
but does not send the order into the matching engine.

测试下单。

验证新订单参数并验证您的签名但不会将订单发送到撮合引擎。

权重: | Condition | Request Weight |
| --- | --- |
| Without `computeCommissionRates` | 1 |
| With `computeCommissionRates` | 20 |

Operation ID: `orderTest`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.test`<br>例: `order.test` |
| params | object | 是 |  |
| params.computeCommissionRates | boolean |  | Default: `false` <br> See [Commissions FAQ](/products/spot/faqs/commission_faq#test-order-diferences) to learn more.<br>默认值: `false` <br> 请参阅[佣金常见问题解答](/products/spot/faqs/commission_faq#test-order-diferences) 了解更多信息。<br>默认: `False`<br>例: `False` |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| params.timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.price | number (float) |  | 例: `1` |
| params.quantity | number (float) |  | 例: `1` |
| params.quoteOrderQty | number (float) |  | 例: `1` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。<br>例: `myOrder1` |
| params.newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.<br>指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。<br>例: `1` |
| params.trailingDelta | integer |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| params.icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| params.strategyId | integer (int64) |  | 例: `1` |
| params.strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.pegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| params.pegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| params.pegOffsetType | string |  | Only `PRICE_LEVEL` is supported. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>仅支持 `PRICE_LEVEL`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| params.quoteNotionalLimit | number (float) |  | For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "order.test",
  "params": {
    "computeCommissionRates": false,
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "MARKET",
    "timeInForce": "GTC",
    "price": 1,
    "quantity": 1,
    "quoteOrderQty": 1,
    "newClientOrderId": "myOrder1",
    "newOrderRespType": "ACK",
    "stopPrice": 1,
    "trailingDelta": 1,
    "icebergQty": 1,
    "strategyId": 1,
    "strategyType": 1,
    "selfTradePreventionMode": "NONE",
    "pegPriceType": "PRIMARY_PEG",
    "pegOffsetValue": 1,
    "pegOffsetType": "PRICE_LEVEL",
    "quoteNotionalLimit": 100,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Test new order / 测试下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `6ffebe91-01d9-43ac-be99-57cf062e0e30` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `6ffebe91-01d9-43ac-be99-57cf062e0e30` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.standardCommissionForOrder | object |  | Standard commission rates on trades from the order.<br>订单交易的标准佣金率。 |
| (oneOf 2).result.standardCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).result.standardCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).result.specialCommissionForOrder | object |  | Special commission rates on trades from the order.<br>订单交易的特殊佣金率。 |
| (oneOf 2).result.specialCommissionForOrder.maker | string |  | 例: `0.05000000` |
| (oneOf 2).result.specialCommissionForOrder.taker | string |  | 例: `0.06000000` |
| (oneOf 2).result.taxCommissionForOrder | object |  | Tax commission rates for trades from the order.<br>订单交易的税率。 |
| (oneOf 2).result.taxCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).result.taxCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).result.discount | object |  | Discount on standard commissions when paying in BNB.<br>以BNB支付时的标准佣金折扣。 |
| (oneOf 2).result.discount.enabledForAccount | boolean |  | 例: `True` |
| (oneOf 2).result.discount.enabledForSymbol | boolean |  | 例: `True` |
| (oneOf 2).result.discount.discountAsset | string |  | 例: `BNB` |
| (oneOf 2).result.discount.discount | string |  | Standard commission is reduced by this rate when paying commission in BNB.<br>当用BNB支付佣金时，在标准佣金上按此比率打折。<br>例: `0.25000000` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `20` |

## Place new order using SOR (TRADE)（下 SOR 订单 (TRADE)）

`POST /sor.order.place`

Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](/products/spot/faqs/sor_faq) to learn more.

发送使用智能订单路由 (SOR) 的新订单。这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

参阅 [智能订单路由 (SOR)](/products/spot/faqs/sor_faq) 了解更多详情。

Operation ID: `sorOrderPlace`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `sor.order.place`<br>例: `sor.order.place` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.side | string | 是 | `BUY` or `SELL`<br>`BUY` 或 `SELL`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.type | string | 是 | Only `LIMIT` and `MARKET` orders are supported.<br>仅支持 `LIMIT` 和 `MARKET` 订单。<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| params.timeInForce | string |  | Applicable only to `LIMIT` order type.<br>仅适用于 `LIMIT` 订单类型。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.price | number (float) |  | 例: `1` |
| params.quantity | number (float) | 是 | 例: `1` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，<br/>那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。<br>例: `myOrder1` |
| params.newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`<br>指定响应类型:<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.icebergQty | number (float) |  | Used with `LIMIT` to create an iceberg order.<br>仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| params.strategyId | integer (int64) |  | 例: `1` |
| params.strategyType | integer |  | The value cannot be less than `1000000`.<br>赋值不能小于 `1000000`.<br>例: `1` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/products/spot/enums#stpmodes).<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "sor.order.place",
  "params": {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "MARKET",
    "timeInForce": "GTC",
    "price": 1,
    "quantity": 1,
    "newClientOrderId": "myOrder1",
    "newOrderRespType": "ACK",
    "icebergQty": 1,
    "strategyId": 1,
    "strategyType": 1,
    "selfTradePreventionMode": "NONE",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Place new order using SOR / 下 SOR 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `3a4437e2-41a3-4c19-897c-9cadc5dce8b6` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].orderId | integer (int64) |  | 例: `2` |
| result[].orderListId | integer (int64) |  | 例: `-1` |
| result[].clientOrderId | string |  | 例: `sBI1KM6nNtOfj5tccZSKly` |
| result[].transactTime | integer (int64) |  | 例: `1689149087774` |
| result[].price | string |  | 例: `31000.00000000` |
| result[].origQty | string |  | 例: `0.50000000` |
| result[].executedQty | string |  | 例: `0.50000000` |
| result[].origQuoteOrderQty | string |  | 例: `0.000000` |
| result[].cummulativeQuoteQty | string |  | 例: `14000.00000000` |
| result[].status | string |  | 例: `FILLED` |
| result[].timeInForce | string |  | 例: `GTC` |
| result[].type | string |  | 例: `LIMIT` |
| result[].side | string |  | 例: `BUY` |
| result[].workingTime | integer (int64) |  | 例: `1689149087774` |
| result[].fills | object[] |  |  |
| result[].fills[].matchType | string |  | 例: `ONE_PARTY_TRADE_REPORT` |
| result[].fills[].price | string |  | 例: `28000.00000000` |
| result[].fills[].qty | string |  | 例: `0.50000000` |
| result[].fills[].commission | string |  | 例: `0.00000000` |
| result[].fills[].commissionAsset | string |  | 例: `BTC` |
| result[].fills[].tradeId | integer (int64) |  | 例: `-1` |
| result[].fills[].allocId | integer (int64) |  | 例: `0` |
| result[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| result[].selfTradePreventionMode | string |  | 例: `NONE` |
| result[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| result[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| result[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| result[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| result[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| result[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| result[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| result[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| result[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| result[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| result[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| result[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| result[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| result[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Test new order using SOR (TRADE)（测试 SOR 下单接口 (TRADE)）

`POST /sor.order.test`

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎。

权重: | Condition | Request Weight |
| --- | --- |
| Without `computeCommissionRates` | 1 |
| With `computeCommissionRates` | 20 |

Operation ID: `sorOrderTest`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `sor.order.test`<br>例: `sor.order.test` |
| params | object | 是 |  |
| params.computeCommissionRates | boolean |  | Default: `false`<br>默认值: `false`<br>默认: `False`<br>例: `False` |
| params.symbol | string | 是 | 例: `BNBUSDT` |
| params.side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| params.timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| params.price | number (float) |  | 例: `1` |
| params.quantity | number (float) | 是 | 例: `1` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。<br>例: `myOrder1` |
| params.newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`.<br>指定响应类型: `ACK`, `RESULT` 或 `FULL`; 默认为 `FULL`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| params.icebergQty | number (float) |  | Used with `LIMIT` to create an iceberg order.<br>仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| params.strategyId | integer (int64) |  | 例: `1` |
| params.strategyType | integer |  | The value cannot be less than `1000000`.<br>赋值不能小于 `1000000`。<br>例: `1` |
| params.selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "sor.order.test",
  "params": {
    "computeCommissionRates": false,
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "MARKET",
    "timeInForce": "GTC",
    "price": 1,
    "quantity": 1,
    "newClientOrderId": "myOrder1",
    "newOrderRespType": "ACK",
    "icebergQty": 1,
    "strategyId": 1,
    "strategyType": 1,
    "selfTradePreventionMode": "NONE",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Test new order using SOR / 测试 SOR 下单接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `3a4437e2-41a3-4c19-897c-9cadc5dce8b6` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `1` |
| (oneOf 2).id | string |  | 例: `3a4437e2-41a3-4c19-897c-9cadc5dce8b6` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object |  |  |
| (oneOf 2).result.standardCommissionForOrder | object |  | Standard commission rates on trades from the order.<br>订单交易的标准佣金率。 |
| (oneOf 2).result.standardCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).result.standardCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).result.taxCommissionForOrder | object |  | Tax commission rates for trades from the order.<br>订单交易的税率。 |
| (oneOf 2).result.taxCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).result.taxCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).result.discount | object |  | Discount on standard commissions when paying in BNB.<br>以BNB支付时的标准佣金折扣。 |
| (oneOf 2).result.discount.enabledForAccount | boolean |  | 例: `True` |
| (oneOf 2).result.discount.enabledForSymbol | boolean |  | 例: `True` |
| (oneOf 2).result.discount.discountAsset | string |  | 例: `BNB` |
| (oneOf 2).result.discount.discount | string |  | Standard commission is reduced by this rate when paying commission in BNB.<br>当用BNB支付佣金时，在标准佣金上按此比率打折。<br>例: `0.25000000` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `6000` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `20` |

## Listing all subscriptions（显示所有订阅）

`POST /session.subscriptions`

**Note:**

* Users should track the corresponding subscription status of related accounts as needed.

**注意：**

* 用户按需要跟踪相关帐户的对应订阅情况。

Operation ID: `sessionSubscriptions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `session.subscriptions`<br>例: `session.subscriptions` |
| params | object |  |  |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "session.subscriptions"
}
```

### 响应 Successful Response：Listing all subscriptions / 显示所有订阅

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].subscriptionId | integer (int64) |  | 例: `0` |

## Subscribe to User Data Stream (USER_STREAM)（订阅用户数据流 (USER_STREAM)）

`POST /userDataStream.subscribe`

Subscribe to the User Data Stream in the current WebSocket connection.

**Notes:**
  - This method requires an authenticated WebSocket connection using Ed25519 keys. Please refer to [`session.logon`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon).
  - To check the subscription status, use [`session.status`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-status), see the `userDataStream` flag indicating you have an active subscription.
  - User Data Stream events are available in both JSON and [SBE](/products/spot/faqs/sbe_faq) sessions.
    - Please refer to [User Data Streams](/products/spot/user-data-stream) for the event format details.
    - For SBE, only SBE schema 2:1 or later is supported.

订阅当前 WebSocket 连接中的用户数据流。

**注意：**
  - 此方法需要使用 Ed25519 密钥并经过鉴权的 WebSocket 连接。请参考 [`session.logon`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon)。
  - 如果需要查看订阅状态，可以通过 [`session.status`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-status) 查询，当 `userDataStream` 字段值为 `true` 时，表示您有一个有效的订阅。
  - 用户数据流在 JSON 和 [SBE 会话](/products/spot/faqs/sbe_faq) 中均可用。
    - 有关事件格式详情，请参阅 [用户数据流](/products/spot/user-data-stream)。
    - 对于 SBE，仅支持 SBE 模式 2:1 或更高版本。

Operation ID: `userDataStreamSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.subscribe`<br>例: `userDataStream.subscribe` |
| params | object |  |  |
| params.filter | object |  | Optional filter that controls which events are delivered on this subscription. See [User Data Stream Subscription Filters](#user-data-stream-subscription-filters). When omitted, all events for the subscribed account are delivered.<br>可选的过滤器，用于控制该订阅推送哪些事件。参见 [用户数据流订阅过滤器](#user-data-stream-subscription-filters)。未提供时，推送所订阅账户的所有事件。 |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "userDataStream.subscribe",
  "params": {
    "filter": {
      "e": [
        "executionReport"
      ]
    }
  }
}
```

### 响应 Successful Response：Subscribe to User Data Stream / 订阅用户数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.subscriptionId | integer (int64) |  | 例: `0` |

## Subscribe to User Data Stream through signature subscription (USER_STREAM)（通过签名订阅的方式订阅用户数据流 (USER_STREAM)）

`POST /userDataStream.subscribe.signature`

Operation ID: `userDataStreamSubscribeSignature`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.subscribe.signature`<br>例: `userDataStream.subscribe.signature` |
| params | object | 是 |  |
| params.recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |
| params.filter | object |  | Optional event filter. See [User Data Stream Subscription Filters](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters). When included, `filter` must be in the signed string with sorted keys and no whitespace between JSON elements.<br>可选的事件过滤器。参见 [用户数据流订阅过滤器](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters)。如果提供，`filter` 必须包含在被签名的字符串中，且键需排序、JSON 元素之间不能有空格。 |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "userDataStream.subscribe.signature",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "filter": {
      "e": [
        "executionReport"
      ]
    }
  }
}
```

### 响应 Successful Response：Subscribe to User Data Stream through signature subscription / 通过签名订阅的方式订阅用户数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.subscriptionId | integer (int64) |  | 例: `0` |

## Unsubscribe from User Data Stream（取消订阅用户数据流）

`POST /userDataStream.unsubscribe`

Stop listening to the User Data Stream in the current WebSocket
connection.

Note that `session.logout` will only close the subscription created with `userDataStream.subscribe` but not subscriptions opened with `userDataStream.subscribe.signature`.

取消订阅当前 WebSocket 连接中的用户数据流。

请注意 `session.logout` 只会关闭由 `userDataStream.subscribe` 创建的订阅，并不会关闭通过 `userDataStream.subscribe.signature` 创建的订阅。

Operation ID: `userDataStreamUnsubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Client-generated request identifier.<br>客户端生成的请求标识符。<br>例: `5494febb-d167-46a2-996d-70533eb4d976` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.unsubscribe`<br>例: `userDataStream.unsubscribe` |
| params | object |  |  |
| params.subscriptionId | integer |  | When called with no parameter, this will close all subscriptions. When called with the subscriptionId parameter, this will attempt to close the subscription with that subscription id, if it exists.<br>不带参数调用时，将关闭所有订阅。带 subscriptionId 参数调用时，将尝试关闭该订阅ID对应的订阅（如果存在）。<br>例: `1` |

```json
{
  "id": "5494febb-d167-46a2-996d-70533eb4d976",
  "method": "userDataStream.unsubscribe",
  "params": {
    "subscriptionId": 1
  }
}
```

### 响应 Successful Response：Unsubscribe from User Data Stream / 取消订阅用户数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |