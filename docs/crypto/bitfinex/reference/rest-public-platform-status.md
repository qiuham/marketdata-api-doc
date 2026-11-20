---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/reference/rest-public-platform-status'
updated_at: 2026-11-20
---

# Platform Status

Get the current status of the platform, “Operative” or “Maintenance”. Maintenance periods generally last for a few minutes to a couple of hours and may be necessary from time to time during infrastructure upgrades. 

For real-time status notifications, we suggest using Websockets to listen to events 20060/20061. For more information about Websockets please see https://docs.bitfinex.com/v2/docs/ws-general.

For more information on REST Public endpoint example code structure please see https://docs.bitfinex.com/v2/docs/rest-public.

### Response Fields

| Index | Field  | Type | Description                  |
| ----- | ------ | ---- | ---------------------------- |
| \[0]  | STATUS | int  | 1: operative, 0: maintenance |

> 🚧 Maintenance mode
>
> When the platform is marked in maintenance mode, bots should stop all trading activity. Cancelling and placing new orders will not be possible during this time.

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">30 reqs/min (requests per minute)</td>
  </tr>
</table>
`}</HTMLBlock>

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings-public",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api-pub.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/platform/status": {
      "get": {
        "summary": "Platform Status",
        "description": "Get the current status of the platform, “Operative” or “Maintenance”. Maintenance periods generally last for a few minutes to a couple of hours and may be necessary from time to time during infrastructure upgrades. \n\nFor real-time status notifications, we suggest using Websockets to listen to events 20060/20061. For more information about Websockets please see https://docs.bitfinex.com/v2/docs/ws-general.\n\nFor more information on REST Public endpoint example code structure please see https://docs.bitfinex.com/v2/docs/rest-public.",
        "operationId": "rest-public-platform-status",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  1 //STATUS\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "integer",
                    "example": 1,
                    "default": 0
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
