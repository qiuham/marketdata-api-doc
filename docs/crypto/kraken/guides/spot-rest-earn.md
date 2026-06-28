---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-rest-earn
api_type: Guide
updated_at: 2026-05-27 19:58:59.280826
---

# Spot REST Earn

The earn API allows interacting with all of Kraken's yield generating products. It replaces the old `/staking` part of the API.

The different available earn products are represented by earn strategies. This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are replaced by `Allocate`/`Deallocate`.

## Overview of available endpoints under Earn

  * `Strategies` \- list all earn strategies for which you are eligible or have a balance.
  * `Allocations` \- lists the balance in your earn account for each strategy. Requires the `Query Funds` API key permission.
  * `Allocate`/`Deallocate` \- allocate/deallocate to an earn strategy through an async operation. Requires the `Earn Funds` API key permission.
  * `AllocateStatus`/`DeallocateStatus` \- verifies the state of the last allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API key permission.

## Examples

### Determine which funds are earning rewards

  1. Call `Strategies` to obtain information about the relevant strategy. The `lock_type` field shows whether bonding/unbonding funds are earning yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.
  2. Call `Allocations` for the relevant strategy. From the previous step, for strategies where bonding/unbonding does not earn yield, substract these balances from `amount_allocated.total` to determine which balances are currently earning.

### Get allocatable balance

Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining balance is available for allocation to a strategy.

### Geo restrictions

Some earn strategies are not available in all geographic regions. `Strategies` will return only strategies available to the caller.

  * Overview of available endpoints under Earn
  * Examples
* Determine which funds are earning rewards
* Get allocatable balance
* Geo restrictions