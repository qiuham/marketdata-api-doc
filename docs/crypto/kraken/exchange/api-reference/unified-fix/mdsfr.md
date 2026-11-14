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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/mdsfr'
updated_at: 2026-11-13
---

# Market Data Snapshot Full Refresh

> Full order book snapshot via FIX

FIX
session: market-data
35=W

The initial response to a valid [Market Data Request](https://docs.kraken.com/exchange/api-reference/unified-fix/mdr.md) containing the full order book snapshot.

***

**header** *required*

35=`W`

**262 - MDReqID** `string` *required*

Unique request identifier.

**55 - Symbol** `string` *required*

Asset Pair listed on the exchange.

**268 - NoMDEntries** `integer` *required*

Number of entries following.

**repeating group**

**269 - MDEntryType** `integer` *required*

**Possible values:**

* `0` : Bid
* `1` : Offer

Trades will only be transmitted via [Market Data Incremental Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdir.md) messages.

**278 - MDEntryID** `string` *required*

Unique identifier for this market data entry. OrderID for the Level 3 subscription.

**270 - MDEntryPx** `float` *required*

Price of the market data entry.

**271 - MDEntrySize** `float` *required*

Volume represented by the market data entry.

**273 - MDEntryTime** `string` *required*

Time of market data entry.

**5060 - MDEntryTimestamp** `string`

High-precision event time for this market data update.
**Level 3 only.** When present with 5273, 5060 is the time the update was generated; 5273 is the queue entry time.
Sample format: `2026-02-03T10:24:34.650069468Z` (ISO 8601, nanosecond fractional seconds, UTC).

**5273 - MDEntryTimeQueue** `string`

Queue entry time: when the order entered the book at this price level.
**Level 3 only.** For L3, orders at the same price are ordered by this tag.
Sample format: `2026-02-03T10:24:29.175114502Z` (ISO 8601, nanosecond fractional seconds, UTC).

**trailer** *required*

```text Spot L2 Example theme={null}
8=FIX.4.4|9=208|35=W|34=21|49=KRAKEN-MD|52=20230707-13:49:11.245|56=MYCOMPID|55=BTC/USD|262=3|268=2|269=1|278=O30300.0|270=30300.0|271=8.44867022|273=13:49:07.307|269=0|278=B30299.9|270=30299.9|271=0.67373926|273=13:49:10.179|10=254|
```

```text Futures L3 Example theme={null}
8=FIX.4.4|9=87775|35=W|34=2|49=KRAKEN-DRV-MD|52=20250304-15:25:09.911|56=MYCOMPID_DRV|55=PF_ETHUSD|262=1|268=10|269=1|278=00bf00ff-00bb-00f7-00ed-006f007f00de|270=2043.1|271=2.05|273=15:25:09.883|269=1|278=009e005a-00b9-0035-00ff-009e00ce007e|270=2043.9|271=2.05|273=15:25:09.767|...|10=000|
```
