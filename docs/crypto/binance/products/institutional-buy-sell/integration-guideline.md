---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-buy-sell/integration-guideline
api_type: Guide
updated_at: 2026-11-20 18:32:22.933487
---

# Institutional Crypto Buy/Sell Solution — Integration Guideline

> This guideline helps partners (merchants) integrate Institutional Crypto Buy/Sell Solution's Open
> API from scratch. Follow the steps below to go from zero to live.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Step-by-Step: Buy Flow Integration](#6-step-by-step-buy-flow-integration)
7. [Step-by-Step: Sell Flow Integration](#7-step-by-step-sell-flow-integration)
8. [Webhook Integration](#8-webhook-integration)
9. [Merchant-Side API Implementation](#9-merchant-side-api-implementation)
10. [Market Data APIs (Optional)](#10-market-data-apis-optional)
11. [Error Handling](#11-error-handling)
12. [Testing & Go-Live Checklist](#12-testing--go-live-checklist)
13. [Best Practices](#13-best-practices)
14. [FAQ](#14-faq)
15. [Documentation Notes](#15-documentation-notes)

---

## 1. Before You Begin

### What is Institutional Crypto Buy/Sell Solution?

> **This is a module of [Crypto-As-A-Service (CAAS)](/products/caas/overview).** It assumes you have
> completed CAAS onboarding and are familiar with the CAAS account and asset model. Read the
> [CAAS Overview](/products/caas/overview) before this guideline. Spread for this module is set per
> request through the `customSpread` parameter — see
> [Get quote](/products/institutional-buy-sell/open-apis/5.get-quote).

Institutional Crypto Buy/Sell Solution is a **turnkey crypto Buy/Sell solution** that enables banks,
fintechs, and platforms to offer crypto services directly inside their own apps — without building
complex infrastructure from scratch. Binance handles the liquidity, order execution, and crypto
infrastructure; you keep control over your fiat operations and customer relationships.

### Core Capabilities

| Capability           | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Buy Crypto**       | Users buy crypto with fiat; Binance executes the trade                    |
| **Sell Crypto**      | Users sell crypto for fiat; Binance executes and you handle fiat transfer |
| **Real-Time Quotes** | Fetch live price quotes with custom spread support                        |
| **Transaction Mgmt** | Query single or bulk transactions, monitor status                         |
| **Webhook**          | Receive real-time order status notifications                              |
| **Market Data**      | Kline, discover price, symbol detail for building UIs                     |

### Architecture Overview

```
┌───────────┐         ┌────────────────────┐         ┌─────────────────────┐
│  End User │ ◄─────► │  Your App / API    │ ◄─────► │  Binance            │
│           │         │  (Merchant Side)   │         │  Open API           │
└───────────┘         └────────────────────┘         └─────────────────────┘
                          │                              │
                          │  Merchant APIs               │  Webhook
                          │  (Check Txn / Refund /       │  (Order status
                          │   Transfer)                  │   notifications)
                          ◄──────────────────────────────┘
```

**Key points:**

- All API communication is **server-to-server** (your backend ↔ Binance).
- Most APIs require a `userId` parameter — this is the Binance sub-account ID obtained after
  completing user onboarding via [Binance Link KYC SaaS](/products/kyc-saas/overview). You must
  integrate Binance CaaS first before calling Institutional Crypto Buy/Sell Solution APIs.
- You **MUST** implement merchant-side APIs for Binance to call back (see
  [Section 9](#9-merchant-side-api-implementation)).
- Webhook provides asynchronous order status updates.

---

## 2. Onboarding Checklist

Before calling any API, complete the following with the CaaS Team:

### Items You Provide to Binance

| #   | Item                       | Description                                                                        |
| --- | -------------------------- | ---------------------------------------------------------------------------------- |
| 1   | **RSA Public Key**         | Your public key for API request signing (2048-bit RSA). Keep the private key safe! |
| 2   | **IP Whitelist**           | IP addresses of your servers that will call Binance APIs                           |
| 3   | **Webhook Callback URL**   | The HTTPS endpoint where Binance sends webhook notifications                       |
| 4   | **Merchant-Side API URLs** | Endpoints for Check Transaction, Refund (Buy), and Transfer (Sell)                 |

### Items Binance Provides to You

| #   | Item                   | Description                                                     |
| --- | ---------------------- | --------------------------------------------------------------- |
| 1   | **Client ID**          | Your unique partner identifier (`X-Tesla-ClientId`)             |
| 2   | **Sign Access Token**  | Access token for API authentication (`X-Tesla-SignAccessToken`) |
| 3   | **Webhook Public Key** | Binance's public key for verifying webhook signatures           |

> **Recommendation:** Start integration in the **QA environment** first. Contact the CaaS Team for
> QA base URLs.

---

## 3. Environment Setup

### Base URLs

| Environment | URL                      |
| ----------- | ------------------------ |
| QA          | Please ask for CaaS Team |
| Production  | Please ask for CaaS Team |

### Required HTTP Headers (Every Request)

| Header                    | Value                                             |
| ------------------------- | ------------------------------------------------- |
| `Content-Type`            | `application/json`                                |
| `X-Tesla-ClientId`        | Your Client ID                                    |
| `X-Tesla-SignAccessToken` | Your Sign Access Token                            |
| `X-Tesla-Timestamp`       | Current timestamp in **milliseconds**             |
| `X-Tesla-Signature`       | RSA SHA256 signature of `requestBody + timestamp` |

---

## 4. Authentication & Request Signing

All API requests must be signed with **SHA256withRSA**. The signing payload is:

```
signPayload = JSON_REQUEST_BODY + TIMESTAMP_IN_MILLISECONDS
```

### Step-by-Step Signing

1. **Generate RSA Key Pair** (2048-bit) — keep the private key secret, share the public key with
   Binance.
2. **Prepare the payload**: concatenate the JSON request body (as a string) with the timestamp.
3. **Sign** the payload with your private key using SHA256withRSA.
4. **Base64-encode** the signature.
5. **Set HTTP headers** with the signature, timestamp, client ID, and access token.

### Java Example

```java
import org.apache.commons.codec.binary.Base64;
import java.security.*;
import java.security.spec.PKCS8EncodedKeySpec;

public class BuySellSigner {

    /**
     * Full signing example: build headers for a Institutional Crypto Buy/Sell Solution API request.
     */
    public static Map<String, String> buildHeaders(
            String clientId, String accessToken,
            String privateKeyBase64, String jsonBody) throws Exception {

        long timestamp = System.currentTimeMillis();
        PrivateKey privateKey = loadPrivateKey(privateKeyBase64);
        String signature = sign(jsonBody + timestamp, privateKey);

        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Tesla-ClientId", clientId);
        headers.put("X-Tesla-SignAccessToken", accessToken);
        headers.put("X-Tesla-Timestamp", String.valueOf(timestamp));
        headers.put("X-Tesla-Signature", signature);
        return headers;
    }

    private static PrivateKey loadPrivateKey(String base64Key) throws Exception {
        byte[] keyBytes = Base64.decodeBase64(base64Key);
        PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
        return KeyFactory.getInstance("RSA").generatePrivate(spec);
    }

    private static String sign(String data, PrivateKey privateKey) throws Exception {
        Signature sig = Signature.getInstance("SHA256withRSA");
        sig.initSign(privateKey);
        sig.update(data.getBytes("UTF-8"));
        return Base64.encodeBase64String(sig.sign());
    }
}
```

### Postman Setup (Quick Testing)

For quick testing with Postman, refer to
[API Request Signing — Postman Section](basics/3.request-signing.md#use-postman-to-sign-and-test-api-requests).

---

## 5. Quick Integration Path

If you want to go live quickly, complete integration in this order:

1. Finish onboarding with the CaaS Team
   - share your public key
   - whitelist your server IPs
   - provide your webhook URL
   - provide your merchant-side callback APIs
2. Implement request signing
3. Verify one basic API call in QA
   - Buy: `buy/fiat-list`
   - Sell: `sell/crypto-list`
4. Implement Buy flow end-to-end
5. Implement Sell flow end-to-end
6. Implement webhook verification
7. Complete merchant-side callback API integration
8. Perform QA checklist and go-live validation

---

## 6. Step-by-Step: Buy Flow Integration

The buy flow allows your users to purchase crypto using fiat currency. Follow these steps in order:

| Step | API                                 | Required | Purpose                                                |
| ---- | ----------------------------------- | -------- | ------------------------------------------------------ |
| 1    | Get Fiat List for Buy               | Yes      | Get supported fiat currencies                          |
| 2    | Get Trading Pair                    | Yes      | Get available crypto list for selected fiat            |
| 3    | Get Fiat/Crypto Amount Limit        | Optional | Validate min/max amount before quote                   |
| 4    | Get Quote                           | Yes      | Get executable quote                                   |
| 5    | _(Merchant internal)_ Transfer fiat | Yes      | Transfer user's fiat to Binance's account on your side |
| 6    | Execute Quote                       | Yes      | Create order                                           |
| 7    | Get Single Transaction / Webhook    | Yes      | Track final order status                               |

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            BUY FLOW OVERVIEW                                 │
│                                                                              │
│  Step 1        Step 2         Step 3       Step 4       Step 5      Step 6   │
│ Get Fiat ──► Get Trading ──► Get Amount ──► Get ──────► Transfer ──► Execute │
│ List         Pair             Limits        Quote       Fiat        Quote    │
│                               (optional)               (internal)           │
│                                                                    │         │
│                                                                    ▼         │
│                                                          Step 7: Monitor     │
│                                                          Transaction Status  │
│                                                          (Polling + Webhook) │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Step 1 — Get Available Fiat Currencies

Fetch the list of supported fiat currencies your users can pay with.

```
POST /papi/v1/ramp/connect/prime/buy/fiat-list
```

```json
// Request
{ "userId": "54321123456" }

// Response
{
  "fiatCurrencies": [
    { "currency": "USD", "precision": 2 },
    { "currency": "EUR", "precision": 2 }
  ]
}
```

**Integration tip:** Cache the fiat list locally and refresh periodically (e.g., every few hours).
The supported fiat list rarely changes.

### Step 2 — Get Trading Pairs

After the user selects a fiat currency, fetch the available crypto currencies they can buy.

```
POST /papi/v1/ramp/connect/prime/trading-pair
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "direction": "BUY"
}

// Response
[
  { "fiatCurrency": "EUR", "cryptoCurrency": "BTC", "precision": 8 },
  { "fiatCurrency": "EUR", "cryptoCurrency": "ETH", "precision": 8 }
]
```

**Integration tip:** The `precision` field in the response indicates the decimal places for the
**crypto** amount in the BUY direction. Use this to format display values and validate user inputs.

### Step 3 — Get Amount Limits (Optional but Recommended)

Before the user enters an amount, fetch the min/max limits to provide client-side validation.

```
POST /papi/v1/ramp/connect/prime/fiat-crypto-amount-limit
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "direction": "BUY",
  "amount": 100,
  "amountType": 1,
  "customSpread": 0.01
}

// Response
{
  "fiatMinLimit": "10",
  "fiatMaxLimit": "10000000",
  "cryptoMinLimit": "0.00448887",
  "cryptoMaxLimit": "4488.87147336"
}
```

**Integration tip:** Display the min/max limits in your UI so users know valid ranges upfront.
`amountType` = 1 for fiat amount, 2 for crypto amount.

### About `customSpread`

The `customSpread` parameter represents your markup percentage (e.g., `0.01` = 1% spread). The
allowed range is agreed upon with the CaaS Team during onboarding. You can either:

- Pass a **different value per request** within the allowed range, or
- Have Binance configure a **fixed value** that applies uniformly to all your quotes.

Exceeding the allowed range returns error `1230313` (CUSTOM_SPREAD_EXCEEDED). Contact the Binance
Institutional Crypto Buy/Sell Solution team to confirm your spread configuration.

### Step 4 — Get Quote

Once the user enters a valid amount, request a real-time quote.

```
POST /papi/v1/ramp/connect/prime/quote
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "direction": "BUY",
  "amount": 100,
  "amountType": 1,
  "customSpread": 0.01
}

// Response
{
  "quoteId": "e064b9eacded478192c45110117926aa",
  "totalAmount": "114.70018989",
  "quotePrice": "0.865734",
  "expiredAt": 1756179222140,
  "spreadAmount": "0.99"
}
```

**Critical integration points:**

- `quoteId` is required for the next step (Execute Quote). Store it temporarily.
- `expiredAt` is a millisecond timestamp. You **must** execute the quote before it expires.
- `quotePrice` means: 1 crypto = `quotePrice` fiat.
- `spreadAmount` is your revenue from the spread in fiat currency.
- Use `spreadAmount` for internal revenue calculation, reconciliation, or merchant-side pricing
  analysis as appropriate.
- **UX Recommendation:** Show a countdown timer in your UI based on `expiredAt`. If the quote
  expires, fetch a new one.

### Step 5 — Transfer Fiat to Binance's Account (Merchant Internal)

After the user confirms the quote, **you must transfer the user's fiat to Binance's designated fiat
account on your (merchant) side** before calling Execute Quote.

This is a merchant-internal operation — there is no Binance API call for this step. The transfer
happens within your own banking / payment system.

**Key points:**

- Transfer the exact fiat amount shown in the quote to Binance's fiat account that was set up during
  onboarding.
- This must be completed **before** calling Execute Quote, because Binance will call your
  [Check Transaction API](#91-buy-flow-check-transaction-status-api) to verify the fiat has arrived.
- If Binance's verification confirms the fiat is received, the order proceeds to crypto execution.
- If verification fails or the quote expires after fiat is transferred, Binance will call your
  [Refund API](#92-buy-flow-refund-api) to return the fiat to the user.

### Step 6 — Execute Quote

When the user confirms, execute the quote to create an order.

```
POST /papi/v1/ramp/connect/prime/quote/execute
```

```json
// Request
{
  "quoteId": "e064b9eacded478192c45110117926aa",
  "clientOrderId": "YOUR_UNIQUE_ORDER_ID_001"
}

// Response
{
  "orderId": "lhJ0uBwFPcCkbxnypoqNzUvri1e8jatT",
  "status": "PROCESSING"
}
```

**Critical integration points:**

- `clientOrderId` must be **unique** per order (max 50 chars). Use UUID or your internal order ID.
- You must have completed the fiat transfer in Step 5 before calling this API.
- During execution, Binance will call your
  **[Check Transaction API](#91-buy-flow-check-transaction-status-api)** to verify the fiat has
  arrived.
- If verification fails, Binance will call your **[Refund API](#92-buy-flow-refund-api)** to return
  fiat to the user.
- Store the `orderId` for status tracking.

### Idempotency Guidelines

- Generate a globally unique `clientOrderId` for every execute request.
- Reuse the same internal order identifier when retrying the same business action.
- Make your merchant-side refund / transfer / status APIs idempotent.
- Use `orderId` as the Binance-side primary identifier after order creation.

### Step 7 — Monitor Transaction Status

Use **both** polling and webhooks for reliable status tracking.

**Polling:**

```
POST /papi/v1/ramp/connect/prime/transaction
```

```json
// Request
{ "orderId": "lhJ0uBwFPcCkbxnypoqNzUvri1e8jatT" }
```

**Order Status Reference:**

| Status     | Code | Final? | Description              |
| ---------- | ---- | ------ | ------------------------ |
| PROCESSING | 1    | No     | Order is being processed |
| FILLED     | 20   | Yes    | Transaction completed    |
| FAILED     | 99   | Yes    | Transaction failed       |

**Polling recommendation:** Poll every **3–5 seconds** while the status is `PROCESSING`. Stop when
you receive `FILLED` or `FAILED`.

---

## 7. Step-by-Step: Sell Flow Integration

The sell flow allows your users to sell crypto and receive fiat. The flow is similar to Buy but with
key differences.

| Step | API                              | Required    | Purpose                                           |
| ---- | -------------------------------- | ----------- | ------------------------------------------------- |
| 1    | Get Crypto List for Sell         | Yes         | Get supported crypto currencies for sell          |
| 2    | Get Balance                      | Recommended | Display the user's available crypto balance       |
| 3    | Get Trading Pair                 | Yes         | Get available fiat currencies for selected crypto |
| 4    | Get Fiat/Crypto Amount Limit     | Optional    | Validate min/max amount before quote              |
| 5    | Get Quote                        | Yes         | Get executable quote                              |
| 6    | Execute Quote                    | Yes         | Create order                                      |
| 7    | Get Single Transaction / Webhook | Yes         | Track final order status                          |

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           SELL FLOW OVERVIEW                                 │
│                                                                              │
│  Step 1         Step 2        Step 3        Step 4      Step 5     Step 6    │
│ Get Crypto ──► Get ────────► Get Trading ──► Get ──────► Get ────► Execute   │
│ List           Balance       Pair            Amount      Quote     Quote     │
│                (recommended)                 Limits                          │
│                                              (optional)                      │
│                                                                    │         │
│                                                                    ▼         │
│                                                          Step 7: Monitor     │
│                                                          + Binance calls     │
│                                                          your Transfer API   │
│                                                          on fill             │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Step 1 — Get Available Crypto Currencies

```
POST /papi/v1/ramp/connect/prime/sell/crypto-list
```

```json
// Request
{ "userId": "54321123456" }

// Response
{
  "cryptoCurrencies": [
    { "cryptoCurrency": "BTC", "precision": 8 },
    { "cryptoCurrency": "ETH", "precision": 8 }
  ]
}
```

### Step 2 — Get Trading Pairs (for Sell direction)

```json
// Request
{
  "userId": "54321123456",
  "cryptoCurrency": "BTC",
  "direction": "SELL"
}
```

**Note:** For SELL, the `precision` in the response refers to the **fiat** currency precision.

### Steps 3–6

The remaining steps (Get Amount Limits → Get Quote → Execute Quote → Monitor) follow the same
pattern as the Buy flow (see [Section 6](#6-step-by-step-buy-flow-integration)), with these
differences:

| Aspect             | Buy                                                    | Sell                                                                                                                |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Starting list API  | Get Fiat List (`buy/fiat-list`)                        | Get Crypto List (`sell/crypto-list`)                                                                                |
| Trading pair input | `fiatCurrency` (required)                              | `cryptoCurrency` (required)                                                                                         |
| `direction` value  | `"BUY"`                                                | `"SELL"`                                                                                                            |
| Precision meaning  | Crypto precision                                       | Fiat precision                                                                                                      |
| Pre-execute step   | Merchant must transfer fiat to Binance's account first | No manual transfer needed — crypto is automatically deducted from the user's Binance sub-account upon Execute Quote |
| Post-fill callback | N/A                                                    | Binance calls your **Transfer API**                                                                                 |
| Balance check      | Fiat balance (your side)                               | Crypto balance (use Get Balance API)                                                                                |

> **Key difference from Buy flow:** In the sell flow, there is no need to transfer crypto before
> executing the quote. When you call Execute Quote, Binance will **automatically deduct** the crypto
> from the user's Binance sub-account. This is different from the buy flow, where you must transfer
> fiat to Binance's account before executing.

### Important: Sell Completion

When a sell order is **FILLED**, Binance will automatically call your
**[Transfer API](#93-sell-flow-transfer-api)** to instruct you to transfer fiat to the user's
account.

---

## 8. Webhook Integration

Webhooks provide **real-time push notifications** for order status changes. You should use webhooks
**alongside polling** for maximum reliability.

### Setup

1. Provide your **webhook callback URL** (HTTPS) to the CaaS Team during onboarding.
2. Binance will provide you with a **webhook public key** for signature verification.

### Incoming Webhook Request

**Headers:**

| Header                   | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `X-BN-Connect-Timestamp` | Request timestamp                                                |
| `X-BN-Connect-Signature` | Signature: `SHA256withRSA(requestBody + X-BN-Connect-Timestamp)` |
| `X-BN-Connect-For`       | Your Client ID                                                   |

**Body:**

```json
{
  "webhookEventType": "prime_order_event",
  "orderId": "1234567890",
  "clientOrderId": "myOrder001",
  "direction": "BUY",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "fiatAmount": 100,
  "cryptoAmount": 0.00102181,
  "price": 97849.27,
  "status": "FILLED",
  "createTime": 1692951399,
  "settleTime": 1692954999
}
```

### Your Response

Return HTTP **200** with:

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": "OK"
}
```

### Verify Webhook Signature (Critical!)

Always verify the webhook signature to ensure the request is genuinely from Binance. Use the public
key provided by Binance:

```java
public static boolean verifyWebhookSignature(
        String requestBody, String timestamp,
        String signature, String binancePublicKeyBase64) throws Exception {

    // 1. Reconstruct the signed payload
    String payload = requestBody + timestamp;

    // 2. Load Binance's public key
    byte[] keyBytes = Base64.decodeBase64(binancePublicKeyBase64);
    X509EncodedKeySpec spec = new X509EncodedKeySpec(keyBytes);
    PublicKey publicKey = KeyFactory.getInstance("RSA").generatePublic(spec);

    // 3. Verify signature
    Signature sig = Signature.getInstance("SHA256withRSA");
    sig.initVerify(publicKey);
    sig.update(payload.getBytes("UTF-8"));
    return sig.verify(Base64.decodeBase64(signature));
}
```

**Best practices:**

- **Always verify** the signature before processing the webhook.
- **Idempotency:** You may receive duplicate webhooks. Use `orderId` to deduplicate.
- **Return 200 quickly:** Process the webhook asynchronously if your logic is heavy. Binance expects
  a timely response.
- **Webhook status values:** Only `FILLED` and `FAILED` are sent via webhook (terminal states).

---

## 9. Merchant-Side API Implementation

Institutional Crypto Buy/Sell Solution requires you to implement several callback APIs that Binance
will invoke during the order lifecycle.

### 9.1 Buy Flow: Check Transaction Status API

**Purpose:** Binance calls this API to verify that the user's fiat payment has been received on your
side before executing the crypto purchase.

**Requirements:**

- Accept a transaction identifier (e.g., `transactionId` or `orderId`) from Binance.
- Return an exhaustive transaction status enum:

```java
public enum TransactionStatus {
    PENDING,    // Fiat transfer is still processing
    COMPLETED,  // Fiat has been received successfully
    FAILED      // Fiat transfer failed
}
```

**Response example:**

```json
{
  "success": true,
  "code": "000000",
  "data": {
    "transactionId": "txn_123456",
    "status": "COMPLETED"
  }
}
```

### 9.2 Buy Flow: Refund API

**Purpose:** If Binance cannot process the buy order (e.g., quote expired after fiat received),
Binance calls this API to refund fiat back to the user.

**Requirements:**

- Accept a refund request with the original transaction details.
- Process the refund and return a refund reference.
- Also provide a **refund status check endpoint** for Binance to query refund progress.

### 9.3 Sell Flow: Transfer API

**Purpose:** After a sell order is filled, Binance calls this API to instruct you to transfer fiat
to the user's account.

**Requirements:**

- Accept a transfer request with user details and fiat amount.
- Initiate the fiat transfer to the user.
- Also provide a **transfer status check endpoint** for Binance to query transfer progress.

### General API Convention for Merchant APIs

| Aspect          | Recommendation                                                 |
| --------------- | -------------------------------------------------------------- |
| Auth            | Token-based (`Bearer <token>`) or RSA key signing              |
| Response format | JSON with `success`, `code`, `data`, `message` envelope        |
| Idempotency     | Each `transactionId` / `orderId` must be unique and idempotent |
| Environments    | Provide both production and QA/sandbox endpoints               |

> Refer to the full [Merchant Side API Requirements](basics/10.merchant-side-API-requirements.md)
> document for detailed specifications.

---

## 10. Market Data APIs (Optional)

These APIs are useful for building rich UIs with price charts, crypto details, and discovery pages.

| API                    | Endpoint                      | Use Case                                      | Cache |
| ---------------------- | ----------------------------- | --------------------------------------------- | ----- |
| **Get Symbol Detail**  | `POST .../info/symbol-detail` | Display market cap, volume, rank, description | 1 day |
| **Get Kline Data**     | `POST .../info/klines`        | Build candlestick / price charts              | —     |
| **Get Discover Price** | `POST .../info/discover`      | Show trending prices with 24h change %        | 10s   |

> Note: The Discover Price API currently supports `AED` only.

### Kline Intervals

| Interval  | Value |
| --------- | ----- |
| 3 minutes | `3m`  |
| 1 hour    | `1h`  |
| 1 day     | `1d`  |

**Integration tip:** Use the Discover Price API for homepage / portfolio overview screens. Use Kline
Data for detailed chart views.

---

## 11. Error Handling

### Common Response Structure

All API responses follow this envelope:

```json
{
  "success": true,       // true = OK, false = error
  "code": "000000",      // "000000" = success, others = error code
  "data": { ... },       // response payload
  "message": "..."       // error description (when success = false)
}
```

> Note: The common response format is wrapped in a standard envelope: `success`, `code`, `data`,
> `message`. In individual API documents, example payloads may show only the `data` portion for
> readability. During implementation, parse the full response envelope first, then read the business
> payload from `data`.

### Error Code Quick Reference

| Code    | Type                        | Meaning                    | Recommended Action                         |
| ------- | --------------------------- | -------------------------- | ------------------------------------------ |
| 1230101 | SYS_ERROR                   | System error               | Retry with exponential backoff             |
| 1230102 | SYS_BUSY                    | System busy                | Retry after 1–2 seconds                    |
| 1230303 | ILLEGAL_PARAMETERS          | Invalid parameter          | Fix request parameters                     |
| 1230304 | INVALID_DIRECTION           | Invalid direction          | Use `"BUY"` or `"SELL"` only               |
| 1230305 | NO_PAYMENT_METHOD_AVAILABLE | No payment method for pair | Try a different currency pair or direction |
| 1230306 | INVALID_AMOUNT_TYPE         | Invalid amount type        | Use `1` (fiat) or `2` (crypto)             |
| 1230307 | QUOTE_GENERATION_FAILED     | Failed to generate quote   | Retry or try a different pair/amount       |
| 1230308 | QUOTE_CACHE_FAILED          | Internal cache error       | Retry with exponential backoff             |
| 1230309 | DUPLICATE_ORDER_SUBMISSION  | Duplicate order            | Use the existing order's `orderId`         |
| 1230310 | QUOTE_EXPIRED               | Quote expired              | Get a new quote and try again              |
| 1230311 | ORDER_EXECUTION_FAILED      | Execution failed           | Get a new quote and retry                  |
| 1230312 | MERCHANT_NOT_EXIST          | Merchant inactive          | Contact CaaS Team                          |
| 1230313 | CUSTOM_SPREAD_EXCEEDED      | Spread out of bounds       | Adjust `customSpread` within allowed range |
| 1230314 | INVALID_ORDER_STATUS        | Invalid order status       | Check order status before operating        |
| 1230315 | LIMIT_CALCULATION_FAILED    | Limit calculation error    | Check parameters and retry                 |

> Timestamp note: Most request-side timestamps in Institutional Crypto Buy/Sell Solution use
> milliseconds. However, some example response fields in the documentation appear in second-level
> format. During integration, always validate the actual timestamp unit returned by the API in your
> environment before using it for display or reconciliation.

---

## 12. Testing & Go-Live Checklist

### QA Checklist

Before going live, verify the following in the QA environment:

#### Authentication

- [ ] RSA key pair generated; public key shared with Binance
- [ ] Request signing works (verify with a simple call like `buy/fiat-list`)
- [ ] All 5 HTTP headers set correctly; timestamp in **milliseconds**

#### Buy Flow

- [ ] Get Fiat List → Get Trading Pair → Get Quote → Execute Quote — full flow succeeds
- [ ] Order lifecycle verified: `PROCESSING` → `FILLED` / `FAILED`
- [ ] Duplicate `clientOrderId` returns error `1230309`
- [ ] Expired quote returns error `1230310`

#### Sell Flow

- [ ] Get Crypto List → Get Trading Pair → Get Quote → Execute Quote — full flow succeeds
- [ ] Binance successfully calls your Transfer API after order is `FILLED`

#### Merchant-Side APIs

- [ ] Check Transaction Status API responds correctly to Binance
- [ ] Refund API processes refunds successfully
- [ ] Transfer API processes fiat transfers successfully

#### Webhook

- [ ] Webhook signature verification works
- [ ] Handler returns HTTP 200 with `{"returnCode":"SUCCESS","returnMessage":"OK"}`
- [ ] Both `FILLED` and `FAILED` events handled; duplicates deduplicated

#### Error Handling

- [ ] All error codes handled gracefully
- [ ] Quote expiry flow: auto-refresh quote when expired

### Go-Live Steps

1. Complete all QA checklist items above
2. Provide production info to Binance: IP whitelist, webhook URL, merchant API URLs
3. Receive production credentials from Binance: Client ID, Access Token, Webhook Public Key
4. Switch configuration to production base URL and credentials
5. Run smoke tests with small amounts
6. Monitor first few production orders end-to-end
7. Go live

---

## 13. Best Practices

### Security

- **Never expose** your RSA private key, Client ID, or Access Token on the client side
  (browser/mobile). All API calls should be server-to-server.
- **Always verify** webhook signatures before processing.
- Consider rotating keys periodically according to your internal security policy, and notify the
  CaaS Team when updating the public key.
- **Use IP whitelisting** to restrict API access.

### Performance & Reliability

- **Cache static data** (fiat list, crypto list, trading pairs) — these change infrequently.
- **Don't cache quotes** — they are time-sensitive and expire quickly.
- **Use both polling + webhook** for order status — webhook for speed, polling as a fallback.
- Do not rely on webhook as the only source of truth.
- Use webhook for near-real-time user experience updates.
- Use Get Single Transaction or Get Transaction List for reconciliation, recovery, and fallback
  checks.
- **Set appropriate timeouts** (recommend 10–15s) for API calls.
- **Implement circuit breakers** for production resilience.

### UX Recommendations

- Show a **countdown timer** for quote expiry to create urgency and prevent expired quotes.
- Display **amount limits** before users enter amounts to reduce errors.
- Use the **`precision`** field to format crypto/fiat amounts correctly in your UI.
- Provide clear **order status feedback** (processing → success / failure) with appropriate UI
  states.
- Use `spreadAmount` for internal revenue calculation, reconciliation, or merchant-side pricing
  analysis as appropriate.
- If your product design requires fee or markup disclosure, align the display logic with your
  commercial agreement and pricing policy before exposing `spreadAmount` directly to end users.

### Reconciliation

- Implement **T+1 reconciliation** by using the Get Transaction List API to fetch historical orders.
- Store `orderId`, `clientOrderId`, and `settleTime` for accurate reconciliation.
- Match `fiatAmount` and `cryptoAmount` against your internal records.

---

## 14. FAQ

### Q1: What RSA key size should I use?

**A:** Use **2048-bit RSA** keys. Refer to the [API Request Signing](basics/3.request-signing.md)
guide for generation instructions.

### Q2: What happens if my quote expires before I execute it?

**A:** You'll receive error `1230310` (Quote Expired). Simply call the Get Quote API again to get a
fresh quote with a new `quoteId`.

### Q3: Can I use the same `clientOrderId` for multiple orders?

**A:** No. Each `clientOrderId` must be unique (max 50 characters). Reusing one returns error
`1230309` (Duplicate Order Submission).

### Q4: How long do quotes last?

**A:** Quote validity varies. Check the `expiredAt` field (millisecond timestamp) in the quote
response. Always execute before expiry.

### Q5: Do I need to implement all merchant-side APIs?

**A:** Yes, for a complete integration:

- **Buy flow:** Check Transaction Status API + Refund API
- **Sell flow:** Transfer API + a status query endpoint for Binance to check transfer progress
- **Reconciliation:** Historical Transaction List API

### Q6: Will I receive webhooks for `PROCESSING` status?

**A:** No. Webhooks are only sent for **terminal states**: `FILLED` and `FAILED`. Use polling for
intermediate `PROCESSING` status.

### Q7: How should I handle the `customSpread` parameter?

**A:** The `customSpread` value represents your markup percentage. For example, `0.01` = 1% spread.
The `spreadAmount` in the quote response shows your revenue in fiat. The allowed range is configured
by the CaaS Team — exceeding it returns error `1230313`.

### Q8: What's the difference between `orderId` and `clientOrderId`?

**A:**

- `orderId` is generated by Binance — use it for all Binance API calls (Get Transaction, etc.).
- `clientOrderId` is generated by you — use it for internal tracking and reconciliation.

### Q9: How do I test in QA without real money?

**A:** Start in the QA environment first. Contact the CaaS Team for QA base URLs, available test
accounts, and environment-specific testing arrangements.

### Q10: What if my webhook endpoint is down?

**A:** Use the polling mechanism (Get Single Transaction API) as a fallback. Ensure your webhook
endpoint has high availability. Contact CaaS Team about webhook retry policies.

---

## Quick Reference: API Endpoint Summary

| #   | API                    | Method | Endpoint                                               | Section                                                                                             |
| --- | ---------------------- | ------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| 1   | Get Fiat List (Buy)    | POST   | `/papi/v1/ramp/connect/prime/buy/fiat-list`            | Buy                                                                                                 |
| 2   | Get Crypto List (Sell) | POST   | `/papi/v1/ramp/connect/prime/sell/crypto-list`         | Sell                                                                                                |
| 3   | Get Trading Pair       | POST   | `/papi/v1/ramp/connect/prime/trading-pair`             | Both                                                                                                |
| 4   | Get Amount Limits      | POST   | `/papi/v1/ramp/connect/prime/fiat-crypto-amount-limit` | Both                                                                                                |
| 5   | Get Quote              | POST   | `/papi/v1/ramp/connect/prime/quote`                    | Both                                                                                                |
| 6   | Execute Quote          | POST   | `/papi/v1/ramp/connect/prime/quote/execute`            | Both                                                                                                |
| 7   | Get Single Transaction | POST   | `/papi/v1/ramp/connect/prime/transaction`              | Both                                                                                                |
| 8   | Get Transaction List   | POST   | `/papi/v1/ramp/connect/prime/transactions`             | Both                                                                                                |
| 9   | Get Balance            | POST   | Refer to `wallet/asset/user-assets`                    | Used mainly in sell flow to display the user's available crypto balance before placing a sell order |
| 10  | Get Symbol Detail      | POST   | `/papi/v1/ramp/connect/prime/info/symbol-detail`       | Market                                                                                              |
| 11  | Get Kline Data         | POST   | `/papi/v1/ramp/connect/prime/info/klines`              | Market                                                                                              |
| 12  | Get Discover Price     | POST   | `/papi/v1/ramp/connect/prime/info/discover`            | Market                                                                                              |

---

## 15. Documentation Notes

During integration, please note that some examples in the current documentation are simplified or
use slightly different wording. When in doubt, align with:

1. the common response envelope,
2. the actual response returned by the QA environment,
3. and confirmation from the CaaS Team.

---

> **Need help?** Contact the CaaS Team for onboarding support, QA credentials, or technical
> assistance.

---

# Institutional Crypto Buy/Sell Solution — Integration Guideline

> This guideline helps partners (merchants) integrate Institutional Crypto Buy/Sell Solution's Open
> API from scratch. Follow the steps below to go from zero to live.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Onboarding Checklist](#2-onboarding-checklist)
3. [Environment Setup](#3-environment-setup)
4. [Authentication & Request Signing](#4-authentication--request-signing)
5. [Quick Integration Path](#5-quick-integration-path)
6. [Step-by-Step: Buy Flow Integration](#6-step-by-step-buy-flow-integration)
7. [Step-by-Step: Sell Flow Integration](#7-step-by-step-sell-flow-integration)
8. [Webhook Integration](#8-webhook-integration)
9. [Merchant-Side API Implementation](#9-merchant-side-api-implementation)
10. [Market Data APIs (Optional)](#10-market-data-apis-optional)
11. [Error Handling](#11-error-handling)
12. [Testing & Go-Live Checklist](#12-testing--go-live-checklist)
13. [Best Practices](#13-best-practices)
14. [FAQ](#14-faq)
15. [Documentation Notes](#15-documentation-notes)

---

## 1. Before You Begin

### What is Institutional Crypto Buy/Sell Solution?

> **This is a module of [Crypto-As-A-Service (CAAS)](/products/caas/overview).** It assumes you have
> completed CAAS onboarding and are familiar with the CAAS account and asset model. Read the
> [CAAS Overview](/products/caas/overview) before this guideline. Spread for this module is set per
> request through the `customSpread` parameter — see
> [Get quote](/products/institutional-buy-sell/open-apis/5.get-quote).

Institutional Crypto Buy/Sell Solution is a **turnkey crypto Buy/Sell solution** that enables banks,
fintechs, and platforms to offer crypto services directly inside their own apps — without building
complex infrastructure from scratch. Binance handles the liquidity, order execution, and crypto
infrastructure; you keep control over your fiat operations and customer relationships.

### Core Capabilities

| Capability           | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Buy Crypto**       | Users buy crypto with fiat; Binance executes the trade                    |
| **Sell Crypto**      | Users sell crypto for fiat; Binance executes and you handle fiat transfer |
| **Real-Time Quotes** | Fetch live price quotes with custom spread support                        |
| **Transaction Mgmt** | Query single or bulk transactions, monitor status                         |
| **Webhook**          | Receive real-time order status notifications                              |
| **Market Data**      | Kline, discover price, symbol detail for building UIs                     |

### Architecture Overview

```
┌───────────┐         ┌────────────────────┐         ┌─────────────────────┐
│  End User │ ◄─────► │  Your App / API    │ ◄─────► │  Binance            │
│           │         │  (Merchant Side)   │         │  Open API           │
└───────────┘         └────────────────────┘         └─────────────────────┘
                          │                              │
                          │  Merchant APIs               │  Webhook
                          │  (Check Txn / Refund /       │  (Order status
                          │   Transfer)                  │   notifications)
                          ◄──────────────────────────────┘
```

**Key points:**

- All API communication is **server-to-server** (your backend ↔ Binance).
- Most APIs require a `userId` parameter — this is the Binance sub-account ID obtained after
  completing user onboarding via [Binance Link KYC SaaS](/products/kyc-saas/overview). You must
  integrate Binance CaaS first before calling Institutional Crypto Buy/Sell Solution APIs.
- You **MUST** implement merchant-side APIs for Binance to call back (see
  [Section 9](#9-merchant-side-api-implementation)).
- Webhook provides asynchronous order status updates.

---

## 2. Onboarding Checklist

Before calling any API, complete the following with the CaaS Team:

### Items You Provide to Binance

| #   | Item                       | Description                                                                        |
| --- | -------------------------- | ---------------------------------------------------------------------------------- |
| 1   | **RSA Public Key**         | Your public key for API request signing (2048-bit RSA). Keep the private key safe! |
| 2   | **IP Whitelist**           | IP addresses of your servers that will call Binance APIs                           |
| 3   | **Webhook Callback URL**   | The HTTPS endpoint where Binance sends webhook notifications                       |
| 4   | **Merchant-Side API URLs** | Endpoints for Check Transaction, Refund (Buy), and Transfer (Sell)                 |

### Items Binance Provides to You

| #   | Item                   | Description                                                     |
| --- | ---------------------- | --------------------------------------------------------------- |
| 1   | **Client ID**          | Your unique partner identifier (`X-Tesla-ClientId`)             |
| 2   | **Sign Access Token**  | Access token for API authentication (`X-Tesla-SignAccessToken`) |
| 3   | **Webhook Public Key** | Binance's public key for verifying webhook signatures           |

> **Recommendation:** Start integration in the **QA environment** first. Contact the CaaS Team for
> QA base URLs.

---

## 3. Environment Setup

### Base URLs

| Environment | URL                      |
| ----------- | ------------------------ |
| QA          | Please ask for CaaS Team |
| Production  | Please ask for CaaS Team |

### Required HTTP Headers (Every Request)

| Header                    | Value                                             |
| ------------------------- | ------------------------------------------------- |
| `Content-Type`            | `application/json`                                |
| `X-Tesla-ClientId`        | Your Client ID                                    |
| `X-Tesla-SignAccessToken` | Your Sign Access Token                            |
| `X-Tesla-Timestamp`       | Current timestamp in **milliseconds**             |
| `X-Tesla-Signature`       | RSA SHA256 signature of `requestBody + timestamp` |

---

## 4. Authentication & Request Signing

All API requests must be signed with **SHA256withRSA**. The signing payload is:

```
signPayload = JSON_REQUEST_BODY + TIMESTAMP_IN_MILLISECONDS
```

### Step-by-Step Signing

1. **Generate RSA Key Pair** (2048-bit) — keep the private key secret, share the public key with
   Binance.
2. **Prepare the payload**: concatenate the JSON request body (as a string) with the timestamp.
3. **Sign** the payload with your private key using SHA256withRSA.
4. **Base64-encode** the signature.
5. **Set HTTP headers** with the signature, timestamp, client ID, and access token.

### Java Example

```java
import org.apache.commons.codec.binary.Base64;
import java.security.*;
import java.security.spec.PKCS8EncodedKeySpec;

public class BuySellSigner {

    /**
     * Full signing example: build headers for a Institutional Crypto Buy/Sell Solution API request.
     */
    public static Map<String, String> buildHeaders(
            String clientId, String accessToken,
            String privateKeyBase64, String jsonBody) throws Exception {

        long timestamp = System.currentTimeMillis();
        PrivateKey privateKey = loadPrivateKey(privateKeyBase64);
        String signature = sign(jsonBody + timestamp, privateKey);

        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Tesla-ClientId", clientId);
        headers.put("X-Tesla-SignAccessToken", accessToken);
        headers.put("X-Tesla-Timestamp", String.valueOf(timestamp));
        headers.put("X-Tesla-Signature", signature);
        return headers;
    }

    private static PrivateKey loadPrivateKey(String base64Key) throws Exception {
        byte[] keyBytes = Base64.decodeBase64(base64Key);
        PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
        return KeyFactory.getInstance("RSA").generatePrivate(spec);
    }

    private static String sign(String data, PrivateKey privateKey) throws Exception {
        Signature sig = Signature.getInstance("SHA256withRSA");
        sig.initSign(privateKey);
        sig.update(data.getBytes("UTF-8"));
        return Base64.encodeBase64String(sig.sign());
    }
}
```

### Postman Setup (Quick Testing)

For quick testing with Postman, refer to
[API Request Signing — Postman Section](basics/3.request-signing.md#use-postman-to-sign-and-test-api-requests).

---

## 5. Quick Integration Path

If you want to go live quickly, complete integration in this order:

1. Finish onboarding with the CaaS Team
   - share your public key
   - whitelist your server IPs
   - provide your webhook URL
   - provide your merchant-side callback APIs
2. Implement request signing
3. Verify one basic API call in QA
   - Buy: `buy/fiat-list`
   - Sell: `sell/crypto-list`
4. Implement Buy flow end-to-end
5. Implement Sell flow end-to-end
6. Implement webhook verification
7. Complete merchant-side callback API integration
8. Perform QA checklist and go-live validation

---

## 6. Step-by-Step: Buy Flow Integration

The buy flow allows your users to purchase crypto using fiat currency. Follow these steps in order:

| Step | API                                 | Required | Purpose                                                |
| ---- | ----------------------------------- | -------- | ------------------------------------------------------ |
| 1    | Get Fiat List for Buy               | Yes      | Get supported fiat currencies                          |
| 2    | Get Trading Pair                    | Yes      | Get available crypto list for selected fiat            |
| 3    | Get Fiat/Crypto Amount Limit        | Optional | Validate min/max amount before quote                   |
| 4    | Get Quote                           | Yes      | Get executable quote                                   |
| 5    | _(Merchant internal)_ Transfer fiat | Yes      | Transfer user's fiat to Binance's account on your side |
| 6    | Execute Quote                       | Yes      | Create order                                           |
| 7    | Get Single Transaction / Webhook    | Yes      | Track final order status                               |

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            BUY FLOW OVERVIEW                                 │
│                                                                              │
│  Step 1        Step 2         Step 3       Step 4       Step 5      Step 6   │
│ Get Fiat ──► Get Trading ──► Get Amount ──► Get ──────► Transfer ──► Execute │
│ List         Pair             Limits        Quote       Fiat        Quote    │
│                               (optional)               (internal)           │
│                                                                    │         │
│                                                                    ▼         │
│                                                          Step 7: Monitor     │
│                                                          Transaction Status  │
│                                                          (Polling + Webhook) │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Step 1 — Get Available Fiat Currencies

Fetch the list of supported fiat currencies your users can pay with.

```
POST /papi/v1/ramp/connect/prime/buy/fiat-list
```

```json
// Request
{ "userId": "54321123456" }

// Response
{
  "fiatCurrencies": [
    { "currency": "USD", "precision": 2 },
    { "currency": "EUR", "precision": 2 }
  ]
}
```

**Integration tip:** Cache the fiat list locally and refresh periodically (e.g., every few hours).
The supported fiat list rarely changes.

### Step 2 — Get Trading Pairs

After the user selects a fiat currency, fetch the available crypto currencies they can buy.

```
POST /papi/v1/ramp/connect/prime/trading-pair
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "direction": "BUY"
}

// Response
[
  { "fiatCurrency": "EUR", "cryptoCurrency": "BTC", "precision": 8 },
  { "fiatCurrency": "EUR", "cryptoCurrency": "ETH", "precision": 8 }
]
```

**Integration tip:** The `precision` field in the response indicates the decimal places for the
**crypto** amount in the BUY direction. Use this to format display values and validate user inputs.

### Step 3 — Get Amount Limits (Optional but Recommended)

Before the user enters an amount, fetch the min/max limits to provide client-side validation.

```
POST /papi/v1/ramp/connect/prime/fiat-crypto-amount-limit
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "direction": "BUY",
  "amount": 100,
  "amountType": 1,
  "customSpread": 0.01
}

// Response
{
  "fiatMinLimit": "10",
  "fiatMaxLimit": "10000000",
  "cryptoMinLimit": "0.00448887",
  "cryptoMaxLimit": "4488.87147336"
}
```

**Integration tip:** Display the min/max limits in your UI so users know valid ranges upfront.
`amountType` = 1 for fiat amount, 2 for crypto amount.

### About `customSpread`

The `customSpread` parameter represents your markup percentage (e.g., `0.01` = 1% spread). The
allowed range is agreed upon with the CaaS Team during onboarding. You can either:

- Pass a **different value per request** within the allowed range, or
- Have Binance configure a **fixed value** that applies uniformly to all your quotes.

Exceeding the allowed range returns error `1230313` (CUSTOM_SPREAD_EXCEEDED). Contact the Binance
Institutional Crypto Buy/Sell Solution team to confirm your spread configuration.

### Step 4 — Get Quote

Once the user enters a valid amount, request a real-time quote.

```
POST /papi/v1/ramp/connect/prime/quote
```

```json
// Request
{
  "userId": "54321123456",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "direction": "BUY",
  "amount": 100,
  "amountType": 1,
  "customSpread": 0.01
}

// Response
{
  "quoteId": "e064b9eacded478192c45110117926aa",
  "totalAmount": "114.70018989",
  "quotePrice": "0.865734",
  "expiredAt": 1756179222140,
  "spreadAmount": "0.99"
}
```

**Critical integration points:**

- `quoteId` is required for the next step (Execute Quote). Store it temporarily.
- `expiredAt` is a millisecond timestamp. You **must** execute the quote before it expires.
- `quotePrice` means: 1 crypto = `quotePrice` fiat.
- `spreadAmount` is your revenue from the spread in fiat currency.
- Use `spreadAmount` for internal revenue calculation, reconciliation, or merchant-side pricing
  analysis as appropriate.
- **UX Recommendation:** Show a countdown timer in your UI based on `expiredAt`. If the quote
  expires, fetch a new one.

### Step 5 — Transfer Fiat to Binance's Account (Merchant Internal)

After the user confirms the quote, **you must transfer the user's fiat to Binance's designated fiat
account on your (merchant) side** before calling Execute Quote.

This is a merchant-internal operation — there is no Binance API call for this step. The transfer
happens within your own banking / payment system.

**Key points:**

- Transfer the exact fiat amount shown in the quote to Binance's fiat account that was set up during
  onboarding.
- This must be completed **before** calling Execute Quote, because Binance will call your
  [Check Transaction API](#91-buy-flow-check-transaction-status-api) to verify the fiat has arrived.
- If Binance's verification confirms the fiat is received, the order proceeds to crypto execution.
- If verification fails or the quote expires after fiat is transferred, Binance will call your
  [Refund API](#92-buy-flow-refund-api) to return the fiat to the user.

### Step 6 — Execute Quote

When the user confirms, execute the quote to create an order.

```
POST /papi/v1/ramp/connect/prime/quote/execute
```

```json
// Request
{
  "quoteId": "e064b9eacded478192c45110117926aa",
  "clientOrderId": "YOUR_UNIQUE_ORDER_ID_001"
}

// Response
{
  "orderId": "lhJ0uBwFPcCkbxnypoqNzUvri1e8jatT",
  "status": "PROCESSING"
}
```

**Critical integration points:**

- `clientOrderId` must be **unique** per order (max 50 chars). Use UUID or your internal order ID.
- You must have completed the fiat transfer in Step 5 before calling this API.
- During execution, Binance will call your
  **[Check Transaction API](#91-buy-flow-check-transaction-status-api)** to verify the fiat has
  arrived.
- If verification fails, Binance will call your **[Refund API](#92-buy-flow-refund-api)** to return
  fiat to the user.
- Store the `orderId` for status tracking.

### Idempotency Guidelines

- Generate a globally unique `clientOrderId` for every execute request.
- Reuse the same internal order identifier when retrying the same business action.
- Make your merchant-side refund / transfer / status APIs idempotent.
- Use `orderId` as the Binance-side primary identifier after order creation.

### Step 7 — Monitor Transaction Status

Use **both** polling and webhooks for reliable status tracking.

**Polling:**

```
POST /papi/v1/ramp/connect/prime/transaction
```

```json
// Request
{ "orderId": "lhJ0uBwFPcCkbxnypoqNzUvri1e8jatT" }
```

**Order Status Reference:**

| Status     | Code | Final? | Description              |
| ---------- | ---- | ------ | ------------------------ |
| PROCESSING | 1    | No     | Order is being processed |
| FILLED     | 20   | Yes    | Transaction completed    |
| FAILED     | 99   | Yes    | Transaction failed       |

**Polling recommendation:** Poll every **3–5 seconds** while the status is `PROCESSING`. Stop when
you receive `FILLED` or `FAILED`.

---

## 7. Step-by-Step: Sell Flow Integration

The sell flow allows your users to sell crypto and receive fiat. The flow is similar to Buy but with
key differences.

| Step | API                              | Required    | Purpose                                           |
| ---- | -------------------------------- | ----------- | ------------------------------------------------- |
| 1    | Get Crypto List for Sell         | Yes         | Get supported crypto currencies for sell          |
| 2    | Get Balance                      | Recommended | Display the user's available crypto balance       |
| 3    | Get Trading Pair                 | Yes         | Get available fiat currencies for selected crypto |
| 4    | Get Fiat/Crypto Amount Limit     | Optional    | Validate min/max amount before quote              |
| 5    | Get Quote                        | Yes         | Get executable quote                              |
| 6    | Execute Quote                    | Yes         | Create order                                      |
| 7    | Get Single Transaction / Webhook | Yes         | Track final order status                          |

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           SELL FLOW OVERVIEW                                 │
│                                                                              │
│  Step 1         Step 2        Step 3        Step 4      Step 5     Step 6    │
│ Get Crypto ──► Get ────────► Get Trading ──► Get ──────► Get ────► Execute   │
│ List           Balance       Pair            Amount      Quote     Quote     │
│                (recommended)                 Limits                          │
│                                              (optional)                      │
│                                                                    │         │
│                                                                    ▼         │
│                                                          Step 7: Monitor     │
│                                                          + Binance calls     │
│                                                          your Transfer API   │
│                                                          on fill             │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Step 1 — Get Available Crypto Currencies

```
POST /papi/v1/ramp/connect/prime/sell/crypto-list
```

```json
// Request
{ "userId": "54321123456" }

// Response
{
  "cryptoCurrencies": [
    { "cryptoCurrency": "BTC", "precision": 8 },
    { "cryptoCurrency": "ETH", "precision": 8 }
  ]
}
```

### Step 2 — Get Trading Pairs (for Sell direction)

```json
// Request
{
  "userId": "54321123456",
  "cryptoCurrency": "BTC",
  "direction": "SELL"
}
```

**Note:** For SELL, the `precision` in the response refers to the **fiat** currency precision.

### Steps 3–6

The remaining steps (Get Amount Limits → Get Quote → Execute Quote → Monitor) follow the same
pattern as the Buy flow (see [Section 6](#6-step-by-step-buy-flow-integration)), with these
differences:

| Aspect             | Buy                                                    | Sell                                                                                                                |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Starting list API  | Get Fiat List (`buy/fiat-list`)                        | Get Crypto List (`sell/crypto-list`)                                                                                |
| Trading pair input | `fiatCurrency` (required)                              | `cryptoCurrency` (required)                                                                                         |
| `direction` value  | `"BUY"`                                                | `"SELL"`                                                                                                            |
| Precision meaning  | Crypto precision                                       | Fiat precision                                                                                                      |
| Pre-execute step   | Merchant must transfer fiat to Binance's account first | No manual transfer needed — crypto is automatically deducted from the user's Binance sub-account upon Execute Quote |
| Post-fill callback | N/A                                                    | Binance calls your **Transfer API**                                                                                 |
| Balance check      | Fiat balance (your side)                               | Crypto balance (use Get Balance API)                                                                                |

> **Key difference from Buy flow:** In the sell flow, there is no need to transfer crypto before
> executing the quote. When you call Execute Quote, Binance will **automatically deduct** the crypto
> from the user's Binance sub-account. This is different from the buy flow, where you must transfer
> fiat to Binance's account before executing.

### Important: Sell Completion

When a sell order is **FILLED**, Binance will automatically call your
**[Transfer API](#93-sell-flow-transfer-api)** to instruct you to transfer fiat to the user's
account.

---

## 8. Webhook Integration

Webhooks provide **real-time push notifications** for order status changes. You should use webhooks
**alongside polling** for maximum reliability.

### Setup

1. Provide your **webhook callback URL** (HTTPS) to the CaaS Team during onboarding.
2. Binance will provide you with a **webhook public key** for signature verification.

### Incoming Webhook Request

**Headers:**

| Header                   | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `X-BN-Connect-Timestamp` | Request timestamp                                                |
| `X-BN-Connect-Signature` | Signature: `SHA256withRSA(requestBody + X-BN-Connect-Timestamp)` |
| `X-BN-Connect-For`       | Your Client ID                                                   |

**Body:**

```json
{
  "webhookEventType": "prime_order_event",
  "orderId": "1234567890",
  "clientOrderId": "myOrder001",
  "direction": "BUY",
  "fiatCurrency": "EUR",
  "cryptoCurrency": "BTC",
  "fiatAmount": 100,
  "cryptoAmount": 0.00102181,
  "price": 97849.27,
  "status": "FILLED",
  "createTime": 1692951399,
  "settleTime": 1692954999
}
```

### Your Response

Return HTTP **200** with:

```json
{
  "returnCode": "SUCCESS",
  "returnMessage": "OK"
}
```

### Verify Webhook Signature (Critical!)

Always verify the webhook signature to ensure the request is genuinely from Binance. Use the public
key provided by Binance:

```java
public static boolean verifyWebhookSignature(
        String requestBody, String timestamp,
        String signature, String binancePublicKeyBase64) throws Exception {

    // 1. Reconstruct the signed payload
    String payload = requestBody + timestamp;

    // 2. Load Binance's public key
    byte[] keyBytes = Base64.decodeBase64(binancePublicKeyBase64);
    X509EncodedKeySpec spec = new X509EncodedKeySpec(keyBytes);
    PublicKey publicKey = KeyFactory.getInstance("RSA").generatePublic(spec);

    // 3. Verify signature
    Signature sig = Signature.getInstance("SHA256withRSA");
    sig.initVerify(publicKey);
    sig.update(payload.getBytes("UTF-8"));
    return sig.verify(Base64.decodeBase64(signature));
}
```

**Best practices:**

- **Always verify** the signature before processing the webhook.
- **Idempotency:** You may receive duplicate webhooks. Use `orderId` to deduplicate.
- **Return 200 quickly:** Process the webhook asynchronously if your logic is heavy. Binance expects
  a timely response.
- **Webhook status values:** Only `FILLED` and `FAILED` are sent via webhook (terminal states).

---

## 9. Merchant-Side API Implementation

Institutional Crypto Buy/Sell Solution requires you to implement several callback APIs that Binance
will invoke during the order lifecycle.

### 9.1 Buy Flow: Check Transaction Status API

**Purpose:** Binance calls this API to verify that the user's fiat payment has been received on your
side before executing the crypto purchase.

**Requirements:**

- Accept a transaction identifier (e.g., `transactionId` or `orderId`) from Binance.
- Return an exhaustive transaction status enum:

```java
public enum TransactionStatus {
    PENDING,    // Fiat transfer is still processing
    COMPLETED,  // Fiat has been received successfully
    FAILED      // Fiat transfer failed
}
```

**Response example:**

```json
{
  "success": true,
  "code": "000000",
  "data": {
    "transactionId": "txn_123456",
    "status": "COMPLETED"
  }
}
```

### 9.2 Buy Flow: Refund API

**Purpose:** If Binance cannot process the buy order (e.g., quote expired after fiat received),
Binance calls this API to refund fiat back to the user.

**Requirements:**

- Accept a refund request with the original transaction details.
- Process the refund and return a refund reference.
- Also provide a **refund status check endpoint** for Binance to query refund progress.

### 9.3 Sell Flow: Transfer API

**Purpose:** After a sell order is filled, Binance calls this API to instruct you to transfer fiat
to the user's account.

**Requirements:**

- Accept a transfer request with user details and fiat amount.
- Initiate the fiat transfer to the user.
- Also provide a **transfer status check endpoint** for Binance to query transfer progress.

### General API Convention for Merchant APIs

| Aspect          | Recommendation                                                 |
| --------------- | -------------------------------------------------------------- |
| Auth            | Token-based (`Bearer <token>`) or RSA key signing              |
| Response format | JSON with `success`, `code`, `data`, `message` envelope        |
| Idempotency     | Each `transactionId` / `orderId` must be unique and idempotent |
| Environments    | Provide both production and QA/sandbox endpoints               |

> Refer to the full [Merchant Side API Requirements](basics/10.merchant-side-API-requirements.md)
> document for detailed specifications.

---

## 10. Market Data APIs (Optional)

These APIs are useful for building rich UIs with price charts, crypto details, and discovery pages.

| API                    | Endpoint                      | Use Case                                      | Cache |
| ---------------------- | ----------------------------- | --------------------------------------------- | ----- |
| **Get Symbol Detail**  | `POST .../info/symbol-detail` | Display market cap, volume, rank, description | 1 day |
| **Get Kline Data**     | `POST .../info/klines`        | Build candlestick / price charts              | —     |
| **Get Discover Price** | `POST .../info/discover`      | Show trending prices with 24h change %        | 10s   |

> Note: The Discover Price API currently supports `AED` only.

### Kline Intervals

| Interval  | Value |
| --------- | ----- |
| 3 minutes | `3m`  |
| 1 hour    | `1h`  |
| 1 day     | `1d`  |

**Integration tip:** Use the Discover Price API for homepage / portfolio overview screens. Use Kline
Data for detailed chart views.

---

## 11. Error Handling

### Common Response Structure

All API responses follow this envelope:

```json
{
  "success": true,       // true = OK, false = error
  "code": "000000",      // "000000" = success, others = error code
  "data": { ... },       // response payload
  "message": "..."       // error description (when success = false)
}
```

> Note: The common response format is wrapped in a standard envelope: `success`, `code`, `data`,
> `message`. In individual API documents, example payloads may show only the `data` portion for
> readability. During implementation, parse the full response envelope first, then read the business
> payload from `data`.

### Error Code Quick Reference

| Code    | Type                        | Meaning                    | Recommended Action                         |
| ------- | --------------------------- | -------------------------- | ------------------------------------------ |
| 1230101 | SYS_ERROR                   | System error               | Retry with exponential backoff             |
| 1230102 | SYS_BUSY                    | System busy                | Retry after 1–2 seconds                    |
| 1230303 | ILLEGAL_PARAMETERS          | Invalid parameter          | Fix request parameters                     |
| 1230304 | INVALID_DIRECTION           | Invalid direction          | Use `"BUY"` or `"SELL"` only               |
| 1230305 | NO_PAYMENT_METHOD_AVAILABLE | No payment method for pair | Try a different currency pair or direction |
| 1230306 | INVALID_AMOUNT_TYPE         | Invalid amount type        | Use `1` (fiat) or `2` (crypto)             |
| 1230307 | QUOTE_GENERATION_FAILED     | Failed to generate quote   | Retry or try a different pair/amount       |
| 1230308 | QUOTE_CACHE_FAILED          | Internal cache error       | Retry with exponential backoff             |
| 1230309 | DUPLICATE_ORDER_SUBMISSION  | Duplicate order            | Use the existing order's `orderId`         |
| 1230310 | QUOTE_EXPIRED               | Quote expired              | Get a new quote and try again              |
| 1230311 | ORDER_EXECUTION_FAILED      | Execution failed           | Get a new quote and retry                  |
| 1230312 | MERCHANT_NOT_EXIST          | Merchant inactive          | Contact CaaS Team                          |
| 1230313 | CUSTOM_SPREAD_EXCEEDED      | Spread out of bounds       | Adjust `customSpread` within allowed range |
| 1230314 | INVALID_ORDER_STATUS        | Invalid order status       | Check order status before operating        |
| 1230315 | LIMIT_CALCULATION_FAILED    | Limit calculation error    | Check parameters and retry                 |

> Timestamp note: Most request-side timestamps in Institutional Crypto Buy/Sell Solution use
> milliseconds. However, some example response fields in the documentation appear in second-level
> format. During integration, always validate the actual timestamp unit returned by the API in your
> environment before using it for display or reconciliation.

---

## 12. Testing & Go-Live Checklist

### QA Checklist

Before going live, verify the following in the QA environment:

#### Authentication

- [ ] RSA key pair generated; public key shared with Binance
- [ ] Request signing works (verify with a simple call like `buy/fiat-list`)
- [ ] All 5 HTTP headers set correctly; timestamp in **milliseconds**

#### Buy Flow

- [ ] Get Fiat List → Get Trading Pair → Get Quote → Execute Quote — full flow succeeds
- [ ] Order lifecycle verified: `PROCESSING` → `FILLED` / `FAILED`
- [ ] Duplicate `clientOrderId` returns error `1230309`
- [ ] Expired quote returns error `1230310`

#### Sell Flow

- [ ] Get Crypto List → Get Trading Pair → Get Quote → Execute Quote — full flow succeeds
- [ ] Binance successfully calls your Transfer API after order is `FILLED`

#### Merchant-Side APIs

- [ ] Check Transaction Status API responds correctly to Binance
- [ ] Refund API processes refunds successfully
- [ ] Transfer API processes fiat transfers successfully

#### Webhook

- [ ] Webhook signature verification works
- [ ] Handler returns HTTP 200 with `{"returnCode":"SUCCESS","returnMessage":"OK"}`
- [ ] Both `FILLED` and `FAILED` events handled; duplicates deduplicated

#### Error Handling

- [ ] All error codes handled gracefully
- [ ] Quote expiry flow: auto-refresh quote when expired

### Go-Live Steps

1. Complete all QA checklist items above
2. Provide production info to Binance: IP whitelist, webhook URL, merchant API URLs
3. Receive production credentials from Binance: Client ID, Access Token, Webhook Public Key
4. Switch configuration to production base URL and credentials
5. Run smoke tests with small amounts
6. Monitor first few production orders end-to-end
7. Go live

---

## 13. Best Practices

### Security

- **Never expose** your RSA private key, Client ID, or Access Token on the client side
  (browser/mobile). All API calls should be server-to-server.
- **Always verify** webhook signatures before processing.
- Consider rotating keys periodically according to your internal security policy, and notify the
  CaaS Team when updating the public key.
- **Use IP whitelisting** to restrict API access.

### Performance & Reliability

- **Cache static data** (fiat list, crypto list, trading pairs) — these change infrequently.
- **Don't cache quotes** — they are time-sensitive and expire quickly.
- **Use both polling + webhook** for order status — webhook for speed, polling as a fallback.
- Do not rely on webhook as the only source of truth.
- Use webhook for near-real-time user experience updates.
- Use Get Single Transaction or Get Transaction List for reconciliation, recovery, and fallback
  checks.
- **Set appropriate timeouts** (recommend 10–15s) for API calls.
- **Implement circuit breakers** for production resilience.

### UX Recommendations

- Show a **countdown timer** for quote expiry to create urgency and prevent expired quotes.
- Display **amount limits** before users enter amounts to reduce errors.
- Use the **`precision`** field to format crypto/fiat amounts correctly in your UI.
- Provide clear **order status feedback** (processing → success / failure) with appropriate UI
  states.
- Use `spreadAmount` for internal revenue calculation, reconciliation, or merchant-side pricing
  analysis as appropriate.
- If your product design requires fee or markup disclosure, align the display logic with your
  commercial agreement and pricing policy before exposing `spreadAmount` directly to end users.

### Reconciliation

- Implement **T+1 reconciliation** by using the Get Transaction List API to fetch historical orders.
- Store `orderId`, `clientOrderId`, and `settleTime` for accurate reconciliation.
- Match `fiatAmount` and `cryptoAmount` against your internal records.

---

## 14. FAQ

### Q1: What RSA key size should I use?

**A:** Use **2048-bit RSA** keys. Refer to the [API Request Signing](basics/3.request-signing.md)
guide for generation instructions.

### Q2: What happens if my quote expires before I execute it?

**A:** You'll receive error `1230310` (Quote Expired). Simply call the Get Quote API again to get a
fresh quote with a new `quoteId`.

### Q3: Can I use the same `clientOrderId` for multiple orders?

**A:** No. Each `clientOrderId` must be unique (max 50 characters). Reusing one returns error
`1230309` (Duplicate Order Submission).

### Q4: How long do quotes last?

**A:** Quote validity varies. Check the `expiredAt` field (millisecond timestamp) in the quote
response. Always execute before expiry.

### Q5: Do I need to implement all merchant-side APIs?

**A:** Yes, for a complete integration:

- **Buy flow:** Check Transaction Status API + Refund API
- **Sell flow:** Transfer API + a status query endpoint for Binance to check transfer progress
- **Reconciliation:** Historical Transaction List API

### Q6: Will I receive webhooks for `PROCESSING` status?

**A:** No. Webhooks are only sent for **terminal states**: `FILLED` and `FAILED`. Use polling for
intermediate `PROCESSING` status.

### Q7: How should I handle the `customSpread` parameter?

**A:** The `customSpread` value represents your markup percentage. For example, `0.01` = 1% spread.
The `spreadAmount` in the quote response shows your revenue in fiat. The allowed range is configured
by the CaaS Team — exceeding it returns error `1230313`.

### Q8: What's the difference between `orderId` and `clientOrderId`?

**A:**

- `orderId` is generated by Binance — use it for all Binance API calls (Get Transaction, etc.).
- `clientOrderId` is generated by you — use it for internal tracking and reconciliation.

### Q9: How do I test in QA without real money?

**A:** Start in the QA environment first. Contact the CaaS Team for QA base URLs, available test
accounts, and environment-specific testing arrangements.

### Q10: What if my webhook endpoint is down?

**A:** Use the polling mechanism (Get Single Transaction API) as a fallback. Ensure your webhook
endpoint has high availability. Contact CaaS Team about webhook retry policies.

---

## Quick Reference: API Endpoint Summary

| #   | API                    | Method | Endpoint                                               | Section                                                                                             |
| --- | ---------------------- | ------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| 1   | Get Fiat List (Buy)    | POST   | `/papi/v1/ramp/connect/prime/buy/fiat-list`            | Buy                                                                                                 |
| 2   | Get Crypto List (Sell) | POST   | `/papi/v1/ramp/connect/prime/sell/crypto-list`         | Sell                                                                                                |
| 3   | Get Trading Pair       | POST   | `/papi/v1/ramp/connect/prime/trading-pair`             | Both                                                                                                |
| 4   | Get Amount Limits      | POST   | `/papi/v1/ramp/connect/prime/fiat-crypto-amount-limit` | Both                                                                                                |
| 5   | Get Quote              | POST   | `/papi/v1/ramp/connect/prime/quote`                    | Both                                                                                                |
| 6   | Execute Quote          | POST   | `/papi/v1/ramp/connect/prime/quote/execute`            | Both                                                                                                |
| 7   | Get Single Transaction | POST   | `/papi/v1/ramp/connect/prime/transaction`              | Both                                                                                                |
| 8   | Get Transaction List   | POST   | `/papi/v1/ramp/connect/prime/transactions`             | Both                                                                                                |
| 9   | Get Balance            | POST   | Refer to `wallet/asset/user-assets`                    | Used mainly in sell flow to display the user's available crypto balance before placing a sell order |
| 10  | Get Symbol Detail      | POST   | `/papi/v1/ramp/connect/prime/info/symbol-detail`       | Market                                                                                              |
| 11  | Get Kline Data         | POST   | `/papi/v1/ramp/connect/prime/info/klines`              | Market                                                                                              |
| 12  | Get Discover Price     | POST   | `/papi/v1/ramp/connect/prime/info/discover`            | Market                                                                                              |

---

## 15. Documentation Notes

During integration, please note that some examples in the current documentation are simplified or
use slightly different wording. When in doubt, align with:

1. the common response envelope,
2. the actual response returned by the QA environment,
3. and confirmation from the CaaS Team.

---

> **Need help?** Contact the CaaS Team for onboarding support, QA credentials, or technical
> assistance.