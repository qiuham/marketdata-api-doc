---
exchange: hyperliquid
source_url: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket/timeouts-and-heartbeats
api_type: WebSocket
updated_at: 2026-05-27 18:52:32.713792
---

# Timeouts and heartbeats

The server will close any connection if it hasn't sent a message to it in the last 60 seconds. If you are subscribing to a channel that doesn't receive messages every 60 seconds, you can send heartbeat messages to keep your connection alive. The format for these messages are:
    
    
    { "method": "ping" }

The server will respond with:
    
    
    { "channel": "pong" }