---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api
api_type: REST
updated_at: 2026-11-20 18:50:27.703954
---

# Options REST API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade Binance Options.

访问市场数据、管理账户，并交易 Binance 期权。

版本: 1.0.0

## 服务地址

- `https://eapi.binance.com`
- `https://testnet.binancefuture.com`

## 接口列表

- `GET /eapi/v1/bill` — Account Funding Flow (USER_DATA)
- `GET /eapi/v1/marginAccount` — Option Margin Account Information (USER_DATA)
- `GET /eapi/v1/time` — Check Server Time
- `GET /eapi/v1/exchangeInfo` — Exchange Information
- `GET /eapi/v1/exerciseHistory` — Historical Exercise Records
- `GET /eapi/v1/index` — Index Price
- `GET /eapi/v1/klines` — Kline/Candlestick Data
- `GET /eapi/v1/openInterest` — Open Interest
- `GET /eapi/v1/mark` — Option Mark Price
- `GET /eapi/v1/depth` — Order Book
- `GET /eapi/v1/blockTrades` — Recent Block Trades List
- `GET /eapi/v1/trades` — Recent Trades List
- `GET /eapi/v1/ping` — Test Connectivity
- `GET /eapi/v1/ticker` — 24hr Ticker Price Change Statistics
- `GET /eapi/v1/block/order/execute` — Query Block Trade Details (USER_DATA)
- `POST /eapi/v1/block/order/execute` — Accept Block Trade Order (TRADE)
- `GET /eapi/v1/block/user-trades` — Account Block Trade List (USER_DATA)
- `POST /eapi/v1/block/order/create` — New Block Trade Order (TRADE)
- `PUT /eapi/v1/block/order/create` — Extend Block Trade Order (TRADE)
- `DELETE /eapi/v1/block/order/create` — Cancel Block Trade Order (TRADE)
- `GET /eapi/v1/block/order/orders` — Query Block Trade Order (TRADE)
- `POST /eapi/v1/countdownCancelAllHeartBeat` — Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
- `GET /eapi/v1/countdownCancelAll` — Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
- `POST /eapi/v1/countdownCancelAll` — Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
- `GET /eapi/v1/mmp` — Get Market Maker Protection Config (TRADE)
- `POST /eapi/v1/mmpReset` — Reset Market Maker Protection Config (TRADE)
- `POST /eapi/v1/mmpSet` — Set Market Maker Protection Config (TRADE)
- `GET /eapi/v1/userTrades` — Account Trade List (USER_DATA)
- `DELETE /eapi/v1/allOpenOrdersByUnderlying` — Cancel All Option Orders By Underlying (TRADE)
- `DELETE /eapi/v1/allOpenOrders` — Cancel all Option orders on specific symbol (TRADE)
- `POST /eapi/v1/batchOrders` — Place Multiple Orders (TRADE)
- `DELETE /eapi/v1/batchOrders` — Cancel Multiple Option Orders (TRADE)
- `GET /eapi/v1/order` — Query Single Order (TRADE)
- `POST /eapi/v1/order` — New Order (TRADE)
- `DELETE /eapi/v1/order` — Cancel Option Order (TRADE)
- `GET /eapi/v1/position` — Option Position Information (USER_DATA)
- `GET /eapi/v1/openOrders` — Query Current Open Option Orders (USER_DATA)
- `GET /eapi/v1/historyOrders` — Query Option Order History (TRADE)
- `POST /eapi/v1/stock/contract` — TradFi Options Contract (USER_DATA)
- `GET /eapi/v1/commission` — User Commission (USER_DATA)
- `GET /eapi/v1/exerciseRecord` — User Exercise Record (USER_DATA)
- `POST /eapi/v1/listenKey` — Start User Data Stream (USER_STREAM)
- `PUT /eapi/v1/listenKey` — Keepalive User Data Stream (USER_STREAM)
- `DELETE /eapi/v1/listenKey` — Close User Data Stream (USER_STREAM)

## Account Funding Flow (USER_DATA)（获取账户资金流水 (USER_DATA)）

`GET /eapi/v1/bill`

Query account funding flows.

获取期权账户资金流水

Operation ID: `accountFundingFlow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| currency | query | string | 是 | Asset type, only support USDT  as of now<br>资产类型目前仅支持USDT<br>枚举: `USDT`<br>例: `USDT` |
| recordId | query | integer (int64) |  | Return the recordId and subsequent data, the latest data is returned by default<br>返回该`recordId`及之后的成交，缺省返回最近的成交<br>例: `100000` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned<br>返回结果集数量<br>默认: `100`<br>例: `20` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Funding Flow / 账户 Funding Flow

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | id<br>ID<br>例: `1125899906842624000` |
| [].asset | string |  | Asset type<br>资产类型<br>例: `USDT` |
| [].amount | string |  | Amount (positive numbers represent inflow, negative numbers represent outflow)<br>数量 (正数为流入，负数为流出)<br>例: `-0.552` |
| [].symbol | string |  | Option symbol the record relates to. Returned only for contract-related types (e.g. `CONTRACT`, `FEE`, `EXERCISE_PNL`, `EXERCISE_FEE`); omitted for other types such as `TRANSFER`. Older records may not include this field.<br>该记录对应的期权交易对。仅在合约相关类型（如 `CONTRACT`、`FEE`、`EXERCISE_PNL`、`EXERCISE_FEE`）中返回；其他类型（如 `TRANSFER`）不返回该字段。较早的记录可能不包含该字段。<br>例: `BTC-200730-9000-C` |
| [].type | string |  | type (fees)<br>类型 (手续费)<br>例: `FEE` |
| [].createDate | integer (int64) |  | Time<br>时间<br>例: `1592449456000` |

## Option Margin Account Information (USER_DATA)（保证金账户信息 (USER_DATA)）

`GET /eapi/v1/marginAccount`

Get current account information.

获取保证金账户信息

Operation ID: `optionMarginAccountInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Option Margin Account Information / Option 杠杆 账户 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | object[] |  | asset<br>资产 |
| asset[].asset | string |  | asset<br>资产<br>例: `USDT` |
| asset[].marginBalance | string |  | margin Balance<br>账户余额<br>例: `10099.448` |
| asset[].equity | string |  | equity<br>账户权益<br>例: `10094.44662` |
| asset[].available | string |  | available<br>账户可用<br>例: `8725.92524` |
| asset[].initialMargin | string |  | initial Margin<br>初始保证金<br>例: `1084.52138` |
| asset[].maintMargin | string |  | maint Margin<br>维持保证金<br>例: `151.00138` |
| asset[].unrealizedPNL | string |  | unrealized PNL<br>未实现盈亏<br>例: `-5.00138` |
| asset[].adjustedEquity | string |  | adjusted Equity<br>margin balance + BTC多仓价值<br>例: `34.13282285` |
| greek | object[] |  | greek |
| greek[].underlying | string |  | underlying<br>标的资产<br>例: `BTCUSDT` |
| greek[].delta | string |  | delta<br>Delta<br>例: `-0.05` |
| greek[].gamma | string |  | gamma<br>Gamma<br>例: `-0.002` |
| greek[].theta | string |  | theta<br>Theta<br>例: `-0.05` |
| greek[].vega | string |  | vega<br>Vega<br>例: `-0.002` |
| time | integer (int64) |  | time<br>时间<br>例: `1762843368098` |
| canTrade | boolean |  | can Trade<br>是否可交易<br>例: `True` |
| canDeposit | boolean |  | can Deposit<br>是否可入金<br>例: `True` |
| canWithdraw | boolean |  | can Withdraw<br>是否可出金<br>例: `True` |
| reduceOnly | boolean |  | reduce Only<br>仅减仓<br>例: `False` |
| tradeGroupId | integer (int64) |  | Trade group ID<br>交易组 ID<br>例: `-1` |

## Check Server Time（获取服务器时间）

`GET /eapi/v1/time`

Test connectivity to the Rest API and get the current server time.

获取服务器时间

Operation ID: `checkServerTime`

### 响应 200：Check Server Time / 检查Server 时间

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serverTime | integer (int64) |  | server Time<br>当前的系统时间<br>例: `1592387156596` |

## Exchange Information（获取交易规则和交易对）

`GET /eapi/v1/exchangeInfo`

Current exchange trading rules and symbol information

获取交易规则和交易对

Operation ID: `exchangeInformation`

### 响应 200：Exchange Information / Exchange 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| timezone | string |  | Time zone used by the server<br>服务器时区<br>例: `UTC` |
| serverTime | integer (int64) |  | Current system time<br>请忽略。如果需要获取当前系统时间，请查询接口 “GET /eapi/v1/time”<br>例: `1592387337630` |
| optionContracts | object[] |  | Option contract underlying asset info<br>期权合约底层资产信息 |
| optionContracts[].baseAsset | string |  | Base currency<br>标的资产<br>例: `BTC` |
| optionContracts[].quoteAsset | string |  | Quotation asset<br>报价资产<br>例: `USDT` |
| optionContracts[].underlying | string |  | Name of the underlying asset of the option contract<br>期权合约底层资产<br>例: `BTCUSDT` |
| optionContracts[].settleAsset | string |  | Settlement currency<br>结算资产<br>例: `USDT` |
| optionAssets | object[] |  | Option asset info<br>期权系统支持资产 |
| optionAssets[].name | string |  | Asset name<br>资产名<br>例: `USDT` |
| optionSymbols | object[] |  | Option trading pair info<br>期权交易对信息 |
| optionSymbols[].expiryDate | integer (int64) |  | expiry time<br>到期时间<br>例: `1660521600000` |
| optionSymbols[].filters | object[] |  | filters |
| optionSymbols[].filters[].filterType | string |  | filter Type<br>例: `PRICE_FILTER` |
| optionSymbols[].filters[].minPrice | string |  | min Price<br>最小价格<br>例: `0.02` |
| optionSymbols[].filters[].maxPrice | string |  | max Price<br>最大价格<br>例: `80000.01` |
| optionSymbols[].filters[].tickSize | string |  | tick Size<br>最小价格精度<br>例: `0.01` |
| optionSymbols[].filters[].minQty | string |  | Minimum order quantity<br>最小下单数量<br>例: `0.01` |
| optionSymbols[].filters[].maxQty | string |  | Maximum order quantity<br>最大下单数量<br>例: `100` |
| optionSymbols[].filters[].stepSize | string |  | step Size<br>数量步长<br>例: `0.01` |
| optionSymbols[].symbol | string |  | Trading pair name<br>交易对<br>例: `BTC-220815-50000-C` |
| optionSymbols[].side | string |  | Direction: CALL long, PUT short<br>期权方向<br>例: `CALL` |
| optionSymbols[].strikePrice | string |  | Strike price<br>行权价<br>例: `50000` |
| optionSymbols[].underlying | string |  | Name of the underlying asset of the option contract<br>期权合约底层资产<br>例: `BTCUSDT` |
| optionSymbols[].unit | integer (int64) |  | Contract unit, the quantity of the underlying asset represented by a single contract.<br>合约单位, 单一合约代表的底层资产数量<br>例: `1` |
| optionSymbols[].liquidationFeeRate | string |  | liquidation fee rate<br>爆仓手续费<br>例: `0.0019000` |
| optionSymbols[].minQty | string |  | Minimum order quantity<br>最小下单数量<br>例: `0.01` |
| optionSymbols[].maxQty | string |  | Maximum order quantity<br>最大下单数量<br>例: `100` |
| optionSymbols[].initialMargin | string |  | Initial Magin Ratio<br>初始保证金率<br>例: `0.15` |
| optionSymbols[].maintenanceMargin | string |  | Maintenance Margin Ratio<br>维持保证金率<br>例: `0.075` |
| optionSymbols[].minInitialMargin | string |  | Min Initial Margin Ratio<br>最低初始保证金率<br>例: `0.1` |
| optionSymbols[].minMaintenanceMargin | string |  | Min Maintenance Margin Ratio<br>最低维持保证金率<br>例: `0.05` |
| optionSymbols[].priceScale | integer (int64) |  | price precision<br>价格精度<br>例: `2` |
| optionSymbols[].quantityScale | integer (int64) |  | quantity precision<br>数量精度<br>例: `2` |
| optionSymbols[].quoteAsset | string |  | Quotation asset<br>报价资产<br>例: `USDT` |
| optionSymbols[].contractType | string |  | Contract type<br>合约类型<br>例: `CRYPTO_OPTIONS` |
| optionSymbols[].underlyingType | string |  | Underlying type<br>标的类型<br>例: `CRYPTO` |
| optionSymbols[].nakedSell | boolean |  | Whether naked selling is allowed for this symbol<br>是否允许该交易对进行裸卖空<br>例: `False` |
| optionSymbols[].status | string |  | Trading Status<br>状态<br>例: `TRADING` |
| rateLimits | object[] |  | rate Limits |
| rateLimits[].rateLimitType | string |  | rate Limit Type<br>限频类型<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | interval<br>时间区间<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | interval Num<br>区间数量<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | limit<br>限制值<br>例: `2400` |

## Historical Exercise Records（历史行权记录）

`GET /eapi/v1/exerciseHistory`

Get historical exercise records.

* REALISTIC_VALUE_STRICKEN -> Exercised
* EXTRINSIC_VALUE_EXPIRED -> Expired OTM

查询行权记录

* REALISTIC_VALUE_STRICKEN 行权
* EXTRINSIC_VALUE_EXPIRED 未行权

Operation ID: `historicalExerciseRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| underlying | query | string |  | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned<br>返回结果集数量，默认值100，最大值100<br>默认: `100`<br>例: `20` |

### 响应 200：Historical Exercise Records / 请参见英文说明：Historical Exercise Records

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol<br>交易对<br>例: `BTC-220121-60000-P` |
| [].strikePrice | string |  | strike price<br>行权价<br>例: `60000` |
| [].realStrikePrice | string |  | real strike price<br>行权结算价格<br>例: `38844.69652571` |
| [].expiryDate | integer (int64) |  | Exercise time<br>行权时间<br>例: `1642752000000` |
| [].strikeResult | string |  | strike result<br>行权结果<br>例: `REALISTIC_VALUE_STRICKEN` |

## Index Price（标的指数价格）

`GET /eapi/v1/index`

Get spot index price for option underlying.

返回指数价格

Operation ID: `indexPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| underlying | query | string | 是 | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |

### 响应 200：Index Price / Index 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| time | integer (int64) |  | time<br>时间<br>例: `1656647305000` |
| indexPrice | string |  | index Price<br>指数价格<br>例: `105917.75` |

## Kline/Candlestick Data（K线数据）

`GET /eapi/v1/klines`

Kline/candlestick bars for an option symbol. Klines are uniquely identified by their open time.

K线数据，每根K线的开盘时间可视为唯一ID

Operation ID: `klineCandlestickData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| interval | query | string | 是 | Time interval<br>时间间隔<br>枚举: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1m` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned<br>返回结果集数量<br>默认: `500`<br>例: `20` |

### 响应 200：Kline/Candlestick Data / K线/Candlestick Data

## Open Interest（合约持仓量）

`GET /eapi/v1/openInterest`

Get open interest for specific underlying asset on specific expiration date.

获取期权持仓量。

Operation ID: `openInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| underlyingAsset | query | string | 是 | Underlying asset.<br>标的资产。<br>例: `ETH/BTC` |
| expiration | query | string | 是 | expiration date<br>到期日<br>例: `221225` |

### 响应 200：Open Interest / 未完成利息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol<br>交易对<br>例: `ETH-221119-1175-P` |
| [].sumOpenInterest | string |  | sum Open Interest<br>总持仓量<br>例: `4.01` |
| [].sumOpenInterestUsd | string |  | sum Open Interest Usd<br>总持仓量(USD)<br>例: `4880.2985615624` |
| [].timestamp | string |  | timestamp<br>时间戳<br>例: `1668754020000` |

## Option Mark Price（查询期权标记价格）

`GET /eapi/v1/mark`

Option mark price and greek info.

查询期权标记价格

Operation ID: `optionMarkPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Option trading pair<br>交易对如<br>例: `BTC-200730-9000-C` |

### 响应 200：Option Mark Price / Option Mark 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol<br>交易对<br>例: `BTC-200730-9000-C` |
| [].markPrice | string |  | Mark price<br>标记价格<br>例: `1343.2883` |
| [].bidIV | string |  | Implied volatility Buy<br>买一隐含波动率<br>例: `1.40000077` |
| [].askIV | string |  | Implied volatility Sell<br>卖一隐含波动率<br>例: `1.50000153` |
| [].markIV | string |  | Implied volatility mark<br>标记价格隐含波动率<br>例: `1.45000000` |
| [].delta | string |  | delta<br>Delta<br>例: `0.55937056` |
| [].theta | string |  | theta<br>Theta<br>例: `3739.82509871` |
| [].gamma | string |  | gamma<br>Gamma<br>例: `0.00010969` |
| [].vega | string |  | vega<br>Vega<br>例: `978.58874732` |
| [].highPriceLimit | string |  | Current highest buy price<br>买最高限价<br>例: `1618.241` |
| [].lowPriceLimit | string |  | Current lowest sell price<br>卖最低限价<br>例: `1068.3356` |
| [].riskFreeInterest | string |  | risk free rate<br>无风险利率<br>例: `0.1` |

## Order Book（深度信息）

`GET /eapi/v1/depth`

Check orderbook depth on specific symbol

查询特定交易对深度

权重: limit         | weight
------------  | ------------
5, 10, 20, 50 | 1
100           | 5
500           | 10
1000          | 20

Operation ID: `orderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| limit | query | integer (int64) |  | Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000]<br>默认值:100 最大值:1000 可选值:[10, 20, 50, 100, 500, 1000]<br>默认: `100`<br>例: `20` |

### 响应 200：Order Book / 订单 Book

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |
| T | integer (int64) |  | transaction time<br>撮合引擎时间<br>例: `1762780909676` |
| lastUpdateId | integer (int64) |  | update id<br>更新id<br>例: `361` |

## Recent Block Trades List（大宗交易历史）

`GET /eapi/v1/blockTrades`

Get recent block trades

查询最近的大宗交易历史

Operation ID: `recentBlockTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Option trading pair<br>交易对如<br>例: `BTC-200730-9000-C` |
| limit | query | integer (int64) |  | Number of records<br>记录数量<br>默认: `100`<br>例: `20` |

### 响应 200：Recent Block Trades List / Recent Block 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | id<br>ID<br>例: `1125899906901081100` |
| [].tradeId | integer (int64) |  | trade Id<br>成交ID<br>例: `389` |
| [].symbol | string |  | symbol<br>交易对<br>例: `ETH-250725-1200-P` |
| [].price | string |  | price<br>价格<br>例: `342.40` |
| [].qty | string |  | qty<br>数量<br>例: `-2167.20` |
| [].quoteQty | string |  | quote Qty<br>报价资产数量<br>例: `-4.90` |
| [].side | integer (int64) |  | side<br>方向<br>例: `-1` |
| [].time | integer (int64) |  | time<br>时间<br>例: `1733950676483` |

## Recent Trades List（近期成交）

`GET /eapi/v1/trades`

Get recent market trades

获取近期订单簿成交

Operation ID: `recentTradesList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| limit | query | integer (int64) |  | Number of result sets returned<br>返回结果集数量<br>默认: `100`<br>例: `20` |

### 响应 200：Recent Trades List / Recent 交易s 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | id<br>ID<br>例: `2323857420768529000` |
| [].tradeId | integer (int64) |  | TradeId<br>成交ID<br>例: `1` |
| [].symbol | string |  | Option trading pair<br>期权交易对<br>例: `BTC-251123-126000-C` |
| [].price | string |  | Completed trade price<br>成交价格<br>例: `1300` |
| [].qty | string |  | Completed trade quantity<br>成交量<br>例: `0.1` |
| [].quoteQty | string |  | Completed trade amount<br>成交额<br>例: `130` |
| [].side | integer (int64) |  | Completed trade direction（-1 Sell，1 Buy）<br>主动成交方方向（-1 Sell，1 Buy）<br>例: `-1` |
| [].time | integer (int64) |  | Time<br>时间<br>例: `1762780453623` |

## Test Connectivity（测试服务器连通性 PING）

`GET /eapi/v1/ping`

Test connectivity to the Rest API.

测试能否联通

Operation ID: `testConnectivity`

### 响应 200：OK / 成功

## 24hr Ticker Price Change Statistics（24hr价格变动情况）

`GET /eapi/v1/ticker`

24 hour rolling window price change statistics.

24小时期权价格变动

权重: 1 for a single symbol; 40 when the symbol parameter is omitted

Operation ID: `ticker24hrPriceChangeStatistics`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Option trading pair<br>交易对如<br>例: `BTC-200730-9000-C` |

### 响应 200：24hr Ticker Price Change Statistics / 24hr 行情 价格 修改Statistics

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | symbol<br>交易对<br>例: `BTC-200730-9000-C` |
| [].priceChange | string |  | 24-hour price change<br>24小时价格变动<br>例: `-16.2038` |
| [].priceChangePercent | string |  | 24-hour percent price change<br>24小时价格变动百分比<br>例: `-0.0162` |
| [].lastPrice | string |  | Last trade price<br>最近一次成交价<br>例: `1000` |
| [].lastQty | string |  | Last trade amount<br>最近一次成交额<br>例: `1000` |
| [].open | string |  | 24-hour open price<br>24小时内第一次成交的价格<br>例: `1016.2038` |
| [].high | string |  | 24-hour high<br>24小时最高价<br>例: `1016.2038` |
| [].low | string |  | 24-hour low<br>24小时最低价<br>例: `0` |
| [].volume | string |  | Trading volume(contracts)<br>成交额<br>例: `5` |
| [].amount | string |  | Trade amount(in quote asset)<br>成交量<br>例: `1` |
| [].bidPrice | string |  | The best buy price<br>最优买价<br>例: `999.34` |
| [].askPrice | string |  | The best sell price<br>最优卖价<br>例: `1000.23` |
| [].openTime | integer (int64) |  | Time the first trade occurred within the last 24 hours<br>24小时内，第一笔交易的发生时间<br>例: `1592317127349` |
| [].closeTime | integer (int64) |  | Time the last trade occurred within the last 24 hours<br>24小时内，最后一笔交易的发生时间<br>例: `1592380593516` |
| [].firstTradeId | integer (int64) |  | First trade ID<br>首笔成交ID<br>例: `1` |
| [].tradeCount | integer (int64) |  | Number of trades<br>成交笔数<br>例: `5` |
| [].strikePrice | string |  | Strike price<br>行权价<br>例: `9000` |
| [].exercisePrice | string |  | return estimated settlement price one hour before exercise, return index price at other times<br>行权前半小时返回预估结算价，其他时刻返回指数价格<br>例: `3000.3356` |

## Query Block Trade Details (USER_DATA)（查询Block 交易 Details (USER_DATA)）

`GET /eapi/v1/block/order/execute`

Query block trade details; returns block trade details from counterparty's perspective.

查询block 交易 details; returns block 交易 details 从 counterparty's perspective.

Operation ID: `queryBlockTradeDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| blockOrderMatchingKey | query | string | 是 | Block trade matching key.<br>大宗交易撮合键。<br>例: `12b96c28-ba05-8906-c89t-703215cfb2e6` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Block Trade Details / Block 交易 Details

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockTradeSettlementKey | string |  | block Trade Settlement Key<br>例: `12b96c28-ba05-8906-c89t-703215cfb2e6` |
| expireTime | integer (int64) |  | expire Time<br>例: `1730171860460` |
| liquidity | string |  | liquidity<br>例: `MAKER` |
| status | string |  | status<br>状态<br>例: `RECEIVED` |
| createTime | integer (int64) |  | create Time<br>例: `1730170060462` |
| legs | object[] |  | legs |
| legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| legs[].side | string |  | side<br>方向<br>例: `SELL` |
| legs[].quantity | string |  | quantity<br>数量<br>例: `1.66` |
| legs[].price | string |  | price<br>价格<br>例: `20` |

## Accept Block Trade Order (TRADE)（Accept Block 交易 订单 (TRADE)）

`POST /eapi/v1/block/order/execute`

Accept a block trade order

Accept a block 交易 订单

Operation ID: `acceptBlockTradeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockOrderMatchingKey | string | 是 | 例: `7d046e6e-a429-4335-ab9d-6a681febcde5` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Accept Block Trade Order / Accept Block 交易 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockTradeSettlementKey | string |  | block Trade Settlement Key<br>例: `7d046e6e-a429-4335-ab9d-6a681febcde5` |
| expireTime | integer (int64) |  | expire Time<br>例: `1730172115801` |
| liquidity | string |  | liquidity<br>例: `MAKER` |
| status | string |  | status<br>状态<br>例: `ACCEPTED` |
| createTime | integer (int64) |  | create Time<br>例: `1730170315803` |
| legs | object[] |  | legs |
| legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| legs[].side | string |  | side<br>方向<br>例: `SELL` |
| legs[].quantity | string |  | quantity<br>数量<br>例: `1.2` |
| legs[].price | string |  | price<br>价格<br>例: `2.8` |

## Account Block Trade List (USER_DATA)（账户 Block 交易 列表 (USER_DATA)）

`GET /eapi/v1/block/user-trades`

Gets block trades for a specific account.

Gets block trades 用于 a specific 账户.

Operation ID: `accountBlockTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| underlying | query | string |  | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Block Trade List / 账户 Block 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].parentOrderId | string |  | parent Order Id<br>例: `4675011431944499201` |
| [].crossType | string |  | cross Type<br>例: `USER_BLOCK` |
| [].legs | object[] |  | legs |
| [].legs[].createTime | integer (int64) |  | create Time<br>例: `1730170445600` |
| [].legs[].updateTime | integer (int64) |  | update Time<br>更新时间<br>例: `1730170445600` |
| [].legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| [].legs[].orderId | string |  | order Id<br>订单ID<br>例: `4675011431944499203` |
| [].legs[].orderPrice | number (float) |  | order Price<br>例: `2.8` |
| [].legs[].orderQuantity | number (float) |  | order Quantity<br>例: `1.2` |
| [].legs[].orderStatus | string |  | order Status<br>例: `FILLED` |
| [].legs[].executedQty | number (float) |  | executed Qty<br>例: `1.2` |
| [].legs[].executedAmount | number (float) |  | executed Amount<br>例: `3.36` |
| [].legs[].fee | number (float) |  | fee<br>例: `0.336` |
| [].legs[].orderType | string |  | order Type<br>例: `PREV_QUOTED` |
| [].legs[].orderSide | string |  | order Side<br>例: `BUY` |
| [].legs[].id | string |  | id<br>ID<br>例: `1125899906900937837` |
| [].legs[].tradeId | integer (int64) |  | trade Id<br>成交ID<br>例: `1` |
| [].legs[].tradePrice | number (float) |  | trade Price<br>例: `2.8` |
| [].legs[].tradeQty | number (float) |  | trade Qty<br>例: `1.2` |
| [].legs[].tradeTime | integer (int64) |  | trade Time<br>例: `1730170445600` |
| [].legs[].liquidity | string |  | liquidity<br>例: `TAKER` |
| [].legs[].commission | number (float) |  | commission<br>例: `0.336` |
| [].blockTradeSettlementKey | string |  | block Trade Settlement Key<br>例: `7d085e6e-a229-2335-ab9d-6a581febcd25` |

## New Block Trade Order (TRADE)（新建大宗交易订单 (TRADE)）

`POST /eapi/v1/block/order/create`

Send in a new block trade order.

提交新的大宗交易订单。

Operation ID: `newBlockTradeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| liquidity | string | 是 | 枚举: `MAKER`, `TAKER`<br>例: `TAKER` |
| legs | object[] | 是 | Max 1 (only single leg supported), list of legs parameters in JSON; example: eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]<br>最多1条（仅支持单腿），JSON格式的legs参数列表；例如：eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}] |
| legs[].symbol | string | 是 | Option trading pair<br>期权交易对<br>例: `BTC-210115-35000-C` |
| legs[].side | string | 是 | Buy/sell direction<br>买卖方向<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| legs[].type | string | 是 | Order type<br>订单类型<br>枚举: `LIMIT`<br>例: `LIMIT` |
| legs[].quantity | string | 是 | Order quantity<br>下单数量<br>例: `0.0002` |
| legs[].price | string |  | Order price<br>订单价格<br>例: `100` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Block Trade Order / 新建大宗交易订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockTradeSettlementKey | string |  | block Trade Settlement Key<br>大宗交易结算键<br>例: `3668822b8-1baa-6a2f-adb8-d3de6289b361` |
| expireTime | integer (int64) |  | expire Time<br>过期时间<br>例: `1730171888109` |
| liquidity | string |  | liquidity<br>流动性方向<br>例: `TAKER` |
| status | string |  | status<br>状态<br>例: `RECEIVED` |
| legs | object[] |  | legs<br>订单腿 |
| legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| legs[].side | string |  | side<br>方向<br>例: `BUY` |
| legs[].quantity | string |  | quantity<br>数量<br>例: `1.2` |
| legs[].price | string |  | price<br>价格<br>例: `2.8` |

## Extend Block Trade Order (TRADE)（Extend Block 交易 订单 (TRADE)）

`PUT /eapi/v1/block/order/create`

Extends a block trade expire time by 30 mins from the current time.

Extends a block 交易 expire 时间 by 30 mins 从 the 当前 时间.

Operation ID: `extendBlockTradeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockOrderMatchingKey | string | 是 | 例: `3668822b8-1baa-6a2f-adb8-d3de6289b361` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Extend Block Trade Order / Extend Block 交易 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| blockTradeSettlementKey | string |  | block Trade Settlement Key<br>例: `3668822b8-1baa-6a2f-adb8-d3de6289b361` |
| expireTime | integer (int64) |  | expire Time<br>例: `1730172007000` |
| liquidity | string |  | liquidity<br>例: `TAKER` |
| status | string |  | status<br>状态<br>例: `RECEIVED` |
| createTime | integer (int64) |  | create Time<br>例: `1730170088111` |
| legs | object[] |  | legs |
| legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| legs[].side | string |  | side<br>方向<br>例: `BUY` |
| legs[].quantity | string |  | quantity<br>数量<br>例: `1.2` |
| legs[].price | string |  | price<br>价格<br>例: `2.8` |

## Cancel Block Trade Order (TRADE)（取消Block 交易 订单 (TRADE)）

`DELETE /eapi/v1/block/order/create`

Cancel a block trade order.

取消a block 交易 订单.

Operation ID: `cancelBlockTradeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| blockOrderMatchingKey | query | string | 是 | Block trade matching key.<br>大宗交易撮合键。<br>例: `7d046e6e-a429-4335-ab9d-6a681febcde5` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Query Block Trade Order (TRADE)（查询Block 交易 订单 (TRADE)）

`GET /eapi/v1/block/order/orders`

Check block trade order status.

检查block 交易 订单 状态.

Operation ID: `queryBlockTradeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| blockOrderMatchingKey | query | string |  | If specified, returns the specific block trade associated with the blockOrderMatchingKey<br>If specified, returns the specific block 交易 associated 带 the block订单Matching Key<br>例: `7d046e6e-a429-4335-ab9d-6a681febcde5` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| underlying | query | string |  | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Block Trade Order / Block 交易 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].blockTradeSettlementKey | string |  | block Trade Settlement Key<br>例: `7d046e6e-a429-4335-ab9d-6a681febcde5` |
| [].expireTime | integer (int64) |  | expire Time<br>例: `1730172115801` |
| [].liquidity | string |  | liquidity<br>例: `TAKER` |
| [].status | string |  | status<br>状态<br>例: `RECEIVED` |
| [].createTime | integer (int64) |  | create Time<br>例: `1730170315803` |
| [].legs | object[] |  | legs |
| [].legs[].symbol | string |  | symbol<br>交易对<br>例: `BNB-241101-700-C` |
| [].legs[].side | string |  | side<br>方向<br>例: `BUY` |
| [].legs[].quantity | string |  | quantity<br>数量<br>例: `1.2` |
| [].legs[].price | string |  | price<br>价格<br>例: `2.8` |

## Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)（重置倒计时取消所有订单心跳 (TRADE)）

`POST /eapi/v1/countdownCancelAllHeartBeat`

This endpoint resets the time from which the countdown will begin to the time this messaged is received.  It should be called repeatedly as heartbeats.  Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

本接口用户更新倒计时取消所有订单心跳。本接口需要作为心跳更新被频繁调用。将多个标的资产以list形式传入`underlyings`可以同时更新多个标的资产的心跳。

Operation ID: `autoCancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyings | string | 是 | 例: `BTCUSDT,ETHUSDT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Auto-Cancel All Open Orders / Auto-取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyings | string[] |  | underlyings |

## Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)（获得倒计时自动取消所有订单配置 (TRADE)）

`GET /eapi/v1/countdownCancelAll`

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

本接口用于获得倒计时自动取消所有订单配置。接口仅返回有效的自动取消参数，如果标的资产的`countdownTime`设置为0，该标的资产对应的参数不会被返回。

Operation ID: `getAutoCancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlying | query | string |  | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Auto-Cancel All Open Orders / 获取Auto-取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlying | string |  | underlying<br>标的资产<br>例: `ETHUSDT` |
| countdownTime | integer (int64) |  | countdown Time<br>例: `100000` |

## Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)（设置倒计时取消所有订单配置 (TRADE)）

`POST /eapi/v1/countdownCancelAll`

This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker protection and non market maker protection order types) of the underlying symbol at the end of the specified countdown time period if no heartbeat message is sent.  After the countdown time period, all open orders will be cancelled. The auto-cancel feature can be turned off by setting countdownTime to 0.

此接口用于设置倒计时取消所有订单（包括做市商保护订单与普通订单）配置，即在倒计时结束前心跳没有更新，特定标的资产的所有订单会被取消。若倒计时结束前心跳没有更新，所有的订单将会被取消。可以通过设置`countdownTime`为0取消此功能。

Operation ID: `setAutoCancelAllOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlying | string | 是 | 例: `BTCUSDT` |
| countdownTime | integer (int64) | 是 | Countdown time in milliseconds (ex. 1,000 for 1 second). 0 to disable the timer. Negative values (ex. -10000) are not accepted. Minimum acceptable value is 5,000<br>以毫秒计量倒计时长 (1000代表1秒)。 设为0时关闭倒计时。最小设为5000（负值无效）<br>例: `5000` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Auto-Cancel All Open Orders / Set Auto-取消All 未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlying | string |  | underlying<br>标的资产<br>例: `ETHUSDT` |
| countdownTime | integer (int64) |  | countdown Time<br>例: `100000` |

## Get Market Maker Protection Config (TRADE)（获取MMP规则 (TRADE)）

`GET /eapi/v1/mmp`

Get config for MMP.

获取MMP参数

Operation ID: `getMarketMakerProtectionConfig`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlying | query | string | 是 | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Market Maker Protection Config / 获取MMP规则

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyingId | integer (int64) |  | underlying Id<br>标的资产ID<br>例: `2` |
| underlying | string |  | underlying<br>标的资产<br>例: `BTCUSDT` |
| windowTimeInMilliseconds | integer (int64) |  | window Time In Milliseconds<br>监控时间窗口（毫秒）<br>例: `3000` |
| frozenTimeInMilliseconds | integer (int64) |  | frozen Time In Milliseconds<br>冻结时间（毫秒）<br>例: `300000` |
| qtyLimit | string |  | qty Limit<br>数量限制<br>例: `2` |
| deltaLimit | string |  | delta Limit<br>净Delta限制<br>例: `2.3` |
| lastTriggerTime | integer (int64) |  | last Trigger Time<br>最近触发时间<br>例: `0` |

## Reset Market Maker Protection Config (TRADE)（重置MMP状态 (TRADE)）

`POST /eapi/v1/mmpReset`

Reset MMP, start MMP order again.

MMP冻结后重置MMP，重新开启MMP下单

Operation ID: `resetMarketMakerProtectionConfig`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlying | string | 是 | 例: `BTCUSDT` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Reset Market Maker Protection Config / 重置MMP状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyingId | integer (int64) |  | underlying Id<br>标的资产ID<br>例: `2` |
| underlying | string |  | underlying<br>标的资产<br>例: `BTCUSDT` |
| windowTimeInMilliseconds | integer (int64) |  | window Time In Milliseconds<br>监控时间窗口（毫秒）<br>例: `3000` |
| frozenTimeInMilliseconds | integer (int64) |  | frozen Time In Milliseconds<br>冻结时间（毫秒）<br>例: `300000` |
| qtyLimit | string |  | qty Limit<br>数量限制<br>例: `2` |
| deltaLimit | string |  | delta Limit<br>净Delta限制<br>例: `2.3` |
| lastTriggerTime | integer (int64) |  | last Trigger Time<br>最近触发时间<br>例: `0` |

## Set Market Maker Protection Config (TRADE)（设置MMP规则 (TRADE)）

`POST /eapi/v1/mmpSet`

Set config for MMP. Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

设置MMP参数。 做市商保护(Market Maker Protection) 是一种为期权做市商设计的保护机制，该机制能够防止做市商的订单在短时间大量成交。一旦某个账户在短时间内的总交易额超过了配置的限额，该账户的做市商保护将被触发。当做市商保护被触发时，账户现有的做市商保护订单（被标记为做市商保护的订单）将被撮合自动取消，而该账户新的做市商保护订单将在冻结期被拒绝。用户可以利用这段时间重新评估行情并修改报价。

Operation ID: `setMarketMakerProtectionConfig`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlying | string | 是 | 例: `BTCUSDT` |
| windowTimeInMilliseconds | integer (int64) | 是 | MMP Interval in milliseconds<br>MMP监控时间窗口（毫秒）<br>例: `1000` |
| frozenTimeInMilliseconds | integer (int64) | 是 | MMP frozen time in milliseconds, if set to 0 manual reset is required<br>MMP冻结时间（毫秒），设置为0后代表账号为冻结状态，需要手动重置<br>例: `1000` |
| qtyLimit | number (float) | 是 | quantity limit<br>数量限制<br>例: `1.0` |
| deltaLimit | number (float) | 是 | net delta limit<br>净delta限制<br>例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Market Maker Protection Config / 设置MMP规则

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyingId | integer (int64) |  | underlying Id<br>标的资产ID<br>例: `2` |
| underlying | string |  | underlying<br>标的资产<br>例: `BTCUSDT` |
| windowTimeInMilliseconds | integer (int64) |  | window Time In Milliseconds<br>监控时间窗口（毫秒）<br>例: `3000` |
| frozenTimeInMilliseconds | integer (int64) |  | frozen Time In Milliseconds<br>冻结时间（毫秒）<br>例: `300000` |
| qtyLimit | string |  | qty Limit<br>数量限制<br>例: `2` |
| deltaLimit | string |  | delta Limit<br>净Delta限制<br>例: `2.3` |
| lastTriggerTime | integer (int64) |  | last Trigger Time<br>最近触发时间<br>例: `0` |

## Account Trade List (USER_DATA)（账户成交历史 (USER_DATA)）

`GET /eapi/v1/userTrades`

Get trades for a specific account and symbol. Only supports querying trades in the past 3 months; a `startTime`/`endTime` outside that window returns `-6073 SEARCH_WINDOW_RESTRICTED`.

查询账户成交历史。仅支持查询最近3个月的成交记录，`startTime`/`endTime` 超出该范围将返回 `-6073 SEARCH_WINDOW_RESTRICTED`。

Operation ID: `accountTradeList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| fromId | query | integer (int64) |  | Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376<br>返回该fromId及之后的成交，缺省返回最近的成交<br>例: `1` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned.<br>返回结果数量。<br>默认: `100`<br>例: `20` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Account Trade List / 账户 交易 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | integer (int64) |  | unique id<br>ID<br>例: `4611875134427365000` |
| [].tradeId | integer (int64) |  | trade id<br>交易id<br>例: `239` |
| [].orderId | integer (int64) |  | order id<br>订单id<br>例: `4611875134427365000` |
| [].symbol | string |  | option symbol<br>交易对<br>例: `BTC-200730-9000-C` |
| [].price | string |  | trade price<br>成交价<br>例: `100` |
| [].quantity | string |  | trade quantity<br>成交量<br>例: `1` |
| [].fee | string |  | fee(negative is fee deduction)<br>手续费（负数为扣费）<br>例: `-1.04378629` |
| [].realizedProfit | string |  | realized profit/loss<br>已实现盈亏<br>例: `0.00000000` |
| [].side | string |  | order side<br>订单方向<br>例: `BUY` |
| [].type | string |  | order type<br>订单类型<br>例: `LIMIT` |
| [].liquidity | string |  | TAKER or MAKER<br>例: `TAKER` |
| [].time | integer (int64) |  | trade time<br>交易时间<br>例: `1592465880683` |
| [].priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| [].optionSide | string |  | option Side<br>期权种类<br>例: `CALL` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |

## Cancel All Option Orders By Underlying (TRADE)（撤销特定标的全部订单 (TRADE)）

`DELETE /eapi/v1/allOpenOrdersByUnderlying`

Cancel all active orders on specified underlying.

撤销特定标的全部订单

Operation ID: `cancelAllOptionOrdersByUnderlying`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlying | query | string | 是 | Underlying asset.<br>标的资产。<br>例: `BTCUSDT` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel All Option Orders By Underlying / 取消All Option 订单 By Underlying

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | code<br>例: `0` |
| msg | string |  | msg<br>例: `success` |

## Cancel all Option orders on specific symbol (TRADE)（撤销单交易对全部订单 (TRADE)）

`DELETE /eapi/v1/allOpenOrders`

Cancel all active order on a symbol.

撤销单交易对全部订单

Operation ID: `cancelAllOptionOrdersOnSpecificSymbol`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel all Option orders on specific symbol / 取消all Option 订单 on specific 交易对

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | code<br>例: `0` |
| msg | string |  | msg<br>例: `success` |

## Place Multiple Orders (TRADE)（批量下单 (TRADE)）

`POST /eapi/v1/batchOrders`

Send multiple option orders.

批量下单。

Operation ID: `placeMultipleOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orders | object[] | 是 | order list. Max 10 orders<br>订单列表，最多支持10个订单 |
| orders[].symbol | string | 是 | 例: `BTC-200730-9000-C` |
| orders[].side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| orders[].type | string | 是 | 枚举: `LIMIT`<br>例: `LIMIT` |
| orders[].quantity | number (float) | 是 | Order Quantity<br>下单数量<br>例: `1.0` |
| orders[].price | number (float) |  | Order Price<br>订单价格<br>例: `1.0` |
| orders[].timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>默认: `GTC`<br>例: `GTC` |
| orders[].reduceOnly | boolean |  | 默认: `False`<br>例: `False` |
| orders[].postOnly | boolean |  | 默认: `False`<br>例: `False` |
| orders[].newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| orders[].clientOrderId | string |  | User-defined order ID cannot be repeated in pending orders<br>用户自定义订单 ID，不可与挂单中的其他订单重复<br>例: `1` |
| orders[].isMmp | boolean |  | is market maker protection order<br>是否为做市商保护订单<br>例: `True` |
| orders[].selfTradePreventionMode | string |  | EXPIRE_TAKER: expire taker order when STP triggers/ EXPIRE_MAKER: expire maker order when STP triggers/ EXPIRE_BOTH: expire both orders when STP triggers; Default EXPIRE_MAKER<br>EXPIRE_TAKER: STP触发时，取消吃单订单/ EXPIRE_MAKER: STP触发时，取消挂单订单/ EXPIRE_BOTH: STP触发时，取消吃单和挂单订单; 默认 EXPIRE_MAKER<br>枚举: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`<br>默认: `EXPIRE_MAKER`<br>例: `NONE` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Place Multiple Orders / 批量下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | System order number<br>订单Id<br>例: `4611875134427365000` |
| [].symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| [].price | string |  | Order Price<br>订单价格<br>例: `100` |
| [].quantity | string |  | Order Quantity<br>订单数量<br>例: `1` |
| [].executedQty | string |  | Number of executed quantity<br>执行数量<br>例: `0` |
| [].fee | integer (int64) |  | fee<br>手续费<br>例: `0` |
| [].side | string |  | Buy/sell direction<br>订单方向<br>例: `BUY` |
| [].type | string |  | Order type<br>订单类型<br>例: `LIMIT` |
| [].timeInForce | string |  | Time in force method<br>有效时间<br>例: `GTC` |
| [].reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| [].postOnly | boolean |  | post Only<br>仅做maker<br>例: `False` |
| [].createTime | integer (int64) |  | Order Time<br>订单创建时间<br>例: `1592465880683` |
| [].updateTime | integer (int64) |  | Update time<br>订单更新时间<br>例: `1566818724722` |
| [].status | string |  | Order status<br>订单状态<br>例: `NEW` |
| [].avgPrice | string |  | Average price of completed trade<br>平均价格<br>例: `0` |
| [].clientOrderId | string |  | Client order ID<br>用户自定义订单Id<br>例: `` |
| [].priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| [].optionSide | string |  | option Side<br>期权类型<br>例: `CALL` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| [].mmp | boolean |  | mmp<br>是否为MMP单<br>例: `False` |
| [].selfTradePreventionMode | string |  | self trading prevention mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |
| [].source | string |  | 例: `API` |

## Cancel Multiple Option Orders (TRADE)（批量撤销订单 (TRADE)）

`DELETE /eapi/v1/batchOrders`

Cancel multiple orders.

批量撤销订单。

Operation ID: `cancelMultipleOptionOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| orderIds | query | integer (int64)[] |  | Order ID list.<br>订单 ID 列表。 |
| clientOrderIds | query | string[] |  | Client order ID list.<br>客户端订单 ID 列表。 |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Multiple Option Orders / 取消Multiple Option 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | System order number<br>订单Id<br>例: `4611875134427365000` |
| [].symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| [].price | string |  | Order Price<br>订单价格<br>例: `100` |
| [].quantity | string |  | Order Quantity<br>订单数量<br>例: `1` |
| [].executedQty | string |  | Number of completed quantity<br>已经成交数量<br>例: `0` |
| [].fee | string |  | fee<br>手续费<br>例: `0` |
| [].side | string |  | Buy/sell direction<br>订单方向<br>例: `BUY` |
| [].type | string |  | Order type<br>订单类型<br>例: `LIMIT` |
| [].timeInForce | string |  | Time in force method<br>有效时间<br>例: `GTC` |
| [].reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| [].createTime | integer (int64) |  | Order Time<br>订单创建时间<br>例: `1592465880683` |
| [].updateTime | integer (int64) |  | Update time<br>订单更新时间<br>例: `1566818724722` |
| [].status | string |  | Order status<br>订单类型<br>例: `ACCEPTED` |
| [].avgPrice | string |  | Average price of completed trade<br>平均成交价<br>例: `0` |
| [].clientOrderId | string |  | Client order ID<br>用户自定义的订单号<br>例: `` |
| [].priceScale | integer (int64) |  | price Scale<br>例: `3` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>例: `4` |
| [].optionSide | string |  | option Side<br>例: `CALL` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| [].mmp | boolean |  | mmp<br>例: `False` |
| [].source | string |  | 例: `API` |
| [].selfTradePreventionMode | string |  | self trading prevention mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Query Single Order (TRADE)（查询单个订单 (TRADE)）

`GET /eapi/v1/order`

Check an order status.

* These orders will not be found:
  * order status is `CANCELED` or `REJECTED`, **AND**
  * order has NO filled trade, **AND**
  * created time + 3 days < current time

查询订单状态。

* 以下订单无法找到:
  * 订单状态为 `CANCELED` or `REJECTED`， **AND**
  * 订单没有成交记录， **AND**
  * 订单生成时间 + 3天 < 当前时间

Operation ID: `querySingleOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| orderId | query | integer (int64) |  | Order ID.<br>订单 ID。<br>例: `4611875134427365000` |
| clientOrderId | query | string |  | User-defined order ID; cannot be duplicated among open orders.<br>用户自定义订单 ID；在挂单中不可重复。<br>例: `abc123` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Single Order / 单个订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | System order id<br>订单号<br>例: `4611875134427365000` |
| symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| price | string |  | Order Price<br>订单价格<br>例: `100` |
| quantity | string |  | Order Quantity<br>订单数量<br>例: `1` |
| executedQty | string |  | Number of executed quantity<br>执行数量<br>例: `0` |
| side | string |  | Buy/sell direction<br>订单方向<br>例: `BUY` |
| type | string |  | Order type<br>订单类型<br>例: `LIMIT` |
| timeInForce | string |  | Time in force method<br>有效时间<br>例: `GTC` |
| reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| postOnly | boolean |  | post Only<br>仅做maker<br>例: `False` |
| createTime | integer (int64) |  | Order Time<br>下单时间<br>例: `1592465880683` |
| updateTime | integer (int64) |  | Update time<br>更新时间<br>例: `1566818724722` |
| status | string |  | Order status<br>订单状态<br>例: `NEW` |
| avgPrice | string |  | Average price of completed trade<br>成交均价<br>例: `0` |
| clientOrderId | string |  | Client order ID<br>自定义id<br>例: `` |
| priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| optionSide | string |  | option Side<br>期权类型<br>例: `CALL` |
| quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| mmp | boolean |  | mmp<br>例: `False` |
| selfTradePreventionMode | string |  | Self trade prevention mode.<br>订单自成交保护模式。<br>例: `EXPIRE_MAKER` |

## New Order (TRADE)（下单 (TRADE)）

`POST /eapi/v1/order`

Send a new order.

下单

Operation ID: `newOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 例: `BTC-200730-9000-C` |
| side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| type | string | 是 | 枚举: `LIMIT`<br>例: `LIMIT` |
| quantity | number (float) | 是 | Order Quantity<br>下单数量<br>例: `1.0` |
| price | number (float) |  | Order Price<br>订单价格<br>例: `1.0` |
| timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>默认: `GTC`<br>例: `GTC` |
| reduceOnly | boolean |  | 默认: `False`<br>例: `False` |
| postOnly | boolean |  | 默认: `False`<br>例: `False` |
| newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| clientOrderId | string |  | User-defined order ID cannot be repeated in pending orders<br>用户自定义订单 ID，不可与挂单中的其他订单重复<br>例: `1` |
| isMmp | boolean |  | is market maker protection order<br>是否为做市商保护订单<br>例: `True` |
| selfTradePreventionMode | string |  | Self-trade prevention mode<br>自我交易预防模式<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`<br>例: `NONE` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：New Order / 新订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | System order number<br>订单Id<br>例: `4611875134427365000` |
| symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| price | string |  | Order Price<br>订单价格<br>例: `100` |
| quantity | string |  | Order Quantity<br>订单数量<br>例: `1` |
| executedQty | string |  | Number of executed quantity<br>执行数量<br>例: `0` |
| fee | integer (int64) |  | fee<br>手续费<br>例: `0` |
| side | string |  | Buy/sell direction<br>订单方向<br>例: `BUY` |
| type | string |  | Order type<br>订单类型<br>例: `LIMIT` |
| timeInForce | string |  | Time in force method<br>有效时间<br>例: `GTC` |
| reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| postOnly | boolean |  | post Only<br>仅做maker<br>例: `False` |
| createTime | integer (int64) |  | Order Time<br>订单创建时间<br>例: `1592465880683` |
| updateTime | integer (int64) |  | Update time<br>订单更新时间<br>例: `1566818724722` |
| status | string |  | Order status<br>订单状态<br>例: `NEW` |
| avgPrice | string |  | Average price of completed trade<br>平均价格<br>例: `0` |
| source | string |  | source<br>订单来源<br>例: `API` |
| clientOrderId | string |  | Client order ID<br>用户自定义订单Id<br>例: `` |
| priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| optionSide | string |  | option Side<br>期权类型<br>例: `CALL` |
| quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| mmp | boolean |  | mmp<br>是否为MMP单<br>例: `False` |
| selfTradePreventionMode | string |  | Self-trade prevention mode<br>自我交易预防模式<br>例: `EXPIRE_MAKER` |

## Cancel Option Order (TRADE)（撤销订单 (TRADE)）

`DELETE /eapi/v1/order`

Cancel an active order.

撤销订单。

Operation ID: `cancelOptionOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| orderId | query | integer (int64) |  | Order ID.<br>订单 ID。<br>例: `4611875134427365000` |
| clientOrderId | query | string |  | clientOrderId<br>例: `10000` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Option Order / 取消Option 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) |  | System order number<br>订单ID<br>例: `4611875134427365000` |
| symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| price | string |  | Order Price<br>价格<br>例: `100` |
| quantity | string |  | Order Quantity<br>数量<br>例: `1` |
| executedQty | string |  | Number of executed quantity<br>例: `0` |
| side | string |  | Buy/sell direction<br>方向<br>例: `BUY` |
| type | string |  | Order type<br>类型<br>例: `LIMIT` |
| timeInForce | string |  | Time in force method<br>例: `GTC` |
| reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| createDate | integer (int64) |  | Order Time<br>创建时间<br>例: `1592465880683` |
| updateTime | integer (int64) |  | Update time<br>更新时间<br>例: `1566818724722` |
| status | string |  | Order status<br>状态<br>例: `ACCEPTED` |
| avgPrice | string |  | Average price of completed trade<br>例: `0` |
| source | string |  | source<br>例: `API` |
| clientOrderId | string |  | Client order ID<br>客户端订单ID<br>例: `` |
| priceScale | integer (int64) |  | price Scale<br>例: `4` |
| quantityScale | integer (int64) |  | quantity Scale<br>例: `4` |
| optionSide | string |  | option Side<br>例: `CALL` |
| quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| mmp | boolean |  | mmp<br>例: `False` |
| selfTradePreventionMode | string |  | self trading prevention mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Option Position Information (USER_DATA)（仓位信息 (USER_DATA)）

`GET /eapi/v1/position`

Get current position information.

获取仓位信息

Operation ID: `optionPositionInformation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Option Position Information / Option 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].entryPrice | string |  | Average entry price<br>例: `1000` |
| [].symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| [].side | string |  | Position direction<br>方向<br>例: `SHORT` |
| [].quantity | string |  | Number of positions (positive numbers represent long positions, negative number represent short positions)<br>数量<br>例: `-0.1` |
| [].markValue | string |  | Current market value<br>例: `105.00138` |
| [].unrealizedPNL | string |  | Unrealized profit/loss<br>未实现盈亏<br>例: `-5.00138` |
| [].markPrice | string |  | Mark price<br>标记价格<br>例: `1050.0138` |
| [].strikePrice | string |  | Strike price<br>行权价<br>例: `9000` |
| [].expiryDate | integer (int64) |  | Exercise time<br>到期时间<br>例: `1593511200000` |
| [].priceScale | integer (int64) |  | price Scale<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>例: `2` |
| [].optionSide | string |  | option type<br>例: `CALL` |
| [].quoteAsset | string |  | quote asset<br>报价资产<br>例: `USDT` |
| [].time | integer (int64) |  | last update time<br>时间<br>例: `1762872654561` |
| [].bidQuantity | string |  | buy order qty<br>例: `0.0000` |
| [].askQuantity | string |  | sell order qty<br>例: `0.0000` |

## Query Current Open Option Orders (USER_DATA)（查询当前挂单 (USER_DATA)）

`GET /eapi/v1/openOrders`

Query current all open orders, status: ACCEPTED PARTIALLY_FILLED

查询当前挂单（包含状态为ACCEPTED/ PARTIALLY_FILLED的订单）

权重: 1 for a single symbol; 40 when the symbol parameter is omitted

Operation ID: `queryCurrentOpenOptionOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| orderId | query | integer (int64) |  | Order ID.<br>订单 ID。<br>例: `4611875134427365000` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Open Option Orders / 当前 未完成Option 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | System order number<br>订单Id<br>例: `4611875134427365000` |
| [].symbol | string |  | Option trading pair<br>交易对<br>例: `BTC-200730-9000-C` |
| [].price | string |  | Order Price<br>订单价格<br>例: `100` |
| [].quantity | string |  | Order Quantity<br>订单数量<br>例: `1` |
| [].executedQty | string |  | Number of completed trades<br>已经成交的交易量<br>例: `0` |
| [].side | string |  | Buy/sell direction<br>订单方向<br>例: `BUY` |
| [].type | string |  | Order type<br>订单类型<br>例: `LIMIT` |
| [].timeInForce | string |  | Time in force method<br>有效时间<br>例: `GTC` |
| [].reduceOnly | boolean |  | Order is reduce only Y/N<br>仅减仓<br>例: `False` |
| [].createTime | integer (int64) |  | Order Time<br>订单创建时间<br>例: `1592465880683` |
| [].updateTime | integer (int64) |  | Update Time<br>订单更新时间<br>例: `1592465880683` |
| [].status | string |  | Order status<br>订单状态<br>例: `NEW` |
| [].avgPrice | string |  | Average price of completed trade<br>已成交平均价<br>例: `0` |
| [].clientOrderId | string |  | Client order ID<br>用户自定义订单id<br>例: `` |
| [].priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| [].optionSide | string |  | option Side<br>期权类型<br>例: `CALL` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| [].mmp | boolean |  | mmp<br>是否为MMP订单<br>例: `False` |
| [].selfTradePreventionMode | string |  | self trading prevention mode<br>订单自成交保护模式<br>例: `EXPIRE_MAKER` |

## Query Option Order History (TRADE)（查询历史订单 (TRADE)）

`GET /eapi/v1/historyOrders`

Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED.

查询5天内的历史订单，订单的最终状态为 `CANCELED` 或者 `FILLED` 或者 `REJECTED`

Operation ID: `queryOptionOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| orderId | query | integer (int64) |  | Order ID.<br>订单 ID。<br>例: `4611875134427365000` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned<br>返回结果数量。<br>默认: `100`<br>例: `20` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Option Order History / Option 订单 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | integer (int64) |  | order Id<br>订单Id<br>例: `4611875134427365000` |
| [].symbol | string |  | symbol<br>交易对<br>例: `BTC-200730-9000-C` |
| [].price | string |  | price<br>订单价格<br>例: `100` |
| [].quantity | string |  | quantity<br>订单数量<br>例: `1` |
| [].executedQty | string |  | executed Qty<br>已经成交的交易量<br>例: `0` |
| [].side | string |  | side<br>订单方向<br>例: `BUY` |
| [].type | string |  | type<br>订单类型<br>例: `LIMIT` |
| [].timeInForce | string |  | time In Force<br>有效时间<br>例: `GTC` |
| [].reduceOnly | boolean |  | reduce Only<br>仅减仓<br>例: `False` |
| [].createTime | integer (int64) |  | create Time<br>订单创建时间<br>例: `1592465880683` |
| [].updateTime | integer (int64) |  | update Time<br>订单更新时间<br>例: `1592465880683` |
| [].status | string |  | status<br>订单状态<br>例: `ACCEPTED` |
| [].avgPrice | string |  | avg Price<br>已成交平均价<br>例: `0` |
| [].clientOrderId | string |  | client Order Id<br>用户自定义订单id<br>例: `` |
| [].priceScale | integer (int64) |  | price Scale<br>价格精度<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>数量精度<br>例: `2` |
| [].optionSide | string |  | option Side<br>期权类型<br>例: `CALL` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |
| [].mmp | boolean |  | mmp<br>是否为MMP订单<br>例: `False` |

## TradFi Options Contract (USER_DATA)（传统金融期权协议 (USER_DATA)）

`POST /eapi/v1/stock/contract`

Sign TradFi Options agreement contract

签署传统金融期权协议

Operation ID: `tradfiOptionsContract`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：TradFi Options Contract / 传统金融期权协议

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | integer (int64) |  | 例: `200` |
| msg | string |  | 例: `success` |

## User Commission (USER_DATA)（用户手续费率 (USER_DATA)）

`GET /eapi/v1/commission`

Get account commission.

获取用户手续费率.

Operation ID: `userCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Commission / 用户 手续费

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| commissions | object[] |  | commissions |
| commissions[].underlying | string |  | underlying<br>标的资产<br>例: `BTCUSDT` |
| commissions[].makerFee | string |  | maker Fee<br>例: `0.000240` |
| commissions[].takerFee | string |  | taker Fee<br>例: `0.000240` |

## User Exercise Record (USER_DATA)（用户行权历史 (USER_DATA)）

`GET /eapi/v1/exerciseRecord`

Get account exercise records.

获取用户行权历史.

Operation ID: `userExerciseRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Option trading pair.<br>期权交易对。<br>例: `BTC-200730-9000-C` |
| startTime | query | integer (int64) |  | Start Time, e.g 1593511200000<br>起始时间如1593511200000<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End Time, e.g 1593512200000<br>结束时间如1593512200000<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of result sets returned.<br>返回结果数量。<br>默认: `1000`<br>例: `20` |
| recvWindow | query | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：User Exercise Record / 用户 Exercise Record

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].id | string |  | id<br>ID<br>例: `1125899906842624042` |
| [].currency | string |  | currency<br>例: `USDT` |
| [].symbol | string |  | symbol<br>交易对<br>例: `BTC-220721-25000-C` |
| [].exercisePrice | string |  | exercise Price<br>例: `25000.00000000` |
| [].quantity | string |  | quantity<br>数量<br>例: `1.00000000` |
| [].amount | string |  | amount<br>金额<br>例: `0.00000000` |
| [].fee | string |  | fee<br>例: `0.00000000` |
| [].createDate | integer (int64) |  | create Date<br>创建时间<br>例: `1658361600000` |
| [].priceScale | integer (int64) |  | price Scale<br>例: `2` |
| [].quantityScale | integer (int64) |  | quantity Scale<br>例: `2` |
| [].optionSide | string |  | option Side<br>例: `CALL` |
| [].positionSide | string |  | position Side<br>例: `LONG` |
| [].quoteAsset | string |  | quote Asset<br>报价资产<br>例: `USDT` |

## Start User Data Stream (USER_STREAM)（生成listenKey (USER_STREAM)）

`POST /eapi/v1/listenKey`

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
| listenKey | string |  | listen Key<br>例: `pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1` |
| expiration | integer (int64) |  | Listen key expiration timestamp in milliseconds<br>listenKey 过期时间戳（毫秒）<br>例: `1762855900452` |

## Keepalive User Data Stream (USER_STREAM)（延长listenKey有效期 (USER_STREAM)）

`PUT /eapi/v1/listenKey`

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

`DELETE /eapi/v1/listenKey`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：OK / 成功