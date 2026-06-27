---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/reject-business_level-fix
api_type: REST
updated_at: 2026-05-27 19:43:42.216224
---

# Reject - Business Level

If Kraken needs to reject a message before it reaches the Trading engine and get an orderId, the order, cancellation will be rejected using a Business level reject.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `j`

**45 - RefSeqNum** integer required

Sequence number of the rejected message. 

**372 - RefMsgType** char required

The MsgType `35` of the FIX message being referenced. .

**379 - BusinessRejectRefID** String required

The value of the CLORDID field on the message being rejected. 

**380 - BusinessRejectReason** integer required

Code to identify reason for a Business Message Reject message

  * `0` : Others
  * `1` : Unknown ID
  * `2` : Unknown Instrument
  * `3` : Unsupported Message Type
  * `4` : Application not available
  * `5` : Conditionally Required Field Missing
  * `6` : Not Authorized
  * `101` : Unknown order
  * `104` : Order too old

**58 - text** integer

Full description for rejection. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=134|35=j|34=16|49=KRAKEN-TRD|52=20230707-14:05:37.805|56=MYCOMPID|45=0|58=1688738737 : EOrder:Insufficient funds|372=D|379=1688738737|380=0|10=149|