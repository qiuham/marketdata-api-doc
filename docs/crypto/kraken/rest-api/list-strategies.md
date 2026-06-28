---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/list-strategies
api_type: REST
updated_at: 2026-05-27 20:08:13.026244
---

# List Earn Strategies

**POST** `https://api.kraken.com/0/private/Earn/Strategies`

List earn strategies along with their parameters.

Requires a valid API key but not specific permission is required.

Returns only strategies that are available to the user based on geographic region.

When the user does not meet the tier restriction, `can_allocate` will be false and `allocation_restriction_info` indicates `Tier` as the restriction reason. Earn products generally require Intermediate tier. Get your account verified to access earn.

A note about `lock_type`:

  * `instant`: can be deallocated without an unbonding period. This is called flexible in the UI.
  * `bonded`: has an unbonding period. Deallocation will not happen until this period has passed.
  * `flex`: "Kraken rewards". This is earning on your spot balances where eligible. It's turned on account wide from the UI and you cannot manually allocate to these strategies.

Paging isn't yet implemented, so the endpoint always returns all data in the first page.

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**ascending** `booleannullable`

`true` to sort ascending, `false` (the default) for descending.

**asset** `stringnullable`

Filter strategies by asset name

**cursor** `stringnullable`

None to start at beginning/end, otherwise next page ID

**limit** `integer<uint16>nullable`

How many items to return per page. Note that the limit may be cap'd to lower value in the application code.

**lock_type** `string[]nullable`

Filter strategies by lock type

**Possible values:** [`flex`, `bonded`, `timed`, `instant`]

## Responses

  * 200

Response

  * application/json
* Schema

**Schema**

**error** `string[]`

**result** `objectnullable`

    ↳ **items** `object[]`

  * Array [

        ↳ **allocation_fee** `object`

Fee applied when allocating to this strategy

oneOf
* string
* integer
* number

****string

****integer

****number

            ↳ **allocation_restriction_info** `string[]`

Reason list why user is not eligible for allocating to the strategy

**Possible values:** [`tier`]

            ↳ **apr_estimate** `objectnullable`

The estimate is based on previous revenues from the strategy. Optional hint, not always present.

                ↳ **high** `string`

Maximal yield percentage for one year

                ↳ **low** `string`

Minimal yield percentage for one year

                ↳ **asset** `string`

The asset to invest for this earn strategy

                ↳ **auto_compound** `object`

Auto compound choices for the earn strategy

oneOf
* MOD1
* MOD2
* MOD3

                    ↳ **type** `string`

**Possible values:** [`disabled`]

                    ↳ **type** `string`

**Possible values:** [`enabled`]

                    ↳ **default** `boolean`

                    ↳ **type** `string`

**Possible values:** [`optional`]

                    ↳ **can_allocate** `boolean`

Is allocation available for this strategy

                    ↳ **can_deallocate** `boolean`

Is deallocation available for this strategy

                    ↳ **deallocation_fee** `object`

Fee applied when deallocating from this strategy

oneOf
* MOD1
* MOD2
* MOD3

****string

****integer

****number

                        ↳ **id** `string`

The unique identifier for this strategy

                        ↳ **lock_type** `object`

Type of the strategy

oneOf
* MOD1
* MOD2
* MOD3

                            ↳ **type** `string`

**Possible values:** [`flex`]

                            ↳ **bonding_period** `integer`

Duration of the bonding period, in seconds

                            ↳ **bonding_period_variable** `boolean`

Is the bonding period length variable (`true`) or static (`false`)

                            ↳ **bonding_rewards** `boolean`

Whether rewards are earned during the bonding period (payouts occur after bonding is complete)

                            ↳ **exit_queue_period** `integer`

In order to remove funds, if this value is greater than 0, funds will first have to enter an exit queue and will have to wait for the exit queue period to end. Once ended, her funds will then follow and respect the `unbonding_period`.

If the value of the exit queue period is 0, then no waiting will have to occur and the exit queue will be skipped

Rewards are always paid out for the exit queue

                            ↳ **payout_frequency** `integer`

At what intervals are rewards distributed and credited to the user's ledger, in seconds

                            ↳ **type** `string`

**Possible values:** [`bonded`]

                            ↳ **unbonding_period** `integer`

Duration of the unbonding period in seconds. In order to remove funds, you must wait for the unbonding period to pass after requesting removal before funds become available in her spot wallet

                            ↳ **unbonding_period_variable** `boolean`

Is the unbonding period length variable (`true`) or static (`false`)

                            ↳ **unbonding_rewards** `boolean`

Whether rewards are earned and payouts are done during the unbonding period

                            ↳ **payout_frequency** `integer`

At what intervals are rewards distributed and credited to the user's ledger, in seconds

                            ↳ **type** `string`

**Possible values:** [`instant`]

                            ↳ **user_cap** `stringnullable`

The maximum amount of funds that any given user may allocate to an account. Absence of value means there is no limit. Zero means that all new allocations will return an error (though auto-compound is unaffected).

                            ↳ **user_min_allocation** `stringnullable`

Minimum amount (in USD) for an allocation or deallocation. Absence means no minimum.

                            ↳ **yield_source** `object`

Yield generation mechanism of this strategy

oneOf
* MOD1
* MOD2

                                ↳ **type** `string`

**Possible values:** [`staking`]

                                ↳ **type** `string`

**Possible values:** [`off_chain`]

  * ]

                                ↳ **next_cursor** `stringnullable`

index to send into PageRequest for next page, None means you've reached the end.
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Earn/Strategies' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 30295839,  
      "asset": "DOT"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 30295839,
      "asset": "DOT"
    }