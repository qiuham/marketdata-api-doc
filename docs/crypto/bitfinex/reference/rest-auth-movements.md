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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-movements'
updated_at: 2026-11-25
---

# Movements

View your past deposits/withdrawals. Currency can be specified to retrieve movements specific to that currency.

#### Response data

| Index    | Field           | Type                                        | Description                                                          |
| :------- | :-------------- | :------------------------------------------ | :------------------------------------------------------------------- |
| \[0...n] | MOVEMENT\_ARRAY | [Movement array](#movement-arrays-index-0n) | Each index contains one of the n\` current user's movements entries. |

#### Movement arrays (Index \[0...n])

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[0]</td>
      <td>ID</td>
      <td>String</td>
      <td>Movement identifier</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>CURRENCY</td>
      <td>String</td>
      <td>The symbol of the currency (ex. "BTC")</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>CURRENCY_NAME</td>
      <td>String</td>
      <td>The extended name of the currency (ex. "BITCOIN")</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>MTS_STARTED</td>
      <td>Int</td>
      <td>Movement started at</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>MTS_UPDATED</td>
      <td>Int</td>
      <td>Movement last updated at</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>STATUS</td>
      <td>String</td>
      <td>Current status</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>AMOUNT</td>
      <td>String</td>
      <td>Amount of funds moved (positive for deposits, negative for withdrawals)</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>FEES</td>
      <td>String</td>
      <td>Tx Fees applied</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[16]</td>
      <td>DESTINATION_ADDRESS</td>
      <td>String</td>
      <td>Destination address</td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>PAYMENT_ID</td>
      <td>String</td>
      <td>Payment ID (if relevant)</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[20]</td>
      <td>TRANSACTION_ID</td>
      <td>String</td>
      <td>Transaction identifier</td>
    </tr>
    <tr>
      <td>[21]</td>
      <td>WITHDRAW_TRANSACTION_NOTE</td>
      <td>String</td>
      <td>Optional personal withdraw transaction note</td>
    </tr>
  </tbody>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb;
  }
  
  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

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
    "/auth/r/movements/{Currency}/hist": {
      "post": {
        "summary": "Movements",
        "description": "View your past deposits/withdrawals. Currency can be specified to retrieve movements specific to that currency.",
        "operationId": "rest-auth-movements",
        "parameters": [
          {
            "name": "Currency",
            "in": "path",
            "description": "Currency (BTC, ...). For an up-to-date listing of supported currencies see: https://api.bitfinex.com/v2/conf/pub:map:currency:label - Currency param can be omitted to retrieve recent movements for all currencies.",
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
                  "start": {
                    "type": "integer",
                    "description": "Millisecond start time, only records with MTS_UPDATED >= start (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "description": "Millisecond end time, only records with MTS_UPDATED <= end (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records (Max 1000)",
                    "format": "int32",
                    "default": "25"
                  },
                  "id": {
                    "type": "array",
                    "description": "Optional array of deposit/withdrawal ids",
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "address": {
                    "type": "string",
                    "description": "Optional deposit address filter"
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
                    "value": "//Deposit\n[\n  [\n  13105603, //ID\n  'ETH', //CURRENCY\n  'ETHEREUM', //CURRENCY_NAME\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  1569348774000, //MTS_STARTED\n  1569348774000, //MTS_UPDATED\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  'COMPLETED', //STATUS\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  '0.26300954', //AMOUNT\n  '-0.00135', //FEES\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  'DESTINATION_ADDRESS', //DESTINATION_ADDRESS\n  null, //PAYMENT_ID\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  'TRANSACTION_ID', //TRANSACTION_ID\n  null //WITHDRAW_TRANSACTION_NOTE\n\t],\n  ...\n]  \n  \n//Withdrawal  \n[\n  [\n    13293039, //ID\n    'ETH', //CURRENCY\n    'ETHEREUM', //CURRENCY_NAME\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    1574175052000, //MTS_STARTED\n    1574181326000, //MTS_UPDATED\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    'CANCELED', //STATUS\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    '-0.24', //AMOUNT\n    '-0.00135', //FEES\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    'DESTINATION_ADDRESS', //DESTINATION_ADDRESS\n    null, //PAYMENT_ID\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    'TRANSACTION_ID',\"Purchase of 100 pizzas\" //WITHDRAW_TRANSACTION_NOTE\n  ],\n  ...\n]\n "
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
