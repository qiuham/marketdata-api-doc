---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/testnet/websocket-api/event-format
api_type: WebSocket
updated_at: 2026-01-15T23:36:49.034816
---

# Event format

[User Data Stream](/docs/binance-spot-api-docs/testnet/user-data-stream) events for non-SBE sessions are sent as JSON in **text frames** , one event per frame.

Events in [SBE sessions](/docs/binance-spot-api-docs/faqs/sbe_faq) will be sent as **binary frames**.

Please refer to [`userDataStream.subscribe`](/docs/binance-spot-api-docs/testnet/websocket-api/user-data-stream-requests#user-data-stream-subscribe) for details on how to subscribe to User Data Stream in WebSocket API.

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
`event`| OBJECT| YES| Event payload. See [User Data Streams](/docs/binance-spot-api-docs/testnet/user-data-stream)  
`subscriptionId`| INT| NO| Identifies which subscription the event is coming from. See [User Data Stream subscriptions](/docs/binance-spot-api-docs/testnet/websocket-api/event-format#general_info_user_data_stream_subscriptions)

---

# Event format

[User Data Stream](/docs/zh-CN/binance-spot-api-docs/testnet/user-data-stream) events for non-SBE sessions are sent as JSON in **text frames** , one event per frame.

Events in [SBE sessions](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq) will be sent as **binary frames**.

Please refer to [`userDataStream.subscribe`](/docs/zh-CN/binance-spot-api-docs/testnet/websocket-api/user-data-stream-requests#user-data-stream-subscribe) for details on how to subscribe to User Data Stream in WebSocket API.

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
`event`| OBJECT| YES| Event payload. See [User Data Streams](/docs/zh-CN/binance-spot-api-docs/testnet/user-data-stream)  
`subscriptionId`| INT| NO| Identifies which subscription the event is coming from. See [User Data Stream subscriptions](/docs/zh-CN/binance-spot-api-docs/testnet/websocket-api/event-format#general_info_user_data_stream_subscriptions)