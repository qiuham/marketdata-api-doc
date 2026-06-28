---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/mdrr-fix
api_type: Market Data
updated_at: 2026-05-27 19:42:52.200894
---

# Market Data Request Reject

* FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `Y`

**262 - MDReqID** string required

Unique request identifier. 

**281 - MDReqRejReason** integer required

**Possible values:**
  * `0` : Unknown Symbol
  * `1` : Duplicate MDReqID
  * `4` : Unsupported SubscriptionRequestType
  * `5`: Unsupported MarketDepth
  * `6` : Unsupported MDUpdateType
  * `8` : Unsupported MDEntryType
  * `A` : Unsupported Scope
  * `B` : Level3 not available
  * `C` : Trade not available on this request

**58 - Text** integer

Full description for rejection. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=141|35=Y|34=3|49=KRAKEN-MD|52=20230707-13:47:50.963|56=MYCOMPID|58=MarketData subscription failed due to unsupported symbol: TEST/TEST|262=1|281=0|10=142