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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-balance-info'
updated_at: 2026-11-19
---

# Balance Info

The Balance Info channel provides data on the total and net assets in your account.

Subscribe to the account information channel to keep track of your account balance. The account information channel will provide a feed of your balance for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Balance events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Balance update events can be recognised by the 'bu' (balance update) abbreviation.

```json Update ('bu')
[
  0, //CHAN_ID
  "bu", //MSG_TYPE
  [
    4131.85, //AUM
    4131.85 //AUM_NET
  ] //BALANCE_UPDATE_ARRAY
]
```

#### Balance info update data

| Index | Field                  | Type   | Description                                                                        |
| :---- | :--------------------- | :----- | :--------------------------------------------------------------------------------- |
| \[0]  | CHAN\_ID               | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | MSG\_TYPE              | String | 'bu' (balance update)                                                              |
| \[2]  | BALANCE\_UPDATE\_ARRAY | Array  | [Balance update array](#balance-update-array-index-2)                              |

#### Balance update array (Index 2)

| Index | Term     | Type  | Description                                                    |
| ----- | :------- | ----- | -------------------------------------------------------------- |
| \[0]  | AUM      | float | Total Assets Under Management                                  |
| \[1]  | AUM\_NET | float | Net Assets Under Management (total assets - total liabilities) |
