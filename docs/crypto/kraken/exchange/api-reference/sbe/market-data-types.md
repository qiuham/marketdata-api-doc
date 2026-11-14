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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/market-data-types'
updated_at: 2026-11-13
---

# Market data enums & encodings

> Enumerations, primitive and composite encodings of the market data schema (ID 36)

SBE
schema 36 · market data
types

## Enumerations

### OrderUpdateAction

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `New` | `1` | |
| `Change` | `2` | |
| `Delete` | `3` | |

### InstrumentUpdateAction

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Add` | `1` | |
| `Modify` | `2` | |
| `Delete` | `3` | |

### Side

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Buy` | `1` | |
| `Sell` | `2` | |

### AggressorSide

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Buy` | `1` | |
| `Sell` | `2` | |

### InstrumentTradingStatus

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Hidden` | `1` | |
| `Online` | `2` | |
| `Maintenance` | `3` | |
| `CancelOnly` | `4` | |
| `PostOnly` | `5` | |
| `LimitOnly` | `6` | |
| `Delisted` | `7` | |
| `ReduceOnly` | `8` | |
| `SystemMaintenance` | `9` | |
| `Halted` | `10` | |
| `Closed` | `11` | Instrument is outside its scheduled trading session |

### TradingSessionStatusCode

Applies to Spot and Futures only. US Perps does not expose a global trading session status; it provides the status per instrument (see `InstrumentTradingStatus`).

Encoding: `uint8`

| Name | Value | Description |
| :- | :- | :- |
| `Halted` | `1` | |
| `Open` | `2` | |
| `CancelOnly` | `101` | |
| `PostOnly` | `102` | |
| `LimitOnly` | `103` | |

### OrdTypeMD

Encoding: `char`

| Name | Value | Description |
| :- | :- | :- |
| `Market` | `1` | Taker order was a market order \[Kraken emits: Yes] |
| `Limit` | `2` | Taker order was a limit order \[Kraken emits: Yes] |

## Primitive and composite encodings

### messageHeader

Composite of: `blockLength:uint16`, `templateId:uint16`, `schemaId:uint16`, `version:uint16`.

### groupSizeEncoding

Composite of: `blockLength:uint16`, `numInGroup:uint16`.

### InstrumentId

Primitive `uint64`, length 1, required.

Opaque, globally unique instrument identifier assigned by Instrument Registry.

### OrderId

Composite of: `low:uint64`, `high:uint64`.

### TradeId

Composite of: `low:uint64`, `high:uint64`.

### TimestampNs

Primitive `int64`, length 1, required.

Positive UTC timestamp in nanoseconds since the Unix epoch.

### Scale

Primitive `uint8`, length 1, required. Maximum value 36.

Number of supported decimal places.

### Decimal

Composite of: `mantissa:int64`, `exponent:int8`.

`exponent` ranges from -36 to 0.

### Price

Composite of: `decimal:ref`.

### OptionalPrice

Composite of: `mantissa:int64`, `exponent:int8` (optional).

Absolute price in the instrument currency. `exponent` ranges from -36 to 0. Exponent `127` means unavailable (null); ignore the mantissa when it is. Zero is a real value. Used by `minPrice`, `maxPrice`, `variation` and `referencePrice`.

### Quantity

Composite of: `decimal:ref`.

### SymbolEncoding

Composite of: `length:uint16`, `varData:char`.

`length` is the number of UTF-8 encoded bytes, up to 128. Used by `symbol`.

### StatusReasonEncoding

Composite of: `length:uint16`, `varData:char`.

`length` is the number of UTF-8 encoded bytes, up to 128. An empty value means no reason was supplied.

> [!NOTE]
>
> Kraken constrains these values to the limits above before publishing and does not truncate identifiers.
