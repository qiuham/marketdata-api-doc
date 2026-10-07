---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/overview
api_type: Guide
updated_at: 2026-10-07 19:07:32.847653
---

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