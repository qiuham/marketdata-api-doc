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
source_url: 'https://docs.bitfinex.com/reference/rest-public-foreign-exchange-rate'
updated_at: 2026-11-27
---

# Foreign Exchange Rate

Calculate the exchange rate between two currencies

### Response Fields

| Index | Field         | Type  | Description   |
| ----- | ------------- | ----- | ------------- |
| \[0]  | CURRENT\_RATE | float | Exchange rate |

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">90 reqs/min (requests per minute)</td>
  </tr>
</table>
`}</HTMLBlock>

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings-public",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api-pub.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/calc/fx": {
      "post": {
        "summary": "Foreign Exchange Rate",
        "description": "Calculate the exchange rate between two currencies",
        "operationId": "rest-public-foreign-exchange-rate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "ccy1",
                  "ccy2"
                ],
                "properties": {
                  "ccy1": {
                    "type": "string",
                    "description": "1st currency (base currency).",
                    "default": "BTC"
                  },
                  "ccy2": {
                    "type": "string",
                    "description": "2nd currency (quote currency).",
                    "default": "USD"
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
                    "value": "[ \n  8668.65 //CURRENT_RATE \n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "example": 8668.65,
                    "default": 0
                  }
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
