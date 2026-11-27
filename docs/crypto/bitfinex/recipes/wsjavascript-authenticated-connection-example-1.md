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
source_url: 'https://docs.bitfinex.com/recipes/wsjavascript-authenticated-connection-example-1'
updated_at: 2026-11-27
---

# [WS][JavaScript] Authenticated connection example

```javascript JavaScript
const crypto = require('crypto') 
const WebSocket = require('ws') 

const apiKey = '' // const apiKey = 'paste key here'
const apiSecret = '' // const apiSecret = 'paste secret here'

const nonce = (Date.now() * 1000).toString()
const authPayload = 'AUTH' + nonce 
const authSig = crypto.createHmac('sha384', apiSecret).update(authPayload).digest('hex') 

const payload = {
  apiKey, //API key
  authSig, //Authentication Sig
  nonce, 
  authPayload,
  event: 'auth'
}

const wss = new WebSocket('wss://api.bitfinex.com/ws/2') // Create new Websocket

wss.on('open', () => wss.send(JSON.stringify(payload)))

wss.on('message', (msg) => { 
  console.log(msg)
})
```

```json Response Example
{"success":true}
```

# Libraries

<!-- javascript@1,2 -->

This example uses the native crypto library to hash the signature using the HmacSHA384 algorithm.

This example uses the 'ws' library to build the WebSocket client

# API keys

<!-- javascript@4,5 -->

Authenticated requests require a pair of API keys. You can generate these keys in your account settings: https://setting.bitfinex.com/api#new-key

# Nonce

<!-- javascript@7 -->

A nonce needs to be passed when you open a WS connection or when you send any requests through an open WS connection. The only requirement for the nonce is that it needs to increase between subsequent requests.

This example code generates a nonce based on the current UNIX timestamp to ensure an increasing value between subsequent requests.

# authPayload

<!-- javascript@8 -->

Compile the authentication payload. This is simply the string 'AUTH' prepended to the nonce value.

# Signature hash

<!-- javascript@9 -->

The authentication payload is hashed using the HmacSHA384 algorithm and the private key. The resulting hash is output as a hexadecimal string

# Payload

<!-- javascript@11-17 -->

The Payload object is created. It should contain all of the following properties:
• apiKey
• authSig
• authNonce
• authPayload
• event

The event property indicates an authentication attempt and should always be set to 'auth'.

# Opening a connection

<!-- javascript@19 -->

A new WebSocket connection is opened with 'wss://api.bitfinex.com/ws/2'

# Sending the payload

<!-- javascript@21 -->

Once the connection is open, the payload is sent as a JSON string to authenticate the connection.

# Logging messages

<!-- javascript@23-25 -->

The 'message' event is called whenever the WS connection receives any message. These messages are then logged to the console.
