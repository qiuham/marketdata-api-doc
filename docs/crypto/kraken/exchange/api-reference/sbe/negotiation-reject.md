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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/negotiation-reject'
updated_at: 2026-11-13
---

# NegotiationReject

> Session schema, template 3

SBE
schema 33 · session
template 3

Rejects a negotiation. `code` gives the reason and `reason` the detail.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `requestTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 3 | `serverTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 4 | `code` | [`NegotiationRejectCode`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#negotiationrejectcode) | field | required | |
| 5 | `reason` | [`VarStringEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varstringencoding) | var data | required | |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
