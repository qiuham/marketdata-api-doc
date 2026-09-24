---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/isolated-positions
api_type: Guide
updated_at: 2026-09-24 19:01:05.176403
---

# Isolated Positions API Guide

Learn how to manage isolated positions with the Global Derivatives JSON-RPC API.

Isolated margin confines risk to the collateral allocated to one position. Isolated orders and positions are owned by managed subaccounts that the API provisions on demand and hides from account listings unless you ask for them with `include_isolated: true`. This guide covers the behavior that differs from cross-margin trading and how to integrate against the JSON-RPC API. Examples use `SOL_USDC-PERPETUAL`. `123456` stands for a discovered integer subaccount ID; `subaccount_id` is an integer on the wire, not a string.

## 1. How isolated margin works

Four behaviors differ from ordinary cross trading. Read these before the walkthrough; most integration bugs come from assuming one of them away.

### 1.1 The API provisions hidden subaccounts for you

You never create an isolated subaccount yourself. Sending [`private/buy`](/api-reference/trading/private-buy) or [`private/sell`](/api-reference/trading/private-sell) from the main account with `isolated: true`:

  1. claims a free isolated subaccount (slot) or creates one if none is free,
  2. binds it to the requested instrument,
  3. places the order under that subaccount’s ID.

The order and position are owned by the isolated subaccount (`user_id`, for example `123456`), not the main account. Responses also carry `main_uid`, which identifies the owning main account. Cross and isolated positions can coexist on the same instrument. A main account can maintain a cross position while simultaneously holding an isolated position on the same instrument via a provisioned slot. Each position is margined, tracked, and managed independently under its respective account ID (`user_id`).

### 1.2 Two flags: routing versus visibility

Because isolated records live on subaccounts, most operations take one of two flags. Mixing them up is the most common integration mistake.

  * `isolated: true` routes a single-order operation (place, edit, cancel, close, leverage, per-order reads) to the subaccount that owns the instrument or order. The default is `false`, so omitting it silently targets cross margin instead of producing an error.
  * `include_isolated: true` widens a main-account list, snapshot, or mass cancel to include hidden isolated subaccounts. Without it, hidden isolated slots are excluded.
  * `subaccount_id` targets one discovered subaccount directly. History calls for a slot require `subaccount_id`; they do not aggregate with `include_isolated`.

Operation| Methods| Flag| If omitted  
---|---|---|---  
Single-order operations| [`private/buy`](/api-reference/trading/private-buy), [`private/sell`](/api-reference/trading/private-sell), [`private/edit`](/api-reference/trading/private-edit), [`private/edit_by_label`](/api-reference/trading/private-edit_by_label), [`private/cancel`](/api-reference/trading/private-cancel), [`private/close_position`](/api-reference/trading/private-close_position), [`private/get_margins`](/api-reference/trading/private-get_margins), [`private/get_leverage`](/api-reference/account-management/private-get_leverage), [`private/set_leverage`](/api-reference/trading/private-set_leverage), [`private/get_order_state`](/api-reference/trading/private-get_order_state), [`private/get_user_trades_by_order`](/api-reference/trading/private-get_user_trades_by_order), [`private/get_max_order_size`](/api-reference/trading/private-get_max_order_size), [`private/get_order_margin_by_ids`](/api-reference/trading/private-get_order_margin_by_ids)| `isolated: true`| Acts on cross margin. [`private/cancel`](/api-reference/trading/private-cancel) and [`private/edit`](/api-reference/trading/private-edit) return `order_not_found` or `not_owner_of_order`.  
Main-account aggregates| [`private/get_subaccounts`](/api-reference/account-management/private-get_subaccounts), [`private/get_subaccounts_details`](/api-reference/account-management/private-get_subaccounts_details), [`private/get_positions`](/api-reference/account-management/private-get_positions), [`private/get_position`](/api-reference/account-management/private-get_position), [`private/get_open_orders`](/api-reference/trading/private-get_open_orders), [`private/get_account_summaries`](/api-reference/account-management/private-get_account_summaries), [`private/get_order_state_by_label`](/api-reference/trading/private-get_order_state_by_label)| `include_isolated: true`| Excludes hidden isolated slots.  
Mass cancel| [`private/cancel_all`](/api-reference/trading/private-cancel_all), [`private/cancel_all_by_instrument`](/api-reference/trading/private-cancel_all_by_instrument), [`private/cancel_all_by_currency`](/api-reference/trading/private-cancel_all_by_currency), [`private/cancel_by_label`](/api-reference/trading/private-cancel_by_label)| `include_isolated: true`| Cancels main-account orders only; isolated orders stay open.  
History| [`private/get_order_history_by_currency`](/api-reference/trading/private-get_order_history_by_currency), [`private/get_user_trades_by_currency`](/api-reference/trading/private-get_user_trades_by_currency), [`private/get_settlement_history_by_currency`](/api-reference/trading/private-get_settlement_history_by_currency), [`private/get_transaction_log`](/api-reference/account-management/private-get_transaction_log)| `subaccount_id`| —  
  
### 1.3 Slots are recycled and IDs are reused

A slot binds to one instrument at a time, reported as `isolated_margin_instrument`. A slot is recycled only when both conditions hold:

  * no position has a non-zero size;
  * no open order remains.

On recycling, remaining collateral settles back to the main account and the binding clears. The subaccount ID itself is retained and can later be bound to a different instrument. Two consequences:

  * History for one `subaccount_id` can span multiple instruments. Key audit trails by `subaccount_id`, `instrument_name`, and timestamp.
  * Do not cache an instrument-to-subaccount mapping. Rediscover it.

### 1.4 Orders auto-allocate margin and slots auto-sweep on close

Placing a risk-increasing order with `isolated: true` automatically transfers the required margin from the main account to the slot, unless you supply `allocated_margin` explicitly. If passed, `allocated_margin` must meet the required minimum, or placement fails with `14033 isolated_allocated_too_low`. When an isolated position is completely closed and has no open orders, an **auto-sweep** automatically transfers all remaining collateral and P&L back to the main account and recycles the slot. Partial position reductions or leverage increases do not trigger a partial auto-sweep; excess margin remains in the slot until complete closure or [manual transfer](/api-reference/wallet/private-submit_transfer_between_subaccounts).

## 2. Integration walkthrough

### 2.1 Authenticate and subscribe

Authenticate HTTP and WebSocket sessions as the main account before you call private methods or subscribe. For the authentication flow, see the [Global Derivatives technical guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical). Subscribe to the [isolated order](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedorderskindcurrencyinterval), [isolated trade](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedtradeskindcurrencyinterval), [isolated change](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedchangeskindcurrencyinterval), [isolated portfolio](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedportfoliocurrency), and [isolated liquidation](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedliquidation) channels. For all private channels and the AsyncAPI specification, see [Global Derivatives WebSocket endpoints](/coinbase-app/advanced-trade-apis/websocket/websocket-endpoints):
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "private/subscribe",
      "params": {
        "channels": [
          "user.isolated.orders.any.USDC.100ms",
          "user.isolated.trades.any.USDC.100ms",
          "user.isolated.changes.any.USDC.100ms",
          "user.isolated.portfolio.USDC",
          "user.isolated.liquidation"
        ]
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": [
        "user.isolated.orders.any.USDC.100ms",
        "user.isolated.trades.any.USDC.100ms",
        "user.isolated.changes.any.USDC.100ms",
        "user.isolated.portfolio.USDC",
        "user.isolated.liquidation"
      ]
    }
    

Channel grammar depends on the channel family:

  * For `orders`, `trades`, and `changes`: `user.isolated.<family>.<kind>.<currency>.<interval>`, where `<kind>` is `future` or `any`, `<currency>` is a currency code or `any`, and `<interval>` is `raw`, `100ms`, or `agg2`. An instrument name can replace `<kind>.<currency>`, for example `user.isolated.orders.SOL_USDC-PERPETUAL.raw`.
  * For `portfolio`: `user.isolated.portfolio.<currency>`, where `<currency>` is a currency code or `any` (e.g. `USDC` or `user.isolated.portfolio.any`).
  * For `liquidation`: `user.isolated.liquidation`.

Compare the `result` array against the channels you requested: unsupported channels are silently omitted. Base channels (`user.orders.*`, `user.trades.*`, `user.changes.*`) carry main-account activity only; subscribe to both sets if you track cross and isolated activity. Events carry the owning slot’s `user_id`, plus `main_uid` and `isolated: true` on order, trade, and change records. When a slot is recycled, the portfolio channel emits a final frame with zeroed equity and margin fields. A liquidation notification reports an event, not slot readiness; refresh positions, orders, portfolio state, and the binding afterward.

### 2.2 Discover isolated subaccounts

Call [`private/get_subaccounts`](/api-reference/account-management/private-get_subaccounts) with `include_isolated: true` on application startup or reconnection to discover existing active slots and their assigned `subaccount_id`s.

If you have not placed an isolated order yet, [`private/get_subaccounts`](/api-reference/account-management/private-get_subaccounts) returns **only your main account**. Isolated subaccounts are lazily provisioned when you submit your first order with `isolated: true` (see Place an isolated order).
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "method": "private/get_subaccounts",
      "params": {
        "include_isolated": true
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "result": [
        {
          "id": 1000,
          "type": "main",
          "isolated": null,
          "isolated_margin_instrument": null
        },
        {
          "id": 123456,
          "type": "subaccount",
          "isolated": true,
          "isolated_margin_instrument": "SOL_USDC-PERPETUAL"
        }
      ]
    }
    

`id` is the value to pass as `subaccount_id` on direct reads and history queries. `isolated: true` distinguishes a managed slot from a regular subaccount. `isolated_margin_instrument` is the reported binding. It becomes `null` after recycling and may later name another instrument. For per-slot positions and open orders in one call, use [`private/get_subaccounts_details`](/api-reference/account-management/private-get_subaccounts_details):
    
    
    {
      "jsonrpc": "2.0",
      "id": 3,
      "method": "private/get_subaccounts_details",
      "params": {
        "currency": "USDC",
        "include_isolated": true,
        "with_open_orders": true
      }
    }
    

### 2.3 Monitor risk
    
    
    {
      "jsonrpc": "2.0",
      "id": 4,
      "method": "private/get_account_summaries",
      "params": {
        "extended": true,
        "include_isolated": true
      }
    }
    

The plural [`private/get_account_summaries`](/api-reference/account-management/private-get_account_summaries) endpoint does not parse a `currency` parameter; summaries for all portfolio currencies are always returned for both main and isolated subaccounts. With `include_isolated: true`, it returns active isolated subaccounts under `isolated_account_summaries` as a list of entries with the structure `{ "id": 123456, "summaries": [ ... ] }`. The risk fields (`equity`, `margin_balance`, `initial_margin`, `maintenance_margin`, `available_funds`) live on the per-currency rows inside the nested `summaries` array, not flat on the slot entry. Callers must select the matching currency row (e.g. `USDC`) from `summaries` client-side. Only active/bound slots appear in `isolated_account_summaries` (recycled slots are omitted). Fields are numeric (zero where applicable); nulls are anomalous. If a slot’s aggregation fails, the slot is omitted entirely. Evaluate risk per isolated slot, not against the cross account. Call [`private/get_account_summary`](/api-reference/account-management/private-get_account_summary) with `subaccount_id` for a direct, per-slot check.

### 2.4 Place an isolated order

Before placing an isolated order, use [`private/get_margins`](/api-reference/trading/private-get_margins) with `isolated: true` to preview the margin requirement in isolated scope.
    
    
    {
      "jsonrpc": "2.0",
      "id": 5,
      "method": "private/buy",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "amount": 10,
        "type": "limit",
        "price": 100,
        "isolated": true
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 5,
      "result": {
        "order": {
          "order_id": "<order_id>",
          "instrument_name": "SOL_USDC-PERPETUAL",
          "user_id": 123456,
          "main_uid": 1000,
          "isolated": true,
          "order_state": "<order_state>",
          "filled_amount": 0
        },
        "trades": []
      }
    }
    

The response identifies the provisioned slot through `order.user_id`.

### 2.5 Manage collateral

Collateral moves between the main account and the slot in three ways. Automatic allocation: on a risk-increasing order with `allocated_margin` omitted, the API calculates the required amount. If you supply it, the amount must meet the required minimum, or the order fails with `14033 isolated_allocated_too_low`; the error `data` returns `required_minimum` and `suggested_amount` (see 3.3). Manual top-up with [`private/submit_transfer_between_subaccounts`](/api-reference/wallet/private-submit_transfer_between_subaccounts):
    
    
    {
      "jsonrpc": "2.0",
      "id": 6,
      "method": "private/submit_transfer_between_subaccounts",
      "params": {
        "currency": "USDC",
        "amount": 50,
        "source": 1000,
        "destination": 123456
      }
    }
    

`source` is the main account ID and `destination` the slot ID. Common failures: `10009 not_enough_funds` (insufficient balance or wrong currency) and `12100 transfer_not_allowed` (invalid or unauthorized destination subaccount ID). Confirm completion through the portfolio channel or a fresh account summary, not the transfer response alone. On a risk-reducing order, a supplied `allocated_margin` is transferred as-is. Omit it on closes unless you mean to add collateral. Collateral returns to the main account automatically when the slot is recycled; there is no separate withdrawal step.

### 2.6 Set leverage

Both [`private/get_leverage`](/api-reference/account-management/private-get_leverage) and [`private/set_leverage`](/api-reference/trading/private-set_leverage) take `isolated: true` to target the isolated slot scope. Omitting `isolated: true` on [`private/get_leverage`](/api-reference/account-management/private-get_leverage) or [`private/set_leverage`](/api-reference/trading/private-set_leverage) silently acts on cross leverage instead of returning an error. Direct targeting via `subaccount_id` is not a substitute for the flag on leverage calls and is rejected with `14020 only_for_retail_brokers`. Isolated leverage can be configured before a slot is active or bound.
    
    
    {
      "jsonrpc": "2.0",
      "id": 7,
      "method": "private/get_leverage",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "isolated": true
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 7,
      "method": "private/set_leverage",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "leverage": 5,
        "isolated": true
      }
    }
    

### 2.7 Edit an isolated order

Send [`private/edit`](/api-reference/trading/private-edit) or [`private/edit_by_label`](/api-reference/trading/private-edit_by_label) from the main account with `isolated: true`:
    
    
    {
      "jsonrpc": "2.0",
      "id": 8,
      "method": "private/edit",
      "params": {
        "order_id": "<order_id>",
        "amount": 12,
        "price": 99,
        "isolated": true
      }
    }
    

An edit that increases risk can include `allocated_margin` to top up the slot in the same call. Editing by targeting the slot directly with `subaccount_id` is rejected with `14020 only_for_retail_brokers`; always edit from the main account with `isolated: true`.

### 2.8 Cancel isolated orders

Single order:
    
    
    {
      "jsonrpc": "2.0",
      "id": 9,
      "method": "private/cancel",
      "params": {
        "order_id": "<order_id>",
        "isolated": true
      }
    }
    

Without `isolated: true`, the cancel searches only the main account and returns `order_not_found` or `not_owner_of_order`. Treat either code as “the flag was missing or the ID is wrong”, not as proof the order no longer exists. Mass cancel:
    
    
    {
      "jsonrpc": "2.0",
      "id": 10,
      "method": "private/cancel_all_by_instrument",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "include_isolated": true
      }
    }
    

[`private/cancel_all`](/api-reference/trading/private-cancel_all), [`private/cancel_all_by_currency`](/api-reference/trading/private-cancel_all_by_currency), and [`private/cancel_by_label`](/api-reference/trading/private-cancel_by_label) take the same flag. With `include_isolated: true`, a mass-cancel method includes matching open orders from the main account and every active isolated-margin subaccount. [`private/cancel_all`](/api-reference/trading/private-cancel_all) therefore cancels all open cross-margin and isolated-margin orders; filtered mass-cancel methods apply their instrument, currency, or label filter across both scopes.

### 2.9 Close, reduce, or reverse a position

The simplest close is [`private/close_position`](/api-reference/trading/private-close_position) with `isolated: true`. The API resolves the slot, reads the current position, and submits an opposite-side reduce-only order for the full size:
    
    
    {
      "jsonrpc": "2.0",
      "id": 11,
      "method": "private/close_position",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "type": "market",
        "isolated": true
      }
    }
    

For manual control, submit an opposite-side reduce-only order with `isolated: true`:
    
    
    {
      "jsonrpc": "2.0",
      "id": 12,
      "method": "private/sell",
      "params": {
        "instrument_name": "SOL_USDC-PERPETUAL",
        "amount": 10,
        "type": "market",
        "reduce_only": true,
        "isolated": true
      }
    }
    

An isolated slot is recycled only after its position is closed and all open orders are cancelled. If a close order remains unfilled, cancel or replace it as needed, then confirm that the position and open orders are cleared before relying on the collateral auto-sweep.

### 2.10 Read positions, open orders, and history

Main-account aggregates:
    
    
    {
      "jsonrpc": "2.0",
      "id": 13,
      "method": "private/get_positions",
      "params": {
        "currency": "any",
        "include_isolated": true
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 13,
      "result": [
        {
          "instrument_name": "SOL_USDC-PERPETUAL",
          "user_id": 123456,
          "main_uid": 1000,
          "isolated": true,
          "direction": "buy",
          "size": 1000.0,
          "size_currency": 10.0
        }
      ]
    }
    

[`private/get_position`](/api-reference/account-management/private-get_position) (singular) with an instrument name and `include_isolated: true` resolves a position by instrument. When a bound isolated slot exists for the instrument, the singular call returns the isolated position and does not show a coexisting cross position; omit `include_isolated: true` to read the cross position, or use plural `get_positions` with `include_isolated: true` to retrieve both.
    
    
    {
      "jsonrpc": "2.0",
      "id": 14,
      "method": "private/get_open_orders",
      "params": {
        "include_isolated": true
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 14,
      "result": [
        {
          "order_id": "<order_id>",
          "instrument_name": "SOL_USDC-PERPETUAL",
          "user_id": 123456,
          "main_uid": 1000,
          "isolated": true,
          "order_state": "open"
        }
      ]
    }
    

Direct reads target one slot by `subaccount_id`:
    
    
    {
      "jsonrpc": "2.0",
      "id": 15,
      "method": "private/get_positions",
      "params": {
        "currency": "any",
        "subaccount_id": 123456
      }
    }
    
    
    
    {
      "jsonrpc": "2.0",
      "id": 16,
      "method": "private/get_open_orders",
      "params": {
        "subaccount_id": 123456
      }
    }
    

Direct targeting requires authority over the subaccount; main-account credentials have it for their own slots. If rejected, use the aggregates instead. History is account-specific. Query order, trade, settlement, and transaction history for each isolated slot with `subaccount_id`. A recycled slot can contain records for multiple instruments, so key your records by `subaccount_id` and `instrument_name`. Settlements and transaction logs are also slot-scoped: To query isolated perpetual settlements, call [`private/get_settlement_history_by_currency`](/api-reference/trading/private-get_settlement_history_by_currency) with `subaccount_id`:
    
    
    {
      "jsonrpc": "2.0",
      "id": 21,
      "method": "private/get_settlement_history_by_currency",
      "params": {
        "currency": "USDC",
        "subaccount_id": 123456,
        "count": 100
      }
    }
    

Isolated perpetual settlements are recorded per slot (including funding fees when non-zero) and are ONLY visible when targeting the slot via `subaccount_id`. Passing `include_isolated: true` to `get_settlement_history_by_currency` has no effect on settlement history queries. To audit full ledger movements for a slot, call [`private/get_transaction_log`](/api-reference/account-management/private-get_transaction_log) with `subaccount_id`, `start_timestamp`, and `end_timestamp` (`start_timestamp` and `end_timestamp` are mandatory; omitting either returns `-32602 value required`):
    
    
    {
      "jsonrpc": "2.0",
      "id": 22,
      "method": "private/get_transaction_log",
      "params": {
        "currency": "USDC",
        "subaccount_id": 123456,
        "start_timestamp": 1787109600000,
        "end_timestamp": 1787196000000,
        "count": 100
      }
    }
    

When an isolated position closes, the API may create transaction-log entries for both the isolated subaccount and the main account. Do not rely on a specific transaction type or on values inside `info`, because they can vary. Use the top-level `cashflow` field to review money movements. The `role` field is only available for some transfer types. Treat a cleared `isolated_margin_instrument` value as the confirmation that the isolated slot was recycled.

## 3. Runbooks and reference

### 3.1 Production startup sequence

Initialize in this order so you never trade on a partial view:

  1. Authenticate the HTTP and WebSocket sessions as the main account.
  2. Subscribe to the `user.isolated.*` channels and verify the accepted list.
  3. Snapshot with [`private/get_subaccounts`](/api-reference/account-management/private-get_subaccounts) (`include_isolated: true`), [`private/get_positions`](/api-reference/account-management/private-get_positions) (`include_isolated: true`), [`private/get_open_orders`](/api-reference/trading/private-get_open_orders) (`include_isolated: true`), and [`private/get_account_summaries`](/api-reference/account-management/private-get_account_summaries) (`include_isolated: true`).
  4. Reconcile positions and orders against slot IDs into local state.
  5. Enable order placement.

### 3.2 Cleanup checklist

  1. Fetch [`private/get_subaccounts`](/api-reference/account-management/private-get_subaccounts) with `include_isolated: true` and record each active slot’s binding.
  2. Cancel the slot’s resting orders with `include_isolated: true` on mass cancels or `isolated: true` on single cancels.
  3. Close the remaining position with [`private/close_position`](/api-reference/trading/private-close_position) and `isolated: true`, or with a manual reduce-only order.
  4. Confirm that the slot has no open orders or position. If it is missing from an aggregate, query it directly with `subaccount_id`.
  5. Refresh subaccounts until `isolated_margin_instrument` clears and funds settle to the main account.
  6. For audit evidence, key slot history by `subaccount_id` and `instrument_name`.

### 3.3 Error reference

Errors arrive in the JSON-RPC `error` object; some isolated validation errors include a `data` object with machine-readable fields:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "error": {
        "code": 14033,
        "message": "isolated_allocated_too_low",
        "data": {
          "allocated_margin": 5,
          "required_minimum": 9.9,
          "suggested_amount": 10,
          "required_im_delta": 10.5
        }
      }
    }
    

Error or symptom| Cause and action  
---|---  
`12001 too_many_subaccounts`| The main account reached its configured total open-subaccount limit (20 by default) and no recyclable slot was available. Clear existing isolated risk and orders, or have the account limit reviewed.  
`14033 isolated_allocated_too_low`| A supplied `allocated_margin` on a risk-increasing order was below the required minimum. Omit it for automatic calculation, or use `required_minimum` / `suggested_amount` from the error `data`.  
`14034 insufficient_cleared_balance`| The main account lacks cleared balance to fund the allocation. Reduce size or `allocated_margin`, or free up main-account balance.  
`14020 only_for_retail_brokers`| An edit was sent targeting the slot directly via `subaccount_id`. Edit from the main account with `isolated: true`.  
`order_not_found` or `not_owner_of_order` on cancel or edit| The order belongs to a slot and the request searched the main account. Confirm the order ID, then retry with `isolated: true`.  
Isolated orders survive a bulk cancel| Mass-cancel methods skip isolated slots unless `include_isolated: true` is sent.  
Hidden data is absent from a list or snapshot| Send `include_isolated: true`. `isolated` is a record attribute, not a visibility switch.  
A bound slot is missing from an aggregate read| Aggregates are best-effort. Query the slot directly with `subaccount_id`.  
Transfer fails with `10009 not_enough_funds` or `12100 transfer_not_allowed`| Check available funds, currency, or destination subaccount authorization. `10009` indicates insufficient funds or invalid currency; `12100` indicates an unauthorized destination.  
History looks mixed across instruments| The slot ID was recycled and reused. Key records by `subaccount_id` and `instrument_name`.  
  
## What to read next

  * [Global Derivatives technical guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical)
  * [Get positions API reference](/api-reference/account-management/private-get_positions)
  * [Isolated orders WebSocket channel reference](/api-reference/coinbase-deribit-app-api/websocket/user/userisolatedorderskindcurrencyinterval)