---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api
api_type: REST
updated_at: 2026-11-28 18:47:00.574931
---

# Futures (COIN-M) REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.

访问市场数据、管理账户，并交易 COIN-M 永续和交割合约。

版本: 1.0.0

## 服务地址

- `https://dapi.binance.com`
- `https://testnet.binancefuture.com`

## 接口列表

- `GET /dapi/v1/account` — Account Information (USER_DATA)
- `GET /dapi/v1/balance` — Futures Account Balance (USER_DATA)
- `GET /dapi/v1/positionSide/dual` — Get Current Position Mode (USER_DATA)
- `POST /dapi/v1/positionSide/dual` — Change Position Mode (TRADE)
- `GET /dapi/v1/order/asyn` — Get Download Id For Futures Order History (USER_DATA)
- `GET /dapi/v1/trade/asyn` — Get Download Id For Futures Trade History (USER_DATA)
- `GET /dapi/v1/income/asyn` — Get Download Id For Futures Transaction History (USER_DATA)
- `GET /dapi/v1/order/asyn/id` — Get Futures Order History Download Link by Id (USER_DATA)
- `GET /dapi/v1/trade/asyn/id` — Get Futures Trade Download Link by Id (USER_DATA)
- `GET /dapi/v1/income/asyn/id` — Get Futures Transaction History Download Link by Id (USER_DATA)
- `GET /dapi/v1/income` — Get Income History (USER_DATA)
- `GET /dapi/v1/leverageBracket` — Notional Bracket for Pair (USER_DATA)
- `GET /dapi/v2/leverageBracket` — Notional Bracket for Symbol (USER_DATA)
- `GET /dapi/v1/commissionRate` — User Commission Rate (USER_DATA)
- `GET /futures/data/basis` — Basis
- `GET /dapi/v1/time` — Check Server time
- `GET /dapi/v1/aggTrades` — Compressed/Aggregate Trades List
- `GET /dapi/v1/continuousKlines` — Continuous Contract Kline/Candlestick Data
- `GET /dapi/v1/exchangeInfo` — Exchange Information
- `GET /dapi/v1/fundingRate` — Get Funding Rate History of Perpetual Futures
- `GET /dapi/v1/fundingInfo` — Get Funding Rate Info
- `GET /dapi/v1/premiumIndex` — Index Price and Mark Price
- `GET /dapi/v1/indexPriceKlines` — Index Price Kline/Candlestick Data
- `GET /dapi/v1/klines` — Kline/Candlestick Data
- `GET /futures/data/globalLongShortAccountRatio` — Long/Short Ratio
- `GET /dapi/v1/markPriceKlines` — Mark Price Kline/Candlestick Data
- `GET /dapi/v1/historicalTrades` — Old Trades Lookup (MARKET_DATA)
- `GET /dapi/v1/openInterest` — Open Interest
- `GET /futures/data/openInterestHist` — Open Interest Statistics
- `GET /dapi/v1/depth` — Order Book
- `GET /dapi/v1/premiumIndexKlines` — Premium index Kline Data
- `GET /dapi/v1/constituents` — Query Index Price Constituents
- `GET /dapi/v1/trades` — Recent Trades List
- `GET /dapi/v1/ticker/bookTicker` — Symbol Order Book Ticker
- `GET /dapi/v1/ticker/price` — Symbol Price Ticker
- `GET /futures/data/takerBuySellVol` — Taker Buy/Sell Volume
- `GET /dapi/v1/ping` — Test Connectivity
- `GET /dapi/v1/ticker/24hr` — 24hr Ticker Price Change Statistics
- `GET /futures/data/topLongShortAccountRatio` — Top Trader Long/Short Account Ratio
- `GET /futures/data/topLongShortPositionRatio` — Top Trader Long/Short Position Ratio
- `GET /dapi/v1/userTrades` — Account Trade List (USER_DATA)
- `GET /dapi/v1/allOrders` — All Orders (USER_DATA)
- `POST /dapi/v1/countdownCancelAll` — Auto-Cancel All Open Orders (TRADE)
- `GET /dapi/v1/algoOrder` — Query Algo Order (USER_DATA)
- `POST /dapi/v1/algoOrder` — New Algo Order (TRADE)
- `DELETE /dapi/v1/algoOrder` — Cancel Algo Order (TRADE)
- `DELETE /dapi/v1/algoOpenOrders` — Cancel All Algo Open Orders (TRADE)
- `DELETE /dapi/v1/allOpenOrders` — Cancel All Open Orders (TRADE)
- `POST /dapi/v1/batchOrders` — Place Multiple Orders (TRADE)
- `PUT /dapi/v1/batchOrders` — Modify Multiple Orders (TRADE)
- `DELETE /dapi/v1/batchOrders` — Cancel Multiple Orders (TRADE)
- `GET /dapi/v1/order` — Query Order (USER_DATA)
- `POST /dapi/v1/order` — New Order (TRADE)
- `PUT /dapi/v1/order` — Modify Order (TRADE)
- `DELETE /dapi/v1/order` — Cancel Order (TRADE)
- `POST /dapi/v1/leverage` — Change Initial Leverage (TRADE)
- `POST /dapi/v1/marginType` — Change Margin Type (TRADE)
- `GET /dapi/v1/openAlgoOrders` — Current All Algo Open Orders (USER_DATA)
- `GET /dapi/v1/openOrders` — Current All Open Orders (USER_DATA)
- `GET /dapi/v1/orderAmendment` — Get Order Modify History (USER_DATA)
- `GET /dapi/v1/positionMargin/history` — Get Position Margin Change History (TRADE)
- `POST /dapi/v1/positionMargin` — Modify Isolated Position Margin (TRADE)
- `GET /dapi/v1/adlQuantile` — Position ADL Quantile Estimation (USER_DATA)
- `GET /dapi/v1/positionRisk` — Position Information (USER_DATA)
- `GET /dapi/v1/allAlgoOrders` — Query All Algo Orders (USER_DATA)
- `GET /dapi/v1/openOrder` — Query Current Open Order (USER_DATA)
- `GET /dapi/v1/forceOrders` — User's Force Orders (USER_DATA)
- `POST /dapi/v1/listenKey` — Start User Data Stream (USER_STREAM)
- `PUT /dapi/v1/listenKey` — Keepalive User Data Stream (USER_STREAM)
- `DELETE /dapi/v1/listenKey` — Close User Data Stream (USER_STREAM)

## Account Information (USER_DATA)（账户信息 (USER_DATA)）

`GET /dapi/v1/account`

Get current account information.

查询账户信息

Operation ID: `accountInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Information / 账户 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] |  | Supported assets.<br>支持的资产列表。 |
| assets[].asset | string |  | asset name<br>资产<br>例: `BTC` |
| assets[].walletBalance | string |  | total wallet balance<br>账户余额<br>例: `0.00241969` |
| assets[].unrealizedProfit | string |  | unrealized profit or loss<br>全部持仓未实现盈亏<br>例: `0.00000000` |
| assets[].marginBalance | string |  | margin balance<br>保证金余额<br>例: `0.00241969` |
| assets[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0.00000000` |
| assets[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>当前所需持仓起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前所需挂单起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| assets[].maxWithdrawAmount | string |  | maximum amount for transfer out<br>最大可转出余额<br>例: `0.00241969` |
| assets[].crossWalletBalance | string |  | wallet balance for crossed margin<br>可用于全仓的账户余额<br>例: `0.00241969` |
| assets[].crossUnPnl | string |  | total unrealized profit or loss of crossed positions<br>所有全仓持仓的未实现盈亏<br>例: `0.00000000` |
| assets[].availableBalance | string |  | available margin balance<br>可用下单余额<br>例: `0.00241969` |
| assets[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1625474304765` |
| positions | object[] |  | Position list.<br>持仓列表. |
| positions[].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_201225` |
| positions[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| positions[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金(按最新标标记价格)<br>例: `0` |
| positions[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0` |
| positions[].unrealizedProfit | string |  | unrealized profit or loss<br>全部持仓未实现盈亏<br>例: `0.00000000` |
| positions[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>当前所需持仓起始保证金(按最新标标记价格)<br>例: `0` |
| positions[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前所需挂单起始保证金(按最新标标记价格)<br>例: `0` |
| positions[].leverage | string |  | Leverage value.<br>杠杆倍数.<br>例: `125` |
| positions[].isolated | boolean |  | Whether isolated margin mode is enabled.<br>是否为逐仓模式.<br>例: `False` |
| positions[].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| positions[].entryPrice | string |  | Position entry price.<br>持仓开仓价格.<br>例: `0.0` |
| positions[].breakEvenPrice | string |  | break-even price<br>盈亏平衡价<br>例: `0.0` |
| positions[].maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `50` |
| positions[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |
| positions[].notionalValue | string |  | Notional value.<br>名义价值.<br>例: `0` |
| canDeposit | boolean |  | Whether deposits are enabled.<br>是否可充值.<br>例: `True` |
| canTrade | boolean |  | Whether trading is enabled.<br>是否可交易.<br>例: `True` |
| canWithdraw | boolean |  | Whether withdrawals are enabled.<br>是否可提现.<br>例: `True` |
| feeTier | integer (int64) |  | Fee tier level.<br>手续费等级.<br>例: `2` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |

## Futures Account Balance (USER_DATA)（账户余额 (USER_DATA)）

`GET /dapi/v1/balance`

Check futures account balance

查询账户余额

Operation ID: `futuresAccountBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Account Balance / 合约 账户 Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].accountAlias | string |  | unique account code<br>账户唯一识别码<br>例: `SgsR` |
| [].asset | string |  | asset name<br>资产<br>例: `BTC` |
| [].balance | string |  | Account balance.<br>账户余额.<br>例: `0.00250000` |
| [].withdrawAvailable | string |  | Available amount for withdrawal.<br>可提现金额.<br>例: `0.00250000` |
| [].crossWalletBalance | string |  | wallet balance for crossed margin<br>可用于全仓的账户余额<br>例: `0.00241969` |
| [].crossUnPnl | string |  | total unrealized profit or loss of crossed positions<br>所有全仓持仓的未实现盈亏<br>例: `0.00000000` |
| [].availableBalance | string |  | available margin balance<br>可用下单余额<br>例: `0.00241969` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1592468353979` |

## Get Current Position Mode (USER_DATA)（查询持仓模式 (USER_DATA)）

`GET /dapi/v1/positionSide/dual`

Get user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***

查询用户目前在 ***所有symbol*** 合约上的持仓模式：双向持仓或单向持仓。

Operation ID: `getCurrentPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Current Position Mode / 获取当前 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | boolean |  | Whether dual-side position mode is enabled.<br>是否开启双向持仓模式.<br>例: `True` |

## Change Position Mode (TRADE)（更改持仓模式 (TRADE)）

`POST /dapi/v1/positionSide/dual`

Change user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***.

**After CM migration**, UM and CM share the **same** `dualSidePosition` setting. Calling this endpoint flips both UM and CM at once. If either side has any open order or open position, the change is rejected:
- `-4067` (open orders exist)
- `-4068` (open position exists)

变换用户在 ***所有symbol*** 合约上的持仓模式：双向持仓或单向持仓。

**迁移后**,UM 与 CM 共用**同一个** `dualSidePosition` 设置。调用此接口会同时翻转 UM 与 CM。任意一侧存在挂单或持仓时,切换会被拒绝:
- `-4067`(存在挂单)
- `-4068`(存在持仓)

Operation ID: `changePositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | string | 是 | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Position Mode / 修改持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `200` |
| msg | string |  | Message details.<br>消息详情.<br>例: `success` |

## Get Download Id For Futures Order History (USER_DATA)（获取合约订单历史下载Id (USER_DATA)）

`GET /dapi/v1/order/asyn`

Get Download Id For Futures Order History

获取合约订单历史下载Id

Operation ID: `getDownloadIdForFuturesOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>起始时间，ms格式时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>结束时间，ms格式时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Order History / 获取Download ID 用于 合约 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `546975389218332672` |

## Get Download Id For Futures Trade History (USER_DATA)（获取合约交易历史下载Id (USER_DATA)）

`GET /dapi/v1/trade/asyn`

Get download id for futures trade history

获取合约交易历史下载Id

Operation ID: `getDownloadIdForFuturesTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>起始时间，ms格式时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>结束时间，ms格式时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Trade History / 获取Download ID 用于 合约 交易 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `546975389218332672` |

## Get Download Id For Futures Transaction History (USER_DATA)（获取合约资金流水下载Id (USER_DATA)）

`GET /dapi/v1/income/asyn`

Get download id for futures transaction history

获取合约资金流水下载Id

Operation ID: `getDownloadIdForFuturesTransactionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>起始时间，ms格式时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>结束时间，ms格式时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Transaction History / 获取Download ID 用于 合约 Transaction 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `546975389218332672` |

## Get Futures Order History Download Link by Id (USER_DATA)（通过下载Id获取合约订单下载链接 (USER_DATA)）

`GET /dapi/v1/order/asyn/id`

Get futures order history download link by Id

通过下载Id获取合约订单下载链接

Operation ID: `getFuturesOrderHistoryDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Order History Download Link by Id / 获取合约 订单 历史 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>订单状态<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Whether the record is expired.<br>记录是否已过期.<br>例: `null` |

## Get Futures Trade Download Link by Id (USER_DATA)（通过下载Id获取合约交易历史下载链接 (USER_DATA)）

`GET /dapi/v1/trade/asyn/id`

Get futures trade download link by Id

通过下载Id获取合约交易历史下载链接

Operation ID: `getFuturesTradeDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Trade Download Link by Id / 获取合约 交易 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>订单状态<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Whether the record is expired.<br>记录是否已过期.<br>例: `null` |

## Get Futures Transaction History Download Link by Id (USER_DATA)（通过下载Id获取合约资金流水下载链接 (USER_DATA)）

`GET /dapi/v1/income/asyn/id`

Get futures transaction history download link by Id

过下载Id获取合约资金流水下载链接

Operation ID: `getFuturesTransactionHistoryDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Transaction History Download Link by Id / 获取合约 Transaction 历史 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download task ID.<br>下载任务 ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>订单状态<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Whether the record is expired.<br>记录是否已过期.<br>例: `null` |

## Get Income History (USER_DATA)（获取账户损益资金流水 (USER_DATA)）

`GET /dapi/v1/income`

Get income history

获取账户损益资金流水

Operation ID: `getIncomeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| incomeType | query | string |  | Income type.<br>收益类型.<br>枚举: `TRANSFER`, `WELCOME_BONUS`, `FUNDING_FEE`, `REALIZED_PNL`, `COMMISSION`, `INSURANCE_CLEAR`, `DELIVERED_SETTELMENT`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `100`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Income History / 获取Income 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `` |
| [].incomeType | string |  | income type<br>资金流类型<br>例: `TRANSFER` |
| [].income | string |  | income amount<br>资金流数量,正数代表流入,负数代表流出<br>例: `-0.37500000` |
| [].asset | string |  | asset name<br>资产<br>例: `BTC` |
| [].info | string |  | extra information<br>备注信息,取决于流水类型<br>例: `WITHDRAW` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1570608000000` |
| [].tranId | string |  | transaction id<br>划转ID<br>例: `9689322392` |
| [].tradeId | string |  | Trade ID.<br>成交 ID.<br>例: `` |

## Notional Bracket for Pair (USER_DATA)（标的交易对默认杠杆分层标准 (USER_DATA)）

`GET /dapi/v1/leverageBracket`

**Not recommended to continue using this v1 endpoint**

Get the pair's default notional bracket list, may return ambiguous
values when there have been multiple different `symbol` brackets under
the `pair`, suggest using the following `GET /dapi/v2/leverageBracket`
query instead to get the specific `symbol` notional bracket list.

**不建议继续使用该 v1 接口**

获取标的交易对默认的杠杆分层标准，当 `pair` 下曾有过多个不同 `symbol` 杠杆分层标准时可能返回歧义值，建议使用下面的 `GET
/dapi/v2/leverageBracket` 代替查询以获取具体 `symbol` 杠杆分层标准

Operation ID: `notionalBracketForPair`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| pair | query | string |  | 例: `BTCUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Notional Bracket for Pair / Notional Bracket 用于 Pair

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].brackets | object[] |  | Leverage bracket details.<br>杠杆分层详情. |
| [].brackets[].bracket | integer (int64) |  | bracket level<br>层级<br>例: `1` |
| [].brackets[].initialLeverage | integer (int64) |  | the maximum leverage<br>该层允许的最高初始杠杆倍数<br>例: `125` |
| [].brackets[].qtyCap | integer (int64) |  | upper edge of base asset quantity<br>该层对应的数量上限<br>例: `50` |
| [].brackets[].qtylFloor | integer (int64) |  | lower edge of base asset quantity<br>该层对应的数量下限<br>例: `0` |
| [].brackets[].maintMarginRatio | number (float) |  | Maintenance margin ratio.<br>维持保证金率.<br>例: `0.004` |
| [].brackets[].cum | number (float) |  | Cumulative value.<br>累计值.<br>例: `0` |

## Notional Bracket for Symbol (USER_DATA)（交易对杠杆分层标准 (USER_DATA)）

`GET /dapi/v2/leverageBracket`

Get the symbol's notional bracket list.

获取交易对的杠杆分层标准

权重: 1 (after CM migration: 1 with `symbol` / 2 without `symbol`)

Operation ID: `notionalBracketForSymbol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_PERP` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Notional Bracket for Symbol / Notional Bracket 用于 交易对

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].notionalCoef | number (float) |  | user symbol bracket multiplier, only appears when user's symbol bracket is adjusted<br>用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示<br>例: `1.5` |
| [].brackets | object[] |  | Leverage bracket details.<br>杠杆分层详情. |
| [].brackets[].bracket | integer (int64) |  | bracket level<br>层级<br>例: `1` |
| [].brackets[].initialLeverage | integer (int64) |  | the maximum leverage<br>该层允许的最高初始杠杆倍数<br>例: `125` |
| [].brackets[].qtyCap | integer (int64) |  | upper edge of base asset quantity<br>该层对应的数量上限<br>例: `50` |
| [].brackets[].qtylFloor | integer (int64) |  | lower edge of base asset quantity<br>该层对应的数量下限<br>例: `0` |
| [].brackets[].maintMarginRatio | number (float) |  | Maintenance margin ratio.<br>维持保证金率.<br>例: `0.004` |
| [].brackets[].cum | number (float) |  | Cumulative value.<br>累计值.<br>例: `0` |

## User Commission Rate (USER_DATA)（用户手续费率 (USER_DATA)）

`GET /dapi/v1/commissionRate`

Query user commission rate

查询用户手续费率

Operation ID: `userCommissionRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Commission Rate / 用户 手续费 利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| makerCommissionRate | string |  | 0.015%<br>例: `0.00015` |
| takerCommissionRate | string |  | Taker commission rate.<br>吃单手续费率.<br>例: `0.00040` |

## Basis（基差）

`GET /futures/data/basis`

Query basis

查询基差

Operation ID: `basis`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | Pair.<br>标的交易对。<br>例: `None` |
| contractType | query | string | 是 | Contract type.<br>合约类型。<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| period | query | string | 是 | Period interval.<br>周期区间。<br>枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Basis / 请参见英文说明：Basis

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].indexPrice | string |  | index price<br>指数价格<br>例: `29269.93972727` |
| [].contractType | string |  | Contract type.<br>合约类型.<br>例: `CURRENT_QUARTER` |
| [].basisRate | string |  | Basis rate.<br>基差率.<br>例: `0.0024` |
| [].futuresPrice | string |  | Futures price.<br>期货价格.<br>例: `29341.3` |
| [].annualizedBasisRate | string |  | Annualized basis rate.<br>年化基差率.<br>例: `0.0283` |
| [].basis | string |  | Basis value.<br>基差值.<br>例: `71.36027273` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].timestamp | integer (int64) |  | Start time of the period, in milliseconds.<br>该周期的开始时间，单位为毫秒。<br>例: `1653381600000` |

## Check Server time（获取服务器时间）

`GET /dapi/v1/time`

Test connectivity to the Rest API and get the current server time.

获取服务器时间

Operation ID: `checkServerTime`

### 响应 200：Check Server time / 检查Server 时间

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serverTime | integer (int64) |  | Ignore please. If you want to check current server time, please check via "GET /dapi/v1/time"<br>请忽略。如果需要获取系统时间，请查询接口 “GET /dapi/v1/time”<br>例: `1499827319559` |

## Compressed/Aggregate Trades List（近期成交）

`GET /dapi/v1/aggTrades`

Get compressed, aggregate trades. Market trades that fill in 100ms with
the same price and the same taking side will have the quantity
aggregated.

归集交易与逐笔交易的区别在于，同一价格、同一方向、同一时间(100ms 计算)的订单簿trade 会被聚合为一条

Operation ID: `compressedAggregateTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `None` |
| fromId | query | integer (int64) |  | ID to get aggregate trades from INCLUSIVE.<br>从包含 fromID 的成交开始返回结果<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades from INCLUSIVE.<br>从该时刻之后的成交记录开始返回结果<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades until INCLUSIVE.<br>返回该时刻为止的成交记录<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Compressed/Aggregate Trades List / Compressed/Aggregate 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].a | integer (int64) |  | Aggregate tradeId<br>归集成交 ID<br>例: `416690` |
| [].p | string |  | Price<br>价格<br>例: `9642.4` |
| [].q | string |  | Quantity<br>数量<br>例: `3` |
| [].f | integer (int64) |  | First tradeId<br>首个成交 ID<br>例: `595259` |
| [].l | integer (int64) |  | Last tradeId<br>最后成交 ID<br>例: `595259` |
| [].T | integer (int64) |  | Timestamp<br>时间戳<br>例: `1591250548649` |
| [].m | boolean |  | Was the buyer the maker?<br>买方是否为挂单方<br>例: `False` |

## Continuous Contract Kline/Candlestick Data（连续合约K线数据）

`GET /dapi/v1/continuousKlines`

Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.

每根K线的开盘时间可视为唯一ID

权重: based on parameter `LIMIT`

| LIMIT | weight |
| --- | --- |
| [1,100) | 1 |
| [100, 500) | 2 |
| [500, 1000] | 5 |
| > 1000 | 10 |

Operation ID: `continuousContractKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | After CM migration, accepts both CM and UM pair values.<br>标的交易对。迁移后支持传入 CM 与 UM 的 pair。<br>例: `BTCUSD` |
| contractType | query | string | 是 | 枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| interval | query | string | 是 | Interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Continuous Contract Kline/Candlestick Data / Continuous Contract K线/Candlestick Data

## Exchange Information（获取交易规则和交易对）

`GET /dapi/v1/exchangeInfo`

Current exchange trading rules and symbol information

获取交易规则和交易对

Operation ID: `exchangeInformation`

### 响应 200：Exchange Information / Exchange 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| exchangeFilters | string[] |  | Exchange filters.<br>交易所过滤器. |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| serverTime | integer (int64) |  | Ignore please. If you want to check current server time, please check via "GET /dapi/v1/time"<br>请忽略。如果需要获取系统时间，请查询接口 “GET /dapi/v1/time”<br>例: `1565613908500` |
| symbols | object[] |  | Supported trading symbols.<br>支持的交易对列表。 |
| symbols[].filters | object[] |  | Trading filters and constraints.<br>交易过滤器与限制。 |
| symbols[].filters[].filterType | string |  | Filter type.<br>过滤器类型。<br>例: `PRICE_FILTER` |
| symbols[].filters[].maxPrice | string |  | Maximum price.<br>最大价格。<br>例: `100000` |
| symbols[].filters[].minPrice | string |  | Minimum price.<br>最小价格。<br>例: `0.1` |
| symbols[].filters[].tickSize | string |  | Tick size.<br>价格步长。<br>例: `0.1` |
| symbols[].filters[].maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `100000` |
| symbols[].filters[].minQty | string |  | Minimum quantity.<br>最小数量。<br>例: `1` |
| symbols[].filters[].stepSize | string |  | Step size.<br>数量步长。<br>例: `1` |
| symbols[].filters[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `200` |
| symbols[].filters[].multiplierUp | string |  | Upper multiplier bound.<br>上限倍率。<br>例: `1.0500` |
| symbols[].filters[].multiplierDown | string |  | Lower multiplier bound.<br>下限倍率。<br>例: `0.9500` |
| symbols[].filters[].multiplierDecimal | string |  | Multiplier decimal precision.<br>乘数小数精度.<br>例: `4` |
| symbols[].orderTypes | string[] |  | Supported order types.<br>支持的订单类型. |
| symbols[].timeInForce | string[] |  | Time in force<br>有效方式 |
| symbols[].liquidationFee | string |  | liquidation fee rate<br>强平费率<br>例: `0.010000` |
| symbols[].marketTakeBound | string |  | the max price difference rate( from mark price) a market order can make<br>市价吃单(相对于标记价格)允许可造成的最大价格偏离比例<br>例: `0.30` |
| symbols[].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| symbols[].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| symbols[].contractType | string |  | Contract type.<br>合约类型.<br>例: `CURRENT_QUARTER` |
| symbols[].deliveryDate | integer (int64) |  | Delivery timestamp.<br>交割时间戳.<br>例: `1601020800000` |
| symbols[].onboardDate | integer (int64) |  | Onboard timestamp.<br>上线时间戳.<br>例: `1590739200000` |
| symbols[].contractStatus | string |  | Contract status.<br>合约状态.<br>例: `TRADING` |
| symbols[].contractSize | integer (int64) |  | Contract size.<br>合约面值.<br>例: `100` |
| symbols[].quoteAsset | string |  | Quote asset symbol.<br>计价资产符号。<br>例: `USD` |
| symbols[].baseAsset | string |  | Base asset symbol.<br>基础资产符号。<br>例: `BTC` |
| symbols[].marginAsset | string |  | Margin asset.<br>保证金币种.<br>例: `BTC` |
| symbols[].pricePrecision | integer (int64) |  | please do not use it as tickSize<br>价格小数点位数(仅作为系统精度使用，注意同tickSize 区分)<br>例: `1` |
| symbols[].quantityPrecision | integer (int64) |  | please do not use it as stepSize<br>数量小数点位数(仅作为系统精度使用，注意同stepSize 区分)<br>例: `0` |
| symbols[].baseAssetPrecision | integer (int64) |  | Base asset precision.<br>基础资产精度。<br>例: `8` |
| symbols[].quotePrecision | integer (int64) |  | Quote asset precision.<br>计价资产精度。<br>例: `8` |
| symbols[].equalQtyPrecision | integer (int64) |  | ignore<br>请忽略<br>例: `4` |
| symbols[].triggerProtect | string |  | threshold for algo order with "priceProtect"<br>开启"priceProtect"的条件订单的触发阈值<br>例: `0.0500` |
| symbols[].maintMarginPercent | string |  | ignore<br>请忽略<br>例: `2.5000` |
| symbols[].requiredMarginPercent | string |  | ignore<br>请忽略<br>例: `5.0000` |
| symbols[].underlyingType | string |  | Underlying asset type.<br>标的资产类型.<br>例: `COIN` |
| symbols[].underlyingSubType | string[] |  | Underlying asset sub-type.<br>标的资产子类型. |
| timezone | string |  | Timezone of market data.<br>行情数据时区。<br>例: `UTC` |

## Get Funding Rate History of Perpetual Futures（查询永续合约资金费率历史）

`GET /dapi/v1/fundingRate`

Get Funding Rate History of Perpetual Futures

查询永续合约资金费率历史

Operation ID: `getFundingRateHistoryOfPerpetualFutures`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `None` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding rate from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding rate until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `100`<br>例: `30` |

### 响应 200：Get Funding Rate History of Perpetual Futures / 获取Funding 利率 历史 of Perpetual 合约

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].fundingTime | integer (int64) |  | Funding time.<br>资金费时间.<br>例: `1596038400000` |
| [].fundingRate | string |  | Funding rate.<br>资金费率.<br>例: `-0.00300000` |

## Get Funding Rate Info（查询资金费率信息）

`GET /dapi/v1/fundingInfo`

Query funding rate info for symbols that had FundingRateCap/FundingRateFloor/fundingIntervalHours adjustment

查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours被特殊调整过的交易对

Operation ID: `getFundingRateInfo`

### 响应 200：Get Funding Rate Info / 获取Funding 利率 Info

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].adjustedFundingRateCap | string |  | Adjusted funding rate cap.<br>调整后资金费率上限.<br>例: `0.02500000` |
| [].adjustedFundingRateFloor | string |  | Adjusted funding rate floor.<br>调整后资金费率下限.<br>例: `-0.02500000` |
| [].fundingIntervalHours | integer (int64) |  | Funding interval in hours.<br>资金费结算间隔（小时）.<br>例: `8` |
| [].disclaimer | boolean |  | Disclaimer text.<br>免责声明文本.<br>例: `False` |

## Index Price and Mark Price（最新现货指数价格和Mark Price）

`GET /dapi/v1/premiumIndex`

Query index price and mark price

查询最新现货指数价格和Mark Price

Operation ID: `indexPriceAndMarkPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSD_PERP` |
| pair | query | string |  | 例: `BTCUSD` |

### 响应 200：Index Price and Mark Price / Index 价格 和 Mark 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].markPrice | string |  | mark price<br>标记价格<br>例: `11029.69574559` |
| [].indexPrice | string |  | index price<br>指数价格<br>例: `10979.14437500` |
| [].estimatedSettlePrice | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在交割开始前最后一小时有意义<br>例: `10981.74168236` |
| [].lastFundingRate | string |  | the lasted funding rate, for perpetual contract symbols only. For delivery symbols, "" will be shown.<br>最近更新的资金费率,只对永续合约有效，其他合约返回""<br>例: `0.00071003` |
| [].interestRate | string |  | the base asset interest rate, for perpetual contract symbols only. For delivery symbols, "" will be shown.<br>标的资产基础利率,只对永续合约有效，其他合约返回""<br>例: `0.00010000` |
| [].nextFundingTime | integer (int64) |  | For perpetual contract symbols only. For delivery symbols, 0 will be shown<br>下次资金费时间，只对永续合约有效，其他合约返回0<br>例: `1596096000000` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1596094042000` |

## Index Price Kline/Candlestick Data（价格指数K线数据）

`GET /dapi/v1/indexPriceKlines`

Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.

查询价格指数K线

权重: Based on parameter `LIMIT`

| LIMIT | weight |
| --- | --- |
| [1,100) | 1 |
| [100, 500) | 2 |
| [500, 1000] | 5 |
| > 1000 | 10 |

Operation ID: `indexPriceKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | After CM migration, accepts both CM and UM pair values.<br>标的交易对 迁移后支持传入 CM 与 UM 的 pair。<br>例: `BTCUSD` |
| interval | query | string | 是 | Interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Index Price Kline/Candlestick Data / Index 价格 K线/Candlestick Data

## Kline/Candlestick Data（K线数据）

`GET /dapi/v1/klines`

Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

每根K线的开盘时间可视为唯一ID

权重: Based on parameter `LIMIT`

| LIMIT | weight |
| --- | --- |
| [1,100) | 1 |
| [100, 500) | 2 |
| [500, 1000] | 5 |
| > 1000 | 10 |

Operation ID: `klineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | After CM migration, accepts both CM and UM symbols.<br>交易对 迁移后支持传入 CM 与 UM 的 symbol。<br>例: `BTCUSD` |
| interval | query | string | 是 | Interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Kline/Candlestick Data / K线/Candlestick Data

## Long/Short Ratio（多空持仓人数比）

`GET /futures/data/globalLongShortAccountRatio`

Query symbol Long/Short Ratio

多空持仓人数比

Operation ID: `longShortRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | BTCUSD<br>请参见英文说明：BTCUSD<br>例: `None` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| contractType | query | string |  | Contract type filter. If omitted, returns aggregated data across all contract types.<br>合约类型过滤。若不填，则返回所有合约类型的汇总数据。<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Long/Short Ratio / 请参见英文说明：Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].longShortRatio | string |  | Long/short ratio.<br>多空比.<br>例: `0.1960` |
| [].longAccount | string |  | 64.42%<br>例: `0.6622` |
| [].shortAccount | string |  | 35.58%<br>例: `0.3378` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1583139600000` |

## Mark Price Kline/Candlestick Data（标记价格K线数据）

`GET /dapi/v1/markPriceKlines`

Kline/candlestick bars for the mark price of a symbol. Klines are uniquely identified by their open time.

K线/candlestick bars 用于 the mark 价格 of a 交易对. K线s are uniquely identified by their 未完成 时间."

权重: Based on parameter `LIMIT`

| LIMIT | weight |
| --- | --- |
| [1,100) | 1 |
| [100, 500) | 2 |
| [500, 1000] | 5 |
| > 1000 | 10 |

Operation ID: `markPriceKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | After CM migration, accepts both CM and UM symbols.<br>交易对 迁移后支持传入 CM 与 UM 的 symbol。<br>例: `BTCUSD` |
| interval | query | string | 是 | Interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Mark Price Kline/Candlestick Data / Mark 价格 K线/Candlestick Data

## Old Trades Lookup (MARKET_DATA)（查询历史成交 (MARKET_DATA)）

`GET /dapi/v1/historicalTrades`

Get older market historical trades.

查询订单簿历史成交

Operation ID: `oldTradesLookup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `None` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `100`<br>例: `30` |
| fromId | query | integer (int64) |  | TradeId to fetch from. Default gets most recent trades.<br>从该 TradeId 开始获取数据。默认为获取最近的成交。<br>例: `595103` |

### 响应 200：Old Trades Lookup / Old 交易s Lookup

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | positionId<br>持仓 ID<br>例: `595103` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `9642.2` |
| [].qty | string |  | Quantity.<br>数量.<br>例: `1` |
| [].baseQty | string |  | Base asset quantity.<br>基础资产数量.<br>例: `0.01037108` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1499865549590` |
| [].isBuyerMaker | boolean |  | Whether buyer is market maker.<br>买方是否为做市方.<br>例: `True` |

## Open Interest（获取未平仓合约数）

`GET /dapi/v1/openInterest`

Get present open interest of a specific symbol.

合约持仓量

Operation ID: `openInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200626` |

### 响应 200：Open Interest / 未完成利息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200626` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| openInterest | string |  | Open interest.<br>未平仓量.<br>例: `15004` |
| contractType | string |  | Contract type.<br>合约类型.<br>例: `CURRENT_QUARTER` |
| time | integer (int64) |  | Time<br>时间<br>例: `1591261042378` |

## Open Interest Statistics（合约持仓量）

`GET /futures/data/openInterestHist`

Query open interest stats

合约持仓量

Operation ID: `openInterestStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | 例: `BTCUSD` |
| contractType | query | string |  | Contract type filter. If omitted, returns aggregated data across all contract types.<br>合约类型过滤。若不填，则返回所有合约类型的汇总数据。<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Open Interest Statistics / 未完成利息 Statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].contractType | string |  | Contract type.<br>合约类型.<br>例: `CURRENT_QUARTER` |
| [].sumOpenInterest | string |  | unit: cont<br>例: `20403` |
| [].sumOpenInterestValue | string |  | unit: base asset<br>例: `176196512.23400000` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Order Book（深度信息）

`GET /dapi/v1/depth`

Query orderbook on specific symbol

查询交易对深度

权重: Adjusted based on the limit:

| Limit | Weight |
| ------------ | ------------ |
| 5, 10, 20, 50 | 2 |
| 100 | 5 |
| 500 | 10 |
| 1000 | 20 |

Operation ID: `orderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| limit | query | integer (int64) |  | Valid limits:[5, 10, 20, 50, 100, 500, 1000].<br>可选限制:[5, 10, 20, 50, 100, 500, 1000].<br>默认: `500`<br>例: `500` |

### 响应 200：Order Book / 订单 Book

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| lastUpdateId | integer (int64) |  | Last update ID.<br>最后更新 ID.<br>例: `16769853` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| E | integer (int64) |  | Message output time<br>消息输出时间<br>例: `1591250106370` |
| T | integer (int64) |  | Transaction time<br>成交时间<br>例: `1591250106368` |
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |

## Premium index Kline Data（溢价指数K线数据）

`GET /dapi/v1/premiumIndexKlines`

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

合约溢价指数K线。每根K线的开盘时间可视为唯一ID。

权重: Based on parameter `LIMIT`

| LIMIT       | weight |
| ----------- | ------ |
| [1,100)     | 1      |
| [100, 500)  | 2      |
| [500, 1000] | 5      |
| > 1000      | 10     |

Operation ID: `premiumIndexKlineData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | After CM migration, accepts both CM and UM symbols.<br>交易对。迁移后支持传入 CM 与 UM 的 symbol。<br>例: `BTCUSD` |
| interval | query | string | 是 | Interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Premium index Kline Data / Premium index K线 Data

## Query Index Price Constituents（查询指数价格成分）

`GET /dapi/v1/constituents`

Query index price constituents

查询指数价格成分

Operation ID: `queryIndexPriceConstituents`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD` |

### 响应 200：Index Price Constituents / Index 价格 Constituents

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD` |
| time | integer (int64) |  | Time<br>时间<br>例: `1697422647853` |
| constituents | object[] |  | Constituent list.<br>成分列表. |
| constituents[].exchange | string |  | Exchange identifier.<br>交易所标识.<br>例: `bitstamp` |
| constituents[].symbol | string |  | Trading symbol<br>交易对<br>例: `btcusd` |
| constituents[].price | string |  | Price<br>价格<br>例: `94057.03000000` |
| constituents[].weight | string |  | Weight<br>权重<br>例: `0.25000000` |

## Recent Trades List（近期成交）

`GET /dapi/v1/trades`

Get recent market trades

获取近期订单簿成交

Operation ID: `recentTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `500`<br>例: `30` |

### 响应 200：Recent Trades List / Recent 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | positionId<br>持仓 ID<br>例: `28457` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `9635.0` |
| [].qty | string |  | Quantity.<br>数量.<br>例: `1` |
| [].baseQty | string |  | Base asset quantity.<br>基础资产数量.<br>例: `0.01037883` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1591250192508` |
| [].isBuyerMaker | boolean |  | Whether buyer is market maker.<br>买方是否为做市方.<br>例: `True` |

## Symbol Order Book Ticker（当前最优挂单）

`GET /dapi/v1/ticker/bookTicker`

Best price/qty on the order book for a symbol or symbols.

返回当前最优的挂单(最高买单,最低卖单)

权重: **2** for a single symbol, **5** when the symbol parameter is omitted

Operation ID: `symbolOrderBookTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| pair | query | string |  | Symbol<br>标的交易对<br>例: `BTCUSD` |

### 响应 200：Symbol Order Book Ticker / 交易对 订单 最优挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].lastUpdateId | integer (int64) |  | Last update ID.<br>最后更新 ID.<br>例: `1027024` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200626` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].bidPrice | string |  | Best bid price.<br>最佳买价.<br>例: `9650.1` |
| [].bidQty | string |  | Best bid quantity.<br>最佳买量.<br>例: `16` |
| [].askPrice | string |  | Best ask price.<br>最佳卖价.<br>例: `9650.3` |
| [].askQty | string |  | Best ask quantity.<br>最佳卖量.<br>例: `7` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1591257300345` |

## Symbol Price Ticker（最新价格）

`GET /dapi/v1/ticker/price`

Latest price for a symbol or symbols.

返回最近价格

权重: **1** for a single symbol, **2** when the symbol parameter is omitted

Operation ID: `symbolPriceTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| pair | query | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |

### 响应 200：Symbol Price Ticker / 交易对 价格 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200626` |
| [].ps | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `9647.8` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1591257246176` |

## Taker Buy/Sell Volume（合约主动买卖量）

`GET /futures/data/takerBuySellVol`

Taker Buy Volume: the total volume of buy orders filled by takers within
the period.

Taker Sell Volume: the total volume of sell orders filled by takers
within the period.

主动买入量：展示单位时间内主动买盘（Taker吃单买入）的成交量。
主动卖出量：展示单位时间内主动卖盘（Taker吃单卖出）的成交量。

Operation ID: `takerBuySellVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | 例: `BTCUSD` |
| contractType | query | string | 是 | 枚举: `ALL`, `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Taker Buy/Sell Volume / 请参见英文说明：Taker Buy/Sell Volume

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].contractType | string |  | Contract type.<br>合约类型.<br>例: `CURRENT_QUARTER` |
| [].takerBuyVol | string |  | unit: cont<br>例: `387` |
| [].takerSellVol | string |  | unit: cont<br>例: `248` |
| [].takerBuyVolValue | string |  | unit: base asset<br>例: `2342.1220` |
| [].takerSellVolValue | string |  | unit: base asset<br>例: `4213.9800` |
| [].timestamp | integer (int64) |  | Start time of the period, in milliseconds.<br>该周期的开始时间，单位为毫秒。<br>例: `1591261042378` |

## Test Connectivity（测试服务器连通性 PING）

`GET /dapi/v1/ping`

Test connectivity to the Rest API.

测试能否联通

Operation ID: `testConnectivity`

### 响应 200：OK / 成功

## 24hr Ticker Price Change Statistics（24hr价格变动情况）

`GET /dapi/v1/ticker/24hr`

24 hour rolling window price change statistics.

请注意,不携带symbol参数会返回全部交易对数据,不仅数据庞大,而且权重极高

权重: **1** for a single symbol, **40** when the symbol parameter is omitted
**Careful** when accessing this with no symbol.

Operation ID: `ticker24hrPriceChangeStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | query | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |

### 响应 200：24hr Ticker Price Change Statistics / 24hr 行情 价格 修改Statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].priceChange | string |  | Absolute price change in the 24h window.<br>24 小时窗口内绝对价格变化。<br>例: `136.6` |
| [].priceChangePercent | string |  | Percentage price change in the 24h window.<br>24 小时窗口内价格变化百分比。<br>例: `1.436` |
| [].weightedAvgPrice | string |  | Weighted average price in the 24h window.<br>24 小时窗口内加权平均价格。<br>例: `9547.3` |
| [].lastPrice | string |  | Latest traded price.<br>最新成交价。<br>例: `9651.6` |
| [].lastQty | string |  | Quantity of the latest trade.<br>最新一笔成交数量。<br>例: `1` |
| [].openPrice | string |  | Opening price of the 24h window.<br>24 小时窗口开盘价。<br>例: `9515.0` |
| [].highPrice | string |  | Highest price in the 24h window.<br>24 小时窗口最高价。<br>例: `9687.0` |
| [].lowPrice | string |  | Lowest price in the 24h window.<br>24 小时窗口最低价。<br>例: `9499.5` |
| [].volume | string |  | Base asset volume in the 24h window.<br>24 小时窗口基础资产成交量。<br>例: `494109` |
| [].baseVolume | string |  | Base asset volume.<br>基础资产成交量.<br>例: `5192.94797687` |
| [].openTime | integer (int64) |  | Start time of the 24h window (milliseconds).<br>24 小时窗口开始时间（毫秒）。<br>例: `1591170300000` |
| [].closeTime | integer (int64) |  | End time of the 24h window (milliseconds).<br>24 小时窗口结束时间（毫秒）。<br>例: `1591256718418` |
| [].firstId | integer (int64) |  | First tradeId<br>首笔成交id<br>例: `600507` |
| [].lastId | integer (int64) |  | Last tradeId<br>末笔成交id<br>例: `697803` |
| [].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `97297` |

## Top Trader Long/Short Account Ratio（大户账户数多空比）

`GET /futures/data/topLongShortAccountRatio`

The proportion of net long and net short accounts to total accounts of
the top 20% users with the highest margin balance. Each account is
counted once only.

Long Account % = Accounts of top traders with net long positions / Total
accounts of top traders with open positions

Short Account % = Accounts of top traders with net short positions /
Total accounts of top traders with open positions

Long/Short Ratio (Accounts) = Long Account % / Short Account %

持仓大户的净持仓多头和空头账户数占比，大户指保证金余额排名前20%的用户。一个账户记一次。
多仓账户数比例 = 持多仓大户数 / 总持仓大户数
空仓账户数比例 = 持空仓大户数 / 总持仓大户数
多空账户数比值 = 多仓账户数比例 / 空仓账户数比例

Operation ID: `topTraderLongShortRatioAccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | Pair<br>标的交易对<br>例: `BTCUSD` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| contractType | query | string |  | Contract type filter. If omitted, returns aggregated data across all contract types.<br>合约类型过滤。若不填，则返回所有合约类型的汇总数据。<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Top Trader Long/Short Ratio / Top 交易r Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].longShortRatio | string |  | Long/short ratio.<br>多空比.<br>例: `1.8105` |
| [].longAccount | string |  | 64.42%<br>例: `0.6442` |
| [].shortAccount | string |  | 35.58%<br>例: `0.3558` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Top Trader Long/Short Position Ratio（大户持仓量多空比）

`GET /futures/data/topLongShortPositionRatio`

The proportion of net long and net short positions to total open
positions of the top 20% users with the highest margin balance.

Long Position % = Long positions of top traders / Total open positions
of top traders

Short Position % = Short positions of top traders / Total open positions
of top traders

Long/Short Ratio (Positions) = Long Position % / Short Position %

大户的多头和空头总持仓量占比，大户指保证金余额排名前20%的用户。
多仓持仓量比例 = 大户多仓持仓量 / 大户总持仓量
空仓持仓量比例 = 大户空仓持仓量 / 大户总持仓量
多空持仓量比值 = 多仓持仓量比例 / 空仓持仓量比例

Operation ID: `topTraderLongShortRatioPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | 例: `BTCUSD` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| contractType | query | string |  | Contract type filter. If omitted, returns aggregated data across all contract types.<br>合约类型过滤。若不填，则返回所有合约类型的汇总数据。<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Top Trader Long/Short Ratio / Top 交易r Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].longShortRatio | string |  | Long/short ratio.<br>多空比.<br>例: `0.7869` |
| [].longPosition | string |  | 64.42%<br>例: `0.6442` |
| [].shortPosition | string |  | 44.04%<br>例: `0.4404` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1592870400000` |

## Account Trade List (USER_DATA)（账户成交历史 (USER_DATA)）

`GET /dapi/v1/userTrades`

Get trades for a specific account and symbol.

获取成交历史

权重: **20** with symbol，**40** with pair (after CM migration: **5** flat)

Operation ID: `accountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200626` |
| pair | query | string |  | pair<br>标的交易对<br>例: `BTCUSD` |
| orderId | query | string |  | Order ID<br>订单号<br>例: `1` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| fromId | query | integer (int64) |  | Trade id to fetch from. Default gets most recent trades.<br>从该成交 ID 开始获取数据. 默认获取最近的成交数据.<br>例: `6` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `50`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Trade List / 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200626` |
| [].id | integer (int64) |  | positionId<br>持仓 ID<br>例: `6` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `28` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `8800` |
| [].qty | string |  | Quantity.<br>数量.<br>例: `1` |
| [].realizedPnl | string |  | Realized PnL.<br>已实现盈亏.<br>例: `0` |
| [].marginAsset | string |  | Margin asset.<br>保证金币种.<br>例: `BTC` |
| [].baseQty | string |  | Base asset quantity. Populated for COIN-M symbols; returns "0" for USDⓈ-M symbols.<br>标的资产成交量。币本位合约交易对返回该值；U 本位合约交易对返回 "0"。<br>例: `0.01136364` |
| [].quoteQty | string |  | Quote asset quantity. Populated for USDⓈ-M symbols; returns "0" for COIN-M symbols.<br>计价资产成交额。U 本位合约交易对返回该值；币本位合约交易对返回 "0"。<br>例: `0` |
| [].commission | string |  | Transaction Fee (in Crypto)<br>交易手续费（以数字货币计）<br>例: `0.00000454` |
| [].commissionAsset | string |  | Commission asset.<br>手续费资产.<br>例: `BTC` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1590743483586` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| [].buyer | boolean |  | Whether the trade is a buy side for the account.<br>该成交对账户而言是否为买入方向.<br>例: `False` |
| [].maker | boolean |  | Whether the account is maker in this trade.<br>该成交中账户是否为做市方.<br>例: `False` |

## All Orders (USER_DATA)（查询所有订单(包括历史订单) (USER_DATA)）

`GET /dapi/v1/allOrders`

Get all account orders; active, canceled, or filled.

* These orders will not be found:
  * order status is CANCELED or EXPIRED AND order has NO filled trade AND created time + 3 days < current time
  * order create time + 90 days < current time

查询订单

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 CANCELED 或者 EXPIRED 并且 订单没有任何的成交记录 并且 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

权重: **20** with symbol, **40** with pair (after CM migration: **5** flat)

Operation ID: `allOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | query | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| orderId | query | integer (int64) |  | 例: `1917641` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `50`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Orders / All 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.0` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `abc` |
| [].cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0` |
| [].cumQuote | string |  | Cumulative quote asset amount.<br>成交金额(计价币种).<br>例: `0` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `1917641` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `0.40` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1579276756075` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `GTD` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auto cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `1579385751000` |

## Auto-Cancel All Open Orders (TRADE)（倒计时撤销所有订单 (TRADE)）

`POST /dapi/v1/countdownCancelAll`

Cancel all open orders of the specified symbol at the end of the
specified countdown. This rest endpoint means to ensure your open orders
are canceled in case of an outage. The endpoint should be called
repeatedly as heartbeats so that the existing countdown time can be
canceled and repalced by a new one. The system will check all countdowns
**approximately every 10 milliseconds**, so please note that sufficient
redundancy should be considered when using this function. We do not
recommend setting the countdown time to be too precise or too small.


* Example usage:

Call this endpoint at 30s intervals with an countdownTime of 120000
(120s).

If this endpoint is not called within 120 seconds, all your orders of
the specified symbol will be automatically canceled.

If this endpoint is called with an countdownTime of 0, the countdown
timer will be stopped.

倒计时撤销所有订单。该接口可以被用于确保在发生故障时撤销指定symbol上的所有挂单。
在使用这个功能时,接口应像心跳一样在倒计时内被反复调用,以便可以取消既有的倒计时并开始新的倒数计时设置。系统会**大约每10毫秒**检查一次所有倒计时情况,因此请注意,使用此功能时应考虑足够的冗余。

我们不建议将倒记时设置得太精确或太小。


* 用法示例：

以30s的间隔重复此接口,每次倒计时countdownTime设置为120000(120s)。

如果在120秒内未再次调用此接口,则您指定symbol上的所有挂单都会被自动撤销。

如果在120秒内以将countdownTime设置为0,则倒数计时器将终止,自动撤单功能取消。

Operation ID: `autoCancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSD_200925` |
| countdownTime | integer (int64) | 是 | countdown time, 1000 for 1 second. 0 to cancel the timer<br>倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。<br>例: `1000` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Auto-Cancel All Open Orders / Auto-取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| countdownTime | string |  | Countdown cancellation time in milliseconds.<br>倒计时撤单时间（毫秒）.<br>例: `100000` |

## Query Algo Order (USER_DATA)（查询条件订单 (USER_DATA)）

`GET /dapi/v1/algoOrder`

Check the status of an algo (conditional) order, such as TP/SL (Take Profit / Stop Loss) or trailing stop orders on COIN-M Futures.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询条件订单（Algo / Conditional Order）的状态，包括 币本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| clientAlgoId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Algo Order / Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `2146760` |
| clientAlgoId | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| algoType | string |  | 例: `CONDITIONAL` |
| orderType | string |  | 例: `TAKE_PROFIT` |
| symbol | string |  | 例: `BTCUSD_PERP` |
| side | string |  | 例: `SELL` |
| positionSide | string |  | 例: `BOTH` |
| timeInForce | string |  | 例: `GTC` |
| quantity | string |  | 例: `0.01` |
| algoStatus | string |  | 例: `CANCELED` |
| actualOrderId | string |  | Empty string if not triggered; orderId if triggered.<br>未触发时为空字符串；触发后为 orderId。<br>例: `` |
| actualPrice | string |  | 0 if not triggered; average price if filled/partially filled.<br>未触发时为 0；成交或部分成交后为平均成交价。<br>例: `0.00000` |
| actualType | string |  | Optional field, only present when triggered.<br>仅在触发后返回的可选字段。<br>例: `LIMIT` |
| actualQty | string |  | Optional field, only present when filled/partially filled.<br>仅在成交或部分成交后返回的可选字段。<br>例: `0.01` |
| triggerPrice | string |  | 例: `750.000` |
| price | string |  | 例: `750.000` |
| icebergQuantity | string |  | Reserved field, ignore.<br>预留字段，请忽略。<br>例: `null` |
| tpOrderType | string |  | 例: `` |
| selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| workingType | string |  | 例: `CONTRACT_PRICE` |
| priceMatch | string |  | 例: `NONE` |
| closePosition | boolean |  | 例: `False` |
| priceProtect | boolean |  | 例: `False` |
| reduceOnly | boolean |  | 例: `False` |
| createTime | integer (int64) |  | 例: `1750485492076` |
| updateTime | integer (int64) |  | 例: `1750514545091` |
| triggerTime | integer (int64) |  | 例: `0` |
| goodTillDate | integer (int64) |  | 例: `0` |

## New Algo Order (TRADE)（下条件单 (TRADE)）

`POST /dapi/v1/algoOrder`

Send in a new algo (conditional) order. Use this endpoint to place **TP/SL (Take Profit / Stop Loss)** and trailing stop orders on COIN-M Futures. Supported order types under `algoType=CONDITIONAL` are `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `STOP`, `TAKE_PROFIT`, and `TRAILING_STOP_MARKET`.

下新的条件单（Algo / Conditional Order），用于 币本位合约的**止盈止损（TP/SL, Take Profit / Stop Loss）**和追踪止损（Trailing Stop）。在 `algoType=CONDITIONAL` 下，支持的订单类型为 `STOP_MARKET`、`TAKE_PROFIT_MARKET`、`STOP`、`TAKE_PROFIT`、`TRAILING_STOP_MARKET`。

权重: 1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
0 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `newAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoType | string | 是 | 枚举: `CONDITIONAL`<br>例: `CONDITIONAL` |
| symbol | string | 是 | 例: `BTCUSD_PERP` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>例: `BOTH` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `STOP_MARKET` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| quantity | number (float) |  | quantity measured by contract number, Cannot be sent with `closePosition`=`true`(Close-All)<br>以合约数量计量的下单数量，使用`closePosition`不支持此参数。<br>例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| triggerPrice | number (float) |  | Trigger price<br>触发价<br>例: `1.0` |
| workingType | string |  | 枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| priceMatch | string |  | only available for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单类型可用；不能与 `price` 参数同时使用<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| closePosition | string |  | Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用<br>枚举: `true`, `false`<br>例: `true` |
| priceProtect | string |  | Used with `STOP_MARKET` or `TAKE_PROFIT_MARKET` order. when price reaches the triggerPrice ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price Protection Threshold of the symbol.<br>仅 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET` 订单类型可用。当价格达到触发价时，标记价格与合约最新价之间的价差不能超过该symbol的触发保护阈值。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`<br>双开模式下不接受此参数； 使用`closePosition`不支持此参数。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| activatePrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`)<br>追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)<br>例: `1.0` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders<br>追踪止损回调比例，可取值范围[0.1, 20],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数<br>例: `1` |
| clientAlgoId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的条件订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers / `EXPIRE_MAKER`: expire maker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`<br>订单自成交保护模式，默认 `NONE`。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `NONE`<br>例: `EXPIRE_TAKER` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Algo Order / New Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `2146760` |
| clientAlgoId | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| algoType | string |  | 例: `CONDITIONAL` |
| orderType | string |  | 例: `TAKE_PROFIT` |
| symbol | string |  | 例: `BTCUSD_PERP` |
| side | string |  | 例: `SELL` |
| positionSide | string |  | 例: `BOTH` |
| timeInForce | string |  | 例: `GTC` |
| quantity | string |  | 例: `0.01` |
| algoStatus | string |  | 例: `NEW` |
| triggerPrice | string |  | 例: `750.000` |
| price | string |  | 例: `750.000` |
| icebergQuantity | string |  | Reserved field, ignore.<br>预留字段，请忽略。<br>例: `null` |
| selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| workingType | string |  | 例: `CONTRACT_PRICE` |
| priceMatch | string |  | 例: `NONE` |
| closePosition | boolean |  | 例: `False` |
| priceProtect | boolean |  | 例: `False` |
| reduceOnly | boolean |  | 例: `False` |
| activatePrice | string |  | TRAILING_STOP_MARKET order<br>例: `` |
| callbackRate | string |  | TRAILING_STOP_MARKET order<br>例: `` |
| createTime | integer (int64) |  | 例: `1750485492076` |
| updateTime | integer (int64) |  | 例: `1750485492076` |
| triggerTime | integer (int64) |  | 例: `0` |
| goodTillDate | integer (int64) |  | 例: `0` |

## Cancel Algo Order (TRADE)（撤销条件订单 (TRADE)）

`DELETE /dapi/v1/algoOrder`

Cancel an active algo (conditional) order, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on COIN-M Futures.

撤销当前有效的条件单（Algo / Conditional Order），覆盖 币本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

Operation ID: `cancelAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | 例: `2146760` |
| clientAlgoId | query | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Algo Order / 取消Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `2146760` |
| clientAlgoId | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| code | string |  | 例: `200` |
| msg | string |  | 例: `success` |

## Cancel All Algo Open Orders (TRADE)（撤销全部条件订单 (TRADE)）

`DELETE /dapi/v1/algoOpenOrders`

Cancel all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on COIN-M Futures.

撤销某个交易对下的全部条件挂单（Algo / Conditional Order），覆盖 币本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

Operation ID: `cancelAllAlgoOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSD_PERP` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All Algo Open Orders / 取消All Algo 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `The operation of cancel all open order is done.` |

## Cancel All Open Orders (TRADE)（撤销全部订单 (TRADE)）

`DELETE /dapi/v1/allOpenOrders`

Cancel All Open Orders

撤销全部订单

Operation ID: `cancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All Open Orders / 取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `200` |
| msg | string |  | Message details.<br>消息详情.<br>例: `The operation of cancel all open order is done.` |

## Place Multiple Orders (TRADE)（批量下单 (TRADE)）

`POST /dapi/v1/batchOrders`

Place multiple orders

* Parameter rules are same with `New Order`
* Batch orders are processed concurrently, and the order of matching is not guaranteed.
* The order of returned contents for batch orders is the same as the order of the order list.

批量下单
* 具体订单条件规则,与普通下单一致
* 批量下单采取并发处理,不保证订单撮合顺序
* 批量下单的返回内容顺序,与订单列表顺序一致

Operation ID: `placeMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchOrders | object[] | 是 | order list. Max 5 orders<br>订单列表,最多支持5个订单 |
| batchOrders[].symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| batchOrders[].side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| batchOrders[].positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.<br>持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| batchOrders[].type | string | 是 | **After CM migration, stop-type values (`STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`) are no longer accepted on a per-element basis and will return element-level `-4120`. Use the new `/dapi/v1/algoOrder` endpoint instead.**<br>**迁移后,本接口对 stop 类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`)按元素级别拒绝,返回元素级 `-4120`。请改用新接口 `/dapi/v1/algoOrder`。**<br>枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| batchOrders[].timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| batchOrders[].quantity | number (float) | 是 | quantity measured by contract number<br>以合约数量计量的下单数量<br>例: `1` |
| batchOrders[].reduceOnly | string |  | 枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| batchOrders[].price | number (float) |  | Order price<br>委托价格<br>例: `10001` |
| batchOrders[].newClientOrderId | string |  | A unique id among open orders. Automatically generated if<br>not sent. Can only be string following the rule:<br>`^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| batchOrders[].stopPrice | number (float) |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数<br>例: `9000` |
| batchOrders[].activationPrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the<br>latest price(supporting different `workingType`)<br>追踪止损激活价格,仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)<br>例: `9020` |
| batchOrders[].callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 4 where 1 for 1%<br>追踪止损回调比例,可取值范围[0.1, 4],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数<br>例: `1` |
| batchOrders[].workingType | string |  | 枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| batchOrders[].priceProtect | string |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| batchOrders[].newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| batchOrders[].priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can't be passed together with `price`<br>仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单可用; 不能与 `price` 同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| batchOrders[].selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers/<br>`EXPIRE_MAKER`: expire taker order when STP triggers/<br>`EXPIRE_BOTH`: expire both orders when STP triggers<br>`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`，默认`EXPIRE_MAKER`<br>枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`<br>默认: `EXPIRE_MAKER`<br>例: `EXPIRE_TAKER` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Place Multiple Orders / 下单Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `testOrder` |
| [].cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `22542179` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `10` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1566818724722` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `-2022` |
| [].msg | string |  | Message details.<br>消息详情.<br>例: `ReduceOnly Order is rejected.` |

## Modify Multiple Orders (TRADE)（批量修改订单 (TRADE)）

`PUT /dapi/v1/batchOrders`

Modify Multiple Orders

批量修改订单

Operation ID: `modifyMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchOrders | object[] | 是 | order list. Max 5 orders<br>订单列表,最多支持5个订单 |
| batchOrders[].orderId | integer (int64) |  | Sub-order ID, required when clientOrderId is not sent.<br>子订单 ID,当clientOrderId未发送时必填.<br>例: `20072994037` |
| batchOrders[].origClientOrderId | string |  | Client order ID, required when orderId is not sent. Only support letters, numbers and underscores, and must be unique within 24 hours.<br>客户端订单 ID,当orderId未发送时必填.仅支持字母、数字和下划线，且在24小时内必须唯一。<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| batchOrders[].symbol | string | 是 | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| batchOrders[].side | string | 是 | Trading side<br>买卖方向<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| batchOrders[].quantity | number (float) |  | Order quantity, cannot be sent with closePosition=true. **After CM migration, this parameter becomes mandatory** (each batch element must send both `price` and `quantity`).<br>订单数量,当closePosition=true时不能发送。**迁移后此参数变为必传**(批量中每一个元素都必须同时传 `price` 与 `quantity`)。<br>例: `1` |
| batchOrders[].price | number (float) |  | Latest token price. **After CM migration, this parameter becomes mandatory** (each batch element must send both `price` and `quantity`).<br>代币最新价格。**迁移后此参数变为必传**(批量中每一个元素都必须同时传 `price` 与 `quantity`)。<br>例: `30005` |
| batchOrders[].modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| batchOrders[].recvWindow | integer (int64) |  | 例: `5000` |
| batchOrders[].timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Multiple Orders / Modify Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `20072994037` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `30005` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| [].cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `LONG` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1629182711600` |
| [].code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `-2022` |
| [].msg | string |  | Message details.<br>消息详情.<br>例: `ReduceOnly Order is rejected.` |

## Cancel Multiple Orders (TRADE)（批量撤销订单 (TRADE)）

`DELETE /dapi/v1/batchOrders`

Cancel Multiple Orders

批量撤销订单

Operation ID: `cancelMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderIdList | query | integer (int64)[] |  | Order IDs to cancel.<br>需要撤销的系统订单号列表. |
| origClientOrderIdList | query | string[] |  | Original client order IDs to cancel.<br>需要撤销的用户自定义订单号列表. |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Multiple Orders / 取消Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `myOrder1` |
| [].cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `283194212` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `11` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1571110484038` |
| [].code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `-2011` |
| [].msg | string |  | Message details.<br>消息详情.<br>例: `Unknown order sent.` |

## Query Order (USER_DATA)（查询订单 (USER_DATA)）

`GET /dapi/v1/order`

Check an order's status.

* These orders will not be found:
  * order status is CANCELED or EXPIRED AND order has NO filled trade AND created time + 3 days < current time
  * order create time + 90 days < current time

查询订单状态

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 CANCELED 或者 EXPIRED 并且 订单没有任何的成交记录 并且 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order / 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.0` |
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `abc` |
| cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0` |
| executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `1573346959` |
| origQty | string |  | Original order quantity<br>原始委托数量<br>例: `0.40` |
| origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| time | integer (int64) |  | Time<br>时间<br>例: `1579276756075` |
| timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## New Order (TRADE)（下单 (TRADE)）

`POST /dapi/v1/order`

Send in a new order.

发送新订单.

权重: 1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M)
0 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `newOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| type | string | 是 | **After CM migration, stop-type values (`STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`) are no longer accepted by this endpoint and will return `-4120`. Use the new `/dapi/v1/algoOrder` endpoint instead.**<br>**迁移后,本接口不再接受 stop 类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`),会返回 `-4120`。请改用新接口 `/dapi/v1/algoOrder`。**<br>枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| reduceOnly | string |  | "true" or "false". Cannot be sent in Hedge<br>Mode; cannot be sent with `closePosition`=`true`(Close-All)<br>`true`, `false`; 非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| quantity | number (float) |  | quantity measured by contract number, Cannot be sent with `closePosition`=`true`<br>以合约数量计量的下单数量，使用`closePosition`不支持此参数。<br>例: `1.0` |
| price | number (float) |  | Order price<br>委托价格<br>例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if<br>not sent. Can only be string following the rule:<br>`^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| stopPrice | number (float) |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数<br>例: `1.0` |
| closePosition | string |  | `true`, `false`；Close-All,used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>`true`,<br>`false`；触发后全部平仓,仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果,不与`reduceOnly`<br>合用<br>例: `true` |
| activationPrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the<br>latest price(supporting different `workingType`)<br>追踪止损激活价格,仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)<br>例: `1.0` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%<br>追踪止损回调比例,可取值范围[0.1, 10],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数<br>例: `5000.0` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| workingType | string |  | 'stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE".<br>"stopPrice 触发类型: `MARK_PRICE`(标记价格), `CONTRACT_PRICE`(合约最新价).<br>枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| priceProtect | string |  | "true" or "false". Used with<br>`STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET`<br>orders.<br>条件单触发保护："true","false", 默认"false". 仅 `STOP`, `STOP_MARKET`,<br>`TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order;<br>Can't be passed together with `price`<br>仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单可用，不能与 `price` 同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers/<br>`EXPIRE_MAKER`: expire taker order when STP triggers/<br>`EXPIRE_BOTH`: expire both orders when STP triggers<br>`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`默认`EXPIRE_MAKER`<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `EXPIRE_MAKER`<br>例: `EXPIRE_TAKER` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Order / New 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `testOrder` |
| cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `22542179` |
| origQty | string |  | Original order quantity<br>原始委托数量<br>例: `10` |
| price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1566818724722` |
| workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Modify Order (TRADE)（修改订单 (TRADE)）

`PUT /dapi/v1/order`

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

Operation ID: `modifyOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) |  | Order quantity, cannot be sent with `closePosition=true`. **After CM migration, this parameter becomes mandatory** (must be sent together with `price`).<br>下单数量,使用`closePosition`不支持此参数。**迁移后此参数变为必传**(需与 `price` 同时传)。<br>例: `1.0` |
| price | number (float) |  | Order price. **After CM migration, this parameter becomes mandatory** (must be sent together with `quantity`).<br>委托价格。**迁移后此参数变为必传**(需与 `quantity` 同时传)。<br>例: `1.0` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>盘口价格下单模式,仅对`LIMIT`/`STOP`/`TAKE_PROFIT`订单有效,与`price`参数互斥<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Order / Modify 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `20072994037` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| price | string |  | Latest token price.<br>代币最新价格。<br>例: `30005` |
| origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position side<br>持仓方向<br>例: `LONG` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1629182711600` |

## Cancel Order (TRADE)（撤销订单 (TRADE)）

`DELETE /dapi/v1/order`

Cancel an active order.

撤销订单

Operation ID: `cancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `283194212` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `myOrder1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Order / 取消订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `myOrder1` |
| cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `283194212` |
| origQty | string |  | Original order quantity<br>原始委托数量<br>例: `11` |
| price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1571110484038` |
| workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Change Initial Leverage (TRADE)（调整开仓杠杆 (TRADE)）

`POST /dapi/v1/leverage`

Change user's initial leverage in the specific symbol market.

For Hedge Mode, LONG and SHORT positions of one symbol use the same
initial leverage and share a total notional value.

调整用户在指定symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数,共享允许的最大交易标的资产数量。

Operation ID: `changeInitialLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| leverage | integer (int64) | 是 | target initial leverage: int from 1 to 125<br>目标杠杆倍数<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Initial Leverage / 修改Initial Leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leverage | integer (int64) |  | Leverage value.<br>杠杆倍数.<br>例: `21` |
| maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `1000` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |

## Change Margin Type (TRADE)（变换逐全仓模式 (TRADE)）

`POST /dapi/v1/marginType`

Change user's margin type in the specific symbol market.For Hedge Mode,
LONG and SHORT positions of one symbol use the same margin type.

With ISOLATED margin type, margins of the LONG and SHORT positions are
isolated from each other.

变换用户在指定 symbol 合约上的保证金模式：逐仓或全仓。
不同持仓方向上使用相同的保证金模式。双向持仓模式下的逐仓,`LONG` 与 `SHORT`使用独立的逐仓仓位。

Operation ID: `changeMarginType`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| marginType | string | 是 | 枚举: `ISOLATED`, `CROSSED`<br>例: `ISOLATED` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Margin Type / 修改杠杆 类型

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `200` |
| msg | string |  | Message details.<br>消息详情.<br>例: `success` |

## Current All Algo Open Orders (USER_DATA)（查看当前全部条件挂单 (USER_DATA)）

`GET /dapi/v1/openAlgoOrders`

Get all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on COIN-M Futures.

查看某个交易对下当前所有的条件挂单（Algo / Conditional Order），包括 币本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

权重: **1** for a single symbol; **40** when the symbol parameter is omitted

**Careful** when accessing this with no symbol.

Operation ID: `currentAllAlgoOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoType | query | string |  | 例: `CONDITIONAL` |
| symbol | query | string |  | 例: `BTCUSD_PERP` |
| algoId | query | integer (int64) |  | 例: `2148627` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current All Algo Open Orders / 当前 All Algo 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].algoId | integer (int64) |  | 例: `2148627` |
| [].clientAlgoId | string |  | 例: `MRumok0dkhrP4kCm12AHaB` |
| [].algoType | string |  | 例: `CONDITIONAL` |
| [].orderType | string |  | 例: `TAKE_PROFIT` |
| [].symbol | string |  | 例: `BTCUSD_PERP` |
| [].side | string |  | 例: `SELL` |
| [].positionSide | string |  | 例: `BOTH` |
| [].timeInForce | string |  | 例: `GTC` |
| [].quantity | string |  | 例: `0.01` |
| [].algoStatus | string |  | 例: `NEW` |
| [].actualOrderId | string |  | 例: `` |
| [].actualPrice | string |  | 例: `0.00000` |
| [].triggerPrice | string |  | 例: `750.000` |
| [].price | string |  | 例: `750.000` |
| [].icebergQuantity | string |  | Reserved field, ignore.<br>预留字段，请忽略。<br>例: `null` |
| [].tpTriggerPrice | string |  | 例: `0.000` |
| [].tpPrice | string |  | 例: `0.000` |
| [].slTriggerPrice | string |  | 例: `0.000` |
| [].slPrice | string |  | 例: `0.000` |
| [].tpOrderType | string |  | 例: `` |
| [].selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| [].workingType | string |  | 例: `CONTRACT_PRICE` |
| [].priceMatch | string |  | 例: `NONE` |
| [].closePosition | boolean |  | 例: `False` |
| [].priceProtect | boolean |  | 例: `False` |
| [].reduceOnly | boolean |  | 例: `False` |
| [].createTime | integer (int64) |  | 例: `1750514941540` |
| [].updateTime | integer (int64) |  | 例: `1750514941540` |
| [].triggerTime | integer (int64) |  | 例: `0` |
| [].goodTillDate | integer (int64) |  | 例: `0` |

## Current All Open Orders (USER_DATA)（查看当前全部挂单 (USER_DATA)）

`GET /dapi/v1/openOrders`

Get all open orders on a symbol. **Careful** when accessing this with no symbol.

查看当前全部挂单

权重: **1** for a single symbol, **40** for mutltiple symbols

Operation ID: `currentAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol. **After CM migration, an invalid `symbol` returns `-1121` (previously a silent `200`).**<br>交易对。**迁移后,传入非法 `symbol` 会返回 `-1121`(此前为静默返回 `200`)。**<br>例: `BTCUSD_200925` |
| pair | query | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current All Open Orders / 当前 All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.0` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `abc` |
| [].cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `1917641` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `0.40` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1579276756075` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Get Order Modify History (USER_DATA)（查询订单修改历史 (USER_DATA)）

`GET /dapi/v1/orderAmendment`

Get order modification history

查询订单修改历史

Operation ID: `getOrderModifyHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `20072994037` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| startTime | query | integer (int64) |  | Timestamp in ms to get modification history from INCLUSIVE<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get modification history until INCLUSIVE<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `50`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Order Modify History / 获取订单 Modify 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amendmentId | integer (int64) |  | Order modification ID<br>修改记录号<br>例: `5363` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `20072994037` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1629184560899` |
| [].amendment | object |  | Order amendment details.<br>订单修改详情. |
| [].amendment.price | object |  | Latest token price.<br>代币最新价格。 |
| [].amendment.price.before | string |  | Before value.<br>之前的值.<br>例: `30004` |
| [].amendment.price.after | string |  | After value.<br>之后的值.<br>例: `30003.2` |
| [].amendment.origQty | object |  | Original order quantity<br>原始委托数量 |
| [].amendment.origQty.before | string |  | Before value.<br>之前的值.<br>例: `1` |
| [].amendment.origQty.after | string |  | After value.<br>之后的值.<br>例: `1` |
| [].amendment.count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `3` |
| [].amendment.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `123` |

## Get Position Margin Change History (TRADE)（逐仓保证金变动历史 (TRADE)）

`GET /dapi/v1/positionMargin/history`

Get position margin change history

逐仓保证金变动历史

Operation ID: `getPositionMarginChangeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSD` |
| type | query | integer (int64) |  | 1: Add position margin,2: Reduce position margin<br>调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金<br>例: `1` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `50`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Position Margin Change History / 获取持仓 杠杆 修改历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amount | string |  | Amount.<br>金额.<br>例: `23.36332311` |
| [].asset | string |  | asset name<br>资产<br>例: `BTC` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1578047897183` |
| [].type | integer (int64) |  | Order type.<br>订单类型.<br>例: `1` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |

## Modify Isolated Position Margin (TRADE)（调整逐仓保证金 (TRADE)）

`POST /dapi/v1/positionMargin`

Modify Isolated Position Margin

针对逐仓模式下的仓位,调整其逐仓保证金资金。

Operation ID: `modifyIsolatedPositionMargin`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.<br>持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| amount | number (float) | 是 | Margin asset<br>保证金资金<br>例: `1.0` |
| type | integer (int64) | 是 | 1: Add position margin,2: Reduce position margin<br>调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Isolated Position Margin / Modify Isolated 持仓 杠杆

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) |  | Amount.<br>金额.<br>例: `100` |
| code | integer (int64) |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `200` |
| msg | string |  | Message details.<br>消息详情.<br>例: `Successfully modify position margin.` |
| type | integer (int64) |  | Order type.<br>订单类型.<br>例: `1` |

## Position ADL Quantile Estimation (USER_DATA)（持仓ADL队列估算 (USER_DATA)）

`GET /dapi/v1/adlQuantile`

Query position ADL quantile estimation

* Values update every 30s.
* Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
* For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
* If the positions of the symbol are crossed margined in Hedge Mode:
  * "HEDGE" as a sign will be returned instead of "BOTH";
  * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.

查询持仓ADL队列估算


* 每30秒更新数据
* 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
* 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
* 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。

Operation ID: `positionAdlQuantileEstimation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_200925` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Position ADL Quantile Estimation / 持仓 ADL Quantile Estimation

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].adlQuantile | object |  | ADL quantile information.<br>ADL 分位信息. |
| [].adlQuantile.LONG | integer (int64) |  | adl quantile for "LONG" position in hedge mode<br>双开模式下多头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.SHORT | integer (int64) |  | adl qauntile for "SHORT" position in hedge mode<br>双开模式下空头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.HEDGE | integer (int64) |  | Hedge mode ADL quantile.<br>双向持仓模式 ADL 分位.<br>例: `0` |
| [].adlQuantile.BOTH | integer (int64) |  | One-way mode ADL quantile.<br>单向持仓模式 ADL 分位.<br>例: `0` |

## Position Information (USER_DATA)（用户持仓风险 (USER_DATA)）

`GET /dapi/v1/positionRisk`

Get current account information.

查询用户持仓风险

Operation ID: `positionInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| marginAsset | query | string |  | 例: `USDT` |
| pair | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Position Information / 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_201225` |
| [].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| [].entryPrice | string |  | Position entry price.<br>持仓开仓价格.<br>例: `0.0` |
| [].breakEvenPrice | string |  | break-even price<br>盈亏平衡价<br>例: `0.0` |
| [].markPrice | string |  | mark price<br>标记价格<br>例: `0.00000000` |
| [].unRealizedProfit | string |  | Unrealized profit.<br>未实现盈亏.<br>例: `0.00000000` |
| [].liquidationPrice | string |  | Liquidation price.<br>强平价格.<br>例: `0` |
| [].leverage | string |  | Leverage value.<br>杠杆倍数.<br>例: `125` |
| [].maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `50` |
| [].marginType | string |  | Margin type.<br>保证金模式.<br>例: `cross` |
| [].isolatedMargin | string |  | Isolated margin amount.<br>逐仓保证金数量.<br>例: `0.00000000` |
| [].isAutoAddMargin | string |  | Whether auto-add margin is enabled.<br>是否开启自动追加保证金.<br>例: `false` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |

## Query All Algo Orders (USER_DATA)（查询所有条件订单(包括历史订单) (USER_DATA)）

`GET /dapi/v1/allAlgoOrders`

Get all algo (conditional) orders — active, CANCELED, TRIGGERED, or FINISHED — including TP/SL (Take Profit / Stop Loss) and trailing stop orders on COIN-M Futures.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询所有条件订单（Algo / Conditional Order），包括活跃、已撤销、已触发与已完成订单，覆盖 币本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）。

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryAllAlgoOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| algoId | query | integer (int64) |  | 例: `2146760` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Algo Orders / All Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].algoId | integer (int64) |  | 例: `2146760` |
| [].clientAlgoId | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| [].algoType | string |  | 例: `CONDITIONAL` |
| [].orderType | string |  | 例: `TAKE_PROFIT` |
| [].symbol | string |  | 例: `BTCUSD_PERP` |
| [].side | string |  | 例: `SELL` |
| [].positionSide | string |  | 例: `BOTH` |
| [].timeInForce | string |  | 例: `GTC` |
| [].quantity | string |  | 例: `0.01` |
| [].algoStatus | string |  | 例: `CANCELED` |
| [].actualOrderId | string |  | 例: `` |
| [].actualPrice | string |  | 例: `0.00000` |
| [].triggerPrice | string |  | 例: `750.000` |
| [].price | string |  | 例: `750.000` |
| [].icebergQuantity | string |  | Reserved field, ignore.<br>预留字段，请忽略。<br>例: `null` |
| [].tpTriggerPrice | string |  | 例: `0.000` |
| [].tpPrice | string |  | 例: `0.000` |
| [].slTriggerPrice | string |  | 例: `0.000` |
| [].slPrice | string |  | 例: `0.000` |
| [].tpOrderType | string |  | 例: `` |
| [].selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| [].workingType | string |  | 例: `CONTRACT_PRICE` |
| [].priceMatch | string |  | 例: `NONE` |
| [].closePosition | boolean |  | 例: `False` |
| [].priceProtect | boolean |  | 例: `False` |
| [].reduceOnly | boolean |  | 例: `False` |
| [].createTime | integer (int64) |  | 例: `1750485492076` |
| [].updateTime | integer (int64) |  | 例: `1750514545091` |
| [].triggerTime | integer (int64) |  | 例: `0` |
| [].goodTillDate | integer (int64) |  | 例: `0` |

## Query Current Open Order (USER_DATA)（查询当前挂单 (USER_DATA)）

`GET /dapi/v1/openOrder`

Query Current Open Order

查询当前挂单

Operation ID: `queryCurrentOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Open Order / 当前 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.0` |
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `abc` |
| cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0` |
| executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `1917641` |
| origQty | string |  | Original order quantity<br>原始委托数量<br>例: `0.40` |
| origType | string |  | Original order type.<br>原始订单类型.<br>例: `TRAILING_STOP_MARKET` |
| price | string |  | Latest token price.<br>代币最新价格。<br>例: `0` |
| reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| time | integer (int64) |  | Time<br>时间<br>例: `1579276756075` |
| timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| type | string |  | Order type.<br>订单类型.<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## User's Force Orders (USER_DATA)（用户强平单历史 (USER_DATA)）

`GET /dapi/v1/forceOrders`

User's Force Orders

用户强平单历史

权重: **20** (after CM migration: **20** with symbol / **50** without symbol)

Operation ID: `usersForceOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_200925` |
| autoCloseType | query | string |  | 枚举: `LIQUIDATION`, `ADL`<br>例: `LIQUIDATION` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `50`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value<br>must reflect the current client time and is validated by the server<br>for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User's Force Orders / 用户's Force 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `165123080` |
| [].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| [].status | string |  | Status.<br>订单状态<br>例: `FILLED` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `autoclose-1596542005017000006` |
| [].price | string |  | Latest token price.<br>代币最新价格。<br>例: `11326.9` |
| [].avgPrice | string |  | Average execution price<br>平均价格<br>例: `11326.9` |
| [].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| [].executedQty | string |  | Executed quantity<br>执行数量<br>例: `1` |
| [].cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0.00882854` |
| [].cumQuote | string |  | Cumulative quote asset amount.<br>成交金额(计价币种).<br>例: `100` |
| [].timeInForce | string |  | Time in force<br>有效方式<br>例: `IOC` |
| [].type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| [].reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| [].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| [].workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1596542005019` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1596542005050` |
| [].goodTillDate | integer (int64) |  | order pre-set auto cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |

## Start User Data Stream (USER_STREAM)（生成listenKey (USER_STREAM)）

`POST /dapi/v1/listenKey`

Start a new user data stream. The stream will close after 60 minutes
unless a keepalive is sent. If the account has an active `listenKey`,
that `listenKey` will be returned and its validity will be extended for
60 minutes.

创建一个新的user data
stream,返回值为一个listenKey,即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`,则将返回该`listenKey`并将其有效期延长60分钟。

Operation ID: `startUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | Listen key.<br>监听密钥.<br>例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1` |

## Keepalive User Data Stream (USER_STREAM)（延长listenKey有效期 (USER_STREAM)）

`PUT /dapi/v1/listenKey`

Keepalive a user data stream to prevent a time out. User data streams
will close after 60 minutes.

有效期延长至本次调用后60分钟

Operation ID: `keepaliveUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Keepalive User Data Stream / Keepalive 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | Listen key.<br>监听密钥.<br>例: `vmNt6gl1so8bXVsaAY153FG5tf63QaODxUarKUM8V8rY4ElSwEe431DNIYNKOkQp` |

## Close User Data Stream (USER_STREAM)（关闭listenKey (USER_STREAM)）

`DELETE /dapi/v1/listenKey`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功