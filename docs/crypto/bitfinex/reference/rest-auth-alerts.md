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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-alerts'
updated_at: 2026-11-26
---

# Alert List

Retrieve a list of active price alerts.

#### Response data

| Index    | Field        | Type                                  | Description                                            |
| :------- | :----------- | :------------------------------------ | :----------------------------------------------------- |
| \[0...n] | ALERT\_ARRAY | [Alert array](#alert-arrays-index-0n) | Each index contains one of the n current user's alerts |

#### Alert arrays (Index \[0...n])

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[0]</td>
      <td>INFO</td>
      <td>String</td>
      <td>'type:pair:price'</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>Alert type ('price')</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>PAIR</td>
      <td>String</td>
      <td>Pair on which the price alert is active (tBTCUSD, tBTCUST, ...)</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>PRICE</td>
      <td>Float</td>
      <td>Alert price</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>COUNTDOWN</td>
      <td>Int</td>
      <td>This is set to 100 when the alert is placed. Each time the alert is triggered, this number will go down. When the countdown reaches 0, the alert gets removed.</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

**Ratelimit**: 45 req/min

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/auth/r/alerts": {
      "post": {
        "summary": "Alert List",
        "description": "Retrieve a list of active price alerts.",
        "operationId": "rest-auth-alerts",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "RAW_BODY": {
                    "type": "string",
                    "default": "{}",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n [\n   \"price:tETHUSD:220\", //INFO\n   \"price\", //TYPE\n   \"tETHUSD\", //PAIR\n   220, //PRICE\n   100 //COUNTDOWN\n ], //ALERT_ARRAY\n ...\n]\n"
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
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
