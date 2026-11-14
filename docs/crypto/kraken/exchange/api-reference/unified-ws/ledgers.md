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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/ledgers'
updated_at: 2026-11-13
---

# Ledgers

> Subscribe to account ledger entries, with derivatives position and realization detail

UWS
uws.kraken.com/v2/private
ledgers

The `ledgers` channel streams each entry written to the account ledger as it happens. Every entry records one change to one balance: a currency balance in a wallet, or the size of a derivatives position.

Entries produced by derivatives activity carry additional detail, such as the trade and mark price, average entry prices, realized profit and loss, and funding.

For current balances, see the [`balances`](https://docs.kraken.com/exchange/api-reference/unified-ws/balances) channel. For open positions, see the [`positions`](https://docs.kraken.com/exchange/api-reference/unified-ws/positions) channel.

This channel contains account specific data, an authentication token is required in the request.

> [!NOTE]
>
> The channel does not currently support snapshots. Each update carries a `sequence` number per connection. A gap in the sequence means an update was not delivered; use the REST Ledgers endpoint to recover missed entries.

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
> Value: `ledgers`
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
> Value: `ledgers`
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

This channel does not accept an `asset_class` parameter. The ledger is account-wide and records entries for every asset class, so there is nothing to select — read `asset_class` on each entry to tell them apart. Sending `params.asset_class` on a `subscribe` or an `unsubscribe` is rejected with `'params.asset_class' is not valid for the ledgers channel`.

## Update

An update is streamed for each new entry in the account ledger.

**channel** `string`

Value: `ledgers`

**type** `string`

One of: `update`

**data** `object[]`

The ledger entry.

**properties**

**ledger\_id** `string`

The identifier for this account ledger entry.

**timestamp** `string`

Format: RFC3339\\

Example: `2026-10-06T14:36:57.050080Z`

The time of the entry.

**type** `string`

Example: `trade`, `deposit`, `derivativesfuturestrade`, `derivativesflexconversion`, `derivativestransfer`, `derivativesfundingratechange`, `earn`

The type of the ledger entry.

**asset** `string`

The asset whose balance changed: a currency symbol such as `USD`, or a derivatives contract such as `PF_DOGEUSD`.

**asset\_class** `string`

One of: `currency`, `equity`, `tokenized_asset`, `derivatives`

The class of the asset.

**wallet\_type** `string`

Example: `spot`, `earn`, `derivatives_multi_collateral`, `derivatives_single_collateral`, `derivatives_holding`

The type of wallet the entry changed.

**wallet\_id** `string`

Example: `main`, `flexible`, `locked`

The wallet identifier, as in the [`balances`](https://docs.kraken.com/exchange/api-reference/unified-ws/balances) channel. Omitted for wallets that have no identifier.

**amount** `float`

The signed change in the asset's balance, in the asset's units.

**balance** `float`

The balance of the asset in this wallet after the entry. For `derivatives`, the position size after the entry.

**fee** `float`

Condition: Omitted when `asset_class` is `derivatives`.

The fee charged on the entry, in the same asset. The fee is not included in `amount`.

**old\_average\_entry\_price** `float`

Condition: Derivatives position entries.

The position's average entry price before the trade. This is the basis for the realized profit and loss on the matching currency entry.

**new\_average\_entry\_price** `float`

Condition: Derivatives position entries.

The position's average entry price after the trade.

**trade\_price** `float`

Condition: Derivatives position and realization entries.

The price the trade executed at.

**mark\_price** `float`

Condition: Derivatives position and realization entries.

The contract's mark price at the time of the trade.

**realized\_pnl** `float`

Condition: Derivatives realization entries.

The profit or loss realized by the trade, in this entry's asset.

**realized\_funding** `float`

Condition: Derivatives realization entries.

The funding realized with this entry, in this entry's asset.

**funding\_rate** `float`

Condition: Derivatives funding realization entries.

The funding rate applied.

**liquidation\_fee** `float`

Condition: Derivatives liquidation entries.

The liquidation fee charged, in this entry's asset.

**conversion\_spread\_percentage** `float`

Condition: Derivatives flex conversion entries with a non-zero spread.

The spread applied to the conversion, as a percentage.

**event\_uuid** `string`

Condition: Derivatives entries produced by an identified event. Omitted for funding realizations.

The identifier of the event that produced the entry. All entries from the same event share it.

**sequence** `integer`

The connection's message sequence number.

Fields that do not apply to an entry are omitted. A field that is present always has a value, including zero.

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
> Value: `ledgers`
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
> Value: `ledgers`
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
        "channel": "ledgers",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "ledgers"
    },
    "success": true,
    "time_in": "2026-10-06T14:30:13.111530Z",
    "time_out": "2026-10-06T14:30:13.111775Z"
}
```

```json Derivatives Trade theme={null}
{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "LZZNW2-IWX3W-IIJABS",
            "timestamp": "2026-10-06T14:36:57.050080Z",
            "type": "derivativesfuturestrade",
            "asset": "PF_DOGEUSD",
            "asset_class": "derivatives",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -31141,
            "balance": 0,
            "old_average_entry_price": 0.095931,
            "new_average_entry_price": 0.095931,
            "trade_price": 0.095781,
            "mark_price": 0.095803,
            "event_uuid": "e524150e-d04c-04ae-7847-880fa62072c6"
        }
    ],
    "sequence": 9
}

{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "L4QXFJ-2HLKE-7MVRBN",
            "timestamp": "2026-10-06T14:36:57.050080Z",
            "type": "derivativesfuturestrade",
            "asset": "USD",
            "asset_class": "currency",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -4.6619,
            "balance": 2371.7258,
            "fee": 0.5220,
            "trade_price": 0.095781,
            "mark_price": 0.095803,
            "realized_pnl": -4.6628,
            "realized_funding": 0.0009,
            "event_uuid": "e524150e-d04c-04ae-7847-880fa62072c6"
        }
    ],
    "sequence": 10
}
```

```json Flex Conversion theme={null}
{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "LSUZPU-XTG2I-HM545C",
            "timestamp": "2026-10-06T14:04:54.070730Z",
            "type": "derivativesflexconversion",
            "asset": "USDT",
            "asset_class": "currency",
            "wallet_type": "derivatives_multi_collateral",
            "wallet_id": "main",
            "amount": -0.20301399,
            "balance": 133661.49188805,
            "fee": 0.00000000,
            "conversion_spread_percentage": 0.2,
            "event_uuid": "7c3a1d52-6e0f-4b89-9a21-3f5d8c0e1b47"
        }
    ],
    "sequence": 3
}
```

```json Funding theme={null}
{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "LKVARP-WNRPY-HAXF7Q",
            "timestamp": "2026-10-06T18:00:01.176117Z",
            "type": "derivativesfundingratechange",
            "asset": "USD",
            "asset_class": "currency",
            "wallet_type": "spot",
            "wallet_id": "main",
            "amount": -0.8408,
            "balance": 2370.7276,
            "fee": 0.0000,
            "realized_funding": -0.8408,
            "funding_rate": 40.04011101807930481
        }
    ],
    "sequence": 16
}
```

```json Earn theme={null}
{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "L4LQQF-LGPJT-YWE5RW",
            "timestamp": "2026-10-06T18:07:13.940222Z",
            "type": "earn",
            "asset": "BTC",
            "asset_class": "currency",
            "wallet_type": "spot",
            "wallet_id": "main",
            "amount": 0.0000055117,
            "balance": 30.1975399028,
            "fee": 0.0000016535
        }
    ],
    "sequence": 19
}
```

```json Deposit theme={null}
{
    "channel": "ledgers",
    "type": "update",
    "data": [
        {
            "ledger_id": "ADKKFF-WEA5A-CNUBHG",
            "timestamp": "2026-10-06T10:23:42.925034Z",
            "type": "deposit",
            "asset": "BTC",
            "asset_class": "currency",
            "wallet_type": "spot",
            "wallet_id": "main",
            "amount": 0.01,
            "balance": 0.02,
            "fee": 0.0
        }
    ],
    "sequence": 1
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "ledgers",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "ledgers"
    },
    "success": true,
    "time_in": "2026-10-06T14:40:13.111530Z",
    "time_out": "2026-10-06T14:40:13.111775Z"
}
```
