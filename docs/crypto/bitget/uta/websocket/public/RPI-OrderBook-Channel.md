---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/RPI-OrderBook-Channel
api_type: WebSocket
updated_at: 2026-11-26 19:03:32.491406
---

# RPI Depth Channel

### Description

Push [RPI (Retail Price Improvement)](https://www.bitget.com/support/articles/12560603867770#:~:text=RPI) depth data. `rpi-books` is the full depth channel, `rpi-books1` is the 1-level channel, `rpi-books5` is the 5-level channel, and `rpi-books50` is the 50-level channel:

- `rpi-books` corresponds to full-depth data, the first push is the full data `snapshot`, subsequent pushes are incremental updates: `update`
- `rpi-books1` corresponds to 1-level depth data, every push: `snapshot`
- `rpi-books5` corresponds to 5-level depth data, every push: `snapshot`
- `rpi-books50` corresponds to 50-level depth data, every push: `snapshot`


- `rpi-books1` push frequency: 10ms 
- `rpi-books5` push frequency: 100ms
- `rpi-books50` push frequency: 100ms
- `rpi-books` push frequency: 100ms


**Sequence Number (seq)**

- The standard orderbook and the RPI orderbook maintain independent seq rules, each calculated separately.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "rpi-books5",
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
| &gt; topic    | String             | Yes      | Topic <br/> `rpi-books` All levels <br/> `rpi-books1` 1 level <br/> `rpi-books5` 5 levels <br/> `rpi-books50` 50 levels                    |
| &gt; [symbol](/docs/catalog/market/market-data#get-instruments)   | String             | Yes      | Symbol name <br/> e.g., `BTCUSDT`                                                                                                          |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "rpi-books5",
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
          "3366.8",
          "9",
          "1"
        ],
        [
          "3367",
          "0",
          "1"
        ],
        [
          "3368",
          "8",
          "2"
        ]
      ],
      "b": [
        [
          "3366.1",
          "7",
          "1"
        ],
        [
          "3366",
          "6",
          "1"
        ]
      ],
      "pseq": 0,
      "seq": 1304314508780744705,
      "ts": "1730969017964"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "symbol": "BTCUSDT",
    "topic": "rpi-books5"
  },
  "action": "snapshot",
  "ts": 1730969017965
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
| ts                 | String             | Data push timestamp                                                                                                                                       |
| data               | List&lt;Object&gt; | Subscribed data                                                                                                                                           |
| &gt; a             | List&lt;String&gt; | Sell Asks. Sort by price in ascending order                                                                                                               |
| &gt; &gt; a[0]     | String             | Ask price                                                                                                                                                 |
| &gt; &gt; a[1]     | String             | Ask non-RPI quantity                                                                                                                                      |
| &gt; &gt; a[2]     | String             | Ask RPI quantity                                                                                                                                          |
| &gt; b             | List&lt;String&gt; | Buy bids. Sort by price in descending order                                                                                                               |
| &gt; &gt; b[0]     | String             | Bid price                                                                                                                                                 |
| &gt; &gt; b[1]     | String             | Bid non-RPI quantity                                                                                                                                      |
| &gt; &gt; b[2]     | String             | Bid RPI quantity                                                                                                                                          |
| &gt; &gt; seq      | String             | Serial number.<br/> It increments when the order book is updated and can be used to determine whether there are out-of-order packets.                     |
| &gt; &gt; pseq     | String             | The serial number of the previous push. <br/> Can be used to determine if there has been packet loss.  This field only has a value for the rpi-books channel. |
| &gt; &gt; ts       | String             | The timestamp that the system generated data <br/>A Unix timestamp in milliseconds                                                                        |

</div>

---

# RPI深度

### 描述

获取[RPI（零售价格优化）](https://www.bitget.com/zh-CN/support/articles/12560603867770#:~:text=RPI)深度数据，`rpi-books`是全量深度频道，`rpi-books1`是1档频道，`rpi-books5`是5档频道，`rpi-books50`是50档频道；

- `rpi-books` 对应全量深度数据，首次推送全量数据 `snapshot`，后续推送增量变化数据: `update`
- `rpi-books1` 对应1档位深度数据，每次推送: `snapshot`
- `rpi-books5` 对应5档位深度数据，每次推送: `snapshot`
- `rpi-books50` 对应50档位深度数据，每次推送: `snapshot`


- `rpi-books1` 推送频率:10ms
- `rpi-books5` 推送频率:100ms
- `rpi-books50` 推送频率:100ms
- `rpi-books` 推送频率:100ms

**seq机制**

- 普通orderbook 及RPI orderbook的seq为两套独立规则，均单独计算

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "rpi-books5",
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
| &gt; topic    | String             | 是    | 频道名<br/>`rpi-books`全部档位频道 <br/>`rpi-books1`一档频道 <br/>`rpi-books5`五档频道 <br/>`rpi-books50`五十档频道       |
| &gt; [symbol](/zh-CN/docs/catalog/market/market-data#get-instruments)   | String             | 是    | 交易对名称<br/>例如`BTCUSDT`                                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "rpi-books5",
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
          "3366.8",
          "9",
          "1"
        ],
        [
          "3367",
          "0",
          "1"
        ],
        [
          "3368",
          "8",
          "2"
        ]
      ],
      "b": [
        [
          "3366.1",
          "7",
          "1"
        ],
        [
          "3366",
          "6",
          "1"
        ]
      ],
      "pseq": 0,
      "seq": 1304314508780744705,
      "ts": "1730969017964"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "symbol": "BTCUSDT",
    "topic": "rpi-books5"
  },
  "action": "snapshot",
  "ts": 1730969017965
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
| ts                 | String             | 数据推送时间戳                                                                                             |
| data               | List&lt;Object&gt; | 订阅的数据                                                                                               |
| &gt; a             | List&lt;String&gt; | 卖方深度                                                                                                |
| &gt; &gt; a[0]     | String             | 卖方价格                                                                                                |
| &gt; &gt; a[1]     | String             | 卖方非RPI数量                                                                                            |
| &gt; &gt; a[2]     | String             | 卖方RPI数量                                                                                             |
| &gt; b             | List&lt;String&gt; | 买方深度                                                                                                |
| &gt; &gt; b[0]     | String             | 买方价格                                                                                                |
| &gt; &gt; b[1]     | String             | 买方非RPI数量                                                                                            |
| &gt; &gt; b[2]     | String             | 买方RPI数量                                                                                             |
| &gt; &gt; seq      | String             | 序列号<br/>订单簿更新时递增，可以用来判断是否乱序                                                                         |
| &gt; &gt; pseq     | String             | 上次推送序列号，可以用来判断是否丢包，只有rpi-books频道有值                                                                  |
| &gt; &gt; ts       | String             | 撮合时间戳                                                                                               |

</div>