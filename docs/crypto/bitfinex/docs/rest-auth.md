---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/docs/rest-auth'
updated_at: 2026-11-22
---

# Authenticated Endpoints

### URL

Authenticated endpoints should use the following domain: <https://api.bitfinex.com>.

### Authentication

Authenticated endpoints require users to sign their requests using a pair of API-KEY and API-SECRET.
Below you can find several guides to authenticate your HTTP requests using different programming languages.
These examples use the [Submit Order](https://docs.bitfinex.com/reference/rest-auth-submit-order) endpoint but can be easily modified to make requests to other endpoints.

[Examples for more programming languages can be found here.](https://docs.bitfinex.com/recipes)

<Recipe slug="restjavascript-authenticated-request-example" title="[REST][Javascript] Authenticated request example" />

<Recipe slug="restpython-authenticated-request-example" title="[REST][Python] Authenticated request example" />

<Recipe slug="restc-authenticated-request-example" title="[REST][C#] Authenticated request example" />

### REST Authenticated Endpoints

**Wallets**

* [Wallets](https://docs.bitfinex.com/reference/rest-auth-wallets)

**Orders**

* [Retrieve Orders](https://docs.bitfinex.com/reference/rest-auth-retrieve-orders)
* [Retrieve Orders (by symbol)](https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol)
* [Submit Order](https://docs.bitfinex.com/reference/rest-auth-submit-order)
* [Update Order](https://docs.bitfinex.com/reference/rest-auth-update-order)
* [Cancel Order](https://docs.bitfinex.com/reference/rest-auth-cancel-order)
* [Cancel Orders (multiple)](https://docs.bitfinex.com/reference/rest-auth-cancel-orders-multiple)
* [Order Multi-OP](https://docs.bitfinex.com/reference/rest-auth-order-multi)
* [Orders History](https://docs.bitfinex.com/reference/rest-auth-orders-history)
* [Orders History (by symbol)](https://docs.bitfinex.com/reference/rest-auth-orders-history-by-symbol)
* [Order Trades](https://docs.bitfinex.com/reference/rest-auth-order-trades)
* [Trades](https://docs.bitfinex.com/reference/rest-auth-trades)
* [Trades (by symbol)](https://docs.bitfinex.com/reference/rest-auth-trades-by-symbol)
* [OTC Orders History](https://docs.bitfinex.com/reference/otc-orders-history)
* [Ledgers](https://docs.bitfinex.com/reference/rest-auth-ledgers)

**Positions**

* [Margin Info](https://docs.bitfinex.com/reference/rest-auth-info-margin)
* [Retrieve Positions](https://docs.bitfinex.com/reference/rest-auth-positions)
* [Claim Position](https://docs.bitfinex.com/reference/rest-auth-position-claim)
* [Increase Position](https://docs.bitfinex.com/reference/rest-auth-position-increase)
* [Increase Position Info](https://docs.bitfinex.com/reference/rest-auth-increase-position-info)
* [Positions History](https://docs.bitfinex.com/reference/rest-auth-positions-hist)
* [Positions Snapshot](https://docs.bitfinex.com/reference/rest-auth-positions-snap)
* [Positions Audit](https://docs.bitfinex.com/reference/rest-auth-positions-audit)
* [Update Position Funding Type](https://docs.bitfinex.com/reference/update-position-funding-type)
* [Derivative Position Collateral](https://docs.bitfinex.com/reference/rest-auth-deriv-pos-collateral-set)
* [Derivative Position Collateral Limits](https://docs.bitfinex.com/reference/rest-auth-calc-deriv-collateral-limits)

**Margin Funding**

* [Active Funding Offers](https://docs.bitfinex.com/reference/rest-auth-funding-offers)
* [Submit Funding Offer](https://docs.bitfinex.com/reference/rest-auth-submit-funding-offer)
* [Cancel Funding Offer](https://docs.bitfinex.com/reference/rest-auth-cancel-funding-offer)
* [Cancel All Funding Offers](https://docs.bitfinex.com/reference/rest-auth-cancel-all-funding-offers)
* [Funding Close](https://docs.bitfinex.com/reference/rest-auth-funding-close)
* [Funding Auto-renew](https://docs.bitfinex.com/reference/rest-auth-funding-auto-renew)
* [Keep Funding](https://docs.bitfinex.com/reference/rest-auth-keep-funding)
* [Funding Offers History](https://docs.bitfinex.com/reference/rest-auth-funding-offers-hist)
* [Funding Loans](https://docs.bitfinex.com/reference/rest-auth-funding-loans)
* [Funding Loans History](https://docs.bitfinex.com/reference/rest-auth-funding-loans-hist)
* [Funding Credits](https://docs.bitfinex.com/reference/rest-auth-funding-credits)
* [Funding Credits History](https://docs.bitfinex.com/reference/rest-auth-funding-credits-hist)
* [Funding Trades](https://docs.bitfinex.com/reference/rest-auth-funding-trades-hist)
* [Funding Info](https://docs.bitfinex.com/reference/rest-auth-info-funding)

**Account Actions**

* [User Info](https://docs.bitfinex.com/reference/rest-auth-info-user)
* [Summary](https://docs.bitfinex.com/reference/rest-auth-summary)
* [Login History](https://docs.bitfinex.com/reference/rest-auth-logins-hist)
* [Key Permissions](https://docs.bitfinex.com/reference/key-permissions)
* [Generate Token](https://docs.bitfinex.com/reference/generate-token)
* [Changelog](https://docs.bitfinex.com/reference/rest-auth-audit-hist)
* [Transfer Between Wallets](https://docs.bitfinex.com/reference/rest-auth-transfer)
* [Deposit Address](https://docs.bitfinex.com/reference/rest-auth-deposit-address)
* [Deposit Address List](https://docs.bitfinex.com/reference/deposit-address-all)
* [Generate Invoice](https://docs.bitfinex.com/reference/rest-auth-deposit-invoice)
* [LNX Invoice Payments](https://docs.bitfinex.com/reference/lnx-invoice-payments)
* [Withdrawal](https://docs.bitfinex.com/reference/rest-auth-withdraw)
* [Movements](https://docs.bitfinex.com/reference/rest-auth-movements)
* [Movement info](https://docs.bitfinex.com/reference/movement-info)
* [Alert List](https://docs.bitfinex.com/reference/rest-auth-alerts)
* [Alert Set](https://docs.bitfinex.com/reference/rest-auth-alert-set)
* [Alert Delete](https://docs.bitfinex.com/reference/rest-auth-alert-del)
* [Balance Available for Orders/Offers](https://docs.bitfinex.com/reference/rest-auth-calc-order-avail)
* [User Settings Write](https://docs.bitfinex.com/reference/rest-auth-settings-set)
* [User Settings Read](https://docs.bitfinex.com/reference/rest-auth-settings)
* [User Settings Delete](https://docs.bitfinex.com/reference/rest-auth-settings-del)

**Thalex Derivatives**

* [Thalex Deposit Request](https://docs.bitfinex.com/reference/thalex-deposit-request)
* [Thalex Withdrawal Request](https://docs.bitfinex.com/reference/thalex-withdrawal-request)
* [Thalex Free Transfer Count](https://docs.bitfinex.com/reference/thalex-free-transfer-count)
