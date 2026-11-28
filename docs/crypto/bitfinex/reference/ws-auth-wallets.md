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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-wallets'
updated_at: 2026-11-28
---

# Wallets

Receive a snapshot and updates for any wallet events on your account.

Subscribe to the account information channel to keep track of your wallets. The account information channel provides a snapshot and updates on the wallet events in your account. The snapshot is delivered upon subscribing and any changes to your wallets will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Wallet events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Wallet events will use one of the following abbreviations: 'ws' (wallet snapshot) and 'wu' (wallet update).

```json Snapshot ('ws')

[
  0, //CHAN_ID
  "ws", //MSG_TYPE
  [
    [
      "exchange", //WALLET_TYPE
      "SAN", //CURRENCY
      19.76, //BALANCE
      0, //UNSETTLED_INTEREST
      null, //BALANCE_AVAILABLE
      null, //Used for DESCRIPTION on 'wu' events
      null //Used for META on 'wu' events
    ] //WALLET_ARRAY
  ] //WALLET_SNAPSHOT
]
```
```json Update ('wu')

[
  0, //CHAN_ID
  "wu", //MSG_TYPE
  [ 
    "exchange", //WALLET_TYPE
    "BTC", //CURRENCY
    1.61169184, //BALANCE
    0, //UNSETTLED_INTEREST
    null, //BALANCE_AVAILABLE
    "Exchange 0.01 BTC for USD @ 7804.6", //DESCRIPTION
    {
      "reason":"TRADE",
      "order_id":34988418651,
      "order_id_oppo":34990541044,
      "trade_price":"7804.6",
      "trade_amount":"0.01"
    } //META
  ] //WALLET_ARRAY
]
```

#### Wallet snapshot data

| Index    | Field            | Type   | Description                                                                        |
| :------- | :--------------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID      | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]     | MSG\_TYPE        | String | 'ws' (wallet snapshot)                                                             |
| \[2]     | WALLET\_SNAPSHOT | Array  | Array with an array of wallet arrays(Indices \[0...n] will be wallet arrays)       |
| \[0...n] | WALLET\_ARRAY    | Array  | [Wallet array](#wallet-arrays)                                                     |

#### Wallet update data

| Index | Field         | Type   | Description                                                                        |
| :---- | :------------ | :----- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID   | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | MSG\_TYPE     | String | 'wu' (wallet update)                                                               |
| \[2]  | WALLET\_ARRAY | Array  | [Wallet array](#wallet-arrays)                                                     |

#### Wallet array

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
    <tr><td>[0]</td><td>WALLET_TYPE</td><td>String</td><td>Wallet name (exchange, margin, funding)</td></tr>
    <tr><td>[1]</td><td>CURRENCY</td><td>String</td><td>Currency (USD, etc)</td></tr>
    <tr><td>[2]</td><td>BALANCE</td><td>Float</td><td>Wallet balance</td></tr>
    <tr><td>[3]</td><td>UNSETTLED_INTEREST</td><td>Float</td><td>Unsettled interest</td></tr>
    <tr><td>[4]</td><td>BALANCE_AVAILABLE</td><td>Float / Null</td><td>Amount not tied up in active orders, positions or funding (null if the value has not yet been calculated).</td></tr>
    <tr><td>[5]</td><td>DESCRIPTION</td><td>String</td><td>Description of the ledger entry (can be null)</td></tr>
    <tr><td>[6]</td><td>META</td><td>Json</td><td>Provides info on the reason for the wallet update (can be null)</td></tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

> 📘 Important
>
> Certain calculated values (available balance) are only updated periodically. If the value reads 'null', this means that the calculated value is not yet available.
>
> A 'calc' request can be used to to receive an updated value. See [calc input dedicated section](http://docs.bitfinex.com/v2/docs/changelog#section--calc-input-message) for more details.
