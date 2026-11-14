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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/mdr'
updated_at: 2026-11-13
---

# Market Data Request

> Subscribe to market data streams via FIX

FIX
session: market-data
35=V

The MarketDataRequest message is used by the client system to request a market data stream for the order book and/or trades.

In response, the FIX Server will begin sending out a [MarketDataSnapshot](https://docs.kraken.com/exchange/api-reference/unified-fix/mdsfr.md) if it is a valid request. Otherwise, the FIX Server will send out a [MarketDataRequestReject](https://docs.kraken.com/exchange/api-reference/unified-fix/mdrr.md) with the Text tag containing the reason for the rejection.

Each subscription request needs to have a unique identifier set via tag MDReqID, which will be used to refer back to the client. It is also used to unsubscribe from market data.

Market data updates are sent to clients using a [MarketDataSnapshotFullRefresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdsfr.md) message and then [MarketDataIncrementalRefresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdir.md) message. A full empty market data snapshot may be sent in case no more prices are received.
These prices will stream continuously until the client requests to unsubscribe using a MarketDataRequest with the SubscriptionRequestType set to Unsubscribe (263=2).

For the OrderBook, the client can request Level 2 or Level 3 depending on the value of the AggregatedBook tag.

In case of a disconnection, the subscription will be cancelled. The Client will need to subscribe again after the reconnection.

***

**header** *required*

35=`V`

**262 - MDReqID** `string` *required*

Unique request identifier.

**263 - SubscriptionRequestType** `integer` *required*

**Possible values:**

* `1` : Snapshot + Updates
* `2` : Disable previous snapshot + Update request

**264 - MarketDepth** `integer` *required*

**Possible values:**

* `0` : Full depth of book (limited to 1000 for Level 2)
* `1` : Top of Book
* `10`, `25`, `100`, `500` and `1000`

**265 - MDUpdateType** `integer`

**Possible values:**

* `1` : Incremental Refresh

Only incremental Refresh is supported.

**266 - AggregatedBook** `boolean`

Specify if the request is for Level 2 or Level 3.

**Possible values:**

* `Y` : one book entry per side per price. Aka Level 2.
* `N` : Multiple entries per side per price allowed. Aka Level 3. Only Available for Derivatives.

**Default value:** `Y`

Level 3 is only available for MDEntryType BID and OFFER. Request will get rejected if used with MDEntryType TRADE.

**267 - NoMDEntryTypes** `integer` *required*

Repeating Group. Number of MDEntryTypes.

**repeating group**

**269 - MDEntryType** `integer` *required*

Client can subscribe to bid/offer and/or trades. It is not possible to subscribe to only bid or only offer.

**Possible values:**

* `0` : Bid
* `1` : Offer
* `2` : Trade

**146 - NoRelatedSym** `integer` *required*

Number of pairs to subscribe to.

**repeating group**

**55 - Symbol** `string` *required*

Asset Pair listed on the exchange.

**trailer** *required*

```text Spot Subscribe BTC/USD L2 (bid+ask, depth 10) theme={null}
8=FIX.4.4|9=117|35=V|34=2|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|262=MDSUB1|263=1|264=10|265=1|267=2|269=0|269=1|55=BTC/USD|10=244|
```

```text Spot Unsubscribe theme={null}
8=FIX.4.4|9=111|35=V|34=3|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:10.000|262=MDSUB1|263=2|264=10|265=1|267=1|269=0|55=BTC/USD|10=223|
```

```text Futures L2 Subscribe theme={null}
8=FIX.4.4|9=133|35=V|34=2|49=CLIENT-DRV|56=KRAKEN-DRV-MD|52=20260407-14:32:01.000|146=1|55=PF_ETHUSD|262=MDSUB2|263=1|264=0|265=1|267=3|269=0|269=1|269=2|10=197|
```

```text Futures L3 Subscribe theme={null}
8=FIX.4.4|9=133|35=V|34=3|49=CLIENT-DRV|56=KRAKEN-DRV-MD|52=20260407-14:32:01.000|146=1|55=PF_ETHUSD|262=MDSUB3|263=1|264=0|265=1|266=N|267=2|269=0|269=1|10=121|
```
