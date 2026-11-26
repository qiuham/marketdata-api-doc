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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-info-funding'
updated_at: 2026-11-26
---

# Funding Info

Get account funding info

#### Response fields

| Index | Field                | Type                                              | Description                                                                      |
| :---- | :------------------- | :------------------------------------------------ | :------------------------------------------------------------------------------- |
| \[0]  | "sym"                | string                                            | "sym"                                                                            |
| \[1]  | SYMBOL               | string                                            | The symbol the information pertains to (funding currencies)                      |
| \[2]  | FUNDING\_INFO\_ARRAY | [Funding info array](#funding-info-array-index-3) | Contains info on the yield and duration of the user's taken and provided funding |

#### Funding info array (Index \[3])

| Index | Term           | Type  | Description                                    |
| ----- | :------------- | ----- | ---------------------------------------------- |
| \[0]  | YIELD\_LOAN    | float | Weighted average rate for taken funding        |
| \[1]  | YIELD\_LEND    | float | Weighted average rate for provided funding     |
| \[2]  | DURATION\_LOAN | float | Weighted average duration for taken funding    |
| \[3]  | DURATION\_LEND | float | Weighted average duration for provided funding |

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
    "/auth/r/info/funding/{key}": {
      "post": {
        "summary": "Funding Info",
        "description": "Get account funding info",
        "operationId": "rest-auth-info-funding",
        "parameters": [
          {
            "name": "key",
            "in": "path",
            "description": "SYMBOL",
            "schema": {
              "type": "string"
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
                    "value": "[\n  \"sym\", //\"sym\"\t\n  \"fUST\", //SYMBOL\n  [\n    0.0024, //YIELD_LOAN\n    0.0024, //YIELD_LEND\n    1.9522164351851852, //DURATION_LOAN\n    1.4818560606060607 //DURATION_LEND\n  ]\n]"
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
