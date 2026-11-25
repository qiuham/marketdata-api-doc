---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-buy-sell/introduction
api_type: Guide
updated_at: 2026-11-25 18:30:54.087585
---

# Institutional Crypto Buy/Sell Solution

## What this module does

Institutional Buy/Sell is an **optional module of
[Crypto-As-A-Service (CAAS)](/products/caas/overview)**, not a standalone product. It builds on the
CAAS account, custody, and commission model described there, and is enabled only for partners
already onboarded to CAAS.

It lets an eligible CaaS partner offer Buy and Sell inside the partner's own customer experience.
Binance provides the crypto account and custody layer, supported-asset and pair discovery, pricing,
quote execution, crypto balance updates, transaction records, and order status events. The partner
owns its application experience and the local fiat movement required by the agreed operating model.

Core capabilities:

- Discover supported fiat currencies, crypto assets, trading pairs, precision, and amount limits.
- Request time-limited Buy or Sell quotes, including an approved partner spread where enabled.
- Execute quotes against a customer Binance sub-account.
- Query a customer's available crypto balance through the applicable Balance API.
- Receive signed order-status webhooks.
- Coordinate Buy fiat confirmation and refunds, and Sell fiat payouts, through partner-hosted APIs.
- Use optional market-data endpoints for price discovery and customer-interface content.

## Prerequisites in CAAS

Read these first — this module assumes the account and customer-onboarding mechanics they define:

| Prerequisite                                    | Where it is documented                                                                                         |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| CAAS account model, assets, and commission data | [CAAS Overview](/products/caas/overview) and [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api) |
| Customer onboarding and KYC data sharing        | [Binance Link KYC SaaS](/products/kyc-saas/overview)                                                           |
| Release history for the Binance Link suite      | [Binance Link Change Log](/products/binance-link/change-log)                                                   |

## Why use this module

- One CaaS proposition: Add fiat ↔ crypto to the same external CaaS product suite.
- Embedded customer journey: Keep the partner's brand, application, customer relationship, and local
  fiat experience while using Binance for crypto infrastructure.
- Faster path to market: Reuse Binance account, custody, liquidity, pricing, and execution
  capabilities rather than building and operating a crypto brokerage stack independently.
- Modular integration: Enable only the Buy/Sell directions, currencies, assets, and optional
  market-data capabilities approved for the partner.
- Institutional controls: Combine signed server APIs, account-level configuration, transaction
  records, webhooks, fiat callbacks, reconciliation, and partner-specific limits.

## Before you integrate

Availability is subject to institutional onboarding, jurisdiction, Binance entity, asset and fiat
support, customer eligibility, risk limits, and the approved commercial and settlement model. Please
contact your account manager for more information.

---

# Institutional Crypto Buy/Sell Solution

## What this module does

Institutional Buy/Sell is an **optional module of
[Crypto-As-A-Service (CAAS)](/products/caas/overview)**, not a standalone product. It builds on the
CAAS account, custody, and commission model described there, and is enabled only for partners
already onboarded to CAAS.

It lets an eligible CaaS partner offer Buy and Sell inside the partner's own customer experience.
Binance provides the crypto account and custody layer, supported-asset and pair discovery, pricing,
quote execution, crypto balance updates, transaction records, and order status events. The partner
owns its application experience and the local fiat movement required by the agreed operating model.

Core capabilities:

- Discover supported fiat currencies, crypto assets, trading pairs, precision, and amount limits.
- Request time-limited Buy or Sell quotes, including an approved partner spread where enabled.
- Execute quotes against a customer Binance sub-account.
- Query a customer's available crypto balance through the applicable Balance API.
- Receive signed order-status webhooks.
- Coordinate Buy fiat confirmation and refunds, and Sell fiat payouts, through partner-hosted APIs.
- Use optional market-data endpoints for price discovery and customer-interface content.

## Prerequisites in CAAS

Read these first — this module assumes the account and customer-onboarding mechanics they define:

| Prerequisite                                    | Where it is documented                                                                                         |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| CAAS account model, assets, and commission data | [CAAS Overview](/products/caas/overview) and [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api) |
| Customer onboarding and KYC data sharing        | [Binance Link KYC SaaS](/products/kyc-saas/overview)                                                           |
| Release history for the Binance Link suite      | [Binance Link Change Log](/products/binance-link/change-log)                                                   |

## Why use this module

- One CaaS proposition: Add fiat ↔ crypto to the same external CaaS product suite.
- Embedded customer journey: Keep the partner's brand, application, customer relationship, and local
  fiat experience while using Binance for crypto infrastructure.
- Faster path to market: Reuse Binance account, custody, liquidity, pricing, and execution
  capabilities rather than building and operating a crypto brokerage stack independently.
- Modular integration: Enable only the Buy/Sell directions, currencies, assets, and optional
  market-data capabilities approved for the partner.
- Institutional controls: Combine signed server APIs, account-level configuration, transaction
  records, webhooks, fiat callbacks, reconciliation, and partner-specific limits.

## Before you integrate

Availability is subject to institutional onboarding, jurisdiction, Binance entity, asset and fiat
support, customer eligibility, risk limits, and the approved commercial and settlement model. Please
contact your account manager for more information.