---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Order-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:01:34.183476
---

# Order Channel

### Description

Get order information. Initial subscriptions will not trigger any push notifications. 

Data will be pushed when the following events occurred:
1. Place orders
2. Orders are filled
3. Cancel orders
4. Modify orders

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "orders",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                                                    | 
|:--------------|:-------------------|:---------|:---------------------------------------------------------------|
| op            | String             | Yes      | Operation, subscribe unsubscribe                               |
| args          | List&lt;Object&gt; | Yes      | List of channels to request subscription                       |
| &gt; instType | String             | Yes      | Product line type                                              |
| &gt; channel  | String             | Yes      | Channel name                                                   |
| &gt; instId   | String             | Yes      | Product ID, e.g. `ETHUSDT`<br/>`default`:subscribe all symbols |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "SPOT",
    "channel": "orders",
    "instId": "BTCUSDT"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                        | 
|:--------------|:-------|:-----------------------------------|
| event         | String | Yes<br/>Event                      |
| arg           | Object | Subscribed channels                |
| &gt; instType | String | Product type                       |
| &gt; channel  | String | Channel name                       |
| &gt; instId   | String | Product ID, e.g. ETHUSDT           |
| code          | String | Error code, returned only on error |
| msg           | String | Error message                      |

</div>

```json title="Push Data"
{
  "action": "snapshot",
  "arg": {
    "instType": "SPOT",
    "channel": "orders",
    "instId": "BTCUSDT"
  },
  "data": [
    {
      "instId": "BTCUSDT",
      "orderId": "1",
      "clientOid": "1",
      "size": "8.0000",
      "newSize": "500.0000",
      "notional": "8.000000",
      "orderType": "market",
      "force": "gtc",
      "side": "buy",
      "fillPrice": "26256.0",
      "tradeId": "1",
      "baseVolume": "0.0003",
      "fillTime": "1695797773286",
      "fillFee": "-0.00000018",
      "fillFeeCoin": "BTC",
      "tradeScope": "T",
      "accBaseVolume": "0.0003",
      "priceAvg": "26256.0",
      "status": "partially_filled",
      "cTime": "1695797773257",
      "uTime": "1695797773326",
      "stpMode": "cancel_taker",
      "feeDetail": [
        {
          "feeCoin": "BTC",
          "fee": "-0.00000018"
        }
      ],
      "enterPointSource": "WEB"
    }
  ],
  "ts": 1695797773370
}
```

### Push Parameters

| Parameter             | Type               | Description                                                                                                                                                                                                                                                                                                                               | 
|:----------------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                   | Object             | Channels with successful subscription                                                                                                                                                                                                                                                                                                     |
| &gt; instType         | String             | Product type                                                                                                                                                                                                                                                                                                                              |
| &gt; channel          | String             | Channel name                                                                                                                                                                                                                                                                                                                              |
| &gt; instId           | String             | Yes                                                                                                                                                                                                                                                                                                                                       |
| action                | String             | Push data action, `snapshot` or `update`                                                                                                                                                                                                                                                                                                  |
| data                  | List&lt;Object&gt; | Subscription data                                                                                                                                                                                                                                                                                                                         |
| &gt; instId           | String             | Product ID, e.g. ETHUSDT                                                                                                                                                                                                                                                                                                                  |
| &gt; orderId          | String             | Order ID                                                                                                                                                                                                                                                                                                                                  |
| &gt; clientOid        | String             | Customized order ID                                                                                                                                                                                                                                                                                                                       |
| &gt; price            | String             | Order price                                                                                                                                                                                                                                                                                                                               |
| &gt; size             | String             | Order amount<br/>when `side=buy`, it represents the amount of quote coin;<br/>when `side=sell`, it represents the amount of base coin.                                                                                                                                                                                                    |
| &gt; newSize          | String             | `newSize` represents the order quantity, following the specified rules:<br/>when `orderType=limit`, `newSize` represents the quantity of base coin,<br/>when `orderType=market`and`side=buy`, `newSize` represents the quantity of quote coin,<br/>when `orderType=market`and`side=sell`, `newSize` represents the quantity of base coin. |
| &gt; notional         | String             | Buy amount, returned when buying at market price                                                                                                                                                                                                                                                                                          |
| &gt; ordType          | String             | Order type, market: market order. Limit: limit order                                                                                                                                                                                                                                                                                      |
| &gt; force            | String             | Order validity, GTC: normal limit order, good till canceled. post_only Post only. FOK: Fill or kill. IOC: Immediate or cancel.                                                                                                                                                                                                            |
| &gt; side             | String             | Order direction                                                                                                                                                                                                                                                                                                                           |
| &gt; fillPrice        | String             | Latest filled price                                                                                                                                                                                                                                                                                                                       |
| &gt; tradeId          | String             | Latest transaction ID                                                                                                                                                                                                                                                                                                                     |
| &gt; baseVolume       | String             | Number of latest filled orders                                                                                                                                                                                                                                                                                                            |
| &gt; fillTime         | String             | Latest transaction time                                                                                                                                                                                                                                                                                                                   | Unix millisecond timestamp, e.g. 1690196141868 |
| &gt; fillFee          | String             | Transaction fee of the latest transaction, negative value                                                                                                                                                                                                                                                                                 |
| &gt; fillFeeCoin      | String             | Currency of transaction fee of the latest transaction                                                                                                                                                                                                                                                                                     |
| &gt; tradeScope       | String             | Direction of liquidity of the latest transaction<br/>`T`:taker;<br/>`M`:maker;                                                                                                                                                                                                                                                            |
| &gt; accBaseVolume    | String             | Total filled quantity                                                                                                                                                                                                                                                                                                                     |
| &gt; priceAvg         | String             | Total average filled price. If the filled orders are 0, the field is 0.                                                                                                                                                                                                                                                                   |
| &gt; status                | String | Order status<br/>`live`:new order;<br/>`partially_filled`:partially filled;<br/>`filled`:full filled;<br/>`cancelled`: cancelled;                                                                                                                                                                                                         |
| &gt; enterPointSource | String             | Order source                                                                                                                                                                                                                                                                                                                              |
| &gt; feeDetail        | List&lt;Object&gt; | transaction fee list                                                                                                                                                                                                                                                                                                                      |
| &gt;&gt; feeCoin      | String             | Transaction fee currency                                                                                                                                                                                                                                                                                                                  |
| &gt;&gt; fee          | String             | Order transaction fee, the transaction fee charged by the platform from the user.                                                                                                                                                                                                                                                         | (orders only, excluding discounts) |
| &gt; cTime            | String             | Order creation time, milliseconds format of Unix timestamp, e.g.1630410492847                                                                                                                                                                                                                                                             |
| &gt; uTime            | String             | Order Update time, milliseconds format of Unix timestamp, e.g.1630410492847                                                                                                                                                                                                                                                               |
| &gt; stpMode          | String             | STP Mode <br/> `none` not setting STP <br/> `cancel_taker` cancel taker order <br/>  `cancel_maker` cancel maker order <br/>  `cancel_both` cancel both of taker and maker orders                                                                                                                                                         |

---

# 订单频道

### 描述

获取订单信息，首次订阅不推送。

以下事件发生时将推送数据：
1. 挂单
2. 订单成交
3. 撤单
4. 订单修改

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "orders",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                     | 
|:--------------|:-------------------|:-----|:---------------------------------------|
| op            | String             | 是    | 操作，subscribe unsubscribe               |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                              |
| &gt; instType | String             | 是    | 产品线类型, `SPOT`                          |
| &gt; channel  | String             | 是    | 频道名, `orders`                          |
| &gt; instId   | String             | 是    | 产品id 例如：`ETHUSDT`<br/>`default`: 订阅所有币对 |

</div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "SPOT",
    "channel": "orders",
    "instId": "BTCUSDT"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                  | 
|:--------------|:-------|:----------------------|
| event         | String | 事件，subscribe unsubscribe error             |
| arg           | Object | 订阅的频道           |
| &gt; instType | String | 产品类型            |
| &gt; channel  | String | 频道名             |
| &gt; instId   | String | 是<br/>产品id 例如：ETHUSDT |
| code          | String | 错误码，错误时才会返回     |
| msg           | String | 错误消息            |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "action": "snapshot",
  "arg": {
    "instType": "SPOT",
    "channel": "orders",
    "instId": "BTCUSDT"
  },
  "data": [
    {
      "instId": "BTCUSDT",
      "orderId": "1",
      "clientOid": "1",
      "size": "8.0000",
      "newSize": "500.0000",
      "notional": "8.000000",
      "orderType": "market",
      "force": "gtc",
      "side": "buy",
      "fillPrice": "26256.0",
      "tradeId": "1",
      "baseVolume": "0.0003",
      "fillTime": "1695797773286",
      "fillFee": "-0.00000018",
      "fillFeeCoin": "BTC",
      "tradeScope": "T",
      "stpMode": "cancel_taker",
      "accBaseVolume": "0.0003",
      "priceAvg": "26256.0",
      "status": "partially_filled",
      "cTime": "1695797773257",
      "uTime": "1695797773326",
      "feeDetail": [
        {
          "feeCoin": "BTC",
          "fee": "-0.00000018"
        }
      ],
      "enterPointSource": "WEB"
    }
  ],
  "ts": 1695797773370
}
```

### 推送数据参数

| 返回字段                          | 参数类型               | 字段说明                                                                                                                                                                   | 
|:------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                           | Object             | 订阅成功的频道                                                                                                                                                                |
| &gt; instType                 | String             | 产品类型                                                                                                                                                                   |
| &gt; channel                  | String             | 频道名                                                                                                                                                                    |
| &gt; instId                   | String             | 是                                                                                                                                                                      |
| action                        | String             | 推送数据动作, `snapshot` or `update`                                                                                                                                         |
| data                          | List&lt;Object&gt; | 订阅的数据                                                                                                                                                                  |
| &gt; instId                   | String             | 产品id 例如：ETHUSDT                                                                                                                                                        |
| &gt; orderId                  | String             | 订单ID                                                                                                                                                                   |
| &gt; clientOid                | String             | 自定义订单id                                                                                                                                                                |
| &gt; price                    | String             | 委托价格                                                                                                                                                                   |
| &gt; size                     | String             | 委托数量<br/>`side=buy` 时，该值为计价币数量<br/>`side=sell` 时，该值为基础币数量                                                                                                              |
| &gt; newSize                  | String             | - 当`orderType=limit`时，`newSize`表示base coin数量;<br/>当`orderType=market`且`side=buy`时，`newSize`表示quote coin数量；<br/>当`orderType=market`且`side=sell`时，`newSize`表示base coin数量 |
| &gt; notional                 | String             | 买入金额，市价买入时返回                                                                                                                                                           |
| &gt; ordType                  | String             | 订单类型，market：市价单 limit：限价单                                                                                                                                              |
| &gt; force                    | String             | 订单有效期，gtc普通限价单，一直有效直至取消；post_only 只做 maker 订单；fok全部成交或立即取消；ioc立即成交并取消剩余                                                                                                |
| &gt; side                     | String             | 订单方向                                                                                                                                                                   |
| &gt; fillPrice                | String             | 最新成交价格                                                                                                                                                                 |
| &gt; tradeId                  | String             | 最新成交ID                                                                                                                                                                 |
| &gt; baseVolume               | String             | 最新成交数量                                                                                                                                                                 |
| &gt; fillTime                 | String             | 最新成交时间      Unix毫秒时间戳，例如1690196141868                                                                                                                                  | 
| &gt; fillFee                  | String             | 最新数量                                                                                                                                                                   | 
| &gt; fillFeeCoin              | String             | 最新成交币种                                                                                                                                                                 | 
| &gt; tradeScope               | String             | 最新一笔成交的流动性方向 <br/>`T`:taker;<br/>`M`:maker;                                                                                                                            |
| &gt; accBaseVolume            | String             | 累计已成交数量                                                                                                                                                                |
| &gt; priceAvg                 | String             | 累计成交均价，如果成交数量为0，该字段也为0                                                                                                                                                 |
| &gt; status                   | String             | 订单状态<br/>`live`:新建订单;<br/>`partially_filled`:部分成交;<br/>`filled`:全部成交;<br/>`cancelled`: 已撤销;                                                                            |
| &gt; enterPointSource         | String             | 订单来源<br/>WEB    WEB客户端<br/>IOS    IOS客户端<br/>ANDROID    Andriod客户端<br/>API    API客户端<br/>SYS    系统, 通常为爆仓                                                              |
| &gt; feeDetail                | List&lt;Object&gt; | 手续费list                                                                                                                                                                |
| &gt;&gt; feeCoin              | String             | 交易手续费币种                                                                                                                                                                |
| &gt;&gt; fee                  | String             | 订单交易手续费，平台向用户收取的交易手续费 （仅订单，不包括折扣）                                                                                                                                      |
| &gt; cTime                    | String             | 订单创建时间，Unix时间戳的毫秒数格式，如 1630410492847                                                                                                                                   |
| &gt; uTime                    | String             | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085                                                                                                                                   |
| &gt; stpMode                  | String             | STP模式 <br/> `none` 不设置STP <br/> `cancel_taker` 取消taker单 <br/>  `cancel_maker` 取消maker单 <br/>  `cancel_both` 两者都取消                                                      |

</div>