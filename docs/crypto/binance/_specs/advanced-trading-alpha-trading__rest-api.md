---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:19.837644
---

# advanced-trading-alpha-trading__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Alpha Trading REST API
  description: APIs for Binance Alpha Trading.
  x-description-cn: Binance Alpha Trading 的 API。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/alpha/general-info#limits
x-rate-limits-guide-cn: products/alpha/general-info#访问限制
x-security-guide: products/alpha/general-info#request-security
x-security-guide-cn: products/alpha/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Alpha Trading docs
  url: https://developers.binance.com/en/docs/products/alpha/Introduction
tags:
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 市场数据
servers:
  - url: https://www.binance.com
paths:
  /bapi/defi/v1/public/alpha-trade/agg-trades:
    get:
      summary: Aggregated Trades
      x-summary-cn: 聚合交易查询
      description: Retrieves compressed, aggregated historical trades for a specific symbol. Useful for recent trade history.
      x-description-cn: 获取指定交易对的压缩聚合历史成交数据，适用于查询近期成交记录。
      tags:
        - market-data
      operationId: aggregatedTrades
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#aggregated-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/aggregatedTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/aggregated_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/aggregated_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/AggregatedTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/AggregatedTrades/AggregatedTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/AggregatedTradesExample.php
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: ALPHA_118USDC
          description: Trading pair symbol, e.g. ALPHA_118USDC (use token ID from Token List).
          x-description-cn: 交易对符号，例如 ALPHA_118USDC（请使用 Token 列表中的代币 ID）。
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 58470
            format: int64
          description: Starting aggregate trade ID to fetch from.
          x-description-cn: 起始聚合成交 ID。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1752568680000
            format: int64
          description: Start timestamp in milliseconds.
          x-description-cn: 起始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1752572280000
            format: int64
          description: End timestamp in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 500
            maximum: 1000
          description: Number of results to return.
          x-description-cn: 返回结果数量。
      responses:
        "200":
          description: Aggregated Trades
          x-description-cn: 聚合交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: ""
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: ""
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        a:
                          type: integer
                          example: 58470
                          format: int64
                          description: Aggregate trade ID.
                          x-description-cn: 聚合成交 ID。
                        p:
                          type: string
                          example: "1.00"
                          description: Trade price.
                          x-description-cn: 成交价格。
                        q:
                          type: string
                          example: "1.00"
                          description: Trade quantity.
                          x-description-cn: 成交数量。
                        f:
                          type: integer
                          example: 58470
                          format: int64
                          description: First trade ID in the aggregation.
                          x-description-cn: 聚合中的首笔成交 ID。
                        l:
                          type: integer
                          example: 58665
                          format: int64
                          description: Last trade ID in the aggregation.
                          x-description-cn: 聚合中的末笔成交 ID。
                        T:
                          type: integer
                          example: 1752568680000
                          format: int64
                          description: Trade timestamp in milliseconds.
                          x-description-cn: 成交时间戳（毫秒）。
                        m:
                          type: boolean
                          example: true
                          description: Whether buyer is the market maker (deprecated).
                          x-description-cn: 买方是否为做市方（已废弃）。
                    description: Array of aggregated trades.
                    x-description-cn: 聚合成交数据数组。
  /bapi/defi/v1/public/alpha-trade/fullDepth:
    get:
      summary: Full Depth
      x-summary-cn: 完整深度（订单簿）
      description: >-
        Fetches the full order book depth (UI & API orders) for a symbol, including bid and ask orders with their prices
        and quantities.
      x-description-cn: 获取指定交易对的完整订单簿深度（UI 和 API 订单），包括买单和卖单的价格和数量。
      tags:
        - market-data
      operationId: fullDepth
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#full-depth
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/fullDepth.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/full_depth.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/full_depth.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/FullDepthExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/FullDepth/FullDepth.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/FullDepthExample.php
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: ALPHA_175USDT
          description: Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).
          x-description-cn: 交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 500
            enum:
              - 5
              - 10
              - 20
              - 50
              - 100
              - 500
              - 1000
          description: "Number of price levels to return. Valid values: 5, 10, 20, 50, 100, 500, 1000."
          x-description-cn: 返回的价格档位数量。有效值：5、10、20、50、100、500、1000。
      responses:
        "200":
          description: Full Depth
          x-description-cn: 完整深度
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: null
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: null
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful.
                    x-description-cn: 请求是否成功。
                  data:
                    type: object
                    properties:
                      lastUpdateId:
                        type: integer
                        example: 47534656223
                        format: int64
                        description: Last order book update ID.
                        x-description-cn: 最新订单簿更新 ID。
                      symbol:
                        type: string
                        example: ALPHA_175USDT
                        description: Trading pair symbol.
                        x-description-cn: 交易对符号。
                      bids:
                        type: array
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price
                              example: "0.00040161"
                            - type: string
                              description: Quantity
                              example: "365980.85000000"
                          items:
                            oneOf:
                              - type: string
                                description: Price
                                example: "0.00040161"
                              - type: string
                                description: Quantity
                                example: "365980.85000000"
                        description: Bid orders. Each entry is [price, quantity].
                        x-description-cn: 买单列表。每项为 [价格, 数量]。
                        example:
                          - - "0.00040161"
                            - "365980.85000000"
                      asks:
                        type: array
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price
                              example: "0.00046996"
                            - type: string
                              description: Quantity
                              example: "61994.70000000"
                          items:
                            oneOf:
                              - type: string
                                description: Price
                                example: "0.00046996"
                              - type: string
                                description: Quantity
                                example: "61994.70000000"
                        description: Ask orders. Each entry is [price, quantity].
                        x-description-cn: 卖单列表。每项为 [价格, 数量]。
                        example:
                          - - "0.00046996"
                            - "61994.70000000"
                      E:
                        type: integer
                        example: 1775027836086
                        format: int64
                        description: Event time in milliseconds.
                        x-description-cn: 事件时间（毫秒）。
                      T:
                        type: integer
                        example: 1775027836072
                        format: int64
                        description: Transaction time in milliseconds.
                        x-description-cn: 交易时间（毫秒）。
                    description: Order book data.
                    x-description-cn: 订单簿数据。
  /bapi/defi/v1/public/alpha-trade/get-exchange-info:
    get:
      summary: Get Exchange Info
      x-summary-cn: 交易对信息
      description: Fetches general exchange information, such as supported symbols, rate limits, and server time.
      x-description-cn: 获取通用的交易所信息，如支持的交易对、限速信息及服务器时间。
      tags:
        - market-data
      operationId: getExchangeInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#get-exchange-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/getExchangeInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/get_exchange_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/get_exchange_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/GetExchangeInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/GetExchangeInfo/GetExchangeInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/GetExchangeInfoExample.php
      parameters: []
      responses:
        "200":
          description: Get Exchange Info
          x-description-cn: 获取交易对信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: ""
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: ""
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful.
                    x-description-cn: 请求是否成功。
                  data:
                    type: object
                    properties:
                      timezone:
                        type: string
                        example: UTC
                        description: Timezone of market data.
                        x-description-cn: 行情数据时区。
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: USDT
                              description: Asset symbol.
                              x-description-cn: 资产符号。
                        description: Supported assets.
                        x-description-cn: 支持的资产列表。
                      symbols:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: ALPHA_105USDT
                              description: Trading symbol.
                              x-description-cn: 交易对。
                            status:
                              type: string
                              example: TRADING
                              description: Trading status.
                              x-description-cn: 交易状态。
                            baseAsset:
                              type: string
                              example: ALPHA_105
                              description: Base asset symbol.
                              x-description-cn: 基础资产符号。
                            quoteAsset:
                              type: string
                              example: USDT
                              description: Quote asset symbol.
                              x-description-cn: 计价资产符号。
                            pricePrecision:
                              type: integer
                              example: 8
                              format: int64
                              description: Allowed precision for price.
                              x-description-cn: 价格精度。
                            quantityPrecision:
                              type: integer
                              example: 8
                              format: int64
                              description: Allowed precision for quantity.
                              x-description-cn: 数量精度。
                            baseAssetPrecision:
                              type: integer
                              example: 8
                              format: int64
                              description: Base asset precision.
                              x-description-cn: 基础资产精度。
                            quotePrecision:
                              type: integer
                              example: 8
                              format: int64
                              description: Quote asset precision.
                              x-description-cn: 计价资产精度。
                            filters:
                              type: array
                              items:
                                type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: PRICE_FILTER
                                    description: Filter type.
                                    x-description-cn: 过滤器类型。
                                  minPrice:
                                    type: string
                                    example: "0.00000001"
                                    description: Minimum price.
                                    x-description-cn: 最小价格。
                                  maxPrice:
                                    type: string
                                    example: "1000"
                                    description: Maximum price.
                                    x-description-cn: 最大价格。
                                  tickSize:
                                    type: string
                                    example: "0.00000001"
                                    description: Tick size.
                                    x-description-cn: 价格步长。
                                  stepSize:
                                    type: string
                                    example: "0.01000000"
                                    description: Step size.
                                    x-description-cn: 数量步长。
                                  maxQty:
                                    type: string
                                    example: "277778"
                                    description: Maximum quantity.
                                    x-description-cn: 最大数量。
                                  minQty:
                                    type: string
                                    example: "0.01000000"
                                    description: Minimum quantity.
                                    x-description-cn: 最小数量。
                                  limit:
                                    type: integer
                                    example: 200
                                    format: int64
                                    description: Maximum allowed orders for this rule.
                                    x-description-cn: 该规则允许的最大订单数。
                                  minNotional:
                                    type: string
                                    example: "0.1"
                                    description: Minimum notional value.
                                    x-description-cn: 最小名义价值。
                                  maxNotional:
                                    type: string
                                    example: "1000000"
                                    description: Maximum notional value.
                                    x-description-cn: 最大名义价值。
                                  multiplierDown:
                                    type: string
                                    example: "0.20000"
                                    description: Lower multiplier bound.
                                    x-description-cn: 下限倍率。
                                  multiplierUp:
                                    type: string
                                    example: "5"
                                    description: Upper multiplier bound.
                                    x-description-cn: 上限倍率。
                                  bidMultiplierUp:
                                    type: string
                                    example: "5"
                                    description: Upper multiplier bound for bids.
                                    x-description-cn: 买单上限倍率。
                                  askMultiplierUp:
                                    type: string
                                    example: "5"
                                    description: Upper multiplier bound for asks.
                                    x-description-cn: 卖单上限倍率。
                                  bidMultiplierDown:
                                    type: string
                                    example: "0.20000"
                                    description: Lower multiplier bound for bids.
                                    x-description-cn: 买单下限倍率。
                                  askMultiplierDown:
                                    type: string
                                    example: "0.20000"
                                    description: Lower multiplier bound for asks.
                                    x-description-cn: 卖单下限倍率。
                              description: Trading filters and constraints.
                              x-description-cn: 交易过滤器与限制。
                            orderTypes:
                              type: array
                              items:
                                type: string
                                example: LIMIT
                              description: Supported order types for this symbol.
                              x-description-cn: 该交易对支持的订单类型。
                        description: Supported trading symbols.
                        x-description-cn: 支持的交易对列表。
                      orderTypes:
                        type: string
                        example: ""
                        description: Order types metadata returned by backend.
                        x-description-cn: 后端返回的订单类型元数据。
                    description: Exchange metadata, including assets and symbols.
                    x-description-cn: 交易所元数据，包含资产和交易对信息。
  /bapi/defi/v1/public/alpha-trade/klines:
    get:
      summary: Klines
      x-summary-cn: K线
      description: >-
        Fetches Kline/candlestick bars for a symbol, which include open/high/low/close prices and volume over intervals.
        Useful for charting and analysis.
      x-description-cn: 获取某一交易对的K线/蜡烛图数据，包含开盘价、最高价、最低价、收盘价及成交量等信息，适用于图表绘制和行情分析。
      tags:
        - market-data
      operationId: klines
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#klines
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/klines.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/klines.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/klines.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/KlinesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/Klines/Klines.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/KlinesExample.php
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: ALPHA_175USDT
          description: Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).
          x-description-cn: 交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。
        - name: interval
          in: query
          required: true
          schema:
            type: string
            example: 1h
            enum:
              - 1s
              - 15s
              - 1m
              - 3m
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 8h
              - 12h
              - 1d
              - 3d
              - 1w
              - 1M
          description: Kline interval.
          x-description-cn: K 线间隔。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 500
            maximum: 1500
          description: Number of klines to return.
          x-description-cn: 返回 K 线数量。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1752642000000
            format: int64
          description: Start timestamp in milliseconds.
          x-description-cn: 起始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1752645599999
            format: int64
          description: End timestamp in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
      responses:
        "200":
          description: Klines
          x-description-cn: K 线
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: ""
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: ""
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful.
                    x-description-cn: 请求是否成功。
                  data:
                    type: array
                    items:
                      type: array
                      items:
                        oneOf:
                          - type: string
                            example: "1752642000000"
                          - type: integer
                            format: int64
                            example: 0
                    description: >-
                      Array of kline rows. Each row contains: open time, open, high, low, close, volume, close time,
                      quote volume, trade count, taker buy base volume, taker buy quote volume, and a static 0.
                    x-description-cn: K 线数组。每一项依次为：开盘时间、开盘价、最高价、最低价、收盘价、成交量、收盘时间、计价成交量、成交笔数、主动买入基础资产量、主动买入计价资产量，以及静态值 0。
  /bapi/defi/v1/public/alpha-trade/ticker:
    get:
      summary: Ticker
      x-summary-cn: 24hr价格变动情况
      description: Gets the 24-hour rolling window price change statistics for a symbol, including volume and price changes.
      x-description-cn: 获取某个交易对过去 24 小时滚动窗口的价格变化统计， 包括成交量和价格变化。
      tags:
        - market-data
      operationId: ticker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/ticker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/TickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/Ticker/Ticker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/TickerExample.php
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: ALPHA_175USDT
          description: Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).
          x-description-cn: 交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。
      responses:
        "200":
          description: Ticker
          x-description-cn: 行情
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: ""
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: ""
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  data:
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: ALPHA_175USDT
                        description: Trading pair symbol.
                        x-description-cn: 交易对符号。
                      priceChange:
                        type: string
                        example: "-0.00007172"
                        description: Absolute price change in the 24h window.
                        x-description-cn: 24 小时窗口内绝对价格变化。
                      priceChangePercent:
                        type: string
                        example: "-8.841"
                        description: Percentage price change in the 24h window.
                        x-description-cn: 24 小时窗口内价格变化百分比。
                      weightedAvgPrice:
                        type: string
                        example: "0.00079608"
                        description: Weighted average price in the 24h window.
                        x-description-cn: 24 小时窗口内加权平均价格。
                      lastPrice:
                        type: string
                        example: "0.00073954"
                        description: Latest traded price.
                        x-description-cn: 最新成交价。
                      lastQty:
                        type: string
                        example: "12600.43000000"
                        description: Quantity of the latest trade.
                        x-description-cn: 最新一笔成交数量。
                      openPrice:
                        type: string
                        example: "0.00081126"
                        description: Opening price of the 24h window.
                        x-description-cn: 24 小时窗口开盘价。
                      highPrice:
                        type: string
                        example: "0.00081126"
                        description: Highest price in the 24h window.
                        x-description-cn: 24 小时窗口最高价。
                      lowPrice:
                        type: string
                        example: "0.00073954"
                        description: Lowest price in the 24h window.
                        x-description-cn: 24 小时窗口最低价。
                      volume:
                        type: string
                        example: "1204754.30000000"
                        description: Base asset volume in the 24h window.
                        x-description-cn: 24 小时窗口基础资产成交量。
                      quoteVolume:
                        type: string
                        example: "959.07729927"
                        description: Quote asset volume in the 24h window.
                        x-description-cn: 24 小时窗口计价资产成交量。
                      openTime:
                        type: integer
                        example: 1768808100000
                        format: int64
                        description: Start time of the 24h window (milliseconds).
                        x-description-cn: 24 小时窗口开始时间（毫秒）。
                      closeTime:
                        type: integer
                        example: 1768893244772
                        format: int64
                        description: End time of the 24h window (milliseconds).
                        x-description-cn: 24 小时窗口结束时间（毫秒）。
                      firstId:
                        type: integer
                        example: 93742
                        format: int64
                        description: First trade ID in the 24h window.
                        x-description-cn: 24 小时窗口内首笔成交 ID。
                      lastId:
                        type: integer
                        example: 93768
                        format: int64
                        description: Last trade ID in the 24h window.
                        x-description-cn: 24 小时窗口内末笔成交 ID。
                      count:
                        type: integer
                        example: 38
                        format: int64
                        description: Total number of trades in the 24h window.
                        x-description-cn: 24 小时窗口内成交总笔数。
                    description: 24-hour rolling window ticker statistics.
                    x-description-cn: 24 小时滚动窗口行情统计。
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful.
                    x-description-cn: 请求是否成功。
  /bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list:
    get:
      summary: Token List
      x-summary-cn: 代币列表
      description: >-
        Retrieves a list of all available ALPHA tokens, including their IDs and symbols. Use this to find the token ID
        for constructing symbols in other endpoints.
      x-description-cn: 获取所有可用ALPHA代币的列表，包括它们的ID和符号。用于在其它接口构造symbol参数时查找代币ID。
      tags:
        - market-data
      operationId: tokenList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/market-data#token-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/rest-api/MarketDataApi/tokenList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/rest_api/market_data_api/token_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/rest_api/MarketData/token_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/rest/marketdata/TokenListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/restapi/MarketDataAPI/TokenList/TokenList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/alpha/marketdata/TokenListExample.php
      parameters: []
      responses:
        "200":
          description: Token List
          x-description-cn: 代币列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: ""
                    description: Response message.
                    x-description-cn: 响应消息。
                  messageDetail:
                    type: string
                    example: ""
                    description: Detailed response message.
                    x-description-cn: 响应详细消息。
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful.
                    x-description-cn: 请求是否成功。
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        tokenId:
                          type: string
                          example: 3F350C8B3621770A673159B7A19BC034
                          description: Unique token identifier.
                          x-description-cn: 代币唯一标识。
                        chainId:
                          type: string
                          example: "56"
                          description: Chain ID.
                          x-description-cn: 链 ID。
                        chainIconUrl:
                          type: string
                          example: >-
                            https://bin.bnbstatic.com/image/admin_mgs_image_upload/20250228/d0216ce4-a3e9-4bda-8937-4a6aa943ccf2.png
                          description: Chain icon URL.
                          x-description-cn: 链图标 URL。
                        chainName:
                          type: string
                          example: BSC
                          description: Chain name.
                          x-description-cn: 链名称。
                        contractAddress:
                          type: string
                          example: "0xcf640fdf9b3d9e45cbd69fda91d7e22579c14444"
                          description: Token contract address.
                          x-description-cn: 代币合约地址。
                        name:
                          type: string
                          example: gorilla
                          description: Token name.
                          x-description-cn: 代币名称。
                        symbol:
                          type: string
                          example: gorilla
                          description: Token symbol.
                          x-description-cn: 代币符号。
                        iconUrl:
                          type: string
                          example: >-
                            https://bin.bnbstatic.com/images/web3-data/public/token/logos/248b5406f88a4ee28913a29107875339.png
                          description: Token icon URL.
                          x-description-cn: 代币图标 URL。
                        price:
                          type: string
                          example: "0.00080595003978242023"
                          description: Latest token price.
                          x-description-cn: 代币最新价格。
                        percentChange24h:
                          type: string
                          example: "-7.42"
                          description: 24-hour price change percentage.
                          x-description-cn: 24 小时价格涨跌幅。
                        volume24h:
                          type: string
                          example: "14847.711222633409558029675"
                          description: 24-hour trading volume.
                          x-description-cn: 24 小时成交量。
                        marketCap:
                          type: string
                          example: "805950.03978242"
                        fdv:
                          type: string
                          example: "805950.03978242"
                        liquidity:
                          type: string
                          example: "263192.72813121626034"
                        totalSupply:
                          type: string
                          example: "1000000000"
                        circulatingSupply:
                          type: string
                          example: "1000000000"
                        holders:
                          type: string
                          example: "7120"
                        decimals:
                          type: integer
                          example: 18
                          format: int64
                        listingCex:
                          type: boolean
                          example: false
                        hotTag:
                          type: boolean
                          example: false
                        cexCoinName:
                          type: string
                          example: ""
                        canTransfer:
                          type: boolean
                          example: false
                        denomination:
                          type: integer
                          example: 1
                          format: int64
                        offline:
                          type: boolean
                          example: false
                        tradeDecimal:
                          type: integer
                          example: 8
                          format: int64
                        alphaId:
                          type: string
                          example: ALPHA_175
                          description: ALPHA token ID, e.g. ALPHA_175.
                          x-description-cn: ALPHA 代币 ID，例如 ALPHA_175。
                        offsell:
                          type: boolean
                          example: false
                        priceHigh24h:
                          type: string
                          example: "0.00088873864475645879"
                        priceLow24h:
                          type: string
                          example: "0.0008020805165487083"
                        count24h:
                          type: string
                          example: "166"
                        onlineTge:
                          type: boolean
                          example: false
                        onlineAirdrop:
                          type: boolean
                          example: false
                        score:
                          type: integer
                          example: 1
                          format: int64
                        cexOffDisplay:
                          type: boolean
                          example: false
                        stockState:
                          type: boolean
                          example: false
                        listingTime:
                          type: integer
                          example: 1746686700000
                          format: int64
                        mulPoint:
                          type: integer
                          example: 1
                          format: int64
                        bnExclusiveState:
                          type: boolean
                          example: false
                    description: List of ALPHA tokens and metadata.
                    x-description-cn: ALPHA 代币及其元数据列表。
```