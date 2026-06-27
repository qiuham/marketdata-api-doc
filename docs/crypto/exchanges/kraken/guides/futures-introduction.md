---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/futures-introduction
api_type: Guide
updated_at: 2026-05-27 19:57:32.450809
---

# Futures Introduction

## Futures Platform

The Kraken Futures platform provides a number of Application Programming Interfaces (APIs) through HTTP (also known as REST),Websockets (WS) and FIX. For the FIX API please refer to the [FIX](/api/docs/guides/fix-intro) for the authentication specific mechanism and endpoint description.

The REST API provides secure access to your Futures account to perform actions such as:

  * request current or historical price information
  * check your account balance and PnL
  * your margin parameters and estimated liquidation thresholds
  * place or cancel orders (individually or in batch)
  * see your open orders
  * open positions or trade history
  * request a digital asset withdrawal

These "endpoints" are explained in the REST API section.

The WebSocket API provides real-time data channels to the Futures platform which eliminates the need to periodically send requests for frequently changing information. The [WebSocket API](/api/docs/guides/futures-websockets) section explains how to create "subscriptions" to these data channels.

Some of the endpoints allow performing sensitive tasks, such as initiating a digital asset withdrawal. To access these endpoints securely, the API uses encryption techniques developed by the National Security Agency. This section describes how to encrypt your communication with the API when accessing these endpoints.

The API can be implemented using any programming language you like (e.g. C, C++, Java or PHP), as long as it is capable of managing HTTP requests. We strongly suggest you look at the code examples listed in sample implementations.

## Conventions and Definitions

### Server Time

The server time is in Coordinated Universal Time (UTC).

### Unique Identifiers

> Unique Identifier Example
    
    
    c18f0c17-9971-40e6-8e5b-10df05d422f0  
    

The system constructs unique identifiers according to the Universally Unique Identifier standard.

### Dates and Times

> Dates and Times Examples
    
    
    2016-02-26T12:09:38.830Z  
    
    
    
    2016-02-26T12:09:38Z  
    

The API requires dates and time arguments in the ISO8601 datetime format and returns all dates and times in the same format. The syntax of this format is `<yyyy>-<mm>-<dd>T<HH>:<MM>:<SS>.<sss>Z` where `<yyyy>` is the year, `<mm>` is the month, `<dd>` is the day, `<HH>` is the hour, `<MM>` is the minute, `<SS>` is the second and `<sss>` is the millisecond. When provided as an argument, `<sss>` is optional. `Z` denotes that the datetime is in UTC.

### Symbols

The system identifies cash accounts, margin accounts, futures contracts and indices through ticker symbols. Please refer to the platform documentation for details on the ticker symbol syntax. The following shows some sample ticker symbols.

Example Symbols| Description  
---|---  
`xbt`| Bitcoin  
`xrp`| Ripple XRP  
`fi_xbtusd`| Bitcoin-Dollar Futures Margin Account  
`fi_xrpusd`| Ripple-Dollar Futures Margin Account  
`fi_xbtusd_180615`| Bitcoin-Dollar Futures, maturing at 16:00 London time on 15 June 2018  
`fi_xrpusd_180615`| Ripple-Dollar Futures, maturing at 16:00 London time on 15 June 2018  
`fi_xrpxbt_180615`| Ripple-Bitcoin Futures, maturing at 16:00 London time on 15 June 2018  
`in_xbtusd`| Bitcoin-Dollar Real-Time Index  
`rr_xbtusd`| Bitcoin-Dollar Reference Rate  
`in_xrpusd`| Ripple-Dollar Real-Time Index  
  
### Order of Arguments

> Example
> 
> When calling the tickers endpoint, the structure for `rr_xbtusd` will not contain the keys `suspended`, `lastSize`, `vol24h`, `bid`, `bidSize`, `ask`, `askSize` and `markPrice`. This is because `rr_xbtusd` is an index such that these keys do not apply.
    
    
    {  
      "symbol": "rr_xbtusd",  
      "last": 4225,  
      "lastTime": "2016-02-25T11:05:21.000Z",  
      "open24h": 4179,  
      "high24h": 4264,  
      "low24h": 4177  
    }  
    

When calling endpoints with required arguments, all arguments must be provided in the order they are listed (see section HTTP API resources).

## Generate API keys

> Your `api_key` (Public key) example:
    
    
    rRra59qKQs3y1egAgSaG0RJlBcbq97wTUXSxXxPdhRZdv7z9ijZRWgrf  
    

> Your `api_secret` (Private key) example:
    
    
    rttp4AzwRfYEdQ7R7X8Z/04Y4TZPa97pqCypi3xXxAqftygftnI6H9yGV+OcUOOJeFtZkr8mVwbAndU3Kz4Q+eG  
    

In order to use the API, you need to generate a pair of unique API keys:

  1. Sign in to your futures account.

  2. Click on your **name** on the upper-right corner.

  3. Select **"Settings"** from the drop-down menu.

  4. Select the **"Create Key"** tab in the API panel.

  5. There are two options when generating API keys with differing levels of access:

**General API:**

**No Access:** This key does not allow any access to any endpoints. (This option could be selected if you only wanted a key with access to withdraw digital assets.)

**Read Only:** This is a read-only key and allows accessing only endpoints that do not write to the server.

**Full Access:** This is a master key and allows accessing all endpoints, excluding digital asset withdrawals.

**Withdrawal API:**

**No Access:** This key is does not allow access to digital asset withdrawals.

**Full Access:** This key allows access to digital asset withdrawals.

  6. Press the **"Create Key"** button.

  7. View your Public and Private keys and **record them somewhere safe**.

danger

The private key is shown only once! You cannot go back and view it again later.

danger

API keys should be kept in a safe location and should never be shared with anyone. If you are not absolutely certain that you can store your API private key in a safe place, **do not generate it.**

### Limits

Up to 50 keys can be created with distinct nonces.

## API Testing Environment

To allow clients to test their API implementation, we have API functionality in our futures demo environment publicly available that is completely separate from the production environment and does not require existing account credentials.

In order to get started, just navigate to: <https://demo-futures.kraken.com/>

Click the Sign Up button and an e-mail and password combination will be generated for you by the platform.

Review the Demo Environment Terms & Conditions and Kraken Privacy Policy before accepting.

Note the credentials so that you may re-use them if desired.

Once these steps are completed, select 'Complete Sign-Up' to create your Demo account

Once you have signed up, you can generate API keys for the purpose of testing.

The WebSocket and REST API code on this environment is identical to the live production code in terms of the feeds/endpoints and the response structure.

You may also use the [Github repository][github-cryptofacilities] which has libraries coded for multiple common programming languages.

The only difference between the demo API behaviour and that of the live production environment is that the base URL is not [futures.kraken.com](https://futures.kraken.com/) but instead [demo-futures.kraken.com](https://demo-futures.kraken.com/).

### Examples

> Example: subscribe to WebSocket ticker feeds by sending:
    
    
    {  
      "event": "subscribe",  
      "feed": "ticker",  
      "product_ids": [  
        "PI_XBTUSD",  
        "FI_ETHUSD_210625"  
      ]  
    }  
    

On the demo, for the WebSocket API you would subscribe to: `wss://demo-futures.kraken.com/ws/v1`

All the feeds are identical to those documented above.

For a similar exercise via the REST API you would request: `https://demo-futures.kraken.com/derivatives/api/v3/tickers`

Please note that when you have successfully tested in the demo environment, the base URL in the live production platform environment works with [futures.kraken.com](http://futures.kraken.com/).

## API URLs

To access the **REST API** 's endpoints, HTTP calls need to be sent to endpoints under:

  * `https://futures.kraken.com/derivatives/api/v3/`
  * `https://futures.kraken.com/api/history/v2/`
  * `https://futures.kraken.com/api/charts/v1/`

To subscribe to a **WebSocket** feed, establish a WebSocket connection to:

`wss://futures.kraken.com/ws/v1`

Note: The direct access URLs for IP whitelisting are different, see [IP whitelisting][ip-whitelisting] below.

## Sample implementations

Sample implementations of the API in Java, Python, C# and Visual Basic .NET can be found on our GitHub page:

<https://github.com/cryptofacilities>

If you have implemented the API in a language that is not listed here and would like to share your code, contact our support team by opening a ticket.

  * Futures Platform
  * Conventions and Definitions
* Server Time
* Unique Identifiers
* Dates and Times
* Symbols
* Order of Arguments
  * Generate API keys
* Limits
  * API Testing Environment
* Examples
  * API URLs
  * Sample implementations