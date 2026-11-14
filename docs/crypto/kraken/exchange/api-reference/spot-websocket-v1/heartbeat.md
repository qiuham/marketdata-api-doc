---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/heartbeat'
updated_at: 2026-11-13
---

# Heartbeat

> Server heartbeat sent when no subscription traffic is detected

WSS
ws.kraken.com
heartbeat

Server heartbeat sent if no subscription traffic within approximately 1 second. Heartbeats are only sent if there is an active connection with at least one subscription.

## Payload

**event** `string`

Value: `heartbeat`

```json Heartbeat theme={null}
{
  "event": "heartbeat"
}
```
