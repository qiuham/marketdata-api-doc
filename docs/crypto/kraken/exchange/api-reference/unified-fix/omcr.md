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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/omcr'
updated_at: 2026-11-13
---

# Order Mass Cancel Request

> Cancel all open orders via FIX

FIX
session: trading
35=q

This request is used by clients to cancel all open orders including untriggered orders and orders resting in the book.
As a response to this request, Kraken will confirm each order cancellation through [execution report](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md) type canceled.

***

**header** *required*

35=`q`

**11 - ClOrdID** `string` *required*

Unique identifier of the order. The ID can be one of the following formats:

* **Ever-Increasing Positive Numbers**: Ever-increasing positive numbers, such as microsecond timestamps, to ensure the uniqueness and sequential nature of the identifiers.
  **Example**: Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
* **Timestamp-First v4 UUIDs**: A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part needs to be 10 microseconds maximum such as `162344829423400`.

**60 - TransactTime** `string` *required*

Time of order cancellation expressed in UTC. Format: `YYYYMMDD-HH:MM:SS.uuu`

**530 - MassCancelRequestType** `integer` *required*

**Possible values:**

* `1` : Cancel all orders created or replaced during the trading Session by Symbol
* `6` : Cancel all orders created or replaced during the trading Session
* `7` : Cancel all open orders created by the SenderCompID

**55 - Symbol** `string`

The pair in format BASE/QUOTE.

Condition: MassCancelRequestType = 1

**trailer** *required*

```text Cancel All Orders for a Symbol (MassCancelRequestType=1) theme={null}
8=FIX.4.4|9=121|35=q|34=6|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|11=1744036340000000|55=BTC/USD|60=20260407-14:32:10.000|530=1|10=238|
```

```text Cancel All Session Orders (MassCancelRequestType=6) theme={null}
8=FIX.4.4|9=110|35=q|34=7|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|11=1744036341000000|60=20260407-14:32:10.000|530=6|10=087|
```

```text Cancel All Open Orders (MassCancelRequestType=7) theme={null}
8=FIX.4.4|9=110|35=q|34=8|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|11=1744036342000000|60=20260407-14:32:10.000|530=7|10=090|
```
