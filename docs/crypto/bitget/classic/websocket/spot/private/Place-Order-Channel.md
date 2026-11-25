---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Place-Order-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:01:35.246501
---

# Place Order Channel

### Description

1.Rate limit will be shared with Rest API <br/>
2.Please connect to V2 Websocket domain: wss://ws.bitget.com/v2/ws/private <br/>
3.So far websocket trading doesn't support placing batch orders<br/>

<div className="api-aligning">

```json title="Request Example"
{
   "op":"trade",
   "args":[
      {
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instType":"SPOT",
         "instId":"BTCUSDT",
         "channel":"place-order",
         "params":{
            "orderType":"limit",
            "side":"buy",
            "size":"1",
            "price":"252",
            "force":"gtc",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ]
}
```

### Request Parameters

| Parameter          | Type               | Required | Description                                                                                                                                                                                                                           | 
|:-------------------|:-------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                 | String             | Yes      | "trade"                                                                                                                                                                                                                               |
| apiCode            | String             | No       | API rebate identifier                                                                                                                                                                                                                 |
| args               | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                                                                                                                                              |
| &gt; id            | String             | Yes      | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                                                                                                   |
| &gt; instType      | String             | Yes      | Product line type `SPOT`                                                                                                                                                                                                              |
| &gt; instId        | String             | Yes      | Product ID, e.g. `ETHUSDT`                                                                                                                                                                                                            |
| &gt; channel       | String             | Yes      | Channel name, `place-order`                                                                                                                                                                                                           |
| &gt; params        | Object             | Yes      |                                                                                                                                                                                                                                       |
| &gt;&gt; orderType | String             | Yes      | Order type<br/>`limit`: Limit order<br/>`market`: Market order                                                                                                                                                                        |
| &gt;&gt; side      | String             | Yes      | Order Direction<br/>`buy`: Buy<br/>`sell`: Sell                                                                                                                                                                                       |
| &gt;&gt; size      | String             | Yes      | Amount<br/>For Limit and Market-Sell orders, it represents the number of base coins.<br/>For Market-Buy orders, it represents the number of quote coins.<br/>The decimal places of amount can be got trough Get Symbol Info interface |
| &gt;&gt; force     | String             | Yes      | Execution strategy(It will be invalid when orderType is market) <br/>`gtc`：Normal limit order, good till cancelled<br/>`post_only`：Post only<br/>`fok`：Fill or kill<br/>`ioc`：Immediate or cancel                                     |
| &gt;&gt; price     | String             | No       | Limit price<br/>The decimal places of price and the price step can be returned by the Get Symbol Info interface                                                                                                                       |
| &gt;&gt; clientOid | String             | No       | Custom order ID.                                                                                                                                                                                                                      |
| &gt;&gt; stpMode   | String             | No       | STP Mode(Self Trade Prevention)<br/>`none`：not setting STP(default)<br/>`cancel_taker`：cancel taker order<br/>`cancel_maker`：cancel maker order<br/>`cancel_both`：cancel both of taker and maker orders                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"SPOT",
      "channel":"place-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### Response Parameters

| Parameter          | Type          | Description                                                                                                                                                                                                                           | 
|:-------------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event              | String        | Event<br/>`trade` <br/>`error`                                                                                                                                                                                                        |
| arg                | Object        | Channel                                                                                                                                                                                                                               |
| &gt; id            | String        | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                                                                                                   |
| &gt; instType      | String        | Product line type `SPOT`                                                                                                                                                                                                              |
| &gt; instId        | String        | Product ID, e.g. `ETHUSDT`                                                                                                                                                                                                            |
| &gt; channel       | String        | Channel name, `place-order`                                                                                                                                                                                                           |
| &gt; params        | Object        |                                                                                                                                                                                                                                       |
| &gt;&gt; orderId   | String        | Order ID.                                                                                                                                                                                                                             |
| &gt;&gt; orderType | String        | Order type<br/>`limit`: Limit order<br/>`market`: Market order                                                                                                                                                                        |
| &gt;&gt; side      | String        | Order Direction<br/>`buy`: Buy<br/>`sell`: Sell                                                                                                                                                                                       |
| &gt;&gt; size      | String        | Amount<br/>For Limit and Market-Sell orders, it represents the number of base coins.<br/>For Market-Buy orders, it represents the number of quote coins.<br/>The decimal places of amount can be got trough Get Symbol Info interface |
| &gt;&gt; force     | String        | Execution strategy(It will be invalid when orderType is market) <br/>`gtc`：Normal limit order, good till cancelled<br/>`post_only`：Post only<br/>`fok`：Fill or kill<br/>`ioc`：Immediate or cancel                                     |
| &gt;&gt; price     | String        | Limit price<br/>The decimal places of price and the price step can be returned by the Get Symbol Info interface                                                                                                                       |
| &gt;&gt; clientOid | String        | Custom order ID.                                                                                                                                                                                                                      |
| &gt;&gt; stpMode   | String        | STP Mode(Self Trade Prevention)<br/>`none`：not setting STP(default)<br/>`cancel_taker`：cancel taker order<br/>`cancel_maker`：cancel maker order<br/>`cancel_both`：cancel both of taker and maker orders                               |
| code               | String        | code                                                                                                                                                                                                                                  |
| msg                | String        | msg                                                                                                                                                                                                                                   |

</div>

---

# 下单频道

### 描述

1.限频与Rest API共享<br/>
2.使用时请求连接V2的websocket域名 wss://ws.bitget.com/v2/ws/private<br/>
3.暂时不支持批量下单，每次请求仅限一单<br/>

<div className="api-aligning">

```json title="请求示例"
{
   "op":"trade",
   "args":[
      {
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instType":"SPOT",
         "instId":"BTCUSDT",
         "channel":"place-order",
         "params":{
            "orderType":"limit",
            "side":"buy",
            "size":"1",
            "price":"252",
            "force":"gtc",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ]
}
```

### 请求参数

| 参数名                | 参数类型               | 是否必须 | 描述                                                                                                                     | 
|:-------------------|:-------------------|:-----|:-----------------------------------------------------------------------------------------------------------------------|
| op                 | String             | 是    | "trade"                                                                                                                |
| apiCode            | String             | 否    | API返佣标识                                                                                                                |
| args               | List&lt;Object&gt; | 是    | 请求参数列表                                                                                                                 |
| &gt; id            | String             | 是    | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                |
| &gt; instType      | String             | 是    | 产品类型 `SPOT`                                                                                                            |
| &gt; instId        | String             | 是    | 产品ID, 例如：`ETHUSDT`                                                                                                     |
| &gt; channel       | String             | 是    | 频道名, `place-order`                                                                                                     |
| &gt; params        | Object             | 是    |                                                                                                                        |
| &gt;&gt; orderType | String             | 是    | 订单类型<br/>`limit`: 限价<br/>`market`: 市价                                                                                  |
| &gt;&gt; side      | String             | 是    | 订单方向<br/>`buy`: 买<br/>`sell`: 卖                                                                                        |
| &gt;&gt; size      | String             | 是    | 数量<br/>对于Limit和Market-Sell订单，此参数表示base coin数量;<br/>对于Market-Buy订单，此参数表示quote coin数量；<br/>数量小数位可以通过获取交易对信息接口获取          |
| &gt;&gt; force     | String             | 是    | 执行策略（orderType为market时无效）<br/>`gtc`：普通限价单，一直有效直至取消<br/>`post_only`：只做 maker 订单<br/>`fok`：全部成交或立即取消<br/>`ioc`：立即成交并取消剩余 |
| &gt;&gt; price     | String             | 否    | 限价价格<br/>价格小数位、价格步长可以通过获取交易对信息接口获取                                                                                     |
| &gt;&gt; clientOid | String             | 否    | 自定义订单ID                                                                                                                |
| &gt;&gt; stpMode   | String             | 否    | STP（自成交预防）模式<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单<br/>`cancel_maker`：取消maker单<br/>`cancel_both`：两者都取消    |

</div>
<div className="api-br-10"></div>

<div className="api-aligning">

```json title="响应示例"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"SPOT",
      "channel":"place-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### 响应参数

| 返回字段               | 参数类型        | 字段说明                                                                                                                   | 
|:-------------------|:------------|:-----------------------------------------------------------------------------------------------------------------------|
| event              | String      | 事件<br/>`trade` 交易<br/>`error`参数错误                                                                                      |
| arg                | Object      | 订阅成功的频道                                                                                                                |
| &gt; id            | String      | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                |
| &gt; instType      | String      | 产品类型 `SPOT`                                                                                                            |
| &gt; instId        | String      | 产品ID, 例如：`ETHUSDT`                                                                                                     |
| &gt; channel       | String      | 频道名, `place-order`                                                                                                     |
| &gt; params        | Object      |                                                                                                                        |
| &gt;&gt; orderId   | String      | 订单ID.                                                                                                                  |
| &gt;&gt; orderType | String      | 订单类型<br/>`limit`: 限价<br/>`market`: 市价                                                                                  |
| &gt;&gt; side      | String      | 订单方向<br/>`buy`: 买<br/>`sell`: 卖                                                                                        |
| &gt;&gt; size      | String      | 数量<br/>对于Limit和Market-Sell订单，此参数表示base coin数量;<br/>对于Market-Buy订单，此参数表示quote coin数量；<br/>数量小数位可以通过获取交易对信息接口获取          |
| &gt;&gt; force     | String      | 执行策略（orderType为market时无效）<br/>`gtc`：普通限价单，一直有效直至取消<br/>`post_only`：只做 maker 订单<br/>`fok`：全部成交或立即取消<br/>`ioc`：立即成交并取消剩余 |
| &gt;&gt; price     | String      | 限价价格<br/>价格小数位、价格步长可以通过获取交易对信息接口获取                                                                                     |
| &gt;&gt; clientOid | String      | 自定义订单ID                                                                                                                |
| &gt;&gt; stpMode   | String      | STP（自成交预防）模式<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单<br/>`cancel_maker`：取消maker单<br/>`cancel_both`：两者都取消    |
| code               | String      | 状态码                                                                                                                    |
| msg                | String      | 状态消息                                                                                                                   |

</div>