---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/ocr-fix
api_type: REST
updated_at: 2026-05-27 19:43:13.601487
---

# Order Cancel Request

Cancel a single GTD or GTC order.

A successful order cancellation will result in an [execution report](/api/docs/fix-api/er-fix) with the OrdStatus set to 4 (Cancelled). Unsuccessful cancellation requests will result in an [business level reject](/api/docs/fix-api/reject-business_level-fix) message with the reason of the rejection.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `F`

**11 - ClOrdID** string required

Unique identifier of the order. The ID can be one of the following formats:

  * **Ever-Increasing Positive Numbers** : Ever-increasing positive numbers, such as microseconds timestamps, to ensure the uniqueness and sequential nature of the identifiers.   
**Example** : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
  * **Timestamp-First v4 UUIDs** : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part need to be 10 microseconds maximum such as `162344829423400`. 

**37 - OrderID** string conditional

**Condition:** One of the Clordid OR OrderID is required at least for the cancellation to be accepted 

OrderId needs to match the one received on the ExecutionReports. 

**41 - OrigClordid** string conditional

**Condition:** One of the Clordid OR OrderID is required at least for the cancellation to be accepted 

Reference the Last ClordId used. If both OrderId and OrigClordid are present then only the OrderID will be used. 

**54 - Side** integer required

Side of the order.

**Possible values:**
  * `1` : Buy
  * `2` : Sell

**55 - Symbol** string required

Pair in the format BASE/QUOTE. 

**60 - TransactTime** string required

**Format:** YYYYDD-HH:MM:SS.uuu

Time of order cancellation expressed in UTC. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=137|35=F|34=5|49=MYCOMPID|52=20230707-13:59:00.000|56=KRAKEN-TRD|11=1688738340|37=OKWUQF-YPJM2-DTAJHH|54=1|55=BTC/USD|60=20230707-13:59:00.023|10=080|