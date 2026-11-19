---
exchange: deribit
source_url: https://docs.deribit.com/starbase/quickstart
api_type: Starbase
updated_at: 2026-11-19 19:05:48.186429
---

# Starbase Connectivity Quickstart

> Plan Starbase network access, assign a Member before creating API keys, connect to test gateways and multicast feeds, and prepare for production.

This quickstart takes you from network planning to a validated Starbase connection. Create and assign a Member **before** you create any API key; Starbase authentication depends on it. Message schemas and order workflows are covered in the [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md).

> [!NOTE]
>
> Starbase is not available over the public internet. You must connect through **hosted colocation** or a **cross-connect** in LD4, or through **AWS Private Link**. Contact \[[colo-support@coinbase.com](mailto:colo-support@coinbase.com)]\(mailto:[colo-support@coinbase.com](mailto:colo-support@coinbase.com)) to arrange network access.

## 1. Choose a Deployment Model

The Starbase matching engine and its gateways run in **Equinix LD4 in London**. The Starbase API is exposed through several protocols, including SBE order entry, SBE multicast market data, FIX Drop Copy, and REST.

| Requirement | Recommended deployment |
| - | - |
| Lowest possible order-entry latency | Use hosted colocation or a cross-connect in LD4 |
| Private connectivity from an AWS-hosted stack | Use AWS Private Link; latency depends on the AWS region and route to LD4 |
| Monitoring, reconciliation, or disaster recovery | Run remotely, outside the critical execution path |

A server in Tokyo or another remote region cannot match the round-trip latency of LD4 colocation because every order must reach the matching engine in London.

> [!NOTE]
>
> **Scope**: Starbase is for derivatives only. Spot trading is not available on Starbase and will migrate to a brokered solution via Coinbase Exchange (existing spot APIs remain unchanged). The standard WebSocket API is supported indefinitely alongside Starbase; the legacy SBE feed is scheduled for deprecation at the end of 2026. See [Scope and migration](https://docs.deribit.com/starbase/overview.md#scope-and-migration).

For detailed trade-offs and cost categories, see [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md#deployment-options).

## 2. Request Starbase Access

Before connecting:

1. Ask your Account Manager or Technical Account Manager to enable Starbase on your **test account**.
2. Confirm which main account and subaccounts will trade through Starbase.
3. Arrange hosted colocation, a cross-connect, or AWS Private Link with [[colo-support@coinbase.com](mailto:colo-support@coinbase.com)](mailto:colo-support@coinbase.com).
4. Provide the source IP addresses that Deribit should allowlist.

> [!NOTE]
>
> Starbase API keys are separate from standard Deribit API keys. Do not create keys yet. The next step assigns those subaccounts to a Member, which is required before any Starbase key can be created.

## 3. Create and Assign a Member

Create a Member on the **main account** and assign every UID that will trade on Starbase **before** you create any API key. Skipping this step is the usual cause of the **"No active member"** error, and leaves the subaccount with no Starbase authentication.

1. Switch into the **main-account UID**. Subaccounts cannot create or manage Members.
2. Open the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel (not the standard **API** section).
3. Click **Add Member**, give it a name, and select every main-account and/or subaccount UID that needs Starbase access.
4. Confirm the Member is active and that each trading subaccount appears in its account list.

Most clients can configure only **one Member**, so add every UID to that Member. Broker clients that need separate Members for independent end clients must contact [[support@deribit.com](mailto:support@deribit.com)](mailto:support@deribit.com) first.

You can do the same programmatically from the main account with [`private/set_member`](https://docs.deribit.com/api-reference/account-management/private-set_member). See [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md) for the UI and API workflow, and [Account Model](https://docs.deribit.com/starbase/account-model.md) for how Members, portfolios, and rate limits relate.

> [!WARNING]
>
> **"No active member" error**: Key creation fails if the target account does not belong to an active Member. Members are managed at the **main-account level only**. Add the account to a Member first, then create the key while switched into the subaccount UID. Every subaccount that trades on Starbase needs a Member; without one there is no Starbase authentication for that subaccount.

## 4. Create a Starbase API Key

Create the key from the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel **after** the subaccount belongs to an active Member. Members are configured on the **main account**, but the key itself is created while switched into the subaccount UID that will use it. Select the Member and portfolio permissions required by the trading application.

See [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md) for the full UI and API workflow.

Keep credentials out of source code, logs, packet captures, and support tickets. Store them in your organization's secret-management system.

Key and session limits to plan around:

* Up to **8 Starbase API keys per subaccount** (separate from the standard Deribit key quota; standard keys cannot authenticate to Starbase).
* **One connection per gateway per key**, up to 10 connections across the 5 gateway pairs with a single key.
* Reconnecting the same key to the same gateway **terminates the existing session**.

## 5. Prepare the Client

Download the integration resources:

* SBE XML schemas for [order entry](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml) and [market data](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml)
* [Order entry SDK](https://docs.deribit.com/starbase/starbase-deribit-order-sdk-14.0.zip) for the SBE order entry API (schema version 14, semantic version 1.5)
* [Market data SDK](https://docs.deribit.com/starbase/starbase-deribit-md-sdk-2.0.zip) for the SBE market data API (schema version 2, semantic version 1.0)
* [Market data PCAP](http://statics.deribit.com/files/starbase-market-data.pcap), a sample multicast packet capture

Then implement:

* [SBE framing, encoding, and decoding](https://docs.deribit.com/starbase/binary-api-reference.md#message-structure)
* [TCP session establishment, authentication, heartbeats, and sequence tracking](https://docs.deribit.com/starbase/session-messages.md)
* Automatic reconnect and state recovery
* [Cancel on Disconnect handling](https://docs.deribit.com/starbase/cancel-on-disconnect.md)
* [UDP multicast reception, packet sequencing, and gap detection](https://docs.deribit.com/starbase/multicast-subscription-guide.md)
* [Snapshot plus incremental L3 order-book reconstruction](https://docs.deribit.com/starbase/order-book-maintenance.md)

Use **IPv4**. SBE order entry uses TCP, multicast market data uses UDP, and REST utility endpoints use plain HTTP. No Starbase traffic is TLS-encrypted. REST, FIX Drop Copy, and multicast are available only on private connectivity, and omitting TLS keeps latency lower.

> [!NOTE]
>
> **Index and mark prices are published on the multicast feed.** Index prices are distributed per currency pair via `IndexInfo` (12), mark price and price bands via `InstrumentInfo` (14), and funding rates and open interest via `InstrumentRef` (15). They are also available from the standard API (`deribit_price_index.{index_name}`, [`public/get_index_price`](https://docs.deribit.com/api-reference/market-data/public-get_index_price), or `ticker.{instrument}.{interval}`). See [Reference Data](https://docs.deribit.com/starbase/reference-data.md#index-prices-and-derived-statistics). Note also that `quantityExponent` is available via the multicast snapshot only; Starbase REST `get_instruments` conveys the same information via `qty_tick_size`, which equals `minOrderQuantity × 10^quantityExponent`. [Classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) does not return `qty_tick_size`; use `min_trade_amount` instead. Neither field is `contract_size`. See [Reference Data](https://docs.deribit.com/starbase/reference-data.md#quantity-tick-size-across-sbe-and-rest).

## 6. Validate Test Connectivity

Use the addresses and ports in [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md#test-environment). Validate each service separately:

1. Establish TCP connectivity to the test SBE order-entry gateway.
2. Authenticate and maintain a healthy heartbeat exchange.
3. Connect to [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md) and complete its session logon.
4. Receive both snapshot and incremental traffic from the required [multicast channels](https://docs.deribit.com/starbase/multicast-channels.md).
5. Verify that [retransmit requests](https://docs.deribit.com/starbase/retransmit-gateway.md) can recover an intentional market-data gap.
6. Connect to the [REST portfolio-management endpoints](https://docs.deribit.com/starbase/portfolio-management.md) over HTTP.

Do not treat a successful TCP connection as a complete test. Authentication, heartbeats, sequence handling, multicast group membership, and recovery must all work.

## 7. Build a Resilient Session Layout

Production order-entry gateways are organized into hot-hot **A/B pairs** according to the instrument's [underlying tier](https://docs.deribit.com/starbase/underlying-tiers.md):

| Product group | Order-entry connections |
| - | - |
| [BTC (Tier 1)](https://docs.deribit.com/starbase/underlying-tiers.md#tier-1) | BTC A and BTC B |
| [ETH (Tier 1)](https://docs.deribit.com/starbase/underlying-tiers.md#tier-1) | ETH A and ETH B |
| [Tier 2](https://docs.deribit.com/starbase/underlying-tiers.md#tier-2) | Tier 2 A and Tier 2 B |
| [Tier 3](https://docs.deribit.com/starbase/underlying-tiers.md#tier-3) | Tier 3 A and Tier 3 B |
| RWA and pre-IPO | RWA A and RWA B |

Connect only to the product groups you trade, but always connect to **both A and B** within each required pair. Both sides are active, and their rate-limit buckets are independent.

Each API key can establish one connection to each gateway instance. A second connection using the same key on the same gateway disconnects the first. Order placement and fills are scoped to the API key and gateway session that originated the order. Amend and cancel acknowledgements are also delivered to the other session in the pair when that session sent the request. See [Cross-session acknowledgements](https://docs.deribit.com/starbase/amending-order.md#cross-session-acknowledgements).

## 8. Validate End-to-End Behavior

On test, verify the complete lifecycle before requesting production access:

* [Submit](https://docs.deribit.com/starbase/placing-new-order.md), [amend](https://docs.deribit.com/starbase/amending-order.md), and [cancel](https://docs.deribit.com/starbase/cancelling-order.md) a single order.
* Send a [mass quote](https://docs.deribit.com/starbase/mass-quotes.md) if your strategy uses option quoting.
* Confirm responses on the originating SBE session.
* Confirm lifecycle events and fills on [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md).
* Confirm trades through the standard private WebSocket API.
* Confirm that open Starbase orders appear in the web UI (open orders and pre-trade risk refresh every 10 seconds) and do **not** appear in the private WebSocket order feed.
* Reconcile orders across feeds: `starbase_order_id` on the standard APIs maps to `OrderID` (Tag 37) on Drop Copy, and fills deduplicate on the `(starbase_match_id, starbase_order_id)` tuple. See [Reconciliation Across APIs](https://docs.deribit.com/starbase/fix-drop-copy-api.md#reconciliation-across-apis).
* Simulate a Drop Copy gap and recover it: detect the gap via `MsgSeqNum` (34), then replay fills with `EventResendRequest` (F3) and Block Trades and Block RFQ trades with `TradeCaptureReportRequest` (AD).
* Disconnect a session and verify [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md) behavior.
* Reconnect with `resetSeqNum=0` and confirm that a too-low inbound seqNum is rejected while a gap is ignored; after a `SEQUENCE_RESET`, reconnect with `resetSeqNum=1`. See [Sequence numbers](https://docs.deribit.com/starbase/session-messages.md#sequence-numbers).
* Reconnect, rebuild state, and resubmit only after reviewing current market conditions.
* Exercise A/B failover without losing the local view of orders or the book.

> [!NOTE]
>
> **Reconciliation essentials**:
>
> * FIX Drop Copy is configured **per Member**. One session delivers the full Member feed for all subaccounts; filter on `portfolioId` for per-portfolio separation.
> * `ClOrdID` is **FIX-only**. To track a client order ID on WebSocket notifications, send it in the `deribitLabel` field.
> * Liquidation cancels arrive on the gateway where the order was placed. Monitor `OrdersCanceled` with `cancelReason = 5` on every session.
> * A cancel sent from another session is reported to the submitting session as `OrdersCanceled` (schema version `17` or later). The cancelling session receives `CancelOrderResponse`.
> * Persist Drop Copy Execution Reports as they arrive; rejected and zero-fill orders cannot be retrieved from order history later.

> [!WARNING]
>
> Cancel on Disconnect is always enabled and session-scoped. Orders from a disconnected session are cancelled immediately and are not restored when the session reconnects.

Before production, also review behavior that can change order acceptance or timing: [speed bumps](https://docs.deribit.com/starbase/speed-bumps.md), [Market Maker Protection](https://docs.deribit.com/starbase/mmp.md), [Self Match Prevention](https://docs.deribit.com/starbase/smp.md), and [risk bypass](https://docs.deribit.com/starbase/risk-bypass.md). Note the MMP scoping difference: order MMP applies **per subaccount and base/quote pair**, while mass-quote MMP works through an explicit `mmpGroupId` referenced on every `MassQuoteRequest`.

> [!TIP]
>
> Utilizing the [MMP risk bypass](https://docs.deribit.com/starbase/risk-bypass.md) is the lowest-latency method for market access and the recommended default for most integrating clients. It works for both orders and mass quotes and reduces load on Deribit's risk and margin engines.

## 9. Review Capacity

Starbase rate limits are applied **per Member, per gateway, and per quoting type**. API keys and sessions within the same Member do not each receive a fresh allocation.

Before production:

* Estimate steady-state and burst order rates by product tier. Burst and steady-state rates are identical under the defaults; per-member overrides can decouple them.
* Separate single-order traffic from [mass-quote](https://docs.deribit.com/starbase/mass-quotes.md) traffic. Within a product tier, options and futures share the same buckets.
* Use both A and B gateways where appropriate. Multiple keys or sessions do **not** multiply limits. The independent A and B buckets (an effective 2x per pair) are the only scaling factor.
* Remember that cancels are never rejected for rate limits but do consume tokens: standard cancels cost the same as a new order, mass-quote cancels 1/20th, and mass cancels nothing.
* Confirm the number of API keys and active orders required.
* Discuss non-default allocations with your Account Manager.

See [API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md) for bucket behavior, defaults, and other limits, including the `get_open_orders` REST endpoint. That endpoint is capped at 10 requests per minute per portfolio on each REST gateway and is intended as a recovery tool rather than a live order feed.

## 10. Prepare for Production

Production readiness should include:

* Redundant client hosts, network interfaces, and power where applicable
* Active connections to both sides of every required gateway pair
* Both A and B [multicast feeds](https://docs.deribit.com/starbase/multicast-channels.md), including snapshot and [retransmit recovery](https://docs.deribit.com/starbase/retransmit-gateway.md)
* Independent [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md) ingestion and durable event persistence
* [Clock synchronization](https://docs.deribit.com/starbase/binary-api-reference.md#clock-synchronization); colocated clients can request PTP
* Metrics and alerts for session state, heartbeats, sequence gaps, rejects, and recovery
* A tested runbook for disconnects, stale books, failover, and reconciliation

Use the production endpoints only after Deribit confirms that account, credentials, source IPs, and network access are ready.

## Troubleshooting

If connectivity fails, record:

* Test or production environment
* Connectivity type and hosting provider
* Account UID and Starbase ClientID
* Source IP, destination IP, port, protocol, gateway, and side
* UTC timestamps and the last successful heartbeat or sequence number
* Whether side A, side B, or both are affected
* TCP-connectivity results and a short sanitized packet capture
* Expected behavior, observed behavior, and any reject code

Send network and multicast issues to [[colo-support@coinbase.com](mailto:colo-support@coinbase.com)](mailto:colo-support@coinbase.com). Send protocol rejects and account-configuration questions to your Technical Account Manager or Deribit Support.

## Next Steps

> [card] [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
>
> Create the Member and assign every trading subaccount before generating API keys.

> [card] [Production Readiness Checklist](https://docs.deribit.com/starbase/production-readiness-checklist.md)
>
> Verify Member setup, API key scopes, MMP risk bypass, SBE XMLs, and logon.

> [card] [Infrastructure & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
>
> Review deployment costs, gateway architecture, failover, and protocol selection.

> [card] [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
>
> Find test and production addresses, ports, and gateway mappings.

> [card] [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)
>
> Implement session and order-entry messages.

> [card] [Multicast Subscription Guide](https://docs.deribit.com/starbase/multicast-subscription-guide.md)
>
> Configure multicast reception and local book maintenance.


## Related topics

- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)
- [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
- [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)