---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/public/Depth-Channel
api_type: WebSocket
updated_at: 2026-11-27 19:01:44.273197
---

# Depth Channel

### Description

This is the channel to get the depth data<br/>Default data push frequency for `books`, `books5`, `books15` is **200ms**<br/>Default data push frequency for `books1` is **10ms**

- `books`: All levels of depth. First update pushed is full data: `snapshot`, and then push the update data: `update`
- `books1`: 1st level of depth. Push `snapshot` each time
- `books5`: 5 depth levels. Push `snapshot` each time
- `books15`: 15 depth levels. Push `snapshot` each time

**Explanation of seq**
- The seq of update incremental messages is incrementing except during symbol maintenance.

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "books5",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description | 
| :---- | :---- | :---- | :---- |
| op | String | Yes | Operation, subscribe unsubscribe |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription |
| &gt; instType | String | Yes | Product line type |
| &gt; channel | String | Yes | Channel name: `books/books1/books5/books15`   |
| &gt; instId | String | Yes | Product ID, e.g. ETHUSDT |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "SPOT",
    "channel": "books5",
    "instId": "BTCUSDT"
  }
}
```

### Response Parameters

| Parameter | Type | Description | 
| :---- | :---- | :---- |
| event | String | Yes<br/>Event |
| arg | Object | Subscribed channels |
| &gt; instType | String | Product type |
| &gt; channel | String | Channel name: `books/books1/books5/books15` |
| &gt; instId | String | Product ID, e.g. ETHUSDT |
| code | String | Error code, returned only on error |
| msg | String | Error message |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "action": "snapshot",
  "arg": {
    "instType": "SPOT",
    "channel": "books5",
    "instId": "BTCUSDT"
  },
  "data": [
    {
      "asks": [
        [
          "26274.9",
          "0.0009"
        ],
        [
          "26275.0",
          "0.0500"
        ]
      ],
      "bids": [
        [
          "26274.8",
          "0.0009"
        ],
        [
          "26274.7",
          "0.0027"
        ]
      ],
      "seq": 123,
      "ts": "1695710946294"
    }
  ],
  "ts": 1695710946294
}
```

### Push Parameters

| Parameter     | Type               | Description                                                                                                                                         | 
|:--------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Channels with successful subscription                                                                                                               |
| &gt; instType | String             | Product type                                                                                                                                        |
| &gt; channel  | String             | Channel name: `books/books1/books5/books15`                                                                                                         |
| &gt; instId   | String             | Product ID, e.g. ETHUSDT                                                                                                                            |
| action        | String             | Push data action, `snapshot` or `update`                                                                                                            |
| data          | List&lt;Object&gt; | Subscription data                                                                                                                                   |
| &gt; instId   | String             | Product ID, e.g. ETHUSDT                                                                                                                            |
| &gt; asks     | List&lt;String&gt; | Seller depth                                                                                                                                        |
| &gt; bids     | List&lt;String&gt; | Buyer depth                                                                                                                                         |
| &gt; ts       | String             | Matching engine timestamp(ms), e.g. 1597026383085                                                                                                   |
| &gt; seq      | Long               | Serial number.<br/>It increases when the order book is updated and can be used to determine whether there is out-of-order packets.                  |

</div>

---

# 深度频道

### 描述

获取深度数据频道<br/>`books`,`books5`,`books15`默认推送频率：**200ms**<br/>`books1`默认推送频率: **10ms**

- `books` 对应全量深度数据，首次推送全量数据：`snapshot`，后续推送增量变化数据：`update`。
- `books1` 对应1档位深度数据，每次推送：`snapshot`。
- `books5` 对应5档位深度数据，每次推送：`snapshot`。
- `books15` 对应15档位深度数据，每次推送：`snapshot`。

**seq说明**
- update增量消息的seq在除币对维护的情况是递增的

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "books5",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述 | 
| :---- | :---- | :---- | :---- |
| op | String | 是 | 操作，subscribe unsubscribe |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表 |
| &gt; instType | String | 是 | 产品线类型 |
| &gt; channel | String | 是 | 频道名: `books/books1/books5/books15`   |
| &gt; instId | String | 是 | 产品id 例如：ETHUSDT |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "books5",
        "instId": "BTCUSDT"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| event | String | 事件，subscribe unsubscribe error |
| arg | Object | 订阅的频道 |
| &gt; instType | String | 产品类型 |
| &gt; channel | String | 频道名: `books/books1/books5/books15` |
| &gt; instId | String | 是<br/>产品id 例如：ETHUSDT |
| code | String | 错误码，错误时才会返回 |
| msg | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "books5",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "asks": [
                [
                    "26274.9",
                    "0.0009"
                ],
                [
                    "26275.0",
                    "0.0500"
                ]
            ],
            "bids": [
                [
                    "26274.8",
                    "0.0009"
                ],
                [
                    "26274.7",
                    "0.0027"
                ]
            ],
            "seq": 123,
            "ts": "1695710946294"
        }
    ],
    "ts": 1695710946294
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                               | 
|:--------------|:-------------------|:---------------------------------------------------|
| arg           | Object             | 订阅成功的频道                                            |
| &gt; instType | String             | 产品类型                                               |
| &gt; channel  | String             | 频道名: `books/books1/books5/books15`                 |
| &gt; instId   | String             | 产品id 例如：ETHUSDT                                    |
| action        | String             | 推送数据动作<br/>`snapshot`: 全量数据推送<br/>`update`: 增量数据推送 |
| data          | List&lt;Object&gt; | 订阅的数据                                              |
| &gt; instId   | String             | 产品id 例如：ETHUSDT                                    |
| &gt; asks     | List&lt;String&gt; | 卖方深度                                               |
| &gt; bids     | List&lt;String&gt; | 买方深度                                               |
| &gt; ts       | String             | 撮合引擎时间戳，Unix时间戳的毫秒数格式，如 1597026383085              |
| &gt; seq      | Long               | 序列号 <br/> 订单簿更新时递增，可以用来判断是否乱序                      |

</div>