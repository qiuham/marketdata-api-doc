---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/margin/cross/private/Cross-Orders
api_type: WebSocket
updated_at: 2026-11-22 19:00:05.978793
---

# Cross-Margin Orders Channel

### Description

<div className="api-aligning">

```json title="Request Example"
{
    "args":[
        {
            "channel":"orders-crossed",
            "instId":"BTCUSDT",
            "instType":"MARGIN"
        }
    ],
    "op":"subscribe"
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                         | 
| :---- | :---- | :---- |:--------------------------------------------------------------------|
| op | String | Yes | Operation<br/>`subscribe`: Subscribe<br/>`unsubscribe`: Unsubscribe |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription                            |
| &gt; instType | String | Yes | Product type: MARGIN                                                |
| &gt; channel | String | Yes | Channel name                                                        |
| &gt; instId | String | Yes | Product ID<br/>e.g. ETHUSDT                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"orders-crossed",
        "instId":"BTCUSDT"
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
| &gt; instId | String | Product ID<br/>e.g. ETHUSDT        |
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
        "channel":"orders-crossed",
        "instId":"BTCUSDT"
    },
    "data":[
        {
            "force":"gtc",
            "orderType":"market",
            "price":"0.000000000",
            "quoteSize":"0.000000000",
            "side":"buy",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538693"
                }
            ],
            "enterPointSource":"web",
            "status":"partially_filled",
            "baseSize":"0.000000000",
            "cTime":"1695881543701",
            "uTime":"1695881543701",
            "clientOid":"2000000000",
            "fillPrice":"26426.800000000",
            "baseVolume":"0.000200000",
            "fillTotalAmount":"5.285360000",
            "loanType":"normal",
            "orderId":"1",
            "stpMode": "cancel_taker"
        }
    ],
    "ts":1695881543805
}
```

### Push Data Parameters

| Parameter | Type | Description | 
| :---- | :---- | :---- |
| arg | Object | Successful channel subscriptions |
| &gt; instType | String | Product type: MARGIN |
| &gt; channel | String | Channel name |
| &gt; instId | String | Product ID, e.g. ETHUSDT |
| action | String | Push data action, `snapshot` or `update` |
| data | List&lt;Object&gt; | Subscribed data |
| &gt; baseSize | String | Number of base coins |
| &gt; cTime | String | Creation time, Unix millisecond timestamp  |
| &gt; uTime  | String | Update time, Unix millisecond timestamp |
| &gt; clientOid | String | Client Unique Identifier |
| &gt; fillPrice | String | Sale price |
| &gt; baseVolume | String | Filled quantity |
| &gt; fillTotalAmount | String | sum of money sold |
| &gt; loanType | String | Margin order model<br/>normal: place a normal order<br/>autoLoan place an order with auto-borrow<br/>autoRepay place an order with auto-repay<br/>autoLoanAndRepay place an order with auto-borrow and auto-repay  |
| &gt; orderId | String | Order ID |
| &gt; orderType | String | Order type<br/>limit: limit order<br/>market |
| &gt; price | String | Order price |
| &gt; quoteSize | String | Number of denominated coins |
| &gt; side | String | Methods of Sale and Purchase |
| &gt; feeDetail                         | List&lt;Object&gt; | Transaction fee of the order                                                                                                                      |
| &nbsp;&nbsp;&gt;&gt; deduction         | String             | Is discount                                                                                                                       |
| &nbsp;&nbsp;&gt;&gt; totalDeductionFee | String             | Fee of discount                                                                                                                      |
| &nbsp;&nbsp;&gt;&gt; totalFee               | String             | Order transaction fee, the transaction fee charged by the platform from the user.                                                                                                                       |
| &nbsp;&nbsp;&gt;&gt; feeCoin           | String             | The currency of the transaction fee                                                                                                                      |
| &gt; enterPointSource | String | Order source<br/>WEB: Orders created on the website<br/>API: Orders created on API<br/>SYS: System managed orders, usually generated by forced liquidation logic<br/>ANDROID: Orders created on the Android app<br/>IOS: Orders created on the iOS app |
| &gt; status | String | Order status<br/>`live`:new order;<br/>`partially_filled`:partially filled;<br/>`filled`:full filled;<br/>`cancelled`: cancelled; |
| &gt; force | String | Order Strategy |
| &gt; stpMode          | String             | STP Mode <br/> `none` not setting STP <br/> `cancel_taker` cancel taker order <br/>  `cancel_maker` cancel maker order <br/>  `cancel_both` cancel both of taker and maker orders                                                                                                                                                         |
| ts | Long | Timestamp ms |

</div>

---

# 全仓杠杆订单频道

### 描述

<div className="api-aligning">

```json title="请求示例"
{
    "args":[
        {
            "channel":"orders-crossed",
            "instId":"BTCUSDT",
            "instType":"MARGIN"
        }
    ],
    "op":"subscribe"
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述 | 
| :---- | :---- | :---- | :---- |
| op | String | 是 | 操作<br/>subscribe 订阅<br/>unsubscribe 取消订阅 |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表 |
| &gt; instType | String | 是 | 产品类型, `MARGIN` |
| &gt; channel | String | 是 | 频道名, `orders-crossed` |
| &gt; instId | String | 是 | 产品ID<br/>如:ETHUSDT |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event":"subscribe",
    "arg":{
        "instType":"MARGIN",
        "channel":"orders-crossed",
        "instId":"BTCUSDT"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| event | String | 事件 |
| arg | Object | 订阅的频道 |
| &gt; instType | String | 产品类型 |
| &gt; channel | String | 频道名 |
| &gt; instId | String | 产品ID。如：ETHUSDT |
| code | String | 错误码，错误时才会返回 |
| msg | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action":"snapshot",
    "arg":{
        "instType":"MARGIN",
        "channel":"orders-crossed",
        "instId":"BTCUSDT"
    },
    "data":[
        {
            "force":"gtc",
            "orderType":"market",
            "price":"0.000000000",
            "quoteSize":"0.000000000",
            "side":"buy",
            "feeDetail":[
                {
                    "feeCoin":"USDT",
                    "deduction":"no",
                    "totalDeductionFee":"0",
                    "totalFee":"0.01538693"
                }
            ],
            "enterPointSource":"web",
            "status":"partially_filled",
            "baseSize":"0.000000000",
            "cTime":"1695881543701",
            "uTime":"1695881543701",
            "stpMode": "cancel_taker",
            "clientOid":"2000000000",
            "fillPrice":"26426.800000000",
            "baseVolume":"0.000200000",
            "fillTotalAmount":"5.285360000",
            "loanType":"normal",
            "orderId":"1000000000"
        }
    ],
    "ts":1695881543805
}
```

### 推送数据参数

| 返回字段 | 参数类型               | 字段说明                                                                                                                      | 
| :---- |:-------------------|:--------------------------------------------------------------------------------------------------------------------------|
| arg | Object             | 订阅成功的频道                                                                                                                   |
| &gt; instType | String             | 产品类型                                                                                                                      |
| &gt; channel | String             | 频道名                                                                                                                       |
| &gt; instId | String             | 产品ID, 如:ETHUSDT                                                                                                           |
| action | String             | 推送数据动作，增量推送数据还是全量推送数据                                                                                                     |
| data | List&lt;Object&gt; | 订阅的数据                                                                                                                     |
| &gt; baseSize | String             | 基础币数量                                                                                                                     |
| &gt; cTime | String             | 订单创建时间                                                                                                                    |
| &gt; uTime | String             | 订单更新时间                                                                                                                    |
| &gt; clientOid | String             | 客户端唯一标识                                                                                                                   |
| &gt; fillPrice | String             | 成交价                                                                                                                       |
| &gt; baseVolume | String             | 成交数量                                                                                                                      |
| &gt; fillTotalAmount | String             | 成交金额                                                                                                                      |
| &gt; loanType | String             | 杠杆订单模式<br/>normal        普通下单<br/>autoLoan        自动借款下单<br/>autoRepay        自动还款下单<br/>autoLoanAndRepay        自动借款还款下单 |
| &gt; orderId | String             | 订单Id                                                                                                                      |
| &gt; orderType | String             | 订单类型<br/>limit 限价<br/>market 市价                                                                                           |
| &gt; price | String             | 订单价格                                                                                                                      |
| &gt; quoteSize | String             | 计价币数量                                                                                                                     |
| &gt; side | String             | 买卖方式                                                                                                                      |
| &gt; feeDetail                         | List&lt;Object&gt; | 手续费明细                                                                                                                     |
| &nbsp;&nbsp;&gt;&gt; deduction         | String             | 是否折扣                                                                                                                      |
| &nbsp;&nbsp;&gt;&gt; totalDeductionFee | String             | 折扣手续费                                                                                                                     |
| &nbsp;&nbsp;&gt;&gt; totalFee               | String             | 总手续费                                                                                                                      |
| &nbsp;&nbsp;&gt;&gt; feeCoin           | String             | 手续费币种                                                                                                                     |
| &gt; enterPointSource | String             | 订单来源<br/>WEB    WEB客户端<br/>IOS    IOS客户端<br/>ANDROID    Andriod客户端<br/>API    API客户端<br/>SYS    系统, 通常为爆仓                 |
| &gt; status | String             | 订单状态<br/>`live`:新建订单;<br/>`partially_filled`:部分成交;<br/>`filled`:全部成交;<br/>`cancelled`: 已撤销;                               |
| &gt; force | String             | 订单策略                                                                                                                      |
| &gt; stpMode          | String             | STP模式 <br/> `none` 不设置STP <br/> `cancel_taker` 取消taker单 <br/>  `cancel_maker` 取消maker单 <br/>  `cancel_both` 两者都取消         |
| ts | Long               | 时间戳，毫秒                                                                                                                    |

</div>