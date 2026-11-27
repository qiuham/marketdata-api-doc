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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-positions-audit'
updated_at: 2026-11-27
---

# Positions Audit

Return an audit of your positions. You latest positions will be retrieved by default, but ID's can be specified to retrieve an audit for specific positions.

#### Response data

| Index    | Field                  | Type                                                          | Description                                                            |
| :------- | :--------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------------- |
| \[0...n] | POSITION\_AUDIT\_ARRAY | [Position audit array](#position-audit-entry-arrays-index-0n) | Each index contains one of the n current user's position audit entries |

#### Position audit entry arrays (index \[0...n])

<HTMLBlock>{`
<table border="1">
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
      <td>String</td>
      <td>Pair (tETHUSD, …).</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>STATUS</td>
      <td>String</td>
      <td>Status (ACTIVE, CLOSED).</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Size of the position. A positive value indicates a long position; a negative value indicates a short position.</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>BASE_PRICE</td>
      <td>Float</td>
      <td>Base price of the position. (Average traded price of the previous orders of the position)</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>FUNDING</td>
      <td>Float</td>
      <td>Funding amount</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>FUNDING_TYPE</td>
      <td>Int</td>
      <td>0 for daily, 1 for term.</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[11]</td>
      <td>POSITION_ID</td>
      <td>Int64</td>
      <td>Position ID</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>MTS_CREATE</td>
      <td>Int</td>
      <td>Millisecond timestamp of creation</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>MTS_UPDATE</td>
      <td>Int</td>
      <td>Millisecond timestamp of update</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[15]</td>
      <td>TYPE</td>
      <td>Int</td>
      <td>Identifies the type of position: 'null' = Margin position, 1 = Derivatives position</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>COLLATERAL</td>
      <td>Float</td>
      <td>The amount of collateral applied to the open position</td>
    </tr>
    <tr>
      <td>[18]</td>
      <td>COLLATERAL_MIN</td>
      <td>Float</td>
      <td>The minimum amount of collateral required for the position</td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>META</td>
      <td>JSON String</td>
      <td>Additional meta information about the position</td>
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
    "/auth/r/positions/audit": {
      "post": {
        "summary": "Positions Audit",
        "description": "Return an audit of your positions. You latest positions will be retrieved by default, but ID's can be specified to retrieve an audit for specific positions.",
        "operationId": "rest-auth-positions-audit",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id"
                ],
                "properties": {
                  "id": {
                    "type": "array",
                    "description": "Array of id's to audit",
                    "default": [
                      null,
                      null,
                      null,
                      null
                    ],
                    "items": {
                      "type": "integer",
                      "format": "int64"
                    }
                  },
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
                    "format": "int32",
                    "default": "50"
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
                    "value": "[\n  [\n  \"tETHUSD\", //SYMBOL\n  \"ACTIVE\", //STATUS\n  0.9682, //AMOUNT\n  182.76, //BASE_PRICE\n  0, //FUNDING\n  0, //FUNDING_TYPE\n  null, //PLACEHOLDER\n  null,\t//PLACEHOLDER\n  null,\t//PLACEHOLDER\n  null,\t//PLACEHOLDER\n  null,\t//PLACEHOLDER\n  142358085, //POSITION_ID\n  1574088504000, //MTS_CREATE\n  1574088504000, //MTS_UPDATE\n  null, //PLACEHOLDER\n  null, //TYPE\n  null, //PLACEHOLDER\t\n  0, //COLLATERAL\n  null, //COLLATERAL_MIN\n  {\n    \"reason\":\"TRADE\",\n    \"order_id\":34319724780,\n    \"liq_stage\":null,\n    \"trade_price\":\n    \"182.76\",\n    \"trade_amount\":\"0.9682\",\n    \"user_id_oppo\":411107,\n    \"order_id_oppo\":34326729830\n  } //META\n  ] //POSITION_AUDIT_ARRAY\n]\n"
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
