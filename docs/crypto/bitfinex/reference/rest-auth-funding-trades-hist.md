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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-trades-hist'
updated_at: 2026-11-26
---

# Funding Trades

Get funding trades for offered funding. Can be used to request funding trades for a specific currency or to retrieve trades for all currencies at once.

#### Response data

| Index    | Field                 | Type                                                  | Description                                                               |
| :------- | :-------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------ |
| \[0...n] | FUNDING\_TRADE\_ARRAY | [Funding trade array](#funding-trade-arrays-index-0n) | Each index contains one of the n\` current user's funding trades entries. |

#### Funding trade arrays (Index \[0...n])

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
      <td>Funding trade ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>CURRENCY</td>
      <td>String</td>
      <td>The currency of the offer (fUSD, etc)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MTS_CREATE</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the offer was created</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>OFFER_ID</td>
      <td>Int</td>
      <td>Funding offer ID</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Amount the offer is for</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>RATE</td>
      <td>Float</td>
      <td>Rate of the offer (percentage expressed as decimal number i.e. 1% = 0.01)</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>PERIOD</td>
      <td>Int</td>
      <td>Period of the offer</td>
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
    "/auth/r/funding/trades/{Symbol}/hist": {
      "post": {
        "summary": "Funding Trades",
        "description": "Get funding trades for offered funding. Can be used to request funding trades for a specific currency or to retrieve trades for all currencies at once.",
        "operationId": "rest-auth-funding-trades-hist",
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
                    "description": "Number of records (Max 10000)",
                    "format": "int32",
                    "default": "25"
                  },
                  "sort": {
                    "type": "integer",
                    "format": "int32",
                    "default": "-1",
                    "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field)."
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
                    "value": "[\n  [\n  636040, //ID\n  \"fUST\", //CURRENCY\n  1574077528000, //MTS_CREATE\n  41237922, //OFFER_ID\n  -100, //AMOUNT\n  0.0024, //RATE\n  2, //PERIOD\n  null //PLACECHOLDER\n\t], //FUNDING_TRADE_ARRAY\n  ...\n]\n"
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
