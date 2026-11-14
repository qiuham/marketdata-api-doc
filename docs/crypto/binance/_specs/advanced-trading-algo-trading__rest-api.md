---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:08.628514
---

# advanced-trading-algo-trading__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Algo Trading REST API
  description: Programmatic access to Binance’s execution algorithms for creating and managing Spot and Futures algo orders.
  x-description-cn: 用于以编程方式访问 Binance 执行算法，以创建和管理现货及期货算法订单.
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/algo/general-info#limits
x-rate-limits-guide-cn: products/algo/general-info#访问限制
x-security-guide: products/algo/general-info#request-security
x-security-guide-cn: products/algo/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Algo Trading docs
  url: https://developers.binance.com/en/docs/products/algo/Introduction
tags:
  - name: future-algo
    x-displayName: Future Algo
    x-displayName-cn: 合约策略
  - name: spot-algo
    x-displayName: Spot Algo
    x-displayName-cn: 现货策略
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/algo/futures/order:
    delete:
      summary: Cancel Futures Algo Order (TRADE)
      x-summary-cn: 取消策略订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 撤销订单
      tags:
        - future-algo
      operationId: cancelAlgoOrderFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#cancel-algo-order-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/cancelAlgoOrderFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/cancel_algo_order_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/cancel_algo_order_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/CancelAlgoOrderFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/CancelAlgoOrderFutureAlgo/CancelAlgoOrderFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/CancelAlgoOrderFutureAlgoExample.php
      x-ip-weight: 1
      x-security-type: TRADE
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
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: eg. 14511
          x-description-cn: 请参见英文说明：eg. 14511
        - name: clientAlgoId
          in: query
          required: false
          schema:
            type: string
            example: 65ce1630101a480b85915d7e11fd5078
          description: eg. "65ce1630101a480b85915d7e11fd5078"
          x-description-cn: 请参见英文说明：eg. "65ce1630101a480b85915d7e11fd5078"
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
      x-parameters-notes: |-
        - Either `algoId` or `clientAlgoId` must be sent.
        - You need to enable `Futures Trading Permission` for the API key that requests this endpoint.
        - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - `algoId` 或 `clientAlgoId` 必须发送其中一个。
        - 请求此接口的 API Key 需要开通 `允许合约交易` 权限。
        - Base URL：`https://api.binance.com`
      responses:
        "200":
          description: Cancel Algo Order
          x-description-cn: 取消策略订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  algoId:
                    type: integer
                    example: 14511
                    format: int64
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
  /sapi/v1/algo/futures/openOrders:
    get:
      summary: Query Current Futures Algo Open Orders (USER_DATA)
      x-summary-cn: 查询当前策略订单挂单 (USER_DATA)
      description: Query Current Algo Open Orders
      x-description-cn: 查询当前策略订单挂单
      tags:
        - future-algo
      operationId: queryCurrentAlgoOpenOrdersFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#query-current-algo-open-orders-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/queryCurrentAlgoOpenOrdersFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/query_current_algo_open_orders_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/query_current_algo_open_orders_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/QueryCurrentAlgoOpenOrdersFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/QueryCurrentAlgoOpenOrdersFutureAlgo/QueryCurrentAlgoOpenOrdersFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/QueryCurrentAlgoOpenOrdersFutureAlgoExample.php
      x-ip-weight: 1
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
      x-parameters-notes: |-
        - You need to enable `Futures Trading Permission` for the API key that requests this endpoint.
        - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - 请求此接口的 API Key 需要开通 `允许合约交易` 权限。
        - Base URL：`https://api.binance.com`
      responses:
        "200":
          description: Current Algo Open Orders
          x-description-cn: 当前策略未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 14517
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        symbol:
                          type: string
                          example: ETHUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: SELL
                          description: Trading side
                          x-description-cn: 买卖方向
                        positionSide:
                          type: string
                          example: SHORT
                          description: Position side
                          x-description-cn: 持仓方向
                        totalQty:
                          type: string
                          example: "5.000"
                          description: Total order quantity
                          x-description-cn: 总下单数量
                        executedQty:
                          type: string
                          example: "0.000"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "0.00000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        avgPrice:
                          type: string
                          example: "0.00"
                          description: Average execution price
                          x-description-cn: 平均价格
                        clientAlgoId:
                          type: string
                          example: d7096549481642f8a0bb69e9e2e31f2e
                          description: Client-defined algo order ID
                          x-description-cn: 用户自定义策略订单 ID
                        bookTime:
                          type: integer
                          example: 1649756817004
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        endTime:
                          type: integer
                          example: 0
                          format: int64
                          description: End time
                          x-description-cn: 结束时间
                        algoStatus:
                          type: string
                          example: WORKING
                          description: Algo order status
                          x-description-cn: 策略订单状态
                        algoType:
                          type: string
                          example: VP
                          description: Algo order type
                          x-description-cn: 策略订单类型
                        urgency:
                          type: string
                          example: LOW
                          description: Execution urgency
                          x-description-cn: 执行速率
  /sapi/v1/algo/futures/historicalOrders:
    get:
      summary: Query Historical Futures Algo Orders (USER_DATA)
      x-summary-cn: 查询历史策略订单 (USER_DATA)
      description: Query Historical Algo Order
      x-description-cn: 查询历史策略订单
      tags:
        - future-algo
      operationId: queryHistoricalAlgoOrdersFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#query-historical-algo-orders-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/queryHistoricalAlgoOrdersFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/query_historical_algo_orders_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/query_historical_algo_orders_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/QueryHistoricalAlgoOrdersFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/QueryHistoricalAlgoOrdersFutureAlgo/QueryHistoricalAlgoOrdersFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/QueryHistoricalAlgoOrdersFutureAlgoExample.php
      x-ip-weight: 1
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
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Trading symbol eg. BTCUSDT
          x-description-cn: 交易对 eg. BTCUSDT
        - name: side
          in: query
          required: false
          schema:
            type: string
            example: BUY
            enum:
              - BUY
              - SELL
          description: BUY or SELL
          x-description-cn: BUY 或者 SELL
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: in milliseconds  eg.1641522717552
          x-description-cn: 毫秒级时间戳  eg.1641522717552
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: in milliseconds  eg.1641522526562
          x-description-cn: 毫秒级时间戳  eg.1641522526562
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Page number
          x-description-cn: 页码
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            example: 100
            format: int64
            minimum: 1
            maximum: 100
            default: 100
          description: Records per page
          x-description-cn: 每页记录数
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
      x-parameters-notes: |-
        - You need to enable `Futures Trading Permission` for the API key that requests this endpoint.
        - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - 请求此接口的 API Key 需要开通 `允许合约交易` 权限。
        - Base URL：`https://api.binance.com`
      responses:
        "200":
          description: Historical Algo Orders
          x-description-cn: 历史策略订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 14518
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        symbol:
                          type: string
                          example: BNBUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: BUY
                          description: Trading side
                          x-description-cn: 买卖方向
                        positionSide:
                          type: string
                          example: BOTH
                          description: Position side
                          x-description-cn: 持仓方向
                        totalQty:
                          type: string
                          example: "100.00"
                          description: Total order quantity
                          x-description-cn: 总下单数量
                        executedQty:
                          type: string
                          example: "0.00"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "0.00000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        avgPrice:
                          type: string
                          example: "0.000"
                          description: Average execution price
                          x-description-cn: 平均价格
                        clientAlgoId:
                          type: string
                          example: acacab56b3c44bef9f6a8f8ebd2a8408
                          description: Client-defined algo order ID
                          x-description-cn: 用户自定义策略订单 ID
                        bookTime:
                          type: integer
                          example: 1649757019503
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        endTime:
                          type: integer
                          example: 1649757088101
                          format: int64
                          description: End time
                          x-description-cn: 结束时间
                        algoStatus:
                          type: string
                          example: CANCELLED
                          description: Algo order status
                          x-description-cn: 策略订单状态
                        algoType:
                          type: string
                          example: VP
                          description: Algo order type
                          x-description-cn: 策略订单类型
                        urgency:
                          type: string
                          example: LOW
                          description: Execution urgency
                          x-description-cn: 执行速率
  /sapi/v1/algo/futures/subOrders:
    get:
      summary: Query Futures Sub Orders (USER_DATA)
      x-summary-cn: 查询执行子订单 (USER_DATA)
      description: Get respective sub orders for a specified algoId
      x-description-cn: 获取指定 algoId 的相应子订单
      tags:
        - future-algo
      operationId: querySubOrdersFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#query-sub-orders-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/querySubOrdersFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/query_sub_orders_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/query_sub_orders_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/QuerySubOrdersFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/QuerySubOrdersFutureAlgo/QuerySubOrdersFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/QuerySubOrdersFutureAlgoExample.php
      x-ip-weight: 1
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
        - name: algoId
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: eg. 14511
          x-description-cn: 例如 14511
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Page number
          x-description-cn: 页码
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            example: 100
            format: int64
            minimum: 1
            maximum: 100
            default: 100
          description: Records per page
          x-description-cn: 每页记录数
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
      x-parameters-notes: |-
        - You need to enable `Futures Trading Permission` for the API key that requests this endpoint.
        - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - 请求此接口的 API Key 需要开通 `允许合约交易` 权限。
        - Base URL：`https://api.binance.com`
      responses:
        "200":
          description: Sub Orders
          x-description-cn: 子订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  executedQty:
                    type: string
                    example: "1.000"
                  executedAmt:
                    type: string
                    example: "3229.44000000"
                  subOrders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 13723
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        orderId:
                          type: integer
                          example: 8389765519993909000
                          format: int64
                          description: Sub-order ID
                          x-description-cn: 子订单 ID
                        orderStatus:
                          type: string
                          example: FILLED
                          description: Sub-order status
                          x-description-cn: 子订单状态
                        executedQty:
                          type: string
                          example: "1.000"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "3229.44000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        feeAmt:
                          type: string
                          example: "-1.61471999"
                          description: Fee amount
                          x-description-cn: 手续费
                        feeAsset:
                          type: string
                          example: USDT
                          description: Fee asset
                          x-description-cn: 手续费币种
                        bookTime:
                          type: integer
                          example: 1649319001964
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        avgPrice:
                          type: string
                          example: "3229.44"
                          description: Average execution price
                          x-description-cn: 平均价格
                        side:
                          type: string
                          example: SELL
                          description: Trading side
                          x-description-cn: 买卖方向
                        symbol:
                          type: string
                          example: ETHUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        subId:
                          type: integer
                          example: 1
                          format: int64
                          description: Sub-order execution sequence ID
                          x-description-cn: 子订单执行顺序 ID
                        timeInForce:
                          type: string
                          example: IMMEDIATE_OR_CANCEL
                          description: Time in force
                          x-description-cn: 有效方式
                        origQty:
                          type: string
                          example: "1.000"
                          description: Original order quantity
                          x-description-cn: 原始委托数量
  /sapi/v1/algo/futures/newOrderTwap:
    post:
      summary: Time-Weighted Futures Average Price (Twap) New Order (TRADE)
      x-summary-cn: 时间加权平均价格策略(Twap)下单 (TRADE)
      description: Send in a Twap new order. Only support on USDⓈ-M Contracts.
      x-description-cn: 发送Twap下单. 仅支持U本位合约
      tags:
        - future-algo
      operationId: timeWeightedAveragePriceFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#time-weighted-average-price-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/timeWeightedAveragePriceFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/time_weighted_average_price_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/time_weighted_average_price_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/TimeWeightedAveragePriceFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/TimeWeightedAveragePriceFutureAlgo/TimeWeightedAveragePriceFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/TimeWeightedAveragePriceFutureAlgoExample.php
      x-security-type: TRADE
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
      x-parameters-notes: |-
        - Other info:
          - Total Algo open orders max allowed: `30` orders.
          - Leverage and position mode follow your futures account settings.
          - Receiving `"success": true` does not guarantee execution; query order endpoints for final status.
          - If balance/position constraints fail, response may still return success but order status becomes `expired`.
          - `quantity * 60 / duration` must be greater than `minQty`.
          - `duration` cannot be less than 5 minutes or greater than 24 hours.
          - For delivery contracts, TWAP end time should be one hour earlier than symbol delivery time.
          - You need to enable the corresponding permission for the API key requesting this endpoint:
            - `Futures Trading Permission` — for Classic Trading Account mode
            - `Portfolio Margin Trading Permission` — for Portfolio Margin Account mode
          - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - 其他说明：
          - 最大策略订单挂单数量：`30`。
          - 杠杆倍数和持仓模式与您的合约账户设置相同。
          - 收到 `"success": true` 不代表订单一定会执行，请通过查询接口确认最终状态。
          - 若余额或持仓限制不满足，接口可能返回 success，但订单状态会为 `expired`。
          - `quantity * 60 / duration` 必须大于 `minQty`。
          - `duration` 不能小于 5 分钟且不能大于 24 小时。
          - 对于交割合约，TWAP 结束时间必须早于交割时间 1 小时。
          - 请求此接口的 API Key 需要开通相应的权限：
            - `允许合约交易` 权限 — 适用于经典交易账户模式
            - `允许组合保证金交易` 权限 — 适用于组合保证金账户模式
          - Base URL：`https://api.binance.com`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - quantity
                - duration
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Trading symbol eg. BTCUSDT
                  x-description-cn: 交易对 eg. BTCUSDT
                side:
                  type: string
                  example: BUY
                  description: Trading side ( BUY or SELL )
                  x-description-cn: 买卖方向 ( BUY or SELL )
                  enum:
                    - BUY
                    - SELL
                positionSide:
                  type: string
                  example: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
                quantity:
                  type: number
                  example: 1
                  format: float
                  description: |-
                    Quantity of base asset; The notional (`quantity` * `mark price(base asset)`) must be more than the
                    equivalent of 1,000 USDT, and the maximum notional varies by symbol: up to 50,000,000 USDT for
                    BTCUSDT perpetual, up to 25,000,000 USDT for ETHUSDT perpetual, and up to 5,000,000 USDT for
                    other symbols
                  x-description-cn: >-
                    下单数量， 以合约币种（base asset）个数下单; 名义价值 (`quantity` * `标记价格(base asset)`) 需要大于 1,000
                    USDT，且上限根据币种有所不同：BTCUSDT永续合约最大为50,000,000

                    USDT，ETHUSDT永续合约最大为25,000,000 USDT，其他币对最大为5,000,000 USDT
                duration:
                  type: integer
                  example: 5000
                  format: int64
                  minimum: 300
                  maximum: 86400
                  description: Duration for TWAP orders in seconds
                  x-description-cn: 请请以秒为单位发送[300,86400]
                clientAlgoId:
                  type: string
                  example: "1"
                  minLength: 32
                  maxLength: 32
                  description: |-
                    A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give
                    default value
                  x-description-cn: 必须传入32位，如果未发送，则自动生成
                reduceOnly:
                  type: boolean
                  example: false
                  description: |-
                    "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a
                    position
                  x-description-cn: true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
                limitPrice:
                  type: number
                  example: 1
                  format: float
                  description: Limit price of the order; If it is not sent, will place order by market price by default
                  x-description-cn: 限价单价格; 若未发送，则以市场价下单
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
          description: Time-Weighted Average Price
          x-description-cn: 时间加权平均价格
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientAlgoId:
                    type: string
                    example: 65ce1630101a480b85915d7e11fd5078
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
  /sapi/v1/algo/futures/newOrderVp:
    post:
      summary: Volume Participation (VP) New Order (TRADE)
      x-summary-cn: 成交量份额参与算法(VP)下单 (TRADE)
      description: Send in a VP new order. Only support on USDⓈ-M Contracts.
      x-description-cn: 发送VP下单. 仅支持U本位合约
      tags:
        - future-algo
      operationId: volumeParticipationFutureAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/future-algo#volume-participation-future-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/FutureAlgoApi/volumeParticipationFutureAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/future_algo_api/volume_participation_future_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/FutureAlgo/volume_participation_future_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/futurealgo/VolumeParticipationFutureAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/FutureAlgoAPI/VolumeParticipationFutureAlgo/VolumeParticipationFutureAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/futurealgo/VolumeParticipationFutureAlgoExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 300
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
        - Other info:
          - Total Algo open orders max allowed: `10` orders.
          - Leverage and position mode follow your futures account settings.
          - Receiving `"success": true` does not guarantee execution; query order endpoints for final status.
          - If balance/position constraints fail, response may still return success but order status becomes `expired`.
          - You need to enable the corresponding permission for the API key requesting this endpoint:
            - `Futures Trading Permission` — for Classic Trading Account mode
            - `Portfolio Margin Trading Permission` — for Portfolio Margin Account mode
          - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: |-
        - 其他说明：
          - 最大策略订单挂单数量：`10`。
          - 杠杆倍数和持仓模式与您的合约账户设置相同。
          - 收到 `"success": true` 不代表订单一定会执行，请通过查询接口确认最终状态。
          - 若余额或持仓限制不满足，接口可能返回 success，但订单状态会为 `expired`。
          - 请求此接口的 API Key 需要开通相应的权限：
            - `允许合约交易` 权限 — 适用于经典交易账户模式
            - `允许组合保证金交易` 权限 — 适用于组合保证金账户模式
          - Base URL：`https://api.binance.com`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - quantity
                - urgency
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Trading symbol eg. BTCUSDT
                  x-description-cn: 交易对 eg. BTCUSDT
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                  description: Trading side ( BUY or SELL )
                  x-description-cn: 买卖方向 ( BUY or SELL )
                positionSide:
                  type: string
                  example: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
                quantity:
                  type: number
                  example: 1
                  format: float
                  description: |-
                    Quantity of base asset; The notional (`quantity` * `mark price(base asset)`) must be more than the
                    equivalent of 10,000 USDT, and the maximum notional varies by symbol: up to 50,000,000 USDT for
                    BTCUSDT perpetual, up to 25,000,000 USDT for ETHUSDT perpetual, and up to 5,000,000 USDT for
                    other symbols
                  x-description-cn: >-
                    下单数量， 以合约币种（base asset）个数下单; 名义价值 (`quantity` * `标记价格(base asset)`) 需要大于 10,000
                    USDT，且上限根据币种有所不同：BTCUSDT永续合约最大为50,000,000

                    USDT，ETHUSDT永续合约最大为25,000,000 USDT，其他币对最大为5,000,000 USDT
                urgency:
                  type: string
                  example: LOW
                  enum:
                    - LOW
                    - MEDIUM
                    - HIGH
                  description: "Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH"
                  x-description-cn: "代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）"
                clientAlgoId:
                  type: string
                  example: "1"
                  minLength: 32
                  maxLength: 32
                  description: |-
                    A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give
                    default value
                  x-description-cn: 必须传入32位，如果未发送，则自动生成
                reduceOnly:
                  type: boolean
                  example: false
                  description: |-
                    "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a
                    position
                  x-description-cn: true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
                limitPrice:
                  type: number
                  example: 1
                  format: float
                  description: Limit price of the order; If it is not sent, will place order by market price by default
                  x-description-cn: 限价单价格; 若未发送，则以市场价下单
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
          description: Volume Participation
          x-description-cn: 成交量份额参与
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientAlgoId:
                    type: string
                    example: 00358ce6a268403398bd34eaa36dffe7
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
  /sapi/v1/algo/spot/order:
    delete:
      summary: Cancel Spot Algo Order (TRADE)
      x-summary-cn: 取消TWAP/VP策略订单 (TRADE)
      description: Cancel an open TWAP or VP algo order
      x-description-cn: 取消正在委托的TWAP或VP订单
      tags:
        - spot-algo
      operationId: cancelAlgoOrderSpotAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#cancel-algo-order-spot-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/cancelAlgoOrderSpotAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/cancel_algo_order_spot_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/cancel_algo_order_spot_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/CancelAlgoOrderSpotAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/CancelAlgoOrderSpotAlgo/CancelAlgoOrderSpotAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/CancelAlgoOrderSpotAlgoExample.php
      x-ip-weight: 1
      x-security-type: TRADE
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
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            example: 14511
            format: int64
        - name: clientAlgoId
          in: query
          required: false
          schema:
            type: string
            example: 65ce1630101a480b85915d7e11fd5078
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
      x-parameters-notes: "- Either `algoId` or `clientAlgoId` must be sent."
      x-parameters-notes-cn: "- `algoId` 或 `clientAlgoId` 必须发送其中一个。"
      responses:
        "200":
          description: Cancel Algo Order
          x-description-cn: 取消策略订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  algoId:
                    type: integer
                    example: 14511
                    format: int64
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
  /sapi/v1/algo/spot/openOrders:
    get:
      summary: Query Current Spot Algo Open Orders (USER_DATA)
      x-summary-cn: 查询当前策略订单挂单 (USER_DATA)
      description: Get all open Spot TWAP and VP algo orders
      x-description-cn: 查询当前策略订单挂单
      tags:
        - spot-algo
      operationId: queryCurrentAlgoOpenOrdersSpotAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#query-current-algo-open-orders-spot-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/queryCurrentAlgoOpenOrdersSpotAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/query_current_algo_open_orders_spot_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/query_current_algo_open_orders_spot_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/QueryCurrentAlgoOpenOrdersSpotAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/QueryCurrentAlgoOpenOrdersSpotAlgo/QueryCurrentAlgoOpenOrdersSpotAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/QueryCurrentAlgoOpenOrdersSpotAlgoExample.php
      x-ip-weight: 1
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
          description: Current Algo Open Orders
          x-description-cn: 当前策略未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 14517
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        symbol:
                          type: string
                          example: ETHUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: SELL
                          description: Trading side
                          x-description-cn: 买卖方向
                        totalQty:
                          type: string
                          example: "5.000"
                          description: Total order quantity
                          x-description-cn: 总下单数量
                        executedQty:
                          type: string
                          example: "0.000"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "0.00000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        avgPrice:
                          type: string
                          example: "0.00"
                          description: Average execution price
                          x-description-cn: 平均价格
                        clientAlgoId:
                          type: string
                          example: d7096549481642f8a0bb69e9e2e31f2e
                          description: Client-defined algo order ID
                          x-description-cn: 用户自定义策略订单 ID
                        bookTime:
                          type: integer
                          example: 1649756817004
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        endTime:
                          type: integer
                          example: 0
                          format: int64
                          description: End time
                          x-description-cn: 结束时间
                        algoStatus:
                          type: string
                          example: WORKING
                          description: Algo order status
                          x-description-cn: 策略订单状态
                        algoType:
                          type: string
                          example: TWAP
                          description: Algo order type
                          x-description-cn: 策略订单类型
                        urgency:
                          type: string
                          example: LOW
                          description: Execution urgency
                          x-description-cn: 执行速率
                        duration:
                          type: integer
                          example: 86400
                          format: int64
                          description: Order duration in seconds. Only returned for TWAP orders
                          x-description-cn: 订单执行时长，以秒为单位，仅 TWAP 订单返回
  /sapi/v1/algo/spot/historicalOrders:
    get:
      summary: Query Historical Spot Algo Orders (USER_DATA)
      x-summary-cn: 查询历史策略订单 (USER_DATA)
      description: Get all historical Spot TWAP and VP algo orders
      x-description-cn: 查询现货TWAP和VP历史订单
      tags:
        - spot-algo
      operationId: queryHistoricalAlgoOrdersSpotAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#query-historical-algo-orders-spot-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/queryHistoricalAlgoOrdersSpotAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/query_historical_algo_orders_spot_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/query_historical_algo_orders_spot_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/QueryHistoricalAlgoOrdersSpotAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/QueryHistoricalAlgoOrdersSpotAlgo/QueryHistoricalAlgoOrdersSpotAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/QueryHistoricalAlgoOrdersSpotAlgoExample.php
      x-ip-weight: 1
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
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Trading symbol
          x-description-cn: 交易对
        - name: side
          in: query
          required: false
          schema:
            type: string
            example: BUY
            enum:
              - BUY
              - SELL
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: in milliseconds  eg.1641522717552
          x-description-cn: 毫秒级时间戳  eg.1641522717552
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: in milliseconds  eg.1641522526562
          x-description-cn: 毫秒级时间戳  eg.1641522526562
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Page number
          x-description-cn: 页码
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            minimum: 1
            maximum: 100
            default: 100
          description: Records per page
          x-description-cn: 每页记录数
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
          description: Historical Algo Orders
          x-description-cn: 历史策略订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 14518
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        symbol:
                          type: string
                          example: BNBUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: BUY
                          description: Trading side
                          x-description-cn: 买卖方向
                        totalQty:
                          type: string
                          example: "100.00"
                          description: Total order quantity
                          x-description-cn: 总下单数量
                        executedQty:
                          type: string
                          example: "0.00"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "0.00000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        avgPrice:
                          type: string
                          example: "0.000"
                          description: Average execution price
                          x-description-cn: 平均价格
                        clientAlgoId:
                          type: string
                          example: acacab56b3c44bef9f6a8f8ebd2a8408
                          description: Client-defined algo order ID
                          x-description-cn: 用户自定义策略订单 ID
                        bookTime:
                          type: integer
                          example: 1649757019503
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        endTime:
                          type: integer
                          example: 1649757088101
                          format: int64
                          description: End time
                          x-description-cn: 结束时间
                        algoStatus:
                          type: string
                          example: CANCELLED
                          description: Algo order status
                          x-description-cn: 策略订单状态
                        algoType:
                          type: string
                          example: TWAP
                          description: Algo order type
                          x-description-cn: 策略订单类型
                        urgency:
                          type: string
                          example: LOW
                          description: Execution urgency
                          x-description-cn: 执行速率
                        duration:
                          type: integer
                          example: 86400
                          format: int64
                          description: Order duration in seconds. Only returned for TWAP orders
                          x-description-cn: 订单执行时长，以秒为单位，仅 TWAP 订单返回
  /sapi/v1/algo/spot/subOrders:
    get:
      summary: Query Spot Sub Orders (USER_DATA)
      x-summary-cn: 查询执行子订单 (USER_DATA)
      description: Get respective sub orders for a specified algoId
      x-description-cn: 获取指定 algoId 的相应子订单
      tags:
        - spot-algo
      operationId: querySubOrdersSpotAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#query-sub-orders-spot-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/querySubOrdersSpotAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/query_sub_orders_spot_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/query_sub_orders_spot_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/QuerySubOrdersSpotAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/QuerySubOrdersSpotAlgo/QuerySubOrdersSpotAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/QuerySubOrdersSpotAlgoExample.php
      x-ip-weight: 1
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
        - name: algoId
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: eg. 14511
          x-description-cn: 例如 14511
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Page number
          x-description-cn: 页码
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            minimum: 1
            maximum: 100
            default: 100
          description: Records per page
          x-description-cn: 每页记录数
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
          description: Sub Orders
          x-description-cn: 子订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  executedQty:
                    type: string
                    example: "1.000"
                  executedAmt:
                    type: string
                    example: "3229.44000000"
                  subOrders:
                    type: array
                    items:
                      type: object
                      properties:
                        algoId:
                          type: integer
                          example: 13723
                          format: int64
                          description: Algo order ID
                          x-description-cn: 策略订单 ID
                        orderId:
                          type: integer
                          example: 8389765519993909000
                          format: int64
                          description: Sub-order ID
                          x-description-cn: 子订单 ID
                        orderStatus:
                          type: string
                          example: FILLED
                          description: Sub-order status
                          x-description-cn: 子订单状态
                        executedQty:
                          type: string
                          example: "1.000"
                          description: Executed quantity
                          x-description-cn: 执行数量
                        executedAmt:
                          type: string
                          example: "3229.44000000"
                          description: Executed amount
                          x-description-cn: 执行金额
                        feeAmt:
                          type: string
                          example: "-1.61471999"
                          description: Fee amount
                          x-description-cn: 手续费
                        feeAsset:
                          type: string
                          example: USDT
                          description: Fee asset
                          x-description-cn: 手续费币种
                        bookTime:
                          type: integer
                          example: 1649319001964
                          format: int64
                          description: Order creation time
                          x-description-cn: 下单时间
                        avgPrice:
                          type: string
                          example: "3229.44"
                          description: Average execution price
                          x-description-cn: 平均价格
                        side:
                          type: string
                          example: SELL
                          description: Trading side
                          x-description-cn: 买卖方向
                        symbol:
                          type: string
                          example: ETHUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        subId:
                          type: integer
                          example: 1
                          format: int64
                          description: Sub-order execution sequence ID
                          x-description-cn: 子订单执行顺序 ID
                        timeInForce:
                          type: string
                          example: IMMEDIATE_OR_CANCEL
                          description: Time in force
                          x-description-cn: 有效方式
                        origQty:
                          type: string
                          example: "1.000"
                          description: Original order quantity
                          x-description-cn: 原始委托数量
  /sapi/v1/algo/spot/newOrderTwap:
    post:
      summary: Time-Weighted Spot Average Price(Twap) New Order (TRADE)
      x-summary-cn: 时间加权平均价格策略(Twap)下单 (TRADE)
      description: Place a new spot TWAP order with Algo service.
      x-description-cn: 通过算法服务进行时间加权平均价格策略（TWAP）下单交易
      tags:
        - spot-algo
      operationId: timeWeightedAveragePriceSpotAlgo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#time-weighted-average-price-spot-algo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/timeWeightedAveragePriceSpotAlgo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/time_weighted_average_price_spot_algo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/time_weighted_average_price_spot_algo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/TimeWeightedAveragePriceSpotAlgoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/TimeWeightedAveragePriceSpotAlgo/TimeWeightedAveragePriceSpotAlgo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/TimeWeightedAveragePriceSpotAlgoExample.php
      x-security-type: TRADE
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
      x-parameters-notes: "- Total Algo open orders max allowed: `20` orders."
      x-parameters-notes-cn: "- 最大策略订单挂单数量：20。"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - quantity
                - duration
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Trading symbol eg. BTCUSDT
                  x-description-cn: 交易对 eg. BTCUSDT
                side:
                  type: string
                  example: BUY
                  description: Trading side ( BUY or SELL )
                  x-description-cn: 买卖方向 ( BUY or SELL )
                  enum:
                    - BUY
                    - SELL
                quantity:
                  type: number
                  example: 1
                  format: float
                  description: |-
                    Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please
                    reduce your size if you order is above the maximum notional per order.
                  x-description-cn: 下单数量， 以Base资产个数下单; 每单支持最大的金额会是200,000， 2,000,000或者10,000,000 USD等额的，取决于币对。请降低您的下单金额，如果您的下单金额超过了上限。
                duration:
                  type: integer
                  example: 5000
                  format: int64
                  minimum: 300
                  maximum: 86400
                  description: Duration for TWAP orders in seconds
                  x-description-cn: 请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h
                clientAlgoId:
                  type: string
                  example: "1"
                  minLength: 32
                  maxLength: 32
                  description: |-
                    A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give
                    default value
                  x-description-cn: 必须传入32位，如果未发送，则自动生成
                limitPrice:
                  type: number
                  example: 1
                  format: float
                  description: Limit price of the order; If it is not sent, will place order by market price by default
                  x-description-cn: 限价单价格; 若未发送，则以市场价下单
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
          description: Time-Weighted Average Price
          x-description-cn: 时间加权平均价格
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientAlgoId:
                    type: string
                    example: 65ce1630101a480b85915d7e11fd5078
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
  /sapi/v1/algo/spot/newOrderVp:
    post:
      summary: Volume Participation (VP) New Order (TRADE)
      x-summary-cn: 成交量份额参与算法(VP)下单 (TRADE)
      description: >-
        Place a new spot VP (Volume Participation) order with Algo service. A VP order automatically slices the total
        quantity over time, targeting a percentage of the market volume.
      x-description-cn: 通过算法服务进行现货成交量份额参与（VP）下单交易。VP 订单会随时间自动拆分总下单数量，目标是参与一定比例的市场成交量。
      tags:
        - spot-algo
      operationId: volumeParticipation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-algo-trading/api/rest-api/spot-algo#volume-participation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/algo/examples/rest-api/SpotAlgoApi/volumeParticipation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/algo/rest_api/spot_algo_api/volume_participation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/algo/examples/rest_api/SpotAlgo/volume_participation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/algo/src/main/java/com/binance/connector/client/algo/rest/spotalgo/VolumeParticipationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/algo/examples/restapi/SpotAlgoAPI/VolumeParticipation/VolumeParticipation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/algo/spotalgo/VolumeParticipationExample.php
      x-security-type: TRADE
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
      x-parameters-notes: >-
        - VP orders do not accept `price` or `timeInForce`; pricing is determined algorithmically based on market
        volume.

        - `urgency` controls the participation rate: LOW = passive, MEDIUM = neutral, HIGH = aggressive.

        - Receiving `"success": true` does not guarantee execution; use the query order endpoints (`GET
        /sapi/v1/algo/spot/openOrders` or `GET /sapi/v1/algo/spot/historicalOrders`) to check the final status.

        - You need to enable the `Spot Trading` permission for the API key requesting this endpoint.

        - Base URL: `https://api.binance.com`
      x-parameters-notes-cn: >-
        - VP 订单不接受 `price` 或 `timeInForce`；价格由算法根据市场成交量自动决定。

        - `urgency` 控制参与速率：LOW = 被动，MEDIUM = 中性，HIGH = 激进。

        - 收到 `"success": true` 不代表订单一定会执行，请通过查询接口（`GET /sapi/v1/algo/spot/openOrders` 或 `GET
        /sapi/v1/algo/spot/historicalOrders`）确认最终状态。

        - 请求此接口的 API Key 需要开通 `允许现货交易` 权限。

        - Base URL：`https://api.binance.com`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - quantity
                - urgency
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Trading symbol eg. BTCUSDT
                  x-description-cn: 交易对 eg. BTCUSDT
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                  description: Trading side ( BUY or SELL )
                  x-description-cn: 买卖方向 ( BUY or SELL )
                quantity:
                  type: number
                  example: 1
                  format: float
                  description: >-
                    Total order quantity in base asset; The notional must be at least the equivalent of 1,000 USDT, and
                    the

                    maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if
                    your

                    order is above the maximum notional per order.
                  x-description-cn: >-
                    下单总数量，以 Base 资产个数计；订单金额不得低于等值 1,000 USDT，每单支持的最大金额为 200,000、2,000,000 或 10,000,000 USD
                    等值，取决于币对。如果下单金额超过上限，请降低下单数量。
                urgency:
                  type: string
                  example: LOW
                  enum:
                    - LOW
                    - MEDIUM
                    - HIGH
                  description: "Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH"
                  x-description-cn: "代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）"
                clientAlgoId:
                  type: string
                  example: "1"
                  minLength: 32
                  maxLength: 32
                  description: |-
                    A unique id among Algo orders (length should be 32 characters). If it is not sent, we will give
                    default value. Must be unique across all open Algo orders.
                  x-description-cn: 必须传入32位，如果未发送，则自动生成；需在所有未完成策略订单中唯一
                vpTimeLimit:
                  type: integer
                  example: 5000
                  format: int64
                  minimum: 300
                  maximum: 86400
                  description: >-
                    Max allowed duration in seconds (minimum 300, maximum 86400). If it is not sent, 86400 is used and
                    the

                    order runs until fully filled or cancelled.
                  x-description-cn: 允许的最长执行时间，以秒为单位（最小 300，最大 86400）；若未发送，默认使用 86400，订单将持续执行直至完全成交或被取消
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                  description: Cannot be greater than 60000
                  x-description-cn: 不能大于 60000
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
          description: Volume Participation
          x-description-cn: 成交量份额参与
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientAlgoId:
                    type: string
                    example: 65ce1630101a480b85915d7e11fd5078
                  success:
                    type: boolean
                    example: true
                  code:
                    type: integer
                    example: 0
                    format: int64
                  msg:
                    type: string
                    example: OK
```