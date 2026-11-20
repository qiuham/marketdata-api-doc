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
source_url: 'https://docs.bitfinex.com/reference/rest-auth-cancel-order'
updated_at: 2026-11-20
---

# Cancel Order

Cancels one of the current user's orders.

Users can cancel their margin, exchange and derivative orders by providing their IDs.

Alternatively, users can cancel an order using its CID along with a date (YYYY-MM-DD).

Both the ID and CID of an order can be get through the [Retrieve Orders](https://docs.bitfinex.com/reference/rest-auth-retrieve-orders) and [Retrieve Orders (by symbol)](https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol) endpoints.

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
      <td>Notification's type ("oc-req")</td>
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
      <td>The order that has been cancelled</td>
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

<br />

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
    "/auth/w/order/cancel": {
      "post": {
        "summary": "Cancel Order",
        "description": "Cancels one of the current user's orders.",
        "operationId": "rest-auth-cancel-order",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The ID of the order to cancel (can be get using the [Retrieve Orders](https://docs.bitfinex.com/reference#rest-auth-retrieve-orders) and the [Retrieve Orders (by symbol)](https://docs.bitfinex.com/reference#rest-auth-retrieve-orders-by-symbol) endpoints). "
                  },
                  "cid": {
                    "type": "integer",
                    "description": "The CID of the order to cancel. Users must also provide a `cid_date` to cancel an order through its CID. Providing only the CID will cause the endpoint to return an error. (int45)"
                  },
                  "cid_date": {
                    "type": "string",
                    "description": "An YYYY-MM-DD date to provide along with an order's CID.",
                    "format": "date"
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
                    "value": " [\n  1678989283488, //MTS\n  \"oc-req\", //TYPE\n  null, //MESSAGE_ID\n  null,\n  [\n    1747566428, //ID\n    null, //GID\n    1678987199446, //CID\n    \"tBTCUSD\", //SYMBOL\n    1678987199446, //MTS_CREATE\n    1678989283489, //MTS_UPDATE\n    0.25, //AMOUNT\n    0.1, //AMOUNT_ORIG\n    \"EXCHANGE LIMIT\", //ORDER_TYPE\n    \"EXCHANGE LIMIT\", //TYPE_PREV\n    null, //MTS_TIF\n    null,\n    0, //FLAGS\n    \"CANCELED\", //STATUS\n    null,\n    null,\n    25000, //PRICE\n    0, //PRICE_AVG\n    0, //PRICE_TRAILING\n    0, //PRICE_AUX_LIMIT\n    null,\n    null,\n    null,\n    0, //NOTIFY\n    0, //HIDDEN\n    null, //PLACED_ID\n    null,\n    null,\n    \"API>BFX\", //ROUTING\n    null,\n    null,\n    null //META\n  ], //DATA\n  null, //CODE\n  \"SUCCESS\", //STATUS\n  \"Submitted for cancellation; waiting for confirmation (ID: 1747566428).\" //TEXT\n]"
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
