---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Plan-Order-Channel
api_type: WebSocket
updated_at: 2026-11-26 19:02:50.508299
---

# Trigger Order Channel

### Description

Subscribe trigger order channel

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "orders-algo",
            "instId": "default"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description                              | 
| :---- | :---- | :---- |:-----------------------------------------|
| op | String | Yes | Operation, subscribe unsubscribe         |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription |
| &gt; channel | String | Yes | Channel name: orders-algo                |
| &gt; instType | String | Yes | Product type<br/>`SPOT`                  |
| &gt; instId | String | No | Trading pair or default                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "orders-algo",
        "instId": "default"
    }
}
```

### Response Parameters

| Parameter | Type | Description               | 
| :---- | :---- |:--------------------------|
| event | String | Event                     |
| arg | Object | Subscribed channels       |
| &gt; channel | String | Channel name: orders-algo |
| &gt; instType | String | Product type<br/>`SPOT`   |
| &gt; instId | String | Product ID/default        |
| code | String | Error code                |
| msg | String | Error message             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    },
    "data": [
        {
            "instId": "BTCUSDT",
            "orderId": "1",
            "clientOid": "1",
            "triggerPrice": "27000.000000000",
            "triggerType": "fill_price",
            "planType": "amount",
            "price": "27000.000000000",
            "size": "0.020000000",
            "actualSize": "0.000000000",
            "orderType": "market",
            "side": "buy",
            "status": "live",
            "executePrice": "0.1",
            "enterPointSource": "web",
            "cTime": "1695719197612",
            "uTime": "1695719197612",
            "stpMode": "cancel_taker"
        }
    ],
    "ts": 1695719197733
}
```

### Push Parameters

| Parameter             | Type | Description                                                                                                                                                                                                                                                     | 
|:----------------------| :---- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action                | String | Push action                                                                                                                                                                                                                                                     |
| arg                   | Object | Channels with successful subscription                                                                                                                                                                                                                           |
| &gt; channel          | String | Channel name: orders-algo                                                                                                                                                                                                                                       |
| &gt; instType         | String | Product type<br/>`SPOT`                                                                                                                                                                                                                                         |
| &gt; instId           | String | Product ID                                                                                                                                                                                                                                                      |
| data                  | List&lt;Object&gt; | Subscription data                                                                                                                                                                                                                                               |
| &gt; instId           | String | Product ID                                                                                                                                                                                                                                                      |
| &gt; orderId          | String | Bot order ID                                                                                                                                                                                                                                                    |
| &gt; clientOid        | String | Customized bot order ID                                                                                                                                                                                                                                         |
| &gt; triggerPrice     | String | Trigger price                                                                                                                                                                                                                                                   |
| &gt; triggerType      | String | Trigger type<br/>fill_price: filled price<br/>mark_price: mark price                                                                                                                                                                                            |
| &gt; planType         | String | Websocket planType, ws Trigger order type<br/>`amount`<br/>`total`                                                                                                                                                                                     |
| &gt; price            | String | Order price                                                                                                                                                                                                                                                     |
| &gt; size             | String | Original order amount in coin                                                                                                                                                                                                                                   |
| &gt; actualSize       | String | Actual number of orders in coin                                                                                                                                                                                                                                 |
| &gt; orderType        | String | Order type<br/>limit: limit order<br/>market                                                                                                                                                                                                                    |
| &gt; side             | String | Order direction,                                                                                                                                                                                                                                                |
| &gt; status           | String | Order status                                                                                                                                                                                                                                                    |
| &gt; executePrice | String | Execute price                                                                                                                                                                                                                                                   |
| &gt; enterPointSource | String | Order source<br/>WEB: Orders created on the website<br/>API: Orders created on API<br/>SYS: System managed orders, usually generated by forced liquidation logic<br/>ANDROID: Orders created on the Android app<br/>IOS: Orders created on the iOS app          |
| &gt; cTime            | String | Order create time, Milliseconds format of updated data timestamp Unix, e.g. 1597026383085                                                                                                                                                                       |
| &gt; uTime            | String | Order update time, Milliseconds format of updated data timestamp Unix, e.g. 1597026383085                                                                                                                                                                       |
| &gt; stpMode          | String             | STP Mode <br/> `none` not setting STP <br/> `cancel_taker` cancel taker order <br/>  `cancel_maker` cancel maker order <br/>  `cancel_both` cancel both of taker and maker orders                                                                                                                                                         |

</div>

---

# 计划委托频道

### 描述

订阅计划委托

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "orders-algo",
            "instId": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                        | 
| :---- | :---- | :---- |:--------------------------|
| op | String | 是 | 操作, subscribe unsubscribe |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                 |
| &gt; channel | String | 是 | 频道名                       |
| &gt; instType | String | 是 | 产品类型                      |
| &gt; instId | String | 否 | 交易对或default               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| event | String | 事件 |
| arg | Object | 订阅的频道 |
| &gt; channel | String | 频道名 |
| &gt; instType | String | 产品类型  |
| &gt; instId | String |产品ID |
| code | String | 错误码 |
| msg | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    },
    "data": [
        {
            "instId": "BTCUSDT",
            "orderId": "1",
            "clientOid": "1",
            "triggerPrice": "27000.000000000",
            "triggerType": "fill_price",
            "stpMode": "cancel_taker",
            "planType": "amount",
            "price": "27000.000000000",
            "size": "0.020000000",
            "actualSize": "0.000000000",
            "orderType": "market",
            "side": "buy",
            "status": "live",
            "executePrice": "0.1",
            "enterPointSource": "web",
            "cTime": "1695719197612",
            "uTime": "1695719197612"
        }
    ],
    "ts": 1695719197733
}
```

### 推送数据参数

| 返回字段                  | 参数类型               | 字段说明                                                                                                              | 
|:----------------------|:-------------------|:------------------------------------------------------------------------------------------------------------------|
| action                | String             | 推送动作                                                                                                              |
| arg                   | Object             | 订阅成功的频道                                                                                                           |
| &gt; channel          | String             | 频道名                                                                                                               |
| &gt; instType         | String             | 产品类型                                                                                                              |
| &gt; instId           | String             | 产品ID                                                                                                              |
| data                  | List&lt;Object&gt; | 订阅的数据                                                                                                             |
| &gt; instId           | String             | 产品ID                                                                                                              |
| &gt; orderId          | String             | 策略订单ID                                                                                                            |
| &gt; clientOid        | String             | 自定义策略订单id                                                                                                         |
| &gt; triggerPrice     | String             | 触发价格                                                                                                              |
| &gt; triggerType      | String             | 触发类型<br/>fill_price成交价格<br/>mark_price标记价格                                                                        |
| &gt; planType         | String             | Websocket planType,ws计划委托类型<br/>`amount` 金额<br/>`total` 数量                                                        |
| &gt; price            | String             | 委托价格                                                                                                              |
| &gt; size             | String             | 原始委托数量，以币为单位                                                                                                      |
| &gt; actualSize       | String             | 实际委托数量 以币为单位                                                                                                      |
| &gt; orderType        | String             | 订单类型<br/>limit 限价单，<br/>market 市价单                                                                                |
| &gt; side             | String             | 订单方向                                                                                                              |
| &gt; status           | String             | 订单状态                                                                                                              |
| &gt; executePrice     | String             | 执行价                                                                                                               |
| &gt; enterPointSource | String             | 客户端: WEB/API/SYS/ANDROID/IOS                                                                                      |
| &gt; cTime            | String             | 订单创建时间，Unix时间戳的毫秒数格式，如 1597026383085                                                                              |
| &gt; uTime            | String             | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085                                                                              |
| &gt; stpMode          | String             | STP模式 <br/> `none` 不设置STP <br/> `cancel_taker` 取消taker单 <br/>  `cancel_maker` 取消maker单 <br/>  `cancel_both` 两者都取消 |

</div>