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
source_url: 'https://docs.bitfinex.com/reference/ws-public-books'
updated_at: 2026-11-27
---

# Books

The Order Books channel allows you to keep track of the state of the Bitfinex order book.
It is provided on a price aggregated basis with customizable precision.
Upon connecting, you will receive a snapshot of the book
followed by updates for any changes to the state of the book.

```javascript
const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'book', 
  symbol: 'tBTCUSD' 
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe", "channel": "book", "symbol": "tBTCUSD" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "book", "symbol": "tBTCUSD"}')

ws.on_message = lambda self, evt:  print (evt)
```

```javascript Request / Response
// request
{
	event: 'subscribe',
	channel: 'book',
	symbol: SYMBOL,
	prec: PRECISION,
	freq: FREQUENCY,
	len: LENGTH,
	subId: SUBID
}

{"event":"subscribe","channel":"book","symbol":"tBTCUSD","prec":"P0","freq":"F0","len":"25","subId": 123}

// response
{
	event: 'subscribed',
	channel: 'book',
	chanId: CHANNEL_ID,
	symbol: SYMBOL,
	prec: PRECISION,
	freq: FREQUENCY,
	len: LENGTH,
	subId: SUBID,
	pair: PAIR 
}

{"event":"subscribed","channel":"book","chanId":10092,"symbol":"tETHUSD","prec":"P0","freq":"F0","len":"25","subId":123,"pair":"ETHUSD"}
```
```javascript Snapshot
// on trading pairs (ex. tBTCUSD)

[
  17082, //CHANNEL_ID
  [
    [
      7254.7, //PRICE
      3, //COUNT
      3.3 //AMOUNT
    ], //BOOK_ENTRY
    ...
  ] //BOOK_ENTRIES
]
  
// on funding currencies (ex. fUSD)

[
  431549, //CHANNEL_ID
  [
    [
      0.00023112, //RATE
      30, //PERIOD
      1, //COUNT
      -15190.7005375 //AMOUNT
    ], //BOOK_ENTRY
    ...
  ] //BOOK_ENTRIES
]
```
```javascript Update
// on trading pairs (ex. tBTCUSD)

[
  17082, //CHANNEL_ID
  [
    7254.5, //PRICE
    0, //COUNT
    1 //AMOUNT
  ] //BOOK_ENTRY
]
  
// on funding currencies (ex. fUSD)

[
  348748, //CHANNEL_ID
  [
    0.00023157, //RATE
    2, //PERIOD
    1, //COUNT
    66.35007188 //AMOUNT
  ] //BOOK_ENTRY
]
```
```javascript Update (Bulk)
//Bulk updates can be enabled using a conf event flag of 536870912

// on trading pairs (ex. tBTCUSD)

[
  17082, //CHANNEL_ID
  [
    [
      7254.5, //PRICE
      0, //COUNT
      1 //AMOUNT
    ], //BOOK_ENTRY
  	...
  ] //BOOK_ENTRIES
]
  
// on funding currencies (ex. fUSD)

[
  348748, //CHANNEL_ID
  [
    [
      0.00023157, //RATE
      2, //PERIOD
      1, //COUNT
      66.35007188 //AMOUNT
    ], //BOOK_ENTRY
    ...
  ]//BOOK_ENTRIES
]
```

#### Request fields

| Fields    | Type   | Description                                                                      |
| --------- | ------ | -------------------------------------------------------------------------------- |
| SYMBOL    | String | Trading pair or funding currency                                                 |
| PRECISION | string | Level of price aggregation (P0, P1, P2, P3, P4).<br/>The default is P0           |
| FREQUENCY | string | Frequency of updates (F0, F1).<br/>F0=realtime / F1=2sec.<br/>The default is F0. |
| LENGTH    | string | Number of price points ("1", "25", "100", "250") \[default="25"]                 |
| SUBID     | string | Optional user-defined ID for the subscription                                    |

#### Book snapshot data

| Index    | Field         | Type  | Description                                                                                  |
| :------- | :------------ | :---- | :------------------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID   | Int   | Identification number assigned to the channel for the duration of this connection.           |
| \[1]     | BOOK\_ENTRIES | Array | Array with an array of currently active book entries (Indices \[0...n] will be book entries) |
| \[0...n] | BOOK\_ENTRY   | Array | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)                       |

#### Book update data

| Index | Field       | Type  | Description                                                                        |
| :---- | :---------- | :---- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | BOOK\_ENTRY | Trade | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)             |

#### Bulk update date

| Index    | Field         | Type  | Description                                                                                  |
| :------- | :------------ | :---- | :------------------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID   | Int   | Identification number assigned to the channel for the duration of this connection.           |
| \[1]     | BOOK\_ENTRIES | Array | Array with an array of currently active book entries (Indices \[0...n] will be book entries) |
| \[0...n] | BOOK\_ENTRY   | Array | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)                       |

#### Book entry

| Index | Field  | Type  | Description                                                                                                                     |
| :---- | :----- | :---- | :------------------------------------------------------------------------------------------------------------------------------ |
| \[0]  | PRICE  | Float | Price level                                                                                                                     |
| \[1]  | COUNT  | Int   | Number of orders at that price level (delete price level if count = 0)                                                          |
| \[2]  | AMOUNT | Float | Total amount available at that price level. Trading: if AMOUNT > 0 then bid else ask; Funding: if AMOUNT < 0 then bid else ask; |

#### Funding book entry

| Index | Field  | Type  | Description                                                                                                                     |
| :---- | :----- | :---- | :------------------------------------------------------------------------------------------------------------------------------ |
| \[0]  | RATE   | Float | Price level                                                                                                                     |
| \[1]  | PERIOD | Int   | Period level                                                                                                                    |
| \[2]  | COUNT  | Int   | Number of orders at that price level (delete price level if count = 0)                                                          |
| \[3]  | AMOUNT | Float | Total amount available at that price level. Trading: if AMOUNT > 0 then bid else ask; Funding: if AMOUNT < 0 then bid else ask; |

**Algorithm to create and keep a trading book instance updated**

1. subscribe to channel
2. receive the book snapshot and create your in-memory book structure
3. when *count* > 0 then you have to add or update the price level\
   3.1 if *amount* > 0 then add/update bids\
   3.2 if *amount* < 0 then add/update asks
4. when *count* = 0 then you have to delete the price level.\
   4.1 if *amount* = 1 then remove from bids\
   4.2 if *amount* = -1 then remove from asks

**Algorithm to create and keep a funding book instance updated**

1. subscribe to channel
2. receive the book snapshot and create your in-memory book structure
3. when *count* > 0 then you have to add or update the price level\
   3.1 if *amount* > 0 then add/update asks (offers)\
   3.2 if *amount* < 0 then add/update bids
4. when *count* = 0 then you have to delete the price level.\
   4.1 if *amount* = 1 then remove from asks (offers)\
   4.2 if *amount* = -1 then remove from bids

Node.JS example gists:

* Aggregated Book: <https://gist.github.com/prdn/b8c067c758aab7fa3bf715101086b47c>
* Raw Book: <https://gist.github.com/prdn/b9c9c24fb1bb38604dcd1e94ee89dd9e>

**Precision Levels**

* Significant Digits Calculations: <https://support.bitfinex.com/hc/en-us/articles/115000371105-How-is-precision-calculated-using-Significant-Digits>

| Precision Level | Number of significant figures |
| --------------- | ----------------------------- |
| P0              | 5                             |
| P1              | 4                             |
| P2              | 3                             |
| P3              | 2                             |
| P4              | 1                             |

**Checksum**\
An Order Book Checksum can be requested through the Websocket configuration. You can find out more on the [WebSocket Checksum](https://docs.bitfinex.com/docs/ws-websocket-checksum) page.

**Bulk Updates**\
Bulk updates can be enabled by sending a [conf event](https://docs.bitfinex.com/docs/ws-general#configuration) with a flag value of 536870912. With bulk updates enabled, updates will arrive as an array of arrays.

> 🚧 Error Codes
>
> 10011 : Unknown Book precision\
> 10012 : Unknown Book length
