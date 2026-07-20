---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/websocket/websocket-rate-limits
api_type: WebSocket
updated_at: 2026-07-20 19:24:39.347511
---

# Advanced Trade WebSocket Rate Limits

The WebSocket feed is publicly available and its real-time market data updates provide the fastest insight into order flow and trades.

  * Advanced Trade API WebSocket connections are rate-limited at **8 per second per IP address**.
  * Advanced Trade API WebSocket unauthenticated messages are rate-limited at **8 per second per IP address**.

You are responsible for reading the message stream and using the messages relevant for your needs, such as building real-time order books and tracking real-time trades.

**See Also:**

  * [WebSocket Best Practices](/coinbase-app/advanced-trade-apis/guides/websocket)
  * [WebSocket Channels](/coinbase-app/advanced-trade-apis/websocket/websocket-channels)