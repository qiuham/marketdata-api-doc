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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-deposit-address'
updated_at: 2026-11-28
---

# Deposit Address

Retrieve your deposit address or generate a new deposit address for a specific currency and wallet.

> 📘 Tag/Memo/Payment\_ID
>
> For currencies that require a tag, memo, or payment ID, the endpoint will provide these. The deposit address cannot be retrieved through this endpoint, but you can find it on your deposit page on the website. The deposit address is always the same; the tag, memo, or payment ID is used to direct your deposit to the correct account and wallet.

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
      <td>DEPOSIT_ADDRESS_ARRAY</td>
      <td><a href="#deposit-address-arrays-index-4">Deposit address array</a></td>
      <td>An array containing deposit adddress data</td>
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

#### Deposit address arrays (Index \[4])

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
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>METHOD</td>
      <td>String</td>
      <td>Method of deposit</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>CURRENCY_CODE</td>
      <td>String</td>
      <td>Currency code of new address</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>ADDRESS</td>
      <td>String</td>
      <td>Deposit address (instead of the address, this field will show Tag/Memo/Payment_ID for currencies that require it)</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>POOL_ADDRESS</td>
      <td>String</td>
      <td>Pool address (for currencies that require a Tag/Memo/Payment_ID)</td>
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

> 📘 Address Limit
>
> Please note that you may generate up to 15 addresses in total per currency per month.

**Ratelimit**: 10 req/min

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
    "/auth/w/deposit/address": {
      "post": {
        "summary": "Deposit Address",
        "description": "Retrieve your deposit address or generate a new deposit address for a specific currency and wallet.",
        "operationId": "rest-auth-deposit-address",
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
                    "description": "Method of deposit (methods accepted: “bitcoin”, “litecoin”, “ethereum”, “tetheruso\", “tetherusl\", “tetherusx\", “tetheruss\", \"ethereumc\", \"zcash\", \"monero\", \"iota\"). For an up-to-date listing of supported currencies see: https://api-pub.bitfinex.com//v2/conf/pub:map:tx:method",
                    "default": "bitcoin"
                  },
                  "op_renew": {
                    "type": "integer",
                    "description": "Input 1 to generate a new deposit address (old addresses remain valid). Defaults to 0 if omitted, which will return the existing deposit address",
                    "default": 0,
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
                    "value": "[\n  1568738594687, //MTS\n  \"acc_dep\", //TYPE\n  null, //MESSAGE_ID\n  null, //PLACEHOLDER\n  [\n    null, //PLACEHOLDER\n    \"BITCOIN\", //METHOD\n    \"BTC\", //CURRENCY_CODE\n    null, //PLACEHOLDER\n    \"YOURADDRESS\", //ADDRESS\n    null //POOL_ADDRESS\n  ], //DEPOSIT_ADDRESS_ARRAY\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"success\" //TEXT\n]"
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
