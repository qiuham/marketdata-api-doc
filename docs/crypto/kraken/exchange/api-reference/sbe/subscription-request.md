---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/subscription-request'
updated_at: 2026-11-13
---

# SubscriptionRequest

> Session schema, template 7

SBE
schema 33 · session
template 7

Requests a snapshot on the snapshot connection, or starts or stops incremental delivery on the live connection, for one market data feed.

**Direction:** Client → Kraken

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `subscriptionId` | `uint64` | field | required | |
| 3 | `requestTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 4 | `subscriptionRequestType` | [`SubscriptionRequestType`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#subscriptionrequesttype) | field | required | Snapshot is valid on the snapshot connection; Subscribe and Unsubscribe are valid on the live connection |
| 5 | `marketDataFeed` | [`MarketDataFeed`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#marketdatafeed) | field | required | |
| 7 | `instrumentListRequestType` | [`InstrumentListRequestType`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#instrumentlistrequesttype) | field | required | |
| 6 | `instruments` | group | group | required | |
| 1 |   ↳ `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#instrumentid) | group field | required | |

Rows marked ↳ are fields of the repeating group above them. Each group is preceded by a `groupSizeEncoding` header (`blockLength`, `numInGroup`).

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
