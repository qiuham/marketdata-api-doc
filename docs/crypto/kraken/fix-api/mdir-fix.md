---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/mdir-fix
api_type: Market Data
updated_at: 2026-05-27 19:42:37.907871
---

# Market Data Incremental Refresh

* FIX Specification
  * Spot L2 Example
  * Futures L2 Example
  * Futures L3 Example

### MESSAGE BODY

**header** `` *required*

MsgType `X`

**262 - MDReqID** string required

Unique request identifier. 

**55 - Symbol** string required

Asset Pair listed on the exchange. 

**268 - NoMDEntries** integer required

Number of entries following. If several entries are present they need to be parsed in order (for example creation and deletion of an entry in the book can happen in the same message)

**279 - MDUpdateAction** integer required

Always first field in this repeating group.

**Possible values:**
  * `0` : New - Creation of an entry in the book
  * `1` : Update - Update of a quantity for an entry in the book
  * `2`: Delete - removal of an entry from the subscribed depth (`271` greater than 0) or from the book entirely (`271=0`, cancelled or filled)

**269 - MDEntryType** integer required

**Possible values:**
  * `0` : Bid
  * `1` : Offer
  * `2` : Trade

**278 - MDEntryID** string required

Unique identifier for this market data entry. Corresponding ot the Order_Id for Level 3 subscription. 

**270 - MDEntryPx** float required

Price of the market data entry. 

**271 - MDEntrySize** float required

Volume represented by the market data entry. 

**273 - MDEntryTime** string required

The time the entry was inserted or amended or deleted. 

**5060 - MDEntryTimestamp** string

High-precision event time for this market data update. **Level 3 only.** When present with 5273, 5060 is the time the update was generated; 5273 is the queue entry time.   
**Sample format:** `2026-02-03T10:24:34.650069468Z` (ISO 8601, nanosecond fractional seconds, UTC).

**5273 - MDEntryTimeQueue** string

Queue entry time: when the order entered the book at this price level. **Level 3 only.** For L3, orders at the same price are ordered by this tag.   
**Sample format:** `2026-02-03T10:24:29.175114502Z` (ISO 8601, nanosecond fractional seconds, UTC).

**40 - OrdType** char conditional

**Condition:** MDEntryType=Trade 

The order type of the taker order.

**Possible values:**
  * `1` : market
  * `2` : Limit

**2446 - AggressorSide** char conditional

**Condition:** MDEntryType=Trade 

The side of the taker order.

**Possible values:**
  * `1` : Buy
  * `2` : Sell

**5041 - ChecksumOrderBook** string conditional

**Condition:** 269= bid or offer 

Checksum to verify that orderbook update. See [ Checksum article](../guides/spot-fix-checksums)

**trailer** `` *required*
    
    
    8=FIX.4.4|9=213|35=X|34=100|56=MYCOMPID|49=KRAKEN-MD|52=20230707-13:42:27.230|55=BTC/USD|262=1|268=2|279=2|269=1|278=O30300.7|270=30300.7|271=0.0|273=13:42:27.208|279=0|269=1|278=O31941.0|270=31941.0|271=0.0031746|273=20:40:00.455|10=112|  
    
    
    
    8=FIX.4.4|9=173|35=X|34=33402|49=KRAKEN-DRV-MD|52=20250303-14:13:24.905|56=MYCOMPID_DRV|55=PF_ETHUSD|262=1|268=1|279=0|269=0|278=B2372.7|270=2372.7|271=0.084|273=14:13:24.859|5041=3254665545|10=121|  
    
    
    
    8=FIX.4.4|9=198|35=X|34=7|49=KRAKEN-DRV-MD|52=20250304-15:25:09.913|56=MYCOMPID_DRV|55=PF_ETHUSD|262=1|268=1|279=2|269=1|278=00bf007e-0039-00dd-0071-00ae00d700c8|270=2044.8|271=2.874|273=15:25:09.844|5041=3889519115|10=012|