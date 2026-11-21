---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/public/Order-Book-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:02:51.005908
---

# Depth Channel

### Description

This is the channel to get the depth data<br/>Default data push frequency for `books`, `books5`, `books15` is **150ms**<br/>Default data push frequency for `books1`:**10ms**

Use `books` for snapshot data, `book1` for 1 depth level, `book5` for 5 depth levels,  `book15` for 15 depth levels

- `books`: All levels of depth. First update pushed is full data: `snapshot`, and then push the update data: `update`
- `books1`: 1st level of depth. Push `snapshot` each time
- `books5`: 5 depth levels. Push `snapshot` each time
- `books15`: 15 depth levels. Push `snapshot` each time

**Explanation of seq**
- The seq of update incremental messages is incrementing except during symbol maintenance.

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "books5",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                                                                         | 
| :---- | :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| op | String | Yes | Operation, subscribe unsubscribe                                                                                    |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription                                                                            |
| &gt; instType | String | Yes | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; channel | String | Yes | Channel name: `books/books1/books5/books15`                                                                         |
| &gt; instId | String | Yes | Product ID                                                                                                          |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "books5",
        "instId": "BTCUSDT"
    }
}
```

### Response Parameters

| Parameter | Type | Description                                                                                                         | 
| :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| event | String | Event,                                                                                                              |
| arg | Object | Subscribed channels                                                                                                 |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; channel | String | Channel name, `books/books1/books5/books15`                                                                         |
| &gt; instId | String | Product ID, e.g. ETHUSDT                                                                                            |
| msg | String | Error message                                                                                                       |
| code | String | Error code, returned only on error                                                                                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "books5",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "asks": [
                [
                    "27000.5",
                    "8.760"
                ],
                [
                    "27001.0",
                    "0.400"
                ]
            ],
            "bids": [
                [
                    "27000.0",
                    "2.710"
                ],
                [
                    "26999.5",
                    "1.460"
                ]
            ],
            "seq": 123,
            "pseq": 122,
            "ts": "1695716059516"
        }
    ],
    "ts": 1695716059516
}
```

### Push Parameters

| Parameter        | Type               | Description                                                                                                                        | 
|:-----------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| arg              | Object             | Channels with successful subscription                                                                                              |
| &gt; instType    | String             | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures                 |
| &gt; channel     | String             | Channel name, `books/books1/books5/books15`                                                                                        |
| &gt; instId      | String             | Product ID                                                                                                                         |
| action           | String             | Push data action, Incremental push data or full volume push data                                                                   |
| data             | List&lt;Object&gt; | Subscription data                                                                                                                  |
| &gt; asks        | List&lt;String&gt; | Seller depth                                                                                                                       |
| &gt; bids        | List&lt;String&gt; | Buyer depth                                                                                                                        |
| &gt; ts          | String             | Match engine timestamp(ms), e.g. 1597026383085                                                                                     |
| &gt; seq         | Long               | Serial number.<br/>It increases when the order book is updated and can be used to determine whether there is out-of-order packets. |
| &gt; pseq        | String             | The serial number of the previous push.<br/>For the `books` channel: non-zero when pushing incremental update data. For `books1`, `books5`, and `books15` channels: always `0`. Can be used to determine whether there is packet loss. |
| ts               | String             | Data streaming time                                                                                                                |

</div>

---

# 深度频道

### 描述

获取深度数据<br/>`books`,`books5`,`books15`默认推送频率：**150ms**<br/>`books1`默认推送频率：**10ms**

- `books` 对应全量深度数据，首次推送全量数据：`snapshot`，后续推送增量变化数据：`update`
- `books1` 对应1档位深度数据，每次推送：`snapshot`
- `books5` 对应5档位深度数据，每次推送：`snapshot`
- `books15` 对应15档位深度数据，每次推送：`snapshot`

**seq说明**
- update增量消息的seq在除币对维护的情况是递增的

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "books5",
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
| &gt; channel | String | 是 | 频道名: `books/books1/books5/books15`                                                |
| &gt; instId | String | 是 | 产品ID                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "books5",
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
| &gt; channel | String | 频道名: `books/books1/books5/books15`                                                |
| &gt; instId | String | 产品ID                                                                              |
| msg | String | 错误消息                                                                              |
| code | String | 错误码                                                                               |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "books5",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "asks": [
                [
                    "27002.0",
                    "5.070"
                ],
                [
                    "27002.5",
                    "1.470"
                ]
            ],
            "bids": [
                [
                    "26998.5",
                    "6.620"
                ],
                [
                    "26998.0",
                    "7.510"
                ]
            ],
            "seq": 123,
            "pseq": 122,
            "ts": 1695716059516
        }
    ],
    "ts": "1695716059516"
}
```

### 推送数据参数

| 返回字段           | 参数类型               | 字段说明                                                                             | 
|:---------------|:-------------------|:---------------------------------------------------------------------------------|
| arg            | Object             | 订阅成功的频道                                                                          |
| &gt; instType  | String             | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel   | String             | 频道名: `books/books1/books5/books15`                                               |
| &gt; instId    | String             | 产品ID                                                                             |
| action         | String             | 推送数据动作， 增量推送数据还是全量推送数据                                                           |
| data           | List&lt;Object&gt; | 订阅的数据                                                                            |
| &gt; asks      | List&lt;String&gt; | 卖方深度                                                                             |
| &gt; bids      | List&lt;String&gt; | 买方深度                                                                             |
| &gt; ts        | String             | 撮合引擎时间戳，Unix时间戳的毫秒数格式，如 1597026383085                                            |
| &gt; seq       | Long               | 序列号 <br/> 订单簿更新时递增，可以用来判断是否乱序                                                    |
| &gt; pseq      | String             | 上次推送序列号<br/>`books` 频道：推送增量变化数据时有值且非0；`books1`、`books5`、`books15` 频道：固定返回 `0`。可用来判断是否丢包 |
| ts             | String             | 数据推送时间                                                                           |

</div>