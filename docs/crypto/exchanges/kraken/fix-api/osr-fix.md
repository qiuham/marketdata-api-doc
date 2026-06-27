---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/osr-fix
api_type: REST
updated_at: 2026-05-27 19:43:34.973816
---

# Order Status Request ( Spot Only )

This request is used by clients to obtain information about current order status on Kraken exchange. As a response to this request, Order Status is sent on [execution report](/api/docs/fix-api/er-fix) with ExecType = `I`. Tag 39 on this response would give away current order status.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `H`

**11 - ClOrdID** string required

Unique identifier of the order. The ID can be one of the following formats:

  * **Ever-Increasing Positive Numbers** : Ever-increasing positive numbers, such as microseconds timestamps, to ensure the uniqueness and sequential nature of the identifiers.   
**Example** : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
  * **Timestamp-First v4 UUIDs** : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part need to be 10 microseconds maximum such as `162344829423400`. 

**37 - OrderID** string required

OrderId needs to match the one received on the ExecutionReports. 

**55 - Symbol** string required

Pair in the format BASE/QUOTE. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=137|35=H|34=5|49=MYCOMPID|52=20230707-13:59:00.000|56=KRAKEN-TRD|11=1688738340|37=OKWUQF-YPJM2-DTAJHH|54=1|55=BTC/USD|60=20230707-13:59:00.023|10=080|