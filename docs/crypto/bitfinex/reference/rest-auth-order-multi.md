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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-order-multi'
updated_at: 2026-11-25
---

# Order Multi-OP

Send Multiple order-related operations. Please note the sent object has only one property with a value of an array of arrays detailing each order operation. (Max 75 operations per request)

> ❗️ Cancel All Orders
>
> Please note that using \{"all" : 1} to cancel all orders will cancel all trading as well as all derivatives orders. Order IDs can be passed instead to cancel only selected orders.

> 🚧 meta: \{protect\_selfmatch: 1}
>
> The 'protect\_selfmatch' flag can be used to avoid matching orders with standing orders on the same account. This flag is passed in the meta object in the order body when submitting or updating your orders.
>
> Note that this flag is only intended to assist users in avoiding unintentional wash trading. As per our [trading rulebook](https://www.bitfinex.com/legal/trading-rulebook), wash trading is forbidden on the platform.

**Response Fields**

<Table>
  <thead>
    <tr>
      <th>
        Term
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        MTS
      </td>

      <td>
        int
      </td>

      <td>
        Millisecond Time Stamp of the update
      </td>
    </tr>

    <tr>
      <td>
        TYPE
      </td>

      <td>
        string
      </td>

      <td>
        Purpose of notification ('on-req', 'oc-req', 'uca', 'fon-req', 'foc-req')
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_ID
      </td>

      <td>
        int
      </td>

      <td>
        unique ID of the message
      </td>
    </tr>

    <tr>
      <td>
        ID
      </td>

      <td>
        int
      </td>

      <td>
        Order ID
      </td>
    </tr>

    <tr>
      <td>
        GID
      </td>

      <td>
        int
      </td>

      <td>
        Group ID
      </td>
    </tr>

    <tr>
      <td>
        CID
      </td>

      <td>
        int
      </td>

      <td>
        Client Order ID
      </td>
    </tr>

    <tr>
      <td>
        SYMBOL
      </td>

      <td>
        string
      </td>

      <td>
        Pair (tBTCUSD, …)
      </td>
    </tr>

    <tr>
      <td>
        MTS_CREATE
      </td>

      <td>
        int
      </td>

      <td>
        Millisecond timestamp of creation
      </td>
    </tr>

    <tr>
      <td>
        MTS_UPDATE
      </td>

      <td>
        int
      </td>

      <td>
        Millisecond timestamp of update
      </td>
    </tr>

    <tr>
      <td>
        AMOUNT
      </td>

      <td>
        float
      </td>

      <td>
        Positive means buy, negative means sell.
      </td>
    </tr>

    <tr>
      <td>
        AMOUNT_ORIG
      </td>

      <td>
        float
      </td>

      <td>
        Original amount
      </td>
    </tr>

    <tr>
      <td>
        TYPE
      </td>

      <td>
        string
      </td>

      <td>
        The type of the order:   
        LIMIT, MARKET,  STOP, STOP LIMIT, TRAILING STOP, FOK, IOC.   
        For exchange orders: EXCHANGE LIMIT, EXCHANGE MARKET, EXCHANGE STOP, EXCHANGE STOP LIMIT, EXCHANGE TRAILING STOP, EXCHANGE FOK, EXCHANGE IOC.
      </td>
    </tr>

    <tr>
      <td>
        TYPE_PREV
      </td>

      <td>
        string
      </td>

      <td>
        Previous order type
      </td>
    </tr>

    <tr>
      <td>
        MTS_TIF
      </td>

      <td>
        int
      </td>

      <td>
        Millisecond timestamp of Time-In-Force: automatic order cancellation
      </td>
    </tr>

    <tr>
      <td>
        ORDER_STATUS
      </td>

      <td>
        string
      </td>

      <td>
        Order Status: ACTIVE, EXECUTED @ PRICE(AMOUNT) e.g. "EXECUTED @ 107.6(-0.2)", PARTIALLY FILLED @ PRICE(AMOUNT), INSUFFICIENT MARGIN was: PARTIALLY FILLED @ PRICE(AMOUNT), CANCELED, CANCELED was: PARTIALLY FILLED @ PRICE(AMOUNT), RSN_DUST (amount is less than 0.00000001), RSN_PAUSE (trading is paused due to rebase events on AMPL or funding settlement on derivatives)
      </td>
    </tr>

    <tr>
      <td>
        PRICE
      </td>

      <td>
        float
      </td>

      <td>
        Price
      </td>
    </tr>

    <tr>
      <td>
        PRICE_AVG
      </td>

      <td>
        float
      </td>

      <td>
        Average price
      </td>
    </tr>

    <tr>
      <td>
        PRICE_TRAILING
      </td>

      <td>
        float
      </td>

      <td>
        The trailing price
      </td>
    </tr>

    <tr>
      <td>
        PRICE_AUX_LIMIT
      </td>

      <td>
        float
      </td>

      <td>
        Auxiliary Limit price (for STOP LIMIT)
      </td>
    </tr>

    <tr>
      <td>
        HIDDEN
      </td>

      <td>
        int
      </td>

      <td>
        "null" if false, 1 if true
      </td>
    </tr>

    <tr>
      <td>
        PLACED_ID
      </td>

      <td>
        int
      </td>

      <td>
        If another order caused this order to be placed (OCO) this will be that other order's ID
      </td>
    </tr>

    <tr>
      <td>
        ROUTING
      </td>

      <td>
        string
      </td>

      <td>
        indicates origin of action: BFX, ETHFX, API>BFX, API>ETHFX
      </td>
    </tr>

    <tr>
      <td>
        FLAGS
      </td>

      <td>
        int
      </td>

      <td>
        See [https://docs.bitfinex.com/v2/docs/flag-values](https://docs.bitfinex.com/v2/docs/flag-values).
      </td>
    </tr>

    <tr>
      <td>
        META
      </td>

      <td>
        json string
      </td>

      <td>
        Additional meta information about the order ( $F7 = IS_POST_ONLY (0 if false, 1 if true), $F33 = Leverage (int))
      </td>
    </tr>

    <tr>
      <td>
        CODE
      </td>

      <td>
        null or integer
      </td>

      <td>
        Work in progress
      </td>
    </tr>

    <tr>
      <td>
        STATUS
      </td>

      <td>
        string
      </td>

      <td>
        Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)
      </td>
    </tr>

    <tr>
      <td>
        TEXT
      </td>

      <td>
        string
      </td>

      <td>
        Text of the notification
      </td>
    </tr>
  </tbody>
</Table>

**Ratelimit**: 90 req/min

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
    "/auth/w/order/multi": {
      "post": {
        "summary": "Order Multi-OP",
        "description": "Send Multiple order-related operations. Please note the sent object has only one property with a value of an array of arrays detailing each order operation. (Max 75 operations per request)",
        "operationId": "rest-auth-order-multi",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "Order Type: LIMIT, EXCHANGE LIMIT, MARKET, EXCHANGE MARKET, STOP, EXCHANGE STOP, STOP LIMIT, EXCHANGE STOP LIMIT, TRAILING STOP, EXCHANGE TRAILING STOP, FOK, EXCHANGE FOK, IOC, EXCHANGE IOC.",
                    "default": "EXCHANGE_LIMIT"
                  },
                  "symbol": {
                    "type": "string",
                    "description": "Symbol for desired pair",
                    "default": "tBTCUSD"
                  },
                  "price": {
                    "type": "string",
                    "description": "Price of order",
                    "default": "123.45"
                  },
                  "amount": {
                    "type": "string",
                    "description": "Amount of order (positive for buy, negative for sell)",
                    "default": "1.2345"
                  },
                  "flags": {
                    "type": "integer",
                    "description": "Optional see https://docs.bitfinex.com/v2/docs/flag-values",
                    "default": 0,
                    "format": "int32"
                  },
                  "lev": {
                    "type": "integer",
                    "description": "Set the leverage for a derivative order, supported by derivative symbol orders only. The value should be between 1 and 100 inclusive. The field is optional, if omitted the default leverage value of 10 will be used.",
                    "default": 10,
                    "format": "int32"
                  },
                  "price_trailing": {
                    "type": "string",
                    "description": "The trailing price for a trailing stop order",
                    "default": "1"
                  },
                  "price_aux_limit": {
                    "type": "string",
                    "description": "Auxiliary Limit price (for STOP LIMIT)",
                    "default": "10"
                  },
                  "price_oco_stop": {
                    "type": "string",
                    "description": "OCO stop price",
                    "default": "10"
                  },
                  "gid": {
                    "type": "integer",
                    "description": "Group Order ID (int45)"
                  },
                  "tif": {
                    "type": "string",
                    "description": "Time-In-Force: UTC datetime for automatic order cancellation (e.g. 2020-01-15 10:45:23). Note: TIF can be updated but not removed.",
                    "default": "YYYY-MM-DD HH:MM:SS"
                  },
                  "id": {
                    "type": "integer",
                    "description": "Order ID (Can be retrieved by calling the [Retrieve Orders](https://docs.bitfinex.com/reference#rest-auth-orders) endpoint)"
                  },
                  "cid": {
                    "type": "integer",
                    "description": "Client Order ID (int45)"
                  },
                  "cid_date": {
                    "type": "string",
                    "description": "Client Order ID Date",
                    "default": "YYYY-MM-DD"
                  },
                  "all": {
                    "type": "integer",
                    "description": "Cancel all open orders if value is set to: 1",
                    "default": 1,
                    "format": "int32"
                  },
                  "meta": {
                    "type": "object",
                    "description": "Object to pass order meta data. Options: 'aff_code' (to pass affiliate codes), 'make_visible' (to toggle visible on hit for hidden orders), 'protect_selfmatch' (to cancel submitted order if it would match with one of your own orders). Example: meta: {aff_code: \"AFF_CODE_HERE\", make_visible: 1}",
                    "properties": {}
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
                    "value": "[\n  MTS, \n  TYPE, \n  MESSAGE_ID, \n  null,\n  \n  [[\n    MTS, \n    TYPE, \n    MESSAGE_ID, \n    null,\n    \n      [[\n        ID,\n        GID,\n        CID,\n        SYMBOL,\n        MTS_CREATE, \n        MTS_UPDATE, \n        AMOUNT, \n        AMOUNT_ORIG, \n        TYPE,\n        TYPE_PREV,\n        MTS_TIF,\n        _PLACEHOLDER,\n        FLAGS,\n        ORDER_STATUS,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        PRICE,\n        PRICE_AVG,\n        PRICE_TRAILING,\n        PRICE_AUX_LIMIT,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        HIDDEN, \n        PLACED_ID,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        ROUTING,\n        _PLACEHOLDER,\n        _PLACEHOLDER,\n        META\n       ],\n       \n      [ID, ...]\n     \n    ],\n   \n   [MTS, TYPE, ...]\n    \n   ],\n   \n  CODE, \n  STATUS, \n  TEXT\n]\n    \n[1569347312984,\"ox_multi-req\",null,null,[[1569347312.977,\"on-req\",null,null,[[31492970019,null,1569347312970,\"tBTCUSD\",1569347312971,1569347312971,0.001,0.001,\"LIMIT\",null,null,null,4096,\"ACTIVE\",null,null,15,0,0,0,null,null,null,0,null,null,null,null,\"API>BFX\",null,null,{\"$F7\":1}]],null,\"SUCCESS\",\"Submitting 1 orders.\"],[1569347312.984,\"on-req\",null,null,[[31492970020,null,1569347312977,\"tBTCUSD\",1569347312978,1569347312978,0.001,0.001,\"LIMIT\",null,null,null,0,\"ACTIVE\",null,null,15,0,0,0,null,null,null,0,null,null,null,null,\"API>BFX\",null,null,null]],null,\"SUCCESS\",\"Submitting 1 orders.\"]],null,\"SUCCESS\",\"Submitting 2 order operations.\"]"
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
              "code": "/*  For guidelines on how to authenticate and use the sample code below please see\nhttps://docs.bitfinex.com/v2/docs/rest-auth */\n\nconst apiPath = 'v2/auth/w/order/multi'\nfetch(`https://api.bitfinex.com/${apiPath}`, {\n  method: 'POST',\n  body: JSON.stringify({\"ops\":[\n      \t[\"on\", {  // Order Submit       \n      \t\ttype: \"EXCHANGE LIMIT\",\n        \tsymbol: \"tBTCUSD\",\n        \tprice: \"123.45\",\n        \tamount: \"1.2345\",\n        \tflags: 0\n        \t}\n        ],\n        [\"oc\", {id: 12345}],// Order cancellation\n        [\"oc_multi\", {id: [ORDER_ID, 1234, 1235, ....]}], // Multi Order Cancellation\n        [\"ou\", {id: 12345, price: '15', amount: '0.001'}], // Order Update\n        ...\n      ]\n    }),\n  headers: {\n    /* auth headers */\n  }\n})\n.then(res => res.json())\n.then(json => console.log(json))\n  .catch(err => {\n    console.log(err)\n })\n",
              "name": "JavaScript"
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
