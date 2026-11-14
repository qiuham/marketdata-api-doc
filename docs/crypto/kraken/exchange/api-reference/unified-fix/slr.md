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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/slr'
updated_at: 2026-11-13
---

# Instrument List Request

> Request a list of available instruments via FIX

FIX
session: market-data
35=x

The InstrumentListRequest message is used to return a list of securities from the exchange that match the criteria provided on the request.
We recommend that clients send an InstrumentListRequest on any new connection or reconnection as the status of the Instrument might have changed during the disconnection.

***

**header** *required*

35=`x`

**320 - InstrumentReqID** `string` *required*

Unique request identifier.

**263 - SubscriptionRequestType** `integer`

**Possible values:**

* `0` : Snapshot
* `1` : Snapshot + Updates
* `2` : Disable previous snapshot + Update request

**559 - InstrumentListRequestType** `integer` *required*

**Possible values:**

* `0` : Single asset pair definition
* `1` : SecurityType
* `4` : All Securities

**167 - SecurityType** `string`

**Possible values:**

* `CASH` : Spot only instruments
* `FUT` : Futures only instruments
* `OPT` : Options only instruments
* `TS` : Tokenized stocks only instruments, i.e. xStocks

Condition: InstrumentListRequestType = 1

**55 - Symbol** `string`

Format should be BASE/QUOTE.

Condition: InstrumentListRequestType = 0

**trailer** *required*

```text Request All Securities (Snapshot) theme={null}
8=FIX.4.4|9=81|35=x|34=2|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|263=0|320=SLREQ1|559=4|10=240|
```

```text Request Single Instrument theme={null}
8=FIX.4.4|9=92|35=x|34=3|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|263=0|320=SLREQ2|559=0|55=BTC/USD|10=140|
```

```text Request All Spot Instruments (SecurityType=CASH) theme={null}
8=FIX.4.4|9=100|35=x|34=4|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|263=0|320=SLREQ3|559=1|167=CASH|10=088|
```
