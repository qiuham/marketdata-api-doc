---
exchange: deribit
source_url: https://docs.deribit.com/articles/intx-api-migration
api_type: Guide
updated_at: 2026-11-24 18:59:42.127809
---

# Coinbase International Exchange API Migration

> How International Exchange API and FIX integrations connect to Deribit after the migration: keys, endpoints, instruments, orders, and positions.

Coinbase International Exchange consolidated into Deribit on **1 October 2026**. This article is for institutional clients who trade over **API or FIX**. It covers how your integration talks to Deribit: new keys, endpoints, instrument names, order attributes, migrated positions, and the checks to run before you restore size.

Sign-in, balances, eligibility, and the rest of the account are in the knowledge base:

> [card] [Institutional Client Migration Guide](https://support.deribit.com/hc/en-us/articles/39354139215389-Institutional-Client-Migration-Guide)
>
> Sign-in, account checks, deposits, and non-API cutover details.

> [!WARNING]
>
> International Exchange API keys do not work on Deribit. Create a new Deribit key for every account or subaccount that trades through an integration.

## Accounts and keys

Your first International Exchange portfolio is the Deribit **main account**. Each additional portfolio is a **subaccount** named after its portfolio UID. Subaccounts do not share margin, positions, or collateral. A subaccount session cannot see the main account or other subaccounts. [`private/get_subaccounts`](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts) returns the mapping.

Create the first Deribit key in the UI on the target account (the main account for the first portfolio, or the matching subaccount for each of the others). Further keys can be created with [`private/create_api_key`](https://docs.deribit.com/api-reference/account-management/private-create_api_key). Set IP allowlists on the Deribit key. International Exchange allowlists are not on Deribit.

Authenticate with [`public/auth`](https://docs.deribit.com/api-reference/authentication/public-auth). On WebSocket, send `access_token` in params; on HTTP, use `Authorization: Bearer`. A main-account session can switch to a subaccount with [`public/exchange_token`](https://docs.deribit.com/api-reference/authentication/public-exchange_token) and `subject_id`.

If you already had a Deribit account, that account is unchanged. The International Exchange book is on this **new main account and its subaccounts**, separate from any existing book.

> [card] [Creating an API key](https://docs.deribit.com/articles/creating-api-key.md)
>
> UI and API key creation, scopes, IP allowlists

> [card] [Authentication](https://docs.deribit.com/articles/authentication.md)
>
> `public/auth`, tokens, `exchange_token`

## Endpoints

Point clients at Deribit. Testnet (`test.deribit.com`) and production use **separate accounts and keys**. JSON-RPC uses named parameters only, and prices and sizes are JSON **numbers**, not decimal strings.

| Interface | Production | Testnet |
| - | - | - |
| JSON-RPC WebSocket | `wss://www.deribit.com/ws/api/v2` | `wss://test.deribit.com/ws/api/v2` |
| JSON-RPC HTTP | `https://www.deribit.com/api/v2/{method}` | `https://test.deribit.com/api/v2/{method}` |
| FIX TCP | `fix.deribit.com:9881` | `fix-test.deribit.com:9881` |
| FIX SSL | `fix.deribit.com:9883` | `fix-test.deribit.com:9883` |

On FIX, `Username`(`553`) is the Deribit Client ID and `Password`(`554`) is derived from the Client Secret. See [JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) and [FIX overview](https://docs.deribit.com/fix-api/production/overview.md). Starbase is a separate stack with separate keys; see [Starbase](https://docs.deribit.com/starbase/overview.md).

You can try the interface and API on [test.deribit.com](https://test.deribit.com) before you restore production size.

## Instruments

Symbols such as `BTC-PERP-INTX` are Deribit linear perpetuals such as `BTC_USDC-PERPETUAL`. Discover names at runtime rather than maintaining a static map:

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "public/get_instruments",
  "params": {
    "currency": "USDC",
    "kind": "future"
  }
}
```

Perpetuals are `kind: "future"` with `settlement_period: "perpetual"`. International Exchange-style books are `instrument_type: "linear"`. On linear instruments, `amount` is in the **base coin**, not USD. Inverse instruments use USD `amount`. [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) is rate-limited (1 req/s); keep the cache current with [`instrument.state.{kind}.{currency}`](https://docs.deribit.com/subscriptions/market-data/instrumentstatekindcurrency).

Read `price_index` from the instrument. Many linear perps use the Coinbase Index; BTC, ETH, SOL, XRP, HYPE, AVAX, and TRX names with listed Deribit options keep the Deribit index. Use [`public/get_index_price`](https://docs.deribit.com/api-reference/market-data/public-get_index_price) for a snapshot and [`deribit_price_index.{index_name}`](https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name) for the stream. Charts, marks, and funding can differ from International Exchange displays.

## Orders

Types and time-in-force are **lowercase**. Deribit has no timestamp good-til-time order; `good_til_day` lasts until session end. Combined take profit / stop loss is not a single order — use linked OCO/OTO instead. A stop-limit has two ids (`trigger_order_id` after trigger). Iceberg size is `display_amount`; hidden quantity always takes.

| International Exchange | Deribit |
| - | - |
| Order types / TIF | `limit`, `market`, `stop_limit`, `good_til_cancelled`, `good_til_day`, `immediate_or_cancel`, `fill_or_kill` on [`private/buy`](https://docs.deribit.com/api-reference/trading/private-buy) / [`private/sell`](https://docs.deribit.com/api-reference/trading/private-sell) |
| Combined TPSL | [`linked_order_type` / `otoco_config`](https://docs.deribit.com/articles/order-management-best-practices#linked-orders-oto-oco-otoco) |
| Client order id | `label` (max 64) |
| Cancel on disconnect | Optional via [`private/enable_cancel_on_disconnect`](https://docs.deribit.com/api-reference/session-management/private-enable_cancel_on_disconnect). Not available over HTTP. |

Open International Exchange orders are not on Deribit. This includes stop, take-profit, iceberg, and good-til-time orders. Recreate them after you have checked balances and positions, starting with hedges and orders that reduce risk.

## Wallet, rate limits, and history

The deposit address is unchanged. Generate it with [`private/create_deposit_address`](https://docs.deribit.com/api-reference/wallet/private-create_deposit_address); Coinbase-custodied accounts also pass `network` ([Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)).

Withdrawal addresses on the main account and on subaccounts match the corresponding International Exchange portfolios and were imported with **no waiting period**. Subaccount withdrawal addresses are not shown in the interface; read them with [`private/get_address_book`](https://docs.deribit.com/api-reference/wallet/private-get_address_book). Withdrawals from subaccounts are not allowed. Additional addresses can still be added with [`private/add_to_address_book`](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book); those new entries follow Deribit's usual delay (default 3 days).

Rate limits are a credit pool **per main account and per subaccount** and do not inherit from International Exchange. A subaccount may not have the same throughput as its International Exchange portfolio. When credits are exhausted the API returns `too_many_requests` (`10028`) and **drops the WebSocket** (unlike a typical HTTP 429). Contact your account manager if you need a higher limit. See [Rate limits](https://docs.deribit.com/articles/rate-limits.md).

International Exchange margin loans and USDC borrow are not on Deribit. International Exchange trade, order, and fill history does not appear on Deribit. Those historical APIs remain available for about **12 months from 1 October 2026**.

## Positions

Open positions from International Exchange are open on Deribit at the **migration reference price**. They are not closed.

In trade history, the booking entries are **block trades tagged `Migration`**. They appear with `block_trade_id` set. They record the transfer onto Deribit. They are not new trading activity, and they incur no trading, transfer, or settlement fees.

The average entry price on Deribit is the migration reference price. If the International Exchange mark and the Deribit mark differed at that price, unrealized profit and loss can differ from the last figure on International Exchange. That gap is unrealized PnL, not a fee.

You can list those trades with [`private/get_user_trades_by_currency`](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_currency) or [`private/get_transaction_log`](https://docs.deribit.com/api-reference/account-management/private-get_transaction_log) (`query`: `block_trade`).

## Before you restore size

**1. Confirm balances and positions**

On the main account and every mapped subaccount, use [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) and [`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions) (`currency: "USDC"` for linear books).

**2. Restore order flow**

Confirm authentication, [`public/set_heartbeat`](https://docs.deribit.com/api-reference/session-management/public-set_heartbeat), and a small order plus cancel before restoring size. Open orders from International Exchange are gone, so the book needs to be rebuilt. Configure MMP with [`private/set_mmp_config`](https://docs.deribit.com/api-reference/trading/private-set_mmp_config). Migrated accounts default to `cross_sm` (Cross Standard Margin). Preview a change with [`private/change_margin_model`](https://docs.deribit.com/api-reference/account-management/private-change_margin_model) and `dry_run: true`.

> [accordion] Settlement, funding, and margin
>
> Session PnL on open perps is realized **daily at 08:00 UTC**, not every 5 minutes. Positions stay open. Funding accrues continuously in realized session profit and loss and is cash-settled at that same settlement; the published rate is an **8-hour** rate. Use [`public/ticker`](https://docs.deribit.com/api-reference/market-data/public-ticker), [`public/get_funding_rate_value`](https://docs.deribit.com/api-reference/market-data/public-get_funding_rate_value), and [`private/get_settlement_history_by_currency`](https://docs.deribit.com/api-reference/trading/private-get_settlement_history_by_currency) for the current values. Margin models are `cross_sm`, `cross_pm`, `segregated_sm`, and `segregated_pm`. The main account and each subaccount can use its own model.


## Related topics

- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)
- [Underlying Tiers](https://docs.deribit.com/starbase/underlying-tiers.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)