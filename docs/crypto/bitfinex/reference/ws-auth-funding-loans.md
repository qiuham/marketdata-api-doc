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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-funding-loans'
updated_at: 2026-11-28
---

# Funding Loans

Receive a snapshot and updates for any funding loans (funds not used in active positions) on your account.

Subscribe to the account information channel to keep track of your funding loans. The account information channel provides a snapshot and updates on the funding loans in your account. The snapshot is delivered upon subscribing and any changes to your funding loans will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Funding loan events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Funding loan events will use one of the following abbreviations: 'fls' (funding loans snapshot), 'fln' (funding loan new), 'flu' (funding loans update), 'flc' (funding loan close).

```json Snapshot ('fls')
[
  0, //CHAN_ID
  "fls", //MSG_TYPE
  [
    [
      26223578, //LOAN_ID
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
    ], //FUNDING_LOAN_ARRAY
    ...
  ] //FUNDING_LOANS_SNAPSHOT
]

[0,"fls",[[2995442,"fUSD",-1,1575291961000,1575295850000,820,0,"ACTIVE",null,null,null,0.002,7,1575282446000,1575295850000,0,0,null,0,null,0]]]
```
```json Update ('fln', 'flu', 'flc')
[
  0, //CHAN_ID
  "fln", //MSG_TYPE
  [
    26223578, //LOAN_ID
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
  ] //FUNDING_LOAN_ARRAY
]
```

#### Funding loans snapshot data

| Index    | Field                    | Type   | Description                                                                         |
| :------- | :----------------------- | :----- | :---------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID              | Int    | Identification number assigned to the channel for the duration of this connection.  |
| \[1]     | MSG\_TYPE                | String | 'fls' (funding loans snapshot)                                                      |
| \[2]     | FUNDING\_LOANS\_SNAPSHOT | Array  | Array with an array of active funding loans(Indices \[0...n] will be funding loans) |
| \[0...n] | FUNDING\_LOAN\_ARRAY     | Array  | [Funding loan array](#funding-loan-arrays)                                          |

#### Funding loans update data

| Index | Field                | Type   | Description                                                                                                      |
| :---- | :------------------- | :----- | :--------------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID          | Int    | Identification number assigned to the channel for the duration of this connection.                               |
| \[1]  | MSG\_TYPE            | String | 'fln' (funding loan new), 'flu' (funding loan update), 'flc' (funding loan cancel (cancelled or fully executed)) |
| \[2]  | FUNDING\_LOAN\_ARRAY | Array  | [Funding loan array](#funding-loan-arrays)                                                                       |

#### Funding loan arrays

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
    <tr><td>[0]</td><td>LOAN_ID</td><td>Integer</td><td>Loan ID</td></tr>
    <tr><td>[1]</td><td>SYMBOL</td><td>String</td><td>The currency of the loan (fUSD, etc)</td></tr>
    <tr><td>[2]</td><td>SIDE</td><td>Int</td><td>1 if you are the lender, 0 if you are both the lender and borrower, -1 if you're the borrower</td></tr>
    <tr><td>[3]</td><td>MTS_CREATE</td><td>Int</td><td>Millisecond Time Stamp when the loan was created</td></tr>
    <tr><td>[4]</td><td>MTS_UPDATE</td><td>Int</td><td>Millisecond Time Stamp when the loan was updated</td></tr>
    <tr><td>[5]</td><td>AMOUNT</td><td>Float</td><td>Amount the loan is for</td></tr>
    <tr><td>[6]</td><td>FLAGS</td><td>Object</td><td>Future params object (stay tuned)</td></tr>
    <tr><td>[7]</td><td>STATUS</td><td>String</td><td>Credit Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[11]</td><td>RATE</td><td>Float</td><td>Rate of the loan</td></tr>
    <tr><td>[12]</td><td>PERIOD</td><td>Int</td><td>Period of the loan</td></tr>
    <tr><td>[13]</td><td>MTS_OPENING</td><td>Int</td><td>Millisecond Time Stamp when the funding was opened</td></tr>
    <tr><td>[14]</td><td>MTS_LAST_PAYOUT</td><td>Int</td><td>Millisecond Time Stamp when the last payout was received</td></tr>
    <tr><td>[15]</td><td>NOTIFY</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[16]</td><td>HIDDEN</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[18]</td><td>RENEW</td><td>Int</td><td>0 if false, 1 if true</td></tr>
    <tr><td>[19]</td><td>RATE_REAL</td><td>Float</td><td>The calculated rate for FRR and FRRDELTAFIX</td></tr>
    <tr><td>[20]</td><td>NO_CLOSE</td><td>Int</td><td>0 if false, 1 if true (whether the funding should be closed when the position is closed)</td></tr>
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
