---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/tssr-fix
api_type: REST
updated_at: 2026-05-27 19:44:32.350284
---

# Trading Session Status Request (Spot only)

This message will return the status of the market. You can subscribe to have snapshot only or updates as well. A specific status can be also available for individual instrument in the [Instrument List Request](/api/docs/fix-api/slr-fix).

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `g`

**335 - TradSesReqID** string required

Unique request identifier .

**336 - TradingSessionID** string required

Trading Session identifier.

**263 - SubscriptionRequestType** integer required

**Possible values:**
  * `0` : Snapshot only
  * `1` : Snapshot + Updates

**trailer** `` *required*
    
    
    8=FIX.4.4|9=85|35=g|34=6|49=MYCOMPID|52=20230707-13:50:02.000|56=KRAKEN-MD|263=0|335=TSS0|336=SESSION|10=247|