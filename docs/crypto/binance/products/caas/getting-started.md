---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/getting-started
api_type: Guide
updated_at: 2026-11-22 18:31:47.823630
---

# Getting Started

Use this page to prepare and sequence a Crypto-As-A-Service (CAAS) integration. It also applies to
[KYC SaaS](/products/kyc-saas/overview), which runs on the sub-accounts created here and has no
separate setup of its own.

## Before you begin

CAAS uses a server-to-server integration model. Your application calls Binance from your own
backend; there is no Binance-hosted interface for your end users.

Before you start building:

- Your institutional onboarding must be complete, and the commercial model — revenue share or
  [Markup](/products/caas/markup/overview) — agreed. Availability depends on jurisdiction, Binance
  entity, and the approved model. See [Overview](/products/caas/overview).
- Your **master account** must hold the CAAS permission. Every CAAS endpoint is called with the
  master account's API key; most of them sit under `/sapi/v1/broker/*`.
- Decide which products your end users need — spot, futures, KYC SaaS, Markup, or the
  [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) — since
  each is enabled per partner.
- Decide how your end users will complete KYC, which gates everything after account creation.

### What each module requires

CAAS is the base. Every other Binance Link module sits on top of a CAAS account, and each is enabled
per partner by the Link team.

| Module                                                                            | What must be in place first                                                                                                                                 |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CAAS**                                                                          | Nothing else — this page is the starting point.                                                                                                             |
| **[KYC SaaS](/products/kyc-saas/overview)**                                       | A CAAS account, enabled by the Link team.                                                                                                                   |
| **[Markup](/products/caas/markup/overview)**                                      | A CAAS account, **plus the markup model uplifted on your master account** by the Link team. Sub-accounts still need their KYC passed before they can trade. |
| **[Institutional Crypto Buy/Sell](/products/institutional-buy-sell/quick-start)** | A CAAS account with the module enabled by the Link team. Sub-accounts still need their KYC passed before they can trade.                                    |

:::note

**Markup and the Institutional Crypto Buy/Sell Solution each have their own Getting Started.** They
are enabled separately, on top of the setup on this page, and their onboarding, credentials and base
endpoints differ. Complete this page first, then see [Markup](/products/caas/markup/getting-started)
or [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/quick-start).

:::

## Account structure

| Level               | What it is                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Master account      | The partner's own Binance account. Holds the CAAS permission and is the parent of every end-user account.           |
| Sub-account         | One Binance account per end user, created by the partner through the API. Holds the end user's balances and orders. |
| Sub-account API key | The credential used to trade or transfer on a single sub-account's behalf.                                          |

## Recommended integration order

1. Complete CAAS onboarding and confirm the approved commercial model.
2. Confirm the account structure above and how end users map to sub-accounts.
3. Create a CAAS sub-account via API.
4. Process KYC for the end user, and validate that it has passed.
5. Enable any additional wallets the end user needs, for example Futures. Do this **before** the
   next step.
6. Create an API key for the sub-account, then set its permissions and IP restrictions.
7. Open the [user data streams](/products/caas/user-data-streams) for the accounts you need events
   from.
8. Complete testing and operational readiness before going live.

:::warning

**Order matters between steps 5 and 6.** `futuresTrade` and `marginTrade` are set when the API key
is **created**, so the corresponding wallet must already exist. Create the key first and it will not
work for those products.

Futures has an enable endpoint; **margin does not** — the margin wallet is created by transferring
any amount of an asset into it. Options are not available to CAAS sub-accounts.

:::

The endpoint-level walkthrough for steps 3 to 6 is in the
[Integration Guide](/products/caas/integration-guide).

## Where to go next

| If you need                                                        | Go to                                                             |
| ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| The step-by-step account creation flow                             | [Integration Guide](/products/caas/integration-guide)             |
| Base endpoints, rate limits, endpoint security, and error payloads | [API basics](/products/caas/basics/1.base-urls)                   |
| The full account, asset, and fee endpoint reference                | [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api) |
| End-user KYC                                                       | [Binance Link KYC SaaS](/products/kyc-saas/overview)              |

---

# Getting Started

Use this page to prepare and sequence a Crypto-As-A-Service (CAAS) integration. It also applies to
[KYC SaaS](/products/kyc-saas/overview), which runs on the sub-accounts created here and has no
separate setup of its own.

## Before you begin

CAAS uses a server-to-server integration model. Your application calls Binance from your own
backend; there is no Binance-hosted interface for your end users.

Before you start building:

- Your institutional onboarding must be complete, and the commercial model — revenue share or
  [Markup](/products/caas/markup/overview) — agreed. Availability depends on jurisdiction, Binance
  entity, and the approved model. See [Overview](/products/caas/overview).
- Your **master account** must hold the CAAS permission. Every CAAS endpoint is called with the
  master account's API key; most of them sit under `/sapi/v1/broker/*`.
- Decide which products your end users need — spot, futures, KYC SaaS, Markup, or the
  [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) — since
  each is enabled per partner.
- Decide how your end users will complete KYC, which gates everything after account creation.

### What each module requires

CAAS is the base. Every other Binance Link module sits on top of a CAAS account, and each is enabled
per partner by the Link team.

| Module                                                                            | What must be in place first                                                                                                                                 |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CAAS**                                                                          | Nothing else — this page is the starting point.                                                                                                             |
| **[KYC SaaS](/products/kyc-saas/overview)**                                       | A CAAS account, enabled by the Link team.                                                                                                                   |
| **[Markup](/products/caas/markup/overview)**                                      | A CAAS account, **plus the markup model uplifted on your master account** by the Link team. Sub-accounts still need their KYC passed before they can trade. |
| **[Institutional Crypto Buy/Sell](/products/institutional-buy-sell/quick-start)** | A CAAS account with the module enabled by the Link team. Sub-accounts still need their KYC passed before they can trade.                                    |

:::note

**Markup and the Institutional Crypto Buy/Sell Solution each have their own Getting Started.** They
are enabled separately, on top of the setup on this page, and their onboarding, credentials and base
endpoints differ. Complete this page first, then see [Markup](/products/caas/markup/getting-started)
or [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/quick-start).

:::

## Account structure

| Level               | What it is                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Master account      | The partner's own Binance account. Holds the CAAS permission and is the parent of every end-user account.           |
| Sub-account         | One Binance account per end user, created by the partner through the API. Holds the end user's balances and orders. |
| Sub-account API key | The credential used to trade or transfer on a single sub-account's behalf.                                          |

## Recommended integration order

1. Complete CAAS onboarding and confirm the approved commercial model.
2. Confirm the account structure above and how end users map to sub-accounts.
3. Create a CAAS sub-account via API.
4. Process KYC for the end user, and validate that it has passed.
5. Enable any additional wallets the end user needs, for example Futures. Do this **before** the
   next step.
6. Create an API key for the sub-account, then set its permissions and IP restrictions.
7. Open the [user data streams](/products/caas/user-data-streams) for the accounts you need events
   from.
8. Complete testing and operational readiness before going live.

:::warning

**Order matters between steps 5 and 6.** `futuresTrade` and `marginTrade` are set when the API key
is **created**, so the corresponding wallet must already exist. Create the key first and it will not
work for those products.

Futures has an enable endpoint; **margin does not** — the margin wallet is created by transferring
any amount of an asset into it. Options are not available to CAAS sub-accounts.

:::

The endpoint-level walkthrough for steps 3 to 6 is in the
[Integration Guide](/products/caas/integration-guide).

## Where to go next

| If you need                                                        | Go to                                                             |
| ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| The step-by-step account creation flow                             | [Integration Guide](/products/caas/integration-guide)             |
| Base endpoints, rate limits, endpoint security, and error payloads | [API basics](/products/caas/basics/1.base-urls)                   |
| The full account, asset, and fee endpoint reference                | [CAAS REST API](/catalog/vip-and-institutional-caas/api/rest-api) |
| End-user KYC                                                       | [Binance Link KYC SaaS](/products/kyc-saas/overview)              |