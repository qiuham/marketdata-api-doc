---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:23.563794
---

# advanced-trading-alpha-trading__ws-streams spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Alpha WebSocket Market Streams
  description: Access Alpha market streams over WebSocket.
  x-description-cn: 通过 WebSocket 访问 Alpha 行情数据流。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-streams
x-untagged-label: true
externalDocs:
  description: Alpha Trading docs
  url: https://developers.binance.com/en/docs/products/alpha
servers:
  - url: wss://nbstream.binance.com/w3w/wsa/stream
paths:
  /{symbol}@aggTrade:
    post:
      summary: Aggregate Trade Stream
      x-summary-cn: 聚合成交流
      description: Pushes aggregate trade updates for a symbol.
      x-description-cn: 推送指定交易对的聚合成交更新。
      operationId: aggregateTradeStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#aggregate-trade-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/aggregateTradeStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/aggregate_trade_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/aggregate_trade_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/AggregateTradeStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/AggregateTradeStream/AggregateTradeStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
                    - alpha_116usdt@aggTrade
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@aggTrade
              id: 532601580
      responses:
        Raw Stream:
          description: Aggregate Trade Stream
          x-description-cn: 聚合成交流
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
                    example: 1771828569861
                    description: Event time (ms)
                    x-description-cn: 事件时间 (ms)
                  T:
                    type: integer
                    format: int64
                    example: 1771828569702
                    description: Trade time (ms)
                    x-description-cn: 成交时间 (ms)
                  a:
                    type: integer
                    format: int64
                    example: 2684294
                    description: Aggregated trade ID
                    x-description-cn: 聚合交易ID
                  f:
                    type: integer
                    format: int64
                    example: 2684294
                    description: First trade ID in the aggregation
                    x-description-cn: 被归集的首个交易ID
                  l:
                    type: integer
                    format: int64
                    example: 2684294
                    description: Last trade ID in the aggregation
                    x-description-cn: 末个交易ID
                  m:
                    type: boolean
                    example: false
                    description: Is the buyer the market maker
                    x-description-cn: 是否为做市方
                  p:
                    type: string
                    example: "0.08530000"
                    description: Price
                    x-description-cn: 成交价格
                  q:
                    type: string
                    example: "879.24000000"
                    description: Quantity
                    x-description-cn: 成交数量
                  s:
                    type: string
                    example: ALPHA_474USDT
                    description: Symbol
                    x-description-cn: 交易对符号
              example:
                e: aggTrade
                E: 1771828569861
                T: 1771828569702
                a: 2684294
                f: 2684294
                l: 2684294
                m: false
                p: "0.08530000"
                q: "879.24000000"
                s: ALPHA_474USDT
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@aggTrade
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
                        example: 1771828569861
                        description: Event time (ms)
                        x-description-cn: 事件时间 (ms)
                      T:
                        type: integer
                        format: int64
                        example: 1771828569702
                        description: Trade time (ms)
                        x-description-cn: 成交时间 (ms)
                      a:
                        type: integer
                        format: int64
                        example: 2684294
                        description: Aggregated trade ID
                        x-description-cn: 聚合交易ID
                      f:
                        type: integer
                        format: int64
                        example: 2684294
                        description: First trade ID in the aggregation
                        x-description-cn: 被归集的首个交易ID
                      l:
                        type: integer
                        format: int64
                        example: 2684294
                        description: Last trade ID in the aggregation
                        x-description-cn: 末个交易ID
                      m:
                        type: boolean
                        example: false
                        description: Is the buyer the market maker
                        x-description-cn: 是否为做市方
                      p:
                        type: string
                        example: "0.08530000"
                        description: Price
                        x-description-cn: 成交价格
                      q:
                        type: string
                        example: "879.24000000"
                        description: Quantity
                        x-description-cn: 成交数量
                      s:
                        type: string
                        example: ALPHA_474USDT
                        description: Symbol
                        x-description-cn: 交易对符号
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@aggTrade
                data:
                  e: aggTrade
                  E: 1771828569861
                  T: 1771828569702
                  a: 2684294
                  f: 2684294
                  l: 2684294
                  m: false
                  p: "0.08530000"
                  q: "879.24000000"
                  s: ALPHA_474USDT
  /!bookTicker:
    post:
      summary: All Book Ticker Stream
      x-summary-cn: 全市场最优挂单流
      description: Pushes best bid/ask updates for all symbols.
      x-description-cn: 推送全市场一档买卖盘更新。
      operationId: allBookTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#all-book-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/allBookTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/all_book_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/all_book_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/AllBookTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/AllBookTickerStream/AllBookTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
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
                    - "!bookTicker"
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - "!bookTicker"
              id: 532601580
      responses:
        Raw Stream:
          description: All Book Ticker Stream
          x-description-cn: 全市场最优挂单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: bookTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773108379067
                    description: eventTime
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    format: int64
                    example: 1773108379054
                    description: transactionTime
                    x-description-cn: 成交时间/交易时间
                  u:
                    type: integer
                    format: int64
                    example: 6663207693
                    description: updateId
                    x-description-cn: 更新 ID
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "8.30000000"
                    description: bid1Price
                    x-description-cn: 买一价格
                  B:
                    type: string
                    example: "0.91076900"
                    description: bid1Quantity
                    x-description-cn: 买一数量
                  a:
                    type: string
                    example: "9.30000000"
                    description: ask1Price
                    x-description-cn: 卖一价格
                  A:
                    type: string
                    example: "2.00353200"
                    description: ask1Quantity
                    x-description-cn: 卖一数量
              example:
                e: bookTicker
                E: 1773108379067
                T: 1773108379054
                u: 6663207693
                s: ALPHA_116USDT
                b: "8.30000000"
                B: "0.91076900"
                a: "9.30000000"
                A: "2.00353200"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!bookTicker"
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: bookTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773108379067
                        description: eventTime
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        format: int64
                        example: 1773108379054
                        description: transactionTime
                        x-description-cn: 成交时间/交易时间
                      u:
                        type: integer
                        format: int64
                        example: 6663207693
                        description: updateId
                        x-description-cn: 更新 ID
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "8.30000000"
                        description: bid1Price
                        x-description-cn: 买一价格
                      B:
                        type: string
                        example: "0.91076900"
                        description: bid1Quantity
                        x-description-cn: 买一数量
                      a:
                        type: string
                        example: "9.30000000"
                        description: ask1Price
                        x-description-cn: 卖一价格
                      A:
                        type: string
                        example: "2.00353200"
                        description: ask1Quantity
                        x-description-cn: 卖一数量
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!bookTicker"
                data:
                  e: bookTicker
                  E: 1773108379067
                  T: 1773108379054
                  u: 6663207693
                  s: ALPHA_116USDT
                  b: "8.30000000"
                  B: "0.91076900"
                  a: "9.30000000"
                  A: "2.00353200"
  /!miniTicker@arr:
    post:
      summary: All Mini Ticker Stream
      x-summary-cn: 全市场简略行情流
      description: Pushes mini ticker statistics for all symbols.
      x-description-cn: 推送全市场简略行情统计。
      operationId: allMiniTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#all-mini-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/allMiniTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/all_mini_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/all_mini_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/AllMiniTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/AllMiniTickerStream/AllMiniTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
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
                  type: integer
                  example: 532601580
                  format: int32
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
              id: 532601580
      responses:
        Raw Stream:
          description: All Mini Ticker Stream
          x-description-cn: 全市场简略行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrMiniTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773109449908
                    description: eventTime
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  c:
                    type: string
                    example: "8.40000000"
                    description: closePrice
                    x-description-cn: 收盘价
                  o:
                    type: string
                    example: "8.40000000"
                    description: openPrice
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "8.50000000"
                    description: highPrice
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "8.30000000"
                    description: lowPrice
                    x-description-cn: 最低价
                  v:
                    type: string
                    example: "64739.03978900"
                    description: volume
                    x-description-cn: 基础资产成交量
                  q:
                    type: string
                    example: "543810.36005090"
                    description: quoteVolume
                    x-description-cn: 计价资产成交额
              example:
                e: 24hrMiniTicker
                E: 1773109449908
                s: ALPHA_116USDT
                c: "8.40000000"
                o: "8.40000000"
                h: "8.50000000"
                l: "8.30000000"
                v: "64739.03978900"
                q: "543810.36005090"
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
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrMiniTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773109449908
                        description: eventTime
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      c:
                        type: string
                        example: "8.40000000"
                        description: closePrice
                        x-description-cn: 收盘价
                      o:
                        type: string
                        example: "8.40000000"
                        description: openPrice
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "8.50000000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "8.30000000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "64739.03978900"
                        description: volume
                        x-description-cn: 基础资产成交量
                      q:
                        type: string
                        example: "543810.36005090"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!miniTicker@arr"
                data:
                  e: 24hrMiniTicker
                  E: 1773109449908
                  s: ALPHA_116USDT
                  c: "8.40000000"
                  o: "8.40000000"
                  h: "8.50000000"
                  l: "8.30000000"
                  v: "64739.03978900"
                  q: "543810.36005090"
  /!ticker@arr:
    post:
      summary: All Ticker Stream
      x-summary-cn: 全市场完整行情流
      description: Pushes full ticker statistics for all symbols.
      x-description-cn: 推送全市场完整行情统计。
      operationId: allTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#all-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/allTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/all_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/all_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/AllTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/AllTickerStream/AllTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
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
                    - "!ticker@arr"
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - "!ticker@arr"
              id: 532601580
      responses:
        Raw Stream:
          description: All Ticker Stream
          x-description-cn: 全市场完整行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773109631569
                    description: eventTime
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "0.00000000"
                    description: priceChange
                    x-description-cn: 涨跌额
                  P:
                    type: string
                    example: "0.00"
                    description: priceChangePercent
                    x-description-cn: 涨跌幅
                  w:
                    type: string
                    example: "8.40003127"
                    description: averagePrice
                    x-description-cn: 平均价
                  c:
                    type: string
                    example: "8.40000000"
                    description: closePrice
                    x-description-cn: 收盘价
                  Q:
                    type: string
                    example: "0.49293200"
                    description: lastTradeVolume
                    x-description-cn: 最近一笔成交量
                  o:
                    type: string
                    example: "8.40000000"
                    description: openPrice
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "8.50000000"
                    description: highPrice
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "8.30000000"
                    description: lowPrice
                    x-description-cn: 最低价
                  v:
                    type: string
                    example: "64750.63418500"
                    description: volume
                    x-description-cn: 基础资产成交量
                  q:
                    type: string
                    example: "543907.35169250"
                    description: quoteVolume
                    x-description-cn: 计价资产成交额
                  O:
                    type: integer
                    format: int64
                    example: 1773023220000
                    description: startTime
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    format: int64
                    example: 1773109631555
                    description: endTime
                    x-description-cn: 统计结束时间
                  F:
                    type: integer
                    format: int64
                    example: 19847634
                    description: firstTradeId
                    x-description-cn: 首笔成交 ID
                  L:
                    type: integer
                    format: int64
                    example: 19911287
                    description: lastTradeId
                    x-description-cn: 末笔成交 ID
                  "n":
                    type: integer
                    format: int64
                    example: 217505
                    description: tradeNum
                    x-description-cn: 成交笔数
              example:
                e: 24hrTicker
                E: 1773109631569
                s: ALPHA_116USDT
                p: "0.00000000"
                P: "0.00"
                w: "8.40003127"
                c: "8.40000000"
                Q: "0.49293200"
                o: "8.40000000"
                h: "8.50000000"
                l: "8.30000000"
                v: "64750.63418500"
                q: "543907.35169250"
                O: 1773023220000
                C: 1773109631555
                F: 19847634
                L: 19911287
                "n": 217505
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!ticker@arr"
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773109631569
                        description: eventTime
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "0.00000000"
                        description: priceChange
                        x-description-cn: 涨跌额
                      P:
                        type: string
                        example: "0.00"
                        description: priceChangePercent
                        x-description-cn: 涨跌幅
                      w:
                        type: string
                        example: "8.40003127"
                        description: averagePrice
                        x-description-cn: 平均价
                      c:
                        type: string
                        example: "8.40000000"
                        description: closePrice
                        x-description-cn: 收盘价
                      Q:
                        type: string
                        example: "0.49293200"
                        description: lastTradeVolume
                        x-description-cn: 最近一笔成交量
                      o:
                        type: string
                        example: "8.40000000"
                        description: openPrice
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "8.50000000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "8.30000000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "64750.63418500"
                        description: volume
                        x-description-cn: 基础资产成交量
                      q:
                        type: string
                        example: "543907.35169250"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                      O:
                        type: integer
                        format: int64
                        example: 1773023220000
                        description: startTime
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        format: int64
                        example: 1773109631555
                        description: endTime
                        x-description-cn: 统计结束时间
                      F:
                        type: integer
                        format: int64
                        example: 19847634
                        description: firstTradeId
                        x-description-cn: 首笔成交 ID
                      L:
                        type: integer
                        format: int64
                        example: 19911287
                        description: lastTradeId
                        x-description-cn: 末笔成交 ID
                      "n":
                        type: integer
                        format: int64
                        example: 217505
                        description: tradeNum
                        x-description-cn: 成交笔数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!ticker@arr"
                data:
                  e: 24hrTicker
                  E: 1773109631569
                  s: ALPHA_116USDT
                  p: "0.00000000"
                  P: "0.00"
                  w: "8.40003127"
                  c: "8.40000000"
                  Q: "0.49293200"
                  o: "8.40000000"
                  h: "8.50000000"
                  l: "8.30000000"
                  v: "64750.63418500"
                  q: "543907.35169250"
                  O: 1773023220000
                  C: 1773109631555
                  F: 19847634
                  L: 19911287
                  "n": 217505
  /came@allTokens@ticker24:
    post:
      summary: All Tokens 24h Ticker Stream
      x-summary-cn: 全部代币 24 小时行情流
      description: Pushes 24h ticker-like metrics for all tokens.
      x-description-cn: 推送全部代币的 24 小时行情指标。
      operationId: allTokens24hTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#all-tokens24h-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/allTokens24hTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/all_tokens24h_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/all_tokens24h_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/AllTokens24hTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/AllTokens24hTickerStream/AllTokens24hTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
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
                    - came@allTokens@ticker24
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - came@allTokens@ticker24
              id: 532601580
      responses:
        Raw Stream:
          description: All Tokens 24h Ticker Stream
          x-description-cn: 全部代币 24 小时行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: tickerList
                    description: Event type
                    x-description-cn: 事件类型
                  d:
                    type: array
                    description: Per-token 24-hour ticker metrics
                    x-description-cn: 按代币维度的 24 小时行情指标
                    items:
                      type: object
                      properties:
                        ca:
                          type: string
                          example: 0x8fce...@56
                          description: Contract address@chain ID
                          x-description-cn: 合约地址@链 ID
                        cnt24:
                          type: integer
                          format: int64
                          example: 10426
                          description: Number of trades in the last 24 hours
                          x-description-cn: 过去 24 小时成交笔数
                        fdv:
                          type: string
                          example: "72834145.18711072"
                          description: Fully diluted valuation
                          x-description-cn: 完全稀释估值
                        hc:
                          type: string
                          example: "6822"
                          description: Number of holders
                          x-description-cn: 持有人数量
                        liq:
                          type: string
                          example: "1442996.98151177662835"
                          description: Liquidity
                          x-description-cn: 流动性
                        mc:
                          type: string
                          example: "13542034.24008014"
                          description: Market cap
                          x-description-cn: 市值
                        p:
                          type: string
                          example: "0.072849536538593663"
                          description: Current price
                          x-description-cn: 当前价格
                        pc24:
                          type: string
                          example: "-2.32"
                          description: 24-hour price change percent
                          x-description-cn: 24 小时价格涨跌幅
                        s:
                          type: string
                          example: "1"
                          description: Token short identifier
                          x-description-cn: 代币短标识
                        t:
                          type: integer
                          format: int64
                          example: 1771825733000
                          description: Event timestamp in milliseconds
                          x-description-cn: 事件时间戳（毫秒）
                        vol24:
                          type: string
                          example: "12930712.213702157742688594285"
                          description: 24-hour volume
                          x-description-cn: 24 小时成交量
              example:
                e: tickerList
                d:
                  - ca: 0x8fce...@56
                    cnt24: 10426
                    fdv: "72834145.18711072"
                    hc: "6822"
                    liq: "1442996.98151177662835"
                    mc: "13542034.24008014"
                    p: "0.072849536538593663"
                    pc24: "-2.32"
                    s: "1"
                    t: 1771825733000
                    vol24: "12930712.213702157742688594285"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: came@allTokens@ticker24
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: tickerList
                        description: Event type
                        x-description-cn: 事件类型
                      d:
                        type: array
                        description: Per-token 24-hour ticker metrics
                        x-description-cn: 按代币维度的 24 小时行情指标
                        items:
                          type: object
                          properties:
                            ca:
                              type: string
                              example: 0x8fce...@56
                              description: Contract address@chain ID
                              x-description-cn: 合约地址@链 ID
                            cnt24:
                              type: integer
                              format: int64
                              example: 10426
                              description: Number of trades in the last 24 hours
                              x-description-cn: 过去 24 小时成交笔数
                            fdv:
                              type: string
                              example: "72834145.18711072"
                              description: Fully diluted valuation
                              x-description-cn: 完全稀释估值
                            hc:
                              type: string
                              example: "6822"
                              description: Number of holders
                              x-description-cn: 持有人数量
                            liq:
                              type: string
                              example: "1442996.98151177662835"
                              description: Liquidity
                              x-description-cn: 流动性
                            mc:
                              type: string
                              example: "13542034.24008014"
                              description: Market cap
                              x-description-cn: 市值
                            p:
                              type: string
                              example: "0.072849536538593663"
                              description: Current price
                              x-description-cn: 当前价格
                            pc24:
                              type: string
                              example: "-2.32"
                              description: 24-hour price change percent
                              x-description-cn: 24 小时价格涨跌幅
                            s:
                              type: string
                              example: "1"
                              description: Token short identifier
                              x-description-cn: 代币短标识
                            t:
                              type: integer
                              format: int64
                              example: 1771825733000
                              description: Event timestamp in milliseconds
                              x-description-cn: 事件时间戳（毫秒）
                            vol24:
                              type: string
                              example: "12930712.213702157742688594285"
                              description: 24-hour volume
                              x-description-cn: 24 小时成交量
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: came@allTokens@ticker24
                data:
                  e: tickerList
                  d:
                    - ca: 0x8fce...@56
                      cnt24: 10426
                      fdv: "72834145.18711072"
                      hc: "6822"
                      liq: "1442996.98151177662835"
                      mc: "13542034.24008014"
                      p: "0.072849536538593663"
                      pc24: "-2.32"
                      s: "1"
                      t: 1771825733000
                      vol24: "12930712.213702157742688594285"
  /{symbol}@bookTicker:
    post:
      summary: Book Ticker Stream
      x-summary-cn: 最优挂单流
      description: Pushes best bid/ask updates for a symbol.
      x-description-cn: 推送指定交易对的一档买卖盘更新。
      operationId: bookTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#book-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/bookTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/book_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/book_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/BookTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/BookTickerStream/BookTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
                    - alpha_116usdt@bookTicker
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@bookTicker
              id: 532601580
      responses:
        Raw Stream:
          description: Book Ticker Stream
          x-description-cn: 最优挂单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: bookTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773108379067
                    description: eventTime
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    format: int64
                    example: 1773108379054
                    description: transactionTime
                    x-description-cn: 成交时间/交易时间
                  u:
                    type: integer
                    format: int64
                    example: 6663207693
                    description: updateId
                    x-description-cn: 更新 ID
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "8.30000000"
                    description: bid1Price
                    x-description-cn: 买一价格
                  B:
                    type: string
                    example: "0.91076900"
                    description: bid1Quantity
                    x-description-cn: 买一数量
                  a:
                    type: string
                    example: "9.30000000"
                    description: ask1Price
                    x-description-cn: 卖一价格
                  A:
                    type: string
                    example: "2.00353200"
                    description: ask1Quantity
                    x-description-cn: 卖一数量
              example:
                e: bookTicker
                E: 1773108379067
                T: 1773108379054
                u: 6663207693
                s: ALPHA_116USDT
                b: "8.30000000"
                B: "0.91076900"
                a: "9.30000000"
                A: "2.00353200"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@bookTicker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: bookTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773108379067
                        description: eventTime
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        format: int64
                        example: 1773108379054
                        description: transactionTime
                        x-description-cn: 成交时间/交易时间
                      u:
                        type: integer
                        format: int64
                        example: 6663207693
                        description: updateId
                        x-description-cn: 更新 ID
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "8.30000000"
                        description: bid1Price
                        x-description-cn: 买一价格
                      B:
                        type: string
                        example: "0.91076900"
                        description: bid1Quantity
                        x-description-cn: 买一数量
                      a:
                        type: string
                        example: "9.30000000"
                        description: ask1Price
                        x-description-cn: 卖一价格
                      A:
                        type: string
                        example: "2.00353200"
                        description: ask1Quantity
                        x-description-cn: 卖一数量
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@bookTicker
                data:
                  e: bookTicker
                  E: 1773108379067
                  T: 1773108379054
                  u: 6663207693
                  s: ALPHA_116USDT
                  b: "8.30000000"
                  B: "0.91076900"
                  a: "9.30000000"
                  A: "2.00353200"
  /{symbol}@depth{levels}@{interval}:
    post:
      summary: Partial Depth Stream
      x-summary-cn: 部分深度流
      description: Pushes partial depth updates (UI orders only).
      x-description-cn: 推送部分深度更新（仅 UI 订单）。
      operationId: partialDepthStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#partial-depth-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/partialDepthStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/partial_depth_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/partial_depth_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/PartialDepthStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/PartialDepthStream/PartialDepthStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
          description: Depth levels.
          x-description-cn: 深度档位。
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 100ms
            enum:
              - 0ms
              - 100ms
              - 500ms
          description: Update interval.
          x-description-cn: 更新间隔。
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
                    - alpha_116usdt@depth5@100ms
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@depth5@100ms
              id: 532601580
      responses:
        Raw Stream:
          description: Partial Depth Stream
          x-description-cn: 部分深度流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773110222878
                    description: eventTime
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    format: int64
                    example: 1773110222767
                    description: transactionTime
                    x-description-cn: 成交时间/交易时间
                  U:
                    type: integer
                    format: int64
                    example: 6663367135
                    description: firstUpdateId
                    x-description-cn: 首个更新 ID
                  u:
                    type: integer
                    format: int64
                    example: 6663367147
                    description: lastUpdateId
                    x-description-cn: 最后更新 ID
                  pu:
                    type: integer
                    format: int64
                    example: 6663366971
                    description: previousUpdateId
                    x-description-cn: 上一个更新 ID
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  b:
                    type: array
                    description: bids to be updated
                    x-description-cn: 需要更新的买单
                    example:
                      - - "0.16479999"
                        - "0"
                      - - "0.16480000"
                        - "18.68000000"
                    items:
                      type: array
                      example:
                        - "0.16480000"
                        - "18.68000000"
                      items:
                        type: string
                        example: "0.16480000"
                  a:
                    type: array
                    description: asks to be updated
                    x-description-cn: 需要更新的卖单
                    example:
                      - - "0.16490000"
                        - "500.00000000"
                      - - "0.16500000"
                        - "0"
                    items:
                      type: array
                      example:
                        - "0.16490000"
                        - "500.00000000"
                      items:
                        type: string
                        example: "0.16490000"
              example:
                e: depthUpdate
                E: 1773110222878
                T: 1773110222767
                U: 6663367135
                u: 6663367147
                pu: 6663366971
                s: ALPHA_116USDT
                b:
                  - - "0.16479999"
                    - "0"
                  - - "0.16480000"
                    - "18.68000000"
                a:
                  - - "0.16490000"
                    - "500.00000000"
                  - - "0.16500000"
                    - "0"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@depth5@100ms
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: depthUpdate
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773110222878
                        description: eventTime
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        format: int64
                        example: 1773110222767
                        description: transactionTime
                        x-description-cn: 成交时间/交易时间
                      U:
                        type: integer
                        format: int64
                        example: 6663367135
                        description: firstUpdateId
                        x-description-cn: 首个更新 ID
                      u:
                        type: integer
                        format: int64
                        example: 6663367147
                        description: lastUpdateId
                        x-description-cn: 最后更新 ID
                      pu:
                        type: integer
                        format: int64
                        example: 6663366971
                        description: previousUpdateId
                        x-description-cn: 上一个更新 ID
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      b:
                        type: array
                        description: bids to be updated
                        x-description-cn: 需要更新的买单
                        example:
                          - - "0.16479999"
                            - "0"
                          - - "0.16480000"
                            - "18.68000000"
                        items:
                          type: array
                          example:
                            - "0.16480000"
                            - "18.68000000"
                          items:
                            type: string
                            example: "0.16480000"
                      a:
                        type: array
                        description: asks to be updated
                        x-description-cn: 需要更新的卖单
                        example:
                          - - "0.16490000"
                            - "500.00000000"
                          - - "0.16500000"
                            - "0"
                        items:
                          type: array
                          example:
                            - "0.16490000"
                            - "500.00000000"
                          items:
                            type: string
                            example: "0.16490000"
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@depth5@100ms
                data:
                  e: depthUpdate
                  E: 1773110222878
                  T: 1773110222767
                  U: 6663367135
                  u: 6663367147
                  pu: 6663366971
                  s: ALPHA_116USDT
                  b:
                    - - "0.16479999"
                      - "0"
                    - - "0.16480000"
                      - "18.68000000"
                  a:
                    - - "0.16490000"
                      - "500.00000000"
                    - - "0.16500000"
                      - "0"
  /{symbol}@fulldepth@{interval}:
    post:
      summary: Full Depth Stream
      x-summary-cn: 全量深度流
      description: Returns all available depth, including UI and API orders.
      x-description-cn: 返回所有可用深度信息，包含 UI 与 API 订单。
      operationId: fullDepthStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#full-depth-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/fullDepthStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/full_depth_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/full_depth_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/FullDepthStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/FullDepthStream/FullDepthStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 500ms
            enum:
              - 0ms
              - 100ms
              - 500ms
          description: Update interval.
          x-description-cn: 更新间隔。
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
                    - alpha_116usdt@fulldepth@500ms
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@fulldepth@500ms
              id: 532601580
      responses:
        Raw Stream:
          description: Full Depth Stream
          x-description-cn: 全量深度流
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
                    example: 1771828614381
                    description: Event time (ms)
                    x-description-cn: 事件时间 (ms)
                  T:
                    type: integer
                    format: int64
                    example: 1771828614258
                    description: Matching time (ms)
                    x-description-cn: 撮合时间 (ms)
                  U:
                    type: integer
                    format: int64
                    example: 42648947917
                    description: First updateId in this event
                    x-description-cn: 本次更新首个updateId
                  u:
                    type: integer
                    format: int64
                    example: 42648948229
                    description: Last updateId in this event
                    x-description-cn: 本次更新末个updateId
                  pu:
                    type: integer
                    format: int64
                    example: 42648947321
                    description: Previous updateId from the last push
                    x-description-cn: 上次推送的updateId
                  s:
                    type: string
                    example: ALPHA_474USDT
                    description: Symbol
                    x-description-cn: 交易对
                  b:
                    type: array
                    description: bids to be updated
                    x-description-cn: 需要更新的买单
                    example:
                      - - "0.16479999"
                        - "0"
                      - - "0.16480000"
                        - "18.68000000"
                    items:
                      type: array
                      example:
                        - "0.16480000"
                        - "18.68000000"
                      items:
                        type: string
                        example: "0.16480000"
                  a:
                    type: array
                    description: asks to be updated
                    x-description-cn: 需要更新的卖单
                    example:
                      - - "0.16490000"
                        - "500.00000000"
                      - - "0.16500000"
                        - "0"
                    items:
                      type: array
                      example:
                        - "0.16490000"
                        - "500.00000000"
                      items:
                        type: string
                        example: "0.16490000"
              example:
                e: depthUpdate
                E: 1771828614381
                T: 1771828614258
                U: 42648947917
                u: 42648948229
                pu: 42648947321
                s: ALPHA_474USDT
                b:
                  - - "0.16479999"
                    - "0"
                  - - "0.16480000"
                    - "18.68000000"
                a:
                  - - "0.16490000"
                    - "500.00000000"
                  - - "0.16500000"
                    - "0"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@fulldepth@500ms
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
                        example: 1771828614381
                        description: Event time (ms)
                        x-description-cn: 事件时间 (ms)
                      T:
                        type: integer
                        format: int64
                        example: 1771828614258
                        description: Matching time (ms)
                        x-description-cn: 撮合时间 (ms)
                      U:
                        type: integer
                        format: int64
                        example: 42648947917
                        description: First updateId in this event
                        x-description-cn: 本次更新首个updateId
                      u:
                        type: integer
                        format: int64
                        example: 42648948229
                        description: Last updateId in this event
                        x-description-cn: 本次更新末个updateId
                      pu:
                        type: integer
                        format: int64
                        example: 42648947321
                        description: Previous updateId from the last push
                        x-description-cn: 上次推送的updateId
                      s:
                        type: string
                        example: ALPHA_474USDT
                        description: Symbol
                        x-description-cn: 交易对
                      b:
                        type: array
                        description: bids to be updated
                        x-description-cn: 需要更新的买单
                        example:
                          - - "0.16479999"
                            - "0"
                          - - "0.16480000"
                            - "18.68000000"
                        items:
                          type: array
                          example:
                            - "0.16480000"
                            - "18.68000000"
                          items:
                            type: string
                            example: "0.16480000"
                      a:
                        type: array
                        description: asks to be updated
                        x-description-cn: 需要更新的卖单
                        example:
                          - - "0.16490000"
                            - "500.00000000"
                          - - "0.16500000"
                            - "0"
                        items:
                          type: array
                          example:
                            - "0.16490000"
                            - "500.00000000"
                          items:
                            type: string
                            example: "0.16490000"
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@fulldepth@500ms
                data:
                  e: depthUpdate
                  E: 1771828614381
                  T: 1771828614258
                  U: 42648947917
                  u: 42648948229
                  pu: 42648947321
                  s: ALPHA_474USDT
                  b:
                    - - "0.16479999"
                      - "0"
                    - - "0.16480000"
                      - "18.68000000"
                  a:
                    - - "0.16490000"
                      - "500.00000000"
                    - - "0.16500000"
                      - "0"
  /{symbol}@kline_{interval}:
    post:
      summary: Kline Stream
      x-summary-cn: K 线流
      description: Pushes kline updates for a symbol.
      x-description-cn: 推送指定交易对 K 线更新。
      operationId: klineStream
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#kline-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/klineStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/kline_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/kline_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/KlineStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/KlineStream/KlineStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 1m
            enum:
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
                    - alpha_116usdt@kline_1m
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@kline_1m
              id: 532601580
      responses:
        Raw Stream:
          description: Kline Stream
          x-description-cn: K 线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: kline
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773111055144
                    description: eventTime
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        format: int64
                        example: 1773111000000
                        description: startTime
                        x-description-cn: K 线开始时间
                      T:
                        type: integer
                        format: int64
                        example: 1773111059999
                        description: endTime
                        x-description-cn: K 线结束时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: interval
                        x-description-cn: K 线周期
                      f:
                        type: integer
                        format: int64
                        example: 19912696
                        description: firstTradeId
                        x-description-cn: 首笔成交 ID
                      L:
                        type: integer
                        format: int64
                        example: 19912765
                        description: lastTradeId
                        x-description-cn: 末笔成交 ID
                      o:
                        type: string
                        example: "8.40000000"
                        description: openPrice
                        x-description-cn: 开盘价
                      c:
                        type: string
                        example: "8.40000000"
                        description: closePrice
                        x-description-cn: 收盘价
                      h:
                        type: string
                        example: "8.40000000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "8.40000000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "63.64876300"
                        description: volume
                        x-description-cn: 成交量
                      "n":
                        type: integer
                        format: int64
                        example: 218
                        description: tradeNum
                        x-description-cn: 成交笔数
                      x:
                        type: boolean
                        example: false
                        description: klineComplete
                        x-description-cn: K 线是否已完结
                      q:
                        type: string
                        example: "534.64960920"
                        description: quoteAssetVolume
                        x-description-cn: 成交额
                      V:
                        type: string
                        example: "63.64876300"
                        description: takerBuyBaseAssetVolume
                        x-description-cn: 主动买入成交量
                      Q:
                        type: string
                        example: "534.64960920"
                        description: takerBuyQuoteAssetVolume
                        x-description-cn: 主动买入成交额
                      B:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 忽略
              example:
                e: kline
                E: 1773111055144
                s: ALPHA_116USDT
                k:
                  t: 1773111000000
                  T: 1773111059999
                  s: ALPHA_116USDT
                  i: 1m
                  f: 19912696
                  L: 19912765
                  o: "8.40000000"
                  c: "8.40000000"
                  h: "8.40000000"
                  l: "8.40000000"
                  v: "63.64876300"
                  "n": 218
                  x: false
                  q: "534.64960920"
                  V: "63.64876300"
                  Q: "534.64960920"
                  B: "0"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@kline_1m
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: kline
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773111055144
                        description: eventTime
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            format: int64
                            example: 1773111000000
                            description: startTime
                            x-description-cn: K 线开始时间
                          T:
                            type: integer
                            format: int64
                            example: 1773111059999
                            description: endTime
                            x-description-cn: K 线结束时间
                          s:
                            type: string
                            example: ALPHA_116USDT
                            description: symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: interval
                            x-description-cn: K 线周期
                          f:
                            type: integer
                            format: int64
                            example: 19912696
                            description: firstTradeId
                            x-description-cn: 首笔成交 ID
                          L:
                            type: integer
                            format: int64
                            example: 19912765
                            description: lastTradeId
                            x-description-cn: 末笔成交 ID
                          o:
                            type: string
                            example: "8.40000000"
                            description: openPrice
                            x-description-cn: 开盘价
                          c:
                            type: string
                            example: "8.40000000"
                            description: closePrice
                            x-description-cn: 收盘价
                          h:
                            type: string
                            example: "8.40000000"
                            description: highPrice
                            x-description-cn: 最高价
                          l:
                            type: string
                            example: "8.40000000"
                            description: lowPrice
                            x-description-cn: 最低价
                          v:
                            type: string
                            example: "63.64876300"
                            description: volume
                            x-description-cn: 成交量
                          "n":
                            type: integer
                            format: int64
                            example: 218
                            description: tradeNum
                            x-description-cn: 成交笔数
                          x:
                            type: boolean
                            example: false
                            description: klineComplete
                            x-description-cn: K 线是否已完结
                          q:
                            type: string
                            example: "534.64960920"
                            description: quoteAssetVolume
                            x-description-cn: 成交额
                          V:
                            type: string
                            example: "63.64876300"
                            description: takerBuyBaseAssetVolume
                            x-description-cn: 主动买入成交量
                          Q:
                            type: string
                            example: "534.64960920"
                            description: takerBuyQuoteAssetVolume
                            x-description-cn: 主动买入成交额
                          B:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 忽略
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@kline_1m
                data:
                  e: kline
                  E: 1773111055144
                  s: ALPHA_116USDT
                  k:
                    t: 1773111000000
                    T: 1773111059999
                    s: ALPHA_116USDT
                    i: 1m
                    f: 19912696
                    L: 19912765
                    o: "8.40000000"
                    c: "8.40000000"
                    h: "8.40000000"
                    l: "8.40000000"
                    v: "63.64876300"
                    "n": 218
                    x: false
                    q: "534.64960920"
                    V: "63.64876300"
                    Q: "534.64960920"
                    B: "0"
  /came@{contractAddress}@{chainId}@kline_{interval}:
    post:
      summary: Contract Kline Stream
      x-summary-cn: 合约地址 K 线流
      description: Pushes kline updates by contractAddress@chainId.
      x-description-cn: 按 contractAddress@chainId 推送 K 线更新。
      operationId: contractKlineStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#contract-kline-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/contractKlineStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/contract_kline_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/contract_kline_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/ContractKlineStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/ContractKlineStream/ContractKlineStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: contractAddress
          in: path
          required: true
          schema:
            type: string
            example: G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG
          description: Contract address.
          x-description-cn: 合约地址。
        - name: chainId
          in: path
          required: true
          schema:
            type: string
            example: CT_501
          description: Chain ID.
          x-description-cn: 链 ID。
        - name: interval
          in: path
          required: true
          schema:
            type: string
            example: 1s
            enum:
              - 1s
              - 1m
              - 5m
              - 15m
              - 1h
              - 4h
              - 1d
          description: Kline interval.
          x-description-cn: K 线间隔。
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
                    - came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s
              id: 532601580
      responses:
        Raw Stream:
          description: Contract Kline Stream
          x-description-cn: 合约地址 K 线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  ca:
                    type: string
                    example: G7vQW...@CT_501
                    description: Contract address@Chain ID
                    x-description-cn: 合约地址@链ID
                  e:
                    type: string
                    example: kline
                    description: Event type
                    x-description-cn: 事件类型
                  k:
                    type: object
                    description: Kline payload
                    x-description-cn: K 线数据
                    properties:
                      o:
                        type: string
                        example: "0.15584372258086979622"
                        description: Open price
                        x-description-cn: 开盘价
                      c:
                        type: string
                        example: "0.15584957424118055058"
                        description: Close price
                        x-description-cn: 收盘价
                      h:
                        type: string
                        example: "0.15584957424118055058"
                        description: High price
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "0.15584372258086979622"
                        description: Low price
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "2.8584092999332775480"
                        description: Volume
                        x-description-cn: 成交量
                      ot:
                        type: integer
                        format: int64
                        example: 1771828655000
                        description: Kline open time
                        x-description-cn: k线开始时间
                      ct:
                        type: integer
                        format: int64
                        example: 1771828656000
                        description: Kline close time
                        x-description-cn: k线结束时间
                      i:
                        type: string
                        example: 1s
                        description: Interval
                        x-description-cn: 周期
              example:
                ca: G7vQW...@CT_501
                e: kline
                k:
                  o: "0.15584372258086979622"
                  c: "0.15584957424118055058"
                  h: "0.15584957424118055058"
                  l: "0.15584372258086979622"
                  v: "2.8584092999332775480"
                  ot: 1771828655000
                  ct: 1771828656000
                  i: 1s
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s
                  data:
                    type: object
                    properties:
                      ca:
                        type: string
                        example: G7vQW...@CT_501
                        description: Contract address@Chain ID
                        x-description-cn: 合约地址@链ID
                      e:
                        type: string
                        example: kline
                        description: Event type
                        x-description-cn: 事件类型
                      k:
                        type: object
                        description: Kline payload
                        x-description-cn: K 线数据
                        properties:
                          o:
                            type: string
                            example: "0.15584372258086979622"
                            description: Open price
                            x-description-cn: 开盘价
                          c:
                            type: string
                            example: "0.15584957424118055058"
                            description: Close price
                            x-description-cn: 收盘价
                          h:
                            type: string
                            example: "0.15584957424118055058"
                            description: High price
                            x-description-cn: 最高价
                          l:
                            type: string
                            example: "0.15584372258086979622"
                            description: Low price
                            x-description-cn: 最低价
                          v:
                            type: string
                            example: "2.8584092999332775480"
                            description: Volume
                            x-description-cn: 成交量
                          ot:
                            type: integer
                            format: int64
                            example: 1771828655000
                            description: Kline open time
                            x-description-cn: k线开始时间
                          ct:
                            type: integer
                            format: int64
                            example: 1771828656000
                            description: Kline close time
                            x-description-cn: k线结束时间
                          i:
                            type: string
                            example: 1s
                            description: Interval
                            x-description-cn: 周期
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: came@g7vqwurmkmmm2du3izpxyftht9biio4f4gzcrwfpknwg@ct_501@kline_1s
                data:
                  ca: G7vQW...@CT_501
                  e: kline
                  k:
                    o: "0.15584372258086979622"
                    c: "0.15584957424118055058"
                    h: "0.15584957424118055058"
                    l: "0.15584372258086979622"
                    v: "2.8584092999332775480"
                    ot: 1771828655000
                    ct: 1771828656000
                    i: 1s
  /{symbol}@miniTicker:
    post:
      summary: Mini Ticker Stream
      x-summary-cn: 简略行情流
      description: Pushes 24h rolling mini ticker statistics.
      x-description-cn: 推送 24 小时滚动简略行情统计。
      operationId: miniTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#mini-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/miniTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/mini_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/mini_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/MiniTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/MiniTickerStream/MiniTickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
                    - alpha_116usdt@miniTicker
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@miniTicker
              id: 532601580
      responses:
        Raw Stream:
          description: Mini Ticker Stream
          x-description-cn: 简略行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrMiniTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773109449908
                    description: eventTime
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  c:
                    type: string
                    example: "8.40000000"
                    description: closePrice
                    x-description-cn: 收盘价
                  o:
                    type: string
                    example: "8.40000000"
                    description: openPrice
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "8.50000000"
                    description: highPrice
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "8.30000000"
                    description: lowPrice
                    x-description-cn: 最低价
                  v:
                    type: string
                    example: "64739.03978900"
                    description: volume
                    x-description-cn: 基础资产成交量
                  q:
                    type: string
                    example: "543810.36005090"
                    description: quoteVolume
                    x-description-cn: 计价资产成交额
              example:
                e: 24hrMiniTicker
                E: 1773109449908
                s: ALPHA_116USDT
                c: "8.40000000"
                o: "8.40000000"
                h: "8.50000000"
                l: "8.30000000"
                v: "64739.03978900"
                q: "543810.36005090"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@miniTicker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrMiniTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773109449908
                        description: eventTime
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      c:
                        type: string
                        example: "8.40000000"
                        description: closePrice
                        x-description-cn: 收盘价
                      o:
                        type: string
                        example: "8.40000000"
                        description: openPrice
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "8.50000000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "8.30000000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "64739.03978900"
                        description: volume
                        x-description-cn: 基础资产成交量
                      q:
                        type: string
                        example: "543810.36005090"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@miniTicker
                data:
                  e: 24hrMiniTicker
                  E: 1773109449908
                  s: ALPHA_116USDT
                  c: "8.40000000"
                  o: "8.40000000"
                  h: "8.50000000"
                  l: "8.30000000"
                  v: "64739.03978900"
                  q: "543810.36005090"
  /{symbol}@ticker:
    post:
      summary: Ticker Stream
      x-summary-cn: 完整行情流
      description: Pushes full 24h rolling ticker statistics.
      x-description-cn: 推送完整 24 小时滚动行情统计。
      operationId: tickerStream
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/tickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/TickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/TickerStream/TickerStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
                    - alpha_116usdt@ticker
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@ticker
              id: 532601580
      responses:
        Raw Stream:
          description: Ticker Stream
          x-description-cn: 完整行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrTicker
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773109631569
                    description: eventTime
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "0.00000000"
                    description: priceChange
                    x-description-cn: 涨跌额
                  P:
                    type: string
                    example: "0.00"
                    description: priceChangePercent
                    x-description-cn: 涨跌幅
                  w:
                    type: string
                    example: "8.40003127"
                    description: averagePrice
                    x-description-cn: 平均价
                  c:
                    type: string
                    example: "8.40000000"
                    description: closePrice
                    x-description-cn: 收盘价
                  Q:
                    type: string
                    example: "0.49293200"
                    description: lastTradeVolume
                    x-description-cn: 最近一笔成交量
                  o:
                    type: string
                    example: "8.40000000"
                    description: openPrice
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "8.50000000"
                    description: highPrice
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "8.30000000"
                    description: lowPrice
                    x-description-cn: 最低价
                  v:
                    type: string
                    example: "64750.63418500"
                    description: volume
                    x-description-cn: 基础资产成交量
                  q:
                    type: string
                    example: "543907.35169250"
                    description: quoteVolume
                    x-description-cn: 计价资产成交额
                  O:
                    type: integer
                    format: int64
                    example: 1773023220000
                    description: startTime
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    format: int64
                    example: 1773109631555
                    description: endTime
                    x-description-cn: 统计结束时间
                  F:
                    type: integer
                    format: int64
                    example: 19847634
                    description: firstTradeId
                    x-description-cn: 首笔成交 ID
                  L:
                    type: integer
                    format: int64
                    example: 19911287
                    description: lastTradeId
                    x-description-cn: 末笔成交 ID
                  "n":
                    type: integer
                    format: int64
                    example: 217505
                    description: tradeNum
                    x-description-cn: 成交笔数
              example:
                e: 24hrTicker
                E: 1773109631569
                s: ALPHA_116USDT
                p: "0.00000000"
                P: "0.00"
                w: "8.40003127"
                c: "8.40000000"
                Q: "0.49293200"
                o: "8.40000000"
                h: "8.50000000"
                l: "8.30000000"
                v: "64750.63418500"
                q: "543907.35169250"
                O: 1773023220000
                C: 1773109631555
                F: 19847634
                L: 19911287
                "n": 217505
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@ticker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrTicker
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773109631569
                        description: eventTime
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "0.00000000"
                        description: priceChange
                        x-description-cn: 涨跌额
                      P:
                        type: string
                        example: "0.00"
                        description: priceChangePercent
                        x-description-cn: 涨跌幅
                      w:
                        type: string
                        example: "8.40003127"
                        description: averagePrice
                        x-description-cn: 平均价
                      c:
                        type: string
                        example: "8.40000000"
                        description: closePrice
                        x-description-cn: 收盘价
                      Q:
                        type: string
                        example: "0.49293200"
                        description: lastTradeVolume
                        x-description-cn: 最近一笔成交量
                      o:
                        type: string
                        example: "8.40000000"
                        description: openPrice
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "8.50000000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "8.30000000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "64750.63418500"
                        description: volume
                        x-description-cn: 基础资产成交量
                      q:
                        type: string
                        example: "543907.35169250"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                      O:
                        type: integer
                        format: int64
                        example: 1773023220000
                        description: startTime
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        format: int64
                        example: 1773109631555
                        description: endTime
                        x-description-cn: 统计结束时间
                      F:
                        type: integer
                        format: int64
                        example: 19847634
                        description: firstTradeId
                        x-description-cn: 首笔成交 ID
                      L:
                        type: integer
                        format: int64
                        example: 19911287
                        description: lastTradeId
                        x-description-cn: 末笔成交 ID
                      "n":
                        type: integer
                        format: int64
                        example: 217505
                        description: tradeNum
                        x-description-cn: 成交笔数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@ticker
                data:
                  e: 24hrTicker
                  E: 1773109631569
                  s: ALPHA_116USDT
                  p: "0.00000000"
                  P: "0.00"
                  w: "8.40003127"
                  c: "8.40000000"
                  Q: "0.49293200"
                  o: "8.40000000"
                  h: "8.50000000"
                  l: "8.30000000"
                  v: "64750.63418500"
                  q: "543907.35169250"
                  O: 1773023220000
                  C: 1773109631555
                  F: 19847634
                  L: 19911287
                  "n": 217505
  /{symbol}@trade:
    post:
      summary: Trade Stream
      x-summary-cn: 逐笔成交流
      description: Pushes raw trade updates for a symbol.
      x-description-cn: 推送指定交易对的逐笔成交更新。
      operationId: tradeStream
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/ws-streams/~#trade-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/alpha/examples/websocket-streams/tradeStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/alpha/websocket_streams/trade_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/alpha/examples/websocket_streams/trade_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/alpha/src/main/java/com/binance/connector/client/alpha/websocket/stream/defaultpkg/TradeStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/alpha/examples/websocketstreams/DefaultAPI/TradeStream/TradeStream.go
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: alpha_116usdt
          description: Symbol to subscribe, in lowercase stream format.
          x-description-cn: 要订阅的交易对（流中使用小写格式）。
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
                    - alpha_116usdt@trade
                id:
                  type: integer
                  example: 532601580
                  format: int32
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
                - alpha_116usdt@trade
              id: 532601580
      responses:
        Raw Stream:
          description: Trade Stream
          x-description-cn: 逐笔成交流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: trade
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    format: int64
                    example: 1773110023891
                    description: eventTime
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    format: int64
                    example: 1773110023877
                    description: tradeTime
                    x-description-cn: 成交时间
                  s:
                    type: string
                    example: ALPHA_116USDT
                    description: symbol
                    x-description-cn: 交易对
                  t:
                    type: integer
                    format: int64
                    example: 19911650
                    description: tradeId
                    x-description-cn: 成交 ID
                  p:
                    type: string
                    example: "8.40000000"
                    description: fillPrice
                    x-description-cn: 成交价
                  q:
                    type: string
                    example: "0.97915700"
                    description: fillQty
                    x-description-cn: 成交量
                  m:
                    type: boolean
                    example: false
                    description: isBuyerMaker
                    x-description-cn: 是否为买方挂单成交
              example:
                e: trade
                E: 1773110023891
                T: 1773110023877
                s: ALPHA_116USDT
                t: 19911650
                p: "8.40000000"
                q: "0.97915700"
                m: false
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: alpha_116usdt@trade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: trade
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        format: int64
                        example: 1773110023891
                        description: eventTime
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        format: int64
                        example: 1773110023877
                        description: tradeTime
                        x-description-cn: 成交时间
                      s:
                        type: string
                        example: ALPHA_116USDT
                        description: symbol
                        x-description-cn: 交易对
                      t:
                        type: integer
                        format: int64
                        example: 19911650
                        description: tradeId
                        x-description-cn: 成交 ID
                      p:
                        type: string
                        example: "8.40000000"
                        description: fillPrice
                        x-description-cn: 成交价
                      q:
                        type: string
                        example: "0.97915700"
                        description: fillQty
                        x-description-cn: 成交量
                      m:
                        type: boolean
                        example: false
                        description: isBuyerMaker
                        x-description-cn: 是否为买方挂单成交
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: alpha_116usdt@trade
                data:
                  e: trade
                  E: 1773110023891
                  T: 1773110023877
                  s: ALPHA_116USDT
                  t: 19911650
                  p: "8.40000000"
                  q: "0.97915700"
                  m: false
```