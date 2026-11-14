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
source_url: 'https://docs.kraken.com/institutional/changelog'
updated_at: 2026-11-13
---

# Release notes

> A history of changes to Kraken's Institutional APIs

## 2026

### 4 November 2026 — Prime REST permissions

* API keys that belong to an organization now need the **Prime Ops** permission for `CreatePrimeSettlementBatch`, `SettlePrimeSettlementBatchAsset`, and all API user and API user key endpoints. Requests without it are rejected with `EGeneral:Permission denied:prime ops`
* Documented the required API key permissions for the API user and API user key endpoints

### 8 October 2026 — OTC REST v1

* `GetOtcOptionsTradeHistory` now returns `symbol`, `premium_settlement_time`, `expiry_settlement_time`, `scheduled_premium_settlement_time` and `scheduled_expiry_settlement_time`, plus `reference_index` for cash-settled options
* Added the optional `updated_after` request parameter, which returns only trades whose trade, settlement, or close record was updated at or after the given time. `start_date` and `end_date` still apply.
* `symbol` keeps a fractional strike. 2.60 prints as `2.6`

### 7 September 2026 — Prime REST errors

* Corrected Prime REST error examples

### 2 September 2026 — OTC REST v1

* Added `GetOtcSpotTradeHistory` and `GetOtcOptionsTradeHistory` endpoints for retrieving booked OTC trade history
