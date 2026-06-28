---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-accounts
api_type: REST
updated_at: 2026-05-27 19:48:44.375876
---

# Get wallets

**GET** `https://futures.kraken.com/derivatives/api/v3/accounts`

This endpoint returns key information relating to all your accounts which may either be cash accounts or margin accounts. This includes digital asset balances, instrument balances, margin requirements, margin trigger estimates and auxiliary information such as available funds, PnL of open positions and portfolio value.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**accounts** `object` *required*

A structure containing structures with account-related information for all margin and cash accounts.

    ↳ **cash** `object` *required*

        ↳ **type** `string` *required*

The type of the account (always "cashAccount").

**Possible values:** [`cashAccount`]

        ↳ **balances** `object` *required*

A structure containing account balances.

**property name*** string<decimal>

**Example:**`12.0353200`

            ↳ **flex** `object` *required*

Structure showing multi-collateral wallet details.

                ↳ **type** `string`

The type of the account (always multiCollateralMarginAccount)

**Possible values:** [`multiCollateralMarginAccount`]

                ↳ **currencies** `object` *required*

Structure with collateral currency details.

**property name*** FlexCurrencySummary

                    ↳ **quantity** `number` *required*

Quantity of asset.

                    ↳ **value** `number` *required*

USD value of asset.

                    ↳ **collateral** `number` *required*

USD value of the asset usable for margin (Asset Value * Haircut).

                    ↳ **available** `number` *required*

Margin (in base currency) available for trading.

**initialMargin** numberrequired

Total initial margin held for open positions (USD).

**initialMarginWithOrders** numberrequired

Total initial margin held for open positions and open orders (USD).

**maintenanceMargin** numberrequired

Total maintenance margin held for open positions (USD).

**balanceValue** numberrequired

USD value of all collateral in multi-collateral wallet.

**portfolioValue** numberrequired

Balance value plus unrealised PnL in USD.

**collateralValue** numberrequired

USD value of balances in account usable for margin (Balance Value * Haircut).

                    ↳ **pnl** `number` *required*

Unrealised PnL in USD.

**unrealizedFunding** numberrequired

Unrealised funding from funding rate (USD).

**totalUnrealized** numberrequired

Total USD value of unrealised funding and unrealised PnL.

**totalUnrealizedAsMargin** numberrequired

Unrealised pnl and unrealised funding that is usable as margin `[(Unrealised Profit/Loss
* Unrealised Funding Rate) * Haircut - Conversion Fee]`.

**availableMargin** numberrequired

Margin Equity - Total Initial Margin.

**marginEquity** numberrequired

`[Balance Value in USD * (1-Haircut)] + (Total Unrealised Profit/Loss as Margin in USD)`

**portfolioMarginBreakdown** object

Breakdown of portfolio margin components.

**totalCrossAssetNettedMarketRisk** number<double>required

**totalMarketRisk** number<double>required

**totalScenarioPnls** number<double>[]

**totalAbsoluteOptionPositionDeltaNotional** number<double>required

**netPortfolioDelta** number<double>required

**totalPremium** number<double>required

**isBuyOnly** booleanrequired

**futuresMaintenanceMargin** number<double>required

**upnlInterestRate** number | nullnullable

Interest rate applied to unrealized profit/loss.

**property name*** MarginAccount

                    ↳ **type** `string` *required*

The type of the account (always "marginAccount").

**Possible values:** [`marginAccount`]

                    ↳ **currency** `string` *required*

The currency of the account. All figures shown in `auxiliary` and `marginRequirements` are in this currency.

                    ↳ **balances** `object` *required*

A structure containing account balances.

**property name*** string<decimal>

**Example:**`12.0353200`

                        ↳ **auxiliary** `object` *required*

A structure containing auxiliary account information.

                            ↳ **usd** `number` *required*

                            ↳ **pv** `number` *required*

The portfolio value of the account, in currency.

                            ↳ **pnl** `number` *required*

The PnL of current open positions of the account, in currency.

                            ↳ **af** `number` *required*

The available funds of the account, in currency.

                            ↳ **funding** `number` *required*

**marginRequirements** objectrequired

A structure containing the account's margin requirements.

                            ↳ **im** `number` *required*

The initial margin requirement of the account.

                            ↳ **mm** `number` *required*

The maintenance margin requirement of the account.

                            ↳ **lt** `number` *required*

The liquidation threshold of the account.

                            ↳ **tt** `number` *required*

The termination threshold of the account

**triggerEstimates** objectrequired

A structure containing the account's margin trigger estimates.

                            ↳ **im** `number` *required*

The initial margin requirement of the account.

                            ↳ **mm** `number` *required*

The maintenance margin requirement of the account.

                            ↳ **lt** `number` *required*

The liquidation threshold of the account.

                            ↳ **tt** `number` *required*

The termination threshold of the account

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
      "accounts": {  
        "cash": {  
          "balances": {  
            "xbt": "141.31756797",  
            "xrp": "52465.1254"  
          },  
          "type": "cashAccount"  
        },  
        "fi_xbtusd": {  
          "auxiliary": {  
            "af": 100.73891563,  
            "funding": 100.73891563,  
            "pnl": 12.42134766,  
            "pv": 153.73891563,  
            "usd": 0  
          },  
          "balances": {  
            "FI_XBTUSD_171215": "50000",  
            "FI_XBTUSD_180615": "-15000",  
            "xbt": "141.31756797",  
            "xrp": "0"  
          },  
          "currency": "xbt",  
          "marginRequirements": {  
            "im": 52.8,  
            "lt": 39.6,  
            "mm": 23.76,  
            "tt": 15.84  
          },  
          "triggerEstimates": {  
            "im": 3110,  
            "lt": 2890,  
            "mm": 3000,  
            "tt": 2830  
          },  
          "type": "marginAccount"  
        },  
        "flex": {  
          "type": "multiCollateralMarginAccount",  
          "currencies": {  
            "XBT": {  
              "quantity": 0.1185308247,  
              "value": 4998.721054420551,  
              "collateral": 4886.49976674881,  
              "available": 0.1185308247  
            },  
            "USD": {  
              "quantity": 5000,  
              "value": 5000,  
              "collateral": 5000,  
              "available": 5000  
            },  
            "EUR": {  
              "quantity": 4540.5837374453,  
              "value": 4999.137289089901,  
              "collateral": 4886.906656949836,  
              "available": 4540.5837374453  
            }  
          },  
          "balanceValue": 34995.52,  
          "portfolioValue": 34995.52,  
          "collateralValue": 34122.66,  
          "initialMargin": 0,  
          "initialMarginWithOrders": 0,  
          "maintenanceMargin": 0,  
          "pnl": 0,  
          "unrealizedFunding": 0,  
          "totalUnrealized": 0,  
          "totalUnrealizedAsMargin": 0,  
          "marginEquity": 34122.66,  
          "availableMargin": 34122.66  
        }  
      },  
      "result": "success",  
      "serverTime": "2016-02-25T09:45:53.818Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/accounts' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent