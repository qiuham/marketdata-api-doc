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
source_url: 'https://docs.bitfinex.com/reference/rest-public-liquidations'
updated_at: 2026-11-21
---

# Liquidations

Endpoint to retrieve liquidations. By default it will retrieve the most recent liquidations, but time-specific data can be retrieved using timestamps.

### Request Fields

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
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[1]</td>
      <td>POS_ID</td>
      <td>int</td>
      <td>Position ID</td>
    </tr>
    <tr>
      <td>[2]</td>
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
      <td>[4]</td>
      <td>SYMBOL</td>
      <td>string</td>
      <td>Trading pair (e.g. tBTCUSD, ...)</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Size of the position. Positive values means a long position, negative values means a short position.</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>BASE_PRICE</td>
      <td>float</td>
      <td>The price at which user entered the position</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[8]</td>
      <td>IS_MATCH</td>
      <td>int</td>
      <td>0: initial liquidation trigger | 1: market execution</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>IS_MARKET_SOLD</td>
      <td>int</td>
      <td>0: position acquired by the system | 1: direct sell into the market</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[11]</td>
      <td>PRICE_ACQUIRED</td>
      <td>float</td>
      <td>The price at which the position has been acquired</td>
    </tr>
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
    <td style="text-align: right;">3 reqs/min (requests per minute)</td>
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
    "/liquidations/hist": {
      "get": {
        "summary": "Liquidations",
        "description": "Endpoint to retrieve liquidations. By default it will retrieve the most recent liquidations, but time-specific data can be retrieved using timestamps.",
        "operationId": "rest-public-liquidations",
        "parameters": [
          {
            "name": "sort",
            "in": "query",
            "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "-1"
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
            "description": "Number of records in response (max. 500).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "120"
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
                    "value": "[\n  [\n    [\n    \t\"pos\",\n      158793100, //POS_ID\n      1678465351520, //MTS\n      null,\n      \"tAMPF0:USTF0\", //SYMBOL\n      1e-8, //AMOUNT\n      1.0093, //BASE_PRICE\n      null,\n      0, //IS_MATCH\n      1, //IS_MARKET_SOLD\n      null,\n      1.0098 //PRICE_ACQUIRED\n    ]\n  ],\n  [...]\n]"
                  }
                }
              }
            }
          }
        },
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
