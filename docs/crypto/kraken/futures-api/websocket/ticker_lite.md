---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/ticker_lite
api_type: WebSocket
updated_at: 2026-05-27 19:56:12.617041
---

# Ticker Lite

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    ticker_lite

The ticker lite feed returns ticker information about listed products. Delta messages are throttled such that they are published every 1s.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `ticker_lite`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribe",  
      "feed": "ticker_lite",  
      "product_ids": ["PI_XBTUSD", "FI_ETHUSD_210625"]  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `ticker_lite`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribed ",  
      "feed": "ticker_lite",  
      "product_ids": ["PI_XBTUSD"]  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Data
  * Subscription Data 2

### MESSAGE BODY

**feed** `string`

The subscribed feed.

**product_id** `string`

The subscribed product (referred also as instrument or symbol).

**bid** `positive float`

The price of the current best bid.

**ask** `positive float`

The price of the current best ask.

**change** `float`

The 24h change in price.

**premium** `float`

The premium associated with the product.

**volume** `positive float`

The sum of the sizes of all fills observed in the last 24 hours.

**tag** `string`

Currently can be `week`, `month` or `quarter`. Other tags may be added without notice..

**pair** `string`

The currency pair of the instrument.

**dtm** `integer`

The days until maturity.

**maturityTime** positive integer

Maturity time in milliseconds.

**volumeQuote** positive float

The same as `volume` except that, for multi-collateral futures, it is converted to the non-base currency

**greeks** `structure`

The current Greeks, if this is an option. 

**iv** `float`

The option's implied volatility. 

**delta** `float`

Delta, the option value's sensitivity to change in the underlying price. 

**theta** `float`

Theta, the option value's sensitivity to the passage of time. 

**gamma** `float`

Gamma, delta's sensitivity to change in the underlying price. 

**vega** `float`

Vega, the option value's sensitivity to change in volatility. 

**rho** `float`

Rho, the option value's sensitivity to the interest ratea. 
    
    
    {  
      "feed": "ticker_lite",  
      "product_id": "PI_XBTUSD",  
      "bid": 34932,  
      "ask": 34949.5,  
      "change": 3.3705205220015966,  
      "premium": 0.1,  
      "volume": 264126741,  
      "tag": "perpetual",  
      "pair": "XBT:USD",  
      "dtm": 0,  
      "maturityTime": 0,  
      "volumeQuote": 264126741  
    }  
    
    
    
    {  
      "feed": "ticker_lite",  
      "product_id": "FI_ETHUSD_210625",  
      "bid": 1753.45,  
      "ask": 1760.35,  
      "change": 13.448175559936647,  
      "premium": 9.1,  
      "volume": 6899673.0,  
      "tag": "semiannual",  
      "pair": "ETH:USD",  
      "dtm": 141,  
      "maturityTime": 1624633200000,  
      "volumeQuote": 6899673.0  
    }  
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid product id`  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Invalid product id"  
    }