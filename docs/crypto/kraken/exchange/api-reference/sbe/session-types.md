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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/session-types'
updated_at: 2026-11-13
---

# Session enums & encodings

> Enumerations, primitive and composite encodings of the session schema (ID 33)

SBE
schema 33 · session
types

## Enumerations

### CredentialType

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `KrakenHmacSha512` | `0` | |

### NegotiationRejectCode

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `InvalidCredentials` | `0` | |
| `NotAuthorized` | `1` | |
| `InvalidTimestamp` | `2` | |
| `AlreadyNegotiated` | `3` | |
| `UnsupportedVersion` | `4` | |
| `TemporaryFailure` | `5` | |

### TerminationCode

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Finished` | `0` | |
| `NotAuthorized` | `1` | |
| `KeepaliveLapsed` | `2` | |
| `SlowConsumer` | `3` | |
| `ProtocolViolation` | `4` | |
| `ServerShutdown` | `5` | |

### SubscriptionRequestType

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Snapshot` | `0` | Request one snapshot on the snapshot connection |
| `Subscribe` | `1` | Start incremental delivery on the live connection |
| `Unsubscribe` | `2` | Stop an active subscription on the live connection |

### InstrumentListRequestType

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `SpecificInstruments` | `0` | |
| `AllSecurities` | `1` | |

### MarketDataFeed

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `InstrumentDefinition` | `0` | |
| `OrderBookL3` | `1` | |
| `Trade` | `2` | |
| `InstrumentStatus` | `4` | Live instrument-status changes. Initial status is included in InstrumentDefinitionSnapshot |
| `TradingSessionStatus` | `5` | Spot and Futures only; not used on US Perps |
| `Summary` | `6` | SummarySnapshot on the snapshot endpoint and SummaryIncremental on the live endpoint |

### SubscriptionResult

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Accepted` | `0` | |
| `InvalidRequest` | `1` | |
| `UnsupportedFeed` | `2` | |
| `UnknownInstrument` | `3` | |
| `AlreadySubscribed` | `4` | |
| `NotAuthorized` | `5` | |
| `TemporaryFailure` | `6` | |

## Primitive and composite encodings

### messageHeader

Composite of: `blockLength:uint16`, `templateId:uint16`, `schemaId:uint16`, `version:uint16`.

### SessionId

Composite of: `low:uint64`, `high:uint64`.

### groupSizeEncoding

Composite of: `blockLength:uint16`, `numInGroup:uint16`.

### InstrumentId

Primitive `uint64`, length 1, required.

Opaque, globally unique instrument identifier assigned by Instrument Registry.

### SequenceNumber

Primitive `uint64`, length 1, required.

Connection-local frame count, with zero meaning no frame received.

### TimestampNs

Primitive `int64`, length 1, required.

Positive UTC timestamp in nanoseconds since the Unix epoch.

### VarStringEncoding

Composite of: `length:uint16`, `varData:char`.

Variable-length UTF-8 string. `length` is the number of bytes in `varData`, up to 65534. Used by `compId`, `accessKey` and the `reason` fields.

### VarBufferEncoding

Composite of: `length:uint32`, `varData:uint8`.

Variable-length byte buffer. `length` is the number of bytes in `varData`, up to 2147483647. Used by the `Negotiate` `signature`.
