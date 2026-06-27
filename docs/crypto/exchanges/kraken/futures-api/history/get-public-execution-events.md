---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/get-public-execution-events
api_type: REST
updated_at: 2026-05-27 19:46:27.127057
---

# Get public execution events

**GET** `https://futures.kraken.com/api/history/v3/market/:tradeable/executions`

Lists trades for a market.

## Request

### Path Parameters

**tradeable** `string` *required*

### Query Parameters

**since** `timestamp-milliseconds`

Timestamp in milliseconds.

**before** `timestamp-milliseconds`

Timestamp in milliseconds.

**sort** `string`

**Possible values:** [`asc`, `desc`]

Determines the order of events in response(s).
* `asc` = chronological
* `desc` = reverse-chronological

**Default value:**`desc`

**continuation_token** `base64`

Opaque token from the `Next-Continuation-Token` header used to continue listing events. The `sort` parameter must be the same as in the previous request to continue listing in the same direction.

**count** `int64`

**Possible values:** `>= 1`

The maximum number of results to return. The upper bound is determined by a global limit.

## Responses

  * 200
* application/json
* Schema

**Schema**

**len** `integer<uint64>` *required*

**elements** `object[]` *required*

  * Array [

    ↳ **uid** `string` *required*

    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

    ↳ **event** `object` *required*

**Execution** objectrequired

        ↳ **execution** `object` *required*

            ↳ **uid** `string<uuid>` *required*

**makerOrder** objectrequired

            ↳ **uid** `string<uuid>` *required*

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**takerOrder** objectrequired

            ↳ **uid** `string<uuid>` *required*

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **price** `string<decimal>` *required*

**Example:**`1234.56789`

**markPrice** string<decimal>required

**Example:**`1234.56789`

**limitFilled** booleanrequired

**oldTakerOrder** object

            ↳ **uid** `string<uuid>` *required*

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**usdValue** string<decimal>required

**Example:**`1234.56789`

**takerReducedQuantity** stringrequired

sometimes empty string

  * ]

**continuationToken** string<base64>

Opaque token to pass to the next request to continue listing events. The `sort` parameter must be the same as in the previous request to continue listing in the same direction.
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/market/:tradeable/executions' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/history/v3

Parameters

tradeable — pathrequired

since — query

before — query

sort — query

\---ascdesc

continuation_token — query

count — query