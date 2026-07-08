---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-connect
anchor_id: overview-websocket-connect
api_type: WebSocket
updated_at: 2026-07-08 19:26:49.643561
---

# Connect

**Connection limit** : 3 requests per second (based on IP)

When subscribing to a public channel, use the address of the public service. When subscribing to a private channel, use the address of the private service

**Request limit** : 

The total number of 'subscribe'/'unsubscribe'/'login' requests per connection is limited to 480 times per hour.

If there’s a network problem, the system will automatically disable the connection. 

The connection will break automatically if the subscription is not established or data has not been pushed for more than 30 seconds. 

To keep the connection stable: 

1\. Set a timer of N seconds whenever a response message is received, where N is less than 30. 

2\. If the timer is triggered, which means that no new message is received within N seconds, send the String 'ping'. 

3\. Expect a 'pong' as a response. If the response message is not received within N seconds, please raise an error or reconnect.

---

# 连接

**连接限制** ：3 次/秒 (基于IP)

当订阅公有频道时，使用公有服务的地址；当订阅私有频道时，使用私有服务的地址

**请求限制** ：

每个连接 对于 `订阅`/`取消订阅`/`登录` 请求的总次数限制为 480 次/小时

如果出现网络问题，系统会自动断开连接

如果连接成功后30s未订阅或订阅后30s内服务器未向用户推送数据，系统会自动断开连接

为了保持连接有效且稳定，建议您进行以下操作：

1\. 每次接收到消息后，用户设置一个定时器，定时N秒，N 小于30。

2\. 如果定时器被触发（N 秒内没有收到新消息），发送字符串 'ping'。

3\. 期待一个文字字符串'pong'作为回应。如果在 N秒内未收到，请发出错误或重新连接。