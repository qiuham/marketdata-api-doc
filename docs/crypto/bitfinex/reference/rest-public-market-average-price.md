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
source_url: 'https://docs.bitfinex.com/reference/rest-public-market-average-price'
updated_at: 2026-11-26
---

# Market Average Price

Calculate the average execution price for Trading or rate for Margin funding.

### Response Fields

#### For trading pair symbols (ex. tBTCUSD)

| Index | Field      | Type  | Description                                                                               |
| ----- | ---------- | ----- | ----------------------------------------------------------------------------------------- |
| \[0]  | PRICE\_AVG | float | Average price for amount bought or sold given the current order book (trading pairs only) |
| \[1]  | AMOUNT     | float | Amount traded or taken/provided in funding                                                |

#### For funding currency symbols (ex. fUSD)

| Index | Field     | Type  | Description                                                                                      |
| ----- | --------- | ----- | ------------------------------------------------------------------------------------------------ |
| \[0]  | RATE\_AVG | float | Average rate for amount taken or provided given the current order book (funding currencies only) |
| \[1]  | AMOUNT    | float | Amount traded or taken/provided in funding                                                       |

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
    "/calc/trade/avg": {
      "post": {
        "summary": "Market Average Price",
        "description": "Calculate the average execution price for Trading or rate for Margin funding.",
        "operationId": "rest-public-market-average-price",
        "parameters": [
          {
            "name": "symbol",
            "in": "query",
            "description": "The symbol you want information about.",
            "required": true,
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
            }
          },
          {
            "name": "amount",
            "in": "query",
            "description": "Amount. Positive for buy, negative for sell  (ex. \"1.123\")",
            "required": true,
            "schema": {
              "type": "string",
              "default": "1.123"
            }
          },
          {
            "name": "period",
            "in": "query",
            "description": "Maximum period for margin funding (required for funding currencies).",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "rate_limit",
            "in": "query",
            "description": "Limit rate/price (ex. \"1000.5\").",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "// on trading pairs (ex. tBTCUSD)\n[\n  24187.614862350845, //PRICE_AVG\n  1.123 //AMOUNT\n]\n\n// on funding currencies (ex. fUSD)\n[\n  0.00033317434, //RATE_AVG\n  1.123 //AMOUNT\n]"
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
