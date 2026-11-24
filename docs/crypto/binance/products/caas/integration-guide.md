---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/integration-guide
api_type: Guide
updated_at: 2026-11-24 18:33:12.896829
---

# Crypto-As-A-Service — Integration Guideline

> This guideline helps partners integrate Crypto-As-A-Service (CAAS) from scratch. Follow the steps
> below to go from zero to live. It repeats the environment and authentication detail from
> [Getting Started](/products/caas/getting-started) and the
> [API basics](/products/caas/basics/1.base-urls) so that this page can be followed end to end
> without switching away.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Step-by-Step: End-User Onboarding](#6-step-by-step-end-user-onboarding)
7. [Step-by-Step: Moving Funds](#7-step-by-step-moving-funds)
8. [Deposits and Withdrawals](#8-deposits-and-withdrawals)
9. [Commission Configuration](#9-commission-configuration)
10. [User Data Streams](#10-user-data-streams)
11. [Error Handling](#11-error-handling)
12. [Readiness Checklist](#12-readiness-checklist)
13. [Best Practices](#13-best-practices)
14. [FAQ](#14-faq)

---

## 1. Before You Begin

### What is CAAS?

Crypto-As-A-Service lets a platform offer crypto functionality to its users without building an
exchange, custody, wallet, trading, or settlement stack. Your application connects to Binance from
your own backend; you build the front end, and Binance provides the account, custody, and execution
layer.

### Core capabilities

| Capability               | What you get                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| Sub-account management   | One Binance account per end user, created and controlled through your master account.     |
| Per-user API credentials | An API key scoped to a single sub-account, with configurable permissions and IP controls. |
| Asset movement           | Transfers between your master account and its sub-accounts across spot, margin, futures.  |
| Commission               | Set and query the commission you earn on each sub-account's spot and futures activity.    |
| Optional modules         | KYC SaaS, Markup, and the Institutional Crypto Buy/Sell Solution.                         |

### Architecture

CAAS is a server-to-server integration. There is no Binance-hosted interface for your end users.

```
Your front end  ──►  Your backend  ──►  CAAS API (/sapi/v1/broker/*)
                          │                    master account API key
                          └────────────►  Trading APIs (/api, /fapi, /dapi)
                                               sub-account API key
```

Two credentials do different jobs, and mixing them is the most common integration mistake:

| Credential             | Used for                                                                 |
| ---------------------- | ------------------------------------------------------------------------ |
| Master account API key | Every `/sapi/v1/broker/*` call — account creation, transfers, commission |
| Sub-account API key    | Trading and wallet operations **on behalf of that one end user**         |

---

## 2. Onboarding Checklist

### Items you provide to Binance

- Your institutional entity details and completed onboarding.
- The commercial model you want — revenue share or [Markup](/products/caas/markup/overview).
- Which modules you need enabled: KYC SaaS, Markup, Institutional Crypto Buy/Sell Solution.

### Items Binance provides to you

- The CAAS permission on your master account.
- Confirmation of which products your sub-accounts may be enabled for.

You create your own master account API key and secret in the Binance interface; Binance does not
issue them to you.

:::note

CAAS itself does not require you to register your calling IP addresses with Binance. IP allowlisting
at onboarding applies to [KYC SaaS](/products/kyc-saas/overview) and the
[Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) only. You
can still restrict the sub-account API keys you create — see
[section 6](#6-step-by-step-end-user-onboarding).

:::

<!-- TODO(sulyn): confirm this checklist against the actual onboarding process. The lists above are
     derived from what the API requires, not from an onboarding runbook. -->

---

## 3. Environment Setup

### Base URLs

| Endpoint family | Used for                                              | Base endpoint                |
| --------------- | ----------------------------------------------------- | ---------------------------- |
| `/sapi/*`       | CAAS, OMS Toolkit, and other wallet/account functions | **https://api.binance.com**  |
| `/api/*`        | Spot trading                                          | **https://api.binance.com**  |
| `/fapi/*`       | USD-M Futures                                         | **https://fapi.binance.com** |
| `/dapi/*`       | COIN-M Futures                                        | **https://dapi.binance.com** |

For `/api/*` and `/sapi/*`, the alternates **https://api-gcp.binance.com** and
**https://api1.binance.com** through **https://api4.binance.com** are also available. Performance
between them may vary; if one is slow, try another.

### Required HTTP headers

| Header         | Value                               | When                                |
| -------------- | ----------------------------------- | ----------------------------------- |
| `X-MBX-APIKEY` | Your API key                        | Every CAAS request                  |
| `Content-Type` | `application/x-www-form-urlencoded` | `POST`, `PUT`, `DELETE` with a body |

### Parameter rules

- For `GET` endpoints, parameters must be sent as a `query string`.
- For `POST`, `PUT`, and `DELETE`, parameters may be sent as a `query string` or in the
  `request body`. You may mix both.
- If the same parameter appears in both, the `query string` value is used.
- Parameters may be sent in any order.
- Email addresses must be URL-encoded and lower case — `alice@test.com` becomes `alice%40test.com`.

---

## 4. Authentication & Request Signing

Every CAAS endpoint is `SIGNED`; there are no public CAAS endpoints. Most of them sit under
`/sapi/v1/broker/*`. This applies to the CAAS API only, not to Binance endpoints in general.

### Security types

| Security Type | Description                                              |
| ------------- | -------------------------------------------------------- |
| TRADE         | Endpoint requires sending a valid API-Key and signature. |
| USER_DATA     | Endpoint requires sending a valid API-Key and signature. |

- API keys are passed via the `X-MBX-APIKEY` header.
- API keys and secret keys **are case sensitive**.
- A key can be restricted to certain endpoint types. By default it can access all secure routes.

### Step-by-step signing

1. Build the request parameter string, including `timestamp` (Unix milliseconds).
2. Optionally include `recvWindow` — the request is rejected if it arrives more than `recvWindow`
   milliseconds after `timestamp`.
3. Sign the parameter string with your secret key.
4. Append the result as a `signature` parameter.
5. Send the API key in the `X-MBX-APIKEY` header.

:::warning

**Sign the exact string you send.** Re-ordering or re-encoding parameters after signing invalidates
the signature. A space must be encoded as `%20`, not `+`.

:::

### Key types

Sub-account API keys support asymmetric key types. `POST /sapi/v1/broker/subAccountApi` accepts a
`publicKey` parameter for **Ed25519 and RSA** keys; omit it for an HMAC key.

### Worked example

Both examples below sign a real request to `GET /sapi/v1/broker/subAccount` with an HMAC key, using
only the standard library. Read your key and secret from the environment rather than hardcoding
them.

```python
import hashlib, hmac, os, time, urllib.parse, urllib.request

API_KEY = os.environ["BINANCE_API_KEY"]
API_SECRET = os.environ["BINANCE_API_SECRET"]
BASE_URL = "https://api.binance.com"


def signed_get(path, params=None):
    params = dict(params or {})
    params["recvWindow"] = 5000
    params["timestamp"] = int(time.time() * 1000)
    # quote_via=quote encodes a space as %20, not '+'
    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    signature = hmac.new(
        API_SECRET.encode("utf-8"), query.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    url = f"{BASE_URL}{path}?{query}&signature={signature}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req) as resp:
        return resp.status, resp.read().decode("utf-8")


print(signed_get("/sapi/v1/broker/subAccount", {"size": 1}))
```

```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class CaasSignExample {

    static final String BASE_URL = "https://api.binance.com";

    static String hmacSha256Hex(String data, String secret) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] raw = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        StringBuilder hex = new StringBuilder(raw.length * 2);
        for (byte b : raw) hex.append(String.format("%02x", b));
        return hex.toString();
    }

    static HttpResponse<String> signedGet(String path, String params,
                                          String apiKey, String apiSecret) throws Exception {
        String query = params + "&recvWindow=5000&timestamp=" + System.currentTimeMillis();
        String signature = hmacSha256Hex(query, apiSecret);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + path + "?" + query + "&signature=" + signature))
                .header("X-MBX-APIKEY", apiKey)
                .GET()
                .build();

        return HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
    }

    public static void main(String[] args) throws Exception {
        HttpResponse<String> resp = signedGet("/sapi/v1/broker/subAccount", "size=1",
                System.getenv("BINANCE_API_KEY"), System.getenv("BINANCE_API_SECRET"));
        System.out.println(resp.statusCode() + " " + resp.body());
    }
}
```

Note in both cases that `signature` is appended **after** the string that was signed, and is not
itself part of it.

---

## 5. Quick Integration Path

1. Get your master account API key and confirm the CAAS permission is active.
2. Call `GET /sapi/v1/broker/info` to verify credentials and see your broker configuration.
3. Create one test sub-account and take it all the way through to a working API key.
4. Transfer a small amount in, and confirm the balance via the asset endpoints.
5. Place a test trade with the sub-account key.
6. Wire up user data streams and confirm you receive the events.
7. Repeat for each product family the end user needs.

---

## 6. Step-by-Step: End-User Onboarding

### Step 1 — Create a sub-account

`POST /sapi/v1/broker/subAccount`

Returns the `subaccountId` used by every later call.

### Step 2 — Complete KYC and bind it to the sub-account

Through the KYC module:

- Share KYC API — `/bapi/ekyc/v2/public/ekyc/customer/share-kyc-data`

### Step 3 — Check that KYC has passed

`/bapi/ekyc/v2/public/ekyc/customer/check-kyc-status`

Requirement: `data.levelInfo.currentLevel.kycStatus` = `PASS`

:::note

**This step gates everything after it.** A sub-account cannot create an API key until its KYC has
passed. Calling `POST /sapi/v1/broker/subAccountApi` before then returns:

```json
{
  "code": -9000,
  "msg": "KYC has not been approved for this subaccount. Please complete KYC within 7 days to re-enable the subaccount. Till KYC is successfully completed, You will only be able to reduce margin and futures positions and withdraw."
}
```

So an un-KYC'd sub-account is **reduce-only**: it can cut margin and futures positions and withdraw,
and nothing else. Note the **7-day window** to complete KYC and re-enable the sub-account. See
[Binance Link KYC SaaS](/products/kyc-saas/overview) for the KYC endpoints and webhook.

`-9000` is reused across this API family for unrelated conditions — it is also returned when two
accounts are not in a parent-child relationship, and by the Markup endpoints when a sub-account has
no fee group. Read the `msg`, not just the code.

:::

### Step 4 — Enable any additional wallets

**Futures** — `POST /sapi/v1/broker/subAccount/futures`

**Margin** — there is no enable endpoint. The margin wallet is created by **transferring any amount
of an asset into it**, for example with `POST /sapi/v1/broker/universalTransfer`.

**Options are not available to CAAS sub-accounts.** `POST /sapi/v1/broker/subAccountApi` accepts
only `canTrade`, `marginTrade` and `futuresTrade`, so there is no permission to grant.

:::warning

**Do this before creating the API key.** `POST /sapi/v1/broker/subAccountApi` takes `futuresTrade`
and `marginTrade` as **creation-time** parameters, so the corresponding wallet must already exist. A
key created before the Futures wallet is opened will not work for Futures, and you will need to
issue a new one.

:::

### Step 5 — Create the sub-account API key

`POST /sapi/v1/broker/subAccountApi`

| Parameter      | Required | Notes                                                  |
| -------------- | -------- | ------------------------------------------------------ |
| `subAccountId` | Yes      | From step 1.                                           |
| `canTrade`     | Yes      | Spot trade.                                            |
| `marginTrade`  | No       | Margin trade — the margin wallet must already exist.   |
| `futuresTrade` | No       | Futures trade — the futures wallet must already exist. |
| `publicKey`    | No       | For Ed25519 or RSA keys.                               |

### Step 6 — Configure the key

- Permissions — `POST /sapi/v1/broker/subAccountApi/permission`
- IP restrictions — `POST /sapi/v2/broker/subAccountApi/ipRestriction`
- Universal transfer permission — `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer`

---

## 7. Step-by-Step: Moving Funds

CAAS has four transfer endpoints. They overlap, and picking the wrong one is a common source of
confusion. Use this table to choose:

| Endpoint                                       | Distinguishing parameters                            | Use when                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `POST /sapi/v1/broker/transfer`                | `fromId`, `toId`                                     | Moving spot balances between the master account and a sub-account.                                                        |
| `POST /sapi/v1/broker/transfer/futures`        | `fromId`, `toId`, `futuresType`                      | The same, for futures wallets. `futuresType` selects USD-M or COIN-M.                                                     |
| `POST /sapi/v1/broker/universalTransfer`       | `fromId`, `toId`, `fromAccountType`, `toAccountType` | Moving freely between Spot, USD-M and COIN-M. Both account types accept **only** `SPOT`, `USDT_FUTURE` and `COIN_FUTURE`. |
| `POST /sapi/v1/broker/futures/accountTransfer` | `subAccountId`, `type`                               | Master account moving funds to or from **one** sub-account's futures account; `type` sets the direction.                  |

All of them accept a `clientTranId` for idempotency except `futures/accountTransfer`.

### Checking transfer history

| Endpoint                                | Covers                     |
| --------------------------------------- | -------------------------- |
| `GET /sapi/v1/broker/transfer`          | Spot transfer history      |
| `GET /sapi/v1/broker/transfer/futures`  | Futures transfer history   |
| `GET /sapi/v1/broker/universalTransfer` | Universal transfer history |

### Checking balances

| Endpoint                                        | Covers                       |
| ----------------------------------------------- | ---------------------------- |
| `GET /sapi/v1/broker/subAccount/spotSummary`    | Sub-account spot balances    |
| `GET /sapi/v1/broker/subAccount/marginSummary`  | Sub-account margin balances  |
| `GET /sapi/v3/broker/subAccount/futuresSummary` | Sub-account futures balances |

### Choosing between the transfer endpoints

They are not interchangeable — each has a constraint the others do not:

| If you need to                                                       | Use                                            | The deciding constraint                                                                                                                                                                                  |
| -------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Move **spot** balances between the master account and a sub-account  | `POST /sapi/v1/broker/transfer`                | Needs no permission beyond the master key.                                                                                                                                                               |
| Move **futures** balances the same way                               | `POST /sapi/v1/broker/transfer/futures`        | `futuresType` selects USD-M or COIN-M.                                                                                                                                                                   |
| Cross wallet types in one call, or move between two **sub-accounts** | `POST /sapi/v1/broker/universalTransfer`       | The only form that crosses wallet types, but it requires the universal-transfer permission enabled on the sub-account API key first — `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer`. |
| Move funds to or from **one** sub-account's futures account          | `POST /sapi/v1/broker/futures/accountTransfer` | Carries no `clientTranId`, so a retry cannot be de-duplicated.                                                                                                                                           |

Two limits apply to all of them:

- **The margin wallet is not reachable.** `fromAccountType` and `toAccountType` accept only `SPOT`,
  `USDT_FUTURE` and `COIN_FUTURE`, and the specific forms cover spot and futures only.
- **Only `universalTransfer` moves between sub-accounts.** The other three are master-to-sub or
  sub-to-master.

---

## 8. Deposits and Withdrawals

Its asset endpoints move funds between your master account and its own sub-accounts. External
movement uses the main Wallet API, and the two directions behave differently:

- **Deposits can go directly to a sub-account.** Retrieve that sub-account's deposit address using
  its own API key.
- **Withdrawals can only be made from the master account.** A sub-account cannot withdraw. To move
  funds off Binance, first transfer from the sub-account to the master account (see
  [section 7](#7-step-by-step-moving-funds)), then withdraw from the master account.

| You need                        | Endpoint                                | Called with            |
| ------------------------------- | --------------------------------------- | ---------------------- |
| A sub-account's deposit address | `GET /sapi/v1/capital/deposit/address`  | Sub-account API key    |
| Deposit history                 | `GET /sapi/v1/capital/deposit/hisrec`   | Sub-account API key    |
| Submit a withdrawal             | `POST /sapi/v1/capital/withdraw/apply`  | **Master account key** |
| Withdrawal history              | `GET /sapi/v1/capital/withdraw/history` | **Master account key** |
| Per-coin network configuration  | `GET /sapi/v1/capital/config/getall`    | Either                 |

See the [Wallet API](/catalog/core-trading-wallet/api/rest-api/capital) for full parameters.

CAAS does provide a **read-only** view of sub-account deposits from the master account:

- `GET /sapi/v1/broker/subAccount/depositHist`
- `GET /sapi/v2/broker/subAccount/depositHist` — the V2 form

:::note

If your sub-accounts sit under a Binance local entity, deposits and withdrawals additionally require
travel rule information. See the
[Travel Rule endpoints](/catalog/core-trading-wallet/api/rest-api/travel-rule) — note the
`/localentity/broker/*` variants, which exist so a partner can submit on an end user's behalf.

:::

---

## 9. Commission Configuration

Commission is set **per sub-account API key**, and separately for each product family.

| Product        | Set                                                         | Query                                                      |
| -------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| Spot           | `POST /sapi/v1/broker/subAccountApi/commission`             | —                                                          |
| USD-M Futures  | `POST /sapi/v1/broker/subAccountApi/commission/futures`     | `GET /sapi/v1/broker/subAccountApi/commission/futures`     |
| COIN-M Futures | `POST /sapi/v1/broker/subAccountApi/commission/coinFutures` | `GET /sapi/v1/broker/subAccountApi/commission/coinFutures` |

### Rebate records

| Endpoint                                          | Covers                     |
| ------------------------------------------------- | -------------------------- |
| `GET /sapi/v1/broker/rebate/recentRecord`         | Spot commission rebates    |
| `GET /sapi/v1/broker/rebate/futures/recentRecord` | Futures commission rebates |

:::note

This is the **revenue share** model. If you are on the markup model instead, commission is
configured through fee groups — see [Markup](/products/caas/markup/overview). Revenue share and
markup cannot be combined.

:::

---

## 10. User Data Streams

CAAS has no user data stream endpoints of its own. Each account opens its own stream with its own
API key, and there is no aggregated stream across your end users.

See [User Data Streams](/products/caas/user-data-streams) for which stream to open per account and
product, the event types for spot and futures, and the keepalive and reconnection rules.

---

## 11. Error Handling

### Common response structure

CAAS endpoints return either a JSON object or array. Errors use the standard Binance envelope:

```json
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

### HTTP status codes

| Status | Meaning                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------- |
| `4XX`  | Malformed request; the issue is on the sender's side.                                                   |
| `429`  | Rate limit breached. Back off rather than continuing to send.                                           |
| `418`  | IP auto-banned after continuing to send following `429`s. **Does not apply to `/sapi/*`.**              |
| `5XX`  | Internal error. **Do not** treat as a failure — execution status is **UNKNOWN** and may have succeeded. |

:::warning

A `5XX` is not a failed operation. Query the resulting state before retrying, or you risk
duplicating a transfer or an account.

:::

### Rate limits

CAAS endpoints are all `/sapi/*`, which behaves differently from `/api/*`:

- Each `/sapi/*` endpoint has its **own independent** limit rather than sharing a pool.
- Weight headers are `X-SAPI-USED-IP-WEIGHT-1M` or `X-SAPI-USED-UID-WEIGHT-1M`.
- Exceeding the limit returns `429`. The `418` IP-ban escalation does **not** apply.

Full detail in [Rate limits](/products/caas/basics/4.rate-limits).

---

## 12. Readiness Checklist

**CAAS, KYC SaaS and Markup have no separate test environment** — you verify against production.
Work through this on a small number of real sub-accounts with minimal balances before onboarding end
users at volume.

The [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) is the
exception: it **does** have a QA environment, and its documentation recommends starting integration
there. Ask the CaaS Team for the QA base URLs — see
[Environments and API base URLs](/products/institutional-buy-sell/basics/4.base-urls). That QA
environment covers the ICBSS module only; the CAAS accounts underneath it are still production.

#### Authentication

- [ ] Master account key authenticates against `GET /sapi/v1/broker/info`.
- [ ] Signature verified against a request containing a space or special character.
- [ ] `recvWindow` behaviour confirmed with a deliberately stale `timestamp`.

#### Account creation

- [ ] Sub-account created and `subaccountId` stored.
- [ ] KYC completed and `kycStatus` = `PASS` observed before key creation.
- [ ] Futures wallet enabled **before** key creation, and `futuresTrade=true` key verified working.
- [ ] IP restrictions applied and confirmed to reject a non-allowlisted caller.

#### Assets

- [ ] Transfer master → sub and sub → master, verified in the balance summaries.
- [ ] Transfer history returns the `clientTranId` you sent.
- [ ] Deposit address retrieved with the sub-account key.

#### Error handling

- [ ] `429` handled with backoff.
- [ ] `5XX` handled by querying state rather than blind retry.

#### Streams

- [ ] User data stream opened per account and events received.
- [ ] Keepalive holds the stream past 60 minutes.
- [ ] Reconnect after the 24-hour disconnect, with REST reconciliation.

---

## 13. Best Practices

### Security

- Keep the master account key on your backend only. It can create and delete accounts.
- Issue each sub-account key with the narrowest permission set the end user needs.
- Apply IP restrictions to every key you create.
- Rotate keys on a schedule, and delete keys for closed accounts.

### Reliability

- Send `clientTranId` on every transfer so retries are idempotent.
- Treat `5XX` as unknown, not failed — query before retrying.
- Reconcile balances against REST after every stream reconnect; missed events are not replayed.
- Do not share one `listenKey` across accounts. A key is scoped to the account that created it.

### Rate limits

- Spread sub-account operations rather than bursting; each `/sapi/*` endpoint has its own limit.
- Read the `X-SAPI-USED-*-WEIGHT-1M` headers rather than inferring your usage.

---

## 14. FAQ

Common questions about CAAS integration are answered on the [CAAS FAQ](/products/caas/Faq).

---

# Crypto-As-A-Service — Integration Guideline

> This guideline helps partners integrate Crypto-As-A-Service (CAAS) from scratch. Follow the steps
> below to go from zero to live. It repeats the environment and authentication detail from
> [Getting Started](/products/caas/getting-started) and the
> [API basics](/products/caas/basics/1.base-urls) so that this page can be followed end to end
> without switching away.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Step-by-Step: End-User Onboarding](#6-step-by-step-end-user-onboarding)
7. [Step-by-Step: Moving Funds](#7-step-by-step-moving-funds)
8. [Deposits and Withdrawals](#8-deposits-and-withdrawals)
9. [Commission Configuration](#9-commission-configuration)
10. [User Data Streams](#10-user-data-streams)
11. [Error Handling](#11-error-handling)
12. [Readiness Checklist](#12-readiness-checklist)
13. [Best Practices](#13-best-practices)
14. [FAQ](#14-faq)

---

## 1. Before You Begin

### What is CAAS?

Crypto-As-A-Service lets a platform offer crypto functionality to its users without building an
exchange, custody, wallet, trading, or settlement stack. Your application connects to Binance from
your own backend; you build the front end, and Binance provides the account, custody, and execution
layer.

### Core capabilities

| Capability               | What you get                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| Sub-account management   | One Binance account per end user, created and controlled through your master account.     |
| Per-user API credentials | An API key scoped to a single sub-account, with configurable permissions and IP controls. |
| Asset movement           | Transfers between your master account and its sub-accounts across spot, margin, futures.  |
| Commission               | Set and query the commission you earn on each sub-account's spot and futures activity.    |
| Optional modules         | KYC SaaS, Markup, and the Institutional Crypto Buy/Sell Solution.                         |

### Architecture

CAAS is a server-to-server integration. There is no Binance-hosted interface for your end users.

```
Your front end  ──►  Your backend  ──►  CAAS API (/sapi/v1/broker/*)
                          │                    master account API key
                          └────────────►  Trading APIs (/api, /fapi, /dapi)
                                               sub-account API key
```

Two credentials do different jobs, and mixing them is the most common integration mistake:

| Credential             | Used for                                                                 |
| ---------------------- | ------------------------------------------------------------------------ |
| Master account API key | Every `/sapi/v1/broker/*` call — account creation, transfers, commission |
| Sub-account API key    | Trading and wallet operations **on behalf of that one end user**         |

---

## 2. Onboarding Checklist

### Items you provide to Binance

- Your institutional entity details and completed onboarding.
- The commercial model you want — revenue share or [Markup](/products/caas/markup/overview).
- Which modules you need enabled: KYC SaaS, Markup, Institutional Crypto Buy/Sell Solution.

### Items Binance provides to you

- The CAAS permission on your master account.
- Confirmation of which products your sub-accounts may be enabled for.

You create your own master account API key and secret in the Binance interface; Binance does not
issue them to you.

:::note

CAAS itself does not require you to register your calling IP addresses with Binance. IP allowlisting
at onboarding applies to [KYC SaaS](/products/kyc-saas/overview) and the
[Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) only. You
can still restrict the sub-account API keys you create — see
[section 6](#6-step-by-step-end-user-onboarding).

:::

<!-- TODO(sulyn): confirm this checklist against the actual onboarding process. The lists above are
     derived from what the API requires, not from an onboarding runbook. -->

---

## 3. Environment Setup

### Base URLs

| Endpoint family | Used for                                              | Base endpoint                |
| --------------- | ----------------------------------------------------- | ---------------------------- |
| `/sapi/*`       | CAAS, OMS Toolkit, and other wallet/account functions | **https://api.binance.com**  |
| `/api/*`        | Spot trading                                          | **https://api.binance.com**  |
| `/fapi/*`       | USD-M Futures                                         | **https://fapi.binance.com** |
| `/dapi/*`       | COIN-M Futures                                        | **https://dapi.binance.com** |

For `/api/*` and `/sapi/*`, the alternates **https://api-gcp.binance.com** and
**https://api1.binance.com** through **https://api4.binance.com** are also available. Performance
between them may vary; if one is slow, try another.

### Required HTTP headers

| Header         | Value                               | When                                |
| -------------- | ----------------------------------- | ----------------------------------- |
| `X-MBX-APIKEY` | Your API key                        | Every CAAS request                  |
| `Content-Type` | `application/x-www-form-urlencoded` | `POST`, `PUT`, `DELETE` with a body |

### Parameter rules

- For `GET` endpoints, parameters must be sent as a `query string`.
- For `POST`, `PUT`, and `DELETE`, parameters may be sent as a `query string` or in the
  `request body`. You may mix both.
- If the same parameter appears in both, the `query string` value is used.
- Parameters may be sent in any order.
- Email addresses must be URL-encoded and lower case — `alice@test.com` becomes `alice%40test.com`.

---

## 4. Authentication & Request Signing

Every CAAS endpoint is `SIGNED`; there are no public CAAS endpoints. Most of them sit under
`/sapi/v1/broker/*`. This applies to the CAAS API only, not to Binance endpoints in general.

### Security types

| Security Type | Description                                              |
| ------------- | -------------------------------------------------------- |
| TRADE         | Endpoint requires sending a valid API-Key and signature. |
| USER_DATA     | Endpoint requires sending a valid API-Key and signature. |

- API keys are passed via the `X-MBX-APIKEY` header.
- API keys and secret keys **are case sensitive**.
- A key can be restricted to certain endpoint types. By default it can access all secure routes.

### Step-by-step signing

1. Build the request parameter string, including `timestamp` (Unix milliseconds).
2. Optionally include `recvWindow` — the request is rejected if it arrives more than `recvWindow`
   milliseconds after `timestamp`.
3. Sign the parameter string with your secret key.
4. Append the result as a `signature` parameter.
5. Send the API key in the `X-MBX-APIKEY` header.

:::warning

**Sign the exact string you send.** Re-ordering or re-encoding parameters after signing invalidates
the signature. A space must be encoded as `%20`, not `+`.

:::

### Key types

Sub-account API keys support asymmetric key types. `POST /sapi/v1/broker/subAccountApi` accepts a
`publicKey` parameter for **Ed25519 and RSA** keys; omit it for an HMAC key.

### Worked example

Both examples below sign a real request to `GET /sapi/v1/broker/subAccount` with an HMAC key, using
only the standard library. Read your key and secret from the environment rather than hardcoding
them.

```python
import hashlib, hmac, os, time, urllib.parse, urllib.request

API_KEY = os.environ["BINANCE_API_KEY"]
API_SECRET = os.environ["BINANCE_API_SECRET"]
BASE_URL = "https://api.binance.com"


def signed_get(path, params=None):
    params = dict(params or {})
    params["recvWindow"] = 5000
    params["timestamp"] = int(time.time() * 1000)
    # quote_via=quote encodes a space as %20, not '+'
    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    signature = hmac.new(
        API_SECRET.encode("utf-8"), query.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    url = f"{BASE_URL}{path}?{query}&signature={signature}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req) as resp:
        return resp.status, resp.read().decode("utf-8")


print(signed_get("/sapi/v1/broker/subAccount", {"size": 1}))
```

```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class CaasSignExample {

    static final String BASE_URL = "https://api.binance.com";

    static String hmacSha256Hex(String data, String secret) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] raw = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        StringBuilder hex = new StringBuilder(raw.length * 2);
        for (byte b : raw) hex.append(String.format("%02x", b));
        return hex.toString();
    }

    static HttpResponse<String> signedGet(String path, String params,
                                          String apiKey, String apiSecret) throws Exception {
        String query = params + "&recvWindow=5000&timestamp=" + System.currentTimeMillis();
        String signature = hmacSha256Hex(query, apiSecret);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + path + "?" + query + "&signature=" + signature))
                .header("X-MBX-APIKEY", apiKey)
                .GET()
                .build();

        return HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
    }

    public static void main(String[] args) throws Exception {
        HttpResponse<String> resp = signedGet("/sapi/v1/broker/subAccount", "size=1",
                System.getenv("BINANCE_API_KEY"), System.getenv("BINANCE_API_SECRET"));
        System.out.println(resp.statusCode() + " " + resp.body());
    }
}
```

Note in both cases that `signature` is appended **after** the string that was signed, and is not
itself part of it.

---

## 5. Quick Integration Path

1. Get your master account API key and confirm the CAAS permission is active.
2. Call `GET /sapi/v1/broker/info` to verify credentials and see your broker configuration.
3. Create one test sub-account and take it all the way through to a working API key.
4. Transfer a small amount in, and confirm the balance via the asset endpoints.
5. Place a test trade with the sub-account key.
6. Wire up user data streams and confirm you receive the events.
7. Repeat for each product family the end user needs.

---

## 6. Step-by-Step: End-User Onboarding

### Step 1 — Create a sub-account

`POST /sapi/v1/broker/subAccount`

Returns the `subaccountId` used by every later call.

### Step 2 — Complete KYC and bind it to the sub-account

Through the KYC module:

- Share KYC API — `/bapi/ekyc/v2/public/ekyc/customer/share-kyc-data`

### Step 3 — Check that KYC has passed

`/bapi/ekyc/v2/public/ekyc/customer/check-kyc-status`

Requirement: `data.levelInfo.currentLevel.kycStatus` = `PASS`

:::note

**This step gates everything after it.** A sub-account cannot create an API key until its KYC has
passed. Calling `POST /sapi/v1/broker/subAccountApi` before then returns:

```json
{
  "code": -9000,
  "msg": "KYC has not been approved for this subaccount. Please complete KYC within 7 days to re-enable the subaccount. Till KYC is successfully completed, You will only be able to reduce margin and futures positions and withdraw."
}
```

So an un-KYC'd sub-account is **reduce-only**: it can cut margin and futures positions and withdraw,
and nothing else. Note the **7-day window** to complete KYC and re-enable the sub-account. See
[Binance Link KYC SaaS](/products/kyc-saas/overview) for the KYC endpoints and webhook.

`-9000` is reused across this API family for unrelated conditions — it is also returned when two
accounts are not in a parent-child relationship, and by the Markup endpoints when a sub-account has
no fee group. Read the `msg`, not just the code.

:::

### Step 4 — Enable any additional wallets

**Futures** — `POST /sapi/v1/broker/subAccount/futures`

**Margin** — there is no enable endpoint. The margin wallet is created by **transferring any amount
of an asset into it**, for example with `POST /sapi/v1/broker/universalTransfer`.

**Options are not available to CAAS sub-accounts.** `POST /sapi/v1/broker/subAccountApi` accepts
only `canTrade`, `marginTrade` and `futuresTrade`, so there is no permission to grant.

:::warning

**Do this before creating the API key.** `POST /sapi/v1/broker/subAccountApi` takes `futuresTrade`
and `marginTrade` as **creation-time** parameters, so the corresponding wallet must already exist. A
key created before the Futures wallet is opened will not work for Futures, and you will need to
issue a new one.

:::

### Step 5 — Create the sub-account API key

`POST /sapi/v1/broker/subAccountApi`

| Parameter      | Required | Notes                                                  |
| -------------- | -------- | ------------------------------------------------------ |
| `subAccountId` | Yes      | From step 1.                                           |
| `canTrade`     | Yes      | Spot trade.                                            |
| `marginTrade`  | No       | Margin trade — the margin wallet must already exist.   |
| `futuresTrade` | No       | Futures trade — the futures wallet must already exist. |
| `publicKey`    | No       | For Ed25519 or RSA keys.                               |

### Step 6 — Configure the key

- Permissions — `POST /sapi/v1/broker/subAccountApi/permission`
- IP restrictions — `POST /sapi/v2/broker/subAccountApi/ipRestriction`
- Universal transfer permission — `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer`

---

## 7. Step-by-Step: Moving Funds

CAAS has four transfer endpoints. They overlap, and picking the wrong one is a common source of
confusion. Use this table to choose:

| Endpoint                                       | Distinguishing parameters                            | Use when                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `POST /sapi/v1/broker/transfer`                | `fromId`, `toId`                                     | Moving spot balances between the master account and a sub-account.                                                        |
| `POST /sapi/v1/broker/transfer/futures`        | `fromId`, `toId`, `futuresType`                      | The same, for futures wallets. `futuresType` selects USD-M or COIN-M.                                                     |
| `POST /sapi/v1/broker/universalTransfer`       | `fromId`, `toId`, `fromAccountType`, `toAccountType` | Moving freely between Spot, USD-M and COIN-M. Both account types accept **only** `SPOT`, `USDT_FUTURE` and `COIN_FUTURE`. |
| `POST /sapi/v1/broker/futures/accountTransfer` | `subAccountId`, `type`                               | Master account moving funds to or from **one** sub-account's futures account; `type` sets the direction.                  |

All of them accept a `clientTranId` for idempotency except `futures/accountTransfer`.

### Checking transfer history

| Endpoint                                | Covers                     |
| --------------------------------------- | -------------------------- |
| `GET /sapi/v1/broker/transfer`          | Spot transfer history      |
| `GET /sapi/v1/broker/transfer/futures`  | Futures transfer history   |
| `GET /sapi/v1/broker/universalTransfer` | Universal transfer history |

### Checking balances

| Endpoint                                        | Covers                       |
| ----------------------------------------------- | ---------------------------- |
| `GET /sapi/v1/broker/subAccount/spotSummary`    | Sub-account spot balances    |
| `GET /sapi/v1/broker/subAccount/marginSummary`  | Sub-account margin balances  |
| `GET /sapi/v3/broker/subAccount/futuresSummary` | Sub-account futures balances |

### Choosing between the transfer endpoints

They are not interchangeable — each has a constraint the others do not:

| If you need to                                                       | Use                                            | The deciding constraint                                                                                                                                                                                  |
| -------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Move **spot** balances between the master account and a sub-account  | `POST /sapi/v1/broker/transfer`                | Needs no permission beyond the master key.                                                                                                                                                               |
| Move **futures** balances the same way                               | `POST /sapi/v1/broker/transfer/futures`        | `futuresType` selects USD-M or COIN-M.                                                                                                                                                                   |
| Cross wallet types in one call, or move between two **sub-accounts** | `POST /sapi/v1/broker/universalTransfer`       | The only form that crosses wallet types, but it requires the universal-transfer permission enabled on the sub-account API key first — `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer`. |
| Move funds to or from **one** sub-account's futures account          | `POST /sapi/v1/broker/futures/accountTransfer` | Carries no `clientTranId`, so a retry cannot be de-duplicated.                                                                                                                                           |

Two limits apply to all of them:

- **The margin wallet is not reachable.** `fromAccountType` and `toAccountType` accept only `SPOT`,
  `USDT_FUTURE` and `COIN_FUTURE`, and the specific forms cover spot and futures only.
- **Only `universalTransfer` moves between sub-accounts.** The other three are master-to-sub or
  sub-to-master.

---

## 8. Deposits and Withdrawals

Its asset endpoints move funds between your master account and its own sub-accounts. External
movement uses the main Wallet API, and the two directions behave differently:

- **Deposits can go directly to a sub-account.** Retrieve that sub-account's deposit address using
  its own API key.
- **Withdrawals can only be made from the master account.** A sub-account cannot withdraw. To move
  funds off Binance, first transfer from the sub-account to the master account (see
  [section 7](#7-step-by-step-moving-funds)), then withdraw from the master account.

| You need                        | Endpoint                                | Called with            |
| ------------------------------- | --------------------------------------- | ---------------------- |
| A sub-account's deposit address | `GET /sapi/v1/capital/deposit/address`  | Sub-account API key    |
| Deposit history                 | `GET /sapi/v1/capital/deposit/hisrec`   | Sub-account API key    |
| Submit a withdrawal             | `POST /sapi/v1/capital/withdraw/apply`  | **Master account key** |
| Withdrawal history              | `GET /sapi/v1/capital/withdraw/history` | **Master account key** |
| Per-coin network configuration  | `GET /sapi/v1/capital/config/getall`    | Either                 |

See the [Wallet API](/catalog/core-trading-wallet/api/rest-api/capital) for full parameters.

CAAS does provide a **read-only** view of sub-account deposits from the master account:

- `GET /sapi/v1/broker/subAccount/depositHist`
- `GET /sapi/v2/broker/subAccount/depositHist` — the V2 form

:::note

If your sub-accounts sit under a Binance local entity, deposits and withdrawals additionally require
travel rule information. See the
[Travel Rule endpoints](/catalog/core-trading-wallet/api/rest-api/travel-rule) — note the
`/localentity/broker/*` variants, which exist so a partner can submit on an end user's behalf.

:::

---

## 9. Commission Configuration

Commission is set **per sub-account API key**, and separately for each product family.

| Product        | Set                                                         | Query                                                      |
| -------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| Spot           | `POST /sapi/v1/broker/subAccountApi/commission`             | —                                                          |
| USD-M Futures  | `POST /sapi/v1/broker/subAccountApi/commission/futures`     | `GET /sapi/v1/broker/subAccountApi/commission/futures`     |
| COIN-M Futures | `POST /sapi/v1/broker/subAccountApi/commission/coinFutures` | `GET /sapi/v1/broker/subAccountApi/commission/coinFutures` |

### Rebate records

| Endpoint                                          | Covers                     |
| ------------------------------------------------- | -------------------------- |
| `GET /sapi/v1/broker/rebate/recentRecord`         | Spot commission rebates    |
| `GET /sapi/v1/broker/rebate/futures/recentRecord` | Futures commission rebates |

:::note

This is the **revenue share** model. If you are on the markup model instead, commission is
configured through fee groups — see [Markup](/products/caas/markup/overview). Revenue share and
markup cannot be combined.

:::

---

## 10. User Data Streams

CAAS has no user data stream endpoints of its own. Each account opens its own stream with its own
API key, and there is no aggregated stream across your end users.

See [User Data Streams](/products/caas/user-data-streams) for which stream to open per account and
product, the event types for spot and futures, and the keepalive and reconnection rules.

---

## 11. Error Handling

### Common response structure

CAAS endpoints return either a JSON object or array. Errors use the standard Binance envelope:

```json
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

### HTTP status codes

| Status | Meaning                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------- |
| `4XX`  | Malformed request; the issue is on the sender's side.                                                   |
| `429`  | Rate limit breached. Back off rather than continuing to send.                                           |
| `418`  | IP auto-banned after continuing to send following `429`s. **Does not apply to `/sapi/*`.**              |
| `5XX`  | Internal error. **Do not** treat as a failure — execution status is **UNKNOWN** and may have succeeded. |

:::warning

A `5XX` is not a failed operation. Query the resulting state before retrying, or you risk
duplicating a transfer or an account.

:::

### Rate limits

CAAS endpoints are all `/sapi/*`, which behaves differently from `/api/*`:

- Each `/sapi/*` endpoint has its **own independent** limit rather than sharing a pool.
- Weight headers are `X-SAPI-USED-IP-WEIGHT-1M` or `X-SAPI-USED-UID-WEIGHT-1M`.
- Exceeding the limit returns `429`. The `418` IP-ban escalation does **not** apply.

Full detail in [Rate limits](/products/caas/basics/4.rate-limits).

---

## 12. Readiness Checklist

**CAAS, KYC SaaS and Markup have no separate test environment** — you verify against production.
Work through this on a small number of real sub-accounts with minimal balances before onboarding end
users at volume.

The [Institutional Crypto Buy/Sell Solution](/products/institutional-buy-sell/introduction) is the
exception: it **does** have a QA environment, and its documentation recommends starting integration
there. Ask the CaaS Team for the QA base URLs — see
[Environments and API base URLs](/products/institutional-buy-sell/basics/4.base-urls). That QA
environment covers the ICBSS module only; the CAAS accounts underneath it are still production.

#### Authentication

- [ ] Master account key authenticates against `GET /sapi/v1/broker/info`.
- [ ] Signature verified against a request containing a space or special character.
- [ ] `recvWindow` behaviour confirmed with a deliberately stale `timestamp`.

#### Account creation

- [ ] Sub-account created and `subaccountId` stored.
- [ ] KYC completed and `kycStatus` = `PASS` observed before key creation.
- [ ] Futures wallet enabled **before** key creation, and `futuresTrade=true` key verified working.
- [ ] IP restrictions applied and confirmed to reject a non-allowlisted caller.

#### Assets

- [ ] Transfer master → sub and sub → master, verified in the balance summaries.
- [ ] Transfer history returns the `clientTranId` you sent.
- [ ] Deposit address retrieved with the sub-account key.

#### Error handling

- [ ] `429` handled with backoff.
- [ ] `5XX` handled by querying state rather than blind retry.

#### Streams

- [ ] User data stream opened per account and events received.
- [ ] Keepalive holds the stream past 60 minutes.
- [ ] Reconnect after the 24-hour disconnect, with REST reconciliation.

---

## 13. Best Practices

### Security

- Keep the master account key on your backend only. It can create and delete accounts.
- Issue each sub-account key with the narrowest permission set the end user needs.
- Apply IP restrictions to every key you create.
- Rotate keys on a schedule, and delete keys for closed accounts.

### Reliability

- Send `clientTranId` on every transfer so retries are idempotent.
- Treat `5XX` as unknown, not failed — query before retrying.
- Reconcile balances against REST after every stream reconnect; missed events are not replayed.
- Do not share one `listenKey` across accounts. A key is scoped to the account that created it.

### Rate limits

- Spread sub-account operations rather than bursting; each `/sapi/*` endpoint has its own limit.
- Read the `X-SAPI-USED-*-WEIGHT-1M` headers rather than inferring your usage.

---

## 14. FAQ

Common questions about CAAS integration are answered on the [CAAS FAQ](/products/caas/Faq).