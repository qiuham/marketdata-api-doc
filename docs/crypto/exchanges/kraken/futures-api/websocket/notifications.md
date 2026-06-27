---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/notifications
api_type: WebSocket
updated_at: 2026-05-27 19:55:35.948220
---

# Notification

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    notifications_auth

This subscription feed publishes notifications to the client.

Authentication is required.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `notifications_auth`

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribe",  
      "feed": "open_orders",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Success

  * Response Fields
  * Successful

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `notifications_auth`

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "notifications_auth",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Snapshot Data

**feed** `string`

The subscribed feed

**notifications** `list of structures`

A list containing the notifications.

**id** `positive integer`

The notification id

**type** `string`

The notification type. Existing types are `market`, `general`, `new_feature`, `bug_fix`, `maintenance`, `settlement`. .

**priority** `string`

The notification priority. Existing priorities are: `low`, `medium`, `high`. If priority is `high` then it implies downtime will occur at `effective_time` when type is `maintenance`.

**note** `string`

The notification note. A short description about the specific notification.

**effective_time** `integer`

The time that notification is taking effect.

**expected_downtime_minutes** `integer`

The expected downtime in minutes or absent if no downtime is expected.
    
    
    {  
      "feed": "notifications_auth",  
      "notifications": [  
        {  
          "id": 5,  
          "type": "market",  
          "priority": "low",  
          "note": "A note describing the notification.",  
          "effective_time": 1520288300000  
        }  
      ]  
    }  
    

## Response Error

  * Response Fields
  * Example Error

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