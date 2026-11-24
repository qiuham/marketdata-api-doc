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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-info-margin'
updated_at: 2026-11-24
---

# Margin Info

Get account margin information (like P/L, Swaps, Margin Balance, Tradable Balance and others). Use different keys (base, SYMBOL, sym_all) to retrieve different kinds of data.

### Margin base response fields

| Index | Field | Type                                              | Description                                     |
| :---- | :---- | :------------------------------------------------ | :---------------------------------------------- |
| \[0]  | KEY   | string                                            | Key for the request ('base')                    |
| \[1]  | DATA  | [Margin base data array](#margin-base-data-array) | Response data associated with the requested key |

#### Margin base data array

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
      <td>USER_PL</td>
      <td>float</td>
      <td>User profit and loss</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>USER_SWAPS</td>
      <td>float</td>
      <td>Amount of swaps a user has</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>MARGIN_BALANCE</td>
      <td>float</td>
      <td>Balance in margin wallet</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>MARGIN_NET</td>
      <td>float</td>
      <td>Balance in margin wallet including P&L</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>MARGIN_MIN</td>
      <td>float</td>
      <td>Minimum required margin for current positions</td>
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

### Margin symbol response fields

#### Margin symbol

| Index | Field  | Type                                                  | Description                                     |
| :---- | :----- | :---------------------------------------------------- | :---------------------------------------------- |
| \[0]  | KEY    | string                                                | Key for the request ('sym')                     |
| \[1]  | SYMBOL | string                                                | Pair (e.g. 'tBTCUSD', 'tETHUSD', ...)           |
| \[2]  | DATA   | [Margin symbol data array](#margin-symbol-data-array) | Response data associated with the requested key |

#### Margin sym\_all

| Index    | Field               | Type                            | Description                                                                                                                  |
| :------- | :------------------ | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| \[0...n] | Margin symbol array | [Margin symbol](#margin-symbol) | Each index contains one of the n margin symbol arrays. This returns margin symbol data for each margin-enabled trading pair. |

#### Margin symbol data array

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
      <td>TRADABLE_BALANCE</td>
      <td>float</td>
      <td>Your buying power (how large a position you can obtain)</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>GROSS_BALANCE</td>
      <td>float</td>
      <td>Your buying power including funds already reserved for open positions</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>BUY</td>
      <td>float</td>
      <td>Maximum amount you can buy at current best ASK</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>SELL</td>
      <td>float</td>
      <td>Maximum amount you can sell at current best BID</td>
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

**Ratelimit**: 90 req/min

> 📘 Limited to Margin Trading
>
> The v2 Margin Info endpoint is limited to margin trading and does not provide information related to derivatives trading.

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
    "/auth/r/info/margin/{key}": {
      "post": {
        "summary": "Margin Info",
        "description": "Get account margin information (like P/L, Swaps, Margin Balance, Tradable Balance and others). Use different keys (base, SYMBOL, sym_all) to retrieve different kinds of data.",
        "operationId": "rest-auth-info-margin",
        "parameters": [
          {
            "name": "key",
            "in": "path",
            "description": "\"base\" | SYMBOL | sym_all",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "RAW_BODY": {
                    "type": "string",
                    "default": "{}",
                    "format": "json"
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
                    "value": "// margin base\n[\"base\", //KEY\n [-3631.798995959999 //USER_PL\n  ,5.6376, //USER_SWAPS\n  299933.09380832, //MARGIN_BALANCE\n  296301.29481236, //MARGIN_BALANCE_NET\n  4975.291049394 //MARGIN_MIN\n ] //MARGIN_BASE_DATA_ARRAY\n]\n\n// margin symbol\n[\n  \"sym\", //KEY\n  \"tBTCUSD\", //SYMBOL\n  [854774.7939165855, //TRADABLE_BALANCE\n   909999.9796645334, //GROSS_BALANCE\n   52.08334097688924, //BUY\n   62.676711921295684, //SELL\n   null, //PLACEHOLDER\n   null, //PLACEHOLDER\n   null, //PLACEHOLDER\n   null //PLACEHOLDER\n  ] //MARGIN_SYM_DATA_ARRAY\n]\n\n// margin sym_all\n[\n  [\n  \t\"sym\", //KEY\n    \"tBTCUSD\", //SYMBOL\n    [\n      909998.8707081091, //TRADABLE_BALANCE\n      909998.8707081091, //GROSS_BALANCE\n      54.66115273354812, //BUY\n      61.63633640667225, //SELL\n      null, //PLACEHOLDER\n      null, //PLACEHOLDER\n      null, //PLACEHOLDER\n      null //PLACEHOLDER\n    ] //MARGIN_SYM_DATA_ARRAY\n  ], //MARGIN_SYM\n [...[...]]\n]"
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
