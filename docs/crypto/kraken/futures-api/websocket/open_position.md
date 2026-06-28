---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/open_position
api_type: WebSocket
updated_at: 2026-05-27 19:55:57.883531
---

# Open Position

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    open_positions

This subscription feed publishes the open positions of the user account.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `open_positions`

**api_key** `string` *required*

The user api key

**original_challenge** `string` *required*

The message that is received from a challenge request

**signed_challenge** `string` *required*

The signed challenge message with user api secret
    
    
      
    {  
      "event": "subscribe",  
      "feed": "open_positions",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
      
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `open_positions `

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "open_positions",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Data

### MESSAGE BODY

**feed** `string`

The subscribed feed

**account** `string`

The user account

**positions** `list of structures`

A list containing the user open positions. 

**instrument** `string`

The instrument (referred also as symbol or product_id) of the order

**balance** `float`

The size of the position.

**entry_price** `positive float`

The average entry price of the instrument.

**mark_price** `positive float`

The market price of the position instrument.

**index_price** `positive float`

The index price of the position instrument.

**pnl** `float`

The profit and loss of the position.

**liquidation_threshold** `float`

The mark price of the contract at which the position will be liquidated.

**return_on_equity** `float`

The percentage gain or loss relative to the initial margin used in the position. Formula: PnL/IM

**unrealized_funding** `float`

Unrealised funding from funding rate

**effective_leverage** `float`

How leveraged the net position is in a given margin account. Formula: Position Value at Market / Portfolio Value.

**initial_margin** `float`

The initial margin for the open position. 

**initial_margin_with_orders** `float`

The initial margin for the open position and open orders of the same instrument.

**maintenance_margin** `float`

The maintenance margin for the open. 

**pnl_currency** `float`

The profit currency for the position, not returned for inverse positions. 

**seq** `float`

The message sequence. 

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
      "feed": "open_positions",  
      "account": "DemoUser",  
      "positions": [  
        {  
          "instrument":"PI_XRPUSD"    
          "balance":500.0,  
          "pnl":-239.6506683474764,  
          "entry_price":0.3985,  
          "mark_price":0.4925844,  
          "index_price":0.49756,  
          "liquidation_threshold":0.0,  
          "effective_leverage":0.17404676894304316,  
          "return_on_equity":-2.3609636135508127,  
          "initial_margin":101.5054475943615,  
          "initial_margin_with_orders":101.5054475943615,  
          "maintenance_margin":50.75272379718075  
        },  
        {  
          "instrument":"PF_XBTUSD",  
          "balance":0.04,  
          "pnl":119.56244985549435,  
          "entry_price":26911.75,  
          "mark_price":29900.81124638736,  
          "index_price":29900.47,  
          "liquidation_threshold":9572.804662403718,  
          "effective_leverage":0.31865408963748215,  
          "return_on_equity":5.553450159107747,  
          "unrealized_funding":0.0004114160669590132,  
          "initial_margin":21.529400000000003,  
          "initial_margin_with_orders":21.529400000000003,  
          "maintenance_margin":10.764700000000001,  
          "pnl_currency":"USD"  
        },  
        {  
          "instrument":"OF_ETHUSD_240101_1000_C",  
          "balance":0.04,  
          "pnl":119.56244985549435,  
          "entry_price":26911.75,  
          "mark_price":29900.81124638736,  
          "index_price":29900.47,  
          "return_on_equity":5.553450159107747,  
          "iv": 0.3,  
          "delta": 0.5,  
          "gamma": 0.5,  
          "vega": 0.5,  
          "theta": 0.5,  
          "rho": 0.5  
        }  
      ],  
      "seq":4,  
      "timestamp":1687383625330  
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