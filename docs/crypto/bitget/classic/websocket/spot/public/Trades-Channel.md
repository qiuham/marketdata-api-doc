---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/public/Trades-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:01:38.685230
---

# Trading Channel

### Description

Push once if any trade is matched(taker orders)

Real-time Push

:::info{title="Push logic adjustment"}
Effective in **demo trading** on November 4, 2026, and expected in **live trading** on November 17, 2026: after a successful subscription, this channel will no longer push snapshot data (`action`=`snapshot`); only real-time incremental data (`action`=`update`) will be pushed. Before the adjustment takes effect, the first push after subscription is a snapshot of recent data. To obtain historical data, please use the corresponding REST API.
:::

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "trade",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description                      | 
| :---- | :---- | :---- |:---------------------------------|
| op | String | Yes | Operation, subscribe unsubscribe |
| args | List&lt;Object&gt; | Yes | List of channels to subscribe to |
| &gt; instType | String | Yes | Product Line Type, `SPOT`        |
| &gt; channel | String | Yes | Channel name, `trade`            |
| &gt; instId | String | Yes | Product id For example: ETHUSDT  |

</div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "trade",
        "instId": "BTCUSDT"
    }
}
```
### Response Parameters

| Parameter | Type | Description                              | 
| :---- | :---- |:-----------------------------------------|
| event | String | Event, `subscribe` `unsubscribe` `error` |
| arg | Object | The channel subscribe to                 |
| &gt; instType | String | product type, `SPOT`                     |
| &gt; channel | String | Channel name, `trade`                    |
| &gt; instId | String | Product id. For example: ETHUSDT         |
| code | String | Error code, returned only on error       |
| msg | String | Error message                            |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "update",
    "arg": {
        "instType": "SPOT",
        "channel": "trade",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "ts": "1695709835822",
            "price": "26293.4",
            "size": "0.0013",
            "side": "buy",
            "tradeId": "1000000000"
        }
    ],
    "ts": 1695711090682
}
```

### Push Parameters

| Parameter | Type | Description                                                                   | 
| :---- | :---- |:------------------------------------------------------------------------------|
| arg | Object | Successfully subscribed channel                                               |
| &gt; instType | String | Product Type, `SPOT`                                                          |
| &gt; channel | String | Channel name, `trade`                                                         |
| &gt; instId | String | Product id For example: ETHUSDT                                               |
| action | String | Push data action, `snapshot` or `update`<br/>After the push logic adjustment takes effect, only `update` is pushed                                      |
| data | List&lt;Object&gt; | Subscribed data                                                               |
| &gt; tradeId | String | Transaction ID                                                                |
| &gt; ts | String | Transaction time, millisecond format of Unix timestamp, such as 1597026383085 |
| &gt; price | String | Transaction price                                                             |
| &gt; size | String | Transaction quantity                                                          |
| &gt; side | String | Transaction direction                                                         |

</div>

---

# 交易频道

### 描述

获取最近的成交数据(taker订单)，有成交数据就推送，实时推送

:::info{title="推送逻辑调整"}
模拟盘自 2026 年 11 月 4 日起生效，实盘预计 2026 年 11 月 17 日生效：订阅成功后，本频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）。调整生效前，订阅后首次推送为最近数据的快照。如需获取历史数据，请使用对应的 REST 接口。
:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "trade",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                       | 
| :---- | :---- | :---- |:-------------------------|
| op | String | 是 | 操作，subscribe unsubscribe |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                |
| &gt; instType | String | 是 | 产品线类型, `SPOT`            |
| &gt; channel | String | 是 | 频道名,`trade`              |
| &gt; instId | String | 是 | 产品id 例如：ETHUSDT          |

</div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "trade",
        "instId": "BTCUSDT"
    }
}
```
### 返回参数

| 返回字段 | 参数类型 | 字段说明                                 | 
| :---- | :---- |:-------------------------------------|
| event | String | 事件，`subscribe` `unsubscribe` `error` |
| arg | Object | 订阅的频道                                |
| &gt; instType | String | 产品类型, `SPOT`                         |
| &gt; channel | String | 频道名, `trade`                         |
| &gt; instId | String | 是<br/>产品id 例如：ETHUSDT                |
| code | String | 错误码，错误时才会返回                          |
| msg | String | 错误消息                                 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "update",
    "arg": {
        "instType": "SPOT",
        "channel": "trade",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "ts": "1695709835822",
            "price": "26293.4",
            "size": "0.0013",
            "side": "buy",
            "tradeId": "1000000000"
        }
    ],
    "ts": 1695711090682
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明                               | 
| :---- | :---- |:-----------------------------------|
| arg | Object | 订阅成功的频道                            |  
| &gt; instType | String | 产品类型, `SPOT`                       |  
| &gt; channel | String | 频道名,`trade`                        |  
| &gt; instId | String | 产品id 例如：ETHUSDT                    |  
| action | String | 推送数据动作, `snapshot` or `update`<br/>推送逻辑调整生效后，仅推送 `update`     |  
| data | List&lt;Object&gt; | 订阅的数据                              |  
| &gt; tradeId | String | 成交ID                               |  
| &gt; ts | String | 成交时间，Unix时间戳的毫秒数格式，如 1597026383085 |  
| &gt; price | String | 成交价格                               |  
| &gt; size | String | 成交数量                               |  
| &gt; side | String | 成交方向                               |  

</div>