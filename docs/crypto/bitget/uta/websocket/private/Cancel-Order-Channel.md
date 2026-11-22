---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Cancel-Order-Channel
api_type: WebSocket
updated_at: 2026-11-22 19:00:40.407887
---

# Cancel Order Channel

### Description

:::tip

The ACK response only indicates that the request has been successfully accepted. Please use the [WebSocket order](/docs/uta/websocket/private/Order-Channel) push channel to confirm the actual order status after cancellation.

:::

This endpoint allows you to cancel a single unfilled or partially filled order across spot, margin, and futures markets, as well as Reality (rToken) stocks.

- Reality (rToken) rate limit<br/>
  The same as Crypto.

Note: If an unexpected error occurs when canceling an order, please check the `event` field (whether it is `trade` or `error`) in the response and use `clientOid` or `orderId` to [query the order details](/docs/catalog/trading/order-management#get-order-details) to confirm the final result of the operation.

- **Order Identification**: Orders can be identified by either `orderId` or `clientOid`. When both are provided, `orderId` takes priority.
- **Error Sample**: `{'event': 'error', 'code': 40015, 'msg': 'System is abnormal, please try again later', 'ts': 1785222459567}`
- Canceling an order may fail if the order has already been fully filled, has already been canceled, or the provided `orderId`/`clientOid` is invalid.

<div className="api-aligning">

```json title="Request Example"
{
    "args": [
        {
            "orderId": "xxxxxxxxxxxxxxxxxx",
            "clientOid": "xxxxxxxxxxxxxxxxxx"
        }
    ],
    "id": "c8a1999c-1f82-409d-870e-f40ff49c4072",
    "op": "trade",
    "topic": "cancel-order"
}
```

### Request Parameters

| Parameter      | Type               | Required | Description                                                                                                                                   | 
|:---------------|:-------------------|----------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| op             | String             | Yes      | Operation: <br/> `trade` trade                                                                                                                |
| id             | String             | Yes      | Request identifier                                                                                                                            |
| topic          | String             | Yes      | topic<br/>`cancel-order`                                                                                                                      |
| category       | String             | No       | Category (recommended)<br/>`spot`Spot<br/>`margin` Margin<br/> `usdt-futures` USDT futures<br/>`coin-futures` Coin futures<br/>`usdc-futures` USDC futures |
| args           | List&lt;Object&gt; | Yes      | Channel list                                                                                                                                  |
| &gt; orderId   | String             | No       | Order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority              |
| &gt; clientOid | String             | No       | Client order ID<br/>Must match the regular expression `^[0-9A-Za-z_:#\-+\s]{1,32}$`, i.e. 1 to 32 characters, consisting of uppercase and lowercase letters, digits, underscores (_), hyphens (-), plus signs (+), colons (:), number signs (#), and spaces<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority      |

</div>


<div className="api-aligning">

```json title="Response Example"
{
  "event": "trade",
  "id": "1750034870205",
  "topic": "cancel-order",
  "args": [
    {
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
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
  "ts": "1750034870597"
}
```

### Response Parameters

| Parameters     | Type               | Description                           |
|:---------------|:-------------------|:--------------------------------------|
| event          | String             | Event<br/>`trade`/`error`             |
| id             | String             | Request identifier                    |
| topic          | String             | Topic<br/>`cancel-order` cancel-order |
| args           | List&lt;Object&gt; | Channel list                          |
| &gt; orderId   | String             | Order ID                              |
| &gt; clientOid | String             | Client order ID                       |
| &gt; receiveTime | String           | Gateway receive time <br/>Unix microsecond timestamp |
| &gt; pushTime  | String             | Gateway push time <br/>Unix microsecond timestamp |
| code           | String             | Code                                  |
| msg            | String             | Message                               |
| connId         | String             | Connection ID                         |
| rateLimit      | Array              | Rate limit balance array              |
| &gt; limit     | String             | Rate limit quota for this dimension   |
| &gt; remaining | String             | Remaining available quota             |
| ts             | String             | Timestamp                             |

</div>

---

# 撤单

### 描述

:::tip

ACK 响应仅代表请求已被成功接收，请通过 [WebSocket 订单频道](/zh-CN/docs/uta/websocket/private/Order-Channel) 推送确认撤单后的实际订单状态。

:::

支持取消单独的现货、合约、杠杆以及 Reality（rToken）股票的未成交以及部分成交订单。

- Reality（rToken）限频<br/>
  与 Crypto 限频规则一致。

注意：若撤单时发生意外错误，请检查响应中的 `event` 字段（是否为 `trade` 或 `error`），并使用 `clientOid` 或 `orderId` [查询订单详情](/zh-CN/docs/catalog/trading/order-management#get-order-details) 以确认最终操作结果。

- **订单标识**：可通过 `orderId` 或 `clientOid` 识别订单。若两者同时传入，以 `orderId` 为准。
- **错误示例**：`{'event': 'error', 'code': 40015, 'msg': 'System is abnormal, please try again later', 'ts': 1785222459567}`
- 若订单已全部成交、已被撤销、或提供的 `orderId`/`clientOid` 无效，撤单可能失败。

<div className="api-aligning">

```json title="请求示例"
{
    "args": [
        {
            "orderId": "xxxxxxxxxxxxxxxxxx",
            "clientOid": "xxxxxxxxxxxxxxxxxx"
        }
    ],
    "id": "c8a1999c-1f82-409d-870e-f40ff49c4072",
    "op": "trade",
    "topic": "cancel-order"
}
```

### 请求参数

| 参数名             | 参数类型               | 是否必须 | 描述                                                                                                                 | 
|:----------------|:-------------------|----|:-------------------------------------------------------------------------------------------------------------------|
| op              | String             | 是  | 操作: <br/> `trade` 交易                                                                                               |
| id              | String             | 是  | 请求标识                                                                                                               |
| topic           | String             | 是  | 频道名<br/>`cancel-order` 撤单                                                                                          |
| category        | String             | 否  | 业务线（建议传入此参数） <br/>`spot`现货交易<br/>`margin` 杠杆交易<br/> `usdt-futures` U本位合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| args            | List&lt;Object&gt; | 是  | 请求订阅的频道列表                                                                                                          |
| &gt; orderId    | String             | 否  | 订单ID<br/>`orderId`及`clientOid`二者必传其一<br/>如果两者都传，则`orderId`优先级更高，忽略`clientOid`                                      |
| &gt; clientOid  | String             | 否  | 自定义订单ID<br/>输入规则：`^[0-9A-Za-z_:#\-+\s]{1,32}$`，即 1 到 32 个字符，由大小写字母、数字、下划线(_)、连字符(-)、加号(+)、冒号(:)、井号(#)和空格组成<br/>`orderId`及`clientOid`二者必传其一<br/>如果两者都传，则`orderId`优先级更高，忽略`clientOid`                                  |

</div>


<div className="api-aligning">

```json title="响应示例"
{
  "event": "trade",
  "id": "1750034870205",
  "topic": "cancel-order",
  "args": [
    {
      "orderId": "xxxxxxxx",
      "clientOid": "xxxxxxxx",
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
  "ts": "1750034870597"
}
```

### 响应参数说明

| 返回字段           | 参数类型               | 字段说明                              |
|:---------------|:-------------------|:----------------------------------|
| event          | String             | 事件<br/>`trade` 交易<br/>`error`参数错误 |
| id             | String             | 请求标识                              |
| topic          | String             | 频道名<br/>`cancel-order` 撤单         |
| args           | List&lt;Object&gt; | 订单列表                              |
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