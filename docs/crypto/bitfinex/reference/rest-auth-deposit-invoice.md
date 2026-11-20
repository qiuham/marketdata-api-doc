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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-deposit-invoice'
updated_at: 2026-11-20
---

# Generate Invoice

Generates a Lightning Network deposit invoice

> ❗️ Creating a deposit address
>
> If this is the first time you are generating an LNX invoice on your account, you will first need to create a deposit address. To do this, call w/deposit/address  with \{ method: 'LNX', wallet: 'exchange' }

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
      <td>INVOICE_HASH</td>
      <td>String</td>
      <td>Hashed invoice</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>INVOICE</td>
      <td>String</td>
      <td>Requested invoice</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>AMOUNT</td>
      <td>String</td>
      <td>Amount of invoice</td>
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
    "/auth/w/deposit/invoice": {
      "post": {
        "summary": "Generate Invoice",
        "description": "Generates a Lightning Network deposit invoice",
        "operationId": "rest-auth-deposit-invoice",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "wallet",
                  "currency",
                  "amount"
                ],
                "properties": {
                  "wallet": {
                    "type": "string",
                    "description": "Select the wallet that will receive the invoice payment. Currently only 'exchange' is available",
                    "default": "exchange"
                  },
                  "currency": {
                    "type": "string",
                    "description": "Select the currency for which you wish to generate an invoice. Currently only LNX (Bitcoin Lightning Network) is available.",
                    "default": "LNX"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount that you wish to deposit (in BTC; min 0.000001, max 0.02)",
                    "default": "0"
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
                    "value": "[\n  '9a0f8079e7aca10ccef8db7ea860485b25d56b89157c33567ee8a037c5b6d658', //IHVOICE_HASH\n  'lnbc10m1p0rn2fkpp5ng8cq7084jssenhcmdl2sczgtvja26ufz47rx4n7azsr03dk6evqdp5xy6kzwfsvfjrzd3cxcux2wfexcmrxcek8psnjdpkvyurxef38y6scqzpgxqzjcyrp0kymmeqejdelm3r586ehz5cs5ntxx96hr3ec49q70rlnljzcpag5pynsalrwmd0w8serwmmtjru6g6z3a607kqw47mqgm6m4ztkqqxgkujx', //INVOICE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  '0.01' //AMOUNT\n]"
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
