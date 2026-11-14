---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/guides/rest/earn'
updated_at: 2026-11-13
---

# Spot REST Earn

> How to allocate and deallocate funds to Kraken Earn strategies, check allocation status, and understand geo restrictions

The earn API allows interacting with all of Kraken's yield generating products. It replaces the old `/staking` part of the API.

The different available earn products are represented by earn strategies. This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are replaced by `Allocate`/`Deallocate`.

## Available Earn endpoints

* `Strategies` - list all earn strategies for which you are eligible or have a balance.
* `Allocations` - lists the balance in your earn account for each strategy. Requires the `Query Funds` API key permission.
* `Allocate`/`Deallocate` - allocate/deallocate to an earn strategy through an async operation. Requires the `Earn Funds` API key permission.
* `AllocateStatus`/`DeallocateStatus` - verifies the state of the last allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API key permission.

## Common workflows

### Determine which funds are earning rewards

1. Call `Strategies` to obtain information about the relevant strategy. The `lock_type` field shows whether bonding/unbonding funds are earning yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.
2. Call `Allocations` for the relevant strategy. From the previous step, for strategies where bonding/unbonding does not earn yield, substract these balances from `amount_allocated.total` to determine which balances are currently earning.

### Get allocatable balance

Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining balance is available for allocation to a strategy.

### Geo restrictions

Some earn strategies are not available in all geographic regions. `Strategies` will return only strategies available to the caller.
