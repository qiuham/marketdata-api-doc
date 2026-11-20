---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Place-Order-Channel
api_type: WebSocket
updated_at: 2026-11-20 19:01:34.411730
---

# Place Order Channel

### Description

:::tip

The ACK response only indicates that the request has been successfully accepted. Please use the [WebSocket order](/docs/uta/websocket/private/Order-Channel) push channel to confirm the actual order status.

:::

This endpoint allows order placement across spot, margin, or futures markets, as well as Reality (rToken) stocks, with customizable parameters, including
price, quantity, and order type, etc.

- Reality (rToken) rate limit, determined by `venue`<br/>
  `internal_market` (on-exchange): follows the Crypto rate limit, 10/sec/UID<br/>
  Default strategy (`venue` omitted) and `lit_market` (off-exchange): follow the rToken rate limit, 5/sec/UID by default, 30/sec/UID for whitelisted users (contact your BD/RM to apply).

- Futures<br/>
  For one-way mode, reduce-only orders are allowed to place. If a reduce only order already exists and the order
  quantity equals the position size, or if a new reduce only order exceeds the remaining position size, the previous
  reduction order will be automatically canceled and replaced. In this case, the returned orderId will be null.
  It is recommended to always provide a clientOid.
- Margin<br/>
  Margin orders will automatically trigger fund borrowing.
- Order Check
    - Futures:price must meet the price multiplier and be a multiple of priceMultiplier, and conform to the
      pricePrecision decimal places. qty must be greater than or equal to minOrderAmount and be a multiple of
      quantityMultiplier.
    - Spot:price must meet the decimal place requirement. qty must be greater than or equal to minOrderAmount.
- Open Position Logic
    - Hedge-mode<br/>
      Open long: side=buy & posSide=long<br/>
      Open Short: side=sell & posSide=short<br/>
      Close long: side=sell & posSide=long<br/>
      Close short: side=buy & posSide=short<br/>
    - One-way-mode<br/>
      Open long: side=buy<br/>
      Open short: side=sell<br/>
      Close long: side=sell & reduceOnly=yes<br/>
      Close short: side=buy & reduceOnly=yes<br/>
- Order Limit
    - Futures: 400 orders across all USDT, Coin-M, and USDC futures trading pairs.
    - Spot: 400 orders across all spot and margin trading pairs.
- ClientOid Constraints
  Please ensure your clientOid matches the regular expression `^[0-9A-Za-z_:#\\-+\\s]{1,32}$`, consisting of 1 to 32
  characters, including periods (.), uppercase letters, colons (:), lowercase letters, numbers, underscores (_), and
  hyphens (-).
- Request Monitor <br/>
  The API requests will be monitored. If the total number of orders for a single account (including master and
  sub-accounts) exceeds a set daily limit (UTC 00:00 - UTC 24:00), the platform reserves the right to issue reminders,
  warnings, and enforce necessary restrictions. By using the API, clients acknowledge and agree to comply with these
  terms.
- Error Sample `{ "code":"40762", "msg":"The order size is greater than the max open size", "requestTime":1627293504612 }`
  This error code may occur in the following scenarios.
    - Insufficient account balance.
    - The position tier for this symbol has reached its
      limit. <a href='https://www.bitget.com/trade-info/position-gear?symbolId=BTCUSDT_UMCBL'>Position tiers</a>
- Note: If the following errors occur when placing an order, please use clientOid to query the order details to confirm
  the final result of the operation.<br/>

- **COIN-M Futures Symbol Format Description:**<br/>
    - <u>The symbol format for the new COIN-M business line is "XXXUSD_CM". For example, the BTCUSD trading pair in
      COIN-M futures is formatted as BTCUSD_CM.</u>
    - The new COIN-M business line does not support modifying orders, ADL, strategy orders，or preset
      take-profit/stop-loss orders.

```json title="Error Code Examples"
{ "code": "40010", "msg": "Request timed out", "id": 1666268894074, "event":"error" }
{ "code": "40725", "msg": "service return an error", "id": 1666268894071, "event":"error" }
{ "code": "45001", "msg": "Unknown error", "id": 1666268894071, "event":"error" }
```

<div className="api-aligning">

```json title="Request Example"
{
  "op": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "requestTime": "1750034396082",
  "args": [
    {
      "orderType": "limit",
      "price": "100",
      "qty": "0.1",
      "side": "buy",
      "symbol": "BTCUSDT",
      "timeInForce": "gtc",
    }
  ]
}
```

### Request Parameters

| Parameter         | Type               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:------------------|:-------------------|----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                | String             | Yes      | Operation: <br/> `trade`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| id                | String             | Yes      | Request identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| topic             | String             | Yes      | Topic: <br/> `place-order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| category          | String             | Yes      | Category (must be lowercase)<br/>`spot`Spot<br/>`margin` Margin<br/> `usdt-futures` USDT futures<br/>`coin-futures` Coin futures<br/>`usdc-futures` USDC futures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| apiCode           | String             | No       | API rebate identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| requestTime       | String             | No       | Request time (client-side timestamp)<br/>Used to calculate the time difference with `receiveWindow`<br/>If not provided, `receiveWindow` will have no effect <br/>Millisecond timestamp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| args              | List&lt;Object&gt; | Yes      | Channel list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &gt; symbol       | String             | Yes      | Symbol name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &gt; [orderType](/docs/uta/enum#ordertype)    | String             | Yes      | Order type <br/>`limit` : Limit order<br/> `market` : Market order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &gt; qty          | String             | Yes      | Order quantity <br/>`Spot/Margin`<br/> For market buy orders,the unit is **quote coin**<br/>For limit and market sell orders, the unit is **base coin**<br/> `USDT/USDC-Futures` <br/> The unit is **base coin** <br/> `COIN-Futures` <br/> The unit is **<u>quote coin</u>**                                                                                                                                                                                                                                                                                                                                                                                                           |
| &gt; price        | String             | No       | Order price <br/> This field is required when the order type is a `limit` order .<br/>This field is not applicable  when the order type is a `market` order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &gt; side         | String             | Yes      | Order side<br/>`buy`<br/>`sell`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &gt; posSide      | String             | No       | Position side<br/>`long` <br/>`short` <br/>This field is required in hedge-mode positions.<br/>Available only for futures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &gt; timeInForce  | String             | No       | [Time in force](https://www.bitget.com/support/articles/12560603818004) <br/> `gtc`: Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`ioc`: Immediate or cancel. It must be executed immediately, with any unfilled portion canceled.<br/>`fok`: Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/> `post_only`: Post only. It will only be added to the order book as a maker. <br/>[`rpi`](https://www.bitget.com/support/articles/12560603867770) Retail Price Improvement order. A non-displayed limit order that provides price improvement for retail order flow. Only available for accounts with RPI market maker permissions.<br/> When orderType is `limit`, it defaults to `gtc`; <br/>when orderType is `market`, the system will execute it as `ioc`<br/>This field is ignored when trading Reality stock pairs (rtoken, e.g. rAAPLUSDT) |
| &gt; reduceOnly   | String             | No       | Reduce-only identifier<br/>`YES`/`NO`<br/>default`NO`; `YES` indicates that your position may only be reduced in size upon the activation of this order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &gt; clientOid    | String             | No       | Client order ID<br/>Must match the regular expression `^[0-9A-Za-z_:#\-+\s]{1,32}$`, i.e. 1 to 32 characters, consisting of uppercase and lowercase letters, digits, underscores (_), hyphens (-), plus signs (+), colons (:), number signs (#), and spaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &gt; stpMode      | String             | No       | [STP Mode(Self Trade Prevention)](https://www.bitget.com/support/articles/12560603812732)<br/>`none`: STP is not applied; orders are matched normally without comparing user IDs (Default)<br/>`cancel_taker`: when a self-trade is detected, the taker order is canceled and the maker order remains in the order book  <br/>`cancel_maker`: when a self-trade is detected, the maker order is canceled and the taker order continues to execute  <br/>`cancel_both`: when a self-trade is detected, both the taker and maker orders are canceled<br/>The STP action is determined by the taker order's `stpMode`; the maker order's existing `stpMode` setting is not considered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &gt; tpTriggerBy  | String             | No       | Preset Take-Profit Trigger Type<br/>`market`Market Price<br/>`mark` Mark Price<br/>If not specified, the default value is market price <br/> Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &gt; slTriggerBy  | String             | No       | Preset Stop-Loss Trigger Type<br/>`market`Market Price<br/>`mark` Mark Price<br/>If not specified, the default value is market price <br/> Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &gt; takeprofit   | String             | No       | Preset Take-Profit Trigger Price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &gt; stoploss     | String             | No       | Preset Stop-Loss Trigger Price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &gt; tpOrderType  | String             | No       | Take-Profit Trigger Strategy Order Type<br/>`limit` Limit Order<br/>`market` Market Order<br/>For Reality (rtoken) trading pairs, only `market` is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &gt; slOrderType  | String             | No       | Stop-Loss Trigger Strategy Order Type<br/>`limit` Limit Order<br/>`market` Market Order<br/>For Reality (rtoken) trading pairs, only `market` is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| &gt; tpLimitPrice | String             | No       | Take-Profit Strategy Order Execution Price<br/>This field is only valid for limit orders (when `tpOrderType=limit`); it is ignored for market orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &gt; slLimitPrice | String             | No       | Stop-Loss Strategy Order Execution Price<br/>This field is only valid for limit orders (when `slOrderType=limit`); it is ignored for market orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &gt; marginMode      | String             | No       | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to cross margin<br/>Available only for futures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &gt; autoBorrow      | String             | No       | Auto borrow switch<br/>`yes` Enable<br/>`no` Disable (default)<br/>Only applicable to spot orders. When enabled, if the obtained coin does not support borrowing while the consumed coin does, and the available balance of the consumed coin is insufficient, the system automatically borrows the consumed coin to make up the shortfall. |
| &gt; pxAmendType     | String             | No       | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |
| &gt; venue           | String             | No       | Order routing strategy<br/>`internal_market` Orders are matched within the exchange and are not submitted to the U.S. stock broker<br/>`lit_market` Orders are submitted to the U.S. stock broker for execution and are not matched within the exchange<br/>If not provided, the default strategy applies: orders are first matched internally within the exchange at the best price; any unfilled portion is submitted to the broker<br/>This field is only effective for Reality (rtoken) trading pairs |
| &gt; rTokenTimeInForce | String           | No       | Order execution strategy for Reality (rtoken) trading pairs<br/>`gtd` Valid for the current session. If placed during US market trading hours (weekdays), the limit order is valid until the end of after-hours trading; if placed on weekends, it is valid until just before the next US market open<br/>`gtc` Valid for 90 days<br/>If not provided, defaults to `gtd`<br/>This field is only effective for Reality (rtoken) trading pairs |
| &gt; bboLevel        | String             | No       | BBO level<br/>`queue1` Same-side price level 1<br/>`queue5` Same-side price level 5<br/>`counterparty1` Opposite-side price level 1<br/>`counterparty5` Opposite-side price level 5<br/>Only supported for limit orders; ignored for market orders |
| &gt; slippageTolerance | String           | No       | Slippage percentage<br/>Default: 2%. Range: [0.01, 0.05], up to 2 decimal places<br/>Only supported for market orders<br/>Higher slippage can increase the likelihood of executing orders, but the execution price may deviate significantly from the last price. |
| &gt; receiveWindow   | String             | No       | Receive window, in milliseconds. Valid range: `[10, 60000]`<br/>If the matching engine receives the order before `requestTime + receiveWindow`, the order is accepted and placed into the order book as usual. If it is received after that window, the order is canceled and `cancelReason` is set to `cancel_receiveWindow`<br/>Note: `receiveWindow` is only effective when `requestTime` is also provided                                                                                                                                                                                                                                                                                                                                                                                                                                       |

</div>


<div className="api-aligning">

```json title="Response Example"
{
  "event": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "cTime": "1750034397008",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    }
  ],
  "code": "0",
  "msg": "success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1750034397076"
}
```

### Response Parameters

| Parameters        | Type               | Description                                                                                                                                   |
|:------------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| event             | String             | Event<br/>`trade`/`error`                                                                                                                     |
| id                | String             | Request identifier                                                                                                                            |
| topic             | String             | Topic<br/>`place-order`                                                                                                                       |
| category          | String             | Category <br/>`spot`Spot<br/>`margin` Margin<br/> `usdt-futures` USDT futures<br/>`coin-futures` Coin futures<br/>`usdc-futures` USDC futures |
| args              | List&lt;Object&gt; | Channel list                                                                                                                                  |
| &gt; symbol       | String             | Symbol name                                                                                                                                   |
| &gt; orderId      | String             | Order ID                                                                                                                                      |
| &gt; clientOid    | String             | Client order ID                                                                                                                               |
| &gt; cTime        | String             | Order creation time <br/>Generated by OMS<br/>Unix millisecond timestamp                                                                                           |
| &gt; receiveTime  | String             | Gateway receive time <br/>Unix microsecond timestamp                                                                                          |
| &gt; pushTime     | String             | Gateway push time <br/>Unix microsecond timestamp                                                                                             |
| code              | String             | Code                                                                                                                                          |
| msg               | String             | Message                                                                                                                                       |
| connId            | String             | Connection ID                                                                                                                                 |
| rateLimit         | Array              | Rate limit balance array                                                                                                                      |
| &gt; limit        | String             | Rate limit quota for this dimension                                                                                                           |
| &gt; remaining    | String             | Remaining available quota                                                                                                                     |
| ts                | String             | Timestamp <br/>Generated by the gateway<br/>Unix millisecond timestamp                                                                                                                                     |

</div>

---

# 下单

### 描述

:::tip

ACK 仅表示请求被成功接受，请使用 [WebSocket order](/zh-CN/docs/uta/websocket/private/Order-Channel) 推送来确认订单的实际状态。

:::

该接口支持现货、杠杆、合约以及 Reality（rToken）股票下单，并可以自定义包括价格、数量和订单类型等参数

- Reality（rToken）限频，按 `venue` 区分<br/>
  `internal_market`（场内）：按 Crypto 限频规则，10次/秒/UID<br/>
  默认策略（不传 `venue`）及 `lit_market`（场外）：按 rToken 限频规则，默认 5次/秒/UID，白名单用户 30次/秒/UID（可联系 BD/RM 申请）。

- 合约交易<br/>
  合约单向持仓下只减仓订单，如果已经存在减仓单并且减仓单数量已经等于仓位数量，或者你新下的减仓单大于仓位剩余数量，会自动把之前减仓单取消，重新下新的减仓单，此时返回的信息
  orderId会为 null，建议一定要传clientOid
- 杠杆交易<br/>
  杠杆下单会自动借贷
- 订单检查
    - 合约：Price下单价格要满足价格乘数priceMultiplier的倍数，并且符合pricePrecision小数位。qty要满足大于minOrderAmount并且满足quantityMultiplier的倍数
    - 现货：price要满足小数位。qty下单数量必须要大于 minOrderAmount
- 开仓逻辑
    - 双向持仓
      开多： side=buy & posSide=long<br/>
      开空：side=sell & posSide=short<br/>
      平多：side=sell & posSide=long<br/>
      平空：side=buy & posSide=short<br/>
    - 单向持仓
      开多 side:buy<br/>
      开空 side:sell<br/>
      平多 side:sell reduceOnly:yes<br/>
      平空 side:buy reduceOnly:yes
- 订单持有上限:
    - 合约: USDT合约/币本位合约/USDC合约所有交易对加起来一共最多支持400个订单
    - 现货: 现货/杠杆所有交易对最多支持400订单
- ClientOid 校验规则: <br/>
  请确保您的 clientOid 满足正则表达式 `^[0-9A-Za-z_:#\\-+\\s]{1,32}$`
- 请求监控:将针对您的 API 请求进行统计监控，当单日 (UTC 0点 - UTC 24点)
  单账号（母账号和子账号整体运算）订单总数超过一定上限，平台将保留提醒、警告，以及进行必要性限制的权利。
  使用API的客户预设接收本条款并负有配合调整的义务。
- 下单出现错误 `{ "code":"40762", "msg":"The order size is greater than the max open size", "requestTime":1627293504612 }` <br/>两种原因
    - 账户余额不足
    -
    当前交易对当前杠杆仓位梯度已满，具体仓位梯度请参考 <a href='https://www.bitget.com/zh-CN/trade-info/position-gear?symbolId=BTCUSDT_UMCBL'>
    仓位档位说明</a>
- 注意：操作订单时出现以下错误，请用clientOid查询订单详情，以确认操作的最终结果<br/>

- **币本位合约说明**:<br/>
    - <u>新币本位业务线symbol格式为"XXXUSD_CM"，例如BTCUSD交易对在币本位合约的格式为BTCUSD_CM</u>
    - 新币本位暂时不支持修改订单，ADL，策略单，预设止盈止损

```json title="错误码示例"
{ "code": "40010", "msg": "Request timed out", "id": 1666268894074, "event":"error" }
{ "code": "40725", "msg": "service return an error", "id": 1666268894071, "event":"error" }
{ "code": "45001", "msg": "Unknown error", "id": 1666268894071, "event":"error" }
```

<div className="api-aligning">

```json title="请求示例"
{
  "op": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "requestTime": "1750034396082",
  "args": [
    {
      "orderType": "limit",
      "price": "100",
      "qty": "0.1",
      "side": "buy",
      "symbol": "BTCUSDT",
      "timeInForce": "gtc",
    }
  ]
}
```

### 请求参数

| 参数名               | 参数类型               | 是否必须 | 描述                                                                                                                                                                                                                                                     |
|:------------------|:-------------------|------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                | String             | 是    | 操作: <br/> `trade` 交易                                                                                                                                                                                                                                   |
| id                | String             | 是    | 请求标识                                                                                                                                                                                                                                                   |
| topic             | String             | 是    | 频道名: <br/> `place-order` 下单                                                                                                                                                                                                                            |
| category          | String             | 是    | 业务线（必须小写）<br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约                                                                                                                                     |
| apiCode           | String             | 否    | API返佣标识                                                                                                                                                                                                                                                |
| requestTime       | String             | 否    | 请求时间（客户端时间戳）<br/>用于与 `receiveWindow` 比对时间差值<br/>不传则 `receiveWindow` 参数无效 <br/>毫秒时间戳                                                                                                                                                                                   |
| args              | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                                                                                                                                                                              |
| &gt; symbol       | String             | 是    | 交易对名称                                                                                                                                                                                                                                                  |
| &gt; [orderType](/zh-CN/docs/uta/enum#ordertype)    | String             | 是    | 订单类型 <br/>`limit` : 限价<br/> `market` : 市价                                                                                                                                                                                                              |
| &gt; qty          | String             | 是    | 下单数量<br/> - 现货<br/> 市价买单，单位为quote coin<br/>限价及市价卖单，单位为base coin <br/> USDT/USDC合约： <br/> 单位为**base coin**  <br/> 币本位合约： <br/> 单位为 **<u>quote coin</u>**                                                                                                |
| &gt; price        | String             | 否    | 下单价格<br/>订单类型为限价单`limit`时，该字段必填<br/>订单类型为市价单`market`时，该字段失效                                                                                                                                                                                            |
| &gt; side         | String             | 是    | 下单方向<br/>`buy`: 买<br/>`sell`: 卖                                                                                                                                                                                                                        |
| &gt; posSide      | String             | 否    | 交易方向<br/>`long` 多仓<br/>`short` 空仓<br/>只限于合约传此参数 其他忽略<br/>用于合约双向持仓                                                                                                                                                                                      |
| &gt; timeInForce  | String             | 否    | [订单执行策略](https://www.bitget.com/zh-CN/support/articles/12560603818004) <br/> `gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤销 <br/> `post_only`: 只做maker <br/>[`rpi`](https://www.bitget.com/zh-CN/support/articles/12560603867770): 零售价格优化订单，为零售订单流提供价格优化的非显示限价单。仅限拥有RPI做市商权限的账户使用。<br/>订单类型为限价单`limit`时，默认值为`gtc`；<br/>订单类型为市价单`market`时，系统会按照`ioc`执行 <br/> 交易Reality 股票交易对（rtoken，如 rAAPLUSDT）时忽略该字段 |
| &gt; reduceOnly   | String             | 否    | 是否只减仓<br/>`YES`是<br/>`NO`否<br/>默认值为`NO`; 仅适用于买卖单向持仓模式下                                                                                                                                                                                                 |
| &gt; clientOid    | String             | 否    | 自定义订单ID<br/>需满足正则表达式 `^[0-9A-Za-z_:#\-+\s]{1,32}$`，即 1-32 个字符，可包含大小写字母、数字、下划线(_)、连字符(-)、加号(+)、冒号(:)、井号(#)和空格                                                                                                                                                                                                                                                |
| &gt; stpMode      | String             | 否    | [STP（自成交预防）模式](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br/>`none`：不比较双方用户ID，订单正常成交，不触发STP（默认值）<br/>`cancel_taker`：检测到自成交时，取消taker（吃单方）订单，maker（挂单方）订单保留在订单簿中 <br/>`cancel_maker`：检测到自成交时，取消maker（挂单方）订单，taker（吃单方）订单继续执行 <br/>`cancel_both`：检测到自成交时，taker和maker订单都取消<br/>STP判定以taker订单自身携带的`stpMode`为准，不看maker订单原有的`stpMode`设置                                                                                                                                  |
| &gt; tpTriggerBy  | String             | 否    | 预设止盈触发类型<br/>`market`市场价格<br/>`mark`标记价格<br/>如不填写，默认值为`market`市场价格<br/>该字段仅针对合约业务线`usdt-futures`，`coin-futures`及`usdc-futures`生效                                                                                                                       |
| &gt; slTriggerBy  | String             | 否    | 预设止损触发类型<br/>`market`市场价格<br/>`mark`标记价格<br/>如不填写，默认值为`market`市场价格<br/>该字段仅针对合约业务线`usdt-futures`，`coin-futures`及`usdc-futures`生效                                                                                                                       |
| &gt; takeprofit   | String             | 否    | 预设止盈触发价格                                                                                                                                                                                                                                               |
| &gt; stoploss     | String             | 否    | 预设止损触发价格                                                                                                                                                                                                                                               |
| &gt; tpOrderType  | String             | 否    | 止盈触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单<br/>Reality（rtoken）交易对暂时仅支持`market`市价单                                                                                                                                                                          |
| &gt; slOrderType  | String             | 否    | 止损触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单<br/>Reality（rtoken）交易对暂时仅支持`market`市价单                                                                                                                                                                          |
| &gt; tpLimitPrice | String             | 否    | 止盈策略单执行价格<br/>仅限价单`tpOrderType=limit`时有效，市价单忽略该参数                                                                                                                                                                                                      |
| &gt; slLimitPrice | String             | 否    | 止损策略单执行价格<br/>仅限价单`slOrderType=limit`时有效，市价单忽略该参数                                                                                                                                                                                                      |
| &gt; marginMode      | String             | 否    | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为全仓<br/>仅适用于合约                                                                                                                                                                                           |
| &gt; autoBorrow      | String             | 否    | 自动借币开关<br/>`yes` 开启<br/>`no` 关闭（默认）<br/>仅用于现货下单。开启后，若得到币不支持借贷、消耗币支持借贷，则在消耗币可用余额不足时，系统将自动借入消耗币，补足委托所需金额。 |
| &gt; pxAmendType     | String             | 否    | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |
| &gt; venue           | String             | 否    | 订单路由策略<br/>`internal_market` 订单在交易所内撮合，不提交美股券商<br/>`lit_market` 订单提交至美股券商执行，不在交易所内撮合<br/>如不传，为默认策略：优先交易所内部比价撮合，未成交部分提交至券商<br/>该参数仅针对 Reality（rtoken）交易对生效 |
| &gt; rTokenTimeInForce | String           | 否    | Reality（rtoken）订单执行策略<br/>`gtd` 当前时段有效。若在美股交易时间（周中）挂单，限价单有效期至美股盘后结束；若在周末挂单，有效期至美股下次开盘前<br/>`gtc` 订单有效期 90 天<br/>如不传，默认值为`gtd`<br/>该参数仅针对 Reality（rtoken）交易对生效 |
| &gt; bboLevel        | String             | 否    | BBO档位<br/>`queue1` 同向价1<br/>`queue5` 同向价5<br/>`counterparty1` 对手价1<br/>`counterparty5` 对手价5<br/>仅支持限价单设置，在市价单时无效 |
| &gt; slippageTolerance | String           | 否    | 滑点百分比<br/>默认值为 2%，范围是 [0.01, 0.05]，最多 2 位小数<br/>仅支持市价单设置<br/>滑点设置越高，成交的可能性越大，但成交价格可能与最新价格偏差较大。 |
| &gt; receiveWindow   | String             | 否    | 接收窗口有效期，单位毫秒，取值范围`[10, 60000]`<br/>若撮合引擎接收到订单的时间早于`requestTime + receiveWindow`，订单正常提交到订单簿；若超出该时间窗口，订单将被撤销，撤单原因`cancelReason`为`cancel_receiveWindow`<br/>注意：`receiveWindow` 仅在同时传入 `requestTime` 时生效                                                                                                                                    |

</div>


<div className="api-aligning">

```json title="响应示例"
{
  "event": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
      "cTime": "1750034397008",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    }
  ],
  "code": "0",
  "msg": "success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1750034397076"
}
```

### 响应参数说明

| 返回字段              | 参数类型               | 字段说明                                                                                                               |
|:------------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------|
| event             | String             | 事件<br/>`trade` 交易<br/>`error`参数错误                                                                                  |
| id                | String             | 请求标识                                                                                                               |
| topic             | String             | 频道名<br/>`place-order`下单                                                                                            |
| category          | String             | 业务线 <br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| args              | List&lt;Object&gt; | 订单列表                                                                                                               |
| &gt; symbol       | String             | 交易对名称，如`BTCUSDT`                                                                                                   |
| &gt; orderId      | String             | 订单ID                                                                                                               |
| &gt; clientOid    | String             | 自定义订单ID                                                                                                            |
| &gt; cTime        | String             | 订单创建时间 <br/>生成于OMS<br/>Unix毫秒时间戳                                                                                              |
| &gt; receiveTime  | String             | 网关接收时间 <br/>Unix微秒时间戳                                                                                             |
| &gt; pushTime     | String             | 网关推送时间 <br/>Unix微秒时间戳                                                                                             |
| code              | String             | 状态码                                                                                                                |
| msg               | String             | 状态消息                                                                                                               |
| connId            | String             | 连接ID                                                                                                               |
| rateLimit         | Array              | 限频余额数组                                                                                                             |
| &gt; limit        | String             | 该维度限额                                                                                                              |
| &gt; remaining    | String             | 剩余可用次数                                                                                                             |
| ts                | String             | 时间戳 <br/>生成于网关<br/>Unix毫秒时间戳                                                                                                               |

</div>