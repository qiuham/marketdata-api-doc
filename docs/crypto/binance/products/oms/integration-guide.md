---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/oms/integration-guide
api_type: Guide
updated_at: 2026-11-18 18:29:03.684742
---

# OMS Toolkit — Integration Guideline

> This guideline helps order management system providers integrate OMS Toolkit from scratch. It
> repeats the environment and authentication detail from the
> [Getting Started](/products/oms/basics/1.base-urls) pages so that this page can be followed end to
> end without switching away.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Applying the Tag to an Order](#6-applying-the-tag-to-an-order)
7. [Customer IDs](#7-customer-ids)
8. [Reporting and Analytics](#8-reporting-and-analytics)
9. [Fast API](#9-fast-api)
10. [Error Handling](#10-error-handling)
11. [Readiness Checklist](#11-readiness-checklist)

---

## 1. Before You Begin

### What is OMS Toolkit?

OMS Toolkit is for order management system providers, API trading platforms, bridges, bot trading
platforms, and non-custodial trading providers who connect to Binance as a software service through
their end users' API keys.

It generates custom tags that let you attribute trades to your platform, so you can report on the
activity of users trading through your system.

### Core capabilities

| Capability              | What you get                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------ |
| Trade tagging           | Your client code, prefixed onto each order, attributing that trade to your platform. |
| Per-user labels         | An optional Customer ID, so some reports can be filtered by individual user.         |
| New-user checks         | Whether a given user is new to Binance.                                              |
| Reporting               | Trade volume, rebate volume, trader counts and income, read back per tag.            |
| [Fast API](#9-fast-api) | Create an API key for a user through OAuth, without them leaving your app.           |

---

## 2. Onboarding Checklist

### Items you provide to Binance

- **Completed entity verification (KYB)** on your Binance account. This is required for the OMS
  Toolkit account itself, whether or not you go on to use Fast API.
- Which product families you need — Spot, USD-M Futures, COIN-M Futures, Portfolio Margin.

[Fast API](#9-fast-api) is a **separate onboarding on top of the above**, and it carries its own
**second KYB review** — **Entity KYB** and **OAuth Security KYB** — applied for through the Binance
Developer Center, plus a 60×60 logo and a callback URL. You can run OMS Toolkit without Fast API;
trade tagging needs only the account KYB above.

### Items Binance provides to you

- Partner permissions on your own Binance account, which its API key then carries.
- Your **client codes** — one for Spot and a separate one for Futures. These are the values you put
  in the `x-` prefix on every order, so keep them straight: a spot code on a futures order does not
  attribute. See [section 6](#6-applying-the-tag-to-an-order).
- For Fast API: your **Client ID** and **Client Secret**, sent by email.

<!-- TODO(sulyn): confirm this checklist against the actual onboarding process. Derived from what
     the API and the Fast API onboarding steps require, not from an onboarding runbook. -->

---

## 3. Environment Setup

### Base URLs

| Product family          | Base endpoint                             | Endpoint prefix          |
| ----------------------- | ----------------------------------------- | ------------------------ |
| Spot                    | **https://api.binance.com**               | `/sapi/v1/apiReferral/*` |
| USD-M Futures           | **https://fapi.binance.com**              | `/fapi/v1/apiReferral/*` |
| COIN-M Futures          | **https://fapi.binance.com**              | `/fapi/v1/apiReferral/*` |
| Portfolio Margin        | **https://papi.binance.com**              | `/papi/v1/apiReferral/*` |
| [Fast API](#9-fast-api) | **https://www.binanceapis.com/oauth-api** | `/v1/api-key/*`          |

**COIN-M Futures has no separate base endpoint.** It is served by the same `/fapi/v1/apiReferral/*`
endpoints as USD-M, selected with the `type` query parameter — `1` for USD-M (the default) and `2`
for COIN-M. `dapi.binance.com` exposes no `apiReferral` paths.

The `type` parameter is accepted by `overview`, `tradeVol`, `rebateVol`, `traderNum`,
`traderSummary` and `ifNewUser`. Any value other than `1` or `2` is rejected with `-1102`. Because
the same endpoint, API key and partner code serve both, a partner enabled for USD-M reporting reads
COIN-M through the same call with no additional setup.

### Required HTTP headers

| Header         | Value                               | When                        |
| -------------- | ----------------------------------- | --------------------------- |
| `X-MBX-APIKEY` | Your API key                        | Every `apiReferral` request |
| `Content-Type` | `application/x-www-form-urlencoded` | `POST` requests with a body |

Fast API does not use `X-MBX-APIKEY` — see [section 9](#9-fast-api).

---

## 4. Authentication & Request Signing

Every `apiReferral` endpoint is `USER_DATA`, so all of them are signed. There are no public OMS
Toolkit endpoints.

1. Build the request parameter string, including `timestamp` (Unix milliseconds).
2. Optionally include `recvWindow`.
3. Sign the parameter string with your secret key.
4. Append the result as a `signature` parameter.
5. Send the API key in the `X-MBX-APIKEY` header.

:::warning

**Sign the exact string you send.** Re-ordering or re-encoding parameters after signing invalidates
the signature. A space must be encoded as `%20`, not `+`.

:::

Fast API is different — it is OAuth on a separate host, with a Client ID and Client Secret rather
than an API key and signature. See [section 9](#9-fast-api).

---

## 5. Quick Integration Path

1. Confirm your partner permissions are active and your API key authenticates.
2. Add the `x-` client-code prefix to every order your platform places — see
   [section 6](#6-applying-the-tag-to-an-order). Nothing is attributed to you without it.
3. Have a user trade, then confirm the activity appears in the
   [reporting endpoints](#8-reporting-and-analytics).
4. Optionally, set a Customer ID per user so you can filter some of those reports by individual user
   — see [section 7](#7-customer-ids).
5. Reconcile the reporting endpoints against your own records.
6. Add [Fast API](#9-fast-api) if you want to issue API keys from inside your own app.

---

## 6. Applying the Tag to an Order

Trade attribution happens at order placement, as a prefix on the `clientOrderId`. **This is what
attribution is.** If the prefix is missing, the order is not yours as far as Binance is concerned,
and nothing in [section 8](#8-reporting-and-analytics) will show it.

Orders are placed from the **end user's own account**, so this is something your platform must do on
their behalf as part of normal Spot and Futures order placement.

### Format

`x-` followed by your client code, followed by anything you choose.

If your client code is `a1B2c3D4`, all of these are valid:

```
x-a1B2c3D4user1order1
x-a1B2c3D4_user1-order1
x-a1B2c3D4myOwnIdentifier
```

The portion after the client code is yours to use — put your own order or user identifier there.
`clientOrderId` must be unique per order, so the value cannot be the bare tag repeated.

### Rules

- **Required on every order.** An order sent without the prefix is not attributed to you and will
  not appear in your reporting.
- **Spot and Futures have separate client codes.** You are issued one per product family, and each
  must be used on that product's orders. A spot code on a futures order does not work.
- **The tag is applied at order placement**, from the end user's account — not from your partner
  account.

---

## 7. Customer IDs

A Customer ID is **your own optional label for an individual user**. It affects nothing about
attribution — that is entirely the `x-` prefix in [section 6](#6-applying-the-tag-to-an-order). What
it buys you is the ability to look a single user up, through the API and in the OMS dashboard,
instead of only seeing partner-wide totals.

:::warning

**Three identifiers have similar names and are not interchangeable.**

| Identifier      | What it is                                      | Who sets it | Where it appears                                                    |
| --------------- | ----------------------------------------------- | ----------- | ------------------------------------------------------------------- |
| **Customer ID** | Your label for one end user                     | **You**     | `userCustomization` request; the `customerId` report filter         |
| **Client code** | Your partner code, identifying _you_ to Binance | Binance     | The `x-` order prefix; `apiAgentCode` (spot) / `brokerId` (futures) |
| **Client ID**   | Your [Fast API](#9-fast-api) OAuth credential   | Binance     | Fast API only — emailed with a Client Secret. Unrelated to tagging. |

A Customer ID is a value you invent; a client code and a Client ID are both issued to you.

:::

**Only `traderSummary` and spot `rebate/recentRecord` accept a `customerId` filter.** `tradeVol`,
`rebateVol`, `traderNum`, `overview` and `income` are partner-wide, so a Customer ID cannot break
those down by user.

### Setting one

The calls are all under `apiReferral`. Use the `/sapi/v1/` prefix for Spot, `/fapi/v1/` for USD-M
Futures and `/papi/v1/` for Portfolio Margin:

| Purpose                       | Method | Path                |
| ----------------------------- | ------ | ------------------- |
| Check whether the user is new | `GET`  | `ifNewUser`         |
| Set the Customer ID           | `POST` | `userCustomization` |
| Read it back to confirm       | `GET`  | `userCustomization` |

On `fapi` and `papi`, `ifNewUser` also takes `type` — `1` for USD-M (the default), `2` for COIN-M.

Two rules that catch people out:

- **It is per product family.** A user who trades spot and USD-M futures needs it set on both.
- **Each set call also carries your client code**, as `apiAgentCode` on spot and `brokerId` on USD-M
  futures. Same value as the `x-` prefix; only the parameter name differs.

### Partner-level vs user-level

`userCustomization` labels a single end user and exists on Spot, USD-M and PAPI. A second
partner-level surface, `customization`, looks users up **by email** and exists on **Spot and USD-M
only** — see the [API Reference](/catalog/vip-and-institutional-oms/api/rest-api) for its endpoints.

:::note

**Portfolio Margin has no partner-level `customization` endpoint.** If your tagging logic assumes it
exists everywhere, it will fail on PAPI.

:::

### Which family to call — it depends on the API key you hold

The two families are not alternatives you pick on preference. **`customization` is called with your
own broker API key; `userCustomization` is called with the end user's API key.** That is the whole
distinction, and it decides which one you can use.

|                         | With **your broker API key** — `customization`                                                                  | With the **user's API key** — `userCustomization`                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Set** a customer ID   | Spot: `POST /sapi/v1/apiReferral/customization` (by email)<br/>USD-M: `POST /fapi/v1/apiReferral/customization` | Spot: `POST /sapi/v1/apiReferral/userCustomization`<br/>USD-M: `POST /fapi/v1/apiReferral/userCustomization`<br/>PM: `POST /papi/v1/apiReferral/userCustomization` |
| **Query** a customer ID | Spot: `GET /sapi/v1/apiReferral/customization`<br/>USD-M: `GET /fapi/v1/apiReferral/customization`              | Spot: `GET /sapi/v1/apiReferral/userCustomization`<br/>USD-M: `GET /fapi/v1/apiReferral/userCustomization`<br/>PM: `GET /papi/v1/apiReferral/userCustomization`    |

So in practice:

- **You hold the broker key and want to label a user you know by email** — use `customization`. This
  is the usual case for a provider administering its own users.
- **You are acting with a user's own API key** — use `userCustomization`, and note it is the
  **only** family that covers Portfolio Margin.

In the API Reference the broker-key variants are the ones titled **"Partner Customize Id For …"**.

---

## 8. Reporting and Analytics

### Spot

| Endpoint                                         | Returns                      |
| ------------------------------------------------ | ---------------------------- |
| `GET /sapi/v1/apiReferral/rebate/recentRecord`   | Partner rebate recent record |
| `GET /sapi/v1/apiReferral/kickback/recentRecord` | Rebate recent record         |

Only `traderSummary` and the spot `rebate/recentRecord` accept a `customerId` filter — see
[section 7](#7-customer-ids). Everything else on this page is partner-wide.

### USD-M and COIN-M Futures

| Endpoint                                 | Returns              | `type` |
| ---------------------------------------- | -------------------- | ------ |
| `GET /fapi/v1/apiReferral/overview`      | Rebate data overview | yes    |
| `GET /fapi/v1/apiReferral/tradeVol`      | User trade volume    | yes    |
| `GET /fapi/v1/apiReferral/rebateVol`     | Rebate volume        | yes    |
| `GET /fapi/v1/apiReferral/traderNum`     | Trader number        | yes    |
| `GET /fapi/v1/apiReferral/traderSummary` | Trader detail        | yes    |
| `GET /fapi/v1/income`                    | Income history       | no     |

:::note

**One endpoint set covers both futures products.** Pass `type=1` for USD-M (the default) or `type=2`
for COIN-M. There is no `/dapi/v1/apiReferral/*` family — see
[Environment Setup](#3-environment-setup).

The exception is income history, which is a plain futures endpoint rather than an `apiReferral` one
and has no `type` parameter. Read COIN-M income from `GET /dapi/v1/income` instead.

:::

**Reporting is asymmetric.** Futures has the fullest set of reporting endpoints, Spot has fewer, and
Portfolio Margin has none. Do not assume a metric available for futures has a spot or PAPI
equivalent.

Tagged activity is delivered over these REST endpoints and the OMS dashboard. OMS Toolkit does
**not** push tagged activity over a user data stream.

---

## 9. Fast API

Fast API lets you create a Binance API key for a user through OAuth, so they do not have to leave
your application to generate one.

It is a separate integration: a different host, OAuth instead of request signing, and its own
onboarding.

| Endpoint                      | Purpose                      |
| ----------------------------- | ---------------------------- |
| `POST /v1/api-key/create`     | Create an API key for a user |
| `GET /v1/api-key/user-status` | Get that user's status       |

### Onboarding

1. Log in to the Binance Developer Center with a verified entity (enterprise) account.
2. Apply for **Entity KYB** and **OAuth Security KYB**.
3. Once both pass, create a **Client ID**, upload a 60×60 logo, and set your **callback URL**.
   Binance emails your Client ID and Client Secret.
4. Download the SDK for the pop-up dialogues.
5. Apply for the OAuth scopes you need.

### Minimum scopes

- `account:status`
- `create:apikey` — spot, margin and futures trading permission. Alternatively
  `create:apikey:margin` for margin loan, repay and transfer, or `create:apikey:options` for
  European Options.
- `user:openId`

:::warning

Never share your **Client Secret**.

:::

Full onboarding steps, remarks and error codes are on [Fast-API](/products/oms/Fast-API/overview).

---

## 10. Error Handling

Errors use the standard Binance envelope:

```json
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

| Status | Meaning                                                                        |
| ------ | ------------------------------------------------------------------------------ |
| `4XX`  | Malformed request; the issue is on the sender's side.                          |
| `429`  | Rate limit breached. Back off rather than continuing to send.                  |
| `418`  | IP auto-banned after continuing to send following `429`s.                      |
| `5XX`  | Internal error. Execution status is **UNKNOWN** — query state before retrying. |

Fast API has its own error codes — see [Fast-API](/products/oms/Fast-API/overview).

Full detail on limits is in [Rate limits](/products/oms/basics/4.rate-limits).

---

## 11. Readiness Checklist

**OMS Toolkit has no separate test environment** — you verify against production. Work through this
with a small number of real users and minimal order sizes before onboarding at volume.

#### Authentication

- [ ] Partner API key authenticates against a signed `apiReferral` call.
- [ ] Signature verified against a request containing a space or special character.

#### Tagging

- [ ] Customer ID set and read back for **each** product family the user trades.
- [ ] A user trading both spot and USD-M is tagged on both, not one.
- [ ] PAPI path exercised without relying on a partner-level `customization` call.

#### Reporting

- [ ] Reporting endpoints return the tag you set.
- [ ] Figures reconcile against your own records.

#### Fast API

- [ ] OAuth flow completes and returns a usable API key.
- [ ] Requested scopes cover the trading the user will actually do.

---

# OMS Toolkit — Integration Guideline

> This guideline helps order management system providers integrate OMS Toolkit from scratch. It
> repeats the environment and authentication detail from the
> [Getting Started](/products/oms/basics/1.base-urls) pages so that this page can be followed end to
> end without switching away.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Applying the Tag to an Order](#6-applying-the-tag-to-an-order)
7. [Customer IDs](#7-customer-ids)
8. [Reporting and Analytics](#8-reporting-and-analytics)
9. [Fast API](#9-fast-api)
10. [Error Handling](#10-error-handling)
11. [Readiness Checklist](#11-readiness-checklist)

---

## 1. Before You Begin

### What is OMS Toolkit?

OMS Toolkit is for order management system providers, API trading platforms, bridges, bot trading
platforms, and non-custodial trading providers who connect to Binance as a software service through
their end users' API keys.

It generates custom tags that let you attribute trades to your platform, so you can report on the
activity of users trading through your system.

### Core capabilities

| Capability              | What you get                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------ |
| Trade tagging           | Your client code, prefixed onto each order, attributing that trade to your platform. |
| Per-user labels         | An optional Customer ID, so some reports can be filtered by individual user.         |
| New-user checks         | Whether a given user is new to Binance.                                              |
| Reporting               | Trade volume, rebate volume, trader counts and income, read back per tag.            |
| [Fast API](#9-fast-api) | Create an API key for a user through OAuth, without them leaving your app.           |

---

## 2. Onboarding Checklist

### Items you provide to Binance

- **Completed entity verification (KYB)** on your Binance account. This is required for the OMS
  Toolkit account itself, whether or not you go on to use Fast API.
- Which product families you need — Spot, USD-M Futures, COIN-M Futures, Portfolio Margin.

[Fast API](#9-fast-api) is a **separate onboarding on top of the above**, and it carries its own
**second KYB review** — **Entity KYB** and **OAuth Security KYB** — applied for through the Binance
Developer Center, plus a 60×60 logo and a callback URL. You can run OMS Toolkit without Fast API;
trade tagging needs only the account KYB above.

### Items Binance provides to you

- Partner permissions on your own Binance account, which its API key then carries.
- Your **client codes** — one for Spot and a separate one for Futures. These are the values you put
  in the `x-` prefix on every order, so keep them straight: a spot code on a futures order does not
  attribute. See [section 6](#6-applying-the-tag-to-an-order).
- For Fast API: your **Client ID** and **Client Secret**, sent by email.

<!-- TODO(sulyn): confirm this checklist against the actual onboarding process. Derived from what
     the API and the Fast API onboarding steps require, not from an onboarding runbook. -->

---

## 3. Environment Setup

### Base URLs

| Product family          | Base endpoint                             | Endpoint prefix          |
| ----------------------- | ----------------------------------------- | ------------------------ |
| Spot                    | **https://api.binance.com**               | `/sapi/v1/apiReferral/*` |
| USD-M Futures           | **https://fapi.binance.com**              | `/fapi/v1/apiReferral/*` |
| COIN-M Futures          | **https://fapi.binance.com**              | `/fapi/v1/apiReferral/*` |
| Portfolio Margin        | **https://papi.binance.com**              | `/papi/v1/apiReferral/*` |
| [Fast API](#9-fast-api) | **https://www.binanceapis.com/oauth-api** | `/v1/api-key/*`          |

**COIN-M Futures has no separate base endpoint.** It is served by the same `/fapi/v1/apiReferral/*`
endpoints as USD-M, selected with the `type` query parameter — `1` for USD-M (the default) and `2`
for COIN-M. `dapi.binance.com` exposes no `apiReferral` paths.

The `type` parameter is accepted by `overview`, `tradeVol`, `rebateVol`, `traderNum`,
`traderSummary` and `ifNewUser`. Any value other than `1` or `2` is rejected with `-1102`. Because
the same endpoint, API key and partner code serve both, a partner enabled for USD-M reporting reads
COIN-M through the same call with no additional setup.

### Required HTTP headers

| Header         | Value                               | When                        |
| -------------- | ----------------------------------- | --------------------------- |
| `X-MBX-APIKEY` | Your API key                        | Every `apiReferral` request |
| `Content-Type` | `application/x-www-form-urlencoded` | `POST` requests with a body |

Fast API does not use `X-MBX-APIKEY` — see [section 9](#9-fast-api).

---

## 4. Authentication & Request Signing

Every `apiReferral` endpoint is `USER_DATA`, so all of them are signed. There are no public OMS
Toolkit endpoints.

1. Build the request parameter string, including `timestamp` (Unix milliseconds).
2. Optionally include `recvWindow`.
3. Sign the parameter string with your secret key.
4. Append the result as a `signature` parameter.
5. Send the API key in the `X-MBX-APIKEY` header.

:::warning

**Sign the exact string you send.** Re-ordering or re-encoding parameters after signing invalidates
the signature. A space must be encoded as `%20`, not `+`.

:::

Fast API is different — it is OAuth on a separate host, with a Client ID and Client Secret rather
than an API key and signature. See [section 9](#9-fast-api).

---

## 5. Quick Integration Path

1. Confirm your partner permissions are active and your API key authenticates.
2. Add the `x-` client-code prefix to every order your platform places — see
   [section 6](#6-applying-the-tag-to-an-order). Nothing is attributed to you without it.
3. Have a user trade, then confirm the activity appears in the
   [reporting endpoints](#8-reporting-and-analytics).
4. Optionally, set a Customer ID per user so you can filter some of those reports by individual user
   — see [section 7](#7-customer-ids).
5. Reconcile the reporting endpoints against your own records.
6. Add [Fast API](#9-fast-api) if you want to issue API keys from inside your own app.

---

## 6. Applying the Tag to an Order

Trade attribution happens at order placement, as a prefix on the `clientOrderId`. **This is what
attribution is.** If the prefix is missing, the order is not yours as far as Binance is concerned,
and nothing in [section 8](#8-reporting-and-analytics) will show it.

Orders are placed from the **end user's own account**, so this is something your platform must do on
their behalf as part of normal Spot and Futures order placement.

### Format

`x-` followed by your client code, followed by anything you choose.

If your client code is `a1B2c3D4`, all of these are valid:

```
x-a1B2c3D4user1order1
x-a1B2c3D4_user1-order1
x-a1B2c3D4myOwnIdentifier
```

The portion after the client code is yours to use — put your own order or user identifier there.
`clientOrderId` must be unique per order, so the value cannot be the bare tag repeated.

### Rules

- **Required on every order.** An order sent without the prefix is not attributed to you and will
  not appear in your reporting.
- **Spot and Futures have separate client codes.** You are issued one per product family, and each
  must be used on that product's orders. A spot code on a futures order does not work.
- **The tag is applied at order placement**, from the end user's account — not from your partner
  account.

---

## 7. Customer IDs

A Customer ID is **your own optional label for an individual user**. It affects nothing about
attribution — that is entirely the `x-` prefix in [section 6](#6-applying-the-tag-to-an-order). What
it buys you is the ability to look a single user up, through the API and in the OMS dashboard,
instead of only seeing partner-wide totals.

:::warning

**Three identifiers have similar names and are not interchangeable.**

| Identifier      | What it is                                      | Who sets it | Where it appears                                                    |
| --------------- | ----------------------------------------------- | ----------- | ------------------------------------------------------------------- |
| **Customer ID** | Your label for one end user                     | **You**     | `userCustomization` request; the `customerId` report filter         |
| **Client code** | Your partner code, identifying _you_ to Binance | Binance     | The `x-` order prefix; `apiAgentCode` (spot) / `brokerId` (futures) |
| **Client ID**   | Your [Fast API](#9-fast-api) OAuth credential   | Binance     | Fast API only — emailed with a Client Secret. Unrelated to tagging. |

A Customer ID is a value you invent; a client code and a Client ID are both issued to you.

:::

**Only `traderSummary` and spot `rebate/recentRecord` accept a `customerId` filter.** `tradeVol`,
`rebateVol`, `traderNum`, `overview` and `income` are partner-wide, so a Customer ID cannot break
those down by user.

### Setting one

The calls are all under `apiReferral`. Use the `/sapi/v1/` prefix for Spot, `/fapi/v1/` for USD-M
Futures and `/papi/v1/` for Portfolio Margin:

| Purpose                       | Method | Path                |
| ----------------------------- | ------ | ------------------- |
| Check whether the user is new | `GET`  | `ifNewUser`         |
| Set the Customer ID           | `POST` | `userCustomization` |
| Read it back to confirm       | `GET`  | `userCustomization` |

On `fapi` and `papi`, `ifNewUser` also takes `type` — `1` for USD-M (the default), `2` for COIN-M.

Two rules that catch people out:

- **It is per product family.** A user who trades spot and USD-M futures needs it set on both.
- **Each set call also carries your client code**, as `apiAgentCode` on spot and `brokerId` on USD-M
  futures. Same value as the `x-` prefix; only the parameter name differs.

### Partner-level vs user-level

`userCustomization` labels a single end user and exists on Spot, USD-M and PAPI. A second
partner-level surface, `customization`, looks users up **by email** and exists on **Spot and USD-M
only** — see the [API Reference](/catalog/vip-and-institutional-oms/api/rest-api) for its endpoints.

:::note

**Portfolio Margin has no partner-level `customization` endpoint.** If your tagging logic assumes it
exists everywhere, it will fail on PAPI.

:::

### Which family to call — it depends on the API key you hold

The two families are not alternatives you pick on preference. **`customization` is called with your
own broker API key; `userCustomization` is called with the end user's API key.** That is the whole
distinction, and it decides which one you can use.

|                         | With **your broker API key** — `customization`                                                                  | With the **user's API key** — `userCustomization`                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Set** a customer ID   | Spot: `POST /sapi/v1/apiReferral/customization` (by email)<br/>USD-M: `POST /fapi/v1/apiReferral/customization` | Spot: `POST /sapi/v1/apiReferral/userCustomization`<br/>USD-M: `POST /fapi/v1/apiReferral/userCustomization`<br/>PM: `POST /papi/v1/apiReferral/userCustomization` |
| **Query** a customer ID | Spot: `GET /sapi/v1/apiReferral/customization`<br/>USD-M: `GET /fapi/v1/apiReferral/customization`              | Spot: `GET /sapi/v1/apiReferral/userCustomization`<br/>USD-M: `GET /fapi/v1/apiReferral/userCustomization`<br/>PM: `GET /papi/v1/apiReferral/userCustomization`    |

So in practice:

- **You hold the broker key and want to label a user you know by email** — use `customization`. This
  is the usual case for a provider administering its own users.
- **You are acting with a user's own API key** — use `userCustomization`, and note it is the
  **only** family that covers Portfolio Margin.

In the API Reference the broker-key variants are the ones titled **"Partner Customize Id For …"**.

---

## 8. Reporting and Analytics

### Spot

| Endpoint                                         | Returns                      |
| ------------------------------------------------ | ---------------------------- |
| `GET /sapi/v1/apiReferral/rebate/recentRecord`   | Partner rebate recent record |
| `GET /sapi/v1/apiReferral/kickback/recentRecord` | Rebate recent record         |

Only `traderSummary` and the spot `rebate/recentRecord` accept a `customerId` filter — see
[section 7](#7-customer-ids). Everything else on this page is partner-wide.

### USD-M and COIN-M Futures

| Endpoint                                 | Returns              | `type` |
| ---------------------------------------- | -------------------- | ------ |
| `GET /fapi/v1/apiReferral/overview`      | Rebate data overview | yes    |
| `GET /fapi/v1/apiReferral/tradeVol`      | User trade volume    | yes    |
| `GET /fapi/v1/apiReferral/rebateVol`     | Rebate volume        | yes    |
| `GET /fapi/v1/apiReferral/traderNum`     | Trader number        | yes    |
| `GET /fapi/v1/apiReferral/traderSummary` | Trader detail        | yes    |
| `GET /fapi/v1/income`                    | Income history       | no     |

:::note

**One endpoint set covers both futures products.** Pass `type=1` for USD-M (the default) or `type=2`
for COIN-M. There is no `/dapi/v1/apiReferral/*` family — see
[Environment Setup](#3-environment-setup).

The exception is income history, which is a plain futures endpoint rather than an `apiReferral` one
and has no `type` parameter. Read COIN-M income from `GET /dapi/v1/income` instead.

:::

**Reporting is asymmetric.** Futures has the fullest set of reporting endpoints, Spot has fewer, and
Portfolio Margin has none. Do not assume a metric available for futures has a spot or PAPI
equivalent.

Tagged activity is delivered over these REST endpoints and the OMS dashboard. OMS Toolkit does
**not** push tagged activity over a user data stream.

---

## 9. Fast API

Fast API lets you create a Binance API key for a user through OAuth, so they do not have to leave
your application to generate one.

It is a separate integration: a different host, OAuth instead of request signing, and its own
onboarding.

| Endpoint                      | Purpose                      |
| ----------------------------- | ---------------------------- |
| `POST /v1/api-key/create`     | Create an API key for a user |
| `GET /v1/api-key/user-status` | Get that user's status       |

### Onboarding

1. Log in to the Binance Developer Center with a verified entity (enterprise) account.
2. Apply for **Entity KYB** and **OAuth Security KYB**.
3. Once both pass, create a **Client ID**, upload a 60×60 logo, and set your **callback URL**.
   Binance emails your Client ID and Client Secret.
4. Download the SDK for the pop-up dialogues.
5. Apply for the OAuth scopes you need.

### Minimum scopes

- `account:status`
- `create:apikey` — spot, margin and futures trading permission. Alternatively
  `create:apikey:margin` for margin loan, repay and transfer, or `create:apikey:options` for
  European Options.
- `user:openId`

:::warning

Never share your **Client Secret**.

:::

Full onboarding steps, remarks and error codes are on [Fast-API](/products/oms/Fast-API/overview).

---

## 10. Error Handling

Errors use the standard Binance envelope:

```json
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

| Status | Meaning                                                                        |
| ------ | ------------------------------------------------------------------------------ |
| `4XX`  | Malformed request; the issue is on the sender's side.                          |
| `429`  | Rate limit breached. Back off rather than continuing to send.                  |
| `418`  | IP auto-banned after continuing to send following `429`s.                      |
| `5XX`  | Internal error. Execution status is **UNKNOWN** — query state before retrying. |

Fast API has its own error codes — see [Fast-API](/products/oms/Fast-API/overview).

Full detail on limits is in [Rate limits](/products/oms/basics/4.rate-limits).

---

## 11. Readiness Checklist

**OMS Toolkit has no separate test environment** — you verify against production. Work through this
with a small number of real users and minimal order sizes before onboarding at volume.

#### Authentication

- [ ] Partner API key authenticates against a signed `apiReferral` call.
- [ ] Signature verified against a request containing a space or special character.

#### Tagging

- [ ] Customer ID set and read back for **each** product family the user trades.
- [ ] A user trading both spot and USD-M is tagged on both, not one.
- [ ] PAPI path exercised without relying on a partner-level `customization` call.

#### Reporting

- [ ] Reporting endpoints return the tag you set.
- [ ] Figures reconcile against your own records.

#### Fast API

- [ ] OAuth flow completes and returns a usable API key.
- [ ] Requested scopes cover the trading the user will actually do.