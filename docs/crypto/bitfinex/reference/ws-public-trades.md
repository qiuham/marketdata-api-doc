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
source_url: 'https://docs.bitfinex.com/reference/ws-public-trades'
updated_at: 2026-11-28
---

# Trades

This channel sends a trade message whenever a trade occurs at Bitfinex. It includes all the pertinent details of the trade, such as price, size and the time of execution. The channel can send funding trade data as well.

```javascript
const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'trades', 
  symbol: 'tBTCUSD' 
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe",  "channel": "trades",  "symbol": "tBTCUSD" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')

ws.on_message = lambda self, evt:  print (evt)
```

```javascript Request / Response
// request
{ 
  event: "subscribe", 
  channel: "trades", 
  symbol: SYMBOL 
}

// response Trading
{
  event: "subscribed",
  channel: "trades",
  chanId: CHANNEL_ID,
  symbol: "tBTCUSD"
  pair: "BTCUSD"
}

{"event":"subscribed","channel":"trades","chanId":19111,"symbol":"tBTCUSD","pair":"BTCUSD"}

// response Funding
{
  event: "subscribed",
  channel: "trades",
  chanId: CHANNEL_ID,
  symbol: "fUSD",
  currency: "USD"
}

{"event":"subscribed","channel":"trades","chanId":339521,"symbol":"fUSD","currency":"USD"}
```
```javascript Snapshot
// on trading pairs (ex. tBTCUSD)

[
  17470, //CHANNEL_ID
  [
    [
      401597393, //ID
      1574694475039, //MTS
      0.005, //AMOUNT
      7244.9 //PRICE
    ], //TRADE
    ...
  ] //SNAPSHOT
]  

// on funding currencies (ex. fUSD)
 
[
  339521, //CHANNEL_ID
  [
    [
      133323072, //ID
      1574694245478, //MTS
      -258.7458086, //AMOUNT
      0.0002587, //RATE
      2 //PERIOD
    ], //TRADE
    ...
  ]
]
```
```javascript Update
// on trading pairs (ex. tBTCUSD)

[
  17470, //CHANNEL_ID
  "te", //MSG_TYPE
  [
    401597395, //ID
    1574694478808, //MTS
    0.005, //AMOUNT
    7245.3 //PRICE
  ] //TRADE
]

// on funding currencies (ex. fUSD)

[
  337371, //CHANNEL_ID
  "fte", //MSG_TYPE
  [
    133323543, //ID
    1574694605000, //MTS
    -59.84, //AMOUNT
    0.00023647, //RATE
    2 //PERIOD
  ] //TRADE
]

```

#### Request fields

| Fields | Type   | Description                      |
| ------ | ------ | -------------------------------- |
| SYMBOL | String | Trading pair or funding currency |

#### Trade snapshot data

| Index    | Field       | Type  | Description                                                                        |
| :------- | :---------- | :---- | :--------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection. |
| \[1]     | SNAPSHOT    | Array | Array with an array of recent trades (Indices \[0...n] will be trades)             |
| \[0...n] | TRADE       | Array | [Trade array](#trade-arrays) or [funding trade array](#funding-trade-arrays)       |

#### Trade update data

| Index | Field       | Type   | Description                                                                                               |
| :---- | :---------- | :----- | :-------------------------------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int    | Identification number assigned to the channel for the duration of this connection.                        |
| \[1]  | MSG\_TYPE   | String | "te" (trade executed), "tu" (trade updated), "fte" (funding trade executed), "ftu" (funding trade updated |
| \[2]  | TRADE       | Trade  | [Trade array](#trade-arrays) or [funding trade array](#funding-trade-arrays)                              |

#### Trade arrays

| Index | Field  | Type  | Description                                  |
| :---- | :----- | :---- | :------------------------------------------- |
| \[0]  | ID     | Int   | Trade ID                                     |
| \[1]  | MTS    | Int   | Millisecond time stamp                       |
| \[2]  | AMOUNT | Float | Amount bought (positive) or sold (negative). |
| \[3]  | PRICE  | Float | Price at which the trade was executed        |

#### Funding trade arrays

| Index | Field  | Type  | Description                                                |
| :---- | :----- | :---- | :--------------------------------------------------------- |
| \[0]  | ID     | Int   | Trade ID                                                   |
| \[1]  | MTS    | Int   | Millisecond time stamp                                     |
| \[2]  | AMOUNT | Float | Amount of funding provided (positive) or taken (negative). |
| \[3]  | RATE   | Float | Funding rate of the trade                                  |
| \[4]  | PERIOD | Int   | Funding offer period in days                               |

> 📘 Amount
>
> The order that causes the trade (the taker) determines if it is a buy or a sell (for trades) or if funding is provided or taken (for funding)

<br/>
