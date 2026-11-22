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
source_url: 'https://docs.bitfinex.com/reference/rest-public-candles'
updated_at: 2026-11-22
---

# Candles

The Candles endpoint provides OCHL (Open, Close, High, Low) and volume data for the specified funding currency or trading pair. The endpoint provides the last 100 candles by default, but a limit and a start and/or end timestamp can be specified.

### Response Fields

| Index | Field  | Type  | Description                                    |
| ----- | ------ | ----- | ---------------------------------------------- |
| \[0]  | MTS    | int   | Millisecond epoch timestamp                    |
| \[1]  | OPEN   | float | First execution during the time frame          |
| \[2]  | CLOSE  | float | Last execution during the time frame           |
| \[3]  | HIGH   | float | Highest execution during the time frame        |
| \[4]  | LOW    | float | Lowest execution during the timeframe          |
| \[5]  | VOLUME | float | Quantity of symbol traded within the timeframe |

### Available candles

#### Trading pair candles

| Key   | Time frame       | Trading pair                   | Example          |
| ----- | ---------------- | ------------------------------ | ---------------- |
| trade | 1m, 5m, 15m, ... | tBTCUSD, tLTCUSD, tETHUSD, ... | trade:1m:tBTCUSD |

#### Funding currency candles

| Key   | Time frame       | Funding currency      | Period   | Example           |
| ----- | ---------------- | --------------------- | -------- | ----------------- |
| trade | 1m, 5m, 15m, ... | fUSD, fBTC, fETH, ... | :pPERIOD | trade:1m:fUSD:p30 |

#### Aggregate funding currency candles

| Key   | Time frame | Funding currency | Aggregation \[10, 30] | Period        | Example                  |
| ----- | ---------- | ---------------- | --------------------- | ------------- | ------------------------ |
| trade | 1m, ...    | fUSD, ...        | :aAGGR                | :pSTART:p:END | trade:1m:fUSD:a10:p2:p10 |

> 📘 Time frame available values
>
> Available values: "1m", "5m", "15m", "30m", "1h", "3h", "6h", "12h", "1D", "1W", "14D", "1M".

> 🚧 Funding Candles
>
> Be sure to specify a period or aggregated period when retrieving funding candles. If you wish to mimic the candles found in the UI, use the following setup to aggregate all funding candles: a30:p2:p30.\
> Example: <https://api-pub.bitfinex.com/v2/candles/trade:1h:fUSD:a30:p2:p30/hist>.

<Callout icon="🚧" theme="warn">
  Specifying either "hist" or "last" section is mandatory for all keys.
</Callout>

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">30 reqs/min (requests per minute)</td>
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
    "/candles/{candle}/{section}": {
      "get": {
        "summary": "Candles",
        "description": "The Candles endpoint provides OCHL (Open, Close, High, Low) and volume data for the specified funding currency or trading pair. The endpoint provides the last 100 candles by default, but a limit and a start and/or end timestamp can be specified.",
        "operationId": "rest-public-candles",
        "parameters": [
          {
            "name": "candle",
            "in": "path",
            "description": "Check [Available candles](https://docs.bitfinex.com/reference/rest-public-candles#available-candles) table to understand how to compose this argument.",
            "schema": {
              "type": "string",
              "default": "trade:1m:tBTCUSD"
            },
            "required": true
          },
          {
            "name": "section",
            "in": "path",
            "description": "Available values: \"last\", \"hist\".",
            "required": true,
            "schema": {
              "type": "string",
              "default": "hist"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "-1"
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
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "// Response with section=\"last\"\n[ \n  1678465320000, //MTS \n  20097, //OPEN\n  20094, //CLOSE\n  20097, //HIGH\n  20094, //LOW\n  0.07870586 //VOLUME\n]\n\n// Response with section=\"hist\"\n[\n  [\n   \t1678465320000, //MTS \n    20097, //OPEN\n    20114, //CLOSE\n    20125, //HIGH\n    20094, //LOW\n    1.43504645 //VOLUME\n  ], \n  [...]\n]"
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
