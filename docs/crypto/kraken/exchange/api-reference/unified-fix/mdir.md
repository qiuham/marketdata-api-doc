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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/mdir'
updated_at: 2026-11-27
---

# Market Data Incremental Refresh

> Incremental order book and trade updates via FIX

FIX
session: market-data
35=X

Incremental updates to the order book and trades following a [Market Data Snapshot Full Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdsfr.md).

***

**header** *required*

35=`X`

**262 - MDReqID** `string` *required*

Unique request identifier.

**55 - Symbol** `string` *required*

Asset Pair listed on the exchange.

**268 - NoMDEntries** `integer` *required*

Number of entries following. If several entries are present they need to be parsed in order (for example creation and deletion of an entry in the book can happen in the same message).

**repeating group**

**279 - MDUpdateAction** `integer` *required*

Always first field in this repeating group.

**Possible values:**

* `0` : New — Creation of an entry in the book
* `1` : Update — Update of a quantity for an entry in the book
* `2` : Delete — Removal of an entry from the subscribed depth (tag `271` greater than 0) or from the book entirely (tag `271=0`, cancelled or filled)

**269 - MDEntryType** `integer` *required*

**Possible values:**

* `0` : Bid
* `1` : Offer
* `2` : Trade

**278 - MDEntryID** `string` *required*

Unique identifier for this market data entry. Corresponding to the OrderID for Level 3 subscription.

**270 - MDEntryPx** `float` *required*

Price of the market data entry.

**271 - MDEntrySize** `float` *required*

Volume represented by the market data entry.

**273 - MDEntryTime** `string`

The time the entry was inserted or amended or deleted.
**Level 2 only.** Level 3 entries carry 5273 instead and do not include 273.

**5273 - MDEntryTimeQueue** `string`

Queue entry time: when the order entered the book at this price level.
**Level 3 only.** For L3, orders at the same price are ordered by this tag.
Sample format: `2026-02-03T10:24:29.175114502Z` (ISO 8601, nanosecond fractional seconds, UTC).

**40 - OrdType** `char`

The order type of the taker order.

**Possible values:**

* `1` : market
* `2` : Limit

Condition: MDEntryType = Trade

**2446 - AggressorSide** `char`

The side of the taker order.

**Possible values:**

* `1` : Buy
* `2` : Sell

Condition: MDEntryType = Trade

**5041 - ChecksumOrderBook** `string`

Checksum to verify the orderbook update. See [Checksum article](https://docs.kraken.com/exchange/guides/fix/checksums.md).

Condition: MDEntryType = Bid or Offer

**5060 - MDEntryTimestamp** `string`

High-precision event time for this message. Sent once per message, after 5041 and before the trailer, not on each entry.
**Level 3 only.**
Sample format: `2026-02-03T10:24:34.650069468Z` (ISO 8601, nanosecond fractional seconds, UTC).

**trailer** *required*

```text Spot L2 Example theme={null}
8=FIX.4.4|9=213|35=X|34=100|56=MYCOMPID|49=KRAKEN-MD|52=20230707-13:42:27.230|55=BTC/USD|262=1|268=2|279=2|269=1|278=O30300.7|270=30300.7|271=0.0|273=13:42:27.208|279=0|269=1|278=O31941.0|270=31941.0|271=0.0031746|273=20:40:00.455|10=112|
```

```text Futures L2 Example theme={null}
8=FIX.4.4|9=173|35=X|34=33402|49=KRAKEN-DRV-MD|52=20250303-14:13:24.905|56=MYCOMPID_DRV|55=PF_ETHUSD|262=1|268=1|279=0|269=0|278=B2372.7|270=2372.7|271=0.084|273=14:13:24.859|5041=3254665545|10=121|
```

```text Futures L3 Example theme={null}
8=FIX.4.4|9=255|35=X|34=7|49=KRAKEN-DRV-MD|52=20261112-17:59:55.625|56=MYCOMPID_DRV|55=PF_XBTUSD|262=1|268=1|279=2|269=1|278=a3359b9f-d288-49dd-8284-3a174f0763a1|270=71850|271=0.0696|5273=2026-11-12T17:59:55.584045155Z|5041=4208402451|5060=2026-11-12T17:59:55.584045155Z|10=166|
```
