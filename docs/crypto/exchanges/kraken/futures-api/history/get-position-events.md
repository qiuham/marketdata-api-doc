---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/get-position-events
api_type: REST
updated_at: 2026-05-27 19:46:19.885068
---

# Get position update events

**GET** `https://futures.kraken.com/api/history/v3/positions`

Lists position events for authenticated account.

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

**opened** `boolean`

True if results should include opened position events. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**closed** `boolean`

True if results should include closed position events. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**increased** `boolean`

True if results should include increased position events. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**decreased** `boolean`

True if results should include decreased position events. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**reversed** `boolean`

True if results should include reversed position events. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**no_change** `boolean`

True if results should include "no change" position events - where the position has not changed. Setting this to false has no effect.

If multiple position change filters (opened/closed/increased/decreased/reversed/no_change) are provided, then positions matching any of these will be included.

When combined with update reason filters (trades/funding_realization/settlement), positions must match at least one position change filter AND at least one update reason filter.

If no filters are provided for the request, all position events will be included.

**trades** `boolean`

True if results should include position events caused by a trade. Setting this to false has no effect.

If multiple update reason filters (trades/funding_realization/settlement) are provided, then positions matching any of these will be included.

When combined with position change filters (opened/closed/increased/decreased/reversed/no_change), positions must match at least one update reason filter AND at least one position change filter.

If no filters are provided for the request, all position events will be included.

**funding_realization** `boolean`

True if results should include position events caused by a funding realisation. Setting this to false has no effect.

If multiple update reason filters (trades/funding_realization/settlement) are provided, then positions matching any of these will be included.

When combined with position change filters (opened/closed/increased/decreased/reversed/no_change), positions must match at least one update reason filter AND at least one position change filter.

If no filters are provided for the request, all position events will be included.

**settlement** `boolean`

True if results should include position events caused by a settlement. Setting this to false has no effect.

If multiple update reason filters (trades/funding_realization/settlement) are provided, then positions matching any of these will be included.

When combined with position change filters (opened/closed/increased/decreased/reversed/no_change), positions must match at least one update reason filter AND at least one position change filter.

If no filters are provided for the request, all position events will be included.

**tradeable** `string`

If present events of other tradeables are filtered out.

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

**accountUid** stringrequired

Account UID

    ↳ **tradeable** `string` *required*

**oldPosition** stringrequired

**oldAverageEntryPrice** string | nullnullable

**newPosition** stringrequired

**newAverageEntryPrice** stringrequired

**fillTime** integer,null<timestamp-milliseconds>nullable

    ↳ **fee** `string`

**feeCurrency** string

**realizedPnL** string

**positionChange** stringrequired

`unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`open`, `close`, `increase`, `decrease`, `reverse`, `noChange`, `unknown`]

**executionUid** string

**executionPrice** string

**executionSize** string

**tradeType** string

`unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`userExecution`, `liquidation`, `partialLiquidation`, `assignment`, `unwind`, `unknown`]

**fundingRealizationTime** integer<timestamp-milliseconds>

**realizedFunding** string

**settlementPrice** string

    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**updateReason** stringrequired

`unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`trade`, `fundingRealisation`, `settlement`, `unknown`]

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

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/positions' \  
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

opened — query

\---truefalse

closed — query

\---truefalse

increased — query

\---truefalse

decreased — query

\---truefalse

reversed — query

\---truefalse

no_change — query

\---truefalse

trades — query

\---truefalse

funding_realization — query

\---truefalse

settlement — query

\---truefalse

tradeable — query