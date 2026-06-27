---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-tradable-asset-pairs
api_type: REST
updated_at: 2026-05-27 20:05:21.846022
---

# Get Tradable Asset Pairs

**GET** `https://api.kraken.com/0/public/AssetPairs`

Get tradable asset pairs

## Request

### Query Parameters

**pair** `string`

Asset pairs to get data for

**Example:** BTC/USD,ETH/BTC

**aclass_base** `string`

**Possible values:** [`currency`, `tokenized_asset`]

Filters the asset class to retrieve (optional)
* `currency` = spot currency pairs.
* `tokenized_asset` = tokenized asset pairs, i.e. xstocks.

**Default value:**`currency`

**info** `string`

**Possible values:** [`info`, `leverage`, `fees`, `margin`]

Info to retrieve (optional)
* `info` = all info
* `leverage` = leverage info
* `fees` = fees schedule
* `margin` = margin info

**Default value:**`info`

**country_code** `ISO 3166-1 alpha-2`

Filter for response to only include pairs available in the provided country/region.

**Example:** GB

**execution_venue** `string`

**Possible values:** [`international`, `bitnomial_exchange`]

Comma-separated list of execution venues to filter by (optional)
* `international` = International exchange
* `bitnomial_exchange` = Bitnomial exchange

**Default value:**`international`

**Examples:**
* International only
* Bitnomial only
* International and Bitnomial

Fetch pairs listed on International execution venue only

**Example:**`international`

Fetch pairs listed on Bitnomial Exchange execution venue only

**Example:**`bitnomial_exchange`

Fetch pairs listed on both International and Bitnomial Exchange execution venues

**Example:**`international,bitnomial_exchange`

## Responses

  * 200

Tradable asset pairs retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Pair names and their info

**property name*** AssetPair

Trading Asset Pair

    ↳ **altname** `string`

Alternate pair name

    ↳ **wsname** `string`

WebSocket pair name (if available)

    ↳ **aclass_base** `string`

Asset class of base component

    ↳ **base** `string`

Asset ID of base component

    ↳ **aclass_quote** `string`

Asset class of quote component

    ↳ **quote** `string`

Asset ID of quote component

    ↳ **execution_venue** `string`

Execution venue where the order book for this pair is listed

**Possible values:** [`international`, `bitnomial_exchange`]

    ↳ **lot** `stringdeprecated`

Volume lot size

    ↳ **pair_decimals** `integer`

Number of decimal places for prices in this pair

    ↳ **cost_decimals** `integer`

Number of decimal places for cost of trades in pair (quote asset terms)

    ↳ **lot_decimals** `integer`

Number of decimal places for volume (base asset terms)

    ↳ **lot_multiplier** `integer`

Amount to multiply lot volume by to get currency volume

    ↳ **leverage_buy** `integer[]`

Array of leverage amounts available when buying

    ↳ **leverage_sell** `integer[]`

Array of leverage amounts available when selling

    ↳ **fees** `array[]`

Fee schedule array in `[<volume>, <percent fee>]` tuples

        ↳ **fees_maker** `array[]`

Maker fee schedule array in `[<volume>, <percent fee>]` tuples (if on maker/taker)

            ↳ **fee_volume_currency** `string`

Volume discount currency

            ↳ **margin_call** `integer`

Margin call level

            ↳ **margin_stop** `integer`

Stop-out/liquidation margin level

            ↳ **ordermin** `string`

Minimum order size (in terms of base currency)

            ↳ **costmin** `string`

Minimum order cost (in terms of quote currency)

            ↳ **tick_size** `string`

Minimum increment between valid price levels

            ↳ **status** `string`

Status of asset. Possible values: `online`, `cancel_only`, `post_only`, `limit_only`, `reduce_only`.

            ↳ **long_position_limit** `integer`

Maximum long margin position size (in terms of base currency)

            ↳ **short_position_limit** `integer`

Maximum short margin position size (in terms of base currency)

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/AssetPairs' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — query

aclass_base — query

\---currencytokenized_asset

info — query

\---infoleveragefeesmargin

country_code — query

execution_venue — query

\---internationalbitnomial_exchange

ResponseClear

Click the `Send API Request` button above and see the response here!