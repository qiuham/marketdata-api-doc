---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/logout-fix
api_type: REST
updated_at: 2026-05-27 19:42:30.800068
---

# Logout

The Logout message initiates or confirms the termination of a FIX session. Disconnection without the exchange of logout messages will be interpreted as an abnormal condition. Before actually closing the session, the logout initiator must wait for the opposite side to respond with a confirming logout message. Abnormal disconnection without logout will activate cancel-on-disconnect on the session.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `5`

**58 - Text** integer

Reason for the logout. This will be used to explain why a logon failed. 
    
    
    8=FIX.4.4|9=59|35=5|49=MYCOMPID|56=KRAKEN-MD|34=10|52=20230707-13:40:01.000|10=229|