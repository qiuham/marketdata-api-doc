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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-funding-credits'
updated_at: 2026-11-28
---

# Funding Credits

Receive a snapshot and updates for any funding credits (funds used in active positions) on your account.

Subscribe to the account information channel to keep track of your funding credits. The account information channel provides a snapshot and updates on the funding credits in your account. The snapshot is delivered upon subscribing and any changes to your funding credits will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Funding credits events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Funding credits events will use one of the following abbreviations: 'fcs' (funding credits snapshot), 'fcn' (funding credits new), 'fcu' (funding credits update), 'fcc' (funding credits close).

```json Snapshot ('fcs')
[
  0, //CHAN_ID
  "fcs", //MSG_TYPE
  [
    [
      26223578, //CREDIT_ID
      "fUST", //SYMBOL
      1, //SIDE
      1575052261000, //MTS_CREATE
      1575296187000, //MTS_UPDATE
      350, //AMOUNT
      0, //FLAGS
      "ACTIVE", //STATUS
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      0, //RATE
      30, //PERIOD
      1575052261000, //MTS_OPENING
      1575293487000, //MTS_LAST_PAYOUT
      0, //NOTIFY
      0, //HIDDEN
      null, //PLACEHOLDER
      0, //RENEW
      null, //RATE_REAL
      0, //NO_CLOSE
      "tBTCUST" //POSITION_PAIR
    ], //FUNDING_CREDIT_ARRAY
    ...
  ] //FUNDING_CREDITS_SNAPSHOT
]
```
```json Update ('fcn', 'fcu', 'fcc')
[
  0, //CHAN_ID
  "fcu", //MSG_TYPE
  [
    26223578, //CREDIT_ID
    "fUST", //SYMBOL
    1, //SIDE
    1575052261000, //MTS_CREATE
    1575296787000, //MTS_UPDATE
    350, //AMOUNT
    0, //FLAGS
    "ACTIVE", //STATUS
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    0, //RATE
    30, //PERIOD
    1575052261000, //MTS_OPENING
    1575293487000, //MTS_LAST_PAYOUT
    0, //NOTIFY
    0, //HIDDEN
    null, //PLACEHOLDER
    0, //RENEW
    null, //RATE_REAL
    0, //NO_CLOSE
    "tBTCUST" //POSITION_PAIR
  ] //FUNDING_CREDIT_ARRAY
]
```

#### Funding credits snapshot data

| Index    | Field                      | Type   | Description                                                                             |
| :------- | :------------------------- | :----- | :-------------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID                | Int    | Identification number assigned to the channel for the duration of this connection.      |
| \[1]     | MSG\_TYPE                  | String | 'fcs' (funding credits snapshot)                                                        |
| \[2]     | FUNDING\_CREDITS\_SNAPSHOT | Array  | Array with an array of active funding credits(Indices \[0...n] will be funding credits) |
| \[0...n] | FUNDING\_CREDIT\_ARRAY     | Array  | [Funding credit array](#funding-credit-arrays)                                          |

#### Funding credits update data

| Index | Field                  | Type   | Description                                                                                                            |
| :---- | :--------------------- | :----- | :--------------------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID            | Int    | Identification number assigned to the channel for the duration of this connection.                                     |
| \[1]  | MSG\_TYPE              | String | 'fcn' (funding credit new), 'fcu' (funding credit update), 'foc' (funding credit cancel (cancelled or fully executed)) |
| \[2]  | FUNDING\_CREDIT\_ARRAY | Array  | [Funding credit array](#funding-credit-arrays)                                                                         |

#### Funding credit arrays

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
    <tr><td>[0]</td><td>CREDIT_ID</td><td>Integer</td><td>Credit ID</td></tr>
    <tr><td>[1]</td><td>SYMBOL</td><td>String</td><td>The currency of the credit (fUSD, etc)</td></tr>
    <tr><td>[2]</td><td>SIDE</td><td>Int</td><td>1 if you are the lender, 0 if you are both the lender and borrower, -1 if you're the borrower</td></tr>
    <tr><td>[3]</td><td>MTS_CREATE</td><td>Int</td><td>Millisecond Time Stamp when the credit was created</td></tr>
    <tr><td>[4]</td><td>MTS_UPDATE</td><td>Int</td><td>Millisecond Time Stamp when the credit was updated</td></tr>
    <tr><td>[5]</td><td>AMOUNT</td><td>Float</td><td>Amount the credit is for</td></tr>
    <tr><td>[6]</td><td>FLAGS</td><td>Object</td><td>Future params object (stay tuned)</td></tr>
    <tr><td>[7]</td><td>STATUS</td><td>String</td><td>Credit Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[11]</td><td>RATE</td><td>Float</td><td>Rate of the credit</td></tr>
    <tr><td>[12]</td><td>PERIOD</td><td>Int</td><td>Period of the credit</td></tr>
    <tr><td>[13]</td><td>MTS_OPENING</td><td>Int</td><td>Millisecond Time Stamp when the funding was opened</td></tr>
    <tr><td>[14]</td><td>MTS_LAST_PAYOUT</td><td>Int</td><td>Millisecond Time Stamp when the last payout was received</td></tr>
    <tr><td>[15]</td><td>NOTIFY</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[16]</td><td>HIDDEN</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[18]</td><td>RENEW</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[19]</td><td>RATE_REAL</td><td>Float</td><td>The calculated rate for FRR and FRRDELTAFIX</td></tr>
    <tr><td>[20]</td><td>NO_CLOSE</td><td>Int</td><td>0 if false, 1 if true (whether the funding should be closed when the position is closed)</td></tr>
    <tr><td>[21]</td><td>POSITION_PAIR</td><td>String</td><td>The pair of the position that the funding is used for</td></tr>
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
