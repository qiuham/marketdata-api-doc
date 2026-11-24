---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-margin-trading/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:11.815954
---

# Margin REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-margin-trading/api/rest-api/1.0.0/schema.yaml

Access account information, borrow and repay assets, and trade with Binance Margin.

访问账户信息、借入和偿还资产，并通过 Binance 杠杆进行交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/margin/max-leverage` — Adjust cross margin max leverage (USER_DATA)
- `GET /sapi/v1/margin/isolated/account` — Query Isolated Margin Account Info (USER_DATA)
- `POST /sapi/v1/margin/isolated/account` — Enable Isolated Margin Account (TRADE)
- `DELETE /sapi/v1/margin/isolated/account` — Disable Isolated Margin Account (TRADE)
- `GET /sapi/v1/bnbBurn` — Get BNB Burn Status (USER_DATA)
- `GET /sapi/v1/margin/tradeCoeff` — Get Summary of Margin account (USER_DATA)
- `GET /sapi/v1/margin/capital-flow` — Query Cross Isolated Margin Capital Flow (USER_DATA)
- `GET /sapi/v1/margin/account` — Query Cross Margin Account Details (USER_DATA)
- `GET /sapi/v1/margin/crossMarginData` — Query Cross Margin Fee Data (USER_DATA)
- `GET /sapi/v1/margin/isolated/accountLimit` — Query Enabled Isolated Margin Account Limit (USER_DATA)
- `GET /sapi/v1/margin/isolatedMarginData` — Query Isolated Margin Fee Data (USER_DATA)
- `GET /sapi/v1/margin/next-hourly-interest-rate` — Get future hourly interest rate (USER_DATA)
- `GET /sapi/v1/margin/interestHistory` — Get Interest History (USER_DATA)
- `GET /sapi/v1/margin/borrow-repay` — Query borrow/repay records in Margin account (USER_DATA)
- `POST /sapi/v1/margin/borrow-repay` — Margin account borrow/repay (USER_DATA)
- `GET /sapi/v1/margin/interestRateHistory` — Query Margin Interest Rate History (USER_DATA)
- `GET /sapi/v1/margin/maxBorrowable` — Query Max Borrow (USER_DATA)
- `GET /sapi/v1/margin/crossMarginCollateralRatio` — Cross margin collateral ratio (MARKET_DATA)
- `GET /sapi/v1/margin/allPairs` — Get All Cross Margin Pairs (MARKET_DATA)
- `GET /sapi/v1/margin/isolated/allPairs` — Get All Isolated Margin Symbol (MARKET_DATA)
- `GET /sapi/v1/margin/allAssets` — Get All Margin Assets (MARKET_DATA)
- `GET /sapi/v1/margin/delist-schedule` — Get Delist Schedule (MARKET_DATA)
- `GET /sapi/v1/margin/limit-price-pairs` — Get Limit Price Pairs (MARKET_DATA)
- `GET /sapi/v1/margin/list-schedule` — Get list Schedule (MARKET_DATA)
- `GET /sapi/v1/margin/risk-based-liquidation-ratio` — Get Margin Asset Risk-Based Liquidation Ratio (MARKET_DATA)
- `GET /sapi/v1/margin/restricted-asset` — Get Margin Restricted Assets (MARKET_DATA)
- `GET /sapi/v1/margin/isolatedMarginTier` — Query Isolated Margin Tier Data (USER_DATA)
- `GET /sapi/v1/margin/leverageBracket` — Query Liability Coin Leverage Bracket in Cross Margin Pro Mode (MARKET_DATA)
- `GET /sapi/v1/margin/available-inventory` — Query Margin Available Inventory (USER_DATA)
- `GET /sapi/v1/margin/priceIndex` — Query Margin PriceIndex (MARKET_DATA)
- `POST /sapi/v1/margin/listen-key` — Start User Data Stream (USER_STREAM)
- `PUT /sapi/v1/margin/listen-key` — Keepalive User Data Stream (USER_STREAM)
- `DELETE /sapi/v1/margin/listen-key` — Close User Data Stream (USER_STREAM)
- `POST /sapi/v2/margin/listen-key` — Start User Data Stream V2 (USER_STREAM)
- `PUT /sapi/v2/margin/listen-key` — Keepalive User Data Stream V2 (USER_STREAM)
- `DELETE /sapi/v2/margin/listen-key` — Close User Data Stream V2 (USER_STREAM)
- `GET /sapi/v1/margin/apiKey` — Query Special key(Low Latency Trading) (TRADE)
- `POST /sapi/v1/margin/apiKey` — Create Special Key(Low-Latency Trading) (TRADE)
- `DELETE /sapi/v1/margin/apiKey` — Delete Special Key(Low-Latency Trading) (TRADE)
- `PUT /sapi/v1/margin/apiKey/ip` — Edit ip for Special Key(Low-Latency Trading) (TRADE)
- `POST /sapi/v1/margin/exit-special-key-mode` — Exit Special Key Mode (TRADE)
- `GET /sapi/v1/margin/forceLiquidationRec` — Get Force Liquidation Record (USER_DATA)
- `GET /sapi/v1/margin/exchange-small-liability` — Get Small Liability Exchange Coin List (USER_DATA)
- `POST /sapi/v1/margin/exchange-small-liability` — Small Liability Exchange (MARGIN)
- `GET /sapi/v1/margin/exchange-small-liability-history` — Get Small Liability Exchange History (USER_DATA)
- `GET /sapi/v1/margin/openOrders` — Query Margin Account's Open Orders (USER_DATA)
- `DELETE /sapi/v1/margin/openOrders` — Margin Account Cancel all Open Orders on a Symbol (TRADE)
- `GET /sapi/v1/margin/orderList` — Query Margin Account's OCO (USER_DATA)
- `DELETE /sapi/v1/margin/orderList` — Margin Account Cancel OCO (TRADE)
- `GET /sapi/v1/margin/order` — Query Margin Account's Order (USER_DATA)
- `POST /sapi/v1/margin/order` — Margin Account New Order (TRADE)
- `DELETE /sapi/v1/margin/order` — Margin Account Cancel Order (TRADE)
- `POST /sapi/v1/margin/order/oco` — Margin Account New OCO (TRADE)
- `POST /sapi/v1/margin/order/oto` — Margin Account New OTO (TRADE)
- `POST /sapi/v1/margin/order/otoco` — Margin Account New OTOCO (TRADE)
- `POST /sapi/v1/margin/manual-liquidation` — Margin Manual Liquidation (TRADE)
- `GET /sapi/v1/margin/rateLimit/order` — Query Current Margin Order Count Usage (TRADE)
- `GET /sapi/v1/margin/allOrderList` — Query Margin Account's all OCO (USER_DATA)
- `GET /sapi/v1/margin/allOrders` — Query Margin Account's All Orders (USER_DATA)
- `GET /sapi/v1/margin/openOrderList` — Query Margin Account's Open OCO (USER_DATA)
- `GET /sapi/v1/margin/oto/openOrderList` — Query Margin Account's Open OTO/OTOCO Order Lists (USER_DATA)
- `GET /sapi/v1/margin/myTrades` — Query Margin Account's Trade List (USER_DATA)
- `GET /sapi/v1/margin/myPreventedMatches` — Query Prevented Matches (USER_DATA)
- `GET /sapi/v1/margin/api-key-list` — Query Special key List(Low Latency Trading) (TRADE)
- `GET /sapi/v1/margin/liquidation-loan` — Query Liquidation Loan (USER_DATA)
- `POST /sapi/v1/margin/liquidation-loan/repay` — Liquidation Loan Repay (MARGIN)
- `GET /sapi/v1/margin/liquidation-loan/repay-history` — Query Liquidation Loan Repay History (USER_DATA)
- `GET /sapi/v1/margin/transfer` — Get Cross Margin Transfer History (USER_DATA)
- `GET /sapi/v1/margin/maxTransferable` — Query Max Transfer-Out Amount (USER_DATA)

## Adjust cross margin max leverage (USER_DATA)（调整全仓最大杠杆 (USER_DATA)）

`POST /sapi/v1/margin/max-leverage`

Adjust cross margin max leverage

调整全仓最大杠杆倍数

Operation ID: `adjustCrossMarginMaxLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| maxLeverage | integer (int64) | 是 | Can only adjust 3 , 5 or 10，Example: maxLeverage = 5 or 3 for Cross Margin Classic; maxLeverage=10 for Cross Margin Pro 10x leverage or 20x if compliance allows.<br>只能调整3, 5 , 或者 10。举例: maxLeverage = 5 或者3是选择全仓Classic模式； maxLeverage=10 是选择切换成全仓 Pro 模式下的10倍杠杆 或者 20倍杠杆（在合规允许的情况下）。<br>例: `3` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Adjust cross margin max leverage / Adjust cross 杠杆 最大leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | success.<br>成功.<br>例: `True` |

## Query Isolated Margin Account Info (USER_DATA)（查询杠杆逐仓账户信息 (USER_DATA)）

`GET /sapi/v1/margin/isolated/account`

Query Isolated Margin Account Info

查询杠杆逐仓账户信息

Operation ID: `queryIsolatedMarginAccountInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbols | query | string |  | Max 5 交易对s can be sent; separated by ",".<br>例: `BTCUSDT,BNBUSDT,ADAUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Isolated Margin Account Info / Isolated 杠杆 账户 Info

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] |  | assets list.<br>assets 列表. |
| assets[].baseAsset | object |  | base Asset object.<br>base 资产 object. |
| assets[].baseAsset.asset | string |  | asset.<br>资产.<br>例: `BTC` |
| assets[].baseAsset.borrowEnabled | boolean |  | borrow Enabled.<br>借款 启用.<br>例: `True` |
| assets[].baseAsset.borrowed | string |  | borrowed.<br>借入.<br>例: `0.00000000` |
| assets[].baseAsset.free | string |  | free.<br>可用.<br>例: `0.00000000` |
| assets[].baseAsset.interest | string |  | interest.<br>利息.<br>例: `0.00000000` |
| assets[].baseAsset.locked | string |  | locked.<br>冻结.<br>例: `0.00000000` |
| assets[].baseAsset.netAsset | string |  | net Asset.<br>净值 资产.<br>例: `0.00000000` |
| assets[].baseAsset.netAssetOfBtc | string |  | net Asset Of Btc.<br>净值 资产 Of Btc.<br>例: `0.00000000` |
| assets[].baseAsset.repayEnabled | boolean |  | repay Enabled.<br>还款 启用.<br>例: `True` |
| assets[].baseAsset.totalAsset | string |  | total Asset.<br>总计 资产.<br>例: `0.00000000` |
| assets[].quoteAsset | object |  | quote Asset object.<br>quote 资产 object. |
| assets[].quoteAsset.asset | string |  | asset.<br>资产.<br>例: `USDT` |
| assets[].quoteAsset.borrowEnabled | boolean |  | borrow Enabled.<br>借款 启用.<br>例: `True` |
| assets[].quoteAsset.borrowed | string |  | borrowed.<br>借入.<br>例: `0.00000000` |
| assets[].quoteAsset.free | string |  | free.<br>可用.<br>例: `0.00000000` |
| assets[].quoteAsset.interest | string |  | interest.<br>利息.<br>例: `0.00000000` |
| assets[].quoteAsset.locked | string |  | locked.<br>冻结.<br>例: `0.00000000` |
| assets[].quoteAsset.netAsset | string |  | net Asset.<br>净值 资产.<br>例: `0.00000000` |
| assets[].quoteAsset.netAssetOfBtc | string |  | net Asset Of Btc.<br>净值 资产 Of Btc.<br>例: `0.00000000` |
| assets[].quoteAsset.repayEnabled | boolean |  | repay Enabled.<br>还款 启用.<br>例: `True` |
| assets[].quoteAsset.totalAsset | string |  | total Asset.<br>总计 资产.<br>例: `0.00000000` |
| assets[].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| assets[].isolatedCreated | boolean |  | isolated Created.<br>逐仓 Created.<br>例: `True` |
| assets[].enabled | boolean |  | true-enabled, false-disabled<br>账户是否启用，true-启用，false-停用<br>例: `True` |
| assets[].marginLevel | string |  | margin Level.<br>杠杆 Level.<br>例: `0.00000000` |
| assets[].marginLevelStatus | string |  | "EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"<br>"EXCESSIVE", "NORMAL", "杠杆_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"<br>例: `EXCESSIVE` |
| assets[].marginRatio | string |  | margin Ratio.<br>杠杆 Ratio.<br>例: `0.00000000` |
| assets[].indexPrice | string |  | index Price.<br>index 价格.<br>例: `10000.00000000` |
| assets[].liquidatePrice | string |  | liquidate Price.<br>liquidate 价格.<br>例: `1000.00000000` |
| assets[].liquidateRate | string |  | liquidate Rate.<br>liquidate 利率.<br>例: `1.00000000` |
| assets[].tradeEnabled | boolean |  | trade Enabled.<br>交易 启用.<br>例: `True` |
| totalAssetOfBtc | string |  | total Asset Of Btc.<br>总计 资产 Of Btc.<br>例: `0.00000000` |
| totalLiabilityOfBtc | string |  | total Liability Of Btc.<br>总计 Liability Of Btc.<br>例: `0.00000000` |
| totalNetAssetOfBtc | string |  | total Net Asset Of Btc.<br>总计 净值 资产 Of Btc.<br>例: `0.00000000` |

## Enable Isolated Margin Account (TRADE)（杠杆逐仓账户启用 (TRADE)）

`POST /sapi/v1/margin/isolated/account`

Enable isolated margin account for a specific symbol(Only supports activation of previously disabled accounts).

启用特定交易对的杠杆逐仓账户（仅支持启用之前停用的账户）。

Operation ID: `enableIsolatedMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enable Isolated Margin Account / 启用Isolated 杠杆 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | success.<br>成功.<br>例: `True` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |

## Disable Isolated Margin Account (TRADE)（杠杆逐仓账户停用 (TRADE)）

`DELETE /sapi/v1/margin/isolated/account`

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24 hours.

停用特定交易对的杠杆逐仓账户。每个交易对 24 小时内仅可停用一次。

Operation ID: `disableIsolatedMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Disable Isolated Margin Account / 禁用Isolated 杠杆 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | success.<br>成功.<br>例: `True` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |

## Get BNB Burn Status (USER_DATA)（获取BNB抵扣开关状态 (USER_DATA)）

`GET /sapi/v1/bnbBurn`

Get BNB Burn Status

获取BNB抵扣开关状态

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
| spotBNBBurn | boolean |  | spot BNBBurn.<br>字段说明：spot BNBBurn.<br>例: `True` |
| interestBNBBurn | boolean |  | interest BNBBurn.<br>利息 BNBBurn.<br>例: `False` |

## Get Summary of Margin account (USER_DATA)（查询Margin账户信息汇总 (USER_DATA)）

`GET /sapi/v1/margin/tradeCoeff`

Get personal margin level information

获取用户个人杠杆账户信息汇总

Operation ID: `getSummaryOfMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Summary of Margin account / 获取Summary of 杠杆 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| normalBar | string |  | normal Bar.<br>字段说明：normal Bar.<br>例: `1.5` |
| marginCallBar | string |  | margin Call Bar.<br>杠杆 Call Bar.<br>例: `1.3` |
| forceLiquidationBar | string |  | force Liquidation Bar.<br>强平 Bar.<br>例: `1.1` |

## Query Cross Isolated Margin Capital Flow (USER_DATA)（查询全仓/逐仓资金流水 (USER_DATA)）

`GET /sapi/v1/margin/capital-flow`

Query Cross Isolated Margin Capital Flow

查询全仓/逐仓资金流水

Operation ID: `queryCrossIsolatedMarginCapitalFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| symbol | query | string |  | Mandatory for Isolated data<br>查询逐仓数据时必填<br>Mandatory for 逐仓 数据<br>例: `BTCUSDT` |
| type | query | string |  | 枚举: `TRANSFER`, `BORROW`, `REPAY`, `BUY_INCOME`, `BUY_EXPENSE`, `SELL_INCOME`, `SELL_EXPENSE`, `TRADING_COMMISSION`, `BUY_LIQUIDATION`, `SELL_LIQUIDATION`, `REPAY_LIQUIDATION`, `OTHER_LIQUIDATION`, `LIQUIDATION_FEE`, `SMALL_BALANCE_CONVERT`, `COMMISSION_RETURN`, `SMALL_CONVERT`<br>例: `TRANSFER` |
| startTime | query | integer (int64) |  | Only supports 查询 数据 from the past 90 days.<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| fromId | query | integer (int64) |  | 如设置 `fromId`，将返回所查询时间范围内 `id` 大于 `fromId` 的数据。否则将返回该时间范围内的最新数据。`fromId` 不会扩展查询的时间范围。<br>例: `1` |
| limit | query | integer (int64) |  | 限制 on the number of 数据 records returned per 请求. ;<br>默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cross Isolated Margin Capital Flow / Cross Isolated 杠杆 Capital Flow

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | id.<br>字段说明：ID.<br>例: `123456` |
| [].tranId | integer (int64) |  | tran Id.<br>字段说明：tran ID.<br>例: `123123` |
| [].timestamp | integer (int64) |  | timestamp.<br>时间戳.<br>例: `1691116657000` |
| [].asset | string |  | asset.<br>资产.<br>例: `USDT` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].type | string |  | type.<br>类型.<br>例: `BORROW` |
| [].amount | string |  | amount.<br>数量.<br>例: `101` |
| [].note | string |  | note.<br>备注.<br>枚举: `INSTITUTIONAL_LOAN_TRANSFER`, `INSTITUTIONAL_LOAN_BORROW`, `INSTITUTIONAL_LOAN_REPAY`<br>例: `INSTITUTIONAL_LOAN_TRANSFER` |

## Query Cross Margin Account Details (USER_DATA)（查询全仓杠杆账户详情 (USER_DATA)）

`GET /sapi/v1/margin/account`

Query Cross Margin Account Details

查询全仓杠杆账户详情

Operation ID: `queryCrossMarginAccountDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cross Margin Account Details / Cross 杠杆 账户 Details

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| created | boolean |  | True means margin account created , false means margin account not created.<br>true 表示已开户, false 表示未开户<br>例: `True` |
| borrowEnabled | boolean |  | borrow Enabled.<br>借款 启用.<br>例: `True` |
| marginLevel | string |  | margin Level.<br>杠杆 Level.<br>例: `11.64405625` |
| collateralMarginLevel | string |  | collateral Margin Level.<br>collateral 杠杆 Level.<br>例: `3.2` |
| totalAssetOfBtc | string |  | total Asset Of Btc.<br>总计 资产 Of Btc.<br>例: `6.82728457` |
| totalLiabilityOfBtc | string |  | total Liability Of Btc.<br>总计 Liability Of Btc.<br>例: `0.58633215` |
| totalNetAssetOfBtc | string |  | total Net Asset Of Btc.<br>总计 净值 资产 Of Btc.<br>例: `6.24095242` |
| TotalCollateralValueInUSDT | string |  | Total Collateral Value In USDT.<br>总计 Collateral Value In USDT.<br>例: `5.82728457` |
| tradeEnabled | boolean |  | trade Enabled.<br>交易 启用.<br>例: `True` |
| transferInEnabled | boolean |  | transfer In Enabled.<br>划转 In 启用.<br>例: `True` |
| transferOutEnabled | boolean |  | transfer Out Enabled.<br>划转 Out 启用.<br>例: `True` |
| accountType | string |  | // MARGIN_1 for Cross Margin Classic, MARGIN_2 for Cross Margin Pro<br>MARGIN_1 全仓Classic模式账户, MARGIN_2 全仓Pro模式账户<br>例: `MARGIN_1` |
| userAssets | object[] |  | user Assets list.<br>user Assets 列表. |
| userAssets[].asset | string |  | asset.<br>资产.<br>例: `BTC` |
| userAssets[].borrowed | string |  | borrowed.<br>借入.<br>例: `0.00000000` |
| userAssets[].free | string |  | free.<br>可用.<br>例: `0.00499500` |
| userAssets[].interest | string |  | interest.<br>利息.<br>例: `0.00000000` |
| userAssets[].locked | string |  | locked.<br>冻结.<br>例: `0.00000000` |
| userAssets[].netAsset | string |  | net Asset.<br>净值 资产.<br>例: `0.00499500` |

## Query Cross Margin Fee Data (USER_DATA)（获取全仓杠杆利率及限额 (USER_DATA)）

`GET /sapi/v1/margin/crossMarginData`

Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

通过VIP等级或用户当前VIP等级获取全仓杠杆利率及限额， 如：https://www.binance.com/en/margin-fee

权重: 1 when coin is specified;(IP) 5 when the coin parameter is omitted(IP)

Operation ID: `queryCrossMarginFeeData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| vipLevel | query | integer (int64) |  | User's current specific margin data will be returned if vipLevel is omitted<br>默认为用户当前VIP等级<br>例: `1` |
| coin | query | string |  | 例: `BTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cross Margin Fee Data / Cross 杠杆 Fee Data

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].vipLevel | integer (int64) |  | vip Level.<br>vip 等级.<br>例: `0` |
| [].coin | string |  | coin.<br>字段说明：coin.<br>例: `BTC` |
| [].transferIn | boolean |  | transfer In.<br>划转 In.<br>例: `True` |
| [].borrowable | boolean |  | borrowable.<br>借款able.<br>例: `True` |
| [].dailyInterest | string |  | daily Interest.<br>daily 利息.<br>例: `0.00026125` |
| [].yearlyInterest | string |  | yearly Interest.<br>yearly 利息.<br>例: `0.0953` |
| [].borrowLimit | string |  | borrow Limit.<br>借款 限制.<br>例: `180` |
| [].marginablePairs | string[] |  | marginable Pairs list.<br>marginable Pairs 列表. |

## Query Enabled Isolated Margin Account Limit (USER_DATA)（查询杠杆逐仓账户启用限制 (USER_DATA)）

`GET /sapi/v1/margin/isolated/accountLimit`

Query enabled isolated margin account limit.

查询杠杆逐仓账户启用限制。

Operation ID: `queryEnabledIsolatedMarginAccountLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Enabled Isolated Margin Account Limit / Enabled Isolated 杠杆 账户 限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enabledAccount | integer (int64) |  | enabled Account.<br>启用 Account.<br>例: `5` |
| maxAccount | integer (int64) |  | max Account.<br>字段说明：max Account.<br>例: `20` |

## Query Isolated Margin Fee Data (USER_DATA)（获取逐仓杠杆利率及限额 (USER_DATA)）

`GET /sapi/v1/margin/isolatedMarginData`

Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

通过VIP等级或用户当前VIP等级获取逐仓杠杆利率及限额， 如： https://www.binance.com/en/margin-fee

权重: 1 when a single is specified;(IP) 10 when the symbol parameter is omitted(IP)

Operation ID: `queryIsolatedMarginFeeData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| vipLevel | query | integer (int64) |  | User's 当前 specific 杠杆 数据 will be returned if vipLevel is omitted<br>例: `1` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Isolated Margin Fee Data / Isolated 杠杆 Fee Data

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].vipLevel | integer (int64) |  | vip Level.<br>vip 等级.<br>例: `0` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].leverage | string |  | leverage.<br>字段说明：leverage.<br>例: `10` |
| [].data | object[] |  | data list.<br>数据 列表. |
| [].data[].coin | string |  | coin.<br>字段说明：coin.<br>例: `BTC` |
| [].data[].dailyInterest | string |  | daily Interest.<br>daily 利息.<br>例: `0.00026125` |
| [].data[].borrowLimit | string |  | borrow Limit.<br>借款 限制.<br>例: `270` |

## Get future hourly interest rate (USER_DATA)（查询下小时预估利率 (USER_DATA)）

`GET /sapi/v1/margin/next-hourly-interest-rate`

Get future hourly interest rate

查询用户币种下小时预估利率

Operation ID: `getFutureHourlyInterestRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| assets | query | string | 是 | 资产列表，以逗号分隔，最多20个<br>例: `BTC,ETH` |
| isIsolated | query | string | 是 | 是否逐仓杠杆，<br>枚举: `TRUE`, `FALSE`<br>例: `TRUE` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get future hourly interest rate / 获取future hourly 利息 利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>资产.<br>例: `BTC` |
| [].nextHourlyInterestRate | string |  | next Hourly Interest Rate.<br>next Hourly Interest 利率.<br>例: `0.00000571` |

## Get Interest History (USER_DATA)（获取利息历史 (USER_DATA)）

`GET /sapi/v1/margin/interestHistory`

Get Interest History

获取利息历史

Operation ID: `getInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| isolatedSymbol | query | string |  | 逐仓交易对，适用于逐仓查询<br>例: `BNBUSDT` |
| startTime | query | integer (int64) |  | Only supports querying data from the past 90 days.<br>只支持查询最近90天的数据<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | 当前查询页。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 赋值不能大于 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Interest History / 获取利息 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | rows list.<br>rows 列表. |
| rows[].txId | integer (int64) |  | tx Id.<br>字段说明：tx ID.<br>例: `1352286576452864800` |
| rows[].interestAccuredTime | integer (int64) |  | interest Accured Time.<br>interest Accured 时间.<br>例: `1672160400000` |
| rows[].asset | string |  | asset.<br>资产.<br>例: `USDT` |
| rows[].rawAsset | string |  | will not be returned for isolated margin<br>逐仓不会返回此字段<br>例: `USDT` |
| rows[].principal | string |  | principal.<br>本金.<br>例: `45.3313` |
| rows[].interest | string |  | interest.<br>利息.<br>例: `0.00024995` |
| rows[].interestRate | string |  | interest Rate.<br>interest 利率.<br>例: `0.00013233` |
| rows[].type | string |  | type.<br>类型.<br>例: `ON_BORROW` |
| rows[].isolatedSymbol | string |  | isolated symbol, will not be returned for crossed margin<br>返回逐仓symbol; 若是全仓不会返回此字段<br>例: `BNBUSDT` |
| total | integer (int64) |  | total.<br>总计.<br>例: `1` |

## Query borrow/repay records in Margin account (USER_DATA)（查询借贷/还款记录 (USER_DATA)）

`GET /sapi/v1/margin/borrow-repay`

Query borrow/repay records in Margin account

查询借贷/还款记录

Operation ID: `queryBorrowRepayRecordsInMarginAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BNB` |
| isolatedSymbol | query | string |  | 逐仓交易对，适用于逐仓查询<br>例: `BNBUSDT` |
| txId | query | integer (int64) |  | `tranId` in `POST /sapi/v1/杠杆/loan`<br>例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | 当前查询页。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| type | query | string | 是 | 枚举: `BORROW`, `REPAY`<br>例: `BORROW` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：borrow/repay records in Margin account / borrow/repay records in 杠杆 账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | rows list.<br>rows 列表. |
| rows[].type | string |  | AUTO,MANUAL for Cross Margin Borrow; MANUAL，AUTO，BNB_AUTO_REPAY，POINT_AUTO_REPAY for Cross Margin Repay; AUTO，MANUAL for Isolated Margin Borrow/Repay;<br>全仓借贷可返回：AUTO,MANUAL ; 全仓还款可返回：MANUAL，AUTO，BNB_AUTO_REPAY，POINT_AUTO_REPAY; 逐仓借贷或还款可返回：AUTO，MANUAL<br>例: `AUTO` |
| rows[].isolatedSymbol | string |  | isolated symbol, will not be returned for crossed margin<br>逐仓还款 返回逐仓symbol; 若是全仓不会返回此字段<br>例: `BNBUSDT` |
| rows[].amount | string |  | Total amount borrowed/repaid<br>还款总额<br>例: `14.00000000` |
| rows[].asset | string |  | asset.<br>资产.<br>例: `BNB` |
| rows[].interest | string |  | Interest repaid<br>支付的利息<br>例: `0.01866667` |
| rows[].principal | string |  | Principal repaid<br>支付的本金<br>例: `13.98133333` |
| rows[].status | string |  | one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account);<br>状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);<br>例: `CONFIRMED` |
| rows[].timestamp | integer (int64) |  | timestamp.<br>时间戳.<br>例: `1563438204000` |
| rows[].txId | integer (int64) |  | tx Id.<br>字段说明：tx ID.<br>例: `2970933056` |
| total | integer (int64) |  | total.<br>总计.<br>例: `1` |

## Margin account borrow/repay (USER_DATA)（杠杆账户借贷/还款 (USER_DATA)）

`POST /sapi/v1/margin/borrow-repay`

Margin account borrow/repay

杠杆账户借贷/还款

Operation ID: `marginAccountBorrowRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| isIsolated | string | 是 | `TRUE` for Isolated Margin, `FALSE` for Cross Margin<br>是否逐仓杠杆，`TRUE`, `FALSE`, 默认 `FALSE`<br>枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `TRUE` |
| symbol | string |  | Only for Isolated margin<br>逐仓交易对，配合逐仓使用<br>例: `BTCUSDT` |
| amount | string | 是 | 例: `1.0` |
| type | string | 是 | 枚举: `BORROW`, `REPAY`<br>例: `BORROW` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin account borrow/repay / 杠杆 账户 borrow/repay

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | tran Id.<br>字段说明：tran ID.<br>例: `100000001` |

## Query Margin Interest Rate History (USER_DATA)（获取杠杆利率历史 (USER_DATA)）

`GET /sapi/v1/margin/interestRateHistory`

Query Margin Interest Rate History

获取杠杆利率历史

Operation ID: `queryMarginInterestRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `BTC` |
| vipLevel | query | integer (int64) |  | 默认： user's vip level<br>例: `1` |
| startTime | query | integer (int64) |  | 默认： 7 days ago<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | 默认： present. 最大范围： 1 months.<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Interest Rate History / 杠杆 利率 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>资产.<br>例: `BTC` |
| [].dailyInterestRate | string |  | daily Interest Rate.<br>daily Interest 利率.<br>例: `0.00025000` |
| [].timestamp | integer (int64) |  | timestamp.<br>时间戳.<br>例: `1611544731000` |
| [].vipLevel | integer (int64) |  | vip Level.<br>vip 等级.<br>例: `1` |

## Query Max Borrow (USER_DATA)（查询账户最大可借贷额度 (USER_DATA)）

`GET /sapi/v1/margin/maxBorrowable`

Query Max Borrow

查询账户最大可借贷额度

Operation ID: `queryMaxBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `BTC` |
| isolatedSymbol | query | string |  | 逐仓交易对，适用于逐仓查询<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Max Borrow / 最大 借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | string |  | account's currently max borrowable amount with sufficient system availability<br>系统可借充足情况下用户账户当前最大可借额度<br>例: `1.69248805` |
| borrowLimit | string |  | max borrowable amount limited by the account level<br>平台限制的用户当前等级可以借的额度<br>例: `60` |

## Cross margin collateral ratio (MARKET_DATA)（全仓币种质押率 (MARKET_DATA)）

`GET /sapi/v1/margin/crossMarginCollateralRatio`

Cross margin collateral ratio

全仓币种质押率

Operation ID: `crossMarginCollateralRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Cross margin collateral ratio / Cross 杠杆 抵押 ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].collaterals | object[] |  | collaterals list.<br>collaterals 列表. |
| [].collaterals[].minUsdValue | string |  | min Usd Value.<br>字段说明：min Usd Value.<br>例: `0` |
| [].collaterals[].maxUsdValue | string |  | max Usd Value.<br>字段说明：max Usd Value.<br>例: `13000000` |
| [].collaterals[].discountRate | string |  | discount Rate.<br>discount 利率.<br>例: `1` |
| [].assetNames | string[] |  | asset Names list.<br>资产 Names 列表. |

## Get All Cross Margin Pairs (MARKET_DATA)（获取所有全仓杠杆交易对 (MARKET_DATA)）

`GET /sapi/v1/margin/allPairs`

Get All Cross Margin Pairs

获取所有全仓杠杆交易对

Operation ID: `getAllCrossMarginPairs`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BNBBTC` |

### 响应 200：Get All Cross Margin Pairs / 获取All Cross 杠杆 Pairs

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].base | string |  | base.<br>字段说明：base.<br>例: `BNB` |
| [].id | integer (int64) |  | id.<br>字段说明：ID.<br>例: `351637150141315840` |
| [].isBuyAllowed | boolean |  | is Buy Allowed.<br>字段说明：is Buy Allowed.<br>例: `True` |
| [].isMarginTrade | boolean |  | is Margin Trade.<br>is 杠杆 交易.<br>例: `True` |
| [].isSellAllowed | boolean |  | is Sell Allowed.<br>字段说明：is Sell Allowed.<br>例: `True` |
| [].quote | string |  | quote.<br>字段说明：quote.<br>例: `BTC` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| [].delistTime | integer (int64) |  | delist Time.<br>delist 时间.<br>例: `1704973040` |

## Get All Isolated Margin Symbol (MARKET_DATA)（获取所有逐仓杠杆交易对 (MARKET_DATA)）

`GET /sapi/v1/margin/isolated/allPairs`

Get All Isolated Margin Symbol

获取所有逐仓杠杆交易对

Operation ID: `getAllIsolatedMarginSymbol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BNBBTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>毫秒时间戳。<br>例: `1770736694138` |

### 响应 200：Get All Isolated Margin Symbol / 获取All Isolated 杠杆 交易对

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].base | string |  | base.<br>字段说明：base.<br>例: `BNB` |
| [].isBuyAllowed | boolean |  | is Buy Allowed.<br>字段说明：is Buy Allowed.<br>例: `True` |
| [].isMarginTrade | boolean |  | is Margin Trade.<br>is 杠杆 交易.<br>例: `True` |
| [].isSellAllowed | boolean |  | is Sell Allowed.<br>字段说明：is Sell Allowed.<br>例: `True` |
| [].quote | string |  | quote.<br>字段说明：quote.<br>例: `BTC` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |

## Get All Margin Assets (MARKET_DATA)（获取所有杠杆资产信息 (MARKET_DATA)）

`GET /sapi/v1/margin/allAssets`

Get All Margin Assets.

获取所有杠杆资产信息

Operation ID: `getAllMarginAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDC` |

### 响应 200：Get All Margin Assets / 获取All 杠杆 Assets

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].assetFullName | string |  | asset Full Name.<br>资产 Full Name.<br>例: `USD coin` |
| [].assetName | string |  | asset Name.<br>资产 Name.<br>例: `USDC` |
| [].isBorrowable | boolean |  | is Borrowable.<br>is 借款able.<br>例: `True` |
| [].isMortgageable | boolean |  | is Mortgageable.<br>字段说明：is Mortgageable.<br>例: `True` |
| [].userMinBorrow | string |  | user Min Borrow.<br>user Min 借款.<br>例: `5.00000000` |
| [].userMinRepay | string |  | user Min Repay.<br>user Min 还款.<br>例: `0.00000000` |
| [].delistTime | integer (int64) |  | delist Time.<br>delist 时间.<br>例: `1704973040000` |

## Get Delist Schedule (MARKET_DATA)（查询下架计划 (MARKET_DATA)）

`GET /sapi/v1/margin/delist-schedule`

Get tokens or symbols delist schedule for cross margin and isolated margin

查询全仓和逐仓的币种或币对的下架计划

Operation ID: `getDelistSchedule`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>毫秒时间戳。<br>例: `1770736694138` |

### 响应 200：Get Delist Schedule / 获取Delist Schedule

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].delistTime | integer (int64) |  | delist Time.<br>delist 时间.<br>例: `1686161202000` |
| [].crossMarginAssets | string[] |  | cross Margin Assets list.<br>全仓 杠杆 Assets 列表. |
| [].isolatedMarginSymbols | string[] |  | isolated Margin Symbols list.<br>逐仓 杠杆 Symbols 列表. |

## Get Limit Price Pairs (MARKET_DATA)（查询出价限定的交易对 (MARKET_DATA)）

`GET /sapi/v1/margin/limit-price-pairs`

Query trading pairs with restriction on limit price range.

In margin trading, you can place orders with limit price. Limit price
should be within (-15%, 15%) of current index price for a list of margin
trading pairs. This rule only impacts limit sell orders with limit price
that is lower than current index price and limit buy orders with limit
price that is higher than current index price.

- Buy order: Your order will be rejected with an error message
notification if the limit price is 15% above the index price.

- Sell order: Your order will be rejected with an error message
notification if the limit price is 15% below the index price.

Please review the limit price order placing strategy, backtest and
calibrate the planned order size with the trading volume and order book
depth to prevent trading loss.

查询所有对于高买低卖的限价单施加了价格区间限制的出价限定的交易对。

在杠杆交易中，用户可以设置限价委托单。对于杠杆交易对，限价应在当前指数价格的(-15%,
15%)范围内。此规则仅适用于低于当前指数价格的限价卖出价和高于当前指数价格的限价买入价。


- 买入订单：如果限价高于指数价格的15%，您的委托将被拒绝，并显示错误消息。

- 卖出订单：如果限价低于指数价格的15%，您的委托将被拒绝，并显示错误消息。

请优化修改限价委托策略，并根据交易量和订单簿深度回测和校准计划的限价委托数量规模，以防止交易亏损。

Operation ID: `getLimitPricePairs`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Get Limit Price Pairs / 获取限制 价格 Pairs

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| crossMarginSymbols | string[] |  | cross Margin Symbols list.<br>全仓 杠杆 Symbols 列表. |

## Get list Schedule (MARKET_DATA)（查询上架计划 (MARKET_DATA)）

`GET /sapi/v1/margin/list-schedule`

Get the upcoming tokens or symbols listing schedule for Cross Margin and Isolated Margin.

查询全仓和逐仓的币种或币对的上架计划

Operation ID: `getListSchedule`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>毫秒时间戳。<br>例: `1770736694138` |

### 响应 200：Get list Schedule / 获取列表 Schedule

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].listTime | integer (int64) |  | list Time.<br>列表 时间.<br>例: `1686161202000` |
| [].crossMarginAssets | string[] |  | cross Margin Assets list.<br>全仓 杠杆 Assets 列表. |
| [].isolatedMarginSymbols | string[] |  | isolated Margin Symbols list.<br>逐仓 杠杆 Symbols 列表. |

## Get Margin Asset Risk-Based Liquidation Ratio (MARKET_DATA)（获取杠杆资产风险强制平仓率 (MARKET_DATA)）

`GET /sapi/v1/margin/risk-based-liquidation-ratio`

Get Margin Asset Risk-Based Liquidation Ratio

获取杠杆资产风险强制平仓率

Operation ID: `getMarginAssetRiskBasedLiquidationRatio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Get Margin Asset Risk-Based Liquidation Ratio / 获取杠杆 资产 Risk-Based Liquidation Ratio

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>资产.<br>例: `USDC` |
| [].riskBasedLiquidationRatio | string |  | risk Based Liquidation Ratio.<br>字段说明：risk Based LiquIDation Ratio.<br>例: `0.01` |

## Get Margin Restricted Assets (MARKET_DATA)（获取杠杆受限资产清单 (MARKET_DATA)）

`GET /sapi/v1/margin/restricted-asset`

Get the list of margin-restricted assets.

获取杠杆受限资产清单

Operation ID: `getMarginRestrictedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Get Margin Restricted Assets / 获取杠杆 Restricted Assets

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| openLongRestrictedAsset | string[] |  | open Long Restricted Asset list.<br>open Long Restricted 资产 列表. |
| maxCollateralExceededAsset | string[] |  | max Collateral Exceeded Asset list.<br>max Collateral Exceeded 资产 列表. |

## Query Isolated Margin Tier Data (USER_DATA)（获取逐仓档位信息 (USER_DATA)）

`GET /sapi/v1/margin/isolatedMarginTier`

Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

通过档位获取逐仓杠杆档位数据， 如： https://www.binance.com/en/margin-data

Operation ID: `queryIsolatedMarginTierData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| tier | query | integer (int64) |  | 不传则返回所有逐仓杠杆档位<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Isolated Margin Tier Data / Isolated 杠杆 Tier Data

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].tier | integer (int64) |  | tier.<br>字段说明：tier.<br>例: `1` |
| [].effectiveMultiple | string |  | effective Multiple.<br>字段说明：effective Multiple.<br>例: `10` |
| [].initialRiskRatio | string |  | initial Risk Ratio.<br>字段说明：initial Risk Ratio.<br>例: `1.111` |
| [].liquidationRiskRatio | string |  | liquidation Risk Ratio.<br>字段说明：liquIDation Risk Ratio.<br>例: `1.05` |
| [].baseAssetMaxBorrowable | string |  | base Asset Max Borrowable.<br>base 资产 Max Borrowable.<br>例: `9` |
| [].quoteAssetMaxBorrowable | string |  | quote Asset Max Borrowable.<br>quote 资产 Max Borrowable.<br>例: `70000` |

## Query Liability Coin Leverage Bracket in Cross Margin Pro Mode (MARKET_DATA)（查询全仓杠杆Pro模式下的负债币种杠杆与保证金率 (MARKET_DATA)）

`GET /sapi/v1/margin/leverageBracket`

Liability Coin Leverage Bracket in Cross Margin Pro Mode

查询全仓杠杆Pro模式下的负债币种杠杆与保证金率

Operation ID: `queryLiabilityCoinLeverageBracketInCrossMarginProMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Liability Coin Leverage Bracket in Cross Margin Pro Mode / Liability Coin Leverage Bracket in Cross 杠杆 Pro Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].assetNames | string[] |  | asset Names list.<br>资产 Names 列表. |
| [].rank | integer (int64) |  | rank.<br>字段说明：rank.<br>例: `1` |
| [].brackets | object[] |  | brackets list.<br>brackets 列表. |
| [].brackets[].leverage | integer (int64) |  | leverage.<br>字段说明：leverage.<br>例: `10` |
| [].brackets[].maxDebt | number (float) |  | max Debt.<br>字段说明：max Debt.<br>例: `1000000` |
| [].brackets[].maintenanceMarginRate | number (float) |  | maintenance Margin Rate.<br>maintenance 杠杆 利率.<br>例: `0.02` |
| [].brackets[].initialMarginRate | number (float) |  | initial Margin Rate.<br>initial 杠杆 利率.<br>例: `0.1112` |
| [].brackets[].fastNum | number (float) |  | fast Num.<br>字段说明：fast Num.<br>例: `60000` |

## Query Margin Available Inventory (USER_DATA)（杠杆可用放贷库存查询 (USER_DATA)）

`GET /sapi/v1/margin/available-inventory`

Margin available Inventory query

杠杆可用放贷库存查询

Operation ID: `queryMarginAvailableInventory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | string | 是 | 枚举: `MARGIN`, `ISOLATED`<br>例: `MARGIN` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Available Inventory / 杠杆 Available Inventory

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object |  | Available inventory per asset. Keys are asset symbols, values are available amounts.<br>每个资产的可用库存。键为资产符号，值为可用数量。 |
| updateTime | integer (int64) |  | update Time.<br>update 时间.<br>例: `1699272487` |

## Query Margin PriceIndex (MARKET_DATA)（查询杠杆价格指数 (MARKET_DATA)）

`GET /sapi/v1/margin/priceIndex`

Query Margin PriceIndex

查询杠杆价格指数

Operation ID: `queryMarginPriceindex`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBBTC` |

### 响应 200：Margin PriceIndex / 杠杆 价格Index

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| calcTime | integer (int64) |  | calc Time.<br>calc 时间.<br>例: `1562046418000` |
| price | string |  | price.<br>价格.<br>例: `0.00333930` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |

## Start User Data Stream (USER_STREAM)（生成listenKey (USER_STREAM)）

`POST /sapi/v1/margin/listen-key`

Start a new user data stream.

创建一个新的user data stream，返回值为一个listenKey

Operation ID: `startUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | listen Key.<br>列表en 密钥.<br>例: `T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhd` |

## Keepalive User Data Stream (USER_STREAM)（延长listenKey有效期 (USER_STREAM)）

`PUT /sapi/v1/margin/listen-key`

Keepalive a user data stream to prevent a time out.

有效期延长至本次调用后24小时。

Operation ID: `keepaliveUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string | 是 | 例: `None` |

### 响应 200：OK / 成功

## Close User Data Stream (USER_STREAM)（关闭listenKey (USER_STREAM)）

`DELETE /sapi/v1/margin/listen-key`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功

## Start User Data Stream V2 (USER_STREAM)（生成listenKey V2 (USER_STREAM)）

`POST /sapi/v2/margin/listen-key`

Start a new user data stream.

创建一个新的user data stream，返回值为一个listenKey

Operation ID: `startUserDataStreamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | listen Key.<br>列表en 密钥.<br>例: `T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhd` |

## Keepalive User Data Stream V2 (USER_STREAM)（延长listenKey有效期 V2 (USER_STREAM)）

`PUT /sapi/v2/margin/listen-key`

Keep alive a user data stream to prevent a timeout. Each successful request extends the listen key validity for 1 hour.

有效期延长至本次调用后1小时。

Operation ID: `keepaliveUserDataStreamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string | 是 | 例: `None` |

### 响应 200：OK / 成功

## Close User Data Stream V2 (USER_STREAM)（关闭listenKey V2 (USER_STREAM)）

`DELETE /sapi/v2/margin/listen-key`

Close out a user data stream.

**Note:** After this request, you will receive another WebSocket message:

```json
{
  "e": "eventStreamTerminated",
  "E": 1793646860552
}
```

- `e` (string): event type. Example: `eventStreamTerminated`
- `E` (integer): current timestamp. Example: `1793646860552`

关闭某账户数据流。

**说明：** 调用此接口后，您将收到另一条 WebSocket 消息：

```json
{
  "e": "eventStreamTerminated",
  "E": 1793646860552
}
```

- `e`（string）：事件类型。示例：`eventStreamTerminated`
- `E`（integer）：当前时间戳。示例：`1793646860552`

Operation ID: `closeUserDataStreamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功

## Query Special key(Low Latency Trading) (TRADE)（查询低延迟交易SpecialKey (TRADE)）

`GET /sapi/v1/margin/apiKey`

Query Special Key Information.

This only applies to Special Key for Low Latency Trading.

查询SpecialKey信息，仅适用于低延迟交易接口的SpecialKey。

Operation ID: `querySpecialKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| apiKey | query | string | 是 | 例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Special key / 专用 密钥

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string |  | api Key.<br>API密钥.<br>例: `npOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoGx` |
| ip | string |  | 0.0.0.0 is just an initial statereference (no extra meaning).<br>字段说明：0.0.0.0 is just an initial statereference (no extra meaning).<br>例: `0.0.0.0,192.168.0.1,192.168.0.2` |
| apiName | string |  | api Name.<br>字段说明：api Name.<br>例: `testName` |
| type | string |  | type.<br>类型.<br>例: `RSA` |
| permissionMode | string |  | permission Mode.<br>permission 模式.<br>例: `TRADE` |

## Create Special Key(Low-Latency Trading) (TRADE)（新建低延迟交易SpecialKey (TRADE)）

`POST /sapi/v1/margin/apiKey`

**Eligibility**

- Binance Margin offers low-latency trading through a [special key](https://www.binance.com/en/support/faq/frequently-asked-questions-on-margin-special-api-key-3208663e900d4d2e9fec4140e1832f4e), available exclusively to users with VIP level 7 or higher.
- If you are VIP level 6 or below, please contact your VIP manager for eligibility criterias.
- All new Margin Special Key users are required to read, understand, and agree to the Margin Special Key Supplemental Product Terms at the master account level before creating a Margin Special Key.
- Once signed at the master account level, the agreement applies to all sub-accounts. The master account and all sub-accounts (Cross Margin Classic and Portfolio Margin Pro) are authorized to create a Margin Special Key and are subject to the LiquidationLoan policy.

For more information, please refer to [FAQ](https://www.binance.com/en/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e).

**Supported Products:**

- Cross Margin
- Isolated Margin
- Portfolio Margin Pro

**Unsupported Products:**

- Portfolio Margin

We support several types of API keys:

* Ed25519 (recommended)
* HMAC
* RSA

We recommend to **use Ed25519 API keys** as it should provide the best performance and security out of all supported key types. We accept PKCS#8 (BEGIN PUBLIC KEY). For how to generate an RSA key pair to send API requests on Binance. Please refer to the document below [FAQ](https://www.binance.com/en/support/faq/how-to-generate-an-rsa-key-pair-to-send-api-requests-on-binance-2b79728f331e43079b27440d9d15c5db) .

**How to use the Margin Special Key**
- Use the below `sapi` endpoint to create your margin special API Key.
- For accessing the Cross Margin account, do not send the `symbol` parameter.
- For accessing the Isolated Margin account(s), pass the relevant `symbol` parameter in the API Key creation request.
- Use the generated API Key (and Secret key, if applicable) to perform margin trading and listenKey generation via **Spot** REST API (`https://api.binance.com/api/v3/*`) endpoints.

Read [REST API](/products/spot/rest-api#signed-trade-and-user_data-endpoint-security) or [WebSocket API](/products/spot/web-socket-api#request-security) documentation to learn how to use different API keys

You need to enable Permits “Enable Spot & Margin Trading” option for the API Key which requests this endpoint.

**资格要求**

- 杠杆交易为VIP7及以上的用户提供了低延迟交易接口，这类接口通过特定的[SpecialKey](https://www.binance.com/zh-CN/support/faq/%E5%B8%81%E5%AE%89%E6%9D%A0%E6%9D%86-margin-special-key-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-3208663e900d4d2e9fec4140e1832f4e)实现杠杆交易。
- 若您的VIP级别为6及以下，请联系您的VIP经理获取相关SpecialKey的使用许可标准。
- 所有新的 Margin Special Key 用户在创建 Margin Special Key 之前，必须在主账户层级阅读、理解并同意《Margin Special Key 补充产品条款》。
- 主账户签署后，该协议适用于所有子账户。主账户及所有子账户（全仓杠杆经典模式和统一账户Pro模式）均有权创建 Margin Special Key，并受 LiquidationLoan 政策约束。

更多信息请参考 [FAQ](https://www.binance.com/zh-CN/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e)。

**该接口支持以下产品：**

* 全仓杠杆
* 逐仓杠杆
* 统一账户Pro模式

**该接口不支持以下产品：**

* 统一账户普通模式

我们提供以下3类接口：

* Ed25519 (recommended)
* HMAC
* RSA

这3类接口中，我们推荐用户使用**use Ed25519 API keys**，它具有最高的性能和安全系数。

我们接受PKCS#8 (BEGIN PUBLIC KEY). 关于如何生成RSA密钥对发送API请求，请参考 [FAQ](https://www.binance.com/zh-TC/support/faq/%E5%A6%82%E4%BD%95%E5%9C%A8%E5%B9%A3%E5%AE%89%E4%B8%8A%E7%94%9F%E6%88%90-rsa-%E9%87%91%E9%91%B0%E5%B0%8D%E4%B8%A6%E7%99%BC%E9%80%81-api-%E8%AB%8B%E6%B1%82-2b79728f331e43079b27440d9d15c5db) 。

**如何使用杠杆专用密钥**
- 使用以下 `sapi` 接口创建您的杠杆专用 SpecialKey。
- 关于访问全仓杠杆账户，请勿发送 `symbol` 参数。
- 关于访问逐仓杠杆账户，请在创建 SpecialKey 的请求中传入相关的 `symbol` 参数。
- 使用生成的 SpecialKey（以及对应的 Secret key，如适用）通过 **现货** REST API (`https://api.binance.com/api/v3/*`) 端点执行杠杆交易和 listenKey 生成操作。

关于如何使用其他API，请参考[REST API](/products/spot/rest-api#signed-trade-and-user_data-endpoint-security) 或 [WebSocket API](/products/spot/web-socket-api#request-security) 。

您需要为special key开通"允许现货及杠杆交易"权限才能调用此接口。

Operation ID: `createSpecialKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiName | string | 是 | 例: `apiName` |
| symbol | string |  | 例: `BTCUSDT` |
| ip | string |  | Can be added in batches, separated by commas. Max 30 for an API key<br>Can be added in batches, separated by commas. 最大 30 用于 an API Key<br>例: `69.210.67.14,69.210.67.15` |
| publicKey | string |  | 1. If publicKey is inputted it will create an RSA or Ed25519<br>key.<br><br>2. Need to be encoded to URL-encoded format<br>1. If public密钥 is inputted it will create an RSA or Ed25519 密钥. 2. Need to be encoded to URL-encoded format<br>例: `publicKey` |
| permissionMode | string |  | This parameter is only for the Ed25519 API key, and does not effact for other encryption methods. The value can be TRADE (TRADE for all permissions) or READ (READ for USER_DATA, FIX_API_READ_ONLY). The default value is TRADE.<br>This parameter is only for the Ed25519 API key, and does not effact for other encryption methods. The value can be 交易 (交易 for all permissions) or READ (READ for USER_DATA, FIX_API_READ_ONLY). The 默认 value is 交易.<br>枚举: `TRADE`, `READ`<br>默认: `TRADE`<br>例: `READ` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create Special Key / 创建Special Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string |  | api Key.<br>API密钥.<br>例: `npOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoGx` |
| secretKey | string |  | secretKey will be null when creating an RSA key<br>secret密钥 will be null when creating an RSA 密钥<br>例: `87ssWB7azoy6ACRfyp6OVOL5U3rtZptX31QWw2kWjl1jHEYRbyM1pd6qykRBQw8p` |
| type | string |  | HMAC_SHA256 or RSA<br>字段说明：HMAC_SHA256 or RSA<br>例: `HMAC_SHA256` |

## Delete Special Key(Low-Latency Trading) (TRADE)（删除Special Key(Low-Latency Trading) (TRADE)）

`DELETE /sapi/v1/margin/apiKey`

Deleting your Margin Special Key alone does not exit you from the Margin Special Key framework or discharge your obligations under the Margin Special Key Supplemental Product Terms. To fully exit, you must:

1. Delete your Margin Special Key.
2. Ensure there are no outstanding liabilities on the account.
3. Call the Exit Margin Special Key API endpoint.
4. Confirm the exit status via the API response.

Only after step 4 is completed and the exit status is confirmed by Binance will your account revert to standard liquidation logic and no longer be subject to the Margin Special Key Supplemental Product Terms.

If apiKey is given, apiName will be ignored. If apiName is given with no
apiKey, all apikeys with given apiName will be deleted.

You need to enable Permits “Enable Spot & Margin” option for the API Key
which requests this endpoint.

仅删除您的 Margin Special Key 并不代表您退出 Margin Special Key 框架，也不解除您在《Margin Special Key 补充产品条款》下的相关义务。如需完全退出，您必须完成以下步骤：

1. 删除您的 Margin Special Key。
2. 确保账户中没有未结清的负债。
3. 调用”退出 Margin Special Key”API 接口。
4. 通过 API 响应确认退出状态。

只有在第 4 步完成且退出状态经 Binance 通过 API 确认后，您的账户才会恢复标准强平逻辑，并不再受《Margin Special Key 补充产品条款》的约束。

如果提供了apiKey参数，则apiName将会被忽略；如果只提供了apiName而没有apiKey，则以apiName为命名的所有apiKey都会被删除。

您需要为special key开通”允许现货及杠杆交易”权限才能调用此接口。

Operation ID: `deleteSpecialKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| apiKey | query | string |  | 例: `apiKey` |
| apiName | query | string |  | 例: `apiName` |
| symbol | query | string |  | 逐仓 杠杆 pair<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Edit ip for Special Key(Low-Latency Trading) (TRADE)（修改可供SpecialKey执行的IP地址 (TRADE)）

`PUT /sapi/v1/margin/apiKey/ip`

Edit ip restriction. This only applies to Special Key for Low Latency
Trading.

You need to enable Permits “Enable Spot & Margin” option for the API Key
which requests this endpoint.

修改可供低延迟交易的SpecialKey执行的IP地址, 仅适用低延迟交易SpecialKey。

该接口需开通“Enable Spot & Margin”的权限。

Operation ID: `editIpForSpecialKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string | 是 | 例: `apiKey` |
| symbol | string |  | isolated margin pair<br>isolated 杠杆 pair<br>例: `BTCUSDT` |
| ip | string | 是 | Can be added in batches, separated by commas. Max 30 for an API key<br>Can be added in batches, separated by commas. Max 30 for an API密钥<br>例: `24.156.99.202` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Exit Special Key Mode (TRADE)（退出Special Key模式 (TRADE)）

`POST /sapi/v1/margin/exit-special-key-mode`

Exit the Margin Special Key mode for Cross Margin Classic accounts.

**All outstanding liabilities under the Cross Margin Classic account must be fully repaid before calling this endpoint.** Deleting the Margin Special Key alone does not constitute a valid exit.

When a user creates a Margin Special API Key, the account enters "Special Key Mode". Upon a successful request, the following actions will be performed atomically:

1. All existing Margin Special API Keys under the Cross Margin Classic mode account will be deleted.
2. All pre-execution margin checks (including Open-order-loss calculation) will revert to standard mode.
3. A cooldown period (default: 24 hours) will be enforced, during which the account will not be permitted to create new Margin Special API Keys.

For more information, please refer to [FAQ](https://www.binance.com/en/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e).

**Preconditions:**

The following conditions must be met; otherwise the request will be rejected:

- Account type must be **Cross Margin Classic**.
- Account must currently be in **Special Key Mode**. If not, the request silently succeeds.
- Account must **not be in liquidation**.
- Account must **have no liability**.

You need to enable "Permits Enable Spot & Margin Trading" option for the API Key which requests this endpoint.

退出全仓杠杆账户经典模式的 Margin Special Key 模式。

**调用本接口前，须确保全仓杠杆账户经典模式下负债已全额还清。**请注意，仅删除 Margin Special Key 并不构成有效退出。

当用户创建 Margin Special Key 后，账户即进入"Margin Special Key 模式"。此接口请求成功后，将自动执行以下操作：

1. 全仓杠杆账户经典模式下的所有 Margin Special Key 将被删除。
2. 所有操作前的保证金检查（包括开仓亏损计算）将恢复为标准模式。
3. 将执行冷却期（默认：24 小时），冷却期内账户不得创建新的 Margin Special Key。

更多信息请参考 [FAQ](https://www.binance.com/zh-CN/support/faq/detail/3208663e900d4d2e9fec4140e1832f4e)。

**前置条件：**

请求需满足以下条件，否则将被拒绝：

- 账户类型必须为**全仓经典(Cross Margin Classic)**。
- 账户必须当前处于 **Special Key 模式**。如不在该模式下，请求将静默成功。
- 账户**不能处于强制平仓中**。
- 账户**不能有负债**。

您需要为请求此接口的 API key 启用"允许现货及杠杆交易"权限。

Operation ID: `exitSpecialKeyMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | The value cannot be greater than `60000`<br>赋值不能大于 `60000`<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Exit Special Key Mode / 退出Special Key模式

## Get Force Liquidation Record (USER_DATA)（获取账户强制平仓记录 (USER_DATA)）

`GET /sapi/v1/margin/forceLiquidationRec`

Get Force Liquidation Record

获取账户强制平仓记录

Operation ID: `getForceLiquidationRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| isolatedSymbol | query | string |  | 例: `BTCUSDT` |
| current | query | integer (int64) |  | 当前查询页。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Force Liquidation Record / 获取Force Liquidation Record

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | rows list.<br>rows 列表. |
| rows[].avgPrice | string |  | avg Price.<br>avg 价格.<br>例: `0.00388359` |
| rows[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `31.39000000` |
| rows[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `180015097` |
| rows[].price | string |  | price.<br>价格.<br>例: `0.00388110` |
| rows[].qty | string |  | qty.<br>数量.<br>例: `31.39000000` |
| rows[].side | string |  | side.<br>方向.<br>例: `SELL` |
| rows[].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| rows[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| rows[].isIsolated | boolean |  | is Isolated.<br>is 逐仓.<br>例: `True` |
| rows[].updatedTime | integer (int64) |  | updated Time.<br>updated 时间.<br>例: `1558941374745` |
| total | integer (int64) |  | total.<br>总计.<br>例: `1` |

## Get Small Liability Exchange Coin List (USER_DATA)（查询可小额负债转换的资产 (USER_DATA)）

`GET /sapi/v1/margin/exchange-small-liability`

Query the coins which can be small liability exchange

查询可小额负债转换的币种

Operation ID: `getSmallLiabilityExchangeCoinList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Small Liability Exchange Coin List / 获取Small Liability Exchange Coin 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>资产.<br>例: `ETH` |
| [].interest | string |  | interest.<br>利息.<br>例: `0.00083334` |
| [].principal | string |  | principal.<br>本金.<br>例: `0.001` |
| [].liabilityAsset | string |  | liability Asset.<br>liability 资产.<br>例: `USDT` |
| [].liabilityQty | number (float) |  | liability Qty.<br>liability 数量.<br>例: `0.3552` |

## Small Liability Exchange (MARGIN)（全仓杠杆小额负债转换 (MARGIN)）

`POST /sapi/v1/margin/exchange-small-liability`

Small Liability Exchange

全仓杠杆小额负债转换

Operation ID: `smallLiabilityExchange`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assetNames | string | 是 | The assets list of small liability exchange<br>小额转换的资产列表<br>例: `BTC,ETH` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Get Small Liability Exchange History (USER_DATA)（查询全仓杠杆小额负债转换历史 (USER_DATA)）

`GET /sapi/v1/margin/exchange-small-liability-history`

Get Small liability Exchange History

查询全仓杠杆小额负债转换历史

Operation ID: `getSmallLiabilityExchangeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| current | query | integer (int64) | 是 | 当前页面，<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) | 是 | 默认: `10`<br>例: `10` |
| startTime | query | integer (int64) |  | 默认： 30 days from 当前 时间戳<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | 默认： present 时间戳<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Small Liability Exchange History / 获取Small Liability Exchange 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | total.<br>总计.<br>例: `1` |
| rows | object[] |  | rows list.<br>rows 列表. |
| rows[].asset | string |  | asset.<br>资产.<br>例: `ETH` |
| rows[].amount | string |  | amount.<br>数量.<br>例: `0.00083434` |
| rows[].targetAsset | string |  | target Asset.<br>target 资产.<br>例: `BUSD` |
| rows[].targetAmount | string |  | target Amount.<br>target 数量.<br>例: `1.37576819` |
| rows[].bizType | string |  | biz Type.<br>biz 类型.<br>例: `EXCHANGE_SMALL_LIABILITY` |
| rows[].timestamp | integer (int64) |  | timestamp.<br>时间戳.<br>例: `1672801339253` |

## Query Margin Account's Open Orders (USER_DATA)（查询杠杆账户挂单记录 (USER_DATA)）

`GET /sapi/v1/margin/openOrders`

Query Margin Account's Open Orders

查询杠杆账户挂单记录

Operation ID: `queryMarginAccountsOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | isolated margin pair<br>isolated 杠杆 pair<br>例: `BNBBTC` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's Open Orders / 杠杆 账户's 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `qhcZw71gAkCCTv0t0k8LUK` |
| [].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.00000000` |
| [].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.00000000` |
| [].icebergQty | string |  | iceberg Qty.<br>iceberg 数量.<br>例: `0.00000000` |
| [].isWorking | boolean |  | is Working.<br>字段说明：is Working.<br>例: `True` |
| [].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `211842552` |
| [].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.30000000` |
| [].price | string |  | price.<br>价格.<br>例: `0.00475010` |
| [].side | string |  | side.<br>方向.<br>例: `SELL` |
| [].status | string |  | status.<br>状态.<br>例: `NEW` |
| [].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `0.00000000` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| [].isIsolated | boolean |  | is Isolated.<br>是否是逐仓symbol交易<br>例: `True` |
| [].time | integer (int64) |  | time.<br>时间.<br>例: `1562040170089` |
| [].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| [].type | string |  | type.<br>类型.<br>例: `LIMIT` |
| [].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |
| [].updateTime | integer (int64) |  | update Time.<br>update 时间.<br>例: `1562040170089` |

## Margin Account Cancel all Open Orders on a Symbol (TRADE)（杠杆账户撤销单一交易对的所有挂单 (TRADE)）

`DELETE /sapi/v1/margin/openOrders`

Cancels all active orders on a symbol for margin account.<br></br>
This includes OCO orders.

杠杆账户撤销单一交易对下所有挂单, 包括OCO的挂单。

Operation ID: `marginAccountCancelAllOpenOrdersOnASymbol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Cancel all Open Orders on a Symbol / 杠杆 账户 取消all 未完成订单 on a 交易对

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `True` |
| [].origClientOrderId | string |  | orig Client Order Id.<br>orig 客户端 订单 ID.<br>例: `E6APeyTJvkMvLMYMqu1KQ4` |
| [].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `11` |
| [].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `-1` |
| [].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `pXLV6Hz6mprAcVYpVMTGgx` |
| [].price | string |  | price.<br>价格.<br>例: `0.089853` |
| [].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.178622` |
| [].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.000000` |
| [].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.000000` |
| [].status | string |  | status.<br>状态.<br>例: `CANCELED` |
| [].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| [].type | string |  | type.<br>类型.<br>例: `LIMIT` |
| [].side | string |  | side.<br>方向.<br>例: `BUY` |
| [].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |
| [].contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| [].listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `ALL_DONE` |
| [].listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `ALL_DONE` |
| [].listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `2inzWQdDvZLHbbAmAozX2N` |
| [].transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1585230948299` |
| [].orders | object[] |  | orders list.<br>订单 列表. |
| [].orders[].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `20` |
| [].orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `CwOOIPHSmYywx6jZX77TdL` |
| [].orderReports | object[] |  | order Reports list.<br>订单 Reports 列表. |
| [].orderReports[].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].orderReports[].origClientOrderId | string |  | orig Client Order Id.<br>orig 客户端 订单 ID.<br>例: `CwOOIPHSmYywx6jZX77TdL` |
| [].orderReports[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `20` |
| [].orderReports[].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `1929` |
| [].orderReports[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `pXLV6Hz6mprAcVYpVMTGgx` |
| [].orderReports[].price | string |  | price.<br>价格.<br>例: `0.668611` |
| [].orderReports[].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.690354` |
| [].orderReports[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.000000` |
| [].orderReports[].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.000000` |
| [].orderReports[].status | string |  | status.<br>状态.<br>例: `CANCELED` |
| [].orderReports[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| [].orderReports[].type | string |  | type.<br>类型.<br>例: `STOP_LOSS_LIMIT` |
| [].orderReports[].side | string |  | side.<br>方向.<br>例: `BUY` |
| [].orderReports[].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `0.378131` |
| [].orderReports[].icebergQty | string |  | iceberg Qty.<br>iceberg 数量.<br>例: `0.017083` |

## Query Margin Account's OCO (USER_DATA)（查询杠杆账户 OCO (USER_DATA)）

`GET /sapi/v1/margin/orderList`

Retrieves a specific OCO based on provided optional parameters

根据提供的可选参数检索特定的杠杆账户 OCO 订单。

Operation ID: `queryMarginAccountsOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| symbol | query | string |  | 逐仓杠杆必填，全仓杠杆不支持该参数<br>例: `LTCBTC` |
| orderListId | query | integer (int64) |  | `orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| origClientOrderId | query | string |  | `orderListId` 或 `origClientOrderId` 必须提供一个。<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's OCO / 杠杆 账户's OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `27` |
| contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `h2USkA5YQpaXHPIrkd96xE` |
| transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1565245656253` |
| symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `True` |
| orders | object[] |  | orders list.<br>订单 列表. |
| orders[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `4` |
| orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `qD1gy3kc3Gx0rihm9Y3xwS` |

## Margin Account Cancel OCO (TRADE)（取消杠杆账户 OCO 订单 (TRADE)）

`DELETE /sapi/v1/margin/orderList`

Cancel an entire Order List for a margin account.

取消杠杆账户订单列表。

Operation ID: `marginAccountCancelOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| orderListId | query | integer (int64) |  | `orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| listClientOrderId | query | string |  | `orderListId` 或 `listClientOrderId` 必须被提供<br>例: `1` |
| newClientOrderId | query | string |  | 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Cancel OCO / 杠杆 账户 取消OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `0` |
| contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `ALL_DONE` |
| listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `ALL_DONE` |
| listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `C3wyj4WVEktd7u9aVBRXcN` |
| transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1574040868128` |
| symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `False` |
| orders | object[] |  | orders list.<br>订单 列表. |
| orders[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `2` |
| orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports | object[] |  | order Reports.<br>订单 Reports. |
| orderReports[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orderReports[].origClientOrderId | string |  | orig Client Order Id.<br>orig 客户端 订单 ID.<br>例: `pO9ufTiFGg3nw2fOdgeOXa` |
| orderReports[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `2` |
| orderReports[].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `0` |
| orderReports[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `unfWT8ig8i0uj6lPuYLez6` |
| orderReports[].price | string |  | price.<br>价格.<br>例: `1.00000000` |
| orderReports[].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `10.00000000` |
| orderReports[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.00000000` |
| orderReports[].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.00000000` |
| orderReports[].status | string |  | status.<br>状态.<br>例: `CANCELED` |
| orderReports[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| orderReports[].type | string |  | type.<br>类型.<br>例: `STOP_LOSS_LIMIT` |
| orderReports[].side | string |  | side.<br>方向.<br>例: `SELL` |
| orderReports[].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `1.00000000` |
| orderReports[].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |

## Query Margin Account's Order (USER_DATA)（查询杠杆账户订单 (USER_DATA)）

`GET /sapi/v1/margin/order`

Query Margin Account's Order

查询杠杆账户订单

Operation ID: `queryMarginAccountsOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBBTC` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's Order / 杠杆 账户's 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `ZwfQzuDIGpceVhKW5DvCmO` |
| cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.00000000` |
| executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.00000000` |
| icebergQty | string |  | iceberg Qty.<br>iceberg 数量.<br>例: `0.00000000` |
| isWorking | boolean |  | is Working.<br>字段说明：is Working.<br>例: `True` |
| orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `213205622` |
| origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.30000000` |
| price | string |  | price.<br>价格.<br>例: `0.00493630` |
| side | string |  | side.<br>方向.<br>例: `SELL` |
| status | string |  | status.<br>状态.<br>例: `NEW` |
| stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `0.00000000` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| isIsolated | boolean |  | is Isolated.<br>is 逐仓.<br>例: `True` |
| time | integer (int64) |  | time.<br>时间.<br>例: `1562133008725` |
| timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| type | string |  | type.<br>类型.<br>例: `LIMIT` |
| selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |
| updateTime | integer (int64) |  | update Time.<br>update 时间.<br>例: `1562133008725` |

## Margin Account New Order (TRADE)（杠杆账户下单 (TRADE)）

`POST /sapi/v1/margin/order`

Post a new order for margin account.

杠杆账户下单

权重: 6(UID) or 1500(UID) when sideEffectType is MARGIN_BUY or AUTO_BORROW_REPAY

Operation ID: `marginAccountNewOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| isIsolated | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| quantity | number (float) |  | 例: `1.0` |
| quoteOrderQty | number (float) |  | 例: `1.0` |
| price | number (float) |  | 例: `1.0` |
| stopPrice | number (float) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>用于 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` 订单.<br>例: `1.0` |
| newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent.<br>客户自定义的唯一订单ID。若未发送自动生成。<br>例: `1` |
| icebergQty | number (float) |  | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.<br>与 `LIMIT`, `STOP_LOSS_LIMIT`, 和 `TAKE_PROFIT_LIMIT` 一起使用创建 iceberg 订单.<br>例: `1.0` |
| newOrderRespType | string |  | MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>MARKET and 限制 订单 types 默认 to FULL, all other 订单 默认 to ACK.<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| sideEffectType | string |  | 枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY`, `AUTO_BORROW_REPAY`<br>默认: `NO_SIDE_EFFECT`<br>例: `NO_SIDE_EFFECT` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| selfTradePreventionMode | string |  | 枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`<br>例: `NONE` |
| trailingDelta | integer (int64) |  | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.<br>配合 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 订单使用。<br>例: `100` |
| autoRepayAtCancel | boolean |  | Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repaid after the order is cancelled.<br>只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true<br>默认: `True`<br>例: `True` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account New Order / 杠杆 账户 New 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `26769564559` |
| clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `E156O3KP4gOif65bjuUK5V` |
| isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `False` |
| transactTime | integer (int64) |  | transact Time.<br>transact 时间.<br>例: `1713873075893` |
| price | string |  | price.<br>价格.<br>例: `0` |
| origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.001` |
| executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.001` |
| cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `65.98253` |
| status | string |  | status.<br>状态.<br>例: `FILLED` |
| timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| type | string |  | type.<br>类型.<br>例: `MARKET` |
| side | string |  | side.<br>方向.<br>例: `SELL` |
| selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `EXPIRE_MAKER` |
| marginBuyBorrowAmount | integer (int64) |  | margin Buy Borrow Amount.<br>杠杆 Buy 借款 数量.<br>例: `5` |
| marginBuyBorrowAsset | string |  | margin Buy Borrow Asset.<br>杠杆 Buy 借款 资产.<br>例: `BTC` |
| fills | object[] |  | fills list.<br>fills 列表. |
| fills[].price | string |  | price.<br>价格.<br>例: `65982.53` |
| fills[].qty | string |  | qty.<br>数量.<br>例: `0.001` |
| fills[].commission | string |  | commission.<br>手续费.<br>例: `0.06598253` |
| fills[].commissionAsset | string |  | commission Asset.<br>手续费 资产.<br>例: `USDT` |
| fills[].tradeId | integer (int64) |  | trade Id.<br>交易 ID.<br>例: `3570680726` |

## Margin Account Cancel Order (TRADE)（杠杆账户撤销订单 (TRADE)）

`DELETE /sapi/v1/margin/order`

Cancel an active order for margin account.

杠杆账户撤销有效订单。

Operation ID: `marginAccountCancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `LTCBTC` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| orderId | query | integer (int64) |  | 例: `1` |
| origClientOrderId | query | string |  | 例: `1` |
| newClientOrderId | query | string |  | 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account Cancel Order / 杠杆 账户 取消订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orderId | string |  | order Id.<br>订单 ID.<br>例: `28` |
| origClientOrderId | string |  | orig Client Order Id.<br>orig 客户端 订单 ID.<br>例: `myOrder1` |
| clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `cancelMyOrder1` |
| price | string |  | price.<br>价格.<br>例: `1.00000000` |
| origQty | string |  | orig Qty.<br>orig 数量.<br>例: `10.00000000` |
| executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `8.00000000` |
| cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `8.00000000` |
| status | string |  | status.<br>状态.<br>例: `CANCELED` |
| timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| type | string |  | type.<br>类型.<br>例: `LIMIT` |
| side | string |  | side.<br>方向.<br>例: `SELL` |
| isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `True` |

## Margin Account New OCO (TRADE)（杠杆账户 OCO 下单 (TRADE)）

`POST /sapi/v1/margin/order/oco`

Send in a new OCO for a margin account

杠杆账户发送新 OCO 订单。

权重: 6(UID) or 1500(UID) when sideEffectType is MARGIN_BUY or AUTO_BORROW_REPAY

Operation ID: `marginAccountNewOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `LTCBTC` |
| isIsolated | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| listClientOrderId | string |  | A unique Id for the entire orderList<br>A unique ID for the entire 订单列表<br>例: `1` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | 例: `1.0` |
| limitClientOrderId | string |  | A unique Id for the limit order<br>A unique ID for the 限制 订单<br>例: `1` |
| price | number (float) | 是 | 例: `1.0` |
| limitIcebergQty | number (float) |  | 例: `1.0` |
| stopClientOrderId | string |  | A unique Id for the stop loss/stop loss limit leg<br>A unique ID for the stop loss/stop loss 限制 leg<br>例: `1` |
| stopPrice | number (float) | 是 | 例: `1.0` |
| stopLimitPrice | number (float) |  | If provided, `stopLimitTimeInForce` is required.<br>If provIDed, `stop限制时间InForce` is required.<br>例: `1.0` |
| stopIcebergQty | number (float) |  | 例: `1.0` |
| stopLimitTimeInForce | string |  | 枚举: `GTC`, `FOK`, `IOC`<br>例: `GTC` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| sideEffectType | string |  | 枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY`, `AUTO_BORROW_REPAY`<br>默认: `NO_SIDE_EFFECT`<br>例: `NO_SIDE_EFFECT` |
| selfTradePreventionMode | string |  | 枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`<br>例: `NONE` |
| autoRepayAtCancel | boolean |  | Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled.<br>Only when MARGIN_BUY or AUTO_BORROW_REPAY 订单 takes effect, true means that the debt generated by the 订单 needs to be 还款 after the 订单 is cancelled.<br>默认: `True`<br>例: `False` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account New OCO / 杠杆 账户 New OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `0` |
| contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `JYVpp3F0f5CAG15DhtrqLp` |
| transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1563417480525` |
| symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| marginBuyBorrowAmount | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `5` |
| marginBuyBorrowAsset | string |  | will not return if no margin trade happens<br>下单后没有发生借款则不返回该字段<br>例: `BTC` |
| isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `False` |
| orders | object[] |  | orders list.<br>订单 列表. |
| orders[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `2` |
| orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports | object[] |  |  |
| orderReports[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| orderReports[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `2` |
| orderReports[].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `0` |
| orderReports[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `Kk7sqHb9J6mJWTMDVW7Vos` |
| orderReports[].transactTime | integer (int64) |  | transact Time.<br>transact 时间.<br>例: `1563417480525` |
| orderReports[].price | string |  | price.<br>价格.<br>例: `0.000000` |
| orderReports[].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.624363` |
| orderReports[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.000000` |
| orderReports[].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.000000` |
| orderReports[].status | string |  | status.<br>状态.<br>例: `NEW` |
| orderReports[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| orderReports[].type | string |  | type.<br>类型.<br>例: `STOP_LOSS` |
| orderReports[].side | string |  | side.<br>方向.<br>例: `BUY` |
| orderReports[].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `0.960664` |
| orderReports[].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |

## Margin Account New OTO (TRADE)（杠杆账户OTO下单 (TRADE)）

`POST /sapi/v1/margin/order/oto`

Post a new OTO order for margin account:

- An OTO (One-Triggers-the-Other) is an order list comprised of 2
orders.

- The first order is called the **working order** and must be `LIMIT` or
`LIMIT_MAKER`. Initially, only the working order goes on the order book.

- The second order is called the **pending order**. It can be any order
type except for `MARKET` orders using parameter `quoteOrderQty`. The
pending order is only placed on the order book when the working order
gets **fully filled**.

- If either the working order or the pending order is cancelled
individually, the other order in the order list will also be canceled or
expired.

- When the order list is placed, if the working order gets **immediately
fully filled**, the placement response will show the working order as
`FILLED` but the pending order will still appear as `PENDING_NEW`. You
need to query the status of the pending order again to see its updated
status.

- OTOs add **2 orders** to the unfilled order count,
`EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

发送一个新的 OTO 订单。

- 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.

- 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。

- 第二个订单被称为**待处理订单**。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET`
订单。只有当生效订单**完全成交**时，待处理订单才会被自动下单。

- 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。

- 如果生效订单在下订单列表后**立即完全成交**，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为
`PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。

- `OTO` 订单将**2 个订单**添加到未成交订单计数，`EXCHANGE_MAX_NUM_ORDERS` 过滤器和
`MAX_NUM_ORDERS` 过滤器中。

权重: 6(UID) or 1500(UID) when sideEffectType is MARGIN_BUY or AUTO_BORROW_REPAY

Operation ID: `marginAccountNewOto`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| isIsolated | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br/>A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired.<br/>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>Arbitrary unique ID among open 订单 lists. 若不传则自动生成。<br/>A new 订单 列表 with the same listClientOrderId is accepted only when the previous one is filled or completely expired.<br/>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>例: `1` |
| newOrderRespType | string |  | MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>MARKET and 限制 订单 types 默认 to FULL, all other 订单 默认 to ACK.<br>枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| sideEffectType | string |  | 枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_BORROW_REPAY`<br>例: `NO_SIDE_EFFECT` |
| selfTradePreventionMode | string |  | 枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`<br>例: `NONE` |
| autoRepayAtCancel | boolean |  | Only when MARGIN_BUY order takes effect, true means that the debt generated by the order needs to be repaid after the order is cancelled.<br>仅在相关订单生效时，true 表示撤单后需归还订单产生的负债。<br>默认: `True`<br>例: `True` |
| workingType | string | 是 | 枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | 枚举: `BUY`, `SELL`<br>例: `SELL` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>Arbitrary unique ID among open 订单 for the working 订单. 若不传则自动生成。<br>例: `1` |
| workingPrice | number (float) | 是 | 例: `1.0` |
| workingQuantity | number (float) | 是 | Sets the quantity for the working order.<br>Sets the quantity 用于 the working 订单.<br>例: `1.0` |
| workingIcebergQty | number (float) | 是 | This can only be used if `workingTimeInForce` is `GTC`.<br>This can 仅 be used if `working 时间 In Force` is `GTC`.<br>例: `1.0` |
| workingTimeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| pendingType | string | 是 | 枚举: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| pendingSide | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingClientOrderId | string |  | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>Arbitrary unique ID among open 订单 for the pending 订单. 若不传则自动生成。<br>例: `1` |
| pendingPrice | number (float) |  | 例: `1.0` |
| pendingStopPrice | number (float) |  | 例: `1.0` |
| pendingTrailingDelta | number (float) |  | 例: `1.0` |
| pendingQuantity | number (float) | 是 | Sets the quantity for the pending order.<br>Sets the quantity 用于 the pending 订单.<br>例: `1.0` |
| pendingIcebergQty | number (float) |  | This can only be used if `pendingTimeInForce` is `GTC`.<br>This can 仅 be used if `pending 时间 In Force` is `GTC`.<br>例: `1.0` |
| pendingTimeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `GTC` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account New OTO / 杠杆 账户 New OTO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `13551` |
| contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OTO` |
| listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `JDuOrsu0Ge8GTyvx8J7VTD` |
| transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1725521998054` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| isIsolated | boolean |  | is Isolated.<br>is 逐仓.<br>例: `False` |
| orders | object[] |  | orders list.<br>订单 列表. |
| orders[].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `29896699` |
| orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `y8RB6tQEMuHUXybqbtzTxk` |
| orderReports | object[] |  | order Reports list.<br>订单 Reports 列表. |
| orderReports[].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| orderReports[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `29896699` |
| orderReports[].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `13551` |
| orderReports[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `y8RB6tQEMuHUXybqbtzTxk` |
| orderReports[].transactTime | integer (int64) |  | transact Time.<br>transact 时间.<br>例: `1725521998054` |
| orderReports[].price | string |  | price.<br>价格.<br>例: `80000.00000000` |
| orderReports[].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `0.02000000` |
| orderReports[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0` |
| orderReports[].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0` |
| orderReports[].status | string |  | status.<br>状态.<br>例: `NEW` |
| orderReports[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| orderReports[].type | string |  | type.<br>类型.<br>例: `LIMIT` |
| orderReports[].side | string |  | side.<br>方向.<br>例: `SELL` |
| orderReports[].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |

## Margin Account New OTOCO (TRADE)（杠杆账户OTOCO下单 (TRADE)）

`POST /sapi/v1/margin/order/otoco`

Post a new OTOCO order for margin account：


- An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list
comprised of 3 orders.

- The first order is called the **working order** and must be `LIMIT` or
`LIMIT_MAKER`. Initially, only the working order goes on the order book.
  - The behavior of the working order is the same as the OTO.
- OTOCO has 2 pending orders (pending above and pending below), forming
an OCO pair. The pending orders are only placed on the order book when
the working order gets **fully filled**.
  - The rules of the pending above and pending below follow the same rules as the [Order List OCO](https://developers.binance.com/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-new-oco).
- OTOCOs add **3 orders** against the unfilled order count,
`EXCHANGE_MAX_NUM_ORDERS` filter, and `MAX_NUM_ORDERS` filter.

杠杆账户OTOCO下单：


- 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。

- 第一个订单被称为 生效订单，必须为LIMIT 或 LIMIT_MAKER类型的订单。最初，订单簿上只有生效订单。
  - 生效订单的行为与此一致 OTO。
- 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO
订单列表。只有当生效订单 完全成交时，待处理订单们才会被自动下单。
  - 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [Order List OCO](https://developers.binance.com/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-new-oco)。
- `OTOCO` 在未成交订单计数，`EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS`
过滤器的基础上添加**3个订单**。

权重: 6(UID) or 1500(UID) when sideEffectType is MARGIN_BUY or AUTO_BORROW_REPAY

Operation ID: `marginAccountNewOtoco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTCUSDT` |
| isIsolated | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| sideEffectType | string |  | 枚举: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_BORROW_REPAY`<br>例: `NO_SIDE_EFFECT` |
| autoRepayAtCancel | boolean |  | Only when MARGIN_BUY order takes effect, true means that the debt generated by the order needs to be repaid after the order is cancelled.<br>只有在自动借款单生效时，true表示的是撤单后需要把订单产生的借款归还，默认为true<br>默认: `True`<br>例: `True` |
| listClientOrderId | string |  | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.<br>整个订单列表的唯一ID。 如果未发送则自动生成。仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。`listClientOrderId` 与 `workingClientOrderId`， `pendingAboveClientOrderId` 以及 `pendingBelowClientOrderId` 不同。<br>例: `1` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`, `FULL`<br>例: `ACK` |
| selfTradePreventionMode | string |  | 枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`<br>例: `NONE` |
| workingType | string | 是 | 枚举: `LIMIT`, `LIMIT_MAKER`<br>例: `LIMIT` |
| workingSide | string | 是 | 枚举: `BUY`, `SELL`<br>例: `SELL` |
| workingClientOrderId | string |  | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>用于标识生效订单的唯一ID。如果未发送则自动生成。<br>例: `1` |
| workingPrice | number (float) | 是 | 例: `1.0` |
| workingQuantity | number (float) | 是 | 例: `1.0` |
| workingIcebergQty | number (float) |  | This can only be used if `workingTimeInForce` is `GTC`.<br>只有当 `workingTimeInForce` 为 `GTC` 时才能使用。<br>例: `1.0` |
| workingTimeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `FOK` |
| pendingSide | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| pendingQuantity | number (float) | 是 | 例: `1.0` |
| pendingAboveType | string | 是 | 枚举: `LIMIT_MAKER`, `STOP_LOSS`, `STOP_LOSS_LIMIT`<br>例: `LIMIT_MAKER` |
| pendingAboveClientOrderId | string |  | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>用于标识待处理上方订单的唯一ID。如果未发送则自动生成。<br>例: `1` |
| pendingAbovePrice | number (float) |  | 例: `1.0` |
| pendingAboveStopPrice | number (float) |  | 例: `1.0` |
| pendingAboveTrailingDelta | number (float) |  | 例: `1.0` |
| pendingAboveIcebergQty | number (float) |  | This can only be used if `pendingAboveTimeInForce` is `GTC`.<br>只有当 `pendingAboveTimeInForce` 为 `GTC` 时才能使用。<br>例: `1.0` |
| pendingAboveTimeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `FOK` |
| pendingBelowType | string |  | 枚举: `LIMIT_MAKER`, `STOP_LOSS`, `STOP_LOSS_LIMIT`<br>例: `LIMIT_MAKER` |
| pendingBelowClientOrderId | string |  | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>用于标识待处理上方订单的唯一ID。如果未发送则自动生成。<br>例: `1` |
| pendingBelowPrice | number (float) |  | 例: `1.0` |
| pendingBelowStopPrice | number (float) |  | 例: `1.0` |
| pendingBelowTrailingDelta | number (float) |  | 例: `1.0` |
| pendingBelowIcebergQty | number (float) |  | This can only be used if `pendingBelowTimeInForce` is `GTC`.<br>只有当 `pendingBelowTimeInForce` 为 `GTC` 时才能使用。<br>例: `1.0` |
| pendingBelowTimeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`<br>例: `FOK` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account New OTOCO / 杠杆 账户 New OTOCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `13509` |
| contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OTO` |
| listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `u2AUo48LLef5qVenRtwJZy` |
| transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1725521881300` |
| symbol | string |  | symbol.<br>交易对.<br>例: `BNBUSDT` |
| isIsolated | boolean |  | is Isolated.<br>is 逐仓.<br>例: `False` |
| orders | object[] |  | orders list.<br>订单 列表. |
| orders[].symbol | string |  | symbol.<br>交易对.<br>例: `BNBUSDT` |
| orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `28282534` |
| orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `IfYDxvrZI4kiyqYpRH13iI` |
| orderReports | object[] |  | order Reports list.<br>订单 Reports 列表. |
| orderReports[].symbol | string |  | symbol.<br>交易对.<br>例: `BNBUSDT` |
| orderReports[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `28282534` |
| orderReports[].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `13509` |
| orderReports[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `IfYDxvrZI4kiyqYpRH13iI` |
| orderReports[].transactTime | integer (int64) |  | transact Time.<br>transact 时间.<br>例: `1725521881300` |
| orderReports[].price | string |  | price.<br>价格.<br>例: `300.00000000` |
| orderReports[].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `1.00000000` |
| orderReports[].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0` |
| orderReports[].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0` |
| orderReports[].status | string |  | status.<br>状态.<br>例: `NEW` |
| orderReports[].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| orderReports[].type | string |  | type.<br>类型.<br>例: `LIMIT` |
| orderReports[].side | string |  | side.<br>方向.<br>例: `BUY` |
| orderReports[].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |
| orderReports[].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `299.00000000` |

## Margin Manual Liquidation (TRADE)（杠杆手动强平 (TRADE)）

`POST /sapi/v1/margin/manual-liquidation`

Margin Manual Liquidation

杠杆手动强平

Operation ID: `marginManualLiquidation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | 枚举: `MARGIN`, `ISOLATED`<br>例: `MARGIN` |
| symbol | string |  | When type selects `ISOLATED`, `symbol` must be filled in<br>当 `type` 选择 `ISOLATED` 时，必须填写 `symbol`<br>例: `ETHUSDT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Manual Liquidation / 杠杆 Manual Liquidation

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | asset.<br>资产.<br>例: `ETH` |
| interest | string |  | interest.<br>利息.<br>例: `0.00083334` |
| principal | string |  | principal.<br>本金.<br>例: `0.001` |
| liabilityAsset | string |  | liability Asset.<br>liability 资产.<br>例: `USDT` |
| liabilityQty | number (float) |  | liability Qty.<br>liability 数量.<br>例: `0.3552` |

## Query Current Margin Order Count Usage (TRADE)（查询目前杠杆账户下单数 (TRADE)）

`GET /sapi/v1/margin/rateLimit/order`

Displays the user's current margin order count usage for all intervals.

获取用户在当前时间区间内的杠杆账户下单总数。

Operation ID: `queryCurrentMarginOrderCountUsage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| symbol | query | string |  | 逐仓交易对，查询逐仓杠杆账户必需<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Margin Order Count Usage / 当前 杠杆 订单 Count Usage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].rateLimitType | string |  | rate Limit Type.<br>利率 限制 类型.<br>例: `ORDERS` |
| [].interval | string |  | interval.<br>字段说明：interval.<br>例: `SECOND` |
| [].intervalNum | integer (int64) |  | interval Num.<br>字段说明：interval Num.<br>例: `10` |
| [].limit | integer (int64) |  | limit.<br>限制.<br>例: `10000` |
| [].count | integer (int64) |  | count.<br>字段说明：count.<br>例: `0` |

## Query Margin Account's all OCO (USER_DATA)（查询特定杠杆账户所有 OCO (USER_DATA)）

`GET /sapi/v1/margin/allOrderList`

Retrieves all OCO for a specific margin account based on provided optional parameters

根据提供的可选参数检索特定杠杆账户所有的 OCO 订单。

Operation ID: `queryMarginAccountsAllOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| symbol | query | string |  | 逐仓杠杆必填，全仓杠杆不支持该参数<br>例: `LTCBTC` |
| fromId | query | integer (int64) |  | 如设置fromId, 将返回id > fromId的数据。否则将返回最新数据<br>例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's all OCO / 杠杆 账户's all OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `29` |
| [].contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| [].listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| [].listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `amEEAXryFzFwYF1FeRpUoZ` |
| [].transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1565245913483` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| [].isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `True` |
| [].orders | object[] |  | orders list.<br>订单 列表. |
| [].orders[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `4` |
| [].orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `oD7aesZqjEGlZrbtRpy5zB` |

## Query Margin Account's All Orders (USER_DATA)（查询杠杆账户的所有订单 (USER_DATA)）

`GET /sapi/v1/margin/allOrders`

Query Margin Account's All Orders

查询杠杆账户的所有订单

Operation ID: `queryMarginAccountsAllOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBBTC` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's All Orders / 杠杆 账户's All 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `D2KDy4DIeS56PvkM13f8cP` |
| [].cummulativeQuoteQty | string |  | cummulative Quote Qty.<br>cummulative Quote 数量.<br>例: `0.00000000` |
| [].executedQty | string |  | executed Qty.<br>executed 数量.<br>例: `0.00000000` |
| [].icebergQty | string |  | iceberg Qty.<br>iceberg 数量.<br>例: `0.00000000` |
| [].isWorking | boolean |  | is Working.<br>字段说明：is Working.<br>例: `False` |
| [].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `41295` |
| [].origQty | string |  | orig Qty.<br>orig 数量.<br>例: `5.31000000` |
| [].price | string |  | price.<br>价格.<br>例: `0.22500000` |
| [].side | string |  | side.<br>方向.<br>例: `SELL` |
| [].status | string |  | status.<br>状态.<br>例: `CANCELED` |
| [].stopPrice | string |  | stop Price.<br>stop 价格.<br>例: `0.18000000` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| [].isIsolated | boolean |  | is Isolated.<br>是否是逐仓symbol交易<br>例: `False` |
| [].time | integer (int64) |  | time.<br>时间.<br>例: `1565769338806` |
| [].timeInForce | string |  | time In Force.<br>时间 In Force.<br>例: `GTC` |
| [].type | string |  | type.<br>类型.<br>例: `TAKE_PROFIT_LIMIT` |
| [].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `NONE` |
| [].updateTime | integer (int64) |  | update Time.<br>update 时间.<br>例: `1565769342148` |

## Query Margin Account's Open OCO (USER_DATA)（查询杠杆账户 OCO 挂单 (USER_DATA)）

`GET /sapi/v1/margin/openOrderList`

Query Margin Account's Open OCO

查询杠杆账户 OCO 挂单

Operation ID: `queryMarginAccountsOpenOco`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| symbol | query | string |  | 逐仓杠杆必填，全仓杠杆不支持该参数<br>例: `LTCBTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's Open OCO / 杠杆 账户's 未完成OCO

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `31` |
| [].contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OCO` |
| [].listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| [].listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `wuB13fmulKj3YjdqWEcsnp` |
| [].transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1565246080644` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| [].isIsolated | boolean |  | if isolated margin<br>是否是逐仓symbol交易<br>例: `True` |
| [].orders | object[] |  | orders list.<br>订单 列表. |
| [].orders[].symbol | string |  | symbol.<br>交易对.<br>例: `LTCBTC` |
| [].orders[].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `4` |
| [].orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `r3EH2N76dHfLoSZWIUw1bT` |

## Query Margin Account's Open OTO/OTOCO Order Lists (USER_DATA)（查询杠杆账户 OTO/OTOCO 未完成订单列表 (USER_DATA)）

`GET /sapi/v1/margin/oto/openOrderList`

Retrieves all open OTO / OTOCO order lists of the margin account.


Notes:
- The returned list contains order lists whose `listOrderStatus` is `EXECUTING`, i.e. at least one order of the list is still open (`NEW` / `PARTIALLY_FILLED`).
- For OTO, the `orders` array contains 2 orders: the working order and the pending order.
- For OTOCO, the `orders` array contains 3 orders: the working order and the two pending orders (pending above / pending below).

获取杠杆账户所有未完成的 OTO / OTOCO 订单列表。


说明：
- 返回的列表仅包含 `listOrderStatus` 为 `EXECUTING` 的订单列表，即该列表中至少有一个订单仍处于未完成状态（`NEW` / `PARTIALLY_FILLED`）。
- 对于 OTO，`orders` 数组包含 2 个订单：生效订单和待处理订单。
- 对于 OTOCO，`orders` 数组包含 3 个订单：生效订单和两个待处理订单（pending above / pending below）。

Operation ID: `queryMarginAccountsOpenOtootocoOrderLists`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 仅支持全仓杠杆交易对查询<br>例: `ASTERUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1790063061632` |

### 响应 200：Margin Account's Open OTO/OTOCO Order Lists / 杠杆账户 OTO/OTOCO 未完成订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderListId | integer (int64) |  | order List Id.<br>订单 列表 ID.<br>例: `24867326110` |
| [].contingencyType | string |  | contingency Type.<br>contingency 类型.<br>例: `OTOCO` |
| [].listStatusType | string |  | list Status Type.<br>列表 状态 类型.<br>例: `EXEC_STARTED` |
| [].listOrderStatus | string |  | list Order Status.<br>列表 订单 状态.<br>例: `EXECUTING` |
| [].listClientOrderId | string |  | list Client Order Id.<br>列表 客户端 订单 ID.<br>例: `web_6324e98951224f96b8a24f312abe5067` |
| [].transactionTime | integer (int64) |  | transaction Time.<br>transaction 时间.<br>例: `1790063061632` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `ASTERUSDT` |
| [].orders | object[] |  | orders list.<br>订单 列表. |
| [].orders[].symbol | string |  | symbol.<br>交易对.<br>例: `ASTERUSDT` |
| [].orders[].orderId | integer (int64) |  | order Id. Returns `null` if the working order is not filled yet.<br>订单 ID. 若生效订单未完成，此处返回 null.<br>例: `499470863` |
| [].orders[].status | string |  | status.<br>状态.<br>例: `NEW` |
| [].orders[].clientOrderId | string |  | client Order Id.<br>客户端 订单 ID.<br>例: `web_f8890794e27b42a1a2ef6b5aef79a949` |

## Query Margin Account's Trade List (USER_DATA)（查询杠杆账户交易历史 (USER_DATA)）

`GET /sapi/v1/margin/myTrades`

Query Margin Account's Trade List

查询杠杆账户交易历史

Operation ID: `queryMarginAccountsTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BNBBTC` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| orderId | query | integer (int64) |  | 例: `1` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| fromId | query | integer (int64) |  | 获取该交易ID之后的数据。默认获取最近的交易。<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `500`<br>例: `500` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Margin Account's Trade List / 杠杆 账户's 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].commission | string |  | commission.<br>手续费.<br>例: `0.00006000` |
| [].commissionAsset | string |  | commission Asset.<br>手续费 资产.<br>例: `BTC` |
| [].id | integer (int64) |  | id.<br>字段说明：ID.<br>例: `34` |
| [].isBestMatch | boolean |  | is Best Match.<br>字段说明：is Best Match.<br>例: `True` |
| [].isBuyer | boolean |  | is Buyer.<br>字段说明：is Buyer.<br>例: `False` |
| [].isMaker | boolean |  | is Maker.<br>is 挂单方.<br>例: `False` |
| [].orderId | integer (int64) |  | order Id.<br>订单 ID.<br>例: `39324` |
| [].price | string |  | price.<br>价格.<br>例: `0.02000000` |
| [].qty | string |  | qty.<br>数量.<br>例: `3.00000000` |
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BNBBTC` |
| [].isIsolated | boolean |  | is Isolated.<br>是否是逐仓symbol交易<br>例: `False` |
| [].time | integer (int64) |  | time.<br>时间.<br>例: `1561973357171` |

## Query Prevented Matches (USER_DATA)（查询Prevented Matches (USER_DATA)）

`GET /sapi/v1/margin/myPreventedMatches`

Displays the list of orders that were expired due to STP. (Self-Trade Prevention).

Displays the 列表 of 订单 that were expired due to STP. (Self-交易 Prevention).

Operation ID: `queryPreventedMatches`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | 例: `BTCUSDT` |
| preventedMatchId | query | integer (int64) |  | 例: `1` |
| orderId | query | integer (int64) |  | 例: `1` |
| fromPreventedMatchId | query | integer (int64) |  | 例: `1` |
| isIsolated | query | string |  | 枚举: `TRUE`, `FALSE`<br>默认: `FALSE`<br>例: `FALSE` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Prevented Matches / 字段说明：Prevented Matches

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol.<br>交易对.<br>例: `BTCUSDT` |
| [].preventedMatchId | integer (int64) |  | prevented Match Id.<br>字段说明：prevented Match ID.<br>例: `1` |
| [].takerOrderId | integer (int64) |  | taker Order Id.<br>taker 订单 ID.<br>例: `5` |
| [].makerSymbol | string |  | maker Symbol.<br>maker 交易对.<br>例: `BTCUSDT` |
| [].makerOrderId | integer (int64) |  | maker Order Id.<br>maker 订单 ID.<br>例: `3` |
| [].tradeGroupId | integer (int64) |  | trade Group Id.<br>交易 Group ID.<br>例: `1` |
| [].selfTradePreventionMode | string |  | self Trade Prevention Mode.<br>self 交易 Prevention Mode.<br>例: `EXPIRE_MAKER` |
| [].price | string |  | price.<br>价格.<br>例: `1.100000` |
| [].makerPreventedQuantity | string |  | maker Prevented Quantity.<br>maker Prevented 数量.<br>例: `1.300000` |
| [].transactTime | integer (int64) |  | transact Time.<br>transact 时间.<br>例: `1669101687094` |

## Query Special key List(Low Latency Trading) (TRADE)（查询低延迟交易SpecialKey清单 (TRADE)）

`GET /sapi/v1/margin/api-key-list`

This only applies to Special Key for Low Latency Trading.

查询SpecialKey清单，仅适用低延迟交易SpecialKey。

Operation ID: `querySpecialKeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | 例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Special key List / Special Key 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].apiName | string |  | api Name.<br>字段说明：api Name.<br>例: `testName1` |
| [].apiKey | string |  | api Key.<br>API密钥.<br>例: `znpOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoG` |
| [].ip | string |  | ip.<br>字段说明：ip.<br>例: `192.168.0.1,192.168.0.2` |
| [].type | string |  | type.<br>类型.<br>例: `RSA` |
| [].permissionMode | string |  | permission Mode.<br>permission 模式.<br>例: `TRADE` |

## Query Liquidation Loan (USER_DATA)（查询强平穿仓欠款 (USER_DATA)）

`GET /sapi/v1/margin/liquidation-loan`

Query the current user's cross-margin liquidation loan information, including the original loan amount, repaid amount, and remaining amount. When a cross-margin account is liquidated and the account equity turns negative (bankruptcy), the system generates a liquidation loan record representing the deficit. This represents the shortfall amount denominated in USDC.

查询当前用户的全仓杠杆强平穿仓欠款信息，包括原始欠款金额、已还金额和剩余金额。当全仓杠杆账户被强平且账户权益变为负数（穿仓）时，系统会生成一条穿仓欠款记录。该欠款金额以 USDC 计价。

Operation ID: `queryLiquidationLoan`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Liquidation Loan / 查询强平穿仓欠款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | The asset of the liquidation loan (USDC by default)<br>穿仓欠款的资产（默认USDC）<br>例: `USDC` |
| amount | string |  | Total liquidation loan amount<br>穿仓欠款总金额<br>例: `1000.00000000` |
| repaidAmount | string |  | Amount that has been repaid<br>已还金额<br>例: `300.00000000` |
| remainingAmount | string |  | Outstanding amount remaining to be repaid<br>剩余未还金额<br>例: `700.00000000` |

## Liquidation Loan Repay (MARGIN)（偿还强平穿仓欠款 (MARGIN)）

`POST /sapi/v1/margin/liquidation-loan/repay`

Repays the outstanding cross-margin liquidation loan from the user's spot wallet. A liquidation loan represents the account deficit incurred when account equity turns negative during liquidation (bankruptcy). The repayment amount must be greater than 0 and cannot exceed the remaining loan balance. If the Spot Account has insufficient USDC balance, the repayment will fail.

从现货钱包偿还全仓杠杆强平穿仓欠款。穿仓欠款是指在强平过程中账户权益变为负数时产生的亏损。还款金额必须大于0且不能超过剩余欠款余额。若现货账户 USDC 余额不足，还款将失败。

Operation ID: `liquidationLoanRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | The asset to repay (e.g. USDT, USDC)<br>还款资产 (如 USDT, USDC)<br>例: `USDT` |
| amount | number (float) | 是 | Repayment amount, must be greater than 0<br>还款金额，必须大于0<br>例: `300.00` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidation Loan Repay / 偿还强平穿仓欠款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayId | integer (int64) |  | Unique identifier for this repayment transaction<br>该笔还款交易的唯一标识<br>例: `12345678` |
| asset | string |  | Asset used for repayment<br>还款使用的资产<br>例: `USDT` |
| amount | string |  | Actual repayment amount<br>实际还款金额<br>例: `300.00000000` |
| status | string |  | Repayment status: `SUCCESS` (completed) or `PENDING` (processing)<br>还款状态：`SUCCESS`（已完成）或 `PENDING`（处理中）<br>枚举: `SUCCESS`, `PENDING`<br>例: `SUCCESS` |
| createTime | integer (int64) |  | Unix timestamp (milliseconds) when the repayment was created<br>还款创建时间（Unix毫秒时间戳）<br>例: `1714492800000` |

## Query Liquidation Loan Repay History (USER_DATA)（查询强平穿仓欠款还款历史 (USER_DATA)）

`GET /sapi/v1/margin/liquidation-loan/repay-history`

Query the repayment history of cross-margin liquidation loans (deficit caused by bankruptcy during liquidation). Supports time-range filtering and pagination.

查询全仓杠杆强平穿仓欠款的还款历史。支持时间范围过滤和分页。

Operation ID: `queryLiquidationLoanRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Start time in Unix timestamp (milliseconds). Defaults to 7 days ago if not specified<br>起始时间（Unix毫秒时间戳）。未指定时默认为7天前<br>例: `1714492800000` |
| endTime | query | integer (int64) |  | End time in Unix timestamp (milliseconds). Defaults to now if not specified<br>结束时间（Unix毫秒时间戳）。未指定时默认为当前时间<br>例: `1714579200000` |
| current | query | integer (int64) |  | Current page number, default `1`<br>当前页码，默认 `1`<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Page size, default `50`<br>每页大小，默认 `50`<br>默认: `50`<br>例: `50` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Liquidation Loan Repay History / 查询强平穿仓欠款还款历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of repayment records<br>还款记录总数<br>例: `2` |
| rows | object[] |  |  |
| rows[].repayId | integer (int64) |  | Unique identifier for the repayment transaction<br>还款交易唯一标识<br>例: `12345678` |
| rows[].asset | string |  | Asset used for repayment<br>还款使用的资产<br>例: `USDC` |
| rows[].amount | string |  | The repayment amount<br>还款金额<br>例: `300.00000000` |
| rows[].status | string |  | Repayment status: `SUCCESS` (completed) or `PENDING` (processing)<br>还款状态：`SUCCESS`（已完成）或 `PENDING`（处理中）<br>枚举: `SUCCESS`, `PENDING`<br>例: `SUCCESS` |
| rows[].createTime | integer (int64) |  | Unix timestamp (milliseconds) when the repayment was created<br>还款创建时间（Unix毫秒时间戳）<br>例: `1714492800000` |

## Get Cross Margin Transfer History (USER_DATA)（获取全仓杠杆划转历史 (USER_DATA)）

`GET /sapi/v1/margin/transfer`

Get Cross Margin Transfer History

获取全仓杠杆划转历史

Operation ID: `getCrossMarginTransferHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BNB` |
| type | query | string |  | 枚举: `ROLL_IN`, `ROLL_OUT`<br>例: `ROLL_IN` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | 当前查询页。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| isolatedSymbol | query | string |  | 逐仓交易对，适用于逐仓查询<br>例: `BNBUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Cross Margin Transfer History / 获取Cross 杠杆 划转 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | rows list.<br>rows 列表. |
| rows[].amount | string |  | amount.<br>数量.<br>例: `0.10000000` |
| rows[].asset | string |  | asset.<br>资产.<br>例: `BNB` |
| rows[].status | string |  | status.<br>状态.<br>例: `CONFIRMED` |
| rows[].timestamp | integer (int64) |  | timestamp.<br>时间戳.<br>例: `1566898617` |
| rows[].txId | integer (int64) |  | tx Id.<br>字段说明：tx ID.<br>例: `5240372201` |
| rows[].type | string |  | type.<br>类型.<br>例: `ROLL_IN` |
| rows[].transFrom | string |  | SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN<br>SPOT,FUTURES,FIAT,DELIVERY,MINING,逐仓_杠杆,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_杠杆,全仓_杠杆<br>例: `SPOT` |
| rows[].transTo | string |  | SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN<br>SPOT,FUTURES,FIAT,DELIVERY,MINING,逐仓_杠杆,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_杠杆,全仓_杠杆<br>例: `ISOLATED_MARGIN` |
| rows[].fromSymbol | string |  | from Symbol.<br>from 交易对.<br>例: `BNBUSDT` |
| rows[].toSymbol | string |  | to Symbol.<br>to 交易对.<br>例: `BTCUSDT` |
| total | integer (int64) |  | total.<br>总计.<br>例: `3` |

## Query Max Transfer-Out Amount (USER_DATA)（查询最大可转出额 (USER_DATA)）

`GET /sapi/v1/margin/maxTransferable`

Query Max Transfer-Out Amount

查询最大可转出额

Operation ID: `queryMaxTransferOutAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | 例: `BTC` |
| isolatedSymbol | query | string |  | 逐仓交易对，适用于逐仓查询<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Max Transfer-Out Amount / 最大 划转-Out 数量

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | string |  | amount.<br>数量.<br>例: `3.59498107` |