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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/omcr'
updated_at: 2026-11-13
---

# Order Mass Cancel Request

> Cancel open orders in bulk

FIX
session: trading
35=q

Cancels open orders in bulk, including orders resting in the book. MassCancelRequestType sets the scope. On US Perps every request must also carry `AllAccounts (5034)`, which says whether the cancel reaches every account or only one. With `AllAccounts=Y`, types `1` and `7` are engine sweeps per instrument and Account, not per session: they cancel every order of that Account on each instrument where this SenderCompID has a cached open order, earlier connections included, whoever placed the order. With `AllAccounts=N` and `Account (1)`, the cancel is narrowed to that one end-client account, for types `1`, `6` and `7` alike. If nothing is cached for the scope, Kraken sends no request to the engine and sends no reply. Each cancellation is confirmed by its own Execution Report; there is no mass cancel report.

> [!WARNING]
>
> **`AllAccounts (5034)` is required on every US Perps mass cancel.** An OrderMassCancelRequest without it is refused with a Reject (`35=3`) before anything reaches the engine. Send `AllAccounts=Y` and no `Account` to keep the previous behaviour.

> [!NOTE]
>
> **Mass cancel: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | `AllAccounts (5034)` and `Account (1)` | `5034` required on every request; `N` with `Account` narrows the cancel to one account | Neither tag is accepted: either one is rejected with `35=3`, `SessionRejectReason (373)` `2` | Same as Spot |
> | Type `1` (one symbol) | Engine sweep on that instrument and Account; also accepts InstrumentID (48) | As documented: orders created or replaced on this session | Same as Spot |
> | Type `6` (this session) | Cancels this connection's orders one by one | As documented | Same as Spot |
> | Type `7` | Engine sweep per instrument and Account for every instrument with a cached open order; misses instruments with nothing cached | Sends a batch of the order ids cached for this SenderCompID, earlier connections included. There is no cancel-all call, so REST and WebSocket orders are not reached | Same as Spot |

**Direction:** Client → Kraken

***

**header** *required*

35=`q`

**11 - ClOrdID** `string` *required*

Client-assigned identifier of the mass cancel request. On US Perps it must be a positive integer of at most 19 digits: use an ever-increasing number, for example a microsecond timestamp. See [New Order Single](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/nos.md) for how invalid values are rejected.

**Format:** Positive integer, up to 19 digits, e.g. a microsecond timestamp.

**530 - MassCancelRequestType** `char` *required*

Scope of the mass cancel.

**Possible values:**

* `1` : Cancel by instrument. Requires Symbol (55) or InstrumentID (48). Engine sweep: for each Account that has a cached open order of this SenderCompID on that instrument, every order of that Account on the instrument is cancelled, whoever placed it. With `AllAccounts=N`, the sweep goes out for the named Account only. `Account (1)` is mandatory unless `AllAccounts=Y`, in which case it must not be sent. Nothing cached for the instrument means no request and no reply.
* `6` : Cancel the orders created on this connection, one by one. With `AllAccounts=N`, only the named Account's orders are cancelled. `Account (1)` is mandatory unless `AllAccounts=Y`, in which case it must not be sent.
* `7` : Cancel by SenderCompID. Engine sweep for every instrument where this SenderCompID has a cached open order, earlier connections included: for each such instrument and Account, every order of that Account is cancelled, whoever placed it. With `AllAccounts=N`, the sweep goes out for the named Account only. `Account (1)` is mandatory unless `AllAccounts=Y`, in which case it must not be sent. An instrument with nothing cached is not reached; nothing cached at all, or nothing cached for the named Account, means no request and no reply.

**5034 - AllAccounts** `boolean` *required*

Kraken tag. Whether the mass cancel reaches every account or only one. Required on every US Perps OrderMassCancelRequest, whatever MassCancelRequestType (530) is.

**Possible values:**

* `Y` : Every account among the cached orders, as before. Account (1) must not be sent.
* `N` : Only the account named in Account (1), which is then required.

A value other than `Y` is read as `N`, so a malformed value narrows the cancel rather than widening it.

**How invalid combinations are rejected.** Each is refused with a Reject (`35=3`) that names the tag, before anything reaches the engine, so nothing is cancelled:

* `5034` missing: `SessionRejectReason (373)` `1`, `RefTagID (371)` `5034`.
* `AllAccounts=N` without `Account (1)`: `373` = `1`, `371` = `1`.
* `AllAccounts=Y` with `Account (1)`: `373` = `5`, `371` = `1`.
* An `Account (1)` that is not numeric, is `0`, or is `18446744073709551615`: `373` = `5`, `371` = `1`.

**1 - Account** `string`

Numeric end-client id the cancel is narrowed to. Required with `AllAccounts=N` and not allowed with `AllAccounts=Y`. Accounts compare as numbers, so `01934980` is `1934980`. A cached order with no readable account is never reached by a narrowed request.

**Format:** Non-zero numeric end-client id.

Required: Conditional

**336 - TradingSessionID** `string`

Trading session the status applies to.

**55 - Symbol** `string`

Perpetual futures contract, in the venue symbol form. Ten contracts are listed at launch. Required for type `1` unless InstrumentID is sent. Ignored when InstrumentID is also sent: the instrument is then recognised from InstrumentID.

**Format:** Venue symbol.

Required: Conditional

**48 - InstrumentID** `string`

Identifier of the instrument within the identification scheme named by InstrumentIDSource.\
Where both Symbol and InstrumentID are sent, InstrumentID is what the instrument is recognised from and Symbol is ignored.

**Format:** Venue instrument identifier. Takes precedence over Symbol when both are sent.

**22 - InstrumentIDSource** `string`

Identification scheme that InstrumentID is expressed in.

**Possible values:**

* `8` : Exchange symbol.

**60 - TransactTime** `UTCTimestamp` *required*

Time of the business event in UTC, formatted YYYYMMDD-HH:MM:SS.uuu.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**trailer** *required*
