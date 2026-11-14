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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-rest'
updated_at: 2026-11-13
---

# Prime REST

> Programmatic access to Kraken Prime — API-user management, key lifecycle, and settlement

The Prime REST API provides programmatic access to Kraken's Prime brokerage
services. Use it to manage Prime API users and their keys, and to drive
the settlement lifecycle for Prime trading activity.

For trade execution and live exposure data, pair Prime REST with the
[Prime WebSocket API](https://docs.kraken.com/institutional/api-reference/prime-websocket/authentication.md) (real-time)
or the [Prime FIX API](https://docs.kraken.com/institutional/api-reference/prime-fix/logon.md)
(session-based, deterministic ordering).

> [!NOTE]
>
> Access to Prime requires onboarding. Contact
> [prime\_trading@kraken.com](mailto:prime_trading@kraken.com) or your Account
> Manager to begin.

## Connection

```text theme={null}
https://api.kraken.com/0
```

## Authentication

Prime REST uses the same HMAC-SHA512 signature scheme as the Spot REST API.
See the [Spot REST authentication
guide](https://docs.kraken.com/exchange/guides/rest/authentication.md) for the exact request signing
flow — the algorithm, headers, and nonce handling are identical.

Sign requests with a standard Kraken API key that has the permissions listed
below. API keys created for Prime API users with
[`CreatePrimeApiUserKey`](https://docs.kraken.com/api-reference/api-user-keys/create-prime-api-user-key)
are for the Prime WebSocket API only.

### API key permissions

| Endpoints | Required key permissions | Also required for organization keys |
| :- | :- | :- |
| `GetPrimeSettlementBatch`, `ListPrimeSettlementBatches` | **Orders and trades – Query open orders & trades** and **Orders and trades – Query closed orders & trades** | None |
| `CreatePrimeSettlementBatch`, `SettlePrimeSettlementBatchAsset` | **Orders and trades – Create & modify orders** | **Prime Ops** |
| `CreatePrimeApiUser`, `UpdatePrimeApiUser`, `UpdatePrimeApiUserRoles` | **Orders and trades – Create & modify orders** | **Prime Ops** |
| `CreatePrimeApiUserKey`, `UpdatePrimeApiUserKey`, `DeletePrimeApiUserKey` | **Orders and trades – Create & modify orders** | **Prime Ops** |
| `GetPrimeApiUser`, `ListPrimeApiUsers`, `ListPrimeApiUserKeys` | None — any valid API key with access to the Prime account | **Prime Ops** |

If your Prime account belongs to an organization, enable **Prime Ops** on the
API key in addition to the permissions above. Requests from an organization
key without **Prime Ops** are rejected with
`EGeneral:Permission denied:prime ops`.

## Typical workflow

**1. Create an API user**

Call [`CreatePrimeApiUser`](https://docs.kraken.com/api-reference/api-users/create-prime-api-user)
with either a `Viewer` (read-only) or `Trader` (read + trade) role.

**2. Generate an API key**

Call [`CreatePrimeApiUserKey`](https://docs.kraken.com/api-reference/api-user-keys/create-prime-api-user-key)
to issue credentials for the user. **The API secret is returned once
at creation time** — store it securely; it cannot be retrieved later.

**3. Trade**

Execute trades over Prime WebSocket or Prime FIX using the issued
credentials. Trades book against your Prime credit line.

**4. Snapshot a settlement batch**

At the end of a trading period, call
[`CreatePrimeSettlementBatch`](https://docs.kraken.com/api-reference/settlement/create-prime-settlement-batch)
to capture all unsettled trades into a batch. Each batch contains legs
representing the net position per asset, and `trade_ids` listing the
trade IDs included in the snapshot. Only one batch per `asset_kind` can
be active at a time.

**5. Wait for Kraken to confirm the batch**

A new batch has `confirmed: false` until Kraken confirms it. There is no
confirm endpoint. Poll
[`GetPrimeSettlementBatch`](https://docs.kraken.com/api-reference/settlement/get-prime-settlement-batch)
until `batch.attributes.confirmed` is `true` before you settle. Calling
`SettlePrimeSettlementBatchAsset` on an unconfirmed batch returns
`EOTC:Conflict:settlement batch is not confirmed`.

**6. Settle each outgoing leg**

For each `outgoing` leg you owe (where `can_settle` is `true`), call
[`SettlePrimeSettlementBatchAsset`](https://docs.kraken.com/api-reference/settlement/settle-prime-settlement-batch-asset)
to initiate the transfer. Kraken settles `incoming` legs. Track progress and retrieve `trade_ids` via
[`GetPrimeSettlementBatch`](https://docs.kraken.com/api-reference/settlement/get-prime-settlement-batch).

## Endpoint groups

> [card] [API Users](https://docs.kraken.com/api-reference/api-users/create-prime-api-user.md)
>
> Create, list, get, and update Prime API users. Manage user roles.

> [card] [API User Keys](https://docs.kraken.com/api-reference/api-user-keys/create-prime-api-user-key.md)
>
> Issue, list, update, and delete API keys for a Prime user.

> [card] [Settlement](https://docs.kraken.com/api-reference/settlement/create-prime-settlement-batch.md)
>
> Snapshot trades into batches and settle each leg.

## Roles

| Role | Access |
| :- | :- |
| `Viewer` | Read-only — query orders, balances, and exposure |
| `Trader` | Read + trade — submit and amend orders, in addition to all `Viewer` permissions |

The role is set at user creation and can be changed via
[`UpdatePrimeApiUserRoles`](https://docs.kraken.com/api-reference/api-users/update-prime-api-user-roles).

## Key lifecycle

API keys are tied to an API user, not directly to a Prime account. A user
may have multiple keys; revoking a key does not affect other keys for the
same user.

* **`CreatePrimeApiUserKey`** — issues a key pair; the secret is returned
  once and never persisted server-side.
* **`UpdatePrimeApiUserKey`** — rotate the IP allow-list or other key
  metadata.
* **`DeletePrimeApiUserKey`** — immediate revocation; subsequent requests
  signed with the deleted key fail authentication.

## Errors

Responses include `result` and `error`. On success, `error` is an empty array.

Common error prefixes:

| Prefix | Meaning |
| :- | :- |
| `EOTC:Invalid arguments` | Invalid or missing request fields, or resource not found |
| `EOTC:Conflict` | Request conflicts with current state |
| `EGeneral:Permission denied` | The API key lacks a required permission |
| `EAPI:Invalid key` | The API key is not valid |
| `EService:Unavailable` | Service temporarily unavailable |
| `EGeneral:Internal error` | Unexpected server error (HTTP 500) |

Settlement errors you may encounter:

| Error | Meaning |
| :- | :- |
| `EOTC:Conflict:client already has an active settlement batch for this kind` | A batch of this `asset_kind` is still open. Settle it before you create another. |
| `EOTC:Invalid arguments:no trades to settle for asset kind <kind>` | There are no unsettled trades to capture. |
| `EOTC:Conflict:settlement batch is not confirmed` | Wait until `confirmed` is `true` on `GetPrimeSettlementBatch`, then retry. |
| `EOTC:Conflict:settlement batch leg is locked` | The leg is already settled or being settled. |

## Related

> [card] [Prime WebSocket](https://docs.kraken.com/institutional/api-reference/prime-websocket.md)
>
> Real-time order entry, executions, exposure, and balance streaming.

> [card] [Prime FIX](https://docs.kraken.com/institutional/api-reference/prime-fix.md)
>
> Session-based order entry with deterministic ordering and replay.

> [card] [Spot REST authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> HMAC-SHA512 signing flow shared with Prime REST.

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> REST vs WebSocket vs FIX trade-offs.
