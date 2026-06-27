---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/ocrr-fix
api_type: REST
updated_at: 2026-05-27 19:43:20.730187
---

# Order Cancel Replace Request (Spot only)

The Order Cancel-Replace Request message (MsgType=G) is used by the Client to amend the replaceable fields of working orders which are Quantities and Prices. A successful order replacement request will result in an execution report with the OrdStatus.

  * FIX Specification
  * Example

### MESSAGE BODY

**header** `` *required*

MsgType `G`

**11 - ClOrdID** string required

Unique identifier of the order. The ID can be one of the following formats:

  * **Ever-Increasing Positive Numbers** : Ever-increasing positive numbers, such as microseconds timestamps, to ensure the uniqueness and sequential nature of the identifiers.   
**Example** : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
  * **Timestamp-First v4 UUIDs** : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part need to be 10 microseconds maximum such as `162344829423400`. 

**37 - OrderID** string required

OrderID to be amended; needs to match the one received on the ExecutionReports. 

**41 - OrigClordid** string required

Reference the Last ClordId used. 

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

**38 - OrderQty** float required

Size of the order. 

**1138 - DisplayQty** float

Maximum qty shown in the market at any point in time for iceberg orders. 

**40 - OrderType** char required

The execution model of the order.

**Possible values:**
  * `1` : market
  * `2` : Limit
  * `3` : Stop-loss
  * `4` : Stop-loss-limit
  * `R` : Take-profit
  * `T` : Take-profit-limit
  * `U` : Trailing-stop
  * `V` : Trailing-stop-limit

**59 - TimeInForce** string required

Time-in-force specifies how long an order remains in effect before being expired.

**Possible values:**
  * `1` : GTC (Good till canceled)
  * `3` : IOC (Immediate or Cancel)
  * `4` : FOK (Fill or Kill)
  * `6` : GTD (Good till date)

**44 - Price** float conditional

**Condition:** OrderType=Limit/Stop-Loss-Limit/Take-Profit-Limit/Trailing-stop-limit 

Limit Price of the order to be placed in the Order Book. This field is denominated in Quote Currency.

**99 - StopPx** float conditional

**Condition:** OrderType=Stop-Loss/Take-Profit/Stop-Loss-Limit/Trailing-stop/Trailing-stop-limit 

Defines the trigger price of the order. This field is denominated in Quote Currency. 

**1138 - DisplayQty** float

Iceberg qty. This will indicate the Qty to show on the book. Only possible on Limit order. The Minimum value is 1 / 15 of order_qty. 

**18 - ExecInst** char

Enable clients to place order using the Post-Only safeguard.

**Possible values:**
  * `P` : Post-Only - Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.

**62 - ValidUntilTime** string

**Format:** YYYYDD-HH:MM:SS.uuu

The engine will reject any order entered into the matching engine after this time. This provides extra protection against latency on time sensitive orders. The timestamp should be at least 2 seconds and at most 60 seconds in the future.

**trailer** `` *required*
    
    
    8=FIX.4.4|9=181|35=G|34=3|49=damien_dlt|52=20240625-08:57:05.000|56=KRAKEN-TRD|11=1719305825|37=OTHB2F-BNGUH-2CMLPT|38=0.2|40=2|41=1719305784|44=71000|54=1|55=BTC/USD|59=1|60=20240625-08:57:05.113|10=249|