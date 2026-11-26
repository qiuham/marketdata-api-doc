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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-withdraw'
updated_at: 2026-11-26
---

# Withdrawal

Allows you to request a withdrawal from one of your wallets.

> 📘 Withdrawal methods
>
> A full list of all withdrawal methods, including the different methods for tether withdrawals, can be found here: <https://api-pub.bitfinex.com//v2/conf/pub:map:tx:method>
>
> Tether can be withdrawn using different networks. Different methods are used to specify which network should be used. The table below specifies which methods need to be used to use different networks.

> 📘 Travel rule
>
> The 'travel\_rule\_tos' field can be used to voluntarily send travel rule information when requesting a withdrawal.
>
> Pass the virtual asset provider ID and name by passing the 'vasp\_did' and 'vasp\_name' respective. For possible values, see the documentation of the [Virtual Asset Service Providers](https://docs.bitfinex.com/reference/virtual-asset-service-providers) endpoint.

**Tether Methods**

| Currency | Transport Protocol                 | Method         |
| -------- | ---------------------------------- | -------------- |
| USDT     | Tether(USD) on Ethereum            | tetheruse      |
| USDT     | Tether(USD) on Tron                | tetherusx      |
| USDT     | Tether(USD) on Liquid              | tetherusl      |
| USDT     | Tether(USD) on Omni                | tetheruso      |
| USDT     | Tether(USD) on Solana              | tetherusdtsol  |
| USDT     | Tether(USD) on Avalanche (C Chain) | tetherusdtavax |
| USDT     | Tether(USD) on Algorand            | tetherusdtalg  |
| USDT     | Tether(USD) on Polkadot            | tetherusdtdot  |
| USDT     | Tether(USD) on Kusama              | tetherusdtksm  |
| USDT     | Tether(USD) on EOS                 | tetheruss      |
| USDT     | Tether(USD) on NEAR                | tetherusdtnear |
| USDT     | Tether(USD) on Polygon             | tetherusdtply  |
| USDT     | Tether(USD) on Bitcoin Cash        | tetherusdtbch  |
| USDT     | Tether(USD) on Tezos               | tetherusdtxtz  |
| USDT     | Tether(USD) on KAVA                | tetherusdtkava |
| USDT     | Tether(USD) on zkSync              | tetherusdtzk   |
| USDT     | Tether(USD) on Celo                | tetherusdtcelo |
| USDT     | Tether(USD) on Toncoin             | tetherusdtton  |
| EURT     | Tether(EUR) on Ethereum            | tethereue      |
| CNHT     | Tether(CNH) on Ethereum            | tethercnhte    |
| CNHT     | Tether(CNH) on Huobi Token         | tethercnhtx    |
| XAUT     | Tether(XAU) on Ethereum            | tetherxaute    |
| XAUT     | Tether(XAU) on zkSync              | tetherxautzk   |
| MXNT     | Tether(MXN) on Ethereum            | tethermxnte    |

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
      <td>Notification's type ("acc_wd-req")</td>
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
      <td>WITHDRAWAL_ARRAY</td>
      <td><a href="#withdrawal-array-index-4">Withdrawal array</a></td>
      <td>An array containing your withdrawal data</td>
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

#### Withdrawal array (Index \[4])

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
      <td>WITHDRAWAL_ID</td>
      <td>Int</td>
      <td>Unique Withdrawal ID (0 or null if the withdrawal was unsuccessful)</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>METHOD</td>
      <td>String</td>
      <td>Method of withdrawal</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>PAYMENT_ID</td>
      <td>String</td>
      <td>Payment ID (if relevant)</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>WALLET</td>
      <td>String</td>
      <td>Sending wallet</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>AMOUNT</td>
      <td>Float</td>
      <td>Amount of the withdrawal</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>WITHDRAWAL_FEE</td>
      <td>Float</td>
      <td>Fee on withdrawal</td>
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
    "/auth/w/withdraw": {
      "post": {
        "summary": "Withdrawal",
        "description": "Allows you to request a withdrawal from one of your wallets.",
        "operationId": "rest-auth-withdraw",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "wallet",
                  "method"
                ],
                "properties": {
                  "wallet": {
                    "type": "string",
                    "description": "Select the wallet from which to transfer (exchange, margin, funding (can also use the old labels which are exchange, trading and deposit respectively))",
                    "default": "trading"
                  },
                  "method": {
                    "type": "string",
                    "description": "Method of withdrawal. For an up-to-date mapping of methods and their respective currencies see: https://api-pub.bitfinex.com//v2/conf/pub:map:tx:method [[[METHOD,[CURRENCY]]...]]  *(methods should be added to the post body in lower case)",
                    "default": "bitcoin"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount of Withdrawal (not used for LNX)",
                    "default": "1234"
                  },
                  "address": {
                    "type": "string",
                    "description": "Destination address (not used for LNX)",
                    "default": "xxxx1234"
                  },
                  "invoice": {
                    "type": "string",
                    "description": "Used instead of address for LNBTC (method: 'lnx')"
                  },
                  "payment_id": {
                    "type": "string",
                    "description": "Specify a tag/memo/etc."
                  },
                  "fee_deduct": {
                    "type": "integer",
                    "description": "Set to 1 to deduct the withdrawal fee from the withdrawal amount",
                    "default": 0,
                    "format": "int32"
                  },
                  "note": {
                    "type": "string",
                    "description": "Add an optional note to your withdrawal"
                  },
                  "travel_rule_tos": {
                    "type": "boolean",
                    "description": "Flag to voluntarily send travel rule details for withdrawal"
                  },
                  "vasp_did": {
                    "type": "string",
                    "description": "Virtual asset provider identifier, optional info for travel rule purpose. DID values can be found on https://api-pub.bitfinex.com/v2/ext/vasps endpoint."
                  },
                  "vasp_name": {
                    "type": "string",
                    "description": "Virtual asset provider name, optional info for travel rule purpose, if self custody ignore the field"
                  },
                  "beneficiary_self": {
                    "type": "boolean",
                    "description": "Set to 'true' to extract destination data from your KYC data. (If 'true', dest_firstname, dest_lastname, or dest_corp_name do not need to be supplied)"
                  },
                  "dest_firstname": {
                    "type": "string",
                    "description": "Destination entity first name for travel rule purpose (mandatory if dest_lastname is supplied, not required if beneficiary_self = true)"
                  },
                  "dest_lastname": {
                    "type": "string",
                    "description": "Destination entity last name for travel rule purpose (mandatory if dest_firstname is supplied, not required if beneficiary_self = true)"
                  },
                  "dest_corp_name": {
                    "type": "string",
                    "description": "Destination entity corporate name for travel rule purpose. (use either dest_firstname + dest_lastname or dest_corp_name, not required if beneficiary_self = true)"
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
                    "value": "[\n  1568742390999, //MTS\n  \"acc_wd-req\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    13080092, //WITHDRAWAL_ID\n    null, //PLACEHOLDER\n    \"ethereum\", //METHOD\n    null, //PAYMENT_ID\n    \"exchange\", //WALLET\n    0.01, //AMOUNT\n    null, //PLACEHOLDER\n    null, //PLACEHOLDER\n    0.00135 //WITHDRAWAL_FEE\n  ], //WITHDRAWAL_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"Your withdrawal request has been successfully submitted.\" //TEXT\n]"
                  }
                },
                "schema": {
                  "type": "array"
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
