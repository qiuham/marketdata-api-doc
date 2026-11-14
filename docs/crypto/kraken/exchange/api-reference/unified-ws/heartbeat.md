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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/heartbeat'
updated_at: 2026-11-13
---

# Heartbeat

> Automatic heartbeat messages to verify the connection is alive

UWS
uws.kraken.com/v2/public
heartbeat

The `heartbeat` channel provides a mechanism to verify that the connection is alive.

Heartbeat messages are sent approximately once every second **in the absence of any other channel updates**.

There is no option to directly request a `heartbeat` subscription, the heartbeats will be automatically generated on subscription to any channel.

## Update

The channel name is the indicator of a heartbeat, there is no other data in the heartbeat payload.

**channel** `string`

Value: `heartbeat`

```json Example: Heartbeat theme={null}
{
    "channel": "heartbeat"
}
```
