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
updated_at: 2026-11-27
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

**273 - MDEntryTime** `string`

Time of market data entry.
**Level 2 only.** Level 3 entries carry 5273 instead and do not include 273.

**5273 - MDEntryTimeQueue** `string`

Queue entry time: when the order entered the book at this price level.
**Level 3 only.** For L3, orders at the same price are ordered by this tag.
Sample format: `2026-02-03T10:24:29.175114502Z` (ISO 8601, nanosecond fractional seconds, UTC).

**5060 - MDEntryTimestamp** `string`

High-precision event time for this message. Sent once per message, after the repeating group, not on each entry.
**Level 3 only.**
Sample format: `2026-02-03T10:24:34.650069468Z` (ISO 8601, nanosecond fractional seconds, UTC).

**trailer** *required*

```text Spot L2 Example theme={null}
8=FIX.4.4|9=208|35=W|34=21|49=KRAKEN-MD|52=20230707-13:49:11.245|56=MYCOMPID|55=BTC/USD|262=3|268=2|269=1|278=O30300.0|270=30300.0|271=8.44867022|273=13:49:07.307|269=0|278=B30299.9|270=30299.9|271=0.67373926|273=13:49:10.179|10=254|
```

```text Futures L3 Example theme={null}
8=FIX.4.4|9=...|35=W|34=2|49=KRAKEN-DRV-MD|52=20261112-17:59:55.585|56=MYCOMPID_DRV|55=PF_CRVUSD|262=1|268=226|269=1|278=a3359aed-64df-4069-aeb7-9203ee0b034a|270=0.2362|271=2000|5273=2026-11-12T17:57:58.432980188Z|269=1|278=a3359aee-e717-43e3-adea-f2217d55f922|270=0.2362|271=2000|5273=2026-11-12T17:57:59.421705274Z|...|893=Y|5060=2026-11-12T17:59:55.059327516Z|10=...|
```
