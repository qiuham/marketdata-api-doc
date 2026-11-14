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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/tss'
updated_at: 2026-11-13
---

# Trading Session Status

> Trading session status response via FIX (Spot only)

FIX
session: market-data
35=h

Response to a [Trading Session Status Request](https://docs.kraken.com/exchange/api-reference/unified-fix/tssr.md) with the current market status.

> [!NOTE]
>
> This message is available for **Spot only**.

***

**header** *required*

35=`h`

**335 - TradSesReqID** `string` *required*

Unique request identifier.

**336 - TradingSessionID** `string` *required*

Trading Session identifier.

**340 - TradSesStatus** `integer`

**Possible values:**

* `0` : unknown
* `1` : Maintenance — Markets are offline for scheduled maintenance — new orders cannot be placed and existing orders cannot be cancelled.
* `2` : Online — Markets are operating normally — all order types may be submitted and order matching can occur.
* `101` : cancel\_only — Orders can be cancelled but new orders cannot be placed. No order matching will occur.
* `102` : post\_only — Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.
* '103' : limit\_only - Only limit orders can be submitted. Orders can be cancelled. No order matching will occur.

**567 - TradSesStatusRejReason** `integer`

**Possible values:**

* `1` : UNKNOWNTRADINGSESSIONID
* `100` : INVALIDREQUESTID
* `101` : INVALIDSUBSTYPE
* `102` : DUPLICATEREQUESTID
* `103` : ALREADYSUBSCRIBED

**trailer** *required*

```text Market Online (TradSesStatus=2) theme={null}
8=FIX.4.4|9=88|35=h|34=3|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|335=TSSREQ1|336=SESSION|340=2|10=048|
```

```text Market Maintenance (TradSesStatus=1) theme={null}
8=FIX.4.4|9=88|35=h|34=4|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|335=TSSREQ1|336=SESSION|340=1|10=048|
```
