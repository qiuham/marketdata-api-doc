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
source_url: 'https://docs.kraken.com/exchange/guides/general/subaccounts'
updated_at: 2026-11-13
---

# Sub-accounts and multi-account management

> How to structure and operate multiple accounts via the API — sub-account creation, fund transfers, and FIX broker management

Institutional clients and professional traders often need to manage multiple accounts — separate strategies, separate risk buckets, or managing on behalf of clients. This page covers the API capabilities for multi-account setups.

## Sub-account model

A **master account** can create and manage **sub-accounts** (also called subaccounts). Each sub-account:

* Has its own balance
* Can have its own API keys
* Shares the master account's trading rate limit via the Domain Rate Limit (5× the individual account limit, pooled across all sub-accounts)
* Is accessible from the master account via the sub-account management endpoints

## Creating a sub-account

```bash theme={null}
POST /0/private/CreateSubaccount

# Required permissions: Create & Modify Orders (on master account)
```

**Parameters:**

| Parameter | Description |
| :- | :- |
| `username` | Unique username for the sub-account |
| `email` | Email address for the sub-account |

```json theme={null}
{
  "error": [],
  "result": true
}
```

After creation, the sub-account owner receives an email to complete setup.

## Transferring funds between accounts

Use `AccountTransfer` to move funds between master and sub-accounts in either direction.

```bash theme={null}
POST /0/private/AccountTransfer
```

**Parameters:**

| Parameter | Description |
| :- | :- |
| `asset` | Asset to transfer (e.g. `XBT`, `ETH`, `USD`) |
| `amount` | Amount to transfer |
| `from` | Sending account (username or account ID) |
| `to` | Receiving account (username or account ID) |

```json theme={null}
{
  "error": [],
  "result": {
    "transfer_id": "TOH3AS2-LPCWR8-JDQGEU",
    "status": "complete"
  }
}
```

> [!NOTE]
>
> Transfers between accounts are instant and do not incur fees. Both accounts must be under the same master account.

## Per-account API keys

Each sub-account can have its own API keys with independent permission sets. This lets you:

* Give a market data service read-only keys on a sub-account
* Give a strategy read/write keys scoped to that sub-account only
* Revoke a single key without affecting other strategies

Generate keys via [Settings → API](https://www.kraken.com/u/security/api) while logged in to the specific sub-account.

## Domain rate limit

Spot rate limits normally apply at the account level. When using sub-accounts, the **Domain Rate Limit** applies: the master account and all sub-accounts share a pooled limit equal to **5× the individual account limit**.

This gives multi-strategy setups significantly more throughput than running everything on a single account.

| Account type | Spot rate limit |
| :- | :- |
| Single account (Starter) | Counter threshold: 60 |
| Single account (Intermediate) | Counter threshold: 125 |
| Single account (Pro) | Counter threshold: 180 |
| Domain (master + sub-accounts) | 5× individual tier limit |

## FIX broker allocation model

Tags 78 and 79 are not sub-account management — they are part of the **FIX broker model**, which allows a prime broker to allocate orders to client accounts within a single FIX session. This is distinct from Kraken's sub-account feature.

| FIX Tag | Name | Description |
| :- | :- | :- |
| 78 | `NoAllocs` | Number of allocation entries |
| 79 | `AllocAccount` | Client account identifier for this allocation |

A broker uses this to route orders on behalf of multiple end clients without opening a separate FIX session per client. The broker holds a single FIX session and tags each order with the target client account.

> [!NOTE]
>
> FIX broker allocation via Tags 78/79 was added in May 2025. Contact your Account Manager to enable this for your FIX session.

## Portfolio-level view

To aggregate balances across master + all sub-accounts, call `Balance` or `BalanceEx` once per account. There is no single endpoint that returns an aggregated portfolio view — you must sum across accounts programmatically.

```python theme={null}
accounts = ["master", "sub1", "sub2", "sub3"]
total_balances = {}

for account in accounts:
    # Use the API key for each account
    balances = get_balance(api_key=keys[account])
    for asset, amount in balances.items():
        total_balances[asset] = total_balances.get(asset, 0) + float(amount)
```

## Futures sub-accounts

Futures has its own sub-account management:

```bash theme={null}
# List sub-accounts
GET /derivatives/api/v3/subaccounts

# Check trading enabled status
GET /derivatives/api/v3/subaccount/{subaccountUid}/trading-enabled

# Enable/disable trading
PUT /derivatives/api/v3/subaccount/{subaccountUid}/trading-enabled
```

Futures also supports cross-account transfers:

```bash theme={null}
POST /derivatives/api/v3/transfer/subaccount
```

## Common patterns

**Strategy isolation:** create one sub-account per strategy. Each strategy has its own balance, its own API keys, and its own risk perimeter. A blown strategy can't draw from other strategies' funds.

**Read-only monitoring:** create a sub-account with Query Funds + Query Open Orders keys only. Use this for your monitoring dashboard, keeping trading keys separate.

**Gradual rollout:** fund a sub-account with a small allocation while testing a new strategy in production. Scale up by transferring more funds once validated.

## Related guides

> [card] [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)
>
> Configure independent permission sets for each sub-account's keys

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> Domain rate limit — how throughput pools across master and sub-accounts

> [card] [API comparison](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> Sub-account management across REST and FIX (Tags 78/79)
