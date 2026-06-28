---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/account_log
api_type: WebSocket
updated_at: 2026-05-27 19:54:52.098780
---

# Account Log

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    account_log

This subscription feed publishes account information.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `account_log`

**api_key** `string` *required*

The user api key

**original_challenge** `string` *required*

The message that is received from a challenge request

**signed_challenge** `string` *required*

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribe",  
      "feed": "account_log",  
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

The requested subscription feed `account_log`

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "account_log",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Snapshot & Delta

  * Response Fields
  * Subscription Snapshot Data
  * Subscription Delta Data

### MESSAGE BODY

**feed** `string`

The subscribed feed

**log** `list of structures`

A list containing the account logs 

**id** `positive integer`

The identifier of the log.

**date** `ISO8601 datetime`

The creation time of the log according to server date and time

**asset** `string`

The asset related of the booking

**info** `string`

A description of the booking.

**booking_uid** `string`

The unique id of the booking.

**margin_account** `string`

The name of the account associated with the entry `old_balance`.

**old_balance** `float`

The account balance before the described in `info` action.

**new_balance** `float`

The new balance of wallet or new size of the position after the described action in `info`.

**old_average_entry_price** `positive float`

The average entry price of the position prior to this trade.

**new_average_entry_price** `positive float`

The average entry price of the position after this trade.

**trade_price** `positive float`

The price the trade was executed at.

**mark_price** `positive float`

The mark price at the time the trade was executed.

**realized_pnl** `float`

The pnl that is realized by reducing the position.

**fee** `float`

The fee paid.

**execution** `string`

The uid of the associated execution.

**collateral** `string`

The currency of the associated entry.

**funding_rate** `float`

The absolute funding rate.

**realized_funding** `float`

The funding rate realized due to change in position size or end of funding rate period.

**conversion_spread_percentage** `float`

The percentage conversion spread used in a currency conversion.

**liquidation_fee** `float`

The liquidation fee associated with a liquidation/assignment entry. Not applicable for inverse futures.
    
    
    {  
      "feed": "account_log_snapshot",  
      "logs": [  
        {  
          "id": 1690,  
          "date": "2019-07-11T08:00:00.000Z",  
          "asset": "bch",  
          "info": "funding rate change",  
          "booking_uid": "86fdc252-1b6e-40ec-ac1d-c7bd46ddeebf",  
          "margin_account": "f-bch:usd",  
          "old_balance": 0.01215667051,  
          "new_balance": 0.01215736653,  
          "old_average_entry_price": 0.0,  
          "new_average_entry_price": 0.0,  
          "trade_price": 0.0,  
          "mark_price": 0.0,  
          "realized_pnl": 0.0,  
          "fee": 0.0,  
          "execution": "",  
          "collateral": "bch",  
          "funding_rate": -8.7002552653e-8,  
          "realized_funding": 6.9602e-7,  
          "conversion_spread_percentage": 0.0,  
          "liquidation_fee": 0.0  
        },  
        {  
          "id": 1689,  
          "date": "2019-07-11T04:00:00.000Z",  
          "asset": "bch",  
          "info": "funding rate change",  
          "booking_uid": "680d3973-5774-4a9d-b807-ab8aa73f95c3",  
          "margin_account": "f-bch:usd",  
          "old_balance": 0.01215715298,  
          "new_balance": 0.01215667051,  
          "old_average_entry_price": 0.0,  
          "new_average_entry_price": 0.0,  
          "trade_price": 0.0,  
          "mark_price": 0.0,  
          "realized_pnl": 0.0,  
          "fee": 0.0,  
          "execution": "",  
          "collateral": "bch",  
          "funding_rate": 6.0309345058e-8,  
          "realized_funding": -4.8247e-7,  
          "conversion_spread_percentage": 0.0,  
          "liquidation_fee": 0.0  
        },  
        {  
          "id": 1688,  
          "date": "2019-07-11T00:00:00.000Z",  
          "asset": "bch",  
          "info": "funding rate change",  
          "booking_uid": "72e3396e-8fc4-4bd9-9379-8e2b2225af85",  
          "margin_account": "f-bch:usd",  
          "old_balance": 0.01215847263,  
          "new_balance": 0.01215715298,  
          "old_average_entry_price": 0.0,  
          "new_average_entry_price": 0.0,  
          "trade_price": 0.0,  
          "mark_price": 0.0,  
          "realized_pnl": 0.0,  
          "fee": 0.0,  
          "execution": "",  
          "collateral": "bch",  
          "funding_rate": 1.64955714332e-7,  
          "realized_funding": -1.31965e-6,  
          "conversion_spread_percentage": 0.0,  
          "liquidation_fee": 0.0  
        }  
      ]  
    }  
    
    
    
    {  
      "feed": "account_log",  
      "new_entry": {  
        "id": 1697,  
        "date": "2019-07-11T13: 00: 27.632Z",  
        "asset": "pi_bchusd",  
        "info": "futures trade",  
        "booking_uid": "55a02b5b-2c90-4d43-b0eb-eb3801d50e3f",  
        "margin_account": "f-bch:usd",  
        "old_balance": 1.0,  
        "new_balance": 2.0,  
        "old_average_entry_price": 413.3,  
        "new_average_entry_price": 374.3445326979084,  
        "trade_price": 342.1,  
        "mark_price": 342.4,  
        "realized_pnl": 0.0,  
        "fee": 0.0,  
        "execution": "fc49fea9-8827-4a2e-8e36-c047523ddc30",  
        "collateral": "bch"  
        "funding_rate": 1.64955714332e-07,  
        "realized_funding": -1.31965e-06,  
        "conversion_spread_percentage": 0.0,  
        "liquidation_fee": 0.0  
      
      }  
    }  
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Invalid feed"  
    }