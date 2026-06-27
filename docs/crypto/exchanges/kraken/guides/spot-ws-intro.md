---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-ws-intro
api_type: WebSocket
updated_at: 2026-05-27 19:59:41.869856
---

# Spot Websockets Introduction

Websockets is a bi-directional protocol helping you build fast, real-time, event-driven applications. This sections contains a summary of the connection details and versions.

## Connection Details

The websocket URLs to connect to our trading environments are:

Environment| API| Public Data| Private Data (authentication required)  
---|---|---|---  
Primary| v2| wss://ws.kraken.com/v2| wss://ws-auth.kraken.com/v2  
Primary| v1| wss://ws.kraken.com| wss://ws-auth.kraken.com  
Beta| v2| wss://beta-ws.kraken.com/v2| wss://beta-ws-auth.kraken.com/v2  
Beta| v1| wss://beta-ws.kraken.com| wss://beta-ws-auth.kraken.com  
* **Primary** : Production API and production trading engine.
  * **Beta** : Beta API and production trading engine. Beta receives API software updates prior to the primary platform. A beta connection may required to access new or enhanced features, this will be indicated by the API guides or the support team

## Websockets Versions

We have 2 versions of websockets for spot: v1 and v2. Websockets v2 cleans up a number idiosyncrasies and ambiguities from v1 with the overall aim to enable easier integration with applications. It is intended that v1 will be maintained but future enhancements will be developed in v2.

Each version is described separately in the API pages:

  * Websockets v2: [API Reference](/api/docs/websocket-v2/add_order)
  * Websockets v1: [API Reference](/api/docs/websocket-v1/addorder)

## Websockets v2

The latest version of websockets has been completely re-designed to enable simpler and faster integration with applications:

### Cleaner Document Structure

  * It has a FIX-like design, FIX is standard communication protocol across the financial industry, enabling a more familiar experience across all of our APIs.
  * Pair symbols have been aligned into the more readable "BTC/USD" format.
  * The timestamps use the RFC3339 format `2021-05-11T19:47:09.896860Z` which are readable, parsable and easy to sort.
  * Prices and quantities are published as a number type for ease of processing. The values contain the same precision as the engine and full precision can be maintained when decoded as a decimal or a string instead of the default json parser setting (usually float). This offers ease of processing and precision where required.
  * Payloads are normalised JSON objects with no/minimal positional or variable length fields, to allow for maximum future flexibility without breaking client code.
  * The message structure is consistent (i.e. predictable dictionary keys) and is more readable for both human and machine clients.

**Example:** Add a `trailing-stop` order which triggers when the market reverts 1% from trough price
    
    
    {  
        "method": "add_order",  
        "params": {  
            "order_type": "trailing-stop",  
            "side": "buy",  
            "order_qty": 100,  
            "symbol": "MATIC/USD",  
            "triggers": {  
                "reference": "last",  
                "price": 1.0,  
                "price_type": "pct"  
            },  
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"  
        }  
    }  
    

### Order Transactions and Requests

#### Requests

  * All requests accept an optional, client-specified integer request identifier (`req_id`) for matching up the response, when returned. The uniqueness of the `req_id` is not enforced by the exchange.
  * Warnings are generated on `add_order` transactions when deprecated fields are detected.

#### Responses

All responses to requests have a standardised response:

  * `time_in` and `time_out` describe when our server received the request and sent the response, to help further isolate and measure network/client/server latency.
  * `success` indicates if the request was handled successfully.
  * `result` includes details specific to the type of request.
  * `error` if present, gives details of what error occurred.

Additionally, the responses now contain advisory messages, highlighting deprecated fields or upcoming changes to the request / channel.

### Channels

Additional event driven streams have been added:

  * `level3`: streams the orders that constitute the central limit order book. This offers an additional level of granularity over level2 `book` channel. This feed enables queue priority and a range of order book analytics to be calculated.
  * `balance`: streams the client asset balances and transactions from your account ledger.

## FAQs

The Frequently Asked Questions (FAQs) section tries to answer the most common questions that users can encounter.

### Connection times out

The server closes any open websocket connection within approximately one minute of inactivity.

Any, for example a [ping](/api/docs/websocket-v2/ping), request can be used to keep the connection alive.

### EOrder:Reduce only:Non-PC

The "**EOrder :Reduce only:Non-PC**" error response indicated to a problem with the Permitted Client (PC).

For more information please see the Kraken support article [Margin trading and Permitted Client self-certification for Ontario, Canada clients](https://support.kraken.com/hc/en-us/articles/6474011237268#whataretherequirementsforontariocanadaresidentstocontinuemargintrading).

### XBT/USD pair is missing

If you are getting the error "**Currency pair not supported XBT/USD** " that is because we are using `BTC` instead of `XBT` for bitcoin in v2.

Please use the [instrument](/api/docs/websocket-v2/instrument) channel to fetch the list of pairs which can be subscribed to via WebSockets API.

## General Considerations (v1 and v2 connections)

  * Transport Layer Security (TLS) with Server Name Indication (SNI) is required in order to establish a Kraken WebSockets API connection. See [Cloudflare's "What is SNI?" guide](https://www.cloudflare.com/learning/ssl/what-is-sni/) for more details.
  * All messages sent and received via websockets are encoded in JavaScript Object Notation (JSON) format.
  * Timestamps should not be considered unique and not be considered as aliases for transaction identifiers (IDs). Also, the granularity of timestamps is not representative of transaction rates.
  * At least one private message should be subscribed to keep the authenticated client connection open.
  * Cloudflare imposes a connection/re-connection rate limit---per Internet Protocol (IP) address---of approximately 150 attempts per rolling 10 minutes. If the reconnection rate limit is exceeded, the IP address is banned for 10 minutes.

### Instrument supported

  * For websocket v1, Please use REST API endpoint [AssetPairs](/api/docs/rest-api/get-tradable-asset-pairs) to fetch the list of pairs which can be subscribed via WebSockets API. For example, field 'wsname' gives the supported pairs name which can be used to subscribe.
  * For websocket v2, Please use websocket endpoint [instrument](/api/docs/websocket-v2/instrument) on Websocket v2 channel to fetch the list of pairs which can be subscribed via WebSockets API. The `pairs` array contains the supported pair names (see field`symbol`).

### Recommended Reconnection Behaviour

  * Normal operation: Attempt reconnection instantly up to a handful of times if the websocket is dropped randomly.
  * After maintenance or extended downtime: Attempt to reconnect no more quickly than once every five (5) seconds. There is no advantage to reconnecting more rapidly after maintenance during `cancel_only` mode.
* Connection Details
  * Websockets Versions
  * Websockets v2
* Cleaner Document Structure
* Order Transactions and Requests
* Channels
  * FAQs
* Connection times out
* EOrder only
* XBT/USD pair is missing
  * General Considerations (v1 and v2 connections)
* Instrument supported
* Recommended Reconnection Behaviour