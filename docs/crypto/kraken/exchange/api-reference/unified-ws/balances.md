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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/balances'
updated_at: 2026-11-13
---

# Balances

> Subscribe to client asset balances and account ledger transactions

UWS
uws.kraken.com/v2/private
balances

The `balances` channel streams client asset balances and transactions from the account ledger.

For derivatives margin requirements, margin equity, and available margin, see the [`margin`](https://docs.kraken.com/exchange/api-reference/unified-ws/margin) channel.

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

This channel does not accept an `asset_class` parameter. Balances are account-wide and cover every asset class at once, so there is nothing to select. Sending `params.asset_class` on a `subscribe` or an `unsubscribe` is rejected with `'params.asset_class' is not valid for the balances channel`.

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

**amount** `float`

The amount of asset change in this event.

**balance** `float`

The total amount of this asset held in account.

**fee** `float`

The fee paid on the transaction.

**ledger\_id** `string`

The identifier for this account ledger entry.

**ref\_id** `string`

A reference identifier in the context of this balance event. For example, `ref_id` will be the `trade_id` for a trade event. This will not be present for Futures balance events.

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
            "balance": 38.1945934387,
            "wallets": [
                {
                    "type": "derivatives_holding",
                    "id": "main",
                    "balance": 8.0000915543
                },
                {
                    "type": "derivatives_multi_collateral",
                    "id": "main",
                    "balance": 30.1299090600
                },
                {
                    "type": "derivatives_single_collateral",
                    "id": "WI7B2YF-UNVGD-NSX6RD",
                    "balance": 0.0000006143
                },
                {
                    "type": "spot",
                    "id": "main",
                    "balance": 0.0645922101
                }
            ]
        },
        {
            "asset": "MATIC",
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

```json Multi-collateral Wallet Transfer theme={null}
{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LZDO5L-2CS66-QBCCBG",
            "timestamp": "2026-06-23T12:57:29.627269Z",
            "type": "derivativestransfer",
            "asset": "USD",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -1.0000,
            "fee": 0.0000,
            "balance": 20411.3030
        }
    ]
}

{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LKBFAQ-EEU5S-D2BRPD",
            "timestamp": "2026-06-23T12:57:29.627269Z",
            "type": "derivativestransfer",
            "asset": "USD",
            "wallet_type": "derivatives_holding",
            "wallet_id": "main",
            "amount": 1.0000,
            "fee": 0.0000,
            "balance": 4854.0000
        }
    ]
}
```

```json Single-collateral Wallet Transfer theme={null}
{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LTIQCL-PL4KB-QJVT7T",
            "timestamp": "2026-06-23T12:57:36.353598Z",
            "type": "derivativestransfer",
            "asset": "LTC",
            "wallet_type": "derivatives_single_collateral",
            "wallet_id": "WIXQGPY-AJIM5-JVEGD4",
            "amount": -0.0232000000,
            "fee": 0.0000000000,
            "balance": 94.9853793615
        }
    ]
}

{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LGATKY-YZ6UG-PVFDXS",
            "timestamp": "2026-06-23T12:57:36.353598Z",
            "type": "derivativestransfer",
            "asset": "LTC",
            "wallet_type": "derivatives_holding",
            "wallet_id": "main",
            "amount": 0.0232000000,
            "fee": 0.0000000000,
            "balance": 95.0773793615
        }
    ]
}
```

```json Derivatives Trade theme={null}
{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LSUZPU-XTG2I-HM545C",
            "timestamp": "2026-06-23T14:04:54.070730Z",
            "type": "derivativesflexconversion",
            "asset": "USDT",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -0.20301399,
            "fee": 0.00000000,
            "balance": 133661.49188805
        }
    ]
}

{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "L3CNEO-YSZPB-2B3EO7",
            "timestamp": "2026-06-23T14:04:54.070730Z",
            "type": "derivativesflexconversion",
            "asset": "USD",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": 0.2026,
            "fee": 0.0000,
            "balance": 0.2026
        }
    ]
}

{
    "channel": "balances",
    "type": "update",
    "data": [
        {
            "ledger_id": "LAU7WC-7H5U7-T5LQB4",
            "timestamp": "2026-06-23T14:04:54.070730Z",
            "type": "derivativesfuturestrade",
            "asset": "USD",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -0.2019,
            "fee": 0.0007,
            "balance": 0.0000
        }
    ]
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
