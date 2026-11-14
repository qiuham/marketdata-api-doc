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
source_url: 'https://docs.kraken.com/exchange/guides/general/historical-data'
updated_at: 2026-11-13
---

# Historical data

> How to access OHLCV history, trade ticks, and order book snapshots for backtesting and research

Kraken's public REST endpoints provide historical market data without authentication. This page covers what's available, the limits per call, and how to paginate efficiently for bulk collection.

## Available data types

| Data type | Endpoint | Depth | Authenticated |
| :- | :- | :- | :- |
| OHLCV candles | `GET /0/public/OHLC` | Up to 720 candles per call | No |
| Trade ticks | `GET /0/public/Trades` | Up to 1000 trades per call | No |
| Order book snapshot | `GET /0/public/Depth` | Up to 500 levels per side | No |
| Grouped book | `GET /0/public/GroupedBook` | Configurable tick size | No |
| L3 order book | `POST /0/private/Level3` | Full book | Yes |

## OHLCV candles

The `OHLC` endpoint returns candlestick data for a given interval.

```bash theme={null}
GET /0/public/OHLC?pair=XBTUSD&interval=1440&since=1700000000
```

**Parameters:**

| Parameter | Values | Default |
| :- | :- | :- |
| `pair` | Instrument name (e.g. `XBTUSD`) | Required |
| `interval` | `1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600` (minutes) | `1` |
| `since` | Unix timestamp — return candles after this time | Oldest available |

**Response structure:**

```json theme={null}
{
  "result": {
    "XXBTZUSD": [
      [1700000000, "37000.0", "37500.0", "36800.0", "37200.0", "37100.0", "150.5", 320],
      ...
    ],
    "last": 1700086400
  }
}
```

Each candle: `[time, open, high, low, close, vwap, volume, count]`

**Pagination:** use the `last` value from the response as the `since` parameter in your next call to page forward.

**Depth limits:**

* Maximum 720 candles per call
* Daily candles (`interval=1440`): \~720 days (\~2 years) per call
* Minute candles (`interval=1`): 720 minutes (\~12 hours) per call

**Practical tip for collecting a year of daily data:**

```python theme={null}
import requests, time

def fetch_ohlcv(pair, interval, since=None):
    params = {"pair": pair, "interval": interval}
    if since:
        params["since"] = since
    r = requests.get("https://api.kraken.com/0/public/OHLC", params=params)
    data = r.json()
    result = list(data["result"].values())[0]  # candles
    last = data["result"]["last"]
    return result, last

all_candles = []
since = None

while True:
    candles, last = fetch_ohlcv("XBTUSD", 1440, since)
    if not candles:
        break
    all_candles.extend(candles)
    if since == last:
        break
    since = last
    time.sleep(1)  # respect rate limits
```

## Trade ticks

The `Trades` endpoint returns a time-ordered list of public trades.

```bash theme={null}
GET /0/public/Trades?pair=XBTUSD&since=1700000000000000000&count=1000
```

**Parameters:**

| Parameter | Description |
| :- | :- |
| `pair` | Instrument name |
| `since` | Nanosecond timestamp — return trades after this time |
| `count` | Max trades per call (up to 1000) |

**Response structure:**

```json theme={null}
{
  "result": {
    "XXBTZUSD": [
      ["37200.00000", "0.05000000", 1700000001.1234, "b", "l", "", 12345678],
      ...
    ],
    "last": "1700000100000000000"
  }
}
```

Each trade: `[price, volume, time, buy/sell, market/limit, miscellaneous, trade_id]`

**Pagination:** use `last` as the `since` value in the next call. The `since` value is in nanoseconds.

**Rate limit note:** the Trades endpoint is public and subject to IP-based rate limits. For bulk historical collection, introduce a delay between requests (100–200ms) to avoid throttling.

## Order book snapshots

The `Depth` endpoint returns the current order book at the time of the request. It is not a historical endpoint — it reflects the live state.

```bash theme={null}
GET /0/public/Depth?pair=XBTUSD&count=100
```

For L3 (order-by-order) book data, use the authenticated `Level3` endpoint:

```bash theme={null}
POST /0/private/Level3
# body: pair=XBT/USD
```

L3 data includes individual `OrderID` values, enabling reconciliation with `ExecutionReport` data from FIX or the `executions` WebSocket channel.

## Futures historical data

Futures provides dedicated historical endpoints under the Futures REST API:

| Data | Endpoint |
| :- | :- |
| OHLCV candles | `GET /api/charts/v1/{tick_type}/{symbol}/{resolution}` |
| Trade history (fills) | `GET /derivatives/api/v3/history` |
| Historical funding rates | `GET /derivatives/api/v3/historicalfundingrates` |

```bash theme={null}
# Get BTC perpetual daily candles
GET https://futures.kraken.com/api/charts/v1/trade/PI_XBTUSD/1D

# Get historical funding rates
GET https://futures.kraken.com/derivatives/api/v3/historicalfundingrates?symbol=PI_XBTUSD
```

## Building a backtesting dataset

A practical approach for collecting a clean historical dataset:

**1. Collect OHLCV for your timeframe**

Start with daily candles to get a broad picture, then drill into minute candles for the periods you need. Use the pagination pattern above.

**2. Augment with trade ticks for microstructure**

Trade ticks give you the actual execution prices and sizes. Useful for modelling slippage and for tick-by-tick backtesting.

**3. Validate against VWAP**

Each OHLC candle includes VWAP. Cross-check your collected trade ticks against the VWAP to verify completeness and catch any pagination gaps.

**4. Handle gaps**

Thin markets or API collection gaps can leave missing candles. Decide upfront how to handle them: forward-fill with the previous close, or exclude those periods from your strategy.

> [!NOTE]
>
> Kraken does not provide a bulk historical data dump or websocket replay service. For very deep history (years of tick data) consider supplementing with third-party data providers.

## Rate limits for data collection

Historical data endpoints are public but rate-limited per IP. Recommended safe intervals:

| Endpoint | Safe delay between calls |
| :- | :- |
| `OHLC` | 1 second |
| `Trades` | 1–2 seconds |
| `Depth` | 1 second |

If you need faster collection, distribute requests across multiple IPs or use the FIX market data feed for real-time capture going forward.

## Related guides

> [card] [API comparison](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> FIX and WebSocket for real-time market data capture

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> IP-based rate limits for public data endpoints

> [card] [WebSocket introduction](https://docs.kraken.com/exchange/guides/websockets/introduction.md)
>
> Stream live market data for forward capture alongside historical backfill
