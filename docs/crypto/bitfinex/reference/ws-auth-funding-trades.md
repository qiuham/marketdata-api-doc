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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-funding-trades'
updated_at: 2026-11-22
---

# Funding Trades

Receive updates for any trade events on your account.

Subscribe to the account information channel to keep track of your funding trades. The account information channel will provide a feed of your funding trades for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Trade events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Funding trade events will use one of the following abbreviations: 'fte' (funding trade executed) and 'ftu' (funding trade update).

```json Update ('fte', 'ftu')
[
  0, //CHAN_ID
  "fte", //TYPE
  [
    636854, //ID
    "fUSD", //SYMBOL
    1575282446000, //MTS_CREATE
    41238905, //OFFER_ID
    -1000, //AMOUNT
    0.002, //RATE
    7, //PERIOD
    null //MAKER
  ] //FUNDING_TRADE_ARRAY
]
```

#### Funding trade update data

| Index | Term                  | Type   | Description                                                                                                                                         |
| :---- | :-------------------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[0]  | CHAN\_ID              | Int    | Identification number for the channel subscribtion. Funding trades events are always sent through the account information channel with CHAN\_ID = 0 |
| \[1]  | TYPE                  | String | 'fte' (funding trade executed), 'ftu' (funding trade update)                                                                                        |
| \[2]  | FUNDING\_TRADE\_ARRAY | Array  | [Funding trade array]()                                                                                                                             |

#### Funding trade arrays (Index \[2])

| Index | Term        | Type   | Description                                                                                      |
| :---- | :---------- | :----- | :----------------------------------------------------------------------------------------------- |
| \[0]  | ID          | Int    | Offer ID                                                                                         |
| \[1]  | SYMBOL      | String | The currency of the offer (fUSD, etc)                                                            |
| \[2]  | MTS\_CREATE | Int    | Millisecond Time Stamp when the offer was created                                                |
| \[3]  | OFFER\_ID   | Int    | The ID of the offer                                                                              |
| \[4]  | AMOUNT      | Float  | Amount the offer is for                                                                          |
| \[5]  | RATE        | Float  | Rate of the offer                                                                                |
| \[6]  | PERIOD      | Int    | Period of the offer                                                                              |
| \[7]  | MAKER       | Int    | 1 if true, 'null' if false; Indicates if the order was executed as maker (true) or taker (false) |
