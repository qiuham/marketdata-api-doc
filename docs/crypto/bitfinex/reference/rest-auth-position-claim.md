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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-position-claim'
updated_at: 2026-11-24
---

# Claim Position

The claim feature allows the use of funds you have in your Margin Wallet to settle a leveraged position as an exchange buy or sale. Claiming some or all of a position requires that you have enough partially realized P/L (you've reduced the position at a profit) and/or funds (BTC or USD) in your Margin Wallet (net of any outstanding financing charges) to satisfy some or all of the outstanding financing associated with your position.

### Response fields

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
      <td>Seconds epoch timestamp of notification</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>string</td>
      <td>Notification's type ("on-req")</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MESSAGE_ID</td>
      <td>int</td>
      <td>Unique notification's ID</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[4]</td>
      <td>DATA</td>
      <td><a href="#claim-array">Claim Array</a>[]</td>
      <td>An array containing info on the position claim</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>CODE</td>
      <td>int</td>
      <td>W.I.P. (work in progress)</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>TEXT</td>
      <td>string</td>
      <td>Additional notification description</td>
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

#### Claim array

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Term</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[0]</td>
      <td>SYMBOL</td>
      <td>string</td>
      <td>Pair (tBTCUSD, …).</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>POSITION_STATUS</td>
      <td>string</td>
      <td>Status (ACTIVE, CLOSED).</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>
        Size of the position. Positive values means a long position, negative
        values means a short position.
      </td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>BASE_PRICE</td>
      <td>float</td>
      <td>
        Base price of the position. (Average traded price of the previous orders
        of the position)
      </td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>MARGIN_FUNDING</td>
      <td>float</td>
      <td>The amount of funding being used for this position.</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>MARGIN_FUNDING_TYPE</td>
      <td>int</td>
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
      <td>int</td>
      <td>position identifier</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>MTS_CREATE</td>
      <td>time</td>
      <td>Timestamp of creation (millis)</td>
    </tr>
    <tr>
        <td>[13]</td>
      <td>MTS_UPDATE</td>
      <td>time</td>
      <td>Timestamp of last update (millis)</td>
    </tr>
    <tr>
        <td colspan="4">
          <div class="placeholders">[ . . . ]</div>
        </td>
      </tr>
    <tr>
      <td>[15]</td>
      <td>POS_TYPE</td>
      <td>int</td>
      <td>Type of Position (0 for margin, 1 for deriv)</td>
    </tr>
    
        <tr>
        <td colspan="4">
          <div class="placeholders">[ . . . ]</div>
        </td>
      </tr>
    <tr>
    
    <tr>
      <td>[17]</td>
      <td>COLLATERAL</td>
      <td>float</td>
      <td>Position collateral</td>
    </tr>
    <tr>
      <td>[18]</td>
      <td>MIN_COLLATERAL</td>
      <td>float</td>
      <td>Min Collateral Required</td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>META</td>
      <td>JSON str</td>
      <td>Meta data about the position claim</td>
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

> 📘 Position ID
>
> Position ID retrievable via <https://docs.bitfinex.com/v2/reference#rest-auth-positions>

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
    "/auth/w/position/claim": {
      "post": {
        "summary": "Claim Position",
        "description": "The claim feature allows the use of funds you have in your Margin Wallet to settle a leveraged position as an exchange buy or sale. Claiming some or all of a position requires that you have enough partially realized P/L (you've reduced the position at a profit) and/or funds (BTC or USD) in your Margin Wallet (net of any outstanding financing charges) to satisfy some or all of the outstanding financing associated with your position.",
        "operationId": "rest-auth-position-claim",
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
                    "type": "integer",
                    "description": "Position ID",
                    "format": "int64"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Optional amount, used to perform a partial claim.",
                    "default": "\"0.001\""
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
                    "value": " [ \n  1568650414540, //MTS\n  'pm-req', //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [ \n    'tBTCUSD', //SYMBOL\n    'ACTIVE', //POSITION_STATUS\n    -0.001, //AMOUNT\n    10119, //BASE_PRICE\n    0, //MARGIN_FUNDING\n    0, //MARGIN_FUNDING_TYPE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    142031891, //POSITION_ID\n    1568650294000, //MTS_CREATE\n    1568650294000, //MTS_UPDATE\n    null, //PLACEHOLDER\n    0, //POS_TYPE\n    null, //PLACEHOLDER\n    0, //COLLATERAL\n    null, //MIN_COLLATERAL\n    '{\"reason\": \"TRADE\", \"order_id\": 31089337681, \"liq_stage\": null, \"trade_price\": \"10119.0\", \"trade_amount\": \"-0.001\", \"user_id_oppo\": 183923, \"order_id_oppo\": 31089692490}' //META \n  ], //CLAIM_ARRAY\n  null, //CODE\t\n  'SUCCESS', //STATUS\n  null //TEXT \n]\n"
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
