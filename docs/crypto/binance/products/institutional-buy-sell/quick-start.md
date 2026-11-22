---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-buy-sell/quick-start
api_type: Guide
updated_at: 2026-11-22 18:29:54.014795
---

# Getting Started

Use this section to prepare and sequence a Institutional Crypto Buy/Sell Solution integration within
[Crypto-As-A-Service (CAAS)](/products/caas/overview).

## Before you begin

This module uses a server-to-server integration model. Most requests require a userId, which is the
customer's Binance sub-account ID created or mapped through the approved CaaS onboarding flow — see
[CAAS Overview](/products/caas/overview) for the account model and
[KYC SaaS](/products/kyc-saas/overview) for the customer onboarding flow that produces it.

Two things must be in place before you call anything:

- **A CAAS account with this module enabled by the Link team.** It is enabled per partner, on top of
  your CAAS integration.
- **The customer's sub-account KYC passed** through KYC SaaS. A sub-account cannot trade until its
  KYC has passed, so Buy and Sell will not work for that customer before then.

## Recommended integration order

1. Complete [CAAS onboarding](/products/caas/overview).

2. Confirm the institutional account structure and customer userId lifecycle.

3. Agree the fiat fund flow, settlement model, supported currencies/assets, limits, and spread
   configuration.

4. Apply for
   [Developer's Account](/products/institutional-buy-sell/basics/6.apply-developer-account),
   exchange public keys, configure API credentials, and allowlist server IP addresses.

5. Implement request signing and verify a discovery endpoint in QA.

6. Implement the required Buy and/or Sell flow.

7. Implement the required partner-hosted fiat confirmation, refund, and payout APIs.

8. Implement webhook signature verification and transaction-status recovery by polling.

9. Complete negative-path testing, reconciliation validation, operational readiness, and production
   approval.

---

# Getting Started

Use this section to prepare and sequence a Institutional Crypto Buy/Sell Solution integration within
[Crypto-As-A-Service (CAAS)](/products/caas/overview).

## Before you begin

This module uses a server-to-server integration model. Most requests require a userId, which is the
customer's Binance sub-account ID created or mapped through the approved CaaS onboarding flow — see
[CAAS Overview](/products/caas/overview) for the account model and
[KYC SaaS](/products/kyc-saas/overview) for the customer onboarding flow that produces it.

Two things must be in place before you call anything:

- **A CAAS account with this module enabled by the Link team.** It is enabled per partner, on top of
  your CAAS integration.
- **The customer's sub-account KYC passed** through KYC SaaS. A sub-account cannot trade until its
  KYC has passed, so Buy and Sell will not work for that customer before then.

## Recommended integration order

1. Complete [CAAS onboarding](/products/caas/overview).

2. Confirm the institutional account structure and customer userId lifecycle.

3. Agree the fiat fund flow, settlement model, supported currencies/assets, limits, and spread
   configuration.

4. Apply for
   [Developer's Account](/products/institutional-buy-sell/basics/6.apply-developer-account),
   exchange public keys, configure API credentials, and allowlist server IP addresses.

5. Implement request signing and verify a discovery endpoint in QA.

6. Implement the required Buy and/or Sell flow.

7. Implement the required partner-hosted fiat confirmation, refund, and payout APIs.

8. Implement webhook signature verification and transaction-status recovery by polling.

9. Complete negative-path testing, reconciliation validation, operational readiness, and production
   approval.