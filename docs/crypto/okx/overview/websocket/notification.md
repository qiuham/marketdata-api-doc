---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-notification
anchor_id: overview-websocket-notification
api_type: WebSocket
updated_at: 2026-07-22 19:18:35.168856
---

# Notification

WebSocket has introduced a new message type (event = `notice`).   
  
  
  
Client will receive the information in the following scenarios:

  * Websocket disconnect for service upgrade  

60 seconds prior to the upgrade of the WebSocket service, the notification message will be sent to users indicating that the connection will soon be disconnected. Users are encouraged to establish a new connection to prevent any disruptions caused by disconnection.

> Response Example
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
The feature is supported by WebSocket Public (/ws/v5/public) and Private (/ws/v5/private) for now.

---

# 通知

WebSocket有一种消息类型(event=`notice`)。   
  
  
  
用户会在如下场景收到此类信息：

  * Websocket服务升级断线

在推送服务升级前60秒会推送信息，告知用户WebSocket服务即将升级。用户可以重新建立新的连接避免由于断线造成的影响。

> 返回示例
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
目前支持WebSocket公共频道(/ws/v5/public)和私有频道(/ws/v5/private)。