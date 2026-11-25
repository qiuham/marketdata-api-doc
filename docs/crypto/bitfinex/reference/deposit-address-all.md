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
source_url: 'https://docs.bitfinex.com/reference/deposit-address-all'
updated_at: 2026-11-25
---

# Deposit Address List

Retrieve all deposit addresses for a specific currency.

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
      <td>ADDRESS</td>
      <td>string</td>
      <td>Deposit address (instead of the address, this field will show Tag/Memo/Payment_ID for currencies that require it)</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>WALLET_TYPE</td>
      <td>string</td>
      <td>Wallet type, e.g. "funding"</td>
    </tr>
  </tbody>
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

#### Deposit address arrays (Index \[4])**Ratelimit**: 10 req/min

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
    "/auth/r/deposit/address/all": {
      "post": {
        "summary": "Deposit Address List",
        "description": "Retrieve all deposit addresses for a specific currency.",
        "operationId": "deposit-address-all",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "method"
                ],
                "properties": {
                  "method": {
                    "type": "string",
                    "description": "Method of deposit (methods accepted: “bitcoin”, “litecoin”, “ethereum”, “tetheruso\", “tetherusl\", “tetherusx\", “tetheruss\", \"ethereumc\", \"zcash\", \"monero\", \"iota\"). For an up-to-date listing of supported currencies see: https://api-pub.bitfinex.com//v2/conf/pub:map:tx:method"
                  },
                  "page": {
                    "type": "integer",
                    "description": "Page cursor, default 1",
                    "format": "int32"
                  },
                  "pageSize": {
                    "type": "integer",
                    "description": "Number of items per page, should be between 20-100, default is 20",
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
                    "value": "[\n  [\n    ADDRESS, //PLACEHOLDER\n    WALLET_TYPE\n  ]\n]\n\n[[\"0x6C20eBD2222CE0F809713EF06AE400C2445B72B7\",\"exchange\"],[\"0xcd752F90494d103F993aB91472129e9DF4987ED0\",\"margin\"],[\"0x01Dd2e1E9bE8C4667C645c8FA694aB89B894d734\",\"exchange\"],[\"0x542BECa0Fc09d2478118b0E777Ee2928F01acC0a\",\"funding\"]]"
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
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/deposit/address/all'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    method: \"TETHERUSE\", // USDt over ERC-20\n    page: 3,\n    pageSize: 25\n  }),\n  headers: {\n    /* auth headers */\n  }\n})\n  .then(res => res.json())\n  .then(json => console.log(json))\n  .catch(err => {\n    console.log(err)\n  })"
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
