---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:56.901335
---

# core-trading-convert__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Convert REST API
  description: Request quotes and execute cryptocurrency conversions via the Convert REST API.
  x-description-cn: 通过 Convert REST API 请求报价并执行加密货币兑换。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/convert/general-info#limits
x-rate-limits-guide-cn: products/convert/general-info#访问限制
x-security-guide: products/convert/general-info#request-security
x-security-guide-cn: products/convert/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Convert docs
  url: https://developers.binance.com/en/docs/products/convert/Introduction
tags:
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 市场数据
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/convert/exchangeInfo:
    get:
      summary: List All Convert Pairs
      x-summary-cn: 查询可交易币对信息
      description: |-
        Query for all convertible token pairs and the tokens’ respective
        upper/lower limits
      x-description-cn: 查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。
      tags:
        - market-data
      operationId: listAllConvertPairs
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/market-data#list-all-convert-pairs
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/MarketDataApi/listAllConvertPairs.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/market_data_api/list_all_convert_pairs.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/MarketData/list_all_convert_pairs.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/marketdata/ListAllConvertPairsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/MarketDataAPI/ListAllConvertPairs/ListAllConvertPairs.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/marketdata/ListAllConvertPairsExample.php
      x-ip-weight: 3000
      parameters:
        - name: fromAsset
          in: query
          required: false
          schema:
            type: string
            example: BTC
          description: User spends coin
          x-description-cn: 用户售出币种
        - name: toAsset
          in: query
          required: false
          schema:
            type: string
            example: USDT
          description: User receives coin
          x-description-cn: 用户买入币种
      x-parameters-notes: |-
        - User needs to supply either or both input parameters.
        - If only one of `fromAsset` and `toAsset` is provided, only partial token pairs are returned.
      x-parameters-notes-cn: |-
        - `fromAsset` 和 `toAsset` 至少填写一个。
        - 若只填写 `fromAsset` 或 `toAsset` 其中一个，仅会返回部分币对信息。
      responses:
        "200":
          description: List All Convert Pairs
          x-description-cn: 查询可交易币对信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    fromAsset:
                      type: string
                      example: BTC
                    toAsset:
                      type: string
                      example: USDT
                    fromAssetMinAmount:
                      type: string
                      example: "0.0004"
                    fromAssetMaxAmount:
                      type: string
                      example: "50"
                    toAssetMinAmount:
                      type: string
                      example: "20"
                    toAssetMaxAmount:
                      type: string
                      example: "2500000"
                      description: 9E+24 signals that this symbol has a very large upper limit close to infinity
                      x-description-cn: 9E+24 表示该交易对的最大上限非常大，可视为接近无穷大
  /sapi/v1/convert/assetInfo:
    get:
      summary: Query order quantity precision per asset (USER_DATA)
      x-summary-cn: 查询可交易币种精度 (USER_DATA)
      description: Query for supported asset’s precision information
      x-description-cn: 查询每个可交易币种的精度信息
      tags:
        - market-data
      operationId: queryOrderQuantityPrecisionPerAsset
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/market-data#query-order-quantity-precision-per-asset
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/MarketDataApi/queryOrderQuantityPrecisionPerAsset.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/market_data_api/query_order_quantity_precision_per_asset.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/MarketData/query_order_quantity_precision_per_asset.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/marketdata/QueryOrderQuantityPrecisionPerAssetExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/MarketDataAPI/QueryOrderQuantityPrecisionPerAsset/QueryOrderQuantityPrecisionPerAsset.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/marketdata/QueryOrderQuantityPrecisionPerAssetExample.php
      x-ip-weight: 100
      x-security-type: USER_DATA
      x-signed: true
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
          description: Request validity window in milliseconds
          x-description-cn: 请求有效时间窗口（毫秒）
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: order quantity precision per asset
          x-description-cn: 查询可交易币种精度
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: BTC
                    fraction:
                      type: integer
                      example: 8
                      format: int64
  /sapi/v1/convert/acceptQuote:
    post:
      summary: Accept Quote (TRADE)
      x-summary-cn: 接受报价 (TRADE)
      description: Accept the offered quote by quote ID.
      x-description-cn: 通过 quote ID 来接受报价。
      tags:
        - trade
      operationId: acceptQuote
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#accept-quote
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/acceptQuote.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/accept_quote.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/accept_quote.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/AcceptQuoteExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/AcceptQuote/AcceptQuote.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/AcceptQuoteExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 500
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - quoteId
                - timestamp
              properties:
                quoteId:
                  type: string
                  example: "1"
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                  description: Request validity window in milliseconds
                  x-description-cn: 请求有效时间窗口（毫秒）
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: |-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Accept Quote
          x-description-cn: 接受报价
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: string
                    example: "933256278426274426"
                  createTime:
                    type: integer
                    example: 1623381330472
                    format: int64
                  orderStatus:
                    type: string
                    example: PROCESS
                    enum:
                      - PROCESS
                      - ACCEPT_SUCCESS
                      - SUCCESS
                      - FAIL
                    description: Order processing status
                    x-description-cn: 订单处理状态
  /sapi/v1/convert/limit/cancelOrder:
    post:
      summary: Cancel limit order (TRADE)
      x-summary-cn: 取消闪兑限价单 (TRADE)
      description: Enable users to cancel a limit order
      x-description-cn: 用户取消闪兑限价单
      tags:
        - trade
      operationId: cancelLimitOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#cancel-limit-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/cancelLimitOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/cancel_limit_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/cancel_limit_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/CancelLimitOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/CancelLimitOrder/CancelLimitOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/CancelLimitOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 200
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - orderId
                - timestamp
              properties:
                orderId:
                  type: integer
                  example: 1603680255057330400
                  format: int64
                  description: The orderId from `placeOrder` api
                  x-description-cn: orderId 在 `placeOrder`接口响应中获得
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                  description: Request validity window in milliseconds
                  x-description-cn: 请求有效时间窗口（毫秒）
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: |-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel limit order
          x-description-cn: 取消闪兑限价单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 1603680255057330400
                    format: int64
                  status:
                    type: string
                    example: CANCELED
  /sapi/v1/convert/tradeFlow:
    get:
      summary: Get Convert Trade History (USER_DATA)
      x-summary-cn: 获取闪兑交易记录 (USER_DATA)
      description: Get Convert Trade History
      x-description-cn: 获取闪兑交易记录
      tags:
        - trade
      operationId: getConvertTradeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#get-convert-trade-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/getConvertTradeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/get_convert_trade_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/get_convert_trade_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/GetConvertTradeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/GetConvertTradeHistory/GetConvertTradeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/GetConvertTradeHistoryExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 3000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 100
            format: int64
            default: 100
            maximum: 1000
          description: Number of records to return
          x-description-cn: 返回记录数量
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
          description: Request validity window in milliseconds
          x-description-cn: 请求有效时间窗口（毫秒）
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- The max interval between `startTime` and `endTime` is 30 days."
      x-parameters-notes-cn: "- `startTime` 和 `endTime` 的最大时间间隔为 30 天。"
      responses:
        "200":
          description: Get Convert Trade History
          x-description-cn: 获取闪兑交易记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  list:
                    type: array
                    items:
                      type: object
                      properties:
                        quoteId:
                          type: string
                          example: f3b91c525b2644c7bc1e1cd31b6e1aa6
                        orderId:
                          type: integer
                          example: 940708407462087200
                          format: int64
                        orderStatus:
                          type: string
                          example: SUCCESS
                          description: Order status
                          x-description-cn: 订单状态
                        fromAsset:
                          type: string
                          example: USDT
                          description: Source asset
                          x-description-cn: 闪兑前币种
                        fromAmount:
                          type: string
                          example: "20"
                          description: Source amount
                          x-description-cn: 闪兑前金额
                        toAsset:
                          type: string
                          example: BNB
                          description: Destination asset
                          x-description-cn: 闪兑后币种
                        toAmount:
                          type: string
                          example: "0.06154036"
                          description: Destination amount
                          x-description-cn: 闪兑后金额
                        ratio:
                          type: string
                          example: "0.00307702"
                          description: Price ratio
                          x-description-cn: 价格
                        inverseRatio:
                          type: string
                          example: "324.99"
                          description: Inverse price ratio
                          x-description-cn: 反向价格
                        createTime:
                          type: integer
                          example: 1624248872184
                          format: int64
                  startTime:
                    type: integer
                    example: 1623824139000
                    format: int64
                  endTime:
                    type: integer
                    example: 1626416139000
                    format: int64
                  limit:
                    type: integer
                    example: 100
                    format: int64
                  moreData:
                    type: boolean
                    example: false
  /sapi/v1/convert/orderStatus:
    get:
      summary: Order status (USER_DATA)
      x-summary-cn: 查询订单状态 (USER_DATA)
      description: Query order status by order ID.
      x-description-cn: 通过 order ID 来查询订单状态。
      tags:
        - trade
      operationId: orderStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#order-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/orderStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/order_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/order_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/OrderStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/OrderStatus/OrderStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/OrderStatusExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 100
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: orderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Either orderId or quoteId is required
          x-description-cn: orderId 和quoteId需要填其中一个
        - name: quoteId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Either orderId or quoteId is required
          x-description-cn: orderId 和quoteId需要填其中一个
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Order status
          x-description-cn: 查询订单状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 933256278426274400
                    format: int64
                  orderStatus:
                    type: string
                    example: SUCCESS
                  fromAsset:
                    type: string
                    example: BTC
                  fromAmount:
                    type: string
                    example: "0.00054414"
                  toAsset:
                    type: string
                    example: USDT
                  toAmount:
                    type: string
                    example: "20"
                  ratio:
                    type: string
                    example: "36755"
                  inverseRatio:
                    type: string
                    example: "0.00002721"
                  createTime:
                    type: integer
                    example: 1623381330472
                    format: int64
  /sapi/v1/convert/limit/placeOrder:
    post:
      summary: Place limit order (TRADE)
      x-summary-cn: 创建闪兑限价单 (TRADE)
      description: Enable users to place a limit order
      x-description-cn: 用户创建闪兑限价单
      tags:
        - trade
      operationId: placeLimitOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#place-limit-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/placeLimitOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/place_limit_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/place_limit_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/PlaceLimitOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/PlaceLimitOrder/PlaceLimitOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/PlaceLimitOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 500
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
      x-parameters-notes: |-
        - `baseAsset` and `quoteAsset` can be determined via the `exchangeInfo` endpoint.
        - Limit price is defined from `baseAsset` to `quoteAsset`.
        - Exactly one of `baseAmount` or `quoteAmount` should be sent.
      x-parameters-notes-cn: |-
        - `baseAsset` 和 `quoteAsset` 可通过 `GET /sapi/v1/convert/exchangeInfo` 接口确定。
        - 限价方向定义为从 `baseAsset` 到 `quoteAsset`。
        - `baseAmount` 和 `quoteAmount` 需且仅需填写一个。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - baseAsset
                - quoteAsset
                - limitPrice
                - side
                - expiredType
                - timestamp
              properties:
                baseAsset:
                  type: string
                  example: BTC
                  description: |-
                    base asset (use the response `fromIsBase` from `GET /sapi/v1/convert/exchangeInfo` api to check
                    which one is baseAsset )
                  x-description-cn: 基础资产（可通过 `GET /sapi/v1/convert/exchangeInfo` 接口中的 `fromIsBase` 字段判断）
                quoteAsset:
                  type: string
                  example: USDT
                  description: quote asset
                  x-description-cn: 报价资产
                limitPrice:
                  type: number
                  example: 1
                  format: float
                  description: Symbol limit price (from baseAsset to quoteAsset)
                  x-description-cn: 币对限价 (从`baseAsset` 到 `quoteAsset`)
                baseAmount:
                  type: number
                  example: 1
                  format: float
                  description: Base asset amount. (One of `baseAmount` or `quoteAmount` is required)
                  x-description-cn: Base asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)
                quoteAmount:
                  type: number
                  example: 1
                  format: float
                  description: Quote asset amount. (One of `baseAmount` or `quoteAmount` is required)
                  x-description-cn: Quote asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)
                side:
                  type: string
                  example: BUY
                  description: "`BUY` or `SELL`"
                  x-description-cn: "`BUY` 或者`SELL`"
                  enum:
                    - BUY
                    - SELL
                walletType:
                  type: string
                  example: SPOT
                  enum:
                    - SPOT
                    - FUNDING
                    - EARN
                    - SPOT_FUNDING
                    - FUNDING_EARN
                    - SPOT_FUNDING_EARN
                    - SPOT_EARN
                  default: SPOT
                  description: >-
                    Wallet to use for payment. Supported values: `SPOT`, `FUNDING`, `EARN`.

                    Combined wallets also supported: `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`.
                    Default is `SPOT`.
                  x-description-cn: |-
                    这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，
                    如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。
                expiredType:
                  type: string
                  example: 1_D
                  enum:
                    - 1_D
                    - 3_D
                    - 7_D
                    - 30_D
                  description: Order expiry duration. 1_D, 3_D, 7_D, 30_D (D means day)
                  x-description-cn: 订单过期时长。1_D, 3_D, 7_D, 30_D (D 指天)
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                  description: Request validity window in milliseconds
                  x-description-cn: 请求有效时间窗口（毫秒）
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: |-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Place limit order
          x-description-cn: 创建闪兑限价单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 1603680255057330400
                    format: int64
                  status:
                    type: string
                    example: PROCESS
  /sapi/v1/convert/limit/queryOpenOrders:
    get:
      summary: Query limit open orders (USER_DATA)
      x-summary-cn: 查询闪兑限价单 (USER_DATA)
      description: Query current open limit orders
      x-description-cn: 查询闪兑限价单
      tags:
        - trade
      operationId: queryLimitOpenOrders
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#query-limit-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/queryLimitOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/query_limit_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/query_limit_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/QueryLimitOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/QueryLimitOpenOrders/QueryLimitOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/QueryLimitOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 3000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
          description: Request validity window in milliseconds
          x-description-cn: 请求有效时间窗口（毫秒）
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: limit open orders
          x-description-cn: 闪兑限价未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  list:
                    type: array
                    items:
                      type: object
                      properties:
                        quoteId:
                          type: string
                          example: 18sdf87kh9df
                        orderId:
                          type: integer
                          example: 1150901289839
                          format: int64
                        orderStatus:
                          type: string
                          example: SUCCESS
                        fromAsset:
                          type: string
                          example: BNB
                        fromAmount:
                          type: string
                          example: "10"
                        toAsset:
                          type: string
                          example: USDT
                        toAmount:
                          type: string
                          example: "2317.89"
                        ratio:
                          type: string
                          example: "231.789"
                        inverseRatio:
                          type: string
                          example: "0.00431427"
                        createTime:
                          type: integer
                          example: 1614089498000
                          format: int64
                        expiredTimestamp:
                          type: integer
                          example: 1614099498000
                          format: int64
  /sapi/v1/convert/getQuote:
    post:
      summary: Send Quote Request (TRADE)
      x-summary-cn: 发送获取报价请求 (TRADE)
      description: Request a quote for the requested token pairs
      x-description-cn: 对所需的币对发送获取报价请求
      tags:
        - trade
      operationId: sendQuoteRequest
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-convert/api/rest-api/trade#send-quote-request
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/convert/examples/rest-api/TradeApi/sendQuoteRequest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/convert/rest_api/trade_api/send_quote_request.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/convert/examples/rest_api/Trade/send_quote_request.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/convert/src/main/java/com/binance/connector/client/convert/rest/trade/SendQuoteRequestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/convert/examples/restapi/TradeAPI/SendQuoteRequest/SendQuoteRequest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/convert/trade/SendQuoteRequestExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 200
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
      x-parameters-notes: |-
        - Either `fromAmount` or `toAmount` should be sent.
        - `quoteId` is returned only if you have enough funds to convert.
      x-parameters-notes-cn: |-
        - `fromAmount` 或 `toAmount` 只需要提供其中一个。
        - `quoteId` 仅在账户余额充足时返回。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - fromAsset
                - toAsset
                - timestamp
              properties:
                fromAsset:
                  type: string
                  example: BTC
                toAsset:
                  type: string
                  example: USDT
                fromAmount:
                  type: number
                  example: 1
                  format: float
                  description: When specified, it is the amount you will be debited after the conversion
                  x-description-cn: 这是成交后将被扣除的金额
                toAmount:
                  type: number
                  example: 1
                  format: float
                  description: When specified, it is the amount you will be credited after the conversion
                  x-description-cn: 这是成交后将会获得的金额
                walletType:
                  type: string
                  example: SPOT
                  enum:
                    - SPOT
                    - FUNDING
                    - EARN
                    - SPOT_FUNDING
                    - FUNDING_EARN
                    - SPOT_FUNDING_EARN
                    - SPOT_EARN
                  default: SPOT
                  description: >-
                    Wallet to use for payment. Supported values: `SPOT`, `FUNDING`, `EARN`.

                    Combined wallets also supported: `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN`, `SPOT_EARN`.
                    Default is `SPOT`.
                  x-description-cn: |-
                    这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，
                    如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。
                validTime:
                  type: string
                  example: 10s
                  enum:
                    - 10s
                    - 30s
                    - 1m
                  default: 10s
                  description: "Quote valid duration. Supported values: 10s, 30s, 1m. Default is 10s."
                  x-description-cn: 可以支持10s、30s、1m等值，默认值为 10s
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                  description: Request validity window in milliseconds
                  x-description-cn: 请求有效时间窗口（毫秒）
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: |-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Send Quote Request
          x-description-cn: 发送获取报价请求
          content:
            application/json:
              schema:
                type: object
                properties:
                  quoteId:
                    type: string
                    example: "12415572564"
                  ratio:
                    type: string
                    example: "38163.7"
                  inverseRatio:
                    type: string
                    example: "0.0000262"
                  validTimestamp:
                    type: integer
                    example: 1623319461670
                    format: int64
                  toAmount:
                    type: string
                    example: "3816.37"
                  fromAmount:
                    type: string
                    example: "0.1"
```