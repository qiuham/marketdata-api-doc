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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-cancel-all-funding-offers'
updated_at: 2026-11-19
---

# Cancel All Funding Offers

Cancel all of your current funding offers. Can also be used to only cancel offers in the specified currency.

> 📘 Currency
>
> Specifying a currency is optional. If the currency param is omitted, all open offers will be cancelled.

**Response data**

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
      <td>Int</td>
      <td>Millisecond Time Stamp of the update</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>Purpose of notification ('foc_all-req' (funding offer cancel all request))</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>STATUS</td>
      <td>String</td>
      <td>Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>TEXT</td>
      <td>String</td>
      <td>Text of the notification</td>
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
    "/auth/w/funding/offer/cancel/all": {
      "post": {
        "summary": "Cancel All Funding Offers",
        "description": "Cancel all of your current funding offers. Can also be used to only cancel offers in the specified currency.",
        "operationId": "rest-auth-cancel-all-funding-offers",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "currency": {
                    "type": "string",
                    "description": "Currency for which to cancel all offers (USD, BTC, UST ...)"
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
                    "value": "[\n  1573911972518, //MTS\n  \"foc_all-req\", //TYPE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"SUCCESS\", //STATUS\n  \"All (8) submitted for cancellation; waiting for confirmation.\" //TEXT\n]\n\n"
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
