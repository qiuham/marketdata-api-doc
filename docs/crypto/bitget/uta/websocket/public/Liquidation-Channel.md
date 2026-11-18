---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Liquidation-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:52.454800
---

# Liquidation Channel

### Description

Liquidation Channel.

Data is pushed once per second (1s/interval). Each push contains the aggregated liquidation data for the previous second: only the record with the highest liquidation quantity for long and short positions respectively per trading pair is included. Both Unified Trading Account and Classic Account liquidation data are covered. For any given trading pair within a single second, at most 2 records are delivered (1 for long, 1 for short).

<div className="api-aligning">

```json title="Request Example"
{
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "liquidation",
            "symbol": "BTCUSDT"
        }
    ],
    "op": "subscribe"
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                        |
|---------------|--------------------|----------|--------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                              |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                 |
| &gt; instType | String             | Yes      | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `liquidation` Liquidation channel                                                                      |
| &gt; symbol   | String             | No       | Symbol name<br/>If provided, only public liquidation data for the specified symbol will be pushed                 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "liquidation"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                        |
|---------------|--------|--------------------------------------------------------------------------------------------------------------------|
| event         | String | Event                                                                                                              |
| arg           | Object | Subscribed channel                                                                                                 |
| &gt; instType | String | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `liquidation` Liquidation channel                                                                      |
| code          | String | Error code                                                                                                         |
| msg           | String | Error message                                                                                                      |
| connId        | String | Connection ID                                                                                                      |

</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "side": "buy",
      "price": "89000",
      "amount": "37.722858",
      "ts": "1736371332162"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "liquidation"
  },
  "action": "update",
  "ts": 1736371332162
}
```

### Push Parameters

| Parameters    | Parameter Type     | Description                                                                                                        |
|---------------|--------------------|--------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Subscribed successful channel                                                                                      |
| &gt; instType | String             | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Topic <br/> `liquidation` Liquidation channel                                                                      |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data                                        |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                    |
| &gt;[symbol](/docs/catalog/market/market-data#get-instruments)    | String             | Symbol name                                                                                                        |
| &gt;side      | String             | Position side<br/>`buy`Long position liquidation<br/>`sell`Short position liquidation                              |
| &gt;price     | String             | Liquidation price                                                                                                  |
| &gt;amount    | String             | Liquidation amount   <br/> Unit: quote coin. For example, `37.722858` means 37.722858 quote coins of the position were liquidated.                                                                       |
| &gt;ts        | String             | Liquidation time (Unix millisecond timestamp)                                                                      |

</div>

---

# 公共强平

### 描述

公共强平数据推送

推送频率为 1s/次，每秒推送上一秒各交易对聚合后的强平数据：仅推送「每个交易对在该秒内、多空分别强平数量最大的记录」，仍涵盖统一账户与经典账户模式下的强平数据，同一交易对在任一秒内最多下发 2 条记录（多头 1 条、空头 1 条）

<div className="api-aligning">

```json title="请求示例"
{
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "liquidation",
            "symbol": "BTCUSDT"
        }
    ],
    "op": "subscribe"
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                                  | 
|:--------------|:-------------------|:-----|:------------------------------------------------------------------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订                                         |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                           |
| &gt; instType | String             | 是    | 产品线类型<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 是    | 频道名<br/>`liquidation`  强平频道                                                         |
| &gt; symbol   | String             | 否    | 交易对名称<br/>传入后，该频道仅推送指定交易对的公共强平数据                                                     |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "liquidation"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                                | 
|:--------------|:-------|:------------------------------------------------------------------------------------|
| event         | String | 事件                                                                                  |
| arg           | Object | 订阅的频道                                                                               |
| &gt; instType | String | 产品线类型<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String | 频道名 <br/>`liquidation`强平频道                                                           |
| code          | String | 错误码                                                                                 |
| msg           | String | 错误消息                                                                                |
| connId        | String | 连接ID                                                                                 |

</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="推送返回示例"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "side": "buy",
      "price": "89000",
      "amount": "37.722858",
      "ts": "1736371332162"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "liquidation"
  },
  "action": "update",
  "ts": 1736371332162
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                                                                | 
|:--------------|:-------------------|:------------------------------------------------------------------------------------|
| arg           | Object             | 订阅成功频道                                                                              |
| &gt; instType | String             | 产品线类型<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 频道名<br/>`liquidation`强平频道                                                           |
| action        | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量                                           |
| data          | List&lt;Object&gt; | 订阅的数据                                                                               |
| &gt;[symbol](/zh-CN/docs/catalog/market/market-data#get-instruments)    | String             | 交易对名称                                                                               |
| &gt;side      | String             | 仓位方向<br/>`buy`多仓强平<br/>`sell`空仓强平                                                   |
| &gt;price     | String             | 强平价格                                                                                |
| &gt;amount    | String             | 强平数量<br/> 单位：计价币。例如 `37.722858` 表示该仓位被强平了 37.722858 个计价币                                                                    |
| &gt;ts        | String             | 强平时间<br/>Unix毫秒时间戳                                                                  |

</div>