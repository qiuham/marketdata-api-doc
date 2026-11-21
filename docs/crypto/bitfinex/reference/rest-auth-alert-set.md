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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-alert-set'
updated_at: 2026-11-21
---

# Alert Set

Sets up a price alert at the given value

#### Response data

| Index | Term      | Type   | Description                                                                                                                                                    |
| ----- | :-------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[0]  | INFO      | string | 'type:pair:price'                                                                                                                                              |
| \[1]  | TYPE      | string | Alert type ('price')                                                                                                                                           |
| \[2]  | PAIR      | string | Pair on which the price alert is active (tBTCUSD, tBTCUST, ...)                                                                                                |
| \[3]  | PRICE     | float  | Alert price                                                                                                                                                    |
| \[4]  | COUNTDOWN | int    | This is set to 100 when the alert is placed. Each time the alert is triggered, this number will go down. When the countdown reaches 0, the alert gets removed. |

**Ratelimit**: 90 req/min

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
    "/auth/w/alert/set": {
      "post": {
        "summary": "Alert Set",
        "description": "Sets up a price alert at the given value",
        "operationId": "rest-auth-alert-set",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "symbol",
                  "price"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "default": "",
                    "description": "Specify the alert type ('price')"
                  },
                  "symbol": {
                    "type": "string",
                    "default": "",
                    "description": "Specify the alert symbol (ex. 'tBTCUSD')"
                  },
                  "price": {
                    "type": "string",
                    "default": "",
                    "description": "Specify the alert price (ex. '232.2')"
                  },
                  "count": {
                    "type": "integer",
                    "description": "Set the number of times an alert can trigger (ex. 100)",
                    "default": ""
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
                    "value": "[\n  \"price:tETHUSD:185\", //INFO\n  \"price\", //TYPE\n  \"tETHUSD\", //PAIR\n  185, //PRICE\n  100 //COUNTDOWN\n]\n"
                  }
                },
                "schema": {
                  "type": "array"
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
