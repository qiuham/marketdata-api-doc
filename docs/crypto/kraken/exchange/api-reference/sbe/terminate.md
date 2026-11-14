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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/terminate'
updated_at: 2026-11-13
---

# Terminate

> Session schema, template 6

SBE
schema 33 · session
template 6

Ends the session. `code` gives the reason and `reason` the detail.

**Direction:** Either direction

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `timestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 3 | `code` | [`TerminationCode`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#terminationcode) | field | required | |
| 4 | `reason` | [`VarStringEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varstringencoding) | var data | required | |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
