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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-settings-set'
updated_at: 2026-11-24
---

# User Settings Write

Allows you to create custom settings by creating key: value pairs.

**Body Fields**

| Term     | Type   | Description                                                                             |
| -------- | ------ | --------------------------------------------------------------------------------------- |
| Settings | Object | Object of keys and values to be set. Must follow regex pattern `/^api:[A-Za-z0-9_-]*$/` |

**Response Fields**

| Term                 | Type   | Description                                                                      |
| -------------------- | ------ | -------------------------------------------------------------------------------- |
| TIMESTAMP            | int    | Timestamp in milliseconds                                                        |
| TYPE                 | string | Purpose of notification ('acc\_ss' (account settings set))                       |
| NUMBER\_OF\_SETTINGS | string | Number of settings changed or created with this request                          |
| STATUS               | string | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...) |

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
    "/auth/w/settings/set": {
      "post": {
        "summary": "User Settings Write",
        "description": "Allows you to create custom settings by creating key: value pairs.",
        "operationId": "rest-auth-settings-set",
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
                    "value": "[\n  TIMESTAMP,\n  TYPE,\n  PLACEHOLDER,\n  PLACEHOLDER,\n  [\n    NUMBER_OF_SETTINGS\n  ]\n  PLACEHOLDER,\n  STATUS,\n  PLACEHOLDER\n]\n\n[ 1574340932016, 'acc_ss', null, null, [ 2 ], null, 'SUCCESS', null ]"
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
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = `v2/auth/w/settings/set` \n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    \tsettings: { 'api:key1': 'foo', 'api:key2': { bar: 2 } }\n  \t}),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })\n",
              "name": "JavaScript"
            }
          ],
          "samples-languages": [
            "javascript"
          ]
        }
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
