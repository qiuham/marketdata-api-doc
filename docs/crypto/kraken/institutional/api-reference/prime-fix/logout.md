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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/logout'
updated_at: 2026-11-13
---

# Logout

> FIX message used to initiate or confirm the termination of a FIX session.

The Logout message is used to initiate or confirm the termination of a FIX session.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `5`
>
> **58 - Text** `string`
>
> Optional text message.
>
> **trailer** *required*
