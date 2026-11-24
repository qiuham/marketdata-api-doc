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
source_url: 'https://docs.bitfinex.com/reference/lnx-invoice-payments'
updated_at: 2026-11-24
---

# LNX Invoice Payments

Retrieve invoice and payment data

#### Response data

| Term                | Type   | Description                                         |
| ------------------- | ------ | --------------------------------------------------- |
| PAYMENT\_HASH       | string | Payment hash                                        |
| CREATED\_AT         | int    | Invoice created timestamp in milliseconds           |
| INVOICE\_EXPIRY     | int    | Optional, invoice expired timestamp in milliseconds |
| INVOICE             | string | LNX invoice                                         |
| RECIPIENT\_PUB\_KEY | string | Recipient public key                                |
| MEMO                | string | Optional, invoice memo                              |
| AMOUNT              | number | Amount in satoshis                                  |
| BFX\_AMOUNT         | string | Amount in BTC                                       |
| STATUS              | string | Invoice/payment status                              |

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
    "/auth/r/ext/invoice/payments": {
      "post": {
        "summary": "LNX Invoice Payments",
        "description": "Retrieve invoice and payment data",
        "operationId": "lnx-invoice-payments",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "action",
                  "query"
                ],
                "properties": {
                  "action": {
                    "type": "string",
                    "description": "Query action, use one of getPaymentsByUser, getInvoicesByUser, getInvoiceById, getPaymentById"
                  },
                  "query": {
                    "type": "object",
                    "description": "Query params",
                    "properties": {
                      "offset": {
                        "type": "integer",
                        "description": "Optional offset, supported only by getInvoicesByUser and getPaymentsByUser actions",
                        "format": "int32"
                      },
                      "txid": {
                        "type": "string",
                        "description": "Optional payment hash, required by getInvoiceById and getPaymentById actions"
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
                    "value": "// getInvoicesByUser\n{\n  \"invoices\": [\n    {\n      \"payment_hash\": PAYMENT_HASH,\n      \"created_at\": CREATED_AT_MTS,\n      \"invoice_expiry\": INVOICE_EXPIRY_MTS,\n      \"invoice\": INVOICE,\n      \"recipient_pub_key\": RECIPIENT_PUB_KEY,\n      \"memo\": MEMO,\n      \"amount\": AMOUNT_SAT,\n      \"bfx_amount\": AMOUNT_BFX,\n      \"state\": STATUS\n    }\n  ]\n}\n\n// getPaymentsByUser\n{\n  \"payments\": [\n    {\n      \"payment_hash\": PAYMENT_HASH,\n      \"created_at\": CREATED_AT_MTS,\n      \"invoice_expiry\": INVOICE_EXPIRY_MTS,\n      \"invoice\": INVOICE,\n      \"recipient_pub_key\": RECIPIENT_PUB_KEY,\n      \"memo\": MEMO,\n      \"amount\": AMOUNT_SAT,\n      \"bfx_amount\": AMOUNT_BFX,\n      \"state\": STATUS\n    }\n  ]\n}\n\n// getInvoiceById\n{\n  \"payment_hash\": PAYMENT_HASH,\n  \"created_at\": CREATED_AT_MTS,\n  \"invoice_expiry\": INVOICE_EXPIRY_MTS,\n  \"invoice\": INVOICE,\n  \"recipient_pub_key\": RECIPIENT_PUB_KEY,\n  \"memo\": MEMO,\n  \"amount\": AMOUNT_SAT,\n  \"bfx_amount\": AMOUNT_BFX,\n  \"state\": STATUS\n}\n\n// getPaymentById\n{\n  \"payment_hash\": PAYMENT_HASH,\n  \"created_at\": CREATED_AT,\n  \"invoice_expiry\": INVOICE_EXPIRY,\n  \"invoice\": INVOICE,\n  \"recipient_pub_key\": RECIPIENT_PUB_KEY,\n  \"memo\": MEMO,\n  \"amount\": AMOUNT_SAT,\n  \"bfx_amount\": AMOUNT_BFX,\n  \"state\": STATUS\n}"
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
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/ext/invoice/payments'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    action: 'getInvoicesByUser',\n    query: {\n        offset: 0\n    }\n  }),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })",
              "name": "getInvoicesByUser"
            },
            {
              "language": "javascript",
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/ext/invoice/payments'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    action: 'getPaymentsByUser',\n    query: {\n        offset: 0\n    }\n  }),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })",
              "name": "getPaymentsByUser"
            },
            {
              "language": "javascript",
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/ext/invoice/payments'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    action: 'getInvoiceById',\n    query: {\n        txid: '05f589c28838e8f08d83ed6419ab54a6e58cfc125e1e7f63c2d350f504ed34d0'\n    }\n  }),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })",
              "name": "getInvoiceById"
            },
            {
              "language": "javascript",
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/r/ext/invoice/payments'\n\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\n    action: 'getPaymentById',\n    query: {\n        txid: '05f589c28838e8f08d83ed6419ab54a6e58cfc125e1e7f63c2d350f504ed34d0'\n    }\n  }),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n.catch(err => {\n    console.log(err)\n })",
              "name": "getPaymentById"
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
