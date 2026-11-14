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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/heartbeat'
updated_at: 2026-11-13
---

# Heartbeat

> FIX message used to maintain session connectivity and confirm the application is functioning normally.

The Heartbeat message is used to maintain session connectivity and indicate that the application is functioning normally. Heartbeat messages are sent periodically based on the HeartBtInt from Logon, in response to Test Request messages, or when no other messages have been sent within the heartbeat interval.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `0`
>
> **112 - TestReqID** `string` *required*
>
> Required when the heartbeat is the result of a Test Request message.
>
> **trailer** *required*
