---
exchange: deribit
source_url: https://docs.deribit.com/starbase/reference-data
api_type: Starbase
updated_at: 2026-11-21 19:01:37.946143
---

# Starbase Reference Data and Instrument Definitions

> Instrument metadata for the Starbase Binary API, including InstrumentDefinition fields, index and mark price sources, and quantityExponent snapshot behavior.

## Reference data

> [!NOTE]
>
> **Combination Orders**: Combination orders are treated as orders on outright books and are not differentiated in any way. Their orderbook\_id links to a combination order book.

> [!NOTE]
>
> **Multicast is the recommended source for full reference data.** The Starbase REST API exposes a subset of instrument fields and does not include all attributes available in the SBE `InstrumentDefinition` message. For example, combination legs, large tick size steps, and the instrument flags are not available via REST. Use the multicast reference data feed to obtain complete instrument definitions.

## Reference data sources

The Starbase and standard Deribit APIs expose overlapping, but not identical, instrument metadata:

| Source | Access | Use it for |
| - | - | - |
| SBE multicast `InstrumentDefinition` | Starbase private connectivity | Authoritative Starbase order-entry units, minimum quantity, tick sizes, instrument type, status, and combo legs |
| [Standard `public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) | [Classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) public API; Starbase network access is not required | Standard instrument metadata including `contract_size`, `min_trade_amount` (quantity increment; Starbase REST name: `qty_tick_size`), `index_id`, and `product_group` |
| Starbase REST [`get_instruments`](https://docs.deribit.com/api-reference/market-data/list-instruments) | Starbase private connectivity | `index_id`, `product_group`, `qty_tick_size`, and a subset of standard instrument metadata. Does not return `contract_size`; use [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) or [`public/get_contract_size`](https://docs.deribit.com/api-reference/market-data/public-get_contract_size) for it. Optional filters: `currency`, `kind`, `expired`, `instrument_id`, `product_group`, and `state` |
| FIX `SecurityList` | Standard FIX session | FIX contract-based metadata including `ContractMultiplier` |

Do not assume that a field available through one interface is available through every other interface. In particular, use the multicast `InstrumentDefinition` when constructing or validating SBE order-entry messages.

> [!NOTE]
>
> On Starbase REST [`get_instruments`](https://docs.deribit.com/api-reference/market-data/list-instruments), `currency` is an exact match on the instrument's base currency (`BTC`, `ETH`, and so on). Omit `currency` to return instruments for every base currency. `currency=any` is compared as a base-currency name, matches no instrument, and the call succeeds with `"result": []`.

## Index prices and derived statistics

Index prices, mark prices, price bands, funding, and open interest are published on the multicast feeds via three dedicated messages:

| Message | Contents | Update frequency |
| - | - | - |
| `IndexInfo` (12) | Index price per currency pair, shared across the pair's instruments | On index price change |
| `InstrumentInfo` (14) | Price band (`minSellPrice`/`maxBuyPrice`) and mark price per instrument | Frequently |
| `InstrumentRef` (15) | Funding, settlement/delivery prices, and open interest per instrument | Less frequently |

On the snapshot channel, every cycle starts with `IndexInfo` messages (one for each known index price on the channel, batched into as few packets as fit) so snapshot joiners receive current index prices before the per-instrument sequences.

These values are also available from the standard Deribit API:

| Data | Sources |
| - | - |
| Index price | `deribit_price_index.{index_name}` WebSocket channel, [`public/get_index_price`](https://docs.deribit.com/api-reference/market-data/public-get_index_price), or `ticker.{instrument}.{interval}` |
| Mark price, funding, open interest | `ticker.{instrument}.{interval}` WebSocket channel, [`public/ticker`](https://docs.deribit.com/api-reference/market-data/public-ticker), or [`public/get_book_summary_by_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_instrument) |

The multicast feed and the endpoints above carry funding **rates**, not the amounts charged to your account. Funding amounts actually paid or received on a perpetual position are recorded in the account transaction log. Retrieve them with [`private/get_transaction_log`](https://docs.deribit.com/api-reference/account-management/private-get_transaction_log): the `interest_pl` field holds the funding PnL for the interval covered by each entry, and `total_interest_pl` holds the funding PnL accrued in the current trading session since the last daily settlement at 08:00 UTC.

## Quantity units and contract size

Starbase does not use contract counts or contract size for matching. All SBE order, quote, trade, and position quantities use Deribit's native **amount**:

| `quantityAsset` | Starbase amount unit |
| - | - |
| `USD` | Dollar value |
| The instrument's base currency, such as `BTC` or `ETH` | Number of coins |

Encode amounts directly as [`Decimal72`](https://docs.deribit.com/starbase/binary-api-reference#data-types), determine whether the amount represents dollar value or coins from `quantityAsset`, and validate the value against `minOrderQuantity`.

> [!WARNING]
>
> Do not derive a contract count before sending an SBE `quantity`, and do not copy a FIX `OrderQty` expressed in contracts into an SBE message. `contract_size` and FIX `ContractMultiplier` remain available for classic JSON-RPC and FIX workflows, but Starbase does not consume either value. Do not substitute classic JSON-RPC `contract_size` for the Starbase quantity tick (`qty_tick_size` / `minOrderQuantity × 10^quantityExponent`). Classic JSON-RPC exposes that increment as `min_trade_amount`, not as `qty_tick_size`. See [Quantity tick size across SBE and REST](#quantity-tick-size-across-sbe-and-rest).

Starbase is designed as a closed system for latency-sensitive matching. Broker, clearing, and other account-management workflows remain on the standard Deribit APIs, so applications that use those workflows may still need the standard reference data in addition to the Starbase feed.

### InstrumentDefinition (10)

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | name | char | 128 | Name of instrument on Deribit |
| 3 | indexId | int64 | 8 | The associated index |
| 4 | underlying | char | 64 | The underlying future; only applicable to options |
| 5 | quantityAsset | char | 8 | Asset used for quantity/amount |
| 6 | priceAsset | char | 8 | Asset used for pricing |
| 7 | expiryTime | int64 | 8 | Nanoseconds since epoch. Time of expiration (optional) |
| 8 | strikePrice | int64 | 8 | Strike price mantissa (×10⁻⁹); optional |
| 9 | minOrderQuantity | int64 | 8 | Minimum order quantity mantissa (aka baseIncrement); resolved value = minOrderQuantity × 10^quantityExponent |
| 10 | tickSize | int64 | 8 | Default tick size mantissa (×10⁻⁹) |
| 11 | quantityExponent | int8 | 1 | Exponent applied to all quantity fields (value = mantissa × 10^quantityExponent) |
| 12 | type | int8 | 1 | `0`=PerpFuture `1`=Option `2`=Spot `3`=FutureCombo `4`=OptionCombo `5`=DatedFuture |
| 13 | flags | uint8 | 1 | Instrument attributes (see flags table below) |
| 14 | status | int8 | 1 | `0`=Open `1`=Inactive `2`=Settlement `3`=Delivered `4`=Locked `5`=Halted |
| 15 | blockLengthOfLargeTickSizes | uint16 | 2 | Block length of each largeTickSizes group entry |
| 16 | numberOfLargeTickSizes | uint16 | 2 | Number of large tick size steps |
| ->17 | largeTickSize | int64 | 8 | Tick size mantissa (×10⁻⁹) applicable when price ≥ thresholdPrice |
| ->18 | thresholdPrice | int64 | 8 | Prices at or above this value use largeTickSize |
| 19 | blockLengthOfLegs | uint16 | 2 | Block length of each legs group entry |
| 20 | numberOfLegs | uint16 | 2 | Number of legs in the combination instrument. Maximum 4 |
| ->21 | legInstrumentId | int64 | 8 | Numeric instrumentId of the leg instrument |
| ->22 | ratio | int8 | 1 | Amount of leg traded per combination unit. Positive = buy leg when buying combo |

The table below outlines the content of field 13 (`flags`) of `InstrumentDefinition`.

| Bit (0 = LSB) | Name | Description |
| - | - | - |
| 0 | isReversed | Set if the instrument is inverse |
| 1 | isPutOption | Set if the option is a put |
| 2 | isPerpetual | Set if the instrument is perpetual |

> [!NOTE]
>
> `quantityExponent` (field 11) is available via the **multicast snapshot only**. No API returns it as a field of its own. It derives from the instrument's quantity tick size: a tick of `1` maps to `0`, `0.1` to `-1`, `0.01` to `-2`, and so on.

#### Quantity tick size across SBE and REST

The Starbase REST `get_instruments` endpoint returns `qty_tick_size`. That field is the Starbase quantity increment, expressed as a single decimal rather than the SBE mantissa and exponent pair: `qty_tick_size = minOrderQuantity × 10^quantityExponent`.

[Classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) does **not** return `qty_tick_size`. The same increment is named `min_trade_amount` on that API.

Reading the equivalent value from SBE therefore requires both `minOrderQuantity` (field 9) and `quantityExponent` (field 11), not `quantityExponent` alone:

| REST | Classic JSON-RPC | SBE | Value |
| - | - | - | - |
| `qty_tick_size` = 1 | `min_trade_amount` = 1 | `minOrderQuantity` = 1, `quantityExponent` = 0 | 1 |
| `qty_tick_size` = 0.1 | `min_trade_amount` = 0.1 | `minOrderQuantity` = 1, `quantityExponent` = -1 | 1 × 10⁻¹ = 0.1 |
| `qty_tick_size` = 0.01 | `min_trade_amount` = 0.01 | `minOrderQuantity` = 1, `quantityExponent` = -2 | 1 × 10⁻² = 0.01 |

The REST `qty_tick_size` and SBE `minOrderQuantity` × 10^`quantityExponent` representations are guaranteed to resolve to the same value for a given instrument. Classic JSON-RPC `min_trade_amount` is that same increment under a different field name.

> [!WARNING]
>
> **`qty_tick_size` is not `contract_size`.** Starbase matching uses the quantity tick (REST `qty_tick_size`, SBE `minOrderQuantity` × 10^`quantityExponent`, or classic JSON-RPC `min_trade_amount`). The classic JSON-RPC `contract_size` field and FIX `ContractMultiplier` are a separate value used by [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md), WebSocket, and FIX workflows. Those classic APIs remain in place and are not being replaced by Starbase.
>
> The quantity tick and `contract_size` may currently coincide on some instruments, but that is not a guarantee. Do not rely on them being equal now or in the future. Do not look for `qty_tick_size` on classic JSON-RPC instrument objects.

***

### IndexDefinition (11)

Sent at the start of the snapshot cycle, followed by `IndexInfo`.

| Field | Name | Type | Length | Description |
| :- | :- | :- | :- | :- |
| 1 | indexId | int64 | 8 | Currency pair ID |
| 2 | name | char | 128 | Name of index |

### IndexInfo (12)

Sent when an index price changes, and at the start of every snapshot cycle (one per known index price on the channel, batched into as few packets as fit). The index price is per currency pair and is shared across the pair's instruments.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | indexId | int64 | 8 | Currency pair ID |
| 2 | indexPrice | int64 | 8 | Index price mantissa (×10⁻⁹) |

### InstrumentInfo (14)

Frequently updated per-instrument fields.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | minSellPrice | int64 | 8 | Lower price band: minimum sell price mantissa (×10⁻⁹) |
| 3 | maxBuyPrice | int64 | 8 | Upper price band: maximum buy price mantissa (×10⁻⁹) |
| 4 | markPrice | int64 | 8 | Mark price mantissa (×10⁻⁹) |

### InstrumentRef (15)

Less frequently updated per-instrument fields. All value fields are optional. A field carries its null value when not applicable to the instrument (for example, funding fields on dated futures).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | currentFunding | double | 8 | Current funding rate (optional) |
| 3 | funding8h | double | 8 | 8-hour funding rate (optional) |
| 4 | estimatedDeliveryPrice | int64 | 8 | Estimated delivery price mantissa (×10⁻⁹); optional |
| 5 | deliveryPrice | int64 | 8 | Delivery price mantissa (×10⁻⁹); optional |
| 6 | settlementPrice | int64 | 8 | Settlement price mantissa (×10⁻⁹); optional |
| 7 | openInterest | double | 8 | Open interest (optional). A plain `double` with no mantissa/exponent scaling. Expressed in amount units: USD for perpetuals and inverse futures, the underlying base currency coin for options and linear futures. |

### InstrumentStatusUpdate (16)

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | tradingStatus | int8 | 1 | `0`=Open `1`=Inactive `2`=Settlement `3`=Delivered `4`=Locked `5`=Halted |

When `EVICT_DELIVERED_INSTRUMENTS_FROM_MD_SNAPSHOT` is on (it ships off, and also requires `EMIT_MD_INSTRUMENT_STATUS_ONLY` and `EMIT_INDEX_DEFINITION`), a transition to `DELIVERED` (`3`) removes the instrument from later snapshot cycles. See [Snapshot messages](https://docs.deribit.com/starbase/order-book-maintenance.md#snapshot-messages).


## Related topics

- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Maintaining the order book](https://docs.deribit.com/starbase/order-book-maintenance.md)
- [Market Model](https://docs.deribit.com/starbase/market-model.md)
- [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)
- [List Instruments](https://docs.deribit.com/api-reference/market-data/list-instruments.md)