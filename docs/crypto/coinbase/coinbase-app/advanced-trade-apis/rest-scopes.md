---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/rest-scopes
api_type: Trading
updated_at: 2026-08-30 18:53:03.908997
---

# Advanced Trade Scope & Permissions

Per-endpoint OAuth and API key scopes for Advanced Trade REST.

A CDP API key needs `view`, `trade`, or `transfer`. An OAuth token needs the OAuth scope listed for that endpoint. Public methods need neither. On Global Derivatives, `public/auth` takes a CDP JWT (or OAuth token) in the request to mint the access token — it does not need a key scope.

  * Spot and US Derivatives

  * Global Derivatives

Endpoint| OAuth 2.0 Scope| API Key Scope  
---|---|---  
GET /accounts| `wallet:accounts:read`| `view`  
GET /accounts/{account_uuid}| `wallet:accounts:read`| `view`  
POST /orders| `wallet:buys:create`| `trade`  
POST /orders/batch_cancel| `wallet:buys:create`| `trade`  
POST /orders/edit| `wallet:buys:create`| `trade`  
POST /orders/edit_preview| `wallet:buys:create`| `view`  
POST /orders/close_position| `wallet:buys:create` or `wallet:transactions:read`| `trade`  
GET /orders/historical/batch| `wallet:transactions:read`| `view`  
GET /orders/historical/fills| `wallet:transactions:read`| `view`  
GET /orders/historical/{order_id}| `wallet:transactions:read`| `view`  
POST /orders/preview| `wallet:buys:create`| `view`  
GET /best_bid_ask| `wallet:user:read`| `view`  
GET /product_book| `wallet:user:read`| `view`  
GET /products| `wallet:user:read`| `view`  
GET /products/{product_id}| `wallet:user:read`| `view`  
GET /products/{product_id}/candles| `wallet:user:read`| `view`  
GET /products/{product_id}/ticker| `wallet:user:read`| `view`  
GET /transaction_summary| `wallet:transactions:read`| `view`  
POST /convert/quote| `wallet:trades:create`| `trade`  
POST /convert/trade/{trade_id}| `wallet:trades:create`| `trade`  
GET /convert/trade/{trade_id}| `wallet:trades:read`| `view`  
GET /portfolios| `wallet:accounts:read`| `view`  
POST /portfolios| `wallet:user:update`| `trade`  
POST /portfolios/move_funds| `wallet:transactions:transfer`| `transfer`  
GET /portfolios/{portfolio_uuid}| `wallet:accounts:read`| `view`  
DELETE /portfolios/{portfolio_uuid}| `wallet:accounts:read`| `trade`  
PUT /portfolios/{portfolio_uuid}| `wallet:user:update`| `trade`  
GET /cfm/balance_summary| `wallet:transactions:read`| `view`  
GET /cfm/positions| `wallet:transactions:read`| `view`  
GET /cfm/positions/{product_id}| `wallet:transactions:read`| `view`  
POST /cfm/sweeps/schedule| `wallet:transactions:transfer`| `transfer`  
GET /cfm/sweeps| `wallet:transactions:read`| `view`  
DELETE /cfm/sweeps| `wallet:transactions:transfer`| `transfer`  
GET /cfm/intraday/margin_setting| `wallet:user:read`| `view`  
POST /cfm/intraday/margin_setting| `wallet:user:update`| `trade`  
GET /cfm/intraday/current_margin_window| `wallet:user:read`| `view`  
GET /payment_methods| `wallet:payment-methods:read`| `view`  
GET /payment_methods/{payment_method_id}| `wallet:payment-methods:read`| `view`  
GET /key_permissions| —| `view`  
GET /intx/portfolio/{portfolio_uuid}| `wallet:transactions:read`| `view`  
GET /intx/positions/{portfolio_uuid}| `wallet:transactions:read`| `view`  
GET /intx/positions/{portfolio_uuid}/{symbol}| `wallet:transactions:read`| `view`  
GET /intx/balances/{portfolio_uuid}| `wallet:transactions:read`| `view`  
POST /intx/multi_asset_collateral| `wallet:buys:create`| `trade`  
POST /intx/allocate| `wallet:transactions:transfer`| `transfer`  
  
Endpoint| OAuth 2.0 Scope| API Key Scope  
---|---|---  
private/buy| `wallet:buys:create`| `trade`  
private/sell| `wallet:buys:create`| `trade`  
private/edit| `wallet:buys:create`| `trade`  
private/edit_by_label| `wallet:buys:create`| `trade`  
private/cancel| `wallet:buys:create`| `trade`  
private/cancel_by_label| `wallet:buys:create`| `trade`  
private/cancel_all| `wallet:buys:create`| `trade`  
private/cancel_all_by_currency| `wallet:buys:create`| `trade`  
private/cancel_all_by_currency_pair| `wallet:buys:create`| `trade`  
private/cancel_all_by_instrument| `wallet:buys:create`| `trade`  
private/cancel_all_by_kind_or_type| `wallet:buys:create`| `trade`  
private/close_position| `wallet:buys:create`| `trade`  
private/get_open_orders| `wallet:transactions:read`| `view`  
private/get_open_orders_by_currency| `wallet:transactions:read`| `view`  
private/get_open_orders_by_instrument| `wallet:transactions:read`| `view`  
private/get_open_orders_by_label| `wallet:transactions:read`| `view`  
private/get_order_state| `wallet:transactions:read`| `view`  
private/get_order_state_by_label| `wallet:transactions:read`| `view`  
private/get_order_history_by_currency| `wallet:transactions:read`| `view`  
private/get_order_history_by_instrument| `wallet:transactions:read`| `view`  
private/get_order_margin_by_ids| `wallet:transactions:read`| `view`  
private/get_trigger_order_history| `wallet:transactions:read`| `view`  
private/get_user_trades_by_currency| `wallet:transactions:read`| `view`  
private/get_user_trades_by_currency_and_time| `wallet:transactions:read`| `view`  
private/get_user_trades_by_instrument| `wallet:transactions:read`| `view`  
private/get_user_trades_by_instrument_and_time| `wallet:transactions:read`| `view`  
private/get_user_trades_by_order| `wallet:transactions:read`| `view`  
private/get_margins| `wallet:accounts:read`| `view`  
private/get_account_summaries| `wallet:accounts:read`| `view`  
private/get_account_summary| `wallet:accounts:read`| `view`  
private/get_position| `wallet:accounts:read`| `view`  
private/get_positions| `wallet:accounts:read`| `view`  
private/change_margin_model| `wallet:user:update`| `trade`  
private/get_access_log| `wallet:user:read`| `view`  
private/get_transaction_log| `wallet:transactions:read`| `view`  
private/get_settlement_history_by_currency| `wallet:transactions:read`| `view`  
private/get_settlement_history_by_instrument| `wallet:transactions:read`| `view`  
private/simulate_portfolio| `wallet:accounts:read`| `view`  
private/pme/simulate| `wallet:accounts:read`| `view`  
private/enable_cancel_on_disconnect| `wallet:buys:create`| `trade`  
private/disable_cancel_on_disconnect| `wallet:buys:create`| `trade`  
private/get_cancel_on_disconnect| `wallet:user:read`| `view`  
private/create_combo| `wallet:buys:create`| `trade`  
private/get_leg_prices| `wallet:user:read`| `view`  
private/create_block_rfq| `wallet:buys:create`| `trade`  
private/cancel_block_rfq| `wallet:buys:create`| `trade`  
private/accept_block_rfq| `wallet:buys:create`| `trade`  
private/cancel_block_rfq_trigger| `wallet:buys:create`| `trade`  
private/get_block_rfqs| `wallet:transactions:read`| `view`  
private/add_block_rfq_quote| `wallet:buys:create`| `trade`  
private/edit_block_rfq_quote| `wallet:buys:create`| `trade`  
private/cancel_block_rfq_quote| `wallet:buys:create`| `trade`  
private/cancel_all_block_rfq_quotes| `wallet:buys:create`| `trade`  
private/get_block_rfq_quotes| `wallet:transactions:read`| `view`  
private/get_block_rfq_makers| `wallet:transactions:read`| `view`  
private/get_block_rfq_user_info| `wallet:transactions:read`| `view`  
private/execute_block_trade| `wallet:buys:create`| `trade`  
private/verify_block_trade| `wallet:buys:create`| `trade`  
private/approve_block_trade| `wallet:buys:create`| `trade`  
private/reject_block_trade| `wallet:buys:create`| `trade`  
private/simulate_block_trade| `wallet:transactions:read`| `view`  
private/invalidate_block_trade_signature| `wallet:buys:create`| `trade`  
private/get_block_trade| `wallet:transactions:read`| `view`  
private/get_block_trades| `wallet:transactions:read`| `view`  
private/get_block_trade_requests| `wallet:transactions:read`| `view`  
private/get_broker_trades| `wallet:transactions:read`| `view`  
private/get_broker_trade_requests| `wallet:transactions:read`| `view`