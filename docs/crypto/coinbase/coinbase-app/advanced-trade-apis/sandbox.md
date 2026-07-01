---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/sandbox
api_type: Trading
updated_at: 2026-07-01 19:42:51.006326
---

# Advanced Trade API Sandbox

Advanced Trade API offers a static sandbox environment and its use cases are:

  * Users can make API requests to Advanced sandbox API without authentication.
  * Users can make API requests to the sandbox and get the same formatted responses as production.
  * All responses are static and pre-defined.
  * Set custom request header “X-Sandbox:” to trigger pre-defined variance in some endpoints.

## Advanced Trade Sandbox Endpoints

Advanced Trade sandbox endpoint URL: **`https://api-sandbox.coinbase.com/api/v3/brokerage/{resource}`**

Only Accounts and Orders related endpoints are currently available in the sandbox. All responses are mocked but have the same format as production.

## Endpoints

The following table shows available Endpoints.

API| Method| Resource  
---|---|---  
[List Accounts](/api-reference/advanced-trade-api/rest-api/accounts/list-accounts)| GET| `/accounts`  
[Get Account](/api-reference/advanced-trade-api/rest-api/accounts/get-account)| GET| `/accounts/{account_id}`  
[Create Order](/api-reference/advanced-trade-api/rest-api/orders/create-order)| POST| `/orders`  
[Cancel Orders](/api-reference/advanced-trade-api/rest-api/orders/cancel-order)| POST| `/orders/batch_cancel`  
[Edit Order](/api-reference/advanced-trade-api/rest-api/orders/edit-order)| POST| `/orders/edit`  
[Edit Order Preview](/api-reference/advanced-trade-api/rest-api/orders/edit-order-preview)| POST| `/orders/edit_preview`  
[List Orders](/api-reference/advanced-trade-api/rest-api/orders/list-orders)| GET| `/orders/historical/batch`  
[List Fills](/api-reference/advanced-trade-api/rest-api/orders/list-fills)| GET| `/orders/historical/fills`  
[Get Order](/api-reference/advanced-trade-api/rest-api/orders/get-order)| GET| `/orders/historical/{order_id}`  
[Preview Order](/api-reference/advanced-trade-api/rest-api/orders/preview-orders)| POST| `/orders/preview`  
[Close Position](/api-reference/advanced-trade-api/rest-api/orders/close-position)| POST| `/orders/close_position`  
[List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)| GET| `/portfolios`  
[Allocate Portfolio](/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio)| POST| `intx/allocate`  
[Get Perpetuals Portfolio Summary](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary)| GET| `/intx/portfolio/{portfolio_uuid}`  
[List Perpetuals Positions](/api-reference/advanced-trade-api/rest-api/perpetuals/list-perpetuals-positions)| GET| `/intx/positions/{portfolio_uuid}`  
[Get Perpetuals Position](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-position)| GET| `/intx/positions/{portfolio_uuid}/{symbol}`  
[Get Portfolios Balances](/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances)| GET| `/intx/balances/{portfolio_uuid}`  
[Opt In or Out of Multi Asset Collateral](/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out)| POST| `/intx/multi_asset_collateral`  
  
  
The following table shows Endpoints with available request parameters.

API| Method| Resource| Request Parameters  
---|---|---|---  
[Get Account](/api-reference/advanced-trade-api/rest-api/accounts/get-account)| GET| `/accounts/{account_id}`| **account_id** retrieved from [List Accounts](/api-reference/advanced-trade-api/rest-api/accounts/list-accounts)  
[Get Order](/api-reference/advanced-trade-api/rest-api/orders/get-order)| GET| `/orders/historical/{order_id}`| **order_id** : retrieved from [List Orders](/api-reference/advanced-trade-api/rest-api/orders/list-orders)  
[List Orders](/api-reference/advanced-trade-api/rest-api/orders/list-orders)| GET| `/orders/historical/batch`| **order_status** : CANCELLED/OPEN  
[List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)| GET| `/portfolios`| **portfolio_type** : DEFAULT/CONSUMER/INTX  
[Allocate Portfolio](/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio)| POST| `intx/allocate`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
[Get Perpetuals Portfolio Summary](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary)| GET| `/intx/portfolio/{portfolio_uuid}`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
[List Perpetuals Positions](/api-reference/advanced-trade-api/rest-api/perpetuals/list-perpetuals-positions)| GET| `/intx/positions/{portfolio_uuid}`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
[Get Perpetuals Position](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-position)| GET| `/intx/positions/{portfolio_uuid}/{symbol}`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
**symbol** : e.g. ETH-PERP-INTX  
[Get Portfolios Balances](/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances)| GET| `/intx/balances/{portfolio_uuid}`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
[Opt In or Out of Multi Asset Collateral](/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out)| POST| `/intx/multi_asset_collateral`| **portfolio_uuid** : retrieved from [List Portfolios](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)  
  
  
The following table shows available Endpoints returning error responses with required headers.

API| Method| Resource| Error| Header  
---|---|---|---|---  
[Create Order](/api-reference/advanced-trade-api/rest-api/orders/create-order)| POST| `/orders`| INSUFFICIENT_FUND| ”X-Sandbox: PostOrder_insufficient_fund”  
[Cancel Orders](/api-reference/advanced-trade-api/rest-api/orders/cancel-order)| POST| `/orders/batch_cancel`| UNKNOWN_CANCEL_ORDER| ”X-Sandbox: CancelOrders_failure”  
[Edit Order](/api-reference/advanced-trade-api/rest-api/orders/edit-order)| POST| `/orders/edit`| ORDER_NOT_FOUND| ”X-Sandbox: EditOrder_failure”  
[Edit Order Preview](/api-reference/advanced-trade-api/rest-api/orders/edit-order-preview)| POST| `/orders/edit_preview`| ORDER_NOT_FOUND| ”X-Sandbox: PreviewEditOrder_failure”  
[Preview Order](/api-reference/advanced-trade-api/rest-api/orders/preview-orders)| POST| `/orders/preview`| PREVIEW_INSUFFICIENT_FUND| ”X-Sandbox: PreviewOrder_insufficient_fund”  
  
  
**See Also:**

  * [REST API Overview](/coinbase-app/advanced-trade-apis/rest-api)