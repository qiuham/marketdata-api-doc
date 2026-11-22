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
source_url: 'https://docs.bitfinex.com/reference/otc-orders-history'
updated_at: 2026-11-22
---

# OTC Orders History

Returns historic OTC orders.

### Response data

| Index    | Field | Type                           | Description                                                            |
| :------- | :---- | :----------------------------- | :--------------------------------------------------------------------- |
| \[0...n] | ORDER | [OTC Order](#otc-order-arrays) | Each index contains one of the `n` current user's historic OTC orders. |

#### OTC order arrays

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
      <td>SYMBOL</td>
      <td>string</td>
      <td>Pair (tBTCUSD, …)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MTS_CREATE</td>
      <td>int</td>
      <td>Millisecond timestamp of creation</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>MTS_UPDATE</td>
      <td>int</td>
      <td>Millisecond timestamp of update</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>INITIATOR</td>
      <td>int</td>
      <td>Order initiator, 0 means counter party initiated order, 1 means user initiated the order</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>INITIATOR_NICKNAME</td>
      <td>string</td>
      <td>Nickname of the initiator</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>COUNTER_PARTY_NICKNAME</td>
      <td>string</td>
      <td>Nickname of the counter party user</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Positive means buy, negative means sell</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>PRICE</td>
      <td>float</td>
      <td>Order price</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>OTC order status, available statuses are: PENDING, CANCELED, REJECTED, COMPLETED</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>TIF</td>
      <td>int</td>
      <td>Millisecond timestamp of automatic trade cancelation</td>
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
    "/auth/r/orders/otc/{Symbol}/hist": {
      "post": {
        "summary": "OTC Orders History",
        "description": "Returns historic OTC orders.",
        "operationId": "otc-orders-history",
        "parameters": [
          {
            "name": "Symbol",
            "in": "path",
            "description": "Symbol (tBTCUSD, ...) , Omit for all symbols (see example)",
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
                    "default": 25,
                    "format": "int32"
                  },
                  "id": {
                    "type": "array",
                    "description": "Allows you to retrieve specific orders by order ID (id: [ID1, ID2, ID3])",
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
                    "value": "[\n  [\n  123, //ID\n  \"tBTCUSD\", //SYMBOL\n  1669126974000, //MTS_CREATE\n  1670596411000, //MTS_UPDATE\n  null, //PLACEHOLDER\n  1, //INITIATOR\n  \"john-doe\", //INITIATOR_NICKNAME\n  \"jane-btc\", //COUNTER_PARTY_NICKNAME\n  null, //PLACEHOLDER\n  0.025, //AMOUNT\n  26325, //PRICE\n  null, //PLACEHOLDER\n  \"REJECTED\" //STATUS\n\t]// OTC_ORDER\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "array"
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
