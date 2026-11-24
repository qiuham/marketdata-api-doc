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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-alert-del'
updated_at: 2026-11-24
---

# Alert Delete

Delete an active alert.

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
    "/auth/w/alert/price:{symbol}:{price}/del": {
      "post": {
        "summary": "Alert Delete",
        "description": "Delete an active alert.",
        "operationId": "rest-auth-alert-del",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
            },
            "required": true
          },
          {
            "name": "price",
            "in": "path",
            "schema": {
              "type": "string",
              "default": 600
            },
            "required": true
          }
        ],
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
                    "value": "[\n  true \n] \n"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "boolean",
                    "example": true,
                    "default": true
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
