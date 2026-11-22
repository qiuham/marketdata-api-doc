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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-margin-info'
updated_at: 2026-11-22
---

# Margin Info

Receive margin info updates for your account.

Subscribe to the account information channel to keep track of your margin info. The account information channel will provide a feed of your margin info for as long as the channel remains open. Any authenticated connection is automatically subscribed to the account information channel.

Example code to open an authenticated connection can be found on our [Authenticated Channels Page](https://docs.bitfinex.com/docs/ws-auth).

Margin info events are sent with CHAN\_ID = 0 and can be identified by looking at the TYPE stream field. Margin info events can be recognised by the 'miu' (margin info update) abbreviation.

```json Update ('miu')
// margin base calc

[
  0, //CHAN_ID
  "miu", //MSG_TYPE
  [
    "base", //UPDATE_TYPE
    [
      -13.014640000000007, //USER_PL
      0, //USER_SWAPS
      49331.70267297, //MARGIN_BALANCE
      49318.68803297, //MARGIN_NET
      27 //MARGIN_REQUIRED
    ] //BASE_UPDATE_ARRAY
  ] //UPDATE_ARRAY
] 

// margin symbol calc
  
[
  0, //CHAN_ID
  "miu", //MSG_TYPE
  [
    "sym", //UPDATE_TYPE
    "tETHUSD", //SYMBOL
    [
      149361.09689202666, //TRADABLE_BALANCE
      149639.26293509, //GROSS_BALANCE
      830.0182168075556, //BUY
      895.0658432466332, //SELL
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      null, //PLACEHOLDER
      null //PLACEHOLDER
    ] //SYM_UPDATE_ARRAY
  ] //UPDATE_ARRAY
] 
```

#### Margin info update data

| Index | Field         | Type   | Description                                                                                                  |
| :---- | :------------ | :----- | :----------------------------------------------------------------------------------------------------------- |
| \[0]  | CHAN\_ID      | Int    | Identification number assigned to the channel for the duration of this connection.                           |
| \[1]  | MSG\_TYPE     | String | 'miu' (margin info update)                                                                                   |
| \[2]  | UPDATE\_ARRAY | Array  | [Margin info 'base' update](#margin-info-base-update) or [Margin info 'sym' update](#margin-info-sym-update) |

#### Margin info 'base' update

| Index | Field               | Type   | Description                              |
| :---- | :------------------ | :----- | :--------------------------------------- |
| \[0]  | UPDATE\_TYPE        | String | Specify the type of update: "base"       |
| \[1]  | BASE\_UPDATE\_ARRAY | Array  | [Base update array](#base-update-arrays) |

#### Margin info 'sym' update

| Index | Field              | Type   | Description                            |
| :---- | :----------------- | :----- | :------------------------------------- |
| \[0]  | UPDATE\_TYPE       | String | Specify the type of update: "base"     |
| \[1]  | SYMBOL             | String | Symbol for the update                  |
| \[2]  | SYM\_UPDATE\_ARRAY | Array  | [Sym update array](#sym-update-arrays) |

#### Base update arrays

| Index | Field            | Type  | Description                                    |
| :---- | :--------------- | :---- | :--------------------------------------------- |
| \[0]  | USER\_PL         | Float | User profit and loss                           |
| \[1]  | USER\_SWAPS      | Float | Amount of swaps a user has                     |
| \[2]  | MARGIN\_BALANCE  | Float | Balance in your margin funding account         |
| \[3]  | MARGIN\_NET      | Float | Balance after P\&L is accounted for            |
| \[4]  | MARGIN\_REQUIRED | Float | Minimum required margin to keep positions open |

#### Sym update arrays

| Index | Field             | Type  | Description                                                           |
| :---- | :---------------- | :---- | :-------------------------------------------------------------------- |
| \[0]  | TRADABLE\_BALANCE | Float | Your buying power (how large a position you can obtain)               |
| \[1]  | GROSS\_BALANCE    | Float | Your buying power including funds already reserved for open positions |
| \[2]  | BUY               | Float | Maximum amount you can buy at current best ASK                        |
| \[3]  | SELL              | Float | Maximum amount you can sell at current best BID                       |

> 📘 NOTE
>
> These messages have gained the ability to send the calculation values equal to "null" meaning that the new calculated value is not yet available.\
> In order to receive those values the user have to actively request for it with a "calc" message.\
> See calc input dedicated section for more details.
