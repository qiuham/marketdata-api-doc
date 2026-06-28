---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/mdsfr-fix
api_type: Market Data
updated_at: 2026-05-27 19:42:59.344614
---

# Market Data Snapshot Full Refresh

* FIX Specification
  * Spot L2 Example
  * Futures L3 Example

### MESSAGE BODY

**header** `` *required*

MsgType `W`

**262 - MDReqID** string required

Unique request identifier. 

**55 - Symbol** string required

Asset Pair listed on the exchange. 

**268 - NoMDEntries** integer required

Number of entries following.

**269 - MDEntryType** integer required

**Possible values:**
  * `0` : Bid
  * `1` : Offer

Trade will only be transmitted via [Market Data Incremental Refresh](./mdir-fix) messages.

**278 - MDEntryID** string required

Unique identifier for this market data entry. OrderID for the Level3 subcription

**270 - MDEntryPx** float required

Price of the market data entry. 

**271 - MDEntrySize** float required

Volume represented by the market data entry. 

**273 - MDEntryTime** string required

Time of market data entry. 

**5060 - MDEntryTimestamp** string

High-precision event time for this market data update. **Level 3 only.** When present with 5273, 5060 is the time the update was generated; 5273 is the queue entry time.   
**Sample format:** `2026-02-03T10:24:34.650069468Z` (ISO 8601, nanosecond fractional seconds, UTC).

**5273 - MDEntryTimeQueue** string

Queue entry time: when the order entered the book at this price level. **Level 3 only.** For L3, orders at the same price are ordered by this tag.   
**Sample format:** `2026-02-03T10:24:29.175114502Z` (ISO 8601, nanosecond fractional seconds, UTC).

**trailer** `` *required*
    
    
    8=FIX.4.4|9=208|35=W|34=21|49=KRAKEN-MD|52=20230707-13:49:11.245|56=MYCOMPID|55=BTC/USD|262=3|268=2|269=1|278=O30300.0|270=30300.0|271=8.44867022|273=13:49:07.307|269=0|278=B30299.9|270=30299.9|271=0.67373926|273=13:49:10.179|10=254|  
    
    
    
    8=FIX.4.4|9=87775|35=W|34=2|49=KRAKEN-DRV-MD|52=20250304-15:25:09.911|56=MYCOMPID_DRV|55=PF_ETHUSD|262=1|268=10|269=1|278=00bf00ff-00bb-00f7-00ed-006f007f00de|270=2043.1|271=2.05|273=15:25:09.883|269=1|278=009e005a-00b9-0035-00ff-009e00ce007e|270=2043.9|271=2.05|273=15:25:09.767|269=1|278=009f00ff-00b8-0055-00f2-00bf00eb00fd|270=2043.9|271=2.05|273=15:25:09.775|269=1|278=009e00de-00bf-003d-00cf-00df005000ee|270=2044.1|271=1.712|273=15:25:09.894|269=1|278=00bf005f-0034-0035-00ab-00f500d6005d|270=2044.2|271=2.05|273=15:25:09.716|269=1|278=00bf005f-00b9-005d-00fe-00f8004f00ff|270=2044.3|271=1.883|273=15:25:09.711|269=1|278=00be00db-0072-0017-00fe-007f0057006f|270=2044.3|271=1.697|273=15:25:09.863|269=1|278=00bf007a-0030-0097-00dd-00670076007f|270=2044.4|271=3.767|273=15:25:09.844|269=1|278=00bf007a-0035-0095-00b9-007f004700cd|270=2044.4|271=1.712|273=15:25:09.881|269=1|278=009e00df-00bf-009b-00ff-00fc006f0063|270=2044.5|271=2.05|273=15:25:08.520|269=1|278=00bf00ff-0031-00fd-00fe-00f900c900fc|270=2044.5|271=22.605|273=15:25:09.885|10=000|