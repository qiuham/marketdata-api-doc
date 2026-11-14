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
source_url: 'https://docs.kraken.com/exchange/guides/futures/introduction'
updated_at: 2026-11-13
---

# Derivatives Introduction

> Overview of the Kraken Derivatives (Futures) API — REST, WebSocket, and FIX access, conventions, and testing environment

## Platform overview

The Kraken Derivatives platform provides access via REST, WebSocket, and FIX APIs. For FIX, refer to the [FIX introduction](https://docs.kraken.com/exchange/guides/fix/introduction.md) for session setup and authentication.

The REST API provides secure access to your Derivatives account to:

* Request current or historical price information
* Check your account balance and PnL
* View margin parameters and estimated liquidation thresholds
* Place or cancel orders (individually or in batch)
* View open orders, open positions, or trade history
* Request a digital asset withdrawal

The [WebSocket API](https://docs.kraken.com/exchange/guides/futures/websockets.md) provides real-time data channels, eliminating the need to periodically poll for frequently changing information.

The API can be implemented in any language capable of managing HTTP requests. See [sample implementations](#sample-implementations) for code in Java, Python, C#, and Visual Basic .NET.

## Conventions

### Server time

All timestamps are in Coordinated Universal Time (UTC).

### Unique identifiers

```text theme={null}
c18f0c17-9971-40e6-8e5b-10df05d422f0
```

Unique identifiers follow the UUID (Universally Unique Identifier) standard.

### Dates and times

```text theme={null}
2016-02-26T12:09:38.830Z
```

The API requires and returns dates in ISO 8601 format: `<yyyy>-<mm>-<dd>T<HH>:<MM>:<SS>.<sss>Z`. The millisecond component `<sss>` is optional when provided as an argument. `Z` denotes UTC.

### Symbols

The system identifies accounts, margin accounts, futures contracts, and indices through ticker symbols:

| Symbol | Description |
| :- | :- |
| `xbt` | Bitcoin |
| `xrp` | Ripple XRP |
| `fi_xbtusd` | Bitcoin-Dollar Futures Margin Account |
| `fi_xrpusd` | Ripple-Dollar Futures Margin Account |
| `fi_xbtusd_180615` | Bitcoin-Dollar Futures, maturing 16:00 London time 15 June 2018 |
| `in_xbtusd` | Bitcoin-Dollar Real-Time Index |
| `rr_xbtusd` | Bitcoin-Dollar Reference Rate |

## Generate API keys

1. Sign in to your Derivatives account.

2. Click your **name** in the upper-right corner.

3. Select **Settings** from the drop-down menu.

4. Select the **Create Key** tab in the API panel.

5. Choose the access level:

   **General API:** No Access / Read Only / Full Access (excludes withdrawals)

   **Withdrawal API:** No Access / Full Access (controls withdrawal permissions)

6. Press **Create Key**.

7. Record your Public and Private keys somewhere safe.

> [!WARNING]
>
> The private key is shown only once. You cannot view it again after closing this screen.

> [!WARNING]
>
> API keys must be kept secure and never shared. If you cannot store your private key safely, do not generate it.

### Key limits

Up to 50 keys can be created per account, each with a distinct nonce.

## API testing environment

A fully functional demo environment is available at [demo-futures.kraken.com](https://demo-futures.kraken.com). It is completely separate from production and does not require existing account credentials.

To get started:

1. Navigate to [demo-futures.kraken.com](https://demo-futures.kraken.com)
2. Click **Sign Up** — email and password are generated automatically
3. Accept the Demo Terms & Conditions and Privacy Policy
4. Note your credentials for reuse, then select **Complete Sign-Up**

Once signed up, [generate API keys](#generate-api-keys) for testing.

The demo API code is identical to production in terms of feeds, endpoints, and response structure. The only difference is the base URL:

| Environment | Base URL |
| :- | :- |
| Production | `https://futures.kraken.com` |
| Demo | `https://demo-futures.kraken.com` |

**WebSocket (demo):** `wss://demo-futures.kraken.com/ws/v1`

**REST (demo):** `https://demo-futures.kraken.com/derivatives/api/v3/tickers`

## API URLs

**REST API:**

```text theme={null}
https://futures.kraken.com/derivatives/api/v3/
https://futures.kraken.com/api/history/v2/
https://futures.kraken.com/api/charts/v1/
```

**WebSocket:**

```text theme={null}
wss://futures.kraken.com/ws/v1
```

> [!NOTE]
>
> Direct access URLs for IP whitelisting are different from the above. Contact your Account Manager for whitelisted endpoint details.

## Sample implementations

Sample implementations in Java, Python, C#, and Visual Basic .NET are available on GitHub:

[github.com/krakenfx](https://github.com/krakenfx)

If you have implemented the API in another language and would like to share it, contact support.
