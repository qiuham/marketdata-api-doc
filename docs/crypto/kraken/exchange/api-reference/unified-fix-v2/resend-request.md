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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/resend-request'
updated_at: 2026-11-13
---

# Resend Request

> Request retransmission after a sequence gap

FIX
session: admin
35=2

Sent by either side when an incoming MsgSeqNum is higher than expected, asking for the messages in the gap. The counterparty answers either with the original messages carrying PossDupFlag=Y, or with a Sequence Reset carrying GapFillFlag=Y for administrative messages it will not replay. Expect one whenever a client reconnects to an existing session without resetting sequence numbers.

**Direction:** Either direction

***

**header** *required*

35=`2`

**7 - BeginSeqNo** `SeqNum` *required*

First message sequence number to retransmit.

**Format:** Sequence number of the first message to retransmit.

**16 - EndSeqNo** `SeqNum` *required*

Last message sequence number to retransmit. Zero requests everything from BeginSeqNo onwards.

**Format:** Sequence number, or 0 to request everything from BeginSeqNo onwards.

**trailer** *required*
