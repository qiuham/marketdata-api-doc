---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Cancel-Order-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:02:45.404064
---

# Cancel Order Channel

### Description

- Cancel order

<div className="api-aligning">

```json title="Request Example"
{
   "args":[
      {
         "channel":"cancel-order",
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instId":"BTCUSDT",
         "instType":"USDT-FUTURES",
         "params":{
            "orderId":"xxxxxxxxxx",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ],
   "op":"trade"
}
```

### Request Parameters

| Parameter            | Type               | Required | Description                                                                                              | 
|:---------------------|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------|
| op                   | String             | Yes      | "trade"                                                                                                  |
| args                 | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                 |
| &gt; id              | String             | Yes      | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                      |
| &gt; instType        | String             | Yes      | Product line type `USDT-FUTURES`                                                                         |
| &gt; instId          | String             | Yes      | Product ID, e.g. `ETHUSDT`                                                                               |
| &gt; channel         | String             | Yes      | Channel name, `cancel-order`                                                                             |
| &gt; params          | Object             | Yes      |                                                                                                          |
| &gt;&gt; orderId     | String             | No       | Order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails.        |
| &gt;&gt; clientOid   | String             | No       | Custom order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails. |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Fail Response Example"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"USDT-FUTURES",
      "channel":"cancel-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### Response Parameters

| Parameter          | Type       | Description                                                                                              | 
|:-------------------|:-----------|:---------------------------------------------------------------------------------------------------------|
| event              | String     | Event<br/>`trade` <br/>`error`                                                                           |
| arg                | Object     | Channel                                                                                                  |
| &gt; id            | String     | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                      |
| &gt; instType      | String     | Product line type `USDT-FUTURES`                                                                         |
| &gt; instId        | String     | Product ID, e.g. `ETHUSDT`                                                                               |
| &gt; channel       | String     | Channel name, `cancel-order`                                                                             |
| &gt; params        | Object     |                                                                                                          |
| &gt;&gt; orderId   | String     | Order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails.        |
| &gt;&gt; clientOid | String     | Custom order ID <br/> Either `orderId` or `clientOid` is required.If both are present, orderId prevails. |
| code               | String     | code                                                                                                     |
| msg                | String     | msg                                                                                                      |

</div>

---

# 撤销订单频道

### 描述

- 合约撤销订单

<div className="api-aligning">

```json title="请求示例"
{
   "args":[
      {
         "channel":"cancel-order",
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instId":"BTCUSDT",
         "instType":"USDT-FUTURES",
         "params":{
            "orderId":"xxxxxxxxxx",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ],
   "op":"trade"
}
```

### 请求参数

| 参数名                   | 参数类型               | 是否必须 | 描述                                                          | 
|:----------------------|:-------------------|:-----|:------------------------------------------------------------|
| op                    | String             | 是    | "trade"                                                     |
| args                  | List&lt;Object&gt; | 是    | 请求参数列表                                                      |
| &gt; id               | String             | 是    | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");     |
| &gt; instType         | String             | 是    | 产品类型 `USDT-FUTURES`                                         |
| &gt; instId           | String             | 是    | 产品ID, 例如：`ETHUSDT`                                          |
| &gt; channel          | String             | 是    | 频道名, `cancel-order`                                          |
| &gt; params           | Object             | 是    |                                                             |
| &gt;&gt; orderId      | String             | 否    | 订单ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId`    |
| &gt;&gt; clientOid    | String             | 否    | 用户自定义ID <br/> `orderId`与`clientOid`二选一必传，如果两者都传，优先`orderId` |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="响应示例"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"USDT-FUTURES",
      "channel":"cancel-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### 响应参数

| 返回字段                         | 参数类型         | 字段说明                                                    | 
|:-----------------------------|:-------------|:--------------------------------------------------------|
| event                        | String       | 事件<br/>`trade` 交易<br/>`error`参数错误                       |
| arg                          | Object       | 订阅成功的频道                                                 |
| &gt; id                      | String       | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$"); |
| &gt; instType                | String       | 产品类型 `USDT-FUTURES`                                     |
| &gt; instId                  | String       | 产品ID, 例如：`ETHUSDT`                                      |
| &gt; channel                 | String       | 频道名, `cancel-order`                                     |
| &gt; params                  | Object       |                                                         |
| &gt;&gt; orderId             | String       | 订单ID                                                    |
| &gt;&gt; clientOid           | String       | 自定义订单ID                                                 |
| code                         | String       | 状态码                                                     |
| msg                          | String       | 状态消息                                                    |

</div>