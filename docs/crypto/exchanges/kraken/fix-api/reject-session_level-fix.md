---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/reject-session_level-fix
api_type: REST
updated_at: 2026-05-27 19:43:49.319982
---

# Reject - Session Level

Kraken will disregard any message that is garbled, cannot be parsed or fails a data integrity check. These message will be rejected using the Session Level reject.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `3`

**45 - RefSeqNum** integer required

Sequence number of the rejected message. 

**371 - RefTagID** char conditional

**Condition:** When rejected due to a specific tag 

**372 - RefMsgType** char required

The MsgType `35` of the FIX message being referenced. .

**373 - SessionRejectReason** integer required

Refer to standard FIX 4.4 documentation 

**58 - text** integer

Full description for rejection. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=104|35=3|34=14|49=KRAKEN-TRD|52=20230707-14:04:24.689|56=MYCOMPID|45=12|58=Missing Mandatory Field: Side (54)|10=159