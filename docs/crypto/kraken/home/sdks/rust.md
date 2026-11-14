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
source_url: 'https://docs.kraken.com/home/sdks/rust'
updated_at: 2026-11-13
---

# Rust

> kraken-sdk — the official Rust SDK for the Spot API, plus Derivatives streams and order entry over the Unified WebSocket

[kraken-sdk](https://github.com/krakenfx/kraken-api-sdk) is the official Rust SDK for building integrations against the Spot API and, over the Unified WebSocket, the Derivatives (Futures) API. It is async-native, built on tokio, and presents REST and WebSocket behind a single client.

> [!NOTE]
>
> Spot is covered over REST and WebSocket v2. Derivatives is covered over the Unified WebSocket only: public and private streams, and order entry. There are no Derivatives REST methods.

## Requirements

Requires Rust 1.88 or later and the tokio async runtime.

## Install

```toml theme={null} theme={null}
[dependencies]
kraken-sdk = { git = "https://github.com/krakenfx/kraken-api-sdk", tag = "v0.1.0" }
tokio = { version = "1", features = ["full"] }
rust_decimal = "1"
```

## What it covers

### Spot

* Spot REST — complete public market data, plus authenticated account and trading endpoints
* Spot WebSocket v2 — public data streams and the authenticated `executions` and `balances` channels
* Order operations: add, amend, cancel, batch add, batch cancel, cancel-all, and a dead man's switch
* Order routing over REST or authenticated WebSocket, selectable per call
* Real-time order book construction with CRC32 checksum validation and automatic reseeding on mismatch

### Derivatives (Futures)

* Public Unified WebSocket streams — system status, instrument, ticker, trade, OHLC and order book (maintained with CRC32 validation, or raw deltas)
* Private Unified WebSocket streams — `executions`, `positions`, `balances`, `margin` and `preferences`
* Order operations over the authenticated Unified WebSocket: place, amend, cancel by client order id or venue order id, batch place (2–15 orders on one symbol), batch cancel (2–50 orders), cancel-all, and a dead man's switch that is independent of Spot's
* Uses the same API key as Spot

### Both

* Automatic reconnect with subscription replay
* Typed errors carrying a stable code, category, retryable flag and request id
* An event bus for connection state, rate-limit warnings, order book gaps and order lifecycle

## Example

```rust theme={null} theme={null}
use kraken_sdk::{ApiKey, Client, Symbol};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder()
        .with_api_key(
            ApiKey::new(std::env::var("KRAKEN_API_KEY")?),
            std::env::var("KRAKEN_API_SECRET")?,
        )?
        .build()?;

    let resp = client.trade()
        .limit_buy(Symbol::new("BTC/USD")?, "0.01".parse()?, "60000".parse()?)
        .await?;

    println!("placed {:?}", resp.txid);
    Ok(())
}
```

Public market data needs no credentials:

```rust theme={null} theme={null}
use kraken_sdk::{Client, Symbol};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder().build()?;
    let pair = Symbol::new("BTC/USD")?;

    let tickers = client.market().ticker(Some(&[pair.clone()])).await?;
    if let Some(t) = tickers.get(&pair) {
        println!("last={} bid={} ask={}", t.last_price, t.bid_price, t.ask_price);
    }
    Ok(())
}
```

### Derivatives example

Stream a Futures order book, then place a limit order. Futures orders always travel on the authenticated Unified WebSocket, so call `client.ready()` before the first WebSocket operation.

```rust theme={null} theme={null}
use kraken_sdk::{
    ApiKey, BookDepth, Client, FuturesOrder, FuturesOrderRequest, OrderType, Side,
};
use rust_decimal::Decimal;
use std::str::FromStr;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder()
        .with_api_key(
            ApiKey::new(std::env::var("KRAKEN_API_KEY")?),
            std::env::var("KRAKEN_API_SECRET")?,
        )
        .build()?;
    client.ready().await?;

    // Dropping the guard unsubscribes and deregisters the handler
    let _book = client.market().futures().on_book_for(
        vec!["PF_XBTUSD".to_owned()],
        BookDepth::D10,
        |book| println!("{} bids={} asks={}", book.symbol, book.bids.len(), book.asks.len()),
    )?;

    let order = FuturesOrder::new(Side::Buy, Decimal::from_str("0.01")?)
        .order_type(OrderType::Limit)
        .price(Decimal::from_str("1500")?);
    let resp = client
        .trade()
        .futures()
        .order(FuturesOrderRequest::new("PF_ETHUSD", order))
        .await?;

    println!("placed {:?}", resp.txid);
    client.close().await?;
    Ok(())
}
```

Public Futures streams need no credentials. The private channels and order entry do.

## Notes for developers coming from other Kraken SDKs

* **Spot symbols use the modern format only.** `BTC/USD`, not `XBTUSD` or `XXBTZUSD`. Legacy codes return a typed error rather than being silently translated. Asset codes in responses are normalised the same way, so balances are keyed `BTC` and `USD`.
* **Derivatives symbols are the native venue strings.** `PF_XBTUSD`, `PF_ETHUSD` and dated contracts such as `FI_XBTUSD_251226`. A Spot pair sent to a Futures method is rejected before anything is sent.
* **Prices and quantities are decimals, not floats.** Parse them from strings (`"0.01".parse()?`). The API does not accept `f64`.
* **A WebSocket subscription is two steps:** register a handler, then subscribe. The `on_*_for` helpers do both in one call and unsubscribe when dropped.
* **Rate limits are reported, not enforced.** For Spot, the SDK emits a warning event as you approach your tier limit and never sleeps on your behalf, so pacing stays under your control. It does not track Derivatives orders. A venue throttle comes back as a retryable `RateLimited` error.
* **Derivatives has no REST path.** `.via(Transport::Rest)` on a Futures order returns a typed `UnsupportedTransport` error.
* **Dead man's switches are per product.** The Spot and Derivatives timers are independent, and `cancel_all` on one does not touch the other's orders.

See the [kraken-sdk repository](https://github.com/krakenfx/kraken-api-sdk) for the full method reference, guides and event catalogue.
