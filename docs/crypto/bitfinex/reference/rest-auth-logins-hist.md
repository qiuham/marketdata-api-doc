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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-logins-hist'
updated_at: 2026-11-23
---

# Login History

Retrieve a list of past logins.

#### Response data

| Index    | Field              | Type                                            | Description                                                           |
| :------- | :----------------- | :---------------------------------------------- | :-------------------------------------------------------------------- |
| \[0...n] | LOGIN\_INFO\_ARRAY | [Login info array](#login-info-arrays-index-0n) | Each index contains one of the n current user's login history entries |

#### Login info arrays (index \[0...n])

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
      <td>Int</td>
      <td>Login ID</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>TIME</td>
      <td>Int</td>
      <td>Millisecond timestamp of login</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>IP</td>
      <td>String</td>
      <td>IP address of login</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>EXTRA_INFO</td>
      <td>Object</td>
      <td>Object with extra information</td>
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
    "/auth/r/logins/hist": {
      "post": {
        "summary": "Login History",
        "description": "Retrieve a list of past logins.",
        "operationId": "rest-auth-logins-hist",
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
                    "description": "Number of records (Max: 250)",
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
                    "value": "[\n  [\n  78404724, //ID\n  null, //PLACEHOLDER\n  1579202754000, //TIME\n  null, //PLACEHOLDER\n  '184.214.55.220', //IP\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  '{\"asn\": \"28545, Cablemas Telecomunicaciones SA de CV\", \"geo\": \"Cancún, MX\", \"user_agent\":   {\"os\": \"Windows 10\", \"raw\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36\", \"browser\": \"Chrome\", \"version\": \"79.0.3945.117\", \"platform\": \"Windows\", \"is_mobile\": false}}' //EXTRA_INFO\n  ], //LOGIN_INFO_ARRAY\n  ...\n]\n  "
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
