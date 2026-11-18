---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Fast-Fill-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:46.211348
---

# Fast Fill Channel

### Description

This channel only pushes order fill data for users in UTA mode.<br/>
This channel does not currently push strategy and copy trading fill data.

For Reality (rtoken) orders, this channel now pushes fills executed both onshore (internal) and offshore (external). Previously, only onshore fills were pushed.

Push rules:
1. No push on first-time subscription
2. Push when spot/leveraged/futures orders are filled in the unified trading account

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "fast-fill",
            "symbol": "default"
        }
    ]
}
```

### Request Parameters


| Parameters    |  Type         | Required | Description                                    |
|:--------------|:-----------------------|:---------|:-----------------------------------------------|
| op            | String                 | Yes      | Operation: <br/> `subscribe` /`unsubscribe`    |
| args          | List&lt;Object&gt;     | Yes      | Subscribed channel list                        |
| &gt; instType | String                 | Yes      | Product type<br/>`UTA` Unified trading account |
| &gt; topic    | String                 | Yes      | Topic <br/>`fast-fill` Fast fill               |
| &gt; symbol   | String                 | No       | Symbol name<br/>`default` All symbols          |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "UTA",
        "topic": "fast-fill"
    },
    "connId": "xxxxxxxxxx"
}
```
### Response Parameters

| Parameters    |  Type   | Description                                            | 
|:-----------------|:-----------------|:-------------------------------------------------------|
| event            | String           | Operation <br/>`subscribe` / `unsubscribe` / `error`   |
| arg              | Object           | Subscribed channel                                     |
| &gt; instType    | String           | Product type <br/>`UTA` Unified trading account        |
| &gt; topic       | String           | Topic <br/>`fast-fill` Fast fill                       |
| code             | String           | Error code                                             |
| msg              | String           | Error message                                          |
| connId           | String           | Connection ID                                          |


</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data":
    {
      "symbol": "BTCUSDT",
      "updatedTime": "1736378720623",
      "side": "buy",
      "orderId": "1288888888888888888",
      "execTime": "1736378720623",
      "tradeScope": "taker",
      "execId": "1288888888888888888",
      "execPrice": "94993",
      "holdSide": "long",
      "category": "usdt-futures",
      "execQty": "0.01",
      "clientOid": "1288888888888888889",
      "execVenue": ""
    },
  "arg": {
    "instType": "UTA",
    "topic": "fast-fill"
  },
  "action": "update",
  "ts": 1736378720653
}
```


### Push Parameters

| Parameters         | Type   | Description                                                                                                                                                                   | Remarks |
|:-------------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
| arg                | Object | Subscribed channel                                                                                                                                                            |         |
| &gt; instType      | String | Product type <br/>`UTA` Unified trading account                                                                                                                               |         |
| &gt; topic         | String | Topic <br/>`fast-fill` Fast fill                                                                                                                                              |         |
| action             | String | Push data action<br/>`update` Incremental                                                                                                                                     |         |
| data               | Object  | Subscribed data                                                                                                                                                               |         |
| &gt; category      | String | Business line <br/> `spot` Spot trading <br/> `margin` Margin trading <br/> `usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |         |
| &gt; orderId       | String | Order ID                                                                                                                                                                      |         |
| &gt; clientOid     | String | Client Order ID                                                                                                                                                               |         |
| &gt; symbol        | String | Symbol name                                                                                                                                                                   |         |
| &gt; execId        | String | Fill ID                                                                                                                                                                       |         |
| &gt; side          | String | Trade side<br/>`buy` Buy<br/>`sell` Sell                                                                                                                                      |         |
| &gt; holdSide      | String | Position direction <br/>`long` Long <br/>`short` Short                                                                                                                        |         |
| &gt; execPrice     | String | Fill price                                                                                                                                                                    |         |
| &gt; execQty       | String | Fill quantity                                                                                                                                                                 |         |
| &gt; tradeScope    | String | Trade scope<br/>`taker` Taker<br/>`maker` Maker                                                                                                                               |         |
| &gt; execVenue     | String | Execution venue identifier<br/>`internal_market` Internal fill: matched in the internal order book<br/>`lit_market` Lit market fill: routed to an external broker and executed on the public market<br/>Only returned for Reality (rToken) fills; empty string for fills of other business lines<br/>Note: `execVenue` is where the fill actually took place, which differs from the `venue` order parameter |         |
| &gt; execTime      | String | Execution timestamp <br/>A Unix timestamp in milliseconds. e.g.,`1622697148123`                                                                                               |         |
| &gt; updatedTime   | String | Updated timestamp<br/>A Unix timestamp in milliseconds. e.g.,`1622697148123`                                                                                                  |         |


</div>

---

# 快速成交

### 描述

本频道仅推送用户UTA模式下的订单成交数据，暂不推送策略及跟单成交数据

针对 Reality（rtoken）订单，本频道现已推送场内（内部）与场外（外部）成交数据，此前仅推送场内成交数据。

推送规则：
1. 首次订阅，不推送
2. 统一账户现货/杠杆/合约委托单成交，推送

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "fast-fill",
            "symbol": "default"
        }
    ]
}
```

### 请求参数说明

| 参数名           | 参数类型               | 是否必须 | 描述                                                                 | 
|:--------------|:-------------------|------|:-------------------------------------------------------------------|
| op            | String             | 是    | 操作: <br/> `subscribe` 订阅 <br/>`unsubscribe` 退订                   |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                          |
| &gt; instType | String             | 是    | 产品线类型<br/>`UTA` 统一账户                                              |
| &gt; topic    | String             | 是    | 频道名<br/>`fast-fill` 快速成交                                          |
| &gt; symbol   | String             | 否    | 交易对名称<br/>`default` 全部交易对                                         |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅响应示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "UTA",
        "topic": "fast-fill"
    },
    "connId": "xxxxxxxxxx"
}
```
### 返回参数说明

| 返回字段          | 参数类型     | 字段说明                                                            | 
|:--------------|:---------|:----------------------------------------------------------------|
| event         | String   | 操作 <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误 |
| arg           | Object   | 订阅的频道                                                           |
| &gt; instType | String   | 产品线类型<br/>`UTA` 统一账户                                           |
| &gt; topic    | String   | 频道名 <br/>`fast-fill` 快速成交                                      |
| code          | String   | 错误码                                                             |
| msg           | String   | 错误消息                                                            |
| connId        | String   | 连接ID                                                            |


</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="推送示例"
{
  "data": 
    {
      "symbol": "BTCUSDT",
      "updatedTime": "1736378720623",
      "side": "buy",
      "orderId": "1288888888888888888",
      "execTime": "1736378720623",
      "tradeScope": "taker",
      "execId": "1288888888888888888",
      "execPrice": "94993",
      "holdSide": "long",
      "category": "usdt-futures",
      "execQty": "0.01",
      "clientOid": "1288888888888888889",
      "execVenue": ""
    },
  "arg": {
    "instType": "UTA",
    "topic": "fast-fill"
  },
  "action": "update",
  "ts": 1736378720653
}
```


### 推送参数说明

| 属性名               | 类型     | 描述                                                                                                              | 备注 |
|:------------------|:-------|:----------------------------------------------------------------------------------------------------------------|:---|
| arg               | Object | 订阅成功频道                                                                                                          |    |
| &gt; instType     | String | 产品线类型<br/>`UTA`统一账户                                                                                             |    |
| &gt; topic        | String | 频道名<br/>`fast-fill`快速成交                                                                                         |    |
| action            | String | 推送数据动作<br/>`update`增量                                                                                           |    |
| data              | Object  | 订阅的数据                                                                                                           |    |
| &gt; category     | String | 业务线 <br/>`spot`现货<br/>`margin` 杠杆<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约 <br/>`usdc-futures` USDC合约 |    |
| &gt; orderId      | String | 订单ID                                                                                                            |    |
| &gt; clientOid    | String | 自定义订单ID                                                                                                         |    |
| &gt; symbol       | String | 交易对名称                                                                                                           |    |
| &gt; execId       | String | 成交ID                                                                                                            |    |
| &gt; side         | String | 委托方向 <br/>`buy` 买<br/>`sell` 卖                                                                                  |    |
| &gt; holdSide     | String | 持仓方向 <br/>`long` 多 <br/> `short` 空                                                                              |    |
| &gt; execPrice    | String | 成交价格                                                                                                            |    |
| &gt; execQty      | String | 成交数量                                                                                                            |    |
| &gt; tradeScope   | String | 交易者标识<br/>`taker` 吃单方<br/>`maker` 挂单方                                                                           |    |
| &gt; execVenue    | String | 成交发生地标识<br/>`internal_market` 内部成交：在内部订单簿成交<br/>`lit_market` 公开市场成交：路由到外部券商，在公开市场成交<br/>仅 Reality（rToken）交易对的成交返回该字段，其他业务线成交该字段为空字符串<br/>注：`execVenue` 为实际成交地，不同于下单参数 `venue` |    |
| &gt; execTime     | String | 成交时间<br/>Unix毫秒时间戳，例如1622697148123                                                                              |    |
| &gt; updatedTime  | String | 更新时间<br/>Unix毫秒时间戳，例如1622697148123                                                                              |    |


</div>