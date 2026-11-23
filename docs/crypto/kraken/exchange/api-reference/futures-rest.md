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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-rest'
updated_at: 2026-11-23
---

# Derivatives REST

> Deprecated. The Derivatives REST API will be decommissioned on 1 March 2027.

> [!WARNING]
>
> **The Derivatives REST API is deprecated and will be decommissioned on 1 March 2027.**
>
> After that date the Derivatives REST API will no longer be available. Do not
> start new integrations on it. Use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket.md) for market data,
> account updates and order entry on one connection, or the
> [Unified FIX API](https://docs.kraken.com/exchange/api-reference/unified-fix.md) for FIX order entry.
> Migrate before 1 March 2027.

## Timeline

| Date | What happens |
| :- | :- |
| **Today** | The Derivatives REST API keeps working. It is deprecated, so build new integrations on the Unified WebSocket or Unified FIX. |
| **1 March 2027** | The Derivatives REST API is decommissioned and is no longer available. |

## What the Derivatives REST API is

The Derivatives REST API gives you request and response access to your Kraken
Derivatives (Futures) account over HTTPS. It is served from:

```text theme={null}
https://futures.kraken.com/derivatives/api/v3
```

Public endpoints return market data. Private endpoints need a Derivatives API
key and an `Authent` signature on each request. See the
[Derivatives REST guide](https://docs.kraken.com/exchange/guides/futures/rest.md) for the authentication
flow.

The API covers these areas:

| Area | What it covers |
| :- | :- |
| Market Data | Tickers, order book and trade history |
| Instruments | Instrument definitions and status |
| Order Management | Placing, editing and cancelling orders, singly or in batch |
| Account | Account data, balances and positions |
| Multi-Collateral | Endpoints for the multi-collateral markets |
| Fee Schedules | Fee schedule endpoints (these no longer reflect the fees charged on Futures trades) |
| Historical Data, Account History, Market History, Candles, Analytics | Historical and analytical data |
| Trading Settings | Trading preferences for your account |
| Subaccounts, Transfers | Subaccount management and transfers |
| Assignment Program, RFQs | The assignment program and requests for quote |
| General, API Keys | General endpoints and API key checks |

The full endpoint list is in this section of the left navigation.

## Where to move

> [card] [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket.md)
>
> Market data, account updates and order entry on one socket, with lower latency and official SDKs.

> [card] [Unified FIX](https://docs.kraken.com/exchange/api-reference/unified-fix.md)
>
> FIX 4.4 order entry across Spot and Derivatives.

To use the Unified WebSocket you need a Kraken API key, not a Derivatives API
key. See
[Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket.md#authentication).

> [!NOTE]
>
> The [Derivatives WebSocket](https://docs.kraken.com/exchange/api-reference/futures-websocket.md) is also
> deprecated and will be decommissioned on 1 March 2027.

## Related

> [card] [Derivatives REST guide](https://docs.kraken.com/exchange/guides/futures/rest.md)
>
> Authentication, request format and response structure.

> [card] [Derivatives rate limits](https://docs.kraken.com/exchange/guides/futures/ratelimits.md)
>
> Limits that apply to the Derivatives REST API.

> [card] [Derivatives introduction](https://docs.kraken.com/exchange/guides/futures/introduction.md)
>
> Endpoints, protocols and conventions for the Derivatives platform.

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> REST vs WebSocket vs FIX trade-offs.
