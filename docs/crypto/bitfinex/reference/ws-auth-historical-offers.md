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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-historical-offers'
updated_at: 2026-11-24
---

# Historical Offers (deprecated)

Deprecated channel that provides your historical funding offers.

```json Snapshot
[
  CHAN_ID,
  'hfos',
  [
    [
      ID,
      SYMBOL,
      MTS_CREATED,
      MTS_UPDATED,
      AMOUNT,
      AMOUNT_ORIG,
      TYPE,
      _PLACEHOLDER,
      _PLACEHOLDER,
      FLAGS,
      STATUS,
      _PLACEHOLDER,
      _PLACEHOLDER,
      _PLACEHOLDER,
      RATE,
      PERIOD,
      NOTIFY,
      HIDDEN,
      _PLACEHOLDER,
      RENEW,
      RATE_REAL,
      ...
    ],
    ...
  ]
]
```

**Stream Fields**

| Term         | Type    | Description                                                |
| ------------ | ------- | ---------------------------------------------------------- |
| ID           | integer | Offer ID                                                   |
| CURRENCY     | string  | The currency of the offer (fUSD, etc)                      |
| MTS\_CREATED | int     | Millisecond Time Stamp when the offer was created          |
| MSG\_UPDATED | int     | Millisecond Time Stamp when the offer was created          |
| AMOUNT       | float   | Amount the offer is for                                    |
| AMOUNT\_ORIG | float   | Amount the offer was entered with originally               |
| TYPE         | string  | "lend" or "loan"                                           |
| FLAGS        | object  | See <https://docs.bitfinex.com/v2/docs/flag-values>.       |
| STATUS       | string  | Offer Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED |
| RATE         | float   | Rate of the offer                                          |
| PERIOD       | int     | Period of the offer                                        |
| NOTIFY       | int     | 0 if false, 1 if true                                      |
| HIDDEN       | int     | 0 if false, 1 if true                                      |
| INSURE       | int     | 0 if false, 1 if true                                      |
| RENEW        | int     | 0 if false, 1 if true                                      |
| RATE\_REAL   | float   | the calculated rate for FRR and FRRDELTAFIX                |
