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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/ocrr'
updated_at: 2026-11-13
---

# Order Cancel Replace Request

> Amend the price, quantity, or other attributes of an existing FIX order.

The Order Cancel-Replace Request message (MsgType=G) is used to amend the price, quantity, or markets of an existing order.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `G`
>
> **11 - ClOrdID** `string` *required*
>
> Unique identifier for Order as assigned by the client. Must be `<= 36 characters`. UUIDs are recommended.
>
> **41 - OrigClordid** `string` *required*
>
> ClOrdID(11) of the previous non-rejected order.
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
> **40 - OrdType** `char` *required*
>
> The execution model of the order.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : market</li>
>   <li>`2` : Limit</li>
>   <li>`A` : LimitAllIn</li>
> </ul>
>
> **38 - OrderQty** `float` *required*
>
> Order quantity in terms of the base asset.
>
> **44 - Price** `float`
>
> Limit price of the order to be placed in the Order Book. Required when OrderType=Limit/LimitAllIn.
>
> **60 - TransactTime** `string` *required*
>
> Business timestamp for this request. Format: YYYYMMDD-HH:MM:SS.uuu
>
> **trailer** *required*
