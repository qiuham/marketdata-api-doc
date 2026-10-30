---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-notification
anchor_id: overview-websocket-notification
api_type: WebSocket
updated_at: 2026-10-30 19:06:10.467542
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
    

  * WebSocket port 8443 retirement  

When a connection is established on port 8443, the notification message will be sent once after the handshake succeeds, indicating that port 8443 will soon be retired. The connection stays open. Users are encouraged to migrate to port 443.

> Response Example
    
    
    {
        "event": "notice",
        "code": "64010",
        "msg": "WebSocket port 8443 will be retired soon. Please migrate to port 443.",
        "connId": "d7d6f1f5"
    }
    

  
  
The `notice` message type is supported by all WebSocket endpoints (/ws/v5/public, /ws/v5/private, /ws/v5/business, and /ws/v5/public-sbe).

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
    

  * WebSocket 8443 端口下线

通过 8443 端口建立连接时，握手成功后会推送一次信息，告知用户 8443 端口即将下线。连接不会断开。用户需尽快迁移至 443 端口。

> 返回示例
    
    
    {
        "event": "notice",
        "code": "64010",
        "msg": "WebSocket port 8443 will be retired soon. Please migrate to port 443.",
        "connId": "d7d6f1f5"
    }
    

  
  
`notice` 消息类型目前支持所有WebSocket端点（/ws/v5/public、/ws/v5/private、/ws/v5/business和/ws/v5/public-sbe）。