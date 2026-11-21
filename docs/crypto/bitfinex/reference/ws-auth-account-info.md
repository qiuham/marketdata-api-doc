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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-account-info'
updated_at: 2026-11-21
---

# Account Info

The account info channel is a channel that you are automatically subscribed to when you authenticate your session. It provides all the pertinent info for your orders, positions, trades, funding offers and loans, balances, and more.

```javascript
const crypto = require('crypto-js') // Standard JavaScript cryptography library
const WebSocket = require('ws') // Websocket library for Node

const apiKey = '' // Users API credentials are defined here
const apiSecret = ''

const authNonce = Date.now() * 1000 // Generate an ever increasing, single use value. (a timestamp satisfies this criteria)
const authPayload = 'AUTH' + authNonce // Compile the authentication payload, this is simply the string 'AUTH' prepended to the nonce value
const authSig = crypto.HmacSHA384(authPayload, apiSecret).toString(crypto.enc.Hex) // The authentication payload is hashed using the private key, the resulting hash is output as a hexadecimal string

const payload = {
  apiKey, //API key
  authSig, //Authentication Sig
  authNonce, 
  authPayload,
  event: 'auth', // The connection event, will always equal 'auth'
  //dms: 4, // Optional Dead-Man-Switch flag to cancel all orders when socket is closed
  //filter: [] // Optional filter for the account info received (default = everything)
}

const wss = new WebSocket('wss://api.bitfinex.com/ws/2') // Create new Websocket

wss.on('open', () => wss.send(JSON.stringify(payload)))

wss.on('message', (msg) => {     // The 'message' event is called whenever the ws recieves ANY message
  let response = JSON.parse(msg)
  console.log(msg)
})
```
```go
package main
import (
    "crypto/hmac"
    "crypto/sha512"
    "encoding/hex"
    "encoding/json"
    "fmt"
    "log"
    "time"
    "golang.org/x/net/websocket"
)
func main() {
    ws, err := websocket.Dial("wss://api.bitfinex.com/ws/2", "", "http://localhost/")
    if err != nil {
        return
    }
    nonce := fmt.Sprintf("%v", time.Now().Unix())
    payload := "AUTH" + nonce
    sig := hmac.New(sha512.New384, []byte("API_SECRET"))
    sig.Write([]byte(payload))
    payload_sign := hex.EncodeToString(sig.Sum(nil))
    connectMsg, _ := json.Marshal(map[string]interface{}{
        "event":       "auth",
        "apiKey":      "API_KEY",
        "authSig":     payload_sign,
        "authPayload": payload,
        "authNonce":   nonce,
    })
    // Send auth message
    _, err = ws.Write(connectMsg)
    if err != nil {
        log.Fatal(err)
        return
    }
    // Read all incoming messages
    var msg string
    for {
        if err = websocket.Message.Receive(ws, &msg); err != nil {
            fmt.Println(err)
        } else {
            fmt.Println(msg)
        }
    }
}
```

#### Subscribing to account info

Use the code above to open an authenticated connection. Subscribing to the Account Info channel is automatically done when you authenticate your session. You will continue to receive updates until the connection is disconnected/terminated/restarted.

```json Request
{
    event: "auth",
    apiKey: api_key,
    authSig: signature,
    authPayload: payload,
    authNonce: authNonce,
    calc: 1
}
```
```json Response
{ event: 'auth',
  status: 'OK',
  chanId: 0,
  userId: 269312,
 	auth_id: 'a26236f1-ef44-4671-be32-197ce190348f',
  caps: '{"orders": {"read": 1, "write": 0}, "account": {"read": 1, "write": 0}, "funding": {"read": 1, "write": 1}, "history": {"read": 1, "write": 0}, "wallets": {"read": 1, "write": 1}, "withdraw": {"read": 0, "write": 1}, "positions": {"read": 1, "write": 1}, ui_withdraw: { read: 0, write: 0 }}' }
```
```json Response failure
// response-failure
{  
   "event":"auth",
   "status":"FAIL",
   "chanId":0,
   "code":"<ERROR_CODE>"
}
```

#### Filters

Filters can be applied to limit the information received through the channel. You can find more information about setting up filters for the account info channel [here](https://docs.bitfinex.com/docs/ws-auth#section-channel-filters),

#### Structure

By default, authentication will subscribe you to all account info updates. The account info channel will be assigned a CHANNEL\_ID of 0. All snapshots and updates provided through the channel will be structured as follows:

```json
[
 CHANNEL_ID // = 0
 <TYPE> //'on', 'ou', 'oc', etc. 
  [
   ... //Content goes here
  ]
]
```

#### Separate streams

Please see the documentation page for each stream to find a further specification of the contents returned by each stream. The following table shows all of the included streams, their purpose, and the abbreviations by which messages in the channel can be identified:

| Stream Name                                                                  | Purpose                                                                                                                       | Associated Abbreviations (TYPE)s                                                                                             |
| :--------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| [Orders](https://docs.bitfinex.com/reference#ws-auth-orders)                 | Snapshot and updates on the trade orders in your account.                                                                     | 'os' = order snapshot; 'on' = order new; 'ou' = order update; 'oc' = order cancel                                            |
| [Positions](https://docs.bitfinex.com/reference#ws-auth-position)            | Snapshot and updates on the positions in your account.                                                                        | 'ps' = position snapshot; 'pn' = position new; 'pu' = position update; 'pc' = position close                                 |
| [Trades](https://docs.bitfinex.com/reference#ws-auth-trades)                 | Provides a feed of your trades                                                                                                | 'te' = trade executed; 'tu' = trade execution update                                                                         |
| [Funding Offers](https://docs.bitfinex.com/reference#ws-auth-offers)         | Provides a snapshot and updates on the funding offers in your account.                                                        | 'fos' = funding offer snapshot; 'fon' = funding offer new; 'fou' = funding offer update; 'foc' = funding offer cancel        |
| [Funding Credits](https://docs.bitfinex.com/reference#ws-auth-credits)       | Provides a snapshot and updates on your provided funding used in active positions.                                            | 'fcs' = funding credits snapshot; 'fcn' = funding credits new; 'fcu' = funding credits update; 'fcc' = funding credits close |
| [Funding Loans](https://docs.bitfinex.com/reference#ws-auth-loans)           | Provides a snapshot and updates on your provided funding that is not used in active positions.                                | 'fls' = funding loans snapshot; 'fln' = funding loans new; 'flu' = funding loans update; 'flc' = funding loans close         |
| [Wallets](https://docs.bitfinex.com/reference#ws-auth-wallets)               | Provides a snapshot and updates on wallet balance, unsettled interest, and available balance.                                 | 'ws' = wallet snapshot; 'wu' = wallet update                                                                                 |
| [Balance Info](https://docs.bitfinex.com/reference#ws-auth-balance)          | Provides updates on the total and net assets in your account.                                                                 | 'bu' = balance update                                                                                                        |
| [Margin Info](https://docs.bitfinex.com/reference#ws-auth-margin)            | Provides margin info updates (tradable balance, margin balance, margin net, margin required)                                  | 'miu' = margin info update                                                                                                   |
| [Funding Info](https://docs.bitfinex.com/reference#ws-auth-funding)          | Provides funding info updates (average rates for taken and provided funding, average duration for taken and provided funding) | 'fiu' = funding info update                                                                                                  |
| [Funding Trades](https://docs.bitfinex.com/reference#ws-auth-funding-trades) | Provides a feed of your funding trades.                                                                                       | 'fte' = funding trade execution; 'ftu' = funding trade update                                                                |
| [Notifications](https://docs.bitfinex.com/reference#ws-auth-notifications)   | Work in progress: will be used for different changes in status, price alerts, etc.                                            | 'n' = notification                                                                                                           |
