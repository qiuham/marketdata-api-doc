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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/test-request'
updated_at: 2026-11-13
---

# Test Request

> FIX message used to force a Heartbeat from the counterparty.

The Test Request message is used to force a Heartbeat from the other side of the connection. When a Test Request is sent, the recipient must respond with a Heartbeat message containing the same TestReqID value.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `1`
>
> **112 - TestReqID** `string` *required*
>
> Unique identifier for the test request.
>
> **trailer** *required*
