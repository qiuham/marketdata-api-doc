---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/perps/geographic-restrictions'
updated_at: 2026-11-13
---

# Geographic Restrictions

> Jurisdictions where Polymarket Perps order placement is not permitted

Polymarket restricts order placement from certain geographic locations to comply
with regulatory requirements and international sanctions. Users in restricted
jurisdictions cannot place Perps orders.

## Restricted Jurisdictions

Order placement is not permitted from:

* United States
* Canada
* Cuba
* Iran
* North Korea
* Syria
* Crimea
* Donetsk
* Luhansk

> [!WARNING]
>
> This list can change. Additional restrictions may apply under Polymarket
> notices or applicable law.

## For Builders

If you're integrating Perps, enforce these restrictions before submitting orders
for a user:

* Verify the end user's location before [placing orders](https://docs.polymarket.com/perps/trading.md#place-orders).
* Block order submission entirely for users in any of the listed jurisdictions.
  Do not only display a warning.
* Apply the same check to any flow that results in a new position, including
  programmatic strategies that act on behalf of a user.

Read-only market data is not subject to these restrictions.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
