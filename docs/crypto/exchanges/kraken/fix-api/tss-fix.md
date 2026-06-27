---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/tss-fix
api_type: REST
updated_at: 2026-05-27 19:44:25.134051
---

# Trading Session Status (Spot only)

* FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `h`

**335 - TradSesReqID** string required

Unique request identifier .

**336 - TradingSessionID** string required

Trading Session identifier.

**340 - TradSesStatus** integer

**Possible values:**
  * `0` : unknown
  * `1` : Maintenance - Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
  * `2` : Online - Markets are operating normally - all order types may be submitted and order matching can occur.
  * `101` : cancel_only - Orders can be cancelled but new orders cannot be placed. No order matching will occur.
  * `102` : post_only - Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.

**567 - TradSesStatusRejReason** integer

**Possible values:**
  * `1` : UNKNOWNTRADINGSESSIONID
  * `100` : INVALIDREQUESTID
  * `101` : INVALIDSUBSTYPE
  * `102` : DUPLICATEREQUESTID
  * `103` : ALREADYSUBSCRIBED

**trailer** `` *required*
    
    
    8=FIX.4.4|9=85|35=h|34=5|49=KRAKEN-MD|52=20230707-13:50:02.413|56=MYCOMPID|335=TSS0|336=SESSION|340=2|10=253|