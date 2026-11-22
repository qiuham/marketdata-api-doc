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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-historical-orders'
updated_at: 2026-11-22
---

# Historical Orders (deprecated)

Deprecated channel that retrieves past orders.

```json Snapshot
[
  CHAN_ID, 
  'hos'
  [
    [
      ID, 
      GID,
      CID,
      SYMBOL, 
      MTS_CREATE, 
      MTS_UPDATE, 
      AMOUNT, 
      AMOUNT_ORIG, 
      TYPE,
      TYPE_PREV,
      _PLACEHOLDER,
      _PLACEHOLDER,
      FLAGS,
      STATUS,
      _PLACEHOLDER,
      _PLACEHOLDER,
      PRICE,
      PRICE_AVG,
      PRICE_TRAILING,
      PRICE_AUX_LIMIT,
      _PLACEHOLDER,
      _PLACEHOLDER,
      _PLACEHOLDER,
      NOTIFY, 
      HIDDEN, 
      PLACED_ID,
      ...
    ], 
    ...
  ]
]
```

**Stream Fields**

| Term              | Type   | Description                                                                                                                                                                                                                   |
| ----------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                | int    | Order ID                                                                                                                                                                                                                      |
| GID               | int    | Group ID                                                                                                                                                                                                                      |
| CID               | int    | Client Order ID                                                                                                                                                                                                               |
| SYMBOL            | string | Pair (tBTCUSD, …)                                                                                                                                                                                                             |
| MTS\_CREATE       | int    | Millisecond timestamp of creation                                                                                                                                                                                             |
| MTS\_UPDATE       | int    | Millisecond timestamp of update                                                                                                                                                                                               |
| AMOUNT            | float  | Positive means buy, negative means sell.                                                                                                                                                                                      |
| AMOUNT\_ORIG      | float  | Original amount                                                                                                                                                                                                               |
| TYPE              | string | The type of the order: LIMIT, MARKET, STOP, STOP LIMIT, TRAILING STOP, FOK, IOC For exchange orders: EXCHANGE MARKET, EXCHANGE LIMIT, EXCHANGE STOP, EXCHANGE STOP LIMIT, EXCHANGE TRAILING STOP, EXCHANGE FOK, EXCHANGE IOC. |
| TYPE\_PREV        | string | Previous order type                                                                                                                                                                                                           |
| FLAGS             | int    | See <https://docs.bitfinex.com/v2/docs/flag-values>.                                                                                                                                                                          |
| ORDER\_STATUS     | string | Order Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED, RSN\_DUST (amount is less than 0.00000001), RSN\_PAUSE (trading is paused / paused due to AMPL rebase event)                                                      |
| PRICE             | float  | Price                                                                                                                                                                                                                         |
| PRICE\_AVG        | float  | Average price                                                                                                                                                                                                                 |
| PRICE\_TRAILING   | float  | The trailing price                                                                                                                                                                                                            |
| PRICE\_AUX\_LIMIT | float  | Auxiliary Limit price (for STOP LIMIT)                                                                                                                                                                                        |
| NOTIFY            | int    | 1 if Notify flag is active, 0 if not                                                                                                                                                                                          |
| HIDDEN            | int    | 1 if Hidden, 0 if not hidden                                                                                                                                                                                                  |
| PLACED\_ID        | int    | If another order caused this order to be placed (OCO) this will be that other order's ID                                                                                                                                      |
