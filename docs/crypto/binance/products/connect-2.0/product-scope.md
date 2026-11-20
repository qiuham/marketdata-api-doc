---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/connect-2.0/product-scope
api_type: Guide
updated_at: 2026-11-20 18:34:13.259280
---

# Product Scope

Hosted Ramp & Onchain Payment APIs is the Binance Pay Onchain product path for partners integrating
Binance-powered hosted ramp and onchain payment flows.

This product path supports three main use cases:

## 1. On-ramp APIs

On-ramp APIs allow partners to offer a hosted fiat-to-crypto purchase flow. A user can start from
the partner experience, continue through a Binance-powered checkout, complete payment using
supported payment methods, and receive crypto to the configured destination.

This is suitable for wallets, dApps, Web3 apps, and partner platforms that want to offer
fiat-to-crypto access without building their own fiat on-ramp infrastructure.

## 2. Onchain Payment APIs

Onchain Payment APIs allow merchants and partners to accept crypto payments through Binance Pay
Onchain. Users can pay with supported Binance balances, and the payment can be sent onchain to a
merchant-controlled wallet or supported settlement destination.

This is suitable for merchants and platforms that want to accept crypto payments while keeping
settlement outside a Binance merchant account structure where applicable.

## 3. Merchant Payout to Binance Account APIs

Merchant Payout to Binance Account APIs allow platforms to simplify crypto payouts to a user's
Binance account.

With user authorization, Binance provides the relevant Binance deposit address to the partner. The
partner can then pre-fill or route the payout to the correct Binance account destination, reducing
manual address entry and wrong-network risk.

Binance does not initiate the merchant's payout transaction through this capability. The merchant or
partner remains responsible for executing the onchain transfer and handling payout status, fees,
risk controls, and reconciliation on its own side.

## Configuration and add-on capabilities

Hosted Ramp & Onchain Payment APIs may also support configuration options such as Smart Convert
Top-Up, Buy Any Token / Swap, checkout behavior, supported assets, supported networks, payment
method configuration, and partner display settings.

Some capabilities are customized or approval-based. Availability depends on partner type, region,
commercial setup, compliance review, and product enablement.

## Not included in this product path

This product path does not cover Institutional Embedded Buy/Sell Solution or Agentic Payments.

Off-ramp / Sell Crypto is not currently covered in this documentation. Contact your Binance
representative if your integration requires it.

---

# Product Scope

Hosted Ramp & Onchain Payment APIs is the Binance Pay Onchain product path for partners integrating
Binance-powered hosted ramp and onchain payment flows.

This product path supports three main use cases:

## 1. On-ramp APIs

On-ramp APIs allow partners to offer a hosted fiat-to-crypto purchase flow. A user can start from
the partner experience, continue through a Binance-powered checkout, complete payment using
supported payment methods, and receive crypto to the configured destination.

This is suitable for wallets, dApps, Web3 apps, and partner platforms that want to offer
fiat-to-crypto access without building their own fiat on-ramp infrastructure.

## 2. Onchain Payment APIs

Onchain Payment APIs allow merchants and partners to accept crypto payments through Binance Pay
Onchain. Users can pay with supported Binance balances, and the payment can be sent onchain to a
merchant-controlled wallet or supported settlement destination.

This is suitable for merchants and platforms that want to accept crypto payments while keeping
settlement outside a Binance merchant account structure where applicable.

## 3. Merchant Payout to Binance Account APIs

Merchant Payout to Binance Account APIs allow platforms to simplify crypto payouts to a user's
Binance account.

With user authorization, Binance provides the relevant Binance deposit address to the partner. The
partner can then pre-fill or route the payout to the correct Binance account destination, reducing
manual address entry and wrong-network risk.

Binance does not initiate the merchant's payout transaction through this capability. The merchant or
partner remains responsible for executing the onchain transfer and handling payout status, fees,
risk controls, and reconciliation on its own side.

## Configuration and add-on capabilities

Hosted Ramp & Onchain Payment APIs may also support configuration options such as Smart Convert
Top-Up, Buy Any Token / Swap, checkout behavior, supported assets, supported networks, payment
method configuration, and partner display settings.

Some capabilities are customized or approval-based. Availability depends on partner type, region,
commercial setup, compliance review, and product enablement.

## Not included in this product path

This product path does not cover Institutional Embedded Buy/Sell Solution or Agentic Payments.

Off-ramp / Sell Crypto is not currently covered in this documentation. Contact your Binance
representative if your integration requires it.