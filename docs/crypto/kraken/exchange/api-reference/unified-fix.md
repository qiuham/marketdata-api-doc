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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix'
updated_at: 2026-11-13
---

# Unified FIX

> FIX 4.4 reference for Spot and Derivatives — message types, session establishment, and endpoint mapping

The Kraken Unified FIX API is a FIX 4.4 implementation that covers
both Spot and Derivatives markets through a single set of credentials.
It is the lowest-latency order-entry path on the platform, with
deterministic sequencing, cancel-on-disconnect, and session-based
message replay.

For protocol architecture, supported messages, ClOrdID rules, STP, and
performance details, see the [FIX overview
guide](https://docs.kraken.com/exchange/guides/fix/introduction.md).

## Connection

| Environment | Hostname |
| :- | :- |
| Production | `colo-london.vip-fix.kraken.com` |
| UAT | `colo-london.vip-fix.uat.kraken.com` |

| Service | Port |
| :- | :- |
| Spot Trading | 4001 |
| Spot Market Data (L2) | 4000 |
| Spot Market Data (L3) | 4005 |
| Derivatives Trading | 4003 |
| Derivatives Market Data (L2) | 4002 |
| Derivatives Market Data (L3) | 4004 |

All connections use TCP with TLS 1.3. DNS records carry a 5-minute
TTL — always resolve at connection time, never bind to static IPs.

## Authentication

Authentication uses a **Spot FIX API Key**. The same key authorises
both Spot and Derivatives sessions on the appropriate ports — no
separate Derivatives FIX credentials are required.

See [FIX authentication](https://docs.kraken.com/exchange/guides/fix/authentication.md) for the
logon message structure, IP allow-listing, and CompID provisioning.

## Hours of operation

FIX sessions operate 24/7 with a logical session rollover every day at
**22:00 UTC**. The rollover lasts approximately 30 seconds. Both
Trading and Market Data sequence numbers reset to `0` after rollover.

## Cancel scope

Single-order cancels on FIX (`OrderCancelRequest`) only affect orders
placed on the same FIX session. To cancel orders placed on another
session — whether FIX, WebSocket, or REST — use
`OrderMassCancelRequest` (Tag 35=q) or fall back to REST/WebSocket.

## Quick start

> [card] [Logon](https://docs.kraken.com/exchange/api-reference/unified-fix/logon.md)
>
> Session establishment and parameters.

> [card] [NewOrderSingle (D)](https://docs.kraken.com/exchange/api-reference/unified-fix/nos.md)
>
> Place an order on Spot or Derivatives.

> [card] [ExecutionReport (8)](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md)
>
> Order acknowledgements, fills, cancels, and rejects.

> [card] [OrderMassCancelRequest (q)](https://docs.kraken.com/exchange/api-reference/unified-fix/omcr.md)
>
> Cancel all orders on the account, regardless of session.

The full message catalog — `OrderCancelRequest`, `OrderCancelReplaceRequest`,
`MarketDataRequest`, `OrderStatusRequest`, `ResendRequest`,
`SequenceReset`, headers/trailers, and reject types — is available in
the **Unified FIX** dropdown in the left navigation.

> [!NOTE]
>
> Access to direct colocation requires VIP status, an executed NDA, and
> an Equinix London presence. Contact your Account Manager to begin
> onboarding.

## Related

> [card] [FIX overview](https://docs.kraken.com/exchange/guides/fix/introduction.md)
>
> Session architecture, supported messages, performance, ports.

> [card] [FIX authentication](https://docs.kraken.com/exchange/guides/fix/authentication.md)
>
> Logon message and CompID setup.

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> REST vs WebSocket vs FIX — sequencing, cancel scope, latency.

> [card] [Colocation and connectivity](https://docs.kraken.com/exchange/guides/general/colocation.md)
>
> Connectivity tiers, latency expectations, LOA process.
