---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:45.559054
---

# core-trading-derivatives-trading-options__ws-streams spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Options WebSocket Market Streams
  description: Access market data, manage accounts, and trade Binance Options.
  x-description-cn: 访问市场数据、管理账户，并交易 Binance 期权。
  version: 1.0.0
x-product-type: ws-streams
x-user-data-streams: true
tags:
  - name: public
    x-displayName: Public
    x-displayName-cn: 公开
    x-url-segment: /public
  - name: market
    x-displayName: Market
    x-displayName-cn: 市场
    x-url-segment: /market
servers:
  - url: wss://fstream.binance.com
  - url: wss://fstream.binancefuture.com
paths:
  /!index@arr:
    post:
      summary: Index Price Streams
      x-summary-cn: 指数价格
      description: Underlying(e.g ETHUSDT) index stream.
      x-description-cn: 指数价格
      tags:
        - market
      operationId: indexPriceStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/market#index-price-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/indexPriceStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/index_price_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/index_price_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//market/IndexPriceStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//MarketAPI/IndexPriceStreams/IndexPriceStreams.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
                    - "!index@arr"
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
                - "!index@arr"
              id: 532601580
      responses:
        Raw Stream:
          description: Index Price Streams
          x-description-cn: 指数价格流
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: indexPrice
                      description: event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      example: 1763092572229
                      format: int64
                      description: time
                      x-description-cn: 时间
                    s:
                      type: string
                      example: ETHUSDT
                      description: underlying symbol
                      x-description-cn: 标的交易对
                    p:
                      type: string
                      example: "3224.51976744"
                      description: index price
                      x-description-cn: 指数价格
              example:
                - e: indexPrice
                  E: 1763092572229
                  s: ETHUSDT
                  p: "3224.51976744"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!index@arr"
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: indexPrice
                          description: event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          example: 1763092572229
                          format: int64
                          description: time
                          x-description-cn: 时间
                        s:
                          type: string
                          example: ETHUSDT
                          description: underlying symbol
                          x-description-cn: 标的交易对
                        p:
                          type: string
                          example: "3224.51976744"
                          description: index price
                          x-description-cn: 指数价格
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!index@arr"
                data:
                  - e: indexPrice
                    E: 1763092572229
                    s: ETHUSDT
                    p: "3224.51976744"
  /{symbol}@kline_{interval}:
    post:
      summary: Kline/Candlestick Streams
      x-summary-cn: K线
      description: >-
        The Kline/Candlestick Stream push updates to the current klines/candlestick every 1000 milliseconds (if
        existing).
      x-description-cn: K线流每1000毫秒推送当前K线更新（如果存在）。
      tags:
        - market
      operationId: klineCandlestickStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/market#kline-candlestick-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/klineCandlestickStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/kline_candlestick_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/kline_candlestick_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//market/KlineCandlestickStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//MarketAPI/KlineCandlestickStreams/KlineCandlestickStreams.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
              - 12h
              - 1d
              - 3d
              - 1w
          description: The interval parameter
          x-description-cn: 间隔参数
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
                - btcusdt@kline_1m
              id: 532601580
      responses:
        Raw Stream:
          description: Kline/Candlestick Streams
          x-description-cn: K 线流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: kline
                    description: event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1638747660000
                    format: int64
                    description: event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTC-200630-9000-P
                    description: Option trading symbol
                    x-description-cn: 交易对
                  k:
                    type: object
                    properties:
                      t:
                        type: integer
                        example: 1638747660000
                        format: int64
                        description: kline start time
                        x-description-cn: 这根K线的起始时间
                      T:
                        type: integer
                        example: 1638747719999
                        format: int64
                        description: kline end time
                        x-description-cn: 这根K线的结束时间
                      s:
                        type: string
                        example: BTC-200630-9000-P
                        description: Option trading symbol
                        x-description-cn: 交易对
                      i:
                        type: string
                        example: 1m
                        description: candle period
                        x-description-cn: K线间隔
                      f:
                        type: integer
                        example: 0
                        format: int64
                        description: first trade ID
                        x-description-cn: 这根K线期间第一笔成交ID
                      L:
                        type: integer
                        example: 0
                        format: int64
                        description: last trade ID
                        x-description-cn: 这根K线期间末一笔成交ID
                      o:
                        type: string
                        example: "1000"
                        description: open
                        x-description-cn: 这根K线期间第一笔成交价
                      c:
                        type: string
                        example: "1000"
                        description: close
                        x-description-cn: 这根K线期间末一笔成交价
                      h:
                        type: string
                        example: "1000"
                        description: high
                        x-description-cn: 这根K线期间最高成交价
                      l:
                        type: string
                        example: "1000"
                        description: low
                        x-description-cn: 这根K线期间最低成交价
                      v:
                        type: string
                        example: "0"
                        description: volume(in contracts)
                        x-description-cn: 这根K线期间成交量
                      "n":
                        type: integer
                        example: 0
                        format: int64
                        description: number of trades
                        x-description-cn: 这根K线期间成交笔数
                      x:
                        type: boolean
                        example: false
                        description: current candle has been completed Y/N
                        x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                      q:
                        type: string
                        example: "0"
                        description: "completed trade amount \_ (in quote asset)"
                        x-description-cn: 这根K线期间成交额
                      V:
                        type: string
                        example: "0"
                        description: taker completed trade volume (in contracts)
                        x-description-cn: 主动买入的成交额
                      Q:
                        type: string
                        example: "0"
                        description: taker trade amount(in quote asset)
                        x-description-cn: 主动买入的成交量
                    description: k
                    x-description-cn: K 线数据
              example:
                e: kline
                E: 1638747660000
                s: BTC-200630-9000-P
                k:
                  t: 1638747660000
                  T: 1638747719999
                  s: BTC-200630-9000-P
                  i: 1m
                  f: 0
                  L: 0
                  o: "1000"
                  c: "1000"
                  h: "1000"
                  l: "1000"
                  v: "0"
                  "n": 0
                  x: false
                  q: "0"
                  V: "0"
                  Q: "0"
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
                        description: event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1638747660000
                        format: int64
                        description: event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTC-200630-9000-P
                        description: Option trading symbol
                        x-description-cn: 交易对
                      k:
                        type: object
                        properties:
                          t:
                            type: integer
                            example: 1638747660000
                            format: int64
                            description: kline start time
                            x-description-cn: 这根K线的起始时间
                          T:
                            type: integer
                            example: 1638747719999
                            format: int64
                            description: kline end time
                            x-description-cn: 这根K线的结束时间
                          s:
                            type: string
                            example: BTC-200630-9000-P
                            description: Option trading symbol
                            x-description-cn: 交易对
                          i:
                            type: string
                            example: 1m
                            description: candle period
                            x-description-cn: K线间隔
                          f:
                            type: integer
                            example: 0
                            format: int64
                            description: first trade ID
                            x-description-cn: 这根K线期间第一笔成交ID
                          L:
                            type: integer
                            example: 0
                            format: int64
                            description: last trade ID
                            x-description-cn: 这根K线期间末一笔成交ID
                          o:
                            type: string
                            example: "1000"
                            description: open
                            x-description-cn: 这根K线期间第一笔成交价
                          c:
                            type: string
                            example: "1000"
                            description: close
                            x-description-cn: 这根K线期间末一笔成交价
                          h:
                            type: string
                            example: "1000"
                            description: high
                            x-description-cn: 这根K线期间最高成交价
                          l:
                            type: string
                            example: "1000"
                            description: low
                            x-description-cn: 这根K线期间最低成交价
                          v:
                            type: string
                            example: "0"
                            description: volume(in contracts)
                            x-description-cn: 这根K线期间成交量
                          "n":
                            type: integer
                            example: 0
                            format: int64
                            description: number of trades
                            x-description-cn: 这根K线期间成交笔数
                          x:
                            type: boolean
                            example: false
                            description: current candle has been completed Y/N
                            x-description-cn: 这根K线是否完结(是否已经开始下一根K线)
                          q:
                            type: string
                            example: "0"
                            description: "completed trade amount \_ (in quote asset)"
                            x-description-cn: 这根K线期间成交额
                          V:
                            type: string
                            example: "0"
                            description: taker completed trade volume (in contracts)
                            x-description-cn: 主动买入的成交额
                          Q:
                            type: string
                            example: "0"
                            description: taker trade amount(in quote asset)
                            x-description-cn: 主动买入的成交量
                        description: k
                        x-description-cn: K 线数据
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@kline_1m
                data:
                  e: kline
                  E: 1638747660000
                  s: BTC-200630-9000-P
                  k:
                    t: 1638747660000
                    T: 1638747719999
                    s: BTC-200630-9000-P
                    i: 1m
                    f: 0
                    L: 0
                    o: "1000"
                    c: "1000"
                    h: "1000"
                    l: "1000"
                    v: "0"
                    "n": 0
                    x: false
                    q: "0"
                    V: "0"
                    Q: "0"
  /{underlying}@optionMarkPrice:
    post:
      summary: Option Mark Price
      x-summary-cn: 标记价格
      description: >-
        The mark price for all option symbols on specific underlying asset.
        E.g.[btcusdt@optionMarkPrice](wss://fstream.binance.com/market/stream?streams=btcusdt@optionMarkPrice)
      x-description-cn: >-
        特定标的资产的所有期权交易对的标记价格。例如：[btcusdt@optionMarkPrice](wss://fstream.binance.com/market/stream?streams=btcusdt@optionMarkPrice)
      tags:
        - market
      operationId: optionMarkPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/market#option-mark-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/optionMarkPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/option_mark_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/option_mark_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//market/OptionMarkPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//MarketAPI/OptionMarkPrice/OptionMarkPrice.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
        - name: underlying
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The underlying parameter
          x-description-cn: 标的资产参数
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
                    - btcusdt@optionMarkPrice
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
                - btcusdt@optionMarkPrice
              id: 532601580
      responses:
        Raw Stream:
          description: Mark Price
          x-description-cn: 标记价格
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    s:
                      type: string
                      example: BTC-251120-126000-C
                      description: Symbol
                      x-description-cn: 交易对
                    mp:
                      type: string
                      example: "770.543"
                      description: Mark price
                      x-description-cn: 标记价格
                    E:
                      type: integer
                      example: 1762867543321
                      format: int64
                      description: Event time
                      x-description-cn: 事件时间
                    e:
                      type: string
                      example: markPrice
                      description: Event type
                      x-description-cn: 事件类型
                    i:
                      type: string
                      example: "104334.60217391"
                      description: Index price
                      x-description-cn: 指数价格
                    P:
                      type: string
                      example: "0.000"
                      description: Estimated Settle Price, only useful in the 0.5 hour before the settlement starts
                      x-description-cn: 预估结算价，结算前半小时有效
                    bo:
                      type: string
                      example: "0.000"
                      description: The best buy price
                      x-description-cn: 买一价格
                    ao:
                      type: string
                      example: "900.000"
                      description: The best sell price
                      x-description-cn: 卖一价格
                    bq:
                      type: string
                      example: "0.0000"
                      description: The best buy quantity
                      x-description-cn: 买一数量
                    aq:
                      type: string
                      example: "0.2000"
                      description: The best sell quantity
                      x-description-cn: 卖一数量
                    b:
                      type: string
                      example: "-1.0"
                      description: BuyImplied volatility
                      x-description-cn: 买一隐含波动率
                    a:
                      type: string
                      example: "0.98161161"
                      description: SellImplied volatility
                      x-description-cn: 卖一隐含波动率
                    hl:
                      type: string
                      example: "924.652"
                      description: Buy Maximum price
                      x-description-cn: 最高买价
                    ll:
                      type: string
                      example: "616.435"
                      description: Sell Minimum price
                      x-description-cn: 最低卖价
                    vo:
                      type: string
                      example: "0.9408058"
                      description: volatility
                      x-description-cn: 隐含波动率
                    rf:
                      type: string
                      example: "0.0"
                      description: risk free rate
                      x-description-cn: 无风险利率
                    d:
                      type: string
                      example: "0.11111964"
                      description: delta
                      x-description-cn: 德尔塔
                    t:
                      type: string
                      example: "-164.26702615"
                      description: theta
                      x-description-cn: 西塔
                    g:
                      type: string
                      example: "0.00001245"
                      description: gamma
                      x-description-cn: 伽马
                    v:
                      type: string
                      example: "30.63855919"
                      description: vega
                      x-description-cn: 维加
              example:
                - s: BTC-251120-126000-C
                  mp: "770.543"
                  E: 1762867543321
                  e: markPrice
                  i: "104334.60217391"
                  P: "0.000"
                  bo: "0.000"
                  ao: "900.000"
                  bq: "0.0000"
                  aq: "0.2000"
                  b: "-1.0"
                  a: "0.98161161"
                  hl: "924.652"
                  ll: "616.435"
                  vo: "0.9408058"
                  rf: "0.0"
                  d: "0.11111964"
                  t: "-164.26702615"
                  g: "0.00001245"
                  v: "30.63855919"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@optionMarkPrice
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        s:
                          type: string
                          example: BTC-251120-126000-C
                          description: Symbol
                          x-description-cn: 交易对
                        mp:
                          type: string
                          example: "770.543"
                          description: Mark price
                          x-description-cn: 标记价格
                        E:
                          type: integer
                          example: 1762867543321
                          format: int64
                          description: Event time
                          x-description-cn: 事件时间
                        e:
                          type: string
                          example: markPrice
                          description: Event type
                          x-description-cn: 事件类型
                        i:
                          type: string
                          example: "104334.60217391"
                          description: Index price
                          x-description-cn: 指数价格
                        P:
                          type: string
                          example: "0.000"
                          description: Estimated Settle Price, only useful in the 0.5 hour before the settlement starts
                          x-description-cn: 预估结算价，结算前半小时有效
                        bo:
                          type: string
                          example: "0.000"
                          description: The best buy price
                          x-description-cn: 买一价格
                        ao:
                          type: string
                          example: "900.000"
                          description: The best sell price
                          x-description-cn: 卖一价格
                        bq:
                          type: string
                          example: "0.0000"
                          description: The best buy quantity
                          x-description-cn: 买一数量
                        aq:
                          type: string
                          example: "0.2000"
                          description: The best sell quantity
                          x-description-cn: 卖一数量
                        b:
                          type: string
                          example: "-1.0"
                          description: BuyImplied volatility
                          x-description-cn: 买一隐含波动率
                        a:
                          type: string
                          example: "0.98161161"
                          description: SellImplied volatility
                          x-description-cn: 卖一隐含波动率
                        hl:
                          type: string
                          example: "924.652"
                          description: Buy Maximum price
                          x-description-cn: 最高买价
                        ll:
                          type: string
                          example: "616.435"
                          description: Sell Minimum price
                          x-description-cn: 最低卖价
                        vo:
                          type: string
                          example: "0.9408058"
                          description: volatility
                          x-description-cn: 隐含波动率
                        rf:
                          type: string
                          example: "0.0"
                          description: risk free rate
                          x-description-cn: 无风险利率
                        d:
                          type: string
                          example: "0.11111964"
                          description: delta
                          x-description-cn: 德尔塔
                        t:
                          type: string
                          example: "-164.26702615"
                          description: theta
                          x-description-cn: 西塔
                        g:
                          type: string
                          example: "0.00001245"
                          description: gamma
                          x-description-cn: 伽马
                        v:
                          type: string
                          example: "30.63855919"
                          description: vega
                          x-description-cn: 维加
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@optionMarkPrice
                data:
                  - s: BTC-251120-126000-C
                    mp: "770.543"
                    E: 1762867543321
                    e: markPrice
                    i: "104334.60217391"
                    P: "0.000"
                    bo: "0.000"
                    ao: "900.000"
                    bq: "0.0000"
                    aq: "0.2000"
                    b: "-1.0"
                    a: "0.98161161"
                    hl: "924.652"
                    ll: "616.435"
                    vo: "0.9408058"
                    rf: "0.0"
                    d: "0.11111964"
                    t: "-164.26702615"
                    g: "0.00001245"
                    v: "30.63855919"
  /!optionSymbol:
    post:
      summary: New Symbol Info
      x-summary-cn: 新增交易对信息推送
      description: New symbol listing stream.
      x-description-cn: 新增交易对信息推送
      tags:
        - market
      operationId: newSymbolInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/market#new-symbol-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/newSymbolInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/new_symbol_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/new_symbol_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//market/NewSymbolInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//MarketAPI/NewSymbolInfo/NewSymbolInfo.go
      x-update-speed: 50ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
                    - "!optionSymbol"
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
                - "!optionSymbol"
              id: 532601580
      responses:
        Raw Stream:
          description: New Symbol Info
          x-description-cn: 新增交易对信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: optionSymbol
                    description: Event Type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1669356423908
                    format: int64
                    description: Event Time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: BTC-250926-140000-C
                    description: Symbol
                    x-description-cn: 交易对
                  ps:
                    type: string
                    example: BTCUSDT
                    description: Underlying index of the contract
                    x-description-cn: 标的资产
                  qa:
                    type: string
                    example: USDT
                    description: Quotation asset
                    x-description-cn: 计价资产
                  d:
                    type: string
                    example: CALL
                    description: Option type
                    x-description-cn: 期权类型
                  sp:
                    type: string
                    example: "21000"
                    description: Strike price
                    x-description-cn: 行权价格
                  dt:
                    type: integer
                    example: 4133404800000
                    format: int64
                    description: Delivery date time
                    x-description-cn: 行权时间
                  u:
                    type: integer
                    example: 1
                    format: int64
                    description: unit, the quantity of the underlying asset represented by a single contract.
                    x-description-cn: 一张合约代表的标的数量
                  ot:
                    type: integer
                    example: 1569398400000
                    format: int64
                    description: onboard date time
                    x-description-cn: 上币时间
                  cs:
                    type: string
                    example: TRADING
                    description: Contract status
                    x-description-cn: 合约状态
              example:
                e: optionSymbol
                E: 1669356423908
                s: BTC-250926-140000-C
                ps: BTCUSDT
                qa: USDT
                d: CALL
                sp: "21000"
                dt: 4133404800000
                u: 1
                ot: 1569398400000
                cs: TRADING
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: "!optionSymbol"
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: optionSymbol
                        description: Event Type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1669356423908
                        format: int64
                        description: Event Time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: BTC-250926-140000-C
                        description: Symbol
                        x-description-cn: 交易对
                      ps:
                        type: string
                        example: BTCUSDT
                        description: Underlying index of the contract
                        x-description-cn: 标的资产
                      qa:
                        type: string
                        example: USDT
                        description: Quotation asset
                        x-description-cn: 计价资产
                      d:
                        type: string
                        example: CALL
                        description: Option type
                        x-description-cn: 期权类型
                      sp:
                        type: string
                        example: "21000"
                        description: Strike price
                        x-description-cn: 行权价格
                      dt:
                        type: integer
                        example: 4133404800000
                        format: int64
                        description: Delivery date time
                        x-description-cn: 行权时间
                      u:
                        type: integer
                        example: 1
                        format: int64
                        description: unit, the quantity of the underlying asset represented by a single contract.
                        x-description-cn: 一张合约代表的标的数量
                      ot:
                        type: integer
                        example: 1569398400000
                        format: int64
                        description: onboard date time
                        x-description-cn: 上币时间
                      cs:
                        type: string
                        example: TRADING
                        description: Contract status
                        x-description-cn: 合约状态
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: "!optionSymbol"
                data:
                  e: optionSymbol
                  E: 1669356423908
                  s: BTC-250926-140000-C
                  ps: BTCUSDT
                  qa: USDT
                  d: CALL
                  sp: "21000"
                  dt: 4133404800000
                  u: 1
                  ot: 1569398400000
                  cs: TRADING
  /{underlying}@openInterest@{expirationDate}:
    post:
      summary: Open Interest
      x-summary-cn: 合约持仓量
      description: >-
        Option open interest for specific underlying asset on specific expiration date.
        E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)
      x-description-cn: >-
        特定标的资产特定到期日的期权合约持仓量。如[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)
      tags:
        - market
      operationId: openInterest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/market#open-interest
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/openInterest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/open_interest.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/open_interest.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//market/OpenInterestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//MarketAPI/OpenInterest/OpenInterest.go
      x-update-speed: 60s
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
        - name: underlying
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The underlying parameter
          x-description-cn: 标的资产参数
        - name: expirationDate
          in: path
          required: true
          schema:
            type: string
            example: "220930"
          description: The expirationDate parameter
          x-description-cn: 到期日参数。
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
                    - btcusdt@openInterest@220930
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
                - btcusdt@openInterest@220930
              id: 532601580
      responses:
        Raw Stream:
          description: Open Interest
          x-description-cn: 合约持仓量
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    e:
                      type: string
                      example: openInterest
                      description: Event type
                      x-description-cn: 事件类型
                    E:
                      type: integer
                      format: int64
                      example: 1668759300045
                      description: Event time
                      x-description-cn: 事件时间
                    s:
                      type: string
                      example: ETH-221125-2700-C
                      description: Option symbol
                      x-description-cn: 交易对
                    o:
                      type: string
                      example: "1580.87"
                      description: Open interest in contracts
                      x-description-cn: 持仓量（以张数计）
                    h:
                      type: string
                      example: "1912992.178168204"
                      description: Open interest in USDT
                      x-description-cn: 持仓量（以USDT计）
              example:
                - e: openInterest
                  E: 1668759300045
                  s: ETH-221125-2700-C
                  o: "1580.87"
                  h: "1912992.178168204"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@openInterest@220930
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        e:
                          type: string
                          example: openInterest
                          description: Event type
                          x-description-cn: 事件类型
                        E:
                          type: integer
                          format: int64
                          example: 1668759300045
                          description: Event time
                          x-description-cn: 事件时间
                        s:
                          type: string
                          example: ETH-221125-2700-C
                          description: Option symbol
                          x-description-cn: 交易对
                        o:
                          type: string
                          example: "1580.87"
                          description: Open interest in contracts
                          x-description-cn: 持仓量（以张数计）
                        h:
                          type: string
                          example: "1912992.178168204"
                          description: Open interest in USDT
                          x-description-cn: 持仓量（以USDT计）
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@openInterest@220930
                data:
                  - e: openInterest
                    E: 1668759300045
                    s: ETH-221125-2700-C
                    o: "1580.87"
                    h: "1912992.178168204"
  /{symbol}@depth@{updateSpeed}:
    post:
      summary: Diff Book Depth Streams
      x-summary-cn: 增量深度信息
      description: Bids and asks, pushed every 500 milliseconds, 100 milliseconds (if existing)
      x-description-cn: 买卖盘，每 500 毫秒推送一次，100 毫秒（如果存在）
      tags:
        - public
      operationId: diffBookDepthStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/public#diff-book-depth-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/diffBookDepthStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/diff_book_depth_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/diff_book_depth_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//publicpkg/DiffBookDepthStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//PublicAPI/DiffBookDepthStreams/DiffBookDepthStreams.go
      x-update-speed: 100ms or 500ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
          required: true
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
              - 500ms
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度。
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
                - btcusdt@depth@100ms
              id: 532601580
      responses:
        Raw Stream:
          description: Diff Book Depth Streams
          x-description-cn: 增量深度流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    description: event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1762866729459
                    format: int64
                    description: event time
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    example: 1762866729358
                    format: int64
                    description: transaction time
                    x-description-cn: 撮合时间
                  s:
                    type: string
                    example: BTC-251123-126000-C
                    description: Option symbol
                    x-description-cn: 交易对
                  U:
                    type: integer
                    example: 465
                    format: int64
                    description: First update ID in event
                    x-description-cn: 从上次推送至今新增的第一个 update Id
                  u:
                    type: integer
                    example: 465
                    format: int64
                    description: Final update ID in event
                    x-description-cn: 从上次推送至今新增的最后一个 update Id
                  pu:
                    type: integer
                    example: 464
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
                          example: "1100.000"
                        - type: string
                          description: Quantity
                          example: "0.6000"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            example: "1100.000"
                          - type: string
                            description: Quantity
                            example: "0.6000"
                    description: Buy order
                    x-description-cn: 买方
                  a:
                    type: array
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price level to be updated
                          example: "1300.000"
                        - type: string
                          description: Quantity
                          example: "0.6000"
                      items:
                        oneOf:
                          - type: string
                            description: Price level to be updated
                            example: "1300.000"
                          - type: string
                            description: Quantity
                            example: "0.6000"
                    description: Sell order
                    x-description-cn: 卖方
              example:
                e: depthUpdate
                E: 1762866729459
                T: 1762866729358
                s: BTC-251123-126000-C
                U: 465
                u: 465
                pu: 464
                b:
                  - - "1100.000"
                    - "0.6000"
                a:
                  - - "1300.000"
                    - "0.6000"
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
                        description: event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1762866729459
                        format: int64
                        description: event time
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        example: 1762866729358
                        format: int64
                        description: transaction time
                        x-description-cn: 撮合时间
                      s:
                        type: string
                        example: BTC-251123-126000-C
                        description: Option symbol
                        x-description-cn: 交易对
                      U:
                        type: integer
                        example: 465
                        format: int64
                        description: First update ID in event
                        x-description-cn: 从上次推送至今新增的第一个 update Id
                      u:
                        type: integer
                        example: 465
                        format: int64
                        description: Final update ID in event
                        x-description-cn: 从上次推送至今新增的最后一个 update Id
                      pu:
                        type: integer
                        example: 464
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
                              example: "1100.000"
                            - type: string
                              description: Quantity
                              example: "0.6000"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                example: "1100.000"
                              - type: string
                                description: Quantity
                                example: "0.6000"
                        description: Buy order
                        x-description-cn: 买方
                      a:
                        type: array
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price level to be updated
                              example: "1300.000"
                            - type: string
                              description: Quantity
                              example: "0.6000"
                          items:
                            oneOf:
                              - type: string
                                description: Price level to be updated
                                example: "1300.000"
                              - type: string
                                description: Quantity
                                example: "0.6000"
                        description: Sell order
                        x-description-cn: 卖方
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@depth@100ms
                data:
                  e: depthUpdate
                  E: 1762866729459
                  T: 1762866729358
                  s: BTC-251123-126000-C
                  U: 465
                  u: 465
                  pu: 464
                  b:
                    - - "1100.000"
                      - "0.6000"
                  a:
                    - - "1300.000"
                      - "0.6000"
  /{symbol}@bookTicker:
    post:
      summary: Individual Symbol Book Ticker Streams
      x-summary-cn: 按Symbol的最优挂单信息
      description: Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
      x-description-cn: 实时推送指定交易对的最优挂单价格或数量的任何更新。
      tags:
        - public
      operationId: individualSymbolBookTickerStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/public#individual-symbol-book-ticker-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/individualSymbolBookTickerStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/individual_symbol_book_ticker_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/individual_symbol_book_ticker_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//publicpkg/IndividualSymbolBookTickerStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//PublicAPI/IndividualSymbolBookTickerStreams/IndividualSymbolBookTickerStreams.go
      x-update-speed: Real-Time
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
                - btcusdt@bookTicker
              id: 532601580
      responses:
        Raw Stream:
          description: Individual Symbol Book Ticker Streams
          x-description-cn: 单个交易对最优挂单流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: bookTicker
                    description: event type
                    x-description-cn: 事件类型
                  u:
                    type: integer
                    example: 2472
                    format: int64
                    description: order book updateId
                    x-description-cn: 更新ID
                  s:
                    type: string
                    example: BTC-251226-110000-C
                    description: symbol
                    x-description-cn: 交易对
                  b:
                    type: string
                    example: "5000.000"
                    description: best bid price
                    x-description-cn: 买单最优挂单价格
                  B:
                    type: string
                    example: "0.2000"
                    description: bid bid quantity
                    x-description-cn: 买单最优挂单数量
                  a:
                    type: string
                    example: "5100.000"
                    description: best ask price
                    x-description-cn: 卖单最优挂单价格
                  A:
                    type: string
                    example: "0.1000"
                    description: best ask quantity
                    x-description-cn: 卖单最优挂单数量
                  T:
                    type: integer
                    example: 1763041762942
                    format: int64
                    description: transaction time
                    x-description-cn: 撮合时间
                  E:
                    type: integer
                    example: 1763041762942
                    format: int64
                    description: event time
                    x-description-cn: 事件推送时间
              example:
                e: bookTicker
                u: 2472
                s: BTC-251226-110000-C
                b: "5000.000"
                B: "0.2000"
                a: "5100.000"
                A: "0.1000"
                T: 1763041762942
                E: 1763041762942
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
                        description: event type
                        x-description-cn: 事件类型
                      u:
                        type: integer
                        example: 2472
                        format: int64
                        description: order book updateId
                        x-description-cn: 更新ID
                      s:
                        type: string
                        example: BTC-251226-110000-C
                        description: symbol
                        x-description-cn: 交易对
                      b:
                        type: string
                        example: "5000.000"
                        description: best bid price
                        x-description-cn: 买单最优挂单价格
                      B:
                        type: string
                        example: "0.2000"
                        description: bid bid quantity
                        x-description-cn: 买单最优挂单数量
                      a:
                        type: string
                        example: "5100.000"
                        description: best ask price
                        x-description-cn: 卖单最优挂单价格
                      A:
                        type: string
                        example: "0.1000"
                        description: best ask quantity
                        x-description-cn: 卖单最优挂单数量
                      T:
                        type: integer
                        example: 1763041762942
                        format: int64
                        description: transaction time
                        x-description-cn: 撮合时间
                      E:
                        type: integer
                        example: 1763041762942
                        format: int64
                        description: event time
                        x-description-cn: 事件推送时间
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@bookTicker
                data:
                  e: bookTicker
                  u: 2472
                  s: BTC-251226-110000-C
                  b: "5000.000"
                  B: "0.2000"
                  a: "5100.000"
                  A: "0.1000"
                  T: 1763041762942
                  E: 1763041762942
  /{symbol}@depth{level}@{updateSpeed}:
    post:
      summary: Partial Book Depth Streams
      x-summary-cn: 有限档深度信息
      description: Top <levels> bids and asks. Valid <levels> are 5, 10, 20.
      x-description-cn: 前 <levels> 档买卖盘。有效档位为 5、10、20。
      tags:
        - public
      operationId: partialBookDepthStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/public#partial-book-depth-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/partialBookDepthStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/partial_book_depth_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/partial_book_depth_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//publicpkg/PartialBookDepthStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//PublicAPI/PartialBookDepthStreams/PartialBookDepthStreams.go
      x-update-speed: 100ms or 500ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
        - name: level
          in: path
          required: true
          schema:
            type: string
            example: 5
            enum:
              - 5
              - 10
              - 20
          description: The level parameter
          x-description-cn: level 参数
        - name: updateSpeed
          in: path
          required: true
          schema:
            type: string
            example: 100ms
            enum:
              - 100ms
              - 500ms
          description: WebSocket stream update speed
          x-description-cn: WebSocket 流更新速度。
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
                    - btcusdt@depth5@100ms
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
                - btcusdt@depth5@100ms
              id: 532601580
      responses:
        Raw Stream:
          description: Partial Book Depth Streams
          x-description-cn: 有限档深度流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: depthUpdate
                    description: event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1762866729459
                    format: int64
                    description: event time
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    example: 1762866729358
                    format: int64
                    description: transaction time
                    x-description-cn: 撮合时间
                  s:
                    type: string
                    example: BTC-251123-126000-C
                    description: Option symbol
                    x-description-cn: 交易对
                  U:
                    type: integer
                    example: 465
                    format: int64
                    description: First update ID in event
                    x-description-cn: 从上次推送至今新增的第一个 update Id
                  u:
                    type: integer
                    example: 465
                    format: int64
                    description: Final update ID in event
                    x-description-cn: 从上次推送至今新增的最后一个 update Id
                  pu:
                    type: integer
                    example: 464
                    format: int64
                    description: Final update Id in last stream(ie `u` in last stream)
                    x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                  b:
                    type: array
                    items:
                      type: array
                      items:
                        type: string
                        example: "1100.000"
                    description: Buy order
                    x-description-cn: 买方
                  a:
                    type: array
                    items:
                      type: array
                      items:
                        type: string
                        example: "1300.000"
                    description: Sell order
                    x-description-cn: 卖方
              example:
                e: depthUpdate
                E: 1762866729459
                T: 1762866729358
                s: BTC-251123-126000-C
                U: 465
                u: 465
                pu: 464
                b:
                  - - "1100.000"
                a:
                  - - "1300.000"
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@depth5@100ms
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: depthUpdate
                        description: event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1762866729459
                        format: int64
                        description: event time
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        example: 1762866729358
                        format: int64
                        description: transaction time
                        x-description-cn: 撮合时间
                      s:
                        type: string
                        example: BTC-251123-126000-C
                        description: Option symbol
                        x-description-cn: 交易对
                      U:
                        type: integer
                        example: 465
                        format: int64
                        description: First update ID in event
                        x-description-cn: 从上次推送至今新增的第一个 update Id
                      u:
                        type: integer
                        example: 465
                        format: int64
                        description: Final update ID in event
                        x-description-cn: 从上次推送至今新增的最后一个 update Id
                      pu:
                        type: integer
                        example: 464
                        format: int64
                        description: Final update Id in last stream(ie `u` in last stream)
                        x-description-cn: 上次推送的最后一个update Id(即上条消息的‘u’)
                      b:
                        type: array
                        items:
                          type: array
                          items:
                            type: string
                            example: "1100.000"
                        description: Buy order
                        x-description-cn: 买方
                      a:
                        type: array
                        items:
                          type: array
                          items:
                            type: string
                            example: "1300.000"
                        description: Sell order
                        x-description-cn: 卖方
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@depth5@100ms
                data:
                  e: depthUpdate
                  E: 1762866729459
                  T: 1762866729358
                  s: BTC-251123-126000-C
                  U: 465
                  u: 465
                  pu: 464
                  b:
                    - - "1100.000"
                  a:
                    - - "1300.000"
  /{symbol}@optionTicker{expirationDate}:
    post:
      summary: 24-hour TICKER
      x-summary-cn: 按交易对的Ticker
      description: 24hr ticker info for all symbols. Only symbols whose ticker info changed will be sent.
      x-description-cn: 所有交易对的24小时Ticker信息。只有Ticker信息发生变化的交易对才会被发送。
      tags:
        - public
      operationId: hour24Ticker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/public#hour24-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/hour24Ticker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/hour24_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/hour24_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//publicpkg/Hour24TickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//PublicAPI/Hour24Ticker/Hour24Ticker.go
      x-update-speed: 1000ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
        - name: symbol
          in: path
          required: true
          schema:
            type: string
            example: btcusdt
          description: The symbol parameter
          x-description-cn: 交易对参数
        - name: expirationDate
          in: path
          required: false
          schema:
            type: string
            example: "251230"
          description: The expiration date parameter
          x-description-cn: 到期日参数
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
                    - btcusdt@optionTicker251230
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
                - btcusdt@optionTicker251230
              id: 532601580
      responses:
        Raw Stream:
          description: 24-hour TICKER
          x-description-cn: 24小时Ticker
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
                    example: 1764080707933
                    format: int64
                    description: Event time
                    x-description-cn: 事件时间
                  s:
                    type: string
                    example: ETH-251226-3000-C
                    description: Symbol
                    x-description-cn: 交易对
                  p:
                    type: string
                    example: "0.0000"
                    description: Price change
                    x-description-cn: 价格变化
                  P:
                    type: string
                    example: "0.00"
                    description: Price change percent
                    x-description-cn: 价格变化百分比
                  w:
                    type: string
                    example: "200.0000"
                    description: Weighted average price
                    x-description-cn: 平均价格
                  c:
                    type: string
                    example: "200.0000"
                    description: Last price
                    x-description-cn: 最新价
                  Q:
                    type: string
                    example: "1.0000"
                    description: Last quantity
                    x-description-cn: 最新成交价格上的成交量
                  o:
                    type: string
                    example: "200.0000"
                    description: Open price
                    x-description-cn: 开盘价
                  h:
                    type: string
                    example: "200.0000"
                    description: High price
                    x-description-cn: 最高价
                  l:
                    type: string
                    example: "200.0000"
                    description: Low price
                    x-description-cn: 最低价
                  v:
                    type: string
                    example: "9.0000"
                    description: Trading volume(in contracts)
                    x-description-cn: 成交量张数
                  q:
                    type: string
                    example: "1800.0000"
                    description: trade amount(in quote asset)
                    x-description-cn: 成交金额
                  O:
                    type: integer
                    example: 1764051060000
                    format: int64
                    description: Statistics open time
                    x-description-cn: 统计开始时间
                  C:
                    type: integer
                    example: 1764080707933
                    format: int64
                    description: Statistics close time
                    x-description-cn: 统计结束时间
                  F:
                    type: integer
                    example: 1
                    format: int64
                    description: First trade ID
                    x-description-cn: 24小时内第一笔成交交易ID
                  L:
                    type: integer
                    example: 22
                    format: int64
                    description: Last trade Id
                    x-description-cn: 24小时内最后一笔成交交易ID
                  "n":
                    type: integer
                    example: 9
                    format: int64
                    description: Total number of trade
                    x-description-cn: 24小时内成交数
              example:
                e: 24hrTicker
                E: 1764080707933
                s: ETH-251226-3000-C
                p: "0.0000"
                P: "0.00"
                w: "200.0000"
                c: "200.0000"
                Q: "1.0000"
                o: "200.0000"
                h: "200.0000"
                l: "200.0000"
                v: "9.0000"
                q: "1800.0000"
                O: 1764051060000
                C: 1764080707933
                F: 1
                L: 22
                "n": 9
        Combined Stream:
          description: Stream payload with stream name.
          content:
            application/json:
              schema:
                type: object
                properties:
                  stream:
                    type: string
                    example: btcusdt@optionTicker251230
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
                        example: 1764080707933
                        format: int64
                        description: Event time
                        x-description-cn: 事件时间
                      s:
                        type: string
                        example: ETH-251226-3000-C
                        description: Symbol
                        x-description-cn: 交易对
                      p:
                        type: string
                        example: "0.0000"
                        description: Price change
                        x-description-cn: 价格变化
                      P:
                        type: string
                        example: "0.00"
                        description: Price change percent
                        x-description-cn: 价格变化百分比
                      w:
                        type: string
                        example: "200.0000"
                        description: Weighted average price
                        x-description-cn: 平均价格
                      c:
                        type: string
                        example: "200.0000"
                        description: Last price
                        x-description-cn: 最新价
                      Q:
                        type: string
                        example: "1.0000"
                        description: Last quantity
                        x-description-cn: 最新成交价格上的成交量
                      o:
                        type: string
                        example: "200.0000"
                        description: Open price
                        x-description-cn: 开盘价
                      h:
                        type: string
                        example: "200.0000"
                        description: High price
                        x-description-cn: 最高价
                      l:
                        type: string
                        example: "200.0000"
                        description: Low price
                        x-description-cn: 最低价
                      v:
                        type: string
                        example: "9.0000"
                        description: Trading volume(in contracts)
                        x-description-cn: 成交量张数
                      q:
                        type: string
                        example: "1800.0000"
                        description: trade amount(in quote asset)
                        x-description-cn: 成交金额
                      O:
                        type: integer
                        example: 1764051060000
                        format: int64
                        description: Statistics open time
                        x-description-cn: 统计开始时间
                      C:
                        type: integer
                        example: 1764080707933
                        format: int64
                        description: Statistics close time
                        x-description-cn: 统计结束时间
                      F:
                        type: integer
                        example: 1
                        format: int64
                        description: First trade ID
                        x-description-cn: 24小时内第一笔成交交易ID
                      L:
                        type: integer
                        example: 22
                        format: int64
                        description: Last trade Id
                        x-description-cn: 24小时内最后一笔成交交易ID
                      "n":
                        type: integer
                        example: 9
                        format: int64
                        description: Total number of trade
                        x-description-cn: 24小时内成交数
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@optionTicker251230
                data:
                  e: 24hrTicker
                  E: 1764080707933
                  s: ETH-251226-3000-C
                  p: "0.0000"
                  P: "0.00"
                  w: "200.0000"
                  c: "200.0000"
                  Q: "1.0000"
                  o: "200.0000"
                  h: "200.0000"
                  l: "200.0000"
                  v: "9.0000"
                  q: "1800.0000"
                  O: 1764051060000
                  C: 1764080707933
                  F: 1
                  L: 22
                  "n": 9
  /{symbol}@optionTrade:
    post:
      summary: Trade Streams
      x-summary-cn: 最新交易
      description: >-
        The Trade Streams push raw trade information for specific symbol or underlying asset.
        E.g.[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)
      x-description-cn: >-
        交易流推送特定交易对或标的资产的原始交易信息。例如[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)
      tags:
        - public
      operationId: tradeStreams
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/ws-streams/public#trade-streams
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/websocket-streams/tradeStreams.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/websocket_streams/trade_streams.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/websocket_streams/trade_streams.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/websocket/stream//publicpkg/TradeStreamsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/websocketstreams//PublicAPI/TradeStreams/TradeStreams.go
      x-update-speed: 50ms
      parameters:
        - name: id
          in: query
          required: false
          schema:
            type: integer
            example: 532601580
            format: int32
          description: Unique WebSocket request ID.
          x-description-cn: 唯一 WebSocket 请求 ID。
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
                    - btcusdt@optionTrade
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
                - btcusdt@optionTrade
              id: 532601580
      responses:
        Raw Stream:
          description: Trade Streams
          x-description-cn: 成交流
          content:
            application/json:
              schema:
                type: object
                properties:
                  e:
                    type: string
                    example: trade
                    description: event type
                    x-description-cn: 事件类型
                  E:
                    type: integer
                    example: 1762856064204
                    format: int64
                    description: event time
                    x-description-cn: 事件时间
                  T:
                    type: integer
                    example: 1762856064203
                    format: int64
                    description: trade completed time
                    x-description-cn: 成交完成时间
                  s:
                    type: string
                    example: BTC-251123-126000-C
                    description: Option trading symbol
                    x-description-cn: 交易对
                  t:
                    type: integer
                    example: 4
                    format: int64
                    description: trade ID
                    x-description-cn: 交易ID
                  p:
                    type: string
                    example: "1300.000"
                    description: price
                    x-description-cn: 交易价格
                  q:
                    type: string
                    example: "0.1000"
                    description: quantity, always positive
                    x-description-cn: 交易数量
                  X:
                    type: string
                    example: MARKET
                    description: trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade
                    x-description-cn: 交易类型，"MARKET" 代表订单薄交易, "BLOCK"代表大宗交易
                  S:
                    type: string
                    example: BUY
                    description: direction
                    x-description-cn: 方向
                  m:
                    type: boolean
                    example: false
                    description: Is the buyer the market maker?
                    x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
              example:
                e: trade
                E: 1762856064204
                T: 1762856064203
                s: BTC-251123-126000-C
                t: 4
                p: "1300.000"
                q: "0.1000"
                X: MARKET
                S: BUY
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
                    example: btcusdt@optionTrade
                  data:
                    type: object
                    properties:
                      e:
                        type: string
                        example: trade
                        description: event type
                        x-description-cn: 事件类型
                      E:
                        type: integer
                        example: 1762856064204
                        format: int64
                        description: event time
                        x-description-cn: 事件时间
                      T:
                        type: integer
                        example: 1762856064203
                        format: int64
                        description: trade completed time
                        x-description-cn: 成交完成时间
                      s:
                        type: string
                        example: BTC-251123-126000-C
                        description: Option trading symbol
                        x-description-cn: 交易对
                      t:
                        type: integer
                        example: 4
                        format: int64
                        description: trade ID
                        x-description-cn: 交易ID
                      p:
                        type: string
                        example: "1300.000"
                        description: price
                        x-description-cn: 交易价格
                      q:
                        type: string
                        example: "0.1000"
                        description: quantity, always positive
                        x-description-cn: 交易数量
                      X:
                        type: string
                        example: MARKET
                        description: trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade
                        x-description-cn: 交易类型，"MARKET" 代表订单薄交易, "BLOCK"代表大宗交易
                      S:
                        type: string
                        example: BUY
                        description: direction
                        x-description-cn: 方向
                      m:
                        type: boolean
                        example: false
                        description: Is the buyer the market maker?
                        x-description-cn: 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。
                required:
                  - stream
                  - data
                additionalProperties: false
              example:
                stream: btcusdt@optionTrade
                data:
                  e: trade
                  E: 1762856064204
                  T: 1762856064203
                  s: BTC-251123-126000-C
                  t: 4
                  p: "1300.000"
                  q: "0.1000"
                  X: MARKET
                  S: BUY
                  m: false
components:
  schemas:
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
          example: 1762914568643
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1762914568619
          format: int64
          description: Transaction Time
          x-description-cn: 交易时间
        eq:
          type: string
          example: "10000371.61462086"
          description: Account equity in USDT
          x-description-cn: 账户USDT权益
        aeq:
          type: string
          example: "10000475.51032086"
          description: Account adjusted equity in USDT
          x-description-cn: 账户调整权益
        b:
          type: string
          example: "10000475.51032086"
          description: Account wallet balance in USDT
          x-description-cn: 账户USDT余额
        m:
          type: string
          example: "-103.89570000"
          description: Position value
          x-description-cn: 仓位价值
        u:
          type: string
          example: "16.10430000"
          description: Unrealized PnL
          x-description-cn: 未实现盈利
        i:
          type: string
          example: "32354.38562539"
          description: Initial margin in USDT
          x-description-cn: 初始保证金
        M:
          type: string
          example: "6089.28766956"
          description: Maintenance margin in USDT
          x-description-cn: 维持保证金
    balancePositionUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - BALANCE_POSITION_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1762917544216
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1762917544206
          format: int64
          description: Transaction Time
          x-description-cn: 交易时间
        m:
          type: string
          example: ORDER
          enum:
            - DEPOSIT
            - WITHDRAW
            - ORDER
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
                example: USDT
                description: Margin asset
                x-description-cn: 资产
              b:
                type: string
                example: "10000471.37940900"
                description: Account balance
                x-description-cn: 钱包余额
              bc:
                type: string
                example: "0"
                description: Balance Change except PnL and Commission
                x-description-cn: 除去盈亏与交易手续费以外的钱包余额改变量
        P:
          type: array
          description: Positions
          x-description-cn: 持仓
          items:
            type: object
            properties:
              s:
                type: string
                example: BTC-251123-126000-C
                description: Symbol
                x-description-cn: 交易对
              c:
                type: string
                example: "-0.1000"
                description: Position quantity
                x-description-cn: 仓位
              p:
                type: string
                example: "-120.00000000"
                description: Position value
                x-description-cn: 仓位价值
              a:
                type: string
                example: "1200.00000000"
                description: Average entry price
                x-description-cn: 仓位均价
    greekUpdate:
      type: object
      properties:
        e:
          type: string
          enum:
            - GREEK_UPDATE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1762917544216
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1762917544216
          format: int64
          description: Transaction Time
          x-description-cn: 交易时间
        G:
          type: array
          items:
            type: object
            properties:
              u:
                type: string
                example: BTCUSDT
                description: Underlying
                x-description-cn: 标的
              d:
                type: string
                example: "-0.01304097"
                description: Delta
                x-description-cn: Delta
              g:
                type: string
                example: "-0.00000124"
                description: Gamma
                x-description-cn: Gamma
              t:
                type: string
                example: "16.11648100"
                description: Theta
                x-description-cn: Theta
              v:
                type: string
                example: "-3.83444011"
                description: Vega
                x-description-cn: Vega
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
          type: string
          example: "1736996475556"
          description: Event Time
          x-description-cn: 事件时间
        listenKey:
          type: string
          example: WsCMN0a4KHUPTQuX6IUnqEZfB1inxmv1qR4kbf1LuEjur5VdbzqvyxqG9TSjVVxv
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
          example: 1568879465651
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        T:
          type: integer
          example: 1568879465650
          format: int64
          description: Transaction Time
          x-description-cn: 交易时间
        o:
          type: object
          properties:
            s:
              type: string
              example: BTCUSDT
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
              enum:
                - BUY
                - SELL
              description: Side
              x-description-cn: 方向
            o:
              type: string
              example: TRAILING_STOP_MARKET
              enum:
                - LIMIT
              description: Order Type
              x-description-cn: 订单类型
            f:
              type: string
              example: GTC
              enum:
                - GTC
                - IOC
                - FOK
                - GTX
              description: Time in Force
              x-description-cn: 有效方式
            q:
              type: string
              example: "0.001"
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
            x:
              type: string
              example: NEW
              enum:
                - NEW
                - CANCELED
                - EXPIRED
                - TRADE
              description: Execution Type
              x-description-cn: 本次事件的具体执行类型
            X:
              type: string
              example: NEW
              enum:
                - NEW
                - PARTIALLY_FILLED
                - FILLED
                - CANCELED
                - EXPIRED
                - EXPIRED_IN_MATCH
              description: Order Status
              x-description-cn: 订单的当前状态
            i:
              type: integer
              example: 8886774
              format: int64
              description: Order Id
              x-description-cn: 订单ID
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
            "N":
              type: string
              example: USDT
              description: Commission Asset
              x-description-cn: 手续费资产
            "n":
              type: string
              example: "0"
              description: Commission, negative means fee charge
              x-description-cn: 手续费，负数代表手续费收取
            T:
              type: integer
              example: 1568879465650
              format: int64
              description: Order Trade Time
              x-description-cn: 交易时间
            t:
              type: integer
              example: 0
              format: int64
              description: Trade Id
              x-description-cn: 交易id
            b:
              type: string
              example: "0"
              description: Bids qty
              x-description-cn: 买单总数量
            a:
              type: string
              example: "9.91"
              description: Ask qty
              x-description-cn: 卖单总数量
            m:
              type: boolean
              example: false
              description: Is this trade the maker side?
              x-description-cn: 该成交是作为挂单成交
            R:
              type: boolean
              example: false
              description: Is this reduce only
              x-description-cn: 是否是只减仓单
            ot:
              type: string
              example: TRAILING_STOP_MARKET
              description: Original Order Type
              x-description-cn: 原始订单类型
            rp:
              type: string
              example: "0"
              description: Realized Profit of the trade
              x-description-cn: 该交易实现盈亏
            V:
              type: string
              example: EXPIRE_TAKER
              description: STP mode
              x-description-cn: 自我交易预防模式
    riskLevelChange:
      type: object
      properties:
        e:
          type: string
          enum:
            - RISK_LEVEL_CHANGE
          description: Event Type
          x-description-cn: 事件类型
        E:
          type: integer
          example: 1587727187525
          format: int64
          description: Event Time
          x-description-cn: 事件时间
        s:
          type: string
          example: REDUCE_ONLY
          enum:
            - NORMAL
            - REDUCE_ONLY
          description: >-
            Risk level. This feature only applies to VIP and Market Maker accounts. Risk level is re-evaluated on: funds
            transfer, trade fill, option expiry.
          x-description-cn: 风险等级
        mb:
          type: string
          example: "1534.11708371"
          description: Margin balance
          x-description-cn: 保证金余额
        mm:
          type: string
          example: "254789.11708371"
          description: Maintenance margin
          x-description-cn: 维持保证金
    User Data Stream Events:
      oneOf:
        - $ref: "#/components/schemas/accountUpdate"
        - $ref: "#/components/schemas/balancePositionUpdate"
        - $ref: "#/components/schemas/greekUpdate"
        - $ref: "#/components/schemas/listenKeyExpired"
        - $ref: "#/components/schemas/orderTradeUpdate"
        - $ref: "#/components/schemas/riskLevelChange"
      discriminator:
        propertyName: e
        mapping:
          ACCOUNT_UPDATE: "#/components/schemas/accountUpdate"
          BALANCE_POSITION_UPDATE: "#/components/schemas/balancePositionUpdate"
          GREEK_UPDATE: "#/components/schemas/greekUpdate"
          listenKeyExpired: "#/components/schemas/listenKeyExpired"
          ORDER_TRADE_UPDATE: "#/components/schemas/orderTradeUpdate"
          RISK_LEVEL_CHANGE: "#/components/schemas/riskLevelChange"
```