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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-position-increase'
updated_at: 2026-11-23
---

# Increase Position

Essentially a reverse of the [Claim Position](https://docs.bitfinex.com/reference#rest-auth-position-claim) feature, the Increase Position feature allows you to create a new position using the funds in your margin wallet. For more information about this feature, please look to the [Increase Position article](https://support.bitfinex.com/hc/en-us/articles/900004477903-Increase-Position) on our knowledge base.

The Increase Position feature requires a verified or paper trading account. Full verification is required to use the increase position feature to open a long position on pairs with a fiat quote currency.

> 🚧 Verification Required
>
> The Increase Position feature is only available on accounts with, basic+, intermediate or full [verification levels](https://support.bitfinex.com/hc/en-us/articles/360017321633-Verification-Levels-and-Advantages) or on accounts marked for paper trading.
>
> Full verification is required to use the increase position feature to open a long position on pairs with a fiat quote currency.

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
      <td>Seconds epoch timestamp of notification</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>string</td>
      <td>Notification's type ("pmi-req")</td>
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
      <td><a href="#position-increase-array">Position increase array</a>[]</td>
      <td>An array containing info on the position increase</td>
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

#### Position increase array

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
        <td>Pair (tBTCUSD, …)</td>
      </tr>
      <tr>
        <td colspan="4">
          <div class="placeholders">[ . . . ]</div>
        </td>
      </tr>
      <tr>
        <td>[2]</td>
        <td>AMOUNT</td>
        <td>float</td>
        <td>Size of the position. Positive for long, negative for short positions</td>
      </tr>
      <tr>
        <td>[3]</td>
        <td>BASE_PRICE</td>
        <td>float</td>
        <td>Base price of the position (average of all trades related to the position)</td>
      </tr>
      
      <tr>
        <td colspan="4">
          <div class="placeholders">[ . . . ]</div>
        </td>
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
    "/auth/w/position/increase": {
      "post": {
        "summary": "Increase Position",
        "description": "Essentially a reverse of the [Claim Position](https://docs.bitfinex.com/reference#rest-auth-position-claim) feature, the Increase Position feature allows you to create a new position using the funds in your margin wallet. For more information about this feature, please look to the [Increase Position article](https://support.bitfinex.com/hc/en-us/articles/900004477903-Increase-Position) on our knowledge base.\n\nThe Increase Position feature requires a verified or paper trading account. Full verification is required to use the increase position feature to open a long position on pairs with a fiat quote currency.",
        "operationId": "rest-auth-position-increase",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "symbol",
                  "amount"
                ],
                "properties": {
                  "symbol": {
                    "type": "string",
                    "description": "Trading pair on which you wish to open a position",
                    "default": "tBTCUSD"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount of the position. (positive for long, negative for short)",
                    "default": "123"
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
                    "value": "[\n  1612447904081, //MTS\n  'pmi-req', //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    'tBTCUSD', //SYMBOL\n    null, //PLACEHOLDER\n    1, //AMOUNT\n    100, //BASE_PRICE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null //PLACEHOLDER\n  ],\n  null, //CODE\n  'SUCCESS', //STATUS\n  'Submitting position increase.' //TEXT\n]\n"
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
