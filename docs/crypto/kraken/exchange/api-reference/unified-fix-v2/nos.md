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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/nos'
updated_at: 2026-11-28
---

# New Order Single

> Submit a new order on the US Perps order book

FIX
session: trading
35=D

Submits a new order onto the perps order book.

**Direction:** Client → Kraken

***

**header** *required*

35=`D`

**11 - ClOrdID** `string` *required*

Client-assigned order identifier, unique within the trading session. On US Perps it must be a positive integer of at most 19 digits (a positive int64). Use an ever-increasing number, for example a microsecond timestamp. With `RelaxedClOrdID=Y` on Logon the value no longer has to increase, but it must still be a positive integer and must never be reused within the session.

**Format:** Positive integer, up to 19 digits, e.g. a microsecond timestamp.

**How invalid values are rejected:**

* A value that is not an integer is rejected with a Reject (`35=3`) and `SessionRejectReason (373)` = `5`.
* Without `RelaxedClOrdID=Y`, a valid timestamp-first COMB UUIDv4 passes session validation and is rejected only on NewOrderSingle, with a BusinessMessageReject (`35=j`): "numeric ClOrdID required on this venue".
* With `RelaxedClOrdID=Y`, anything other than a positive int64 is rejected with `35=3` and reason `5`.

> [!NOTE]
>
> **ClOrdID: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | Accepted format | Positive integer, up to 19 digits | UUIDs (36 characters) are accepted | Timestamp-first COMB UUIDv4 required |

**1 - Account** `string` *required*

Numeric end-client id identifying the end client the order is placed for. Required on every order and must be a non-zero numeric value. Orders without it are rejected with "Account is required on this venue", and non-numeric values with "numeric account id required". It also identifies the end client for self-trade prevention.

**Format:** Non-zero numeric end-client id.

**18 - ExecInst** `MultipleStringValue`

One or more execution instructions, space-separated.

**Possible values:**

* `P` : Post-only. Limit orders only. The order is rejected instead of taking liquidity.
* `n` : No market price protection. Market orders only.

**55 - Symbol** `string`

Perpetual futures contract, in the venue symbol form. Ten contracts are listed at launch. Either Symbol or InstrumentID must be sent. Ignored when InstrumentID is also sent: the instrument is then recognised from InstrumentID.

**Format:** Venue symbol.

Required: Conditional

**48 - InstrumentID** `string`

Identifier of the instrument within the identification scheme named by InstrumentIDSource. Either Symbol or InstrumentID must be sent.\
Where both Symbol and InstrumentID are sent, InstrumentID is what the instrument is recognised from and Symbol is ignored.

**Format:** Venue instrument identifier. Takes precedence over Symbol when both are sent.

Required: Conditional

**22 - InstrumentIDSource** `string`

Identification scheme that InstrumentID is expressed in.

**Possible values:**

* `8` : Exchange symbol.

**54 - Side** `char` *required*

Side of the order.

**Possible values:**

* `1` : Buy.
* `2` : Sell.

**60 - TransactTime** `UTCTimestamp` *required*

Time of the business event in UTC, formatted YYYYMMDD-HH:MM:SS.uuu.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**38 - OrderQty** `Qty` *required*

Order quantity in Min Tradable Contracts. One Min Tradable Contract is the smallest quantity the contract trades in, a fraction of a contract: where that is one ten-thousandth of a contract, a quantity of `1` is 0.0001 contract, not one contract. On US Perps it must be a whole number of Min Tradable Contracts and not below the contract's minimum order quantity. An order that is not is rejected before it reaches the matching engine, with a Reject (`35=3`), `SessionRejectReason (373)` = `5` and `RefTagID (371)` = `38`. Text (58) gives the increment or the minimum.

**40 - OrdType** `char` *required*

Execution model of the order.

**Possible values:**

* `1` : Market - fill the whole quantity immediately at the best available prices.
* `2` : Limit - rest in the book, trading only at the limit price or better.

**44 - Price** `Price`

Limit price of the order, denominated in the quote currency. Required for limit orders.

**Format:** Limit price, denominated in the quote currency.

**Tick size:** On US Perps the price must be a multiple of the instrument's `tickSize` (see the [SBE instrument definition](https://docs.kraken.com/exchange/api-reference/sbe/instrument-definition-snapshot.md)). A price that is not is rejected before it reaches the matching engine, with a Reject (`35=3`), `SessionRejectReason (373)` = `5` and `RefTagID (371)` = `44`; Text (58) gives the tick size. If an instrument has no usable tick size, a priced order on it is refused with a BusinessMessageReject (`35=j`): "Instrument tick size is unavailable".

Required: Conditional

**59 - TimeInForce** `char` *required*

How long the order stays in effect. GTC, IOC, FOK and GTD are accepted; a change of TimeInForce on an amend is rejected.

**Possible values:**

* `1` : GTC - good till cancelled. Rests indefinitely.
* `3` : IOC - fill what you can immediately, cancel the rest.
* `4` : FOK - fill the entire quantity immediately or cancel the whole order.
* `6` : GTD - good till date. Rests until the expiry in `ExpireTime (126)`, which is then required.

**126 - ExpireTime** `UTCTimestamp`

Expiry of a good-till-date order, in UTC. Required when TimeInForce (59) is `6`. A GTC order (`59=1`) that carries ExpireTime is not rejected: it silently becomes good-till-date, so leave ExpireTime out of GTC orders.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

Required: Conditional

**1138 - DisplayQty** `Qty`

Visible size of an iceberg order. Limit orders only: on any other order type the order is rejected. It is held to the same minimum and increment as OrderQty (38).

> [!NOTE]
>
> **GTD and DisplayQty: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | GTD (`59=6` with `ExpireTime`) | Accepted | Supported | Supported |
> | DisplayQty (1138) | Supported (iceberg orders, limit orders only) | Supported | Not read as a size, but its presence turns the order into an iceberg order with no display size, so do not send it |

**168 - EffectiveTime** `UTCTimestamp`

Scheduled start time. Not supported on US Perps: an order that carries it is rejected with a BusinessMessageReject (`35=j`).

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**62 - ValidUntilTime** `UTCTimestamp`

On US Perps the value is only range-checked: it must be between 2 and 60 seconds in the future, formatted YYYYMMDD-HH:MM:SS.uuu. It is not sent to the matching engine, so it does not reject an order that arrives late. It is rejected on an amend.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu, and between 2 and 60 seconds in the future.

> [!NOTE]
>
> **ValidUntilTime: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | Behaviour | Range-checked only; never sent to the engine; rejected on amend | Forwarded to the back end as a deadline | Forwarded to the back end as a deadline |
> | Minimum distance | 2 seconds | Varies by deployment, from 1 ms to 2 s | Varies by deployment, 50 ms or 2 s |

**5001 - Margin** `char`

Whether the order draws on the margin account. Margin=`1` is rejected on US Perps with a BusinessMessageReject (`35=j`); Margin=`0` is accepted and has no effect.

**Possible values:**

* `0` : Fund the order from the cash account. Default. Accepted on US Perps and has no effect.
* `1` : Fund the order from the margin account. Rejected on US Perps.

> [!NOTE]
>
> **EffectiveTime and Margin: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | EffectiveTime (168) | Rejected (`35=j`) | Supported | Forwarded by the gateway |
> | Margin (5001) | `1` rejected (`35=j`); `0` accepted, no effect | Supported | Forwarded by the gateway |

**7928 - SelfTradePrevention** `char`

Self-trade prevention mode, deciding which order is expired when your own orders would match. Defaults to cancelling the newest.

**Possible values:**

* `0` : Cancel both - the arriving and the resting order are both cancelled.
* `1` : Cancel newest - the arriving order is cancelled. Default.
* `2` : Cancel oldest - the resting order is cancelled.

**trailer** *required*

***

> [!NOTE]
>
> The examples are UAT captures. The symbols, InstrumentIDs and account `12345` are UAT test values: use a contract listed for production and your own account. The ExecID (17) values are in the earlier form, captured before the ExecID change, and will be replaced with captures in the new form after the cutover.

> [accordion] Requests
>
> ```text Limit order, GTC, by Symbol theme={null}
> 8=FIX.4.4|9=160|35=D|49=CLIENT|56=KRAKEN-PERPS-TRD|34=25|52=20261027-11:51:30.659|11=1793101834495177|1=12345|55=PBTCUCZ50|54=1|60=20261027-11:50:34.479|38=100|40=2|44=15|59=1|10=189|
> ```
>
> ```text Limit order, GTC, by InstrumentID theme={null}
> 8=FIX.4.4|9=173|35=D|49=CLIENT|56=KRAKEN-PERPS-TRD|34=3|52=20261026-16:09:28.559|11=1793030888862644|1=12345|48=9189124771557588612|22=8|54=1|60=20261026-16:08:08.861|38=1|40=2|44=250|59=1|10=193|
> ```
>
> ```text Limit order, FOK, not fillable theme={null}
> 8=FIX.4.4|9=178|35=D|49=CLIENT|56=KRAKEN-PERPS-TRD|34=23|52=20261030-22:35:16.884|11=38007374505886700|1=12345|48=9189124771557588612|22=8|54=1|60=20261030-22:35:16.884|38=1|40=2|44=249.01|59=4|10=173|
> ```

> [accordion] Responses
>
> ```text Execution Report, New theme={null}
> 8=FIX.4.4|9=316|35=8|49=KRAKEN-PERPS-TRD|56=CLIENT|34=21|52=20261027-11:51:30.928|37=1793101890928737584|11=1793101834495177|17=ZESOIDORLYDAA:KHHOMZVLMDRBQ|150=0|39=0|1=12345|55=PBTCUCZ50|48=12184107997830506656|54=1|38=100.0|40=2|44=15.0|59=1|151=100.0|14=0.0|6=0.0|60=20261027-11:51:30.928|381=0.0|58=buy 100 PBTCUCZ50 @ limit 15|10=014|
> ```
>
> ```text Execution Report, Rejected (FOK not filled) theme={null}
> 8=FIX.4.4|9=309|35=8|49=KRAKEN-PERPS-TRD|56=CLIENT|34=26|52=20261030-22:35:17.103|37=1793399717103088130|11=38007374505886700|17=1003-3989538979|150=8|39=8|103=99|1=12345|55=AAPL-PERP|48=9189124771557588612|54=1|38=1.0|40=2|44=249.01|59=4|151=0.0|14=0.0|6=0.0|60=20261030-22:35:17.103|58=EOrder:Fill or kill order not filled|10=244|
> ```

> [!NOTE]
>
> The rejected order is shown as the gateway reports it now: LeavesQty (151) is `0` and the Execution Report is the only answer. An environment that has not been updated yet sends `151` equal to the order quantity and then a BusinessMessageReject (`35=j`) for the same ClOrdID; treat the two as one rejection.
