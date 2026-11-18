---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Fill-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:08.452062
---

# Fill Channel

### Description

Trade Details channel

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "fill",
            "instId": "default"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description            | 
| :---- | :---- |:---------|:-----------------------|
| op | String | Yes      | Operation, subscribe unsubscribe|
| arg | Object | Yes      |Subscribed channels    |
| &gt; channel | String | Yes      | Channel name: `fill`   |
| &gt; instType | String | Yes      | Product type<br/>`SPOT` |
| &gt; instId | String | No       | Product ID or default |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "fill",
        "instId": "default"
    }
}
```

### Response Parameters

| Parameter | Type | Description             | 
| :---- | :---- |:------------------------|
| event | String | Event                   |
| arg | Object | Subscribed channels     |
| &gt; channel | String | Channel name: fill      |
| &gt; instType | String | Product type<br/>`SPOT` |
| &gt; instId | String | Product ID/default      |
| code | String | Error code              |
| msg | String | Error message           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action":"snapshot",
    "arg":{
        "instType":"SPOT",
        "channel":"fill",
        "instId":"default"
    },
    "data":[
        {
            "orderId":"111",
            "tradeId":"111",
            "symbol":"BTCUSDT",
            "orderType":"limit",
            "side":"buy",
            "priceAvg":"42740.41",
            "size":"0.0006",
            "amount":"25.644246",
            "tradeScope":"marker",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538655"
                }
            ],
            "cTime":"1703580202094",
            "uTime":"1703580202094"
        },
        {
            "orderId":"111",
            "tradeId":"222",
            "symbol":"BTCUSDT",
            "orderType":"limit",
            "side":"buy",
            "priceAvg":"42741.46",
            "size":"0.0006",
            "amount":"25.644876",            
            "tradeScope":"marker",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538693"
                }
            ],
            "cTime":"1703580202094",
            "uTime":"1703580202094"
        }
    ],
    "ts":1703580202416
}
```

### Push Parameters

| Parameter                              | Type | Description                                                                  | 
|:---------------------------------------|:-------------------|:-----------------------------------------------------------------------------|
| action                                 | String             | Push action<br/>`snapshot`                                                   |
| arg                                    | Object             | Channels with successful subscription                                        |
| &gt; channel                           | String             | Channel name: fill                                                           |
| &gt; instType                          | String             | Product type<br/>`SPOT`                                                      |
| &gt; instId                            | String             | Product ID                                                                   |
| data                                   | List&lt;Object&gt; | Subscription data                                                            |
| &gt; orderId                           | String             | Order ID                                                                     |
| &gt; tradeId                           | String             | Trade ID                                                                     |
| &gt; symbol                            | String             | Symbol                                                                       |
| &gt; orderType                         | String     | Order type:<br/>`limit`<br/>`market`                                         |
| &gt; side                              | String             | Order direction<br/>`buy `<br/>`sell`                                        |
| &gt; priceAvg                          | String             | Total average filled price                                                   |
| &gt; size                              | String             | Filled size                                                                  |
| &gt; amount                            | String             | Accumulated filled size                                                      |
| &gt; tradeScope                        | String             | The liquidity direction of the latest transaction<br/>`taker ` <br/>`maker ` |
| &gt; feeDetail                         | List&lt;Object&gt;             | Transaction fee of the order                                                 |
| &nbsp;&nbsp;&gt;&gt; deduction         | String            | deduction<br/>`yes `<br/>`no`                                                |
| &nbsp;&nbsp;&gt;&gt; totalDeductionFee | String             | Fee of deduction                                                             |
| &nbsp;&nbsp;&gt;&gt; totalFee          | String             | Fee of all                                                                   |
| &nbsp;&nbsp;&gt;&gt; feeCoin           | String             | Currency of transaction fee                                                  |
| &gt; cTime                             | String             | Create Time，milliseconds format of Unix timestamp, e.g.1597026383085         |
| &gt; uTime                             | String             | Update Time，milliseconds format of Unix timestamp, e.g.1597026383085         |

</div>

---

# 成交明细

### 描述

订阅成交明细信息

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "fill",
            "instId": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                        | 
| :---- | :---- |:-----|:--------------------------|
| op | String | 是    | 操作, subscribe unsubscribe |
| args | List&lt;Object&gt; | 是    | 请求订阅的频道列表                 |
| &gt; channel | String | 是    | 频道名                       |
| &gt; instType | String | 是    | 产品类型                      |
| &gt; instId | String | 否    | 产品名或default               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "fill",
        "instId": "default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明        | 
| :---- | :---- |:------------|
| event | String | 事件          |
| arg | Object | 订阅的频道       |
| &gt; channel | String | 频道名         |
| &gt; instType | String | 产品类型        |
| &gt; instId | String | 产品名或default |
| code | String | 错误码，错误时才会返回 |
| msg | String | 错误消息        |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action":"snapshot",
    "arg":{
        "instType":"SPOT",
        "channel":"fill",
        "instId":"default"
    },
    "data":[
        {
            "orderId":"111",
            "tradeId":"111",
            "symbol":"BTCUSDT",
            "orderType":"limit",
            "side":"buy",
            "priceAvg":"42740.41",
            "size":"0.0006",
            "amount":"25.644246",
            "tradeScope":"marker",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538655"
                }
            ],
            "cTime":"1703580202094",
            "uTime":"1703580202094"
        },
        {
            "orderId":"111",
            "tradeId":"222",
            "symbol":"BTCUSDT",
            "orderType":"limit",
            "side":"buy",
            "priceAvg":"42741.46",
            "size":"0.0006",
            "amount":"25.644876",            
            "tradeScope":"marker",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538693"
                }
            ],
            "cTime":"1703580202094",
            "uTime":"1703580202094"
        }
    ],
    "ts":1703580202416
}
```

### 推送数据参数

| 返回字段                           | 参数类型               | 字段说明                                    | 
|:-------------------------------|:-------------------|:----------------------------------------|
| action                         | String             | 推送动作, 'snapshot'                        |
| arg                            | Object             | 订阅成功的频道                                 |
| &gt; channel                   | String             | 频道名                                     |
| &gt; instType                  | String             | 产品类型<br/>`SPOT`                         |
| &gt; instId                    | String             | 产品ID                                    |
| data                           | List&lt;Object&gt; | 订阅的数据                                   |
| &gt; orderId                   | String             | 订单ID                                    |
| &gt; tradeId                   | String             | 成交ID                                    |
| &gt; symbol                    | String             | 产品名称                                    |
| &gt; side                      | String             | 买卖方向<br/>`buy ` 买<br/>`sell` 卖          |
| &gt; orderType                 | String             | 订单类型<br/>`limit ` 限价单<br/>`market` 市价单    |
| &gt; priceAvg                     | String             | 成交均价                                    |
| &gt; size                | String             | 成交数量                                    |
| &gt; amount               | String             | 成交总额                                    |
| &gt; tradeScope                | String             | 交易者标识<br/>`taker ` 吃单方<br/>`maker ` 挂单方 |
| &gt; feeDetail                 | List&lt;Object&gt;             | 手续费明细                                   |
| &nbsp;&nbsp;&gt;&gt; deduction | String            | 是否折扣                                    |
| &nbsp;&nbsp;&gt;&gt; totalDeductionFee     | String             | 折扣手续费                                   |
| &nbsp;&nbsp;&gt;&gt; totalFee              | String             | 总手续费                                    |
| &nbsp;&nbsp;&gt;&gt; feeCoin           | String             | 手续费币种                                   |
| &gt; cTime                     | String             | 创建时间，Unix时间戳的毫秒数格式，如 1597026383085      |
| &gt; uTime                     | String             | 更新时间，Unix时间戳的毫秒数格式，如 1597026383085      |

</div>