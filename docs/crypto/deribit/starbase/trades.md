---
exchange: deribit
source_url: https://docs.deribit.com/starbase/trades
api_type: Starbase
updated_at: 2026-11-20 19:00:11.777278
---

# Trades

> Starbase Binary API trade messages: Trade Summary, Trade, and Block Trade, plus the execution timestamp and wasDelayed flag on delayed Block RFQ prints.

## Trades

### Trade Summary (30)

This message is sent when a taker order matches against one or more maker/resting orders, followed by one or more Trade messages.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | instrumentId | int64 | 8 | Numeric instrument ID |
| 2 | takerOrderId | int64 | 8 | Unique identifier for the taker order |
| 3 | totalFilledMantissa | QuantityMantissa | 8 | Total amount filled (by the taker order) |
| 4 | deepestPrice | Price9 | 8 | Deepest price in book matched by taker order |
| 5 | markPrice | Price9 | 8 | Mark price at the time of the trade |
| 6 | indexPrice | Price9 | 8 | Index price at the time of the trade |
| 7 | tradeCount | int32 | 4 | Number of Trade messages that will follow this message |
| 8 | takerFlags | uint32 | 4 | Attributes of taker order, defined below |

The table below outlines the content of `TradeFlags`: field 8 (takerFlags) in Trade Summary, field 6 (makerFlags) in Trade and field 10 (takerFlags) in Block Trade:

| Bit number (from last to first) | Name | Description |
| - | - | - |
| 1 | isSell | `0`=Buy `1`=Sell |
| 2 | isLiquidation | `0`=Not a liquidation `1`=Liquidation trade |
| 3 | wasDelayed | `0`=Published at execution `1`=Block RFQ trade published after a delay. Added in schema version `2`. Set only on [Block Trade (33)](#block-trade-33) messages; see [Delayed Block RFQ trades](#delayed-block-rfq-trades) |
| 4 | Reserved for future use | |
| 5 | Reserved for future use | |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |
| 8 | Reserved for future use | |

### Trade (31)

This message is sent for each matched order (including implied orders) and synthetic leg for trades on combo instruments.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | matchId | int64 | 8 | Unique identifier of the trade |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | makerOrderId | int64 | 8 | Unique identifier for the resting order. In case of implied order or synthetic leg of a combo trade, encoded as `0x8000000000000000` |
| 4 | amount | QuantityMantissa | 8 | Amount that was matched |
| 5 | price | Price9 | 8 | Price at which the match occurred |
| 6 | makerFlags | uint32 | 4 | See table above |

## Block Trades

### Block Trade (33)

This message is sent for each individual trade in a Deribit Block Trade or Deribit Block RFQ trade. Multiple `Block Trade` messages belonging to the same block trade event are grouped as a transaction via the `startOfTransaction` and `endOfTransaction` flags in the message header. A block trade event is per instrument: a multi-leg Block Trade or Block RFQ trade generates one transaction per leg. For example, a Block RFQ with 3 legs where the taker trades against 2 makers produces 3 transactions, each containing 2 `Block Trade` messages. Block RFQ trades include a `blockRfqId`; Block Trades omit it.

From schema version `2` the message body is 88 bytes (previously 78). Fields 12 and 13 are appended at the end of the message, so earlier fields keep their offsets. With the 16-byte message header and padding to an 8-byte boundary, `messageLength` in the message header is `104` (previously `96`).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | matchId | int64 | 8 | Unique identifier of the block trade fill |
| 2 | instrumentId | int64 | 8 | Numeric instrument ID |
| 3 | blockTradeId | int64 | 8 | Per-fill block trade identifier assigned by the matching engine |
| 4 | blockRfqId | int64 | 8 | Block RFQ identifier; absent (null value) for Block Trades, present for Block RFQ trades |
| 5 | fillQtyMantissa | QuantityMantissa | 8 | Fill quantity |
| 6 | fillPrice | Price9 | 8 | Price at which the block trade occurred |
| 7 | markPrice | Price9 | 8 | Mark price at the time of the block trade. On a delayed print, the mark price at execution |
| 8 | indexPrice | Price9 | 8 | Index price at the time of the block trade. On a delayed print, the index price at execution |
| 9 | impliedVolatility | double | 8 | Implied volatility; absent (null value) for non-option instruments |
| 10 | takerFlags | uint32 | 4 | Attributes of the taker side; see flags table in [Trades](#trades) section above |
| 11 | numberOfLegs | uint16 | 2 | Total number of legs in the block trade structure |
| 12 | padding2 | int16 | 2 | Padding; ignore. Added in schema version `2` |
| 13 | executionTimestamp | TimestampNanos (int64) | 8 | Nanoseconds since epoch. Execution time of the Block RFQ trade. Set only when `wasDelayed`=`1`; otherwise null value (`0x8000000000000000`). Added in schema version `2` |

### Delayed Block RFQ trades

Qualifying Block RFQ trades can have their public publication delayed. The eligibility rules, size thresholds and delay are the same as for the JSON-RPC API; see the [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md).

A delayed Block RFQ trade is not published on the incremental channel at execution. When the delay ends, its `Block Trade` messages are published with:

* `wasDelayed` set in `takerFlags`
* `executionTimestamp` set to the execution time
* `transactTime` in the message header set to the publication time
* the original `matchId`, `blockTradeId`, `blockRfqId`, prices and quantities from execution

Block Trades and Block RFQ trades that are not delayed are published at execution as before, with `wasDelayed`=`0` and a null `executionTimestamp`; `transactTime` is the execution time.


## Related topics

- [block_trade_confirmations ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmations.md)
- [private/get_block_trade](https://docs.deribit.com/api-reference/block-trade/private-get_block_trade.md)
- [private/execute_block_trade](https://docs.deribit.com/api-reference/block-trade/private-execute_block_trade.md)
- [private/get_block_trades](https://docs.deribit.com/api-reference/block-trade/private-get_block_trades.md)
- [private/approve_block_trade](https://docs.deribit.com/api-reference/block-trade/private-approve_block_trade.md)