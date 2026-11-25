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
updated_at: 2026-11-25
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

***

> [accordion] Requests
>
> ```text Resend Request theme={null}
> 8=FIX.4.4|9=74|35=2|49=CLIENT|56=KRAKEN-PERPS-TRD|34=3|52=20261027-14:18:17.642|7=1|16=2|10=167|
> ```

> [accordion] Responses
>
> ```text Sequence Reset, GapFill theme={null}
> 8=FIX.4.4|9=81|35=4|49=KRAKEN-PERPS-TRD|56=CLIENT|34=1|43=Y|52=20261027-14:18:17.884|123=Y|36=3|10=053|
> ```
