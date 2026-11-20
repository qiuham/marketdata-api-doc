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
source_url: 'https://docs.bitfinex.com/reference/rest-public-book'
updated_at: 2026-11-20
---

# Book

The Public Books endpoint allows you to keep track of the state of Bitfinex order books on a price aggregated basis with customizable precision. Raw books can be retrieved by using precision R0.

### Response Fields (Books)

#### For trading pair symbols (ex. tBTCUSD)

| Index | Field  | Type  | Description                                                                  |
| ----- | ------ | ----- | ---------------------------------------------------------------------------- |
| \[0]  | PRICE  | float | Price level                                                                  |
| \[1]  | COUNT  | int   | Number of orders at that price level                                         |
| \[2]  | AMOUNT | float | Total amount available at that price level (if AMOUNT > 0 then bid else ask) |

#### For funding currency symbols (ex. fUSD)

| Index | Field  | Type  | Description                                                                  |
| ----- | ------ | ----- | ---------------------------------------------------------------------------- |
| \[0]  | RATE   | float | Rate level                                                                   |
| \[1]  | PERIOD | int   | Period level                                                                 |
| \[2]  | COUNT  | int   | Number of orders at that price level                                         |
| \[3]  | AMOUNT | float | Total amount available at that price level (if AMOUNT > 0 then ask else bid) |

### Response Fields (Raw Books)

#### For trading pair symbols (ex. tBTCUSD)

| Index | Field     | Type  | Description                                                                  |
| ----- | --------- | ----- | ---------------------------------------------------------------------------- |
| \[0]  | ORDER\_ID | int   | Order ID                                                                     |
| \[1]  | PRICE     | float | Price level                                                                  |
| \[2]  | AMOUNT    | float | Total amount available at that price level (if AMOUNT > 0 then bid else ask) |

#### For funding currency symbols (ex. fUSD)

| Index | Field     | Type  | Description                                                                  |
| ----- | --------- | ----- | ---------------------------------------------------------------------------- |
| \[0]  | OFFER\_ID | int   | Offer ID                                                                     |
| \[1]  | PERIOD    | int   | Period level                                                                 |
| \[2]  | RATE      | float | Rate level                                                                   |
| \[3]  | AMOUNT    | float | Total amount available at that price level (if AMOUNT > 0 then ask else bid) |

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">240 reqs/min (requests per minute)</td>
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
    "/book/{symbol}/{precision}": {
      "get": {
        "summary": "Book",
        "description": "The Public Books endpoint allows you to keep track of the state of Bitfinex order books on a price aggregated basis with customizable precision. Raw books can be retrieved by using precision R0.",
        "operationId": "rest-public-book",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "description": "The symbol you want information about. (e.g. tBTCUSD, tETHUSD, fUSD, fBTC)",
            "required": true,
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
            }
          },
          {
            "name": "precision",
            "in": "path",
            "description": "Level of price aggregation (P0, P1, P2, P3, P4 and R0).",
            "schema": {
              "type": "string",
              "default": "P0"
            },
            "required": true
          },
          {
            "name": "len",
            "in": "query",
            "description": "Number of price points (\"1\", \"25\", \"100\", \"250\").",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 25
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result (Books)": {
                    "value": "// on trading pairs (ex. tBTCUSD)\n[\n  [\n    8744.9, //PRICE\n    2, //COUNT\n    0.45603413 //AMOUNT\n  ],\n  [...]\n]\n\n// on funding currencies (ex. fUSD)\n[\n  [\n  \t0.0003301, //RATE\n  \t30, //PERIOD\n  \t1, //COUNT\n  \t-3862.874 //AMOUNT\n  ],\n  [...]\n]"
                  },
                  "Result (Raw Books)": {
                    "value": "// on trading pairs (ex. tBTCUSD)\n[\n  [\n    34006738527, //ORDER_ID\n    8744.9, //PRICE\n    0.25603413 //AMOUNT\n  ],\n  [...]\n]\n\n// on funding currencies (ex. fUSD)\n[\n  [\n  \t645902785, //OFFER_ID\n  \t30, //PERIOD\n  \t0.0003301, //RATE\n  \t-3862.874 //AMOUNT\n\t],\n  [...]\n]"
                  }
                }
              }
            }
          },
          "500": {
            "description": "500",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[ \n\t\"error\", \n  10020, \n  \"symbol: invalid\" \n]"
                  }
                },
                "schema": {
                  "type": "array"
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
