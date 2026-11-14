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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/mdrr'
updated_at: 2026-11-13
---

# Market Data Request Reject

> Rejection of a market data subscription request via FIX

FIX
session: market-data
35=Y

When a [Market Data Request](https://docs.kraken.com/exchange/api-reference/unified-fix/mdr.md) cannot be honored, the FIX Server responds with this reject message.

***

**header** *required*

35=`Y`

**262 - MDReqID** `string` *required*

Unique request identifier.

**281 - MDReqRejReason** `integer` *required*

**Possible values:**

* `0` : Unknown Symbol
* `1` : Duplicate MDReqID
* `4` : Unsupported SubscriptionRequestType
* `5` : Unsupported MarketDepth
* `6` : Unsupported MDUpdateType
* `8` : Unsupported MDEntryType
* `A` : Unsupported Scope
* `B` : Level3 not available
* `C` : Trade not available on this request

**58 - Text** `string`

Full description for rejection.

**trailer** *required*

```text Unknown Symbol (MDReqRejReason=0) theme={null}
8=FIX.4.4|9=102|35=Y|34=3|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|262=MDSUB1|281=0|58=Unknown symbol: FOO/BAR|10=115|
```

```text Duplicate MDReqID (MDReqRejReason=1) theme={null}
8=FIX.4.4|9=96|35=Y|34=4|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|262=MDSUB1|281=1|58=Duplicate MDReqID|10=106|
```

```text Unsupported Market Depth (MDReqRejReason=5) theme={null}
8=FIX.4.4|9=108|35=Y|34=5|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|262=MDSUB2|281=5|58=Unsupported market depth: 100|10=006|
```
