---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/user-data-streams
api_type: WebSocket
updated_at: 2026-11-28 18:32:21.167006
---

# User Data Streams

CAAS has **no user data stream endpoints of its own**. Account, balance, and order events are
delivered by the standard Binance user data streams, and each account — the master account and every
sub-account — opens its own stream with **its own API key**.

This matters for a CAAS integration: there is no single stream that reports events for all of your
end users. Plan for one stream per account, per product family.

For public prices, order books and trades, see
[Market Data Streams](/products/caas/market-data-streams) instead — those need no API key and one
connection can serve every user.

## Which stream to open

| Account          | Product        | How to open                                                                                                          | Reference                                                                                |
| ---------------- | -------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Master account   | Spot           | Subscribe over the [WebSocket API](/products/spot/web-socket-api#user-data-stream-subscribe) with the master API key | [Spot user data stream](/products/spot/user-data-stream)                                 |
| Master account   | USD-M Futures  | `POST /fapi/v1/listenKey`                                                                                            | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| Master account   | COIN-M Futures | `POST /dapi/v1/listenKey`                                                                                            | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |
| Each sub-account | Spot           | Same as above, using **that sub-account's** API key                                                                  | [Spot user data stream](/products/spot/user-data-stream)                                 |
| Each sub-account | USD-M Futures  | Same as above, using **that sub-account's** API key                                                                  | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| Each sub-account | COIN-M Futures | Same as above, using **that sub-account's** API key                                                                  | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |

Sub-account API keys are created with `POST /sapi/v1/broker/subAccountApi` — see
[Getting Started](/products/caas/getting-started). A sub-account key only ever reports that
sub-account's own events.

## WebSocket endpoints

| Product        | Connect to                                            |
| -------------- | ----------------------------------------------------- |
| Spot           | Subscribe over the WebSocket API — no `listenKey` URL |
| USD-M Futures  | `wss://fstream.binance.com/private/ws/<listenKey>`    |
| COIN-M Futures | `wss://dstream.binance.com/ws/<listenKey>`            |

:::warning

**USD-M user data lives under `/private`.** `fstream.binance.com` routes by path — `/public` and
`/market` carry market data, `/private` carries user data. Omitting `/private` will not deliver your
account events. COIN-M has no routed paths; its user data stream is a bare `/ws/<listenKey>`.

See [Market Data Streams](/products/caas/market-data-streams) for the full routing table.

:::

## Suggested setup

1. **Create the sub-account API key at onboarding**, in the same flow that creates the sub-account,
   so the stream can be opened as soon as the account is usable.
2. **Open one stream per sub-account per product family** the end user is enabled for. A spot-only
   end user needs one stream; an end user trading spot and USD-M futures needs two.
3. **Keep the master account's own streams separate** from end-user streams. The master account's
   events cover your own transfers and treasury activity, not your end users' trading.
4. **Run the keepalive and the reconnect as separate concerns.** The keepalive (below) is a
   60-minute cycle; the 24-hour reconnect is a hard limit that will disconnect you regardless.
5. **Reconcile against REST after every reconnect.** Events that occurred while disconnected are not
   replayed, so re-read balances and open orders on reconnect rather than assuming continuity.
6. **Treat the stream as the primary source for order state.** REST queries can lag under volatile
   conditions, which is why the futures documentation recommends prioritising stream messages for
   order and account state.

## Event types

### Spot

| Event                     | Sent when                                                         |
| ------------------------- | ----------------------------------------------------------------- |
| `outboundAccountPosition` | An account balance changes; carries the assets the event changed. |
| `balanceUpdate`           | A deposit, withdrawal, or transfer changes a balance.             |
| `executionReport`         | An order is created, filled, cancelled, expired, or rejected.     |
| `listStatus`              | An order list (OCO and similar) changes state.                    |
| `eventStreamTerminated`   | The stream is closed.                                             |
| `externalLockUpdate`      | A balance is locked or unlocked outside of trading.               |

### USD-M Futures

| Event                              | Sent when                                              |
| ---------------------------------- | ------------------------------------------------------ |
| `ACCOUNT_UPDATE`                   | Balance or position changes.                           |
| `ORDER_TRADE_UPDATE`               | An order is created, filled, cancelled, or expired.    |
| `TRADE_LITE`                       | A lighter-weight trade notification.                   |
| `ACCOUNT_CONFIG_UPDATE`            | Leverage or margin configuration changes.              |
| `MARGIN_CALL`                      | Position margin is insufficient.                       |
| `STRATEGY_UPDATE`                  | A strategy order changes state.                        |
| `GRID_UPDATE`                      | A grid order changes state.                            |
| `CONDITIONAL_ORDER_TRIGGER_REJECT` | A triggered conditional order is rejected.             |
| `listenKeyExpired`                 | The `listenKey` has expired and the stream is closing. |

### COIN-M Futures

COIN-M sends `ACCOUNT_UPDATE`, `ORDER_TRADE_UPDATE`, `ACCOUNT_CONFIG_UPDATE`, `MARGIN_CALL` and
`listenKeyExpired`. It does **not** send the strategy, grid, conditional-order or `TRADE_LITE`
events listed for USD-M.

## Keepalive and reconnection

These apply to the futures `listenKey` streams:

- A `listenKey` is valid for **60 minutes** after creation.
- `PUT` on the `listenKey` extends it by 60 minutes. If it returns `-1125` — _"This listenKey does
  not exist"_ — the key is gone and you must `POST` a new one.
- `POST` on an account that already has an active `listenKey` **returns the existing key** and
  extends it, rather than issuing a second one.
- `DELETE` closes the stream and invalidates the key.
- A single connection is valid for **24 hours**; expect to be disconnected at that mark and
  reconnect.

## Where to go next

| If you need               | Go to                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Spot event payloads       | [Spot user data stream](/products/spot/user-data-stream)                                 |
| USD-M event payloads      | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| COIN-M event payloads     | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |
| Creating sub-account keys | [Getting Started](/products/caas/getting-started)                                        |

---

# User Data Streams

CAAS has **no user data stream endpoints of its own**. Account, balance, and order events are
delivered by the standard Binance user data streams, and each account — the master account and every
sub-account — opens its own stream with **its own API key**.

This matters for a CAAS integration: there is no single stream that reports events for all of your
end users. Plan for one stream per account, per product family.

For public prices, order books and trades, see
[Market Data Streams](/products/caas/market-data-streams) instead — those need no API key and one
connection can serve every user.

## Which stream to open

| Account          | Product        | How to open                                                                                                          | Reference                                                                                |
| ---------------- | -------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Master account   | Spot           | Subscribe over the [WebSocket API](/products/spot/web-socket-api#user-data-stream-subscribe) with the master API key | [Spot user data stream](/products/spot/user-data-stream)                                 |
| Master account   | USD-M Futures  | `POST /fapi/v1/listenKey`                                                                                            | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| Master account   | COIN-M Futures | `POST /dapi/v1/listenKey`                                                                                            | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |
| Each sub-account | Spot           | Same as above, using **that sub-account's** API key                                                                  | [Spot user data stream](/products/spot/user-data-stream)                                 |
| Each sub-account | USD-M Futures  | Same as above, using **that sub-account's** API key                                                                  | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| Each sub-account | COIN-M Futures | Same as above, using **that sub-account's** API key                                                                  | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |

Sub-account API keys are created with `POST /sapi/v1/broker/subAccountApi` — see
[Getting Started](/products/caas/getting-started). A sub-account key only ever reports that
sub-account's own events.

## WebSocket endpoints

| Product        | Connect to                                            |
| -------------- | ----------------------------------------------------- |
| Spot           | Subscribe over the WebSocket API — no `listenKey` URL |
| USD-M Futures  | `wss://fstream.binance.com/private/ws/<listenKey>`    |
| COIN-M Futures | `wss://dstream.binance.com/ws/<listenKey>`            |

:::warning

**USD-M user data lives under `/private`.** `fstream.binance.com` routes by path — `/public` and
`/market` carry market data, `/private` carries user data. Omitting `/private` will not deliver your
account events. COIN-M has no routed paths; its user data stream is a bare `/ws/<listenKey>`.

See [Market Data Streams](/products/caas/market-data-streams) for the full routing table.

:::

## Suggested setup

1. **Create the sub-account API key at onboarding**, in the same flow that creates the sub-account,
   so the stream can be opened as soon as the account is usable.
2. **Open one stream per sub-account per product family** the end user is enabled for. A spot-only
   end user needs one stream; an end user trading spot and USD-M futures needs two.
3. **Keep the master account's own streams separate** from end-user streams. The master account's
   events cover your own transfers and treasury activity, not your end users' trading.
4. **Run the keepalive and the reconnect as separate concerns.** The keepalive (below) is a
   60-minute cycle; the 24-hour reconnect is a hard limit that will disconnect you regardless.
5. **Reconcile against REST after every reconnect.** Events that occurred while disconnected are not
   replayed, so re-read balances and open orders on reconnect rather than assuming continuity.
6. **Treat the stream as the primary source for order state.** REST queries can lag under volatile
   conditions, which is why the futures documentation recommends prioritising stream messages for
   order and account state.

## Event types

### Spot

| Event                     | Sent when                                                         |
| ------------------------- | ----------------------------------------------------------------- |
| `outboundAccountPosition` | An account balance changes; carries the assets the event changed. |
| `balanceUpdate`           | A deposit, withdrawal, or transfer changes a balance.             |
| `executionReport`         | An order is created, filled, cancelled, expired, or rejected.     |
| `listStatus`              | An order list (OCO and similar) changes state.                    |
| `eventStreamTerminated`   | The stream is closed.                                             |
| `externalLockUpdate`      | A balance is locked or unlocked outside of trading.               |

### USD-M Futures

| Event                              | Sent when                                              |
| ---------------------------------- | ------------------------------------------------------ |
| `ACCOUNT_UPDATE`                   | Balance or position changes.                           |
| `ORDER_TRADE_UPDATE`               | An order is created, filled, cancelled, or expired.    |
| `TRADE_LITE`                       | A lighter-weight trade notification.                   |
| `ACCOUNT_CONFIG_UPDATE`            | Leverage or margin configuration changes.              |
| `MARGIN_CALL`                      | Position margin is insufficient.                       |
| `STRATEGY_UPDATE`                  | A strategy order changes state.                        |
| `GRID_UPDATE`                      | A grid order changes state.                            |
| `CONDITIONAL_ORDER_TRIGGER_REJECT` | A triggered conditional order is rejected.             |
| `listenKeyExpired`                 | The `listenKey` has expired and the stream is closing. |

### COIN-M Futures

COIN-M sends `ACCOUNT_UPDATE`, `ORDER_TRADE_UPDATE`, `ACCOUNT_CONFIG_UPDATE`, `MARGIN_CALL` and
`listenKeyExpired`. It does **not** send the strategy, grid, conditional-order or `TRADE_LITE`
events listed for USD-M.

## Keepalive and reconnection

These apply to the futures `listenKey` streams:

- A `listenKey` is valid for **60 minutes** after creation.
- `PUT` on the `listenKey` extends it by 60 minutes. If it returns `-1125` — _"This listenKey does
  not exist"_ — the key is gone and you must `POST` a new one.
- `POST` on an account that already has an active `listenKey` **returns the existing key** and
  extends it, rather than issuing a second one.
- `DELETE` closes the stream and invalidates the key.
- A single connection is valid for **24 hours**; expect to be disconnected at that mark and
  reconnect.

## Where to go next

| If you need               | Go to                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Spot event payloads       | [Spot user data stream](/products/spot/user-data-stream)                                 |
| USD-M event payloads      | [USD-M user data streams](/products/derivatives-trading-usds-futures/user-data-streams)  |
| COIN-M event payloads     | [COIN-M user data streams](/products/derivatives-trading-coin-futures/user-data-streams) |
| Creating sub-account keys | [Getting Started](/products/caas/getting-started)                                        |