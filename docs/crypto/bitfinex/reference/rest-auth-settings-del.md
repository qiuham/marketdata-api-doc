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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-settings-del'
updated_at: 2026-11-23
---

# User Settings Delete

Allows you to delete custom settings.

**Body Fields**

| Term     | Type  | Description                                                                     |
| -------- | ----- | ------------------------------------------------------------------------------- |
| Settings | Array | Array of keys to be deleted. Must follow regex pattern `/^api:[A-Za-z0-9_-]*$/` |

**Response Fields**

| Term      | Type   | Description                                                                      |
| --------- | ------ | -------------------------------------------------------------------------------- |
| TIMESTAMP | int    | Timestamp in milliseconds                                                        |
| TYPE      | string | Purpose of notification ('acc\_sd' (account settings del))                       |
| STATUS    | string | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...) |

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
    "/auth/w/settings/del": {
      "post": {
        "summary": "User Settings Delete",
        "description": "Allows you to delete custom settings.",
        "operationId": "rest-auth-settings-del",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  TIMESTAMP,\n  TYPE,\n  PLACEHOLDER,\n  PLACEHOLDER,\n\t[\n    PLACEHOLDER\n  ],\n  PLACEHOLDEr,\n  STATUS\n  PLACEHOLDER\n ]\n\n[ 1617005634199, 'acc_sd', null, null, [ 1 ], null, 'SUCCESS', null ]"
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
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/w/settings/del'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    keys: ['api:key1', 'api:key2']\n  \t}),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })\n",
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
