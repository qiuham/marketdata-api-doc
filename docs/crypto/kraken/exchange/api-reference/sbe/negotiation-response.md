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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/negotiation-response'
updated_at: 2026-11-13
---

# NegotiationResponse

> Session schema, template 2

SBE
schema 33 · session
template 2

Confirms a successful negotiation, with the agreed keepalive interval and the session expiry time.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `requestTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 3 | `serverTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 4 | `sessionExpiryTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | Expiry of the current authorization. Not a fixed disconnect time: the gateway renews authorization in the background |
| 5 | `keepaliveIntervalMs` | `uint32` | field | required | |

`sessionExpiryTimestampNs` is not a fixed disconnect time. The gateway renews the session's authorization in the background, so you do not need to reconnect when this timestamp passes.

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).
