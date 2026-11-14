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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/tssr'
updated_at: 2026-11-13
---

# Trading Session Status Request

> Request trading session status via FIX (Spot only)

FIX
session: market-data
35=g

This message will return the status of the market. You can subscribe to have snapshot only or updates as well.
A specific status can also be available for individual instruments in the [Instrument List Request](https://docs.kraken.com/exchange/api-reference/unified-fix/slr.md).

> [!NOTE]
>
> This message is available for **Spot only**.

***

**header** *required*

35=`g`

**335 - TradSesReqID** `string` *required*

Unique request identifier.

**336 - TradingSessionID** `string` *required*

Trading Session identifier.

**263 - SubscriptionRequestType** `integer` *required*

**Possible values:**

* `0` : Snapshot only
* `1` : Snapshot + Updates
* '2' : Unsubscribe

**5200 - KrakenIncludeAdvisories** `char`

Y = opt-in to maintenance / emergency News broadcast. Default is N.

**trailer** *required*

```text Snapshot-only Request (SubscriptionRequestType=0) theme={null}
8=FIX.4.4|9=88|35=g|34=3|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|263=0|335=TSSREQ2|336=SESSION|10=050|
```

```text Subscribe to Updates (SubscriptionRequestType=1) theme={null}
8=FIX.4.4|9=88|35=g|34=2|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|263=1|335=TSSREQ1|336=SESSION|10=049|
```

```text Subscribe to Updates (SubscriptionRequestType=1) and opt-in to maintenance / emergency News broadcast theme={null}
8=FIX.4.4|35=g|49=QAProdFIXtesting|56=KRAKEN-TRD|263=0|335=MSR0|336=SESSION|5200=Y|10=119|
```
