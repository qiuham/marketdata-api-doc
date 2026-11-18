---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/ADL-Notification-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:35:23.490372
---

# ADL Notification Channel

### Description

Adl Notification Channel

<div className="api-aligning">

```json title="Request Example"
{
    "args": [
        {
            "channel": "adl-noti",
            "instId": "default",
            "instType": "USDT-FUTURES"
        }
    ],
    "op": "subscribe"
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                                                                                                        | 
|:--------------|:-------------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation, subscribe unsubscribe                                                                                   |
| args          | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                           |
| &gt; channel  | String             | Yes      | Channel name: `adl-noti`                                                                                           |
| &gt; instType | String             | Yes      | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; instId   | String             | No       | Symbol Name <br/>By default, subscribes to all symbols: default                                                    |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "adl-noti",
    "instId": "default"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                                                                                                        | 
|:--------------|:-------|:-------------------------------------------------------------------------------------------------------------------|
| event         | String | Event                                                                                                              |
| arg           | Object | Subscribed channels                                                                                                |
| &gt; channel  | String | Channel name: `adl-noti`                                                                                           |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; instId   | String | Symbol Name <br/>By default, subscribes to all symbols: default                                                    |
| code          | String | Error code                                                                                                         |
| msg           | String | Error message                                                                                                      |

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
    "instType": "USDT-FUTURES",
    "channel": "adl-noti",
    "instId": "default"
  },
  "action": "update",
  "ts": 1740546523244
}
```

### Push Parameters

| Parameters    | Type               | Description                                                                                                        |
|:--------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Channels with successful subscription                                                                              |
| &gt; channel  | String             | Channel name: `adl-noti`                                                                                           |
| &gt; instType | String             | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; instId   | String             | Symbol Name <br/>By default, subscribes to all symbols: default                                                    |
| action        | String             | Action <br/>`snapshot` Full data <br/>`update` Incremental data                                                    |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                    |
| &gt;symbol    | String             | Symbol name                                                                                                        |
| &gt;side      | String             | Position side <br/>`buy`Buy<br/>`sell`Sell                                                                         |
| &gt;status    | String             | ADL status <br/>`triggered`Triggered                                                                               |
| &gt;price     | String             | ADL execution price                                                                                                |
| &gt;amount    | String             | ADL execution amount   <br/> Unit: quote coin.                                                                                               |
| &gt;ts        | String             | ADL start time (Unix millisecond timestamp)                                                                        |

</div>

---

# ADL通知

### 描述

ADL通知推送

<div className="api-aligning">

```json title="请求示例"
{
    "args": [
        {
            "channel": "adl-noti",
            "instId": "default",
            "instType": "USDT-FUTURES"
        }
    ],
    "op": "subscribe"
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                               | 
|:--------------|:-------------------|:-----|:---------------------------------------------------------------------------------|
| op            | String             | 是    | 操作, subscribe unsubscribe                                                        |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                        |
| &gt; instType | String             | 是    | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel  | String             | 是    | 频道名     `adl-noti` ADL通知                                                         |
| &gt; instId   | String             | 否    | 交易对名称 <br/> 默认为全量交易对订阅，`default`                                                 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "adl-noti",
    "instId": "default"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                             | 
|:--------------|:-------|:---------------------------------------------------------------------------------|
| event         | String | 操作                                                                               |
| arg           | Object | 订阅的频道                                                                            |
| &gt; channel  | String | 频道名                                                                              |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; instId   | String | 交易对名称 <br/> 默认为全量交易对订阅，`default`                                                 |
| code          | String | 错误码                                                                              |
| msg           | String | 错误消息                                                                             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
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
    "instType": "USDT-FUTURES",
    "channel": "adl-noti",
    "instId": "default"
  },
  "action": "update",
  "ts": 1740546523244
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                                                             | 
|:--------------|:-------------------|:---------------------------------------------------------------------------------|
| action        | String             | 推送动作, `update` 增量 <br/>`snapshot`全量                                              |
| arg           | Object             | 请求订阅的频道                                                                          |
| &gt; channel  | String             | 频道名  `adl-noti`                                                                  |
| &gt; instType | String             | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; instId   | String             | 交易对名称 <br/> 默认为全量交易对订阅，`default`                                                 |
| data          | List&lt;Object&gt; | 订阅的数据                                                                            |
| &gt;symbol    | String             | 交易对名称                                                                            |
| &gt;side      | String             | 仓位方向<br/>`buy`买<br/>`sell`卖                                                      |
| &gt;status    | String             | ADL状态<br/>`triggered`已触发                                                         |
| &gt;price     | String             | ADL执行价格                                                                          |
| &gt;amount    | String             | ADL执行数量   <br/> 单位：计价币                                                           |
| &gt;ts        | String             | ADL开始时间<br/>Unix毫秒时间戳                                                            |

</div>