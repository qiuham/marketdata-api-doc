---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/market_data_only
api_type: Guide
updated_at: 2026-11-20 18:37:51.663623
---

# Market Data Only URLs

These URLs do not require any authentication (i.e. The API key is not necessary) and serve only
public market data.

### RESTful API

On the RESTful API, these are the endpoints you can request on `data-api.binance.vision`:

- [GET /api/v3/aggTrades](/catalog/core-trading-spot-trading/api/rest-api/market#agg-trades)
- [GET /api/v3/avgPrice](/catalog/core-trading-spot-trading/api/rest-api/market#avg-price)
- [GET /api/v3/depth](/catalog/core-trading-spot-trading/api/rest-api/market#depth)
- [GET /api/v3/exchangeInfo](/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info)
- [GET /api/v3/klines](/catalog/core-trading-spot-trading/api/rest-api/market#klines)
- [GET /api/v3/ping](/catalog/core-trading-spot-trading/api/rest-api/general#ping)
- [GET /api/v3/ticker](/catalog/core-trading-spot-trading/api/rest-api/market#ticker)
- [GET /api/v3/ticker/24hr](/catalog/core-trading-spot-trading/api/rest-api/market#ticker24hr)
- [GET /api/v3/ticker/bookTicker](/catalog/core-trading-spot-trading/api/rest-api/market#ticker-book-ticker)
- [GET /api/v3/ticker/price](/catalog/core-trading-spot-trading/api/rest-api/market#ticker-price)
- [GET /api/v3/time](/catalog/core-trading-spot-trading/api/rest-api/general#time)
- [GET /api/v3/trades](/catalog/core-trading-spot-trading/api/rest-api/market#get-trades)
- [GET /api/v3/uiKlines](/catalog/core-trading-spot-trading/api/rest-api/market#ui-klines)

Sample request:

```
curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
```

### Websocket Streams

Public market data can also be retrieved through the websocket market data using the URL
`data-stream.binance.vision`. The streams available through this domain are the same that can be
found in the [WebSocket Market Streams](../web-socket-streams.md) documentation.

Note that User Data Streams **cannot** be accessed through this URL.

Sample request:

```
wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m
```

---

# 仅提供市场数据的URL

这些 URL 不需要任何身份验证（即不需要 API Key）并且仅提供公开市场数据。

### RESTful API

在 RESTful API 上，您可以在 `data-api.binance.vision` 上访问以下接口：

- [GET /api/v3/aggTrades](/catalog/core-trading-spot-trading/api/rest-api/market#agg-trades)
- [GET /api/v3/avgPrice](/catalog/core-trading-spot-trading/api/rest-api/market#avg-price)
- [GET /api/v3/depth](/catalog/core-trading-spot-trading/api/rest-api/market#depth)
- [GET /api/v3/exchangeInfo](/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info)
- [GET /api/v3/klines](/catalog/core-trading-spot-trading/api/rest-api/market#klines)
- [GET /api/v3/ping](/catalog/core-trading-spot-trading/api/rest-api/general#ping)
- [GET /api/v3/ticker](/catalog/core-trading-spot-trading/api/rest-api/market#ticker)
- [GET /api/v3/ticker/24hr](/catalog/core-trading-spot-trading/api/rest-api/market#ticker24hr)
- [GET /api/v3/ticker/bookTicker](/catalog/core-trading-spot-trading/api/rest-api/market#ticker-book-ticker)
- [GET /api/v3/ticker/price](/catalog/core-trading-spot-trading/api/rest-api/market#ticker-price)
- [GET /api/v3/time](/catalog/core-trading-spot-trading/api/rest-api/general#time)
- [GET /api/v3/trades](/catalog/core-trading-spot-trading/api/rest-api/market#get-trades)
- [GET /api/v3/uiKlines](/catalog/core-trading-spot-trading/api/rest-api/market#ui-klines)

请求示例:

```
curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
```

### Websocket Streams

也可以通过 Websocket 市场数据的 URL `data-stream.binance.vision`
提取公共市场数据。此域名所提供的 stream 与 [WebSocket Market Streams_CN](../web-socket-streams.md)
文档中的相同。请注意用户数据流**无法**从此 URL 获得。

请求示例:

```
wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m
```