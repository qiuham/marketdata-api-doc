---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/portfolios
api_type: Guide
updated_at: 2026-07-05 19:22:44.008358
---

# Advanced Trade Portfolios

Advanced Trade API supports trading in [multiple portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios). Portfolios let you create new trading environments and segregate trading strategies, or operate multiple managed accounts. Transfers between portfolios are instantaneous and free.

## Max Number

The maximum number of portfolios allowed is 100.

## API Keys

For each portfolio, you must create a dedicated API key in Coinbase Developer Platform (CDP). Your existing API keys will authenticate all portfolio APIs; however, to limit access to your portfolios, you must use a new [CDP API key](/coinbase-app/authentication-authorization/api-key-authentication). Each API key is scoped to specific portfolio and, unless otherwise noted, can only view and create data that belongs to its own portfolio.

## Deleting Portfolios

Portfolios can be deleted by API only. See [Delete Portfolio](/api-reference/advanced-trade-api/rest-api/portfolios/delete-portfolio). They can be viewed in a read-only state at [coinbase.com/advanced-trade](https://www.coinbase.com/advanced-trade).