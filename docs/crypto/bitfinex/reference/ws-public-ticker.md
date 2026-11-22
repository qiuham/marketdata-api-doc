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
source_url: 'https://docs.bitfinex.com/reference/ws-public-ticker'
updated_at: 2026-11-22
---

# Ticker

The ticker endpoint provides a high level overview of the state of the market for a specified pair. It shows the current best bid and ask, the last traded price, as well as information on the daily volume and price movement over the last day.

```javascript
const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'ticker', 
  symbol: 'tBTCUSD' 
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe",  "channel": "ticker",  "symbol": "tBTCUSD" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}')

ws.on_message = lambda self, evt:  print (evt)
```

```javascript Request / Response
// request
{ 
  event: "subscribe", 
  channel: "ticker", 
  symbol: SYMBOL
}

// response - trading
{
   event: "subscribed",
   channel: "ticker",
   chanId: CHANNEL_ID,
   symbol: SYMBOL,
   pair: PAIR
}

{"event":"subscribed","channel":"ticker","chanId":224555,"symbol":"tBTCUSD","pair":"BTCUSD"}

// response - funding
{
  event: "subscribed",
  channel: "ticker",
  chanId: CHANNEL_ID,
  symbol: SYMBOL,
  currency: CURRENCY
}

{"event":"subscribed","channel":"ticker","chanId":232591,"symbol":"fUSD","currency":"USD"}
```
```javascript Snapshot
// Trading pairs

[
  443378, //CHANNEL_ID
  [
    7616.5, //BID
    31.89055171, //BID_SIZE
    7617.5, //ASK
    43.358118629999986, //ASK_SIZE
    -550.8, //DAILY_CHANGE
    -0.0674, //DAILY_CHANGE_RELATIVE
    7617.1, //LAST_PRICE
    8314.71200815, //VOLUME
    8257.8, //HIGH
    7500, //LOW
    1358182043000 //FIRST_TRADE
  ] //UPDATE
]

// Funding pairs

[
  234509, //CHANNEL_ID
  [
    0.0003193369863013699, //FRR
    0.0002401, //BID
    30, //BID_PERIOD
    3939629.6177260396, //BID_SIZE
    0.00019012, //ASK
    2, //ASK_PERIOD
    307776.1592138799, //ASK_SIZE
    -0.00005823, //DAILY_CHANGE
    -0.2344, //DAILY_CHANGE_RELATIVE
    0.00019016, //LAST_PRICE
    122156333.45260866, //VOLUME
    0.00027397, //HIGH
    6.8e-7, //LOW
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    3441851.73330503, //FRR_AMOUNT_AVAILABLE
    1469734163000 //FIRST_TRADE
  ] //UPDATE
]
```
```javascript Update
// Trading pairs

[
  443378, //CHANNEL_ID
  [
    7616.5, //BID
    31.89055171, //BID_SIZE
    7617.5, //ASK
    43.358118629999986, //ASK_SIZE
    -550.8, //DAILY_CHANGE
    -0.0674, //DAILY_CHANGE_RELATIVE
    7617.1, //LAST_PRICE
    8314.71200815, //VOLUME
    8257.8, //HIGH
    7500, //LOW
    1358182043000 //FIRST_TRADE
  ] //UPDATE
]

// Funding pairs

[
  234509, //CHANNEL_ID
  [
    0.0003193369863013699, //FRR
    0.0002401, //BID
    30, //BID_PERIOD
    3939629.6177260396, //BID_SIZE
    0.00019012, //ASK
    2, //ASK_PERIOD
    307776.1592138799, //ASK_SIZE
    -0.00005823, //DAILY_CHANGE
    -0.2344, //DAILY_CHANGE_RELATIVE
    0.00019016, //LAST_PRICE
    122156333.45260866, //VOLUME
    0.00027397, //HIGH
    6.8e-7, //LOW
    null, //PLACEHOLDER
    null, //PLACEHOLDER
    3441851.73330503, //FRR_AMOUNT_AVAILABLE
    1469734163000 //FIRST_TRADE
  ] //UPDATE
]
```

#### Request fields

| Fields | Type   | Description                      |
| ------ | ------ | -------------------------------- |
| SYMBOL | String | Trading pair or funding currency |

#### Stream data

| Index | Field       | Type  | Description                                                                                                                                         |
| :---- | :---------- | :---- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection.                                                                  |
| \[1]  | UPDATE      | Array | Array with relevant data ([trading snapshot/update](#trading-snapshotupdate-index-1) or [funding snapshot/update](#funding-snapshotupdate-index-1)) |

#### Trading snapshot/update (Index \[1])

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
    <tr><td>[0]</td><td>BID</td><td>Float</td><td>Price of last highest bid</td></tr>
    <tr><td>[1]</td><td>BID_SIZE</td><td>Float</td><td>Sum of the 25 highest bid sizes</td></tr>
    <tr><td>[2]</td><td>ASK</td><td>Float</td><td>Price of last lowest ask</td></tr>
    <tr><td>[3]</td><td>ASK_SIZE</td><td>Float</td><td>Sum of the 25 lowest ask sizes</td></tr>
    <tr><td>[4]</td><td>DAILY_CHANGE</td><td>Float</td><td>Amount that the last price has changed since yesterday</td></tr>
    <tr><td>[5]</td><td>DAILY_CHANGE_RELATIVE</td><td>Float</td><td>Relative price change since yesterday (*100 for percentage change)</td></tr>
    <tr><td>[6]</td><td>LAST_PRICE</td><td>Float</td><td>Price of the last trade.</td></tr>
    <tr><td>[7]</td><td>VOLUME</td><td>Float</td><td>Daily volume</td></tr>
    <tr><td>[8]</td><td>HIGH</td><td>Float</td><td>Daily high</td></tr>
    <tr><td>[9]</td><td>LOW</td><td>Float</td><td>Daily low</td></tr>
    <tr><td>[10]</td><td>FIRST_TRADE</td><td>int</td><td>Timestamp of the first trade</td></tr>
  </tbody>
</table>
`}</HTMLBlock>

#### Funding snapshot/update (Index \[1])

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
    <tr><td>[0]</td><td>FRR</td><td>Float</td><td>Flash Return Rate - average of all fixed rate funding over the last hour (funding tickers only)</td></tr>
    <tr><td>[1]</td><td>BID</td><td>Float</td><td>Price of last highest bid</td></tr>
    <tr><td>[2]</td><td>BID_PERIOD</td><td>Int</td><td>Bid period covered in days (funding tickers only)</td></tr>
    <tr><td>[3]</td><td>BID_SIZE</td><td>Float</td><td>Sum of the 25 highest bid sizes</td></tr>
    <tr><td>[4]</td><td>ASK</td><td>Float</td><td>Price of last lowest ask</td></tr>
    <tr><td>[5]</td><td>ASK_PERIOD</td><td>Int</td><td>Ask period covered in days (funding tickers only)</td></tr>
    <tr><td>[6]</td><td>ASK_SIZE</td><td>Float</td><td>Sum of the 25 lowest ask sizes</td></tr>
    <tr><td>[7]</td><td>DAILY_CHANGE</td><td>Float</td><td>Amount that the last price has changed since yesterday</td></tr>
    <tr><td>[8]</td><td>DAILY_CHANGE_RELATIVE</td><td>Float</td><td>Relative price change since yesterday (*100 for percentage change)</td></tr>
    <tr><td>[9]</td><td>LAST_PRICE</td><td>Float</td><td>Price of the last trade.</td></tr>
    <tr><td>[10]</td><td>VOLUME</td><td>Float</td><td>Daily volume</td></tr>
    <tr><td>[11]</td><td>HIGH</td><td>Float</td><td>Daily high</td></tr>
    <tr><td>[12]</td><td>LOW</td><td>Float</td><td>Daily low</td></tr>
    <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
    <tr><td>[15]</td><td>FRR_AMOUNT_AVAILABLE</td><td>Float</td><td>The amount of funding that is available at the Flash Return Rate (funding tickers only)</td></tr>
    <tr><td>[16]</td><td>FIRST_TRADE</td><td>int</td><td>Timestamp of the first trade</td></tr>
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
