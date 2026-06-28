---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-pre-trade
api_type: REST
updated_at: 2026-05-27 20:04:20.102487
---

# Pre-Trade Data

**GET** `https://api.kraken.com/0/public/PreTrade`

Returns the price levels in the order book with aggregated order quantities at each price level. The top 10 levels are returned for each trading pair.

## Request

### Query Parameters

**symbol** `string` *required*

**Possible values:** `>= 3 characters` and `<= 32 characters`

A list of symbols for the currency pairs.

**Example:** BTC/USD

## Responses

  * 200

The top price levels of the aggregated order book.

  * application/json
* Schema

**Schema**

**result** `object`

An aggregated order book.

    ↳ **symbol** `string`

The symbol of the currency pair.

**Possible values:** `<= 32 characters`

**Example:**`BTC/USD`

    ↳ **description** `string`

The full description of the currency pair.

**Possible values:** `<= 350 characters`

**Example:**`Bitcoin / US Dollars`

    ↳ **base_asset** `string<ISO 4217>`

Currency code for the base asset.

**Example:**`BTC`

    ↳ **base_notation** `string`

Indicates that the quantity is expressed in nominal value.

**Possible values:** [`NOML`]

    ↳ **quote_asset** `string<ISO 4217>`

Currency in which the trading price is expressed.

**Example:**`USD`

    ↳ **quote_notation** `string`

Indicates that the price is expressed in monetary value.

**Possible values:** [`MONE`]

    ↳ **venue** `string<ISO 10383>`

Market Identifier Code (MIC) of the trading platform where the order was submitted.

**Possible values:** [`PGSL`]

    ↳ **system** `string`

Indicates the order system is a Central Limit Order Book.

**Possible values:** [`CLOB`]

    ↳ **bids** `object[]`

  * Array [

        ↳ **side** `string`

Indicates whether the price level is a bid (BUY) or offer (SELL).

**Possible values:** [`BUY`]

        ↳ **price** `string`

Price level in the Central Limit Order Book (CLOB).

**Example:**`102002.1`

        ↳ **qty** `string`

The aggregated quantity at the price level.

**Example:**`102002.1`

        ↳ **count** `int`

The number of orders in the price level.

**Possible values:** `non-empty`

        ↳ **publication_ts** `string<ISO 8601>`

Timestamp the price level was 
**Example:**`2024-05-30T12:34:56.123456Z`

  * ]

        ↳ **asks** `object[]`

  * Array [

            ↳ **side** `string`

Indicates whether the price level is a bid (BUY) or offer (SELL).

**Possible values:** [`SELL`]

            ↳ **price** `string`

Price level in the Central Limit Order Book (CLOB).

**Example:**`102002.1`

            ↳ **qty** `string`

The aggregated quantity at the price level.

**Example:**`102002.1`

            ↳ **count** `int`

The number of orders in the price level.

**Possible values:** `non-empty`

            ↳ **publication_ts** `string<ISO 8601>`

Timestamp the price level was 
**Example:**`2024-05-30T12:34:56.123456Z`

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/PreTrade' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

symbol — queryrequired

ResponseClear

Click the `Send API Request` button above and see the response here!