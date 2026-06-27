---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/list-allocations
api_type: REST
updated_at: 2026-05-27 20:08:05.773386
---

# List Earn Allocations

**POST** `https://api.kraken.com/0/private/Earn/Allocations`

List all allocations for the user.

Requires the `Query Funds` API key permission.

By default all allocations are returned, even for strategies that have been used in the past and have zero balance now. That is so that the user can see how much was earned with given strategy in the past. `hide_zero_allocations` parameter can be used to remove zero balance entries from the output. Paging hasn't been implemented for this method as we don't expect the result for a particular user to be overwhelmingly large.

All amounts in the output can be denominated in a currency of user's choice (the `converted_asset` parameter).

Information about when the next reward will be paid to the client is also provided in the output.

Allocated funds can be in up to 4 states:

  * bonding
  * allocated
  * exit_queue (ETH only)
  * unbonding

Any funds in `total` not in `bonding`/`unbonding` are simply allocated and earning rewards. Depending on the strategy funds in the other 3 states can also be earning rewards. Consult the output of `/Earn/Strategies` to know whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still earns rewards.

Note that for `ETH`, when the funds are in the `exit_queue` state, the `expires` time given is the time when the funds will have finished unbonding, not when they go from exit queue to unbonding.

(Un)bonding time estimate can be inaccurate right after having (de)allocated the funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**ascending** `booleannullable`

`true` to sort ascending, `false` (the default) for descending.

**converted_asset** `stringnullable`

A secondary currency to express the value of your allocations (the default is USD).

**hide_zero_allocations** `booleannullable`

Omit entries for strategies that were used in the past but now they don't hold any allocation (the default is `false`)

## Responses

  * 200

Response

  * application/json
* Schema

**Schema**

**error** `string[]`

**result** `objectnullable`

Page response

    ↳ **converted_asset** `string`

A secondary asset to show the value of allocations. (Eg. you also want to see the value of your allocations in USD). Choose this in the request parameters.

    ↳ **items** `object[]`

  * Array [

        ↳ **amount_allocated** `object`

Amounts allocated to this Earn strategy

            ↳ **bonding** `objectnullable`

Amount allocated in bonding status. Only present when there are bonding allocations.

                ↳ **allocation_count** `integer<uint>`

The total number of allocations in this state for this asset

                ↳ **allocations** `object[]`

Details about when each allocation will expire and move to the next state

  * Array [

                    ↳ **converted** `string`

Amount converted into the requested asset

                    ↳ **created_at** `string<date-time>`

The date and time which a request to either allocate was received and the funds started bonding.

                    ↳ **expires** `string<date-time>`

The date at which the `Bonded` allocation will move to the `Earning` state.

                    ↳ **native** `string`

Amount in the native asset

  * ]

                    ↳ **converted** `string`

Amount converted into the requested asset

                    ↳ **native** `string`

Amount in the native asset

                    ↳ **exit_queue** `objectnullable`

Amount allocated in the exit-queue status. Only present when there are exit_queue allocations.

                        ↳ **allocation_count** `integer<uint>`

The total number of allocations in this state for this asset

                        ↳ **allocations** `object[]`

Details about when each allocation will expire and move to the next state

  * Array [

                            ↳ **converted** `string`

Amount converted into the requested asset

                            ↳ **created_at** `string<date-time>`

The date and time which a request to deallocate was received and processed. For a deallocation request to a strategy with an `exit-queue`, this will be the time the funds joined the exit queue.

                            ↳ **expires** `string<date-time>`

The date/time when the funds will be unbonded.

                            ↳ **native** `string`

Amount in the native asset

  * ]

                            ↳ **converted** `string`

Amount converted into the requested asset

                            ↳ **native** `string`

Amount in the native asset

                            ↳ **pending** `objectnullable`

Pending allocation amount - can be negative if the pending operation is deallocation. Only present when there are pending allocations.

                                ↳ **converted** `string`

Amount converted into the requested asset

                                ↳ **native** `string`

Amount in the native asset

                                ↳ **total** `object`

Total amount allocated to this Earn strategy

                                    ↳ **converted** `string`

Amount converted into the requested asset

                                    ↳ **native** `string`

Amount in the native asset

                                    ↳ **unbonding** `objectnullable`

Amount allocated in unbonding status. Only present when there are unbonding allocations.

                                        ↳ **allocation_count** `integer<uint>`

The total number of allocations in this state for this asset

                                        ↳ **allocations** `object[]`

Details about when each allocation will expire and move to the next state

  * Array [

                                            ↳ **converted** `string`

Amount converted into the requested asset

                                            ↳ **created_at** `string<date-time>`

The date and time which a request to either allocate or deallocate was received and processed.

For a deallocation request to a strategy with an `exit-queue`, this will be the time the funds joined the exit queue. For a deallocation request to a strategy without exit queue, this will be the time the funds started unbonding

                                            ↳ **expires** `string<date-time>`

The date/time the funds will be unbonded.

                                            ↳ **native** `string`

Amount in the native asset

  * ]

                                            ↳ **converted** `string`

Amount converted into the requested asset

                                            ↳ **native** `string`

Amount in the native asset

                                            ↳ **native_asset** `string`

The asset of the native currency of this allocation

                                            ↳ **payout** `objectnullable`

Information about the current payout period, absent if when there is no current payout period.

                                                ↳ **accumulated_reward** `object`

Reward accumulated in the payout period until now

                                                    ↳ **converted** `string`

Amount converted into the requested asset

                                                    ↳ **native** `string`

Amount in the native asset

                                                    ↳ **estimated_reward** `object`

Estimated reward from now until the payout

                                                        ↳ **converted** `string`

Amount converted into the requested asset

                                                        ↳ **native** `string`

Amount in the native asset

                                                        ↳ **period_end** `string<date-time>`

Tentative date of the next reward payout.

                                                        ↳ **period_start** `string<date-time>`

When the current payout period started. Either the date of the last payout or when it was enabled.

                                                        ↳ **strategy_id** `string`

Unique ID for Earn Strategy

                                                        ↳ **total_rewarded** `object`

Amount earned using the strategy during the whole lifetime of user account

                                                            ↳ **converted** `string`

Amount converted into the requested asset

                                                            ↳ **native** `string`

Amount in the native asset

  * ]

                                                            ↳ **total_allocated** `string`

The total amount allocated across all strategies, denominated in the `converted_asset` currency

                                                            ↳ **total_rewarded** `string`

Amount earned across all strategies during the whole lifetime of user account, denominated in `converted_asset` currency
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Earn/Allocations' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 30295839,  
      "converted_asset": "EUR",  
      "hide_zero_allocations": true  
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
      "converted_asset": "EUR",
      "hide_zero_allocations": true
    }