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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy'
updated_at: 2026-11-21
---

# Drop Copy

> FIX 4.4 drop copy for Kraken US Perps — session layer and Execution Report reference

The **Kraken US Perps drop copy** is a FIX 4.4 session that delivers a copy of every Execution Report on your account: acknowledgements, fills, amendments, cancellations, expiries, restatements and engine rejects. Business messages flow one way, from Kraken to the client.

On the drop copy, the Execution Report carries the fields of the one sent on the [Unified FIX v2](https://docs.kraken.com/exchange/api-reference/unified-fix-v2.md) order-entry session, in the same order and with the same values, apart from the differences listed on the [Execution Report](https://docs.kraken.com/exchange/api-reference/drop-copy/er.md) page. `ExecID (17)` is the one order entry sends on the same report, so a client reading both feeds can match the two reports. Order status answers (`ExecType (150)=I`) are not sent.

For an overview of the US Perps APIs and how to connect, see the [US Perps guides](https://docs.kraken.com/exchange/guides/us-perps/overview.md).

## Protocol

| | |
| :- | :- |
| **Protocol** | FIX 4.4 (`BeginString` = `FIX.4.4`) |
| **Scope** | Session layer, standard header and trailer, and the Execution Report |

## Messages

### Session layer (either direction)

| Message | MsgType | Description |
| :- | :- | :- |
| [Logon](https://docs.kraken.com/exchange/api-reference/drop-copy/logon.md) | `35=A` | Opens the session and agrees the heartbeat interval, sequence-number reset and credentials. Must be the first message after the connection is established. |
| [Logout](https://docs.kraken.com/exchange/api-reference/drop-copy/logout.md) | `35=5` | Initiates or confirms the end of the session, and carries the reason for a failed logon. |
| [Heartbeat](https://docs.kraken.com/exchange/api-reference/drop-copy/heartbeat.md) | `35=0` | Keeps the session alive during inactivity, and answers a Test Request. |
| [TestRequest](https://docs.kraken.com/exchange/api-reference/drop-copy/test-request.md) | `35=1` | Probes whether the counterparty is still alive; must be answered with a Heartbeat. |
| [ResendRequest](https://docs.kraken.com/exchange/api-reference/drop-copy/resend-request.md) | `35=2` | Asks the counterparty to retransmit a range of messages after a sequence gap. |
| [SequenceReset](https://docs.kraken.com/exchange/api-reference/drop-copy/sequence-reset.md) | `35=4` | Resets the counterparty's expected sequence number, or stands in for messages that will not be resent. |
| [Reject](https://docs.kraken.com/exchange/api-reference/drop-copy/reject.md) | `35=3` | Session-level rejection of a message that is malformed or fails field validation. |

### Execution (Kraken → client)

| Message | MsgType | Description |
| :- | :- | :- |
| [ExecutionReport](https://docs.kraken.com/exchange/api-reference/drop-copy/er.md) | `35=8` | The drop copy payload. Reports every change to an order: acknowledgement, fill, amendment, cancellation, expiry, restatement or engine reject. |

Every message starts with the [standard header and ends with the standard trailer](https://docs.kraken.com/exchange/api-reference/drop-copy/header-trailer.md).

## Recovery

On reconnect, the session resumes from the last report Kraken sent, not from the last report you received. A report Kraken sent that you did not receive is not sent again on its own: ask for it with a ResendRequest. If you ask for every gap with a ResendRequest, delivery is at least once: Execution Reports can be delivered again after a reconnect. Some of them carry `PossResend (97)=Y`, but not every report that is delivered again is tagged.

**What the client should do:**

* De-duplicate Execution Reports by `ExecID (17)`: a report delivered again has the same ExecID as the first. A report with `PossResend (97)=Y` may be one you have already processed, and so may one without it.
* Send a [ResendRequest](https://docs.kraken.com/exchange/api-reference/drop-copy/resend-request.md) (`35=2`) when you detect a gap in `MsgSeqNum (34)`.
* Do not log on with `ResetSeqNumFlag (141)=Y` outside the daily reset (22:00 UTC). Kraken then discards the reports a ResendRequest would replay, so reports sent but not yet received are lost.

## Related

> [card] [US Perps API overview](https://docs.kraken.com/exchange/guides/us-perps/api.md)
>
> How order entry, market data and drop copy fit together.

> [card] [Unified FIX v2](https://docs.kraken.com/exchange/api-reference/unified-fix-v2.md)
>
> FIX 4.4 order entry for US Perps.

> [card] [SBE market data](https://docs.kraken.com/exchange/api-reference/sbe.md)
>
> Binary market data: instruments, L3 book, trades and status.

> [card] [US Perps connectivity](https://docs.kraken.com/exchange/guides/us-perps/connectivity.md)
>
> Connectivity and colocation documents.
