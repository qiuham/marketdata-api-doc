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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-cancel-funding-offer'
updated_at: 2026-11-24
---

# Cancel Funding Offer

Cancels an existing Funding Offer based on the offer ID entered.

> 📘 Offer ID
>
> The offer ID can be retrieved by calling the [Funding Offers](https://docs.bitfinex.com/reference#rest-auth-funding-offers) endpoint.

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
      <td>FUNDING_OFFER_ARRAY</td>
      <td><a href="#funding-offer-array-index-4">FUNDING_OFFER_ARRAY</a></td>
      <td>An array containing only the new offer</td>
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

#### Funding offer array (Index \[4])

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
      <td>Integer</td>
      <td>Offer ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>SYMBOL</td>
      <td>String</td>
      <td>The currency of the offer (fUSD, etc)</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MTS_CREATED</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the offer was created</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>MTS_UPDATED</td>
      <td>Int</td>
      <td>Millisecond Time Stamp when the offer was updated</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Current amount of the offer</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT_ORIGINAL</td>
      <td>Float</td>
      <td>Amount of the initial offer</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>OFFER_TYPE</td>
      <td>String</td>
      <td>Offer Type</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>FLAGS</td>
      <td>Int</td>
      <td>Flags active on the offer; see https://docs.bitfinex.com/v2/docs/flag-values</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>OFFER_STATUS</td>
      <td>String</td>
      <td>Offer Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[14]</td>
      <td>RATE</td>
      <td>Float</td>
      <td>Rate of the offer (percentage expressed as decimal number i.e. 1% = 0.01)</td>
    </tr>
    <tr>
      <td>[15]</td>
      <td>PERIOD</td>
      <td>Int</td>
      <td>Period of the offer</td>
    </tr>
    <tr>
      <td>[16]</td>
      <td>NOTIFY</td>
      <td>Boolean</td>
      <td>True / false</td>
    </tr>
        <tr>
      <td>[17]</td>
      <td>HIDDEN</td>
      <td>Int</td>
      <td>0 if false, 1 if true</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>RENEW</td>
      <td>Boolean</td>
      <td>True / false</td>
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
    "/auth/w/funding/offer/cancel": {
      "post": {
        "summary": "Cancel Funding Offer",
        "description": "Cancels an existing Funding Offer based on the offer ID entered.",
        "operationId": "rest-auth-cancel-funding-offer",
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
                    "description": "Offer ID",
                    "format": "int64"
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
                    "value": "[\n  1568716652310, //MTS\n  \"foc-req\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    604393839, //ID\n    \"fUSD\", //SYMBOL\n    1568716545000, //MTS_CREATED\n    1568716545000, //MTS_UPDATED\n    50, //AMOUNT\n    50, //AMOUNT_ORIG\n    \"LIMIT\", //OFFER_TYPE\n    null, //PLACEHOLDER\n    null,//PLACEHOLDER\n    null, //FLAGS\n    \"ACTIVE\", //OFFER_STATUS\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.06, //RATE\n    2, //PERIOD\n    false, //NOTIFY\n    null, //HIDDEN\n    null, //PLACEHOLDER\n    false, //RENEW\n    null //PLACEHOLDER\n  ], //FUNDING_OFFER_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  null //TEXT\n]\n"
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
