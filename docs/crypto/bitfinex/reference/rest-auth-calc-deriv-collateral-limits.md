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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-calc-deriv-collateral-limits'
updated_at: 2026-11-26
---

# Derivative Position Collateral Limits

Calculate the minimum and maximum collateral that can be assigned to your derivative position.

When adjusting collateral on a derivative position, the system can sometimes return an error: \["error",110202,"collateral: market risk"]. The error prevents the reduction of assigned collateral to a point where the risk of liquidation would be too high. When updating the collateral through the UI, minimum and maximum values are shown to prevent such an error. When updating collateral through the API, this endpoint can be used to calculate these minimum and maximum values.

> 🚧 Position required
>
> An open position is required on the pair for which you would like to calculate the collateral limits.

**Response fields**

| Index | Field           | Type  | Description                                                                                      |
| ----- | :-------------- | ----- | ------------------------------------------------------------------------------------------------ |
| \[0]  | MIN\_COLLATERAL | float | Minimum amount of collateral that can be assigned to your current position on the provided pair. |
| \[1]  | MAX\_COLLATERAL | float | Maximum amount of collateral that can be assigned to your current position on the provided pair. |

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
    "/auth/calc/deriv/collateral/limits": {
      "post": {
        "summary": "Derivative Position Collateral Limits",
        "description": "Calculate the minimum and maximum collateral that can be assigned to your derivative position.",
        "operationId": "rest-auth-calc-deriv-collateral-limits",
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
                    "value": "[ \n  18.289, //MIN_COLLATERAL\n  896.67400419 //MAX_COLLATERAL\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "example": 18.289,
                    "default": 0
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
