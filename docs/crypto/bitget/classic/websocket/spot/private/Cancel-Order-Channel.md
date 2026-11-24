---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/private/Cancel-Order-Channel
api_type: WebSocket
updated_at: 2026-11-24 19:00:44.718952
---

# Cancel Order Channel

### Description

1.Rate limit will be shared with Rest API <br/>
2.Please connect to V2 Websocket domain: wss://ws.bitget.com/v2/ws/private <br/>
3.So far websocket trading doesn't support canceling batch orders<br/>

<div className="api-aligning">

```json title="Request Example"
{
   "op":"trade",
   "args":[
      {
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instType":"SPOT",
         "instId":"BTCUSDT",
         "channel":"cancel-order",
         "params":{
            "orderId":"xxxxxxxxx",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ]
}
```

### Request Parameters

| Parameter          | Type               | Required | Description                                                                                              | 
|:-------------------|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------|
| op                 | String             | Yes      | "trade"                                                                                                  |
| args               | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                 |
| &gt; id            | String             | Yes      | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                      |
| &gt; instType      | String             | Yes      | Product line type `SPOT`                                                                                 |
| &gt; instId        | String             | Yes      | Product ID, e.g. `ETHUSDT`                                                                               |
| &gt; channel       | String             | Yes      | Channel name, `cancel-order`                                                                             |
| &gt; params        | Object             | Yes      |                                                                                                          |
| &gt;&gt; orderId   | String             | No       | Order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails.        |
| &gt;&gt; clientOid | String             | No       | Custom order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails. |

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
      "channel":"cancel-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### Response Parameters

| Parameter          | Type         | Description                                                                                              | 
|:-------------------|:-------------|:---------------------------------------------------------------------------------------------------------|
| event              | String       | Event<br/>`trade` <br/>`error`                                                                           |
| arg                | Object       | Channel                                                                                                  |
| &gt; id            | String       | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                      |
| &gt; instType      | String       | Product line type `SPOT`                                                                                 |
| &gt; instId        | String       | Product ID, e.g. `ETHUSDT`                                                                               |
| &gt; channel       | String       | Channel name, `cancel-order`                                                                             |
| &gt; params        | Object       |                                                                                                          |
| &gt;&gt; orderId   | String       | Order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails.        |
| &gt;&gt; clientOid | String       | Custom order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails. |
| code               | String       | code                                                                                                     |
| msg                | String       | msg                                                                                                      |

</div>

---

# 撤销订单频道

### 描述

1.限频与Rest API共享<br/>
2.使用时请求连接V2的websocket域名 wss://ws.bitget.com/v2/ws/private<br/>
3.暂时不支持批量撤单，每次请求仅限一单<br/>

<div className="api-aligning">

```json title="请求示例"
{
   "op":"trade",
   "args":[
      {
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instType":"SPOT",
         "instId":"BTCUSDT",
         "channel":"cancel-order",
         "params":{
            "orderId":"xxxxxxxxx",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ]
}
```

### 请求参数

| 参数名                | 参数类型               | 是否必须 | 描述                                                          | 
|:-------------------|:-------------------|:-----|:------------------------------------------------------------|
| op                 | String             | 是    | "trade"                                                     |
| args               | List&lt;Object&gt; | 是    | 请求参数列表                                                      |
| &gt; id            | String             | 是    | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");     |
| &gt; instType      | String             | 是    | 产品类型 `SPOT`                                                 |
| &gt; instId        | String             | 是    | 产品ID, 例如：`ETHUSDT`                                          |
| &gt; channel       | String             | 是    | 频道名, `cancel-order`                                         |
| &gt; params        | Object             | 是    |                                                             |
| &gt;&gt; orderId   | String             | 否    | 订单ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId`    |
| &gt;&gt; clientOid | String             | 否    | 用户自定义ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId` |

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
      "channel":"cancel-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### 响应参数

| 返回字段               | 参数类型                | 字段说明                                                        | 
|:-------------------|:--------------------|:------------------------------------------------------------|
| event              | String              | 事件<br/>`trade` 交易<br/>`error`参数错误                           |
| arg                | Object              | 订阅成功的频道                                                     |
| &gt; id            | String              | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");     |
| &gt; instType      | String              | 产品类型 `SPOT`                                                 |
| &gt; instId        | String              | 产品ID, 例如：`ETHUSDT`                                          |
| &gt; channel       | String              | 频道名, `cancel-order`                                          |
| &gt; params        | Object              |                                                             |
| &gt;&gt; orderId   | String              | 订单ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId`    |
| &gt;&gt; clientOid | String              | 用户自定义ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId` |
| code               | String              | 状态码                                                         |
| msg                | String              | 状态消息                                                        |

</div>