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
source_url: 'https://docs.kraken.com/exchange/guides/general/order-lifecycle'
updated_at: 2026-11-13
---

# Order lifecycle

> Every order state, transition, and how to observe them across REST, WebSocket, and FIX

Understanding how an order moves through states is critical for systematic trading. This page documents every state, what triggers each transition, and how to observe them across the three API protocols.

## State machine

```
                    ┌─────────────────────────────┐
                    │           PENDING            │
                    │  Order received, not yet     │
                    │  validated by trading engine │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │             OPEN             │
                    │  Resting in the order book   │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
  ┌───────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
  │  PARTIALLY FILLED  │ │     FILLED      │ │    CANCELED     │
  │  Some qty matched  │ │  Fully matched  │ │  Canceled by    │
  │  remainder rests   │ │                 │ │  user or system │
  └───────────┬────────┘ └─────────────────┘ └─────────────────┘
              │
  ┌───────────▼──────────────────────────────────────────────┐
  │  CLOSED (fully filled from partial, or canceled partial) │
  └──────────────────────────────────────────────────────────┘
```

## States

| State | Description |
| :- | :- |
| `pending` | Order has been accepted but not yet processed by the trading engine |
| `open` | Order is live in the order book, awaiting a match |
| `partially_filled` | One or more partial fills have occurred; remainder is still open |
| `filled` (closed) | Order has been fully matched |
| `canceled` (closed) | Order was canceled — by the user, by COD, by `cancelAllOrdersAfter`, or by the system |
| `expired` (closed) | GTD (Good Till Date) order whose expiry time was reached |

## State transitions

| From | To | Trigger |
| :- | :- | :- |
| — | `pending` | Order accepted by OES/FIX Gateway |
| `pending` | `open` | Validated and placed in the order book |
| `pending` | `canceled` | Validation failure (insufficient funds, invalid params, rate limit) |
| `open` | `partially_filled` | Partial match in the trading engine |
| `open` | `filled` | Full match in the trading engine |
| `open` | `canceled` | User cancel, COD disconnect, `cancelAllOrdersAfter` deadline, `cancelAll` |
| `open` | `expired` | GTD order expiry reached |
| `partially_filled` | `partially_filled` | Additional partial fill |
| `partially_filled` | `filled` | Final fill clears remaining quantity |
| `partially_filled` | `canceled` | Remaining quantity canceled (IOC residual, user cancel, reduce-only limit) |

## Observing state by API

### REST

Use `OpenOrders` to see live orders and `ClosedOrders` / `QueryOrders` for historical state. The `status` field returns the current state string.

```bash theme={null}
# All open orders
POST /0/private/OpenOrders

# Specific order (open or closed)
POST /0/private/QueryOrders
# body: txid=ORDERTXID1
```

Response includes:

* `status`: `open`, `pending`, `closed`, `canceled`, `expired`
* `vol_exec`: volume filled so far
* `reason`: populated on cancellation (e.g. `"User requested"`, `"Order would trigger immediately"`)
* `amended`: boolean, `true` if the order was ever amended

### WebSocket v2

Subscribe to the `executions` channel for real-time state changes. Every state transition produces a message.

```json theme={null}
{
  "channel": "executions",
  "type": "snapshot" | "update",
  "data": [{
    "exec_type": "new" | "trade" | "canceled" | "expired" | "amended" | "status" | "restated" | "liquidated",
    "order_status": "new" | "partially_filled" | "filled" | "canceled" | "expired",
    "order_id": "ABCDE-12345-XXXXX",
    "qty": 1.0,
    "filled_qty": 0.5,
    "reason": "..."
  }]
}
```

Key `exec_type` values:

| `exec_type` | Meaning |
| :- | :- |
| `new` | Order placed in the book |
| `trade` | Partial or full fill |
| `canceled` | Order canceled |
| `expired` | GTD expiry |
| `amended` | Order was amended (price, quantity, or both) |
| `status` | State confirmation with no change (e.g. on reconnect snapshot) |
| `restated` | Order state was restated, typically after a system event |
| `liquidated` | Order was forcibly closed by the risk system |

### WebSocket v1

Subscribe to `openOrders` for live state updates. The feed sends a snapshot on subscribe, then incremental updates.

```json theme={null}
[
  { "ORDERTXID": { "status": "open", "vol_exec": "0.50000000" } },
  [{"sequence": 4}]
]
```

### FIX

ExecutionReport (MsgType=8) is the primary message for order state. Key tags:

| Tag | Field | Values |
| :- | :- | :- |
| 39 | `OrdStatus` | `0`=New, `1`=Partial fill, `2`=Filled, `4`=Canceled, `6`=Pending cancel, `8`=Rejected, `C`=Expired |
| 150 | `ExecType` | `0`=New, `1`=Partial fill, `2`=Fill, `4`=Canceled, `8`=Rejected, `C`=Expired, `D`=Restated, `G`=Trade correct |
| 58 | `Text` | Human-readable reason on rejection or cancellation |
| 14 | `CumQty` | Total quantity filled |
| 151 | `LeavesQty` | Remaining open quantity |

## Amendment and queue priority

When you amend an order, queue priority behaviour depends on what changed:

| Amendment type | Queue priority |
| :- | :- |
| Reduce quantity only | Preserved — the order keeps its time priority |
| Increase quantity | Lost — order moves to back of queue at that price |
| Change price | Lost — order moves to back of queue at the new price |

> [!TIP]
>
> For market-making strategies: reducing size without changing price preserves priority. This is a key advantage of `AmendOrder` over cancel-replace (`CancelOrder` + `AddOrder`).

## Special cancellation triggers

**Cancel on Disconnect (COD) — FIX only**
When a FIX session disconnects, all orders placed on that session are automatically canceled. COD is configured at the session level during onboarding.

**Dead Man's Switch — all APIs**
`CancelAllOrdersAfter` sets a countdown timer. If not refreshed before expiry, all open orders are canceled. Use this as a safety net against connectivity issues.

```bash theme={null}
POST /0/private/CancelAllOrdersAfter
# body: timeout=60  (seconds)
```

Refresh it periodically from your trading loop. Cancel it by setting `timeout=0`.

**IOC — Immediate or Cancel**
Orders with `time_in_force=IOC` fill immediately at the available best price and the unfilled remainder is instantly canceled with `reason: "Immediate or cancel"`.

**Reduce-only cancellation**
If a reduce-only order would flip a position, it matches as much as possible and the remainder is canceled with `EOrder:Reduce only:Position is closed`.

## Self-trade prevention

Self-trade prevention (STP) prevents your orders from matching against each other. Configure at the order level:

| Mode | FIX Tag 7928 | REST `stp_type` | Behaviour |
| :- | :- | :- | :- |
| Cancel newest (default) | `1` | `cancel-newest` | Arriving order is canceled |
| Cancel oldest | `2` | `cancel-oldest` | Resting order is canceled |
| Cancel both | `0` | `cancel-both` | Both orders are canceled |

## Related guides

> [card] [API comparison](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> Choose between REST, WebSocket, and FIX for order management

> [card] [Error reference](https://docs.kraken.com/exchange/guides/general/errors.md)
>
> Order error codes and cancellation reason strings

> [card] [WebSocket reconnection](https://docs.kraken.com/exchange/guides/websockets/reconnection.md)
>
> Reconcile order state after a disconnect

> [card] [Order amends](https://docs.kraken.com/exchange/guides/general/amends.md)
>
> Amend price or quantity without losing queue priority

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> How order placement and cancellation consume rate limit

> [card] [FIX ExecutionReport](https://docs.kraken.com/exchange/api-reference/unified-fix/er.md)
>
> FIX MsgType=8 — full field reference for order state messages
