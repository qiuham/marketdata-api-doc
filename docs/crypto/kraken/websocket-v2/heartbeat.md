---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/heartbeat
api_type: WebSocket
updated_at: 2026-05-27 20:12:16.692882
---

# Heartbeat

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    heartbeat

The `heartbeat` channel provides a mechanism to verify that the connection is alive.

Heartbeat messages are sent approximately once every second **in the absence of any other channel updates**.

There is no option to directly request a `heartbeat` subscription, the heartbeats will be automatically generated on subscription to any channel.

## Update Response

The channel name is the indicator of a heartbeat, here is no other data in the heartbeat payload.

  * Update Response
  * Example

### MESSAGE BODY

**channel** `string`

`heartbeat`
    
    
    {  
        "channel": "heartbeat"  
    }