---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/technical
api_type: Guide
updated_at: 2026-07-16 19:07:54.864409
---

# Technical Migration Guide

Technical guide to trading international derivatives on Coinbase Advanced Trade via the new Deribit-powered gateway

On **September 9, 2026** , Coinbase Advanced is moving international derivatives from INTX onto a Deribit-powered gateway running the next-generation Starbase engine.

For the full API reference — all methods, parameters and schemas — see the [Advanced Trade API reference](/api-reference/advanced-trade-api/rest-api/introduction).

## HTTP API

  * The new gateway is JSON-RPC 2.0 over HTTP (and WebSocket).

    
    
    # Current gateway
    https://api.coinbase.com/api/v3/brokerage
    
    # New gateway
    https://drb.coinbase.com/api/v2
    

These are the schema changes most likely to break an existing integration.

  * **Envelope.** Responses follow JSON-RPC: a top-level result or error object plus the request ID, not a bare REST body.
  * **Numeric values.** Send prices and sizes as JSON numbers, and expect them back as JSON numbers. This differs from the Coinbase spot API, which encodes decimals as decimal strings.
  * **Order size.** `amount` is in the base coin of the instrument, or size in contract units with `contracts`.
  * **Client order ID.** Carried in the `label` field, not a dedicated client-order-ID field. Unlike `client_order_id` today, `label` is not guaranteed unique, so don’t rely on it as an idempotency key.
  * **Instrument names.** Instrument names replace the old symbol field and use a new format (see below).

## WebSocket API

**WebSocket now supports full order entry.** Use WebSocket for trading or event-driven flows — live market data and streams of your orders, positions, and portfolio.

Every JSON-RPC HTTP method can be sent over WebSocket in addition to the dedicated streaming methods.
    
    
    # Current gateway — public
    wss://advanced-trade-ws.coinbase.com
    
    # Current gateway — private
    wss://advanced-trade-ws-user.coinbase.com
    
    # New gateway — public + private
    wss://drb.coinbase.com/ws/api/v2
    

  * **One connection.** The same endpoint carries public market data and your authenticated order flow. Authenticate by calling `public/auth` after connecting; the socket then stays authenticated, and you re-send `public/auth` on it before the session expires.
  * **Subscriptions.** Subscribe to channels by name. Market-data channels cover the order book, ticker, trades, and charts; private channels cover your orders, position changes, and portfolio.
  * **Cancel on Disconnect (CoD).** An opt-in safety mechanism: your orders auto-cancel if the connection drops.
  * **Heartbeats.** The server sends periodic test requests that your client must answer to keep the connection alive. You set the heartbeat interval from `public/set_heartbeat`.

## Symbology

Product| Current| New gateway| Example  
---|---|---|---  
**Perpetuals**| `{BASE}-PERP-INTX`| `{BASE}_USDC-PERPETUAL`| `BTC-PERP-INTX` → `BTC_USDC-PERPETUAL`  
**Options** (new)| —| `{BASE}-{DDMMMYY}-{STRIKE}-{C/P}`| `BTC-25MAR26-100000-C`  
**Dated futures** (new)| —| `{BASE}-{DDMMMYY}`| `BTC-12JUN26`  
  
Discover all tradable instruments via `public/get_instruments`, filtering by kind (future or option).

## Authentication

Keep your CDP API key. You do not need to create a separate trading account or key. Your derivatives traffic routes through the Coinbase gateway, and you authenticate with the same CDP API key you use today. What changes is the auth flow. On the new gateway you exchange your key for a short-lived access token, then send that token with each private request.

Aspect| Current API| New gateway  
---|---|---  
**Key management**|  CDP Portal| Unchanged — CDP Portal, as today  
**Auth flow (HTTP)**|  Sign every request| Exchange your credential once via `public/auth`, then carry the returned access token on each request  
**Auth flow (WebSocket)**|  Sign every request| Authenticate once via `public/auth`; the connection stays authenticated  
  
### Auth example

Exchange your CDP key for an access token, then trade:
    
    
    // public/auth — exchange your CDP key for an access token
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "public/auth",
      "params": { "grant_type": "coinbase_cdp", "token": "<signed_cdp_jwt>" }
    }
    
    // To trade, send the returned access token in the Authorization: Bearer <access_token> header
    // (for websockets the channel is authenticated, see below)
    {
      "jsonrpc": "2.0",
      "id": 2,
      "method": "private/buy",
      "params": {
        "instrument_name": "BTC_USDC-PERPETUAL",
        "amount": 0.001,
        "type": "limit",
        "price": 65000.5
      }
    }
    

  * HTTP

  * WebSocket

![CDP key authentication over HTTP](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-http-fp.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=1d12d48f39983816ab0879def4726d74)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * You need to provide the Deribit access token on each private method call.
  * Refresh the Deribit access token every 15 minutes.

![CDP key authentication over WebSocket](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-ws-fp.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=e44065dec8d63d86311406ca5921c655)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * When you call `public/auth` that authorizes the websocket session, no return token is needed to access private methods.
  * Refresh the websockets authentication before it expires (~50 minutes).

**Tip** : Send `public/auth` as a `POST` with the credential in the request body, so it stays out of URLs, browser history, and access logs. The example below shows the calls.

## Attaching a Take Profit / Stop Loss (OTOCO)

The combined take-profit / stop-loss order is replaced by an entry order with two attached exit legs. Set `linked_order_type` to `one_triggers_one_cancels_other` and supply the legs in `otoco_config`. When the entry fills it places both exits; whichever fills first cancels the other. Each leg returns its own order ID.
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "private/buy",
      "params": {
        "instrument_name": "BTC_USDC-PERPETUAL",
        "amount": 0.1,
        "type": "limit",
        "price": 60000,
        "linked_order_type": "one_triggers_one_cancels_other",
        "otoco_config": [
          { "type": "take_limit",  "direction": "sell", "amount": 0.1, "price": 65000, "trigger": "last_price" },
          { "type": "stop_market", "direction": "sell", "amount": 0.1, "trigger_price": 55000, "trigger": "mark_price" }
        ]
      }
    }
    

## Endpoint mapping

The protocol changes from REST to JSON-RPC 2.0. Instead of calling a REST path, you call a method by name with a parameters object. Send one request per frame, with no batching and a 32 KB maximum per frame.

Action| Current API| New API  
---|---|---  
**Place order**  
 _Side becomes the method_| `POST /orders`| `private/buy`, `private/sell`  
**Edit order**  
 _Edit by label supported_| `POST /orders/edit`| `private/edit`, `private/edit_by_label`  
**Cancel orders**  
 _No cancel-by-ID-list; loop, or cancel all_| `POST /orders/batch_cancel`| `private/cancel`, `private/cancel_all_*`  
 **Close position**| `POST /orders/close_position`| `private/close_position`  
**Order preview**  
 _No simulated fills_| `POST /orders/preview`| —  
**Order history**| `GET /orders/historical/batch`| `private/get_order_history_*`  
 **Order status**| `GET /orders/historical/{id}`| `private/get_order_state`  
**Fills**  
 _Deribit calls fills “user trades”_| `GET /orders/historical/fills`| `private/get_user_trades_*`  
 **Positions**  
 _Filter by currency and kind_| `GET /intx/positions/{uuid}`| `private/get_positions`  
**Account summary**| `GET /intx/portfolio/{uuid}`| `private/get_account_summary`  
**Margin model**| `POST /intx/multi_asset_collateral`| `private/change_margin_model`  
**Instruments**  
 _Filter by currency and kind_| `GET /products`| `public/get_instruments`  
**Order book**| `GET /product_book`| `public/get_order_book`  
**Ticker**| `GET /best_bid_ask`| `public/ticker`  
**Candles**| `GET /products/{id}/candles`| `public/get_tradingview_chart_data`  
  
Method names shown with `*` denote a family — for example, `private/get_order_history_by_currency` and `private/get_order_history_by_instrument`.

## FAQ

My stop-limit order has two different IDs.

Expected. A stop-limit order yields two IDs across its lifecycle — one before trigger and one after. Track both; do not assume a stable single ID.

Why are my order-type and status values lowercase?

Order-type, time-in-force, and status values are lowercase on the new gateway — for example, status `open` and `filled`, not `OPEN` and `FILLED`.

What price do stop and take orders trigger on?

Stop and take orders trigger on `index_price`, `mark_price`, or `last_price` — you choose the trigger source per order.