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
source_url: 'https://docs.bitfinex.com/reference/rest-public-trades'
updated_at: 2026-11-19
---

# Trades

The trades endpoint allows the retrieval of past public trades and includes details such as price, size, and time. Optional parameters can be used to limit the number of results; you can specify a start and end timestamp, a limit, and a sorting method.

### Response Fields

#### For trading pair symbols (ex. tBTCUSD)

| Index | Field  | Type  | Description                                       |
| ----- | ------ | ----- | ------------------------------------------------- |
| \[0]  | ID     | int   | ID of the trade                                   |
| \[1]  | MTS    | int   | Millisecond epoch timestamp                       |
| \[2]  | AMOUNT | float | How much was bought (positive) or sold (negative) |
| \[3]  | PRICE  | float | Price at which the trade was executed             |

#### For funding currency symbols (ex. fUSD)

| Index | Field  | Type  | Description                                       |
| ----- | ------ | ----- | ------------------------------------------------- |
| \[0]  | ID     | int   | ID of the trade                                   |
| \[1]  | MTS    | int   | Millisecond epoch timestamp                       |
| \[2]  | AMOUNT | float | How much was bought (positive) or sold (negative) |
| \[3]  | RATE   | float | Rate at which funding transaction occurred        |
| \[4]  | PERIOD | int   | Amount of time the funding transaction was for    |

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">15 reqs/min (requests per minute)</td>
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
    "/trades/{symbol}/hist": {
      "get": {
        "summary": "Trades",
        "description": "The trades endpoint allows the retrieval of past public trades and includes details such as price, size, and time. Optional parameters can be used to limit the number of results; you can specify a start and end timestamp, a limit, and a sorting method.",
        "operationId": "rest-public-trades",
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
            "name": "limit",
            "in": "query",
            "description": "Number of records in response (max. 10000).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "120"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": -1
            }
          },
          {
            "name": "start",
            "in": "query",
            "description": "If start is given, only records with MTS >= start (milliseconds) will be given as response.",
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          },
          {
            "name": "end",
            "in": "query",
            "description": "If end is given, only records with MTS <= end (milliseconds) will be given as response.",
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "// on trading pairs (ex. tBTCUSD)\n[\n  [\n    388063448, //ID\n    1567526214876, //MTS\n    1.918524, //AMOUNT\n    10682 //PRICE\n  ],\n  [...]\n]\n\n// on funding currencies (ex. fUSD)\n[\n  [\n    124486873, //ID\n    1567526287066, //MTS\n    -210.69675707, //AMOUNT\n    0.00034369, //RATE\n    2 //PERIOD\n  ],\n  [...]\n]"
                  }
                }
              }
            }
          }
        },
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
