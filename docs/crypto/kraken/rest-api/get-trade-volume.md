---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-trade-volume
api_type: REST
updated_at: 2026-05-27 20:05:44.333017
---

# Get Trade Volume

**POST** `https://api.kraken.com/0/private/TradeVolume`

Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided. Fees will not be included if `pair` is not specified as Kraken fees differ by asset pair. Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

**API Key Permissions Required:** `Funds permissions - Query`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**pair** `string`

Comma delimited list of asset pairs to get fee info on (optional, but required if any fee info is desired)

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Trade Volume retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Trade Volume

    ↳ **currency** `string`

Fee volume currency (will always be USD)

    ↳ **volume** `string`

Current fee discount volume (in USD, breakdown by subaccount if applicable and logged in to master account)

    ↳ **fees** `object`

Taker fees that will be applied for each `pair` included in the request. Default `None` if `pair` is not requested.

**property name*** FeeTierInfo

Fee Tier Info

        ↳ **fee** `string`

Current fee (in percent)

        ↳ **min_fee** `string`

minimum fee for pair (if not fixed fee)

        ↳ **max_fee** `string`

maximum fee for pair (if not fixed fee)

        ↳ **next_fee** `stringnullable`

next tier's fee for pair (if not fixed fee, null if at lowest fee tier)

        ↳ **tier_volume** `stringnullable`

volume level of current tier (if not fixed fee. null if at lowest fee tier)

        ↳ **next_volume** `stringnullable`

volume level of next tier (if not fixed fee. null if at lowest fee tier)

        ↳ **fees_maker** `object`

Maker fees that will be applied for this each `pair` included in the request. Default `None` if `pair` is not requested.

**property name*** FeeTierInfo

Fee Tier Info

            ↳ **fee** `string`

Current fee (in percent)

            ↳ **min_fee** `string`

minimum fee for pair (if not fixed fee)

            ↳ **max_fee** `string`

maximum fee for pair (if not fixed fee)

            ↳ **next_fee** `stringnullable`

next tier's fee for pair (if not fixed fee, null if at lowest fee tier)

            ↳ **tier_volume** `stringnullable`

volume level of current tier (if not fixed fee. null if at lowest fee tier)

            ↳ **next_volume** `stringnullable`

volume level of next tier (if not fixed fee. null if at lowest fee tier)

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/TradeVolume' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "pair": "XXBT/ZUSD, XETH/ZEUR"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828490,
      "pair": "XXBT/ZUSD, XETH/ZEUR"
    }