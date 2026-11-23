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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-order-cancel'
updated_at: 2026-11-23
---

# Cancel Order

Cancels the specified order

To cancel an order, construct a payload using the "oc" (order cancel) abbreviation. The order details need to include either the Internal Order ID or the Client Order ID and Client Order ID Date (YYYY-MM-DD format). Please look to the sidebar for examples.

When you cancel an order, you will receive a message of the appropriated type on the "account info" channel. Example responses are included in the sidebar. Please look to the [Orders](https://docs.bitfinex.com/reference/ws-auth-orders) and [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications) pages for further information.

Order inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Cancel order by internal order Id
[
  0,
  "oc",
  null,
  {
    "id": ID
  }
]

// Cancel order using client order Id and order creation date
[
  0,
  "oc",
  null,
  {
    "cid": CID,
    "cid_date": CID_DATE
  }
]
```
```json Response
// When the cancellation request is submitted you will receive an 'n' (notification) event as confirmation. If the cancellation is successful, you will also receive an 'oc' (order cancelled) event. Both events are sent through CHANNEL_ID = 0.

[
  0, // CHANNEL_ID
  "n", // EVENT
  [
    1575291219660, // MTS
    "oc-req", // TYPE
    null, // MESSAGE_ID
    null, // _PLACEHOLDER
    [
      1185815100, // ID
      null, // GID
      1575289350475, // CID
      "tETHUSD", // SYMBOL
      1575289351944, // MTS_CREATE
      1575289447644, // MTS_UPDATE
      -3, // AMOUNT
      -3, // AMOUNT_ORIG
      "LIMIT", // ORDER_TYPE
      "LIMIT", // TYPE_PREV
      null, // MTS_TIF
      null, // _PLACEHOLDER
      0, // FLAGS
      "ACTIVE", // STATUS
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      240, // PRICE
      0, // PRICE_AVG
      0, // PRICE_TRAILING
      0, // PRICE_AUX_LIMIT
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      0, // NOTIFY
      0, // HIDDEN
      null, // PLACED_ID
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      "API>BFX", // ROUTING
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      null // META
    ],
    null, // CODE
    "SUCCESS", // STATUS
    "Submitted for cancellation; waiting for confirmation (ID: 1185815100)." // TEXT
  ]
]

[
  0, // CHANNEL_ID
  "oc", // EVENT
  [
    1185815100, // ID
    null, // GID
    1575289350475, // CID
    "tETHUSD", // SYMBOL
    1575289351944, // MTS_CREATE
    1575291219663, // MTS_UPDATE
    -3, // AMOUNT
    -3, // AMOUNT_ORIG
    "LIMIT", // ORDER_TYPE
    "LIMIT", // TYPE_PREV
    null, // MTS_TIF
    null, // _PLACEHOLDER
    0, // FLAGS
    "CANCELED", // STATUS
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    240, // PRICE
    0, // PRICE_AVG
    0, // PRICE_TRAILING
    0, // PRICE_AUX_LIMIT
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    0, // NOTIFY
    0, // HIDDEN
    null, // PLACED_ID
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    "API>BFX", // ROUTING
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    null // META
  ]
]

```

#### Request fields

| Name      | Type   | Description          |
| --------- | ------ | -------------------- |
| id        | Int    | Internal Order ID    |
| cid       | Int    | Client Order ID      |
| cid\_date | String | Client Order ID Date |

#### Cancel order notification data

| Index | Field               | Type   | Description                                                                                                  |
| :---- | :------------------ | :----- | :----------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID         | Int    | ID of the channel. (0 for account info messages)                                                             |
| \[1]  | EVENT               | String | Type of event ('n' for notification)                                                                         |
| \[2]  | NOTIFICATION\_ARRAY | Array  | [Notification array](https://docs.bitfinex.com/reference/ws-auth-input-order-cancel#notification-array-data) |

#### Notification array data

| Index | Field         | Type            | Description                                                                                   |
| :---- | :------------ | :-------------- | :-------------------------------------------------------------------------------------------- |
| \[0]  | MTS           | Int             | Millisecond Time Stamp of the update                                                          |
| \[1]  | TYPE          | String          | Purpose of notification ('oc-req')                                                            |
| \[2]  | MESSAGE\_ID   | Int             | Unique ID of the message                                                                      |
| \[3]  | \_PLACEHOLDER |                 |                                                                                               |
| \[4]  | ORDER\_ARRAY  | Array           | [Order data](https://docs.bitfinex.com/reference/ws-auth-input-order-cancel#order-array-data) |
| \[5]  | CODE          | Null or integer | Work in progress                                                                              |
| \[6]  | STATUS        | String          | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)              |
| \[7]  | TEXT          | String          | Text of the notification                                                                      |

#### "oc" event data

| Index | Field        | Type   | Description                                                                                   |
| :---- | :----------- | :----- | :-------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | ID of the channel. (0 for account info messages)                                              |
| \[1]  | TYPE         | String | Type of event ('oc' for order cancelled)                                                      |
| \[2]  | ORDER\_ARRAY | Array  | [Order data](https://docs.bitfinex.com/reference/ws-auth-input-order-cancel#order-array-data) |

#### Order Array data

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
    <tr><td>[0]</td><td>ID</td><td>Int</td><td>Order ID</td></tr>
    <tr><td>[1]</td><td>GID</td><td>Int</td><td>Group ID</td></tr>
    <tr><td>[2]</td><td>CID</td><td>Int</td><td>Client Order ID</td></tr>
    <tr><td>[3]</td><td>SYMBOL</td><td>String</td><td>Pair (tBTCUSD, …)</td></tr>
    <tr><td>[4]</td><td>MTS_CREATE</td><td>Int</td><td>Millisecond timestamp of creation</td></tr>
    <tr><td>[5]</td><td>MTS_UPDATE</td><td>Int</td><td>Millisecond timestamp of update</td></tr>
    <tr><td>[6]</td><td>AMOUNT</td><td>Float</td><td>Positive means buy, negative means sell.</td></tr>
    <tr><td>[7]</td><td>AMOUNT_ORIG</td><td>Float</td><td>Original amount</td></tr>
    <tr><td>[8]</td><td>ORDER_TYPE</td><td>String</td><td>The type of the order: LIMIT, MARKET, STOP, STOP LIMIT, TRAILING STOP, FOK, IOC For exchange orders: EXCHANGE MARKET, EXCHANGE LIMIT, EXCHANGE STOP, EXCHANGE STOP LIMIT, EXCHANGE TRAILING STOP, EXCHANGE FOK, EXCHANGE IOC.</td></tr>
    <tr><td>[9]</td><td>TYPE_PREV</td><td>String</td><td>Previous order type</td></tr>
    <tr><td>[10]</td><td>MTS_TIF</td><td>Int</td><td>Millisecond timestamp of Time-In-Force: automatic order cancellation</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[12]</td><td>FLAGS</td><td>Int</td><td>See https://docs.bitfinex.com/v2/docs/flag-values</td></tr>
    <tr><td>[13]</td><td>ORDER_STATUS</td><td>String</td><td>Order Status: ACTIVE, EXECUTED @ PRICE(AMOUNT) e.g. "EXECUTED @ 107.6(-0.2)", PARTIALLY FILLED @ PRICE(AMOUNT), INSUFFICIENT MARGIN was: PARTIALLY FILLED @ PRICE(AMOUNT), CANCELED, CANCELED was: PARTIALLY FILLED @ PRICE(AMOUNT), RSN_DUST (amount is less than 0.00000001), RSN_PAUSE (trading is paused due to rebase events on AMPL or funding settlement on derivatives)</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[16]</td><td>PRICE</td><td>Float</td><td>Price</td></tr>
    <tr><td>[17]</td><td>PRICE_AVG</td><td>Float</td><td>Average price</td></tr>
    <tr><td>[18]</td><td>PRICE_TRAILING</td><td>Float</td><td>The trailing price</td></tr>
    <tr><td>[19]</td><td>PRICE_AUX_LIMIT</td><td>Float</td><td>Auxiliary Limit price (for STOP LIMIT)</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[23]</td><td>NOTIFY</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[24]</td><td>HIDDEN</td><td>Int</td><td>1 if Hidden, 0 if not hidden</td></tr>
    <tr><td>[25]</td><td>PLACED_ID</td><td>Int</td><td>If another order caused this order to be placed (OCO) this will be that other order's ID</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[28]</td><td>ROUTING</td><td>String</td><td>Indicates origin of action: BFX, ETHFX, API>BFX, API>ETHFX</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[31]</td><td>META</td><td>Json string</td><td>Additional meta information about the order (e.g., $F7 = IS_POST_ONLY (0 if false, 1 if true), $F33 = Leverage (int))</td></tr>
  </tbody>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb;
  }
  
  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

<br />
