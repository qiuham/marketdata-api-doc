---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/overview
api_type: Guide
updated_at: 2026-11-18 02:05:56.392519
---

# Crypto-As-A-Service (CAAS)

Crypto-As-A-Service (CAAS) is a backend API solution that lets a platform offer crypto functionality
to its users without building a full exchange, custody, wallet, trading, or settlement
infrastructure from scratch.

Instead of operating the full crypto stack yourself, your application connects to Binance through
APIs. Your team only needs to build and manage the front end user experience, while the CAAS backend
handles the core crypto operations such as account creation, wallet management, balances, transfers,
trading, deposits, withdrawals, and reporting.

![CAAS architecture: your front end calls your backend, which calls the CAAS API](./images/caas-architecture.png)

## Account Structure

CAAS works on a modular level with the sub-account system as the central core infrastructure. Each
account is held by a master account and every user under it is created as a sub-account. Each
sub-account functions as a wallet with its own unique deposit address.

![CAAS account structure: a master account holding one sub-account per end user](./images/caas-account-structure.png)

See [Getting Started](/products/caas/getting-started) for how to create sub-accounts and issue their
API keys.

## What the API covers

Once that foundation is in place, available products such as institutional buy/sell crypto
(on/off-ramp), spot trading, futures trading, and KYC SaaS can be layered on top as modular
services.

API Integration generally covers:

| Area                                                                                      | What it does                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CAAS Account](/catalog/vip-and-institutional-caas/api/rest-api/account)                  | Create and manage Binance sub-accounts for the partner's end users, and manage their API keys and permissions.                                                                                       |
| [CAAS Asset](/catalog/vip-and-institutional-caas/api/rest-api/asset)                      | Query sub-account balances and deposit history, and move funds between the master account and its sub-accounts.                                                                                      |
| [CAAS Fee](/catalog/vip-and-institutional-caas/api/rest-api/fee)                          | Query and configure the commission the partner earns on its end users' activity.                                                                                                                     |
| [Wallet](/catalog/core-trading-wallet/api/rest-api/capital)                               | External movement of funds: fetch a sub-account's deposit address, submit withdrawals, and query deposit and withdrawal history and per-coin network config, through `/sapi/v1/capital/*`.           |
| [Travel Rule](/catalog/core-trading-wallet/api/rest-api/travel-rule)                      | Required where your sub-accounts sit under a Binance local entity. Submit originator/beneficiary information for deposits and withdrawals and look up VASPs and per-country questionnaires.          |
| [Spot Trading](/catalog/core-trading-spot-trading/api/rest-api)                           | Place and manage spot orders for your end users' sub-accounts, and query their trades and order history, through the main `/api/*` endpoints.                                                        |
| [Futures Trading](/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api) | Trade USD-M futures from your end users' sub-accounts through the main `/fapi/*` endpoints. COIN-M is covered by [`/dapi/*`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api). |
| [KYC SaaS](/catalog/vip-and-institutional-kyc-saas/api/rest-api)                          | Verify your end users' identity: submit KYC information for a sub-account, query its verification status, and respond to requests for additional information.                                        |
| [Markup](/catalog/vip-and-institutional-vip-caas/api/rest-api)                            | Set the commission your end users pay above Binance's own fee, using fee groups. See the [Markup Overview](/products/caas/markup/overview).                                                          |
| [Institutional Buy/Sell](/products/institutional-buy-sell/introduction)                   | Embed a fiat on/off-ramp in your own application: quote, execute, and track end-user fiat-to-crypto purchases and sales.                                                                             |

KYC SaaS, Markup and the Institutional Crypto Buy/Sell Solution are modules enabled per partner, on
top of the core CAAS integration. Travel Rule applies only to sub-accounts held under a Binance
local entity — see the [deposit](/products/wallet/travel-rule/deposit-questionnaire) and
[withdrawal](/products/wallet/travel-rule/withdraw-questionnaire) questionnaires. Everything else is
part of the base integration.

## Where to go next

Next, read [Getting Started](/products/caas/getting-started) for prerequisites and the integration
order, then the [Integration Guide](/products/caas/integration-guide) for the step-by-step account
creation flow. The API basics are [base URLs](/products/caas/basics/1.base-urls),
[rate limits](/products/caas/basics/4.rate-limits) and
[endpoint security](/products/caas/basics/5.endpoint-security). Release history is in the
[Binance Link Change Log](/products/binance-link/change-log).

## Before you integrate

CAAS is a gated service. Availability is subject to institutional onboarding, jurisdiction, Binance
entity, and the approved commercial model. For more information, please contact
[link@binance.com](mailto:link@binance.com) or your account manager.

---

# Crypto-As-A-Service (CAAS)

Crypto-As-A-Service (CAAS) is a backend API solution that lets a platform offer crypto functionality
to its users without building a full exchange, custody, wallet, trading, or settlement
infrastructure from scratch.

Instead of operating the full crypto stack yourself, your application connects to Binance through
APIs. Your team only needs to build and manage the front end user experience, while the CAAS backend
handles the core crypto operations such as account creation, wallet management, balances, transfers,
trading, deposits, withdrawals, and reporting.

![CAAS architecture: your front end calls your backend, which calls the CAAS API](./images/caas-architecture.png)

## Account Structure

CAAS works on a modular level with the sub-account system as the central core infrastructure. Each
account is held by a master account and every user under it is created as a sub-account. Each
sub-account functions as a wallet with its own unique deposit address.

![CAAS account structure: a master account holding one sub-account per end user](./images/caas-account-structure.png)

See [Getting Started](/products/caas/getting-started) for how to create sub-accounts and issue their
API keys.

## What the API covers

Once that foundation is in place, available products such as institutional buy/sell crypto
(on/off-ramp), spot trading, futures trading, and KYC SaaS can be layered on top as modular
services.

API Integration generally covers:

| Area                                                                                      | What it does                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CAAS Account](/catalog/vip-and-institutional-caas/api/rest-api/account)                  | Create and manage Binance sub-accounts for the partner's end users, and manage their API keys and permissions.                                                                                       |
| [CAAS Asset](/catalog/vip-and-institutional-caas/api/rest-api/asset)                      | Query sub-account balances and deposit history, and move funds between the master account and its sub-accounts.                                                                                      |
| [CAAS Fee](/catalog/vip-and-institutional-caas/api/rest-api/fee)                          | Query and configure the commission the partner earns on its end users' activity.                                                                                                                     |
| [Wallet](/catalog/core-trading-wallet/api/rest-api/capital)                               | External movement of funds: fetch a sub-account's deposit address, submit withdrawals, and query deposit and withdrawal history and per-coin network config, through `/sapi/v1/capital/*`.           |
| [Travel Rule](/catalog/core-trading-wallet/api/rest-api/travel-rule)                      | Required where your sub-accounts sit under a Binance local entity. Submit originator/beneficiary information for deposits and withdrawals and look up VASPs and per-country questionnaires.          |
| [Spot Trading](/catalog/core-trading-spot-trading/api/rest-api)                           | Place and manage spot orders for your end users' sub-accounts, and query their trades and order history, through the main `/api/*` endpoints.                                                        |
| [Futures Trading](/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api) | Trade USD-M futures from your end users' sub-accounts through the main `/fapi/*` endpoints. COIN-M is covered by [`/dapi/*`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api). |
| [KYC SaaS](/catalog/vip-and-institutional-kyc-saas/api/rest-api)                          | Verify your end users' identity: submit KYC information for a sub-account, query its verification status, and respond to requests for additional information.                                        |
| [Markup](/catalog/vip-and-institutional-vip-caas/api/rest-api)                            | Set the commission your end users pay above Binance's own fee, using fee groups. See the [Markup Overview](/products/caas/markup/overview).                                                          |
| [Institutional Buy/Sell](/products/institutional-buy-sell/introduction)                   | Embed a fiat on/off-ramp in your own application: quote, execute, and track end-user fiat-to-crypto purchases and sales.                                                                             |

KYC SaaS, Markup and the Institutional Crypto Buy/Sell Solution are modules enabled per partner, on
top of the core CAAS integration. Travel Rule applies only to sub-accounts held under a Binance
local entity — see the [deposit](/products/wallet/travel-rule/deposit-questionnaire) and
[withdrawal](/products/wallet/travel-rule/withdraw-questionnaire) questionnaires. Everything else is
part of the base integration.

## Where to go next

Next, read [Getting Started](/products/caas/getting-started) for prerequisites and the integration
order, then the [Integration Guide](/products/caas/integration-guide) for the step-by-step account
creation flow. The API basics are [base URLs](/products/caas/basics/1.base-urls),
[rate limits](/products/caas/basics/4.rate-limits) and
[endpoint security](/products/caas/basics/5.endpoint-security). Release history is in the
[Binance Link Change Log](/products/binance-link/change-log).

## Before you integrate

CAAS is a gated service. Availability is subject to institutional onboarding, jurisdiction, Binance
entity, and the approved commercial model. For more information, please contact
[link@binance.com](mailto:link@binance.com) or your account manager.