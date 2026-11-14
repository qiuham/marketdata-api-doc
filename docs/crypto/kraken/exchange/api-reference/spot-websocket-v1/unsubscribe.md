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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/unsubscribe'
updated_at: 2026-11-13
---

# Unsubscribe

> Unsubscribe from one or more WebSocket channels

WSS
ws.kraken.com
unsubscribe

Unsubscribe from one or more channels. You can specify a channelID or multiple currency pairs. The response is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

## Request

**event** `string` *required*

Value: `unsubscribe`

**pair** `array of strings`

Condition: All channels which support pair subscriptions\\

Example: `["BTC/USD", "MATIC/GBP"]`

Unsubscribe to specific pairs.

**reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.

**subscription** `object`

**properties**

**name** `string` *required*

One of: `book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`

The name of the channel to unsubscribe. Wildcard `*` is supported.

**depth** `integer`

Condition: `book` channel only

Unsubscribe to a specific depth.

**interval** `integer`

Condition: `ohlc` channel only

Unsubscribe to a specific interval.

```json Unsubscribe theme={null}
{
    "event": "unsubscribe",
    "pair": [
        "XBT/EUR",
        "XBT/USD"
    ],
    "subscription": {
        "name": "ticker"
    }
}
```
