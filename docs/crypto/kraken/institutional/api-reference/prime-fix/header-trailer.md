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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/header-trailer'
updated_at: 2026-11-13
---

# Header & Trailer

> Standard FIX message header and trailer fields required in every FIX message.

Every FIX message must include a standard header and trailer. The header contains essential routing and sequence information, while the trailer provides message integrity verification.

> [tab] FIX Specification
>
> **8 - BeginString** `string` *required*
>
> FIX.4.4. Must be the first field in the message.
>
> **9 - BodyLength** `integer` *required*
>
> Must be the second field in the message.
>
> **35 - MsgType** `string` *required*
>
> Must be the third field in the message.
>
> **49 - SenderCompID** `string` *required*
>
> Provided by Customer during onboarding.
>
> **56 - TargetCompID** `string` *required*
>
> Provided by Customer during onboarding.
>
> **34 - MsgSeqNum** `integer` *required*
>
> Message sequence number.
>
> **43 - PossDupFlag** `boolean`
>
> Always required for retransmitted messages, whether prompted by the sending system or as the result of a resend request.
>
> **97 - PossResend** `boolean`
>
> Required when the message may be duplicate of another message sent under a different sequence number.
>
> **52 - SendingTime** `string`
>
> Time of message transmission expressed in UTC. Format: YYYYMMDD-HH:MM:SS.uuu (required).
>
> **122 - OrigSendingTime** `string`
>
> Required for message re-sent as a result of a ResendRequest. If data is not available set to same value as SendingTime (52). Format: YYYYMMDD-HH:MM:SS.uuu
>
> **10 - CheckSum** `string` *required*
>
> Three byte, simple checksum. See the FIX spec for details.
