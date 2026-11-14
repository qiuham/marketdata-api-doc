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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus'
updated_at: 2026-11-13
---

# Subscription Status

> Server-pushed subscription status response to subscribe, unsubscribe, or exchange-initiated unsubscribe

WSS
ws.kraken.com
subscriptionStatus

Subscription status response to subscribe, unsubscribe or exchange-initiated unsubscribe. This message is returned for every subscribe or unsubscribe request across all channels.

## Payload

**event** `string`

Value: `subscriptionStatus`

**channelName** `string` *required*

One of: `book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`

The name of the channel.

**pair** `string`

Example: `"BTC/USD"`

The currency pair associated with this subscription.

**status** `string`

One of: `subscribed`, `unsubscribed`, `ok`, `error`

**subscription** `object`

**properties**

**depth** `integer`

Condition: 'book' channel only

The book depth.

**interval** `integer`

Condition: 'ohlc' channel only

The ohlc interval.

**maxratecount** `integer`

The rate counter.

**name** `string` *required*

One of: `book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`

The name of the channel.

**token** `string`

Condition: Authenticated requests only

The authentication token associated with the request.

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** `string`

Condition: Unsuccessful requests only

Error message for unsuccessful requests.

**channelID** `integer` *deprecated*

Deprecated: use `channelName` and `pair`

Channel ID on successful subscription, applicable to public messages only.

```json Subscribed: Ticker theme={null}
{
  "channelID": 10001,
  "channelName": "ticker",
  "event": "subscriptionStatus",
  "pair": "XBT/EUR",
  "status": "subscribed",
  "subscription": {
    "name": "ticker"
  }
}
```

```json Unsubscribed: OHLC theme={null}
{
  "channelID": 10001,
  "channelName": "ohlc-5",
  "event": "subscriptionStatus",
  "pair": "XBT/EUR",
  "reqid": 42,
  "status": "unsubscribed",
  "subscription": {
    "interval": 5,
    "name": "ohlc"
  }
}
```

```json Subscribed: ownTrades theme={null}
{
  "channelName": "ownTrades",
  "event": "subscriptionStatus",
  "status": "subscribed",
  "subscription": {
    "name": "ownTrades"
  }
}
```

```json Error theme={null}
{
  "errorMessage": "Subscription depth not supported",
  "event": "subscriptionStatus",
  "pair": "XBT/USD",
  "status": "error",
  "subscription": {
    "depth": 42,
    "name": "book"
  }
}
```
