---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/public/Auction-Channel
api_type: WebSocket
updated_at: 2026-11-27 19:01:43.192870
---

# Auction Channel

### Description

Get the product's Call Auction information. Frequency of data push: 100ms ~ 300ms

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "auction",
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
| &gt; instType | String | Yes | Product Line Type                |
| &gt; channel | String | Yes | Channel name: `auction`          |
| &gt; instId | String | Yes | Product id For example: ETHUSDT  |

</div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "auction",
        "instId": "BTCUSDT"
    }
}
```
### Response Parameters

| Parameter | Type | Description                             | 
| :---- | :---- |:----------------------------------------|
| event | String | is an <br/> event,                      |
| arg | Object | No<br/>Channel to subscribe to          |
| &gt; instType | String | Is<br/>product type                     |
| &gt; channel | String | is<br/>channel name                     |
| &gt; instId | String | is<br/>product id. For example: BTCUSDT |
| code | String | Error code, returned only on error      |
| msg | String | Error message                           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "auction",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "stage": "stage_1",
            "stageEndTime": "1728876900000",
            "estOpeningPrice": null,
            "matchedVolume": null,
            "auctionEndTime": "1728877500000"
        }
    ],
    "ts": 1695711090682
}
```

### Push Parameters

| Parameter            | Type | Description | 
|:---------------------| :---- | :---- |
| arg                  | Object | Successfully subscribed channel |
| &gt; instType        | String | Product Type |
| &gt; channel         | String | Channel name |
| &gt; instId          | String | Product id For example: ETHUSDT |
| action               | String | Push data action, `snapshot` or `update` |
| data                 | List&lt;Object&gt; | Subscribed data |
| &gt; stage           | String | Call Auction <br/>`pre_market` pre market<br/>`stage_1` Auction 1<br/>`stage_2` Auction 2<br/>`stage_3` Auction 3<br/>`success`  Auction success<br/>`failure` Auction failed |
| &gt; stageEndTime    | String | Current phase end time , millseconds                                                                                                                                          |
| &gt; estOpeningPrice | String | Estimated Opening Price                                                                                                                                                       |
| &gt; matchedVolume   | String | Matched Volume ,base coin                                                                                                                                                     |
| &gt;auctionEndTime       | String | Call Auction end time , millseconds                                                                                                                                           |

</div>

---

# 集合竞价信息频道

### 描述

获取产品的集合竞价信息。定时推送频率：100ms 至 300ms

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "auction",
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
| &gt; instType | String | 是 | 产品线类型                    |
| &gt; channel | String | 是 | 频道名: `auction`           |
| &gt; instId | String | 是 | 产品id 例如：BTCUSDT          |

</div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "auction",
        "instId": "BTCUSDT"
    }
}
```
### 返回参数

| 返回字段 | 参数类型 | 字段说明                           | 
| :---- | :---- |:-------------------------------|
| event | String | 事件，subscribe unsubscribe error |
| arg | Object | 订阅的频道                          |
| &gt; instType | String | 产品类型                           |
| &gt; channel | String | 频道名                            |
| &gt; instId | String | 是<br/>产品id 例如：BTCUSDT          |
| code | String | 错误码，错误时才会返回                    |
| msg | String | 错误消息                           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "auction",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "stage": "stage_1",
            "stageEndTime": "1728876900000",
            "estOpeningPrice": null,
            "matchedVolume": null,
            "auctionEndTime": "1728877500000"
        }
    ],
    "ts": 1695711090682
}
```

### 推送数据参数

| 返回字段                 | 参数类型 | 字段说明                               | 
|:---------------------| :---- |:-----------------------------------|
| arg                  | Object | 订阅成功的频道                            |  
| &gt; instType        | String | 产品类型                               |  
| &gt; channel         | String | 频道名                                |  
| &gt; instId          | String | 产品id 例如：ETHUSDT                    |  
| action               | String | 推送数据动作, `snapshot` or `update`              |  
| data                 | List&lt;Object&gt; | 订阅的数据                              |  
| &gt; stage           | String | 集合竞价阶段<br/>`pre_market` 盘前<br/>`stage_1` 第一阶段<br/>`stage_2` 第二阶段<br/>`stage_3` 第三阶段<br/>`success` 竞价成功<br/>`failure` 竞价失败 |
| &gt; stageEndTime    | String | 当前阶段结束时间 Unix毫秒时间戳                                                                                                        |
| &gt; estOpeningPrice | String | 预估开盘价                                                                                                                     |
| &gt; matchedVolume   | String | 撮合量 单位为集合竞价币种                                                                                                             |
| &gt; auctionEndTime  | String | 集合竞价结束时间                                                                                                                  |

</div>