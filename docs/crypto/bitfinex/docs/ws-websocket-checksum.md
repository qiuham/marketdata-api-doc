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
source_url: 'https://docs.bitfinex.com/docs/ws-websocket-checksum'
updated_at: 2026-11-18
---

# WebSocket Checksum

The Websocket V2 [Books](https://docs.bitfinex.com/reference/ws-public-books) and [Raw Books](https://docs.bitfinex.com/reference/ws-public-raw-books) support the option to request that checksums be sent through the WebSocket connection. The checksum is a CRC32 value which covers the first 25 bids and asks. By calculating your own checksum and comparing it to the provided value, you can verify that your order book data is correct and up to date.

Checksums can be enabled by sending a 'conf' event with 'flag: 131072' when opening your WebSocket connection. Here is an example for opening a connection and subscribing to the BTCUSD book with checksums enabled.

```javascript
const WS = require('ws')
const ws = new WS('wss://api.bitfinex.com/ws/2')

ws.on('open', function open () {
  ws.send(JSON.stringify({ event: 'conf', flags: 131072 }))
  ws.send(JSON.stringify({ event: 'subscribe', channel: 'book', pair: 'tBTCUSD', prec: 'P0' }))
})
```

Checksums will be sent as a signed integer. The messages used to send checksums will follow this format:

\[ CHAN\_ID, 'cs', CHECKSUM ]\[ CHAN\_ID, 'cs', CHECKSUM ]

### Examples

A guide with examples to use checksums for an order book with precision P0, P1, P2, P3, or P4 can be found in this [blog post](https://blog.bitfinex.com/api/bitfinex-api-order-books-checksums/).

For sample code to use with a raw order book, please look at this [GitHub example](https://gist.github.com/prdn/b9c9c24fb1bb38604dcd1e94ee89dd9e).

### Step by step

When Checksums are enabled, take the following steps to use them to validate your order book data.

1. Extract and store the checksum value in index 2 of the received checksum message. This will be the server-side checksum.
2. Identify your book precision. If you are using P-precision books, price and amount values will be used to calculate your client-side checksum. If you are using Raw books (R0 precision), the calculation will be done based on order ID's and amount values.
3. Compile your data sequentially. The calculation will need you to input the 25 highest bids and the 25 lowest asks. Below you can see the format for raw books. For books with P-precision, replace the ID value with the price. You should end up with an array with 100 elements.

```json
[
    bids[0].id, 
    bids[0].amount, 
    asks[0].id, 
    asks[0].amount, 
    bids[1].id, 
    bids[1].amount, 
    asks[1].id, 
    asks[1].amount,
    ...
    bids[24].id, 
    bids[24].amount, 
    asks[24].id, 
    asks[24].amount,
 ]
```

> 🚧 Notes on compiling
>
> * When compiling checksum data, the order book must be sorted by price. For bids, price values must be descending. For asks, price values must be ascending.
>
> * Orders of the same price (for raw books) will need to be sub-sorted by ID in an ascending order (the lower index holds the lower id by numeric value).

4. Concatenate the values to a string using a colon (":") as the delimiter. For example:

```json
"50968755521:0.10783801:50968615681:-0.4675:50962803816:0.48:50968707576:-0.4678:50962803817:0.48:50968127526:-0.0012:50963483835:1.9414:50968169523:-0.0012:50963975797:0.810549:50968687160:-0.0997...."
```

5. Pass the string to the CRC-32 function to generate a client-side checksum. In our examples, we use the following library:

```javascript
const CRC = require('crc-32')
```

6. Compare the client and server checksum values. If the checksums match, your order book data is valid and up to date.
