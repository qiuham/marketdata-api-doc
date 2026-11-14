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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/session-reject'
updated_at: 2026-11-13
---

# Session Reject

> FIX message used to reject a received message at the session level due to protocol violations.

The Session Reject message is used to reject a received message at the session level due to protocol violations or other session-related issues.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `3`
>
> **45 - RefSeqNum** `integer` *required*
>
> MsgSeqNum of rejected message.
>
> **371 - RefTagID** `integer`
>
> The tag number of the FIX field being referenced.
>
> **372 - RefMsgType** `string`
>
> The MsgType of the FIX message being referenced.
>
> **373 - SessionRejectReason** `integer`
>
> Code to identify reason for a session-level Reject message.
>
> **58 - Text** `string`
>
> Where possible, message to explain reason for rejection.
>
> **trailer** *required*
