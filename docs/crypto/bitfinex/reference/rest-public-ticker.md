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
source_url: 'https://docs.bitfinex.com/reference/rest-public-ticker'
updated_at: 2026-11-22
---

# Ticker

The ticker endpoint provides a high level overview of the state of the market for a specified pair. It shows the current best bid and ask, the last traded price, as well as information on the daily volume and price movement over the last day.

### Response Fields (trading pairs, ex. tBTCUSD)

| Index | Field            | Type  | Description                                                                  |
| ----- | ---------------- | ----- | ---------------------------------------------------------------------------- |
| \[0]  | BID              | float | Price of last highest bid                                                    |
| \[1]  | BID\_SIZE        | float | Sum of the 25 highest bid sizes                                              |
| \[2]  | ASK              | float | Price of last lowest ask                                                     |
| \[3]  | ASK\_SIZE        | float | Sum of the 25 lowest ask sizes                                               |
| \[4]  | CHANGE           | float | Amount that the last price changed in the respective period                  |
| \[5]  | CHANGE\_RELATIVE | float | Relative price change in the respective period (\*100 for percentage change) |
| \[6]  | LAST\_PRICE      | float | Price of the last trade                                                      |
| \[7]  | VOLUME           | float | Volume in the respective period                                              |
| \[8]  | HIGH             | float | High in the respective period                                                |
| \[9]  | LOW              | float | Low in the respective period                                                 |
| \[10] | FIRST\_TRADE     | int   | Timestamp of the first trade                                                 |

### Response Fields (funding currencies, ex. fUSD)

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
      <td>FRR</td>
      <td>float</td>
      <td>Flash Return Rate - average of all fixed rate funding over the last hour</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>BID</td>
      <td>float</td>
      <td>Price of last highest bid</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>BID_PERIOD</td>
      <td>int</td>
      <td>Bid period covered in days</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>BID_SIZE</td>
      <td>float</td>
      <td>Sum of the 25 highest bid sizes</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>ASK</td>
      <td>float</td>
      <td>	Price of last lowest ask</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>ASK_PERIOD</td>
      <td>int</td>
      <td>Ask period covered in days</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>ASK_SIZE</td>
      <td>float</td>
      <td>Sum of the 25 lowest ask sizes</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>DAILY_CHANGE</td>
      <td>float</td>
      <td>Amount that the last price changed in the respective period</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>DAILY_CHANGE_PERC</td>
      <td>float</td>
      <td>Relative price change in the respective period (*100 for percentage change)</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>LAST_PRICE</td>
      <td>float</td>
      <td>Price of the last trade</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>VOLUME</td>
      <td>float</td>
      <td>Volume in the respective period</td>
    </tr>
    <tr>
      <td>[11]</td>
      <td>HIGH</td>
      <td>float</td>
      <td>High in the respective period</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>LOW</td>
      <td>float</td>
      <td>Low in the respective period</td>
    </tr>

    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>

    <tr>
      <td>[15]</td>
      <td>FRR_AMOUNT_AVAILABLE</td>
      <td>float</td>
      <td>The amount of funding that is available at the Flash Return Rate</td>
    </tr>
<tr>
      <td>[16]</td>
      <td>FIRST_TRADE</td>
      <td>int</td>
      <td>Timestamp of the first trade</td>
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
    "/ticker/{symbol}": {
      "get": {
        "summary": "Ticker",
        "description": "The ticker endpoint provides a high level overview of the state of the market for a specified pair. It shows the current best bid and ask, the last traded price, as well as information on the daily volume and price movement over the last day.",
        "operationId": "rest-public-ticker",
        "parameters": [
          {
            "name": "symbol",
            "in": "path",
            "description": "The symbol you want information about. (e.g. tBTCUSD, tETHUSD, fUSD, fBTC)",
            "required": true,
            "schema": {
              "type": "string",
              "default": "tBTCUSD"
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
                    "value": "// on trading pairs (ex. tBTCUSD)\n[\n  10645, //BID\n  73.93854271, //BID_SIZE\n  10647, //ASK\n  75.22266119, //ASK_SIZE\n  731.60645389, //CHANGE\n  0.0738, //CHANGE_RELATIVE\n  10644.00645389, //LAST_PRICE\n  14480.89849423, //VOLUME\n  10766, //HIGH\n  9889.1449809, //LOW\n\t1358182043000 //FIRST_TRADE\n]\n\n// on funding currencies (ex. fUSD)\n[\n  0.0003447041095890411, //FRR\n  0.000316, //BID\n  30, //BID_PERIOD\n  1681669.14021675, //BID_SIZE\n  0.00033268, //ASK\n  2, //ASK_PERIOD\n  146425121.0115426, //ASK_SIZE\n  -0.00001062, //CHANGE\n  -0.0307, //CHANGE_RELATIVE\n  0.00033534, //LAST_PRICE\n  157503514.7976808, //VOLUME\n  0.000347, //HIGH\n  4e-7, //LOW\n  null,\n  null,\n  146212916.17047712, //FRR_AMOUNT_AVAILABLE\n\t1469734163000 //FIRST_TRADE\n]"
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
                    "value": "[\"error\", 10020, \"symbol: invalid\"]"
                  }
                },
                "schema": {
                  "type": "array"
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
