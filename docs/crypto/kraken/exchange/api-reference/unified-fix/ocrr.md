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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/ocrr'
updated_at: 2026-11-13
---

# Order Cancel Replace Request

> Amend a working order via FIX (Spot only)

FIX
session: trading
35=G

The Order Cancel-Replace Request message (MsgType=G) is used by the Client to amend the replaceable fields of working orders which are Quantities and Prices.
A successful order replacement request will result in an execution report with the OrdStatus.

> [!NOTE]
>
> This message is available for **Spot only**.

***

**header** *required*

35=`G`

**11 - ClOrdID** `string` *required*

Unique identifier of the order. The ID can be one of the following formats:

* **Ever-Increasing Positive Numbers**: Ever-increasing positive numbers, such as microsecond timestamps, to ensure the uniqueness and sequential nature of the identifiers.
  **Example**: Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
* **Timestamp-First v4 UUIDs**: A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part needs to be 10 microseconds maximum such as `162344829423400`.

**37 - OrderID** `string` *required*

OrderID to be amended; needs to match the one received on the ExecutionReports.

**41 - OrigClordid** `string` *required*

Reference the Last ClOrdID used.

**54 - Side** `integer` *required*

Side of the order.

**Possible values:**

* `1` : Buy
* `2` : Sell

**55 - Symbol** `string` *required*

Pair in the format BASE/QUOTE.

**60 - TransactTime** `string` *required*

Time of order cancellation expressed in UTC. Format: `YYYYMMDD-HH:MM:SS.uuu`

**38 - OrderQty** `float` *required*

Size of the order.

**1138 - DisplayQty** `float`

Maximum qty shown in the market at any point in time for iceberg orders.

**40 - OrderType** `char` *required*

The execution model of the order.

**Possible values:**

* `1` : market
* `2` : Limit
* `3` : Stop-loss
* `4` : Stop-loss-limit
* `R` : Take-profit
* `T` : Take-profit-limit
* `U` : Trailing-stop
* `V` : Trailing-stop-limit

**59 - TimeInForce** `string` *required*

Time-in-force specifies how long an order remains in effect before being expired.

**Possible values:**

* `1` : GTC (Good till canceled)
* `3` : IOC (Immediate or Cancel)
* `6` : GTD (Good till date)

**44 - Price** `float`

Limit Price of the order to be placed in the Order Book. This field is denominated in Quote Currency.

Condition: OrderType = Limit / Stop-Loss-Limit / Take-Profit-Limit / Trailing-stop-limit

**99 - StopPx** `float`

Defines the trigger price of the order. This field is denominated in Quote Currency.

Condition: OrderType = Stop-Loss / Take-Profit / Stop-Loss-Limit / Trailing-stop / Trailing-stop-limit

**18 - ExecInst** `char`

Enable clients to place order using the Post-Only safeguard.

**Possible values:**

* `P` : Post-Only — Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.

**62 - ValidUntilTime** `string`

The engine will reject any order entered into the matching engine after this time. This provides extra protection against latency on time sensitive orders. The timestamp should be at least 2 seconds and at most 60 seconds in the future. Format: `YYYYMMDD-HH:MM:SS.uuu`

**trailer** *required*

```text Amend Price and Qty (client → server) theme={null}
8=FIX.4.4|9=191|35=G|34=3|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|11=1744036325100000|37=OQNCZM-NVAVC-AVD2LO|41=1744036325000000|54=1|55=BTC/USD|60=20260407-14:32:10.000|38=0.002|40=2|44=83500|59=1|10=083|
```

```text ER Replace Response (server → client) theme={null}
8=FIX.4.4|9=245|35=8|34=7|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:10.000|6=0|11=1744036325100000|14=0|17=EXEC011:TRD001|37=OQNCZM-NVAVC-AVD2LO|38=0.002|39=5|40=2|41=1744036325000000|44=83500|54=1|55=BTC/USD|59=1|60=20260407-14:32:10.000|150=5|151=0.002|381=0|10=136|
```
