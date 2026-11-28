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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-keep-funding'
updated_at: 2026-11-28
---

# Keep Funding

Toggle to keep funding taken. Specify loan for unused funding and credit for used funding.

> 📘 Loan and credit ID's
>
> Loan or credit ID's can be retrieved through the  [Funding Loans](https://docs.bitfinex.com/reference?showHidden=94bdb#rest-auth-funding-loans) and [Funding Credits](https://docs.bitfinex.com/reference?showHidden=94bdb#rest-auth-funding-credits) endpoints.

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
      <td>Int</td>
      <td>Millisecond Time Stamp of the update</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>String</td>
      <td>Purpose of notification ('fk-req' (funding keep request))</td>
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
    "title": "api-settings-auth",
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
    "/auth/w/funding/keep": {
      "post": {
        "summary": "Keep Funding",
        "description": "Toggle to keep funding taken. Specify loan for unused funding and credit for used funding.",
        "operationId": "rest-auth-keep-funding",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "Specify the funding type ('credit' or 'loan')"
                  },
                  "id": {
                    "type": "array",
                    "description": "Pass an array of id's to toggle their keep funding status (on -> off, off -> on). If the changes object is also passed, keep funding status will change as specified in the changes object.",
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "changes": {
                    "type": "object",
                    "description": "Optional object to specify changes for each id (1 to enable, 0 to disable) ex. {1234: 1, 1235: 1, 1236: 0, ...}",
                    "properties": {}
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
                    "value": "[\n  1573914639029, //MTS\n  \"fk-req\", //TYPE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"SUCCESS\", //STATUS\n  \"Credit updated\" //TEXT\n]\n\n"
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
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": false,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
