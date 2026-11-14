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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/systemstatus'
updated_at: 2026-11-13
---

# System Status

> Server-pushed system status on connection or status changes

WSS
ws.kraken.com
systemStatus

Status sent on connection or system status changes. This is a server-initiated message — no subscription is required.

## Payload

**event** `string`

Value: `systemStatus`

**status** `string`

One of: `online`, `cancel_only`, `maintenance`, `post_only`

The status of the trading engine.

* `online`: Markets are operating normally - all order types may be submitted and order matching can occur.
* `maintenance`: Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
* `cancel_only`: Orders can be cancelled but new orders cannot be placed. No order matching will occur.
* `post_only`: Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.

**version** `string`

The version of the websockets service.

**connectionID** `integer`

A unique connection identifier (for debugging).

```json System Status theme={null}
{
  "connectionID": 8628615390848610000,
  "event": "systemStatus",
  "status": "online",
  "version": "1.9.1"
}
```
