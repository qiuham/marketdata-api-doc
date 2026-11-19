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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-audit-hist'
updated_at: 2026-11-19
---

# Changelog

Retrieve account changelog.

#### Response data

| Index    | Field            | Type                                         | Description                                                       |
| :------- | :--------------- | :------------------------------------------- | :---------------------------------------------------------------- |
| \[0...n] | CHANGELOG\_ARRAY | [Changelog array](#changelog-array-index-0n) | Each index contains one of the n current user's changelog entries |

#### Changelog array (Index \[0...n])

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
      <td>MTS_CREATE</td>
      <td>Int</td>
      <td>Millisecond timestamp of change</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>LOG</td>
      <td>String</td>
      <td>Log entry</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>IP</td>
      <td>String</td>
      <td>IP address for logged change</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>USER_AGENT</td>
      <td>Object</td>
      <td>Browser info</td>
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
    "/auth/r/audit/hist": {
      "post": {
        "summary": "Changelog",
        "description": "Retrieve account changelog.",
        "operationId": "rest-auth-audit-hist",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start": {
                    "type": "integer",
                    "description": "Millisecond start time",
                    "format": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "description": "Millisecond end time",
                    "format": "int64"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records (Max: 500)",
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
                    "value": "[\n  [\n    1574332100000, //MTS_CREATE\n    null, //PLACEHOLDER\n    'settings: api key created', //LOG\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    '182.64.34.9', //IP\n    'Mozilla/5.0 (X11; CrOS x86_64 12499.51.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.92 Safari/537.36' //USER_AGENT\n  ],\n  ...\n]\n  "
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
