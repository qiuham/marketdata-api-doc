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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-trades-by-symbol'
updated_at: 2026-11-22
---

# Trades (by symbol)

Retrieve your trades by trading pair symbol (e.g. tBTCUSD, tLTCUSD, ...). Your most recent trades will be retrieved by default, but a timestamp can be used to retrieve time-specific data.

### Response Fields

| Index | Field         | Type   | Description                             |
| ----- | :------------ | ------ | --------------------------------------- |
| \[0]  | ID            | int    | Trade database id                       |
| \[1]  | SYMBOL        | string | Symbol (BTCUSD, …)                      |
| \[2]  | MTS           | int    | Execution timestamp                     |
| \[3]  | ORDER\_ID     | int    | Order id                                |
| \[4]  | EXEC\_AMOUNT  | float  | Positive means buy, negative means sell |
| \[5]  | EXEC\_PRICE   | float  | Execution price                         |
| \[6]  | ORDER\_TYPE   | string | Order type                              |
| \[7]  | ORDER\_PRICE  | float  | Order price                             |
| \[8]  | MAKER         | int    | 1 if true, -1 if false                  |
| \[9]  | FEE           | float  | Fee                                     |
| \[10] | FEE\_CURRENCY | string | Fee currency                            |
| \[11] | CID           | int    | Client Order ID                         |

> 🚧 Order type
>
> For trades older than March 2020, the ORDER\_TYPE field will not be set.

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">90 reqs/min (requests per minute)</td>
  </tr>
</table>
`}</HTMLBlock>

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings-auth",
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
    "/auth/r/trades/{symbol}/hist": {
      "post": {
        "summary": "Trades (by symbol)",
        "description": "Retrieve your trades by trading pair symbol (e.g. tBTCUSD, tLTCUSD, ...). Your most recent trades will be retrieved by default, but a timestamp can be used to retrieve time-specific data.",
        "operationId": "rest-auth-trades-by-symbol",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "description": "The symbol for which to retrieve trade history (e.g. tBTCUSD, tETHUSD, ...).",
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
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
                  "start": {
                    "type": "integer",
                    "description": "If start is given, only records with MTS >= start (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "description": "If start is given, only records with MTS <= end (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records in response (max. 10000).",
                    "format": "int32",
                    "default": "25"
                  },
                  "sort": {
                    "type": "integer",
                    "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
                    "format": "int32",
                    "default": "-1"
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
                    "value": "[\n  [\n  \t402088407, //ID\n  \t\"tETHUST\", //SYMBOL\n  \t1574963975602, //MTS\n    34938060782, //ORDER_ID\n  \t-0.2, //EXEC_AMOUNT\n  \t153.57, //EXEC_PRICE\n  \t\"MARKET\", //ORDER_TYPE\n  \t0, //ORDER_PRICE\n  \t-1, //MAKER\n  \t-0.061668, //FEE\n  \t\"USD\", //FEE_CURRENCY\n  \t1234 //CID\n\t],\n  [...]\n]"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": false,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
