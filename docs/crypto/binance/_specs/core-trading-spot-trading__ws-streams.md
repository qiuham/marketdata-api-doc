---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:15.040156
---

# core-trading-spot-trading__ws-streams spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Spot WebSocket Market Streams
  description: Access market data, manage accounts, and trade on Binance Spot.
  x-description-cn: 访问市场数据、管理账户，并在 Binance 现货市场交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-streams
x-untagged-label: true
x-user-data-streams: true
externalDocs:
  description: Spot docs
  url: https://developers.binance.com/en/docs/products/spot
servers:
  - url: wss://stream.binance.com:9443
  - url: wss://stream.binance.com:443
  - url: wss://demo-stream.binance.com:9443
  - url: wss://demo-stream.binance.com:443
  - url: wss://stream.testnet.binance.vision
paths:
  /{symbol}@aggTrade:
    post:
      summary: Aggregate Trade Streams
      x-summary-cn: 归集交易
      description: |-
        The Aggregate Trade Streams push trade information that is aggregated
        for a single taker order.
      x-description-cn: 归集交易与逐笔交易的区别在于，同一个taker在同一价格与多个maker成交时，会被归集为一笔成交。
      operationId: aggTrade
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#agg-trade
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/aggTrade.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/agg_trade.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/agg_trade.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/AggTradeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/AggTrade/AggTrade.go
      x-update-speed: Real-time
      x-update-speed-cn: 实时
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@aggTrade
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@aggTrade
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Aggregate Trade Streams
          x-description-cn: 归集交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: aggTrade
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  a:
                    type: integer
                    format: int64
                    example: 12345
                    description: Aggregate trade ID
                    x-description-cn: 归集交易ID
                  p:
                    type: string
                    example: "0.001"
                    description: Price
                    x-description-cn: 成交价格
                  q:
                    type: string
                    example: "100"
                    description: Quantity
                    x-description-cn: 成交数量
                  f:
                    type: integer
                    format: int64
                    example: 100
                    description: First trade ID
                    x-description-cn: 被归集的首个交易ID
                  l:
                    type: integer
                    format: int64
                    example: 105
                    description: Last trade ID
                    x-description-cn: 被归集的末次交易ID
                  T:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Trade time
                    x-description-cn: 成交时间
                  m:
                    type: boolean
                    example: true
                    description: Is the buyer the market maker?
                    x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
                  M:
                    type: boolean
                    example: true
                    description: Ignore
                    x-description-cn: 请忽略该字段
              example:
                e: aggTrade
                E: 1672515782136
                s: BNBBTC
                a: 12345
                p: "0.001"
                q: "100"
                f: 100
                l: 105
                T: 1672515782136
                m: true
                M: true
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@aggTrade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: aggTrade
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      a:
                        type: integer
                        format: int64
                        example: 12345
                        description: Aggregate trade ID
                        x-description-cn: 归集交易ID
                      p:
                        type: string
                        example: "0.001"
                        description: Price
                        x-description-cn: 成交价格
                      q:
                        type: string
                        example: "100"
                        description: Quantity
                        x-description-cn: 成交数量
                      f:
                        type: integer
                        format: int64
                        example: 100
                        description: First trade ID
                        x-description-cn: 被归集的首个交易ID
                      l:
                        type: integer
                        format: int64
                        example: 105
                        description: Last trade ID
                        x-description-cn: 被归集的末次交易ID
                      T:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Trade time
                        x-description-cn: 成交时间
                      m:
                        type: boolean
                        example: true
                        description: Is the buyer the market maker?
                        x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
                      M:
                        type: boolean
                        example: true
                        description: Ignore
                        x-description-cn: 请忽略该字段
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@aggTrade
                data:
                  e: aggTrade
                  E: 1672515782136
                  s: BNBBTC
                  a: 12345
                  p: "0.001"
                  q: "100"
                  f: 100
                  l: 105
                  T: 1672515782136
                  m: true
                  M: true
  /!ticker_{windowSize}@arr:
    post:
      summary: All Market Rolling Window Statistics Streams
      x-summary-cn: 全市场滚动窗口统计
      description: |-
        Rolling window ticker statistics for all market symbols, computed over
        multiple windows.

        Note that only tickers that have changed will be present in the array.
      x-description-cn: |-
        全市场symbols的滚动窗口ticker统计，计算于多个窗口。

        注意：有变动的ticker才会推送。
      operationId: allMarketRollingWindowTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-market-rolling-window-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/allMarketRollingWindowTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/all_market_rolling_window_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/all_market_rolling_window_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/AllMarketRollingWindowTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/AllMarketRollingWindowTicker/AllMarketRollingWindowTicker.go
      x-legacy-anchors:
        - all-market-rolling-window-ticker
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: windowSize
          in: path
          required: true
          schema:
            type: string
            example: 1h
            enum:
              - 1h
              - 4h
              - 1d
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - "!ticker_1h@arr"
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - "!ticker_1h@arr"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: All Market Rolling Window Statistics Streams
          x-description-cn: 全市场滚动窗口统计
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: 1hTicker
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      format: int64
                      example: 1672515782136
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: BNBBTC
                      description: Symbol
                      x-description-cn: 交易对
                    p:
                      type: string
                      example: "0.0015"
                      description: Price change
                      x-description-cn: 价格变化
                    P:
                      type: string
                      example: "250.00"
                      description: Price change percent
                      x-description-cn: 价格变化百分比
                    o:
                      type: string
                      example: "0.0010"
                      description: Open price
                      x-description-cn: 开盘价
                    h:
                      type: string
                      example: "0.0025"
                      description: High price
                      x-description-cn: 最高价
                    l:
                      type: string
                      example: "0.0010"
                      description: Low price
                      x-description-cn: 最低价
                    c:
                      type: string
                      example: "0.0025"
                      description: Last price
                      x-description-cn: 最新价
                    w:
                      type: string
                      example: "0.0018"
                      description: Weighted average price
                      x-description-cn: 加权平均价格
                    v:
                      type: string
                      example: "10000"
                      description: Total traded base asset volume
                      x-description-cn: 总成交基础资产量
                    q:
                      type: string
                      example: "18"
                      description: Total traded quote asset volume
                      x-description-cn: 总成交计价资产量
                    O:
                      type: integer
                      format: int64
                      example: 0
                      description: Statistics open time
                      x-description-cn: 统计开始时间
                    C:
                      type: integer
                      format: int64
                      example: 1675216573749
                      description: Statistics close time
                      x-description-cn: 统计结束时间
                    F:
                      type: integer
                      format: int64
                      example: 0
                      description: First trade ID
                      x-description-cn: 第一笔成交ID
                    L:
                      type: integer
                      format: int64
                      example: 18150
                      description: Last trade Id
                      x-description-cn: 最后一笔成交ID
                    "n":
                      type: integer
                      format: int64
                      example: 18151
                      description: Total number of trades
                      x-description-cn: 总成交笔数
              example:
                - e: 1hTicker
                  E: 1672515782136
                  s: BNBBTC
                  p: "0.0015"
                  P: "250.00"
                  o: "0.0010"
                  h: "0.0025"
                  l: "0.0010"
                  c: "0.0025"
                  w: "0.0018"
                  v: "10000"
                  q: "18"
                  O: 0
                  C: 1675216573749
                  F: 0
                  L: 18150
                  "n": 18151
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!ticker_1h@arr"
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: 1hTicker
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          format: int64
                          example: 1672515782136
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: BNBBTC
                          description: Symbol
                          x-description-cn: 交易对
                        p:
                          type: string
                          example: "0.0015"
                          description: Price change
                          x-description-cn: 价格变化
                        P:
                          type: string
                          example: "250.00"
                          description: Price change percent
                          x-description-cn: 价格变化百分比
                        o:
                          type: string
                          example: "0.0010"
                          description: Open price
                          x-description-cn: 开盘价
                        h:
                          type: string
                          example: "0.0025"
                          description: High price
                          x-description-cn: 最高价
                        l:
                          type: string
                          example: "0.0010"
                          description: Low price
                          x-description-cn: 最低价
                        c:
                          type: string
                          example: "0.0025"
                          description: Last price
                          x-description-cn: 最新价
                        w:
                          type: string
                          example: "0.0018"
                          description: Weighted average price
                          x-description-cn: 加权平均价格
                        v:
                          type: string
                          example: "10000"
                          description: Total traded base asset volume
                          x-description-cn: 总成交基础资产量
                        q:
                          type: string
                          example: "18"
                          description: Total traded quote asset volume
                          x-description-cn: 总成交计价资产量
                        O:
                          type: integer
                          format: int64
                          example: 0
                          description: Statistics open time
                          x-description-cn: 统计开始时间
                        C:
                          type: integer
                          format: int64
                          example: 1675216573749
                          description: Statistics close time
                          x-description-cn: 统计结束时间
                        F:
                          type: integer
                          format: int64
                          example: 0
                          description: First trade ID
                          x-description-cn: 第一笔成交ID
                        L:
                          type: integer
                          format: int64
                          example: 18150
                          description: Last trade Id
                          x-description-cn: 最后一笔成交ID
                        "n":
                          type: integer
                          format: int64
                          example: 18151
                          description: Total number of trades
                          x-description-cn: 总成交笔数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!ticker_1h@arr"
                data:
                  - e: 1hTicker
                    E: 1672515782136
                    s: BNBBTC
                    p: "0.0015"
                    P: "250.00"
                    o: "0.0010"
                    h: "0.0025"
                    l: "0.0010"
                    c: "0.0025"
                    w: "0.0018"
                    v: "10000"
                    q: "18"
                    O: 0
                    C: 1675216573749
                    F: 0
                    L: 18150
                    "n": 18151
  /!miniTicker@arr:
    post:
      summary: All Market Mini Tickers Stream
      x-summary-cn: 全市场所有Symbol的精简Ticker
      description: |-
        24hr rolling window mini-ticker statistics for all symbols that changed
        in an array. These are NOT the statistics of the UTC day, but a 24hr
        rolling window for the previous 24hrs. Note that only tickers that have
        changed will be present in the array.
      x-description-cn: 所有交易对的24小时滚动窗口迷你行情统计，以数组形式推送。这些不是UTC日统计数据，而是过去24小时的滚动窗口。注意，只有发生变化的行情才会出现在数组中。
      operationId: allMiniTicker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/allMiniTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/all_mini_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/all_mini_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/AllMiniTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/AllMiniTicker/AllMiniTicker.go
      x-legacy-anchors:
        - all-markets-mini-ticker
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - "!miniTicker@arr"
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - "!miniTicker@arr"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: All Market Mini Tickers Stream
          x-description-cn: All Market Mini 行情s Stream
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: 24hrMiniTicker
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      format: int64
                      example: 1672515782136
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: BNBBTC
                      description: Symbol
                      x-description-cn: 交易对
                    c:
                      type: string
                      example: "0.0025"
                      description: Close price
                      x-description-cn: 最新成交价格
                    o:
                      type: string
                      example: "0.0010"
                      description: Open price
                      x-description-cn: 24小时前开始第一笔成交价格
                    h:
                      type: string
                      example: "0.0025"
                      description: High price
                      x-description-cn: 24小时内最高成交价
                    l:
                      type: string
                      example: "0.0010"
                      description: Low price
                      x-description-cn: 24小时内最低成交价
                    v:
                      type: string
                      example: "10000"
                      description: Total traded base asset volume
                      x-description-cn: 成交量
                    q:
                      type: string
                      example: "18"
                      description: Total traded quote asset volume
                      x-description-cn: 成交额
              example:
                - e: 24hrMiniTicker
                  E: 1672515782136
                  s: BNBBTC
                  c: "0.0025"
                  o: "0.0010"
                  h: "0.0025"
                  l: "0.0010"
                  v: "10000"
                  q: "18"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!miniTicker@arr"
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: 24hrMiniTicker
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          format: int64
                          example: 1672515782136
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: BNBBTC
                          description: Symbol
                          x-description-cn: 交易对
                        c:
                          type: string
                          example: "0.0025"
                          description: Close price
                          x-description-cn: 最新成交价格
                        o:
                          type: string
                          example: "0.0010"
                          description: Open price
                          x-description-cn: 24小时前开始第一笔成交价格
                        h:
                          type: string
                          example: "0.0025"
                          description: High price
                          x-description-cn: 24小时内最高成交价
                        l:
                          type: string
                          example: "0.0010"
                          description: Low price
                          x-description-cn: 24小时内最低成交价
                        v:
                          type: string
                          example: "10000"
                          description: Total traded base asset volume
                          x-description-cn: 成交量
                        q:
                          type: string
                          example: "18"
                          description: Total traded quote asset volume
                          x-description-cn: 成交额
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!miniTicker@arr"
                data:
                  - e: 24hrMiniTicker
                    E: 1672515782136
                    s: BNBBTC
                    c: "0.0025"
                    o: "0.0010"
                    h: "0.0025"
                    l: "0.0010"
                    v: "10000"
                    q: "18"
  /{symbol}@avgPrice:
    post:
      summary: Average Price
      x-summary-cn: 平均价格
      description: Average price streams push changes in the average price over a fixed time interval.
      x-description-cn: 平均价格流推送在固定时间间隔内的平均价格变动。
      operationId: avgPrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#avg-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/avgPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/avg_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/avg_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/AvgPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/AvgPrice/AvgPrice.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@avgPrice
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@avgPrice
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Average Price
          x-description-cn: 平均价格
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: avgPrice
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1693907033000
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTCUSDT
                    description: Symbol
                    x-description-cn: 交易对
                  i:
                    type: string
                    example: 5m
                    description: Average price interval
                    x-description-cn: 平均价格间隔
                  w:
                    type: string
                    example: "25776.86000000"
                    description: Average price
                    x-description-cn: 平均价格
                  T:
                    type: integer
                    format: int64
                    example: 1693907032213
                    description: Last trade time
                    x-description-cn: 最后成交时间
              example:
                e: avgPrice
                E: 1693907033000
                s: BTCUSDT
                i: 5m
                w: "25776.86000000"
                T: 1693907032213
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@avgPrice
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: avgPrice
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1693907033000
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTCUSDT
                        description: Symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 5m
                        description: Average price interval
                        x-description-cn: 平均价格间隔
                      w:
                        type: string
                        example: "25776.86000000"
                        description: Average price
                        x-description-cn: 平均价格
                      T:
                        type: integer
                        format: int64
                        example: 1693907032213
                        description: Last trade time
                        x-description-cn: 最后成交时间
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@avgPrice
                data:
                  e: avgPrice
                  E: 1693907033000
                  s: BTCUSDT
                  i: 5m
                  w: "25776.86000000"
                  T: 1693907032213
  /{symbol}@bookTicker:
    post:
      summary: Individual Symbol Book Ticker Streams
      x-summary-cn: 按Symbol的最优挂单信息
      description: |-
        Pushes any update to the best bid or ask's price or quantity in
        real-time for a specified symbol.

        Multiple `<symbol>@bookTicker` streams can be subscribed to over one
        connection.
      x-description-cn: |-
        实时推送指定交易对最优挂单信息
        多个 `<symbol>@bookTicker` 可以订阅在一个WebSocket连接上
      operationId: bookTicker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#book-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/bookTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/book_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/book_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/BookTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/BookTicker/BookTicker.go
      x-update-speed: Real-time
      x-update-speed-cn: 实时
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@bookTicker
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@bookTicker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Book Ticker Streams
          x-description-cn: 按Symbol的最优挂单信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  u:
                    type: integer
                    format: int64
                    example: 400900217
                    description: Order book updateId
                    x-description-cn: order book updateId
                  s:
                    type: string
                    example: BNBUSDT
                    description: Symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "25.35190000"
                    description: Best bid price
                    x-description-cn: 买单最优挂单价格
                  B:
                    type: string
                    example: "31.21000000"
                    description: Best bid qty
                    x-description-cn: 买单最优挂单数量
                  a:
                    type: string
                    example: "25.36520000"
                    description: Best ask price
                    x-description-cn: 卖单最优挂单价格
                  A:
                    type: string
                    example: "40.66000000"
                    description: Best ask qty
                    x-description-cn: 卖单最优挂单数量
              example:
                u: 400900217
                s: BNBUSDT
                b: "25.35190000"
                B: "31.21000000"
                a: "25.36520000"
                A: "40.66000000"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@bookTicker
                  data:
                    type: object
                    properties:
                      u:
                        type: integer
                        format: int64
                        example: 400900217
                        description: Order book updateId
                        x-description-cn: order book updateId
                      s:
                        type: string
                        example: BNBUSDT
                        description: Symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "25.35190000"
                        description: Best bid price
                        x-description-cn: 买单最优挂单价格
                      B:
                        type: string
                        example: "31.21000000"
                        description: Best bid qty
                        x-description-cn: 买单最优挂单数量
                      a:
                        type: string
                        example: "25.36520000"
                        description: Best ask price
                        x-description-cn: 卖单最优挂单价格
                      A:
                        type: string
                        example: "40.66000000"
                        description: Best ask qty
                        x-description-cn: 卖单最优挂单数量
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@bookTicker
                data:
                  u: 400900217
                  s: BNBUSDT
                  b: "25.35190000"
                  B: "31.21000000"
                  a: "25.36520000"
                  A: "40.66000000"
  /{symbol}@depth@{updateSpeed}:
    post:
      summary: Diff. Depth Stream
      x-summary-cn: 增量深度信息stream
      description: Order book price and quantity depth updates used to locally manage an order book.
      x-description-cn: 每秒推送orderbook的变化部分（如果有）
      operationId: diffBookDepth
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#diff-book-depth
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/diffBookDepth.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/diff_book_depth.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/diff_book_depth.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/DiffBookDepthExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/DiffBookDepth/DiffBookDepth.go
      x-legacy-anchors:
        - diff-depth
      x-update-speed: 1000ms or 100ms
      x-update-speed-cn: 1000ms 或者 100ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
          description: Optional stream update speed suffix
          x-description-cn: 可选的推送速度后缀
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@depth@100ms
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@depth@100ms
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Diff. Depth Stream
          x-description-cn: 增量深度信息stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  U:
                    type: integer
                    format: int64
                    example: 157
                    description: First update ID in event
                    x-description-cn: 从上次推送至今新增的第一个 update Id
                  u:
                    type: integer
                    format: int64
                    example: 160
                    description: Final update ID in event
                    x-description-cn: 从上次推送至今新增的最后一个 update Id
                  b:
                    type: array
                    description: Bids to be updated
                    x-description-cn: 变动的买单深度
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          x-description-cn: 价
                          example: "0.0024"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "10"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            x-description-cn: 价
                            example: "0.0024"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "10"
                  a:
                    type: array
                    description: Asks to be updated
                    x-description-cn: 变动的卖单深度
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          x-description-cn: 价
                          example: "0.0026"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "100"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            x-description-cn: 价
                            example: "0.0026"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "100"
              example:
                e: depthUpdate
                E: 1672515782136
                s: BNBBTC
                U: 157
                u: 160
                b:
                  - - "0.0024"
                    - "10"
                a:
                  - - "0.0026"
                    - "100"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@depth@100ms
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: depthUpdate
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      U:
                        type: integer
                        format: int64
                        example: 157
                        description: First update ID in event
                        x-description-cn: 从上次推送至今新增的第一个 update Id
                      u:
                        type: integer
                        format: int64
                        example: 160
                        description: Final update ID in event
                        x-description-cn: 从上次推送至今新增的最后一个 update Id
                      b:
                        type: array
                        description: Bids to be updated
                        x-description-cn: 变动的买单深度
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              x-description-cn: 价
                              example: "0.0024"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "10"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                x-description-cn: 价
                                example: "0.0024"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "10"
                      a:
                        type: array
                        description: Asks to be updated
                        x-description-cn: 变动的卖单深度
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              x-description-cn: 价
                              example: "0.0026"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "100"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                x-description-cn: 价
                                example: "0.0026"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "100"
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@depth@100ms
                data:
                  e: depthUpdate
                  E: 1672515782136
                  s: BNBBTC
                  U: 157
                  u: 160
                  b:
                    - - "0.0024"
                      - "10"
                  a:
                    - - "0.0026"
                      - "100"
  /{symbol}@kline_{interval}:
    post:
      summary: Kline/Candlestick Streams for UTC
      x-summary-cn: UTC K线
      description: |-
        The Kline/Candlestick Stream push updates to the current
        klines/candlestick every second in `UTC+0` timezone
      x-description-cn: K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+0` 时区的。
      operationId: kline
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#kline
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/kline.ts
        rust: https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/kline.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/kline.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/KlineExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/Kline/Kline.go
      x-update-speed: 1000ms for `1s`, 2000ms for the other intervals
      x-update-speed-cn: "`1s` 1000ms，其它间隔 2000ms"
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 1s
            enum:
              - 1s
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@kline_1s
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@kline_1s
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Kline/Candlestick Streams for UTC
          x-description-cn: UTC K线
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: kline
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  k:
                    type: object
                    description: Kline payload
                    x-description-cn: K线数据
                    properties:
                      t:
                        type: integer
                        format: int64
                        example: 1672515780000
                        description: Kline start time
                        x-description-cn: 该K线的起始时间
                      T:
                        type: integer
                        format: int64
                        example: 1672515839999
                        description: Kline close time
                        x-description-cn: 该K线的结束时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: Interval
                        x-description-cn: K线间隔
                      f:
                        type: integer
                        format: int64
                        example: 100
                        description: First trade ID
                        x-description-cn: 该K线期间第一笔成交ID
                      L:
                        type: integer
                        format: int64
                        example: 200
                        description: Last trade ID
                        x-description-cn: 该K线期间末一笔成交ID
                      o:
                        type: string
                        example: "0.0010"
                        description: Open price
                        x-description-cn: 该K线期间第一笔成交价
                      c:
                        type: string
                        example: "0.0020"
                        description: Close price
                        x-description-cn: 该K线期间末一笔成交价
                      h:
                        type: string
                        example: "0.0025"
                        description: High price
                        x-description-cn: 该K线期间最高成交价
                      l:
                        type: string
                        example: "0.0015"
                        description: Low price
                        x-description-cn: 该K线期间最低成交价
                      v:
                        type: string
                        example: "1000"
                        description: Base asset volume
                        x-description-cn: 该K线期间成交量
                      "n":
                        type: integer
                        format: int64
                        example: 100
                        description: Number of trades
                        x-description-cn: 该K线期间成交数量
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 该K线是否完结（是否已经开始下一根K线）
                      q:
                        type: string
                        example: "1.0000"
                        description: Quote asset volume
                        x-description-cn: 该K线期间成交额
                      V:
                        type: string
                        example: "500"
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入的成交量
                      Q:
                        type: string
                        example: "0.500"
                        description: Taker buy quote asset volume
                        x-description-cn: 主动买入的成交额
                      B:
                        type: string
                        example: "123456"
                        description: Ignore
                        x-description-cn: 忽略此参数
              example:
                e: kline
                E: 1672515782136
                s: BNBBTC
                k:
                  t: 1672515780000
                  T: 1672515839999
                  s: BNBBTC
                  i: 1m
                  f: 100
                  L: 200
                  o: "0.0010"
                  c: "0.0020"
                  h: "0.0025"
                  l: "0.0015"
                  v: "1000"
                  "n": 100
                  x: false
                  q: "1.0000"
                  V: "500"
                  Q: "0.500"
                  B: "123456"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@kline_1s
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: kline
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      k:
                        type: object
                        description: Kline payload
                        x-description-cn: K线数据
                        properties:
                          t:
                            type: integer
                            format: int64
                            example: 1672515780000
                            description: Kline start time
                            x-description-cn: 该K线的起始时间
                          T:
                            type: integer
                            format: int64
                            example: 1672515839999
                            description: Kline close time
                            x-description-cn: 该K线的结束时间
                          s:
                            type: string
                            example: BNBBTC
                            description: Symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: Interval
                            x-description-cn: K线间隔
                          f:
                            type: integer
                            format: int64
                            example: 100
                            description: First trade ID
                            x-description-cn: 该K线期间第一笔成交ID
                          L:
                            type: integer
                            format: int64
                            example: 200
                            description: Last trade ID
                            x-description-cn: 该K线期间末一笔成交ID
                          o:
                            type: string
                            example: "0.0010"
                            description: Open price
                            x-description-cn: 该K线期间第一笔成交价
                          c:
                            type: string
                            example: "0.0020"
                            description: Close price
                            x-description-cn: 该K线期间末一笔成交价
                          h:
                            type: string
                            example: "0.0025"
                            description: High price
                            x-description-cn: 该K线期间最高成交价
                          l:
                            type: string
                            example: "0.0015"
                            description: Low price
                            x-description-cn: 该K线期间最低成交价
                          v:
                            type: string
                            example: "1000"
                            description: Base asset volume
                            x-description-cn: 该K线期间成交量
                          "n":
                            type: integer
                            format: int64
                            example: 100
                            description: Number of trades
                            x-description-cn: 该K线期间成交数量
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 该K线是否完结（是否已经开始下一根K线）
                          q:
                            type: string
                            example: "1.0000"
                            description: Quote asset volume
                            x-description-cn: 该K线期间成交额
                          V:
                            type: string
                            example: "500"
                            description: Taker buy base asset volume
                            x-description-cn: 主动买入的成交量
                          Q:
                            type: string
                            example: "0.500"
                            description: Taker buy quote asset volume
                            x-description-cn: 主动买入的成交额
                          B:
                            type: string
                            example: "123456"
                            description: Ignore
                            x-description-cn: 忽略此参数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@kline_1s
                data:
                  e: kline
                  E: 1672515782136
                  s: BNBBTC
                  k:
                    t: 1672515780000
                    T: 1672515839999
                    s: BNBBTC
                    i: 1m
                    f: 100
                    L: 200
                    o: "0.0010"
                    c: "0.0020"
                    h: "0.0025"
                    l: "0.0015"
                    v: "1000"
                    "n": 100
                    x: false
                    q: "1.0000"
                    V: "500"
                    Q: "0.500"
                    B: "123456"
  /{symbol}@kline_{interval}@+08:00:
    post:
      summary: Kline/Candlestick Streams with timezone offset
      x-summary-cn: 带有时区偏移量的K线
      description: >-
        The Kline/Candlestick Stream push updates to the current

        klines/candlestick every second in `UTC+8` timezone


        **Kline/Candlestick chart intervals:**


        Supported intervals: See Kline/Candlestick chart intervals


        **UTC+8 timezone offset:**


        - Kline intervals open and close in the `UTC+8` timezone. For example the `1d` klines will open at the beginning
        of the `UTC+8` day, and close at the end of the `UTC+8` day.

        - Note that `E` (event time), `t` (start time) and `T` (close time) in the payload are Unix timestamps, which
        are always interpreted in UTC.
      x-description-cn: |-
        K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+8` 时区的。

        **订阅Kline需要提供的间隔参数:**

        参考 `Kline所支持的间隔参数`

        **UTC+8 时区偏移量：**

        - K线间隔的开始和结束时间会基于 `UTC+8` 时区。例如， `1d` K线将在 `UTC+8` 当天开始，并在 `UTC+8` 当日完结时随之结束。
        - 请注意，Payload中的 `E`（event time），`t`（start time）和 `T`（close time）是 Unix 时间戳，它们始终以 UTC 格式解释。
      operationId: klineOffset
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#kline-offset
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/klineOffset.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/kline_offset.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/kline_offset.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/KlineOffsetExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/KlineOffset/KlineOffset.go
      x-update-speed: 1000ms for `1s`, 2000ms for the other intervals
      x-update-speed-cn: "`1s` 1000ms，其它间隔 2000ms"
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 1s
            enum:
              - 1s
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@kline_1s@+08:00
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@kline_1s@+08:00
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Kline/Candlestick Streams with timezone offset
          x-description-cn: 带有时区偏移量的K线
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: kline
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  k:
                    type: object
                    description: Kline payload
                    x-description-cn: K线数据
                    properties:
                      t:
                        type: integer
                        format: int64
                        example: 1672515780000
                        description: Kline start time
                        x-description-cn: 该K线的起始时间
                      T:
                        type: integer
                        format: int64
                        example: 1672515839999
                        description: Kline close time
                        x-description-cn: 该K线的结束时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: Interval
                        x-description-cn: K线间隔
                      f:
                        type: integer
                        format: int64
                        example: 100
                        description: First trade ID
                        x-description-cn: 该K线期间第一笔成交ID
                      L:
                        type: integer
                        format: int64
                        example: 200
                        description: Last trade ID
                        x-description-cn: 该K线期间末一笔成交ID
                      o:
                        type: string
                        example: "0.0010"
                        description: Open price
                        x-description-cn: 该K线期间第一笔成交价
                      c:
                        type: string
                        example: "0.0020"
                        description: Close price
                        x-description-cn: 该K线期间末一笔成交价
                      h:
                        type: string
                        example: "0.0025"
                        description: High price
                        x-description-cn: 该K线期间最高成交价
                      l:
                        type: string
                        example: "0.0015"
                        description: Low price
                        x-description-cn: 该K线期间最低成交价
                      v:
                        type: string
                        example: "1000"
                        description: Base asset volume
                        x-description-cn: 该K线期间成交量
                      "n":
                        type: integer
                        format: int64
                        example: 100
                        description: Number of trades
                        x-description-cn: 该K线期间成交数量
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 该K线是否完结（是否已经开始下一根K线）
                      q:
                        type: string
                        example: "1.0000"
                        description: Quote asset volume
                        x-description-cn: 该K线期间成交额
                      V:
                        type: string
                        example: "500"
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入的成交量
                      Q:
                        type: string
                        example: "0.500"
                        description: Taker buy quote asset volume
                        x-description-cn: 主动买入的成交额
                      B:
                        type: string
                        example: "123456"
                        description: Ignore
                        x-description-cn: 忽略此参数
              example:
                e: kline
                E: 1672515782136
                s: BNBBTC
                k:
                  t: 1672515780000
                  T: 1672515839999
                  s: BNBBTC
                  i: 1m
                  f: 100
                  L: 200
                  o: "0.0010"
                  c: "0.0020"
                  h: "0.0025"
                  l: "0.0015"
                  v: "1000"
                  "n": 100
                  x: false
                  q: "1.0000"
                  V: "500"
                  Q: "0.500"
                  B: "123456"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@kline_1s@+08:00
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: kline
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      k:
                        type: object
                        description: Kline payload
                        x-description-cn: K线数据
                        properties:
                          t:
                            type: integer
                            format: int64
                            example: 1672515780000
                            description: Kline start time
                            x-description-cn: 该K线的起始时间
                          T:
                            type: integer
                            format: int64
                            example: 1672515839999
                            description: Kline close time
                            x-description-cn: 该K线的结束时间
                          s:
                            type: string
                            example: BNBBTC
                            description: Symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: Interval
                            x-description-cn: K线间隔
                          f:
                            type: integer
                            format: int64
                            example: 100
                            description: First trade ID
                            x-description-cn: 该K线期间第一笔成交ID
                          L:
                            type: integer
                            format: int64
                            example: 200
                            description: Last trade ID
                            x-description-cn: 该K线期间末一笔成交ID
                          o:
                            type: string
                            example: "0.0010"
                            description: Open price
                            x-description-cn: 该K线期间第一笔成交价
                          c:
                            type: string
                            example: "0.0020"
                            description: Close price
                            x-description-cn: 该K线期间末一笔成交价
                          h:
                            type: string
                            example: "0.0025"
                            description: High price
                            x-description-cn: 该K线期间最高成交价
                          l:
                            type: string
                            example: "0.0015"
                            description: Low price
                            x-description-cn: 该K线期间最低成交价
                          v:
                            type: string
                            example: "1000"
                            description: Base asset volume
                            x-description-cn: 该K线期间成交量
                          "n":
                            type: integer
                            format: int64
                            example: 100
                            description: Number of trades
                            x-description-cn: 该K线期间成交数量
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 该K线是否完结（是否已经开始下一根K线）
                          q:
                            type: string
                            example: "1.0000"
                            description: Quote asset volume
                            x-description-cn: 该K线期间成交额
                          V:
                            type: string
                            example: "500"
                            description: Taker buy base asset volume
                            x-description-cn: 主动买入的成交量
                          Q:
                            type: string
                            example: "0.500"
                            description: Taker buy quote asset volume
                            x-description-cn: 主动买入的成交额
                          B:
                            type: string
                            example: "123456"
                            description: Ignore
                            x-description-cn: 忽略此参数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@kline_1s@+08:00
                data:
                  e: kline
                  E: 1672515782136
                  s: BNBBTC
                  k:
                    t: 1672515780000
                    T: 1672515839999
                    s: BNBBTC
                    i: 1m
                    f: 100
                    L: 200
                    o: "0.0010"
                    c: "0.0020"
                    h: "0.0025"
                    l: "0.0015"
                    v: "1000"
                    "n": 100
                    x: false
                    q: "1.0000"
                    V: "500"
                    Q: "0.500"
                    B: "123456"
  /{symbol}@miniTicker:
    post:
      summary: Individual Symbol Mini Ticker Stream
      x-summary-cn: 按Symbol的精简Ticker
      description: |-
        24hr rolling window mini-ticker statistics. These are NOT the statistics
        of the UTC day, but a 24hr rolling window for the previous 24hrs.
      x-description-cn: 按Symbol逐秒刷新的24小时精简ticker信息
      operationId: miniTicker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#mini-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/miniTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/mini_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/mini_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/MiniTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/MiniTicker/MiniTicker.go
      x-legacy-anchors:
        - twentyfourhourminiticker
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@miniTicker
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@miniTicker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Mini Ticker Stream
          x-description-cn: 按Symbol的精简Ticker
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrMiniTicker
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  c:
                    type: string
                    example: "0.0025"
                    description: Close price
                    x-description-cn: 最新成交价格
                  o:
                    type: string
                    example: "0.0010"
                    description: Open price
                    x-description-cn: 24小时前开始第一笔成交价格
                  h:
                    type: string
                    example: "0.0025"
                    description: High price
                    x-description-cn: 24小时内最高成交价
                  l:
                    type: string
                    example: "0.0010"
                    description: Low price
                    x-description-cn: 24小时内最低成交价
                  v:
                    type: string
                    example: "10000"
                    description: Total traded base asset volume
                    x-description-cn: 成交量
                  q:
                    type: string
                    example: "18"
                    description: Total traded quote asset volume
                    x-description-cn: 成交额
              example:
                e: 24hrMiniTicker
                E: 1672515782136
                s: BNBBTC
                c: "0.0025"
                o: "0.0010"
                h: "0.0025"
                l: "0.0010"
                v: "10000"
                q: "18"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@miniTicker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrMiniTicker
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      c:
                        type: string
                        example: "0.0025"
                        description: Close price
                        x-description-cn: 最新成交价格
                      o:
                        type: string
                        example: "0.0010"
                        description: Open price
                        x-description-cn: 24小时前开始第一笔成交价格
                      h:
                        type: string
                        example: "0.0025"
                        description: High price
                        x-description-cn: 24小时内最高成交价
                      l:
                        type: string
                        example: "0.0010"
                        description: Low price
                        x-description-cn: 24小时内最低成交价
                      v:
                        type: string
                        example: "10000"
                        description: Total traded base asset volume
                        x-description-cn: 成交量
                      q:
                        type: string
                        example: "18"
                        description: Total traded quote asset volume
                        x-description-cn: 成交额
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@miniTicker
                data:
                  e: 24hrMiniTicker
                  E: 1672515782136
                  s: BNBBTC
                  c: "0.0025"
                  o: "0.0010"
                  h: "0.0025"
                  l: "0.0010"
                  v: "10000"
                  q: "18"
  /{symbol}@depth{levels}@{updateSpeed}:
    post:
      summary: Partial Book Depth Streams
      x-summary-cn: 有限档深度信息
      description: Top **\<levels\>** bids and asks, pushed every second. Valid **\<levels\>** are 5, 10, or 20.
      x-description-cn: 每秒推送有限档深度信息。levels 表示几档买卖单信息, 可选 5/10/20档
      operationId: partialBookDepth
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#partial-book-depth
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/partialBookDepth.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/partial_book_depth.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/partial_book_depth.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/PartialBookDepthExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/PartialBookDepth/PartialBookDepth.go
      x-legacy-anchors:
        - depth
      x-update-speed: 1000ms or 100ms
      x-update-speed-cn: 1000ms 或者 100ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
        - name: levels
          in: path
          required: true
          schema:
            type: string
            example: 5
            enum:
              - 5
              - 10
              - 20
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
          description: Optional stream update speed suffix
          x-description-cn: 可选的推送速度后缀
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@depth5@100ms
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@depth5@100ms
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Partial Book Depth Streams
          x-description-cn: 有限档深度信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  lastUpdateId:
                    type: integer
                    format: int64
                    example: 160
                    description: Last update ID
                    x-description-cn: 末次更新ID
                  bids:
                    type: array
                    description: Bids to be updated
                    x-description-cn: 买单
                    example:
                      - - "0.0024"
                        - "10"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          x-description-cn: 价
                          example: "0.0024"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "10"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            x-description-cn: 价
                            example: "0.0024"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "10"
                  asks:
                    type: array
                    description: Asks to be updated
                    x-description-cn: 卖单
                    example:
                      - - "0.0026"
                        - "100"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          x-description-cn: 价
                          example: "0.0026"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "100"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            x-description-cn: 价
                            example: "0.0026"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "100"
              example:
                lastUpdateId: 160
                bids:
                  - - "0.0024"
                    - "10"
                asks:
                  - - "0.0026"
                    - "100"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@depth5@100ms
                  data:
                    type: object
                    properties:
                      lastUpdateId:
                        type: integer
                        format: int64
                        example: 160
                        description: Last update ID
                        x-description-cn: 末次更新ID
                      bids:
                        type: array
                        description: Bids to be updated
                        x-description-cn: 买单
                        example:
                          - - "0.0024"
                            - "10"
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              x-description-cn: 价
                              example: "0.0024"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "10"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                x-description-cn: 价
                                example: "0.0024"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "10"
                      asks:
                        type: array
                        description: Asks to be updated
                        x-description-cn: 卖单
                        example:
                          - - "0.0026"
                            - "100"
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              x-description-cn: 价
                              example: "0.0026"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "100"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                x-description-cn: 价
                                example: "0.0026"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "100"
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@depth5@100ms
                data:
                  lastUpdateId: 160
                  bids:
                    - - "0.0024"
                      - "10"
                  asks:
                    - - "0.0026"
                      - "100"
  /{symbol}@referencePrice:
    post:
      summary: Reference Price Streams
      x-summary-cn: 参考价格数据流
      description: Reference price stream for a symbol.
      x-description-cn: 推送交易对参考价格信息。
      operationId: referencePrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#reference-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/referencePrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/reference_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/reference_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/ReferencePriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/ReferencePrice/ReferencePrice.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bazusd
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bazusd@referencePrice
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bazusd@referencePrice
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Reference Price Streams
          x-description-cn: 参考价格数据流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: referencePrice
                    description: Event type
                    x-description-cn: 事件类型
                  s:
                    type: string
                    example: BAZUSD
                    description: Symbol
                    x-description-cn: 交易对
                  r:
                    type: string
                    example: "1.00"
                    description: Reference price (null if no reference price)
                    x-description-cn: 参考价格（如果无参考价格则为 null）
                  t:
                    type: integer
                    format: int64
                    example: 1770313263917
                    description: Engine timestamp when reference price was valid
                    x-description-cn: 参考价格生效时的撮合引擎时间
              example:
                e: referencePrice
                s: BAZUSD
                r: "1.00"
                t: 1770313263917
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bazusd@referencePrice
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: referencePrice
                        description: Event type
                        x-description-cn: 事件类型
                      s:
                        type: string
                        example: BAZUSD
                        description: Symbol
                        x-description-cn: 交易对
                      r:
                        type: string
                        example: "1.00"
                        description: Reference price (null if no reference price)
                        x-description-cn: 参考价格（如果无参考价格则为 null）
                      t:
                        type: integer
                        format: int64
                        example: 1770313263917
                        description: Engine timestamp when reference price was valid
                        x-description-cn: 参考价格生效时的撮合引擎时间
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bazusd@referencePrice
                data:
                  e: referencePrice
                  s: BAZUSD
                  r: "1.00"
                  t: 1770313263917
  /{symbol}@ticker_{windowSize}:
    post:
      summary: Individual Symbol Rolling Window Statistics Streams
      x-summary-cn: 按Symbol的滚动窗口统计
      description: >-
        Rolling window ticker statistics for a single symbol, computed over

        multiple windows.


        **Note:** This stream is different from the `<symbol>@ticker` stream. The open time `"O"` always starts on a
        minute, while the closing time `"C"` is the current time

        of the update. As such, the effective window might be up to 59999ms wider than `<windowSize>`.
      x-description-cn: |-
        单个symbol的滚动窗口统计, 支持多个时间窗口。

        **注意:**

        - 该数据流和 `<symbol>@ticker` 不一样。
        - `O` (`open time`) 会在每分钟整点开始, 而 `C` (`closing time`)是当前更新时间。
        - 实际统计的时间范围会比 `<windowSize>` 多不超过59999ms。
      operationId: rollingWindowTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#rolling-window-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/rollingWindowTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/rolling_window_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/rolling_window_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/RollingWindowTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/RollingWindowTicker/RollingWindowTicker.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
        - name: windowSize
          in: path
          required: true
          schema:
            type: string
            example: 1h
            enum:
              - 1h
              - 4h
              - 1d
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@ticker_1h
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@ticker_1h
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Rolling Window Statistics Streams
          x-description-cn: 按Symbol的滚动窗口统计
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 1hTicker
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "0.0015"
                    description: Price change
                    x-description-cn: 价格变化
                  P:
                    type: string
                    example: "250.00"
                    description: Price change percent
                    x-description-cn: 价格变化百分比
                  o:
                    type: string
                    example: "0.0010"
                    description: Open price
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "0.0025"
                    description: High price
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "0.0010"
                    description: Low price
                    x-description-cn: 最低价
                  c:
                    type: string
                    example: "0.0025"
                    description: Last price
                    x-description-cn: 最新价
                  w:
                    type: string
                    example: "0.0018"
                    description: Weighted average price
                    x-description-cn: 加权平均价格
                  v:
                    type: string
                    example: "10000"
                    description: Total traded base asset volume
                    x-description-cn: 总成交基础资产量
                  q:
                    type: string
                    example: "18"
                    description: Total traded quote asset volume
                    x-description-cn: 总成交计价资产量
                  O:
                    type: integer
                    format: int64
                    example: 0
                    description: Statistics open time
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    format: int64
                    example: 1675216573749
                    description: Statistics close time
                    x-description-cn: 统计结束时间
                  F:
                    type: integer
                    format: int64
                    example: 0
                    description: First trade ID
                    x-description-cn: 第一笔成交ID
                  L:
                    type: integer
                    format: int64
                    example: 18150
                    description: Last trade Id
                    x-description-cn: 最后一笔成交ID
                  "n":
                    type: integer
                    format: int64
                    example: 18151
                    description: Total number of trades
                    x-description-cn: 总成交笔数
              example:
                e: 1hTicker
                E: 1672515782136
                s: BNBBTC
                p: "0.0015"
                P: "250.00"
                o: "0.0010"
                h: "0.0025"
                l: "0.0010"
                c: "0.0025"
                w: "0.0018"
                v: "10000"
                q: "18"
                O: 0
                C: 1675216573749
                F: 0
                L: 18150
                "n": 18151
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@ticker_1h
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 1hTicker
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "0.0015"
                        description: Price change
                        x-description-cn: 价格变化
                      P:
                        type: string
                        example: "250.00"
                        description: Price change percent
                        x-description-cn: 价格变化百分比
                      o:
                        type: string
                        example: "0.0010"
                        description: Open price
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "0.0025"
                        description: High price
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "0.0010"
                        description: Low price
                        x-description-cn: 最低价
                      c:
                        type: string
                        example: "0.0025"
                        description: Last price
                        x-description-cn: 最新价
                      w:
                        type: string
                        example: "0.0018"
                        description: Weighted average price
                        x-description-cn: 加权平均价格
                      v:
                        type: string
                        example: "10000"
                        description: Total traded base asset volume
                        x-description-cn: 总成交基础资产量
                      q:
                        type: string
                        example: "18"
                        description: Total traded quote asset volume
                        x-description-cn: 总成交计价资产量
                      O:
                        type: integer
                        format: int64
                        example: 0
                        description: Statistics open time
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        format: int64
                        example: 1675216573749
                        description: Statistics close time
                        x-description-cn: 统计结束时间
                      F:
                        type: integer
                        format: int64
                        example: 0
                        description: First trade ID
                        x-description-cn: 第一笔成交ID
                      L:
                        type: integer
                        format: int64
                        example: 18150
                        description: Last trade Id
                        x-description-cn: 最后一笔成交ID
                      "n":
                        type: integer
                        format: int64
                        example: 18151
                        description: Total number of trades
                        x-description-cn: 总成交笔数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@ticker_1h
                data:
                  e: 1hTicker
                  E: 1672515782136
                  s: BNBBTC
                  p: "0.0015"
                  P: "250.00"
                  o: "0.0010"
                  h: "0.0025"
                  l: "0.0010"
                  c: "0.0025"
                  w: "0.0018"
                  v: "10000"
                  q: "18"
                  O: 0
                  C: 1675216573749
                  F: 0
                  L: 18150
                  "n": 18151
  /{symbol}@ticker:
    post:
      summary: Individual Symbol Ticker Streams
      x-summary-cn: 按Symbol的完整Ticker
      description: |-
        24hr rolling window ticker statistics for a single symbol. These are NOT
        the statistics of the UTC day, but a 24hr rolling window for the
        previous 24hrs.
      x-description-cn: 按Symbol逐秒刷新的24小时完整ticker信息
      operationId: ticker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/ticker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/TickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/Ticker/Ticker.go
      x-legacy-anchors:
        - twentyfourhourticker
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@ticker
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@ticker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Ticker Streams
          x-description-cn: 按Symbol的完整Ticker
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrTicker
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "0.0015"
                    description: Price change
                    x-description-cn: 24小时价格变化
                  P:
                    type: string
                    example: "250.00"
                    description: Price change percent
                    x-description-cn: 24小时价格变化（百分比）
                  w:
                    type: string
                    example: "0.0018"
                    description: Weighted average price
                    x-description-cn: 平均价格
                  x:
                    type: string
                    example: "0.0009"
                    description: First trade(F)-1 price (first trade before the 24hr rolling window)
                    x-description-cn: 整整24小时之前，向前数的最后一次成交价格
                  c:
                    type: string
                    example: "0.0025"
                    description: Last price
                    x-description-cn: 最新成交价格
                  Q:
                    type: string
                    example: "10"
                    description: Last quantity
                    x-description-cn: 最新成交交易的成交量
                  b:
                    type: string
                    example: "0.0024"
                    description: Best bid price
                    x-description-cn: 目前最高买单价
                  B:
                    type: string
                    example: "10"
                    description: Best bid quantity
                    x-description-cn: 目前最高买单价的挂单量
                  a:
                    type: string
                    example: "0.0026"
                    description: Best ask price
                    x-description-cn: 目前最低卖单价
                  A:
                    type: string
                    example: "100"
                    description: Best ask quantity
                    x-description-cn: 目前最低卖单价的挂单量
                  o:
                    type: string
                    example: "0.0010"
                    description: Open price
                    x-description-cn: 整整24小时前，向后数的第一次成交价格
                  h:
                    type: string
                    example: "0.0025"
                    description: High price
                    x-description-cn: 24小时内最高成交价
                  l:
                    type: string
                    example: "0.0010"
                    description: Low price
                    x-description-cn: 24小时内最低成交价
                  v:
                    type: string
                    example: "10000"
                    description: Total traded base asset volume
                    x-description-cn: 24小时内成交量
                  q:
                    type: string
                    example: "18"
                    description: Total traded quote asset volume
                    x-description-cn: 24小时内成交额
                  O:
                    type: integer
                    format: int64
                    example: 0
                    description: Statistics open time
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    format: int64
                    example: 1675216573749
                    description: Statistics close time
                    x-description-cn: 统计结束时间
                  F:
                    type: integer
                    format: int64
                    example: 0
                    description: First trade ID
                    x-description-cn: 24小时内第一笔成交交易ID
                  L:
                    type: integer
                    format: int64
                    example: 18150
                    description: Last trade Id
                    x-description-cn: 24小时内最后一笔成交交易ID
                  "n":
                    type: integer
                    format: int64
                    example: 18151
                    description: Total number of trades
                    x-description-cn: 24小时内成交数
              example:
                e: 24hrTicker
                E: 1672515782136
                s: BNBBTC
                p: "0.0015"
                P: "250.00"
                w: "0.0018"
                x: "0.0009"
                c: "0.0025"
                Q: "10"
                b: "0.0024"
                B: "10"
                a: "0.0026"
                A: "100"
                o: "0.0010"
                h: "0.0025"
                l: "0.0010"
                v: "10000"
                q: "18"
                O: 0
                C: 1675216573749
                F: 0
                L: 18150
                "n": 18151
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@ticker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrTicker
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "0.0015"
                        description: Price change
                        x-description-cn: 24小时价格变化
                      P:
                        type: string
                        example: "250.00"
                        description: Price change percent
                        x-description-cn: 24小时价格变化（百分比）
                      w:
                        type: string
                        example: "0.0018"
                        description: Weighted average price
                        x-description-cn: 平均价格
                      x:
                        type: string
                        example: "0.0009"
                        description: First trade(F)-1 price (first trade before the 24hr rolling window)
                        x-description-cn: 整整24小时之前，向前数的最后一次成交价格
                      c:
                        type: string
                        example: "0.0025"
                        description: Last price
                        x-description-cn: 最新成交价格
                      Q:
                        type: string
                        example: "10"
                        description: Last quantity
                        x-description-cn: 最新成交交易的成交量
                      b:
                        type: string
                        example: "0.0024"
                        description: Best bid price
                        x-description-cn: 目前最高买单价
                      B:
                        type: string
                        example: "10"
                        description: Best bid quantity
                        x-description-cn: 目前最高买单价的挂单量
                      a:
                        type: string
                        example: "0.0026"
                        description: Best ask price
                        x-description-cn: 目前最低卖单价
                      A:
                        type: string
                        example: "100"
                        description: Best ask quantity
                        x-description-cn: 目前最低卖单价的挂单量
                      o:
                        type: string
                        example: "0.0010"
                        description: Open price
                        x-description-cn: 整整24小时前，向后数的第一次成交价格
                      h:
                        type: string
                        example: "0.0025"
                        description: High price
                        x-description-cn: 24小时内最高成交价
                      l:
                        type: string
                        example: "0.0010"
                        description: Low price
                        x-description-cn: 24小时内最低成交价
                      v:
                        type: string
                        example: "10000"
                        description: Total traded base asset volume
                        x-description-cn: 24小时内成交量
                      q:
                        type: string
                        example: "18"
                        description: Total traded quote asset volume
                        x-description-cn: 24小时内成交额
                      O:
                        type: integer
                        format: int64
                        example: 0
                        description: Statistics open time
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        format: int64
                        example: 1675216573749
                        description: Statistics close time
                        x-description-cn: 统计结束时间
                      F:
                        type: integer
                        format: int64
                        example: 0
                        description: First trade ID
                        x-description-cn: 24小时内第一笔成交交易ID
                      L:
                        type: integer
                        format: int64
                        example: 18150
                        description: Last trade Id
                        x-description-cn: 24小时内最后一笔成交交易ID
                      "n":
                        type: integer
                        format: int64
                        example: 18151
                        description: Total number of trades
                        x-description-cn: 24小时内成交数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@ticker
                data:
                  e: 24hrTicker
                  E: 1672515782136
                  s: BNBBTC
                  p: "0.0015"
                  P: "250.00"
                  w: "0.0018"
                  x: "0.0009"
                  c: "0.0025"
                  Q: "10"
                  b: "0.0024"
                  B: "10"
                  a: "0.0026"
                  A: "100"
                  o: "0.0010"
                  h: "0.0025"
                  l: "0.0010"
                  v: "10000"
                  q: "18"
                  O: 0
                  C: 1675216573749
                  F: 0
                  L: 18150
                  "n": 18151
  /{symbol}@trade:
    post:
      summary: Trade Streams
      x-summary-cn: 逐笔交易
      description: |-
        The Trade Streams push raw trade information; each trade has a unique
        buyer and seller.
      x-description-cn: 逐笔交易推送每一笔成交的信息。**成交**，或者说交易的定义是仅有一个吃单者与一个挂单者相互交易。
      operationId: trade
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#trade
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/trade.ts
        rust: https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/trade.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/trade.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/TradeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/Trade/Trade.go
      x-update-speed: Real-time
      x-update-speed-cn: 实时
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@trade
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@trade
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Trade Streams
          x-description-cn: 逐笔交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: trade
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  t:
                    type: integer
                    format: int64
                    example: 12345
                    description: Trade ID
                    x-description-cn: 交易ID
                  p:
                    type: string
                    example: "0.001"
                    description: Price
                    x-description-cn: 成交价格
                  q:
                    type: string
                    example: "100"
                    description: Quantity
                    x-description-cn: 成交数量
                  T:
                    type: integer
                    format: int64
                    example: 1672515782136
                    description: Trade time
                    x-description-cn: 成交时间
                  m:
                    type: boolean
                    example: true
                    description: Is the buyer the market maker?
                    x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
                  M:
                    type: boolean
                    example: true
                    description: Ignore
                    x-description-cn: 请忽略该字段
              example:
                e: trade
                E: 1672515782136
                s: BNBBTC
                t: 12345
                p: "0.001"
                q: "100"
                T: 1672515782136
                m: true
                M: true
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@trade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: trade
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      t:
                        type: integer
                        format: int64
                        example: 12345
                        description: Trade ID
                        x-description-cn: 交易ID
                      p:
                        type: string
                        example: "0.001"
                        description: Price
                        x-description-cn: 成交价格
                      q:
                        type: string
                        example: "100"
                        description: Quantity
                        x-description-cn: 成交数量
                      T:
                        type: integer
                        format: int64
                        example: 1672515782136
                        description: Trade time
                        x-description-cn: 成交时间
                      m:
                        type: boolean
                        example: true
                        description: Is the buyer the market maker?
                        x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
                      M:
                        type: boolean
                        example: true
                        description: Ignore
                        x-description-cn: 请忽略该字段
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@trade
                data:
                  e: trade
                  E: 1672515782136
                  s: BNBBTC
                  t: 12345
                  p: "0.001"
                  q: "100"
                  T: 1672515782136
                  m: true
                  M: true
  /{symbol}@blockTrade:
    post:
      summary: Block Trade Streams
      x-summary-cn: 大宗交易
      description: Block Trade Streams push block trade information in real-time.
      x-description-cn: 大宗交易推送实时的大宗交易信息。
      operationId: blockTrade
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#block-trade
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-streams/blockTrade.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_streams/block_trade.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_streams/block_trade.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/stream/defaultpkg/BlockTradeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketstreams/DefaultAPI/BlockTrade/BlockTrade.go
      x-update-speed: Real-time
      x-update-speed-cn: 实时
      parameters:
        - name: id
          in: query
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          description: Symbol to query
          x-description-cn: 要查询的交易对
          schema:
            type: string
            example: bnbusdt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  description: WebSocket Streams method name.
                  x-description-cn: WebSocket 数据流方法名称。
                  enum:
                    - SUBSCRIBE
                  example: SUBSCRIBE
                params:
                  type: array
                  items:
                    type: string
                  description: List of streams to subscribe to.
                  x-description-cn: 要订阅的数据流列表。
                  example:
                    - bnbusdt@blockTrade
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                  description: Unique WebSocket request ID.
                  x-description-cn: 唯一的 WebSocket 请求 ID。
              required:
                - method
                - params
                - id
              additionalProperties: false
            example:
              method: SUBSCRIBE
              params:
                - bnbusdt@blockTrade
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Block Trade Streams
          x-description-cn: 大宗交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: blockTrade
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1772506983582
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BNBBTC
                    description: Symbol
                    x-description-cn: 交易对
                  t:
                    type: integer
                    format: int64
                    example: 582
                    description: Block Trade ID
                    x-description-cn: 大宗交易ID
                  p:
                    type: string
                    example: "0.052"
                    description: Price
                    x-description-cn: 成交价格
                  q:
                    type: string
                    example: "5838"
                    description: Quantity
                    x-description-cn: 成交数量
                  T:
                    type: integer
                    format: int64
                    example: 1772506983321
                    description: Trade time
                    x-description-cn: 成交时间
                  m:
                    type: boolean
                    example: true
                    description: Is the buyer the maker?
                    x-description-cn: 买方是否是做市方。
              example:
                e: blockTrade
                E: 1772506983582
                s: BNBBTC
                t: 582
                p: "0.052"
                q: "5838"
                T: 1772506983321
                m: true
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: bnbusdt@blockTrade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: blockTrade
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1772506983582
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BNBBTC
                        description: Symbol
                        x-description-cn: 交易对
                      t:
                        type: integer
                        format: int64
                        example: 582
                        description: Block Trade ID
                        x-description-cn: 大宗交易ID
                      p:
                        type: string
                        example: "0.052"
                        description: Price
                        x-description-cn: 成交价格
                      q:
                        type: string
                        example: "5838"
                        description: Quantity
                        x-description-cn: 成交数量
                      T:
                        type: integer
                        format: int64
                        example: 1772506983321
                        description: Trade time
                        x-description-cn: 成交时间
                      m:
                        type: boolean
                        example: true
                        description: Is the buyer the maker?
                        x-description-cn: 买方是否是做市方。
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: bnbusdt@blockTrade
                data:
                  e: blockTrade
                  E: 1772506983582
                  s: BNBBTC
                  t: 582
                  p: "0.052"
                  q: "5838"
                  T: 1772506983321
                  m: true
components:
  schemas:
    balanceUpdate:
      type: object
      properties:
        e:
          type: string
          description: Event Type
          x-description-cn: 事件类型
          enum:
            - balanceUpdate
          example: balanceUpdate
        E:
          type: integer
          description: Event Time
          x-description-cn: 事件时间
          example: 1573200697110
          format: int64
        a:
          type: string
          description: Asset
          x-description-cn: 资产名称
          example: BTC
        d:
          type: string
          description: Balance Delta
          x-description-cn: 余额增量
          example: "100.00000000"
        T:
          type: integer
          description: Clear Time
          x-description-cn: 清算时间
          example: 1573200697068
          format: int64
    eventStreamTerminated:
      type: object
      properties:
        e:
          type: string
          description: Event Type
          x-description-cn: 事件类型
          enum:
            - eventStreamTerminated
          example: eventStreamTerminated
        E:
          type: integer
          description: Event Time
          x-description-cn: 事件时间
          example: 1728973001334
          format: int64
    executionReport:
      type: object
      properties:
        e:
          type: string
          description: Event type
          x-description-cn: 事件类型
          enum:
            - executionReport
          example: executionReport
        E:
          type: integer
          description: Event time
          x-description-cn: 事件时间
          example: 1499405658658
          format: int64
        s:
          type: string
          description: Symbol
          x-description-cn: 交易对
          example: ETHBTC
        c:
          type: string
          description: Client order ID
          x-description-cn: clientOrderId
          example: mUvoqJxFIILMdfAW5iGSOW
        S:
          type: string
          description: Side
          x-description-cn: 订单方向
          example: BUY
        o:
          type: string
          description: Order type
          x-description-cn: 订单类型
          example: LIMIT
        f:
          type: string
          description: Time in force
          x-description-cn: 有效方式
          example: GTC
        q:
          type: string
          description: Order quantity
          x-description-cn: 订单原始数量
          example: "1.00000000"
        p:
          type: string
          description: Order price
          x-description-cn: 订单原始价格
          example: "0.10264410"
        P:
          type: string
          description: Stop price
          x-description-cn: 止盈止损单触发价格
          example: "0.00000000"
        F:
          type: string
          description: Iceberg quantity
          x-description-cn: 冰山订单数量
          example: "0.00000000"
        g:
          type: integer
          description: OrderListId
          x-description-cn: OCO订单 OrderListId
          example: -1
          format: int64
        C:
          type: string
          description: Original client order ID; This is the ID of the order being canceled
          x-description-cn: 原始订单自定义ID（原始订单，指撤单操作的对象。撤单本身被视为另一个订单）
          example: ""
        x:
          type: string
          description: Current execution type
          x-description-cn: 本次事件的具体执行类型
          example: NEW
        X:
          type: string
          description: Current order status
          x-description-cn: 订单的当前状态
          example: NEW
        r:
          type: string
          description: Order reject reason; Please see Order Reject Reason for more information.
          x-description-cn: 订单被拒绝的原因；请参阅订单被拒绝的原因了解更多信息
          example: NONE
        i:
          type: integer
          description: Order ID
          x-description-cn: 系统的订单ID
          example: 4293153
          format: int64
        l:
          type: string
          description: Last executed quantity
          x-description-cn: 订单末次成交量
          example: "0.00000000"
        z:
          type: string
          description: Cumulative filled quantity
          x-description-cn: 订单累计已成交量
          example: "0.00000000"
        L:
          type: string
          description: Last executed price
          x-description-cn: 订单末次成交价格
          example: "0.00000000"
        "n":
          type: string
          description: Commission amount
          x-description-cn: 佣金数量
          example: "0"
        "N":
          type: string
          nullable: true
          description: Commission asset
          x-description-cn: 佣金资产类别
          example: null
        T:
          type: integer
          description: Transaction time
          x-description-cn: 成交时间
          example: 1499405658657
          format: int64
        t:
          type: integer
          description: Trade ID
          x-description-cn: 交易ID
          example: -1
          format: int64
        v:
          type: integer
          description: Prevented Match Id; This is only visible if the order expired due to STP
          x-description-cn: 被阻止的交易Id；仅在订单因为STP被阻止时显示
          example: 3
          format: int64
        I:
          type: integer
          description: Execution Id
          x-description-cn: Execution ID
          example: 8641984
          format: int64
        w:
          type: boolean
          description: Is the order on the book?
          x-description-cn: 订单是否在订单簿上？
          example: true
        m:
          type: boolean
          description: Is this trade the maker side?
          x-description-cn: 该成交是作为挂单成交吗？
          example: false
        M:
          type: boolean
          description: Ignore
          x-description-cn: 请忽略
          example: false
        O:
          type: integer
          description: Order creation time
          x-description-cn: 订单创建时间
          example: 1499405658657
          format: int64
        Z:
          type: string
          description: Cumulative quote asset transacted quantity
          x-description-cn: 订单累计已成交金额
          example: "0.00000000"
        "Y":
          type: string
          description: Last quote asset transacted quantity (i.e. lastPrice * lastQty)
          x-description-cn: 订单末次成交金额
          example: "0.00000000"
        Q:
          type: string
          description: Quote Order Quantity
          x-description-cn: 报价订单数量
          example: "0.00000000"
        W:
          type: integer
          description: Working Time; This is only visible if the order has been placed on the book.
          x-description-cn: Working Time; 订单被添加到 order book 的时间
          example: 1499405658657
          format: int64
        V:
          type: string
          description: SelfTradePreventionMode
          x-description-cn: SelfTradePreventionMode
          example: NONE
        d:
          type: integer
          description: Trailing Delta
          x-description-cn: 追踪止损Delta
          example: 4
          format: int64
        D:
          type: integer
          description: Trailing Time
          x-description-cn: 追踪止损时间
          example: 1668680518494
          format: int64
        j:
          type: integer
          description: Strategy Id
          x-description-cn: 策略ID
          example: 1
          format: int64
        J:
          type: integer
          description: Strategy Type
          x-description-cn: 策略类型
          example: 1000000
          format: int64
        A:
          type: string
          description: Prevented Quantity
          x-description-cn: Prevented Quantity
          example: "3.000000"
        B:
          type: string
          description: Last Prevented Quantity
          x-description-cn: Last Prevented Quantity
          example: "3.000000"
        u:
          type: integer
          description: Trade Group Id
          x-description-cn: Trade Group Id
          example: 1
          format: int64
        U:
          type: integer
          description: Counter Order Id
          x-description-cn: Counter Order Id
          example: 37
          format: int64
        Cs:
          type: string
          description: Counter Symbol
          x-description-cn: Counter Symbol
          example: BTCUSDT
        pl:
          type: string
          description: Prevented Execution Quantity
          x-description-cn: Prevented Execution Quantity
          example: "2.123456"
        pL:
          type: string
          description: Prevented Execution Price
          x-description-cn: Prevented Execution Price
          example: "0.10000001"
        pY:
          type: string
          description: Prevented Execution Quote Qty
          x-description-cn: Prevented Execution Quote Qty
          example: "0.21234562"
        Qq:
          type: string
          description: Quote Notional Limit. Appears only if the order was placed with a quote notional limit.
          x-description-cn: 报价资产名义价值上限。仅当下单时设置了报价资产名义价值上限时出现。
          example: "90.00000000"
        eV:
          type: string
          description: >-
            Effective Self Trade Prevention Mode. Appears on prevented-match reports when the applied STP mode differs
            from the order's `selfTradePreventionMode`. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`.
          x-description-cn: >-
            实际生效的 STP 模式。仅在预防撮合的执行报告中，且实际生效的 STP 模式与订单的 `selfTradePreventionMode`
            不同时出现。可能的值：`EXPIRE_MAKER`、`EXPIRE_BOTH`、`DECREMENT`。
          example: DECREMENT
        b:
          type: string
          description: Match Type
          x-description-cn: Match Type
          example: ONE_PARTY_TRADE_REPORT
        a:
          type: integer
          description: Allocation ID
          x-description-cn: Allocation ID
          example: 1234
          format: int64
        k:
          type: string
          description: Working Floor
          x-description-cn: Working Floor
          example: SOR
        uS:
          type: boolean
          description: UsedSor
          x-description-cn: UsedSor
          example: true
        gP:
          type: string
          description: Pegged Price Type
          x-description-cn: 挂钩价格类型
          example: PRIMARY_PEG
        gOT:
          type: string
          description: Pegged Offset Type
          x-description-cn: 挂钩偏移类型
          example: PRICE_LEVEL
        gOV:
          type: integer
          description: Pegged Offset Value
          x-description-cn: 挂钩偏移值
          example: 5
          format: int64
        gp:
          type: string
          description: Pegged Price
          x-description-cn: 挂钩价格
          example: "1.00000000"
        eR:
          type: string
          example: INSUFFICIENT_LIQUIDITY
          description: Expiry Reason. Appears when the order has expired.
          x-description-cn: 过期原因。当订单已过期时出现。
    externalLockUpdate:
      type: object
      properties:
        e:
          type: string
          description: Event Type
          x-description-cn: 事件类型
          enum:
            - externalLockUpdate
          example: externalLockUpdate
        E:
          type: integer
          description: Event Time
          x-description-cn: 事件时间
          example: 1581557507324
          format: int64
        a:
          type: string
          description: Asset
          x-description-cn: 资产
          example: NEO
        d:
          type: string
          description: Delta
          x-description-cn: 余额变动量
          example: "10.00000000"
        T:
          type: integer
          description: Transaction Time
          x-description-cn: 交易时间
          example: 1581557507268
          format: int64
    listStatus:
      type: object
      properties:
        e:
          type: string
          description: Event Type
          x-description-cn: 事件类型
          enum:
            - listStatus
          example: listStatus
        E:
          type: integer
          description: Event Time
          x-description-cn: 事件时间
          example: 1564035303637
          format: int64
        s:
          type: string
          description: Symbol
          x-description-cn: 交易对
          example: ETHBTC
        g:
          type: integer
          description: OrderListId
          x-description-cn: OrderListId
          example: 2
          format: int64
        c:
          type: string
          description: Contingency Type
          x-description-cn: Contingency 类型
          example: OCO
        l:
          type: string
          description: List Status Type
          x-description-cn: List 状态类型
          example: EXEC_STARTED
        L:
          type: string
          description: List Order Status
          x-description-cn: List 订单类型
          example: EXECUTING
        r:
          type: string
          description: List Reject Reason
          x-description-cn: List 被拒绝的原因
          example: NONE
        C:
          type: string
          description: List Client Order ID
          x-description-cn: List Client Order ID
          example: F4QN4G8DlFATFlIUQ0cjdD
        T:
          type: integer
          description: Transaction Time
          x-description-cn: 成交时间
          example: 1564035303625
          format: int64
        O:
          type: array
          description: An array of objects
          x-description-cn: 对象数组
          example:
            - s: ETHBTC
              i: 17
              c: AJYsMjErWJesZvqlJCTUgL
            - s: ETHBTC
              i: 18
              c: bfYPSQdLoqAJeNrOr9adzq
          items:
            type: object
            properties:
              s:
                type: string
                description: Symbol
                x-description-cn: 交易对
                example: ETHBTC
              i:
                type: integer
                description: OrderId
                x-description-cn: 系统的订单ID
                example: 17
                format: int64
              c:
                type: string
                description: ClientOrderId
                x-description-cn: clientOrderId
                example: AJYsMjErWJesZvqlJCTUgL
    outboundAccountPosition:
      type: object
      properties:
        e:
          type: string
          description: Event type
          x-description-cn: 事件类型
          enum:
            - outboundAccountPosition
          example: outboundAccountPosition
        E:
          type: integer
          description: Event Time
          x-description-cn: 事件时间
          example: 1564034571105
          format: int64
        u:
          type: integer
          description: Time of last account update
          x-description-cn: 账户末次更新时间戳
          example: 1564034571073
          format: int64
        B:
          type: array
          description: Balances Array
          x-description-cn: 余额
          items:
            type: object
            properties:
              a:
                type: string
                description: Asset
                x-description-cn: 资产名称
                example: ETH
              f:
                type: string
                description: Free
                x-description-cn: 可用余额
                example: "10000.000000"
              l:
                type: string
                description: Locked
                x-description-cn: 冻结余额
                example: "0.000000"
    User Data Stream Events:
      oneOf:
        - $ref: "#/components/schemas/balanceUpdate"
        - $ref: "#/components/schemas/eventStreamTerminated"
        - $ref: "#/components/schemas/executionReport"
        - $ref: "#/components/schemas/externalLockUpdate"
        - $ref: "#/components/schemas/listStatus"
        - $ref: "#/components/schemas/outboundAccountPosition"
      discriminator:
        propertyName: e
        mapping:
          balanceUpdate: "#/components/schemas/balanceUpdate"
          eventStreamTerminated: "#/components/schemas/eventStreamTerminated"
          executionReport: "#/components/schemas/executionReport"
          externalLockUpdate: "#/components/schemas/externalLockUpdate"
          listStatus: "#/components/schemas/listStatus"
          outboundAccountPosition: "#/components/schemas/outboundAccountPosition"
```