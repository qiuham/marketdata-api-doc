---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api
api_type: REST
updated_at: 2026-11-26 18:49:56.433516
---

# Algo Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/1.0.0/schema.yaml

Programmatic access to Binance’s execution algorithms for creating and managing Spot and Futures algo orders.

用于以编程方式访问 Binance 执行算法，以创建和管理现货及期货算法订单.

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `DELETE /sapi/v1/algo/futures/order` — Cancel Futures Algo Order (TRADE)
- `GET /sapi/v1/algo/futures/openOrders` — Query Current Futures Algo Open Orders (USER_DATA)
- `GET /sapi/v1/algo/futures/historicalOrders` — Query Historical Futures Algo Orders (USER_DATA)
- `GET /sapi/v1/algo/futures/subOrders` — Query Futures Sub Orders (USER_DATA)
- `POST /sapi/v1/algo/futures/newOrderTwap` — Time-Weighted Futures Average Price (Twap) New Order (TRADE)
- `POST /sapi/v1/algo/futures/newOrderVp` — Volume Participation (VP) New Order (TRADE)
- `DELETE /sapi/v1/algo/spot/order` — Cancel Spot Algo Order (TRADE)
- `GET /sapi/v1/algo/spot/openOrders` — Query Current Spot Algo Open Orders (USER_DATA)
- `GET /sapi/v1/algo/spot/historicalOrders` — Query Historical Spot Algo Orders (USER_DATA)
- `GET /sapi/v1/algo/spot/subOrders` — Query Spot Sub Orders (USER_DATA)
- `POST /sapi/v1/algo/spot/newOrderTwap` — Time-Weighted Spot Average Price(Twap) New Order (TRADE)
- `POST /sapi/v1/algo/spot/newOrderVp` — Volume Participation (VP) New Order (TRADE)

## Cancel Futures Algo Order (TRADE)（取消策略订单 (TRADE)）

`DELETE /sapi/v1/algo/futures/order`

Cancel an active order.

撤销订单

Operation ID: `cancelAlgoOrderFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | eg. 14511<br>请参见英文说明：eg. 14511<br>例: `1` |
| clientAlgoId | query | string |  | eg. "65ce1630101a480b85915d7e11fd5078"<br>请参见英文说明：eg. "65ce1630101a480b85915d7e11fd5078"<br>例: `65ce1630101a480b85915d7e11fd5078` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Algo Order / 取消策略订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `14511` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |

## Query Current Futures Algo Open Orders (USER_DATA)（查询当前策略订单挂单 (USER_DATA)）

`GET /sapi/v1/algo/futures/openOrders`

Query Current Algo Open Orders

查询当前策略订单挂单

Operation ID: `queryCurrentAlgoOpenOrdersFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Algo Open Orders / 当前策略未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| orders | object[] |  |  |
| orders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `14517` |
| orders[].symbol | string |  | Trading symbol<br>交易对<br>例: `ETHUSDT` |
| orders[].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| orders[].positionSide | string |  | Position side<br>持仓方向<br>例: `SHORT` |
| orders[].totalQty | string |  | Total order quantity<br>总下单数量<br>例: `5.000` |
| orders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0.000` |
| orders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `0.00000000` |
| orders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.00` |
| orders[].clientAlgoId | string |  | Client-defined algo order ID<br>用户自定义策略订单 ID<br>例: `d7096549481642f8a0bb69e9e2e31f2e` |
| orders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649756817004` |
| orders[].endTime | integer (int64) |  | End time<br>结束时间<br>例: `0` |
| orders[].algoStatus | string |  | Algo order status<br>策略订单状态<br>例: `WORKING` |
| orders[].algoType | string |  | Algo order type<br>策略订单类型<br>例: `VP` |
| orders[].urgency | string |  | Execution urgency<br>执行速率<br>例: `LOW` |

## Query Historical Futures Algo Orders (USER_DATA)（查询历史策略订单 (USER_DATA)）

`GET /sapi/v1/algo/futures/historicalOrders`

Query Historical Algo Order

查询历史策略订单

Operation ID: `queryHistoricalAlgoOrdersFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Trading symbol eg. BTCUSDT<br>交易对 eg. BTCUSDT<br>例: `BTCUSDT` |
| side | query | string |  | BUY or SELL<br>BUY 或者 SELL<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| startTime | query | integer (int64) |  | in milliseconds  eg.1641522717552<br>毫秒级时间戳  eg.1641522717552<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | in milliseconds  eg.1641522526562<br>毫秒级时间戳  eg.1641522526562<br>例: `1641782889000` |
| page | query | integer (int64) |  | Page number<br>页码<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Records per page<br>每页记录数<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Historical Algo Orders / 历史策略订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| orders | object[] |  |  |
| orders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `14518` |
| orders[].symbol | string |  | Trading symbol<br>交易对<br>例: `BNBUSDT` |
| orders[].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| orders[].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| orders[].totalQty | string |  | Total order quantity<br>总下单数量<br>例: `100.00` |
| orders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0.00` |
| orders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `0.00000000` |
| orders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.000` |
| orders[].clientAlgoId | string |  | Client-defined algo order ID<br>用户自定义策略订单 ID<br>例: `acacab56b3c44bef9f6a8f8ebd2a8408` |
| orders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649757019503` |
| orders[].endTime | integer (int64) |  | End time<br>结束时间<br>例: `1649757088101` |
| orders[].algoStatus | string |  | Algo order status<br>策略订单状态<br>例: `CANCELLED` |
| orders[].algoType | string |  | Algo order type<br>策略订单类型<br>例: `VP` |
| orders[].urgency | string |  | Execution urgency<br>执行速率<br>例: `LOW` |

## Query Futures Sub Orders (USER_DATA)（查询执行子订单 (USER_DATA)）

`GET /sapi/v1/algo/futures/subOrders`

Get respective sub orders for a specified algoId

获取指定 algoId 的相应子订单

Operation ID: `querySubOrdersFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) | 是 | eg. 14511<br>例如 14511<br>例: `1` |
| page | query | integer (int64) |  | Page number<br>页码<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Records per page<br>每页记录数<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Orders / 子订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| executedQty | string |  | 例: `1.000` |
| executedAmt | string |  | 例: `3229.44000000` |
| subOrders | object[] |  |  |
| subOrders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `13723` |
| subOrders[].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `8389765519993909000` |
| subOrders[].orderStatus | string |  | Sub-order status<br>子订单状态<br>例: `FILLED` |
| subOrders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `1.000` |
| subOrders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `3229.44000000` |
| subOrders[].feeAmt | string |  | Fee amount<br>手续费<br>例: `-1.61471999` |
| subOrders[].feeAsset | string |  | Fee asset<br>手续费币种<br>例: `USDT` |
| subOrders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649319001964` |
| subOrders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `3229.44` |
| subOrders[].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| subOrders[].symbol | string |  | Trading symbol<br>交易对<br>例: `ETHUSDT` |
| subOrders[].subId | integer (int64) |  | Sub-order execution sequence ID<br>子订单执行顺序 ID<br>例: `1` |
| subOrders[].timeInForce | string |  | Time in force<br>有效方式<br>例: `IMMEDIATE_OR_CANCEL` |
| subOrders[].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1.000` |

## Time-Weighted Futures Average Price (Twap) New Order (TRADE)（时间加权平均价格策略(Twap)下单 (TRADE)）

`POST /sapi/v1/algo/futures/newOrderTwap`

Send in a Twap new order. Only support on USDⓈ-M Contracts.

发送Twap下单. 仅支持U本位合约

Operation ID: `timeWeightedAveragePriceFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading symbol eg. BTCUSDT<br>交易对 eg. BTCUSDT<br>例: `BTCUSDT` |
| side | string | 是 | Trading side ( BUY or SELL )<br>买卖方向 ( BUY or SELL )<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| quantity | number (float) | 是 | Quantity of base asset; The notional (`quantity` * `mark price(base asset)`) must be more than the<br>equivalent of 1,000 USDT, and the maximum notional varies by symbol: up to 50,000,000 USDT for<br>BTCUSDT perpetual, up to 25,000,000 USDT for ETHUSDT perpetual, and up to 5,000,000 USDT for<br>other symbols<br>下单数量， 以合约币种（base asset）个数下单; 名义价值 (`quantity` * `标记价格(base asset)`) 需要大于 1,000 USDT，且上限根据币种有所不同：BTCUSDT永续合约最大为50,000,000<br>USDT，ETHUSDT永续合约最大为25,000,000 USDT，其他币对最大为5,000,000 USDT<br>例: `1` |
| duration | integer (int64) | 是 | Duration for TWAP orders in seconds<br>请请以秒为单位发送[300,86400]<br>例: `5000` |
| clientAlgoId | string |  | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give<br>default value<br>必须传入32位，如果未发送，则自动生成<br>例: `1` |
| reduceOnly | boolean |  | "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a<br>position<br>true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数<br>例: `False` |
| limitPrice | number (float) |  | Limit price of the order; If it is not sent, will place order by market price by default<br>限价单价格; 若未发送，则以市场价下单<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Time-Weighted Average Price / 时间加权平均价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientAlgoId | string |  | 例: `65ce1630101a480b85915d7e11fd5078` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |

## Volume Participation (VP) New Order (TRADE)（成交量份额参与算法(VP)下单 (TRADE)）

`POST /sapi/v1/algo/futures/newOrderVp`

Send in a VP new order. Only support on USDⓈ-M Contracts.

发送VP下单. 仅支持U本位合约

Operation ID: `volumeParticipationFutureAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading symbol eg. BTCUSDT<br>交易对 eg. BTCUSDT<br>例: `BTCUSDT` |
| side | string | 是 | Trading side ( BUY or SELL )<br>买卖方向 ( BUY or SELL )<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| quantity | number (float) | 是 | Quantity of base asset; The notional (`quantity` * `mark price(base asset)`) must be more than the<br>equivalent of 10,000 USDT, and the maximum notional varies by symbol: up to 50,000,000 USDT for<br>BTCUSDT perpetual, up to 25,000,000 USDT for ETHUSDT perpetual, and up to 5,000,000 USDT for<br>other symbols<br>下单数量， 以合约币种（base asset）个数下单; 名义价值 (`quantity` * `标记价格(base asset)`) 需要大于 10,000 USDT，且上限根据币种有所不同：BTCUSDT永续合约最大为50,000,000<br>USDT，ETHUSDT永续合约最大为25,000,000 USDT，其他币对最大为5,000,000 USDT<br>例: `1` |
| urgency | string | 是 | Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH<br>代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）<br>枚举: `LOW`, `MEDIUM`, `HIGH`<br>例: `LOW` |
| clientAlgoId | string |  | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give<br>default value<br>必须传入32位，如果未发送，则自动生成<br>例: `1` |
| reduceOnly | boolean |  | "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a<br>position<br>true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数<br>例: `False` |
| limitPrice | number (float) |  | Limit price of the order; If it is not sent, will place order by market price by default<br>限价单价格; 若未发送，则以市场价下单<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Volume Participation / 成交量份额参与

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientAlgoId | string |  | 例: `00358ce6a268403398bd34eaa36dffe7` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |

## Cancel Spot Algo Order (TRADE)（取消TWAP/VP策略订单 (TRADE)）

`DELETE /sapi/v1/algo/spot/order`

Cancel an open TWAP or VP algo order

取消正在委托的TWAP或VP订单

Operation ID: `cancelAlgoOrderSpotAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) |  | 例: `14511` |
| clientAlgoId | query | string |  | 例: `65ce1630101a480b85915d7e11fd5078` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Cancel Algo Order / 取消策略订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| algoId | integer (int64) |  | 例: `14511` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |

## Query Current Spot Algo Open Orders (USER_DATA)（查询当前策略订单挂单 (USER_DATA)）

`GET /sapi/v1/algo/spot/openOrders`

Get all open Spot TWAP and VP algo orders

查询当前策略订单挂单

Operation ID: `queryCurrentAlgoOpenOrdersSpotAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current Algo Open Orders / 当前策略未完成订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| orders | object[] |  |  |
| orders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `14517` |
| orders[].symbol | string |  | Trading symbol<br>交易对<br>例: `ETHUSDT` |
| orders[].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| orders[].totalQty | string |  | Total order quantity<br>总下单数量<br>例: `5.000` |
| orders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0.000` |
| orders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `0.00000000` |
| orders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.00` |
| orders[].clientAlgoId | string |  | Client-defined algo order ID<br>用户自定义策略订单 ID<br>例: `d7096549481642f8a0bb69e9e2e31f2e` |
| orders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649756817004` |
| orders[].endTime | integer (int64) |  | End time<br>结束时间<br>例: `0` |
| orders[].algoStatus | string |  | Algo order status<br>策略订单状态<br>例: `WORKING` |
| orders[].algoType | string |  | Algo order type<br>策略订单类型<br>例: `TWAP` |
| orders[].urgency | string |  | Execution urgency<br>执行速率<br>例: `LOW` |
| orders[].duration | integer (int64) |  | Order duration in seconds. Only returned for TWAP orders<br>订单执行时长，以秒为单位，仅 TWAP 订单返回<br>例: `86400` |

## Query Historical Spot Algo Orders (USER_DATA)（查询历史策略订单 (USER_DATA)）

`GET /sapi/v1/algo/spot/historicalOrders`

Get all historical Spot TWAP and VP algo orders

查询现货TWAP和VP历史订单

Operation ID: `queryHistoricalAlgoOrdersSpotAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Trading symbol<br>交易对<br>例: `BTCUSDT` |
| side | query | string |  | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| startTime | query | integer (int64) |  | in milliseconds  eg.1641522717552<br>毫秒级时间戳  eg.1641522717552<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | in milliseconds  eg.1641522526562<br>毫秒级时间戳  eg.1641522526562<br>例: `1641782889000` |
| page | query | integer (int64) |  | Page number<br>页码<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Records per page<br>每页记录数<br>默认: `100`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Historical Algo Orders / 历史策略订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| orders | object[] |  |  |
| orders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `14518` |
| orders[].symbol | string |  | Trading symbol<br>交易对<br>例: `BNBUSDT` |
| orders[].side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| orders[].totalQty | string |  | Total order quantity<br>总下单数量<br>例: `100.00` |
| orders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `0.00` |
| orders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `0.00000000` |
| orders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.000` |
| orders[].clientAlgoId | string |  | Client-defined algo order ID<br>用户自定义策略订单 ID<br>例: `acacab56b3c44bef9f6a8f8ebd2a8408` |
| orders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649757019503` |
| orders[].endTime | integer (int64) |  | End time<br>结束时间<br>例: `1649757088101` |
| orders[].algoStatus | string |  | Algo order status<br>策略订单状态<br>例: `CANCELLED` |
| orders[].algoType | string |  | Algo order type<br>策略订单类型<br>例: `TWAP` |
| orders[].urgency | string |  | Execution urgency<br>执行速率<br>例: `LOW` |
| orders[].duration | integer (int64) |  | Order duration in seconds. Only returned for TWAP orders<br>订单执行时长，以秒为单位，仅 TWAP 订单返回<br>例: `86400` |

## Query Spot Sub Orders (USER_DATA)（查询执行子订单 (USER_DATA)）

`GET /sapi/v1/algo/spot/subOrders`

Get respective sub orders for a specified algoId

获取指定 algoId 的相应子订单

Operation ID: `querySubOrdersSpotAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| algoId | query | integer (int64) | 是 | eg. 14511<br>例如 14511<br>例: `1` |
| page | query | integer (int64) |  | Page number<br>页码<br>默认: `1`<br>例: `1` |
| pageSize | query | integer (int64) |  | Records per page<br>每页记录数<br>默认: `100`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub Orders / 子订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| executedQty | string |  | 例: `1.000` |
| executedAmt | string |  | 例: `3229.44000000` |
| subOrders | object[] |  |  |
| subOrders[].algoId | integer (int64) |  | Algo order ID<br>策略订单 ID<br>例: `13723` |
| subOrders[].orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `8389765519993909000` |
| subOrders[].orderStatus | string |  | Sub-order status<br>子订单状态<br>例: `FILLED` |
| subOrders[].executedQty | string |  | Executed quantity<br>执行数量<br>例: `1.000` |
| subOrders[].executedAmt | string |  | Executed amount<br>执行金额<br>例: `3229.44000000` |
| subOrders[].feeAmt | string |  | Fee amount<br>手续费<br>例: `-1.61471999` |
| subOrders[].feeAsset | string |  | Fee asset<br>手续费币种<br>例: `USDT` |
| subOrders[].bookTime | integer (int64) |  | Order creation time<br>下单时间<br>例: `1649319001964` |
| subOrders[].avgPrice | string |  | Average execution price<br>平均价格<br>例: `3229.44` |
| subOrders[].side | string |  | Trading side<br>买卖方向<br>例: `SELL` |
| subOrders[].symbol | string |  | Trading symbol<br>交易对<br>例: `ETHUSDT` |
| subOrders[].subId | integer (int64) |  | Sub-order execution sequence ID<br>子订单执行顺序 ID<br>例: `1` |
| subOrders[].timeInForce | string |  | Time in force<br>有效方式<br>例: `IMMEDIATE_OR_CANCEL` |
| subOrders[].origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1.000` |

## Time-Weighted Spot Average Price(Twap) New Order (TRADE)（时间加权平均价格策略(Twap)下单 (TRADE)）

`POST /sapi/v1/algo/spot/newOrderTwap`

Place a new spot TWAP order with Algo service.

通过算法服务进行时间加权平均价格策略（TWAP）下单交易

Operation ID: `timeWeightedAveragePriceSpotAlgo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading symbol eg. BTCUSDT<br>交易对 eg. BTCUSDT<br>例: `BTCUSDT` |
| side | string | 是 | Trading side ( BUY or SELL )<br>买卖方向 ( BUY or SELL )<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please<br>reduce your size if you order is above the maximum notional per order.<br>下单数量， 以Base资产个数下单; 每单支持最大的金额会是200,000， 2,000,000或者10,000,000 USD等额的，取决于币对。请降低您的下单金额，如果您的下单金额超过了上限。<br>例: `1` |
| duration | integer (int64) | 是 | Duration for TWAP orders in seconds<br>请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h<br>例: `5000` |
| clientAlgoId | string |  | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give<br>default value<br>必须传入32位，如果未发送，则自动生成<br>例: `1` |
| limitPrice | number (float) |  | Limit price of the order; If it is not sent, will place order by market price by default<br>限价单价格; 若未发送，则以市场价下单<br>例: `1` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Time-Weighted Average Price / 时间加权平均价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientAlgoId | string |  | 例: `65ce1630101a480b85915d7e11fd5078` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |

## Volume Participation (VP) New Order (TRADE)（成交量份额参与算法(VP)下单 (TRADE)）

`POST /sapi/v1/algo/spot/newOrderVp`

Place a new spot VP (Volume Participation) order with Algo service. A VP order automatically slices the total quantity over time, targeting a percentage of the market volume.

通过算法服务进行现货成交量份额参与（VP）下单交易。VP 订单会随时间自动拆分总下单数量，目标是参与一定比例的市场成交量。

Operation ID: `volumeParticipation`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading symbol eg. BTCUSDT<br>交易对 eg. BTCUSDT<br>例: `BTCUSDT` |
| side | string | 是 | Trading side ( BUY or SELL )<br>买卖方向 ( BUY or SELL )<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| quantity | number (float) | 是 | Total order quantity in base asset; The notional must be at least the equivalent of 1,000 USDT, and the<br>maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if your<br>order is above the maximum notional per order.<br>下单总数量，以 Base 资产个数计；订单金额不得低于等值 1,000 USDT，每单支持的最大金额为 200,000、2,000,000 或 10,000,000 USD 等值，取决于币对。如果下单金额超过上限，请降低下单数量。<br>例: `1` |
| urgency | string | 是 | Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH<br>代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）<br>枚举: `LOW`, `MEDIUM`, `HIGH`<br>例: `LOW` |
| clientAlgoId | string |  | A unique id among Algo orders (length should be 32 characters). If it is not sent, we will give<br>default value. Must be unique across all open Algo orders.<br>必须传入32位，如果未发送，则自动生成；需在所有未完成策略订单中唯一<br>例: `1` |
| vpTimeLimit | integer (int64) |  | Max allowed duration in seconds (minimum 300, maximum 86400). If it is not sent, 86400 is used and the<br>order runs until fully filled or cancelled.<br>允许的最长执行时间，以秒为单位（最小 300，最大 86400）；若未发送，默认使用 86400，订单将持续执行直至完全成交或被取消<br>例: `5000` |
| recvWindow | integer (int64) |  | Cannot be greater than 60000<br>不能大于 60000<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Volume Participation / 成交量份额参与

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clientAlgoId | string |  | 例: `65ce1630101a480b85915d7e11fd5078` |
| success | boolean |  | 例: `True` |
| code | integer (int64) |  | 例: `0` |
| msg | string |  | 例: `OK` |