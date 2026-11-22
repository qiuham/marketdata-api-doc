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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-transfer'
updated_at: 2026-11-22
---

# Transfer Between Wallets

Transfer funds between wallets. This endpoint can also be used to convert USDT to USDT0 for derivatives trading.

#### Response data

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
      <td>int</td>
      <td>Seconds epoch timestamp of notification</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>string</td>
      <td>Notification's type ("on-req")</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MESSAGE_ID</td>
      <td>int</td>
      <td>Unique notification's ID</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[4]</td>
      <td>TRANSFER_ARRAY</td>
      <td><a href="#transfer-array-index-4">TRANSFER_ARRAY</a></td>
      <td>An array containing details of the transfer/conversion</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>CODE</td>
      <td>int</td>
      <td>W.I.P. (work in progress)</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>TEXT</td>
      <td>string</td>
      <td>Additional notification description</td>
    </tr>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb
  }
  
  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

#### Transfer array (index \[4])

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
      <td>MTS_UPDATED</td>
      <td>Int</td>
      <td>Millisecond Time Stamp of the update</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>WALLET_FROM</td>
      <td>String</td>
      <td>Starting wallet</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>WALLET_TO</td>
      <td>String</td>
      <td>Destination wallet</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>CURRENCY</td>
      <td>String</td>
      <td>Currency</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>CURRENCY_TO</td>
      <td>String</td>
      <td>Currency converted to</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>AMOUNT</td>
      <td>Int</td>
      <td>Amount of Transfer</td>
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

> 📘 Derivatives Wallet
>
> Note that the margin wallet, for Derivative symbols, is the derivatives wallet. If the destination is 'margin' and the currency\_to is 'USTF0', the funds will end up in the derivatives wallet.

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
    "/auth/w/transfer": {
      "post": {
        "summary": "Transfer Between Wallets",
        "description": "Transfer funds between wallets. This endpoint can also be used to convert USDT to USDT0 for derivatives trading.",
        "operationId": "rest-auth-transfer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "from",
                  "to",
                  "currency",
                  "amount"
                ],
                "properties": {
                  "from": {
                    "type": "string",
                    "description": "Select the wallet from which to transfer (exchange, margin, funding (can also use the old labels which are exchange, trading and deposit respectively))",
                    "default": "trading"
                  },
                  "to": {
                    "type": "string",
                    "description": "Select the wallet to transfer to (exchange, margin, funding (can also use the old labels which are exchange, trading and deposit respectively))",
                    "default": "exchange"
                  },
                  "currency": {
                    "type": "string",
                    "description": "Select the currency that you would like to transfer (USD, UST, BTC, ....)",
                    "default": "UST"
                  },
                  "currency_to": {
                    "type": "string",
                    "description": "Select the currency that you would like to exchange to (USTF0 === USDT for derivatives pairs)",
                    "default": "USTF0"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Select the amount to transfer",
                    "default": "123.45"
                  },
                  "email_dst": {
                    "type": "string",
                    "description": "Allows transfer of funds to a sub- or master-account identified by the associated email address."
                  },
                  "user_id_dst": {
                    "type": "integer",
                    "description": "Allows transfer of funds to a sub- or master-account identified by the associated user id.",
                    "format": "int32"
                  },
                  "tfaToken": {
                    "type": "object",
                    "description": "Required only when email_dst or user_id_dst is present and auth token is used instead of api credentials",
                    "required": [
                      "method"
                    ],
                    "properties": {
                      "method": {
                        "type": "string",
                        "description": "2FA method used, could be one of otp or u2f"
                      },
                      "token": {
                        "type": "string",
                        "description": "OTP 6 digits, use this only when otp method is used"
                      },
                      "response": {
                        "type": "object",
                        "description": "Webauthn assertation challenge response, use when method is u2f",
                        "required": [
                          "id"
                        ],
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "Base64 url safe encoded buffe"
                          },
                          "response": {
                            "type": "object",
                            "required": [
                              "authenticatorData",
                              "clientDataJSON",
                              "signature"
                            ],
                            "properties": {
                              "authenticatorData": {
                                "type": "string",
                                "description": "Base64 url safe encoded buffer"
                              },
                              "clientDataJSON": {
                                "type": "string",
                                "description": "Base64 url safe encoded buffer"
                              },
                              "signature": {
                                "type": "string",
                                "description": "Base64 url safe encoded buffer"
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
                    "value": "//Transfer    \n[\n  1568736745789, //MTS\n  \"acc_tf\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    1568736745790, //MTS_UPDATE\n    \"margin\", //WALLET_FROM\n    \"exchange\", //WALLET_TO\n    null, //PLACEHOLDER\n    \"USD\", //CURRENCY\n    null, //CURRENCY_TO\n    null, //PLACEHOLDER\n    50 //AMOUNT\n  ], //TRANSFER_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"50.0 US Dollar transferred from Margin to Exchange\" //TEXT\n]\n\n//Transfer and conversion to USDT0\n[\n  1574173088379, //MTS\n  \"acc_tf\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    1574173088379, //MTS_UPDATE\n    \"exchange\", //WALLET_FROM\n    \"margin\", //WALLET_TO\n    null, //PLACEHOLDER\n    \"UST\", //CURRENCY\n    \"USTF0\", //CURRENCY_TO\n    null, //PLACEHOLDER\n    200 //AMOUNT\n  ], //TRANSFER_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"200.0 Tether USDt transfered from Exchange to Margin\" //TEXT\n]\n"
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
