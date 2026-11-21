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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-input'
updated_at: 2026-11-21
---

# Websocket Inputs

This page lists the additional code necessary to send inputs through your Websocket connection. This code is used in addition to the authentication payload listed [here](https://docs.bitfinex.com/docs/ws-auth).

Edit the example code below depending on the type of input you wish to send. Simply edit the order details according to your wishes and the requirements for each input. You will also need to ensure that the payload (inputPayload) includes the appropriate abbreviation for the action you wish to perform. The example code included on this page is used to send a new order and therefore includes the 'on' (order new) abbreviation. Use different abbreviations for different actions. A full list of abbreviations can be found in our [Abbreviation Glossary](https://docs.bitfinex.com/docs/abbreviations-glossary).

```javascript
//...
//authentication code
//....
const inputDetails = {
    "cid": Date.now(),
    "type": "LIMIT",
    "symbol": 'tBTCUSD',
    "amount": "0.020",
    "price": '9600'
}

const inputPayload = [0, 'on', null, inputDetails] // Note how the payload is constructed here. It consists of an array starting with the CHANNEL_ID, TYPE, and PLACEHOLDER and is followed by the inputDetails object.

//Websocket Listener

wss.on('message', (msg) => {     // The 'message' event is called whenever the ws recieves ANY message
  let response = JSON.parse(msg)
  if (response[1] === 'ws') { //Payload is sent when the wallet snapshot is received. Sending an order before the snapshot can result in a tradable balance error
    wss.send(JSON.stringify(inputPayload));// Submit payload for input
  } 
  console.log(msg); // ALL ws receipts will be logged to console
})
```
