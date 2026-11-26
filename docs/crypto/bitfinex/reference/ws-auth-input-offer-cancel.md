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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-offer-cancel'
updated_at: 2026-11-26
---

# Cancel Offer

Cancel a funding offer.

To cancel an offer, construct a payload using the "foc" (funding offer cancel) abbreviation. Include the Offer ID in the payload. Please look to the sidebar for a model and example.

When you cancel an offer, you will receive a message of the appropriated type on the "account info" channel. Example responses are included in the sidebar. Please look to the [Funding Offers](https://docs.bitfinex.com/reference/ws-auth-funding-offers) page for further information.

Funding offer inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Model
[
  0,
  "foc",
  null,
  {
    id: ID
  }
]

// Examples
[
  0, 
  'foc', 
  null, 
  { 
    id: 12345
  }
]
```
```json Response
// When the cancellation request is submitted you will receive an 'n' (notification) event as confirmation. If the cancellation is successful, you will also receive a 'foc' (funding offer cancel) event. Both events are sent through CHANNEL_ID = 0.

[
  0, // CHANNEL_ID
  "n", // EVENT
  [
    1575294374000, // MTS
    "foc-req", // TYPE
    null, // MESSAGE_ID
    null, // _PLACEHOLDER
    [
      41238934, // ID
      "fUST", // SYMBOL
      1575293959000, // MTS_CREATED
      1575294374000, // MTS_UPDATED
      500, // AMOUNT
      500, // AMOUNT_ORIG
      "LIMIT", // OFFER_TYPE
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      0, // FLAGS
      "ACTIVE", // OFFER_STATUS
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      0.02, // RATE
      2, // PERIOD
      0, // NOTIFY
      0, // HIDDEN
      null, // _PLACEHOLDER
      0, // RENEW
      null // _PLACEHOLDER
    ],
    null, // CODE
    "SUCCESS", // STATUS
    "Submitted for cancellation; waiting for confirmation (ID: 41238934)." // TEXT
  ]
]

[
  0, // CHANNEL_ID
  "foc", // EVENT
  [
    41238934, // ID
    "fUST", // SYMBOL
    1575293959000, // MTS_CREATED
    1575294374000, // MTS_UPDATED
    500, // AMOUNT
    500, // AMOUNT_ORIG
    "LIMIT", // OFFER_TYPE
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    0, // FLAGS
    "CANCELED", // OFFER_STATUS
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    null, // _PLACEHOLDER
    0.02, // RATE
    2, // PERIOD
    0, // NOTIFY
    0, // HIDDEN
    null, // _PLACEHOLDER
    0, // RENEW
    null // _PLACEHOLDER
  ]
]

```

#### Request fields

| Name | Type | Description |
| ---- | ---- | ----------- |
| id   | Int  | Offer ID    |

#### Cancel offer notification data

| Index | Field               | Type   | Description                                                                                                  |
| :---- | :------------------ | :----- | :----------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID         | Int    | ID of the channel. (0 for account info messages)                                                             |
| \[1]  | EVENT               | String | Type of event ('n' for notification)                                                                         |
| \[2]  | NOTIFICATION\_ARRAY | Array  | [Notification array](https://docs.bitfinex.com/reference/ws-auth-input-offer-cancel#notification-array-data) |

#### Notification array data

| Index | Field         | Type            | Description                                                                                   |
| :---- | :------------ | :-------------- | :-------------------------------------------------------------------------------------------- |
| \[0]  | MTS           | Int             | Millisecond Time Stamp of the update                                                          |
| \[1]  | TYPE          | String          | Purpose of notification ('foc-req')                                                           |
| \[2]  | MESSAGE\_ID   | Int             | Unique ID of the message                                                                      |
| \[3]  | \_PLACEHOLDER |                 |                                                                                               |
| \[4]  | OFFER\_ARRAY  | Array           | [Offer data](https://docs.bitfinex.com/reference/ws-auth-input-offer-cancel#offer-array-data) |
| \[5]  | CODE          | Null or integer | Work in progress                                                                              |
| \[6]  | STATUS        | String          | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)              |
| \[7]  | TEXT          | String          | Text of the notification                                                                      |

#### "foc" event data

| Index | Field        | Type   | Description                                                                                   |
| :---- | :----------- | :----- | :-------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | ID of the channel. (0 for account info messages)                                              |
| \[1]  | TYPE         | String | Type of event ('foc' for funding offer cancel)                                                |
| \[2]  | OFFER\_ARRAY | Array  | [Offer data](https://docs.bitfinex.com/reference/ws-auth-input-offer-cancel#offer-array-data) |

#### Offer Array data

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
    <tr><td>[0]</td><td>ID</td><td>Int</td><td>Offer ID</td></tr>
    <tr><td>[1]</td><td>SYMBOL</td><td>String</td><td>The currency of the offer (fUSD, etc)</td></tr>
    <tr><td>[2]</td><td>MTS_CREATED</td><td>Int</td><td>Millisecond Time Stamp when the offer was created</td></tr>
    <tr><td>[3]</td><td>MTS_UPDATED</td><td>Int</td><td>Millisecond Time Stamp when the offer was updated</td></tr>
    <tr><td>[4]</td><td>AMOUNT</td><td>Float</td><td>Current amount of the offer</td></tr>
    <tr><td>[5]</td><td>AMOUNT_ORIG</td><td>Float</td><td>Amount of the initial offer</td></tr>
    <tr><td>[6]</td><td>OFFER_TYPE</td><td>String</td><td>Offer Type</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[9]</td><td>FLAGS</td><td>Int</td><td>Flags active on the offer; see https://docs.bitfinex.com/v2/docs/flag-values</td></tr>
    <tr><td>[10]</td><td>OFFER_STATUS</td><td>String</td><td>Offer Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED</td></tr>
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

<br />
