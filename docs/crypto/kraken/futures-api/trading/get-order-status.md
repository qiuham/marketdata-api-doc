---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-order-status
api_type: REST
updated_at: 2026-05-27 19:50:32.156321
---

# Get Specific Orders' Status

**POST** `https://futures.kraken.com/derivatives/api/v3/orders/status`

Returns information on specified orders which are open or were filled/cancelled in the last 5 seconds.

## Request

### Query Parameters

**orderIds** uuid[]

UIDs associated with orders or triggers.

**cliOrdIds** string[]

Client Order IDs associated with orders or triggers.

**Example:**[testOrder1, testOrder2]

## Responses

  * 200
* application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**orders** `object[]` *required*

  * Array [

    ↳ **order** `object` *required*

        ↳ **type** `string` *required*

**Possible values:** [`TRIGGER_ORDER`, `ORDER`]

**orderId** string<uuid>required

**cliOrdId** string | nullnullablerequired

        ↳ **symbol** `string` *required*

        ↳ **side** `string` *required*

        ↳ **quantity** `number | nullnullable` *required*

        ↳ **filled** `number | nullnullable` *required*

**limitPrice** number | nullnullablerequired

**reduceOnly** booleanrequired

        ↳ **timestamp** `string` *required*

**lastUpdateTimestamp** stringrequired

**priceTriggerOptions** objectrequired

oneOf
* TriggerOptions
* MOD2

**triggerPrice** numberrequired

**triggerSide** stringrequired

**Possible values:** [`TRIGGER_ABOVE`, `TRIGGER_BELOW`]

**triggerSignal** stringrequired

**Possible values:** [`MARK_PRICE`, `LAST_PRICE`, `SPOT_PRICE`]

**triggerTime** string | nullnullablerequired

        ↳ **status** `OrderStatusJson (string)` *required*

**Possible values:** [`ENTERED_BOOK`, `FULLY_EXECUTED`, `REJECTED`, `CANCELLED`, `TRIGGER_PLACED`, `TRIGGER_ACTIVATION_FAILURE`]

**updateReason** objectrequired

oneOf
* OrderUpdateReason
* MOD2

****string

**Possible values:** [`LOADING_MARKET`, `NEW_USER_ORDER`, `LIQUIDATION_ORDER`, `STOP_ORDER_TRIGGERED`, `LIMIT_FROM_STOP`, `PARTIAL_FILL`, `FULL_FILL`, `CANCELLED_BY_USER`, `CONTRACT_EXPIRED`, `NOT_ENOUGH_MARGIN`, `MARKET_INACTIVE`, `DEAD_MAN_SWITCH`, `CANCELLED_BY_ADMIN`, `POST_WOULD_EXECUTE_REASON`, `IOC_WOULD_NOT_EXECUTE_REASON`, `WOULD_EXECUTE_SELF_REASON`, `WOULD_NOT_REDUCE_POSITION`, `EDITED_BY_USER`, `ORDER_FOR_EDIT_NOT_FOUND_REASON`, `EXPIRED`, `TRAILING_STOP_PRICE_UPDATED`, `TRAILING_STOP_CANCELLED_AND_REPLACED_BY_ADMIN`]

**error** `object` *required*

oneOf
* OrderError
* MOD2

****string

**Possible values:** [`MARKET_SUSPENDED`, `MARKET_NOT_FOUND`, `INVALID_PRICE`, `INVALID_QUANTITY`, `SMALL_ORDER_LIMIT_EXCEEDED`, `INSUFFICIENT_MARGIN`, `WOULD_CAUSE_LIQUIDATION`, `CLIENT_ORDER_ID_IN_USE`, `CLIENT_ORDER_ID_TOO_LONG`, `MAX_POSITION_EXCEEDED`, `PRICE_COLLAR`, `PRICE_DISLOCATION`, `EDIT_HAS_NO_EFFECT`, `ORDER_FOR_CANCELLATION_NOT_FOUND`, `ORDER_FOR_EDIT_NOT_FOUND`, `ORDER_CANNOT_HAVE_TRIGGER_PRICE`, `POST_WOULD_EXECUTE`, `IOC_WOULD_NOT_EXECUTE`, `WOULD_EXECUTE_SELF`, `WOULD_NOT_REDUCE_POSITION`, `REJECTED_AFTER_EXECUTION`, `MARKET_IS_POST_ONLY`, `ORDER_LIMIT_EXCEEDED`, `FIXED_LEVERAGE_TOO_HIGH`, `CANNOT_EDIT_TRIGGER_PRICE_OF_TRAILING_STOP`, `CANNOT_EDIT_LIMIT_PRICE_OF_TRAILING_STOP`, `TRAILING_STOP_ORDER_LIMIT_EXCEEDED`, `TRAILING_STOP_PERCENT_DEVIATION_EXCEEDS_MAX_DECIMAL_PLACES`, `TRAILING_STOP_QUOTE_DEVIATION_NOT_MULTIPLE_OF_TICK_SIZE`, `TRAILING_STOP_MAX_DEVIATION_TOO_LARGE`, `TRAILING_STOP_MAX_DEVIATION_TOO_SMALL`, `INSUFFICIENT_HEADROOM_AROUND_CURRENT_PRICE_TO_EDIT_TRAILING_STOP`, `NO_REFERENCE_PRICE_AVAILABLE_FOR_CALCULATING_TRAILING_STOP_TRIGGER_PRICE`, `INSUFFICIENT_CLOSING_MARGIN`, `LIMIT_PRICE_SET_AS_ABSOLUTE_AND_RELATIVE`, `LIMIT_PRICE_OFFSET_VALUE_INVALID`, `LIMIT_PRICE_OFFSET_UNIT_INVALID`, `LIMIT_PRICE_OFFSET_MUST_HAVE_VALUE_AND_UNIT`, `LIMIT_PRICE_OFFSET_QUOTE_CURRENCY_VALUE_MUST_BE_MULTIPLE_OF_TICK_SIZE`, `LIMIT_PRICE_OFFSET_PERCENT_VALUE_TOO_MANY_DECIMAL_PLACES`, `LIMIT_PRICE_OFFSET_TOO_HIGH`, `LIMIT_PRICE_OFFSET_TOO_LOW`]

  * ]

**result** `string` *required*

**Possible values:** [`success`]

**Example:**`success`

**serverTime** string<date-time>required

Server time in Coordinated Universal Time (UTC)

**Example:**`2020-08-27T17:03:33.196Z`

**errors** `Error (string)[]`

**Possible values:** [`accountInactive`, `apiLimitExceeded`, `authenticationError`, `insufficientFunds`, `invalidAccount`, `invalidAmount`, `invalidArgument`, `invalidUnit`, `Json Parse Error`, `marketUnavailable`, `nonceBelowThreshold`, `nonceDuplicate`, `notFound`, `requiredArgumentMissing`, `Server Error`, `Unavailable`, `unknownError`]

**error** `Error (string)` *required*

Error description.
* `accountInactive`: The Futures account the request refers to is inactive
* `apiLimitExceeded`: The API limit for the calling IP address has been exceeded
* `authenticationError`: The request could not be authenticated
* `insufficientFunds`: The amount requested for transfer is below the amount of funds available
* `invalidAccount`: The Futures account the transfer request refers to is invalid
* `invalidAmount`: The amount the transfer request refers to is invalid
* `invalidArgument`: One or more arguments provided are invalid
* `invalidUnit`: The unit the transfer request refers to is invalid
* `Json Parse Error`: The request failed to pass valid JSON as an argument
* `marketUnavailable`: The market is currently unavailable
* `nonceBelowThreshold`: The provided nonce is below the threshold
* `nonceDuplicate`: The provided nonce is a duplicate as it has been used in a previous request
* `notFound`: The requested information could not be found
* `requiredArgumentMissing`: One or more required arguments are missing
* `Server Error`: There was an error processing the request
* `Unavailable`: The endpoint being called is unavailable
* `unknownError`: An unknown error has occurred

**Possible values:** [`accountInactive`, `apiLimitExceeded`, `authenticationError`, `insufficientFunds`, `invalidAccount`, `invalidAmount`, `invalidArgument`, `invalidUnit`, `Json Parse Error`, `marketUnavailable`, `nonceBelowThreshold`, `nonceDuplicate`, `notFound`, `requiredArgumentMissing`, `Server Error`, `Unavailable`, `unknownError`]

**result** `string` *required*

**Possible values:** [`error`]

**Example:**`error`

**serverTime** string<date-time>required

Server time in Coordinated Universal Time (UTC)

**Example:**`2020-08-27T17:03:33.196Z`

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/orders/status' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key

authent

Parameters

orderIds — query

cliOrdIds — query