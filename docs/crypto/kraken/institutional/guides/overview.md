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
source_url: 'https://docs.kraken.com/institutional/guides/overview'
updated_at: 2026-11-13
---

# Institutional overview

> OTC trading, custody, and prime brokerage APIs — designed for institutions managing large positions or client assets

Kraken's Institutional platform covers four distinct services, each purpose-built for a specific use case. Access to all Institutional APIs requires onboarding through your Kraken Account Manager.

## Services overview

| Service | What it does | Protocol |
| :- | :- | :- |
| **OTC** | Execute large block trades off the order book with minimal market impact | REST |
| **Custody** | Secure digital asset storage with segregated accounts, deposits, and withdrawals | REST |
| **Prime FIX** | Low-latency institutional order management via FIX 4.4 | FIX 4.4 |
| **Prime WebSocket** | Real-time market data, order updates, and account event streaming | WebSocket |

## What can I build?

> [card] Block trading desk
>
> Use the **OTC REST** API to request quotes and execute large trades at negotiated prices, avoiding slippage on the public order book. Suitable for single-asset and cross-asset block trades.

> [card] Institutional custody
>
> Use the **Custody REST** API to manage segregated wallets, automate deposit monitoring, initiate withdrawals, and reconcile client balances programmatically.

> [card] Prime order management
>
> Use **Prime FIX** for deterministic, low-latency order routing with cancel-on-disconnect, session-based message replay, and co-location at Equinix London. Designed for systematic and HFT workflows.

> [card] Real-time prime data
>
> Use **Prime WebSocket** to stream live order book data, fills, open positions, and account balances into your own execution or risk systems.

## Choosing your protocol

| Need | Use |
| :- | :- |
| Large off-book trade at a specific price | OTC REST |
| Programmatic custody and asset movement | Custody REST |
| Low-latency order management with replay | Prime FIX |
| Real-time fills and position data | Prime WebSocket |
| Combined order entry + data streaming | Prime FIX + Prime WebSocket |

## Getting started

All Institutional API access requires onboarding. Contact your Account Manager or reach out at [institutional@kraken.com](mailto:institutional@kraken.com) to:

* Request API credentials for the services you need
* Arrange co-location if using Prime FIX
* Complete any required NDA or compliance documentation

> [card] [Custody REST authentication](https://docs.kraken.com/institutional/guides/custody-rest-auth.md)
>
> How to authenticate requests to the Custody REST API

> [card] [Prime WebSocket authentication](https://docs.kraken.com/institutional/guides/prime-websocket-auth.md)
>
> How to authenticate and subscribe to Prime WebSocket channels
