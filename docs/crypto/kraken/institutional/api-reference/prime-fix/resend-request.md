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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/resend-request'
updated_at: 2026-11-13
---

# Resend Request

> FIX message used to request retransmission of messages when a sequence gap is detected.

The Resend Request message is used to request retransmission of messages from the counterparty when a sequence gap is detected. When a sequence gap is detected (i.e., when the incoming message sequence number is greater than expected), a Resend Request should be sent to request retransmission of the missing messages.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `2`
>
> **7 - BeginSeqNo** `integer` *required*
>
> First message sequence number to be resent.
>
> **16 - EndSeqNo** `integer` *required*
>
> Last message sequence number to be resent. Set to 0 to request all messages from BeginSeqNo onwards.
>
> **trailer** *required*
