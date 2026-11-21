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
source_url: 'https://docs.bitfinex.com/docs/ws-auth'
updated_at: 2026-11-21
---

# Authenticated Channels

### URL

Channels that require authentication should use the domain:
wss\://api.bitfinex.com/

The domain:
wss\://api-pub.bitfinex.com/
Should only be used for public channels.

### Rate Limit

The rate limit for wss\://api.bitfinex.com/ is set at 5 connections per 15 seconds.

### Account Information

This channel allows you to keep up to date with the status of your account. You can receive updates on your positions, your balances, your orders, and your trades. Once your session is authenticated it remains so until the connection is disconnected/terminated/restarted.

Account info always uses chanId 0.

To learn more, look to the [Account Info](https://docs.bitfinex.com/reference/ws-auth-account-info) channel page.

### Authenticating your Connection

**Request parameters**

Below are the parameters that are used to authenticate a connection. The dms and filter parameters are optional.

| Field       | Type   | Description                                                                                                                                                                                  |
| :---------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event       | string | "auth"                                                                                                                                                                                       |
| apiKey      | string |                                                                                                                                                                                              |
| authPayload | string |                                                                                                                                                                                              |
| authSig     | string | The generated signature                                                                                                                                                                      |
| authNonce   | string | An ever increasing numeric string but should not exceed the MAX\_SAFE\_INTEGER constant value of 9007199254740991.                                                                           |
| dms         | int    | Dead-Man-Switch flag (optional). Values: 4                                                                                                                                                   |
| filter      | array  | Allows you to filter which information you are interested in (default = everything). See [Channel Filters](https://docs.bitfinex.com/docs/ws-auth#section-channel-filters) for more details. |

Note:

* `dms: 4` -> when socket is closed, cancel all account orders

Below is the example code to authenticate your connection. The optional parameters 'dms' and 'filter' are not used, but can be appended to the payload if desired.

**JavaScript Authenticated Connection Example**
Link: <https://docs.bitfinex.com/v2/recipes/wsjavascript-authenticated-connection-example-1>

**Python Authenticated Connection Example**
Link: <https://docs.bitfinex.com/v2/recipes/wspython-authenticated-connection-example>

> 📘 WS Inputs
>
> Please note that the above examples only authenticate your WS connection to the server. If you wish you interact with the API further you'll have to include some sort of listener to perform some action on a particular Websocket "event".
>
> An example can be found here: [Websocket Inputs](https://docs.bitfinex.com/reference/ws-auth-input)

### Channel Filters

During authentication, you can provide an array to indicate which information/messages you are interested to receive (default = everything).

> 🚧 Wallet Labels
>
> The following labels are used for the different wallets:
>
> 'exchange', 'trading', 'deposit'
>
> These correspond to the Exchange Wallet, Margin Wallet, and Funding Wallet respectively.

```javascript
const payload = {
  event: 'auth', 
  // ... 
  filter: [
    'trading', // orders, positions, trades 
    'trading-tBTCUSD', // tBTCUSD orders, positions, trades
    'funding', // offers, credits, loans, funding trades
    'funding-fBTC', // fBTC offers, credits, loans, funding trades
    'wallet',  // wallet
    'wallet-exchange-BTC', // Exchange BTC wallet changes 
    'algo',    // algorithmic orders
    'balance', // balance (tradable balance, ...)
    'notify'   // notifications
  ]
}
```

### List of Account Info Events

* [Orders](https://docs.bitfinex.com/reference/ws-auth-orders)
* [Positions](https://docs.bitfinex.com/reference/ws-auth-positions)
* [Trades](https://docs.bitfinex.com/reference/ws-auth-trades)
* [Funding Offers](https://docs.bitfinex.com/reference/ws-auth-funding-offers)
* [Funding Credits](https://docs.bitfinex.com/reference/ws-auth-funding-credits)
* [Funding Loans](https://docs.bitfinex.com/reference/ws-auth-funding-loans)
* [Wallets](https://docs.bitfinex.com/reference/ws-auth-wallets)
* [Balance Info](https://docs.bitfinex.com/reference/ws-auth-balance-info)
* [Margin Info](https://docs.bitfinex.com/reference/ws-auth-margin-info)
* [Funding Info](https://docs.bitfinex.com/reference/ws-auth-funding)
* [Funding Trades](https://docs.bitfinex.com/reference/ws-auth-funding-trades)
* [Notifications](https://docs.bitfinex.com/reference/ws-auth-notifications)

### List of WS Inputs

* [New Order](https://docs.bitfinex.com/reference/ws-auth-input-order-new)
* [Update Order](https://docs.bitfinex.com/reference/ws-auth-input-order-update)
* [Order Multi-OP](https://docs.bitfinex.com/reference/ws-auth-input-order-multi-op)
* [Cancel Order](https://docs.bitfinex.com/reference/ws-auth-input-order-cancel)
* [Cancel Order Multi](https://docs.bitfinex.com/reference/ws-auth-input-order-cancel-multi)
* [New Offer](https://docs.bitfinex.com/reference/ws-auth-input-offer-new)
* [Cancel Offer](https://docs.bitfinex.com/reference/ws-auth-input-offer-cancel)
* [Calc](https://docs.bitfinex.com/reference/ws-auth-input-calc)
