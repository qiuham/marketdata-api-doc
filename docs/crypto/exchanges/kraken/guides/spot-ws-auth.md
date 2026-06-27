---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-ws-auth
api_type: WebSocket
updated_at: 2026-05-27 19:59:20.489834
---

# Spot Websockets Authentication

## Retrieving Authentication Token from REST

For the websockets API, the client must retrieve an authentication token via the REST endpoint [GetWebSocketsToken](/api/docs/rest-api/get-websockets-token).

This token can be used as the `token` parameter in the message body for all authenticated websockets endpoints for the duration of the websockets connection.
    
    
    {  
      "event": "subscribe",  
      "subscription":  
      {  
        "name": "ownTrades",  
        "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"  
      }  
    }  
    

caution

The websockets token should be used within 15 minutes of creation.

  * Retrieving Authentication Token from REST