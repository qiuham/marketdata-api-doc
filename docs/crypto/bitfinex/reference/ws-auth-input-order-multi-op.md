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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-order-multi-op'
updated_at: 2026-11-26
---

# Order Multi-OP

Send multiple order-related operations. (Max 75 operations per request)

The Order Multi-OP command allows sending of multiple order operations at the same time. To do this, construct a payload with the "ox\_multi" (order operation multi) abbreviation. Use the inner array to specify the different operations you would like to perform, starting each separate operation with the appropriate abbreviation followed by an object holding the details.

You will receive messages to confirm your requests through "n" (notification) events and, if successful, confirmation of the operations using other event messages ("on", "oc", "ou", etc.). Please look to the [Orders](https://docs.bitfinex.com/reference/ws-auth-orders) and [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications) pages for further information on the responses you receive.

Order inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Model
[
  0,
  "ox_multi",
  null,
  [
    [OPERATION, {}],
    [OPERATION, {}],
    [OPERATION, {}],
    ...
  ]
]
  
// Example
[
  0,
  "ox_multi",
  null,
  [
    ["on", {...}],
    ["oc", {...}],
    ["oc_multi", {...}],
    ["oc", {...}],
    ...
  ]
]
```
