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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-submit-funding-offer'
updated_at: 2026-11-20
---

# Submit Funding Offer

Submit a new funding offer.

**What is FRR?**

The FRR, or Flash Return Rate, is a dynamic rate that is a derivative of current market conditions.\
See the [Knowledge Base](https://support.bitfinex.com/hc/en-us/articles/213919009-Flash-Return-Rate) for more information.

**FRR Offer**

To place an FRR offer, use type FRRDELTAVAR and specify the rate as 0. This will place an FRRDELTAVAR offer with an offset of 0.

> 📘 Funding Order Types
>
> **LIMIT: Place an order at an explicit, static rate**\
> e.g. Placing a LIMIT order with a rate of 0.01 will put an order on the book with a rate of 0.01. Do note that rates are percentages expressed as decimals, so a rate of 0.01 will equal 1%.
>
> ***
>
> **FRRDELTAFIX: Place an order at an implicit, static rate, relative to the FRR**\
> e.g. Given that the FRR was 0.03 at the time, placing a FRRDELTAFIX order with a rate of 0.01 will put an order on the book with a rate of 0.04 (FRR + rate).
>
> Before the order is matched, the rate updates against the FRR. Once matched, the rate becomes static and will no longer update against the FRR.
>
> The offset can be negative or positive for FRRDELTAFIX.
>
> ***
>
> **FRRDELTAVAR: Place an order at an implicit, dynamic rate, relative to the FRR**\
> e.g. Given that the FRR was 0.03 at the time, placing a FRRDELTAVAR order with a rate of 0.01 will put an order on the book with a rate of 0.04 (FRR + rate).
>
> This rate will update automatically with the FRR both on the book as well as after matching.
>
> The offset can only be positive for FRRDELTAVAR.

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
    "/auth/w/funding/offer/submit": {
      "post": {
        "summary": "Submit Funding Offer",
        "description": "Submit a new funding offer.",
        "operationId": "rest-auth-submit-funding-offer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "symbol",
                  "amount",
                  "rate",
                  "period"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "Order Type (LIMIT, FRRDELTAVAR, FRRDELTAFIX)",
                    "default": "LIMIT"
                  },
                  "symbol": {
                    "type": "string",
                    "description": "Symbol for desired pair (fUSD, fBTC, etc..)",
                    "default": "fUSD"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount (positive for offer, negative for bid)",
                    "default": "123.45"
                  },
                  "rate": {
                    "type": "string",
                    "description": "Daily rate",
                    "default": "0.001"
                  },
                  "period": {
                    "type": "integer",
                    "description": "Time period of offer. Minimum 2 days. Maximum 120 days.",
                    "default": 2,
                    "format": "int32"
                  },
                  "flags": {
                    "type": "integer",
                    "description": "Optional see https://docs.bitfinex.com/v2/docs/flag-values",
                    "default": 0,
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
                    "value": "[\n  1568713496510, //MTS\n  \"fon-req\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    604366339, //ID\n    \"fUSD\", //SYMBOL\n    1568713496502, //MTS_CREATED\n    1568713496502, //MTS_UPDATED\n    50, //AMOUNT\n    50, //AMOUNT_ORIGINAL\n    \"LIMIT\", //OFFER_TYPE\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //FLAGS\n    \"ACTIVE\", //OFFER_STATUS\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.00002, //RATE\n    2, //PERIOD\n    false, //NOTIFY\n    null, //HIDDEN\n    null, //PLACEHOLDER\n    false, //RENEW\n    null //PLACEHOLDER\n  ], //FUNDING_OFFER_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"Submitting funding offer of 50.0 USD at 0.002000 for 2 days.\" //TEXT\n]"
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
