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
source_url: 'https://docs.bitfinex.com/reference/rest-public-derivatives-status'
updated_at: 2026-11-23
---

# Derivatives Status

Endpoint used to receive different types of platform information - currently supports derivatives pair status only.

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
      <td>KEY</td>
      <td>string</td>
      <td>Requested key(s)</td>
    </tr>
    <tr>
      <td>[1]</td>
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
      <td>[3]</td>
      <td>DERIV_PRICE</td>
      <td>float</td>
      <td>Derivative book mid price</td>
    </tr>
    <tr>
      <td>[4]</td>
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
      <td>[6]</td>
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
      <td>[8]</td>
      <td>NEXT_FUNDING_EVT_MTS</td>
      <td>int</td>
      <td>Millisecond timestamp of next funding event</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>NEXT_FUNDING_ACCRUED</td>
      <td>float</td>
      <td>Current accrued funding for next 8h period</td>
    </tr>
    <tr>
      <td>[10]</td>
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
      <td>[12]</td>
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
      <td>[15]</td>
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
      <td>[18]</td>
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
      <td>[22]</td>
      <td>CLAMP_MIN</td>
      <td>float</td>
      <td>Range in the average spread that does not require a funding payment</td>
    </tr>
    <tr>
      <td>[23]</td>
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
    "/status/deriv": {
      "get": {
        "summary": "Derivatives Status",
        "description": "Endpoint used to receive different types of platform information - currently supports derivatives pair status only.",
        "operationId": "rest-public-derivatives-status",
        "parameters": [
          {
            "name": "keys",
            "in": "query",
            "description": "The key or keys (separate by commas) of the pairs to fetch status information. To fetch information for all pairs use the key value 'ALL'.",
            "schema": {
              "type": "string",
              "default": "tBTCF0:USTF0,tETHF0:USTF0"
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
                    "value": "[\n  [\n    \"tAMPF0:USTF0\", //KEY\n    1596124822000, //MTS\n    null,\n    0.896, //DERIV_PRICE\n    0.771995, //SPOT_PRICE\n    null,\n    1396531.67460709, //INSURANCE_FUND_BALANCE\n    null,\n    1596153600000, //NEXT_FUNDING_EVT_MTS\n    0.0001056, //NEXT_FUNDING_ACCRUED\n    6, //NEXT_FUNDING_STEP \n    null,\n    -0.01381344, //CURRENT_FUNDING\n    null,\n    null,\n    0.7664, //MARK_PRICE\n    null,\n    null,\n    246502.09001551, //OPEN_INTEREST\n    null,\n    null,\n    null,\n    0.0005, //CLAMP_MIN\n    0.0025 //CLAMP_MAX\n  ],\n  [...]\n]"
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
