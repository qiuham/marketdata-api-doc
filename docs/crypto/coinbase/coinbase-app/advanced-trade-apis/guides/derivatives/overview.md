---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/overview
api_type: Guide
updated_at: 2026-11-05 18:53:44.902593
---

# Global Derivatives Overview

Guide to trading Global Derivatives on Advanced Trade

Coinbase International Exchange and Deribit have come together as a unified derivatives platform. On October 1, 2026, Advanced Trade moved international derivatives from INTX onto a Deribit-powered gateway running on the Starbase platform, and INTX perpetuals trading through the Advanced Trade API ended.

## Migration to Deribit Global Derivatives trading

### Who is this guide for:Global Derivatives

# Global Derivatives Overview

Guide to trading Global Derivatives on Advanced Trade

Coinbase International Exchange and Deribit have come together as a unified derivatives platform. On October 1, 2026, Advanced Trade moved international derivatives from INTX onto a Deribit-powered gateway running on the Starbase platform, and INTX perpetuals trading through the Advanced Trade API ended.

## Migration to Deribit Global Derivatives trading

### Who is this guide for:

  * These guides are for new or existing Coinbase retail clients and partners who trade Global Derivatives, including anyone moving an INTX integration to the new gateway.
  * Existing Deribit clients can continue to use Deribit services and APIs as they do today.

### What’s new for you:

  * 125+ perpetual contracts: Including equity and commodity perpetuals
  * Up to 50x maximum leverage
  * Deeper liquidity: Unified order books from a combined global user base
  * Starbase platform: Faster, more scalable, lower-latency execution
  * Options and dated futures are not yet available through the gateway

### What’s changing

  * **New API endpoints.** Derivatives trading runs on a Deribit-powered gateway. The protocol is JSON-RPC 2.0 over HTTP or WebSocket, not REST. Hosts are on the [API reference overview](/api-reference/advanced-trade-api/rest-api/introduction); protocol detail is in the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical).
  * **New products.** 125+ perpetual contracts, including equity and commodity perpetuals, with up to 50x maximum leverage.
  * **A richer trading surface.** New native order types and features are available, including trailing stops, market-limit orders, iceberg orders, and WebSocket order entry.
  * **More order controls.** Choose your margin model per portfolio, trigger stop and take orders on the index, mark, or last price, and auto-cancel resting orders if your WebSocket connection drops (Cancel on Disconnect).

### What’s not changing

  * **Your API key.** Keep your existing CDP API key. There are no new credentials to create, and the same key authenticates to the new gateway.
  * **Spot trading.** Spot API endpoints are unaffected and remain on api.coinbase.com.
  * **Funding.** You fund your derivatives account through Coinbase, as today — see Funding below.
  * **Key management.** API keys are still created and managed in the CDP Portal, as today.

This is a different protocol and order model. Some behaviours change — see Order types below. Plan integration time accordingly.

### Migration Guides

The migration is covered in the 4 guides:

## Overview

This guide covers what changed from INTX: products, order types, margin models, and the migration checklist.

## Technical Guide

The implementation reference: authentication, endpoint and schema mapping, and spec references.

![](https://mintcdn.com/coinbase-prod/phXOVZOc62bKg-Ju/icons/deribit.svg?fit=max&auto=format&n=phXOVZOc62bKg-Ju&q=85&s=2835c105c3254cb649486413884d36c0)

## Deribit Partners Guide

For registered Deribit partners — how the Coinbase integration affects an existing Deribit integration.

## INTX Partners Guide

For partners on Coinbase’s international (INTX) platform moving to the new Deribit-backed service.

## What happened at migration

The migration completed on October 1, 2026. INTX perpetuals trading through the Advanced Trade API ended, and there was no parallel run. An integration that still calls the INTX endpoints to trade must move to the new gateway. Positions and balances migrated automatically, but open orders did not.

  * **Open orders were cancelled.** Resting orders on International Exchange were cancelled at migration. Re-place any you still need on the new gateway.
  * **Positions were settled and recreated.** Open positions settled at the mark price (PnL crystallized, funding paid), then were recreated at the settlement price on the new platform.
  * **Balances transferred.** Collateral moved to your account on the combined platform.

You may see multiple trade records, a reset of your average entry price, and a small PnL variance around the migration. These are standard migration artifacts. No trading or settlement fees were charged for the migration.

## Funding

Funding stays on Coinbase. Only derivatives _trading_ moves to the new gateway. Fund your derivatives portfolio in the same way via the UI or API before you place orders:

  * Retrieve the portfolio’s account ID with `GET /api/v3/brokerage/portfolios`
  * Transfer collateral with `POST /api/v3/brokerage/portfolios/move_funds`.

## Margin models

You choose a margin model per portfolio, and the choice combines two independent settings.

  * **Cross or segregated.** Cross margin pools collateral across all your positions, so a gain on one cushions a loss on another. Segregated (isolated) margin ring-fences collateral to a single position, so a loss there can’t drain the rest of your account.
  * **Portfolio or standard.** Portfolio margin nets the risk of related positions and can lower your total requirement. Standard margin sizes each position’s requirement on its own, with no netting.

The four models combine these two settings:

Model| Plain meaning  
---|---  
Cross, portfolio margin| Pooled collateral, risk netted across positions  
Cross, standard margin| Pooled collateral, each position sized on its own  
Segregated, portfolio margin| Collateral ring-fenced per position, risk netted within it  
Segregated, standard margin| Collateral ring-fenced per position, each sized on its own  
  
Set or change your model with `private/change_margin_model`.

## Order types

Order-type and time-in-force values are renamed and lowercased. The take-profit / stop-loss model also changes shape.

### Order type mapping

Order type| Current value| New gateway value| Notes  
---|---|---|---  
**Limit**| `LIMIT`| `limit`| Direct equivalent  
**Market**| `MARKET`| `market`| Direct equivalent  
**Stop (market)**| `STOP`| `stop_market`| Same behaviour, new name  
**Stop limit**| `STOP_LIMIT`| `stop_limit`| Creates two order IDs (pre- and post-trigger)  
**Take-profit / stop-loss**| `TAKE_PROFIT_STOP_LOSS`| `take_limit` \+ `take_market`| Model change — see the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical#attaching-a-take-profit--stop-loss-otoco)  
**Market limit**|  —| `market_limit`| New: fills like market, remainder rests as limit  
**Trailing stop**|  —| `trailing_stop`| New: stop tracks price by offset  
**Iceberg**|  —| `limit` \+ `display_amount`| New: hides part of a resting limit order; the visible slice refreshes as it fills  
  
### Time-in-force

TIF| Current| New gateway| Notes  
---|---|---|---  
**Good-til-cancel**| `GTC`| `good_til_cancelled`| Direct equivalent  
**Immediate-or-cancel**| `IOC`| `immediate_or_cancel`| Direct equivalent  
**Fill-or-kill**| `FOK`| `fill_or_kill`| Direct equivalent  
**Good-til-time**| `GTT`| No equivalent| Closest is `good_til_day` (expires at session end). Custom-expiry resting orders are not supported  
**Good-til-day**|  —| `good_til_day`| New: expires at session end  
  
## Migration checklist

Detailed auth, endpoint, and schema specifics are in the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical). This is the action list:

1

Update base URLs and move to JSON-RPC 2.0

  * REST `https://drb.coinbase.com/api/v2`
  * WebSocket `wss://drb.coinbase.com/ws/api/v2`

Each request carries a method, parameters object, ID, and protocol version. Use REST for request-response, WebSocket for live event-driven flows.

2

Keep your CDP API keys but add the new token exchange

Call `public/auth` with `grant_type: coinbase_cdp`, then cache and refresh the access token before it expires.

3

Update instrument names

Perpetuals become `{BASE}_USDC-PERPETUAL` (for example, `BTC-PERP-INTX` → `BTC_USDC-PERPETUAL`). Discover exact names via `public/get_instruments`.

4

Fund your derivatives account

Confirm collateral is in place via Coinbase before you trade.

5

Send numeric values as numbers

Prices and sizes are JSON numbers in and out; `amount` units follow the instrument.

6

Update order-type and time-in-force values

Switch to the new lowercase names. There is no good-til-time equivalent; use good-til-day or handle expiry yourself.

7

Refactor take-profit / stop-loss to OTOCO

Replace the single combined order with two linked exit orders.

8

Repoint production traffic

Move production traffic to the new gateway. The INTX endpoints no longer accept derivatives orders.

## FAQ

Do I need a separate trading account or API key?

No. You keep your existing Coinbase (CDP) API key and authenticate to the new gateway with it. There is no separate account or key to create.

Can I still trade derivatives on the INTX endpoints?

No. INTX perpetuals trading through the Advanced Trade API ended on October 1, 2026, with no parallel run. Trade on the new gateway.

  * These guides are for new or existing Coinbase retail clients and partners who trade Global Derivatives, including anyone moving an INTX integration to the new gateway.
  * Existing Deribit clients can continue to use Deribit services and APIs as they do today.

### What’s new for you:

  * 125+ perpetual contracts: Including equity and commodity perpetuals
  * Up to 50x maximum leverage
  * Deeper liquidity: Unified order books from a combined global user base
  * Starbase platform: Faster, more scalable, lower-latency execution
  * Options and dated futures are not yet available through the gateway

### What’s changing

  * **New API endpoints.** Derivatives trading runs on a Deribit-powered gateway. The protocol is JSON-RPC 2.0 over HTTP or WebSocket, not REST. Hosts are on the [API reference overview](/api-reference/advanced-trade-api/rest-api/introduction); protocol detail is in the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical).
  * **New products.** 125+ perpetual contracts, including equity and commodity perpetuals, with up to 50x maximum leverage.
  * **A richer trading surface.** New native order types and features are available, including trailing stops, market-limit orders, iceberg orders, and WebSocket order entry.
  * **More order controls.** Choose your margin model per portfolio, trigger stop and take orders on the index, mark, or last price, and auto-cancel resting orders if your WebSocket connection drops (Cancel on Disconnect).

### What’s not changing

  * **Your API key.** Keep your existing CDP API key. There are no new credentials to create, and the same key authenticates to the new gateway.
  * **Spot trading.** Spot API endpoints are unaffected and remain on api.coinbase.com.
  * **Funding.** You fund your derivatives account through Coinbase, as today — see Funding below.
  * **Key management.** API keys are still created and managed in the CDP Portal, as today.

This is a different protocol and order model. Some behaviours change — see Order types below. Plan integration time accordingly.

### Migration Guides

The migration is covered in the 4 guides:

## Overview

This guide covers what changed from INTX: products, order types, margin models, and the migration checklist.

## Technical Guide

The implementation reference: authentication, endpoint and schema mapping, and spec references.

![](https://mintcdn.com/coinbase-prod/phXOVZOc62bKg-Ju/icons/deribit.svg?fit=max&auto=format&n=phXOVZOc62bKg-Ju&q=85&s=2835c105c3254cb649486413884d36c0)

## Deribit Partners Guide

For registered Deribit partners — how the Coinbase integration affects an existing Deribit integration.

## INTX Partners Guide

For partners on Coinbase’s international (INTX) platform moving to the new Deribit-backed service.

## What happened at migration

The migration completed on October 1, 2026. INTX perpetuals trading through the Advanced Trade API ended, and there was no parallel run. An integration that still calls the INTX endpoints to trade must move to the new gateway. Positions and balances migrated automatically, but open orders did not.

  * **Open orders were cancelled.** Resting orders on International Exchange were cancelled at migration. Re-place any you still need on the new gateway.
  * **Positions were settled and recreated.** Open positions settled at the mark price (PnL crystallized, funding paid), then were recreated at the settlement price on the new platform.
  * **Balances transferred.** Collateral moved to your account on the combined platform.

You may see multiple trade records, a reset of your average entry price, and a small PnL variance around the migration. These are standard migration artifacts. No trading or settlement fees were charged for the migration.

## Funding

Funding stays on Coinbase. Only derivatives _trading_ moves to the new gateway. Fund your derivatives portfolio in the same way via the UI or API before you place orders:

  * Retrieve the portfolio’s account ID with `GET /api/v3/brokerage/portfolios`
  * Transfer collateral with `POST /api/v3/brokerage/portfolios/move_funds`.

## Margin models

You choose a margin model per portfolio, and the choice combines two independent settings.

  * **Cross or segregated.** Cross margin pools collateral across all your positions, so a gain on one cushions a loss on another. Segregated (isolated) margin ring-fences collateral to a single position, so a loss there can’t drain the rest of your account.
  * **Portfolio or standard.** Portfolio margin nets the risk of related positions and can lower your total requirement. Standard margin sizes each position’s requirement on its own, with no netting.

The four models combine these two settings:

Model| Plain meaning  
---|---  
Cross, portfolio margin| Pooled collateral, risk netted across positions  
Cross, standard margin| Pooled collateral, each position sized on its own  
Segregated, portfolio margin| Collateral ring-fenced per position, risk netted within it  
Segregated, standard margin| Collateral ring-fenced per position, each sized on its own  
  
Set or change your model with `private/change_margin_model`.

## Order types

Order-type and time-in-force values are renamed and lowercased. The take-profit / stop-loss model also changes shape.

### Order type mapping

Order type| Current value| New gateway value| Notes  
---|---|---|---  
**Limit**| `LIMIT`| `limit`| Direct equivalent  
**Market**| `MARKET`| `market`| Direct equivalent  
**Stop (market)**| `STOP`| `stop_market`| Same behaviour, new name  
**Stop limit**| `STOP_LIMIT`| `stop_limit`| Creates two order IDs (pre- and post-trigger)  
**Take-profit / stop-loss**| `TAKE_PROFIT_STOP_LOSS`| `take_limit` \+ `take_market`| Model change — see the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical#attaching-a-take-profit--stop-loss-otoco)  
**Market limit**|  —| `market_limit`| New: fills like market, remainder rests as limit  
**Trailing stop**|  —| `trailing_stop`| New: stop tracks price by offset  
**Iceberg**|  —| `limit` \+ `display_amount`| New: hides part of a resting limit order; the visible slice refreshes as it fills  
  
### Time-in-force

TIF| Current| New gateway| Notes  
---|---|---|---  
**Good-til-cancel**| `GTC`| `good_til_cancelled`| Direct equivalent  
**Immediate-or-cancel**| `IOC`| `immediate_or_cancel`| Direct equivalent  
**Fill-or-kill**| `FOK`| `fill_or_kill`| Direct equivalent  
**Good-til-time**| `GTT`| No equivalent| Closest is `good_til_day` (expires at session end). Custom-expiry resting orders are not supported  
**Good-til-day**|  —| `good_til_day`| New: expires at session end  
  
## Migration checklist

Detailed auth, endpoint, and schema specifics are in the [Technical Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical). This is the action list:

1

Update base URLs and move to JSON-RPC 2.0

  * REST `https://drb.coinbase.com/api/v2`
  * WebSocket `wss://drb.coinbase.com/ws/api/v2`

Each request carries a method, parameters object, ID, and protocol version. Use REST for request-response, WebSocket for live event-driven flows.

2

Keep your CDP API keys but add the new token exchange

Call `public/auth` with `grant_type: coinbase_cdp`, then cache and refresh the access token before it expires.

3

Update instrument names

Perpetuals become `{BASE}_USDC-PERPETUAL` (for example, `BTC-PERP-INTX` → `BTC_USDC-PERPETUAL`). Discover exact names via `public/get_instruments`.

4

Fund your derivatives account

Confirm collateral is in place via Coinbase before you trade.

5

Send numeric values as numbers

Prices and sizes are JSON numbers in and out; `amount` units follow the instrument.

6

Update order-type and time-in-force values

Switch to the new lowercase names. There is no good-til-time equivalent; use good-til-day or handle expiry yourself.

7

Refactor take-profit / stop-loss to OTOCO

Replace the single combined order with two linked exit orders.

8

What happened to my open orders and positions?

Open orders were cancelled; re-place them on the new gateway. Positions and balances migrated automatically (settled and recreated on the new platform). See What happened at migration.

Is spot trading affected?

No. Your spot integration is unchanged — spot API endpoints remain on `api.coinbase.com`. You can also place spot orders through the new gateway, which routes them to the same Coinbase Exchange order books. That path is optional and additive; there is nothing to migrate for spot.

How do I fund my derivatives account?

Funding stays on Coinbase and is unchanged. See Funding above.

My GTT orders — what do I do?

There is no good-til-time equivalent. Use good-til-day (expires at session end) or manage expiry client-side.

My stop-limit tracking broke after a trigger.

Expected. The engine issues a new order ID after the stop triggers. Track both IDs.

My retry loop keeps getting disconnected.

Expected. Rate-limit exhaustion disconnects you; it does not return a retryable HTTP 429. Implement credit-aware backoff.

Where do I get integration support?

Contact your Coinbase account manager.

Global Derivatives

# Deribit Registered Partners — Migration Guide

This is the migration guide for existing registered Deribit partners.

## Summary

Coinbase integrated Deribit on October 1, 2026. Your existing Deribit users are unaffected. They keep their Deribit accounts and credentials, and you keep receiving rebates from them. What changed is your new users: they now arrive with Coinbase credentials. Your integration therefore serves a mix of existing users on Deribit credentials and new users on Coinbase credentials. That takes some integration work: route each user to the correct endpoint, and add the auth path for new (Coinbase) users.

## What changes — and what doesn’t

Cohort| What changed  
---|---  
**Your existing Deribit users**|  Unaffected. They keep their Deribit accounts, credentials, and UX. No migration. You keep receiving rebates from them.  
**Your new users**|  Can no longer self-serve at `deribit.com`. They onboard through Coinbase and arrive with Coinbase credentials.  
  
## Route per user

Existing and new users hold different credentials, so your integration selects the base URL and auth model per user, based on how they onboarded.

End-user cohort| Account type| Base URL (REST / WebSocket)| Auth model  
---|---|---|---  
**Existing users**|  Deribit-native| `https://www.deribit.com/api/v2` · `wss://www.deribit.com/ws/api/v2`| Deribit OAuth / Deribit API key  
**New users**|  Coinbase| `https://drb.coinbase.com/api/v2` · `wss://drb.coinbase.com/ws/api/v2`| Coinbase CDP key or OAuth2 via token exchange  
  
## Authentication

  * **Existing users** keep their native Deribit authentication (Deribit OAuth or Deribit API key) — unchanged from today.
  * **New users** authenticate with Coinbase credentials — either a CDP API key or OAuth2 — by calling `public/auth` to obtain a Deribit access token (HTTP) or an authenticated session (WebSocket).

**Tokens** — the following tokens are used in the authentication flows:

Token| What it is| Issued by| Lifetime| Reference  
---|---|---|---|---  
`cdp jwt`| short-lived JWT signed with the user’s CDP API key| you, signed locally| ~120s| [API key auth](/coinbase-app/authentication-authorization/api-key-authentication)  
`oauth2 access token`| the user’s Coinbase OAuth2 access token| `POST login.coinbase.com/oauth2/token`| 1 hour| [Access & refresh tokens](/coinbase-app/oauth2-integration/access-and-refresh-tokens)  
`deribit access token`| Deribit bearer token from `public/auth`, HTTP only; on WebSocket the socket itself is authenticated (no token)| Deribit `public/auth`| ~15m (HTTP) · ~50m session (WS)| [Deribit API docs](https://docs.deribit.com)  
  
**Authenticate over the transport you will use:** an HTTP token cannot authenticate a WebSocket, and vice versa.

### API Keys - Private Access Sequence

  * HTTP

  * WebSocket

![CDP API key HTTP authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-http.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=01dacfc9f9bf1082f63630ce381d7a00)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * You need to provide the Deribit access token on each private method call.
  * Refresh the Deribit access token every 15 minutes.

![CDP API key WebSocket authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-ws.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=da205794e4b2fb96d27d53a5c55fb828)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * When you call `public/auth` that authorizes the websocket session, no return token is needed to access private methods.
  * Refresh the websockets authentication before it expires (~50 minutes).

### OAuth2 - Private Access Sequence

  * HTTP

  * WebSocket

![OAuth2 HTTP authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-oauth2-http.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=edeeecd9516b905490e8e17475a23642)

  * Retrieve an OAuth2 access token from `POST login.coinbase.com/oauth2/token`.
  * It expires in 60 mins, use an unexpired OAuth2 access token with every `public/auth` call.
  * You need to provide the Deribit access token on each private method call.

For OAuth there are 2 separate refresh cycles:

  * Refresh the Deribit access token every 15 minutes.
  * Refresh the OAuth2 access token every 1 hour. `POST login.coinbase.com/oauth2/token` with `grant_type=refresh_token` and your refresh token; you get back a new access _and_ refresh token.

![OAuth2 WebSocket authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-oauth2-ws.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=051d7746684e34ffb42517e5548e2588)

  * Retrieve an OAuth2 access token from `POST login.coinbase.com/oauth2/token`.
  * It expires in 60 mins, use an unexpired OAuth2 access token with every `public/auth` call.
  * When you call `public/auth` that authorizes the websocket session, no return token is needed to access private methods.

For OAuth there are 2 separate refresh cycles:

  * Refresh the websockets authentication before it expires (~50 minutes).
  * Refresh the OAuth2 access token every 1 hour. `POST login.coinbase.com/oauth2/token` with `grant_type=refresh_token` and your refresh token; you get back a new access _and_ refresh token.

### Notes

  * **On WebSocket, the connection is the credential.** `public/auth` returns no token — private method calls are authorized by the authenticated socket itself. Re-send `public/auth` on the same socket to extend. If the socket drops, you’ll need to re-authenticate from scratch.
  * **Request`offline_access` to get a refresh token (OAuth2).** Coinbase only issues a refresh token if the `offline_access` scope was in your authorize request. Without it, the 1-hour access token cannot be refreshed and the user must re-authorize. See [OAuth2 scopes](/coinbase-app/oauth2-integration/scopes) and [access & refresh tokens](/coinbase-app/oauth2-integration/access-and-refresh-tokens).
  * **CDP keys can use Ed25519 or ECDSA algorithms.** Ed25519 is recommended and works with direct API calls. ECDSA keys are only required for legacy / third party SDKs.
  * **Send`public/auth` as a `POST` so credentials stay out of the URL.** Deribit accepts `public/auth` over both `GET` and `POST`; use `POST` so the CDP JWT or OAuth2 access token travels in the request body, not the query string — keeping it out of URLs, browser history, and access logs. See [OAuth2 security best practices](/coinbase-app/oauth2-integration/security-best-practices).

## Migration Checklist

1

Keep your existing Deribit integration as-is

Repoint production traffic

Move production traffic to the new gateway. The INTX endpoints no longer accept derivatives orders.

## FAQ

Do I need a separate trading account or API key?

No. You keep your existing Coinbase (CDP) API key and authenticate to the new gateway with it. There is no separate account or key to create.

Can I still trade derivatives on the INTX endpoints?

No. INTX perpetuals trading through the Advanced Trade API ended on October 1, 2026, with no parallel run. Trade on the new gateway.

What happened to my open orders and positions?

Open orders were cancelled; re-place them on the new gateway. Positions and balances migrated automatically (settled and recreated on the new platform). See What happened at migration.

Is spot trading affected?

No. Your spot integration is unchanged — spot API endpoints remain on `api.coinbase.com`. You can also place spot orders through the new gateway, which routes them to the same Coinbase Exchange order books. That path is optional and additive; there is nothing to migrate for spot.

How do I fund my derivatives account?

Funding stays on Coinbase and is unchanged. See Funding above.

My GTT orders — what do I do?

There is no good-til-time equivalent. Use good-til-day (expires at session end) or manage expiry client-side.

My stop-limit tracking broke after a trigger.

Expected. The engine issues a new order ID after the stop triggers. Track both IDs.

My retry loop keeps getting disconnected.

Expected. Rate-limit exhaustion disconnects you; it does not return a retryable HTTP 429. Implement credit-aware backoff.

Where do I get integration support?

Contact your Coinbase account manager.