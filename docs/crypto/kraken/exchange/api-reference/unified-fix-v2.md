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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2'
updated_at: 2026-11-13
---

# Unified FIX v2

> FIX 4.4 order entry for Kraken US Perps — message types, tags and session behaviour

Unified FIX v2 is the FIX 4.4 order-entry interface for **Kraken US Perps**. It covers the session layer, order entry (new, cancel, amend, mass cancel and status requests) and the execution and reject messages Kraken sends back.

For an overview of the US Perps APIs and how to connect, see the [US Perps guides](https://docs.kraken.com/exchange/guides/us-perps/overview.md).

## Protocol

| | |
| :- | :- |
| **Protocol** | FIX 4.4 (`BeginString` = `FIX.4.4`) |
| **Messages** | 15, plus the standard header (9 fields) and trailer (1 field) |
| **Transport** | TLS required on all connections |
| **Authentication** | API key, HMAC-SHA512 password signature and nonce on [Logon](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/logon.md) |
| **Session rollover** | Daily at 22:00 UTC; sequence numbers reset |
| **Cancel-on-disconnect** | On by default; done by the FIX gateway; controlled by `CancelOrdersOnDisconnect (8674)` |

## Messages

### Session layer

| Message | MsgType | Direction | Description |
| :- | :- | :- | :- |
| [Logon](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/logon.md) | `35=A` | Client → Kraken, then Kraken → client | Authenticates the session and sets its parameters. Must be the first message after the TCP connection is established. |
| [Logout](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/logout.md) | `35=5` | Either direction | Initiates or confirms the end of the session, and carries the reason for a failed logon. |
| [Heartbeat](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/heartbeat.md) | `35=0` | Either direction | Keeps the session alive during inactivity, and answers a Test Request. |
| [TestRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/test-request.md) | `35=1` | Either direction | Probes whether the counterparty is still alive; must be answered with a Heartbeat. |
| [ResendRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/resend-request.md) | `35=2` | Either direction | Asks the counterparty to retransmit a range of messages after a sequence gap. |
| [SequenceReset](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/sequence-reset.md) | `35=4` | Either direction | Resets the counterparty's expected sequence number, or stands in for messages that will not be resent. |

### Order entry (Client → Kraken)

| Message | MsgType | Description |
| :- | :- | :- |
| [NewOrderSingle](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/nos.md) | `35=D` | Submits a new limit or market order. |
| [OrderCancelRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/ocr.md) | `35=F` | Cancels a single working order. |
| [OrderCancelReplaceRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/ocrr.md) | `35=G` | Amends the price, quantity or expiry of a working order. |
| [OrderMassCancelRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/omcr.md) | `35=q` | Cancels open orders in bulk. On US Perps every request carries `AllAccounts (5034)`, which can narrow the cancel to one account. |
| [OrderStatusRequest](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/osr.md) | `35=H` | Asks for the current state of a single order. |

### Execution and rejects (Kraken → client)

| Message | MsgType | Description |
| :- | :- | :- |
| [ExecutionReport](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/er.md) | `35=8` | Reports every change to an order: acknowledgement, fill, amendment, cancellation, expiry, restatement, or an answer to a status request. |
| [OrderCancelReject](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/ocj.md) | `35=9` | Rejects a single-order cancel. On US Perps cancel business rejects arrive as `35=9` where it is enabled (UAT today; production to be confirmed) and as `35=j` otherwise, so handle both. Amend rejects arrive as `35=j` or `35=3`, never `35=9`. |
| [Reject](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/reject-session.md) | `35=3` | Session-level rejection of a message that is malformed or fails field validation. |
| [BusinessMessageReject](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/reject-business.md) | `35=j` | Business-level rejection of a message that fails a business rule before it reaches the trading engine. |

Every message starts with the [standard header and ends with the standard trailer](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/header-trailer.md).

## Cancel scope

A single-order cancel (`OrderCancelRequest`) looks the order up among the orders cached for this SenderCompID, earlier connections included, not only the orders of the current session. `Side` and `Symbol` (or `InstrumentID`) must match the order.

On US Perps every `OrderMassCancelRequest` (`35=q`) must carry `AllAccounts (5034)`. With `Y`, `MassCancelRequestType (530)` = `1` and `7` are engine sweeps per instrument and Account: they cancel every order of that Account on each instrument where this SenderCompID has a cached open order, whoever placed it, and type `6` cancels this connection's orders one by one. With `N` and `Account (1)`, the cancel is narrowed to that one account for types `1`, `6` and `7`. A request without `5034` is refused with `35=3`. If nothing is cached for the scope, Kraken sends no request and no reply. See [Order Mass Cancel Request](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/omcr.md).

## How US Perps differs from Spot and Futures

Some behaviours differ by venue. The table summarises where US Perps differs from Spot and Futures; the message pages give the details. Spot and Futures are shown for comparison only. Items marked "to be confirmed" have not been verified end to end.

| Area | US Perps | Spot | Futures |
| :- | :- | :- | :- |
| ClOrdID | Positive integer, up to 19 digits | UUIDs (36 characters) accepted | Timestamp-first COMB UUIDv4 required |
| Cancel business reject | `35=9` where enabled (UAT; production to be confirmed), otherwise `35=j` | `35=j` | `35=j` |
| Amend reject | `35=j` or `35=3`, never `35=9` | `35=j` | `35=j`; amend is off in production, on in UAT |
| Matching-engine reject | Execution Report `150=8` / `39=8` with OrdRejReason | Not sent; `35=j` | Not sent; `35=j` |
| Single-order cancel | Any order cached for the SenderCompID; Side and Symbol or InstrumentID must match | Same cache scope; no Side or Symbol rule | Same as Spot |
| Mass cancel account | `AllAccounts (5034)` required; `N` with `Account (1)` narrows to one account | Neither tag accepted (`35=3`, reason 2) | Same as Spot |
| Mass cancel type `7` | Engine sweep per instrument and Account | Batch of the cached order ids; REST and WebSocket orders not reached | Same as Spot |
| Order status request | Live cached orders only; others `35=j`, `380=101` | Orders outside the cache are found; `380=101` for unknown orders | Off in production and UAT |
| ExecInst on amend | Only `P`; leaving it out clears post-only | Only `P`; effect of leaving it out differs by route | Same rule in UAT; amend off in production |
| GTD | Accepted (`59=6` with `ExpireTime`) | Supported | Supported |
| DisplayQty | Rejected | Supported | Not read as a size; outcome to be confirmed |
| EffectiveTime, Margin | Rejected; `Margin=0` accepted with no effect | Supported | Forwarded; to be confirmed |
| ValidUntilTime | Range-checked only; rejected on amend | Forwarded as a deadline; minimum varies | Forwarded as a deadline; minimum varies |
| Logon nonce | 60 s in UAT; production to be confirmed | Freshness not checked | Freshness not checked |
| Cancel-on-disconnect | FIX gateway only | Gateway, plus a back-end backstop timer by default | Gateway only (one production deployment also arms the back-end timer) |
| ExecID | Opaque | Base32 of a ClOrdID-derived value plus a timestamp | Same as Spot |
| LastLiquidityInd | Tag 851, values `1` and `2` | Tag 5050 | Same as Spot |
| InstrumentID (48) | Accepted on orders; sent on reports when cached | Never sent; ignored outside US Perps | Same as Spot |

## Related

> [card] [US Perps API overview](https://docs.kraken.com/exchange/guides/us-perps/api.md)
>
> How order entry, market data and drop copy fit together.

> [card] [Drop Copy](https://docs.kraken.com/exchange/api-reference/drop-copy.md)
>
> FIX 4.4 copy of every execution report on your account.

> [card] [SBE market data](https://docs.kraken.com/exchange/api-reference/sbe.md)
>
> Binary market data: instruments, L3 book, trades and status.

> [card] [US Perps connectivity](https://docs.kraken.com/exchange/guides/us-perps/connectivity.md)
>
> Connectivity and colocation documents.
