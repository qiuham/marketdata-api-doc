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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-summary'
updated_at: 2026-11-26
---

# Summary

Provides an overview of the different fee rates for the account as well as the LEO discount level and the average amount of LEO held over the last 30 days.

#### Response data

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
      <td>[4]</td>
      <td>FEE_INFO</td>
      <td><a href="#fee-info-array-index-4">Fee info array</a></td>
      <td>Array with info on your current fee rates</td>
    </tr>
		<tr>
      <td>[5]</td>
      <td>TRADING_VOL_AND_FEE</td>
      <td><a href="#trading-volume-and-fees-array-index-5">Trading vol and fee</a></td>
      <td>Array with data on your trading volume and fees paid</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>FUNDING_EARNINGS</td>
      <td><a href="#funding-earnings-array-index-6">Funding earnings array</a></td>
      <td>Array with data on your funding earnings</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>LEO_INFO</td>
      <td>Object</td>
      <td>Object with info on your LEO level and holdings. Keys: "leo_lev" (to see your current LEO level) and "leo_amount_avg" (to see your average LEO amount held in the past 30 days)</td>
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

#### Fee info array (Index \[4])

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
      <td>MAKER_FEE_INFO</td>
      <td><a href="#maker-fee-info-array-index-4">Maker fee info array</a></td>
      <td>Array with info on your current maker fee rates</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TAKER_FEE_INFO</td>
      <td><a href="#taker-fee-info-array-index-4">Taker fee info array</a></td>
      <td>Array with info on your current taker fee rates</td>
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

##### Maker fee info array (Index \[0])

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
      <td>MAKER_FEE</td>
      <td>Float</td>
      <td>Shows the maker fee rate for the account</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>MAKER_FEE</td>
      <td>Float</td>
      <td>Shows the maker fee rate for the account</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MAKER_FEE</td>
      <td>Float</td>
      <td>Shows the maker fee rate for the account</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>DERIV_REBATE</td>
      <td>float</td>
      <td>Shows the maker rebate for derivative trades on the account</td>
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

##### Taker fee info array (Index \[1])

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
      <td>TAKER_FEE_TO_CRYPTO</td>
      <td>Float</td>
      <td>Shows the taker fee rate for crypto to crypto trades on the account</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TAKER_FEE_TO_STABLE</td>
      <td>Float</td>
      <td>Shows the taker fee rate for crypto to stable coin trades on the account</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>TAKER_FEE_TO_FIAT</td>
      <td>Float</td>
      <td>Shows the taker fee rate for crypto to fiat trades on the account</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>DERIV_TAKER_FEE</td>
      <td>float</td>
      <td>Shows the taker fee rate for derivative trades on the account</td>
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

#### Trading volume and fees array (Index \[5])

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
      <td>TRADE_VOL_30d</td>
      <td>Array of objects</td>
      <td>Shows objects containing trading volume per currency and Total(USD) over the past 30 days</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>FEES_TRADING_30d</td>
      <td>Object</td>
      <td>Shows trading fees paid per currency over the past 30 days</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>FEES_TRADING_TOTAL_30d</td>
      <td>Float</td>
      <td>Shows the USD equivalent of the total trading fees paid over the past 30 days</td>
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

#### Funding earnings array (Index \[6]

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
      <td>FUNDING_EARNINGS_PER_CURR</td>
      <td>Object</td>
      <td>Shows the amount earned on your provided funding per currency over the past 30 days</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>FUNDING_EARNINGS_TOTAL</td>
      <td>Float</td>
      <td>Shows the USD equivalent of the total earnings on your provided funding over the past 30 days</td>
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
    "/auth/r/summary": {
      "post": {
        "summary": "Summary",
        "description": "Provides an overview of the different fee rates for the account as well as the LEO discount level and the average amount of LEO held over the last 30 days.",
        "operationId": "rest-auth-summary",
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
                    "value": "[\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  [\n    [\n    0.001, //MAKER_FEE\n    0.001, //MAKER_FEE\n    0.001, //MAKER_FEE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.0002 //DERIV_REBATE\n\t ], //MAKER_FEE_INFO\n   [\n    0.002 //TAKER_FEE_TO_CRYPTO,\n    0.002 //TAKER_FEE_TO_STABLE,\n    0.002 //TAKER_FEE_TO_FIAT,\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.0065 //DERIV_TAKER_FEE\n   ] //TAKER_FEE_INFO\n  ], //FEE_INFO\n  [\n    [\n      {\"curr\": \"BTCF0\", \"vol\": 0.016},\n      {\"curr\": \"BTC\", \"vol\": 0.765}\n      {\"curr\": \"Total (USD)\",\n        \"vol\": 52069.01928633,\n        \"vol_safe\": 52069.01928633,\n        \"vol_maker\": 11362.82692633,\n        \"vol_BFX\": 52069.01928633,\n        \"vol_BFX_safe\": 52069.01928633,\n        \"vol_BFX_maker\": 11362.82692633\n      },\n    ] //TRADE_VOL_30d,\n    {\n  \t\t\"USTF0\": 0.17569482,\n      \"USD\": 38.95555663,\n      \"BTC\": 0.0005152\n    } //FEES_TRADING_30d,\n    51.12300602 //FEES_TRADING_TOTAL_30d\n  ],//TRADING_VOL_AND_FEE\n  [\n    null, //PLACEHOLDER\n    {\n      \"USD\": 21.87,\n      \"BTC\": 0.04\n    } //FUNDING_EARNINGS_PER_CURR,\n    82.1078 //FUNDING_EARNINGS_TOTAL\n  ], //FUNDING_EARNINGS\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  {\n    \"leo_lev\": 0, //LEO_LEV\n    \"leo_amount_avg\": 0, //LEO_AMOUNT_AVG\n  } //LEO_INFO\n]"
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
