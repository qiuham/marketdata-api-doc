---
exchange: kraken
source_url: https://docs.kraken.com/exchange/api-reference/sbe/subscriber-heartbeat
api_type: SBE
updated_at: 2026-11-18 01:44:55.780864
---

# SubscriberHeartbeat

> Session schema, template 5

SBE
schema 33 · session
template 5

Keepalive from the client. Reports the latest server frame processed on this connection.

**Direction:** Client → Kraken

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `clientTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | |
| 3 | `lastReceivedServerSequence` | [`SequenceNumber`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sequencenumber) | field | required | Latest server frame processed on this connection |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).