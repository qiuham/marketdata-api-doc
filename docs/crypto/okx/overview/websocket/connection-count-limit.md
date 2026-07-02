---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-connection-count-limit
anchor_id: overview-websocket-connection-count-limit
api_type: WebSocket
updated_at: 2026-07-02 19:42:39.219626
---

# Connection count limit

The limit will be set at 30 WebSocket connections per specific WebSocket channel per sub-account. Each WebSocket connection is identified by the unique `connId`.

  

The WebSocket channels subject to this limitation are as follows:

  1. [Orders channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel)
  2. [Account channel](/docs-v5/en/#trading-account-websocket-account-channel)
  3. [Positions channel](/docs-v5/en/#trading-account-websocket-positions-channel)
  4. [Balance and positions channel](/docs-v5/en/#trading-account-websocket-balance-and-position-channel)
  5. [Position risk warning channel](/docs-v5/en/#trading-account-websocket-position-risk-warning)
  6. [Account greeks channel](/docs-v5/en/#trading-account-websocket-account-greeks-channel)

If users subscribe to the same channel through the same WebSocket connection through multiple arguments, for example, by using `{"channel": "orders", "instType": "ANY"}` and `{"channel": "orders", "instType": "SWAP"}`, it will be counted once only. If users subscribe to the listed channels (such as orders and accounts) using either the same or different connections, it will not affect the counting, as these are considered as two different channels. The system calculates the number of WebSocket connections per channel.

  

The platform will send the number of active connections to clients through the `channel-conn-count` event message **to new channel subscriptions**.

> Connection count update
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

When the limit is breached, generally the latest connection that sends the subscription request will be rejected. Client will receive the usual subscription acknowledgement followed by the `channel-conn-count-error` from the connection that the subscription has been terminated. In exceptional circumstances the platform may unsubscribe existing connections.

> Connection limit error
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

Order operations through WebSocket, including place, amend and cancel orders, are not impacted through this change.

---

# 连接限制

子账户维度，订阅每个 WebSocket 频道的最大连接数为 30 个。每个 WebSocket 连接都由唯一的 connId 标识。

  

受此限制的 WebSocket 频道如下：

  1. [订单频道](/docs-v5/zh/#order-book-trading-trade-ws-order-channel)
  2. [账户频道](/docs-v5/zh/#trading-account-websocket-account-channel)
  3. [持仓频道](/docs-v5/zh/#trading-account-websocket-positions-channel)
  4. [账户余额和持仓频道](/docs-v5/zh/#trading-account-websocket-balance-and-position-channel)
  5. [爆仓风险预警推送频道](/docs-v5/zh/#trading-account-websocket-position-risk-warning)
  6. [账户greeks频道](/docs-v5/zh/#trading-account-websocket-account-greeks-channel)

若用户通过不同的请求参数在同一个 WebSocket 连接下订阅同一个频道，如使用 `{"channel": "orders", "instType": "ANY"}` 和 `{"channel": "orders", "instType": "SWAP"}`，只算为一次连接。若用户使用相同或不同的 WebSocket 连接订阅上述频道，如订单频道和账户频道。在该两个频道之间，计数不会累计，因为它们被视作不同的频道。简言之，系统计算每个频道对应的 WebSocket 连接数量。

  

新链接订阅频道时，平台将对该订阅返回`channel-conn-count`的消息同步链接数量。

> 链接数量更新
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

当超出限制时，一般最新订阅的链接会收到拒绝。用户会先收到平时的订阅成功信息然后收到`channel-conn-count-error`消息，代表平台终止了这个链接的订阅。在异常场景下平台会终止已订阅的现有链接。

> 链接数量限制报错
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

通过 WebSocket 进行的订单操作，例如下单、修改和取消订单，不会受到此改动影响。