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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/balances'
updated_at: 2026-11-13
---

# Balances

> Subscribe to client asset balances and account ledger transactions

WSS
ws-auth.kraken.com/v2
balances

The `balances` channel streams client asset balances and transactions from the account ledger.

This channel contains account specific data, an authentication token is required in the request.

## Subscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `balances`
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot after subscribing.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **rebased** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`\\
>
> Condition: Effective for viewing xStocks only
>
> If `true`, display in terms of underlying equity, otherwise display in terms of SPV tokens.
>
> **users** `string`
>
> One of: `all`\\
>
> Condition: Available on master accounts only
>
> If `all`, events for master and subaccounts are streamed, otherwise only master account events are published. No snapshot is provided.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `balances`
>
> **snapshot** `boolean`
>
> Indicates if a snapshot is requested.
>
> **warnings** `string[]`
>
> An advisory message, highlighting deprecated fields or upcoming changes to the channel.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot

The snapshot provides the value of each asset held in this account.

**channel** `string`

Value: `balances`

**type** `string`

One of: `snapshot`

**data** `object[]`

A list of assets held on account.

**properties**

**asset** `string`

The asset symbol code.

**asset\_class** `string`

One of: `currency`

The asset class. A placeholder for future expansion.

**balance** `float`

The total amount of asset held across all wallet types.

**wallets** `object[]`

A list of wallets for each asset.

**properties**

**balance** `float`

Balance of asset in wallet.

**type** `string`

One of: `spot`, `earn`

Wallet type.

**id** `string`

One of: `main`, `flex`, `bonded`, `flexible`, `liquid`, `locked`, `closed`

Wallet identifier.

**sequence** `integer`

The subscription message sequence number.

## Update

An update will be streamed on each completed transaction to the client account.

**channel** `string`

Value: `balances`

**type** `string`

One of: `update`

**data** `object[]`

A list of account ledger transactions for each asset.

**properties**

**asset** `string`

The asset symbol code.

**asset\_class** `string`

One of: `currency`

The asset class. A placeholder for future expansion.

**amount** `float`

The amount of asset change in this event.

**balance** `float`

The total amount of this asset held in account.

**fee** `float`

The fee paid on the transaction.

**ledger\_id** `string`

The identifier for this account ledger entry.

**ref\_id** `string`

A reference identifier in the context of this balance event. For example, `ref_id` will be the `trade_id` for a trade event.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The time of the balance change.

**type** `string`

One of: `deposit`, `withdrawal`, `trade`, `margin`, `adjustment`, `rollover`, `credit`, `transfer`, `settled`, `staking`, `sale`, `reserve`, `conversion`, `dividend`, `reward`, `creator_fee`

The broad type of the balance event.

**subtype** `string`

One of: `spotfromfutures`, `spottofutures`, `stakingfromspot`, `spotfromstaking`, `stakingtospot`, `spottostaking`

The specific subtype of the balance event.

**category** `string`

One of: `deposit`, `withdrawal`, `trade`, `margin-trade`, `margin-settle`, `margin-conversion`, `conversion`, `credit`, `marginrollover`, `staking-rewards`, `instant`, `equity-trade`, `airdrop`, `equity-dividend`, `reward-bonus`, `nft`, `block-trade`

The categorization of the balance event.

**wallet\_type** `string`

One of: `spot`, `earn`

Wallet type.

**wallet\_id** `string`

One of: `main`, `bonded`, `flexible`, `liquid`, `locked`

Wallet identifier.

The following combinations of wallet types and wallet identifiers are available:

Wallet type `spot`:

* `main`: Primary spot pairs trading wallet.

Wallet type `earn`:

* `bonded`: earn on-chain product with lockup period.
* `flexible`: earn product without lockup period.
* `liquid`: kraken rewards program.
* `locked`: earn product (may or may not have a lockup period).

**user** `string`

Example: `AA96N74GCGEFN8KI`\\

Condition: Published when request parameters have 'users=all'

The Kraken generated identifier for a user / sub-account.

**sequence** `integer`

The subscription message sequence number.

## Unsubscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `balances`
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `balances`
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "balances",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "balances",
        "snapshot": true
    },
    "success": true,
    "time_in": "2023-10-16T13:29:13.111530Z",
    "time_out": "2023-10-16T13:29:13.111775Z"
}
```

```json Snapshot theme={null}
{
    "channel": "balances",
    "data": [
        {
            "asset": "BTC",
            "asset_class": "currency",
            "balance": 1.2,
            "wallets": [
                {
                    "type": "spot",
                    "id": "main",
                    "balance": 1.2
                }
            ]
        },
        {
            "asset": "MATIC",
            "asset_class": "currency",
            "balance": 500,
            "wallets": [
                {
                    "type": "spot",
                    "id": "main",
                    "balance": 300
                },
                {
                    "type": "earn",
                    "id": "flex",
                    "balance": 200
                }
            ]
        },
        {
            "asset": "USD",
            "asset_class": "currency",
            "balance": 80595.4943,
            "wallets": [
                {
                    "type": "spot",
                    "id": "main",
                    "balance": 80595.4943
                }
            ]
        }
    ],
    "type": "snapshot",
    "sequence": 1
}
```

```json Deposit Update theme={null}
{
   "channel": "balances",
   "type": "update",
   "data": [
      {
         "ledger_id": "ADKKFF-WEA5A-CNUBHG",
         "ref_id": "AGBWUJRU-LAREZ-W3UFAN",
         "timestamp": "2023-09-22T10:23:42.925034Z",
         "type": "deposit",
         "asset": "BTC",
         "asset_class": "currency",
         "category": "deposit",
         "wallet_type": "spot",
         "wallet_id": "main",
         "amount": 0.01,
         "fee": 0.0,
         "balance": 0.02
      }
   ],
   "sequence": 2
}
```

```json Trade Update theme={null}
{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "AAICKV-NMQSR-ZO5IJD",
            "ref_id": "AGBB7L-HT5LX-J3BB4A",
            "timestamp": "2023-09-22T10:33:05.710082Z",
            "type": "trade",
            "asset": "BTC",
            "asset_class": "currency",
            "category": "trade",
            "wallet_type": "spot",
            "wallet_id": "main",
            "amount": -0.005,
            "fee": 0.0,
            "balance": 0.005
        }
    ],
    "sequence": 9
}

{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "A5KS77-LQRMP-SMMN4B",
            "ref_id": "AGBB7L-HT5LX-J3BB4A",
            "timestamp": "2023-09-22T10:33:05.710082Z",
            "type": "trade",
            "asset": "USD",
            "asset_class": "currency",
            "category": "trade",
            "wallet_type": "spot",
            "wallet_id": "main",
            "amount": 132.9995,
            "fee": 0.3458,
            "balance": 500
        }
    ],
    "sequence": 10
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "balances",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "balances"
    },
    "success": true,
    "time_in": "2023-10-16T13:29:13.111530Z",
    "time_out": "2023-10-16T13:29:13.111775Z"
}
```
