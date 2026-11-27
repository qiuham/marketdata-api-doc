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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-offers-hist'
updated_at: 2026-11-27
---

# Funding Offers History

Get past inactive funding offers.

#### Response data

| Index    | Field                 | Type                                                                 | Description                                                                     |
| :------- | :-------------------- | :------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| \[0...n] | FUNDING\_OFFER\_ARRAY | [Funding offer array](#funding-offers-history-entry-arrays-index-0n) | Each index contains one of the n\` current user's funding offer history entries |

#### Funding offers history entry arrays (Index \[0...n])

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
      <td>Int</td>
      <td>Offer ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>SYMBOL</td>
      <td>String</td>
      <td>The currency of the offer (fUSD, etc)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MTS_CREATED</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the offer was created</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>MTS_UPDATED</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the offer was updated</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Amount the offer is for</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT_ORIG</td>
      <td>Float</td>
      <td>Amount the offer was entered with originally</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>Offer type ('LIMIT')</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>FLAGS</td>
      <td>Object</td>
      <td>Future params object (stay tuned)</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>STATUS</td>
      <td>String</td>
      <td>Offer Status: EXECUTED, CANCELED</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[14]</td>
      <td>RATE</td>
      <td>Float</td>
      <td>Rate of the offer (percentage expressed as decimal number i.e. 1% = 0.01)</td>
    </tr>
    <tr>
      <td>[15]</td>
      <td>PERIOD</td>
      <td>Int</td>
      <td>Period of the offer</td>
    </tr>
    <tr>
      <td>[16]</td>
      <td>NOTIFY</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>HIDDEN</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>RENEW</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
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
    "/auth/r/funding/offers/{Symbol}/hist": {
      "post": {
        "summary": "Funding Offers History",
        "description": "Get past inactive funding offers.",
        "operationId": "rest-auth-funding-offers-hist",
        "parameters": [
          {
            "name": "Symbol",
            "in": "path",
            "description": "Symbol (fUSD, ...) , Omit for all symbols (see example)",
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
                    "description": "Number of records (Max 500)",
                    "default": "50",
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
                    "value": "[\n    [\n    653170899, //ID\n    \"fUSD\", //SYMBOL\n    1574072620000, //MTS_CREATED\n    1574072620000, //MTS_UPDATED\n    0, //AMOUNT\n    -57.9, //AMOUNT_ORIG\n    null, //TYPE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //FLAGS\n    \"EXECUTED at 0.0368% (57.9)\", //STATUS\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.000369, //RATE\n    2, //PERIOD\n    0, //NOTIFY\n    0, //HIDDEN\n    null, //PLACEHOLDER\n    null, //RENEW\n    null //PLACEHOLDER\n  \t], //FUNDING_OFFER_ARRAY\n  \t...\n]"
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
