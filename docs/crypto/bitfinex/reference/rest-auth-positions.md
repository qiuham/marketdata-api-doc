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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-positions'
updated_at: 2026-11-25
---

# Retrieve Positions

Get active positions

### Response Fields

| Index | Field           | Type                               | Description                                               |
| :---- | :-------------- | :--------------------------------- | :-------------------------------------------------------- |
| \[0]  | POSITION\_ARRAY | [Position Array](#positions-array) | Each index contains one of the n current user's positions |

#### Positions Array

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
      <td>Pair (tBTCUSD ...)</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>Position status (ACTIVE)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Position value. Positive for long and negative for short positions</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>BASE_PRICE</td>
      <td>float</td>
      <td>Base price of the position (average traded price of all previous orders related to the position).</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>FUNDING</td>
      <td>float</td>
      <td>Current funding cost of the position</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>FUNDING_TYPE</td>
      <td>int</td>
      <td>0 for daily, 1 for term</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>PL</td>
      <td>float</td>
      <td>Profit & Loss (includes 0.2% fee to close position)</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>PL_PERC</td>
      <td>float</td>
      <td>Profit & loss percentage</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>PRICE_LIQ</td>
      <td>float</td>
      <td>Liquidation price</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>LEVERAGE</td>
      <td>float</td>
      <td>Leverage used for the position</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[11]</td>
      <td>POSITION_ID</td>
      <td>int</td>
      <td>Position ID</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>MTS_CREATE</td>
      <td>int</td>
      <td>Millisecond timestamp of creation</td>
    </tr>
    <tr>
      <td>[13]</td>
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
      <td>[15]</td>
      <td>TYPE</td>
      <td>int</td>
      <td>Identifies the type of position: 0 = Margin position, 1 = Derivatives position</td>
    </tr>
        <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>COLLATERAL</td>
      <td>float</td>
      <td>Position collateral</td>
    </tr>
    <tr>
      <td>[18]</td>
      <td>COLLATERAL_MIN</td>
      <td>float</td>
      <td>Min Collateral Required</td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>META</td>
      <td>JSON str</td>
      <td>Meta data about the position</td>
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
    "/auth/r/positions": {
      "post": {
        "summary": "Retrieve Positions",
        "description": "Get active positions",
        "operationId": "rest-auth-positions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "RAW_BODY": {
                    "type": "string",
                    "default": "{}",
                    "format": "json"
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
                    "value": "  [\n    [\n    \"tBTCUSD\", //SYMBOL\n    \"ACTIVE\", //STATUS\n    0.0195, //AMOUNT\n    8565.0267019, //BASE_PRICE\n    0, //FUNDING\n    0, //FUNDING_TYPE\n    -0.33455568705000516, //PL\n    -0.0003117550117425625, //PL_PERC\n    7045.876419249083, //PRICE_LIQ\n    3.0673001895895604, //LEVERAGE\n    null, //PLACEHOLDER\n    142355652, //POSITION_ID\n    1574002216000, //MTS_CREATE\n    1574002216000, //MTS_UPDATE\n    null, //PLACEHOLDER\n    0, //TYPE\n    null, //PLACEHOLDER\n    0, //COLLATERAL\n    0, //COLLATERAL_MIN\n    {\n    \t\"reason\":\"TRADE\",\n    \t\"order_id\":34271018124,\n    \t\"liq_stage\":null,\n    \t\"trade_price\":\"8565.0267019\",\n    \t\"trade_amount\":\"0.0195\",\n    \t\"order_id_oppo\":34277498022\n    } //META\n\t] //POSITION_ARRAY\n]    \n"
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
