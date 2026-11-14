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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/ocr'
updated_at: 2026-11-13
---

# Order Cancel Request

> Cancel a single order via FIX

FIX
session: trading
35=F

Cancel a single GTD or GTC order.

A successful order cancellation will result in an [execution report](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md) with the OrdStatus set to 4 (Cancelled).
Unsuccessful cancellation requests will result in a [business level reject](https://docs.kraken.com/exchange/api-reference/unified-fix/reject-business.md) message with the reason of the rejection.

***

**header** *required*

35=`F`

**11 - ClOrdID** `string` *required*

Unique identifier of the order. The ID can be one of the following formats:

* **Ever-Increasing Positive Numbers**: Ever-increasing positive numbers, such as microsecond timestamps, to ensure the uniqueness and sequential nature of the identifiers.
  **Example**: Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
* **Timestamp-First v4 UUIDs**: A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part needs to be 10 microseconds maximum such as `162344829423400`.

**37 - OrderID** `string`

OrderId needs to match the one received on the ExecutionReports.

Condition: One of ClOrdID or OrderID is required at least for the cancellation to be accepted

**41 - OrigClordid** `string`

Reference the Last ClOrdID used. If both OrderID and OrigClordid are present then only the OrderID will be used.

Condition: One of ClOrdID or OrderID is required at least for the cancellation to be accepted

**54 - Side** `integer` *required*

Side of the order.

**Possible values:**

* `1` : Buy
* `2` : Sell

**55 - Symbol** `string` *required*

Pair in the format BASE/QUOTE.

**60 - TransactTime** `string` *required*

Time of order cancellation expressed in UTC. Format: `YYYYMMDD-HH:MM:SS.uuu`

**trailer** *required*

> [tab] Spot
>
> ```text Cancel request (client → server) theme={null}
> 8=FIX.4.4|9=163|35=F|34=5|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:06.000|11=1744036325300000|37=OQNCZM-NVAVC-AVD2LO|41=1744036325000000|54=1|55=BTC/USD|60=20260407-14:32:06.000|10=111|
> ```
>
> ```text ER cancel response (server → client) theme={null}
> 8=FIX.4.4|9=267|35=8|34=6|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:06.000|6=0|11=1744036325300000|14=0|17=EXEC010:TRD001|37=OQNCZM-NVAVC-AVD2LO|38=0.001|39=4|40=2|41=1744036325000000|44=84000|54=1|55=BTC/USD|58=Order canceled by user|59=1|60=20260407-14:32:06.000|150=4|151=0|381=0|10=159|
> ```

> [tab] Futures
>
> ```text Cancel request (client → server) theme={null}
> 8=FIX.4.4|9=230|35=F|34=5|49=CLIENT-DRV|56=KRAKEN-DRV-TRD|52=20260407-14:32:06.000|11=a17d4975-2001-4abc-def0-1234567890ab|37=9e58120f-40e0-44dc-beec-6d1b5ea9136c|41=a17d4971-f00d-4f67-94d1-e7d604104ed2|54=1|55=PF_XBTUSD|60=20260407-14:32:06.000|10=188|
> ```
