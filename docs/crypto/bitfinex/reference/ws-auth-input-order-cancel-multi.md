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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-order-cancel-multi'
updated_at: 2026-11-27
---

# Cancel Order Multi

Cancel the specified order list

The Cancel Order Multi command allows sending of multiple order cancellation operations at the same time. To do this, construct a payload with the "oc\_multi" (order cancel multi) abbreviation. The payload needs to include an object that specifies which orders to cancel based on Internal Order ID's, Client Order ID's (along with the cid\_DATE in a YYYY-MM-DD format), Group ID, or the "all" request field. Please look to the sidebar for examples of each method.

You will receive messages to confirm your cancellation requests through "n" (notification) events and, if successful, confirmation through "oc" (order cancelled) events.  Please look to the [Orders](https://docs.bitfinex.com/reference/ws-auth-orders) and [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications) pages for further information on the responses you receive.

Order inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Cancel all orders
[
  0,
  "oc_multi",
  null,
  {
    "all": 1
  }
]

// Cancel multiple orders by Internal Order ID
[
  0,
  "oc_multi",
  null,
  {
    "id": [ID, 1234, ...]
  }
]

// Cancel multiple orders using Client Order ID and order creation date
[
  0,
  "oc_multi",
  null,
  {
    "cid": [
      [ID, CID_DATE],
      [234, "2016-12-05"],
      ...
    ]
  }
]

// Cancel multiple orders using Group ID
[
  0,
  "oc_multi",
  null,
  {
     "gid": [GID, 11, ...]
  }
]
```

**Request Fields**

| Name      | Type   | Description          |
| --------- | ------ | -------------------- |
| id        | int64  | Internal Order ID    |
| cid       | int45  | Client Order ID      |
| cid\_date | string | Client Order ID Date |
| gid       | int45  | Group Order ID       |

> ❗️ Cancel All Orders
>
> Please note that using \{"all" : 1} to cancel all orders will cancel all trading as well as all derivatives orders. Order IDs can be passed instead to cancel only selected orders.
