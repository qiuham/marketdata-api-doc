---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-instruments
api_type: REST
updated_at: 2026-05-27 19:49:34.571992
---

# Get instruments

**GET** `https://futures.kraken.com/derivatives/api/v3/instruments`

Returns specifications for all currently listed markets and indices.

## Request

### Query Parameters

**contractType** string[]

**Possible values:** [`futures_inverse`, `futures_vanilla`, `flexible_futures`, `options`, `all`]

Contract type(s) to return statuses for.

By default, includes all futures instrument types.

Multi-value example: `?contractType=futures_inverse&contractType=futures_vanilla`

**expired** `boolean`

If `true`, return only expired instruments

Defaults to `false`, in which case only non-expired instruments are returned

**Default value:**`false`

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**instruments** `object[]` *required*

A list containing structures for each available instrument. The list is in no particular order.

  * Array [

    ↳ **category** `string`

'Category of the contract: "Layer 1", "Layer 2", "DeFi", or "Privacy" (multi-collateral contracts only).'

**contractSize** number

The contract size of the Futures.

**contractValueTradePrecision** number

Trade precision for the contract (e.g. trade precision of 2 means trades are precise to the hundredth decimal place 0.01).

**fundingRateCoefficient** number

**impactMidSize** number

Amount of contract used to calculated the mid price for the mark price.

    ↳ **isin** `string`

International Securities Identification Number (ISIN)

**lastTradingTime** string<date-time>

**marginSchedules** object

A map containing margin schedules by platform.

**property name*** MarginSchedule

    ↳ **retail** `object[]` *required*

  * Array [

        ↳ **contracts** `integer,null<int64>nullable`

For futures: The lower limit of the number of contracts to which this margin level applies

For indices: Not returned because N/A

**numNonContractUnits** number,null<double>nullable

For futures: The lower limit of the number of non-contract units (i.e. quote currency units for linear futures) to which this margin level applies

For indices: Not returned because N/A.

**initialMargin** numberrequired

For futures: The initial margin requirement for this level

For indices: Not returned because N/A

**maintenanceMargin** numberrequired

For futures: The maintenance margin requirement for this level

For indices: Not returned because N/A

  * ]

        ↳ **professional** `object[]` *required*

  * Array [

            ↳ **contracts** `integer,null<int64>nullable`

For futures: The lower limit of the number of contracts to which this margin level applies

For indices: Not returned because N/A

**numNonContractUnits** number,null<double>nullable

For futures: The lower limit of the number of non-contract units (i.e. quote currency units for linear futures) to which this margin level applies

For indices: Not returned because N/A.

**initialMargin** numberrequired

For futures: The initial margin requirement for this level

For indices: Not returned because N/A

**maintenanceMargin** numberrequired

For futures: The maintenance margin requirement for this level

For indices: Not returned because N/A

  * ]

**retailMarginLevels** object[]

Margin levels for retail clients.

  * Array [

            ↳ **contracts** `integer,null<int64>nullable`

For futures: The lower limit of the number of contracts to which this margin level applies

For indices: Not returned because N/A

**numNonContractUnits** number,null<double>nullable

For futures: The lower limit of the number of non-contract units (i.e. quote currency units for linear futures) to which this margin level applies

For indices: Not returned because N/A.

**initialMargin** numberrequired

For futures: The initial margin requirement for this level

For indices: Not returned because N/A

**maintenanceMargin** numberrequired

For futures: The maintenance margin requirement for this level

For indices: Not returned because N/A

  * ]

**marginLevels** object[]

Margin levels for professional clients.

  * Array [

            ↳ **contracts** `integer,null<int64>nullable`

For futures: The lower limit of the number of contracts to which this margin level applies

For indices: Not returned because N/A

**numNonContractUnits** number,null<double>nullable

For futures: The lower limit of the number of non-contract units (i.e. quote currency units for linear futures) to which this margin level applies

For indices: Not returned because N/A.

**initialMargin** numberrequired

For futures: The initial margin requirement for this level

For indices: Not returned because N/A

**maintenanceMargin** numberrequired

For futures: The maintenance margin requirement for this level

For indices: Not returned because N/A

  * ]

**maxPositionSize** number

Maximum number of contracts that one can hold in a position

**maxRelativeFundingRate** number

Perpetuals only: the absolute value of the maximum permissible funding rate

**openingDate** string<date-time>

When the contract was first available for trading

**postOnly** boolean

True if the instrument is in post-only mode, false otherwise.

**feeScheduleUid** stringdeprecated

**DEPRECATED** — Effective 2026-06-22, this field no longer corresponds to the fee schedule used for fee calculation on this instrument. Use the Spot [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume) endpoint authenticated with a Spot API key to determine your fee rate.

Unique identifier of fee schedule associated with the instrument

            ↳ **symbol** `string` *required*

Market symbol.

**Example:**`PF_BTCUSD`

            ↳ **pair** `string`

Asset pair.

**Example:**`BTC:USD`

            ↳ **base** `string`

Base asset.

**Example:**`BTC`

            ↳ **quote** `string`

Quote asset.

**Example:**`USD`

            ↳ **tags** `string[]`

Tag for the contract (currently does not return a value).

**tickSize** number

Tick size of the contract being traded.

            ↳ **tradeable** `boolean` *required*

True if this instrument is, or has ever been, a tradable instrument (i.e. a market).

Always `true` for instruments returned by this endpoint — historical/expired instruments retain `tradeable=true`

            ↳ **type** `string`

The type of the instrument

**Possible values:** [`flexible_futures`, `futures_inverse`, `futures_vanilla`, `options`]

            ↳ **underlying** `string`

The underlying of the Futures.

**underlyingFuture** string

For options: The underlying future of the option. Otherwise null.

            ↳ **tradfi** `boolean` *required*

True if this is a non-crypto market.

            ↳ **mtf** `boolean`

True if currently has MTF status.

**isExpired** booleanrequired

True if the instrument has expired.

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

    
    
    {  
      "instruments": [  
        {  
          "symbol": "PI_XBTUSD",  
          "pair": "XBT:USD",  
          "base": "XBT",  
          "quote": "USD",  
          "type": "futures_inverse",  
          "underlying": "rr_xbtusd",  
          "tickSize": 0.5,  
          "contractSize": 1,  
          "tradeable": true,  
          "impactMidSize": 1,  
          "maxPositionSize": 1000000,  
          "openingDate": "2022-01-01T00:00:00.000Z",  
          "marginLevels": [  
            {  
              "contracts": 0,  
              "initialMargin": 0.02,  
              "maintenanceMargin": 0.01  
            },  
            {  
              "contracts": 500000,  
              "initialMargin": 0.04,  
              "maintenanceMargin": 0.02  
            },  
            {  
              "contracts": 1000000,  
              "initialMargin": 0.06,  
              "maintenanceMargin": 0.03  
            },  
            {  
              "contracts": 3000000,  
              "initialMargin": 0.1,  
              "maintenanceMargin": 0.05  
            }  
          ],  
          "fundingRateCoefficient": 8,  
          "maxRelativeFundingRate": 0.001,  
          "isin": "GB00J62YGL67",  
          "contractValueTradePrecision": 0,  
          "postOnly": false,  
          "feeScheduleUid": "eef90775-995b-4596-9257-0917f6134766",  
          "retailMarginLevels": [  
            {  
              "contracts": 0,  
              "initialMargin": 0.5,  
              "maintenanceMargin": 0.25  
            }  
          ],  
          "category": "",  
          "tags": [],  
          "tradfi": false,  
          "mtf": true,  
          "isExpired": false  
        },  
        {  
          "symbol": "FI_XBTUSD_220930",  
          "pair": "XBT:USD",  
          "base": "XBT",  
          "quote": "USD",  
          "type": "futures_inverse",  
          "underlying": "rr_xbtusd",  
          "lastTradingTime": "2022-09-30T15:00:00.000Z",  
          "tickSize": 0.5,  
          "contractSize": 1,  
          "tradeable": true,  
          "impactMidSize": 1,  
          "maxPositionSize": 1000000,  
          "openingDate": "2022-01-01T00:00:00.000Z",  
          "marginLevels": [  
            {  
              "contracts": 0,  
              "initialMargin": 0.02,  
              "maintenanceMargin": 0.01  
            },  
            {  
              "contracts": 500000,  
              "initialMargin": 0.04,  
              "maintenanceMargin": 0.02  
            },  
            {  
              "contracts": 1000000,  
              "initialMargin": 0.06,  
              "maintenanceMargin": 0.03  
            },  
            {  
              "contracts": 3000000,  
              "initialMargin": 0.1,  
              "maintenanceMargin": 0.05  
            }  
          ],  
          "isin": "GB00JVMLP260",  
          "contractValueTradePrecision": 0,  
          "postOnly": false,  
          "feeScheduleUid": "eef90775-995b-4596-9257-0917f6134766",  
          "retailMarginLevels": [  
            {  
              "contracts": 0,  
              "initialMargin": 0.5,  
              "maintenanceMargin": 0.25  
            }  
          ],  
          "category": "",  
          "tags": [],  
          "tradfi": false,  
          "mtf": false,  
          "isExpired": false  
        },  
        {  
          "symbol": "PF_XBTUSD",  
          "pair": "XBT:USD",  
          "base": "XBT",  
          "quote": "USD",  
          "type": "flexible_futures",  
          "tickSize": 1,  
          "contractSize": 1,  
          "tradeable": true,  
          "impactMidSize": 1,  
          "maxPositionSize": 1000000,  
          "openingDate": "2022-01-01T00:00:00.000Z",  
          "marginLevels": [  
            {  
              "numNonContractUnits": 0,  
              "initialMargin": 0.02,  
              "maintenanceMargin": 0.01  
            },  
            {  
              "numNonContractUnits": 500000,  
              "initialMargin": 0.04,  
              "maintenanceMargin": 0.02  
            },  
            {  
              "numNonContractUnits": 2000000,  
              "initialMargin": 0.1,  
              "maintenanceMargin": 0.05  
            },  
            {  
              "numNonContractUnits": 5000000,  
              "initialMargin": 0.2,  
              "maintenanceMargin": 0.1  
            },  
            {  
              "numNonContractUnits": 10000000,  
              "initialMargin": 0.3,  
              "maintenanceMargin": 0.15  
            },  
            {  
              "numNonContractUnits": 30000000,  
              "initialMargin": 0.5,  
              "maintenanceMargin": 0.25  
            }  
          ],  
          "fundingRateCoefficient": 8,  
          "maxRelativeFundingRate": 0.001,  
          "contractValueTradePrecision": 4,  
          "feeScheduleUid": "5b755fea-c5b0-4307-a66e-b392cd5bd931",  
          "postOnly": false,  
          "retailMarginLevels": [  
            {  
              "numNonContractUnits": 0,  
              "initialMargin": 0.02,  
              "maintenanceMargin": 0.01  
            },  
            {  
              "numNonContractUnits": 500000,  
              "initialMargin": 0.04,  
              "maintenanceMargin": 0.02  
            },  
            {  
              "numNonContractUnits": 2000000,  
              "initialMargin": 0.1,  
              "maintenanceMargin": 0.05  
            },  
            {  
              "numNonContractUnits": 5000000,  
              "initialMargin": 0.2,  
              "maintenanceMargin": 0.1  
            },  
            {  
              "numNonContractUnits": 10000000,  
              "initialMargin": 0.3,  
              "maintenanceMargin": 0.15  
            },  
            {  
              "numNonContractUnits": 30000000,  
              "initialMargin": 0.5,  
              "maintenanceMargin": 0.25  
            }  
          ],  
          "category": "Layer 1",  
          "tags": [],  
          "tradfi": false,  
          "mtf": false,  
          "isExpired": false  
        }  
      ],  
      "result": "success",  
      "serverTime": "2022-06-28T09:29:04.243Z"  
    }  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/instruments' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Parameters

contractType — query

futures_inversefutures_vanillaflexible_futuresoptionsall

expired — query

\---truefalse

ResponseClear

Click the `Send API Request` button above and see the response here!