---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-system-status
api_type: REST
updated_at: 2026-05-27 20:05:04.239037
---

# Get System Status

**GET** `https://api.kraken.com/0/public/SystemStatus`

Get the current system status or trading mode.

## Responses

  * 200

Success response

  * application/json
* Schema

**Schema**

**result**

**status** `string`

Current system status:
* `online` Kraken is operating normally. All order types may be submitted and trades can occur.
* `maintenance` The exchange is offline. No new orders or cancellations may be submitted.
* `cancel_only` Resting (open) orders can be cancelled but no new orders may be submitted. No trades will occur.
* `post_only` Only post-only limit orders can be submitted. Existing orders may still be cancelled. No trades will occur.

**Possible values:** [`online`, `maintenance`, `cancel_only`, `post_only`]

**timestamp** `string`

Current timestamp (RFC3339)

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/SystemStatus' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

ResponseClear

Click the `Send API Request` button above and see the response here!