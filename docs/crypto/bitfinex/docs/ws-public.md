---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/docs/ws-public'
updated_at: 2026-11-18
---

# Public Channels

### URL

Public channels should use the domain:
wss\://api-pub.bitfinex.com/

The domain:
wss\://api.bitfinex.com/
Should only be used for channels that require authentication.

### Rate Limit

The rate limit for the wss\://api-pub.bitfinex.com/ domain is set at 20 connections per minute.

### Connecting to a channel

Use a subscription message to subscribe to a channel:

```json
{
   "event": "subscribe",
   "channel": CHANNEL_NAME
}
```

Each channel documentation page also includes example subscription messages. You can subscribe to 25 channels at the same time on the same connection.

* [Ticker](https://docs.bitfinex.com/reference/ws-public-ticker)
* [Trades](https://docs.bitfinex.com/reference/ws-public-trades)
* [Books](https://docs.bitfinex.com/reference/ws-public-books)
* [Raw Books](https://docs.bitfinex.com/reference/ws-public-raw-books)
* [Candles](https://docs.bitfinex.com/reference/ws-public-candles)
* [Status](https://docs.bitfinex.com/reference/ws-public-status)

<br />
