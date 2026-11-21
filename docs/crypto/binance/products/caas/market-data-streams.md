---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/market-data-streams
api_type: WebSocket
updated_at: 2026-11-21 18:32:25.143554
---

# Market Data Streams

Market data streams carry prices, order books, and trades for the whole exchange. They are
**public** — no API key, no signature, and nothing CAAS-specific about them.

Use them to drive prices and charts in your own front end. They are separate from
[User Data Streams](/products/caas/user-data-streams), which carry the account and order events for
one specific account and do require a key.

## Which stream to connect to

| Product        | Base endpoint                                   | Reference                                                                                            |
| -------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Spot           | `wss://stream.binance.com`                      | [Spot WebSocket streams](/products/spot/web-socket-streams)                                          |
| USD-M Futures  | `wss://fstream.binance.com/public` or `/market` | [USD-M market streams](/products/derivatives-trading-usds-futures/websocket-market-streams/Connect)  |
| COIN-M Futures | `wss://dstream.binance.com`                     | [COIN-M market streams](/products/derivatives-trading-coin-futures/websocket-market-streams/Connect) |

Spot also offers `wss://data-stream.binance.vision` as a market-data-only alternative.

## USD-M Futures routes streams by path

USD-M Futures is the exception. `fstream.binance.com` splits into three routed paths, and which one
you need depends on the stream:

| Path       | Carries                                                               |
| ---------- | --------------------------------------------------------------------- |
| `/public`  | High-frequency public market data, for example `@depth`               |
| `/market`  | Regular market data, for example `@aggTrade` and `@markPrice`         |
| `/private` | User data — see [User Data Streams](/products/caas/user-data-streams) |

```
wss://fstream.binance.com/market/ws/bnbusdt@aggTrade
wss://fstream.binance.com/public/ws/bnbusdt@depth
wss://fstream.binance.com/market/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice
```

:::warning

**A connection with no routed path only receives `/public` data.** `wss://fstream.binance.com/ws/…`
still works for streams that belong to `/public`, so `btcusdt@depth` succeeds — but
`btcusdt@markPrice` belongs to `/market` and will **not** deliver. This fails silently rather than
erroring, so it is easy to mistake for a stream that has simply gone quiet.

Spot and COIN-M do **not** use routed paths. Only USD-M does.

:::

The full stream catalogues are at
[Spot ws-streams](/catalog/core-trading-spot-trading/api/ws-streams/~),
[USD-M ws-streams](/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-streams/~) and
[COIN-M ws-streams](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~).

## How this differs from user data streams

|                | Market data streams                | [User data streams](/products/caas/user-data-streams) |
| -------------- | ---------------------------------- | ----------------------------------------------------- |
| Authentication | None — public                      | API key of the account concerned                      |
| Scope          | Exchange-wide, per symbol          | One account                                           |
| Connections    | One connection can serve all users | One per account, per product family                   |
| Carries        | Prices, order books, trades        | Balances, orders, positions                           |

This distinction matters for capacity planning. Market data does **not** scale with your end-user
count — a single connection can feed every user in your application. User data streams do scale with
end-user count, because each sub-account needs its own.

## Where to go next

| If you need                           | Go to                                                                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account, balance, and order events    | [User Data Streams](/products/caas/user-data-streams)                                                                                              |
| Spot stream reference                 | [Spot WebSocket streams](/products/spot/web-socket-streams)                                                                                        |
| Managing a local order book correctly | [How to manage a local order book](/products/derivatives-trading-usds-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly) |

---

# Market Data Streams

Market data streams carry prices, order books, and trades for the whole exchange. They are
**public** — no API key, no signature, and nothing CAAS-specific about them.

Use them to drive prices and charts in your own front end. They are separate from
[User Data Streams](/products/caas/user-data-streams), which carry the account and order events for
one specific account and do require a key.

## Which stream to connect to

| Product        | Base endpoint                                   | Reference                                                                                            |
| -------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Spot           | `wss://stream.binance.com`                      | [Spot WebSocket streams](/products/spot/web-socket-streams)                                          |
| USD-M Futures  | `wss://fstream.binance.com/public` or `/market` | [USD-M market streams](/products/derivatives-trading-usds-futures/websocket-market-streams/Connect)  |
| COIN-M Futures | `wss://dstream.binance.com`                     | [COIN-M market streams](/products/derivatives-trading-coin-futures/websocket-market-streams/Connect) |

Spot also offers `wss://data-stream.binance.vision` as a market-data-only alternative.

## USD-M Futures routes streams by path

USD-M Futures is the exception. `fstream.binance.com` splits into three routed paths, and which one
you need depends on the stream:

| Path       | Carries                                                               |
| ---------- | --------------------------------------------------------------------- |
| `/public`  | High-frequency public market data, for example `@depth`               |
| `/market`  | Regular market data, for example `@aggTrade` and `@markPrice`         |
| `/private` | User data — see [User Data Streams](/products/caas/user-data-streams) |

```
wss://fstream.binance.com/market/ws/bnbusdt@aggTrade
wss://fstream.binance.com/public/ws/bnbusdt@depth
wss://fstream.binance.com/market/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice
```

:::warning

**A connection with no routed path only receives `/public` data.** `wss://fstream.binance.com/ws/…`
still works for streams that belong to `/public`, so `btcusdt@depth` succeeds — but
`btcusdt@markPrice` belongs to `/market` and will **not** deliver. This fails silently rather than
erroring, so it is easy to mistake for a stream that has simply gone quiet.

Spot and COIN-M do **not** use routed paths. Only USD-M does.

:::

The full stream catalogues are at
[Spot ws-streams](/catalog/core-trading-spot-trading/api/ws-streams/~),
[USD-M ws-streams](/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-streams/~) and
[COIN-M ws-streams](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~).

## How this differs from user data streams

|                | Market data streams                | [User data streams](/products/caas/user-data-streams) |
| -------------- | ---------------------------------- | ----------------------------------------------------- |
| Authentication | None — public                      | API key of the account concerned                      |
| Scope          | Exchange-wide, per symbol          | One account                                           |
| Connections    | One connection can serve all users | One per account, per product family                   |
| Carries        | Prices, order books, trades        | Balances, orders, positions                           |

This distinction matters for capacity planning. Market data does **not** scale with your end-user
count — a single connection can feed every user in your application. User data streams do scale with
end-user count, because each sub-account needs its own.

## Where to go next

| If you need                           | Go to                                                                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account, balance, and order events    | [User Data Streams](/products/caas/user-data-streams)                                                                                              |
| Spot stream reference                 | [Spot WebSocket streams](/products/spot/web-socket-streams)                                                                                        |
| Managing a local order book correctly | [How to manage a local order book](/products/derivatives-trading-usds-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly) |