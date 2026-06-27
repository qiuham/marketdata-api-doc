---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired
api_type: REST
updated_at: 2026-01-15T23:46:07.676510
---

# Event: User Data Stream Expired

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#event-description "Direct link to Event Description")

When the `listenKey` used for the user data stream turns expired, this event will be pushed.

**Notice:**

  * This event is not related to the websocket disconnection.
  * This event will be received only when a valid `listenKey` in connection got expired.
  * No more user data event will be updated after this event received until a new valid `listenKey` used.



## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#event-name "Direct link to Event Name")

`listenKeyExpired`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#response-example "Direct link to Response Example")
    
    
    {  
        'e': 'listenKeyExpired',      // event type  
        'E': 1576653824250              // event time  
    }

---

# listenKey过期推送

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#事件描述 "事件描述的直接链接")

当前连接使用的有效 listenKey 过期时，user data stream 将会推送此事件。

**注意:**

  * 此事件与 websocket 连接中断没有必然联系
  * 只有正在连接中的有效`listenKey`过期时才会收到此消息
  * 收到此消息后 user data stream 将不再更新，直到用户使用新的有效的`listenKey`



## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#事件类型 "事件类型的直接链接")

`listenKeyExpired`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired#响应示例 "响应示例的直接链接")
    
    
    {  
    	'e': 'listenKeyExpired',  // 事件类型  
    	'E': 1576653824250		  // 事件时间  
    }