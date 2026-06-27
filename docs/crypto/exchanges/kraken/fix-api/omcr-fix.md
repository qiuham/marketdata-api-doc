---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/omcr-fix
api_type: REST
updated_at: 2026-05-27 19:43:27.857027
---

# Order Mass Cancel Request

This request is used by clients to cancel all open orders including untriggered orders and orders resting in the book. As a response to this request, Kraken will confirm each order cancelation through [execution report](/api/docs/fix-api/er-fix) type canceled.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `q`

**11 - ClOrdID** string required

Unique identifier of the order. The ID can be one of the following formats:

  * **Ever-Increasing Positive Numbers** : Ever-increasing positive numbers, such as microseconds timestamps, to ensure the uniqueness and sequential nature of the identifiers.   
**Example** : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
  * **Timestamp-First v4 UUIDs** : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part need to be 10 microseconds maximum such as `162344829423400`. 

**60 - TransactTime** string required

**Format:** YYYYMMDD-HH:MM:SS.uuu

Time of order cancellation expressed in UTC. 

**530 - MassCancelRequestType** integer required

**Possible values:**
  * `1` : Cancel all orders created or replaced during the trading Session by Symbol
  * `6` : Cancel all orders created or replaced during the trading Session
  * `7` : Cancel all open orders created by the SenderCompID

**55 - Symbol** string conditional

**Condition:** MassCancelRequestType=1 

The pair in format BASE/QUOTE. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=115|35=q|34=6|49=MYCOMPID|52=20230707-13:59:36.000|56=KRAKEN-TRD|11=1688738376|55=BTC/USD|60=20230707-13:59:36.422|530=1|10=193|