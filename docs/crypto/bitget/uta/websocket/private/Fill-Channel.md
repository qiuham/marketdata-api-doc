---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Fill-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:36:55.826974
---

# Fill Channel

### Description
Push real-time fill data.

Push rules:
1. No push on first-time subscription
2. Push when spot/leveraged/futures orders are filled

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "fill"
        }
    ]
}
```

### Request Parameters


| Parameters    |  Type         | Description                                    |
|:--------------|:-----------------------|:-----------------------------------------------|
| op            | String                 | Operation: <br/> `subscribe` /`unsubscribe`    |
| args          | List&lt;Object&gt;     | Subscribed channel                             |
| &gt; instType | String                 | Product type<br/>`UTA` Unified trading account |
| &gt; topic    | String                 | Topic <br/>`fill`                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "UTA",
        "topic": "fill"
    },
    "connId": "xxxxxxxxxx"
}
```
### Response Parameters

| Parameters    |  Type   | Description                                            | 
|:-----------------|:-----------------|:-------------------------------------------------------|
| event            | String           | Operation <br/>`subscribe` / `unsubscribe` / `error`   |
| arg              | Object           | Subscribed channel                                     |
| &gt; instType    | String           | Product type <br/>`UTA`                                |
| &gt; topic       | String           | Topic <br/>`fill`                               |
| code             | String           | Error code                                             |
| msg              | String           | Error message                                          |
| connId           | String           | Connection ID                                          |


</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderType": "market",
      "updatedTime": "1736378720623",
      "side": "buy",
      "orderId": "1288888888888888888",
      "execPnl": "0",
      "feeDetail": [
        {
          "feeCoin": "USDT",
          "fee": "0.569958"
        }
      ],
      "execTime": "1736378720623",
      "tradeScope": "taker",
      "tradeSide": "open",
      "execId": "1288888888888888888",
      "execLinkId": "1288888888888888888",
      "execPrice": "94993",
      "holdSide": "long",
      "execValue": "949.93",
      "category": "usdt-futures",
      "execQty": "0.01",
      "clientOid": "1288888888888888889",
      "isRPI": "no"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "fill"
  },
  "action": "snapshot",
  "ts": 1733904123981
}
```


### Push Parameters

| Parameters         | Type               | Description                                                                                                                                                                  |
|:-------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                | Object             | Subscribed channel                                                                                                                                                           |
| &gt; instType      | String             | product type <br/>`UTA` Unified trading account                                                                                                                              |
| &gt; topic         | String             | Topic <br/>`fill` fill                                                                                                                                                       |
| action             | String             | Action <br/>`snapshot` Full data                                                                                                           |
| data               | List&lt;Object&gt; | Subscribed data                                                                                                                                                              |
| &gt; category      | String             | Product type <br/> `spot` Spot trading <br/> `margin` Margin trading <br/> `usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; orderId       | String             | Order ID                                                                                                                                                                     |
| &gt; clientOid     | String             | Client Order ID                                                                                                                                                              |
| &gt; execId        | String             | Fill ID                                                                                                                                                                      |
| &gt; execLinkId    | String             | Execution correlation ID                                                                                                                                                                      |
| &gt; symbol        | String             | Symbol name                                                                                                                                                                  |
| &gt; orderType     | String             | Order type <br/>`limit`/`market`                                                                                                                                             |
| &gt; side          | String             | Trade side<br/>`buy`/`sell`                                                                                                                                                  |
| &gt; holdSide      | String             | Position direction <br/>`long`: Long <br/>`short`: Short                                                                                                                     |
| &gt; tradeSide     | String             | Trade side <br/>`open`/`close`    <br/>Detailed enumerations can be obtained on the Enumeration page.                                                                              |
| &gt; execPrice     | String             | Fill price                                                                                                                                                                   |
| &gt; execQty       | String             | Fill quantity<br/>_The unit is base coin_                                                                                                                                    |
| &gt; execValue     | String             | Fill value<br/>_The unit is quote coin_                                                                                                                                      |
| &gt; execPnl       | String             | Execution profit and loss                                                                                                                                                    |
| &gt; tradeScope    | String             | Trade scope<br/>`taker`/`maker`                                                                                                                                              |
| &gt; feeDetail     | String             | Fee detail                                                                                                                                                                   |
| &gt;&gt; feeCoin   | String             | Fee coin                                                                                                                                                                     |
| &gt;&gt; fee       | String             | Total fee                                                                                                                                                                    |
| &gt; execTime      | String             | Execution timestamp <br/>Generated by the matching engine<br/>A Unix timestamp in milliseconds. e.g.,`1622697148123`                                                                                                 |
| &gt; updatedTime   | String             | Updated timestamp<br/>Generated by OMS<br/>A Unix timestamp in milliseconds. e.g.,`1622697148123`                                                                                                    |
| &gt; isRPI         | String             | Whether it is an RPI fill<br/>`yes` Yes<br/>`no` No                                                                                                                             |


</div>

---

# 成交

### 描述
实时推送用户成交信息


推送规则：
1. 首次订阅不推送
2. 统一账户现货/杠杆/合约委托单成交,推送

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "fill"
        }
    ]
}
```

### 请求参数说明

| 参数名           | 参数类型               | 是否必须 | 描述                                                                 | 
|:--------------|:-------------------|------|:-------------------------------------------------------------------|
| op            | String             | 是    | 操作: <br/> `subscribe` 订阅 <br/>`unsubscribe` 取消订阅                   |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                          |
| &gt; instType | String             | 是    | 产品类型<br/>`UTA` 统一账户                                                |
| &gt; topic    | String             | 是    | 频道名: `fill` 成交                                                     |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅响应示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "fill"
  },
  "connId": "xxxxxxxxxx"
}
```
### 返回参数说明

| 返回字段          | 参数类型     | 字段说明                                                            | 
|:--------------|:---------|:----------------------------------------------------------------|
| event         | String   | 操作 <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误 |
| arg           | Object   | 订阅的频道                                                           |
| &gt; instType | String   | 产品类型<br/>`UTA` 统一账户                                             |
| &gt; topic    | String   | 频道名 <br/>`fill` 成交                                              |
| code          | String   | 错误码                                                             |
| msg           | String   | 错误消息                                                            |
| connId        | String   | 连接ID                                                            |


</div>

<div className="api-br-10"></div>


<div className="api-aligning">

```json title="推送示例"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderType": "market",
      "updatedTime": "1736378720623",
      "side": "buy",
      "orderId": "1288888888888888888",
      "execPnl": "0",
      "feeDetail": [
        {
          "feeCoin": "USDT",
          "fee": "0.569958"
        }
      ],
      "execTime": "1736378720623",
      "tradeScope": "taker",
      "tradeSide": "open",
      "execId": "1288888888888888888",
      "execLinkId": "1288888888888888888",
      "execPrice": "94993",
      "holdSide": "long",
      "execValue": "949.93",
      "category": "usdt-futures",
      "execQty": "0.01",
      "clientOid": "1288888888888888889",
      "isRPI": "no"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "fill"
  },
  "action": "snapshot",
  "ts": 1736378720653
}
```


### 推送参数说明

| 属性名               | 类型                 | 描述                                                                                                            |
|:------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------|
| arg               | Object             | 订阅成功频道                                                                                                        |
| &gt; instType     | String             | 产品线类型<br/>`UTA`统一账户                                                                                           |
| &gt; topic        | String             | 频道名<br/>`fill`成交频道                                                                                            |
| action            | String             | 推送数据动作<br/>`snapshot`全量                                                                                       |
| data              | List&lt;Object&gt; | 订阅的数据                                                                                                         |
| &gt; category     | String             | 业务线 <br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约 <br/>`usdc-futures` USDC合约 |
| &gt; orderId      | String             | 订单ID                                                                                                          |
| &gt; clientOid    | String             | 客户端订单ID                                                                                                       |
| &gt; execId       | String             | 成交ID                                                                                                          |
| &gt; execLinkId   | String             | 成交关联ID                                                                                                          |
| &gt; symbol       | String             | 交易对名称                                                                                                         |
| &gt; orderType    | String             | 订单类型 <br/>`limit` :限价<br/> `market` : 市价                                                                      |
| &gt; side         | String             | 委托方向 <br/>`buy`: 买<br/>`sell`: 卖                                                                              |
| &gt; holdSide     | String             | 持仓方向 <br/>`long`:多 <br/> `short` :空                                                                           |
| &gt; tradeSide    | String             | 交易方向 <br/>`open`: 开 <br/> `close` : 平     <br/>详细枚举可以在 枚举 页面获取                                                                              |
| &gt; execPrice    | String             | 成交价格                                                                                                          |
| &gt; execQty      | String             | 成交数量                                                                                                          |
| &gt; execValue    | String             | 成交总额                                                                                                          |
| &gt; execPnl      | String             | 成交盈亏                                                                                                          |
| &gt; tradeScope   | String             | 交易者标识<br/>`taker`: 吃单方<br/>`maker`: 挂单方                                                                       |
| &gt; feeDetail    | String             | 手续费明细                                                                                                         |
| &gt;&gt; feeCoin  | String             | 手续费币种                                                                                                         |
| &gt;&gt; fee      | String             | 总计手续费                                                                                                         |
| &gt; execTime     | String             | 成交时间 <br/> 生成于撮合<br/> Unix毫秒时间戳，例如1622697148123                                                                          |
| &gt; updatedTime  | String             | 更新时间 <br/> 生成于OMS<br/>Unix毫秒时间戳，例如1622697148123                                                                          |
| &gt; isRPI        | String             | 是否为RPI类型成交<br/>`yes` 是<br/>`no` 否                                                                               |


</div>