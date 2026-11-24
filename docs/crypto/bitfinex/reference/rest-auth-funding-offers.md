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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-offers'
updated_at: 2026-11-24
---

# Active Funding Offers

Get active funding offers. A path param can be used to retrieve offers in a particular currency. All offers are returned if no currency is specified.

#### Response data

| Index    | Field                 | Type                                                                | Description                                                                    |
| :------- | :-------------------- | :------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| \[0...n] | FUNDING\_OFFER\_ARRAY | [Funding offer array](#active-funding-offers-entry-arrays-index-0n) | Each index contains one of the n\` current user's active funding offer entries |

#### Active funding offers entry arrays (index \[0...n]

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
      <td>Integer</td>
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
      <td>Amount of the offer</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT_ORIG</td>
      <td>Float</td>
      <td>Amount of the offer when it was first created</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>"LIMIT, ..."</td>
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
      <td>Offer Status: ACTIVE, PARTIALLY FILLED</td>
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
      <td>null if false, 1 if true</td>
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
    background-color: #ebebeb
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
    "/auth/r/funding/offers/{Symbol}": {
      "post": {
        "summary": "Active Funding Offers",
        "description": "Get active funding offers. A path param can be used to retrieve offers in a particular currency. All offers are returned if no currency is specified.",
        "operationId": "rest-auth-funding-offers",
        "parameters": [
          {
            "name": "Symbol",
            "in": "path",
            "description": "Symbol (fUSD, ...) (Can be omitted to return funding offers for all currencies)",
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
                    "value": "[\n  [\n    652606505, //ID\n    \"fETH\", //SYMBOL\n    1574000611000, //MTS_CREATED\n    1574000611000, //MTS_UPDATED\n    0.29797676, //AMOUNT\n    0.29797676, //AMOUNT_ORIG\n    \"LIMIT\", //TYPE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0, //FLAGS\n    \"ACTIVE\", //STATUS\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.0002, //RATE\n    2, //PERIOD\n    0, //NOTIFY\n    null, //HIDDEN\n    null, //PLACEHOLDER\n    0, //RENEW\n    null //PLACEHOLDER\n  ],\n  ...\n]"
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
