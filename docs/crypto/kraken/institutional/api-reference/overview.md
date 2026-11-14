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
source_url: 'https://docs.kraken.com/institutional/api-reference/overview'
updated_at: 2026-11-13
---

# Institutional API reference

> OTC, Custody, and Prime — pick the service and protocol for your workflow

Kraken's Institutional APIs cover three services. **OTC** and **Custody** are single-protocol; **Prime** offers REST, FIX, and WebSocket against the same accounts.

> [!NOTE]
>
> All Institutional APIs require onboarding through your Account Manager. See the [Institutional overview](https://docs.kraken.com/institutional/guides/overview.md) for use cases and access requirements.

## OTC

Off-book block trading with negotiated quotes — request, accept, and reconcile large trades.

> [card] [OTC REST](https://docs.kraken.com/institutional/api-reference/otc-rest.md)
>
> Quote requests, active and historical quotes, exposures.

## Custody

Programmatic management of segregated wallets, deposits, withdrawals, and reconciliation.

> [card] [Custody REST](https://docs.kraken.com/institutional/api-reference/custody-rest.md)
>
> Vaults, balances, deposit/withdraw methods, custody tasks and activities.

## Prime

Institutional brokerage with three protocol surfaces against the same Prime accounts and keys.

> [card] [Prime REST](https://docs.kraken.com/institutional/api-reference/prime-rest.md)
>
> API-user management, key lifecycle, and settlement batches.

> [card] [Prime FIX](https://docs.kraken.com/institutional/api-reference/prime-fix/logon.md)
>
> FIX 4.4 order management and market data — co-located, deterministic.

> [card] [Prime WebSocket](https://docs.kraken.com/institutional/api-reference/prime-websocket/authentication.md)
>
> Real-time order events, balances, exposures, and RFQ flows.

## Not sure where to start?

> [card] [Custody REST authentication](https://docs.kraken.com/institutional/guides/custody-rest-auth.md)
>
> Authenticate requests to the Custody REST API.

> [card] [Prime WebSocket authentication](https://docs.kraken.com/institutional/guides/prime-websocket-auth.md)
>
> Authenticate and subscribe to Prime WebSocket channels.
