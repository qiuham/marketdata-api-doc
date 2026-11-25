---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/Faq
api_type: Guide
updated_at: 2026-11-25 18:33:06.362312
---

# FAQ

## Crypto-As-A-Service (CAAS)

### How often are rebates paid out, and how do I check them?

Rebates are credited on an ongoing basis rather than on a fixed payout schedule. The normal delay is
around 30 minutes after the trade.

Query your rebate records with:

| Product         | Endpoint                                          |
| --------------- | ------------------------------------------------- |
| Spot and Margin | `GET /sapi/v1/broker/rebate/recentRecord`         |
| Futures         | `GET /sapi/v1/broker/rebate/futures/recentRecord` |

If a rebate has not appeared after 24 hours, contact your account manager so it can be investigated.

### Why is a rebate missing?

Check in this order:

1. **Timing** — allow for the usual delay of around 30 minutes.
2. **Referral relationship** — confirm the sub-account is correctly linked to your master account.
3. **Eligibility** — confirm the trade qualifies, including VIP level and the period it fell in.
4. If the rebate is still missing after 24 hours, contact your account manager.

### Do travel rule requirements apply to my sub-accounts?

It depends on the Binance entity your sub-account is tagged to. The rules differ per entity, and
your end users' tags are not necessarily the same as your own.

| Entity       | Status                  | What applies to CAAS sub-accounts                                                                                                                                                              |
| ------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AU (AUSTRAC) | Live since 1 July 2026  | A travel rule questionnaire is required for both deposits and withdrawals, with **no minimum threshold** — every transaction triggers it. Transfers between two AU-tagged accounts are exempt. |
| IN (India)   | Live since 22 June 2026 | Travel rule applies to all transactions above a 1,000 USD threshold, for every IN-tagged sub-account.                                                                                          |
| FR, PL       | Live                    | The only EU travel rule entities. Unchanged.                                                                                                                                                   |

### Which withdrawal endpoint should I use for a travel rule entity?

For sub-accounts tagged to a travel rule entity, migrate from `POST /sapi/v1/capital/withdraw/apply`
to `POST /sapi/v1/localentity/withdraw/apply`, which carries the travel rule fields.

For sub-accounts **not** tagged to a travel rule entity, keep using
`POST /sapi/v1/capital/withdraw/apply`. Calling the `localentity` endpoint for a non-travel-rule
entity returns error `103191203 Not supported entity`, which is expected rather than a fault.

### How do I know which entity a sub-account is tagged to?

You cannot infer it from the registration country alone. Please confirm the applicable entity with
your account manager before assuming which travel rule regime and withdrawal endpoint apply.

### Which API key do I use for which call?

The **master account** key for every `/sapi/v1/broker/*` call, and for withdrawals. The
**sub-account** key for trading, retrieving that account's deposit address, and that account's user
data stream.

### Why does my sub-account key not work for Futures?

The Futures wallet was almost certainly not enabled before the key was created. `futuresTrade` is
set at creation time. Enable the wallet, then issue a new key.

### Can CAAS withdraw funds to an external address?

Not directly from a sub-account. A sub-account cannot withdraw. Transfer the funds from the
sub-account to your master account first, then withdraw from the master account with
`POST /sapi/v1/capital/withdraw/apply`. Deposits are the other way round — they can go straight to a
sub-account's own deposit address.

### Which transfer endpoint should I use?

See the comparison table in the
[Integration Guide](/products/caas/integration-guide#7-step-by-step-moving-funds).
`universalTransfer` moves freely between Spot, USD-M and COIN-M; the others are narrower.

### Is there one stream for all my end users?

No. Each account opens its own stream with its own API key. See
[User Data Streams](/products/caas/user-data-streams).

### Can I use revenue share and markup together?

No. They are mutually exclusive — see [Markup](/products/caas/markup/overview).

## KYC SaaS

### What is KYC Status Notification URL?

The `notifyUrl` parameter. Binance sends a `POST` webhook to it whenever a KYC record changes, so
you do not have to poll for every update.

- It is **mandatory** when initiating KYC. If you do not want notifications, pass `"."`.
- If a delivery fails, it is retried at the **3rd, 5th and 10th minute**.
- Verify the signature on every notification before acting on it.

Full request format, response requirements and verification examples are on
[Webhook](/products/kyc-saas/webhook/webhook).

### Can I change the notifyUrl after submitting?

**No.** The `notifyUrl` is bound to the `kycUserId` at submission and there is currently no endpoint
to modify it. Resubmitting after a rejection does **not** reset it either.

Point it at a stable endpoint you control before the first submission. Note the trap: `notifyUrl` is
mandatory and accepts `"."`, so a partner who passes `"."` to get started has no way back to real
webhooks for that `kycUserId`.

### Where can I get BizEntityKey?

Binance issues it to you during onboarding — ask the Link team if you do not have one.

`bizEntityKey` identifies **your entity**, not a customer. There is one per partner, and it is
required in the body of every KYC SaaS request.

### What is entityCustomerId?

**Your own** user ID for the customer, taken from your system. You choose the value and send it to
Binance, which stores it to link your customer record to the KYC record. It is the only identifier
present on every KYC SaaS endpoint.

- **Allowed characters: letters, numbers, and `+`, `-`, `_` and `@` only.** Anything else is
  rejected, so do not pass a raw value from your own system without checking it first.
- Pick something **stable**. You cannot re-key a customer later without unlinking and relinking.
- One `kycUserId` maps to one `entityCustomerId`.

### How many sub-accounts can one customer's KYC cover?

**Up to five.** If one person holds several accounts, link them with
`POST /bapi/ekyc/v2/public/ekyc/customer/add-account-info-list` so the customer only completes KYC
once — the spec states _"One person can link maximum 5 accounts."_

Use `POST /bapi/ekyc/v2/public/ekyc/customer/query-linked-accounts` to see what is linked, and
`POST /bapi/ekyc/v2/public/ekyc/customer/unlink-kyc-data` to unlink.

See [Identifiers](/products/kyc-saas/integration-guide#2-identifiers) for how the IDs relate.

### How to populate the "language" field?

A language code, for example `en`. It controls the language of the KYC page shown to the customer.

Supported values:

```json
{
  "en": "English",
  "ar": "العربية",
  "ar-BH": "العربية (البحرين)",
  "bg": "български",
  "bn": "বাংলা",
  "cs": "Čeština",
  "de": "Deutsch",
  "de-CH": "Deutsch (Schweiz)",
  "en-AU": "English (Australia)",
  "en-BH": "English (Bahrain)",
  "en-GB": "English (Britain)",
  "en-KZ": "English (Kazakhstan)",
  "en-NZ": "English (New Zealand)",
  "es": "Español (Internacional)",
  "es-AR": "Español (Argentina)",
  "es-LA": "Español (Latinoamérica)",
  "fr": "Français",
  "he": "עברית",
  "id": "Bahasa Indonesia",
  "en-IN": "English (India)",
  "it": "Italiano",
  "kk-KZ": "Қазақша (Қазақстан)",
  "ko": "한국어",
  "kz": "Қазақша",
  "lv": "latviešu valoda",
  "ng": "English (Nigeria)",
  "nl": "Nederlands",
  "ph": "Filipino",
  "pl": "Polski",
  "pt": "Português",
  "pt-BR": "Português (Brasil)",
  "pt-PT": "Português (Portugal)",
  "ro": "Română",
  "ru": "Русский",
  "ru-KZ": "Русский (Казахстан)",
  "sv": "svenska",
  "th": "ไทย",
  "tr": "Türkçe",
  "uk-UA": "Українська",
  "vi": "Tiếng Việt",
  "zh-CN": "简体中文",
  "zh-TC": "繁體中文"
}
```

### Can I switch a customer between KYC Sharing and the KYC page?

Only in one direction. The route a KYC record was **originally** created through determines what you
can do with it later:

| Originally created through | Can you switch later?                                          |
| -------------------------- | -------------------------------------------------------------- |
| KYC URL (the KYC page)     | **No.** You cannot use KYC Sharing for it, even after a reset. |
| KYC Sharing                | **Yes.** You can reset it and redo it through the KYC page.    |

So if there is any chance a customer will need the KYC page later, do not start them on the KYC URL
route on the assumption you can move them to Sharing afterwards — that path is one-way.

### Misplaced / Uncredited Deposits?

#### What if my user deposited into a retired wallet address, or into a sub-account that has not completed KYC yet?

Since the implementation of KYC restrictions, newly created sub accounts will not be able to create
an API key and retrieve a deposit address without first completing KYC, hence this scenario would
not be applicable.

For older sub-accounts where users might have saved a copy of the wallet address and did not
complete KYC, the deposit will be rejected. In order to retrieve the deposit, please use the SAPI
asset recovery API to submit an appeal request. If you do not have the SAPI asset recovery API
documentation, please approach our business team or contact our Binance Link team.

Please note that the appeal will be refunded to the source address, and could take up to 30 days to
process. Please manage your user accordingly.

### Overview of Restrictions

#### 1.Service Restrictions

Sub-Account Restrictions

| Services        | Restrictions                                                                      |
| --------------- | --------------------------------------------------------------------------------- |
| Deposits        | Restricted                                                                        |
| Withdrawals     | Allowed, unless otherwise specified                                               |
| Spot Trading    | Restricted. Cannot place new orders and all existing spot orders will be canceled |
| Futures Trading | Restricted. Cannot place new orders, but can reduce existing positions            |
| Margin Trading  | Restricted. Cannot place new orders, but can reduce existing positions            |

#### 2.API Restrictions

Not allowed to create or permission API keys on a non-KYC-ed sub account Common APIs affected:

- POST /sapi/v1/broker/subAccountApi
- POST /sapi/v1/broker/subAccount/futures
- POST /sapi/v1/broker/subAccountApi/permission

Not allowed to receive deposits into a non-KYC-ed sub account Common APIs affected:

- POST /sapi/v1/broker/subAccountApi/permission/universalTransfer
- POST /sapi/v1/broker/transfer
- POST /sapi/v1/broker/transfer/futures
- POST /sapi/v1/broker/universalTransfer

Note:

- Non-KYC-ed Sub account can withdraw to Master account
- Non-KYC-ed Sub account can withdraw to a sub account that is KYC-ed.
- Non-KYC-ed Sub account CANNOT withdraw to another non-KYC-ed sub account
- Master account CANNOT deposit into a non-KYC-ed sub account

---

# FAQ

## Crypto-As-A-Service (CAAS)

### How often are rebates paid out, and how do I check them?

Rebates are credited on an ongoing basis rather than on a fixed payout schedule. The normal delay is
around 30 minutes after the trade.

Query your rebate records with:

| Product         | Endpoint                                          |
| --------------- | ------------------------------------------------- |
| Spot and Margin | `GET /sapi/v1/broker/rebate/recentRecord`         |
| Futures         | `GET /sapi/v1/broker/rebate/futures/recentRecord` |

If a rebate has not appeared after 24 hours, contact your account manager so it can be investigated.

### Why is a rebate missing?

Check in this order:

1. **Timing** — allow for the usual delay of around 30 minutes.
2. **Referral relationship** — confirm the sub-account is correctly linked to your master account.
3. **Eligibility** — confirm the trade qualifies, including VIP level and the period it fell in.
4. If the rebate is still missing after 24 hours, contact your account manager.

### Do travel rule requirements apply to my sub-accounts?

It depends on the Binance entity your sub-account is tagged to. The rules differ per entity, and
your end users' tags are not necessarily the same as your own.

| Entity       | Status                  | What applies to CAAS sub-accounts                                                                                                                                                              |
| ------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AU (AUSTRAC) | Live since 1 July 2026  | A travel rule questionnaire is required for both deposits and withdrawals, with **no minimum threshold** — every transaction triggers it. Transfers between two AU-tagged accounts are exempt. |
| IN (India)   | Live since 22 June 2026 | Travel rule applies to all transactions above a 1,000 USD threshold, for every IN-tagged sub-account.                                                                                          |
| FR, PL       | Live                    | The only EU travel rule entities. Unchanged.                                                                                                                                                   |

### Which withdrawal endpoint should I use for a travel rule entity?

For sub-accounts tagged to a travel rule entity, migrate from `POST /sapi/v1/capital/withdraw/apply`
to `POST /sapi/v1/localentity/withdraw/apply`, which carries the travel rule fields.

For sub-accounts **not** tagged to a travel rule entity, keep using
`POST /sapi/v1/capital/withdraw/apply`. Calling the `localentity` endpoint for a non-travel-rule
entity returns error `103191203 Not supported entity`, which is expected rather than a fault.

### How do I know which entity a sub-account is tagged to?

You cannot infer it from the registration country alone. Please confirm the applicable entity with
your account manager before assuming which travel rule regime and withdrawal endpoint apply.

### Which API key do I use for which call?

The **master account** key for every `/sapi/v1/broker/*` call, and for withdrawals. The
**sub-account** key for trading, retrieving that account's deposit address, and that account's user
data stream.

### Why does my sub-account key not work for Futures?

The Futures wallet was almost certainly not enabled before the key was created. `futuresTrade` is
set at creation time. Enable the wallet, then issue a new key.

### Can CAAS withdraw funds to an external address?

Not directly from a sub-account. A sub-account cannot withdraw. Transfer the funds from the
sub-account to your master account first, then withdraw from the master account with
`POST /sapi/v1/capital/withdraw/apply`. Deposits are the other way round — they can go straight to a
sub-account's own deposit address.

### Which transfer endpoint should I use?

See the comparison table in the
[Integration Guide](/products/caas/integration-guide#7-step-by-step-moving-funds).
`universalTransfer` moves freely between Spot, USD-M and COIN-M; the others are narrower.

### Is there one stream for all my end users?

No. Each account opens its own stream with its own API key. See
[User Data Streams](/products/caas/user-data-streams).

### Can I use revenue share and markup together?

No. They are mutually exclusive — see [Markup](/products/caas/markup/overview).

## KYC SaaS

### What is KYC Status Notification URL?

The `notifyUrl` parameter. Binance sends a `POST` webhook to it whenever a KYC record changes, so
you do not have to poll for every update.

- It is **mandatory** when initiating KYC. If you do not want notifications, pass `"."`.
- If a delivery fails, it is retried at the **3rd, 5th and 10th minute**.
- Verify the signature on every notification before acting on it.

Full request format, response requirements and verification examples are on
[Webhook](/products/kyc-saas/webhook/webhook).

### Can I change the notifyUrl after submitting?

**No.** The `notifyUrl` is bound to the `kycUserId` at submission and there is currently no endpoint
to modify it. Resubmitting after a rejection does **not** reset it either.

Point it at a stable endpoint you control before the first submission. Note the trap: `notifyUrl` is
mandatory and accepts `"."`, so a partner who passes `"."` to get started has no way back to real
webhooks for that `kycUserId`.

### Where can I get BizEntityKey?

Binance issues it to you during onboarding — ask the Link team if you do not have one.

`bizEntityKey` identifies **your entity**, not a customer. There is one per partner, and it is
required in the body of every KYC SaaS request.

### What is entityCustomerId?

**Your own** user ID for the customer, taken from your system. You choose the value and send it to
Binance, which stores it to link your customer record to the KYC record. It is the only identifier
present on every KYC SaaS endpoint.

- **Allowed characters: letters, numbers, and `+`, `-`, `_` and `@` only.** Anything else is
  rejected, so do not pass a raw value from your own system without checking it first.
- Pick something **stable**. You cannot re-key a customer later without unlinking and relinking.
- One `kycUserId` maps to one `entityCustomerId`.

### How many sub-accounts can one customer's KYC cover?

**Up to five.** If one person holds several accounts, link them with
`POST /bapi/ekyc/v2/public/ekyc/customer/add-account-info-list` so the customer only completes KYC
once — the spec states _"One person can link maximum 5 accounts."_

Use `POST /bapi/ekyc/v2/public/ekyc/customer/query-linked-accounts` to see what is linked, and
`POST /bapi/ekyc/v2/public/ekyc/customer/unlink-kyc-data` to unlink.

See [Identifiers](/products/kyc-saas/integration-guide#2-identifiers) for how the IDs relate.

### How to populate the "language" field?

A language code, for example `en`. It controls the language of the KYC page shown to the customer.

Supported values:

```json
{
  "en": "English",
  "ar": "العربية",
  "ar-BH": "العربية (البحرين)",
  "bg": "български",
  "bn": "বাংলা",
  "cs": "Čeština",
  "de": "Deutsch",
  "de-CH": "Deutsch (Schweiz)",
  "en-AU": "English (Australia)",
  "en-BH": "English (Bahrain)",
  "en-GB": "English (Britain)",
  "en-KZ": "English (Kazakhstan)",
  "en-NZ": "English (New Zealand)",
  "es": "Español (Internacional)",
  "es-AR": "Español (Argentina)",
  "es-LA": "Español (Latinoamérica)",
  "fr": "Français",
  "he": "עברית",
  "id": "Bahasa Indonesia",
  "en-IN": "English (India)",
  "it": "Italiano",
  "kk-KZ": "Қазақша (Қазақстан)",
  "ko": "한국어",
  "kz": "Қазақша",
  "lv": "latviešu valoda",
  "ng": "English (Nigeria)",
  "nl": "Nederlands",
  "ph": "Filipino",
  "pl": "Polski",
  "pt": "Português",
  "pt-BR": "Português (Brasil)",
  "pt-PT": "Português (Portugal)",
  "ro": "Română",
  "ru": "Русский",
  "ru-KZ": "Русский (Казахстан)",
  "sv": "svenska",
  "th": "ไทย",
  "tr": "Türkçe",
  "uk-UA": "Українська",
  "vi": "Tiếng Việt",
  "zh-CN": "简体中文",
  "zh-TC": "繁體中文"
}
```

### Can I switch a customer between KYC Sharing and the KYC page?

Only in one direction. The route a KYC record was **originally** created through determines what you
can do with it later:

| Originally created through | Can you switch later?                                          |
| -------------------------- | -------------------------------------------------------------- |
| KYC URL (the KYC page)     | **No.** You cannot use KYC Sharing for it, even after a reset. |
| KYC Sharing                | **Yes.** You can reset it and redo it through the KYC page.    |

So if there is any chance a customer will need the KYC page later, do not start them on the KYC URL
route on the assumption you can move them to Sharing afterwards — that path is one-way.

### Misplaced / Uncredited Deposits?

#### What if my user deposited into a retired wallet address, or into a sub-account that has not completed KYC yet?

Since the implementation of KYC restrictions, newly created sub accounts will not be able to create
an API key and retrieve a deposit address without first completing KYC, hence this scenario would
not be applicable.

For older sub-accounts where users might have saved a copy of the wallet address and did not
complete KYC, the deposit will be rejected. In order to retrieve the deposit, please use the SAPI
asset recovery API to submit an appeal request. If you do not have the SAPI asset recovery API
documentation, please approach our business team or contact our Binance Link team.

Please note that the appeal will be refunded to the source address, and could take up to 30 days to
process. Please manage your user accordingly.

### Overview of Restrictions

#### 1.Service Restrictions

Sub-Account Restrictions

| Services        | Restrictions                                                                      |
| --------------- | --------------------------------------------------------------------------------- |
| Deposits        | Restricted                                                                        |
| Withdrawals     | Allowed, unless otherwise specified                                               |
| Spot Trading    | Restricted. Cannot place new orders and all existing spot orders will be canceled |
| Futures Trading | Restricted. Cannot place new orders, but can reduce existing positions            |
| Margin Trading  | Restricted. Cannot place new orders, but can reduce existing positions            |

#### 2.API Restrictions

Not allowed to create or permission API keys on a non-KYC-ed sub account Common APIs affected:

- POST /sapi/v1/broker/subAccountApi
- POST /sapi/v1/broker/subAccount/futures
- POST /sapi/v1/broker/subAccountApi/permission

Not allowed to receive deposits into a non-KYC-ed sub account Common APIs affected:

- POST /sapi/v1/broker/subAccountApi/permission/universalTransfer
- POST /sapi/v1/broker/transfer
- POST /sapi/v1/broker/transfer/futures
- POST /sapi/v1/broker/universalTransfer

Note:

- Non-KYC-ed Sub account can withdraw to Master account
- Non-KYC-ed Sub account can withdraw to a sub account that is KYC-ed.
- Non-KYC-ed Sub account CANNOT withdraw to another non-KYC-ed sub account
- Master account CANNOT deposit into a non-KYC-ed sub account