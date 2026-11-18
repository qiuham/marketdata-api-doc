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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-funding-close'
updated_at: 2026-11-18
---

# Funding Close

Return Taken "Used" or "Unused" funding.

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
      <td>Int</td>
      <td>Millisecond Time Stamp of the update</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>Purpose of notification ('on-req', 'oc-req', 'uca', 'fon-req', 'foc-req')</td>
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
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
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

> 🚧 Offer ID
>
> Please note that the Offer ID needed is not the one received from the initial offer submission response. The Offer ID should be retrieved via the [Funding Loans](https://docs.bitfinex.com/v2/reference#rest-auth-funding-loans) and [Funding Credits](https://docs.bitfinex.com/reference#rest-auth-funding-credits) endpoints.

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
    "/auth/w/funding/close": {
      "post": {
        "summary": "Funding Close",
        "description": "Return Taken \"Used\" or \"Unused\" funding.",
        "operationId": "rest-auth-funding-close",
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
                    "description": "Offer ID (retrievable via the [Funding Loans](https://docs.bitfinex.com/v2/reference#rest-auth-funding-loans) and [Funding Credits](https://docs.bitfinex.com/reference#rest-auth-funding-credits) endpoints)",
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
                    "value": "[\n  1574075056449, //MTS\n  \"fr-req\", //TYPE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"SUCCESS\",  //STATUS\n  null //PLACEHOLDER\n]"
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
