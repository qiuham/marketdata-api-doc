---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/sequence-reset-fix
api_type: REST
updated_at: 2026-05-27 19:43:56.566777
---

# Sequence Reset

* FIX Specification

### MESSAGE BODY

**header** `` *required*

MsgType `4`

**123 - SequenceReset** boolean required

**Possible values:**[`true`, ` false`] 

Indicates that the Sequence Reset (4) message is replacing administrative or application messages which will not be resent.  
* `Y` : Gap Fill message, MsgSeqNum field valid
  * `N` : Sequence Reset, ignore MsgSeqNum

**36 - NewSeqNo** integer required

New sequence number. 

**trailer** `` *required*