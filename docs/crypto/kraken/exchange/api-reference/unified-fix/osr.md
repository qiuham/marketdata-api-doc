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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/osr'
updated_at: 2026-11-13
---

# Order Status Request

> Request current order status via FIX (Spot only)

FIX
session: trading
35=H

This request is used by clients to obtain information about current order status on Kraken exchange.
As a response to this request, Order Status is sent on [execution report](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md) with ExecType = `I`.
Tag 39 on this response would give away current order status.

> [!NOTE]
>
> This message is available for **Spot only**.

***

**header** *required*

35=`H`

**11 - ClOrdID** `string` *required*

Unique identifier of the order. The ID can be one of the following formats:

* **Ever-Increasing Positive Numbers**: Ever-increasing positive numbers, such as microsecond timestamps, to ensure the uniqueness and sequential nature of the identifiers.
  **Example**: Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
* **Timestamp-First v4 UUIDs**: A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part needs to be 10 microseconds maximum such as `162344829423400`.

**37 - OrderID** `string` *required*

OrderId needs to match the one received on the ExecutionReports.

**55 - Symbol** `string` *required*

Pair in the format BASE/QUOTE.

**trailer** *required*

```text Order Status Request (client → server) theme={null}
8=FIX.4.4|9=113|35=H|34=6|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|11=1744036325000000|37=OQNCZM-NVAVC-AVD2LO|55=BTC/USD|10=255|
```

```text ER OrderStatus Response (server → client, ExecType=I) theme={null}
8=FIX.4.4|9=225|35=8|34=8|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:10.000|6=0|11=1744036325000000|14=0|17=EXEC012:TRD001|37=OQNCZM-NVAVC-AVD2LO|38=0.001|39=0|40=2|44=84000|54=1|55=BTC/USD|59=1|60=20260407-14:32:05.000|150=I|151=0.001|381=0|10=206|
```
