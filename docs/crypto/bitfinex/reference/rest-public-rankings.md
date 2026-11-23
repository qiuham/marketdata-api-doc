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
source_url: 'https://docs.bitfinex.com/reference/rest-public-rankings'
updated_at: 2026-11-23
---

# Leaderboards

The leaderboards endpoint allows you to retrieve leaderboard standings for unrealized profit (period delta), unrealized profit (inception), volume, and realized profit.

> 📘 Leaderboard Competitions
>
> The [Configs Endpoint](https://dash.readme.io/project/bitfinex/v2/refs/rest-public-conf) can be used to retrieve a list of all competitions shown on our [Leaderboards](https://leaderboard.bitfinex.com/).
>
> The endpoint can be called like this: <https://api-pub.bitfinex.com/v2/conf/pub:list:competitions>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Available Time Frames
      </th>

      <th style={{ textAlign: "left" }}>
        Available Symbols
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        "plu\_diff" - (Unrealised Profit (Period Delta))
      </td>

      <td style={{ textAlign: "left" }}>
        "1w", "1M"
      </td>

      <td style={{ textAlign: "left" }}>
        tGLOBAL:USD
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        "plu" - (Unrealised Profit (Inception))
      </td>

      <td style={{ textAlign: "left" }}>
        "3h" - for specific pairs\
        "1w", "1M" - for tGLOBAL:USD
      </td>

      <td style={{ textAlign: "left" }}>
        * Trading Pairs (e.g. tBTCUSD, tETHUSD)
        * tGLOBAL:USD
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        "plr" - (Realized Profit)
      </td>

      <td style={{ textAlign: "left" }}>
        "1w", "1M"
      </td>

      <td style={{ textAlign: "left" }}>
        tGLOBAL:USD
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        "vol" - (Volume)
      </td>

      <td style={{ textAlign: "left" }}>
        "3h", "1w", "1M"
      </td>

      <td style={{ textAlign: "left" }}>
        * Trading Pairs (e.g. tBTCUSD, tETHUSD)
        * tGLOBAL:USD
      </td>
    </tr>
  </tbody>
</Table>

**Response Details**

| Fields          | Type   | Description                                            |
| --------------- | ------ | ------------------------------------------------------ |
| MTS             | int    | millisecond timestamp                                  |
| USERNAME        | string | Username                                               |
| RANKING         | int    | Place on leaderboard                                   |
| VALUE           | float  | Value of volume, unrealized profit, or realized profit |
| TWITTER\_HANDLE | string | Shows the user's Twitter handle (if available)         |

**Ratelimit**: 90 req/min

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
    "/rankings/{Key}:{Time_Frame}:{Symbol}/{Section}": {
      "get": {
        "summary": "Leaderboards",
        "description": "The leaderboards endpoint allows you to retrieve leaderboard standings for unrealized profit (period delta), unrealized profit (inception), volume, and realized profit.",
        "operationId": "rest-public-rankings",
        "parameters": [
          {
            "name": "Key",
            "in": "path",
            "description": "Allowed values: \"plu_diff\" for unrealized profit (period delta); \"plu\" for unrealized profit (inception); \"vol\" for volume; \"plr\" for realized profit",
            "required": true,
            "schema": {
              "type": "string",
              "default": "vol"
            }
          },
          {
            "name": "Time_Frame",
            "in": "path",
            "description": "Available values: \"3h\", \"1w\", \"1M\" - see table below for available time frames per key",
            "required": true,
            "schema": {
              "type": "string",
              "default": "3h"
            }
          },
          {
            "name": "Symbol",
            "in": "path",
            "description": "The symbol you want information about. (e.g. tBTCUSD, tETHUSD, tGLOBAL:USD) - see table below for available symbols per key",
            "required": true,
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
            }
          },
          {
            "name": "Section",
            "in": "path",
            "description": "Available values: \"hist\"",
            "required": true,
            "schema": {
              "type": "string",
              "default": "hist"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "if = 1 it sorts results returned with old > new",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": -1
            }
          },
          {
            "name": "start",
            "in": "query",
            "description": "Millisecond start time",
            "schema": {
              "type": "integer",
              "format": "int64",
              "default": null
            }
          },
          {
            "name": "end",
            "in": "query",
            "description": "Millisecond end time",
            "schema": {
              "type": "integer",
              "format": "int64",
              "default": null
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of records (Max: 10000)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "120"
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
                    "value": "[[ \n  MTS,\n  PLACEHOLDER,\n  USERNAME,\n  RANKING,\n  PLACEHOLDER,\n  PLACEHOLDER,\n  VALUE,\n  PLACEHOLDER\n  PLACEHOLDER\n  TWITTER_HANDLE\n],\n [\n  ...\n ]\n]\n\n\n//unrealized profit (period delta)\n[[1575201600000,null,\"USERNAME\",1,null,null,15504971.51,null,0,\"TWITTER_HANDLE\"]\n\n//unrealized profit (inception)\n[[1574640000000,null,\"USERNAME\",1,null,null,4134739.62,null,0,\"TWITTER_HANDLE\"]]\n \n//realized profit\n[[1574640000000,null,\"USERNAME\",1,null,null,156129.59,null,0,\"TWITTER_HANDLE\"]]\n \n//vol\n[[1575190800000,null,\"USERNAME\",1,null,null,442.03,null,0,\"TWITTER_HANDLE\"]]\n"
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
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "\"use strict\"\n\nconst axios = require('axios')\n\nconst baseUrl = \"https://api-pub.bitfinex.com/v2/\";\nconst pathParams = \"rankings/vol:3h:tBTCUSD/hist\"\nconst queryParams = \"\"\n\naxios.get(`${baseUrl}/${pathParams}?${queryParams}`)\n    .then(response => {\n        console.log(response.data);\n    }, error => {\n        console.log(error);\n    })"
            },
            {
              "language": "text",
              "code": "\n\n-Unrealized profit (period delta)\n\ncurl https://api-pub.bitfinex.com/v2/rankings/plu_diff:1w:tGLOBAL:USD/hist\n\n-Unrealized profit (inception)\n\ncurl https://api-pub.bitfinex.com/v2/rankings/plu:1w:tGLOBAL:USD/hist\ncurl https://api-pub.bitfinex.com/v2/rankings/plu:3h:tBTCUSD/hist\n\n-Volume\n\ncurl https://api-pub.bitfinex.com/v2/rankings/vol:3h:tBTCUSD/hist\ncurl https://api-pub.bitfinex.com/v2/rankings/vol:3h:tGLOBAL:USD/hist\n\n-Realized Profit\n\ncurl https://api-pub.bitfinex.com/v2/rankings/plr:1M:tGLOBAL:USD/hist",
              "name": "cURL"
            }
          ],
          "samples-languages": [
            "javascript",
            "text"
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
