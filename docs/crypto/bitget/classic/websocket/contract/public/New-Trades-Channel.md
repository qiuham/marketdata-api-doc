---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/public/New-Trades-Channel
api_type: WebSocket
updated_at: 2026-11-27 19:01:35.573299
---

# Public Trade Channel

### Description

Get the public trade data(taker orders)

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
            "instType": "USDT-FUTURES",
            "channel": "trade",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                                                                         | 
| :---- | :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| op | String | Yes | Operation, subscribe unsubscribe                                                                                    |
| args | List&lt;Object&gt; | Yes | op list                                                                                                             |
| &gt; instType | String | Yes | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; channel | String | Yes | Channel, `trade`                                                                                                    |
| &gt; instId | String | Yes | Product ID<br/>e.g: ETHUSDT                                                                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "trade",
        "instId": "BTCUSDT"
    }
}
```

### Response Parameters

| Parameter | Type | Description                                                                                                         | 
| :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| event | String | event                                                                                                               |
| arg | Object | arg list                                                                                                            |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; channel | String | Channel, `trade`                                                                                                    |
| &gt; instId | String | Symbol name<br/>e.g: ETHUSDT                                                                                        |
| code | String | Error code                                                                                                          |
| msg | String | Error message                                                                                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "update",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "trade",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "ts": "1695716760565",
            "price": "27000.5",
            "size": "0.001",
            "side": "buy",
            "tradeId": "1111111111"
        },
        {
            "ts": "1695716759514",
            "price": "27000.0",
            "size": "0.001",
            "side": "sell",
            "tradeId": "1111111111"
        }
    ],
    "ts": 1695716761589
}
```

### Push Parameters

| Parameter       | Type               | Description                                                                                                                      | 
|:----------------|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| action          | String             | Push data action, `snapshot` or `update`<br/>After the push logic adjustment takes effect, only `update` is pushed                                                                                                                           |
| arg             | Object             | arg                                                                                                                              |
| &gt; instType   | String             | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures               |
| &gt; channel    | String             | Channel, `trade`                                                                                                                 |
| &gt; instId     | String             | Symbol: ETHUSDT                                                                                                                  |
| data            | List&lt;Object&gt; | Data                                                                                                                             |
| &gt; ts         | String             | Fill time: 1597026383085                                                                                                         |
| &gt; price      | String             | Filled price                                                                                                                     |
| &gt; size       | String             | Filled amount                                                                                                                    |
| &gt; side       | String             | Filled side, sell/buy                                                                                                            |
| &gt; tradeId    | String             | tradeId                                                                                                                          |
| ts              | String             | Data streaming time                                                                                                              |

<div className="api-br-10"></div>

</div>

---

# 平台成交详情频道

### 描述

平台成交频道(taker订单)

实时推送

:::info{title="推送逻辑调整"}
模拟盘自 2026 年 11 月 4 日起生效，实盘预计 2026 年 11 月 17 日生效：订阅成功后，本频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）。调整生效前，订阅后首次推送为最近数据的快照。如需获取历史数据，请使用对应的 REST 接口。
:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "trade",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                                                                | 
| :---- | :---- | :---- |:----------------------------------------------------------------------------------|
| op | String | 是 | 操作, subscribe unsubscribe                                                         |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                                                         |
| &gt; instType | String | 是 | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; channel | String | 是 | 频道名                                                                               |
| &gt; instId | String | 是 | 产品ID<br/>如：ETHUSDT                                                                |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "trade",
        "instId": "BTCUSDT"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明                                                                              | 
| :---- | :---- |:----------------------------------------------------------------------------------|
| event | String | 事件                                                                                |
| arg | Object | 订阅的频道                                                                             |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; channel | String | 频道名                                                                               |
| &gt; instId | String | 产品ID<br/>如：ETHUSDT                                                                |
| code | String | 错误码                                                                               |
| msg | String | 错误消息                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "update",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "trade",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "ts": "1695716760565",
            "price": "27000.5",
            "size": "0.001",
            "side": "buy",
            "tradeId": "1111111111"
        },
        {
            "ts": "1695716759514",
            "price": "27000.0",
            "size": "0.001",
            "side": "sell",
            "tradeId": "1111111111"
        }
    ],
    "ts": 1695716761589
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                                                             | 
|:--------------|:-------------------|:---------------------------------------------------------------------------------|
| action        | String             | 推送动作 <br/>推送逻辑调整生效后，仅推送 `update`                                                                            |
| arg           | Object             | 订阅成功的频道                                                                          |
| &gt; instType | String             | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel  | String             | 频道名                                                                              |
| &gt; instId   | String             | 产品ID, 如：ETHUSDT                                                                  |
| data          | List&lt;Object&gt; | 订阅的数据                                                                            |
| &gt; ts       | String             | 成交时间，Unix时间戳的毫秒数格式，如 1597026383085                                               |
| &gt; price    | String             | 成交价格                                                                             |
| &gt; size     | String             | 成交数量                                                                             |
| &gt; side     | String             | 成交方向, sell/buy                                                                   |
| &gt; tradeId  | String             | 成交id                                                                             |
| ts            | String             | 数据推送时间                                                                           |

</div>