---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/connect-2.0/send-primary-mode/send-primary-mode
api_type: Guide
updated_at: 2026-11-23 18:40:39.855147
---

# Onchain Payment APIs

> Legacy/internal configuration name: **Send Primary Mode**.

As we know, Binance Pay Onchain has a wide range of application scenarios. In addition to on-ramp
(buy) and off-ramp (sell), Binance Pay Onchain can also be used as a crypto payment channel/tool,
that is, users can directly use the crypto balance in their Binance wallet to make third-party
payments. This is the "send primary mode" we launched.

In send primary mode, the product process and user flow are different from the normal on-ramp (buy),
as follows:

- Send (transfer) crypto will be promoted as the first priority;
- Buy crypto related features will be downgraded and hidden, users don't need to buy crypto, they
  only need to send (transfer) crypto from their Binance wallet;
- Only in one case, when the crypto balance in user's Binance wallet is insufficient, the flow will
  return back to the buy crypto process, to avoid users being blocked here;

## When to use Onchain Payment APIs

Use Onchain Payment APIs when your platform wants users to complete payment using crypto through
Binance Pay Onchain.

This is suitable for merchants, Web3 apps, payment partners, and platforms that want to accept
crypto payments through a Binance-powered flow.

## Core Integration APIs used by this flow

Onchain Payment APIs use the shared [Core Integration APIs](../core-integration-apis/0.overview.md)
for discovery, quote, order creation, order query, and webhook handling:

- Get Supported Trading Pairs
- Get Supported Crypto Networks
- Get Estimated Quote
- Create Order Link
- Query Order Details
- Order Status Webhook

## How to integrate send primary mode

If you are going to integrate send primary mode, please follow these instructions:

1. Contact Binance Pay Onchain team to enable this feature for you (it's disabled by default);
2. Pass `"SEND_PRIMARY": true` or `"SEND_PRIMARY_FLEXIBLE": true` in the `customization` parameter
   of the pre-order API. Please refer to [Customization](../basics/9.customization.md).

### Difference between SEND_PRIMARY and SEND_PRIMARY_FLEXIBLE

- **SEND_PRIMARY**: The crypto amount is locked and fixed based on the amount specified in the
  pre-order API. Users cannot modify the amount on the Binance Pay Onchain page. Should work
  together with `amountType: 2`.
- **SEND_PRIMARY_FLEXIBLE**: The crypto amount specified in the pre-order API will be used as a
  default value, but users can freely input and modify the amount on the Binance Pay Onchain page.
  This provides more flexibility for users to adjust the payment amount as needed.

> **Note**: You should only use either `SEND_PRIMARY` or `SEND_PRIMARY_FLEXIBLE`, not both at the
> same time.

## Typical Send Flow

1. **Initiate Send & Fetch Info**
   - The user initiates a crypto transfer from Binance on the partner's frontend.
   - The partner's backend requests the list of supported crypto networks and trading pairs from
     Binance Pay Onchain.
   - This information is then relayed to the partner's frontend to be displayed to the user.

2. **Confirm & Create Pre-order**
   - The user confirms the details on the partner's frontend.
   - The partner's backend sends a pre-order request to Binance Pay Onchain.
   - Binance Pay Onchain returns a `redirectUrl` in the response.

3. **Redirect to Binance**
   - The partner's frontend redirects the user to the Binance App/website using the `redirectUrl`.

4. **Complete Flow on Binance**
   - The user completes the send process on the Binance platform.
   - Note: If the user's balance is insufficient, the flow will include a buy step before sending.

5. **Webhook Notification**
   - Binance Pay Onchain sends a webhook notification to the partner's backend about the order
     status update.

6. **Query Order Status**
   - The partner's backend can then query the order details from Binance Pay Onchain to get the
     final status of the transaction.

## Diagram

![send-flow.png](../images/send-flow.png)

## Sample Create Order Link payloads

The examples below use
[Core Integration APIs > Create Order Link](../on-ramp-buy-apis/5.pre-order.md) with Onchain Payment
configuration. The endpoint remains `POST /papi/v1/ramp/connect/buy/pre-order`.

### Example 1 — Fixed crypto payment amount with locked amount

Use this pattern when the merchant requires a fixed crypto payment amount and the user should not
edit the amount on the Binance-hosted page.

```jsonc
{
  "externalOrderId": "pay-20260709-001",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "clientType": "web",
  "customization": {
    "SEND_PRIMARY": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 2 — Fixed merchant net receive amount

Use this pattern when the merchant wants the configured destination to receive the requested crypto
amount after applicable network fee handling. Where enabled, `NET_RECEIVE` helps treat the requested
amount as the amount expected to arrive at the destination.

```jsonc
{
  "externalOrderId": "pay-20260709-002",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY": true,
    "NET_RECEIVE": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 3 — Flexible crypto payment amount

Use this pattern when the request should prefill a suggested crypto amount but still allow the user
to adjust the payment amount on the Binance-hosted page.

```jsonc
{
  "externalOrderId": "pay-20260709-003",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY_FLEXIBLE": true,
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 4 — Mobile app payment return flow

Use deep links together with web fallback URLs when the merchant or partner needs to return the user
to a mobile app after payment completion.

```jsonc
{
  "externalOrderId": "pay-20260709-004",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "10",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "redirectDeepLink": "merchantapp://payment/success",
  "failRedirectDeepLink": "merchantapp://payment/failure",
  "clientType": "mobile",
  "customization": {
    "SEND_PRIMARY": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
  },
}
```

### Example 5 — Branded merchant checkout

Use this pattern when the hosted page should show the approved merchant display name, helping users
understand who they are paying.

```jsonc
{
  "externalOrderId": "pay-20260709-005",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "15",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY": true,
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### How to choose between locked amount, flexible amount, and net receive

| Payment need                                         | Recommended pattern                                              | Notes                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| Merchant requires an exact payment amount            | `SEND_PRIMARY: true` + `LOCK_ORDER_ATTRIBUTES`                   | User should not edit the payment amount.                   |
| Merchant wants the destination to receive the amount | `SEND_PRIMARY: true` + `NET_RECEIVE: true`                       | Use where net-receive behavior is enabled.                 |
| User may decide the final amount                     | `SEND_PRIMARY_FLEXIBLE: true`                                    | Useful when the requested amount is a default, not strict. |
| Merchant wants a branded hosted page                 | `MERCHANT_DISPLAY_NAME`                                          | Subject to approval and product enablement.                |
| Mobile app payment flow                              | `redirectDeepLink`, `failRedirectDeepLink`, `clientType: mobile` | Use together with web redirect URLs as fallback.           |

### Mix and match customization

The payloads above are examples of payment patterns. Partners can combine available request fields
and approved customization keys to support different checkout, payment, redirect, branding, and
amount-locking needs.

> **Important:** Do not use `SEND_PRIMARY` and `SEND_PRIMARY_FLEXIBLE` together. Supported payment
> behavior, net-receive behavior, redirect behavior, merchant display name, and checkout
> customization depend on partner enablement and should be confirmed with Binance before production
> use.

---

# Onchain Payment APIs

> Legacy/internal configuration name: **Send Primary Mode**.

As we know, Binance Pay Onchain has a wide range of application scenarios. In addition to on-ramp
(buy) and off-ramp (sell), Binance Pay Onchain can also be used as a crypto payment channel/tool,
that is, users can directly use the crypto balance in their Binance wallet to make third-party
payments. This is the "send primary mode" we launched.

In send primary mode, the product process and user flow are different from the normal on-ramp (buy),
as follows:

- Send (transfer) crypto will be promoted as the first priority;
- Buy crypto related features will be downgraded and hidden, users don't need to buy crypto, they
  only need to send (transfer) crypto from their Binance wallet;
- Only in one case, when the crypto balance in user's Binance wallet is insufficient, the flow will
  return back to the buy crypto process, to avoid users being blocked here;

## When to use Onchain Payment APIs

Use Onchain Payment APIs when your platform wants users to complete payment using crypto through
Binance Pay Onchain.

This is suitable for merchants, Web3 apps, payment partners, and platforms that want to accept
crypto payments through a Binance-powered flow.

## Core Integration APIs used by this flow

Onchain Payment APIs use the shared [Core Integration APIs](../core-integration-apis/0.overview.md)
for discovery, quote, order creation, order query, and webhook handling:

- Get Supported Trading Pairs
- Get Supported Crypto Networks
- Get Estimated Quote
- Create Order Link
- Query Order Details
- Order Status Webhook

## How to integrate send primary mode

If you are going to integrate send primary mode, please follow these instructions:

1. Contact Binance Pay Onchain team to enable this feature for you (it's disabled by default);
2. Pass `"SEND_PRIMARY": true` or `"SEND_PRIMARY_FLEXIBLE": true` in the `customization` parameter
   of the pre-order API. Please refer to [Customization](../basics/9.customization.md).

### Difference between SEND_PRIMARY and SEND_PRIMARY_FLEXIBLE

- **SEND_PRIMARY**: The crypto amount is locked and fixed based on the amount specified in the
  pre-order API. Users cannot modify the amount on the Binance Pay Onchain page. Should work
  together with `amountType: 2`.
- **SEND_PRIMARY_FLEXIBLE**: The crypto amount specified in the pre-order API will be used as a
  default value, but users can freely input and modify the amount on the Binance Pay Onchain page.
  This provides more flexibility for users to adjust the payment amount as needed.

> **Note**: You should only use either `SEND_PRIMARY` or `SEND_PRIMARY_FLEXIBLE`, not both at the
> same time.

## Typical Send Flow

1. **Initiate Send & Fetch Info**
   - The user initiates a crypto transfer from Binance on the partner's frontend.
   - The partner's backend requests the list of supported crypto networks and trading pairs from
     Binance Pay Onchain.
   - This information is then relayed to the partner's frontend to be displayed to the user.

2. **Confirm & Create Pre-order**
   - The user confirms the details on the partner's frontend.
   - The partner's backend sends a pre-order request to Binance Pay Onchain.
   - Binance Pay Onchain returns a `redirectUrl` in the response.

3. **Redirect to Binance**
   - The partner's frontend redirects the user to the Binance App/website using the `redirectUrl`.

4. **Complete Flow on Binance**
   - The user completes the send process on the Binance platform.
   - Note: If the user's balance is insufficient, the flow will include a buy step before sending.

5. **Webhook Notification**
   - Binance Pay Onchain sends a webhook notification to the partner's backend about the order
     status update.

6. **Query Order Status**
   - The partner's backend can then query the order details from Binance Pay Onchain to get the
     final status of the transaction.

## Diagram

![send-flow.png](../images/send-flow.png)

## Sample Create Order Link payloads

The examples below use
[Core Integration APIs > Create Order Link](../on-ramp-buy-apis/5.pre-order.md) with Onchain Payment
configuration. The endpoint remains `POST /papi/v1/ramp/connect/buy/pre-order`.

### Example 1 — Fixed crypto payment amount with locked amount

Use this pattern when the merchant requires a fixed crypto payment amount and the user should not
edit the amount on the Binance-hosted page.

```jsonc
{
  "externalOrderId": "pay-20260709-001",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "clientType": "web",
  "customization": {
    "SEND_PRIMARY": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 2 — Fixed merchant net receive amount

Use this pattern when the merchant wants the configured destination to receive the requested crypto
amount after applicable network fee handling. Where enabled, `NET_RECEIVE` helps treat the requested
amount as the amount expected to arrive at the destination.

```jsonc
{
  "externalOrderId": "pay-20260709-002",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY": true,
    "NET_RECEIVE": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 3 — Flexible crypto payment amount

Use this pattern when the request should prefill a suggested crypto amount but still allow the user
to adjust the payment amount on the Binance-hosted page.

```jsonc
{
  "externalOrderId": "pay-20260709-003",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "25",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY_FLEXIBLE": true,
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### Example 4 — Mobile app payment return flow

Use deep links together with web fallback URLs when the merchant or partner needs to return the user
to a mobile app after payment completion.

```jsonc
{
  "externalOrderId": "pay-20260709-004",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "10",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "redirectDeepLink": "merchantapp://payment/success",
  "failRedirectDeepLink": "merchantapp://payment/failure",
  "clientType": "mobile",
  "customization": {
    "SEND_PRIMARY": true,
    "LOCK_ORDER_ATTRIBUTES": [6],
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
  },
}
```

### Example 5 — Branded merchant checkout

Use this pattern when the hosted page should show the approved merchant display name, helping users
understand who they are paying.

```jsonc
{
  "externalOrderId": "pay-20260709-005",
  "cryptoCurrency": "USDT",
  "amountType": 2,
  "requestedAmount": "15",
  "network": "BSC",
  "address": "0xbb4CdB9CBd3AB01bD10BaEBF2De08d9173bc095c",
  "redirectUrl": "https://merchant.example.com/payment/success",
  "failRedirectUrl": "https://merchant.example.com/payment/failure",
  "customization": {
    "SEND_PRIMARY": true,
    "MERCHANT_DISPLAY_NAME": "Example Merchant",
    "AUTO_REDIRECTION": true,
  },
}
```

### How to choose between locked amount, flexible amount, and net receive

| Payment need                                         | Recommended pattern                                              | Notes                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| Merchant requires an exact payment amount            | `SEND_PRIMARY: true` + `LOCK_ORDER_ATTRIBUTES`                   | User should not edit the payment amount.                   |
| Merchant wants the destination to receive the amount | `SEND_PRIMARY: true` + `NET_RECEIVE: true`                       | Use where net-receive behavior is enabled.                 |
| User may decide the final amount                     | `SEND_PRIMARY_FLEXIBLE: true`                                    | Useful when the requested amount is a default, not strict. |
| Merchant wants a branded hosted page                 | `MERCHANT_DISPLAY_NAME`                                          | Subject to approval and product enablement.                |
| Mobile app payment flow                              | `redirectDeepLink`, `failRedirectDeepLink`, `clientType: mobile` | Use together with web redirect URLs as fallback.           |

### Mix and match customization

The payloads above are examples of payment patterns. Partners can combine available request fields
and approved customization keys to support different checkout, payment, redirect, branding, and
amount-locking needs.

> **Important:** Do not use `SEND_PRIMARY` and `SEND_PRIMARY_FLEXIBLE` together. Supported payment
> behavior, net-receive behavior, redirect behavior, merchant display name, and checkout
> customization depend on partner enablement and should be confirmed with Binance before production
> use.