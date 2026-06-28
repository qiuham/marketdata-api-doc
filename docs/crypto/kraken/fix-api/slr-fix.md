---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/slr-fix
api_type: REST
updated_at: 2026-05-27 19:44:17.991021
---

# Instrument List Request

The InstrumentListRequest message is used to return a list of securities from the exchange that match the criteria provided on the request. We recommend that clients send an InstrumentListRequest on any new connection or reconnection as the status of the Instrument might have changed during the disconnection.

  * FIX Specification

### MESSAGE BODY

**header** `` *required*

MsgType `x`

**320 - InstrumentReqID** string required

Unique request identifier .

**263 - SubscriptionRequestType** integer

**Possible values:**
  * `0` : Snapshot 
  * `1` : Snapshot + Updates
  * `2` : Disable previous snapshot + Update request

**559 - InstrumentListRequestType** integer required

**Possible values:**
  * `0` : Single asset pair definition
  * `1` : SecurityType
  * `4` : All Securities

**167 - SecurityType** string conditional

**Condition:** InstrumentListRequestType=1 

**Possible values:**
  * `CASH` : Spot only instruments
  * `FUT` : Futures only instruments
  * `OPT` : Options only instruments
  * `TS` : Tokenized stocks only instruments, i.e. xStocks

**55 - Symbol** string conditional

**Condition:** InstrumentListRequestType=0 

Format should be BASE/QUOTE. 

**trailer** `` *required*