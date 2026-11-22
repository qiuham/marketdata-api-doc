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
source_url: 'https://docs.bitfinex.com/reference/thalex-free-transfer-count'
updated_at: 2026-11-22
---

# Thalex Free Transfer Count

Get information about free transfers and their renewal. Users are eligible for two free deposits every 24 hours.

#### Response data

| Key                   | Type              | Description                                                                                  |
| :-------------------- | :---------------- | :------------------------------------------------------------------------------------------- |
| deposits.available    | Integer           | Number of free deposits available                                                            |
| deposits.resetsAt     | Integer \|\| null | Timestamp at which the number of free deposits resets (defaults to null if not available)    |
| withdrawals.available | Integer           | Number of free withdrawals available                                                         |
| withdrawals.resetsAt  | Integer \|\| null | Timestamp at which the number of free withdrawals resets (defaults to null if not available) |

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
    "/auth/r/ext/wallets/transfers/free/count": {
      "post": {
        "summary": "Thalex Free Transfer Count",
        "description": "Get information about free transfers and their renewal. Users are eligible for two free deposits every 24 hours.",
        "operationId": "thalex-free-transfer-count",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "Provider"
                ],
                "properties": {
                  "Provider": {
                    "type": "string",
                    "description": "Specify the provider ('thalex')",
                    "default": "thalex"
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
                    "value": "{\n    \"deposits\": {\n        \"available\": 1,\n        \"resetsAt\": 1732147200000\n    },\n    \"withdrawals\": {\n        \"available\": 0,\n        \"resetsAt\": null\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "deposits": {
                      "type": "object",
                      "properties": {
                        "available": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "resetsAt": {
                          "type": "integer",
                          "example": 1732147200000,
                          "default": 0
                        }
                      }
                    },
                    "withdrawals": {
                      "type": "object",
                      "properties": {
                        "available": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "resetsAt": {}
                      }
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "500",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  \"error\",\n  null,\n  \"ERR_WRONG_AMOUNT\"\n]\n\n/*\nList of possible errors\n\nERR_INTERNAL - failed to process request due to unexpected error\nERR_NOT_FOUND_USER - user has not onboarded\nERR_NOT_ALLOWED - onboarding was not completed\nERR_ERR_PROVIDER_UNK - wrong provider value"
                  }
                },
                "schema": {
                  "type": "array"
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
