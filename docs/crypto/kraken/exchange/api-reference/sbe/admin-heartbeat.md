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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/admin-heartbeat'
updated_at: 2026-11-13
---

# AdminHeartbeat

> Session schema, template 4

SBE
schema 33 · session
template 4

Keepalive from Kraken. Reports the latest valid client frame accepted on this connection.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `serverTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 3 | `lastReceivedClientSequence` | [`SequenceNumber`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sequencenumber) | field | required | Latest valid client frame accepted on this connection |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
