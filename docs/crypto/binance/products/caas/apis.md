---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/apis
api_type: Guide
updated_at: 2026-11-26 18:33:58.111789
---

# APIs

The CAAS API is on `/sapi/v1/broker/*`, grouped into three areas. Every endpoint is called with your
**master account** API key.

> This index does not replace the endpoint reference. Each endpoint's parameters, responses, and
> error codes are in the [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api).

| Area                                                                | What it covers                                                                                                                                     |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Account](/catalog/vip-and-institutional-caas/api/rest-api/account) | Create and delete sub-accounts, issue and delete their API keys, set key permissions and IP restrictions, enable futures, and query broker info.   |
| [Asset](/catalog/vip-and-institutional-caas/api/rest-api/asset)     | Query sub-account spot, margin, and futures balance summaries and deposit history, and move funds between the master account and its sub-accounts. |
| [Fee](/catalog/vip-and-institutional-caas/api/rest-api/fee)         | Set and query the commission you earn on each sub-account's spot and futures activity, and query rebate records.                                   |

## What is not in this API

| You need                           | Use instead                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------- |
| Spot or futures trading            | The main trading APIs, with the sub-account's own API key                               |
| External deposits and withdrawals  | [Wallet `/sapi/v1/capital/*`](/catalog/core-trading-wallet/api/rest-api/capital)        |
| Account and order events           | [User Data Streams](/products/caas/user-data-streams)                                   |
| End-user KYC                       | [KYC SaaS](/products/kyc-saas/overview)                                                 |
| Commission above Binance's own fee | [Markup](/products/caas/markup/overview)                                                |
| Fiat on/off-ramp                   | [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) |

The CAAS Asset endpoints move funds **between the master account and its own sub-accounts**. They do
not send funds to an external address — see
[Environments and API base URLs](/products/caas/basics/1.base-urls) for which product owns which
endpoint family.

---

# APIs

The CAAS API is on `/sapi/v1/broker/*`, grouped into three areas. Every endpoint is called with your
**master account** API key.

> This index does not replace the endpoint reference. Each endpoint's parameters, responses, and
> error codes are in the [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api).

| Area                                                                | What it covers                                                                                                                                     |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Account](/catalog/vip-and-institutional-caas/api/rest-api/account) | Create and delete sub-accounts, issue and delete their API keys, set key permissions and IP restrictions, enable futures, and query broker info.   |
| [Asset](/catalog/vip-and-institutional-caas/api/rest-api/asset)     | Query sub-account spot, margin, and futures balance summaries and deposit history, and move funds between the master account and its sub-accounts. |
| [Fee](/catalog/vip-and-institutional-caas/api/rest-api/fee)         | Set and query the commission you earn on each sub-account's spot and futures activity, and query rebate records.                                   |

## What is not in this API

| You need                           | Use instead                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------- |
| Spot or futures trading            | The main trading APIs, with the sub-account's own API key                               |
| External deposits and withdrawals  | [Wallet `/sapi/v1/capital/*`](/catalog/core-trading-wallet/api/rest-api/capital)        |
| Account and order events           | [User Data Streams](/products/caas/user-data-streams)                                   |
| End-user KYC                       | [KYC SaaS](/products/kyc-saas/overview)                                                 |
| Commission above Binance's own fee | [Markup](/products/caas/markup/overview)                                                |
| Fiat on/off-ramp                   | [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) |

The CAAS Asset endpoints move funds **between the master account and its own sub-accounts**. They do
not send funds to an external address — see
[Environments and API base URLs](/products/caas/basics/1.base-urls) for which product owns which
endpoint family.