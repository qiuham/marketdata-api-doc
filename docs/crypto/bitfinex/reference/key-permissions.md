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
source_url: 'https://docs.bitfinex.com/reference/key-permissions'
updated_at: 2026-11-27
---

# Key Permissions

Retrieve current api key/token permissions

#### Response data

| Index    | Field                  | Type                                                    | Description                                              |
| :------- | :--------------------- | :------------------------------------------------------ | :------------------------------------------------------- |
| \[0...n] | KEY\_PERMISSION\_ARRAY | [Key permission array](#key-permission-arrays-index-0n) | Each index contains one of the current key's permissions |

#### Key permission arrays (index \[0...n]

| Index | Term  | Type   | Description                                                                                                                       |
| ----- | :---- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| \[0]  | SCOPE | string | Api scope, ('account', 'history',  'orders', 'positions', 'funding', 'settings', 'wallets', 'withdraw', 'ui\_withdraw', 'bfxpay') |
| \[1]  | READ  | int    | Read permission (0 - false, 1 - true)                                                                                             |
| \[2]  | WRITE | int    | Write permission (0 - false, 1 - true)                                                                                            |

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
    "/auth/r/permissions": {
      "post": {
        "summary": "Key Permissions",
        "description": "Retrieve current api key/token permissions",
        "operationId": "key-permissions",
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
                    "value": "[\n  [\n    'account', //SCOPE\n    1, //READ\n    1 //WRITE\n\t], //KEY_PERMISSION_ARRAY\n  [\n    'history', //SCOPE\n    1, //READ\n    1 //WRITE\n\t], //KEY_PERMISSION_ARRAY\n  [\n    'orders',\n    1,\n    1\n\t],\n  [\n    'positions',\n    0,\n    0\n\t],\n  [\n    'funding',\n    1,\n    1\n\t],\n  [\n    'settings',\n    0,\n    0\n\t],\n  [\n    'wallets',\n    1,\n    1\n\t],\n  [\n    'withdraw',\n    0,\n    1\n\t],\n  [\n    'ui_withdraw',\n    0,\n    0\n\t],\n  [\n    'bfxpay', \n    0, \n    0\n\t]\n]"
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
