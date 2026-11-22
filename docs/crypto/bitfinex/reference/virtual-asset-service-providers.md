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
source_url: 'https://docs.bitfinex.com/reference/virtual-asset-service-providers'
updated_at: 2026-11-22
---

# Virtual Asset Service Providers

Returns a list of VASP names along with their respective ID

> 📘 Travel Rule
>
> The endpoint can be used to lookup the ID of a VASP.
>
> This ID is the VASP "Decentralised ID" and can be applied to the `vasp_did`field to identify the recipient VASP for Travel Rule purposes when making a withdrawal request.
>
> For details, see the documentation for the [Withdrawal](https://docs.bitfinex.com/reference/rest-auth-withdraw) endpoint.

#### Response data

| Index    | Field        | Type   | Description                  |
| :------- | :----------- | :----- | :--------------------------- |
| \[0...n] | VASP\_OBJECT | Object | Object with VASP name and ID |

#### VASP objects (index \[0...n])

| Key  | Type   | Description |
| :--- | :----- | :---------- |
| id   | String | VASP ID     |
| name | String | VASP name   |

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
    "/ext/vasps": {
      "get": {
        "summary": "Virtual Asset Service Providers",
        "description": "Returns a list of VASP names along with their respective ID",
        "operationId": "virtual-asset-service-providers",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": \"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1\",\n    \"name\": \"1xbet\" \n  }, // VASP_OBJECT\n  ...\n]"
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
        "security": []
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
