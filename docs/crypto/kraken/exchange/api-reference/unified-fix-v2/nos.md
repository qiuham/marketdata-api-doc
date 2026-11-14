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
updated_at: 2026-11-13
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

Order quantity in contracts.

**40 - OrdType** `char` *required*

Execution model of the order.

**Possible values:**

* `1` : Market - fill the whole quantity immediately at the best available prices.
* `2` : Limit - rest in the book, trading only at the limit price or better.

**44 - Price** `Price`

Limit price of the order, denominated in the quote currency. Required for limit orders.

**Format:** Limit price, denominated in the quote currency.

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

Not supported on US Perps. An order that carries it is rejected with a BusinessMessageReject (`35=j`): "Order type iceberg is not supported on this venue".

> [!NOTE]
>
> **GTD and DisplayQty: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | GTD (`59=6` with `ExpireTime`) | Accepted | Supported | Supported |
> | DisplayQty (1138) | Rejected (iceberg orders are not supported) | Supported | Not read as a size, but its presence turns the order into an iceberg order with no display size. The back-end outcome is to be confirmed, so do not send it |

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
> | EffectiveTime (168) | Rejected (`35=j`) | Supported | Forwarded by the gateway; whether the back end honours it is to be confirmed |
> | Margin (5001) | `1` rejected (`35=j`); `0` accepted, no effect | Supported | Forwarded by the gateway; whether the back end honours it is to be confirmed |

**7928 - SelfTradePrevention** `char`

Self-trade prevention mode, deciding which order is expired when your own orders would match. Defaults to cancelling the newest.

**Possible values:**

* `0` : Cancel both - the arriving and the resting order are both cancelled.
* `1` : Cancel newest - the arriving order is cancelled. Default.
* `2` : Cancel oldest - the resting order is cancelled.

**trailer** *required*
