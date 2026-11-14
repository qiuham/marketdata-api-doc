---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: hyperliquid
provider_name: Hyperliquid
product: api
product_id: hyperliquid
source_url: 'https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket/timeouts-and-heartbeats'
updated_at: 2026-11-13
---

# Timeouts and heartbeats

This page describes the measures to keep WebSocket connections alive.

The server will close any connection if it hasn't sent a message to it in the last 60 seconds. If you are subscribing to a channel that doesn't receive messages every 60 seconds, you can send heartbeat messages to keep your connection alive. The format for these messages are:

```json
{ "method": "ping" }
```

The server will respond with:

```json
{ "channel": "pong" }
```
