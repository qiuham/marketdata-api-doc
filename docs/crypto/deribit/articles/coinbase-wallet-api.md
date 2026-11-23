---
exchange: deribit
source_url: https://docs.deribit.com/articles/coinbase-wallet-api
api_type: Guide
updated_at: 2026-11-23 19:00:29.362841
---

# Coinbase Wallet API

> Wallet API behavior for Coinbase-custodied Deribit accounts: network selection, deposit addresses, address book and CTN counterparties, and withdrawals.

Accounts whose wallet is custodied by Coinbase use the same wallet methods as
every other account, but a single currency can exist on more than one blockchain
network. Because an address is only meaningful together with its network, these
methods take an extra `network` parameter, address book entries carry their own
identifier, and withdrawals can also be sent to a Coinbase Travel Network (CTN)
counterparty instead of an on-chain address.

## Discovering the available networks

Networks are identified by a **network resource name** such as
`networks/ethereum-mainnet`, and this string is the value you pass as `network`.
Do not construct it yourself. Read it from
[`public/get_currencies`](https://docs.deribit.com/api-reference/market-data/public-get_currencies).
Every Coinbase wallet currency includes a `coinbase_networks` array. It usually
contains at least one network, but it can be empty for SEI on production and for
more currencies on testnet.

### Example Response

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "currency": "ETH",
      "currency_long": "Ethereum",
      "coinbase_networks": [
        {
          "resource_name": "networks/ethereum-mainnet",
          "display_name": "Ethereum"
        }
      ]
    }
  ]
}
```

Each entry has a `resource_name` to send to the API and a `display_name` to show
to a user. `coinbase_networks` can be empty for SEI on production and for more
currencies on testnet. An empty array means that currency has no network to pass
to wallet methods.

[`private/create_deposit_address`](https://docs.deribit.com/api-reference/wallet/private-create_deposit_address),
[`private/get_current_deposit_address`](https://docs.deribit.com/api-reference/wallet/private-get_current_deposit_address)
and `private/add_to_address_book` validate `network` against the currency's
`coinbase_networks` and reject one that is not configured for it. Elsewhere
(`private/withdraw`, the update and remove methods and
`private/set_address_requires_security_key`), `network` is only used to select an
existing address book entry, so an unknown value fails to match. The method
[`private/coinbase/estimate_withdrawal_fee`](https://docs.deribit.com/api-reference/wallet/private-estimate_withdrawal_fee)
is restricted to Coinbase wallet type accounts.

## Deposit addresses

[`private/create_deposit_address`](https://docs.deribit.com/api-reference/wallet/private-create_deposit_address)
requires both `currency` and `network`, so each currency and network combination
has its own deposit address. An optional `label` can be supplied, which defaults
to `"deposit address"`.

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/create_deposit_address",
  "params": {
    "currency": "ETH",
    "network": "networks/ethereum-mainnet",
    "label": "Treasury inflows"
  },
  "id": 1
}
```

### Response

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b",
    "currency": "ETH",
    "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "type": "deposit",
    "kind": "onchain",
    "label": "Treasury inflows",
    "creation_timestamp": 1719993033041,
    "updated_timestamp": 1719993033041,
    "status": "active",
    "waiting_timestamp": null,
    "requires_confirmation": false,
    "requires_confirmation_change": false,
    "requires_security_key": false,
    "info_required": true,
    "network": "networks/ethereum-mainnet",
    "network_display_name": "Ethereum",
    "tag": ""
  }
}
```

`tag` is only returned for networks which use a destination tag, for example
XRPL. Deposit addresses always report `info_required` as `true`; the flag concerns
withdrawal beneficiary data and has no meaning for a deposit address.

This method is get-or-create. If an address already exists for the currency and
network it is returned unchanged, which means a `label` sent on a later call is
ignored rather than applied. Use
[`private/get_current_deposit_address`](https://docs.deribit.com/api-reference/wallet/private-get_current_deposit_address)
to read the existing address without attempting to create one; it also requires
`network` and returns `null` when nothing has been created yet.

> [!WARNING]
>
> A deposit address is only valid on the network it was created for. Sending funds
> to it over a different network may make them unrecoverable.

## Address book entries

Every entry has an `id`, a UUID7 assigned by Deribit and returned by
[`private/get_address_book`](https://docs.deribit.com/api-reference/wallet/private-get_address_book).
Because the same address can be whitelisted on several networks, an entry is
identified in one of two ways:

* By `id`. This is unambiguous and is the recommended approach.
* By `address`, adding `network` and `tag` where needed.

The `kind` field distinguishes the two sorts of destination:

| `kind` | Destination |
| - | - |
| `onchain` | A blockchain address on a specific network |
| `ctn` | A Coinbase Travel Network counterparty, identified by a counterparty ID rather than an address |

Accepted `type` values differ per method:

| Method | Accepted `type` |
| - | - |
| `private/add_to_address_book` | `withdrawal`, `transfer` |
| `private/update_in_address_book` | `withdrawal`, `transfer` |
| `private/remove_from_address_book` | `withdrawal`, `transfer` |
| `private/get_address_book` | `withdrawal`, `transfer`, `deposit` |

`deposit_source` is not used. Deposit entries are created by
`private/create_deposit_address` rather than added by hand, which is why
`deposit` is readable but not writable.

The `status` field reports availability: `waiting` while your account's
withdrawal delay is still pending, `ready` once the entry can be used, and
`active` for deposit addresses. Fields that were never set (`tag` and `network`
on CTN entries, and any Travel Rule field you did not supply) are omitted from
address book responses rather than returned as `null`, so test for presence. The
exception is a deposit entry, which reports `tag` as an empty string; these are
returned by `type: "deposit"` as well as by the deposit address methods.

### Listing entries, including CTN counterparties

CTN counterparties work with any asset, so they are stored under `"all"` rather
than under a specific currency like ETH or BTC.

> [!WARNING]
>
> `private/get_address_book` returns only entries for the `currency` you pass. A
> call with `currency: "ETH"` therefore omits CTN counterparties. List those with
> a second call using `currency: "all"`. Make both calls if you need every
> withdrawal destination.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/get_address_book",
  "params": {
    "currency": "all",
    "type": "withdrawal"
  },
  "id": 2
}
```

### Adding an on-chain address

[`private/add_to_address_book`](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book)
requires `type` and `label`, plus `currency`, `address` and `network`. Add `tag`
for networks that use a destination tag or memo.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/add_to_address_book",
  "params": {
    "currency": "ETH",
    "type": "withdrawal",
    "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "network": "networks/ethereum-mainnet",
    "label": "Main address",
    "name": "Alice Smith",
    "country": "NL"
  },
  "id": 3
}
```

### Adding a CTN counterparty

Supply `counterparty_id` instead of `address` and `network`, and omit `currency`.
The entry is stored under `"all"`.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/add_to_address_book",
  "params": {
    "type": "withdrawal",
    "counterparty_id": "cp-8f3e2a1b9c4d",
    "label": "CTN Partner"
  },
  "id": 4
}
```

### Travel Rule data

Beneficiary information is supplied on **on-chain** entries when adding or
updating them. The legacy `beneficiary_*`, `agreed` and `personal` parameters are
not used, and `extra_currencies` is not supported.

`name` and `country` are the two fields that matter operationally: together they
satisfy the Travel Rule requirement, clear `info_required`, and are the values
forwarded with the withdrawal. The remaining fields are stored alongside them as
supplementary detail.

| Parameter | Description |
| - | - |
| `name` | Full name of the beneficiary, person or organization. Required to satisfy the Travel Rule |
| `country` | Beneficiary country code, ISO 3166-1 alpha-2. Required to satisfy the Travel Rule |
| `address` | Beneficiary address. On an on-chain entry this is the same value as the destination address |
| `financial_institution` | Institution holding the beneficiary account |
| `account` | Account identifier at that institution |
| `account_location` | Location of the beneficiary account |
| `entity_type` | `organization` or `individual` |
| `wallet_type` | `exchange` or `self_hosted` |
| `is_self` | `true` when the beneficiary is the account owner |

Once any of this data is stored the entry returns `beneficiary_created` and
`beneficiary_updated` timestamps. A withdrawal that needs Travel Rule data and
does not have `name` and `country` is rejected. On the usual confirmation path
this happens when the withdrawal is confirmed rather than when it is created, so
`private/withdraw` can return `prepared` and the withdrawal then fail with
`travel_rule_data_required`. Supply both fields when whitelisting an address you
intend to withdraw to.

> [!NOTE]
>
> CTN entries do not store beneficiary data. Travel Rule fields sent with a
> `counterparty_id` are accepted but discarded, such entries always report
> `info_required` as `true`, and they never return the `beneficiary_*` timestamps.
> Counterparty identity is already established within the Travel Network, so CTN
> withdrawals are not blocked by this.

### Updating and removing entries

[`private/update_in_address_book`](https://docs.deribit.com/api-reference/wallet/private-update_in_address_book)
takes `currency` and `type`, plus either `address` or `id`. `label` is optional
here, and the method returns the updated entry rather than `"ok"`.

[`private/remove_from_address_book`](https://docs.deribit.com/api-reference/wallet/private-remove_from_address_book)
takes the same identifying parameters and returns `"ok"`.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/update_in_address_book",
  "params": {
    "currency": "ETH",
    "type": "withdrawal",
    "id": "0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b",
    "label": "Updated label"
  },
  "id": 5
}
```

### Resolving an entry by address

When you identify an entry by `address` rather than `id`, Deribit narrows the
candidates by `tag` first and then by `network`:

* If several entries share the address and all of them carry a tag, omitting
  `tag` is rejected, whether or not the tags differ.
* If some candidates have a tag and others do not, omitting `tag` selects the
  untagged ones.
* If more than one candidate still remains and `network` was not supplied, the
  call is rejected.

Because tag narrowing runs first, an address whitelisted on two networks can
still resolve without `network` when only one of the two entries is untagged.
Pass `id`, or `address` together with `network` and `tag`, whenever you need to
be certain which entry you are acting on.

### Requiring a security key per address

[`private/set_address_requires_security_key`](https://docs.deribit.com/api-reference/wallet/private-set_address_requires_security_key)
controls whether withdrawals to one entry need security key approval. It takes
`currency`, `type` and `value`, plus either `address` or `id`, and returns the
updated entry. It requires only the `wallet:read_write` scope. Unlike the legacy
wallet type, it does not additionally require `mainaccount`, so a subaccount can
call it for its own entries.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/set_address_requires_security_key",
  "params": {
    "currency": "ETH",
    "type": "withdrawal",
    "id": "0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b",
    "value": true
  },
  "id": 6
}
```

## Creating a withdrawal

[`private/withdraw`](https://docs.deribit.com/api-reference/wallet/private-withdraw) requires `currency`
and `amount`, plus either `address` or `id`. The destination must already exist
in the address book. When identifying it by `address`, pass `network` (and `tag`
where applicable) for an on-chain destination, or pass the counterparty ID as
`address` for a CTN destination.

The `priority` and `nonce` parameters are not used.

> [!WARNING]
>
> Because `nonce` is ignored, Coinbase withdrawals have no request idempotency. A
> retried `private/withdraw` creates a second withdrawal rather than returning the
> first, so retry only after confirming the outcome with
> [`private/get_withdrawals`](https://docs.deribit.com/api-reference/wallet/private-get_withdrawals).

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/withdraw",
  "params": {
    "currency": "ETH",
    "id": "0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b",
    "amount": 0.5
  },
  "id": 7
}
```

### Response

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 7,
  "result": {
    "id": "01912f4e-8b6a-7c1d-9e2f-3a4b5c6d7e8f",
    "currency": "ETH",
    "state": "prepared",
    "amount": 0.5,
    "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "network": "networks/ethereum-mainnet",
    "network_display_name": "Ethereum",
    "created_timestamp": 1719993033041,
    "updated_timestamp": 1719993033041,
    "note": ""
  }
}
```

The `id` here is the withdrawal's own identifier and is unrelated to the address
book `id` used to select the destination.

### Withdrawal states

| `state` | Meaning |
| - | - |
| `prepared` | Created and awaiting email confirmation |
| `awaiting_second_email` | Confirmed once, awaiting the second confirmation where a secondary email is configured |
| `unconfirmed` | Submitted to the custodian, not yet settled |
| `completed` | Settled by the custodian |
| `cancelled` | Cancelled before settlement |

A new withdrawal starts as `prepared` and requires email confirmation. Entries
whose `requires_confirmation` is `false` and whose delay has elapsed are
**trusted**, and withdrawals to them skip confirmation and are submitted
immediately, so they start at `unconfirmed`. Since `requires_confirmation`
defaults to `true`, expect the confirmation path unless you have explicitly
turned it off for that entry.

> [!NOTE]
>
> `transfer_idem` is the idempotency key shared with the custodian and appears only
> once the withdrawal has been submitted, so it is absent while a withdrawal is
> `prepared`. As with the rest of the response, unset fields are omitted;
> `transaction_id` appears only after the transaction has been broadcast.

## Estimating the withdrawal fee

[`private/coinbase/estimate_withdrawal_fee`](https://docs.deribit.com/api-reference/wallet/private-estimate_withdrawal_fee)
returns the expected network fee for a currency and network. Note that this
method names the parameter `network_name`, not `network`.

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/coinbase/estimate_withdrawal_fee",
  "params": {
    "currency": "BTC",
    "network_name": "networks/bitcoin-mainnet"
  },
  "id": 8
}
```

### Response

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 8,
  "result": {
    "estimated_fee": "0.0005",
    "estimated_fee_before_subsidy": "0.001",
    "expires_at": "2026-04-06T12:00:00Z"
  }
}
```

`estimated_fee` is returned as a **string** to preserve precision, and
`estimated_fee_before_subsidy` is the amount before any fee subsidy is applied.
It falls back to `estimated_fee` when the custodian does not report it, so the two
being equal does not by itself mean no subsidy applied. `expires_at` is a
timestamp after which the estimate should no longer be relied on, and is `null`
when the custodian does not supply one. The estimate is indicative: the fee
charged at settlement may differ. Parse these values defensively. They are
passed through from the custodian.

## Subaccount withdrawals

Subaccounts cannot withdraw unless the main account has allowed it. The main
account controls this with
[`private/set_coinbase_subaccount_withdrawals_allowed`](https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed),
which takes a single `enabled` boolean and echoes it back. Calling it from a
subaccount is rejected. While disabled, `private/withdraw` from a subaccount
fails with a permission error.

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/set_coinbase_subaccount_withdrawals_allowed",
  "params": {
    "enabled": true
  },
  "id": 9
}
```

## Differences from the legacy wallet type

| Area | Legacy wallet type | Coinbase wallet type |
| - | - | - |
| Network | Implied by the currency | Explicit `network`, discovered from `coinbase_networks` |
| Entry identity | `currency` and `address` | `id`, or `address` with `network` and `tag` |
| Destinations | On-chain addresses | On-chain addresses and CTN counterparties |
| Address book `type` | `withdrawal`, `transfer`, `deposit_source` | `withdrawal`, `transfer`, plus `deposit` when reading |
| Travel Rule fields | `beneficiary_*`, `agreed`, `personal` | `name` and `country`, plus supplementary fields |
| Withdrawal fee | Chosen with `priority` | Set by the custodian; estimate via `private/coinbase/estimate_withdrawal_fee` |
| Withdrawal idempotency | `nonce` deduplicates retries | None |
| Withdrawal result | Legacy withdrawal object | Coinbase withdrawal object with `state` and `transfer_idem` |
| Currency scope | Wallet currencies | Any portfolio currency, or `"all"` for CTN entries |
| Address book management | Main account only, except `deposit_source` | Subaccounts can manage their own entries |

## Notes and best practices

* **Always read network names from the API.** Treat `resource_name` as an opaque string and never hardcode or derive it, so that newly supported networks work without a client change.
* **Prefer `id` over `address`.** Identifying an entry by `id` avoids the tag and network ambiguity described above, and avoids sending the address on every call.
* **Query `currency: "all"` as well.** CTN counterparties are invisible to a per-currency `private/get_address_book` call.
* **Supply `name` and `country` when whitelisting.** Without them an on-chain entry stays at `info_required: true` and withdrawals that need Travel Rule data are rejected.
* **Do not blindly retry withdrawals.** There is no `nonce`, so a retry creates a second withdrawal.
* **Test for presence, not for `null`.** Unset fields are omitted from address book and withdrawal responses.
* **Re-check the fee near submission.** Fee estimates expire, and the amount charged at settlement can differ from the estimate.
* **Enable subaccount withdrawals deliberately.** The setting is off by default and can only be changed by the main account.
* **Match the tag to the network.** Networks that use a destination tag or memo need `tag` both when whitelisting the address and when withdrawing to it by address.


## Related topics

- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [private/set_coinbase_subaccount_withdrawals_allowed](https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed.md)
- [private/coinbase/estimate_withdrawal_fee](https://docs.deribit.com/api-reference/wallet/private-estimate_withdrawal_fee.md)
- [private/get_current_deposit_address](https://docs.deribit.com/api-reference/wallet/private-get_current_deposit_address.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)