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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/negotiate'
updated_at: 2026-11-13
---

# Negotiate

> Session schema, template 1

SBE
schema 33 · session
template 1

Opens and authenticates a session. `requestTimestampNs` is the authentication nonce and replay check.

**Direction:** Client → Kraken

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `sessionId` | [`SessionId`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#sessionid) | field | required | |
| 2 | `requestTimestampNs` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#timestampns) | field | required | Client-generated UTC timestamp used as the ACG authentication nonce and replay check |
| 3 | `keepaliveIntervalMs` | `uint32` | field | required | Keepalive interval in milliseconds. Kraken returns the agreed interval in `NegotiationResponse.keepaliveIntervalMs` |
| 4 | `credentialType` | [`CredentialType`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#credentialtype) | field | required | Signing scheme. The only value is `KrakenHmacSha512` (`0`) |
| 5 | `compId` | [`VarStringEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varstringencoding) | var data | required | Registered logical client identity; 1 to 128 printable ASCII bytes |
| 6 | `accessKey` | [`VarStringEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varstringencoding) | var data | required | Kraken API key. Its API secret signs the message |
| 7 | `signature` | [`VarBufferEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/session-types#varbufferencoding) | var data | required | Raw 64-byte HMAC-SHA512 output, not base64 encoded. See [Authentication](#authentication) |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/session-types.md#messageheader).

## Authentication

`KrakenHmacSha512` authenticates `Negotiate` with the API secret that belongs to `accessKey`, using the same HMAC-SHA512 model as the Kraken FIX API.

### Signed payload

The signed payload is the contiguous encoded SBE message from the first byte of the 8-byte `messageHeader` through the last byte of `accessKey`. It includes the encoded `compId` and `accessKey` length prefixes and values. The SOFH, the Kraken TCP header and `signature` (including its length prefix) are not part of the payload.

Read `blockLength` from the message header you are encoding, not from a constant in your generated codec: new fixed fields extend `blockLength` and are therefore signed.

```text theme={null}
payloadLength = 8 + messageHeader.blockLength
              + 2 + compIdLength
              + 2 + accessKeyLength
payload       = sbeMessage[0:payloadLength]
data          = SHA256(payload)
signature     = HMAC-SHA512(base64_decode(apiSecret), data)
```

The two-byte terms are the `uint16` length prefixes of `compId` and `accessKey`. Because the SBE header, session ID, timestamp, keepalive interval, credential type, `compId` and `accessKey` are all signed, none of them can be changed without invalidating the signature.

`signature` must remain the last variable-length field of the message. Put the raw 64 bytes of the HMAC output in `signature`; do not base64 encode them.

### Fields

* **`requestTimestampNs`** is a UTC timestamp in nanoseconds that you generate for each attempt. It is the authentication nonce and replay check. Kraken rejects values outside its allowed clock window (see [`NegotiationReject`](https://docs.kraken.com/exchange/api-reference/sbe/negotiation-reject)); there is no separate nonce field.
* **`sessionId`** identifies one negotiation attempt. Generate a new `sessionId` for every attempt, including when you reconnect.
* **`compId`** is your registered logical client identity. It is case-sensitive, 1 to 128 printable ASCII bytes, and must be authorized for the account that owns `accessKey`. Use the same `compId` every time you reconnect. An account can have more than one registered `compId`. Each `compId` allows one active live connection and one active snapshot connection.
* **`accessKey`** is the Kraken API key whose secret signs the message.

The service endpoint identifies the target, so there is no FIX-style `TargetCompID`. Credentials are provided during onboarding.
