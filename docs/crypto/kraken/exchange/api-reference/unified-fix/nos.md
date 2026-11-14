---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/nos'
updated_at: 2026-11-13
---

# New Order Single

> Submit a new order via FIX

FIX
session: trading
35=D

To submit a new order, the client needs to send a NewOrderSingle message. All orders are submitted from the client's perspective to Kraken exchange to place bid/offer on the Kraken Order book.
A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

The supported order types are:

* `market`: The full order quantity executes immediately at the best available price in the order book.
* `limit`: The full order quantity is placed immediately with a limit price restriction to only trade at this price or better.
* `stop-loss`: A market order is triggered when the reference price reaches the stop price (from an unfavourable direction).
* `stop-loss-limit`: A limit order is triggered when the reference price reaches the stop price (from an unfavourable direction).
* `take-profit`: A market order is triggered when the reference price reaches the stop price (from a favourable direction).
* `take-profit-limit`: A limit order is triggered when the reference price reaches the stop price (from a favourable direction).
* `trailing-stop`: A market order is triggered when the market reverts a specified distance from the peak price.
* `trailing-stop-limit`: A limit order is triggered when the market reverts a specified distance from the peak price.

***

**header** *required*

35=`D`

**11 - ClOrdID** `string` *required*

Unique identifier of the order. The ID can be one of the following formats:

* **Ever-Increasing Positive Numbers**: Ever-increasing positive numbers, such as microsecond timestamps, to ensure the uniqueness and sequential nature of the identifiers. (Spot only)
  **Example**: Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (Max 18 characters)
* **Timestamp-First v4 UUIDs** (required for Futures, supported for Spot): A COMB UUID where the first 48 bits (first two UUID fields) encode the current timestamp in **10-microsecond units** since the Unix epoch. Example: `a17d49af-1186-4984-bd10-29b8f232ee4d`, where `a17d49af-1186` encodes the timestamp `177559467882990` (= 10-μs units for a given moment). The server validates that this timestamp is within 120 seconds of server time.

**40 - OrderType** `char` *required*

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

**44 - Price** `float`

Limit Price of the order to be placed in the Order Book. This field is denominated in Quote Currency.

Condition: OrderType = Limit / Stop-Loss-Limit / Take-Profit-Limit / Trailing-stop-limit

**38 - OrderQty** `float` *required*

Order quantity in terms of the base asset.

**1138 - DisplayQty** `float`

Iceberg qty. This will indicate the Qty to show on the book.
Only possible on Limit order. The Minimum value is 1 / 15 of order\_qty. (Spot only)

**54 - Side** `integer` *required*

Side of the order.

**Possible values:**

* `1` : Buy
* `2` : Sell

**55 - Symbol** `string` *required*

Pair in the format BASE/QUOTE.

**59 - TimeInForce** `string` *required*

Time-in-force specifies how long an order remains in effect before being expired.

**Possible values:**

* `1` : GTC (Good till canceled)
* `3` : IOC (Immediate or Cancel)
* `4` : FOK (Fill or Kill) — The order must be filled in its entirety immediately or canceled entirely. (Spot only)
* `6` : GTD (Good till date) - (Spot only)

**60 - TransactTime** `string` *required*

Time of order creation expressed in UTC. Format: `YYYYMMDD-HH:MM:SS.uuu`

**126 - ExpireTime** `string`

Expiration of the Order if not fully filled before it. Expressed in UTC. GTD orders can have an expiry time up to one month in future. (Spot only) Format: `YYYYMMDD-HH:MM:SS`

Condition: TimeInForce = GTD

**168 - EffectiveTime** `string`

Scheduled start time on the order expressed in UTC. The order won't be visible on the book and won't match before that time. (Spot only)

**18 - ExecInst** `char`

If more than one instruction is applicable to an order, this field may contain multiple instructions separated by space.

**Possible values:**

* `E` : Reduce-Only — Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
* `P` : Post-Only — Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
* `v` : viqc — OrderQty (tag 38) expressed in quote currency. (Spot only)
* `f` : Cumulative fee in base currency — base is the default for sell orders. (Spot only)
* `q` : Cumulative fee in quote currency — quote is the default for buy orders. (Spot only)
* `s` : Single fee — Mandatory and only supported fee option for derivatives — fee sent on the execution report are based on the trade.

**99 - StopPx** `float`

Defines the trigger price of the order. This field is denominated in Quote Currency.

Condition: OrderType = Stop-Loss / Take-Profit / Stop-Loss-Limit / Trailing-stop / Trailing-stop-limit

**388 - DiscretionInst** `integer`

The reference price to track for triggering orders.

**Possible values:**

* `1` : Related to index price
* `5` : Related to last trade price

**Default value:** `5`

**5001 - Leverage** `string`

Use margin account for the order funding. (Spot only)

**Possible values:**

* `0` : Margin disabled
* `1` : Margin enabled

**Default value:** `0`

**7928 - SelfTradePrevention** `integer`

Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves.
To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired. (Spot only)

**Possible values:**

* `0` : Cancel both — both arriving and resting orders will be canceled.
* `1` : Cancel Newest — arriving order will be canceled.
* `2` : Cancel Oldest — resting order will be canceled.

**Default value:** `1`

**78 - NoAllocs** `integer`

Number of subaccount that are part of the order. Always 1 for the broker accounts.

**repeating group**

**79 - AllocAccount** `string`

Account ID of the Subaccount that this order is targeted to. Only available for Broker accounts. Please contact your AM for further questions.

**62 - ValidUntilTime** `string`

The engine will reject any order entered into the matching engine after this time. This provides extra protection against latency on time sensitive orders. The timestamp should be at least 2 seconds and at most 60 seconds in the future. Format: `YYYYMMDD-HH:MM:SS.uuu`

**trailer** *required*

***

> [!NOTE]
>
> **Order Validation** — Kraken will validate each order it receives by checking that the user sent all the required FIX fields for the order.
>
> * FIX field level validation will result in [session level reject](https://docs.kraken.com/exchange/api-reference/unified-fix/reject-session.md).
> * Business rule validation failures will result in rejection in the form of a [business level reject](https://docs.kraken.com/exchange/api-reference/unified-fix/reject-business.md).
> * Once the order is accepted and Acked, any further business rule validations will result in an [execution report](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md) with an unsolicited cancel status.

> [tab] Spot
>
> ```text Limit (GTC) theme={null}
> 8=FIX.4.4|9=148|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036325000000|55=BTC/USD|54=1|40=2|44=84000|38=0.001|59=1|60=20260407-14:32:05.000|10=141|
> ```
>
> ```text Market theme={null}
> 8=FIX.4.4|9=139|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036325200000|55=BTC/USD|54=1|40=1|38=0.001|59=1|60=20260407-14:32:05.000|10=236|
> ```
>
> ```text IOC theme={null}
> 8=FIX.4.4|9=148|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036325300000|55=BTC/USD|54=1|40=2|44=84000|38=0.001|59=3|60=20260407-14:32:05.000|10=146|
> ```
>
> ```text FOK theme={null}
> 8=FIX.4.4|9=148|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036335000000|55=BTC/USD|54=1|40=2|44=84000|38=0.001|59=4|60=20260407-14:32:05.000|10=145|
> ```
>
> ```text GTD theme={null}
> 8=FIX.4.4|9=170|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036325400000|55=BTC/USD|54=1|40=2|44=84000|38=0.001|59=6|126=20260408-14:32:05|60=20260407-14:32:05.000|10=206|
> ```
>
> ```text Post-Only theme={null}
> 8=FIX.4.4|9=153|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036326000000|55=BTC/USD|54=1|40=2|44=83000|38=0.001|59=1|18=P|60=20260407-14:32:05.000|10=128|
> ```
>
> > [accordion] Conditional orders
> >
> > ```text Stop-Loss theme={null}
> > 8=FIX.4.4|9=148|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036327000000|55=BTC/USD|54=2|40=3|99=80000|38=0.001|59=1|60=20260407-14:32:05.000|10=151|
> > ```
> >
> > ```text Stop-Loss-Limit theme={null}
> > 8=FIX.4.4|9=157|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036328000000|55=BTC/USD|54=2|40=4|99=80000|44=79500|38=0.001|59=1|60=20260407-14:32:05.000|10=068|
> > ```
> >
> > ```text Take-Profit theme={null}
> > 8=FIX.4.4|9=148|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036329000000|55=BTC/USD|54=2|40=R|99=90000|38=0.001|59=1|60=20260407-14:32:05.000|10=185|
> > ```
> >
> > ```text Take-Profit-Limit theme={null}
> > 8=FIX.4.4|9=157|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036330000000|55=BTC/USD|54=2|40=T|99=90000|44=90500|38=0.001|59=1|60=20260407-14:32:05.000|10=087|
> > ```
> >
> > ```text Trailing-Stop theme={null}
> > 8=FIX.4.4|9=147|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036331000000|55=BTC/USD|54=2|40=U|99=2000|38=0.001|59=1|60=20260407-14:32:05.000|10=125|
> > ```
>
> > [accordion] Iceberg and margin
> >
> > ```text Iceberg theme={null}
> > 8=FIX.4.4|9=157|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036332000000|55=BTC/USD|54=1|40=2|44=84000|38=0.15|1138=0.01|59=1|60=20260407-14:32:05.000|10=042|
> > ```
> >
> > ```text Margin theme={null}
> > 8=FIX.4.4|9=155|35=D|34=2|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:05.000|11=1744036333000000|55=BTC/USD|54=1|40=2|44=84000|38=0.001|59=1|5001=1|60=20260407-14:32:05.000|10=191|
> > ```

> [tab] Futures
>
> ```text Limit (COMB UUID + ExecInst=s) theme={null}
> 8=FIX.4.4|9=183|35=D|34=2|49=CLIENT-DRV|56=KRAKEN-DRV-TRD|52=20260407-14:32:05.000|11=a17d4971-f00d-4f67-94d1-e7d604104ed2|55=PF_XBTUSD|54=1|40=2|44=84000|38=0.001|59=1|18=s|60=20260407-14:32:05.000|10=163|
> ```
>
> ```text Market theme={null}
> 8=FIX.4.4|9=173|35=D|34=3|49=CLIENT-DRV|56=KRAKEN-DRV-TRD|52=20260407-14:32:05.000|11=a17d4972-1001-4abc-def0-1234567890ab|55=PF_ETHUSD|54=2|40=1|38=0.01|59=1|18=s|60=20260407-14:32:05.000|10=179|
> ```
>
> ```text Stop-Loss theme={null}
> 8=FIX.4.4|9=183|35=D|34=4|49=CLIENT-DRV|56=KRAKEN-DRV-TRD|52=20260407-14:32:05.000|11=a17d4973-1001-4abc-def0-1234567890ab|55=PF_XBTUSD|54=2|40=3|99=80000|38=0.001|59=1|18=s|60=20260407-14:32:05.000|10=157|
> ```
