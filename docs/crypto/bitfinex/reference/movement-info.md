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
source_url: 'https://docs.bitfinex.com/reference/movement-info'
updated_at: 2026-11-26
---

# Movement info

Detailed information about the deposit/withdrawal

#### Response data

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
    <tr><td>[0]</td><td>ID</td><td>Integer</td><td>Movement identifier</td></tr>
    <tr><td>[1]</td><td>CURRENCY</td><td>String</td><td>The symbol of the currency (ex. "BTC")</td></tr>
    <tr><td>[2]</td><td>CURRENCY_METHOD</td><td>String</td><td>The extended name of the currency (ex. "BITCOIN") or WIRE for fiat</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[4]</td><td>REMARK</td><td>String</td><td>Remarks related to movement</td></tr>
    <tr><td>[5]</td><td>MTS_STARTED</td><td>Integer</td><td>Movement started at</td></tr>
    <tr><td>[6]</td><td>MTS_UPDATED</td><td>Integer</td><td>Movement last updated at</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[9]</td><td>STATUS</td><td>String</td><td>Current status</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[12]</td><td>AMOUNT</td><td>Float</td><td>Amount of funds moved (positive for deposits, negative for withdrawals)</td></tr>
    <tr><td>[13]</td><td>FEES</td><td>Float</td><td>Tx Fees applied</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[16]</td><td>DESTINATION_ADDRESS</td><td>String</td><td>Destination address</td></tr>
    <tr><td>[17]</td><td>MEMO</td><td>String</td><td>Memo/Tag related to transaction</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[20]</td><td>TRANSACTION_ID</td><td>String</td><td>Transaction identifier</td></tr>
    <tr><td>[21]</td><td>MOVEMENT_NOTE</td><td>String</td><td>Optional personal transaction note</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[24]</td><td>BANK_FEES</td><td>Float</td><td>Wire bank fees</td></tr>
    <tr><td>[25]</td><td>BANK_ROUTER_ID</td><td>Integer</td><td>Identifier of bank router</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[28]</td><td>EXTERNAL_BANK_MOV_ID</td><td>String</td><td>External provider movement id</td></tr>
    <tr><td>[29]</td><td>EXTERNAL_BANK_MOV_STATUS</td><td>String</td><td>External provider movement status</td></tr>
    <tr><td>[30]</td><td>EXTERNAL_BANK_MOV_DESCRIPTION</td><td>String</td><td>External provider movement info</td></tr>
    <tr><td>[31]</td><td>EXTERNAL_BANK_ACC_INFO</td><td>Object</td><td>External provider bank account information for user</td></tr>
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
    "/auth/r/movements/info": {
      "post": {
        "summary": "Movement info",
        "description": "Detailed information about the deposit/withdrawal",
        "operationId": "movement-info",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id"
                ],
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "deposit/withdrawal ids",
                    "format": "int32"
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
                    "value": "[\n  24, //ID\n  \"EUR\", //CURRENCY\n  \"WIRE\", //CURRENCY_METHOD\n  null, //PLACEHOLDER\n  \"remark related to bank details\", //REMARK\n  1677086074000, //MTS_STARTED\n  1677086210000, //MTS_UPDATED\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"COMPLETED\", //STATUS\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  -29.5, //AMOUNT\n  -0.5, //FEES\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //DESTINATION_ADDRESS\n  null, //MEMO\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //TRANSACTION_ID\n  \"testing note\", //MOVEMENT_NOTE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  0, //BANK_FEES\n  123, //BANK_ROUTER_ID\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"abcd-1234\", //EXTERNAL_BANK_MOVE_ID\n  \"COMPLETED\", //EXTERNAL_BANK_MOV_STATUS\n  \"finished withdrawal in platform\", //EXTERNAL_BANK_MOV_DESCRIPTION\n  {\"router\":\"my-router\",\"meta\":{\"foo\":\"bar\"}} //EXTERNAL_BANK_ACC_INFO\n]"
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
