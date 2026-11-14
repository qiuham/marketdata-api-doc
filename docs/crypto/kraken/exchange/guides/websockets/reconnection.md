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
source_url: 'https://docs.kraken.com/exchange/guides/websockets/reconnection'
updated_at: 2026-11-13
---

# Reconnection and resilience

> How to handle WebSocket disconnections, re-subscription, and state reconciliation

WebSocket connections will disconnect — during maintenance windows, network hiccups, or load balancer recycling. A resilient client handles this transparently. This page covers the patterns you need.

## Connection lifecycle

A WebSocket connection to Kraken goes through these phases:

1. **Connect** — TCP + TLS handshake to `wss://ws.kraken.com/v2`
2. **Authenticate** (private channels) — obtain a token via `GetWebSocketsToken` and send it in the subscription
3. **Subscribe** — send subscription messages for each channel you need
4. **Receive snapshot** — Kraken sends the current state for stateful channels (book, open orders, balances)
5. **Stream updates** — incremental updates from there on
6. **Disconnect** — connection closes (server or network)
7. **Reconnect** — repeat from step 1

## Detecting disconnects

Kraken sends periodic `heartbeat` messages. If you stop receiving them, the connection is likely dead.

Subscribe to the heartbeat channel after connecting:

```json theme={null}
{"method": "subscribe", "params": {"channel": "heartbeat"}}
```

A heartbeat arrives roughly every second:

```json theme={null}
{"channel": "heartbeat"}
```

**Recommended approach:** set a deadline timer (e.g. 5 seconds). If no message of any kind arrives within the deadline, close and reconnect. Don't rely solely on TCP close events — connections can go silent without a clean close.

## Reconnection with backoff

Use exponential backoff with jitter to avoid thundering-herd reconnection storms:

```python theme={null}
import asyncio, random, websockets, json

async def connect_with_backoff(uri, handler):
    delay = 1.0
    max_delay = 60.0
    while True:
        try:
            async with websockets.connect(uri) as ws:
                delay = 1.0  # reset on successful connect
                await handler(ws)
        except Exception as e:
            jitter = random.uniform(0, delay * 0.1)
            print(f"Disconnected: {e}. Reconnecting in {delay:.1f}s")
            await asyncio.sleep(delay + jitter)
            delay = min(delay * 2, max_delay)
```

## Re-subscribing after reconnect

After reconnecting you must re-subscribe to all channels. Kraken does not automatically restore subscriptions.

Keep a local registry of your active subscriptions and replay them on every connect:

```python theme={null}
subscriptions = [
    {"method": "subscribe", "params": {"channel": "book", "symbol": ["BTC/USD"], "depth": 10}},
    {"method": "subscribe", "params": {"channel": "executions", "token": token}},
    {"method": "subscribe", "params": {"channel": "balances", "token": token}},
]

async def on_connect(ws):
    for sub in subscriptions:
        await ws.send(json.dumps(sub))
```

## State reconciliation after reconnect

On subscribe, Kraken sends a **snapshot** of the current state for stateful channels. Use this to rebuild your local state rather than trying to merge with your pre-disconnect state — the snapshot is authoritative.

### Order book

When you subscribe to `book`, you receive a full snapshot first:

```json theme={null}
{"channel": "book", "type": "snapshot", "data": [...all levels...]}
```

Followed by incremental updates:

```json theme={null}
{"channel": "book", "type": "update", "data": [...changed levels...]}
```

**On reconnect:** discard your existing book, wait for the snapshot, rebuild from scratch. Do not attempt to merge deltas from before and after the reconnect gap.

**Checksum validation:** after each update, validate the CRC32 checksum included in the message. If it fails, unsubscribe and re-subscribe to force a fresh snapshot.

```python theme={null}
def validate_checksum(book, expected_checksum):
    # Construct string from top 10 asks and bids
    # Format: price_without_dot + qty_without_dot, repeated
    # See checksum guide for full algorithm
    pass
```

### Open orders

Subscribe to `executions` to receive live order state. On reconnect, the snapshot contains all currently open orders.

After reconnecting, call `QueryOrders` via REST to cross-check against the snapshot for any orders that transitioned during the reconnect window:

```python theme={null}
# REST cross-check after reconnect
open_orders = rest_client.query_open_orders()
ws_snapshot_ids = {o["order_id"] for o in ws_snapshot}
for order in open_orders:
    if order["txid"] not in ws_snapshot_ids:
        # Order exists on exchange but not in WS snapshot — handle
        pass
```

### Balances

The `balances` channel snapshot on reconnect reflects current state. No additional REST call needed unless you need sub-second precision during the gap.

## Token refresh for private channels

WebSocket tokens expire after 15 minutes. If your connection lives longer than that, you need to refresh the token and re-authenticate.

**Recommended:** fetch a new token just before subscribing (not when the connection opens), so the token is fresh. For long-running connections, fetch a new token proactively before each reconnect:

```python theme={null}
async def get_fresh_token():
    response = await rest_client.post("/0/private/GetWebSocketsToken")
    return response["result"]["token"]

async def reconnect():
    token = await get_fresh_token()
    # Use token in subscription messages
```

## Using `cancelAllOrdersAfter` as a safety net

Enable the Dead Man's Switch before going live. It ensures that if your client fails to reconnect and stops refreshing, all open orders will be canceled automatically:

```python theme={null}
# Set a 60-second countdown — refresh this every ~30 seconds from your trading loop
rest_client.post("/0/private/CancelAllOrdersAfter", {"timeout": 60})

# Cancel the switch when you shut down cleanly
rest_client.post("/0/private/CancelAllOrdersAfter", {"timeout": 0})
```

## System status

Subscribe to the `status` channel to receive notifications about planned maintenance and trading mode changes:

```json theme={null}
{"method": "subscribe", "params": {"channel": "status"}}
```

Status updates include:

```json theme={null}
{
  "channel": "status",
  "data": [{
    "api_version": "v2",
    "connection_id": 12345678,
    "system": "online",
    "version": "2.0.9"
  }]
}
```

`system` values: `online`, `maintenance`, `cancel_only`, `post_only`, `limit_only`. When `maintenance` is received, stop sending orders and prepare to reconnect.

## Sequence numbers (WebSocket v1)

WebSocket v1 private feeds (`openOrders`, `ownTrades`) include sequence numbers. On reconnect, compare the first sequence number in the new snapshot against your last received sequence number to detect gaps.

If a gap is detected, fall back to REST (`OpenOrders`, `ClosedOrders`) to reconstruct the missed state before resuming from the new WebSocket feed.

## Maintenance windows

FIX sessions have a logical session rollover every day at **22:00 UTC**. This lasts approximately 30 seconds. Sequence numbers reset to 0. Reconnect and re-establish the session after the rollover.

WebSocket connections during maintenance receive a `status: maintenance` message. Reconnect attempts during the window will fail — implement your backoff so you retry automatically once the window ends.

## Related guides

> [card] [WebSocket authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md)
>
> How to obtain and refresh WebSocket tokens

> [card] [Order lifecycle](https://docs.kraken.com/exchange/guides/general/order-lifecycle.md)
>
> Order states and how to reconcile them after a disconnect

> [card] [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)
>
> Access WebSocket API permission required for private channels

> [card] [Book checksum (v2)](https://docs.kraken.com/exchange/guides/websockets/book-checksum-v2.md)
>
> Validate your order book state after reconnect
