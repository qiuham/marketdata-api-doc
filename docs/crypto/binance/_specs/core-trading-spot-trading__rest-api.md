---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:07.076825
---

# core-trading-spot-trading__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Spot REST API
  description: Access market data, manage accounts, and trade on Binance Spot.
  x-description-cn: 访问市场数据、管理账户，并在 Binance 现货市场交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/spot/rest-api#limits
x-rate-limits-guide-cn: products/spot/rest-api#访问限制
x-security-guide: products/spot/rest-api#request-security
x-security-guide-cn: products/spot/rest-api#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
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
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
  - url: https://demo-api.binance.com
  - url: https://data-api.binance.vision
  - url: https://testnet.binance.vision
  - url: https://api1.testnet.binance.vision
paths:
  /api/v3/account/commission:
    get:
      summary: Query Commission Rates (USER_DATA)
      x-summary-cn: 查询佣金费率 (USER_DATA)
      description: Get current account commission rates.
      x-description-cn: 获取当前账户的佣金费率。
      tags:
        - account
      operationId: accountCommission
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#account-commission
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/accountCommission.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/account_commission.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/account_commission.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/AccountCommissionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/AccountCommission/AccountCommission.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/AccountCommissionExample.php
      x-ip-weight: 20
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
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Query Commission Rates
          x-description-cn: 查询佣金费率
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSDT
                  standardCommission:
                    type: object
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
                    description: Commission rates on trades from the order.
                    x-description-cn: 订单交易的标准佣金率。
                  specialCommission:
                    type: object
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
                    description: Special commission rates from the order.
                    x-description-cn: 订单交易的特殊佣金率。
                  taxCommission:
                    type: object
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
                    description: Tax commission rates for trades from the order.
                    x-description-cn: 订单交易的税率。
                  discount:
                    type: object
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
                          Multiplier applied to the standard commission when paying commission in BNB (e.g. 0.75 = 75%
                          of the standard commission is charged).
                        x-description-cn: 当用BNB支付佣金时，在标准佣金上按此比率打折
                    description: Discount commission when paying in BNB
                    x-description-cn: 使用BNB支付时的佣金折扣。
  /api/v3/allOrderList:
    get:
      summary: Query all Order lists (USER_DATA)
      x-summary-cn: 查询所有订单列表 (USER_DATA)
      description: |-
        Retrieves all order lists based on provided optional parameters.

        Note that the time between `startTime` and `endTime` can't be longer
        than 24 hours.
      x-description-cn: |-
        根据提供的可选参数检索所有的订单列表。

        请注意，`startTime`和`endTime`之间的时间不能超过 24 小时。
      tags:
        - account
      operationId: allOrderList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#all-order-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/allOrderList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/all_order_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/all_order_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/AllOrderListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/AllOrderList/AllOrderList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/AllOrderListExample.php
      x-ip-weight: 20
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
        - name: fromId
          in: query
          required: false
          description: If supplied, neither startTime or endTime can be provided
          x-description-cn: 提供该项后, startTime 和 endTime 都不可提供
          schema:
            type: integer
            format: int64
            example: 1
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Query all Order lists
          x-description-cn: 查询所有订单列表
          content:
            application/json:
              schema:
                type: array
                example:
                  - orderListId: 29
                    contingencyType: OCO
                    listStatusType: EXEC_STARTED
                    listOrderStatus: EXECUTING
                    listClientOrderId: amEEAXryFzFwYF1FeRpUoZ
                    transactionTime: 1565245913483
                    symbol: LTCBTC
                    orders:
                      - symbol: LTCBTC
                        orderId: 4
                        clientOrderId: oD7aesZqjEGlZrbtRpy5zB
                      - symbol: LTCBTC
                        orderId: 5
                        clientOrderId: Jr1h6xirOxgeJOUuYQS7V3
                  - orderListId: 28
                    contingencyType: OCO
                    listStatusType: EXEC_STARTED
                    listOrderStatus: EXECUTING
                    listClientOrderId: hG7hFNxJV6cZy3Ze4AUT4d
                    transactionTime: 1565245913407
                    symbol: LTCBTC
                    orders:
                      - symbol: LTCBTC
                        orderId: 2
                        clientOrderId: j6lFOfbmFMRjTYA7rRJ0LP
                      - symbol: LTCBTC
                        orderId: 3
                        clientOrderId: z0KCjOdditiLS5ekAFtK81
                items:
                  type: object
                  properties:
                    orderListId:
                      type: integer
                      format: int64
                      example: 29
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
                      example: amEEAXryFzFwYF1FeRpUoZ
                    transactionTime:
                      type: integer
                      format: int64
                      example: 1565245913483
                    symbol:
                      type: string
                      example: LTCBTC
                    orders:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: LTCBTC
                          orderId:
                            type: integer
                            format: int64
                            example: 4
                          clientOrderId:
                            type: string
                            example: oD7aesZqjEGlZrbtRpy5zB
  /api/v3/allOrders:
    get:
      summary: All orders (USER_DATA)
      x-summary-cn: 查询所有订单（包括历史订单） (USER_DATA)
      description: Get all account orders; active, canceled, or filled.
      x-description-cn: 获取all 账户 订单; active, canceled, 或 filled.
      tags:
        - account
      operationId: allOrders
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#all-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/allOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/all_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/all_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/AllOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/AllOrders/AllOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/AllOrdersExample.php
      x-ip-weight: 20
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
          required: true
          schema:
            type: string
            example: LTCBTC
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: recvWindow
          in: query
          required: false
          description: >-
            The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g.,
            6000.346) so that microseconds may be specified.
          x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: |-
        **Data Source:** Database

        - If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
        - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.
        - If `startTime` and/or `endTime` provided, `orderId` is not required.
        - The time between `startTime` and `endTime` can't be longer than 24 hours.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        - **注意:** * 如设置 `orderId` , 订单量将 >= `orderId`。否则将返回最新订单。
        - 一些历史订单 `cummulativeQuoteQty` < 0, 是指数据此时不存在。
        - 如果设置 `startTime` 和 `endTime`, `orderId` 就不需要设置。
        - `startTime`和`endTime`之间的时间不能超过 24 小时。 **数据源:** 数据库
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: All orders
          x-description-cn: All 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: LTCBTC
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                    orderListId:
                      type: integer
                      format: int64
                      example: -1
                      description: Unless it's part of an order list, value will be -1
                      x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                    clientOrderId:
                      type: string
                      example: myOrder1
                    price:
                      type: string
                      example: "0.1"
                    origQty:
                      type: string
                      example: "1.0"
                    executedQty:
                      type: string
                      example: "0.0"
                    cummulativeQuoteQty:
                      type: string
                      example: "0.0"
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
                    stopPrice:
                      type: string
                      example: "0.00000000"
                      description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                      x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                    icebergQty:
                      type: string
                      example: "0.00000000"
                      description: Appears only if the parameter icebergQty was sent in the request.
                      x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                    time:
                      type: integer
                      format: int64
                      example: 1499827319559
                    updateTime:
                      type: integer
                      format: int64
                      example: 1499827319559
                    isWorking:
                      type: boolean
                      example: true
                    origQuoteOrderQty:
                      type: string
                      example: "0.000000"
                    workingTime:
                      type: integer
                      format: int64
                      example: 1499827319559
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
  /api/v3/account:
    get:
      summary: Account information (USER_DATA)
      x-summary-cn: 账户信息 (USER_DATA)
      description: Get current account information.
      x-description-cn: 获取当前账户信息。
      tags:
        - account
      operationId: getAccount
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#get-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/getAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/get_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/get_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/GetAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/GetAccount/GetAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/GetAccountExample.php
      x-ip-weight: 20
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
        - name: omitZeroBalances
          in: query
          required: false
          description: When set to `true`, emits only the non-zero balances of an account.
          x-description-cn: 如果`true`，将隐藏所有零余额。
          schema:
            type: boolean
            example: false
            default: false
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Memory => Database"
      x-parameters-notes-cn: "**数据源:** 缓存 => 数据库"
      responses:
        "200":
          description: Account information
          x-description-cn: 账户信息
          content:
            application/json:
              schema:
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
                  canTrade:
                    type: boolean
                    example: true
                  canWithdraw:
                    type: boolean
                    example: true
                  canDeposit:
                    type: boolean
                    example: true
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
                    example: 123456789
                  accountType:
                    type: string
                    example: SPOT
                  balances:
                    type: array
                    example:
                      - asset: BTC
                        free: "4723846.89208129"
                        locked: "0.00000000"
                      - asset: LTC
                        free: "4763368.68006011"
                        locked: "0.00000000"
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: BTC
                        free:
                          type: string
                          example: "4723846.89208129"
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
  /api/v3/openOrders:
    get:
      summary: Current open orders (USER_DATA)
      x-summary-cn: 查看账户当前挂单 (USER_DATA)
      description: Get all open orders on a symbol. **Careful** when accessing this with no symbol.
      x-description-cn: 请小心使用不带symbol参数的调用
      tags:
        - account
      operationId: getOpenOrders
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#get-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/getOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/get_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/get_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/GetOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/GetOpenOrders/GetOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/GetOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: 6 for a single symbol; 80 when the symbol parameter is omitted
      x-weight-cn: "带 symbol: 6；不带 symbol: 80"
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
            example: LTCBTC
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: |-
        **Data Source:** Memory => Database

        - If the symbol is not sent, orders for all symbols will be returned in an array.
      x-parameters-notes-cn: |-
        **数据源:** 缓存 => 数据库

        - 不带symbol参数，会返回所有交易对的挂单
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: Current open orders
          x-description-cn: 查看账户当前挂单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: LTCBTC
                    orderId:
                      type: integer
                      format: int64
                      example: 1
                    orderListId:
                      type: integer
                      format: int64
                      example: -1
                      description: Unless it's part of an order list, value will be -1
                      x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                    clientOrderId:
                      type: string
                      example: myOrder1
                    price:
                      type: string
                      example: "0.1"
                    origQty:
                      type: string
                      example: "1.0"
                    executedQty:
                      type: string
                      example: "0.0"
                    origQuoteOrderQty:
                      type: string
                      example: "0.000000"
                    cummulativeQuoteQty:
                      type: string
                      example: "0.0"
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
                    stopPrice:
                      type: string
                      example: "0.00000000"
                      description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                      x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                    icebergQty:
                      type: string
                      example: "0.00000000"
                      description: Appears only if the parameter icebergQty was sent in the request.
                      x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                    time:
                      type: integer
                      format: int64
                      example: 1499827319559
                    updateTime:
                      type: integer
                      format: int64
                      example: 1499827319559
                    isWorking:
                      type: boolean
                      example: true
                    workingTime:
                      type: integer
                      format: int64
                      example: 1499827319559
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
    delete:
      summary: Cancel All Open Orders on a Symbol (TRADE)
      x-summary-cn: 撤销单一交易对的所有挂单 (TRADE)
      description: |-
        Cancels all active orders on a symbol.
        This includes orders that are part of an order list.
      x-description-cn: 撤销单一交易对下所有挂单。这也包括了来自订单列表的挂单。
      tags:
        - trade
      operationId: deleteOpenOrders
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#delete-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/deleteOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/delete_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/delete_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/DeleteOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/DeleteOpenOrders/DeleteOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/DeleteOpenOrdersExample.php
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
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      responses:
        "200":
          description: Cancel All Open Orders on a Symbol
          x-description-cn: 撤销单一交易对的所有挂单
          content:
            application/json:
              schema:
                type: array
                example:
                  - symbol: BTCUSDT
                    origClientOrderId: E6APeyTJvkMvLMYMqu1KQ4
                    orderId: 11
                    orderListId: -1
                    clientOrderId: pXLV6Hz6mprAcVYpVMTGgx
                    transactTime: 1684804350068
                    price: "0.089853"
                    origQty: "0.178622"
                    executedQty: "0.000000"
                    origQuoteOrderQty: "0.000000"
                    cummulativeQuoteQty: "0.000000"
                    status: CANCELED
                    timeInForce: GTC
                    type: LIMIT
                    side: BUY
                    selfTradePreventionMode: NONE
                  - symbol: BTCUSDT
                    origClientOrderId: A3EF2HCwxgZPFMrfwbgrhv
                    orderId: 13
                    orderListId: -1
                    clientOrderId: pXLV6Hz6mprAcVYpVMTGgx
                    transactTime: 1684804350069
                    price: "0.090430"
                    origQty: "0.178622"
                    executedQty: "0.000000"
                    origQuoteOrderQty: "0.000000"
                    cummulativeQuoteQty: "0.000000"
                    status: CANCELED
                    timeInForce: GTC
                    type: LIMIT
                    side: BUY
                    selfTradePreventionMode: NONE
                  - orderListId: 1929
                    contingencyType: OCO
                    listStatusType: ALL_DONE
                    listOrderStatus: ALL_DONE
                    listClientOrderId: 2inzWQdDvZLHbbAmAozX2N
                    transactionTime: 1585230948299
                    symbol: BTCUSDT
                    orders:
                      - symbol: BTCUSDT
                        orderId: 20
                        clientOrderId: CwOOIPHSmYywx6jZX77TdL
                      - symbol: BTCUSDT
                        orderId: 21
                        clientOrderId: 461cPg51vQjV3zIMOXNz39
                    orderReports:
                      - symbol: BTCUSDT
                        origClientOrderId: CwOOIPHSmYywx6jZX77TdL
                        orderId: 20
                        orderListId: 1929
                        clientOrderId: pXLV6Hz6mprAcVYpVMTGgx
                        transactTime: 1688005070874
                        price: "0.668611"
                        origQty: "0.690354"
                        executedQty: "0.000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.000000"
                        status: CANCELED
                        timeInForce: GTC
                        type: STOP_LOSS_LIMIT
                        side: BUY
                        stopPrice: "0.378131"
                        icebergQty: "0.017083"
                        selfTradePreventionMode: NONE
                      - symbol: BTCUSDT
                        origClientOrderId: 461cPg51vQjV3zIMOXNz39
                        orderId: 21
                        orderListId: 1929
                        clientOrderId: pXLV6Hz6mprAcVYpVMTGgx
                        transactTime: 1688005070874
                        price: "0.008791"
                        origQty: "0.690354"
                        executedQty: "0.000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.000000"
                        status: CANCELED
                        timeInForce: GTC
                        type: LIMIT_MAKER
                        side: BUY
                        icebergQty: "0.639962"
                        selfTradePreventionMode: NONE
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSDT
                    origClientOrderId:
                      type: string
                      example: E6APeyTJvkMvLMYMqu1KQ4
                    orderId:
                      type: integer
                      format: int64
                      example: 11
                    orderListId:
                      type: integer
                      format: int64
                      example: -1
                    clientOrderId:
                      type: string
                      example: pXLV6Hz6mprAcVYpVMTGgx
                    transactTime:
                      type: integer
                      format: int64
                      example: 1684804350068
                    price:
                      type: string
                      example: "0.089853"
                    origQty:
                      type: string
                      example: "0.178622"
                    executedQty:
                      type: string
                      example: "0.000000"
                    origQuoteOrderQty:
                      type: string
                      example: "0.000000"
                    cummulativeQuoteQty:
                      type: string
                      example: "0.000000"
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
                      example: BUY
                    selfTradePreventionMode:
                      type: string
                      example: NONE
  /api/v3/order:
    get:
      summary: Query order (USER_DATA)
      x-summary-cn: 查询订单 (USER_DATA)
      description: Check an order's status.
      x-description-cn: 查询订单状态
      tags:
        - account
      operationId: getOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#get-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/getOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/get_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/get_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/GetOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/GetOrder/GetOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/GetOrderExample.php
      x-ip-weight: 4
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
          required: true
          schema:
            type: string
            example: LTCBTC
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: myOrder1
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: >-
        **Data Source:** Memory => Database


        - Either `orderId` or `origClientOrderId` must be sent.

        - If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the
        `origClientOrderId` from that result is checked against that order. If both conditions are not met the request
        will be rejected.

        - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.
      x-parameters-notes-cn: >-
        **数据源:** 缓存 => 数据库


        - 至少需要发送 `orderId` 与 `origClientOrderId`中的一个。

        - 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId`
        的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。

        - 某些历史订单的 `cummulativeQuoteQty` 会 < 0, 表示当前暂无该数据。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: Query order
          x-description-cn: 查询订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: LTCBTC
                    x-description-cn: 交易对
                    description: symbol.
                  orderId:
                    type: integer
                    format: int64
                    example: 1
                    x-description-cn: 系统的订单ID
                    description: order Id.
                  orderListId:
                    type: integer
                    format: int64
                    example: -1
                    description: This field will always have a value of -1 if not an order list.
                    x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                  clientOrderId:
                    type: string
                    example: myOrder1
                    x-description-cn: 客户自己设置的ID
                    description: client Order Id.
                  price:
                    type: string
                    example: "0.1"
                    x-description-cn: 订单价格
                    description: price.
                  origQty:
                    type: string
                    example: "1.0"
                    x-description-cn: 用户设置的原始订单数量
                    description: orig Qty.
                  executedQty:
                    type: string
                    example: "0.0"
                    x-description-cn: 交易的订单数量
                    description: executed Qty.
                  origQuoteOrderQty:
                    type: string
                    example: "0.000000"
                    x-description-cn: 原始的交易金额
                    description: orig Quote Order Qty.
                  cummulativeQuoteQty:
                    type: string
                    example: "0.0"
                    x-description-cn: 累计交易的金额
                    description: cummulative Quote Qty.
                  status:
                    type: string
                    example: NEW
                    x-description-cn: 订单状态
                    description: status.
                  timeInForce:
                    type: string
                    example: GTC
                    x-description-cn: 订单的时效方式
                    description: time In Force.
                  type:
                    type: string
                    example: LIMIT
                    x-description-cn: 订单类型， 比如市价单，现价单等
                    description: type.
                  side:
                    type: string
                    example: BUY
                    x-description-cn: 订单方向，买还是卖
                    description: side.
                  stopPrice:
                    type: string
                    example: "0.00000000"
                    description: Appears for STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT orders.
                    x-description-cn: 出现在 STOP_LOSS, TAKE_PROFIT, STOP_LOSS_LIMIT 和 TAKE_PROFIT_LIMIT 订单中。
                  icebergQty:
                    type: string
                    example: "0.00000000"
                    description: Appears only if the parameter icebergQty was sent in the request.
                    x-description-cn: 仅在请求中发送了 icebergQty 参数时出现。
                  time:
                    type: integer
                    format: int64
                    example: 1499827319559
                    x-description-cn: 订单时间
                    description: time.
                  updateTime:
                    type: integer
                    format: int64
                    example: 1499827319559
                    x-description-cn: 最后更新时间
                    description: update Time.
                  isWorking:
                    type: boolean
                    example: true
                    x-description-cn: 订单是否出现在orderbook中
                    description: is Working.
                  workingTime:
                    type: integer
                    format: int64
                    example: 1499827319559
                    x-description-cn: 订单添加到 order book 的时间
                    description: working Time.
                  selfTradePreventionMode:
                    type: string
                    example: NONE
                    x-description-cn: 如何处理自我交易模式
                    description: self Trade Prevention Mode.
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
    delete:
      summary: Cancel order (TRADE)
      x-summary-cn: 撤销订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 撤销订单.
      tags:
        - trade
      operationId: deleteOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#delete-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/deleteOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/delete_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/delete_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/DeleteOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/DeleteOrder/DeleteOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/DeleteOrderExample.php
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
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: myOrder1
        - name: newClientOrderId
          in: query
          required: false
          description: Used to uniquely identify this cancel. Automatically generated by default.
          x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
          schema:
            type: string
            example: cancelMyOrder1
        - name: cancelRestrictions
          in: query
          required: false
          schema:
            type: string
            enum:
              - ONLY_NEW
              - ONLY_PARTIALLY_FILLED
            example: ONLY_NEW
          description: >-
            Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br>
            `ONLY_PARTIALLY_FILLED` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information
            please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions).
          x-description-cn: >-
            支持的值: <br>`ONLY_NEW` - 如果订单状态为 `NEW`，撤销将成功。<br> `ONLY_PARTIALLY_FILLED` - 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。
            请参阅[关于 `cancelRestrictions`](#regarding-cancelrestrictions) 了解更多信息。
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        - Either `orderId` or `origClientOrderId` must be sent.

        - If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the
        `origClientOrderId` from that result is checked against that order. If both conditions are not met the request
        will be rejected.
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        - `orderId` 与 `origClientOrderId` 必须至少发送一个。

        - 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId`
        的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。
      x-response-notes: >-
        **Notes:**

        - The payload above does not show all fields that can appear in the order response. Please refer to [Conditional
        fields in Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).

        - The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when
        only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.


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
        **注意:**

        - 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。

        - 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` +
        `origClientOrderId` 会稍慢。


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
        "200":
          description: Cancel order
          x-description-cn: 撤销订单
          content:
            application/json:
              schema:
                type: object
                additionalProperties: false
                properties:
                  symbol:
                    type: string
                    example: LTCBTC
                  orderId:
                    type: integer
                    format: int64
                    example: 4
                  orderListId:
                    type: integer
                    format: int64
                    example: -1
                    description: Unless it's part of an order list, value will be -1
                    x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                  origClientOrderId:
                    type: string
                    example: myOrder1
                  clientOrderId:
                    type: string
                    example: cancelMyOrder1
                  transactTime:
                    type: integer
                    format: int64
                    example: 1684804350068
                  price:
                    type: string
                    example: "2.00000000"
                  origQty:
                    type: string
                    example: "1.00000000"
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
                    example: LIMIT
                  side:
                    type: string
                    example: BUY
                  selfTradePreventionMode:
                    type: string
                    example: NONE
                  icebergQty:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Quantity for the iceberg order. Appears only if the parameter `icebergQty` was sent in the
                      request.
                    x-description-cn: 冰山订单数量。仅当请求中发送了 `icebergQty` 参数时返回。
                  preventedMatchId:
                    type: integer
                    format: int64
                    example: 0
                    description: >-
                      When used together with `symbol`, can be used to query a prevented match. Appears only if the
                      order expired due to STP.
                    x-description-cn: 与 `symbol` 搭配时可用于查询 prevented match。仅当订单因 STP 过期时返回。
                  preventedQuantity:
                    type: string
                    example: "1.200000"
                    description: Order quantity that expired due to STP. Appears only if the order expired due to STP.
                    x-description-cn: 因 STP 过期的订单数量。仅当订单因 STP 过期时返回。
                  stopPrice:
                    type: string
                    example: "23500.00000000"
                    description: >-
                      Price when the algorithmic order will be triggered. Appears for `STOP_LOSS`, `TAKE_PROFIT`,
                      `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` orders.
                    x-description-cn: 算法订单触发价格。适用于 `STOP_LOSS`、`TAKE_PROFIT`、`STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。
                  strategyId:
                    type: integer
                    format: int64
                    example: 37463720
                    description: >-
                      Can be used to label an order that's part of an order strategy. Appears if the parameter was
                      populated in the request.
                    x-description-cn: 可用于标记订单策略中的订单。仅当请求中传入该参数时返回。
                  strategyType:
                    type: integer
                    format: int64
                    example: 1000000
                    description: >-
                      Can be used to label an order that is using an order strategy. Appears if the parameter was
                      populated in the request.
                    x-description-cn: 可用于标记使用订单策略的订单。仅当请求中传入该参数时返回。
                  trailingDelta:
                    type: integer
                    format: int64
                    example: 10
                    description: Delta price change required before order activation. Appears for trailing stop orders.
                    x-description-cn: 订单激活前所需的价格变动幅度。适用于追踪止损订单。
                  trailingTime:
                    type: integer
                    format: int64
                    example: -1
                    description: >-
                      Time when the trailing order becomes active and starts tracking price changes. Appears only for
                      trailing stop orders.
                    x-description-cn: 追踪订单激活并开始跟踪价格变化的时间。仅适用于追踪止损订单。
                  usedSor:
                    type: boolean
                    example: true
                    description: Indicates whether the order used SOR. Appears when placing orders using SOR.
                    x-description-cn: 表示订单是否使用了 SOR。仅在使用 SOR 下单时返回。
                  workingFloor:
                    type: string
                    example: SOR
                    description: >-
                      Indicates whether the order is being filled by SOR or by the order book to which it was submitted.
                      Appears when placing orders using SOR.
                    x-description-cn: 表示订单由 SOR 撮合还是由提交到的订单簿撮合。仅在使用 SOR 下单时返回。
                  pegPriceType:
                    type: string
                    example: PRIMARY_PEG
                    description: Price peg type. Only for pegged orders.
                    x-description-cn: Peg 价格类型。仅适用于 pegged 订单。
                  pegOffsetType:
                    type: string
                    example: PRICE_LEVEL
                    description: Price peg offset type. Only for pegged orders, if requested.
                    x-description-cn: Peg 价格偏移类型。仅适用于请求了该字段的 pegged 订单。
                  pegOffsetValue:
                    type: integer
                    format: int64
                    example: 5
                    description: Price peg offset value. Only for pegged orders, if requested.
                    x-description-cn: Peg 价格偏移值。仅适用于请求了该字段的 pegged 订单。
                  peggedPrice:
                    type: string
                    example: "87523.83710000"
                    description: Current price the order is pegged at. Only for pegged orders, once determined.
                    x-description-cn: 订单当前 peg 到的价格。仅适用于已确定 peg 价格的订单。
                  expiryReason:
                    type: string
                    example: INSUFFICIENT_LIQUIDITY
                    description: Cause of the order's expiration. Returned when an order has expired.
                    x-description-cn: 订单过期原因。仅当订单已过期时返回。
    post:
      summary: New order (TRADE)
      x-summary-cn: 下单 (TRADE)
      description: |-
        Send in a new order.

        This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
      x-description-cn: 这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: newOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/NewOrder/NewOrder.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/NewOrderExample.php
      x-ip-weight: 1
      x-legacy-anchors:
        - place-new-order-trade
      x-order-weight: 1
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
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        Some additional mandatory parameters based on order `type`:


        ::span{#order-type}


        Type | Additional mandatory parameters | Additional Information

        ------------ | ------------| ------

        `LIMIT` | `timeInForce`, `quantity`, `price`|

        `MARKET` | `quantity` or `quoteOrderQty`| `MARKET` orders using the `quantity` field specifies the amount of the
        `base asset` the user wants to buy or sell at the market price. <br/> E.g. MARKET order on BTCUSDT will specify
        how much BTC the user is buying or selling. <br/><br/> `MARKET` orders using `quoteOrderQty` specifies the
        amount the user wants to spend (when buying) or receive (when selling) the `quote` asset; the correct `quantity`
        will be determined based on the market liquidity and `quoteOrderQty`. <br/> E.g. Using the symbol BTCUSDT: <br/>
        `BUY` side, the order will buy as many BTC as `quoteOrderQty` USDT can. <br/> `SELL` side, the order will sell
        as much BTC needed to receive `quoteOrderQty` USDT.

        `STOP_LOSS` | `quantity`, `stopPrice` or `trailingDelta`| This will execute a `MARKET` order when the conditions
        are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)

        `STOP_LOSS_LIMIT` | `timeInForce`, `quantity`,  `price`, `stopPrice` or `trailingDelta`

        `TAKE_PROFIT` | `quantity`, `stopPrice` or `trailingDelta` | This will execute a `MARKET` order when the
        conditions are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)

        `TAKE_PROFIT_LIMIT` | `timeInForce`, `quantity`, `price`, `stopPrice` or `trailingDelta` |

        `LIMIT_MAKER` | `quantity`, `price`| This is a `LIMIT` order that will be rejected if the order immediately
        matches and trades as a taker. <br/> This is also known as a POST-ONLY order.



        Notes on using parameters for Pegged Orders:

        ::span{#pegged-orders-info}


        * These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.

        * If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.

        * `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as
        your order.

        * `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book
        from your order.

        * Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters
        must be specified together.


        Other info:

        * Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`.

        * Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`.

        * For `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` and `TAKE_PROFIT` orders, `trailingDelta` can be
        combined with `stopPrice`.

        * `MARKET` orders using `quoteOrderQty` will not break `LOT_SIZE` filter rules; the order will execute a
        `quantity` that will have the notional value as close as possible to `quoteOrderQty`. Trigger order price rules
        against market price for both MARKET and LIMIT versions:
          * Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`
          * Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        根据 order `type`的不同，某些参数 有强制要求，具体如下:


        ::span{#order-type}


        Type | 强制要求的参数 | 其他信息

        ------------ | ------------ | ------------

        `LIMIT` | `timeInForce`, `quantity`, `price`

        `MARKET` | `quantity` |  市价买卖单可用`quantity`参数来设置`base asset`数量.<br/> 例如：BTCUSDT 市价单，BTC 买卖数量取决于`quantity`参数.
        <br/><br/>市价买卖单可用`quoteOrderQty`参数来设置`quote asset`数量. 正确的`quantity`取决于市场的流动性与`quoteOrderQty`<br/> 例如: 市价 `BUY`
        BTCUSDT，单子会基于`quoteOrderQty`- USDT 的数量，购买 BTC.<br/> 市价 `SELL` BTCUSDT，单子会卖出 BTC 来满足`quoteOrderQty`- USDT 的数量.

        `STOP_LOSS` | `quantity`, `stopPrice`, `trailingDelta` | 条件满足后会下`MARKET`单子.
        (例如：达到`stopPrice`或`trailingDelta`被启动)

        `STOP_LOSS_LIMIT` | `timeInForce`, `quantity`,  `price`, `stopPrice`, `trailingDelta`

        `TAKE_PROFIT` | `quantity`, `stopPrice`, `trailingDelta` | 条件满足后会下`MARKET`单子.
        (例如：达到`stopPrice`或`trailingDelta`被启动)

        `TAKE_PROFIT_LIMIT` | `timeInForce`, `quantity`, `price`, `stopPrice`, `trailingDelta`

        `LIMIT_MAKER` | `quantity`, `price` |
        订单大部分情况下与普通的限价单没有区别，但是如果在当前价格会立即吃对手单并成交则下单会被拒绝。因此使用这个订单类型可以保证订单一定是挂单方，不会成为吃单方。



        关于挂钩订单参数的注意事项：

        ::span{#pegged-orders-info}


        * 这些参数仅适用于 `LIMIT`， `LIMIT_MAKER`， `STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。

        * 如果使用了 `pegPriceType`， 那么 `price` 字段将是可选的。 否则，`price` 字段依旧是必须的。

        * `pegPriceType=PRIMARY_PEG` 就是主要挂钩（`primary`），这是订单簿上与您的订单同一方向的最佳价格。

        * `pegPriceType=MARKET_PEG` 就是市场挂钩（`market`），这是订单簿上与您的订单相反方向的最佳价格。

        * 可以通过使用 `pegOffsetType` 和 `pegOffsetValue` 来获取最佳价格以外的价格水平。 这两个参数必须一起使用。


        其他:

        * 任何`LIMIT`或`LIMIT_MAKER`只要填`icebergQty`参数都可以下冰上订单。

        * 冰山订单的 `timeInForce`必须设置为`GTC`。

        * `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` 与 `TAKE_PROFIT` 单子都能同时填上`trailingDelta`与`stopPrice`。

        * 填上`quoteOrderQty`的市价单不会触犯过滤器的`LOT_SIZE`限制。订单的`quantity`会尽量满足`quoteOrderQty`的数量。


        条件单的触发价格必须:

        * 比下单时当前市价高: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`

        * 比下单时当前市价低: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - type
                - timestamp
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
                quantity:
                  type: number
                  format: float
                  example: 1
                quoteOrderQty:
                  type: number
                  format: float
                  example: 1
                price:
                  type: number
                  format: float
                  example: 400
                newClientOrderId:
                  type: string
                  example: myOrder1
                  description: >-
                    A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same
                    `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be
                    rejected.
                  x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。
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
                stopPrice:
                  type: number
                  format: float
                  example: 1
                  description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                  x-description-cn: 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。
                trailingDelta:
                  type: integer
                  format: int64
                  example: 1
                  description: See Trailing Stop order FAQ
                  x-description-cn: 参见 追踪止盈止损(Trailing Stop)订单常见问题
                icebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
                  x-description-cn: 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                newOrderRespType:
                  type: string
                  example: ACK
                  enum:
                    - ACK
                    - RESULT
                    - FULL
                  description: "`MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`."
                  x-description-cn: "`MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。"
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
                  x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: New order
          x-description-cn: 下单
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`ACK` response type:"
                    x-description-cn: "`ACK` 响应类型：返回速度最快，不包含成交信息，信息量最少"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      orderId:
                        type: integer
                        format: int64
                        example: 28
                      orderListId:
                        type: integer
                        format: int64
                        description: Unless it's part of an order list, value will be -1
                        x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                        example: -1
                      clientOrderId:
                        type: string
                        example: 6gCrw2kRUAF9CvJDGP16IP
                      transactTime:
                        type: integer
                        format: int64
                        example: 1507725176595
                  - description: "`RESULT` response type:"
                    x-description-cn: "`RESULT` 响应类型：返回速度居中，返回吃单成交的少量信息"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      orderId:
                        type: integer
                        format: int64
                        example: 28
                      orderListId:
                        type: integer
                        format: int64
                        description: Unless it's part of an order list, value will be -1
                        x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                        example: -1
                      clientOrderId:
                        type: string
                        example: 6gCrw2kRUAF9CvJDGP16IP
                      transactTime:
                        type: integer
                        format: int64
                        example: 1507725176595
                      price:
                        type: string
                        example: "0.00000000"
                      origQty:
                        type: string
                        example: "10.00000000"
                      executedQty:
                        type: string
                        example: "10.00000000"
                      origQuoteOrderQty:
                        type: string
                        example: "0.000000"
                      cummulativeQuoteQty:
                        type: string
                        example: "10.00000000"
                      status:
                        type: string
                        example: FILLED
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: MARKET
                      side:
                        type: string
                        example: SELL
                      workingTime:
                        type: integer
                        format: int64
                        example: 1507725176595
                      selfTradePreventionMode:
                        type: string
                        example: NONE
                  - description: "`FULL` response type:"
                    x-description-cn: "`FULL` 响应类型：返回速度最慢，返回吃单成交的详细信息"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      orderId:
                        type: integer
                        format: int64
                        example: 28
                      orderListId:
                        type: integer
                        format: int64
                        example: -1
                        description: Unless it's part of an order list, value will be -1
                        x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                      clientOrderId:
                        type: string
                        example: 6gCrw2kRUAF9CvJDGP16IP
                      transactTime:
                        type: integer
                        format: int64
                        example: 1507725176595
                      price:
                        type: string
                        example: "1.00000000"
                      origQty:
                        type: string
                        example: "10.00000000"
                      executedQty:
                        type: string
                        example: "10.00000000"
                      origQuoteOrderQty:
                        type: string
                        example: "0.000000"
                      cummulativeQuoteQty:
                        type: string
                        example: "10.00000000"
                      status:
                        type: string
                        example: FILLED
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: MARKET
                      side:
                        type: string
                        example: SELL
                      workingTime:
                        type: integer
                        format: int64
                        example: 1507725176595
                      selfTradePreventionMode:
                        type: string
                        example: NONE
                      fills:
                        type: array
                        example:
                          - price: "4000.00000000"
                            qty: "1.00000000"
                            commission: "4.00000000"
                            commissionAsset: USDT
                            tradeId: 56
                          - price: "3999.00000000"
                            qty: "5.00000000"
                            commission: "19.99500000"
                            commissionAsset: USDT
                            tradeId: 57
                          - price: "3998.00000000"
                            qty: "2.00000000"
                            commission: "7.99600000"
                            commissionAsset: USDT
                            tradeId: 58
                          - price: "3997.00000000"
                            qty: "1.00000000"
                            commission: "3.99700000"
                            commissionAsset: USDT
                            tradeId: 59
                          - price: "3995.00000000"
                            qty: "1.00000000"
                            commission: "3.99500000"
                            commissionAsset: USDT
                            tradeId: 60
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              example: "4000.00000000"
                            qty:
                              type: string
                              example: "1.00000000"
                            commission:
                              type: string
                              example: "4.00000000"
                            commissionAsset:
                              type: string
                              example: USDT
                            tradeId:
                              type: integer
                              format: int64
                              example: 56
  /api/v3/orderList:
    get:
      summary: Query Order list (USER_DATA)
      x-summary-cn: 查询订单列表 (USER_DATA)
      description: Retrieves a specific order list based on provided optional parameters.
      x-description-cn: 根据提供的可选参数检索特定的订单列表。
      tags:
        - account
      operationId: getOrderList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#get-order-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/getOrderList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/get_order_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/get_order_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/GetOrderListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/GetOrderList/GetOrderList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/GetOrderListExample.php
      x-ip-weight: 4
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
        - name: orderListId
          in: query
          required: false
          description: Query order list by `orderListId`. `orderListId` or `origClientOrderId` must be provided.
          x-description-cn: 通过 `orderListId` 获取订单列表。必须提供 `orderListId` 或 `origClientOrderId`。
          schema:
            type: integer
            format: int64
            example: 27
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: 1
          description: Query order list by `listClientOrderId`. `orderListId` or `origClientOrderId` must be provided.
          x-description-cn: 通过 `listClientOrderId` 查询订单列表。`orderListId` 或 `origClientOrderId` 必须被提供。
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Query Order list
          x-description-cn: 查询订单列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    format: int64
                    example: 27
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
                    example: h2USkA5YQpaXHPIrkd96xE
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1565245656253
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 4
                        clientOrderId: qD1gy3kc3Gx0rihm9Y3xwS
                      - symbol: LTCBTC
                        orderId: 5
                        clientOrderId: ARzZ9I00CPM8i3NhmU9Ega
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 4
                        clientOrderId:
                          type: string
                          example: qD1gy3kc3Gx0rihm9Y3xwS
    delete:
      summary: Cancel Order list (TRADE)
      x-summary-cn: 取消订单列表 (TRADE)
      description: Cancel an entire Order list
      x-description-cn: 取消整个订单列表。
      tags:
        - trade
      operationId: deleteOrderList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#delete-order-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/deleteOrderList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/delete_order_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/delete_order_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/DeleteOrderListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/DeleteOrderList/DeleteOrderList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/DeleteOrderListExample.php
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
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: orderListId
          in: query
          required: false
          description: Either `orderListId` or `listClientOrderId` must be provided
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
          schema:
            type: integer
            format: int64
            example: 1
        - name: listClientOrderId
          in: query
          required: false
          description: Either `orderListId` or `listClientOrderId` must be provided
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
          schema:
            type: string
            example: C3wyj4WVEktd7u9aVBRXcN
        - name: newClientOrderId
          in: query
          required: false
          description: Used to uniquely identify this cancel. Automatically generated by default.
          x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
          schema:
            type: string
            example: cancelMyOrder1
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: |-
        **Data Source:** Matching Engine

        **Notes:**
          - Canceling an individual order from an order list will cancel the entire order list.
          - If both orderListId and listClientOrderId parameters are provided, the orderListId is searched first, then the listClientOrderId from that result is checked against that order. If both conditions are not met the request will be rejected.
      x-parameters-notes-cn: |-
        **数据源:** 撮合引擎

        **其他注意点:**
          - 取消订单列表中的单个订单将取消整个订单列表.
          - 当同时提供 orderListId 和 listClientOrderId 两个参数时，系统首先将会使用 orderListId 来搜索订单。然后， 查找结果中的 listClientOrderId 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。
      responses:
        "200":
          description: Cancel Order list
          x-description-cn: 取消订单列表
          content:
            application/json:
              schema:
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
                    example: ALL_DONE
                  listOrderStatus:
                    type: string
                    example: ALL_DONE
                  listClientOrderId:
                    type: string
                    example: C3wyj4WVEktd7u9aVBRXcN
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1574040868128
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 2
                        clientOrderId: pO9ufTiFGg3nw2fOdgeOXa
                      - symbol: LTCBTC
                        orderId: 3
                        clientOrderId: TXOvglzXuaubXAaENpaRCB
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 2
                        clientOrderId:
                          type: string
                          example: pO9ufTiFGg3nw2fOdgeOXa
                  orderReports:
                    type: array
                    example:
                      - symbol: LTCBTC
                        origClientOrderId: pO9ufTiFGg3nw2fOdgeOXa
                        orderId: 2
                        orderListId: 0
                        clientOrderId: unfWT8ig8i0uj6lPuYLez6
                        transactTime: 1688005070874
                        price: "1.00000000"
                        origQty: "10.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: CANCELED
                        timeInForce: GTC
                        type: STOP_LOSS_LIMIT
                        side: SELL
                        stopPrice: "1.00000000"
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        origClientOrderId: TXOvglzXuaubXAaENpaRCB
                        orderId: 3
                        orderListId: 0
                        clientOrderId: unfWT8ig8i0uj6lPuYLez6
                        transactTime: 1688005070874
                        price: "3.00000000"
                        origQty: "10.00000000"
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
                          example: LTCBTC
                        origClientOrderId:
                          type: string
                          example: pO9ufTiFGg3nw2fOdgeOXa
                        orderId:
                          type: integer
                          format: int64
                          example: 2
                        orderListId:
                          type: integer
                          format: int64
                          example: 0
                        clientOrderId:
                          type: string
                          example: unfWT8ig8i0uj6lPuYLez6
                        transactTime:
                          type: integer
                          format: int64
                          example: 1688005070874
                        price:
                          type: string
                          example: "1.00000000"
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
  /api/v3/myAllocations:
    get:
      summary: Query Allocations (USER_DATA)
      x-summary-cn: 查询分配结果 (USER_DATA)
      description: Retrieves allocations resulting from SOR order placement.
      x-description-cn: 检索由 SOR 订单生成引起的分配结果。
      tags:
        - account
      operationId: myAllocations
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-allocations
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/myAllocations.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/my_allocations.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/my_allocations.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/MyAllocationsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/MyAllocations/MyAllocations.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/MyAllocationsExample.php
      x-ip-weight: 20
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
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: fromAllocationId
          in: query
          required: false
          schema:
            type: integer
            example: 0
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: |-
        **Data Source:** Database"

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

        参数                                  | 响应 |
        ------------------------------------------- | -------- |
        `symbol`                                    | 按从最旧到最新排序的分配 |
        `symbol` + `startTime`                      | 从 `startTime` 开始的最旧的分配 |
        `symbol` + `endTime`                        | 到 `endTime` 为止的最新的分配 |
        `symbol` + `startTime` + `endTime`          | 在指定时间范围内的分配 |
        `symbol` + `fromAllocationId`               | 从指定 `AllocationId` 开始的分配  |
        `symbol` + `orderId`                        | 按从最旧到最新排序并和特定订单关联的分配 |
        `symbol` + `orderId` + `fromAllocationId`   | 从指定 `AllocationId` 开始并和特定订单关联的分配 |

        **注意:** `startTime` 和 `endTime` 之间的时间不能超过 24 小时。
      responses:
        "200":
          description: Query Allocations
          x-description-cn: 查询分配结果
          content:
            application/json:
              schema:
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
                      example: 1
                    orderListId:
                      type: integer
                      format: int64
                      example: -1
                    price:
                      type: string
                      example: "1.00000000"
                    qty:
                      type: string
                      example: "5.00000000"
                    quoteQty:
                      type: string
                      example: "5.00000000"
                    commission:
                      type: string
                      example: "0.00000000"
                    commissionAsset:
                      type: string
                      example: BTC
                    time:
                      type: integer
                      format: int64
                      example: 1687506878118
                    isBuyer:
                      type: boolean
                      example: true
                    isMaker:
                      type: boolean
                      example: false
                    isAllocator:
                      type: boolean
                      example: false
  /api/v3/myFilters:
    get:
      summary: Query relevant filters (USER_DATA)
      x-summary-cn: 查询相关过滤器 (USER_DATA)
      description: >-
        Retrieves the list of [filters](/products/spot/filters) relevant to an account on a given symbol. This is the
        only endpoint that shows if an account has [`MAX_ASSET`](/products/spot/filters#max_asset) filters applied to
        it.
      x-description-cn: >-
        用于检索一个账户上指定交易对的 [filters](/products/spot/filters) 列表。这是唯一一个目前会显示账户是否应用了
        [`MAX_ASSET`](/products/spot/filters#max_asset) 过滤器的端点。
      tags:
        - account
      operationId: myFilters
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-filters
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/myFilters.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/my_filters.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/my_filters.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/MyFiltersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/MyFilters/MyFilters.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/MyFiltersExample.php
      x-ip-weight: 40
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
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Query relevant filters
          x-description-cn: 查询相关过滤器
          content:
            application/json:
              schema:
                type: object
                properties:
                  exchangeFilters:
                    type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ORDERS
                            maxNumOrders:
                              type: integer
                              format: int64
                              example: 1000
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ALGO_ORDERS
                            maxNumAlgoOrders:
                              type: integer
                              format: int64
                              example: 200
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
                            maxNumIcebergOrders:
                              type: integer
                              format: int64
                              example: 10
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ORDER_LISTS
                            maxNumOrderLists:
                              type: integer
                              format: int64
                              example: 20
                      discriminator:
                        propertyName: filterType
                        mapping:
                          EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
                          EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
                          EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
                          EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
                  symbolFilters:
                    type: array
                    items:
                      oneOf:
                        - type: object
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
                        - type: object
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
                        - type: object
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
                        - type: object
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
                        - type: object
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
                        - type: object
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
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: ICEBERG_PARTS
                            limit:
                              type: integer
                              format: int64
                              example: 10
                        - type: object
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
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: MAX_NUM_ORDERS
                            maxNumOrders:
                              type: integer
                              format: int64
                              example: 200
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: MAX_NUM_ALGO_ORDERS
                            maxNumAlgoOrders:
                              type: integer
                              format: int64
                              example: 10
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: MAX_NUM_ICEBERG_ORDERS
                            maxNumIcebergOrders:
                              type: integer
                              format: int64
                              example: 5
                        - type: object
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
                        - type: object
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
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: T_PLUS_SELL
                            endTime:
                              type: integer
                              format: int64
                              example: 1741672924895
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: MAX_NUM_ORDER_LISTS
                            maxNumOrderLists:
                              type: integer
                              format: int64
                              example: 20
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: MAX_NUM_ORDER_AMENDS
                            maxNumOrderAmends:
                              type: integer
                              format: int64
                              example: 10
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
                    type: array
                    items:
                      oneOf:
                        - type: object
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
                              example: "100.00000000"
                            asset:
                              type: string
                              example: BNB
                      discriminator:
                        propertyName: filterType
                        mapping:
                          MAX_ASSET: "#/components/schemas/MaxAssetFilter"
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
                          example: 321
  /api/v3/myPreventedMatches:
    get:
      summary: Query Prevented Matches (USER_DATA)
      x-summary-cn: 获取 Prevented Matches (USER_DATA)
      description: |-
        Displays the list of orders that were expired due to STP.

        These are the combinations supported:
          - `symbol` + `preventedMatchId`
          - `symbol` + `orderId`
          - `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
          - `symbol` + `orderId` + `fromPreventedMatchId` + `limit`
      x-description-cn: |-
        获取因 STP 而过期的订单列表。

        这些是支持的组合：
          - `symbol` + `preventedMatchId`
          - `symbol` + `orderId`
          - `symbol` + `orderId` + `fromPreventedMatchId` (`limit` 默认为 500)
          - `symbol` + `orderId` + `fromPreventedMatchId` + `limit`
      tags:
        - account
      operationId: myPreventedMatches
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-prevented-matches
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/myPreventedMatches.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/my_prevented_matches.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/my_prevented_matches.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/MyPreventedMatchesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/MyPreventedMatches/MyPreventedMatches.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/MyPreventedMatchesExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: preventedMatchId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: fromPreventedMatchId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Query Prevented Matches
          x-description-cn: 获取 Prevented Matches
          content:
            application/json:
              schema:
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
  /api/v3/myTrades:
    get:
      summary: Account trade list (USER_DATA)
      x-summary-cn: 账户成交历史 (USER_DATA)
      description: Get trades for a specific account and symbol.
      x-description-cn: 获取某交易对的成交历史
      tags:
        - account
      operationId: myTrades
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/myTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/my_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/my_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/MyTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/MyTrades/MyTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/MyTradesExample.php
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
          required: true
          schema:
            type: string
            example: BNBBTC
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 100234
          description: This can only be used in combination with `symbol`.
          x-description-cn: 必须要和参数`symbol`一起使用。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: fromId
          in: query
          required: false
          description: TradeId to fetch from. Default gets most recent trades.
          x-description-cn: 返回该fromId之后的成交，缺省返回最近的成交
          schema:
            type: integer
            format: int64
            example: 1
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: |-
        **Data Source:** Memory => Database

        **Notes:**:
        - If `fromId` is set, it will get trades >= that `fromId`. Otherwise most recent trades are returned.
        - The time between `startTime` and `endTime` can't be longer than 24 hours.
        - These are the supported combinations of all parameters:
          - `symbol`
          - `symbol` + `orderId`
          - `symbol` + `startTime`
          - `symbol` + `endTime`
          - `symbol` + `fromId`
          - `symbol` + `startTime` + `endTime`
          - `symbol`+ `orderId` + `fromId`
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        **备注:** 
        - 如果设置了 `fromId`, 会返回ID大于此 `fromId` 的交易. 不然则会返回最近的交易。
        - `startTime` 和 `endTime` 设置的时间间隔不能超过24小时。
        - 支持的所有参数组合:
          - `symbol`
          - `symbol` + `orderId`
          - `symbol` + `startTime`
          - `symbol` + `endTime`
          - `symbol` + `fromId`
          - `symbol` + `startTime` + `endTime`
          - `symbol`+ `orderId` + `fromId`
      responses:
        "200":
          description: Account trade list
          x-description-cn: 账户成交历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BNBBTC
                    id:
                      type: integer
                      format: int64
                      example: 28457
                    orderId:
                      type: integer
                      format: int64
                      example: 100234
                    orderListId:
                      type: integer
                      format: int64
                      example: -1
                    price:
                      type: string
                      example: "4.00000100"
                    qty:
                      type: string
                      example: "12.00000000"
                    quoteQty:
                      type: string
                      example: "48.000012"
                    commission:
                      type: string
                      example: "10.10000000"
                    commissionAsset:
                      type: string
                      example: BNB
                    time:
                      type: integer
                      format: int64
                      example: 1499865549590
                    isBuyer:
                      type: boolean
                      example: true
                    isMaker:
                      type: boolean
                      example: false
                    isBestMatch:
                      type: boolean
                      example: true
  /api/v3/openOrderList:
    get:
      summary: Query Open Order lists (USER_DATA)
      x-summary-cn: 查询订单列表挂单 (USER_DATA)
      description: Query Open Order lists
      x-description-cn: 查询订单列表挂单
      tags:
        - account
      operationId: openOrderList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#open-order-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/openOrderList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/open_order_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/open_order_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/OpenOrderListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/OpenOrderList/OpenOrderList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/OpenOrderListExample.php
      x-ip-weight: 6
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
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Memory -> Database"
      x-parameters-notes-cn: "**数据源:** 缓存 => 数据库"
      responses:
        "200":
          description: Query Open Order lists
          x-description-cn: 查询订单列表挂单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderListId:
                      type: integer
                      format: int64
                      example: 31
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
                      example: wuB13fmulKj3YjdqWEcsnp
                    transactionTime:
                      type: integer
                      format: int64
                      example: 1565246080644
                    symbol:
                      type: string
                      example: LTCBTC
                    orders:
                      type: array
                      example:
                        - symbol: LTCBTC
                          orderId: 4
                          clientOrderId: r3EH2N76dHfLoSZWIUw1bT
                        - symbol: LTCBTC
                          orderId: 5
                          clientOrderId: Cv1SnyPD3qhqpbjpYEHbd2
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: LTCBTC
                          orderId:
                            type: integer
                            format: int64
                            example: 4
                          clientOrderId:
                            type: string
                            example: r3EH2N76dHfLoSZWIUw1bT
  /api/v3/order/amendments:
    get:
      summary: Query Order Amendments (USER_DATA)
      x-summary-cn: 查询改单 (USER_DATA)
      description: Queries all amendments of a single order.
      x-description-cn: 查询对一个订单的所有改单操作。
      tags:
        - account
      operationId: orderAmendments
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#order-amendments
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/orderAmendments.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/order_amendments.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/order_amendments.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/OrderAmendmentsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/OrderAmendments/OrderAmendments.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/OrderAmendmentsExample.php
      x-ip-weight: 4
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
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: orderId
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 9
        - name: fromExecutionId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 22
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
            default: 500
            maximum: 1000
        - name: recvWindow
          in: query
          required: false
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Query Order Amendments
          x-description-cn: 查询改单
          content:
            application/json:
              schema:
                type: array
                example:
                  - symbol: BTCUSDT
                    orderId: 9
                    executionId: 22
                    origClientOrderId: W0fJ9fiLKHOJutovPK3oJp
                    newClientOrderId: UQ1Np3bmQ71jJzsSDW9Vpi
                    origQty: "5.00000000"
                    newQty: "4.00000000"
                    time: 1741669661670
                  - symbol: BTCUDST
                    orderId: 9
                    executionId: 25
                    origClientOrderId: UQ1Np3bmQ71jJzsSDW9Vpi
                    newClientOrderId: 5uS0r35ohuQyDlCzZuYXq2
                    origQty: "4.00000000"
                    newQty: "3.00000000"
                    time: 1741672924895
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSDT
                    orderId:
                      type: integer
                      format: int64
                      example: 9
                    executionId:
                      type: integer
                      format: int64
                      example: 22
                    origClientOrderId:
                      type: string
                      example: W0fJ9fiLKHOJutovPK3oJp
                    newClientOrderId:
                      type: string
                      example: UQ1Np3bmQ71jJzsSDW9Vpi
                    origQty:
                      type: string
                      example: "5.00000000"
                    newQty:
                      type: string
                      example: "4.00000000"
                    time:
                      type: integer
                      format: int64
                      example: 1741669661670
  /api/v3/rateLimit/order:
    get:
      summary: Query Unfilled Order Count (USER_DATA)
      x-summary-cn: 查询未成交的订单计数 (USER_DATA)
      description: Displays the user's unfilled order count for all intervals.
      x-description-cn: 显示用户在所有时间间隔内的未成交订单计数。
      tags:
        - account
      operationId: rateLimitOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#rate-limit-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/AccountApi/rateLimitOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/account_api/rate_limit_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Account/rate_limit_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/account/RateLimitOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/AccountAPI/RateLimitOrder/RateLimitOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/account/RateLimitOrderExample.php
      x-ip-weight: 40
      x-legacy-anchors:
        - query-unfilled-order-count
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
          description: Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
          x-description-cn: 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
          schema:
            type: number
            format: float
            example: 5000
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the current
            client time and is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Query Unfilled Order Count
          x-description-cn: 查询未成交的订单计数
          content:
            application/json:
              schema:
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
  /api/v3/exchangeInfo:
    get:
      summary: Exchange information
      x-summary-cn: 交易规范信息
      description: Current exchange trading rules and symbol information
      x-description-cn: 获取此时的交易规范信息
      tags:
        - general
      operationId: exchangeInfo
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/GeneralApi/exchangeInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/general_api/exchange_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/General/exchange_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/general/ExchangeInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/GeneralAPI/ExchangeInfo/ExchangeInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/general/ExchangeInfoExample.php
      x-ip-weight: 20
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: false
          description: 'Example: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"'
          x-description-cn: 示例：curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"
          schema:
            type: string
            example: ETHBTC
        - name: symbols
          in: query
          required: false
          description: >-
            Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D"
            or curl -g -X GET 'https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC"]'
          x-description-cn: |-
            示例：curl -X GET
            "https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D"
            <br/> 或 <br/> curl -g -X GET
            'https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC"]'
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBBTC
            items:
              type: string
              example: BTCUSDT
        - name: permissions
          in: query
          required: false
          description: |-
            Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT"

            curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D"
            or
            curl -g -X GET 'https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED"]'
          x-description-cn: |-
            示例：curl -X GET
            "https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT" <br/>
            or <br/> curl -X GET
            "https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D"
            <br/> or <br/> curl -g -X GET
            'https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED"]'
          schema:
            type: array
            example:
              - SPOT
            items:
              type: string
              example: SPOT
              enum:
                - SPOT
                - MARGIN
                - LEVERAGED
                - TRD_GRP_002
                - TRD_GRP_003
                - TRD_GRP_004
                - TRD_GRP_005
                - TRD_GRP_006
                - TRD_GRP_007
                - TRD_GRP_008
                - TRD_GRP_009
                - TRD_GRP_010
                - TRD_GRP_011
                - TRD_GRP_012
                - TRD_GRP_013
                - TRD_GRP_014
                - TRD_GRP_015
                - TRD_GRP_016
                - TRD_GRP_017
                - TRD_GRP_018
                - TRD_GRP_019
                - TRD_GRP_020
                - TRD_GRP_021
                - TRD_GRP_022
                - TRD_GRP_023
                - TRD_GRP_024
                - TRD_GRP_025
        - name: showPermissionSets
          in: query
          required: false
          description: Controls whether the content of the `permissionSets` field is populated or not.
          x-description-cn: 用于控制是否提供 `permissionSets` 字段的内容。
          schema:
            type: boolean
            example: false
            default: true
        - name: symbolStatus
          in: query
          required: false
          schema:
            type: string
            example: TRADING
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
          description: >-
            Filters for symbols that have this `tradingStatus`. Cannot be used in combination with `symbols` or
            `symbol`.
          x-description-cn: 用于过滤具有此 `tradingStatus` 的交易对。不能与 `symbols` 或 `symbol` 组合使用。
      x-parameters-notes: >-
        **Data Source:** Memory


        **Notes:**

        * If the value provided to `symbol` or `symbols` do not exist, the endpoint will throw an error saying the
        symbol is invalid.

        * All parameters are optional.

        * `permissions` can support single or multiple values (e.g. `SPOT`, `["MARGIN","LEVERAGED"]`). This cannot be
        used in combination with `symbol` or `symbols`.

        * If `permissions` parameter not provided, all symbols that have either `SPOT`, `MARGIN`, or `LEVERAGED`
        permission will be exposed.
          * To display symbols with any permission you need to specify them explicitly in `permissions`: (e.g. `["SPOT","MARGIN",...]`.). See Account and Symbol Permissions for the full list.

        ::span{#examples-of-symbol-permissions-interpretation-from-the-response}


        **Examples of Symbol Permissions Interpretation from the Response:**


        * `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".

        * `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".

        * `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or
        permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B"
        and permission "C".)
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        **备注**:
          - 如果参数 `symbol` 或者 `symbols` 提供的交易对不存在, 系统会返回错误并提示交易对不正确。
          - 所有的参数都是可选的。
          - `permissions` 可以支持单个或多个值（例如 `SPOT`, `["MARGIN","LEVERAGED"]`）。此参数不能与 `symbol` 或 `symbols` 组合使用。
          - 如果未提供 `permissions` 参数，那么所有具有 `SPOT`、`MARGIN` 或 `LEVERAGED` 权限的交易对都将被返回。
            - 要显示具有任何权限的交易对，您需要在 `permissions` 中明确指定它们：（例如 `["SPOT","MARGIN",...]`)。有关完整列表，请参阅 [可用权限]
            
        ::span{#examples-of-symbol-permissions-interpretation-from-the-response}

        **解释响应中的 `permissionSets`：**
          - `[["A","B"]]` 有权限"A"**或**权限"B"的账户可以下订单。
          - `[["A"],["B"]]` 有权限"A"**和**权限"B"的账户可以下订单。
          - `[["A"],["B","C"]]` 有权限"A"**和**权限"B"或权限"C"的账户可以下订单。（此处应用的是包含或，而不是排除或，因此账户可以同时拥有权限"B"和权限"C"。）
      responses:
        "200":
          description: Exchange information
          x-description-cn: 交易规范信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  timezone:
                    type: string
                    example: UTC
                  serverTime:
                    type: integer
                    format: int64
                    example: 1565246363776
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
                          example: 321
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
                      oneOf:
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ORDERS
                            maxNumOrders:
                              type: integer
                              format: int64
                              example: 1000
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ALGO_ORDERS
                            maxNumAlgoOrders:
                              type: integer
                              format: int64
                              example: 200
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
                            maxNumIcebergOrders:
                              type: integer
                              format: int64
                              example: 10
                        - type: object
                          properties:
                            filterType:
                              type: string
                              example: EXCHANGE_MAX_NUM_ORDER_LISTS
                            maxNumOrderLists:
                              type: integer
                              format: int64
                              example: 20
                      discriminator:
                        propertyName: filterType
                        mapping:
                          EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
                          EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
                          EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
                          EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
                  symbols:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: ETHBTC
                        status:
                          type: string
                          example: TRADING
                        baseAsset:
                          type: string
                          example: ETH
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
                          description: will be removed in future api versions (v4+)
                          x-description-cn: 将在未来的 api 版本中移除 (v4+)
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
                            - STOP_LOSS
                            - STOP_LOSS_LIMIT
                            - TAKE_PROFIT
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
                          example: false
                        cancelReplaceAllowed:
                          type: boolean
                          example: false
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
                          items:
                            oneOf:
                              - type: object
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
                              - type: object
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
                              - type: object
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
                              - type: object
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
                              - type: object
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
                              - type: object
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
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: ICEBERG_PARTS
                                  limit:
                                    type: integer
                                    format: int64
                                    example: 10
                              - type: object
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
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: MAX_NUM_ORDERS
                                  maxNumOrders:
                                    type: integer
                                    format: int64
                                    example: 200
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: MAX_NUM_ALGO_ORDERS
                                  maxNumAlgoOrders:
                                    type: integer
                                    format: int64
                                    example: 10
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: MAX_NUM_ICEBERG_ORDERS
                                  maxNumIcebergOrders:
                                    type: integer
                                    format: int64
                                    example: 5
                              - type: object
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
                              - type: object
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
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: T_PLUS_SELL
                                  endTime:
                                    type: integer
                                    format: int64
                                    example: 1741672924895
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: MAX_NUM_ORDER_LISTS
                                  maxNumOrderLists:
                                    type: integer
                                    format: int64
                                    example: 20
                              - type: object
                                properties:
                                  filterType:
                                    type: string
                                    example: MAX_NUM_ORDER_AMENDS
                                  maxNumOrderAmends:
                                    type: integer
                                    format: int64
                                    example: 10
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
                        permissions:
                          type: array
                          items:
                            type: string
                            example: undefined
                        permissionSets:
                          type: array
                          items:
                            type: array
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
                          items:
                            type: string
                            example: BTCUSDT
              example:
                timezone: UTC
                serverTime: 1565246363776
                rateLimits:
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
                  - rateLimitType: RAW_REQUESTS
                    interval: MINUTE
                    intervalNum: 5
                    limit: 61000
                exchangeFilters: []
                symbols:
                  - symbol: ETHBTC
                    status: TRADING
                    baseAsset: ETH
                    baseAssetPrecision: 8
                    quoteAsset: BTC
                    quotePrecision: 8
                    quoteAssetPrecision: 8
                    baseCommissionPrecision: 8
                    quoteCommissionPrecision: 8
                    orderTypes:
                      - LIMIT
                      - LIMIT_MAKER
                      - MARKET
                      - STOP_LOSS
                      - STOP_LOSS_LIMIT
                      - TAKE_PROFIT
                      - TAKE_PROFIT_LIMIT
                    icebergAllowed: true
                    ocoAllowed: true
                    otoAllowed: true
                    opoAllowed: true
                    quoteOrderQtyMarketAllowed: true
                    allowTrailingStop: false
                    cancelReplaceAllowed: false
                    amendAllowed: false
                    pegInstructionsAllowed: true
                    marketQuoteNotionalLimitAllowed: true
                    limitQuoteNotionalLimitAllowed: true
                    isSpotTradingAllowed: true
                    isMarginTradingAllowed: true
                    filters: []
                    permissions: []
                    permissionSets:
                      - - SPOT
                        - MARGIN
                    defaultSelfTradePreventionMode: NONE
                    allowedSelfTradePreventionModes:
                      - NONE
                sors:
                  - baseAsset: BTC
                    symbols:
                      - BTCUSDT
                      - BTCUSDC
  /api/v3/executionRules:
    get:
      summary: Query Execution Rules
      x-summary-cn: 查询执行规则
      description: Query execution rules for symbols.
      x-description-cn: 查询交易对的执行规则。
      tags:
        - general
      operationId: executionRules
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#execution-rules
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/GeneralApi/executionRules.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/general_api/execution_rules.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/General/execution_rules.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/general/ExecutionRulesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/GeneralAPI/ExecutionRules/ExecutionRules.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/general/ExecutionRulesExample.php
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
      parameters:
        - name: symbol
          in: query
          required: false
          description: Query for specified symbol.
          x-description-cn: 查询指定的交易对。
          schema:
            type: string
            example: BAZUSD
        - name: symbols
          in: query
          required: false
          description: Query for multiple symbols.
          x-description-cn: 查询多个交易对。
          schema:
            type: array
            example:
              - BAZUSD
              - BNBUSDT
            items:
              type: string
              example: BAZUSD
        - name: symbolStatus
          in: query
          required: false
          description: Query for all symbols with the specified status.
          x-description-cn: 查询指定状态的所有交易对。
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
      x-parameters-notes: |-
        **Data Source:** Memory

        **Note:**: No combination of multiple parameters is allowed.
      x-parameters-notes-cn: |-
        **数据源:** 缓存

        **注意:** 不允许多个参数组合使用。
      responses:
        "200":
          description: Query execution rules
          x-description-cn: 查询执行规则
          content:
            application/json:
              schema:
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
  /api/v3/ping:
    get:
      summary: Test connectivity
      x-summary-cn: 测试服务器连通性 PING
      description: Test connectivity to the Rest API.
      x-description-cn: 测试能否联通
      tags:
        - general
      operationId: ping
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#ping
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/GeneralApi/ping.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/general_api/ping.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/General/ping.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/general/PingExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/GeneralAPI/Ping/Ping.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/general/PingExample.php
      x-ip-weight: 1
      x-security-type: NONE
      parameters: []
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: OK
          x-description-cn: 成功
  /api/v3/time:
    get:
      summary: Check server time
      x-summary-cn: 获取服务器时间
      description: Test connectivity to the Rest API and get the current server time.
      x-description-cn: 获取服务器时间
      tags:
        - general
      operationId: time
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#time
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/GeneralApi/time.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/general_api/time.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/General/time.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/general/TimeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/GeneralAPI/Time/Time.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/general/TimeExample.php
      x-ip-weight: 1
      x-security-type: NONE
      parameters: []
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Check server time
          x-description-cn: 获取服务器时间
          content:
            application/json:
              schema:
                type: object
                properties:
                  serverTime:
                    type: integer
                    format: int64
                    example: 1499827319559
  /api/v3/aggTrades:
    get:
      summary: Compressed/Aggregate trades list
      x-summary-cn: 近期成交(归集)
      description: >-
        Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price
        will have the quantity aggregated.
      x-description-cn: 与trades的区别是，同一个taker在同一时间同一价格与多个maker的成交会被合并为一条记录
      tags:
        - market
      operationId: aggTrades
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#agg-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/aggTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/agg_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/agg_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/AggTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/AggTrades/AggTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/AggTradesExample.php
      x-ip-weight: 4
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: fromId
          in: query
          required: false
          description: ID to get aggregate trades from INCLUSIVE.
          x-description-cn: 从包含fromID的成交开始返回结果
          schema:
            type: integer
            format: int64
            example: 1
        - name: startTime
          in: query
          required: false
          description: Timestamp in ms to get aggregate trades from INCLUSIVE.
          x-description-cn: 从该时刻之后的成交记录开始返回结果
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          description: Timestamp in ms to get aggregate trades until INCLUSIVE.
          x-description-cn: 返回该时刻为止的成交记录
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
      x-parameters-notes: |-
        **Data Source:** Database

        - If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        - 如果没有发送任何筛选参数(fromId, startTime, endTime)，默认返回最近的成交记录
      responses:
        "200":
          description: Compressed/Aggregate trades list
          x-description-cn: 近期成交(归集
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    a:
                      type: integer
                      format: int64
                      example: 26129
                      description: Aggregate tradeId
                      x-description-cn: 归集成交ID
                    p:
                      type: string
                      example: "0.01633102"
                      description: Price
                      x-description-cn: 成交价
                    q:
                      type: string
                      example: "4.70443515"
                      description: Quantity
                      x-description-cn: 成交量
                    f:
                      type: integer
                      format: int64
                      example: 27781
                      description: First tradeId
                      x-description-cn: 被归集的首个成交ID
                    l:
                      type: integer
                      format: int64
                      example: 27781
                      description: Last tradeId
                      x-description-cn: 被归集的末个成交ID
                    T:
                      type: integer
                      format: int64
                      example: 1498793709153
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
  /api/v3/avgPrice:
    get:
      summary: Current average price
      x-summary-cn: 当前平均价格
      description: Current average price for a symbol.
      x-description-cn: 当前平均价格
      tags:
        - market
      operationId: avgPrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#avg-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/avgPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/avg_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/avg_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/AvgPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/AvgPrice/AvgPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/AvgPriceExample.php
      x-ip-weight: 2
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Current average price
          x-description-cn: 当前平均价格
          content:
            application/json:
              schema:
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
                    example: "9.35751834"
                    description: Average price
                    x-description-cn: 平均价格
                  closeTime:
                    type: integer
                    format: int64
                    example: 1694061154503
                    description: Last trade time
                    x-description-cn: 最近成交时间
  /api/v3/depth:
    get:
      summary: Order book
      x-summary-cn: 深度信息
      description: Order book
      x-description-cn: 深度信息
      tags:
        - market
      operationId: depth
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#depth
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/depth.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/depth.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/depth.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/DepthExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/Depth/Depth.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/DepthExample.php
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
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: limit
          in: query
          required: false
          description: If limit > 5000, only 5000 entries will be returned.
          x-description-cn: 如果 limit > 5000, 最多返回5000条数据。
          schema:
            type: integer
            example: 1
            default: 100
            maximum: 5000
        - name: symbolStatus
          in: query
          required: false
          schema:
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
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Order book
          x-description-cn: 深度信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  lastUpdateId:
                    type: integer
                    format: int64
                    example: 1027024
                  bids:
                    type: array
                    description: Bid orders. Each entry is [price, quantity].
                    x-description-cn: 买单列表。每项为 [价格, 数量]。
                    example:
                      - - "4.00000000"
                        - "431.00000000"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          x-description-cn: 价位
                          example: "4.00000000"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "431.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            x-description-cn: 价位
                            example: "4.00000000"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "431.00000000"
                  asks:
                    type: array
                    description: Ask orders. Each entry is [price, quantity].
                    x-description-cn: 卖单列表。每项为 [价格, 数量]。
                    example:
                      - - "4.00000200"
                        - "12.00000000"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          x-description-cn: 价位
                          example: "4.00000200"
                        - type: string
                          description: Quantity
                          x-description-cn: 挂单量
                          example: "12.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            x-description-cn: 价位
                            example: "4.00000200"
                          - type: string
                            description: Quantity
                            x-description-cn: 挂单量
                            example: "12.00000000"
  /api/v3/trades:
    get:
      summary: Recent trades list
      x-summary-cn: 近期成交
      description: Get recent trades.
      x-description-cn: 获取近期成交
      tags:
        - market
      operationId: getTrades
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#get-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/getTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/get_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/get_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/GetTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/GetTrades/GetTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/GetTradesExample.php
      x-ip-weight: 25
      x-legacy-anchors:
        - trades
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Recent trades list
          x-description-cn: 近期成交
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      format: int64
                      example: 28457
                    price:
                      type: string
                      example: "4.00000100"
                    qty:
                      type: string
                      example: "12.00000000"
                    quoteQty:
                      type: string
                      example: "48.000012"
                    time:
                      type: integer
                      format: int64
                      example: 1499865549590
                    isBuyerMaker:
                      type: boolean
                      example: true
                    isBestMatch:
                      type: boolean
                      example: true
  /api/v3/historicalTrades:
    get:
      summary: Old trade lookup
      x-summary-cn: 查询历史成交
      description: Get older trades.
      x-description-cn: 查询历史成交
      tags:
        - market
      operationId: historicalTrades
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#historical-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/historicalTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/historical_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/historical_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/HistoricalTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/HistoricalTrades/HistoricalTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/HistoricalTradesExample.php
      x-ip-weight: 25
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
        - name: fromId
          in: query
          required: false
          description: TradeId to fetch from. Default gets most recent trades.
          x-description-cn: 从哪一条成交id开始返回，缺省返回最近的成交记录
          schema:
            type: integer
            format: int64
            example: 1
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Old trade lookup
          x-description-cn: 查询历史成交
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      format: int64
                      example: 28457
                    price:
                      type: string
                      example: "4.00000100"
                    qty:
                      type: string
                      example: "12.00000000"
                    quoteQty:
                      type: string
                      example: "48.000012"
                    time:
                      type: integer
                      format: int64
                      example: 1499865549590
                    isBuyerMaker:
                      type: boolean
                      example: true
                    isBestMatch:
                      type: boolean
                      example: true
  /api/v3/historicalBlockTrades:
    get:
      summary: Historical Block Trades (MARKET_DATA)
      x-summary-cn: 查询历史大宗交易 (MARKET_DATA)
      description: Get block trades.
      x-description-cn: 获取大宗交易记录。
      tags:
        - market
      operationId: historicalBlockTrades
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#historical-block-trades
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/historicalBlockTrades.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/historical_block_trades.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/historical_block_trades.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/HistoricalBlockTradesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/HistoricalBlockTrades/HistoricalBlockTrades.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/HistoricalBlockTradesExample.php
      x-ip-weight: 25
      x-security-type: MARKET_DATA
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBBTC
        - name: fromId
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 582
          description: Block trade ID to fetch from
          x-description-cn: 从该大宗交易ID开始查询
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 500
            default: 500
            maximum: 1000
          description: "Default: 500; Maximum: 1000"
          x-description-cn: "默认: 500; 最大: 1000"
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Historical Block Trades
          x-description-cn: 历史大宗交易
          content:
            application/json:
              schema:
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
  /api/v3/klines:
    get:
      summary: Kline/Candlestick data
      x-summary-cn: K线数据
      description: |-
        Kline/candlestick bars for a symbol.
        Klines are uniquely identified by their open time.
      x-description-cn: 每根K线的开盘时间可视为唯一ID
      tags:
        - market
      operationId: klines
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#klines
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/klines.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/klines.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/klines.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/KlinesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/Klines/Klines.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/KlinesExample.php
      x-ip-weight: 2
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: interval
          in: query
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
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: timeZone
          in: query
          required: false
          description: "Default: 0 (UTC)"
          x-description-cn: 默认值： 0 (UTC)
          schema:
            type: string
            example: "0"
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
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
      responses:
        "200":
          description: Kline/Candlestick data
          x-description-cn: K线数据
          content:
            application/json:
              schema:
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
  /api/v3/ticker:
    get:
      summary: Rolling window price change statistics
      x-summary-cn: 滚动窗口价格变动统计
      description: |-
        **Note:** This endpoint differs from `GET /api/v3/ticker/24hr`.

        The statistical time range of this endpoint can be up to 59999ms longer
        than the requested `windowSize`.

        `openTime` starts at the beginning of a minute, while the end time is
        the current time. Therefore, the actual interval can be up to 59999ms
        longer than the requested window.

        For example, if `closeTime` is 1641287867099 (January 04, 2022
        09:17:47:099 UTC) and `windowSize` is `1d`, then `openTime` is
        1641201420000 (January 3, 2022, 09:17:00 UTC).
      x-description-cn: |-
        **注意:** 此接口和 `GET /api/v3/ticker/24hr` 有所不同.

        此接口统计的时间范围比请求的`windowSize`多不超过59999ms.

        接口的 `openTime` 是某一分钟的起始，而结束是当前的时间. 所以实际的统计区间会比请求的时间窗口多不超过59999ms.

        比如, 结束时间 `closeTime` 是 1641287867099 (January 04, 2022 09:17:47:099 UTC)
        , `windowSize` 为 `1d`. 那么开始时间 `openTime` 则为 1641201420000 (January 3,
        2022, 09:17:00 UTC)
      tags:
        - market
      operationId: ticker
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/ticker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/TickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/Ticker/Ticker.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/TickerExample.php
      x-legacy-anchors:
        - rollingwindowticker
      x-security-type: NONE
      x-weight: |-
        4 for each requested symbol regardless of windowSize.

        The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.
      x-weight-cn: |-
        每个交易对占用 4 个权重，与 windowSize 无关。

        当请求中的 `symbols` 数量超过 50 时，此请求的权重上限为 200。
      parameters:
        - name: symbol
          in: query
          required: false
          description: Either `symbol` or `symbols` must be provided
          x-description-cn: 参数 `symbol` 和 `symbols` 不可以一起使用
          schema:
            type: string
            example: BNBUSDT
        - name: symbols
          in: query
          required: false
          description: >-
            Either `symbol` or `symbols` must be provided


            Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D


            The maximum number of symbols allowed in a request is 100.
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的ticker数据都会返回. symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBUSDT
            items:
              type: string
              example: BTCUSDT
        - name: windowSize
          in: query
          required: false
          description: Units cannot be combined (e.g. `1d2h` is not allowed).
          x-description-cn: 不可以组合使用, 比如`1d2h`
          schema:
            type: string
            example: 1m
            default: 1d
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
        - name: type
          in: query
          required: false
          schema:
            type: string
            example: FULL
            default: FULL
            enum:
              - FULL
              - MINI
        - name: symbolStatus
          in: query
          required: false
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
            description: |-
              Filters for symbols that have this `tradingStatus`.
              For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
              For multiple symbols, non-matching ones are simply excluded from the response.
            x-description-cn: |-
              过滤具有此 `tradingStatus` 的交易对。
              对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。
              对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。
      x-parameters-notes: "**Data Source:** Database"
      x-parameters-notes-cn: "**数据源:** 数据库"
      responses:
        "200":
          description: Rolling window price change statistics
          x-description-cn: Rolling 窗口 价格 修改 statistics
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`FULL` type, when using `symbol`:"
                    x-description-cn: "`FULL` 类型，使用参数 `symbol` 返回:"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: LTCBTC
                      priceChange:
                        type: string
                        example: "-8.00000000"
                        description: Absolute price change
                        x-description-cn: 价格变化
                      priceChangePercent:
                        type: string
                        example: "-88.889"
                        description: Relative price change in percent
                        x-description-cn: 价格变化百分比
                      weightedAvgPrice:
                        type: string
                        example: "2.60427807"
                        description: QuoteVolume / Volume
                        x-description-cn: QuoteVolume / 成交量
                      openPrice:
                        type: string
                        example: "0.10000000"
                      highPrice:
                        type: string
                        example: "2.00000000"
                      lowPrice:
                        type: string
                        example: "0.10000000"
                      lastPrice:
                        type: string
                        example: "2.00000000"
                      volume:
                        type: string
                        example: "39.00000000"
                      quoteVolume:
                        type: string
                        example: "13.40000000"
                        description: Sum of (price * volume) for all trades
                        x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                      openTime:
                        type: integer
                        format: int64
                        example: 1656986580000
                        description: Open time for ticker window
                        x-description-cn: ticker的开始时间
                      closeTime:
                        type: integer
                        format: int64
                        example: 1657001016795
                        description: Close time for ticker window
                        x-description-cn: ticker的结束时间
                      firstId:
                        type: integer
                        format: int64
                        example: 0
                        description: Trade IDs
                        x-description-cn: 统计时间内的第一笔trade id
                      lastId:
                        type: integer
                        format: int64
                        example: 34
                      count:
                        type: integer
                        format: int64
                        example: 35
                        description: Number of trades in the interval
                        x-description-cn: 统计时间内交易笔数
                  - description: "`FULL` type, when using `symbols`:"
                    x-description-cn: "`FULL` 类型，使用参数 `symbols` 返回:"
                    type: array
                    example:
                      - symbol: BTCUSDT
                        priceChange: "-154.13000000"
                        priceChangePercent: "-0.740"
                        weightedAvgPrice: "20677.46305250"
                        openPrice: "20825.27000000"
                        highPrice: "20972.46000000"
                        lowPrice: "20327.92000000"
                        lastPrice: "20671.14000000"
                        volume: "72.65112300"
                        quoteVolume: "1502240.91155513"
                        openTime: 1655432400000
                        closeTime: 1655446835460
                        firstId: 11147809
                        lastId: 11149775
                        count: 1967
                      - symbol: BNBBTC
                        priceChange: "0.00008530"
                        priceChangePercent: "0.823"
                        weightedAvgPrice: "0.01043129"
                        openPrice: "0.01036170"
                        highPrice: "0.01049850"
                        lowPrice: "0.01033870"
                        lastPrice: "0.01044700"
                        volume: "166.67000000"
                        quoteVolume: "1.73858301"
                        openTime: 1655432400000
                        closeTime: 1655446835460
                        firstId: 2351674
                        lastId: 2352034
                        count: 361
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        priceChange:
                          type: string
                          example: "-154.13000000"
                          description: Absolute price change
                          x-description-cn: 价格变化
                        priceChangePercent:
                          type: string
                          example: "-0.740"
                          description: Relative price change in percent
                          x-description-cn: 价格变化百分比
                        weightedAvgPrice:
                          type: string
                          example: "20677.46305250"
                          description: QuoteVolume / Volume
                          x-description-cn: QuoteVolume / 成交量
                        openPrice:
                          type: string
                          example: "20825.27000000"
                        highPrice:
                          type: string
                          example: "20972.46000000"
                        lowPrice:
                          type: string
                          example: "20327.92000000"
                        lastPrice:
                          type: string
                          example: "20671.14000000"
                        volume:
                          type: string
                          example: "72.65112300"
                        quoteVolume:
                          type: string
                          example: "1502240.91155513"
                          description: Sum of (price * volume) for all trades
                          x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                        openTime:
                          type: integer
                          format: int64
                          example: 1655432400000
                          description: Open time for ticker window
                          x-description-cn: ticker的开始时间
                        closeTime:
                          type: integer
                          format: int64
                          example: 1655446835460
                          description: Close time for ticker window
                          x-description-cn: ticker的结束时间
                        firstId:
                          type: integer
                          format: int64
                          example: 11147809
                          description: Trade IDs
                          x-description-cn: 统计时间内的第一笔trade id
                        lastId:
                          type: integer
                          format: int64
                          example: 11149775
                        count:
                          type: integer
                          format: int64
                          example: 1967
                          description: Number of trades in the interval
                          x-description-cn: 统计时间内交易笔数
                  - description: "`MINI` type, when using `symbol`:"
                    x-description-cn: "`MINI` 类型，使用参数 `symbol` 返回:"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: LTCBTC
                      openPrice:
                        type: string
                        example: "0.10000000"
                      highPrice:
                        type: string
                        example: "2.00000000"
                      lowPrice:
                        type: string
                        example: "0.10000000"
                      lastPrice:
                        type: string
                        example: "2.00000000"
                      volume:
                        type: string
                        example: "39.00000000"
                      quoteVolume:
                        type: string
                        description: Sum of (price * volume) for all trades
                        x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                        example: "13.40000000"
                      openTime:
                        type: integer
                        format: int64
                        description: Open time for ticker window
                        x-description-cn: ticker窗口的开始时间
                        example: 1656986580000
                      closeTime:
                        type: integer
                        format: int64
                        description: Close time for ticker window
                        x-description-cn: ticker窗口的结束时间
                        example: 1657001016795
                      firstId:
                        type: integer
                        format: int64
                        description: Trade IDs
                        x-description-cn: 首笔成交id
                        example: 0
                      lastId:
                        type: integer
                        format: int64
                        example: 34
                      count:
                        type: integer
                        format: int64
                        description: Number of trades in the interval
                        x-description-cn: 统计时间内交易笔数
                        example: 35
                  - description: "`MINI` type, when using `symbols`:"
                    x-description-cn: "`MINI` 类型，使用参数 `symbols` 返回:"
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNBBTC
                        openPrice:
                          type: string
                          example: "0.10000000"
                        highPrice:
                          type: string
                          example: "2.00000000"
                        lowPrice:
                          type: string
                          example: "0.10000000"
                        lastPrice:
                          type: string
                          example: "2.00000000"
                        volume:
                          type: string
                          example: "39.00000000"
                        quoteVolume:
                          type: string
                          description: Sum of (price * volume) for all trades
                          x-description-cn: 此k线内所有交易的price(价格) x volume(交易量)的总和
                          example: "13.40000000"
                        openTime:
                          type: integer
                          format: int64
                          description: Open time for ticker window
                          x-description-cn: ticker窗口的开始时间
                          example: 1656986880000
                        closeTime:
                          type: integer
                          format: int64
                          description: Close time for ticker window
                          x-description-cn: ticker窗口的结束时间
                          example: 1657001297799
                        firstId:
                          type: integer
                          format: int64
                          description: Trade IDs
                          x-description-cn: 首笔成交id
                          example: 0
                        lastId:
                          type: integer
                          format: int64
                          example: 34
                        count:
                          type: integer
                          format: int64
                          description: Number of trades in the interval
                          x-description-cn: 统计时间内交易笔数
                          example: 35
                    example:
                      - symbol: BNBBTC
                        openPrice: "0.10000000"
                        highPrice: "2.00000000"
                        lowPrice: "0.10000000"
                        lastPrice: "2.00000000"
                        volume: "39.00000000"
                        quoteVolume: "13.40000000"
                        openTime: 1656986880000
                        closeTime: 1657001297799
                        firstId: 0
                        lastId: 34
                        count: 35
                      - symbol: LTCBTC
                        openPrice: "0.07000000"
                        highPrice: "0.07000000"
                        lowPrice: "0.07000000"
                        lastPrice: "0.07000000"
                        volume: "33.00000000"
                        quoteVolume: "2.31000000"
                        openTime: 1656986880000
                        closeTime: 1657001297799
                        firstId: 0
                        lastId: 32
                        count: 33
  /api/v3/ticker/24hr:
    get:
      summary: 24hr ticker price change statistics
      x-summary-cn: 24hr价格变动情况
      description: 24 hour rolling window price change statistics. **Careful** when accessing this with no symbol.
      x-description-cn: 请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高
      tags:
        - market
      operationId: ticker24hr
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ticker24hr
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/ticker24hr.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ticker24hr.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ticker24hr.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/Ticker24hrExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/Ticker24hr/Ticker24hr.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/Ticker24hrExample.php
      x-legacy-anchors:
        - twentyfourhourticker
      x-security-type: NONE
      x-weight: |-
        <table>
          <thead>
              <tr>
                  <th>Parameter</th>
                  <th>Symbols Provided</th>
                  <th>Weight</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td rowspan="2">symbol</td>
                  <td>1</td>
                  <td>2</td>
              </tr>
              <tr>
                  <td>symbol parameter is omitted</td>
                  <td>80</td>
              </tr>
              <tr>
                  <td rowspan="4">symbols</td>
                  <td>1-20</td>
                  <td>2</td>
              </tr>
              <tr>
                  <td>21-100</td>
                  <td>40</td>
              </tr>
              <tr>
                  <td>101 or more</td>
                  <td>80</td>
              </tr>
              <tr>
                  <td>symbols parameter is omitted</td>
                  <td>80</td>
              </tr>
          </tbody>
        </table>
      x-weight-cn: |-
        <table>
          <thead>
              <tr>
                  <th>参数</th>
                  <th>提供Symbol数量</th>
                  <th>权重</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td rowspan="2">symbol</td>
                  <td>1</td>
                  <td>2</td>
              </tr>
              <tr>
                  <td>不提供 symbol 参数</td>
                  <td>80</td>
              </tr>
              <tr>
                  <td rowspan="4">symbols</td>
                  <td>1-20</td>
                  <td>2</td>
              </tr>
              <tr>
                  <td>21-100</td>
                  <td>40</td>
              </tr>
              <tr>
                  <td>101 或更多</td>
                  <td>80</td>
              </tr>
              <tr>
                  <td>不提供 symbols 参数</td>
                  <td>80</td>
              </tr>
          </tbody>
        </table>
      parameters:
        - name: symbol
          in: query
          required: false
          description: Either `symbol` or `symbols` must be provided
          x-description-cn: 参数 `symbol` 和 `symbols` 不可以一起使用
          schema:
            type: string
            example: BNBUSDT
        - name: symbols
          in: query
          required: false
          description: >-
            Either `symbol` or `symbols` must be provided


            Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D


            The maximum number of symbols allowed in a request is 100.
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的ticker数据都会返回. symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBUSDT
            items:
              type: string
              example: BTCUSDT
        - name: type
          in: query
          required: false
          schema:
            type: string
            example: FULL
            default: FULL
            enum:
              - FULL
              - MINI
        - name: symbolStatus
          in: query
          required: false
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
            description: |-
              Filters for symbols that have this `tradingStatus`.
              For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
              For multiple symbols, non-matching ones are simply excluded from the response.
            x-description-cn: |-
              过滤具有此 `tradingStatus` 的交易对。
              对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。
              对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: 24hr ticker price change statistics
          x-description-cn: 24hr ticker 价格 修改 statistics
          content:
            application/json:
              schema:
                oneOf:
                  - description: "`FULL` type, with `symbol`:"
                    x-description-cn: "`FULL` 类型，有 `symbol`:"
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BNBBTC
                        description: Symbol Name
                        x-description-cn: 交易对
                      priceChange:
                        type: string
                        example: "-94.99999800"
                      priceChangePercent:
                        type: string
                        example: "-95.960"
                      weightedAvgPrice:
                        type: string
                        example: "0.29628482"
                      prevClosePrice:
                        type: string
                        example: "0.10002000"
                      lastPrice:
                        type: string
                        example: "4.00000200"
                        description: Closing price of the interval
                        x-description-cn: 间隔收盘价
                      lastQty:
                        type: string
                        example: "200.00000000"
                      bidPrice:
                        type: string
                        example: "4.00000000"
                      bidQty:
                        type: string
                        example: "100.00000000"
                      askPrice:
                        type: string
                        example: "4.00000200"
                      askQty:
                        type: string
                        example: "100.00000000"
                      openPrice:
                        type: string
                        example: "99.00000000"
                        description: Opening price of the Interval
                        x-description-cn: 间隔开盘价
                      highPrice:
                        type: string
                        example: "100.00000000"
                        description: Highest price in the interval
                        x-description-cn: 间隔最高价
                      lowPrice:
                        type: string
                        example: "0.10000000"
                        description: Lowest  price in the interval
                        x-description-cn: 间隔最低价
                      volume:
                        type: string
                        example: "8913.30000000"
                        description: Total trade volume (in base asset)
                        x-description-cn: 总交易量 (base asset)
                      quoteVolume:
                        type: string
                        example: "15.30000000"
                        description: Total trade volume (in quote asset)
                        x-description-cn: 总交易量 (quote asset)
                      openTime:
                        type: integer
                        format: int64
                        example: 1499783499040
                        description: Start of the ticker interval
                        x-description-cn: ticker间隔的开始时间
                      closeTime:
                        type: integer
                        format: int64
                        example: 1499869899040
                        description: End of the ticker interval
                        x-description-cn: ticker间隔的结束时间
                      firstId:
                        type: integer
                        format: int64
                        example: 28385
                        description: First tradeId
                        x-description-cn: 首笔成交id
                      lastId:
                        type: integer
                        format: int64
                        example: 28460
                        description: Last tradeId
                        x-description-cn: 末笔成交id
                      count:
                        type: integer
                        format: int64
                        example: 76
                        description: Trade count
                        x-description-cn: 成交笔数
                  - description: "`FULL` type, with `symbols`:"
                    x-description-cn: "`FULL` 类型，有 `symbols`:"
                    type: array
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
                          example: "-94.99999800"
                        priceChangePercent:
                          type: string
                          example: "-95.960"
                        weightedAvgPrice:
                          type: string
                          example: "0.29628482"
                        prevClosePrice:
                          type: string
                          example: "0.10002000"
                        lastPrice:
                          type: string
                          example: "4.00000200"
                          description: Closing price of the interval
                          x-description-cn: 间隔收盘价
                        lastQty:
                          type: string
                          example: "200.00000000"
                        bidPrice:
                          type: string
                          example: "4.00000000"
                        bidQty:
                          type: string
                          example: "100.00000000"
                        askPrice:
                          type: string
                          example: "4.00000200"
                        askQty:
                          type: string
                          example: "100.00000000"
                        openPrice:
                          type: string
                          example: "99.00000000"
                          description: Opening price of the Interval
                          x-description-cn: 间隔开盘价
                        highPrice:
                          type: string
                          example: "100.00000000"
                          description: Highest price in the interval
                          x-description-cn: 间隔最高价
                        lowPrice:
                          type: string
                          example: "0.10000000"
                          description: Lowest  price in the interval
                          x-description-cn: 间隔最低价
                        volume:
                          type: string
                          example: "8913.30000000"
                          description: Total trade volume (in base asset)
                          x-description-cn: 总交易量 (base asset)
                        quoteVolume:
                          type: string
                          example: "15.30000000"
                          description: Total trade volume (in quote asset)
                          x-description-cn: 总交易量 (quote asset)
                        openTime:
                          type: integer
                          format: int64
                          example: 1499783499040
                          description: Start of the ticker interval
                          x-description-cn: ticker间隔的开始时间
                        closeTime:
                          type: integer
                          format: int64
                          example: 1499869899040
                          description: End of the ticker interval
                          x-description-cn: ticker间隔的结束时间
                        firstId:
                          type: integer
                          format: int64
                          example: 28385
                          description: First tradeId
                          x-description-cn: 首笔成交id
                        lastId:
                          type: integer
                          format: int64
                          example: 28460
                          description: Last tradeId
                          x-description-cn: 末笔成交id
                        count:
                          type: integer
                          format: int64
                          example: 76
                          description: Trade count
                          x-description-cn: 成交笔数
                  - description: "`MINI` type, with `symbol`:"
                    x-description-cn: "`MINI` 类型，有 `symbol`:"
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
                        example: "99.00000000"
                      highPrice:
                        type: string
                        description: Highest price in the interval
                        x-description-cn: 间隔最高价
                        example: "100.00000000"
                      lowPrice:
                        type: string
                        description: Lowest  price in the interval
                        x-description-cn: 间隔最低价
                        example: "0.10000000"
                      lastPrice:
                        type: string
                        description: Closing price of the interval
                        x-description-cn: 间隔收盘价
                        example: "4.00000200"
                      volume:
                        type: string
                        description: Total trade volume (in base asset)
                        x-description-cn: 总交易量 (base asset)
                        example: "8913.30000000"
                      quoteVolume:
                        type: string
                        description: Total trade volume (in quote asset)
                        x-description-cn: 总交易量 (quote asset)
                        example: "15.30000000"
                      openTime:
                        type: integer
                        format: int64
                        description: Start of the ticker interval
                        x-description-cn: ticker间隔的开始时间
                        example: 1499783499040
                      closeTime:
                        type: integer
                        format: int64
                        description: End of the ticker interval
                        x-description-cn: ticker间隔的结束时间
                        example: 1499869899040
                      firstId:
                        type: integer
                        format: int64
                        description: First tradeId considered
                        x-description-cn: 统计时间内的第一笔trade id
                        example: 28385
                      lastId:
                        type: integer
                        format: int64
                        description: Last tradeId considered
                        x-description-cn: 统计时间内的最后一笔trade id
                        example: 28460
                      count:
                        type: integer
                        format: int64
                        description: Total trade count
                        x-description-cn: 统计时间内交易笔数
                        example: 76
                  - description: "`MINI` type, with `symbols`:"
                    x-description-cn: "`MINI` 类型，有 `symbols`:"
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNBBTC
                        openPrice:
                          type: string
                          example: "99.00000000"
                        highPrice:
                          type: string
                          example: "100.00000000"
                        lowPrice:
                          type: string
                          example: "0.10000000"
                        lastPrice:
                          type: string
                          example: "4.00000200"
                        volume:
                          type: string
                          example: "8913.30000000"
                        quoteVolume:
                          type: string
                          example: "15.30000000"
                        openTime:
                          type: integer
                          format: int64
                          example: 1499783499040
                        closeTime:
                          type: integer
                          format: int64
                          example: 1499869899040
                        firstId:
                          type: integer
                          format: int64
                          example: 28385
                        lastId:
                          type: integer
                          format: int64
                          example: 28460
                        count:
                          type: integer
                          format: int64
                          example: 76
                    example:
                      - symbol: BNBBTC
                        openPrice: "99.00000000"
                        highPrice: "100.00000000"
                        lowPrice: "0.10000000"
                        lastPrice: "4.00000200"
                        volume: "8913.30000000"
                        quoteVolume: "15.30000000"
                        openTime: 1499783499040
                        closeTime: 1499869899040
                        firstId: 28385
                        lastId: 28460
                        count: 76
                      - symbol: LTCBTC
                        openPrice: "0.07000000"
                        highPrice: "0.07000000"
                        lowPrice: "0.07000000"
                        lastPrice: "0.07000000"
                        volume: "11.00000000"
                        quoteVolume: "0.77000000"
                        openTime: 1656908192899
                        closeTime: 1656994592899
                        firstId: 0
                        lastId: 10
                        count: 11
  /api/v3/ticker/bookTicker:
    get:
      summary: Symbol order book ticker
      x-summary-cn: 最优挂单接口
      description: Best price/qty on the order book for a symbol or symbols.
      x-description-cn: 返回当前最优的挂单(最高买单，最低卖单)
      tags:
        - market
      operationId: tickerBookTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ticker-book-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/tickerBookTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ticker_book_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ticker_book_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/TickerBookTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/TickerBookTicker/TickerBookTicker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/TickerBookTickerExample.php
      x-legacy-anchors:
        - bookTicker
      x-security-type: NONE
      x-weight: |-
        |Parameter|Symbols Provided|Weight|
        |---|---|---|
        |symbol| 1 |2|
        | |omitted| 4|
        |symbols| Any |4|
      x-weight-cn: |-
        |参数|提供Symbol数量|权重|
        |---|---|---|
        |symbol| 1 |2|
        | |不提供| 4|
        |symbols| 任意 |4|
      parameters:
        - name: symbol
          in: query
          required: false
          description: |-
            Parameter symbol and symbols cannot be used in combination.
            If neither parameter is sent, `bookTickers` for all symbols will be returned in an array.
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的bookTicker数据都会返回.
          schema:
            type: string
            example: BNBUSDT
        - name: symbols
          in: query
          required: false
          description: >-
            Parameter symbol and symbols cannot be used in combination.

            If neither parameter is sent, `bookTickers` for all symbols will be returned in an array.

            Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"] or
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的bookTicker数据都会返回.

            symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"] 或 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBUSDT
            items:
              type: string
              example: BTCUSDT
        - name: symbolStatus
          in: query
          required: false
          description: |-
            Filters for symbols that have this `tradingStatus`.
            For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
            For multiple or all symbols, non-matching ones are simply excluded from the response.
          x-description-cn: |-
            过滤具有此 `tradingStatus` 的交易对。
            对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。
            对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Symbol order book ticker
          x-description-cn: 最优挂单接口
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: LTCBTC
                      bidPrice:
                        type: string
                        example: "4.00000000"
                        x-description-cn: 最优买单价
                        description: best bid price.
                      bidQty:
                        type: string
                        example: "431.00000000"
                        x-description-cn: 挂单量
                        description: bid/ask qty.
                      askPrice:
                        type: string
                        example: "4.00000200"
                        x-description-cn: 最优卖单价
                        description: best ask price.
                      askQty:
                        type: string
                        example: "9.00000000"
                        x-description-cn: 挂单量
                        description: bid/ask qty.
                  - type: array
                    example:
                      - symbol: LTCBTC
                        bidPrice: "4.00000000"
                        bidQty: "431.00000000"
                        askPrice: "4.00000200"
                        askQty: "9.00000000"
                      - symbol: ETHBTC
                        bidPrice: "0.07946700"
                        bidQty: "9.00000000"
                        askPrice: "100000.00000000"
                        askQty: "1000.00000000"
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        bidPrice:
                          type: string
                          example: "4.00000000"
                          x-description-cn: 最优买单价
                          description: best bid price.
                        bidQty:
                          type: string
                          example: "431.00000000"
                          x-description-cn: 挂单量
                          description: bid/ask qty.
                        askPrice:
                          type: string
                          example: "4.00000200"
                          x-description-cn: 最优卖单价
                          description: best ask price.
                        askQty:
                          type: string
                          example: "9.00000000"
                          x-description-cn: 挂单量
                          description: bid/ask qty.
  /api/v3/ticker/price:
    get:
      summary: Symbol price ticker
      x-summary-cn: 最新价格接口
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回最近价格
      tags:
        - market
      operationId: tickerPrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ticker-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/tickerPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ticker_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ticker_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/TickerPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/TickerPrice/TickerPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/TickerPriceExample.php
      x-security-type: NONE
      x-weight: |-
        |Parameter|Symbols Provided|Weight|
        |---|---|---|
        |symbol| 1 |2|
        | |omitted| 4|
        |symbols| Any |4|
      x-weight-cn: |-
        |参数|提供Symbol数量|权重|
        |---|---|---|
        |symbol| 1 |2|
        | |不提供| 4|
        |symbols| 任意 |4|
      parameters:
        - name: symbol
          in: query
          required: false
          description: |-
            Parameter symbol and symbols cannot be used in combination.
            If neither parameter is sent, prices for all symbols will be returned in an array.
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的价格数据都会返回.
          schema:
            type: string
            example: BNBUSDT
        - name: symbols
          in: query
          required: false
          description: >-
            Parameter symbol and symbols cannot be used in combination.

            If neither parameter is sent, prices for all symbols will be returned in an array.

            Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"] or
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          x-description-cn: |-
            参数 `symbol` 和 `symbols` 不可以一起使用
            如果都不提供, 所有symbol的价格数据都会返回.

            symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"] 或 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBUSDT
            items:
              type: string
              example: BTCUSDT
        - name: symbolStatus
          in: query
          required: false
          description: |-
            Filters for symbols that have this `tradingStatus`.
            For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
            For multiple or all symbols, non-matching ones are simply excluded from the response.
          x-description-cn: |-
            过滤具有此 `tradingStatus` 的交易对。
            对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。
            对于多个或者全部交易对，响应中不会包括状态不匹配的交易对。
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Symbol price ticker
          x-description-cn: 最新价格接口
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: LTCBTC
                      price:
                        type: string
                        example: "4.00000200"
                  - type: array
                    example:
                      - symbol: LTCBTC
                        price: "4.00000200"
                      - symbol: ETHBTC
                        price: "0.07946600"
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        price:
                          type: string
                          example: "4.00000200"
  /api/v3/ticker/tradingDay:
    get:
      summary: Trading Day Ticker
      x-summary-cn: 交易日行情(Ticker)
      description: Price change statistics for a trading day.
      x-description-cn: 交易日价格变动统计。
      tags:
        - market
      operationId: tickerTradingDay
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ticker-trading-day
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/tickerTradingDay.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ticker_trading_day.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ticker_trading_day.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/TickerTradingDayExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/TickerTradingDay/TickerTradingDay.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/TickerTradingDayExample.php
      x-security-type: NONE
      x-weight: >-
        4 for each requested symbol. The weight for this request will cap at 200 once the number of symbols in the
        request is more than 50.
      x-weight-cn: 每个交易对占用 4 个权重。当请求中的交易对数量超过 50 时，此请求的权重上限为 200。
      parameters:
        - name: symbol
          in: query
          required: false
          description: Either `symbol` or `symbols` must be provided.
          x-description-cn: "`symbol` 或者 `symbols` 必须提供之"
          schema:
            type: string
            example: BNBUSDT
        - name: symbols
          in: query
          required: false
          description: >-
            Either `symbol` or `symbols` must be provided.

            Examples of accepted format for the `symbols` parameter: ["BTCUSDT","BNBUSDT"] or
            %5B%22BTCUSDT%22,%22BNBUSDT%22%5D.

            The maximum number of `symbols` allowed in a request is 100.
          x-description-cn: |-
            `symbol` 或者 `symbols` 必须提供之一
            `symbols` 可以接受的格式: ["BTCUSDT","BNBUSDT"] 或者 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D.
            `symbols` 最多可以发送100个.
          schema:
            type: array
            example:
              - BTCUSDT
              - BNBUSDT
            items:
              type: string
              example: BTCUSDT
        - name: timeZone
          in: query
          required: false
          description: "Default: 0 (UTC)"
          x-description-cn: 默认值： 0 (UTC)
          schema:
            type: string
            example: "0"
            default: "0"
        - name: type
          in: query
          required: false
          schema:
            type: string
            enum:
              - FULL
              - MINI
            example: FULL
            default: FULL
        - name: symbolStatus
          in: query
          required: false
          description: |-
            Filters for symbols that have this `tradingStatus`.
            For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.
            For multiple symbols, non-matching ones are simply excluded from the response.
          x-description-cn: |-
            过滤具有此 `tradingStatus` 的交易对。
            对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。
            对于多个交易对，响应中不会包括状态不匹配的交易对。
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
      x-parameters-notes: |-
        **Data Source:** Database

        **Notes:**:
          - Supported values for `timeZone`:
            - Hours and minutes (e.g. `-1:00`, `05:45`)
            - Only hours (e.g. `0`, `8`, `4`)
      x-parameters-notes-cn: |-
        **数据源:** 数据库

        **注意:**
          - `timeZone`支持的值包括：
            - 小时和分钟（例如 `-1:00`，`05:45`）
            - 仅小时（例如 `0`，`8`，`4`）
      responses:
        "200":
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
                  - description: "`FULL` type, with `symbols`:"
                    x-description-cn: "`FULL` 类型，有 `symbols`:"
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
                  - description: "`MINI` type, with `symbol`:"
                    x-description-cn: "`MINI` 类型，有 `symbol`:"
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
                  - description: "`MINI` type, with `symbols`:"
                    x-description-cn: "`MINI` 类型，有 `symbols`:"
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
  /api/v3/uiKlines:
    get:
      summary: UIKlines
      x-summary-cn: UIK线数据
      description: |-
        The request is similar to klines having the same parameters and
        response.

        `uiKlines` return modified kline data, optimized for presentation of
        candlestick charts.
      x-description-cn: |-
        请求参数与响应和k线接口相同。

        `uiKlines` 返回修改后的k线数据，针对k线图的呈现进行了优化。
      tags:
        - market
      operationId: uiKlines
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#ui-klines
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/uiKlines.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/ui_klines.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/ui_klines.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/UiKlinesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/UiKlines/UiKlines.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/UiKlinesExample.php
      x-ip-weight: 2
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: interval
          in: query
          required: true
          schema:
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
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1735693200000
        - name: timeZone
          in: query
          required: false
          description: "Default: 0 (UTC)"
          x-description-cn: 默认值： 0 (UTC)
          schema:
            type: string
            example: "0"
            default: "0"
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 500
            maximum: 1000
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
      responses:
        "200":
          description: UIKlines
          x-description-cn: UIK线数据
          content:
            application/json:
              schema:
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
  /api/v3/referencePrice:
    get:
      summary: Query Reference Price
      x-summary-cn: 查询参考价格
      description: Query the reference price for a symbol.
      x-description-cn: 查询某个交易对的参考价格。
      tags:
        - market
      operationId: referencePrice
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#reference-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/referencePrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/reference_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/reference_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/ReferencePriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/ReferencePrice/ReferencePrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/ReferencePriceExample.php
      x-ip-weight: 2
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
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
      responses:
        "200":
          description: Reference price
          x-description-cn: 参考价格
          content:
            application/json:
              schema:
                oneOf:
                  - description: "If a reference price is set:"
                    x-description-cn: 如果设置了参考价格：
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BAZUSD
                      referencePrice:
                        type: string
                        example: "10.00"
                        description: Reference price. Can be `null` if no reference price is set.
                        x-description-cn: 参考价格。如果没有设置参考价格，则为 `null`。
                      timestamp:
                        type: integer
                        format: int64
                        example: 1770736694138
                        description: Timestamp when reference price was valid.
                        x-description-cn: 参考价格有效时的时间戳。
                  - description: "If no reference price is set:"
                    x-description-cn: 如果未设置参考价格：
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BAZUSD
                      referencePrice:
                        description: Reference price. Can be `null` if no reference price is set.
                        x-description-cn: 参考价格。如果没有设置参考价格，则为 `null`。
                        example: null
                      timestamp:
                        type: integer
                        format: int64
                        description: Timestamp when reference price was valid
                        x-description-cn: 参考价格生效的时间
                        example: 1770736694138
        "400":
          description: The symbol does not have a reference price
          x-description-cn: 该交易对没有参考价格
          content:
            application/json:
              schema:
                description: "If no reference price has ever been set:"
                x-description-cn: 如果从未设置过参考价格：
                type: object
                properties:
                  code:
                    type: integer
                    format: int64
                    example: -2043
                  msg:
                    type: string
                    example: This symbol doesn't have a reference price.
  /api/v3/referencePrice/calculation:
    get:
      summary: Query Reference Price Calculation
      x-summary-cn: 查询参考价格计算方式
      description: Describes how reference price is calculated for a given symbol.
      x-description-cn: 描述某个交易对的参考价格是如何计算的。
      tags:
        - market
      operationId: referencePriceCalculation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market#reference-price-calculation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/MarketApi/referencePriceCalculation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/market_api/reference_price_calculation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Market/reference_price_calculation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/market/ReferencePriceCalculationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/MarketAPI/ReferencePriceCalculation/ReferencePriceCalculation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/market/ReferencePriceCalculationExample.php
      x-ip-weight: 2
      x-security-type: NONE
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: symbolStatus
          in: query
          required: false
          description: "Supported values: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`"
          x-description-cn: "支持的值: `TRADING`, `HALT`, `BREAK`, `CANCEL_ONLY`"
          schema:
            type: string
            enum:
              - TRADING
              - HALT
              - BREAK
              - CANCEL_ONLY
            example: TRADING
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      responses:
        "200":
          description: Reference price calculation
          x-description-cn: 参考价格计算方式
          content:
            application/json:
              schema:
                oneOf:
                  - description: "If the reference price is being calculated by the matching engine as an arithmetic mean:"
                    x-description-cn: 如果参考价格由撮合引擎以算术平均数计算：
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BAZUSD
                      calculationType:
                        type: string
                        description: Either `ARITHMETIC_MEAN` or `EXTERNAL`.
                        x-description-cn: "`ARITHMETIC_MEAN` 或 `EXTERNAL`。"
                        example: ARITHMETIC_MEAN
                      bucketCount:
                        type: integer
                        format: int64
                        description: Present when calculationType is ARITHMETIC_MEAN.
                        x-description-cn: 当 calculationType 为 ARITHMETIC_MEAN 时存在。
                        example: 10
                      bucketWidthMs:
                        type: integer
                        format: int64
                        description: Present when calculationType is ARITHMETIC_MEAN.
                        x-description-cn: 当 calculationType 为 ARITHMETIC_MEAN 时存在。
                        example: 1000
                  - description: "If the reference price is being calculated outside the matching engine:"
                    x-description-cn: 如果参考价格由撮合引擎外部计算：
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BAZUSD
                      calculationType:
                        type: string
                        description: Either `ARITHMETIC_MEAN` or `EXTERNAL`.
                        x-description-cn: "`ARITHMETIC_MEAN` 或 `EXTERNAL`。"
                        example: EXTERNAL
                      externalCalculationId:
                        type: integer
                        format: int64
                        description: Present when calculationType is EXTERNAL.
                        x-description-cn: 当 calculationType 为 EXTERNAL 时存在。
                        example: 42
        "400":
          description: The symbol does not have a reference price
          x-description-cn: 该交易对没有参考价格
          content:
            application/json:
              schema:
                description: "If reference price is not being calculated:"
                x-description-cn: 如果参考价格未被计算：
                type: object
                properties:
                  code:
                    type: integer
                    format: int64
                    example: -2043
                  msg:
                    type: string
                    example: This symbol doesn't have a reference price.
  /api/v3/order/amend/keepPriority:
    put:
      summary: Order Amend Keep Priority (TRADE)
      x-summary-cn: 修改订单并保留优先级 (TRADE)
      description: |-
        Reduce the quantity of an existing open order.

        This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

        Read [Order Amend Keep Priority FAQ](/products/spot/faqs/order_amend_keep_priority) to learn more.
      x-description-cn: |-
        由客户发送以减少其现有当前订单的原始数量。

        这个请求将添加0个订单到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

        请阅读 [保留优先权的修改订单常见问题](/products/spot/faqs/order_amend_keep_priority) 了解更多信息。
      tags:
        - trade
      operationId: orderAmendKeepPriority
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-amend-keep-priority
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderAmendKeepPriority.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_amend_keep_priority.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_amend_keep_priority.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderAmendKeepPriorityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderAmendKeepPriority/OrderAmendKeepPriority.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderAmendKeepPriorityExample.php
      x-ip-weight: 4
      x-order-weight: 0
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
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - newQty
                - timestamp
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
                    The new client order ID for the order after being amended. <br> If not sent, one will be randomly
                    generated. <br> It is possible to reuse the current clientOrderId by sending it as the
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
                  description: >-
                    The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision
                    (e.g., 6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
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
                      transactTime:
                        type: integer
                        format: int64
                        example: 1741926410255
                      executionId:
                        type: integer
                        format: int64
                        example: 75
                      amendedOrder:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 33
                          orderListId:
                            type: integer
                            format: int64
                            example: -1
                          origClientOrderId:
                            type: string
                            example: 5xrgbMyg6z36NzBn2pbT8H
                          clientOrderId:
                            type: string
                            example: PFaq6hIHxqFENGfdtn4J6Q
                          price:
                            type: string
                            example: "6.00000000"
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
                            example: SELL
                          workingTime:
                            type: integer
                            format: int64
                            example: 1741926410242
                          selfTradePreventionMode:
                            type: string
                            example: NONE
                  - description: "Response for an order that is part of an Order list:"
                    x-description-cn: 来自订单列表中单个订单的响应：
                    type: object
                    properties:
                      transactTime:
                        type: integer
                        format: int64
                        example: 1741926410255
                      executionId:
                        type: integer
                        format: int64
                        example: 75
                      amendedOrder:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          orderId:
                            type: integer
                            format: int64
                            example: 33
                          orderListId:
                            type: integer
                            format: int64
                            example: -1
                          origClientOrderId:
                            type: string
                            example: 5xrgbMyg6z36NzBn2pbT8H
                          clientOrderId:
                            type: string
                            example: PFaq6hIHxqFENGfdtn4J6Q
                          price:
                            type: string
                            example: "6.00000000"
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
                            example: SELL
                          workingTime:
                            type: integer
                            format: int64
                            example: 1741926410242
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
                            example: 1
                          contingencyType:
                            type: string
                            example: OTO
                          listOrderStatus:
                            type: string
                            example: EXECUTING
                          listClientOrderId:
                            type: string
                            example: AT7FTxZXylVSwRoZs52mt3
                          symbol:
                            type: string
                            example: BTCUSDT
                          orders:
                            type: array
                            example:
                              - symbol: BTCUSDT
                                orderId: 8
                                clientOrderId: GkwwHZUUbFtZOoH1YsZk9Q
                              - symbol: BTCUSDT
                                orderId: 9
                                clientOrderId: UQ1Np3bmQ71jJzsSDW9Vpi
                            items:
                              type: object
                              properties:
                                symbol:
                                  type: string
                                  example: BTCUSDT
                                orderId:
                                  type: integer
                                  format: int64
                                  example: 8
                                clientOrderId:
                                  type: string
                                  example: GkwwHZUUbFtZOoH1YsZk9Q
  /api/v3/order/cancelReplace:
    post:
      summary: Cancel an Existing Order and Send a New Order (TRADE)
      x-summary-cn: 撤消挂单再下单 (TRADE)
      description: >-
        - Cancels an existing order and places a new order on the same symbol.

        - Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

        - A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the
        unfilled order count by 1.

        - You can only cancel an individual order from an orderList using this endpoint, but the result is the same as
        canceling the entire orderList.
      x-description-cn: |-
        - 撤消挂单并在同个交易对上重新下单。
        - 在撤消订单和下单前会判断: 1) 过滤器参数, 以及 2) 目前下单数量。
        - 即使请求中没有尝试发送新订单，比如(`newOrderResult: NOT_ATTEMPTED`)，未成交订单的数量仍然会加1。
        - 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。
      tags:
        - trade
      operationId: orderCancelReplace
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-cancel-replace
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderCancelReplace.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_cancel_replace.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_cancel_replace.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderCancelReplaceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderCancelReplace/OrderCancelReplace.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderCancelReplaceExample.php
      x-ip-weight: 1
      x-order-weight: 1
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
      x-parameters-notes: >-
        **Data Source:** Matching Engine


        Similar to `POST /api/v3/order`, additional mandatory parameters are determined by `type`.

        Response format varies depending on whether the processing of the message succeeded, partially succeeded, or
        failed.


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
                  <td align=right><code>N/A</code></td>
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
      x-parameters-notes-cn: |-
        **数据源:** 撮合引擎

        如同 `POST /api/v3/order`，额外的强制参数取决于 `type` 。
        响应格式根据消息的处理是成功、部分成功还是失败而有所不同。

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
                  <td align=right><code>N/A</code></td>
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - type
                - cancelReplaceMode
                - timestamp
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
                cancelReplaceMode:
                  type: string
                  enum:
                    - STOP_ON_FAILURE
                    - ALLOW_FAILURE
                  example: STOP_ON_FAILURE
                  description: >-
                    The allowed values are: <br/> `STOP_ON_FAILURE` - If the cancel request fails, the new order
                    placement will not be attempted. <br/> `ALLOW_FAILURE` - new order placement will be attempted even
                    if cancel request fails.
                  x-description-cn: 指定类型：`STOP_ON_FAILURE` - 如果撤消订单失败将不会继续重新下单。<br/> `ALLOW_FAILURE` - 不管撤消订单是否成功都会继续重新下单。
                timeInForce:
                  type: string
                  enum:
                    - GTC
                    - IOC
                    - FOK
                  example: GTC
                quantity:
                  type: number
                  format: float
                  example: 1
                quoteOrderQty:
                  type: number
                  format: float
                  example: 1
                price:
                  type: number
                  format: float
                  example: 400
                cancelNewClientOrderId:
                  type: string
                  example: cancelMyOrder1
                  description: Used to uniquely identify this cancel. Automatically generated by default.
                  x-description-cn: 用户自定义的id，如空缺系统会自动赋值
                cancelOrigClientOrderId:
                  type: string
                  example: myOrder1
                  description: >-
                    Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br> If both `cancelOrderId`
                    and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then
                    the `cancelOrigClientOrderId` from that result is checked against that order. <br></br> If both
                    conditions are not met the request will be rejected.
                  x-description-cn: >-
                    必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和
                    `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的
                    `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。
                cancelOrderId:
                  type: integer
                  format: int64
                  example: 1
                  description: >-
                    Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br>If both `cancelOrderId`
                    and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then
                    the `cancelOrigClientOrderId` from that result is checked against that order. <br></br>If both
                    conditions are not met the request will be rejected.
                  x-description-cn: >-
                    必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。 <br></br> 当同时提供 `cancelOrderId` 和
                    `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。<br></br> 然后， 查找结果中的
                    `cancelOrigClientOrderId` 的值将会被用来验证订单。<br></br> 如果两个条件都不满足，则请求将被拒绝。
                newClientOrderId:
                  type: string
                  example: myOrder2
                  description: Used to identify the new order.
                  x-description-cn: 用于辨识新订单。
                strategyId:
                  type: integer
                  format: int64
                  example: 1
                strategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 不能低于 `1000000`。
                stopPrice:
                  type: number
                  format: float
                  example: 1
                trailingDelta:
                  type: integer
                  format: int64
                  example: 1
                  description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                  x-description-cn: 参考 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                icebergQty:
                  type: number
                  format: float
                  example: 1
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
                    The allowed enums is dependent on what is configured on the symbol. The possible supported values
                    are: [STP Modes](/products/spot/enums#stpmodes).
                  x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                cancelRestrictions:
                  type: string
                  enum:
                    - ONLY_NEW
                    - ONLY_PARTIALLY_FILLED
                  example: ONLY_NEW
                  description: >-
                    Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br>
                    `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more
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
                    Supported values: <br> `DO_NOTHING` (default)- will only attempt to cancel the order if account has
                    not exceeded the unfilled order rate limit<br> `CANCEL_ONLY` - will always cancel the order
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
                  description: "Price level to peg the price to (max: 100) <br> See Pegged Orders"
                  x-description-cn: 用于挂钩的价格水平（最大值：100）。 <br> 参阅 关于挂钩订单参数的注意事项
                pegOffsetType:
                  type: string
                  enum:
                    - PRICE_LEVEL
                  example: PRICE_LEVEL
                  description: Only `PRICE_LEVEL` is supported <br> See Pegged Orders.
                  x-description-cn: 仅支持 `PRICE_LEVEL`。 <br> 参阅 关于挂钩订单参数的注意事项
                quoteNotionalLimit:
                  type: number
                  format: float
                  example: 100
                  description: >-
                    For replacement orders on the BUY side only. Maximum quote-asset notional the replacement order may
                    consume. See [Quote Notional Limit](/products/spot/faqs/quoteNotionalLimit).
                  x-description-cn: 仅适用于买单方向的新订单。新订单可消耗的报价资产名义价值上限。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                recvWindow:
                  type: number
                  format: float
                  example: 5000
                  maximum: 60000
                  description: >-
                    Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be
                    specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Notes:**

        - The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order
        Responses](/products/spot/rest-api#conditional-fields-in-order-responses).

        - The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when
        only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.
      x-response-notes-cn: >-
        **注意:**

        - 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。

        - 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` +
        `origClientOrderId` 会稍慢。
      responses:
        "200":
          description: Cancel an existing order and send a new order
          x-description-cn: 撤消挂单再下单
          content:
            application/json:
              schema:
                description: >-
                  Both the cancel and the new order placement succeeded, and the account has not exceeded its unfilled
                  order count:
                x-description-cn: 撤单和下单都成功，而且账户没有超出未成交订单计数时：
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
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      origClientOrderId:
                        type: string
                        example: DnLo3vTAQcjha43lAZhZ0y
                        description: cancelOrigClientOrderId from request
                        x-description-cn: 请求的 cancelOrigClientOrderId
                      orderId:
                        type: integer
                        format: int64
                        example: 9
                      orderListId:
                        type: integer
                        format: int64
                        example: -1
                        description: Unless it's part of an order list, value will be -1
                        x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                      clientOrderId:
                        type: string
                        example: osxN3JXAtJvKvCqGeMWMVR
                        description: cancelNewClientOrderId from request
                        x-description-cn: 请求的 cancelNewClientOrderId
                      transactTime:
                        type: integer
                        format: int64
                        example: 1684804350068
                      price:
                        type: string
                        example: "0.01000000"
                      origQty:
                        type: string
                        example: "0.000100"
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
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      orderId:
                        type: integer
                        format: int64
                        example: 10
                      orderListId:
                        type: integer
                        format: int64
                        example: -1
                        description: Unless it's part of an order list, value will be -1
                        x-description-cn: 除非此单是订单列表的一部分, 否则此值为 -1
                      clientOrderId:
                        type: string
                        example: wOceeeOzNORyLiQfw7jd8S
                      transactTime:
                        type: integer
                        format: int64
                        example: 1652928801803
                      price:
                        type: string
                        example: "0.02000000"
                      origQty:
                        type: string
                        example: "0.040000"
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
                        example: 1669277163808
                      fills:
                        type: array
                        example: []
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              example: "4000.00000000"
                            qty:
                              type: string
                              example: "1.00000000"
                            commission:
                              type: string
                              example: "4.00000000"
                            commissionAsset:
                              type: string
                              example: USDT
                            tradeId:
                              type: integer
                              example: 12345
                              format: int64
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
        "400":
          description: Order cancel-replace failed
          x-description-cn: 撤消挂单再下单失败
          content:
            application/json:
              schema:
                oneOf:
                  - description: >-
                      Cancel order fails with `STOP_ON_FAILURE`, and the account has not exceeded its unfilled order
                      count:
                    x-description-cn: 选择了 `STOP_ON_FAILURE` 而且账户没有超出未成交订单计数时, 撤单出现错误：
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
                  - description: >-
                      Both the cancel and the new order placement fail with `cancelReplaceMode=ALLOW_FAILURE`, and the
                      account has not exceeded its unfilled order count:
                    x-description-cn: 选择 `cancelReplaceMode=ALLOW_FAILURE` 而且账户没有超出未成交订单计数时, 撤单和下单失败：
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
        "409":
          description: Order cancel-replace partially failed
          x-description-cn: 撤消挂单再下单部分失败
          content:
            application/json:
              schema:
                oneOf:
                  - description: >-
                      Cancel order succeeds but the new order placement fails, and the account has not exceeded its
                      unfilled order count:
                    x-description-cn: 撤单成功而且账户没有超出未成交订单计数时，下单失败：
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
                                example: 86M8erehfExV8z2RC8Zo8k
                                description: cancelOrigClientOrderId from request
                                x-description-cn: 请求的 cancelOrigClientOrderId
                              orderId:
                                type: integer
                                format: int64
                                example: 3
                              orderListId:
                                type: integer
                                format: int64
                                example: -1
                              clientOrderId:
                                type: string
                                example: G1kLo6aDv2KGNTFcjfTSFq
                                description: cancelNewClientOrderId from request
                                x-description-cn: 请求的 cancelNewClientOrderId
                              transactTime:
                                type: integer
                                format: int64
                                example: 1684804350068
                              price:
                                type: string
                                example: "0.006123"
                              origQty:
                                type: string
                                example: "10000.000000"
                              executedQty:
                                type: string
                                example: "0.000000"
                              origQuoteOrderQty:
                                type: string
                                example: "0.000000"
                              cummulativeQuoteQty:
                                type: string
                                example: "0.000000"
                              status:
                                type: string
                                example: CANCELED
                              timeInForce:
                                type: string
                                example: GTC
                              type:
                                type: string
                                example: LIMIT_MAKER
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
                  - description: >-
                      Cancel order fails with `ALLOW_FAILURE`, and the account has not exceeded its unfilled order
                      count:
                    x-description-cn: 选择 `ALLOW_FAILURE` 而且账户没有超出未成交订单计数时, 撤单出现错误：
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
                                example: 11
                              orderListId:
                                type: integer
                                format: int64
                                example: -1
                              clientOrderId:
                                type: string
                                example: pfojJMg6IMNDKuJqDxvoxN
                              transactTime:
                                type: integer
                                format: int64
                                example: 1648540168818
                  - description: >-
                      Using `orderRateLimitExceededMode=CANCEL_ONLY`, and the account has exceeded its unfilled order
                      count:
                    x-description-cn: 选择 `orderRateLimitExceededMode=CANCEL_ONLY` 而且账户超出未成交订单计数时：
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
                                  Too many orders placed without trading; current limit is 1 non-trading orders per 10
                                  SECOND. Unable to place new orders until trades occur or window resets.
        "429":
          description: Too many new orders
          x-description-cn: 新订单过多
          content:
            application/json:
              schema:
                description: "Using `orderRateLimitExceededMode=DO_NOTHING`, and the account has exceeded its unfilled order count:"
                x-description-cn: 选择 `orderRateLimitExceededMode=DO_NOTHING` 而且账户超出未成交订单计数时：
                type: object
                properties:
                  code:
                    type: integer
                    format: int64
                    example: -1015
                  msg:
                    type: string
                    example: >-
                      Too many orders placed without trading; current limit is 1 non-trading orders per 10 SECOND.
                      Unable to place new orders until trades occur or window resets.
  /api/v3/orderList/oco:
    post:
      summary: New Order list - OCO (TRADE)
      x-summary-cn: 新订单列表 - OCO (TRADE)
      description: >-
        Send in an one-cancels-the-other (OCO) pair, where activation of one

        order immediately cancels the other.


        - An OCO has 2 orders called the **above order** and **below order**.

        - One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be
        `STOP_LOSS` or `STOP_LOSS_LIMIT` order.

        - Price restrictions
          - If the OCO is on the `SELL` side:
            - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price >  `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
            - `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
          - If the OCO is on the `BUY` side:
            - `LIMIT_MAKER/TAKE_PROFIT_LIMIT price` < Last Traded Price < `stopPrice`
            - `TAKE_PROFIT stopPrice` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT stopPrice` * OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
        - OCOs add 2 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

        - OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单**。
        - 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
        - 针对价格限制：
          - 如果 OCO 订单方向是 `SELL`：
            - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 >  `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
            - `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
          - 如果 OCO 订单方向是 `BUY`：
            - `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` < 最后交易价格 < `stopPrice`
            - `TAKE_PROFIT` `stopPrice` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
        - OCO 会添加 **2个订单** 到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: orderListOco
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-list-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderListOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_list_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_list_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderListOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderListOco/OrderListOco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderListOcoExample.php
      x-ip-weight: 1
      x-order-weight: 2
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
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
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
                - aboveType
                - belowType
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: lH1YDkuQKWiXVXHPSKYEIp
                  description: >-
                    Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list
                    with the same `listClientOrderId` is accepted only when the previous one is filled or completely
                    expired. `listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowClientOrderId`.
                  x-description-cn: >-
                    整个 OCO order list 的唯一ID。 如果未发送则自动生成。 仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。
                    `listClientOrderId` 与 `aboveClientOrderId` 和 `belowClientOrderId` 不同。
                side:
                  type: string
                  enum:
                    - BUY
                    - SELL
                  example: BUY
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
                    Can be used if `aboveType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify
                    the limit price.
                  x-description-cn: 当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                aboveStopPrice:
                  type: number
                  format: float
                  example: 1.50000001
                  description: >-
                    Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
                    Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.
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
                    Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify
                    the limit price.
                  x-description-cn: 当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                belowStopPrice:
                  type: number
                  format: float
                  example: 1.50000001
                  description: >-
                    Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
                    Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.
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
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: New Order list - OCO
          x-description-cn: New 订单 列表 - OCO
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    format: int64
                    example: 1
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
                    example: lH1YDkuQKWiXVXHPSKYEIp
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1710485608839
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 10
                        clientOrderId: 44nZvqpemY7sVYgPYbvPih
                      - symbol: LTCBTC
                        orderId: 11
                        clientOrderId: NuMp0nVYnciDiFmVqfpBqK
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 10
                        clientOrderId:
                          type: string
                          example: 44nZvqpemY7sVYgPYbvPih
                  orderReports:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 10
                        orderListId: 1
                        clientOrderId: 44nZvqpemY7sVYgPYbvPih
                        transactTime: 1710485608839
                        price: "1.00000000"
                        origQty: "5.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: STOP_LOSS_LIMIT
                        side: SELL
                        stopPrice: "1.00000000"
                        workingTime: -1
                        icebergQty: "1.00000000"
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        orderId: 11
                        orderListId: 1
                        clientOrderId: NuMp0nVYnciDiFmVqfpBqK
                        transactTime: 1710485608839
                        price: "3.00000000"
                        origQty: "5.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT_MAKER
                        side: SELL
                        workingTime: 1710485608839
                        selfTradePreventionMode: NONE
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 10
                        orderListId:
                          type: integer
                          format: int64
                          example: 1
                        clientOrderId:
                          type: string
                          example: 44nZvqpemY7sVYgPYbvPih
                        transactTime:
                          type: integer
                          format: int64
                          example: 1710485608839
                        price:
                          type: string
                          example: "1.00000000"
                        origQty:
                          type: string
                          example: "5.00000000"
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
                        stopPrice:
                          type: string
                          example: "1.00000000"
                        icebergQty:
                          type: string
                          example: "1.00000000"
  /api/v3/orderList/opo:
    post:
      summary: New Order List - OPO (TRADE)
      x-summary-cn: 新订单列表 - OPO (TRADE)
      description: |-
        Place an [OPO](/products/spot/faqs/opo).

        - The working order must be `LIMIT` or `LIMIT_MAKER`.
        - OPOs add 2 orders to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送一个新的 [OPO](/products/spot/faqs/opo) 订单。

        - 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
        - OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。
      tags:
        - trade
      operationId: orderListOpo
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-list-opo
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderListOpo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_list_opo.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_list_opo.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderListOpoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderListOpo/OrderListOpo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderListOpoExample.php
      x-ip-weight: 1
      x-order-weight: 2
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
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - workingType
                - workingSide
                - workingPrice
                - workingQuantity
                - pendingType
                - pendingSide
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: H94qCqO27P74OEiO4X8HOG
                  description: >-
                    Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list
                    with the same `listClientOrderId` is accepted only when the previous one is filled or completely
                    expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the
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
                  description: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
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
                    Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using
                    `quoteOrderQty` are not supported.
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
                  description: Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
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
                  x-description-cn: 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: New Order List - OPO
          x-description-cn: New 订单 列表- OPO
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    format: int64
                    example: 0
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
                    example: H94qCqO27P74OEiO4X8HOG
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1762998011671
                  symbol:
                    type: string
                    example: BTCUSDT
                  orders:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        orderId: 2
                        clientOrderId: JX6xfdjo0wysiGumfHNmPu
                      - symbol: BTCUSDT
                        orderId: 3
                        clientOrderId: 2ZJCY0IjOhuYIMLGN8kU8S
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
                          example: JX6xfdjo0wysiGumfHNmPu
                  orderReports:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        orderId: 2
                        orderListId: 0
                        clientOrderId: JX6xfdjo0wysiGumfHNmPu
                        transactTime: 1762998011671
                        price: "102264.00000000"
                        origQty: "0.00060000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.00000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT
                        side: BUY
                        workingTime: 1762998011671
                        selfTradePreventionMode: NONE
                      - symbol: BTCUSDT
                        orderId: 3
                        orderListId: 0
                        clientOrderId: 2ZJCY0IjOhuYIMLGN8kU8S
                        transactTime: 1762998011671
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
                          example: 0
                        clientOrderId:
                          type: string
                          example: JX6xfdjo0wysiGumfHNmPu
                        transactTime:
                          type: integer
                          format: int64
                          example: 1762998011671
                        price:
                          type: string
                          example: "102264.00000000"
                        executedQty:
                          type: string
                          example: "0.00000000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.00000000"
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
                          example: 1762998011671
                        selfTradePreventionMode:
                          type: string
                          example: NONE
                        origQty:
                          type: string
                          example: "0.00060000"
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
  /api/v3/orderList/opoco:
    post:
      summary: New Order List - OPOCO (TRADE)
      x-summary-cn: 新订单列表 - OPOCO (TRADE)
      description: |-
        Place an [OPOCO](/products/spot/faqs/opo).

        - The working order must be `LIMIT` or `LIMIT_MAKER`.
      x-description-cn: |-
        发送一个 [OPOCO](/products/spot/faqs/opo) 订单。

        - 生效订单必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。
      tags:
        - trade
      operationId: orderListOpoco
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-list-opoco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderListOpoco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_list_opoco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_list_opoco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderListOpocoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderListOpoco/OrderListOpoco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderListOpocoExample.php
      x-ip-weight: 1
      x-order-weight: 3
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
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - workingType
                - workingSide
                - workingPrice
                - workingQuantity
                - pendingSide
                - pendingAboveType
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: bcedxMpQG6nFrZUPQyshoL
                  description: >-
                    Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list
                    with the same `listClientOrderId` is accepted only when the previous one is filled or completely
                    expired. `listClientOrderId` is distinct from the `workingClientOrderId`,
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
                  description: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
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
                  description: "Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`"
                  x-description-cn: 支持的数值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`
                pendingAboveClientOrderId:
                  type: string
                  example: pendingAboveOrder1
                  description: >-
                    Arbitrary unique ID among open orders for the pending above order. Automatically generated if not
                    sent.
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
                  description: This can only be used if `pendingAboveTimeInForce` is `GTC` or `pendingAboveType` is `LIMIT_MAKER`.
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
                    Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000`
                    are reserved and cannot be used.
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
                    Arbitrary unique ID among open orders for the pending below order. Automatically generated if not
                    sent.
                  x-description-cn: 待处理"下方"订单中开放订单的任意唯一 ID。如果未发送，则自动生成。
                pendingBelowPrice:
                  type: number
                  format: float
                  example: 1
                  description: >-
                    Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit
                    price.
                  x-description-cn: 当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。
                pendingBelowStopPrice:
                  type: number
                  format: float
                  example: 1
                  description: >-
                    Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                    `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be
                    specified.
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
                  description: This can only be used if `pendingBelowTimeInForce` is `GTC` or `pendingBelowType` is `LIMIT_MAKER`.
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
                    Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000`
                    are reserved and cannot be used.
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
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: New Order List - OPOCO
          x-description-cn: New 订单 列表- OPOCO
          content:
            application/json:
              schema:
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
                    example: bcedxMpQG6nFrZUPQyshoL
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1763000506354
                  symbol:
                    type: string
                    example: BTCUSDT
                  orders:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        orderId: 9
                        clientOrderId: OLSBhMWaIlLSzZ9Zm7fnKB
                      - symbol: BTCUSDT
                        orderId: 10
                        clientOrderId: mfif39yPTHsB3C0FIXznR2
                      - symbol: BTCUSDT
                        orderId: 11
                        clientOrderId: yINkaXSJeoi3bU5vWMY8Z8
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        orderId:
                          type: integer
                          format: int64
                          example: 9
                        clientOrderId:
                          type: string
                          example: OLSBhMWaIlLSzZ9Zm7fnKB
                  orderReports:
                    type: array
                    example:
                      - symbol: BTCUSDT
                        orderId: 9
                        orderListId: 2
                        clientOrderId: OLSBhMWaIlLSzZ9Zm7fnKB
                        transactTime: 1763000506354
                        price: "102496.00000000"
                        origQty: "0.00170000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.00000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT
                        side: BUY
                        workingTime: 1763000506354
                        selfTradePreventionMode: NONE
                      - symbol: BTCUSDT
                        orderId: 10
                        orderListId: 2
                        clientOrderId: mfif39yPTHsB3C0FIXznR2
                        transactTime: 1763000506354
                        price: "101613.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.00000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: PENDING_NEW
                        timeInForce: GTC
                        type: STOP_LOSS_LIMIT
                        side: SELL
                        stopPrice: "10100.00000000"
                        workingTime: -1
                        selfTradePreventionMode: NONE
                      - symbol: BTCUSDT
                        orderId: 11
                        orderListId: 2
                        clientOrderId: yINkaXSJeoi3bU5vWMY8Z8
                        transactTime: 1763000506354
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
                          example: 9
                        orderListId:
                          type: integer
                          format: int64
                          example: 2
                        clientOrderId:
                          type: string
                          example: OLSBhMWaIlLSzZ9Zm7fnKB
                        transactTime:
                          type: integer
                          format: int64
                          example: 1763000506354
                        price:
                          type: string
                          example: "102496.00000000"
                        executedQty:
                          type: string
                          example: "0.00000000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.00000000"
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
                          example: 1763000506354
                        selfTradePreventionMode:
                          type: string
                          example: NONE
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
  /api/v3/orderList/oto:
    post:
      summary: New Order list - OTO (TRADE)
      x-summary-cn: 新订单列表 - OTO (TRADE)
      description: >-
        Place an OTO.


        - An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.

        - The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the
        working order goes on the order book.

        - The second order is called the **pending order**. It can be any order type except for `MARKET` orders using
        parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets
        **fully filled**.

        - If either the working order or the pending order is cancelled individually, the other order in the order list
        will also be canceled or expired.

        - When the order list is placed, if the working order gets **immediately fully filled**, the placement response
        will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to
        query the status of the pending order again to see its updated status.

        - OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: >-
        发送一个新的 OTO 订单。


        - 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.

        - 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。

        - 第二个订单被称为**待处理订单**。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET` 订单。只有当生效订单**完全成交**时，待处理订单才会被自动下单。

        - 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。

        - 如果生效订单在下订单列表后**立即完全成交**，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为
        `PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。

        - `OTO` 订单将**2 个订单**添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      tags:
        - trade
      operationId: orderListOto
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-list-oto
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderListOto.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_list_oto.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_list_oto.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderListOtoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderListOto/OrderListOto.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderListOtoExample.php
      x-ip-weight: 1
      x-order-weight: 2
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

        |`pendingType` = `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`|`pendingPrice`, `pendingStopPrice` and/or
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
          application/x-www-form-urlencoded:
            schema:
              type: object
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
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: yl2ERtcar1o25zcWtqVBTC
                  description: >-
                    Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list
                    with the same `listClientOrderId` is accepted only when the previous one is filled or completely
                    expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the
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
                  description: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
                  x-description-cn: 用于标识生效订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
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
                    Supported values: [Order Types](/products/spot/enums#ordertypes). Note that `MARKET` orders using
                    `quoteOrderQty` are not supported.
                  x-description-cn: 支持的数值： [订单类型](/products/spot/enums#ordertypes) 请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。
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
                  description: Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the pending order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
                  x-description-cn: 用于标识待处理订单策略的任意数值。 小于 `1000000` 的值被保留，无法使用。
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
                workingQuoteNotionalLimit:
                  type: number
                  format: float
                  example: 100
                  description: >-
                    Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional
                    Limit](/products/spot/faqs/quoteNotionalLimit).
                  x-description-cn: 生效订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                pendingQuoteNotionalLimit:
                  type: number
                  format: float
                  example: 100
                  description: >-
                    Quote notional limit for the pending order (only for orders on the BUY side). See [Quote Notional
                    Limit](/products/spot/faqs/quoteNotionalLimit).
                  x-description-cn: 待处理订单的报价资产名义价值上限（仅适用于买单）。参见 [报价资产名义价值上限](/products/spot/faqs/quoteNotionalLimit)。
                recvWindow:
                  type: number
                  format: float
                  example: 5000
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: New Order list - OTO
          x-description-cn: New 订单 列表- OTO
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    format: int64
                    example: 0
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
                    example: yl2ERtcar1o25zcWtqVBTC
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1712289389158
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 4
                        clientOrderId: Bq17mn9fP6vyCn75Jw1xya
                      - symbol: LTCBTC
                        orderId: 5
                        clientOrderId: arLFo0zGJVDE69cvGBaU0d
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 4
                        clientOrderId:
                          type: string
                          example: Bq17mn9fP6vyCn75Jw1xya
                  orderReports:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 4
                        orderListId: 0
                        clientOrderId: Bq17mn9fP6vyCn75Jw1xya
                        transactTime: 1712289389158
                        price: "1.00000000"
                        origQty: "1.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT
                        side: SELL
                        workingTime: 1712289389158
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        orderId: 5
                        orderListId: 0
                        clientOrderId: arLFo0zGJVDE69cvGBaU0d
                        transactTime: 1712289389158
                        price: "0.00000000"
                        origQty: "5.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
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
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 4
                        orderListId:
                          type: integer
                          format: int64
                          example: 0
                        clientOrderId:
                          type: string
                          example: Bq17mn9fP6vyCn75Jw1xya
                        transactTime:
                          type: integer
                          format: int64
                          example: 1712289389158
                        price:
                          type: string
                          example: "1.00000000"
                        origQty:
                          type: string
                          example: "1.00000000"
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
                          example: 1712289389158
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
  /api/v3/orderList/otoco:
    post:
      summary: New Order list - OTOCO (TRADE)
      x-summary-cn: 新订单列表 - OTOCO (TRADE)
      description: >-
        Place an OTOCO.


        - An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.

        - The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the
        working order goes on the order book.
          - The behavior of the working order is the same as the [OTO](#order-list-oto).
        - OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only
        placed on the order book when the working order gets **fully filled**.
          - The rules of the pending above and pending below follow the same rules as the [Order list OCO](#order-list-oco).
        - OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送一个新的 OTOCO 订单。

        - 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
        - 第一个订单被称为**生效订单**，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
          - 生效订单的行为与此一致 [OTO](#order-list-oto)
        - 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交**时，待处理订单们才会被自动下单。
          - 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [OrderList OCO](#order-list-oco)。
        - `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单**。
      tags:
        - trade
      operationId: orderListOtoco
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-list-otoco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderListOtoco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_list_otoco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_list_otoco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderListOtocoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderListOtoco/OrderListOtoco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderListOtocoExample.php
      x-ip-weight: 1
      x-order-weight: 3
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

        |`pendingAboveType`= `LIMIT_MAKER`                                |`pendingAbovePrice`     |

        |`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`        |`pendingAboveStopPrice` and/or
        `pendingAboveTrailingDelta`|

        |`pendingAboveType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` |`pendingAbovePrice`, `pendingAboveStopPrice` and/or
        `pendingAboveTrailingDelta`, `pendingAboveTimeInForce`|

        |`pendingBelowType`= `LIMIT_MAKER`                                |`pendingBelowPrice`          |

        |`pendingBelowType= STOP_LOSS/TAKE_PROFIT`         |`pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`|

        |`pendingBelowType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` |`pendingBelowPrice`, `pendingBelowStopPrice` and/or
        `pendingBelowTrailingDelta`, `pendingBelowTimeInForce`|
      x-parameters-notes-cn: >-
        **数据源:** 撮合引擎


        ::span{#mandatory-parameters-based-on-pendingabovetype-pendingbelowtype-or-workingtype}


        **根据 `pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些参数的强制要求**


        根据 `pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：


        |类型                                                        | 强制要求的参数                  | 其他信息|

        |----                                                       |----                           |------

        |`workingType` = `LIMIT`                                    |`workingTimeInForce`           |

        |`pendingAboveType` = `LIMIT_MAKER`                                |`pendingAbovePrice`     |

        |`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT` | `pendingAboveStopPrice` 与/或  `pendingAboveTrailingDelta` |

        |`pendingAboveType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` | `pendingAbovePrice`， `pendingAboveStopPrice` 与/或
        `pendingAboveTrailingDelta`， `pendingAboveTimeInForce` |

        |`pendingBelowType` = `LIMIT_MAKER`                                |`pendingBelowPrice`          |

        |`pendingBelowType` = `STOP_LOSS/TAKE_PROFIT` | `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta` |

        |`pendingBelowType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` | `pendingBelowPrice`， `pendingBelowStopPrice` 与/或
        `pendingBelowTrailingDelta`， `pendingBelowTimeInForce` |
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
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
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: RumwQpBaDctlUu5jyG5rs0
                  description: >-
                    Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list
                    with the same `listClientOrderId` is accepted only when the previous one is filled or completely
                    expired. `listClientOrderId` is distinct from the `workingClientOrderId`,
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
                  description: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
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
                    Arbitrary numeric value identifying the working order strategy. Values smaller than `1000000` are
                    reserved and cannot be used.
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
                  description: "Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`"
                  x-description-cn: 支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
                pendingAboveClientOrderId:
                  type: string
                  example: pendingAboveOrder1
                  description: >-
                    Arbitrary unique ID among open orders for the pending above order. Automatically generated if not
                    sent.
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
                    Arbitrary numeric value identifying the pending above order strategy. Values smaller than `1000000`
                    are reserved and cannot be used.
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
                    Arbitrary unique ID among open orders for the pending below order. Automatically generated if not
                    sent.
                  x-description-cn: 用于标识待处理下方订单的唯一ID。 如果未发送则自动生成。
                pendingBelowPrice:
                  type: number
                  format: float
                  example: 1
                  description: >-
                    Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit
                    price.
                  x-description-cn: 当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。
                pendingBelowStopPrice:
                  type: number
                  format: float
                  example: 1
                  description: >-
                    Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
                    `TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be
                    specified.
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
                    Arbitrary numeric value identifying the pending below order strategy. Values smaller than `1000000`
                    are reserved and cannot be used.
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
                workingQuoteNotionalLimit:
                  type: number
                  format: float
                  example: 100
                  description: >-
                    Quote notional limit for the working order (only for orders on the BUY side). See [Quote Notional
                    Limit](/products/spot/faqs/quoteNotionalLimit).
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
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      x-response-notes: >-
        **Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in
        Order Responses](/products/spot/rest-api#conditional-fields-in-order-responses).
      x-response-notes-cn: >-
        **注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看
        [订单响应中的特定条件时才会出现的字段](/products/spot/rest-api#conditional-fields-in-order-responses) 部分。
      responses:
        "200":
          description: New Order list - OTOCO
          x-description-cn: New 订单 列表- OTOCO
          content:
            application/json:
              schema:
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
                    example: RumwQpBaDctlUu5jyG5rs0
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1712291372842
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 6
                        clientOrderId: fM9Y4m23IFJVCQmIrlUmMK
                      - symbol: LTCBTC
                        orderId: 7
                        clientOrderId: 6pcQbFIzTXGZQ1e2MkGDq4
                      - symbol: LTCBTC
                        orderId: 8
                        clientOrderId: r4JMv9cwAYYUwwBZfbussx
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 6
                        clientOrderId:
                          type: string
                          example: fM9Y4m23IFJVCQmIrlUmMK
                  orderReports:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 6
                        orderListId: 1
                        clientOrderId: fM9Y4m23IFJVCQmIrlUmMK
                        transactTime: 1712291372842
                        price: "1.00000000"
                        origQty: "1.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT
                        side: SELL
                        workingTime: 1712291372842
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        orderId: 7
                        orderListId: 1
                        clientOrderId: 6pcQbFIzTXGZQ1e2MkGDq4
                        transactTime: 1712291372842
                        price: "1.00000000"
                        origQty: "5.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: PENDING_NEW
                        timeInForce: IOC
                        type: STOP_LOSS_LIMIT
                        side: BUY
                        stopPrice: "6.00000000"
                        workingTime: -1
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        orderId: 8
                        orderListId: 1
                        clientOrderId: r4JMv9cwAYYUwwBZfbussx
                        transactTime: 1712291372842
                        price: "3.00000000"
                        origQty: "5.00000000"
                        executedQty: "0.00000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.00000000"
                        status: PENDING_NEW
                        timeInForce: GTC
                        type: LIMIT_MAKER
                        side: BUY
                        workingTime: -1
                        selfTradePreventionMode: NONE
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
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
                          example: fM9Y4m23IFJVCQmIrlUmMK
                        transactTime:
                          type: integer
                          format: int64
                          example: 1712291372842
                        price:
                          type: string
                          example: "1.00000000"
                        origQty:
                          type: string
                          example: "1.00000000"
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
                          example: 1712291372842
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
  /api/v3/order/oco:
    post:
      summary: New OCO - Deprecated (TRADE)
      x-summary-cn: 发送新 OCO 订单 - 已弃用 (TRADE)
      description: |-
        Send in a new OCO.

        - Price Restrictions:
          - `SELL`: Limit Price > Last Price > Stop Price
          - `BUY`: Limit Price < Last Price < Stop Price
        - Quantity Restrictions:
          - Both legs must have the same quantity.
          - `ICEBERG` quantities however do not have to be the same
        - `OCO` adds **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.
      x-description-cn: |-
        发送新的 OCO。

        - 价格限制：
          - `SELL`： Limit price > 最后交易价格 > stop Price
          - `BUY`： Limit price < 最后交易价格 < stop Price
        - 数量限制：
          - 两条腿的数量必须相同。
          - 不过， `冰山` 交易的数量不一定相同
        - `OCO` 将**2个订单**添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。
      deprecated: true
      tags:
        - trade
      operationId: orderOco
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderOco/OrderOco.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderOcoExample.php
      x-ip-weight: 1
      x-legacy-anchors:
        - order-lists
      x-order-weight: 2
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
      x-parameters-notes: "**Data Source:** Matching Engine"
      x-parameters-notes-cn: "**数据源:** 撮合引擎"
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
                - price
                - stopPrice
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BNBUSDT
                listClientOrderId:
                  type: string
                  example: JYVpp3F0f5CAG15DhtrqLp
                  description: A unique Id for the entire orderList
                  x-description-cn: 整个orderList的唯一ID
                side:
                  type: string
                  enum:
                    - BUY
                    - SELL
                  example: BUY
                quantity:
                  type: number
                  format: float
                  example: 1
                limitClientOrderId:
                  type: string
                  example: limitOrder1
                  description: A unique Id for the limit order
                  x-description-cn: 限价单的唯一ID
                price:
                  type: number
                  format: float
                  example: 1
                limitStrategyId:
                  type: integer
                  format: int64
                  example: 1
                limitStrategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 不能低于 `1000000`
                limitIcebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used to make the `LIMIT_MAKER` leg an iceberg order.
                  x-description-cn: 用于使 `LIMIT_MAKER` 腿单成为冰山订单。
                trailingDelta:
                  type: integer
                  format: int64
                  example: 1
                stopClientOrderId:
                  type: string
                  example: stopOrder1
                  description: A unique Id for the stop loss/stop loss limit leg
                  x-description-cn: 止损/止损限价单的唯一ID
                stopPrice:
                  type: number
                  format: float
                  example: 1
                stopStrategyId:
                  type: integer
                  format: int64
                  example: 1
                stopStrategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 不能低于 `1000000`
                stopLimitPrice:
                  type: number
                  format: float
                  example: 1
                  description: If provided, `stopLimitTimeInForce` is required.
                  x-description-cn: 如果提供，须配合提交`stopLimitTimeInForce`
                stopIcebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.
                  x-description-cn: 与 `STOP_LOSS_LIMIT` 腿单一起使用，使其成为冰山订单。
                stopLimitTimeInForce:
                  type: string
                  enum:
                    - GTC
                    - IOC
                    - FOK
                  example: GTC
                  description: Valid values are `GTC`/`FOK`/`IOC`
                  x-description-cn: 有效值 `GTC`/`FOK`/`IOC`
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
                  description: >-
                    The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision
                    (e.g., 6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: New OCO - Deprecated
          x-description-cn: 发送新 OCO 订单 - 已弃用
          content:
            application/json:
              schema:
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
                    example: JYVpp3F0f5CAG15DhtrqLp
                  transactionTime:
                    type: integer
                    format: int64
                    example: 1563417480525
                  symbol:
                    type: string
                    example: LTCBTC
                  orders:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 2
                        clientOrderId: Kk7sqHb9J6mJWTMDVW7Vos
                      - symbol: LTCBTC
                        orderId: 3
                        clientOrderId: xTXKaGYd4bluPVp78IVRvl
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 2
                        clientOrderId:
                          type: string
                          example: Kk7sqHb9J6mJWTMDVW7Vos
                  orderReports:
                    type: array
                    example:
                      - symbol: LTCBTC
                        orderId: 2
                        orderListId: 0
                        clientOrderId: Kk7sqHb9J6mJWTMDVW7Vos
                        transactTime: 1563417480525
                        price: "0.000000"
                        origQty: "0.624363"
                        executedQty: "0.000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.000000"
                        status: NEW
                        timeInForce: GTC
                        type: STOP_LOSS
                        side: BUY
                        stopPrice: "0.960664"
                        workingTime: -1
                        selfTradePreventionMode: NONE
                      - symbol: LTCBTC
                        orderId: 3
                        orderListId: 0
                        clientOrderId: xTXKaGYd4bluPVp78IVRvl
                        transactTime: 1563417480525
                        price: "0.036435"
                        origQty: "0.624363"
                        executedQty: "0.000000"
                        origQuoteOrderQty: "0.000000"
                        cummulativeQuoteQty: "0.000000"
                        status: NEW
                        timeInForce: GTC
                        type: LIMIT_MAKER
                        side: BUY
                        workingTime: 1563417480525
                        selfTradePreventionMode: NONE
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                        orderId:
                          type: integer
                          format: int64
                          example: 2
                        orderListId:
                          type: integer
                          format: int64
                          example: 0
                        clientOrderId:
                          type: string
                          example: Kk7sqHb9J6mJWTMDVW7Vos
                        transactTime:
                          type: integer
                          format: int64
                          example: 1563417480525
                        price:
                          type: string
                          example: "0.000000"
                        origQty:
                          type: string
                          example: "0.624363"
                        executedQty:
                          type: string
                          example: "0.000000"
                        origQuoteOrderQty:
                          type: string
                          example: "0.000000"
                        cummulativeQuoteQty:
                          type: string
                          example: "0.000000"
                        status:
                          type: string
                          example: NEW
                        timeInForce:
                          type: string
                          example: GTC
                        type:
                          type: string
                          example: STOP_LOSS
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
                        stopPrice:
                          type: string
                          example: "0.960664"
  /api/v3/order/test:
    post:
      summary: Test new order (TRADE)
      x-summary-cn: 测试下单接口 (TRADE)
      description: |-
        Test new order creation and signature/recvWindow long.

        Creates and validates a new order but does not send it into the matching
        engine.
      x-description-cn: 用于测试订单请求，但不会提交到撮合引擎
      tags:
        - trade
      operationId: orderTest
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#order-test
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/orderTest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/order_test.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/order_test.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/OrderTestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/OrderTest/OrderTest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/OrderTestExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        |Condition|Weight|
        |---|---|
        |Without `computeCommissionRates`|1|
        |With `computeCommissionRates`|20|
      x-weight-cn: |-
        |条件|权重|
        |---|---|
        |没有 `computeCommissionRates`|1|
        |有 `computeCommissionRates`|20|
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
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - type
                - timestamp
              properties:
                computeCommissionRates:
                  type: boolean
                  example: false
                  description: >-
                    Default: `false` <br> See [Commissions
                    FAQ](/products/spot/faqs/commission_faq#test-order-diferences) to learn more.
                  x-description-cn: "默认值: `false` <br> 请参阅[佣金常见问题解答](/products/spot/faqs/commission_faq#test-order-diferences) 了解更多信息。"
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
                quantity:
                  type: number
                  format: float
                  example: 1
                quoteOrderQty:
                  type: number
                  format: float
                  example: 1
                price:
                  type: number
                  format: float
                  example: 400
                newClientOrderId:
                  type: string
                  example: myOrder1
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Orders with the same
                    `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be
                    rejected.
                  x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。
                strategyId:
                  type: integer
                  format: int64
                  example: 1
                strategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 不能低于 `1000000`。
                stopPrice:
                  type: number
                  format: float
                  example: 1
                  description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                  x-description-cn: 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。
                trailingDelta:
                  type: integer
                  format: int64
                  example: 1
                  description: See [Trailing Stop order FAQ](/products/spot/faqs/trailing-stop-faq)
                  x-description-cn: 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/products/spot/faqs/trailing-stop-faq)
                icebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
                  x-description-cn: 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
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
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: Test new order
          x-description-cn: 测试下单接口
          content:
            application/json:
              schema:
                oneOf:
                  - description: Without `computeCommissionRates`
                    x-description-cn: 没有 `computeCommissionRates`
                    type: object
                    properties: {}
                  - description: With `computeCommissionRates`
                    x-description-cn: 有 `computeCommissionRates`
                    type: object
                    properties:
                      standardCommissionForOrder:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.00000112"
                          taker:
                            type: string
                            example: "0.00000114"
                        description: Standard commission rates on trades from the order.
                        x-description-cn: 订单交易的标准佣金率
                      specialCommissionForOrder:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.05000000"
                          taker:
                            type: string
                            example: "0.06000000"
                        description: Special commission rates on trades from the order.
                        x-description-cn: 订单交易的特殊佣金率
                      taxCommissionForOrder:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.00000112"
                          taker:
                            type: string
                            example: "0.00000114"
                        description: Tax commission rates for trades from the order.
                        x-description-cn: 订单交易的税率
                      discount:
                        type: object
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
                            example: "0.25000000"
                        description: Discount on standard commissions when paying in BNB.
                        x-description-cn: 以BNB支付时的标准佣金折扣。
  /api/v3/sor/order:
    post:
      summary: New order using SOR (TRADE)
      x-summary-cn: 下 SOR 订单 (TRADE)
      description: |-
        Places an order using smart order routing (SOR).

        This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

        Read [SOR FAQ](/products/spot/faqs/sor_faq) to learn more.
      x-description-cn: |-
        发送使用智能订单路由 (SOR) 的新订单。

        这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

        参阅 [智能订单路由 (SOR)](/products/spot/faqs/sor_faq) 了解更多详情。
      tags:
        - trade
      operationId: sorOrder
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#sor-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/sorOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/sor_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/sor_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/SorOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/SorOrder/SorOrder.go
        php: https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/SorOrderExample.php
      x-ip-weight: 1
      x-legacy-anchors:
        - sor
      x-order-weight: 1
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
      x-parameters-notes: |-
        **Data Source:** Matching Engine

        **Note:** `POST /api/v3/sor/order` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.
      x-parameters-notes-cn: |-
        **数据源:** 撮合引擎

        **请注意:** `POST /api/v3/sor/order` 只支持 `限价` 和 `市场` 单， 并不支持 `quoteOrderQty`。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - type
                - quantity
                - timestamp
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
                type:
                  type: string
                  enum:
                    - MARKET
                    - LIMIT
                  example: MARKET
                timeInForce:
                  type: string
                  enum:
                    - GTC
                    - IOC
                    - FOK
                  example: GTC
                quantity:
                  type: number
                  format: float
                  example: 1
                price:
                  type: number
                  format: float
                  example: 400
                newClientOrderId:
                  type: string
                  example: myOrder1
                  description: >-
                    A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same
                    `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be
                    rejected.
                  x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，<br/>那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。
                strategyId:
                  type: integer
                  format: int64
                  example: 1
                strategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 赋值不能小于 `1000000`.
                icebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used with `LIMIT` to create an iceberg order.
                  x-description-cn: 仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                newOrderRespType:
                  type: string
                  enum:
                    - ACK
                    - RESULT
                    - FULL
                  example: ACK
                  description: Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`
                  x-description-cn: "指定响应类型:"
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
                    The allowed enums is dependent on what is configured on the symbol. The possible supported values
                    are: [STP Modes](/products/spot/enums#stpmodes).
                  x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/products/spot/enums#stpmodes)。
                recvWindow:
                  type: number
                  format: float
                  example: 5000
                  description: >-
                    The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision
                    (e.g., 6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 <br> 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: New order using SOR
          x-description-cn: 下 SOR 订单
          content:
            application/json:
              schema:
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
                  selfTradePreventionMode:
                    type: string
                    example: NONE
                  usedSor:
                    type: boolean
                    example: true
  /api/v3/sor/order/test:
    post:
      summary: Test new order using SOR (TRADE)
      x-summary-cn: 测试 SOR 下单接口 (TRADE)
      description: |-
        Test new order creation and signature/recvWindow using smart order routing (SOR).
        Creates and validates a new order but does not send it into the matching engine.
      x-description-cn: 用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎
      tags:
        - trade
      operationId: sorOrderTest
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#sor-order-test
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/spot/examples/rest-api/TradeApi/sorOrderTest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/spot/rest_api/trade_api/sor_order_test.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/spot/examples/rest_api/Trade/sor_order_test.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/spot/src/main/java/com/binance/connector/client/spot/rest/trade/SorOrderTestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/spot/examples/restapi/TradeAPI/SorOrderTest/SorOrderTest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/spot/trade/SorOrderTestExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        |Condition|Weight|
        |---|---|
        |Without `computeCommissionRates`|1|
        |With `computeCommissionRates`|20|
      x-weight-cn: |-
        |条件|权重|
        |---|---|
        |没有 `computeCommissionRates`|1|
        |有 `computeCommissionRates`|20|
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
      x-parameters-notes: "**Data Source:** Memory"
      x-parameters-notes-cn: "**数据源:** 缓存"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - type
                - quantity
                - timestamp
              properties:
                computeCommissionRates:
                  type: boolean
                  example: false
                  default: false
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
                quantity:
                  type: number
                  format: float
                  example: 1
                price:
                  type: number
                  format: float
                  example: 400
                newClientOrderId:
                  type: string
                  example: myOrder1
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Orders with the same
                    `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be
                    rejected.
                  x-description-cn: 用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。
                strategyId:
                  type: integer
                  format: int64
                  example: 1
                strategyType:
                  type: integer
                  example: 1
                  description: The value cannot be less than `1000000`.
                  x-description-cn: 赋值不能小于 `1000000`。
                icebergQty:
                  type: number
                  format: float
                  example: 1
                  description: Used with `LIMIT` to create an iceberg order.
                  x-description-cn: 仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
                newOrderRespType:
                  type: string
                  enum:
                    - ACK
                    - RESULT
                    - FULL
                  example: ACK
                  description: Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`.
                  x-description-cn: "指定响应类型: `ACK`, `RESULT` 或 `FULL`; 默认为 `FULL`。"
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
                  description: >-
                    The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g.,
                    6000.346) so that microseconds may be specified.
                  x-description-cn: 最大值为 `60000` 毫秒。 支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp used to sign the request, in milliseconds or microseconds. The value must reflect the
                    current client

                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒或微秒。该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验。
      responses:
        "200":
          description: Test new order using SOR
          x-description-cn: 测试 SOR 下单接口
          content:
            application/json:
              schema:
                oneOf:
                  - description: Without `computeCommissionRates`
                    x-description-cn: 没有 `computeCommissionRates`
                    type: object
                    properties: {}
                  - description: With `computeCommissionRates`
                    x-description-cn: 有 `computeCommissionRates`
                    type: object
                    properties:
                      standardCommissionForOrder:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.00000112"
                          taker:
                            type: string
                            example: "0.00000114"
                        description: Standard commission rates on trades from the order.
                        x-description-cn: 订单交易的标准佣金率。
                      taxCommissionForOrder:
                        type: object
                        properties:
                          maker:
                            type: string
                            example: "0.00000112"
                          taker:
                            type: string
                            example: "0.00000114"
                        description: Tax commission rates for trades from the order.
                        x-description-cn: 订单交易的税率。
                      discount:
                        type: object
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
                            example: "0.25000000"
                        description: Discount on standard commissions when paying in BNB.
                        x-description-cn: 以BNB支付时的标准佣金折扣。
components:
  schemas:
    myFiltersResponse:
      type: object
      properties:
        exchangeFilters:
          type: array
          items:
            oneOf:
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ORDERS
                  maxNumOrders:
                    type: integer
                    format: int64
                    example: 1000
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ALGO_ORDERS
                  maxNumAlgoOrders:
                    type: integer
                    format: int64
                    example: 200
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
                  maxNumIcebergOrders:
                    type: integer
                    format: int64
                    example: 10
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ORDER_LISTS
                  maxNumOrderLists:
                    type: integer
                    format: int64
                    example: 20
            discriminator:
              propertyName: filterType
              mapping:
                EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
                EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
                EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
                EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
        symbolFilters:
          type: array
          items:
            oneOf:
              - type: object
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
              - type: object
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
              - type: object
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
              - type: object
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
              - type: object
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
              - type: object
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
              - type: object
                properties:
                  filterType:
                    type: string
                    example: ICEBERG_PARTS
                  limit:
                    type: integer
                    format: int64
                    example: 10
              - type: object
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
              - type: object
                properties:
                  filterType:
                    type: string
                    example: MAX_NUM_ORDERS
                  maxNumOrders:
                    type: integer
                    format: int64
                    example: 200
              - type: object
                properties:
                  filterType:
                    type: string
                    example: MAX_NUM_ALGO_ORDERS
                  maxNumAlgoOrders:
                    type: integer
                    format: int64
                    example: 10
              - type: object
                properties:
                  filterType:
                    type: string
                    example: MAX_NUM_ICEBERG_ORDERS
                  maxNumIcebergOrders:
                    type: integer
                    format: int64
                    example: 5
              - type: object
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
              - type: object
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
              - type: object
                properties:
                  filterType:
                    type: string
                    example: T_PLUS_SELL
                  endTime:
                    type: integer
                    format: int64
                    example: 1741672924895
              - type: object
                properties:
                  filterType:
                    type: string
                    example: MAX_NUM_ORDER_LISTS
                  maxNumOrderLists:
                    type: integer
                    format: int64
                    example: 20
              - type: object
                properties:
                  filterType:
                    type: string
                    example: MAX_NUM_ORDER_AMENDS
                  maxNumOrderAmends:
                    type: integer
                    format: int64
                    example: 10
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
          type: array
          items:
            oneOf:
              - type: object
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
                    example: "100.00000000"
                  asset:
                    type: string
                    example: BNB
            discriminator:
              propertyName: filterType
              mapping:
                MAX_ASSET: "#/components/schemas/MaxAssetFilter"
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
                example: 321
    exchangeFilters:
      oneOf:
        - type: object
          properties:
            filterType:
              type: string
              example: EXCHANGE_MAX_NUM_ORDERS
            maxNumOrders:
              type: integer
              format: int64
              example: 1000
        - type: object
          properties:
            filterType:
              type: string
              example: EXCHANGE_MAX_NUM_ALGO_ORDERS
            maxNumAlgoOrders:
              type: integer
              format: int64
              example: 200
        - type: object
          properties:
            filterType:
              type: string
              example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
            maxNumIcebergOrders:
              type: integer
              format: int64
              example: 10
        - type: object
          properties:
            filterType:
              type: string
              example: EXCHANGE_MAX_NUM_ORDER_LISTS
            maxNumOrderLists:
              type: integer
              format: int64
              example: 20
      discriminator:
        propertyName: filterType
        mapping:
          EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
          EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
          EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
          EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
    symbolFilters:
      oneOf:
        - type: object
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
        - type: object
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
        - type: object
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
        - type: object
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
        - type: object
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
        - type: object
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
        - type: object
          properties:
            filterType:
              type: string
              example: ICEBERG_PARTS
            limit:
              type: integer
              format: int64
              example: 10
        - type: object
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
        - type: object
          properties:
            filterType:
              type: string
              example: MAX_NUM_ORDERS
            maxNumOrders:
              type: integer
              format: int64
              example: 200
        - type: object
          properties:
            filterType:
              type: string
              example: MAX_NUM_ALGO_ORDERS
            maxNumAlgoOrders:
              type: integer
              format: int64
              example: 10
        - type: object
          properties:
            filterType:
              type: string
              example: MAX_NUM_ICEBERG_ORDERS
            maxNumIcebergOrders:
              type: integer
              format: int64
              example: 5
        - type: object
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
        - type: object
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
        - type: object
          properties:
            filterType:
              type: string
              example: T_PLUS_SELL
            endTime:
              type: integer
              format: int64
              example: 1741672924895
        - type: object
          properties:
            filterType:
              type: string
              example: MAX_NUM_ORDER_LISTS
            maxNumOrderLists:
              type: integer
              format: int64
              example: 20
        - type: object
          properties:
            filterType:
              type: string
              example: MAX_NUM_ORDER_AMENDS
            maxNumOrderAmends:
              type: integer
              format: int64
              example: 10
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
        - type: object
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
              example: "100.00000000"
            asset:
              type: string
              example: BNB
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
          example: "100.00000000"
        asset:
          type: string
          example: BNB
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
          example: 321
    exchangeInfoResponse:
      type: object
      properties:
        timezone:
          type: string
          example: UTC
        serverTime:
          type: integer
          format: int64
          example: 1565246363776
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
                example: 321
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
            oneOf:
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ORDERS
                  maxNumOrders:
                    type: integer
                    format: int64
                    example: 1000
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ALGO_ORDERS
                  maxNumAlgoOrders:
                    type: integer
                    format: int64
                    example: 200
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ICEBERG_ORDERS
                  maxNumIcebergOrders:
                    type: integer
                    format: int64
                    example: 10
              - type: object
                properties:
                  filterType:
                    type: string
                    example: EXCHANGE_MAX_NUM_ORDER_LISTS
                  maxNumOrderLists:
                    type: integer
                    format: int64
                    example: 20
            discriminator:
              propertyName: filterType
              mapping:
                EXCHANGE_MAX_NUM_ORDERS: "#/components/schemas/ExchangeMaxNumOrdersFilter"
                EXCHANGE_MAX_NUM_ALGO_ORDERS: "#/components/schemas/ExchangeMaxNumAlgoOrdersFilter"
                EXCHANGE_MAX_NUM_ICEBERG_ORDERS: "#/components/schemas/ExchangeMaxNumIcebergOrdersFilter"
                EXCHANGE_MAX_NUM_ORDER_LISTS: "#/components/schemas/ExchangeMaxNumOrderListsFilter"
        symbols:
          type: array
          items:
            type: object
            properties:
              symbol:
                type: string
                example: ETHBTC
              status:
                type: string
                example: TRADING
              baseAsset:
                type: string
                example: ETH
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
                description: will be removed in future api versions (v4+)
                x-description-cn: 将在未来的 api 版本中移除 (v4+)
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
                  - STOP_LOSS
                  - STOP_LOSS_LIMIT
                  - TAKE_PROFIT
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
                example: false
              cancelReplaceAllowed:
                type: boolean
                example: false
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
                items:
                  oneOf:
                    - type: object
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
                    - type: object
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
                    - type: object
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
                    - type: object
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
                    - type: object
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
                    - type: object
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
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: ICEBERG_PARTS
                        limit:
                          type: integer
                          format: int64
                          example: 10
                    - type: object
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
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: MAX_NUM_ORDERS
                        maxNumOrders:
                          type: integer
                          format: int64
                          example: 200
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: MAX_NUM_ALGO_ORDERS
                        maxNumAlgoOrders:
                          type: integer
                          format: int64
                          example: 10
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: MAX_NUM_ICEBERG_ORDERS
                        maxNumIcebergOrders:
                          type: integer
                          format: int64
                          example: 5
                    - type: object
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
                    - type: object
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
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: T_PLUS_SELL
                        endTime:
                          type: integer
                          format: int64
                          example: 1741672924895
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: MAX_NUM_ORDER_LISTS
                        maxNumOrderLists:
                          type: integer
                          format: int64
                          example: 20
                    - type: object
                      properties:
                        filterType:
                          type: string
                          example: MAX_NUM_ORDER_AMENDS
                        maxNumOrderAmends:
                          type: integer
                          format: int64
                          example: 10
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
              permissions:
                type: array
                items:
                  type: string
                  example: undefined
              permissionSets:
                type: array
                items:
                  type: array
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
                items:
                  type: string
                  example: BTCUSDT
```