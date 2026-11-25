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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-trades'
updated_at: 2026-11-25
---

# Trades

Receive updates for any trade events on your account.

Subscribe to the account information channel to keep track of your trades. The account information channel will provide a feed of your trades for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Trade events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Trade events will use one of the following abbreviations: 'te' (trade executed) and 'tu' (trade execution update). The 'te' message is sent when a trade is executed while the 'tu' message is sent shortly after containing the trade id (ID) and additional updated fields.

```json Update (te)

[
  0, //CHAN_ID
  "te", //MSG_TYPE
  [
    402088407, //ID
    "tETHUST", //SYMBOL
    1574963975602, //MTS_CREATE
    34938060782, //ORDER_ID
    -0.2, //EXEC_AMOUNT
    153.57, //EXEC_PRICE
    "MARKET", //ORDER_TYPE
    0, //ORDER_PRICE
    -1, //MAKER
    null, //FEE ('tu' only)
    null, //FEE_CURRENCY ('tu' only)
    0 //CID
  ] //TRADE_ARRAY
]
```
```json Update (tu)
  
[
  0, //CHAN_ID
  "tu", //MSG_TYPE
  [
    402088407, //ID
    "tETHUST", //SYMBOL
    1574963975602, //MTS_CREATE
    34938060782, //ORDER_ID
    -0.2, //EXEC_AMOUNT
    153.57, //EXEC_PRICE
    "MARKET", //ORDER_TYPE
    0, //ORDER_PRICE
    -1, //MAKER
    -0.061668, //FEE
    "USD", //FEE_CURRENCY
    1714466193700 //CID
  ] //TRADE_ARRAY
]
```

#### Trade update data

| Index | Field        | Type   | Description                                                                        |
| :---- | :----------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID  | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | MSG\_TYPE    | String | 'te' (trade executed), 'tu' (trade execution update)                               |
| \[2]  | TRADE\_ARRAY | Array  | [Trade array](#trade-arrays)                                                       |

#### Trade arrays

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
    <tr><td>[0]</td><td>ID</td><td>Integer</td><td>Trade database id</td></tr>
    <tr><td>[1]</td><td>SYMBOL</td><td>String</td><td>Symbol (tBTCUSD, …)</td></tr>
    <tr><td>[2]</td><td>MTS_CREATE</td><td>Integer</td><td>Execution timestamp</td></tr>
    <tr><td>[3]</td><td>ORDER_ID</td><td>Integer</td><td>Order id</td></tr>
    <tr><td>[4]</td><td>EXEC_AMOUNT</td><td>Float</td><td>Positive means buy, negative means sell</td></tr>
    <tr><td>[5]</td><td>EXEC_PRICE</td><td>Float</td><td>Execution price</td></tr>
    <tr><td>[6]</td><td>ORDER_TYPE</td><td>String</td><td>Order type</td></tr>
    <tr><td>[7]</td><td>ORDER_PRICE</td><td>Float</td><td>Order price</td></tr>
    <tr><td>[8]</td><td>MAKER</td><td>Int</td><td>1 if true, -1 if false</td></tr>
    <tr><td>[9]</td><td>FEE</td><td>Float</td><td>Fee ('tu' only, returns null for 'te' events)</td></tr>
    <tr><td>[10]</td><td>FEE_CURRENCY</td><td>String</td><td>Fee currency ('tu' only, returns null for 'te' events)</td></tr>
    <tr><td>[11]</td><td>CID</td><td>Integer</td><td>Client Order ID</td></tr>
  </tbody>
</table>
`}</HTMLBlock>
