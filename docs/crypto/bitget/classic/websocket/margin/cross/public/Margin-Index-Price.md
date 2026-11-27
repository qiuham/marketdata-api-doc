---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/margin/cross/public/Margin-Index-Price
api_type: WebSocket
updated_at: 2026-11-27 19:01:38.803276
---

# Margin Index Price

### Description

Subscribe margin trading pair index price

<div className="api-aligning">

```json title="Request Example"
{
    "args":[
        {
            "channel":"index-price",
            "instType":"MARGIN",
            "instId":"default"
        }
    ],
    "op":"subscribe"
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                   | 
| :---- | :---- | :---- |:--------------------------------------------------------------|
| op | String | Yes | Operation<br/>subscribe Subscribe<br/>unsubscribe Unsubscribe |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription                      |
| &gt; instType | String | Yes | Product type: MARGIN                                          |
| &gt; channel | String | Yes | Channel name                                                  |
| &gt; instId | String | Yes | Product ID<br/>Only support: `default`(all symbols)           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"index-price",
        "instId":"default"
    }
}
```

### Response Parameters

| Parameter | Type | Description                        | 
| :---- | :---- |:-----------------------------------|
| event | String | Event                              |
| arg | Object | Subscribed channels                |
| &gt; instType | String | Product type: MARGIN               |
| &gt; channel | String | Channel name                       |
| &gt; instId | String | Product ID<br/>`default`           |
| code | String | Error code, returned only on error |
| msg | String | Error message                      |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action":"snapshot",
    "arg":{
        "instType":"MARGIN",
        "channel":"index-price",
        "instId":"default"
    },
    "data":[
        {
            "symbol":"BTCUSDT",
            "baseCoin":"BTC",
            "quoteCoin":"USDT",
            "indexPrice":"25702.4",
            "ts":"1695880514609"
        }
    ],
    "ts":1695880514622
}
```

### Push Parameters

| Parameter | Type | Description | 
| :---- | :---- | :---- |
| arg | Object | Channels with successful subscription |
| &gt; instType | String | Product type: MARGIN |
| &gt; channel | String | Channel name |
| &gt; instId | String | Product ID  |
| action | String | Push data action, `snapshot` or `update` |
| data | List&lt;Object&gt; | Subscribed data |
| &gt; baseCoin | String | Base currency |
| &gt; indexPrice | String | Index price |
| &gt; quoteCoin | String | Quote currency |
| &gt; symbol | String | Trading pair |
| &gt; ts | String | Data generation time, Unix millisecond timestamp |
| ts | Long | Push timestamp, Unix millisecond timestamp |

</div>

---

# 杠杆币对指数价格推送

### 描述

获取杠杆币对指数价格推送

<div className="api-aligning">

```json title="请求示例"
{
    "args":[
        {
            "channel":"index-price",
            "instType":"MARGIN",
            "instId":"default"
        }
    ],
    "op":"subscribe"
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                       | 
| :---- | :---- | :---- |:-----------------------------------------|
| op | String | 是 | 操作<br/>subscribe 订阅<br/>unsubscribe 取消订阅 |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                |
| &gt; instType | String | 是 | 产品类型, `MARGIN`                           |
| &gt; channel | String | 是 | 频道名, `index-price`                       |
| &gt; instId | String | 是 | 产品ID<br/>只支持：`default`(全部币对)             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"index-price",
        "instId":"default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明               | 
| :---- | :---- |:-------------------|
| event | String | 事件                 |
| arg | Object | 订阅的频道              |
| &gt; instType | String | 产品类型, `MARGIN`     |
| &gt; channel | String | 频道名, `index-price` |
| &gt; instId | String | 产品ID<br/>`default` |
| code | String | 错误码，错误时才会返回        |
| msg | String | 错误消息               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action":"snapshot",
    "arg":{
        "instType":"MARGIN",
        "channel":"index-price",
        "instId":"default"
    },
    "data":[
        {
            "symbol":"BTCUSDT",
            "baseCoin":"BTC",
            "quoteCoin":"USDT",
            "indexPrice":"25702.4",
            "ts":"1695880514609"
        }
    ],
    "ts":1695880514622
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| arg | Object | 订阅成功的频道 |
| &gt; instType | String | 产品类型, `MARGIN` |
| &gt; channel | String | 频道名, `index-price` |
| &gt; instId | String | 产品id  |
| action | String | 推送数据动作，增量推送数据还是全量推送数据 |
| data | List&lt;Object&gt; | 订阅的数据 |
| &gt; baseCoin | String | 基础币 |
| &gt; indexPrice | String | 指数价格 |
| &gt; quoteCoin | String | 计价币 |
| &gt; symbol | String | 交易对 |
| &gt; ts | String | 数据产生时间，Unix毫秒时间戳 |
| ts | Long | 推送时间戳，Unix毫秒时间戳 |

</div>