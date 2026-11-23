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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/sequence-reset'
updated_at: 2026-11-23
---

# Sequence Reset

> Gap fill or hard reset of sequence numbers

FIX
session: admin
35=4

With GapFillFlag=Y this stands in for messages that will not be resent and MsgSeqNum remains meaningful. With GapFillFlag=N it is a hard reset: the counterparty jumps to NewSeqNo and ignores MsgSeqNum. Note that sequence numbers also reset at the daily 22:00 UTC session rollover.

**Direction:** Either direction

***

**header** *required*

35=`4`

**123 - GapFillFlag** `boolean`

Whether this is a gap fill, in which case MsgSeqNum is valid, or a hard sequence reset.

**Possible values:**

* `N` : Hard sequence reset - ignore MsgSeqNum and jump to NewSeqNo.
* `Y` : Gap fill - this SequenceReset stands in for messages that will not be resent; MsgSeqNum is valid.

**36 - NewSeqNo** `SeqNum` *required*

Sequence number the counterparty should expect next.

**trailer** *required*

***

```text Sequence Reset, GapFill theme={null}
8=FIX.4.4|9=81|35=4|49=KRAKEN-PERPS-TRD|56=CLIENT|34=1|43=Y|52=20261027-14:18:17.884|123=Y|36=3|10=053|
```
