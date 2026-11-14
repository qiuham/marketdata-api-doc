---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:37.819923
---

# core-trading-derivatives-trading-coin-m-futures__ws-streams spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Futures (COIN-M) WebSocket Market Streams
  description: Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.
  x-description-cn: 访问市场数据、管理账户，并交易 COIN-M 永续合约和交割合约。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-streams
x-untagged-label: true
x-user-data-streams: true
externalDocs:
  description: Futures (COIN-M) docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/general-info
servers:
  - url: wss://dstream.binance.com
  - url: wss://dstream.binancefuture.com
paths:
  /{symbol}@aggTrade:
    post:
      summary: Aggregate Trade Streams
      x-summary-cn: 归集交易
      description: >-
        The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and
        taking side every 100 milliseconds.


        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        归集成交流推送市场成交信息, 每100毫秒为一个时间窗口, 将同一价格和买卖方向的成交进行归集。

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: aggregateTradeStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#aggregate-trade-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/aggregateTradeStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/aggregate_trade_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/aggregate_trade_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/AggregateTradeStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/AggregateTradeStreams/AggregateTradeStreams.go
      x-update-speed: 100ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
                    - btcusdt@aggTrade
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
                - btcusdt@aggTrade
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Aggregate Trade Streams
          x-description-cn: 归集成交流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: aggTrade
                    enum:
                      - aggTrade
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591261134288
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  a:
                    type: integer
                    example: 424951
                    format: int64
                    description: Aggregate trade ID
                    x-description-cn: 归集成交ID
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "9643.5"
                    description: Price
                    x-description-cn: 成交价格
                  q:
                    type: string
                    example: "2"
                    description: Quantity
                    x-description-cn: 成交量
                  f:
                    type: integer
                    example: 606073
                    format: int64
                    description: First trade ID
                    x-description-cn: 被归集的首个交易ID
                  l:
                    type: integer
                    example: 606073
                    format: int64
                    description: Last trade ID
                    x-description-cn: 被归集的末次交易ID
                  T:
                    type: integer
                    example: 1591261134199
                    format: int64
                    description: Trade time
                    x-description-cn: 成交时间
                  m:
                    type: boolean
                    example: false
                    description: Is the buyer the market maker?
                    x-description-cn: 买方是否是做市方。如true,则此次成交是一个主动卖出单,否则是一个主动买入单。
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: aggTrade
                E: 1591261134288
                a: 424951
                s: BTCUSD_200626
                p: "9643.5"
                q: "2"
                f: 606073
                l: 606073
                T: 1591261134199
                m: false
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@aggTrade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: aggTrade
                        enum:
                          - aggTrade
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591261134288
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      a:
                        type: integer
                        example: 424951
                        format: int64
                        description: Aggregate trade ID
                        x-description-cn: 归集成交ID
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "9643.5"
                        description: Price
                        x-description-cn: 成交价格
                      q:
                        type: string
                        example: "2"
                        description: Quantity
                        x-description-cn: 成交量
                      f:
                        type: integer
                        example: 606073
                        format: int64
                        description: First trade ID
                        x-description-cn: 被归集的首个交易ID
                      l:
                        type: integer
                        example: 606073
                        format: int64
                        description: Last trade ID
                        x-description-cn: 被归集的末次交易ID
                      T:
                        type: integer
                        example: 1591261134199
                        format: int64
                        description: Trade time
                        x-description-cn: 成交时间
                      m:
                        type: boolean
                        example: false
                        description: Is the buyer the market maker?
                        x-description-cn: 买方是否是做市方。如true,则此次成交是一个主动卖出单,否则是一个主动买入单。
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@aggTrade
                data:
                  e: aggTrade
                  E: 1591261134288
                  a: 424951
                  s: BTCUSD_200626
                  p: "9643.5"
                  q: "2"
                  f: 606073
                  l: 606073
                  T: 1591261134199
                  m: false
                  st: 1
  /!bookTicker:
    post:
      summary: All Book Tickers Stream
      x-summary-cn: 全市场最优挂单信息
      description: >-
        Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.


        > **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and
        `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        实时推送所有交易对的最优挂单价格或数量的任何更新。

        > **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: allBookTickersStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#all-book-tickers-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/allBookTickersStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/all_book_tickers_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/all_book_tickers_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/AllBookTickersStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/AllBookTickersStream/AllBookTickersStream.go
      x-update-speed: Real-time
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
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
                - "!bookTicker"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: All Book Tickers Stream
          x-description-cn: 全市场最优挂单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: bookTicker
                    enum:
                      - bookTicker
                    description: Event type
                    x-description-cn: 事件类型
                  u:
                    type: integer
                    example: 17242169
                    format: int64
                    description: Order book update Id
                    x-description-cn: 更新ID
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "9548.1"
                    description: Best bid price
                    x-description-cn: 买单最优挂单价格
                  B:
                    type: string
                    example: "52"
                    description: Best bid qty
                    x-description-cn: 买单最优挂单数量
                  a:
                    type: string
                    example: "9548.5"
                    description: Best ask price
                    x-description-cn: 卖单最优挂单价格
                  A:
                    type: string
                    example: "11"
                    description: Best ask qty
                    x-description-cn: 卖单最优挂单数量
                  T:
                    type: integer
                    example: 1591268628155
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合时间
                  E:
                    type: integer
                    example: 1591268628166
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: bookTicker
                u: 17242169
                s: BTCUSD_200626
                b: "9548.1"
                B: "52"
                a: "9548.5"
                A: "11"
                T: 1591268628155
                E: 1591268628166
                ps: BTCUSD
                st: 1
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
                        enum:
                          - bookTicker
                        description: Event type
                        x-description-cn: 事件类型
                      u:
                        type: integer
                        example: 17242169
                        format: int64
                        description: Order book update Id
                        x-description-cn: 更新ID
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "9548.1"
                        description: Best bid price
                        x-description-cn: 买单最优挂单价格
                      B:
                        type: string
                        example: "52"
                        description: Best bid qty
                        x-description-cn: 买单最优挂单数量
                      a:
                        type: string
                        example: "9548.5"
                        description: Best ask price
                        x-description-cn: 卖单最优挂单价格
                      A:
                        type: string
                        example: "11"
                        description: Best ask qty
                        x-description-cn: 卖单最优挂单数量
                      T:
                        type: integer
                        example: 1591268628155
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合时间
                      E:
                        type: integer
                        example: 1591268628166
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!bookTicker"
                data:
                  e: bookTicker
                  u: 17242169
                  s: BTCUSD_200626
                  b: "9548.1"
                  B: "52"
                  a: "9548.5"
                  A: "11"
                  T: 1591268628155
                  E: 1591268628166
                  ps: BTCUSD
                  st: 1
  /!forceOrder@arr:
    post:
      summary: All Market Liquidation Order Streams
      x-summary-cn: 全市场强平订单
      description: >-
        The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the
        market. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If
        no liquidation happens in the interval of 1000ms, no stream will be pushed.


        > **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and
        `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        全市场强平订单快照流推送全市场所有交易对的强平订单信息。每个交易对在 1000ms 内只会推送最新的一笔强平订单作为快照，如果 1000ms 内没有发生强平，则不会推送任何流。

        > **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: allMarketLiquidationOrderStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#all-market-liquidation-order-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/allMarketLiquidationOrderStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/all_market_liquidation_order_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/all_market_liquidation_order_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/AllMarketLiquidationOrderStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/AllMarketLiquidationOrderStreams/AllMarketLiquidationOrderStreams.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
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
                    - "!forceOrder@arr"
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
                - "!forceOrder@arr"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: All Market Liquidation Order Streams
          x-description-cn: 全市场强平订单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: forceOrder
                    enum:
                      - forceOrder
                    description: Event Type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591154240950
                    format: int64
                    description: Event Time
                    x-description-cn: 事件时间
                  o:
                    type: object
                    properties:
                      s:
                        type: string
                        example: BTCUSD_200925
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      S:
                        type: string
                        example: SELL
                        description: Side
                        x-description-cn: 订单方向
                      o:
                        type: string
                        example: LIMIT
                        description: Order Type
                        x-description-cn: 订单类型
                      f:
                        type: string
                        example: IOC
                        description: Time in Force
                        x-description-cn: 有效方式
                      q:
                        type: string
                        example: "1"
                        description: Original Quantity
                        x-description-cn: 订单数量
                      p:
                        type: string
                        example: "9425.5"
                        description: Price
                        x-description-cn: 订单价格
                      ap:
                        type: string
                        example: "9496.5"
                        description: Average Price
                        x-description-cn: 平均价格
                      X:
                        type: string
                        example: FILLED
                        description: Order Status
                        x-description-cn: 订单状态
                      l:
                        type: string
                        example: "1"
                        description: Order Last Filled Quantity
                        x-description-cn: 订单最近成交量
                      z:
                        type: string
                        example: "1"
                        description: Order Filled Accumulated Quantity
                        x-description-cn: 订单累计成交量
                      T:
                        type: integer
                        example: 1591154240949
                        format: int64
                        description: Order Trade Time
                        x-description-cn: 交易时间
                    description: Order Type
                    x-description-cn: 订单类型
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: forceOrder
                E: 1591154240950
                o:
                  s: BTCUSD_200925
                  ps: BTCUSD
                  S: SELL
                  o: LIMIT
                  f: IOC
                  q: "1"
                  p: "9425.5"
                  ap: "9496.5"
                  X: FILLED
                  l: "1"
                  z: "1"
                  T: 1591154240949
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!forceOrder@arr"
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: forceOrder
                        enum:
                          - forceOrder
                        description: Event Type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591154240950
                        format: int64
                        description: Event Time
                        x-description-cn: 事件时间
                      o:
                        type: object
                        properties:
                          s:
                            type: string
                            example: BTCUSD_200925
                            description: Symbol
                            x-description-cn: 交易对
                          ps:
                            type: string
                            example: BTCUSD
                            description: Pair
                            x-description-cn: 标的交易对
                          S:
                            type: string
                            example: SELL
                            description: Side
                            x-description-cn: 订单方向
                          o:
                            type: string
                            example: LIMIT
                            description: Order Type
                            x-description-cn: 订单类型
                          f:
                            type: string
                            example: IOC
                            description: Time in Force
                            x-description-cn: 有效方式
                          q:
                            type: string
                            example: "1"
                            description: Original Quantity
                            x-description-cn: 订单数量
                          p:
                            type: string
                            example: "9425.5"
                            description: Price
                            x-description-cn: 订单价格
                          ap:
                            type: string
                            example: "9496.5"
                            description: Average Price
                            x-description-cn: 平均价格
                          X:
                            type: string
                            example: FILLED
                            description: Order Status
                            x-description-cn: 订单状态
                          l:
                            type: string
                            example: "1"
                            description: Order Last Filled Quantity
                            x-description-cn: 订单最近成交量
                          z:
                            type: string
                            example: "1"
                            description: Order Filled Accumulated Quantity
                            x-description-cn: 订单累计成交量
                          T:
                            type: integer
                            example: 1591154240949
                            format: int64
                            description: Order Trade Time
                            x-description-cn: 交易时间
                        description: Order Type
                        x-description-cn: 订单类型
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!forceOrder@arr"
                data:
                  e: forceOrder
                  E: 1591154240950
                  o:
                    s: BTCUSD_200925
                    ps: BTCUSD
                    S: SELL
                    o: LIMIT
                    f: IOC
                    q: "1"
                    p: "9425.5"
                    ap: "9496.5"
                    X: FILLED
                    l: "1"
                    z: "1"
                    T: 1591154240949
                  st: 1
  /!miniTicker@arr:
    post:
      summary: All Market Mini Tickers Stream
      x-summary-cn: 全市场的精简Ticker
      description: >-
        24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a
        24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present
        in the array.


        > **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and
        `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        所有交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计数据，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

        > **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: allMarketMiniTickersStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#all-market-mini-tickers-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/allMarketMiniTickersStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/all_market_mini_tickers_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/all_market_mini_tickers_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/AllMarketMiniTickersStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/AllMarketMiniTickersStream/AllMarketMiniTickersStream.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
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
          x-description-cn: 全市场精简行情流
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
                      enum:
                        - 24hrMiniTicker
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      example: 1591267704450
                      format: int64
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: BTCUSD_200626
                      description: Symbol
                      x-description-cn: 交易对
                    ps:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    c:
                      type: string
                      example: "9561.7"
                      description: Close price
                      x-description-cn: 最新成交价格
                    o:
                      type: string
                      example: "9580.9"
                      description: Open price
                      x-description-cn: 24小时前开始第一笔成交价格
                    h:
                      type: string
                      example: "10000.0"
                      description: High price
                      x-description-cn: 24小时内最高成交价
                    l:
                      type: string
                      example: "7000.0"
                      description: Low price
                      x-description-cn: 24小时内最低成交价
                    v:
                      type: string
                      example: "487476"
                      description: Total traded volume
                      x-description-cn: 24小时成交量
                    q:
                      type: string
                      example: "33264343847.22378500"
                      description: Total traded base asset volume
                      x-description-cn: 24小时成交额(标的数量)
                    st:
                      type: integer
                      example: 1
                      description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                      x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                - e: 24hrMiniTicker
                  E: 1591267704450
                  s: BTCUSD_200626
                  ps: BTCUSD
                  c: "9561.7"
                  o: "9580.9"
                  h: "10000.0"
                  l: "7000.0"
                  v: "487476"
                  q: "33264343847.22378500"
                  st: 1
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
                          enum:
                            - 24hrMiniTicker
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          example: 1591267704450
                          format: int64
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: BTCUSD_200626
                          description: Symbol
                          x-description-cn: 交易对
                        ps:
                          type: string
                          example: BTCUSD
                          description: Pair
                          x-description-cn: 标的交易对
                        c:
                          type: string
                          example: "9561.7"
                          description: Close price
                          x-description-cn: 最新成交价格
                        o:
                          type: string
                          example: "9580.9"
                          description: Open price
                          x-description-cn: 24小时前开始第一笔成交价格
                        h:
                          type: string
                          example: "10000.0"
                          description: High price
                          x-description-cn: 24小时内最高成交价
                        l:
                          type: string
                          example: "7000.0"
                          description: Low price
                          x-description-cn: 24小时内最低成交价
                        v:
                          type: string
                          example: "487476"
                          description: Total traded volume
                          x-description-cn: 24小时成交量
                        q:
                          type: string
                          example: "33264343847.22378500"
                          description: Total traded base asset volume
                          x-description-cn: 24小时成交额(标的数量)
                        st:
                          type: integer
                          example: 1
                          description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                          x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!miniTicker@arr"
                data:
                  - e: 24hrMiniTicker
                    E: 1591267704450
                    s: BTCUSD_200626
                    ps: BTCUSD
                    c: "9561.7"
                    o: "9580.9"
                    h: "10000.0"
                    l: "7000.0"
                    v: "487476"
                    q: "33264343847.22378500"
                    st: 1
  /!ticker@arr:
    post:
      summary: All Market Tickers Streams
      x-summary-cn: 全市场的完整Ticker
      description: >-
        24hr rolling window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr
        rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the
        array.


        > **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and
        `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        24小时滚动窗口的所有交易对的Ticker统计。这些不是UTC日的统计，而是从请求时间到24小时前的24小时滚动窗口。请注意，只有发生变化的Ticker才会出现在数组中。

        > **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: allMarketTickersStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#all-market-tickers-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/allMarketTickersStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/all_market_tickers_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/all_market_tickers_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/AllMarketTickersStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/AllMarketTickersStreams/AllMarketTickersStreams.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
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
                - "!ticker@arr"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: All Market Tickers Streams
          x-description-cn: 全市场行情流
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: 24hrTicker
                      enum:
                        - 24hrTicker
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      example: 1591268262453
                      format: int64
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: BTCUSD_200626
                      description: Symbol
                      x-description-cn: 交易对
                    p:
                      type: string
                      example: "-43.4"
                      description: Price change
                      x-description-cn: 24小时价格变化
                    P:
                      type: string
                      example: "-0.452"
                      description: Price change percent
                      x-description-cn: 24小时价格变化(百分比)
                    w:
                      type: string
                      example: "0.00147974"
                      description: Weighted average price
                      x-description-cn: 24小时平均价格
                    c:
                      type: string
                      example: "9548.5"
                      description: Last price
                      x-description-cn: 最新成交价格
                    Q:
                      type: string
                      example: "2"
                      description: Last quantity
                      x-description-cn: 最新成交价格上的成交量
                    o:
                      type: string
                      example: "9591.9"
                      description: Open price
                      x-description-cn: 24小时前第一笔成交价格
                    h:
                      type: string
                      example: "10000.0"
                      description: High price
                      x-description-cn: 24小时内最高成交价
                    l:
                      type: string
                      example: "7000.0"
                      description: Low price
                      x-description-cn: 24小时内最低成交价
                    v:
                      type: string
                      example: "487850"
                      description: Total traded volume
                      x-description-cn: 24小时成交量
                    q:
                      type: string
                      example: "32968676323.46222700"
                      description: Total traded base asset volume
                      x-description-cn: 24小时成交额(标的数量)
                    O:
                      type: integer
                      example: 1591181820000
                      format: int64
                      description: Statistics open time
                      x-description-cn: 统计开始时间
                    C:
                      type: integer
                      example: 1591268262442
                      format: int64
                      description: Statistics close time
                      x-description-cn: 统计关闭时间
                    F:
                      type: integer
                      example: 512014
                      format: int64
                      description: First trade ID
                      x-description-cn: 24小时内第一笔成交交易ID
                    L:
                      type: integer
                      example: 615289
                      format: int64
                      description: Last trade Id
                      x-description-cn: 24小时内最后一笔成交交易ID
                    "n":
                      type: integer
                      example: 103272
                      format: int64
                      description: Total number of trades
                      x-description-cn: 24小时内成交数
                    ps:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    st:
                      type: integer
                      example: 1
                      description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                      x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                - e: 24hrTicker
                  E: 1591268262453
                  s: BTCUSD_200626
                  p: "-43.4"
                  P: "-0.452"
                  w: "0.00147974"
                  c: "9548.5"
                  Q: "2"
                  o: "9591.9"
                  h: "10000.0"
                  l: "7000.0"
                  v: "487850"
                  q: "32968676323.46222700"
                  O: 1591181820000
                  C: 1591268262442
                  F: 512014
                  L: 615289
                  "n": 103272
                  ps: BTCUSD
                  st: 1
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
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: 24hrTicker
                          enum:
                            - 24hrTicker
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          example: 1591268262453
                          format: int64
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: BTCUSD_200626
                          description: Symbol
                          x-description-cn: 交易对
                        p:
                          type: string
                          example: "-43.4"
                          description: Price change
                          x-description-cn: 24小时价格变化
                        P:
                          type: string
                          example: "-0.452"
                          description: Price change percent
                          x-description-cn: 24小时价格变化(百分比)
                        w:
                          type: string
                          example: "0.00147974"
                          description: Weighted average price
                          x-description-cn: 24小时平均价格
                        c:
                          type: string
                          example: "9548.5"
                          description: Last price
                          x-description-cn: 最新成交价格
                        Q:
                          type: string
                          example: "2"
                          description: Last quantity
                          x-description-cn: 最新成交价格上的成交量
                        o:
                          type: string
                          example: "9591.9"
                          description: Open price
                          x-description-cn: 24小时前第一笔成交价格
                        h:
                          type: string
                          example: "10000.0"
                          description: High price
                          x-description-cn: 24小时内最高成交价
                        l:
                          type: string
                          example: "7000.0"
                          description: Low price
                          x-description-cn: 24小时内最低成交价
                        v:
                          type: string
                          example: "487850"
                          description: Total traded volume
                          x-description-cn: 24小时成交量
                        q:
                          type: string
                          example: "32968676323.46222700"
                          description: Total traded base asset volume
                          x-description-cn: 24小时成交额(标的数量)
                        O:
                          type: integer
                          example: 1591181820000
                          format: int64
                          description: Statistics open time
                          x-description-cn: 统计开始时间
                        C:
                          type: integer
                          example: 1591268262442
                          format: int64
                          description: Statistics close time
                          x-description-cn: 统计关闭时间
                        F:
                          type: integer
                          example: 512014
                          format: int64
                          description: First trade ID
                          x-description-cn: 24小时内第一笔成交交易ID
                        L:
                          type: integer
                          example: 615289
                          format: int64
                          description: Last trade Id
                          x-description-cn: 24小时内最后一笔成交交易ID
                        "n":
                          type: integer
                          example: 103272
                          format: int64
                          description: Total number of trades
                          x-description-cn: 24小时内成交数
                        ps:
                          type: string
                          example: BTCUSD
                          description: Pair
                          x-description-cn: 标的交易对
                        st:
                          type: integer
                          example: 1
                          description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                          x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!ticker@arr"
                data:
                  - e: 24hrTicker
                    E: 1591268262453
                    s: BTCUSD_200626
                    p: "-43.4"
                    P: "-0.452"
                    w: "0.00147974"
                    c: "9548.5"
                    Q: "2"
                    o: "9591.9"
                    h: "10000.0"
                    l: "7000.0"
                    v: "487850"
                    q: "32968676323.46222700"
                    O: 1591181820000
                    C: 1591268262442
                    F: 512014
                    L: 615289
                    "n": 103272
                    ps: BTCUSD
                    st: 1
  /{pair}_{contractType}@continuousKline_{interval}:
    post:
      summary: Continuous Contract Kline/Candlestick Streams
      x-summary-cn: 连续合约K线
      description: |-
        Kline update every second

        > **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.
      x-description-cn: |-
        K线每秒更新

        > **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。
      operationId: continuousContractKlineCandlestickStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#continuous-contract-kline-candlestick-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/continuousContractKlineCandlestickStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/continuous_contract_kline_candlestick_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/continuous_contract_kline_candlestick_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/ContinuousContractKlineCandlestickStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/ContinuousContractKlineCandlestickStreams/ContinuousContractKlineCandlestickStreams.go
      x-update-speed: 250ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: pair
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The pair parameter
          x-description-cn: 交易对参数
        - name: contractType
          in: path
          required: true
          schema:
            type: string
            example: next_quarter
            enum:
              - perpetual
              - current_quarter
              - next_quarter
          description: The contractType parameter
          x-description-cn: The contract 类型 parameter
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
          description: The interval parameter
          x-description-cn: 间隔 参数
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
                    - btcusdt_next_quarter@continuousKline_1m
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
                - btcusdt_next_quarter@continuousKline_1m
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Continuous Contract Kline/Candlestick Streams
          x-description-cn: 连续合约 K线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: continuous_kline
                    enum:
                      - continuous_kline
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591261542539
                    format: int64
                    description: eventTime
                    x-description-cn: 事件时间
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  ct:
                    type: string
                    example: NEXT_QUARTER
                    description: Contract type
                    x-description-cn: 合约类型
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        example: 1591261500000
                        format: int64
                        description: Kline start time
                        x-description-cn: 这根K线的起始时间
                      T:
                        type: integer
                        example: 1591261559999
                        format: int64
                        description: transactionTime
                        x-description-cn: 成交时间/交易时间
                      i:
                        type: string
                        example: 1m
                        description: interval
                        x-description-cn: K 线周期
                      f:
                        type: integer
                        example: 606400
                        format: int64
                        description: First update ID
                        x-description-cn: 第一个更新 ID
                      L:
                        type: integer
                        example: 606430
                        format: int64
                        description: Last update ID
                        x-description-cn: 最后一个更新 ID
                      o:
                        type: string
                        example: "9638.9"
                        description: openPrice
                        x-description-cn: 开盘价
                      c:
                        type: string
                        example: "9639.8"
                        description: closePrice
                        x-description-cn: 收盘价
                      h:
                        type: string
                        example: "9639.8"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "9638.6"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "156"
                        description: volume
                        x-description-cn: 基础资产成交量
                      "n":
                        type: integer
                        example: 31
                        format: int64
                        description: tradeNum
                        x-description-cn: 成交笔数
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                      q:
                        type: string
                        example: "1.61836886"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                      V:
                        type: string
                        example: "73"
                        description: Taker buy volume
                        x-description-cn: 无意义字段
                      Q:
                        type: string
                        example: "0.75731156"
                        description: lastTradeVolume
                        x-description-cn: 最近一笔成交量
                      B:
                        type: string
                        example: "0"
                        description: Best bid qty
                        x-description-cn: 买单最优挂单数量
                    description: Kline payload
                    x-description-cn: K 线数据
              example:
                e: continuous_kline
                E: 1591261542539
                ps: BTCUSD
                ct: NEXT_QUARTER
                k:
                  t: 1591261500000
                  T: 1591261559999
                  i: 1m
                  f: 606400
                  L: 606430
                  o: "9638.9"
                  c: "9639.8"
                  h: "9639.8"
                  l: "9638.6"
                  v: "156"
                  "n": 31
                  x: false
                  q: "1.61836886"
                  V: "73"
                  Q: "0.75731156"
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
                    example: btcusdt_next_quarter@continuousKline_1m
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: continuous_kline
                        enum:
                          - continuous_kline
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591261542539
                        format: int64
                        description: eventTime
                        x-description-cn: 事件时间
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      ct:
                        type: string
                        example: NEXT_QUARTER
                        description: Contract type
                        x-description-cn: 合约类型
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            example: 1591261500000
                            format: int64
                            description: Kline start time
                            x-description-cn: 这根K线的起始时间
                          T:
                            type: integer
                            example: 1591261559999
                            format: int64
                            description: transactionTime
                            x-description-cn: 成交时间/交易时间
                          i:
                            type: string
                            example: 1m
                            description: interval
                            x-description-cn: K 线周期
                          f:
                            type: integer
                            example: 606400
                            format: int64
                            description: First update ID
                            x-description-cn: 第一个更新 ID
                          L:
                            type: integer
                            example: 606430
                            format: int64
                            description: Last update ID
                            x-description-cn: 最后一个更新 ID
                          o:
                            type: string
                            example: "9638.9"
                            description: openPrice
                            x-description-cn: 开盘价
                          c:
                            type: string
                            example: "9639.8"
                            description: closePrice
                            x-description-cn: 收盘价
                          h:
                            type: string
                            example: "9639.8"
                            description: highPrice
                            x-description-cn: 最高价
                          l:
                            type: string
                            example: "9638.6"
                            description: lowPrice
                            x-description-cn: 最低价
                          v:
                            type: string
                            example: "156"
                            description: volume
                            x-description-cn: 基础资产成交量
                          "n":
                            type: integer
                            example: 31
                            format: int64
                            description: tradeNum
                            x-description-cn: 成交笔数
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                          q:
                            type: string
                            example: "1.61836886"
                            description: quoteVolume
                            x-description-cn: 计价资产成交额
                          V:
                            type: string
                            example: "73"
                            description: Taker buy volume
                            x-description-cn: 无意义字段
                          Q:
                            type: string
                            example: "0.75731156"
                            description: lastTradeVolume
                            x-description-cn: 最近一笔成交量
                          B:
                            type: string
                            example: "0"
                            description: Best bid qty
                            x-description-cn: 买单最优挂单数量
                        description: Kline payload
                        x-description-cn: K 线数据
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt_next_quarter@continuousKline_1m
                data:
                  e: continuous_kline
                  E: 1591261542539
                  ps: BTCUSD
                  ct: NEXT_QUARTER
                  k:
                    t: 1591261500000
                    T: 1591261559999
                    i: 1m
                    f: 606400
                    L: 606430
                    o: "9638.9"
                    c: "9639.8"
                    h: "9639.8"
                    l: "9638.6"
                    v: "156"
                    "n": 31
                    x: false
                    q: "1.61836886"
                    V: "73"
                    Q: "0.75731156"
                    B: "0"
  /!contractInfo:
    post:
      summary: Contract Info Stream
      x-summary-cn: 交易对信息信息流
      description: >-
        ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). bks field
        only shows up when bracket gets updated.


        > **After CM migration**, this stream pushes the merged UM + CM universe (subscribable on both `fstream` and
        `dstream`); each payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        ContractInfo 流在合约信息更新时推送（上架/结算/分层更新）。当分层更新时才会出现 bks 字段。

        > **迁移后**,此 stream 推送合并的 UM + CM universe(`fstream` 与 `dstream` 都可订阅);payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: contractInfoStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#contract-info-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/contractInfoStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/contract_info_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/contract_info_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/ContractInfoStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/ContractInfoStream/ContractInfoStream.go
      x-update-speed: Real-time
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
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
                    - "!contractInfo"
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
                - "!contractInfo"
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Contract Info Stream
          x-description-cn: Contract Info 流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: contractInfo
                    enum:
                      - contractInfo
                    description: Event Type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1669647330375
                    format: int64
                    description: Event Time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: APTUSD_PERP
                    description: Symbol
                    x-description-cn: 交易对
                  ps:
                    type: string
                    example: APTUSD
                    description: Pair
                    x-description-cn: 交易对标的
                  ct:
                    type: string
                    example: PERPETUAL
                    description: Contract type
                    x-description-cn: 合约类型
                  dt:
                    type: integer
                    example: 4133404800000
                    format: int64
                    description: Delivery date time
                    x-description-cn: 结算时间
                  ot:
                    type: integer
                    example: 1666594800000
                    format: int64
                    description: onboard date time
                    x-description-cn: 上架时间
                  cs:
                    type: string
                    example: TRADING
                    description: Contract status
                    x-description-cn: 交易对状态
                  bks:
                    type: array
                    items:
                      type: object
                      properties:
                        bs:
                          type: integer
                          example: 1
                          format: int64
                          description: Notional bracket
                          x-description-cn: 层级
                        bnf:
                          type: integer
                          example: 0
                          format: int64
                          description: Floor notional of this bracket
                          x-description-cn: 该层对应的名义价值下限
                        bnc:
                          type: integer
                          example: 500000
                          format: int64
                          description: Cap notional of this bracket
                          x-description-cn: 该层对应的名义价值上限
                        mmr:
                          type: number
                          example: 0.0065
                          format: float
                          description: Maintenance ratio for this bracket
                          x-description-cn: 该层对应的维持保证金率
                        cf:
                          type: integer
                          example: 75
                          format: int64
                          description: Auxiliary number for quick calculation
                          x-description-cn: 速算数
                        mi:
                          type: integer
                          example: 51
                          format: int64
                          description: Min leverage for this bracket
                          x-description-cn: 该层杠杆下界
                        ma:
                          type: integer
                          example: 75
                          format: int64
                          description: Max leverage for this bracket
                          x-description-cn: 该层杠杆上界
                    description: Bracket list.
                    x-description-cn: 分层列表.
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: contractInfo
                E: 1669647330375
                s: APTUSD_PERP
                ps: APTUSD
                ct: PERPETUAL
                dt: 4133404800000
                ot: 1666594800000
                cs: TRADING
                bks:
                  - bs: 1
                    bnf: 0
                    bnc: 500000
                    mmr: 0.0065
                    cf: 75
                    mi: 51
                    ma: 75
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!contractInfo"
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: contractInfo
                        enum:
                          - contractInfo
                        description: Event Type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1669647330375
                        format: int64
                        description: Event Time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: APTUSD_PERP
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: APTUSD
                        description: Pair
                        x-description-cn: 交易对标的
                      ct:
                        type: string
                        example: PERPETUAL
                        description: Contract type
                        x-description-cn: 合约类型
                      dt:
                        type: integer
                        example: 4133404800000
                        format: int64
                        description: Delivery date time
                        x-description-cn: 结算时间
                      ot:
                        type: integer
                        example: 1666594800000
                        format: int64
                        description: onboard date time
                        x-description-cn: 上架时间
                      cs:
                        type: string
                        example: TRADING
                        description: Contract status
                        x-description-cn: 交易对状态
                      bks:
                        type: array
                        items:
                          type: object
                          properties:
                            bs:
                              type: integer
                              example: 1
                              format: int64
                              description: Notional bracket
                              x-description-cn: 层级
                            bnf:
                              type: integer
                              example: 0
                              format: int64
                              description: Floor notional of this bracket
                              x-description-cn: 该层对应的名义价值下限
                            bnc:
                              type: integer
                              example: 500000
                              format: int64
                              description: Cap notional of this bracket
                              x-description-cn: 该层对应的名义价值上限
                            mmr:
                              type: number
                              example: 0.0065
                              format: float
                              description: Maintenance ratio for this bracket
                              x-description-cn: 该层对应的维持保证金率
                            cf:
                              type: integer
                              example: 75
                              format: int64
                              description: Auxiliary number for quick calculation
                              x-description-cn: 速算数
                            mi:
                              type: integer
                              example: 51
                              format: int64
                              description: Min leverage for this bracket
                              x-description-cn: 该层杠杆下界
                            ma:
                              type: integer
                              example: 75
                              format: int64
                              description: Max leverage for this bracket
                              x-description-cn: 该层杠杆上界
                        description: Bracket list.
                        x-description-cn: 分层列表.
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!contractInfo"
                data:
                  e: contractInfo
                  E: 1669647330375
                  s: APTUSD_PERP
                  ps: APTUSD
                  ct: PERPETUAL
                  dt: 4133404800000
                  ot: 1666594800000
                  cs: TRADING
                  bks:
                    - bs: 1
                      bnf: 0
                      bnc: 500000
                      mmr: 0.0065
                      cf: 75
                      mi: 51
                      ma: 75
                  st: 1
  /{symbol}@depth@{updateSpeed}:
    post:
      summary: Diff. Book Depth Streams
      x-summary-cn: 增量深度信息stream
      description: |-
        Bids and asks, pushed every 250 milliseconds, 500 milliseconds, or 100 milliseconds

        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        买单和卖单，每 250ms、500ms 或 100ms 推送一次

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: diffBookDepthStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#diff-book-depth-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/diffBookDepthStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/diff_book_depth_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/diff_book_depth_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/DiffBookDepthStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/DiffBookDepthStreams/DiffBookDepthStreams.go
      x-update-speed: 250ms or 500ms or 100ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
              - 500ms
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度
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
                    - btcusdt@depth@100ms
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
                - btcusdt@depth@100ms
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Diff. Book Depth Streams
          x-description-cn: 增量深度流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    enum:
                      - depthUpdate
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591270260907
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    example: 1591270260891
                    format: int64
                    description: Transction time
                    x-description-cn: 撮合时间
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  U:
                    type: integer
                    example: 17285681
                    format: int64
                    description: First update ID in event
                    x-description-cn: 从上次推送至今新增的第一个 update Id
                  u:
                    type: integer
                    example: 17285702
                    format: int64
                    description: Final update ID in event
                    x-description-cn: 从上次推送至今新增的最后一个 update Id
                  pu:
                    type: integer
                    example: 17285675
                    format: int64
                    description: Final update Id in last stream(ie `u` in last stream)
                    x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                  b:
                    type: array
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          example: "9517.6"
                        - type: string
                          description: Quantity
                          example: "10"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            example: "9517.6"
                          - type: string
                            description: Quantity
                            example: "10"
                    description: Bids to be updated
                    x-description-cn: 变动的买单深度
                  a:
                    type: array
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          example: "9518.5"
                        - type: string
                          description: Quantity
                          example: "45"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            example: "9518.5"
                          - type: string
                            description: Quantity
                            example: "45"
                    description: Asks to be updated
                    x-description-cn: 变动的卖单深度
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: depthUpdate
                E: 1591270260907
                T: 1591270260891
                s: BTCUSD_200626
                ps: BTCUSD
                U: 17285681
                u: 17285702
                pu: 17285675
                b:
                  - - "9517.6"
                    - "10"
                a:
                  - - "9518.5"
                    - "45"
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@depth@100ms
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: depthUpdate
                        enum:
                          - depthUpdate
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591270260907
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        example: 1591270260891
                        format: int64
                        description: Transction time
                        x-description-cn: 撮合时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      U:
                        type: integer
                        example: 17285681
                        format: int64
                        description: First update ID in event
                        x-description-cn: 从上次推送至今新增的第一个 update Id
                      u:
                        type: integer
                        example: 17285702
                        format: int64
                        description: Final update ID in event
                        x-description-cn: 从上次推送至今新增的最后一个 update Id
                      pu:
                        type: integer
                        example: 17285675
                        format: int64
                        description: Final update Id in last stream(ie `u` in last stream)
                        x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                      b:
                        type: array
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              example: "9517.6"
                            - type: string
                              description: Quantity
                              example: "10"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                example: "9517.6"
                              - type: string
                                description: Quantity
                                example: "10"
                        description: Bids to be updated
                        x-description-cn: 变动的买单深度
                      a:
                        type: array
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              example: "9518.5"
                            - type: string
                              description: Quantity
                              example: "45"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                example: "9518.5"
                              - type: string
                                description: Quantity
                                example: "45"
                        description: Asks to be updated
                        x-description-cn: 变动的卖单深度
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@depth@100ms
                data:
                  e: depthUpdate
                  E: 1591270260907
                  T: 1591270260891
                  s: BTCUSD_200626
                  ps: BTCUSD
                  U: 17285681
                  u: 17285702
                  pu: 17285675
                  b:
                    - - "9517.6"
                      - "10"
                  a:
                    - - "9518.5"
                      - "45"
                  st: 1
  /{pair}@indexPriceKline_{interval}:
    post:
      summary: Index Kline/Candlestick Streams
      x-summary-cn: 价格指数K线
      description: |-
        Index Kline/Candlestick Streams

        > **After CM migration**, both `fstream` and `dstream` may subscribe to CM symbols on this stream.
      x-description-cn: |-
        价格指数K线

        > **迁移后**,`fstream` 与 `dstream` 都可订阅 CM 的 symbol。
      operationId: indexKlineCandlestickStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#index-kline-candlestick-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/indexKlineCandlestickStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/index_kline_candlestick_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/index_kline_candlestick_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/IndexKlineCandlestickStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/IndexKlineCandlestickStreams/IndexKlineCandlestickStreams.go
      x-update-speed: 250ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: pair
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The pair parameter
          x-description-cn: 交易对参数
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
          description: The interval parameter
          x-description-cn: 间隔 参数
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
                    - btcusdt@indexPriceKline_1m
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
                - btcusdt@indexPriceKline_1m
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Index Kline/Candlestick Streams
          x-description-cn: 指数 K线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: indexPrice_kline
                    enum:
                      - indexPrice_kline
                    description: eventType
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591267070033
                    format: int64
                    description: eventTime
                    x-description-cn: 事件时间
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        example: 1591267020000
                        format: int64
                        description: Kline start time
                        x-description-cn: 这根K线的起始时间
                      T:
                        type: integer
                        example: 1591267079999
                        format: int64
                        description: transactionTime
                        x-description-cn: 成交时间/交易时间
                      s:
                        type: string
                        example: "0"
                        description: symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: interval
                        x-description-cn: K 线周期
                      f:
                        type: integer
                        example: 1591267020000
                        format: int64
                        description: Ignore
                        x-description-cn: 忽略
                      L:
                        type: integer
                        example: 1591267070000
                        format: int64
                        description: Ignore
                        x-description-cn: 忽略
                      o:
                        type: string
                        example: "9542.21900000"
                        description: openPrice
                        x-description-cn: 开盘价
                      c:
                        type: string
                        example: "9542.50440000"
                        description: closePrice
                        x-description-cn: 收盘价
                      h:
                        type: string
                        example: "9542.71640000"
                        description: highPrice
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "9542.21040000"
                        description: lowPrice
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "0"
                        description: volume
                        x-description-cn: 基础资产成交量
                      "n":
                        type: integer
                        example: 51
                        format: int64
                        description: tradeNum
                        x-description-cn: 成交笔数
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                      q:
                        type: string
                        example: "0"
                        description: quoteVolume
                        x-description-cn: 计价资产成交额
                      V:
                        type: string
                        example: "0"
                        description: Taker buy volume
                        x-description-cn: 无意义字段
                      Q:
                        type: string
                        example: "0"
                        description: lastTradeVolume
                        x-description-cn: 最近一笔成交量
                      B:
                        type: string
                        example: "0"
                        description: Best bid qty
                        x-description-cn: 买单最优挂单数量
                    description: Kline payload
                    x-description-cn: K 线数据
              example:
                e: indexPrice_kline
                E: 1591267070033
                ps: BTCUSD
                k:
                  t: 1591267020000
                  T: 1591267079999
                  s: "0"
                  i: 1m
                  f: 1591267020000
                  L: 1591267070000
                  o: "9542.21900000"
                  c: "9542.50440000"
                  h: "9542.71640000"
                  l: "9542.21040000"
                  v: "0"
                  "n": 51
                  x: false
                  q: "0"
                  V: "0"
                  Q: "0"
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
                    example: btcusdt@indexPriceKline_1m
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: indexPrice_kline
                        enum:
                          - indexPrice_kline
                        description: eventType
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591267070033
                        format: int64
                        description: eventTime
                        x-description-cn: 事件时间
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            example: 1591267020000
                            format: int64
                            description: Kline start time
                            x-description-cn: 这根K线的起始时间
                          T:
                            type: integer
                            example: 1591267079999
                            format: int64
                            description: transactionTime
                            x-description-cn: 成交时间/交易时间
                          s:
                            type: string
                            example: "0"
                            description: symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: interval
                            x-description-cn: K 线周期
                          f:
                            type: integer
                            example: 1591267020000
                            format: int64
                            description: Ignore
                            x-description-cn: 忽略
                          L:
                            type: integer
                            example: 1591267070000
                            format: int64
                            description: Ignore
                            x-description-cn: 忽略
                          o:
                            type: string
                            example: "9542.21900000"
                            description: openPrice
                            x-description-cn: 开盘价
                          c:
                            type: string
                            example: "9542.50440000"
                            description: closePrice
                            x-description-cn: 收盘价
                          h:
                            type: string
                            example: "9542.71640000"
                            description: highPrice
                            x-description-cn: 最高价
                          l:
                            type: string
                            example: "9542.21040000"
                            description: lowPrice
                            x-description-cn: 最低价
                          v:
                            type: string
                            example: "0"
                            description: volume
                            x-description-cn: 基础资产成交量
                          "n":
                            type: integer
                            example: 51
                            format: int64
                            description: tradeNum
                            x-description-cn: 成交笔数
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                          q:
                            type: string
                            example: "0"
                            description: quoteVolume
                            x-description-cn: 计价资产成交额
                          V:
                            type: string
                            example: "0"
                            description: Taker buy volume
                            x-description-cn: 无意义字段
                          Q:
                            type: string
                            example: "0"
                            description: lastTradeVolume
                            x-description-cn: 最近一笔成交量
                          B:
                            type: string
                            example: "0"
                            description: Best bid qty
                            x-description-cn: 买单最优挂单数量
                        description: Kline payload
                        x-description-cn: K 线数据
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@indexPriceKline_1m
                data:
                  e: indexPrice_kline
                  E: 1591267070033
                  ps: BTCUSD
                  k:
                    t: 1591267020000
                    T: 1591267079999
                    s: "0"
                    i: 1m
                    f: 1591267020000
                    L: 1591267070000
                    o: "9542.21900000"
                    c: "9542.50440000"
                    h: "9542.71640000"
                    l: "9542.21040000"
                    v: "0"
                    "n": 51
                    x: false
                    q: "0"
                    V: "0"
                    Q: "0"
                    B: "0"
  /{pair}@indexPrice@{updateSpeed}:
    post:
      summary: Index Price Stream
      x-summary-cn: 最新现货指数价格
      description: Index Price Stream
      x-description-cn: 最新现货指数价格
      operationId: indexPriceStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#index-price-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/indexPriceStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/index_price_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/index_price_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/IndexPriceStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/IndexPriceStream/IndexPriceStream.go
      x-update-speed: 3000ms OR 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: pair
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The pair parameter
          x-description-cn: 交易对参数
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 1s
            enum:
              - 1s
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度
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
                    - btcusdt@indexPrice@1s
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
                - btcusdt@indexPrice@1s
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Index Price Stream
          x-description-cn: 指数价格流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: indexPriceUpdate
                    enum:
                      - indexPriceUpdate
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591261236000
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  i:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  p:
                    type: string
                    example: "9636.57860000"
                    description: Index Price
                    x-description-cn: 指数价格
              example:
                e: indexPriceUpdate
                E: 1591261236000
                i: BTCUSD
                p: "9636.57860000"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@indexPrice@1s
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: indexPriceUpdate
                        enum:
                          - indexPriceUpdate
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591261236000
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      i:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      p:
                        type: string
                        example: "9636.57860000"
                        description: Index Price
                        x-description-cn: 指数价格
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@indexPrice@1s
                data:
                  e: indexPriceUpdate
                  E: 1591261236000
                  i: BTCUSD
                  p: "9636.57860000"
  /{symbol}@bookTicker:
    post:
      summary: Individual Symbol Book Ticker Streams
      x-summary-cn: 按Symbol的最优挂单信息
      description: |-
        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        实时推送指定交易对的最优挂单价格或数量的任何更新。

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: individualSymbolBookTickerStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#individual-symbol-book-ticker-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/individualSymbolBookTickerStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/individual_symbol_book_ticker_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/individual_symbol_book_ticker_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/IndividualSymbolBookTickerStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/IndividualSymbolBookTickerStreams/IndividualSymbolBookTickerStreams.go
      x-update-speed: Real-time
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
                    - btcusdt@bookTicker
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
                - btcusdt@bookTicker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Book Ticker Streams
          x-description-cn: 单交易对最优挂单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: bookTicker
                    enum:
                      - bookTicker
                    description: Event type
                    x-description-cn: 事件类型
                  u:
                    type: integer
                    example: 17242169
                    format: int64
                    description: Order book update Id
                    x-description-cn: 更新ID
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "9548.1"
                    description: Best bid price
                    x-description-cn: 买单最优挂单价格
                  B:
                    type: string
                    example: "52"
                    description: Best bid qty
                    x-description-cn: 买单最优挂单数量
                  a:
                    type: string
                    example: "9548.5"
                    description: Best ask price
                    x-description-cn: 卖单最优挂单价格
                  A:
                    type: string
                    example: "11"
                    description: Best ask qty
                    x-description-cn: 卖单最优挂单数量
                  T:
                    type: integer
                    example: 1591268628155
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合时间
                  E:
                    type: integer
                    example: 1591268628166
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  st:
                    type: integer
                    example: 2
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: bookTicker
                u: 17242169
                s: BTCUSD_200626
                b: "9548.1"
                B: "52"
                a: "9548.5"
                A: "11"
                T: 1591268628155
                E: 1591268628166
                ps: BTCUSD
                st: 2
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@bookTicker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: bookTicker
                        enum:
                          - bookTicker
                        description: Event type
                        x-description-cn: 事件类型
                      u:
                        type: integer
                        example: 17242169
                        format: int64
                        description: Order book update Id
                        x-description-cn: 更新ID
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "9548.1"
                        description: Best bid price
                        x-description-cn: 买单最优挂单价格
                      B:
                        type: string
                        example: "52"
                        description: Best bid qty
                        x-description-cn: 买单最优挂单数量
                      a:
                        type: string
                        example: "9548.5"
                        description: Best ask price
                        x-description-cn: 卖单最优挂单价格
                      A:
                        type: string
                        example: "11"
                        description: Best ask qty
                        x-description-cn: 卖单最优挂单数量
                      T:
                        type: integer
                        example: 1591268628155
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合时间
                      E:
                        type: integer
                        example: 1591268628166
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      st:
                        type: integer
                        example: 2
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@bookTicker
                data:
                  e: bookTicker
                  u: 17242169
                  s: BTCUSD_200626
                  b: "9548.1"
                  B: "52"
                  a: "9548.5"
                  A: "11"
                  T: 1591268628155
                  E: 1591268628166
                  ps: BTCUSD
                  st: 2
  /{symbol}@miniTicker:
    post:
      summary: Individual Symbol Mini Ticker Stream
      x-summary-cn: 按Symbol的精简Ticker
      description: >-
        24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but
        a 24hr rolling window from requestTime to 24hrs before.


        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        单个交易对的24小时滚动窗口精简Ticker统计。这些不是UTC日的统计，而是从requestTime到24小时前的24小时滚动窗口。

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: individualSymbolMiniTickerStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#individual-symbol-mini-ticker-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/individualSymbolMiniTickerStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/individual_symbol_mini_ticker_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/individual_symbol_mini_ticker_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/IndividualSymbolMiniTickerStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/IndividualSymbolMiniTickerStream/IndividualSymbolMiniTickerStream.go
      x-update-speed: 500ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
                    - btcusdt@miniTicker
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
                - btcusdt@miniTicker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Mini Ticker Stream
          x-description-cn: 单交易对精简行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrMiniTicker
                    enum:
                      - 24hrMiniTicker
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591267704450
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  c:
                    type: string
                    example: "9561.7"
                    description: Close price
                    x-description-cn: 最新成交价格
                  o:
                    type: string
                    example: "9580.9"
                    description: Open price
                    x-description-cn: 24小时前开始第一笔成交价格
                  h:
                    type: string
                    example: "10000.0"
                    description: High price
                    x-description-cn: 24小时内最高成交价
                  l:
                    type: string
                    example: "7000.0"
                    description: Low price
                    x-description-cn: 24小时内最低成交价
                  v:
                    type: string
                    example: "487476"
                    description: Total traded volume
                    x-description-cn: 24小时成交量
                  q:
                    type: string
                    example: "33264343847.22378500"
                    description: Total traded base asset volume
                    x-description-cn: 24小时成交额(标的数量)
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: 24hrMiniTicker
                E: 1591267704450
                s: BTCUSD_200626
                ps: BTCUSD
                c: "9561.7"
                o: "9580.9"
                h: "10000.0"
                l: "7000.0"
                v: "487476"
                q: "33264343847.22378500"
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@miniTicker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrMiniTicker
                        enum:
                          - 24hrMiniTicker
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591267704450
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      c:
                        type: string
                        example: "9561.7"
                        description: Close price
                        x-description-cn: 最新成交价格
                      o:
                        type: string
                        example: "9580.9"
                        description: Open price
                        x-description-cn: 24小时前开始第一笔成交价格
                      h:
                        type: string
                        example: "10000.0"
                        description: High price
                        x-description-cn: 24小时内最高成交价
                      l:
                        type: string
                        example: "7000.0"
                        description: Low price
                        x-description-cn: 24小时内最低成交价
                      v:
                        type: string
                        example: "487476"
                        description: Total traded volume
                        x-description-cn: 24小时成交量
                      q:
                        type: string
                        example: "33264343847.22378500"
                        description: Total traded base asset volume
                        x-description-cn: 24小时成交额(标的数量)
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@miniTicker
                data:
                  e: 24hrMiniTicker
                  E: 1591267704450
                  s: BTCUSD_200626
                  ps: BTCUSD
                  c: "9561.7"
                  o: "9580.9"
                  h: "10000.0"
                  l: "7000.0"
                  v: "487476"
                  q: "33264343847.22378500"
                  st: 1
  /{symbol}@ticker:
    post:
      summary: Individual Symbol Ticker Streams
      x-summary-cn: 按Symbol的完整Ticker
      description: >-
        24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a
        24hr rolling window from requestTime to 24hrs before.


        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        24小时滚动窗口的单个交易对的行情统计。这些不是UTC日的统计，而是从requestTime到24小时前的24小时滚动窗口。

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: individualSymbolTickerStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#individual-symbol-ticker-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/individualSymbolTickerStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/individual_symbol_ticker_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/individual_symbol_ticker_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/IndividualSymbolTickerStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/IndividualSymbolTickerStreams/IndividualSymbolTickerStreams.go
      x-update-speed: 500ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
                    - btcusdt@ticker
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
                - btcusdt@ticker
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Individual Symbol Ticker Streams
          x-description-cn: 单交易对行情流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: 24hrTicker
                    enum:
                      - 24hrTicker
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591268262453
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "-43.4"
                    description: Price change
                    x-description-cn: 24小时价格变化
                  P:
                    type: string
                    example: "-0.452"
                    description: Price change percent
                    x-description-cn: 24小时价格变化(百分比)
                  w:
                    type: string
                    example: "0.00147974"
                    description: Weighted average price
                    x-description-cn: 24小时平均价格
                  c:
                    type: string
                    example: "9548.5"
                    description: Last price
                    x-description-cn: 最新成交价格
                  Q:
                    type: string
                    example: "2"
                    description: Last quantity
                    x-description-cn: 最新成交价格上的成交量
                  o:
                    type: string
                    example: "9591.9"
                    description: Open price
                    x-description-cn: 24小时前第一笔成交价格
                  h:
                    type: string
                    example: "10000.0"
                    description: High price
                    x-description-cn: 24小时内最高成交价
                  l:
                    type: string
                    example: "7000.0"
                    description: Low price
                    x-description-cn: 24小时内最低成交价
                  v:
                    type: string
                    example: "487850"
                    description: Total traded volume
                    x-description-cn: 24小时成交量
                  q:
                    type: string
                    example: "32968676323.46222700"
                    description: Total traded base asset volume
                    x-description-cn: 24小时成交额(标的数量)
                  O:
                    type: integer
                    example: 1591181820000
                    format: int64
                    description: Statistics open time
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    example: 1591268262442
                    format: int64
                    description: Statistics close time
                    x-description-cn: 统计关闭时间
                  F:
                    type: integer
                    example: 512014
                    format: int64
                    description: First trade ID
                    x-description-cn: 24小时内第一笔成交交易ID
                  L:
                    type: integer
                    example: 615289
                    format: int64
                    description: Last trade Id
                    x-description-cn: 24小时内最后一笔成交交易ID
                  "n":
                    type: integer
                    example: 103272
                    format: int64
                    description: Total number of trades
                    x-description-cn: 24小时内成交数
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: 24hrTicker
                E: 1591268262453
                s: BTCUSD_200626
                p: "-43.4"
                P: "-0.452"
                w: "0.00147974"
                c: "9548.5"
                Q: "2"
                o: "9591.9"
                h: "10000.0"
                l: "7000.0"
                v: "487850"
                q: "32968676323.46222700"
                O: 1591181820000
                C: 1591268262442
                F: 512014
                L: 615289
                "n": 103272
                ps: BTCUSD
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@ticker
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: 24hrTicker
                        enum:
                          - 24hrTicker
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591268262453
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "-43.4"
                        description: Price change
                        x-description-cn: 24小时价格变化
                      P:
                        type: string
                        example: "-0.452"
                        description: Price change percent
                        x-description-cn: 24小时价格变化(百分比)
                      w:
                        type: string
                        example: "0.00147974"
                        description: Weighted average price
                        x-description-cn: 24小时平均价格
                      c:
                        type: string
                        example: "9548.5"
                        description: Last price
                        x-description-cn: 最新成交价格
                      Q:
                        type: string
                        example: "2"
                        description: Last quantity
                        x-description-cn: 最新成交价格上的成交量
                      o:
                        type: string
                        example: "9591.9"
                        description: Open price
                        x-description-cn: 24小时前第一笔成交价格
                      h:
                        type: string
                        example: "10000.0"
                        description: High price
                        x-description-cn: 24小时内最高成交价
                      l:
                        type: string
                        example: "7000.0"
                        description: Low price
                        x-description-cn: 24小时内最低成交价
                      v:
                        type: string
                        example: "487850"
                        description: Total traded volume
                        x-description-cn: 24小时成交量
                      q:
                        type: string
                        example: "32968676323.46222700"
                        description: Total traded base asset volume
                        x-description-cn: 24小时成交额(标的数量)
                      O:
                        type: integer
                        example: 1591181820000
                        format: int64
                        description: Statistics open time
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        example: 1591268262442
                        format: int64
                        description: Statistics close time
                        x-description-cn: 统计关闭时间
                      F:
                        type: integer
                        example: 512014
                        format: int64
                        description: First trade ID
                        x-description-cn: 24小时内第一笔成交交易ID
                      L:
                        type: integer
                        example: 615289
                        format: int64
                        description: Last trade Id
                        x-description-cn: 24小时内最后一笔成交交易ID
                      "n":
                        type: integer
                        example: 103272
                        format: int64
                        description: Total number of trades
                        x-description-cn: 24小时内成交数
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@ticker
                data:
                  e: 24hrTicker
                  E: 1591268262453
                  s: BTCUSD_200626
                  p: "-43.4"
                  P: "-0.452"
                  w: "0.00147974"
                  c: "9548.5"
                  Q: "2"
                  o: "9591.9"
                  h: "10000.0"
                  l: "7000.0"
                  v: "487850"
                  q: "32968676323.46222700"
                  O: 1591181820000
                  C: 1591268262442
                  F: 512014
                  L: 615289
                  "n": 103272
                  ps: BTCUSD
                  st: 1
  /{symbol}@kline_{interval}:
    post:
      summary: Kline/Candlestick Streams
      x-summary-cn: K线
      description: >-
        The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if
        existing).


        > **After CM migration**, both `fstream` and `dstream` may subscribe to either UM or CM symbols on this stream.
      x-description-cn: |-
        K线流每250毫秒推送当前K线更新（如果有）.

        > **迁移后**,`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。
      operationId: klineCandlestickStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#kline-candlestick-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/klineCandlestickStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/kline_candlestick_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/kline_candlestick_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/KlineCandlestickStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/KlineCandlestickStreams/KlineCandlestickStreams.go
      x-update-speed: 250ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
          description: The interval parameter
          x-description-cn: 间隔 参数
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
                    - btcusdt@kline_1m
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
                - btcusdt@kline_1m
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Kline/Candlestick Streams
          x-description-cn: K线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: kline
                    enum:
                      - kline
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591261542539
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        example: 1591261500000
                        format: int64
                        description: Kline start time
                        x-description-cn: 这根K线的起始时间
                      T:
                        type: integer
                        example: 1591261559999
                        format: int64
                        description: Kline close time
                        x-description-cn: 这根K线的结束时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: Interval
                        x-description-cn: K线间隔
                      f:
                        type: integer
                        example: 606400
                        format: int64
                        description: First trade ID
                        x-description-cn: 这根K线期间第一笔成交ID
                      L:
                        type: integer
                        example: 606430
                        format: int64
                        description: Last trade ID
                        x-description-cn: 这根K线期间末一笔成交ID
                      o:
                        type: string
                        example: "9638.9"
                        description: Open price
                        x-description-cn: 这根K线期间第一笔成交价
                      c:
                        type: string
                        example: "9639.8"
                        description: Close price
                        x-description-cn: 这根K线期间末一笔成交价
                      h:
                        type: string
                        example: "9639.8"
                        description: High price
                        x-description-cn: 这根K线期间最高成交价
                      l:
                        type: string
                        example: "9638.6"
                        description: Low price
                        x-description-cn: 这根K线期间最低成交价
                      v:
                        type: string
                        example: "156"
                        description: volume
                        x-description-cn: 这根K线期间成交量
                      "n":
                        type: integer
                        example: 31
                        format: int64
                        description: Number of trades
                        x-description-cn: 这根K线期间成交笔数
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                      q:
                        type: string
                        example: "1.61836886"
                        description: Base asset volume
                        x-description-cn: 这根K线期间成交额(标的数量)
                      V:
                        type: string
                        example: "73"
                        description: Taker buy volume
                        x-description-cn: 主动买入的成交量
                      Q:
                        type: string
                        example: "0.75731156"
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入的成交额(标的数量)
                      B:
                        type: string
                        example: "0"
                        description: Ignore
                        x-description-cn: 忽略此参数
                    description: Kline payload
                    x-description-cn: K 线数据
              example:
                e: kline
                E: 1591261542539
                s: BTCUSD_200626
                k:
                  t: 1591261500000
                  T: 1591261559999
                  s: BTCUSD_200626
                  i: 1m
                  f: 606400
                  L: 606430
                  o: "9638.9"
                  c: "9639.8"
                  h: "9639.8"
                  l: "9638.6"
                  v: "156"
                  "n": 31
                  x: false
                  q: "1.61836886"
                  V: "73"
                  Q: "0.75731156"
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
                    example: btcusdt@kline_1m
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: kline
                        enum:
                          - kline
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591261542539
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            example: 1591261500000
                            format: int64
                            description: Kline start time
                            x-description-cn: 这根K线的起始时间
                          T:
                            type: integer
                            example: 1591261559999
                            format: int64
                            description: Kline close time
                            x-description-cn: 这根K线的结束时间
                          s:
                            type: string
                            example: BTCUSD_200626
                            description: Symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: Interval
                            x-description-cn: K线间隔
                          f:
                            type: integer
                            example: 606400
                            format: int64
                            description: First trade ID
                            x-description-cn: 这根K线期间第一笔成交ID
                          L:
                            type: integer
                            example: 606430
                            format: int64
                            description: Last trade ID
                            x-description-cn: 这根K线期间末一笔成交ID
                          o:
                            type: string
                            example: "9638.9"
                            description: Open price
                            x-description-cn: 这根K线期间第一笔成交价
                          c:
                            type: string
                            example: "9639.8"
                            description: Close price
                            x-description-cn: 这根K线期间末一笔成交价
                          h:
                            type: string
                            example: "9639.8"
                            description: High price
                            x-description-cn: 这根K线期间最高成交价
                          l:
                            type: string
                            example: "9638.6"
                            description: Low price
                            x-description-cn: 这根K线期间最低成交价
                          v:
                            type: string
                            example: "156"
                            description: volume
                            x-description-cn: 这根K线期间成交量
                          "n":
                            type: integer
                            example: 31
                            format: int64
                            description: Number of trades
                            x-description-cn: 这根K线期间成交笔数
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                          q:
                            type: string
                            example: "1.61836886"
                            description: Base asset volume
                            x-description-cn: 这根K线期间成交额(标的数量)
                          V:
                            type: string
                            example: "73"
                            description: Taker buy volume
                            x-description-cn: 主动买入的成交量
                          Q:
                            type: string
                            example: "0.75731156"
                            description: Taker buy base asset volume
                            x-description-cn: 主动买入的成交额(标的数量)
                          B:
                            type: string
                            example: "0"
                            description: Ignore
                            x-description-cn: 忽略此参数
                        description: Kline payload
                        x-description-cn: K 线数据
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@kline_1m
                data:
                  e: kline
                  E: 1591261542539
                  s: BTCUSD_200626
                  k:
                    t: 1591261500000
                    T: 1591261559999
                    s: BTCUSD_200626
                    i: 1m
                    f: 606400
                    L: 606430
                    o: "9638.9"
                    c: "9639.8"
                    h: "9639.8"
                    l: "9638.6"
                    v: "156"
                    "n": 31
                    x: false
                    q: "1.61836886"
                    V: "73"
                    Q: "0.75731156"
                    B: "0"
  /{symbol}@forceOrder:
    post:
      summary: Market Liquidation Order Streams
      x-summary-cn: 强平订单
      description: >-
        The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol. For each
        symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation
        happens in the interval of 1000ms, no stream will be pushed.
      x-description-cn: 强平订单快照流推送特定交易对的强平订单信息。对于每个交易对，在1000ms内只会推送最新的一笔强平订单作为快照。如果在1000ms的时间间隔内没有发生强平，则不会推送任何流。
      operationId: marketLiquidationOrderStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#market-liquidation-order-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/marketLiquidationOrderStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/market_liquidation_order_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/market_liquidation_order_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/MarketLiquidationOrderStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/MarketLiquidationOrderStreams/MarketLiquidationOrderStreams.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
                    - btcusdt@forceOrder
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
                - btcusdt@forceOrder
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Liquidation Order Streams
          x-description-cn: 强平订单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: forceOrder
                    enum:
                      - forceOrder
                    description: Event Type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591154240950
                    format: int64
                    description: Event Time
                    x-description-cn: 事件时间
                  o:
                    type: object
                    properties:
                      s:
                        type: string
                        example: BTCUSD_200925
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      S:
                        type: string
                        example: SELL
                        description: Side
                        x-description-cn: 订单方向
                      o:
                        type: string
                        example: LIMIT
                        description: Order Type
                        x-description-cn: 订单类型
                      f:
                        type: string
                        example: IOC
                        description: Time in Force
                        x-description-cn: 有效方式
                      q:
                        type: string
                        example: "1"
                        description: Original Quantity
                        x-description-cn: 订单数量
                      p:
                        type: string
                        example: "9425.5"
                        description: Price
                        x-description-cn: 订单价格
                      ap:
                        type: string
                        example: "9496.5"
                        description: Average Price
                        x-description-cn: 平均价格
                      X:
                        type: string
                        example: FILLED
                        description: Order Status
                        x-description-cn: 订单状态
                      l:
                        type: string
                        example: "1"
                        description: Order Last Filled Quantity
                        x-description-cn: 订单最近成交量
                      z:
                        type: string
                        example: "1"
                        description: Order Filled Accumulated Quantity
                        x-description-cn: 订单累计成交量
                      T:
                        type: integer
                        example: 1591154240949
                        format: int64
                        description: Order Trade Time
                        x-description-cn: 交易时间
                    description: Order Type
                    x-description-cn: 订单类型
              example:
                e: forceOrder
                E: 1591154240950
                o:
                  s: BTCUSD_200925
                  ps: BTCUSD
                  S: SELL
                  o: LIMIT
                  f: IOC
                  q: "1"
                  p: "9425.5"
                  ap: "9496.5"
                  X: FILLED
                  l: "1"
                  z: "1"
                  T: 1591154240949
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@forceOrder
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: forceOrder
                        enum:
                          - forceOrder
                        description: Event Type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591154240950
                        format: int64
                        description: Event Time
                        x-description-cn: 事件时间
                      o:
                        type: object
                        properties:
                          s:
                            type: string
                            example: BTCUSD_200925
                            description: Symbol
                            x-description-cn: 交易对
                          ps:
                            type: string
                            example: BTCUSD
                            description: Pair
                            x-description-cn: 标的交易对
                          S:
                            type: string
                            example: SELL
                            description: Side
                            x-description-cn: 订单方向
                          o:
                            type: string
                            example: LIMIT
                            description: Order Type
                            x-description-cn: 订单类型
                          f:
                            type: string
                            example: IOC
                            description: Time in Force
                            x-description-cn: 有效方式
                          q:
                            type: string
                            example: "1"
                            description: Original Quantity
                            x-description-cn: 订单数量
                          p:
                            type: string
                            example: "9425.5"
                            description: Price
                            x-description-cn: 订单价格
                          ap:
                            type: string
                            example: "9496.5"
                            description: Average Price
                            x-description-cn: 平均价格
                          X:
                            type: string
                            example: FILLED
                            description: Order Status
                            x-description-cn: 订单状态
                          l:
                            type: string
                            example: "1"
                            description: Order Last Filled Quantity
                            x-description-cn: 订单最近成交量
                          z:
                            type: string
                            example: "1"
                            description: Order Filled Accumulated Quantity
                            x-description-cn: 订单累计成交量
                          T:
                            type: integer
                            example: 1591154240949
                            format: int64
                            description: Order Trade Time
                            x-description-cn: 交易时间
                        description: Order Type
                        x-description-cn: 订单类型
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@forceOrder
                data:
                  e: forceOrder
                  E: 1591154240950
                  o:
                    s: BTCUSD_200925
                    ps: BTCUSD
                    S: SELL
                    o: LIMIT
                    f: IOC
                    q: "1"
                    p: "9425.5"
                    ap: "9496.5"
                    X: FILLED
                    l: "1"
                    z: "1"
                    T: 1591154240949
  /{symbol}@markPriceKline_{interval}:
    post:
      summary: Mark Price Kline/Candlestick Streams
      x-summary-cn: 标记价格K线
      description: |-
        Mark Price Kline/Candlestick Streams

        > **After CM migration**, both `fstream` and `dstream` may subscribe to CM symbols on this stream.
      x-description-cn: |-
        标记价格K线

        > **迁移后**,`fstream` 与 `dstream` 都可订阅 CM 的 symbol。
      operationId: markPriceKlineCandlestickStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#mark-price-kline-candlestick-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/markPriceKlineCandlestickStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/mark_price_kline_candlestick_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/mark_price_kline_candlestick_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/MarkPriceKlineCandlestickStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/MarkPriceKlineCandlestickStreams/MarkPriceKlineCandlestickStreams.go
      x-update-speed: 250ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
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
          description: The interval parameter
          x-description-cn: 间隔 参数
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
                    - btcusdt@markPriceKline_1m
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
                - btcusdt@markPriceKline_1m
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Mark Price Kline/Candlestick Streams
          x-description-cn: 标记价格 K线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: markPrice_kline
                    enum:
                      - markPrice_kline
                    description: Event Name
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591267398004
                    format: int64
                    description: Event Time
                    x-description-cn: 事件时间
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        example: 1591267380000
                        format: int64
                        description: Kline start time
                        x-description-cn: 这根K线的起始时间
                      T:
                        type: integer
                        example: 1591267439999
                        format: int64
                        description: Kline close time
                        x-description-cn: 这根K线的结束时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: Interval
                        x-description-cn: K线间隔
                      f:
                        type: integer
                        example: 1591267380000
                        format: int64
                        description: ignore
                        x-description-cn: 无意义字段
                      L:
                        type: integer
                        example: 1591267398000
                        format: int64
                        description: ignore
                        x-description-cn: 无意义字段
                      o:
                        type: string
                        example: "9539.67161333"
                        description: Open price
                        x-description-cn: 这根K线期间第一笔成交价
                      c:
                        type: string
                        example: "9540.82761333"
                        description: Close price
                        x-description-cn: 这根K线期间末一笔成交价
                      h:
                        type: string
                        example: "9540.82761333"
                        description: High price
                        x-description-cn: 这根K线期间最高成交价
                      l:
                        type: string
                        example: "9539.66961333"
                        description: Low price
                        x-description-cn: 这根K线期间最低成交价
                      v:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 无意义字段
                      "n":
                        type: integer
                        example: 19
                        format: int64
                        description: Number of basic data
                        x-description-cn: 这根K线更新期间数据数量
                      x:
                        type: boolean
                        example: false
                        description: Is this kline closed?
                        x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                      q:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 无意义字段
                      V:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 无意义字段
                      Q:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 无意义字段
                      B:
                        type: string
                        example: "0"
                        description: ignore
                        x-description-cn: 无意义字段
                    description: Kline payload
                    x-description-cn: K 线数据
              example:
                e: markPrice_kline
                E: 1591267398004
                ps: BTCUSD
                k:
                  t: 1591267380000
                  T: 1591267439999
                  s: BTCUSD_200626
                  i: 1m
                  f: 1591267380000
                  L: 1591267398000
                  o: "9539.67161333"
                  c: "9540.82761333"
                  h: "9540.82761333"
                  l: "9539.66961333"
                  v: "0"
                  "n": 19
                  x: false
                  q: "0"
                  V: "0"
                  Q: "0"
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
                    example: btcusdt@markPriceKline_1m
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: markPrice_kline
                        enum:
                          - markPrice_kline
                        description: Event Name
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591267398004
                        format: int64
                        description: Event Time
                        x-description-cn: 事件时间
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            example: 1591267380000
                            format: int64
                            description: Kline start time
                            x-description-cn: 这根K线的起始时间
                          T:
                            type: integer
                            example: 1591267439999
                            format: int64
                            description: Kline close time
                            x-description-cn: 这根K线的结束时间
                          s:
                            type: string
                            example: BTCUSD_200626
                            description: Symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: Interval
                            x-description-cn: K线间隔
                          f:
                            type: integer
                            example: 1591267380000
                            format: int64
                            description: ignore
                            x-description-cn: 无意义字段
                          L:
                            type: integer
                            example: 1591267398000
                            format: int64
                            description: ignore
                            x-description-cn: 无意义字段
                          o:
                            type: string
                            example: "9539.67161333"
                            description: Open price
                            x-description-cn: 这根K线期间第一笔成交价
                          c:
                            type: string
                            example: "9540.82761333"
                            description: Close price
                            x-description-cn: 这根K线期间末一笔成交价
                          h:
                            type: string
                            example: "9540.82761333"
                            description: High price
                            x-description-cn: 这根K线期间最高成交价
                          l:
                            type: string
                            example: "9539.66961333"
                            description: Low price
                            x-description-cn: 这根K线期间最低成交价
                          v:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 无意义字段
                          "n":
                            type: integer
                            example: 19
                            format: int64
                            description: Number of basic data
                            x-description-cn: 这根K线更新期间数据数量
                          x:
                            type: boolean
                            example: false
                            description: Is this kline closed?
                            x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                          q:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 无意义字段
                          V:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 无意义字段
                          Q:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 无意义字段
                          B:
                            type: string
                            example: "0"
                            description: ignore
                            x-description-cn: 无意义字段
                        description: Kline payload
                        x-description-cn: K 线数据
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@markPriceKline_1m
                data:
                  e: markPrice_kline
                  E: 1591267398004
                  ps: BTCUSD
                  k:
                    t: 1591267380000
                    T: 1591267439999
                    s: BTCUSD_200626
                    i: 1m
                    f: 1591267380000
                    L: 1591267398000
                    o: "9539.67161333"
                    c: "9540.82761333"
                    h: "9540.82761333"
                    l: "9539.66961333"
                    v: "0"
                    "n": 19
                    x: false
                    q: "0"
                    V: "0"
                    Q: "0"
                    B: "0"
  /{pair}@markPrice@{updateSpeed}:
    post:
      summary: Mark Price of All Symbols of a Pair
      x-summary-cn: 特定pair最新MarkPrice
      description: >-
        Mark Price of All Symbols of a Pair


        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and
        `dstream` may subscribe to either UM or CM symbols on this stream.
      x-description-cn: |-
        特定pair最新MarkPrice

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。
      operationId: markPriceOfAllSymbolsOfAPair
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#mark-price-of-all-symbols-of-apair
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/markPriceOfAllSymbolsOfAPair.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/mark_price_of_all_symbols_of_a_pair.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/mark_price_of_all_symbols_of_a_pair.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/MarkPriceOfAllSymbolsOfAPairExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/MarkPriceOfAllSymbolsOfAPair/MarkPriceOfAllSymbolsOfAPair.go
      x-update-speed: 3000ms OR 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: pair
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The pair parameter
          x-description-cn: 交易对参数
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 1s
            enum:
              - 1s
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度
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
                    - btcusdt@markPrice@1s
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
                - btcusdt@markPrice@1s
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Mark Price of All Symbols of a Pair
          x-description-cn: 某个标的交易对下所有合约的标记价格流
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: markPriceUpdate
                      enum:
                        - markPriceUpdate
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      example: 1596095725000
                      format: int64
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: BTCUSD_201225
                      description: Symbol
                      x-description-cn: 交易对
                    p:
                      type: string
                      example: "10934.62615417"
                      description: Mark Price
                      x-description-cn: 标记价格
                    P:
                      type: string
                      example: "10962.17178236"
                      description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                      x-description-cn: 预估结算价,仅在结算前最后一小时有参考价值
                    i:
                      type: string
                      example: "10933.62615417"
                      description: Index Price
                      x-description-cn: 指数价格
                    r:
                      type: string
                      example: ""
                      description: funding rate for perpetual symbol, "" will be shown for delivery symbol
                      x-description-cn: 资金费率，对非永续合约显示""
                    T:
                      type: integer
                      example: 0
                      format: int64
                      description: next funding time for perpetual symbol, 0 will be shown for delivery symbol
                      x-description-cn: 下个资金时间,对非永续合约显示0
                    st:
                      type: integer
                      example: 1
                      description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                      x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                - e: markPriceUpdate
                  E: 1596095725000
                  s: BTCUSD_201225
                  p: "10934.62615417"
                  P: "10962.17178236"
                  i: "10933.62615417"
                  r: ""
                  T: 0
                  st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@markPrice@1s
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: markPriceUpdate
                          enum:
                            - markPriceUpdate
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          example: 1596095725000
                          format: int64
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: BTCUSD_201225
                          description: Symbol
                          x-description-cn: 交易对
                        p:
                          type: string
                          example: "10934.62615417"
                          description: Mark Price
                          x-description-cn: 标记价格
                        P:
                          type: string
                          example: "10962.17178236"
                          description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                          x-description-cn: 预估结算价,仅在结算前最后一小时有参考价值
                        i:
                          type: string
                          example: "10933.62615417"
                          description: Index Price
                          x-description-cn: 指数价格
                        r:
                          type: string
                          example: ""
                          description: funding rate for perpetual symbol, "" will be shown for delivery symbol
                          x-description-cn: 资金费率，对非永续合约显示""
                        T:
                          type: integer
                          example: 0
                          format: int64
                          description: next funding time for perpetual symbol, 0 will be shown for delivery symbol
                          x-description-cn: 下个资金时间,对非永续合约显示0
                        st:
                          type: integer
                          example: 1
                          description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                          x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@markPrice@1s
                data:
                  - e: markPriceUpdate
                    E: 1596095725000
                    s: BTCUSD_201225
                    p: "10934.62615417"
                    P: "10962.17178236"
                    i: "10933.62615417"
                    r: ""
                    T: 0
                    st: 1
  /{symbol}@markPrice@{updateSpeed}:
    post:
      summary: Mark Price Stream
      x-summary-cn: 最新MarkPrice
      description: >-
        Mark price update stream


        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM); both `fstream` and
        `dstream` may subscribe to either UM or CM symbols on this stream.
      x-description-cn: |-
        标记价格更新流

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM);`fstream` 与 `dstream` 都可订阅 UM 或 CM 的 symbol。
      operationId: markPriceStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#mark-price-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/markPriceStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/mark_price_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/mark_price_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/MarkPriceStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/MarkPriceStream/MarkPriceStream.go
      x-update-speed: 3000ms OR 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 1s
            enum:
              - 1s
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度
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
                    - btcusdt@markPrice@1s
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
                - btcusdt@markPrice@1s
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Mark Price Stream
          x-description-cn: 标记价格流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: markPriceUpdate
                    enum:
                      - markPriceUpdate
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1596095725000
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTCUSD_201225
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "10934.62615417"
                    description: Mark Price
                    x-description-cn: 标记价格
                  P:
                    type: string
                    example: "10962.17178236"
                    description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                    x-description-cn: 预估结算价,仅在结算前最后一小时有参考价值
                  i:
                    type: string
                    example: "10933.62615417"
                    description: Index Price
                    x-description-cn: 指数价格
                  r:
                    type: string
                    example: ""
                    description: funding rate for perpetual symbol, "" will be shown for delivery symbol
                    x-description-cn: 资金费率，对非永续合约显示""
                  T:
                    type: integer
                    example: 0
                    format: int64
                    description: next funding time for perpetual symbol, 0 will be shown for delivery symbol
                    x-description-cn: 下个资金时间,对非永续合约显示0
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: markPriceUpdate
                E: 1596095725000
                s: BTCUSD_201225
                p: "10934.62615417"
                P: "10962.17178236"
                i: "10933.62615417"
                r: ""
                T: 0
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@markPrice@1s
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: markPriceUpdate
                        enum:
                          - markPriceUpdate
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1596095725000
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTCUSD_201225
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "10934.62615417"
                        description: Mark Price
                        x-description-cn: 标记价格
                      P:
                        type: string
                        example: "10962.17178236"
                        description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                        x-description-cn: 预估结算价,仅在结算前最后一小时有参考价值
                      i:
                        type: string
                        example: "10933.62615417"
                        description: Index Price
                        x-description-cn: 指数价格
                      r:
                        type: string
                        example: ""
                        description: funding rate for perpetual symbol, "" will be shown for delivery symbol
                        x-description-cn: 资金费率，对非永续合约显示""
                      T:
                        type: integer
                        example: 0
                        format: int64
                        description: next funding time for perpetual symbol, 0 will be shown for delivery symbol
                        x-description-cn: 下个资金时间,对非永续合约显示0
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@markPrice@1s
                data:
                  e: markPriceUpdate
                  E: 1596095725000
                  s: BTCUSD_201225
                  p: "10934.62615417"
                  P: "10962.17178236"
                  i: "10933.62615417"
                  r: ""
                  T: 0
                  st: 1
  /{symbol}@depth{levels}@{updateSpeed}:
    post:
      summary: Partial Book Depth Streams
      x-summary-cn: 有限档深度信息
      description: |-
        Top levels bids and asks.

        > **After CM migration**, the payload is appended with a new `st` field (`1` = UM, `2` = CM).
      x-description-cn: |-
        买卖双方前几档的深度信息。

        > **迁移后**,payload 末尾新增 `st` 字段(`1` = UM,`2` = CM)。
      operationId: partialBookDepthStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~#partial-book-depth-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-streams/partialBookDepthStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_streams/partial_book_depth_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_streams/partial_book_depth_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/stream/defaultpkg/PartialBookDepthStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketstreams/DefaultAPI/PartialBookDepthStreams/PartialBookDepthStreams.go
      x-update-speed: 250ms, 500ms or 100ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: string
            example: e9d6b4349871b40611412680b3445fac
          description: Unique WebSocket request ID.
          x-description-cn: 唯一的 WebSocket 请求 ID.
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
        - name: levels
          in: path
          required: true
          schema:
            type: string
            example: 10
            enum:
              - 5
              - 10
              - 20
          description: The levels parameter
          x-description-cn: levels 参数
        - name: updateSpeed
          in: path
          required: false
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
              - 500ms
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度
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
                    - btcusdt@depth10@100ms
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
                - btcusdt@depth10@100ms
              id: e9d6b4349871b40611412680b3445fac
      responses:
        Raw Stream:
          description: Partial Book Depth Streams
          x-description-cn: 部分深度流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    enum:
                      - depthUpdate
                    description: Event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1591269996801
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    example: 1591269996646
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合时间
                  s:
                    type: string
                    example: BTCUSD_200626
                    description: Symbol
                    x-description-cn: 交易对
                  ps:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  U:
                    type: integer
                    example: 17276694
                    format: int64
                    description: First update ID in event
                    x-description-cn: 从上次推送至今新增的第一个 update Id
                  u:
                    type: integer
                    example: 17276701
                    format: int64
                    description: updateId
                    x-description-cn: 更新 ID
                  pu:
                    type: integer
                    example: 17276678
                    format: int64
                    description: Final update Id in last stream(ie `u` in last stream)
                    x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                  b:
                    type: array
                    items:
                      type: array
                      items:
                        type: string
                        example: "9523.0"
                    description: Bids to be updated
                    x-description-cn: 买方
                  a:
                    type: array
                    items:
                      type: array
                      items:
                        type: string
                        example: "9524.6"
                    description: Asks to be updated
                    x-description-cn: 卖方
                  st:
                    type: integer
                    example: 1
                    description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                    x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
              example:
                e: depthUpdate
                E: 1591269996801
                T: 1591269996646
                s: BTCUSD_200626
                ps: BTCUSD
                U: 17276694
                u: 17276701
                pu: 17276678
                b:
                  - - "9523.0"
                a:
                  - - "9524.6"
                st: 1
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@depth10@100ms
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: depthUpdate
                        enum:
                          - depthUpdate
                        description: Event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1591269996801
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        example: 1591269996646
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合时间
                      s:
                        type: string
                        example: BTCUSD_200626
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      U:
                        type: integer
                        example: 17276694
                        format: int64
                        description: First update ID in event
                        x-description-cn: 从上次推送至今新增的第一个 update Id
                      u:
                        type: integer
                        example: 17276701
                        format: int64
                        description: updateId
                        x-description-cn: 更新 ID
                      pu:
                        type: integer
                        example: 17276678
                        format: int64
                        description: Final update Id in last stream(ie `u` in last stream)
                        x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                      b:
                        type: array
                        items:
                          type: array
                          items:
                            type: string
                            example: "9523.0"
                        description: Bids to be updated
                        x-description-cn: 买方
                      a:
                        type: array
                        items:
                          type: array
                          items:
                            type: string
                            example: "9524.6"
                        description: Asks to be updated
                        x-description-cn: 卖方
                      st:
                        type: integer
                        example: 1
                        description: "(After CM migration) Symbol type: 1 = UM, 2 = CM"
                        x-description-cn: (迁移后新增) Symbol 类型:1 = UM,2 = CM
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@depth10@100ms
                data:
                  e: depthUpdate
                  E: 1591269996801
                  T: 1591269996646
                  s: BTCUSD_200626
                  ps: BTCUSD
                  U: 17276694
                  u: 17276701
                  pu: 17276678
                  b:
                    - - "9523.0"
                  a:
                    - - "9524.6"
                  st: 1
components:
  schemas:
    accountConfigUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - ACCOUNT_CONFIG_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1611646737479
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1611646737476
          format: int64
          description: Transaction Time
          x-description-cn: 撮合时间
        ac:
          type: object
          properties:
            s:
              type: string
              example: BTCUSD_PERP
              description: Symbol
              x-description-cn: 交易对
            l:
              type: integer
              example: 25
              format: int64
              description: Leverage
              x-description-cn: 杠杆倍数
    accountUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - ACCOUNT_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1564745798939
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1564745798938
          format: int64
          description: Transaction
          x-description-cn: 撮合时间
        i:
          type: string
          example: SfsR
          description: Account Alias
          x-description-cn: 账户唯一识别码 accountAlias
        a:
          type: object
          description: Update Data
          x-description-cn: 账户更新事件
          properties:
            m:
              type: string
              example: ORDER
              description: Event reason type
              x-description-cn: 事件推出原因
            B:
              type: array
              description: Balances
              x-description-cn: 余额信息
              items:
                type: object
                properties:
                  a:
                    type: string
                    example: BTC
                    description: Asset
                    x-description-cn: 资产名称
                  wb:
                    type: string
                    example: "122624.12345678"
                    description: Wallet Balance
                    x-description-cn: 钱包余额
                  cw:
                    type: string
                    example: "100.12345678"
                    description: Cross Wallet Balance
                    x-description-cn: 除去逐仓保证金的钱包余额
                  bc:
                    type: string
                    example: "50.12345678"
                    description: Balance Change except PnL and Commission
                    x-description-cn: 除去盈亏与交易手续费以外的钱包余额改变量
            P:
              type: array
              items:
                type: object
                properties:
                  s:
                    type: string
                    example: BTCUSD_200925
                    description: Symbol
                    x-description-cn: 交易对
                  pa:
                    type: string
                    example: "0"
                    description: Position Amount
                    x-description-cn: 仓位
                  ep:
                    type: string
                    example: "0.0"
                    description: Entry Price
                    x-description-cn: 入仓价格
                  bep:
                    type: string
                    example: "0.0"
                    description: Break-Even Price
                    x-description-cn: 盈亏平衡价
                  cr:
                    type: string
                    example: "200"
                    description: (Pre-fee) Accumulated Realized
                    x-description-cn: (费前)累计实现损益
                  up:
                    type: string
                    example: "0"
                    description: Unrealized PnL
                    x-description-cn: 持仓未实现盈亏
                  mt:
                    type: string
                    example: isolated
                    description: Margin Type
                    x-description-cn: 保证金模式
                  iw:
                    type: string
                    example: "0.00000000"
                    description: Isolated Wallet (if isolated position)
                    x-description-cn: 若为逐仓，仓位保证金
                  ps:
                    type: string
                    example: BOTH
                    description: Position Side
                    x-description-cn: 持仓方向
            S:
              type: string
              example: BTCUSD_200925
              description: Symbol associated with FUNDING_FEE event
              x-description-cn: 本次 FUNDING_FEE 事件对应的交易对
    gridUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - GRID_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        T:
          type: integer
          example: 1669262908216
          format: int64
          description: Transaction Time
          x-description-cn: 撮合时间
        E:
          type: integer
          example: 1669262908218
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        gu:
          type: object
          properties:
            si:
              type: integer
              example: 176057039
              format: int64
              description: Strategy ID
              x-description-cn: 策略 ID
            st:
              type: string
              example: GRID
              description: Strategy Type
              x-description-cn: 策略类型
            ss:
              type: string
              example: WORKING
              description: Strategy Status
              x-description-cn: 策略状态
            s:
              type: string
              example: BTCUSDT
              description: Symbol
              x-description-cn: 交易对
            r:
              type: string
              example: "-0.00300716"
              description: Realized PNL
              x-description-cn: 已实现 PNL
            up:
              type: string
              example: "16720"
              description: Unmatched Average Price
              x-description-cn: 未配对均价
            uq:
              type: string
              example: "-0.001"
              description: Unmatched Qty
              x-description-cn: 未配对数量
            uf:
              type: string
              example: "-0.00300716"
              description: Unmatched Fee
              x-description-cn: 未配对手续费
            mp:
              type: string
              example: "0.0"
              description: Matched PNL
              x-description-cn: 已配对 PNL
            ut:
              type: integer
              example: 1669262908197
              format: int64
              description: Update Time
              x-description-cn: 更新时间
    listenKeyExpired:
      type: object
      properties:
        e:
          type: string
          enum:
            - listenKeyExpired
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1576653824250
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        listenKey:
          type: string
          example: WsCMN0a4KHUPTQuX6IUnqEZfB1inxmv1qR4kbf1LuEjur5VdbzqvyxqG9TSjVVxv
    marginCall:
      type: object
      properties:
        e:
          type: string
          enum:
            - MARGIN_CALL
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1587727187525
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        i:
          type: string
          example: SfsR
          description: Account Alias
          x-description-cn: 账户唯一识别码 accountAlias
        cw:
          type: string
          example: "3.16812045"
          description: Cross Wallet Balance. Only pushed with crossed position margin call
          x-description-cn: 除去逐仓仓位保证金的钱包余额, 仅在全仓 margin call 情况下推送此字段
        p:
          type: array
          description: Position(s) of Margin Call
          x-description-cn: 涉及持仓
          items:
            type: object
            properties:
              s:
                type: string
                example: BTCUSD_200925
                description: Symbol
                x-description-cn: Symbol
              ps:
                type: string
                example: LONG
                description: Position Side
                x-description-cn: 持仓方向
              pa:
                type: string
                example: "132"
                description: Position Amount
                x-description-cn: 仓位
              mt:
                type: string
                example: CROSSED
                description: Margin Type
                x-description-cn: 保证金模式
              iw:
                type: string
                example: "0"
                description: Isolated Wallet (if isolated position)
                x-description-cn: 若为逐仓，仓位保证金
              mp:
                type: string
                example: "9187.17127000"
                description: Mark Price
                x-description-cn: 标记价格
              up:
                type: string
                example: "-1.166074"
                description: Unrealized PnL
                x-description-cn: 未实现盈亏
              mm:
                type: string
                example: "1.614445"
                description: Maintenance Margin Required
                x-description-cn: 持仓需要的维持保证金
    orderTradeUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - ORDER_TRADE_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1591274595442
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1591274595442
          format: int64
          description: Transaction Time
          x-description-cn: 撮合时间
        i:
          type: string
          example: SfsR
          description: Account Alias
          x-description-cn: 账户唯一识别码 accountAlias
        o:
          type: object
          properties:
            s:
              type: string
              example: BTCUSD_200925
              description: Symbol
              x-description-cn: 交易对
            c:
              type: string
              example: TEST
              description: Client Order Id
              x-description-cn: 客户端自定订单ID
            S:
              type: string
              example: SELL
              description: Side
              x-description-cn: 订单方向
            o:
              type: string
              example: TRAILING_STOP_MARKET
              description: Order Type
              x-description-cn: 订单类型
            f:
              type: string
              example: GTC
              description: Time in Force
              x-description-cn: 有效方式
            q:
              type: string
              example: "2"
              description: Original Quantity
              x-description-cn: 订单原始数量
            p:
              type: string
              example: "0"
              description: Original Price
              x-description-cn: 订单原始价格
            ap:
              type: string
              example: "0"
              description: Average Price
              x-description-cn: 订单平均价格
            sp:
              type: string
              example: "9103.1"
              description: Stop Price. Please ignore with TRAILING_STOP_MARKET order
              x-description-cn: 订单停止价格
            x:
              type: string
              example: NEW
              description: Execution Type
              x-description-cn: 本次事件的具体执行类型
            X:
              type: string
              example: NEW
              description: Order Status
              x-description-cn: 订单的当前状态
            i:
              type: integer
              example: 8888888
              format: int64
              description: Order Id
              x-description-cn: 订单ID
            M:
              type: string
              example: "44444"
              description: >-
                modifyId, only pushed for AMENDMENT (order modification) events when a modifyId was provided in the
                request
              x-description-cn: 改单标识 modifyId，仅在改单(AMENDMENT)事件且请求中传入时推送
            l:
              type: string
              example: "0"
              description: Order Last Filled Quantity
              x-description-cn: 订单末次成交量
            z:
              type: string
              example: "0"
              description: Order Filled Accumulated Quantity
              x-description-cn: 订单累计已成交量
            L:
              type: string
              example: "0"
              description: Last Filled Price
              x-description-cn: 订单末次成交价格
            ma:
              type: string
              example: BTC
              description: Margin Asset
              x-description-cn: 保证金资产类型
            "N":
              type: string
              example: BTC
              description: Commission Asset
              x-description-cn: 该成交手续费资产类型
            "n":
              type: string
              example: "0"
              description: Commission
              x-description-cn: 该成交手续费数量
            T:
              type: integer
              example: 1591274595442
              format: int64
              description: Order Trade Time
              x-description-cn: 成交时间
            t:
              type: integer
              example: 0
              format: int64
              description: Trade Id
              x-description-cn: 成交ID
            rp:
              type: string
              example: "0"
              description: Realized Profit of the trade
              x-description-cn: 该成交已实现盈亏
            b:
              type: string
              example: "0"
              description: Bid quantity of base asset
              x-description-cn: 买单净值
            a:
              type: string
              example: "0"
              description: Ask quantity of base asset
              x-description-cn: 卖单净值
            m:
              type: boolean
              example: false
              description: Is this trade the maker side?
              x-description-cn: 该成交是作为挂单成交吗？
            R:
              type: boolean
              example: false
              description: Is this reduce only
              x-description-cn: 是否是只减仓单
            wt:
              type: string
              example: CONTRACT_PRICE
              description: Stop Price Working Type
              x-description-cn: 触发价类型
            ot:
              type: string
              example: TRAILING_STOP_MARKET
              description: Original Order Type
              x-description-cn: 原始订单类型
            ps:
              type: string
              example: LONG
              description: Position Side
              x-description-cn: 持仓方向
            cp:
              type: boolean
              example: false
              description: If Close-All, pushed with conditional order
              x-description-cn: 是否为触发平仓单
            AP:
              type: string
              example: "9476.8"
              description: Activation Price, only pushed with TRAILING_STOP_MARKET order
              x-description-cn: 追踪止损激活价格
            cr:
              type: string
              example: "5.0"
              description: Callback Rate, only pushed with TRAILING_STOP_MARKET order
              x-description-cn: 追踪止损回调比例
            pP:
              type: boolean
              example: false
              description: If conditional order trigger is protected
              x-description-cn: 是否开启条件单触发保护
            V:
              type: string
              example: EXPIRE_TAKER
              description: STP mode
              x-description-cn: 自成交防止模式
            pm:
              type: string
              example: OPPONENT
              description: Price match mode
              x-description-cn: 价格匹配模式
            er:
              type: string
              example: "0"
              description: Expiry Reason
              x-description-cn: 过期原因
    strategyUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - STRATEGY_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        T:
          type: integer
          example: 1669261797627
          format: int64
          description: Transaction Time
          x-description-cn: 撮合时间
        E:
          type: integer
          example: 1669261797628
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        su:
          type: object
          properties:
            si:
              type: integer
              example: 176054594
              format: int64
              description: Strategy ID
              x-description-cn: 策略 ID
            st:
              type: string
              example: GRID
              description: Strategy Type
              x-description-cn: 策略类型
            ss:
              type: string
              example: NEW
              description: Strategy Status
              x-description-cn: 策略状态
            s:
              type: string
              example: BTCUSDT
              description: Symbol
              x-description-cn: 交易对
            ut:
              type: integer
              example: 1669261797627
              format: int64
              description: Update Time
              x-description-cn: 更新时间
            c:
              type: integer
              example: 8007
              format: int64
              description: opCode
              x-description-cn: opCode
    User Data Stream Events:
      oneOf:
        - $ref: "#/components/schemas/accountConfigUpdate"
        - $ref: "#/components/schemas/accountUpdate"
        - $ref: "#/components/schemas/gridUpdate"
        - $ref: "#/components/schemas/listenKeyExpired"
        - $ref: "#/components/schemas/marginCall"
        - $ref: "#/components/schemas/orderTradeUpdate"
        - $ref: "#/components/schemas/strategyUpdate"
      discriminator:
        propertyName: e
        mapping:
          ACCOUNT_CONFIG_UPDATE: "#/components/schemas/accountConfigUpdate"
          ACCOUNT_UPDATE: "#/components/schemas/accountUpdate"
          GRID_UPDATE: "#/components/schemas/gridUpdate"
          listenKeyExpired: "#/components/schemas/listenKeyExpired"
          MARGIN_CALL: "#/components/schemas/marginCall"
          ORDER_TRADE_UPDATE: "#/components/schemas/orderTradeUpdate"
          STRATEGY_UPDATE: "#/components/schemas/strategyUpdate"
```