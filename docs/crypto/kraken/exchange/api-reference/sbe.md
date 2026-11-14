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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe'
updated_at: 2026-11-13
---

# SBE

> Simple Binary Encoding (SBE) market data for Kraken US Perps — session negotiation and public market data wire contract

Kraken US Perps publishes public market data over **Simple Binary Encoding (SBE)**: a compact, fixed-layout binary format designed for low-latency decoding. The protocol is defined by two schemas — a **session** schema for TLS session negotiation, authentication, subscriptions and keepalive, and a **market data** schema for instrument definitions, order books, trades, instrument summaries and trading status.

For an overview of the US Perps APIs and how to connect, see the [US Perps guides](https://docs.kraken.com/exchange/guides/us-perps/overview.md).

## Schemas

| Schema | Package | Schema ID | Wire version | Semantic version | Byte order | Role |
| :- | :- | :- | :- | :- | :- | :- |
| Session | `Kraken.MarketDataAPIProto` | 33 | 5 | 6.0.0 | littleEndian | TLS session negotiation, authentication, subscriptions and keepalive |
| Market data | `Kraken.MarketDataProto` | 36 | 15 | 13.0.0 | littleEndian | Instrument definitions, books, trades, summaries and trading status |

Every SBE message starts with the standard SBE `messageHeader` (`blockLength:uint16`, `templateId:uint16`, `schemaId:uint16`, `version:uint16`). Use `schemaId` and `templateId` to select the decoder. On the wire, each SBE message is carried inside a TCP frame that adds a framing header in front of the SBE `messageHeader` — see [Framing](#framing).

> [!NOTE]
>
> **Compatibility rule:** new optional or versioned fields require a schema version increase. Existing field and template IDs are never reused or reordered.

> [!NOTE]
>
> **Breaking change from market data schema 34.** Schema 36 removes static reference data from the instrument definition messages, changes the layout of both definition messages and replaces the template 11 and 12 layouts. Schema 34 codecs cannot decode schema 36. Regenerate your codecs from schema 36 together with session schema 33 version 5.

## Connections

The session uses two connections. Each `compId` allows one active live connection and one active snapshot connection.

* **Snapshot connection** — send a `SubscriptionRequest` with `subscriptionRequestType` = `Snapshot` to receive one snapshot (instrument definitions, order book, instrument summaries or, on Spot and Futures only, trading session status).
* **Live connection** — send `Subscribe` or `Unsubscribe` to start or stop incremental delivery for a feed.

Feeds are selected with [`MarketDataFeed`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#marketdatafeed): `InstrumentDefinition`, `OrderBookL3`, `Trade`, `InstrumentStatus`, `Summary` and `TradingSessionStatus`.

> [!NOTE]
>
> **`TradingSessionStatus` applies to Spot and Futures, not to US Perps.** US Perps does not expose a global trading session status. It provides the status per instrument: use the `InstrumentStatus` feed, and the status carried by each `InstrumentDefinition`.

## Framing

Each TCP frame carries exactly one SBE message, in both directions. TLS protects the TCP stream but does not change the frame bytes.

```text theme={null}
bytes 0..5       SOFH
bytes 6..13      Kraken TCP header
bytes 14..21     SBE message header
bytes 22..end    SBE message body
```

| Offset | Size | Field | Type | Byte order | Description |
| :- | :- | :- | :- | :- | :- |
| 0 | 4 | `messageLength` | `uint32` | big endian | Total frame size in bytes, including the SOFH and the Kraken TCP header |
| 4 | 2 | `encodingType` | `uint16` | big endian | `0xEB50`: Kraken TCP header followed by an SBE 1.0 message in little endian byte order |
| 6 | 8 | `SendingTime` | `int64` | little endian | Unix epoch nanoseconds (Kraken TCP header) |
| 14 | 8 | SBE `messageHeader` | composite | little endian | `blockLength`, `templateId`, `schemaId`, `version` |
| 22 | variable | SBE message body | | little endian | Root block, repeating groups and variable-length data |

The first six bytes are the Simple Open Framing Header (SOFH). The eight-byte Kraken TCP header is a Kraken extension to the usual SOFH and SBE layout: a generic SOFH reader must skip those eight bytes before decoding the SBE `messageHeader`.

* **`SendingTime`** is diagnostic only. The gateway stamps a shared market data frame once, when it enters the shared fanout, so every client sees the same time for that frame. It is not a kernel transmit timestamp, and it must not be used for authentication or replay checks.
* **Reading frames.** TCP may split one frame across several reads or return several frames in one read. Read the full SOFH, check its fields, then wait until `messageLength` bytes have arrived.
* **Protocol errors.** An unsupported `encodingType`, a `messageLength` below 22 (the minimum frame size), or a `messageLength` above the service limit is a protocol error. Kraken closes the connection instead of skipping the frame.
* **Repeating groups.** Before reading a group, verify that its block length and entry count fit inside the enclosing frame. Check the size arithmetic for overflow.

### Frame counting

Frame counting is implicit: there is no sequence number on the wire for session control.

* Each direction has its own counter. Both start at 1 on a new connection, never wrap, and have no daily reset.
* A sender advances its counter after it successfully sends a complete frame. A receiver advances its counter after it validates the complete SOFH and SBE frame.
* Every frame counts, including negotiation, subscription, heartbeat, termination and market data messages. Zero means no frame has been received.
* `AdminHeartbeat.lastReceivedClientSequence` reports the latest client frame Kraken accepted, and `SubscriberHeartbeat.lastReceivedServerSequence` reports the latest server frame the client processed.
* An acknowledgement greater than the number of frames its peer has sent is a protocol violation. A lower value is allowed while frames are in flight or waiting to be processed; persistent lag is handled by the service's slow consumer limits.
* Heartbeat acknowledgements never request a replay. After a broken connection, start a new session and request a fresh snapshot.

## Session schema (ID 33)

| Template | Message | Description |
| :- | :- | :- |
| 1 | [Negotiate](https://docs.kraken.com/exchange/api-reference/sbe/negotiate.md) | Opens and authenticates a session. |
| 2 | [NegotiationResponse](https://docs.kraken.com/exchange/api-reference/sbe/negotiation-response.md) | Confirms a successful negotiation. |
| 3 | [NegotiationReject](https://docs.kraken.com/exchange/api-reference/sbe/negotiation-reject.md) | Rejects a negotiation. |
| 4 | [AdminHeartbeat](https://docs.kraken.com/exchange/api-reference/sbe/admin-heartbeat.md) | Keepalive from Kraken. |
| 5 | [SubscriberHeartbeat](https://docs.kraken.com/exchange/api-reference/sbe/subscriber-heartbeat.md) | Keepalive from the client. |
| 6 | [Terminate](https://docs.kraken.com/exchange/api-reference/sbe/terminate.md) | Ends the session. |
| 7 | [SubscriptionRequest](https://docs.kraken.com/exchange/api-reference/sbe/subscription-request.md) | Requests a snapshot, or starts or stops incremental delivery. |
| 8 | [SubscriptionResponse](https://docs.kraken.com/exchange/api-reference/sbe/subscription-response.md) | Answers a SubscriptionRequest. |

Enumerations and encodings: [Session enums & encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md).

## Market data schema (ID 36)

| Template | Message | Description |
| :- | :- | :- |
| 1 | [InstrumentDefinitionSnapshot](https://docs.kraken.com/exchange/api-reference/sbe/instrument-definition-snapshot.md) | Instrument definitions, one per message, within a snapshot cycle. |
| 2 | [OrderBookIncremental](https://docs.kraken.com/exchange/api-reference/sbe/order-book-incremental.md) | Order-by-order (L3) book updates. |
| 3 | [TradeIncremental](https://docs.kraken.com/exchange/api-reference/sbe/trade-incremental.md) | Trades. |
| 4 | [OrderBookSnapshot](https://docs.kraken.com/exchange/api-reference/sbe/order-book-snapshot.md) | Full L3 book snapshot, in chunks. |
| 5 | [InstrumentStatusIncremental](https://docs.kraken.com/exchange/api-reference/sbe/instrument-status-incremental.md) | Live instrument trading-status changes. |
| 6 | [TradingSessionStatusIncremental](https://docs.kraken.com/exchange/api-reference/sbe/trading-session-status-incremental.md) | Trading session status changes. Spot and Futures only; not used on US Perps. |
| 7 | [InstrumentDefinitionIncremental](https://docs.kraken.com/exchange/api-reference/sbe/instrument-definition-incremental.md) | Instrument additions, modifications and deletions. |
| 10 | [TradingSessionStatusSnapshot](https://docs.kraken.com/exchange/api-reference/sbe/trading-session-status-snapshot.md) | Current trading session status. Spot and Futures only; not used on US Perps. |
| 11 | [SummarySnapshot](https://docs.kraken.com/exchange/api-reference/sbe/summary-snapshot.md) | Current summary (reference price) of one instrument, one message per instrument. |
| 12 | [SummaryIncremental](https://docs.kraken.com/exchange/api-reference/sbe/summary-incremental.md) | Updated summary (reference price) of one instrument. |

Enumerations and encodings: [Market data enums & encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md).

## Instrument definitions

The instrument definition messages carry an instrument's trading parameters (scales, tick size, quantity increment, maximum trade volume, price controls and status) and its `symbol`. They do not carry `contractMultiplier`, `currency`, `underlyingSymbol`, `description`, `productType`, `marketSector` or `maturityType`.

`symbol` is at most 128 UTF-8 bytes, not 128 characters, so you can resolve an `instrumentId` to a symbol from SBE alone. For an `instrumentId` you do not know, recover the definition from an `InstrumentDefinitionSnapshot`. Do not infer a mapping.

### Price controls

`minPrice`, `maxPrice` and `variation` are optional absolute prices in the instrument currency, each with its own exponent ([`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice)). They are not percentages and are not scaled by `priceScale`. Exponent `127` means unavailable, and the mantissa must then be ignored. Zero is a valid value, including a variation of zero.

`minPrice` and `maxPrice` are inclusive static bounds. `variation` is a non-negative offset around the reference the matching engine selects for an aggressive limit order. Market-order protection is separate and is not represented by `variation`. A change to these values is published as a full-replacement `InstrumentDefinitionIncremental`.

## Instrument summaries

The `Summary` feed carries one summary per instrument. Each `SummarySnapshot` and `SummaryIncremental` is the complete current summary for that instrument. Currently it holds `referencePrice`, the external reference price accepted by the matching engine, and `referencePriceTime`, the producer timestamp of that value or of its clear. Mark price, volume and turnover are not defined.

Every update replaces the whole summary. A null `referencePrice` (exponent `127`) clears the value, it does not mean unchanged, and zero is a real price. A `referencePriceTime` of zero means the source timestamp is unavailable.

`summarySeq` is contiguous per instrument, starts at one, is shared by all summary metrics and continues across reconnects and restarts. To join the feed:

1. Subscribe to `Summary` on the live connection and buffer the updates.
2. Request the `Summary` snapshot on the snapshot connection.
3. Discard buffered updates with `summarySeq` at or below the snapshot's `lastSummarySeqProcessed`, then apply later updates in contiguous order.

A `lastSummarySeqProcessed` of zero means no summary update has been published: the reference price is null and its time is zero. A gap requires a new summary snapshot. A snapshot response has one message per instrument, numbered 1 through `totalSummaries` with `summaryNumber`, and is complete when every number has arrived. An instrument without a price is still a row, with a null `referencePrice`.

## Sequencing

Incremental feeds carry contiguous per-instrument (or per-feed) sequence numbers starting at one — `orderBookSeq`, `tradeSeq`, `instrumentStatusSeq`, `instrumentDefinitionSeq`, `summarySeq` and `tradingSessionSeq`. Snapshots carry the last sequence number they include (for example `lastOrderBookSeqProcessed`), so you can apply buffered incrementals with a higher sequence number on top of the snapshot.

### Gap recovery

There is no message replay. When you detect a gap, request a new snapshot on the snapshot connection and rebuild from it:

| Feed | Gap recovered by |
| :- | :- |
| `OrderBookL3` | `OrderBookSnapshot` |
| `InstrumentDefinition` | `InstrumentDefinitionSnapshot` |
| `InstrumentStatus` | `InstrumentDefinitionSnapshot`, which carries each instrument's current status and its `lastInstrumentStatusSeqProcessed` |
| `Summary` | `SummarySnapshot`, which carries `lastSummarySeqProcessed` |
| `TradingSessionStatus` (Spot and Futures only) | `TradingSessionStatusSnapshot` |
| `Trade` | Not recoverable |

> [!NOTE]
>
> There is no trade snapshot. A gap in `tradeSeq` can be detected, but trades missed during the gap, or while you were disconnected, cannot be recovered from a book snapshot or any other feed.

## Related

> [card] [US Perps API overview](https://docs.kraken.com/exchange/guides/us-perps/api.md)
>
> How order entry, market data and drop copy fit together.

> [card] [Unified FIX v2](https://docs.kraken.com/exchange/api-reference/unified-fix-v2.md)
>
> FIX 4.4 order entry for US Perps.

> [card] [Drop Copy](https://docs.kraken.com/exchange/api-reference/drop-copy.md)
>
> FIX 4.4 copy of every execution report on your account.

> [card] [US Perps connectivity](https://docs.kraken.com/exchange/guides/us-perps/connectivity.md)
>
> Connectivity and colocation documents.
