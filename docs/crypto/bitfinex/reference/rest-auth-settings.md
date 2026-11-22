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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-settings'
updated_at: 2026-11-22
---

# User Settings Read

Allows you to read custom settings by providing a key. You can set or adjust these settings using the [User Settings Write](https://docs.bitfinex.com/reference#user-settings-set) endpoint.

**Body Fields**

| Term | Type  | Description                                                                 |
| ---- | ----- | --------------------------------------------------------------------------- |
| Keys | Array | Array of keys requested. Must follow regex pattern `/^api:[A-Za-z0-9_-]*$/` |

**Returned Fields**

| Term  | Type         | Description      |
| ----- | ------------ | ---------------- |
| KEY   | String       | Requested Key    |
| VALUE | Self defined | Returned setting |

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
    "/auth/r/settings": {
      "post": {
        "summary": "User Settings Read",
        "description": "Allows you to read custom settings by providing a key. You can set or adjust these settings using the [User Settings Write](https://docs.bitfinex.com/reference#user-settings-set) endpoint.",
        "operationId": "rest-auth-settings",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "keys"
                ],
                "properties": {
                  "keys": {
                    "type": "array",
                    "description": "The keys for which you wish to retrieve the values.",
                    "items": {
                      "type": "string"
                    }
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
                    "value": "[\n  [\n    KEY\n    VALUE\n  ],\n  ...\n]\n  \n[ [ 'bit', 'finex' ] ]"
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
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/settings'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    keys: [ 'api:key1' ]\n  \t}),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })\n",
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
