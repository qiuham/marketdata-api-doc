---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:30.272913
---

# core-trading-derivatives-trading-coin-m-futures__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Futures (COIN-M) REST API
  description: Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.
  x-description-cn: 访问市场数据、管理账户，并交易 COIN-M 永续和交割合约。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/derivatives-trading-coin-futures/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-coin-futures/general-info#访问限制
x-security-guide: products/derivatives-trading-coin-futures/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-coin-futures/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Futures (COIN-M) docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/general-info
  x-description-cn: Futures (COIN-M) docs
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 行情接口
  - name: portfolio-margin-endpoints
    x-displayName: Portfolio Margin Endpoints
    x-displayName-cn: 经典统一账户接口
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: user-data-streams
    x-displayName: User Data Streams
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: https://dapi.binance.com
  - url: https://testnet.binancefuture.com
paths:
  /dapi/v1/account:
    get:
      summary: Account Information (USER_DATA)
      x-summary-cn: 账户信息 (USER_DATA)
      description: Get current account information.
      x-description-cn: 查询账户信息
      tags:
        - account
      operationId: accountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/accountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/AccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/AccountInformation/AccountInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/AccountInformationExample.php
      x-ip-weight: 5
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - for One-way Mode user, the "positions" will only show the "BOTH" positions
        - for Hedge Mode user, the "positions" will show "BOTH", "LONG", and "SHORT" positions.
      x-parameters-notes-cn: |-
        - 对于单向持仓模式，"positions"仅会展示"BOTH"方向的持仓
        - 对于双向持仓模式，"positions"会展示所有"BOTH", "LONG", 和"SHORT"方向的持仓
      responses:
        "200":
          description: Account Information
          x-description-cn: 账户 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  assets:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: BTC
                          description: asset name
                          x-description-cn: 资产
                        walletBalance:
                          type: string
                          example: "0.00241969"
                          description: total wallet balance
                          x-description-cn: 账户余额
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit or loss
                          x-description-cn: 全部持仓未实现盈亏
                        marginBalance:
                          type: string
                          example: "0.00241969"
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
                          example: "0.00241969"
                          description: maximum amount for transfer out
                          x-description-cn: 最大可转出余额
                        crossWalletBalance:
                          type: string
                          example: "0.00241969"
                          description: wallet balance for crossed margin
                          x-description-cn: 可用于全仓的账户余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: total unrealized profit or loss of crossed positions
                          x-description-cn: 所有全仓持仓的未实现盈亏
                        availableBalance:
                          type: string
                          example: "0.00241969"
                          description: available margin balance
                          x-description-cn: 可用下单余额
                        updateTime:
                          type: integer
                          example: 1625474304765
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
                          example: BTCUSD_201225
                          description: Trading symbol
                          x-description-cn: 交易对
                        positionAmt:
                          type: string
                          example: "0"
                          description: position amount
                          x-description-cn: 持仓数量
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
                          example: "125"
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
                          example: "0.0"
                          description: Position entry price.
                          x-description-cn: 持仓开仓价格.
                        breakEvenPrice:
                          type: string
                          example: "0.0"
                          description: break-even price
                          x-description-cn: 盈亏平衡价
                        maxQty:
                          type: string
                          example: "50"
                          description: maximum quantity of base asset
                          x-description-cn: 数量上限, 最大数量
                        updateTime:
                          type: integer
                          example: 0
                          format: int64
                          description: update time
                          x-description-cn: 更新时间
                        notionalValue:
                          type: string
                          example: "0"
                          description: Notional value.
                          x-description-cn: 名义价值.
                    description: Position list.
                    x-description-cn: 持仓列表.
                  canDeposit:
                    type: boolean
                    example: true
                    description: Whether deposits are enabled.
                    x-description-cn: 是否可充值.
                  canTrade:
                    type: boolean
                    example: true
                    description: Whether trading is enabled.
                    x-description-cn: 是否可交易.
                  canWithdraw:
                    type: boolean
                    example: true
                    description: Whether withdrawals are enabled.
                    x-description-cn: 是否可提现.
                  feeTier:
                    type: integer
                    example: 2
                    format: int64
                    description: Fee tier level.
                    x-description-cn: 手续费等级.
                  updateTime:
                    type: integer
                    example: 0
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
  /dapi/v1/balance:
    get:
      summary: Futures Account Balance (USER_DATA)
      x-summary-cn: 账户余额 (USER_DATA)
      description: Check futures account balance
      x-description-cn: 查询账户余额
      tags:
        - account
      operationId: futuresAccountBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#futures-account-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/futuresAccountBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/futures_account_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/futures_account_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/FuturesAccountBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/FuturesAccountBalance/FuturesAccountBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/FuturesAccountBalanceExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Futures Account Balance
          x-description-cn: 合约 账户 Balance
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    accountAlias:
                      type: string
                      example: SgsR
                      description: unique account code
                      x-description-cn: 账户唯一识别码
                    asset:
                      type: string
                      example: BTC
                      description: asset name
                      x-description-cn: 资产
                    balance:
                      type: string
                      example: "0.00250000"
                      description: Account balance.
                      x-description-cn: 账户余额.
                    withdrawAvailable:
                      type: string
                      example: "0.00250000"
                      description: Available amount for withdrawal.
                      x-description-cn: 可提现金额.
                    crossWalletBalance:
                      type: string
                      example: "0.00241969"
                      description: wallet balance for crossed margin
                      x-description-cn: 可用于全仓的账户余额
                    crossUnPnl:
                      type: string
                      example: "0.00000000"
                      description: total unrealized profit or loss of crossed positions
                      x-description-cn: 所有全仓持仓的未实现盈亏
                    availableBalance:
                      type: string
                      example: "0.00241969"
                      description: available margin balance
                      x-description-cn: 可用下单余额
                    updateTime:
                      type: integer
                      example: 1592468353979
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
  /dapi/v1/positionSide/dual:
    get:
      summary: Get Current Position Mode (USER_DATA)
      x-summary-cn: 查询持仓模式 (USER_DATA)
      description: Get user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***
      x-description-cn: 查询用户目前在 ***所有symbol*** 合约上的持仓模式：双向持仓或单向持仓。
      tags:
        - account
      operationId: getCurrentPositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-current-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getCurrentPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_current_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_current_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetCurrentPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetCurrentPositionMode/GetCurrentPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetCurrentPositionModeExample.php
      x-ip-weight: 30
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Current Position Mode
          x-description-cn: 获取当前 持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  dualSidePosition:
                    type: boolean
                    example: true
                    description: Whether dual-side position mode is enabled.
                    x-description-cn: 是否开启双向持仓模式.
    post:
      summary: Change Position Mode (TRADE)
      x-summary-cn: 更改持仓模式 (TRADE)
      description: >-
        Change user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***.


        **After CM migration**, UM and CM share the **same** `dualSidePosition` setting. Calling this endpoint flips
        both UM and CM at once. If either side has any open order or open position, the change is rejected:

        - `-4067` (open orders exist)

        - `-4068` (open position exists)
      x-description-cn: |-
        变换用户在 ***所有symbol*** 合约上的持仓模式：双向持仓或单向持仓。

        **迁移后**,UM 与 CM 共用**同一个** `dualSidePosition` 设置。调用此接口会同时翻转 UM 与 CM。任意一侧存在挂单或持仓时,切换会被拒绝:
        - `-4067`(存在挂单)
        - `-4068`(存在持仓)
      tags:
        - trade
      operationId: changePositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#change-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/changePositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/change_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/change_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ChangePositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ChangePositionMode/ChangePositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ChangePositionModeExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - dualSidePosition
                - timestamp
              properties:
                dualSidePosition:
                  type: string
                  example: "true"
                  description: '"true": Hedge Mode; "false": One-way Mode'
                  x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
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
      responses:
        "200":
          description: Change Position Mode
          x-description-cn: 修改持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  msg:
                    type: string
                    example: success
                    description: Message details.
                    x-description-cn: 消息详情.
  /dapi/v1/order/asyn:
    get:
      summary: Get Download Id For Futures Order History (USER_DATA)
      x-summary-cn: 获取合约订单历史下载Id (USER_DATA)
      description: Get Download Id For Futures Order History
      x-description-cn: 获取合约订单历史下载Id
      tags:
        - account
      operationId: getDownloadIdForFuturesOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-download-id-for-futures-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_download_id_for_futures_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_download_id_for_futures_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetDownloadIdForFuturesOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesOrderHistory/GetDownloadIdForFuturesOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetDownloadIdForFuturesOrderHistoryExample.php
      x-ip-weight: 1000
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
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms
          x-description-cn: 起始时间，ms格式时间戳
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 结束时间，ms格式时间戳
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Request Limitation is 8 times per month, shared by front end download page and rest api

        - This endpoint uses the IP rate limit bucket and costs 1000 weight per call. The maximum is 2 calls per minute;
        the 3rd call within the same minute will trigger a ban.

        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月8次的请求限制，网页端和Rest接口下载次数共用。
        - 该接口走IP限流桶，每次消耗1000 weight。每分钟最多调用2次，第3次将触发封禁。
        - `startTime`与`endTime`间隔不能超过1年
      responses:
        "200":
          description: Get Download Id For Futures Order History
          x-description-cn: 获取Download ID 用于 合约 订单 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgCostTimestampOfLast30d:
                    type: integer
                    example: 7241837
                    format: int64
                    description: Average time taken for data download in the past 30 days
                    x-description-cn: 过去30天平均数据下载时间
                  downloadId:
                    type: string
                    example: "546975389218332672"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
  /dapi/v1/trade/asyn:
    get:
      summary: Get Download Id For Futures Trade History (USER_DATA)
      x-summary-cn: 获取合约交易历史下载Id (USER_DATA)
      description: Get download id for futures trade history
      x-description-cn: 获取合约交易历史下载Id
      tags:
        - account
      operationId: getDownloadIdForFuturesTradeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-download-id-for-futures-trade-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesTradeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_download_id_for_futures_trade_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_download_id_for_futures_trade_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetDownloadIdForFuturesTradeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesTradeHistory/GetDownloadIdForFuturesTradeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetDownloadIdForFuturesTradeHistoryExample.php
      x-ip-weight: 1000
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
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms
          x-description-cn: 起始时间，ms格式时间戳
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 结束时间，ms格式时间戳
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Request Limitation is 8 times per month, shared by front end download page and rest api

        - This endpoint uses the IP rate limit bucket and costs 1000 weight per call. The maximum is 2 calls per minute;
        the 3rd call within the same minute will trigger a ban.

        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月8次的请求限制，网页端和Rest接口下载次数共用。
        - 该接口走IP限流桶，每次消耗1000 weight。每分钟最多调用2次，第3次将触发封禁。
        - `startTime`与`endTime`间隔不能超过1年
      responses:
        "200":
          description: Get Download Id For Futures Trade History
          x-description-cn: 获取Download ID 用于 合约 交易 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgCostTimestampOfLast30d:
                    type: integer
                    example: 7241837
                    format: int64
                    description: Average time taken for data download in the past 30 days
                    x-description-cn: 过去30天平均数据下载时间
                  downloadId:
                    type: string
                    example: "546975389218332672"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
  /dapi/v1/income/asyn:
    get:
      summary: Get Download Id For Futures Transaction History (USER_DATA)
      x-summary-cn: 获取合约资金流水下载Id (USER_DATA)
      description: Get download id for futures transaction history
      x-description-cn: 获取合约资金流水下载Id
      tags:
        - account
      operationId: getDownloadIdForFuturesTransactionHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-download-id-for-futures-transaction-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesTransactionHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_download_id_for_futures_transaction_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_download_id_for_futures_transaction_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetDownloadIdForFuturesTransactionHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesTransactionHistory/GetDownloadIdForFuturesTransactionHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetDownloadIdForFuturesTransactionHistoryExample.php
      x-ip-weight: 1000
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
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms
          x-description-cn: 起始时间，ms格式时间戳
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 结束时间，ms格式时间戳
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - The request limit is 100 times per month, shared across the front end download page and rest api, as well as
        between USDⓈ-M and COIN-M contracts.

        - This endpoint uses the IP rate limit bucket and costs 1000 weight per call. The maximum is 2 calls per minute;
        the 3rd call within the same minute will trigger a ban.

        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月100次的请求限制，该限制在网页端下载页面与Rest接口之间共用，并且在U本位合约与币本位合约之间共用。
        - 该接口走IP限流桶，每次消耗1000 weight。每分钟最多调用2次，第3次将触发封禁。
        - `startTime`与`endTime`间隔不能超过1年
      responses:
        "200":
          description: Get Download Id For Futures Transaction History
          x-description-cn: 获取Download ID 用于 合约 Transaction 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgCostTimestampOfLast30d:
                    type: integer
                    example: 7241837
                    format: int64
                    description: Average time taken for data download in the past 30 days
                    x-description-cn: 过去30天平均数据下载时间
                  downloadId:
                    type: string
                    example: "546975389218332672"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
  /dapi/v1/order/asyn/id:
    get:
      summary: Get Futures Order History Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取合约订单下载链接 (USER_DATA)
      description: Get futures order history download link by Id
      x-description-cn: 通过下载Id获取合约订单下载链接
      tags:
        - account
      operationId: getFuturesOrderHistoryDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-futures-order-history-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getFuturesOrderHistoryDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_futures_order_history_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_futures_order_history_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetFuturesOrderHistoryDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetFuturesOrderHistoryDownloadLinkById/GetFuturesOrderHistoryDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetFuturesOrderHistoryDownloadLinkByIdExample.php
      x-ip-weight: 5
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
        - name: downloadId
          in: query
          required: true
          schema:
            type: string
            example: "545923594199212032"
          description: get by download id api
          x-description-cn: 通过下载id 接口获取
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get Futures Order History Download Link by Id
          x-description-cn: 获取合约 订单 历史 Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 订单状态
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  notified:
                    type: boolean
                    example: false
                    description: ignore
                    x-description-cn: 忽略
                  expirationTimestamp:
                    type: integer
                    example: -1
                    format: int64
                    description: The link would expire after this timestamp
                    x-description-cn: 晚于该时间戳之后链接将自动失效
                  isExpired:
                    type: string
                    example: "null"
                    description: Whether the record is expired.
                    x-description-cn: 记录是否已过期.
  /dapi/v1/trade/asyn/id:
    get:
      summary: Get Futures Trade Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取合约交易历史下载链接 (USER_DATA)
      description: Get futures trade download link by Id
      x-description-cn: 通过下载Id获取合约交易历史下载链接
      tags:
        - account
      operationId: getFuturesTradeDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-futures-trade-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getFuturesTradeDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_futures_trade_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_futures_trade_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetFuturesTradeDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetFuturesTradeDownloadLinkById/GetFuturesTradeDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetFuturesTradeDownloadLinkByIdExample.php
      x-ip-weight: 5
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
        - name: downloadId
          in: query
          required: true
          schema:
            type: string
            example: "545923594199212032"
          description: get by download id api
          x-description-cn: 通过下载id 接口获取
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get Futures Trade Download Link by Id
          x-description-cn: 获取合约 交易 Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 订单状态
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  notified:
                    type: boolean
                    example: false
                    description: ignore
                    x-description-cn: 忽略
                  expirationTimestamp:
                    type: integer
                    example: -1
                    format: int64
                    description: The link would expire after this timestamp
                    x-description-cn: 晚于该时间戳之后链接将自动失效
                  isExpired:
                    type: string
                    example: "null"
                    description: Whether the record is expired.
                    x-description-cn: 记录是否已过期.
  /dapi/v1/income/asyn/id:
    get:
      summary: Get Futures Transaction History Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取合约资金流水下载链接 (USER_DATA)
      description: Get futures transaction history download link by Id
      x-description-cn: 过下载Id获取合约资金流水下载链接
      tags:
        - account
      operationId: getFuturesTransactionHistoryDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-futures-transaction-history-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getFuturesTransactionHistoryDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_futures_transaction_history_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_futures_transaction_history_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetFuturesTransactionHistoryDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetFuturesTransactionHistoryDownloadLinkById/GetFuturesTransactionHistoryDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetFuturesTransactionHistoryDownloadLinkByIdExample.php
      x-ip-weight: 5
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
        - name: downloadId
          in: query
          required: true
          schema:
            type: string
            example: "545923594199212032"
          description: get by download id api
          x-description-cn: 通过下载id 接口获取
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get Futures Transaction History Download Link by Id
          x-description-cn: 获取合约 Transaction 历史 Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download task ID.
                    x-description-cn: 下载任务 ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 订单状态
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  notified:
                    type: boolean
                    example: false
                    description: ignore
                    x-description-cn: 忽略
                  expirationTimestamp:
                    type: integer
                    example: -1
                    format: int64
                    description: The link would expire after this timestamp
                    x-description-cn: 晚于该时间戳之后链接将自动失效
                  isExpired:
                    type: string
                    example: "null"
                    description: Whether the record is expired.
                    x-description-cn: 记录是否已过期.
  /dapi/v1/income:
    get:
      summary: Get Income History (USER_DATA)
      x-summary-cn: 获取账户损益资金流水 (USER_DATA)
      description: Get income history
      x-description-cn: 获取账户损益资金流水
      tags:
        - account
      operationId: getIncomeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#get-income-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/getIncomeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/get_income_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/get_income_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/GetIncomeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/GetIncomeHistory/GetIncomeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/GetIncomeHistoryExample.php
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
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: incomeType
          in: query
          required: false
          schema:
            type: string
            example: TRANSFER
            enum:
              - TRANSFER
              - WELCOME_BONUS
              - FUNDING_FEE
              - REALIZED_PNL
              - COMMISSION
              - INSURANCE_CLEAR
              - DELIVERED_SETTELMENT
          description: Income type.
          x-description-cn: 收益类型.
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms to get funding from INCLUSIVE.
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms to get funding until INCLUSIVE.
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 100
            maximum: 1000
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `incomeType ` is not sent, all kinds of flow will be returned
        - "trandId" is unique in the same "incomeType" for a user
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 如果`incomeType`没有发送,返回所有类型账户损益资金流水。
        - "trandId" 在相同用户的同一种收益流水类型中是唯一的。
        - `startTime`与`endTime`间隔不能超过1年回
      responses:
        "200":
          description: Get Income History
          x-description-cn: 获取Income 历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ""
                      description: Trading symbol
                      x-description-cn: 交易对
                    incomeType:
                      type: string
                      example: TRANSFER
                      description: income type
                      x-description-cn: 资金流类型
                    income:
                      type: string
                      example: "-0.37500000"
                      description: income amount
                      x-description-cn: 资金流数量,正数代表流入,负数代表流出
                    asset:
                      type: string
                      example: BTC
                      description: asset name
                      x-description-cn: 资产
                    info:
                      type: string
                      example: WITHDRAW
                      description: extra information
                      x-description-cn: 备注信息,取决于流水类型
                    time:
                      type: integer
                      example: 1570608000000
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    tranId:
                      type: string
                      example: "9689322392"
                      description: transaction id
                      x-description-cn: 划转ID
                    tradeId:
                      type: string
                      example: ""
                      description: Trade ID.
                      x-description-cn: 成交 ID.
  /dapi/v1/leverageBracket:
    get:
      summary: Notional Bracket for Pair (USER_DATA)
      x-summary-cn: 标的交易对默认杠杆分层标准 (USER_DATA)
      description: |-
        **Not recommended to continue using this v1 endpoint**

        Get the pair's default notional bracket list, may return ambiguous
        values when there have been multiple different `symbol` brackets under
        the `pair`, suggest using the following `GET /dapi/v2/leverageBracket`
        query instead to get the specific `symbol` notional bracket list.
      x-description-cn: |-
        **不建议继续使用该 v1 接口**

        获取标的交易对默认的杠杆分层标准，当 `pair` 下曾有过多个不同 `symbol` 杠杆分层标准时可能返回歧义值，建议使用下面的 `GET
        /dapi/v2/leverageBracket` 代替查询以获取具体 `symbol` 杠杆分层标准
      tags:
        - account
      operationId: notionalBracketForPair
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#notional-bracket-for-pair
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/notionalBracketForPair.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/notional_bracket_for_pair.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/notional_bracket_for_pair.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/NotionalBracketForPairExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/NotionalBracketForPair/NotionalBracketForPair.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/NotionalBracketForPairExample.php
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
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Notional Bracket for Pair
          x-description-cn: Notional Bracket 用于 Pair
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    brackets:
                      type: array
                      items:
                        type: object
                        properties:
                          bracket:
                            type: integer
                            example: 1
                            format: int64
                            description: bracket level
                            x-description-cn: 层级
                          initialLeverage:
                            type: integer
                            example: 125
                            format: int64
                            description: the maximum leverage
                            x-description-cn: 该层允许的最高初始杠杆倍数
                          qtyCap:
                            type: integer
                            example: 50
                            format: int64
                            description: upper edge of base asset quantity
                            x-description-cn: 该层对应的数量上限
                          qtylFloor:
                            type: integer
                            example: 0
                            format: int64
                            description: lower edge of base asset quantity
                            x-description-cn: 该层对应的数量下限
                          maintMarginRatio:
                            type: number
                            example: 0.004
                            format: float
                            description: Maintenance margin ratio.
                            x-description-cn: 维持保证金率.
                          cum:
                            type: number
                            example: 0
                            format: float
                            description: Cumulative value.
                            x-description-cn: 累计值.
                      description: Leverage bracket details.
                      x-description-cn: 杠杆分层详情.
  /dapi/v2/leverageBracket:
    get:
      summary: Notional Bracket for Symbol (USER_DATA)
      x-summary-cn: 交易对杠杆分层标准 (USER_DATA)
      description: Get the symbol's notional bracket list.
      x-description-cn: 获取交易对的杠杆分层标准
      tags:
        - account
      operationId: notionalBracketForSymbol
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#notional-bracket-for-symbol
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/notionalBracketForSymbol.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/notional_bracket_for_symbol.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/notional_bracket_for_symbol.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/NotionalBracketForSymbolExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/NotionalBracketForSymbol/NotionalBracketForSymbol.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/NotionalBracketForSymbolExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "1 (after CM migration: 1 with `symbol` / 2 without `symbol`)"
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
            example: BTCUSD_PERP
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Notional Bracket for Symbol
          x-description-cn: Notional Bracket 用于 交易对
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_PERP
                      description: Trading symbol
                      x-description-cn: 交易对
                    notionalCoef:
                      type: number
                      example: 1.5
                      format: float
                      description: user symbol bracket multiplier, only appears when user's symbol bracket is adjusted
                      x-description-cn: 用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示
                    brackets:
                      type: array
                      items:
                        type: object
                        properties:
                          bracket:
                            type: integer
                            example: 1
                            format: int64
                            description: bracket level
                            x-description-cn: 层级
                          initialLeverage:
                            type: integer
                            example: 125
                            format: int64
                            description: the maximum leverage
                            x-description-cn: 该层允许的最高初始杠杆倍数
                          qtyCap:
                            type: integer
                            example: 50
                            format: int64
                            description: upper edge of base asset quantity
                            x-description-cn: 该层对应的数量上限
                          qtylFloor:
                            type: integer
                            example: 0
                            format: int64
                            description: lower edge of base asset quantity
                            x-description-cn: 该层对应的数量下限
                          maintMarginRatio:
                            type: number
                            example: 0.004
                            format: float
                            description: Maintenance margin ratio.
                            x-description-cn: 维持保证金率.
                          cum:
                            type: number
                            example: 0
                            format: float
                            description: Cumulative value.
                            x-description-cn: 累计值.
                      description: Leverage bracket details.
                      x-description-cn: 杠杆分层详情.
  /dapi/v1/commissionRate:
    get:
      summary: User Commission Rate (USER_DATA)
      x-summary-cn: 用户手续费率 (USER_DATA)
      description: Query user commission rate
      x-description-cn: 查询用户手续费率
      tags:
        - account
      operationId: userCommissionRate
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/account#user-commission-rate
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/AccountApi/userCommissionRate.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/account_api/user_commission_rate.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Account/user_commission_rate.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/account/UserCommissionRateExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/AccountAPI/UserCommissionRate/UserCommissionRate.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/account/UserCommissionRateExample.php
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
            example: BTCUSD_PERP
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: User Commission Rate
          x-description-cn: 用户 手续费 利率
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSD_PERP
                    description: Trading symbol
                    x-description-cn: 交易对
                  makerCommissionRate:
                    type: string
                    example: "0.00015"
                    description: 0.015%
                    x-description-cn: 0.015%
                  takerCommissionRate:
                    type: string
                    example: "0.00040"
                    description: Taker commission rate.
                    x-description-cn: 吃单手续费率.
  /futures/data/basis:
    get:
      summary: Basis
      x-summary-cn: 基差
      description: Query basis
      x-description-cn: 查询基差
      tags:
        - market-data
      operationId: basis
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#basis
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/basis.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/basis.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/basis.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/BasisExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/Basis/Basis.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/BasisExample.php
      x-ip-weight: 1
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: null
          description: Pair.
          x-description-cn: 标的交易对。
        - name: contractType
          in: query
          required: true
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
          description: Contract type.
          x-description-cn: 合约类型。
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
          description: Period interval.
          x-description-cn: 周期区间。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Basis
          x-description-cn: 请参见英文说明：Basis
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    indexPrice:
                      type: string
                      example: "29269.93972727"
                      description: index price
                      x-description-cn: 指数价格
                    contractType:
                      type: string
                      example: CURRENT_QUARTER
                      description: Contract type.
                      x-description-cn: 合约类型.
                    basisRate:
                      type: string
                      example: "0.0024"
                      description: Basis rate.
                      x-description-cn: 基差率.
                    futuresPrice:
                      type: string
                      example: "29341.3"
                      description: Futures price.
                      x-description-cn: 期货价格.
                    annualizedBasisRate:
                      type: string
                      example: "0.0283"
                      description: Annualized basis rate.
                      x-description-cn: 年化基差率.
                    basis:
                      type: string
                      example: "71.36027273"
                      description: Basis value.
                      x-description-cn: 基差值.
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    timestamp:
                      type: integer
                      example: 1653381600000
                      format: int64
                      description: Start time of the period, in milliseconds.
                      x-description-cn: 该周期的开始时间，单位为毫秒。
  /dapi/v1/time:
    get:
      summary: Check Server time
      x-summary-cn: 获取服务器时间
      description: Test connectivity to the Rest API and get the current server time.
      x-description-cn: 获取服务器时间
      tags:
        - market-data
      operationId: checkServerTime
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#check-server-time
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/checkServerTime.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/check_server_time.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/check_server_time.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/CheckServerTimeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/CheckServerTime/CheckServerTime.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/CheckServerTimeExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: Check Server time
          x-description-cn: 检查Server 时间
          content:
            application/json:
              schema:
                type: object
                properties:
                  serverTime:
                    type: integer
                    example: 1499827319559
                    format: int64
                    description: Ignore please. If you want to check current server time, please check via "GET /dapi/v1/time"
                    x-description-cn: 请忽略。如果需要获取系统时间，请查询接口 “GET /dapi/v1/time”
  /dapi/v1/aggTrades:
    get:
      summary: Compressed/Aggregate Trades List
      x-summary-cn: 近期成交
      description: |-
        Get compressed, aggregate trades. Market trades that fill in 100ms with
        the same price and the same taking side will have the quantity
        aggregated.
      x-description-cn: 归集交易与逐笔交易的区别在于，同一价格、同一方向、同一时间(100ms 计算)的订单簿trade 会被聚合为一条
      tags:
        - market-data
      operationId: compressedAggregateTradesList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#compressed-aggregate-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/compressedAggregateTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/compressed_aggregate_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/compressed_aggregate_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/CompressedAggregateTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/CompressedAggregateTradesList/CompressedAggregateTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/CompressedAggregateTradesListExample.php
      x-ip-weight: 20
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: null
          description: Symbol
          x-description-cn: 交易对
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: ID to get aggregate trades from INCLUSIVE.
          x-description-cn: 从包含 fromID 的成交开始返回结果
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms to get aggregate trades from INCLUSIVE.
          x-description-cn: 从该时刻之后的成交记录开始返回结果
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms to get aggregate trades until INCLUSIVE.
          x-description-cn: 返回该时刻为止的成交记录
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1000
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: >-
        - only trade histories within the past 48 hours (counted from now) can be queried

        - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 1 hour.

        - If `fromId`, `startTime`, and `endTime` are not sent, the most recent aggregate trades will be returned.

        - Only market trades will be aggregated and returned, which means the insurance fund trades and ADL trades won't
        be aggregated.

        - Sending both `startTime`/`endTime` and `fromId` might cause response timeout, please send either `fromId` or
        `startTime`/`endTime`
      x-parameters-notes-cn: |-
        - 接口仅支持查询最近24小时的交易数据
        - 如果同时发送`startTime`和`endTime`，间隔必须小于一小时
        - 如果没有发送任何筛选参数(`fromId`, `startTime`, `endTime`),默认返回最近的成交记录
        - 保险基金和自动减仓(ADL)成交不属于订单簿成交，故不会被归并聚合
        - 同时发送`startTime`/`endTime`和`fromId`可能导致请求超时，建议仅发送`fromId`或仅发送`startTime`和`endTime`
      responses:
        "200":
          description: Compressed/Aggregate Trades List
          x-description-cn: Compressed/Aggregate 交易s 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    a:
                      type: integer
                      example: 416690
                      format: int64
                      description: Aggregate tradeId
                      x-description-cn: 归集成交 ID
                    p:
                      type: string
                      example: "9642.4"
                      description: Price
                      x-description-cn: 价格
                    q:
                      type: string
                      example: "3"
                      description: Quantity
                      x-description-cn: 数量
                    f:
                      type: integer
                      example: 595259
                      format: int64
                      description: First tradeId
                      x-description-cn: 首个成交 ID
                    l:
                      type: integer
                      example: 595259
                      format: int64
                      description: Last tradeId
                      x-description-cn: 最后成交 ID
                    T:
                      type: integer
                      example: 1591250548649
                      format: int64
                      description: Timestamp
                      x-description-cn: 时间戳
                    m:
                      type: boolean
                      example: false
                      description: Was the buyer the maker?
                      x-description-cn: 买方是否为挂单方
  /dapi/v1/continuousKlines:
    get:
      summary: Continuous Contract Kline/Candlestick Data
      x-summary-cn: 连续合约K线数据
      description: Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.
      x-description-cn: 每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: continuousContractKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#continuous-contract-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/continuousContractKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/continuous_contract_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/continuous_contract_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/ContinuousContractKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/ContinuousContractKlineCandlestickData/ContinuousContractKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/ContinuousContractKlineCandlestickDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

        | LIMIT | weight |
        | --- | --- |
        | [1,100) | 1 |
        | [100, 500) | 2 |
        | [500, 1000] | 5 |
        | > 1000 | 10 |
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: After CM migration, accepts both CM and UM pair values.
          x-description-cn: 标的交易对。迁移后支持传入 CM 与 UM 的 pair。
        - name: contractType
          in: query
          required: true
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
        - name: interval
          in: query
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
          description: Interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: |-
        - The difference between `startTime` and `endTime` can only be up to 200 days
        - Between `startTime` and `endTime`, the most recent `limit` data from `endTime` will be returned:
          - If `startTime` and `endTime` are not sent, current timestamp will be set as `endTime`, and the most recent data will be returned.
          - If `startTime` is sent only, the timestamp of 200 days after `startTime` will be set as `endTime`(up to the current time)
          - If `endTime` is sent only, the timestamp of 200 days before `endTime` will be set as `startTime`
      x-parameters-notes-cn: |-
        - startTime 与 endTime 之间最多只可以相差200天
        - 默认返回 startTime 与 endTime 之间最接近 endTime的 limit 条数据:
          - startTime, endTime 均未提供的, 将会使用当前时间为 endTime, 200天前为 startTime
          - 仅提供 startTime 的, 将会使用 startTime 之后200天作为默认 endTime (至多为当前时间)
          - 仅提供 endTime 的, 将会使用endTime 之前200天作为默认 startTime
      responses:
        "200":
          description: Continuous Contract Kline/Candlestick Data
          x-description-cn: Continuous Contract K线/Candlestick Data
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
                      example: 1591258320000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "9640.7"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "9642.4"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "9640.6"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "9642.0"
                    - type: string
                      description: Volume
                      x-description-cn: 成交量
                      example: "206"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1591258379999
                    - type: string
                      description: Base asset volume
                      x-description-cn: 成交额
                      example: "2.13660389"
                    - type: integer
                      description: Number of trades
                      x-description-cn: 成交笔数
                      example: 48
                    - type: string
                      description: Taker buy volume
                      x-description-cn: 主动买入成交量
                      example: "119"
                    - type: string
                      description: Taker buy base asset volume
                      x-description-cn: 主动买入基础资产成交量
                      example: "1.23424865"
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
                        example: 1591258320000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "9640.7"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "9642.4"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "9640.6"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "9642.0"
                      - type: string
                        description: Volume
                        x-description-cn: 成交量
                        example: "206"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1591258379999
                      - type: string
                        description: Base asset volume
                        x-description-cn: 成交额
                        example: "2.13660389"
                      - type: integer
                        description: Number of trades
                        x-description-cn: 成交笔数
                        example: 48
                      - type: string
                        description: Taker buy volume
                        x-description-cn: 主动买入成交量
                        example: "119"
                      - type: string
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入基础资产成交量
                        example: "1.23424865"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /dapi/v1/exchangeInfo:
    get:
      summary: Exchange Information
      x-summary-cn: 获取交易规则和交易对
      description: Current exchange trading rules and symbol information
      x-description-cn: 获取交易规则和交易对
      tags:
        - market-data
      operationId: exchangeInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#exchange-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/exchangeInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/exchange_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/exchange_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/ExchangeInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/ExchangeInformation/ExchangeInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/ExchangeInformationExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: Exchange Information
          x-description-cn: Exchange 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  exchangeFilters:
                    type: array
                    items:
                      type: string
                      example: []
                    description: Exchange filters.
                    x-description-cn: 交易所过滤器.
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
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
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: Rate limit type.
                          x-description-cn: 频率限制类型.
                    description: Rate limit definitions.
                    x-description-cn: 频率限制定义.
                  serverTime:
                    type: integer
                    example: 1565613908500
                    format: int64
                    description: Ignore please. If you want to check current server time, please check via "GET /dapi/v1/time"
                    x-description-cn: 请忽略。如果需要获取系统时间，请查询接口 “GET /dapi/v1/time”
                  symbols:
                    type: array
                    items:
                      type: object
                      properties:
                        filters:
                          type: array
                          items:
                            type: object
                            properties:
                              filterType:
                                type: string
                                example: PRICE_FILTER
                                description: Filter type.
                                x-description-cn: 过滤器类型。
                              maxPrice:
                                type: string
                                example: "100000"
                                description: Maximum price.
                                x-description-cn: 最大价格。
                              minPrice:
                                type: string
                                example: "0.1"
                                description: Minimum price.
                                x-description-cn: 最小价格。
                              tickSize:
                                type: string
                                example: "0.1"
                                description: Tick size.
                                x-description-cn: 价格步长。
                              maxQty:
                                type: string
                                example: "100000"
                                description: maximum quantity of base asset
                                x-description-cn: 数量上限, 最大数量
                              minQty:
                                type: string
                                example: "1"
                                description: Minimum quantity.
                                x-description-cn: 最小数量。
                              stepSize:
                                type: string
                                example: "1"
                                description: Step size.
                                x-description-cn: 数量步长。
                              limit:
                                type: integer
                                example: 200
                                format: int64
                                description: Maximum allowed orders for this rule.
                                x-description-cn: 该规则允许的最大订单数。
                              multiplierUp:
                                type: string
                                example: "1.0500"
                                description: Upper multiplier bound.
                                x-description-cn: 上限倍率。
                              multiplierDown:
                                type: string
                                example: "0.9500"
                                description: Lower multiplier bound.
                                x-description-cn: 下限倍率。
                              multiplierDecimal:
                                type: string
                                example: "4"
                                description: Multiplier decimal precision.
                                x-description-cn: 乘数小数精度.
                          description: Trading filters and constraints.
                          x-description-cn: 交易过滤器与限制。
                        orderTypes:
                          type: array
                          items:
                            type: string
                            example: LIMIT
                          description: Supported order types.
                          x-description-cn: 支持的订单类型.
                        timeInForce:
                          type: array
                          items:
                            type: string
                            example: GTC
                          description: Time in force
                          x-description-cn: 有效方式
                        liquidationFee:
                          type: string
                          example: "0.010000"
                          description: liquidation fee rate
                          x-description-cn: 强平费率
                        marketTakeBound:
                          type: string
                          example: "0.30"
                          description: the max price difference rate( from mark price) a market order can make
                          x-description-cn: 市价吃单(相对于标记价格)允许可造成的最大价格偏离比例
                        symbol:
                          type: string
                          example: BTCUSD_200925
                          description: Trading symbol
                          x-description-cn: 交易对
                        pair:
                          type: string
                          example: BTCUSD
                          description: Pair
                          x-description-cn: 标的交易对
                        contractType:
                          type: string
                          example: CURRENT_QUARTER
                          description: Contract type.
                          x-description-cn: 合约类型.
                        deliveryDate:
                          type: integer
                          example: 1601020800000
                          format: int64
                          description: Delivery timestamp.
                          x-description-cn: 交割时间戳.
                        onboardDate:
                          type: integer
                          example: 1590739200000
                          format: int64
                          description: Onboard timestamp.
                          x-description-cn: 上线时间戳.
                        contractStatus:
                          type: string
                          example: TRADING
                          description: Contract status.
                          x-description-cn: 合约状态.
                        contractSize:
                          type: integer
                          example: 100
                          format: int64
                          description: Contract size.
                          x-description-cn: 合约面值.
                        quoteAsset:
                          type: string
                          example: USD
                          description: Quote asset symbol.
                          x-description-cn: 计价资产符号。
                        baseAsset:
                          type: string
                          example: BTC
                          description: Base asset symbol.
                          x-description-cn: 基础资产符号。
                        marginAsset:
                          type: string
                          example: BTC
                          description: Margin asset.
                          x-description-cn: 保证金币种.
                        pricePrecision:
                          type: integer
                          example: 1
                          format: int64
                          description: please do not use it as tickSize
                          x-description-cn: 价格小数点位数(仅作为系统精度使用，注意同tickSize 区分)
                        quantityPrecision:
                          type: integer
                          example: 0
                          format: int64
                          description: please do not use it as stepSize
                          x-description-cn: 数量小数点位数(仅作为系统精度使用，注意同stepSize 区分)
                        baseAssetPrecision:
                          type: integer
                          example: 8
                          format: int64
                          description: Base asset precision.
                          x-description-cn: 基础资产精度。
                        quotePrecision:
                          type: integer
                          example: 8
                          format: int64
                          description: Quote asset precision.
                          x-description-cn: 计价资产精度。
                        equalQtyPrecision:
                          type: integer
                          example: 4
                          format: int64
                          description: ignore
                          x-description-cn: 请忽略
                        triggerProtect:
                          type: string
                          example: "0.0500"
                          description: threshold for algo order with "priceProtect"
                          x-description-cn: 开启"priceProtect"的条件订单的触发阈值
                        maintMarginPercent:
                          type: string
                          example: "2.5000"
                          description: ignore
                          x-description-cn: 请忽略
                        requiredMarginPercent:
                          type: string
                          example: "5.0000"
                          description: ignore
                          x-description-cn: 请忽略
                        underlyingType:
                          type: string
                          example: COIN
                          description: Underlying asset type.
                          x-description-cn: 标的资产类型.
                        underlyingSubType:
                          type: array
                          items:
                            type: string
                            example: []
                          description: Underlying asset sub-type.
                          x-description-cn: 标的资产子类型.
                    description: Supported trading symbols.
                    x-description-cn: 支持的交易对列表。
                  timezone:
                    type: string
                    example: UTC
                    description: Timezone of market data.
                    x-description-cn: 行情数据时区。
  /dapi/v1/fundingRate:
    get:
      summary: Get Funding Rate History of Perpetual Futures
      x-summary-cn: 查询永续合约资金费率历史
      description: Get Funding Rate History of Perpetual Futures
      x-description-cn: 查询永续合约资金费率历史
      tags:
        - market-data
      operationId: getFundingRateHistoryOfPerpetualFutures
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#get-funding-rate-history-of-perpetual-futures
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/getFundingRateHistoryOfPerpetualFutures.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/get_funding_rate_history_of_perpetual_futures.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/get_funding_rate_history_of_perpetual_futures.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/GetFundingRateHistoryOfPerpetualFuturesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/GetFundingRateHistoryOfPerpetualFutures/GetFundingRateHistoryOfPerpetualFutures.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/GetFundingRateHistoryOfPerpetualFuturesExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: null
          description: Symbol
          x-description-cn: 交易对
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms to get funding rate from INCLUSIVE.
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms to get funding rate until INCLUSIVE.
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 100
            maximum: 1000
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: "- empty array will be returned for delivery symbols."
      x-parameters-notes-cn: "- 对非永续合约，将返回空列表"
      responses:
        "200":
          description: Get Funding Rate History of Perpetual Futures
          x-description-cn: 获取Funding 利率 历史 of Perpetual 合约
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_PERP
                      description: Trading symbol
                      x-description-cn: 交易对
                    fundingTime:
                      type: integer
                      example: 1596038400000
                      format: int64
                      description: Funding time.
                      x-description-cn: 资金费时间.
                    fundingRate:
                      type: string
                      example: "-0.00300000"
                      description: Funding rate.
                      x-description-cn: 资金费率.
  /dapi/v1/fundingInfo:
    get:
      summary: Get Funding Rate Info
      x-summary-cn: 查询资金费率信息
      description: Query funding rate info for symbols that had FundingRateCap/FundingRateFloor/fundingIntervalHours adjustment
      x-description-cn: 查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours被特殊调整过的交易对
      tags:
        - market-data
      operationId: getFundingRateInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#get-funding-rate-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/getFundingRateInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/get_funding_rate_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/get_funding_rate_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/GetFundingRateInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/GetFundingRateInfo/GetFundingRateInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/GetFundingRateInfoExample.php
      parameters: []
      responses:
        "200":
          description: Get Funding Rate Info
          x-description-cn: 获取Funding 利率 Info
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_PERP
                      description: Trading symbol
                      x-description-cn: 交易对
                    adjustedFundingRateCap:
                      type: string
                      example: "0.02500000"
                      description: Adjusted funding rate cap.
                      x-description-cn: 调整后资金费率上限.
                    adjustedFundingRateFloor:
                      type: string
                      example: "-0.02500000"
                      description: Adjusted funding rate floor.
                      x-description-cn: 调整后资金费率下限.
                    fundingIntervalHours:
                      type: integer
                      example: 8
                      format: int64
                      description: Funding interval in hours.
                      x-description-cn: 资金费结算间隔（小时）.
                    disclaimer:
                      type: boolean
                      example: false
                      description: Disclaimer text.
                      x-description-cn: 免责声明文本.
  /dapi/v1/premiumIndex:
    get:
      summary: Index Price and Mark Price
      x-summary-cn: 最新现货指数价格和Mark Price
      description: Query index price and mark price
      x-description-cn: 查询最新现货指数价格和Mark Price
      tags:
        - market-data
      operationId: indexPriceAndMarkPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#index-price-and-mark-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/indexPriceAndMarkPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/index_price_and_mark_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/index_price_and_mark_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/IndexPriceAndMarkPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/IndexPriceAndMarkPrice/IndexPriceAndMarkPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/IndexPriceAndMarkPriceExample.php
      x-ip-weight: 10
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD_PERP
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
      responses:
        "200":
          description: Index Price and Mark Price
          x-description-cn: Index 价格 和 Mark 价格
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
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
                    markPrice:
                      type: string
                      example: "11029.69574559"
                      description: mark price
                      x-description-cn: 标记价格
                    indexPrice:
                      type: string
                      example: "10979.14437500"
                      description: index price
                      x-description-cn: 指数价格
                    estimatedSettlePrice:
                      type: string
                      example: "10981.74168236"
                      description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                      x-description-cn: 预估结算价,仅在交割开始前最后一小时有意义
                    lastFundingRate:
                      type: string
                      example: "0.00071003"
                      description: >-
                        the lasted funding rate, for perpetual contract symbols only. For delivery symbols, "" will be
                        shown.
                      x-description-cn: 最近更新的资金费率,只对永续合约有效，其他合约返回""
                    interestRate:
                      type: string
                      example: "0.00010000"
                      description: >-
                        the base asset interest rate, for perpetual contract symbols only. For delivery symbols, "" will
                        be shown.
                      x-description-cn: 标的资产基础利率,只对永续合约有效，其他合约返回""
                    nextFundingTime:
                      type: integer
                      example: 1596096000000
                      format: int64
                      description: For perpetual contract symbols only. For delivery symbols, 0 will be shown
                      x-description-cn: 下次资金费时间，只对永续合约有效，其他合约返回0
                    time:
                      type: integer
                      example: 1596094042000
                      format: int64
                      description: Time
                      x-description-cn: 时间
  /dapi/v1/indexPriceKlines:
    get:
      summary: Index Price Kline/Candlestick Data
      x-summary-cn: 价格指数K线数据
      description: Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.
      x-description-cn: 查询价格指数K线
      tags:
        - market-data
      operationId: indexPriceKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#index-price-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/indexPriceKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/index_price_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/index_price_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/IndexPriceKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/IndexPriceKlineCandlestickData/IndexPriceKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/IndexPriceKlineCandlestickDataExample.php
      x-weight: |-
        Based on parameter `LIMIT`

        | LIMIT | weight |
        | --- | --- |
        | [1,100) | 1 |
        | [100, 500) | 2 |
        | [500, 1000] | 5 |
        | > 1000 | 10 |
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: After CM migration, accepts both CM and UM pair values.
          x-description-cn: 标的交易对 迁移后支持传入 CM 与 UM 的 pair。
        - name: interval
          in: query
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
          description: Interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: |-
        - The difference between `startTime` and `endTime` can only be up to 200 days
        - Between `startTime` and `endTime`, the most recent `limit` data from `endTime` will be returned:
          - If `startTime` and `endTime` are not sent, current timestamp will be set as `endTime`, and the most recent data will be returned.
          - If `startTime` is sent only, the timestamp of 200 days after `startTime` will be set as `endTime`(up to the current time)
          - If `endTime` is sent only, the timestamp of 200 days before `endTime` will be set as `startTime`
      x-parameters-notes-cn: |-
        - startTime 与 endTime 之间最多只可以相差200天
        - 默认返回 startTime 与 endTime 之间最接近 endTime的 limit 条数据:
          - startTime, endTime 均未提供的, 将会使用当前时间为 endTime, 200天前为 startTime
          - 仅提供 startTime 的, 将会使用 startTime 之后200天作为默认 endTime (至多为当前时间)
          - 仅提供 endTime 的, 将会使用endTime 之前200天作为默认 startTime
      responses:
        "200":
          description: Index Price Kline/Candlestick Data
          x-description-cn: Index 价格 K线/Candlestick Data
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
                      example: 1591256400000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "9653.69440000"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "9653.69640000"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "9651.38600000"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "9651.55200000"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1591256459999
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      description: Number of bisic data
                      x-description-cn: 成交笔数
                      example: 60
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
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
                        example: 1591256400000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "9653.69440000"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "9653.69640000"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "9651.38600000"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "9651.55200000"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1591256459999
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        description: Number of bisic data
                        x-description-cn: 成交笔数
                        example: 60
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /dapi/v1/klines:
    get:
      summary: Kline/Candlestick Data
      x-summary-cn: K线数据
      description: Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
      x-description-cn: 每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: klineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/klineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/KlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/KlineCandlestickData/KlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/KlineCandlestickDataExample.php
      x-weight: |-
        Based on parameter `LIMIT`

        | LIMIT | weight |
        | --- | --- |
        | [1,100) | 1 |
        | [100, 500) | 2 |
        | [500, 1000] | 5 |
        | > 1000 | 10 |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: After CM migration, accepts both CM and UM symbols.
          x-description-cn: 交易对 迁移后支持传入 CM 与 UM 的 symbol。
        - name: interval
          in: query
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
          description: Interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: |-
        - The difference between `startTime` and `endTime` can only be up to 200 days
        - Between `startTime` and `endTime`, the most recent `limit` data from `endTime` will be returned:
          - If `startTime` and `endTime` are not sent, current timestamp will be set as `endTime`, and the most recent data will be returned.
          - If `startTime` is sent only, the timestamp of 200 days after `startTime` will be set as `endTime`(up to the current time)
          - If `endTime` is sent only, the timestamp of 200 days before `endTime` will be set as `startTime`
      x-parameters-notes-cn: |-
        - startTime 与 endTime 之间最多只可以相差200天
        - 默认返回 startTime 与 endTime 之间最接近 endTime的 limit 条数据:
          - startTime, endTime 均未提供的, 将会使用当前时间为 endTime, 200天前为 startTime
          - 仅提供 startTime 的, 将会使用 startTime 之后200天作为默认 endTime (至多为当前时间)
          - 仅提供 endTime 的, 将会使用endTime 之前200天作为默认 startTime
      responses:
        "200":
          description: Kline/Candlestick Data
          x-description-cn: K线/Candlestick Data
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
                      example: 1591258320000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "9640.7"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "9642.4"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "9640.6"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "9642.0"
                    - type: string
                      description: Volume
                      x-description-cn: 成交量
                      example: "206"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1591258379999
                    - type: string
                      description: Base asset volume
                      x-description-cn: 成交额
                      example: "2.13660389"
                    - type: integer
                      description: Number of trades
                      x-description-cn: 成交笔数
                      example: 48
                    - type: string
                      description: Taker buy volume
                      x-description-cn: 主动买入成交量
                      example: "119"
                    - type: string
                      description: Taker buy base asset volume
                      x-description-cn: 主动买入基础资产成交量
                      example: "1.23424865"
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
                        example: 1591258320000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "9640.7"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "9642.4"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "9640.6"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "9642.0"
                      - type: string
                        description: Volume
                        x-description-cn: 成交量
                        example: "206"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1591258379999
                      - type: string
                        description: Base asset volume
                        x-description-cn: 成交额
                        example: "2.13660389"
                      - type: integer
                        description: Number of trades
                        x-description-cn: 成交笔数
                        example: 48
                      - type: string
                        description: Taker buy volume
                        x-description-cn: 主动买入成交量
                        example: "119"
                      - type: string
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入基础资产成交量
                        example: "1.23424865"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /futures/data/globalLongShortAccountRatio:
    get:
      summary: Long/Short Ratio
      x-summary-cn: 多空持仓人数比
      description: Query symbol Long/Short Ratio
      x-description-cn: 多空持仓人数比
      tags:
        - market-data
      operationId: longShortRatio
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#long-short-ratio
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/longShortRatio.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/long_short_ratio.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/long_short_ratio.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/LongShortRatioExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/LongShortRatio/LongShortRatio.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/LongShortRatioExample.php
      x-ip-weight: 1
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: null
          description: BTCUSD
          x-description-cn: 请参见英文说明：BTCUSD
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
        - name: contractType
          in: query
          required: false
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
          description: Contract type filter. If omitted, returns aggregated data across all contract types.
          x-description-cn: 合约类型过滤。若不填，则返回所有合约类型的汇总数据。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Long/Short Ratio
          x-description-cn: 请参见英文说明：Long/Short Ratio
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    longShortRatio:
                      type: string
                      example: "0.1960"
                      description: Long/short ratio.
                      x-description-cn: 多空比.
                    longAccount:
                      type: string
                      example: "0.6622"
                      description: 64.42%
                      x-description-cn: 64.42%
                    shortAccount:
                      type: string
                      example: "0.3378"
                      description: 35.58%
                      x-description-cn: 35.58%
                    timestamp:
                      type: integer
                      example: 1583139600000
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /dapi/v1/markPriceKlines:
    get:
      summary: Mark Price Kline/Candlestick Data
      x-summary-cn: 标记价格K线数据
      description: Kline/candlestick bars for the mark price of a symbol. Klines are uniquely identified by their open time.
      x-description-cn: K线/candlestick bars 用于 the mark 价格 of a 交易对. K线s are uniquely identified by their 未完成 时间."
      tags:
        - market-data
      operationId: markPriceKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#mark-price-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/markPriceKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/mark_price_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/mark_price_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/MarkPriceKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/MarkPriceKlineCandlestickData/MarkPriceKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/MarkPriceKlineCandlestickDataExample.php
      x-weight: |-
        Based on parameter `LIMIT`

        | LIMIT | weight |
        | --- | --- |
        | [1,100) | 1 |
        | [100, 500) | 2 |
        | [500, 1000] | 5 |
        | > 1000 | 10 |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: After CM migration, accepts both CM and UM symbols.
          x-description-cn: 交易对 迁移后支持传入 CM 与 UM 的 symbol。
        - name: interval
          in: query
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
          description: Interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: |-
        - The difference between `startTime` and `endTime` can only be up to 200 days
        - Between `startTime` and `endTime`, the most recent `limit` data from `endTime` will be returned:
          - If `startTime` and `endTime` are not sent, current timestamp will be set as `endTime`, and the most recent data will be returned.
          - If `startTime` is sent only, the timestamp of 200 days after `startTime` will be set as `endTime`(up to the current time)
          - If `endTime` is sent only, the timestamp of 200 days before `endTime` will be set as `startTime`
      x-parameters-notes-cn: |-
        - startTime 与 endTime 之间最多只可以相差200天
        - 默认返回 startTime 与 endTime 之间最接近 endTime的 limit 条数据:
          - startTime, endTime 均未提供的, 将会使用当前时间为 endTime, 200天前为 startTime
          - 仅提供 startTime 的, 将会使用 startTime 之后200天作为默认 endTime (至多为当前时间)
          - 仅提供 endTime 的, 将会使用endTime 之前200天作为默认 startTime
      responses:
        "200":
          description: Mark Price Kline/Candlestick Data
          x-description-cn: Mark 价格 K线/Candlestick Data
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
                      example: 1591256400000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "9653.69440000"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "9653.69640000"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "9651.38600000"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "9651.55200000"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1591256459999
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      description: Number of bisic data
                      x-description-cn: 成交笔数
                      example: 60
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
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
                        example: 1591256400000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "9653.69440000"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "9653.69640000"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "9651.38600000"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "9651.55200000"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1591256459999
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        description: Number of bisic data
                        x-description-cn: 成交笔数
                        example: 60
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /dapi/v1/historicalTrades:
    get:
      summary: Old Trades Lookup (MARKET_DATA)
      x-summary-cn: 查询历史成交 (MARKET_DATA)
      description: Get older market historical trades.
      x-description-cn: 查询订单簿历史成交
      tags:
        - market-data
      operationId: oldTradesLookup
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#old-trades-lookup
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/oldTradesLookup.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/old_trades_lookup.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/old_trades_lookup.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/OldTradesLookupExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/OldTradesLookup/OldTradesLookup.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/OldTradesLookupExample.php
      x-ip-weight: 200
      x-security-type: MARKET_DATA
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
            example: null
          description: Symbol
          x-description-cn: 交易对
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 100
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 595103
            format: int64
          description: TradeId to fetch from. Default gets most recent trades.
          x-description-cn: 从该 TradeId 开始获取数据。默认为获取最近的成交。
      x-parameters-notes: >-
        - Market trades means trades filled in the order book. Only market trades will be returned, which means the
        insurance fund trades and ADL trades won't be returned.

        - Only supports data from within the last one month
      x-parameters-notes-cn: |-
        - 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交
        - 仅支持返回最近1个月的数据
      responses:
        "200":
          description: Old Trades Lookup
          x-description-cn: Old 交易s Lookup
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 595103
                      format: int64
                      description: positionId
                      x-description-cn: 持仓 ID
                    price:
                      type: string
                      example: "9642.2"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    qty:
                      type: string
                      example: "1"
                      description: Quantity.
                      x-description-cn: 数量.
                    baseQty:
                      type: string
                      example: "0.01037108"
                      description: Base asset quantity.
                      x-description-cn: 基础资产数量.
                    time:
                      type: integer
                      example: 1499865549590
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    isBuyerMaker:
                      type: boolean
                      example: true
                      description: Whether buyer is market maker.
                      x-description-cn: 买方是否为做市方.
  /dapi/v1/openInterest:
    get:
      summary: Open Interest
      x-summary-cn: 获取未平仓合约数
      description: Get present open interest of a specific symbol.
      x-description-cn: 合约持仓量
      tags:
        - market-data
      operationId: openInterest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#open-interest
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/openInterest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/open_interest.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/open_interest.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/OpenInterestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/OpenInterest/OpenInterest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/OpenInterestExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD_200626
          description: Symbol
          x-description-cn: 交易对
      responses:
        "200":
          description: Open Interest
          x-description-cn: 未完成利息
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSD_200626
                    description: Trading symbol
                    x-description-cn: 交易对
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  openInterest:
                    type: string
                    example: "15004"
                    description: Open interest.
                    x-description-cn: 未平仓量.
                  contractType:
                    type: string
                    example: CURRENT_QUARTER
                    description: Contract type.
                    x-description-cn: 合约类型.
                  time:
                    type: integer
                    example: 1591261042378
                    format: int64
                    description: Time
                    x-description-cn: 时间
  /futures/data/openInterestHist:
    get:
      summary: Open Interest Statistics
      x-summary-cn: 合约持仓量
      description: Query open interest stats
      x-description-cn: 合约持仓量
      tags:
        - market-data
      operationId: openInterestStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#open-interest-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/openInterestStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/open_interest_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/open_interest_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/OpenInterestStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/OpenInterestStatistics/OpenInterestStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/OpenInterestStatisticsExample.php
      x-ip-weight: 1
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
        - name: contractType
          in: query
          required: false
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
          description: Contract type filter. If omitted, returns aggregated data across all contract types.
          x-description-cn: 合约类型过滤。若不填，则返回所有合约类型的汇总数据。
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Open Interest Statistics
          x-description-cn: 未完成利息 Statistics
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    contractType:
                      type: string
                      example: CURRENT_QUARTER
                      description: Contract type.
                      x-description-cn: 合约类型.
                    sumOpenInterest:
                      type: string
                      example: "20403"
                      description: "unit: cont"
                      x-description-cn: "unit: cont"
                    sumOpenInterestValue:
                      type: string
                      example: "176196512.23400000"
                      description: "unit: base asset"
                      x-description-cn: "unit: base asset"
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /dapi/v1/depth:
    get:
      summary: Order Book
      x-summary-cn: 深度信息
      description: Query orderbook on specific symbol
      x-description-cn: 查询交易对深度
      tags:
        - market-data
      operationId: orderBook
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#order-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/orderBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/order_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/order_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/OrderBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/OrderBook/OrderBook.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/OrderBookExample.php
      x-weight: |-
        Adjusted based on the limit:

        | Limit | Weight |
        | ------------ | ------------ |
        | 5, 10, 20, 50 | 2 |
        | 100 | 5 |
        | 500 | 10 |
        | 1000 | 20 |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD_PERP
          description: Symbol
          x-description-cn: 交易对
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 500
            maximum: 1000
          description: Valid limits:[5, 10, 20, 50, 100, 500, 1000].
          x-description-cn: 可选限制:[5, 10, 20, 50, 100, 500, 1000].
      responses:
        "200":
          description: Order Book
          x-description-cn: 订单 Book
          content:
            application/json:
              schema:
                type: object
                properties:
                  lastUpdateId:
                    type: integer
                    example: 16769853
                    format: int64
                    description: Last update ID.
                    x-description-cn: 最后更新 ID.
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
                  E:
                    type: integer
                    example: 1591250106370
                    format: int64
                    description: Message output time
                    x-description-cn: 消息输出时间
                  T:
                    type: integer
                    example: 1591250106368
                    format: int64
                    description: Transaction time
                    x-description-cn: 成交时间
                  bids:
                    type: array
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          example: "9638.00000000"
                        - type: string
                          description: Quantity
                          example: "431.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "9638.00000000"
                          - type: string
                            description: Quantity
                            example: "431.00000000"
                    description: Bid orders. Each entry is [price, quantity].
                    x-description-cn: 买单列表。每项为 [价格, 数量]。
                    example:
                      - - "9638.00000000"
                        - "431.00000000"
                  asks:
                    type: array
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          example: "9638.20000000"
                        - type: string
                          description: Quantity
                          example: "12.00000000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "9638.20000000"
                          - type: string
                            description: Quantity
                            example: "12.00000000"
                    description: Ask orders. Each entry is [price, quantity].
                    x-description-cn: 卖单列表。每项为 [价格, 数量]。
                    example:
                      - - "9638.20000000"
                        - "12.00000000"
  /dapi/v1/premiumIndexKlines:
    get:
      summary: Premium index Kline Data
      x-summary-cn: 溢价指数K线数据
      description: Premium index kline bars of a symbol. Klines are uniquely identified by their open time.
      x-description-cn: 合约溢价指数K线。每根K线的开盘时间可视为唯一ID。
      tags:
        - market-data
      operationId: premiumIndexKlineData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#premium-index-kline-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/premiumIndexKlineData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/premium_index_kline_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/premium_index_kline_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/PremiumIndexKlineDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/PremiumIndexKlineData/PremiumIndexKlineData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/PremiumIndexKlineDataExample.php
      x-weight: |-
        Based on parameter `LIMIT`

        | LIMIT       | weight |
        | ----------- | ------ |
        | [1,100)     | 1      |
        | [100, 500)  | 2      |
        | [500, 1000] | 5      |
        | > 1000      | 10     |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: After CM migration, accepts both CM and UM symbols.
          x-description-cn: 交易对。迁移后支持传入 CM 与 UM 的 symbol。
        - name: interval
          in: query
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
          description: Interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: "- If startTime and endTime are not sent, the most recent klines are returned."
      x-parameters-notes-cn: "- 缺省返回最近的数据"
      responses:
        "200":
          description: Premium index Kline Data
          x-description-cn: Premium index K线 Data
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
                      example: 1691603820000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "-0.00042931"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "-0.00023641"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "-0.00059406"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "-0.00043659"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1691603879999
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: 12
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
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
                        example: 1691603820000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "-0.00042931"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "-0.00023641"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "-0.00059406"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "-0.00043659"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1691603879999
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: 12
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /dapi/v1/constituents:
    get:
      summary: Query Index Price Constituents
      x-summary-cn: 查询指数价格成分
      description: Query index price constituents
      x-description-cn: 查询指数价格成分
      tags:
        - market-data
      operationId: queryIndexPriceConstituents
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#query-index-price-constituents
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/queryIndexPriceConstituents.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/query_index_price_constituents.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/query_index_price_constituents.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/QueryIndexPriceConstituentsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/QueryIndexPriceConstituents/QueryIndexPriceConstituents.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/QueryIndexPriceConstituentsExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: Symbol
          x-description-cn: 交易对
      responses:
        "200":
          description: Index Price Constituents
          x-description-cn: Index 价格 Constituents
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSD
                    description: Trading symbol
                    x-description-cn: 交易对
                  time:
                    type: integer
                    example: 1697422647853
                    format: int64
                    description: Time
                    x-description-cn: 时间
                  constituents:
                    type: array
                    items:
                      type: object
                      properties:
                        exchange:
                          type: string
                          example: bitstamp
                          description: Exchange identifier.
                          x-description-cn: 交易所标识.
                        symbol:
                          type: string
                          example: btcusd
                          description: Trading symbol
                          x-description-cn: 交易对
                        price:
                          type: string
                          example: "94057.03000000"
                          description: Price
                          x-description-cn: 价格
                        weight:
                          type: string
                          example: "0.25000000"
                          description: Weight
                          x-description-cn: 权重
                    description: Constituent list.
                    x-description-cn: 成分列表.
  /dapi/v1/trades:
    get:
      summary: Recent Trades List
      x-summary-cn: 近期成交
      description: Get recent market trades
      x-description-cn: 获取近期订单簿成交
      tags:
        - market-data
      operationId: recentTradesList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#recent-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/recentTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/recent_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/recent_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/RecentTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/RecentTradesList/RecentTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/RecentTradesListExample.php
      x-ip-weight: 5
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: Symbol
          x-description-cn: 交易对
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 500
            maximum: 1000
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
      x-parameters-notes: >-
        - Market trades means trades filled in the order book. Only market trades will be returned, which means the
        insurance fund trades and ADL trades won't be returned.
      x-parameters-notes-cn: "- 市场成交指订单簿中的成交。该接口仅返回市场成交，不包含保险基金成交和 ADL 成交。"
      responses:
        "200":
          description: Recent Trades List
          x-description-cn: Recent 交易s 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 28457
                      format: int64
                      description: positionId
                      x-description-cn: 持仓 ID
                    price:
                      type: string
                      example: "9635.0"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    qty:
                      type: string
                      example: "1"
                      description: Quantity.
                      x-description-cn: 数量.
                    baseQty:
                      type: string
                      example: "0.01037883"
                      description: Base asset quantity.
                      x-description-cn: 基础资产数量.
                    time:
                      type: integer
                      example: 1591250192508
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    isBuyerMaker:
                      type: boolean
                      example: true
                      description: Whether buyer is market maker.
                      x-description-cn: 买方是否为做市方.
  /dapi/v1/ticker/bookTicker:
    get:
      summary: Symbol Order Book Ticker
      x-summary-cn: 当前最优挂单
      description: Best price/qty on the order book for a symbol or symbols.
      x-description-cn: 返回当前最优的挂单(最高买单,最低卖单)
      tags:
        - market-data
      operationId: symbolOrderBookTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#symbol-order-book-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/symbolOrderBookTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/symbol_order_book_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/symbol_order_book_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/SymbolOrderBookTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/SymbolOrderBookTicker/SymbolOrderBookTicker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/SymbolOrderBookTickerExample.php
      x-weight: "**2** for a single symbol, **5** when the symbol parameter is omitted"
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD_200626
          description: Symbol
          x-description-cn: 交易对
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: Symbol
          x-description-cn: 标的交易对
      x-parameters-notes: |-
        - Symbol and pair cannot be sent together
        - If a pair is sent,tickers for all symbols of the pair will be returned
        - If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
      x-parameters-notes-cn: |-
        - symbol 和 pair 不接受同时发送
        - 发送 pair的,返回pair对应所有正在交易的symbol数据
        - symbol,pair 都没有发送的,返回所有symbol数据
      responses:
        "200":
          description: Symbol Order Book Ticker
          x-description-cn: 交易对 订单 最优挂单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    lastUpdateId:
                      type: integer
                      example: 1027024
                      format: int64
                      description: Last update ID.
                      x-description-cn: 最后更新 ID.
                    symbol:
                      type: string
                      example: BTCUSD_200626
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    bidPrice:
                      type: string
                      example: "9650.1"
                      description: Best bid price.
                      x-description-cn: 最佳买价.
                    bidQty:
                      type: string
                      example: "16"
                      description: Best bid quantity.
                      x-description-cn: 最佳买量.
                    askPrice:
                      type: string
                      example: "9650.3"
                      description: Best ask price.
                      x-description-cn: 最佳卖价.
                    askQty:
                      type: string
                      example: "7"
                      description: Best ask quantity.
                      x-description-cn: 最佳卖量.
                    time:
                      type: integer
                      example: 1591257300345
                      format: int64
                      description: Time
                      x-description-cn: 时间
  /dapi/v1/ticker/price:
    get:
      summary: Symbol Price Ticker
      x-summary-cn: 最新价格
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回最近价格
      tags:
        - market-data
      operationId: symbolPriceTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#symbol-price-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/symbolPriceTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/symbol_price_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/symbol_price_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/SymbolPriceTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/SymbolPriceTicker/SymbolPriceTicker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/SymbolPriceTickerExample.php
      x-weight: "**1** for a single symbol, **2** when the symbol parameter is omitted"
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD_200626
          description: Symbol
          x-description-cn: 交易对
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: Pair
          x-description-cn: 标的交易对
      x-parameters-notes: |-
        - Symbol and pair cannot be sent together
        - If a pair is sent,tickers for all symbols of the pair will be returned
        - If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
      x-parameters-notes-cn: |-
        - symbol 和 pair 不接受同时发送
        - 发送 pair的,返回pair对应所有正在交易的symbol数据
        - symbol,pair 都没有发送的,返回所有symbol数据
      responses:
        "200":
          description: Symbol Price Ticker
          x-description-cn: 交易对 价格 行情
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_200626
                      description: Trading symbol
                      x-description-cn: 交易对
                    ps:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    price:
                      type: string
                      example: "9647.8"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    time:
                      type: integer
                      example: 1591257246176
                      format: int64
                      description: Time
                      x-description-cn: 时间
  /futures/data/takerBuySellVol:
    get:
      summary: Taker Buy/Sell Volume
      x-summary-cn: 合约主动买卖量
      description: |-
        Taker Buy Volume: the total volume of buy orders filled by takers within
        the period.

        Taker Sell Volume: the total volume of sell orders filled by takers
        within the period.
      x-description-cn: |-
        主动买入量：展示单位时间内主动买盘（Taker吃单买入）的成交量。
        主动卖出量：展示单位时间内主动卖盘（Taker吃单卖出）的成交量。
      tags:
        - market-data
      operationId: takerBuySellVolume
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#taker-buy-sell-volume
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/takerBuySellVolume.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/taker_buy_sell_volume.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/taker_buy_sell_volume.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/TakerBuySellVolumeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/TakerBuySellVolume/TakerBuySellVolume.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/TakerBuySellVolumeExample.php
      x-ip-weight: 1
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
        - name: contractType
          in: query
          required: true
          schema:
            type: string
            example: PERPETUAL
            enum:
              - ALL
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Taker Buy/Sell Volume
          x-description-cn: 请参见英文说明：Taker Buy/Sell Volume
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    contractType:
                      type: string
                      example: CURRENT_QUARTER
                      description: Contract type.
                      x-description-cn: 合约类型.
                    takerBuyVol:
                      type: string
                      example: "387"
                      description: "unit: cont"
                      x-description-cn: "unit: cont"
                    takerSellVol:
                      type: string
                      example: "248"
                      description: "unit: cont"
                      x-description-cn: "unit: cont"
                    takerBuyVolValue:
                      type: string
                      example: "2342.1220"
                      description: "unit: base asset"
                      x-description-cn: "unit: base asset"
                    takerSellVolValue:
                      type: string
                      example: "4213.9800"
                      description: "unit: base asset"
                      x-description-cn: "unit: base asset"
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: Start time of the period, in milliseconds.
                      x-description-cn: 该周期的开始时间，单位为毫秒。
  /dapi/v1/ping:
    get:
      summary: Test Connectivity
      x-summary-cn: 测试服务器连通性 PING
      description: Test connectivity to the Rest API.
      x-description-cn: 测试能否联通
      tags:
        - market-data
      operationId: testConnectivity
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#test-connectivity
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/testConnectivity.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/test_connectivity.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/test_connectivity.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/TestConnectivityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/TestConnectivity/TestConnectivity.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/TestConnectivityExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: OK
          x-description-cn: 成功
  /dapi/v1/ticker/24hr:
    get:
      summary: 24hr Ticker Price Change Statistics
      x-summary-cn: 24hr价格变动情况
      description: 24 hour rolling window price change statistics.
      x-description-cn: 请注意,不携带symbol参数会返回全部交易对数据,不仅数据庞大,而且权重极高
      tags:
        - market-data
      operationId: ticker24hrPriceChangeStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#ticker24hr-price-change-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/ticker24hrPriceChangeStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/ticker24hr_price_change_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/ticker24hr_price_change_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/Ticker24hrPriceChangeStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/Ticker24hrPriceChangeStatistics/Ticker24hrPriceChangeStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/Ticker24hrPriceChangeStatisticsExample.php
      x-weight: |-
        **1** for a single symbol, **40** when the symbol parameter is omitted
        **Careful** when accessing this with no symbol.
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: Pair
          x-description-cn: 标的交易对
      x-parameters-notes: |-
        - Symbol and pair cannot be sent together
        - If a pair is sent,tickers for all symbols of the pair will be returned
        - If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
      x-parameters-notes-cn: |-
        - symbol 和 pair 不接受同时发送
        - 发送 pair的,返回pair对应所有正在交易的symbol数据
        - symbol,pair 都没有发送的,返回所有symbol数据
      responses:
        "200":
          description: 24hr Ticker Price Change Statistics
          x-description-cn: 24hr 行情 价格 修改Statistics
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    priceChange:
                      type: string
                      example: "136.6"
                      description: Absolute price change in the 24h window.
                      x-description-cn: 24 小时窗口内绝对价格变化。
                    priceChangePercent:
                      type: string
                      example: "1.436"
                      description: Percentage price change in the 24h window.
                      x-description-cn: 24 小时窗口内价格变化百分比。
                    weightedAvgPrice:
                      type: string
                      example: "9547.3"
                      description: Weighted average price in the 24h window.
                      x-description-cn: 24 小时窗口内加权平均价格。
                    lastPrice:
                      type: string
                      example: "9651.6"
                      description: Latest traded price.
                      x-description-cn: 最新成交价。
                    lastQty:
                      type: string
                      example: "1"
                      description: Quantity of the latest trade.
                      x-description-cn: 最新一笔成交数量。
                    openPrice:
                      type: string
                      example: "9515.0"
                      description: Opening price of the 24h window.
                      x-description-cn: 24 小时窗口开盘价。
                    highPrice:
                      type: string
                      example: "9687.0"
                      description: Highest price in the 24h window.
                      x-description-cn: 24 小时窗口最高价。
                    lowPrice:
                      type: string
                      example: "9499.5"
                      description: Lowest price in the 24h window.
                      x-description-cn: 24 小时窗口最低价。
                    volume:
                      type: string
                      example: "494109"
                      description: Base asset volume in the 24h window.
                      x-description-cn: 24 小时窗口基础资产成交量。
                    baseVolume:
                      type: string
                      example: "5192.94797687"
                      description: Base asset volume.
                      x-description-cn: 基础资产成交量.
                    openTime:
                      type: integer
                      example: 1591170300000
                      format: int64
                      description: Start time of the 24h window (milliseconds).
                      x-description-cn: 24 小时窗口开始时间（毫秒）。
                    closeTime:
                      type: integer
                      example: 1591256718418
                      format: int64
                      description: End time of the 24h window (milliseconds).
                      x-description-cn: 24 小时窗口结束时间（毫秒）。
                    firstId:
                      type: integer
                      example: 600507
                      format: int64
                      description: First tradeId
                      x-description-cn: 首笔成交id
                    lastId:
                      type: integer
                      example: 697803
                      format: int64
                      description: Last tradeId
                      x-description-cn: 末笔成交id
                    count:
                      type: integer
                      example: 97297
                      format: int64
                      description: Total number of trades in the 24h window.
                      x-description-cn: 24 小时窗口内成交总笔数。
  /futures/data/topLongShortAccountRatio:
    get:
      summary: Top Trader Long/Short Account Ratio
      x-summary-cn: 大户账户数多空比
      description: |-
        The proportion of net long and net short accounts to total accounts of
        the top 20% users with the highest margin balance. Each account is
        counted once only.

        Long Account % = Accounts of top traders with net long positions / Total
        accounts of top traders with open positions

        Short Account % = Accounts of top traders with net short positions /
        Total accounts of top traders with open positions

        Long/Short Ratio (Accounts) = Long Account % / Short Account %
      x-description-cn: |-
        持仓大户的净持仓多头和空头账户数占比，大户指保证金余额排名前20%的用户。一个账户记一次。
        多仓账户数比例 = 持多仓大户数 / 总持仓大户数
        空仓账户数比例 = 持空仓大户数 / 总持仓大户数
        多空账户数比值 = 多仓账户数比例 / 空仓账户数比例
      tags:
        - market-data
      operationId: topTraderLongShortRatioAccounts
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#top-trader-long-short-ratio-accounts
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/topTraderLongShortRatioAccounts.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/top_trader_long_short_ratio_accounts.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/top_trader_long_short_ratio_accounts.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/TopTraderLongShortRatioAccountsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/TopTraderLongShortRatioAccounts/TopTraderLongShortRatioAccounts.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/TopTraderLongShortRatioAccountsExample.php
      x-ip-weight: 1
      x-security-type: Accounts
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
          description: Pair
          x-description-cn: 标的交易对
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
        - name: contractType
          in: query
          required: false
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
          description: Contract type filter. If omitted, returns aggregated data across all contract types.
          x-description-cn: 合约类型过滤。若不填，则返回所有合约类型的汇总数据。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Top Trader Long/Short Ratio
          x-description-cn: Top 交易r Long/Short Ratio
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    longShortRatio:
                      type: string
                      example: "1.8105"
                      description: Long/short ratio.
                      x-description-cn: 多空比.
                    longAccount:
                      type: string
                      example: "0.6442"
                      description: 64.42%
                      x-description-cn: 64.42%
                    shortAccount:
                      type: string
                      example: "0.3558"
                      description: 35.58%
                      x-description-cn: 35.58%
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /futures/data/topLongShortPositionRatio:
    get:
      summary: Top Trader Long/Short Position Ratio
      x-summary-cn: 大户持仓量多空比
      description: |-
        The proportion of net long and net short positions to total open
        positions of the top 20% users with the highest margin balance.

        Long Position % = Long positions of top traders / Total open positions
        of top traders

        Short Position % = Short positions of top traders / Total open positions
        of top traders

        Long/Short Ratio (Positions) = Long Position % / Short Position %
      x-description-cn: |-
        大户的多头和空头总持仓量占比，大户指保证金余额排名前20%的用户。
        多仓持仓量比例 = 大户多仓持仓量 / 大户总持仓量
        空仓持仓量比例 = 大户空仓持仓量 / 大户总持仓量
        多空持仓量比值 = 多仓持仓量比例 / 空仓持仓量比例
      tags:
        - market-data
      operationId: topTraderLongShortRatioPositions
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/market-data#top-trader-long-short-ratio-positions
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/MarketDataApi/topTraderLongShortRatioPositions.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/market_data_api/top_trader_long_short_ratio_positions.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/MarketData/top_trader_long_short_ratio_positions.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/marketdata/TopTraderLongShortRatioPositionsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/MarketDataAPI/TopTraderLongShortRatioPositions/TopTraderLongShortRatioPositions.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/marketdata/TopTraderLongShortRatioPositionsExample.php
      x-ip-weight: 1
      x-security-type: Positions
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSD
        - name: period
          in: query
          required: true
          schema:
            type: string
            example: 5m
            enum:
              - 5m
              - 15m
              - 30m
              - 1h
              - 2h
              - 4h
              - 6h
              - 12h
              - 1d
        - name: contractType
          in: query
          required: false
          schema:
            type: string
            example: PERPETUAL
            enum:
              - PERPETUAL
              - CURRENT_QUARTER
              - NEXT_QUARTER
          description: Contract type filter. If omitted, returns aggregated data across all contract types.
          x-description-cn: 合约类型过滤。若不填，则返回所有合约类型的汇总数据。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 500
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
      x-parameters-notes: |-
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
      responses:
        "200":
          description: Top Trader Long/Short Ratio
          x-description-cn: Top 交易r Long/Short Ratio
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    longShortRatio:
                      type: string
                      example: "0.7869"
                      description: Long/short ratio.
                      x-description-cn: 多空比.
                    longPosition:
                      type: string
                      example: "0.6442"
                      description: 64.42%
                      x-description-cn: 64.42%
                    shortPosition:
                      type: string
                      example: "0.4404"
                      description: 44.04%
                      x-description-cn: 44.04%
                    timestamp:
                      type: integer
                      example: 1592870400000
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /dapi/v1/userTrades:
    get:
      summary: Account Trade List (USER_DATA)
      x-summary-cn: 账户成交历史 (USER_DATA)
      description: Get trades for a specific account and symbol.
      x-description-cn: 获取成交历史
      tags:
        - trade
      operationId: accountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/accountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/AccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/AccountTradeList/AccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/AccountTradeListExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "**20** with symbol，**40** with pair (after CM migration: **5** flat)"
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
            example: BTCUSD_200626
          description: Symbol
          x-description-cn: 交易对
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: pair
          x-description-cn: 标的交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Order ID
          x-description-cn: 订单号
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 6
            format: int64
          description: Trade id to fetch from. Default gets most recent trades.
          x-description-cn: 从该成交 ID 开始获取数据. 默认获取最近的成交数据.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 50
            maximum: 1000
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either symbol or pair must be sent
        - Symbol and pair cannot be sent together
        - Pair and fromId cannot be sent together
        - OrderId can only be sent together with symbol
        - If a pair is sent,tickers for all symbols of the pair will be returned
        - The parameter `fromId` cannot be sent with `startTime` or `endTime`
        - If startTime and endTime are both not sent, then the last 7 days' data will be returned.
        - The time between startTime and endTime cannot be longer than 7 days.
        - Only support querying trade in the past 3 months
      x-parameters-notes-cn: |-
        - symbol 或 pair 其中一个必传
        - symbol 和 pair 不可同时提供
        - fromId 和 pair 不可同时提供
        - orderId必须和symbol一起提供
        - 发送 pair的,返回pair对应所有正在交易的symbol数据
        - 参数 fromId 不能和startTime 与 endTime一起发送
        - 如果startTime 和 endTime 均未发送, 只会返回最近7天的数据。
        - startTime 和 endTime 的最大间隔为7天
        - 本接口仅支持最近3个月历史交易的查询
      responses:
        "200":
          description: Account Trade List
          x-description-cn: 账户 交易 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_200626
                      description: Trading symbol
                      x-description-cn: 交易对
                    id:
                      type: integer
                      example: 6
                      format: int64
                      description: positionId
                      x-description-cn: 持仓 ID
                    orderId:
                      type: integer
                      example: 28
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    side:
                      type: string
                      example: SELL
                      description: Trading side
                      x-description-cn: 买卖方向
                    price:
                      type: string
                      example: "8800"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    qty:
                      type: string
                      example: "1"
                      description: Quantity.
                      x-description-cn: 数量.
                    realizedPnl:
                      type: string
                      example: "0"
                      description: Realized PnL.
                      x-description-cn: 已实现盈亏.
                    marginAsset:
                      type: string
                      example: BTC
                      description: Margin asset.
                      x-description-cn: 保证金币种.
                    baseQty:
                      type: string
                      example: "0.01136364"
                      description: Base asset quantity. Populated for COIN-M symbols; returns "0" for USDⓈ-M symbols.
                      x-description-cn: 标的资产成交量。币本位合约交易对返回该值；U 本位合约交易对返回 "0"。
                    quoteQty:
                      type: string
                      example: "0"
                      description: Quote asset quantity. Populated for USDⓈ-M symbols; returns "0" for COIN-M symbols.
                      x-description-cn: 计价资产成交额。U 本位合约交易对返回该值；币本位合约交易对返回 "0"。
                    commission:
                      type: string
                      example: "0.00000454"
                      description: Transaction Fee (in Crypto)
                      x-description-cn: 交易手续费（以数字货币计）
                    commissionAsset:
                      type: string
                      example: BTC
                      description: Commission asset.
                      x-description-cn: 手续费资产.
                    time:
                      type: integer
                      example: 1590743483586
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    positionSide:
                      type: string
                      example: BOTH
                      description: Position side
                      x-description-cn: 持仓方向
                    buyer:
                      type: boolean
                      example: false
                      description: Whether the trade is a buy side for the account.
                      x-description-cn: 该成交对账户而言是否为买入方向.
                    maker:
                      type: boolean
                      example: false
                      description: Whether the account is maker in this trade.
                      x-description-cn: 该成交中账户是否为做市方.
  /dapi/v1/allOrders:
    get:
      summary: All Orders (USER_DATA)
      x-summary-cn: 查询所有订单(包括历史订单) (USER_DATA)
      description: |-
        Get all account orders; active, canceled, or filled.

        * These orders will not be found:
          * order status is CANCELED or EXPIRED AND order has NO filled trade AND created time + 3 days < current time
          * order create time + 90 days < current time
      x-description-cn: |-
        查询订单

        * 请注意，如果订单满足如下条件，不会被查询到：
          * 订单的最终状态为 CANCELED 或者 EXPIRED 并且 订单没有任何的成交记录 并且 订单生成时间 + 3天 < 当前时间
          * 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: allOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#all-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/allOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/all_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/all_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/AllOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/AllOrders/AllOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/AllOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "**20** with symbol, **40** with pair (after CM migration: **5** flat)"
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
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: Pair
          x-description-cn: 标的交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1917641
            format: int64
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 50
            maximum: 100
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `symbol` or `pair` must be sent.
        - `pair` can't be sent with `orderId`
        - If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
        - If orderId is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - The query time period must be less then 7 days( default as the recent 7 days).
      x-parameters-notes-cn: |-
        - `symbol` 或 `pair`必须传一个，不能同时传
        - `pair`和`orderId`不能一起传
        - 如果设置了`orderId`，将返回在此`orderId`之后的订单，否则会返回最近的订单
        - 查询时间范围最大不得超过7天
        - 默认查询最近7天内的数据
      responses:
        "200":
          description: All Orders
          x-description-cn: All 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    avgPrice:
                      type: string
                      example: "0.0"
                      description: Average execution price
                      x-description-cn: 平均价格
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    cumBase:
                      type: string
                      example: "0"
                      description: Cumulative base asset amount.
                      x-description-cn: 累计基础资产数量.
                    cumQuote:
                      type: string
                      example: "0"
                      description: Cumulative quote asset amount.
                      x-description-cn: 成交金额(计价币种).
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed quantity
                      x-description-cn: 执行数量
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    origQty:
                      type: string
                      example: "0.40"
                      description: Original order quantity
                      x-description-cn: 原始委托数量
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Original order type.
                      x-description-cn: 原始订单类型.
                    price:
                      type: string
                      example: "0"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Whether the order is reduce-only.
                      x-description-cn: 是否为只减仓订单.
                    side:
                      type: string
                      example: BUY
                      description: Trading side
                      x-description-cn: 买卖方向
                    positionSide:
                      type: string
                      example: SHORT
                      description: Position side
                      x-description-cn: 持仓方向
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    timeInForce:
                      type: string
                      example: GTD
                      description: Time in force
                      x-description-cn: 有效方式
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Order type.
                      x-description-cn: 订单类型.
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
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
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
                    goodTillDate:
                      type: integer
                      example: 1579385751000
                      format: int64
                      description: order pre-set auto cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
  /dapi/v1/countdownCancelAll:
    post:
      summary: Auto-Cancel All Open Orders (TRADE)
      x-summary-cn: 倒计时撤销所有订单 (TRADE)
      description: |-
        Cancel all open orders of the specified symbol at the end of the
        specified countdown. This rest endpoint means to ensure your open orders
        are canceled in case of an outage. The endpoint should be called
        repeatedly as heartbeats so that the existing countdown time can be
        canceled and repalced by a new one. The system will check all countdowns
        **approximately every 10 milliseconds**, so please note that sufficient
        redundancy should be considered when using this function. We do not
        recommend setting the countdown time to be too precise or too small.


        * Example usage:

        Call this endpoint at 30s intervals with an countdownTime of 120000
        (120s).

        If this endpoint is not called within 120 seconds, all your orders of
        the specified symbol will be automatically canceled.

        If this endpoint is called with an countdownTime of 0, the countdown
        timer will be stopped.
      x-description-cn: |-
        倒计时撤销所有订单。该接口可以被用于确保在发生故障时撤销指定symbol上的所有挂单。
        在使用这个功能时,接口应像心跳一样在倒计时内被反复调用,以便可以取消既有的倒计时并开始新的倒数计时设置。系统会**大约每10毫秒**检查一次所有倒计时情况,因此请注意,使用此功能时应考虑足够的冗余。

        我们不建议将倒记时设置得太精确或太小。


        * 用法示例：

        以30s的间隔重复此接口,每次倒计时countdownTime设置为120000(120s)。

        如果在120秒内未再次调用此接口,则您指定symbol上的所有挂单都会被自动撤销。

        如果在120秒内以将countdownTime设置为0,则倒数计时器将终止,自动撤单功能取消。
      tags:
        - trade
      operationId: autoCancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#auto-cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/autoCancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/auto_cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/auto_cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/AutoCancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/AutoCancelAllOpenOrders/AutoCancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/AutoCancelAllOpenOrdersExample.php
      x-ip-weight: 10
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - countdownTime
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSD_200925
                countdownTime:
                  type: integer
                  example: 1000
                  format: int64
                  description: countdown time, 1000 for 1 second. 0 to cancel the timer
                  x-description-cn: 倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。
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
      responses:
        "200":
          description: Auto-Cancel All Open Orders
          x-description-cn: Auto-取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
                  countdownTime:
                    type: string
                    example: "100000"
                    description: Countdown cancellation time in milliseconds.
                    x-description-cn: 倒计时撤单时间（毫秒）.
  /dapi/v1/allOpenOrders:
    delete:
      summary: Cancel All Open Orders (TRADE)
      x-summary-cn: 撤销全部订单 (TRADE)
      description: Cancel All Open Orders
      x-description-cn: 撤销全部订单
      tags:
        - trade
      operationId: cancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/cancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/CancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/CancelAllOpenOrders/CancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/CancelAllOpenOrdersExample.php
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
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All Open Orders
          x-description-cn: 取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
                    description: Message details.
                    x-description-cn: 消息详情.
  /dapi/v1/batchOrders:
    delete:
      summary: Cancel Multiple Orders (TRADE)
      x-summary-cn: 批量撤销订单 (TRADE)
      description: Cancel Multiple Orders
      x-description-cn: 批量撤销订单
      tags:
        - trade
      operationId: cancelMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#cancel-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/cancelMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/cancel_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/cancel_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/CancelMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/CancelMultipleOrders/CancelMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/CancelMultipleOrdersExample.php
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
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: orderIdList
          in: query
          required: false
          schema:
            type: array
            maxItems: 10
            example:
              - 1234567
              - 2345678
            items:
              type: integer
              format: int64
              example: 1234567
          description: Order IDs to cancel.
          x-description-cn: 需要撤销的系统订单号列表.
        - name: origClientOrderIdList
          in: query
          required: false
          schema:
            type: array
            maxItems: 10
            example:
              - my_id_1
              - my_id_2
            items:
              type: string
              example: my_id_1
          description: Original client order IDs to cancel.
          x-description-cn: 需要撤销的用户自定义订单号列表.
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderIdList` or `origClientOrderIdList ` must be sent."
      x-parameters-notes-cn: "- `orderIdList` 与 `origClientOrderIdList` 必须至少发送一个,不可同时发送"
      responses:
        "200":
          description: Cancel Multiple Orders
          x-description-cn: 取消Multiple 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    clientOrderId:
                      type: string
                      example: myOrder1
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    cumQty:
                      type: string
                      example: "0"
                      description: Cumulative filled quantity.
                      x-description-cn: 累计成交数量.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed quantity
                      x-description-cn: 执行数量
                    orderId:
                      type: integer
                      example: 283194212
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    origQty:
                      type: string
                      example: "11"
                      description: Original order quantity
                      x-description-cn: 原始委托数量
                    price:
                      type: string
                      example: "0"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Whether the order is reduce-only.
                      x-description-cn: 是否为只减仓订单.
                    side:
                      type: string
                      example: BUY
                      description: Trading side
                      x-description-cn: 买卖方向
                    positionSide:
                      type: string
                      example: SHORT
                      description: Position side
                      x-description-cn: 持仓方向
                    status:
                      type: string
                      example: CANCELED
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force
                      x-description-cn: 有效方式
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Original order type.
                      x-description-cn: 原始订单类型.
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Order type.
                      x-description-cn: 订单类型.
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
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
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
                    updateTime:
                      type: integer
                      example: 1571110484038
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
                    code:
                      type: integer
                      example: -2011
                      format: int64
                      description: API response code. "000000" indicates success.
                      x-description-cn: API 响应码。"000000" 表示成功。
                    msg:
                      type: string
                      example: Unknown order sent.
                      description: Message details.
                      x-description-cn: 消息详情.
    put:
      summary: Modify Multiple Orders (TRADE)
      x-summary-cn: 批量修改订单 (TRADE)
      description: Modify Multiple Orders
      x-description-cn: 批量修改订单
      tags:
        - trade
      operationId: modifyMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#modify-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/modifyMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/modify_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/modify_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ModifyMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ModifyMultipleOrders/ModifyMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ModifyMultipleOrdersExample.php
      x-ip-weight: 5
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
        - Parameter rules are same with `Modify Order`

        - Batch modify orders are processed concurrently, and the order of matching is not guaranteed.

        - The order of returned contents for batch modify orders is the same as the order of the order list.

        - One order can only be modfied for less than 10000 times

        - `modifyId` is an optional user-defined identifier passed through as-is; the server does not validate its
        uniqueness. If omitted, it is not included in the response.
      x-parameters-notes-cn: |-
        - 具体订单条件规则,与普通修改订单一致
        - 批量修改订单采取并发处理,不保证订单撮合顺序
        - 批量修改订单的返回内容顺序,与订单列表顺序一致
        - 同一订单被修改次数不能超过10000次
        - `modifyId` 为可选的用户自定义标识，服务端原样透传且不校验唯一性；不传时响应中不包含该字段。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - batchOrders
                - timestamp
              properties:
                batchOrders:
                  type: array
                  items:
                    type: object
                    required:
                      - symbol
                      - side
                      - timestamp
                    properties:
                      orderId:
                        type: integer
                        example: 20072994037
                        format: int64
                        description: Sub-order ID, required when clientOrderId is not sent.
                        x-description-cn: 子订单 ID,当clientOrderId未发送时必填.
                      origClientOrderId:
                        type: string
                        example: LJ9R4QZDihCaS8UAOOLpgW
                        description: >-
                          Client order ID, required when orderId is not sent. Only support letters, numbers and
                          underscores, and must be unique within 24 hours.
                        x-description-cn: 客户端订单 ID,当orderId未发送时必填.仅支持字母、数字和下划线，且在24小时内必须唯一。
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Trading symbol
                        x-description-cn: 交易对
                      side:
                        type: string
                        example: BUY
                        enum:
                          - BUY
                          - SELL
                        description: Trading side
                        x-description-cn: 买卖方向
                      quantity:
                        type: number
                        example: 1
                        format: float
                        description: >-
                          Order quantity, cannot be sent with closePosition=true. **After CM migration, this parameter
                          becomes mandatory** (each batch element must send both `price` and `quantity`).
                        x-description-cn: 订单数量,当closePosition=true时不能发送。**迁移后此参数变为必传**(批量中每一个元素都必须同时传 `price` 与 `quantity`)。
                      price:
                        type: number
                        example: 30005
                        format: float
                        description: >-
                          Latest token price. **After CM migration, this parameter becomes mandatory** (each batch
                          element must send both `price` and `quantity`).
                        x-description-cn: 代币最新价格。**迁移后此参数变为必传**(批量中每一个元素都必须同时传 `price` 与 `quantity`)。
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
                  description: order list. Max 5 orders
                  x-description-cn: 订单列表,最多支持5个订单
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
      responses:
        "200":
          description: Modify Multiple Orders
          x-description-cn: Modify Multiple 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 20072994037
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
                      example: LJ9R4QZDihCaS8UAOOLpgW
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
                      example: "30005"
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
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
                    updateTime:
                      type: integer
                      example: 1629182711600
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
                    code:
                      type: integer
                      example: -2022
                      format: int64
                      description: API response code. "000000" indicates success.
                      x-description-cn: API 响应码。"000000" 表示成功。
                    msg:
                      type: string
                      example: ReduceOnly Order is rejected.
                      description: Message details.
                      x-description-cn: 消息详情.
    post:
      summary: Place Multiple Orders (TRADE)
      x-summary-cn: 批量下单 (TRADE)
      description: |-
        Place multiple orders

        * Parameter rules are same with `New Order`
        * Batch orders are processed concurrently, and the order of matching is not guaranteed.
        * The order of returned contents for batch orders is the same as the order of the order list.
      x-description-cn: |-
        批量下单
        * 具体订单条件规则,与普通下单一致
        * 批量下单采取并发处理,不保证订单撮合顺序
        * 批量下单的返回内容顺序,与订单列表顺序一致
      tags:
        - trade
      operationId: placeMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#place-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/placeMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/place_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/place_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/PlaceMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/PlaceMultipleOrders/PlaceMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/PlaceMultipleOrdersExample.php
      x-ip-weight: 5
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
        - `batchOrders` must be a JSON array of order parameter objects.
        - Example:
          `/dapi/v1/batchOrders?batchOrders=[{"type":"LIMIT","timeInForce":"GTC","symbol":"BTCUSD_PERP","side":"BUY","price":"10001","quantity":"1"}]`
      x-parameters-notes-cn: |-
        - `batchOrders` 需传 JSON 数组格式的订单参数对象列表。
        - 示例：
          `/dapi/v1/batchOrders?batchOrders=[{"type":"LIMIT","timeInForce":"GTC","symbol":"BTCUSD_PERP","side":"BUY","price":"10001","quantity":"1"}]`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - batchOrders
                - timestamp
              properties:
                batchOrders:
                  type: array
                  items:
                    type: object
                    required:
                      - symbol
                      - side
                      - type
                      - quantity
                    properties:
                      symbol:
                        type: string
                        example: BTCUSD_PERP
                        description: Symbol
                        x-description-cn: 交易对
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
                          Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge
                          Mode.
                        x-description-cn: 持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
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
                          `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`) are no longer accepted on a per-element basis
                          and will return element-level `-4120`. Use the new `/dapi/v1/algoOrder` endpoint instead.**
                        x-description-cn: >-
                          **迁移后,本接口对 stop
                          类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`)按元素级别拒绝,返回元素级
                          `-4120`。请改用新接口 `/dapi/v1/algoOrder`。**
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
                        example: 1
                        format: float
                        description: quantity measured by contract number
                        x-description-cn: 以合约数量计量的下单数量
                      reduceOnly:
                        type: string
                        example: "true"
                        default: "false"
                        enum:
                          - "true"
                          - "false"
                      price:
                        type: number
                        example: 10001
                        format: float
                        description: Order price
                        x-description-cn: 委托价格
                      newClientOrderId:
                        type: string
                        example: "1"
                        description: |-
                          A unique id among open orders. Automatically generated if
                          not sent. Can only be string following the rule:
                          `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                        x-description-cn: 用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                      stopPrice:
                        type: number
                        example: 9000
                        format: float
                        description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                        x-description-cn: 触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数
                      activationPrice:
                        type: number
                        example: 9020
                        format: float
                        description: |-
                          Used with `TRAILING_STOP_MARKET` orders, default as the
                          latest price(supporting different `workingType`)
                        x-description-cn: 追踪止损激活价格,仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)
                      callbackRate:
                        type: number
                        example: 1
                        format: float
                        minimum: 0.1
                        maximum: 4
                        description: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 4 where 1 for 1%
                        x-description-cn: 追踪止损回调比例,可取值范围[0.1, 4],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数
                      workingType:
                        type: string
                        example: MARK_PRICE
                        default: CONTRACT_PRICE
                        enum:
                          - MARK_PRICE
                          - CONTRACT_PRICE
                      priceProtect:
                        type: string
                        example: "false"
                        default: "false"
                        enum:
                          - "true"
                          - "false"
                        description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                        x-description-cn: 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数
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
                        description: only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can't be passed together with `price`
                        x-description-cn: 仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单可用; 不能与 `price` 同时传
                      selfTradePreventionMode:
                        type: string
                        example: EXPIRE_TAKER
                        default: EXPIRE_MAKER
                        enum:
                          - EXPIRE_TAKER
                          - EXPIRE_MAKER
                          - EXPIRE_BOTH
                        description: |-
                          `EXPIRE_TAKER`: expire taker order when STP triggers/
                          `EXPIRE_MAKER`: expire taker order when STP triggers/
                          `EXPIRE_BOTH`: expire both orders when STP triggers
                        x-description-cn: "`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`，默认`EXPIRE_MAKER`"
                  description: order list. Max 5 orders
                  x-description-cn: 订单列表,最多支持5个订单
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
      responses:
        "200":
          description: Place Multiple Orders
          x-description-cn: 下单Multiple 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    clientOrderId:
                      type: string
                      example: testOrder
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    cumQty:
                      type: string
                      example: "0"
                      description: Cumulative filled quantity.
                      x-description-cn: 累计成交数量.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed quantity
                      x-description-cn: 执行数量
                    orderId:
                      type: integer
                      example: 22542179
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    origQty:
                      type: string
                      example: "10"
                      description: Original order quantity
                      x-description-cn: 原始委托数量
                    price:
                      type: string
                      example: "0"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Whether the order is reduce-only.
                      x-description-cn: 是否为只减仓订单.
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
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "0"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force
                      x-description-cn: 有效方式
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Order type.
                      x-description-cn: 订单类型.
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Original order type.
                      x-description-cn: 原始订单类型.
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
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
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
                    code:
                      type: integer
                      example: -2022
                      format: int64
                      description: API response code. "000000" indicates success.
                      x-description-cn: API 响应码。"000000" 表示成功。
                    msg:
                      type: string
                      example: ReduceOnly Order is rejected.
                      description: Message details.
                      x-description-cn: 消息详情.
  /dapi/v1/order:
    delete:
      summary: Cancel Order (TRADE)
      x-summary-cn: 撤销订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 撤销订单
      tags:
        - trade
      operationId: cancelOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#cancel-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/cancelOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/cancel_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/cancel_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/CancelOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/CancelOrder/CancelOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/CancelOrderExample.php
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
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 283194212
            format: int64
          description: Order ID
          x-description-cn: 系统订单号
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: myOrder1
          description: Client order ID
          x-description-cn: 用户自定义的订单号
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 与 `origClientOrderId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel Order
          x-description-cn: 取消订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: myOrder1
                    description: Client order ID.
                    x-description-cn: 客户端订单 ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cumulative filled quantity.
                    x-description-cn: 累计成交数量.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed quantity
                    x-description-cn: 执行数量
                  orderId:
                    type: integer
                    example: 283194212
                    format: int64
                    description: Sub-order ID
                    x-description-cn: 子订单 ID
                  origQty:
                    type: string
                    example: "11"
                    description: Original order quantity
                    x-description-cn: 原始委托数量
                  price:
                    type: string
                    example: "0"
                    description: Latest token price.
                    x-description-cn: 代币最新价格。
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Whether the order is reduce-only.
                    x-description-cn: 是否为只减仓订单.
                  side:
                    type: string
                    example: BUY
                    description: Trading side
                    x-description-cn: 买卖方向
                  positionSide:
                    type: string
                    example: SHORT
                    description: Position side
                    x-description-cn: 持仓方向
                  status:
                    type: string
                    example: CANCELED
                    description: Status.
                    x-description-cn: 订单状态
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force
                    x-description-cn: 有效方式
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Original order type.
                    x-description-cn: 原始订单类型.
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Order type.
                    x-description-cn: 订单类型.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  updateTime:
                    type: integer
                    example: 1571110484038
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
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
                  priceMatch:
                    type: string
                    example: NONE
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
    put:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#modify-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/modifyOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/modify_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/modify_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ModifyOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ModifyOrder/ModifyOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ModifyOrderExample.php
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
      x-parameters-notes: >-
        - Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.

        - Either `quantity` or `price` must be sent. *(After CM migration, both `quantity` and `price` are required.)*

        - When the new `quantity` or `price` doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be
        rejected and the order will stay as it is.

        - However the order will be cancelled by the amendment in the following situations:
          - when the order is in partially filled status and the new `quantity` <= `executedQty`
          - When the order is `GTX` and the new price will cause it to be executed immediately
        - One order can only be modfied for less than 10000 times
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
        - `quantity` 与 `price` 必须至少发送一个。*(迁移后,`quantity` 与 `price` 必须同时传。)*
        - 当新订单的`quantity` 或 `price`不满足PRICE_FILTER / PERCENT_FILTER / LOT_SIZE限制，修改会被拒绝，原订单依旧被保留
        - 订单会在下列情况下被取消：
          - 原订单被部分执行且新订单`quantity` <= `executedQty`
          - 原订单是`GTX`，新订单的价格会导致订单立刻执行
        - 同一订单修改次数最多10000次
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - timestamp
              properties:
                orderId:
                  type: integer
                  example: 1
                  format: int64
                  description: Order ID
                  x-description-cn: 系统订单号
                origClientOrderId:
                  type: string
                  example: "1"
                  description: Client order ID
                  x-description-cn: 用户自定义的订单号
                symbol:
                  type: string
                  example: BTCUSD_PERP
                  description: Symbol
                  x-description-cn: 交易对
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
                  description: >-
                    Order quantity, cannot be sent with `closePosition=true`. **After CM migration, this parameter
                    becomes mandatory** (must be sent together with `price`).
                  x-description-cn: 下单数量,使用`closePosition`不支持此参数。**迁移后此参数变为必传**(需与 `price` 同时传)。
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: >-
                    Order price. **After CM migration, this parameter becomes mandatory** (must be sent together with
                    `quantity`).
                  x-description-cn: 委托价格。**迁移后此参数变为必传**(需与 `quantity` 同时传)。
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
                  x-description-cn: 盘口价格下单模式,仅对`LIMIT`/`STOP`/`TAKE_PROFIT`订单有效,与`price`参数互斥
                modifyId:
                  type: integer
                  example: 1
                  format: int64
                  description: >-
                    User-defined modification identifier, returned as-is in the response. Optional; not validated for
                    uniqueness.
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
      responses:
        "200":
          description: Modify Order
          x-description-cn: Modify 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 20072994037
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
                    example: LJ9R4QZDihCaS8UAOOLpgW
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
                    example: "30005"
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
                  priceMatch:
                    type: string
                    example: NONE
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
                  updateTime:
                    type: integer
                    example: 1629182711600
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
    post:
      summary: New Order (TRADE)
      x-summary-cn: 下单 (TRADE)
      description: Send in a new order.
      x-description-cn: 发送新订单.
      tags:
        - trade
      operationId: newOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/NewOrder/NewOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/NewOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M)
        0 on IP rate limit(x-mbx-used-weight-1m)
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
        - Additional mandatory parameters based on `type`:
          - Order with type `STOP`, parameter `timeInForce` can be sent ( default `GTC`).
          - Order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`).
          - Condition orders will be triggered when:
          - If parameter`priceProtect`is sent as true:
          - when price reaches the `stopPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
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

          - For `TRAILING_STOP_MARKET`, if you got such error code. > `{"code": -2021, "msg": "Order would immediately trigger."}` > means that the parameters you send do not meet the following requirements:
          - BUY: `activationPrice` should be smaller than latest price.
          - SELL: `activationPrice` should be larger than latest price.
          - If `newOrderRespType ` is sent as `RESULT` :
          - `MARKET` order: the final FILLED result of the order will be return directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
          - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:
          - Follow the same rules for condition orders.
          - If triggered,**close all** current long position( if `SELL`) or current short position( if `BUY`).
          - Cannot be used with `quantity` parameter
          - Cannot be used with `reduceOnly` parameter
          - In Hedge Mode,cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side

          - `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC`.
      x-parameters-notes-cn: |-
        - 根据 order `type`的不同,某些参数强制要求,具体如下:
        - 条件单的触发必须:
        - 如果订单参数`priceProtect`为true:
        - 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
        - 触发保护阈值请参考接口`GET /dapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
        - `STOP`, `STOP_MARKET` 止损单:
        - 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
        - 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
        - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单:
        - 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
        - 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
        - `TRAILING_STOP_MARKET` 跟踪止损单:
        - 买入: 当合约价格/标记价格区间最低价格低于激活价格`activationPrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。
        - 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activationPrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。
        - `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}` 表示订单不满足以下条件:
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
        - 双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持`SELL`
        - `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`时生效.
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
                  example: BTCUSD_200925
                  description: Symbol
                  x-description-cn: 交易对
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
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
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
                    **After CM migration, stop-type values (`STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`,
                    `TRAILING_STOP_MARKET`) are no longer accepted by this endpoint and will return `-4120`. Use the new
                    `/dapi/v1/algoOrder` endpoint instead.**
                  x-description-cn: >-
                    **迁移后,本接口不再接受 stop
                    类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`),会返回
                    `-4120`。请改用新接口 `/dapi/v1/algoOrder`。**
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: |-
                    "true" or "false". Cannot be sent in Hedge
                    Mode; cannot be sent with `closePosition`=`true`(Close-All)
                  x-description-cn: "`true`, `false`; 非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。"
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: quantity measured by contract number, Cannot be sent with `closePosition`=`true`
                  x-description-cn: 以合约数量计量的下单数量，使用`closePosition`不支持此参数。
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order price
                  x-description-cn: 委托价格
                newClientOrderId:
                  type: string
                  example: "1"
                  description: |-
                    A unique id among open orders. Automatically generated if
                    not sent. Can only be string following the rule:
                    `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                  x-description-cn: 用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                stopPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                  x-description-cn: 触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数
                closePosition:
                  type: string
                  example: "true"
                  description: "`true`, `false`；Close-All,used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`."
                  x-description-cn: |-
                    `true`,
                    `false`；触发后全部平仓,仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果,不与`reduceOnly`
                    合用
                activationPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: |-
                    Used with `TRAILING_STOP_MARKET` orders, default as the
                    latest price(supporting different `workingType`)
                  x-description-cn: 追踪止损激活价格,仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)
                callbackRate:
                  type: number
                  example: "5000.0"
                  format: float
                  description: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%
                  x-description-cn: 追踪止损回调比例,可取值范围[0.1, 10],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数
                timeInForce:
                  type: string
                  example: GTC
                  enum:
                    - GTC
                    - IOC
                    - FOK
                    - GTX
                workingType:
                  type: string
                  example: MARK_PRICE
                  enum:
                    - MARK_PRICE
                    - CONTRACT_PRICE
                  default: CONTRACT_PRICE
                  description: '''stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE".'
                  x-description-cn: '"stopPrice 触发类型: `MARK_PRICE`(标记价格), `CONTRACT_PRICE`(合约最新价).'
                priceProtect:
                  type: string
                  example: "false"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: |-
                    "true" or "false". Used with
                    `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET`
                    orders.
                  x-description-cn: |-
                    条件单触发保护："true","false", 默认"false". 仅 `STOP`, `STOP_MARKET`,
                    `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数
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
                  description: |-
                    only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order;
                    Can't be passed together with `price`
                  x-description-cn: 仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单可用，不能与 `price` 同时传
                selfTradePreventionMode:
                  type: string
                  example: EXPIRE_TAKER
                  default: EXPIRE_MAKER
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: |-
                    `EXPIRE_TAKER`: expire taker order when STP triggers/
                    `EXPIRE_MAKER`: expire taker order when STP triggers/
                    `EXPIRE_BOTH`: expire both orders when STP triggers
                  x-description-cn: "`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`默认`EXPIRE_MAKER`"
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
      responses:
        "200":
          description: New Order
          x-description-cn: New 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: testOrder
                    description: Client order ID.
                    x-description-cn: 客户端订单 ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cumulative filled quantity.
                    x-description-cn: 累计成交数量.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed quantity
                    x-description-cn: 执行数量
                  orderId:
                    type: integer
                    example: 22542179
                    format: int64
                    description: Sub-order ID
                    x-description-cn: 子订单 ID
                  origQty:
                    type: string
                    example: "10"
                    description: Original order quantity
                    x-description-cn: 原始委托数量
                  price:
                    type: string
                    example: "0"
                    description: Latest token price.
                    x-description-cn: 代币最新价格。
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
                    example: SELL
                    description: Trading side
                    x-description-cn: 买卖方向
                  positionSide:
                    type: string
                    example: SHORT
                    description: Position side
                    x-description-cn: 持仓方向
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  stopPrice:
                    type: string
                    example: "0"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force
                    x-description-cn: 有效方式
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Order type.
                    x-description-cn: 订单类型.
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Original order type.
                    x-description-cn: 原始订单类型.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
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
                  priceMatch:
                    type: string
                    example: NONE
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
    get:
      summary: Query Order (USER_DATA)
      x-summary-cn: 查询订单 (USER_DATA)
      description: |-
        Check an order's status.

        * These orders will not be found:
          * order status is CANCELED or EXPIRED AND order has NO filled trade AND created time + 3 days < current time
          * order create time + 90 days < current time
      x-description-cn: |-
        查询订单状态

        * 请注意，如果订单满足如下条件，不会被查询到：
          * 订单的最终状态为 CANCELED 或者 EXPIRED 并且 订单没有任何的成交记录 并且 订单生成时间 + 3天 < 当前时间
          * 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: queryOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#query-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/queryOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/query_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/query_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/QueryOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/QueryOrder/QueryOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/QueryOrderExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Order ID
          x-description-cn: 系统订单号
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Client order ID
          x-description-cn: 用户自定义的订单号
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- 至少需要发送 `orderId` 与 `origClientOrderId`中的一个"
      responses:
        "200":
          description: Order
          x-description-cn: 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgPrice:
                    type: string
                    example: "0.0"
                    description: Average execution price
                    x-description-cn: 平均价格
                  clientOrderId:
                    type: string
                    example: abc
                    description: Client order ID.
                    x-description-cn: 客户端订单 ID.
                  cumBase:
                    type: string
                    example: "0"
                    description: Cumulative base asset amount.
                    x-description-cn: 累计基础资产数量.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed quantity
                    x-description-cn: 执行数量
                  orderId:
                    type: integer
                    example: 1573346959
                    format: int64
                    description: Sub-order ID
                    x-description-cn: 子订单 ID
                  origQty:
                    type: string
                    example: "0.40"
                    description: Original order quantity
                    x-description-cn: 原始委托数量
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Original order type.
                    x-description-cn: 原始订单类型.
                  price:
                    type: string
                    example: "0"
                    description: Latest token price.
                    x-description-cn: 代币最新价格。
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Whether the order is reduce-only.
                    x-description-cn: 是否为只减仓订单.
                  side:
                    type: string
                    example: BUY
                    description: Trading side
                    x-description-cn: 买卖方向
                  positionSide:
                    type: string
                    example: SHORT
                    description: Position side
                    x-description-cn: 持仓方向
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: Time
                    x-description-cn: 时间
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force
                    x-description-cn: 有效方式
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Order type.
                    x-description-cn: 订单类型.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  updateTime:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
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
                  priceMatch:
                    type: string
                    example: NONE
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
  /dapi/v1/leverage:
    post:
      summary: Change Initial Leverage (TRADE)
      x-summary-cn: 调整开仓杠杆 (TRADE)
      description: |-
        Change user's initial leverage in the specific symbol market.

        For Hedge Mode, LONG and SHORT positions of one symbol use the same
        initial leverage and share a total notional value.
      x-description-cn: 调整用户在指定symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数,共享允许的最大交易标的资产数量。
      tags:
        - trade
      operationId: changeInitialLeverage
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#change-initial-leverage
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/changeInitialLeverage.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/change_initial_leverage.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/change_initial_leverage.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ChangeInitialLeverageExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ChangeInitialLeverage/ChangeInitialLeverage.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ChangeInitialLeverageExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - leverage
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSD_200925
                  description: Symbol
                  x-description-cn: 交易对
                leverage:
                  type: integer
                  example: 1
                  format: int64
                  description: "target initial leverage: int from 1 to 125"
                  x-description-cn: 目标杠杆倍数
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
      responses:
        "200":
          description: Change Initial Leverage
          x-description-cn: 修改Initial Leverage
          content:
            application/json:
              schema:
                type: object
                properties:
                  leverage:
                    type: integer
                    example: 21
                    format: int64
                    description: Leverage value.
                    x-description-cn: 杠杆倍数.
                  maxQty:
                    type: string
                    example: "1000"
                    description: maximum quantity of base asset
                    x-description-cn: 数量上限, 最大数量
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
  /dapi/v1/marginType:
    post:
      summary: Change Margin Type (TRADE)
      x-summary-cn: 变换逐全仓模式 (TRADE)
      description: |-
        Change user's margin type in the specific symbol market.For Hedge Mode,
        LONG and SHORT positions of one symbol use the same margin type.

        With ISOLATED margin type, margins of the LONG and SHORT positions are
        isolated from each other.
      x-description-cn: |-
        变换用户在指定 symbol 合约上的保证金模式：逐仓或全仓。
        不同持仓方向上使用相同的保证金模式。双向持仓模式下的逐仓,`LONG` 与 `SHORT`使用独立的逐仓仓位。
      tags:
        - trade
      operationId: changeMarginType
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#change-margin-type
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/changeMarginType.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/change_margin_type.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/change_margin_type.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ChangeMarginTypeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ChangeMarginType/ChangeMarginType.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ChangeMarginTypeExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - marginType
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSD_200925
                  description: Symbol
                  x-description-cn: 交易对
                marginType:
                  type: string
                  example: ISOLATED
                  enum:
                    - ISOLATED
                    - CROSSED
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
      responses:
        "200":
          description: Change Margin Type
          x-description-cn: 修改杠杆 类型
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  msg:
                    type: string
                    example: success
                    description: Message details.
                    x-description-cn: 消息详情.
  /dapi/v1/openOrders:
    get:
      summary: Current All Open Orders (USER_DATA)
      x-summary-cn: 查看当前全部挂单 (USER_DATA)
      description: Get all open orders on a symbol. **Careful** when accessing this with no symbol.
      x-description-cn: 查看当前全部挂单
      tags:
        - trade
      operationId: currentAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#current-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/currentAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/current_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/current_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/CurrentAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/CurrentAllOpenOrders/CurrentAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/CurrentAllOpenOrdersExample.php
      x-ip-weight: null
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "**1** for a single symbol, **40** for mutltiple symbols"
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
            example: BTCUSD_200925
          description: Symbol. **After CM migration, an invalid `symbol` returns `-1121` (previously a silent `200`).**
          x-description-cn: 交易对。**迁移后,传入非法 `symbol` 会返回 `-1121`(此前为静默返回 `200`)。**
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
          description: Pair
          x-description-cn: 标的交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Current All Open Orders
          x-description-cn: 当前 All 未完成订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    avgPrice:
                      type: string
                      example: "0.0"
                      description: Average execution price
                      x-description-cn: 平均价格
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    cumBase:
                      type: string
                      example: "0"
                      description: Cumulative base asset amount.
                      x-description-cn: 累计基础资产数量.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed quantity
                      x-description-cn: 执行数量
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    origQty:
                      type: string
                      example: "0.40"
                      description: Original order quantity
                      x-description-cn: 原始委托数量
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Original order type.
                      x-description-cn: 原始订单类型.
                    price:
                      type: string
                      example: "0"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Whether the order is reduce-only.
                      x-description-cn: 是否为只减仓订单.
                    side:
                      type: string
                      example: BUY
                      description: Trading side
                      x-description-cn: 买卖方向
                    positionSide:
                      type: string
                      example: SHORT
                      description: Position side
                      x-description-cn: 持仓方向
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force
                      x-description-cn: 有效方式
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Order type.
                      x-description-cn: 订单类型.
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
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
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
  /dapi/v1/orderAmendment:
    get:
      summary: Get Order Modify History (USER_DATA)
      x-summary-cn: 查询订单修改历史 (USER_DATA)
      description: Get order modification history
      x-description-cn: 查询订单修改历史
      tags:
        - trade
      operationId: getOrderModifyHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#get-order-modify-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/getOrderModifyHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/get_order_modify_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/get_order_modify_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/GetOrderModifyHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/GetOrderModifyHistory/GetOrderModifyHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/GetOrderModifyHistoryExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSD_PERP
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 20072994037
            format: int64
          description: Order ID
          x-description-cn: 系统订单号
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: LJ9R4QZDihCaS8UAOOLpgW
          description: Client order ID
          x-description-cn: 用户自定义的订单号
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in ms to get modification history from INCLUSIVE
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms to get modification history until INCLUSIVE
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 50
            maximum: 100
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.
        - Order modify history longer than 3 month is not avaliable
      x-parameters-notes-cn: |-
        - 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 `orderId` 为准
        - 接口仅保留最近三个月订单修改历史
      responses:
        "200":
          description: Get Order Modify History
          x-description-cn: 获取订单 Modify 历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    amendmentId:
                      type: integer
                      example: 5363
                      format: int64
                      description: Order modification ID
                      x-description-cn: 修改记录号
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
                    orderId:
                      type: integer
                      example: 20072994037
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    clientOrderId:
                      type: string
                      example: LJ9R4QZDihCaS8UAOOLpgW
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    time:
                      type: integer
                      example: 1629184560899
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    amendment:
                      type: object
                      properties:
                        price:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "30004"
                              description: Before value.
                              x-description-cn: 之前的值.
                            after:
                              type: string
                              example: "30003.2"
                              description: After value.
                              x-description-cn: 之后的值.
                          description: Latest token price.
                          x-description-cn: 代币最新价格。
                        origQty:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "1"
                              description: Before value.
                              x-description-cn: 之前的值.
                            after:
                              type: string
                              example: "1"
                              description: After value.
                              x-description-cn: 之后的值.
                          description: Original order quantity
                          x-description-cn: 原始委托数量
                        count:
                          type: integer
                          example: 3
                          format: int64
                          description: Total number of trades in the 24h window.
                          x-description-cn: 24 小时窗口内成交总笔数。
                        modifyId:
                          type: integer
                          example: 123
                          format: int64
                          description: user-defined modification identifier, only returned if provided in the request
                          x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                      description: Order amendment details.
                      x-description-cn: 订单修改详情.
  /dapi/v1/positionMargin/history:
    get:
      summary: Get Position Margin Change History (TRADE)
      x-summary-cn: 逐仓保证金变动历史 (TRADE)
      description: Get position margin change history
      x-description-cn: 逐仓保证金变动历史
      tags:
        - trade
      operationId: getPositionMarginChangeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#get-position-margin-change-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/getPositionMarginChangeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/get_position_margin_change_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/get_position_margin_change_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/GetPositionMarginChangeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/GetPositionMarginChangeHistory/GetPositionMarginChangeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/GetPositionMarginChangeHistoryExample.php
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
            example: BTCUSD
        - name: type
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: Add position margin,2: Reduce position margin"
          x-description-cn: "调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金"
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time
          x-description-cn: 起始时间
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time
          x-description-cn: 结束时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 50
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Position Margin Change History
          x-description-cn: 获取持仓 杠杆 修改历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    amount:
                      type: string
                      example: "23.36332311"
                      description: Amount.
                      x-description-cn: 金额.
                    asset:
                      type: string
                      example: BTC
                      description: asset name
                      x-description-cn: 资产
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    time:
                      type: integer
                      example: 1578047897183
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    type:
                      type: integer
                      example: 1
                      format: int64
                      description: Order type.
                      x-description-cn: 订单类型.
                    positionSide:
                      type: string
                      example: BOTH
                      description: Position side
                      x-description-cn: 持仓方向
  /dapi/v1/positionMargin:
    post:
      summary: Modify Isolated Position Margin (TRADE)
      x-summary-cn: 调整逐仓保证金 (TRADE)
      description: Modify Isolated Position Margin
      x-description-cn: 针对逐仓模式下的仓位,调整其逐仓保证金资金。
      tags:
        - trade
      operationId: modifyIsolatedPositionMargin
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#modify-isolated-position-margin
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/modifyIsolatedPositionMargin.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/modify_isolated_position_margin.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/modify_isolated_position_margin.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/ModifyIsolatedPositionMarginExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/ModifyIsolatedPositionMargin/ModifyIsolatedPositionMargin.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/ModifyIsolatedPositionMarginExample.php
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
      x-parameters-notes: "- Only for isolated symbol"
      x-parameters-notes-cn: "- 只针对逐仓 symbol 与 positionSide(如有)"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - amount
                - type
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Symbol
                  x-description-cn: 交易对
                positionSide:
                  type: string
                  example: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.
                  x-description-cn: 持仓方向,单向持仓模式下非必填,默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: Margin asset
                  x-description-cn: 保证金资金
                type:
                  type: integer
                  example: 1
                  format: int64
                  description: "1: Add position margin,2: Reduce position margin"
                  x-description-cn: "调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金"
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
      responses:
        "200":
          description: Modify Isolated Position Margin
          x-description-cn: Modify Isolated 持仓 杠杆
          content:
            application/json:
              schema:
                type: object
                properties:
                  amount:
                    type: number
                    example: 100
                    format: float
                    description: Amount.
                    x-description-cn: 金额.
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  msg:
                    type: string
                    example: Successfully modify position margin.
                    description: Message details.
                    x-description-cn: 消息详情.
                  type:
                    type: integer
                    example: 1
                    format: int64
                    description: Order type.
                    x-description-cn: 订单类型.
  /dapi/v1/adlQuantile:
    get:
      summary: Position ADL Quantile Estimation (USER_DATA)
      x-summary-cn: 持仓ADL队列估算 (USER_DATA)
      description: >-
        Query position ADL quantile estimation


        * Values update every 30s.

        * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.

        * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and
        "BOTH" will be returned to show the positions' adl quantiles of different position sides.

        * If the positions of the symbol are crossed margined in Hedge Mode:
          * "HEDGE" as a sign will be returned instead of "BOTH";
          * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
      x-description-cn: >-
        查询持仓ADL队列估算



        * 每30秒更新数据

        * 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前

        * 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数

        * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE",
        其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。
      tags:
        - trade
      operationId: positionAdlQuantileEstimation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#position-adl-quantile-estimation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/positionAdlQuantileEstimation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/position_adl_quantile_estimation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/position_adl_quantile_estimation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/PositionAdlQuantileEstimationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/PositionAdlQuantileEstimation/PositionAdlQuantileEstimation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/PositionAdlQuantileEstimationExample.php
      x-ip-weight: 5
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
            example: BTCUSD_200925
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Position ADL Quantile Estimation
          x-description-cn: 持仓 ADL Quantile Estimation
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    adlQuantile:
                      type: object
                      properties:
                        LONG:
                          type: integer
                          example: 3
                          format: int64
                          description: adl quantile for "LONG" position in hedge mode
                          x-description-cn: 双开模式下多头持仓的ADL队列估算分
                        SHORT:
                          type: integer
                          example: 3
                          format: int64
                          description: adl qauntile for "SHORT" position in hedge mode
                          x-description-cn: 双开模式下空头持仓的ADL队列估算分
                        HEDGE:
                          type: integer
                          example: 0
                          format: int64
                          description: Hedge mode ADL quantile.
                          x-description-cn: 双向持仓模式 ADL 分位.
                        BOTH:
                          type: integer
                          example: 0
                          format: int64
                          description: One-way mode ADL quantile.
                          x-description-cn: 单向持仓模式 ADL 分位.
                      description: ADL quantile information.
                      x-description-cn: ADL 分位信息.
  /dapi/v1/positionRisk:
    get:
      summary: Position Information (USER_DATA)
      x-summary-cn: 用户持仓风险 (USER_DATA)
      description: Get current account information.
      x-description-cn: 查询用户持仓风险
      tags:
        - trade
      operationId: positionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/positionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/PositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/PositionInformation/PositionInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/PositionInformationExample.php
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
        - name: marginAsset
          in: query
          required: false
          schema:
            type: string
            example: USDT
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - If neither `marginAsset` nor `pair` is sent, positions of all symbols with `TRADING` status will be returned.

        - for One-way Mode user, the response will only show the "BOTH" positions

        - for Hedge Mode user, the response will show "BOTH", "LONG", and "SHORT" positions. **Note** > Please use with
        user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.

        - Please use with user data stream ACCOUNT_UPDATE to meet your timeliness and accuracy needs.
      x-parameters-notes-cn: |-
        - marginAsset 和 pair 不要同时提供
        - marginAsset 和 pair 均不提供则返回所有上市状态和结算中的symbol
        - 对于单向持仓模式，仅会展示"BOTH"方向的持仓
        - 对于双向持仓模式，会展示所有"BOTH", "LONG", 和"SHORT"方向的持仓 **注意** > 请与账户推送信息`ACCOUNT_UPDATE`配合使用,以满足您的及时性和准确性需求。
        - 请与账户推送信息`ACCOUNT_UPDATE`配合使用,以满足您的及时性和准确性需求。
      responses:
        "200":
          description: Position Information
          x-description-cn: 持仓 信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTCUSD_201225
                      description: Trading symbol
                      x-description-cn: 交易对
                    positionAmt:
                      type: string
                      example: "0"
                      description: position amount
                      x-description-cn: 持仓数量
                    entryPrice:
                      type: string
                      example: "0.0"
                      description: Position entry price.
                      x-description-cn: 持仓开仓价格.
                    breakEvenPrice:
                      type: string
                      example: "0.0"
                      description: break-even price
                      x-description-cn: 盈亏平衡价
                    markPrice:
                      type: string
                      example: "0.00000000"
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
                      example: "125"
                      description: Leverage value.
                      x-description-cn: 杠杆倍数.
                    maxQty:
                      type: string
                      example: "50"
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
                    updateTime:
                      type: integer
                      example: 0
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
  /dapi/v1/openOrder:
    get:
      summary: Query Current Open Order (USER_DATA)
      x-summary-cn: 查询当前挂单 (USER_DATA)
      description: Query Current Open Order
      x-description-cn: 查询当前挂单
      tags:
        - trade
      operationId: queryCurrentOpenOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#query-current-open-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/queryCurrentOpenOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/query_current_open_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/query_current_open_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/QueryCurrentOpenOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/QueryCurrentOpenOrder/QueryCurrentOpenOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/QueryCurrentOpenOrderExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSD_200925
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Order ID
          x-description-cn: 系统订单号
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Client order ID
          x-description-cn: 用户自定义的订单号
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either`orderId` or `origClientOrderId` must be sent
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 中的一个为必填参数
        - 查询的订单如果已经成交或取消,将返回报错"Order does not exist."
      responses:
        "200":
          description: Current Open Order
          x-description-cn: 当前 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgPrice:
                    type: string
                    example: "0.0"
                    description: Average execution price
                    x-description-cn: 平均价格
                  clientOrderId:
                    type: string
                    example: abc
                    description: Client order ID.
                    x-description-cn: 客户端订单 ID.
                  cumBase:
                    type: string
                    example: "0"
                    description: Cumulative base asset amount.
                    x-description-cn: 累计基础资产数量.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed quantity
                    x-description-cn: 执行数量
                  orderId:
                    type: integer
                    example: 1917641
                    format: int64
                    description: Sub-order ID
                    x-description-cn: 子订单 ID
                  origQty:
                    type: string
                    example: "0.40"
                    description: Original order quantity
                    x-description-cn: 原始委托数量
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Original order type.
                    x-description-cn: 原始订单类型.
                  price:
                    type: string
                    example: "0"
                    description: Latest token price.
                    x-description-cn: 代币最新价格。
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Whether the order is reduce-only.
                    x-description-cn: 是否为只减仓订单.
                  side:
                    type: string
                    example: BUY
                    description: Trading side
                    x-description-cn: 买卖方向
                  positionSide:
                    type: string
                    example: SHORT
                    description: Position side
                    x-description-cn: 持仓方向
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价,对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trading symbol
                    x-description-cn: 交易对
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair
                    x-description-cn: 标的交易对
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: Time
                    x-description-cn: 时间
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force
                    x-description-cn: 有效方式
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Order type.
                    x-description-cn: 订单类型.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
                  updateTime:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: update time
                    x-description-cn: 更新时间
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
                  priceMatch:
                    type: string
                    example: NONE
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
  /dapi/v1/forceOrders:
    get:
      summary: User's Force Orders (USER_DATA)
      x-summary-cn: 用户强平单历史 (USER_DATA)
      description: User's Force Orders
      x-description-cn: 用户强平单历史
      tags:
        - trade
      operationId: usersForceOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/trade#users-force-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/TradeApi/usersForceOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/trade_api/users_force_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/Trade/users_force_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/trade/UsersForceOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/TradeAPI/UsersForceOrders/UsersForceOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/trade/UsersForceOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "**20** (after CM migration: **20** with symbol / **50** without symbol)"
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
            example: BTCUSD_200925
        - name: autoCloseType
          in: query
          required: false
          schema:
            type: string
            example: LIQUIDATION
            enum:
              - LIQUIDATION
              - ADL
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 50
            maximum: 100
          description: Maximum number of records to return.
          x-description-cn: 返回记录数量上限。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value
            must reflect the current client time and is validated by the server
            for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - Only support querying data in the past 90 days
      x-parameters-notes-cn: |-
        - 如果没有传 "autoCloseType", 强平单和 ADL 减仓单都会被返回
        - 如果没有传"startTime", 只会返回"endTime"之前 200 天内的数据
      responses:
        "200":
          description: User's Force Orders
          x-description-cn: 用户's Force 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 165123080
                      format: int64
                      description: Sub-order ID
                      x-description-cn: 子订单 ID
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trading symbol
                      x-description-cn: 交易对
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair
                      x-description-cn: 标的交易对
                    status:
                      type: string
                      example: FILLED
                      description: Status.
                      x-description-cn: 订单状态
                    clientOrderId:
                      type: string
                      example: autoclose-1596542005017000006
                      description: Client order ID.
                      x-description-cn: 客户端订单 ID.
                    price:
                      type: string
                      example: "11326.9"
                      description: Latest token price.
                      x-description-cn: 代币最新价格。
                    avgPrice:
                      type: string
                      example: "11326.9"
                      description: Average execution price
                      x-description-cn: 平均价格
                    origQty:
                      type: string
                      example: "1"
                      description: Original order quantity
                      x-description-cn: 原始委托数量
                    executedQty:
                      type: string
                      example: "1"
                      description: Executed quantity
                      x-description-cn: 执行数量
                    cumBase:
                      type: string
                      example: "0.00882854"
                      description: Cumulative base asset amount.
                      x-description-cn: 累计基础资产数量.
                    cumQuote:
                      type: string
                      example: "100"
                      description: Cumulative quote asset amount.
                      x-description-cn: 成交金额(计价币种).
                    timeInForce:
                      type: string
                      example: IOC
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
                      example: SELL
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
                    time:
                      type: integer
                      example: 1596542005019
                      format: int64
                      description: Time
                      x-description-cn: 时间
                    updateTime:
                      type: integer
                      example: 1596542005050
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
                      description: order pre-set auto cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
  /dapi/v1/listenKey:
    delete:
      summary: Close User Data Stream (USER_STREAM)
      x-summary-cn: 关闭listenKey (USER_STREAM)
      description: Close out a user data stream.
      x-description-cn: 关闭某账户数据流
      tags:
        - user-data-streams
      operationId: closeUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/userdatastreams/CloseUserDataStreamExample.php
      x-ip-weight: 1
      x-security-type: USER_STREAM
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
      responses:
        "200":
          description: OK
          x-description-cn: 成功
    put:
      summary: Keepalive User Data Stream (USER_STREAM)
      x-summary-cn: 延长listenKey有效期 (USER_STREAM)
      description: |-
        Keepalive a user data stream to prevent a time out. User data streams
        will close after 60 minutes.
      x-description-cn: 有效期延长至本次调用后60分钟
      tags:
        - user-data-streams
      operationId: keepaliveUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/userdatastreams/KeepaliveUserDataStreamExample.php
      x-ip-weight: 1
      x-security-type: USER_STREAM
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
      responses:
        "200":
          description: Keepalive User Data Stream
          x-description-cn: Keepalive 用户 Data Stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  listenKey:
                    type: string
                    example: vmNt6gl1so8bXVsaAY153FG5tf63QaODxUarKUM8V8rY4ElSwEe431DNIYNKOkQp
                    description: Listen key.
                    x-description-cn: 监听密钥.
    post:
      summary: Start User Data Stream (USER_STREAM)
      x-summary-cn: 生成listenKey (USER_STREAM)
      description: |-
        Start a new user data stream. The stream will close after 60 minutes
        unless a keepalive is sent. If the account has an active `listenKey`,
        that `listenKey` will be returned and its validity will be extended for
        60 minutes.
      x-description-cn: |-
        创建一个新的user data
        stream,返回值为一个listenKey,即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`,则将返回该`listenKey`并将其有效期延长60分钟。
      tags:
        - user-data-streams
      operationId: startUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/rest-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-coin-futures/examples/rest-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_coin_futures/rest_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_coin_futures/examples/rest_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-coin-futures/src/main/java/com/binance/connector/client/derivatives_trading_coin_futures/rest/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingcoinfutures/examples/restapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-coin-futures/userdatastreams/StartUserDataStreamExample.php
      x-ip-weight: 1
      x-security-type: USER_STREAM
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
      responses:
        "200":
          description: Start User Data Stream
          x-description-cn: 开始 用户 Data Stream
          content:
            application/json:
              schema:
                type: object
                properties:
                  listenKey:
                    type: string
                    example: pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1
                    description: Listen key.
                    x-description-cn: 监听密钥.
```