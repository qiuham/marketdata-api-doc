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
source_url: 'https://docs.bitfinex.com/reference/rest-public-tickers-history'
updated_at: 2026-11-27
---

# Tickers History

History of recent trading tickers. Provides historic data of the best bid and ask at an hourly interval.

Historic data goes back 1 year.

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
      <td>SYMBOL</td>
      <td>string</td>
      <td>The symbol of the requested ticker history data</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>BID</td>
      <td>float</td>
      <td>Price of last highest bid</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[3]</td>
      <td>ASK</td>
      <td>float</td>
      <td>Price of last lowest ask</td>
    </tr>

    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>

    <tr>
      <td>[12]</td>
      <td>MTS</td>
      <td>int</td>
      <td>Millisecond epoch timestamp</td>
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
    "/tickers/hist": {
      "get": {
        "summary": "Tickers History",
        "description": "History of recent trading tickers. Provides historic data of the best bid and ask at an hourly interval.\n\nHistoric data goes back 1 year.",
        "operationId": "rest-public-tickers-history",
        "parameters": [
          {
            "name": "symbols",
            "in": "query",
            "description": "The symbols you want information about as a comma separated list, or ALL for every symbol. Ex: 'tBTCUSD' (funding currencies are not supported at this time).",
            "required": true,
            "schema": {
              "type": "string",
              "default": "ALL"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of records in response (max. 250).",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 100
            },
            "required": false
          },
          {
            "name": "start",
            "in": "query",
            "description": "If start is given, only records with MTS >= start (milliseconds) will be given as response.",
            "schema": {
              "type": "integer",
              "default": ""
            },
            "required": false
          },
          {
            "name": "end",
            "in": "query",
            "description": "If end is given, only records with MTS <= end (milliseconds) will be given as response.",
            "schema": {
              "type": "integer",
              "default": ""
            },
            "required": false
          },
          {
            "name": "sort",
            "in": "query",
            "required": false,
            "description": "+1: sort in ascending order | -1: sort in descending order (by MTS field).",
            "schema": {
              "type": "integer",
              "default": "-1"
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
                    "value": "[\n  [\n    \"tMKRF0:USTF0\", //SYMBOL\n    643.57, //BID\n    null,\n    648.82, //ASK\n    null,\n    null,\n    null,\n    null,\n    null,\n    null,\n    null,\n    null,\n    1674061204000 //MTS\n  ],\n  [...]\n]"
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
