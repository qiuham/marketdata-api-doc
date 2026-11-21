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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-ledgers'
updated_at: 2026-11-21
---

# Ledgers

View your past ledger entries. Most recent entries are returned by default, but a timestamp can be used to retrieve time-specific data.

The endpoint returns data up to 6 years old.

> 🚧 Retrieve all ledgers
>
> The currency param can be omitted to return a ledger including all currencies. The path for this call is 'v2/auth/r/ledgers/hist'.

### Response data

| Index    | Field         | Type                                 | Description                                                       |
| :------- | :------------ | :----------------------------------- | :---------------------------------------------------------------- |
| \[0...n] | LEDGER\_ENTRY | [Ledger entry](#ledger-entry-arrays) | Each index contains one of the `n` current user's ledger entries. |

#### Ledger entry arrays

| Index | Field       | Type             | Description                                                                                        |
| :---- | :---------- | :--------------- | :------------------------------------------------------------------------------------------------- |
| \[0]  | ID          | int              | Ledger identifier                                                                                  |
| \[1]  | CURRENCY    | string           | The symbol of the currency (e.g. "BTC")                                                            |
| \[2]  | WALLET      | string (or null) | Returns the relevant wallet for the ledger entry ('exchange', 'margin', 'funding', 'contribution') |
| \[3]  | MTS         | int              | Timestamp in milliseconds                                                                          |
| \[5]  | AMOUNT      | float            | Amount changed                                                                                     |
| \[6]  | BALANCE     | float            | Balance after change                                                                               |
| \[8]  | DESCRIPTION | string           | Description of ledger transaction                                                                  |

#### Possible values for the 'category' filter

This table shows the possible values for the 'category' body param. The table shows the filter followed by the int value that should be entered in the 'category' param to activate the filter.

| Filter                                    | Int Value | Filter                        | Int Value | Filter                                | Int Value |
| :---------------------------------------- | :-------- | :---------------------------- | :-------- | :------------------------------------ | :-------- |
| exchange                                  | 5         | canceled withdrawal           | 105       | withdrawal fee                        | 254       |
| position modified, closed, or liquidated  | 22        | trading fee                   | 201       | withdrawal express fee                | 255       |
| position claim                            | 23        | trading rebate                | 202       | miner fee                             | 258       |
| position transfer                         | 25        | hidden order fee              | 204       | staking payment                       | 262       |
| position swap                             | 26        | otc trade fee                 | 207       | adjustment                            | 401       |
| position funding cost or interest charged | 27        | swap fee                      | 222       | expense                               | 501       |
| margin / swap / interest payment          | 28        | claiming fee                  | 224       | currency conversion / computation fee | 905       |
| derivatives funding event                 | 29        | used margin funding charge    | 226       | monthly profit payment                | 907       |
| settlement                                | 31        | unused margin funding fee     | 228       | losses                                | 911       |
| transfer                                  | 51        | earned fee / affiliate rebate | 241       |                                       |           |
| deposit                                   | 101       | ETHFX loyalty fee             | 243       |                                       |           |
| withdrawal                                | 104       | deposit fee                   | 251       |                                       |           |

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
    "/auth/r/ledgers/{Currency}/hist": {
      "post": {
        "summary": "Ledgers",
        "description": "View your past ledger entries. Most recent entries are returned by default, but a timestamp can be used to retrieve time-specific data.\n\nThe endpoint returns data up to 6 years old.",
        "operationId": "rest-auth-ledgers",
        "parameters": [
          {
            "name": "Currency",
            "in": "path",
            "description": "Currency (BTC, ...) For an up-to-date listing of supported currencies see: https://api.bitfinex.com/v2/conf/pub:map:currency:label (Can be omitted to retrieve Ledgers for all currencies)",
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
                  "category": {
                    "type": "integer",
                    "description": "Allows you to filter the ledger response using an int value. For a list of possible values, see the table below.",
                    "format": "int32"
                  },
                  "start": {
                    "type": "integer",
                    "description": "Millisecond start time",
                    "format": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "description": "Millisecond end time",
                    "format": "int64"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records (Max 2500)",
                    "format": "int32"
                  },
                  "wallet": {
                    "type": "string",
                    "description": "Wallet name e.g. exchange, margin, funding"
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
                    "value": " [\n  [\n  2531822314, //ID\n  \"USD\", //CURRENCY\n  \"margin\", //WALLET\n  1573521810000, //MTS\n  null, //PLACEHOLDER\n  0.01644445, //AMOUNT\n  0, //BALANCE\n  null, //PLACEHOLDER\n  \"Settlement @ 185.79 on wallet margin\" //DESCRIPTION\n\t], //LEDGER_ENTRY\n  [...]\n]"
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
