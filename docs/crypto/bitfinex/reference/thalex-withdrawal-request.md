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
source_url: 'https://docs.bitfinex.com/reference/thalex-withdrawal-request'
updated_at: 2026-11-27
---

# Thalex Withdrawal Request

Withdraw from Thalex to Bitfinex

#### Response data

| Key         | Type    | Description                               |
| :---------- | :------ | :---------------------------------------- |
| type        | String  | Specifies the transfer type: "withdrawal" |
| addressDest | String  | Specifies the address for the transaction |
| amount      | String  | Amount of the withdrawal                  |
| ccy         | String  | Currency withdrawn                        |
| createdAt   | Integer | Withdrawal creation timestamp             |
| updatedAt   | Integer | Withdrawal update timestamp               |
| id          | string  | Withdrawal id                             |
| status      | string  | Withdrawal status                         |
| fee         | string  | Fee charged for the withdrawal            |

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
    "/auth/w/ext/wallets/withdrawals/request": {
      "post": {
        "summary": "Thalex Withdrawal Request",
        "description": "Withdraw from Thalex to Bitfinex",
        "operationId": "thalex-withdrawal-request",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "provider",
                  "amount",
                  "ccy",
                  "tfaToken"
                ],
                "properties": {
                  "provider": {
                    "type": "string",
                    "description": "Specify the provider ('thalex')",
                    "default": "thalex"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount to withdraw from Thalex to Bitfinex"
                  },
                  "ccy": {
                    "type": "string",
                    "description": "Currency to withdraw from Thalex (allowed values: 'USE', 'ETH', 'BTC')"
                  },
                  "tfaToken": {
                    "type": "object",
                    "description": "Provide a tfaToken object to validate the request with U2F 2FA",
                    "required": [
                      "method"
                    ],
                    "properties": {
                      "method": {
                        "type": "string",
                        "description": "'otp' or 'u2f'"
                      },
                      "token": {
                        "type": "string",
                        "description": "Only used when method is 'otp'. Provide otp as a string. (e.g. '123456')"
                      },
                      "response": {
                        "type": "object",
                        "description": "Only used when method is 'u2f'. Used to pass assertion result. ([ref](https://webauthn-open-source.github.io/fido2-lib/Fido2Lib.html#assertionResult))",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "The base64url encoded id returned by the client"
                          },
                          "rawId": {
                            "type": "string",
                            "description": "The base64url encoded rawId returned by the client. If res.rawId is missing, res.id will be used instead. If both are missing an error will be thrown."
                          },
                          "response": {
                            "type": "object",
                            "description": "Client response",
                            "required": [
                              "clientDataJSON",
                              "attestationObject",
                              "signature"
                            ],
                            "properties": {
                              "clientDataJSON": {
                                "type": "string",
                                "description": "The base64url encoded clientDataJSON returned by the client"
                              },
                              "attestationObject": {
                                "type": "string",
                                "description": "The base64url encoded authenticatorData returned by the client"
                              },
                              "signature": {
                                "type": "string",
                                "description": "The base64url encoded signature returned by the client"
                              },
                              "userHandle": {
                                "type": "string",
                                "description": "The base64url encoded userHandle returned by the client. May be null or an empty string."
                              }
                            }
                          }
                        }
                      }
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
                    "value": "{\n    \"type\": \"withdraw\",\n    \"addressDest\": \"0x1d341cR1512C6s1984da95C15BfF2B9F3A29345e1\",\n    \"amount\": \"90\",\n    \"ccy\": \"USE\",\n    \"createdAt\": 1732126385718,\n    \"updatedAt\": 1732126385718,\n    \"id\": \"f70a4286-6f7c-4af8-931f-3e89f74ebdf3\",\n    \"status\": \"PENDING\",\n    \"fee\": \"0\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "withdraw"
                    },
                    "addressDest": {
                      "type": "string",
                      "example": "0x1d341cR1512C6s1984da95C15BfF2B9F3A29345e1"
                    },
                    "amount": {
                      "type": "string",
                      "example": "90"
                    },
                    "ccy": {
                      "type": "string",
                      "example": "USE"
                    },
                    "createdAt": {
                      "type": "integer",
                      "example": 1732126385718,
                      "default": 0
                    },
                    "updatedAt": {
                      "type": "integer",
                      "example": 1732126385718,
                      "default": 0
                    },
                    "id": {
                      "type": "string",
                      "example": "f70a4286-6f7c-4af8-931f-3e89f74ebdf3"
                    },
                    "status": {
                      "type": "string",
                      "example": "PENDING"
                    },
                    "fee": {
                      "type": "string",
                      "example": "0"
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
                    "value": "[\n  \"error\",\n  null,\n  \"ERR_WRONG_AMOUNT\"\n]\n\n/*\nList of possible errors\n\nERR_ERR_PROVIDER_UNK - wrong provider value\nERR_NOT_FOUND_USER - user has not onboarded\nERR_NOT_ALLOWED - onboarding was not completed\nERR_CCY_UNK - ccy value is not supported\nERR_WRONG_AMOUNT - amount value has not passed validation\nERR_FAILED - failed to request deposit due to internal error\nERR_INTERNAL - failed to process request due to unexpected error\n\n*/"
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
