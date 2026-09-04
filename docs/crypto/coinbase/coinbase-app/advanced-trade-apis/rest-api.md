---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/rest-api
api_type: Trading
updated_at: 2026-09-04 18:56:05.025465
---

# Advanced Trade REST Endpoints

REST endpoints for Advanced Trade across spot, US derivatives, and Global Derivatives.

Public and private methods share one URL on each venue. Send a JWT on the request for private methods.

  * Spot and US Derivatives

  * Global Derivatives

## API Reference

Request schemas, parameters, and examples.

## OpenAPI spec

Download the [OpenAPI spec](/api-reference/advanced-trade-api/rest-api/advanced-trade-spec.yaml).

### URL

`https://api.coinbase.com/api/v3/brokerage`Public and private methods both use this URL.

### Public

Public market data for spot crypto and US futures.

#### Endpoints

Endpoint| Description  
---|---  
[`GET /time`](/api-reference/advanced-trade-api/rest-api/public/get-server-time)| Server time  
[`GET /market/product_book`](/api-reference/advanced-trade-api/rest-api/public/get-public-product-book)| Public order book  
[`GET /market/products`](/api-reference/advanced-trade-api/rest-api/public/list-public-products)| Public product list  
[`GET /market/products/\{product_id\}`](/api-reference/advanced-trade-api/rest-api/public/get-public-product)| Public product  
[`GET /market/products/\{product_id\}/candles`](/api-reference/advanced-trade-api/rest-api/public/get-public-product-candles)| Public candles  
[`GET /market/products/\{product_id\}/ticker`](/api-reference/advanced-trade-api/rest-api/public/get-public-market-trades)| Public trades  
  
#### Notes

  * A JWT is not required.
  * Public responses are cached for 1 second. For live data, use the [WebSocket](/coinbase-app/advanced-trade-apis/websocket/websocket-overview), send `cache-control: no-cache`, or call the private product endpoints.

* * *

### Private

Orders, accounts, portfolios, converts, and US futures.

#### Endpoints

Endpoint| Description  
---|---  
[`GET /accounts`](/api-reference/advanced-trade-api/rest-api/accounts/list-accounts)| The user’s accounts  
[`GET /accounts/\{account_uuid\}`](/api-reference/advanced-trade-api/rest-api/accounts/get-account)| One account  
[`POST /orders`](/api-reference/advanced-trade-api/rest-api/orders/create-order)| Place an order  
[`POST /orders/batch_cancel`](/api-reference/advanced-trade-api/rest-api/orders/cancel-order)| Cancel orders  
[`POST /orders/edit`](/api-reference/advanced-trade-api/rest-api/orders/edit-order)| Edit an order  
[`POST /orders/edit_preview`](/api-reference/advanced-trade-api/rest-api/orders/edit-order-preview)| Preview an order edit  
[`POST /orders/close_position`](/api-reference/advanced-trade-api/rest-api/orders/close-position)| Close a position  
[`GET /orders/historical/batch`](/api-reference/advanced-trade-api/rest-api/orders/list-orders)| Order history  
[`GET /orders/historical/fills`](/api-reference/advanced-trade-api/rest-api/orders/list-fills)| Fill history  
[`GET /orders/historical/\{order_id\}`](/api-reference/advanced-trade-api/rest-api/orders/get-order)| One order  
[`POST /orders/preview`](/api-reference/advanced-trade-api/rest-api/orders/preview-orders)| Preview an order  
[`GET /best_bid_ask`](/api-reference/advanced-trade-api/rest-api/products/get-best-bid-ask)| Best bid and ask  
[`GET /product_book`](/api-reference/advanced-trade-api/rest-api/products/get-product-book)| Order book  
[`GET /products`](/api-reference/advanced-trade-api/rest-api/products/list-products)| Product list  
[`GET /products/\{product_id\}`](/api-reference/advanced-trade-api/rest-api/products/get-product)| One product  
[`GET /products/\{product_id\}/candles`](/api-reference/advanced-trade-api/rest-api/products/get-product-candles)| Product candles  
[`GET /products/\{product_id\}/ticker`](/api-reference/advanced-trade-api/rest-api/products/get-market-trades)| Market trades  
[`GET /transaction_summary`](/api-reference/advanced-trade-api/rest-api/fees/get-transaction-summary)| Fee summary  
[`POST /convert/quote`](/api-reference/advanced-trade-api/rest-api/convert/create-convert-quote)| Create a convert quote  
[`POST /convert/trade/\{trade_id\}`](/api-reference/advanced-trade-api/rest-api/convert/commit-convert-trade)| Commit a convert  
[`GET /convert/trade/\{trade_id\}`](/api-reference/advanced-trade-api/rest-api/convert/get-convert-trade)| One convert  
[`GET /portfolios`](/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios)| The user’s portfolios  
[`POST /portfolios`](/api-reference/advanced-trade-api/rest-api/portfolios/create-portfolio)| Create a portfolio  
[`POST /portfolios/move_funds`](/api-reference/advanced-trade-api/rest-api/portfolios/move-portfolios-funds)| Move funds between portfolios  
[`GET /portfolios/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/portfolios/get-portfolio-breakdown)| Portfolio breakdown  
[`DELETE /portfolios/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/portfolios/delete-portfolio)| Delete a portfolio  
[`PUT /portfolios/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/portfolios/edit-portfolio)| Edit a portfolio  
[`GET /cfm/balance_summary`](/api-reference/advanced-trade-api/rest-api/futures/get-futures-balance-summary)| US futures balances  
[`GET /cfm/positions`](/api-reference/advanced-trade-api/rest-api/futures/list-futures-positions)| US futures positions  
[`GET /cfm/positions/\{product_id\}`](/api-reference/advanced-trade-api/rest-api/futures/get-futures-position)| One US futures position  
[`POST /cfm/sweeps/schedule`](/api-reference/advanced-trade-api/rest-api/futures/schedule-futures-sweep)| Schedule a US futures sweep  
[`GET /cfm/sweeps`](/api-reference/advanced-trade-api/rest-api/futures/list-futures-sweeps)| US futures sweeps  
[`DELETE /cfm/sweeps`](/api-reference/advanced-trade-api/rest-api/futures/cancel-pending-futures-sweep)| Cancel a pending sweep  
[`GET /cfm/intraday/margin_setting`](/api-reference/advanced-trade-api/rest-api/futures/get-intraday-margin-setting)| Intraday margin setting  
[`POST /cfm/intraday/margin_setting`](/api-reference/advanced-trade-api/rest-api/futures/set-intraday-margin-settings)| Set intraday margin  
[`GET /cfm/intraday/current_margin_window`](/api-reference/advanced-trade-api/rest-api/futures/get-current-margin-window)| Current margin window  
[`GET /payment_methods`](/api-reference/advanced-trade-api/rest-api/payment-methods/list-payment-methods)| Payment methods  
[`GET /payment_methods/\{payment_method_id\}`](/api-reference/advanced-trade-api/rest-api/payment-methods/get-payment-method)| One payment method  
[`GET /key_permissions`](/api-reference/advanced-trade-api/rest-api/data-api/get-api-key-permissions)| API key permissions  
[`GET /intx/portfolio/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary)| INTX portfolio summary (deprecated)  
[`GET /intx/positions/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/perpetuals/list-perpetuals-positions)| INTX positions (deprecated)  
[`GET /intx/positions/\{portfolio_uuid\}/\{symbol\}`](/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-position)| One INTX position (deprecated)  
[`GET /intx/balances/\{portfolio_uuid\}`](/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances)| INTX balances (deprecated)  
[`POST /intx/multi_asset_collateral`](/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out)| INTX multi-asset collateral (deprecated)  
[`POST /intx/allocate`](/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio)| Allocate to an INTX portfolio (deprecated)  
  
#### Notes

  * Same URL as the public methods. A CDP JWT is required. See [API key authentication](/coinbase-app/authentication-authorization/api-key-authentication).
  * Endpoints require `view`, `trade`, or `transfer` on the key, depending on the call.
  * `/intx/*` endpoints are the current international-derivatives API. They retire on **September 9, 2026** — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

## API Reference

Hosts, specs, and the Global Derivatives method playground.

## OpenAPI spec

Download the [OpenAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-openapi.json).

### URL

`https://drb.coinbase.com/api/v2`Public and private methods both use this URL. JSON-RPC 2.0 over HTTP.

### Public

Public market data for options, futures, and perpetuals.

#### Endpoints

Endpoint| Description  
---|---  
`public/auth`| Exchange a CDP JWT for an access token  
`public/get_announcements`| Platform notices  
`public/get_block_rfq_trades`| Public Block RFQ trades  
`public/get_book_summary_by_currency`| Book summary for a currency  
`public/get_book_summary_by_instrument`| Book summary for one instrument  
`public/get_combo_details`| One combo’s structure and state  
`public/get_combo_ids`| Available combo IDs  
`public/get_combos`| Active combos for a currency  
`public/get_contract_size`| Contract size for an instrument  
`public/get_currencies`| Supported currencies  
`public/get_delivery_prices`| Historical delivery prices for an index  
`public/get_expirations`| Expiration timestamps  
`public/get_funding_chart_data`| Funding-rate chart for a perpetual  
`public/get_funding_rate_history`| Hourly funding-rate history  
`public/get_funding_rate_value`| Funding rate over a period  
`public/get_historical_volatility`| Historical volatility  
`public/get_index_chart_data`| Index price chart  
`public/get_index_price`| Current index price  
`public/get_index_price_names`| Index names  
`public/get_instrument`| One instrument  
`public/get_instruments`| Tradable instruments  
`public/get_last_settlements_by_currency`| Settlements for a currency  
`public/get_last_settlements_by_instrument`| Settlements for one instrument  
`public/get_last_trades_by_currency`| Public trades for a currency  
`public/get_last_trades_by_currency_and_time`| Public trades for a currency, time range  
`public/get_last_trades_by_instrument`| Public trades for one instrument  
`public/get_last_trades_by_instrument_and_time`| Public trades for one instrument, time range  
`public/get_mark_price_history`| 5-minute mark-price history  
`public/get_order_book`| Order book  
`public/get_order_book_by_instrument_id`| Order book by instrument ID  
`public/get_supported_index_names`| Supported index names  
`public/get_time`| Server time  
`public/get_trade_volumes`| 24h trade volumes  
`public/get_tradingview_chart_data`| Candle data for TradingView  
`public/get_volatility_index_data`| Volatility-index candles  
`public/status`| Locked currencies  
`public/test`| Connection test and server version  
`public/ticker`| 24h ticker  
  
#### Notes

  * Send JSON-RPC 2.0 in the request body. The method name goes in `method`.
  * A JWT is not required, except on `public/auth`.
  * These methods also run on the main WebSocket (`wss://drb.coinbase.com/ws/api/v2`). They are not available on the public streams host.
  * Subscribe, unsubscribe, and heartbeat methods are WebSocket-only. See [WebSocket Endpoints](/coinbase-app/advanced-trade-apis/websocket/websocket-endpoints).

* * *

### Private

The user’s orders, fills, positions, portfolio, and Block RFQs.

**Coming soon.** The Deribit-powered gateway goes live **September 9, 2026**. It is published ahead of cutover so you can plan your integration now — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

#### Endpoints

Endpoint| Description  
---|---  
`private/buy`| Place a buy order  
`private/sell`| Place a sell order  
`private/edit`| Edit an order  
`private/edit_by_label`| Edit an order by label  
`private/cancel`| Cancel one order  
`private/cancel_by_label`| Cancel orders by label  
`private/cancel_all`| Cancel all open orders  
`private/cancel_all_by_currency`| Cancel open orders for a currency  
`private/cancel_all_by_currency_pair`| Cancel open orders for a currency pair  
`private/cancel_all_by_instrument`| Cancel open orders for an instrument  
`private/cancel_all_by_kind_or_type`| Cancel open orders by kind or type  
`private/close_position`| Close a position  
`private/get_open_orders`| All open orders  
`private/get_open_orders_by_currency`| Open orders for a currency  
`private/get_open_orders_by_instrument`| Open orders for an instrument  
`private/get_open_orders_by_label`| Open orders by label  
`private/get_order_state`| One order  
`private/get_order_state_by_label`| Recent orders by label  
`private/get_order_history_by_currency`| Order history for a currency  
`private/get_order_history_by_instrument`| Order history for an instrument  
`private/get_order_margin_by_ids`| Initial margin for orders  
`private/get_trigger_order_history`| Trigger-order history  
`private/get_user_trades_by_currency`| Fills for a currency  
`private/get_user_trades_by_currency_and_time`| Fills for a currency, time range  
`private/get_user_trades_by_instrument`| Fills for an instrument  
`private/get_user_trades_by_instrument_and_time`| Fills for an instrument, time range  
`private/get_user_trades_by_order`| Fills for one order  
`private/get_margins`| Margin for a hypothetical order  
`private/get_account_summaries`| Account summaries by currency  
`private/get_account_summary`| Account summary for one currency  
`private/get_position`| Position for one instrument  
`private/get_positions`| All open positions  
`private/change_margin_model`| Change the margin model  
`private/get_access_log`| API access log  
`private/get_transaction_log`| Transaction log  
`private/get_settlement_history_by_currency`| Settlements for a currency  
`private/get_settlement_history_by_instrument`| Settlements for an instrument  
`private/simulate_portfolio`| Simulated portfolio margin  
`private/pme/simulate`| Portfolio-margin risk matrix  
`private/enable_cancel_on_disconnect`| Enable cancel-on-disconnect  
`private/disable_cancel_on_disconnect`| Disable cancel-on-disconnect  
`private/get_cancel_on_disconnect`| Cancel-on-disconnect setting  
`private/create_combo`| Create a combo  
`private/get_leg_prices`| Prices for each instrument in a combo  
`private/create_block_rfq`| Create a Block RFQ  
`private/cancel_block_rfq`| Cancel a Block RFQ  
`private/accept_block_rfq`| Accept a Block RFQ quote  
`private/cancel_block_rfq_trigger`| Cancel a Block RFQ trigger  
`private/get_block_rfqs`| Block RFQs for the user  
`private/add_block_rfq_quote`| Quote a Block RFQ  
`private/edit_block_rfq_quote`| Edit a Block RFQ quote  
`private/cancel_block_rfq_quote`| Cancel a Block RFQ quote  
`private/cancel_all_block_rfq_quotes`| Cancel all Block RFQ quotes  
`private/get_block_rfq_quotes`| Open Block RFQ quotes  
`private/get_block_rfq_makers`| Available Block RFQ makers  
`private/get_block_rfq_user_info`| Block RFQ identity and rating  
`private/execute_block_trade`| Execute a block trade  
`private/verify_block_trade`| Verify a block trade  
`private/approve_block_trade`| Approve a pending block trade  
`private/reject_block_trade`| Reject a pending block trade  
`private/simulate_block_trade`| Simulate a block trade  
`private/invalidate_block_trade_signature`| Invalidate a block-trade signature  
`private/get_block_trade`| One block trade  
`private/get_block_trades`| The user’s block trades  
`private/get_block_trade_requests`| Pending block-trade requests  
`private/get_broker_trades`| Broker block trades  
`private/get_broker_trade_requests`| Broker block-trade requests  
  
#### Notes

  * Send JSON-RPC 2.0 in the request body. The method name goes in `method`.
  * Same URL as the public methods. Call `public/auth` with a CDP JWT, then send the returned access token as `Authorization: Bearer` on each private method. See the [Technical Migration Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical).
  * These methods also run on the main WebSocket (`wss://drb.coinbase.com/ws/api/v2`). They are not available on the public streams host.
  * Subscribe methods are WebSocket-only. See [WebSocket Endpoints](/coinbase-app/advanced-trade-apis/websocket/websocket-endpoints).