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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-auto-renew'
updated_at: 2026-11-22
---

# Funding Auto-renew

Activate or deactivate auto-renew. Allows you to specify the currency, amount, rate, and period.

#### Response array

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
      <td>Notification's type ("fa-req")</td>
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
      <td>FUNDING_OFFER_ARRAY</td>
      <td><a href="#funding-offer-array-index-4">FUNDING_OFFER_ARRAY</a></td>
      <td>An array containing data for the funding offer</td>
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

#### Funding offer array (index 4)

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
      <td>CURRENCY</td>
      <td>String</td>
      <td>Currency (USD, …)</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>PERIOD</td>
      <td>Int</td>
      <td>Period in days</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>RATE</td>
      <td>Float</td>
      <td>Rate of the offer (percentage expressed as decimal number i.e. 1% = 0.01)</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>THRESHOLD</td>
      <td>Float</td>
      <td>Max amount to be auto-renewed</td>
    </tr>
  </tbody>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb;
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
    "/auth/w/funding/auto": {
      "post": {
        "summary": "Funding Auto-renew",
        "description": "Activate or deactivate auto-renew. Allows you to specify the currency, amount, rate, and period.",
        "operationId": "rest-auth-funding-auto-renew",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "status",
                  "currency"
                ],
                "properties": {
                  "status": {
                    "type": "integer",
                    "description": "1 to activate, 0 to deactivate",
                    "default": 1,
                    "format": "int32"
                  },
                  "currency": {
                    "type": "string",
                    "description": "Currency for which to enable auto-renew",
                    "default": "USD"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount to be auto-renewed (Minimum 50 USD equivalent). Defaultst to the amount currently provided if omitted.",
                    "default": "123.45"
                  },
                  "rate": {
                    "type": "string",
                    "description": "Percentage rate at which to auto-renew. (rate == 0 to renew at FRR). Defaults to FRR if omitted"
                  },
                  "period": {
                    "type": "integer",
                    "description": "Period in days. Defaults to 2 if omitted.",
                    "default": 2,
                    "format": "int32"
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
                    "value": "[\n  1574075756185, //MTS\n  \"fa-req\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    \"UST\", //CURRENCY\n    2, //PERIOD\n    0, //RATE\n    350 //THRESHOLD\n  ],//FUNDING_OFFER_ARRAY\t\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"Auto-renew of UST offers activated at FRR for 2 days periods\" //TEXT\n]"
                  }
                },
                "schema": {
                  "type": "array"
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
