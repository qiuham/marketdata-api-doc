---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:34.029448
---

# core-trading-derivatives-trading-coin-m-futures__ws-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Futures (COIN-M) WebSocket API
  description: Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.
  x-description-cn: 访问市场数据、管理账户，并交易 COIN-M 永续合约和交割合约。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-api
x-rate-limits-guide: products/derivatives-trading-coin-futures/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-coin-futures/general-info#访问限制
x-security-guide: products/derivatives-trading-coin-futures/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-coin-futures/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Futures (COIN-M) docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/general-info
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: user-data-streams
    x-displayName: User Data Streams
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: wss://ws-dapi.binance.com/ws-dapi/v1
  - url: wss://testnet.binancefuture.com/ws-dapi/v1
paths:
  /account.status:
    post:
      summary: Account Information (USER_DATA)
      x-summary-cn: 账户信息 (USER_DATA)
      description: |-
        Get current account information. User in single-asset/ multi-assets mode
        will see different value, see comments in response section for detail.
      x-description-cn: 现有账户信息。
      tags:
        - account
      operationId: accountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/account#account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/AccountApi/accountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/account_api/account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Account/account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/account/AccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/AccountAPI/AccountInformation/AccountInformation.go
      x-ip-weight: 5
      x-security-type: USER_DATA
      x-signed: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
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
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: account.status
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account Information
          x-description-cn: 账户 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: baaec739-c5cf-4920-b448-c0b9c5431410
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      feeTier:
                        type: integer
                        example: 0
                        format: int64
                        description: Fee tier level.
                        x-description-cn: 手续费等级.
                      canTrade:
                        type: boolean
                        example: true
                        description: Whether trading is enabled.
                        x-description-cn: 是否可交易.
                      canDeposit:
                        type: boolean
                        example: true
                        description: Whether deposits are enabled.
                        x-description-cn: 是否可充值.
                      canWithdraw:
                        type: boolean
                        example: true
                        description: Whether withdrawals are enabled.
                        x-description-cn: 是否可提现.
                      updateTime:
                        type: integer
                        example: 0
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: WLD
                              description: asset name
                              x-description-cn: 资产
                            walletBalance:
                              type: string
                              example: "0.00000000"
                              description: total wallet balance
                              x-description-cn: 账户余额
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit or loss
                              x-description-cn: 全部持仓未实现盈亏
                            marginBalance:
                              type: string
                              example: "0.00000000"
                              description: margin balance
                              x-description-cn: 保证金余额
                            maintMargin:
                              type: string
                              example: "0.00000000"
                              description: maintenance margin
                              x-description-cn: 维持保证金
                            initialMargin:
                              type: string
                              example: "0.00000000"
                              description: total intial margin required with the latest mark price
                              x-description-cn: 当前所需起始保证金(按最新标标记价格)
                            positionInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: positions" margin required with the latest mark price
                              x-description-cn: 当前所需持仓起始保证金(按最新标标记价格)
                            openOrderInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: open orders" intial margin required with the latest mark price
                              x-description-cn: 当前所需挂单起始保证金(按最新标标记价格)
                            maxWithdrawAmount:
                              type: string
                              example: "0.00000000"
                              description: maximum amount for transfer out
                              x-description-cn: 最大可转出余额
                            crossWalletBalance:
                              type: string
                              example: "0.00000000"
                              description: wallet balance for crossed margin
                              x-description-cn: 可用于全仓的账户余额
                            crossUnPnl:
                              type: string
                              example: "0.00000000"
                              description: total unrealized profit or loss of crossed positions
                              x-description-cn: 所有全仓持仓的未实现盈亏
                            availableBalance:
                              type: string
                              example: "0.00000000"
                              description: available margin balance
                              x-description-cn: 可用下单余额
                            updateTime:
                              type: integer
                              example: 0
                              format: int64
                              description: update time
                              x-description-cn: 更新时间
                        description: Supported assets.
                        x-description-cn: 支持的资产列表。
                      positions:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: ETHUSD_220930
                              description: Trading symbol
                              x-description-cn: 交易对
                            initialMargin:
                              type: string
                              example: "0"
                              description: total intial margin required with the latest mark price
                              x-description-cn: 当前所需起始保证金(按最新标标记价格)
                            maintMargin:
                              type: string
                              example: "0"
                              description: maintenance margin
                              x-description-cn: 维持保证金
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit or loss
                              x-description-cn: 全部持仓未实现盈亏
                            positionInitialMargin:
                              type: string
                              example: "0"
                              description: positions" margin required with the latest mark price
                              x-description-cn: 当前所需持仓起始保证金(按最新标标记价格)
                            openOrderInitialMargin:
                              type: string
                              example: "0"
                              description: open orders" intial margin required with the latest mark price
                              x-description-cn: 当前所需挂单起始保证金(按最新标标记价格)
                            leverage:
                              type: string
                              example: "7"
                              description: Leverage value.
                              x-description-cn: 杠杆倍数.
                            isolated:
                              type: boolean
                              example: false
                              description: Whether isolated margin mode is enabled.
                              x-description-cn: 是否为逐仓模式.
                            positionSide:
                              type: string
                              example: BOTH
                              description: Position side
                              x-description-cn: 持仓方向
                            entryPrice:
                              type: string
                              example: "0.00000000"
                              description: Position entry price.
                              x-description-cn: 持仓开仓价格.
                            maxQty:
                              type: string
                              example: "1000"
                              description: maximum quantity of base asset
                              x-description-cn: 数量上限, 最大数量
                            notionalValue:
                              type: string
                              example: "0"
                              description: Notional value.
                              x-description-cn: 名义价值.
                            isolatedWallet:
                              type: string
                              example: "0"
                              description: Isolated wallet balance.
                              x-description-cn: 逐仓钱包余额.
                            updateTime:
                              type: integer
                              example: 0
                              format: int64
                              description: update time
                              x-description-cn: 更新时间
                            positionAmt:
                              type: string
                              example: "0"
                              description: position amount
                              x-description-cn: 持仓数量
                            breakEvenPrice:
                              type: string
                              example: "0.00000000"
                              description: break-even price
                              x-description-cn: 盈亏平衡价
                        description: Position list.
                        x-description-cn: 持仓列表.
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 10
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /account.balance:
    post:
      summary: Futures Account Balance (USER_DATA)
      x-summary-cn: 账户余额 (USER_DATA)
      description: Futures Account Balance
      x-description-cn: 账户余额
      tags:
        - account
      operationId: futuresAccountBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/account#futures-account-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/AccountApi/futuresAccountBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/account_api/futures_account_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Account/futures_account_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/account/FuturesAccountBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/AccountAPI/FuturesAccountBalance/FuturesAccountBalance.go
      x-ip-weight: 5
      x-security-type: USER_DATA
      x-signed: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - account.balance
                  example: account.balance
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: account.balance
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Futures Account Balance
          x-description-cn: 合约 账户 Balance
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 9328e612-1560-4108-979e-283bf85b5acb
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        accountAlias:
                          type: string
                          example: fWAuTiuXoCuXmY
                          description: unique account code
                          x-description-cn: 账户唯一识别码
                        asset:
                          type: string
                          example: WLD
                          description: asset name
                          x-description-cn: 资产
                        balance:
                          type: string
                          example: "0.00000000"
                          description: Account balance.
                          x-description-cn: 账户余额.
                        withdrawAvailable:
                          type: string
                          example: "0.00000000"
                          description: Available amount for withdrawal.
                          x-description-cn: 可提现金额.
                        crossWalletBalance:
                          type: string
                          example: "0.00000000"
                          description: wallet balance for crossed margin
                          x-description-cn: 可用于全仓的账户余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: total unrealized profit or loss of crossed positions
                          x-description-cn: 所有全仓持仓的未实现盈亏
                        availableBalance:
                          type: string
                          example: "0.00000000"
                          description: available margin balance
                          x-description-cn: 可用下单余额
                        updateTime:
                          type: integer
                          example: 0
                          format: int64
                          description: update time
                          x-description-cn: 更新时间
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 10
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /order.cancel:
    post:
      summary: Cancel Order (TRADE)
      x-summary-cn: 撤销订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 撤销订单
      tags:
        - trade
      operationId: cancelOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/trade#cancel-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/TradeApi/cancelOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/trade_api/cancel_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Trade/cancel_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/trade/CancelOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/TradeAPI/CancelOrder/CancelOrder.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 或 `origClientOrderId` 至少需要发送一个。"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
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
                      example: BTCUSD_PERP
                    orderId:
                      type: integer
                      example: 1
                      format: int64
                    origClientOrderId:
                      type: string
                      example: "1"
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: order.cancel
              params:
                symbol: BTCUSD_PERP
                orderId: 1
                origClientOrderId: "1"
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Cancel Order
          x-description-cn: 取消订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: a8627ea5-8b9f-452f-90ae-4136f2b442e2
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 333245211
                        format: int64
                        description: Sub-order ID
                        x-description-cn: 子订单 ID
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Trading symbol
                        x-description-cn: 交易对
                      pair:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      status:
                        type: string
                        example: CANCELED
                        description: Status.
                        x-description-cn: 订单状态
                      clientOrderId:
                        type: string
                        example: 5SztZiGFAxgAqw4J9EN9fA
                        description: Client order ID.
                        x-description-cn: 客户端订单 ID.
                      price:
                        type: string
                        example: "51000"
                        description: Latest token price.
                        x-description-cn: 代币最新价格。
                      origQty:
                        type: string
                        example: "1"
                        description: Original order quantity
                        x-description-cn: 原始委托数量
                      executedQty:
                        type: string
                        example: "0"
                        description: Executed quantity
                        x-description-cn: 执行数量
                      cumQty:
                        type: string
                        example: "0"
                        description: Cumulative filled quantity.
                        x-description-cn: 累计成交数量.
                      timeInForce:
                        type: string
                        example: GTC
                        description: Time in force
                        x-description-cn: 有效方式
                      type:
                        type: string
                        example: LIMIT
                        description: Order type.
                        x-description-cn: 订单类型.
                      reduceOnly:
                        type: boolean
                        example: false
                        description: Whether the order is reduce-only.
                        x-description-cn: 是否为只减仓订单.
                      closePosition:
                        type: boolean
                        example: false
                        description: if Close-All
                        x-description-cn: 是否条件全平仓
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
                      stopPrice:
                        type: string
                        example: "0"
                        description: please ignore when order type is TRAILING_STOP_MARKET
                        x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                        description: Stop trigger price type.
                        x-description-cn: 止损触发价格类型.
                      priceProtect:
                        type: boolean
                        example: false
                        description: if conditional order trigger is protected
                        x-description-cn: 是否开启条件单触发保护
                      origType:
                        type: string
                        example: LIMIT
                        description: Original order type.
                        x-description-cn: 原始订单类型.
                      updateTime:
                        type: integer
                        example: 1728416138285
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 6
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /order.modify:
    post:
      summary: Modify Order (TRADE)
      x-summary-cn: 修改订单 (TRADE)
      description: |-
        Order modify function, currently only LIMIT order modification is
        supported, modified orders will be reordered in the match queue
      x-description-cn: 修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序
      tags:
        - trade
      operationId: modifyOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/trade#modify-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/TradeApi/modifyOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/trade_api/modify_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Trade/modify_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/trade/ModifyOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/TradeAPI/ModifyOrder/ModifyOrder.go
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
        1 on IP rate limit(x-mbx-used-weight-1m)
      x-parameters-notes: >-
        - Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.

        - Both `quantity` and `price` must be sent.

        - When the new `quantity` or `price` doesn't satisfy `PRICE_FILTER` / `PERCENT_FILTER` / `LOT_SIZE`, amendment
        will be rejected and the order will stay as it is.

        - However the order will be cancelled by the amendment in the following situations:
          - when the order is in partially filled status and the new `quantity` <= `executedQty`
          - When the order is `GTX` and the new price will cause it to be executed immediately
        - One order can only be modified for less than 10000 times.
      x-parameters-notes-cn: |-
        - 必须发送 `orderId` 或 `origClientOrderId` 其中之一，如果两个都发送，`orderId` 优先。
        - `quantity` 和 `price` 必须同时发送。
        - 当新的 `quantity` 或 `price` 不满足 `PRICE_FILTER` / `PERCENT_FILTER` / `LOT_SIZE` 时，修改将被拒绝，订单保持不变。
        - 但在以下情况下，订单将被修改操作取消：
          - 当订单处于部分成交状态且新的 `quantity` <= `executedQty` 时
          - 当订单为 `GTX` 且新价格会导致立即执行时
        - 一个订单最多只能修改 10000 次。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - order.modify
                  example: order.modify
                params:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 1
                      format: int64
                    origClientOrderId:
                      type: string
                      example: "1"
                    symbol:
                      type: string
                      example: BTCUSD_PERP
                    side:
                      type: string
                      example: BUY
                      enum:
                        - BUY
                        - SELL
                    quantity:
                      type: number
                      example: "1.0"
                      format: float
                      description: Order quantity, cannot be sent with `closePosition=true`
                      x-description-cn: 请参见英文说明：Order quantity, cannot be sent with `closePosition=true`
                    price:
                      type: number
                      example: "1.0"
                      format: float
                    priceMatch:
                      type: string
                      example: OPPONENT
                      enum:
                        - OPPONENT
                        - OPPONENT_5
                        - OPPONENT_10
                        - OPPONENT_20
                        - QUEUE
                        - QUEUE_5
                        - QUEUE_10
                        - QUEUE_20
                      description: only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`
                      x-description-cn: 仅对 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单有效；不能与 `price` 参数同时传递
                    modifyId:
                      type: integer
                      example: 1
                      format: int64
                      description: >-
                        User-defined modification identifier, returned as-is in the response. Optional; not validated
                        for uniqueness.
                      x-description-cn: 用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
                    - price
                    - timestamp
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: order.modify
              params:
                orderId: 1
                origClientOrderId: "1"
                symbol: BTCUSD_PERP
                side: BUY
                quantity: "1.0"
                price: "1.0"
                priceMatch: OPPONENT
                modifyId: 1
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Modify Order
          x-description-cn: Modify 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 88601d02-bd0d-430d-8733-2708a569ebda
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 333245211
                        format: int64
                        description: Sub-order ID
                        x-description-cn: 子订单 ID
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Trading symbol
                        x-description-cn: 交易对
                      pair:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      status:
                        type: string
                        example: NEW
                        description: Status.
                        x-description-cn: 订单状态
                      clientOrderId:
                        type: string
                        example: 5SztZiGFAxgAqw4J9EN9fA
                        description: Client order ID.
                        x-description-cn: 客户端订单 ID.
                      modifyId:
                        type: integer
                        example: 1
                        format: int64
                        description: user-defined modification identifier, only returned if provided in the request
                        x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                      price:
                        type: string
                        example: "51000"
                        description: Latest token price.
                        x-description-cn: 代币最新价格。
                      origQty:
                        type: string
                        example: "1"
                        description: Original order quantity
                        x-description-cn: 原始委托数量
                      executedQty:
                        type: string
                        example: "0"
                        description: Executed quantity
                        x-description-cn: 执行数量
                      cumQty:
                        type: string
                        example: "0"
                        description: Cumulative filled quantity.
                        x-description-cn: 累计成交数量.
                      timeInForce:
                        type: string
                        example: GTC
                        description: Time in force
                        x-description-cn: 有效方式
                      type:
                        type: string
                        example: LIMIT
                        description: Order type.
                        x-description-cn: 订单类型.
                      reduceOnly:
                        type: boolean
                        example: false
                        description: Whether the order is reduce-only.
                        x-description-cn: 是否为只减仓订单.
                      closePosition:
                        type: boolean
                        example: false
                        description: if Close-All
                        x-description-cn: 是否条件全平仓
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
                      stopPrice:
                        type: string
                        example: "0"
                        description: please ignore when order type is TRAILING_STOP_MARKET
                        x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                        description: Stop trigger price type.
                        x-description-cn: 止损触发价格类型.
                      priceProtect:
                        type: boolean
                        example: false
                        description: if conditional order trigger is protected
                        x-description-cn: 是否开启条件单触发保护
                      origType:
                        type: string
                        example: LIMIT
                        description: Original order type.
                        x-description-cn: 原始订单类型.
                      updateTime:
                        type: integer
                        example: 1728415765493
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 6
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /order.place:
    post:
      summary: New Order (TRADE)
      x-summary-cn: 下单 (TRADE)
      description: Send in a new order.
      x-description-cn: 下单
      tags:
        - trade
      operationId: newOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/TradeAPI/NewOrder/NewOrder.go
      x-ip-weight: 0
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: |-
        - Additional mandatory parameters based on `type`:
          | Type | Additional mandatory parameters |  | :---: | --- |  | `LIMIT` | `timeInForce`, `quantity`, `price` | | `MARKET` | `quantity` | | `STOP/TAKE_PROFIT` | `quantity`, `price`, `stopPrice` | | `STOP_MARKET/TAKE_PROFIT_MARKET` | `stopPrice` | | `TRAILING_STOP_MARKET` | `callbackRate` |
          - Order with type `STOP`, parameter `timeInForce` can be sent ( default `GTC`). * Order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`). * Condition orders will be triggered when:
          - If parameter `priceProtect` is sent as true:
          - when price reaches the `stopPrice`，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
          - "triggerProtect" of a symbol can be got from `GET /dapi/v1/exchangeInfo`
          - `STOP`, `STOP_MARKET`:
          - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
          - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`:
          - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
          - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
          - `TRAILING_STOP_MARKET`:
          - BUY: the lowest price after order placed <= `activationPrice`, and the latest price >= the lowest price * (1 + `callbackRate`)
          - SELL: the highest price after order placed >= `activationPrice`, and the latest price <= the highest price * (1 - `callbackRate`)
          - For `TRAILING_STOP_MARKET`, if you got such error code.
          - BUY: `activationPrice` should be smaller than latest price.
          - SELL: `activationPrice` should be larger than latest price.
          - If `newOrderRespType` is sent as `RESULT`:
          - `MARKET` order: the final FILLED result of the order will be return directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
          - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition=true`:
          - Follow the same rules for condition orders.
          - If triggered，**close all** current long position(if `SELL`) or current short position(if `BUY`).
          - Cannot be used with `quantity` parameter
          - Cannot be used with `reduceOnly` parameter
          - In Hedge Mode, cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side
      x-parameters-notes-cn: >-
        - 根据 order `type` 的不同,某些参数强制要求,具体如下: | Type | 强制要求的参数 |  | :---: | --- |  | `LIMIT` | `timeInForce`, `quantity`,
        `price` | | `MARKET` | `quantity` | | `STOP/TAKE_PROFIT` | `quantity`, `price`, `stopPrice` | |
        `STOP_MARKET/TAKE_PROFIT_MARKET` | `stopPrice` | | `TRAILING_STOP_MARKET` | `callbackRate` |
          - 条件单的触发必须:
          - 如果订单参数`priceProtect`为true:
          - 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
          - 触发保护阈值请参考接口`GET /dapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
          - `STOP`, `STOP_MARKET` 止损单:
          - 买入: 最新合约价格/标记价格高于等于触发价stopPrice
          - 卖出: 最新合约价格/标记价格低于等于触发价stopPrice
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单:
          - 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
          - 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
          - `TRAILING_STOP_MARKET` 跟踪止损单: * 买入: 当合约价格/标记价格区间最低价格低于激活价格`activationPrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。 * 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activationPrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。 * `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}` 表示订单不满足以下条件:
          - 买入: 指定的`activationPrice` 必须小于 latest price
          - 卖出: 指定的`activationPrice` 必须大于 latest price
          - `newOrderRespType` 如果传 `RESULT`:
          - `MARKET` 订单将直接返回成交结果；
          - 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
          - `STOP_MARKET`, `TAKE_PROFIT_MARKET` 配合 `closePosition`=`true`:
          - 条件单触发依照上述条件单触发逻辑
          - 条件触发后,平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)
          - 不支持 `quantity` 参数
          - 自带只平仓属性,不支持`reduceOnly`参数
          - 双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持SELL
          - `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`时生效.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
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
                      example: BTCUSD_PERP
                    side:
                      type: string
                      example: BUY
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
                      description: >-
                        Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode.  It must be sent in Hedge
                        Mode.
                      x-description-cn: One-way 模式默认 `BOTH`；Hedge 模式 `LONG` 或 `SHORT`，Hedge 模式必须发送
                    type:
                      type: string
                      example: LIMIT
                      enum:
                        - LIMIT
                        - MARKET
                        - STOP
                        - STOP_MARKET
                        - TAKE_PROFIT
                        - TAKE_PROFIT_MARKET
                        - TRAILING_STOP_MARKET
                      description: >-
                        **After CM migration, stop-type values (`STOP`, `STOP_MARKET`, `TAKE_PROFIT`,
                        `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`) are no longer accepted and will return `-4120`.
                        Use the REST `/dapi/v1/algoOrder` endpoint instead.**
                      x-description-cn: >-
                        **迁移后,本接口不再接受 stop
                        类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`),会返回
                        `-4120`。请改用 REST 接口 `/dapi/v1/algoOrder`。**
                    timeInForce:
                      type: string
                      example: GTC
                      enum:
                        - GTC
                        - IOC
                        - FOK
                        - GTX
                    quantity:
                      type: number
                      example: "1.0"
                      format: float
                      description: Quantity measured by contract number, Cannot be sent with `closePosition`=`true`
                      x-description-cn: 请参见英文说明：Quantity measured by contract number, Cannot be sent with `closePosition`=`true`
                    reduceOnly:
                      type: string
                      example: "true"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true` (Close-All)"
                      x-description-cn: 请参见英文说明：Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true` (Close-All)
                    price:
                      type: number
                      example: "1.0"
                      format: float
                    newClientOrderId:
                      type: string
                      example: "1"
                      description: >-
                        A unique id among open orders. Automatically generated if not sent. Can only be string following
                        the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                      x-description-cn: >-
                        请参见英文说明：A unique id among open orders. Automatically generated if not sent. Can only be string
                        following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                    stopPrice:
                      type: number
                      example: "1.0"
                      format: float
                      description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                      x-description-cn: 请参见英文说明：Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                    closePosition:
                      type: string
                      example: "true"
                      enum:
                        - "true"
                        - "false"
                      description: "`true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`."
                      x-description-cn: 请参见英文说明：`true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.
                    activationPrice:
                      type: number
                      example: "1.0"
                      format: float
                      description: >-
                        Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different
                        workingType)
                      x-description-cn: >-
                        请参见英文说明：Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting
                        different workingType)
                    callbackRate:
                      type: number
                      example: "5000.0"
                      format: float
                      description: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%
                      x-description-cn: 请参见英文说明：Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%
                    workingType:
                      type: string
                      example: MARK_PRICE
                      default: CONTRACT_PRICE
                      enum:
                        - MARK_PRICE
                        - CONTRACT_PRICE
                      description: 'stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"'
                      x-description-cn: '请参见英文说明：stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"'
                    priceProtect:
                      type: string
                      example: "true"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.'
                      x-description-cn: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                    newOrderRespType:
                      type: string
                      example: ACK
                      default: ACK
                      enum:
                        - ACK
                        - RESULT
                    priceMatch:
                      type: string
                      example: OPPONENT
                      enum:
                        - OPPONENT
                        - OPPONENT_5
                        - OPPONENT_10
                        - OPPONENT_20
                        - QUEUE
                        - QUEUE_5
                        - QUEUE_10
                        - QUEUE_20
                      description: only available for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`
                      x-description-cn: >-
                        请参见英文说明：only available for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with
                        `price`
                    selfTradePreventionMode:
                      type: string
                      example: NONE
                      default: NONE
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_BOTH
                        - EXPIRE_MAKER
                      description: >-
                        `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire
                        taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers
                      x-description-cn: >-
                        请参见英文说明：`NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`:
                        expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: order.place
              params:
                symbol: BTCUSD_PERP
                side: BUY
                positionSide: BOTH
                type: LIMIT
                timeInForce: GTC
                quantity: "1.0"
                reduceOnly: "true"
                price: "1.0"
                newClientOrderId: "1"
                stopPrice: "1.0"
                closePosition: "true"
                activationPrice: "1.0"
                callbackRate: "5000.0"
                workingType: MARK_PRICE
                priceProtect: "true"
                newOrderRespType: ACK
                priceMatch: OPPONENT
                selfTradePreventionMode: NONE
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: New Order
          x-description-cn: New 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 60fa4366-f96e-42fe-a82b-f819952c6db4
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 333245211
                        format: int64
                        description: Sub-order ID
                        x-description-cn: 子订单 ID
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Trading symbol
                        x-description-cn: 交易对
                      pair:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      status:
                        type: string
                        example: NEW
                        description: Status.
                        x-description-cn: 订单状态
                      clientOrderId:
                        type: string
                        example: 5SztZiGFAxgAqw4J9EN9fA
                        description: Client order ID.
                        x-description-cn: 客户端订单 ID.
                      price:
                        type: string
                        example: "50000"
                        description: Latest token price.
                        x-description-cn: 代币最新价格。
                      origQty:
                        type: string
                        example: "1"
                        description: Original order quantity
                        x-description-cn: 原始委托数量
                      executedQty:
                        type: string
                        example: "0"
                        description: Executed quantity
                        x-description-cn: 执行数量
                      cumQty:
                        type: string
                        example: "0"
                        description: Cumulative filled quantity.
                        x-description-cn: 累计成交数量.
                      timeInForce:
                        type: string
                        example: GTC
                        description: Time in force
                        x-description-cn: 有效方式
                      type:
                        type: string
                        example: LIMIT
                        description: Order type.
                        x-description-cn: 订单类型.
                      reduceOnly:
                        type: boolean
                        example: false
                        description: Whether the order is reduce-only.
                        x-description-cn: 是否为只减仓订单.
                      closePosition:
                        type: boolean
                        example: false
                        description: if Close-All
                        x-description-cn: 是否条件全平仓
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
                      stopPrice:
                        type: string
                        example: "0"
                        description: please ignore when order type is TRAILING_STOP_MARKET
                        x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                        description: Stop trigger price type.
                        x-description-cn: 止损触发价格类型.
                      priceProtect:
                        type: boolean
                        example: false
                        description: if conditional order trigger is protected
                        x-description-cn: 是否开启条件单触发保护
                      origType:
                        type: string
                        example: LIMIT
                        description: Original order type.
                        x-description-cn: 原始订单类型.
                      updateTime:
                        type: integer
                        example: 1728413795125
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 6
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /account.position:
    post:
      summary: Position Information (USER_DATA)
      x-summary-cn: 用户持仓风险 (USER_DATA)
      description: Get current position information.
      x-description-cn: 查询持仓风险
      tags:
        - trade
      operationId: positionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/trade#position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/TradeApi/positionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/trade_api/position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Trade/position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/trade/PositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/TradeAPI/PositionInformation/PositionInformation.go
      x-ip-weight: 5
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "- Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs."
      x-parameters-notes-cn: "- 请与用户数据流 `ACCOUNT_UPDATE` 配合使用，以满足时效性和准确性需求。"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - account.position
                  example: account.position
                params:
                  type: object
                  properties:
                    marginAsset:
                      type: string
                      example: USDT
                    pair:
                      type: string
                      example: BTCUSD
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: account.position
              params:
                marginAsset: USDT
                pair: BTCUSD
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Position Information
          x-description-cn: 持仓 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 233b8741-a96d-48e8-8ce1-160f43548aeb
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSD_PERP
                          description: Trading symbol
                          x-description-cn: 交易对
                        positionAmt:
                          type: string
                          example: "0"
                          description: position amount
                          x-description-cn: 持仓数量
                        entryPrice:
                          type: string
                          example: "0.00000000"
                          description: Position entry price.
                          x-description-cn: 持仓开仓价格.
                        markPrice:
                          type: string
                          example: "62297.60417296"
                          description: mark price
                          x-description-cn: 标记价格
                        unRealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: Unrealized profit.
                          x-description-cn: 未实现盈亏.
                        liquidationPrice:
                          type: string
                          example: "0"
                          description: Liquidation price.
                          x-description-cn: 强平价格.
                        leverage:
                          type: string
                          example: "7"
                          description: Leverage value.
                          x-description-cn: 杠杆倍数.
                        maxQty:
                          type: string
                          example: "100"
                          description: maximum quantity of base asset
                          x-description-cn: 数量上限, 最大数量
                        marginType:
                          type: string
                          example: cross
                          description: Margin type.
                          x-description-cn: 保证金模式.
                        isolatedMargin:
                          type: string
                          example: "0.00000000"
                          description: Isolated margin amount.
                          x-description-cn: 逐仓保证金数量.
                        isAutoAddMargin:
                          type: string
                          example: "false"
                          description: Whether auto-add margin is enabled.
                          x-description-cn: 是否开启自动追加保证金.
                        positionSide:
                          type: string
                          example: BOTH
                          description: Position side
                          x-description-cn: 持仓方向
                        notionalValue:
                          type: string
                          example: "0"
                          description: Notional value.
                          x-description-cn: 名义价值.
                        isolatedWallet:
                          type: string
                          example: "0"
                          description: Isolated wallet balance.
                          x-description-cn: 逐仓钱包余额.
                        updateTime:
                          type: integer
                          example: 1726731195634
                          format: int64
                          description: update time
                          x-description-cn: 更新时间
                        breakEvenPrice:
                          type: string
                          example: "0.00000000"
                          description: break-even price
                          x-description-cn: 盈亏平衡价
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 10
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /order.status:
    post:
      summary: Query Order (USER_DATA)
      x-summary-cn: 查询订单 (USER_DATA)
      description: |-
        Check an order's status.

        * These orders will not be found:
          * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
          * order create time + 90 days < current time
      x-description-cn: |-
        查询订单状态

        * 请注意，如果订单满足如下条件，不会被查询到：
          * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
          * 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: queryOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/trade#query-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/TradeApi/queryOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/trade_api/query_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/Trade/query_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/trade/QueryOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/TradeAPI/QueryOrder/QueryOrder.go
      x-ip-weight: 1
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 或 `origClientOrderId` 至少需要发送一个。"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
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
                      example: BTCUSD_PERP
                    orderId:
                      type: integer
                      example: 1
                      format: int64
                    origClientOrderId:
                      type: string
                      example: "1"
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      maximum: 60000
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: |-
                        Unix timestamp in milliseconds used to sign the request. The
                        value must reflect the current client time and is validated
                        by the server for signed endpoints.
                      x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
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
              id: e9d6b4349871b40611412680b3445fac
              method: order.status
              params:
                symbol: BTCUSD_PERP
                orderId: 1
                origClientOrderId: "1"
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Order
          x-description-cn: 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 0ce5d070-a5e5-4ff2-b57f-1556741a4204
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 328999071
                        format: int64
                        description: Sub-order ID
                        x-description-cn: 子订单 ID
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Trading symbol
                        x-description-cn: 交易对
                      pair:
                        type: string
                        example: BTCUSD
                        description: Pair
                        x-description-cn: 标的交易对
                      status:
                        type: string
                        example: NEW
                        description: Status.
                        x-description-cn: 订单状态
                      clientOrderId:
                        type: string
                        example: ArY8Ng1rln0s9x3fclmAHy
                        description: Client order ID.
                        x-description-cn: 客户端订单 ID.
                      price:
                        type: string
                        example: "58000"
                        description: Latest token price.
                        x-description-cn: 代币最新价格。
                      avgPrice:
                        type: string
                        example: "0.00"
                        description: Average execution price
                        x-description-cn: 平均价格
                      origQty:
                        type: string
                        example: "1"
                        description: Original order quantity
                        x-description-cn: 原始委托数量
                      executedQty:
                        type: string
                        example: "0"
                        description: Executed quantity
                        x-description-cn: 执行数量
                      cumQty:
                        type: string
                        example: "0"
                        description: Cumulative filled quantity.
                        x-description-cn: 累计成交数量.
                      cumBase:
                        type: string
                        example: "0"
                        description: Cumulative base asset amount.
                        x-description-cn: 累计基础资产数量.
                      timeInForce:
                        type: string
                        example: GTC
                        description: Time in force
                        x-description-cn: 有效方式
                      type:
                        type: string
                        example: LIMIT
                        description: Order type.
                        x-description-cn: 订单类型.
                      reduceOnly:
                        type: boolean
                        example: false
                        description: Whether the order is reduce-only.
                        x-description-cn: 是否为只减仓订单.
                      closePosition:
                        type: boolean
                        example: false
                        description: if Close-All
                        x-description-cn: 是否条件全平仓
                      side:
                        type: string
                        example: BUY
                        description: Trading side
                        x-description-cn: 买卖方向
                      positionSide:
                        type: string
                        example: LONG
                        description: Position side
                        x-description-cn: 持仓方向
                      stopPrice:
                        type: string
                        example: "0"
                        description: please ignore when order type is TRAILING_STOP_MARKET
                        x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                        description: Stop trigger price type.
                        x-description-cn: 止损触发价格类型.
                      priceProtect:
                        type: boolean
                        example: false
                        description: if conditional order trigger is protected
                        x-description-cn: 是否开启条件单触发保护
                      origType:
                        type: string
                        example: LIMIT
                        description: Original order type.
                        x-description-cn: 原始订单类型.
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_TAKER
                        description: self trading preventation mode
                        x-description-cn: 订单自成交保护模式
                      time:
                        type: integer
                        example: 1733740063619
                        format: int64
                        description: Time
                        x-description-cn: 时间
                      updateTime:
                        type: integer
                        example: 1733740063619
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                      priceMatch:
                        type: string
                        example: NONE
                        description: price match mode
                        x-description-cn: 盘口价格下单模式
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 6
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /userDataStream.stop:
    post:
      summary: Close User Data Stream (USER_STREAM)
      x-summary-cn: Websocket API关闭listenKey (USER_STREAM)
      description: Close out a user data stream.
      x-description-cn: 关闭某账户数据流
      tags:
        - user-data-streams
      operationId: closeUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
      x-ip-weight: 1
      x-security-type: USER_STREAM
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.stop
                  example: userDataStream.stop
                params:
                  type: object
                  properties:
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
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: userDataStream.stop
              params:
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Close User Data Stream
          x-description-cn: 关闭 用户 Data Stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 819e1b1b-8c06-485b-a13e-131326c69599
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties: {}
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 2
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /userDataStream.ping:
    post:
      summary: Keepalive User Data Stream (USER_STREAM)
      x-summary-cn: Websocket API延长listenKey有效期 (USER_STREAM)
      description: |-
        Keepalive a user data stream to prevent a time out. User data streams
        will close after 60 minutes. It's recommended to send a ping about every
        60 minutes.
      x-description-cn: 有效期延长至本次调用后60分钟
      tags:
        - user-data-streams
      operationId: keepaliveUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
      x-ip-weight: 1
      x-security-type: USER_STREAM
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.ping
                  example: userDataStream.ping
                params:
                  type: object
                  properties:
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
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: userDataStream.ping
              params:
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Keepalive User Data Stream
          x-description-cn: Keepalive 用户 Data Stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 815d5fce-0880-4287-a567-80badf004c74
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      listenKey:
                        type: string
                        example: 3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg
                        description: Listen key.
                        x-description-cn: 监听密钥.
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 2
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
  /userDataStream.start:
    post:
      summary: Start User Data Stream (USER_STREAM)
      x-summary-cn: Websocket API生成listenKey (USER_STREAM)
      description: |-
        Start a new user data stream. The stream will close after 60 minutes
        unless a keepalive is sent. If the account has an active `listenKey`,
        that `listenKey` will be returned and its validity will be extended for
        60 minutes.
      x-description-cn: |-
        创建一个新的user data
        stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。
      tags:
        - user-data-streams
      operationId: startUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/websocket-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/websocket_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/websocket_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/websocket/api/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/websocketapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
      x-ip-weight: 1
      x-security-type: USER_STREAM
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: e9d6b4349871b40611412680b3445fac
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - userDataStream.start
                  example: userDataStream.start
                params:
                  type: object
                  properties:
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
                    - apiKey
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: userDataStream.start
              params:
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Start User Data Stream
          x-description-cn: 开始 用户 Data Stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0
                    description: positionId
                    x-description-cn: 持仓 ID
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      listenKey:
                        type: string
                        example: xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP
                        description: Listen key.
                        x-description-cn: 监听密钥.
                    description: Indicates that combined is set to true.
                    x-description-cn: Indicates that combined is set to true.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                        interval:
                          type: string
                          example: MINUTE
                          description: Rate limit interval.
                          x-description-cn: 频率限制区间.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: Rate limit interval multiplier.
                          x-description-cn: 频率限制区间倍数.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: Maximum allowed orders for this rule.
                          x-description-cn: 该规则允许的最大订单数。
                        count:
                          type: integer
                          example: 2
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
```