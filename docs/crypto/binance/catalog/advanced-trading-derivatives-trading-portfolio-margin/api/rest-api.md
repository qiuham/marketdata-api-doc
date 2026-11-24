---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:13.850437
---

# Portfolio Margin REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/1.0.0/schema.yaml

Access account information, manage margin positions, and trade with Binance Portfolio Margin.

访问账户信息、管理保证金仓位，并通过 Binance 统一账户进行交易。

版本: 1.0.0

## 服务地址

- `https://papi.binance.com`
- `https://testnet.binancefuture.com`

## 接口列表

- `GET /papi/v1/balance` — Account Balance (USER_DATA)
- `GET /papi/v1/account` — Account Information (USER_DATA)
- `POST /papi/v1/bnb-transfer` — BNB transfer (TRADE)
- `GET /papi/v1/repay-futures-switch` — Get Auto-repay-futures Status (USER_DATA)
- `POST /papi/v1/repay-futures-switch` — Change Auto-repay-futures Status (TRADE)
- `POST /papi/v1/cm/leverage` — Change CM Initial Leverage (TRADE)
- `GET /papi/v1/cm/positionSide/dual` — Get CM Current Position Mode (USER_DATA)
- `POST /papi/v1/cm/positionSide/dual` — Change CM Position Mode (TRADE)
- `POST /papi/v1/um/leverage` — Change UM Initial Leverage (TRADE)
- `GET /papi/v1/um/positionSide/dual` — Get UM Current Position Mode (USER_DATA)
- `POST /papi/v1/um/positionSide/dual` — Change UM Position Mode (TRADE)
- `GET /papi/v1/cm/leverageBracket` — CM Notional and Leverage Brackets (USER_DATA)
- `POST /papi/v1/auto-collection` — Fund Auto-collection (TRADE)
- `POST /papi/v1/asset-collection` — Fund Collection by Asset (TRADE)
- `GET /papi/v1/cm/account` — Get CM Account Detail (USER_DATA)
- `GET /papi/v1/cm/order/asyn/id` — Get CM Futures Order Download Link by Id (USER_DATA)
- `GET /papi/v1/cm/trade/asyn/id` — Get CM Futures Trade Download Link by Id (USER_DATA)
- `GET /papi/v1/cm/income/asyn/id` — Get CM Futures Transaction Download Link by Id (USER_DATA)
- `GET /papi/v1/cm/income` — Get CM Income History (USER_DATA)
- `GET /papi/v1/cm/order/asyn` — Get Download Id For CM Futures Order History (USER_DATA)
- `GET /papi/v1/cm/trade/asyn` — Get Download Id For CM Futures Trade History (USER_DATA)
- `GET /papi/v1/cm/income/asyn` — Get Download Id For CM Futures Transaction History (USER_DATA)
- `GET /papi/v1/um/order/asyn` — Get Download Id For UM Futures Order History (USER_DATA)
- `GET /papi/v1/um/trade/asyn` — Get Download Id For UM Futures Trade History (USER_DATA)
- `GET /papi/v1/um/income/asyn` — Get Download Id For UM Futures Transaction History (USER_DATA)
- `GET /papi/v1/margin/marginInterestHistory` — Get Margin Borrow/Loan Interest History (USER_DATA)
- `GET /papi/v1/um/account` — Get UM Account Detail (USER_DATA)
- `GET /papi/v2/um/account` — Get UM Account Detail V2 (USER_DATA)
- `GET /papi/v1/um/order/asyn/id` — Get UM Futures Order Download Link by Id (USER_DATA)
- `GET /papi/v1/um/trade/asyn/id` — Get UM Futures Trade Download Link by Id (USER_DATA)
- `GET /papi/v1/um/income/asyn/id` — Get UM Futures Transaction Download Link by Id (USER_DATA)
- `GET /papi/v1/um/income` — Get UM Income History (USER_DATA)
- `GET /papi/v1/cm/commissionRate` — Get User Commission Rate for CM (USER_DATA)
- `GET /papi/v1/um/commissionRate` — Get User Commission Rate for UM (USER_DATA)
- `GET /papi/v1/margin/maxBorrowable` — Margin Max Borrow (USER_DATA)
- `GET /papi/v1/um/apiTradingStatus` — Portfolio Margin UM Trading Quantitative Rules Indicators (USER_DATA)
- `GET /papi/v1/cm/positionRisk` — Query CM Position Information (USER_DATA)
- `GET /papi/v1/margin/marginLoan` — Query Margin Loan Record (USER_DATA)
- `GET /papi/v1/margin/maxWithdraw` — Query Margin Max Withdraw (USER_DATA)
- `GET /papi/v1/margin/repayLoan` — Query Margin repay Record (USER_DATA)
- `GET /papi/v1/portfolio/interest-history` — Query Portfolio Margin Negative Balance Interest History (USER_DATA)
- `GET /papi/v1/um/positionRisk` — Query UM Position Information (USER_DATA)
- `GET /papi/v1/portfolio/negative-balance-exchange-record` — Query User Negative Balance Auto Exchange Record (USER_DATA)
- `GET /papi/v1/rateLimit/order` — Query User Rate Limit (USER_DATA)
- `POST /papi/v1/repay-futures-negative-balance` — Repay futures Negative Balance (USER_DATA)
- `GET /papi/v1/um/accountConfig` — UM Futures Account Configuration (USER_DATA)
- `GET /papi/v1/um/symbolConfig` — UM Futures Symbol Configuration (USER_DATA)
- `GET /papi/v1/um/leverageBracket` — UM Notional and Leverage Brackets (USER_DATA)
- `GET /papi/v1/ping` — Test Connectivity
- `DELETE /papi/v1/cm/conditional/allOpenOrders` — Cancel All CM Open Conditional Orders (TRADE)
- `DELETE /papi/v1/cm/allOpenOrders` — Cancel All CM Open Orders (TRADE)
- `DELETE /papi/v1/um/allOpenOrders` — Cancel All UM Open Orders (TRADE)
- `POST /papi/v1/cm/conditional/order` — New CM Conditional Order (TRADE)
- `DELETE /papi/v1/cm/conditional/order` — Cancel CM Conditional Order (TRADE)
- `GET /papi/v1/cm/order` — Query CM Order (USER_DATA)
- `POST /papi/v1/cm/order` — New CM Order (TRADE)
- `PUT /papi/v1/cm/order` — Modify CM Order (TRADE)
- `DELETE /papi/v1/cm/order` — Cancel CM Order (TRADE)
- `DELETE /papi/v1/margin/allOpenOrders` — Cancel Margin Account All Open Orders on a Symbol (TRADE)
- `GET /papi/v1/margin/orderList` — Query Margin Account's OCO (USER_DATA)
- `DELETE /papi/v1/margin/orderList` — Cancel Margin Account OCO Orders (TRADE)
- `GET /papi/v1/margin/order` — Query Margin Account Order (USER_DATA)
- `POST /papi/v1/margin/order` — New Margin Order (TRADE)
- `DELETE /papi/v1/margin/order` — Cancel Margin Account Order (TRADE)
- `GET /papi/v1/um/order` — Query UM Order (USER_DATA)
- `POST /papi/v1/um/order` — New UM Order (TRADE)
- `PUT /papi/v1/um/order` — Modify UM Order (TRADE)
- `DELETE /papi/v1/um/order` — Cancel UM Order (TRADE)
- `GET /papi/v1/cm/userTrades` — CM Account Trade List (USER_DATA)
- `GET /papi/v1/cm/adlQuantile` — CM Position ADL Quantile Estimation (USER_DATA)
- `GET /papi/v1/um/feeBurn` — Get UM Futures BNB Burn Status (USER_DATA)
- `POST /papi/v1/um/feeBurn` — Toggle BNB Burn On UM Futures Trade (TRADE)
- `POST /papi/v1/marginLoan` — Margin Account Borrow (MARGIN)
- `POST /papi/v1/margin/order/oco` — Margin Account New OCO (TRADE)
- `POST /papi/v1/repayLoan` — Margin Account Repay (MARGIN)
- `POST /papi/v1/margin/repay-debt` — Margin Account Repay Debt (TRADE)
- `GET /papi/v1/margin/myTrades` — Margin Account Trade List (USER_DATA)
- `GET /papi/v1/cm/conditional/allOrders` — Query All CM Conditional Orders (USER_DATA)
- `GET /papi/v1/cm/allOrders` — Query All CM Orders (USER_DATA)
- `GET /papi/v1/cm/conditional/openOrders` — Query All Current CM Open Conditional Orders (USER_DATA)
- `GET /papi/v1/cm/openOrders` — Query All Current CM Open Orders (USER_DATA)
- `GET /papi/v1/um/openOrders` — Query All Current UM Open Orders (USER_DATA)
- `GET /papi/v1/margin/allOrders` — Query All Margin Account Orders (USER_DATA)
- `GET /papi/v1/um/allOrders` — Query All UM Orders (USER_DATA)
- `GET /papi/v1/cm/conditional/orderHistory` — Query CM Conditional Order History (USER_DATA)
- `GET /papi/v1/cm/orderAmendment` — Query CM Modify Order History (TRADE)
- `GET /papi/v1/cm/conditional/openOrder` — Query Current CM Open Conditional Order (USER_DATA)
- `GET /papi/v1/cm/openOrder` — Query Current CM Open Order (USER_DATA)
- `GET /papi/v1/margin/openOrders` — Query Current Margin Open Order (USER_DATA)
- `GET /papi/v1/um/openOrder` — Query Current UM Open Order (USER_DATA)
- `GET /papi/v1/margin/allOrderList` — Query Margin Account's all OCO (USER_DATA)
- `GET /papi/v1/margin/openOrderList` — Query Margin Account's Open OCO (USER_DATA)
- `GET /papi/v1/um/orderAmendment` — Query UM Modify Order History (TRADE)
- `GET /papi/v1/cm/forceOrders` — Query User's CM Force Orders (USER_DATA)
- `GET /papi/v1/margin/forceOrders` — Query User's Margin Force Orders (USER_DATA)
- `GET /papi/v1/um/forceOrders` — Query User's UM Force Orders (USER_DATA)
- `GET /papi/v1/um/userTrades` — UM Account Trade List (USER_DATA)
- `GET /papi/v1/um/adlQuantile` — UM Position ADL Quantile Estimation (USER_DATA)
- `POST /papi/v1/um/algo/order` — New UM Algo Order (TRADE)
- `DELETE /papi/v1/um/algo/order` — Cancel UM Algo Order (TRADE)
- `DELETE /papi/v1/um/algo/allOpenOrders` — Cancel All UM Algo Open Orders (TRADE)
- `GET /papi/v1/um/algo/algoOrder` — Query Current UM Open Algo Order (USER_DATA)
- `GET /papi/v1/um/algo/openAlgoOrders` — Query All Current UM Open Algo Orders (USER_DATA)
- `GET /papi/v1/um/algo/allAlgoOrders` — Query UM Algo Order History (USER_DATA)
- `POST /papi/v1/um/stock/contract` — Futures TradFi Perps Contract (USER_DATA)
- `POST /papi/v1/listenKey` — Start User Data Stream (USER_STREAM)
- `PUT /papi/v1/listenKey` — Keepalive User Data Stream (USER_STREAM)
- `DELETE /papi/v1/listenKey` — Close User Data Stream (USER_STREAM)

## Account Balance (USER_DATA)（查询账户余额 (USER_DATA)）

`GET /papi/v1/balance`

Query account balance

查询账户余额

Operation ID: `accountBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Balance / 账户 Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 2).asset | string |  | asset name<br>资产<br>例: `USDT` |
| (oneOf 2).totalWalletBalance | string |  | Total Wallet Balance.<br>例: `126.72469206` |
| (oneOf 2).crossMarginBorrowed | string |  | Cross Margin Borrowed.<br>例: `10.00000000` |
| (oneOf 2).crossMarginFree | string |  | Cross Margin Free.<br>例: `100.00000000` |
| (oneOf 2).crossMarginInterest | string |  | Cross Margin Interest.<br>例: `0.72469206` |
| (oneOf 2).crossMarginLocked | string |  | Cross Margin Locked.<br>例: `3.00000000` |
| (oneOf 2).umWalletBalance | string |  | Um Wallet Balance.<br>例: `0.00000000` |
| (oneOf 2).umUnrealizedPNL | string |  | Um Unrealized PNL.<br>例: `23.72469206` |
| (oneOf 2).cmWalletBalance | string |  | Cm Wallet Balance.<br>例: `23.72469206` |
| (oneOf 2).cmUnrealizedPNL | string |  | Cm Unrealized PNL.<br>例: `` |
| (oneOf 2).updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1617939110373` |
| (oneOf 2).negativeBalance | string |  | negative balance amount<br>当前负余额值<br>例: `0` |

## Account Information (USER_DATA)（查询账户信息 (USER_DATA)）

`GET /papi/v1/account`

Query account information

查询账户信息

Operation ID: `accountInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Information / 账户 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uniMMR | string |  | Portfolio margin account maintenance margin rate<br>统一账户维持保证金率<br>例: `5167.92171923` |
| accountEquity | string |  | Account equity, in USD value<br>以USD计价的账户权益<br>例: `73.47428058` |
| actualEquity | string |  | Account equity without collateral rate, in USD value<br>不考虑质押率的以USD计价账户权益<br>例: `122607.35137903` |
| accountInitialMargin | string |  | Account Initial Margin.<br>例: `23.72469206` |
| accountMaintMargin | string |  | Portfolio margin account maintenance margin, unit：USD<br>以USD计价统一账户维持保证金<br>例: `23.72469206` |
| accountStatus | string |  | Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"<br>统一账户账户状态："NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"<br>例: `NORMAL` |
| virtualMaxWithdrawAmount | string |  | Portfolio margin maximum amount for transfer out in USD<br>以USD计价的最大可转出<br>例: `1627523.32459208` |
| totalAvailableBalance | string |  | Total Available Balance.<br>例: `` |
| totalMarginOpenLoss | string |  | in USD margin open order<br>例: `` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1657707212154` |

## BNB transfer (TRADE)（BNB划转 (TRADE)）

`POST /papi/v1/bnb-transfer`

Transfer BNB in and out of UM

从PM钱包划转BNB到UM钱包

Operation ID: `bnbTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | 例: `1.0` |
| transferSide | string | 是 | 枚举: `TO_UM`, `FROM_UM`<br>例: `TO_UM` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：BNB transfer / BNB 划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | Transaction ID.<br>交易ID。<br>例: `100000001` |

## Get Auto-repay-futures Status (USER_DATA)（查询自动清还合约负余额模式 (USER_DATA)）

`GET /papi/v1/repay-futures-switch`

Query Auto-repay-futures Status

查询自动清还合约负余额模式

Operation ID: `getAutoRepayFuturesStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Auto-repay-futures Status / 获取Auto-repay-futures 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| autoRepay | boolean |  | "true" for turn on the auto-repay futures; "false" for turn off the auto-repay futures<br>`true`代表自动清还合约负余额; `false`代表关闭自动清还合约负余额<br>例: `True` |

## Change Auto-repay-futures Status (TRADE)（更改自动清还合约负余额模式 (TRADE)）

`POST /papi/v1/repay-futures-switch`

Change Auto-repay-futures Status

更改自动支付合约负余额模式

Operation ID: `changeAutoRepayFuturesStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| autoRepay | string | 是 | `false` for turn off the auto-repay futures negative balance function<br>`false`代表关闭自动清还合约负余额<br>枚举: `true`, `false`<br>默认: `true`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Auto-repay-futures Status / 修改Auto-repay-futures 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | Msg.<br>例: `success` |

## Change CM Initial Leverage (TRADE)（调整CM开仓杠杆 (TRADE)）

`POST /papi/v1/cm/leverage`

Change user's initial leverage of specific symbol in CM.

调整用户在指定CM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量

Operation ID: `changeCmInitialLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSD_200925` |
| leverage | integer (int64) | 是 | target initial leverage<br>目标初始杠杆倍数<br>例: `21` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change CM Initial Leverage / 修改CM Initial Leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leverage | integer (int64) |  | current initial leverage<br>杠杆倍率<br>例: `21` |
| maxQty | string |  | maximum quantity of base asset<br>例: `1000` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |

## Get CM Current Position Mode (USER_DATA)（查询CM持仓模式 (USER_DATA)）

`GET /papi/v1/cm/positionSide/dual`

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

查询用户目前在CM所有symbol合约上的持仓模式: 双向持仓或单向持仓。

Operation ID: `getCmCurrentPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Current Position Mode / 获取CM 当前 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | boolean |  | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>例: `True` |

## Change CM Position Mode (TRADE)（更改CM持仓模式 (TRADE)）

`POST /papi/v1/cm/positionSide/dual`

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

变换用户在 CM 所有 symbol 合约上的持仓模式：双向持仓或单向持仓。

Operation ID: `changeCmPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | string | 是 | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>枚举: `true`, `false`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change CM Position Mode / 修改CM 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `success` |

## Change UM Initial Leverage (TRADE)（调整UM开仓杠杆 (TRADE)）

`POST /papi/v1/um/leverage`

Change user's initial leverage of specific symbol in UM.

调整用户在指定UM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量

Operation ID: `changeUmInitialLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| leverage | integer (int64) | 是 | Target initial leverage. The maximum is symbol-specific: use `initialLeverage` of bracket 1 from `GET /papi/v1/um/leverageBracket`.<br>目标初始杠杆倍数。最大值因交易对而异，以 `GET /papi/v1/um/leverageBracket` 返回的第 1 档 `initialLeverage` 为准。<br>例: `21` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change UM Initial Leverage / 修改UM Initial Leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| leverage | integer (int64) |  | current initial leverage<br>杠杆倍率<br>例: `21` |
| maxNotionalValue | string |  | Max Notional Value.<br>例: `1000000` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |

## Get UM Current Position Mode (USER_DATA)（查询UM持仓模式 (USER_DATA)）

`GET /papi/v1/um/positionSide/dual`

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

查询用户目前在UM所有symbol合约上的持仓模式: 双向持仓或单向持仓。

Operation ID: `getUmCurrentPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Current Position Mode / 获取UM 当前 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | boolean |  | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>例: `True` |

## Change UM Position Mode (TRADE)（更改UM持仓模式 (TRADE)）

`POST /papi/v1/um/positionSide/dual`

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

变换用户在UM所有symbol合约上的持仓模式：双向持仓或单向持仓。

Operation ID: `changeUmPositionMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dualSidePosition | string | 是 | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>枚举: `true`, `false`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change UM Position Mode / 修改UM 持仓 Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `success` |

## CM Notional and Leverage Brackets (USER_DATA)（查询CM杠杆分层标准 (USER_DATA)）

`GET /papi/v1/cm/leverageBracket`

Query CM notional and leverage brackets

查询CM杠杆分层标准

Operation ID: `cmNotionalAndLeverageBrackets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_PERP` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Notional and Leverage Brackets / CM Notional 和 Leverage Brackets

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_PERP` |
| [].brackets | object[] |  | Brackets. |
| [].brackets[].bracket | integer (int64) |  | bracket level<br>层级<br>例: `1` |
| [].brackets[].initialLeverage | integer (int64) |  | the maximum leverage<br>该层允许的最高初始杠杆倍数<br>例: `125` |
| [].brackets[].qtyCap | integer (int64) |  | upper edge of base asset quantity<br>该层对应的数量上限<br>例: `50` |
| [].brackets[].qtyFloor | integer (int64) |  | lower edge of base asset quantity<br>该层对应的数量下限<br>例: `0` |
| [].brackets[].maintMarginRatio | number (float) |  | maintenance margin rate<br>该层对应的维持保证金率<br>例: `0.004` |
| [].brackets[].cum | number (float) |  | Auxiliary number for quick calculation<br>速算数<br>例: `0` |

## Fund Auto-collection (TRADE)（统一账户资金归集 (TRADE)）

`POST /papi/v1/auto-collection`

Fund collection for Portfolio Margin

资金归集到统一账户钱包

Operation ID: `fundAutoCollection`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fund Auto-collection / 请参见英文说明：Fund Auto-collection

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | Msg.<br>例: `success` |

## Fund Collection by Asset (TRADE)（特定资产资金归集 (TRADE)）

`POST /papi/v1/asset-collection`

Transfers specific asset from Futures Account to Margin account

特定资产账户资金归集，从合约账户划转到杠杆账户

Operation ID: `fundCollectionByAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `BTC` |
| amount | number (float) |  | Amount to collect. When provided, `futureType` is required.<br>待归集的数量。传入该参数时，`futureType` 为必填。<br>例: `10` |
| futureType | string |  | Target wallet for the collection. `OPTION` is for SPAN only. Cannot be sent without `amount`. `amount` and `futureType` must be provided together. If neither is provided, existing behavior is unchanged (query all wallets + transfer).<br>归集的目标钱包。`OPTION` 仅支持 SPAN。不能在不传 `amount` 的情况下传入。`amount` 和 `futureType` 必须同时传入。均不传入时行为不变（查询所有钱包并划转）。<br>枚举: `UM`, `CM`, `OPTION`<br>例: `UM` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fund Collection by Asset / Fund Collection by 资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | Msg.<br>例: `success` |

## Get CM Account Detail (USER_DATA)（获取CM账户信息 (USER_DATA)）

`GET /papi/v1/cm/account`

Get current CM account asset and position information.

获取现有CM账户资产和仓位信息

Operation ID: `getCmAccountDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Account Detail / 获取CM 账户 Detail

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] |  | Assets. |
| assets[].asset | string |  | asset name<br>资产<br>例: `BTC` |
| assets[].crossWalletBalance | string |  | total wallet balance<br>全仓账户余额<br>例: `0.00241969` |
| assets[].crossUnPnl | string |  | unrealized profit or loss<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| assets[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0.00000000` |
| assets[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>持仓所需起始保证金(基于最新标记价格)<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前挂单所需起始保证金(基于最新标记价格)e<br>例: `0.00000000` |
| assets[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1625474304765` |
| positions | object[] |  | positions of all symbols in the market are returned<br>头寸，将返回所有市场symbol。 |
| positions[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_201225` |
| positions[].positionAmt | string |  | position amount<br>例: `0` |
| positions[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金<br>例: `0` |
| positions[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0` |
| positions[].unrealizedProfit | string |  | unrealized profit<br>持仓未实现盈亏<br>例: `0.00000000` |
| positions[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>持仓所需起始保证金(基于最新标记价格)<br>例: `0` |
| positions[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前挂单所需起始保证金(基于最新标记价格)e<br>例: `0` |
| positions[].leverage | string |  | current initial leverage<br>杠杆倍率<br>例: `125` |
| positions[].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| positions[].entryPrice | string |  | average entry price<br>持仓成本价<br>例: `0.0` |
| positions[].maxQty | string |  | maximum quantity of base asset<br>例: `50` |
| positions[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `0` |

## Get CM Futures Order Download Link by Id (USER_DATA)（通过下载Id获取CM合约订单历史下载链接 (USER_DATA)）

`GET /papi/v1/cm/order/asyn/id`

Get CM futures order download link by Id

通过下载Id获取CM合约订单历史下载链接

Operation ID: `getCmFuturesOrderDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Futures Order Download Link by Id / 获取CM 合约 订单 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get CM Futures Trade Download Link by Id (USER_DATA)（通过下载Id获取CM合约交易历史下载链接 (USER_DATA)）

`GET /papi/v1/cm/trade/asyn/id`

Get CM futures trade download link by Id

通过下载Id获取CM合约交易历史下载链接

Operation ID: `getCmFuturesTradeDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Futures Trade Download Link by Id / 获取CM 合约 交易 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get CM Futures Transaction Download Link by Id (USER_DATA)（通过下载Id获取CM合约资金流水历史下载链接 (USER_DATA)）

`GET /papi/v1/cm/income/asyn/id`

Get CM futures Transaction download link by Id

通过下载Id获取CM合约资金流水历史下载链接

Operation ID: `getCmFuturesTransactionDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Futures Transaction Download Link by Id / 获取CM 合约 Transaction Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get CM Income History (USER_DATA)（获取CM损益资金流水 (USER_DATA)）

`GET /papi/v1/cm/income`

Get CM Income History.

获取CM损益资金流水。

Operation ID: `getCmIncomeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_200925` |
| incomeType | query | string |  | 枚举: `TRANSFER`, `WELCOME_BONUS`, `FUNDING_FEE`, `REALIZED_PNL`, `COMMISSION`, `INSURANCE_CLEAR`, `DELIVERED_SETTELMENT`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get CM Income History / 获取CM损益资金流水

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `` |
| [].incomeType | string |  | Income type.<br>收益类型。<br>例: `TRANSFER` |
| [].income | string |  | Income amount.<br>收益金额。<br>例: `-0.37500000` |
| [].asset | string |  | Income asset.<br>收益资产。<br>例: `BTC` |
| [].info | string |  | Extra information.<br>附加信息。<br>例: `WITHDRAW` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1570608000000` |
| [].tranId | string |  | Transaction ID.<br>交易ID。<br>例: `9689322392` |
| [].tradeId | string |  | Trade ID, if existing.<br>成交ID（如存在）。<br>例: `` |

## Get Download Id For CM Futures Order History (USER_DATA)（获取CM合约订单历史下载Id (USER_DATA)）

`GET /papi/v1/cm/order/asyn`

Get download id for CM futures order history

获取CM合约订单历史下载Id

Operation ID: `getDownloadIdForCmFuturesOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For CM Futures Order History / 获取Download ID 用于 CM 合约 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Download Id For CM Futures Trade History (USER_DATA)（获取CM合约交易历史下载Id (USER_DATA)）

`GET /papi/v1/cm/trade/asyn`

Get download id for CM futures trade history

获取CM合约交易历史下载Id

Operation ID: `getDownloadIdForCmFuturesTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For CM Futures Trade History / 获取Download ID 用于 CM 合约 交易 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Download Id For CM Futures Transaction History (USER_DATA)（获取CM合约资金流水历史下载Id (USER_DATA)）

`GET /papi/v1/cm/income/asyn`

Get download id for CM futures transaction history

获取CM合约资金流水历史下载Id

Operation ID: `getDownloadIdForCmFuturesTransactionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳，单位ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For CM Futures Transaction History / 获取Download ID 用于 CM 合约 Transaction 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Download Id For UM Futures Order History (USER_DATA)（获取UM合约订单历史下载Id (USER_DATA)）

`GET /papi/v1/um/order/asyn`

Get download id for UM futures order history

获取UM合约订单历史下载Id

Operation ID: `getDownloadIdForUmFuturesOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For UM Futures Order History / 获取Download ID 用于 UM 合约 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Download Id For UM Futures Trade History (USER_DATA)（获取UM合约交易历史下载Id (USER_DATA)）

`GET /papi/v1/um/trade/asyn`

Get download id for UM futures trade history

获取UM合约交易历史下载Id

Operation ID: `getDownloadIdForUmFuturesTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For UM Futures Trade History / 获取Download ID 用于 UM 合约 交易 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Download Id For UM Futures Transaction History (USER_DATA)（获取UM合约资金流水历史下载Id (USER_DATA)）

`GET /papi/v1/um/income/asyn`

Get download id for UM futures transaction history

获取UM合约资金流水历史下载Id

Operation ID: `getDownloadIdForUmFuturesTransactionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1623319461670` |
| endTime | query | integer (int64) | 是 | Timestamp in ms<br>时间戳 in ms<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Download Id For UM Futures Transaction History / 获取Download ID 用于 UM 合约 Transaction 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgCostTimestampOfLast30d | integer (int64) |  | Average time taken for data download in the past 30 days<br>过去30天平均数据下载时间<br>例: `7241837` |
| downloadId | string |  | Download ID.<br>例: `546975389218332672` |

## Get Margin Borrow/Loan Interest History (USER_DATA)（获取杠杆利息历史 (USER_DATA)）

`GET /papi/v1/margin/marginInterestHistory`

Get Margin Borrow/Loan Interest History

获取杠杆利息历史

Operation ID: `getMarginBorrowLoanInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number.<br>当前页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `10`<br>例: `10` |
| archived | query | string |  | Set to true to query archived data from 6 months ago.<br>设为 true 可查询 6 个月前的归档数据。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`<br>赋值不能超过 `60000`<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Margin Borrow/Loan Interest History / 获取杠杆 借款/借贷 利息 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Rows. |
| rows[].txId | integer (int64) |  | Tx ID.<br>例: `1352286576452864800` |
| rows[].interestAccuredTime | integer (int64) |  | Interest Accured Time.<br>例: `1672160400000` |
| rows[].asset | string |  | asset name<br>资产<br>例: `USDT` |
| rows[].rawAsset | string |  | Raw Asset.<br>例: `USDT` |
| rows[].principal | string |  | Principal repaid<br>支付的本金<br>例: `45.3313` |
| rows[].interest | string |  | Interest repaid<br>支付的利息<br>例: `0.00024995` |
| rows[].interestRate | string |  | daily interest rate<br>日利率<br>例: `0.00013233` |
| rows[].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `ON_BORROW` |
| total | integer (int64) |  | Total.<br>例: `1` |

## Get UM Account Detail (USER_DATA)（获取UM账户信息 (USER_DATA)）

`GET /papi/v1/um/account`

Get current UM account asset and position information.

现有UM账户资产和仓位信息

Operation ID: `getUmAccountDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Account Detail / 获取UM 账户 Detail

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] |  | Assets. |
| assets[].asset | string |  | asset name<br>资产<br>例: `USDT` |
| assets[].crossWalletBalance | string |  | wallet balance<br>全仓账户余额<br>例: `23.72469206` |
| assets[].crossUnPnl | string |  | unrealized profit<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| assets[].maintMargin | string |  | maintenance margin required<br>维持保证金<br>例: `0.00000000` |
| assets[].initialMargin | string |  | total initial margin required with current mark price<br>当前所需起始保证金<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>持仓所需起始保证金(基于最新标记价格)<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前挂单所需起始保证金(基于最新标记价格)<br>例: `0.00000000` |
| assets[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1625474304765` |
| positions | object[] |  | positions of all symbols in the market are returned<br>头寸，将返回所有市场symbol。 |
| positions[].symbol | string |  | symbol name<br>交易对<br>例: `BTCUSDT` |
| positions[].initialMargin | string |  | total initial margin required with current mark price<br>当前所需起始保证金<br>例: `0` |
| positions[].maintMargin | string |  | maintenance margin required<br>维持保证金<br>例: `0` |
| positions[].unrealizedProfit | string |  | unrealized profit<br>持仓未实现盈亏<br>例: `0.00000000` |
| positions[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>持仓所需起始保证金(基于最新标记价格)<br>例: `0` |
| positions[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前挂单所需起始保证金(基于最新标记价格)<br>例: `0` |
| positions[].leverage | string |  | current initial leverage<br>杠杆倍率<br>例: `100` |
| positions[].entryPrice | string |  | average entry price<br>持仓成本价<br>例: `0.00000` |
| positions[].maxNotional | string |  | maximum available notional with current leverage<br>当前杠杆下用户可用的最大名义价值<br>例: `250000` |
| positions[].bidNotional | string |  | bids notional, ignore<br>买单净值，忽略<br>例: `0` |
| positions[].askNotional | string |  | ask notional, ignore<br>卖单净值，忽略<br>例: `0` |
| positions[].positionSide | string |  | position side<br>持仓方向<br>例: `BOTH` |
| positions[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| positions[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `0` |

## Get UM Account Detail V2 (USER_DATA)（获取UM账户信息V2 (USER_DATA)）

`GET /papi/v2/um/account`

Get current UM account asset and position information.

现有UM账户资产和仓位信息

Operation ID: `getUmAccountDetailV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Account Detail V2 / 获取UM 账户 Detail V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] |  | Assets. |
| assets[].asset | string |  | asset name<br>资产<br>例: `USDT` |
| assets[].crossWalletBalance | string |  | wallet balance<br>全仓账户余额<br>例: `23.72469206` |
| assets[].crossUnPnl | string |  | unrealized profit<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| assets[].maintMargin | string |  | maintenance margin required<br>维持保证金<br>例: `0.00000000` |
| assets[].initialMargin | string |  | total initial margin required with current mark price<br>当前所需起始保证金<br>例: `0.00000000` |
| assets[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>持仓所需起始保证金(基于最新标记价格)<br>例: `0.00000000` |
| assets[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前挂单所需起始保证金(基于最新标记价格)<br>例: `0.00000000` |
| assets[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1625474304765` |
| positions | object[] |  | positions of all symbols in the market are returned<br>头寸，将返回所有市场symbol。 |
| positions[].symbol | string |  | symbol name<br>交易对<br>例: `BTCUSDT` |
| positions[].initialMargin | string |  | total initial margin required with current mark price<br>当前所需起始保证金<br>例: `0` |
| positions[].maintMargin | string |  | maintenance margin required<br>维持保证金<br>例: `0` |
| positions[].unrealizedProfit | string |  | unrealized profit<br>持仓未实现盈亏<br>例: `0.00000000` |
| positions[].positionSide | string |  | position side<br>持仓方向<br>例: `BOTH` |
| positions[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| positions[].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `0` |
| positions[].notional | string |  | Notional.<br>例: `86.98650000` |

## Get UM Futures Order Download Link by Id (USER_DATA)（通过下载Id获取UM合约订单历史下载链接 (USER_DATA)）

`GET /papi/v1/um/order/asyn/id`

Get UM futures order download link by Id

通过下载Id获取UM合约订单历史下载链接

Operation ID: `getUmFuturesOrderDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Futures Order Download Link by Id / 获取UM 合约 订单 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get UM Futures Trade Download Link by Id (USER_DATA)（通过下载Id获取UM合约交易历史下载链接 (USER_DATA)）

`GET /papi/v1/um/trade/asyn/id`

Get UM futures trade download link by Id

通过下载Id获取UM合约交易历史下载链接

Operation ID: `getUmFuturesTradeDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `545923594199212032` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Futures Trade Download Link by Id / 获取UM 合约 交易 Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get UM Futures Transaction Download Link by Id (USER_DATA)（通过下载Id获取UM合约资金流水历史下载链接 (USER_DATA)）

`GET /papi/v1/um/income/asyn/id`

Get UM futures Transaction download link by Id

通过下载Id获取UM合约资金流水历史下载链接

Operation ID: `getUmFuturesTransactionDownloadLinkById`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| downloadId | query | string | 是 | get by download id api<br>通过下载id 接口获取<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Futures Transaction Download Link by Id / 获取UM 合约 Transaction Download Link by ID

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| downloadId | string |  | Download ID.<br>例: `545923594199212032` |
| status | string |  | Enum：completed，processing<br>状态，枚举类型：completed 已完成，processing 处理中<br>例: `processing` |
| url | string |  | The link is mapped to download id<br>适配该笔ID请求的下载链接<br>例: `` |
| s3Link | string |  | S3 Link.<br>例: `null` |
| notified | boolean |  | ignore<br>忽略<br>例: `False` |
| expirationTimestamp | integer (int64) |  | The link would expire after this timestamp<br>晚于该时间戳之后链接将自动失效<br>例: `-1` |
| isExpired | string |  | Is Expired.<br>例: `null` |

## Get UM Income History (USER_DATA)（获取UM损益资金流水 (USER_DATA)）

`GET /papi/v1/um/income`

Get UM Income History.

获取UM损益资金流水。

Operation ID: `getUmIncomeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `None` |
| incomeType | query | string |  | Income type.<br>收益类型。<br>枚举: `TRANSFER`, `WELCOME_BONUS`, `REALIZED_PNL`, `FUNDING_FEE`, `COMMISSION`, `INSURANCE_CLEAR`, `REFERRAL_KICKBACK`, `COMMISSION_REBATE`, `API_REBATE`, `CONTEST_REWARD`, `CROSS_COLLATERAL_TRANSFER`, `OPTIONS_PREMIUM_FEE`, `OPTIONS_SETTLE_PROFIT`, `INTERNAL_TRANSFER`, `DELIVERED_SETTELMENT`, `COIN_SWAP_DEPOSIT`, `COIN_SWAP_WITHDRAW`, `POSITION_LIMIT_INCREASE_FEE`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Income History / 获取UM损益资金流水

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `` |
| [].incomeType | string |  | Income type.<br>收益类型。<br>例: `TRANSFER` |
| [].income | string |  | Income amount.<br>收益金额。<br>例: `-0.37500000` |
| [].asset | string |  | Income asset.<br>收益资产。<br>例: `USDT` |
| [].info | string |  | Extra information.<br>附加信息。<br>例: `TRANSFER` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1570608000000` |
| [].tranId | string |  | Transaction ID.<br>交易ID。<br>例: `9689322392` |
| [].tradeId | string |  | Trade ID, if existing.<br>成交ID（如存在）。<br>例: `` |

## Get User Commission Rate for CM (USER_DATA)（查询用户CM手续费率 (USER_DATA)）

`GET /papi/v1/cm/commissionRate`

Get User Commission Rate for CM

查询用户CM手续费率

Operation ID: `getUserCommissionRateForCm`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_PERP` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User Commission Rate for CM / 获取用户 手续费 利率 用于 CM

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_PERP` |
| makerCommissionRate | string |  | 0.015%<br>例: `0.00015` |
| takerCommissionRate | string |  | 0.040%<br>例: `0.00040` |

## Get User Commission Rate for UM (USER_DATA)（查询用户UM手续费率 (USER_DATA)）

`GET /papi/v1/um/commissionRate`

Get User Commission Rate for UM

查询用户UM手续费率

Operation ID: `getUserCommissionRateForUm`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get User Commission Rate for UM / 获取用户 手续费 利率 用于 UM

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| makerCommissionRate | string |  | 0.02%<br>例: `0.0002` |
| takerCommissionRate | string |  | 0.04%<br>例: `0.0004` |

## Margin Max Borrow (USER_DATA)（查询账户最大可借贷额度 (USER_DATA)）

`GET /papi/v1/margin/maxBorrowable`

Query margin max borrow

查询账户最大可借贷额度

Operation ID: `marginMaxBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `USDT` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`<br>赋值不能超过 `60000`<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Max Borrow / 杠杆 最大 借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | string |  | account's currently max borrowable amount with sufficient system availability<br>系统可借充足情况下用户账户当前最大可借额度<br>例: `1.69248805` |
| borrowLimit | string |  | max borrowable amount limited by the account level<br>平台限制的用户当前等级可以借的额度<br>例: `60` |

## Portfolio Margin UM Trading Quantitative Rules Indicators (USER_DATA)（统一账户UM合约交易量化规则指标 (USER_DATA)）

`GET /papi/v1/um/apiTradingStatus`

Portfolio Margin UM Trading Quantitative Rules Indicators

查询合约交易量化规则指标

权重: - 1 for a single `symbol`
- 10 when `symbol` is omitted

Operation ID: `portfolioMarginUmTradingQuantitativeRulesIndicators`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin UM Trading Quantitative Rules Indicators / Portfolio 杠杆 UM Trading Quantitative Rules Indicators

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| indicators | object |  | Indicators. |
| indicators.BTCUSDT | object[] |  | BTCUSDT. |
| indicators.BTCUSDT[].isLocked | boolean |  | Is Locked.<br>例: `True` |
| indicators.BTCUSDT[].plannedRecoverTime | integer (int64) |  | Planned Recover Time.<br>例: `1545741270000` |
| indicators.BTCUSDT[].indicator | string |  | Indicator.<br>例: `UFR` |
| indicators.BTCUSDT[].value | number (float) |  | Value.<br>例: `0.05` |
| indicators.BTCUSDT[].triggerValue | number (float) |  | Trigger Value.<br>例: `0.995` |
| indicators.ACCOUNT | object[] |  | ACCOUNT. |
| indicators.ACCOUNT[].indicator | string |  | Indicator.<br>例: `TMV` |
| indicators.ACCOUNT[].value | integer (int64) |  | Value.<br>例: `10` |
| indicators.ACCOUNT[].triggerValue | integer (int64) |  | Trigger Value.<br>例: `1` |
| indicators.ACCOUNT[].plannedRecoverTime | integer (int64) |  | Planned Recover Time.<br>例: `1644919865000` |
| indicators.ACCOUNT[].isLocked | boolean |  | Is Locked.<br>例: `True` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1644913304748` |

## Query CM Position Information (USER_DATA)（用户CM持仓风险 (USER_DATA)）

`GET /papi/v1/cm/positionRisk`

Get current CM position information.

获取用户CM持仓风险

Operation ID: `queryCmPositionInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| marginAsset | query | string |  | 例: `USDT` |
| pair | query | string |  | 例: `BTCUSD_201225` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Position Information / CM 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_201225` |
| [].positionAmt | string |  | position amount<br>例: `0` |
| [].entryPrice | string |  | average entry price<br>持仓成本价<br>例: `0.0` |
| [].markPrice | string |  | Mark Price.<br>例: `0.00000000` |
| [].unRealizedProfit | string |  | Un Realized Profit.<br>例: `0.00000000` |
| [].liquidationPrice | string |  | Liquidation Price.<br>例: `6170.20509059` |
| [].leverage | string |  | current initial leverage<br>杠杆倍率<br>例: `125` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `0` |
| [].maxQty | string |  | maximum quantity of base asset<br>例: `50` |
| [].notionalValue | string |  | Notional Value.<br>例: `0.00084827` |

## Query Margin Loan Record (USER_DATA)（查询杠杆借贷记录 (USER_DATA)）

`GET /papi/v1/margin/marginLoan`

Query margin loan record

查询杠杆借贷记录

Operation ID: `queryMarginLoanRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `USDT` |
| txId | query | integer (int64) |  | the `tranId` in `POST/papi/v1/marginLoan`<br>`tran ID` in `POST/papi/v1/margin借贷`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number.<br>当前页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `10`<br>例: `10` |
| archived | query | string |  | Set to true to query archived data from 6 months ago.<br>设为 true 可查询 6 个月前的归档数据。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Loan Record / 杠杆 借贷 Record

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Rows. |
| rows[].txId | integer (int64) |  | Tx ID.<br>例: `12807067523` |
| rows[].asset | string |  | asset name<br>资产<br>例: `BNB` |
| rows[].principal | string |  | Principal repaid<br>支付的本金<br>例: `0.84624403` |
| rows[].timestamp | integer (int64) |  | Timestamp.<br>例: `1555056425000` |
| rows[].status | string |  | one of PENDING (pending execution), CONFIRMED (successfully loaned), FAILED (execution failed, nothing happened to your account);<br>状态: PENDING (等待执行), CONFIRMED (成功借贷), FAILED (执行失败);<br>例: `CONFIRMED` |
| total | integer (int64) |  | Total.<br>例: `1` |

## Query Margin Max Withdraw (USER_DATA)（查询账户最大可转出额度 (USER_DATA)）

`GET /papi/v1/margin/maxWithdraw`

Query Margin Max Withdraw

查询账户最大可转出额度

Operation ID: `queryMarginMaxWithdraw`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `USDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Max Withdraw / 杠杆 最大 Withdraw

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | string |  | account's currently max withdrawable amount with sufficient system availability<br>系统可用充足情况下用户账户当前最大可转出额度<br>例: `60` |

## Query Margin repay Record (USER_DATA)（查询杠杆还贷记录 (USER_DATA)）

`GET /papi/v1/margin/repayLoan`

Query margin repay record.

查询杠杆还贷记录

Operation ID: `queryMarginRepayRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `USDT` |
| txId | query | integer (int64) |  | the `tranId` in `POST /papi/v1/repayLoan`<br>`tran ID` in `POST /papi/v1/repayLoan`<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number.<br>当前页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `10`<br>例: `10` |
| archived | query | string |  | Set to true to query archived data from 6 months ago.<br>设为 true 可查询 6 个月前的归档数据。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin repay Record / 杠杆 还款 Record

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Rows. |
| rows[].amount | string |  | Total amount repaid<br>还款总额<br>例: `14.00000000` |
| rows[].asset | string |  | asset name<br>资产<br>例: `BNB` |
| rows[].interest | string |  | Interest repaid<br>支付的利息<br>例: `0.01866667` |
| rows[].principal | string |  | Principal repaid<br>支付的本金<br>例: `13.98133333` |
| rows[].status | string |  | one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account)<br>状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);<br>例: `CONFIRMED` |
| rows[].timestamp | integer (int64) |  | Timestamp.<br>例: `1563438204000` |
| rows[].txId | integer (int64) |  | Tx ID.<br>例: `2970933056` |
| total | integer (int64) |  | Total.<br>例: `1` |

## Query Portfolio Margin Negative Balance Interest History (USER_DATA)（查询统一账户期货负余额收息历史 (USER_DATA)）

`GET /papi/v1/portfolio/interest-history`

Query interest history of negative balance for portfolio margin.

查询统一账户期货负余额收息历史

Operation ID: `queryPortfolioMarginNegativeBalanceInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| size | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Negative Balance Interest History / Portfolio 杠杆 Negative Balance 利息 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset name<br>资产<br>例: `USDT` |
| [].interest | string |  | interest amount<br>利息金额<br>例: `24.4440` |
| [].interestAccuredTime | integer (int64) |  | Interest Accured Time.<br>例: `1670227200000` |
| [].interestRate | string |  | daily interest rate<br>日利率<br>例: `0.0001164` |
| [].principal | string |  | Principal repaid<br>支付的本金<br>例: `210000` |

## Query UM Position Information (USER_DATA)（用户UM持仓风险 (USER_DATA)）

`GET /papi/v1/um/positionRisk`

Get current UM position information.

获取用户UM持仓风险

Operation ID: `queryUmPositionInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Position Information / UM 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].entryPrice | string |  | average entry price<br>持仓成本价<br>例: `0.00000` |
| [].leverage | string |  | current initial leverage<br>杠杆倍率<br>例: `10` |
| [].markPrice | string |  | Mark Price.<br>例: `6679.50671178` |
| [].maxNotionalValue | string |  | Max Notional Value.<br>例: `20000000` |
| [].positionAmt | string |  | position amount<br>例: `0.000` |
| [].notional | string |  | Notional.<br>例: `0` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].unRealizedProfit | string |  | Un Realized Profit.<br>例: `0.00000000` |
| [].liquidationPrice | string |  | Liquidation Price.<br>例: `6170.20509059` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1625474304765` |

## Query User Negative Balance Auto Exchange Record (USER_DATA)（查询用户负余额自动兑换记录 (USER_DATA)）

`GET /papi/v1/portfolio/negative-balance-exchange-record`

Query user negative balance auto exchange record

查询用户负余额自动兑换记录

Operation ID: `queryUserNegativeBalanceAutoExchangeRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) | 是 | 例: `1623319461670` |
| endTime | query | integer (int64) | 是 | 例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Negative Balance Auto Exchange Record / 用户 Negative Balance Auto Exchange Record

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total.<br>例: `2` |
| rows | object[] |  | Rows. |
| rows[].startTime | integer (int64) |  | Start Time.<br>例: `1736263046841` |
| rows[].endTime | integer (int64) |  | End Time.<br>例: `1736263248179` |
| rows[].details | object[] |  | Details. |
| rows[].details[].asset | string |  | asset name<br>资产<br>例: `ETH` |
| rows[].details[].negativeBalance | number (float) |  | negative balance amount<br>当前负余额值<br>例: `1.10264488` |
| rows[].details[].negativeMaxThreshold | integer (int64) |  | the max negative balance threshold<br>该资产触发自动兑换的阈值<br>例: `5` |

## Query User Rate Limit (USER_DATA)（查询用户下单限频 (USER_DATA)）

`GET /papi/v1/rateLimit/order`

Query User Rate Limit

查询用户下单限频

Operation ID: `queryUserRateLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Rate Limit / 用户 频率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].rateLimitType | string |  | Rate Limit Type.<br>例: `ORDERS` |
| [].interval | string |  | Interval.<br>例: `MINUTE` |
| [].intervalNum | integer (int64) |  | Interval Num.<br>例: `1` |
| [].limit | integer (int64) |  | Limit.<br>例: `1200` |

## Repay futures Negative Balance (USER_DATA)（清还合约负余额 (USER_DATA)）

`POST /papi/v1/repay-futures-negative-balance`

Repay futures Negative Balance

清还合约负余额

Operation ID: `repayFuturesNegativeBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Repay futures Negative Balance / 还款 合约 Negative Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | Msg.<br>例: `success` |

## UM Futures Account Configuration (USER_DATA)（账户配置 (USER_DATA)）

`GET /papi/v1/um/accountConfig`

Query UM Futures account configuration

查询UM 合约 账户 configuration

Operation ID: `umFuturesAccountConfiguration`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Futures Account Configuration / UM 合约 账户 Configuration

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeTier | integer (int64) |  | account commission tier<br>费率等级<br>例: `0` |
| canTrade | boolean |  | if can trade<br>是否可以交易<br>例: `True` |
| canDeposit | boolean |  | if can transfer in asset<br>是否可以存款<br>例: `True` |
| canWithdraw | boolean |  | if can transfer out asset<br>是否可以提现<br>例: `True` |
| dualSidePosition | boolean |  | "true": Hedge Mode; "false": One-way Mode<br>"true": 双向持仓模式；"false": 单向持仓模式<br>例: `True` |
| updateTime | integer (int64) |  | reserved property, please ignore<br>忽略<br>例: `1724416653850` |
| multiAssetsMargin | boolean |  | Multi Assets Margin.<br>例: `False` |
| tradeGroupId | integer (int64) |  | Trade Group ID.<br>例: `-1` |

## UM Futures Symbol Configuration (USER_DATA)（交易对配置 (USER_DATA)）

`GET /papi/v1/um/symbolConfig`

Get current UM account symbol configuration.

查询UM合约交易对上的基础配置

Operation ID: `umFuturesSymbolConfiguration`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Futures Symbol Configuration / UM 合约 交易对 Configuration

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].marginType | string |  | Margin Type.<br>例: `CROSSED` |
| [].isAutoAddMargin | string |  | Is Auto Add Margin.<br>例: `false` |
| [].leverage | integer (int64) |  | current initial leverage<br>杠杆倍率<br>例: `21` |
| [].maxNotionalValue | string |  | Max Notional Value.<br>例: `1000000` |

## UM Notional and Leverage Brackets (USER_DATA)（查询UM杠杆分层标准 (USER_DATA)）

`GET /papi/v1/um/leverageBracket`

Query UM notional and leverage brackets

查询UM杠杆分层标准

Operation ID: `umNotionalAndLeverageBrackets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `ETHUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Notional and Leverage Brackets / UM Notional 和 Leverage Brackets

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `ETHUSDT` |
| [].notionalCoef | string |  | Notional Coef.<br>例: `4.0` |
| [].brackets | object[] |  | Brackets. |
| [].brackets[].bracket | integer (int64) |  | Notional bracket<br>层级<br>例: `1` |
| [].brackets[].initialLeverage | integer (int64) |  | Max initial leverage for this bracket<br>该层允许的最高初始杠杆倍数<br>例: `75` |
| [].brackets[].notionalCap | integer (int64) |  | Cap notional of this bracket<br>该层对应的数量上限<br>例: `10000` |
| [].brackets[].notionalFloor | integer (int64) |  | Notional threshold of this bracket<br>该层对应的数量下限<br>例: `0` |
| [].brackets[].maintMarginRatio | number (float) |  | Maintenance ratio for this bracket<br>该层对应的维持保证金率<br>例: `0.0065` |
| [].brackets[].cum | integer (int64) |  | Auxiliary number for quick calculation<br>速算数<br>例: `0` |

## Test Connectivity（测试服务器连通性 PING）

`GET /papi/v1/ping`

Test connectivity to the Rest API.

测试能否联通

Operation ID: `testConnectivity`

### 响应 200：OK / 成功

## Cancel All CM Open Conditional Orders (TRADE)（取消全部CM条件单 (TRADE)）

`DELETE /papi/v1/cm/conditional/allOpenOrders`

Cancel All CM Open Conditional Orders

取消全部CM条件单

Operation ID: `cancelAllCmOpenConditionalOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All CM Open Conditional Orders / 取消All CM 未完成Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `The operation of cancel all conditional open order is done.` |

## Cancel All CM Open Orders (TRADE)（撤销全部CM订单 (TRADE)）

`DELETE /papi/v1/cm/allOpenOrders`

Cancel all active LIMIT orders on specific symbol

撤销特定交易对全部CM订单

Operation ID: `cancelAllCmOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All CM Open Orders / 取消All CM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `The operation of cancel all open order is done.` |

## Cancel All UM Open Orders (TRADE)（撤销全部UM订单 (TRADE)）

`DELETE /papi/v1/um/allOpenOrders`

Cancel all active LIMIT orders on specific symbol

撤销特定交易对全部UM订单

Operation ID: `cancelAllUmOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All UM Open Orders / 取消All UM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `The operation of cancel all open order is done.` |

## New CM Conditional Order (TRADE)（CM条件单下单 (TRADE)）

`POST /papi/v1/cm/conditional/order`

New CM Conditional Order

CM条件单下单

Operation ID: `newCmConditionalOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| side | string | 是 | Side<br>方向<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>默认: `BOTH`<br>例: `BOTH` |
| strategyType | string | 是 | 枚举: `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `STOP` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| quantity | number (float) |  | 例: `1.0` |
| reduceOnly | string |  | "true" or "false". default "false". Cannot be sent in Hedge Mode<br>`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数<br>默认: `false`<br>例: `true` |
| price | number (float) |  | 例: `1.0` |
| workingType | string |  | stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"<br>stopPrice 触发类型: `MARK_PRICE`, `CONTRACT_PRICE`. 默认 `CONTRACT_PRICE`<br>枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| priceProtect | string |  | "true" or "false", default "false". Used with `STOP`/`STOP_MARKET` or `TAKE_PROFIT`/`TAKE_PROFIT_MARKET` orders<br>条件单触发保护："true" or "false", 默认 "false". `STOP`/`STOP_MARKET` or `TAKE_PROFIT`/`TAKE_PROFIT_MARKET` 需要此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| newClientStrategyId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br>例: `1` |
| stopPrice | number (float) |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>Used 带 `STOP/STOP_MARKET` 或 `TAKE_PROFIT/TAKE_PROFIT_MARKET` 订单.<br>例: `1.0` |
| activationPrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders.<br>`TRAILING_STOP_MARKET` 单使用，默认标记价格<br>例: `1.0` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders.<br>`TRAILING_STOP_MARKET` 单使用, 最小0.1, 最大5，1代表1%<br>例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New CM Conditional Order / New CM Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| newClientStrategyId | string |  | New Client Strategy ID.<br>例: `testOrder` |
| strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| strategyStatus | string |  | Strategy Status.<br>例: `NEW` |
| strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| origQty | string |  | Orig Qty.<br>例: `10` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| pair | string |  | Pair.<br>例: `BTCUSD` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |
| bookTime | integer (int64) |  | order place time<br>条件单下单时间<br>例: `1566818724710` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| workingType | string |  | Working Type.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | Price Protect.<br>例: `False` |

## Cancel CM Conditional Order (TRADE)（取消CM条件订单 (TRADE)）

`DELETE /papi/v1/cm/conditional/order`

Cancel CM Conditional Order

取消CM条件订单

Operation ID: `cancelCmConditionalOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| strategyId | query | integer (int64) |  | 例: `1` |
| newClientStrategyId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel CM Conditional Order / 取消CM Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| newClientStrategyId | string |  | New Client Strategy ID.<br>例: `myOrder1` |
| strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| strategyStatus | string |  | Strategy Status.<br>例: `CANCELED` |
| strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| origQty | string |  | Orig Qty.<br>例: `11` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |
| bookTime | integer (int64) |  | order place time<br>条件单下单时间<br>例: `1566818724710` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| workingType | string |  | Working Type.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | Price Protect.<br>例: `False` |

## Query CM Order (USER_DATA)（查询CM订单 (USER_DATA)）

`GET /papi/v1/cm/order`

Check an CM order's status.

查询CM订单状态

Operation ID: `queryCmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Order / CM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Avg Price.<br>例: `0.0` |
| clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| cumBase | string |  | Cum Base.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| origType | string |  | Orig Type.<br>例: `LIMIT` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| pair | string |  | Pair.<br>例: `BTCUSD` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| time | integer (int64) |  | order time<br>例: `1579276756075` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | update time<br>例: `1579276756075` |

## New CM Order (TRADE)（CM下单 (TRADE)）

`POST /papi/v1/cm/order`

Place new CM order

CM下单

Operation ID: `newCmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| side | string | 是 | Side<br>方向<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>默认: `BOTH`<br>例: `BOTH` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`<br>例: `LIMIT` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| quantity | number (float) |  | Place amount<br>下单数量<br>例: `1.0` |
| reduceOnly | string |  | "true" or "false". Cannot be sent in Hedge Mode.<br>`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| price | number (float) |  | Order price<br>委托价格<br>例: `1.0` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`<br>`OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br>用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br>例: `1` |
| newOrderRespType | string |  | "ACK", "RESULT", default "ACK"<br>`ACK`， `RESULT`，默认 `ACK`<br>枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New CM Order / New CM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order ID.<br>例: `testOrder` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `22542179` |
| origQty | string |  | Orig Qty.<br>例: `10` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| pair | string |  | Pair.<br>例: `BTCUSD` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `MARKET` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |

## Modify CM Order (TRADE)（修改CM订单 (TRADE)）

`PUT /papi/v1/cm/order`

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

修改CM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

Operation ID: `modifyCmOrder`

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
| quantity | number (float) | 是 | Order quantity<br>下单数量<br>例: `1.0` |
| price | number (float) | 是 | Order price<br>委托价格<br>例: `1.0` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`<br>`OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify CM Order / Modify CM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20072994037` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_PERP` |
| pair | string |  | Pair.<br>例: `BTCUSD` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| clientOrderId | string |  | Client Order ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| price | string |  | Price.<br>例: `30005` |
| origQty | string |  | Orig Qty.<br>例: `1` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `LONG` |
| origType | string |  | Orig Type.<br>例: `LIMIT` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1629182711600` |

## Cancel CM Order (TRADE)（撤销CM订单 (TRADE)）

`DELETE /papi/v1/cm/order`

Cancel an active LIMIT order

撤销CM订单

Operation ID: `cancelCmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel CM Order / 取消CM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order ID.<br>例: `myOrder1` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `283194212` |
| origQty | string |  | Orig Qty.<br>例: `2` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| pair | string |  | Pair.<br>例: `BTCUSD` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1571110484038` |

## Cancel Margin Account All Open Orders on a Symbol (TRADE)（杠杆账户撤销单一交易对的所有挂单 (TRADE)）

`DELETE /papi/v1/margin/allOpenOrders`

Cancel Margin Account All Open Orders on a Symbol

杠杆账户撤销单一交易对的所有挂单

Operation ID: `cancelMarginAccountAllOpenOrdersOnASymbol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Margin Account All Open Orders on a Symbol / 取消杠杆 账户 All 未完成订单 on a 交易对

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].origClientOrderId | string |  | Orig Client Order ID.<br>例: `E6APeyTJvkMvLMYMqu1KQ4` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `11` |
| [].orderListId | integer (int64) |  | Order List ID.<br>例: `-1` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `pXLV6Hz6mprAcVYpVMTGgx` |
| [].price | string |  | Price.<br>例: `0.089853` |
| [].origQty | string |  | Orig Qty.<br>例: `0.178622` |
| [].executedQty | string |  | Executed Qty.<br>例: `0.000000` |
| [].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.000000` |
| [].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| [].listStatusType | string |  | List Status Type.<br>例: `ALL_DONE` |
| [].listOrderStatus | string |  | List Order Status.<br>例: `ALL_DONE` |
| [].listClientOrderId | string |  | List Client Order ID.<br>例: `2inzWQdDvZLHbbAmAozX2N` |
| [].transactionTime | integer (int64) |  | Transaction Time.<br>例: `1585230948299` |
| [].orders | object[] |  | Orders. |
| [].orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20` |
| [].orders[].clientOrderId | string |  | Client Order ID.<br>例: `CwOOIPHSmYywx6jZX77TdL` |
| [].orderReports | object[] |  | Order Reports. |
| [].orderReports[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].orderReports[].origClientOrderId | string |  | Orig Client Order ID.<br>例: `CwOOIPHSmYywx6jZX77TdL` |
| [].orderReports[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20` |
| [].orderReports[].orderListId | integer (int64) |  | Order List ID.<br>例: `1929` |
| [].orderReports[].clientOrderId | string |  | Client Order ID.<br>例: `pXLV6Hz6mprAcVYpVMTGgx` |
| [].orderReports[].price | string |  | Price.<br>例: `0.668611` |
| [].orderReports[].origQty | string |  | Orig Qty.<br>例: `0.690354` |
| [].orderReports[].executedQty | string |  | Executed Qty.<br>例: `0.000000` |
| [].orderReports[].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.000000` |
| [].orderReports[].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| [].orderReports[].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].orderReports[].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `STOP_LOSS_LIMIT` |
| [].orderReports[].side | string |  | Side.<br>例: `BUY` |
| [].orderReports[].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `0.378131` |
| [].orderReports[].icebergQty | string |  | Iceberg Qty.<br>例: `0.017083` |

## Query Margin Account's OCO (USER_DATA)（查询杠杆账户 OCO (USER_DATA)）

`GET /papi/v1/margin/orderList`

Retrieves a specific OCO based on provided optional parameters

根据提供的可选参数检索特定的杠杆账户 OCO 订单。

Operation ID: `queryMarginAccountsOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderListId | query | integer (int64) |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| origClientOrderId | query | string |  | `orderListId` or `listClientOrderId` must be provided.<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's OCO / 杠杆 账户's OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | Order List ID.<br>例: `27` |
| contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| listStatusType | string |  | List Status Type.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | List Order Status.<br>例: `EXECUTING` |
| listClientOrderId | string |  | List Client Order ID.<br>例: `h2USkA5YQpaXHPIrkd96xE` |
| transactionTime | integer (int64) |  | Transaction Time.<br>例: `1565245656253` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orders | object[] |  | Orders. |
| orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `4` |
| orders[].clientOrderId | string |  | Client Order ID.<br>例: `qD1gy3kc3Gx0rihm9Y3xwS` |

## Cancel Margin Account OCO Orders (TRADE)（取消杠杆账户OCO订单 (TRADE)）

`DELETE /papi/v1/margin/orderList`

Cancel Margin Account OCO Orders

取消杠杆账户订单。

Operation ID: `cancelMarginAccountOcoOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `LTCBTC` |
| orderListId | query | integer (int64) |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| listClientOrderId | query | string |  | Either `orderListId` or `listClientOrderId` must be provided<br>`orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| newClientOrderId | query | string |  | Used to uniquely identify this cancel request.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值<br>例: `1` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Margin Account OCO Orders / 取消杠杆 账户 OCO 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | Order List ID.<br>例: `0` |
| contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| listStatusType | string |  | List Status Type.<br>例: `ALL_DONE` |
| listOrderStatus | string |  | List Order Status.<br>例: `ALL_DONE` |
| listClientOrderId | string |  | List Client Order ID.<br>例: `C3wyj4WVEktd7u9aVBRXcN` |
| transactionTime | integer (int64) |  | Transaction Time.<br>例: `1574040868128` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orders | object[] |  | Orders. |
| orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `2` |
| orders[].clientOrderId | string |  | Client Order ID.<br>例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports | object[] |  | Order Reports. |
| orderReports[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orderReports[].origClientOrderId | string |  | Orig Client Order ID.<br>例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `2` |
| orderReports[].orderListId | integer (int64) |  | Order List ID.<br>例: `0` |
| orderReports[].clientOrderId | string |  | Client Order ID.<br>例: `unfWT8ig8i0uj6lPuYLez6` |
| orderReports[].price | string |  | Price.<br>例: `1.00000000` |
| orderReports[].origQty | string |  | Orig Qty.<br>例: `10.00000000` |
| orderReports[].executedQty | string |  | Executed Qty.<br>例: `0.00000000` |
| orderReports[].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.00000000` |
| orderReports[].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| orderReports[].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| orderReports[].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `STOP_LOSS_LIMIT` |
| orderReports[].side | string |  | Side.<br>例: `SELL` |
| orderReports[].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `1.00000000` |

## Query Margin Account Order (USER_DATA)（查询杠杆账户订单 (USER_DATA)）

`GET /papi/v1/margin/order`

Query Margin Account Order

查询杠杆账户订单

Operation ID: `queryMarginAccountOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Order / 杠杆 账户 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order ID.<br>例: `ZwfQzuDIGpceVhKW5DvCmO` |
| cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.00000000` |
| executedQty | string |  | Executed Qty.<br>例: `0.00000000` |
| icebergQty | string |  | Iceberg Qty.<br>例: `0.00000000` |
| isWorking | boolean |  | Is Working.<br>例: `True` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `213205622` |
| origQty | string |  | Orig Qty.<br>例: `0.30000000` |
| price | string |  | Price.<br>例: `0.00493630` |
| side | string |  | Side.<br>例: `SELL` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `0.00000000` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BNBBTC` |
| time | integer (int64) |  | Event time.<br>时间。<br>例: `1562133008725` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1562133008725` |
| accountId | integer (int64) |  | Account ID.<br>例: `152950866` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_TAKER` |
| preventedMatchId | string |  | Prevented Match ID.<br>例: `null` |
| preventedQuantity | string |  | Prevented Quantity.<br>例: `null` |

## New Margin Order (TRADE)（杠杆账户下单 (TRADE)）

`POST /papi/v1/margin/order`

New Margin Order

杠杆账户下单

Operation ID: `newMarginOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| quantity | number (float) |  | 例: `1.0` |
| quoteOrderQty | number (float) |  | 例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>与 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`，和 `TAKE_PROFIT_LIMIT` 订单一起使用<br>例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br>客户自定义的唯一订单ID。若未发送自动生成。<br>例: `1` |
| newOrderRespType | string |  | Set the response JSON. ACK, RESULT, or FULL.<br>设置响应: JSON。 `ACK`， `RESULT`， 或 `FULL`; `MARKET` 和 `LIMIT` 订单类型默认为 `FULL`， 所有其他订单默认为 `ACK`<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order<br>与 `LIMIT`， `STOP_LOSS_LIMIT`，和 `TAKE_PROFIT_LIMIT` 一起使用创建 iceberg 订单<br>例: `1.0` |
| sideEffectType | string |  | 枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY`, `AUTO_BORROW_REPAY`<br>默认: `NO_SIDE_EFFECT`<br>例: `NO_SIDE_EFFECT` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| selfTradePreventionMode | string |  | `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers<br>允许的 ENUM 取决于交易对的配置。支持的值有 EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>例: `NONE` |
| autoRepayAtCancel | boolean |  | Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repaid after the order is cancelled.<br>只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true<br>枚举: `True`, `False`<br>默认: `True`<br>例: `True` |
| recvWindow | integer (int64) |  | The value cannot be greater than `60000`<br>赋值不能超过 `60000`<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Margin Order / New 杠杆 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `28` |
| clientOrderId | string |  | Client Order ID.<br>例: `6gCrw2kRUAF9CvJDGP16IP` |
| transactTime | integer (int64) |  | Transact Time.<br>例: `1507725176595` |
| price | string |  | Price.<br>例: `1.00000000` |
| origQty | string |  | Orig Qty.<br>例: `10.00000000` |
| executedQty | string |  | Executed Qty.<br>例: `10.00000000` |
| cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `10.00000000` |
| status | string |  | Status.<br>订单状态<br>例: `FILLED` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `MARKET` |
| side | string |  | Side.<br>例: `SELL` |
| marginBuyBorrowAmount | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `5` |
| marginBuyBorrowAsset | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `BTC` |
| fills | object[] |  | Fills. |
| fills[].price | string |  | Price.<br>例: `4000.00000000` |
| fills[].qty | string |  | Qty.<br>例: `1.00000000` |
| fills[].commission | string |  | Commission.<br>例: `4.00000000` |
| fills[].commissionAsset | string |  | Commission Asset.<br>例: `USDT` |

## Cancel Margin Account Order (TRADE)（杠杆账户撤销订单 (TRADE)）

`DELETE /papi/v1/margin/order`

Cancel Margin Account Order

杠杆账户撤销订单

Operation ID: `cancelMarginAccountOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `LTCBTC` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| newClientOrderId | query | string |  | Used to uniquely identify this cancel request.<br>用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值<br>例: `1` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`<br>赋值不能超过 `60000`<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Margin Account Order / 取消杠杆 账户 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `28` |
| origClientOrderId | string |  | Orig Client Order ID.<br>例: `myOrder1` |
| clientOrderId | string |  | Client Order ID.<br>例: `cancelMyOrder1` |
| price | string |  | Price.<br>例: `1.00000000` |
| origQty | string |  | Orig Qty.<br>例: `10.00000000` |
| executedQty | string |  | Executed Qty.<br>例: `8.00000000` |
| cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `8.00000000` |
| status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| side | string |  | Side.<br>例: `SELL` |

## Query UM Order (USER_DATA)（查询UM订单 (USER_DATA)）

`GET /papi/v1/um/order`

Check an UM order's status.

查询UM订单状态

Operation ID: `queryUmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Order / UM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Avg Price.<br>例: `0.00000` |
| clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| cumQuote | string |  | Cum Quote.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| origType | string |  | Orig Type.<br>例: `LIMIT` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| time | integer (int64) |  | order time<br>例: `1579276756075` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | update time<br>例: `1579276756075` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## New UM Order (TRADE)（UM下单 (TRADE)）

`POST /papi/v1/um/order`

Place new UM order

UM下单

Operation ID: `newUmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>默认: `BOTH`<br>例: `BOTH` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`<br>例: `LIMIT` |
| timeInForce | string |  | Valid values<br>有效方法<br>枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`<br>例: `GTC` |
| quantity | number (float) |  | Place amount<br>下单数量<br>例: `1.0` |
| reduceOnly | string |  | "true" or "false". default "false". Cannot be sent in Hedge Mode .<br>`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| price | number (float) |  | Order price<br>委托价格<br>例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br>用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br>例: `1` |
| newOrderRespType | string |  | `ACK`, `RESULT`, default `ACK`<br>`ACK`， `RESULT`，默认 `ACK`<br>枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`<br>`OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers<br>EXPIRE_TAKER/ EXPIRE_MAKER/ EXPIRE_BOTH； 默认EXPIRE_MAKER<br>枚举: `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000Mode. It must be sent in Hedge Mode.<br>TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000<br>例: `1770736694138` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New UM Order / New UM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order ID.<br>例: `testOrder` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `22542179` |
| origQty | string |  | Orig Qty.<br>例: `10` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| timeInForce | string |  | Time In Force.<br>例: `GTD` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `MARKET` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>//订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>订单TIF为GTD时的自动取消时间<br>例: `1693207680000` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## Modify UM Order (TRADE)（修改UM订单 (TRADE)）

`PUT /papi/v1/um/order`

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

修改UM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

Operation ID: `modifyUmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| symbol | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | Order quantity<br>下单数量<br>例: `1.0` |
| price | number (float) | 是 | Order price<br>委托价格<br>例: `1.0` |
| priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`<br>`OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Modify UM Order / Modify UM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20072994037` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| clientOrderId | string |  | Client Order ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| price | string |  | Price.<br>例: `30005` |
| origQty | string |  | Orig Qty.<br>例: `1` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `LONG` |
| origType | string |  | Orig Type.<br>例: `LIMIT` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1629182711600` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## Cancel UM Order (TRADE)（撤销UM订单 (TRADE)）

`DELETE /papi/v1/um/order`

Cancel an active UM LIMIT order

撤销UM订单

Operation ID: `cancelUmOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel UM Order / 取消UM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | Client Order ID.<br>例: `myOrder1` |
| cumQty | string |  | Cum Qty.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `4611875134427365000` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1571110484038` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## CM Account Trade List (USER_DATA)（CM账户成交历史 (USER_DATA)）

`GET /papi/v1/cm/userTrades`

Get trades for a specific account and CM symbol.

获取CM成交历史

权重: - 20 with `symbol`
- 40 with `pair`

Operation ID: `cmAccountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_200626` |
| pair | query | string |  | 例: `BTCUSD` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| fromId | query | integer (int64) |  | Trade ID to fetch from.<br>起始成交 ID。<br>例: `1` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `50`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Account Trade List / CM 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200626` |
| [].id | integer (int64) |  | ID.<br>例: `6` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `28` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].price | string |  | Price.<br>例: `8800` |
| [].qty | string |  | Qty.<br>例: `1` |
| [].realizedPnl | string |  | Realized Pnl.<br>例: `0` |
| [].marginAsset | string |  | Margin Asset.<br>例: `BTC` |
| [].baseQty | string |  | Base Qty.<br>例: `0.01136364` |
| [].commission | string |  | Commission.<br>例: `0.00000454` |
| [].commissionAsset | string |  | Commission Asset.<br>例: `BTC` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1590743483586` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| [].buyer | boolean |  | Buyer.<br>例: `False` |
| [].maker | boolean |  | Maker.<br>例: `False` |

## CM Position ADL Quantile Estimation (USER_DATA)（CM持仓ADL队列估算 (USER_DATA)）

`GET /papi/v1/cm/adlQuantile`

Query CM Position ADL Quantile Estimation
* Values update every 30s.
* Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
* For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
* If the positions of the symbol are crossed margined in Hedge Mode:
* "HEDGE" as a sign will be returned instead of "BOTH";
* A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.

CM持仓ADL队列估算
* 每30秒更新数据
* 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
* 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
* 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。

Operation ID: `cmPositionAdlQuantileEstimation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_201225` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Position ADL Quantile Estimation / CM 持仓 ADL Quantile Estimation

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_201225` |
| [].adlQuantile | object |  | Adl Quantile. |
| [].adlQuantile.LONG | integer (int64) |  | adl quantile for "LONG" position in hedge mode<br>双开模式下多头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.SHORT | integer (int64) |  | adl qauntile for "SHORT" position in hedge mode<br>双开模式下空头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.HEDGE | integer (int64) |  | only a sign, ignore the value<br>HEDGE 仅作为指示出现，请忽略数值<br>例: `0` |
| [].adlQuantile.BOTH | integer (int64) |  | adl qunatile for position in one-way mode<br>单开模式下持仓的ADL队列估算分<br>例: `0` |

## Get UM Futures BNB Burn Status (USER_DATA)（获取UM BNB抵扣开关状态 (USER_DATA)）

`GET /papi/v1/um/feeBurn`

Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )

查询用户 ***所有 symbol*** UM合约交易BNB抵扣开关状态(手续费抵扣开或关)

Operation ID: `getUmFuturesBnbBurnStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get UM Futures BNB Burn Status / 获取UM 合约 BNB Burn 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeBurn | boolean |  | "true": Fee Discount On; "false": Fee Discount Off<br>"true": 手续费抵扣开; "false": 手续费抵扣关<br>例: `True` |

## Toggle BNB Burn On UM Futures Trade (TRADE)（UM合约交易BNB抵扣开关 (TRADE)）

`POST /papi/v1/um/feeBurn`

Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***

改变用户 ***所有 symbol*** UM合约交易BNB抵扣开关(手续费抵扣开或关)

Operation ID: `toggleBnbBurnOnUmFuturesTrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| feeBurn | string | 是 | "true": Fee Discount On; "false": Fee Discount Off<br>"true": 手续费抵扣开; "false": 手续费抵扣关<br>枚举: `true`, `false`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Toggle BNB Burn On UM Futures Trade / Toggle BNB Burn On UM 合约 交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | Code.<br>例: `200` |
| msg | string |  | Msg.<br>例: `success` |

## Margin Account Borrow (MARGIN)（杠杆账户借贷 (MARGIN)）

`POST /papi/v1/marginLoan`

Apply for a margin loan.

申请借贷

Operation ID: `marginAccountBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Borrow / 杠杆 账户 借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | Transaction ID.<br>交易ID。<br>例: `100000001` |

## Margin Account New OCO (TRADE)（杠杆账户 OCO 下单 (TRADE)）

`POST /papi/v1/margin/order/oco`

Send in a new OCO for a margin account

杠杆账户发送新 OCO 订单

Operation ID: `marginAccountNewOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `LTCBTC` |
| listClientOrderId | string |  | A unique Id for the entire orderList<br>整个 orderList 的唯一 ID<br>例: `1` |
| side | string | 是 | See enum definitions: order side<br>详见枚举定义：订单方向<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | 例: `1.0` |
| limitClientOrderId | string |  | A unique Id for the limit order<br>限价单的唯一 ID<br>例: `1` |
| price | number (float) | 是 | 例: `1.0` |
| limitIcebergQty | number (float) |  | 例: `1.0` |
| stopClientOrderId | string |  | A unique Id for the stop loss/stop loss limit leg<br>止损/止损限价单的唯一 ID<br>例: `1` |
| stopPrice | number (float) | 是 | 例: `1.0` |
| stopLimitPrice | number (float) |  | If provided, stopLimitTimeInForce is required.<br>如果提供，须配合提交`stopLimitTimeInForce`<br>例: `1.0` |
| stopIcebergQty | number (float) |  | 例: `1.0` |
| stopLimitTimeInForce | string |  | Valid values are `GTC/FOK/IOC`<br>有效值 `GTC/FOK/IOC`<br>枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| newOrderRespType | string |  | Set the response JSON.<br>详见枚举定义：订单返回类型<br>枚举: `ACK`, `RESULT`<br>例: `ACK` |
| sideEffectType | string |  | NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.<br>NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; 默认为 NO_SIDE_EFFECT<br>枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY`<br>默认: `NO_SIDE_EFFECT`<br>例: `NO_SIDE_EFFECT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account New OCO / 杠杆 账户 New OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | Order List ID.<br>例: `0` |
| contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| listStatusType | string |  | List Status Type.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | List Order Status.<br>例: `EXECUTING` |
| listClientOrderId | string |  | List Client Order ID.<br>例: `JYVpp3F0f5CAG15DhtrqLp` |
| transactionTime | integer (int64) |  | Transaction Time.<br>例: `1563417480525` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| marginBuyBorrowAmount | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `5` |
| marginBuyBorrowAsset | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `BTC` |
| orders | object[] |  | Orders. |
| orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `2` |
| orders[].clientOrderId | string |  | Client Order ID.<br>例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports | object[] |  | Order Reports. |
| orderReports[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `2` |
| orderReports[].orderListId | integer (int64) |  | Order List ID.<br>例: `0` |
| orderReports[].clientOrderId | string |  | Client Order ID.<br>例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports[].transactTime | integer (int64) |  | Transact Time.<br>例: `1563417480525` |
| orderReports[].price | string |  | Price.<br>例: `0.000000` |
| orderReports[].origQty | string |  | Orig Qty.<br>例: `0.624363` |
| orderReports[].executedQty | string |  | Executed Qty.<br>例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.000000` |
| orderReports[].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| orderReports[].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| orderReports[].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `STOP_LOSS` |
| orderReports[].side | string |  | Side.<br>例: `BUY` |
| orderReports[].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `0.960664` |

## Margin Account Repay (MARGIN)（杠杆账户归还借贷 (MARGIN)）

`POST /papi/v1/repayLoan`

Repay for a margin loan.

获取杠杆账户归还借贷

Operation ID: `marginAccountRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过`60000`<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Repay / 杠杆 账户 还款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | Transaction ID.<br>交易ID。<br>例: `100000001` |

## Margin Account Repay Debt (TRADE)（杠杆账户还款 (TRADE)）

`POST /papi/v1/margin/repay-debt`

Repay debt for a margin loan.

杠杆账户还款

Operation ID: `marginAccountRepayDebt`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| amount | string |  | 例: `1.0` |
| specifyRepayAssets | string |  | Specific asset list to repay debt; Can be added in batch, separated by commas<br>指定还款资产，多资产用逗号分隔<br>例: `BNB` |
| recvWindow | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过`60000`<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Repay Debt / 杠杆 账户 还款 Debt

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | string |  | Amount repaid<br>还款金额<br>例: `0.10000000` |
| asset | string |  | asset name<br>资产<br>例: `BNB` |
| specifyRepayAssets | string[] |  | Specify Repay Assets. |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1636371437000` |
| success | boolean |  | Success.<br>例: `True` |

## Margin Account Trade List (USER_DATA)（查询杠杆账户交易历史 (USER_DATA)）

`GET /papi/v1/margin/myTrades`

Margin Account Trade List

查询杠杆账户交易历史

Operation ID: `marginAccountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| fromId | query | integer (int64) |  | Trade ID to fetch from.<br>起始成交 ID。<br>例: `1` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Trade List / 杠杆 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].commission | string |  | Commission.<br>例: `0.00006000` |
| [].commissionAsset | string |  | Commission Asset.<br>例: `BTC` |
| [].id | integer (int64) |  | ID.<br>例: `34` |
| [].isBestMatch | boolean |  | Is Best Match.<br>例: `True` |
| [].isBuyer | boolean |  | Is Buyer.<br>例: `False` |
| [].isMaker | boolean |  | Is Maker.<br>例: `False` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `39324` |
| [].price | string |  | Price.<br>例: `0.02000000` |
| [].qty | string |  | Qty.<br>例: `3.00000000` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BNBBTC` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1561973357171` |

## Query All CM Conditional Orders (USER_DATA)（查询CM所有条件订单(包括历史订单) (USER_DATA)）

`GET /papi/v1/cm/conditional/allOrders`

Query All CM Conditional Orders

查询CM所有条件订单（包括历史订单

权重: - 1 for a single `symbol`
- 40 when `symbol` is omitted

Operation ID: `queryAllCmConditionalOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| strategyId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All CM Conditional Orders / All CM Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].newClientStrategyId | string |  | New Client Strategy ID.<br>例: `abc` |
| [].strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| [].strategyStatus | string |  | Strategy Status.<br>例: `TRIGGERED` |
| [].strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `12123343534` |
| [].status | string |  | Normal order status after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单状态, 当条件单被触发后才有<br>例: `NEW` |
| [].bookTime | integer (int64) |  | order time<br>条件单下单时间<br>例: `1566818724710` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| [].triggerTime | integer (int64) |  | Trigger Time.<br>例: `1566818724750` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `MARKET` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |

## Query All CM Orders (USER_DATA)（查询所有CM订单(包括历史订单) (USER_DATA)）

`GET /papi/v1/cm/allOrders`

Get all account CM orders; active, canceled, or filled.

查询所有CM订单(包括历史订单)

权重: - 20 with `symbol`
- 40 with `pair`

Operation ID: `queryAllCmOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| pair | query | string |  | 例: `BTCUSD` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `50`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All CM Orders / All CM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>例: `0.0` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| [].cumBase | string |  | Cum Base.<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>例: `0` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].time | integer (int64) |  | order time<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | update time<br>例: `1579276756075` |

## Query All Current CM Open Conditional Orders (USER_DATA)（查看CM当前全部条件挂单 (USER_DATA)）

`GET /papi/v1/cm/conditional/openOrders`

Get all open conditional orders on a symbol. **Careful** when accessing this with no symbol.

查看CM当前全部条件挂单。 请小心使用不带symbol参数的调用

权重: - 1 for a single `symbol`
- 40 when `symbol` is omitted

Operation ID: `queryAllCurrentCmOpenConditionalOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Current CM Open Conditional Orders / All 当前 CM 未完成Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].newClientStrategyId | string |  | New Client Strategy ID.<br>例: `abc` |
| [].strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| [].strategyStatus | string |  | Strategy Status.<br>例: `NEW` |
| [].strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD` |
| [].bookTime | integer (int64) |  | order time<br>例: `1566818724710` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| [].priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |

## Query All Current CM Open Orders (USER_DATA)（查看当前全部CM挂单 (USER_DATA)）

`GET /papi/v1/cm/openOrders`

Get all open orders on a symbol.

* If the symbol is not sent, orders for all symbols will be returned in an array.

查看当前全部CM挂单，请小心使用不带symbol参数的调用

* 不带`symbol`参数，会返回所有交易对的挂单

权重: - 1 for a single `symbol`
- 40 when `symbol` is omitted

Operation ID: `queryAllCurrentCmOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSD_200925` |
| pair | query | string |  | 例: `BTCUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Current CM Open Orders / All 当前 CM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>例: `0.0` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| [].cumBase | string |  | Cum Base.<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>例: `0` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].time | integer (int64) |  | order time<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | update time<br>例: `1579276756075` |

## Query All Current UM Open Orders (USER_DATA)（查看当前全部UM挂单 (USER_DATA)）

`GET /papi/v1/um/openOrders`

Get all open orders on a symbol.

查看当前全部UM挂单，请小心使用不带symbol参数的调用

权重: - 1 for a single `symbol`
- 40 when `symbol` is omitted

Operation ID: `queryAllCurrentUmOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Current UM Open Orders / All 当前 UM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>例: `0.00000` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| [].cumQuote | string |  | Cum Quote.<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>例: `0` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].time | integer (int64) |  | order time<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | update time<br>例: `1579276756075` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| [].priceMatch | string |  | Price Match.<br>例: `NONE` |

## Query All Margin Account Orders (USER_DATA)（查询杠杆账户的所有订单 (USER_DATA)）

`GET /papi/v1/margin/allOrders`

Query All Margin Account Orders

查询杠杆账户的所有订单

Operation ID: `queryAllMarginAccountOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All Margin Account Orders / All 杠杆 账户 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client Order ID.<br>例: `D2KDy4DIeS56PvkM13f8cP` |
| [].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.00000000` |
| [].executedQty | string |  | Executed Qty.<br>例: `0.00000000` |
| [].icebergQty | string |  | Iceberg Qty.<br>例: `0.00000000` |
| [].isWorking | boolean |  | Is Working.<br>例: `False` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `41295` |
| [].origQty | string |  | Orig Qty.<br>例: `5.31000000` |
| [].price | string |  | Price.<br>例: `0.22500000` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `0.18000000` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BNBBTC` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1565769338806` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `TAKE_PROFIT_LIMIT` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1565769342148` |
| [].accountId | integer (int64) |  | Account ID.<br>例: `152950866` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_TAKER` |
| [].preventedMatchId | string |  | Prevented Match ID.<br>例: `null` |
| [].preventedQuantity | string |  | Prevented Quantity.<br>例: `null` |

## Query All UM Orders (USER_DATA)（查询所有UM订单(包括历史订单) (USER_DATA)）

`GET /papi/v1/um/allOrders`

Get all account UM orders; active, canceled, or filled.

查询所有UM订单

Operation ID: `queryAllUmOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：All UM Orders / All UM 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>例: `0.00000` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| [].cumQuote | string |  | Cum Quote.<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>例: `0` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].time | integer (int64) |  | order time<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | update time<br>例: `1579276756075` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| [].goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| [].priceMatch | string |  | Price Match.<br>例: `NONE` |

## Query CM Conditional Order History (USER_DATA)（查询CM条件单历史 (USER_DATA)）

`GET /papi/v1/cm/conditional/orderHistory`

Query CM Conditional Order History

查询CM条件单历史

Operation ID: `queryCmConditionalOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| strategyId | query | integer (int64) |  | 例: `1` |
| newClientStrategyId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Conditional Order History / CM Conditional 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| newClientStrategyId | string |  | New Client Strategy ID.<br>例: `abc` |
| strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| strategyStatus | string |  | Strategy Status.<br>例: `TRIGGERED` |
| strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable，only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `12123343534` |
| status | string |  | Normal order status after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单状态, 当条件单被触发后才有<br>例: `NEW` |
| bookTime | integer (int64) |  | order time<br>条件单下单时间<br>例: `1566818724710` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| triggerTime | integer (int64) |  | Trigger Time.<br>例: `1566818724750` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `MARKET` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |
| workingType | string |  | Working Type.<br>例: `CONTRACT_PRICE` |
| priceProtect | boolean |  | Price Protect.<br>例: `False` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## Query CM Modify Order History (TRADE)（查询CM订单修改历史 (TRADE)）

`GET /papi/v1/cm/orderAmendment`

Get order modification history

查询CM订单修改历史

Operation ID: `queryCmModifyOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：CM Modify Order History / CM Modify 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amendmentId | integer (int64) |  | Order modification ID<br>修改记录号<br>例: `5363` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_PERP` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20072994037` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].time | integer (int64) |  | Order modification time<br>修改时间<br>例: `1629184560899` |
| [].amendment | object |  | Amendment. |
| [].amendment.price | object |  | Price. |
| [].amendment.price.before | string |  | Before.<br>例: `30004` |
| [].amendment.price.after | string |  | After.<br>例: `30003.2` |
| [].amendment.origQty | object |  | Orig Qty. |
| [].amendment.origQty.before | string |  | Before.<br>例: `1` |
| [].amendment.origQty.after | string |  | After.<br>例: `1` |
| [].amendment.count | integer (int64) |  | Order modification count, representing the number of times the order has been modified<br>修改记数，代表该修改记录是这笔订单第几次修改<br>例: `3` |
| [].amendment.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `123` |

## Query Current CM Open Conditional Order (USER_DATA)（查询CM当前条件挂单 (USER_DATA)）

`GET /papi/v1/cm/conditional/openOrder`

Query Current CM Open Conditional Order

查询CM当前条件挂单

Operation ID: `queryCurrentCmOpenConditionalOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSD_200925` |
| strategyId | query | integer (int64) |  | 例: `1` |
| newClientStrategyId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current CM Open Conditional Order / 当前 CM 未完成Conditional 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| newClientStrategyId | string |  | New Client Strategy ID.<br>例: `abc` |
| strategyId | integer (int64) |  | Strategy ID.<br>例: `123445` |
| strategyStatus | string |  | Strategy Status.<br>例: `NEW` |
| strategyType | string |  | Strategy Type.<br>例: `TRAILING_STOP_MARKET` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `9300` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD` |
| bookTime | integer (int64) |  | order time<br>条件单下单时间<br>例: `1566818724710` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1566818724722` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>例: `9020` |
| priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>例: `0.3` |

## Query Current CM Open Order (USER_DATA)（查看当前全部CM挂单 (USER_DATA)）

`GET /papi/v1/cm/openOrder`

Query current CM open order

查看当前全部CM挂单，请小心使用不带symbol参数的调用

Operation ID: `queryCurrentCmOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Trading pair.<br>交易对。<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | Order ID.<br>订单ID。<br>例: `1917641` |
| origClientOrderId | query | string |  | User-defined order ID.<br>用户自定义订单ID。<br>例: `abc` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current CM Open Order / 当前 CM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].avgPrice | string |  | Avg Price.<br>例: `0.0` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| [].cumBase | string |  | Cum Base.<br>例: `0` |
| [].executedQty | string |  | Executed Qty.<br>例: `0` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| [].origQty | string |  | Orig Qty.<br>例: `0.40` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].price | string |  | Price.<br>例: `0` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `BUY` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].time | integer (int64) |  | order time<br>例: `1579276756075` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | update time<br>例: `1579276756075` |

## Query Current Margin Open Order (USER_DATA)（查询杠杆账户挂单记录 (USER_DATA)）

`GET /papi/v1/margin/openOrders`

Query Current Margin Open Order

查询杠杆账户挂单记录

Operation ID: `queryCurrentMarginOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Margin Open Order / 当前 杠杆 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | Client Order ID.<br>例: `qhcZw71gAkCCTv0t0k8LUK` |
| [].cummulativeQuoteQty | string |  | Cummulative Quote Qty.<br>例: `0.00000000` |
| [].executedQty | string |  | Executed Qty.<br>例: `0.00000000` |
| [].icebergQty | string |  | Iceberg Qty.<br>例: `0.00000000` |
| [].isWorking | boolean |  | Is Working.<br>例: `True` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `211842552` |
| [].origQty | string |  | Orig Qty.<br>例: `0.30000000` |
| [].price | string |  | Price.<br>例: `0.00475010` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].status | string |  | Status.<br>订单状态<br>例: `NEW` |
| [].stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>例: `0.00000000` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BNBBTC` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1562040170089` |
| [].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1562040170089` |
| [].accountId | integer (int64) |  | Account ID.<br>例: `152950866` |
| [].selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_TAKER` |
| [].preventedMatchId | string |  | Prevented Match ID.<br>例: `null` |
| [].preventedQuantity | string |  | Prevented Quantity.<br>例: `null` |

## Query Current UM Open Order (USER_DATA)（查询当前UM挂单 (USER_DATA)）

`GET /papi/v1/um/openOrder`

Query current UM open order

查询当前UM挂单

Operation ID: `queryCurrentUmOpenOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current UM Open Order / 当前 UM 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| avgPrice | string |  | Avg Price.<br>例: `0.00000` |
| clientOrderId | string |  | Client Order ID.<br>例: `abc` |
| cumQuote | string |  | Cum Quote.<br>例: `0` |
| executedQty | string |  | Executed Qty.<br>例: `0` |
| orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `1917641` |
| origQty | string |  | Orig Qty.<br>例: `0.40` |
| origType | string |  | Orig Type.<br>例: `LIMIT` |
| price | string |  | Price.<br>例: `0` |
| reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| side | string |  | Side.<br>例: `BUY` |
| positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `SHORT` |
| status | string |  | Status.<br>订单状态<br>例: `NEW` |
| symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| time | integer (int64) |  | order time<br>例: `1579276756075` |
| timeInForce | string |  | Time In Force.<br>例: `GTC` |
| type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1579276756075` |
| selfTradePreventionMode | string |  | self trading preventation mode<br>例: `EXPIRE_MAKER` |
| goodTillDate | integer (int64) |  | order pre-set auot cancel time for TIF GTD order<br>例: `0` |
| priceMatch | string |  | Price Match.<br>例: `NONE` |

## Query Margin Account's all OCO (USER_DATA)（查询特定杠杆账户所有 OCO (USER_DATA)）

`GET /papi/v1/margin/allOrderList`

Query all OCO for a specific margin account based on provided optional parameters

根据提供的可选参数检索特定杠杆账户所有的 OCO 订单。

Operation ID: `queryMarginAccountsAllOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| fromId | query | integer (int64) |  | Trade ID to fetch from.<br>起始成交 ID。<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `500` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's all OCO / 杠杆 账户's all OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | Order List ID.<br>例: `29` |
| [].contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| [].listStatusType | string |  | List Status Type.<br>例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | List Order Status.<br>例: `EXECUTING` |
| [].listClientOrderId | string |  | List Client Order ID.<br>例: `amEEAXryFzFwYF1FeRpUoZ` |
| [].transactionTime | integer (int64) |  | Transaction Time.<br>例: `1565245913483` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| [].orders | object[] |  | Orders. |
| [].orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `4` |
| [].orders[].clientOrderId | string |  | Client Order ID.<br>例: `oD7aesZqjEGlZrbtRpy5zB` |

## Query Margin Account's Open OCO (USER_DATA)（查询杠杆账户 OCO 挂单 (USER_DATA)）

`GET /papi/v1/margin/openOrderList`

Query Margin Account's Open OCO

查询杠杆账户 OCO 挂单

Operation ID: `queryMarginAccountsOpenOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Value cannot be greater than 60000<br>赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's Open OCO / 杠杆 账户's 未完成OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | Order List ID.<br>例: `31` |
| [].contingencyType | string |  | Contingency Type.<br>例: `OCO` |
| [].listStatusType | string |  | List Status Type.<br>例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | List Order Status.<br>例: `EXECUTING` |
| [].listClientOrderId | string |  | List Client Order ID.<br>例: `wuB13fmulKj3YjdqWEcsnp` |
| [].transactionTime | integer (int64) |  | Transaction Time.<br>例: `1565246080644` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| [].orders | object[] |  | Orders. |
| [].orders[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `4` |
| [].orders[].clientOrderId | string |  | Client Order ID.<br>例: `r3EH2N76dHfLoSZWIUw1bT` |

## Query UM Modify Order History (TRADE)（查询UM订单修改历史 (TRADE)）

`GET /papi/v1/um/orderAmendment`

Get order modification history

查询UM订单修改历史

Operation ID: `queryUmModifyOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| orderId | query | integer (int64) |  | Order ID<br>系统订单号<br>例: `1` |
| origClientOrderId | query | string |  | Client order ID<br>用户自定义的订单号<br>例: `1` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Modify Order History / UM Modify 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].amendmentId | integer (int64) |  | Order modification ID<br>修改记录号<br>例: `5363` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].pair | string |  | Pair.<br>例: `BTCUSDT` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `20072994037` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `LJ9R4QZDihCaS8UAOOLpgW` |
| [].time | integer (int64) |  | Order modification time<br>修改时间<br>例: `1629184560899` |
| [].amendment | object |  | Amendment. |
| [].amendment.price | object |  | Price. |
| [].amendment.price.before | string |  | Before.<br>例: `30004` |
| [].amendment.price.after | string |  | After.<br>例: `30003.2` |
| [].amendment.origQty | object |  | Orig Qty. |
| [].amendment.origQty.before | string |  | Before.<br>例: `1` |
| [].amendment.origQty.after | string |  | After.<br>例: `1` |
| [].amendment.count | integer (int64) |  | Order modification count, representing the number of times the order has been modified<br>修改记数，代表该修改记录是这笔订单第几次修改<br>例: `3` |
| [].amendment.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `123` |
| [].priceMatch | string |  | Price Match.<br>例: `NONE` |

## Query User's CM Force Orders (USER_DATA)（用户CM强平单历史 (USER_DATA)）

`GET /papi/v1/cm/forceOrders`

Query User's CM Force Orders

查询用户CM强平单历史

权重: - 20 with `symbol`
- 50 without `symbol`

Operation ID: `queryUsersCmForceOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| autoCloseType | query | string |  | `LIQUIDATION` for liquidation orders, `ADL` for ADL orders.<br>`LIQUIDATION`: 强平单, `ADL`: ADL 减仓单.<br>枚举: `LIQUIDATION`, `ADL`<br>例: `LIQUIDATION` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `50`<br>例: `500` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User's CM Force Orders / 用户's CM Force 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `165123080` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSD_200925` |
| [].pair | string |  | Pair.<br>例: `BTCUSD` |
| [].status | string |  | Status.<br>订单状态<br>例: `FILLED` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `autoclose-1596542005017000006` |
| [].price | string |  | Price.<br>例: `11326.9` |
| [].avgPrice | string |  | Avg Price.<br>例: `11326.9` |
| [].origQty | string |  | Orig Qty.<br>例: `1` |
| [].executedQty | string |  | Executed Qty.<br>例: `1` |
| [].cumBase | string |  | Cum Base.<br>例: `0.00882854` |
| [].timeInForce | string |  | Time In Force.<br>例: `IOC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1596542005019` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1596542005050` |

## Query User's Margin Force Orders (USER_DATA)（获取账户杠杆强制平仓记录 (USER_DATA)）

`GET /papi/v1/margin/forceOrders`

Query user's margin force orders

> **Note:** Portfolio Margin accounts liquidated through the [Risk-Based Liquidation Adjustment](https://www.binance.com/en/support/faq/detail/662268636eb44b71af55c6c6a597d481) flow will not have any order or trade records returned by this endpoint. Query the capital flow endpoint instead: [Query Cross Isolated Margin Capital Flow](https://developers.binance.com/en/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-isolated-margin-capital-flow).

获取账户杠杆强制平仓记录

> **注意：** 通过[强平中基于风险的清算调整机制](https://www.binance.com/zh-CN/support/faq/detail/662268636eb44b71af55c6c6a597d481)流程被强平的统一账户（Portfolio Margin），本接口不会返回任何订单或成交记录。请改为查询资金流水接口：[查询全仓/逐仓资金流水](https://developers.binance.com/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-isolated-margin-capital-flow)。

Operation ID: `queryUsersMarginForceOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number.<br>当前页码。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能大于 `60000`<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User's Margin Force Orders / 用户's 杠杆 Force 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Rows. |
| rows[].avgPrice | string |  | Avg Price.<br>例: `0.00388359` |
| rows[].executedQty | string |  | Executed Qty.<br>例: `31.39000000` |
| rows[].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `180015097` |
| rows[].price | string |  | Price.<br>例: `0.00388110` |
| rows[].qty | string |  | Qty.<br>例: `31.39000000` |
| rows[].side | string |  | Side.<br>例: `SELL` |
| rows[].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BNBBTC` |
| rows[].timeInForce | string |  | Time In Force.<br>例: `GTC` |
| rows[].updatedTime | integer (int64) |  | Updated Time.<br>例: `1558941374745` |
| total | integer (int64) |  | Total.<br>例: `1` |

## Query User's UM Force Orders (USER_DATA)（用户强平单历史 (USER_DATA)）

`GET /papi/v1/um/forceOrders`

Query User's UM Force Orders

查询用户UM强平单历史

权重: - 20 with `symbol`
- 50 without `symbol`

Operation ID: `queryUsersUmForceOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| autoCloseType | query | string |  | `LIQUIDATION` for liquidation orders, `ADL` for ADL orders.<br>`LIQUIDATION`: 强平单, `ADL`: ADL 减仓单.<br>枚举: `LIQUIDATION`, `ADL`<br>例: `LIQUIDATION` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `50`<br>例: `500` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than 60000<br>赋值不能超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User's UM Force Orders / 用户's UM Force 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `6071832819` |
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].status | string |  | Status.<br>订单状态<br>例: `FILLED` |
| [].clientOrderId | string |  | Client Order ID.<br>例: `autoclose-1596107620040000020` |
| [].price | string |  | Price.<br>例: `10871.09` |
| [].avgPrice | string |  | Avg Price.<br>例: `10913.21000` |
| [].origQty | string |  | Orig Qty.<br>例: `0.001` |
| [].executedQty | string |  | Executed Qty.<br>例: `0.001` |
| [].cumQuote | string |  | Cum Quote.<br>例: `10.91321` |
| [].timeInForce | string |  | Time In Force.<br>例: `IOC` |
| [].type | string |  | Normal order type after trigger if appliable<br>条件单触发后普通订单类型<br>例: `LIMIT` |
| [].reduceOnly | boolean |  | Reduce Only.<br>例: `False` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |
| [].origType | string |  | Orig Type.<br>例: `LIMIT` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1596107620044` |
| [].updateTime | integer (int64) |  | last update time<br>更新时间<br>例: `1596107620087` |

## UM Account Trade List (USER_DATA)（UM账户成交历史 (USER_DATA)）

`GET /papi/v1/um/userTrades`

Get trades for a specific account and UM symbol.

获取UM某交易对的成交历史

Operation ID: `umAccountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BTCUSDT` |
| startTime | query | integer (int64) |  | Timestamp in ms to get funding from INCLUSIVE.<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Timestamp in ms to get funding until INCLUSIVE.<br>结束时间<br>例: `1641782889000` |
| fromId | query | integer (int64) |  | Trade ID to fetch from.<br>起始成交 ID。<br>例: `1` |
| limit | query | integer (int64) |  | Number of results returned.<br>返回结果数量。<br>默认: `100`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Account Trade List / UM 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `BTCUSDT` |
| [].id | integer (int64) |  | ID.<br>例: `67880589` |
| [].orderId | integer (int64) |  | Normal orderID after trigger if appliable, only have when the strategy is triggered<br>条件单触发后普通单id，当条件单被触发后才有<br>例: `270093109` |
| [].side | string |  | Side.<br>例: `SELL` |
| [].price | string |  | Price.<br>例: `28511.00` |
| [].qty | string |  | Qty.<br>例: `0.010` |
| [].realizedPnl | string |  | Realized Pnl.<br>例: `2.58500000` |
| [].quoteQty | string |  | Quote Qty.<br>例: `285.11000` |
| [].commission | string |  | Commission.<br>例: `0.11404400` |
| [].commissionAsset | string |  | Commission Asset.<br>例: `USDT` |
| [].time | integer (int64) |  | Event time.<br>时间。<br>例: `1680688557875` |
| [].buyer | boolean |  | Buyer.<br>例: `False` |
| [].maker | boolean |  | Maker.<br>例: `False` |
| [].positionSide | string |  | BOTH means that it is the position of One-way Mode<br>例: `BOTH` |

## UM Position ADL Quantile Estimation (USER_DATA)（UM持仓ADL队列估算 (USER_DATA)）

`GET /papi/v1/um/adlQuantile`

Query UM Position ADL Quantile Estimation

* Values update every 30s.
* Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
* For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
* If the positions of the symbol are crossed margined in Hedge Mode:
* "HEDGE" as a sign will be returned instead of "BOTH";
* A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.

查询UM持仓ADL队列估算

* 每30秒更新数据
* 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前
* 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数
* 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE", 其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。

Operation ID: `umPositionAdlQuantileEstimation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：UM Position ADL Quantile Estimation / UM 持仓 ADL Quantile Estimation

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | Trade symbol, if existing.<br>交易对（如存在）。<br>例: `ETHUSDT` |
| [].adlQuantile | object |  | Adl Quantile. |
| [].adlQuantile.LONG | integer (int64) |  | adl quantile for "LONG" position in hedge mode<br>双开模式下多头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.SHORT | integer (int64) |  | adl quantile for "SHORT" position in hedge mode<br>双开模式下空头持仓的ADL队列估算分<br>例: `3` |
| [].adlQuantile.BOTH | integer (int64) |  | adl quantile for position in one-way mode<br>单开模式下持仓的ADL队列估算分<br>例: `0` |

## New UM Algo Order (TRADE)（UM条件单下单 (TRADE)）

`POST /papi/v1/um/algo/order`

Place new UM conditional order

UM条件单下单

Operation ID: `newUmAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoType | string | 是 | Only support `CONDITIONAL`<br>仅支持 `CONDITIONAL`<br>枚举: `CONDITIONAL`<br>例: `CONDITIONAL` |
| symbol | string | 是 | 例: `BNBUSDT` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `SELL` |
| positionSide | string |  | Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode<br>单向持仓模式下默认且仅可填`BOTH`；双向持仓模式下必填，仅可选择 `LONG` 或 `SHORT`<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| type | string | 是 | Conditional order type<br>条件订单类型<br>枚举: `STOP`, `TAKE_PROFIT`, `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `TAKE_PROFIT` |
| timeInForce | string |  | 枚举: `IOC`, `GTC`, `FOK`, `GTX`, `GTD`<br>默认: `GTC`<br>例: `GTC` |
| quantity | number (float) |  | Order quantity. Cannot be sent with `closePosition`=`true`(Close-All)<br>下单数量,使用`closePosition`不支持此参数。<br>例: `0.01` |
| price | number (float) |  | Order price<br>委托价格<br>例: `750.000` |
| triggerPrice | number (float) |  | Trigger price<br>触发价<br>例: `750.000` |
| workingType | string |  | Trigger price type. Default `CONTRACT_PRICE`<br>触发类型，默认 `CONTRACT_PRICE`<br>枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `CONTRACT_PRICE` |
| priceMatch | string |  | Can't be passed together with `price`<br>不能与 `price` 同时传<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `NONE` |
| closePosition | string |  | Close-All, used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用<br>枚举: `true`, `false`<br>例: `true` |
| priceProtect | string |  | Price protection. Default `false`<br>条件单触发保护，默认 `false`<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`<br>非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| activatePrice | number (float) |  | Used with `TRAILING_STOP_MARKET`, default as latest price<br>追踪止损激活价格，仅`TRAILING_STOP_MARKET`需要<br>例: `700` |
| callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET`, min 0.1, max 20 (1 = 1%)<br>追踪止损回调比例，范围[0.1, 20]，1代表1%<br>例: `1` |
| clientAlgoId | string |  | Unique id among open orders. Auto-generated if not sent<br>用户自定义的条件订单号，不可以重复出现在挂单中<br>例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| selfTradePreventionMode | string |  | 枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`<br>默认: `NONE`<br>例: `NONE` |
| goodTillDate | integer (int64) |  | Order cancel time for `GTD` timeInForce, mandatory when timeInForce is `GTD`<br>TIF为GTD时订单的自动取消时间，当timeInForce为GTD时必传<br>例: `0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New UM Algo Order / UM条件单下单

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

## Cancel UM Algo Order (TRADE)（UM撤销条件订单 (TRADE)）

`DELETE /papi/v1/um/algo/order`

Cancel an active UM algo order

撤销条件订单

Operation ID: `cancelUmAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | Algo order ID<br>系统订单号<br>例: `2146760` |
| clientAlgoId | query | string |  | Client algo order ID<br>用户自定义的订单号<br>例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel UM Algo Order / UM撤销条件订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| complete | boolean |  | 例: `True` |

## Cancel All UM Algo Open Orders (TRADE)（UM撤销全部条件订单 (TRADE)）

`DELETE /papi/v1/um/algo/allOpenOrders`

Cancel All UM Algo Open Orders

UM撤销全部条件订单

Operation ID: `cancelAllUmAlgoOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Symbol<br>交易对<br>例: `BNBUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All UM Algo Open Orders / UM撤销全部条件订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer |  | 例: `200` |
| msg | string |  | 例: `The operation of cancel all open order is done.` |

## Query Current UM Open Algo Order (USER_DATA)（查询UM当前条件挂单 (USER_DATA)）

`GET /papi/v1/um/algo/algoOrder`

Check an UM algo order's status. Orders will not be found if: status is CANCELED/EXPIRED with no fills and created 3+ days ago; or created 90+ days ago.

查询UM条件订单状态。如果订单状态为 CANCELED 或 EXPIRED 且无成交记录且创建时间超过3天，或创建时间超过90天，将不会被查询到。

Operation ID: `queryCurrentUmOpenAlgoOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | Algo order ID<br>系统订单号<br>例: `2146760` |
| clientAlgoId | query | string |  | Client algo order ID<br>用户自定义的订单号<br>例: `6B2I9XVcJpCjqPAJ4YoFX7` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query UM Algo Order / 查询UM当前条件挂单

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
| actualOrderId | string |  | 例: `` |
| actualPrice | string |  | 例: `0.00000` |
| triggerPrice | string |  | 例: `750.000` |
| price | string |  | 例: `750.000` |
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

## Query All Current UM Open Algo Orders (USER_DATA)（查看UM当前全部条件挂单 (USER_DATA)）

`GET /papi/v1/um/algo/openAlgoOrders`

Get all UM open algo orders on a symbol. If the symbol is not sent, orders for all symbols will be returned.

查看当前全部条件挂单。不带symbol参数，会返回所有交易对的挂单。

Operation ID: `queryAllCurrentUmOpenAlgoOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoType | query | string |  | 例: `CONDITIONAL` |
| symbol | query | string |  | 例: `BNBUSDT` |
| algoId | query | integer (int64) |  | 例: `2146760` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query All Current UM Open Algo Orders / 查看UM当前全部条件挂单

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
| [].algoStatus | string |  | 例: `NEW` |
| [].triggerPrice | string |  | 例: `750.000` |
| [].price | string |  | 例: `750.000` |
| [].selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| [].workingType | string |  | 例: `CONTRACT_PRICE` |
| [].priceMatch | string |  | 例: `NONE` |
| [].closePosition | boolean |  | 例: `False` |
| [].priceProtect | boolean |  | 例: `False` |
| [].reduceOnly | boolean |  | 例: `False` |
| [].createTime | integer (int64) |  | 例: `1750485492076` |
| [].updateTime | integer (int64) |  | 例: `1750485492076` |
| [].triggerTime | integer (int64) |  | 例: `0` |
| [].goodTillDate | integer (int64) |  | 例: `0` |

## Query UM Algo Order History (USER_DATA)（查询UM条件单历史 (USER_DATA)）

`GET /papi/v1/um/algo/allAlgoOrders`

Get all algo orders: ACTIVE, CANCELED, TRIGGERED or FINISHED.

查询UM条件单历史

Operation ID: `queryUmAlgoOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| algoId | query | integer (int64) |  | Only return orders >= this algoId<br>只返回此orderID及之后的订单，缺省返回最近的订单<br>例: `2146760` |
| startTime | query | integer (int64) |  | 例: `1770130294138` |
| endTime | query | integer (int64) |  | 例: `1770736694138` |
| limit | query | integer (int64) |  | Default 500; max 1000<br>默认值:500 最大值:1000<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query UM Algo Order History / 查询UM条件单历史

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

## Futures TradFi Perps Contract (USER_DATA)（传统金融合约协议 (USER_DATA)）

`POST /papi/v1/um/stock/contract`

Sign TradFi-Perps agreement contract

签署传统金融合约协议

Operation ID: `futuresTradfiPerpsContract`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures TradFi Perps Contract / 传统金融合约协议

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer |  | 例: `200` |
| msg | string |  | 例: `success` |

## Start User Data Stream (USER_STREAM)（生成listenKey (USER_STREAM)）

`POST /papi/v1/listenKey`

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

Operation ID: `startUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | Listen Key.<br>例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1` |

## Keepalive User Data Stream (USER_STREAM)（延长listenKey有效期 (USER_STREAM)）

`PUT /papi/v1/listenKey`

Keepalive a user data stream to prevent a time out. User data streams
will close after 60 minutes. It's recommended to send a ping about every
60 minutes.

有效期延长至本次调用后60分钟

Operation ID: `keepaliveUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功

## Close User Data Stream (USER_STREAM)（关闭listenKey (USER_STREAM)）

`DELETE /papi/v1/listenKey`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功