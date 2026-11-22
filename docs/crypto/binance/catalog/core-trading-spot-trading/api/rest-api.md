---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:45:57.361467
---

# Spot REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade on Binance Spot.

访问市场数据、管理账户，并在 Binance 现货市场交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`
- `https://demo-api.binance.com`
- `https://data-api.binance.vision`
- `https://testnet.binance.vision`
- `https://api1.testnet.binance.vision`

## 接口列表

- `GET /api/v3/account/commission` — Query Commission Rates (USER_DATA)
- `GET /api/v3/allOrderList` — Query all Order lists (USER_DATA)
- `GET /api/v3/allOrders` — All orders (USER_DATA)
- `GET /api/v3/account` — Account information (USER_DATA)
- `GET /api/v3/openOrders` — Current open orders (USER_DATA)
- `DELETE /api/v3/openOrders` — Cancel All Open Orders on a Symbol (TRADE)
- `GET /api/v3/order` — Query order (USER_DATA)
- `POST /api/v3/order` — New order (TRADE)
- `DELETE /api/v3/order` — Cancel order (TRADE)
- `GET /api/v3/orderList` — Query Order list (USER_DATA)
- `DELETE /api/v3/orderList` — Cancel Order list (TRADE)
- `GET /api/v3/myAllocations` — Query Allocations (USER_DATA)
- `GET /api/v3/myFilters` — Query relevant filters (USER_DATA)
- `GET /api/v3/myPreventedMatches` — Query Prevented Matches (USER_DATA)
- `GET /api/v3/myTrades` — Account trade list (USER_DATA)
- `GET /api/v3/openOrderList` — Query Open Order lists (USER_DATA)
- `GET /api/v3/order/amendments` — Query Order Amendments (USER_DATA)
- `GET /api/v3/rateLimit/order` — Query Unfilled Order Count (USER_DATA)
- `GET /api/v3/exchangeInfo` — Exchange information
- `GET /api/v3/executionRules` — Query Execution Rules
- `GET /api/v3/ping` — Test connectivity
- `GET /api/v3/time` — Check server time
- `GET /api/v3/aggTrades` — Compressed/Aggregate trades list
- `GET /api/v3/avgPrice` — Current average price
- `GET /api/v3/depth` — Order book
- `GET /api/v3/trades` — Recent trades list
- `GET /api/v3/historicalTrades` — Old trade lookup
- `GET /api/v3/historicalBlockTrades` — Historical Block Trades (MARKET_DATA)
- `GET /api/v3/klines` — Kline/Candlestick data
- `GET /api/v3/ticker` — Rolling window price change statistics
- `GET /api/v3/ticker/24hr` — 24hr ticker price change statistics
- `GET /api/v3/ticker/bookTicker` — Symbol order book ticker
- `GET /api/v3/ticker/price` — Symbol price ticker
- `GET /api/v3/ticker/tradingDay` — Trading Day Ticker
- `GET /api/v3/uiKlines` — UIKlines
- `GET /api/v3/referencePrice` — Query Reference Price
- `GET /api/v3/referencePrice/calculation` — Query Reference Price Calculation
- `PUT /api/v3/order/amend/keepPriority` — Order Amend Keep Priority (TRADE)
- `POST /api/v3/order/cancelReplace` — Cancel an Existing Order and Send a New Order (TRADE)
- `POST /api/v3/orderList/oco` — New Order list - OCO (TRADE)
- `POST /api/v3/orderList/opo` — New Order List - OPO (TRADE)
- `POST /api/v3/orderList/opoco` — New Order List - OPOCO (TRADE)
- `POST /api/v3/orderList/oto` — New Order list - OTO (TRADE)
- `POST /api/v3/orderList/otoco` — New Order list - OTOCO (TRADE)
- `POST /api/v3/order/oco` — New OCO - Deprecated (TRADE)
- `POST /api/v3/order/test` — Test new order (TRADE)
- `POST /api/v3/sor/order` — New order using SOR (TRADE)
- `POST /api/v3/sor/order/test` — Test new order using SOR (TRADE)

## Query Commission Rates (USER_DATA)（查询佣金费率 (USER_DATA)）

`GET /api/v3/account/commission`

Get current account commission rates.

获取当前账户的佣金费率。

Operation ID: `accountCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Commission Rates / 查询佣金费率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `BTCUSDT` |
| standardCommission | object |  | Commission rates on trades from the order.<br>订单交易的标准佣金率。 |
| standardCommission.maker | string |  | 例: `0.00000010` |
| standardCommission.taker | string |  | 例: `0.00000020` |
| standardCommission.buyer | string |  | 例: `0.00000030` |
| standardCommission.seller | string |  | 例: `0.00000040` |
| specialCommission | object |  | Special commission rates from the order.<br>订单交易的特殊佣金率。 |
| specialCommission.maker | string |  | 例: `0.01000000` |
| specialCommission.taker | string |  | 例: `0.02000000` |
| specialCommission.buyer | string |  | 例: `0.03000000` |
| specialCommission.seller | string |  | 例: `0.04000000` |
| taxCommission | object |  | Tax commission rates for trades from the order.<br>订单交易的税率。 |
| taxCommission.maker | string |  | 例: `0.00000112` |
| taxCommission.taker | string |  | 例: `0.00000114` |
| taxCommission.buyer | string |  | 例: `0.00000118` |
| taxCommission.seller | string |  | 例: `0.00000116` |
| discount | object |  | Discount commission when paying in BNB<br>使用BNB支付时的佣金折扣。 |
| discount.enabledForAccount | boolean |  | 例: `True` |
| discount.enabledForSymbol | boolean |  | 例: `True` |
| discount.discountAsset | string |  | 例: `BNB` |
| discount.discount | string |  | Multiplier applied to the standard commission when paying commission in BNB (e.g. 0.75 = 75% of the standard commission is charged).<br>当用BNB支付佣金时，在标准佣金上按此比率打折<br>例: `0.75000000` |

## Query all Order lists (USER_DATA)（查询所有订单列表 (USER_DATA)）

`GET /api/v3/allOrderList`

Retrieves all order lists based on provided optional parameters.

Note that the time between `startTime` and `endTime` can't be longer
than 24 hours.

根据提供的可选参数检索所有的订单列表。

请注意，`startTime`和`endTime`之间的时间不能超过 24 小时。

Operation ID: `allOrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| fromId | query | integer (int64) |  | If supplied, neither startTime or endTime can be provided<br>提供该项后, startTime 和 endTime 都不可提供<br>例: `1` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query all Order lists / 查询所有订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | 例: `29` |
| [].contingencyType | string |  | 例: `OCO` |
| [].listStatusType | string |  | 例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | 例: `EXECUTING` |
| [].listClientOrderId | string |  | 例: `amEEAXryFzFwYF1FeRpUoZ` |
| [].transactionTime | integer (int64) |  | 例: `1565245913483` |
| [].symbol | string |  | 例: `LTCBTC` |
| [].orders | object[] |  |  |
| [].orders[].symbol | string |  | 例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | 例: `4` |
| [].orders[].clientOrderId | string |  | 例: `oD7aesZqjEGlZrbtRpy5zB` |

```json
[
  {
    "orderListId": 29,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",
    "transactionTime": 1565245913483,
    "symbol": "LTCBTC",
    "orders": [
      {
        "symbol": "LTCBTC",
        "orderId": 4,
        "clientOrderId": "oD7aesZqjEGlZrbtRpy5zB"
      },
      {
        "symbol": "LTCBTC",
        "orderId": 5,
        "clientOrderId": "Jr1h6xirOxgeJOUuYQS7V3"
      }
    ]
  },
  {
    "orderListId": 28,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "hG7hFNxJV6cZy3Ze4AUT4d",
    "transactionTime": 1565245913407,
    "symbol": "LTCBTC",
    "orders": [
      {
        "symbol": "LTCBTC",
        "orderId": 2,
        "clientOrderId": "j6lFOfbmFMRjTYA7rRJ0LP"
      },
      {
        "symbol": "LTCBTC",
        "orderId": 3,
        "clientOrderId": "z0KCjOdditiLS5ekAFtK81"
      }
    ]
  }
]
```

## All orders (USER_DATA)（查询所有订单（包括历史订单） (USER_DATA)）

`GET /api/v3/allOrders`

Get all account orders; active, canceled, or filled.

获取all 账户 订单; active, canceled, 或 filled.

Operation ID: `allOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `LTCBTC` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| recvWindow | query | number (float) |  | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：All orders / All 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `LTCBTC` |
| [].orderId | integer (int64) |  | 例: `1` |
| [].orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| [].clientOrderId | string |  | 例: `myOrder1` |
| [].price | string |  | 例: `0.1` |
| [].origQty | string |  | 例: `1.0` |
| [].executedQty | string |  | 例: `0.0` |
| [].cummulativeQuoteQty | string |  | 例: `0.0` |
| [].status | string |  | 例: `NEW` |
| [].timeInForce | string |  | 例: `GTC` |
| [].type | string |  | 例: `LIMIT` |
| [].side | string |  | 例: `BUY` |
| [].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| [].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| [].time | integer (int64) |  | 例: `1499827319559` |
| [].updateTime | integer (int64) |  | 例: `1499827319559` |
| [].isWorking | boolean |  | 例: `True` |
| [].origQuoteOrderQty | string |  | 例: `0.000000` |
| [].workingTime | integer (int64) |  | 例: `1499827319559` |
| [].selfTradePreventionMode | string |  | 例: `NONE` |
| [].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| [].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| [].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| [].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| [].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| [].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| [].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| [].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| [].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| [].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| [].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| [].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| [].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## Account information (USER_DATA)（账户信息 (USER_DATA)）

`GET /api/v3/account`

Get current account information.

获取当前账户信息。

Operation ID: `getAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| omitZeroBalances | query | boolean |  | When set to `true`, emits only the non-zero balances of an account.<br>如果`true`，将隐藏所有零余额。<br>默认: `False`<br>例: `False` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Account information / 账户信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| makerCommission | integer (int64) |  | 例: `15` |
| takerCommission | integer (int64) |  | 例: `15` |
| buyerCommission | integer (int64) |  | 例: `0` |
| sellerCommission | integer (int64) |  | 例: `0` |
| commissionRates | object |  |  |
| commissionRates.maker | string |  | 例: `0.00150000` |
| commissionRates.taker | string |  | 例: `0.00150000` |
| commissionRates.buyer | string |  | 例: `0.00000000` |
| commissionRates.seller | string |  | 例: `0.00000000` |
| canTrade | boolean |  | 例: `True` |
| canWithdraw | boolean |  | 例: `True` |
| canDeposit | boolean |  | 例: `True` |
| brokered | boolean |  | 例: `False` |
| requireSelfTradePrevention | boolean |  | 例: `False` |
| preventSor | boolean |  | 例: `False` |
| updateTime | integer (int64) |  | 例: `123456789` |
| accountType | string |  | 例: `SPOT` |
| balances | object[] |  |  |
| balances[].asset | string |  | 例: `BTC` |
| balances[].free | string |  | 例: `4723846.89208129` |
| balances[].locked | string |  | 例: `0.00000000` |
| permissions | string[] |  |  |
| uid | integer (int64) |  | 例: `354937868` |

## Current open orders (USER_DATA)（查看账户当前挂单 (USER_DATA)）

`GET /api/v3/openOrders`

Get all open orders on a symbol. **Careful** when accessing this with no symbol.

请小心使用不带symbol参数的调用

权重: 6 for a single symbol; 80 when the symbol parameter is omitted

Operation ID: `getOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `LTCBTC` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Current open orders / 查看账户当前挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `LTCBTC` |
| [].orderId | integer (int64) |  | 例: `1` |
| [].orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| [].clientOrderId | string |  | 例: `myOrder1` |
| [].price | string |  | 例: `0.1` |
| [].origQty | string |  | 例: `1.0` |
| [].executedQty | string |  | 例: `0.0` |
| [].origQuoteOrderQty | string |  | 例: `0.000000` |
| [].cummulativeQuoteQty | string |  | 例: `0.0` |
| [].status | string |  | 例: `NEW` |
| [].timeInForce | string |  | 例: `GTC` |
| [].type | string |  | 例: `LIMIT` |
| [].side | string |  | 例: `BUY` |
| [].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| [].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| [].time | integer (int64) |  | 例: `1499827319559` |
| [].updateTime | integer (int64) |  | 例: `1499827319559` |
| [].isWorking | boolean |  | 例: `True` |
| [].workingTime | integer (int64) |  | 例: `1499827319559` |
| [].selfTradePreventionMode | string |  | 例: `NONE` |
| [].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| [].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| [].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| [].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| [].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| [].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| [].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| [].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| [].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| [].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| [].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| [].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| [].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## Cancel All Open Orders on a Symbol (TRADE)（撤销单一交易对的所有挂单 (TRADE)）

`DELETE /api/v3/openOrders`

Cancels all active orders on a symbol.
This includes orders that are part of an order list.

撤销单一交易对下所有挂单。这也包括了来自订单列表的挂单。

Operation ID: `deleteOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Cancel All Open Orders on a Symbol / 撤销单一交易对的所有挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].origClientOrderId | string |  | 例: `E6APeyTJvkMvLMYMqu1KQ4` |
| [].orderId | integer (int64) |  | 例: `11` |
| [].orderListId | integer (int64) |  | 例: `-1` |
| [].clientOrderId | string |  | 例: `pXLV6Hz6mprAcVYpVMTGgx` |
| [].transactTime | integer (int64) |  | 例: `1684804350068` |
| [].price | string |  | 例: `0.089853` |
| [].origQty | string |  | 例: `0.178622` |
| [].executedQty | string |  | 例: `0.000000` |
| [].origQuoteOrderQty | string |  | 例: `0.000000` |
| [].cummulativeQuoteQty | string |  | 例: `0.000000` |
| [].status | string |  | 例: `CANCELED` |
| [].timeInForce | string |  | 例: `GTC` |
| [].type | string |  | 例: `LIMIT` |
| [].side | string |  | 例: `BUY` |
| [].selfTradePreventionMode | string |  | 例: `NONE` |

```json
[
  {
    "symbol": "BTCUSDT",
    "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",
    "orderId": 11,
    "orderListId": -1,
    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
    "transactTime": 1684804350068,
    "price": "0.089853",
    "origQty": "0.178622",
    "executedQty": "0.000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.000000",
    "status": "CANCELED",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "selfTradePreventionMode": "NONE"
  },
  {
    "symbol": "BTCUSDT",
    "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",
    "orderId": 13,
    "orderListId": -1,
    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
    "transactTime": 1684804350069,
    "price": "0.090430",
    "origQty": "0.178622",
    "executedQty": "0.000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.000000",
    "status": "CANCELED",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "selfTradePreventionMode": "NONE"
  },
  {
    "orderListId": 1929,
    "contingencyType": "OCO",
    "listStatusType": "ALL_DONE",
    "listOrderStatus": "ALL_DONE",
    "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",
    "transactionTime": 1585230948299,
    "symbol": "BTCUSDT",
    "orders": [
      {
        "symbol": "BTCUSDT",
        "orderId": 20,
        "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"
      },
      {
        "symbol": "BTCUSDT",
        "orderId": 21,
        "clientOrderId": "461cPg51vQjV3zIMOXNz39"
      }
    ],
    "orderReports": [
      {
        "symbol": "BTCUSDT",
        "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",
        "orderId": 20,
        "orderListId": 1929,
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
        "transactTime": 1688005070874,
        "price": "0.668611",
        "origQty": "0.690354",
        "executedQty": "0.000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.000000",
        "status": "CANCELED",
        "timeInForce": "GTC",
        "type": "STOP_LOSS_LIMIT",
        "side": "BUY",
        "stopPrice": "0.378131",
        "icebergQty": "0.017083",
        "selfTradePreventionMode": "NONE"
      },
      {
        "symbol": "BTCUSDT",
        "origClientOrderId": "461cPg51vQjV3zIMOXNz39",
        "orderId": 21,
        "orderListId": 1929,
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
        "transactTime": 1688005070874,
        "price": "0.008791",
        "origQty": "0.690354",
        "executedQty": "0.000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.000000",
        "status": "CANCELED",
        "timeInForce": "GTC",
        "type": "LIMIT_MAKER",
        "side": "BUY",
        "icebergQty": "0.639962",
        "selfTradePreventionMode": "NONE"
      }
    ]
  }
]
```

## Query order (USER_DATA)（查询订单 (USER_DATA)）

`GET /api/v3/order`

Check an order's status.

查询订单状态

Operation ID: `getOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `LTCBTC` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `myOrder1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query order / 查询订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | symbol.<br>交易对<br>例: `LTCBTC` |
| orderId | integer (int64) |  | order Id.<br>系统的订单ID<br>例: `1` |
| orderListId | integer (int64) |  | This field will always have a value of -1 if not an order list.<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| clientOrderId | string |  | client Order Id.<br>客户自己设置的ID<br>例: `myOrder1` |
| price | string |  | price.<br>订单价格<br>例: `0.1` |
| origQty | string |  | orig Qty.<br>用户设置的原始订单数量<br>例: `1.0` |
| executedQty | string |  | executed Qty.<br>交易的订单数量<br>例: `0.0` |
| origQuoteOrderQty | string |  | orig Quote Order Qty.<br>原始的交易金额<br>例: `0.000000` |
| cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>累计交易的金额<br>例: `0.0` |
| status | string |  | status.<br>订单状态<br>例: `NEW` |
| timeInForce | string |  | time In Force.<br>订单的时效方式<br>例: `GTC` |
| type | string |  | type.<br>订单类型， 比如市价单，现价单等<br>例: `LIMIT` |
| side | string |  | side.<br>订单方向，买还是卖<br>例: `BUY` |
| stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| time | integer (int64) |  | time.<br>订单时间<br>例: `1499827319559` |
| updateTime | integer (int64) |  | update Time.<br>最后更新时间<br>例: `1499827319559` |
| isWorking | boolean |  | is Working.<br>订单是否出现在orderbook中<br>例: `True` |
| workingTime | integer (int64) |  | working Time.<br>订单添加到 order book 的时间<br>例: `1499827319559` |
| selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>如何处理自我交易模式<br>例: `NONE` |
| preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## New order (TRADE)（下单 (TRADE)）

`POST /api/v3/order`

Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `newOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| quantity | number (float) |  | 例: `1` |
| quoteOrderQty | number (float) |  | 例: `1` |
| price | number (float) |  | 例: `400` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。<br>例: `myOrder1` |
| strategyId | integer (int64) |  | 例: `1` |
| strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。<br>例: `1` |
| trailingDelta | integer (int64) |  | See Trailing Stop order FAQ<br>参见 追踪止盈止损(Trailing Stop)订单常见问题<br>例: `1` |
| icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| newOrderRespType | string |  | `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.<br>`MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol.<br>允许的 ENUM 取决于交易对的配置。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| pegPriceType | string |  | See Pegged Orders Info<br>参阅 关于挂钩订单参数的注意事项<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pegOffsetValue | integer |  | Price level to peg the price to (max: 100). See Pegged Orders Info<br>用于挂钩的价格水平（最大值：100）。参阅 关于挂钩订单参数的注意事项<br>例: `1` |
| pegOffsetType | string |  | Only `PRICE_LEVEL` is supported. See Pegged Orders Info<br>仅支持 `PRICE_LEVEL`。参阅 关于挂钩订单参数的注意事项<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| quoteNotionalLimit | number (float) |  | For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New order / 下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).orderId | integer (int64) |  | 例: `28` |
| (oneOf 1).orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| (oneOf 1).clientOrderId | string |  | 例: `6gCrw2kRUAF9CvJDGP16IP` |
| (oneOf 1).transactTime | integer (int64) |  | 例: `1507725176595` |
| (oneOf 2).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).orderId | integer (int64) |  | 例: `28` |
| (oneOf 2).orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| (oneOf 2).clientOrderId | string |  | 例: `6gCrw2kRUAF9CvJDGP16IP` |
| (oneOf 2).transactTime | integer (int64) |  | 例: `1507725176595` |
| (oneOf 2).price | string |  | 例: `0.00000000` |
| (oneOf 2).origQty | string |  | 例: `10.00000000` |
| (oneOf 2).executedQty | string |  | 例: `10.00000000` |
| (oneOf 2).origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 2).cummulativeQuoteQty | string |  | 例: `10.00000000` |
| (oneOf 2).status | string |  | 例: `FILLED` |
| (oneOf 2).timeInForce | string |  | 例: `GTC` |
| (oneOf 2).type | string |  | 例: `MARKET` |
| (oneOf 2).side | string |  | 例: `SELL` |
| (oneOf 2).workingTime | integer (int64) |  | 例: `1507725176595` |
| (oneOf 2).selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 3).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 3).orderId | integer (int64) |  | 例: `28` |
| (oneOf 3).orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| (oneOf 3).clientOrderId | string |  | 例: `6gCrw2kRUAF9CvJDGP16IP` |
| (oneOf 3).transactTime | integer (int64) |  | 例: `1507725176595` |
| (oneOf 3).price | string |  | 例: `1.00000000` |
| (oneOf 3).origQty | string |  | 例: `10.00000000` |
| (oneOf 3).executedQty | string |  | 例: `10.00000000` |
| (oneOf 3).origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 3).cummulativeQuoteQty | string |  | 例: `10.00000000` |
| (oneOf 3).status | string |  | 例: `FILLED` |
| (oneOf 3).timeInForce | string |  | 例: `GTC` |
| (oneOf 3).type | string |  | 例: `MARKET` |
| (oneOf 3).side | string |  | 例: `SELL` |
| (oneOf 3).workingTime | integer (int64) |  | 例: `1507725176595` |
| (oneOf 3).selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 3).fills | object[] |  |  |
| (oneOf 3).fills[].price | string |  | 例: `4000.00000000` |
| (oneOf 3).fills[].qty | string |  | 例: `1.00000000` |
| (oneOf 3).fills[].commission | string |  | 例: `4.00000000` |
| (oneOf 3).fills[].commissionAsset | string |  | 例: `USDT` |
| (oneOf 3).fills[].tradeId | integer (int64) |  | 例: `56` |

## Cancel order (TRADE)（撤销订单 (TRADE)）

`DELETE /api/v3/order`

Cancel an active order.

撤销订单.

Operation ID: `deleteOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `myOrder1` |
| newClientOrderId | query | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `cancelMyOrder1` |
| cancelRestrictions | query | string |  | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).<br>支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。<br>枚举: `ONLY_NEW`, `ONLY_PARTIALLY_FILLED`<br>例: `ONLY_NEW` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Cancel order / 撤销订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `LTCBTC` |
| orderId | integer (int64) |  | 例: `4` |
| orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| origClientOrderId | string |  | 例: `myOrder1` |
| clientOrderId | string |  | 例: `cancelMyOrder1` |
| transactTime | integer (int64) |  | 例: `1684804350068` |
| price | string |  | 例: `2.00000000` |
| origQty | string |  | 例: `1.00000000` |
| executedQty | string |  | 例: `0.00000000` |
| origQuoteOrderQty | string |  | 例: `0.000000` |
| cummulativeQuoteQty | string |  | 例: `0.00000000` |
| status | string |  | 例: `CANCELED` |
| timeInForce | string |  | 例: `GTC` |
| type | string |  | 例: `LIMIT` |
| side | string |  | 例: `BUY` |
| selfTradePreventionMode | string |  | 例: `NONE` |
| icebergQty | string |  | Quantity for the iceberg order. Appears only if the parameter `icebergQty` was sent in the request.<br>冰山订单数量。仅当请求中发送了 `icebergQty` 参数时返回。<br>例: `0.00000000` |
| preventedMatchId | integer (int64) |  | When used together with `symbol`, can be used to query a prevented match. Appears only if the order expired due to STP.<br>与 `symbol` 搭配时可用于查询 prevented match。仅当订单因 STP 过期时返回。<br>例: `0` |
| preventedQuantity | string |  | Order quantity that expired due to STP. Appears only if the order expired due to STP.<br>因 STP 过期的订单数量。仅当订单因 STP 过期时返回。<br>例: `1.200000` |
| stopPrice | string |  | Price when the algorithmic order will be triggered. Appears for `STOP_LOSS`, `TAKE_PROFIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` orders.<br>算法订单触发价格。适用于 `STOP_LOSS`、`TAKE_PROFIT`、`STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。<br>例: `23500.00000000` |
| strategyId | integer (int64) |  | Can be used to label an order that's part of an order strategy. Appears if the parameter was populated in the request.<br>可用于标记订单策略中的订单。仅当请求中传入该参数时返回。<br>例: `37463720` |
| strategyType | integer (int64) |  | Can be used to label an order that is using an order strategy. Appears if the parameter was populated in the request.<br>可用于标记使用订单策略的订单。仅当请求中传入该参数时返回。<br>例: `1000000` |
| trailingDelta | integer (int64) |  | Delta price change required before order activation. Appears for trailing stop orders.<br>订单激活前所需的价格变动幅度。适用于追踪止损订单。<br>例: `10` |
| trailingTime | integer (int64) |  | Time when the trailing order becomes active and starts tracking price changes. Appears only for trailing stop orders.<br>追踪订单激活并开始跟踪价格变化的时间。仅适用于追踪止损订单。<br>例: `-1` |
| usedSor | boolean |  | Indicates whether the order used SOR. Appears when placing orders using SOR.<br>表示订单是否使用了 SOR。仅在使用 SOR 下单时返回。<br>例: `True` |
| workingFloor | string |  | Indicates whether the order is being filled by SOR or by the order book to which it was submitted. Appears when placing orders using SOR.<br>表示订单由 SOR 撮合还是由提交到的订单簿撮合。仅在使用 SOR 下单时返回。<br>例: `SOR` |
| pegPriceType | string |  | Price peg type. Only for pegged orders.<br>Peg 价格类型。仅适用于 pegged 订单。<br>例: `PRIMARY_PEG` |
| pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>Peg 价格偏移类型。仅适用于请求了该字段的 pegged 订单。<br>例: `PRICE_LEVEL` |
| pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>Peg 价格偏移值。仅适用于请求了该字段的 pegged 订单。<br>例: `5` |
| peggedPrice | string |  | Current price the order is pegged at. Only for pegged orders, once determined.<br>订单当前 peg 到的价格。仅适用于已确定 peg 价格的订单。<br>例: `87523.83710000` |
| expiryReason | string |  | Cause of the order's expiration. Returned when an order has expired.<br>订单过期原因。仅当订单已过期时返回。<br>例: `INSUFFICIENT_LIQUIDITY` |

## Query Order list (USER_DATA)（查询订单列表 (USER_DATA)）

`GET /api/v3/orderList`

Retrieves a specific order list based on provided optional parameters.

根据提供的可选参数检索特定的订单列表。

Operation ID: `getOrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderListId | query | integer (int64) |  | Query order list by `orderListId`. `orderListId` or `origClientOrderId` must be provided.<br>通过 `orderListId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。<br>例: `27` |
| origClientOrderId | query | string |  | Query order list by `listClientOrderId`. `orderListId` or `origClientOrderId` must be provided.<br>通过 `listClientOrderId` 查询订单列表。`orderListId` 或 `origClientOrderId` 必须被提供。<br>例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Order list / 查询订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `27` |
| contingencyType | string |  | 例: `OCO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `h2USkA5YQpaXHPIrkd96xE` |
| transactionTime | integer (int64) |  | 例: `1565245656253` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `4` |
| orders[].clientOrderId | string |  | 例: `qD1gy3kc3Gx0rihm9Y3xwS` |

## Cancel Order list (TRADE)（取消订单列表 (TRADE)）

`DELETE /api/v3/orderList`

Cancel an entire Order list

取消整个订单列表。

Operation ID: `deleteOrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| orderListId | query | integer (int64) |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| listClientOrderId | query | string |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `C3wyj4WVEktd7u9aVBRXcN` |
| newClientOrderId | query | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `cancelMyOrder1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Cancel Order list / 取消订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `0` |
| contingencyType | string |  | 例: `OCO` |
| listStatusType | string |  | 例: `ALL_DONE` |
| listOrderStatus | string |  | 例: `ALL_DONE` |
| listClientOrderId | string |  | 例: `C3wyj4WVEktd7u9aVBRXcN` |
| transactionTime | integer (int64) |  | 例: `1574040868128` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `2` |
| orders[].clientOrderId | string |  | 例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `LTCBTC` |
| orderReports[].origClientOrderId | string |  | 例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports[].orderId | integer (int64) |  | 例: `2` |
| orderReports[].orderListId | integer (int64) |  | 例: `0` |
| orderReports[].clientOrderId | string |  | 例: `unfWT8ig8i0uj6lPuYLez6` |
| orderReports[].transactTime | integer (int64) |  | 例: `1688005070874` |
| orderReports[].price | string |  | 例: `1.00000000` |
| orderReports[].origQty | string |  | 例: `10.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `CANCELED` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| orderReports[].side | string |  | 例: `SELL` |
| orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## Query Allocations (USER_DATA)（查询分配结果 (USER_DATA)）

`GET /api/v3/myAllocations`

Retrieves allocations resulting from SOR order placement.

检索由 SOR 订单生成引起的分配结果。

Operation ID: `myAllocations`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| fromAllocationId | query | integer |  | 例: `0` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| orderId | query | integer (int64) |  | 例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Allocations / 查询分配结果

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].allocationId | integer (int64) |  | 例: `0` |
| [].allocationType | string |  | 例: `SOR` |
| [].orderId | integer (int64) |  | 例: `1` |
| [].orderListId | integer (int64) |  | 例: `-1` |
| [].price | string |  | 例: `1.00000000` |
| [].qty | string |  | 例: `5.00000000` |
| [].quoteQty | string |  | 例: `5.00000000` |
| [].commission | string |  | 例: `0.00000000` |
| [].commissionAsset | string |  | 例: `BTC` |
| [].time | integer (int64) |  | 例: `1687506878118` |
| [].isBuyer | boolean |  | 例: `True` |
| [].isMaker | boolean |  | 例: `False` |
| [].isAllocator | boolean |  | 例: `False` |

## Query relevant filters (USER_DATA)（查询相关过滤器 (USER_DATA)）

`GET /api/v3/myFilters`

Retrieves the list of [filters](/products/spot/filters) relevant to an account on a given symbol. This is the only endpoint that shows if an account has [`MAX_ASSET`](/products/spot/filters#max_asset) filters applied to it.

用于检索一个账户上指定交易对的 [filters](/products/spot/filters) 列表。这是唯一一个目前会显示账户是否应用了 [`MAX_ASSET`](/products/spot/filters#max_asset) 过滤器的端点。

Operation ID: `myFilters`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query relevant filters / 查询相关过滤器

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| exchangeFilters | oneOf[] |  |  |
| exchangeFilters[](oneOf 1).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDERS` |
| exchangeFilters[](oneOf 1).maxNumOrders | integer (int64) |  | 例: `1000` |
| exchangeFilters[](oneOf 2).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ALGO_ORDERS` |
| exchangeFilters[](oneOf 2).maxNumAlgoOrders | integer (int64) |  | 例: `200` |
| exchangeFilters[](oneOf 3).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` |
| exchangeFilters[](oneOf 3).maxNumIcebergOrders | integer (int64) |  | 例: `10` |
| exchangeFilters[](oneOf 4).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDER_LISTS` |
| exchangeFilters[](oneOf 4).maxNumOrderLists | integer (int64) |  | 例: `20` |
| symbolFilters | oneOf[] |  |  |
| symbolFilters[](oneOf 1).filterType | string |  | 例: `PRICE_FILTER` |
| symbolFilters[](oneOf 1).priceExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 1).minPrice | string |  | 例: `0.00000100` |
| symbolFilters[](oneOf 1).maxPrice | string |  | 例: `100000.00000000` |
| symbolFilters[](oneOf 1).tickSize | string |  | 例: `0.00000100` |
| symbolFilters[](oneOf 2).filterType | string |  | 例: `PERCENT_PRICE` |
| symbolFilters[](oneOf 2).multiplierExponent | integer |  | 例: `4` |
| symbolFilters[](oneOf 2).multiplierUp | string |  | 例: `1.3000` |
| symbolFilters[](oneOf 2).multiplierDown | string |  | 例: `0.7000` |
| symbolFilters[](oneOf 2).avgPriceMins | integer |  | 例: `5` |
| symbolFilters[](oneOf 3).filterType | string |  | 例: `PERCENT_PRICE_BY_SIDE` |
| symbolFilters[](oneOf 3).multiplierExponent | integer |  | 例: `4` |
| symbolFilters[](oneOf 3).bidMultiplierUp | string |  | 例: `1.2000` |
| symbolFilters[](oneOf 3).bidMultiplierDown | string |  | 例: `0.8000` |
| symbolFilters[](oneOf 3).askMultiplierUp | string |  | 例: `1.2000` |
| symbolFilters[](oneOf 3).askMultiplierDown | string |  | 例: `0.8000` |
| symbolFilters[](oneOf 3).avgPriceMins | integer |  | 例: `5` |
| symbolFilters[](oneOf 4).filterType | string |  | 例: `LOT_SIZE` |
| symbolFilters[](oneOf 4).qtyExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 4).minQty | string |  | 例: `0.00010000` |
| symbolFilters[](oneOf 4).maxQty | string |  | 例: `100000.00000000` |
| symbolFilters[](oneOf 4).stepSize | string |  | 例: `0.00010000` |
| symbolFilters[](oneOf 5).filterType | string |  | 例: `MIN_NOTIONAL` |
| symbolFilters[](oneOf 5).priceExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 5).minNotional | string |  | 例: `10.00000000` |
| symbolFilters[](oneOf 5).applyToMarket | boolean |  | 例: `True` |
| symbolFilters[](oneOf 5).avgPriceMins | integer |  | 例: `5` |
| symbolFilters[](oneOf 6).filterType | string |  | 例: `NOTIONAL` |
| symbolFilters[](oneOf 6).priceExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 6).minNotional | string |  | 例: `10.00000000` |
| symbolFilters[](oneOf 6).applyMinToMarket | boolean |  | 例: `True` |
| symbolFilters[](oneOf 6).maxNotional | string |  | 例: `100000.00000000` |
| symbolFilters[](oneOf 6).applyMaxToMarket | boolean |  | 例: `False` |
| symbolFilters[](oneOf 6).avgPriceMins | integer |  | 例: `5` |
| symbolFilters[](oneOf 7).filterType | string |  | 例: `ICEBERG_PARTS` |
| symbolFilters[](oneOf 7).limit | integer (int64) |  | 例: `10` |
| symbolFilters[](oneOf 8).filterType | string |  | 例: `MARKET_LOT_SIZE` |
| symbolFilters[](oneOf 8).qtyExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 8).minQty | string |  | 例: `0.00000000` |
| symbolFilters[](oneOf 8).maxQty | string |  | 例: `1000.00000000` |
| symbolFilters[](oneOf 8).stepSize | string |  | 例: `0.00000000` |
| symbolFilters[](oneOf 9).filterType | string |  | 例: `MAX_NUM_ORDERS` |
| symbolFilters[](oneOf 9).maxNumOrders | integer (int64) |  | 例: `200` |
| symbolFilters[](oneOf 10).filterType | string |  | 例: `MAX_NUM_ALGO_ORDERS` |
| symbolFilters[](oneOf 10).maxNumAlgoOrders | integer (int64) |  | 例: `10` |
| symbolFilters[](oneOf 11).filterType | string |  | 例: `MAX_NUM_ICEBERG_ORDERS` |
| symbolFilters[](oneOf 11).maxNumIcebergOrders | integer (int64) |  | 例: `5` |
| symbolFilters[](oneOf 12).filterType | string |  | 例: `MAX_POSITION` |
| symbolFilters[](oneOf 12).qtyExponent | integer |  | 例: `8` |
| symbolFilters[](oneOf 12).maxPosition | string |  | 例: `100.00000000` |
| symbolFilters[](oneOf 13).filterType | string |  | 例: `TRAILING_DELTA` |
| symbolFilters[](oneOf 13).minTrailingAboveDelta | integer (int64) |  | 例: `10` |
| symbolFilters[](oneOf 13).maxTrailingAboveDelta | integer (int64) |  | 例: `2000` |
| symbolFilters[](oneOf 13).minTrailingBelowDelta | integer (int64) |  | 例: `10` |
| symbolFilters[](oneOf 13).maxTrailingBelowDelta | integer (int64) |  | 例: `2000` |
| symbolFilters[](oneOf 14).filterType | string |  | 例: `T_PLUS_SELL` |
| symbolFilters[](oneOf 14).endTime | integer (int64) |  | 例: `1741672924895` |
| symbolFilters[](oneOf 15).filterType | string |  | 例: `MAX_NUM_ORDER_LISTS` |
| symbolFilters[](oneOf 15).maxNumOrderLists | integer (int64) |  | 例: `20` |
| symbolFilters[](oneOf 16).filterType | string |  | 例: `MAX_NUM_ORDER_AMENDS` |
| symbolFilters[](oneOf 16).maxNumOrderAmends | integer (int64) |  | 例: `10` |
| assetFilters | oneOf[] |  |  |
| assetFilters[](oneOf 1).filterType | string |  | 例: `MAX_ASSET` |
| assetFilters[](oneOf 1).qtyExponent | integer |  | 例: `8` |
| assetFilters[](oneOf 1).limit | string |  | 例: `100.00000000` |
| assetFilters[](oneOf 1).asset | string |  | 例: `BNB` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `321` |

## Query Prevented Matches (USER_DATA)（获取 Prevented Matches (USER_DATA)）

`GET /api/v3/myPreventedMatches`

Displays the list of orders that were expired due to STP.

These are the combinations supported:
  - `symbol` + `preventedMatchId`
  - `symbol` + `orderId`
  - `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
  - `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

获取因 STP 而过期的订单列表。

这些是支持的组合：
  - `symbol` + `preventedMatchId`
  - `symbol` + `orderId`
  - `symbol` + `orderId` + `fromPreventedMatchId` (`limit` 默认为 500)
  - `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

权重: Case                            | Weight
----                            | -----
If `symbol` is invalid          | 2
Querying by `preventedMatchId`  | 2
Querying by `orderId`           | 20

Operation ID: `myPreventedMatches`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| preventedMatchId | query | integer (int64) |  | 例: `1` |
| orderId | query | integer (int64) |  | 例: `1` |
| fromPreventedMatchId | query | integer (int64) |  | 例: `1` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Prevented Matches / 获取 Prevented Matches

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].preventedMatchId | integer (int64) |  | 例: `1` |
| [].takerOrderId | integer (int64) |  | 例: `5` |
| [].makerSymbol | string |  | 例: `BTCUSDT` |
| [].makerOrderId | integer (int64) |  | 例: `3` |
| [].tradeGroupId | integer (int64) |  | 例: `1` |
| [].selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| [].price | string |  | 例: `1.100000` |
| [].makerPreventedQuantity | string |  | 例: `1.300000` |
| [].transactTime | integer (int64) |  | 例: `1669101687094` |

## Account trade list (USER_DATA)（账户成交历史 (USER_DATA)）

`GET /api/v3/myTrades`

Get trades for a specific account and symbol.

获取某交易对的成交历史

权重: Condition| Weight|
---| ---
|Without orderId|20|
|With orderId|5|

Operation ID: `myTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBBTC` |
| orderId | query | integer (int64) |  | This can only be used in combination with `symbol`.<br>必须要和参数`symbol`一起使用。<br>例: `100234` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| fromId | query | integer (int64) |  | TradeId to fetch from. Default gets most recent trades.<br>返回该fromId之后的成交，缺省返回最近的成交<br>例: `1` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Account trade list / 账户成交历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BNBBTC` |
| [].id | integer (int64) |  | 例: `28457` |
| [].orderId | integer (int64) |  | 例: `100234` |
| [].orderListId | integer (int64) |  | 例: `-1` |
| [].price | string |  | 例: `4.00000100` |
| [].qty | string |  | 例: `12.00000000` |
| [].quoteQty | string |  | 例: `48.000012` |
| [].commission | string |  | 例: `10.10000000` |
| [].commissionAsset | string |  | 例: `BNB` |
| [].time | integer (int64) |  | 例: `1499865549590` |
| [].isBuyer | boolean |  | 例: `True` |
| [].isMaker | boolean |  | 例: `False` |
| [].isBestMatch | boolean |  | 例: `True` |

## Query Open Order lists (USER_DATA)（查询订单列表挂单 (USER_DATA)）

`GET /api/v3/openOrderList`

Query Open Order lists

查询订单列表挂单

Operation ID: `openOrderList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Open Order lists / 查询订单列表挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | 例: `31` |
| [].contingencyType | string |  | 例: `OCO` |
| [].listStatusType | string |  | 例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | 例: `EXECUTING` |
| [].listClientOrderId | string |  | 例: `wuB13fmulKj3YjdqWEcsnp` |
| [].transactionTime | integer (int64) |  | 例: `1565246080644` |
| [].symbol | string |  | 例: `LTCBTC` |
| [].orders | object[] |  |  |
| [].orders[].symbol | string |  | 例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | 例: `4` |
| [].orders[].clientOrderId | string |  | 例: `r3EH2N76dHfLoSZWIUw1bT` |

## Query Order Amendments (USER_DATA)（查询改单 (USER_DATA)）

`GET /api/v3/order/amendments`

Queries all amendments of a single order.

查询对一个订单的所有改单操作。

Operation ID: `orderAmendments`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) | 是 | 例: `9` |
| fromExecutionId | query | integer (int64) |  | 例: `22` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `1` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Order Amendments / 查询改单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].orderId | integer (int64) |  | 例: `9` |
| [].executionId | integer (int64) |  | 例: `22` |
| [].origClientOrderId | string |  | 例: `W0fJ9fiLKHOJutovPK3oJp` |
| [].newClientOrderId | string |  | 例: `UQ1Np3bmQ71jJzsSDW9Vpi` |
| [].origQty | string |  | 例: `5.00000000` |
| [].newQty | string |  | 例: `4.00000000` |
| [].time | integer (int64) |  | 例: `1741669661670` |

```json
[
  {
    "symbol": "BTCUSDT",
    "orderId": 9,
    "executionId": 22,
    "origClientOrderId": "W0fJ9fiLKHOJutovPK3oJp",
    "newClientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",
    "origQty": "5.00000000",
    "newQty": "4.00000000",
    "time": 1741669661670
  },
  {
    "symbol": "BTCUDST",
    "orderId": 9,
    "executionId": 25,
    "origClientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",
    "newClientOrderId": "5uS0r35ohuQyDlCzZuYXq2",
    "origQty": "4.00000000",
    "newQty": "3.00000000",
    "time": 1741672924895
  }
]
```

## Query Unfilled Order Count (USER_DATA)（查询未成交的订单计数 (USER_DATA)）

`GET /api/v3/rateLimit/order`

Displays the user's unfilled order count for all intervals.

显示用户在所有时间间隔内的未成交订单计数。

Operation ID: `rateLimitOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Query Unfilled Order Count / 查询未成交的订单计数

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].rateLimitType | string |  | 例: `ORDERS` |
| [].interval | string |  | 例: `SECOND` |
| [].intervalNum | integer (int64) |  | 例: `10` |
| [].limit | integer (int64) |  | 例: `50` |
| [].count | integer (int64) |  | 例: `0` |

```json
[
  {
    "rateLimitType": "ORDERS",
    "interval": "SECOND",
    "intervalNum": 10,
    "limit": 50,
    "count": 0
  },
  {
    "rateLimitType": "ORDERS",
    "interval": "DAY",
    "intervalNum": 1,
    "limit": 160000,
    "count": 0
  }
]
```

## Exchange information（交易规范信息）

`GET /api/v3/exchangeInfo`

Current exchange trading rules and symbol information

获取此时的交易规范信息

Operation ID: `exchangeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Example: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"<br>示例：curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"<br>例: `ETHBTC` |
| symbols | query | string[] |  | Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D" or curl -g -X GET 'https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC"]'<br>示例：curl -X GET<br>"https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D"<br><br/> 或 <br/> curl -g -X GET<br>'https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC"]' |
| permissions | query | string[] |  | Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT"<br><br>curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D"<br>or<br>curl -g -X GET 'https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED"]'<br>示例：curl -X GET<br>"https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT" <br/><br>or <br/> curl -X GET<br>"https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D"<br><br/> or <br/> curl -g -X GET<br>'https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED"]' |
| showPermissionSets | query | boolean |  | Controls whether the content of the `permissionSets` field is populated or not.<br>用于控制是否提供 `permissionSets` 字段的内容。<br>默认: `True`<br>例: `False` |
| symbolStatus | query | string |  | Filters for symbols that have this `tradingStatus`. Cannot be used in combination with `symbols` or `symbol`.<br>用于过滤具有此 `tradingStatus` 的交易对。不能与 `symbols` 或 `symbol` 组合使用。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Exchange information / 交易规范信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| timezone | string |  | 例: `UTC` |
| serverTime | integer (int64) |  | 例: `1565246363776` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `6000` |
| rateLimits[].count | integer (int64) |  | 例: `321` |
| exchangeFilters | oneOf[] |  | Exchange filters are explained on the "Filters" page:<br>/products/spot/filters.md<br>All exchange filters are optional.<br>交易所级别过滤器在 "过滤器" 页面上进行了说明：<br>/products/spot/filters.md<br>全部交易过滤器是可选的。 |
| exchangeFilters[](oneOf 1).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDERS` |
| exchangeFilters[](oneOf 1).maxNumOrders | integer (int64) |  | 例: `1000` |
| exchangeFilters[](oneOf 2).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ALGO_ORDERS` |
| exchangeFilters[](oneOf 2).maxNumAlgoOrders | integer (int64) |  | 例: `200` |
| exchangeFilters[](oneOf 3).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` |
| exchangeFilters[](oneOf 3).maxNumIcebergOrders | integer (int64) |  | 例: `10` |
| exchangeFilters[](oneOf 4).filterType | string |  | 例: `EXCHANGE_MAX_NUM_ORDER_LISTS` |
| exchangeFilters[](oneOf 4).maxNumOrderLists | integer (int64) |  | 例: `20` |
| symbols | object[] |  |  |
| symbols[].symbol | string |  | 例: `ETHBTC` |
| symbols[].status | string |  | 例: `TRADING` |
| symbols[].baseAsset | string |  | 例: `ETH` |
| symbols[].baseAssetPrecision | integer (int64) |  | 例: `8` |
| symbols[].quoteAsset | string |  | 例: `BTC` |
| symbols[].quotePrecision | integer (int64) |  | will be removed in future api versions (v4+)<br>将在未来的 api 版本中移除 (v4+)<br>例: `8` |
| symbols[].quoteAssetPrecision | integer (int64) |  | 例: `8` |
| symbols[].baseCommissionPrecision | integer (int64) |  | 例: `8` |
| symbols[].quoteCommissionPrecision | integer (int64) |  | 例: `8` |
| symbols[].orderTypes | string[] |  |  |
| symbols[].icebergAllowed | boolean |  | 例: `True` |
| symbols[].ocoAllowed | boolean |  | 例: `True` |
| symbols[].otoAllowed | boolean |  | 例: `True` |
| symbols[].opoAllowed | boolean |  | 例: `True` |
| symbols[].quoteOrderQtyMarketAllowed | boolean |  | 例: `True` |
| symbols[].allowTrailingStop | boolean |  | 例: `False` |
| symbols[].cancelReplaceAllowed | boolean |  | 例: `False` |
| symbols[].amendAllowed | boolean |  | 例: `False` |
| symbols[].pegInstructionsAllowed | boolean |  | 例: `True` |
| symbols[].marketQuoteNotionalLimitAllowed | boolean |  | 例: `True` |
| symbols[].limitQuoteNotionalLimitAllowed | boolean |  | 例: `True` |
| symbols[].isSpotTradingAllowed | boolean |  | 例: `True` |
| symbols[].isMarginTradingAllowed | boolean |  | 例: `True` |
| symbols[].filters | oneOf[] |  | Symbol filters are explained on the "Filters" page:<br>/products/spot/filters.md<br>All symbol filters are optional.<br>交易对过滤器在"过滤器"页面上进行了说明：<br>/products/spot/filters.md<br>全部交易对过滤器是可选的。 |
| symbols[].filters[](oneOf 1).filterType | string |  | 例: `PRICE_FILTER` |
| symbols[].filters[](oneOf 1).priceExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 1).minPrice | string |  | 例: `0.00000100` |
| symbols[].filters[](oneOf 1).maxPrice | string |  | 例: `100000.00000000` |
| symbols[].filters[](oneOf 1).tickSize | string |  | 例: `0.00000100` |
| symbols[].filters[](oneOf 2).filterType | string |  | 例: `PERCENT_PRICE` |
| symbols[].filters[](oneOf 2).multiplierExponent | integer |  | 例: `4` |
| symbols[].filters[](oneOf 2).multiplierUp | string |  | 例: `1.3000` |
| symbols[].filters[](oneOf 2).multiplierDown | string |  | 例: `0.7000` |
| symbols[].filters[](oneOf 2).avgPriceMins | integer |  | 例: `5` |
| symbols[].filters[](oneOf 3).filterType | string |  | 例: `PERCENT_PRICE_BY_SIDE` |
| symbols[].filters[](oneOf 3).multiplierExponent | integer |  | 例: `4` |
| symbols[].filters[](oneOf 3).bidMultiplierUp | string |  | 例: `1.2000` |
| symbols[].filters[](oneOf 3).bidMultiplierDown | string |  | 例: `0.8000` |
| symbols[].filters[](oneOf 3).askMultiplierUp | string |  | 例: `1.2000` |
| symbols[].filters[](oneOf 3).askMultiplierDown | string |  | 例: `0.8000` |
| symbols[].filters[](oneOf 3).avgPriceMins | integer |  | 例: `5` |
| symbols[].filters[](oneOf 4).filterType | string |  | 例: `LOT_SIZE` |
| symbols[].filters[](oneOf 4).qtyExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 4).minQty | string |  | 例: `0.00010000` |
| symbols[].filters[](oneOf 4).maxQty | string |  | 例: `100000.00000000` |
| symbols[].filters[](oneOf 4).stepSize | string |  | 例: `0.00010000` |
| symbols[].filters[](oneOf 5).filterType | string |  | 例: `MIN_NOTIONAL` |
| symbols[].filters[](oneOf 5).priceExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 5).minNotional | string |  | 例: `10.00000000` |
| symbols[].filters[](oneOf 5).applyToMarket | boolean |  | 例: `True` |
| symbols[].filters[](oneOf 5).avgPriceMins | integer |  | 例: `5` |
| symbols[].filters[](oneOf 6).filterType | string |  | 例: `NOTIONAL` |
| symbols[].filters[](oneOf 6).priceExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 6).minNotional | string |  | 例: `10.00000000` |
| symbols[].filters[](oneOf 6).applyMinToMarket | boolean |  | 例: `True` |
| symbols[].filters[](oneOf 6).maxNotional | string |  | 例: `100000.00000000` |
| symbols[].filters[](oneOf 6).applyMaxToMarket | boolean |  | 例: `False` |
| symbols[].filters[](oneOf 6).avgPriceMins | integer |  | 例: `5` |
| symbols[].filters[](oneOf 7).filterType | string |  | 例: `ICEBERG_PARTS` |
| symbols[].filters[](oneOf 7).limit | integer (int64) |  | 例: `10` |
| symbols[].filters[](oneOf 8).filterType | string |  | 例: `MARKET_LOT_SIZE` |
| symbols[].filters[](oneOf 8).qtyExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 8).minQty | string |  | 例: `0.00000000` |
| symbols[].filters[](oneOf 8).maxQty | string |  | 例: `1000.00000000` |
| symbols[].filters[](oneOf 8).stepSize | string |  | 例: `0.00000000` |
| symbols[].filters[](oneOf 9).filterType | string |  | 例: `MAX_NUM_ORDERS` |
| symbols[].filters[](oneOf 9).maxNumOrders | integer (int64) |  | 例: `200` |
| symbols[].filters[](oneOf 10).filterType | string |  | 例: `MAX_NUM_ALGO_ORDERS` |
| symbols[].filters[](oneOf 10).maxNumAlgoOrders | integer (int64) |  | 例: `10` |
| symbols[].filters[](oneOf 11).filterType | string |  | 例: `MAX_NUM_ICEBERG_ORDERS` |
| symbols[].filters[](oneOf 11).maxNumIcebergOrders | integer (int64) |  | 例: `5` |
| symbols[].filters[](oneOf 12).filterType | string |  | 例: `MAX_POSITION` |
| symbols[].filters[](oneOf 12).qtyExponent | integer |  | 例: `8` |
| symbols[].filters[](oneOf 12).maxPosition | string |  | 例: `100.00000000` |
| symbols[].filters[](oneOf 13).filterType | string |  | 例: `TRAILING_DELTA` |
| symbols[].filters[](oneOf 13).minTrailingAboveDelta | integer (int64) |  | 例: `10` |
| symbols[].filters[](oneOf 13).maxTrailingAboveDelta | integer (int64) |  | 例: `2000` |
| symbols[].filters[](oneOf 13).minTrailingBelowDelta | integer (int64) |  | 例: `10` |
| symbols[].filters[](oneOf 13).maxTrailingBelowDelta | integer (int64) |  | 例: `2000` |
| symbols[].filters[](oneOf 14).filterType | string |  | 例: `T_PLUS_SELL` |
| symbols[].filters[](oneOf 14).endTime | integer (int64) |  | 例: `1741672924895` |
| symbols[].filters[](oneOf 15).filterType | string |  | 例: `MAX_NUM_ORDER_LISTS` |
| symbols[].filters[](oneOf 15).maxNumOrderLists | integer (int64) |  | 例: `20` |
| symbols[].filters[](oneOf 16).filterType | string |  | 例: `MAX_NUM_ORDER_AMENDS` |
| symbols[].filters[](oneOf 16).maxNumOrderAmends | integer (int64) |  | 例: `10` |
| symbols[].permissions | string[] |  |  |
| symbols[].permissionSets | string[][] |  |  |
| symbols[].defaultSelfTradePreventionMode | string |  | 例: `NONE` |
| symbols[].allowedSelfTradePreventionModes | string[] |  |  |
| sors | object[] |  | Optional field. Present only when SOR is available.<br>/products/spot/faqs/sor_faq.md<br>可选字段，仅当 SOR 可用时才会被显示出来。<br>/products/spot/faqs/sor_faq.md |
| sors[].baseAsset | string |  | 例: `BTC` |
| sors[].symbols | string[] |  |  |

```json
{
  "timezone": "UTC",
  "serverTime": 1565246363776,
  "rateLimits": [
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 6000
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "intervalNum": 10,
      "limit": 50
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "DAY",
      "intervalNum": 1,
      "limit": 160000
    },
    {
      "rateLimitType": "RAW_REQUESTS",
      "interval": "MINUTE",
      "intervalNum": 5,
      "limit": 61000
    }
  ],
  "exchangeFilters": [],
  "symbols": [
    {
      "symbol": "ETHBTC",
      "status": "TRADING",
      "baseAsset": "ETH",
      "baseAssetPrecision": 8,
      "quoteAsset": "BTC",
      "quotePrecision": 8,
      "quoteAssetPrecision": 8,
      "baseCommissionPrecision": 8,
      "quoteCommissionPrecision": 8,
      "orderTypes": [
        "LIMIT",
        "LIMIT_MAKER",
        "MARKET",
        "STOP_LOSS",
        "STOP_LOSS_LIMIT",
        "TAKE_PROFIT",
        "TAKE_PROFIT_LIMIT"
      ],
      "icebergAllowed": true,
      "ocoAllowed": true,
      "otoAllowed": true,
      "opoAllowed": true,
      "quoteOrderQtyMarketAllowed": true,
      "allowTrailingStop": false,
      "cancelReplaceAllowed": false,
      "amendAllowed": false,
      "pegInstructionsAllowed": true,
      "marketQuoteNotionalLimitAllowed": true,
      "limitQuoteNotionalLimitAllowed": true,
      "isSpotTradingAllowed": true,
      "isMarginTradingAllowed": true,
      "filters": [],
      "permissions": [],
      "permissionSets": [
        [
          "SPOT",
          "MARGIN"
        ]
      ],
      "defaultSelfTradePreventionMode": "NONE",
      "allowedSelfTradePreventionModes": [
        "NONE"
      ]
    }
  ],
  "sors": [
    {
      "baseAsset": "BTC",
      "symbols": [
        "BTCUSDT",
        "BTCUSDC"
      ]
    }
  ]
}
```

## Query Execution Rules（查询执行规则）

`GET /api/v3/executionRules`

Query execution rules for symbols.

查询交易对的执行规则。

权重: Parameter | Weight
--- | ---
`symbol` | 2
`symbols` | 2 for each `symbol`, capped at a max of 40
`symbolStatus` | 40
None | 40

Operation ID: `executionRules`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Query for specified symbol.<br>查询指定的交易对。<br>例: `BAZUSD` |
| symbols | query | string[] |  | Query for multiple symbols.<br>查询多个交易对。 |
| symbolStatus | query | string |  | Query for all symbols with the specified status.<br>查询指定状态的所有交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Query execution rules / 查询执行规则

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolRules | object[] |  |  |
| symbolRules[].symbol | string |  | 例: `BAZUSD` |
| symbolRules[].rules | object[] |  |  |
| symbolRules[].rules[].ruleType | string |  | 例: `PRICE_RANGE` |
| symbolRules[].rules[].bidLimitMultUp | string |  | 例: `1.0001` |
| symbolRules[].rules[].bidLimitMultDown | string |  | 例: `0.9999` |
| symbolRules[].rules[].askLimitMultUp | string |  | 例: `1.0001` |
| symbolRules[].rules[].askLimitMultDown | string |  | 例: `0.9999` |

## Test connectivity（测试服务器连通性 PING）

`GET /api/v3/ping`

Test connectivity to the Rest API.

测试能否联通

Operation ID: `ping`

### 响应 200：OK / 成功

## Check server time（获取服务器时间）

`GET /api/v3/time`

Test connectivity to the Rest API and get the current server time.

获取服务器时间

Operation ID: `time`

### 响应 200：Check server time / 获取服务器时间

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serverTime | integer (int64) |  | 例: `1499827319559` |

## Compressed/Aggregate trades list（近期成交(归集)）

`GET /api/v3/aggTrades`

Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

与trades的区别是，同一个taker在同一时间同一价格与多个maker的成交会被合并为一条记录

Operation ID: `aggTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| fromId | query | integer (int64) |  | ID to get aggregate trades from INCLUSIVE.<br>从包含fromID的成交开始返回结果<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades from INCLUSIVE.<br>从该时刻之后的成交记录开始返回结果<br>例: `1735693200000` |
| endTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades until INCLUSIVE.<br>返回该时刻为止的成交记录<br>例: `1735693200000` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |

### 响应 200：Compressed/Aggregate trades list / 近期成交(归集

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].a | integer (int64) |  | Aggregate tradeId<br>归集成交ID<br>例: `26129` |
| [].p | string |  | Price<br>成交价<br>例: `0.01633102` |
| [].q | string |  | Quantity<br>成交量<br>例: `4.70443515` |
| [].f | integer (int64) |  | First tradeId<br>被归集的首个成交ID<br>例: `27781` |
| [].l | integer (int64) |  | Last tradeId<br>被归集的末个成交ID<br>例: `27781` |
| [].T | integer (int64) |  | Timestamp<br>成交时间<br>例: `1498793709153` |
| [].m | boolean |  | Was the buyer the maker?<br>是否为主动卖出单<br>例: `True` |
| [].M | boolean |  | Was the trade the best price match?<br>是否为最优撮合单(可忽略，目前总为最优撮合)<br>例: `True` |

## Current average price（当前平均价格）

`GET /api/v3/avgPrice`

Current average price for a symbol.

当前平均价格

Operation ID: `avgPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |

### 响应 200：Current average price / 当前平均价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| mins | integer (int64) |  | Average price interval (in minutes)<br>平均价格间隔（以分钟为单位）<br>例: `5` |
| price | string |  | Average price<br>平均价格<br>例: `9.35751834` |
| closeTime | integer (int64) |  | Last trade time<br>最近成交时间<br>例: `1694061154503` |

## Order book（深度信息）

`GET /api/v3/depth`

Order book

深度信息

权重: Adjusted based on the limit:

|Limit|Request Weight
------|-------
1-100|  5
101-500| 25
501-1000| 50
1001-5000| 250

Operation ID: `depth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| limit | query | integer |  | If limit > 5000, only 5000 entries will be returned.<br>如果 limit > 5000, 最多返回5000条数据。<br>默认: `100`<br>例: `1` |
| symbolStatus | query | string |  | Filters for symbols that have this `tradingStatus`.<br>A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br>过滤具有此 `tradingStatus` 的交易对。<br>如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Order book / 深度信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| lastUpdateId | integer (int64) |  | 例: `1027024` |
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |

## Recent trades list（近期成交）

`GET /api/v3/trades`

Get recent trades.

获取近期成交

Operation ID: `getTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |

### 响应 200：Recent trades list / 近期成交

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | 例: `28457` |
| [].price | string |  | 例: `4.00000100` |
| [].qty | string |  | 例: `12.00000000` |
| [].quoteQty | string |  | 例: `48.000012` |
| [].time | integer (int64) |  | 例: `1499865549590` |
| [].isBuyerMaker | boolean |  | 例: `True` |
| [].isBestMatch | boolean |  | 例: `True` |

## Old trade lookup（查询历史成交）

`GET /api/v3/historicalTrades`

Get older trades.

查询历史成交

Operation ID: `historicalTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |
| fromId | query | integer (int64) |  | TradeId to fetch from. Default gets most recent trades.<br>从哪一条成交id开始返回，缺省返回最近的成交记录<br>例: `1` |

### 响应 200：Old trade lookup / 查询历史成交

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | 例: `28457` |
| [].price | string |  | 例: `4.00000100` |
| [].qty | string |  | 例: `12.00000000` |
| [].quoteQty | string |  | 例: `48.000012` |
| [].time | integer (int64) |  | 例: `1499865549590` |
| [].isBuyerMaker | boolean |  | 例: `True` |
| [].isBestMatch | boolean |  | 例: `True` |

## Historical Block Trades (MARKET_DATA)（查询历史大宗交易 (MARKET_DATA)）

`GET /api/v3/historicalBlockTrades`

Get block trades.

获取大宗交易记录。

Operation ID: `historicalBlockTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBBTC` |
| fromId | query | integer (int64) | 是 | Block trade ID to fetch from<br>从该大宗交易ID开始查询<br>例: `582` |
| limit | query | integer (int64) |  | Default: 500; Maximum: 1000<br>默认: 500; 最大: 1000<br>默认: `500`<br>例: `500` |

### 响应 200：Historical Block Trades / 历史大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | 例: `582` |
| [].price | string |  | 例: `0.052` |
| [].qty | string |  | 例: `5838` |
| [].quoteQty | string |  | 例: `303.576` |
| [].time | integer (int64) |  | 例: `1772506983321` |
| [].isBuyerMaker | boolean |  | 例: `True` |

## Kline/Candlestick data（K线数据）

`GET /api/v3/klines`

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

每根K线的开盘时间可视为唯一ID

Operation ID: `klines`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| interval | query | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| timeZone | query | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>例: `0` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |

### 响应 200：Kline/Candlestick data / K线数据

## Rolling window price change statistics（滚动窗口价格变动统计）

`GET /api/v3/ticker`

**Note:** This endpoint differs from `GET /api/v3/ticker/24hr`.

The statistical time range of this endpoint can be up to 59999ms longer
than the requested `windowSize`.

`openTime` starts at the beginning of a minute, while the end time is
the current time. Therefore, the actual interval can be up to 59999ms
longer than the requested window.

For example, if `closeTime` is 1641287867099 (January 04, 2022
09:17:47:099 UTC) and `windowSize` is `1d`, then `openTime` is
1641201420000 (January 3, 2022, 09:17:00 UTC).

**注意:** 此接口和 `GET /api/v3/ticker/24hr` 有所不同.

此接口统计的时间范围比请求的`windowSize`多不超过59999ms.

接口的 `openTime` 是某一分钟的起始，而结束是当前的时间. 所以实际的统计区间会比请求的时间窗口多不超过59999ms.

比如, 结束时间 `closeTime` 是 1641287867099 (January 04, 2022 09:17:47:099 UTC)
, `windowSize` 为 `1d`. 那么开始时间 `openTime` 则为 1641201420000 (January 3,
2022, 09:17:00 UTC)

权重: 4 for each requested symbol regardless of windowSize.

The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

Operation ID: `ticker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Either `symbol` or `symbols` must be provided<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>例: `BNBUSDT` |
| symbols | query | string[] |  | Either `symbol` or `symbols` must be provided<br><br>Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D<br><br>The maximum number of symbols allowed in a request is 100.<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的ticker数据都会返回. symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]<br>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D |
| windowSize | query | string |  | Units cannot be combined (e.g. `1d2h` is not allowed).<br>不可以组合使用, 比如`1d2h`<br>枚举: `1m`, `2m`, `3m`, `4m`, `5m`, `6m`, `7m`, `8m`, `9m`, `10m`, `11m`, `12m`, `13m`, `14m`, `15m`, `16m`, `17m`, `18m`, `19m`, `20m`, `21m`, `22m`, `23m`, `24m`, `25m`, `26m`, `27m`, `28m`, `29m`, `30m`, `31m`, `32m`, `33m`, `34m`, `35m`, `36m`, `37m`, `38m`, `39m`, `40m`, `41m`, `42m`, `43m`, `44m`, `45m`, `46m`, `47m`, `48m`, `49m`, `50m`, `51m`, `52m`, `53m`, `54m`, `55m`, `56m`, `57m`, `58m`, `59m`, `1h`, `2h`, `3h`, `4h`, `5h`, `6h`, `7h`, `8h`, `9h`, `10h`, `11h`, `12h`, `13h`, `14h`, `15h`, `16h`, `17h`, `18h`, `19h`, `20h`, `21h`, `22h`, `23h`, `1d`, `2d`, `3d`, `4d`, `5d`, `6d`, `7d`<br>默认: `1d`<br>例: `1m` |
| type | query | string |  | 枚举: `FULL`, `MINI`<br>默认: `FULL`<br>例: `FULL` |
| symbolStatus | query | string |  | 过滤具有此 `tradingStatus` 的交易对。<br>对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。<br>对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Rolling window price change statistics / Rolling 窗口 价格 修改 statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `LTCBTC` |
| (oneOf 1).priceChange | string |  | Absolute price change<br>价格变化<br>例: `-8.00000000` |
| (oneOf 1).priceChangePercent | string |  | Relative price change in percent<br>价格变化百分比<br>例: `-88.889` |
| (oneOf 1).weightedAvgPrice | string |  | QuoteVolume / Volume<br>QuoteVolume / 成交量<br>例: `2.60427807` |
| (oneOf 1).openPrice | string |  | 例: `0.10000000` |
| (oneOf 1).highPrice | string |  | 例: `2.00000000` |
| (oneOf 1).lowPrice | string |  | 例: `0.10000000` |
| (oneOf 1).lastPrice | string |  | 例: `2.00000000` |
| (oneOf 1).volume | string |  | 例: `39.00000000` |
| (oneOf 1).quoteVolume | string |  | Sum of (price * volume) for all trades<br>此k线内所有交易的price(价格) x volume(交易量)的总和<br>例: `13.40000000` |
| (oneOf 1).openTime | integer (int64) |  | Open time for ticker window<br>ticker的开始时间<br>例: `1656986580000` |
| (oneOf 1).closeTime | integer (int64) |  | Close time for ticker window<br>ticker的结束时间<br>例: `1657001016795` |
| (oneOf 1).firstId | integer (int64) |  | Trade IDs<br>统计时间内的第一笔trade id<br>例: `0` |
| (oneOf 1).lastId | integer (int64) |  | 例: `34` |
| (oneOf 1).count | integer (int64) |  | Number of trades in the interval<br>统计时间内交易笔数<br>例: `35` |
| (oneOf 3).symbol | string |  | 例: `LTCBTC` |
| (oneOf 3).openPrice | string |  | 例: `0.10000000` |
| (oneOf 3).highPrice | string |  | 例: `2.00000000` |
| (oneOf 3).lowPrice | string |  | 例: `0.10000000` |
| (oneOf 3).lastPrice | string |  | 例: `2.00000000` |
| (oneOf 3).volume | string |  | 例: `39.00000000` |
| (oneOf 3).quoteVolume | string |  | Sum of (price * volume) for all trades<br>此k线内所有交易的price(价格) x volume(交易量)的总和<br>例: `13.40000000` |
| (oneOf 3).openTime | integer (int64) |  | Open time for ticker window<br>ticker窗口的开始时间<br>例: `1656986580000` |
| (oneOf 3).closeTime | integer (int64) |  | Close time for ticker window<br>ticker窗口的结束时间<br>例: `1657001016795` |
| (oneOf 3).firstId | integer (int64) |  | Trade IDs<br>首笔成交id<br>例: `0` |
| (oneOf 3).lastId | integer (int64) |  | 例: `34` |
| (oneOf 3).count | integer (int64) |  | Number of trades in the interval<br>统计时间内交易笔数<br>例: `35` |

## 24hr ticker price change statistics（24hr价格变动情况）

`GET /api/v3/ticker/24hr`

24 hour rolling window price change statistics. **Careful** when accessing this with no symbol.

请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高

权重: <table>
  <thead>
      <tr>
          <th>Parameter</th>
          <th>Symbols Provided</th>
          <th>Weight</th>
      </tr>
  </thead>
  <tbody>
      <tr>
          <td rowspan="2">symbol</td>
          <td>1</td>
          <td>2</td>
      </tr>
      <tr>
          <td>symbol parameter is omitted</td>
          <td>80</td>
      </tr>
      <tr>
          <td rowspan="4">symbols</td>
          <td>1-20</td>
          <td>2</td>
      </tr>
      <tr>
          <td>21-100</td>
          <td>40</td>
      </tr>
      <tr>
          <td>101 or more</td>
          <td>80</td>
      </tr>
      <tr>
          <td>symbols parameter is omitted</td>
          <td>80</td>
      </tr>
  </tbody>
</table>

Operation ID: `ticker24hr`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Either `symbol` or `symbols` must be provided<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>例: `BNBUSDT` |
| symbols | query | string[] |  | Either `symbol` or `symbols` must be provided<br><br>Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D<br><br>The maximum number of symbols allowed in a request is 100.<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的ticker数据都会返回. symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]<br>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D |
| type | query | string |  | 枚举: `FULL`, `MINI`<br>默认: `FULL`<br>例: `FULL` |
| symbolStatus | query | string |  | 过滤具有此 `tradingStatus` 的交易对。<br>对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。<br>对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：24hr ticker price change statistics / 24hr ticker 价格 修改 statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | Symbol Name<br>交易对<br>例: `BNBBTC` |
| (oneOf 1).priceChange | string |  | 例: `-94.99999800` |
| (oneOf 1).priceChangePercent | string |  | 例: `-95.960` |
| (oneOf 1).weightedAvgPrice | string |  | 例: `0.29628482` |
| (oneOf 1).prevClosePrice | string |  | 例: `0.10002000` |
| (oneOf 1).lastPrice | string |  | Closing price of the interval<br>间隔收盘价<br>例: `4.00000200` |
| (oneOf 1).lastQty | string |  | 例: `200.00000000` |
| (oneOf 1).bidPrice | string |  | 例: `4.00000000` |
| (oneOf 1).bidQty | string |  | 例: `100.00000000` |
| (oneOf 1).askPrice | string |  | 例: `4.00000200` |
| (oneOf 1).askQty | string |  | 例: `100.00000000` |
| (oneOf 1).openPrice | string |  | Opening price of the Interval<br>间隔开盘价<br>例: `99.00000000` |
| (oneOf 1).highPrice | string |  | Highest price in the interval<br>间隔最高价<br>例: `100.00000000` |
| (oneOf 1).lowPrice | string |  | Lowest  price in the interval<br>间隔最低价<br>例: `0.10000000` |
| (oneOf 1).volume | string |  | Total trade volume (in base asset)<br>总交易量 (base asset)<br>例: `8913.30000000` |
| (oneOf 1).quoteVolume | string |  | Total trade volume (in quote asset)<br>总交易量 (quote asset)<br>例: `15.30000000` |
| (oneOf 1).openTime | integer (int64) |  | Start of the ticker interval<br>ticker间隔的开始时间<br>例: `1499783499040` |
| (oneOf 1).closeTime | integer (int64) |  | End of the ticker interval<br>ticker间隔的结束时间<br>例: `1499869899040` |
| (oneOf 1).firstId | integer (int64) |  | First tradeId<br>首笔成交id<br>例: `28385` |
| (oneOf 1).lastId | integer (int64) |  | Last tradeId<br>末笔成交id<br>例: `28460` |
| (oneOf 1).count | integer (int64) |  | Trade count<br>成交笔数<br>例: `76` |
| (oneOf 3).symbol | string |  | Symbol Name<br>交易对<br>例: `BNBBTC` |
| (oneOf 3).openPrice | string |  | Opening price of the Interval<br>间隔开盘价<br>例: `99.00000000` |
| (oneOf 3).highPrice | string |  | Highest price in the interval<br>间隔最高价<br>例: `100.00000000` |
| (oneOf 3).lowPrice | string |  | Lowest  price in the interval<br>间隔最低价<br>例: `0.10000000` |
| (oneOf 3).lastPrice | string |  | Closing price of the interval<br>间隔收盘价<br>例: `4.00000200` |
| (oneOf 3).volume | string |  | Total trade volume (in base asset)<br>总交易量 (base asset)<br>例: `8913.30000000` |
| (oneOf 3).quoteVolume | string |  | Total trade volume (in quote asset)<br>总交易量 (quote asset)<br>例: `15.30000000` |
| (oneOf 3).openTime | integer (int64) |  | Start of the ticker interval<br>ticker间隔的开始时间<br>例: `1499783499040` |
| (oneOf 3).closeTime | integer (int64) |  | End of the ticker interval<br>ticker间隔的结束时间<br>例: `1499869899040` |
| (oneOf 3).firstId | integer (int64) |  | First tradeId considered<br>统计时间内的第一笔trade id<br>例: `28385` |
| (oneOf 3).lastId | integer (int64) |  | Last tradeId considered<br>统计时间内的最后一笔trade id<br>例: `28460` |
| (oneOf 3).count | integer (int64) |  | Total trade count<br>统计时间内交易笔数<br>例: `76` |

## Symbol order book ticker（最优挂单接口）

`GET /api/v3/ticker/bookTicker`

Best price/qty on the order book for a symbol or symbols.

返回当前最优的挂单(最高买单，最低卖单)

权重: |Parameter|Symbols Provided|Weight|
|---|---|---|
|symbol| 1 |2|
| |omitted| 4|
|symbols| Any |4|

Operation ID: `tickerBookTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Parameter symbol and symbols cannot be used in combination.<br>If neither parameter is sent, `bookTickers` for all symbols will be returned in an array.<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的bookTicker数据都会返回.<br>例: `BNBUSDT` |
| symbols | query | string[] |  | Parameter symbol and symbols cannot be used in combination.<br>If neither parameter is sent, `bookTickers` for all symbols will be returned in an array.<br>Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的bookTicker数据都会返回.<br><br>symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"] 或 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D |
| symbolStatus | query | string |  | Filters for symbols that have this `tradingStatus`.<br>For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>过滤具有此 `tradingStatus` 的交易对。<br>对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。<br>对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Symbol order book ticker / 最优挂单接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `LTCBTC` |
| (oneOf 1).bidPrice | string |  | best bid price.<br>最优买单价<br>例: `4.00000000` |
| (oneOf 1).bidQty | string |  | bid/ask qty.<br>挂单量<br>例: `431.00000000` |
| (oneOf 1).askPrice | string |  | best ask price.<br>最优卖单价<br>例: `4.00000200` |
| (oneOf 1).askQty | string |  | bid/ask qty.<br>挂单量<br>例: `9.00000000` |

## Symbol price ticker（最新价格接口）

`GET /api/v3/ticker/price`

Latest price for a symbol or symbols.

返回最近价格

权重: |Parameter|Symbols Provided|Weight|
|---|---|---|
|symbol| 1 |2|
| |omitted| 4|
|symbols| Any |4|

Operation ID: `tickerPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Parameter symbol and symbols cannot be used in combination.<br>If neither parameter is sent, prices for all symbols will be returned in an array.<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的价格数据都会返回.<br>例: `BNBUSDT` |
| symbols | query | string[] |  | Parameter symbol and symbols cannot be used in combination.<br>If neither parameter is sent, prices for all symbols will be returned in an array.<br>Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D<br>参数 `symbol` 和 `symbols` 不可以一起使用<br>如果都不提供, 所有symbol的价格数据都会返回.<br><br>symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"] 或 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D |
| symbolStatus | query | string |  | Filters for symbols that have this `tradingStatus`.<br>For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>过滤具有此 `tradingStatus` 的交易对。<br>对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。<br>对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Symbol price ticker / 最新价格接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `LTCBTC` |
| (oneOf 1).price | string |  | 例: `4.00000200` |

## Trading Day Ticker（交易日行情(Ticker)）

`GET /api/v3/ticker/tradingDay`

Price change statistics for a trading day.

交易日价格变动统计。

权重: 4 for each requested symbol. The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

Operation ID: `tickerTradingDay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Either `symbol` or `symbols` must be provided.<br>`symbol` 或者 `symbols` 必须提供之<br>例: `BNBUSDT` |
| symbols | query | string[] |  | Either `symbol` or `symbols` must be provided.<br>Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D.<br>The maximum number of `symbols` allowed in a request is 100.<br>`symbol` 或者 `symbols` 必须提供之一<br>`symbols` 可以接受的格式: ["BTCUSDT","BNBUSDT"] 或者 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D.<br>`symbols` 最多可以发送100个. |
| timeZone | query | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>默认: `0`<br>例: `0` |
| type | query | string |  | 枚举: `FULL`, `MINI`<br>默认: `FULL`<br>例: `FULL` |
| symbolStatus | query | string |  | Filters for symbols that have this `tradingStatus`.<br>For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br>For multiple symbols, non-matching ones are simply excluded from the response.<br>过滤具有此 `tradingStatus` 的交易对。<br>对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。<br>对于多个交易对，响应中不会包括状态不匹配的交易对。<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Trading Day Ticker / Trading Day 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).priceChange | string |  | Absolute price change<br>绝对价格变动<br>例: `-83.13000000` |
| (oneOf 1).priceChangePercent | string |  | Relative price change in percent<br>相对价格变动百分比<br>例: `-0.317` |
| (oneOf 1).weightedAvgPrice | string |  | quoteVolume / volume<br>报价成交量 / 成交量<br>例: `26234.58803036` |
| (oneOf 1).openPrice | string |  | 例: `26304.80000000` |
| (oneOf 1).highPrice | string |  | 例: `26397.46000000` |
| (oneOf 1).lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 1).lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 1).volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 1).quoteVolume | string |  | Volume in quote asset<br>报价资产的成交量<br>例: `485217905.04210480` |
| (oneOf 1).openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 1).closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 1).firstId | integer (int64) |  | Trade ID of the first trade in the interval<br>区间内的第一个交易的交易ID<br>例: `3220151555` |
| (oneOf 1).lastId | integer (int64) |  | Trade ID of the last trade in the interval<br>区间内的最后一个交易的交易ID<br>例: `3220849281` |
| (oneOf 1).count | integer (int64) |  | Number of trades in the interval<br>区间内的交易数量<br>例: `697727` |
| (oneOf 3).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 3).openPrice | string |  | 例: `26304.80000000` |
| (oneOf 3).highPrice | string |  | 例: `26397.46000000` |
| (oneOf 3).lowPrice | string |  | 例: `26088.34000000` |
| (oneOf 3).lastPrice | string |  | 例: `26221.67000000` |
| (oneOf 3).volume | string |  | Volume in base asset<br>基础资产的成交量<br>例: `18495.35066000` |
| (oneOf 3).quoteVolume | string |  | Volume in quote asset<br>报价资产的成交量<br>例: `485217905.04210480` |
| (oneOf 3).openTime | integer (int64) |  | 例: `1695686400000` |
| (oneOf 3).closeTime | integer (int64) |  | 例: `1695772799999` |
| (oneOf 3).firstId | integer (int64) |  | Trade ID of the first trade in the interval<br>区间内的第一个交易的交易ID<br>例: `3220151555` |
| (oneOf 3).lastId | integer (int64) |  | Trade ID of the last trade in the interval<br>区间内的最后一个交易的交易ID<br>例: `3220849281` |
| (oneOf 3).count | integer (int64) |  | Number of trades in the interval<br>区间内的交易数量<br>例: `697727` |

## UIKlines（UIK线数据）

`GET /api/v3/uiKlines`

The request is similar to klines having the same parameters and
response.

`uiKlines` return modified kline data, optimized for presentation of
candlestick charts.

请求参数与响应和k线接口相同。

`uiKlines` 返回修改后的k线数据，针对k线图的呈现进行了优化。

Operation ID: `uiKlines`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| interval | query | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1s` |
| startTime | query | integer (int64) |  | 例: `1735693200000` |
| endTime | query | integer (int64) |  | 例: `1735693200000` |
| timeZone | query | string |  | Default: 0 (UTC)<br>默认值： 0 (UTC)<br>默认: `0`<br>例: `0` |
| limit | query | integer |  | 默认: `500`<br>例: `1` |

### 响应 200：UIKlines / UIK线数据

## Query Reference Price（查询参考价格）

`GET /api/v3/referencePrice`

Query the reference price for a symbol.

查询某个交易对的参考价格。

Operation ID: `referencePrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |

### 响应 200：Reference price / 参考价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BAZUSD` |
| (oneOf 1).referencePrice | string |  | Reference price. Can be `null` if no reference price is set.<br>参考价格。如果没有设置参考价格，则为 `null`。<br>例: `10.00` |
| (oneOf 1).timestamp | integer (int64) |  | Timestamp when reference price was valid.<br>参考价格有效时的时间戳。<br>例: `1770736694138` |
| (oneOf 2).symbol | string |  | 例: `BAZUSD` |
| (oneOf 2).referencePrice |  |  | Reference price. Can be `null` if no reference price is set.<br>参考价格。如果没有设置参考价格，则为 `null`。<br>例: `None` |
| (oneOf 2).timestamp | integer (int64) |  | Timestamp when reference price was valid<br>参考价格生效的时间<br>例: `1770736694138` |

### 响应 400：The symbol does not have a reference price / 该交易对没有参考价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `-2043` |
| msg | string |  | 例: `This symbol doesn't have a reference price.` |

## Query Reference Price Calculation（查询参考价格计算方式）

`GET /api/v3/referencePrice/calculation`

Describes how reference price is calculated for a given symbol.

描述某个交易对的参考价格是如何计算的。

Operation ID: `referencePriceCalculation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BNBUSDT` |
| symbolStatus | query | string |  | Supported values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>支持的值: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>枚举: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`<br>例: `TRADING` |

### 响应 200：Reference price calculation / 参考价格计算方式

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BAZUSD` |
| (oneOf 1).calculationType | string |  | Either `ARITHMETIC_MEAN` or `EXTERNAL`.<br>`ARITHMETIC_MEAN` 或 `EXTERNAL`。<br>例: `ARITHMETIC_MEAN` |
| (oneOf 1).bucketCount | integer (int64) |  | Present when calculationType is ARITHMETIC_MEAN.<br>当 calculationType 为 ARITHMETIC_MEAN 时存在。<br>例: `10` |
| (oneOf 1).bucketWidthMs | integer (int64) |  | Present when calculationType is ARITHMETIC_MEAN.<br>当 calculationType 为 ARITHMETIC_MEAN 时存在。<br>例: `1000` |
| (oneOf 2).symbol | string |  | 例: `BAZUSD` |
| (oneOf 2).calculationType | string |  | Either `ARITHMETIC_MEAN` or `EXTERNAL`.<br>`ARITHMETIC_MEAN` 或 `EXTERNAL`。<br>例: `EXTERNAL` |
| (oneOf 2).externalCalculationId | integer (int64) |  | Present when calculationType is EXTERNAL.<br>当 calculationType 为 EXTERNAL 时存在。<br>例: `42` |

### 响应 400：The symbol does not have a reference price / 该交易对没有参考价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `-2043` |
| msg | string |  | 例: `This symbol doesn't have a reference price.` |

## Order Amend Keep Priority (TRADE)（修改订单并保留优先级 (TRADE)）

`PUT /api/v3/order/amend/keepPriority`

Reduce the quantity of an existing open order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [Order Amend Keep Priority FAQ](/products/spot/faqs/order_amend_keep_priority) to learn more.

由客户发送以减少其现有当前订单的原始数量。

这个请求将添加0个订单到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

请阅读 [保留优先权的修改订单常见问题](/products/spot/faqs/order_amend_keep_priority) 了解更多信息。

Operation ID: `orderAmendKeepPriority`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| orderId | integer (int64) |  | `orderId` or `origClientOrderId` must be sent<br>需提供 `orderId` 或 `origClientOrderId`。<br>例: `1` |
| origClientOrderId | string |  | `orderId` or `origClientOrderId` must be sent<br>需提供 `orderId` 或 `origClientOrderId`。<br>例: `myOrder1` |
| newClientOrderId | string |  | The new client order ID for the order after being amended. <br> If not sent, one will be randomly generated. <br> It is possible to reuse the current clientOrderId by sending it as the `newClientOrderId`.<br>订单在被修改后被赋予的新 client order ID。 <br> 如果未发送则自动生成。 <br> 可以将当前 clientOrderId 作为 `newClientOrderId` 发送来重用当前 clientOrderId 的值。<br>例: `myOrder2` |
| newQty | number (float) | 是 | `newQty` must be greater than 0 and less than the order's quantity.<br>交易的新数量。 `newQty` 必须大于0, 但是必须比订单的原始数量小。<br>例: `5` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Order Amend Keep Priority / 修改订单并保留优先级

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).transactTime | integer (int64) |  | 例: `1741926410255` |
| (oneOf 1).executionId | integer (int64) |  | 例: `75` |
| (oneOf 1).amendedOrder | object |  |  |
| (oneOf 1).amendedOrder.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).amendedOrder.orderId | integer (int64) |  | 例: `33` |
| (oneOf 1).amendedOrder.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 1).amendedOrder.origClientOrderId | string |  | 例: `5xrgbMyg6z36NzBn2pbT8H` |
| (oneOf 1).amendedOrder.clientOrderId | string |  | 例: `PFaq6hIHxqFENGfdtn4J6Q` |
| (oneOf 1).amendedOrder.price | string |  | 例: `6.00000000` |
| (oneOf 1).amendedOrder.qty | string |  | 例: `5.00000000` |
| (oneOf 1).amendedOrder.executedQty | string |  | 例: `0.00000000` |
| (oneOf 1).amendedOrder.preventedQty | string |  | 例: `0.00000000` |
| (oneOf 1).amendedOrder.quoteOrderQty | string |  | 例: `0.00000000` |
| (oneOf 1).amendedOrder.cumulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 1).amendedOrder.status | string |  | 例: `NEW` |
| (oneOf 1).amendedOrder.timeInForce | string |  | 例: `GTC` |
| (oneOf 1).amendedOrder.type | string |  | 例: `LIMIT` |
| (oneOf 1).amendedOrder.side | string |  | 例: `SELL` |
| (oneOf 1).amendedOrder.workingTime | integer (int64) |  | 例: `1741926410242` |
| (oneOf 1).amendedOrder.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).transactTime | integer (int64) |  | 例: `1741926410255` |
| (oneOf 2).executionId | integer (int64) |  | 例: `75` |
| (oneOf 2).amendedOrder | object |  |  |
| (oneOf 2).amendedOrder.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).amendedOrder.orderId | integer (int64) |  | 例: `33` |
| (oneOf 2).amendedOrder.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 2).amendedOrder.origClientOrderId | string |  | 例: `5xrgbMyg6z36NzBn2pbT8H` |
| (oneOf 2).amendedOrder.clientOrderId | string |  | 例: `PFaq6hIHxqFENGfdtn4J6Q` |
| (oneOf 2).amendedOrder.price | string |  | 例: `6.00000000` |
| (oneOf 2).amendedOrder.qty | string |  | 例: `5.00000000` |
| (oneOf 2).amendedOrder.executedQty | string |  | 例: `0.00000000` |
| (oneOf 2).amendedOrder.preventedQty | string |  | 例: `0.00000000` |
| (oneOf 2).amendedOrder.quoteOrderQty | string |  | 例: `0.00000000` |
| (oneOf 2).amendedOrder.cumulativeQuoteQty | string |  | 例: `0.00000000` |
| (oneOf 2).amendedOrder.status | string |  | 例: `NEW` |
| (oneOf 2).amendedOrder.timeInForce | string |  | 例: `GTC` |
| (oneOf 2).amendedOrder.type | string |  | 例: `LIMIT` |
| (oneOf 2).amendedOrder.side | string |  | 例: `SELL` |
| (oneOf 2).amendedOrder.workingTime | integer (int64) |  | 例: `1741926410242` |
| (oneOf 2).amendedOrder.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 2).amendedOrder.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| (oneOf 2).amendedOrder.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| (oneOf 2).amendedOrder.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| (oneOf 2).amendedOrder.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| (oneOf 2).amendedOrder.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| (oneOf 2).amendedOrder.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| (oneOf 2).amendedOrder.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| (oneOf 2).amendedOrder.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| (oneOf 2).amendedOrder.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| (oneOf 2).amendedOrder.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| (oneOf 2).amendedOrder.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| (oneOf 2).amendedOrder.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| (oneOf 2).amendedOrder.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| (oneOf 2).amendedOrder.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| (oneOf 2).amendedOrder.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| (oneOf 2).listStatus | object |  |  |
| (oneOf 2).listStatus.orderListId | integer (int64) |  | 例: `1` |
| (oneOf 2).listStatus.contingencyType | string |  | 例: `OTO` |
| (oneOf 2).listStatus.listOrderStatus | string |  | 例: `EXECUTING` |
| (oneOf 2).listStatus.listClientOrderId | string |  | 例: `AT7FTxZXylVSwRoZs52mt3` |
| (oneOf 2).listStatus.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).listStatus.orders | object[] |  |  |
| (oneOf 2).listStatus.orders[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).listStatus.orders[].orderId | integer (int64) |  | 例: `8` |
| (oneOf 2).listStatus.orders[].clientOrderId | string |  | 例: `GkwwHZUUbFtZOoH1YsZk9Q` |

## Cancel an Existing Order and Send a New Order (TRADE)（撤消挂单再下单 (TRADE)）

`POST /api/v3/order/cancelReplace`

- Cancels an existing order and places a new order on the same symbol.
- Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.
- A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.
- You can only cancel an individual order from an orderList using this endpoint, but the result is the same as canceling the entire orderList.

- 撤消挂单并在同个交易对上重新下单。
- 在撤消订单和下单前会判断: 1) 过滤器参数, 以及 2) 目前下单数量。
- 即使请求中没有尝试发送新订单，比如(`newOrderResult: NOT_ATTEMPTED`)，未成交订单的数量仍然会加1。
- 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。

Operation ID: `orderCancelReplace`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | 枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| cancelReplaceMode | string | 是 | The allowed values are: <br/> `STOP_ON_FAILURE` - If the cancel request fails, the new order placement will not be attempted. <br/> `ALLOW_FAILURE` - new order placement will be attempted even if cancel request fails.<br>指定类型：`STOP_ON_FAILURE` - 如果撤消订单失败将不会继续重新下单。<br/> `ALLOW_FAILURE` - 不管撤消订单是否成功都会继续重新下单。<br>枚举: `STOP_ON_FAILURE`, `ALLOW_FAILURE`<br>例: `STOP_ON_FAILURE` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| quantity | number (float) |  | 例: `1` |
| quoteOrderQty | number (float) |  | 例: `1` |
| price | number (float) |  | 例: `400` |
| cancelNewClientOrderId | string |  | Used to uniquely identify this cancel. Automatically generated by default.<br>用户自定义的id，如空缺系统会自动赋值<br>例: `cancelMyOrder1` |
| cancelOrigClientOrderId | string |  | Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br> If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br> If both conditions are not met the request will be rejected.<br>必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。<br>例: `myOrder1` |
| cancelOrderId | integer (int64) |  | Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br>If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br>If both conditions are not met the request will be rejected.<br>必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。<br>例: `1` |
| newClientOrderId | string |  | Used to identify the new order.<br>用于辨识新订单。<br>例: `myOrder2` |
| strategyId | integer (int64) |  | 例: `1` |
| strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| stopPrice | number (float) |  | 例: `1` |
| trailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参考 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| icebergQty | number (float) |  | 例: `1` |
| newOrderRespType | string |  | Allowed values: <br/> `ACK`, `RESULT`, `FULL` <br/> `MARKET` and `LIMIT` orders types default to `FULL`; all other orders default to `ACK`<br>指定响应类型: <br/> 指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`， 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/products/spot/enums#stpmodes).<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| cancelRestrictions | string |  | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).<br>支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。<br>枚举: `ONLY_NEW`, `ONLY_PARTIALLY_FILLED`<br>例: `ONLY_NEW` |
| orderRateLimitExceededMode | string |  | Supported values: <br> `DO_NOTHING` (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit<br> `CANCEL_ONLY` - will always cancel the order<br>支持的值： <br></br> `DO_NOTHING`（默认值）- 仅在账户未超过未成交订单频率限制时，会尝试取消订单。<br></br> `CANCEL_ONLY` - 将始终取消订单。<br>枚举: `DO_NOTHING`, `CANCEL_ONLY`<br>例: `DO_NOTHING` |
| pegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG` <br> See Pegged Orders<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 <br> 参阅 关于挂钩订单参数的注意事项<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pegOffsetValue | integer |  | Price level to peg the price to (max: 100) <br> See Pegged Orders<br>用于挂钩的价格水平（最大值：100）。 <br> 参阅 关于挂钩订单参数的注意事项<br>例: `1` |
| pegOffsetType | string |  | Only `PRICE_LEVEL` is supported <br> See Pegged Orders.<br>仅支持 `PRICE_LEVEL`。 <br> 参阅 关于挂钩订单参数的注意事项<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| quoteNotionalLimit | number (float) |  | For replacement orders on the BUY side only. Maximum quote-asset notional the replacement order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单方向的新订单。新订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Cancel an existing order and send a new order / 撤消挂单再下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| cancelResult | string |  | 例: `SUCCESS` |
| newOrderResult | string |  | 例: `SUCCESS` |
| cancelResponse | object |  |  |
| cancelResponse.symbol | string |  | 例: `BTCUSDT` |
| cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `DnLo3vTAQcjha43lAZhZ0y` |
| cancelResponse.orderId | integer (int64) |  | 例: `9` |
| cancelResponse.orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `osxN3JXAtJvKvCqGeMWMVR` |
| cancelResponse.transactTime | integer (int64) |  | 例: `1684804350068` |
| cancelResponse.price | string |  | 例: `0.01000000` |
| cancelResponse.origQty | string |  | 例: `0.000100` |
| cancelResponse.executedQty | string |  | 例: `0.00000000` |
| cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| cancelResponse.cummulativeQuoteQty | string |  | 例: `0.00000000` |
| cancelResponse.status | string |  | 例: `CANCELED` |
| cancelResponse.timeInForce | string |  | 例: `GTC` |
| cancelResponse.type | string |  | 例: `LIMIT` |
| cancelResponse.side | string |  | 例: `SELL` |
| cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| cancelResponse.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| cancelResponse.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| cancelResponse.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| cancelResponse.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| cancelResponse.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| cancelResponse.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| cancelResponse.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| cancelResponse.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| cancelResponse.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| cancelResponse.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| cancelResponse.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| cancelResponse.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| cancelResponse.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| cancelResponse.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| cancelResponse.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |
| newOrderResponse | object |  |  |
| newOrderResponse.symbol | string |  | 例: `BTCUSDT` |
| newOrderResponse.orderId | integer (int64) |  | 例: `10` |
| newOrderResponse.orderListId | integer (int64) |  | Unless it's part of an order list, value will be -1<br>除非此单是订单列表的一部分, 否则此值为 -1<br>例: `-1` |
| newOrderResponse.clientOrderId | string |  | 例: `wOceeeOzNORyLiQfw7jd8S` |
| newOrderResponse.transactTime | integer (int64) |  | 例: `1652928801803` |
| newOrderResponse.price | string |  | 例: `0.02000000` |
| newOrderResponse.origQty | string |  | 例: `0.040000` |
| newOrderResponse.executedQty | string |  | 例: `0.00000000` |
| newOrderResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| newOrderResponse.cummulativeQuoteQty | string |  | 例: `0.00000000` |
| newOrderResponse.status | string |  | 例: `NEW` |
| newOrderResponse.timeInForce | string |  | 例: `GTC` |
| newOrderResponse.type | string |  | 例: `LIMIT` |
| newOrderResponse.side | string |  | 例: `BUY` |
| newOrderResponse.workingTime | integer (int64) |  | 例: `1669277163808` |
| newOrderResponse.fills | object[] |  |  |
| newOrderResponse.fills[].price | string |  | 例: `4000.00000000` |
| newOrderResponse.fills[].qty | string |  | 例: `1.00000000` |
| newOrderResponse.fills[].commission | string |  | 例: `4.00000000` |
| newOrderResponse.fills[].commissionAsset | string |  | 例: `USDT` |
| newOrderResponse.fills[].tradeId | integer (int64) |  | 例: `12345` |
| newOrderResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| newOrderResponse.icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| newOrderResponse.preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| newOrderResponse.preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| newOrderResponse.stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| newOrderResponse.strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| newOrderResponse.strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| newOrderResponse.trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| newOrderResponse.trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| newOrderResponse.usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| newOrderResponse.workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| newOrderResponse.pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| newOrderResponse.pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| newOrderResponse.pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| newOrderResponse.peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| newOrderResponse.expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

### 响应 400：Order cancel-replace failed / 撤消挂单再下单失败

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).code | integer (int64) |  | 例: `-2022` |
| (oneOf 1).msg | string |  | 例: `Order cancel-replace failed.` |
| (oneOf 1).data | object |  |  |
| (oneOf 1).data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 1).data.newOrderResult | string |  | 例: `NOT_ATTEMPTED` |
| (oneOf 1).data.cancelResponse | object |  |  |
| (oneOf 1).data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 1).data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 1).data.newOrderResponse |  |  | 例: `None` |
| (oneOf 2).code | integer (int64) |  | 例: `-2022` |
| (oneOf 2).msg | string |  | 例: `Order cancel-replace failed.` |
| (oneOf 2).data | object |  |  |
| (oneOf 2).data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 2).data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 2).data.cancelResponse | object |  |  |
| (oneOf 2).data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 2).data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 2).data.newOrderResponse | object |  |  |
| (oneOf 2).data.newOrderResponse.code | integer (int64) |  | 例: `-2010` |
| (oneOf 2).data.newOrderResponse.msg | string |  | 例: `Order would immediately match and take.` |

### 响应 409：Order cancel-replace partially failed / 撤消挂单再下单部分失败

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).code | integer (int64) |  | 例: `-2021` |
| (oneOf 1).msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 1).data | object |  |  |
| (oneOf 1).data.cancelResult | string |  | 例: `SUCCESS` |
| (oneOf 1).data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 1).data.cancelResponse | object |  |  |
| (oneOf 1).data.cancelResponse.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).data.cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `86M8erehfExV8z2RC8Zo8k` |
| (oneOf 1).data.cancelResponse.orderId | integer (int64) |  | 例: `3` |
| (oneOf 1).data.cancelResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 1).data.cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `G1kLo6aDv2KGNTFcjfTSFq` |
| (oneOf 1).data.cancelResponse.transactTime | integer (int64) |  | 例: `1684804350068` |
| (oneOf 1).data.cancelResponse.price | string |  | 例: `0.006123` |
| (oneOf 1).data.cancelResponse.origQty | string |  | 例: `10000.000000` |
| (oneOf 1).data.cancelResponse.executedQty | string |  | 例: `0.000000` |
| (oneOf 1).data.cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 1).data.cancelResponse.cummulativeQuoteQty | string |  | 例: `0.000000` |
| (oneOf 1).data.cancelResponse.status | string |  | 例: `CANCELED` |
| (oneOf 1).data.cancelResponse.timeInForce | string |  | 例: `GTC` |
| (oneOf 1).data.cancelResponse.type | string |  | 例: `LIMIT_MAKER` |
| (oneOf 1).data.cancelResponse.side | string |  | 例: `SELL` |
| (oneOf 1).data.cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 1).data.newOrderResponse | object |  |  |
| (oneOf 1).data.newOrderResponse.code | integer (int64) |  | 例: `-2010` |
| (oneOf 1).data.newOrderResponse.msg | string |  | 例: `Order would immediately match and take.` |
| (oneOf 2).code | integer (int64) |  | 例: `-2021` |
| (oneOf 2).msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 2).data | object |  |  |
| (oneOf 2).data.cancelResult | string |  | 例: `FAILURE` |
| (oneOf 2).data.newOrderResult | string |  | 例: `SUCCESS` |
| (oneOf 2).data.cancelResponse | object |  |  |
| (oneOf 2).data.cancelResponse.code | integer (int64) |  | 例: `-2011` |
| (oneOf 2).data.cancelResponse.msg | string |  | 例: `Unknown order sent.` |
| (oneOf 2).data.newOrderResponse | object |  |  |
| (oneOf 2).data.newOrderResponse.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).data.newOrderResponse.orderId | integer (int64) |  | 例: `11` |
| (oneOf 2).data.newOrderResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 2).data.newOrderResponse.clientOrderId | string |  | 例: `pfojJMg6IMNDKuJqDxvoxN` |
| (oneOf 2).data.newOrderResponse.transactTime | integer (int64) |  | 例: `1648540168818` |
| (oneOf 3).code | integer (int64) |  | 例: `-2021` |
| (oneOf 3).msg | string |  | 例: `Order cancel-replace partially failed.` |
| (oneOf 3).data | object |  |  |
| (oneOf 3).data.cancelResult | string |  | 例: `SUCCESS` |
| (oneOf 3).data.newOrderResult | string |  | 例: `FAILURE` |
| (oneOf 3).data.cancelResponse | object |  |  |
| (oneOf 3).data.cancelResponse.symbol | string |  | 例: `LTCBNB` |
| (oneOf 3).data.cancelResponse.origClientOrderId | string |  | cancelOrigClientOrderId from request<br>请求的 cancelOrigClientOrderId<br>例: `GKt5zzfOxRDSQLveDYCTkc` |
| (oneOf 3).data.cancelResponse.orderId | integer (int64) |  | 例: `64` |
| (oneOf 3).data.cancelResponse.orderListId | integer (int64) |  | 例: `-1` |
| (oneOf 3).data.cancelResponse.clientOrderId | string |  | cancelNewClientOrderId from request<br>请求的 cancelNewClientOrderId<br>例: `loehOJF3FjoreUBDmv739R` |
| (oneOf 3).data.cancelResponse.transactTime | integer (int64) |  | 例: `1715779007228` |
| (oneOf 3).data.cancelResponse.price | string |  | 例: `1.00` |
| (oneOf 3).data.cancelResponse.origQty | string |  | 例: `10.00000000` |
| (oneOf 3).data.cancelResponse.executedQty | string |  | 例: `0.00000000` |
| (oneOf 3).data.cancelResponse.origQuoteOrderQty | string |  | 例: `0.000000` |
| (oneOf 3).data.cancelResponse.cummulativeQuoteQty | string |  | 例: `0.00` |
| (oneOf 3).data.cancelResponse.status | string |  | 例: `CANCELED` |
| (oneOf 3).data.cancelResponse.timeInForce | string |  | 例: `GTC` |
| (oneOf 3).data.cancelResponse.type | string |  | 例: `LIMIT` |
| (oneOf 3).data.cancelResponse.side | string |  | 例: `SELL` |
| (oneOf 3).data.cancelResponse.selfTradePreventionMode | string |  | 例: `NONE` |
| (oneOf 3).data.newOrderResponse | object |  |  |
| (oneOf 3).data.newOrderResponse.code | integer (int64) |  | 例: `-1015` |
| (oneOf 3).data.newOrderResponse.msg | string |  | 例: `Too many orders placed without trading; current limit is 1 non-trading orders per 10 SECOND. Unable to place new orders until trades occur or window resets.` |

### 响应 429：Too many new orders / 新订单过多

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `-1015` |
| msg | string |  | 例: `Too many orders placed without trading; current limit is 1 non-trading orders per 10 SECOND. Unable to place new orders until trades occur or window resets.` |

## New Order list - OCO (TRADE)（新订单列表 - OCO (TRADE)）

`POST /api/v3/orderList/oco`

Send in an one-cancels-the-other (OCO) pair, where activation of one
order immediately cancels the other.

- An OCO has 2 orders called the **above order** and **below order**.
- One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
- Price restrictions
  - If the OCO is on the `SELL` side:
    - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price >  `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    - `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
  - If the OCO is on the `BUY` side:
    - `LIMIT_MAKER/TAKE_PROFIT_LIMIT price` < Last Traded Price < `stopPrice`
    - `TAKE_PROFIT stopPrice` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT stopPrice` * OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
- OCOs add 2 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

- OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单**。
- 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
- 针对价格限制：
  - 如果 OCO 订单方向是 `SELL`：
    - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 >  `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    - `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
  - 如果 OCO 订单方向是 `BUY`：
    - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` < 最后交易价格 < `stopPrice`
    - `TAKE_PROFIT` `stopPrice` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
- OCO 会添加 **2个订单** 到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderListOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowClientOrderId`.<br>整个 OCO order list 的唯一ID。 如果未发送则自动生成。 仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。 `listClientOrderId` 与 `aboveClientOrderId` 和 `belowClientOrderId` 不同。<br>例: `lH1YDkuQKWiXVXHPSKYEIp` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | Quantity for both orders of the order list.<br>两个订单的数量。<br>例: `1` |
| aboveType | string | 是 | 枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| aboveClientOrderId | string |  | Arbitrary unique ID among open orders for the above order. Automatically generated if not sent.<br>上方订单的唯一ID。 如果未发送则自动生成。<br>例: `aboveOrder1` |
| aboveIcebergQty | integer (int64) |  | Note that this can only be used if `aboveTimeInForce` is `GTC`.<br>请注意，只有当 `aboveTimeInForce` 为 `GTC` 时才能使用。<br>例: `1` |
| abovePrice | number (float) |  | Can be used if `aboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1.5` |
| aboveStopPrice | number (float) |  | Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.<br>如果 `aboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `aboveStopPrice` 或 `aboveTrailingDelta` 或两者。<br>例: `1.50000001` |
| aboveTrailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| aboveTimeInForce | string |  | Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `aboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| aboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the above order within an order strategy.<br>订单策略中上方订单的 ID。<br>例: `1` |
| aboveStrategyType | integer |  | Arbitrary numeric value identifying the above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>上方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| abovePegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| abovePegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| abovePegOffsetValue | integer |  | 例: `1` |
| belowType | string | 是 | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持值：`STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`。<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| belowClientOrderId | string |  | Arbitrary unique ID among open orders for the below order. Automatically generated if not sent.<br>下方订单的唯一ID。 如果未发送则自动生成。<br>例: `belowOrder1` |
| belowIcebergQty | integer (int64) |  | Note that this can only be used if `belowTimeInForce` is `GTC`.<br>请注意，只有当 `belowTimeInForce` 为 `GTC` 时才能使用。<br>例: `1` |
| belowPrice | number (float) |  | Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1.49999999` |
| belowStopPrice | number (float) |  | Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.<br>如果 `belowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `belowStopPrice` 或 `belowTrailingDelta` 或两者。<br>例: `1.50000001` |
| belowTrailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| belowTimeInForce | string |  | Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `belowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| belowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the below order within an order strategy.<br>订单策略中下方订单的 ID。<br>例: `1` |
| belowStrategyType | integer |  | Arbitrary numeric value identifying the below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>下方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| belowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| belowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| belowPegOffsetValue | integer |  | 例: `1` |
| newOrderRespType | string |  | Select response format: `ACK`, `RESULT`, `FULL`.<br>响应格式可选值: `ACK`, `RESULT`, `FULL`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对上的配置。 支持值：[STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| aboveQuoteNotionalLimit | number (float) |  | Quote notional limit for the above order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| belowQuoteNotionalLimit | number (float) |  | Quote notional limit for the below order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New Order list - OCO / New 订单 列表 - OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `1` |
| contingencyType | string |  | 例: `OCO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `lH1YDkuQKWiXVXHPSKYEIp` |
| transactionTime | integer (int64) |  | 例: `1710485608839` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `10` |
| orders[].clientOrderId | string |  | 例: `44nZvqpemY7sVYgPYbvPih` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | 例: `10` |
| orderReports[].orderListId | integer (int64) |  | 例: `1` |
| orderReports[].clientOrderId | string |  | 例: `44nZvqpemY7sVYgPYbvPih` |
| orderReports[].transactTime | integer (int64) |  | 例: `1710485608839` |
| orderReports[].price | string |  | 例: `1.00000000` |
| orderReports[].origQty | string |  | 例: `5.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `STOP_LOSS_LIMIT` |
| orderReports[].side | string |  | 例: `SELL` |
| orderReports[].workingTime | integer (int64) |  | 例: `-1` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].stopPrice | string |  | 例: `1.00000000` |
| orderReports[].icebergQty | string |  | 例: `1.00000000` |

## New Order List - OPO (TRADE)（新订单列表 - OPO (TRADE)）

`POST /api/v3/orderList/opo`

Place an [OPO](/products/spot/faqs/opo).

- The working order must be `LIMIT` or `LIMIT_MAKER`.
- OPOs add 2 orders to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 [OPO](/products/spot/faqs/opo) 订单。

- 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
- OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。

Operation ID: `orderListOpo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。<br>例: `H94qCqO27P74OEiO4X8HOG` |
| newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值：`LIMIT`，`LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `workingOrder1` |
| workingPrice | number (float) | 是 | Price for the working order.<br>生效订单价格<br>例: `1` |
| workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>设置生效订单的数量<br>例: `1` |
| workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>用于标识订单策略中生效订单的任意数字值<br>例: `1` |
| workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| workingPegOffsetValue | integer |  | 例: `1` |
| pendingType | string | 是 | Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using `quoteOrderQty` are not supported.<br>支持的数值：[订单类型](/products/spot/enums#ordertypes)。注意，不支持使用 `quoteOrderQty` 的 `MARKET` 订单。<br>枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingClientOrderId | string |  | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>待处理订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingOrder1` |
| pendingPrice | number (float) |  | Price for the pending order.<br>待处理订单价格<br>例: `1` |
| pendingStopPrice | number (float) |  | Stop price for the pending order.<br>待处理订单止损价格<br>例: `1` |
| pendingTrailingDelta | number (float) |  | Trailing delta for the pending order.<br>待处理订单跟踪止损差值<br>例: `1` |
| pendingIcebergQty | number (float) |  | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.<br>仅当 `pendingTimeInForce` 为 `GTC` 或 `pendingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| pendingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending order within an order strategy.<br>用于标识订单策略中待处理订单的任意数字值<br>例: `1` |
| pendingStrategyType | integer |  | Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| pendingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingPegOffsetValue | integer |  | 例: `1` |
| workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New Order List - OPO / New 订单 列表- OPO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `0` |
| contingencyType | string |  | 例: `OTO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `H94qCqO27P74OEiO4X8HOG` |
| transactionTime | integer (int64) |  | 例: `1762998011671` |
| symbol | string |  | 例: `BTCUSDT` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `BTCUSDT` |
| orders[].orderId | integer (int64) |  | 例: `2` |
| orders[].clientOrderId | string |  | 例: `JX6xfdjo0wysiGumfHNmPu` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `BTCUSDT` |
| orderReports[].orderId | integer (int64) |  | 例: `2` |
| orderReports[].orderListId | integer (int64) |  | 例: `0` |
| orderReports[].clientOrderId | string |  | 例: `JX6xfdjo0wysiGumfHNmPu` |
| orderReports[].transactTime | integer (int64) |  | 例: `1762998011671` |
| orderReports[].price | string |  | 例: `102264.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.00000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `LIMIT` |
| orderReports[].side | string |  | 例: `BUY` |
| orderReports[].workingTime | integer (int64) |  | 例: `1762998011671` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].origQty | string |  | 例: `0.00060000` |
| orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## New Order List - OPOCO (TRADE)（新订单列表 - OPOCO (TRADE)）

`POST /api/v3/orderList/opoco`

Place an [OPOCO](/products/spot/faqs/opo).

- The working order must be `LIMIT` or `LIMIT_MAKER`.

发送一个 [OPOCO](/products/spot/faqs/opo) 订单。

- 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。

Operation ID: `orderListOpoco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.<br>订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。<br>例: `bcedxMpQG6nFrZUPQyshoL` |
| newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值：`LIMIT`，`LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。<br>例: `workingOrder1` |
| workingPrice | number (float) | 是 | Price for the working order.<br>生效订单价格<br>例: `1` |
| workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>设置生效订单的数量<br>例: `1` |
| workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用<br>例: `1` |
| workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>用于标识订单策略中生效订单的任意数字值<br>例: `1` |
| workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| workingPegOffsetType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| workingPegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingAboveType | string | 是 | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| pendingAboveClientOrderId | string |  | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>待处理"上方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingAboveOrder1` |
| pendingAbovePrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingAboveType` 为 `STOP_LOSS_LIMIT`、`LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。<br>例: `1` |
| pendingAboveStopPrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.<br>当 `pendingAboveType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT`、`TAKE_PROFIT_LIMIT` 时可用。<br>例: `1` |
| pendingAboveTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| pendingAboveIcebergQty | number (float) |  | This can only be used if `pendingAboveTimeInForce` is `GTC` or `pendingAboveType` is `LIMIT_MAKER`.<br>仅当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时可用。<br>例: `1` |
| pendingAboveTimeInForce | string |  | Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingAboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending above order within an order strategy.<br>用于标识订单策略中待处理上方订单的任意数字值。<br>例: `1` |
| pendingAboveStrategyType | integer |  | Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理上方订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。<br>例: `1` |
| pendingAbovePegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingAbovePegOffsetType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingAbovePegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| pendingBelowType | string |  | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值：`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| pendingBelowClientOrderId | string |  | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>待处理"下方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。<br>例: `pendingBelowOrder1` |
| pendingBelowPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。<br>例: `1` |
| pendingBelowStopPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.<br>当 `pendingBelowType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 时可用。`pendingBelowStopPrice`、`pendingBelowTrailingDelta` 或两者之一必须被指定。<br>例: `1` |
| pendingBelowTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| pendingBelowIcebergQty | number (float) |  | This can only be used if `pendingBelowTimeInForce` is `GTC` or `pendingBelowType` is `LIMIT_MAKER`.<br>仅当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时可用。<br>例: `1` |
| pendingBelowTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingBelowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending below order within an order strategy.<br>用于标识订单策略中待处理下方订单的任意数字值。<br>例: `1` |
| pendingBelowStrategyType | integer |  | Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理下方订单策略的任意数字值。小于 `1000000` 为保留值，不能使用。<br>例: `1` |
| pendingBelowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingBelowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingBelowPegOffsetValue | integer |  | 例: `1` |
| workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New Order List - OPOCO / New 订单 列表- OPOCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `2` |
| contingencyType | string |  | 例: `OTO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `bcedxMpQG6nFrZUPQyshoL` |
| transactionTime | integer (int64) |  | 例: `1763000506354` |
| symbol | string |  | 例: `BTCUSDT` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `BTCUSDT` |
| orders[].orderId | integer (int64) |  | 例: `9` |
| orders[].clientOrderId | string |  | 例: `OLSBhMWaIlLSzZ9Zm7fnKB` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `BTCUSDT` |
| orderReports[].orderId | integer (int64) |  | 例: `9` |
| orderReports[].orderListId | integer (int64) |  | 例: `2` |
| orderReports[].clientOrderId | string |  | 例: `OLSBhMWaIlLSzZ9Zm7fnKB` |
| orderReports[].transactTime | integer (int64) |  | 例: `1763000506354` |
| orderReports[].price | string |  | 例: `102496.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.00000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `LIMIT` |
| orderReports[].side | string |  | 例: `BUY` |
| orderReports[].workingTime | integer (int64) |  | 例: `1763000506354` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].origQty | string |  | 例: `0.00170000` |
| orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## New Order list - OTO (TRADE)（新订单列表 - OTO (TRADE)）

`POST /api/v3/orderList/oto`

Place an OTO.

- An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
- The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
- The second order is called the **pending order**. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets **fully filled**.
- If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
- When the order list is placed, if the working order gets **immediately fully filled**, the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
- OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 OTO 订单。

- 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.
- 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
- 第二个订单被称为**待处理订单**。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET` 订单。只有当生效订单**完全成交**时，待处理订单才会被自动下单。
- 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。
- 如果生效订单在下订单列表后**立即完全成交**，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为 `PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。
- `OTO` 订单将**2 个订单**添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderListOto`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。 `listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。<br>例: `yl2ERtcar1o25zcWtqVBTC` |
| newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值： `LIMIT`， `LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>用于标识生效订单的唯一ID。 如果未发送则自动生成。<br>例: `workingOrder1` |
| workingPrice | number (float) | 是 | 例: `1` |
| workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>用于设置生效订单的数量。<br>例: `1` |
| workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。<br>例: `1` |
| workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>订单策略中用于标识生效订单的 ID。<br>例: `1` |
| workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| pendingType | string | 是 | Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using `quoteOrderQty` are not supported.<br>支持的数值： [订单类型](/products/spot/enums#ordertypes) 请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。<br>枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| workingPegOffsetValue | integer |  | 例: `1` |
| pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingClientOrderId | string |  | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>用于标识待处理订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingOrder1` |
| pendingPrice | number (float) |  | 例: `1` |
| pendingStopPrice | number (float) |  | 例: `1` |
| pendingTrailingDelta | number (float) |  | 例: `1` |
| pendingQuantity | number (float) | 是 | Sets the quantity for the pending order.<br>用于设置待处理订单的数量。<br>例: `1` |
| pendingIcebergQty | number (float) |  | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.<br>只有当 `pendingTimeInForce` 为 `GTC` 或者当 `pendingType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| pendingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending order within an order strategy.<br>订单策略中用于标识待处理订单的 ID。<br>例: `1` |
| pendingStrategyType | integer |  | Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| pendingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingPegOffsetValue | integer |  | 例: `1` |
| workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| pendingQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New Order list - OTO / New 订单 列表- OTO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `0` |
| contingencyType | string |  | 例: `OTO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `yl2ERtcar1o25zcWtqVBTC` |
| transactionTime | integer (int64) |  | 例: `1712289389158` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `4` |
| orders[].clientOrderId | string |  | 例: `Bq17mn9fP6vyCn75Jw1xya` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | 例: `4` |
| orderReports[].orderListId | integer (int64) |  | 例: `0` |
| orderReports[].clientOrderId | string |  | 例: `Bq17mn9fP6vyCn75Jw1xya` |
| orderReports[].transactTime | integer (int64) |  | 例: `1712289389158` |
| orderReports[].price | string |  | 例: `1.00000000` |
| orderReports[].origQty | string |  | 例: `1.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `LIMIT` |
| orderReports[].side | string |  | 例: `SELL` |
| orderReports[].workingTime | integer (int64) |  | 例: `1712289389158` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## New Order list - OTOCO (TRADE)（新订单列表 - OTOCO (TRADE)）

`POST /api/v3/orderList/otoco`

Place an OTOCO.

- An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
- The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  - The behavior of the working order is the same as the [OTO](#order-list-oto).
- OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**.
  - The rules of the pending above and pending below follow the same rules as the [Order list OCO](#order-list-oco).
- OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 OTOCO 订单。

- 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
- 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
  - 生效订单的行为与此一致 [OTO](#order-list-oto)
- 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交**时，待处理订单们才会被自动下单。
  - 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [OrderList OCO](#order-list-oco)。
- `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单**。

Operation ID: `orderListOtoco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.<br>整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。 `listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。<br>例: `RumwQpBaDctlUu5jyG5rs0` |
| newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| workingType | string | 是 | Supported values: `LIMIT`, `LIMIT_MAKER`<br>支持的数值： `LIMIT`， `LIMIT_MAKER`<br>枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>用于标识生效订单的唯一ID。 如果未发送则自动生成。<br>例: `workingOrder1` |
| workingPrice | number (float) | 是 | 例: `1` |
| workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>用于设置生效订单的数量。<br>例: `1` |
| workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.<br>仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。<br>例: `1` |
| workingTimeInForce | string |  | Supported values: [Time In Force](/products/spot/enums#timeinforce)<br>支持的数值： [生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| workingStrategyId | integer (int64) |  | Arbitrary numeric value identifying the working order within an order strategy.<br>订单策略中用于标识生效订单的 ID。<br>例: `1` |
| workingStrategyType | integer |  | Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| workingPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| workingPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| workingPegOffsetValue | integer |  | 例: `1` |
| pendingSide | string | 是 | Supported values: [Order Side](/products/spot/enums#side)<br>支持的数值： [订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingQuantity | number (float) | 是 | Sets the quantity for the pending orders.<br>用于设置待处理订单的数量。<br>例: `1` |
| pendingAboveType | string | 是 | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS_LIMIT` |
| pendingAboveClientOrderId | string |  | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>用于标识待处理上方订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingAboveOrder1` |
| pendingAbovePrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingAboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1` |
| pendingAboveStopPrice | number (float) |  | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。<br>例: `1` |
| pendingAboveTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| pendingAboveIcebergQty | number (float) |  | This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.<br>只有当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| pendingAboveTimeInForce | string |  | Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingAboveStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending above order within an order strategy.<br>订单策略中用于标识待处理上方订单的 ID。<br>例: `1` |
| pendingAboveStrategyType | integer |  | Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理上方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| pendingAbovePegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingAbovePegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingAbovePegOffsetValue | integer |  | 例: `1` |
| pendingBelowType | string |  | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>支持的数值： `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>枚举: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`<br>例: `STOP_LOSS` |
| pendingBelowClientOrderId | string |  | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>用于标识待处理下方订单的唯一ID。 如果未发送则自动生成。<br>例: `pendingBelowOrder1` |
| pendingBelowPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.<br>当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。<br>例: `1` |
| pendingBelowStopPrice | number (float) |  | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.<br>如果 `pendingBelowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。 必须指定 `pendingBelowStopPrice` 或 `pendingBelowTrailingDelta` 或两者。<br>例: `1` |
| pendingBelowTrailingDelta | number (float) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| pendingBelowIcebergQty | number (float) |  | This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.<br>只有当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时才能使用。<br>例: `1` |
| pendingBelowTimeInForce | string |  | Required if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.<br>如果 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingBelowStrategyId | integer (int64) |  | Arbitrary numeric value identifying the pending below order within an order strategy.<br>订单策略中用于标识待处理下方订单的 ID。<br>例: `1` |
| pendingBelowStrategyType | integer |  | Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000` are reserved and cannot be used.<br>用于标识待处理下方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。<br>例: `1` |
| pendingBelowPegPriceType | string |  | See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pendingBelowPegOffsetType | string |  | 枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| pendingBelowPegOffsetValue | integer |  | 例: `1` |
| workingQuoteNotionalLimit | number (float) |  | Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| pendingAboveQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending above order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| pendingBelowQuoteNotionalLimit | number (float) |  | Quote notional limit for the pending below order (only for orders on the BUY side). See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>待处理下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New Order list - OTOCO / New 订单 列表- OTOCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `1` |
| contingencyType | string |  | 例: `OTO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `RumwQpBaDctlUu5jyG5rs0` |
| transactionTime | integer (int64) |  | 例: `1712291372842` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `6` |
| orders[].clientOrderId | string |  | 例: `fM9Y4m23IFJVCQmIrlUmMK` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | 例: `6` |
| orderReports[].orderListId | integer (int64) |  | 例: `1` |
| orderReports[].clientOrderId | string |  | 例: `fM9Y4m23IFJVCQmIrlUmMK` |
| orderReports[].transactTime | integer (int64) |  | 例: `1712291372842` |
| orderReports[].price | string |  | 例: `1.00000000` |
| orderReports[].origQty | string |  | 例: `1.00000000` |
| orderReports[].executedQty | string |  | 例: `0.00000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.00000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `LIMIT` |
| orderReports[].side | string |  | 例: `SELL` |
| orderReports[].workingTime | integer (int64) |  | 例: `1712291372842` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].icebergQty | string |  | Appears only if the parameter icebergQty was sent in the request.<br>仅在请求中发送了 icebergQty 参数时出现。<br>例: `0.00000000` |
| orderReports[].preventedMatchId | integer (int64) |  | Appears only if the order expired due to STP.<br>仅在因 STP 导致订单失效时出现。<br>例: `0` |
| orderReports[].preventedQuantity | string |  | Order quantity that expired due to STP.<br>因 STP 导致订单失效的数量。<br>例: `1.200000` |
| orderReports[].stopPrice | string |  | Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.<br>出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。<br>例: `0.00000000` |
| orderReports[].strategyId | integer (int64) |  | Appears only if the strategyId parameter was provided upon order placement.<br>仅在下单时提供了 strategyId 参数时出现。<br>例: `1` |
| orderReports[].strategyType | integer (int64) |  | Appears only if the strategyType parameter was provided upon order placement.<br>仅在下单时提供了 strategyType 参数时出现。<br>例: `1000000` |
| orderReports[].trailingDelta | integer (int64) |  | Delta price change required before order activation.<br>订单激活前所需的价格变动。<br>例: `10` |
| orderReports[].trailingTime | integer (int64) |  | Time when the trailing order is now active and tracking price changes.<br>追踪单被激活和跟踪价格变化的时间。<br>例: `-1` |
| orderReports[].usedSor | boolean |  | Field that determines whether order used SOR.<br>用于确定订单是否使用SOR的字段。<br>例: `True` |
| orderReports[].workingFloor | string |  | Determines whether the order is being filled by the SOR or by the order book.<br>用以定义订单是通过 SOR 还是由订单簿成交的。<br>例: `SOR` |
| orderReports[].pegPriceType | string |  | Price peg type. Only for pegged orders.<br>挂钩价格类型。仅用于挂钩订单。<br>例: `PRIMARY_PEG` |
| orderReports[].pegOffsetType | string |  | Price peg offset type. Only for pegged orders, if requested.<br>挂钩价格偏移类型。如若需要，仅用于挂钩订单。<br>例: `PRICE_LEVEL` |
| orderReports[].pegOffsetValue | integer (int64) |  | Price peg offset value. Only for pegged orders, if requested.<br>挂钩价格偏移值。如若需要，仅用于挂钩订单。<br>例: `5` |
| orderReports[].peggedPrice | string |  | Current price order is pegged at. Only for pegged orders, once determined.<br>订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。<br>例: `87523.83710000` |
| orderReports[].expiryReason | string |  | Cause of the order's expiration. Appears when an order has expired.<br>订单过期的原因。当订单过期时出现。<br>例: `INSUFFICIENT_LIQUIDITY` |

## New OCO - Deprecated (TRADE)（发送新 OCO 订单 - 已弃用 (TRADE)）

`POST /api/v3/order/oco`

Send in a new OCO.

- Price Restrictions:
  - `SELL`: Limit Price > Last Price > Stop Price
  - `BUY`: Limit Price < Last Price < Stop Price
- Quantity Restrictions:
  - Both legs must have the same quantity.
  - `ICEBERG` quantities however do not have to be the same
- `OCO` adds **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

发送新的 OCO。

- 价格限制：
  - `SELL`： Limit price > 最后交易价格 > stop Price
  - `BUY`： Limit price < 最后交易价格 < stop Price
- 数量限制：
  - 两条腿的数量必须相同。
  - 不过， `冰山` 交易的数量不一定相同
- `OCO` 将**2个订单**添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

Operation ID: `orderOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| listClientOrderId | string |  | A unique Id for the entire orderList<br>整个orderList的唯一ID<br>例: `JYVpp3F0f5CAG15DhtrqLp` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | 例: `1` |
| limitClientOrderId | string |  | A unique Id for the limit order<br>限价单的唯一ID<br>例: `limitOrder1` |
| price | number (float) | 是 | 例: `1` |
| limitStrategyId | integer (int64) |  | 例: `1` |
| limitStrategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`<br>例: `1` |
| limitIcebergQty | number (float) |  | Used to make the `LIMIT_MAKER` leg an iceberg order.<br>用于使 `LIMIT_MAKER` 腿单成为冰山订单。<br>例: `1` |
| trailingDelta | integer (int64) |  | 例: `1` |
| stopClientOrderId | string |  | A unique Id for the stop loss/stop loss limit leg<br>止损/止损限价单的唯一ID<br>例: `stopOrder1` |
| stopPrice | number (float) | 是 | 例: `1` |
| stopStrategyId | integer (int64) |  | 例: `1` |
| stopStrategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`<br>例: `1` |
| stopLimitPrice | number (float) |  | If provided, `stopLimitTimeInForce` is required.<br>如果提供，须配合提交`stopLimitTimeInForce`<br>例: `1` |
| stopIcebergQty | number (float) |  | Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.<br>与 `STOP_LOSS_LIMIT` 腿单一起使用，使其成为冰山订单。<br>例: `1` |
| stopLimitTimeInForce | string |  | Valid values are `GTC`/`FOK`/`IOC`<br>有效值 `GTC`/`FOK`/`IOC`<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| newOrderRespType | string |  | Format of the JSON response. Supported values: [Order Response Type](/products/spot/enums#orderresponsetype)<br>JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New OCO - Deprecated / 发送新 OCO 订单 - 已弃用

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | 例: `0` |
| contingencyType | string |  | 例: `OCO` |
| listStatusType | string |  | 例: `EXEC_STARTED` |
| listOrderStatus | string |  | 例: `EXECUTING` |
| listClientOrderId | string |  | 例: `JYVpp3F0f5CAG15DhtrqLp` |
| transactionTime | integer (int64) |  | 例: `1563417480525` |
| symbol | string |  | 例: `LTCBTC` |
| orders | object[] |  |  |
| orders[].symbol | string |  | 例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | 例: `2` |
| orders[].clientOrderId | string |  | 例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | 例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | 例: `2` |
| orderReports[].orderListId | integer (int64) |  | 例: `0` |
| orderReports[].clientOrderId | string |  | 例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports[].transactTime | integer (int64) |  | 例: `1563417480525` |
| orderReports[].price | string |  | 例: `0.000000` |
| orderReports[].origQty | string |  | 例: `0.624363` |
| orderReports[].executedQty | string |  | 例: `0.000000` |
| orderReports[].origQuoteOrderQty | string |  | 例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | 例: `0.000000` |
| orderReports[].status | string |  | 例: `NEW` |
| orderReports[].timeInForce | string |  | 例: `GTC` |
| orderReports[].type | string |  | 例: `STOP_LOSS` |
| orderReports[].side | string |  | 例: `BUY` |
| orderReports[].workingTime | integer (int64) |  | 例: `-1` |
| orderReports[].selfTradePreventionMode | string |  | 例: `NONE` |
| orderReports[].stopPrice | string |  | 例: `0.960664` |

## Test new order (TRADE)（测试下单接口 (TRADE)）

`POST /api/v3/order/test`

Test new order creation and signature/recvWindow long.

Creates and validates a new order but does not send it into the matching
engine.

用于测试订单请求，但不会提交到撮合引擎

权重: |Condition|Weight|
|---|---|
|Without `computeCommissionRates`|1|
|With `computeCommissionRates`|20|

Operation ID: `orderTest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| computeCommissionRates | boolean |  | Default: `false` <br> See [Commissions FAQ](/products/spot/faqs/commission_faq#test-order-diferences) to learn more.<br>默认值: `false` <br> 请参阅[佣金常见问题解答](/products/spot/faqs/commission_faq#test-order-diferences) 了解更多信息。<br>例: `False` |
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `MARKET` |
| timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| quantity | number (float) |  | 例: `1` |
| quoteOrderQty | number (float) |  | 例: `1` |
| price | number (float) |  | 例: `400` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。<br>例: `myOrder1` |
| strategyId | integer (int64) |  | 例: `1` |
| strategyType | integer |  | The value cannot be less than `1000000`.<br>不能低于 `1000000`。<br>例: `1` |
| stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。<br>例: `1` |
| trailingDelta | integer (int64) |  | See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)<br>参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)<br>例: `1` |
| icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.<br>指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| pegPriceType | string |  | `PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRIMARY_PEG`, `MARKET_PEG`<br>例: `PRIMARY_PEG` |
| pegOffsetValue | integer |  | Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>例: `1` |
| pegOffsetType | string |  | Only `PRICE_LEVEL` is supported. See [Pegged Orders](/products/spot/faqs/pegged_orders)<br>仅支持 `PRICE_LEVEL`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)<br>枚举: `PRICE_LEVEL`<br>例: `PRICE_LEVEL` |
| quoteNotionalLimit | number (float) |  | For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).<br>仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。<br>例: `100` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Test new order / 测试下单接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 2).standardCommissionForOrder | object |  | Standard commission rates on trades from the order.<br>订单交易的标准佣金率 |
| (oneOf 2).standardCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).standardCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).specialCommissionForOrder | object |  | Special commission rates on trades from the order.<br>订单交易的特殊佣金率 |
| (oneOf 2).specialCommissionForOrder.maker | string |  | 例: `0.05000000` |
| (oneOf 2).specialCommissionForOrder.taker | string |  | 例: `0.06000000` |
| (oneOf 2).taxCommissionForOrder | object |  | Tax commission rates for trades from the order.<br>订单交易的税率 |
| (oneOf 2).taxCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).taxCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).discount | object |  | Discount on standard commissions when paying in BNB.<br>以BNB支付时的标准佣金折扣。 |
| (oneOf 2).discount.enabledForAccount | boolean |  | 例: `True` |
| (oneOf 2).discount.enabledForSymbol | boolean |  | 例: `True` |
| (oneOf 2).discount.discountAsset | string |  | 例: `BNB` |
| (oneOf 2).discount.discount | string |  | 例: `0.25000000` |

## New order using SOR (TRADE)（下 SOR 订单 (TRADE)）

`POST /api/v3/sor/order`

Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](/products/spot/faqs/sor_faq) to learn more.

发送使用智能订单路由 (SOR) 的新订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

参阅 [智能订单路由 (SOR)](/products/spot/faqs/sor_faq) 了解更多详情。

Operation ID: `sorOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | 枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| quantity | number (float) | 是 | 例: `1` |
| price | number (float) |  | 例: `400` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，<br/>那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。<br>例: `myOrder1` |
| strategyId | integer (int64) |  | 例: `1` |
| strategyType | integer |  | The value cannot be less than `1000000`.<br>赋值不能小于 `1000000`.<br>例: `1` |
| icebergQty | number (float) |  | Used with `LIMIT` to create an iceberg order.<br>仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`<br>指定响应类型:<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/products/spot/enums#stpmodes).<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：New order using SOR / 下 SOR 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `BTCUSDT` |
| orderId | integer (int64) |  | 例: `2` |
| orderListId | integer (int64) |  | 例: `-1` |
| clientOrderId | string |  | 例: `sBI1KM6nNtOfj5tccZSKly` |
| transactTime | integer (int64) |  | 例: `1689149087774` |
| price | string |  | 例: `31000.00000000` |
| origQty | string |  | 例: `0.50000000` |
| executedQty | string |  | 例: `0.50000000` |
| origQuoteOrderQty | string |  | 例: `0.000000` |
| cummulativeQuoteQty | string |  | 例: `14000.00000000` |
| status | string |  | 例: `FILLED` |
| timeInForce | string |  | 例: `GTC` |
| type | string |  | 例: `LIMIT` |
| side | string |  | 例: `BUY` |
| workingTime | integer (int64) |  | 例: `1689149087774` |
| fills | object[] |  |  |
| fills[].matchType | string |  | 例: `ONE_PARTY_TRADE_REPORT` |
| fills[].price | string |  | 例: `28000.00000000` |
| fills[].qty | string |  | 例: `0.50000000` |
| fills[].commission | string |  | 例: `0.00000000` |
| fills[].commissionAsset | string |  | 例: `BTC` |
| fills[].tradeId | integer (int64) |  | 例: `-1` |
| fills[].allocId | integer (int64) |  | 例: `0` |
| workingFloor | string |  | 例: `SOR` |
| selfTradePreventionMode | string |  | 例: `NONE` |
| usedSor | boolean |  | 例: `True` |

## Test new order using SOR (TRADE)（测试 SOR 下单接口 (TRADE)）

`POST /api/v3/sor/order/test`

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎

权重: |Condition|Weight|
|---|---|
|Without `computeCommissionRates`|1|
|With `computeCommissionRates`|20|

Operation ID: `sorOrderTest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| computeCommissionRates | boolean |  | 默认: `False`<br>例: `False` |
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | Please see [Enums](/products/spot/enums#side) for supported values.<br>详见枚举定义：[订单方向](/products/spot/enums#side)<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | Please see [Enums](/products/spot/enums#ordertypes) for supported values.<br>详见枚举定义：[订单类型](/products/spot/enums#ordertypes)<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| timeInForce | string |  | Please see [Enums](/products/spot/enums#timeinforce) for supported values.<br>详见枚举定义：[生效时间](/products/spot/enums#timeinforce)<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| quantity | number (float) | 是 | 例: `1` |
| price | number (float) |  | 例: `400` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.<br>用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。<br>例: `myOrder1` |
| strategyId | integer (int64) |  | 例: `1` |
| strategyType | integer |  | The value cannot be less than `1000000`.<br>赋值不能小于 `1000000`。<br>例: `1` |
| icebergQty | number (float) |  | Used with `LIMIT` to create an iceberg order.<br>仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。<br>例: `1` |
| newOrderRespType | string |  | Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`.<br>指定响应类型: `ACK`, `RESULT` 或 `FULL`; 默认为 `FULL`。<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/products/spot/enums#stpmodes)<br>允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`, `TRANSFER`<br>例: `NONE` |
| recvWindow | number (float) |  | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.<br>最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。<br>例: `1770736694138` |

### 响应 200：Test new order using SOR / 测试 SOR 下单接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 2).standardCommissionForOrder | object |  | Standard commission rates on trades from the order.<br>订单交易的标准佣金率。 |
| (oneOf 2).standardCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).standardCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).taxCommissionForOrder | object |  | Tax commission rates for trades from the order.<br>订单交易的税率。 |
| (oneOf 2).taxCommissionForOrder.maker | string |  | 例: `0.00000112` |
| (oneOf 2).taxCommissionForOrder.taker | string |  | 例: `0.00000114` |
| (oneOf 2).discount | object |  | Discount on standard commissions when paying in BNB.<br>以BNB支付时的标准佣金折扣。 |
| (oneOf 2).discount.enabledForAccount | boolean |  | 例: `True` |
| (oneOf 2).discount.enabledForSymbol | boolean |  | 例: `True` |
| (oneOf 2).discount.discountAsset | string |  | 例: `BNB` |
| (oneOf 2).discount.discount | string |  | 例: `0.25000000` |