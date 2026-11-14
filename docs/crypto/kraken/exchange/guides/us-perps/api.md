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
source_url: 'https://docs.kraken.com/exchange/guides/us-perps/api'
updated_at: 2026-11-13
---

# US Perps APIs

> The three US Perps APIs — FIX for order entry, SBE for market data and FIX for drop copy

Kraken US Perps is accessed through three APIs. Each has its own session and its own reference in the [API Reference](https://docs.kraken.com/exchange/api-reference/overview.md).

| API | Protocol | Purpose | Reference |
| :- | :- | :- | :- |
| **Order entry** | FIX 4.4 | Place, amend and cancel orders; receive execution reports | [Unified FIX v2](https://docs.kraken.com/exchange/api-reference/unified-fix-v2.md) |
| **Market data** | SBE (Simple Binary Encoding) | Instrument definitions, order-by-order (L3) books, trades, instrument summaries and trading status | [SBE](https://docs.kraken.com/exchange/api-reference/sbe.md) |
| **Drop copy** | FIX 4.4 | A copy of every execution report on your account | [Drop Copy](https://docs.kraken.com/exchange/api-reference/drop-copy.md) |

## Order entry — FIX

Order entry uses FIX 4.4. A trading session authenticates on Logon with your FIX API key, an HMAC-SHA512 password signature and a nonce, then sends `NewOrderSingle`, `OrderCancelRequest`, `OrderCancelReplaceRequest`, `OrderMassCancelRequest` and `OrderStatusRequest`. Kraken answers with `ExecutionReport`, and with `OrderCancelReject`, `Reject` or `BusinessMessageReject` when a request cannot be processed.

* Market and limit orders, with GTC, IOC and FOK time in force
* A mass cancel carries `AllAccounts (5034)`: `Y` reaches every account, `N` with `Account (1)` cancels one account's orders only
* Cancel-on-disconnect is on by default
* Sequence numbers reset at the daily 22:00 UTC session rollover

See the [Unified FIX v2 reference](https://docs.kraken.com/exchange/api-reference/unified-fix-v2.md).

## Market data — SBE

Public market data is published in Simple Binary Encoding, a fixed-layout binary format designed for low-latency decoding. A session schema handles negotiation, authentication, subscriptions and keepalive; a market data schema carries the data itself.

* Subscribe to incremental updates on the live connection and buffer them first, then request a snapshot on the snapshot connection and apply the buffered updates that follow it. Requesting the snapshot first can miss updates published in between
* Feeds: instrument definitions, L3 order book, trades, instrument status and instrument summaries (reference price). US Perps provides trading status per instrument; the trading session status feed applies to Spot and Futures only
* Contiguous sequence numbers on every incremental feed, so gaps can be detected. Book, instrument, summary and trading-session gaps are recovered from a snapshot; there is no trade snapshot, so missed trades are not recovered

See the [SBE reference](https://docs.kraken.com/exchange/api-reference/sbe.md).

## Drop copy — FIX

The drop copy is a separate FIX 4.4 session that delivers a copy of every Execution Report on your account. The Execution Report is identical to the one on the order-entry session.

See the [Drop Copy reference](https://docs.kraken.com/exchange/api-reference/drop-copy.md).

## Related

> [card] [API Reference](https://docs.kraken.com/exchange/api-reference/overview.md)
>
> All Exchange API references.

> [card] [Connectivity](https://docs.kraken.com/exchange/guides/us-perps/connectivity.md)
>
> Connectivity and colocation guides.
