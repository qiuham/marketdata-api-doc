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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-order-update'
updated_at: 2026-11-19
---

# Update Order

Update an existing order, can be used to update margin, exchange, and derivative orders.

To update an order, construct a payload using the "ou" (order update) abbreviation and include the desired order details. Please look to the sidebar for examples.

When you update the order, you will receive a message of the appropriated type on the "account info" channel. Example responses are included in the sidebar. Please look to the [Orders](https://docs.bitfinex.com/reference/ws-auth-orders) and [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications) pages for further information, such as the response fields.

Order inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Adjust the remaining amount to 0.1 and set price to 500
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    amount: '0.1', 
    price: '500' 
  }
]   
    
// Increase the remaining amount by 0.1
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    delta: '0.1', 
    price: '6500' 
  }
]
    
// Change both price parameters of a stop limit order and set it to hidden
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    delta: '0.1', 
    price: '2500', 
    price_aux_limit: '2600', 
    flags: 64 
  }
]

// Move the order to group `123`
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    gid: 123 
  }
]
    
// set trailing price delta to 45
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    price_trailing: '45' 
  }
]

// set order expiration date
[
  0, 
  'ou', 
  null, 
  { 
    id: 1149698545, 
    tif: '2020-06-30' 
  }
]
```
```json Response
// When the order update is submitted you will receive an 'n' (notification) event as confirmation. If successful, you will also receive an 'ou' (order update) event. Both events are sent on CHANNEL_ID = 0.

[
  0, // CHANNEL_ID
  "n", // EVENT
  [
    1575289447641, // MTS
    "ou-req", // TYPE
    null, // MESSAGE_ID
    null, // _PLACEHOLDER
    [
      1185815100, // ID
      null, // GID
      1575289350475, // CID
      "tETHUSD", // SYMBOL
      1575289351944, // MTS_CREATE
      1575289351948, // MTS_UPDATE
      -3, // AMOUNT
      -3, // AMOUNT_ORIG
      "LIMIT", // ORDER_TYPE
      null, // TYPE_PREV
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
    "Submitting update to limit sell order for 3 ETH." // TEXT
  ]
]

[
  0, // CHANNEL_ID
  "ou", // EVENT
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
  ]
]

```

#### Request fields

| Name              | Type            | Description                                                                                                                                                                                                                                                          |
| ----------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                | Int             | Order ID                                                                                                                                                                                                                                                             |
| cid               | Int             | Client Order ID                                                                                                                                                                                                                                                      |
| cid\_date         | String          | Client Order ID Date                                                                                                                                                                                                                                                 |
| gid               | Int             | Group Order ID                                                                                                                                                                                                                                                       |
| price             | Decimal string  | Price                                                                                                                                                                                                                                                                |
| amount            | Decimal string  | Amount                                                                                                                                                                                                                                                               |
| lev               | Int             | Set the leverage for a derivative order, supported by derivative symbol orders only. The value should be between 1 and 100 inclusive. Mandatory for derivative order updates.                                                                                        |
| delta             | Decimal string  | Change of amount                                                                                                                                                                                                                                                     |
| price\_aux\_limit | Decimal string  | Auxiliary limit price                                                                                                                                                                                                                                                |
| price\_trailing   | Decimal string  | Trailing price delta                                                                                                                                                                                                                                                 |
| flags             | Int             | See `<https://docs.bitfinex.com/v2/docs/flag-values>`.                                                                                                                                                                                                               |
| tif               | Datetime string | Time-In-Force: datetime for automatic order cancellation (e.g. 2020-01-15 10:45:23). Note: TIF can be updated but not removed.                                                                                                                                       |
| meta              | Object          | Object to pass order meta data. Options: 'make\_visible' (to toggle visible on hit for hidden orders), 'protect\_selfmatch' (to cancel submitted order if it would match with one of your own orders). Example: meta: `{aff_code: "AFF_CODE_HERE", make_visible: 1}` |

> 📘 Multiple Flags
>
> The summation of flags may result in multiple flags. For example 4160 (64 + 4096) means hidden post only.

> 🚧 meta: `{protect_selfmatch: 1}`
>
> The 'protect\_selfmatch' flag can be used to avoid matching orders with standing orders on the same account. This flag is passed in the meta object in the order body when submitting or updating your orders.
>
> Note that this flag is only intended to assist users in avoiding unintentional wash trading. As per our [trading rulebook](https://www.bitfinex.com/legal/trading-rulebook), wash trading is forbidden on the platform.

#### Update order notification data

| Index | Field               | Type   | Description                                                                                                  |
| :---- | :------------------ | :----- | :----------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID         | Int    | ID of the channel. (0 for account info messages)                                                             |
| \[1]  | EVENT               | String | Type of event ('n' for notification)                                                                         |
| \[2]  | NOTIFICATION\_ARRAY | Array  | [Notification array](https://docs.bitfinex.com/reference/ws-auth-input-order-update#notification-array-data) |

#### Notification array data

| Index | Field         | Type            | Description                                                                                   |
| :---- | :------------ | :-------------- | :-------------------------------------------------------------------------------------------- |
| \[0]  | MTS           | Int             | Millisecond Time Stamp of the update                                                          |
| \[1]  | TYPE          | String          | Purpose of notification ('ou-req')                                                            |
| \[2]  | MESSAGE\_ID   | Int             | Unique ID of the message                                                                      |
| \[3]  | \_PLACEHOLDER |                 |                                                                                               |
| \[4]  | ORDER\_ARRAY  | Array           | [Order data](https://docs.bitfinex.com/reference/ws-auth-input-order-update#order-array-data) |
| \[5]  | CODE          | Null or integer | Work in progress                                                                              |
| \[6]  | STATUS        | String          | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)              |
| \[7]  | TEXT          | String          | Text of the notification                                                                      |

#### "ou" event data

| Index | Field        | Type   | Description                                                                                   |
| :---- | :----------- | :----- | :-------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | ID of the channel. (0 for account info messages)                                              |
| \[1]  | TYPE         | String | Type of event ('ou' for order update)                                                         |
| \[2]  | ORDER\_ARRAY | Array  | [Order data](https://docs.bitfinex.com/reference/ws-auth-input-order-update#order-array-data) |

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
