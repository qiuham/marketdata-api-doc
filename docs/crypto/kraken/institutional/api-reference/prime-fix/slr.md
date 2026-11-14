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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/slr'
updated_at: 2026-11-13
---

# Security List Request

> FIX message to request the list of securities available for trading.

Request a list of securities available for trading.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `x`
>
> **320 - SecurityReqID** `string` *required*
>
> Unique ID to identify this request.
>
> **559 - SecurityListRequestType** `integer` *required*
>
> Identifies the type of Security List Request.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`4` : ALL\_SECURITIES</li>
> </ul>
>
> **trailer** *required*

> [tab] Example
>
> ```text theme={null}
> 8=FIX.4.4|9=88|35=x|34=3|49=CUSTOMER|52=20220930-13:28:16.451|56={{ Customer }}|320=id-220929160342682-27|559=4|10=156|
> ```
