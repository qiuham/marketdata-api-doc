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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/sequence-reset'
updated_at: 2026-11-13
---

# Sequence Reset

> FIX message used to reset sequence numbering or indicate that a range of sequence numbers will not be transmitted.

The Sequence Reset message is used to reset the sequence numbering or to indicate that a range of sequence numbers will not be transmitted. It can be used as a Gap Fill to indicate that no messages were sent in a range of sequence numbers, or as a Sequence Reset to reset the sequence number to a new value.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `4`
>
> **123 - GapFillFlag** `boolean`
>
> Indicates whether this is a gap fill message.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`Y` : Gap Fill - indicates no messages were sent in a range of sequence numbers</li>
>   <li>`N` or not present : Sequence Reset - resets sequence number to new value</li>
> </ul>
>
> **36 - NewSeqNo** `integer` *required*
>
> New sequence number for next message.
>
> **trailer** *required*
