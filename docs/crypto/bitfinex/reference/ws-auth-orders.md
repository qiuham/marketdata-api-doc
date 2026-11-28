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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-orders'
updated_at: 2026-11-28
---

# Orders

Receive a snapshot and updates for any order events on your account.

Subscribe to the account information channel to keep track of your orders. The account information channel provides a snapshot and updates on the orders in your account. The snapshot is delivered upon subscribing and any changes to your orders will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Order events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Order events will use one of the following abbreviations: 'os' (order snapshot), 'on' (order new), 'ou' (order update), and 'oc' (order cancel).

```json Snapshot ('os')

[
  0, //CHAN_ID
  "os", //MSG_TYPE
  [
    [
      34930659963, //ID
      null, //GID
      1574955083558, //CID
      "tETHUSD", //SYMBOL
      1574955083558, //MTS_CREATE
      1574955083573, //MTS_UPDATE
      0.201104, //AMOUNT
      0.201104, //AMOUNT_ORIG
      "EXCHANGE LIMIT", //ORDER_TYPE
      null, //TYPE_PREV
      null, //MTS_TIF
      null, //PLACEHOLDER
      0, //FLAGS
      "ACTIVE", //STATUS
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      120, //PRICE
      0, //PRICE_AVG
      0, //PRICE_TRAILING
      0, //PRICE_AUX_LIMIT
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      0, //NOTIFY
      0, //HIDDEN
      null, //PLACED_ID
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      "BFX", //ROUTING
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      {meta_object} //META
    ], //ORDER_ARRAY
    ...
  ] //ORDER_SNAPSHOT
]
```
```json Update ('on', 'ou', 'oc')
[
  0, //CHAN_ID
  "oc", //MSG_TYPE
  [
    34930659963, //ID
    null, //GID
    1574955083558, //CID
    "tETHUSD", //SYMBOL
    1574955083558, //MTS_CREATE
    1574955354487, //MTS_UPDATE
    0.201104, //AMOUNT
    0.201104, //AMOUNT_ORIG
    "EXCHANGE LIMIT", //ORDER_TYPE
    null, //TYPE_PREV
    null, //MTS_TIF
    null, //PLACEHOLDER
    0, //FLAGS
    "CANCELED", //ORDER_STATUS
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    120, //PRICE
    0, //PRICE_AVG
    0, //PRICE_TRAILING
    0, //PRICE_AUX_LIMIT
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    0, //NOTIFY
    0, //HIDDEN
    null, //PLACED_ID
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    "BFX", //ROUTING
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    {meta_object} //META
  ] //ORDER_ARRAY
]
```

#### Order snapshot data

| Index    | Field           | Type   | Description                                                                        |
| :------- | :-------------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID     | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]     | MSG\_TYPE       | String | 'os' (order snapshot)                                                              |
| \[2]     | ORDER\_SNAPSHOT | Array  | Array with an array of active orders (Indices \[0...n] will be orders)             |
| \[0...n] | ORDER\_ARRAY    | Array  | [Order array](#order-arrays)                                                       |

#### Order update data

| Index | Field        | Type   | Description                                                                              |
| :---- | :----------- | :----- | :--------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | Identification number assigned to the channel for the duration of this connection.       |
| \[1]  | MSG\_TYPE    | String | 'on' (order new), 'ou' (order update), 'oc' (order cancel (canceled or fully executed)). |
| \[2]  | ORDER\_ARRAY | Trade  | [Order array](#order-arrays)                                                             |

#### Order arrays

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
    <tr><td>[28]</td><td>ROUTING</td><td>String</td><td>Indicates origin of action: BFX</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[31]</td><td>META</td><td>Json string</td><td>Additional meta information about the order (e.g., $F7 = IS_POST_ONLY (0 if false, 1 if true), $F33 = Leverage (int), aff_code: "aff_code_here")</td></tr>
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

> 📘 Multiple Flags
>
> The summation of flags may result in multiple flags. For example 4160 (64 + 4096) means hidden post only.
