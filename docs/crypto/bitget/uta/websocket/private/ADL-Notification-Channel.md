---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/ADL-Notification-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:03:27.162796
---

# ADL Notification Channel

### Description

[ADL (Auto-Deleveraging)](https://www.bitget.com/support/articles/12560603800805) is a risk management mechanism that
automatically reduces a trader's position when their margin balance falls below the maintenance margin requirement. This
channel pushes real-time notifications when an ADL event is triggered for a position under the unified trading account.

- Subscribe to `adl-notification` to receive push notifications when your position enters the ADL queue or is being
  auto-deleveraged.
- The push data includes the symbol, position side, execution price, and execution amount of the affected position.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "adl-notification"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                                     | 
|:--------------|:-------------------|:---------|:------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe`/`unsubscribe`       |
| args          | List&lt;Object&gt; | Yes      | Subscribed channels                             |
| &gt; instType | String             | Yes      | Product type<br/>`UTA` Unified trading account  |
| &gt; topic    | String             | Yes      | Topic <br/> `adl-notification` ADL Notification |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "adl-notification"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                          | 
|:--------------|:-------|:-----------------------------------------------------|
| event         | String | Operation <br/>`subscribe` / `unsubscribe` / `error` |
| arg           | Object | Subscribed channel                                   |
| &gt; instType | String | Product type <br/>`UTA`                              |
| &gt; topic    | String | Topic <br/>`adl-notification` ADL Notification       |
| code          | String | Error code                                           |
| msg           | String | Error message                                        |
| connId        | String | Connection ID                                        |

</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "side": "buy",
      "status": "triggered",
      "price": "88291.2",
      "amount": "2.35",
      "ts": "1740546523244"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "adl-notification"
  },
  "action": "update",
  "ts": 1740546523244
}
```

### Push Parameters

| Parameters    | Type               | Description                                                     |
|:--------------|:-------------------|:----------------------------------------------------------------|
| arg           | Object             | Subscribed channel                                              |
| ts            | String             | Push timestamp<br/>Unix millisecond timestamp                     |
| &gt; instType | String             | product type <br/>`UTA` Unified trading account                 |
| &gt; topic    | String             | Topic <br/>`adl-notification` ADL Notification                  |
| action        | String             | Action: <br/>`update` Incremental data                          |
| data          | List&lt;Object&gt; | Subscribed data                                                 |
| &gt;symbol    | String             | Symbol name                                                     |
| &gt;[side](/docs/uta/enum#side)      | String             | Position side <br/>`buy` Buy<br/>`sell` Sell                      |
| &gt;status    | String             | ADL status <br/>`triggered` Triggered; the ADL has been activated and the position is being reduced                            |
| &gt;price     | String             | ADL execution price                                             |
| &gt;amount    | String             | ADL execution amount<br/>Unit: base coin. For example, `2.35` means 2.35 base coins of the affected position were reduced                                           |
| &gt;ts        | String             | ADL start time (Unix millisecond timestamp)                     |

</div>

---

# ADL通知

### 描述

[ADL（自动减仓）](https://www.bitget.com/zh-CN/support/articles/12560603800805)
是一种风险管理机制，当交易者的保证金余额低于维持保证金要求时，系统会自动减少其仓位以降低风险。本频道实时推送统一账户仓位触发
ADL 事件的通知。

- 订阅 `adl-notification` 后，当您的仓位进入 ADL 队列或被自动减仓时，会收到推送通知。
- 推送数据包含受影响的交易对、持仓方向、执行价格和执行数量。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "adl-notification"
        }
    ]
}
```

### 请求参数说明

| 参数名           | 参数类型               | 是否必须 | 描述                                              | 
|:--------------|:-------------------|:-----|:------------------------------------------------|
| op            | String             | 是    | 操作 <br/> `subscribe` 订阅 <br/>`unsubscribe` 取消订阅 |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                       |
| &gt; instType | String             | 是    | 产品类型<br/>`UTA` 统一账户                             |
| &gt; topic    | String             | 是    | 频道名  `adl-notification` ADL通知                   |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "adl-notification"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数说明

| 返回字段          | 参数类型   | 字段说明                                                             | 
|:--------------|:-------|:-----------------------------------------------------------------|
| event         | String | 操作  <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误 |
| arg           | Object | 订阅的频道                                                            |
| &gt; instType | String | 产品类型<br/>`UTA` 统一账户                                              |
| &gt; topic    | String | 频道名 <br/>`adl-notification` ADL通知                                |
| code          | String | 错误码                                                              |
| msg           | String | 错误消息                                                             |
| connId        | String | 连接ID                                                             |

</div>


<div className="api-br-10"></div>


<div className="api-aligning">

```json title="推送示例"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "side": "buy",
      "status": "triggered",
      "price": "88291.2",
      "amount": "2.35",
      "ts": "1740546523244"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "adl-notification"
  },
  "action": "update",
  "ts": 1740546523244
}
```

### 推送参数说明

| 属性名           | 类型                 | 描述                                        |
|---------------|--------------------|-------------------------------------------|
| arg           | Object             | 订阅成功频道                                    |
| ts            | String             | 时间戳                                       |
| &gt; instType | String             | 产品线类型<br/>`UTA`统一账户                       |
| &gt; topic    | String             | 频道名<br/>`adl-notification` ADL通知          |
| action        | String             | 推送数据动作 <br/> `update` 增量                  |
| data          | List&lt;Object&gt; | 订阅的数据                                     |
| &gt;symbol    | String             | 交易对名称                                     |
| &gt;[side](/zh-CN/docs/uta/enum#side)      | String             | 仓位方向<br/>`buy` 买<br/>`sell`卖               |
| &gt;status    | String             | ADL状态<br/>`triggered` 已触发，ADL 已被激活，仓位正在被自动减仓                  |
| &gt;price     | String             | ADL执行价格                                   |
| &gt;amount    | String             | ADL执行数量<br/>单位：基础币。例如 `2.35` 表示该仓位被减仓了 2.35 个基础币                     |
| &gt;ts        | String             | ADL开始时间<br/>Unix毫秒时间戳                     |

</div>