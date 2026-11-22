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
source_url: 'https://docs.bitfinex.com/reference/ws-auth-historical-loans'
updated_at: 2026-11-22
---

# Historical Loans (deprecated)

Deprecated channel that provides historical information on your provided funding which was not used in active positions.

```json Snapshot
[
  CHAN_ID,
  'hfls',
  [
    [
      ID,
      SYMBOL,
      SIDE,
      MTS_CREATE,
      MTS_UPDATE,
      AMOUNT,
      FLAGS,
      STATUS,
      _PLACEHOLDER,
      _PLACEHOLDER,
      _PLACEHOLDER,
      RATE,
      PERIOD,
      MTS_OPENING,
      MTS_LAST_PAYOUT,
      NOTIFY,
      HIDDEN,
      _PLACEHOLDER,
      RENEW,
      RATE_REAL,
      NO_CLOSE,
      ...
    ],
    ...
  ]
]
```

**Stream Fields**

| Term              | Type    | Description                                                                |
| ----------------- | ------- | -------------------------------------------------------------------------- |
| ID                | integer | Offer ID                                                                   |
| SYMBOL            | string  | The currency of the offer (fUSD, etc)                                      |
| SIDE              | string  | "Lend" or "Loan"                                                           |
| MTS\_CREATE       | int     | Millisecond Time Stamp when the offer was created                          |
| MTS\_UPDATE       | int     | Millisecond Time Stamp when the offer was created                          |
| AMOUNT            | float   | Amount the offer is for                                                    |
| FLAGS             | object  | future params object (stay tuned)                                          |
| STATUS            | string  | Offer Status: ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED                 |
| RATE              | float   | Rate of the offer                                                          |
| PERIOD            | int     | Period of the offer                                                        |
| MTS\_OPENING      | int     | Millisecond Time Stamp for when the loan was opened                        |
| MTS\_LAST\_PAYOUT | int     | Millisecond Time Stamp for when the last payout was made                   |
| NOTIFY            | int     | 0 if false, 1 if true                                                      |
| HIDDEN            | int     | 0 if false, 1 if true                                                      |
| INSURED           | int     | 0 if false, 1 if true                                                      |
| RENEW             | int     | 0 if false, 1 if true                                                      |
| RATE\_REAL        | float   | the calculated rate for FRR and FRRDELTAFIX                                |
| NO\_CLOSE         | int     | If funding will be returned when position is closed. 0 if false, 1 if true |
