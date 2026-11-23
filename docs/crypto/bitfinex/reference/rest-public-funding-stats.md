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
source_url: 'https://docs.bitfinex.com/reference/rest-public-funding-stats'
updated_at: 2026-11-23
---

# Funding Statistics

Get a list of the most recent funding data for the given currency: FRR, average period, total amount provided, total amount used

### Response Fields

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
      <td>MTS</td>
      <td>int</td>
      <td>Milliseconds epoch timestamp</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[3]</td>
      <td>FRR</td>
      <td>float</td>
      <td>
        1/365th of Flash Return Rate (To get the daily rate, use: <b>rate x 365</b>.
          To get the daily rate as percentage use: <b>rate x 365 x 100</b>. 
          To get APR as percentage use <b>rate x 100 x 365 x 365</b>.)
      </td>
    </tr>
    
    <tr>
      <td>[4]</td>
      <td>AVG_PERIOD</td>
      <td>float</td>
      <td>Average period for funding provided</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[7]</td>
      <td>FUNDING_AMOUNT</td>
      <td>float</td>
      <td>Total funding provided</td>
    </tr>
    
    <tr>
      <td>[8]</td>
      <td>FUNDING_AMOUNT_USED</td>
      <td>float</td>
      <td>Total funding provided that is used in positions</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[11]</td>
      <td>FUNDING_BELOW_THRESHOLD</td>
      <td>float</td>
      <td>Sum of open funding offers &#60; 0.75%</td>
    </tr>
  </tbody>
</table>

<style>
  b {
    font-weight: 600
  }
  
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
    "/funding/stats/{symbol}/hist": {
      "get": {
        "summary": "Funding Statistics",
        "description": "Get a list of the most recent funding data for the given currency: FRR, average period, total amount provided, total amount used",
        "operationId": "rest-public-funding-stats",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "description": "The symbol you want information about. (e.g. fUSD, fBTC, fETH, ...)",
            "schema": {
              "type": "string",
              "default": "fUSD"
            },
            "required": true
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
            "description": "Number of records in response (max. 250).",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                    "value": "[\n  [\n    1678467900000, //MTS\n    null,\n    null,\n    0.00000187, //FRR\n    68.88, //AVG_PERIOD\n    null,\n    null,\n    3230660371.4429536, //FUNDING_AMOUNT\n    2988430006.4623938, //FUNDING_AMOUNT_USED\n    null,\n    null,\n    1447938775.5708046 //FUNDING_BELOW_THRESHOLD\n  ],\n  [...]\n]"
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "\"use strict\"\n\nconst axios = require('axios')\n\nconst baseUrl = \"https://api-pub.bitfinex.com/v2/\";\nconst pathParams = \"funding/stats/fBTC/hist\"\nconst queryParams = \"limit=5\"\n\naxios.get(`${baseUrl}/${pathParams}?${queryParams}`)\n    .then(response => {\n        console.log(response.data);\n    }, error => {\n        console.log(error);\n    })\n"
            },
            {
              "language": "curl",
              "code": "curl https://api-pub.bitfinex.com/v2/funding/stats/fUSD/hist"
            }
          ],
          "samples-languages": [
            "javascript",
            "curl"
          ]
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
