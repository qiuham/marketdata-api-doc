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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-positions'
updated_at: 2026-11-26
---

# Positions

Receive a snapshot and updates for any position events on your account.

Subscribe to the account information channel to keep track of your positions. The account information channel provides a snapshot and updates on the positions in your account. The snapshot is delivered upon subscribing and any changes to your positions will be provided as updates for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Position events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Positions events will use one of the following abbreviations: 'ps' (positions snapshot), 'pn' (position new), 'pu' (position update), and 'pc' (position close).

```json Snapshot ('ps')
[
  0, //CHAN_ID
  "ps", //TYPE
  [
    [
      "tETHUST", //SYMBOL
      "ACTIVE", //STATUS
      0.2, //AMOUNT
      153.71, //BASE_PRICE
      0, //MARGIN_FUNDING
      0, //MARGIN_FUNDING_TYPE
      null, //PL
      null, //PL_PERC
      null, //PRICE_LIQ
      null, //LEVERAGE
      null, //FLAGS
      142420429, //POSITION_ID
      null, //MTS_CREATE
      null, //MTS_UPDATE
      null, //PLACEHOLDER
      0, //TYPE
      null, //PLACEHOLDER
      0, //COLLATERAL
      null, //COLLATERAL_MIN
      {
        "reason":"TRADE",
        "order_id":34934099168,
        "order_id_oppo":34934090814,
        "liq_stage":null,
        "trade_price":"153.71",
        "trade_amount":"0.2"
      } //META
    ], //POSITION_ARRAY
    ...
  ] //POSITION_SNAPSHOT
]
```
```json Update ('pn', 'pu', 'pc')
[
  0, //CHAN_ID
  "pu", //MSG_TYPE
  [
    "tETHUST", //SYMBOL
    "ACTIVE", //STATUS
    0.2, //AMOUNT
    153.71, //BASE_PRICE
    0, //MARGIN_FUNDING
    0, //MARGIN_FUNDING_TYPE
    -0.07944800000000068, //PL
    -0.05855181835925015, //PL_PERC
    67.52755254906451, //PRICE_LIQ
    1.409288545397275, //LEVERAGE
    null, //FLAGS
    142420429, //POSITION_ID
    null, //MTS_CREATE
    null, //MTS_UPDATE
    null, //PLACEHOLDER
    0, //TYPE
    null, //PLACEHOLDER
    0, //COLLATERAL
    0, //COLLATERAL_MIN
    {
      "reason":"TRADE",
      "order_id":34934099168,
      "order_id_oppo":34934090814,
      "liq_stage":null,
      "trade_price":"153.71",
      "trade_amount":"0.2"
    } //META
  ] //POSITION_ARRAY
]
```

#### Position snapshot data

| Index    | Field              | Type   | Description                                                                        |
| :------- | :----------------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID        | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]     | MSG\_TYPE          | String | 'ps' (position snapshot)                                                           |
| \[2]     | POSITION\_SNAPSHOT | Array  | Array with an array of active positions (Indices \[0...n] will be positions)       |
| \[0...n] | POSITION\_ARRAY    | Array  | [Position array](#position-arrays)                                                 |

#### Position update data

| Index | Field           | Type   | Description                                                                        |
| :---- | :-------------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID     | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | MSG\_TYPE       | String | 'pn' (position new), 'pu' (position update), 'pc' (position close).                |
| \[2]  | POSITION\_ARRAY | Array  | [Position array](#position-arrays)                                                 |

#### Position arrays

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
    <tr><td>[0]</td><td>SYMBOL</td><td>String</td><td>Pair (tBTCUSD, …).</td></tr>
    <tr><td>[1]</td><td>STATUS</td><td>String</td><td>Status (ACTIVE, CLOSED).</td></tr>
    <tr><td>[2]</td><td>AMOUNT</td><td>Float</td><td>Size of the position. Positive values means a long position, negative values means a short position. 0 means position closed.</td></tr>
    <tr><td>[3]</td><td>BASE_PRICE</td><td>Float</td><td>The price at which you entered your position.</td></tr>
    <tr><td>[4]</td><td>MARGIN_FUNDING</td><td>Float</td><td>Current funding cost of the position</td></tr>
    <tr><td>[5]</td><td>MARGIN_FUNDING_TYPE</td><td>Int</td><td>0 for daily, 1 for term.</td></tr>
    <tr><td>[6]</td><td>PL</td><td>Float</td><td>Profit & Loss</td></tr>
    <tr><td>[7]</td><td>PL_PERC</td><td>Float</td><td>Profit & Loss Percentage</td></tr>
    <tr><td>[8]</td><td>PRICE_LIQ</td><td>Float</td><td>Liquidation price ('null' if the value is not updated yet (see notice below))</td></tr>
    <tr><td>[9]</td><td>LEVERAGE</td><td>Float</td><td>For derivative positions</td></tr>
    <tr><td>[10]</td><td>FLAGS</td><td>Int</td><td>Special flags for position</td></tr>
    <tr><td>[11]</td><td>POSITION_ID</td><td>Int</td><td>Position ID</td></tr>
    <tr><td>[12]</td><td>MTS_CREATE</td><td>Int</td><td>Millisecond timestamp of creation</td></tr>
    <tr><td>[13]</td><td>MTS_UPDATE</td><td>Int</td><td>Millisecond timestamp of update</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[15]</td><td>TYPE</td><td>Int</td><td>Identifies the type of position, 0 = Margin position, 1 = Derivatives position</td></tr>
		<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[17]</td><td>COLLATERAL</td><td>Float</td><td>The amount of collateral applied to the open position</td></tr>
    <tr><td>[18]</td><td>COLLATERAL_MIN</td><td>Float</td><td>The minimum amount of collateral required for the position</td></tr>
    <tr><td>[19]</td><td>META</td><td>Json string</td><td>Additional meta information about the position including trade and order IDs</td></tr>
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

> 📘 NOTE
>
> These messages have gained the ability to send the calculation values (liquidation price). If the value is equal to "null" this means that the newly calculated value is not yet available.
>
> A calc request can be sent to request that the value be updated. See [calc input dedicated section](http://docs.bitfinex.com/v2/docs/changelog#section--calc-input-message) for more details.
