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
source_url: 'https://docs.kraken.com/institutional/api-reference/custody-rest'
updated_at: 2026-11-13
---

# Custody REST overview

> Endpoint index and legacy method mapping for the Kraken Custody REST API

The current API is the `v0` surface under `/v0/insto/custody/`. It replaces the earlier
`POST /0/private/GetCustody*` and `POST /0/private/ListCustody*` methods. Authenticate as
described in [Custody REST authentication](https://docs.kraken.com/institutional/guides/custody-rest-auth.md).

## Endpoint index

Every published operation, grouped as it appears in the sidebar. Paths link to the full
operation reference.

### Assets

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/assets`](https://docs.kraken.com/api-reference/custody-external-api/list-assets) | Assets available in custody, with metadata. |

### Organizations

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/organizations`](https://docs.kraken.com/api-reference/custody-external-api/list-organizations) | Organizations the caller belongs to. |
| `GET` | [`/v0/insto/custody/organizations/{org_iiban}/balances`](https://docs.kraken.com/api-reference/custody-external-api/list-balances) | Organization-level balances. |

### Vaults

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/vaults`](https://docs.kraken.com/api-reference/custody-external-api/list-vaults) | Vaults the caller can access, each with an aggregate `quote_value`. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-vault) | Metadata for one vault. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/balances`](https://docs.kraken.com/api-reference/custody-external-api/get-vault-balance) | Aggregate vault valuation in a quote currency. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/assets/balances`](https://docs.kraken.com/api-reference/custody-external-api/list-vault-asset-balances) | Per-asset quantities: spot, hold, available, staked, pledged. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/policies`](https://docs.kraken.com/api-reference/custody-external-api/list-vault-policies) | Approval policies configured on the vault. |

### Deposits

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/deposit-methods`](https://docs.kraken.com/api-reference/custody-external-api/list-deposit-methods) | Deposit methods enabled for the vault. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/deposit-methods/{method_id}/addresses`](https://docs.kraken.com/api-reference/custody-external-api/list-deposit-addresses) | Existing deposit addresses for a method. |
| `POST` | [`/v0/insto/custody/vaults/{vault_id}/deposit-methods/{method_id}/addresses`](https://docs.kraken.com/api-reference/custody-external-api/create-address) | Create a deposit address. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/deposits/info`](https://docs.kraken.com/api-reference/custody-external-api/get-deposit-info) | Deposit limits and constraints. |

### Withdrawals

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/whitelist/addresses`](https://docs.kraken.com/api-reference/custody-external-api/list-whitelist-addresses) | Whitelisted withdrawal addresses. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/withdrawal-methods`](https://docs.kraken.com/api-reference/custody-external-api/list-withdrawal-methods) | Withdrawal methods enabled for the vault. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/withdrawals/info`](https://docs.kraken.com/api-reference/custody-external-api/get-withdrawal-info) | Withdrawal limits and constraints. |
| `POST` | [`/v0/insto/custody/vaults/{vault_id}/withdrawals/fee-quotes`](https://docs.kraken.com/api-reference/custody-external-api/create-withdrawal-fee-quote) | Quote withdrawal fees before raising a task. |

### Tasks

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/tasks`](https://docs.kraken.com/api-reference/custody-external-api/list-tasks) | List tasks. Filter by `id`, the task's approval UUID. |
| `POST` | [`/v0/insto/custody/tasks`](https://docs.kraken.com/api-reference/custody-external-api/create-task) | Create a task from one or more instructions. |
| `GET` | [`/v0/insto/custody/tasks/{task_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-task-by-id) | Full task detail: instructions, initiator, reviewers, activities. |
| `POST` | [`/v0/insto/custody/tasks/{task_id}/review`](https://docs.kraken.com/api-reference/custody-external-api/review-task) | Approve or deny a task. |
| `GET` | [`/v0/insto/custody/tasks/activities`](https://docs.kraken.com/api-reference/custody-external-api/list-task-activities) | List task activities. Filter by `task_id`. |
| `GET` | [`/v0/insto/custody/tasks/activities/{activity_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-task-activity-by-id) | One activity by its `A`-prefixed activity id. |

### Transactions

| Method | Path | Purpose |
| - | - | - |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/transactions`](https://docs.kraken.com/api-reference/custody-external-api/list-transactions) | Vault transaction history. Filter by `task_id`. |
| `GET` | [`/v0/insto/custody/vaults/{vault_id}/transactions/{transaction_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-transaction) | One transaction. |

## Moving from the legacy methods

> [!NOTE]
>
> The v0 API identifies tasks by their approval UUID. Legacy `T`-prefixed task IDs
> are not accepted by task routes or task filters. Use the `id` returned by
> `POST /v0/insto/custody/tasks` for subsequent task reads and reviews.

| Legacy method | Replacement |
| - | - |
| `POST /0/private/ListCustodyVaults` | [`GET /v0/insto/custody/vaults`](https://docs.kraken.com/api-reference/custody-external-api/list-vaults) |
| `POST /0/private/GetCustodyVault` | [`GET /v0/insto/custody/vaults/{vault_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-vault) |
| `POST /0/private/GetCustodyBalance` | [`GET /v0/insto/custody/vaults/{vault_id}/balances`](https://docs.kraken.com/api-reference/custody-external-api/get-vault-balance) for the aggregate, [`GET /v0/insto/custody/vaults/{vault_id}/assets/balances`](https://docs.kraken.com/api-reference/custody-external-api/list-vault-asset-balances) for per-asset quantities. |
| `POST /0/private/DepositMethods` | [`GET /v0/insto/custody/vaults/{vault_id}/deposit-methods`](https://docs.kraken.com/api-reference/custody-external-api/list-deposit-methods) |
| `POST /0/private/DepositAddresses` | [`GET`](https://docs.kraken.com/api-reference/custody-external-api/list-deposit-addresses) and [`POST`](https://docs.kraken.com/api-reference/custody-external-api/create-address) `/v0/insto/custody/vaults/{vault_id}/deposit-methods/{method_id}/addresses`. |
| `POST /0/private/WithdrawMethods` | [`GET /v0/insto/custody/vaults/{vault_id}/withdrawal-methods`](https://docs.kraken.com/api-reference/custody-external-api/list-withdrawal-methods) |
| `POST /0/private/WithdrawAddresses` | [`GET /v0/insto/custody/vaults/{vault_id}/whitelist/addresses`](https://docs.kraken.com/api-reference/custody-external-api/list-whitelist-addresses) |
| `POST /0/private/ListCustodyTransactions` | [`GET /v0/insto/custody/vaults/{vault_id}/transactions`](https://docs.kraken.com/api-reference/custody-external-api/list-transactions) |
| `POST /0/private/GetCustodyTransaction` | [`GET /v0/insto/custody/vaults/{vault_id}/transactions/{transaction_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-transaction) |
| `POST /0/private/ListCustodyTasks` | [`GET /v0/insto/custody/tasks`](https://docs.kraken.com/api-reference/custody-external-api/list-tasks) |
| `POST /0/private/GetCustodyTask` | [`GET /v0/insto/custody/tasks/{task_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-task-by-id) |
| `POST /0/private/ListCustodyActivities` | [`GET /v0/insto/custody/tasks/activities`](https://docs.kraken.com/api-reference/custody-external-api/list-task-activities) |
| `POST /0/private/GetCustodyActivity` | [`GET /v0/insto/custody/tasks/activities/{activity_id}`](https://docs.kraken.com/api-reference/custody-external-api/get-task-activity-by-id) |
| `POST /0/private/RequestCustodyTransferToSpot` | [`POST /v0/insto/custody/tasks`](https://docs.kraken.com/api-reference/custody-external-api/create-task) with a `request_transfer_to_spot` instruction. |

## Gaps without a direct successor

* **Earn.** There is no Custody `v0` equivalent of the legacy Earn APIs. Staking positions surface
  indirectly through the `staked` component on
  [`GET /v0/insto/custody/vaults/{vault_id}/assets/balances`](https://docs.kraken.com/api-reference/custody-external-api/list-vault-asset-balances)
  and through the `custody_staking*` transaction types.
* **OTC quote and accept.** There are no dedicated OTC quote or acceptance endpoints on Custody
  `v0`. Settled OTC activity appears as `otc_buy` and `otc_sell` transaction types. Use the
  [OTC REST API](https://docs.kraken.com/institutional/api-reference/otc-rest.md) to trade.
