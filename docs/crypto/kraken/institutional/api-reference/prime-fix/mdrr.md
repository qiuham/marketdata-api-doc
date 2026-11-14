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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/mdrr'
updated_at: 2026-11-13
---

# Market Data Request Reject

> FIX message used to reject invalid market data requests.

The Market Data Request Reject message is used to reject invalid market data requests.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `Y`
>
> **262 - MDReqID** `string` *required*
>
> Refers to the MDReqID of the request.
>
> **58 - Text** `string`
>
> Free-format text string explaining the rejection reason.
>
> **trailer** *required*
