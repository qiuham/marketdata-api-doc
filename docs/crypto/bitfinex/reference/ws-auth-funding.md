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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-funding'
updated_at: 2026-11-24
---

# Funding Info

Get account funding info

```json Update ('fiu')
[
  0, //CHAN_ID
  "fiu", //MSG_TYPE
  [
    "sym", //UPDATE_TYPE
    "fUSD",  //SYMBOL
    [
      0.0008595462068208099, //YIELD_LOAN
      0, //YIELD_LEND
      1.8444560185185186, //DURATION_LOAN
      0 //DURATION_LEND
    ] //FUNDING_INFO_UPDATE_ARRAY
  ] //UPDATE_ARRAY
]
```

#### Funding info update data

| Index | Field         | Type   | Description                                                                        |
| :---- | :------------ | :----- | :--------------------------------------------------------------------------------- |
| \[0]  | CHAN\_ID      | Int    | Identification number assigned to the channel for the duration of this connection. |
| \[1]  | MSG\_TYPE     | String | 'fiu' (funding info update)                                                        |
| \[2]  | UPDATE\_ARRAY | Array  | [Funding info 'sym' update](#update-array-data-index-2)                            |

#### Update array data (Index \[2])

| Index | Field                        | Type   | Description                                                     |
| :---- | :--------------------------- | :----- | :-------------------------------------------------------------- |
| \[0]  | UPDATE\_TYPE                 | String | Specifies the type of the update: 'sym'                         |
| \[1]  | SYMBOL                       | String | Symbol related to the update                                    |
| \[2]  | FUNDING\_INFO\_UPDATE\_ARRAY | Array  | [Funding info update array](#funding-info-update-array-index-2) |

#### Funding info update array (Index \[2]

| Index | Field          | Type  | Description                                    |
| :---- | :------------- | :---- | :--------------------------------------------- |
| \[0]  | YIELD\_LOAN    | float | Weighted average rate for taken funding        |
| \[1]  | YIELD\_LEND    | float | Weighted average rate for provided funding     |
| \[2]  | DURATION\_LOAN | float | Weighted average duration for taken funding    |
| \[3]  | DURATION\_LEND | float | Weighted average duration for provided funding |

> 📘 NOTE
>
> These messages have gained the ability to send the calculation values equal to "null" meaning that the new calculated value is not yet available.\
> In order to receive those values the user have to actively request for it with a "calc" message.\
> See calc input dedicated section for more details.
