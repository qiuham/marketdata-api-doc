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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-orders-history-by-symbol'
updated_at: 2026-11-27
---

# Orders History (by symbol)

Retrieves all user's closed/cancelled orders up to 2 weeks in the past by trading pair symbol (e.g. tBTCUSD, tLTCBTC, ...).

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
      <td>ID</td>
      <td>int</td>
      <td>Order ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>GID</td>
      <td>int</td>
      <td>Group Order ID</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>CID</td>
      <td>int</td>
      <td>Client Order ID</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>SYMBOL</td>
      <td>string</td>
      <td>Trading pair (tBTCUSD, tLTCBTC, ...)</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>MTS_CREATE</td>
      <td>int</td>
      <td>Millisecond epoch timestamp of creation</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>MTS_UPDATE</td>
      <td>int</td>
      <td>Millisecond epoch timestamp of last update</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Positive means buy, negative means sell</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>AMOUNT_ORIG</td>
      <td>float</td>
      <td>Original amount (before any update)</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>ORDER_TYPE</td>
      <td>string</td>
      <td>The order's type (see list below)</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>TYPE_PREV</td>
      <td>string</td>
      <td>Previous order type (before the last update)</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>MTS_TIF</td>
      <td>int</td>
      <td>Millisecond epoch timestamp for TIF (Time-In-Force)</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[12]</td>
      <td>FLAGS</td>
      <td>int</td>
      <td>Sum of all active flags for the order (values can be found <a href="https://docs.bitfinex.com/v2/docs/flag-values">here</a>)</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>A complete overview on available order statuses can be found <a href="https://docs.bitfinex.com/docs/abbreviations-glossary#order-status">here</a></td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[16]</td>
      <td>PRICE</td>
      <td>float</td>
      <td>Price</td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>PRICE_AVG</td>
      <td>float</td>
      <td>Average price</td>
    </tr>
    <tr>
      <td>[18]</td>
      <td>PRICE_TRAILING</td>
      <td>float</td>
      <td>The trailing price</td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>PRICE_AUX_LIMIT</td>
      <td>float</td>
      <td>Auxiliary Limit price (for STOP LIMIT)</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[23]</td>
      <td>NOTIFY</td>
      <td>int</td>
      <td>1 if operations on order must trigger a notification, 0 if operations on order must not trigger a notification</td>
    </tr>
    <tr>
      <td>[24]</td>
      <td>HIDDEN</td>
      <td>int</td>
      <td>1 if order must be hidden, 0 if order must not be hidden</td>
    </tr>
    <tr>
      <td>[25]</td>
      <td>PLACED_ID</td>
      <td>int</td>
      <td>If another order caused this order to be placed (OCO) this will be that other order's ID</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[28]</td>
      <td>ROUTING</td>
      <td>string</td>
      <td>Indicates origin of action: BFX, API>BFX</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[31]</td>
      <td>META</td>
      <td>JSON</td>
      <td>Additional meta information about the order ( $F7 = IS_POST_ONLY (0 if false, 1 if true), $F33 = Leverage (int), aff_code: "aff_code_here")</td>
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

<br />

> 📘 Available order types
>
> Available order types are: `LIMIT`, `MARKET`, `STOP`, `STOP LIMIT`, `TRAILING STOP`, `FOK`, `IOC`.\
> For exchange orders, add the EXCHANGE prefix: `EXCHANGE LIMIT`, `EXCHANGE MARKET`, `EXCHANGE STOP`, `EXCHANGE STOP LIMIT`, `EXCHANGE TRAILING STOP`, `EXCHANGE FOK`, `EXCHANGE IOC`

<br />

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
    "title": "api-settings-auth",
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
    "/auth/r/orders/{symbol}/hist": {
      "post": {
        "summary": "Orders History (by symbol)",
        "description": "Retrieves all user's closed/cancelled orders up to 2 weeks in the past by trading pair symbol (e.g. tBTCUSD, tLTCBTC, ...).",
        "operationId": "rest-auth-orders-history-by-symbol",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "description": "The symbol for which to retrieve order history (e.g. tBTCUSD, tETHUSD, ...).",
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
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
                    "description": "If start is given, only records with MTS_CREATE >= start (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "description": "If end is given, only records with MTS_CREATE <= end (milliseconds) will be given as response.",
                    "format": "int64"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records in response (max. 2500)",
                    "format": "int32"
                  },
                  "id": {
                    "type": "array",
                    "description": "Allows users to retrieve specific orders by Order ID (id: [ID1, ID2, ID3]).",
                    "items": {
                      "type": "integer",
                      "format": "int64"
                    }
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
                    "value": "[\n  [\n    33961681942, //ID\n    \"1227\", //GID\n    1337, //CID\n    \"tBTCUSD\", //SYMBOL\n    1573482478000, //MTS_CREATE\n    1573485373000, //MTS_UPDATE\n    0.001, //AMOUNT\n    0.001, //AMOUNT_ORIG\n    \"EXCHANGE LIMIT\", //ORDER_TYPE\n    null, //TYPE_PREV\n    null, //MTS_TIF\n    null,\n    \"0\", //FLAGS\n    \"CANCELED\", //STATUS\n    null,\n    null,\n    15, //PRICE\n    0, //PRICE_AVG\n    0, //PRICE_TRAILING\n    0, //PRICE_AUX_LIMIT\n    null,\n    null,\n    null,\n    0, //NOTIFY\n    0, //HIDDEN\n    null, //PLACED_ID\n    null,\n    null,\n    \"API>BFX\", //ROUTING\n    null,\n    null,\n    null //META\n  ],\n  [...]\n]"
                  }
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
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": false,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
