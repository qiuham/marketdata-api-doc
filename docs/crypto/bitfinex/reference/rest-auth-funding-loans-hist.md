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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-loans-hist'
updated_at: 2026-11-20
---

# Funding Loans History

Inactive funds not used in positions.
Limited to last 3 days.

#### Response data

| Index    | Field                | Type                                                | Description                                                             |
| :------- | :------------------- | :-------------------------------------------------- | :---------------------------------------------------------------------- |
| \[0...n] | FUNDING\_LOAN\_ARRAY | [Funding loan array](#funding-loan-arrays-index-0n) | Each index contains one of the n\` current user's funding loans entries |

#### Funding loan arrays (Index \[0...n])

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
      <td>Loan ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>SYMBOL</td>
      <td>String</td>
      <td>The currency of the loan (fUSD, etc)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>SIDE</td>
      <td>Int</td>
      <td>1 if you are the lender, 0 if you are both the lender and borrower, -1 if you're the borrower</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>MTS_CREATE</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the loan was created</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>MTS_UPDATE</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the loan was updated</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Amount of funds provided</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>FLAGS</td>
      <td>Object</td>
      <td>Future params object (stay tuned)</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>STATUS</td>
      <td>String</td>
      <td>Loan Status: ACTIVE</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>RATE_TYPE</td>
      <td>String</td>
      <td>"FIXED" or "VAR" (for FRR)</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[11]</td>
      <td>RATE</td>
      <td>Float</td>
      <td>Rate of the loan (percentage expressed as decimal number i.e. 1% = 0.01)</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>PERIOD</td>
      <td>Int</td>
      <td>Period of the loan</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>MTS_OPENING</td>
      <td>Int</td>
      <td>Millisecond Time Stamp for when the loan was opened</td>
    </tr>
    <tr>
      <td>[14]</td>
      <td>MTS_LAST_PAYOUT</td>
      <td>Int</td>
      <td>Millisecond Time Stamp for when the last payout was made</td>
    </tr>
    <tr>
      <td>[15]</td>
      <td>NOTIFY</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
    <tr>
      <td>[16]</td>
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
      <td>[18]</td>
      <td>RENEW</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
        <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[20]</td>
      <td>NO_CLOSE</td>
      <td>Int</td>
      <td>If funding will be returned when position is closed. 0 if false, 1 if true</td>
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
    "/auth/r/funding/loans/{Symbol}/hist": {
      "post": {
        "summary": "Funding Loans History",
        "description": "Inactive funds not used in positions.\nLimited to last 3 days.",
        "operationId": "rest-auth-funding-loans-hist",
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
                    "format": "int32"
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
                    "value": "    \n[\n    [\n    3027653, //ID\n    'fUST', //SYMBOL\n    -1, //SIDE\n    1702649922000, //MTS_CREATE \n    1702649922000, //MTS_UPDATE\n    402.10731456, //AMOUNT\n    null, //FLAGS\n    'CLOSED', //STATUS\n    null, //RATE_TYPE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0, //RATE\n    2, //PERIOD\n    1702649922000, //MTS_OPENING\n    1702649958000, //MTS_LAST_PAYOUT\n    null, //NOTIFY\n    0, //HIDDEN\n    null, //PLACEHOLDER\n    0, //RENEW\n    null, //PLACEHOLDER\n    0 //NO_CLOSE\n  \t]\n]\n\n"
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
