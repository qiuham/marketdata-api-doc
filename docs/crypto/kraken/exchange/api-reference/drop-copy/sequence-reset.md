---
exchange: kraken
source_url: https://docs.kraken.com/exchange/api-reference/drop-copy/sequence-reset
api_type: FIX
updated_at: 2026-11-18 01:44:49.568204
---

# Sequence Reset

> Gap fill or hard reset of sequence numbers

FIX
session: drop copy
35=4

With GapFillFlag=Y this stands in for messages that will not be resent and MsgSeqNum remains meaningful. With GapFillFlag=N it is a hard reset: the counterparty jumps to NewSeqNo and ignores MsgSeqNum.

**Direction:** Either direction

***

**header** *required*

35=`4`

**123 - GapFillFlag** `boolean`

Whether this is a gap fill, in which case MsgSeqNum stays valid, or a hard sequence reset.

**Possible values:**

* `Y` : Gap fill - this SequenceReset stands in for messages that will not be resent; MsgSeqNum stays valid.
* `N` : Hard sequence reset - ignore MsgSeqNum and jump to NewSeqNo.

**36 - NewSeqNo** `SeqNum` *required*

Sequence number the counterparty should expect next.

**trailer** *required*