---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/get-order-events
api_type: REST
updated_at: 2026-05-27 19:46:12.717362
---

# Get order events

**GET** `https://futures.kraken.com/api/history/v3/orders`

Lists order events for authenticated account.

## Request

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

**tradeable** `string`

If present events of other tradeables are filtered out.

**opened** `boolean`

Determines status of the orders that should be included in response(s).
* `true` = return orders that have been placed within given time range.
* `false` = don't return orders that have been placed within given time range.

**closed** `boolean`

Determines status of the order that should be included in response(s).
* `true` = return orders that have been closed/cancelled/rejected within given time range.
* `false` = don't return orders that have been closed/cancelled/rejected within given time range.

## Responses

  * 200
* application/json
* Schema

**Schema**

**accountUid** string<uuid>required

**len** `integer<uint64>` *required*

**serverTime** string<date-time>

**elements** `object[]` *required*

  * Array [

    ↳ **uid** `string` *required*

    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

    ↳ **event** `object` *required*

oneOf
* MOD1
* MOD2
* MOD3
* MOD4
* MOD5
* MOD6

**OrderPlaced** objectrequired

        ↳ **order** `object` *required*

            ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

            ↳ **reason** `string` *required*

**reducedQuantity** stringrequired

always empty string

**OrderUpdated** objectrequired

**oldOrder** objectrequired

            ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

**newOrder** objectrequired

            ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

            ↳ **tradeable** `string` *required*

            ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

            ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

            ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

            ↳ **reason** `string` *required*

**reducedQuantity** string<decimal>required

**Example:**`1234.56789`

**OrderRejected** objectrequired

            ↳ **order** `object` *required*

                ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                ↳ **tradeable** `string` *required*

                ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

**orderError** stringrequired

                ↳ **reason** `string` *required*

**OrderCancelled** objectrequired

                ↳ **order** `object` *required*

                    ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                    ↳ **tradeable** `string` *required*

                    ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                    ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

                    ↳ **reason** `string` *required*

**OrderNotFound** objectrequired

**accountUid** string<uuid>required

**orderId** stringrequired

**Example:**`Uuid(uuid=2ceb1d31-f619-457b-870c-fd4ddbb10d45)`

**OrderEditRejected** objectrequired

**oldOrder** objectrequired

                    ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                    ↳ **tradeable** `string` *required*

                    ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                    ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

**attemptedOrder** objectrequired

                    ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                    ↳ **tradeable** `string` *required*

                    ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                    ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

**orderError** stringrequired

  * ]

**continuationToken** string<base64>

Opaque token to pass to the next request to continue listing events. The `sort` parameter must be the same as in the previous request to continue listing in the same direction.

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/orders' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/history/v3

Auth

general-api-key-read-only

authent

Parameters

since — query

before — query

sort — query

\---ascdesc

continuation_token — query

count — query

tradeable — query

opened — query

\---truefalse

closed — query

\---truefalse