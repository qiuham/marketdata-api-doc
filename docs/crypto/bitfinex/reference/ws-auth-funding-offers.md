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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-funding-offers'
updated_at: 2026-11-20
---

# Funding Offers

Receive a snapshot and updates for any position events on your account.

Subscribe to the account information channel to keep track of your funding offers. The account information channel provides a snapshot and updates on the funding offers in your account. The snapshot is delivered upon subscribing and any changes to your positions will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Funding offer events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Funding offer events will use one of the following abbreviations: 'fos' (funding offers snapshot), 'fon' (funding offer new), 'fou' (funding offers update), and 'foc' (funding offer cancel).

```json Snapshot ('fos')
    
[
  0, //CHAN_ID
  "fos", //MSG_TYPE
  [
    [
      41237920, //OFFER_ID
      "fETH", //SYMBOL
      1573912039000, //MTS_CREATED
      1573912039000, //MTS_UPDATED
      0.5, //AMOUNT
      0.5, //AMOUNT_ORIG
      "LIMIT", //OFFER_TYPE
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      0, //FLAGS
      "ACTIVE", //STATUS
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      0.0024, //RATE
      2, //PERIOD
      0, //NOTIFY
      0, //HIDDEN
      null, //PLACEHOLDER
      0, //RENEW
      null //PLACEHOLDER
    ] //FUNDING_OFFER_ARRAY
  ] //FUNDING_OFFERS_SNAPSHOT
]
```
```json Update ('fon', 'fou', 'foc')

[
  0, //CHAN_ID
  "fon", //MSG_TYPE
  [
    41238747, //OFFER_ID
    "fUST", //SYMBOL
    1575026670000, //MTS_CREATED
    1575026670000, //MTS_UPDATED
    5000, //AMOUNT
    5000, //AMOUNT_ORIG
    "LIMIT", //OFFER_TYPE
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    0, //FLAGS
    "ACTIVE", //STATUS
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    0.006000000000000001, //RATE
    30, //PERIOD
    0, //NOTIFY
    0, //HIDDEN
    null, //PLACEHOLDER
    0, //RENEW
    null //RATE_REAL
  ]
]
```

#### Funding offer snapshot data

| Index    | Field                     | Type   | Description                                                                           |
| :------- | :------------------------ | :----- | :------------------------------------------------------------------------------------ |
| \[0]     | CHANNEL\_ID               | Int    | Identification number assigned to the channel for the duration of this connection.    |
| \[1]     | MSG\_TYPE                 | String | 'fos' (funding offers snapshot)                                                       |
| \[2]     | FUNDING\_OFFERS\_SNAPSHOT | Array  | Array with an array of active funding offers(Indices \[0...n] will be funding offers) |
| \[0...n] | FUNDING\_OFFER\_ARRAY     | Array  | [Funding offer array](#funding-offer-arrays)                                          |

#### Funding offer update data

| Index | Field                 | Type   | Description                                                                                                         |
| :---- | :-------------------- | :----- | :------------------------------------------------------------------------------------------------------------------ |
| \[0]  | CHANNEL\_ID           | Int    | Identification number assigned to the channel for the duration of this connection.                                  |
| \[1]  | MSG\_TYPE             | String | 'fon' (funding offer new), 'fou' (funding offer update), 'foc' (funding offer cancel (cancelled or fully executed)) |
| \[2]  | FUNDING\_OFFER\_ARRAY | Array  | [Funding offer array](#funding-offer-arrays)                                                                        |

#### Funding offer array

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
    <tr><td>[0]</td><td>OFFER_ID</td><td>Integer</td><td>Offer ID</td></tr>
    <tr><td>[1]</td><td>SYMBOL</td><td>String</td><td>The currency of the offer (fUSD, etc)</td></tr>
    <tr><td>[2]</td><td>MTS_CREATED</td><td>Int</td><td>Millisecond Time Stamp when the offer was created</td></tr>
    <tr><td>[3]</td><td>MTS_UPDATED</td><td>Int</td><td>Millisecond Time Stamp when the offer was updated</td></tr>
    <tr><td>[4]</td><td>AMOUNT</td><td>Float</td><td>Amount the offer is for</td></tr>
    <tr><td>[5]</td><td>AMOUNT_ORIG</td><td>Float</td><td>Amount the offer was entered with originally</td></tr>
    <tr><td>[6]</td><td>OFFER_TYPE</td><td>String</td><td>"LIMIT" or "FRRDELTAVAR"</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[9]</td><td>FLAGS</td><td>Object</td><td>See <https://docs.bitfinex.com/v2/docs/flag-values>.</td></tr>
    <tr><td>[10]</td><td>STATUS</td><td>String</td><td>Offer Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[14]</td><td>RATE</td><td>Float</td><td>Rate of the offer</td></tr>
    <tr><td>[15]</td><td>PERIOD</td><td>Int</td><td>Period of the offer</td></tr>
    <tr><td>[16]</td><td>NOTIFY</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[17]</td><td>HIDDEN</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[19]</td><td>RENEW</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
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
