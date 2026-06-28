---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-asset-info
api_type: REST
updated_at: 2026-05-27 20:02:07.948015
---

# Get Asset Info

**GET** `https://api.kraken.com/0/public/Assets`

Get information about the assets that are available for deposit, withdrawal, trading and earn.

## Request

### Query Parameters

**asset** `string`

Comma delimited list of assets to get info on (optional, default all available assets)

**Example:** XBT,ETH

**aclass** `string`

**Possible values:** [`currency`, `tokenized_asset`]

Filters the asset class to retrieve (optional)
* `currency` = spot currency pairs.
* `tokenized_asset` = xstocks.

**Default value:**`currency`

## Responses

  * 200

Asset info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

**property name*** AssetInfo

Asset Info

    ↳ **aclass** `string`

Asset Class

    ↳ **altname** `string`

Alternate name

    ↳ **decimals** `integer`

Number of decimal places for record keeping amounts of this asset

    ↳ **display_decimals** `integer`

Number of decimal places shown for display purposes in frontends

    ↳ **collateral_value** `number`

Valuation as margin collateral (if applicable)

    ↳ **status** `string`

Status of asset. Possible values: `enabled`, `deposit_only`, `withdrawal_only`, `funding_temporarily_disabled`.

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Assets' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

asset — query

aclass — query

\---currencytokenized_asset

ResponseClear

Click the `Send API Request` button above and see the response here!