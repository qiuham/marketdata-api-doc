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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-update-order'
updated_at: 2026-11-27
---

# Update Order

Updates an existing order, can be used to update margin, exchange, and derivative orders.

### Response Fields

This endpoint returns a notification.

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
      <td>Milliseconds epoch timestamp of notification</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>TYPE</td>
      <td>string</td>
      <td>Notification's type ("ou-req")</td>
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
      <td>DATA</td>
      <td><a href="#order-objects">Order</a></td>
      <td>The order that has been updated</td>
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

#### Order data array

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
      <td>ID</td>
      <td>int</td>
      <td>Order ID</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>GID</td>
      <td>int</td>
      <td>Group Order ID</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>CID</td>
      <td>int</td>
      <td>Client Order ID</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>SYMBOL</td>
      <td>string</td>
      <td>Trading pair (tBTCUSD, tLTCETH, ...)</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>MTS_CREATE</td>
      <td>int</td>
      <td>Millisecond epoch timestamp of creation</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>MTS_UPDATE</td>
      <td>int</td>
      <td>Millisecond epoch timestamp of last update</td>
    </tr>
    <tr>
      <td>[6]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Positive means buy, negative means sell</td>
    </tr>
    <tr>
      <td>[7]</td>
      <td>AMOUNT_ORIG</td>
      <td>float</td>
      <td>Original amount (before any update)</td>
    </tr>
    <tr>
      <td>[8]</td>
      <td>ORDER_TYPE</td>
      <td>string</td>
      <td>The order's type (see list below)</td>
    </tr>
    <tr>
      <td>[9]</td>
      <td>TYPE_PREV</td>
      <td>string</td>
      <td>Previous order type (before the last update)</td>
    </tr>
    <tr>
      <td>[10]</td>
      <td>MTS_TIF</td>
      <td>int</td>
      <td>Millisecond epoch timestamp for TIF (Time-In-Force)</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[12]</td>
      <td>FLAGS</td>
      <td>int</td>
      <td>Sum of all active flags for the order (values can be found <a href="https://docs.bitfinex.com/v2/docs/flag-values">here</a>)</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>A complete overview on available order statuses can be found <a href="https://docs.bitfinex.com/docs/abbreviations-glossary#order-status">here</a></td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[16]</td>
      <td>PRICE</td>
      <td>float</td>
      <td>Price</td>
    </tr>
    <tr>
      <td>[17]</td>
      <td>PRICE_AVG</td>
      <td>float</td>
      <td>Average price</td>
    </tr>
    <tr>
      <td>[18]</td>
      <td>PRICE_TRAILING</td>
      <td>float</td>
      <td>The trailing price</td>
    </tr>
    <tr>
      <td>[19]</td>
      <td>PRICE_AUX_LIMIT</td>
      <td>float</td>
      <td>Auxiliary Limit price (for STOP LIMIT)</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[23]</td>
      <td>NOTIFY</td>
      <td>int</td>
      <td>1 if operations on order must trigger a notification, 0 if operations on order must not trigger a notification</td>
    </tr>
    <tr>
      <td>[24]</td>
      <td>HIDDEN</td>
      <td>int</td>
      <td>1 if order must be hidden, 0 if order must not be hidden</td>
    </tr>
    <tr>
      <td>[25]</td>
      <td>PLACED_ID</td>
      <td>int</td>
      <td>If another order caused this order to be placed (OCO) this will be that other order's ID</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[28]</td>
      <td>ROUTING</td>
      <td>string</td>
      <td>Indicates origin of action: BFX, API>BFX</td>
    </tr>
    
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    
    <tr>
      <td>[31]</td>
      <td>META</td>
      <td>JSON</td>
      <td>Additional meta information about the order ( $F7 = IS_POST_ONLY (0 if false, 1 if true), $F33 = Leverage (int), aff_code: "aff_code_here")</td>
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

> 📘 Available order types
>
> Available order types are: `LIMIT`, `MARKET`, `STOP`, `STOP LIMIT`, `TRAILING STOP`, `FOK`, `IOC`.\
> For exchange orders, add the EXCHANGE prefix: `EXCHANGE LIMIT`, `EXCHANGE MARKET`, `EXCHANGE STOP`, `EXCHANGE STOP LIMIT`, `EXCHANGE TRAILING STOP`, `EXCHANGE FOK`, `EXCHANGE IOC`

> 📘 Using multiple flags at once
>
> You may sum flag values to pass multiple flags.
> For example, 4160 (64 + 4096) means Hidden and Post Only.

> 🚧 meta: \{protect\_selfmatch: 1}
>
> The 'protect\_selfmatch' flag can be used to avoid matching orders with standing orders on the same account. This flag is passed in the meta object in the order body when submitting or updating your orders.
>
> Note that this flag is only intended to assist users in avoiding unintentional wash trading. As per our [trading rulebook](https://www.bitfinex.com/legal/trading-rulebook), wash trading is forbidden on the platform.

<HTMLBlock>{`
<hr/>

<table>
  <tr>
    <td style="font-weight: 600;">Rate Limit:</td>
    <td style="text-align: right;">90 reqs/min (requests per minute)</td>
  </tr>
</table>
`}</HTMLBlock>

<br />

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings-auth",
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
    "/auth/w/order/update": {
      "post": {
        "summary": "Update Order",
        "description": "Updates an existing order, can be used to update margin, exchange, and derivative orders.",
        "operationId": "rest-auth-update-order",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id"
                ],
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The ID of the order to update (can be retrieved by calling the [Retrieve Orders](https://docs.bitfinex.com/reference#rest-auth-retrieve-orders) and the [Retrieve Orders (by symbol)](https://docs.bitfinex.com/reference#rest-auth-retrieve-orders-by-symbol) endpoints).",
                    "format": "int64"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount of order (positive for buy, negative for sell)."
                  },
                  "price": {
                    "type": "string",
                    "description": "Price of the order."
                  },
                  "cid": {
                    "type": "integer",
                    "description": "Client Order ID; should be unique in the day (UTC+0).",
                    "format": "int64"
                  },
                  "cid_date": {
                    "type": "string",
                    "description": "`YYYY-MM-DD` Date of Client Order ID."
                  },
                  "gid": {
                    "type": "integer",
                    "description": "Group ID for the order.",
                    "format": "int64"
                  },
                  "flags": {
                    "type": "integer",
                    "description": "The sum of all order flags (see https://docs.bitfinex.com/docs/flag-values).",
                    "format": "int32"
                  },
                  "lev": {
                    "type": "integer",
                    "description": "Set the leverage for a derivative order, supported by derivative symbol orders only. The value should be between 1 and 100 inclusive. -- Mandatory for derivative order updates",
                    "format": "int32"
                  },
                  "delta": {
                    "type": "string",
                    "description": "The delta to apply to the amount value."
                  },
                  "price_aux_limit": {
                    "type": "string",
                    "description": "Auxiliary Limit price (only for STOP LIMIT)."
                  },
                  "price_trailing": {
                    "type": "string",
                    "description": "The trailing price for a trailing stop order."
                  },
                  "tif": {
                    "type": "string",
                    "description": "Time-In-Force: UTC datetime for automatic order cancellation (e.g. 2020-01-15 10:45:23). Note: TIF can be updated but not removed."
                  },
                  "meta": {
                    "type": "object",
                    "description": "Object to pass order meta data. Options: 'aff_code' (to pass affiliate codes), 'make_visible' (to toggle visible on hit for hidden orders), 'protect_selfmatch' (to cancel submitted order if it would match with one of your own orders). Example: meta: {aff_code: \"AFF_CODE_HERE\", make_visible: 1}",
                    "properties": {
                      "aff_code": {
                        "type": "string",
                        "description": "Pass an affiliate code as a string"
                      },
                      "make_visible": {
                        "type": "integer",
                        "description": "Turn on 'visible on hit' for hidden orders (1 to enable)",
                        "format": "int32"
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
                    "value": "[\n  1678988263842, //MTS\n  \"ou-req\", //TYPE\n  null, //MESSAGE_ID\n  null,\n  [\n    1747566428, //ID\n    null, //GID\n    1678987199446, //CID\n    \"tBTCUSD\", //SYMBOL\n    1678987199446, //MTS_CREATE\n    1678988263843, //MTS_UPDATE\n    0.25, //AMOUNT\n    0.1, //AMOUNT_ORIG\n    \"EXCHANGE LIMIT\", //ORDER_TYPE\n    \"EXCHANGE LIMIT\", //TYPE_PREV\n    null, //MTS_TIF\n    null,\n    0, //FLAGS\n    \"ACTIVE\", //STATUS\n    null,\n    null,\n    25000, //PRICE\n    0, //PRICE_AVG\n    0, //PRICE_TRAILING\n    0, //PRICE_AUX_LIMIT\n    null,\n    null,\n    null,\n    0, //NOTIFY\n    0, //HIDDEN\n    null, //PLACED_ID\n    null,\n    null,\n    \"API>BFX\", //ROUTING\n    null,\n    null,\n    null //META\n  ], //DATA\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"Submitting update to exchange limit buy order for 0.1 BTC.\" //TEXT\n]"
                  }
                },
                "schema": {
                  "type": "array"
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
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": false,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
