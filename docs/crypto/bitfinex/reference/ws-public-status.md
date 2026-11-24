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
source_url: 'https://docs.bitfinex.com/reference/ws-public-status'
updated_at: 2026-11-24
---

# Status

Subscribe to and receive different types of platform information - currently supports derivatives pair status and liquidation feed.

```javascript
const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'status', 
  key: 'deriv:tBTCF0:USTF0' 
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe",  "channel": "status",  "key": "deriv:tBTCF0:USTF0" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "status", "key": "deriv:tBTCF0:USTF0"}')

ws.on_message = lambda self, evt:  print (evt)
```

<br />

```javascript Request / Response
// request
{ 
  event: "subscribe", 
  channel: "status", 
  key: KEY
}

// response - 
{
   event: "subscribed",
   channel: "status",
   chanId: CHANNEL_ID,
   key: KEY
}

//Derivative pair status
{"event":"subscribed","channel":"status","chanId":335856,"key":"deriv:tBTCF0:USTF0"}

//Liquidation feed
{"event":"subscribed","channel":"status","chanId":91684,"key":"liq:global"}
```
```javascript Update
// Derivatives Status

[
  335856, //CHANNEL_ID
  [
    1596124822000, //TIME_MS
    null, //PLACEHOLDER
    0.896, //DERIV_PRICE
    0.771995, //SPOT_PRICE
    null, //PLACEHOLDER
    1396531.67460709, //INSURANCE_FUND_BALANCE
    null, //PLACEHOLDER
    1596153600000, //NEXT_FUNDING_EVT_TIMESTAMP_MS
    0.0001056, //NEXT_FUNDING_ACCRUED
    6, //NEXT_FUNDING_STEP
    null, //PLACEHOLDER
    -0.01381344, //CURRENT_FUNDING
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    0.7664, //MARK_PRICE
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    246502.09001551, //OPEN_INTEREST
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    null, //CLAMP_MIN
    0.3 //CLAMP_MAX
  ] //DERIVATIVE_STATUS_ARRAY
]

// Liquidation feed updates

[
  91684, //CHANNEL_ID
  [
    [
      "pos", //MSG_TYPE
      142397657, //POS_ID
      1574697680828.2002, //TIME_MS
      null, //PLACEHOLDER
      "tBSVUSD", //SYMBOL
      -2.62932, //AMOUNT
      91.583875238719, //BASE_PRICE
      null, //PLACEHOLDER
      1, //IS_MATCH
      1, //IS_MARKET_SOLD
      null, //PLACEHOLDER
      112.27 //LIQUIDATION_PRICE
    ] //LIQUIDATION_ARRAY
  ] //LIQUIDATIONS
]
```

#### Request fields

| Keys                                       | Type   | Description                                         |
| :----------------------------------------- | :----- | :-------------------------------------------------- |
| "deriv:SYMBOL" (e.g. "deriv:tBTCF0:USTF0") | String | Used to subscribe to derivative pair status updates |
| "liq:global"                               | String | Used to subscribe to liquidation feed updates       |

#### Status update data

| Index | Field       | Type  | Description                                                                                                |
| :---- | :---------- | :---- | :--------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection.                         |
| \[1]  | UPDATE      | Array | [Derivative status array](#derivative-status-array-index-1) or [Liquidations array](#liquidations-index-1) |

#### Derivative status array (Index \[1])

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
    <tr><td>[0]</td><td>TIME_MS</td><td>Int</td><td>Millisecond timestamp</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[2]</td><td>DERIV_PRICE</td><td>Float</td><td>Derivative book mid price.</td></tr>
    <tr><td>[3]</td><td>SPOT_PRICE</td><td>Float</td><td>Book mid price of the underlying Bitfinex spot trading pair</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[5]</td><td>INSURANCE_FUND_BALANCE</td><td>Float</td><td>The balance available to the liquidation engine to absorb losses.</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[7]</td><td>NEXT_FUNDING_EVT_TIMESTAMP_MS</td><td>Int</td><td>Millisecond timestamp of next funding event</td></tr>
    <tr><td>[8]</td><td>NEXT_FUNDING_ACCRUED</td><td>Float</td><td>Current accrued funding for next 8h period</td></tr>
    <tr><td>[9]</td><td>NEXT_FUNDING_STEP</td><td>Int</td><td>Incremental accrual counter</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[11]</td><td>CURRENT_FUNDING</td><td>Float</td><td>Funding applied in the current 8h period</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[14]</td><td>MARK_PRICE</td><td>Float</td><td>Price based on the BFX Composite Index</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[17]</td><td>OPEN_INTEREST</td><td>Float</td><td>Current open interest</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[21]</td><td>CLAMP_MIN</td><td>Float</td><td>Range in the average spread that does not require a funding payment</td></tr>
    <tr><td>[22]</td><td>CLAMP_MAX</td><td>Float</td><td>Funding payment cap</td></tr>
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

#### Liquidations (Index \[1])

| Index     | Field              | Type  | Description                                     |
| :-------- | :----------------- | :---- | :---------------------------------------------- |
| \[0....n] | LIQUIDATION\_ARRAY | Array | [Liquidation array](#liquidation-array-index-1) |

#### Liquidation array (Index \[0...n])

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
    <tr><td>[0]</td><td>MSG_TYPE</td><td>String</td><td>Type of message ('pos')</td></tr>
    <tr><td>[1]</td><td>POS_ID</td><td>Int</td><td>Position id</td></tr>
    <tr><td>[2]</td><td>TIME_MS</td><td>Int</td><td>Millisecond timestamp</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[4]</td><td>SYMBOL</td><td>String</td><td>Trading pair</td></tr>
    <tr><td>[5]</td><td>AMOUNT</td><td>Float</td><td>Amount of the liquidated position</td></tr>
    <tr><td>[6]</td><td>BASE_PRICE</td><td>Float</td><td>Base price of the liquidated position</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[8]</td><td>IS_MATCH</td><td>Int</td><td>0 -> initial liquidation trigger, 1 market execution</td></tr>
    <tr><td>[9]</td><td>IS_MARKET_SOLD</td><td>Int</td><td>0 -> direct sell into the market, 1 position acquired by the system</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[11]</td><td>LIQUIDATION_PRICE</td><td>Float</td><td>Price at which the liquidation was triggered</td></tr>
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
