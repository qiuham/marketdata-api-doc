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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-calc-order-avail'
updated_at: 2026-11-19
---

# Balance Available for Orders/Offers

Calculate the balance available for orders/offers

**Fields**

| Fields        | Type  | Description                      |
| ------------- | ----- | -------------------------------- |
| AMOUNT\_AVAIL | float | Amount available for order/offer |

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
    "/auth/calc/order/avail": {
      "post": {
        "summary": "Balance Available for Orders/Offers",
        "description": "Calculate the balance available for orders/offers",
        "operationId": "rest-auth-calc-order-avail",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "symbol",
                  "type"
                ],
                "properties": {
                  "symbol": {
                    "type": "string",
                    "description": "Symbol (tBTCUSD, tBTCUST, fUSD, .... )"
                  },
                  "dir": {
                    "type": "integer",
                    "description": "Direction of the order (1 for by, -1 for sell) (Mandatory for EXCHANGE and MARGIN type, not used for FUNDING)",
                    "format": "int32"
                  },
                  "rate": {
                    "type": "string",
                    "description": "Order price (Mandatory for EXCHANGE and MARGIN type, not used for FUNDING)"
                  },
                  "type": {
                    "type": "string",
                    "description": "Type of the order/offer EXCHANGE, MARGIN, DERIV, or FUNDING"
                  },
                  "lev": {
                    "type": "string",
                    "description": "Leverage that you want to use in calculating the max order amount (DERIV only)"
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
                    "value": "[AMOUNT_AVAIL]\n\n[0.8056309]"
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
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = `v2/auth/calc/order/avail` \n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n      symbol: 'tBTCUSD',\n      dir: 1, // buy\n      rate: '800',\n      type: 'EXCHANGE' // (optional) body parameters go here\n  \t}),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })\n",
              "name": "JavaScript"
            }
          ],
          "samples-languages": [
            "javascript"
          ]
        }
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
