---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Batch-Cancel-Order-Channel
api_type: WebSocket
updated_at: 2026-11-28 18:59:56.935668
---

# Batch Cancel Order Channel

### Description

:::tip

The ACK response only indicates that the request has been successfully accepted. Please use the [WebSocket order](/docs/uta/websocket/private/Order-Channel) push channel to confirm the actual order status of each cancellation.

:::

- This endpoint allows you to cancel multiple unfilled or partially filled orders across spot, margin, and futures markets via WebSocket.
- Each request supports cancellation of up to 20 orders.
- Batch order cancellation allows partial success. Each order in the batch is processed independently — if one cancellation fails, it does not affect the cancellation of the other orders in the same batch.
- In batch order cancellation, ensure that each call uses only orderId or clientOid for identification, and avoid mixing
  them. If orderId and clientOid are used together in one call, clientOid will be invalid.
- **Order Identification**: Orders can be identified by either `orderId` or `clientOid`. When both are provided, `orderId` takes priority.

Note: Please check the `code` and `msg` fields for each order in the response's `args` list to confirm the result of each cancellation. If the result is unclear, use `clientOid` or `orderId` to [query the order details](/docs/catalog/trading/order-management#get-order-details).

<div className="api-aligning">

```json title="Request Example"
{
    "args": [
        {
            "orderId": "xxxxxxxx"
        },
        {
            "orderId": "xxxxxxxx"
        }
    ],
    "id": "xxxxx-xxx-xxx-xxxx-xxxxxx",
    "op": "trade",
    "topic": "batch-cancel"
}
```

### Request Parameters

| Parameter      | Type               | Required | Description                                                                                                                              | 
|:---------------|:-------------------|----------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| op             | String             | Yes      | Operation: <br/> `trade` trade                                                                                                           |
| id             | String             | Yes      | Request identifier                                                                                                                       |
| topic          | String             | Yes      | Topic<br/>`batch-cancel`                                                                                                                 |
| args           | List&lt;Object&gt; | Yes      | Channel list                                                                                                                             |
| &gt; orderId   | String             | No       | Order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority         |
| &gt; clientOid | String             | No       | Client order ID<br/>Must match the regular expression `^[0-9A-Za-z_:#\-+\s]{1,32}$`, i.e. 1 to 32 characters, consisting of uppercase and lowercase letters, digits, underscores (_), hyphens (-), plus signs (+), colons (:), number signs (#), and spaces<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |

</div>


<div className="api-aligning">

```json title="Response Example"
{
  "event": "trade",
  "id": "bb553cc0-c1fa-454e-956d-c96c8d715760",
  "topic": "batch-cancel",
  "args": [
    {
      "code": "0",
      "msg": "Success",
      "orderId": "xxxxxxxxxxxxx",
      "clientOid": "xxxxxxxxxxxxx",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    },
    {
      "code": "25204",
      "msg": "Order does not exist",
      "orderId": "xxxxxxxxxxxxx",
      "clientOid": "xxxxxxxxxxxxx",
      "receiveTime": "1750034396999456",
      "pushTime": "1750034397077789"
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
  "ts": "1751980011084"
}
```

### Response Parameters

| Parameters     | Type               | Description               |
|:---------------|:-------------------|:--------------------------|
| event          | String             | Event<br/>`trade`/`error` |
| id             | String             | Request identifier        |
| topic          | String             | Topic<br/>`batch-cancel`  |
| args           | List&lt;Object&gt; | Channel list              |
| &gt; code      | String             | Code                      |
| &gt; msg       | String             | Message                   |
| &gt; orderId   | String             | Order ID                  |
| &gt; clientOid | String             | Client order ID           |
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

# 批量撤单

### 描述

:::tip

ACK 响应仅代表请求已被成功接收，请通过 [WebSocket 订单频道](/zh-CN/docs/uta/websocket/private/Order-Channel) 推送确认每笔撤单的实际状态。

:::

- 该接口支持通过 WebSocket 批量取消现货、合约、杠杆的未成交以及部分成交订单
- 每次请求最多支持撤销 20 笔
- 批量撤单允许部分成功。每笔订单独立处理——若某笔撤单失败，不影响同批次其他订单的撤销
- 在批量撤单操作中，请确保每次调用仅使用orderId或clientOid进行标识，避免混用。如果在一次调用中混合使用orderId和clientOid，则clientOid将失效
- **订单标识**：可通过 `orderId` 或 `clientOid` 识别订单。若两者同时传入，以 `orderId` 为准

注意：请检查响应 `args` 列表中每笔订单对应的 `code` 和 `msg` 字段，以确认每笔撤单的结果。若结果不明确，请使用 `clientOid` 或 `orderId` [查询订单详情](/zh-CN/docs/catalog/trading/order-management#get-order-details)。

<div className="api-aligning">

```json title="请求示例"
{
    "args": [
        {
            "orderId": "xxxxxxxx"
        },
        {
            "orderId": "xxxxxxxx"
        }
    ],
    "id": "xxxxx-xxx-xxx-xxxx-xxxxxx",
    "op": "trade",
    "topic": "batch-cancel"
}
```

### 请求参数

| 参数名            | 参数类型               | 是否必须 | 描述                                                                               | 
|:---------------|:-------------------|------|:---------------------------------------------------------------------------------|
| op             | String             | 是    | 操作: <br/> `trade` 交易                                                             |
| id             | String             | 是    | 请求标识                                                                             |
| topic          | String             | 是    | 频道名: <br/> `batch-cancel` 批量撤单                                                   |
| args           | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                        |
| &gt; orderId   | String             | 否    | 订单ID<br/>`orderId`及`clientOid`二者必传其一<br/>如果两者都传，则`orderId`优先级更高，忽略`clientOid`    |
| &gt; clientOid | String             | 否    | 自定义订单ID<br/>输入规则：`^[0-9A-Za-z_:#\-+\s]{1,32}$`，即 1 到 32 个字符，由大小写字母、数字、下划线(_)、连字符(-)、加号(+)、冒号(:)、井号(#)和空格组成<br/>`orderId`及`clientOid`二者必传其一<br/>如果两者都传，则`orderId`优先级更高，忽略`clientOid` |

</div>


<div className="api-aligning">

```json title="响应示例"
{
  "event": "trade",
  "id": "bb553cc0-c1fa-454e-956d-c96c8d715760",
  "topic": "batch-cancel",
  "args": [
    {
      "code": "0",
      "msg": "Success",
      "orderId": "xxxxxxxxxxxxx",
      "clientOid": "xxxxxxxxxxxxx",
      "receiveTime": "1750034396998123",
      "pushTime": "1750034397076456"
    },
    {
      "code": "25204",
      "msg": "Order does not exist",
      "orderId": "xxxxxxxxxxxxx",
      "clientOid": "xxxxxxxxxxxxx",
      "receiveTime": "1750034396999456",
      "pushTime": "1750034397077789"
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
  "ts": "1751980011084"
}
```

### 响应参数说明

| 返回字段           | 参数类型               | 字段说明                              |
|:---------------|:-------------------|:----------------------------------|
| event          | String             | 事件<br/>`trade` 交易<br/>`error`参数错误 |
| id             | String             | 请求标识                              |
| topic          | String             | 频道名<br/>`batch-cancel` 批量撤单       |
| args           | List&lt;Object&gt; | 订单列表                              |
| &gt; code      | String             | 状态码                               |
| &gt; msg       | String             | 状态消息                              |
| &gt; orderId   | String             | 订单ID                              |
| &gt; clientOid | String             | 自定义订单ID                           |
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