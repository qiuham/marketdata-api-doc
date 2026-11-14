---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:10.939256
---

# core-trading-spot-trading__ws-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Spot WebSocket API
  description: Access market data, manage accounts, and trade on Binance Spot.
  x-description-cn: 访问市场数据、管理账户，并在 Binance 现货市场交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-api
x-rate-limits-guide: products/spot/websocket-api#rate-limits
x-rate-limits-guide-cn: products/spot/websocket-api#rate-limits
x-security-guide: products/spot/websocket-api#request-security
x-security-guide-cn: products/spot/websocket-api#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
x-user-data-streams: true
externalDocs:
  description: Spot docs
  url: https://developers.binance.com/en/docs/products/spot
tags:
  - name: general
    x-displayName: General
    x-displayName-cn: 通用
  - name: market
    x-displayName: Market
    x-displayName-cn: 行情
  - name: auth
    x-displayName: Authentication
    x-displayName-cn: 身份验证
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户
  - name: user-data-stream
    x-displayName: User Data Stream
    x-displayName-cn: 用户数据流
servers:
  - url: wss://ws-api.binance.com:443/ws-api/v3
  - url: wss://demo-ws-api.binance.com:443/ws-api/v3
  - url: wss://ws-api.testnet.binance.vision:443/ws-api/v3
paths:
  /account.commission:
    post:
      summary: Account Commission Rates (USER_DATA)
      x-summary-cn: 账户佣金费率 (USER_DATA)
      description: Get current account commission rates.
      x-description-cn: 获取当前账户的佣金费率。
      tags:
        - account
      operationId: accountCommission
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#account-commission
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/accountCommission.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/account_commission.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/account_commission.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/AccountCommissionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/AccountCommission/AccountCommission.go
      x-ip-weight: 20
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - account.commission
                  example: account.commission
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: account.commission
              params:
                symbol: BNBUSDT
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account Commission Rates
          x-description-cn: 账户佣金费率
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      standardCommission:
                        type: object
                        description: Standard commission rates on trades from the order.
                        x-description-cn: 订单成交的标准佣金率。
                        properties:
                          maker:
                            type: string
                            example: "0.00000010"
                          taker:
                            type: string
                            example: "0.00000020"
                          buyer:
                            type: string
                            example: "0.00000030"
                          seller:
                            type: string
                            example: "0.00000040"
                      specialCommission:
                        type: object
                        description: Special commission rates from the order.
                        x-description-cn: 订单成交的特殊佣金率。
                        properties:
                          maker:
                            type: string
                            example: "0.01000000"
                          taker:
                            type: string
                            example: "0.02000000"
                          buyer:
                            type: string
                            example: "0.03000000"
                          seller:
                            type: string
                            example: "0.04000000"
                      taxCommission:
                        type: object
                        description: Tax commission rates on trades from the order.
                        x-description-cn: 订单成交的税费率。
                        properties:
                          maker:
                            type: string
                            example: "0.00000112"
                          taker:
                            type: string
                            example: "0.00000114"
                          buyer:
                            type: string
                            example: "0.00000118"
                          seller:
                            type: string
                            example: "0.00000116"
                      discount:
                        type: object
                        description: Discount on standard commissions when paying in BNB.
                        x-description-cn: 使用 BNB 支付时的标准佣金折扣信息。
                        properties:
                          enabledForAccount:
                            type: boolean
                            example: true
                          enabledForSymbol:
                            type: boolean
                            example: true
                          discountAsset:
                            type: string
                            example: BNB
                          discount:
                            type: string
                            example: "0.75000000"
                            description: >-
                              Multiplier applied to the standard commission when paying commission in BNB (e.g. 0.75 =
                              75% of the standard commission is charged).
                            x-description-cn: 当用BNB支付佣金时，在标准佣金上按此比率打折。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /account.rateLimits.orders:
    post:
      summary: Unfilled Order Count (USER_DATA)
      x-summary-cn: 查询未成交的订单计数 (USER_DATA)
      description: Query your current unfilled order count for all intervals.
      x-description-cn: 显示用户在所有时间间隔内的未成交订单计数。
      tags:
        - account
      operationId: accountRateLimitsOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#account-rate-limits-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/accountRateLimitsOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/account_rate_limits_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/account_rate_limits_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/AccountRateLimitsOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/AccountRateLimitsOrders/AccountRateLimitsOrders.go
      x-ip-weight: 40
      x-legacy-anchors:
        - query-unfilled-order-count
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - account.rateLimits.orders
                  example: account.rateLimits.orders
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: account.rateLimits.orders
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Unfilled Order Count
          x-description-cn: 查询未成交的订单计数
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3783d8d-f8d1-4d2c-b8a0-b7596af5a664
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: SECOND
                        intervalNum: 10
                        limit: 50
                        count: 0
                      - rateLimitType: ORDERS
                        interval: DAY
                        intervalNum: 1
                        limit: 160000
                        count: 0
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: ORDERS
                        interval:
                          type: string
                          example: SECOND
                        intervalNum:
                          type: integer
                          format: int64
                          example: 10
                        limit:
                          type: integer
                          format: int64
                          example: 50
                        count:
                          type: integer
                          format: int64
                          example: 0
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 40
  /account.status:
    post:
      summary: Account information (USER_DATA)
      x-summary-cn: 账户信息 (USER_DATA)
      description: Query information about your account.
      x-description-cn: 获取当前账户信息。
      tags:
        - account
      operationId: accountStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#account-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/accountStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/account_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/account_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/AccountStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/AccountStatus/AccountStatus.go
      x-ip-weight: 20
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory => Database"
      x-parameters-notes-cn: "**数据源:** 缓存 => 数据库"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - account.status
                  example: account.status
                params:
                  type: object
                  properties:
                    omitZeroBalances:
                      type: boolean
                      example: false
                      default: false
                      description: "When set to `true`, emits only the non-zero balances of an account. Default value: `false`."
                      x-description-cn: 如果`true`，将隐藏所有零余额。默认值：`false`。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: account.status
              params:
                omitZeroBalances: false
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account information
          x-description-cn: 账户信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 605a6d20-6588-4cb9-afa0-b0ab087507ba
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      makerCommission:
                        type: integer
                        format: int64
                        example: 15
                      takerCommission:
                        type: integer
                        format: int64
                        example: 15
                      buyerCommission:
                        type: integer
                        format: int64
                        example: 0
                      sellerCommission:
                        type: integer
                        format: int64
                        example: 0
                      canTrade:
                        type: boolean
                        example: true
                      canWithdraw:
                        type: boolean
                        example: true
                      canDeposit:
                        type: boolean
                        example: true
                      commissionRates:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.00150000"
                          taker:
                            type: string
                            example: "0.00150000"
                          buyer:
                            type: string
                            example: "0.00000000"
                          seller:
                            type: string
                            example: "0.00000000"
                      brokered:
                        type: boolean
                        example: false
                      requireSelfTradePrevention:
                        type: boolean
                        example: false
                      preventSor:
                        type: boolean
                        example: false
                      updateTime:
                        type: integer
                        format: int64
                        example: 1660801833000
                      accountType:
                        type: string
                        example: SPOT
                      balances:
                        type: array
                        example:
                          - asset: BNB
                            free: "0.00000000"
                            locked: "0.00000000"
                          - asset: BTC
                            free: "1.3447112"
                            locked: "0.08600000"
                          - asset: USDT
                            free: "1021.21000000"
                            locked: "0.00000000"
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: BNB
                            free:
                              type: string
                              example: "0.00000000"
                            locked:
                              type: string
                              example: "0.00000000"
                      permissions:
                        type: array
                        items:
                          type: string
                          example: SPOT
                      uid:
                        type: integer
                        format: int64
                        example: 354937868
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /allOrderLists:
    post:
      summary: Account order list history (USER_DATA)
      x-summary-cn: 账户订单列表历史 (USER_DATA)
      description: Query information about all your order lists, filtered by time range.
      x-description-cn: 查询所有订单列表的信息，按时间范围过滤。
      tags:
        - account
      operationId: allOrderLists
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#all-order-lists
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/allOrderLists.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/all_order_lists.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/all_order_lists.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/AllOrderListsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/AllOrderLists/AllOrderLists.go
      x-ip-weight: 20
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Database

        Notes:
        * If `startTime` and/or `endTime` are specified, `fromId` is ignored.
          Order lists are filtered by `transactionTime` of the last order list execution status update.
        * If `fromId` is specified, return order lists with order list ID >= `fromId`.
        * If no condition is specified, the most recent order lists are returned.
        * The time between `startTime` and `endTime` can't be longer than 24 hours.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        备注：

        * 如果指定了 `startTime` 和/或 `endTime`，则忽略 `fromId`。

          订单列表是按照最后一次更新的订单列表执行状态的 `transactionTime` 过滤的。

        * 如果指定了 `fromId`，返回的订单列表将是 order list ID >= `fromId`。

        * 如果不指定条件，则返回最近的订单列表。

        * `startTime`和`endTime`之间的时间不能超过 24 小时
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - allOrderLists
                  example: allOrderLists
                params:
                  type: object
                  properties:
                    fromId:
                      type: integer
                      example: 1
                      description: Order list ID to begin at
                      x-description-cn: 起始的 Order list ID
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: allOrderLists
              params:
                fromId: 1
                startTime: 1735693200000
                endTime: 1735693200000
                limit: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account order list history
          x-description-cn: 账户订单列表历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 8617b7b3-1b3d-4dec-94cd-eefd929b8ceb
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        orderListId:
                          type: integer
                          format: int64
                          example: 1274512
                        contingencyType:
                          type: string
                          example: OCO
                        listStatusType:
                          type: string
                          example: EXEC_STARTED
                        listOrderStatus:
                          type: string
                          example: EXECUTING
                        listClientOrderId:
                          type: string
                          example: 08985fedd9ea2cf6b28996
                        transactionTime:
                          type: integer
                          format: int64
                          example: 1660801713793
                        symbol:
                          type: string
                          example: BTCUSDT
                        orders:
                          type: array
                          example:
                            - symbol: BTCUSDT
                              orderId: 12569138901
                              clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                            - symbol: BTCUSDT
                              orderId: 12569138902
                              clientOrderId: jLnZpj5enfMXTuhKB1d0us
                          items:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTCUSDT
                              orderId:
                                type: integer
                                format: int64
                                example: 12569138901
                              clientOrderId:
                                type: string
                                example: BqtFCj5odMoWtSqGk2X9tU
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /allOrders:
    post:
      summary: Account order history (USER_DATA)
      x-summary-cn: 账户订单历史 (USER_DATA)
      description: Query information about all your orders – active, canceled, filled – filtered by time range.
      x-description-cn: 查询所有订单（活动、已撤销、已成交）信息，并按时间范围过滤。
      tags:
        - account
      operationId: allOrders
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#all-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/allOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/all_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/all_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/AllOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/AllOrders/AllOrders.go
      x-ip-weight: 20
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Database

        Notes:

        * If `startTime` and/or `endTime` are specified, `orderId` is ignored.

          Orders are filtered by `time` of the last execution status update.

        * If `orderId` is specified, return orders with order ID >= `orderId`.

        * If no condition is specified, the most recent orders are returned.

        * For some historical orders the `cummulativeQuoteQty` response field may be negative,
          meaning the data is not available at this time.

        * The time between `startTime` and `endTime` can't be longer than 24 hours.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        备注：

        * 如果指定了 `startTime` 和/或 `endTime`，则忽略 `orderId`。

          订单是按照最后一次更新的执行状态的`time`过滤的。

        * 如果指定了 `orderId`，返回的订单将是订单ID >= `orderId`

        * 如果不指定条件，则返回最近的订单。

        * 对于某些历史订单，`cummulativeQuoteQty` 响应字段可能为负数，代表着此时数据还不可用。

        * `startTime`和`endTime`之间的时间不能超过 24 小时。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - allOrders
                  example: allOrders
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: Order ID to begin at
                      x-description-cn: 起始订单ID
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: allOrders
              params:
                symbol: BNBUSDT
                orderId: 1
                startTime: 1735693200000
                endTime: 1735693200000
                limit: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account order history
          x-description-cn: 账户订单历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 734235c2-13d2-4574-be68-723e818c08f3
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        orderId:
                          type: integer
                          format: int64
                          example: 12569099453
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                          description: Present only for orders that belong to an order list.
                          x-description-cn: 仅当订单属于订单列表时返回。
                        clientOrderId:
                          type: string
                          example: 4d96324ff9d44481926157
                        price:
                          type: string
                          example: "23416.10000000"
                        origQty:
                          type: string
                          example: "0.00847000"
                        executedQty:
                          type: string
                          example: "0.00847000"
                        cummulativeQuoteQty:
                          type: string
                          example: "198.33521500"
                        status:
                          type: string
                          example: FILLED
                        timeInForce:
                          type: string
                          example: GTC
                        type:
                          type: string
                          example: LIMIT
                        side:
                          type: string
                          example: SELL
                        time:
                          type: integer
                          format: int64
                          example: 1660801715639
                          description: Order placement time.
                          x-description-cn: 下单时间。
                        updateTime:
                          type: integer
                          format: int64
                          example: 1660801717945
                          description: Time of the last update to the order.
                          x-description-cn: 订单最后更新时间。
                        isWorking:
                          type: boolean
                          example: true
                        workingTime:
                          type: integer
                          format: int64
                          example: 1660801715639
                        origQuoteOrderQty:
                          type: string
                          example: "0.000000"
                          description: Always present. Zero if the order type does not use `quoteOrderQty`.
                          x-description-cn: 始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。
                        selfTradePreventionMode:
                          type: string
                          example: NONE
                        preventedMatchId:
                          type: integer
                          format: int64
                          example: 0
                          description: Present only if the order expired due to STP.
                          x-description-cn: 仅当订单因 STP 过期时返回。
                        preventedQuantity:
                          type: string
                          example: "1.200000"
                          description: Present only if the order expired due to STP.
                          x-description-cn: 仅当订单因 STP 过期时返回。
                        icebergQty:
                          type: string
                          example: "0.00000000"
                          description: Appears only if the parameter icebergQty was sent in the request.
                          x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                        stopPrice:
                          type: string
                          example: "0.00000000"
                          description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                          x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                        strategyId:
                          type: integer
                          format: int64
                          example: 1
                          description: Appears only if the strategyId parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                        strategyType:
                          type: integer
                          format: int64
                          example: 1000000
                          description: Appears only if the strategyType parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                        trailingDelta:
                          type: integer
                          format: int64
                          example: 10
                          description: Delta price change required before order activation.
                          x-description-cn: 订单激活前所需的价格变动。
                        trailingTime:
                          type: integer
                          format: int64
                          example: -1
                          description: Time when the trailing order is now active and tracking price changes.
                          x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                        usedSor:
                          type: boolean
                          example: true
                          description: Field that determines whether order used SOR.
                          x-description-cn: 用于确定订单是否使用SOR的字段。
                        workingFloor:
                          type: string
                          example: SOR
                          description: Determines whether the order is being filled by the SOR or by the order book.
                          x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                        pegPriceType:
                          type: string
                          example: PRIMARY_PEG
                          description: Price peg type. Only for pegged orders.
                          x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                        pegOffsetType:
                          type: string
                          example: PRICE_LEVEL
                          description: Price peg offset type. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                        pegOffsetValue:
                          type: integer
                          format: int64
                          example: 5
                          description: Price peg offset value. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                        peggedPrice:
                          type: string
                          example: "87523.83710000"
                          description: Current price order is pegged at. Only for pegged orders, once determined.
                          x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                        expiryReason:
                          type: string
                          example: INSUFFICIENT_LIQUIDITY
                          description: Cause of the order's expiration. Appears when an order has expired.
                          x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /myAllocations:
    post:
      summary: Account allocations (USER_DATA)
      x-summary-cn: 查询分配结果 (USER_DATA)
      description: Retrieves allocations resulting from SOR order placement.
      x-description-cn: 检索由 SOR 订单生成引起的分配结果。
      tags:
        - account
      operationId: myAllocations
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-allocations
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/myAllocations.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/my_allocations.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/my_allocations.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/MyAllocationsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/MyAllocations/MyAllocations.go
      x-ip-weight: 20
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Database

        Supported parameter combinations:

        Parameters                                  | Response |
        ------------------------------------------- | -------- |
        `symbol`                                    | allocations from oldest to newest |
        `symbol` + `startTime`                      | oldest allocations since `startTime` |
        `symbol` + `endTime`                        | newest allocations until `endTime` |
        `symbol` + `startTime` + `endTime`          | allocations within the time range |
        `symbol` + `fromAllocationId`               | allocations by allocation ID |
        `symbol` + `orderId`                        | allocations related to an order starting with oldest |
        `symbol` + `orderId` + `fromAllocationId`   | allocations related to an order by allocation ID |

        **Note:** The time between `startTime` and `endTime` can't be longer than 24 hours.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        支持的参数组合:

        参数                                        | 响应      |
        ------------------------------------------- | -------- |
        `symbol`                                    | 按从最旧到最新排序的分配 |
        `symbol` + `startTime`                      | 从 `startTime` 开始的最旧的分配 |
        `symbol` + `endTime`                        | 到 `endTime` 为止的最新的分配 |
        `symbol` + `startTime` + `endTime`          | 在指定时间范围内的分配  |
        `symbol` + `fromAllocationId`               | 从指定 `AllocationId` 开始的分配  |
        `symbol` + `orderId`                        | 按从最旧到最新排序并和特定订单关联的分配 |
        `symbol` + `orderId` + `fromAllocationId`   | 从指定 `AllocationId` 开始并和特定订单关联的分配 |

        **注意:** `startTime` 和 `endTime` 之间的时间不能超过 24 小时。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - myAllocations
                  example: myAllocations
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    fromAllocationId:
                      type: integer
                      example: 1
                      description: Allocation ID to begin at
                      x-description-cn: 起始分配 ID
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: Order ID
                      x-description-cn: 订单 ID
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - apiKey
                    - timestamp
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: myAllocations
              params:
                symbol: BNBUSDT
                startTime: 1735693200000
                endTime: 1735693200000
                fromAllocationId: 1
                limit: 1
                orderId: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account allocations
          x-description-cn: 查询分配结果
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: g4ce6a53-a39d-4f71-823b-4ab5r391d6y8
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        allocationId:
                          type: integer
                          format: int64
                          example: 0
                        allocationType:
                          type: string
                          example: SOR
                        orderId:
                          type: integer
                          format: int64
                          example: 500
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                        price:
                          type: string
                          example: "1.00000000"
                        qty:
                          type: string
                          example: "0.10000000"
                        quoteQty:
                          type: string
                          example: "0.10000000"
                        commission:
                          type: string
                          example: "0.00000000"
                        commissionAsset:
                          type: string
                          example: BTC
                        time:
                          type: integer
                          format: int64
                          example: 1687319487614
                        isBuyer:
                          type: boolean
                          example: false
                        isMaker:
                          type: boolean
                          example: false
                        isAllocator:
                          type: boolean
                          example: false
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /myFilters:
    post:
      summary: Query Relevant Filters (USER_DATA)
      x-summary-cn: 查询相关过滤器 (USER_DATA)
      description: >-
        Retrieves the list of [filters](/products/spot/filters) relevant to an account on a given symbol. This is the
        only method

        that shows if an account has [`MAX_ASSET`](/products/spot/filters#max_asset) filters applied to it.
      x-description-cn: |-
        用于检索一个账户上指定交易对的 [filters](/products/spot/filters) 列表。这是唯一一个目前会显示账户是否应用了
        [`MAX_ASSET`](/products/spot/filters#max_asset) 过滤器的方法。
      tags:
        - account
      operationId: myFilters
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-filters
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/myFilters.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/my_filters.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/my_filters.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/MyFiltersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/MyFilters/MyFilters.go
      x-ip-weight: 40
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - myFilters
                  example: myFilters
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: myFilters
              params:
                symbol: BNBUSDT
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Query Relevant Filters
          x-description-cn: 查询相关过滤器
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: "1758009606869"
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    $ref: "#/components/schemas/myFiltersResponse"
  /myPreventedMatches:
    post:
      summary: Account prevented matches (USER_DATA)
      x-summary-cn: 账户的 Prevented Matches (USER_DATA)
      description: |-
        Displays the list of orders that were expired due to STP.

        These are the combinations supported:

        * `symbol` + `preventedMatchId`
        * `symbol` + `orderId`
        * `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
        * `symbol` + `orderId` + `fromPreventedMatchId` + `limit`
      x-description-cn: |-
        获取因 STP 而过期的订单列表。

        这些是支持的组合：

        * `symbol` + `preventedMatchId`
        * `symbol` + `orderId`
        * `symbol` + `orderId` + `fromPreventedMatchId` (`limit`  默认为 500)
        * `symbol` + `orderId` + `fromPreventedMatchId` + `limit`
      tags:
        - account
      operationId: myPreventedMatches
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-prevented-matches
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/myPreventedMatches.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/my_prevented_matches.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/my_prevented_matches.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/MyPreventedMatchesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/MyPreventedMatches/MyPreventedMatches.go
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        Case                            | Weight
        ----                            | -----
        If `symbol` is invalid          | 2
        Querying by `preventedMatchId`  | 2
        Querying by `orderId`           | 20
      x-weight-cn: |-
        情况                          | 权重
        ----                          | -----
        如果 `symbol` 不合法           | 2
        通过 `preventedMatchId` 查询   | 2
        通过 `orderId` 查询            | 20
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - myPreventedMatches
                  example: myPreventedMatches
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    preventedMatchId:
                      type: integer
                      format: int64
                      example: 1
                      description: Prevented match ID
                      x-description-cn: Prevented match ID
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: Order ID
                      x-description-cn: 订单 ID
                    fromPreventedMatchId:
                      type: integer
                      format: int64
                      example: 1
                      description: Prevented match ID to begin at
                      x-description-cn: 起始 prevented match ID
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: myPreventedMatches
              params:
                symbol: BNBUSDT
                preventedMatchId: 1
                orderId: 1
                fromPreventedMatchId: 1
                limit: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account prevented matches
          x-description-cn: 账户的 Prevented Matches
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: g4ce6a53-a39d-4f71-823b-4ab5r391d6y8
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        preventedMatchId:
                          type: integer
                          format: int64
                          example: 1
                        takerOrderId:
                          type: integer
                          format: int64
                          example: 5
                        makerSymbol:
                          type: string
                          example: BTCUSDT
                        makerOrderId:
                          type: integer
                          format: int64
                          example: 3
                        tradeGroupId:
                          type: integer
                          format: int64
                          example: 1
                        selfTradePreventionMode:
                          type: string
                          example: EXPIRE_MAKER
                        price:
                          type: string
                          example: "1.100000"
                        makerPreventedQuantity:
                          type: string
                          example: "1.300000"
                        transactTime:
                          type: integer
                          format: int64
                          example: 1669101687094
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /myTrades:
    post:
      summary: Account trade history (USER_DATA)
      x-summary-cn: 账户成交历史 (USER_DATA)
      description: Query information about all your trades, filtered by time range.
      x-description-cn: 获取账户指定交易对的成交历史，按时间范围过滤。
      tags:
        - account
      operationId: myTrades
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/myTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/my_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/my_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/MyTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/MyTrades/MyTrades.go
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        Condition| Weight|
        ---| ---
        |Without orderId|20|
        |With orderId|5|
      x-weight-cn: |-
        条件| 权重|
        ---| ---
        |没有 orderId|20|
        |有 orderId|5|
      x-parameters-notes: |-
        **Data Source:** Memory => Database

        Notes:
        - If `fromId` is specified, return trades with trade ID >= `fromId`.
        - If `startTime` and/or `endTime` are specified, trades are filtered by execution time (`time`).
        - `fromId` cannot be used together with `startTime` and `endTime`.
        - If `orderId` is specified, only trades related to that order are returned.
        - `startTime` and `endTime` cannot be used together with `orderId`.
        - If no condition is specified, the most recent trades are returned.
        - The time between `startTime` and `endTime` can't be longer than 24 hours.
      x-parameters-notes-cn: |-
        **数据源:** 缓存 => 数据库

        说明：
        - 指定 `fromId` 时，返回 trade ID >= `fromId` 的成交记录。
        - 指定 `startTime` 和/或 `endTime` 时，按执行时间（`time`）过滤。
        - `fromId` 不能与 `startTime`、`endTime` 同时使用。
        - 指定 `orderId` 时，仅返回该订单相关成交。
        - `startTime`、`endTime` 不能与 `orderId` 同时使用。
        - 未指定条件时，返回最近成交记录。
        - `startTime` 与 `endTime` 间隔不能超过 24 小时。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - myTrades
                  example: myTrades
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: This can only be used in combination with `symbol`.
                      x-description-cn: 必须要和参数`symbol`一起使用。
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms
                      x-description-cn: 毫秒时间戳
                    fromId:
                      type: integer
                      example: 1
                      description: First trade ID to query
                      x-description-cn: 起始交易 ID
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: myTrades
              params:
                symbol: BNBUSDT
                orderId: 1
                startTime: 1735693200000
                endTime: 1735693200000
                fromId: 1
                limit: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account trade history
          x-description-cn: 账户成交历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: f4ce6a53-a29d-4f70-823b-4ab59391d6e8
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        id: 1650422481
                        orderId: 12569099453
                        orderListId: -1
                        price: "23416.10000000"
                        qty: "0.00635000"
                        quoteQty: "148.69223500"
                        commission: "0.00000000"
                        commissionAsset: BNB
                        time: 1660801715793
                        isBuyer: false
                        isMaker: true
                        isBestMatch: true
                      - symbol: BTCUSDT
                        id: 1650422482
                        orderId: 12569099453
                        orderListId: -1
                        price: "23416.50000000"
                        qty: "0.00212000"
                        quoteQty: "49.64298000"
                        commission: "0.00000000"
                        commissionAsset: BNB
                        time: 1660801715793
                        isBuyer: false
                        isMaker: true
                        isBestMatch: true
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        id:
                          type: integer
                          format: int64
                          example: 1650422481
                        orderId:
                          type: integer
                          format: int64
                          example: 12569099453
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                        price:
                          type: string
                          example: "23416.10000000"
                        qty:
                          type: string
                          example: "0.00635000"
                        quoteQty:
                          type: string
                          example: "148.69223500"
                        commission:
                          type: string
                          example: "0.00000000"
                        commissionAsset:
                          type: string
                          example: BNB
                        time:
                          type: integer
                          format: int64
                          example: 1660801715793
                        isBuyer:
                          type: boolean
                          example: false
                        isMaker:
                          type: boolean
                          example: true
                        isBestMatch:
                          type: boolean
                          example: true
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /openOrderLists.status:
    post:
      summary: Current open Order lists (USER_DATA)
      x-summary-cn: 查询订单列表挂单 (USER_DATA)
      description: >-
        Query execution status of all open order lists.


        If you need to continuously monitor order status updates, please consider using WebSocket Streams:


        *
        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
        if on an authenticated session

        *
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
        if subscribing through signature subscription
      x-description-cn: >-
        查询所有订单列表挂单的执行状态。


        如果您需要持续监控订单状态更新，请考虑使用 WebSocket Streams：


        * 如果会话已通过验证，请使用
        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)

        * 如果通过签名订阅的方式订阅，请使用
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
      tags:
        - account
      operationId: openOrderListsStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#open-order-lists-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/openOrderListsStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/open_order_lists_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/open_order_lists_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/OpenOrderListsStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/OpenOrderListsStatus/OpenOrderListsStatus.go
      x-ip-weight: 6
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory -> Database"
      x-parameters-notes-cn: "**数据源:** 缓存 => 数据库"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - openOrderLists.status
                  example: openOrderLists.status
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: openOrderLists.status
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Current open Order lists
          x-description-cn: 查询订单列表挂单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 3a4437e2-41a3-4c19-897c-9cadc5dce8b6
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        orderListId:
                          type: integer
                          format: int64
                          example: 0
                        contingencyType:
                          type: string
                          example: OCO
                        listStatusType:
                          type: string
                          example: EXEC_STARTED
                        listOrderStatus:
                          type: string
                          example: EXECUTING
                        listClientOrderId:
                          type: string
                          example: 08985fedd9ea2cf6b28996
                        transactionTime:
                          type: integer
                          format: int64
                          example: 1660801713793
                        symbol:
                          type: string
                          example: BTCUSDT
                        orders:
                          type: array
                          example:
                            - symbol: BTCUSDT
                              orderId: 4
                              clientOrderId: CUhLgTXnX5n2c0gWiLpV4d
                            - symbol: BTCUSDT
                              orderId: 5
                              clientOrderId: 1ZqG7bBuYwaF4SU8CwnwHm
                          items:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTCUSDT
                              orderId:
                                type: integer
                                format: int64
                                example: 4
                              clientOrderId:
                                type: string
                                example: CUhLgTXnX5n2c0gWiLpV4d
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 6
  /openOrders.status:
    post:
      summary: Current open orders (USER_DATA)
      x-summary-cn: 当前挂单 (USER_DATA)
      description: >-
        Query execution status of all open orders.


        If you need to continuously monitor order status updates, please consider using WebSocket Streams:


        *
        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
        if on an authenticated session

        *
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
        if subscribing through signature subscription
      x-description-cn: >-
        查询所有挂订单的执行状态。


        如果您需要持续监控订单状态更新，请考虑使用 WebSocket Streams：


        * 如果会话已通过验证，请使用
        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)

        * 如果通过签名订阅的方式订阅，请使用
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
      tags:
        - account
      operationId: openOrdersStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#open-orders-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/openOrdersStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/open_orders_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/open_orders_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/OpenOrdersStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/OpenOrdersStatus/OpenOrdersStatus.go
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        | Parameter | Weight |
        | --------- | ------ |
        | `symbol`  |      6 |
        | none      |     80 |
      x-weight-cn: |-
        | 参数 | 权重 |
        | --------- | ------ |
        | `symbol`  |      6 |
        | 不提供    |     80 |
      x-parameters-notes: "**Data Source:** Memory => Database"
      x-parameters-notes-cn: "**数据源:** 缓存 => 数据库"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - openOrders.status
                  example: openOrders.status
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                      description: If omitted, open orders for all symbols are returned
                      x-description-cn: 如果省略，则返回所有交易对的挂单
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: openOrders.status
              params:
                symbol: BNBUSDT
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Current open orders
          x-description-cn: 当前挂单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 55f07876-4f6f-4c47-87dc-43e5fff3f2e7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        orderId:
                          type: integer
                          format: int64
                          example: 12569099453
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                          description: Present only for orders that belong to an order list.
                          x-description-cn: 仅当订单属于订单列表时返回。
                        clientOrderId:
                          type: string
                          example: 4d96324ff9d44481926157
                        price:
                          type: string
                          example: "23416.10000000"
                        origQty:
                          type: string
                          example: "0.00847000"
                        executedQty:
                          type: string
                          example: "0.00720000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.000000"
                          description: Always present. Zero if the order type does not use `quoteOrderQty`.
                          x-description-cn: 始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。
                        cummulativeQuoteQty:
                          type: string
                          example: "172.43931000"
                        status:
                          type: string
                          example: PARTIALLY_FILLED
                        timeInForce:
                          type: string
                          example: GTC
                        type:
                          type: string
                          example: LIMIT
                        side:
                          type: string
                          example: SELL
                        time:
                          type: integer
                          format: int64
                          example: 1660801715639
                          description: Order placement time.
                          x-description-cn: 下单时间。
                        updateTime:
                          type: integer
                          format: int64
                          example: 1660801717945
                          description: Time of the last update to the order.
                          x-description-cn: 订单最后更新时间。
                        isWorking:
                          type: boolean
                          example: true
                        workingTime:
                          type: integer
                          format: int64
                          example: 1660801715639
                        selfTradePreventionMode:
                          type: string
                          example: NONE
                        icebergQty:
                          type: string
                          example: "0.00000000"
                          description: Appears only if the parameter icebergQty was sent in the request.
                          x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                        preventedMatchId:
                          type: integer
                          format: int64
                          example: 0
                          description: Appears only if the order expired due to STP.
                          x-description-cn: 仅在因 STP 导致订单失效时出现。
                        preventedQuantity:
                          type: string
                          example: "1.200000"
                          description: Order quantity that expired due to STP.
                          x-description-cn: 因 STP 导致订单失效的数量。
                        stopPrice:
                          type: string
                          example: "0.00000000"
                          description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                          x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                        strategyId:
                          type: integer
                          format: int64
                          example: 1
                          description: Appears only if the strategyId parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                        strategyType:
                          type: integer
                          format: int64
                          example: 1000000
                          description: Appears only if the strategyType parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                        trailingDelta:
                          type: integer
                          format: int64
                          example: 10
                          description: Delta price change required before order activation.
                          x-description-cn: 订单激活前所需的价格变动。
                        trailingTime:
                          type: integer
                          format: int64
                          example: -1
                          description: Time when the trailing order is now active and tracking price changes.
                          x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                        usedSor:
                          type: boolean
                          example: true
                          description: Field that determines whether order used SOR.
                          x-description-cn: 用于确定订单是否使用SOR的字段。
                        workingFloor:
                          type: string
                          example: SOR
                          description: Determines whether the order is being filled by the SOR or by the order book.
                          x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                        pegPriceType:
                          type: string
                          example: PRIMARY_PEG
                          description: Price peg type. Only for pegged orders.
                          x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                        pegOffsetType:
                          type: string
                          example: PRICE_LEVEL
                          description: Price peg offset type. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                        pegOffsetValue:
                          type: integer
                          format: int64
                          example: 5
                          description: Price peg offset value. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                        peggedPrice:
                          type: string
                          example: "87523.83710000"
                          description: Current price order is pegged at. Only for pegged orders, once determined.
                          x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                        expiryReason:
                          type: string
                          example: INSUFFICIENT_LIQUIDITY
                          description: Cause of the order's expiration. Appears when an order has expired.
                          x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 6
  /order.amendments:
    post:
      summary: Query Order Amendments (USER_DATA)
      x-summary-cn: 查询改单 (USER_DATA)
      description: Queries all amendments of a single order.
      x-description-cn: 查询对一个订单的所有改单操作。
      tags:
        - account
      operationId: orderAmendments
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#order-amendments
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/orderAmendments.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/order_amendments.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/order_amendments.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/OrderAmendmentsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/OrderAmendments/OrderAmendments.go
      x-ip-weight: 4
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.amendments
                  example: order.amendments
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: Order ID
                      x-description-cn: 订单 ID
                    fromExecutionId:
                      type: integer
                      format: int64
                      example: 1
                      description: Execution ID to begin at
                      x-description-cn: 起始执行 ID
                    limit:
                      type: integer
                      format: int64
                      example: 1
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认值: 500; 最大值: 1000"
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - orderId
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.amendments
              params:
                symbol: BNBUSDT
                orderId: 1
                fromExecutionId: 1
                limit: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Query Order Amendments
          x-description-cn: 查询改单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 6f5ebe91-01d9-43ac-be99-57cf062e0e30
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        orderId:
                          type: integer
                          format: int64
                          example: 23
                        executionId:
                          type: integer
                          format: int64
                          example: 60
                        origClientOrderId:
                          type: string
                          example: my_pending_order
                        newClientOrderId:
                          type: string
                          example: xbxXh5SSwaHS7oUEOCI88B
                        origQty:
                          type: string
                          example: "7.00000000"
                        newQty:
                          type: string
                          example: "5.00000000"
                        time:
                          type: integer
                          format: int64
                          example: 1741924229819
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 4
  /orderList.status:
    post:
      summary: Query Order list (USER_DATA)
      x-summary-cn: 查询订单列表 (USER_DATA)
      description: |-
        Check execution status of an Order list.

        For execution status of individual orders, use `order.status`.
      x-description-cn: |-
        检查订单列表的执行状态。

        对于单个订单的执行状态，使用 `order.status`。
      tags:
        - account
      operationId: orderListStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#order-list-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/orderListStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/order_list_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/order_list_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/OrderListStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/OrderListStatus/OrderListStatus.go
      x-ip-weight: 4
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Database

        Notes:

        * `origClientOrderId` refers to `listClientOrderId` of the order list itself.

        * If both `origClientOrderId` and `orderListId` parameters are specified,
          only `origClientOrderId` is used and `orderListId` is ignored.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        备注：

        * `origClientOrderId` 指的是订单列表本身的 `listClientOrderId`。

        * 如果同时指定了 `origClientOrderId` 和 `orderListId` 参数，仅使用 `origClientOrderId` 并忽略 `orderListId`。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.status
                  example: orderList.status
                params:
                  type: object
                  properties:
                    origClientOrderId:
                      type: string
                      example: 08985fedd9ea2cf6b28996
                      description: Query order list by `listClientOrderId`. `orderListId` or `origClientOrderId` must be provided.
                      x-description-cn: 通过 `listClientOrderId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。
                    orderListId:
                      type: integer
                      example: 1
                      description: Query order list by `orderListId`. `orderListId` or `origClientOrderId` must be provided.
                      x-description-cn: 通过 `orderListId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.status
              params:
                origClientOrderId: 08985fedd9ea2cf6b28996
                orderListId: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Query Order list
          x-description-cn: 查询订单列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: b53fd5ff-82c7-4a04-bd64-5f9dc42c2100
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 1274512
                      contingencyType:
                        type: string
                        example: OCO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: 08985fedd9ea2cf6b28996
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1660801713793
                      symbol:
                        type: string
                        example: BTCUSDT
                      orders:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 12569138901
                            clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                          - symbol: BTCUSDT
                            orderId: 12569138902
                            clientOrderId: jLnZpj5enfMXTuhKB1d0us
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 12569138901
                            clientOrderId:
                              type: string
                              example: BqtFCj5odMoWtSqGk2X9tU
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 4
  /order.status:
    post:
      summary: Query order (USER_DATA)
      x-summary-cn: 查询订单 (USER_DATA)
      description: Check execution status of an order.
      x-description-cn: 查询订单状态。
      tags:
        - account
      operationId: orderStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#order-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AccountApi/orderStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/account_api/order_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Account/order_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/account/OrderStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AccountAPI/OrderStatus/OrderStatus.go
      x-ip-weight: 4
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Memory => Database


        Notes:


        * If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the
        `origClientOrderId` from that result is checked against that order. If both conditions are not met the request
        will be rejected.


        * For some historical orders the `cummulativeQuoteQty` response field may be negative,
          meaning the data is not available at this time.
      x-parameters-notes-cn: >-
        **数据源:** 缓存 => 数据库


        备注：


        * 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId`
        的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。


        * 对于某些历史订单，`cummulativeQuoteQty` 响应字段可能为负数，意味着此时数据不可用。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.status
                  example: order.status
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: Lookup order by `orderId`
                      x-description-cn: 按 `orderId` 查找订单
                    origClientOrderId:
                      type: string
                      example: myOrder1
                      description: Lookup order by `clientOrderId`
                      x-description-cn: 按 `clientOrderId` 查找订单
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.status
              params:
                symbol: BNBUSDT
                orderId: 1
                origClientOrderId: myOrder1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Query order
          x-description-cn: 查询订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: aa62318a-5a97-4f3b-bdc7-640bbe33b291
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      orderId:
                        type: integer
                        format: int64
                        example: 12569099453
                      orderListId:
                        type: integer
                        format: int64
                        example: -1
                        description: Present only for orders that belong to an order list.
                        x-description-cn: 仅当订单属于订单列表时返回。
                      clientOrderId:
                        type: string
                        example: 4d96324ff9d44481926157
                      price:
                        type: string
                        example: "23416.10000000"
                      origQty:
                        type: string
                        example: "0.00847000"
                      executedQty:
                        type: string
                        example: "0.00847000"
                      origQuoteOrderQty:
                        type: string
                        example: "0.000000"
                        description: Always present. Zero if the order type does not use `quoteOrderQty`.
                        x-description-cn: 始终返回；若订单类型不使用 `quoteOrderQty` 则为 0。
                      cummulativeQuoteQty:
                        type: string
                        example: "198.33521500"
                      status:
                        type: string
                        example: FILLED
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: LIMIT
                      side:
                        type: string
                        example: SELL
                      stopPrice:
                        type: string
                        example: "0.00000000"
                        description: Always present. Zero if the order type does not use `stopPrice`.
                        x-description-cn: 始终返回；若订单类型不使用 `stopPrice` 则为 0。
                      trailingDelta:
                        type: integer
                        format: int64
                        example: 10
                        description: Present only if `trailingDelta` was set on the order.
                        x-description-cn: 仅当订单设置了 `trailingDelta` 时返回。
                      trailingTime:
                        type: integer
                        format: int64
                        example: -1
                        description: Present only if `trailingDelta` was set on the order.
                        x-description-cn: 仅当订单设置了 `trailingDelta` 时返回。
                      icebergQty:
                        type: string
                        example: "0.00000000"
                        description: Always present. Zero for non-iceberg orders.
                        x-description-cn: 始终返回；非冰山订单为 0。
                      time:
                        type: integer
                        format: int64
                        example: 1660801715639
                        description: Order placement time.
                        x-description-cn: 下单时间。
                      updateTime:
                        type: integer
                        format: int64
                        example: 1660801717945
                        description: Time of the last update to the order.
                        x-description-cn: 订单最后更新时间。
                      isWorking:
                        type: boolean
                        example: true
                      workingTime:
                        type: integer
                        format: int64
                        example: 1660801715639
                      strategyId:
                        type: integer
                        format: int64
                        example: 37463720
                        description: Present only if `strategyId` was set on the order.
                        x-description-cn: 仅当订单设置了 `strategyId` 时返回。
                      strategyType:
                        type: integer
                        format: int64
                        example: 1000000
                        description: Present only if `strategyType` was set on the order.
                        x-description-cn: 仅当订单设置了 `strategyType` 时返回。
                      selfTradePreventionMode:
                        type: string
                        example: NONE
                      preventedMatchId:
                        type: integer
                        format: int64
                        example: 0
                        description: Present only if the order expired due to STP.
                        x-description-cn: 仅当订单因 STP 过期时返回。
                      preventedQuantity:
                        type: string
                        example: "1.200000"
                        description: Present only if the order expired due to STP.
                        x-description-cn: 仅当订单因 STP 过期时返回。
                      usedSor:
                        type: boolean
                        example: true
                        description: Field that determines whether order used SOR.
                        x-description-cn: 用于确定订单是否使用SOR的字段。
                      workingFloor:
                        type: string
                        example: SOR
                        description: Determines whether the order is being filled by the SOR or by the order book.
                        x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                      pegPriceType:
                        type: string
                        example: PRIMARY_PEG
                        description: Price peg type. Only for pegged orders.
                        x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                      pegOffsetType:
                        type: string
                        example: PRICE_LEVEL
                        description: Price peg offset type. Only for pegged orders, if requested.
                        x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                      pegOffsetValue:
                        type: integer
                        format: int64
                        example: 5
                        description: Price peg offset value. Only for pegged orders, if requested.
                        x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                      peggedPrice:
                        type: string
                        example: "87523.83710000"
                        description: Current price order is pegged at. Only for pegged orders, once determined.
                        x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                      expiryReason:
                        type: string
                        example: INSUFFICIENT_LIQUIDITY
                        description: Cause of the order's expiration. Appears when an order has expired.
                        x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 4
  /session.logon:
    post:
      summary: Log in with API key (USER_DATA)
      x-summary-cn: 用API key登录 (USER_DATA)
      description: >-
        Authenticate WebSocket connection using the provided API key.


        After calling `session.logon`, you can omit `apiKey` and `signature` parameters for future requests that require
        them.


        Note that only one API key can be authenticated.


        Calling `session.logon` multiple times changes the current authenticated API key.


        **Note:** Only Ed25519 keys are supported for this feature.
      x-description-cn: |-
        使用提供的API密钥进行WebSocket连接身份验证。

        在调用`session.logon`后，将来的需要`apiKey`和`signature`参数的请求可以省略它们。

        请注意，只能认证一个API密钥。
        多次调用`session.logon`将更改当前已认证的API密钥。

        **注意：** 仅支持 Ed25519 密钥用于此功能。
      tags:
        - auth
      operationId: sessionLogon
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AuthApi/sessionLogon.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/auth_api/session_logon.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Auth/session_logon.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/auth/SessionLogonExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AuthAPI/SessionLogon/SessionLogon.go
      x-ip-weight: 2
      x-legacy-anchors:
        - log-in-with-api-key-signed
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - session.logon
                  example: session.logon
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        The value cannot be greater than `60000`. Supports up to three decimal places of precision
                        (e.g., 6000.346) so that microseconds may be specified.
                      x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: session.logon
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Log in with API key
          x-description-cn: 用API key登录
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: c174a2b1-3f51-4580-b200-8528bd237cb7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      apiKey:
                        type: string
                        example: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
                      authorizedSince:
                        type: integer
                        format: int64
                        example: 1649729878532
                      connectedSince:
                        type: integer
                        format: int64
                        example: 1649729873021
                      returnRateLimits:
                        type: boolean
                        example: false
                      serverTime:
                        type: integer
                        format: int64
                        example: 1649729878630
                      userDataStream:
                        type: boolean
                        example: false
                        description: Is User Data Stream subscription active?
                        x-description-cn: User Data Stream 订阅是否有效？
  /session.logout:
    post:
      summary: Log out of the session
      x-summary-cn: 退出会话
      description: >-
        Forget the API key previously authenticated. If the connection is not authenticated, this request does nothing.


        Note that the WebSocket connection stays open after `session.logout` request. You can continue using the
        connection, but now you will have to explicitly provide the `apiKey` and `signature` parameters where needed.
      x-description-cn: |-
        忘记之前认证的API密钥。
        如果连接未经身份验证，此请求不会有任何作用。

        请注意，`session.logout`请求后，WebSocket连接仍然保持打开状态。
        你可以继续使用连接，但现在必须在需要的地方明确提供`apiKey`和`signature`参数。
      tags:
        - auth
      operationId: sessionLogout
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AuthApi/sessionLogout.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/auth_api/session_logout.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Auth/session_logout.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/auth/SessionLogoutExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AuthAPI/SessionLogout/SessionLogout.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - session.logout
                  example: session.logout
                params:
                  type: object
                  properties: {}
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: session.logout
      responses:
        Successful Response:
          description: Log out of the session
          x-description-cn: 退出会话
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: c174a2b1-3f51-4580-b200-8528bd237cb7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      apiKey:
                        type: string
                        example: null
                      authorizedSince:
                        type: integer
                        format: int64
                        example: null
                      connectedSince:
                        type: integer
                        format: int64
                        example: 1649729873021
                      returnRateLimits:
                        type: boolean
                        example: false
                      serverTime:
                        type: integer
                        format: int64
                        example: 1649730611671
                      userDataStream:
                        type: boolean
                        example: false
                        description: Is User Data Stream subscription active?
                        x-description-cn: User Data Stream 订阅是否有效？
  /session.status:
    post:
      summary: Query session status
      x-summary-cn: 查询会话状态
      description: |-
        Query the status of the WebSocket connection,
        inspecting which API key (if any) is used to authorize requests.
      x-description-cn: 查询WebSocket连接的状态，检查用于授权请求的API密钥（如果有的话）。
      tags:
        - auth
      operationId: sessionStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/AuthApi/sessionStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/auth_api/session_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Auth/session_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/auth/SessionStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/AuthAPI/SessionStatus/SessionStatus.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - session.status
                  example: session.status
                params:
                  type: object
                  properties: {}
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: session.status
      responses:
        Successful Response:
          description: Query session status
          x-description-cn: 查询会话状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: b50c16cd-62c9-4e29-89e4-37f10111f5bf
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      apiKey:
                        type: string
                        example: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
                        description: "`null` if the connection is not authenticated."
                        x-description-cn: 如果连接未经过身份验证，则为 `null`。
                      authorizedSince:
                        type: integer
                        format: int64
                        example: 1649729878532
                        description: "`null` if the connection is not authenticated."
                        x-description-cn: 如果连接未经过身份验证，则为 `null`。
                      connectedSince:
                        type: integer
                        format: int64
                        example: 1649729873021
                      returnRateLimits:
                        type: boolean
                        example: false
                      serverTime:
                        type: integer
                        format: int64
                        example: 1649730611671
                      userDataStream:
                        type: boolean
                        example: true
                        description: Is User Data Stream subscription active?
                        x-description-cn: User Data Stream 订阅是否有效？
  /exchangeInfo:
    post:
      summary: Exchange information
      x-summary-cn: 交易规范信息
      description: |-
        Query current exchange trading rules, rate limits, and symbol
        information.
      x-description-cn: 获取交易规则，速率限制，和交易对信息。
      tags:
        - general
      operationId: exchangeInfo
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/GeneralApi/exchangeInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/general_api/exchange_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/General/exchange_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/general/ExchangeInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/GeneralAPI/ExchangeInfo/ExchangeInfo.go
      x-ip-weight: 20
      x-security-type: NONE
      x-parameters-notes: >-
        **Data Source:** Memory


        **Notes:**

        * If the value provided to `symbol` or `symbols` do not exist, the endpoint will throw an error saying the
        symbol is invalid.

        * All parameters are optional.

        * Only one of `symbol`, `symbols`, `permissions` parameters can be specified.

        * Without parameters, `exchangeInfo` displays all symbols with `["SPOT", "MARGIN", "LEVERAGED"]` permissions.
          * In order to list *all* active symbols on the exchange, you need to explicitly request all permissions.
        * `permissions` accepts either a list of permissions, or a single permission name. E.g. `"SPOT"`.


        ::span{#examples-of-symbol-permissions-interpretation-from-the-response}


        **Examples of Symbol Permissions Interpretation from the Response:**


        * `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".

        * `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".

        * `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or
        permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B"
        and permission "C".)
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        **备注:**
        * 如果参数 `symbol` 或者 `symbols` 提供的交易对不存在, 系统会返回错误并提示交易对不正确。
        * 所有的参数都是可选的。
        * `symbol`、`symbols`、`permissions` 参数只能指定其中一个。
        * 不带参数时, `exchangeInfo` 显示所有具有 `["SPOT", "MARGIN", "LEVERAGED"]` 权限的交易对。
          * 要列出交易所上所有活跃的交易对, 您需要在 `permissions` 中明确指定它们。
        * `permissions` 可以支持单个或多个值（例如 `"SPOT"`, `["MARGIN","LEVERAGED"]`）。

        ::span{#examples-of-symbol-permissions-interpretation-from-the-response}

        **解释响应中的 `permissionSets`：**

        * `[["A","B"]]` 有权限"A"**或**权限"B"的账户可以下订单。
        * `[["A"],["B"]]` 有权限"A"**和**权限"B"的账户可以下订单。
        * `[["A"],["B","C"]]` 有权限"A"**和**权限"B"或权限"C"的账户可以下订单。（此处应用的是包含或，而不是排除或，因此账户可以同时拥有权限"B"和权限"C"。）
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - exchangeInfo
                  example: exchangeInfo
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                      description: Describe a single symbol
                      x-description-cn: 描述单个交易对
                    symbols:
                      type: array
                      items:
                        type: string
                        example: BTCUSDT
                      description: Describe multiple symbols
                      x-description-cn: 描述多个交易对
                    permissions:
                      type: array
                      items:
                        type: string
                        example: SPOT
                      description: Filter symbols by permissions
                      x-description-cn: 按权限过滤交易对
                    showPermissionSets:
                      type: boolean
                      example: true
                      default: true
                      description: >-
                        Controls whether the content of the `permissionSets` field is populated or not. Defaults to
                        `true`.
                      x-description-cn: 控制 `permissionSets` 字段的内容是否填充。默认为 `true`。
                    symbolStatus:
                      type: string
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                      description: >-
                        Filters for symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`. Cannot be used in combination with `symbol` or `symbols`.
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。有效值：`TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`。不能与 `symbol` 或
                        `symbols` 组合使用。
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: exchangeInfo
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                permissions:
                  - SPOT
                showPermissionSets: true
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Exchange information
          x-description-cn: 交易规范信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 5494febb-d167-46a2-996d-70533eb4d976
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    $ref: "#/components/schemas/exchangeInfoResponse"
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 20
  /executionRules:
    post:
      summary: Query Execution Rules
      x-summary-cn: 查询执行规则
      description: Query execution rules for symbols.
      x-description-cn: 查询交易对的执行规则。
      tags:
        - general
      operationId: executionRules
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#execution-rules
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/GeneralApi/executionRules.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/general_api/execution_rules.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/General/execution_rules.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/general/ExecutionRulesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/GeneralAPI/ExecutionRules/ExecutionRules.go
      x-security-type: NONE
      x-weight: |-
        Parameter | Weight
        --- | ---
        `symbol` | 2
        `symbols` | 2 for each `symbol`, capped at a max of 40
        `symbolStatus` | 40
        None | 40
      x-weight-cn: |-
        参数 | 权重
        --- | ---
        `symbol` | 2
        `symbols` | 每个 `symbol` 占用 2，最多为 40
        `symbolStatus` | 40
        无 | 40
      x-parameters-notes: |-
        **Data Source:** Memory

        **Note:** No combination of multiple parameters is allowed.
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        **注意:** 不允许多个参数组合使用。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - executionRules
                  example: executionRules
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BAZUSD
                      description: Query for specified symbol.
                      x-description-cn: 查询指定的交易对。
                    symbols:
                      type: array
                      items:
                        type: string
                        example: BAZUSD
                      description: Query for multiple symbols.
                      x-description-cn: 查询多个交易对。
                    symbolStatus:
                      type: string
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                      description: >-
                        Query for all symbols with the specified status. Supported values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: 查询指定状态的所有交易对。支持的值：`TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: executionRules
              params:
                symbol: BAZUSD
                symbols:
                  - BAZUSD
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Query Execution Rules
          x-description-cn: 查询执行规则
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 5162affb-0aba-4821-b475-f2625006eb43
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      symbolRules:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BAZUSD
                            rules:
                              type: array
                              items:
                                type: object
                                properties:
                                  ruleType:
                                    type: string
                                    example: PRICE_RANGE
                                  bidLimitMultUp:
                                    type: string
                                    example: "1.0001"
                                  bidLimitMultDown:
                                    type: string
                                    example: "0.9999"
                                  askLimitMultUp:
                                    type: string
                                    example: "1.0001"
                                  askLimitMultDown:
                                    type: string
                                    example: "0.9999"
  /ping:
    post:
      summary: Test connectivity
      x-summary-cn: 测试连通性
      description: >-
        Test connectivity to the WebSocket API.


        Note: You can use regular WebSocket ping frames to test connectivity as well, WebSocket API will respond with
        pong frames as soon as possible. ping request along with time is a safe way to test request-response handling in
        your application.
      x-description-cn: |-
        测试能否联通 WebSocket API。

        **注意:**

        您也可以使用常规 WebSocket ping 帧来测试连通性，
        WebSocket API 将尽快以 pong 帧响应。
        `ping` 请求和 `time` 是在应用程序中测试请求-响应处理的安全方法。
      tags:
        - general
      operationId: ping
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#ping
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/GeneralApi/ping.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/general_api/ping.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/General/ping.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/general/PingExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/GeneralAPI/Ping/Ping.go
      x-ip-weight: 1
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ping
                  example: ping
                params:
                  type: object
                  properties: {}
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ping
      responses:
        Successful Response:
          description: Test connectivity
          x-description-cn: 测试连通性
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 922bcc6e-9de8-440d-9e84-7c80933a8d0d
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /time:
    post:
      summary: Check server time
      x-summary-cn: 检查服务器时间
      description: Test connectivity to the WebSocket API and get the current server time.
      x-description-cn: 测试与 WebSocket API 的连通性并获取当前服务器时间。
      tags:
        - general
      operationId: time
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#time
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/GeneralApi/time.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/general_api/time.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/General/time.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/general/TimeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/GeneralAPI/Time/Time.go
      x-ip-weight: 1
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - time
                  example: time
                params:
                  type: object
                  properties: {}
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: time
      responses:
        Successful Response:
          description: Check server time
          x-description-cn: 检查服务器时间
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 187d3cb2-942d-484c-8271-4e2141bbadb1
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      serverTime:
                        type: integer
                        format: int64
                        example: 1656400526260
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /avgPrice:
    post:
      summary: Current average price
      x-summary-cn: 当前平均价格
      description: Get current average price for a symbol.
      x-description-cn: 获取交易对的当前平均价格
      tags:
        - market
      operationId: avgPrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#avg-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/avgPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/avg_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/avg_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/AvgPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/AvgPrice/AvgPrice.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - avgPrice
                  example: avgPrice
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: avgPrice
              params:
                symbol: BNBUSDT
      responses:
        Successful Response:
          description: Current average price
          x-description-cn: 当前平均价格
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: ddbfb65f-9ebf-42ec-8240-8f0f91de0867
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      mins:
                        type: integer
                        format: int64
                        example: 5
                        description: Average price interval (in minutes)
                        x-description-cn: 平均价格间隔（以分钟为单位）
                      price:
                        type: string
                        example: "0.01378135"
                        description: Average price
                        x-description-cn: 平均价格
                      closeTime:
                        type: integer
                        format: int64
                        example: 1694061154503
                        description: Last trade time
                        x-description-cn: 最近成交时间
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 2
  /depth:
    post:
      summary: Order book
      x-summary-cn: 订单簿深度信息
      description: >-
        Get current order book.


        Note that this request returns limited market depth.


        If you need to continuously monitor order book updates, please consider using WebSocket Streams:
          * `<symbol>@depth<levels>`
          * `<symbol>@depth`

        You can use `depth` request together with `<symbol>@depth` streams to [maintain a local order
        book](/products/spot/web-socket-streams#how-to-manage-a-local-order-book-correctly).
      x-description-cn: >-
        获取当前深度信息。


        请注意，此请求返回有限的市场深度。


        如果需要持续监控深度信息更新，请考虑使用 WebSocket Streams：
          * `<symbol>@depth<levels>`
          * `<symbol>@depth`

        如果需要[维护本地orderbook](/products/spot/web-socket-streams#how-to-maintain-orderbook)，您可以将 `depth` 请求与
        `<symbol>@depth` streams 一起使用。
      tags:
        - market
      operationId: depth
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#depth
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/depth.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/depth.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/depth.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/DepthExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/Depth/Depth.go
      x-security-type: NONE
      x-weight: |-
        Adjusted based on the limit:

        |Limit|Request Weight
        ------|-------
        1-100|  5
        101-500| 25
        501-1000| 50
        1001-5000| 250
      x-weight-cn: |-
        根据 limit 调整：

        |限制|请求权重
        ------|-------
        1-100|  5
        101-500| 25
        501-1000| 50
        1001-5000| 250
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - depth
                  example: depth
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    limit:
                      type: integer
                      example: 1
                      default: 100
                      maximum: 5000
                    symbolStatus:
                      type: string
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                      description: |-
                        Filters for symbols that have this `tradingStatus`.
                        A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
                      x-description-cn: |-
                        过滤具有此 `tradingStatus` 的交易对。
                        如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: depth
              params:
                symbol: BNBUSDT
                limit: 1
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Order book
          x-description-cn: 订单簿深度信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 51e2affb-0aba-4821-ba75-f2625006eb43
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      lastUpdateId:
                        type: integer
                        format: int64
                        example: 2731179239
                      bids:
                        type: array
                        description: Bid orders. Each entry is [price, quantity].
                        x-description-cn: 买单列表。每项为 [价格, 数量]
                        example:
                          - - "0.01379900"
                            - "3.43200000"
                          - - "0.01379800"
                            - "3.24300000"
                          - - "0.01379700"
                            - "10.45500000"
                          - - "0.01379600"
                            - "3.82100000"
                          - - "0.01379500"
                            - "10.26200000"
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price
                              x-description-cn: 价位
                              example: "0.01379900"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "3.43200000"
                          items:
                            oneOf:
                              - type: string
                                description: Price
                                x-description-cn: 价位
                                example: "0.01379900"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "3.43200000"
                      asks:
                        type: array
                        description: Ask orders. Each entry is [price, quantity].
                        x-description-cn: 卖单列表。每项为 [价格, 数量]
                        example:
                          - - "0.01380000"
                            - "5.91700000"
                          - - "0.01380100"
                            - "6.01400000"
                          - - "0.01380200"
                            - "0.26800000"
                          - - "0.01380300"
                            - "0.33800000"
                          - - "0.01380400"
                            - "0.26800000"
                        items:
                          type: array
                          minItems: 2
                          maxItems: 2
                          x-prefixItems:
                            - type: string
                              description: Price
                              x-description-cn: 价位
                              example: "0.01380000"
                            - type: string
                              description: Quantity
                              x-description-cn: 挂单量
                              example: "5.91700000"
                          items:
                            oneOf:
                              - type: string
                                description: Price
                                x-description-cn: 价位
                                example: "0.01380000"
                              - type: string
                                description: Quantity
                                x-description-cn: 挂单量
                                example: "5.91700000"
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 2
  /klines:
    post:
      summary: Klines
      x-summary-cn: K线数据
      description: >-
        Get klines (candlestick bars).


        Klines are uniquely identified by their open & close time.


        If you need access to real-time kline updates, please consider using WebSocket Streams:
          * `<symbol>@kline_<interval>`

        If you need historical kline data, please consider using
        [data.binance.vision](https://github.com/binance/binance-public-data/#klines).
      x-description-cn: |-
        获取K线数据。

        Klines 由其开盘时间和收盘时间为唯一标识。

        如果您需要访问实时 kline 更新，请考虑使用 WebSocket Streams：
          * `<symbol>@kline_<interval>`

        如果需要历史K线数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/#klines)。
      tags:
        - market
      operationId: klines
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#klines
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/klines.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/klines.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/klines.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/KlinesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/Klines/Klines.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: |-
        **Data Source:** Database

        ::span{#kline-intervals}

        Supported kline intervals (case-sensitive):

        Interval  | `interval` value
        --------- | ----------------
        seconds   | `1s`
        minutes   | `1m`, `3m`, `5m`, `15m`, `30m`
        hours     | `1h`, `2h`, `4h`, `6h`, `8h`, `12h`
        days      | `1d`, `3d`
        weeks     | `1w`
        months    | `1M`

        **Notes:**

        * If `startTime` and `endTime` are not sent, the most recent klines are returned.
        * Supported values for `timeZone`:
          * Hours and minutes (e.g. `-1:00`, `05:45`)
          * Only hours (e.g. `0`, `8`, `4`)
          * Accepted range is strictly [-12:00 to +14:00] inclusive
        * If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
        * Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        ::span{#kline-intervals}

        支持的K线间隔 （区分大小写）：

        间隔  | `间隔` 值
        --------- | ----------------
        seconds -> 秒   | `1s`
        minutes -> 分钟 | `1m`， `3m`， `5m`， `15m`， `30m`
        hours -> 小时   | `1h`， `2h`， `4h`， `6h`， `8h`， `12h`
        days -> 天      | `1d`， `3d`
        weeks -> 周    | `1w`
        months -> 月  | `1M`

        **请注意：**

        * 如果未发送`startTime`和`endTime`，将返回最近的K线数据。
        * `timeZone`支持的值包括：
            * 小时和分钟（例如 `-1:00`，`05:45`）
            * 仅小时（例如 `0`，`8`，`4`）
            * 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
        * 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
        * 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - klines
                  example: klines
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    interval:
                      type: string
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
                      example: 1s
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                    timeZone:
                      type: string
                      example: "0"
                      description: "Default: 0 (UTC)"
                      x-description-cn: 默认值： 0 (UTC)
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                  additionalProperties: false
                  required:
                    - symbol
                    - interval
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: klines
              params:
                symbol: BNBUSDT
                interval: 1s
                startTime: 1735693200000
                endTime: 1735693200000
                timeZone: "0"
                limit: 1
      responses:
        Successful Response:
          description: Klines
          x-description-cn: K线数据
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: array
                      minItems: 12
                      maxItems: 12
                      x-prefixItems:
                        - type: integer
                          format: int64
                          description: Open time
                          x-description-cn: 开盘时间
                          example: 1499040000000
                        - type: string
                          description: Open
                          x-description-cn: 开盘价
                          example: "0.01634790"
                        - type: string
                          description: High
                          x-description-cn: 最高价
                          example: "0.80000000"
                        - type: string
                          description: Low
                          x-description-cn: 最低价
                          example: "0.01575800"
                        - type: string
                          description: Close
                          x-description-cn: 收盘价
                          example: "0.01577100"
                        - type: string
                          description: Volume
                          x-description-cn: 成交量
                          example: "148976.11427815"
                        - type: integer
                          format: int64
                          description: Close time
                          x-description-cn: 收盘时间
                          example: 1499644799999
                        - type: string
                          description: Quote asset volume
                          x-description-cn: 成交额
                          example: "2434.19055334"
                        - type: integer
                          description: Number of trades
                          x-description-cn: 成交笔数
                          example: 308
                        - type: string
                          description: Taker buy base asset volume
                          x-description-cn: 主动买入成交量
                          example: "1756.87402397"
                        - type: string
                          description: Taker buy quote asset volume
                          x-description-cn: 主动买入成交额
                          example: "28.46694368"
                        - type: string
                          description: Ignore
                          x-description-cn: 忽略字段
                          example: "0"
                      items:
                        oneOf:
                          - type: integer
                            format: int64
                            description: Open time
                            x-description-cn: 开盘时间
                            example: 1499040000000
                          - type: string
                            description: Open
                            x-description-cn: 开盘价
                            example: "0.01634790"
                          - type: string
                            description: High
                            x-description-cn: 最高价
                            example: "0.80000000"
                          - type: string
                            description: Low
                            x-description-cn: 最低价
                            example: "0.01575800"
                          - type: string
                            description: Close
                            x-description-cn: 收盘价
                            example: "0.01577100"
                          - type: string
                            description: Volume
                            x-description-cn: 成交量
                            example: "148976.11427815"
                          - type: integer
                            format: int64
                            description: Close time
                            x-description-cn: 收盘时间
                            example: 1499644799999
                          - type: string
                            description: Quote asset volume
                            x-description-cn: 成交额
                            example: "2434.19055334"
                          - type: integer
                            description: Number of trades
                            x-description-cn: 成交笔数
                            example: 308
                          - type: string
                            description: Taker buy base asset volume
                            x-description-cn: 主动买入成交量
                            example: "1756.87402397"
                          - type: string
                            description: Taker buy quote asset volume
                            x-description-cn: 主动买入成交额
                            example: "28.46694368"
                          - type: string
                            description: Ignore
                            x-description-cn: 忽略字段
                            example: "0"
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 2
  /ticker:
    post:
      summary: Rolling window price change statistics
      x-summary-cn: 滚动窗口价格变动统计
      description: >-
        Get rolling window price change statistics with a custom window.


        This request is similar to [`ticker.24hr`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker-24hr) but
        statistics are computed on demand using the arbitrary window you specify.


        **Note:** Window size precision is limited to 1 minute.

        While the `closeTime` is the current time of the request, `openTime` always start on a minute boundary.

        As such, the effective window might be up to 59999 ms wider than the requested `windowSize`.


        <details>

        <summary>Window computation example</summary>


        For example, a request for `"windowSize": "7d"` might result in the following window:


        ```javascript

        {
            "openTime": 1659580020000,
            "closeTime": 1660184865291
        }

        ```


        Time of the request – `closeTime` – is 1660184865291 (August 11, 2022 02:27:45.291).

        Requested window size should put the `openTime` 7 days before that – August 4, 02:27:45.291 –

        but due to limited precision it ends up a bit earlier: 1659580020000 (August 4, 2022 02:27:00),

        exactly at the start of a minute.

        </details>


        If you need to continuously monitor trading statistics, please consider using WebSocket Streams:
          * `<symbol>@ticker_<window_size>` or `!ticker_<window-size>@arr`
      x-description-cn: |-
        使用自定义窗口获取滚动窗口价格变化统计信息。

        这个请求类似于 [`ticker.24hr`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker-24hr)，但统计数据是使用指定的任意窗口按需计算的。

        **注意：** 窗口大小精度限制为1分钟。
        虽然 `closeTime` 是请求的当前时间，`openTime` 总是从分钟边界开始。
        因此，有效窗口可能比请求的 `windowSize` 宽59999毫秒。

        <details>
        <summary>窗口计算示例</summary>

        例如，对 `"windowSize": "7d"` 的请求可能会导致以下窗口：

        ```javascript
        {
            "openTime": 1659580020000,
            "closeTime": 1660184865291
        }
        ```

        请求的时间 - `closeTime` - 是 1660184865291（2022年8月11日 02:27:45.291）。
        请求的窗口大小应将 `openTime` 设置为7天之前 – 8月4日，02:27:45.291 – 但由于精度有限，它最终会提前一点：1659580020000（2022年8月4日 02:27:00），正好在一分钟开始。
        </details>

        如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:
          * `<symbol>@ticker_<window_size>` 或者 `!ticker_<window-size>@arr`
      tags:
        - market
      operationId: ticker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/ticker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/Ticker/Ticker.go
      x-security-type: NONE
      x-weight: |-
        Adjusted based on the number of requested symbols:

        | Symbols | Weight |
        |:-------:|:------:|
        |    1–50 | 4 per symbol |
        |  51–100 |    200 |
      x-weight-cn: |-
        根据请求的交易对数量进行调整：

        | 交易对 | 权重 |
        |:-------:|:------:|
        |    1–50 | 每个交易对 4 |
        |  51–100 |    200 |
      x-parameters-notes: |-
        **Data Source:** Database

        Supported window sizes:

        Unit    | `windowSize` value
        ------- | ------------------
        minutes | `1m`, `2m` ... `59m`
        hours   | `1h`, `2h` ... `23h`
        days    | `1d`, `2d` ... `7d`

        Notes:

        * Either `symbol` or `symbols` must be specified.

        * Maximum number of symbols in one request: 200.

        * Window size units cannot be combined.
          E.g., <code>1d 2h</code> is not supported.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        支持的窗口 size:

        单位    | `windowSize` 值
        ------- | ------------------
        minutes | `1m`, `2m` ... `59m`
        hours   | `1h`, `2h` ... `23h`
        days    | `1d`, `2d` ... `7d`

        备注：

        * 必须指定 `symbol` 或 `symbols`。

        * 一个请求中的最大交易对数：200。

        * 窗口 size 单位不能合并。
          比如不支持 <code>1d 2h</code>。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ticker
                  example: ticker
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      description: Query ticker of a single symbol
                      x-description-cn: 获取单个交易对的ticker
                      example: BNBUSDT
                    symbols:
                      type: array
                      description: Query ticker for multiple symbols
                      x-description-cn: 获取多个交易对的ticker
                      items:
                        type: string
                        example: BTCUSDT
                    type:
                      type: string
                      description: "Ticker type. Supported values: FULL (default) or MINI"
                      x-description-cn: "Ticker 类型: FULL (默认) 或者 MINI"
                      enum:
                        - FULL
                        - MINI
                      example: FULL
                    windowSize:
                      type: string
                      description: Defaults to 1d if no parameter provided.
                      x-description-cn: 默认为 1d
                      enum:
                        - 1m
                        - 2m
                        - 3m
                        - 4m
                        - 5m
                        - 6m
                        - 7m
                        - 8m
                        - 9m
                        - 10m
                        - 11m
                        - 12m
                        - 13m
                        - 14m
                        - 15m
                        - 16m
                        - 17m
                        - 18m
                        - 19m
                        - 20m
                        - 21m
                        - 22m
                        - 23m
                        - 24m
                        - 25m
                        - 26m
                        - 27m
                        - 28m
                        - 29m
                        - 30m
                        - 31m
                        - 32m
                        - 33m
                        - 34m
                        - 35m
                        - 36m
                        - 37m
                        - 38m
                        - 39m
                        - 40m
                        - 41m
                        - 42m
                        - 43m
                        - 44m
                        - 45m
                        - 46m
                        - 47m
                        - 48m
                        - 49m
                        - 50m
                        - 51m
                        - 52m
                        - 53m
                        - 54m
                        - 55m
                        - 56m
                        - 57m
                        - 58m
                        - 59m
                        - 1h
                        - 2h
                        - 3h
                        - 4h
                        - 5h
                        - 6h
                        - 7h
                        - 8h
                        - 9h
                        - 10h
                        - 11h
                        - 12h
                        - 13h
                        - 14h
                        - 15h
                        - 16h
                        - 17h
                        - 18h
                        - 19h
                        - 20h
                        - 21h
                        - 22h
                        - 23h
                        - 1d
                        - 2d
                        - 3d
                        - 4d
                        - 5d
                        - 6d
                        - 7d
                      example: 1d
                    symbolStatus:
                      type: string
                      description: >-
                        Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch
                        returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching
                        ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220
                        交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ticker
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                type: FULL
                windowSize: 1d
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Rolling window price change statistics
          x-description-cn: 滚动窗口价格变动统计
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`FULL` type, for a single symbol:"
                    x-description-cn: "`FULL` 类型，对于单个交易对："
                    type: object
                    properties:
                      id:
                        type: string
                        example: bdb7c503-542c-495c-b797-4d2ee2e91173
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNBBTC
                          priceChange:
                            type: string
                            example: "0.00061500"
                            description: Absolute price change
                            x-description-cn: 价格变化
                          priceChangePercent:
                            type: string
                            example: "4.735"
                            description: Relative price change in percent
                            x-description-cn: 价格变化百分比
                          weightedAvgPrice:
                            type: string
                            example: "0.01368242"
                            description: QuoteVolume / Volume
                            x-description-cn: QuoteVolume / 成交量
                          openPrice:
                            type: string
                            example: "0.01298900"
                          highPrice:
                            type: string
                            example: "0.01418800"
                          lowPrice:
                            type: string
                            example: "0.01296000"
                          lastPrice:
                            type: string
                            example: "0.01360400"
                          volume:
                            type: string
                            example: "587179.23900000"
                          quoteVolume:
                            type: string
                            example: "8034.03382165"
                            description: Sum of (price * volume) for all trades
                            x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                          openTime:
                            type: integer
                            format: int64
                            example: 1659580020000
                            description: Open time for ticker window
                            x-description-cn: ticker的开始时间
                          closeTime:
                            type: integer
                            format: int64
                            example: 1660184865291
                            description: Close time for ticker window
                            x-description-cn: ticker的结束时间
                          firstId:
                            type: integer
                            format: int64
                            example: 192977765
                            description: Trade IDs
                            x-description-cn: 统计时间内的第一笔trade id
                          lastId:
                            type: integer
                            format: int64
                            example: 195365758
                          count:
                            type: integer
                            format: int64
                            example: 2387994
                            description: Number of trades in the interval
                            x-description-cn: 统计时间内交易笔数
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
                  - description: "`MINI` type, for a single symbol:"
                    x-description-cn: "`MINI` 类型，对于单个交易对："
                    type: object
                    properties:
                      id:
                        type: string
                        example: bdb7c503-542c-495c-b797-4d2ee2e91173
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNBBTC
                          openPrice:
                            type: string
                            example: "0.01298900"
                          highPrice:
                            type: string
                            example: "0.01418800"
                          lowPrice:
                            type: string
                            example: "0.01296000"
                          lastPrice:
                            type: string
                            example: "0.01360400"
                          volume:
                            type: string
                            example: "587179.23900000"
                          quoteVolume:
                            type: string
                            description: Sum of (price * volume) for all trades
                            x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                            example: "8034.03382165"
                          openTime:
                            type: integer
                            format: int64
                            description: Open time for ticker window
                            x-description-cn: ticker的开始时间
                            example: 1659580020000
                          closeTime:
                            type: integer
                            format: int64
                            description: Close time for ticker window
                            x-description-cn: ticker的结束时间
                            example: 1660184865291
                          firstId:
                            type: integer
                            format: int64
                            description: First trade ID
                            x-description-cn: 第一个交易 ID
                            example: 192977765
                          lastId:
                            type: integer
                            format: int64
                            description: Last trade ID
                            x-description-cn: 最后交易 ID
                            example: 195365758
                          count:
                            type: integer
                            format: int64
                            description: Number of trades
                            x-description-cn: 成交笔数
                            example: 2387994
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              description: Number of trades
                              x-description-cn: 成交笔数
                              example: 4
                  - description: "If more than one symbol is requested, response returns an array:"
                    x-description-cn: "如果请求是有多个交易对，响应会是数组类型:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: f4b3b507-c8f2-442a-81a6-b2f12daa030f
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        example:
                          - symbol: BNBBTC
                            priceChange: "0.00061500"
                            priceChangePercent: "4.735"
                            weightedAvgPrice: "0.01368242"
                            openPrice: "0.01298900"
                            highPrice: "0.01418800"
                            lowPrice: "0.01296000"
                            lastPrice: "0.01360400"
                            volume: "587169.48600000"
                            quoteVolume: "8033.90114517"
                            openTime: 1659580020000
                            closeTime: 1660184820927
                            firstId: 192977765
                            lastId: 195365700
                            count: 2387936
                          - symbol: BTCUSDT
                            priceChange: "1182.92000000"
                            priceChangePercent: "5.113"
                            weightedAvgPrice: "23349.27074846"
                            openPrice: "23135.33000000"
                            highPrice: "24491.22000000"
                            lowPrice: "22400.00000000"
                            lastPrice: "24318.25000000"
                            volume: "1039498.10978000"
                            quoteVolume: "24271522807.76838630"
                            openTime: 1659580020000
                            closeTime: 1660184820927
                            firstId: 1568787779
                            lastId: 1604337406
                            count: 35549628
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BNBBTC
                            priceChange:
                              type: string
                              example: "0.00061500"
                              description: Absolute price change
                              x-description-cn: 价格变化
                            priceChangePercent:
                              type: string
                              example: "4.735"
                              description: Relative price change in percent
                              x-description-cn: 价格变化百分比
                            weightedAvgPrice:
                              type: string
                              example: "0.01368242"
                              description: QuoteVolume / Volume
                              x-description-cn: QuoteVolume / 成交量
                            openPrice:
                              type: string
                              example: "0.01298900"
                            highPrice:
                              type: string
                              example: "0.01418800"
                            lowPrice:
                              type: string
                              example: "0.01296000"
                            lastPrice:
                              type: string
                              example: "0.01360400"
                            volume:
                              type: string
                              example: "587169.48600000"
                            quoteVolume:
                              type: string
                              example: "8033.90114517"
                              description: Sum of (price * volume) for all trades
                              x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                            openTime:
                              type: integer
                              format: int64
                              example: 1659580020000
                              description: Open time for ticker window
                              x-description-cn: ticker的开始时间
                            closeTime:
                              type: integer
                              format: int64
                              example: 1660184820927
                              description: Close time for ticker window
                              x-description-cn: ticker的结束时间
                            firstId:
                              type: integer
                              format: int64
                              example: 192977765
                              description: Trade IDs
                              x-description-cn: 统计时间内的第一笔trade id
                            lastId:
                              type: integer
                              format: int64
                              example: 195365700
                            count:
                              type: integer
                              format: int64
                              example: 2387936
                              description: Number of trades in the interval
                              x-description-cn: 统计时间内交易笔数
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 8
  /ticker.24hr:
    post:
      summary: 24hr ticker price change statistics
      x-summary-cn: 24hr 价格变动情况
      description: >-
        Get 24-hour rolling window price change statistics.


        If you need to continuously monitor trading statistics, please consider using WebSocket Streams:


        * [`<symbol>@ticker`](/products/spot/web-socket-streams#individual-symbol-ticker-streams) or `!ticker@arr`


        * [`<symbol>@miniTicker`](/products/spot/web-socket-streams#individual-symbol-mini-ticker-stream) or
        [`!miniTicker@arr`](/products/spot/web-socket-streams#all-market-mini-tickers-stream)


        If you need different window sizes,


        use the [`ticker`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker) request.
      x-description-cn: >-
        24 小时滚动窗口价格变动数据。

        如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:


        * [`<symbol>@ticker`](/products/spot/web-socket-streams#individual-symbol-ticker-streams)

        * [`<symbol>@miniTicker`](/products/spot/web-socket-streams#individual-symbol-mini-ticker-stream) 或者
        [`!miniTicker@arr`](/products/spot/web-socket-streams#all-market-mini-tickers-stream)


        如果你想用不同的窗口数量，可以用 [`ticker`](/catalog/core-trading-spot-trading/api/ws-api/market#ticker) 请求。
      tags:
        - market
      operationId: ticker24hr
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ticker24hr
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/ticker24hr.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ticker24hr.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ticker24hr.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/Ticker24hrExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/Ticker24hr/Ticker24hr.go
      x-legacy-anchors:
        - twentyfourhourticker
      x-security-type: NONE
      x-weight: |-
        Adjusted based on the number of requested symbols:

        |Parameter|Symbols Provided|Weight|
        |---|---|---|
        |symbol| 1 |2|
        | |omitted| 80|
        |symbols| 1-20 |2|
        | | 21-100 |40|
        | | 101+ |80|
        | |omitted| 80|
      x-weight-cn: |-
        根据请求的交易对数量进行调整：

        |参数|提供Symbol数量|权重|
        |---|---|---|
        |symbol| 1 |2|
        | |不提供| 80|
        |symbols| 1-20 |2|
        | | 21-100 |40|
        | | 101+ |80|
        | |不提供| 80|
      x-parameters-notes: |-
        **Data Source:** Memory

        Notes:

        * `symbol` and `symbols` cannot be used together.

        * If no symbol is specified, returns information about all symbols currently trading on the exchange.
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        备注:

        * `symbol` 和 `symbols` 不能同时用。

        * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ticker.24hr
                  example: ticker.24hr
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    symbols:
                      type: array
                      items:
                        type: string
                        example: BTCUSDT
                    type:
                      type: string
                      description: "Ticker type. Supported values: FULL (default) or MINI"
                      x-description-cn: "Ticker 类型: FULL (默认) 或者 MINI"
                      enum:
                        - FULL
                        - MINI
                      example: FULL
                    symbolStatus:
                      type: string
                      description: >-
                        Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch
                        returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching
                        ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220
                        交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ticker.24hr
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                type: FULL
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: 24hr ticker price change statistics
          x-description-cn: 24hr 价格变动情况
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`FULL` type, for a single symbol:"
                    x-description-cn: "`FULL` 类型，对于单个交易对："
                    type: object
                    properties:
                      id:
                        type: string
                        example: 9fa2a91b-3fca-4ed7-a9ad-58e3b67483de
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNBBTC
                            description: Symbol Name
                            x-description-cn: 交易对
                          priceChange:
                            type: string
                            example: "0.00013900"
                          priceChangePercent:
                            type: string
                            example: "1.020"
                          weightedAvgPrice:
                            type: string
                            example: "0.01382453"
                          prevClosePrice:
                            type: string
                            example: "0.01362800"
                          lastPrice:
                            type: string
                            example: "0.01376700"
                            description: Closing price of the interval
                            x-description-cn: 间隔收盘价
                          lastQty:
                            type: string
                            example: "1.78800000"
                          bidPrice:
                            type: string
                            example: "0.01376700"
                          bidQty:
                            type: string
                            example: "4.64600000"
                          askPrice:
                            type: string
                            example: "0.01376800"
                          askQty:
                            type: string
                            example: "14.31400000"
                          openPrice:
                            type: string
                            example: "0.01362800"
                            description: Opening price of the Interval
                            x-description-cn: 间隔开盘价
                          highPrice:
                            type: string
                            example: "0.01414900"
                            description: Highest price in the interval
                            x-description-cn: 间隔最高价
                          lowPrice:
                            type: string
                            example: "0.01346600"
                            description: Lowest  price in the interval
                            x-description-cn: 间隔最低价
                          volume:
                            type: string
                            example: "69412.40500000"
                            description: Total trade volume (in base asset)
                            x-description-cn: 总交易量 (base asset)
                          quoteVolume:
                            type: string
                            example: "959.59411487"
                            description: Total trade volume (in quote asset)
                            x-description-cn: 总交易量 (quote asset)
                          openTime:
                            type: integer
                            format: int64
                            example: 1660014164909
                            description: Start of the ticker interval
                            x-description-cn: ticker间隔的开始时间
                          closeTime:
                            type: integer
                            format: int64
                            example: 1660100564909
                            description: End of the ticker interval
                            x-description-cn: ticker间隔的结束时间
                          firstId:
                            type: integer
                            format: int64
                            example: 194696115
                            description: First tradeId
                            x-description-cn: 首笔成交id
                          lastId:
                            type: integer
                            format: int64
                            example: 194968287
                            description: Last tradeId
                            x-description-cn: 末笔成交id
                          count:
                            type: integer
                            format: int64
                            example: 272173
                            description: Trade count
                            x-description-cn: 成交笔数
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - description: "`MINI` type, for a single symbol:"
                    x-description-cn: "`MINI` 类型，对于单个交易对："
                    type: object
                    properties:
                      id:
                        type: string
                        example: 9fa2a91b-3fca-4ed7-a9ad-58e3b67483de
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            description: Symbol Name
                            x-description-cn: 交易对
                            example: BNBBTC
                          openPrice:
                            type: string
                            description: Opening price of the Interval
                            x-description-cn: 间隔开盘价
                            example: "0.01362800"
                          highPrice:
                            type: string
                            description: Highest price in the interval
                            x-description-cn: 间隔最高价
                            example: "0.01414900"
                          lowPrice:
                            type: string
                            description: Lowest  price in the interval
                            x-description-cn: 间隔最低价
                            example: "0.01346600"
                          lastPrice:
                            type: string
                            description: Closing price of the interval
                            x-description-cn: 间隔收盘价
                            example: "0.01376700"
                          volume:
                            type: string
                            description: Total trade volume (in base asset)
                            x-description-cn: 总交易量 (base asset)
                            example: "69412.40500000"
                          quoteVolume:
                            type: string
                            description: Total trade volume (in quote asset)
                            x-description-cn: 总交易量 (quote asset)
                            example: "959.59411487"
                          openTime:
                            type: integer
                            format: int64
                            description: Start of the ticker interval
                            x-description-cn: ticker间隔的开始时间
                            example: 1660014164909
                          closeTime:
                            type: integer
                            format: int64
                            description: End of the ticker interval
                            x-description-cn: ticker间隔的结束时间
                            example: 1660100564909
                          firstId:
                            type: integer
                            format: int64
                            description: First trade ID
                            x-description-cn: 第一个交易 ID
                            example: 194696115
                          lastId:
                            type: integer
                            format: int64
                            description: Last trade ID
                            x-description-cn: 最后一个交易ID
                            example: 194968287
                          count:
                            type: integer
                            format: int64
                            description: Number of trades
                            x-description-cn: 成交笔数
                            example: 272173
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              description: Number of trades
                              x-description-cn: 成交笔数
                              example: 2
                  - description: "If more than one symbol is requested, response returns an array:"
                    x-description-cn: "如果请求是有多个交易对，响应会是数组类型:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: 901be0d9-fd3b-45e4-acd6-10c580d03430
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        example:
                          - symbol: BNBBTC
                            priceChange: "0.00016500"
                            priceChangePercent: "1.213"
                            weightedAvgPrice: "0.01382508"
                            prevClosePrice: "0.01360800"
                            lastPrice: "0.01377200"
                            lastQty: "1.01400000"
                            bidPrice: "0.01377100"
                            bidQty: "7.55700000"
                            askPrice: "0.01377200"
                            askQty: "4.37900000"
                            openPrice: "0.01360700"
                            highPrice: "0.01414900"
                            lowPrice: "0.01346600"
                            volume: "69376.27900000"
                            quoteVolume: "959.13277091"
                            openTime: 1660014615517
                            closeTime: 1660101015517
                            firstId: 194697254
                            lastId: 194969483
                            count: 272230
                          - symbol: BTCUSDT
                            priceChange: "-938.06000000"
                            priceChangePercent: "-3.938"
                            weightedAvgPrice: "23265.34432003"
                            prevClosePrice: "23819.17000000"
                            lastPrice: "22880.91000000"
                            lastQty: "0.00536000"
                            bidPrice: "22880.40000000"
                            bidQty: "0.00424000"
                            askPrice: "22880.91000000"
                            askQty: "0.04276000"
                            openPrice: "23818.97000000"
                            highPrice: "23933.25000000"
                            lowPrice: "22664.69000000"
                            volume: "153508.37606000"
                            quoteVolume: "3571425225.04441220"
                            openTime: 1660014615977
                            closeTime: 1660101015977
                            firstId: 1592019902
                            lastId: 1597301762
                            count: 5281861
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BNBBTC
                              description: Symbol Name
                              x-description-cn: 交易对
                            priceChange:
                              type: string
                              example: "0.00016500"
                            priceChangePercent:
                              type: string
                              example: "1.213"
                            weightedAvgPrice:
                              type: string
                              example: "0.01382508"
                            prevClosePrice:
                              type: string
                              example: "0.01360800"
                            lastPrice:
                              type: string
                              example: "0.01377200"
                              description: Closing price of the interval
                              x-description-cn: 间隔收盘价
                            lastQty:
                              type: string
                              example: "1.01400000"
                            bidPrice:
                              type: string
                              example: "0.01377100"
                            bidQty:
                              type: string
                              example: "7.55700000"
                            askPrice:
                              type: string
                              example: "0.01377200"
                            askQty:
                              type: string
                              example: "4.37900000"
                            openPrice:
                              type: string
                              example: "0.01360700"
                              description: Opening price of the Interval
                              x-description-cn: 间隔开盘价
                            highPrice:
                              type: string
                              example: "0.01414900"
                              description: Highest price in the interval
                              x-description-cn: 间隔最高价
                            lowPrice:
                              type: string
                              example: "0.01346600"
                              description: Lowest  price in the interval
                              x-description-cn: 间隔最低价
                            volume:
                              type: string
                              example: "69376.27900000"
                              description: Total trade volume (in base asset)
                              x-description-cn: 总交易量 (base asset)
                            quoteVolume:
                              type: string
                              example: "959.13277091"
                              description: Total trade volume (in quote asset)
                              x-description-cn: 总交易量 (quote asset)
                            openTime:
                              type: integer
                              format: int64
                              example: 1660014615517
                              description: Start of the ticker interval
                              x-description-cn: ticker间隔的开始时间
                            closeTime:
                              type: integer
                              format: int64
                              example: 1660101015517
                              description: End of the ticker interval
                              x-description-cn: ticker间隔的结束时间
                            firstId:
                              type: integer
                              format: int64
                              example: 194697254
                              description: First tradeId
                              x-description-cn: 首笔成交id
                            lastId:
                              type: integer
                              format: int64
                              example: 194969483
                              description: Last tradeId
                              x-description-cn: 末笔成交id
                            count:
                              type: integer
                              format: int64
                              example: 272230
                              description: Trade count
                              x-description-cn: 成交笔数
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
  /ticker.book:
    post:
      summary: Symbol order book ticker
      x-summary-cn: 当前最优挂单
      description: |-
        Get the current best price and quantity on the order book.

        If you need access to real-time order book ticker updates, please
        consider using WebSocket Streams:

        * [`<symbol>@bookTicker`](/products/spot/web-socket-streams#individual-symbol-book-ticker-streams)
      x-description-cn: |-
        在订单簿获取当前最优价格和数量。

        如果您需要访问实时订单簿 ticker 更新，请考虑使用 WebSocket Streams:

        * [`<symbol>@bookTicker`](/products/spot/web-socket-streams#individual-symbol-book-ticker-streams)
      tags:
        - market
      operationId: tickerBook
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ticker-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tickerBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ticker_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ticker_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TickerBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TickerBook/TickerBook.go
      x-security-type: NONE
      x-weight: |-
        Adjusted based on the number of requested symbols:

        |Parameter|Symbols Provided|Weight|
        |---|---|---|
        |symbol| 1 |2|
        | |omitted| 4|
        |symbols| Any |4|
      x-weight-cn: |-
        根据请求的交易对数量进行调整：

        |参数|提供Symbol数量|权重|
        |---|---|---|
        |symbol| 1 |2|
        | |不提供| 4|
        |symbols| 任意 |4|
      x-parameters-notes: |-
        **Data Source:** Memory

        Notes:

        * `symbol` and `symbols` cannot be used together.

        * If no symbol is specified, returns information about all symbols currently trading on the exchange.
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        备注：

        * `symbol` 和 `symbols` 不能一起使用。

        * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ticker.book
                  example: ticker.book
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      description: Query ticker for a single symbol
                      x-description-cn: 获取单个交易对的ticker
                      example: BNBUSDT
                    symbols:
                      type: array
                      description: Query ticker for multiple symbols
                      x-description-cn: 获取多个交易对的ticker
                      items:
                        type: string
                        example: BTCUSDT
                    symbolStatus:
                      type: string
                      description: >-
                        Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch
                        returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching
                        ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220
                        交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ticker.book
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Symbol order book ticker
          x-description-cn: 当前最优挂单
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        example: 9d32157c-a556-4d27-9866-66760a174b57
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNBBTC
                          bidPrice:
                            type: string
                            example: "0.01358000"
                            description: best bid price.
                            x-description-cn: 最优买单价
                          bidQty:
                            type: string
                            example: "12.53400000"
                            description: bid/ask qty.
                            x-description-cn: 挂单量
                          askPrice:
                            type: string
                            example: "0.01358100"
                            description: best ask price.
                            x-description-cn: 最优卖单价
                          askQty:
                            type: string
                            example: "17.83700000"
                            description: bid/ask qty.
                            x-description-cn: 挂单量
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - type: object
                    properties:
                      id:
                        type: string
                        example: 057deb3a-2990-41d1-b58b-98ea0f09e1b4
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        example:
                          - symbol: BNBBTC
                            bidPrice: "0.01358000"
                            bidQty: "12.53400000"
                            askPrice: "0.01358100"
                            askQty: "17.83700000"
                          - symbol: BTCUSDT
                            bidPrice: "23980.49000000"
                            bidQty: "0.01000000"
                            askPrice: "23981.31000000"
                            askQty: "0.01512000"
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BNBBTC
                            bidPrice:
                              type: string
                              example: "0.01358000"
                              description: best bid price.
                              x-description-cn: 最优买单价
                            bidQty:
                              type: string
                              example: "12.53400000"
                              description: bid/ask qty.
                              x-description-cn: 挂单量
                            askPrice:
                              type: string
                              example: "0.01358100"
                              description: best ask price.
                              x-description-cn: 最优卖单价
                            askQty:
                              type: string
                              example: "17.83700000"
                              description: bid/ask qty.
                              x-description-cn: 挂单量
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
  /ticker.price:
    post:
      summary: Symbol price ticker
      x-summary-cn: 最新价格
      description: |-
        Get the latest market price for a symbol.

        If you need access to real-time price updates, please consider using
        WebSocket Streams:

        * `<symbol>@aggTrade`

        * `<symbol>@trade`
      x-description-cn: |-
        获取交易对最新价格

        如果需要访问实时价格更新，请考虑使用 WebSocket Streams:

        * `<symbol>@aggTrade`
        * `<symbol>@trade`
      tags:
        - market
      operationId: tickerPrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ticker-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tickerPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ticker_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ticker_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TickerPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TickerPrice/TickerPrice.go
      x-security-type: NONE
      x-weight: |-
        Adjusted based on the number of requested symbols:

        |Parameter|Symbols Provided|Weight|
        |---|---|---|
        |symbol| 1 |2|
        | |omitted| 4|
        |symbols| Any |4|
      x-weight-cn: |-
        根据请求的交易对数量进行调整：

        |参数|提供Symbol数量|权重|
        |---|---|---|
        |symbol| 1 |2|
        | |不提供| 4|
        |symbols| 任意 |4|
      x-parameters-notes: |-
        **Data Source:** Memory

        Notes:

        * `symbol` and `symbols` cannot be used together.

        * If no symbol is specified, returns information about all symbols currently trading on the exchange.
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        备注：

        * `symbol` 和 `symbols` 不能一起使用。

        * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ticker.price
                  example: ticker.price
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      description: Query price for a single symbol
                      x-description-cn: 获取单个交易对的价格
                      example: BNBUSDT
                    symbols:
                      type: array
                      description: Query price for multiple symbols
                      x-description-cn: 获取多个交易对的价格
                      items:
                        type: string
                        example: BTCUSDT
                    symbolStatus:
                      type: string
                      description: >-
                        Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch
                        returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching
                        ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220
                        交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ticker.price
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Symbol price ticker
          x-description-cn: 最新价格
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        example: 043a7cf2-bde3-4888-9604-c8ac41fcba4d
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNBBTC
                          price:
                            type: string
                            example: "0.01361900"
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - type: object
                    properties:
                      id:
                        type: string
                        example: e739e673-24c8-4adf-9cfa-b81f30330b09
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        example:
                          - symbol: BNBBTC
                            price: "0.01363700"
                          - symbol: BTCUSDT
                            price: "24267.15000000"
                          - symbol: BNBBUSD
                            price: "331.10000000"
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BNBBTC
                            price:
                              type: string
                              example: "0.01363700"
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
  /ticker.tradingDay:
    post:
      summary: Trading Day Ticker
      x-summary-cn: 交易日行情(Ticker)
      description: Price change statistics for a trading day.
      x-description-cn: 交易日价格变动统计。
      tags:
        - market
      operationId: tickerTradingDay
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ticker-trading-day
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tickerTradingDay.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ticker_trading_day.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ticker_trading_day.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TickerTradingDayExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TickerTradingDay/TickerTradingDay.go
      x-security-type: NONE
      x-weight: >-
        4 for each requested symbol regardless of windowSize. The weight for this request will cap at 200 once the
        number of symbols in the request is more than 50.
      x-weight-cn: 每个交易对占用 4 个权重，与 windowSize 无关。当请求中的交易对数量超过 50 时，此请求的权重上限为 200。
      x-parameters-notes: |
        **Data Source:** Database

        **Notes:**

        * Supported values for `timeZone`:
          * Hours and minutes (e.g. `-1:00`, `05:45`)
          * Only hours (e.g. `0`, `8`, `4`)
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        **注意:**

        * `timeZone`支持的值包括：
            * 小时和分钟（例如 `-1:00`，`05:45`）
            * 仅小时（例如 `0`，`8`，`4`）
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - ticker.tradingDay
                  example: ticker.tradingDay
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    symbols:
                      type: array
                      items:
                        type: string
                        example: BTCUSDT
                    timeZone:
                      type: string
                      description: "Default: 0 (UTC)"
                      x-description-cn: 默认值： 0 (UTC)
                      example: "0"
                    type:
                      type: string
                      description: "Ticker type. Supported values: FULL (default) or MINI"
                      x-description-cn: "Ticker 类型: FULL (默认) 或者 MINI"
                      enum:
                        - FULL
                        - MINI
                      example: FULL
                    symbolStatus:
                      type: string
                      description: >-
                        Filters for symbols that have this `tradingStatus`. For a single symbol, a status mismatch
                        returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`. For multiple or all symbols, non-matching
                        ones are simply excluded from the response. Valid values: `TRADING`, `HALT`, `BREAK`,
                        `CANCEL_ONLY`
                      x-description-cn: >-
                        过滤具有此 `tradingStatus` 的交易对。对于单个交易对，如果状态不匹配，将返回错误 `-1220
                        交易对与状态不匹配`。对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。有效值： `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                      example: TRADING
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: ticker.tradingDay
              params:
                symbol: BNBUSDT
                symbols:
                  - BTCUSDT
                timeZone: "0"
                type: FULL
                symbolStatus: TRADING
      responses:
        Successful Response:
          description: Trading Day Ticker
          x-description-cn: Trading Day 行情
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`FULL` type, with `symbol`:"
                    x-description-cn: "`FULL` 类型，有 `symbol`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: f4b3b507-c8f2-442a-81a6-b2f12daa030f
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          priceChange:
                            type: string
                            description: Absolute price change
                            x-description-cn: 绝对价格变动
                            example: "-83.13000000"
                          priceChangePercent:
                            type: string
                            description: Relative price change in percent
                            x-description-cn: 相对价格变动百分比
                            example: "-0.317"
                          weightedAvgPrice:
                            type: string
                            description: quoteVolume / volume
                            x-description-cn: 报价成交量 / 成交量
                            example: "26234.58803036"
                          openPrice:
                            type: string
                            example: "26304.80000000"
                          highPrice:
                            type: string
                            example: "26397.46000000"
                          lowPrice:
                            type: string
                            example: "26088.34000000"
                          lastPrice:
                            type: string
                            example: "26221.67000000"
                          volume:
                            type: string
                            description: Volume in base asset
                            x-description-cn: 基础资产的成交量
                            example: "18495.35066000"
                          quoteVolume:
                            type: string
                            example: "485217905.04210480"
                          openTime:
                            type: integer
                            format: int64
                            example: 1695686400000
                          closeTime:
                            type: integer
                            format: int64
                            example: 1695772799999
                          firstId:
                            type: integer
                            format: int64
                            example: 3220151555
                          lastId:
                            type: integer
                            format: int64
                            example: 3220849281
                          count:
                            type: integer
                            format: int64
                            example: 697727
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
                  - description: "`FULL` type, with `symbols`:"
                    x-description-cn: "`FULL` 类型，有 `symbols`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: f4b3b507-c8f2-442a-81a6-b2f12daa030f
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            priceChange: "-83.13000000"
                            priceChangePercent: "-0.317"
                            weightedAvgPrice: "26234.58803036"
                            openPrice: "26304.80000000"
                            highPrice: "26397.46000000"
                            lowPrice: "26088.34000000"
                            lastPrice: "26221.67000000"
                            volume: "18495.35066000"
                            quoteVolume: "485217905.04210480"
                            openTime: 1695686400000
                            closeTime: 1695772799999
                            firstId: 3220151555
                            lastId: 3220849281
                            count: 697727
                          - symbol: BNBUSDT
                            priceChange: "2.60000000"
                            priceChangePercent: "1.238"
                            weightedAvgPrice: "211.92276958"
                            openPrice: "210.00000000"
                            highPrice: "213.70000000"
                            lowPrice: "209.70000000"
                            lastPrice: "212.60000000"
                            volume: "280709.58900000"
                            quoteVolume: "59488753.54750000"
                            openTime: 1695686400000
                            closeTime: 1695772799999
                            firstId: 672397461
                            lastId: 672496158
                            count: 98698
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            priceChange:
                              type: string
                              example: "-83.13000000"
                              description: Absolute price change
                              x-description-cn: 绝对价格变动
                            priceChangePercent:
                              type: string
                              example: "-0.317"
                              description: Relative price change in percent
                              x-description-cn: 相对价格变动百分比
                            weightedAvgPrice:
                              type: string
                              example: "26234.58803036"
                              description: quoteVolume / volume
                              x-description-cn: 报价成交量 / 成交量
                            openPrice:
                              type: string
                              example: "26304.80000000"
                            highPrice:
                              type: string
                              example: "26397.46000000"
                            lowPrice:
                              type: string
                              example: "26088.34000000"
                            lastPrice:
                              type: string
                              example: "26221.67000000"
                            volume:
                              type: string
                              example: "18495.35066000"
                              description: Volume in base asset
                              x-description-cn: 基础资产的成交量
                            quoteVolume:
                              type: string
                              example: "485217905.04210480"
                              description: Volume in quote asset
                              x-description-cn: 报价资产的成交量
                            openTime:
                              type: integer
                              format: int64
                              example: 1695686400000
                            closeTime:
                              type: integer
                              format: int64
                              example: 1695772799999
                            firstId:
                              type: integer
                              format: int64
                              example: 3220151555
                              description: Trade ID of the first trade in the interval
                              x-description-cn: 区间内的第一个交易的交易ID
                            lastId:
                              type: integer
                              format: int64
                              example: 3220849281
                              description: Trade ID of the last trade in the interval
                              x-description-cn: 区间内的最后一个交易的交易ID
                            count:
                              type: integer
                              format: int64
                              example: 697727
                              description: Number of trades in the interval
                              x-description-cn: 区间内的交易数量
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 8
                  - description: "`MINI` type, with `symbol`:"
                    x-description-cn: "`MINI` 类型，有 `symbol`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: f4b3b507-c8f2-442a-81a6-b2f12daa030f
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          openPrice:
                            type: string
                            example: "26304.80000000"
                          highPrice:
                            type: string
                            example: "26397.46000000"
                          lowPrice:
                            type: string
                            example: "26088.34000000"
                          lastPrice:
                            type: string
                            example: "26221.67000000"
                          volume:
                            type: string
                            description: Volume in base asset
                            x-description-cn: 基础资产的成交量
                            example: "18495.35066000"
                          quoteVolume:
                            type: string
                            description: Volume in quote asset
                            x-description-cn: 报价资产的成交量
                            example: "485217905.04210480"
                          openTime:
                            type: integer
                            format: int64
                            example: 1695686400000
                          closeTime:
                            type: integer
                            format: int64
                            example: 1695772799999
                          firstId:
                            type: integer
                            format: int64
                            description: Trade ID of the first trade in the interval
                            x-description-cn: 区间内的第一个交易的交易ID
                            example: 3220151555
                          lastId:
                            type: integer
                            format: int64
                            description: Trade ID of the last trade in the interval
                            x-description-cn: 区间内的最后一个交易的交易ID
                            example: 3220849281
                          count:
                            type: integer
                            format: int64
                            description: Number of trades in the interval
                            x-description-cn: 区间内的交易数量
                            example: 697727
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
                  - description: "`MINI` type, with `symbols`:"
                    x-description-cn: "`MINI` 类型，有 `symbols`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: f4b3b507-c8f2-442a-81a6-b2f12daa030f
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            openPrice:
                              type: string
                              example: "26304.80000000"
                            highPrice:
                              type: string
                              example: "26397.46000000"
                            lowPrice:
                              type: string
                              example: "26088.34000000"
                            lastPrice:
                              type: string
                              example: "26221.67000000"
                            volume:
                              type: string
                              description: Volume in base asset
                              x-description-cn: 基础资产的成交量
                              example: "18495.35066000"
                            quoteVolume:
                              type: string
                              description: Volume in quote asset
                              x-description-cn: 报价资产的成交量
                              example: "485217905.04210480"
                            openTime:
                              type: integer
                              format: int64
                              example: 1695686400000
                            closeTime:
                              type: integer
                              format: int64
                              example: 1695772799999
                            firstId:
                              type: integer
                              format: int64
                              description: Trade ID of the first trade in the interval
                              x-description-cn: 区间内的第一个交易的交易ID
                              example: 3220151555
                            lastId:
                              type: integer
                              format: int64
                              description: Trade ID of the last trade in the interval
                              x-description-cn: 区间内的最后一个交易的交易ID
                              example: 3220849281
                            count:
                              type: integer
                              format: int64
                              description: Number of trades in the interval
                              x-description-cn: 区间内的交易数量
                              example: 697727
                        example:
                          - symbol: BTCUSDT
                            openPrice: "26304.80000000"
                            highPrice: "26397.46000000"
                            lowPrice: "26088.34000000"
                            lastPrice: "26221.67000000"
                            volume: "18495.35066000"
                            quoteVolume: "485217905.04210480"
                            openTime: 1695686400000
                            closeTime: 1695772799999
                            firstId: 3220151555
                            lastId: 3220849281
                            count: 697727
                          - symbol: BNBUSDT
                            openPrice: "210.00000000"
                            highPrice: "213.70000000"
                            lowPrice: "209.70000000"
                            lastPrice: "212.60000000"
                            volume: "280709.58900000"
                            quoteVolume: "59488753.54750000"
                            openTime: 1695686400000
                            closeTime: 1695772799999
                            firstId: 672397461
                            lastId: 672496158
                            count: 98698
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 8
  /trades.aggregate:
    post:
      summary: Aggregate trades
      x-summary-cn: 归集交易
      description: >-
        Get aggregate trades.


        An *aggregate trade* (aggtrade) represents one or more individual

        trades.


        Trades that fill at the same time, from the same taker order, with the

        same price –


        those trades are collected into an aggregate trade with total quantity

        of the individual trades.


        If you need access to real-time trading activity, please consider using

        WebSocket Streams:


        * `<symbol>@aggTrade`


        If you need historical aggregate trade data, please consider using
        [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades).
      x-description-cn: |-
        获取归集交易。

        一个 *归集交易* (aggtrade) 代表一个或多个单独的交易。

        同时间，同 taker 订单和同价格的执行交易会被聚合为一条归集交易。

        如果需要访问实时交易活动，请考虑使用 WebSocket Streams：

        * `<symbol>@aggTrade`

        如果需要历史总交易数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades)。
      tags:
        - market
      operationId: tradesAggregate
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#trades-aggregate
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tradesAggregate.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/trades_aggregate.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/trades_aggregate.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TradesAggregateExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TradesAggregate/TradesAggregate.go
      x-ip-weight: 4
      x-security-type: NONE
      x-parameters-notes: >-
        **Data Source:** Database


        - If `fromId` is specified, return aggtrades with aggregate trade ID >= `fromId`. Use `fromId` and `limit` to
        page through all aggtrades.

        - If `startTime` and/or `endTime` are specified, aggtrades are filtered by execution time (`T`). `fromId` cannot
        be used together with `startTime` and `endTime`.

        - If no condition is specified, the most recent aggregate trades are returned.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        - 如果指定了 `fromId`，则返回归集交易ID >= `fromId` 的归集交易。使用 `fromId` 和 `limit` 分页查询所有归集交易。
        - 如果指定了 `startTime` 和/或 `endTime`，则按执行时间 (`T`) 过滤归集交易。`fromId` 不能与 `startTime` 和 `endTime` 同时使用。
        - 如果没有指定条件，将返回最近的归集交易。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - trades.aggregate
                  example: trades.aggregate
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    fromId:
                      type: integer
                      format: int64
                      example: 1
                      description: Aggregate trade ID to begin at
                      x-description-cn: 起始归集交易ID
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms to get aggregate trades from INCLUSIVE.
                      x-description-cn: 从该时刻之后的成交记录开始返回结果
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                      description: Timestamp in ms to get aggregate trades until INCLUSIVE.
                      x-description-cn: 返回该时刻为止的成交记录
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: trades.aggregate
              params:
                symbol: BNBUSDT
                fromId: 1
                startTime: 1735693200000
                endTime: 1735693200000
                limit: 1
      responses:
        Successful Response:
          description: Aggregate trades
          x-description-cn: 归集交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 189da436-d4bd-48ca-9f95-9f613d621717
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        a:
                          type: integer
                          format: int64
                          example: 50000000
                          description: Aggregate tradeId
                          x-description-cn: 归集成交ID
                        p:
                          type: string
                          example: "0.00274100"
                          description: Price
                          x-description-cn: 成交价
                        q:
                          type: string
                          example: "57.19000000"
                          description: Quantity
                          x-description-cn: 成交量
                        f:
                          type: integer
                          format: int64
                          example: 59120167
                          description: First tradeId
                          x-description-cn: 被归集的首个成交ID
                        l:
                          type: integer
                          format: int64
                          example: 59120170
                          description: Last tradeId
                          x-description-cn: 被归集的末个成交ID
                        T:
                          type: integer
                          format: int64
                          example: 1565877971222
                          description: Timestamp
                          x-description-cn: 成交时间
                        m:
                          type: boolean
                          example: true
                          description: Was the buyer the maker?
                          x-description-cn: 是否为主动卖出单
                        M:
                          type: boolean
                          example: true
                          description: Was the trade the best price match?
                          x-description-cn: 是否为最优撮合单(可忽略，目前总为最优撮合)
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 4
  /trades.historical:
    post:
      summary: Historical trades
      x-summary-cn: 历史交易
      description: Get historical trades.
      x-description-cn: 获取历史交易。
      tags:
        - market
      operationId: tradesHistorical
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#trades-historical
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tradesHistorical.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/trades_historical.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/trades_historical.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TradesHistoricalExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TradesHistorical/TradesHistorical.go
      x-ip-weight: 25
      x-security-type: NONE
      x-parameters-notes: |-
        **Data Source:** Database

        Notes:

        * If `fromId` is not specified, the most recent trades are returned.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        备注：

        * 如果 `fromId` 未指定，则返回最近的交易。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - trades.historical
                  example: trades.historical
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    fromId:
                      type: integer
                      format: int64
                      example: 1
                      description: Trade ID to begin at
                      x-description-cn: 起始交易ID
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: trades.historical
              params:
                symbol: BNBUSDT
                fromId: 1
                limit: 1
      responses:
        Successful Response:
          description: Historical trades
          x-description-cn: 历史交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: cffc9c7d-4efc-4ce0-b587-6b87448f052a
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          format: int64
                          example: 0
                        price:
                          type: string
                          example: "0.00005000"
                        qty:
                          type: string
                          example: "40.00000000"
                        quoteQty:
                          type: string
                          example: "0.00200000"
                        time:
                          type: integer
                          format: int64
                          example: 1500004800376
                        isBuyerMaker:
                          type: boolean
                          example: true
                        isBestMatch:
                          type: boolean
                          example: true
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 25
  /blockTrades.historical:
    post:
      summary: Historical Block Trades
      x-summary-cn: 查询历史大宗交易
      description: Get block trades.
      x-description-cn: 获取大宗交易记录。
      tags:
        - market
      operationId: blockTradesHistorical
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#block-trades-historical
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/blockTradesHistorical.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/block_trades_historical.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/block_trades_historical.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/BlockTradesHistoricalExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/BlockTradesHistorical/BlockTradesHistorical.go
      x-ip-weight: 25
      x-legacy-anchors:
        - historicalBlockTrades
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - blockTrades.historical
                  example: blockTrades.historical
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBBTC
                    fromId:
                      type: integer
                      format: int64
                      example: 582
                      description: Block trade ID to fetch from
                      x-description-cn: 从该大宗交易ID开始查询
                    limit:
                      type: integer
                      format: int64
                      example: 500
                      default: 500
                      maximum: 1000
                      description: "Default: 500; Maximum: 1000"
                      x-description-cn: "默认: 500; 最大: 1000"
                  additionalProperties: false
                  required:
                    - symbol
                    - fromId
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: blockTrades.historical
              params:
                symbol: BNBBTC
                fromId: 582
                limit: 500
      responses:
        Successful Response:
          description: Historical Block Trades
          x-description-cn: 历史大宗交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: cffc9c7d-4efc-4ce0-b587-6b87448f052a
                  status:
                    type: integer
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 582
                          format: int64
                        price:
                          type: string
                          example: "0.052"
                        qty:
                          type: string
                          example: "5838"
                        quoteQty:
                          type: string
                          example: "303.576"
                        time:
                          type: integer
                          example: 1772506983321
                          format: int64
                        isBuyerMaker:
                          type: boolean
                          example: true
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          example: 1
                        limit:
                          type: integer
                          example: 6000
                        count:
                          type: integer
                          example: 10
  /trades.recent:
    post:
      summary: Recent trades
      x-summary-cn: 最近的交易
      description: |-
        Get recent trades.

        If you need access to real-time trading activity, please consider using
        WebSocket Streams:

        * `<symbol>@trade`
      x-description-cn: |-
        获取最近的交易

        如果您需要访问实时交易活动，请考虑使用 WebSocket Streams：

        * `<symbol>@trade`
      tags:
        - market
      operationId: tradesRecent
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#trades-recent
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/tradesRecent.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/trades_recent.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/trades_recent.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/TradesRecentExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/TradesRecent/TradesRecent.go
      x-ip-weight: 25
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - trades.recent
                  example: trades.recent
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: trades.recent
              params:
                symbol: BNBUSDT
                limit: 1
      responses:
        Successful Response:
          description: Recent trades
          x-description-cn: 最近的交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 409a20bd-253d-41db-a6dd-687862a5882f
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          format: int64
                          example: 194686783
                        price:
                          type: string
                          example: "0.01361000"
                        qty:
                          type: string
                          example: "0.01400000"
                        quoteQty:
                          type: string
                          example: "0.00019054"
                        time:
                          type: integer
                          format: int64
                          example: 1660009530807
                        isBuyerMaker:
                          type: boolean
                          example: true
                        isBestMatch:
                          type: boolean
                          example: true
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 25
  /uiKlines:
    post:
      summary: UI Klines
      x-summary-cn: UI K线数据
      description: >-
        Get klines (candlestick bars) optimized for presentation.


        This request is similar to `klines`, having the same parameters and response. `uiKlines` return modified kline
        data, optimized for presentation of candlestick charts.
      x-description-cn: |-
        请求参数和响应字段与`k线`接口相同。
        uiKlines 是返回修改后的k线数据，针对k线图的呈现进行了优化。
      tags:
        - market
      operationId: uiKlines
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#ui-klines
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/uiKlines.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/ui_klines.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/ui_klines.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/UiKlinesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/UiKlines/UiKlines.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: |-
        **Data Source:** Database

        - If `startTime` and `endTime` are not sent, the most recent klines are returned.
        - Supported values for `timeZone`:
          - Hours and minutes (e.g. `-1:00`, `05:45`)
          - Only hours (e.g. `0`, `8`, `4`)
          - Accepted range is strictly [-12:00 to +14:00] inclusive
        - If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
        - Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        - 如果未发送 `startTime` 和 `endTime`，默认返回最近的交易。
        - `timeZone`支持的值包括：
            - 小时和分钟（例如 `-1:00`，`05:45`）
            - 仅小时（例如 `0`，`8`，`4`）
            - 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
        - 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
        - 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - uiKlines
                  example: uiKlines
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    interval:
                      type: string
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
                      example: 1s
                    startTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                    endTime:
                      type: integer
                      format: int64
                      example: 1735693200000
                    timeZone:
                      type: string
                      example: "0"
                      description: "Default: 0 (UTC)"
                      x-description-cn: 默认值： 0 (UTC)
                    limit:
                      type: integer
                      example: 1
                      default: 500
                      maximum: 1000
                  additionalProperties: false
                  required:
                    - symbol
                    - interval
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: uiKlines
              params:
                symbol: BNBUSDT
                interval: 1s
                startTime: 1735693200000
                endTime: 1735693200000
                timeZone: "0"
                limit: 1
      responses:
        Successful Response:
          description: UI Klines
          x-description-cn: UI K线数据
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: b137468a-fb20-4c06-bd6b-625148eec958
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: array
                      minItems: 12
                      maxItems: 12
                      x-prefixItems:
                        - type: integer
                          format: int64
                          description: Open time
                          x-description-cn: 开盘时间
                          example: 1499040000000
                        - type: string
                          description: Open
                          x-description-cn: 开盘价
                          example: "0.01634790"
                        - type: string
                          description: High
                          x-description-cn: 最高价
                          example: "0.80000000"
                        - type: string
                          description: Low
                          x-description-cn: 最低价
                          example: "0.01575800"
                        - type: string
                          description: Close
                          x-description-cn: 收盘价
                          example: "0.01577100"
                        - type: string
                          description: Volume
                          x-description-cn: 成交量
                          example: "148976.11427815"
                        - type: integer
                          format: int64
                          description: Close time
                          x-description-cn: 收盘时间
                          example: 1499644799999
                        - type: string
                          description: Quote asset volume
                          x-description-cn: 成交额
                          example: "2434.19055334"
                        - type: integer
                          description: Number of trades
                          x-description-cn: 成交笔数
                          example: 308
                        - type: string
                          description: Taker buy base asset volume
                          x-description-cn: 主动买入成交量
                          example: "1756.87402397"
                        - type: string
                          description: Taker buy quote asset volume
                          x-description-cn: 主动买入成交额
                          example: "28.46694368"
                        - type: string
                          description: Ignore
                          x-description-cn: 忽略字段
                          example: "0"
                      items:
                        oneOf:
                          - type: integer
                            format: int64
                            description: Open time
                            x-description-cn: 开盘时间
                            example: 1499040000000
                          - type: string
                            description: Open
                            x-description-cn: 开盘价
                            example: "0.01634790"
                          - type: string
                            description: High
                            x-description-cn: 最高价
                            example: "0.80000000"
                          - type: string
                            description: Low
                            x-description-cn: 最低价
                            example: "0.01575800"
                          - type: string
                            description: Close
                            x-description-cn: 收盘价
                            example: "0.01577100"
                          - type: string
                            description: Volume
                            x-description-cn: 成交量
                            example: "148976.11427815"
                          - type: integer
                            format: int64
                            description: Close time
                            x-description-cn: 收盘时间
                            example: 1499644799999
                          - type: string
                            description: Quote asset volume
                            x-description-cn: 成交额
                            example: "2434.19055334"
                          - type: integer
                            description: Number of trades
                            x-description-cn: 成交笔数
                            example: 308
                          - type: string
                            description: Taker buy base asset volume
                            x-description-cn: 主动买入成交量
                            example: "1756.87402397"
                          - type: string
                            description: Taker buy quote asset volume
                            x-description-cn: 主动买入成交额
                            example: "28.46694368"
                          - type: string
                            description: Ignore
                            x-description-cn: 忽略字段
                            example: "0"
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 2
  /referencePrice:
    post:
      summary: Query Reference Price
      x-summary-cn: 查询参考价格
      description: Query Reference Price
      x-description-cn: 查询参考价格
      tags:
        - market
      operationId: referencePrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#reference-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/referencePrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/reference_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/reference_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/ReferencePriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/ReferencePrice/ReferencePrice.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: |-
        **Data Source:** Memory

        If the symbol has never had a reference price set, the request is rejected with:

        ```json
        {
            "code": -2043,
            "msg": "This symbol doesn't have a reference price."
        }
        ```
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        如果该交易对从未设置过参考价格，则请求会被拒绝并返回：

        ```json
        {
            "code": -2043,
            "msg": "This symbol doesn't have a reference price."
        }
        ```
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - referencePrice
                  example: referencePrice
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BAZUSD
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: referencePrice
              params:
                symbol: BAZUSD
      responses:
        Successful Response:
          description: Query Reference Price
          x-description-cn: 查询参考价格
          content:
            application/json:
              schema:
                oneOf:
                  - description: "If a reference price is set:"
                    x-description-cn: 如果设置了参考价格：
                    type: object
                    properties:
                      id:
                        type: string
                        example: ddbfb65f-9ebf-42ec-8240-8f0f91de0867
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BAZUSD
                          referencePrice:
                            type: string
                            example: "0.00501900"
                          timestamp:
                            type: integer
                            format: int64
                            example: 1770946889251
                            description: Timestamp when the reference price was valid
                            x-description-cn: 参考价格生效的时间
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - description: "If no reference price is set:"
                    x-description-cn: 如果未设置参考价格：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 5132affb-0aba-4821-b475-f262504556b43
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BAZUSD
                          referencePrice:
                            example: null
                          timestamp:
                            type: integer
                            format: int64
                            description: Timestamp when the reference price was valid
                            x-description-cn: 参考价格生效的时间
                            example: 1770946889251
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - description: "If no reference price has ever been set:"
                    x-description-cn: 如果从未设置过参考价格：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 5132affa-0aba-4831-b475-f262504556b41
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2043
                          msg:
                            type: string
                            example: This symbol doesn't have a reference price.
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
  /referencePrice.calculation:
    post:
      summary: Query Reference Price Calculation
      x-summary-cn: 查询参考价格计算方式
      description: Query Reference Price Calculation
      x-description-cn: 查询参考价格计算方式
      tags:
        - market
      operationId: referencePriceCalculation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/market#reference-price-calculation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/MarketApi/referencePriceCalculation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/market_api/reference_price_calculation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Market/reference_price_calculation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/market/ReferencePriceCalculationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/MarketAPI/ReferencePriceCalculation/ReferencePriceCalculation.go
      x-ip-weight: 2
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - referencePrice.calculation
                  example: referencePrice.calculation
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BAZUSD
                    symbolStatus:
                      type: string
                      example: BAZUSD
                      enum:
                        - TRADING
                        - HALT
                        - BREAK
                        - CANCEL_ONLY
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: referencePrice.calculation
              params:
                symbol: BAZUSD
                symbolStatus: BAZUSD
      responses:
        Successful Response:
          description: Query Reference Price Calculation
          x-description-cn: 查询参考价格计算方式
          content:
            application/json:
              schema:
                oneOf:
                  - description: "If the reference price is being calculated by the matching engine as an arithmetic mean:"
                    x-description-cn: 如果参考价格由撮合引擎以算术平均数计算：
                    type: object
                    properties:
                      id:
                        type: string
                        example: ddbfb65f-9ebf-42ec-8240-8f0f91de0867
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BAZUSD
                          calculationType:
                            type: string
                            example: ARITHMETIC_MEAN
                          bucketCount:
                            type: integer
                            format: int64
                            example: 10
                            description: If the reference price is being calculated by the matching engine as an arithmetic mean
                            x-description-cn: 如果参考价格由撮合引擎以算术平均数计算
                          bucketWidthMs:
                            type: integer
                            format: int64
                            example: 1000
                            description: If the reference price is being calculated by the matching engine as an arithmetic mean
                            x-description-cn: 如果参考价格由撮合引擎以算术平均数计算
                          externalCalculationId:
                            type: integer
                            format: int64
                            example: 42
                            description: If the reference price is being calculated outside the matching engine
                            x-description-cn: 如果参考价格由撮合引擎外部计算
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
                  - description: "If the reference price is being calculated outside the matching engine:"
                    x-description-cn: 如果参考价格由撮合引擎外部计算：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 5132affa-0aba-4831-b475-f262504556b41
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BAZUSD
                          calculationType:
                            type: string
                            example: EXTERNAL
                          externalCalculationId:
                            type: integer
                            format: int64
                            description: If the reference price is being calculated outside the matching engine
                            x-description-cn: 如果参考价格由撮合引擎外部计算
                            example: 42
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 2
        Unsuccessful Response (400):
          description: The symbol does not have a reference price
          x-description-cn: 该交易对没有参考价格
          content:
            application/json:
              schema:
                description: "If reference price is not being calculated:"
                x-description-cn: 如果参考价格未被计算：
                type: object
                properties:
                  id:
                    type: string
                    example: 5132affa-0aba-4831-b475-f262504556b41
                  status:
                    type: integer
                    format: int64
                    example: 400
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                        format: int64
                        example: -2043
                      msg:
                        type: string
                        example: This symbol doesn't have a reference price.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 2
  /openOrders.cancelAll:
    post:
      summary: Cancel open orders (TRADE)
      x-summary-cn: 撤销单一交易对的所有挂单 (TRADE)
      description: |-
        Cancel all open orders on a symbol.
        This includes orders that are part of an order list.
      x-description-cn: 撤销单一交易对的所有挂单,包括交易组。
      tags:
        - trade
      operationId: openOrdersCancelAll
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#open-orders-cancel-all
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/openOrdersCancelAll.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/open_orders_cancel_all.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/open_orders_cancel_all.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OpenOrdersCancelAllExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OpenOrdersCancelAll/OpenOrdersCancelAll.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - openOrders.cancelAll
                  example: openOrders.cancelAll
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: openOrders.cancelAll
              params:
                symbol: BNBUSDT
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Cancel open orders
          x-description-cn: 撤销单一交易对的所有挂单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 778f938f-9041-4b88-9914-efbf64eeacc8
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        origClientOrderId: 4d96324ff9d44481926157
                        orderId: 12569099453
                        orderListId: -1
                        clientOrderId: 91fe37ce9e69c90d6358c0
                        transactTime: 1684804350068
                        price: "23416.10000000"
                        origQty: "0.00847000"
                        executedQty: "0.00001000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.23416100"
                        status: CANCELED
                        timeInForce: GTC
                        type: LIMIT
                        side: SELL
                        stopPrice: "0.00000000"
                        trailingDelta: 0
                        trailingTime: -1
                        icebergQty: "0.00000000"
                        strategyId: 37463720
                        strategyType: 1000000
                        selfTradePreventionMode: NONE
                      - orderListId: 19431
                        contingencyType: OCO
                        listStatusType: ALL_DONE
                        listOrderStatus: ALL_DONE
                        listClientOrderId: iuVNVJYYrByz6C4yGOPPK0
                        transactionTime: 1660803702431
                        symbol: BTCUSDT
                        orders:
                          - symbol: BTCUSDT
                            orderId: 12569099453
                            clientOrderId: bX5wROblo6YeDwa9iTLeyY
                          - symbol: BTCUSDT
                            orderId: 12569099454
                            clientOrderId: Tnu2IP0J5Y4mxw3IATBfmW
                        orderReports:
                          - symbol: BTCUSDT
                            origClientOrderId: bX5wROblo6YeDwa9iTLeyY
                            orderId: 12569099453
                            orderListId: 19431
                            clientOrderId: OFFXQtxVFZ6Nbcg4PgE2DA
                            transactTime: 1684804350068
                            price: "23450.50000000"
                            origQty: "0.00850000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: CANCELED
                            timeInForce: GTC
                            type: STOP_LOSS_LIMIT
                            side: BUY
                            stopPrice: "23430.00000000"
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            origClientOrderId: Tnu2IP0J5Y4mxw3IATBfmW
                            orderId: 12569099454
                            orderListId: 19431
                            clientOrderId: OFFXQtxVFZ6Nbcg4PgE2DA
                            transactTime: 1684804350068
                            price: "23400.00000000"
                            origQty: "0.00850000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: CANCELED
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: BUY
                            selfTradePreventionMode: NONE
                    items:
                      type: object
                      properties:
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                        contingencyType:
                          type: string
                          example: OCO
                        listStatusType:
                          type: string
                          example: ALL_DONE
                        listOrderStatus:
                          type: string
                          example: ALL_DONE
                        listClientOrderId:
                          type: string
                          example: iuVNVJYYrByz6C4yGOPPK0
                        transactionTime:
                          type: integer
                          format: int64
                          example: 1660803702431
                        symbol:
                          type: string
                          example: BTCUSDT
                        orders:
                          type: array
                          items:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTCUSDT
                              orderId:
                                type: integer
                                format: int64
                                example: 12569099453
                              clientOrderId:
                                type: string
                                example: bX5wROblo6YeDwa9iTLeyY
                        orderReports:
                          type: array
                          items:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTCUSDT
                              origClientOrderId:
                                type: string
                                example: bX5wROblo6YeDwa9iTLeyY
                              orderId:
                                type: integer
                                format: int64
                                example: 12569099453
                              orderListId:
                                type: integer
                                format: int64
                                example: 19431
                              clientOrderId:
                                type: string
                                example: OFFXQtxVFZ6Nbcg4PgE2DA
                              transactTime:
                                type: integer
                                format: int64
                                example: 1684804350068
                              price:
                                type: string
                                example: "23450.50000000"
                              origQty:
                                type: string
                                example: "0.00850000"
                              executedQty:
                                type: string
                                example: "0.00000000"
                              origQuoteOrderQty:
                                type: string
                                example: "0.000000"
                              cummulativeQuoteQty:
                                type: string
                                example: "0.00000000"
                              status:
                                type: string
                                example: CANCELED
                              timeInForce:
                                type: string
                                example: GTC
                              type:
                                type: string
                                example: STOP_LOSS_LIMIT
                              side:
                                type: string
                                example: BUY
                              selfTradePreventionMode:
                                type: string
                                example: NONE
                              icebergQty:
                                type: string
                                example: "0.00000000"
                                description: Appears only if the parameter icebergQty was sent in the request.
                                x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                              preventedMatchId:
                                type: integer
                                format: int64
                                example: 0
                                description: Appears only if the order expired due to STP.
                                x-description-cn: 仅在因 STP 导致订单失效时出现。
                              preventedQuantity:
                                type: string
                                example: "1.200000"
                                description: Order quantity that expired due to STP.
                                x-description-cn: 因 STP 导致订单失效的数量。
                              stopPrice:
                                type: string
                                example: "0.00000000"
                                description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                                x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                              strategyId:
                                type: integer
                                format: int64
                                example: 1
                                description: Appears only if the strategyId parameter was provided upon order placement.
                                x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                              strategyType:
                                type: integer
                                format: int64
                                example: 1000000
                                description: Appears only if the strategyType parameter was provided upon order placement.
                                x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                              trailingDelta:
                                type: integer
                                format: int64
                                example: 10
                                description: Delta price change required before order activation.
                                x-description-cn: 订单激活前所需的价格变动。
                              trailingTime:
                                type: integer
                                format: int64
                                example: -1
                                description: Time when the trailing order is now active and tracking price changes.
                                x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                              usedSor:
                                type: boolean
                                example: true
                                description: Field that determines whether order used SOR.
                                x-description-cn: 用于确定订单是否使用SOR的字段。
                              workingFloor:
                                type: string
                                example: SOR
                                description: Determines whether the order is being filled by the SOR or by the order book.
                                x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                              pegPriceType:
                                type: string
                                example: PRIMARY_PEG
                                description: Price peg type. Only for pegged orders.
                                x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                              pegOffsetType:
                                type: string
                                example: PRICE_LEVEL
                                description: Price peg offset type. Only for pegged orders, if requested.
                                x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                              pegOffsetValue:
                                type: integer
                                format: int64
                                example: 5
                                description: Price peg offset value. Only for pegged orders, if requested.
                                x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                              peggedPrice:
                                type: string
                                example: "87523.83710000"
                                description: Current price order is pegged at. Only for pegged orders, once determined.
                                x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                              expiryReason:
                                type: string
                                example: INSUFFICIENT_LIQUIDITY
                                description: Cause of the order's expiration. Appears when an order has expired.
                                x-description-cn: 订单过期的原因。当订单过期时出现。
                        origClientOrderId:
                          type: string
                          example: 4d96324ff9d44481926157
                        orderId:
                          type: integer
                          format: int64
                          example: 12569099453
                        clientOrderId:
                          type: string
                          example: 91fe37ce9e69c90d6358c0
                        transactTime:
                          type: integer
                          format: int64
                          example: 1684804350068
                        price:
                          type: string
                          example: "23416.10000000"
                        origQty:
                          type: string
                          example: "0.00847000"
                        executedQty:
                          type: string
                          example: "0.00001000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.000000"
                        cummulativeQuoteQty:
                          type: string
                          example: "0.23416100"
                        status:
                          type: string
                          example: CANCELED
                        timeInForce:
                          type: string
                          example: GTC
                        type:
                          type: string
                          example: LIMIT
                        side:
                          type: string
                          example: SELL
                        stopPrice:
                          type: string
                          example: "0.00000000"
                          description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                          x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                        trailingDelta:
                          type: integer
                          format: int64
                          example: 10
                          description: Delta price change required before order activation.
                          x-description-cn: 订单激活前所需的价格变动。
                        trailingTime:
                          type: integer
                          format: int64
                          example: -1
                          description: Time when the trailing order is now active and tracking price changes.
                          x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                        icebergQty:
                          type: string
                          example: "0.00000000"
                          description: Appears only if the parameter icebergQty was sent in the request.
                          x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                        strategyId:
                          type: integer
                          format: int64
                          example: 1
                          description: Appears only if the strategyId parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                        strategyType:
                          type: integer
                          format: int64
                          example: 1000000
                          description: Appears only if the strategyType parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                        selfTradePreventionMode:
                          type: string
                          example: NONE
                        preventedMatchId:
                          type: integer
                          format: int64
                          example: 0
                          description: Appears only if the order expired due to STP.
                          x-description-cn: 仅在因 STP 导致订单失效时出现。
                        preventedQuantity:
                          type: string
                          example: "1.200000"
                          description: Order quantity that expired due to STP.
                          x-description-cn: 因 STP 导致订单失效的数量。
                        usedSor:
                          type: boolean
                          example: true
                          description: Field that determines whether order used SOR.
                          x-description-cn: 用于确定订单是否使用SOR的字段。
                        workingFloor:
                          type: string
                          example: SOR
                          description: Determines whether the order is being filled by the SOR or by the order book.
                          x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                        pegPriceType:
                          type: string
                          example: PRIMARY_PEG
                          description: Price peg type. Only for pegged orders.
                          x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                        pegOffsetType:
                          type: string
                          example: PRICE_LEVEL
                          description: Price peg offset type. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                        pegOffsetValue:
                          type: integer
                          format: int64
                          example: 5
                          description: Price peg offset value. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                        peggedPrice:
                          type: string
                          example: "87523.83710000"
                          description: Current price order is pegged at. Only for pegged orders, once determined.
                          x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                        expiryReason:
                          type: string
                          example: INSUFFICIENT_LIQUIDITY
                          description: Cause of the order's expiration. Appears when an order has expired.
                          x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /order.amend.keepPriority:
    post:
      summary: Order Amend Keep Priority (TRADE)
      x-summary-cn: 修改订单并保留优先级 (TRADE)
      description: |-
        Reduce the quantity of an existing open order.

        This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

        Read [Order Amend Keep Priority FAQ](/products/spot/faqs/order_amend_keep_priority) to learn more.
      x-description-cn: |-
        由客户发送以减少其现有当前挂单的原始数量。

        这个请求会把0个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

        请阅读 [保留优先权的修改订单常见问题](/products/spot/faqs/order_amend_keep_priority) 了解更多信息。
      tags:
        - trade
      operationId: orderAmendKeepPriority
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-amend-keep-priority
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderAmendKeepPriority.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_amend_keep_priority.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_amend_keep_priority.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderAmendKeepPriorityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderAmendKeepPriority/OrderAmendKeepPriority.go
      x-ip-weight: 4
      x-order-weight: 0
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.amend.keepPriority
                  example: order.amend.keepPriority
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                      description: "`orderId` or `origClientOrderId` must be sent"
                      x-description-cn: 需提供 `orderId` 或 `origClientOrderId`。
                    origClientOrderId:
                      type: string
                      example: myOrder1
                      description: "`orderId` or `origClientOrderId` must be sent"
                      x-description-cn: 需提供 `orderId` 或 `origClientOrderId`。
                    newClientOrderId:
                      type: string
                      example: myOrder2
                      description: >-
                        The new client order ID for the order after being amended. <br> If not sent, one will be
                        randomly generated. <br> It is possible to reuse the current clientOrderId by sending it as the
                        `newClientOrderId`.
                      x-description-cn: >-
                        订单在被修改后被赋予的新 client order ID。 <br> 如果未发送则自动生成。 <br> 可以将当前 clientOrderId 作为 `newClientOrderId`
                        发送来重用当前 clientOrderId 的值。
                    newQty:
                      type: number
                      format: float
                      example: 5
                      description: "`newQty` must be greater than 0 and less than the order's quantity."
                      x-description-cn: 交易的新数量。 `newQty` 必须大于0, 但是必须比订单的原始数量小。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - newQty
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.amend.keepPriority
              params:
                symbol: BNBUSDT
                orderId: 1
                origClientOrderId: myOrder1
                newClientOrderId: myOrder2
                newQty: 5
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Order Amend Keep Priority
          x-description-cn: 修改订单并保留优先级
          content:
            application/json:
              schema:
                oneOf:
                  - description: "Response for a single order:"
                    x-description-cn: 来自单个订单的响应：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 56374a46-3061-486b-a311-89ee972eb648
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          transactTime:
                            type: integer
                            format: int64
                            example: 1741923284382
                          executionId:
                            type: integer
                            format: int64
                            example: 16
                          amendedOrder:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTCUSDT
                              orderId:
                                type: integer
                                format: int64
                                example: 12
                              orderListId:
                                type: integer
                                format: int64
                                example: -1
                              origClientOrderId:
                                type: string
                                example: my_test_order1
                              clientOrderId:
                                type: string
                                example: 4zR9HFcEq8gM1tWUqPEUHc
                              price:
                                type: string
                                example: "5.00000000"
                              qty:
                                type: string
                                example: "5.00000000"
                              executedQty:
                                type: string
                                example: "0.00000000"
                              preventedQty:
                                type: string
                                example: "0.00000000"
                              quoteOrderQty:
                                type: string
                                example: "0.00000000"
                              cumulativeQuoteQty:
                                type: string
                                example: "0.00000000"
                              status:
                                type: string
                                example: NEW
                              timeInForce:
                                type: string
                                example: GTC
                              type:
                                type: string
                                example: LIMIT
                              side:
                                type: string
                                example: BUY
                              workingTime:
                                type: integer
                                format: int64
                                example: 1741923284364
                              selfTradePreventionMode:
                                type: string
                                example: NONE
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
                  - description: "Response for an order which is part of an Order list:"
                    x-description-cn: 来自订单列表中单个订单的响应：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 56374b46-3061-486b-a311-89ee972eb648
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          transactTime:
                            type: integer
                            format: int64
                            example: 1741924229819
                          executionId:
                            type: integer
                            format: int64
                            example: 60
                          amendedOrder:
                            type: object
                            properties:
                              symbol:
                                type: string
                                example: BTUCSDT
                              orderId:
                                type: integer
                                format: int64
                                example: 23
                              orderListId:
                                type: integer
                                format: int64
                                example: 4
                              origClientOrderId:
                                type: string
                                example: my_pending_order
                              clientOrderId:
                                type: string
                                example: xbxXh5SSwaHS7oUEOCI88B
                              price:
                                type: string
                                example: "1.00000000"
                              qty:
                                type: string
                                example: "5.00000000"
                              executedQty:
                                type: string
                                example: "0.00000000"
                              preventedQty:
                                type: string
                                example: "0.00000000"
                              quoteOrderQty:
                                type: string
                                example: "0.00000000"
                              cumulativeQuoteQty:
                                type: string
                                example: "0.00000000"
                              status:
                                type: string
                                example: NEW
                              timeInForce:
                                type: string
                                example: GTC
                              type:
                                type: string
                                example: LIMIT
                              side:
                                type: string
                                example: BUY
                              workingTime:
                                type: integer
                                format: int64
                                example: 1741924204920
                              selfTradePreventionMode:
                                type: string
                                example: NONE
                              icebergQty:
                                type: string
                                example: "0.00000000"
                                description: Appears only if the parameter icebergQty was sent in the request.
                                x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                              preventedMatchId:
                                type: integer
                                format: int64
                                example: 0
                                description: Appears only if the order expired due to STP.
                                x-description-cn: 仅在因 STP 导致订单失效时出现。
                              preventedQuantity:
                                type: string
                                example: "1.200000"
                                description: Order quantity that expired due to STP.
                                x-description-cn: 因 STP 导致订单失效的数量。
                              stopPrice:
                                type: string
                                example: "0.00000000"
                                description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                                x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                              strategyId:
                                type: integer
                                format: int64
                                example: 1
                                description: Appears only if the strategyId parameter was provided upon order placement.
                                x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                              strategyType:
                                type: integer
                                format: int64
                                example: 1000000
                                description: Appears only if the strategyType parameter was provided upon order placement.
                                x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                              trailingDelta:
                                type: integer
                                format: int64
                                example: 10
                                description: Delta price change required before order activation.
                                x-description-cn: 订单激活前所需的价格变动。
                              trailingTime:
                                type: integer
                                format: int64
                                example: -1
                                description: Time when the trailing order is now active and tracking price changes.
                                x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                              usedSor:
                                type: boolean
                                example: true
                                description: Field that determines whether order used SOR.
                                x-description-cn: 用于确定订单是否使用SOR的字段。
                              workingFloor:
                                type: string
                                example: SOR
                                description: Determines whether the order is being filled by the SOR or by the order book.
                                x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                              pegPriceType:
                                type: string
                                example: PRIMARY_PEG
                                description: Price peg type. Only for pegged orders.
                                x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                              pegOffsetType:
                                type: string
                                example: PRICE_LEVEL
                                description: Price peg offset type. Only for pegged orders, if requested.
                                x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                              pegOffsetValue:
                                type: integer
                                format: int64
                                example: 5
                                description: Price peg offset value. Only for pegged orders, if requested.
                                x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                              peggedPrice:
                                type: string
                                example: "87523.83710000"
                                description: Current price order is pegged at. Only for pegged orders, once determined.
                                x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                              expiryReason:
                                type: string
                                example: INSUFFICIENT_LIQUIDITY
                                description: Cause of the order's expiration. Appears when an order has expired.
                                x-description-cn: 订单过期的原因。当订单过期时出现。
                          listStatus:
                            type: object
                            properties:
                              orderListId:
                                type: integer
                                format: int64
                                example: 4
                              contingencyType:
                                type: string
                                example: OTO
                              listOrderStatus:
                                type: string
                                example: EXECUTING
                              listClientOrderId:
                                type: string
                                example: 8nOGLLawudj1QoOiwbroRH
                              symbol:
                                type: string
                                example: BTCUSDT
                              orders:
                                type: array
                                example:
                                  - symbol: BTCUSDT
                                    orderId: 22
                                    clientOrderId: g04EWsjaackzedjC9wRkWD
                                  - symbol: BTCUSDT
                                    orderId: 23
                                    clientOrderId: xbxXh5SSwaHS7oUEOCI88B
                                items:
                                  type: object
                                  properties:
                                    symbol:
                                      type: string
                                      example: BTCUSDT
                                    orderId:
                                      type: integer
                                      format: int64
                                      example: 22
                                    clientOrderId:
                                      type: string
                                      example: g04EWsjaackzedjC9wRkWD
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 4
  /order.cancel:
    post:
      summary: Cancel order (TRADE)
      x-summary-cn: 撤销订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 取消有效订单。
      tags:
        - trade
      operationId: orderCancel
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-cancel
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderCancel.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_cancel.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_cancel.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderCancelExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderCancel/OrderCancel.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        Notes:


        * If both `orderId` and `origClientOrderId` parameters are provided, the `orderId` is searched first, then the
        `origClientOrderId` from that result is checked against that order. If both conditions are not met the request
        will be rejected.


        * `newClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.


        * If you cancel an order that is a part of an order list, the entire order list is canceled.


        * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when
        only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        备注：


        * 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId`
        的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。


        * `newClientOrderId` 将替换已取消订单的 `clientOrderId`，为新订单腾出空间。


        * 如果您取消属于订单列表的订单，则整个订单列表将被取消。


        * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` +
        `origClientOrderId` 会稍慢。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.cancel
                  example: order.cancel
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                    origClientOrderId:
                      type: string
                      example: myOrder1
                    newClientOrderId:
                      type: string
                      example: cancelMyOrder1
                      description: Used to uniquely identify this cancel. Automatically generated by default.
                      x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
                    cancelRestrictions:
                      type: string
                      enum:
                        - ONLY_NEW
                        - ONLY_PARTIALLY_FILLED
                      example: ONLY_NEW
                      description: >-
                        Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br>
                        `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more
                        information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).
                      x-description-cn: >-
                        支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为
                        `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.cancel
              params:
                symbol: BNBUSDT
                orderId: 1
                origClientOrderId: myOrder1
                newClientOrderId: cancelMyOrder1
                cancelRestrictions: ONLY_NEW
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).


        <a id="regarding-cancelrestrictions"></a>


        **Regarding `cancelRestrictions`**


        * If the `cancelRestrictions` value is not any of the supported values, the error will be:

        ```json

        {
            "code": -1145,
            "msg": "Invalid cancelRestrictions"
        }

        ```

        * If the order did not pass the conditions for `cancelRestrictions`, the error will be:

        ```json

        {
            "code": -2011,
            "msg": "Order was not canceled due to cancel restrictions."
        }

        ```
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。


        <a id="regarding-cancelrestrictions"></a>


        **关于 `cancelRestrictions`**


        * 如果 `cancelRestrictions` 值不是任何受支持的值，则错误将是：

        ```json

        {
            "code": -1145,
            "msg": "Invalid cancelRestrictions"
        }

        ```

        * 如果订单没有通过 `cancelRestrictions` 的条件，错误将是：

        ```json

        {
            "code": -2011,
            "msg": "Order was not canceled due to cancel restrictions."
        }

        ```
      responses:
        Successful Response:
          description: Cancel order
          x-description-cn: 撤销订单
          content:
            application/json:
              schema:
                oneOf:
                  - description: "When an individual order is canceled:"
                    x-description-cn: 取消单个订单时：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 5633b6a2-90a9-4192-83e7-925c90b6a2fd
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          origClientOrderId:
                            type: string
                            description: clientOrderId that was canceled
                            x-description-cn: 被取消的 clientOrderId
                            example: 4d96324ff9d44481926157
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            description: set only for legs of an order list
                            x-description-cn: 订单列表的ID，不然就是 -1
                            example: -1
                          clientOrderId:
                            type: string
                            description: newClientOrderId from request
                            x-description-cn: 请求的 newClientOrderId
                            example: 91fe37ce9e69c90d6358c0
                          transactTime:
                            type: integer
                            format: int64
                            example: 1684804350068
                          price:
                            type: string
                            example: "23416.10000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00001000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "0.23416100"
                          status:
                            type: string
                            example: CANCELED
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          stopPrice:
                            type: string
                            description: present only if stopPrice set for the order
                            x-description-cn: 如果订单设置了 stopPrice 会出现
                            example: "0.00000000"
                          trailingDelta:
                            type: integer
                            format: int64
                            description: present only if trailingDelta set for the order
                            x-description-cn: 如果订单设置了 trailingDelta 会出现
                            example: 0
                          icebergQty:
                            type: string
                            description: present only if icebergQty set for the order
                            x-description-cn: 如果订单设置了 icebergQty 会出现
                            example: "0.00000000"
                          strategyId:
                            type: integer
                            format: int64
                            description: present only if strategyId set for the order
                            x-description-cn: 如果订单设置了 strategyId 会出现
                            example: 37463720
                          strategyType:
                            type: integer
                            format: int64
                            description: present only if strategyType set for the order
                            x-description-cn: 如果订单设置了 strategyType 会出现
                            example: 1000000
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
                  - description: "When an order list is canceled:"
                    x-description-cn: 取消订单列表时：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 16eaf097-bbec-44b9-96ff-e97e6e875870
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          origClientOrderId:
                            type: string
                            example: 4d96324ff9d44481926157
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            example: 19431
                          clientOrderId:
                            type: string
                            example: 91fe37ce9e69c90d6358c0
                          transactTime:
                            type: integer
                            format: int64
                            example: 1684804350068
                          price:
                            type: string
                            example: "23416.10000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00001000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "0.23416100"
                          status:
                            type: string
                            example: CANCELED
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          stopPrice:
                            type: string
                            example: "0.00000000"
                            description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                            x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                          trailingDelta:
                            type: integer
                            format: int64
                            example: 10
                            description: Delta price change required before order activation.
                            x-description-cn: 订单激活前所需的价格变动。
                          icebergQty:
                            type: string
                            example: "0.00000000"
                            description: Appears only if the parameter icebergQty was sent in the request.
                            x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                          strategyId:
                            type: integer
                            format: int64
                            example: 1
                            description: Appears only if the strategyId parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                          strategyType:
                            type: integer
                            format: int64
                            example: 1000000
                            description: Appears only if the strategyType parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                          preventedMatchId:
                            type: integer
                            format: int64
                            example: 0
                            description: Appears only if the order expired due to STP.
                            x-description-cn: 仅在因 STP 导致订单失效时出现。
                          preventedQuantity:
                            type: string
                            example: "1.200000"
                            description: Order quantity that expired due to STP.
                            x-description-cn: 因 STP 导致订单失效的数量。
                          trailingTime:
                            type: integer
                            format: int64
                            example: -1
                            description: Time when the trailing order is now active and tracking price changes.
                            x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                          usedSor:
                            type: boolean
                            example: true
                            description: Field that determines whether order used SOR.
                            x-description-cn: 用于确定订单是否使用SOR的字段。
                          workingFloor:
                            type: string
                            example: SOR
                            description: Determines whether the order is being filled by the SOR or by the order book.
                            x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                          pegPriceType:
                            type: string
                            example: PRIMARY_PEG
                            description: Price peg type. Only for pegged orders.
                            x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                          pegOffsetType:
                            type: string
                            example: PRICE_LEVEL
                            description: Price peg offset type. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                          pegOffsetValue:
                            type: integer
                            format: int64
                            example: 5
                            description: Price peg offset value. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                          peggedPrice:
                            type: string
                            example: "87523.83710000"
                            description: Current price order is pegged at. Only for pegged orders, once determined.
                            x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                          expiryReason:
                            type: string
                            example: INSUFFICIENT_LIQUIDITY
                            description: Cause of the order's expiration. Appears when an order has expired.
                            x-description-cn: 订单过期的原因。当订单过期时出现。
                          contingencyType:
                            type: string
                            example: OCO
                          listStatusType:
                            type: string
                            example: ALL_DONE
                          listOrderStatus:
                            type: string
                            example: ALL_DONE
                          listClientOrderId:
                            type: string
                            example: iuVNVJYYrByz6C4yGOPPK0
                          transactionTime:
                            type: integer
                            format: int64
                            example: 1660803702431
                          orders:
                            type: array
                            example:
                              - symbol: BTCUSDT
                                orderId: 12569099453
                                clientOrderId: bX5wROblo6YeDwa9iTLeyY
                              - symbol: BTCUSDT
                                orderId: 12569099454
                                clientOrderId: Tnu2IP0J5Y4mxw3IATBfmW
                            items:
                              type: object
                              properties:
                                symbol:
                                  type: string
                                  example: BTCUSDT
                                orderId:
                                  type: integer
                                  format: int64
                                  example: 12569099453
                                clientOrderId:
                                  type: string
                                  example: bX5wROblo6YeDwa9iTLeyY
                          orderReports:
                            type: array
                            description: order list order's status format is the same as for individual orders.
                            x-description-cn: 订单列表的状态格式与单个订单相同。
                            example:
                              - symbol: BTCUSDT
                                origClientOrderId: bX5wROblo6YeDwa9iTLeyY
                                orderId: 12569099453
                                orderListId: 19431
                                clientOrderId: OFFXQtxVFZ6Nbcg4PgE2DA
                                transactTime: 1684804350068
                                price: "23450.50000000"
                                origQty: "0.00850000"
                                executedQty: "0.00000000"
                                origQuoteOrderQty: "0.000000"
                                cummulativeQuoteQty: "0.00000000"
                                status: CANCELED
                                timeInForce: GTC
                                type: STOP_LOSS_LIMIT
                                side: BUY
                                stopPrice: "23430.00000000"
                                selfTradePreventionMode: NONE
                              - symbol: BTCUSDT
                                origClientOrderId: Tnu2IP0J5Y4mxw3IATBfmW
                                orderId: 12569099454
                                orderListId: 19431
                                clientOrderId: OFFXQtxVFZ6Nbcg4PgE2DA
                                transactTime: 1684804350068
                                price: "23400.00000000"
                                origQty: "0.00850000"
                                executedQty: "0.00000000"
                                origQuoteOrderQty: "0.000000"
                                cummulativeQuoteQty: "0.00000000"
                                status: CANCELED
                                timeInForce: GTC
                                type: LIMIT_MAKER
                                side: BUY
                                selfTradePreventionMode: NONE
                            items:
                              type: object
                              properties:
                                symbol:
                                  type: string
                                  example: BTCUSDT
                                origClientOrderId:
                                  type: string
                                  example: bX5wROblo6YeDwa9iTLeyY
                                orderId:
                                  type: integer
                                  format: int64
                                  example: 12569099453
                                orderListId:
                                  type: integer
                                  format: int64
                                  example: 19431
                                clientOrderId:
                                  type: string
                                  example: OFFXQtxVFZ6Nbcg4PgE2DA
                                transactTime:
                                  type: integer
                                  format: int64
                                  example: 1684804350068
                                price:
                                  type: string
                                  example: "23450.50000000"
                                origQty:
                                  type: string
                                  example: "0.00850000"
                                executedQty:
                                  type: string
                                  example: "0.00000000"
                                origQuoteOrderQty:
                                  type: string
                                  example: "0.000000"
                                cummulativeQuoteQty:
                                  type: string
                                  example: "0.00000000"
                                status:
                                  type: string
                                  example: CANCELED
                                timeInForce:
                                  type: string
                                  example: GTC
                                type:
                                  type: string
                                  example: STOP_LOSS_LIMIT
                                side:
                                  type: string
                                  example: BUY
                                selfTradePreventionMode:
                                  type: string
                                  example: NONE
                                icebergQty:
                                  type: string
                                  example: "0.00000000"
                                  description: Appears only if the parameter icebergQty was sent in the request.
                                  x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                                preventedMatchId:
                                  type: integer
                                  format: int64
                                  example: 0
                                  description: Appears only if the order expired due to STP.
                                  x-description-cn: 仅在因 STP 导致订单失效时出现。
                                preventedQuantity:
                                  type: string
                                  example: "1.200000"
                                  description: Order quantity that expired due to STP.
                                  x-description-cn: 因 STP 导致订单失效的数量。
                                stopPrice:
                                  type: string
                                  example: "0.00000000"
                                  description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                                  x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                                strategyId:
                                  type: integer
                                  format: int64
                                  example: 1
                                  description: Appears only if the strategyId parameter was provided upon order placement.
                                  x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                                strategyType:
                                  type: integer
                                  format: int64
                                  example: 1000000
                                  description: Appears only if the strategyType parameter was provided upon order placement.
                                  x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                                trailingDelta:
                                  type: integer
                                  format: int64
                                  example: 10
                                  description: Delta price change required before order activation.
                                  x-description-cn: 订单激活前所需的价格变动。
                                trailingTime:
                                  type: integer
                                  format: int64
                                  example: -1
                                  description: Time when the trailing order is now active and tracking price changes.
                                  x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                                usedSor:
                                  type: boolean
                                  example: true
                                  description: Field that determines whether order used SOR.
                                  x-description-cn: 用于确定订单是否使用SOR的字段。
                                workingFloor:
                                  type: string
                                  example: SOR
                                  description: Determines whether the order is being filled by the SOR or by the order book.
                                  x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                                pegPriceType:
                                  type: string
                                  example: PRIMARY_PEG
                                  description: Price peg type. Only for pegged orders.
                                  x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                                pegOffsetType:
                                  type: string
                                  example: PRICE_LEVEL
                                  description: Price peg offset type. Only for pegged orders, if requested.
                                  x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                                pegOffsetValue:
                                  type: integer
                                  format: int64
                                  example: 5
                                  description: Price peg offset value. Only for pegged orders, if requested.
                                  x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                                peggedPrice:
                                  type: string
                                  example: "87523.83710000"
                                  description: Current price order is pegged at. Only for pegged orders, once determined.
                                  x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                                expiryReason:
                                  type: string
                                  example: INSUFFICIENT_LIQUIDITY
                                  description: Cause of the order's expiration. Appears when an order has expired.
                                  x-description-cn: 订单过期的原因。当订单过期时出现。
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
  /order.cancelReplace:
    post:
      summary: Cancel and replace order (TRADE)
      x-summary-cn: 撤消挂单再下单 (TRADE)
      description: >-
        * Cancel an existing order and immediately place a new order instead of the canceled one.

        * A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the
        unfilled order count by 1.

        * You can only cancel an individual order from an orderList using this method, but the result is the same as
        canceling the entire orderList.
      x-description-cn: |-
        * 撤消一个现有订单，并立即重新下单。
        * 即使新订单未被尝试（即 `newOrderResult: NOT_ATTEMPTED`），未成交订单数量仍会增加1。
        * 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。
      tags:
        - trade
      operationId: orderCancelReplace
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-cancel-replace
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderCancelReplace.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_cancel_replace.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_cancel_replace.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderCancelReplaceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderCancelReplace/OrderCancelReplace.go
      x-ip-weight: 1
      x-order-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        Similar to the [`order.place`](/catalog/core-trading-spot-trading/api/ws-api/trade#order-place) request,

        additional mandatory parameters (*) are determined by the new order `type`.


        Available `cancelReplaceMode` options:


        * `STOP_ON_FAILURE` – if cancellation request fails, new order placement will not be attempted.

        * `ALLOW_FAILURE` – new order placement will be attempted even if the cancel request fails.


        <table>

        <thead>
            <tr>
                <th colspan=3 align=left>Request</th>
                <th colspan=3 align=left>Response</th>
            </tr>
            <tr>
                <th><code>cancelReplaceMode</code></th>
                <th><code>orderRateLimitExceededMode</code></th>
                <th>Unfilled Order Count</th>
                <th><code>cancelResult</code></th>
                <th><code>newOrderResult</code></th>
                <th><code>status</code></th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td rowspan="11"><code>STOP_ON_FAILURE</code></td>
                <td rowspan="6"><code>DO_NOTHING</code></td>
                <td rowspan="3">Within Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="3">Exceeds Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td rowspan="5"><code>CANCEL_ONLY</code></td>
                <td rowspan="3">Within Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="2">Exceeds Limits</td>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>429</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>429</code></td>
            </tr>
            <tr>
                <td rowspan="16"><code>ALLOW_FAILURE</code></td>
                <td rowspan="8"><code>DO_NOTHING</code></td>
                <td rowspan="4">Within Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
            <td rowspan="4">Exceeds Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td rowspan="8"><CODE>CANCEL_ONLY</CODE></td>
                <td rowspan="4">Within Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="4">Exceeds Limits</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
        </tbody>

        </table>


        Notes:


        * If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched
        first, then the `cancelOrigClientOrderId` from that result is checked against that order. If both conditions are
        not met the request will be rejected.


        * `cancelNewClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.


        * `newClientOrderId` specifies `clientOrderId` value for the placed order.

          A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

          The new order can reuse old `clientOrderId` of the canceled order.

        * This cancel-replace operation is **not transactional**.

          If one operation succeeds but the other one fails, the successful operation is still executed.

          For example, in `STOP_ON_FAILURE` mode, if the new order placement fails, the old order is still canceled.

        * Filters and order count limits are evaluated before cancellation and order placement occurs.


        * If new order placement is not attempted, your order count is still incremented.


        * Like [`order.cancel`](#order-cancel), if you cancel an individual order from an order list, the entire order
        list is canceled.


        * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when
        only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        类似于 [`order.place`](/catalog/core-trading-spot-trading/api/ws-api/trade#order-place) 请求，额外的强制参数 (*) 由新订单的 `type`
        确定。


        可用的 `cancelReplaceMode` 选项：


        * `STOP_ON_FAILURE` – 如果撤销订单请求失败，将不会尝试下新订单。

        * `ALLOW_FAILURE` – 即使撤销订单请求失败，也会尝试下新订单。


        <table>

        <thead>
            <tr>
                <th colspan=3 align=left>请求</th>
                <th colspan=3 align=left>响应</th>
            </tr>
            <tr>
                <th><code>cancelReplaceMode</code></th>
                <th><code>orderRateLimitExceededMode</code></th>
                <th>未成交订单数</th>
                <th><code>cancelResult</code></th>
                <th><code>newOrderResult</code></th>
                <th><code>status</code></th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td rowspan="11"><code>STOP_ON_FAILURE</code></td>
                <td rowspan="6"><code>DO_NOTHING</code></td>
                <td rowspan="3">在限制范围内</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="3">超出限制范围</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td rowspan="5"><code>CANCEL_ONLY</code></td>
                <td rowspan="3">在限制范围内</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="2">超出限制范围</td>
                <td>❌ <code>FAILURE</code></td>
                <td>➖ <code>NOT_ATTEMPTED</code></td>
                <td align=right><code>429</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>429</code></td>
            </tr>
            <tr>
                <td rowspan="16"><code>ALLOW_FAILURE</code></td>
                <td rowspan="8"><code>DO_NOTHING</code></td>
                <td rowspan="4">在限制范围内</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
            <td rowspan="4">超出限制范围</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td rowspan="8"><CODE>CANCEL_ONLY</CODE></td>
                <td rowspan="4">在限制范围内</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
            <tr>
                <td rowspan="4">超出限制范围</td>
                <td>✅ <code>SUCCESS</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right><code>200</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>400</code></td>
            </tr>
            <tr>
                <td>❌ <code>FAILURE</code></td>
                <td>✅ <code>SUCCESS</code></td>
                <td align=right>N/A</td>
            </tr>
            <tr>
                <td>✅ <code>SUCCESS</code></td>
                <td>❌ <code>FAILURE</code></td>
                <td align=right><code>409</code></td>
            </tr>
        </tbody>

        </table>


        备注：


        * 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。然后， 查找结果中的
        `cancelOrigClientOrderId` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。


        * `cancelNewClientOrderId` 将替换已撤销订单的 `clientOrderId`，为新订单腾出空间。


        * `newClientOrderId` 指定下单的 `clientOrderId` 值。

          仅当前一个订单已成交或过期时，才会接受具有相同 `clientOrderId` 的新订单。

          新订单可以重用已取消订单的旧 `clientOrderId`。

        * 此 cancel-replace 操作**不是事务性的**。

          如果一个操作成功但另一个操作失败，则仍然执行成功的操作。

          例如，在 `STOP_ON_FAILURE` 模式下，如果下新订单达失败，旧订单仍然被撤销。

        * 过滤器和订单次数限制会在撤销和下订单之前评估。


        * 如果未尝试下新订单，订单次数仍会增加。


        * 与 [`order.cancel`](#order-cancel) 一样，如果您撤销订单列表内的某个订单，则整个订单列表将被撤销。


        * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` +
        `origClientOrderId` 会稍慢。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.cancelReplace
                  example: order.cancelReplace
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    cancelReplaceMode:
                      type: string
                      enum:
                        - STOP_ON_FAILURE
                        - ALLOW_FAILURE
                      example: STOP_ON_FAILURE
                      description: >-
                        The allowed values are: <br/> `STOP_ON_FAILURE` - If the cancel request fails, the new order
                        placement will not be attempted. <br/> `ALLOW_FAILURE` - new order placement will be attempted
                        even if cancel request fails.
                      x-description-cn: 指定类型：`STOP_ON_FAILURE` - 如果撤消订单失败将不会继续重新下单。<br/> `ALLOW_FAILURE` - 不管撤消订单是否成功都会继续重新下单。
                    cancelOrderId:
                      type: integer
                      format: int64
                      example: 1
                      description: >-
                        Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br>If both
                        `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is
                        searched first, then the `cancelOrigClientOrderId` from that result is checked against that
                        order. <br></br>If both conditions are not met the request will be rejected.
                      x-description-cn: >-
                        必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和
                        `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的
                        `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。
                    cancelOrigClientOrderId:
                      type: string
                      example: myOrder1
                      description: >-
                        Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br> If both
                        `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is
                        searched first, then the `cancelOrigClientOrderId` from that result is checked against that
                        order. <br></br> If both conditions are not met the request will be rejected.
                      x-description-cn: >-
                        必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和
                        `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的
                        `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。
                    cancelNewClientOrderId:
                      type: string
                      example: cancelMyOrder1
                      description: Used to uniquely identify this cancel. Automatically generated by default.
                      x-description-cn: 用户自定义的id，如空缺系统会自动赋值
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: Please see [Enums](/products/spot/enums#side) for supported values.
                      x-description-cn: 详见枚举定义：[订单方向](/products/spot/enums#side)
                    type:
                      type: string
                      enum:
                        - MARKET
                        - LIMIT
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                        - LIMIT_MAKER
                      example: MARKET
                      description: Please see [Enums](/products/spot/enums#ordertypes) for supported values.
                      x-description-cn: 详见枚举定义：[订单类型](/products/spot/enums#ordertypes)
                    timeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Please see [Enums](/products/spot/enums#timeinforce) for supported values.
                      x-description-cn: 详见枚举定义：[生效时间](/products/spot/enums#timeinforce)
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    quoteOrderQty:
                      type: number
                      format: float
                      example: 1
                    newClientOrderId:
                      type: string
                      example: myOrder2
                      description: Used to identify the new order.
                      x-description-cn: 用于辨识新订单。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Allowed values: <br/> `ACK`, `RESULT`, `FULL` <br/> `MARKET` and `LIMIT` orders types default to
                        `FULL`; all other orders default to `ACK`
                      x-description-cn: "指定响应类型: <br/> 指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`， 其他默认为`ACK`。"
                    stopPrice:
                      type: number
                      format: float
                      example: 1
                      description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                      x-description-cn: 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。
                    trailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 参考 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    icebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
                      x-description-cn: 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                    strategyId:
                      type: integer
                      format: int64
                      example: 1
                    strategyType:
                      type: integer
                      example: 1
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 不能低于 `1000000`。
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. The possible supported
                        values are: [STP Modes](/products/spot/enums#stpmodes).
                      x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                    cancelRestrictions:
                      type: string
                      enum:
                        - ONLY_NEW
                        - ONLY_PARTIALLY_FILLED
                      example: ONLY_NEW
                      description: >-
                        Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br>
                        `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more
                        information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).
                      x-description-cn: >-
                        支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为
                        `PARTIALLY_FILLED`，撤销将成功。 请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。
                    orderRateLimitExceededMode:
                      type: string
                      enum:
                        - DO_NOTHING
                        - CANCEL_ONLY
                      example: DO_NOTHING
                      description: >-
                        Supported values: <br> `DO_NOTHING` (default)- will only attempt to cancel the order if account
                        has not exceeded the unfilled order rate limit<br> `CANCEL_ONLY` - will always cancel the order
                      x-description-cn: 支持的值： <br></br> `DO_NOTHING`（默认值）- 仅在账户未超过未成交订单频率限制时，会尝试取消订单。<br></br> `CANCEL_ONLY` - 将始终取消订单。
                    pegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: "`PRIMARY_PEG` or `MARKET_PEG` <br> See Pegged Orders"
                      x-description-cn: "`PRIMARY_PEG` 或 `MARKET_PEG`。 <br> 参阅 关于挂钩订单参数的注意事项"
                    pegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                      description: "Price level to peg the price to (max: 100) <br> See Pegged Orders"
                      x-description-cn: 用于挂钩的价格水平（最大值：100）。 <br> 参阅 关于挂钩订单参数的注意事项
                    pegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                      description: Only `PRICE_LEVEL` is supported <br> See Pegged Orders
                      x-description-cn: 仅支持 `PRICE_LEVEL`。 <br> 参阅 关于挂钩订单参数的注意事项
                    quoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        For replacement orders on the BUY side only. Maximum quote-asset notional the replacement order
                        may consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 仅适用于买单方向的新订单。新订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - cancelReplaceMode
                    - side
                    - type
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.cancelReplace
              params:
                symbol: BNBUSDT
                cancelReplaceMode: STOP_ON_FAILURE
                cancelOrderId: 1
                cancelOrigClientOrderId: myOrder1
                cancelNewClientOrderId: cancelMyOrder1
                side: BUY
                type: MARKET
                timeInForce: GTC
                price: 1
                quantity: 1
                quoteOrderQty: 1
                newClientOrderId: myOrder2
                newOrderRespType: ACK
                stopPrice: 1
                trailingDelta: 1
                icebergQty: 1
                strategyId: 1
                strategyType: 1
                selfTradePreventionMode: NONE
                cancelRestrictions: ONLY_NEW
                orderRateLimitExceededMode: DO_NOTHING
                pegPriceType: PRIMARY_PEG
                pegOffsetValue: 1
                pegOffsetType: PRICE_LEVEL
                quoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Cancel and replace order
          x-description-cn: 撤消挂单再下单
          content:
            application/json:
              schema:
                description: 'If both cancel and placement succeed, you get the following response with `"status": 200`:'
                x-description-cn: '如果撤销订单和下新订单都成功，响应会是 `"status": 200`：'
                type: object
                properties:
                  id:
                    type: string
                    example: 99de1036-b5e2-4e0f-9b5c-13d751c93a1a
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      cancelResult:
                        type: string
                        example: SUCCESS
                      newOrderResult:
                        type: string
                        example: SUCCESS
                      cancelResponse:
                        type: object
                        description: |-
                          Format is identical to "order.cancel" format.
                          Some fields are optional and are included only for orders that set them.
                        x-description-cn: |-
                          格式与 "order.cancel" 格式相同。
                          某些字段是可选的，仅在订单中有设置它们时才包括。
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          origClientOrderId:
                            type: string
                            example: 4d96324ff9d44481926157
                            description: cancelOrigClientOrderId from request
                            x-description-cn: 请求的 cancelOrigClientOrderId
                          orderId:
                            type: integer
                            format: int64
                            example: 125690984230
                          orderListId:
                            type: integer
                            format: int64
                            example: -1
                          clientOrderId:
                            type: string
                            example: 91fe37ce9e69c90d6358c0
                            description: cancelNewClientOrderId from request
                            x-description-cn: 请求的 cancelNewClientOrderId
                          transactTime:
                            type: integer
                            format: int64
                            example: 1684804350068
                          price:
                            type: string
                            example: "23450.00000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00001000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "0.23450000"
                          status:
                            type: string
                            example: CANCELED
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                          icebergQty:
                            type: string
                            example: "0.00000000"
                            description: Appears only if the parameter icebergQty was sent in the request.
                            x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                          preventedMatchId:
                            type: integer
                            format: int64
                            example: 0
                            description: Appears only if the order expired due to STP.
                            x-description-cn: 仅在因 STP 导致订单失效时出现。
                          preventedQuantity:
                            type: string
                            example: "1.200000"
                            description: Order quantity that expired due to STP.
                            x-description-cn: 因 STP 导致订单失效的数量。
                          stopPrice:
                            type: string
                            example: "0.00000000"
                            description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                            x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                          strategyId:
                            type: integer
                            format: int64
                            example: 1
                            description: Appears only if the strategyId parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                          strategyType:
                            type: integer
                            format: int64
                            example: 1000000
                            description: Appears only if the strategyType parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                          trailingDelta:
                            type: integer
                            format: int64
                            example: 10
                            description: Delta price change required before order activation.
                            x-description-cn: 订单激活前所需的价格变动。
                          trailingTime:
                            type: integer
                            format: int64
                            example: -1
                            description: Time when the trailing order is now active and tracking price changes.
                            x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                          usedSor:
                            type: boolean
                            example: true
                            description: Field that determines whether order used SOR.
                            x-description-cn: 用于确定订单是否使用SOR的字段。
                          workingFloor:
                            type: string
                            example: SOR
                            description: Determines whether the order is being filled by the SOR or by the order book.
                            x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                          pegPriceType:
                            type: string
                            example: PRIMARY_PEG
                            description: Price peg type. Only for pegged orders.
                            x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                          pegOffsetType:
                            type: string
                            example: PRICE_LEVEL
                            description: Price peg offset type. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                          pegOffsetValue:
                            type: integer
                            format: int64
                            example: 5
                            description: Price peg offset value. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                          peggedPrice:
                            type: string
                            example: "87523.83710000"
                            description: Current price order is pegged at. Only for pegged orders, once determined.
                            x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                          expiryReason:
                            type: string
                            example: INSUFFICIENT_LIQUIDITY
                            description: Cause of the order's expiration. Appears when an order has expired.
                            x-description-cn: 订单过期的原因。当订单过期时出现。
                      newOrderResponse:
                        type: object
                        description: |-
                          Format is identical to "order.place" format, affected by "newOrderRespType".
                          Some fields are optional and are included only for orders that set them.
                        x-description-cn: |-
                          格式与 "order.place" 格式相同, 受 "newOrderRespType" 影响。
                          某些字段是可选的，仅在订单中有设置它们时才包括。
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            example: -1
                          clientOrderId:
                            type: string
                            example: bX5wROblo6YeDwa9iTLeyY
                          transactTime:
                            type: integer
                            format: int64
                            example: 1660813156959
                          price:
                            type: string
                            example: "23416.10000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00000000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "0.00000000"
                          status:
                            type: string
                            example: NEW
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                          icebergQty:
                            type: string
                            example: "0.00000000"
                            description: Appears only if the parameter icebergQty was sent in the request.
                            x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                          preventedMatchId:
                            type: integer
                            format: int64
                            example: 0
                            description: Appears only if the order expired due to STP.
                            x-description-cn: 仅在因 STP 导致订单失效时出现。
                          preventedQuantity:
                            type: string
                            example: "1.200000"
                            description: Order quantity that expired due to STP.
                            x-description-cn: 因 STP 导致订单失效的数量。
                          stopPrice:
                            type: string
                            example: "0.00000000"
                            description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                            x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                          strategyId:
                            type: integer
                            format: int64
                            example: 1
                            description: Appears only if the strategyId parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                          strategyType:
                            type: integer
                            format: int64
                            example: 1000000
                            description: Appears only if the strategyType parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                          trailingDelta:
                            type: integer
                            format: int64
                            example: 10
                            description: Delta price change required before order activation.
                            x-description-cn: 订单激活前所需的价格变动。
                          trailingTime:
                            type: integer
                            format: int64
                            example: -1
                            description: Time when the trailing order is now active and tracking price changes.
                            x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                          usedSor:
                            type: boolean
                            example: true
                            description: Field that determines whether order used SOR.
                            x-description-cn: 用于确定订单是否使用SOR的字段。
                          workingFloor:
                            type: string
                            example: SOR
                            description: Determines whether the order is being filled by the SOR or by the order book.
                            x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                          pegPriceType:
                            type: string
                            example: PRIMARY_PEG
                            description: Price peg type. Only for pegged orders.
                            x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                          pegOffsetType:
                            type: string
                            example: PRICE_LEVEL
                            description: Price peg offset type. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                          pegOffsetValue:
                            type: integer
                            format: int64
                            example: 5
                            description: Price peg offset value. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                          peggedPrice:
                            type: string
                            example: "87523.83710000"
                            description: Current price order is pegged at. Only for pegged orders, once determined.
                            x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                          expiryReason:
                            type: string
                            example: INSUFFICIENT_LIQUIDITY
                            description: Cause of the order's expiration. Appears when an order has expired.
                            x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: SECOND
                        intervalNum: 10
                        limit: 50
                        count: 1
                      - rateLimitType: ORDERS
                        interval: DAY
                        intervalNum: 1
                        limit: 160000
                        count: 1
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 6000
                        count: 1
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
        Unsuccessful Response (400):
          description: Order cancel-replace failed
          x-description-cn: 撤消挂单再下单失败
          content:
            application/json:
              schema:
                oneOf:
                  - description: |-
                      In `STOP_ON_FAILURE` mode, failed order cancellation prevents new order from being placed
                      and returns the following response with `"status": 400`:
                    x-description-cn: '在 `STOP_ON_FAILURE` 模式，失败的撤销订单会阻止下新订单，响应会是`"status": 400`：'
                    type: object
                    properties:
                      id:
                        type: string
                        example: 27e1bf9f-0539-4fb0-85c6-06183d36f66c
                      status:
                        type: integer
                        format: int64
                        example: 400
                      error:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2022
                          msg:
                            type: string
                            example: Order cancel-replace failed.
                          data:
                            type: object
                            properties:
                              cancelResult:
                                type: string
                                example: FAILURE
                              newOrderResult:
                                type: string
                                example: NOT_ATTEMPTED
                              cancelResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -2011
                                  msg:
                                    type: string
                                    example: Unknown order sent.
                              newOrderResponse:
                                example: null
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                  - description: 'If both operations fail, response will have `"status": 400`:'
                    x-description-cn: '如果两个操作都失败，响应将有 `"status": 400`：'
                    type: object
                    properties:
                      id:
                        type: string
                        example: 3b3ac45c-1002-4c7d-88e8-630c408ecd87
                      status:
                        type: integer
                        format: int64
                        example: 400
                      error:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2022
                          msg:
                            type: string
                            example: Order cancel-replace failed.
                          data:
                            type: object
                            properties:
                              cancelResult:
                                type: string
                                example: FAILURE
                              newOrderResult:
                                type: string
                                example: FAILURE
                              cancelResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -2011
                                  msg:
                                    type: string
                                    example: Unknown order sent.
                              newOrderResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -2010
                                  msg:
                                    type: string
                                    example: Order would immediately match and take.
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
        Unsuccessful Response (409):
          description: Order cancel-replace partially failed
          x-description-cn: 撤消挂单再下单部分失败
          content:
            application/json:
              schema:
                oneOf:
                  - description: |-
                      If cancel-replace mode allows failure and one of the operations fails,
                      you get a response with `"status": 409`,
                      and the `"data"` field detailing which operation succeeded, which failed, and why.

                      Cancellation succeeded, new order placement failed:
                    x-description-cn: |-
                      如果 cancel-replace 模式允许失败并且其中一个操作失败，响应会是 `"status": 409` 和 `"data"` 字段会制定哪个操作成功，哪个失败，以及原因：

                      撤销订单成功，下新订单失败：
                    type: object
                    properties:
                      id:
                        type: string
                        example: b220edfe-f3c4-4a3a-9d13-b35473783a25
                      status:
                        type: integer
                        format: int64
                        example: 409
                      error:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2021
                          msg:
                            type: string
                            example: Order cancel-replace partially failed.
                          data:
                            type: object
                            properties:
                              cancelResult:
                                type: string
                                example: SUCCESS
                              newOrderResult:
                                type: string
                                example: FAILURE
                              cancelResponse:
                                type: object
                                properties:
                                  symbol:
                                    type: string
                                    example: BTCUSDT
                                  origClientOrderId:
                                    type: string
                                    example: 4d96324ff9d44481926157
                                    description: cancelOrigClientOrderId from request
                                    x-description-cn: 请求的 cancelOrigClientOrderId
                                  orderId:
                                    type: integer
                                    format: int64
                                    example: 125690984230
                                  orderListId:
                                    type: integer
                                    format: int64
                                    example: -1
                                  clientOrderId:
                                    type: string
                                    example: 91fe37ce9e69c90d6358c0
                                    description: cancelNewClientOrderId from request
                                    x-description-cn: 请求的 cancelNewClientOrderId
                                  transactTime:
                                    type: integer
                                    format: int64
                                    example: 1684804350068
                                  price:
                                    type: string
                                    example: "23450.00000000"
                                  origQty:
                                    type: string
                                    example: "0.00847000"
                                  executedQty:
                                    type: string
                                    example: "0.00001000"
                                  origQuoteOrderQty:
                                    type: string
                                    example: "0.000000"
                                  cummulativeQuoteQty:
                                    type: string
                                    example: "0.23450000"
                                  status:
                                    type: string
                                    example: CANCELED
                                  timeInForce:
                                    type: string
                                    example: GTC
                                  type:
                                    type: string
                                    example: LIMIT
                                  side:
                                    type: string
                                    example: SELL
                                  selfTradePreventionMode:
                                    type: string
                                    example: NONE
                              newOrderResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -2010
                                  msg:
                                    type: string
                                    example: Order would immediately match and take.
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                  - description: "Cancellation failed, new order placement succeeded:"
                    x-description-cn: 撤销订单失败，下新订单成功：
                    type: object
                    properties:
                      id:
                        type: string
                        example: ce641763-ff74-41ac-b9f7-db7cbe5e93b1
                      status:
                        type: integer
                        format: int64
                        example: 409
                      error:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2021
                          msg:
                            type: string
                            example: Order cancel-replace partially failed.
                          data:
                            type: object
                            properties:
                              cancelResult:
                                type: string
                                example: FAILURE
                              newOrderResult:
                                type: string
                                example: SUCCESS
                              cancelResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -2011
                                  msg:
                                    type: string
                                    example: Unknown order sent.
                              newOrderResponse:
                                type: object
                                properties:
                                  symbol:
                                    type: string
                                    example: BTCUSDT
                                  orderId:
                                    type: integer
                                    format: int64
                                    example: 12569099453
                                  orderListId:
                                    type: integer
                                    format: int64
                                    example: -1
                                  clientOrderId:
                                    type: string
                                    example: bX5wROblo6YeDwa9iTLeyY
                                  transactTime:
                                    type: integer
                                    format: int64
                                    example: 1660813156959
                                  price:
                                    type: string
                                    example: "23416.10000000"
                                  origQty:
                                    type: string
                                    example: "0.00847000"
                                  executedQty:
                                    type: string
                                    example: "0.00000000"
                                  origQuoteOrderQty:
                                    type: string
                                    example: "0.000000"
                                  cummulativeQuoteQty:
                                    type: string
                                    example: "0.00000000"
                                  status:
                                    type: string
                                    example: NEW
                                  timeInForce:
                                    type: string
                                    example: GTC
                                  type:
                                    type: string
                                    example: LIMIT
                                  side:
                                    type: string
                                    example: SELL
                                  workingTime:
                                    type: integer
                                    format: int64
                                    example: 1669693344508
                                  fills:
                                    type: array
                                    example: []
                                  selfTradePreventionMode:
                                    type: string
                                    example: NONE
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                  - description: >-
                      If `orderRateLimitExceededMode` is `CANCEL_ONLY` regardless of `cancelReplaceMode`, and you have
                      exceeded your unfilled order count, you will get status `409` with the following error:
                    x-description-cn: >-
                      如果 `orderRateLimitExceededMode` 是 `CANCEL_ONLY`，那么无论 `cancelReplaceMode` 的取值，当账户超出未成交订单计数时，响应将有
                      `"status": 409`:
                    type: object
                    properties:
                      id:
                        type: string
                        example: 3b3ac45c-1002-4c7d-88e8-630c408ecd87
                      status:
                        type: integer
                        format: int64
                        example: 409
                      error:
                        type: object
                        properties:
                          code:
                            type: integer
                            format: int64
                            example: -2021
                          msg:
                            type: string
                            example: Order cancel-replace partially failed.
                          data:
                            type: object
                            properties:
                              cancelResult:
                                type: string
                                example: SUCCESS
                              newOrderResult:
                                type: string
                                example: FAILURE
                              cancelResponse:
                                type: object
                                properties:
                                  symbol:
                                    type: string
                                    example: LTCBNB
                                  origClientOrderId:
                                    type: string
                                    example: GKt5zzfOxRDSQLveDYCTkc
                                    description: cancelOrigClientOrderId from request
                                    x-description-cn: 请求的 cancelOrigClientOrderId
                                  orderId:
                                    type: integer
                                    format: int64
                                    example: 64
                                  orderListId:
                                    type: integer
                                    format: int64
                                    example: -1
                                  clientOrderId:
                                    type: string
                                    example: loehOJF3FjoreUBDmv739R
                                    description: cancelNewClientOrderId from request
                                    x-description-cn: 请求的 cancelNewClientOrderId
                                  transactTime:
                                    type: integer
                                    format: int64
                                    example: 1715779007228
                                  price:
                                    type: string
                                    example: "1.00"
                                  origQty:
                                    type: string
                                    example: "10.00000000"
                                  executedQty:
                                    type: string
                                    example: "0.00000000"
                                  origQuoteOrderQty:
                                    type: string
                                    example: "0.000000"
                                  cummulativeQuoteQty:
                                    type: string
                                    example: "0.00"
                                  status:
                                    type: string
                                    example: CANCELED
                                  timeInForce:
                                    type: string
                                    example: GTC
                                  type:
                                    type: string
                                    example: LIMIT
                                  side:
                                    type: string
                                    example: SELL
                                  selfTradePreventionMode:
                                    type: string
                                    example: NONE
                              newOrderResponse:
                                type: object
                                properties:
                                  code:
                                    type: integer
                                    format: int64
                                    example: -1015
                                  msg:
                                    type: string
                                    example: >-
                                      Too many orders placed without trading; current limit is 50 non-trading orders per
                                      10 SECOND. Unable to place new orders until trades occur or window resets.
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 50
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 50
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 50
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
        Unsuccessful Response (429):
          description: Too many new orders
          x-description-cn: 新订单过多
          content:
            application/json:
              schema:
                description: >-
                  If `orderRateLimitExceededMode` is `DO_NOTHING` regardless of `cancelReplaceMode`, and you have
                  exceeded your unfilled order count, you will get status `429` with the following error:
                x-description-cn: >-
                  如果 `orderRateLimitExceededMode` 是 `DO_NOTHING`，那么无论 `cancelReplaceMode` 的取值，当账户超出未成交订单计数时，响应将有
                  `"status": 429`:
                type: object
                properties:
                  id:
                    type: string
                    example: 3b3ac45c-1002-4c7d-88e8-630c408ecd87
                  status:
                    type: integer
                    format: int64
                    example: 429
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                        format: int64
                        example: -1015
                      msg:
                        type: string
                        example: >-
                          Too many orders placed without trading; current limit is 50 non-trading orders per 10 SECOND.
                          Unable to place new orders until trades occur or window resets.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: ORDERS
                        interval:
                          type: string
                          example: SECOND
                        intervalNum:
                          type: integer
                          format: int64
                          example: 10
                        limit:
                          type: integer
                          format: int64
                          example: 50
                        count:
                          type: integer
                          format: int64
                          example: 50
                    example:
                      - rateLimitType: ORDERS
                        interval: SECOND
                        intervalNum: 10
                        limit: 50
                        count: 50
                      - rateLimitType: ORDERS
                        interval: DAY
                        intervalNum: 1
                        limit: 160000
                        count: 50
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 6000
                        count: 1
  /orderList.cancel:
    post:
      summary: Cancel Order list (TRADE)
      x-summary-cn: 撤销订单列表订单 (TRADE)
      description: Cancel an active order list.
      x-description-cn: 取消整个订单列表。
      tags:
        - trade
      operationId: orderListCancel
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-cancel
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListCancel.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_cancel.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_cancel.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListCancelExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListCancel/OrderListCancel.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        Notes:


        * If both `orderListId` and `listClientOrderId` parameters are provided, the `orderListId` is searched first,
        then the `listClientOrderId` from that result is checked against that order. If both conditions are not met the
        request will be rejected.


        * Canceling an individual order with [`order.cancel`](#order-cancel) will cancel the entire order list as well.
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        备注：


        * 如果同时指定了 `orderListId` 和 `listClientOrderId` 参数，首先将会用`orderListId` 进行搜索，然后将检索结果中的 `listClientOrderId`
        与订单进行比对。如果两个条件都不满足，则请求将被拒绝。


        * 使用 [`order.cancel`](#order-cancel) 撤销订单列表内的某个订单，则整个订单列表将被撤销。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.cancel
                  example: orderList.cancel
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    orderListId:
                      type: integer
                      example: 1
                      description: Either `orderListId` or `listClientOrderId` must be provided
                      x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
                    listClientOrderId:
                      type: string
                      example: C3wyj4WVEktd7u9aVBRXcN
                      description: Either `orderListId` or `listClientOrderId` must be provided
                      x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
                    newClientOrderId:
                      type: string
                      example: cancelMyOrder1
                      description: Used to uniquely identify this cancel. Automatically generated by default.
                      x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.cancel
              params:
                symbol: BNBUSDT
                orderListId: 1
                listClientOrderId: C3wyj4WVEktd7u9aVBRXcN
                newClientOrderId: cancelMyOrder1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Cancel Order list
          x-description-cn: 撤销订单列表订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: c5899911-d3f4-47ae-8835-97da553d27d0
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 1274512
                      contingencyType:
                        type: string
                        example: OCO
                      listStatusType:
                        type: string
                        example: ALL_DONE
                      listOrderStatus:
                        type: string
                        example: ALL_DONE
                      listClientOrderId:
                        type: string
                        example: 6023531d7edaad348f5aff
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1660801720215
                      symbol:
                        type: string
                        example: BTCUSDT
                      orders:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 12569138901
                            clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                          - symbol: BTCUSDT
                            orderId: 12569138902
                            clientOrderId: jLnZpj5enfMXTuhKB1d0us
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 12569138901
                            clientOrderId:
                              type: string
                              example: BqtFCj5odMoWtSqGk2X9tU
                      orderReports:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 12569138901
                            orderListId: 1274512
                            clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                            transactTime: 1660801720215
                            price: "23410.00000000"
                            origQty: "0.00650000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: CANCELED
                            timeInForce: GTC
                            type: STOP_LOSS_LIMIT
                            side: SELL
                            stopPrice: "23405.00000000"
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            orderId: 12569138902
                            orderListId: 1274512
                            clientOrderId: jLnZpj5enfMXTuhKB1d0us
                            transactTime: 1660801720215
                            price: "23420.00000000"
                            origQty: "0.00650000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: CANCELED
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: SELL
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 12569138901
                            orderListId:
                              type: integer
                              format: int64
                              example: 1274512
                            clientOrderId:
                              type: string
                              example: BqtFCj5odMoWtSqGk2X9tU
                            transactTime:
                              type: integer
                              format: int64
                              example: 1660801720215
                            price:
                              type: string
                              example: "23410.00000000"
                            origQty:
                              type: string
                              example: "0.00650000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: CANCELED
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: STOP_LOSS_LIMIT
                            side:
                              type: string
                              example: SELL
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "23405.00000000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /orderList.place:
    post:
      summary: Place new OCO - Deprecated (TRADE)
      x-summary-cn: OCO下单 - 已弃用 (TRADE)
      description: |-
        Send in a new one-cancels-the-other (OCO) pair:
        `LIMIT_MAKER` + `STOP_LOSS`/`STOP_LOSS_LIMIT` orders (called *legs*),
        where activation of one order immediately cancels the other.

        This adds 1 order to `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter
      x-description-cn: |-
        发送新的OCO(one-cancels-the-other) 订单:
        `LIMIT_MAKER` 订单 + `STOP_LOSS`/`STOP_LOSS_LIMIT` 订单(称呼为 *legs*), 其中一个订单的激活会立即取消另一个订单。

        这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      deprecated: true
      tags:
        - trade
      operationId: orderListPlace
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlace.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlace/OrderListPlace.go
      x-ip-weight: 1
      x-legacy-anchors:
        - order-lists
      x-order-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Matching Engine

        Notes:

        * `listClientOrderId` parameter specifies `listClientOrderId` for the OCO pair.

          A new OCO with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.

          `listClientOrderId` is distinct from `clientOrderId` of individual orders.

        * `limitClientOrderId` and `stopClientOrderId` specify `clientOrderId` values for both legs of the OCO.

          A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

        * Price restrictions on the legs:

          | `side` | Price relation |
          | ------ | -------------- |
          | `BUY`  | `price` < market price < `stopPrice` |
          | `SELL` | `price` > market price > `stopPrice` |

        * Both legs have the same `quantity`.

          However, you can set different iceberg quantity for individual legs.

          If `stopIcebergQty` is used, `stopLimitTimeInForce` must be `GTC`.

        * `trailingDelta` applies only to the `STOP_LOSS`/`STOP_LOSS_LIMIT` leg of the OCO.
      x-parameters-notes-cn: |
        **数据源:** 撮合引擎

        备注：

        * `listClientOrderId` 参数指定 OCO 对的 `listClientOrderId`。

          只有当前一个 OCO 已满或完全过期时，才会接受具有相同 `listClientOrderId` 的新 OCO。

          `listClientOrderId` 与单个订单的 `clientOrderId` 不同。

        * legs 的价格限制：

          | `side` | 价格关系 |
          | ------ | -------------- |
          | `BUY` | `price` < 市场价格 < `stopPrice` |
          | `SELL`| `price` > 市场价格 > `stopPrice` |

        * 两个 legs 的 `quantity` 需要相同。

          不过单个 leg 可以设置不同的冰山数量。

          如果使用 `stopIcebergQty`，`stopLimitTimeInForce` 必须是 `GTC`。

        * `trailingDelta` 仅适用于 OCO 的 `STOP_LOSS`/`STOP_LOSS_LIMIT` leg。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place
                  example: orderList.place
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: Please see [Enums](/products/spot/enums#side) for supported values.
                      x-description-cn: 详见枚举定义：[订单方向](/products/spot/enums#side)
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    listClientOrderId:
                      type: string
                      example: 08985fedd9ea2cf6b28996
                      description: A unique Id for the entire orderList
                      x-description-cn: 整个orderList的唯一ID
                    limitClientOrderId:
                      type: string
                      example: limitOrder1
                      description: A unique Id for the limit order
                      x-description-cn: 限价单的唯一ID
                    limitIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used to make the `LIMIT_MAKER` leg an iceberg order.
                      x-description-cn: 用于使 `LIMIT_MAKER` 腿单成为冰山订单。
                    limitStrategyId:
                      type: integer
                      format: int64
                      example: 1
                    limitStrategyType:
                      type: integer
                      example: 1
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 不能低于 `1000000`
                    stopPrice:
                      type: number
                      format: float
                      example: 1
                    trailingDelta:
                      type: integer
                      example: 1
                    stopClientOrderId:
                      type: string
                      example: stopOrder1
                      description: A unique Id for the stop loss/stop loss limit leg
                      x-description-cn: 止损/止损限价单的唯一ID
                    stopLimitPrice:
                      type: number
                      format: float
                      example: 1
                      description: If provided, `stopLimitTimeInForce` is required.
                      x-description-cn: 如果提供，须配合提交`stopLimitTimeInForce`
                    stopLimitTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Valid values are `GTC`/`FOK`/`IOC`
                      x-description-cn: 有效值 `GTC`/`FOK`/`IOC`
                    stopIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.
                      x-description-cn: 与 `STOP_LOSS_LIMIT` 腿单一起使用，使其成为冰山订单。
                    stopStrategyId:
                      type: integer
                      format: int64
                      example: 1
                    stopStrategyType:
                      type: integer
                      example: 1
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 不能低于 `1000000`
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Format of the JSON response. Supported values: [Order Response
                        Type](/products/spot/enums#orderresponsetype)
                      x-description-cn: JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed values are dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - price
                    - quantity
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place
              params:
                symbol: BNBUSDT
                side: BUY
                price: 1
                quantity: 1
                listClientOrderId: 08985fedd9ea2cf6b28996
                limitClientOrderId: limitOrder1
                limitIcebergQty: 1
                limitStrategyId: 1
                limitStrategyType: 1
                stopPrice: 1
                trailingDelta: 1
                stopClientOrderId: stopOrder1
                stopLimitPrice: 1
                stopLimitTimeInForce: GTC
                stopIcebergQty: 1
                stopStrategyId: 1
                stopStrategyType: 1
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Place new OCO - Deprecated
          x-description-cn: OCO下单 - 已弃用
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 57833dc0-e3f2-43fb-ba20-46480973b0aa
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 1274512
                      contingencyType:
                        type: string
                        example: OCO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: 08985fedd9ea2cf6b28996
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1660801713793
                      symbol:
                        type: string
                        example: BTCUSDT
                      orders:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 12569138901
                            clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                          - symbol: BTCUSDT
                            orderId: 12569138902
                            clientOrderId: jLnZpj5enfMXTuhKB1d0us
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 12569138901
                            clientOrderId:
                              type: string
                              example: BqtFCj5odMoWtSqGk2X9tU
                      orderReports:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 12569138901
                            orderListId: 1274512
                            clientOrderId: BqtFCj5odMoWtSqGk2X9tU
                            transactTime: 1660801713793
                            price: "23410.00000000"
                            origQty: "0.00650000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: STOP_LOSS_LIMIT
                            side: SELL
                            stopPrice: "23405.00000000"
                            workingTime: -1
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            orderId: 12569138902
                            orderListId: 1274512
                            clientOrderId: jLnZpj5enfMXTuhKB1d0us
                            transactTime: 1660801713793
                            price: "23420.00000000"
                            origQty: "0.00650000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: SELL
                            workingTime: 1660801713793
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 12569138901
                            orderListId:
                              type: integer
                              format: int64
                              example: 1274512
                            clientOrderId:
                              type: string
                              example: BqtFCj5odMoWtSqGk2X9tU
                            transactTime:
                              type: integer
                              format: int64
                              example: 1660801713793
                            price:
                              type: string
                              example: "23410.00000000"
                            origQty:
                              type: string
                              example: "0.00650000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: STOP_LOSS_LIMIT
                            side:
                              type: string
                              example: SELL
                            workingTime:
                              type: integer
                              format: int64
                              example: -1
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "23405.00000000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: SECOND
                        intervalNum: 10
                        limit: 50
                        count: 2
                      - rateLimitType: ORDERS
                        interval: DAY
                        intervalNum: 1
                        limit: 160000
                        count: 2
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 6000
                        count: 1
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /orderList.place.oco:
    post:
      summary: Place new Order list - OCO (TRADE)
      x-summary-cn: 发送新 OCO 订单 (TRADE)
      description: |-
        Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

        * An OCO has 2 orders called the **above order** and **below order**.

        * One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be
        `STOP_LOSS` or `STOP_LOSS_LIMIT` order.

        * Price restrictions:
          * If the OCO is on the `SELL` side:
            * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT`
        `stopPrice`
            * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT
        stopPrice`
          * If the OCO is on the `BUY` side:
            * `LIMIT_MAKER` `price` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
            * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
        *  OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

        * OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单**。
        * 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
        * 针对价格限制：
          * 如果 OCO 订单方向是 `SELL`：
            * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT`
        `stopPrice`
            * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
          * 如果 OCO 订单方向是 `BUY`：
            * `LIMIT_MAKER` `price` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
            * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
        * OCO 将**2 个订单**添加到 `EXCHANGE_MAX_ORDERS`过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: orderListPlaceOco
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlaceOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlaceOco/OrderListPlaceOco.go
      x-ip-weight: 1
      x-order-weight: 2
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place.oco
                  example: orderList.place.oco
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    listClientOrderId:
                      type: string
                      example: cKPMnDCbcLQILtDYM4f4fX
                      description: >-
                        Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order
                        list with the same `listClientOrderId` is accepted only when the previous one is filled or
                        completely expired. `listClientOrderId` is distinct from the `aboveClientOrderId` and the
                        `belowClientOrderId`.
                      x-description-cn: >-
                        整个 OCO order list 的唯一ID。 如果未发送则自动生成。 仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。
                        `listClientOrderId` 与 `aboveClientOrderId` 和 `belowClientOrderId` 不同。
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "`BUY` or `SELL`"
                      x-description-cn: 订单方向：`BUY` or `SELL`
                    quantity:
                      type: number
                      format: float
                      example: 1
                      description: Quantity for both orders of the order list.
                      x-description-cn: 两个订单的数量。
                    aboveType:
                      type: string
                      enum:
                        - STOP_LOSS_LIMIT
                        - STOP_LOSS
                        - LIMIT_MAKER
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS_LIMIT
                    aboveClientOrderId:
                      type: string
                      example: aboveOrder1
                      description: Arbitrary unique ID among open orders for the above order. Automatically generated if not sent.
                      x-description-cn: 上方订单的唯一ID。 如果未发送则自动生成。
                    aboveIcebergQty:
                      type: integer
                      format: int64
                      example: 1
                      description: Note that this can only be used if `aboveTimeInForce` is `GTC`.
                      x-description-cn: 请注意，只有当 `aboveTimeInForce` 为 `GTC` 时才能使用。
                    abovePrice:
                      type: number
                      format: float
                      example: 1.5
                      description: >-
                        Can be used if `aboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to
                        specify the limit price.
                      x-description-cn: 当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                    aboveStopPrice:
                      type: number
                      format: float
                      example: 1.50000001
                      description: >-
                        Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`. Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.
                      x-description-cn: >-
                        如果 `aboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定
                        `aboveStopPrice` 或 `aboveTrailingDelta` 或两者。
                    aboveTrailingDelta:
                      type: integer
                      format: int64
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    aboveTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `aboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。
                    aboveStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the above order within an order strategy.
                      x-description-cn: 订单策略中上方订单的 ID。
                    aboveStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the above order strategy. Values smaller than `1000000` are
                        reserved and cannot be used.
                      x-description-cn: 上方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。
                    abovePegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: "`PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)"
                      x-description-cn: "`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)"
                    abovePegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    abovePegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    belowType:
                      type: string
                      enum:
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS
                      description: "Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`"
                      x-description-cn: 支持值：`STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`。
                    belowClientOrderId:
                      type: string
                      example: belowOrder1
                      description: Arbitrary unique ID among open orders for the below order. Automatically generated if not sent.
                      x-description-cn: 下方订单的唯一ID。 如果未发送则自动生成。
                    belowIcebergQty:
                      type: integer
                      format: int64
                      example: 1
                      description: Note that this can only be used if `belowTimeInForce` is `GTC`.
                      x-description-cn: 请注意，只有当 `belowTimeInForce` 为 `GTC` 时才能使用。
                    belowPrice:
                      type: number
                      format: float
                      example: 1.49999999
                      description: >-
                        Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to
                        specify the limit price.
                      x-description-cn: 当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                    belowStopPrice:
                      type: number
                      format: float
                      example: 1.50000001
                      description: >-
                        Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`. Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.
                      x-description-cn: >-
                        如果 `belowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。 必须指定
                        `belowStopPrice` 或 `belowTrailingDelta` 或两者。
                    belowTrailingDelta:
                      type: integer
                      format: int64
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    belowTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `belowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。
                    belowStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the below order within an order strategy.
                      x-description-cn: 订单策略中下方订单的 ID。
                    belowStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the below order strategy. Values smaller than `1000000` are
                        reserved and cannot be used.
                      x-description-cn: 下方订单策略的任意数值。小于 `1000000` 的值被保留，无法使用。
                    belowPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    belowPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    belowPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: "Select response format: `ACK`, `RESULT`, `FULL`."
                      x-description-cn: "响应格式可选值: `ACK`, `RESULT`, `FULL`。"
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的 ENUM 取决于交易对上的配置。 支持值：[STP 模式](/products/spot/enums#stpmodes)
                    aboveQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the above order (only for orders on the BUY side). See [Quote Notional
                        Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    belowQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the below order (only for orders on the BUY side). See [Quote Notional
                        Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - quantity
                    - aboveType
                    - belowType
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place.oco
              params:
                symbol: BNBUSDT
                listClientOrderId: cKPMnDCbcLQILtDYM4f4fX
                side: BUY
                quantity: 1
                aboveType: STOP_LOSS_LIMIT
                aboveClientOrderId: aboveOrder1
                aboveIcebergQty: 1
                abovePrice: 1.5
                aboveStopPrice: 1.50000001
                aboveTrailingDelta: 1
                aboveTimeInForce: GTC
                aboveStrategyId: 1
                aboveStrategyType: 1
                abovePegPriceType: PRIMARY_PEG
                abovePegOffsetType: PRICE_LEVEL
                abovePegOffsetValue: 1
                belowType: STOP_LOSS
                belowClientOrderId: belowOrder1
                belowIcebergQty: 1
                belowPrice: 1.49999999
                belowStopPrice: 1.50000001
                belowTrailingDelta: 1
                belowTimeInForce: GTC
                belowStrategyId: 1
                belowStrategyType: 1
                belowPegPriceType: PRIMARY_PEG
                belowPegOffsetType: PRICE_LEVEL
                belowPegOffsetValue: 1
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                aboveQuoteNotionalLimit: 100
                belowQuoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Place new Order list - OCO
          x-description-cn: 发送新 OCO 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 56374a46-3261-486b-a211-99ed972eb648
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 2
                      contingencyType:
                        type: string
                        example: OCO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: cKPMnDCbcLQILtDYM4f4fX
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1711062760648
                      symbol:
                        type: string
                        example: LTCBNB
                      orders:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 2
                            clientOrderId: 0m6I4wfxvTUrOBSMUl0OPU
                          - symbol: LTCBNB
                            orderId: 3
                            clientOrderId: Z2IMlR79XNY5LU0tOxrWyW
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 2
                            clientOrderId:
                              type: string
                              example: 0m6I4wfxvTUrOBSMUl0OPU
                      orderReports:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 2
                            orderListId: 2
                            clientOrderId: 0m6I4wfxvTUrOBSMUl0OPU
                            transactTime: 1711062760648
                            price: "1.50000000"
                            origQty: "1.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: STOP_LOSS_LIMIT
                            side: BUY
                            stopPrice: "1.50000001"
                            workingTime: -1
                            selfTradePreventionMode: NONE
                          - symbol: LTCBNB
                            orderId: 3
                            orderListId: 2
                            clientOrderId: Z2IMlR79XNY5LU0tOxrWyW
                            transactTime: 1711062760648
                            price: "1.49999999"
                            origQty: "1.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: BUY
                            workingTime: 1711062760648
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 2
                            orderListId:
                              type: integer
                              format: int64
                              example: 2
                            clientOrderId:
                              type: string
                              example: 0m6I4wfxvTUrOBSMUl0OPU
                            transactTime:
                              type: integer
                              format: int64
                              example: 1711062760648
                            price:
                              type: string
                              example: "1.50000000"
                            origQty:
                              type: string
                              example: "1.000000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: STOP_LOSS_LIMIT
                            side:
                              type: string
                              example: BUY
                            workingTime:
                              type: integer
                              format: int64
                              example: -1
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "1.50000001"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: SECOND
                        intervalNum: 10
                        limit: 50
                        count: 2
                      - rateLimitType: ORDERS
                        interval: DAY
                        intervalNum: 1
                        limit: 160000
                        count: 2
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 6000
                        count: 1
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /orderList.place.opo:
    post:
      summary: OPO (TRADE)
      x-summary-cn: 新订单列表 - OPO (TRADE)
      description: |-
        Place an [OPO](/products/spot/faqs/opo).

        * The working order must be `LIMIT` or `LIMIT_MAKER`.
        * OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.
      x-description-cn: |-
        发送一个 [OPO](/products/spot/faqs/opo) 订单。

        * 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
        * OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。
      tags:
        - trade
      operationId: orderListPlaceOpo
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-opo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlaceOpo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place_opo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place_opo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceOpoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlaceOpo/OrderListPlaceOpo.go
      x-ip-weight: 1
      x-order-weight: 2
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place.opo
                  example: orderList.place.opo
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    listClientOrderId:
                      type: string
                      example: OiOgqvRagBefpzdM5gjYX3
                      description: >-
                        Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order
                        list with the same `listClientOrderId` is accepted only when the previous one is filled or
                        completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the
                        `pendingClientOrderId`.
                      x-description-cn: >-
                        订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId`
                        的订单列表。`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Format of the JSON response. Supported values: [Order Response
                        Type](/products/spot/enums#orderresponsetype)
                      x-description-cn: JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)
                    workingType:
                      type: string
                      enum:
                        - LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: "Supported values: `LIMIT`, `LIMIT_MAKER`"
                      x-description-cn: 支持的数值：`LIMIT`，`LIMIT_MAKER`
                    workingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值：[订单方向](/products/spot/enums#side)
                    workingClientOrderId:
                      type: string
                      example: workingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the working order. Automatically generated if not
                        sent.
                      x-description-cn: 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。
                    workingPrice:
                      type: number
                      format: float
                      example: 1
                      description: Price for the working order.
                      x-description-cn: 生效订单价格
                    workingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the working order.
                      x-description-cn: 设置生效订单的数量
                    workingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
                      x-description-cn: 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用
                    workingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值：[生效时间](/products/spot/enums#timeinforce)
                    workingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the working order within an order strategy.
                      x-description-cn: 用于标识订单策略中生效订单的任意数字值
                    workingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。
                    workingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    workingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    workingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    pendingType:
                      type: string
                      enum:
                        - LIMIT
                        - MARKET
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: >-
                        Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders
                        using `quoteOrderQty` are not supported.
                      x-description-cn: 支持的数值：[订单类型](/products/spot/enums#ordertypes)。注意，不支持使用 `quoteOrderQty` 的 `MARKET` 订单。
                    pendingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值：[订单方向](/products/spot/enums#side)
                    pendingClientOrderId:
                      type: string
                      example: pendingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending order. Automatically generated if not
                        sent.
                      x-description-cn: 待处理订单中挂单的任意唯一 ID。如果未发送，则自动生成。
                    pendingPrice:
                      type: number
                      format: float
                      example: 1
                      description: Price for the pending order.
                      x-description-cn: 待处理订单价格
                    pendingStopPrice:
                      type: number
                      format: float
                      example: 1
                      description: Stop price for the pending order.
                      x-description-cn: 待处理订单止损价格
                    pendingTrailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: Trailing delta for the pending order.
                      x-description-cn: 待处理订单跟踪止损差值
                    pendingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.
                      x-description-cn: 仅当 `pendingTimeInForce` 为 `GTC` 或 `pendingType` 为 `LIMIT_MAKER` 时可用
                    pendingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值：[生效时间](/products/spot/enums#timeinforce)
                    pendingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending order within an order strategy.
                      x-description-cn: 用于标识订单策略中待处理订单的任意数字值
                    pendingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识待处理订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。
                    pendingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    pendingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    workingQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional
                        Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - workingType
                    - workingSide
                    - workingPrice
                    - workingQuantity
                    - pendingType
                    - pendingSide
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place.opo
              params:
                symbol: BNBUSDT
                listClientOrderId: OiOgqvRagBefpzdM5gjYX3
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                workingType: LIMIT
                workingSide: BUY
                workingClientOrderId: workingOrder1
                workingPrice: 1
                workingQuantity: 1
                workingIcebergQty: 1
                workingTimeInForce: GTC
                workingStrategyId: 1
                workingStrategyType: 1
                workingPegPriceType: PRIMARY_PEG
                workingPegOffsetType: PRICE_LEVEL
                workingPegOffsetValue: 1
                pendingType: LIMIT
                pendingSide: BUY
                pendingClientOrderId: pendingOrder1
                pendingPrice: 1
                pendingStopPrice: 1
                pendingTrailingDelta: 1
                pendingIcebergQty: 1
                pendingTimeInForce: GTC
                pendingStrategyId: 1
                pendingStrategyType: 1
                pendingPegPriceType: PRIMARY_PEG
                pendingPegOffsetType: PRICE_LEVEL
                pendingPegOffsetValue: 1
                workingQuoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: OPO
          x-description-cn: 请参见英文说明：OPO
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: eabb220d-1c53-4f8a-8bca-a1cd3594b3ce
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 2
                      contingencyType:
                        type: string
                        example: OTO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: OiOgqvRagBefpzdM5gjYX3
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1762941318142
                      symbol:
                        type: string
                        example: BTCUSDT
                      orders:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 2
                            clientOrderId: pUzhKBbc0ZVdMScIRAqitH
                          - symbol: BTCUSDT
                            orderId: 3
                            clientOrderId: x7ISSjywZxFXOdzwsThNnd
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 2
                            clientOrderId:
                              type: string
                              example: pUzhKBbc0ZVdMScIRAqitH
                      orderReports:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 2
                            orderListId: 2
                            clientOrderId: pUzhKBbc0ZVdMScIRAqitH
                            transactTime: 1762941318142
                            price: "101496.00000000"
                            origQty: "0.00070000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.00000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT
                            side: BUY
                            workingTime: 1762941318142
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            orderId: 3
                            orderListId: 2
                            clientOrderId: x7ISSjywZxFXOdzwsThNnd
                            transactTime: 1762941318142
                            price: "0.00000000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.00000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: PENDING_NEW
                            timeInForce: GTC
                            type: MARKET
                            side: SELL
                            workingTime: -1
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 2
                            orderListId:
                              type: integer
                              format: int64
                              example: 2
                            clientOrderId:
                              type: string
                              example: pUzhKBbc0ZVdMScIRAqitH
                            transactTime:
                              type: integer
                              format: int64
                              example: 1762941318142
                            price:
                              type: string
                              example: "101496.00000000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: LIMIT
                            side:
                              type: string
                              example: BUY
                            workingTime:
                              type: integer
                              format: int64
                              example: 1762941318142
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            origQty:
                              type: string
                              example: "0.00070000"
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "0.00000000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
  /orderList.place.opoco:
    post:
      summary: OPOCO (TRADE)
      x-summary-cn: 新订单列表 - OPOCO (TRADE)
      description: |-
        Place an [OPOCO](/products/spot/faqs/opo).

        * The working order must be `LIMIT` or `LIMIT_MAKER`.
      x-description-cn: |-
        发送一个 [OPOCO](/products/spot/faqs/opo) 订单。

        * 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
      tags:
        - trade
      operationId: orderListPlaceOpoco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-opoco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlaceOpoco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place_opoco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place_opoco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceOpocoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlaceOpoco/OrderListPlaceOpoco.go
      x-ip-weight: 1
      x-order-weight: 3
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place.opoco
                  example: orderList.place.opoco
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    listClientOrderId:
                      type: string
                      example: TVbG6ymkYMXTj7tczbOsBf
                      description: >-
                        Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order
                        list with the same `listClientOrderId` is accepted only when the previous one is filled or
                        completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`,
                        `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.
                      x-description-cn: >-
                        订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId`
                        的订单列表。`listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和
                        `pendingBelowClientOrderId` 不同。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Format of the JSON response. Supported values: [Order Response
                        Type](/products/spot/enums#orderresponsetype)
                      x-description-cn: JSON 响应格式。支持的数值：[订单返回类型](/products/spot/enums#orderresponsetype)
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的数值取决于交易对的配置。支持的数值：[STP模式](/products/spot/enums#stpmodes)
                    workingType:
                      type: string
                      enum:
                        - LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: "Supported values: `LIMIT`, `LIMIT_MAKER`"
                      x-description-cn: 支持的数值：`LIMIT`，`LIMIT_MAKER`
                    workingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值：[订单方向](/products/spot/enums#side)
                    workingClientOrderId:
                      type: string
                      example: workingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the working order. Automatically generated if not
                        sent.
                      x-description-cn: 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。
                    workingPrice:
                      type: number
                      format: float
                      example: 1
                      description: Price for the working order.
                      x-description-cn: 生效订单价格
                    workingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the working order.
                      x-description-cn: 设置生效订单的数量
                    workingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
                      x-description-cn: 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用
                    workingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值：[生效时间](/products/spot/enums#timeinforce)
                    workingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the working order within an order strategy.
                      x-description-cn: 用于标识订单策略中生效订单的任意数字值
                    workingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识生效订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。
                    workingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    workingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    workingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                      description: "Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)"
                      x-description-cn: 用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值：[订单方向](/products/spot/enums#side)
                    pendingAboveType:
                      type: string
                      enum:
                        - STOP_LOSS_LIMIT
                        - STOP_LOSS
                        - LIMIT_MAKER
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS_LIMIT
                      description: >-
                        Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`
                      x-description-cn: 支持的数值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`
                    pendingAboveClientOrderId:
                      type: string
                      example: pendingAboveOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending above order. Automatically generated if
                        not sent.
                      x-description-cn: 待处理"上方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。
                    pendingAbovePrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to
                        specify the limit price.
                      x-description-cn: 当 `pendingAboveType` 为 `STOP_LOSS_LIMIT`、`LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。
                    pendingAboveStopPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 当 `pendingAboveType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT`、`TAKE_PROFIT_LIMIT` 时可用。
                    pendingAboveTrailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)
                    pendingAboveIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        This can only be used if `pendingAboveTimeInForce` is `GTC` or `pendingAboveType` is
                        `LIMIT_MAKER`.
                      x-description-cn: 仅当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时可用。
                    pendingAboveTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。
                    pendingAboveStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending above order within an order strategy.
                      x-description-cn: 用于标识订单策略中待处理上方订单的任意数字值。
                    pendingAboveStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending above order strategy. Values smaller than
                        `1000000` are reserved and cannot be used.
                      x-description-cn: 用于标识待处理上方订单策略的任意数字值。小于 `1000000` 的值为保留值，不能使用。
                    pendingAbovePegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingAbovePegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingAbovePegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                      description: "Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)"
                      x-description-cn: 用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingBelowType:
                      type: string
                      enum:
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS
                      description: "Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`"
                      x-description-cn: 支持的数值：`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`
                    pendingBelowClientOrderId:
                      type: string
                      example: pendingBelowOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending below order. Automatically generated if
                        not sent.
                      x-description-cn: 待处理"下方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。
                    pendingBelowPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the
                        limit price.
                      x-description-cn: 当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。
                    pendingBelowStopPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must
                        be specified.
                      x-description-cn: >-
                        当 `pendingBelowType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT`
                        时可用。`pendingBelowStopPrice`、`pendingBelowTrailingDelta` 或两者之一必须被指定。
                    pendingBelowTrailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 详见 [追踪止盈止损常见问题](/products/spot/faqs/trailing-stop-faq)
                    pendingBelowIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        This can only be used if `pendingBelowTimeInForce` is `GTC` or `pendingBelowType` is
                        `LIMIT_MAKER`.
                      x-description-cn: 仅当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时可用。
                    pendingBelowTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值：[生效时间](/products/spot/enums#timeinforce)
                    pendingBelowStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending below order within an order strategy.
                      x-description-cn: 用于标识订单策略中待处理下方订单的任意数字值。
                    pendingBelowStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending below order strategy. Values smaller than
                        `1000000` are reserved and cannot be used.
                      x-description-cn: 用于标识待处理下方订单策略的任意数字值。小于 `1000000` 为保留值，不能使用。
                    pendingBelowPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingBelowPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    pendingBelowPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    workingQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the working LIMIT order on the BUY side. See [Quote Notional
                        Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 生效 LIMIT 买单的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - workingType
                    - workingSide
                    - workingPrice
                    - workingQuantity
                    - pendingSide
                    - pendingAboveType
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place.opoco
              params:
                symbol: BNBUSDT
                listClientOrderId: TVbG6ymkYMXTj7tczbOsBf
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                workingType: LIMIT
                workingSide: BUY
                workingClientOrderId: workingOrder1
                workingPrice: 1
                workingQuantity: 1
                workingIcebergQty: 1
                workingTimeInForce: GTC
                workingStrategyId: 1
                workingStrategyType: 1
                workingPegPriceType: PRIMARY_PEG
                workingPegOffsetType: PRICE_LEVEL
                workingPegOffsetValue: 1
                pendingSide: BUY
                pendingAboveType: STOP_LOSS_LIMIT
                pendingAboveClientOrderId: pendingAboveOrder1
                pendingAbovePrice: 1
                pendingAboveStopPrice: 1
                pendingAboveTrailingDelta: 1
                pendingAboveIcebergQty: 1
                pendingAboveTimeInForce: GTC
                pendingAboveStrategyId: 1
                pendingAboveStrategyType: 1
                pendingAbovePegPriceType: PRIMARY_PEG
                pendingAbovePegOffsetType: PRICE_LEVEL
                pendingAbovePegOffsetValue: 1
                pendingBelowType: STOP_LOSS
                pendingBelowClientOrderId: pendingBelowOrder1
                pendingBelowPrice: 1
                pendingBelowStopPrice: 1
                pendingBelowTrailingDelta: 1
                pendingBelowIcebergQty: 1
                pendingBelowTimeInForce: GTC
                pendingBelowStrategyId: 1
                pendingBelowStrategyType: 1
                pendingBelowPegPriceType: PRIMARY_PEG
                pendingBelowPegOffsetType: PRICE_LEVEL
                pendingBelowPegOffsetValue: 1
                workingQuoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: OPOCO
          x-description-cn: 请参见英文说明：OPOCO
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 606063bf-43ea-40a6-a463-5c66fbd53b56
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 1
                      contingencyType:
                        type: string
                        example: OTO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: TVbG6ymkYMXTj7tczbOsBf
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1763000139104
                      symbol:
                        type: string
                        example: BTCUSDT
                      orders:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 6
                            clientOrderId: 3czuJSeyjPwV9Xo28j1Dv3
                          - symbol: BTCUSDT
                            orderId: 7
                            clientOrderId: kyIKnMLKQclE5FmyYgaMSo
                          - symbol: BTCUSDT
                            orderId: 8
                            clientOrderId: i76cGJWN9J1FpADS56TtQZ
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 6
                            clientOrderId:
                              type: string
                              example: 3czuJSeyjPwV9Xo28j1Dv3
                      orderReports:
                        type: array
                        example:
                          - symbol: BTCUSDT
                            orderId: 6
                            orderListId: 1
                            clientOrderId: 3czuJSeyjPwV9Xo28j1Dv3
                            transactTime: 1763000139104
                            price: "102496.00000000"
                            origQty: "0.00170000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.00000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT
                            side: BUY
                            workingTime: 1763000139104
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            orderId: 7
                            orderListId: 1
                            clientOrderId: kyIKnMLKQclE5FmyYgaMSo
                            transactTime: 1763000139104
                            price: "101613.00000000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.00000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: PENDING_NEW
                            timeInForce: IOC
                            type: STOP_LOSS_LIMIT
                            side: SELL
                            stopPrice: "10100.00000000"
                            workingTime: -1
                            selfTradePreventionMode: NONE
                          - symbol: BTCUSDT
                            orderId: 8
                            orderListId: 1
                            clientOrderId: i76cGJWN9J1FpADS56TtQZ
                            transactTime: 1763000139104
                            price: "104261.00000000"
                            executedQty: "0.00000000"
                            origQuoteOrderQty: "0.00000000"
                            cummulativeQuoteQty: "0.00000000"
                            status: PENDING_NEW
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: SELL
                            workingTime: -1
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            orderId:
                              type: integer
                              format: int64
                              example: 6
                            orderListId:
                              type: integer
                              format: int64
                              example: 1
                            clientOrderId:
                              type: string
                              example: 3czuJSeyjPwV9Xo28j1Dv3
                            transactTime:
                              type: integer
                              format: int64
                              example: 1763000139104
                            price:
                              type: string
                              example: "102496.00000000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: LIMIT
                            side:
                              type: string
                              example: BUY
                            workingTime:
                              type: integer
                              format: int64
                              example: 1763000139104
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            stopPrice:
                              type: string
                              example: "10100.00000000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            origQty:
                              type: string
                              example: "0.00170000"
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
  /orderList.place.oto:
    post:
      summary: Place new Order list - OTO (TRADE)
      x-summary-cn: 发送新订单列表 - OTO (TRADE)
      description: |-
        Places an OTO.

        * An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.

        * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the
        working order goes on the order book.

        * The second order is called the **pending order**. It can be any order type except for `MARKET` orders using
        parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets
        **fully filled**.

        * If either the working order or the pending order is cancelled individually, the other order in the order list
        will also be canceled or expired.

        * When the order list is placed, if the working order gets **immediately fully filled**, the placement response
        will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to
        query the status of the pending order again to see its updated status.

        * OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送一个新的 OTO 订单。


        * 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.

        * 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。

        * 第二个订单被称为**待处理订单**。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET` 订单。只有当生效订单**完全成交**时，待处理订单才会被自动下单。

        * 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。

        * 如果生效订单在下订单列表后**立即完全成交**，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为
        `PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。

        * `OTO` 订单将**2 个订单**添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: orderListPlaceOto
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oto
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlaceOto.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place_oto.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place_oto.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceOtoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlaceOto/OrderListPlaceOto.go
      x-ip-weight: 1
      x-order-weight: 2
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        ::span{#mandatory-parameters-based-on-pendingtype-or-workingtype}


        **Mandatory parameters based on `pendingType` or `workingType`**


        Depending on the `pendingType` or `workingType`, some optional parameters will become mandatory.


        |Type                                                  |Additional mandatory parameters|Additional information|

        |----                                                  |----                           |------

        |`workingType` = `LIMIT`                               |`workingTimeInForce`           |

        |`pendingType` = `LIMIT`                                |`pendingPrice`, `pendingTimeInForce`          |

        |`pendingType` = `STOP_LOSS` or `TAKE_PROFIT`           |`pendingStopPrice` and/or `pendingTrailingDelta`|

        |`pendingType` =`STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`|`pendingPrice`, `pendingStopPrice` and/or
        `pendingTrailingDelta`, `pendingTimeInForce`|
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        ::span{#mandatory-parameters-based-on-pendingtype-or-workingtype}


        **根据 `pendingType` 或者 `workingType` 的不同值，对于某些参数的强制要求**


        根据 `pendingType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：


        |类型                                                   | 强制要求的参数                  | 其他信息|

        |----                                                  |----                           |------

        |`workingType` = `LIMIT`                               |`workingTimeInForce`           |

        |`pendingType` = `LIMIT`                                |`pendingPrice`， `pendingTimeInForce`          |

        |`pendingType` = `STOP_LOSS` 或 `TAKE_PROFIT`           |`pendingStopPrice` 与/或 `pendingTrailingDelta`|

        |`pendingType` = `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`|`pendingPrice`， `pendingStopPrice` 与/或
        `pendingTrailingDelta`， `pendingTimeInForce`|
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place.oto
                  example: orderList.place.oto
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    listClientOrderId:
                      type: string
                      example: KA4EBjGnzvSwSCQsDdTrlf
                      description: >-
                        Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order
                        list with the same `listClientOrderId` is accepted only when the previous one is filled or
                        completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the
                        `pendingClientOrderId`.
                      x-description-cn: >-
                        整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。
                        `listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Format of the JSON response. Supported values: [Order Response
                        Type](/products/spot/enums#orderresponsetype)
                      x-description-cn: 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)
                    workingType:
                      type: string
                      enum:
                        - LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: "Supported values: `LIMIT`, `LIMIT_MAKER`"
                      x-description-cn: 支持的数值： `LIMIT`， `LIMIT_MAKER`
                    workingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值： [订单方向](/products/spot/enums#side)
                    workingClientOrderId:
                      type: string
                      example: workingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the working order. Automatically generated if not
                        sent.
                      x-description-cn: 用于标识生效订单的唯一ID。 如果未发送则自动生成。
                    workingPrice:
                      type: number
                      format: float
                      example: 1
                    workingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the working order.
                      x-description-cn: 用于设置生效订单的数量。
                    workingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
                      x-description-cn: 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。
                    workingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值： [生效时间](/products/spot/enums#timeinforce)
                    workingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the working order within an order strategy.
                      x-description-cn: 订单策略中用于标识生效订单的 ID。
                    workingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
                    workingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    workingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    workingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    pendingType:
                      type: string
                      enum:
                        - LIMIT
                        - MARKET
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: >-
                        Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders
                        using `quoteOrderQty` are not supported.
                      x-description-cn: 支持的数值： [订单类型](/products/spot/enums#ordertypes) 请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。
                    pendingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值： [订单方向](/products/spot/enums#side)
                    pendingClientOrderId:
                      type: string
                      example: pendingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending order. Automatically generated if not
                        sent.
                      x-description-cn: 用于标识待处理订单的唯一ID。 如果未发送则自动生成。
                    pendingPrice:
                      type: number
                      format: float
                      example: 1
                    pendingStopPrice:
                      type: number
                      format: float
                      example: 1
                    pendingTrailingDelta:
                      type: number
                      format: float
                      example: 1
                    pendingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the pending order.
                      x-description-cn: 用于设置待处理订单的数量。
                    pendingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.
                      x-description-cn: 只有当 `pendingTimeInForce` 为 `GTC` 或者当 `pendingType` 为 `LIMIT_MAKER` 时才能使用。
                    pendingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值： [生效时间](/products/spot/enums#timeinforce)
                    pendingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending order within an order strategy.
                      x-description-cn: 订单策略中用于标识待处理订单的 ID。
                    pendingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识待处理订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
                    pendingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    pendingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    workingQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the working order (only for orders on the BUY side). See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    pendingQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the pending order (only for orders on the BUY side). See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 待处理订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - workingType
                    - workingSide
                    - workingPrice
                    - workingQuantity
                    - pendingType
                    - pendingSide
                    - pendingQuantity
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place.oto
              params:
                symbol: BNBUSDT
                listClientOrderId: KA4EBjGnzvSwSCQsDdTrlf
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                workingType: LIMIT
                workingSide: BUY
                workingClientOrderId: workingOrder1
                workingPrice: 1
                workingQuantity: 1
                workingIcebergQty: 1
                workingTimeInForce: GTC
                workingStrategyId: 1
                workingStrategyType: 1
                workingPegPriceType: PRIMARY_PEG
                workingPegOffsetType: PRICE_LEVEL
                workingPegOffsetValue: 1
                pendingType: LIMIT
                pendingSide: BUY
                pendingClientOrderId: pendingOrder1
                pendingPrice: 1
                pendingStopPrice: 1
                pendingTrailingDelta: 1
                pendingQuantity: 1
                pendingIcebergQty: 1
                pendingTimeInForce: GTC
                pendingStrategyId: 1
                pendingStrategyType: 1
                pendingPegOffsetType: PRICE_LEVEL
                pendingPegPriceType: PRIMARY_PEG
                pendingPegOffsetValue: 1
                workingQuoteNotionalLimit: 100
                pendingQuoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Place new Order list - OTO
          x-description-cn: 发送新订单列表 - OTO
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: "1712544395950"
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 626
                      contingencyType:
                        type: string
                        example: OTO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: KA4EBjGnzvSwSCQsDdTrlf
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1712544395981
                      symbol:
                        type: string
                        example: LTCBNB
                      orders:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 13
                            clientOrderId: YiAUtM9yJjl1a2jXHSp9Ny
                          - symbol: LTCBNB
                            orderId: 14
                            clientOrderId: 9MxJSE1TYkmyx5lbGLve7R
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 13
                            clientOrderId:
                              type: string
                              example: YiAUtM9yJjl1a2jXHSp9Ny
                      orderReports:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 13
                            orderListId: 626
                            clientOrderId: YiAUtM9yJjl1a2jXHSp9Ny
                            transactTime: 1712544395981
                            price: "1.000000"
                            origQty: "1.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT
                            side: SELL
                            workingTime: 1712544395981
                            selfTradePreventionMode: NONE
                          - symbol: LTCBNB
                            orderId: 14
                            orderListId: 626
                            clientOrderId: 9MxJSE1TYkmyx5lbGLve7R
                            transactTime: 1712544395981
                            price: "0.000000"
                            origQty: "1.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.000000"
                            status: PENDING_NEW
                            timeInForce: GTC
                            type: MARKET
                            side: BUY
                            workingTime: -1
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 13
                            orderListId:
                              type: integer
                              format: int64
                              example: 626
                            clientOrderId:
                              type: string
                              example: YiAUtM9yJjl1a2jXHSp9Ny
                            transactTime:
                              type: integer
                              format: int64
                              example: 1712544395981
                            price:
                              type: string
                              example: "1.00000000"
                            origQty:
                              type: string
                              example: "1.000000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: LIMIT
                            side:
                              type: string
                              example: SELL
                            workingTime:
                              type: integer
                              format: int64
                              example: 1712544395981
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "0.00000000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: MINUTE
                        intervalNum: 1
                        limit: 10000000
                        count: 10
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 1000
                        count: 38
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /orderList.place.otoco:
    post:
      summary: Place new Order list - OTOCO (TRADE)
      x-summary-cn: 发送新订单列表 - OTOCO (TRADE)
      description: >-
        Place an OTOCO.


        * An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.

        * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the
        working order goes on the order book.
          * The behavior of the working order is the same as the [OTO](#order-list-place-oto).
        * OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only
        placed on the order book when the working order gets **fully filled**.
          * The rules of the pending above and pending below follow the same rules as the [Order list OCO](/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oco).
        * OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送一个新的 OTOCO 订单。

        * 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
        * 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
          * 生效订单的行为与此一致 [OTO](#orderList-place-oto)
        * 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交**时，待处理订单们才会被自动下单。
          * 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [OrderList OCO](/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-oco)。
        * `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单**。
      tags:
        - trade
      operationId: orderListPlaceOtoco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-list-place-otoco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderListPlaceOtoco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_list_place_otoco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_list_place_otoco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderListPlaceOtocoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderListPlaceOtoco/OrderListPlaceOtoco.go
      x-ip-weight: 1
      x-order-weight: 3
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        ::span{#mandatory-parameters-based-on-pendingabovetype-pendingbelowtype-or-workingtype}


        **Mandatory parameters based on `pendingAboveType`, `pendingBelowType` or `workingType`**


        Depending on the `pendingAboveType`/`pendingBelowType` or `workingType`, some optional parameters will become
        mandatory.


        |Type                                                       |Additional mandatory parameters|Additional
        information|

        |----                                                       |----                           |------

        |`workingType` = `LIMIT`                                    |`workingTimeInForce`           |

        |`pendingAboveType`= `LIMIT_MAKER`                                |`pendingAbovePrice`          |

        |`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`         |`pendingAboveStopPrice` and/or
        `pendingAboveTrailingDelta`|

        |`pendingAboveType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`|`pendingAbovePrice`, `pendingAboveStopPrice` and/or
        `pendingAboveTrailingDelta`, `pendingAboveTimeInForce`|

        |`pendingBelowType`= `LIMIT_MAKER`                                |`pendingBelowPrice`          |

        `pendingBelowType= STOP_LOSS/TAKE_PROFIT`         |`pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`|

        |`pendingBelowType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`|`pendingBelowPrice`, `pendingBelowStopPrice` and/or
        `pendingBelowTrailingDelta`, `pendingBelowTimeInForce`|
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        ::span{#mandatory-parameters-based-on-pendingabovetype-pendingbelowtype-or-workingtype}


        根据 `pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：


        |类型                                                        | 强制要求的参数                  | 其他信息|

        |----                                                       |----                           |------

        |`workingType` = `LIMIT`                                    |`workingTimeInForce`           |

        |`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT` | `pendingAboveStopPrice` 与/或  `pendingAboveTrailingDelta` |

        |`pendingAboveType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` | `pendingAbovePrice`， `pendingAboveStopPrice` 与/或
        `pendingAboveTrailingDelta`， `pendingAboveTimeInForce` |

        |`pendingAboveType` = `LIMIT_MAKER`                                |`pendingAbovePrice`     |

        |`pendingBelowType` = `STOP_LOSS/TAKE_PROFIT` | `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta` |

        |`pendingBelowType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` | `pendingBelowPrice`， `pendingBelowStopPrice` 与/或
        `pendingBelowTrailingDelta`， `pendingBelowTimeInForce` |

        |`pendingBelowType` = `LIMIT_MAKER`                                |`pendingBelowPrice`          |
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - orderList.place.otoco
                  example: orderList.place.otoco
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    listClientOrderId:
                      type: string
                      example: GaeJHjZPasPItFj4x7Mqm6
                      description: >-
                        Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order
                        list with the same `listClientOrderId` is accepted only when the previous one is filled or
                        completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`,
                        `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.
                      x-description-cn: >-
                        整个订单列表的唯一ID。 如果未发送则自动生成。 仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。
                        `listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和
                        `pendingBelowClientOrderId` 不同。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Format of the JSON response. Supported values: [Order Response
                        Type](/products/spot/enums#orderresponsetype)
                      x-description-cn: 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/products/spot/enums#orderresponsetype)
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的数值取决于交易对上的配置。参考 [STP 模式](/products/spot/enums#stpmodes)
                    workingType:
                      type: string
                      enum:
                        - LIMIT
                        - LIMIT_MAKER
                      example: LIMIT
                      description: "Supported values: `LIMIT`, `LIMIT_MAKER`"
                      x-description-cn: 支持的数值： `LIMIT`， `LIMIT_MAKER`
                    workingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值： [订单方向](/products/spot/enums#side)
                    workingClientOrderId:
                      type: string
                      example: workingOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the working order. Automatically generated if not
                        sent.
                      x-description-cn: 用于标识生效订单的唯一ID。 如果未发送则自动生成。
                    workingPrice:
                      type: number
                      format: float
                      example: 1
                    workingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the working order.
                      x-description-cn: 用于设置生效订单的数量。
                    workingIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
                      x-description-cn: 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。
                    workingTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: "Supported values: [Time In Force](/products/spot/enums#timeinforce)"
                      x-description-cn: 支持的数值： [生效时间](/products/spot/enums#timeinforce)
                    workingStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the working order within an order strategy.
                      x-description-cn: 订单策略中用于标识生效订单的 ID。
                    workingStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000`
                        are reserved and cannot be used.
                      x-description-cn: 用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
                    workingPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    workingPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    workingPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    pendingSide:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "Supported values: [Order Side](/products/spot/enums#side)"
                      x-description-cn: 支持的数值： [订单方向](/products/spot/enums#side)
                    pendingQuantity:
                      type: number
                      format: float
                      example: 1
                      description: Sets the quantity for the pending orders.
                      x-description-cn: 用于设置待处理订单的数量。
                    pendingAboveType:
                      type: string
                      enum:
                        - STOP_LOSS_LIMIT
                        - STOP_LOSS
                        - LIMIT_MAKER
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS_LIMIT
                      description: >-
                        Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`
                      x-description-cn: 支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
                    pendingAboveClientOrderId:
                      type: string
                      example: pendingAboveOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending above order. Automatically generated if
                        not sent.
                      x-description-cn: 用于标识待处理上方订单的唯一ID。 如果未发送则自动生成。
                    pendingAbovePrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to
                        specify the limit price.
                      x-description-cn: 当 `pendingAboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                    pendingAboveStopPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `pendingAboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。
                    pendingAboveTrailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    pendingAboveIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is
                        `LIMIT_MAKER`.
                      x-description-cn: 只有当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时才能使用。
                    pendingAboveTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Required if `pendingAboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `pendingAboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。
                    pendingAboveStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending above order within an order strategy.
                      x-description-cn: 订单策略中用于标识待处理上方订单的 ID。
                    pendingAboveStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending above order strategy. Values smaller than
                        `1000000` are reserved and cannot be used.
                      x-description-cn: 用于标识待处理上方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
                    pendingAbovePegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingAbovePegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    pendingAbovePegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    pendingBelowType:
                      type: string
                      enum:
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                      example: STOP_LOSS
                      description: "Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`"
                      x-description-cn: 支持的数值： `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
                    pendingBelowClientOrderId:
                      type: string
                      example: pendingBelowOrder1
                      description: >-
                        Arbitrary unique ID among open orders for the pending below order. Automatically generated if
                        not sent.
                      x-description-cn: 用于标识待处理下方订单的唯一ID。 如果未发送则自动生成。
                    pendingBelowPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the
                        limit price.
                      x-description-cn: 当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                    pendingBelowStopPrice:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must
                        be specified.
                      x-description-cn: >-
                        如果 `pendingBelowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。
                        必须指定 `pendingBelowStopPrice` 或 `pendingBelowTrailingDelta` 或两者。
                    pendingBelowTrailingDelta:
                      type: number
                      format: float
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    pendingBelowIcebergQty:
                      type: number
                      format: float
                      example: 1
                      description: >-
                        This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is
                        `LIMIT_MAKER`.
                      x-description-cn: 只有当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时才能使用。
                    pendingBelowTimeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Required if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
                      x-description-cn: 如果 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。
                    pendingBelowStrategyId:
                      type: integer
                      format: int64
                      example: 1
                      description: Arbitrary numeric value identifying the pending below order within an order strategy.
                      x-description-cn: 订单策略中用于标识待处理下方订单的 ID。
                    pendingBelowStrategyType:
                      type: integer
                      example: 1
                      description: >-
                        Arbitrary numeric value identifying the pending below order strategy. Values smaller than
                        `1000000` are reserved and cannot be used.
                      x-description-cn: 用于标识待处理下方订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
                    pendingBelowPegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pendingBelowPegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                    pendingBelowPegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                    workingQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the working order (only for orders on the BUY side). See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    pendingAboveQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the pending above order (only for orders on the BUY side). See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 待处理上方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    pendingBelowQuoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        Quote notional limit for the pending below order (only for orders on the BUY side). See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 待处理下方订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - workingType
                    - workingSide
                    - workingPrice
                    - workingQuantity
                    - pendingSide
                    - pendingQuantity
                    - pendingAboveType
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: orderList.place.otoco
              params:
                symbol: BNBUSDT
                listClientOrderId: GaeJHjZPasPItFj4x7Mqm6
                newOrderRespType: ACK
                selfTradePreventionMode: NONE
                workingType: LIMIT
                workingSide: BUY
                workingClientOrderId: workingOrder1
                workingPrice: 1
                workingQuantity: 1
                workingIcebergQty: 1
                workingTimeInForce: GTC
                workingStrategyId: 1
                workingStrategyType: 1
                workingPegPriceType: PRIMARY_PEG
                workingPegOffsetType: PRICE_LEVEL
                workingPegOffsetValue: 1
                pendingSide: BUY
                pendingQuantity: 1
                pendingAboveType: STOP_LOSS_LIMIT
                pendingAboveClientOrderId: pendingAboveOrder1
                pendingAbovePrice: 1
                pendingAboveStopPrice: 1
                pendingAboveTrailingDelta: 1
                pendingAboveIcebergQty: 1
                pendingAboveTimeInForce: GTC
                pendingAboveStrategyId: 1
                pendingAboveStrategyType: 1
                pendingAbovePegPriceType: PRIMARY_PEG
                pendingAbovePegOffsetType: PRICE_LEVEL
                pendingAbovePegOffsetValue: 1
                pendingBelowType: STOP_LOSS
                pendingBelowClientOrderId: pendingBelowOrder1
                pendingBelowPrice: 1
                pendingBelowStopPrice: 1
                pendingBelowTrailingDelta: 1
                pendingBelowIcebergQty: 1
                pendingBelowTimeInForce: GTC
                pendingBelowStrategyId: 1
                pendingBelowStrategyType: 1
                pendingBelowPegPriceType: PRIMARY_PEG
                pendingBelowPegOffsetType: PRICE_LEVEL
                pendingBelowPegOffsetValue: 1
                workingQuoteNotionalLimit: 100
                pendingAboveQuoteNotionalLimit: 100
                pendingBelowQuoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/web-socket-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/web-socket-api#conditional-fields-in-order-responses) 部分。
      responses:
        Successful Response:
          description: Place new Order list - OTOCO
          x-description-cn: 发送新订单列表 - OTOCO
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: "1712544408508"
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      orderListId:
                        type: integer
                        format: int64
                        example: 629
                      contingencyType:
                        type: string
                        example: OTO
                      listStatusType:
                        type: string
                        example: EXEC_STARTED
                      listOrderStatus:
                        type: string
                        example: EXECUTING
                      listClientOrderId:
                        type: string
                        example: GaeJHjZPasPItFj4x7Mqm6
                      transactionTime:
                        type: integer
                        format: int64
                        example: 1712544408537
                      symbol:
                        type: string
                        example: LTCBNB
                      orders:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 23
                            clientOrderId: OVQOpKwfmPCfaBTD0n7e7H
                          - symbol: LTCBNB
                            orderId: 24
                            clientOrderId: YcCPKCDMQIjNvLtNswt82X
                          - symbol: LTCBNB
                            orderId: 25
                            clientOrderId: ilpIoShcFZ1ZGgSASKxMPt
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 23
                            clientOrderId:
                              type: string
                              example: OVQOpKwfmPCfaBTD0n7e7H
                      orderReports:
                        type: array
                        example:
                          - symbol: LTCBNB
                            orderId: 23
                            orderListId: 629
                            clientOrderId: OVQOpKwfmPCfaBTD0n7e7H
                            transactTime: 1712544408537
                            price: "1.500000"
                            origQty: "1.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.000000"
                            status: NEW
                            timeInForce: GTC
                            type: LIMIT
                            side: BUY
                            workingTime: 1712544408537
                            selfTradePreventionMode: NONE
                          - symbol: LTCBNB
                            orderId: 24
                            orderListId: 629
                            clientOrderId: YcCPKCDMQIjNvLtNswt82X
                            transactTime: 1712544408537
                            price: "0.000000"
                            origQty: "5.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.000000"
                            status: PENDING_NEW
                            timeInForce: GTC
                            type: STOP_LOSS
                            side: SELL
                            stopPrice: "0.500000"
                            workingTime: -1
                            selfTradePreventionMode: NONE
                          - symbol: LTCBNB
                            orderId: 25
                            orderListId: 629
                            clientOrderId: ilpIoShcFZ1ZGgSASKxMPt
                            transactTime: 1712544408537
                            price: "5.000000"
                            origQty: "5.000000"
                            executedQty: "0.000000"
                            origQuoteOrderQty: "0.000000"
                            cummulativeQuoteQty: "0.000000"
                            status: PENDING_NEW
                            timeInForce: GTC
                            type: LIMIT_MAKER
                            side: SELL
                            workingTime: -1
                            selfTradePreventionMode: NONE
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: LTCBNB
                            orderId:
                              type: integer
                              format: int64
                              example: 23
                            orderListId:
                              type: integer
                              format: int64
                              example: 629
                            clientOrderId:
                              type: string
                              example: OVQOpKwfmPCfaBTD0n7e7H
                            transactTime:
                              type: integer
                              format: int64
                              example: 1712544408537
                            price:
                              type: string
                              example: "1.50000000"
                            origQty:
                              type: string
                              example: "1.000000"
                            executedQty:
                              type: string
                              example: "0.00000000"
                            origQuoteOrderQty:
                              type: string
                              example: "0.000000"
                            cummulativeQuoteQty:
                              type: string
                              example: "0.00000000"
                            status:
                              type: string
                              example: NEW
                            timeInForce:
                              type: string
                              example: GTC
                            type:
                              type: string
                              example: LIMIT
                            side:
                              type: string
                              example: BUY
                            workingTime:
                              type: integer
                              format: int64
                              example: 1712544408537
                            selfTradePreventionMode:
                              type: string
                              example: NONE
                            icebergQty:
                              type: string
                              example: "0.00000000"
                              description: Appears only if the parameter icebergQty was sent in the request.
                              x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                            preventedMatchId:
                              type: integer
                              format: int64
                              example: 0
                              description: Appears only if the order expired due to STP.
                              x-description-cn: 仅在因 STP 导致订单失效时出现。
                            preventedQuantity:
                              type: string
                              example: "1.200000"
                              description: Order quantity that expired due to STP.
                              x-description-cn: 因 STP 导致订单失效的数量。
                            stopPrice:
                              type: string
                              example: "0.500000"
                              description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                              x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                            strategyId:
                              type: integer
                              format: int64
                              example: 1
                              description: Appears only if the strategyId parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                            strategyType:
                              type: integer
                              format: int64
                              example: 1000000
                              description: Appears only if the strategyType parameter was provided upon order placement.
                              x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                            trailingDelta:
                              type: integer
                              format: int64
                              example: 10
                              description: Delta price change required before order activation.
                              x-description-cn: 订单激活前所需的价格变动。
                            trailingTime:
                              type: integer
                              format: int64
                              example: -1
                              description: Time when the trailing order is now active and tracking price changes.
                              x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                            usedSor:
                              type: boolean
                              example: true
                              description: Field that determines whether order used SOR.
                              x-description-cn: 用于确定订单是否使用SOR的字段。
                            workingFloor:
                              type: string
                              example: SOR
                              description: Determines whether the order is being filled by the SOR or by the order book.
                              x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                            pegPriceType:
                              type: string
                              example: PRIMARY_PEG
                              description: Price peg type. Only for pegged orders.
                              x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                            pegOffsetType:
                              type: string
                              example: PRICE_LEVEL
                              description: Price peg offset type. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                            pegOffsetValue:
                              type: integer
                              format: int64
                              example: 5
                              description: Price peg offset value. Only for pegged orders, if requested.
                              x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                            peggedPrice:
                              type: string
                              example: "87523.83710000"
                              description: Current price order is pegged at. Only for pegged orders, once determined.
                              x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                            expiryReason:
                              type: string
                              example: INSUFFICIENT_LIQUIDITY
                              description: Cause of the order's expiration. Appears when an order has expired.
                              x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    example:
                      - rateLimitType: ORDERS
                        interval: MINUTE
                        intervalNum: 1
                        limit: 10000000
                        count: 18
                      - rateLimitType: REQUEST_WEIGHT
                        interval: MINUTE
                        intervalNum: 1
                        limit: 1000
                        count: 65
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /order.place:
    post:
      summary: Place new order (TRADE)
      x-summary-cn: 下新的订单 (TRADE)
      description: |-
        Send in a new order.

        This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        下新的订单。

        这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: orderPlace
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-place
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderPlace.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_place.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_place.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderPlaceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderPlace/OrderPlace.go
      x-ip-weight: 1
      x-order-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        <a id="order-type">Certain parameters (*)</a> become mandatory based on the order `type`:


        <table>

        <thead>
            <tr>
                <th>Order <code>type</code></th>
                <th>Mandatory parameters</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td><code>LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>LIMIT_MAKER</code></td>
                <td>
                <ul>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>MARKET</code></td>
                <td>
                <ul>
                    <li><code>quantity</code> or <code>quoteOrderQty</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS</code></td>
                <td>
                <ul>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> or <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS_LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> or <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT</code></td>
                <td>
                <ul>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> or <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT_LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> or <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
        </tbody>

        </table>


        Supported order types:


        <table>

        <thead>
            <tr>
                <th>Order <code>type</code></th>
                <th>Description</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td><code>LIMIT</code></td>
                <td>
                <p>
                    Buy or sell <code>quantity</code> at the specified <code>price</code> or better.
                </p>
                </td>
            </tr>
            <tr>
                <td><code>LIMIT_MAKER</code></td>
                <td>
                <p>
                    <code>LIMIT</code> order that will be rejected if it immediately matches and trades as a taker.
                </p>
                <p>
                    This order type is also known as a POST-ONLY order.
                </p>
                </td>
            </tr>
            <tr>
                <td><code>MARKET</code></td>
                <td>
                <p>
                    Buy or sell at the best available market price.
                </p>
                <ul>
                    <li>
                        <p>
                            <code>MARKET</code> order with <code>quantity</code> parameter
                            specifies the amount of the <em>base asset</em> you want to buy or sell.
                            Actually executed quantity of the quote asset will be determined by available market liquidity.
                        </p>
                        <p>
                            E.g., a MARKET BUY order on BTCUSDT for <code>"quantity": "0.1000"</code>
                            specifies that you want to buy 0.1 BTC at the best available price.
                            If there is not enough BTC at the best price, keep buying at the next best price,
                            until either your order is filled, or you run out of USDT, or market runs out of BTC.
                        </p>
                    </li>
                    <li>
                        <p>
                            <code>MARKET</code> order with <code>quoteOrderQty</code> parameter
                            specifies the amount of the <em>quote asset</em> you want to spend (when buying) or receive (when selling).
                            Actually executed quantity of the base asset will be determined by available market liquidity.
                        </p>
                        <p>
                            E.g., a MARKET BUY on BTCUSDT for <code>"quoteOrderQty": "100.00"</code>
                            specifies that you want to buy as much BTC as you can for 100 USDT at the best available price.
                            Similarly, a SELL order will sell as much available BTC as needed for you to receive 100 USDT
                            (before commission).
                        </p>
                    </li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS</code></td>
                <td>
                <p>
                    Execute a <code>MARKET</code> order for given <code>quantity</code> when specified conditions are met.
                </p>
                <p>
                    I.e., when <code>stopPrice</code> is reached, or when <code>trailingDelta</code> is activated.
                </p>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS_LIMIT</code></td>
                <td>
                <p>
                    Place a <code>LIMIT</code> order with given parameters when specified conditions are met.
                </p>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT</code></td>
                <td>
                <p>
                    Like <code>STOP_LOSS</code> but activates when market price moves in the favorable direction.
                </p>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT_LIMIT</code></td>
                <td>
                <p>
                    Like <code>STOP_LOSS_LIMIT</code> but activates when market price moves in the favorable direction.
                </p>
                </td>
            </tr>
        </tbody>

        </table>


        ::span{#pegged-orders-info}

        Notes on using parameters for Pegged Orders:


        * These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.

        * If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.

        * `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as
        your order.

        * `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book
        from your order.

        * Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters
        must be specified together.


        ::span{#timeInForce}


        Available `timeInForce` options,

        setting how long the order should be active before expiration:


        TIF  | Description

        ----- | --------------

        `GTC` | **Good 'til Canceled** – the order will remain on the book until you cancel it, or the order is
        completely filled.

        `IOC` | **Immediate or Cancel** – the order will be filled for as much as possible, the unfilled quantity
        immediately expires.

        `FOK` | **Fill or Kill** – the order will expire unless it cannot be immediately filled for the entire quantity.


        Notes:


        * `newClientOrderId` specifies `clientOrderId` value for the order.

          A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

        * Any `LIMIT` or `LIMIT_MAKER` order can be made into an iceberg order by specifying the `icebergQty`.

          An order with an `icebergQty` must have `timeInForce` set to `GTC`.

        * Trigger order price rules for `STOP_LOSS`/`TAKE_PROFIT` orders:

          * `stopPrice` must be above market price: `STOP_LOSS BUY`, `TAKE_PROFIT SELL`
          * `stopPrice` must be below market price: `STOP_LOSS SELL`, `TAKE_PROFIT BUY`

        * `MARKET` orders using `quoteOrderQty` follow [`LOT_SIZE`](/products/spot/filters#lot_size) filter rules.

          The order will execute a quantity that has notional value as close as possible to requested `quoteOrderQty`.
      x-parameters-notes-cn: |-
        **数据源:** 撮合引擎

        根据订单 `type`，<a id="order-type">某些参数(*)</a> 可能成为必需参数:

        <table>
        <thead>
            <tr>
                <th>订单 <code>type</code></th>
                <th>强制要求的参数</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>LIMIT_MAKER</code></td>
                <td>
                <ul>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>MARKET</code></td>
                <td>
                <ul>
                    <li><code>quantity</code> 或者 <code>quoteOrderQty</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS</code></td>
                <td>
                <ul>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> 或者 <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS_LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> 或者 <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT</code></td>
                <td>
                <ul>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> 或者 <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT_LIMIT</code></td>
                <td>
                <ul>
                    <li><code>timeInForce</code></li>
                    <li><code>price</code></li>
                    <li><code>quantity</code></li>
                    <li><code>stopPrice</code> 或者 <code>trailingDelta</code></li>
                </ul>
                </td>
            </tr>
        </tbody>
        </table>

        支持的订单类型：

        <table>
        <thead>
            <tr>
                <th>订单 <code>type</code></th>
                <th>描述</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>LIMIT</code></td>
                <td>
                <p>
                    以指定的 <code>price</code> 或更好的 <code>price</code>, 买入或卖出 <code>quantity</code>。
                </p>
                </td>
            </tr>
            <tr>
                <td><code>LIMIT_MAKER</code></td>
                <td>
                <p>
                    <code>LIMIT</code> 订单，如果它立即匹配并成为吃单方将被拒绝。
                </p>
                <p>
                    此订单类型也称为 POST-ONLY 订单。
                </p>
                </td>
            </tr>
            <tr>
                <td><code>MARKET</code></td>
                <td>
                <p>
                    以最佳市场价格买入或卖出。
                </p>
                <ul>
                    <li>
                        <p>
                            带有 <code>quantity</code> 参数的 <code>MARKET</code> 订单指定您要BUY或SELL的<em>base asset</em>的数量。
                            报价资产的实际执行quantity将取决于可用的市场流动性。
                        </p>
                        <p>
                            例如，在 BTCUSDT 下<code> "quantity": "0.1000" </code> 的市场买单，指定您想以最优惠的价格 BUY 0.1 BTC。
                            如果以最优价格没有足够的 BTC，会继续以次优价格买入，直到您的订单被执行，或者您的 USDT 用完，或者市场上的 BTC 用完。
                        </p>
                    </li>
                    <li>
                        <p>
                            使用 <code>quoteOrderQty</code> 的 <code>MARKET</code> 订单 明确的是通过买入(或卖出)想要花费(或获取)的 <em>quote asset</em> 数量。
                            基础资产的实际执行数量将取决于可用的市场流动性。
                        </p>
                        <p>
                            例如，在 BTCUSDT 下 <code> "quoteOrderQty": "100.00" </code> 的市场买单，指定您想以最优惠的价格以 100 USDT 购买尽可能多的 BTC。
                            同样，卖出订单将卖出尽可能多的可用 BTC，以便您获得 100 USDT（佣金前）。
                        </p>
                    </li>
                </ul>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS</code></td>
                <td>
                <p>
                    当满足指定条件时，执行给定 <code>quantity</code> 的 <code>MARKET</code> 订单。
                </p>
                <p>
                    I.e., 当达到 <code>stopPrice</code> 或激活 <code>trailingDelta</code> 时。
                </p>
                </td>
            </tr>
            <tr>
                <td><code>STOP_LOSS_LIMIT</code></td>
                <td>
                <p>
                    当满足指定条件时，执行给定参数的 <code>LIMIT</code> 订单。
                </p>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT</code></td>
                <td>
                <p>
                    与 <code>STOP_LOSS</code> 类似，但在市场价格向有利方向移动时激活。
                </p>
                </td>
            </tr>
            <tr>
                <td><code>TAKE_PROFIT_LIMIT</code></td>
                <td>
                <p>
                    与 <code>STOP_LOSS_LIMIT</code> 类似，但在市场价格向有利方向移动时激活。
                </p>
                </td>
            </tr>
        </tbody>
        </table>

        ::span{#pegged-orders-info}
        关于挂钩订单参数的注意事项：

        * 这些参数仅适用于 `LIMIT`， `LIMIT_MAKER`， `STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。
        * 如果使用了 `pegPriceType`， 那么 `price` 字段将是可选的。 否则，`price` 字段依旧是必须的。
        * `pegPriceType=PRIMARY_PEG` 就是主要挂钩（`primary`），这是订单簿上与您的订单同一方向的最佳价格。
        * `pegPriceType=MARKET_PEG` 就是市场挂钩（`market`），这是订单簿上与您的订单相反方向的最佳价格。
        * 可以通过使用 `pegOffsetType` 和 `pegOffsetValue` 来获取最佳价格以外的价格水平。 这两个参数必须一起使用。

        ::span{#timeInForce}

        可用的 `timeInForce` 选项，设置订单在到期前应该活跃多长时间：

        TIF  | 描述
        ----- | --------------
        `GTC` | **Good 'til Canceled** – 成交为止。订单会一直有效，直到被成交或者取消。
        `IOC` | **Immediate 或者 Cancel** – 无法立即成交的部分就撤销。订单在失效前会尽量多的成交。
        `FOK` | **Fill 或者 Kill** – 无法全部立即成交就撤销。如果无法全部成交，订单会失效。

        备注：

        * `newClientOrderId` 指定订单的 `clientOrderId` 值。

          仅当前一个订单已成交或过期时，才会接受具有相同 `clientOrderId` 的新订单。

        * 任何 `LIMIT` 或 `LIMIT_MAKER` 订单都可以通过指定 `icebergQty` 变成冰山订单。

          带有 `icebergQty` 的订单必须将 `timeInForce` 设置为 `GTC`。

        * `STOP_LOSS`/`TAKE_PROFIT` 订单的触发订单价格规则：

          * `stopPrice` 必须高于市场价格：`STOP_LOSS BUY`，`TAKE_PROFIT SELL`
          * `stopPrice` 必须低于市场价格：`STOP_LOSS SELL`，`TAKE_PROFIT BUY`

        * 使用 `quoteOrderQty` 的 `MARKET` 订单遵循 [`LOT_SIZE`](/products/spot/filters#lot_size) 过滤规则。

          该订单将执行一个名义价值尽可能接近请求的 `quoteOrderQty` 的数量。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.place
                  example: order.place
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: Please see [Enums](/products/spot/enums#side) for supported values.
                      x-description-cn: 详见枚举定义：[订单方向](/products/spot/enums#side)
                    type:
                      type: string
                      enum:
                        - MARKET
                        - LIMIT
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                        - LIMIT_MAKER
                      example: MARKET
                      description: Please see [Enums](/products/spot/enums#ordertypes) for supported values.
                      x-description-cn: 详见枚举定义：[订单类型](/products/spot/enums#ordertypes)
                    timeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Please see [Enums](/products/spot/enums#timeinforce) for supported values.
                      x-description-cn: 详见枚举定义：[生效时间](/products/spot/enums#timeinforce)
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    quoteOrderQty:
                      type: number
                      format: float
                      example: 1
                    newClientOrderId:
                      type: string
                      example: myOrder1
                      description: >-
                        A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same
                        `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order
                        will be rejected.
                      x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: "`MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`."
                      x-description-cn: "`MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。"
                    stopPrice:
                      type: number
                      format: float
                      example: 1
                      description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                      x-description-cn: 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。
                    trailingDelta:
                      type: integer
                      example: 1
                      description: See Trailing Stop order FAQ
                      x-description-cn: 参见 追踪止盈止损(Trailing Stop)订单常见问题
                    icebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
                      x-description-cn: 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                    strategyId:
                      type: integer
                      format: int64
                      example: 1
                    strategyType:
                      type: integer
                      example: 1
                      minimum: 1000000
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 不能低于 `1000000`。
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: The allowed enums is dependent on what is configured on the symbol.
                      x-description-cn: 允许的 ENUM 取决于交易对的配置。
                    pegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: See Pegged Orders Info
                      x-description-cn: 参阅 关于挂钩订单参数的注意事项
                    pegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                      description: "Price level to peg the price to (max: 100). See Pegged Orders Info"
                      x-description-cn: 用于挂钩的价格水平（最大值：100）。参阅 关于挂钩订单参数的注意事项
                    pegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                      description: Only `PRICE_LEVEL` is supported. See Pegged Orders Info
                      x-description-cn: 仅支持 `PRICE_LEVEL`。参阅 关于挂钩订单参数的注意事项
                    quoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - type
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.place
              params:
                symbol: BNBUSDT
                side: BUY
                type: MARKET
                timeInForce: GTC
                price: 1
                quantity: 1
                quoteOrderQty: 1
                newClientOrderId: myOrder1
                newOrderRespType: ACK
                stopPrice: 1
                trailingDelta: 1
                icebergQty: 1
                strategyId: 1
                strategyType: 1
                selfTradePreventionMode: NONE
                pegPriceType: PRIMARY_PEG
                pegOffsetValue: 1
                pegOffsetType: PRICE_LEVEL
                quoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Place new order
          x-description-cn: 下新的订单
          content:
            application/json:
              schema:
                oneOf:
                  - description: |-
                      Response format is selected by using the `newOrderRespType` parameter.
                      `ACK` response type:
                    x-description-cn: |-
                      使用 `newOrderRespType` 参数可以选择响应格式。
                      `ACK` 响应类型：
                    type: object
                    properties:
                      id:
                        type: string
                        example: 56374a46-3061-486b-a311-99ee972eb648
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            description: always -1 for singular orders
                            x-description-cn: 单个订单会一直是 -1
                            example: -1
                          clientOrderId:
                            type: string
                            example: 4d96324ff9d44481926157ec08158a40
                          transactTime:
                            type: integer
                            format: int64
                            example: 1660801715639
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                  - description: "`RESULT` response type:"
                    x-description-cn: "`RESULT` 响应类型："
                    type: object
                    properties:
                      id:
                        type: string
                        example: 56374a46-3061-486b-a311-99ee972eb648
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            description: always -1 for singular orders
                            x-description-cn: 单个订单会一直是 -1
                            example: -1
                          clientOrderId:
                            type: string
                            example: 4d96324ff9d44481926157ec08158a40
                          transactTime:
                            type: integer
                            format: int64
                            example: 1660801715639
                          price:
                            type: string
                            example: "23416.10000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00000000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "0.00000000"
                          status:
                            type: string
                            example: NEW
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          workingTime:
                            type: integer
                            format: int64
                            example: 1660801715639
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: ORDERS
                            interval:
                              type: string
                              example: SECOND
                            intervalNum:
                              type: integer
                              format: int64
                              example: 10
                            limit:
                              type: integer
                              format: int64
                              example: 50
                            count:
                              type: integer
                              format: int64
                              example: 1
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                  - description: "`FULL` response type:"
                    x-description-cn: "`FULL` 响应类型："
                    type: object
                    properties:
                      id:
                        type: string
                        example: 56374a46-3061-486b-a311-99ee972eb648
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 12569099453
                          orderListId:
                            type: integer
                            format: int64
                            example: -1
                          clientOrderId:
                            type: string
                            example: 4d96324ff9d44481926157ec08158a40
                          transactTime:
                            type: integer
                            format: int64
                            example: 1660801715793
                          price:
                            type: string
                            example: "23416.10000000"
                          origQty:
                            type: string
                            example: "0.00847000"
                          executedQty:
                            type: string
                            example: "0.00847000"
                          origQuoteOrderQty:
                            type: string
                            example: "0.000000"
                          cummulativeQuoteQty:
                            type: string
                            example: "198.33521500"
                          status:
                            type: string
                            example: FILLED
                          timeInForce:
                            type: string
                            example: GTC
                          type:
                            type: string
                            example: LIMIT
                          side:
                            type: string
                            example: SELL
                          workingTime:
                            type: integer
                            format: int64
                            example: 1660801715639
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                          stopPrice:
                            type: string
                            example: "0.00000000"
                            description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                            x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                          trailingDelta:
                            type: integer
                            format: int64
                            example: 10
                            description: Delta price change required before order activation.
                            x-description-cn: 订单激活前所需的价格变动。
                          icebergQty:
                            type: string
                            example: "0.00000000"
                            description: Appears only if the parameter icebergQty was sent in the request.
                            x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                          strategyId:
                            type: integer
                            format: int64
                            example: 1
                            description: Appears only if the strategyId parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                          strategyType:
                            type: integer
                            format: int64
                            example: 1000000
                            description: Appears only if the strategyType parameter was provided upon order placement.
                            x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                          preventedMatchId:
                            type: integer
                            format: int64
                            example: 0
                            description: Appears only if the order expired due to STP.
                            x-description-cn: 仅在因 STP 导致订单失效时出现。
                          preventedQuantity:
                            type: string
                            example: "1.200000"
                            description: Order quantity that expired due to STP.
                            x-description-cn: 因 STP 导致订单失效的数量。
                          trailingTime:
                            type: integer
                            format: int64
                            example: -1
                            description: Time when the trailing order is now active and tracking price changes.
                            x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                          usedSor:
                            type: boolean
                            example: true
                            description: Field that determines whether order used SOR.
                            x-description-cn: 用于确定订单是否使用SOR的字段。
                          workingFloor:
                            type: string
                            example: SOR
                            description: Determines whether the order is being filled by the SOR or by the order book.
                            x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                          pegPriceType:
                            type: string
                            example: PRIMARY_PEG
                            description: Price peg type. Only for pegged orders.
                            x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                          pegOffsetType:
                            type: string
                            example: PRICE_LEVEL
                            description: Price peg offset type. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                          pegOffsetValue:
                            type: integer
                            format: int64
                            example: 5
                            description: Price peg offset value. Only for pegged orders, if requested.
                            x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                          peggedPrice:
                            type: string
                            example: "87523.83710000"
                            description: Current price order is pegged at. Only for pegged orders, once determined.
                            x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                          expiryReason:
                            type: string
                            example: INSUFFICIENT_LIQUIDITY
                            description: Cause of the order's expiration. Appears when an order has expired.
                            x-description-cn: 订单过期的原因。当订单过期时出现。
                          fills:
                            type: array
                            description: |-
                              FULL response is identical to RESULT response, with the same optional fields
                              based on the order type and parameters. FULL response additionally includes
                              the list of trades which immediately filled the order.
                            x-description-cn: FULL 响应与 RESULT 响应相同，具有相同的可选字段基于订单类型和参数。FULL响应还包括立即完成订单的交易列表。
                            example:
                              - price: "23416.10000000"
                                qty: "0.00635000"
                                commission: "0.000000"
                                commissionAsset: BNB
                                tradeId: 1650422481
                              - price: "23416.50000000"
                                qty: "0.00212000"
                                commission: "0.000000"
                                commissionAsset: BNB
                                tradeId: 1650422482
                            items:
                              type: object
                              properties:
                                price:
                                  type: string
                                  example: "23416.10000000"
                                qty:
                                  type: string
                                  example: "0.00635000"
                                commission:
                                  type: string
                                  example: "0.00000000"
                                commissionAsset:
                                  type: string
                                  example: BNB
                                tradeId:
                                  type: integer
                                  format: int64
                                  example: 1650422481
                      rateLimits:
                        type: array
                        example:
                          - rateLimitType: ORDERS
                            interval: SECOND
                            intervalNum: 10
                            limit: 50
                            count: 1
                          - rateLimitType: ORDERS
                            interval: DAY
                            intervalNum: 1
                            limit: 160000
                            count: 1
                          - rateLimitType: REQUEST_WEIGHT
                            interval: MINUTE
                            intervalNum: 1
                            limit: 6000
                            count: 1
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
  /order.test:
    post:
      summary: Test new order (TRADE)
      x-summary-cn: 测试下单 (TRADE)
      description: |-
        Test order placement.

        Validates new order parameters and verifies your signature
        but does not send the order into the matching engine.
      x-description-cn: |-
        测试下单。

        验证新订单参数并验证您的签名但不会将订单发送到撮合引擎。
      tags:
        - trade
      operationId: orderTest
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-test
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/orderTest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/order_test.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/order_test.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/OrderTestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/OrderTest/OrderTest.go
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        | Condition | Request Weight |
        | --- | --- |
        | Without `computeCommissionRates` | 1 |
        | With `computeCommissionRates` | 20 |
      x-weight-cn: |-
        | 条件 | 请求权重 |
        | --- | --- |
        | 没有 `computeCommissionRates` | 1 |
        | 有 `computeCommissionRates` | 20 |
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.test
                  example: order.test
                params:
                  type: object
                  properties:
                    computeCommissionRates:
                      type: boolean
                      example: false
                      default: false
                      description: >-
                        Default: `false` <br> See [Commissions
                        FAQ](/products/spot/faqs/commission_faq#test-order-diferences) to learn more.
                      x-description-cn: >-
                        默认值: `false` <br> 请参阅[佣金常见问题解答](/products/spot/faqs/commission_faq#test-order-diferences)
                        了解更多信息。
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: Please see [Enums](/products/spot/enums#side) for supported values.
                      x-description-cn: 详见枚举定义：[订单方向](/products/spot/enums#side)
                    type:
                      type: string
                      enum:
                        - MARKET
                        - LIMIT
                        - STOP_LOSS
                        - STOP_LOSS_LIMIT
                        - TAKE_PROFIT
                        - TAKE_PROFIT_LIMIT
                        - LIMIT_MAKER
                      example: MARKET
                      description: Please see [Enums](/products/spot/enums#ordertypes) for supported values.
                      x-description-cn: 详见枚举定义：[订单类型](/products/spot/enums#ordertypes)
                    timeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Please see [Enums](/products/spot/enums#timeinforce) for supported values.
                      x-description-cn: 详见枚举定义：[生效时间](/products/spot/enums#timeinforce)
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    quoteOrderQty:
                      type: number
                      format: float
                      example: 1
                    newClientOrderId:
                      type: string
                      example: myOrder1
                      description: >-
                        A unique id among open orders. Automatically generated if not sent. Orders with the same
                        `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order
                        will be rejected.
                      x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: >-
                        Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to
                        `FULL`, all other orders default to `ACK`.
                      x-description-cn: 指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。
                    stopPrice:
                      type: number
                      format: float
                      example: 1
                      description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                      x-description-cn: 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。
                    trailingDelta:
                      type: integer
                      example: 1
                      description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                      x-description-cn: 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                    icebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
                      x-description-cn: 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                    strategyId:
                      type: integer
                      format: int64
                      example: 1
                    strategyType:
                      type: integer
                      example: 1
                      minimum: 1000000
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 不能低于 `1000000`。
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                    pegPriceType:
                      type: string
                      enum:
                        - PRIMARY_PEG
                        - MARKET_PEG
                      example: PRIMARY_PEG
                      description: "`PRIMARY_PEG` or `MARKET_PEG`. See [Pegged Orders](/products/spot/faqs/pegged_orders)"
                      x-description-cn: "`PRIMARY_PEG` 或 `MARKET_PEG`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)"
                    pegOffsetValue:
                      type: integer
                      example: 1
                      maximum: 100
                      description: "Price level for pegging (max: 100). See [Pegged Orders](/products/spot/faqs/pegged_orders)"
                      x-description-cn: 用于挂钩的价格水平（最大值：100）。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    pegOffsetType:
                      type: string
                      enum:
                        - PRICE_LEVEL
                      example: PRICE_LEVEL
                      description: Only `PRICE_LEVEL` is supported. See [Pegged Orders](/products/spot/faqs/pegged_orders)
                      x-description-cn: 仅支持 `PRICE_LEVEL`。 参阅 [关于挂钩订单参数的注意事项](/products/spot/faqs/pegged_orders)
                    quoteNotionalLimit:
                      type: number
                      format: float
                      example: 100
                      description: >-
                        For orders on the BUY side only. Maximum quote-asset notional the order may consume. See [Quote
                        Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                      x-description-cn: 仅适用于买单。订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - type
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: order.test
              params:
                computeCommissionRates: false
                symbol: BNBUSDT
                side: BUY
                type: MARKET
                timeInForce: GTC
                price: 1
                quantity: 1
                quoteOrderQty: 1
                newClientOrderId: myOrder1
                newOrderRespType: ACK
                stopPrice: 1
                trailingDelta: 1
                icebergQty: 1
                strategyId: 1
                strategyType: 1
                selfTradePreventionMode: NONE
                pegPriceType: PRIMARY_PEG
                pegOffsetValue: 1
                pegOffsetType: PRICE_LEVEL
                quoteNotionalLimit: 100
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Test new order
          x-description-cn: 测试下单
          content:
            application/json:
              schema:
                oneOf:
                  - description: "Without `computeCommissionRates`:"
                    x-description-cn: "没有 `computeCommissionRates`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: 6ffebe91-01d9-43ac-be99-57cf062e0e30
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties: {}
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
                  - description: "With `computeCommissionRates`:"
                    x-description-cn: "有 `computeCommissionRates`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: 6ffebe91-01d9-43ac-be99-57cf062e0e30
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          standardCommissionForOrder:
                            type: object
                            description: Standard commission rates on trades from the order.
                            x-description-cn: 订单交易的标准佣金率。
                            properties:
                              maker:
                                type: string
                                example: "0.00000112"
                              taker:
                                type: string
                                example: "0.00000114"
                          specialCommissionForOrder:
                            type: object
                            description: Special commission rates on trades from the order.
                            x-description-cn: 订单交易的特殊佣金率。
                            properties:
                              maker:
                                type: string
                                example: "0.05000000"
                              taker:
                                type: string
                                example: "0.06000000"
                          taxCommissionForOrder:
                            type: object
                            description: Tax commission rates for trades from the order.
                            x-description-cn: 订单交易的税率。
                            properties:
                              maker:
                                type: string
                                example: "0.00000112"
                              taker:
                                type: string
                                example: "0.00000114"
                          discount:
                            type: object
                            description: Discount on standard commissions when paying in BNB.
                            x-description-cn: 以BNB支付时的标准佣金折扣。
                            properties:
                              enabledForAccount:
                                type: boolean
                                example: true
                              enabledForSymbol:
                                type: boolean
                                example: true
                              discountAsset:
                                type: string
                                example: BNB
                              discount:
                                type: string
                                description: Standard commission is reduced by this rate when paying commission in BNB.
                                x-description-cn: 当用BNB支付佣金时，在标准佣金上按此比率打折。
                                example: "0.25000000"
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 20
  /sor.order.place:
    post:
      summary: Place new order using SOR (TRADE)
      x-summary-cn: 下 SOR 订单 (TRADE)
      description: |-
        Places an order using smart order routing (SOR).

        This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

        Read [SOR FAQ](/products/spot/faqs/sor_faq) to learn more.
      x-description-cn: |-
        发送使用智能订单路由 (SOR) 的新订单。这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

        参阅 [智能订单路由 (SOR)](/products/spot/faqs/sor_faq) 了解更多详情。
      tags:
        - trade
      operationId: sorOrderPlace
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#sor-order-place
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/sorOrderPlace.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/sor_order_place.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/sor_order_place.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/SorOrderPlaceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/SorOrderPlace/SorOrderPlace.go
      x-ip-weight: 1
      x-legacy-anchors:
        - sor
      x-order-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: |-
        **Data Source:** Matching Engine

        **Note:** `sor.order.place` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.
      x-parameters-notes-cn: |-
        **数据源:** 撮合引擎

        **注意:** `sor.order.place` 只支持 `限价` 和 `市场` 单， 并不支持 `quoteOrderQty`。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - sor.order.place
                  example: sor.order.place
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: "`BUY` or `SELL`"
                      x-description-cn: "`BUY` 或 `SELL`"
                    type:
                      type: string
                      enum:
                        - MARKET
                        - LIMIT
                      example: MARKET
                      description: Only `LIMIT` and `MARKET` orders are supported.
                      x-description-cn: 仅支持 `LIMIT` 和 `MARKET` 订单。
                    timeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Applicable only to `LIMIT` order type.
                      x-description-cn: 仅适用于 `LIMIT` 订单类型。
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    newClientOrderId:
                      type: string
                      example: myOrder1
                      description: >-
                        A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same
                        `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order
                        will be rejected.
                      x-description-cn: >-
                        用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID`
                        赋值，<br/>那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`
                      x-description-cn: "指定响应类型:"
                    icebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `LIMIT` to create an iceberg order.
                      x-description-cn: 仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                    strategyId:
                      type: integer
                      format: int64
                      example: 1
                    strategyType:
                      type: integer
                      example: 1
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 赋值不能小于 `1000000`.
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. The possible supported
                        values are: [STP Modes](/products/spot/enums#stpmodes).
                      x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - type
                    - quantity
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: sor.order.place
              params:
                symbol: BNBUSDT
                side: BUY
                type: MARKET
                timeInForce: GTC
                price: 1
                quantity: 1
                newClientOrderId: myOrder1
                newOrderRespType: ACK
                icebergQty: 1
                strategyId: 1
                strategyType: 1
                selfTradePreventionMode: NONE
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Place new order using SOR
          x-description-cn: 下 SOR 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 3a4437e2-41a3-4c19-897c-9cadc5dce8b6
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        orderId:
                          type: integer
                          format: int64
                          example: 2
                        orderListId:
                          type: integer
                          format: int64
                          example: -1
                        clientOrderId:
                          type: string
                          example: sBI1KM6nNtOfj5tccZSKly
                        transactTime:
                          type: integer
                          format: int64
                          example: 1689149087774
                        price:
                          type: string
                          example: "31000.00000000"
                        origQty:
                          type: string
                          example: "0.50000000"
                        executedQty:
                          type: string
                          example: "0.50000000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.000000"
                        cummulativeQuoteQty:
                          type: string
                          example: "14000.00000000"
                        status:
                          type: string
                          example: FILLED
                        timeInForce:
                          type: string
                          example: GTC
                        type:
                          type: string
                          example: LIMIT
                        side:
                          type: string
                          example: BUY
                        workingTime:
                          type: integer
                          format: int64
                          example: 1689149087774
                        fills:
                          type: array
                          items:
                            type: object
                            properties:
                              matchType:
                                type: string
                                example: ONE_PARTY_TRADE_REPORT
                              price:
                                type: string
                                example: "28000.00000000"
                              qty:
                                type: string
                                example: "0.50000000"
                              commission:
                                type: string
                                example: "0.00000000"
                              commissionAsset:
                                type: string
                                example: BTC
                              tradeId:
                                type: integer
                                format: int64
                                example: -1
                              allocId:
                                type: integer
                                format: int64
                                example: 0
                        workingFloor:
                          type: string
                          example: SOR
                          description: Determines whether the order is being filled by the SOR or by the order book.
                          x-description-cn: 用以定义订单是通过 SOR 还是由订单簿成交的。
                        selfTradePreventionMode:
                          type: string
                          example: NONE
                        usedSor:
                          type: boolean
                          example: true
                          description: Field that determines whether order used SOR.
                          x-description-cn: 用于确定订单是否使用SOR的字段。
                        stopPrice:
                          type: string
                          example: "0.00000000"
                          description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                          x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                        trailingDelta:
                          type: integer
                          format: int64
                          example: 10
                          description: Delta price change required before order activation.
                          x-description-cn: 订单激活前所需的价格变动。
                        icebergQty:
                          type: string
                          example: "0.00000000"
                          description: Appears only if the parameter icebergQty was sent in the request.
                          x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                        strategyId:
                          type: integer
                          format: int64
                          example: 1
                          description: Appears only if the strategyId parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyId 参数时出现。
                        strategyType:
                          type: integer
                          format: int64
                          example: 1000000
                          description: Appears only if the strategyType parameter was provided upon order placement.
                          x-description-cn: 仅在下单时提供了 strategyType 参数时出现。
                        preventedMatchId:
                          type: integer
                          format: int64
                          example: 0
                          description: Appears only if the order expired due to STP.
                          x-description-cn: 仅在因 STP 导致订单失效时出现。
                        preventedQuantity:
                          type: string
                          example: "1.200000"
                          description: Order quantity that expired due to STP.
                          x-description-cn: 因 STP 导致订单失效的数量。
                        trailingTime:
                          type: integer
                          format: int64
                          example: -1
                          description: Time when the trailing order is now active and tracking price changes.
                          x-description-cn: 追踪单被激活和跟踪价格变化的时间。
                        pegPriceType:
                          type: string
                          example: PRIMARY_PEG
                          description: Price peg type. Only for pegged orders.
                          x-description-cn: 挂钩价格类型。仅用于挂钩订单。
                        pegOffsetType:
                          type: string
                          example: PRICE_LEVEL
                          description: Price peg offset type. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移类型。如若需要，仅用于挂钩订单。
                        pegOffsetValue:
                          type: integer
                          format: int64
                          example: 5
                          description: Price peg offset value. Only for pegged orders, if requested.
                          x-description-cn: 挂钩价格偏移值。如若需要，仅用于挂钩订单。
                        peggedPrice:
                          type: string
                          example: "87523.83710000"
                          description: Current price order is pegged at. Only for pegged orders, once determined.
                          x-description-cn: 订单对应的当前挂钩价格。一旦确定，仅用于挂钩订单。
                        expiryReason:
                          type: string
                          example: INSUFFICIENT_LIQUIDITY
                          description: Cause of the order's expiration. Appears when an order has expired.
                          x-description-cn: 订单过期的原因。当订单过期时出现。
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                        interval:
                          type: string
                          example: MINUTE
                        intervalNum:
                          type: integer
                          format: int64
                          example: 1
                        limit:
                          type: integer
                          format: int64
                          example: 6000
                        count:
                          type: integer
                          format: int64
                          example: 1
  /sor.order.test:
    post:
      summary: Test new order using SOR (TRADE)
      x-summary-cn: 测试 SOR 下单接口 (TRADE)
      description: |-
        Test new order creation and signature/recvWindow using smart order routing (SOR).
        Creates and validates a new order but does not send it into the matching engine.
      x-description-cn: 用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎。
      tags:
        - trade
      operationId: sorOrderTest
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#sor-order-test
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/TradeApi/sorOrderTest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/trade_api/sor_order_test.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/Trade/sor_order_test.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/trade/SorOrderTestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/TradeAPI/SorOrderTest/SorOrderTest.go
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        | Condition | Request Weight |
        | --- | --- |
        | Without `computeCommissionRates` | 1 |
        | With `computeCommissionRates` | 20 |
      x-weight-cn: |-
        | 条件 | 请求权重 |
        | --- | --- |
        | 没有 `computeCommissionRates` | 1 |
        | 有 `computeCommissionRates` | 20 |
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - sor.order.test
                  example: sor.order.test
                params:
                  type: object
                  properties:
                    computeCommissionRates:
                      type: boolean
                      example: false
                      default: false
                      description: "Default: `false`"
                      x-description-cn: "默认值: `false`"
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      enum:
                        - BUY
                        - SELL
                      example: BUY
                      description: Please see [Enums](/products/spot/enums#side) for supported values.
                      x-description-cn: 详见枚举定义：[订单方向](/products/spot/enums#side)
                    type:
                      type: string
                      enum:
                        - MARKET
                        - LIMIT
                      example: MARKET
                      description: Please see [Enums](/products/spot/enums#ordertypes) for supported values.
                      x-description-cn: 详见枚举定义：[订单类型](/products/spot/enums#ordertypes)
                    timeInForce:
                      type: string
                      enum:
                        - GTC
                        - IOC
                        - FOK
                      example: GTC
                      description: Please see [Enums](/products/spot/enums#timeinforce) for supported values.
                      x-description-cn: 详见枚举定义：[生效时间](/products/spot/enums#timeinforce)
                    price:
                      type: number
                      format: float
                      example: 1
                    quantity:
                      type: number
                      format: float
                      example: 1
                    newClientOrderId:
                      type: string
                      example: myOrder1
                      description: >-
                        A unique id among open orders. Automatically generated if not sent. Orders with the same
                        `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order
                        will be rejected.
                      x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。
                    newOrderRespType:
                      type: string
                      enum:
                        - ACK
                        - RESULT
                        - FULL
                      example: ACK
                      description: Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`.
                      x-description-cn: "指定响应类型: `ACK`, `RESULT` 或 `FULL`; 默认为 `FULL`。"
                    icebergQty:
                      type: number
                      format: float
                      example: 1
                      description: Used with `LIMIT` to create an iceberg order.
                      x-description-cn: 仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                    strategyId:
                      type: integer
                      format: int64
                      example: 1
                    strategyType:
                      type: integer
                      example: 1
                      description: The value cannot be less than `1000000`.
                      x-description-cn: 赋值不能小于 `1000000`。
                    selfTradePreventionMode:
                      type: string
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_MAKER
                        - EXPIRE_BOTH
                        - DECREMENT
                        - TRANSFER
                      example: NONE
                      description: >-
                        The allowed enums is dependent on what is configured on the symbol. Supported values: [STP
                        Modes](/products/spot/enums#stpmodes)
                      x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    apiKey:
                      type: string
                      description: >-
                        An API Key is required to access this endpoint and must be included in the request headers. To
                        create an API Key, refer to:
                        [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
                      x-description-cn: >-
                        访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
                        Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
                      example: API_KEY
                  additionalProperties: false
                  required:
                    - symbol
                    - side
                    - type
                    - quantity
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: sor.order.test
              params:
                computeCommissionRates: false
                symbol: BNBUSDT
                side: BUY
                type: MARKET
                timeInForce: GTC
                price: 1
                quantity: 1
                newClientOrderId: myOrder1
                newOrderRespType: ACK
                icebergQty: 1
                strategyId: 1
                strategyType: 1
                selfTradePreventionMode: NONE
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Test new order using SOR
          x-description-cn: 测试 SOR 下单接口
          content:
            application/json:
              schema:
                oneOf:
                  - description: "Without `computeCommissionRates`:"
                    x-description-cn: "没有 `computeCommissionRates`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: 3a4437e2-41a3-4c19-897c-9cadc5dce8b6
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties: {}
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 1
                  - description: "With `computeCommissionRates`:"
                    x-description-cn: "有 `computeCommissionRates`:"
                    type: object
                    properties:
                      id:
                        type: string
                        example: 3a4437e2-41a3-4c19-897c-9cadc5dce8b6
                      status:
                        type: integer
                        format: int64
                        example: 200
                      result:
                        type: object
                        properties:
                          standardCommissionForOrder:
                            type: object
                            description: Standard commission rates on trades from the order.
                            x-description-cn: 订单交易的标准佣金率。
                            properties:
                              maker:
                                type: string
                                example: "0.00000112"
                              taker:
                                type: string
                                example: "0.00000114"
                          taxCommissionForOrder:
                            type: object
                            description: Tax commission rates for trades from the order.
                            x-description-cn: 订单交易的税率。
                            properties:
                              maker:
                                type: string
                                example: "0.00000112"
                              taker:
                                type: string
                                example: "0.00000114"
                          discount:
                            type: object
                            description: Discount on standard commissions when paying in BNB.
                            x-description-cn: 以BNB支付时的标准佣金折扣。
                            properties:
                              enabledForAccount:
                                type: boolean
                                example: true
                              enabledForSymbol:
                                type: boolean
                                example: true
                              discountAsset:
                                type: string
                                example: BNB
                              discount:
                                type: string
                                description: Standard commission is reduced by this rate when paying commission in BNB.
                                x-description-cn: 当用BNB支付佣金时，在标准佣金上按此比率打折。
                                example: "0.25000000"
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            rateLimitType:
                              type: string
                              example: REQUEST_WEIGHT
                            interval:
                              type: string
                              example: MINUTE
                            intervalNum:
                              type: integer
                              format: int64
                              example: 1
                            limit:
                              type: integer
                              format: int64
                              example: 6000
                            count:
                              type: integer
                              format: int64
                              example: 20
  /session.subscriptions:
    post:
      summary: Listing all subscriptions
      x-summary-cn: 显示所有订阅
      description: |-
        **Note:**

        * Users should track the corresponding subscription status of related accounts as needed.
      x-description-cn: |-
        **注意：**

        * 用户按需要跟踪相关帐户的对应订阅情况。
      tags:
        - user-data-stream
      operationId: sessionSubscriptions
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#session-subscriptions
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/UserDataStreamApi/sessionSubscriptions.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/user_data_stream_api/session_subscriptions.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/UserDataStream/session_subscriptions.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/userdatastream/SessionSubscriptionsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/UserDataStreamAPI/SessionSubscriptions/SessionSubscriptions.go
      x-ip-weight: 2
      x-legacy-anchors:
        - session-subscription
      x-security-type: NONE
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - session.subscriptions
                  example: session.subscriptions
                params:
                  type: object
                  properties: {}
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: session.subscriptions
      responses:
        Successful Response:
          description: Listing all subscriptions
          x-description-cn: 显示所有订阅
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: array
                    example:
                      - subscriptionId: 0
                      - subscriptionId: 1
                    items:
                      type: object
                      properties:
                        subscriptionId:
                          type: integer
                          format: int64
                          example: 0
  /userDataStream.subscribe:
    post:
      summary: Subscribe to User Data Stream (USER_STREAM)
      x-summary-cn: 订阅用户数据流 (USER_STREAM)
      description: |-
        Subscribe to the User Data Stream in the current WebSocket connection.

        **Notes:**
          - This method requires an authenticated WebSocket connection using Ed25519 keys. Please refer to [`session.logon`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon).
          - To check the subscription status, use [`session.status`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-status), see the `userDataStream` flag indicating you have an active subscription.
          - User Data Stream events are available in both JSON and [SBE](/products/spot/faqs/sbe_faq) sessions.
            - Please refer to [User Data Streams](/products/spot/user-data-stream) for the event format details.
            - For SBE, only SBE schema 2:1 or later is supported.
      x-description-cn: |-
        订阅当前 WebSocket 连接中的用户数据流。

        **注意：**
          - 此方法需要使用 Ed25519 密钥并经过鉴权的 WebSocket 连接。请参考 [`session.logon`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon)。
          - 如果需要查看订阅状态，可以通过 [`session.status`](/catalog/core-trading-spot-trading/api/ws-api/auth#session-status) 查询，当 `userDataStream` 字段值为 `true` 时，表示您有一个有效的订阅。
          - 用户数据流在 JSON 和 [SBE 会话](/products/spot/faqs/sbe_faq) 中均可用。
            - 有关事件格式详情，请参阅 [用户数据流](/products/spot/user-data-stream)。
            - 对于 SBE，仅支持 SBE 模式 2:1 或更高版本。
      tags:
        - user-data-stream
      operationId: userDataStreamSubscribe
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/UserDataStreamApi/userDataStreamSubscribe.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/user_data_stream_api/user_data_stream_subscribe.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/UserDataStream/user_data_stream_subscribe.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/userdatastream/UserDataStreamSubscribeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/UserDataStreamAPI/UserDataStreamSubscribe/UserDataStreamSubscribe.go
      x-ip-weight: 2
      x-security-type: USER_STREAM
      x-parameters-notes: >-
        ::span{#user-data-stream-subscription-filters}

        **User Data Stream Subscription Filters**


        The optional `filter` parameter accepted by
        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
        and
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
        controls which events are delivered on the subscription. Without a filter, all events for the subscribed account
        are delivered. The filter object must contain at least one key when present; empty objects and empty arrays are
        rejected.


        Filters use the short field names that appear in event payloads. Within a filter key, values are logically ORed
        (match any). Across filter keys, matches are logically ANDed (an event must pass every specified filter).
        Filters that don't apply to an event type are ignored - the event passes through.


        **Available filter keys:**


        Key | Field | Values | Applies to | Bypass behavior

        --- | ----- | ------ | ---------- | ---------------

        `e` | Event type | camelCase event type names | All events | -

        `s` | Symbol | Instrument symbol names (e.g. `BTCUSDT`) | Events that carry a symbol field | Events without a
        symbol (`balanceUpdate`, `outboundAccountPosition`, `externalLockUpdate`) are delivered regardless.

        `a` | Asset | Asset names (e.g. `BTC`, `USDT`) | Events that carry an asset field | Events without an asset
        (`executionReport`, `listStatus`, `outboundAccountPosition`) are delivered regardless.

        `x` | Execution type | `SCREAMING_SNAKE_CASE` execution types | `executionReport` events only | All
        non-`executionReport` events are delivered regardless.


        **Event type values (`e`):**


        Value | Description

        ----- | -----------

        `executionReport` | Order lifecycle events (new, trade, cancel, expire, amend)

        `balanceUpdate` | Balance credit/debit (deposits, withdrawals)

        `outboundAccountPosition` | Account position snapshot after a change

        `listStatus` | Order list (OCO, OTO, OTOCO, OPO, OPOCO) status updates

        `externalLockUpdate` | External lock balance changes


        **Execution type values (`x`):**


        Value | Description

        ----- | -----------

        `NEW` | New order accepted

        `TRADE` | Order filled (partial or full)

        `CANCELED` | Order canceled

        `REPLACED` | Order replaced (cancel-replace)

        `REJECTED` | Order rejected

        `EXPIRED` | Order expired

        `TRADE_PREVENTION` | Self-trade prevention triggered


        **Examples:**


        Only execution reports and balance updates:


        ```javascript

        { "filter": { "e": ["executionReport", "balanceUpdate"] } }

        ```


        Only events for BTCUSDT and ETHUSDT:


        ```javascript

        { "filter": { "s": ["BTCUSDT", "ETHUSDT"] } }

        ```


        Only balance updates for BTC:


        ```javascript

        { "filter": { "e": ["balanceUpdate"], "a": ["BTC"] } }

        ```


        Only fills on execution reports:


        ```javascript

        { "filter": { "e": ["executionReport"], "x": ["TRADE"] } }

        ```


        **Validation rules:**


        Condition | Result

        --------- | ------

        `filter` omitted | All events delivered (no filter)

        `filter: {}` | Error: empty filter object

        `filter: {"e": []}` | Error: empty value array

        `filter: {"e": ["executionReport", "executionReport"]}` | Error: duplicate value

        `filter: {"e": ["badType"]}` | Error: unrecognized event type

        `filter: {"s": ["NOSYMBOL"]}` | Error: unknown symbol ([`-1121`](/products/spot/errors#-1121-bad_symbol))

        `filter: {"a": ["NOASSET"]}` | Error: unknown asset ([`-1108`](/products/spot/errors#-1108-bad_asset))

        `filter: {"z": [...]}` | Error: unknown filter key


        **Notes:**


        * `listenKeyExpired` and `eventStreamTerminated` lifecycle events are always delivered regardless of filters.

        * When using `userDataStream.subscribe.signature`, the `filter` must be included in the string that is signed.
        For the signature to match:
          * Filter keys must be sorted alphabetically: `a`, `e`, `s`, `x`.
          * There must be no whitespace between JSON elements of the filter.

          Example parameter string being signed:

          ```
          apiKey=...&filter={"e":["executionReport"],"s":["BAZUSD"],"x":["TRADE"]}&timestamp=...
          ```

        * When extending a signature subscription by re-subscribing with a new request, the active filter is replaced
        with the one in the new request.
      x-parameters-notes-cn: >-
        ::span{#user-data-stream-subscription-filters}

        **用户数据流订阅过滤器**


        [`userDataStream.subscribe`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)
        和
        [`userDataStream.subscribe.signature`](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature)
        接受可选参数 `filter`，用于控制该订阅推送哪些事件。未设置过滤器时，会推送所订阅账户的所有事件。如果提供了过滤器对象，则必须至少包含一个键；空对象和空数组都会被拒绝。


        过滤器使用事件负载中出现的字段简称。同一个过滤键内的多个值之间为"或"关系（匹配任意一个）。不同过滤键之间为"与"关系（事件必须通过所有指定的过滤条件）。不适用于某事件类型的过滤条件会被忽略，该事件照常推送。


        **可用的过滤键：**


        键 | 字段 | 取值 | 适用范围 | 不适用时的行为

        --- | ----- | ------ | ---------- | ---------------

        `e` | 事件类型 | 驼峰命名（camelCase）的事件类型名称 | 所有事件 | -

        `s` | 交易对 | 交易对名称（例如 `BTCUSDT`） | 带有交易对字段的事件 |
        不带交易对字段的事件（`balanceUpdate`、`outboundAccountPosition`、`externalLockUpdate`）始终推送。

        `a` | 资产 | 资产名称（例如 `BTC`、`USDT`） | 带有资产字段的事件 |
        不带资产字段的事件（`executionReport`、`listStatus`、`outboundAccountPosition`）始终推送。

        `x` | 执行类型 | 大写下划线命名（`SCREAMING_SNAKE_CASE`）的执行类型 | 仅 `executionReport` 事件 | 所有非 `executionReport` 事件始终推送。


        **事件类型取值（`e`）：**


        取值 | 描述

        ----- | -----------

        `executionReport` | 订单生命周期事件（新订单、成交、撤单、过期、修改）

        `balanceUpdate` | 余额增减（充值、提现）

        `outboundAccountPosition` | 账户变动后的持仓快照

        `listStatus` | 订单列表（OCO、OTO、OTOCO、OPO、OPOCO）状态更新

        `externalLockUpdate` | 外部锁定余额变动


        **执行类型取值（`x`）：**


        取值 | 描述

        ----- | -----------

        `NEW` | 新订单已被接受

        `TRADE` | 订单成交（部分或全部）

        `CANCELED` | 订单已撤销

        `REPLACED` | 订单已替换（撤销并替换）

        `REJECTED` | 订单被拒绝

        `EXPIRED` | 订单已过期

        `TRADE_PREVENTION` | 触发了自成交预防（STP）


        **示例：**


        仅推送执行报告和余额更新：


        ```javascript

        { "filter": { "e": ["executionReport", "balanceUpdate"] } }

        ```


        仅推送 BTCUSDT 和 ETHUSDT 的事件：


        ```javascript

        { "filter": { "s": ["BTCUSDT", "ETHUSDT"] } }

        ```


        仅推送 BTC 的余额更新：


        ```javascript

        { "filter": { "e": ["balanceUpdate"], "a": ["BTC"] } }

        ```


        仅推送执行报告中的成交：


        ```javascript

        { "filter": { "e": ["executionReport"], "x": ["TRADE"] } }

        ```


        **校验规则：**


        条件 | 结果

        --------- | ------

        未提供 `filter` | 推送所有事件（无过滤）

        `filter: {}` | 错误：过滤器对象为空

        `filter: {"e": []}` | 错误：取值数组为空

        `filter: {"e": ["executionReport", "executionReport"]}` | 错误：取值重复

        `filter: {"e": ["badType"]}` | 错误：无法识别的事件类型

        `filter: {"s": ["NOSYMBOL"]}` | 错误：未知交易对（[`-1121`](/products/spot/errors#-1121-bad_symbol)）

        `filter: {"a": ["NOASSET"]}` | 错误：未知资产（[`-1108`](/products/spot/errors#-1108-bad_asset)）

        `filter: {"z": [...]}` | 错误：未知的过滤键


        **注意：**


        * `listenKeyExpired` 和 `eventStreamTerminated` 生命周期事件始终推送，不受过滤器影响。

        * 使用 `userDataStream.subscribe.signature` 时，`filter` 必须包含在被签名的字符串中。为使签名匹配：
          * 过滤键必须按字母顺序排列：`a`、`e`、`s`、`x`。
          * 过滤器的 JSON 元素之间不能有空格。

          被签名的参数字符串示例：

          ```
          apiKey=...&filter={"e":["executionReport"],"s":["BAZUSD"],"x":["TRADE"]}&timestamp=...
          ```

        * 通过新请求重新订阅以延长签名订阅时，当前生效的过滤器会被新请求中的过滤器替换。
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.subscribe
                  example: userDataStream.subscribe
                params:
                  type: object
                  properties:
                    filter:
                      type: object
                      example:
                        e:
                          - executionReport
                      description: >-
                        Optional filter that controls which events are delivered on this subscription. See [User Data
                        Stream Subscription Filters](#user-data-stream-subscription-filters). When omitted, all events
                        for the subscribed account are delivered.
                      x-description-cn: 可选的过滤器，用于控制该订阅推送哪些事件。参见 [用户数据流订阅过滤器](#user-data-stream-subscription-filters)。未提供时，推送所订阅账户的所有事件。
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: userDataStream.subscribe
              params:
                filter:
                  e:
                    - executionReport
      responses:
        Successful Response:
          description: Subscribe to User Data Stream
          x-description-cn: 订阅用户数据流
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      subscriptionId:
                        type: integer
                        format: int64
                        example: 0
  /userDataStream.subscribe.signature:
    post:
      summary: Subscribe to User Data Stream through signature subscription (USER_STREAM)
      x-summary-cn: 通过签名订阅的方式订阅用户数据流 (USER_STREAM)
      tags:
        - user-data-stream
      operationId: userDataStreamSubscribeSignature
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe-signature
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/UserDataStreamApi/userDataStreamSubscribeSignature.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/user_data_stream_api/user_data_stream_subscribe_signature.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/UserDataStream/user_data_stream_subscribe_signature.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/userdatastream/UserDataStreamSubscribeSignatureExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/UserDataStreamAPI/UserDataStreamSubscribeSignature/UserDataStreamSubscribeSignature.go
      x-ip-weight: 2
      x-legacy-anchors:
        - user-data-signature
      x-security-type: USER_STREAM
      x-signed: true
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.subscribe.signature
                  example: userDataStream.subscribe.signature
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: number
                      format: float
                      example: 5000
                      maximum: 60000
                      description: >-
                        Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                        specified.
                      x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect
                        the current client

                        time and is validated by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
                    filter:
                      type: object
                      example:
                        e:
                          - executionReport
                      description: >-
                        Optional event filter. See [User Data Stream Subscription
                        Filters](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters).
                        When included, `filter` must be in the signed string with sorted keys and no whitespace between
                        JSON elements.
                      x-description-cn: >-
                        可选的事件过滤器。参见
                        [用户数据流订阅过滤器](/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters)。如果提供，`filter`
                        必须包含在被签名的字符串中，且键需排序、JSON 元素之间不能有空格。
                  additionalProperties: false
                  required:
                    - timestamp
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: userDataStream.subscribe.signature
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                filter:
                  e:
                    - executionReport
      responses:
        Successful Response:
          description: Subscribe to User Data Stream through signature subscription
          x-description-cn: 通过签名订阅的方式订阅用户数据流
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
                    properties:
                      subscriptionId:
                        type: integer
                        format: int64
                        example: 0
  /userDataStream.unsubscribe:
    post:
      summary: Unsubscribe from User Data Stream
      x-summary-cn: 取消订阅用户数据流
      description: >-
        Stop listening to the User Data Stream in the current WebSocket

        connection.


        Note that `session.logout` will only close the subscription created with `userDataStream.subscribe` but not
        subscriptions opened with `userDataStream.subscribe.signature`.
      x-description-cn: |-
        取消订阅当前 WebSocket 连接中的用户数据流。

        请注意 `session.logout` 只会关闭由 `userDataStream.subscribe` 创建的订阅，并不会关闭通过 `userDataStream.subscribe.signature` 创建的订阅。
      tags:
        - user-data-stream
      operationId: userDataStreamUnsubscribe
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-unsubscribe
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/websocket-api/UserDataStreamApi/userDataStreamUnsubscribe.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/websocket_api/user_data_stream_api/user_data_stream_unsubscribe.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/websocket_api/UserDataStream/user_data_stream_unsubscribe.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/websocket/api/userdatastream/UserDataStreamUnsubscribeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/websocketapi/UserDataStreamAPI/UserDataStreamUnsubscribe/UserDataStreamUnsubscribe.go
      x-ip-weight: 2
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Client-generated request identifier.
                  x-description-cn: 客户端生成的请求标识符。
                  example: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.unsubscribe
                  example: userDataStream.unsubscribe
                params:
                  type: object
                  properties:
                    subscriptionId:
                      type: integer
                      example: 1
                      description: >-
                        When called with no parameter, this will close all subscriptions. When called with the
                        subscriptionId parameter, this will attempt to close the subscription with that subscription id,
                        if it exists.
                      x-description-cn: 不带参数调用时，将关闭所有订阅。带 subscriptionId 参数调用时，将尝试关闭该订阅ID对应的订阅（如果存在）。
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: 7d3b9b46-5f4f-4c8b-9a2d-0a8f9a4a0f5b
              method: userDataStream.unsubscribe
              params:
                subscriptionId: 1
      responses:
        Successful Response:
          description: Unsubscribe from User Data Stream
          x-description-cn: 取消订阅用户数据流
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7
                  status:
                    type: integer
                    format: int64
                    example: 200
                  result:
                    type: object
components:
  schemas:
    myFiltersResponse:
      type: object
      properties:
        exchangeFilters:
          type: array
          items:
            $ref: "#/components/schemas/exchangeFilters"
        symbolFilters:
          type: array
          items:
            $ref: "#/components/schemas/symbolFilters"
        assetFilters:
          type: array
          items:
            $ref: "#/components/schemas/assetFilters"
        rateLimits:
          type: array
          items:
            $ref: "#/components/schemas/rateLimits"
    exchangeFilters:
      oneOf:
        - $ref: "#/components/schemas/ExchangeMaxNumOrdersFilter"
        - $ref: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
        - $ref: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
        - $ref: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
      discriminator:
        propertyName: filterType
        mapping:
          EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
          EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
          EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
          EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
    symbolFilters:
      oneOf:
        - $ref: "#/components/schemas/PriceFilter"
        - $ref: "#/components/schemas/PercentPriceFilter"
        - $ref: "#/components/schemas/PercentPriceBySideFilter"
        - $ref: "#/components/schemas/LotSizeFilter"
        - $ref: "#/components/schemas/MinNotionalFilter"
        - $ref: "#/components/schemas/NotionalFilter"
        - $ref: "#/components/schemas/IcebergPartsFilter"
        - $ref: "#/components/schemas/MarketLotSizeFilter"
        - $ref: "#/components/schemas/MaxNumOrdersFilter"
        - $ref: "#/components/schemas/MaxNumAlgoOrdersFilter"
        - $ref: "#/components/schemas/MaxNumIcebergOrdersFilter"
        - $ref: "#/components/schemas/MaxPositionFilter"
        - $ref: "#/components/schemas/TrailingDeltaFilter"
        - $ref: "#/components/schemas/TPlusSellFilter"
        - $ref: "#/components/schemas/MaxNumOrderListsFilter"
        - $ref: "#/components/schemas/MaxNumOrderAmendsFilter"
      discriminator:
        propertyName: filterType
        mapping:
          PRICE_FILTER: "#/components/schemas/PriceFilter"
          PERCENT_PRICE: "#/components/schemas/PercentPriceFilter"
          PERCENT_PRICE_BY_SIDE: "#/components/schemas/PercentPriceBySideFilter"
          LOT_SIZE: "#/components/schemas/LotSizeFilter"
          MIN_NOTIONAL: "#/components/schemas/MinNotionalFilter"
          NOTIONAL: "#/components/schemas/NotionalFilter"
          ICEBERG_PARTS: "#/components/schemas/IcebergPartsFilter"
          MARKET_LOT_SIZE: "#/components/schemas/MarketLotSizeFilter"
          MAX_NUM_ORDERS: "#/components/schemas/MaxNumOrdersFilter"
          MAX_NUM_ALGO_ORDERS: "#/components/schemas/MaxNumAlgoOrdersFilter"
          MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/MaxNumIcebergOrdersFilter"
          MAX_POSITION: "#/components/schemas/MaxPositionFilter"
          TRAILING_DELTA: "#/components/schemas/TrailingDeltaFilter"
          T_PLUS_SELL: "#/components/schemas/TPlusSellFilter"
          MAX_NUM_ORDER_LISTS: "#/components/schemas/MaxNumOrderListsFilter"
          MAX_NUM_ORDER_AMENDS: "#/components/schemas/MaxNumOrderAmendsFilter"
    assetFilters:
      oneOf:
        - $ref: "#/components/schemas/MaxAssetFilter"
      discriminator:
        propertyName: filterType
        mapping:
          MAX_ASSET: "#/components/schemas/MaxAssetFilter"
    ExchangeMaxNumOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: EXCHANGE_MAX_NUM_ORDERS
        maxNumOrders:
          type: integer
          format: int64
          example: 1000
    ExchangeMaxNumAlgoOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: EXCHANGE_MAX_NUM_ALGO_ORDERS
        maxNumAlgoOrders:
          type: integer
          format: int64
          example: 200
    ExchangeMaxNumIcebergOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
        maxNumIcebergOrders:
          type: integer
          format: int64
          example: 10
    ExchangeMaxNumOrderListsFilter:
      type: object
      properties:
        filterType:
          type: string
          example: EXCHANGE_MAX_NUM_ORDER_LISTS
        maxNumOrderLists:
          type: integer
          format: int64
          example: 20
    PriceFilter:
      type: object
      properties:
        filterType:
          type: string
          example: PRICE_FILTER
        priceExponent:
          type: integer
          example: 8
          x-sbe-only: true
        minPrice:
          type: string
          example: "0.00000100"
        maxPrice:
          type: string
          example: "100000.00000000"
        tickSize:
          type: string
          example: "0.00000100"
    PercentPriceFilter:
      type: object
      properties:
        filterType:
          type: string
          example: PERCENT_PRICE
        multiplierExponent:
          type: integer
          example: 4
          x-sbe-only: true
        multiplierUp:
          type: string
          example: "1.3000"
        multiplierDown:
          type: string
          example: "0.7000"
        avgPriceMins:
          type: integer
          example: 5
    PercentPriceBySideFilter:
      type: object
      properties:
        filterType:
          type: string
          example: PERCENT_PRICE_BY_SIDE
        multiplierExponent:
          type: integer
          example: 4
          x-sbe-only: true
        bidMultiplierUp:
          type: string
          example: "1.2000"
        bidMultiplierDown:
          type: string
          example: "0.8000"
        askMultiplierUp:
          type: string
          example: "1.2000"
        askMultiplierDown:
          type: string
          example: "0.8000"
        avgPriceMins:
          type: integer
          example: 5
    LotSizeFilter:
      type: object
      properties:
        filterType:
          type: string
          example: LOT_SIZE
        qtyExponent:
          type: integer
          example: 8
          x-sbe-only: true
        minQty:
          type: string
          example: "0.00010000"
        maxQty:
          type: string
          example: "100000.00000000"
        stepSize:
          type: string
          example: "0.00010000"
    MinNotionalFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MIN_NOTIONAL
        priceExponent:
          type: integer
          example: 8
          x-sbe-only: true
        minNotional:
          type: string
          example: "10.00000000"
        applyToMarket:
          type: boolean
          example: true
        avgPriceMins:
          type: integer
          example: 5
    NotionalFilter:
      type: object
      properties:
        filterType:
          type: string
          example: NOTIONAL
        priceExponent:
          type: integer
          example: 8
          x-sbe-only: true
        minNotional:
          type: string
          example: "10.00000000"
        applyMinToMarket:
          type: boolean
          example: true
        maxNotional:
          type: string
          example: "100000.00000000"
        applyMaxToMarket:
          type: boolean
          example: false
        avgPriceMins:
          type: integer
          example: 5
    IcebergPartsFilter:
      type: object
      properties:
        filterType:
          type: string
          example: ICEBERG_PARTS
        limit:
          type: integer
          format: int64
          example: 10
    MarketLotSizeFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MARKET_LOT_SIZE
        qtyExponent:
          type: integer
          example: 8
          x-sbe-only: true
        minQty:
          type: string
          example: "0.00000000"
        maxQty:
          type: string
          example: "1000.00000000"
        stepSize:
          type: string
          example: "0.00000000"
    MaxNumOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_NUM_ORDERS
        maxNumOrders:
          type: integer
          format: int64
          example: 200
    MaxNumAlgoOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_NUM_ALGO_ORDERS
        maxNumAlgoOrders:
          type: integer
          format: int64
          example: 10
    MaxNumIcebergOrdersFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_NUM_ICEBERG_ORDERS
        maxNumIcebergOrders:
          type: integer
          format: int64
          example: 5
    MaxPositionFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_POSITION
        qtyExponent:
          type: integer
          example: 8
          x-sbe-only: true
        maxPosition:
          type: string
          example: "100.00000000"
    TrailingDeltaFilter:
      type: object
      properties:
        filterType:
          type: string
          example: TRAILING_DELTA
        minTrailingAboveDelta:
          type: integer
          format: int64
          example: 10
        maxTrailingAboveDelta:
          type: integer
          format: int64
          example: 2000
        minTrailingBelowDelta:
          type: integer
          format: int64
          example: 10
        maxTrailingBelowDelta:
          type: integer
          format: int64
          example: 2000
    TPlusSellFilter:
      type: object
      properties:
        filterType:
          type: string
          example: T_PLUS_SELL
        endTime:
          type: integer
          format: int64
          example: 1741672924895
    MaxNumOrderListsFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_NUM_ORDER_LISTS
        maxNumOrderLists:
          type: integer
          format: int64
          example: 20
    MaxNumOrderAmendsFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_NUM_ORDER_AMENDS
        maxNumOrderAmends:
          type: integer
          format: int64
          example: 10
    MaxAssetFilter:
      type: object
      properties:
        filterType:
          type: string
          example: MAX_ASSET
        qtyExponent:
          type: integer
          example: 8
          x-sbe-only: true
        limit:
          type: string
          example: "1000000.00000000"
        asset:
          type: string
          example: JPY
    rateLimits:
      type: object
      properties:
        rateLimitType:
          type: string
          example: REQUEST_WEIGHT
        interval:
          type: string
          example: MINUTE
        intervalNum:
          type: integer
          format: int64
          example: 1
        limit:
          type: integer
          format: int64
          example: 6000
        count:
          type: integer
          format: int64
          example: 40
    exchangeInfoResponse:
      type: object
      properties:
        timezone:
          type: string
          example: UTC
        serverTime:
          type: integer
          format: int64
          example: 1655969291181
        rateLimits:
          type: array
          description: Global rate limits. See "Rate limits" section.
          x-description-cn: 全局速率限制。请参阅 "速率限制" 部分。
          example:
            - rateLimitType: REQUEST_WEIGHT
              interval: MINUTE
              intervalNum: 1
              limit: 6000
            - rateLimitType: ORDERS
              interval: SECOND
              intervalNum: 10
              limit: 50
            - rateLimitType: ORDERS
              interval: DAY
              intervalNum: 1
              limit: 160000
            - rateLimitType: CONNECTIONS
              interval: MINUTE
              intervalNum: 5
              limit: 300
          items:
            $ref: "#/components/schemas/rateLimits"
        exchangeFilters:
          type: array
          description: |-
            Exchange filters are explained on the "Filters" page:
            /products/spot/filters.md
            All exchange filters are optional.
          x-description-cn: |-
            交易所级别过滤器在 "过滤器" 页面上进行了说明：
            /products/spot/filters.md
            全部交易过滤器是可选的。
          items:
            $ref: "#/components/schemas/exchangeFilters"
        symbols:
          type: array
          items:
            type: object
            properties:
              symbol:
                type: string
                example: BNBBTC
              status:
                type: string
                example: TRADING
              baseAsset:
                type: string
                example: BNB
              baseAssetPrecision:
                type: integer
                format: int64
                example: 8
              quoteAsset:
                type: string
                example: BTC
              quotePrecision:
                type: integer
                format: int64
                example: 8
              quoteAssetPrecision:
                type: integer
                format: int64
                example: 8
              baseCommissionPrecision:
                type: integer
                format: int64
                example: 8
              quoteCommissionPrecision:
                type: integer
                format: int64
                example: 8
              orderTypes:
                type: array
                example:
                  - LIMIT
                  - LIMIT_MAKER
                  - MARKET
                  - STOP_LOSS_LIMIT
                  - TAKE_PROFIT_LIMIT
                items:
                  type: string
                  example: LIMIT
              icebergAllowed:
                type: boolean
                example: true
              ocoAllowed:
                type: boolean
                example: true
              otoAllowed:
                type: boolean
                example: true
              opoAllowed:
                type: boolean
                example: true
              quoteOrderQtyMarketAllowed:
                type: boolean
                example: true
              allowTrailingStop:
                type: boolean
                example: true
              cancelReplaceAllowed:
                type: boolean
                example: true
              amendAllowed:
                type: boolean
                example: false
              pegInstructionsAllowed:
                type: boolean
                example: true
              marketQuoteNotionalLimitAllowed:
                type: boolean
                example: true
              limitQuoteNotionalLimitAllowed:
                type: boolean
                example: true
              isSpotTradingAllowed:
                type: boolean
                example: true
              isMarginTradingAllowed:
                type: boolean
                example: true
              filters:
                type: array
                description: |-
                  Symbol filters are explained on the "Filters" page:
                  /products/spot/filters.md
                  All symbol filters are optional.
                x-description-cn: |-
                  交易对过滤器在"过滤器"页面上进行了说明：
                  /products/spot/filters.md
                  全部交易对过滤器是可选的。
                example:
                  - filterType: PRICE_FILTER
                    minPrice: "0.00000100"
                    maxPrice: "100000.00000000"
                    tickSize: "0.00000100"
                  - filterType: LOT_SIZE
                    minQty: "0.00100000"
                    maxQty: "100000.00000000"
                    stepSize: "0.00100000"
                items:
                  $ref: "#/components/schemas/symbolFilters"
              permissions:
                type: array
                items:
                  type: string
                  example: SPOT
              permissionSets:
                type: array
                items:
                  type: array
                  example:
                    - SPOT
                    - MARGIN
                    - TRD_GRP_004
                  items:
                    type: string
                    example: SPOT
              defaultSelfTradePreventionMode:
                type: string
                example: NONE
              allowedSelfTradePreventionModes:
                type: array
                items:
                  type: string
                  example: NONE
        sors:
          type: array
          description: |-
            Optional field. Present only when SOR is available.
            /products/spot/faqs/sor_faq.md
          x-description-cn: |-
            可选字段，仅当 SOR 可用时才会被显示出来。
            /products/spot/faqs/sor_faq.md
          items:
            type: object
            properties:
              baseAsset:
                type: string
                example: BTC
              symbols:
                type: array
                example:
                  - BTCUSDT
                  - BTCUSDC
                items:
                  type: string
                  example: BTCUSDT
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