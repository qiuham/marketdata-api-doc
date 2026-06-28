---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-ticker-information
api_type: REST
updated_at: 2026-05-27 20:05:11.490823
---

# Get Ticker Information

**GET** `https://api.kraken.com/0/public/Ticker`

Get ticker information for all or requested markets. To clarify usage, note that

  * Today's prices start at midnight UTC
  * Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken

## Request

### Query Parameters

**pair** `string`

Asset pair to get data for (optional, default: all tradeable exchange pairs)

**Example:** XBTUSD

**asset_class** `string`

**Possible values:** [`tokenized_asset`, `forex`]

This parameter is required on requests for tokenized pairs, i.e. xstocks. If `asset_class` is provided without the `pair` parameter, all pairs for that asset class will be returned.

**Default value:**`forex`

## Responses

  * 200

Ticker info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

**property name*** AssetTickerInfo

Asset Ticker Info

    ↳ **a** `string[]`

Ask `[<price>, <whole lot volume>, <lot volume>]`

    ↳ **b** `string[]`

Bid `[<price>, <whole lot volume>, <lot volume>]`

    ↳ **c** `string[]`

Last trade closed `[<price>, <lot volume>]`

    ↳ **v** `string[]`

Volume `[<today>, <last 24 hours>]`

    ↳ **p** `string[]`

Volume weighted average price `[<today>, <last 24 hours>]`

    ↳ **t** `integer[]`

Number of trades `[<today>, <last 24 hours>]`

    ↳ **l** `string[]`

Low `[<today>, <last 24 hours>]`

    ↳ **h** `string[]`

High `[<today>, <last 24 hours>]`

    ↳ **o** `string`

Today's opening price

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Ticker' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — query

asset_class — query

\---tokenized_assetforex

ResponseClear

Click the `Send API Request` button above and see the response here!