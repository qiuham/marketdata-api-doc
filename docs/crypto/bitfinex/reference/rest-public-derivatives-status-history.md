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
source_url: 'https://docs.bitfinex.com/reference/rest-public-derivatives-status-history'
updated_at: 2026-11-21
---

# Derivatives Status History

Endpoint used to receive different types of historical platform information - currently supports derivatives pair status only.

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
      <td>Millisecond epoch timestamp</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[2]</td>
      <td>DERIV_PRICE</td>
      <td>float</td>
      <td>Derivative book mid price</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>SPOT_PRICE</td>
      <td>float</td>
      <td>Book mid price of the underlying Bitfinex spot trading pair</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[5]</td>
      <td>INSURANCE_FUND_BALANCE</td>
      <td>float</td>
      <td>The balance available to the liquidation engine to absorb losses</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[7]</td>
      <td>NEXT_FUNDING_EVT_MTS</td>
      <td>int</td>
      <td>Millisecond timestamp of next funding event</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>NEXT_FUNDING_ACCRUED</td>
      <td>float</td>
      <td>Current accrued funding for next 8h period</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>NEXT_FUNDING_STEP</td>
      <td>int</td>
      <td>Incremental accrual counter</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[11]</td>
      <td>CURRENT_FUNDING</td>
      <td>float</td>
      <td>Funding applied in the current 8h period</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[14]</td>
      <td>MARK_PRICE</td>
      <td>float</td>
      <td>Price based on the BFX Composite Index</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[17]</td>
      <td>OPEN_INTEREST</td>
      <td>float</td>
      <td>Total number of outstanding derivative contracts</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[21]</td>
      <td>CLAMP_MIN</td>
      <td>float</td>
      <td>Range in the average spread that does not require a funding payment</td>
    </tr>
    <tr>
      <td>[22]</td>
      <td>CLAMP_MAX</td>
      <td>float</td>
      <td>Funding payment cap</td>
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
    "/status/deriv/{key}/hist": {
      "get": {
        "summary": "Derivatives Status History",
        "description": "Endpoint used to receive different types of historical platform information - currently supports derivatives pair status only.",
        "operationId": "rest-public-derivatives-status-history",
        "parameters": [
          {
            "name": "key",
            "in": "path",
            "description": "The key of the pairs to obtain history information. (e.g. tBTCF0:USTF0, tETHF0:USTF0, ...)",
            "schema": {
              "type": "string",
              "default": "tBTCF0:USTF0"
            },
            "required": true
          },
          {
            "name": "sort",
            "in": "query",
            "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
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
            "description": "Number of records in response (max. 5000).",
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
                    "value": "\n[\n  [\n    1570578776000, //MTS\n    null, \n    8194.95, //DERIV_PRICE\n    8196.95, //SPOT_PRICE\n    null,\n    101120.80328179, //INSURANCE_FUND_BALANCE\n    null,\n    1570579200000, //NEXT_FUNDING_EVT_MTS\n    0.00021817, //NEXT_FUNDING_ACCRUED\n    9379, //NEXT_FUNDING_STEP\n    null,\n    0, //CURRENT_FUNDING\n    null, \n    null,\n    8192.823333333334, //MARK_PRICE\n    null,\n    null,\n    5174.01444474, //OPEN_INTEREST\n    null,\n    null,\n    null,\n    0.0005, //CLAMP_MIN\n    0.0025 //CLAMP_MAX\n  ],\n  [...]\n]"
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
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
