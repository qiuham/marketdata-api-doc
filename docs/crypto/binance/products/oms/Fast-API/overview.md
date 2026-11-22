---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/oms/Fast-API/overview
api_type: Guide
updated_at: 2026-11-22 18:35:23.045803
---

# Fast API

Fast API can help users quickly authorize specific account permissions, create API keys, and
automatically connect to third-party API link platforms. For more details, please refer to the
[FAQ](https://www.binance.com/en/support/faq/what-is-fast-api-and-how-does-it-work-6aa7e2253c544d91b60746bfd03fd75d).

Fast API is part of [OMS Toolkit](/products/oms/overview). It is a **separate integration** from
trade tagging: a different host, OAuth instead of request signing, and its own onboarding.

## Onboarding Steps

1. Log in [Binance Developer center](https://developers.binance.com/en) with
   [verified entity(enterprise) account](https://www.binance.com/en/support/faq/how-to-complete-entity-verification-kyb-on-binance-step-by-step-guide-360015552032)
2. Apply for "**Entity KYB**" & "**OAuth Security KYB**"
3. Once both passed, client can create "**Client ID**", upload "**logo(60 x60)**" and set up
   "**callback url**". We will send an Email that include “**Client ID**” and “**Client
   Secret**”(**please do not share your Client secret with anyone**)
4. Download the [SDK](https://drive.google.com/file/d/1xFvDTEjUQCL8bviGR9FfszzTiV6pN8Ci/view) for
   utilizing the pop up dialogues.
5. Apply for the oAuth scopes required.
6. Start development of oAuth and Fast API.

:::note

**If your application appears stuck at any of the steps above**, contact
[link@binance.com](mailto:link@binance.com) or your Account Manager. Steps 2 and 3 depend on a
Binance-side review, so progress there is not something you can unblock from the Developer Center.

:::

### Minimum requirements for Fast API:

- `account:status`
- `create:apikey` (For Spot & Margin trading permission, and Futures trading permission) _Or_
  `create:apikey:margin` (For Margin Loan, repay, and Transfer permission) _Or_
  `create:apikey:options` (For European Options Trading permission)
- `user:openId`

## Where to go next

| If you need                  | Go to                                                                     |
| ---------------------------- | ------------------------------------------------------------------------- |
| Base URL and OAuth mechanics | [Environments and API base URLs](/products/oms/Fast-API/base-urls)        |
| Error codes                  | [API Error Code](/products/oms/Fast-API/error-code)                       |
| The endpoint reference       | [Fast API REST](/catalog/vip-and-institutional-oms/api/rest-api/fast-api) |
| The trade tagging side       | [OMS Integration Guide](/products/oms/integration-guide)                  |

---

# Fast API

Fast API can help users quickly authorize specific account permissions, create API keys, and
automatically connect to third-party API link platforms. For more details, please refer to the
[FAQ](https://www.binance.com/en/support/faq/what-is-fast-api-and-how-does-it-work-6aa7e2253c544d91b60746bfd03fd75d).

Fast API is part of [OMS Toolkit](/products/oms/overview). It is a **separate integration** from
trade tagging: a different host, OAuth instead of request signing, and its own onboarding.

## Onboarding Steps

1. Log in [Binance Developer center](https://developers.binance.com/en) with
   [verified entity(enterprise) account](https://www.binance.com/en/support/faq/how-to-complete-entity-verification-kyb-on-binance-step-by-step-guide-360015552032)
2. Apply for "**Entity KYB**" & "**OAuth Security KYB**"
3. Once both passed, client can create "**Client ID**", upload "**logo(60 x60)**" and set up
   "**callback url**". We will send an Email that include “**Client ID**” and “**Client
   Secret**”(**please do not share your Client secret with anyone**)
4. Download the [SDK](https://drive.google.com/file/d/1xFvDTEjUQCL8bviGR9FfszzTiV6pN8Ci/view) for
   utilizing the pop up dialogues.
5. Apply for the oAuth scopes required.
6. Start development of oAuth and Fast API.

:::note

**If your application appears stuck at any of the steps above**, contact
[link@binance.com](mailto:link@binance.com) or your Account Manager. Steps 2 and 3 depend on a
Binance-side review, so progress there is not something you can unblock from the Developer Center.

:::

### Minimum requirements for Fast API:

- `account:status`
- `create:apikey` (For Spot & Margin trading permission, and Futures trading permission) _Or_
  `create:apikey:margin` (For Margin Loan, repay, and Transfer permission) _Or_
  `create:apikey:options` (For European Options Trading permission)
- `user:openId`

## Where to go next

| If you need                  | Go to                                                                     |
| ---------------------------- | ------------------------------------------------------------------------- |
| Base URL and OAuth mechanics | [Environments and API base URLs](/products/oms/Fast-API/base-urls)        |
| Error codes                  | [API Error Code](/products/oms/Fast-API/error-code)                       |
| The endpoint reference       | [Fast API REST](/catalog/vip-and-institutional-oms/api/rest-api/fast-api) |
| The trade tagging side       | [OMS Integration Guide](/products/oms/integration-guide)                  |