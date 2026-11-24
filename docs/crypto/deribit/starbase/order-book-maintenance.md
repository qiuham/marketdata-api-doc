---
exchange: deribit
source_url: https://docs.deribit.com/starbase/order-book-maintenance
api_type: Starbase
updated_at: 2026-11-24 18:59:46.231909
---

# Maintaining the order book

> Maintain order books using the Starbase Binary API including Buy Put, Sell Put, Buy Amount Reduced, Sell Amount Reduced, and Order Delete messages.

Position in the price-time priority queue is explicitly stated and can be tracked using the `sortOrderId`. Snapshots are disseminated starting with the first-to-execute order, in sequence of execution priority. Always sort each price level by `sortOrderId`. Priority should *never* be inferred from message sequence or from `transactTime`. See [Queue priority](#queue-priority).

> [!NOTE]
>
> Every matching engine event that changes the book (including an order that is added and then cancelled within the same instant) generates messages on this feed (e.g. a `Buy Put`/`Sell Put` followed by an `Order Delete`). Starbase publishes market-by-order (L3) data only; there is no separate Level 2 (aggregated price-level) feed.

## Queue priority

Each price level is a FIFO queue ordered by `sortOrderId`. A smaller `sortOrderId` has priority over a larger one, and a taker fills the resting orders at a price level in ascending `sortOrderId` order.

* **Assigned when the order rests.** The `sortOrderId` published in market data is assigned when the order goes on the book, after any applicable pre-trade risk check or speed bump. This applies to all orders that rest on the book, whether or not they pass through a speed bump. A newly resting order always joins the back of its price level, behind every order already resting there
* **Strictly increasing, not consecutive.** `sortOrderId` values increase in the order orders rest on the book, but they are not consecutive. Consecutive resting orders typically differ by `2` (e.g. `101`, `103`). Do not use `sortOrderId` gaps to detect missed messages; use the packet `sequenceNum` (see [Detecting and recovering from gaps](#detecting-and-recovering-from-gaps))
* **Never changes once visible.** Market data publishes resting orders only, so it only carries the `sortOrderId` assigned on rest. An order's `sortOrderId` never changes after it appears in market data
* **`transactTime` is not priority.** On a `Buy Put` or `Sell Put`, `transactTime` in the message header is the time the order went on the book. Do not use it to work out queue position

> [!NOTE]
>
> **Previous behavior.** `sortOrderId` was assigned when the matching engine accepted the order, before the pre-trade risk check. An order still waiting on its risk check could rest after a later order that skipped the check (for example an MMP order), yet take a place ahead of it. A `Buy Put` or `Sell Put` could therefore insert an order in the middle of a price level instead of at the back. With the new behavior, the order in which `Buy Put` and `Sell Put` messages arrive for a price level, `sortOrderId` order and fill order agree.

## Heartbeat messages

A heartbeat message will be sent as an empty packet (0 messages). The heartbeat interval is 5 seconds and will be sent when the interval has elapsed since the last send. The packet will contain the current sequence number. This ensures that the sequence number stream is alive even when there are no market data changes.

## Incremental messages

### Buy Put (20)

This message is sent when a new buy order is placed, an existing buy order is partially executed or an existing buy order is amended. The order specified by a `Buy Put` moves to the back of the price level queue.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | quantity | QuantityMantissa | 8 | It represents the requested order's visible quantity |
| 4 | price | Price9 | 8 | The price of the order or quote |
| 5 | sortOrderId | int64 | 8 | Order priority within a price level. A smaller number has priority over a larger number. Assigned when the order rests on the book; strictly increasing but not consecutive. See [Queue priority](#queue-priority). |

### Sell Put (21)

This message is sent when a new sell order is placed, an existing sell order is partially executed or an existing sell order is amended. The order specified by a `Sell Put` moves to the back of the price level queue.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | quantity | QuantityMantissa | 8 | It represents the requested order's visible quantity |
| 4 | price | Price9 | 8 | The price of the order or quote |
| 5 | sortOrderId | int64 | 8 | Order priority within a price level. A smaller number has priority over a larger number. Assigned when the order rests on the book; strictly increasing but not consecutive. See [Queue priority](#queue-priority). |

### Buy Amount Reduced (22)

This message is sent when the amount of an existing buy order is amended to be smaller. This does not affect the order's position in the price level queue.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | quantity | QuantityMantissa | 8 | New quantity |

### Sell Amount Reduced (23)

This message is sent when the amount of an existing sell order is amended to be smaller. This does not affect the order's position in the price level queue.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | quantity | QuantityMantissa | 8 | New quantity |

### Buy Order Delete (24)

This message is sent when a buy order is fully executed or cancelled.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |

### Sell Order Delete (25)

This message is sent when a sell order is fully executed or cancelled.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |

## Snapshot messages

Each snapshot cycle starts with `IndexInfo (12)` messages, one for each known index price on the channel, batched into as few packets as fit. Each snapshot for an instrument then starts with `SnapshotHeader (100)`, followed by the instrument's `InstrumentDefinition (10)`, `InstrumentInfo (14)`, and the order book as `Buy Put (20)` and `Sell Put (21)` messages, and ends with `SnapshotTrailer (101)`. After all snapshots have been sent, an `EndOfCycle (119)` message is sent.

> [!NOTE]
>
> **Delivered instruments.** Instruments in status `DELIVERED` (`3`) stay in the snapshot cache by default, so they keep appearing in later cycles. Removal is gated by `EVICT_DELIVERED_INSTRUMENTS_FROM_MD_SNAPSHOT`, which is off at deploy and does not change the feed until it is turned on. Eviction also requires `EMIT_MD_INSTRUMENT_STATUS_ONLY` and `EMIT_INDEX_DEFINITION`. While those flags are on, an instrument is dropped from the snapshot cache once it reaches `DELIVERED` and is omitted from later cycles. A client already on the incremental feed still sees the transition as [`InstrumentStatusUpdate` (16)](https://docs.deribit.com/starbase/reference-data#instrumentstatusupdate-16). The market-data schema stays version `1` (`semanticVersion` `1.0`).

### SnapshotHeader (100)

| Field | Name | Type | Length | Description |
| :- | :- | :- | :- | :- |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | incrementalTimestamp | int64 | 8 | Nanoseconds since epoch. Timestamp of last incremental update included in this snapshot. |
| 3 | incrementalSeqNum | int64 | 8 | Sequence number of last incremental update included in this snapshot |

### SnapshotTrailer (101)

| Field | Name | Type | Length | Description |
| :- | :- | :- | :- | :- |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | incrementalTimestamp | int64 | 8 | Nanoseconds since epoch. Timestamp of last incremental update included in this snapshot. |
| 3 | incrementalSeqNum | int64 | 8 | Sequence number of last incremental update included in this snapshot |

### EndOfCycle (119)

| Field | Name | Type | Length | Description |
| :- | :- | :- | :- | :- |
| 1 | activeInstrumentCount | int32 | 4 | Total number of active instruments |

## Synchronizing snapshots with the incremental feed

Each product type has a snapshot channel and an incremental channel (see [Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md)). To build a book and keep it current, combine the two feeds per instrument:

1. Join the incremental channel first and buffer every packet you receive, along with its `sequenceNum`.
2. Join the snapshot channel and read snapshots until you have one for each instrument you need.
3. For each instrument, read `incrementalSeqNum` from its `SnapshotHeader (100)` or `SnapshotTrailer (101)`. This is the sequence number of the last incremental update already included in that snapshot.
4. Apply buffered incremental messages for that instrument only if their sequence number is greater than its `incrementalSeqNum`. Discard messages at or below it.
5. Once every instrument you track is synchronized, you can leave the snapshot channel and process the incremental channel directly.

> [!NOTE]
>
> `incrementalSeqNum` is scoped to a single instrument's snapshot. There is no cycle-wide sequence number. Instruments in the same snapshot cycle can carry different `incrementalSeqNum` values, so track the synchronization point per instrument.

### Detecting and recovering from gaps

Only the first message in a packet carries a sequence number in the packet header. The next expected sequence number is the packet's `sequenceNum` plus its `messageCount`. Heartbeat packets have a `messageCount` of `0` and carry the next expected sequence number. See [UDP messages](https://docs.deribit.com/starbase/binary-api-reference.md#udp-messages).

If a packet arrives with a higher `sequenceNum` than expected, you have missed messages:

1. Request the missing range from the [Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md) and apply the recovered messages in sequence order.
2. If the gateway returns `SEQ_TOO_LOW`, the messages are no longer available. The missing messages could affect any instrument on the channel. Rebuild each affected book from a later snapshot whose `incrementalSeqNum` is at or past the last missing sequence number, then resume applying incremental messages after that point.


## Related topics

- [public/get_order_book](https://docs.deribit.com/api-reference/market-data/public-get_order_book.md)
- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)
- [public/get_order_book_by_instrument_id](https://docs.deribit.com/api-reference/market-data/public-get_order_book_by_instrument_id.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)