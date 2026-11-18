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
source_url: 'https://docs.bitfinex.com/reference/ws-public-candles'
updated_at: 2026-11-18
---

# Candles

The Candles endpoint provides OCHL (Open, Close, High, Low) and volume data for the specified trading pair.

```javascript
//Trading Candles

const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'candles', 
  key: 'trade:1m:tBTCUSD' //'trade:TIMEFRAME:SYMBOL'
})

w.on('open', () => w.send(msg))

//Funding Candles

const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'candles', 
  key: 'trade:1m:fUSD:a30:p2:p30' //'trade:TIMEFRAME:SYMBOL:aAGGR:pPER_START:pEND'
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }')

ws.on_message = lambda self, evt:  print (evt)
```

```javascript Request / Response
// request
{
   event: "subscribe",
   channel: "candles",
   key: "trade:1m:tBTCUSD"
}

// response
{
  event: "subscribed",
  channel: "candles",
  chanId": CHANNEL_ID,
  key: "trade:1m:tBTCUSD"
}

{"event":"subscribed","channel":"candles","chanId":343351,"key":"trade:1m:tBTCUSD"}
```
```javascript Snapshot
[
  343351, //CHANNEL_ID
  [
    [
      1574698260000, //MTS
      7379.785503, //OPEN
      7383.8, //CLOSE
      7388.3, //HIGH
      7379.785503, //LOW
      1.68829482 //VOLUME
    ], //CANDLE
    ...
  ] //SNAPSHOT
]
```
```javascript Update
[
  343351, //CHANNEL_ID
  [
    1574698200000, //MTS
    7399.9, //OPEN
    7379.7, //CLOSE
    7399.9, //HIGH
    7371.8, //LOW
    41.63633658 //VOLUME
  ] //CANDLE
]
```

#### Request fields

| Fields        | Type   | Description                                                                                                                         |
| ------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| KEY           | string | Specify the time frame and symbol ('trade:TIMEFRAME:SYMBOL').                                                                       |
| KEY (funding) | string | Specify the time frame and symbol along with the pPeriod or an aAGGR aggregated period using a Pper\_start and Pper\_end parameter. |

> 🚧 Funding Candles
>
> Be sure to specify a period or aggregated period when retrieving funding candles. If you wish to mimic the candles found in the UI, use the following setup to aggregate all funding candles: a30:p2:30

#### Candle snapshot data

| Index    | Field       | Type  | Description                                                                        |
| :------- | :---------- | :---- | :--------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection. |
| \[1]     | SNAPSHOT    | Array | Array with an array of recent candles (Indices \[0...n] will be candles)           |
| \[0...n] | CANDLE      | Array | [Candle array](#candle-arrays)                                                     |

#### Candle update data

| Index | Field       | Type  | Description                                                                        |
| :---- | :---------- | :---- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | CANDLE      | Array | [Candle array](#candle-arrays)                                                     |

#### Candle arrays

| Index | Fields | Type  | Description                                    |
| ----- | :----- | ----- | ---------------------------------------------- |
| \[0]  | MTS    | int   | millisecond time stamp                         |
| \[1]  | OPEN   | float | First execution during the time frame          |
| \[2]  | CLOSE  | float | Last execution during the time frame           |
| \[3]  | HIGH   | float | Highest execution during the time frame        |
| \[4]  | LOW    | float | Lowest execution during the timeframe          |
| \[5]  | VOLUME | float | Quantity of symbol traded within the timeframe |

**Time frames**

* 1m:  one minute
* 5m : five minutes
* 15m : 15 minutes
* 30m : 30 minutes
* 1h : one hour
* 3h : 3 hours
* 6h : 6 hours
* 12h : 12 hours
* 1D : one day
* 1W : one week
* 14D : two weeks
* 1M : one month
