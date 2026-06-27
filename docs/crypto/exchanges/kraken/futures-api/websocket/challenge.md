---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/challenge
api_type: WebSocket
updated_at: 2026-05-27 19:55:13.754749
---

# Challenge

**WebSocket Endpoint:** `wss://futures.kraken.com/ws/v1`
    
    challenge

This request returns a challenge to be used in handshake for user authentication.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

The request event type

**api_key** `string` *required*

The user API key.
    
    
    {  
      "event": "challenge",  
      "api_key": "CMl2SeSn09Tz+2tWuzPfdaJdsahq6qv5UaexXuQ3SnahDQU/gO3aT+"  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

Always challenge

**message** `string`

The message that user will have to sign for authentication reasons 
    
    
    {  
      "event": "challenge",  
      "message": "226aee50-88fc-4618-a42a-34f7709570b2"  
    }  
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Json Error"  
    }