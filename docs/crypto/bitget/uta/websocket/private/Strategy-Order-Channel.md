---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Strategy-Order-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:02:12.043195
---

# Strategy Order Channel

### Description

The following events will trigger a data push:

1. No push on first-time subscription
2. Push when a strategy order is placed in the unified trading account
3. Push when a strategy order status changes in the unified trading account
4. Push when a strategy order is cancelled in the unified trading account

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "strategy-order",
            "symbol": "default"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                                                         |
|:--------------|:-------------------|:---------|:--------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` / `unsubscribe`                         |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel list                                             |
| &gt; instType | String             | Yes      | Product type <br/> `UTA` Unified trading account                    |
| &gt; topic    | String             | Yes      | Topic <br/>`strategy-order` Strategy order                          |
| &gt; symbol   | String             | No       | Symbol name<br/>Currently only `default` is supported (all symbols) |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "strategy-order",
    "symbol": "default"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                     |
|:--------------|:-------|:--------------------------------------------------------------------------------|
| event         | String | Event <br/>`subscribe` / `unsubscribe` / `error`                                |
| arg           | Object | Subscribed channel                                                              |
| &gt; instType | String | Product type <br/> `UTA` Unified trading account                                |
| &gt; topic    | String | Topic <br/>`strategy-order` Strategy order                                      |
| code          | String | Error code                                                                      |
| msg           | String | Error message                                                                   |
| connId        | String | Connection ID                                                                   |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "action": "snapshot",
  "arg": {
    "instType": "UTA",
    "topic": "strategy-order",
    "symbol": "default"
  },
  "data": [
    {
      "category": "usdt-futures",
      "symbol": "BTCUSDT",
      "orderId": "111111111111111111",
      "clientOid": "myorder001",
      "qty": "0.01",
      "side": "buy",
      "posSide": "long",
      "reduceOnly": "no",
      "type": "tpsl",
      "status": "pending",
      "triggerType": "takeProfit",
      "tpTriggerBy": "market",
      "slTriggerBy": "market",
      "takeProfit": "110000",
      "stopLoss": "90000",
      "tpOrderType": "market",
      "slOrderType": "market",
      "tpLimitPrice": "",
      "slLimitPrice": "",
      "triggerBy": "market",
      "triggerPrice": "100000",
      "triggerOrderType": "limit",
      "triggerOrderPrice": "100500",
      "createdTime": "1730186725663",
      "updatedTime": "1730186725691"
    }
  ],
  "ts": 1730186725700
}
```

### Push Parameters

| Return Field          | Parameter Type     | Description                                                                                                            |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------|
| arg                   | Object             | Subscribed channel                                                                                                     |
| &gt; instType         | String             | Product type <br/> `UTA` Unified trading account                                                                       |
| &gt; topic            | String             | Topic <br/>`strategy-order` Strategy order                                                                             |
| action                | String             | Push data action <br/>`snapshot` Full data                                                                             |
| ts                    | String             | Push timestamp (milliseconds)                                                                                          |
| data                  | List&lt;Object&gt; | Push data                                                                                                              |
| &gt; category         | String             | Product type <br/>`spot` Spot <br/>`margin` Margin <br/>`usdt-futures` USDT futures <br/>`coin-futures` Coin-M futures <br/>`usdc-futures` USDC futures      |
| &gt; symbol           | String             | Symbol name                                                                                                            |
| &gt; orderId          | String             | Strategy order ID                                                                                                      |
| &gt; clientOid        | String             | Client strategy order ID                                                                                               |
| &gt; qty              | String             | Order quantity                                                                                                         |
| &gt; side             | String             | Trade side <br/>`buy` / `sell`                                                                                         |
| &gt; posSide          | String             | Position side <br/>`long` / `short`                                                                                    |
| &gt; reduceOnly       | String             | Whether it is reduce-only                                                                                              |
| &gt; type             | String             | Strategy type <br/>`tpsl` Take-Profit and Stop-Loss <br/>`trigger` Trigger Order                                       |
| &gt; status           | String             | Strategy order status <br/>`pending` Waiting to be executed <br/>`success` Executed <br/>`failed` Execution failed <br/>`cancelled` Cancelled <br/>`submitting` Submitting |
| &gt; triggerType      | String             | Trigger type <br/>`takeProfit` Take-Profit <br/>`stopLoss` Stop-Loss                                                   |
| &gt; tpTriggerBy      | String             | Take-Profit trigger price type <br/>`market`: Market Price <br/>`mark`: Mark Price                                     |
| &gt; slTriggerBy      | String             | Stop-Loss trigger price type <br/>`market`: Market Price <br/>`mark`: Mark Price                                       |
| &gt; takeProfit       | String             | Take-Profit trigger price                                                                                              |
| &gt; stopLoss         | String             | Stop-Loss trigger price                                                                                                |
| &gt; tpOrderType      | String             | Take-Profit trigger strategy order type <br/>`limit`: Limit Order <br/>`market`: Market Order                          |
| &gt; slOrderType      | String             | Stop-Loss trigger strategy order type <br/>`limit`: Limit Order <br/>`market`: Market Order                            |
| &gt; tpLimitPrice     | String             | Take-Profit strategy order execution price                                                                             |
| &gt; slLimitPrice     | String             | Stop-Loss strategy order execution price                                                                               |
| &gt; triggerBy        | String             | Trigger order trigger price type <br/>`market`: Market Price <br/>`mark`: Mark Price                                   |
| &gt; triggerPrice     | String             | Trigger order trigger price                                                                                            |
| &gt; triggerOrderType | String             | Trigger order type <br/>`limit`: Limit Order <br/>`market`: Market Order                                               |
| &gt; triggerOrderPrice | String            | Trigger order execution price                                                                                          |
| &gt; createdTime      | String             | Order created timestamp (Unix milliseconds)                                                                            |
| &gt; updatedTime      | String             | Order update timestamp (Unix milliseconds)                                                                             |

</div>

---

# 策略订单频道

### 描述

以下事件发生时推送数据：

1. 首次订阅，不推送
2. 统一账户策略单下单，推送
3. 统一账户策略单状态变化，推送
4. 统一账户策略单撤单，推送

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "strategy-order",
            "symbol": "default"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                               |
|:--------------|:-------------------|:-----|:-------------------------------------------------|
| op            | String             | 是    | 操作 <br/> `subscribe` 订阅 <br/>`unsubscribe` 取消订阅  |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                        |
| &gt; instType | String             | 是    | 产品类型<br/>`UTA` 统一账户                              |
| &gt; topic    | String             | 是    | 频道名 <br/>`strategy-order` 策略订单                   |
| &gt; symbol   | String             | 否    | 交易对名称<br/>当前只支持 `default`，全部交易对信息推送              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="响应示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "strategy-order",
    "symbol": "default"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数说明

| 返回字段          | 参数类型   | 字段说明                                                                            |
|:--------------|:-------|:--------------------------------------------------------------------------------|
| event         | String | 操作 <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订 <br/>`error` 参数错误                 |
| arg           | Object | 订阅的频道                                                                           |
| &gt; instType | String | 产品类型<br/>`UTA` 统一账户                                                             |
| &gt; topic    | String | 频道名 <br/>`strategy-order` 策略订单                                                  |
| code          | String | 错误码                                                                             |
| msg           | String | 错误消息                                                                            |
| connId        | String | 连接ID                                                                            |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="推送数据"
{
  "action": "snapshot",
  "arg": {
    "instType": "UTA",
    "topic": "strategy-order",
    "symbol": "default"
  },
  "data": [
    {
      "category": "usdt-futures",
      "symbol": "BTCUSDT",
      "orderId": "111111111111111111",
      "clientOid": "myorder001",
      "qty": "0.01",
      "side": "buy",
      "posSide": "long",
      "reduceOnly": "no",
      "type": "tpsl",
      "status": "pending",
      "triggerType": "takeProfit",
      "tpTriggerBy": "market",
      "slTriggerBy": "market",
      "takeProfit": "110000",
      "stopLoss": "90000",
      "tpOrderType": "market",
      "slOrderType": "market",
      "tpLimitPrice": "",
      "slLimitPrice": "",
      "triggerBy": "market",
      "triggerPrice": "100000",
      "triggerOrderType": "limit",
      "triggerOrderPrice": "100500",
      "createdTime": "1730186725663",
      "updatedTime": "1730186725691"
    }
  ],
  "ts": 1730186725700
}
```

### 推送参数

| 返回字段                      | 参数类型               | 字段说明                                                                                                   |
|:--------------------------|:-------------------|:-------------------------------------------------------------------------------------------------------|
| arg                       | Object             | 订阅成功频道                                                                                                 |
| &gt; instType             | String             | 产品类型<br/>`UTA` 统一账户                                                                                    |
| &gt; topic                | String             | 频道名 <br/>`strategy-order` 策略订单                                                                         |
| action                    | String             | 推送数据动作 <br/>`snapshot` 全量                                                                              |
| ts                        | String             | 推送时间戳（毫秒）                                                                                              |
| data                      | List&lt;Object&gt; | 订阅数据                                                                                                   |
| &gt; category             | String             | 业务线<br/>`spot` 现货<br/>`margin` 杠杆<br/>`usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约                        |
| &gt; symbol               | String             | 币对名称                                                                                                   |
| &gt; orderId              | String             | 策略订单号                                                                                                  |
| &gt; clientOid            | String             | 自定义策略订单号                                                                                               |
| &gt; qty                  | String             | 委托数量                                                                                                   |
| &gt; side                 | String             | 交易方向<br/>`buy` 买<br/>`sell` 卖                                                                          |
| &gt; posSide              | String             | 仓位方向<br/>`long` 多仓<br/>`short` 空仓                                                                      |
| &gt; reduceOnly           | String             | 是否只减仓                                                                                                  |
| &gt; type                 | String             | 策略类型<br/>`tpsl` 止盈止损<br/>`trigger` 计划委托                                                               |
| &gt; status               | String             | 策略订单状态<br/>`pending` 等待执行<br/>`success` 已执行<br/>`failed` 执行失败<br/>`cancelled` 已撤销<br/>`submitting` 下单中 |
| &gt; triggerType          | String             | 触发类型<br/>`takeProfit` 止盈<br/>`stopLoss` 止损                                                             |
| &gt; tpTriggerBy          | String             | 止盈触发类型<br/>`market` 市场价格<br/>`mark` 标记价格                                                              |
| &gt; slTriggerBy          | String             | 止损触发类型<br/>`market` 市场价格<br/>`mark` 标记价格                                                              |
| &gt; takeProfit           | String             | 止盈触发价格                                                                                                 |
| &gt; stopLoss             | String             | 止损触发价格                                                                                                 |
| &gt; tpOrderType          | String             | 止盈触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单                                                           |
| &gt; slOrderType          | String             | 止损触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单                                                           |
| &gt; tpLimitPrice         | String             | 止盈策略单执行价格                                                                                              |
| &gt; slLimitPrice         | String             | 止损策略单执行价格                                                                                              |
| &gt; triggerBy            | String             | 计划委托触发价格类型<br/>`market` 市场价格<br/>`mark` 标记价格                                                          |
| &gt; triggerPrice         | String             | 计划委托触发价格                                                                                               |
| &gt; triggerOrderType     | String             | 计划委托订单类型<br/>`limit` 限价单<br/>`market` 市价单                                                             |
| &gt; triggerOrderPrice    | String             | 计划委托执行价格                                                                                               |
| &gt; createdTime          | String             | 订单创建时间（Unix毫秒时间戳）                                                                                      |
| &gt; updatedTime          | String             | 订单更新时间（Unix毫秒时间戳）                                                                                      |

</div>