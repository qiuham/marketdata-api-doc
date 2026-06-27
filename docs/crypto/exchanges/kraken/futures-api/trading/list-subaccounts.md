---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/list-subaccounts
api_type: REST
updated_at: 2026-05-27 19:52:34.571272
---

# Get subaccounts

**GET** `https://futures.kraken.com/derivatives/api/v3/subaccounts`

Return information about subaccounts, including balances and UIDs.

## Responses

  * 200
* application/json
* Schema
  * kfSuccess

**Schema**

oneOf
* Success Response
* ErrorResponse

**masterAccountUid** stringrequired

Master account UID

**subaccounts** `object[]` *required*

The sub-accounts.

  * Array [

**accountUid** stringrequired

The account UID

    ↳ **email** `string` *required*

The email associated with the account

**fullName** string | nullnullablerequired

The name of the account

**holdingAccounts** object[]required

Structure containing structures with holding accounts information for a specific holding account asset.

  * Array [

    ↳ **currency** `string` *required*

The currency of the account. All figures shown in this currency.

    ↳ **amount** `number` *required*

The amount of currency in the holding account.

  * ]

**futuresAccounts** object[]required

Structure containing structures with single-collateral accounts information for a specific futures account asset.

  * Array [

    ↳ **name** `string` *required*

The name of the futures account as the account pair.

**availableMargin** numberrequired

The amount of currency in the holding account in the quote currency of the name pair.

  * ]

**flexAccount** objectrequired

Multi-collateral account structure.

    ↳ **currencies** `object[]` *required*

  * Array [

        ↳ **currency** `string` *required*

The name of the currency.

        ↳ **quantity** `number` *required*

The amount of currency in the multi-collateral account.

        ↳ **value** `number` *required*

The value of the currency quantity.

        ↳ **collateral** `number` *required*

The collateral value of the currency quantity (value * haircut).

        ↳ **available** `number` *required*

The available currency (quantity - margin requirement)

  * ]

**initialMargin** numberrequired

The total initial margin for the multi-collateral account in USD.

**initialMarginWithOrders** numberrequired

The total initial margin of open positions without the margin held by open orders for the multi-collateral account in USD.

**maintenanceMargin** numberrequired

The total maintenance margin for the multi-collateral account in USD.

**balanceValue** numberrequired

The total balance value for the multi-collateral account in USD.

**portfolioValue** numberrequired

The total value of the portfolio in USD (Balance Value + Total Unrealised Profit/Loss).

**collateralValue** numberrequired

The USD value of balances in account usable for margin [(Balance Value * (1-Haircut)].

        ↳ **pnl** `number` *required*

The unrealised pnl for the multi-collateral account.

**unrealizedFunding** numberrequired

The total unrealised funding for the multi-collateral account in USD.

**totalUnrealized** numberrequired

Total unrealised Profit/Loss and unrealised funding of open positions in USD `(Unrealised Position(s) Profit/Loss + Unrealised Funding Rate Profit/Loss) * USD rate`.

**totalUnrealizedAsMargin** numberrequired

Unrealised Profit/Loss and unrealised funding that is usable as margin `(Unrealised Profit/Loss + Unrealised Funding Rate) * Haircut - Conversion Fee`.

**availableMargin** numberrequired

Account-wide margin available to create new orders (Margin Equity - Total Initial Margin).

**marginEquity** numberrequired

The Balance Value multiplied by the dollar rate and with haircuts applied to non-USD currencies, plus unrealised profit or loss as Margin.

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
      "result": "success",  
      "serverTime": "2022-03-31T20:38:53.677Z",  
      "masterAccountUid": "ba598ca1-65c1-4f48-927d-0e2b647d627a",  
      "subaccounts": [  
        {  
          "holdingAccounts": [  
            {  
              "currency": "gbp",  
              "amount": 0  
            },  
            {  
              "currency": "bch",  
              "amount": 0.00004  
            },  
            {  
              "currency": "xrp",  
              "amount": 13662.85078  
            },  
            {  
              "currency": "usd",  
              "amount": 0  
            },  
            {  
              "currency": "eth",  
              "amount": 3.0000485057  
            },  
            {  
              "currency": "usdt",  
              "amount": 0  
            },  
            {  
              "currency": "ltc",  
              "amount": 0.00002  
            },  
            {  
              "currency": "usdc",  
              "amount": 0  
            },  
            {  
              "currency": "xbt",  
              "amount": 3.46e-9  
            }  
          ],  
          "futuresAccounts": [  
            {  
              "name": "f-xrp:usd",  
              "availableMargin": 16187.33210488726  
            },  
            {  
              "name": "f-eth:usd",  
              "availableMargin": 67.59768318324302  
            },  
            {  
              "name": "f-xbt:usd",  
              "availableMargin": -0.0009056832839642471  
            },  
            {  
              "name": "f-ltc:usd",  
              "availableMargin": 67.51126059691163  
            },  
            {  
              "name": "f-xrp:xbt",  
              "availableMargin": 2.34e-9  
            },  
            {  
              "name": "f-bch:usd",  
              "availableMargin": 47.151615710695495  
            }  
          ],  
          "flexAccount": {  
            "currencies": [  
              {  
                "currency": "eth",  
                "quantity": 0.5,  
                "value": 1646.575,  
                "collateral": 1543.91104875,  
                "available": 0.49999966035931903  
              },  
              {  
                "currency": "usdt",  
                "quantity": 0,  
                "value": 0,  
                "collateral": 0,  
                "available": 0  
              },  
              {  
                "currency": "gbp",  
                "quantity": 0,  
                "value": 0,  
                "collateral": 0,  
                "available": 0  
              },  
              {  
                "currency": "xbt",  
                "quantity": 0,  
                "value": 0,  
                "collateral": 0,  
                "available": 0  
              },  
              {  
                "currency": "usdc",  
                "quantity": 0,  
                "value": 0,  
                "collateral": 0,  
                "available": 0  
              },  
              {  
                "currency": "usd",  
                "quantity": 0,  
                "value": 0,  
                "collateral": 0,  
                "available": 0  
              }  
            ],  
            "initialMargin": 0,  
            "initialMarginWithOrders": 0,  
            "maintenanceMargin": 0,  
            "balanceValue": 1646.58,  
            "portfolioValue": 1646.58,  
            "collateralValue": 1543.91,  
            "pnl": 0,  
            "unrealizedFunding": 0,  
            "totalUnrealized": 0,  
            "totalUnrealizedAsMargin": 0,  
            "availableMargin": 1543.91,  
            "marginEquity": 1543.91  
          },  
          "fullName": "fullname redacted",  
          "email": "email redacted",  
          "accountUid": "7f5c528e-2285-45f0-95f5-83d53d4bfcd2"  
        }  
      ]  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/subaccounts' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent