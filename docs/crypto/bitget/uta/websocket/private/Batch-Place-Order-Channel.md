---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Batch-Place-Order-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:02:07.490114
---

# Batch Place Order Channel

### Description

:::tip

The ACK response only indicates that the request has been successfully accepted. Please use the [WebSocket order](/docs/uta/websocket/private/Order-Channel) push channel to confirm the actual order status.

:::

> This endpoint does not support Reality stock trading pairs. To place Reality stock orders, please use the [Place Reality Order](/docs/catalog/reality/trading#place-reality-order) endpoint.

This endpoint allows the order placement across spot, margin, or futures markets with customizable parameters, including
price, quantity, and order type, etc.

- Maximum 20 orders allowed in a single request

- **Partial Success Handling**<br/>
  Each order within the batch is processed independently. If one order fails, it does not affect the placement of the other orders in the same batch. The `args` array in the response returns one result object per order, each carrying its own `code` and `msg`; please check every item in the response list to confirm the actual outcome of each order.

- **Futures** <br/>
  `reduce-only` orders are not supported

- **Margin** <br/>Margin orders will automatically trigger fund borrowing.

- **Order Check**
  - **Futures**:`price` must meet the price multiplier and be a multiple of `priceMultiplier`, and conform to the `pricePrecision` decimal places. `qty` must be greater than or equal to `minOrderAmount` and be a multiple of `quantityMultiplier`.

  - **Spot**:`price` must meet the decimal place requirement. `qty` must be greater than or equal to `minOrderAmount`.
  - Related parameters can be obtained via [Instruments](/docs/catalog/market/market-data#get-instruments).

- **Open Position Logic**
  - **[Hedge-mode](https://www.bitget.com/support/articles/12560603817602)**<br/>
    Open long: `side=buy` & `posSide=long`<br/>
    Open Short:  `side=sell` & `posSide=short`<br/>
    Close long: `side=sell` & `posSide=long`<br/>
    Close short: `side=buy` & `posSide=short`<br/>

  - **One-way-mode**<br/>
    Open long: `side=buy`<br/>
    Open short: `side=sell`<br/>
    Close long: `side=sell` & `reduceOnly=yes`<br/>
    Close short: `side=buy` & `reduceOnly=yes`<br/>

- **Order Limit**
  - The specific limit can be obtained via [Instruments](/docs/catalog/market/market-data#get-instruments). The relevant fields are:
    - `maxSymbolOrderNum`: Maximum number of pending orders allowed for a single trading pair
    - `maxProductOrderNum`: Maximum number of pending orders allowed across all pairs within a product line

- **Request Monitor**<br/>
  The API requests will be monitored. If the total number of orders for a single account (including master and sub-accounts) exceeds a set daily limit (UTC 00:00 - UTC 24:00), the platform reserves the right to issue reminders, warnings, and enforce necessary restrictions. By using the API, clients acknowledge and agree to comply with these terms.

- **API Broker rebate identifier**:<br/>
  The following code block needs to be added to the HTTP Header of the request.
  > "X-CHANNEL-API-CODE":"your-channel-api-code"

- **COIN-M Futures Symbol Format Description:**<br/>
  - **<u>The symbol format for the new COIN-M business line is "XXXUSD_CM". For example, the BTCUSD trading pair in COIN-M futures is formatted as BTCUSD_CM.</u>**
  - The new COIN-M business line does not support modifying orders

- Note: If errors `40010`, `40725`, or `45001` occur when placing an order, please use `clientOid` to query the order details to confirm the final result of the operation.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "trade",
    "id": "1750035029506",
    "category": "spot",
    "topic": "batch-place",
    "args": [
        {
            "clientOid": "xxxxxxxx",
            "orderType": "limit",
            "price": "100",
            "qty": "0.1",
            "side": "buy",
            "symbol": "BTCUSDT",
            "timeInForce": "gtc"
        },
        {
            "clientOid": "xxxxxxxx",
            "orderType": "limit",
            "price": "100",
            "qty": "0.15",
            "side": "buy",
            "symbol": "BTCUSDT",
            "timeInForce": "gtc"
        }
    ]
}
```

### Request Parameters

| Parameter         | Type               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 
|:------------------|:-------------------|----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                | String             | Yes      | Operation: <br/> `trade`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| id                | String             | Yes      | Request identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| topic             | String             | Yes      | Topic: <br/> `batch-place`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| category          | String             | Yes      | Category (must be lowercase)<br/>`spot`Spot<br/>`margin` Margin<br/> `usdt-futures` USDT futures<br/>`coin-futures` Coin futures<br/>`usdc-futures` USDC futures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| args              | List&lt;Object&gt; | Yes      | Channel list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &gt; symbol       | String             | Yes      | Symbol name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &gt; [orderType](/docs/uta/enum#ordertype)    | String             | Yes      | Order type <br/>`limit` : Limit order<br/> `market` : Market order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &gt; qty          | String             | Yes      | Order quantity <br/>`Spot/Margin`<br/> For market buy orders,the unit is **quote coin**<br/>For limit and market sell orders, the unit is **base coin**<br/> `USDT/USDC-Futures` <br/> The unit is **base coin** <br/> `COIN-Futures` <br/> The unit is **<u>quote coin</u>**                                                                                                                                                                                                                                                                                                                                                                                                            |
| &gt; price        | String             | No       | Order price<br/>This field is required when the order type is a `limit` order .<br/>This field is not applicable  when the order type is a `market` order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &gt; side         | String             | Yes      | Order side<br/>`buy`<br/>`sell`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &gt; posSide      | String             | No       | Position side<br/>`long` <br/>`short` <br/>This field is required in hedge-mode positions.<br/>Available only for futures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &gt; timeInForce  | String             | No       | Time in force <br/> `gtc`: Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`ioc`: Immediate or cancel. It must be executed immediately, with any unfilled portion canceled.<br/>`fok`: Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/> `post_only`: Post only. It will only be added to the order book as a maker. <br/>[`rpi`](https://www.bitget.com/support/articles/12560603867770) Retail Price Improvement order. A non-displayed limit order that provides price improvement for retail order flow. Only available for accounts with RPI market maker permissions. <br/>When orderType is `limit`, it defaults to `gtc`; <br/>when orderType is `market`, the system will execute it as `ioc`<br/>This field is ignored when trading Reality stock pairs (rtoken, e.g. rAAPLUSDT) |
| &gt; clientOid    | String             | No       | Client order ID<br/>Must match the regular expression `^[0-9A-Za-z_:#\-+\s]{1,32}$`, i.e. 1 to 32 characters, consisting of uppercase and lowercase letters, digits, underscores (_), hyphens (-), plus signs (+), colons (:), number signs (#), and spaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &gt; stpMode      | String             | No       | [STP Mode(Self Trade Prevention)](https://www.bitget.com/support/articles/12560603812732)<br/>`none`: STP is not applied; orders are matched normally without comparing user IDs (Default)<br/>`cancel_taker`: when a self-trade is detected, the taker order is canceled and the maker order remains in the order book  <br/>`cancel_maker`: when a self-trade is detected, the maker order is canceled and the taker order continues to execute  <br/>`cancel_both`: when a self-trade is detected, both the taker and maker orders are canceled<br/>The STP action is determined by the taker order's `stpMode`; the maker order's existing `stpMode` setting is not considered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &gt; tpTriggerBy  | String             | No       | Preset Take-Profit Trigger Type<br/>`market`Market Price<br/>`mark` Mark Price<br/>If not specified, the default value is market price <br/> Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &gt; slTriggerBy  | String             | No       | Preset Stop-Loss Trigger Type<br/>`market`Market Price<br/>`mark` Mark Price<br/>If not specified, the default value is market price <br/> Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &gt; takeprofit   | String             | No       | Preset Take-Profit Trigger Price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &gt; stoploss     | String             | No       | Preset Stop-Loss Trigger Price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &gt; tpOrderType  | String             | No       | Take-Profit Trigger Strategy Order Type<br/>`limit` Limit Order<br/>`market` Market Order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &gt; slOrderType  | String             | No       | Stop-Loss Trigger Strategy Order Type<br/>`limit` Limit Order<br/>`market` Market Order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| &gt; tpLimitPrice | String             | No       | Take-Profit Strategy Order Execution Price<br/>This field is only valid for limit orders (when `tpOrderType=limit`); it is ignored for market orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &gt; slLimitPrice | String             | No       | Stop-Loss Strategy Order Execution Price<br/>This field is only valid for limit orders (when `slOrderType=limit`); it is ignored for market orders. |
| &gt; pxAmendType | String             | No       | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

</div>


<div className="api-aligning">

```json title="Response Example"
{
  "event": "trade",
  "id": "1750035029506",
  "category": "spot",
  "topic": "batch-place",
  "args": [
    {
      "code": "0",
      "msg": "Success",
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    },
    {
      "code": "0",
      "msg": "Success",
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "receiveTime": "1750034396999456",
      "pushTime": "1750034397077789"
    }
  ],
  "code": "0",
  "msg": "Success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1750035029925"
}
```

### Response Parameters

| Parameters        | Type               | Description                                                                                                                                   |
|:------------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| event             | String             | Event<br/>`trade`/`error`                                                                                                                     |
| id                | String             | Request identifier                                                                                                                            |
| topic             | String             | Topic: <br/> `batch-place`                                                                                                                    |
| category          | String             | Category <br/>`spot`Spot<br/>`margin` Margin<br/> `usdt-futures` USDT futures<br/>`coin-futures` Coin futures<br/>`usdc-futures` USDC futures |
| args              | List&lt;Object&gt; | Channel list                                                                                                                                  |
| &gt; symbol       | String             | Symbol name                                                                                                                                   |
| &gt; orderId      | String             | Order ID                                                                                                                                      |
| &gt; clientOid    | String             | Client order ID                                                                                                                               |
| &gt; receiveTime  | String             | Gateway receive time <br/>Unix microsecond timestamp                                                                                          |
| &gt; pushTime     | String             | Gateway push time <br/>Unix microsecond timestamp                                                                                             |
| &gt; code         | String             | Code                                                                                                                                          |
| &gt; msg          | String             | Message                                                                                                                                       |
| code              | String             | Code                                                                                                                                          |
| msg               | String             | Message                                                                                                                                       |
| connId            | String             | Connection ID                                                                                                                                 |
| rateLimit         | Array              | Rate limit balance array                                                                                                                      |
| &gt; limit        | String             | Rate limit quota for this dimension                                                                                                           |
| &gt; remaining    | String             | Remaining available quota                                                                                                                     |
| ts                | String             | Timestamp                                                                                                                                     |

</div>

---

# 批量下单

### 描述

:::tip

ACK 仅表示请求被成功接受，请使用 [WebSocket order](/zh-CN/docs/uta/websocket/private/Order-Channel) 推送来确认订单的实际状态。

:::

该接口支持现货、杠杆及合约的批量下单，并可以自定义包括价格、数量和订单类型等参数。

- 单次调用最多支持20笔订单

- **部分成功处理**<br/>
  批量中的每笔订单独立处理，某一笔订单失败不影响同批次其他订单的下单。返回结果中每笔订单各自带一个结果对象，包含独立的 `code` 和 `msg`，请逐一检查返回列表中的每一项以确认每笔订单的实际执行结果。

- **合约交易**<br/>暂不支持`reduce-only`订单

- **杠杆交易**<br/>杠杆下单会自动借贷

- **订单检查**
  - **合约**：`Price`下单价格要满足价格乘数`priceMultiplier`的倍数，并且符合`pricePrecision`小数位。`qty`要满足大于
    `minTradeUSDT`并且满足`quantityMultiplier`的倍数

  - **现货**：`price`要满足小数位。`qty`下单数量必须要大于`minTradeUSDT`
  - 相关参数可以通过[这里](/zh-CN/docs/catalog/market/market-data#get-instruments)获取；

- **开仓逻辑**
  - **[双向持仓](https://www.bitget.com/zh-CN/support/articles/12560603817602)**<br/>
    开多： `side=buy` & `posSide=long`<br/>
    开空：`side=sell` & `posSide=short`<br/>
    平多：`side=sell` & `posSide=long`<br/>
    平空：`side=buy` & `posSide=short`<br/>

  - **单向持仓**<br/>
    开多 `side`:buy<br/>
    开空 `side`:sell<br/>
    平多 `side`:sell   `reduceOnly`:yes<br/>
    平空 `side`:buy    `reduceOnly`:yes<br/>

- **订单持有上限:**
  - 具体上限可以通过[这里](/zh-CN/docs/catalog/market/market-data#get-instruments)获取，相关字段：
    - `maxSymbolOrderNum`：单个交易对维度的最大委托数量
    - `maxProductOrderNum`：同一业务线下所有交易对的最大委托数量

- **请求监控**:<br/>
  将针对您的 API 请求进行统计监控，当单日 (UTC 0点 - UTC 24点) 单账号（母账号和子账号整体运算）订单总数超过一定上限，平台将保留提醒、警告，以及进行必要性限制的权利。
  使用API的客户预设接收本条款并负有配合调整的义务。

- **API Broker返佣标识**:<br/>
  需在HTTP Header请求头中添加如下代码块
  > "X-CHANNEL-API-CODE":"your-channel-api-code"

- **币本位合约说明**:<br/>
  - **<u>新币本位业务线symbol格式为"XXXUSD_CM"，例如BTCUSD交易对在币本位合约的格式为BTCUSD_CM</u>**
  - 新币本位暂时不支持修改订单

- 注意：操作订单时出现 `40010` `40725` `45001` 错误码，请用`clientOid`查询订单详情，以确认操作的最终结果

<div className="api-aligning">

```json title="请求示例"
{
    "op": "trade",
    "id": "1750035029506",
    "category": "spot",
    "topic": "batch-place",
    "args": [
        {
            "clientOid": "xxxxxxxx",
            "orderType": "limit",
            "price": "100",
            "qty": "0.1",
            "side": "buy",
            "symbol": "BTCUSDT",
            "timeInForce": "gtc"
        },
        {
            "clientOid": "xxxxxxxx",
            "orderType": "limit",
            "price": "100",
            "qty": "0.15",
            "side": "buy",
            "symbol": "BTCUSDT",
            "timeInForce": "gtc"
        }
    ]
}
```

### 请求参数

| 参数名               | 参数类型               | 是否必须 | 描述                                                                                                                                                                                                                                                     | 
|:------------------|:-------------------|------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                | String             | 是    | 操作: <br/> `trade` 交易                                                                                                                                                                                                                                   |
| id                | String             | 是    | 请求标识                                                                                                                                                                                                                                                   |
| topic             | String             | 是    | 频道名: <br/> `batch-place` 下单                                                                                                                                                                                                                            |
| category          | String             | 是    | 业务线（必须小写）<br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约                                                                                                                                     |
| args              | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                                                                                                                                                                              |
| &gt; symbol       | String             | 是    | 交易对名称                                                                                                                                                                                                                                                  |
| &gt; [orderType](/zh-CN/docs/uta/enum#ordertype)    | String             | 是    | 订单类型 <br/>`limit` : 限价<br/> `market` : 市价                                                                                                                                                                                                              |
| &gt; qty          | String             | 是    | 下单数量<br/> - 现货<br/> 市价买单，单位为quote coin<br/>限价及市价卖单，单位为base coin <br/> USDT/USDC合约： <br/> 单位为**base coin**  <br/> 币本位合约： <br/> 单位为 **<u>quote coin</u>**                                                                                                |
| &gt; price        | String             | 否    | 下单价格<br/>订单类型为限价单`limit`时，该字段必填<br/>订单类型为市价单`market`时，该字段失效                                                                                                                                                                                            |
| &gt; side         | String             | 是    | 下单方向<br/>`buy`: 买<br/>`sell`: 卖                                                                                                                                                                                                                        |
| &gt; posSide      | String             | 否    | 交易方向<br/>`long` 多仓<br/>`short` 空仓<br/>只限于合约传此参数 其他忽略<br/>用于合约双向持仓                                                                                                                                                                                      |
| &gt; timeInForce  | String             | 否    | [订单执行策略](https://www.bitget.com/zh-CN/support/articles/12560603818004) <br/> `gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤销 <br/> `post_only`: 只做maker <br/>[`rpi`](https://www.bitget.com/zh-CN/support/articles/12560603867770): 零售价格优化订单，为零售订单流提供价格优化的非显示限价单。仅限拥有RPI做市商权限的账户使用。<br/>订单类型为限价单`limit`时，默认值为`gtc`；<br/>订单类型为市价单`market`时，系统会按照`ioc`执行<br/>交易Reality 股票交易对（rtoken，如 rAAPLUSDT）时忽略该字段 |
| &gt; clientOid    | String             | 否    | 自定义订单ID<br/>需满足正则表达式 `^[0-9A-Za-z_:#\-+\s]{1,32}$`，即 1-32 个字符，可包含大小写字母、数字、下划线(_)、连字符(-)、加号(+)、冒号(:)、井号(#)和空格                                                                                                                                                                                                                                                |
| &gt; stpMode      | String             | 否    | [STP（自成交预防）模式](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br/>`none`：不比较双方用户ID，订单正常成交，不触发STP（默认值）<br/>`cancel_taker`：检测到自成交时，取消taker（吃单方）订单，maker（挂单方）订单保留在订单簿中 <br/>`cancel_maker`：检测到自成交时，取消maker（挂单方）订单，taker（吃单方）订单继续执行 <br/>`cancel_both`：检测到自成交时，taker和maker订单都取消<br/>STP判定以taker订单自身携带的`stpMode`为准，不看maker订单原有的`stpMode`设置                                                                                                                                  |
| &gt; tpTriggerBy  | String             | 否    | 预设止盈触发类型<br/>`market`市场价格<br/>`mark`标记价格<br/>如不填写，默认值为`market`市场价格<br/>该字段仅针对合约业务线`usdt-futures`，`coin-futures`及`usdc-futures`生效                                                                                                                       |
| &gt; slTriggerBy  | String             | 否    | 预设止损触发类型<br/>`market`市场价格<br/>`mark`标记价格<br/>如不填写，默认值为`market`市场价格<br/>该字段仅针对合约业务线`usdt-futures`，`coin-futures`及`usdc-futures`生效                                                                                                                       |
| &gt; takeprofit   | String             | 否    | 预设止盈触发价格                                                                                                                                                                                                                                               |
| &gt; stoploss     | String             | 否    | 预设止损触发价格                                                                                                                                                                                                                                               |
| &gt; tpOrderType  | String             | 否    | 止盈触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单                                                                                                                                                                                                            |
| &gt; slOrderType  | String             | 否    | 止损触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单                                                                                                                                                                                                            |
| &gt; tpLimitPrice | String             | 否    | 止盈策略单执行价格<br/>仅限价单`tpOrderType=limit`时有效，市价单忽略该参数                                                                                                                                                                                                      |
| &gt; slLimitPrice | String             | 否    | 止损策略单执行价格<br/>仅限价单`slOrderType=limit`时有效，市价单忽略该参数                                                                                                                                                                                                      |
| &gt; pxAmendType | String             | 否    | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

</div>


<div className="api-aligning">

```json title="响应示例"
{
  "event": "trade",
  "id": "1750035029506",
  "category": "spot",
  "topic": "batch-place",
  "args": [
    {
      "code": "0",
      "msg": "Success",
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    },
    {
      "code": "0",
      "msg": "Success",
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "receiveTime": "1750034396999456",
      "pushTime": "1750034397077789"
    }
  ],
  "code": "0",
  "msg": "Success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1750035029925"
}
```

### 响应参数说明

| 返回字段           | 参数类型               | 字段说明                                                                                                               |
|:---------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------|
| event          | String             | 事件<br/>`trade` 交易<br/>`error`参数错误                                                                                  |
| id             | String             | 请求标识                                                                                                               |
| topic          | String             | 频道名<br/>`batch-place` 批量下单                                                                                         |
| category       | String             | 业务线 <br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| args           | List&lt;Object&gt; | 订单列表                                                                                                               |
| &gt; symbol    | String             | 交易对名称，如`BTCUSDT`                                                                                                   |
| &gt; orderId   | String             | 订单ID                                                                                                               |
| &gt; clientOid | String             | 自定义订单ID                                                                                                            |
| &gt; receiveTime | String           | 网关接收时间 <br/>Unix微秒时间戳                                                                                             |
| &gt; pushTime  | String             | 网关推送时间 <br/>Unix微秒时间戳                                                                                             |
| &gt; code      | String             | 状态码                                                                                                                |
| &gt; msg       | String             | 状态消息                                                                                                               |
| code           | String             | 状态码                                                                                                                |
| msg            | String             | 状态消息                                                                                                               |
| connId         | String             | 连接ID                                                                                                               |
| rateLimit      | Array              | 限频余额数组                                                                                                             |
| &gt; limit     | String             | 该维度限额                                                                                                              |
| &gt; remaining | String             | 剩余可用次数                                                                                                             |
| ts             | String             | 时间戳                                                                                                                |

</div>