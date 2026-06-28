---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/get-trigger-events
api_type: REST
updated_at: 2026-05-27 19:46:48.892252
---

# Get trigger events

**GET** `https://futures.kraken.com/api/history/v3/triggers`

Lists trigger events for authenticated account.

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

Determines status of the triggers that should be included in response(s).
* `true` = return triggers that have been placed within given time range.
* `false` = don't return triggers that have been placed within given time range.

**closed** `boolean`

Determines status of the trigger that should be included in response(s).
* `true` = return triggers that have been closed/cancelled/rejected within given time range.
* `false` = don't return triggers that have been closed/cancelled/rejected within given time range.

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

**OrderTriggerPlaced** objectrequired

        ↳ **order** `object` *required*

            ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

            ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

            ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

            ↳ **reason** `string` *required*

**OrderTriggerCancelled** objectrequired

            ↳ **order** `object` *required*

                ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

                ↳ **reason** `string` *required*

**OrderTriggerUpdated** objectrequired

**oldOrderTrigger** objectrequired

                ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**newOrderTrigger** objectrequired

                ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

                ↳ **reason** `string` *required*

**OrderTriggerActivated** objectrequired

                ↳ **order** `object` *required*

                    ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**OrderTriggerEditRejected** objectrequired

**attemptedOrderTrigger** objectrequired

                    ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**oldOrderTrigger** objectrequired

                    ↳ **uid** `string<uuid>` *required*

**accountId** number<uint64>required

**accountUid** string<uuid>required

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

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**triggerOptions** objectrequired

**triggerPrice** string<decimal>required

**Example:**`1234.56789`

**triggerSignal** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`MarkPrice`, `LastPrice`, `SpotPrice`, `Unknown`]

**triggerSide** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Above`, `Below`, `Unknown`]

**trailingStopOptions** objectrequired

**maxDeviation** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

**limitPriceOffset** objectrequired

**priceOffset** string<decimal>required

**Example:**`1234.56789`

                    ↳ **unit** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Percent`, `QuoteCurrency`, `Unknown`]

                    ↳ **reason** `string` *required*

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

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/triggers' \  
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