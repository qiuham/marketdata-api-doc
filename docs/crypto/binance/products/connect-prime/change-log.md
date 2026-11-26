---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/connect-prime/change-log
api_type: Changelog
updated_at: 2026-11-26 18:33:40.430013
---

# Change Log

### Sep 11, 2026

- API request signing now specifies **2048-bit RSA** keys. The guide and its key-generation examples
  previously showed 1024-bit.
- Corrected the `TransactionStatus` example on the merchant side API requirements page. All three
  constants were declared with the same value, which made the statuses indistinguishable.

### Mar 27, 2026

- Added new API endpoint `Get Symbol Detail` for retrieving cryptocurrency details (market cap,
  volume, rank, circulating supply, etc.).
- Added new API endpoint `Get Kline Data` for retrieving K-line/candlestick data with support for
  3m, 1h, 1d intervals.
- Added new API endpoint `Get Discover Price` for retrieving cryptocurrency quotation prices and
  24-hour changes.

### Nov 07, 2025

- Updated typical buy/sell sequence diagrams and flow descriptions.
- Added new merchant side API requirements.
- Added curl examples for all APIs.

### Nov 03, 2025

- Updated the get-fiat-crypto-limits API to include new fields for more accurate limits.

### Oct 20, 2025

- Added new field `webhookEventType` in the webhook payload.

### Oct 15, 2025

- Support 1024-bits RSA keys for enhanced security.

### Sep 30, 2025

- Added new API endpoint for getting fiat and crypto amount limits.
- Updated typical buy/sell sequence diagrams and flow descriptions.
- Removed fiat/crypto amount limit details from get-trading-pair API.

### Sep 22, 2025

- Added typical buy/sell sequence diagrams and flow descriptions.
- Update the get-quote API to replace the request field `spreadLevel` with `customSpread`.

### Sep 05, 2025

- Initial release of Binance Pay Prime with core features and functionalities.

---

# Change Log

### Sep 11, 2026

- API request signing now specifies **2048-bit RSA** keys. The guide and its key-generation examples
  previously showed 1024-bit.
- Corrected the `TransactionStatus` example on the merchant side API requirements page. All three
  constants were declared with the same value, which made the statuses indistinguishable.

### Mar 27, 2026

- Added new API endpoint `Get Symbol Detail` for retrieving cryptocurrency details (market cap,
  volume, rank, circulating supply, etc.).
- Added new API endpoint `Get Kline Data` for retrieving K-line/candlestick data with support for
  3m, 1h, 1d intervals.
- Added new API endpoint `Get Discover Price` for retrieving cryptocurrency quotation prices and
  24-hour changes.

### Nov 07, 2025

- Updated typical buy/sell sequence diagrams and flow descriptions.
- Added new merchant side API requirements.
- Added curl examples for all APIs.

### Nov 03, 2025

- Updated the get-fiat-crypto-limits API to include new fields for more accurate limits.

### Oct 20, 2025

- Added new field `webhookEventType` in the webhook payload.

### Oct 15, 2025

- Support 1024-bits RSA keys for enhanced security.

### Sep 30, 2025

- Added new API endpoint for getting fiat and crypto amount limits.
- Updated typical buy/sell sequence diagrams and flow descriptions.
- Removed fiat/crypto amount limit details from get-trading-pair API.

### Sep 22, 2025

- Added typical buy/sell sequence diagrams and flow descriptions.
- Update the get-quote API to replace the request field `spreadLevel` with `customSpread`.

### Sep 05, 2025

- Initial release of Binance Pay Prime with core features and functionalities.