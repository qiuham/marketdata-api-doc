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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/subscription-response'
updated_at: 2026-11-13
---

# SubscriptionResponse

> Session schema, template 8

SBE
schema 33 · session
template 8

Answers a SubscriptionRequest. `subscriptionResult` says whether it was accepted.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `subscriptionId` | `uint64` | field | required | |
| 3 | `serverTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 4 | `subscriptionResult` | [`SubscriptionResult`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#subscriptionresult) | field | required | |
| 5 | `reason` | [`VarStringEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varstringencoding) | var data | required | |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
