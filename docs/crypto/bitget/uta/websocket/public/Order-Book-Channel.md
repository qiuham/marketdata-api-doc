---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Order-Book-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:55.259727
---

# Depth Channel

### Description

Push depth data. `books` is the full depth channel, `books1` is the 1-level channel, `books5` is the 5-level channel,
and `books50` is the 50-level channel:

- `books` corresponds to full-depth data, the first push is the full data `snapshot`, subsequent pushes are incremental
  updates: `update`
- `books1` corresponds to 1-level depth data, every push: `snapshot`
- `books5` corresponds to 5-level depth data, every push: `snapshot`
- `books50` corresponds to 50-level depth data, the first push is the full data `snapshot`, subsequent pushes are
  incremental updates: `update`

Spot

- `books1` push frequency: 1ms
- `books5` push frequency: 10ms
- `books50` push frequency: 20ms
- `books` push frequency: 50ms


Futures

- `books1` push frequency: 1ms
- `books5` push frequency: 10ms
- `books50` push frequency: 20ms
- `books` push frequency: 50ms

The serial number of the previous push `pseq` :
- Under normal circumstances, the serial numbers pushed by the depth channel are incremental, meaning that the `seq` value received in a push sequence is always greater than the `pseq`.
- In cases such as system releases or service restarts, the serial numbers may be reset. At this time, users will most likely receive a push message with `pseq=0`. After the reset, all subsequent messages will continue to be ordered normally.
- The seq of the previous update incremental message must be equal to the pseq of the following update incremental message.
- The seq of update incremental messages should be increasing, except during symbol maintenance.
- After receiving a snapshot (full snapshot), the seq of the snapshot should fall within the range [pseq, seq] of the first update incremental data received after the snapshot.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "books",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                                                |
|---------------|--------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                                                      |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                                         |
| &gt; instType | String             | Yes      | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `books` All levels <br/> `books1` 1 level <br/> `books5` 5 levels <br/> `books50` 50 levels                                    |
| &gt; symbol   | String             | Yes      | Symbol name <br/> e.g., `BTCUSDT`                                                                                                          |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books1",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters      | Type   | Description                                                                                                                                |
|-----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| event           | String | Event                                                                                                                                      |
| arg             | Object | Subscribed channel                                                                                                                         |
| &gt; instType   | String | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic      | String | Topic                                                                                                                                      |
| &gt; symbol     | String | Symbol name                                                                                                                                |
| code            | String | Error code                                                                                                                                 |
| msg             | String | Error message                                                                                                                              |
| connId          | String | Connection ID                                                                                                                              |

</div>

<div className="api-br-5"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "a": [
        [
          "99756.7",
          "23.9774"
        ]
      ],
      "b": [
        [
          "99756.6",
          "0.0128"
        ]
      ],
      "pseq": 0,
      "seq": 1304314508780744705,
      "maxDepth": "50",
      "ts": "1746698732562"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "symbol": "BTCUSDT",
    "topic": "books"
  },
  "action": "snapshot",
  "ts": 1746698732563
}
```

### Push Parameters

| Return Field       | Parameter Type     | Description                                                                                                                                               |
|--------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                | Object             | Subscribed channel                                                                                                                                        |
| &gt; instType      | String             | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures                |
| &gt; topic         | String             | Topic                                                                                                                                                     |
| &gt; symbol        | String             | Symbol name                                                                                                                                               |
| action             | String             | Data push action <br/> `snapshot` Full push <br/> `update` Incremental push                                                                               |
| ts                 | String             | Data push timestamp                                                                              |
| data               | List&lt;Object&gt; | Subscribed data                                                                                                                                           |
| &gt; a             | List&lt;String&gt; | Sell Asks. Sort by price in ascending order                                                                                                               |
| &gt; &gt; a[0]     | String             | Sell price                                                                                                                                                |
| &gt; &gt; a[1]     | String             | Sell quantity                                                                                                                                             |
| &gt; b             | List&lt;String&gt; | Buy bids. Sort by price in descending order                                                                                                               |
| &gt; &gt; b[0]     | String             | Buy Price                                                                                                                                                 |
| &gt; &gt; b[1]     | String             | Buy quantity                                                                                                                                              |
| &gt; &gt; seq      | String             | Serial number.<br/> It increments when the order book is updated and can be used to determine whether there is out-of-order packets.                      |
| &gt; &gt; pseq     | String             | The serial number of the previous push. <br/> Can be used to determine if there has been packet loss.  This field only has a value for the `books` and `books50` channels. |
| &gt; maxDepth      | String             | Maximum depth levels.<br/>Range: [0,1000].<br/>Positive integer, varies between trading pairs.<br/>This field only has a value for the `books` channel.    |
| &gt; &gt; ts       | String             | The timestamp that the system generated data <br/>A Unix timestamp in milliseconds                                                                        |

</div>

---

# 深度

### 描述

获取深度数据，books是全量深度频道，books1是1档频道，books5是5档频道，books50是50档频道；

- `books` 对应全量深度数据,首次推送全量数据 `snapshot`，后续推送增量变化数据: `update`
- `books1` 对应1档位深度数据,每次推送: `snapshot`
- `books5` 对应5档位深度数据,每次推送:  `snapshot`
- `books50` 对应50档位深度数据,首次推送全量数据 `snapshot`，后续推送增量变化数据: `update`

现货

- `books1` 推送频率:1ms
- `books5` 推送频率:10ms
- `books50` 推送频率:20ms
- `books` 推送频率:50ms


合约

- `books1` 推送频率:1ms
- `books5` 推送频率:10ms
- `books50` 推送频率:20ms
- `books` 推送频率:50ms

上次推送序列号 `pseq` :
- 正常情况下，深度频道推送的序列号是增长的，即在一个推送序列里接收到的`seq`值总是大于`pseq`。
- 在系统发布等服务重启的情况下，序列号可能会被重置。此时用户大概率会收到一个 `pseq=0`的推送消息。重置后，所有后续消息将继续按正常顺序排序。
- update增量消息前一条的seq一定等于后一条的pseq
- update增量消息的seq在除币对维护的情况是递增的
- 接收snapshot全量快照后的第一条update增量数据，snapshot的seq在update增量[pseq, seq] 范围内

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "books1",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                                                  | 
|:--------------|:-------------------|:-----|:----------------------------------------------------------------------------------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订                                                         |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                           |
| &gt; instType | String             | 是    | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 是    | 频道名<br/>`books`全部档位频道 <br/>`books1`一档频道 <br/>`books5`五档频道 <br/>`books50`五十挡频道                       |
| &gt; symbol   | String             | 是    | 交易对名称<br/>例如`BTCUSDT`                                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books1",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                                                | 
|:--------------|:-------|:----------------------------------------------------------------------------------------------------|
| event         | String | 事件                                                                                                  |
| arg           | Object | 订阅的频道                                                                                               |
| &gt; instType | String | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String | 频道名                                                                                                 |
| &gt; symbol   | String | 交易对名称                                                                                               |
| code          | String | 错误码                                                                                                 |
| msg           | String | 错误消息                                                                                                |
| connId        | String | 连接ID                                                                                                 |

</div>

<div className="api-br-5"></div>


<div className="api-aligning">

```json title="推送返回示例"
{
  "data": [
    {
      "a": [
        [
          "99756.7",
          "23.9774"
        ]
      ],
      "b": [
        [
          "99756.6",
          "0.0128"
        ]
      ],
      "pseq":0,
      "seq": 1304314508780744705,
      "maxDepth": "50",
      "ts": "1746698732562"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "symbol": "BTCUSDT",
    "topic": "books"
  },
  "action": "snapshot",
  "ts": 1746698732563
}
```

### 推送数据参数

| 返回字段               | 参数类型               | 字段说明                                                                                                | 
|:-------------------|:-------------------|:----------------------------------------------------------------------------------------------------|
| arg                | Object             | 订阅成功的频道                                                                                             |
| &gt; instType      | String             | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic         | String             | 频道名                                                                                                 |
| &gt; symbol        | String             | 交易对名称                                                                                               |
| action             | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量                                                           |
| ts                 | String             | 数据推送时间戳                                                                                              |
| data               | List&lt;Object&gt; | 订阅的数据                                                                                               |
| &gt; a             | List&lt;String&gt;             | 卖方深度                                                                                                |
| &gt; &gt; a[0]     | String             | 卖一价                                                                                                 |
| &gt; &gt; a[1]     | String             | 卖一量                                                                                                 |
| &gt; b             | List&lt;String&gt;             | 买方深度                                                                                                |
| &gt; &gt; b[0]     | String             | 买一价                                                                                                 |
| &gt; &gt; b[1]     | String             | 买一量                                                                                                 |
| &gt; &gt;seq       | String             | 序列号<br/>订单簿更新时递增，可以用来判断是否乱序                                                                         |
| &gt; &gt;pseq      | String             | 上次推送序列号，可以用来判断是否丢包，只有`books`和`books50`频道有值                                                               |
| &gt; maxDepth      | String             | 最大深度档位<br/>范围为[0,1000]<br/>正整数，不同交易对之间有差异<br/>只有`books`频道有值                                        |
| &gt; &gt;ts        | String             | 撮合时间戳                                                                                               |

</div>