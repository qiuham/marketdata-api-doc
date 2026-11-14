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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/ocr'
updated_at: 2026-11-13
---

# Order Cancel Request

> Cancel an existing order via FIX.

Cancel an existing order.

A successful order cancellation will result in an [execution report](https://docs.kraken.com/institutional/api-reference/prime-fix/er.md) with the OrdStatus set to 4 (Cancelled).
Unsuccessful cancellation requests will result in a [business level reject](https://docs.kraken.com/institutional/api-reference/prime-fix/ocrej.md) message with the reason of the rejection.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `F`
>
> **11 - ClOrdID** `string` *required*
>
> Unique identifier for Order as assigned by the client. Must be `<= 36 characters`. UUIDs are recommended.
>
> **41 - OrigClordid** `string`
>
> ClOrdID(11) of the previous non-rejected order. One of ClOrdID or OrderID is required at least for the cancellation to be accepted.
>
> **55 - Symbol** `string` *required*
>
> The symbol of the currency pair to place an order on in the format `BASE-QUOTE`.
>
> **54 - Side** `integer` *required*
>
> Side of the order.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : Buy</li>
>   <li>`2` : Sell</li>
> </ul>
>
> **60 - TransactTime** `string` *required*
>
> Time of order cancellation expressed in UTC. Format: YYYYDD-HH:MM:SS.uuu
>
> **trailer** *required*
