---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api
api_type: REST
updated_at: 2026-11-25 18:49:14.358053
---

# Futures (USDⓈ-M) REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade USDⓈ-M perpetual futures.

访问市场数据、管理账户，并交易 USDⓈ-M 永续合约。

版本: 1.0.0

## 服务地址

- `https://fapi.binance.com`
- `https://testnet.binancefuture.com`

## 接口列表

- `GET /fapi/v2/account` — Account Information V2 (USER_DATA)
- `GET /fapi/v3/account` — Account Information V3 (USER_DATA)
- `GET /fapi/v2/balance` — Futures Account Balance V2 (USER_DATA)
- `GET /fapi/v3/balance` — Futures Account Balance V3 (USER_DATA)
- `GET /fapi/v1/accountConfig` — Futures Account Configuration (USER_DATA)
- `GET /fapi/v1/apiTradingStatus` — Futures Trading Quantitative Rules Indicators (USER_DATA)
- `GET /fapi/v1/feeBurn` — Get BNB Burn Status (USER_DATA)
- `POST /fapi/v1/feeBurn` — Toggle BNB Burn On Futures Trade (TRADE)
- `GET /fapi/v1/multiAssetsMargin` — Get Current Multi-Assets Mode (USER_DATA)
- `POST /fapi/v1/multiAssetsMargin` — Change Multi-Assets Mode (TRADE)
- `GET /fapi/v1/positionSide/dual` — Get Current Position Mode (USER_DATA)
- `POST /fapi/v1/positionSide/dual` — Change Position Mode (TRADE)
- `GET /fapi/v1/order/asyn` — Get Download Id For Futures Order History (USER_DATA)
- `GET /fapi/v1/trade/asyn` — Get Download Id For Futures Trade History (USER_DATA)
- `GET /fapi/v1/income/asyn` — Get Download Id For Futures Transaction History (USER_DATA)
- `GET /fapi/v1/order/asyn/id` — Get Futures Order History Download Link by Id (USER_DATA)
- `GET /fapi/v1/trade/asyn/id` — Get Futures Trade Download Link by Id (USER_DATA)
- `GET /fapi/v1/income/asyn/id` — Get Futures Transaction History Download Link by Id (USER_DATA)
- `GET /fapi/v1/income` — Get Income History (USER_DATA)
- `GET /fapi/v1/leverageBracket` — Notional and Leverage Brackets (USER_DATA)
- `GET /fapi/v1/rateLimit/order` — Query User Rate Limit (USER_DATA)
- `GET /fapi/v1/symbolConfig` — Symbol Configuration (USER_DATA)
- `GET /fapi/v1/commissionRate` — User Commission Rate (USER_DATA)
- `POST /fapi/v1/convert/acceptQuote` — Accept the offered quote (USER_DATA)
- `GET /fapi/v1/convert/exchangeInfo` — List All Convert Pairs
- `GET /fapi/v1/convert/orderStatus` — Order status (USER_DATA)
- `POST /fapi/v1/convert/getQuote` — Send Quote Request (USER_DATA)
- `GET /fapi/v1/symbolAdlRisk` — ADL Risk
- `GET /futures/data/basis` — Basis
- `GET /fapi/v1/time` — Check Server Time
- `GET /fapi/v1/indexInfo` — Composite Index Symbol Information
- `GET /fapi/v1/aggTrades` — Compressed/Aggregate Trades List
- `GET /fapi/v1/continuousKlines` — Continuous Contract Kline/Candlestick Data
- `GET /fapi/v1/exchangeInfo` — Exchange Information
- `GET /fapi/v1/fundingRate` — Get Funding Rate History
- `GET /fapi/v1/fundingInfo` — Get Funding Rate Info
- `GET /fapi/v1/indexPriceKlines` — Index Price Kline/Candlestick Data
- `GET /fapi/v1/klines` — Kline/Candlestick Data
- `GET /futures/data/globalLongShortAccountRatio` — Long/Short Ratio
- `GET /fapi/v1/premiumIndex` — Mark Price
- `GET /fapi/v1/markPriceKlines` — Mark Price Kline/Candlestick Data
- `GET /fapi/v1/assetIndex` — Multi-Assets Mode Asset Index
- `GET /fapi/v1/historicalTrades` — Old Trades Lookup (MARKET_DATA)
- `GET /fapi/v1/openInterest` — Open Interest
- `GET /futures/data/openInterestHist` — Open Interest Statistics
- `GET /fapi/v1/depth` — Order Book
- `GET /fapi/v1/premiumIndexKlines` — Premium index Kline Data
- `GET /futures/data/delivery-price` — Quarterly Contract Settlement Price
- `GET /fapi/v1/constituents` — Query Index Price Constituents
- `GET /fapi/v1/insuranceBalance` — Query Insurance Fund Balance Snapshot
- `GET /fapi/v1/trades` — Recent Trades List
- `GET /fapi/v1/rpiDepth` — RPI Order Book
- `GET /fapi/v1/ticker/bookTicker` — Symbol Order Book Ticker
- `GET /fapi/v1/ticker/price` — Symbol Price Ticker
- `GET /fapi/v2/ticker/price` — Symbol Price Ticker V2
- `GET /futures/data/takerlongshortRatio` — Taker Buy/Sell Volume
- `GET /fapi/v1/ping` — Test Connectivity
- `GET /fapi/v1/ticker/24hr` — 24hr Ticker Price Change Statistics
- `GET /futures/data/topLongShortAccountRatio` — Top Trader Long/Short Account Ratio (MARKET_DATA)
- `GET /futures/data/topLongShortPositionRatio` — Top Trader Long/Short Position Ratio (MARKET_DATA)
- `GET /fapi/v1/tradingSchedule` — Trading Schedule
- `GET /fapi/v1/pmAccountInfo` — Classic Portfolio Margin Account Information (USER_DATA)
- `GET /fapi/v1/userTrades` — Account Trade List (USER_DATA)
- `GET /fapi/v1/allOrders` — All Orders (USER_DATA)
- `POST /fapi/v1/countdownCancelAll` — Auto-Cancel All Open Orders (TRADE)
- `GET /fapi/v1/algoOrder` — Query Algo Order (USER_DATA)
- `POST /fapi/v1/algoOrder` — New Algo Order (TRADE)
- `DELETE /fapi/v1/algoOrder` — Cancel Algo Order (TRADE)
- `DELETE /fapi/v1/algoOpenOrders` — Cancel All Algo Open Orders (TRADE)
- `DELETE /fapi/v1/allOpenOrders` — Cancel All Open Orders (TRADE)
- `POST /fapi/v1/batchOrders` — Place Multiple Orders (TRADE)
- `PUT /fapi/v1/batchOrders` — Modify Multiple Orders (TRADE)
- `DELETE /fapi/v1/batchOrders` — Cancel Multiple Orders (TRADE)
- `GET /fapi/v1/order` — Query Order (USER_DATA)
- `POST /fapi/v1/order` — New Order (TRADE)
- `PUT /fapi/v1/order` — Modify Order (TRADE)
- `DELETE /fapi/v1/order` — Cancel Order (TRADE)
- `POST /fapi/v1/leverage` — Change Initial Leverage (TRADE)
- `POST /fapi/v1/marginType` — Change Margin Type (TRADE)
- `GET /fapi/v1/openAlgoOrders` — Current All Algo Open Orders (USER_DATA)
- `GET /fapi/v1/openOrders` — Current All Open Orders (USER_DATA)
- `POST /fapi/v1/stock/contract` — Futures TradFi Perps Contract (USER_DATA)
- `GET /fapi/v1/orderAmendment` — Get Order Modify History (USER_DATA)
- `GET /fapi/v1/positionMargin/history` — Get Position Margin Change History (TRADE)
- `POST /fapi/v1/positionMargin` — Modify Isolated Position Margin (TRADE)
- `GET /fapi/v1/adlQuantile` — Position ADL Quantile Estimation (USER_DATA)
- `GET /fapi/v2/positionRisk` — Position Information V2 (USER_DATA)
- `GET /fapi/v3/positionRisk` — Position Information V3 (USER_DATA)
- `GET /fapi/v1/allAlgoOrders` — Query All Algo Orders (USER_DATA)
- `GET /fapi/v1/openOrder` — Query Current Open Order (USER_DATA)
- `POST /fapi/v1/order/test` — Test Order (TRADE)
- `GET /fapi/v1/forceOrders` — User's Force Orders (USER_DATA)
- `POST /fapi/v1/listenKey` — Start User Data Stream (USER_STREAM)
- `PUT /fapi/v1/listenKey` — Keepalive User Data Stream (USER_STREAM)
- `DELETE /fapi/v1/listenKey` — Close User Data Stream (USER_STREAM)

## Account Information V2 (USER_DATA)（账户信息V2 (USER_DATA)）

`GET /fapi/v2/account`

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

Operation ID: `accountInformationV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Information V2 / 账户 信息 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeTier | integer (int64) |  | Account commission tier.<br>手续费等级。<br>例: `0` |
| feeBurn | boolean |  | Whether fee discount is enabled.<br>是否开启手续费抵扣。<br>例: `True` |
| canTrade | boolean |  | Whether trading is enabled.<br>是否可以交易。<br>例: `True` |
| canDeposit | boolean |  | Whether transfer-in is enabled.<br>是否可以入金。<br>例: `True` |
| canWithdraw | boolean |  | Whether transfer-out is enabled.<br>是否可以出金。<br>例: `True` |
| updateTime | integer (int64) |  | Reserved field, ignore.<br>保留字段，可忽略。<br>例: `0` |
| multiAssetsMargin | boolean |  | Whether multi-assets mode is enabled.<br>是否开启多资产模式。<br>例: `True` |
| tradeGroupId | integer (int64) |  | Trade group identifier.<br>交易组 ID。<br>例: `-1` |
| totalInitialMargin | string |  | Total initial margin requirement. USDT only in single-asset mode; the sum of USD value of all cross positions/open order initial margin in multi-assets mode.<br>起始保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓/挂单起始保证金的美元价值总和。<br>例: `0.00000000` |
| totalMaintMargin | string |  | Total maintenance margin requirement. USDT only in single-asset mode; the sum of USD value of all cross positions maintenance margin in multi-assets mode.<br>维持保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓维持保证金的美元价值总和。<br>例: `0.00000000` |
| totalWalletBalance | string |  | Total wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>账户总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalUnrealizedProfit | string |  | Total unrealized profit. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| totalMarginBalance | string |  | Total margin balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>保证金总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalPositionInitialMargin | string |  | Initial margin required for positions. USDT only in single-asset mode; the sum of USD value of all cross positions initial margin in multi-assets mode.<br>持仓所需起始保证金。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓起始保证金的美元价值总和。<br>例: `0.00000000` |
| totalOpenOrderInitialMargin | string |  | Initial margin required for open orders. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>当前挂单所需起始保证金。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| totalCrossWalletBalance | string |  | Cross wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>全仓账户余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalCrossUnPnl | string |  | Unrealized PnL for cross positions. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>全仓持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| availableBalance | string |  | Available balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>可用余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount. USDT only in single-asset mode; a maximum virtual USD amount in multi-assets mode.<br>最大可转出余额。单资产模式下仅计 USDT；多资产模式下为可转出的最大虚拟美元金额。<br>例: `126.72469206` |
| assets | object[] |  | Asset-level account details.<br>资产维度账户信息。 |
| assets[].asset | string |  | Asset name.<br>资产名称。<br>例: `USDT` |
| assets[].walletBalance | string |  | Wallet balance.<br>钱包余额。<br>例: `23.72469206` |
| assets[].unrealizedProfit | string |  | Unrealized profit.<br>未实现盈亏。<br>例: `0.00000000` |
| assets[].marginBalance | string |  | Margin balance.<br>保证金余额。<br>例: `23.72469206` |
| assets[].maintMargin | string |  | Maintenance margin requirement.<br>维持保证金。<br>例: `0.00000000` |
| assets[].initialMargin | string |  | Total initial margin requirement.<br>所需起始保证金。<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | Initial margin required for positions.<br>持仓所需起始保证金。<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | Initial margin required for open orders.<br>当前挂单所需起始保证金。<br>例: `0.00000000` |
| assets[].crossWalletBalance | string |  | Cross wallet balance.<br>全仓账户余额。<br>例: `23.72469206` |
| assets[].crossUnPnl | string |  | Unrealized PnL for cross positions.<br>全仓持仓未实现盈亏。<br>例: `0.00000000` |
| assets[].availableBalance | string |  | Available balance.<br>可用余额。<br>例: `126.72469206` |
| assets[].maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount.<br>最大可转出余额。<br>例: `23.72469206` |
| assets[].marginAvailable | boolean |  | Whether the asset can be used as margin in multi-assets mode.<br>在多资产模式下，该资产是否可作为保证金。<br>例: `True` |
| assets[].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `1625474304765` |
| positions | object[] |  | Position details for symbols. One-way mode returns BOTH; hedge mode returns LONG/SHORT.<br>各交易对持仓信息。单向模式返回 BOTH，双向模式返回 LONG/SHORT。 |
| positions[].symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| positions[].initialMargin | string |  | Initial margin requirement.<br>所需起始保证金。<br>例: `0` |
| positions[].maintMargin | string |  | Maintenance margin requirement.<br>维持保证金。<br>例: `0` |
| positions[].unrealizedProfit | string |  | Unrealized profit.<br>持仓未实现盈亏。<br>例: `0.00000000` |
| positions[].positionInitialMargin | string |  | Initial margin required for positions.<br>持仓所需起始保证金。<br>例: `0` |
| positions[].openOrderInitialMargin | string |  | Initial margin required for open orders.<br>当前挂单所需起始保证金。<br>例: `0` |
| positions[].leverage | string |  | Current initial leverage.<br>当前杠杆倍数。<br>例: `100` |
| positions[].isolated | boolean |  | Whether the position uses isolated margin mode.<br>是否为逐仓模式。<br>例: `True` |
| positions[].entryPrice | string |  | Average entry price.<br>持仓成本价。<br>例: `0.00000` |
| positions[].maxNotional | string |  | Maximum available notional under current leverage.<br>当前杠杆下可用最大名义价值。<br>例: `250000` |
| positions[].bidNotional | string |  | Bid notional (ignore).<br>买单名义价值（可忽略）。<br>例: `0` |
| positions[].askNotional | string |  | Ask notional (ignore).<br>卖单名义价值（可忽略）。<br>例: `0` |
| positions[].positionSide | string |  | Position side.<br>持仓方向。<br>例: `BOTH` |
| positions[].positionAmt | string |  | Position quantity.<br>持仓数量。<br>例: `0` |
| positions[].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `0` |

## Account Information V3 (USER_DATA)（账户信息V3 (USER_DATA)）

`GET /fapi/v3/account`

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

Operation ID: `accountInformationV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Information V3 / 账户 信息 V3

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalInitialMargin | string |  | Total initial margin requirement. USDT only in single-asset mode; the sum of USD value of all cross positions/open order initial margin in multi-assets mode.<br>起始保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓/挂单起始保证金的美元价值总和。<br>例: `0.00000000` |
| totalMaintMargin | string |  | Total maintenance margin requirement. USDT only in single-asset mode; the sum of USD value of all cross positions maintenance margin in multi-assets mode.<br>维持保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓维持保证金的美元价值总和。<br>例: `0.00000000` |
| totalWalletBalance | string |  | Total wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>账户总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalUnrealizedProfit | string |  | Total unrealized profit. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| totalMarginBalance | string |  | Total margin balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>保证金总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalPositionInitialMargin | string |  | Initial margin required for positions. USDT only in single-asset mode; the sum of USD value of all cross positions initial margin in multi-assets mode.<br>持仓所需起始保证金。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓起始保证金的美元价值总和。<br>例: `0.00000000` |
| totalOpenOrderInitialMargin | string |  | Initial margin required for open orders. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>当前挂单所需起始保证金。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| totalCrossWalletBalance | string |  | Cross wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>全仓账户余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| totalCrossUnPnl | string |  | Unrealized PnL for cross positions. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>全仓持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `0.00000000` |
| availableBalance | string |  | Available balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.<br>可用余额。单资产模式下仅计 USDT；多资产模式下以美元计价。<br>例: `126.72469206` |
| maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount. USDT only in single-asset mode; a maximum virtual USD amount in multi-assets mode.<br>最大可转出余额。单资产模式下仅计 USDT；多资产模式下为可转出的最大虚拟美元金额。<br>例: `126.72469206` |
| assets | object[] |  | Asset-level account details.<br>资产维度账户信息。 |
| assets[].asset | string |  | Asset name.<br>资产名称。<br>例: `USDT` |
| assets[].walletBalance | string |  | Wallet balance.<br>钱包余额。<br>例: `23.72469206` |
| assets[].unrealizedProfit | string |  | Unrealized profit.<br>未实现盈亏。<br>例: `0.00000000` |
| assets[].marginBalance | string |  | Margin balance.<br>保证金余额。<br>例: `23.72469206` |
| assets[].maintMargin | string |  | Maintenance margin requirement.<br>维持保证金。<br>例: `0.00000000` |
| assets[].initialMargin | string |  | Total initial margin requirement.<br>所需起始保证金。<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | Initial margin required for positions.<br>持仓所需起始保证金。<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | Initial margin required for open orders.<br>当前挂单所需起始保证金。<br>例: `0.00000000` |
| assets[].crossWalletBalance | string |  | Cross wallet balance.<br>全仓账户余额。<br>例: `23.72469206` |
| assets[].crossUnPnl | string |  | Unrealized PnL for cross positions.<br>全仓持仓未实现盈亏。<br>例: `0.00000000` |
| assets[].availableBalance | string |  | Available balance.<br>可用余额。<br>例: `23.72469206` |
| assets[].maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount.<br>最大可转出余额。<br>例: `23.72469206` |
| assets[].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `1625474304765` |
| positions | object[] |  | Position details for symbols.<br>各交易对持仓信息。 |
| positions[].symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| positions[].positionSide | string |  | Position side.<br>持仓方向。<br>例: `BOTH` |
| positions[].positionAmt | string |  | Position quantity.<br>持仓数量。<br>例: `1.000` |
| positions[].unrealizedProfit | string |  | Unrealized profit.<br>持仓未实现盈亏。<br>例: `0.00000000` |
| positions[].isolatedMargin | string |  | Isolated margin.<br>逐仓保证金。<br>例: `0.00000000` |
| positions[].notional | string |  | Position notional value.<br>持仓名义价值。<br>例: `0` |
| positions[].isolatedWallet | string |  | Isolated wallet balance.<br>逐仓钱包余额。<br>例: `0` |
| positions[].initialMargin | string |  | Initial margin requirement.<br>所需起始保证金。<br>例: `0` |
| positions[].maintMargin | string |  | Maintenance margin requirement.<br>维持保证金。<br>例: `0` |
| positions[].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `0` |

## Futures Account Balance V2 (USER_DATA)（账户余额V2 (USER_DATA)）

`GET /fapi/v2/balance`

Query account balance information.

查询账户余额信息。

Operation ID: `futuresAccountBalanceV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Account Balance V2 / 合约 账户 Balance V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].accountAlias | string |  | Unique account alias.<br>唯一账户别名。<br>例: `SgsR` |
| [].asset | string |  | Asset name.<br>资产名称。<br>例: `USDT` |
| [].balance | string |  | Wallet balance.<br>钱包余额。<br>例: `122607.35137903` |
| [].crossWalletBalance | string |  | Cross wallet balance.<br>全仓钱包余额。<br>例: `23.72469206` |
| [].crossUnPnl | string |  | Unrealized PnL of cross positions.<br>全仓持仓未实现盈亏。<br>例: `0.00000000` |
| [].availableBalance | string |  | Available balance.<br>可用余额。<br>例: `23.72469206` |
| [].maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount.<br>最大可转出余额。<br>例: `23.72469206` |
| [].marginAvailable | boolean |  | Whether the asset can be used as margin in multi-assets mode.<br>在多资产模式下，该资产是否可作为保证金。<br>例: `True` |
| [].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `1617939110373` |

## Futures Account Balance V3 (USER_DATA)（账户余额V3 (USER_DATA)）

`GET /fapi/v3/balance`

Query account balance information.

查询账户余额信息。

Operation ID: `futuresAccountBalanceV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Account Balance V3 / 合约 账户 Balance V3

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].accountAlias | string |  | Unique account alias.<br>唯一账户别名。<br>例: `SgsR` |
| [].asset | string |  | Asset name.<br>资产名称。<br>例: `USDT` |
| [].balance | string |  | Wallet balance.<br>钱包余额。<br>例: `122607.35137903` |
| [].crossWalletBalance | string |  | Cross wallet balance.<br>全仓钱包余额。<br>例: `23.72469206` |
| [].crossUnPnl | string |  | Unrealized PnL of cross positions.<br>全仓持仓未实现盈亏。<br>例: `0.00000000` |
| [].availableBalance | string |  | Available balance.<br>可用余额。<br>例: `23.72469206` |
| [].maxWithdrawAmount | string |  | Maximum transferable/withdrawable amount.<br>最大可转出余额。<br>例: `23.72469206` |
| [].marginAvailable | boolean |  | Whether the asset can be used as margin in multi-assets mode.<br>在多资产模式下，该资产是否可作为保证金。<br>例: `True` |
| [].updateTime | integer (int64) |  | Last update time in milliseconds.<br>最后更新时间（毫秒）。<br>例: `1617939110373` |

## Futures Account Configuration (USER_DATA)（账户配置 (USER_DATA)）

`GET /fapi/v1/accountConfig`

Query account configuration

查询账户 configuration

Operation ID: `futuresAccountConfiguration`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Account Configuration / 合约 账户 Configuration

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeTier | integer (int64) |  | account commission tier<br>费率等级<br>例: `0` |
| canTrade | boolean |  | if can trade<br>是否可以交易<br>例: `True` |
| canDeposit | boolean |  | if can transfer in asset<br>是否可以存款<br>例: `True` |
| canWithdraw | boolean |  | if can transfer out asset<br>是否可以提现<br>例: `True` |
| dualSidePosition | boolean |  | 例: `True` |
| updateTime | integer (int64) |  | reserved property, please ignore<br>忽略<br>例: `0` |
| multiAssetsMargin | boolean |  | 例: `False` |
| tradeGroupId | integer (int64) |  | 例: `-1` |

## Futures Trading Quantitative Rules Indicators (USER_DATA)（合约交易量化规则指标 (USER_DATA)）

`GET /fapi/v1/apiTradingStatus`

Futures trading quantitative rules indicators, for more information on this, please refer to the [Futures Trading Quantitative Rules](https://www.binance.com/en/support/faq/4f462ebe6ff445d4a170be7d9e897272)

合约交易量化规则指标，更多细节, 请参考[合约交易量化规则](https://www.binance.com/cn/support/faq/4f462ebe6ff445d4a170be7d9e897272)

权重: - **1** for a single symbol
- **10** when the symbol parameter is omitted

Operation ID: `futuresTradingQuantitativeRulesIndicators`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures Trading Quantitative Rules Indicators / 合约 Trading Quantitative Rules Indicators

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| indicators | object |  | indicator: quantitative rules indicators, value: user's indicators value, triggerValue: trigger indicator value threshold of quantitative rules.<br>indicator:风控指标名, value:用户在该市场的风控指标数值, triggerValue:阈值, 对于没有达到记录阈值的则不返回数据。 |
| indicators.BTCUSDT | object[] |  |  |
| indicators.BTCUSDT[].isLocked | boolean |  | Is Locked.<br>用户该品种交易是否被风控禁用<br>例: `True` |
| indicators.BTCUSDT[].plannedRecoverTime | integer (int64) |  | Planned Recover Time.<br>预计恢复时间，若当前时间大等于预计恢复时间则为空<br>例: `1545741270000` |
| indicators.BTCUSDT[].indicator | string |  | Too many violations under multiple symbols trigger account violation<br>Too many violations 多交易对触发账号层级违规<br>例: `UFR` |
| indicators.BTCUSDT[].value | number (float) |  | Current value<br>例: `0.05` |
| indicators.BTCUSDT[].triggerValue | number (float) |  | Trigger value<br>例: `0.995` |
| indicators.ETHUSDT | object[] |  |  |
| indicators.ETHUSDT[].isLocked | boolean |  | Is Locked.<br>用户该品种交易是否被风控禁用<br>例: `True` |
| indicators.ETHUSDT[].plannedRecoverTime | integer (int64) |  | Planned Recover Time.<br>预计恢复时间，若当前时间大等于预计恢复时间则为空<br>例: `1545741270000` |
| indicators.ETHUSDT[].indicator | string |  | Too many violations under multiple symbols trigger account violation<br>Too many violations 多交易对触发账号层级违规<br>例: `UFR` |
| indicators.ETHUSDT[].value | number (float) |  | Current value<br>例: `0.05` |
| indicators.ETHUSDT[].triggerValue | number (float) |  | Trigger value<br>例: `0.995` |
| indicators.ACCOUNT | object[] |  |  |
| indicators.ACCOUNT[].indicator | string |  | Too many violations under multiple symbols trigger account violation<br>Too many violations 多交易对触发账号层级违规<br>例: `TMV` |
| indicators.ACCOUNT[].value | integer (int64) |  | Current value<br>例: `10` |
| indicators.ACCOUNT[].triggerValue | integer (int64) |  | Trigger value<br>例: `1` |
| indicators.ACCOUNT[].plannedRecoverTime | integer (int64) |  | Planned Recover Time.<br>预计恢复时间，若当前时间大等于预计恢复时间则为空<br>例: `1644919865000` |
| indicators.ACCOUNT[].isLocked | boolean |  | Is Locked.<br>用户该品种交易是否被风控禁用<br>例: `True` |
| updateTime | integer (int64) |  | Update Time.<br>返回值的更新时间<br>例: `1644913304748` |

## Get BNB Burn Status (USER_DATA)（获取BNB抵扣开关状态 (USER_DATA)）

`GET /fapi/v1/feeBurn`

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

查询用户 ***所有 symbol*** 合约交易BNB抵扣开关状态(手续费抵扣开或关)

Operation ID: `getBnbBurnStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get BNB Burn Status / 获取BNB Burn 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeBurn | boolean |  | "true": Fee Discount On; "false": Fee Discount Off<br>"true": 手续费抵扣开; "false": 手续费抵扣关<br>例: `True` |

## Toggle BNB Burn On Futures Trade (TRADE)（合约交易BNB抵扣开关 (TRADE)）

`POST /fapi/v1/feeBurn`

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***

改变用户 ***所有 symbol*** 合约交易BNB抵扣开关(手续费抵扣开或关)

Operation ID: `toggleBnbBurnOnFuturesTrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeBurn | string | 是 | "true": Fee Discount On; "false": Fee Discount Off<br>"true": 手续费抵扣开; "false": 手续费抵扣关<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Toggle BNB Burn On Futures Trade / Toggle BNB Burn On 合约 交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## Get Current Multi-Assets Mode (USER_DATA)（查询联合保证金模式 (USER_DATA)）

`GET /fapi/v1/multiAssetsMargin`

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***

查询用户目前在 ***所有symbol*** 合约上的联合保证金模式。

Operation ID: `getCurrentMultiAssetsMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Current Multi-Assets Mode / 获取当前 Multi-Assets Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| multiAssetsMargin | boolean |  | "true": Multi-Assets Mode; "false": Single-Asset Mode<br>"true": 联合保证金模式开启；"false": 联合保证金模式关闭<br>例: `True` |

## Change Multi-Assets Mode (TRADE)（更改联合保证金模式 (TRADE)）

`POST /fapi/v1/multiAssetsMargin`

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***

变换用户在 ***所有symbol*** 合约上的联合保证金模式：开启或关闭联合保证金模式。

Operation ID: `changeMultiAssetsMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| multiAssetsMargin | string | 是 | "true": Multi-Assets Mode; "false": Single-Asset Mode<br>"true": 联合保证金模式开启；"false": 联合保证金模式关闭<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Multi-Assets Mode / 修改Multi-Assets Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## Get Current Position Mode (USER_DATA)（查询持仓模式 (USER_DATA)）

`GET /fapi/v1/positionSide/dual`

Get user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***

查询用户目前在 ***所有symbol*** 合约上的持仓模式：双向持仓或单向持仓。

Operation ID: `getCurrentPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Current Position Mode / 获取当前 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | boolean |  | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>例: `True` |

## Change Position Mode (TRADE)（更改持仓模式 (TRADE)）

`POST /fapi/v1/positionSide/dual`

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
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Position Mode / 修改持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## Get Download Id For Futures Order History (USER_DATA)（获取合约订单历史下载Id (USER_DATA)）

`GET /fapi/v1/order/asyn`

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
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Order History / 获取Download ID 用于 合约 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download Id.<br>下载Id<br>例: `546975389218332672` |

## Get Download Id For Futures Trade History (USER_DATA)（获取合约交易历史下载Id (USER_DATA)）

`GET /fapi/v1/trade/asyn`

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
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Trade History / 获取Download ID 用于 合约 交易 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download Id.<br>下载Id<br>例: `546975389218332672` |

## Get Download Id For Futures Transaction History (USER_DATA)（获取合约资金流水下载Id (USER_DATA)）

`GET /fapi/v1/income/asyn`

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
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For Futures Transaction History / 获取Download ID 用于 合约 Transaction 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download Id.<br>下载Id<br>例: `546975389218332672` |

## Get Futures Order History Download Link by Id (USER_DATA)（通过下载Id获取合约订单下载链接 (USER_DATA)）

`GET /fapi/v1/order/asyn/id`

Get futures order history download link by Id

通过下载Id获取合约订单下载链接

Operation ID: `getFuturesOrderHistoryDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Order History Download Link by Id / 获取合约 订单 历史 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download Id.<br>下载Id<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | 例: `null` |

## Get Futures Trade Download Link by Id (USER_DATA)（通过下载Id获取合约交易历史下载链接 (USER_DATA)）

`GET /fapi/v1/trade/asyn/id`

Get futures trade download link by Id

通过下载Id获取合约交易历史下载链接

Operation ID: `getFuturesTradeDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Trade Download Link by Id / 获取合约 交易 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download Id.<br>下载Id<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `www.binance.com` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `1645009771000` |
| isExpired | string |  | 例: `null` |

## Get Futures Transaction History Download Link by Id (USER_DATA)（通过下载Id获取合约资金流水下载链接 (USER_DATA)）

`GET /fapi/v1/income/asyn/id`

Get futures transaction history download link by Id

过下载Id获取合约资金流水下载链接

Operation ID: `getFuturesTransactionHistoryDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Futures Transaction History Download Link by Id / 获取合约 Transaction 历史 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download Id.<br>下载Id<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `www.binance.com` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `1645009771000` |
| isExpired | string |  | 例: `null` |

## Get Income History (USER_DATA)（获取账户损益资金流水 (USER_DATA)）

`GET /fapi/v1/income`

Query income history

获取账户损益资金流水

Operation ID: `getIncomeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Trading symbol.<br>交易对。<br>例: `BTCUSDT` |
| incomeType | query | string |  | Income type.<br>收益类型。<br>枚举: `TRANSFER`, `WELCOME_BONUS`, `REALIZED_PNL`, `FUNDING_FEE`, `COMMISSION`, `INSURANCE_CLEAR`, `REFERRAL_KICKBACK`, `COMMISSION_REBATE`, `API_REBATE`, `CONTEST_REWARD`, `CROSS_COLLATERAL_TRANSFER`, `OPTIONS_PREMIUM_FEE`, `OPTIONS_SETTLE_PROFIT`, `INTERNAL_TRANSFER`, `AUTO_EXCHANGE`, `DELIVERED_SETTELMENT`, `COIN_SWAP_DEPOSIT`, `COIN_SWAP_WITHDRAW`, `POSITION_LIMIT_INCREASE_FEE`, `STRATEGY_UMFUTURES_TRANSFER`, `FEE_RETURN`, `BFUSD_REWARD`, `SPECIAL_FUNDING_FEE`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Timestamp in milliseconds (inclusive start).<br>起始时间戳（毫秒，包含）。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in milliseconds (inclusive end).<br>结束时间戳（毫秒，包含）。<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Maximum number of records to return.<br>返回记录数量上限。<br>默认: `100`<br>例: `30` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Income History / 获取Income 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | trade symbol, if existing<br>交易对，仅针对涉及交易对的资金流<br>例: `` |
| [].incomeType | string |  | income type<br>资金流类型<br>例: `TRANSFER` |
| [].income | string |  | income amount<br>资金流数量，正数代表流入，负数代表流出<br>例: `-0.37500000` |
| [].asset | string |  | income asset<br>资产内容<br>例: `USDT` |
| [].info | string |  | extra information<br>备注信息，取决于流水类型<br>例: `TRANSFER` |
| [].time | integer (int64) |  | Time.<br>时间<br>例: `1570608000000` |
| [].tranId | integer (int64) |  | transaction id<br>划转ID<br>例: `9689322392` |
| [].tradeId | string |  | trade id, if existing<br>引起流水产生的原始交易ID<br>例: `` |

## Notional and Leverage Brackets (USER_DATA)（杠杆分层标准 (USER_DATA)）

`GET /fapi/v1/leverageBracket`

Query user notional and leverage bracket on speicfic symbol

查询账户特定交易对的杠杆分层标准

Operation ID: `notionalAndLeverageBrackets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `ETHUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Notional and Leverage Brackets / Notional 和 Leverage Brackets

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 2).symbol | string |  | 例: `ETHUSDT` |
| (oneOf 2).notionalCoef | number (float) |  | user symbol bracket multiplier, only appears when user's symbol bracket is adjusted<br>用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示<br>例: `1.5` |
| (oneOf 2).brackets | object[] |  |  |
| (oneOf 2).brackets[].bracket | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| (oneOf 2).brackets[].initialLeverage | integer (int64) |  | Max initial leverage for this bracket<br>该层允许的最高初始杠杆倍数<br>例: `75` |
| (oneOf 2).brackets[].notionalCap | integer (int64) |  | Cap notional of this bracket<br>该层对应的名义价值上限<br>例: `10000` |
| (oneOf 2).brackets[].notionalFloor | integer (int64) |  | Notional threshold of this bracket<br>该层对应的名义价值下限<br>例: `0` |
| (oneOf 2).brackets[].maintMarginRatio | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.0065` |
| (oneOf 2).brackets[].cum | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `0` |

## Query User Rate Limit (USER_DATA)（查询用户下单限频 (USER_DATA)）

`GET /fapi/v1/rateLimit/order`

Query User Rate Limit

查询用户下单限频

Operation ID: `queryUserRateLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Rate Limit / 用户 频率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].rateLimitType | string |  | 例: `ORDERS` |
| [].interval | string |  | 例: `SECOND` |
| [].intervalNum | integer (int64) |  | 例: `10` |
| [].limit | integer (int64) |  | 例: `10000` |

## Symbol Configuration (USER_DATA)（交易对配置 (USER_DATA)）

`GET /fapi/v1/symbolConfig`

Get current account symbol configuration.

查询交易对上的基础配置

Operation ID: `symbolConfiguration`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Symbol Configuration / 交易对 Configuration

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].marginType | string |  | 例: `CROSSED` |
| [].isAutoAddMargin | boolean |  | 例: `False` |
| [].leverage | integer (int64) |  | 例: `21` |
| [].maxNotionalValue | string |  | 例: `1000000` |

## User Commission Rate (USER_DATA)（用户手续费率 (USER_DATA)）

`GET /fapi/v1/commissionRate`

Get User Commission Rate

查询用户手续费率

Operation ID: `userCommissionRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Commission Rate / 用户 手续费 利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `BTCUSDT` |
| makerCommissionRate | string |  | 0.02%<br>例: `0.0002` |
| takerCommissionRate | string |  | 0.04%<br>例: `0.0004` |
| rpiCommissionRate | string |  | 0.005%<br>例: `0.00005` |

## Accept the offered quote (USER_DATA)（接受报价 (USER_DATA)）

`POST /fapi/v1/convert/acceptQuote`

Accept the offered quote by quote ID.

通过 quote ID 来接受报价。

Operation ID: `acceptTheOfferedQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| quoteId | string | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Accept the offered quote

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `933256278426274426` |
| createTime | integer (int64) |  | 例: `1623381330472` |
| orderStatus | string |  | PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL<br>例: `PROCESS` |

## List All Convert Pairs（查询可交易币对信息）

`GET /fapi/v1/convert/exchangeInfo`

Query for all convertible token pairs and the tokens’ respective upper/lower limits

查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。

Operation ID: `listAllConvertPairs`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromAsset | query | string |  | User spends coin<br>用户售出币种<br>例: `BTC` |
| toAsset | query | string |  | User receives coin<br>用户买入币种<br>例: `USDT` |

### 响应 200：List All Convert Pairs / 列表All Convert Pairs

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].fromAsset | string |  | 例: `BTC` |
| [].toAsset | string |  | 例: `USDT` |
| [].fromAssetMinAmount | string |  | 例: `0.0004` |
| [].fromAssetMaxAmount | string |  | 例: `50` |
| [].toAssetMinAmount | string |  | 例: `20` |
| [].toAssetMaxAmount | string |  | 例: `2500000` |

## Order status (USER_DATA)（查询订单状态 (USER_DATA)）

`GET /fapi/v1/convert/orderStatus`

Query order status by order ID.

通过 order ID 来查询订单状态。

Operation ID: `orderStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string |  | Either orderId or quoteId is required<br>orderId 和quoteId需要填其中一个<br>例: `933256278426274400` |
| quoteId | query | string |  | Either orderId or quoteId is required<br>orderId 和quoteId需要填其中一个<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order status / 订单 状态

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

## Send Quote Request (USER_DATA)（发送获取报价请求 (USER_DATA)）

`POST /fapi/v1/convert/getQuote`

Request a quote for the requested token pairs

对所需的币对发送获取报价请求

权重: 50(IP)
360/hour, 500/day

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
| fromAmount | number (float) |  | When specified, it is the amount you will be debited after the conversion<br>这是成交后将被扣除的金额<br>例: `1.0` |
| toAmount | number (float) |  | When specified, it is the amount you will be credited after the conversion<br>这是成交后将会获得的金额<br>例: `1.0` |
| validTime | string |  | 10s, default 10s<br>可以支持10s，默认值为10s<br>例: `10s` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Send Quote Request / Send Quote 请求

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| quoteId | string |  | 例: `12415572564` |
| ratio | string |  | 例: `38163.7` |
| inverseRatio | string |  | 例: `0.0000262` |
| validTimestamp | integer (int64) |  | 例: `1623319461670` |
| toAmount | string |  | 例: `3816.37` |
| fromAmount | string |  | 例: `0.1` |

## ADL Risk（自动减仓风险评级）

`GET /fapi/v1/symbolAdlRisk`

Query the symbol-level ADL risk rating.

The ADL risk rating measures the likelihood of ADL during liquidation,
and the rating takes into account the insurance fund balance, position
concentration on the symbol, order book depth, price volatility, average
leverage, unrealized PnL, and margin utilization at the symbol level.

The rating can be high, medium and low, and is updated every 30 minutes.

查询symbol级别的 ADL 风险评级。

ADL 风险评级用于衡量在发生强平时触发 ADL
的可能性，该评级会综合考虑该symbol的保险基金余额、仓位集中度、盘口深度、价格波动率、平均杠杆水平、未实现盈亏以及保证金利用率。

风险等级分为高、中、低，每半小时更新一次。

Operation ID: `adlRisk`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |

### 响应 200：ADL Risk / 请参见英文说明：ADL Risk

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).adlRisk | string |  | ADL Risk rating<br>自动减仓风险评级<br>例: `low` |
| (oneOf 1).updateTime | integer (int64) |  | 例: `1597370495002` |

## Basis（基差）

`GET /futures/data/basis`

Query future basis

查询期货基差

Operation ID: `basis`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | 例: `BTCUSDT` |
| contractType | query | string | 是 | 枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`<br>例: `PERPETUAL` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `30` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Basis / 请参见英文说明：Basis

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].indexPrice | string |  | 例: `34400.15945055` |
| [].contractType | string |  | 例: `PERPETUAL` |
| [].basisRate | string |  | 例: `0.0004` |
| [].futuresPrice | string |  | 例: `34414.10` |
| [].annualizedBasisRate | string |  | 例: `` |
| [].basis | string |  | 例: `13.94054945` |
| [].pair | string |  | 例: `BTCUSDT` |
| [].timestamp | integer (int64) |  | Start time of the period, in milliseconds.<br>该周期的开始时间，单位为毫秒。<br>例: `1698742800000` |

## Check Server Time（获取服务器时间）

`GET /fapi/v1/time`

Test connectivity to the Rest API and get the current server time.

获取服务器时间

Operation ID: `checkServerTime`

### 响应 200：Check Server Time / 检查Server 时间

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serverTime | integer (int64) |  | Server Time.<br>当前的系统时间<br>例: `1499827319559` |

## Composite Index Symbol Information（综合指数交易对信息）

`GET /fapi/v1/indexInfo`

Query composite index symbol information

获取交易对为综合指数的基础成分信息。

Operation ID: `compositeIndexSymbolInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `DEFIUSDT` |

### 响应 200：Composite Index Symbol Information / Composite Index 交易对 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `DEFIUSDT` |
| [].time | integer (int64) |  | Current time<br>请求时间<br>例: `1589437530011` |
| [].component | string |  | Component asset<br>成分资产<br>例: `baseAsset` |
| [].baseAssetList | object[] |  |  |
| [].baseAssetList[].baseAsset | string |  | Base Asset.<br>基础资产<br>例: `BAL` |
| [].baseAssetList[].quoteAsset | string |  | Quote Asset.<br>报价资产<br>例: `USDT` |
| [].baseAssetList[].weightInQuantity | string |  | Weight In Quantity.<br>权重(数量)<br>例: `1.04406228` |
| [].baseAssetList[].weightInPercentage | string |  | Weight In Percentage.<br>权重(比例)<br>例: `0.02783900` |

## Compressed/Aggregate Trades List（近期成交）

`GET /fapi/v1/aggTrades`

Get compressed, aggregate market trades. Market trades that fill in
100ms with the same price and the same taking side will have the
quantity aggregated.

Retail Price Improvement(RPI) orders are aggregated and without special
tags to be distinguished.

获取归集/压缩的市场成交记录。100ms内价格和买卖方向相同的成交会被归集成一条记录。

零点价差改善订单（RPI订单）会被归集，并且没有特殊标签区分。

Operation ID: `compressedAggregateTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| fromId | query | integer (int64) |  | ID to get aggregate trades from INCLUSIVE.<br>从包含fromID的成交开始返回结果<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades from INCLUSIVE.<br>从该时刻之后的成交记录开始返回结果<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get aggregate trades until INCLUSIVE.<br>返回该时刻为止的成交记录<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Compressed/Aggregate Trades List / Compressed/Aggregate 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].a | integer (int64) |  | Aggregate tradeId<br>归集成交ID<br>例: `26129` |
| [].p | string |  | Price<br>成交价<br>例: `0.01633102` |
| [].q | string |  | Quantity<br>成交量<br>例: `4.70443515` |
| [].nq | string |  | Normal quantity without the trades involving RPI orders<br>普通订单成交量，不包含RPI订单数据<br>例: `100` |
| [].f | integer (int64) |  | First tradeId<br>被归集的首个成交ID<br>例: `27781` |
| [].l | integer (int64) |  | Last tradeId<br>被归集的末个成交ID<br>例: `27781` |
| [].T | integer (int64) |  | Timestamp<br>成交时间<br>例: `1498793709153` |
| [].m | boolean |  | Was the buyer the maker?<br>是否为主动卖出单<br>例: `True` |

## Continuous Contract Kline/Candlestick Data（连续合约K线数据）

`GET /fapi/v1/continuousKlines`

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

获取特定合约类型的K线数据。K线由开盘时间唯一标识。

权重: based on parameter `LIMIT`

| LIMIT       | weight |
| ----------- | ------ |
| [1,100)     | 1      |
| [100, 500)  | 2      |
| [500, 1000] | 5      |
| > 1000      | 10     |

Operation ID: `continuousContractKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | After CM migration, accepts both UM and CM pair values.<br>标的交易对 迁移后支持传入 UM 与 CM 的 pair。<br>例: `BTCUSDT` |
| contractType | query | string | 是 | Futurestype<br>合约类型<br>枚举: `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`, `TRADIFI_PERPETUAL`<br>例: `PERPETUAL` |
| interval | query | string | 是 | 枚举: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Continuous Contract Kline/Candlestick Data / Continuous Contract K线/Candlestick Data

## Exchange Information（获取交易规则和交易对）

`GET /fapi/v1/exchangeInfo`

Current exchange trading rules and symbol information

获取交易规则和交易对

Operation ID: `exchangeInformation`

### 响应 200：Exchange Information / Exchange 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| exchangeFilters | string[] |  |  |
| rateLimits | object[] |  | Rate Limits.<br>API访问的限制 |
| rateLimits[].interval | string |  | Interval.<br>按照分钟计算<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Interval Num.<br>按照1分钟计算<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Limit.<br>上限次数<br>例: `2400` |
| rateLimits[].rateLimitType | string |  | Rate Limit Type.<br>按照访问权重来计算<br>例: `REQUEST_WEIGHT` |
| serverTime | integer (int64) |  | Ignore please. If you want to check current server time, please check via "GET /fapi/v1/time"<br>请忽略。如果需要获取当前系统时间，请查询接口 “GET /fapi/v1/time”<br>例: `1565613908500` |
| assets | object[] |  | assets information<br>资产信息 |
| assets[].asset | string |  | 例: `BTC` |
| assets[].marginAvailable | boolean |  | whether the asset can be used as margin in Multi-Assets mode<br>是否可用作保证金<br>例: `True` |
| assets[].autoAssetExchange | string |  | auto-exchange threshold in Multi-Assets margin mode<br>保证金资产自动兑换阈值<br>例: `-0.10` |
| symbols | object[] |  | Symbols.<br>交易对信息 |
| symbols[].symbol | string |  | Symbol.<br>交易对<br>例: `BLZUSDT` |
| symbols[].pair | string |  | Pair.<br>标的交易对<br>例: `BLZUSDT` |
| symbols[].contractType | string |  | Contract Type.<br>合约类型<br>例: `PERPETUAL` |
| symbols[].deliveryDate | integer (int64) |  | Delivery Date.<br>交割日期<br>例: `4133404800000` |
| symbols[].onboardDate | integer (int64) |  | Onboard Date.<br>上线日期<br>例: `1598252400000` |
| symbols[].status | string |  | Status.<br>交易对状态<br>例: `TRADING` |
| symbols[].maintMarginPercent | string |  | ignore<br>请忽略<br>例: `2.5000` |
| symbols[].requiredMarginPercent | string |  | ignore<br>请忽略<br>例: `5.0000` |
| symbols[].baseAsset | string |  | Base Asset.<br>标的资产<br>例: `BLZ` |
| symbols[].quoteAsset | string |  | Quote Asset.<br>报价资产<br>例: `USDT` |
| symbols[].marginAsset | string |  | Margin Asset.<br>保证金资产<br>例: `USDT` |
| symbols[].pricePrecision | integer (int64) |  | please do not use it as tickSize<br>价格小数点位数(仅作为系统精度使用，注意同tickSize 区分）<br>例: `5` |
| symbols[].quantityPrecision | integer (int64) |  | please do not use it as stepSize<br>数量小数点位数(仅作为系统精度使用，注意同stepSize 区分）<br>例: `0` |
| symbols[].baseAssetPrecision | integer (int64) |  | Base Asset Precision.<br>标的资产精度<br>例: `8` |
| symbols[].quotePrecision | integer (int64) |  | Quote Precision.<br>报价资产精度<br>例: `8` |
| symbols[].underlyingType | string |  | 例: `COIN` |
| symbols[].underlyingSubType | string[] |  |  |
| symbols[].settlePlan | integer (int64) |  | 例: `0` |
| symbols[].triggerProtect | string |  | threshold for algo order with "priceProtect"<br>开启"priceProtect"的条件订单的触发阈值<br>例: `0.15` |
| symbols[].filters | object[] |  |  |
| symbols[].filters[].filterType | string |  | Filter Type.<br>市价订单数量限制<br>例: `PRICE_FILTER` |
| symbols[].filters[].maxPrice | string |  | Max Price.<br>价格上限, 最大价格<br>例: `300` |
| symbols[].filters[].minPrice | string |  | Min Price.<br>价格下限, 最小价格<br>例: `0.0001` |
| symbols[].filters[].tickSize | string |  | Tick Size.<br>订单最小价格间隔<br>例: `0.0001` |
| symbols[].filters[].maxQty | string |  | Max Qty.<br>数量上限, 最大数量<br>例: `10000000` |
| symbols[].filters[].minQty | string |  | Min Qty.<br>数量下限, 最小数量<br>例: `1` |
| symbols[].filters[].stepSize | string |  | Step Size.<br>订单最小数量间隔<br>例: `1` |
| symbols[].filters[].limit | integer (int64) |  | Limit.<br>上限次数<br>例: `200` |
| symbols[].filters[].notional | string |  | 例: `5.0` |
| symbols[].filters[].multiplierUp | string |  | Multiplier Up.<br>价格上限百分比<br>例: `1.1500` |
| symbols[].filters[].multiplierDown | string |  | Multiplier Down.<br>价格下限百分比<br>例: `0.8500` |
| symbols[].filters[].multiplierDecimal | string |  | 例: `4` |
| symbols[].orderTypes | string[] |  |  |
| symbols[].timeInForce | string[] |  | Time In Force.<br>有效方式 |
| symbols[].liquidationFee | string |  | liquidation fee rate<br>强平费率<br>例: `0.010000` |
| symbols[].marketTakeBound | string |  | the max price difference rate( from mark price) a market order can make<br>市价吃单(相对于标记价格)允许可造成的最大价格偏离比例<br>例: `0.30` |
| timezone | string |  | Timezone.<br>服务器所用的时间区域<br>例: `UTC` |

## Get Funding Rate History（查询资金费率历史）

`GET /fapi/v1/fundingRate`

Get Funding Rate History

查询资金费率历史

权重: When `limit` ≤ 200: share 500/5min/IP rate limit with `GET /fapi/v1/fundingInfo`

When `limit` > 200: 100/5min/IP rate limit

Operation ID: `getFundingRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding rate from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding rate until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `100`<br>例: `50` |

### 响应 200：Get Funding Rate History / 获取Funding 利率 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].fundingRate | string |  | Funding Rate.<br>资金费率<br>例: `-0.03750000` |
| [].fundingTime | integer (int64) |  | Funding Time.<br>资金费时间<br>例: `1570608000000` |
| [].markPrice | string |  | mark price associated with a particular funding fee charge<br>资金费对应标记价格<br>例: `34287.54619963` |
| [].rateType | string |  | Funding rate type. `Regular` for the normal funding rate; `Special` for the additional funding rate generated by stock dividends.<br>资金费率类型。`Regular` 为正常资金费率；`Special` 为股票分红产生的额外资金费率。<br>枚举: `Regular`, `Special`<br>例: `Regular` |

## Get Funding Rate Info（查询资金费率信息）

`GET /fapi/v1/fundingInfo`

Query funding rate info for symbols that had FundingRateCap/FundingRateFloor / fundingIntervalHours adjustment

查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours等被特殊调整过的交易对，没调整过的不返回。

权重: **0**

share 500/5min/IP rate limit with `GET /fapi/v1/fundingRate`

Operation ID: `getFundingRateInfo`

### 响应 200：Get Funding Rate Info / 获取Funding 利率 Info

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BLZUSDT` |
| [].adjustedFundingRateCap | string |  | 例: `0.02500000` |
| [].adjustedFundingRateFloor | string |  | 例: `-0.02500000` |
| [].fundingIntervalHours | integer (int64) |  | 例: `8` |
| [].disclaimer | boolean |  | ingore<br>例: `False` |

## Index Price Kline/Candlestick Data（价格指数K线数据）

`GET /fapi/v1/indexPriceKlines`

Kline/candlestick bars for the index price of a pair.
Klines are uniquely identified by their open time.

价格指数K线数据，每根K线的开盘时间可视为唯一ID

权重: based on parameter `LIMIT`

| LIMIT       | weight |
| ----------- | ------ |
| [1,100)     | 1      |
| [100, 500)  | 2      |
| [500, 1000] | 5      |
| > 1000      | 10     |

Operation ID: `indexPriceKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | After CM migration, accepts both UM and CM pair values.<br>标的交易对 迁移后支持传入 UM 与 CM 的 pair。<br>例: `BTCUSDT` |
| interval | query | string | 是 | 枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Index Price Kline/Candlestick Data / Index 价格 K线/Candlestick Data

## Kline/Candlestick Data（K线数据）

`GET /fapi/v1/klines`

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

每根K线的开盘时间可视为唯一ID

权重: based on parameter `LIMIT`

| LIMIT       | weight |
| ----------- | ------ |
| [1,100)     | 1      |
| [100, 500)  | 2      |
| [500, 1000] | 5      |
| > 1000      | 10     |

Operation ID: `klineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | After CM migration, accepts both UM and CM symbols.<br>交易对 迁移后支持传入 UM 与 CM 的 symbol。<br>例: `BTCUSDT` |
| interval | query | string | 是 | 枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Kline/Candlestick Data / K线/Candlestick Data

## Long/Short Ratio（多空持仓人数比）

`GET /futures/data/globalLongShortAccountRatio`

Query symbol Long/Short Ratio

多空持仓人数比

Operation ID: `longShortRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `50` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Long/Short Ratio / 请参见英文说明：Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | long/short account num ratio of all traders<br>例: `BTCUSDT` |
| [].longShortRatio | string |  | long account num ratio of all traders<br>多空人数比值<br>例: `0.1960` |
| [].longAccount | string |  | short account num ratio of all traders<br>多仓人数比例<br>例: `0.6622` |
| [].shortAccount | string |  | Short Account.<br>空仓人数比例<br>例: `0.3378` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Mark Price（最新标记价格和资金费率）

`GET /fapi/v1/premiumIndex`

Mark Price and Funding Rate

采集各大交易所数据加权平均

权重: **1** with symbol, **10** without symbol

Operation ID: `markPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |

### 响应 200：Mark Price / Mark 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| (oneOf 1).markPrice | string |  | mark price<br>标记价格<br>例: `11793.63104562` |
| (oneOf 1).indexPrice | string |  | index price<br>指数价格<br>例: `11781.80495970` |
| (oneOf 1).estimatedSettlePrice | string |  | Estimated Settle Price, only useful in the last hour before the settlement starts.<br>预估结算价,仅在交割开始前最后一小时有意义<br>例: `11781.16138815` |
| (oneOf 1).lastFundingRate | string |  | This is the Latest funding rate<br>最近更新的资金费率<br>例: `0.00038246` |
| (oneOf 1).interestRate | string |  | Interest Rate.<br>标的资产基础利率<br>例: `0.00010000` |
| (oneOf 1).nextFundingTime | integer (int64) |  | Next Funding Time.<br>下次资金费时间<br>例: `1597392000000` |
| (oneOf 1).time | integer (int64) |  | Time.<br>更新时间<br>例: `1597370495002` |

## Mark Price Kline/Candlestick Data（标记价格K线数据）

`GET /fapi/v1/markPriceKlines`

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

每根K线的开盘时间可视为唯一ID

权重: based on parameter `LIMIT`

| LIMIT       | weight |
| ----------- | ------ |
| [1,100)     | 1      |
| [100, 500)  | 2      |
| [500, 1000] | 5      |
| > 1000      | 10     |

Operation ID: `markPriceKlineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | After CM migration, accepts both UM and CM symbols.<br>交易对 迁移后支持传入 UM 与 CM 的 symbol。<br>例: `BTCUSDT` |
| interval | query | string | 是 | 枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Mark Price Kline/Candlestick Data / Mark 价格 K线/Candlestick Data

## Multi-Assets Mode Asset Index（多资产模式资产汇率指数）

`GET /fapi/v1/assetIndex`

Asset index price.

> **CM-UM Integration (Effective 2026-06-30):** Renamed from *Multi-Assets Mode Asset Index*. The response now additionally pushes COIN-M settlement-asset price index entries (e.g., `BTCUSD`, `ETHUSD`, `BNBUSD`). The endpoint path `/fapi/v1/assetIndex` is unchanged.

资产汇率指数。

> **币本位/U本位整合迁移(2026-06-30 生效):** 接口名由 *多资产模式资产汇率指数* 变更为 *资产汇率指数*。响应中**额外推送**币本位结算资产的价格指数(如 `BTCUSD`、`ETHUSD`、`BNBUSD`)。HTTP 路径 `/fapi/v1/assetIndex` 保持不变。

权重: **1** for a single symbol; **10** when the symbol parameter is omitted

Operation ID: `assetIndex`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Asset pair<br>资产 pair<br>例: `ADAUSD` |

### 响应 200：Multi-Assets Mode Asset Index / Multi-Assets Mode 资产 Index

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `ADAUSD` |
| (oneOf 1).time | integer (int64) |  | 例: `1635740268004` |
| (oneOf 1).index | string |  | 例: `1.92957370` |
| (oneOf 1).bidBuffer | string |  | 例: `0.10000000` |
| (oneOf 1).askBuffer | string |  | 例: `0.10000000` |
| (oneOf 1).bidRate | string |  | 例: `1.73661633` |
| (oneOf 1).askRate | string |  | 例: `2.12253107` |
| (oneOf 1).autoExchangeBidBuffer | string |  | 例: `0.05000000` |
| (oneOf 1).autoExchangeAskBuffer | string |  | 例: `0.05000000` |
| (oneOf 1).autoExchangeBidRate | string |  | 例: `1.83309501` |
| (oneOf 1).autoExchangeAskRate | string |  | 例: `2.02605238` |

## Old Trades Lookup (MARKET_DATA)（查询历史成交 (MARKET_DATA)）

`GET /fapi/v1/historicalTrades`

Get older market historical trades.

查询订单簿历史成交

Operation ID: `oldTradesLookup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| limit | query | integer (int64) |  | 默认: `100`<br>例: `50` |
| fromId | query | integer (int64) |  | TradeId to fetch from. Default gets most recent trades.<br>从该 TradeId 开始获取数据，默认获取最近的成交数据<br>例: `1` |

### 响应 200：Old Trades Lookup / Old 交易s Lookup

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | Id.<br>成交ID<br>例: `28457` |
| [].price | string |  | Price.<br>成交价格<br>例: `4.00000100` |
| [].qty | string |  | Qty.<br>成交量<br>例: `12.00000000` |
| [].quoteQty | string |  | Quote Qty.<br>成交额<br>例: `8000.00` |
| [].time | integer (int64) |  | Time.<br>时间<br>例: `1499865549590` |
| [].isBuyerMaker | boolean |  | Is Buyer Maker.<br>买方是否为挂单方<br>例: `True` |
| [].isRPITrade | boolean |  | Is RPITrade.<br>Maker方是否为RPI挂单<br>例: `True` |

## Open Interest（获取未平仓合约数）

`GET /fapi/v1/openInterest`

Get present open interest of a specific symbol.

获取未平仓合约数

Operation ID: `openInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |

### 响应 200：Open Interest / 未完成利息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| openInterest | string |  | Open Interest.<br>未平仓合约数量<br>例: `10659.509` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| time | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589437530011` |

## Open Interest Statistics（合约持仓量历史）

`GET /futures/data/openInterestHist`

Open Interest Statistics

查询合约持仓量历史

Operation ID: `openInterestStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `50` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Open Interest Statistics / 未完成利息 Statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].sumOpenInterest | string |  | total open interest<br>持仓总数量<br>例: `20403.12345678` |
| [].sumOpenInterestValue | string |  | total open interest value<br>持仓总价值<br>例: `176196512.12345678` |
| [].CMCCirculatingSupply | string |  | circulating supply provided by CMC<br>CMC提供的流通供应量<br>例: `165880.538` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Order Book（深度信息）

`GET /fapi/v1/depth`

Query symbol orderbook

Retail Price Improvement(RPI) orders are not visible and excluded in the
response message.

查询交易对订单 Book

零售价格改进（RPI）订单不可见，并且在响应消息中被排除。

权重: Adjusted based on the limit:

| Limit         | Weight |
| ------------- | ------ |
| 5, 10, 20, 50 | 2      |
| 100           | 5      |
| 500           | 10     |
| 1000          | 20     |

Operation ID: `orderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| limit | query | integer (int64) |  | Valid limits:[5, 10, 20, 50, 100, 500, 1000]<br>可选值:[5, 10, 20, 50, 100, 500, 1000]<br>默认: `500`<br>例: `50` |

### 响应 200：Order Book / 订单 Book

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| lastUpdateId | integer (int64) |  | 例: `1027024` |
| E | integer (int64) |  | Message output time<br>消息时间<br>例: `1589436922972` |
| T | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589436922959` |
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |

## Premium index Kline Data（溢价指数K线数据）

`GET /fapi/v1/premiumIndexKlines`

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

获取某个交易对的溢价指数K线数据。K线由开盘时间唯一标识。

权重: based on parameter `LIMIT`

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
| symbol | query | string | 是 | After CM migration, accepts both UM and CM symbols.<br>交易对。迁移后支持传入 UM 与 CM 的 symbol。<br>例: `BTCUSDT` |
| interval | query | string | 是 | 枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Premium index Kline Data / Premium index K线 Data

## Quarterly Contract Settlement Price（季度合约历史结算价）

`GET /futures/data/delivery-price`

Latest price for a symbol or symbols.

返回季度合约历史结算价

Operation ID: `quarterlyContractSettlementPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pair | query | string | 是 | 例: `BTCUSDT` |

### 响应 200：Quarterly Contract Settlement Price / Quarterly Contract Settlement 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].deliveryTime | integer (int64) |  | 例: `1695945600000` |
| [].deliveryPrice | number (float) |  | 例: `27103` |

## Query Index Price Constituents（查询指数价格成分）

`GET /fapi/v1/constituents`

Query index price constituents

**Note**:
Prices from constituents of TradFi perps will be hiden and displayed as -1.

查询指数价格成分

**注意：** 传统金融合约的成分价格将被隐藏，并统一显示为 -1。

Operation ID: `queryIndexPriceConstituents`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |

### 响应 200：Index Price Constituents / Index 价格 Constituents

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `BTCUSDT` |
| time | integer (int64) |  | 例: `1745401553408` |
| constituents | object[] |  |  |
| constituents[].exchange | string |  | 例: `binance` |
| constituents[].symbol | string |  | 例: `BTCUSDT` |
| constituents[].price | string |  | 例: `94057.03000000` |
| constituents[].weight | string |  | 例: `0.51282051` |

## Query Insurance Fund Balance Snapshot（查询保险基金余额快照）

`GET /fapi/v1/insuranceBalance`

Query Insurance Fund Balance Snapshot

查询保险基金余额快照

Operation ID: `queryInsuranceFundBalanceSnapshot`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol<br>交易对<br>例: `BNBUSDT` |

### 响应 200：Insurance Fund Balance Snapshot / 请参见英文说明：Insurance Fund Balance Snapshot

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbols | string[] |  |  |
| (oneOf 1).assets | object[] |  |  |
| (oneOf 1).assets[].asset | string |  | 例: `USDC` |
| (oneOf 1).assets[].marginBalance | string |  | 例: `299999998.6497832` |
| (oneOf 1).assets[].updateTime | integer (int64) |  | 例: `1745366402000` |

## Recent Trades List（近期成交）

`GET /fapi/v1/trades`

Get recent market trades

获取近期订单簿成交

Operation ID: `recentTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |

### 响应 200：Recent Trades List / Recent 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | Id.<br>成交ID<br>例: `28457` |
| [].price | string |  | Price.<br>成交价格<br>例: `4.00000100` |
| [].qty | string |  | Qty.<br>成交量<br>例: `12.00000000` |
| [].quoteQty | string |  | Quote Qty.<br>成交额<br>例: `48.00` |
| [].time | integer (int64) |  | Time.<br>时间<br>例: `1499865549590` |
| [].isBuyerMaker | boolean |  | Is Buyer Maker.<br>买方是否为挂单方<br>例: `True` |
| [].isRPITrade | boolean |  | Is RPITrade.<br>Maker方是否为RPI挂单<br>例: `True` |

## RPI Order Book（RPI深度信息）

`GET /fapi/v1/rpiDepth`

Query symbol orderbook with RPI orders

RPI(Retail Price Improvement) orders are included and aggreated in the
response message. Crossed price levels are hidden and invisible.

交易对深度信息，包含非交叉的RPI订单

权重: Adjusted based on the limit:

| Limit         | Weight |
| ------------- | ------ |
| 1000          | 20     |

Operation ID: `rpiOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| limit | query | integer (int64) |  | Valid limits:[1000]<br>可选值:[1000]<br>默认: `1000`<br>例: `1000` |

### 响应 200：RPI Order Book / RPI 订单 Book

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| lastUpdateId | integer (int64) |  | 例: `1027024` |
| E | integer (int64) |  | Message output time<br>消息时间<br>例: `1589436922972` |
| T | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589436922959` |
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |

## Symbol Order Book Ticker（当前最优挂单）

`GET /fapi/v1/ticker/bookTicker`

Best price/qty on the order book for a symbol or symbols.

Retail Price Improvement(RPI) orders are not visible and excluded in the
response message.

返回当前最优的挂单(最高买单，最低卖单)

权重: **2** for a single symbol;
**5** when the symbol parameter is omitted

Operation ID: `symbolOrderBookTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |

### 响应 200：Symbol Order Book Ticker / 交易对 订单 最优挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| (oneOf 1).bidPrice | string |  | Bid Price.<br>最优买单价<br>例: `4.00000000` |
| (oneOf 1).bidQty | string |  | Bid Qty.<br>挂单量<br>例: `431.00000000` |
| (oneOf 1).askPrice | string |  | Ask Price.<br>最优卖单价<br>例: `4.00000200` |
| (oneOf 1).askQty | string |  | Ask Qty.<br>挂单量<br>例: `9.00000000` |
| (oneOf 1).time | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589437530011` |

## Symbol Price Ticker（最新价格）

`GET /fapi/v1/ticker/price`

Latest price for a symbol or symbols.

返回最近价格

权重: 1 for a single symbol;
2 when the symbol parameter is omitted

Operation ID: `symbolPriceTicker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |

### 响应 200：Symbol Price Ticker / 交易对 价格 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| (oneOf 1).price | string |  | Price.<br>价格<br>例: `6000.01` |
| (oneOf 1).time | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589437530011` |

## Symbol Price Ticker V2（最新价格V2）

`GET /fapi/v2/ticker/price`

Latest price for a symbol or symbols.

返回最近价格

权重: 1 for a single symbol;
2 when the symbol parameter is omitted

Operation ID: `symbolPriceTickerV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |

### 响应 200：Symbol Price Ticker V2 / 交易对 价格 行情 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| (oneOf 1).price | string |  | Price.<br>价格<br>例: `6000.01` |
| (oneOf 1).time | integer (int64) |  | Transaction time<br>撮合引擎时间<br>例: `1589437530011` |

## Taker Buy/Sell Volume（合约主动买卖量）

`GET /futures/data/takerlongshortRatio`

Taker Buy/Sell Volume

合约主动买卖量

Operation ID: `takerBuySellVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 例: `BTCUSDT` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `50` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Taker Buy/Sell Volume

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].buySellRatio | string |  | 例: `1.5586` |
| [].buyVol | string |  | 例: `387.3300` |
| [].sellVol | string |  | 例: `248.5030` |
| [].timestamp | integer (int64) |  | Start time of the period, in milliseconds.<br>该周期的开始时间，单位为毫秒。<br>例: `1591261042378` |

## Test Connectivity（测试服务器连通性 PING）

`GET /fapi/v1/ping`

Test connectivity to the Rest API.

测试能否联通

Operation ID: `testConnectivity`

### 响应 200：OK / 成功

## 24hr Ticker Price Change Statistics（24hr价格变动情况）

`GET /fapi/v1/ticker/24hr`

24 hour rolling window price change statistics.
**Careful** when accessing this with no symbol.

请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高

权重: **1** for a single symbol;
**40** when the symbol parameter is omitted

Operation ID: `ticker24hrPriceChangeStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 例: `BTCUSDT` |

### 响应 200：24hr Ticker Price Change Statistics / 24hr 行情 价格 修改Statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).priceChange | string |  | Price Change.<br>24小时价格变动<br>例: `-94.99999800` |
| (oneOf 1).priceChangePercent | string |  | Price Change Percent.<br>24小时价格变动百分比<br>例: `-95.960` |
| (oneOf 1).weightedAvgPrice | string |  | Weighted Avg Price.<br>加权平均价<br>例: `0.29628482` |
| (oneOf 1).lastPrice | string |  | Last Price.<br>最近一次成交价<br>例: `4.00000200` |
| (oneOf 1).lastQty | string |  | Last Qty.<br>最近一次成交额<br>例: `200.00000000` |
| (oneOf 1).openPrice | string |  | Open Price.<br>24小时内第一次成交的价格<br>例: `99.00000000` |
| (oneOf 1).highPrice | string |  | High Price.<br>24小时最高价<br>例: `100.00000000` |
| (oneOf 1).lowPrice | string |  | Low Price.<br>24小时最低价<br>例: `0.10000000` |
| (oneOf 1).volume | string |  | Volume.<br>24小时成交量<br>例: `8913.30000000` |
| (oneOf 1).quoteVolume | string |  | Quote Volume.<br>24小时成交额<br>例: `15.30000000` |
| (oneOf 1).openTime | integer (int64) |  | Open Time.<br>24小时内，第一笔交易的发生时间<br>例: `1499783499040` |
| (oneOf 1).closeTime | integer (int64) |  | Close Time.<br>24小时内，最后一笔交易的发生时间<br>例: `1499869899040` |
| (oneOf 1).firstId | integer (int64) |  | First tradeId<br>首笔成交id<br>例: `28385` |
| (oneOf 1).lastId | integer (int64) |  | Last tradeId<br>末笔成交id<br>例: `28460` |
| (oneOf 1).count | integer (int64) |  | Trade count<br>成交笔数<br>例: `76` |

## Top Trader Long/Short Account Ratio (MARKET_DATA)（大户账户数多空比 (MARKET_DATA)）

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
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `50` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Top Trader Long/Short Ratio / Top 交易r Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].longShortRatio | string |  | long/short account num ratio of top traders<br>大户多空账户数比值<br>例: `1.8105` |
| [].longAccount | string |  | long account num ratio of top traders<br>大户多仓账户数比例<br>例: `0.6442` |
| [].shortAccount | string |  | long account num ratio of top traders<br>大户空仓账户数比例<br>例: `0.3558` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Top Trader Long/Short Position Ratio (MARKET_DATA)（大户持仓量多空比 (MARKET_DATA)）

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
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| period | query | string | 是 | 枚举: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`<br>例: `5m` |
| limit | query | integer (int64) |  | 默认: `30`<br>例: `50` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |

### 响应 200：Top Trader Long/Short Ratio / Top 交易r Long/Short Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `BTCUSDT` |
| [].longShortRatio | string |  | long/short position ratio of top traders<br>大户多空持仓量比值<br>例: `1.4342` |
| [].longAccount | string |  | long positions ratio of top traders<br>大户多仓持仓量比例<br>例: `0.5344` |
| [].shortAccount | string |  | short positions ratio of top traders<br>大户空仓持仓量比例<br>例: `0.4238` |
| [].timestamp | integer (int64) |  | End time of the period, in milliseconds.<br>该周期的结束时间，单位为毫秒。<br>例: `1591261042378` |

## Trading Schedule（交易时段）

`GET /fapi/v1/tradingSchedule`

Trading session schedules for the underlying assets of TradFi Perps are provided for a one-week period forward and one-week period backward starting from the day prior to the query time, covering the U.S. equity market, Korean equity market, Hong Kong equity market, China equity market, the commodity market, and the FX market.

Session types per market:
- U.S. equity market: "PRE_MARKET", "REGULAR", "AFTER_MARKET", "OVERNIGHT", "NO_TRADING".
- Commodity market: "REGULAR", "NO_TRADING".
- Korean equity market: "REGULAR", "NO_TRADING".
- Hong Kong equity market: "REGULAR", "NO_TRADING".
- China equity market: "REGULAR", "NO_TRADING".
- FX market: "REGULAR", "NO_TRADING".

从查询时间的前一日起算、返回往后为期一周以及往前为期一周的传统金融合约标的资产的交易时段信息，覆盖美国股票市场，韩国股票市场，香港股票市场，中国股票市场，商品市场和外汇市场。

各市场时段类型：
- 美股市场："PRE_MARKET"、"REGULAR"、"AFTER_MARKET"、"OVERNIGHT"、"NO_TRADING"。
- 商品市场："REGULAR"、"NO_TRADING"。
- 韩国股票市场："REGULAR"、"NO_TRADING"。
- 香港股票市场："REGULAR"、"NO_TRADING"。
- 中国股票市场："REGULAR"、"NO_TRADING"。
- 外汇市场："REGULAR"、"NO_TRADING"。

Operation ID: `tradingSchedule`

### 响应 200：Trading Schedule / 请参见英文说明：Trading Schedule

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| updateTime | integer (int64) |  | 例: `1761286643918` |
| marketSchedules | object |  |  |
| marketSchedules.EQUITY | object |  |  |
| marketSchedules.EQUITY.sessions | object[] |  |  |
| marketSchedules.EQUITY.sessions[].startTime | integer (int64) |  | 例: `1761177600000` |
| marketSchedules.EQUITY.sessions[].endTime | integer (int64) |  | 例: `1761206400000` |
| marketSchedules.EQUITY.sessions[].type | string |  | 例: `OVERNIGHT` |
| marketSchedules.COMMODITY | object |  |  |
| marketSchedules.COMMODITY.sessions | object[] |  |  |
| marketSchedules.COMMODITY.sessions[].startTime | integer (int64) |  | 例: `1761724800000` |
| marketSchedules.COMMODITY.sessions[].endTime | integer (int64) |  | 例: `1761744600000` |
| marketSchedules.COMMODITY.sessions[].type | string |  | 例: `NO_TRADING` |
| marketSchedules.KR_EQUITY | object |  |  |
| marketSchedules.KR_EQUITY.sessions | object[] |  |  |
| marketSchedules.KR_EQUITY.sessions[].startTime | integer (int64) |  | 例: `1779958800000` |
| marketSchedules.KR_EQUITY.sessions[].endTime | integer (int64) |  | 例: `1780009200000` |
| marketSchedules.KR_EQUITY.sessions[].type | string |  | 例: `NO_TRADING` |
| marketSchedules.HK_EQUITY | object |  |  |
| marketSchedules.HK_EQUITY.sessions | object[] |  |  |
| marketSchedules.HK_EQUITY.sessions[].startTime | integer (int64) |  | 例: `1779955200000` |
| marketSchedules.HK_EQUITY.sessions[].endTime | integer (int64) |  | 例: `1780018200000` |
| marketSchedules.HK_EQUITY.sessions[].type | string |  | 例: `NO_TRADING` |
| marketSchedules.CN_EQUITY | object |  |  |
| marketSchedules.CN_EQUITY.sessions | object[] |  |  |
| marketSchedules.CN_EQUITY.sessions[].startTime | integer (int64) |  | 例: `1779955200000` |
| marketSchedules.CN_EQUITY.sessions[].endTime | integer (int64) |  | 例: `1780018200000` |
| marketSchedules.CN_EQUITY.sessions[].type | string |  | 例: `NO_TRADING` |
| marketSchedules.FX | object |  |  |
| marketSchedules.FX.sessions | object[] |  |  |
| marketSchedules.FX.sessions[].startTime | integer (int64) |  | 例: `1779966000000` |
| marketSchedules.FX.sessions[].endTime | integer (int64) |  | 例: `1780027200000` |
| marketSchedules.FX.sessions[].type | string |  | 例: `NO_TRADING` |

## Classic Portfolio Margin Account Information (USER_DATA)（Classic Portfolio 杠杆 账户 信息 (USER_DATA)）

`GET /fapi/v1/pmAccountInfo`

Get Classic Portfolio Margin current account information.

查询经典统一账户当前账户信息

Operation ID: `classicPortfolioMarginAccountInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `BTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Classic Portfolio Margin Account Information / Classic Portfolio 杠杆 账户 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| maxWithdrawAmountUSD | string |  | Classic Portfolio margin maximum virtual amount for transfer out in USD<br>Classic Portfolio 杠杆账户最大可转出金额，单位为美元<br>例: `1627523.32459208` |
| asset | string |  | asset name<br>资产<br>例: `BTC` |
| maxWithdrawAmount | string |  | maximum amount for transfer out<br>最大可转出余额<br>例: `27.43689636` |

## Account Trade List (USER_DATA)（账户成交历史 (USER_DATA)）

`GET /fapi/v1/userTrades`

Get trades for a specific account and symbol.

获取某交易对的成交历史

Operation ID: `accountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | Must be used together with parameter `symbol`.<br>必须要和参数`symbol`一起使用<br>例: `25851813` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| fromId | query | integer (int64) |  | Trade id to fetch from. Default gets most recent trades.<br>从该交易ID开始获取数据. 默认获取最近的交易数据.<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Trade List / 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].buyer | boolean |  | Buyer.<br>是否是买方<br>例: `False` |
| [].commission | string |  | Commission.<br>手续费<br>例: `0.07819010` |
| [].commissionAsset | string |  | Commission Asset.<br>手续费计价单位<br>例: `USDT` |
| [].id | integer (int64) |  | Id.<br>交易ID<br>例: `698759` |
| [].maker | boolean |  | Maker.<br>是否是挂单方<br>例: `False` |
| [].orderId | integer (int64) |  | Order Id.<br>订单编号<br>例: `25851813` |
| [].price | string |  | Price.<br>成交价<br>例: `7819.01` |
| [].qty | string |  | Qty.<br>成交量<br>例: `0.002` |
| [].quoteQty | string |  | Quote asset quantity. Populated for USDⓈ-M symbols; returns "0" for COIN-M symbols.<br>计价资产成交额。U 本位合约交易对返回该值；币本位合约交易对返回 "0"。<br>例: `15.63802` |
| [].baseQty | string |  | Base asset quantity. Populated for COIN-M symbols; returns "0" for USDⓈ-M symbols.<br>标的资产成交量。币本位合约交易对返回该值；U 本位合约交易对返回 "0"。<br>例: `0` |
| [].marginAsset | string |  | Margin Asset.<br>保证金币种<br>例: `USDT` |
| [].realizedPnl | string |  | Realized Pnl.<br>实现盈亏<br>例: `-0.91539999` |
| [].side | string |  | Side.<br>买卖方向<br>例: `SELL` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].pair | string |  | Pair.<br>标的交易对<br>例: `BTCUSDT` |
| [].time | integer (int64) |  | Time.<br>时间<br>例: `1569514978020` |

## All Orders (USER_DATA)（查询所有订单(包括历史订单) (USER_DATA)）

`GET /fapi/v1/allOrders`

Get all account orders; active, canceled, or filled.

- These orders will not be found:
  - order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  - order create time + 90 days < current time

查询所有订单(包括历史订单)

- 请注意，如果订单满足如下条件，不会被查询到：
  - 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  - 订单创建时间 + 90天 < 当前时间

Operation ID: `allOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1917641` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Orders / All 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>平均成交价<br>例: `0.00000` |
| [].clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `abc` |
| [].cumQuote | string |  | Cum Quote.<br>成交金额<br>例: `0` |
| [].cumBase | string |  | Cum Base.<br>成交金额(标的数量)<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| [].orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].price | string |  | Price.<br>委托价格<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>是否仅减仓<br>例: `False` |
| [].side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].pair | string |  | Pair.<br>标的交易对<br>例: `BTCUSDT` |
| [].time | integer (int64) |  | order time<br>订单时间<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| [].type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| [].workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |

## Auto-Cancel All Open Orders (TRADE)（倒计时撤销所有订单 (TRADE)）

`POST /fapi/v1/countdownCancelAll`

Cancel all open orders of the specified symbol at the end of the specified countdown.

The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and
replaced by a new one.

Example usage:

Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically
canceled.
If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.

The system will check all countdowns **approximately every 10 milliseconds**, so please note that sufficient
redundancy should be considered when using this function. We do not recommend setting the countdown time to be
too precise or too small.

* 该接口可以被用于确保在倒计时结束时撤销指定symbol上的所有挂单。 在使用这个功能时，接口应像心跳一样在倒计时内被反复调用，以便可以取消既有的倒计时并开始新的倒数计时设置。

* 用法示例：
以30s的间隔重复此接口，每次倒计时countdownTime设置为120000(120s)。
如果在120秒内未再次调用此接口，则您指定symbol上的所有挂单都会被自动撤销。
如果在120秒内以将countdownTime设置为0，则倒数计时器将终止，自动撤单功能取消。

* 系统会**大约每10毫秒**检查一次所有倒计时情况，因此请注意，使用此功能时应考虑足够的冗余。
我们不建议将倒记时设置得太精确或太小。

Operation ID: `autoCancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| countdownTime | integer (int64) | 是 | Countdown in milliseconds. `1000` means 1 second; `0` disables countdown cancel-all.<br>倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。<br>例: `1000` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Auto-Cancel All Open Orders / Auto-取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 例: `BTCUSDT` |
| countdownTime | string |  | 例: `100000` |

## Query Algo Order (USER_DATA)（查询条件订单 (USER_DATA)）

`GET /fapi/v1/algoOrder`

Check the status of an algo (conditional) order, such as TP/SL (Take Profit / Stop Loss) or trailing stop orders on USD-M Futures.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询条件订单（Algo / Conditional Order）的状态，包括 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

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
| symbol | string |  | 例: `BNBUSDT` |
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

`POST /fapi/v1/algoOrder`

Send in a new algo (conditional) order. Use this endpoint to place **TP/SL (Take Profit / Stop Loss)** and trailing stop orders on USD-M Futures. Supported order types under `algoType=CONDITIONAL` are `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `STOP`, `TAKE_PROFIT`, and `TRAILING_STOP_MARKET`.

下新的条件单（Algo / Conditional Order），用于 U 本位合约的**止盈止损（TP/SL, Take Profit / Stop Loss）**和追踪止损（Trailing Stop）。在 `algoType=CONDITIONAL` 下，支持的订单类型为 `STOP_MARKET`、`TAKE_PROFIT_MARKET`、`STOP`、`TAKE_PROFIT`、`TRAILING_STOP_MARKET`。

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
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>例: `BOTH` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `STOP_MARKET` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`, `RPI`<br>例: `GTC` |
| quantity | number (float) |  | Cannot be sent with `closePosition`=`true`(Close-All)<br>下单数量,使用`closePosition`不支持此参数。<br>例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| triggerPrice | number (float) |  | Trigger price<br>触发价<br>例: `1.0` |
| workingType | string |  | 枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单类型可用；不能与 `price` 参数同时使用<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| closePosition | string |  | Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用"<br>枚举: `true`, `false`<br>例: `true` |
| priceProtect | string |  | Used with `STOP_MARKET` or `TAKE_PROFIT_MARKET` order. when price reaches the triggerPrice ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price Protection Threshold of the symbol.'<br>仅 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET` 订单类型可用。当价格达到触发价时，标记价格与合约最新价之间的价差不能超过该symbol的触发保护阈值。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`'<br>双开模式下不接受此参数； 使用`closePosition`不支持此参数。"<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| activatePrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`)<br>追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)<br>例: `1.0` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders<br>追踪止损回调比例，可取值范围[0.1, 20],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数<br>例: `1` |
| clientAlgoId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的条件订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers / `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`<br>订单自成交保护模式，默认 `NONE`。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `NONE`<br>例: `EXPIRE_TAKER` |
| goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000<br>TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Algo Order / New Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `2146760` |
| clientAlgoId | string |  | 例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| algoType | string |  | 例: `CONDITIONAL` |
| orderType | string |  | 例: `TAKE_PROFIT` |
| symbol | string |  | 例: `BNBUSDT` |
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

`DELETE /fapi/v1/algoOrder`

Cancel an active algo (conditional) order, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on USD-M Futures.

撤销当前有效的条件单（Algo / Conditional Order），覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

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

`DELETE /fapi/v1/algoOpenOrders`

Cancel all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on USD-M Futures.

撤销某个交易对下的全部条件挂单（Algo / Conditional Order），覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

Operation ID: `cancelAllAlgoOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All Algo Open Orders / 取消All Algo 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `The operation of cancel all open order is done.` |

## Cancel All Open Orders (TRADE)（撤销全部订单 (TRADE)）

`DELETE /fapi/v1/allOpenOrders`

Cancel All Open Orders

撤销全部订单 (TRADE)

Operation ID: `cancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All Open Orders / 取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `The operation of cancel all open order is done.` |

## Place Multiple Orders (TRADE)（批量下单 (TRADE)）

`POST /fapi/v1/batchOrders`

Place Multiple Orders

批量下单

权重: 5 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
5 on IP rate limit(x-mbx-used-weight-1m);

Operation ID: `placeMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchOrders | object[] | 是 | order list. Max 5 orders<br>订单列表，最多支持5个订单 |
| batchOrders[].symbol | string |  | 例: `BTCUSDT` |
| batchOrders[].side | string |  | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| batchOrders[].positionSide | string |  | Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode.<br>持仓方向，单向持仓模式默认 `BOTH`；双向持仓模式可选 `LONG` 或 `SHORT`。<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| batchOrders[].type | string |  | 枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| batchOrders[].timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`, `RPI`<br>例: `GTC` |
| batchOrders[].quantity | number (float) |  | 例: `0.001` |
| batchOrders[].reduceOnly | string |  | 枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| batchOrders[].price | number (float) |  | 例: `10001` |
| batchOrders[].newClientOrderId | string |  | 例: `1` |
| batchOrders[].newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| batchOrders[].priceMatch | string |  | only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price<br>盘口价格下单模式，不能与 `price` 同时传入。<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| batchOrders[].selfTradePreventionMode | string |  | EXPIRE_TAKER: expire taker order when STP triggers/ EXPIRE_MAKER: expire taker order when STP triggers/ EXPIRE_BOTH: expire both orders when STP triggers; default NONE<br>订单自成交保护模式，默认 `NONE`。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>例: `NONE` |
| batchOrders[].goodTillDate | integer (int64) |  | Auto-cancel time for `GTD` orders.<br>`GTD` 订单的自动取消时间。<br>例: `1693207680000` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Place Multiple Orders / 下单Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `testOrder` |
| [].cumQty | string |  | 例: `0` |
| [].executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| [].orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `22542179` |
| [].origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `10` |
| [].price | string |  | Price.<br>委托价格<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>仅减仓<br>例: `False` |
| [].side | string |  | Side.<br>买卖方向<br>例: `SELL` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | 例: `0` |
| [].closePosition | boolean |  | Close Position.<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| [].type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1566818724722` |
| [].workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auto cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `1693207680000` |
| [].code | integer (int64) |  | 例: `-2022` |
| [].msg | string |  | 例: `ReduceOnly Order is rejected.` |

## Modify Multiple Orders (TRADE)（批量修改订单 (TRADE)）

`PUT /fapi/v1/batchOrders`

Modify Multiple Orders (TRADE)

批量修改订单

权重: 5 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
5 on IP rate limit(x-mbx-used-weight-1m);

Operation ID: `modifyMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchOrders | object[] | 是 | order list. Max 5 orders<br>订单列表,最多支持5个订单 |
| batchOrders[].orderId | integer (int64) |  | 例: `20072994037` |
| batchOrders[].origClientOrderId | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| batchOrders[].symbol | string |  | 例: `BTCUSDT` |
| batchOrders[].side | string |  | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| batchOrders[].quantity | number (float) |  | Order quantity, cannot be sent with closePosition=true<br>委托数量, 不能与 closePosition=true 同时传入<br>例: `1` |
| batchOrders[].price | number (float) |  | 例: `30005` |
| batchOrders[].priceMatch | string |  | Only avaliable for LIMIT/STOP/TAKE_PROFIT order; Cannot be sent together with `price`.<br>仅适用于LIMIT/STOP/TAKE_PROFIT订单; 不能与 `price` 同时传入.<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| batchOrders[].stopPrice | number (float) |  | stop price, only STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET need<br>止损价, 仅 STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET 订单需要<br>例: `0` |
| batchOrders[].modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| batchOrders[].recvWindow | integer (int64) |  | Validity window in milliseconds.<br>请求有效时间窗口（毫秒）。<br>例: `5000` |
| batchOrders[].timestamp | integer (int64) |  | Unix timestamp in milliseconds.<br>Unix 时间戳（毫秒）。<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Multiple Orders / Modify Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | 例: `20072994037` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].pair | string |  | 例: `BTCUSDT` |
| [].status | string |  | 例: `NEW` |
| [].clientOrderId | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| [].price | string |  | 例: `30005` |
| [].origQty | string |  | 例: `1` |
| [].executedQty | string |  | 例: `0` |
| [].cumQty | string |  | 例: `0` |
| [].timeInForce | string |  | 例: `GTC` |
| [].type | string |  | 例: `LIMIT` |
| [].reduceOnly | boolean |  | 例: `False` |
| [].closePosition | boolean |  | 例: `False` |
| [].side | string |  | 例: `BUY` |
| [].positionSide | string |  | 例: `LONG` |
| [].stopPrice | string |  | 例: `0` |
| [].workingType | string |  | 例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | 例: `False` |
| [].origType | string |  | 例: `LIMIT` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |
| [].updateTime | integer (int64) |  | 例: `1629182711600` |
| [].code | integer (int64) |  | 例: `-2022` |
| [].msg | string |  | 例: `ReduceOnly Order is rejected.` |

## Cancel Multiple Orders (TRADE)（批量撤销订单 (TRADE)）

`DELETE /fapi/v1/batchOrders`

Cancel Multiple Orders

批量撤销订单 (TRADE)

Operation ID: `cancelMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderIdList | query | integer (int64)[] |  |  |
| origClientOrderIdList | query | string[] |  |  |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Multiple Orders / 取消Multiple 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `myOrder1` |
| [].cumQty | string |  | 例: `0` |
| [].executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| [].orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `283194212` |
| [].origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `11` |
| [].price | string |  | Price.<br>委托价格<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>仅减仓<br>例: `False` |
| [].side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| [].origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1571110484038` |
| [].workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |
| [].code | integer (int64) |  | 例: `-2011` |
| [].msg | string |  | 例: `Unknown order sent.` |

## Query Order (USER_DATA)（查询订单 (USER_DATA)）

`GET /fapi/v1/order`

Check an order's status.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询订单状态

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1917641` |
| origClientOrderId | query | string |  | 例: `abc` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Order / 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Avg Price.<br>平均成交价<br>例: `0.00000` |
| clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `abc` |
| cumQuote | string |  | Cum Quote.<br>成交金额<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `1573346959` |
| origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `0.40` |
| origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| price | string |  | Price.<br>委托价格<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>是否仅减仓<br>例: `False` |
| side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| time | integer (int64) |  | order time<br>订单时间<br>例: `1579276756075` |
| timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | Price Match.<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | Self Trade Prevention Mode.<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | Good Till Date.<br>订单TIF为GTD时的自动取消时间<br>例: `0` |

## New Order (TRADE)（下单 (TRADE)）

`POST /fapi/v1/order`

Send in a new order.

下单

权重: 1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
0 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `newOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>例: `BOTH` |
| type | string | 是 | Order type<br>订单类型 `LIMIT`, `MARKET`<br>枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`, `RPI`<br>例: `GTC` |
| reduceOnly | string |  | Cannot be sent in Hedge Mode<br>双开模式下不接受此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| quantity | number (float) |  | 例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>仅对`LIMIT`/`STOP`/`TAKE_PROFIT`订单有效；不能与`price`参数同时传入<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `EXPIRE_MAKER`<br>`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`； 默认`EXPIRE_MAKER`<br>枚举: `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>例: `EXPIRE_TAKER` |
| goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000<br>TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Order / New 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `testOrder` |
| cumQty | string |  | 例: `0` |
| executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `22542179` |
| origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `10` |
| price | string |  | Price.<br>委托价格<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>仅减仓<br>例: `False` |
| side | string |  | Side.<br>买卖方向<br>例: `SELL` |
| positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | ignored for LIMIT / MARKET orders<br>触发价，`LIMIT`/`MARKET` 订单忽略此字段<br>例: `0` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTD` |
| type | string |  | Type.<br>订单类型<br>例: `LIMIT` |
| origType | string |  | Orig Type.<br>触发前订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1566818724722` |
| workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `1693207680000` |

## Modify Order (TRADE)（修改订单 (TRADE)）

`PUT /fapi/v1/order`

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

权重: 1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
0 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `modifyOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `20072994037` |
| origClientOrderId | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| symbol | string | 是 | 例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | Order quantity, cannot be sent with `closePosition=true`<br>下单数量,使用`closePosition`不支持此参数。<br>例: `1.0` |
| price | number (float) | 是 | 例: `30005` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>仅适用于`LIMIT`/`STOP`/`TAKE_PROFIT`订单; 不能与`price`参数同时传入<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| reduceOnly | string |  | See notes below for behavior.<br>行为说明见下方备注。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Order / Modify 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | 例: `20072994037` |
| symbol | string |  | 例: `BTCUSDT` |
| pair | string |  | 例: `BTCUSDT` |
| status | string |  | 例: `NEW` |
| clientOrderId | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| price | string |  | 例: `30005` |
| origQty | string |  | 例: `1` |
| executedQty | string |  | 例: `0` |
| cumQty | string |  | 例: `0` |
| timeInForce | string |  | 例: `GTC` |
| type | string |  | 例: `LIMIT` |
| reduceOnly | boolean |  | 例: `False` |
| closePosition | boolean |  | 例: `False` |
| side | string |  | 例: `BUY` |
| positionSide | string |  | 例: `LONG` |
| stopPrice | string |  | 例: `0` |
| workingType | string |  | 例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | 例: `False` |
| origType | string |  | 例: `LIMIT` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |
| updateTime | integer (int64) |  | 例: `1629182711600` |

## Cancel Order (TRADE)（撤销订单 (TRADE)）

`DELETE /fapi/v1/order`

Cancel an active order.

撤销订单

Operation ID: `cancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `283194212` |
| origClientOrderId | query | string |  | 例: `myOrder1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Order / 取消订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `myOrder1` |
| cumQty | string |  | 例: `0` |
| executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `283194212` |
| origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `11` |
| price | string |  | Price.<br>委托价格<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>仅减仓<br>例: `False` |
| side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1571110484038` |
| workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |

## Change Initial Leverage (TRADE)（调整开仓杠杆 (TRADE)）

`POST /fapi/v1/leverage`

Change user's initial leverage of specific symbol market.

调整用户在指定symbol合约的开仓杠杆。

Operation ID: `changeInitialLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| leverage | integer (int64) | 是 | Target initial leverage. The maximum is symbol-specific: use `initialLeverage` of bracket 1 from `GET /fapi/v1/leverageBracket`.<br>目标杠杆倍数。最大值因交易对而异，以 `GET /fapi/v1/leverageBracket` 返回的第 1 档 `initialLeverage` 为准。<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Initial Leverage / 修改Initial Leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leverage | integer (int64) |  | Leverage.<br>杠杆倍数<br>例: `21` |
| maxNotionalValue | string |  | Max Notional Value.<br>当前杠杆倍数下允许的最大名义价值<br>例: `1000000` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |

## Change Margin Type (TRADE)（变换逐全仓模式 (TRADE)）

`POST /fapi/v1/marginType`

Change symbol level margin type

变换用户在指定symbol合约上的保证金模式：逐仓或全仓。

Operation ID: `changeMarginType`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| marginType | string | 是 | 枚举: `ISOLATED`, `CROSSED`<br>例: `ISOLATED` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Margin Type / 修改杠杆 类型

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## Current All Algo Open Orders (USER_DATA)（查看当前全部条件挂单 (USER_DATA)）

`GET /fapi/v1/openAlgoOrders`

Get all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on USD-M Futures.

查看某个交易对下当前所有的条件挂单（Algo / Conditional Order），包括 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

权重: **1** for a single symbol; **40** when the symbol parameter is omitted

**Careful** when accessing this with no symbol.

Operation ID: `currentAllAlgoOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoType | query | string |  | 例: `CONDITIONAL` |
| symbol | query | string |  | 例: `BTCUSDT` |
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
| [].symbol | string |  | 例: `BNBUSDT` |
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

`GET /fapi/v1/openOrders`

Get all open orders on a symbol.

查看当前全部挂单

权重: **1** for a single symbol; **40** when the symbol parameter is omitted

**Careful** when accessing this with no symbol.

Operation ID: `currentAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current All Open Orders / 当前 All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>平均成交价<br>例: `0.00000` |
| [].clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `abc` |
| [].cumQuote | string |  | Cum Quote.<br>成交金额<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| [].orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].price | string |  | Price.<br>委托价格<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>是否仅减仓<br>例: `False` |
| [].side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| [].closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].time | integer (int64) |  | order time<br>订单时间<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| [].type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| [].workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| [].priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| [].priceMatch | string |  | price match mode<br>例: `NONE` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |

## Futures TradFi Perps Contract (USER_DATA)（传统金融合约协议 (USER_DATA)）

`POST /fapi/v1/stock/contract`

Sign TradFi-Perps agreement contract

签署 TradFi-Perps 协议合约

Operation ID: `futuresTradfiPerpsContract`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures TradFi Perps Contract / 合约 Trad Fi Perps Contract

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## Get Order Modify History (USER_DATA)（查询订单修改历史 (USER_DATA)）

`GET /fapi/v1/orderAmendment`

Get order modification history

查询订单修改历史

Operation ID: `getOrderModifyHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `20072994037` |
| origClientOrderId | query | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| startTime | query | integer (int64) |  | Timestamp in ms to get modification history from INCLUSIVE<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get modification history until INCLUSIVE<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `50`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Order Modify History / 获取订单 Modify 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amendmentId | integer (int64) |  | Order modification ID<br>修改记录号<br>例: `5363` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].pair | string |  | 例: `BTCUSDT` |
| [].orderId | integer (int64) |  | 例: `20072994037` |
| [].clientOrderId | string |  | 例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].time | integer (int64) |  | Order modification time<br>修改时间<br>例: `1629184560899` |
| [].amendment | object |  |  |
| [].amendment.price | object |  |  |
| [].amendment.price.before | string |  | 例: `30004` |
| [].amendment.price.after | string |  | 例: `30003.2` |
| [].amendment.origQty | object |  |  |
| [].amendment.origQty.before | string |  | 例: `1` |
| [].amendment.origQty.after | string |  | 例: `1` |
| [].amendment.count | integer (int64) |  | Order modification count, representing the number of times the order has been modified<br>修改记数，代表该修改记录是这笔订单第几次修改<br>例: `3` |
| [].amendment.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `123` |

## Get Position Margin Change History (TRADE)（逐仓保证金变动历史 (TRADE)）

`GET /fapi/v1/positionMargin/history`

Get Position Margin Change History

查询逐仓保证金变动历史

Operation ID: `getPositionMarginChangeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| type | query | string |  | 1: Add position margin，2: Reduce position margin<br>调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金<br>例: `1` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | time if not pass<br>结束时间，默认为当前时间<br>默认: `current`<br>例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Position Margin Change History / 获取持仓 杠杆 修改历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].type | integer (int64) |  | Type.<br>调整方向<br>例: `1` |
| [].deltaType | string |  | Delta Type.<br>划转类型<br>例: `USER_ADJUST` |
| [].amount | string |  | Amount.<br>数量<br>例: `23.36332311` |
| [].asset | string |  | Asset.<br>资产<br>例: `USDT` |
| [].time | integer (int64) |  | Time.<br>时间<br>例: `1578047897183` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `BOTH` |

## Modify Isolated Position Margin (TRADE)（调整逐仓保证金 (TRADE)）

`POST /fapi/v1/positionMargin`

Modify Isolated Position Margin

针对逐仓模式下的仓位，调整其逐仓保证金资金。

Operation ID: `modifyIsolatedPositionMargin`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>例: `BOTH` |
| amount | number (float) | 是 | Margin asset<br>保证金资金<br>例: `1.0` |
| type | integer | 是 | 1: Add position margin，2: Reduce position margin<br>调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify Isolated Position Margin / Modify Isolated 持仓 杠杆

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) |  | 例: `100` |
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `Successfully modify position margin.` |
| type | integer (int64) |  | 例: `1` |

## Position ADL Quantile Estimation (USER_DATA)（持仓ADL队列估算 (USER_DATA)）

`GET /fapi/v1/adlQuantile`

Position ADL Quantile Estimation

* Values update every 30s.
* Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
* For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
* If the positions of the symbol are crossed margined in Hedge Mode:
  * "HEDGE" as a sign will be returned instead of "BOTH";
  * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.

持仓ADL队列估算

* 每30秒更新数据
* 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
* 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
  * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE",
  其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。

Operation ID: `positionAdlQuantileEstimation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Position ADL Quantile Estimation / 持仓 ADL Quantile Estimation

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | 例: `ETHUSDT` |
| [].adlQuantile | object |  |  |
| [].adlQuantile.LONG | integer (int64) |  | adl quantile for "LONG" position in hedge mode<br>双开模式下多头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.SHORT | integer (int64) |  | adl qauntile for "SHORT" position in hedge mode<br>双开模式下空头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.HEDGE | integer (int64) |  | only a sign, ignore the value<br>HEDGE 仅作为指示出现，请忽略数值<br>例: `0` |
| [].adlQuantile.BOTH | integer (int64) |  | adl qunatile for position in one-way mode<br>单开模式下持仓的ADL队列估算分<br>例: `0` |

## Position Information V2 (USER_DATA)（用户持仓风险V2 (USER_DATA)）

`GET /fapi/v2/positionRisk`

Get current position information.

查询持仓风险

Operation ID: `positionInformationV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Position Information V2 / 持仓 信息 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].entryPrice | string |  | Entry Price.<br>开仓均价<br>例: `0.00000` |
| [].breakEvenPrice | string |  | Break Even Price.<br>盈亏平衡价<br>例: `0.0` |
| [].marginType | string |  | Margin Type.<br>逐仓模式或全仓模式<br>例: `isolated` |
| [].isAutoAddMargin | string |  | 例: `false` |
| [].isolatedMargin | string |  | Isolated Margin.<br>逐仓保证金<br>例: `0.00000000` |
| [].leverage | string |  | Leverage.<br>当前杠杆倍数<br>例: `10` |
| [].liquidationPrice | string |  | Liquidation Price.<br>参考强平价格<br>例: `0` |
| [].markPrice | string |  | Mark Price.<br>当前标记价格<br>例: `6679.50671178` |
| [].maxNotionalValue | string |  | Max Notional Value.<br>当前杠杆倍数允许的名义价值上限<br>例: `20000000` |
| [].positionAmt | string |  | Position Amt.<br>头寸数量，符号代表多空方向, 正数为多，负数为空<br>例: `0.000` |
| [].notional | string |  | 例: `0` |
| [].isolatedWallet | string |  | 例: `0` |
| [].symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| [].unRealizedProfit | string |  | Un Realized Profit.<br>持仓未实现盈亏<br>例: `0.00000000` |
| [].positionSide | string |  | Position Side.<br>持仓方向<br>例: `BOTH` |
| [].updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1625474304765` |

## Position Information V3 (USER_DATA)（用户持仓风险V3 (USER_DATA)）

`GET /fapi/v3/positionRisk`

Get current position information(only symbol that has position or open
orders will be returned).

查询持仓风险，仅返回有持仓或挂单的交易对

Operation ID: `positionInformationV3`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Position Information V3 / 持仓 信息 V3

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol<br>交易对<br>例: `ADAUSDT` |
| [].positionSide | string |  | position side<br>持仓方向<br>例: `BOTH` |
| [].positionAmt | string |  | position amount, positive for long, negative for short<br>头寸数量，符号代表多空方向, 正数为多，负数为空<br>例: `30` |
| [].entryPrice | string |  | entry price<br>开仓均价<br>例: `0.385` |
| [].breakEvenPrice | string |  | break-even price<br>盈亏平衡价<br>例: `0.385077` |
| [].markPrice | string |  | current mark price<br>当前标记价格<br>例: `0.41047590` |
| [].unRealizedProfit | string |  | unrealized profit<br>持仓未实现盈亏<br>例: `0.76427700` |
| [].liquidationPrice | string |  | liquidation price<br>参考强平价格<br>例: `0` |
| [].isolatedMargin | string |  | isolated margin<br>逐仓保证金<br>例: `0` |
| [].notional | string |  | notional value of position<br>名义价值<br>例: `12.31427700` |
| [].marginAsset | string |  | margin asset<br>保证金资产<br>例: `USDT` |
| [].isolatedWallet | string |  | isolated wallet (if isolated position)<br>逐仓钱包余额<br>例: `0` |
| [].initialMargin | string |  | initial margin required with current mark price<br>初始保证金<br>例: `0.61571385` |
| [].maintMargin | string |  | maintenance margin required<br>维持保证金<br>例: `0.08004280` |
| [].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>仓位初始保证金<br>例: `0.61571385` |
| [].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>订单初始保证金<br>例: `0` |
| [].adl | integer (int64) |  | auto-deleverage ranking<br>自动减仓等级<br>例: `2` |
| [].bidNotional | string |  | ignore<br>忽略<br>例: `0` |
| [].askNotional | string |  | ignore<br>忽略<br>例: `0` |
| [].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1720736417660` |

## Query All Algo Orders (USER_DATA)（查询所有条件订单(包括历史订单) (USER_DATA)）

`GET /fapi/v1/allAlgoOrders`

Get all algo (conditional) orders — active, CANCELED, TRIGGERED, or FINISHED — including TP/SL (Take Profit / Stop Loss) and trailing stop orders on USD-M Futures.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询所有条件订单（Algo / Conditional Order），包括活跃、已撤销、已触发与已完成订单，覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）。

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryAllAlgoOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
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
| [].symbol | string |  | 例: `BNBUSDT` |
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

`GET /fapi/v1/openOrder`

Query open order

请小心使用不带symbol参数的调用

Operation ID: `queryCurrentOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1917641` |
| origClientOrderId | query | string |  | 例: `abc` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Open Order / 当前 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Avg Price.<br>平均成交价<br>例: `0.00000` |
| clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `abc` |
| cumQuote | string |  | Cum Quote.<br>成交金额<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `1917641` |
| origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `0.40` |
| origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| price | string |  | Price.<br>委托价格<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>是否仅减仓<br>例: `False` |
| side | string |  | Side.<br>买卖方向<br>例: `BUY` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `9300` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| time | integer (int64) |  | order time<br>订单时间<br>例: `1579276756075` |
| timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTC` |
| type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1579276756075` |
| workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `0` |

## Test Order (TRADE)（下单测试 (TRADE)）

`POST /fapi/v1/order/test`

Testing order request, this order will not be submitted to matching engine

用于测试订单请求，但不会提交到撮合引擎

Operation ID: `testOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`<br>双开模式下不接受此参数；使用`closePosition`不支持此参数。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| quantity | number (float) |  | Cannot be sent with `closePosition`=`true`(Close-All)<br>下单数量,使用`closePosition`不支持此参数。<br>例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| stopPrice | number (float) |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数<br>例: `1.0` |
| closePosition | string |  | Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`."<br>触发后全部平仓，仅支持 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET`。<br>枚举: `true`, `false`<br>例: `false` |
| activationPrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`)<br>追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)<br>例: `1.0` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders<br>追踪止损回调比例，仅 `TRAILING_STOP_MARKET` 使用。<br>例: `1` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`, `RPI`<br>例: `GTC` |
| workingType | string |  | 枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| priceProtect | string |  | 枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>盘口价格下单模式，不能与 `price` 同时传入。<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| selfTradePreventionMode | string |  | `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`<br>订单自成交保护模式，默认 `NONE`。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `NONE`<br>例: `EXPIRE_TAKER` |
| goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000<br>TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Test Order / Test 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order Id.<br>用户自定义的订单号<br>例: `testOrder` |
| cumQty | string |  | 例: `0` |
| cumQuote | string |  | Cum Quote.<br>成交金额<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>成交量<br>例: `0` |
| orderId | integer (int64) |  | Order Id.<br>系统订单号<br>例: `22542179` |
| avgPrice | string |  | Avg Price.<br>平均成交价<br>例: `0.00000` |
| origQty | string |  | Orig Qty.<br>原始委托数量<br>例: `10` |
| price | string |  | Price.<br>委托价格<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>仅减仓<br>例: `False` |
| side | string |  | Side.<br>买卖方向<br>例: `SELL` |
| positionSide | string |  | Position Side.<br>持仓方向<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价，对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| symbol | string |  | Symbol.<br>交易对<br>例: `BTCUSDT` |
| timeInForce | string |  | Time In Force.<br>有效方法<br>例: `GTD` |
| type | string |  | Type.<br>订单类型<br>例: `TRAILING_STOP_MARKET` |
| origType | string |  | Orig Type.<br>触发前订单类型<br>例: `TRAILING_STOP_MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段<br>例: `0.3` |
| updateTime | integer (int64) |  | Update Time.<br>更新时间<br>例: `1566818724722` |
| workingType | string |  | Working Type.<br>条件价格触发类型<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `1693207680000` |

## User's Force Orders (USER_DATA)（用户强平单历史 (USER_DATA)）

`GET /fapi/v1/forceOrders`

Query user's Force Orders

查询用户强平单历史

权重: **20** with symbol, **50** without symbol

Operation ID: `usersForceOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| autoCloseType | query | string |  | "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.<br>"LIQUIDATION": 强平单, "ADL": ADL 减仓单.<br>枚举: `LIQUIDATION`, `ADL`<br>例: `LIQUIDATION` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `50`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User's Force Orders / 用户's Force 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | 例: `6071832819` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].pair | string |  | Pair.<br>标的交易对<br>例: `BTCUSDT` |
| [].status | string |  | 例: `FILLED` |
| [].clientOrderId | string |  | 例: `autoclose-1596107620040000020` |
| [].price | string |  | 例: `10871.09` |
| [].avgPrice | string |  | 例: `10913.21000` |
| [].origQty | string |  | 例: `0.001` |
| [].executedQty | string |  | 例: `0.001` |
| [].cumQuote | string |  | 例: `10.91321` |
| [].cumBase | string |  | Cum Base.<br>成交金额(标的数量)<br>例: `0.001` |
| [].timeInForce | string |  | 例: `IOC` |
| [].type | string |  | 例: `LIMIT` |
| [].reduceOnly | boolean |  | 例: `False` |
| [].closePosition | boolean |  | 例: `False` |
| [].side | string |  | 例: `SELL` |
| [].positionSide | string |  | 例: `BOTH` |
| [].stopPrice | string |  | 例: `0` |
| [].workingType | string |  | 例: `CONTRACT_PRICE` |
| [].origType | string |  | 例: `LIMIT` |
| [].time | integer (int64) |  | 例: `1596107620044` |
| [].updateTime | integer (int64) |  | 例: `1596107620087` |

## Start User Data Stream (USER_STREAM)（生成listenKey (USER_STREAM)）

`POST /fapi/v1/listenKey`

Start a new user data stream. The stream will close after 60 minutes
unless a keepalive is sent. If the account has an active `listenKey`,
that `listenKey` will be returned and its validity will be extended for
60 minutes.

创建一个新的user data
stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

Operation ID: `startUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | 例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1` |

## Keepalive User Data Stream (USER_STREAM)（延长listenKey有效期 (USER_STREAM)）

`PUT /fapi/v1/listenKey`

Keepalive a user data stream to prevent a time out. User data streams
will close after 60 minutes. It's recommended to send a ping about every
60 minutes.

有效期延长至本次调用后60分钟

Operation ID: `keepaliveUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Keepalive User Data Stream / Keepalive 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | the listenkey which got extended<br>被延长有效期的 listenKey<br>例: `3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg` |

## Close User Data Stream (USER_STREAM)（关闭listenKey (USER_STREAM)）

`DELETE /fapi/v1/listenKey`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功