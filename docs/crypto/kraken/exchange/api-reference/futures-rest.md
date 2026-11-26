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
updated_at: 2026-11-26
---

# Derivatives REST

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
