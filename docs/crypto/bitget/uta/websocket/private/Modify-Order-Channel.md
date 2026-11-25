---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Modify-Order-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:02:09.717819
---

# Modify Order Channel

### Description

**Asynchronous Order Modification:**
- Order modifications are executed asynchronously. Even after receiving a successful acknowledgment (ACK) response, the final modification may still fail.
- No additional notification will be sent in case of failure, but you may receive order fill or cancellation updates (e.g., if the order is canceled or fully filled before the modification request takes effect).
- It is recommended to query the current order status via REST API to confirm whether the modification was successful: If the order still exists, you can retry; if it does not exist, it indicates the order has been filled or canceled, and no further action is needed.

<div className="api-aligning">

```json title="Request Example"
{
    "args": [
        {
            "autoCancel": "yes",
            "clientOid": "135423791666666666",
            "orderId": "1354237910666666666",
            "price": "5",
            "qty": "2",
            "requestId": 12345678,
            "symbol":"BTCUSDT"
        }
    ],
    "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
    "op": "trade",
    "category": "usdt-futures",
    "topic": "modify-order"
}
```

### Request Parameters

| Parameter       | Type               | Required | Description                                                                                                                                                                                           | 
|:----------------|:-------------------|----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op              | String             | Yes      | Operation: <br/> `trade`                                                                                                                                                                              |
| id              | String             | Yes      | Request identifier                                                                                                                                                                                    |
| topic           | String             | Yes      | Topic<br/> `modify-order`                                                                                                                                                                             |
| category        | String             | No       | Business line, **lowercase only**<br/>`spot` Spot trading<br/>`margin` Margin trading<br/> `usdt-futures` USDT Futures<br/>`coin-futures` Coin-M futures<br/>`usdc-futures` USDC Futures                                 |
| args            | List&lt;Object&gt; | Yes      | Channel list                                                                                                                                                                                          |
| &gt; orderId    | String             | No       | Order ID <br/>Either orderId or clientOid is required.<br/>If both orderId and clientOid are passed simultaneously, orderId takes higher priority, and the clientOid parameter will be ignored.       |
| &gt; clientOid  | String             | No       | Client order ID<br/>Either orderId or clientOid is required.<br/>If both orderId and clientOid are passed simultaneously, orderId takes higher priority, and the clientOid parameter will be ignored. |
| &gt; qty        | String             | No       | Order quantity<br/>- Spot<br/> For market buy orders, the unit is quote coin <br/>For limit and market sell orders, the unit is base coin <br/>- Futures<br/>The unit is base coin                    |
| &gt; price      | String             | No       | Order price<br/>This field is required when orderType is `limit`                                                                                                                                      |
| &gt; autoCancel | String             | No       | Will the original order be canceled if the order modification fails<br/>`yes`: Cancel <br/>`no`: Not cancel（default）<br/>When set to `yes`: if the matching engine fails to modify the order, the order is cancelled immediately; after cancellation, the counter will reject any further modification requests for that order (including in-flight and new requests). |
| &gt; symbol     | String             | No       | Symbol name, case-insensitive                                                                                                                                                                                           |
| &gt; requestId  | Number             | No       | Custom request ID used to identify the order modification request<br/>Only supports numbers within 18 digits<br/>Returned when autoCancel=yes and the modify order request is rejected                                                                                                            |
| &gt; pxAmendType | String           | No       | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

</div>


<div className="api-aligning">

```json title="Response Example"
{
  "event": "trade",
  "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
  "topic": "modify-order",
  "args": [
    {
      "orderId": "135423791666666666",
      "clientOid": "1354237910666666666",
      "requestId": 12345678,
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    }
  ],
  "code": "0",
  "msg": "Success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1758601481031"
}
```

### Response Parameters

| Parameters     | Type               | Description               |
|:---------------|:-------------------|:--------------------------|
| event          | String             | Event<br/>`trade`/`error` |
| id             | String             | Request identifier        |
| topic          | String             | Topic<br/>`modify-order`  |
| args           | List&lt;Object&gt; | Channel list              |
| &gt; orderId   | String             | Order ID                  |
| &gt; clientOid | String             | Client order ID           |
| &gt; requestId | Number             | Custom request ID<br/>Only returned when passed in the modify-order request |
| &gt; receiveTime | String           | Gateway receive time <br/>Unix microsecond timestamp |
| &gt; pushTime  | String             | Gateway push time <br/>Unix microsecond timestamp |
| code           | String             | Code                      |
| msg            | String             | Message                   |
| connId         | String             | Connection ID             |
| rateLimit      | Array              | Rate limit balance array  |
| &gt; limit     | String             | Rate limit quota for this dimension |
| &gt; remaining | String             | Remaining available quota |
| ts             | String             | Timestamp                 |

</div>

---

# 修改订单

### 描述

**异步改单说明：**
- 改单为异步执行，收到成功响应后仍可能最终失败
- 失败时不会收到额外通知，但可能收到订单成交或撤销的更新（例如，订单在改单请求生效前被取消或完全成交）
- 建议通过REST API查询当前订单状态来确认改单是否成功：如订单仍存在则可重试；如不存在则说明已成交或撤销，无需再操作

<div className="api-aligning">

```json title="请求示例"
{
    "args": [
        {
            "autoCancel": "yes",
            "clientOid": "135423791666666666",
            "orderId": "1354237910666666666",
            "price": "5",
            "qty": "2",
            "requestId": 12345678,
            "symbol":"BTCUSDT"
        }
    ],
    "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
    "op": "trade",
    "category": "usdt-futures",
    "topic": "modify-order"
}
```

### 请求参数

| 参数名             | 参数类型               | 是否必须 | 描述                                                                                                                 | 
|:----------------|:-------------------|------|:-------------------------------------------------------------------------------------------------------------------|
| op              | String             | 是    | 操作: <br/> `trade` 交易                                                                                               |
| id              | String             | 是    | 请求标识                                                                                                               |
| topic           | String             | 是    | 频道名: <br/> `modify-order` 修改订单                                                                                     |
| category        | String             | 否    | 业务线,**仅接受小写**<br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| args            | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                                          |
| &gt; orderId    | String             | 否    | 订单id<br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高，忽略clientOid入参                            |
| &gt; clientOid  | String             | 否    | 自定义订单id <br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高，忽略clientOid入参                        |
| &gt; qty        | String             | 否    | 下单数量<br/> - 现货<br/> 市价买单，单位为quote coin<br/>限价及市价卖单，单位为base coin <br/>- 合约<br/>单位为base coin                         |
| &gt; price      | String             | 否    | 下单价格<br/>订单类型为限价单`limit`时，该字段必填<br/>订单类型为市价单`market`时，该字段失效                                                        |
| &gt; autoCancel | String             | 否    | 修改订单失败是否撤销原订单<br/>`yes`撤销<br/>`no`不撤销<br/>若设置为 `yes`：撮合改单失败后，直接执行撤单；撤单后，柜台将拒绝该订单的后续改单请求（含在途及新请求）。 |
| &gt; symbol     | String             | 否    | 交易对名称,**不区分大小写**                                                                                                              |
| &gt; requestId  | Number             | 否    | 自定义requestId，用于标识改单请求<br/>只支持18位以内的数字<br/>当 autoCancel=yes 且改单请求被拒绝时会返回                                                                                        |
| &gt; pxAmendType | String           | 否    | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

</div>


<div className="api-aligning">

```json title="响应示例"
{
  "event": "trade",
  "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
  "topic": "modify-order",
  "args": [
    {
      "orderId": "135423791666666666",
      "clientOid": "1354237910666666666",
      "requestId": 12345678,
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    }
  ],
  "code": "0",
  "msg": "Success",
  "connId": "xxxxxxxxxx",
  "rateLimit": [
    {
      "limit": "10",
      "remaining": "9"
    }
  ],
  "ts": "1758601481031"
}
```

### 响应参数说明

| 返回字段           | 参数类型               | 字段说明                              |
|:---------------|:-------------------|:----------------------------------|
| event          | String             | 事件<br/>`trade` 交易<br/>`error`参数错误 |
| id             | String             | 请求标识                              |
| topic          | String             | 频道名<br/>`modify-order`修改订单        |
| args           | List&lt;Object&gt; | 订单列表                              |
| &gt; orderId   | String             | 订单ID                              |
| &gt; clientOid | String             | 自定义订单ID                           |
| &gt; requestId | Number             | 自定义requestId<br/>仅在改单请求中传入该参数时才返回  |
| &gt; receiveTime | String           | 网关接收时间 <br/>Unix微秒时间戳             |
| &gt; pushTime  | String             | 网关推送时间 <br/>Unix微秒时间戳             |
| code           | String             | 状态码                               |
| msg            | String             | 状态消息                              |
| connId         | String             | 连接ID                              |
| rateLimit      | Array              | 限频余额数组                            |
| &gt; limit     | String             | 该维度限额                             |
| &gt; remaining | String             | 剩余可用次数                            |
| ts             | String             | 时间戳                               |

</div>