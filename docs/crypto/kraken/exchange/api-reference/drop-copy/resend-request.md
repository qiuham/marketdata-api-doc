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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy/resend-request'
updated_at: 2026-11-25
---

# Resend Request

> Request retransmission after a sequence gap

FIX
session: drop copy
35=2

Asks the counterparty to retransmit a range of messages after a sequence gap is detected. The counterparty answers either with the original messages carrying PossDupFlag=Y, or with a Sequence Reset carrying GapFillFlag=Y for administrative messages it will not replay.

**Direction:** Either direction

***

**header** *required*

35=`2`

**7 - BeginSeqNo** `SeqNum` *required*

First message sequence number to retransmit.

**Format:** Sequence number of the first message to retransmit.

**16 - EndSeqNo** `SeqNum` *required*

Last message sequence number to retransmit. Zero requests everything from BeginSeqNo onwards.

**Format:** Sequence number, or 0 for everything from BeginSeqNo onwards.

**trailer** *required*
