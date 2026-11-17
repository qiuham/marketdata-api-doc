---
exchange: deribit
source_url: https://docs.deribit.com/articles/currency-parameter
api_type: Guide
updated_at: 2026-11-16 20:31:55.791704
---

# Using the currency Parameter

> Discover supported currencies with get_currencies, learn what currency selects on each Deribit method, and avoid invalid currency and spot routing errors.

Many Deribit methods take a `currency` parameter, but they do not all mean the same thing by it, and they do not all accept the same values. A currency you can deposit is not necessarily a currency you can hold a position in, and a currency that is valid on one method can be rejected on another.

This article explains what to send, how to discover the valid values at runtime, and how to avoid the two mistakes that generate most currency-related errors: asking for positions or balances in a currency the account does not support, and asking for spot trade data on a currency whose spot pair is routed to Coinbase.

> [!NOTE]
>
> The concrete currency lists in this article are a snapshot taken from production and are included to illustrate the categories. Deribit adds and removes currencies over time, so treat [`public/get_currencies`](https://docs.deribit.com/api-reference/market-data/public-get_currencies) and [`private/get_currencies`](https://docs.deribit.com/api-reference/account-management/private-get_currencies) as the authoritative sources and read them at runtime rather than hardcoding a list.

## Discover currencies instead of hardcoding them

Two methods answer the question "which currencies may I ask about?", and they answer it differently.

### public/get\_currencies

[`public/get_currencies`](https://docs.deribit.com/api-reference/market-data/public-get_currencies) returns every currency the platform recognizes, with its withdrawal fees, confirmation counts, precision and cross-collateral membership. This is the set that the `currency` parameter accepts on public and account-wide methods: any symbol returned here is a syntactically valid `currency`, and any symbol not returned here is rejected.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "public/get_currencies",
  "params": {},
  "id": 1
}
```

> [!NOTE]
>
> The `currency` enum on an individual method's reference page lists the main settlement currencies rather than every value the parameter will accept. In practice these methods take any symbol `public/get_currencies` returns, and a currency with no instruments simply produces an empty result rather than an error. Validate against `get_currencies` rather than against the enum on the page.

### private/get\_currencies

[`private/get_currencies`](https://docs.deribit.com/api-reference/account-management/private-get_currencies) takes no parameters and returns the currencies available to the authenticated account. Because it is scoped to your account's custody arrangement, it is narrower than the public list and it is the correct list to drive wallet and balance requests from.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/get_currencies",
  "params": {},
  "id": 2
}
```

> [!TIP]
>
> Call `private/get_currencies` once when your application starts, cache the result, and iterate over that list instead of a list compiled by hand. This removes the whole class of "unsupported currency" errors, and it means new currencies are picked up without a code change.

## What currency means on each method

The same parameter name covers four different concepts. Which one applies depends on the method.

| Concept | What it selects | Typical methods |
| - | - | - |
| Settlement currency | The currency a derivative is margined and settled in, and therefore the currency a position and its margin are denominated in | [`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions), [`public/get_expirations`](https://docs.deribit.com/api-reference/market-data/public-get_expirations) |
| Wallet currency | A currency your account can hold, deposit or withdraw as a balance | [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary), [`private/get_deposits`](https://docs.deribit.com/api-reference/wallet/private-get_deposits), [`private/get_withdrawals`](https://docs.deribit.com/api-reference/wallet/private-get_withdrawals), [`private/get_transfers`](https://docs.deribit.com/api-reference/wallet/private-get_transfers) |
| Instrument grouping | Every instrument whose name involves the currency, as base or as quote | [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments), [`public/get_book_summary_by_currency`](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency), [`public/get_last_trades_by_currency`](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_currency), [`private/get_open_orders_by_currency`](https://docs.deribit.com/api-reference/trading/private-get_open_orders_by_currency) |
| Currency pair | A spot or index pair rather than a single currency, sent as `currency_pair` | [`private/cancel_all_by_currency_pair`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_currency_pair) |

Only a handful of methods accept the special value `any`, among them [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) and [`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions). The `by_currency` market data and trading methods require a single concrete currency, so sending `currency: "any"` to [`public/get_book_summary_by_currency`](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency) or [`public/get_last_trades_by_currency`](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_currency) is rejected. Check the method's own reference page before relying on `any`.

> [!NOTE]
>
> Starbase REST [`get_instruments`](https://docs.deribit.com/api-reference/market-data/list-instruments) matches `currency` to the instrument's base currency. Omit `currency` to return every base currency. `currency=any` matches no instrument and the call succeeds with an empty `result`.

### Single value or list

The `currency` parameter takes a single symbol on most methods. [`private/cancel_all_by_kind_or_type`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_kind_or_type) is one of the few methods that also accepts a JSON array of symbols; its reference page documents `currency` as "The currency symbol, list of currency symbols or `any` for all." Any other method rejects an array.

No method accepts a comma-separated string. Sending `currency: "BTC, USDC"` to [`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions) is treated as one unknown symbol and rejected with `invalid currency`. To query more than one currency at once, pass `currency: "any"` and filter the response client-side.

Currency symbols are matched case-insensitively, so `BTC` and `btc` are equivalent, but responses always use the uppercase form. Send uppercase and compare uppercase.

## Base and quote currency on spot amounts

On spot instruments the currency question also applies to sizes, because a pair has two of them: `BTC_USDT` has a base currency of BTC and a quote currency of USDT. An amount is meaningless until you know which of the two it is denominated in.

[`private/get_margins`](https://docs.deribit.com/api-reference/trading/private-get_margins) makes this explicit with `amount_type`, which applies to spot instruments only:

* `base`, the default, reads `amount` as a quantity of the base currency, with fees charged on top of it.
* `quote` reads `amount` as a total spend in the quote currency, with fees included in it.

Either way the resulting base quantities come back in `taker_base_amount` and `maker_base_amount`. Because taker and maker fee rates differ, a fee-inclusive spend buys a slightly different quantity in each role, and both are floored to a whole multiple of the instrument's `min_trade_amount`.

> [!NOTE]
>
> Leaving `amount_type` unset is the same as sending `base`, so a value you intended as "spend this much USDT" will be read as "buy this many BTC" unless you set `quote` explicitly. Read `base_currency` and `quote_currency` from [`public/get_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_instrument) rather than splitting the instrument name.

## An empty result is not an error

A currency can be perfectly valid and still have nothing to return. Most currencies on Deribit are wallet-only: they can be deposited, held and withdrawn, but no instrument is listed against them. Asking for their instruments or trades succeeds and returns an empty array.

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": []
}
```

At the time of writing, only BTC, ETH and USDC have listed derivatives, and spot pairs exist for a slightly wider set. Every other currency returned by `public/get_currencies` is wallet-only. So an empty `result` from [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) means "this currency has no instruments", not "your request was malformed". Do not retry it, and do not treat it as a failure.

## Positions

[`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions) reports open derivative positions. Two things follow from that, and both are common sources of confusion.

**Spot is not a position.** Spot trades settle immediately into your balances, so there is no open position to report. Sending `kind: "spot"` is rejected:

```json theme={null}
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "param": "kind",
      "reason": "spot kind not allowed"
    }
  },
  "id": 4
}
```

The accepted values are `future`, `option`, `future_combo` and `option_combo`. To see what you hold in a spot currency, read its balance from [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) instead.

**Positions only exist in settlement currencies.** Because a position is denominated in the currency its instrument settles in, only currencies that actually carry derivatives can return positions. Requesting a wallet-only currency is not an error, but it can only ever return an empty list.

> [!TIP]
>
> Rather than looping over currencies and guessing which ones are settlement currencies, call `private/get_positions` once with `currency: "any"` and omit `kind`. One request returns every open position across every currency and instrument kind, which is both cheaper in rate-limit credits and immune to changes in the currency list.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/get_positions",
  "params": {
    "currency": "any"
  },
  "id": 5
}
```

## Wallet and balances

Wallet methods validate `currency` against the currencies your account can actually hold, which depends on how your account is custodied. A currency that is valid for another account, or valid on a public method, can still be rejected here, with a different reason string depending on which check failed. See [Error reference](#error-reference) below.

The fix is the same in every case: drive these calls from [`private/get_currencies`](https://docs.deribit.com/api-reference/account-management/private-get_currencies), which already returns only what your account supports.

For balances specifically, prefer [`private/get_account_summaries`](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries) over a loop of [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) calls. It takes no `currency` parameter and returns one summary per currency your account holds, so there is no currency to get wrong and no unsupported currency to trip over.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/get_account_summaries",
  "params": {},
  "id": 6
}
```

## Spot trade data and Coinbase-routed pairs

Some Deribit spot pairs are matched on the Deribit matching engine; others are routed to Coinbase Exchange for matching. Deribit only sees a match on a routed pair when one of your own orders was part of it, so it cannot publish a complete public trade tape for those instruments. Rather than serve partial data, it rejects trade-derived requests for them with `not_supported_for_coinbase_routed_spot` (`11060`).

The trap is that this hits currency-scoped requests you did not think of as spot requests at all. On [`public/get_last_trades_by_currency`](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_currency) and [`public/get_last_trades_by_currency_and_time`](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_currency_and_time), `kind` defaults to `any`, and `any` includes spot. So a request that names only a currency is treated as covering that currency's spot pairs:

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "public/get_last_trades_by_currency",
  "params": {
    "currency": "USDC"
  },
  "id": 7
}
```

```json theme={null}
{
  "jsonrpc": "2.0",
  "error": {
    "code": 11060,
    "message": "not_supported_for_coinbase_routed_spot"
  },
  "id": 7
}
```

### How to avoid it

**Send an explicit derivative `kind`.** The rejection only applies when `kind` is `spot` or `any`. Naming `future`, `option`, `future_combo` or `option_combo` scopes the request away from spot and always succeeds, even on a currency that has routed pairs:

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "public/get_last_trades_by_currency",
  "params": {
    "currency": "USDC",
    "kind": "future"
  },
  "id": 8
}
```

**Subscribe per currency, not with `any`.** The `trades.{kind}.{currency}.{interval}` channel is refused for routed pairs, and `currency: "any"` is refused whenever any routed pair exists. Subscribe to the specific currencies or instruments you need.

**Query per instrument when you want spot.** For spot pairs matched on Deribit, [`public/get_last_trades_by_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_instrument) works normally. For routed pairs, get the full tape from Coinbase Exchange directly.

> [!WARNING]
>
> Which pairs are routed, and therefore which currencies are affected, is a configuration setting that Deribit can change. A currency can be affected even when it currently has no listed routed pair, so the affected set cannot be reliably derived from the instrument list. Do not maintain your own list of affected currencies: send an explicit derivative `kind` whenever you are not asking for spot data, and handle `11060` wherever you are.

For the full picture of how routed instruments differ, including order entry, see [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md).

## Error reference

| Code | Message | `data` | Cause and fix |
| - | - | - | - |
| -32602 | `Invalid params` | `param: currency`, `reason: invalid currency` | The symbol is not a Deribit currency, or `any` was sent to a method that requires a concrete currency. Validate against [`public/get_currencies`](https://docs.deribit.com/api-reference/market-data/public-get_currencies) and check whether the method accepts `any` |
| -32602 | `Invalid params` | `param: currency`, `reason: currency not supported` | A wallet method received a currency that is not available as a wallet balance. Use [`private/get_currencies`](https://docs.deribit.com/api-reference/account-management/private-get_currencies) |
| -32602 | `Invalid params` | `param: currency`, `reason: not supported for wallet type` | The currency exists but is not part of your account's custody arrangement. Use [`private/get_currencies`](https://docs.deribit.com/api-reference/account-management/private-get_currencies) |
| -32602 | `Invalid params` | `param: kind`, `reason: spot kind not allowed` | `kind: "spot"` was sent to [`private/get_positions`](https://docs.deribit.com/api-reference/account-management/private-get_positions). Read spot holdings as balances instead |
| -32602 | `Invalid params` | `param: kind`, `reason: invalid value` | The `kind` value is not recognized for this method. Check the accepted values on the method's reference page |
| 11060 | `not_supported_for_coinbase_routed_spot` | n/a | A trade-derived request covered a Coinbase-routed spot pair. Send an explicit derivative `kind`, or query the pair directly |

Code `11060` is also returned under its earlier message `not_supported_for_csr_spot`; treat the two as equivalent. See [Error Codes](https://docs.deribit.com/articles/errors.md) for the full list.

## Checklist

* Read `private/get_currencies` at startup and cache it; never hardcode a currency list.
* Send uppercase symbols and compare uppercase.
* Do not send `any` unless the method's reference page documents it.
* Use `private/get_positions` with `currency: "any"` instead of looping over currencies, and never send `kind: "spot"`.
* Use `private/get_account_summaries` instead of a loop of `private/get_account_summary` calls.
* Always send an explicit derivative `kind` on `by_currency` trade methods unless you genuinely want spot data.
* On spot, be explicit about `amount_type` so `amount` is read in the currency you meant.
* Treat an empty `result` as "nothing to return", not as a failed request.


## Related topics

- [private/get_currencies](https://docs.deribit.com/api-reference/account-management/private-get_currencies.md)
- [public/get_currencies](https://docs.deribit.com/api-reference/market-data/public-get_currencies.md)
- [private/get_open_orders_by_currency](https://docs.deribit.com/api-reference/trading/private-get_open_orders_by_currency.md)
- [private/get_order_history_by_currency](https://docs.deribit.com/api-reference/trading/private-get_order_history_by_currency.md)
- [public/get_book_summary_by_currency](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency.md)