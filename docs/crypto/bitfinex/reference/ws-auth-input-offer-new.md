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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input-offer-new'
updated_at: 2026-11-22
---

# New Offer

Create a new funding offer.

Create a new funding offer by constructing a payload using the "fon" (funding offer new) abbreviation and include an offer details object. Please look to the sidebar for examples.

Upon sending an offer, you will receive a confirmation as an 'n' (notification) event and, if the offer is placed successfully, a confirmation through a "fon" (funding offer new) event. Example responses are included in the sidebar. Please look to the [Funding Offers](https://docs.bitfinex.com/reference/ws-auth-funding-offers) and [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications) pages for further information.

Funding offer inputs require you to run the authentication code along with additional code for the input. The authentication code can be found  on our [Authenticated Channels](https://docs.bitfinex.com/docs/ws-auth) and the additional code for inputs can be found on the [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input) page.

```json Payload
// Model
[
  0,
  "fon",
  null,
  {
    type: TYPE,
    symbol: SYMBOL,
    amount: AMOUNT,
    rate: RATE,
    period: PERIOD,
    flags: FLAGS
  }
]

// Examples
[
  0, 
  'fon', 
  null, 
  { 
    type: "LIMIT", 
    symbol: "fUSD", 
    amount: '50', 
    rate: '0.0002', 
    period: 7, 
    flags: 0 
  }
]

[
  0, 
  'fon', 
  null, 
  { 
    type: "FRRDELTAVAR", 
    symbol: "fUSD", 
    amount: '-50', 
    rate: '0.0001', 
    period: 7, 
    flags: 64 
  }
]
```
```json Response
// When the offer request is submitted you will receive an 'n' (notification) event as confirmation. If the offer placement is successful, you will also receive an 'fon' (funding offer new) event. Both events are sent through CHANNEL_ID = 0.

[
  0, // CHANNEL_ID
  "n", // EVENT
  [
    1575293958819, // MTS
    "fon-req", // TYPE
    null, // MESSAGE_ID
    null, // _PLACEHOLDER
    [
      41238934, // ID
      null, // SYMBOL
      null, // MTS_CREATED
      null, // MTS_UPDATED
      500, // AMOUNT
      null, // AMOUNT_ORIG
      null, // OFFER_TYPE
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      null, // FLAGS
      null, // OFFER_STATUS
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      null, // _PLACEHOLDER
      0.02, // RATE
      2, // PERIOD
      null, // NOTIFY
      null, // HIDDEN
      null, // _PLACEHOLDER
      null, // RENEW
      null // _PLACEHOLDER
    ],
    null, // CODE
    "SUCCESS", // STATUS
    "Submitting funding offer of 500.0 UST at 2.000 for 2 days." // TEXT
  ]
]

[
  0, // CHANNEL_ID
  "fon", // EVENT
  [
    41238934, // ID
    "fUST", // SYMBOL
    1575293959000, // MTS_CREATED
    1575293959000, // MTS_UPDATED
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
  ]
]

```

> 🚧 FRR offer
>
> To place an FRR offer, use type FRRDELTAVAR and specify the rate as 0. This will place an FRRDELTAVAR offer with an offset of 0.

#### Request fields

| Name   | Type           | Description                                             |
| ------ | -------------- | ------------------------------------------------------- |
| type   | String         | LIMIT, FRRDELTAVAR, FRRDELTAFIX                         |
| symbol | String         | Symbol (fUSD, fBTC, ...)                                |
| amount | Decimal string | Amount (> 0 for offer, < 0 for bid)                     |
| rate   | Decimal string | Rate (or offset for FRRDELTA offers)                    |
| period | Decimal        | Time period of offer. Minimum 2 days. Maximum 120 days. |
| flags  | Int            | See `<https://docs.bitfinex.com/v2/docs/flag-values>`.  |

#### New offer notification data

| Index | Field               | Type   | Description                                                                                               |
| :---- | :------------------ | :----- | :-------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID         | Int    | ID of the channel. (0 for account info messages)                                                          |
| \[1]  | EVENT               | String | Type of event ('n' for notification)                                                                      |
| \[2]  | NOTIFICATION\_ARRAY | Array  | [Notification array](https://docs.bitfinex.com/reference/ws-auth-input-offer-new#notification-array-data) |

#### Notification array data

| Index | Field         | Type            | Description                                                                                |
| :---- | :------------ | :-------------- | :----------------------------------------------------------------------------------------- |
| \[0]  | MTS           | Int             | Millisecond Time Stamp of the update                                                       |
| \[1]  | TYPE          | String          | Purpose of notification ('fon-req')                                                        |
| \[2]  | MESSAGE\_ID   | Int             | Unique ID of the message                                                                   |
| \[3]  | \_PLACEHOLDER |                 |                                                                                            |
| \[4]  | OFFER\_ARRAY  | Array           | [Offer data](https://docs.bitfinex.com/reference/ws-auth-input-offer-new#offer-array-data) |
| \[5]  | CODE          | Null or integer | Work in progress                                                                           |
| \[6]  | STATUS        | String          | Status of the notification; it may vary over time (SUCCESS, ERROR, FAILURE, ...)           |
| \[7]  | TEXT          | String          | Text of the notification                                                                   |

#### "fon" event data

| Index | Field        | Type   | Description                                                                                |
| :---- | :----------- | :----- | :----------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | ID of the channel. (0 for account info messages)                                           |
| \[1]  | TYPE         | String | Type of event ('fon' for funding offer new)                                                |
| \[2]  | OFFER\_ARRAY | Array  | [Offer data](https://docs.bitfinex.com/reference/ws-auth-input-offer-new#offer-array-data) |

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
