---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/nos-fix
api_type: REST
updated_at: 2026-05-27 19:43:06.451248
---

# New Order Single

To submit a new order, the client needs to send a NewOrderSingle message. All orders are submitted from the client’s perspective to Kraken exchange to place bid/offer on the Kraken Order book. A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

The supported order types are:

  * `market`: The full order quantity executes immediately at the best available price in the order book.
  * `limit`: The full order quantity is placed immediately with a limit price restriction to only trade at this price or better.
  * `stop-loss`: A market order is triggered when the reference price reaches the stop price (from an unfavourable direction).
  * `stop-loss-limit`: A limit order is triggered when the reference price reaches the stop price (from an unfavourable direction).
  * `take-profit`: A market order is triggered when the reference price reaches the stop price (from an favourable direction).
  * `take-profit-limit`: A limit order is triggered when the reference price reaches the stop price (from an favourable direction).
  * `trailing-stop`: A market order is triggered when the market reverts a specified distance from the peak price.
  * `trailing-stop-limit`: A limit order is triggered when the market reverts a specified distance from the peak price.
* FIX Specification
  * Spot Example
  * Futures Example

### MESSAGE BODY

**header** `` *required*

MsgType `D`

**11 - ClOrdID** string required

Unique identifier of the order. The ID can be one of the following formats:

  * **Ever-Increasing Positive Numbers** : Ever-increasing positive numbers, such as microseconds timestamps, to ensure the uniqueness and sequential nature of the identifiers. (Spot only)   
**Example** : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
  * **Timestamp-First v4 UUIDs** : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp. The timestamp granularity to generate the first part need to be 10 microseconds maximum such as `162344829423400`. 

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
  * `V` : Trailing-stop-limit (Spot only) 

**44 - Price** float conditional

**Condition:** OrderType=Limit/Stop-Loss-Limit/Take-Profit-Limit/Trailing-stop-limit 

Limit Price of the order to be placed in the Order Book. This field is denominated in Quote Currency.

**38 - OrderQty** float required

Order quantity in terms of the base asset.

**1138 - DisplayQty** float

Iceberg qty. This will indicate the Qty to show on the book. Only possible on Limit order. The Minimum value is 1 / 15 of order_qty. (Spot only)

**54 - Side** integer required

Side of the order.

**Possible values:**
  * `1` : Buy
  * `2` : Sell

**55 - Symbol** string required

Pair in the format BASE/QUOTE.

**59 - TimeInForce** string required

Time-in-force specifies how long an order remains in effect before being expired.

**Possible values:**
  * `1` : GTC (Good till canceled)
  * `3` : IOC (Immediate or Cancel)
  * `4` : FOK (Fill or Kill)
  * `6` : GTD (Good till date) - (Spot only) 

**60 - TransactTime** string required

**Format:** YYYYMMDD-HH:MM:SS.uuu

Time of order creation expressed in UTC. 

**126 - ExpireTime** string conditional

**Condition:** TimeinForce=GTD 

**Format:** YYYYMMDD-HH:MM:SS

Expiration of the Order if not fully filled before it. Expressed in UTC. GTD orders can have an expiry time up to one month in future. (Spot only) 

**168 - EffectiveTime** string

Scheduled start time on the order expressed in UTC. the order won't be visible on the book and won't match before that time. (Spot only) 

**18 - ExecInst** char

If more than one instruction is applicable to an order, this field may contain multiple instructions separated by space.

**Possible values:**
  * `E` : Reduce-Only - Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
  * `P` : Post-Only - Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
  * `v` : viqc - Orderqty (tag 38) expressed in quote currency. (Spot Only) 
  * `f` : Cumulative fee in base currency - base is the default for sell orders. (Spot Only)
  * `q` : Cumulative fee in quote currency - quote is the default for buy orders. (Spot Only)
  * `s` : Single fee - Mandatory and only supported fee option for derivatives - fee sent on the execution report are based on the trade.

**99 - StopPx** float conditional

**Condition:** OrderType=Stop-Loss/Take-Profit/Stop-Loss-Limit/Trailing-stop/Trailing-stop-limit 

Defines the trigger price of the order. This field is denominated in Quote Currency. 

**388 - DiscretionInst** integer

The reference price to track for triggering orders.

**Possible values:**
  * `1` :Related to index price
  * `5` :Related to last trade price
**Default value:`5`**

**5001 - Leverage** string

Use margin account for the order funding. (Spot only)

**Possible values:**
  * `0` :Margin disabled 
  * `1` :Margin enabled
**Default value:`0`**

**7928 - SelfTradePrevention** integer

Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves. To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired. (Spot only)

**Possible values:**
  * `0` : Cancel both - both arriving and resting orders will be canceled.
  * `1` : Cancel Newest - arriving order will be canceled.
  * `2` : Cancel Oldest - resting order will be canceled.
**Default value:`1`**

**78 - NoAllocs** integer

Number of subaccount that are part of the order. Always 1 for the broker accounts.

**79 - AllocAccount** String

Account ID of the Subaccount that this order is targeted to. Only available for Broker accounts. Please contact your AM for further questions.

**62 - ValidUntilTime** string

**Format:** YYYYMMDD-HH:MM:SS.uuu

The engine will reject any order entered into the matching engine after this time. This provides extra protection against latency on time sensitive orders. The timestamp should be at least 2 seconds and at most 60 seconds in the future.

**trailer** `` *required*
    
    
    8=FIX.4.4|9=140|35=D|34=2|49=MYCOMPID|52=20230707-13:56:08.000|56=KRAKEN-TRD|11=1688738168|38=0.01|40=2|44=1000|54=1|55=BTC/USD|59=1|60=20230707-13:56:08.277|10=222|  
    
    
    
    8=FIX.4.4|9=181|35=D|34=2|49=damien2_DRV|52=20250303-14:09:32.902|56=KRAKEN-DRV-TRD|11=9e58120f-182b-4dce-9609-8ca7cdd174f0|18=s|38=0.1|40=2|44=1000|54=1|55=PF_ETHUSD|59=1|60=20250303-14:09:32.896|10=148|  
    

Order Validation

Kraken will validate each order it receives by checking that the user sent all the required FIX fields for the order.

  * FIX field level validation will result in [session level reject](/api/docs/fix-api/reject-session_level-fix).
  * Business rule validation failures will result in rejection in the form of an [business level reject](/api/docs/fix-api/reject-business_level-fix)
  * Once the order is accepted and Acked, any further Business rule validations that will result in an [execution report](/api/docs/fix-api/er-fix) with an unsolicited cancel status.