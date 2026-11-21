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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-increase-position-info'
updated_at: 2026-11-21
---

# Increase Position Info

Returns information relevant to the increase position endpoint.

**Response Fields**

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
      <td>POSITION INFO</td>
      <td><a href="#position-info-index-0">Position Info Array</a></td>
      <td>Position info</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>BALANCE INFO</td>
      <td><a href="#balance-info-index-1">Balance Info Array</a></td>
      <td>Array of info with base currency balance, tradable balance data, and available funding</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
		<tr>
      <td>[4]</td>
      <td>FUNDING INFO</td>
      <td><a href="#funding-info-index-4">Funding Info Array</a></td>
      <td>Array with data on funding required</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>FUNDING CURRENCY INFO</td>
      <td><a href="#funding-currency-info-index-5">Funding Currency Info Array</a></td>
      <td>Array with additional info on funding required</td>
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

#### Position Info (Index \[0])

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
      <td>MAX_POS</td>
      <td>float</td>
      <td>Maximum position size for increase position on the pair</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>CURRENT_POS</td>
      <td>float</td>
      <td>Size of current position on the pair</td>
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

#### Balance Info (Index \[1])

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
      <td>BASE_CURRENCY_BALANCE</td>
      <td>float</td>
      <td>Current margin wallet balance in the base currency</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>TRADABLE BALANCE INFO</td>
      <td><a href="#tradable-balance-info-index1">Tradable Balance Info Array</a></td>
      <td>Array with total and current tradable balances for both currencies</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>FUNDING_AVAIL</td>
      <td>float</td>
      <td>Available funding below 0.75% (currency depends on the funding currency required for the entered amount)</td>
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

#### Tradable Balance Info (Index\[1])

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
      <td>TRADABLE_BALANCE_QUOTE_CURRENCY</td>
      <td>float</td>
      <td>Tradable balance in the quote currency adjusted for open orders and positions</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>TRADABLE_BALANCE_QUOTE_TOTAL</td>
      <td>float</td>
      <td>Tradable balance in the quote currency non-adjusted</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>TRADABLE_BALANCE_BASE_CURRENCY</td>
      <td>float</td>
      <td>Tradable balance in the base currency adjusted for open orders and positions</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>TRADABLE_BALANCE_BASE_TOTAL</td>
      <td>float</td>
      <td>Tradable balance in the base currency non-adjusted</td>
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

#### Funding Info (Index \[4])

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
      <td>FUNDING_VALUE</td>
      <td>float</td>
      <td>Value of funding required in opposite currency</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>FUNDING_REQUIRED</td>
      <td>float</td>
      <td>Funding required for a position of the specified amount</td>
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

#### Funding Currency Info (Index \[5])

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
      <td>FUNDING_VALUE_CURRENCY</td>
      <td>string</td>
      <td>Currency of the FUNDING_VALUE field</td>
    </tr>
		<tr>
      <td>[1]</td>
      <td>FUNDING_REQUIRED_CURRENCY</td>
      <td>string</td>
      <td>Currency of the FUNDING_REQUIRED field</td>
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
    "/auth/r/position/increase/info": {
      "post": {
        "summary": "Increase Position Info",
        "description": "Returns information relevant to the increase position endpoint.",
        "operationId": "rest-auth-increase-position-info",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "symbol"
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
                    "value": " \n[\n  [\n   10, //MAX_POS\n   0.1 //CURRENT_POS\n  ],//POSITION INFO\n  [\n    1.09965743, //BASE_CURRENCY_BALANCE\n   [\n    516734.60048924293, //TRADABLE_BALANCE_QUOTE_CURRENCY\n    518415.66409424297, //TRADABLE_BALANCE_QUOTE_TOTAL\n    11.5085657124553, //TRADABLE_BALANCE_BASE_CURRENCY\n    11.702877580552862, //TRADABLE_BALANCE_BASE_TOTAL\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null //PLACEHOLDER\n   ], \n   6843080.04050819 //\tFUNDING_AVAIL\n  ], //BALANCE INFO \n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  [\n   1.5, //FUNDING_VALUE\n   63345 //FUNDING_REQUIRED\n  ], \n  [\n   'BTC', //FUNDING_VALUE_CURRENCY\n   'USD' //FUNDING_REQUIRED_CURRENCY\n  ]\n]"
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
