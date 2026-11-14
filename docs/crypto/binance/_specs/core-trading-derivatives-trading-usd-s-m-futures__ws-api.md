---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:22.690890
---

# core-trading-derivatives-trading-usd-s-m-futures__ws-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Futures (USDⓈ-M) WebSocket API
  description: Access market data, manage accounts, and trade USDⓈ-M perpetual futures.
  x-description-cn: 访问市场数据、管理账户，并交易 USDⓈ-M 永续合约。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: ws-api
x-rate-limits-guide: products/derivatives-trading-usds-futures/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-usds-futures/general-info#访问限制
x-security-guide: products/derivatives-trading-usds-futures/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-usds-futures/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Futures (USDⓈ-M) docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-usds-futures/general-info
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 行情接口
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: user-data-streams
    x-displayName: User Data Streams
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: wss://ws-fapi.binance.com/ws-fapi/v1
  - url: wss://testnet.binancefuture.com/ws-fapi/v1
paths:
  /account.status:
    post:
      summary: Account Information (USER_DATA)
      x-summary-cn: 账户信息 (USER_DATA)
      description: >-
        Get current account information. User in single-asset/ multi-assets mode will see different value, see comments
        in response section for detail.
      x-description-cn: 现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。
      tags:
        - account
      operationId: accountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/account#account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/AccountApi/accountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/account_api/account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Account/account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/account/AccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/AccountAPI/AccountInformation/AccountInformation.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                    example: 605a6d20-6588-4cb9-afa0-b0ab087507ba
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
                        description: account commission tier
                        x-description-cn: 手续费等级
                      canTrade:
                        type: boolean
                        example: true
                        description: if can trade
                        x-description-cn: 是否可交易
                      canDeposit:
                        type: boolean
                        example: true
                        description: if can transfer in asset
                        x-description-cn: 是否可入金
                      canWithdraw:
                        type: boolean
                        example: true
                        description: if can transfer out asset
                        x-description-cn: 是否可出金
                      updateTime:
                        type: integer
                        example: 0
                        format: int64
                        description: reserved property, please ignore
                        x-description-cn: 保留字段，请忽略
                      multiAssetsMargin:
                        type: boolean
                        example: true
                      tradeGroupId:
                        type: integer
                        example: -1
                        format: int64
                      totalInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: >-
                          total initial margin required with current mark price (useless with isolated positions), only
                          for USDT asset
                        x-description-cn: >-
                          total initial margin required with current mark price (useless with isolated positions), only
                          for USDT asset
                      totalMaintMargin:
                        type: string
                        example: "0.00000000"
                        description: the sum of USD value of all cross positions maintenance margin
                        x-description-cn: 全仓持仓维持保证金总额（USD 计价）。
                      totalWalletBalance:
                        type: string
                        example: "126.72469206"
                        description: total wallet balance, only for USDT asset
                        x-description-cn: 账户总钱包余额，仅 USDT 资产。
                      totalUnrealizedProfit:
                        type: string
                        example: "0.00000000"
                        description: total unrealized profit, only for USDT asset
                        x-description-cn: 未实现盈亏总额，仅 USDT 资产。
                      totalMarginBalance:
                        type: string
                        example: "126.72469206"
                        description: total margin balance, only for USDT asset
                        x-description-cn: 保证金余额总额，仅 USDT 资产。
                      totalPositionInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: initial margin required for positions with current mark price, only for USDT asset
                        x-description-cn: initial margin required for positions with current mark price, only for USDT asset
                      totalOpenOrderInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: initial margin required for open orders with current mark price, only for USDT asset
                        x-description-cn: initial margin required for open orders with current mark price, only for USDT asset
                      totalCrossWalletBalance:
                        type: string
                        example: "126.72469206"
                        description: crossed wallet balance, only for USDT asset
                        x-description-cn: 全仓钱包余额，仅 USDT 资产。
                      totalCrossUnPnl:
                        type: string
                        example: "0.00000000"
                        description: unrealized profit of crossed positions, only for USDT asset
                        x-description-cn: 全仓持仓未实现盈亏，仅 USDT 资产。
                      availableBalance:
                        type: string
                        example: "126.72469206"
                        description: available balance, only for USDT asset
                        x-description-cn: 可用余额，仅 USDT 资产。
                      maxWithdrawAmount:
                        type: string
                        example: "126.72469206"
                        description: maximum amount for transfer out, only for USDT asset
                        x-description-cn: 最大可转出金额，仅 USDT 资产。
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: USDT
                              description: asset name
                              x-description-cn: 资产名称
                            walletBalance:
                              type: string
                              example: "23.72469206"
                              description: wallet balance
                              x-description-cn: 钱包余额
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit
                              x-description-cn: 未实现盈亏
                            marginBalance:
                              type: string
                              example: "23.72469206"
                              description: margin balance
                              x-description-cn: 保证金余额
                            maintMargin:
                              type: string
                              example: "0.00000000"
                              description: maintenance margin required
                              x-description-cn: 所需维持保证金
                            initialMargin:
                              type: string
                              example: "0.00000000"
                              description: total initial margin required with current mark price
                              x-description-cn: 当前标记价格下所需总起始保证金。
                            positionInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: initial margin required for positions with current mark price
                              x-description-cn: 当前标记价格下持仓所需起始保证金。
                            openOrderInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: initial margin required for open orders with current mark price
                              x-description-cn: 当前标记价格下挂单所需起始保证金。
                            crossWalletBalance:
                              type: string
                              example: "23.72469206"
                              description: crossed wallet balance
                              x-description-cn: 全仓钱包余额
                            crossUnPnl:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit of crossed positions
                              x-description-cn: 全仓持仓未实现盈亏
                            availableBalance:
                              type: string
                              example: "126.72469206"
                              description: available balance, only for USDT asset
                              x-description-cn: 可用余额，仅 USDT 资产。
                            maxWithdrawAmount:
                              type: string
                              example: "23.72469206"
                              description: maximum amount for transfer out, only for USDT asset
                              x-description-cn: 最大可转出金额，仅 USDT 资产。
                            marginAvailable:
                              type: boolean
                              example: true
                              description: whether the asset can be used as margin in Multi-Assets mode
                              x-description-cn: 该资产是否可在多资产模式下作为保证金。
                            updateTime:
                              type: integer
                              example: 1625474304765
                              format: int64
                              description: reserved property, please ignore
                              x-description-cn: 保留字段，请忽略
                      positions:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                              description: symbol name
                              x-description-cn: 交易对名称
                            initialMargin:
                              type: string
                              example: "0"
                              description: total initial margin required with current mark price
                              x-description-cn: 当前标记价格下所需总起始保证金。
                            maintMargin:
                              type: string
                              example: "0"
                              description: maintenance margin required
                              x-description-cn: 所需维持保证金
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit
                              x-description-cn: 未实现盈亏
                            positionInitialMargin:
                              type: string
                              example: "0"
                              description: initial margin required for positions with current mark price
                              x-description-cn: 当前标记价格下持仓所需起始保证金。
                            openOrderInitialMargin:
                              type: string
                              example: "0"
                              description: initial margin required for open orders with current mark price
                              x-description-cn: 当前标记价格下挂单所需起始保证金。
                            leverage:
                              type: string
                              example: "100"
                              description: current initial leverage
                              x-description-cn: 当前初始杠杆
                            isolated:
                              type: boolean
                              example: true
                              description: if the position is isolated
                              x-description-cn: 是否逐仓持仓
                            entryPrice:
                              type: string
                              example: "0.00000"
                              description: average entry price
                              x-description-cn: 持仓成本价
                            maxNotional:
                              type: string
                              example: "250000"
                              description: maximum available notional with current leverage
                              x-description-cn: 当前杠杆下最大可用名义价值。
                            bidNotional:
                              type: string
                              example: "0"
                              description: bids notional, ignore
                              x-description-cn: 买单名义价值（忽略）。
                            askNotional:
                              type: string
                              example: "0"
                              description: ask notional, ignore
                              x-description-cn: 卖单名义价值（忽略）。
                            positionSide:
                              type: string
                              example: BOTH
                              description: position side
                              x-description-cn: 持仓方向
                            positionAmt:
                              type: string
                              example: "0"
                              description: position amount
                              x-description-cn: 持仓数量
                            updateTime:
                              type: integer
                              example: 0
                              format: int64
                              description: reserved property, please ignore
                              x-description-cn: 保留字段，请忽略
                            breakEvenPrice:
                              type: string
                              example: "0.0"
                              description: average entry price
                              x-description-cn: 持仓成本价
                        description: positions of all symbols in the market are returned
                        x-description-cn: 返回市场中所有交易对的持仓。
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
  /v2/account.status:
    post:
      summary: Account Information V2 (USER_DATA)
      x-summary-cn: 账户信息V2 (USER_DATA)
      description: >-
        Get current account information. User in single-asset/ multi-assets mode will see different value, see comments
        in response section for detail.
      x-description-cn: 现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。
      tags:
        - account
      operationId: accountInformationV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/account#account-information-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/AccountApi/accountInformationV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/account_api/account_information_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Account/account_information_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/account/AccountInformationV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/AccountAPI/AccountInformationV2/AccountInformationV2.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - v2/account.status
                  example: v2/account.status
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
              method: v2/account.status
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Account Information V2
          x-description-cn: 账户 信息 V2
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
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      totalInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: >-
                          total initial margin required with current mark price (useless with isolated positions), only
                          for USDT asset
                        x-description-cn: >-
                          total initial margin required with current mark price (useless with isolated positions), only
                          for USDT asset
                      totalMaintMargin:
                        type: string
                        example: "0.00000000"
                        description: the sum of USD value of all cross positions maintenance margin
                        x-description-cn: 全仓持仓维持保证金总额（USD 计价）。
                      totalWalletBalance:
                        type: string
                        example: "126.72469206"
                        description: total wallet balance, only for USDT asset
                        x-description-cn: 账户总钱包余额，仅 USDT 资产。
                      totalUnrealizedProfit:
                        type: string
                        example: "0.00000000"
                        description: total unrealized profit, only for USDT asset
                        x-description-cn: 未实现盈亏总额，仅 USDT 资产。
                      totalMarginBalance:
                        type: string
                        example: "126.72469206"
                        description: total margin balance, only for USDT asset
                        x-description-cn: 保证金余额总额，仅 USDT 资产。
                      totalPositionInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: initial margin required for positions with current mark price, only for USDT asset
                        x-description-cn: initial margin required for positions with current mark price, only for USDT asset
                      totalOpenOrderInitialMargin:
                        type: string
                        example: "0.00000000"
                        description: initial margin required for open orders with current mark price, only for USDT asset
                        x-description-cn: initial margin required for open orders with current mark price, only for USDT asset
                      totalCrossWalletBalance:
                        type: string
                        example: "126.72469206"
                        description: crossed wallet balance, only for USDT asset
                        x-description-cn: 全仓钱包余额，仅 USDT 资产。
                      totalCrossUnPnl:
                        type: string
                        example: "0.00000000"
                        description: unrealized profit of crossed positions, only for USDT asset
                        x-description-cn: 全仓持仓未实现盈亏，仅 USDT 资产。
                      availableBalance:
                        type: string
                        example: "126.72469206"
                        description: available balance, only for USDT asset
                        x-description-cn: 可用余额，仅 USDT 资产。
                      maxWithdrawAmount:
                        type: string
                        example: "126.72469206"
                        description: maximum amount for transfer out, only for USDT asset
                        x-description-cn: 最大可转出金额，仅 USDT 资产。
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: USDT
                              description: asset name
                              x-description-cn: 资产名称
                            walletBalance:
                              type: string
                              example: "23.72469206"
                              description: wallet balance
                              x-description-cn: 钱包余额
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit
                              x-description-cn: 未实现盈亏
                            marginBalance:
                              type: string
                              example: "23.72469206"
                              description: margin balance
                              x-description-cn: 保证金余额
                            maintMargin:
                              type: string
                              example: "0.00000000"
                              description: maintenance margin required
                              x-description-cn: 所需维持保证金
                            initialMargin:
                              type: string
                              example: "0.00000000"
                              description: total initial margin required with current mark price
                              x-description-cn: 当前标记价格下所需总起始保证金。
                            positionInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: initial margin required for positions with current mark price
                              x-description-cn: 当前标记价格下持仓所需起始保证金。
                            openOrderInitialMargin:
                              type: string
                              example: "0.00000000"
                              description: initial margin required for open orders with current mark price
                              x-description-cn: 当前标记价格下挂单所需起始保证金。
                            crossWalletBalance:
                              type: string
                              example: "23.72469206"
                              description: crossed wallet balance
                              x-description-cn: 全仓钱包余额
                            crossUnPnl:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit of crossed positions
                              x-description-cn: 全仓持仓未实现盈亏
                            availableBalance:
                              type: string
                              example: "23.72469206"
                              description: available balance, only for USDT asset
                              x-description-cn: 可用余额，仅 USDT 资产。
                            maxWithdrawAmount:
                              type: string
                              example: "23.72469206"
                              description: maximum amount for transfer out, only for USDT asset
                              x-description-cn: 最大可转出金额，仅 USDT 资产。
                            marginAvailable:
                              type: boolean
                              example: true
                              description: whether the asset can be used as margin in Multi-Assets mode
                              x-description-cn: 该资产是否可在多资产模式下作为保证金。
                            updateTime:
                              type: integer
                              example: 1625474304765
                              format: int64
                              description: last update time
                              x-description-cn: 最后更新时间
                        description: For assets that are quote assets, USDT/USDC/BTC
                        x-description-cn: 报价资产列表（USDT/USDC/BTC）。
                      positions:
                        type: array
                        items:
                          type: object
                          properties:
                            symbol:
                              type: string
                              example: BTCUSDT
                            positionSide:
                              type: string
                              example: BOTH
                              description: position side
                              x-description-cn: 持仓方向
                            positionAmt:
                              type: string
                              example: "1.000"
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                              description: unrealized profit
                              x-description-cn: 未实现盈亏
                            isolatedMargin:
                              type: string
                              example: "0.00000000"
                            notional:
                              type: string
                              example: "0"
                            isolatedWallet:
                              type: string
                              example: "0"
                            initialMargin:
                              type: string
                              example: "0"
                              description: total initial margin required with current mark price
                              x-description-cn: 当前标记价格下所需总起始保证金。
                            maintMargin:
                              type: string
                              example: "0"
                              description: maintenance margin required
                              x-description-cn: 所需维持保证金
                            updateTime:
                              type: integer
                              example: 0
                              format: int64
                              description: last update time
                              x-description-cn: 最后更新时间
                        description: positions of all symbols user had position/ open orders are returned
                        x-description-cn: 返回用户有持仓或有挂单的所有交易对持仓。
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/account#futures-account-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/AccountApi/futuresAccountBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/account_api/futures_account_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Account/futures_account_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/account/FuturesAccountBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/AccountAPI/FuturesAccountBalance/FuturesAccountBalance.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
          x-description-cn: 合约账户余额
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
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        accountAlias:
                          type: string
                          example: SgsR
                          description: unique account code
                          x-description-cn: 唯一账户标识
                        asset:
                          type: string
                          example: USDT
                          description: asset name
                          x-description-cn: 资产名称
                        balance:
                          type: string
                          example: "122607.35137903"
                          description: wallet balance
                          x-description-cn: 钱包余额
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: crossed wallet balance
                          x-description-cn: 全仓钱包余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit of crossed positions
                          x-description-cn: 全仓持仓未实现盈亏
                        availableBalance:
                          type: string
                          example: "23.72469206"
                          description: available balance
                          x-description-cn: 可用余额
                        maxWithdrawAmount:
                          type: string
                          example: "23.72469206"
                          description: maximum amount for transfer out
                          x-description-cn: 最大可转出金额
                        marginAvailable:
                          type: boolean
                          example: true
                          description: whether the asset can be used as margin in Multi-Assets mode
                          x-description-cn: 该资产是否可在多资产模式下作为保证金。
                        updateTime:
                          type: integer
                          example: 1617939110373
                          format: int64
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
  /v2/account.balance:
    post:
      summary: Futures Account Balance V2 (USER_DATA)
      x-summary-cn: 账户余额V2 (USER_DATA)
      description: Futures Account Balance V2
      x-description-cn: 账户余额V2
      tags:
        - account
      operationId: futuresAccountBalanceV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/account#futures-account-balance-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/AccountApi/futuresAccountBalanceV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/account_api/futures_account_balance_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Account/futures_account_balance_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/account/FuturesAccountBalanceV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/AccountAPI/FuturesAccountBalanceV2/FuturesAccountBalanceV2.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - v2/account.balance
                  example: v2/account.balance
                params:
                  type: object
                  properties:
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
              method: v2/account.balance
              params:
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Futures Account Balance V2
          x-description-cn: 合约账户余额 V2
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
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        accountAlias:
                          type: string
                          example: SgsR
                          description: unique account code
                          x-description-cn: 唯一账户标识
                        asset:
                          type: string
                          example: USDT
                          description: asset name
                          x-description-cn: 资产名称
                        balance:
                          type: string
                          example: "122607.35137903"
                          description: wallet balance
                          x-description-cn: 钱包余额
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: crossed wallet balance
                          x-description-cn: 全仓钱包余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit of crossed positions
                          x-description-cn: 全仓持仓未实现盈亏
                        availableBalance:
                          type: string
                          example: "23.72469206"
                          description: available balance
                          x-description-cn: 可用余额
                        maxWithdrawAmount:
                          type: string
                          example: "23.72469206"
                          description: maximum amount for transfer out
                          x-description-cn: 最大可转出金额
                        marginAvailable:
                          type: boolean
                          example: true
                          description: whether the asset can be used as margin in Multi-Assets mode
                          x-description-cn: 该资产是否可在多资产模式下作为保证金。
                        updateTime:
                          type: integer
                          example: 1617939110373
                          format: int64
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
  /depth:
    post:
      summary: Order Book
      x-summary-cn: 深度信息
      description: |-
        Get current order book. Note that this request returns limited market
        depth.

        If you need to continuously monitor order book updates, please consider
        using Websocket Market Streams:
          * `<symbol>@depth<levels>`
          * `<symbol>@depth`

        You can use `depth` request together with `<symbol>@depth` streams to
        maintain a local order book.

        **Note:**

        - Retail Price Improvement(RPI) orders are not visible and excluded in
        the response message.
      x-description-cn: |-
        获取当前订单簿。请注意，此请求返回有限的市场深度。
        如果您需要持续监控订单簿更新，请考虑使用Websocket市场流：
          * `<symbol>@depth<levels>`
          * `<symbol>@depth`

        您可以将`depth`请求与`<symbol>@depth`流一起使用以维护本地订单簿。
        **注意：**
        - 零点价订单在响应消息中不可见且被排除在外。
      tags:
        - market-data
      operationId: orderBook
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/market-data#order-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/MarketDataApi/orderBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/market_data_api/order_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/MarketData/order_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/marketdata/OrderBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/MarketDataAPI/OrderBook/OrderBook.go
      x-weight: |-
        Adjusted based on the limit:

        | Limit         | Weight |
        | ------------- | ------ |
        | 5, 10, 20, 50 | 2      |
        | 100           | 5      |
        | 500           | 10     |
        | 1000          | 20     |
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    limit:
                      type: integer
                      example: 10
                      default: 500
                      maximum: 1000
                      description: Valid limits:[5, 10, 20, 50, 100, 500, 1000]
                      x-description-cn: 有效限制：[5, 10, 20, 50, 100, 500, 1000]
                      format: int64
                  additionalProperties: false
                  required:
                    - symbol
              required:
                - id
                - method
                - params
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: depth
              params:
                symbol: BTCUSDT
                limit: 10
      responses:
        Successful Response:
          description: Order Book
          x-description-cn: 订单簿
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
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      lastUpdateId:
                        type: integer
                        example: 1027024
                        format: int64
                      E:
                        type: integer
                        example: 1589436922972
                        format: int64
                        description: Message output time
                        x-description-cn: 消息输出时间
                      T:
                        type: integer
                        example: 1589436922959
                        format: int64
                        description: Transaction time
                        x-description-cn: 成交时间
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
                          example: "4.00000000"
                        - type: string
                          description: Quantity
                          example: "431.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "4.00000000"
                          - type: string
                            description: Quantity
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
                          example: "4.00000200"
                        - type: string
                          description: Quantity
                          example: "12.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "4.00000200"
                          - type: string
                            description: Quantity
                            example: "12.00000000"
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 5
                          format: int64
  /ticker.book:
    post:
      summary: Symbol Order Book Ticker
      x-summary-cn: 当前最优挂单
      description: |-
        Best price/qty on the order book for a symbol or symbols.

        **Note:**

        - Retail Price Improvement(RPI) orders are not visible and excluded in
        the response message.
      x-description-cn: |-
        交易对订单簿最优挂单价格和数量。
        **注意：**
        - 零售价格改进（RPI）订单在响应消息中不可见且被排除在外。
      tags:
        - market-data
      operationId: symbolOrderBookTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/market-data#symbol-order-book-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/MarketDataApi/symbolOrderBookTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/market_data_api/symbol_order_book_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/MarketData/symbol_order_book_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/marketdata/SymbolOrderBookTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/MarketDataAPI/SymbolOrderBookTicker/SymbolOrderBookTicker.go
      x-weight: |-
        **2** for a single symbol;
        **5** when the symbol parameter is omitted
      x-parameters-notes: |-
        - If the symbol is not sent, bookTickers for all symbols will be
        returned in an array.

        - The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate
        from this endpoint, please ignore.
      x-parameters-notes-cn: |-
        - 如果未发送symbol，则将返回所有symbol的bookTickers数组。

        - 此端点响应头中的字段`X-MBX-USED-WEIGHT-1M`不准确，请忽略。
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: ticker.book
              params:
                symbol: BTCUSDT
      responses:
        Successful Response:
          description: Symbol Order Book Ticker
          x-description-cn: 交易对 订单 最优挂单
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
                        example: 200
                        format: int64
                      result:
                        type: object
                        properties:
                          lastUpdateId:
                            type: integer
                            example: 1027024
                            format: int64
                          symbol:
                            type: string
                            example: BTCUSDT
                          bidPrice:
                            type: string
                            example: "4.00000000"
                          bidQty:
                            type: string
                            example: "431.00000000"
                          askPrice:
                            type: string
                            example: "4.00000200"
                          askQty:
                            type: string
                            example: "9.00000000"
                          time:
                            type: integer
                            example: 1589437530011
                            format: int64
                            description: Transaction time
                            x-description-cn: 成交时间
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
                              format: int64
                            limit:
                              type: integer
                              example: 2400
                              format: int64
                            count:
                              type: integer
                              example: 2
                              format: int64
                  - type: object
                    properties:
                      id:
                        type: string
                        example: 9d32157c-a556-4d27-9866-66760a174b57
                      status:
                        type: integer
                        example: 200
                        format: int64
                      result:
                        type: array
                        items:
                          type: object
                          properties:
                            lastUpdateId:
                              type: integer
                              example: 1027024
                              format: int64
                            symbol:
                              type: string
                              example: BTCUSDT
                            bidPrice:
                              type: string
                              example: "4.00000000"
                            bidQty:
                              type: string
                              example: "431.00000000"
                            askPrice:
                              type: string
                              example: "4.00000200"
                            askQty:
                              type: string
                              example: "9.00000000"
                            time:
                              type: integer
                              example: 1589437530011
                              format: int64
                              description: Transaction time
                              x-description-cn: 成交时间
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
                              format: int64
                            limit:
                              type: integer
                              example: 2400
                              format: int64
                            count:
                              type: integer
                              example: 2
                              format: int64
  /ticker.price:
    post:
      summary: Symbol Price Ticker
      x-summary-cn: 最新价格
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回最近价格
      tags:
        - market-data
      operationId: symbolPriceTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/market-data#symbol-price-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/MarketDataApi/symbolPriceTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/market_data_api/symbol_price_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/MarketData/symbol_price_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/marketdata/SymbolPriceTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/MarketDataAPI/SymbolPriceTicker/SymbolPriceTicker.go
      x-weight: |-
        **1** for a single symbol;
        **2** when the symbol parameter is omitted
      x-parameters-notes: "- If the symbol is not sent, prices for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 如果未发送symbol，则将返回所有symbol的价格数组。"
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                  additionalProperties: false
              required:
                - id
                - method
              additionalProperties: false
            example:
              id: e9d6b4349871b40611412680b3445fac
              method: ticker.price
              params:
                symbol: BTCUSDT
      responses:
        Successful Response:
          description: Symbol Price Ticker
          x-description-cn: 交易对 价格 行情
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
                        example: 200
                        format: int64
                      result:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                          price:
                            type: string
                            example: "6000.01"
                          time:
                            type: integer
                            example: 1589437530011
                            format: int64
                            description: Transaction time
                            x-description-cn: 成交时间
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
                              format: int64
                            limit:
                              type: integer
                              example: 2400
                              format: int64
                            count:
                              type: integer
                              example: 2
                              format: int64
                  - type: object
                    properties:
                      id:
                        type: string
                        example: 9d32157c-a556-4d27-9866-66760a174b57
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
                              example: BTCUSDT
                            price:
                              type: string
                              example: "6000.01"
                            time:
                              type: integer
                              example: 1589437530011
                              format: int64
                              description: Transaction time
                              x-description-cn: 成交时间
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
                              format: int64
                            limit:
                              type: integer
                              example: 2400
                              format: int64
                            count:
                              type: integer
                              example: 2
                              format: int64
  /algoOrder.cancel:
    post:
      summary: Cancel Algo Order (TRADE)
      x-summary-cn: 条件单撤销订单 (TRADE)
      description: Cancel an active algo order.
      x-description-cn: 撤销条件订单
      tags:
        - trade
      operationId: cancelAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#cancel-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/cancelAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/cancel_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/cancel_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/CancelAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/CancelAlgoOrder/CancelAlgoOrder.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "- Either `algoId` or `clientAlgoId` must be sent."
      x-parameters-notes-cn: "- `algoId`或`clientAlgoId`必须发送其中一个。"
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
                  description: Id.
                  x-description-cn: 请求 ID。
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - algoOrder.cancel
                  example: algoOrder.cancel
                params:
                  type: object
                  properties:
                    algoId:
                      type: integer
                      example: 2000000002162519
                      format: int64
                      description: Algo Id.
                      x-description-cn: 条件单 ID。
                    clientAlgoId:
                      type: string
                      example: rDMG8WSde6LkyMNtk6s825
                      description: Client Algo Id.
                      x-description-cn: 自定义条件单 ID。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
              method: algoOrder.cancel
              params:
                algoId: 2000000002162519
                clientAlgoId: rDMG8WSde6LkyMNtk6s825
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Cancel Algo Order
          x-description-cn: 取消Algo 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: unique-cancel-request-id-5678
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      algoId:
                        type: integer
                        example: 2000000002162519
                        format: int64
                      clientAlgoId:
                        type: string
                        example: rDMG8WSde6LkyMNtk6s825
                      code:
                        type: string
                        example: "200"
                      msg:
                        type: string
                        example: success
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 6
                          format: int64
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#cancel-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/cancelOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/cancel_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/cancel_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/CancelOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/CancelOrder/CancelOrder.go
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId`或`origClientOrderId`必须发送其中一个。"
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    orderId:
                      type: integer
                      example: 1
                      format: int64
                      description: Order Id.
                      x-description-cn: 系统订单号。
                    origClientOrderId:
                      type: string
                      example: "1"
                      description: Orig Client Order Id.
                      x-description-cn: 原客户端订单号。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                symbol: BTCUSDT
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
                    example: 5633b6a2-90a9-4192-83e7-925c90b6a2fd
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      clientOrderId:
                        type: string
                        example: myOrder1
                      cumQty:
                        type: string
                        example: "0"
                      executedQty:
                        type: string
                        example: "0"
                      orderId:
                        type: integer
                        example: 283194212
                        format: int64
                      origQty:
                        type: string
                        example: "11"
                      origType:
                        type: string
                        example: TRAILING_STOP_MARKET
                      price:
                        type: string
                        example: "0"
                      reduceOnly:
                        type: boolean
                        example: false
                      side:
                        type: string
                        example: BUY
                      positionSide:
                        type: string
                        example: SHORT
                      status:
                        type: string
                        example: CANCELED
                      stopPrice:
                        type: string
                        example: "9300"
                      closePosition:
                        type: boolean
                        example: false
                      symbol:
                        type: string
                        example: BTCUSDT
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: TRAILING_STOP_MARKET
                      activatePrice:
                        type: string
                        example: "9020"
                      priceRate:
                        type: string
                        example: "0.3"
                      updateTime:
                        type: integer
                        example: 1571110484038
                        format: int64
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                      priceProtect:
                        type: boolean
                        example: false
                      priceMatch:
                        type: string
                        example: NONE
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_MAKER
                      goodTillDate:
                        type: integer
                        example: 0
                        format: int64
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 1
                          format: int64
  /order.modify:
    post:
      summary: Modify Order (TRADE)
      x-summary-cn: 修改订单 (TRADE)
      description: >-
        Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered
        in the match queue
      x-description-cn: 修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序
      tags:
        - trade
      operationId: modifyOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#modify-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/modifyOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/modify_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/modify_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/ModifyOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/ModifyOrder/ModifyOrder.go
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
        0 on IP rate limit(x-mbx-used-weight-1m)
      x-parameters-notes: >-
        - Either `orderId` or `origClientOrderId` must be sent, and the

        `orderId` will prevail if both are sent.


        - Both `quantity` and `price` must be sent. *(After CM migration, the dapi modify order endpoint follows the
        same rule.)*


        - When the new `quantity` or `price` doesn't satisfy PRICE_FILTER /

        PERCENT_FILTER / LOT_SIZE, amendment will be rejected and the order will

        stay as it is.


        - However the order will be cancelled by the amendment in the following

        situations:


        - when the order is in partially filled status and the new `quantity` <=

        `executedQty`


        - When the order is `GTX` and the new price will cause it to be executed

        immediately


        - One order can only be modfied for less than 10000 times


        - `reduceOnly` behavior:
          - `false` or omitted: behave as today — `min_notional` is enforced on the modified order.
          - `true` and the original order's `reduceOnly` attribute is also `true` (consistent): the `min_notional` check is skipped on the modified order, matching placement semantics.
          - `true` but the original order's `reduceOnly` attribute is `false` (inconsistent): the modify request is rejected with error code `-5047`, "The original order is not a reduce-only order".
          - `reduceOnly` is used purely for validation — passing `true` does not change the original order's `reduceOnly` attribute; that flag remains whatever it was set to at placement time.
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 必须至少传一个，若同时传入则以
        `orderId` 为准。

        - `quantity` 和 `price` 必须同时传入。*(迁移后,dapi 修改订单接口同样要求两者必传。)*

        - 当新的 `quantity` 或 `price` 不满足 PRICE_FILTER / PERCENT_FILTER /
        LOT_SIZE 时，修改将被拒绝，原订单保持不变。

        - 在以下场景中，本次修改会导致订单被取消：
          - 订单已部分成交且新 `quantity` <= `executedQty`
          - 订单类型为 `GTX` 且新价格会立即成交

        - 同一订单最多可修改 10000 次。

        - `reduceOnly` 行为说明：
          - `false` 或不传：与当前行为一致——对修改后的订单执行 `min_notional` 校验。
          - `true` 且原订单的 `reduceOnly` 属性也为 `true`（一致）：跳过修改后订单的 `min_notional` 校验，与下单语义对齐。
          - `true` 但原订单的 `reduceOnly` 属性为 `false`（不一致）：拒绝本次改单请求，返回错误码 `-5047`，"The original order is not a reduce-only order"。
          - `reduceOnly` 仅用于校验——传 `true` 不会改变原订单的 `reduceOnly` 属性，该属性仍保持下单时设定的值。
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      description: Order Id.
                      x-description-cn: 系统订单号。
                    origClientOrderId:
                      type: string
                      example: "1"
                      description: Orig Client Order Id.
                      x-description-cn: 原客户端订单号。
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    side:
                      type: string
                      example: BUY
                      enum:
                        - BUY
                        - SELL
                      description: "`SELL`, `BUY`"
                      x-description-cn: "`SELL`、`BUY`"
                    quantity:
                      type: number
                      example: "1.0"
                      format: float
                      description: Order quantity, cannot be sent with `closePosition=true`
                      x-description-cn: 下单数量，不可与 `closePosition=true` 同时传。
                    price:
                      type: number
                      example: "1.0"
                      format: float
                      description: Price.
                      x-description-cn: 价格。
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
                      description: only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price
                      x-description-cn: only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price
                    modifyId:
                      type: integer
                      example: 1
                      format: int64
                      description: >-
                        User-defined modification identifier, returned as-is in the response. Optional; not validated
                        for uniqueness.
                      x-description-cn: 用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。
                    reduceOnly:
                      type: string
                      example: "false"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: See notes below for behavior.
                      x-description-cn: 行为说明见下方备注。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                symbol: BTCUSDT
                side: BUY
                quantity: "1.0"
                price: "1.0"
                priceMatch: OPPONENT
                modifyId: 1
                reduceOnly: "false"
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Modify Order
          x-description-cn: 修改订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: c8c271ba-de70-479e-870c-e64951c753d9
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 328971409
                        format: int64
                      symbol:
                        type: string
                        example: BTCUSDT
                      status:
                        type: string
                        example: NEW
                      clientOrderId:
                        type: string
                        example: xGHfltUMExx0TbQstQQfRX
                      modifyId:
                        type: integer
                        example: 1
                        format: int64
                        description: user-defined modification identifier, only returned if provided in the request
                        x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                      price:
                        type: string
                        example: "43769.10"
                      origQty:
                        type: string
                        example: "0.110"
                      executedQty:
                        type: string
                        example: "0.000"
                      cumQty:
                        type: string
                        example: "0.000"
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: LIMIT
                      reduceOnly:
                        type: boolean
                        example: false
                      closePosition:
                        type: boolean
                        example: false
                      side:
                        type: string
                        example: SELL
                      positionSide:
                        type: string
                        example: SHORT
                      stopPrice:
                        type: string
                        example: "0.00"
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                      priceProtect:
                        type: boolean
                        example: false
                      origType:
                        type: string
                        example: LIMIT
                      priceMatch:
                        type: string
                        example: NONE
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_MAKER
                      goodTillDate:
                        type: integer
                        example: 0
                        format: int64
                      updateTime:
                        type: integer
                        example: 1703426756190
                        format: int64
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
                          example: 10
                          format: int64
                        limit:
                          type: integer
                          example: 300
                          format: int64
                        count:
                          type: integer
                          example: 1
                          format: int64
  /algoOrder.place:
    post:
      summary: New Algo Order (TRADE)
      x-summary-cn: 条件单下单 (TRADE)
      description: Send in a new algo order.
      x-description-cn: 条件单下单
      tags:
        - trade
      operationId: newAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#new-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/newAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/new_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/new_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/NewAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/NewAlgoOrder/NewAlgoOrder.go
      x-ip-weight: 0
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: |-
        - Condition orders will be triggered when:

        >

        - If parameter`priceProtect`is sent as true:

        - when price reaches the `triggerPrice` ，the difference rate between
        "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the
        "triggerProtect" of the symbol

        - "triggerProtect" of a symbol can be got from `GET
        /fapi/v1/exchangeInfo`

        >

        - `STOP`, `STOP_MARKET`:

        - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `triggerPrice`

        - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <=
        `triggerPrice`

        - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`:

        - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `triggerPrice`

        - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >=
        `triggerPrice`

        - `TRAILING_STOP_MARKET`:

        - BUY: the lowest price after order placed <= `activatePrice`, and the
        latest price >= the lowest price * (1 + `callbackRate`)

        - SELL: the highest price after order placed >= `activatePrice`, and the
        latest price <= the highest price * (1 - `callbackRate`)

        >

        - For `TRAILING_STOP_MARKET`, if you got such error code.

        >   ``{"code": -2021, "msg": "Order would immediately trigger."}``

        >   means that the parameters you send do not meet the following
        requirements:

        - BUY: `activatePrice` should be smaller than latest price.

        - SELL: `activatePrice` should be larger than latest price.

        >

        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:

        - Follow the same rules for condition orders.

        - If triggered，**close all** current long position( if `SELL`) or
        current short position( if `BUY`).

        - Cannot be used with `quantity` paremeter

        - Cannot be used with `reduceOnly` parameter

        - In Hedge Mode,cannot be used with `BUY` orders in `LONG` position
        side. and cannot be used with `SELL` orders in `SHORT` position side

        - `selfTradePreventionMode` is only effective when `timeInForce` set to
        `IOC` or `GTC` or `GTD`.
      x-parameters-notes-cn: |-
        - 条件单触发规则：
          - 若 `priceProtect=true`，当价格到达 `triggerPrice` 时，`MARK_PRICE`
            与 `CONTRACT_PRICE` 的价差不能超过该交易对的 `triggerProtect`。
          - `STOP` / `STOP_MARKET`：
            - BUY：最新价 >= `triggerPrice`
            - SELL：最新价 <= `triggerPrice`
          - `TAKE_PROFIT` / `TAKE_PROFIT_MARKET`：
            - BUY：最新价 <= `triggerPrice`
            - SELL：最新价 >= `triggerPrice`
          - `TRAILING_STOP_MARKET`：
            - BUY：最低价 <= `activatePrice` 且最新价 >= 最低价 * (1 + `callbackRate`)
            - SELL：最高价 >= `activatePrice` 且最新价 <= 最高价 * (1 - `callbackRate`)

        - 若 `TRAILING_STOP_MARKET` 返回 `{"code": -2021, "msg": "Order would immediately trigger."}`：
          - BUY：`activatePrice` 必须小于最新价
          - SELL：`activatePrice` 必须大于最新价

        - `STOP_MARKET` / `TAKE_PROFIT_MARKET` 且 `closePosition=true`：
          - 触发后全平当前方向仓位
          - 不可与 `quantity` 同时使用
          - 不可与 `reduceOnly` 同时使用
          - 双向持仓模式下，`LONG` 不支持 `BUY`，`SHORT` 不支持 `SELL`

        - `selfTradePreventionMode` 仅在 `timeInForce` 为 `IOC`、`GTC` 或 `GTD` 时生效。
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
                  description: Id.
                  x-description-cn: 请求 ID。
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - algoOrder.place
                  example: algoOrder.place
                params:
                  type: object
                  properties:
                    algoType:
                      type: string
                      example: CONDITIONAL
                      enum:
                        - CONDITIONAL
                      description: Only support `CONDITIONAL`
                      x-description-cn: 仅支持 `CONDITIONAL`。
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    side:
                      type: string
                      example: BUY
                      enum:
                        - BUY
                        - SELL
                      description: Side.
                      x-description-cn: 买卖方向。
                    positionSide:
                      type: string
                      example: BOTH
                      enum:
                        - BOTH
                        - LONG
                        - SHORT
                      description: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
                      x-description-cn: 单向模式默认 `BOTH`；双向模式可为 `LONG` 或 `SHORT`，双向模式必传。
                    type:
                      type: string
                      example: STOP_MARKET
                      enum:
                        - STOP_MARKET
                        - TAKE_PROFIT_MARKET
                        - STOP
                        - TAKE_PROFIT
                        - TRAILING_STOP_MARKET
                      description: >-
                        For `CONDITIONAL` algoType,
                        `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET` as order type
                      x-description-cn: >-
                        当 algoType=`CONDITIONAL` 时，订单类型可为
                        `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET` 之一。
                    timeInForce:
                      type: string
                      example: GTC
                      enum:
                        - IOC
                        - GTC
                        - FOK
                      description: "`IOC` or `GTC` or `FOK`, default `GTC`"
                      x-description-cn: "`IOC`、`GTC` 或 `FOK`，默认 `GTC`。"
                    quantity:
                      type: number
                      example: "1.0"
                      format: float
                      description: Cannot be sent with `closePosition`=`true`(Close-All)
                      x-description-cn: 不可与 `closePosition=true`（全平）同时传。
                    price:
                      type: number
                      example: "1.0"
                      format: float
                      description: Price.
                      x-description-cn: 价格。
                    triggerPrice:
                      type: number
                      example: "1.0"
                      format: float
                      description: Trigger Price.
                      x-description-cn: 触发价格。
                    workingType:
                      type: string
                      example: MARK_PRICE
                      default: CONTRACT_PRICE
                      enum:
                        - MARK_PRICE
                        - CONTRACT_PRICE
                      description: "triggerPrice triggered by: `MARK_PRICE`, `CONTRACT_PRICE`. Default `CONTRACT_PRICE`"
                      x-description-cn: 触发价格类型：`MARK_PRICE` 或 `CONTRACT_PRICE`，默认 `CONTRACT_PRICE`。
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
                      description: only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price
                      x-description-cn: 仅适用于 LIMIT/STOP/TAKE_PROFIT；不可与 price 同时传。
                    closePosition:
                      type: string
                      example: "true"
                      enum:
                        - "true"
                        - "false"
                      description: Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
                      x-description-cn: 全平，仅用于 `STOP_MARKET` 或 `TAKE_PROFIT_MARKET`。
                    priceProtect:
                      type: string
                      example: "true"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: >-
                        Used with STOP_MARKET or TAKE_PROFIT_MARKET order. when price reaches the triggerPrice ，the
                        difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price
                        Protection Threshold of the symbol.
                      x-description-cn: >-
                        用于 STOP_MARKET 或 TAKE_PROFIT_MARKET；当价格触达 triggerPrice 时，MARK_PRICE 与 CONTRACT_PRICE
                        的价差比例不得超过该交易对的价格保护阈值。
                    reduceOnly:
                      type: string
                      example: "true"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
                      x-description-cn: 双向持仓模式不可传；不可与 closePosition=true 同时传。
                    activatePrice:
                      type: number
                      example: "1.0"
                      format: float
                      description: >-
                        Used with TRAILING_STOP_MARKET orders, default as the latest price(supporting different
                        workingType)
                      x-description-cn: 仅用于 TRAILING_STOP_MARKET，默认使用最新价（支持不同 workingType）。
                    callbackRate:
                      type: number
                      example: 1
                      format: float
                      minimum: 0.1
                      maximum: 20
                      description: Used with TRAILING_STOP_MARKET orders
                      x-description-cn: 仅用于 `TRAILING_STOP_MARKET`。
                    clientAlgoId:
                      type: string
                      example: "1"
                      description: >-
                        A unique id among open orders. Automatically generated if not sent. Can only be string following
                        the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                      x-description-cn: 挂单中的唯一客户端订单 ID；未传则自动生成。仅支持匹配 `^[\\.A-Z\\:/a-z0-9_-]{1,36}$` 的字符串。
                    newOrderRespType:
                      type: string
                      example: ACK
                      enum:
                        - ACK
                        - RESULT
                      description: '"ACK", "RESULT", default "ACK"'
                      x-description-cn: "`ACK` 或 `RESULT`，默认 `ACK`。"
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_TAKER
                      enum:
                        - NONE
                        - EXPIRE_TAKER
                        - EXPIRE_BOTH
                        - EXPIRE_MAKER
                      description: >-
                        `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when
                        STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`
                      x-description-cn: "`EXPIRE_TAKER`（触发时撤吃单）/ `EXPIRE_MAKER`（触发时撤挂单）/ `EXPIRE_BOTH`（触发时两边都撤）；默认 `NONE`"
                    goodTillDate:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                        timestamp only retains second-level precision, ms part will be ignored; The goodTillDate
                        timestamp must be greater than the current time plus 600 seconds and smaller than
                        253402300799000
                      x-description-cn: |-
                        `timeInForce=GTD` 时的撤单时间（必传）；仅保留秒级精度（毫秒会被忽略）；必须大于当前时间+600秒且小于
                        253402300799000。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                    - algoType
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
              method: algoOrder.place
              params:
                algoType: CONDITIONAL
                symbol: BTCUSDT
                side: BUY
                positionSide: BOTH
                type: STOP_MARKET
                timeInForce: GTC
                quantity: "1.0"
                price: "1.0"
                triggerPrice: "1.0"
                workingType: MARK_PRICE
                priceMatch: OPPONENT
                closePosition: "true"
                priceProtect: "true"
                reduceOnly: "true"
                activatePrice: "1.0"
                callbackRate: 1
                clientAlgoId: "1"
                newOrderRespType: ACK
                selfTradePreventionMode: EXPIRE_TAKER
                goodTillDate: 1770736694138
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: New Algo Order
          x-description-cn: 下单（算法单）
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 06c9dbd8-ccbf-4ecf-a29c-fe31495ac73f
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      algoId:
                        type: integer
                        example: 3000000000003505
                        format: int64
                      clientAlgoId:
                        type: string
                        example: 0Xkl1p621E4EryvufmYre1
                      algoType:
                        type: string
                        example: CONDITIONAL
                      orderType:
                        type: string
                        example: TAKE_PROFIT
                      symbol:
                        type: string
                        example: BTCUSDT
                      side:
                        type: string
                        example: SELL
                      positionSide:
                        type: string
                        example: SHORT
                      timeInForce:
                        type: string
                        example: GTC
                      quantity:
                        type: string
                        example: "1.000"
                      algoStatus:
                        type: string
                        example: NEW
                      triggerPrice:
                        type: string
                        example: "120000.00"
                      price:
                        type: string
                        example: "160000.00"
                      icebergQuantity:
                        type: string
                        example: "null"
                        description: Reserved field, ignore.
                        x-description-cn: 预留字段，请忽略。
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_MAKER
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                      priceMatch:
                        type: string
                        example: NONE
                      closePosition:
                        type: boolean
                        example: false
                      priceProtect:
                        type: boolean
                        example: false
                      reduceOnly:
                        type: boolean
                        example: false
                      createTime:
                        type: integer
                        example: 1762507264142
                        format: int64
                      updateTime:
                        type: integer
                        example: 1762507264143
                        format: int64
                      triggerTime:
                        type: integer
                        example: 0
                        format: int64
                      goodTillDate:
                        type: integer
                        example: 0
                        format: int64
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 1
                          format: int64
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/NewOrder/NewOrder.go
      x-ip-weight: 0
      x-security-type: TRADE
      x-signed: true
      x-parameters-notes: >-
        Additional mandatory parameters based on `type`:


        - `LIMIT`: `timeInForce`, `quantity`, `price`

        - `MARKET`: `quantity`


        > * If `newOrderRespType` is sent as `RESULT`:

        >   * `MARKET` order: the final FILLED result of the order will be return directly.

        >   * `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be
        returned directly.

        >

        > * `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.

        > * In extreme market conditions, timeInForce `GTD` order auto cancel time might be delayed comparing to
        `goodTillDate`
      x-parameters-notes-cn: |-
        根据 `type` 不同，部分参数为必填：
        - `LIMIT`：`timeInForce`、`quantity`、`price`
        - `MARKET`：`quantity`

        > * `newOrderRespType` 如果传 `RESULT`：
        >   * `MARKET` 订单将直接返回成交结果；
        >   * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
        >
        > * `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
        > * 极端行情时，`timeInForce`为`GTD`的订单自动取消可能有一定延迟
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    side:
                      type: string
                      example: BUY
                      enum:
                        - BUY
                        - SELL
                      description: Side.
                      x-description-cn: 买卖方向。
                    positionSide:
                      type: string
                      example: BOTH
                      enum:
                        - BOTH
                        - LONG
                        - SHORT
                      description: >-
                        Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge
                        Mode.
                      x-description-cn: >-
                        Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge
                        Mode.
                    type:
                      type: string
                      example: LIMIT
                      enum:
                        - LIMIT
                        - MARKET
                    timeInForce:
                      type: string
                      example: GTC
                      enum:
                        - GTC
                        - IOC
                        - FOK
                        - GTX
                        - GTD
                        - RPI
                      description: Time In Force.
                      x-description-cn: 有效方式。
                    reduceOnly:
                      type: string
                      example: "false"
                      default: "false"
                      enum:
                        - "true"
                        - "false"
                      description: Cannot be sent in Hedge Mode
                      x-description-cn: 双向持仓模式下不可传。
                    quantity:
                      type: number
                      example: "1.0"
                      format: float
                    price:
                      type: number
                      example: "1.0"
                      format: float
                      description: Price.
                      x-description-cn: 价格。
                    newClientOrderId:
                      type: string
                      example: "1"
                      description: >-
                        A unique id among open orders. Automatically generated if not sent. Can only be string following
                        the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                      x-description-cn: 挂单中的唯一客户端订单 ID；未传则自动生成。仅支持匹配 `^[\\.A-Z\\:/a-z0-9_-]{1,36}$` 的字符串。
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
                      description: only available for `LIMIT` order; Can't be passed together with `price`
                      x-description-cn: 仅 `LIMIT` 订单可用；不能与 `price` 同时传。
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
                        taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default
                        `NONE`
                      x-description-cn: 自成交保护模式，默认 `NONE`。
                    goodTillDate:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                        timestamp only retains second-level precision, ms part will be ignored; The goodTillDate
                        timestamp must be greater than the current time plus 600 seconds and smaller than
                        253402300799000
                      x-description-cn: >-
                        order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                        timestamp only retains second-level precision, ms part will be ignored; The goodTillDate
                        timestamp must be greater than the current time plus 600 seconds and smaller than
                        253402300799000
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                symbol: BTCUSDT
                side: BUY
                positionSide: BOTH
                type: LIMIT
                timeInForce: GTC
                reduceOnly: "false"
                quantity: "1.0"
                price: "1.0"
                newClientOrderId: "1"
                newOrderRespType: ACK
                priceMatch: OPPONENT
                selfTradePreventionMode: NONE
                goodTillDate: 1770736694138
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: New Order
          x-description-cn: 下单
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 3f7df6e3-2df4-44b9-9919-d2f38f90a99a
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        example: 325078477
                        format: int64
                      symbol:
                        type: string
                        example: BTCUSDT
                      status:
                        type: string
                        example: NEW
                      clientOrderId:
                        type: string
                        example: iCXL1BywlBaf2sesNUrVl3
                      price:
                        type: string
                        example: "43187.00"
                      origQty:
                        type: string
                        example: "0.100"
                      executedQty:
                        type: string
                        example: "0.000"
                      cumQty:
                        type: string
                        example: "0.000"
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: LIMIT
                      reduceOnly:
                        type: boolean
                        example: false
                      closePosition:
                        type: boolean
                        example: false
                      side:
                        type: string
                        example: BUY
                      positionSide:
                        type: string
                        example: BOTH
                      stopPrice:
                        type: string
                        example: "0.00"
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                      priceProtect:
                        type: boolean
                        example: false
                      origType:
                        type: string
                        example: LIMIT
                      priceMatch:
                        type: string
                        example: NONE
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_MAKER
                      goodTillDate:
                        type: integer
                        example: 0
                        format: int64
                      updateTime:
                        type: integer
                        example: 1702555534435
                        format: int64
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
                          example: 10
                          format: int64
                        limit:
                          type: integer
                          example: 300
                          format: int64
                        count:
                          type: integer
                          example: 1
                          format: int64
  /account.position:
    post:
      summary: Position Information (USER_DATA)
      x-summary-cn: 用户持仓风险V2 (USER_DATA)
      description: Get current position information.
      x-description-cn: 查询持仓风险
      tags:
        - trade
      operationId: positionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/positionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/PositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/PositionInformation/PositionInformation.go
      x-ip-weight: 5
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        - Please use with user data stream `ACCOUNT_UPDATE` to meet your
        timeliness and accuracy needs.
      x-parameters-notes-cn: "- 建议结合用户数据流 `ACCOUNT_UPDATE` 一起使用，以满足时效性和准确性需求。"
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                symbol: BTCUSDT
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
                    example: 605a6d20-6588-4cb9-afa0-b0ab087507ba
                  status:
                    type: integer
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        entryPrice:
                          type: string
                          example: "0.00000"
                        breakEvenPrice:
                          type: string
                          example: "0.0"
                        marginType:
                          type: string
                          example: isolated
                        isAutoAddMargin:
                          type: string
                          example: "false"
                        isolatedMargin:
                          type: string
                          example: "0.00000000"
                        leverage:
                          type: string
                          example: "10"
                        liquidationPrice:
                          type: string
                          example: "0"
                        markPrice:
                          type: string
                          example: "6679.50671178"
                        maxNotionalValue:
                          type: string
                          example: "20000000"
                        positionAmt:
                          type: string
                          example: "0.000"
                        notional:
                          type: string
                          example: "0"
                        isolatedWallet:
                          type: string
                          example: "0"
                        symbol:
                          type: string
                          example: BTCUSDT
                        unRealizedProfit:
                          type: string
                          example: "0.00000000"
                        positionSide:
                          type: string
                          example: BOTH
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
  /v2/account.position:
    post:
      summary: Position Information V2 (USER_DATA)
      x-summary-cn: 用户持仓风险V2 (USER_DATA)
      description: |-
        Get current position information(only symbol that has position or open
        orders will be returned).
      x-description-cn: 查询持仓风险，仅返回有仓位或挂单的交易对
      tags:
        - trade
      operationId: positionInformationV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#position-information-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/positionInformationV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/position_information_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/position_information_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/PositionInformationV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/PositionInformationV2/PositionInformationV2.go
      x-ip-weight: 5
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        - Please use with user data stream `ACCOUNT_UPDATE` to meet your
        timeliness and accuracy needs.
      x-parameters-notes-cn: "- 建议结合用户数据流 `ACCOUNT_UPDATE` 一起使用，以满足时效性和准确性需求。"
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
                  description: Id.
                  x-description-cn: 请求 ID。
                method:
                  type: string
                  description: WebSocket API method name.
                  x-description-cn: WebSocket API 方法名称。
                  enum:
                    - v2/account.position
                  example: v2/account.position
                params:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
              method: v2/account.position
              params:
                symbol: BTCUSDT
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Position Information V2
          x-description-cn: 持仓 信息 V2
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
                    example: 200
                    format: int64
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: ADAUSDT
                        positionSide:
                          type: string
                          example: BOTH
                          description: Position Side
                          x-description-cn: 持仓方向
                        positionAmt:
                          type: string
                          example: "30"
                        entryPrice:
                          type: string
                          example: "0.385"
                        breakEvenPrice:
                          type: string
                          example: "0.385077"
                        markPrice:
                          type: string
                          example: "0.41047590"
                        unRealizedProfit:
                          type: string
                          example: "0.76427700"
                          description: Unrealized Profit
                          x-description-cn: 未实现盈亏
                        liquidationPrice:
                          type: string
                          example: "0"
                        isolatedMargin:
                          type: string
                          example: "0"
                        notional:
                          type: string
                          example: "12.31427700"
                        marginAsset:
                          type: string
                          example: USDT
                        isolatedWallet:
                          type: string
                          example: "0"
                        initialMargin:
                          type: string
                          example: "0.61571385"
                          description: Initial Margin
                          x-description-cn: 起始保证金
                        maintMargin:
                          type: string
                          example: "0.08004280"
                          description: Maintainance Margin
                          x-description-cn: 维持保证金
                        positionInitialMargin:
                          type: string
                          example: "0.61571385"
                          description: Position Initial Margin
                          x-description-cn: 持仓起始保证金
                        openOrderInitialMargin:
                          type: string
                          example: "0"
                          description: Open Order Initial Margin
                          x-description-cn: 挂单起始保证金
                        adl:
                          type: integer
                          example: 2
                          format: int64
                        bidNotional:
                          type: string
                          example: "0"
                        askNotional:
                          type: string
                          example: "0"
                        updateTime:
                          type: integer
                          example: 1720736417660
                          format: int64
                          description: Update Time
                          x-description-cn: 更新时间
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 20
                          format: int64
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/trade#query-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/TradeApi/queryOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/trade_api/query_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/Trade/query_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/trade/QueryOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/TradeAPI/QueryOrder/QueryOrder.go
      x-ip-weight: 1
      x-security-type: USER_DATA
      x-signed: true
      x-parameters-notes: |-
        Notes:
        - Either `orderId` or `origClientOrderId` must be sent.
        - `orderId` is self-increment for each specific `symbol`
      x-parameters-notes-cn: |-
        说明：
        - `orderId` 与 `origClientOrderId` 至少需要传一个。
        - `orderId` 在每个 `symbol` 维度内自增。
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
                      example: BTCUSDT
                      description: Symbol.
                      x-description-cn: 交易对。
                    orderId:
                      type: integer
                      example: 1
                      format: int64
                      description: Order Id.
                      x-description-cn: 系统订单号。
                    origClientOrderId:
                      type: string
                      example: "1"
                      description: Orig Client Order Id.
                      x-description-cn: 原客户端订单号。
                    recvWindow:
                      type: integer
                      example: 5000
                      format: int64
                      description: Recv Window.
                      x-description-cn: 接收窗口。
                    timestamp:
                      type: integer
                      example: 1770736694138
                      format: int64
                      description: >-
                        Unix timestamp in milliseconds used to sign the request. The value must reflect the current
                        client time and is validated by the server for signed endpoints.
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
                symbol: BTCUSDT
                orderId: 1
                origClientOrderId: "1"
                recvWindow: 5000
                timestamp: 1770736694138
                apiKey: API_KEY
      responses:
        Successful Response:
          description: Order Status
          x-description-cn: 订单
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
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      avgPrice:
                        type: string
                        example: "0.00000"
                      clientOrderId:
                        type: string
                        example: abc
                      cumQuote:
                        type: string
                        example: "0"
                      executedQty:
                        type: string
                        example: "0"
                      orderId:
                        type: integer
                        example: 1573346959
                        format: int64
                      origQty:
                        type: string
                        example: "0.40"
                      origType:
                        type: string
                        example: TRAILING_STOP_MARKET
                      price:
                        type: string
                        example: "0"
                      reduceOnly:
                        type: boolean
                        example: false
                      side:
                        type: string
                        example: BUY
                      positionSide:
                        type: string
                        example: SHORT
                      status:
                        type: string
                        example: NEW
                      stopPrice:
                        type: string
                        example: "9300"
                        description: please ignore when order type is TRAILING_STOP_MARKET
                        x-description-cn: 当订单类型为 `TRAILING_STOP_MARKET` 时请忽略。
                      closePosition:
                        type: boolean
                        example: false
                        description: if Close-All
                        x-description-cn: 是否全平
                      symbol:
                        type: string
                        example: BTCUSDT
                      time:
                        type: integer
                        example: 1579276756075
                        format: int64
                        description: order time
                        x-description-cn: 下单时间
                      timeInForce:
                        type: string
                        example: GTC
                      type:
                        type: string
                        example: TRAILING_STOP_MARKET
                      activatePrice:
                        type: string
                        example: "9020"
                        description: activation price, only return with TRAILING_STOP_MARKET order
                        x-description-cn: 激活价格，仅 `TRAILING_STOP_MARKET` 返回。
                      priceRate:
                        type: string
                        example: "0.3"
                        description: callback rate, only return with TRAILING_STOP_MARKET order
                        x-description-cn: 回调比例，仅 `TRAILING_STOP_MARKET` 返回。
                      updateTime:
                        type: integer
                        example: 1579276756075
                        format: int64
                        description: update time
                        x-description-cn: 更新时间
                      workingType:
                        type: string
                        example: CONTRACT_PRICE
                      priceProtect:
                        type: boolean
                        example: false
                        description: if conditional order trigger is protected
                        x-description-cn: 条件单触发是否启用保护。
                      priceMatch:
                        type: string
                        example: NONE
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_MAKER
                        description: Self-trade prevention mode
                        x-description-cn: 自我交易预防模式
                      goodTillDate:
                        type: integer
                        format: int64
                        example: 0
                        description: Order good till date timestamp
                        x-description-cn: 订单有效截止时间戳
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
          x-description-cn: 关闭用户数据流
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 819e1b1b-8c06-485b-a13e-131326c69599
                  status:
                    type: integer
                    example: 200
                    format: int64
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
                          example: 1
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 2
                          format: int64
  /userDataStream.ping:
    post:
      summary: Keepalive User Data Stream (USER_STREAM)
      x-summary-cn: Websocket API延长listenKey有效期 (USER_STREAM)
      description: >-
        Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's
        recommended to send a ping about every 60 minutes.
      x-description-cn: 有效期延长至本次调用后60分钟
      tags:
        - user-data-streams
      operationId: keepaliveUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
          x-description-cn: 延长用户数据流有效期
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 815d5fce-0880-4287-a567-80badf004c74
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 2
                          format: int64
  /userDataStream.start:
    post:
      summary: Start User Data Stream (USER_STREAM)
      x-summary-cn: Websocket API生成listenKey (USER_STREAM)
      description: >-
        Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account
        has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.
      x-description-cn: 创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。
      tags:
        - user-data-streams
      operationId: startUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/websocket-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/websocket_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/websocket_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/websocket/api/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/websocketapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
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
                  description: Id.
                  x-description-cn: 请求 ID。
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
          x-description-cn: 启动用户数据流
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
                    example: 200
                    format: int64
                  result:
                    type: object
                    properties:
                      listenKey:
                        type: string
                        example: xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP
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
                          format: int64
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                        count:
                          type: integer
                          example: 2
                          format: int64
```