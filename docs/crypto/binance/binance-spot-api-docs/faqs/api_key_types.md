---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/faqs/api_key_types
api_type: REST
updated_at: 2026-06-30 19:04:34.387639
---

# Market Data Only URLs

These URLs do not require any authentication (i.e. The API key is not necessary) and serve only public market data.

### RESTful API[​](/docs/binance-spot-api-docs/faqs/market_data_only#restful-api "Direct link to RESTful API")

On the RESTful API, these are the endpoints you can request on `data-api.binance.vision`:

  * [GET /api/v3/aggTrades](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#compressedaggregate-trades-list)
  * [GET /api/v3/avgPrice](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#current-average-price)
  * [GET /api/v3/depth](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#order-book)
  * [GET /api/v3/exchangeInfo](/docs/binance-spot-api-docs/rest-api/general-endpoints#exchange-information)
  * [GET /api/v3/klines](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klines)
  * [GET /api/v3/ping](/docs/binance-spot-api-docs/rest-api/general-endpoints#test-connectivity)
  * [GET /api/v3/ticker](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#rolling-window-price-change-statistics)
  * [GET /api/v3/ticker/24hr](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics)
  * [GET /api/v3/ticker/bookTicker](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-order-book-ticker)
  * [GET /api/v3/ticker/price](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-price-ticker)
  * [GET /api/v3/time](/docs/binance-spot-api-docs/rest-api/general-endpoints#check-server-time)
  * [GET /api/v3/trades](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#recent-trades-list)
  * [GET /api/v3/uiKlines](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#uiKlines)



Sample request:
    
    
    curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"  
    

### Websocket Streams[​](/docs/binance-spot-api-docs/faqs/market_data_only#websocket-streams "Direct link to Websocket Streams")

Public market data can also be retrieved through the websocket market data using the URL `data-stream.binance.vision`. The streams available through this domain are the same that can be found in the [WebSocket Market Streams](/docs/binance-spot-api-docs/web-socket-streams) documentation.

Note that User Data Streams **cannot** be accessed through this URL.

Sample request:
    
    
    wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m

---

# 仅提供市场数据的URL

这些 URL 不需要任何身份验证（即不需要 API Key）并且仅提供公开市场数据。

### RESTful API[​](/docs/zh-CN/binance-spot-api-docs/faqs/market_data_only#restful-api "RESTful API的直接链接")

在 RESTful API 上，您可以在 `data-api.binance.vision` 上访问以下接口：

  * [GET /api/v3/aggTrades](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#aggTrades)
  * [GET /api/v3/avgPrice](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#avgPrice)
  * [GET /api/v3/depth](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#depth)
  * [GET /api/v3/exchangeInfo](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#exchangeInfo)
  * [GET /api/v3/klines](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#klines)
  * [GET /api/v3/ping](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#ping)
  * [GET /api/v3/ticker](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#rollingwindowticker)
  * [GET /api/v3/ticker/24hr](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#twentyfourhourticker)
  * [GET /api/v3/ticker/bookTicker](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#bookTicker)
  * [GET /api/v3/ticker/price](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#ticker-price)
  * [GET /api/v3/time](/docs/zh-CN/binance-spot-api-docs/rest-api/general-endpoints#time)
  * [GET /api/v3/trades](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#trades)
  * [GET /api/v3/uiKlines](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#uiKlines)



请求示例:
    
    
    curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"  
    

### Websocket Streams[​](/docs/zh-CN/binance-spot-api-docs/faqs/market_data_only#websocket-streams "Websocket Streams的直接链接")

也可以通过 Websocket 市场数据的 URL `data-stream.binance.vision` 提取公共市场数据。 此域名所提供的 stream 与 [WebSocket Market Streams_CN](/docs/zh-CN/binance-spot-api-docs/web-socket-streams) 文档中的相同。 请注意用户数据流**无法** 从此 URL 获得。

请求示例:
    
    
    wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m