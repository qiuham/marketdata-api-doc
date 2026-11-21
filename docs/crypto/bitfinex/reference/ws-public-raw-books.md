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
source_url: 'https://docs.bitfinex.com/reference/ws-public-raw-books'
updated_at: 2026-11-21
---

# Raw Books

The Raw Books channel provides the most granular books.

```javascript
const ws = require('ws')
const w = new ws('wss://api-pub.bitfinex.com/ws/2')

w.on('message', (msg) => console.log(msg))

let msg = JSON.stringify({ 
  event: 'subscribe', 
  channel: 'book',
  prec: 'R0',
  symbol: 'tBTCUSD' 
})

w.on('open', () => w.send(msg))
```
```shell
wscat -c wss://api-pub.bitfinex.com/ws/2
{ "event": "subscribe", "channel": "book", "prec": "R0", "symbol": "tBTCUSD" }
```
```python
ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "book", "prec": "R0", "symbol": "tBTCUSD" }')

ws.on_message = lambda self, evt:  print (evt)
```

> 📘 Note
>
> PRICE = 0 means that you have to remove the order from your book.

```json Request / Response
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

{"event":"subscribe","channel":"book","symbol":"tBTCUSD","prec":"R0","freq":"F0","len":"25","subId": 123}
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

{"event":"subscribed","channel":"book","chanId":10092,"symbol":"tETHUSD","prec":"R0","freq":"F0","len":"25","subId":123,"pair":"ETHUSD"}
```
```json Snapshot
// on trading pairs (ex. tBTCUSD)

[
  433290, //CHANNEL_ID
  [
    [
      34753002978, //ORDER_ID
      7294.7, //PRICE
      1.54340371 //AMOUNT
    ], //BOOK_ENTRY
    ...
  ] //BOOK_ENTRIES
]  
  
// on funding currencies (ex. fUSD)

[
  472778, //CHANNEL_ID
  [
    [
      658282397, //OFFER_ID
      30, //PERIOD
      0.000233, //RATE
      -530 //AMOUNT
    ], //BOOK_ENTRY
    ...
  ] //BOOK_ENTRIES
]
```
```javascript Updates
// on trading pairs (ex. tBTCUSD)

[
  433290, //CHANNEL_ID
  [
    34753006045, //ORDER_ID
    0, //PRICE
    -1 //AMOUNT
  ] //BOOK_ENTRY
]
  
// on funding currencies (ex. fUSD)

[
  472778, //CHANNEL_ID
  [
    658286906, //OFFER_ID
    2, //PERIOD
    0, //RATE
    1 //AMOUNT
  ]
]
```
```javascript Updates (Bulk)
//Bulk updates can be enabled using a conf event flag of 536870912

// on trading pairs (ex. tBTCUSD)

[
  433290, //CHANNEL_ID
  [
    [
      34753006045, //ORDER_ID
      0, //PRICE
      -1 //AMOUNT
    ], //BOOK_ENTRY
  	...
  ] //BOOK_ENTRIES
]
  
// on funding currencies (ex. fUSD)

[
  472778, //CHANNEL_ID
  [
    [
      658286906, //OFFER_ID
      2, //PERIOD
      0, //RATE
      1 //AMOUNT
    ], //BOOK_ENTRY
  	...
  ] //BOOK_ENTRIES
]
```

#### Request fields

| Fields | Type   | Description                                                      |
| ------ | ------ | ---------------------------------------------------------------- |
| SYMBOL | String | Trading pair or funding currency                                 |
| PREC   | string | Level of price aggregation (R0 for Raw Books).<br/>              |
| LEN    | string | Number of price points ("1", "25", "100", "250") \[default="25"] |
| SUBID  | string | Optional user-defined ID for the subscription                    |

#### Raw book snapshot data

| Index    | Field         | Type  | Description                                                                                  |
| :------- | :------------ | :---- | :------------------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID   | Int   | Identification number assigned to the channel for the duration of this connection.           |
| \[1]     | BOOK\_ENTRIES | Array | Array with an array of currently active book entries (Indices \[0...n] will be book entries) |
| \[0...n] | BOOK\_ENTRY   | Array | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)                       |

#### Raw book update data

| Index | Field       | Type  | Description                                                                        |
| :---- | :---------- | :---- | :--------------------------------------------------------------------------------- |
| \[0]  | CHANNEL\_ID | Int   | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | BOOK\_ENTRY | Trade | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)             |

#### Raw book bulk update data

| Index    | Field         | Type  | Description                                                                                  |
| :------- | :------------ | :---- | :------------------------------------------------------------------------------------------- |
| \[0]     | CHANNEL\_ID   | Int   | Identification number assigned to the channel for the duration of this connection.           |
| \[1]     | BOOK\_ENTRIES | Array | Array with an array of currently active book entries (Indices \[0...n] will be book entries) |
| \[0...n] | BOOK\_ENTRY   | Array | [Book entry](#book-entry) or [funding book entry](#funding-book-entry)                       |

#### Book entry

| Index | Field     | Type  | Description                                                                          |
| :---- | :-------- | :---- | :----------------------------------------------------------------------------------- |
| \[0]  | ORDER\_ID | Int   | Identification number of the order.                                                  |
| \[1]  | PRICE     | Float | Order price; if 0 you have to remove the order from your book                        |
| \[2]  | AMOUNT    | Float | Total amount available at that price level. Trading: if AMOUNT > 0 then bid else ask |

#### Funding book entry

| Index | Field     | Type  | Description                                                                           |
| :---- | :-------- | :---- | :------------------------------------------------------------------------------------ |
| \[0]  | OFFER\_ID | Int   | Identification number of the funding offer.                                           |
| \[1]  | PERIOD    | Int   | Funding period in days                                                                |
| \[2]  | RATE      | Int   | Funding rate for the offer; if 0 you have to remove the offer from your book          |
| \[3]  | AMOUNT    | Float | Total amount available at that price level. Funding: if AMOUNT < 0 then bid else ask; |

**Trading**: if AMOUNT > 0 then bid else ask; **Funding**: if AMOUNT < 0 then bid else ask;

**Algorithm to create and keep a book instance updated**

1. subscribe to channel with R0 precision
2. receive the raw book snapshot and create your in-memory book structure
3. when *PRICE* > 0 then you have to add or update the order
4. when *PRICE* = 0 then you have to delete the order

**Note:** The algorithm for raw books using `R0` is based on the *ORDER ID* instead of *COUNT*, *PRICE* and *AMOUNT*.\
If *LENGTH* is set to 25, you will get 25 orders (not price levels). If all orders belong to the same price level, your orderbook will just have that one price level.

**Checksum**\
An Order Book Checksum can be requested through the Websocket configuration. You can find out more on the [WebSocket Checksum](https://docs.bitfinex.com/docs/ws-websocket-checksum) page.

**Bulk Updates**\
Bulk updates can be enabled by sending a [conf event](https://docs.bitfinex.com/docs/ws-general#configuration) with a flag value of 536870912. With bulk updates enabled, updates will arrive as an array of arrays.
