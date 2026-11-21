---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/changelog
api_type: Changelog
updated_at: 2026-11-21 18:33:07.749449
---

# Binance Pay API: Changelog

Last Updated: 2026-11

## 2026-11

Release of a new platform certificate for webhook signatures:

- Release of new API to query the new certificate
  - POST /binancepay/openapi/certificates-new
- New webhook headers BinancePay-Certificate-SN-New and BinancePay-Signature-New, sent next to the
  existing headers once the new certificate is enabled
- Deprecated, to be retired soon: please migrate to the new API and headers
  - POST /binancepay/openapi/certificates
  - Webhook headers BinancePay-Certificate-SN and BinancePay-Signature

## 2025-06

Release of new Webhook Notification: Merchant QR Code

## 2025-02

Modification to existing endpoints:

- A new parameter subMerchantId in Payout API for CP payout order management.
  - POST /binancepay/openapi/payout/transfer
- EUR is no longer supported as order currency, MICA user may use USDC
  - POST /binancepay/openapi/v3/order
  - POST /binancepay/openapi/direct-debit/contract

## 2024-08

Modification to existing endpoints:

- Parameter subMerchantId is now mandatory for CP
  - POST /binancepay/openapi/v3/order
- Release of new API to modify submerchant information
  - POST /binancepay/openapi/submerchant/modify

## 2024-05

EUR is supported as order currency for MICA user per MICA rules

- POST /binancepay/openapi/v3/order
- POST /binancepay/openapi/direct-debit/contract

## 2023-06

Release of new Create Order API version, v3 endpoint

- New mandatory parameter description
  - POST /binancepay/openapi/v3/order

## 2023-01

Release of new Direct debit API for recurring and pre-authorize payment

- POST /binancepay/openapi/direct-debit/contract
- POST /binancepay/openapi/direct-debit/contract/query
- POST /binancepay/openapi/direct-debit/contract/termination
- POST /binancepay/openapi/pay/notify
- POST /binancepay/openapi/pay/apply

## 2022-08

Modification to existing endpoints:

- New option parameter passThroughInfo can be used in the Create Order API for merchant to pass any
  other information of the order
  - POST /binancepay/openapi/v2/order
- New optional parameter webhookUrl can be used in Create Order API for merchant to receive webhook
  notification in another endpoint
  - POST /binancepay/openapi/v2/order

---

# Binance Pay API: Changelog

Last Updated: 2026-11

## 2026-11

Release of a new platform certificate for webhook signatures:

- Release of new API to query the new certificate
  - POST /binancepay/openapi/certificates-new
- New webhook headers BinancePay-Certificate-SN-New and BinancePay-Signature-New, sent next to the
  existing headers once the new certificate is enabled
- Deprecated, to be retired soon: please migrate to the new API and headers
  - POST /binancepay/openapi/certificates
  - Webhook headers BinancePay-Certificate-SN and BinancePay-Signature

## 2025-06

Release of new Webhook Notification: Merchant QR Code

## 2025-02

Modification to existing endpoints:

- A new parameter subMerchantId in Payout API for CP payout order management.
  - POST /binancepay/openapi/payout/transfer
- EUR is no longer supported as order currency, MICA user may use USDC
  - POST /binancepay/openapi/v3/order
  - POST /binancepay/openapi/direct-debit/contract

## 2024-08

Modification to existing endpoints:

- Parameter subMerchantId is now mandatory for CP
  - POST /binancepay/openapi/v3/order
- Release of new API to modify submerchant information
  - POST /binancepay/openapi/submerchant/modify

## 2024-05

EUR is supported as order currency for MICA user per MICA rules

- POST /binancepay/openapi/v3/order
- POST /binancepay/openapi/direct-debit/contract

## 2023-06

Release of new Create Order API version, v3 endpoint

- New mandatory parameter description
  - POST /binancepay/openapi/v3/order

## 2023-01

Release of new Direct debit API for recurring and pre-authorize payment

- POST /binancepay/openapi/direct-debit/contract
- POST /binancepay/openapi/direct-debit/contract/query
- POST /binancepay/openapi/direct-debit/contract/termination
- POST /binancepay/openapi/pay/notify
- POST /binancepay/openapi/pay/apply

## 2022-08

Modification to existing endpoints:

- New option parameter passThroughInfo can be used in the Create Order API for merchant to pass any
  other information of the order
  - POST /binancepay/openapi/v2/order
- New optional parameter webhookUrl can be used in Create Order API for merchant to receive webhook
  notification in another endpoint
  - POST /binancepay/openapi/v2/order