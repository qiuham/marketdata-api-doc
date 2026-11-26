---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/live-data/overview'
updated_at: 2026-11-26
---

# PolyBolt WebSocket

> Stream crypto, equity and TWAP reference prices over one WebSocket connection.

PolyBolt streams crypto, equity and TWAP reference prices over a single
connection. Subscriptions require CLOB API credentials.

For existing RTDS integrations, see [Migrate from RTDS to PolyBolt](https://docs.polymarket.com/migrate/rtds-to-polybolt.md).

> [!WARNING]
>
> Price subscriptions must name a provider.
> Subscriptions served by Chainlink also require your Chainlink API key. See
> [Send Your Chainlink API Key](#send-your-chainlink-api-key) and [Pin a Price
> Provider](#pin-a-price-provider).

## Connect

Open a WebSocket connection to:

```text theme={null}
wss://ws-live-v2.polymarket.com/ws
```

Choose a channel, authenticate, then send a subscription request.

## Channels

| Channel | Data | Filter | Access |
| - | - | - | - |
| `price.crypto` | Crypto reference prices | `{"symbol": "btcusd", "provider": "chainlink"}` | CLOB API credentials |
| `price.equity` | Stock, ETF, forex, metal and commodity reference prices | `{"symbol": "aapl", "provider": "pyth"}` | CLOB API credentials |
| `price.crypto.twap` | 60-second time-weighted average prices (TWAP) from Chainlink | `{"symbol": "btcusd", "window_seconds": 60, "provider": "chainlink"}` | CLOB API credentials |
| `price.equity.twap` | 60-second forex TWAP prices from Chainlink (`eurusd` and `usdjpy`) | `{"symbol": "eurusd", "window_seconds": 60, "provider": "chainlink"}` | CLOB API credentials |

Use lowercase symbols, and name the provider in every filter (see
[Pin a Price Provider](#pin-a-price-provider)).

## Authenticate for Gated Channels

Send your
[CLOB API credentials](https://docs.polymarket.com/getting-started/api.md#authentication) on the open connection
before subscribing:

```json theme={null}
{
  "op": "auth",
  "rid": "a1",
  "auth": {
    "apiKey": "<api key>",
    "secret": "<api secret>",
    "passphrase": "<api passphrase>"
  }
}
```

Wait for the server to confirm authentication:

```json theme={null}
{
  "op": "authed",
  "rid": "a1"
}
```

### Send Your Chainlink API Key

Subscriptions served by Chainlink, including TWAP, require your Chainlink API key in addition to CLOB API credentials.

> [!NOTE]
>
> Request a Chainlink API Key using [this form](https://institutional.polymarket.com/request-chainlink-api-key).

> [tab] TypeScript
>
> Use an authenticated [SecureClient](https://docs.polymarket.com/trading/wallets-auth.md) and pass your key as `providerApiKey` with the Chainlink provider.
>
> ```ts theme={null}
> import { PriceProvider } from "@polymarket/client";
>
> const stream = await client.subscribe([
>   {
>     topic: "prices.crypto.twap",
>     symbols: ["btcusd"],
>     provider: PriceProvider.Chainlink,
>     providerApiKey: "<chainlink api key>",
>   },
> ]);
>
> try {
>   for await (const event of stream) {
>     // event: CryptoTwapPriceEvent
>   }
> } finally {
>   await stream.close();
> }
> ```

> [tab] Python
>
> Use an authenticated [AsyncSecureClient](https://docs.polymarket.com/trading/wallets-auth.md) and pass your key as `provider_api_key` with the Chainlink provider.
>
> ```python theme={null}
> from polymarket.streams import CryptoTwapPriceSpec
>
> async with await client.subscribe(
>     CryptoTwapPriceSpec(
>         symbols=["btcusd"],
>         provider="chainlink",
>         provider_api_key="<chainlink api key>",
>     )
> ) as stream:
>     async for event in stream:
>         # event: CryptoTwapPriceEvent
>         pass
> ```

> [tab] API
>
> Send `chainlink_api_key` in the first `auth` frame alongside your CLOB API credentials. To change the key, open a new connection.
>
> ```json theme={null}
> {
>   "op": "auth",
>   "rid": "a1",
>   "auth": {
>     "apiKey": "<api key>",
>     "secret": "<api secret>",
>     "passphrase": "<api passphrase>"
>   },
>   "chainlink_api_key": "<chainlink api key>"
> }
> ```

Subscriptions served by other providers do not need an API key for now. If a requested provider falls back to Chainlink, the key is still required.

The server reports authentication problems with an error acknowledgement, for example:

```json theme={null}
{
  "op": "error",
  "code": "auth_required",
  "channel": "price.crypto",
  "rid": "s1"
}
```

These errors leave the connection open:

| Code | Meaning | Action |
| - | - | - |
| `auth_required` | The subscription was sent before authentication. | Authenticate, then resend the subscription. |
| `auth_invalid` | The credentials were rejected. | Correct the credentials before retrying. |
| `auth_unavailable` | Authentication is temporarily unavailable. | Wait, then retry authentication. |
| `chainlink_key_required` | A subscription served by Chainlink was sent on a connection authenticated without a Chainlink API key. | Open a new connection, authenticate with `chainlink_api_key`, then resend the subscription. |

`chainlink_key_required` also carries a numeric `status` of `4010`. It is not a
close code: the connection stays open.

## Subscribe

Send the channels and filters you want to follow. This request subscribes to the
BTC reference price from Chainlink on a connection authenticated with your
Chainlink API key:

```json theme={null}
{
  "op": "subscribe",
  "rid": "s1",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "chainlink" } }
  ]
}
```

A batch counts as one request against the rate limit.

### Pin a Price Provider

Crypto and equity prices can come from more than one vendor. Every payload
names its producer in `source`. Choose one by adding `provider` to the filter:

```json theme={null}
{
  "op": "subscribe",
  "rid": "s2",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "pyth" } }
  ]
}
```

`provider` accepts `chainlink`, `pyth` or `binance`. Binance serves
`price.crypto` only, with USDT spot closes under the canonical USD symbol. The
`subscribed` acknowledgement names the provider actually served. A pin the
server cannot serve for that symbol falls back to the symbol's default
provider, and the acknowledgement names the fallback, so always read the
acknowledgement rather than assuming the pin held. The TWAP channels are
served by Chainlink only, so pin `chainlink` there.

Values other than `chainlink`, `pyth` or `binance` are rejected with a
`bad_filter` error.

`provider` is required on
`price.crypto`, `price.equity`, `price.crypto.twap` and `price.equity.twap`.
A subscription without `provider`
answers this error, and the connection stays open:

```json theme={null}
{
  "op": "error",
  "code": "provider_required",
  "status": 4011,
  "channel": "price.crypto",
  "rid": "s2"
}
```

### Read the Market Status

Equity markets close: exchanges keep session hours, and metals and forex
pause daily and over the weekend. On `price.equity` and `price.equity.twap`,
each payload says whether the market of the instrument it prices is trading,
so you can show "closed at" a price instead of a price that silently stops
moving.

`market_status` is `open`, `closed` or `unknown` (the vendor reported that it
cannot determine the status). It is absent when the producer states nothing:
treat an absent status as not stated, never as open.

The status belongs to the provider's series, because it describes the
instrument that provider prices. Chainlink's equity products trade around the
clock, so a symbol served by Chainlink can read `open` on a weekend while the
same symbol pinned to `pyth` follows its exchange session and reads `closed`.

When the status changes without a new price, you receive a normal update that
repeats the last price with the new status and `is_carried_forward: true`:

```json theme={null}
{
  "v": 1,
  "channel": "price.equity",
  "seq": 41,
  "ts": 1792526399800,
  "payload": {
    "symbol": "aapl",
    "value": 262.71,
    "full_accuracy_value": "262.71",
    "timestamp": 1792526399800,
    "received_at": 1792526401200,
    "is_carried_forward": true,
    "source": "pyth",
    "market_status": "closed"
  }
}
```

That update shares its `timestamp` and `value` with the update before it, so
never discard an update only because its `timestamp` repeats. While a series
is `closed` or `unknown`, its snapshot also carries the last price point even
when it is older than two minutes, and the snapshot's `ts` is that point's
time. Re-read `market_status` from the snapshot after every reconnect.

SDK 0.14.0 and later expose this field as `payload.marketStatus` in TypeScript
and `payload.market_status` in Python, on snapshots and live updates. See
[Read the Market Status](https://docs.polymarket.com/market-data/realtime-data.md#read-the-market-status) for
TypeScript, Python, and API examples.

## Envelope

Data envelopes carry snapshots and live updates. Acknowledgements report the
result of a request.

```json Live Update theme={null}
{
  "v": 1,
  "channel": "price.crypto",
  "seq": 2,
  "ts": 1788973001000,
  "payload": {
    "symbol": "btcusd",
    "value": 64126.0,
    "full_accuracy_value": "64126.00000000",
    "timestamp": 1788973001000,
    "source": "chainlink"
  }
}
```

```json Snapshot theme={null}
{
  "v": 1,
  "channel": "price.crypto",
  "seq": 1,
  "ts": 1788973000000,
  "snapshot": true,
  "payload": {
    "symbol": "btcusd",
    "source": "chainlink",
    "data": [
      {
        "timestamp": 1788972880000,
        "value": 64123.5,
        "full_accuracy_value": "64123.50000000"
      },
      {
        "timestamp": 1788972881000,
        "value": 64125.1,
        "full_accuracy_value": "64125.10000000"
      }
    ]
  }
}
```

```json Acknowledgement theme={null}
{
  "op": "subscribed",
  "channel": "price.crypto",
  "rid": "s1",
  "provider": "chainlink"
}
```

Acknowledgements echo `rid` when the request includes it.

| `op` | Meaning |
| - | - |
| `authed` | Authentication succeeded. You can subscribe to gated channels. |
| `subscribed` | The subscription was accepted. `channel` identifies the channel; on price channels, `provider` names the vendor served. |
| `unsubscribed` | The unsubscribe request was accepted. `channel` identifies the channel. |
| `pong` | The server received your application-level `ping` request. |
| `error` | The request failed. `code` identifies the reason. Policy violations can also close the connection. |

`chainlink_key_required` and `provider_required` errors also carry a numeric
`status`, `4010` and `4011`. Neither closes the connection.

Each new subscription receives an acknowledgement and one snapshot. Seed local state from the snapshot, then apply the latest price. Snapshots contain the preceding two minutes of prices, with an empty `data` array when no recent data is available. Repeating an existing channel and filter returns another acknowledgement without a new snapshot.

For data envelopes:

* `seq` is consecutive per connection and per channel, including snapshots. It resets on reconnect.
* `ts` is the producer's event time in Unix milliseconds.
* `snapshot: true` identifies the initial snapshot.
* `dropped`, when present, counts frames dropped on that channel since the last delivered frame because the client fell behind.
* `source` names the vendor that produced the price (`pyth`, `massive` or `chainlink`): on every point of a live update and once per snapshot batch. On single-provider channels it is constant; on `price.crypto` and the equity channels a symbol's vendor can change between connections, so re-read it after every reconnect.
* `market_status`, on the equity channels, is `open`, `closed` or `unknown`: on every live update and once per snapshot batch, absent when not stated. See [Read the Market Status](#read-the-market-status).

Compare sequence numbers only within the same connection and channel. See the
[Live Data Channel](https://docs.polymarket.com/api-reference/wss/polybolt.md) for every message schema and
`https://ws-live-v2.polymarket.com/asyncapi.json` for the machine-readable contract.

## Unsubscribe

Send the same channel and filter with `op: "unsubscribe"` to stop a subscription:

```json theme={null}
{
  "op": "unsubscribe",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "chainlink" } }
  ]
}
```

The server confirms with `unsubscribed`. Both `subscribe` and `unsubscribe`
accept a single `channel` and `filter` or a `subscriptions` array.

## Supported Symbols

### Crypto Prices

| Channel | Symbols |
| - | - |
| `price.crypto` | `btcusd`, `ethusd`, `solusd`, `xrpusd`, `dogeusd`, `hypeusd`, `bnbusd`, `zecusd` |
| `price.crypto.twap` | `btcusd`, `ethusd`, `solusd`, `xrpusd`, `dogeusd`, `hypeusd`, `bnbusd`, `zecusd` |
| `price.equity.twap` | `eurusd`, `usdjpy` |

For the TWAP channels, use `window_seconds: 60`. Other windows do not provide data.

Every `price.crypto` symbol is served by Chainlink, its default provider, and
by Binance. `btcusd`, `ethusd`, `solusd`, `xrpusd`, `dogeusd` and `bnbusd` are
also served by Pyth; on `hypeusd` and `zecusd` a `pyth` pin falls back to
Chainlink. `price.crypto.twap` is Chainlink only.

### Equity Prices

`price.equity` supports these lowercase symbols:

| Asset class | Symbols |
| - | - |
| Stocks | `aapl`, `tsla`, `msft`, `googl`, `amzn`, `meta`, `nvda`, `nflx`, `pltr`, `open`, `rklb`, `abnb`, `coin`, `hood`, `spcx`, `intc`, `mstr`, `crcl`, `mu` |
| ETFs | `qqq`, `spy`, `ewy`, `vxx` |
| Forex | `eurusd`, `gbpusd`, `usdcad`, `usdjpy`, `usdkrw`, `usdchf`, `usdmxn`, `usdzar`, `usdbrl`, `usdnok`, `usdsek`, `usdtry`, `dxy` |
| Precious metals | `xauusd`, `xagusd` |

`dxy` is the US Dollar Index.

Each equity symbol has a default provider, which serves any pin the symbol
does not support, including every `binance` pin:

| Symbols | Default | Pinnable |
| - | - | - |
| `xauusd`, `xagusd`, `nvda`, `googl`, `tsla`, `spcx`, `mu` | `chainlink` | `pyth` |
| `intc`, `mstr`, `crcl`, `wti`, `brent`, `natgas` | `chainlink` | none |
| `eurusd`, `usdjpy` | `pyth` | `chainlink` |
| Every other equity symbol | `pyth` | none |

Commodities serve under `cll` (WTI crude oil futures) and `hn` (Henry Hub
natural gas futures) from Pyth, `wti` (WTI crude oil futures), `brent` (Brent
crude oil futures) and `natgas` (natural gas futures) from Chainlink, and
`cc3m` (the copper 3-month contract price in USD). Each futures symbol keeps
one symbol as its contract rolls. `cll` and `hn` move to the next contract at
the open of the current contract's third-to-last trading session, the Active
Month the WTI and natural gas Up or Down markets resolve on. `wti`, `brent`
and `natgas` follow Chainlink's own roll schedule. `cc3m` is a single
continuous contract.

## Limits and Liveness

| Limit | Value | On breach |
| - | - | - |
| Active subscriptions per connection | 64 `(channel, filter)` pairs | `sub_limit` error, then close `4008` |
| Subscribe or unsubscribe frames | 20 per second (a batch counts once) | `rate_limited` error, then close `4008` |
| Frame size | 64 KB | close `4008` |
| Auth frames per connection | 8 | `auth_attempts` error, then close `4008` |

The server sends a WebSocket ping every 25 seconds. Standard clients answer
automatically. Two missed pongs close the connection with `4002`.

You can also send `{ "op": "ping" }` to check the connection at the application
level. The server responds with `pong`.

## Close Codes and Reconnecting

Choose the retry behavior based on the close code:

| Code | Meaning | Client behavior |
| - | - | - |
| `4001` | Authentication failed | Fix authentication before reconnecting. |
| `4002` | Slow consumer or pong timeout | Retry with exponential backoff and jitter. Reduce subscription load if this repeats. |
| `4003` | Server draining | Reconnect after a uniformly random delay of 0 to 10 seconds. |
| `4008` | Policy violation | Fix the request or limit violation before reconnecting. |
| `1006` | Abnormal disconnect | Retry with exponential backoff and full jitter, starting at 1 second and capped at 30 seconds. |

If the connection is refused with HTTP `429` or `503`, use `Retry-After` as the minimum
wait and add jitter. Browser clients see handshake failures as `1006` and should
use exponential backoff with full jitter.

After reconnecting, authenticate again for gated channels and resend your
subscriptions with their `provider` pins. Initialize from the new
snapshots and re-read `source`: a crypto or equity symbol can legitimately
arrive from a different vendor than before the reconnect. Sequence numbers
start over.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
