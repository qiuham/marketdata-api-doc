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
source_url: 'https://docs.bitfinex.com/reference/generate-token'
updated_at: 2026-11-27
---

# Generate Token

Generates an auth token that could be used for api requests

> 📘 Caps
>
> Available caps are:
>
> * a - account
> * o - orders
> * f - funding
> * s - settings
> * w - wallets
> * wd - withdraw -- writePermission: true is required for wd permission
> * bp - bfxpay

#### Response data

| Index | Term  | Type   | Description                    |
| ----- | :---- | ------ | ------------------------------ |
| \[0]  | TOKEN | string | Generated authentication token |

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
    "/auth/w/token": {
      "post": {
        "summary": "Generate Token",
        "description": "Generates an auth token that could be used for api requests",
        "operationId": "generate-token",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "scope"
                ],
                "properties": {
                  "scope": {
                    "type": "string",
                    "description": "scope of the token, set it to `api`",
                    "default": "api"
                  },
                  "ttl": {
                    "type": "integer",
                    "description": "time to live in seconds",
                    "default": 120,
                    "format": "int32"
                  },
                  "caps": {
                    "type": "array",
                    "description": "token caps/permissions, available values: [a, o, f, s, w, wd, bp]",
                    "items": {
                      "type": "string"
                    }
                  },
                  "writePermission": {
                    "type": "boolean",
                    "description": "token write permission for the caps",
                    "default": false
                  },
                  "_cust_ip": {
                    "type": "string",
                    "description": "user's ip address"
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
                    "value": "[\n  \"pub:api:665b6328-cc1e-4627-8caf-9ea5ddb8dfb0-caps:a:o:f-write\" //TOKEN\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "example": "pub:api:665b6328-cc1e-4627-8caf-9ea5ddb8dfb0-caps:a:o:f-write"
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
