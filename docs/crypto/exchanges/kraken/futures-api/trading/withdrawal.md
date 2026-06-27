---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/withdrawal
api_type: REST
updated_at: 2026-05-27 19:54:44.560880
---

# Initiate withdrawal to Spot wallet

**POST** `https://futures.kraken.com/derivatives/api/v3/withdrawal`

This endpoint allows you to request to withdraw digital assets to your Kraken Spot wallet.

Wallet names can be found in the 'accounts' structure in the Get Wallets /accounts response.

## Request

### Query Parameters

**currency** `string` *required*

The digital asset that shall be withdrawn back to spot wallet.

**amount** `decimal` *required*

**Possible values:** `> 0`

The amount of currency that shall be withdrawn back to spot wallet.

**sourceWallet** string

The wallet from which the funds shall be withdrawn back to spot wallet. Default is "cash" wallet.

## Responses

  * 200
* application/json
* Schema
  * success
  * failure

**Schema**

oneOf
* WithdrawalResponse
* ErrorResponse

**uid** `string` *required*

Withdrawal/transfer reference

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
      "uid": "9053db5f-0d5e-48dd-b606-a5c92576b706",  
      "result": "success",  
      "serverTime": "2022-06-28T14:48:58.711Z"  
    }  
    
    
    
    {  
      "result": "error",  
      "serverTime": "2019-05-15T09:24:16.968Z",  
      "error": "Unavailable"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** **Withdrawal** API key with **full** access
    **in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/withdrawal' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

withdrawal-api-key

authent

Parameters

currency — queryrequired

amount — queryrequired

sourceWallet — query