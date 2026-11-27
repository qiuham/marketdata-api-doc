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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-deriv-pos-collateral-set'
updated_at: 2026-11-27
---

# Derivative Position Collateral

Update the amount of collateral assigned to a derivative position

Sets the amount of collateral, applied to the active derivative position, for the given symbol.

![](https://files.readme.io/1e9466b-Screenshot_2.png "Screenshot_2.png")

**Response Fields**

| Index | Field  | Type | Description             |
| ----- | :----- | ---- | ----------------------- |
| \[0]  | STATUS | int  | Returns 1 if successful |

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
    "/auth/w/deriv/collateral/set": {
      "post": {
        "summary": "Derivative Position Collateral",
        "description": "Update the amount of collateral assigned to a derivative position",
        "operationId": "rest-auth-deriv-pos-collateral-set",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "symbol": {
                    "type": "string",
                    "description": "The derivative symbol, e.g. tBTCF0:USTF0",
                    "default": "tBTCF0:USTF0"
                  },
                  "collateral": {
                    "type": "number",
                    "description": "The amount of collateral to apply to the open position",
                    "default": 1150.61,
                    "format": "float"
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
                    "value": "[\n  [\n    1 //STATUS\n  ]\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
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
          },
          "500": {
            "description": "500",
            "content": {
              "application/json": {
                "examples": {
                  "Collateral amount is too large / small": {
                    "value": "[\n  \"error\", \n  10020,\n  \"collateral: insufficient\"\n]"
                  },
                  "Symbol does not support derivatives": {
                    "value": "[\n  \"error\",\n  10020,\n  \"symbol: invalid\"\n]"
                  },
                  "No active positions for the given symbol": {
                    "value": "[\n  \"error\", \n  10020, \n  \"position: invalid\"\n]"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "Collateral amount is too large / small",
                      "type": "array"
                    },
                    {
                      "title": "Symbol does not support derivatives",
                      "type": "array"
                    },
                    {
                      "title": "No active positions for the given symbol",
                      "type": "array"
                    }
                  ]
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
