---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/balances
api_type: WebSocket
updated_at: 2026-05-27 20:11:12.388897
---

# Balances

CHANNEL
**Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `balances` (Authentication Required)
The `balances` channel streams client asset balances and transactions from the account ledger.

This channel contains account specific data, an authentication token is required in the request.

## Subscribe Request

  * Subscribe Schema
  * Subscribe Ack Schema
  * Example: Subscribe
  * Example: Subscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `balances`

    ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

Request a snapshot after subscribing.

    ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**rebased** `boolean` *conditional*

**Condition:** Effective for viewing xstocks only. 

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

If `true`, display in terms of underlying equity, otherwise display in terms of SPV tokens.

**users** `string` *conditional*

**Condition:** Available on master accounts only. 

**Value:** `all`

If `all`, events for master and subaccounts are streamed, otherwise only master account events are published. No snapshot is provided.

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `balances`

    ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if a snapshot is requested.

    ↳ **warnings** `array of strings`

An advisory message, highlighting deprecated fields or upcoming changes to the channel.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "subscribe",  
        "params": {  
            "channel": "balances",  
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"  
        }  
    }  
    
    
    
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
    

## Snapshot Response

The snapshot provides the value of each asset held in this account.

  * Snapshot Schema
  * Example: Snapshot

### MESSAGE BODY

**channel** `string`

**Value:** `balances`

**type** `string`

**Value:** `snapshot`

**data** `array [`

A list of assets held on account.

**[many] asset** object

    ↳ **asset** `string`

The asset symbol code.

    ↳ **asset_class** `string`

**Value:** `currency`

The asset class. A placeholder for future expansion.

    ↳ **balance** `float`

The total amount of asset held across all wallet types.

    ↳ **wallets** `array [`

A list of wallets for each asset.

**[many] wallet** object

        ↳ **balance** `float`

Balance of asset in wallet.

        ↳ **type** `string`

**Possible values:**[`spot`, ` earn`] 

Wallet type.

        ↳ **id** `string`

**Possible values:**[`main`, `flex`, `bonded`, `flexible`, `liquid`, `locked`, `closed`] 

Wallet identifier.

]

]

        ↳ **sequence** `integer`

The subscription message sequence number.
    
    
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
    

## Update Response

An update will be streamed on each completed transaction to the client account.

  * Update Schema
  * Example: Deposit Update
  * Example: Trade Update

### MESSAGE BODY

**channel** `string`

**Value:** `balances`

**type** `string`

**Value:** `update`

**data** `array [`

A list of account ledger transactions for each asset.

**[many] ledger_transaction** object

    ↳ **asset** `string`

The asset symbol code.

    ↳ **asset_class** `string`

**Value:** `currency`

The asset class. A placeholder for future expansion.

    ↳ **amount** `float`

The amount of asset change in this event.

    ↳ **balance** `float`

The total amount of this asset held in account.

    ↳ **fee** `float`

The fee paid on the transaction.

    ↳ **ledger_id** `string`

The identifier for this account ledger entry.

    ↳ **ref_id** `string`

A reference identifier in the context of this balance event. For example, `ref_id` will be the `trade_id` for a trade event.

    ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The time of the balance change.

    ↳ **type** `string`

**Possible values:**[`deposit`, ` withdrawal`, ` trade`, ` margin`, ` adjustment`, ` rollover`, ` credit`, ` transfer`, ` settled`, ` staking`, ` sale`, ` reserve`, ` conversion`, ` dividend`, ` reward`, ` creator_fee`] 

The broad type of the balance event.

    ↳ **subtype** `string`

**Possible values:**[`spotfromfutures`, ` spottofutures`, ` stakingfromspot`, ` spotfromstaking`, ` stakingtospot`, ` spottostaking`] 

The specific subtype of the balance event.

    ↳ **category** `string`

**Possible values:**[`deposit`, ` withdrawal`, ` trade`, ` margin-trade`, ` margin-settle`, ` margin-conversion`, ` conversion`, ` credit`, ` marginrollover`, ` staking-rewards`, ` instant`, ` equity-trade`, ` airdrop`, ` equity-dividend`, ` reward-bonus`, ` nft`, ` block-trade`] 

The categorization of the balance event.

    ↳ **wallet_type** `string`

**Possible values:**[`spot`, ` earn`] 

Wallet type.

    ↳ **wallet_id** `string`

**Possible values:**[`main`, `bonded`, `flexible`, `liquid`, `locked`] 

The following combinations of wallet types and wallet identifiers are available:

Wallet type `spot`:

  * `main`: Primary spot pairs trading wallet.

Wallet type `earn`:

  * `bonded`: earn on-chain product with lockup period.
  * `flexible`: earn product without lockup period.
  * `liquid`: kraken rewards program, see [support center](https://support.kraken.com/hc/en-us/articles/overview-of-rewards-on-kraken).
  * `locked`: earn product (may or may not have a lockup period).

    ↳ **user** `string` *conditional*

**Condition:** Published when request parameters have 'users=all'. 

**Example:** AA96N74GCGEFN8KI

The Kraken generated identifier for a user / sub-account.

]

    ↳ **sequence** `integer`

The subscription message sequence number.
    
    
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
    

An example of selling 0.005 BTC/USD, two events are streamed with a shared `ref_id`. The `ref_id` refers to the `trade_id` in this scenario:

  * BTC debit of -0.005.
  * USD credit of 132.9995.

    
    
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
    },  
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
    

## Unsubscribe Request

  * Unsubscribe Schema
  * Unsubscribe Ack Schema
  * Example: Unsubscribe
  * Example: Unsubscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `balances`

    ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `balances`

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "unsubscribe",  
        "params": {  
            "channel": "balances",  
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"  
        }  
    }  
    
    
    
    {  
        "method": "unsubscribe",  
        "result": {  
            "channel": "balances"  
        },  
        "success": true,  
        "time_in": "2023-10-16T13:29:13.111530Z",  
        "time_out": "2023-10-16T13:29:13.111775Z"  
    }