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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-wallets'
updated_at: 2026-11-18
---

# Wallets

Returns an array of all the current user's wallets.

### Response data

| Index    | Field  | Type                     | Description                                                |
| :------- | :----- | :----------------------- | :--------------------------------------------------------- |
| \[0...n] | WALLET | [Wallet](#wallet-arrays) | Each index contains one of the `n` current user's wallets. |

#### Wallet arrays

| Index | Field                  | Type   | Description                                             |
| ----- | ---------------------- | ------ | ------------------------------------------------------- |
| \[0]  | TYPE                   | string | Wallet name (exchange, margin, funding)                 |
| \[1]  | CURRENCY               | string | Currency (e.g. USD, BTC, ETH, ...)                      |
| \[2]  | BALANCE                | float  | Balance                                                 |
| \[3]  | UNSETTLED\_INTEREST    | float  | Unsettled interest                                      |
| \[4]  | AVAILABLE\_BALANCE     | float  | Wallet balance available for orders/withdrawal/transfer |
| \[5]  | LAST\_CHANGE           | string | Description of the last ledger entry                    |
| \[6]  | LAST\_CHANGE\_METADATA | JSON   | Optional object with details                            |

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
    "/auth/r/wallets": {
      "post": {
        "summary": "Wallets",
        "description": "Returns an array of all the current user's wallets.",
        "operationId": "rest-auth-wallets",
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
                    "value": "[\n  [\n  \t\"exchange\", //TYPE\n  \t\"UST\", //CURRENCY\n  \t19788.6529257, //BALANCE\n  \t0, //UNSETTLED_INTEREST\n  \t19788.6529257, //AVAILABLE_BALANCE\n  \t\"Exchange 2.0 UST for USD @ 11.696\", //LAST_CHANGE\n  \t{\n  \t\treason: \"TRADE\",\n  \t\torder_id: 1189740779,\n  \t\torder_id_oppo: 1189785673,\n  \t\ttrade_price: \"11.696\",\n  \t\ttrade_amount: \"-2.0\",\n  \t\torder_cid: 1598516362757,\n  \t\torder_gid: 1598516362629\n  \t} //TRADE_DETAILS\n  ], //WALLET\n  [...]\n]"
                  }
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
