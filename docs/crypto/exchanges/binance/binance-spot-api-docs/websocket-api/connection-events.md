---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/connection-events
api_type: WebSocket
updated_at: 2026-05-27 18:55:02.113922
---

# Event format

[User Data Stream](/docs/binance-spot-api-docs/user-data-stream) events for non-SBE sessions are sent as JSON in **text frames** , one event per frame.

Events in [SBE sessions](/docs/binance-spot-api-docs/faqs/sbe_faq) will be sent as **binary frames**.

Please refer to [`userDataStream.subscribe`](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe) for details on how to subscribe to User Data Stream in WebSocket API.

Example of an event:
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "outboundAccountPosition",  
            "E": 1728972148778,  
            "u": 1728972148778,  
            "B": [  
                {  
                    "a": "BTC",  
                    "f": "11818.00000000",  
                    "l": "182.00000000"  
                },  
                {  
                    "a": "USDT",  
                    "f": "10580.00000000",  
                    "l": "70.00000000"  
                }  
            ]  
        }  
    }  
    

Event fields:

Name| Type| Mandatory| Description  
---|---|---|---  
`event`| OBJECT| YES| Event payload. See [User Data Streams](/docs/binance-spot-api-docs/user-data-stream)  
`subscriptionId`| INT| NO| Identifies which subscription the event is coming from. See [User Data Stream subscriptions](/docs/binance-spot-api-docs/websocket-api/event-format#general_info_user_data_stream_subscriptions)

---

# 事件格式

[用户数据流](/docs/zh-CN/binance-spot-api-docs/user-data-stream)中的非 SBE 会话事件以 JSON 格式在 **text 帧** 中发送，每帧一个事件。

[SBE 会话](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq)中的事件将作为 **二进制帧** 发送。

有关如何在 WebSocket API 中订阅用户数据流的详细信息，请参阅 [`订阅用户数据流`](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe)。

事件示例:
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "outboundAccountPosition",  
            "E": 1728972148778,  
            "u": 1728972148778,  
            "B": [  
                {  
                    "a": "BTC",  
                    "f": "11818.00000000",  
                    "l": "182.00000000"  
                },  
                {  
                    "a": "USDT",  
                    "f": "10580.00000000",  
                    "l": "70.00000000"  
                }  
            ]  
        }  
    }  
    

事件字段:

名称| 类型| 是否必须| 描述  
---|---|---|---  
`event`| OBJECT| YES| 事件 payload。请看 [用户数据流](/docs/zh-CN/binance-spot-api-docs/user-data-stream)  
`subscriptionId`| INT| NO| 用以标识事件来自于哪个订阅。详见 [用户数据流订阅](/docs/zh-CN/binance-spot-api-docs/websocket-api/event-format#general_info_user_data_stream_subscriptions)