---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:00.707628
---

# advanced-trading-derivatives-trading-portfolio-margin__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Portfolio Margin REST API
  description: Access account information, manage margin positions, and trade with Binance Portfolio Margin.
  x-description-cn: 访问账户信息、管理保证金仓位，并通过 Binance 统一账户进行交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/derivatives-trading-portfolio-margin/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-portfolio-margin/general-info#访问限制
x-security-guide: products/derivatives-trading-portfolio-margin/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-portfolio-margin/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Portfolio Margin docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin/general-info
  x-description-cn: Portfolio Margin docs
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 市场数据
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: user-data-streams
    x-displayName: User Data Streams
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: https://papi.binance.com
  - url: https://testnet.binancefuture.com
paths:
  /papi/v1/balance:
    get:
      summary: Account Balance (USER_DATA)
      x-summary-cn: 查询账户余额 (USER_DATA)
      description: Query account balance
      x-description-cn: 查询账户余额
      tags:
        - account
      operationId: accountBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#account-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/accountBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/account_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/account_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/AccountBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/AccountBalance/AccountBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/AccountBalanceExample.php
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
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: USDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Account Balance
          x-description-cn: 账户 Balance
          content:
            application/json:
              schema:
                oneOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                          description: asset name
                          x-description-cn: 资产
                        totalWalletBalance:
                          type: string
                          example: "126.72469206"
                          description: Total Wallet Balance.
                          x-description-cn: Total Wallet Balance.
                        crossMarginAsset:
                          type: string
                          example: "103.00000000"
                          description: Cross Margin Asset. Equal to crossMarginFree + crossMarginLocked.
                          x-description-cn: 全仓资产。等于 crossMarginFree + crossMarginLocked。
                        crossMarginBorrowed:
                          type: string
                          example: "10.00000000"
                          description: Cross Margin Borrowed.
                          x-description-cn: Cross Margin Borrowed.
                        crossMarginFree:
                          type: string
                          example: "100.00000000"
                          description: Cross Margin Free.
                          x-description-cn: Cross Margin Free.
                        crossMarginInterest:
                          type: string
                          example: "0.72469206"
                          description: Cross Margin Interest.
                          x-description-cn: Cross Margin Interest.
                        crossMarginLocked:
                          type: string
                          example: "3.00000000"
                          description: Cross Margin Locked.
                          x-description-cn: Cross Margin Locked.
                        umWalletBalance:
                          type: string
                          example: "0.00000000"
                          description: Um Wallet Balance.
                          x-description-cn: Um Wallet Balance.
                        umUnrealizedPNL:
                          type: string
                          example: "23.72469206"
                          description: Um Unrealized PNL.
                          x-description-cn: Um Unrealized PNL.
                        cmWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: Cm Wallet Balance.
                          x-description-cn: Cm Wallet Balance.
                        cmUnrealizedPNL:
                          type: string
                          example: ""
                          description: Cm Unrealized PNL.
                          x-description-cn: Cm Unrealized PNL.
                        updateTime:
                          type: integer
                          example: 1617939110373
                          format: int64
                          description: last update time
                          x-description-cn: 更新时间
                        negativeBalance:
                          type: string
                          example: "0"
                          description: negative balance amount
                          x-description-cn: 当前负余额值
                  - type: object
                    properties:
                      asset:
                        type: string
                        example: USDT
                        description: asset name
                        x-description-cn: 资产
                      totalWalletBalance:
                        type: string
                        example: "126.72469206"
                        description: Total Wallet Balance.
                        x-description-cn: Total Wallet Balance.
                      crossMarginBorrowed:
                        type: string
                        example: "10.00000000"
                        description: Cross Margin Borrowed.
                        x-description-cn: Cross Margin Borrowed.
                      crossMarginFree:
                        type: string
                        example: "100.00000000"
                        description: Cross Margin Free.
                        x-description-cn: Cross Margin Free.
                      crossMarginInterest:
                        type: string
                        example: "0.72469206"
                        description: Cross Margin Interest.
                        x-description-cn: Cross Margin Interest.
                      crossMarginLocked:
                        type: string
                        example: "3.00000000"
                        description: Cross Margin Locked.
                        x-description-cn: Cross Margin Locked.
                      umWalletBalance:
                        type: string
                        example: "0.00000000"
                        description: Um Wallet Balance.
                        x-description-cn: Um Wallet Balance.
                      umUnrealizedPNL:
                        type: string
                        example: "23.72469206"
                        description: Um Unrealized PNL.
                        x-description-cn: Um Unrealized PNL.
                      cmWalletBalance:
                        type: string
                        example: "23.72469206"
                        description: Cm Wallet Balance.
                        x-description-cn: Cm Wallet Balance.
                      cmUnrealizedPNL:
                        type: string
                        example: ""
                        description: Cm Unrealized PNL.
                        x-description-cn: Cm Unrealized PNL.
                      updateTime:
                        type: integer
                        example: 1617939110373
                        format: int64
                        description: last update time
                        x-description-cn: 更新时间
                      negativeBalance:
                        type: string
                        example: "0"
                        description: negative balance amount
                        x-description-cn: 当前负余额值
  /papi/v1/account:
    get:
      summary: Account Information (USER_DATA)
      x-summary-cn: 查询账户信息 (USER_DATA)
      description: Query account information
      x-description-cn: 查询账户信息
      tags:
        - account
      operationId: accountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/accountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/AccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/AccountInformation/AccountInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/AccountInformationExample.php
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
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Account Information
          x-description-cn: 账户 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  uniMMR:
                    type: string
                    example: "5167.92171923"
                    description: Portfolio margin account maintenance margin rate
                    x-description-cn: 统一账户维持保证金率
                  accountEquity:
                    type: string
                    example: "73.47428058"
                    description: Account equity, in USD value
                    x-description-cn: 以USD计价的账户权益
                  actualEquity:
                    type: string
                    example: "122607.35137903"
                    description: Account equity without collateral rate, in USD value
                    x-description-cn: 不考虑质押率的以USD计价账户权益
                  accountInitialMargin:
                    type: string
                    example: "23.72469206"
                    description: Account Initial Margin.
                    x-description-cn: Account Initial Margin.
                  accountMaintMargin:
                    type: string
                    example: "23.72469206"
                    description: Portfolio margin account maintenance margin, unit：USD
                    x-description-cn: 以USD计价统一账户维持保证金
                  accountStatus:
                    type: string
                    example: NORMAL
                    description: >-
                      Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY",
                      "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"
                    x-description-cn: >-
                      统一账户账户状态："NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION",
                      "FORCE_LIQUIDATION", "BANKRUPTED"
                  virtualMaxWithdrawAmount:
                    type: string
                    example: "1627523.32459208"
                    description: Portfolio margin maximum amount for transfer out in USD
                    x-description-cn: 以USD计价的最大可转出
                  totalAvailableBalance:
                    type: string
                    example: ""
                    description: Total Available Balance.
                    x-description-cn: Total Available Balance.
                  totalMarginOpenLoss:
                    type: string
                    example: ""
                    description: in USD margin open order
                    x-description-cn: in USD margin open order
                  updateTime:
                    type: integer
                    example: 1657707212154
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
  /papi/v1/bnb-transfer:
    post:
      summary: BNB transfer (TRADE)
      x-summary-cn: BNB划转 (TRADE)
      description: Transfer BNB in and out of UM
      x-description-cn: 从PM钱包划转BNB到UM钱包
      tags:
        - account
      operationId: bnbTransfer
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#bnb-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/bnbTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/bnb_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/bnb_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/BnbTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/BnbTransfer/BnbTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/BnbTransferExample.php
      x-ip-weight: 750
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
      x-parameters-notes: "- The endpoint can only be called 10 times per 10 minutes in a rolling manner"
      x-parameters-notes-cn: "- 本接口每10分钟只能调用10次（时间滚动计算）"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - amount
                - transferSide
                - timestamp
              properties:
                amount:
                  type: number
                  example: "1.0"
                  format: float
                transferSide:
                  type: string
                  example: TO_UM
                  enum:
                    - TO_UM
                    - FROM_UM
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: BNB transfer
          x-description-cn: BNB 划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 100000001
                    format: int64
                    description: Transaction ID.
                    x-description-cn: 交易ID。
  /papi/v1/repay-futures-switch:
    post:
      summary: Change Auto-repay-futures Status (TRADE)
      x-summary-cn: 更改自动清还合约负余额模式 (TRADE)
      description: Change Auto-repay-futures Status
      x-description-cn: 更改自动支付合约负余额模式
      tags:
        - account
      operationId: changeAutoRepayFuturesStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#change-auto-repay-futures-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/changeAutoRepayFuturesStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/change_auto_repay_futures_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/change_auto_repay_futures_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/ChangeAutoRepayFuturesStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/ChangeAutoRepayFuturesStatus/ChangeAutoRepayFuturesStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/ChangeAutoRepayFuturesStatusExample.php
      x-ip-weight: 750
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
                - autoRepay
                - timestamp
              properties:
                autoRepay:
                  type: string
                  example: "true"
                  default: "true"
                  enum:
                    - "true"
                    - "false"
                  description: "`false` for turn off the auto-repay futures negative balance function"
                  x-description-cn: "`false`代表关闭自动清还合约负余额"
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Change Auto-repay-futures Status
          x-description-cn: 修改Auto-repay-futures 状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
    get:
      summary: Get Auto-repay-futures Status (USER_DATA)
      x-summary-cn: 查询自动清还合约负余额模式 (USER_DATA)
      description: Query Auto-repay-futures Status
      x-description-cn: 查询自动清还合约负余额模式
      tags:
        - account
      operationId: getAutoRepayFuturesStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-auto-repay-futures-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getAutoRepayFuturesStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_auto_repay_futures_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_auto_repay_futures_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetAutoRepayFuturesStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetAutoRepayFuturesStatus/GetAutoRepayFuturesStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetAutoRepayFuturesStatusExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Auto-repay-futures Status
          x-description-cn: 获取Auto-repay-futures 状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  autoRepay:
                    type: boolean
                    example: true
                    description: '"true" for turn on the auto-repay futures; "false" for turn off the auto-repay futures'
                    x-description-cn: "`true`代表自动清还合约负余额; `false`代表关闭自动清还合约负余额"
  /papi/v1/cm/leverage:
    post:
      summary: Change CM Initial Leverage (TRADE)
      x-summary-cn: 调整CM开仓杠杆 (TRADE)
      description: Change user's initial leverage of specific symbol in CM.
      x-description-cn: 调整用户在指定CM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量
      tags:
        - account
      operationId: changeCmInitialLeverage
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#change-cm-initial-leverage
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/changeCmInitialLeverage.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/change_cm_initial_leverage.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/change_cm_initial_leverage.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/ChangeCmInitialLeverageExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/ChangeCmInitialLeverage/ChangeCmInitialLeverage.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/ChangeCmInitialLeverageExample.php
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
                leverage:
                  type: integer
                  example: 21
                  minimum: 1
                  maximum: 125
                  format: int64
                  description: target initial leverage
                  x-description-cn: 目标初始杠杆倍数
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Change CM Initial Leverage
          x-description-cn: 修改CM Initial Leverage
          content:
            application/json:
              schema:
                type: object
                properties:
                  leverage:
                    type: integer
                    example: 21
                    format: int64
                    description: current initial leverage
                    x-description-cn: 杠杆倍率
                  maxQty:
                    type: string
                    example: "1000"
                    description: maximum quantity of base asset
                    x-description-cn: maximum quantity of base asset
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
  /papi/v1/cm/positionSide/dual:
    post:
      summary: Change CM Position Mode (TRADE)
      x-summary-cn: 更改CM持仓模式 (TRADE)
      description: Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM
      x-description-cn: 变换用户在 CM 所有 symbol 合约上的持仓模式：双向持仓或单向持仓。
      tags:
        - account
      operationId: changeCmPositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#change-cm-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/changeCmPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/change_cm_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/change_cm_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/ChangeCmPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/ChangeCmPositionMode/ChangeCmPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/ChangeCmPositionModeExample.php
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
                  enum:
                    - "true"
                    - "false"
                  description: '"true": Hedge Mode; "false": One-way Mode'
                  x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Change CM Position Mode
          x-description-cn: 修改CM 持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
    get:
      summary: Get CM Current Position Mode (USER_DATA)
      x-summary-cn: 查询CM持仓模式 (USER_DATA)
      description: Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM
      x-description-cn: "查询用户目前在CM所有symbol合约上的持仓模式: 双向持仓或单向持仓。"
      tags:
        - account
      operationId: getCmCurrentPositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-cm-current-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getCmCurrentPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_cm_current_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_cm_current_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetCmCurrentPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetCmCurrentPositionMode/GetCmCurrentPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetCmCurrentPositionModeExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get CM Current Position Mode
          x-description-cn: 获取CM 当前 持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  dualSidePosition:
                    type: boolean
                    example: true
                    description: '"true": Hedge Mode; "false": One-way Mode'
                    x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
  /papi/v1/um/leverage:
    post:
      summary: Change UM Initial Leverage (TRADE)
      x-summary-cn: 调整UM开仓杠杆 (TRADE)
      description: Change user's initial leverage of specific symbol in UM.
      x-description-cn: 调整用户在指定UM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量
      tags:
        - account
      operationId: changeUmInitialLeverage
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#change-um-initial-leverage
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/changeUmInitialLeverage.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/change_um_initial_leverage.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/change_um_initial_leverage.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/ChangeUmInitialLeverageExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/ChangeUmInitialLeverage/ChangeUmInitialLeverage.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/ChangeUmInitialLeverageExample.php
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
                  example: BTCUSDT
                leverage:
                  type: integer
                  example: 21
                  minimum: 1
                  format: int64
                  description: >-
                    Target initial leverage. The maximum is symbol-specific: use `initialLeverage` of bracket 1 from
                    `GET /papi/v1/um/leverageBracket`.
                  x-description-cn: 目标初始杠杆倍数。最大值因交易对而异，以 `GET /papi/v1/um/leverageBracket` 返回的第 1 档 `initialLeverage` 为准。
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Change UM Initial Leverage
          x-description-cn: 修改UM Initial Leverage
          content:
            application/json:
              schema:
                type: object
                properties:
                  leverage:
                    type: integer
                    example: 21
                    format: int64
                    description: current initial leverage
                    x-description-cn: 杠杆倍率
                  maxNotionalValue:
                    type: string
                    example: "1000000"
                    description: Max Notional Value.
                    x-description-cn: Max Notional Value.
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
  /papi/v1/um/positionSide/dual:
    post:
      summary: Change UM Position Mode (TRADE)
      x-summary-cn: 更改UM持仓模式 (TRADE)
      description: Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM
      x-description-cn: 变换用户在UM所有symbol合约上的持仓模式：双向持仓或单向持仓。
      tags:
        - account
      operationId: changeUmPositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#change-um-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/changeUmPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/change_um_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/change_um_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/ChangeUmPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/ChangeUmPositionMode/ChangeUmPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/ChangeUmPositionModeExample.php
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
                  enum:
                    - "true"
                    - "false"
                  description: '"true": Hedge Mode; "false": One-way Mode'
                  x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Change UM Position Mode
          x-description-cn: 修改UM 持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
    get:
      summary: Get UM Current Position Mode (USER_DATA)
      x-summary-cn: 查询UM持仓模式 (USER_DATA)
      description: Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM
      x-description-cn: "查询用户目前在UM所有symbol合约上的持仓模式: 双向持仓或单向持仓。"
      tags:
        - account
      operationId: getUmCurrentPositionMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-current-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmCurrentPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_current_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_current_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmCurrentPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmCurrentPositionMode/GetUmCurrentPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmCurrentPositionModeExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get UM Current Position Mode
          x-description-cn: 获取UM 当前 持仓 Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  dualSidePosition:
                    type: boolean
                    example: true
                    description: '"true": Hedge Mode; "false": One-way Mode'
                    x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
  /papi/v1/cm/leverageBracket:
    get:
      summary: CM Notional and Leverage Brackets (USER_DATA)
      x-summary-cn: 查询CM杠杆分层标准 (USER_DATA)
      description: Query CM notional and leverage brackets
      x-description-cn: 查询CM杠杆分层标准
      tags:
        - account
      operationId: cmNotionalAndLeverageBrackets
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#cm-notional-and-leverage-brackets
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/cmNotionalAndLeverageBrackets.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/cm_notional_and_leverage_brackets.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/cm_notional_and_leverage_brackets.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/CmNotionalAndLeverageBracketsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/CmNotionalAndLeverageBrackets/CmNotionalAndLeverageBrackets.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/CmNotionalAndLeverageBracketsExample.php
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
            example: BTCUSD_PERP
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: CM Notional and Leverage Brackets
          x-description-cn: CM Notional 和 Leverage Brackets
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
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
                          qtyFloor:
                            type: integer
                            example: 0
                            format: int64
                            description: lower edge of base asset quantity
                            x-description-cn: 该层对应的数量下限
                          maintMarginRatio:
                            type: number
                            example: 0.004
                            format: float
                            description: maintenance margin rate
                            x-description-cn: 该层对应的维持保证金率
                          cum:
                            type: number
                            example: 0
                            format: float
                            description: Auxiliary number for quick calculation
                            x-description-cn: 速算数
                      description: Brackets.
                      x-description-cn: Brackets.
  /papi/v1/auto-collection:
    post:
      summary: Fund Auto-collection (TRADE)
      x-summary-cn: 统一账户资金归集 (TRADE)
      description: Fund collection for Portfolio Margin
      x-description-cn: 资金归集到统一账户钱包
      tags:
        - account
      operationId: fundAutoCollection
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#fund-auto-collection
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/fundAutoCollection.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/fund_auto_collection.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/fund_auto_collection.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/FundAutoCollectionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/FundAutoCollection/FundAutoCollection.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/FundAutoCollectionExample.php
      x-ip-weight: 750
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
        - BNB assets will not be auto-collected.
        - Rolling window endpoint can be called at most 500 times per hour.
      x-parameters-notes-cn: |-
        - BNB资产不会归集
        - 滚动每小时仅能调用500次
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Fund Auto-collection
          x-description-cn: 请参见英文说明：Fund Auto-collection
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/asset-collection:
    post:
      summary: Fund Collection by Asset (TRADE)
      x-summary-cn: 特定资产资金归集 (TRADE)
      description: Transfers specific asset from Futures Account to Margin account
      x-description-cn: 特定资产账户资金归集，从合约账户划转到杠杆账户
      tags:
        - account
      operationId: fundCollectionByAsset
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#fund-collection-by-asset
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/fundCollectionByAsset.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/fund_collection_by_asset.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/fund_collection_by_asset.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/FundCollectionByAssetExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/FundCollectionByAsset/FundCollectionByAsset.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/FundCollectionByAssetExample.php
      x-ip-weight: 30
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
      x-parameters-notes: "- The BNB transfer is not be supported"
      x-parameters-notes-cn: "- 本接口不支持划转BNB资产"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - asset
                - timestamp
              properties:
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: 10
                  format: float
                  description: Amount to collect. When provided, `futureType` is required.
                  x-description-cn: 待归集的数量。传入该参数时，`futureType` 为必填。
                futureType:
                  type: string
                  example: UM
                  enum:
                    - UM
                    - CM
                    - OPTION
                  description: >-
                    Target wallet for the collection. `OPTION` is for SPAN only. Cannot be sent without `amount`.
                    `amount` and `futureType` must be provided together. If neither is provided, existing behavior is
                    unchanged (query all wallets + transfer).
                  x-description-cn: 归集的目标钱包。`OPTION` 仅支持 SPAN。不能在不传 `amount` 的情况下传入。`amount` 和 `futureType` 必须同时传入。均不传入时行为不变（查询所有钱包并划转）。
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Fund Collection by Asset
          x-description-cn: Fund Collection by 资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/cm/account:
    get:
      summary: Get CM Account Detail (USER_DATA)
      x-summary-cn: 获取CM账户信息 (USER_DATA)
      description: Get current CM account asset and position information.
      x-description-cn: 获取现有CM账户资产和仓位信息
      tags:
        - account
      operationId: getCmAccountDetail
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-cm-account-detail
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getCmAccountDetail.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_cm_account_detail.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_cm_account_detail.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetCmAccountDetailExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetCmAccountDetail/GetCmAccountDetail.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetCmAccountDetailExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get CM Account Detail
          x-description-cn: 获取CM 账户 Detail
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
                        crossWalletBalance:
                          type: string
                          example: "0.00241969"
                          description: total wallet balance
                          x-description-cn: 全仓账户余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit or loss
                          x-description-cn: 全仓持仓未实现盈亏
                        maintMargin:
                          type: string
                          example: "0.00000000"
                          description: maintenance margin
                          x-description-cn: 维持保证金
                        initialMargin:
                          type: string
                          example: "0.00000000"
                          description: total intial margin required with the latest mark price
                          x-description-cn: 当前所需起始保证金
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: positions" margin required with the latest mark price
                          x-description-cn: 持仓所需起始保证金(基于最新标记价格)
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: open orders" intial margin required with the latest mark price
                          x-description-cn: 当前挂单所需起始保证金(基于最新标记价格)e
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
                          description: last update time
                          x-description-cn: 更新时间
                    description: Assets.
                    x-description-cn: Assets.
                  positions:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSD_201225
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        positionAmt:
                          type: string
                          example: "0"
                          description: position amount
                          x-description-cn: position amount
                        initialMargin:
                          type: string
                          example: "0"
                          description: total intial margin required with the latest mark price
                          x-description-cn: 当前所需起始保证金
                        maintMargin:
                          type: string
                          example: "0"
                          description: maintenance margin
                          x-description-cn: 维持保证金
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit
                          x-description-cn: 持仓未实现盈亏
                        positionInitialMargin:
                          type: string
                          example: "0"
                          description: positions" margin required with the latest mark price
                          x-description-cn: 持仓所需起始保证金(基于最新标记价格)
                        openOrderInitialMargin:
                          type: string
                          example: "0"
                          description: open orders" intial margin required with the latest mark price
                          x-description-cn: 当前挂单所需起始保证金(基于最新标记价格)e
                        leverage:
                          type: string
                          example: "125"
                          description: current initial leverage
                          x-description-cn: 杠杆倍率
                        positionSide:
                          type: string
                          example: BOTH
                          description: BOTH means that it is the position of One-way Mode
                          x-description-cn: BOTH means that it is the position of One-way Mode
                        entryPrice:
                          type: string
                          example: "0.0"
                          description: average entry price
                          x-description-cn: 持仓成本价
                        maxQty:
                          type: string
                          example: "50"
                          description: maximum quantity of base asset
                          x-description-cn: maximum quantity of base asset
                        updateTime:
                          type: integer
                          example: 0
                          format: int64
                          description: last update time
                          x-description-cn: 更新时间
                    description: positions of all symbols in the market are returned
                    x-description-cn: 头寸，将返回所有市场symbol。
  /papi/v1/cm/income:
    get:
      summary: Get CM Income History (USER_DATA)
      x-summary-cn: 获取CM损益资金流水 (USER_DATA)
      description: Get CM Income History.
      x-description-cn: 获取CM损益资金流水。
      tags:
        - account
      operationId: getCmIncomeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-cm-income-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getCmIncomeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_cm_income_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_cm_income_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetCmIncomeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetCmIncomeHistory/GetCmIncomeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetCmIncomeHistoryExample.php
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
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD_200925
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
            example: 100
            default: 100
            maximum: 1000
            format: int64
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
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
        - If `incomeType` is not sent, all kinds of flow will be returned
        - "trandId" is unique in the same "incomeType" for a user
        - The interval between `startTime` and `endTime` can not exceed 200 days:
          - If `startTime` and `endTime` are not sent, the last 200 days will be returned
      x-parameters-notes-cn: |-
        - 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据.
        - 如果`incomeType`没有发送，返回所有类型账户损益资金流水。
        - `trandId` 在相同用户的同一种收益流水类型中是唯一的。
          - 仅保留最近3个月的数据。
      responses:
        "200":
          description: Get CM Income History
          x-description-cn: 获取CM损益资金流水
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    incomeType:
                      type: string
                      example: TRANSFER
                      description: Income type.
                      x-description-cn: 收益类型。
                    income:
                      type: string
                      example: "-0.37500000"
                      description: Income amount.
                      x-description-cn: 收益金额。
                    asset:
                      type: string
                      example: BTC
                      description: Income asset.
                      x-description-cn: 收益资产。
                    info:
                      type: string
                      example: WITHDRAW
                      description: Extra information.
                      x-description-cn: 附加信息。
                    time:
                      type: integer
                      example: 1570608000000
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    tranId:
                      type: string
                      example: "9689322392"
                      description: Transaction ID.
                      x-description-cn: 交易ID。
                    tradeId:
                      type: string
                      example: ""
                      description: Trade ID, if existing.
                      x-description-cn: 成交ID（如存在）。
  /papi/v1/um/order/asyn:
    get:
      summary: Get Download Id For UM Futures Order History (USER_DATA)
      x-summary-cn: 获取UM合约订单历史下载Id (USER_DATA)
      description: Get download id for UM futures order history
      x-description-cn: 获取UM合约订单历史下载Id
      tags:
        - account
      operationId: getDownloadIdForUmFuturesOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-download-id-for-um-futures-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getDownloadIdForUmFuturesOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_download_id_for_um_futures_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_download_id_for_um_futures_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetDownloadIdForUmFuturesOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetDownloadIdForUmFuturesOrderHistory/GetDownloadIdForUmFuturesOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetDownloadIdForUmFuturesOrderHistoryExample.php
      x-ip-weight: 1500
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
          x-description-cn: 时间戳 in ms
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 时间戳 in ms
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Request Limitation is 10 times per month, shared by front end download page and rest api
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 请求 Limitation is 10 times per month, shared by front 结束 download 页 和 rest API
        - The 时间 between `开始 时间` 和 `结束 时间` can not be longer than 1 year
      responses:
        "200":
          description: Get Download Id For UM Futures Order History
          x-description-cn: 获取Download ID 用于 UM 合约 订单 历史
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
                    description: Download ID.
                    x-description-cn: Download ID.
  /papi/v1/um/trade/asyn:
    get:
      summary: Get Download Id For UM Futures Trade History (USER_DATA)
      x-summary-cn: 获取UM合约交易历史下载Id (USER_DATA)
      description: Get download id for UM futures trade history
      x-description-cn: 获取UM合约交易历史下载Id
      tags:
        - account
      operationId: getDownloadIdForUmFuturesTradeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-download-id-for-um-futures-trade-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getDownloadIdForUmFuturesTradeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_download_id_for_um_futures_trade_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_download_id_for_um_futures_trade_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetDownloadIdForUmFuturesTradeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetDownloadIdForUmFuturesTradeHistory/GetDownloadIdForUmFuturesTradeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetDownloadIdForUmFuturesTradeHistoryExample.php
      x-ip-weight: 1500
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
          x-description-cn: 时间戳 in ms
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 时间戳 in ms
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Request Limitation is 5 times per month, shared by front end download page and rest api
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 请求 Limitation is 5 times per month, shared by front 结束 download 页 和 rest API
        - The 时间 between `开始 时间` 和 `结束 时间` can not be longer than 1 year
      responses:
        "200":
          description: Get Download Id For UM Futures Trade History
          x-description-cn: 获取Download ID 用于 UM 合约 交易 历史
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
                    description: Download ID.
                    x-description-cn: Download ID.
  /papi/v1/um/income/asyn:
    get:
      summary: Get Download Id For UM Futures Transaction History (USER_DATA)
      x-summary-cn: 获取UM合约资金流水历史下载Id (USER_DATA)
      description: Get download id for UM futures transaction history
      x-description-cn: 获取UM合约资金流水历史下载Id
      tags:
        - account
      operationId: getDownloadIdForUmFuturesTransactionHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-download-id-for-um-futures-transaction-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getDownloadIdForUmFuturesTransactionHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_download_id_for_um_futures_transaction_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_download_id_for_um_futures_transaction_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetDownloadIdForUmFuturesTransactionHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetDownloadIdForUmFuturesTransactionHistory/GetDownloadIdForUmFuturesTransactionHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetDownloadIdForUmFuturesTransactionHistoryExample.php
      x-ip-weight: 1500
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
          x-description-cn: 时间戳 in ms
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in ms
          x-description-cn: 时间戳 in ms
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Request Limitation is 5 times per month, shared by front end download page and rest api
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 请求 Limitation is 5 times per month, shared by front 结束 download 页 和 rest API
        - The 时间 between `开始 时间` 和 `结束 时间` can not be longer than 1 year
      responses:
        "200":
          description: Get Download Id For UM Futures Transaction History
          x-description-cn: 获取Download ID 用于 UM 合约 Transaction 历史
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
                    description: Download ID.
                    x-description-cn: Download ID.
  /papi/v1/margin/marginInterestHistory:
    get:
      summary: Get Margin Borrow/Loan Interest History (USER_DATA)
      x-summary-cn: 获取杠杆利息历史 (USER_DATA)
      description: Get Margin Borrow/Loan Interest History
      x-description-cn: 获取杠杆利息历史
      tags:
        - account
      operationId: getMarginBorrowLoanInterestHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-margin-borrow-loan-interest-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getMarginBorrowLoanInterestHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_margin_borrow_loan_interest_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_margin_borrow_loan_interest_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetMarginBorrowLoanInterestHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetMarginBorrowLoanInterestHistory/GetMarginBorrowLoanInterestHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetMarginBorrowLoanInterestHistoryExample.php
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
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: USDT
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
            minimum: 1
          description: Current page number.
          x-description-cn: 当前页码。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: archived
          in: query
          required: false
          schema:
            type: string
            example: "true"
            default: "false"
            enum:
              - "true"
              - "false"
          description: Set to true to query archived data from 6 months ago.
          x-description-cn: 设为 true 可查询 6 个月前的归档数据。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than `60000`
          x-description-cn: 赋值不能超过 `60000`
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Response in descending order

        - The max interval between startTime and endTime is 30 days. It is a MUST to ensure data correctness.

        - If `startTime` and `endTime` not sent, return records of the last 7 days by default

        - If `startTime` is sent and `endTime` is not sent, the records from `startTime` to the present will be
        returned; if `startTime` is more than 30 days ago, the records of the past 30 days will be returned.

        - If `startTime` is not sent and `endTime` is sent, the records of the 7 days before `endTime` is returned.

        - Type in response has 5 enums:
          - `PERIODIC` interest charged per hour
          - `ON_BORROW` first interest charged on borrow
          - `PERIODIC_CONVERTED` interest charged per hour converted into BNB
          - `ON_BORROW_CONVERTED` first interest charged on borrow converted into BNB
          - `PORTFOLIO` Portfolio Margin negative balance daily interest
      x-parameters-notes-cn: |-
        - 响应返回为降序排列。
        - 查询时间范围最大不得超过30天，这是确保数据正确性必须的。
        - 若`startTime`和`endTime`没传，则默认返回最近7天数据。
        - 如果发送了`startTime`且未发送`endTime`，则返回`startTime`到现在的的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
        - 如果没有发送`startTime`而发送了`endTime`，则返回`endTime`之前7天的利息历史记录。
        - 返回的type数据有5种类型:
          - `PERIODIC` 每小时收的利息
          - `ON_BORROW` 借款的时候第一次收的利息
          - `PERIODIC_CONVERTED` 每小时收的利息，用BNB抵扣
          - `ON_BORROW_CONVERTED` 借款的时候第一次收的利息，用BNB抵扣
          - `PORTFOLIO`统一账户负余额每日利息
      responses:
        "200":
          description: Get Margin Borrow/Loan Interest History
          x-description-cn: 获取杠杆 借款/借贷 利息 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        txId:
                          type: integer
                          example: 1352286576452864800
                          format: int64
                          description: Tx ID.
                          x-description-cn: Tx ID.
                        interestAccuredTime:
                          type: integer
                          example: 1672160400000
                          format: int64
                          description: Interest Accured Time.
                          x-description-cn: Interest Accured Time.
                        asset:
                          type: string
                          example: USDT
                          description: asset name
                          x-description-cn: 资产
                        rawAsset:
                          type: string
                          example: USDT
                          description: Raw Asset.
                          x-description-cn: Raw Asset.
                        principal:
                          type: string
                          example: "45.3313"
                          description: Principal repaid
                          x-description-cn: 支付的本金
                        interest:
                          type: string
                          example: "0.00024995"
                          description: Interest repaid
                          x-description-cn: 支付的利息
                        interestRate:
                          type: string
                          example: "0.00013233"
                          description: daily interest rate
                          x-description-cn: 日利率
                        type:
                          type: string
                          example: ON_BORROW
                          description: Normal order type after trigger if appliable
                          x-description-cn: 条件单触发后普通订单类型
                    description: Rows.
                    x-description-cn: Rows.
                  total:
                    type: integer
                    example: 1
                    format: int64
                    description: Total.
                    x-description-cn: Total.
  /papi/v1/um/account:
    get:
      summary: Get UM Account Detail (USER_DATA)
      x-summary-cn: 获取UM账户信息 (USER_DATA)
      description: Get current UM account asset and position information.
      x-description-cn: 现有UM账户资产和仓位信息
      tags:
        - account
      operationId: getUmAccountDetail
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-account-detail
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmAccountDetail.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_account_detail.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_account_detail.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmAccountDetailExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmAccountDetail/GetUmAccountDetail.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmAccountDetailExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get UM Account Detail
          x-description-cn: 获取UM 账户 Detail
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
                          example: USDT
                          description: asset name
                          x-description-cn: 资产
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: wallet balance
                          x-description-cn: 全仓账户余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit
                          x-description-cn: 全仓持仓未实现盈亏
                        maintMargin:
                          type: string
                          example: "0.00000000"
                          description: maintenance margin required
                          x-description-cn: 维持保证金
                        initialMargin:
                          type: string
                          example: "0.00000000"
                          description: total initial margin required with current mark price
                          x-description-cn: 当前所需起始保证金
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: initial margin required for positions with current mark price
                          x-description-cn: 持仓所需起始保证金(基于最新标记价格)
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: initial margin required for open orders with current mark price
                          x-description-cn: 当前挂单所需起始保证金(基于最新标记价格)
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
                          description: last update time
                          x-description-cn: 更新时间
                    description: Assets.
                    x-description-cn: Assets.
                  positions:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          description: symbol name
                          x-description-cn: 交易对
                        initialMargin:
                          type: string
                          example: "0"
                          description: total initial margin required with current mark price
                          x-description-cn: 当前所需起始保证金
                        maintMargin:
                          type: string
                          example: "0"
                          description: maintenance margin required
                          x-description-cn: 维持保证金
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit
                          x-description-cn: 持仓未实现盈亏
                        positionInitialMargin:
                          type: string
                          example: "0"
                          description: initial margin required for positions with current mark price
                          x-description-cn: 持仓所需起始保证金(基于最新标记价格)
                        openOrderInitialMargin:
                          type: string
                          example: "0"
                          description: initial margin required for open orders with current mark price
                          x-description-cn: 当前挂单所需起始保证金(基于最新标记价格)
                        leverage:
                          type: string
                          example: "100"
                          description: current initial leverage
                          x-description-cn: 杠杆倍率
                        entryPrice:
                          type: string
                          example: "0.00000"
                          description: average entry price
                          x-description-cn: 持仓成本价
                        maxNotional:
                          type: string
                          example: "250000"
                          description: maximum available notional with current leverage
                          x-description-cn: 当前杠杆下用户可用的最大名义价值
                        bidNotional:
                          type: string
                          example: "0"
                          description: bids notional, ignore
                          x-description-cn: 买单净值，忽略
                        askNotional:
                          type: string
                          example: "0"
                          description: ask notional, ignore
                          x-description-cn: 卖单净值，忽略
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
                          description: last update time
                          x-description-cn: 更新时间
                    description: positions of all symbols in the market are returned
                    x-description-cn: 头寸，将返回所有市场symbol。
  /papi/v2/um/account:
    get:
      summary: Get UM Account Detail V2 (USER_DATA)
      x-summary-cn: 获取UM账户信息V2 (USER_DATA)
      description: Get current UM account asset and position information.
      x-description-cn: 现有UM账户资产和仓位信息
      tags:
        - account
      operationId: getUmAccountDetailV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-account-detail-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmAccountDetailV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_account_detail_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_account_detail_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmAccountDetailV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmAccountDetailV2/GetUmAccountDetailV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmAccountDetailV2Example.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get UM Account Detail V2
          x-description-cn: 获取UM 账户 Detail V2
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
                          example: USDT
                          description: asset name
                          x-description-cn: 资产
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: wallet balance
                          x-description-cn: 全仓账户余额
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit
                          x-description-cn: 全仓持仓未实现盈亏
                        maintMargin:
                          type: string
                          example: "0.00000000"
                          description: maintenance margin required
                          x-description-cn: 维持保证金
                        initialMargin:
                          type: string
                          example: "0.00000000"
                          description: total initial margin required with current mark price
                          x-description-cn: 当前所需起始保证金
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: initial margin required for positions with current mark price
                          x-description-cn: 持仓所需起始保证金(基于最新标记价格)
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: initial margin required for open orders with current mark price
                          x-description-cn: 当前挂单所需起始保证金(基于最新标记价格)
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
                          description: last update time
                          x-description-cn: 更新时间
                    description: Assets.
                    x-description-cn: Assets.
                  positions:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          description: symbol name
                          x-description-cn: 交易对
                        initialMargin:
                          type: string
                          example: "0"
                          description: total initial margin required with current mark price
                          x-description-cn: 当前所需起始保证金
                        maintMargin:
                          type: string
                          example: "0"
                          description: maintenance margin required
                          x-description-cn: 维持保证金
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: unrealized profit
                          x-description-cn: 持仓未实现盈亏
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
                          description: last update time
                          x-description-cn: 更新时间
                        notional:
                          type: string
                          example: "86.98650000"
                          description: Notional.
                          x-description-cn: Notional.
                    description: positions of all symbols in the market are returned
                    x-description-cn: 头寸，将返回所有市场symbol。
  /papi/v1/um/order/asyn/id:
    get:
      summary: Get UM Futures Order Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取UM合约订单历史下载链接 (USER_DATA)
      description: Get UM futures order download link by Id
      x-description-cn: 通过下载Id获取UM合约订单历史下载链接
      tags:
        - account
      operationId: getUmFuturesOrderDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-futures-order-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmFuturesOrderDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_futures_order_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_futures_order_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmFuturesOrderDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmFuturesOrderDownloadLinkById/GetUmFuturesOrderDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmFuturesOrderDownloadLinkByIdExample.php
      x-ip-weight: 10
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get UM Futures Order Download Link by Id
          x-description-cn: 获取UM 合约 订单 Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download ID.
                    x-description-cn: Download ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 状态，枚举类型：completed 已完成，processing 处理中
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  s3Link:
                    type: string
                    example: "null"
                    description: S3 Link.
                    x-description-cn: S3 Link.
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
                    description: Is Expired.
                    x-description-cn: Is Expired.
  /papi/v1/um/trade/asyn/id:
    get:
      summary: Get UM Futures Trade Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取UM合约交易历史下载链接 (USER_DATA)
      description: Get UM futures trade download link by Id
      x-description-cn: 通过下载Id获取UM合约交易历史下载链接
      tags:
        - account
      operationId: getUmFuturesTradeDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-futures-trade-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmFuturesTradeDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_futures_trade_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_futures_trade_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmFuturesTradeDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmFuturesTradeDownloadLinkById/GetUmFuturesTradeDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmFuturesTradeDownloadLinkByIdExample.php
      x-ip-weight: 10
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get UM Futures Trade Download Link by Id
          x-description-cn: 获取UM 合约 交易 Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download ID.
                    x-description-cn: Download ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 状态，枚举类型：completed 已完成，processing 处理中
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  s3Link:
                    type: string
                    example: "null"
                    description: S3 Link.
                    x-description-cn: S3 Link.
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
                    description: Is Expired.
                    x-description-cn: Is Expired.
  /papi/v1/um/income/asyn/id:
    get:
      summary: Get UM Futures Transaction Download Link by Id (USER_DATA)
      x-summary-cn: 通过下载Id获取UM合约资金流水历史下载链接 (USER_DATA)
      description: Get UM futures Transaction download link by Id
      x-description-cn: 通过下载Id获取UM合约资金流水历史下载链接
      tags:
        - account
      operationId: getUmFuturesTransactionDownloadLinkById
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-futures-transaction-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmFuturesTransactionDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_futures_transaction_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_futures_transaction_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmFuturesTransactionDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmFuturesTransactionDownloadLinkById/GetUmFuturesTransactionDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmFuturesTransactionDownloadLinkByIdExample.php
      x-ip-weight: 10
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
            example: "1"
          description: get by download id api
          x-description-cn: 通过下载id 接口获取
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Download link expiration: 7 days"
      x-parameters-notes-cn: "- 下载链接有效期：7天。"
      responses:
        "200":
          description: Get UM Futures Transaction Download Link by Id
          x-description-cn: 获取UM 合约 Transaction Download Link by ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  downloadId:
                    type: string
                    example: "545923594199212032"
                    description: Download ID.
                    x-description-cn: Download ID.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 状态，枚举类型：completed 已完成，processing 处理中
                  url:
                    type: string
                    example: ""
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  s3Link:
                    type: string
                    example: "null"
                    description: S3 Link.
                    x-description-cn: S3 Link.
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
                    description: Is Expired.
                    x-description-cn: Is Expired.
  /papi/v1/um/income:
    get:
      summary: Get UM Income History (USER_DATA)
      x-summary-cn: 获取UM损益资金流水 (USER_DATA)
      description: Get UM Income History.
      x-description-cn: 获取UM损益资金流水。
      tags:
        - account
      operationId: getUmIncomeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-um-income-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUmIncomeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_um_income_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_um_income_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUmIncomeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUmIncomeHistory/GetUmIncomeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUmIncomeHistoryExample.php
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
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: incomeType
          in: query
          required: false
          schema:
            type: string
            example: TRANSFER
            enum:
              - TRANSFER
              - WELCOME_BONUS
              - REALIZED_PNL
              - FUNDING_FEE
              - COMMISSION
              - INSURANCE_CLEAR
              - REFERRAL_KICKBACK
              - COMMISSION_REBATE
              - API_REBATE
              - CONTEST_REWARD
              - CROSS_COLLATERAL_TRANSFER
              - OPTIONS_PREMIUM_FEE
              - OPTIONS_SETTLE_PROFIT
              - INTERNAL_TRANSFER
              - DELIVERED_SETTELMENT
              - COIN_SWAP_DEPOSIT
              - COIN_SWAP_WITHDRAW
              - POSITION_LIMIT_INCREASE_FEE
          description: Income type.
          x-description-cn: 收益类型。
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
            example: 100
            default: 100
            maximum: 1000
            format: int64
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
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
        - If neither `startTime` nor `endTime` is sent, the recent 7-day data will be returned.
        - If `incomeType` is not sent, all kinds of flow will be returned
        - "trandId" is unique in the same incomeType for a user
        - Income history only contains data for the last three months
      x-parameters-notes-cn: |-
        - 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据.
        - 如果`incomeType`没有发送，返回所有类型账户损益资金流水。
        - `trandId` 在相同用户的同一种收益流水类型中是唯一的。
        - 仅保留最近3个月的数据。
      responses:
        "200":
          description: Get UM Income History
          x-description-cn: 获取UM损益资金流水
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    incomeType:
                      type: string
                      example: TRANSFER
                      description: Income type.
                      x-description-cn: 收益类型。
                    income:
                      type: string
                      example: "-0.37500000"
                      description: Income amount.
                      x-description-cn: 收益金额。
                    asset:
                      type: string
                      example: USDT
                      description: Income asset.
                      x-description-cn: 收益资产。
                    info:
                      type: string
                      example: TRANSFER
                      description: Extra information.
                      x-description-cn: 附加信息。
                    time:
                      type: integer
                      example: 1570608000000
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    tranId:
                      type: string
                      example: "9689322392"
                      description: Transaction ID.
                      x-description-cn: 交易ID。
                    tradeId:
                      type: string
                      example: ""
                      description: Trade ID, if existing.
                      x-description-cn: 成交ID（如存在）。
  /papi/v1/cm/commissionRate:
    get:
      summary: Get User Commission Rate for CM (USER_DATA)
      x-summary-cn: 查询用户CM手续费率 (USER_DATA)
      description: Get User Commission Rate for CM
      x-description-cn: 查询用户CM手续费率
      tags:
        - account
      operationId: getUserCommissionRateForCm
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-user-commission-rate-for-cm
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUserCommissionRateForCm.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_user_commission_rate_for_cm.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_user_commission_rate_for_cm.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUserCommissionRateForCmExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUserCommissionRateForCm/GetUserCommissionRateForCm.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUserCommissionRateForCmExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get User Commission Rate for CM
          x-description-cn: 获取用户 手续费 利率 用于 CM
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSD_PERP
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  makerCommissionRate:
                    type: string
                    example: "0.00015"
                    description: 0.015%
                    x-description-cn: 0.015%
                  takerCommissionRate:
                    type: string
                    example: "0.00040"
                    description: 0.040%
                    x-description-cn: 0.040%
  /papi/v1/um/commissionRate:
    get:
      summary: Get User Commission Rate for UM (USER_DATA)
      x-summary-cn: 查询用户UM手续费率 (USER_DATA)
      description: Get User Commission Rate for UM
      x-description-cn: 查询用户UM手续费率
      tags:
        - account
      operationId: getUserCommissionRateForUm
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#get-user-commission-rate-for-um
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/getUserCommissionRateForUm.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/get_user_commission_rate_for_um.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/get_user_commission_rate_for_um.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/GetUserCommissionRateForUmExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/GetUserCommissionRateForUm/GetUserCommissionRateForUm.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/GetUserCommissionRateForUmExample.php
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
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get User Commission Rate for UM
          x-description-cn: 获取用户 手续费 利率 用于 UM
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  makerCommissionRate:
                    type: string
                    example: "0.0002"
                    description: 0.02%
                    x-description-cn: 0.02%
                  takerCommissionRate:
                    type: string
                    example: "0.0004"
                    description: 0.04%
                    x-description-cn: 0.04%
  /papi/v1/margin/maxBorrowable:
    get:
      summary: Margin Max Borrow (USER_DATA)
      x-summary-cn: 查询账户最大可借贷额度 (USER_DATA)
      description: Query margin max borrow
      x-description-cn: 查询账户最大可借贷额度
      tags:
        - account
      operationId: marginMaxBorrow
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#margin-max-borrow
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/marginMaxBorrow.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/margin_max_borrow.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/margin_max_borrow.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/MarginMaxBorrowExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/MarginMaxBorrow/MarginMaxBorrow.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/MarginMaxBorrowExample.php
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
        - name: asset
          in: query
          required: true
          schema:
            type: string
            example: USDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than `60000`
          x-description-cn: 赋值不能超过 `60000`
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Max Borrow
          x-description-cn: 杠杆 最大 借款
          content:
            application/json:
              schema:
                type: object
                properties:
                  amount:
                    type: string
                    example: "1.69248805"
                    description: account's currently max borrowable amount with sufficient system availability
                    x-description-cn: 系统可借充足情况下用户账户当前最大可借额度
                  borrowLimit:
                    type: string
                    example: "60"
                    description: max borrowable amount limited by the account level
                    x-description-cn: 平台限制的用户当前等级可以借的额度
  /papi/v1/um/apiTradingStatus:
    get:
      summary: Portfolio Margin UM Trading Quantitative Rules Indicators (USER_DATA)
      x-summary-cn: 统一账户UM合约交易量化规则指标 (USER_DATA)
      description: Portfolio Margin UM Trading Quantitative Rules Indicators
      x-description-cn: 查询合约交易量化规则指标
      tags:
        - account
      operationId: portfolioMarginUmTradingQuantitativeRulesIndicators
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#portfolio-margin-um-trading-quantitative-rules-indicators
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/portfolioMarginUmTradingQuantitativeRulesIndicators.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/portfolio_margin_um_trading_quantitative_rules_indicators.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/portfolio_margin_um_trading_quantitative_rules_indicators.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/PortfolioMarginUmTradingQuantitativeRulesIndicatorsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/PortfolioMarginUmTradingQuantitativeRulesIndicators/PortfolioMarginUmTradingQuantitativeRulesIndicators.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/PortfolioMarginUmTradingQuantitativeRulesIndicatorsExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 1 for a single `symbol`
        - 10 when `symbol` is omitted
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
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Portfolio Margin UM Trading Quantitative Rules Indicators
          x-description-cn: Portfolio 杠杆 UM Trading Quantitative Rules Indicators
          content:
            application/json:
              schema:
                type: object
                properties:
                  indicators:
                    type: object
                    properties:
                      BTCUSDT:
                        type: array
                        items:
                          type: object
                          properties:
                            isLocked:
                              type: boolean
                              example: true
                              description: Is Locked.
                              x-description-cn: Is Locked.
                            plannedRecoverTime:
                              type: integer
                              example: 1545741270000
                              format: int64
                              description: Planned Recover Time.
                              x-description-cn: Planned Recover Time.
                            indicator:
                              type: string
                              example: UFR
                              description: Indicator.
                              x-description-cn: Indicator.
                            value:
                              type: number
                              example: 0.05
                              format: float
                              description: Value.
                              x-description-cn: Value.
                            triggerValue:
                              type: number
                              example: 0.995
                              format: float
                              description: Trigger Value.
                              x-description-cn: Trigger Value.
                        description: BTCUSDT.
                        x-description-cn: BTCUSDT.
                      ACCOUNT:
                        type: array
                        items:
                          type: object
                          properties:
                            indicator:
                              type: string
                              example: TMV
                              description: Indicator.
                              x-description-cn: Indicator.
                            value:
                              type: integer
                              example: 10
                              format: int64
                              description: Value.
                              x-description-cn: Value.
                            triggerValue:
                              type: integer
                              example: 1
                              format: int64
                              description: Trigger Value.
                              x-description-cn: Trigger Value.
                            plannedRecoverTime:
                              type: integer
                              example: 1644919865000
                              format: int64
                              description: Planned Recover Time.
                              x-description-cn: Planned Recover Time.
                            isLocked:
                              type: boolean
                              example: true
                              description: Is Locked.
                              x-description-cn: Is Locked.
                        description: ACCOUNT.
                        x-description-cn: ACCOUNT.
                    description: Indicators.
                    x-description-cn: Indicators.
                  updateTime:
                    type: integer
                    example: 1644913304748
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
  /papi/v1/cm/positionRisk:
    get:
      summary: Query CM Position Information (USER_DATA)
      x-summary-cn: 用户CM持仓风险 (USER_DATA)
      description: Get current CM position information.
      x-description-cn: 获取用户CM持仓风险
      tags:
        - account
      operationId: queryCmPositionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-cm-position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryCmPositionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_cm_position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_cm_position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryCmPositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryCmPositionInformation/QueryCmPositionInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryCmPositionInformationExample.php
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
            example: BTCUSD_201225
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If neither `marginAsset` nor `pair` is sent, positions of all symbols with `TRADING` status will be returned.
        - for One-way Mode user, the response will only show the "BOTH" positions
        - for Hedge Mode user, the response will show "LONG", and "SHORT" positions. **Note**
        - Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.
      x-parameters-notes-cn: |-
        - `marginAsset` 和 `pair` 不要同时提供
        - `marginAsset` 和 `pair` 均不提供则返回所有上市状态和结算中的symbol
        - 对于单向持仓模式，仅会展示`BOTH`方向的持仓
        - 对于双向持仓模式，会展示所有`BOTH`，`LONG`，和`SHORT`方向的持仓
        - 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
      responses:
        "200":
          description: CM Position Information
          x-description-cn: CM 持仓 信息
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    positionAmt:
                      type: string
                      example: "0"
                      description: position amount
                      x-description-cn: position amount
                    entryPrice:
                      type: string
                      example: "0.0"
                      description: average entry price
                      x-description-cn: 持仓成本价
                    markPrice:
                      type: string
                      example: "0.00000000"
                      description: Mark Price.
                      x-description-cn: Mark Price.
                    unRealizedProfit:
                      type: string
                      example: "0.00000000"
                      description: Un Realized Profit.
                      x-description-cn: Un Realized Profit.
                    liquidationPrice:
                      type: string
                      example: "6170.20509059"
                      description: Liquidation Price.
                      x-description-cn: Liquidation Price.
                    leverage:
                      type: string
                      example: "125"
                      description: current initial leverage
                      x-description-cn: 杠杆倍率
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    updateTime:
                      type: integer
                      example: 0
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
                    maxQty:
                      type: string
                      example: "50"
                      description: maximum quantity of base asset
                      x-description-cn: maximum quantity of base asset
                    notionalValue:
                      type: string
                      example: "0.00084827"
                      description: Notional Value.
                      x-description-cn: Notional Value.
  /papi/v1/margin/marginLoan:
    get:
      summary: Query Margin Loan Record (USER_DATA)
      x-summary-cn: 查询杠杆借贷记录 (USER_DATA)
      description: Query margin loan record
      x-description-cn: 查询杠杆借贷记录
      tags:
        - account
      operationId: queryMarginLoanRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-margin-loan-record
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryMarginLoanRecord.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_margin_loan_record.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_margin_loan_record.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryMarginLoanRecordExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryMarginLoanRecord/QueryMarginLoanRecord.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryMarginLoanRecordExample.php
      x-ip-weight: 10
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
        - name: asset
          in: query
          required: true
          schema:
            type: string
            example: USDT
        - name: txId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: the `tranId` in `POST/papi/v1/marginLoan`
          x-description-cn: "`tran ID` in `POST/papi/v1/margin借贷`"
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
            minimum: 1
          description: Current page number.
          x-description-cn: 当前页码。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: archived
          in: query
          required: false
          schema:
            type: string
            example: "true"
            default: "false"
            enum:
              - "true"
              - "false"
          description: Set to true to query archived data from 6 months ago.
          x-description-cn: 设为 true 可查询 6 个月前的归档数据。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than 60000
          x-description-cn: 赋值不能超过 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - txId or startTime must be sent. txId takes precedence.
        - Response in descending order
        - The max interval between `startTime` and `endTime` is 30 days.
        - If `startTime` and `endTime` not sent, return records of the last 7 days by default
        - Set `archived` to `true` to query data from 6 months ago
      x-parameters-notes-cn: |-
        - 必须发送txId 或 startTime，txId 优先
        - 响应返回为降序排列。
        - 查询时间范围最大不得超过30天。
        - 若startTime和endTime没传，则默认返回最近7天数据
        - 如果想查询6个月以前数据，设置 archived 为 true
      responses:
        "200":
          description: Margin Loan Record
          x-description-cn: 杠杆 借贷 Record
          content:
            application/json:
              schema:
                type: object
                properties:
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        txId:
                          type: integer
                          example: 12807067523
                          format: int64
                          description: Tx ID.
                          x-description-cn: Tx ID.
                        asset:
                          type: string
                          example: BNB
                          description: asset name
                          x-description-cn: 资产
                        principal:
                          type: string
                          example: "0.84624403"
                          description: Principal repaid
                          x-description-cn: 支付的本金
                        timestamp:
                          type: integer
                          example: 1555056425000
                          format: int64
                          description: Timestamp.
                          x-description-cn: Timestamp.
                        status:
                          type: string
                          example: CONFIRMED
                          description: >-
                            one of PENDING (pending execution), CONFIRMED (successfully loaned), FAILED (execution
                            failed, nothing happened to your account);
                          x-description-cn: "状态: PENDING (等待执行), CONFIRMED (成功借贷), FAILED (执行失败);"
                    description: Rows.
                    x-description-cn: Rows.
                  total:
                    type: integer
                    example: 1
                    format: int64
                    description: Total.
                    x-description-cn: Total.
  /papi/v1/margin/maxWithdraw:
    get:
      summary: Query Margin Max Withdraw (USER_DATA)
      x-summary-cn: 查询账户最大可转出额度 (USER_DATA)
      description: Query Margin Max Withdraw
      x-description-cn: 查询账户最大可转出额度
      tags:
        - account
      operationId: queryMarginMaxWithdraw
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-margin-max-withdraw
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryMarginMaxWithdraw.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_margin_max_withdraw.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_margin_max_withdraw.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryMarginMaxWithdrawExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryMarginMaxWithdraw/QueryMarginMaxWithdraw.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryMarginMaxWithdrawExample.php
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
        - name: asset
          in: query
          required: true
          schema:
            type: string
            example: USDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Max Withdraw
          x-description-cn: 杠杆 最大 Withdraw
          content:
            application/json:
              schema:
                type: object
                properties:
                  amount:
                    type: string
                    example: "60"
                    description: account's currently max withdrawable amount with sufficient system availability
                    x-description-cn: 系统可用充足情况下用户账户当前最大可转出额度
  /papi/v1/margin/repayLoan:
    get:
      summary: Query Margin repay Record (USER_DATA)
      x-summary-cn: 查询杠杆还贷记录 (USER_DATA)
      description: Query margin repay record.
      x-description-cn: 查询杠杆还贷记录
      tags:
        - account
      operationId: queryMarginRepayRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-margin-repay-record
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryMarginRepayRecord.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_margin_repay_record.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_margin_repay_record.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryMarginRepayRecordExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryMarginRepayRecord/QueryMarginRepayRecord.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryMarginRepayRecordExample.php
      x-ip-weight: 10
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
        - name: asset
          in: query
          required: true
          schema:
            type: string
            example: USDT
        - name: txId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: the `tranId` in `POST /papi/v1/repayLoan`
          x-description-cn: "`tran ID` in `POST /papi/v1/repayLoan`"
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
            minimum: 1
          description: Current page number.
          x-description-cn: 当前页码。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: archived
          in: query
          required: false
          schema:
            type: string
            example: "true"
            default: "false"
            enum:
              - "true"
              - "false"
          description: Set to true to query archived data from 6 months ago.
          x-description-cn: 设为 true 可查询 6 个月前的归档数据。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - txId or startTime must be sent. txId takes precedence.
        - Response in descending order
        - The max interval between `startTime` and `endTime` is 30 days.
        - If `startTime` and `endTime` not sent, return records of the last 7 days by default
        - Set `archived` to `true` to query data from 6 months ago
      x-parameters-notes-cn: |-
        - 必须发送txId 或 startTime，txId 优先
        - 响应返回为降序排列。
        - 查询时间范围最大不得超过30天。
        - 若startTime和endTime没传，则默认返回最近7天数据
        - 如果想查询6个月以前数据，设置 archived 为 true
      responses:
        "200":
          description: Margin repay Record
          x-description-cn: 杠杆 还款 Record
          content:
            application/json:
              schema:
                type: object
                properties:
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        amount:
                          type: string
                          example: "14.00000000"
                          description: Total amount repaid
                          x-description-cn: 还款总额
                        asset:
                          type: string
                          example: BNB
                          description: asset name
                          x-description-cn: 资产
                        interest:
                          type: string
                          example: "0.01866667"
                          description: Interest repaid
                          x-description-cn: 支付的利息
                        principal:
                          type: string
                          example: "13.98133333"
                          description: Principal repaid
                          x-description-cn: 支付的本金
                        status:
                          type: string
                          example: CONFIRMED
                          description: >-
                            one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution
                            failed, nothing happened to your account)
                          x-description-cn: "状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);"
                        timestamp:
                          type: integer
                          example: 1563438204000
                          format: int64
                          description: Timestamp.
                          x-description-cn: Timestamp.
                        txId:
                          type: integer
                          example: 2970933056
                          format: int64
                          description: Tx ID.
                          x-description-cn: Tx ID.
                    description: Rows.
                    x-description-cn: Rows.
                  total:
                    type: integer
                    example: 1
                    format: int64
                    description: Total.
                    x-description-cn: Total.
  /papi/v1/portfolio/interest-history:
    get:
      summary: Query Portfolio Margin Negative Balance Interest History (USER_DATA)
      x-summary-cn: 查询统一账户期货负余额收息历史 (USER_DATA)
      description: Query interest history of negative balance for portfolio margin.
      x-description-cn: 查询统一账户期货负余额收息历史
      tags:
        - account
      operationId: queryPortfolioMarginNegativeBalanceInterestHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-portfolio-margin-negative-balance-interest-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryPortfolioMarginNegativeBalanceInterestHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_portfolio_margin_negative_balance_interest_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_portfolio_margin_negative_balance_interest_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryPortfolioMarginNegativeBalanceInterestHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryPortfolioMarginNegativeBalanceInterestHistory/QueryPortfolioMarginNegativeBalanceInterestHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryPortfolioMarginNegativeBalanceInterestHistoryExample.php
      x-ip-weight: 50
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
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: USDT
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
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Results are returned in descending order.

        - The query range cannot exceed 30 days to ensure data correctness.

        - If both `startTime` and `endTime` are omitted, the most recent 7 days are returned by default.

        - If `startTime` is provided but `endTime` is omitted, records from `startTime` to now are returned; if that
        exceeds 30 days, only the most recent 30 days are returned.

        - If `endTime` is provided but `startTime` is omitted, records from the 7 days before `endTime` are returned.
      x-parameters-notes-cn: |-
        - 响应返回为降序排列。
        - 查询时间范围最大不得超过30天，这是确保数据正确性必须的。
        - 若`startTime`和`endTime`没传，则默认返回最近7天数据。
        - 如果发送了`startTime`且未发送`endTime`，则返回`startTime`到现在的的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
        - 如果没有发送`startTime`而发送了`endTime`，则返回`endTime`之前7天的利息历史记录。
      responses:
        "200":
          description: Portfolio Margin Negative Balance Interest History
          x-description-cn: Portfolio 杠杆 Negative Balance 利息 历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: USDT
                      description: asset name
                      x-description-cn: 资产
                    interest:
                      type: string
                      example: "24.4440"
                      description: interest amount
                      x-description-cn: 利息金额
                    interestAccuredTime:
                      type: integer
                      example: 1670227200000
                      format: int64
                      description: Interest Accured Time.
                      x-description-cn: Interest Accured Time.
                    interestRate:
                      type: string
                      example: "0.0001164"
                      description: daily interest rate
                      x-description-cn: 日利率
                    principal:
                      type: string
                      example: "210000"
                      description: Principal repaid
                      x-description-cn: 支付的本金
  /papi/v1/um/positionRisk:
    get:
      summary: Query UM Position Information (USER_DATA)
      x-summary-cn: 用户UM持仓风险 (USER_DATA)
      description: Get current UM position information.
      x-description-cn: 获取用户UM持仓风险
      tags:
        - account
      operationId: queryUmPositionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-um-position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryUmPositionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_um_position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_um_position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryUmPositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryUmPositionInformation/QueryUmPositionInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryUmPositionInformationExample.php
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
            example: BTCUSDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Please use with account push event `ACCOUNT_UPDATE` for timeliness and accuracy.
        - In One-way Mode, only positions with side `BOTH` are shown.
        - In Hedge Mode, positions with sides `BOTH`, `LONG`, and `SHORT` are shown.
      x-parameters-notes-cn: |-
        - 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
        - 对于单向持仓模式，仅会展示`BOTH`方向的持仓
        - 对于双向持仓模式，会展示所有`BOTH`，`LONG`，和`SHORT`方向的持仓
      responses:
        "200":
          description: UM Position Information
          x-description-cn: UM 持仓 信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    entryPrice:
                      type: string
                      example: "0.00000"
                      description: average entry price
                      x-description-cn: 持仓成本价
                    leverage:
                      type: string
                      example: "10"
                      description: current initial leverage
                      x-description-cn: 杠杆倍率
                    markPrice:
                      type: string
                      example: "6679.50671178"
                      description: Mark Price.
                      x-description-cn: Mark Price.
                    maxNotionalValue:
                      type: string
                      example: "20000000"
                      description: Max Notional Value.
                      x-description-cn: Max Notional Value.
                    positionAmt:
                      type: string
                      example: "0.000"
                      description: position amount
                      x-description-cn: position amount
                    notional:
                      type: string
                      example: "0"
                      description: Notional.
                      x-description-cn: Notional.
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    unRealizedProfit:
                      type: string
                      example: "0.00000000"
                      description: Un Realized Profit.
                      x-description-cn: Un Realized Profit.
                    liquidationPrice:
                      type: string
                      example: "6170.20509059"
                      description: Liquidation Price.
                      x-description-cn: Liquidation Price.
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    updateTime:
                      type: integer
                      example: 1625474304765
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
  /papi/v1/portfolio/negative-balance-exchange-record:
    get:
      summary: Query User Negative Balance Auto Exchange Record (USER_DATA)
      x-summary-cn: 查询用户负余额自动兑换记录 (USER_DATA)
      description: Query user negative balance auto exchange record
      x-description-cn: 查询用户负余额自动兑换记录
      tags:
        - account
      operationId: queryUserNegativeBalanceAutoExchangeRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-user-negative-balance-auto-exchange-record
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryUserNegativeBalanceAutoExchangeRecord.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_user_negative_balance_auto_exchange_record.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_user_negative_balance_auto_exchange_record.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryUserNegativeBalanceAutoExchangeRecordExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryUserNegativeBalanceAutoExchangeRecord/QueryUserNegativeBalanceAutoExchangeRecord.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryUserNegativeBalanceAutoExchangeRecordExample.php
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
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Response in descending order
        - The max interval between `startTime` and `endTime` is 3 months.
      x-parameters-notes-cn: |-
        - 响应返回为降序排列。
        - 查询时间范围最大不得超过3个月。
      responses:
        "200":
          description: User Negative Balance Auto Exchange Record
          x-description-cn: 用户 Negative Balance Auto Exchange Record
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 2
                    format: int64
                    description: Total.
                    x-description-cn: Total.
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        startTime:
                          type: integer
                          example: 1736263046841
                          format: int64
                          description: Start Time.
                          x-description-cn: Start Time.
                        endTime:
                          type: integer
                          example: 1736263248179
                          format: int64
                          description: End Time.
                          x-description-cn: End Time.
                        details:
                          type: array
                          items:
                            type: object
                            properties:
                              asset:
                                type: string
                                example: ETH
                                description: asset name
                                x-description-cn: 资产
                              negativeBalance:
                                type: number
                                example: 1.10264488
                                format: float
                                description: negative balance amount
                                x-description-cn: 当前负余额值
                              negativeMaxThreshold:
                                type: integer
                                example: 5
                                format: int64
                                description: the max negative balance threshold
                                x-description-cn: 该资产触发自动兑换的阈值
                          description: Details.
                          x-description-cn: Details.
                    description: Rows.
                    x-description-cn: Rows.
  /papi/v1/rateLimit/order:
    get:
      summary: Query User Rate Limit (USER_DATA)
      x-summary-cn: 查询用户下单限频 (USER_DATA)
      description: Query User Rate Limit
      x-description-cn: 查询用户下单限频
      tags:
        - account
      operationId: queryUserRateLimit
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#query-user-rate-limit
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/queryUserRateLimit.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/query_user_rate_limit.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/query_user_rate_limit.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/QueryUserRateLimitExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/QueryUserRateLimit/QueryUserRateLimit.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/QueryUserRateLimitExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: User Rate Limit
          x-description-cn: 用户 频率限制
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    rateLimitType:
                      type: string
                      example: ORDERS
                      description: Rate Limit Type.
                      x-description-cn: Rate Limit Type.
                    interval:
                      type: string
                      example: MINUTE
                      description: Interval.
                      x-description-cn: Interval.
                    intervalNum:
                      type: integer
                      example: 1
                      format: int64
                      description: Interval Num.
                      x-description-cn: Interval Num.
                    limit:
                      type: integer
                      example: 1200
                      format: int64
                      description: Limit.
                      x-description-cn: Limit.
  /papi/v1/repay-futures-negative-balance:
    post:
      summary: Repay futures Negative Balance (USER_DATA)
      x-summary-cn: 清还合约负余额 (USER_DATA)
      description: Repay futures Negative Balance
      x-description-cn: 清还合约负余额
      tags:
        - account
      operationId: repayFuturesNegativeBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#repay-futures-negative-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/repayFuturesNegativeBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/repay_futures_negative_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/repay_futures_negative_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/RepayFuturesNegativeBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/RepayFuturesNegativeBalance/RepayFuturesNegativeBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/RepayFuturesNegativeBalanceExample.php
      x-ip-weight: 750
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Repay futures Negative Balance
          x-description-cn: 还款 合约 Negative Balance
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/um/accountConfig:
    get:
      summary: UM Futures Account Configuration (USER_DATA)
      x-summary-cn: 账户配置 (USER_DATA)
      description: Query UM Futures account configuration
      x-description-cn: 查询UM 合约 账户 configuration
      tags:
        - account
      operationId: umFuturesAccountConfiguration
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#um-futures-account-configuration
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/umFuturesAccountConfiguration.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/um_futures_account_configuration.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/um_futures_account_configuration.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/UmFuturesAccountConfigurationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/UmFuturesAccountConfiguration/UmFuturesAccountConfiguration.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/UmFuturesAccountConfigurationExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: UM Futures Account Configuration
          x-description-cn: UM 合约 账户 Configuration
          content:
            application/json:
              schema:
                type: object
                properties:
                  feeTier:
                    type: integer
                    example: 0
                    format: int64
                    description: account commission tier
                    x-description-cn: 费率等级
                  canTrade:
                    type: boolean
                    example: true
                    description: if can trade
                    x-description-cn: 是否可以交易
                  canDeposit:
                    type: boolean
                    example: true
                    description: if can transfer in asset
                    x-description-cn: 是否可以存款
                  canWithdraw:
                    type: boolean
                    example: true
                    description: if can transfer out asset
                    x-description-cn: 是否可以提现
                  dualSidePosition:
                    type: boolean
                    example: true
                    description: '"true": Hedge Mode; "false": One-way Mode'
                    x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
                  updateTime:
                    type: integer
                    example: 1724416653850
                    format: int64
                    description: reserved property, please ignore
                    x-description-cn: 忽略
                  multiAssetsMargin:
                    type: boolean
                    example: false
                    description: Multi Assets Margin.
                    x-description-cn: Multi Assets Margin.
                  tradeGroupId:
                    type: integer
                    example: -1
                    format: int64
                    description: Trade Group ID.
                    x-description-cn: Trade Group ID.
  /papi/v1/um/symbolConfig:
    get:
      summary: UM Futures Symbol Configuration (USER_DATA)
      x-summary-cn: 交易对配置 (USER_DATA)
      description: Get current UM account symbol configuration.
      x-description-cn: 查询UM合约交易对上的基础配置
      tags:
        - account
      operationId: umFuturesSymbolConfiguration
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#um-futures-symbol-configuration
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/umFuturesSymbolConfiguration.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/um_futures_symbol_configuration.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/um_futures_symbol_configuration.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/UmFuturesSymbolConfigurationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/UmFuturesSymbolConfiguration/UmFuturesSymbolConfiguration.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/UmFuturesSymbolConfigurationExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: UM Futures Symbol Configuration
          x-description-cn: UM 合约 交易对 Configuration
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    marginType:
                      type: string
                      example: CROSSED
                      description: Margin Type.
                      x-description-cn: Margin Type.
                    isAutoAddMargin:
                      type: string
                      example: "false"
                      description: Is Auto Add Margin.
                      x-description-cn: Is Auto Add Margin.
                    leverage:
                      type: integer
                      example: 21
                      format: int64
                      description: current initial leverage
                      x-description-cn: 杠杆倍率
                    maxNotionalValue:
                      type: string
                      example: "1000000"
                      description: Max Notional Value.
                      x-description-cn: Max Notional Value.
  /papi/v1/um/leverageBracket:
    get:
      summary: UM Notional and Leverage Brackets (USER_DATA)
      x-summary-cn: 查询UM杠杆分层标准 (USER_DATA)
      description: Query UM notional and leverage brackets
      x-description-cn: 查询UM杠杆分层标准
      tags:
        - account
      operationId: umNotionalAndLeverageBrackets
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/account#um-notional-and-leverage-brackets
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/AccountApi/umNotionalAndLeverageBrackets.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/account_api/um_notional_and_leverage_brackets.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Account/um_notional_and_leverage_brackets.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/account/UmNotionalAndLeverageBracketsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/AccountAPI/UmNotionalAndLeverageBrackets/UmNotionalAndLeverageBrackets.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/account/UmNotionalAndLeverageBracketsExample.php
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
            example: ETHUSDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: UM Notional and Leverage Brackets
          x-description-cn: UM Notional 和 Leverage Brackets
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ETHUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    notionalCoef:
                      type: string
                      example: "4.0"
                      description: Notional Coef.
                      x-description-cn: Notional Coef.
                    brackets:
                      type: array
                      items:
                        type: object
                        properties:
                          bracket:
                            type: integer
                            example: 1
                            format: int64
                            description: Notional bracket
                            x-description-cn: 层级
                          initialLeverage:
                            type: integer
                            example: 75
                            format: int64
                            description: Max initial leverage for this bracket
                            x-description-cn: 该层允许的最高初始杠杆倍数
                          notionalCap:
                            type: integer
                            example: 10000
                            format: int64
                            description: Cap notional of this bracket
                            x-description-cn: 该层对应的数量上限
                          notionalFloor:
                            type: integer
                            example: 0
                            format: int64
                            description: Notional threshold of this bracket
                            x-description-cn: 该层对应的数量下限
                          maintMarginRatio:
                            type: number
                            example: 0.0065
                            format: float
                            description: Maintenance ratio for this bracket
                            x-description-cn: 该层对应的维持保证金率
                          cum:
                            type: integer
                            example: 0
                            format: int64
                            description: Auxiliary number for quick calculation
                            x-description-cn: 速算数
                      description: Brackets.
                      x-description-cn: Brackets.
  /papi/v1/ping:
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
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/market-data#test-connectivity
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/MarketDataApi/testConnectivity.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/market_data_api/test_connectivity.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/MarketData/test_connectivity.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/marketdata/TestConnectivityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/MarketDataAPI/TestConnectivity/TestConnectivity.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/marketdata/TestConnectivityExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: OK
          x-description-cn: 成功
  /papi/v1/cm/conditional/allOpenOrders:
    delete:
      summary: Cancel All CM Open Conditional Orders (TRADE)
      x-summary-cn: 取消全部CM条件单 (TRADE)
      description: Cancel All CM Open Conditional Orders
      x-description-cn: 取消全部CM条件单
      tags:
        - trade
      operationId: cancelAllCmOpenConditionalOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-all-cm-open-conditional-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelAllCmOpenConditionalOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_all_cm_open_conditional_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_all_cm_open_conditional_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelAllCmOpenConditionalOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelAllCmOpenConditionalOrders/CancelAllCmOpenConditionalOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelAllCmOpenConditionalOrdersExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All CM Open Conditional Orders
          x-description-cn: 取消All CM 未完成Conditional 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "200"
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: The operation of cancel all conditional open order is done.
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/cm/allOpenOrders:
    delete:
      summary: Cancel All CM Open Orders (TRADE)
      x-summary-cn: 撤销全部CM订单 (TRADE)
      description: Cancel all active LIMIT orders on specific symbol
      x-description-cn: 撤销特定交易对全部CM订单
      tags:
        - trade
      operationId: cancelAllCmOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-all-cm-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelAllCmOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_all_cm_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_all_cm_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelAllCmOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelAllCmOpenOrders/CancelAllCmOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelAllCmOpenOrdersExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All CM Open Orders
          x-description-cn: 取消All CM 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/um/allOpenOrders:
    delete:
      summary: Cancel All UM Open Orders (TRADE)
      x-summary-cn: 撤销全部UM订单 (TRADE)
      description: Cancel all active LIMIT orders on specific symbol
      x-description-cn: 撤销特定交易对全部UM订单
      tags:
        - trade
      operationId: cancelAllUmOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-all-um-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelAllUmOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_all_um_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_all_um_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelAllUmOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelAllUmOpenOrders/CancelAllUmOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelAllUmOpenOrdersExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All UM Open Orders
          x-description-cn: 取消All UM 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/cm/conditional/order:
    delete:
      summary: Cancel CM Conditional Order (TRADE)
      x-summary-cn: 取消CM条件订单 (TRADE)
      description: Cancel CM Conditional Order
      x-description-cn: 取消CM条件订单
      tags:
        - trade
      operationId: cancelCmConditionalOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-cm-conditional-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelCmConditionalOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_cm_conditional_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_cm_conditional_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelCmConditionalOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelCmConditionalOrder/CancelCmConditionalOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelCmConditionalOrderExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: strategyId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: newClientStrategyId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `strategyId` or `newClientStrategyId` must be sent."
      x-parameters-notes-cn: "- `strategyId` 与 `newClientStrategyId` 之一必须发送"
      responses:
        "200":
          description: Cancel CM Conditional Order
          x-description-cn: 取消CM Conditional 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  newClientStrategyId:
                    type: string
                    example: myOrder1
                    description: New Client Strategy ID.
                    x-description-cn: New Client Strategy ID.
                  strategyId:
                    type: integer
                    example: 123445
                    format: int64
                    description: Strategy ID.
                    x-description-cn: Strategy ID.
                  strategyStatus:
                    type: string
                    example: CANCELED
                    description: Strategy Status.
                    x-description-cn: Strategy Status.
                  strategyType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Strategy Type.
                    x-description-cn: Strategy Type.
                  origQty:
                    type: string
                    example: "11"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                  symbol:
                    type: string
                    example: BTCUSD
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
                  bookTime:
                    type: integer
                    example: 1566818724710
                    format: int64
                    description: order place time
                    x-description-cn: 条件单下单时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    description: Working Type.
                    x-description-cn: Working Type.
                  priceProtect:
                    type: boolean
                    example: false
                    description: Price Protect.
                    x-description-cn: Price Protect.
    post:
      summary: New CM Conditional Order (TRADE)
      x-summary-cn: CM条件单下单 (TRADE)
      description: New CM Conditional Order
      x-description-cn: CM条件单下单
      tags:
        - trade
      operationId: newCmConditionalOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#new-cm-conditional-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/newCmConditionalOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/new_cm_conditional_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/new_cm_conditional_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/NewCmConditionalOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/NewCmConditionalOrder/NewCmConditionalOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/NewCmConditionalOrderExample.php
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
      x-parameters-notes: |-
        - Additional mandatory parameters based on type:
          - Order with type `STOP/TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`).
          - Condition orders will be triggered when:
          - `STOP`, `STOP_MARKET`:
          - BUY: "MARK_PRICE" >= `stopPrice`
          - SELL: "MARK_PRICE" <= `stopPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`:
          - BUY: "MARK_PRICE" <= `stopPrice`
          - SELL: "MARK_PRICE" >= `stopPrice`
          - `TRAILING_STOP_MARKET`:
          - BUY: the lowest mark price after order placed <= `activationPrice`, and the latest mark price >= the lowest mark price * (1 + `callbackRate`)
          - SELL: the highest mark price after order placed >= `activationPrice`, and the latest mark price <= the highest mark price * (1 - `callbackRate`)
          - For `TRAILING_STOP_MARKET`, if you got such error code. `{"code": -2021, "msg": "Order would immediately trigger."}` means that the parameters you send do not meet the following requirements:
          - BUY: `activationPrice` should be smaller than latest mark price.
          - SELL: `activationPrice` should be larger than latest mark price.
      x-parameters-notes-cn: |-
        - 根据 order `type` 的不同，某些参数强制要求，具体如下:
          - 条件单为`STOP/TAKE_PROFIT`时, 参数`timeInForce`可以使用(默认`GTC`)
          - 条件单的触发必须:
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
          - 买入: 指定的`activationPrice` 必须小于 latest mark price
          - 卖出: 指定的`activationPrice` 必须大于 latest mark price
          - 条件单的触发必须:
          - 如果订单参数`priceProtect`为true:
          - 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
          - 触发保护阈值请参考接口`GET /fapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
          - `STOP`, `STOP_MARKET` 止损单:
          - 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
          - 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单:
          - 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
          - 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - symbol
                - side
                - strategyType
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Symbol
                  x-description-cn: 交易对
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                  description: Side
                  x-description-cn: 方向
                positionSide:
                  type: string
                  example: BOTH
                  default: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
                strategyType:
                  type: string
                  example: STOP
                  enum:
                    - STOP
                    - STOP_MARKET
                    - TAKE_PROFIT
                    - TAKE_PROFIT_MARKET
                    - TRAILING_STOP_MARKET
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
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  description: '"true" or "false". default "false". Cannot be sent in Hedge Mode'
                  x-description-cn: "`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数"
                price:
                  type: number
                  example: "1.0"
                  format: float
                workingType:
                  type: string
                  example: MARK_PRICE
                  default: CONTRACT_PRICE
                  enum:
                    - MARK_PRICE
                    - CONTRACT_PRICE
                  description: 'stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"'
                  x-description-cn: "stopPrice 触发类型: `MARK_PRICE`, `CONTRACT_PRICE`. 默认 `CONTRACT_PRICE`"
                priceProtect:
                  type: string
                  example: "true"
                  default: "false"
                  description: >-
                    "true" or "false", default "false". Used with `STOP`/`STOP_MARKET` or
                    `TAKE_PROFIT`/`TAKE_PROFIT_MARKET` orders
                  x-description-cn: >-
                    条件单触发保护："true" or "false", 默认 "false". `STOP`/`STOP_MARKET` or `TAKE_PROFIT`/`TAKE_PROFIT_MARKET`
                    需要此参数
                  enum:
                    - "true"
                    - "false"
                newClientStrategyId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                  x-description-cn: '用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`'
                stopPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                  x-description-cn: Used 带 `STOP/STOP_MARKET` 或 `TAKE_PROFIT/TAKE_PROFIT_MARKET` 订单.
                activationPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `TRAILING_STOP_MARKET` orders.
                  x-description-cn: "`TRAILING_STOP_MARKET` 单使用，默认标记价格"
                callbackRate:
                  type: number
                  example: "1.0"
                  format: float
                  minimum: 0.1
                  maximum: 5
                  description: Used with `TRAILING_STOP_MARKET` orders.
                  x-description-cn: "`TRAILING_STOP_MARKET` 单使用, 最小0.1, 最大5，1代表1%"
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: New CM Conditional Order
          x-description-cn: New CM Conditional 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  newClientStrategyId:
                    type: string
                    example: testOrder
                    description: New Client Strategy ID.
                    x-description-cn: New Client Strategy ID.
                  strategyId:
                    type: integer
                    example: 123445
                    format: int64
                    description: Strategy ID.
                    x-description-cn: Strategy ID.
                  strategyStatus:
                    type: string
                    example: NEW
                    description: Strategy Status.
                    x-description-cn: Strategy Status.
                  strategyType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Strategy Type.
                    x-description-cn: Strategy Type.
                  origQty:
                    type: string
                    example: "10"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair.
                    x-description-cn: Pair.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
                  bookTime:
                    type: integer
                    example: 1566818724710
                    format: int64
                    description: order place time
                    x-description-cn: 条件单下单时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    description: Working Type.
                    x-description-cn: Working Type.
                  priceProtect:
                    type: boolean
                    example: false
                    description: Price Protect.
                    x-description-cn: Price Protect.
  /papi/v1/cm/order:
    delete:
      summary: Cancel CM Order (TRADE)
      x-summary-cn: 撤销CM订单 (TRADE)
      description: Cancel an active LIMIT order
      x-description-cn: 撤销CM订单
      tags:
        - trade
      operationId: cancelCmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-cm-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelCmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_cm_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_cm_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelCmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelCmOrder/CancelCmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelCmOrderExample.php
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
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 或 `origClientOrderId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel CM Order
          x-description-cn: 取消CM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: myOrder1
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 283194212
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "2"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: CANCELED
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair.
                    x-description-cn: Pair.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1571110484038
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
    put:
      summary: Modify CM Order (TRADE)
      x-summary-cn: 修改CM订单 (TRADE)
      description: >-
        Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered
        in the match queue
      x-description-cn: 修改CM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序
      tags:
        - trade
      operationId: modifyCmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#modify-cm-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/modifyCmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/modify_cm_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/modify_cm_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/ModifyCmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/ModifyCmOrder/ModifyCmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/ModifyCmOrderExample.php
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

        - Both `quantity` and `price` must be sent

        - When the new `quantity` or `price` doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be
        rejected and the order will stay as it is.

        - However the order will be cancelled by the amendment in the following situations:
          - when the order is in partially filled status and the new `quantity` <= `executedQty`
          - When the order is `GTX` and the new price will cause it to be executed immediately
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
        - `quantity` 与 `price` 必须全部发送
        - 当新订单的`quantity` 或 `price`不满足PRICE_FILTER / PERCENT_FILTER / LOT_SIZE限制，修改会被拒绝，原订单依旧被保留
        - 订单会在下列情况下被取消：
          - 原订单被部分执行且新订单`quantity` <= `executedQty`
          - 原订单是`GTX`，新订单的价格会导致订单立刻执行
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
                  description: Order quantity
                  x-description-cn: 下单数量
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order price
                  x-description-cn: 委托价格
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
                  description: >-
                    only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/
                    `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together
                    with `price`
                  x-description-cn: >-
                    `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/
                    `QUEUE_20`；不能与price同时传
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
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Modify CM Order
          x-description-cn: Modify CM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 20072994037
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  symbol:
                    type: string
                    example: BTCUSD_PERP
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair.
                    x-description-cn: Pair.
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  clientOrderId:
                    type: string
                    example: LJ9R4QZDihCaS8UAOOLpgW
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  modifyId:
                    type: integer
                    example: 1
                    format: int64
                    description: user-defined modification identifier, only returned if provided in the request
                    x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                  price:
                    type: string
                    example: "30005"
                    description: Price.
                    x-description-cn: Price.
                  origQty:
                    type: string
                    example: "1"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: LONG
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  origType:
                    type: string
                    example: LIMIT
                    description: Orig Type.
                    x-description-cn: Orig Type.
                  updateTime:
                    type: integer
                    example: 1629182711600
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
    post:
      summary: New CM Order (TRADE)
      x-summary-cn: CM下单 (TRADE)
      description: Place new CM order
      x-description-cn: CM下单
      tags:
        - trade
      operationId: newCmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#new-cm-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/newCmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/new_cm_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/new_cm_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/NewCmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/NewCmOrder/NewCmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/NewCmOrderExample.php
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
      x-parameters-notes: |-
        - Additional mandatory parameters based on `type`:
          - If `newOrderRespType` is sent as `RESULT` :
          - `MARKET` order: the final FILLED result of the order will be return directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
      x-parameters-notes-cn: |-
        - 根据 order `type`的不同，某些参数强制要求，具体如下:
        - `newOrderRespType` 如果传 `RESULT`:
        - `MARKET` 订单将直接返回成交结果；
        - 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
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
                  example: BTCUSDT
                  description: Symbol
                  x-description-cn: 交易对
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                  description: Side
                  x-description-cn: 方向
                positionSide:
                  type: string
                  example: BOTH
                  default: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
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
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: Place amount
                  x-description-cn: 下单数量
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: '"true" or "false". Cannot be sent in Hedge Mode.'
                  x-description-cn: "`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数"
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order price
                  x-description-cn: 委托价格
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
                  description: >-
                    only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/
                    `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together
                    with `price`
                  x-description-cn: >-
                    `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/
                    `QUEUE_20`；不能与price同时传
                newClientOrderId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`
                  x-description-cn: '用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`'
                newOrderRespType:
                  type: string
                  example: ACK
                  default: ACK
                  enum:
                    - ACK
                    - RESULT
                  description: '"ACK", "RESULT", default "ACK"'
                  x-description-cn: "`ACK`， `RESULT`，默认 `ACK`"
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: New CM Order
          x-description-cn: New CM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: testOrder
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 22542179
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "10"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair.
                    x-description-cn: Pair.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: MARKET
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
    get:
      summary: Query CM Order (USER_DATA)
      x-summary-cn: 查询CM订单 (USER_DATA)
      description: Check an CM order's status.
      x-description-cn: 查询CM订单状态
      tags:
        - trade
      operationId: queryCmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-cm-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_cm_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_cm_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCmOrder/QueryCmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCmOrderExample.php
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
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `orderId` or `origClientOrderId` must be sent.
        - These orders will not be found:
          - order status is `CANCELED` or `EXPIRED`, **AND**
          - order has NO filled trade, **AND**
          - created time + 3 days < current time
      x-parameters-notes-cn: |-
        - 注意:
          - `orderId` 或 `origClientOrderId` 必须至少发送一个
          - 请注意，如果订单满足如下条件，不会被查询到：
          - 订单的最终状态为 `CANCELED` 或 `EXPIRED`, **AND**
          - 订单没有任何的成交记录，并且
          - 订单生成时间 + 3天 < 当前时间
      responses:
        "200":
          description: CM Order
          x-description-cn: CM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgPrice:
                    type: string
                    example: "0.0"
                    description: Avg Price.
                    x-description-cn: Avg Price.
                  clientOrderId:
                    type: string
                    example: abc
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumBase:
                    type: string
                    example: "0"
                    description: Cum Base.
                    x-description-cn: Cum Base.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 1917641
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  origType:
                    type: string
                    example: LIMIT
                    description: Orig Type.
                    x-description-cn: Orig Type.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSD_200925
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  pair:
                    type: string
                    example: BTCUSD
                    description: Pair.
                    x-description-cn: Pair.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: order time
                    x-description-cn: order time
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: update time
                    x-description-cn: update time
  /papi/v1/margin/allOpenOrders:
    delete:
      summary: Cancel Margin Account All Open Orders on a Symbol (TRADE)
      x-summary-cn: 杠杆账户撤销单一交易对的所有挂单 (TRADE)
      description: Cancel Margin Account All Open Orders on a Symbol
      x-description-cn: 杠杆账户撤销单一交易对的所有挂单
      tags:
        - trade
      operationId: cancelMarginAccountAllOpenOrdersOnASymbol
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-margin-account-all-open-orders-on-asymbol
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelMarginAccountAllOpenOrdersOnASymbol.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_margin_account_all_open_orders_on_a_symbol.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_margin_account_all_open_orders_on_a_symbol.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelMarginAccountAllOpenOrdersOnASymbolExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelMarginAccountAllOpenOrdersOnASymbol/CancelMarginAccountAllOpenOrdersOnASymbol.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelMarginAccountAllOpenOrdersOnASymbolExample.php
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
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel Margin Account All Open Orders on a Symbol
          x-description-cn: 取消杠杆 账户 All 未完成订单 on a 交易对
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    origClientOrderId:
                      type: string
                      example: E6APeyTJvkMvLMYMqu1KQ4
                      description: Orig Client Order ID.
                      x-description-cn: Orig Client Order ID.
                    orderId:
                      type: integer
                      example: 11
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    orderListId:
                      type: integer
                      example: -1
                      format: int64
                      description: Order List ID.
                      x-description-cn: Order List ID.
                    clientOrderId:
                      type: string
                      example: pXLV6Hz6mprAcVYpVMTGgx
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    price:
                      type: string
                      example: "0.089853"
                      description: Price.
                      x-description-cn: Price.
                    origQty:
                      type: string
                      example: "0.178622"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    executedQty:
                      type: string
                      example: "0.000000"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    cummulativeQuoteQty:
                      type: string
                      example: "0.000000"
                      description: Cummulative Quote Qty.
                      x-description-cn: Cummulative Quote Qty.
                    status:
                      type: string
                      example: CANCELED
                      description: Status.
                      x-description-cn: 订单状态
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    contingencyType:
                      type: string
                      example: OCO
                      description: Contingency Type.
                      x-description-cn: Contingency Type.
                    listStatusType:
                      type: string
                      example: ALL_DONE
                      description: List Status Type.
                      x-description-cn: List Status Type.
                    listOrderStatus:
                      type: string
                      example: ALL_DONE
                      description: List Order Status.
                      x-description-cn: List Order Status.
                    listClientOrderId:
                      type: string
                      example: 2inzWQdDvZLHbbAmAozX2N
                      description: List Client Order ID.
                      x-description-cn: List Client Order ID.
                    transactionTime:
                      type: integer
                      example: 1585230948299
                      format: int64
                      description: Transaction Time.
                      x-description-cn: Transaction Time.
                    orders:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                            description: Trade symbol, if existing.
                            x-description-cn: 交易对（如存在）。
                          orderId:
                            type: integer
                            example: 20
                            format: int64
                            description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                            x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                          clientOrderId:
                            type: string
                            example: CwOOIPHSmYywx6jZX77TdL
                            description: Client Order ID.
                            x-description-cn: Client Order ID.
                      description: Orders.
                      x-description-cn: Orders.
                    orderReports:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BTCUSDT
                            description: Trade symbol, if existing.
                            x-description-cn: 交易对（如存在）。
                          origClientOrderId:
                            type: string
                            example: CwOOIPHSmYywx6jZX77TdL
                            description: Orig Client Order ID.
                            x-description-cn: Orig Client Order ID.
                          orderId:
                            type: integer
                            example: 20
                            format: int64
                            description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                            x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                          orderListId:
                            type: integer
                            example: 1929
                            format: int64
                            description: Order List ID.
                            x-description-cn: Order List ID.
                          clientOrderId:
                            type: string
                            example: pXLV6Hz6mprAcVYpVMTGgx
                            description: Client Order ID.
                            x-description-cn: Client Order ID.
                          price:
                            type: string
                            example: "0.668611"
                            description: Price.
                            x-description-cn: Price.
                          origQty:
                            type: string
                            example: "0.690354"
                            description: Orig Qty.
                            x-description-cn: Orig Qty.
                          executedQty:
                            type: string
                            example: "0.000000"
                            description: Executed Qty.
                            x-description-cn: Executed Qty.
                          cummulativeQuoteQty:
                            type: string
                            example: "0.000000"
                            description: Cummulative Quote Qty.
                            x-description-cn: Cummulative Quote Qty.
                          status:
                            type: string
                            example: CANCELED
                            description: Status.
                            x-description-cn: 订单状态
                          timeInForce:
                            type: string
                            example: GTC
                            description: Time In Force.
                            x-description-cn: Time In Force.
                          type:
                            type: string
                            example: STOP_LOSS_LIMIT
                            description: Normal order type after trigger if appliable
                            x-description-cn: 条件单触发后普通订单类型
                          side:
                            type: string
                            example: BUY
                            description: Side.
                            x-description-cn: Side.
                          stopPrice:
                            type: string
                            example: "0.378131"
                            description: please ignore when order type is TRAILING_STOP_MARKET
                            x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                          icebergQty:
                            type: string
                            example: "0.017083"
                            description: Iceberg Qty.
                            x-description-cn: Iceberg Qty.
                      description: Order Reports.
                      x-description-cn: Order Reports.
  /papi/v1/margin/orderList:
    delete:
      summary: Cancel Margin Account OCO Orders (TRADE)
      x-summary-cn: 取消杠杆账户OCO订单 (TRADE)
      description: Cancel Margin Account OCO Orders
      x-description-cn: 取消杠杆账户订单。
      tags:
        - trade
      operationId: cancelMarginAccountOcoOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-margin-account-oco-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelMarginAccountOcoOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_margin_account_oco_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_margin_account_oco_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelMarginAccountOcoOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelMarginAccountOcoOrders/CancelMarginAccountOcoOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelMarginAccountOcoOrdersExample.php
      x-ip-weight: 2
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
            example: LTCBTC
          description: Symbol
          x-description-cn: 交易对
        - name: orderListId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Either `orderListId` or `listClientOrderId` must be provided
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
        - name: listClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Either `orderListId` or `listClientOrderId` must be provided
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
        - name: newClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Used to uniquely identify this cancel request.
          x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than 60000
          x-description-cn: 赋值不能超过 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Additional notes: Canceling an individual leg will cancel the entire OCO"
      x-parameters-notes-cn: "- 其他备注: 取消单个 leg 将取消整个 OCO 订单。"
      responses:
        "200":
          description: Cancel Margin Account OCO Orders
          x-description-cn: 取消杠杆 账户 OCO 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    example: 0
                    format: int64
                    description: Order List ID.
                    x-description-cn: Order List ID.
                  contingencyType:
                    type: string
                    example: OCO
                    description: Contingency Type.
                    x-description-cn: Contingency Type.
                  listStatusType:
                    type: string
                    example: ALL_DONE
                    description: List Status Type.
                    x-description-cn: List Status Type.
                  listOrderStatus:
                    type: string
                    example: ALL_DONE
                    description: List Order Status.
                    x-description-cn: List Order Status.
                  listClientOrderId:
                    type: string
                    example: C3wyj4WVEktd7u9aVBRXcN
                    description: List Client Order ID.
                    x-description-cn: List Client Order ID.
                  transactionTime:
                    type: integer
                    example: 1574040868128
                    format: int64
                    description: Transaction Time.
                    x-description-cn: Transaction Time.
                  symbol:
                    type: string
                    example: LTCBTC
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        orderId:
                          type: integer
                          example: 2
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        clientOrderId:
                          type: string
                          example: pO9ufTiFGg3nw2fOdgeOXa
                          description: Client Order ID.
                          x-description-cn: Client Order ID.
                    description: Orders.
                    x-description-cn: Orders.
                  orderReports:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        origClientOrderId:
                          type: string
                          example: pO9ufTiFGg3nw2fOdgeOXa
                          description: Orig Client Order ID.
                          x-description-cn: Orig Client Order ID.
                        orderId:
                          type: integer
                          example: 2
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        orderListId:
                          type: integer
                          example: 0
                          format: int64
                          description: Order List ID.
                          x-description-cn: Order List ID.
                        clientOrderId:
                          type: string
                          example: unfWT8ig8i0uj6lPuYLez6
                          description: Client Order ID.
                          x-description-cn: Client Order ID.
                        price:
                          type: string
                          example: "1.00000000"
                          description: Price.
                          x-description-cn: Price.
                        origQty:
                          type: string
                          example: "10.00000000"
                          description: Orig Qty.
                          x-description-cn: Orig Qty.
                        executedQty:
                          type: string
                          example: "0.00000000"
                          description: Executed Qty.
                          x-description-cn: Executed Qty.
                        cummulativeQuoteQty:
                          type: string
                          example: "0.00000000"
                          description: Cummulative Quote Qty.
                          x-description-cn: Cummulative Quote Qty.
                        status:
                          type: string
                          example: CANCELED
                          description: Status.
                          x-description-cn: 订单状态
                        timeInForce:
                          type: string
                          example: GTC
                          description: Time In Force.
                          x-description-cn: Time In Force.
                        type:
                          type: string
                          example: STOP_LOSS_LIMIT
                          description: Normal order type after trigger if appliable
                          x-description-cn: 条件单触发后普通订单类型
                        side:
                          type: string
                          example: SELL
                          description: Side.
                          x-description-cn: Side.
                        stopPrice:
                          type: string
                          example: "1.00000000"
                          description: please ignore when order type is TRAILING_STOP_MARKET
                          x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    description: Order Reports.
                    x-description-cn: Order Reports.
    get:
      summary: Query Margin Account's OCO (USER_DATA)
      x-summary-cn: 查询杠杆账户 OCO (USER_DATA)
      description: Retrieves a specific OCO based on provided optional parameters
      x-description-cn: 根据提供的可选参数检索特定的杠杆账户 OCO 订单。
      tags:
        - trade
      operationId: queryMarginAccountsOco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-margin-accounts-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryMarginAccountsOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_margin_accounts_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_margin_accounts_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryMarginAccountsOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryMarginAccountsOco/QueryMarginAccountsOco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryMarginAccountsOcoExample.php
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
        - name: orderListId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Either `orderListId` or `listClientOrderId` must be provided
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: "`orderListId` or `listClientOrderId` must be provided."
          x-description-cn: "`orderListId` 或 `listClientOrderId` 必须被提供"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account's OCO
          x-description-cn: 杠杆 账户's OCO
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    example: 27
                    format: int64
                    description: Order List ID.
                    x-description-cn: Order List ID.
                  contingencyType:
                    type: string
                    example: OCO
                    description: Contingency Type.
                    x-description-cn: Contingency Type.
                  listStatusType:
                    type: string
                    example: EXEC_STARTED
                    description: List Status Type.
                    x-description-cn: List Status Type.
                  listOrderStatus:
                    type: string
                    example: EXECUTING
                    description: List Order Status.
                    x-description-cn: List Order Status.
                  listClientOrderId:
                    type: string
                    example: h2USkA5YQpaXHPIrkd96xE
                    description: List Client Order ID.
                    x-description-cn: List Client Order ID.
                  transactionTime:
                    type: integer
                    example: 1565245656253
                    format: int64
                    description: Transaction Time.
                    x-description-cn: Transaction Time.
                  symbol:
                    type: string
                    example: LTCBTC
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        orderId:
                          type: integer
                          example: 4
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        clientOrderId:
                          type: string
                          example: qD1gy3kc3Gx0rihm9Y3xwS
                          description: Client Order ID.
                          x-description-cn: Client Order ID.
                    description: Orders.
                    x-description-cn: Orders.
  /papi/v1/margin/order:
    delete:
      summary: Cancel Margin Account Order (TRADE)
      x-summary-cn: 杠杆账户撤销订单 (TRADE)
      description: Cancel Margin Account Order
      x-description-cn: 杠杆账户撤销订单
      tags:
        - trade
      operationId: cancelMarginAccountOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-margin-account-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelMarginAccountOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_margin_account_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_margin_account_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelMarginAccountOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelMarginAccountOrder/CancelMarginAccountOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelMarginAccountOrderExample.php
      x-ip-weight: 2
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
            example: LTCBTC
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: newClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Used to uniquely identify this cancel request.
          x-description-cn: 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than `60000`
          x-description-cn: 赋值不能超过 `60000`
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 或 `origClientOrderId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel Margin Account Order
          x-description-cn: 取消杠杆 账户 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: LTCBTC
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  orderId:
                    type: integer
                    example: 28
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origClientOrderId:
                    type: string
                    example: myOrder1
                    description: Orig Client Order ID.
                    x-description-cn: Orig Client Order ID.
                  clientOrderId:
                    type: string
                    example: cancelMyOrder1
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  price:
                    type: string
                    example: "1.00000000"
                    description: Price.
                    x-description-cn: Price.
                  origQty:
                    type: string
                    example: "10.00000000"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  executedQty:
                    type: string
                    example: "8.00000000"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  cummulativeQuoteQty:
                    type: string
                    example: "8.00000000"
                    description: Cummulative Quote Qty.
                    x-description-cn: Cummulative Quote Qty.
                  status:
                    type: string
                    example: CANCELED
                    description: Status.
                    x-description-cn: 订单状态
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  side:
                    type: string
                    example: SELL
                    description: Side.
                    x-description-cn: Side.
    post:
      summary: New Margin Order (TRADE)
      x-summary-cn: 杠杆账户下单 (TRADE)
      description: New Margin Order
      x-description-cn: 杠杆账户下单
      tags:
        - trade
      operationId: newMarginOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#new-margin-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/newMarginOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/new_margin_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/new_margin_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/NewMarginOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/NewMarginOrder/NewMarginOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/NewMarginOrderExample.php
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
                - side
                - type
                - timestamp
              properties:
                symbol:
                  type: string
                  example: BTCUSDT
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                type:
                  type: string
                  example: LIMIT
                  enum:
                    - LIMIT
                    - MARKET
                    - STOP_LOSS
                    - STOP_LOSS_LIMIT
                    - TAKE_PROFIT
                    - TAKE_PROFIT_LIMIT
                    - LIMIT_MAKER
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                quoteOrderQty:
                  type: number
                  example: "1.0"
                  format: float
                price:
                  type: number
                  example: "1.0"
                  format: float
                stopPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
                  x-description-cn: 与 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`，和 `TAKE_PROFIT_LIMIT` 订单一起使用
                newClientOrderId:
                  type: string
                  example: "1"
                  description: A unique id among open orders. Automatically generated if not sent.
                  x-description-cn: 客户自定义的唯一订单ID。若未发送自动生成。
                newOrderRespType:
                  type: string
                  example: ACK
                  enum:
                    - ACK
                    - RESULT
                    - FULL
                  description: Set the response JSON. ACK, RESULT, or FULL.
                  x-description-cn: "设置响应: JSON。 `ACK`， `RESULT`， 或 `FULL`; `MARKET` 和 `LIMIT` 订单类型默认为 `FULL`， 所有其他订单默认为 `ACK`"
                icebergQty:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order
                  x-description-cn: 与 `LIMIT`， `STOP_LOSS_LIMIT`，和 `TAKE_PROFIT_LIMIT` 一起使用创建 iceberg 订单
                sideEffectType:
                  type: string
                  example: NO_SIDE_EFFECT
                  default: NO_SIDE_EFFECT
                  enum:
                    - NO_SIDE_EFFECT
                    - MARGIN_BUY
                    - AUTO_REPAY
                    - AUTO_BORROW_REPAY
                timeInForce:
                  type: string
                  example: GTC
                  enum:
                    - GTC
                    - IOC
                    - FOK
                selfTradePreventionMode:
                  type: string
                  example: NONE
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: >-
                    `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker
                    order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers
                  x-description-cn: 允许的 ENUM 取决于交易对的配置。支持的值有 EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE
                autoRepayAtCancel:
                  type: boolean
                  example: true
                  default: true
                  enum:
                    - true
                    - false
                  description: >-
                    Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by
                    the order needs to be repaid after the order is cancelled.
                  x-description-cn: 只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  description: The value cannot be greater than `60000`
                  x-description-cn: 赋值不能超过 `60000`
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: New Margin Order
          x-description-cn: New 杠杆 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  orderId:
                    type: integer
                    example: 28
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  clientOrderId:
                    type: string
                    example: 6gCrw2kRUAF9CvJDGP16IP
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  transactTime:
                    type: integer
                    example: 1507725176595
                    format: int64
                    description: Transact Time.
                    x-description-cn: Transact Time.
                  price:
                    type: string
                    example: "1.00000000"
                    description: Price.
                    x-description-cn: Price.
                  origQty:
                    type: string
                    example: "10.00000000"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  executedQty:
                    type: string
                    example: "10.00000000"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  cummulativeQuoteQty:
                    type: string
                    example: "10.00000000"
                    description: Cummulative Quote Qty.
                    x-description-cn: Cummulative Quote Qty.
                  status:
                    type: string
                    example: FILLED
                    description: Status.
                    x-description-cn: 订单状态
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: MARKET
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  side:
                    type: string
                    example: SELL
                    description: Side.
                    x-description-cn: Side.
                  marginBuyBorrowAmount:
                    type: string
                    example: "5"
                    description: will not return if no margin trade happens
                    x-description-cn: 下单后没有发生借款则不返回该字段
                  marginBuyBorrowAsset:
                    type: string
                    example: BTC
                    description: will not return if no margin trade happens
                    x-description-cn: 下单后没有发生借款则不返回该字段
                  fills:
                    type: array
                    items:
                      type: object
                      properties:
                        price:
                          type: string
                          example: "4000.00000000"
                          description: Price.
                          x-description-cn: Price.
                        qty:
                          type: string
                          example: "1.00000000"
                          description: Qty.
                          x-description-cn: Qty.
                        commission:
                          type: string
                          example: "4.00000000"
                          description: Commission.
                          x-description-cn: Commission.
                        commissionAsset:
                          type: string
                          example: USDT
                          description: Commission Asset.
                          x-description-cn: Commission Asset.
                    description: Fills.
                    x-description-cn: Fills.
    get:
      summary: Query Margin Account Order (USER_DATA)
      x-summary-cn: 查询杠杆账户订单 (USER_DATA)
      description: Query Margin Account Order
      x-description-cn: 查询杠杆账户订单
      tags:
        - trade
      operationId: queryMarginAccountOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-margin-account-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryMarginAccountOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_margin_account_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_margin_account_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryMarginAccountOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryMarginAccountOrder/QueryMarginAccountOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryMarginAccountOrderExample.php
      x-ip-weight: 10
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
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `orderId` or `origClientOrderId` must be sent.
        - For some historical orders, `cummulativeQuoteQty < 0` means the data is unavailable at this time.
      x-parameters-notes-cn: |-
        - 必须发送 `orderId` 或 `origClientOrderId` 其中一个。
        - 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。
      responses:
        "200":
          description: Margin Account Order
          x-description-cn: 杠杆 账户 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: ZwfQzuDIGpceVhKW5DvCmO
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cummulativeQuoteQty:
                    type: string
                    example: "0.00000000"
                    description: Cummulative Quote Qty.
                    x-description-cn: Cummulative Quote Qty.
                  executedQty:
                    type: string
                    example: "0.00000000"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  icebergQty:
                    type: string
                    example: "0.00000000"
                    description: Iceberg Qty.
                    x-description-cn: Iceberg Qty.
                  isWorking:
                    type: boolean
                    example: true
                    description: Is Working.
                    x-description-cn: Is Working.
                  orderId:
                    type: integer
                    example: 213205622
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "0.30000000"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0.00493630"
                    description: Price.
                    x-description-cn: Price.
                  side:
                    type: string
                    example: SELL
                    description: Side.
                    x-description-cn: Side.
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  stopPrice:
                    type: string
                    example: "0.00000000"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                  symbol:
                    type: string
                    example: BNBBTC
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  time:
                    type: integer
                    example: 1562133008725
                    format: int64
                    description: Event time.
                    x-description-cn: 时间。
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1562133008725
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  accountId:
                    type: integer
                    example: 152950866
                    format: int64
                    description: Account ID.
                    x-description-cn: Account ID.
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_TAKER
                    description: self trading preventation mode
                    x-description-cn: self trading preventation mode
                  preventedMatchId:
                    type: string
                    example: "null"
                    description: Prevented Match ID.
                    x-description-cn: Prevented Match ID.
                  preventedQuantity:
                    type: string
                    example: "null"
                    description: Prevented Quantity.
                    x-description-cn: Prevented Quantity.
  /papi/v1/um/order:
    delete:
      summary: Cancel UM Order (TRADE)
      x-summary-cn: 撤销UM订单 (TRADE)
      description: Cancel an active UM LIMIT order
      x-description-cn: 撤销UM订单
      tags:
        - trade
      operationId: cancelUmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-um-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelUmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_um_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_um_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelUmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelUmOrder/CancelUmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelUmOrderExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 或 `origClientOrderId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel UM Order
          x-description-cn: 取消UM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: myOrder1
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 4611875134427365000
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: CANCELED
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1571110484038
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: self trading preventation mode
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: order pre-set auot cancel time for TIF GTD order
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
    put:
      summary: Modify UM Order (TRADE)
      x-summary-cn: 修改UM订单 (TRADE)
      description: >-
        Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered
        in the match queue
      x-description-cn: 修改UM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序
      tags:
        - trade
      operationId: modifyUmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#modify-um-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/modifyUmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/modify_um_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/modify_um_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/ModifyUmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/ModifyUmOrder/ModifyUmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/ModifyUmOrderExample.php
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
        - Either orderId or origClientOrderId must be sent, and the orderId will prevail if both are sent.

        - Both quantity and price must be sent

        - When the new quantity or price doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be
        rejected and the order will stay as it is.

        - However the order will be cancelled by the amendment in the following situations:
          - when the order is in partially filled status and the new quantity <= executedQty
          - When the order is GTX and the new price will cause it to be executed immediately
        - The amendment keeps the order's original selfTradePreventionMode.
      x-parameters-notes-cn: |-
        - orderId 与 origClientOrderId 必须至少发送一个，同时发送则以 orderId 为准
        - quantity 与 price 均必须发送
        - 当新订单的 quantity 或 price 不满足 PRICE_FILTER / PERCENT_FILTER / LOT_SIZE 限制，修改会被拒绝，原订单依旧被保留
        - 订单会在下列情况下被取消：
          - 原订单被部分执行且新订单 quantity <= executedQty
          - 原订单是 GTX，新订单的价格会导致订单立刻执行
        - 改单会保留该单原有的 selfTradePreventionMode
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
                  example: BTCUSDT
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
                  description: Order quantity
                  x-description-cn: 下单数量
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order price
                  x-description-cn: 委托价格
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
                  description: >-
                    only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/
                    `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together
                    with `price`
                  x-description-cn: >-
                    `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/
                    `QUEUE_20`；不能与price同时传
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
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Modify UM Order
          x-description-cn: Modify UM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 20072994037
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  clientOrderId:
                    type: string
                    example: LJ9R4QZDihCaS8UAOOLpgW
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  modifyId:
                    type: integer
                    example: 1
                    format: int64
                    description: user-defined modification identifier, only returned if provided in the request
                    x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                  price:
                    type: string
                    example: "30005"
                    description: Price.
                    x-description-cn: Price.
                  origQty:
                    type: string
                    example: "1"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: LONG
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  origType:
                    type: string
                    example: LIMIT
                    description: Orig Type.
                    x-description-cn: Orig Type.
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: self trading preventation mode
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: order pre-set auot cancel time for TIF GTD order
                  updateTime:
                    type: integer
                    example: 1629182711600
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
    post:
      summary: New UM Order (TRADE)
      x-summary-cn: UM下单 (TRADE)
      description: Place new UM order
      x-description-cn: UM下单
      tags:
        - trade
      operationId: newUmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#new-um-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/newUmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/new_um_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/new_um_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/NewUmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/NewUmOrder/NewUmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/NewUmOrderExample.php
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
      x-parameters-notes: |-
        - Additional mandatory parameters based on type:
          - If `newOrderRespType` is sent as `RESULT` :
          - `MARKET` order: the final FILLED result of the order will be return directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
          - `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
          - In extreme market conditions, timeInForce `GTD` order auto cancel time might be delayed comparing to `goodTillDate`
      x-parameters-notes-cn: |-
        - 根据 order `type`的不同，某些参数强制要求，具体如下:
          - `newOrderRespType` 如果传 `RESULT`:
          - `MARKET` 订单将直接返回成交结果；
          - 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
          - `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
          - 极端行情时，`timeInForce`为`GTD`的订单自动取消可能有一定延迟
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
                  example: BTCUSDT
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
                  default: BOTH
                  enum:
                    - BOTH
                    - LONG
                    - SHORT
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
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
                  description: Valid values
                  x-description-cn: 有效方法
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: Place amount
                  x-description-cn: 下单数量
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: '"true" or "false". default "false". Cannot be sent in Hedge Mode .'
                  x-description-cn: "`true`或`false`; 非双开模式下默认false；双开模式下不接受此参数"
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order price
                  x-description-cn: 委托价格
                newClientOrderId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`
                  x-description-cn: '用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`'
                newOrderRespType:
                  type: string
                  example: ACK
                  default: ACK
                  enum:
                    - ACK
                    - RESULT
                  description: "`ACK`, `RESULT`, default `ACK`"
                  x-description-cn: "`ACK`， `RESULT`，默认 `ACK`"
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
                  description: >-
                    only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/
                    `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together
                    with `price`
                  x-description-cn: >-
                    `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/
                    `QUEUE_20`；不能与price同时传
                selfTradePreventionMode:
                  type: string
                  example: EXPIRE_MAKER
                  enum:
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: >-
                    `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP
                    triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers
                  x-description-cn: EXPIRE_TAKER/ EXPIRE_MAKER/ EXPIRE_BOTH； 默认EXPIRE_MAKER
                goodTillDate:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                    timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp
                    must be greater than the current time plus 600 seconds and smaller than 253402300799000Mode. It must
                    be sent in Hedge Mode.
                  x-description-cn: TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: New UM Order
          x-description-cn: New UM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: testOrder
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQty:
                    type: string
                    example: "0"
                    description: Cum Qty.
                    x-description-cn: Cum Qty.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 22542179
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "10"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  timeInForce:
                    type: string
                    example: GTD
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: MARKET
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: //订单自成交保护模式
                  goodTillDate:
                    type: integer
                    example: 1693207680000
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
    get:
      summary: Query UM Order (USER_DATA)
      x-summary-cn: 查询UM订单 (USER_DATA)
      description: Check an UM order's status.
      x-description-cn: 查询UM订单状态
      tags:
        - trade
      operationId: queryUmOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-um-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUmOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_um_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_um_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUmOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUmOrder/QueryUmOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUmOrderExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - These orders will not be found:
          - Either `orderId` or `origClientOrderId` must be sent.
          - order status is `CANCELED` or `EXPIRED`, **AND**
          - order has NO filled trade, **AND**
          - created time + 3 days < current time
      x-parameters-notes-cn: |-
        - 注意:
          - `orderId` 或 `origClientOrderId` 必须至少发送一个
          - 请注意，如果订单满足如下条件，不会被查询到：
          - 订单的最终状态为 `CANCELED` 或 `EXPIRED`，并且
          - 订单没有任何的成交记录，并且
          - 订单生成时间 + 3天 < 当前时间
      responses:
        "200":
          description: UM Order
          x-description-cn: UM 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgPrice:
                    type: string
                    example: "0.00000"
                    description: Avg Price.
                    x-description-cn: Avg Price.
                  clientOrderId:
                    type: string
                    example: abc
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQuote:
                    type: string
                    example: "0"
                    description: Cum Quote.
                    x-description-cn: Cum Quote.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 1917641
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  origType:
                    type: string
                    example: LIMIT
                    description: Orig Type.
                    x-description-cn: Orig Type.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: order time
                    x-description-cn: order time
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: update time
                    x-description-cn: update time
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: self trading preventation mode
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: order pre-set auot cancel time for TIF GTD order
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
  /papi/v1/cm/userTrades:
    get:
      summary: CM Account Trade List (USER_DATA)
      x-summary-cn: CM账户成交历史 (USER_DATA)
      description: Get trades for a specific account and CM symbol.
      x-description-cn: 获取CM成交历史
      tags:
        - trade
      operationId: cmAccountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cm-account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cmAccountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cm_account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cm_account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CmAccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CmAccountTradeList/CmAccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CmAccountTradeListExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 20 with `symbol`
        - 40 with `pair`
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
        - name: pair
          in: query
          required: false
          schema:
            type: string
            example: BTCUSD
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
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Trade ID to fetch from.
          x-description-cn: 起始成交 ID。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 50
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `symbol` or `pair` must be sent
        - `symbol` and `pair` cannot be sent together
        - `pair` and `fromId` cannot be sent together
        - `OrderId` can only be sent together with symbol
        - If a `pair` is sent, tickers for all symbols of the `pair` will be returned
        - The parameter `fromId` cannot be sent with `startTime` or `endTime`
        - If `startTime` and `endTime` are both not sent, then the last '24 hours' data will be returned.
        - The time between `startTime` and `endTime` cannot be longer than 24 hours.
      x-parameters-notes-cn: |-
        - `symbol` 或 `pair` 其中一个必传
        - `symbol` 或 `pair` 不能同时传
        - `fromId` 或 `pair` 不能同时传
        - `orderId`必须和`symbol`一起提供
        - 如果传`pair`，该`pair`的所有交易对会被返回
        - 参数`fromId`不能和`startTime`或`endTime`一起发送
        - 如果`startTime` 和 `endTime` 均未发送, 只会返回最近24小时的数据。
        - `startTime` 和 `endTime` 的最大间隔为24小时。
      responses:
        "200":
          description: CM Account Trade List
          x-description-cn: CM 账户 交易 列表
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    id:
                      type: integer
                      example: 6
                      format: int64
                      description: ID.
                      x-description-cn: ID.
                    orderId:
                      type: integer
                      example: 28
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    price:
                      type: string
                      example: "8800"
                      description: Price.
                      x-description-cn: Price.
                    qty:
                      type: string
                      example: "1"
                      description: Qty.
                      x-description-cn: Qty.
                    realizedPnl:
                      type: string
                      example: "0"
                      description: Realized Pnl.
                      x-description-cn: Realized Pnl.
                    marginAsset:
                      type: string
                      example: BTC
                      description: Margin Asset.
                      x-description-cn: Margin Asset.
                    baseQty:
                      type: string
                      example: "0.01136364"
                      description: Base Qty.
                      x-description-cn: Base Qty.
                    commission:
                      type: string
                      example: "0.00000454"
                      description: Commission.
                      x-description-cn: Commission.
                    commissionAsset:
                      type: string
                      example: BTC
                      description: Commission Asset.
                      x-description-cn: Commission Asset.
                    time:
                      type: integer
                      example: 1590743483586
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    buyer:
                      type: boolean
                      example: false
                      description: Buyer.
                      x-description-cn: Buyer.
                    maker:
                      type: boolean
                      example: false
                      description: Maker.
                      x-description-cn: Maker.
  /papi/v1/cm/adlQuantile:
    get:
      summary: CM Position ADL Quantile Estimation (USER_DATA)
      x-summary-cn: CM持仓ADL队列估算 (USER_DATA)
      description: >-
        Query CM Position ADL Quantile Estimation

        * Values update every 30s.

        * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.

        * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and
        "BOTH" will be returned to show the positions' adl quantiles of different position sides.

        * If the positions of the symbol are crossed margined in Hedge Mode:

        * "HEDGE" as a sign will be returned instead of "BOTH";

        * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and
        "SHORT" when there are positions in both of long and short sides.
      x-description-cn: >-
        CM持仓ADL队列估算

        * 每30秒更新数据

        * 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前

        * 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数

        * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE",
        其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。
      tags:
        - trade
      operationId: cmPositionAdlQuantileEstimation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cm-position-adl-quantile-estimation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cmPositionAdlQuantileEstimation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cm_position_adl_quantile_estimation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cm_position_adl_quantile_estimation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CmPositionAdlQuantileEstimationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CmPositionAdlQuantileEstimation/CmPositionAdlQuantileEstimation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CmPositionAdlQuantileEstimationExample.php
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
            example: BTCUSD_201225
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: CM Position ADL Quantile Estimation
          x-description-cn: CM 持仓 ADL Quantile Estimation
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
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
                          description: only a sign, ignore the value
                          x-description-cn: HEDGE 仅作为指示出现，请忽略数值
                        BOTH:
                          type: integer
                          example: 0
                          format: int64
                          description: adl qunatile for position in one-way mode
                          x-description-cn: 单开模式下持仓的ADL队列估算分
                      description: Adl Quantile.
                      x-description-cn: Adl Quantile.
  /papi/v1/um/feeBurn:
    get:
      summary: Get UM Futures BNB Burn Status (USER_DATA)
      x-summary-cn: 获取UM BNB抵扣开关状态 (USER_DATA)
      description: Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )
      x-description-cn: 查询用户 ***所有 symbol*** UM合约交易BNB抵扣开关状态(手续费抵扣开或关)
      tags:
        - trade
      operationId: getUmFuturesBnbBurnStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#get-um-futures-bnb-burn-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/getUmFuturesBnbBurnStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/get_um_futures_bnb_burn_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/get_um_futures_bnb_burn_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/GetUmFuturesBnbBurnStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/GetUmFuturesBnbBurnStatus/GetUmFuturesBnbBurnStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/GetUmFuturesBnbBurnStatusExample.php
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get UM Futures BNB Burn Status
          x-description-cn: 获取UM 合约 BNB Burn 状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  feeBurn:
                    type: boolean
                    example: true
                    description: '"true": Fee Discount On; "false": Fee Discount Off'
                    x-description-cn: '"true": 手续费抵扣开; "false": 手续费抵扣关'
    post:
      summary: Toggle BNB Burn On UM Futures Trade (TRADE)
      x-summary-cn: UM合约交易BNB抵扣开关 (TRADE)
      description: Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***
      x-description-cn: 改变用户 ***所有 symbol*** UM合约交易BNB抵扣开关(手续费抵扣开或关)
      tags:
        - trade
      operationId: toggleBnbBurnOnUmFuturesTrade
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#toggle-bnb-burn-on-um-futures-trade
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/toggleBnbBurnOnUmFuturesTrade.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/toggle_bnb_burn_on_um_futures_trade.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/toggle_bnb_burn_on_um_futures_trade.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/ToggleBnbBurnOnUmFuturesTradeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/ToggleBnbBurnOnUmFuturesTrade/ToggleBnbBurnOnUmFuturesTrade.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/ToggleBnbBurnOnUmFuturesTradeExample.php
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
      x-parameters-notes: "- The BNB would not be collected from UM-PM account to the Portfolio Margin account."
      x-parameters-notes-cn: "- The BNB would not be collected 从 UM-PM 账户 到 the Portfolio 杠杆 账户."
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - feeBurn
                - timestamp
              properties:
                feeBurn:
                  type: string
                  example: "true"
                  enum:
                    - "true"
                    - "false"
                  description: '"true": Fee Discount On; "false": Fee Discount Off'
                  x-description-cn: '"true": 手续费抵扣开; "false": 手续费抵扣关'
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Toggle BNB Burn On UM Futures Trade
          x-description-cn: Toggle BNB Burn On UM 合约 交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: Code.
                    x-description-cn: Code.
                  msg:
                    type: string
                    example: success
                    description: Msg.
                    x-description-cn: Msg.
  /papi/v1/marginLoan:
    post:
      summary: Margin Account Borrow (MARGIN)
      x-summary-cn: 杠杆账户借贷 (MARGIN)
      description: Apply for a margin loan.
      x-description-cn: 申请借贷
      tags:
        - trade
      operationId: marginAccountBorrow
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#margin-account-borrow
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/marginAccountBorrow.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/margin_account_borrow.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/margin_account_borrow.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/MarginAccountBorrowExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/MarginAccountBorrow/MarginAccountBorrow.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/MarginAccountBorrowExample.php
      x-ip-weight: 100
      x-security-type: MARGIN
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
                - asset
                - amount
                - timestamp
              properties:
                asset:
                  type: string
                  example: USDT
                amount:
                  type: number
                  example: "1.0"
                  format: float
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account Borrow
          x-description-cn: 杠杆 账户 借款
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 100000001
                    format: int64
                    description: Transaction ID.
                    x-description-cn: 交易ID。
  /papi/v1/margin/order/oco:
    post:
      summary: Margin Account New OCO (TRADE)
      x-summary-cn: 杠杆账户 OCO 下单 (TRADE)
      description: Send in a new OCO for a margin account
      x-description-cn: 杠杆账户发送新 OCO 订单
      tags:
        - trade
      operationId: marginAccountNewOco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#margin-account-new-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/marginAccountNewOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/margin_account_new_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/margin_account_new_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/MarginAccountNewOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/MarginAccountNewOco/MarginAccountNewOco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/MarginAccountNewOcoExample.php
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
      x-parameters-notes: |-
        - Other Info:
          - Price Restrictions:
          - `SELL`: Limit Price > Last Price > Stop Price
          - `BUY`: Limit Price  * Quantity Restrictions:
          - Both legs must have the same quantity
          - `ICEBERG` quantities however do not have to be the same.
          - Order Rate Limit
          - `OCO` counts as 2 orders against the order rate limit.
      x-parameters-notes-cn: |-
        - Other Info:
          - 价格限制：
          - `SELL`: 限价 > 最新成交价 >触发价
          - `BUY`: 限价  - 数量限制：
          - 两个 legs 必须具有同样的数量
          - `ICEBERG` 数量不必相同
          - 下单 rate：
          - 一个`OCO`订单被算成 2 个普通订单
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
                  example: LTCBTC
                listClientOrderId:
                  type: string
                  example: "1"
                  description: A unique Id for the entire orderList
                  x-description-cn: 整个 orderList 的唯一 ID
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                  description: "See enum definitions: order side"
                  x-description-cn: 详见枚举定义：订单方向
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                limitClientOrderId:
                  type: string
                  example: "1"
                  description: A unique Id for the limit order
                  x-description-cn: 限价单的唯一 ID
                price:
                  type: number
                  example: "1.0"
                  format: float
                limitIcebergQty:
                  type: number
                  example: "1.0"
                  format: float
                stopClientOrderId:
                  type: string
                  example: "1"
                  description: A unique Id for the stop loss/stop loss limit leg
                  x-description-cn: 止损/止损限价单的唯一 ID
                stopPrice:
                  type: number
                  example: "1.0"
                  format: float
                stopLimitPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: If provided, stopLimitTimeInForce is required.
                  x-description-cn: 如果提供，须配合提交`stopLimitTimeInForce`
                stopIcebergQty:
                  type: number
                  example: "1.0"
                  format: float
                stopLimitTimeInForce:
                  type: string
                  example: GTC
                  enum:
                    - GTC
                    - IOC
                    - FOK
                  description: Valid values are `GTC/FOK/IOC`
                  x-description-cn: 有效值 `GTC/FOK/IOC`
                newOrderRespType:
                  type: string
                  example: ACK
                  enum:
                    - ACK
                    - RESULT
                  description: Set the response JSON.
                  x-description-cn: 详见枚举定义：订单返回类型
                sideEffectType:
                  type: string
                  example: NO_SIDE_EFFECT
                  default: NO_SIDE_EFFECT
                  enum:
                    - NO_SIDE_EFFECT
                    - MARGIN_BUY
                    - AUTO_REPAY
                  description: NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.
                  x-description-cn: NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; 默认为 NO_SIDE_EFFECT
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account New OCO
          x-description-cn: 杠杆 账户 New OCO
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderListId:
                    type: integer
                    example: 0
                    format: int64
                    description: Order List ID.
                    x-description-cn: Order List ID.
                  contingencyType:
                    type: string
                    example: OCO
                    description: Contingency Type.
                    x-description-cn: Contingency Type.
                  listStatusType:
                    type: string
                    example: EXEC_STARTED
                    description: List Status Type.
                    x-description-cn: List Status Type.
                  listOrderStatus:
                    type: string
                    example: EXECUTING
                    description: List Order Status.
                    x-description-cn: List Order Status.
                  listClientOrderId:
                    type: string
                    example: JYVpp3F0f5CAG15DhtrqLp
                    description: List Client Order ID.
                    x-description-cn: List Client Order ID.
                  transactionTime:
                    type: integer
                    example: 1563417480525
                    format: int64
                    description: Transaction Time.
                    x-description-cn: Transaction Time.
                  symbol:
                    type: string
                    example: LTCBTC
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  marginBuyBorrowAmount:
                    type: string
                    example: "5"
                    description: will not return if no margin trade happens
                    x-description-cn: 下单后没有发生借款则不返回该字段
                  marginBuyBorrowAsset:
                    type: string
                    example: BTC
                    description: will not return if no margin trade happens
                    x-description-cn: 下单后没有发生借款则不返回该字段
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        orderId:
                          type: integer
                          example: 2
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        clientOrderId:
                          type: string
                          example: Kk7sqHb9J6mJWTMDVW7Vos
                          description: Client Order ID.
                          x-description-cn: Client Order ID.
                    description: Orders.
                    x-description-cn: Orders.
                  orderReports:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: LTCBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        orderId:
                          type: integer
                          example: 2
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        orderListId:
                          type: integer
                          example: 0
                          format: int64
                          description: Order List ID.
                          x-description-cn: Order List ID.
                        clientOrderId:
                          type: string
                          example: Kk7sqHb9J6mJWTMDVW7Vos
                          description: Client Order ID.
                          x-description-cn: Client Order ID.
                        transactTime:
                          type: integer
                          example: 1563417480525
                          format: int64
                          description: Transact Time.
                          x-description-cn: Transact Time.
                        price:
                          type: string
                          example: "0.000000"
                          description: Price.
                          x-description-cn: Price.
                        origQty:
                          type: string
                          example: "0.624363"
                          description: Orig Qty.
                          x-description-cn: Orig Qty.
                        executedQty:
                          type: string
                          example: "0.000000"
                          description: Executed Qty.
                          x-description-cn: Executed Qty.
                        cummulativeQuoteQty:
                          type: string
                          example: "0.000000"
                          description: Cummulative Quote Qty.
                          x-description-cn: Cummulative Quote Qty.
                        status:
                          type: string
                          example: NEW
                          description: Status.
                          x-description-cn: 订单状态
                        timeInForce:
                          type: string
                          example: GTC
                          description: Time In Force.
                          x-description-cn: Time In Force.
                        type:
                          type: string
                          example: STOP_LOSS
                          description: Normal order type after trigger if appliable
                          x-description-cn: 条件单触发后普通订单类型
                        side:
                          type: string
                          example: BUY
                          description: Side.
                          x-description-cn: Side.
                        stopPrice:
                          type: string
                          example: "0.960664"
                          description: please ignore when order type is TRAILING_STOP_MARKET
                          x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    description: Order Reports.
                    x-description-cn: Order Reports.
  /papi/v1/repayLoan:
    post:
      summary: Margin Account Repay (MARGIN)
      x-summary-cn: 杠杆账户归还借贷 (MARGIN)
      description: Repay for a margin loan.
      x-description-cn: 获取杠杆账户归还借贷
      tags:
        - trade
      operationId: marginAccountRepay
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#margin-account-repay
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/marginAccountRepay.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/margin_account_repay.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/margin_account_repay.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/MarginAccountRepayExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/MarginAccountRepay/MarginAccountRepay.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/MarginAccountRepayExample.php
      x-ip-weight: 100
      x-security-type: MARGIN
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
                - asset
                - amount
                - timestamp
              properties:
                asset:
                  type: string
                  example: USDT
                amount:
                  type: number
                  example: "1.0"
                  format: float
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  description: The value cannot be greater than 60000
                  x-description-cn: 赋值不能超过`60000`
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account Repay
          x-description-cn: 杠杆 账户 还款
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 100000001
                    format: int64
                    description: Transaction ID.
                    x-description-cn: 交易ID。
  /papi/v1/margin/repay-debt:
    post:
      summary: Margin Account Repay Debt (TRADE)
      x-summary-cn: 杠杆账户还款 (TRADE)
      description: Repay debt for a margin loan.
      x-description-cn: 杠杆账户还款
      tags:
        - trade
      operationId: marginAccountRepayDebt
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#margin-account-repay-debt
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/marginAccountRepayDebt.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/margin_account_repay_debt.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/margin_account_repay_debt.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/MarginAccountRepayDebtExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/MarginAccountRepayDebt/MarginAccountRepayDebt.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/MarginAccountRepayDebtExample.php
      x-ip-weight: 3000
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
        - The repay asset amount cannot exceed 50000 USD equivalent value for a single request.

        - If `amount` is not sent, all the asset loan will be repaid if having enough specific repay assets.

        - If `amount` is sent, only the certain amount of the asset loan will be repaid if having enough specific repay
        assets.

        - The system will use the same asset to repay the loan first (if have) no matter whether put the asset in
        `specifyRepayAssets`
      x-parameters-notes-cn: |-
        - 单次还款价值需小于等于 50000 USD
        - 如果`amount`未发送，则在有足够的特定偿还资产的情况下，将偿还所有资产负债。
        - 如果发送`amount`，则在有足够的特定还款资产的情况下，仅偿还指定`amount`的资产负债。
        - 无论是否将需要偿还的负债资产放入`specifyRepayAssets`中，系统都会先使用相同的资产（如果有）来偿还负债
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - asset
                - timestamp
              properties:
                asset:
                  type: string
                  example: USDT
                amount:
                  type: string
                  example: "1.0"
                specifyRepayAssets:
                  type: string
                  example: BNB
                  description: Specific asset list to repay debt; Can be added in batch, separated by commas
                  x-description-cn: 指定还款资产，多资产用逗号分隔
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  description: The value cannot be greater than 60000
                  x-description-cn: 赋值不能超过`60000`
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account Repay Debt
          x-description-cn: 杠杆 账户 还款 Debt
          content:
            application/json:
              schema:
                type: object
                properties:
                  amount:
                    type: string
                    example: "0.10000000"
                    description: Amount repaid
                    x-description-cn: 还款金额
                  asset:
                    type: string
                    example: BNB
                    description: asset name
                    x-description-cn: 资产
                  specifyRepayAssets:
                    type: array
                    items:
                      type: string
                      example: USDT
                    description: Specify Repay Assets.
                    x-description-cn: Specify Repay Assets.
                  updateTime:
                    type: integer
                    example: 1636371437000
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  success:
                    type: boolean
                    example: true
                    description: Success.
                    x-description-cn: Success.
  /papi/v1/margin/myTrades:
    get:
      summary: Margin Account Trade List (USER_DATA)
      x-summary-cn: 查询杠杆账户交易历史 (USER_DATA)
      description: Margin Account Trade List
      x-description-cn: 查询杠杆账户交易历史
      tags:
        - trade
      operationId: marginAccountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#margin-account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/marginAccountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/margin_account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/margin_account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/MarginAccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/MarginAccountTradeList/MarginAccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/MarginAccountTradeListExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
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
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Trade ID to fetch from.
          x-description-cn: 起始成交 ID。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 500
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - **Note:** * If `fromId` is set, returns orders with id >= `fromId`; otherwise returns recent order history.
        - The interval between `startTime` and `endTime` must be less than 24 hours.
      x-parameters-notes-cn: |-
        - **注意:** * 如果设置 `fromId` , 获取订单 id >= `fromId`， 否则返回近期订单历史。
        - `startTime` 和 `endTime`的间隔需要小于24小时。
      responses:
        "200":
          description: Margin Account Trade List
          x-description-cn: 杠杆 账户 交易 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    commission:
                      type: string
                      example: "0.00006000"
                      description: Commission.
                      x-description-cn: Commission.
                    commissionAsset:
                      type: string
                      example: BTC
                      description: Commission Asset.
                      x-description-cn: Commission Asset.
                    id:
                      type: integer
                      example: 34
                      format: int64
                      description: ID.
                      x-description-cn: ID.
                    isBestMatch:
                      type: boolean
                      example: true
                      description: Is Best Match.
                      x-description-cn: Is Best Match.
                    isBuyer:
                      type: boolean
                      example: false
                      description: Is Buyer.
                      x-description-cn: Is Buyer.
                    isMaker:
                      type: boolean
                      example: false
                      description: Is Maker.
                      x-description-cn: Is Maker.
                    orderId:
                      type: integer
                      example: 39324
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    price:
                      type: string
                      example: "0.02000000"
                      description: Price.
                      x-description-cn: Price.
                    qty:
                      type: string
                      example: "3.00000000"
                      description: Qty.
                      x-description-cn: Qty.
                    symbol:
                      type: string
                      example: BNBBTC
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    time:
                      type: integer
                      example: 1561973357171
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
  /papi/v1/cm/conditional/allOrders:
    get:
      summary: Query All CM Conditional Orders (USER_DATA)
      x-summary-cn: 查询CM所有条件订单(包括历史订单) (USER_DATA)
      description: Query All CM Conditional Orders
      x-description-cn: 查询CM所有条件订单（包括历史订单
      tags:
        - trade
      operationId: queryAllCmConditionalOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-cm-conditional-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCmConditionalOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_cm_conditional_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_cm_conditional_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCmConditionalOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCmConditionalOrders/QueryAllCmConditionalOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCmConditionalOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 1 for a single `symbol`
        - 40 when `symbol` is omitted
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
        - name: strategyId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
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
            example: 500
            format: int64
            default: 500
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - These orders will not be found:
          - order strategyStatus is `CANCELED` or `EXPIRED`, **AND**
          - order has NO filled trade, **AND**
          - created time + 7 days  * The query time period must be less than 7 days( default as the recent 7 days).
      x-parameters-notes-cn: >-
        - **注意:** - 请注意，如果订单满足如下条件，不会被查询到： - 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且 - 订单没有任何的成交记录, 并且 - 订单生成时间 + 3 天 <
        当前时间 - 查询时间范围最大不得超过 7 天(默认查询最近 7 天内的数据).
      responses:
        "200":
          description: All CM Conditional Orders
          x-description-cn: All CM Conditional 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    newClientStrategyId:
                      type: string
                      example: abc
                      description: New Client Strategy ID.
                      x-description-cn: New Client Strategy ID.
                    strategyId:
                      type: integer
                      example: 123445
                      format: int64
                      description: Strategy ID.
                      x-description-cn: Strategy ID.
                    strategyStatus:
                      type: string
                      example: TRIGGERED
                      description: Strategy Status.
                      x-description-cn: Strategy Status.
                    strategyType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Strategy Type.
                      x-description-cn: Strategy Type.
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    symbol:
                      type: string
                      example: BTCUSD
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    orderId:
                      type: integer
                      example: 12123343534
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    status:
                      type: string
                      example: NEW
                      description: Normal order status after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单状态, 当条件单被触发后才有
                    bookTime:
                      type: integer
                      example: 1566818724710
                      format: int64
                      description: order time
                      x-description-cn: 条件单下单时间
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
                    triggerTime:
                      type: integer
                      example: 1566818724750
                      format: int64
                      description: Trigger Time.
                      x-description-cn: Trigger Time.
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: MARKET
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
  /papi/v1/cm/allOrders:
    get:
      summary: Query All CM Orders (USER_DATA)
      x-summary-cn: 查询所有CM订单(包括历史订单) (USER_DATA)
      description: Get all account CM orders; active, canceled, or filled.
      x-description-cn: 查询所有CM订单(包括历史订单)
      tags:
        - trade
      operationId: queryAllCmOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-cm-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCmOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_cm_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_cm_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCmOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCmOrders/QueryAllCmOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCmOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 20 with `symbol`
        - 40 with `pair`
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
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
            example: 500
            format: int64
            default: 50
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `symbol` or `pair` must be sent.
        - If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - These orders will not be found:
          - order status is `CANCELED` or `EXPIRED`, **AND**
          - order has NO filled trade, **AND**
          - created time + 3 days < current time
      x-parameters-notes-cn: |-
        - `symbol` 或 `pair` 必须传一个,不能同时传
        - 请注意，如果订单满足如下条件，不会被查询到：
        - 订单的最终状态为 `CANCELED` 或 `EXPIRED`, **AND**
          - 订单没有任何的成交记录，并且
          - 订单生成时间 + 3天 < 当前时间
      responses:
        "200":
          description: All CM Orders
          x-description-cn: All CM 订单
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
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cumBase:
                      type: string
                      example: "0"
                      description: Cum Base.
                      x-description-cn: Cum Base.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: order time
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: update time
  /papi/v1/cm/conditional/openOrders:
    get:
      summary: Query All Current CM Open Conditional Orders (USER_DATA)
      x-summary-cn: 查看CM当前全部条件挂单 (USER_DATA)
      description: Get all open conditional orders on a symbol. **Careful** when accessing this with no symbol.
      x-description-cn: 查看CM当前全部条件挂单。 请小心使用不带symbol参数的调用
      tags:
        - trade
      operationId: queryAllCurrentCmOpenConditionalOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-current-cm-open-conditional-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCurrentCmOpenConditionalOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_current_cm_open_conditional_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_current_cm_open_conditional_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCurrentCmOpenConditionalOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCurrentCmOpenConditionalOrders/QueryAllCurrentCmOpenConditionalOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCurrentCmOpenConditionalOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 1 for a single `symbol`
        - 40 when `symbol` is omitted
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
            example: BTCUSD
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- If the symbol is not sent, orders for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不带symbol参数，会返回所有交易对的条件挂单"
      responses:
        "200":
          description: All Current CM Open Conditional Orders
          x-description-cn: All 当前 CM 未完成Conditional 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    newClientStrategyId:
                      type: string
                      example: abc
                      description: New Client Strategy ID.
                      x-description-cn: New Client Strategy ID.
                    strategyId:
                      type: integer
                      example: 123445
                      format: int64
                      description: Strategy ID.
                      x-description-cn: Strategy ID.
                    strategyStatus:
                      type: string
                      example: NEW
                      description: Strategy Status.
                      x-description-cn: Strategy Status.
                    strategyType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      description: Strategy Type.
                      x-description-cn: Strategy Type.
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    symbol:
                      type: string
                      example: BTCUSD
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    bookTime:
                      type: integer
                      example: 1566818724710
                      format: int64
                      description: order time
                      x-description-cn: order time
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    activatePrice:
                      type: string
                      example: "9020"
                      description: activation price, only return with TRAILING_STOP_MARKET order
                      x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                    priceRate:
                      type: string
                      example: "0.3"
                      description: callback rate, only return with TRAILING_STOP_MARKET order
                      x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
  /papi/v1/cm/openOrders:
    get:
      summary: Query All Current CM Open Orders (USER_DATA)
      x-summary-cn: 查看当前全部CM挂单 (USER_DATA)
      description: |-
        Get all open orders on a symbol.

        * If the symbol is not sent, orders for all symbols will be returned in an array.
      x-description-cn: |-
        查看当前全部CM挂单，请小心使用不带symbol参数的调用

        * 不带`symbol`参数，会返回所有交易对的挂单
      tags:
        - trade
      operationId: queryAllCurrentCmOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-current-cm-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCurrentCmOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_current_cm_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_current_cm_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCurrentCmOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCurrentCmOpenOrders/QueryAllCurrentCmOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCurrentCmOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 1 for a single `symbol`
        - 40 when `symbol` is omitted
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: All Current CM Open Orders
          x-description-cn: All 当前 CM 未完成订单
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
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cumBase:
                      type: string
                      example: "0"
                      description: Cum Base.
                      x-description-cn: Cum Base.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: order time
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: update time
  /papi/v1/um/openOrders:
    get:
      summary: Query All Current UM Open Orders (USER_DATA)
      x-summary-cn: 查看当前全部UM挂单 (USER_DATA)
      description: Get all open orders on a symbol.
      x-description-cn: 查看当前全部UM挂单，请小心使用不带symbol参数的调用
      tags:
        - trade
      operationId: queryAllCurrentUmOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-current-um-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCurrentUmOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_current_um_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_current_um_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCurrentUmOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCurrentUmOpenOrders/QueryAllCurrentUmOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCurrentUmOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 1 for a single `symbol`
        - 40 when `symbol` is omitted
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
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- If the symbol is not sent, orders for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不带`symbol`参数，会返回所有交易对的挂单"
      responses:
        "200":
          description: All Current UM Open Orders
          x-description-cn: All 当前 UM 未完成订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    avgPrice:
                      type: string
                      example: "0.00000"
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cumQuote:
                      type: string
                      example: "0"
                      description: Cum Quote.
                      x-description-cn: Cum Quote.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: order time
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: update time
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: self trading preventation mode
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
                      description: order pre-set auot cancel time for TIF GTD order
                      x-description-cn: order pre-set auot cancel time for TIF GTD order
                    priceMatch:
                      type: string
                      example: NONE
                      description: Price Match.
                      x-description-cn: Price Match.
  /papi/v1/margin/allOrders:
    get:
      summary: Query All Margin Account Orders (USER_DATA)
      x-summary-cn: 查询杠杆账户的所有订单 (USER_DATA)
      description: Query All Margin Account Orders
      x-description-cn: 查询杠杆账户的所有订单
      tags:
        - trade
      operationId: queryAllMarginAccountOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-margin-account-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllMarginAccountOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_margin_account_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_margin_account_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllMarginAccountOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllMarginAccountOrders/QueryAllMarginAccountOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllMarginAccountOrdersExample.php
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
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
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
            example: 500
            format: int64
            default: 500
            maximum: 500
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `orderId` is set, returns orders with id >= `orderId`; otherwise returns recent order history.
        - For some historical orders, `cummulativeQuoteQty < 0` means the data is unavailable at this time.
      x-parameters-notes-cn: |-
        - 如果设置 `orderId` , 获取订单 >= `orderId`， 否则返回近期订单历史。
        - 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。
      responses:
        "200":
          description: All Margin Account Orders
          x-description-cn: All 杠杆 账户 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    clientOrderId:
                      type: string
                      example: D2KDy4DIeS56PvkM13f8cP
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cummulativeQuoteQty:
                      type: string
                      example: "0.00000000"
                      description: Cummulative Quote Qty.
                      x-description-cn: Cummulative Quote Qty.
                    executedQty:
                      type: string
                      example: "0.00000000"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    icebergQty:
                      type: string
                      example: "0.00000000"
                      description: Iceberg Qty.
                      x-description-cn: Iceberg Qty.
                    isWorking:
                      type: boolean
                      example: false
                      description: Is Working.
                      x-description-cn: Is Working.
                    orderId:
                      type: integer
                      example: 41295
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "5.31000000"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    price:
                      type: string
                      example: "0.22500000"
                      description: Price.
                      x-description-cn: Price.
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    status:
                      type: string
                      example: CANCELED
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "0.18000000"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    symbol:
                      type: string
                      example: BNBBTC
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    time:
                      type: integer
                      example: 1565769338806
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: TAKE_PROFIT_LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1565769342148
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
                    accountId:
                      type: integer
                      example: 152950866
                      format: int64
                      description: Account ID.
                      x-description-cn: Account ID.
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_TAKER
                      description: self trading preventation mode
                      x-description-cn: self trading preventation mode
                    preventedMatchId:
                      type: string
                      example: "null"
                      description: Prevented Match ID.
                      x-description-cn: Prevented Match ID.
                    preventedQuantity:
                      type: string
                      example: "null"
                      description: Prevented Quantity.
                      x-description-cn: Prevented Quantity.
  /papi/v1/um/allOrders:
    get:
      summary: Query All UM Orders (USER_DATA)
      x-summary-cn: 查询所有UM订单(包括历史订单) (USER_DATA)
      description: Get all account UM orders; active, canceled, or filled.
      x-description-cn: 查询所有UM订单
      tags:
        - trade
      operationId: queryAllUmOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-um-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllUmOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_um_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_um_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllUmOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllUmOrders/QueryAllUmOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllUmOrdersExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
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
            example: 500
            format: int64
            default: 500
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - The query time period must be less then 7 days( default as the recent 7 days).
      x-parameters-notes-cn: |-
        - `orderId` 或 `origClientOrderId` 必须至少发送一个
        - 请注意，如果订单满足如下条件，不会被查询到：
          - 订单的最终状态为 `CANCELED` 或 `EXPIRED`，并且
          - 订单没有任何的成交记录，并且
          - 订单生成时间 + 3天  * 查询时间范围最大不得超过7天
          - 默认查询最近7天内的数据
      responses:
        "200":
          description: All UM Orders
          x-description-cn: All UM 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    avgPrice:
                      type: string
                      example: "0.00000"
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cumQuote:
                      type: string
                      example: "0"
                      description: Cum Quote.
                      x-description-cn: Cum Quote.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: order time
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: update time
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: self trading preventation mode
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
                      description: order pre-set auot cancel time for TIF GTD order
                      x-description-cn: order pre-set auot cancel time for TIF GTD order
                    priceMatch:
                      type: string
                      example: NONE
                      description: Price Match.
                      x-description-cn: Price Match.
  /papi/v1/cm/conditional/orderHistory:
    get:
      summary: Query CM Conditional Order History (USER_DATA)
      x-summary-cn: 查询CM条件单历史 (USER_DATA)
      description: Query CM Conditional Order History
      x-description-cn: 查询CM条件单历史
      tags:
        - trade
      operationId: queryCmConditionalOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-cm-conditional-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCmConditionalOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_cm_conditional_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_cm_conditional_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCmConditionalOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCmConditionalOrderHistory/QueryCmConditionalOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCmConditionalOrderHistoryExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: strategyId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: newClientStrategyId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `strategyId` or `newClientStrategyId` must be sent.
        - `NEW` orders will not be found.
        - These orders will not be found:
          - order status is `CANCELED` or `EXPIRED`, **AND**
          - order has NO filled trade, **AND**
          - created time + 7 days < current time
      x-parameters-notes-cn: |-
        - **注意:**
          - `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
          - `NEW` 状态的条件订单不会返回
          - 请注意，如果订单满足如下条件，不会被查询到：
          - 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
          - 订单没有任何的成交记录, 并且
          - 订单生成时间 + 3天 < 当前时间
      responses:
        "200":
          description: CM Conditional Order History
          x-description-cn: CM Conditional 订单 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  newClientStrategyId:
                    type: string
                    example: abc
                    description: New Client Strategy ID.
                    x-description-cn: New Client Strategy ID.
                  strategyId:
                    type: integer
                    example: 123445
                    format: int64
                    description: Strategy ID.
                    x-description-cn: Strategy ID.
                  strategyStatus:
                    type: string
                    example: TRIGGERED
                    description: Strategy Status.
                    x-description-cn: Strategy Status.
                  strategyType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Strategy Type.
                    x-description-cn: Strategy Type.
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                  symbol:
                    type: string
                    example: BTCUSD
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  orderId:
                    type: integer
                    example: 12123343534
                    format: int64
                    description: Normal orderID after trigger if appliable，only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  status:
                    type: string
                    example: NEW
                    description: Normal order status after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单状态, 当条件单被触发后才有
                  bookTime:
                    type: integer
                    example: 1566818724710
                    format: int64
                    description: order time
                    x-description-cn: 条件单下单时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  triggerTime:
                    type: integer
                    example: 1566818724750
                    format: int64
                    description: Trigger Time.
                    x-description-cn: Trigger Time.
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: MARKET
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    description: Working Type.
                    x-description-cn: Working Type.
                  priceProtect:
                    type: boolean
                    example: false
                    description: Price Protect.
                    x-description-cn: Price Protect.
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
  /papi/v1/cm/orderAmendment:
    get:
      summary: Query CM Modify Order History (TRADE)
      x-summary-cn: 查询CM订单修改历史 (TRADE)
      description: Get order modification history
      x-description-cn: 查询CM订单修改历史
      tags:
        - trade
      operationId: queryCmModifyOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-cm-modify-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCmModifyOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_cm_modify_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_cm_modify_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCmModifyOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCmModifyOrderHistory/QueryCmModifyOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCmModifyOrderHistoryExample.php
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
            example: BTCUSDT
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
            example: 500
            format: int64
            default: 100
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent."
      x-parameters-notes-cn: "- 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 orderId 为准"
      responses:
        "200":
          description: CM Modify Order History
          x-description-cn: CM Modify 订单 历史
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    orderId:
                      type: integer
                      example: 20072994037
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    clientOrderId:
                      type: string
                      example: LJ9R4QZDihCaS8UAOOLpgW
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    time:
                      type: integer
                      example: 1629184560899
                      format: int64
                      description: Order modification time
                      x-description-cn: 修改时间
                    amendment:
                      type: object
                      properties:
                        price:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "30004"
                              description: Before.
                              x-description-cn: Before.
                            after:
                              type: string
                              example: "30003.2"
                              description: After.
                              x-description-cn: After.
                          description: Price.
                          x-description-cn: Price.
                        origQty:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "1"
                              description: Before.
                              x-description-cn: Before.
                            after:
                              type: string
                              example: "1"
                              description: After.
                              x-description-cn: After.
                          description: Orig Qty.
                          x-description-cn: Orig Qty.
                        count:
                          type: integer
                          example: 3
                          format: int64
                          description: Order modification count, representing the number of times the order has been modified
                          x-description-cn: 修改记数，代表该修改记录是这笔订单第几次修改
                        modifyId:
                          type: integer
                          example: 123
                          format: int64
                          description: user-defined modification identifier, only returned if provided in the request
                          x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                      description: Amendment.
                      x-description-cn: Amendment.
  /papi/v1/cm/conditional/openOrder:
    get:
      summary: Query Current CM Open Conditional Order (USER_DATA)
      x-summary-cn: 查询CM当前条件挂单 (USER_DATA)
      description: Query Current CM Open Conditional Order
      x-description-cn: 查询CM当前条件挂单
      tags:
        - trade
      operationId: queryCurrentCmOpenConditionalOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-current-cm-open-conditional-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCurrentCmOpenConditionalOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_current_cm_open_conditional_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_current_cm_open_conditional_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCurrentCmOpenConditionalOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCurrentCmOpenConditionalOrder/QueryCurrentCmOpenConditionalOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCurrentCmOpenConditionalOrderExample.php
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
        - name: strategyId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: newClientStrategyId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Either `strategyId` or `newClientStrategyId` must be sent.

        - If the queried order has been triggered, cancelled or expired, the error message "Order does not exist" will
        be returned.
      x-parameters-notes-cn: |-
        - 注意:
          - `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
          - 如果查询的条件单已经为`CANCELED`， `TRIGGERED`或`EXPIRED`，会报错"Order does not exist"
      responses:
        "200":
          description: Current CM Open Conditional Order
          x-description-cn: 当前 CM 未完成Conditional 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  newClientStrategyId:
                    type: string
                    example: abc
                    description: New Client Strategy ID.
                    x-description-cn: New Client Strategy ID.
                  strategyId:
                    type: integer
                    example: 123445
                    format: int64
                    description: Strategy ID.
                    x-description-cn: Strategy ID.
                  strategyStatus:
                    type: string
                    example: NEW
                    description: Strategy Status.
                    x-description-cn: Strategy Status.
                  strategyType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    description: Strategy Type.
                    x-description-cn: Strategy Type.
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                  symbol:
                    type: string
                    example: BTCUSD
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  bookTime:
                    type: integer
                    example: 1566818724710
                    format: int64
                    description: order time
                    x-description-cn: 条件单下单时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  activatePrice:
                    type: string
                    example: "9020"
                    description: activation price, only return with TRAILING_STOP_MARKET order
                    x-description-cn: activation price, only return with TRAILING_STOP_MARKET order
                  priceRate:
                    type: string
                    example: "0.3"
                    description: callback rate, only return with TRAILING_STOP_MARKET order
                    x-description-cn: callback rate, only return with TRAILING_STOP_MARKET order
  /papi/v1/cm/openOrder:
    get:
      summary: Query Current CM Open Order (USER_DATA)
      x-summary-cn: 查看当前全部CM挂单 (USER_DATA)
      description: Query current CM open order
      x-description-cn: 查看当前全部CM挂单，请小心使用不带symbol参数的调用
      tags:
        - trade
      operationId: queryCurrentCmOpenOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-current-cm-open-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCurrentCmOpenOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_current_cm_open_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_current_cm_open_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCurrentCmOpenOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCurrentCmOpenOrder/QueryCurrentCmOpenOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCurrentCmOpenOrderExample.php
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
            example: BTCUSDT
          description: Trading pair.
          x-description-cn: 交易对。
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1917641
            format: int64
          description: Order ID.
          x-description-cn: 订单ID。
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: abc
          description: User-defined order ID.
          x-description-cn: 用户自定义订单ID。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `orderId` or `origClientOrderId` must be sent.
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
      x-parameters-notes-cn: |-
        - 必须发送 `orderId` 或 `origClientOrderId` 其中之一。
        - 如果查询的订单已经成交或取消，将返回错误信息 "Order does not exist"。
      responses:
        "200":
          description: Current CM Open Order
          x-description-cn: 当前 CM 未完成订单
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
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cumBase:
                      type: string
                      example: "0"
                      description: Cum Base.
                      x-description-cn: Cum Base.
                    executedQty:
                      type: string
                      example: "0"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.40"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    price:
                      type: string
                      example: "0"
                      description: Price.
                      x-description-cn: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: order time
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: update time
                      x-description-cn: update time
  /papi/v1/margin/openOrders:
    get:
      summary: Query Current Margin Open Order (USER_DATA)
      x-summary-cn: 查询杠杆账户挂单记录 (USER_DATA)
      description: Query Current Margin Open Order
      x-description-cn: 查询杠杆账户挂单记录
      tags:
        - trade
      operationId: queryCurrentMarginOpenOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-current-margin-open-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCurrentMarginOpenOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_current_margin_open_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_current_margin_open_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCurrentMarginOpenOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCurrentMarginOpenOrder/QueryCurrentMarginOpenOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCurrentMarginOpenOrderExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - If `symbol` is not sent, order records for all symbols are returned.

        - When returning all symbols, the request count charged to the rate limiter equals the number of symbols
        currently trading on the exchange.
      x-parameters-notes-cn: |-
        - 如未发送`symbol`，返回所有 symbols 订单记录。
        - 当返回所有symbols时，针对限速器计数的请求数量等于当前在交易所交易的symbols数量。
      responses:
        "200":
          description: Current Margin Open Order
          x-description-cn: 当前 杠杆 未完成订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    clientOrderId:
                      type: string
                      example: qhcZw71gAkCCTv0t0k8LUK
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    cummulativeQuoteQty:
                      type: string
                      example: "0.00000000"
                      description: Cummulative Quote Qty.
                      x-description-cn: Cummulative Quote Qty.
                    executedQty:
                      type: string
                      example: "0.00000000"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    icebergQty:
                      type: string
                      example: "0.00000000"
                      description: Iceberg Qty.
                      x-description-cn: Iceberg Qty.
                    isWorking:
                      type: boolean
                      example: true
                      description: Is Working.
                      x-description-cn: Is Working.
                    orderId:
                      type: integer
                      example: 211842552
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    origQty:
                      type: string
                      example: "0.30000000"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    price:
                      type: string
                      example: "0.00475010"
                      description: Price.
                      x-description-cn: Price.
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    status:
                      type: string
                      example: NEW
                      description: Status.
                      x-description-cn: 订单状态
                    stopPrice:
                      type: string
                      example: "0.00000000"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: please ignore when order type is TRAILING_STOP_MARKET
                    symbol:
                      type: string
                      example: BNBBTC
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    time:
                      type: integer
                      example: 1562040170089
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    updateTime:
                      type: integer
                      example: 1562040170089
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
                    accountId:
                      type: integer
                      example: 152950866
                      format: int64
                      description: Account ID.
                      x-description-cn: Account ID.
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_TAKER
                      description: self trading preventation mode
                      x-description-cn: self trading preventation mode
                    preventedMatchId:
                      type: string
                      example: "null"
                      description: Prevented Match ID.
                      x-description-cn: Prevented Match ID.
                    preventedQuantity:
                      type: string
                      example: "null"
                      description: Prevented Quantity.
                      x-description-cn: Prevented Quantity.
  /papi/v1/um/openOrder:
    get:
      summary: Query Current UM Open Order (USER_DATA)
      x-summary-cn: 查询当前UM挂单 (USER_DATA)
      description: Query current UM open order
      x-description-cn: 查询当前UM挂单
      tags:
        - trade
      operationId: queryCurrentUmOpenOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-current-um-open-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCurrentUmOpenOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_current_um_open_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_current_um_open_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCurrentUmOpenOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCurrentUmOpenOrder/QueryCurrentUmOpenOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCurrentUmOpenOrderExample.php
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
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Either `orderId` or `origClientOrderId` must be sent.
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
      x-parameters-notes-cn: |-
        - `orderId` 或 `origClientOrderId` 必须至少发送一个
        - 查询的订单如果已经成交或取消，将返回报错 "Order does not exist"
      responses:
        "200":
          description: Current UM Open Order
          x-description-cn: 当前 UM 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  avgPrice:
                    type: string
                    example: "0.00000"
                    description: Avg Price.
                    x-description-cn: Avg Price.
                  clientOrderId:
                    type: string
                    example: abc
                    description: Client Order ID.
                    x-description-cn: Client Order ID.
                  cumQuote:
                    type: string
                    example: "0"
                    description: Cum Quote.
                    x-description-cn: Cum Quote.
                  executedQty:
                    type: string
                    example: "0"
                    description: Executed Qty.
                    x-description-cn: Executed Qty.
                  orderId:
                    type: integer
                    example: 1917641
                    format: int64
                    description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                    x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                  origQty:
                    type: string
                    example: "0.40"
                    description: Orig Qty.
                    x-description-cn: Orig Qty.
                  origType:
                    type: string
                    example: LIMIT
                    description: Orig Type.
                    x-description-cn: Orig Type.
                  price:
                    type: string
                    example: "0"
                    description: Price.
                    x-description-cn: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Reduce Only.
                    x-description-cn: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    description: Side.
                    x-description-cn: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    description: BOTH means that it is the position of One-way Mode
                    x-description-cn: BOTH means that it is the position of One-way Mode
                  status:
                    type: string
                    example: NEW
                    description: Status.
                    x-description-cn: 订单状态
                  symbol:
                    type: string
                    example: BTCUSDT
                    description: Trade symbol, if existing.
                    x-description-cn: 交易对（如存在）。
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: order time
                    x-description-cn: order time
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time In Force.
                    x-description-cn: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    description: Normal order type after trigger if appliable
                    x-description-cn: 条件单触发后普通订单类型
                  updateTime:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: last update time
                    x-description-cn: 更新时间
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: self trading preventation mode
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: order pre-set auot cancel time for TIF GTD order
                  priceMatch:
                    type: string
                    example: NONE
                    description: Price Match.
                    x-description-cn: Price Match.
  /papi/v1/margin/allOrderList:
    get:
      summary: Query Margin Account's all OCO (USER_DATA)
      x-summary-cn: 查询特定杠杆账户所有 OCO (USER_DATA)
      description: Query all OCO for a specific margin account based on provided optional parameters
      x-description-cn: 根据提供的可选参数检索特定杠杆账户所有的 OCO 订单。
      tags:
        - trade
      operationId: queryMarginAccountsAllOco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-margin-accounts-all-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryMarginAccountsAllOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_margin_accounts_all_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_margin_accounts_all_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryMarginAccountsAllOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryMarginAccountsAllOco/QueryMarginAccountsAllOco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryMarginAccountsAllOcoExample.php
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
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Trade ID to fetch from.
          x-description-cn: 起始成交 ID。
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
            example: 500
            format: int64
            default: 100
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account's all OCO
          x-description-cn: 杠杆 账户's all OCO
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderListId:
                      type: integer
                      example: 29
                      format: int64
                      description: Order List ID.
                      x-description-cn: Order List ID.
                    contingencyType:
                      type: string
                      example: OCO
                      description: Contingency Type.
                      x-description-cn: Contingency Type.
                    listStatusType:
                      type: string
                      example: EXEC_STARTED
                      description: List Status Type.
                      x-description-cn: List Status Type.
                    listOrderStatus:
                      type: string
                      example: EXECUTING
                      description: List Order Status.
                      x-description-cn: List Order Status.
                    listClientOrderId:
                      type: string
                      example: amEEAXryFzFwYF1FeRpUoZ
                      description: List Client Order ID.
                      x-description-cn: List Client Order ID.
                    transactionTime:
                      type: integer
                      example: 1565245913483
                      format: int64
                      description: Transaction Time.
                      x-description-cn: Transaction Time.
                    symbol:
                      type: string
                      example: LTCBTC
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    orders:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: LTCBTC
                            description: Trade symbol, if existing.
                            x-description-cn: 交易对（如存在）。
                          orderId:
                            type: integer
                            example: 4
                            format: int64
                            description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                            x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                          clientOrderId:
                            type: string
                            example: oD7aesZqjEGlZrbtRpy5zB
                            description: Client Order ID.
                            x-description-cn: Client Order ID.
                      description: Orders.
                      x-description-cn: Orders.
  /papi/v1/margin/openOrderList:
    get:
      summary: Query Margin Account's Open OCO (USER_DATA)
      x-summary-cn: 查询杠杆账户 OCO 挂单 (USER_DATA)
      description: Query Margin Account's Open OCO
      x-description-cn: 查询杠杆账户 OCO 挂单
      tags:
        - trade
      operationId: queryMarginAccountsOpenOco
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-margin-accounts-open-oco
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryMarginAccountsOpenOco.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_margin_accounts_open_oco.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_margin_accounts_open_oco.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryMarginAccountsOpenOcoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryMarginAccountsOpenOco/QueryMarginAccountsOpenOco.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryMarginAccountsOpenOcoExample.php
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
          description: Value cannot be greater than 60000
          x-description-cn: 赋值不能大于 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Account's Open OCO
          x-description-cn: 杠杆 账户's 未完成OCO
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderListId:
                      type: integer
                      example: 31
                      format: int64
                      description: Order List ID.
                      x-description-cn: Order List ID.
                    contingencyType:
                      type: string
                      example: OCO
                      description: Contingency Type.
                      x-description-cn: Contingency Type.
                    listStatusType:
                      type: string
                      example: EXEC_STARTED
                      description: List Status Type.
                      x-description-cn: List Status Type.
                    listOrderStatus:
                      type: string
                      example: EXECUTING
                      description: List Order Status.
                      x-description-cn: List Order Status.
                    listClientOrderId:
                      type: string
                      example: wuB13fmulKj3YjdqWEcsnp
                      description: List Client Order ID.
                      x-description-cn: List Client Order ID.
                    transactionTime:
                      type: integer
                      example: 1565246080644
                      format: int64
                      description: Transaction Time.
                      x-description-cn: Transaction Time.
                    symbol:
                      type: string
                      example: LTCBTC
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    orders:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: LTCBTC
                            description: Trade symbol, if existing.
                            x-description-cn: 交易对（如存在）。
                          orderId:
                            type: integer
                            example: 4
                            format: int64
                            description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                            x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                          clientOrderId:
                            type: string
                            example: r3EH2N76dHfLoSZWIUw1bT
                            description: Client Order ID.
                            x-description-cn: Client Order ID.
                      description: Orders.
                      x-description-cn: Orders.
  /papi/v1/um/orderAmendment:
    get:
      summary: Query UM Modify Order History (TRADE)
      x-summary-cn: 查询UM订单修改历史 (TRADE)
      description: Get order modification history
      x-description-cn: 查询UM订单修改历史
      tags:
        - trade
      operationId: queryUmModifyOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-um-modify-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUmModifyOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_um_modify_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_um_modify_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUmModifyOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUmModifyOrderHistory/QueryUmModifyOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUmModifyOrderHistoryExample.php
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
            example: BTCUSDT
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
            example: 500
            format: int64
            default: 100
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent."
      x-parameters-notes-cn: "- 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 orderId 为准"
      responses:
        "200":
          description: UM Modify Order History
          x-description-cn: UM Modify 订单 历史
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
                      example: BTCUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSDT
                      description: Pair.
                      x-description-cn: Pair.
                    orderId:
                      type: integer
                      example: 20072994037
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    clientOrderId:
                      type: string
                      example: LJ9R4QZDihCaS8UAOOLpgW
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    time:
                      type: integer
                      example: 1629184560899
                      format: int64
                      description: Order modification time
                      x-description-cn: 修改时间
                    amendment:
                      type: object
                      properties:
                        price:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "30004"
                              description: Before.
                              x-description-cn: Before.
                            after:
                              type: string
                              example: "30003.2"
                              description: After.
                              x-description-cn: After.
                          description: Price.
                          x-description-cn: Price.
                        origQty:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "1"
                              description: Before.
                              x-description-cn: Before.
                            after:
                              type: string
                              example: "1"
                              description: After.
                              x-description-cn: After.
                          description: Orig Qty.
                          x-description-cn: Orig Qty.
                        count:
                          type: integer
                          example: 3
                          format: int64
                          description: Order modification count, representing the number of times the order has been modified
                          x-description-cn: 修改记数，代表该修改记录是这笔订单第几次修改
                        modifyId:
                          type: integer
                          example: 123
                          format: int64
                          description: user-defined modification identifier, only returned if provided in the request
                          x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                      description: Amendment.
                      x-description-cn: Amendment.
                    priceMatch:
                      type: string
                      example: NONE
                      description: Price Match.
                      x-description-cn: Price Match.
  /papi/v1/cm/forceOrders:
    get:
      summary: Query User's CM Force Orders (USER_DATA)
      x-summary-cn: 用户CM强平单历史 (USER_DATA)
      description: Query User's CM Force Orders
      x-description-cn: 查询用户CM强平单历史
      tags:
        - trade
      operationId: queryUsersCmForceOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-users-cm-force-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUsersCmForceOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_users_cm_force_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_users_cm_force_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUsersCmForceOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUsersCmForceOrders/QueryUsersCmForceOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUsersCmForceOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 20 with `symbol`
        - 50 without `symbol`
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
        - name: autoCloseType
          in: query
          required: false
          schema:
            type: string
            example: LIQUIDATION
            enum:
              - LIQUIDATION
              - ADL
          description: "`LIQUIDATION` for liquidation orders, `ADL` for ADL orders."
          x-description-cn: "`LIQUIDATION`: 强平单, `ADL`: ADL 减仓单."
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
            example: 500
            format: int64
            default: 50
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than 60000
          x-description-cn: 赋值不能超过 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - If "startTime" is not sent, data within 7 days before "endTime" can be queried
      x-parameters-notes-cn: |-
        - 如果没有传`autoCloseType`，强平单和 ADL 减仓单都会被返回
        - 如果没有传`startTime`, 只会返回`endTime`之前 7 天内的数据
      responses:
        "200":
          description: User's CM Force Orders
          x-description-cn: 用户's CM Force 订单
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
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    symbol:
                      type: string
                      example: BTCUSD_200925
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    pair:
                      type: string
                      example: BTCUSD
                      description: Pair.
                      x-description-cn: Pair.
                    status:
                      type: string
                      example: FILLED
                      description: Status.
                      x-description-cn: 订单状态
                    clientOrderId:
                      type: string
                      example: autoclose-1596542005017000006
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    price:
                      type: string
                      example: "11326.9"
                      description: Price.
                      x-description-cn: Price.
                    avgPrice:
                      type: string
                      example: "11326.9"
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    origQty:
                      type: string
                      example: "1"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    executedQty:
                      type: string
                      example: "1"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    cumBase:
                      type: string
                      example: "0.00882854"
                      description: Cum Base.
                      x-description-cn: Cum Base.
                    timeInForce:
                      type: string
                      example: IOC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    time:
                      type: integer
                      example: 1596542005019
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    updateTime:
                      type: integer
                      example: 1596542005050
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
  /papi/v1/margin/forceOrders:
    get:
      summary: Query User's Margin Force Orders (USER_DATA)
      x-summary-cn: 获取账户杠杆强制平仓记录 (USER_DATA)
      description: >-
        Query user's margin force orders


        > **Note:** Portfolio Margin accounts liquidated through the [Risk-Based Liquidation
        Adjustment](https://www.binance.com/en/support/faq/detail/662268636eb44b71af55c6c6a597d481) flow will not have
        any order or trade records returned by this endpoint. Query the capital flow endpoint instead: [Query Cross
        Isolated Margin Capital
        Flow](https://developers.binance.com/en/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-isolated-margin-capital-flow).
      x-description-cn: >-
        获取账户杠杆强制平仓记录


        > **注意：**
        通过[强平中基于风险的清算调整机制](https://www.binance.com/zh-CN/support/faq/detail/662268636eb44b71af55c6c6a597d481)流程被强平的统一账户（Portfolio
        Margin），本接口不会返回任何订单或成交记录。请改为查询资金流水接口：[查询全仓/逐仓资金流水](https://developers.binance.com/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-isolated-margin-capital-flow)。
      tags:
        - trade
      operationId: queryUsersMarginForceOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-users-margin-force-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUsersMarginForceOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_users_margin_force_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_users_margin_force_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUsersMarginForceOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUsersMarginForceOrders/QueryUsersMarginForceOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUsersMarginForceOrdersExample.php
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Current page number.
          x-description-cn: 当前页码。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than 60000
          x-description-cn: 赋值不能大于 `60000`
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: User's Margin Force Orders
          x-description-cn: 用户's 杠杆 Force 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        avgPrice:
                          type: string
                          example: "0.00388359"
                          description: Avg Price.
                          x-description-cn: Avg Price.
                        executedQty:
                          type: string
                          example: "31.39000000"
                          description: Executed Qty.
                          x-description-cn: Executed Qty.
                        orderId:
                          type: integer
                          example: 180015097
                          format: int64
                          description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                          x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                        price:
                          type: string
                          example: "0.00388110"
                          description: Price.
                          x-description-cn: Price.
                        qty:
                          type: string
                          example: "31.39000000"
                          description: Qty.
                          x-description-cn: Qty.
                        side:
                          type: string
                          example: SELL
                          description: Side.
                          x-description-cn: Side.
                        symbol:
                          type: string
                          example: BNBBTC
                          description: Trade symbol, if existing.
                          x-description-cn: 交易对（如存在）。
                        timeInForce:
                          type: string
                          example: GTC
                          description: Time In Force.
                          x-description-cn: Time In Force.
                        updatedTime:
                          type: integer
                          example: 1558941374745
                          format: int64
                          description: Updated Time.
                          x-description-cn: Updated Time.
                    description: Rows.
                    x-description-cn: Rows.
                  total:
                    type: integer
                    example: 1
                    format: int64
                    description: Total.
                    x-description-cn: Total.
  /papi/v1/um/forceOrders:
    get:
      summary: Query User's UM Force Orders (USER_DATA)
      x-summary-cn: 用户强平单历史 (USER_DATA)
      description: Query User's UM Force Orders
      x-description-cn: 查询用户UM强平单历史
      tags:
        - trade
      operationId: queryUsersUmForceOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-users-um-force-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUsersUmForceOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_users_um_force_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_users_um_force_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUsersUmForceOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUsersUmForceOrders/QueryUsersUmForceOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUsersUmForceOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - 20 with `symbol`
        - 50 without `symbol`
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
        - name: autoCloseType
          in: query
          required: false
          schema:
            type: string
            example: LIQUIDATION
            enum:
              - LIQUIDATION
              - ADL
          description: "`LIQUIDATION` for liquidation orders, `ADL` for ADL orders."
          x-description-cn: "`LIQUIDATION`: 强平单, `ADL`: ADL 减仓单."
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
            example: 500
            format: int64
            default: 50
            maximum: 100
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: The value cannot be greater than 60000
          x-description-cn: 赋值不能超过 60000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `autoCloseType` is not sent, orders with both of the types will be returned
        - If `startTime` is not sent, data within 7 days before `endTime` can be queried
      x-parameters-notes-cn: |-
        - 如果没有传`autoCloseType`，强平单和 ADL 减仓单都会被返回
        - 如果没有传`startTime`, 只会返回`endTime`之前 7 天内的数据
      responses:
        "200":
          description: User's UM Force Orders
          x-description-cn: 用户's UM Force 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 6071832819
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    status:
                      type: string
                      example: FILLED
                      description: Status.
                      x-description-cn: 订单状态
                    clientOrderId:
                      type: string
                      example: autoclose-1596107620040000020
                      description: Client Order ID.
                      x-description-cn: Client Order ID.
                    price:
                      type: string
                      example: "10871.09"
                      description: Price.
                      x-description-cn: Price.
                    avgPrice:
                      type: string
                      example: "10913.21000"
                      description: Avg Price.
                      x-description-cn: Avg Price.
                    origQty:
                      type: string
                      example: "0.001"
                      description: Orig Qty.
                      x-description-cn: Orig Qty.
                    executedQty:
                      type: string
                      example: "0.001"
                      description: Executed Qty.
                      x-description-cn: Executed Qty.
                    cumQuote:
                      type: string
                      example: "10.91321"
                      description: Cum Quote.
                      x-description-cn: Cum Quote.
                    timeInForce:
                      type: string
                      example: IOC
                      description: Time In Force.
                      x-description-cn: Time In Force.
                    type:
                      type: string
                      example: LIMIT
                      description: Normal order type after trigger if appliable
                      x-description-cn: 条件单触发后普通订单类型
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Reduce Only.
                      x-description-cn: Reduce Only.
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
                    origType:
                      type: string
                      example: LIMIT
                      description: Orig Type.
                      x-description-cn: Orig Type.
                    time:
                      type: integer
                      example: 1596107620044
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    updateTime:
                      type: integer
                      example: 1596107620087
                      format: int64
                      description: last update time
                      x-description-cn: 更新时间
  /papi/v1/um/userTrades:
    get:
      summary: UM Account Trade List (USER_DATA)
      x-summary-cn: UM账户成交历史 (USER_DATA)
      description: Get trades for a specific account and UM symbol.
      x-description-cn: 获取UM某交易对的成交历史
      tags:
        - trade
      operationId: umAccountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#um-account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/umAccountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/um_account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/um_account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/UmAccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/UmAccountTradeList/UmAccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/UmAccountTradeListExample.php
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
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
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
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Trade ID to fetch from.
          x-description-cn: 起始成交 ID。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 500
            format: int64
            default: 100
            maximum: 1000
          description: Number of results returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `startTime` and `endTime` are both not sent, then the last '7 days' data will be returned.
        - The time between `startTime` and `endTime` cannot be longer than 7 days.
        - The parameter `fromId` cannot be sent with `startTime` or `endTime`.
      x-parameters-notes-cn: |-
        - 如果`startTime`和`endTime`均不填，默认返回最近7天数据
        - `startTime`和`endTime`的最大间隔为7天
        - 参数 `fromId` 不能和`startTime` 与 `endTime`一起发送
      responses:
        "200":
          description: UM Account Trade List
          x-description-cn: UM 账户 交易 列表
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
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
                    id:
                      type: integer
                      example: 67880589
                      format: int64
                      description: ID.
                      x-description-cn: ID.
                    orderId:
                      type: integer
                      example: 270093109
                      format: int64
                      description: Normal orderID after trigger if appliable, only have when the strategy is triggered
                      x-description-cn: 条件单触发后普通单id，当条件单被触发后才有
                    side:
                      type: string
                      example: SELL
                      description: Side.
                      x-description-cn: Side.
                    price:
                      type: string
                      example: "28511.00"
                      description: Price.
                      x-description-cn: Price.
                    qty:
                      type: string
                      example: "0.010"
                      description: Qty.
                      x-description-cn: Qty.
                    realizedPnl:
                      type: string
                      example: "2.58500000"
                      description: Realized Pnl.
                      x-description-cn: Realized Pnl.
                    quoteQty:
                      type: string
                      example: "285.11000"
                      description: Quote Qty.
                      x-description-cn: Quote Qty.
                    commission:
                      type: string
                      example: "0.11404400"
                      description: Commission.
                      x-description-cn: Commission.
                    commissionAsset:
                      type: string
                      example: USDT
                      description: Commission Asset.
                      x-description-cn: Commission Asset.
                    time:
                      type: integer
                      example: 1680688557875
                      format: int64
                      description: Event time.
                      x-description-cn: 时间。
                    buyer:
                      type: boolean
                      example: false
                      description: Buyer.
                      x-description-cn: Buyer.
                    maker:
                      type: boolean
                      example: false
                      description: Maker.
                      x-description-cn: Maker.
                    positionSide:
                      type: string
                      example: BOTH
                      description: BOTH means that it is the position of One-way Mode
                      x-description-cn: BOTH means that it is the position of One-way Mode
  /papi/v1/um/adlQuantile:
    get:
      summary: UM Position ADL Quantile Estimation (USER_DATA)
      x-summary-cn: UM持仓ADL队列估算 (USER_DATA)
      description: >-
        Query UM Position ADL Quantile Estimation


        * Values update every 30s.

        * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.

        * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and
        "BOTH" will be returned to show the positions' adl quantiles of different position sides.

        * If the positions of the symbol are crossed margined in Hedge Mode:

        * "HEDGE" as a sign will be returned instead of "BOTH";

        * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and
        "SHORT" when there are positions in both of long and short sides.
      x-description-cn: >-
        查询UM持仓ADL队列估算


        * 每30秒更新数据

        * 队列分数0，1，2，3，4，分数越高说明在ADL队列中的位置越靠前

        * 对于单向持仓模式或者是逐仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "BOTH" 分别表示不同持仓方向上持仓的adl队列分数

        * 对于全仓状态下的双向持仓模式的交易对，会返回 "LONG", "SHORT" 和 "HEDGE",
        其中"HEDGE"的存在仅作为标记;其中如果多空均有持仓的情况下,"LONG"和"SHORT"返回共同计算后相同的队列分数。
      tags:
        - trade
      operationId: umPositionAdlQuantileEstimation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#um-position-adl-quantile-estimation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/umPositionAdlQuantileEstimation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/um_position_adl_quantile_estimation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/um_position_adl_quantile_estimation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/UmPositionAdlQuantileEstimationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/UmPositionAdlQuantileEstimation/UmPositionAdlQuantileEstimation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/UmPositionAdlQuantileEstimationExample.php
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
            example: BTCUSDT
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: UM Position ADL Quantile Estimation
          x-description-cn: UM 持仓 ADL Quantile Estimation
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ETHUSDT
                      description: Trade symbol, if existing.
                      x-description-cn: 交易对（如存在）。
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
                          description: adl quantile for "SHORT" position in hedge mode
                          x-description-cn: 双开模式下空头持仓的ADL队列估算分
                        BOTH:
                          type: integer
                          example: 0
                          format: int64
                          description: adl quantile for position in one-way mode
                          x-description-cn: 单开模式下持仓的ADL队列估算分
                      description: Adl Quantile.
                      x-description-cn: Adl Quantile.
  /papi/v1/um/algo/order:
    post:
      summary: New UM Algo Order (TRADE)
      x-summary-cn: UM条件单下单 (TRADE)
      description: Place new UM conditional order
      x-description-cn: UM条件单下单
      tags:
        - trade
      operationId: newUmAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#new-um-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/newUmAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/new_um_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/new_um_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/NewUmAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/NewUmAlgoOrder/NewUmAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/NewUmAlgoOrderExample.php
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
        - Algo order with type `STOP`, parameter `timeInForce` can be sent (default `GTC`).

        - Algo order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent (default `GTC`).

        - Condition orders will be triggered when price reaches the `triggerPrice`.

        - `STOP`, `STOP_MARKET`: BUY: latest price >= `triggerPrice`; SELL: latest price <= `triggerPrice`.

        - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`: BUY: latest price <= `triggerPrice`; SELL: latest price >=
        `triggerPrice`.

        - `TRAILING_STOP_MARKET`: BUY: lowest price after order placed <= `activatePrice`, and latest price >= lowest
        price * (1 + `callbackRate`); SELL: highest price after order placed >= `activatePrice`, and latest price <=
        highest price * (1 - `callbackRate`).

        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`: follow the same rules for conditional orders;
        if triggered, close all current long position (if `SELL`) or current short position (if `BUY`); cannot be used
        with `quantity` parameter; cannot be used with `reduceOnly` parameter; in Hedge Mode, cannot be used with `BUY`
        orders in `LONG` position side, and cannot be used with `SELL` orders in `SHORT` position side.

        - `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
      x-parameters-notes-cn: >-
        - 类型为 `STOP` 的条件订单可以传入参数 `timeInForce`（默认值为 `GTC`）。

        - 类型为 `TAKE_PROFIT` 的条件订单可以传入参数 `timeInForce`（默认值为 `GTC`）。

        - 条件单的触发必须满足对应价格条件。

        - `STOP`, `STOP_MARKET` 止损单: 买入: 最新价格 >= 触发价; 卖出: 最新价格 <= 触发价。

        - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单: 买入: 最新价格 <= 触发价; 卖出: 最新价格 >= 触发价。

        - `TRAILING_STOP_MARKET` 跟踪止损单: 买入: 最低价 <= 激活价格，且最新价格 >= 最低价 * (1 + 回调比例); 卖出: 最高价 >= 激活价格，且最新价格 <= 最高价 * (1 -
        回调比例)。

        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` 配合 `closePosition`=`true`:
        条件单触发依照上述条件单触发逻辑；条件触发后，平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)；不支持 `quantity` 参数；自带只平仓属性，不支持 `reduceOnly`
        参数；双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持`SELL`。

        - `selfTradePreventionMode` 仅在 `timeInForce` 为 `IOC` 或 `GTC` 或 `GTD` 时生效。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - algoType
                - symbol
                - side
                - type
                - timestamp
              properties:
                algoType:
                  type: string
                  example: CONDITIONAL
                  enum:
                    - CONDITIONAL
                  description: Only support `CONDITIONAL`
                  x-description-cn: 仅支持 `CONDITIONAL`
                symbol:
                  type: string
                  example: BNBUSDT
                side:
                  type: string
                  example: SELL
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
                  description: Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode
                  x-description-cn: 单向持仓模式下默认且仅可填`BOTH`；双向持仓模式下必填，仅可选择 `LONG` 或 `SHORT`
                type:
                  type: string
                  example: TAKE_PROFIT
                  enum:
                    - STOP
                    - TAKE_PROFIT
                    - STOP_MARKET
                    - TAKE_PROFIT_MARKET
                    - TRAILING_STOP_MARKET
                  description: Conditional order type
                  x-description-cn: 条件订单类型
                timeInForce:
                  type: string
                  example: GTC
                  enum:
                    - IOC
                    - GTC
                    - FOK
                    - GTX
                    - GTD
                  default: GTC
                quantity:
                  type: number
                  format: float
                  example: "0.01"
                  description: Order quantity. Cannot be sent with `closePosition`=`true`(Close-All)
                  x-description-cn: 下单数量,使用`closePosition`不支持此参数。
                price:
                  type: number
                  format: float
                  example: "750.000"
                  description: Order price
                  x-description-cn: 委托价格
                triggerPrice:
                  type: number
                  format: float
                  example: "750.000"
                  description: Trigger price
                  x-description-cn: 触发价
                workingType:
                  type: string
                  example: CONTRACT_PRICE
                  enum:
                    - MARK_PRICE
                    - CONTRACT_PRICE
                  default: CONTRACT_PRICE
                  description: Trigger price type. Default `CONTRACT_PRICE`
                  x-description-cn: 触发类型，默认 `CONTRACT_PRICE`
                priceMatch:
                  type: string
                  example: NONE
                  enum:
                    - OPPONENT
                    - OPPONENT_5
                    - OPPONENT_10
                    - OPPONENT_20
                    - QUEUE
                    - QUEUE_5
                    - QUEUE_10
                    - QUEUE_20
                  description: Can't be passed together with `price`
                  x-description-cn: 不能与 `price` 同时传
                closePosition:
                  type: string
                  example: "true"
                  enum:
                    - "true"
                    - "false"
                  description: Close-All, used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.
                  x-description-cn: 触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用
                priceProtect:
                  type: string
                  example: "false"
                  enum:
                    - "true"
                    - "false"
                  default: "false"
                  description: Price protection. Default `false`
                  x-description-cn: 条件单触发保护，默认 `false`
                reduceOnly:
                  type: string
                  example: "false"
                  enum:
                    - "true"
                    - "false"
                  default: "false"
                  description: Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`
                  x-description-cn: 非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。
                activatePrice:
                  type: number
                  format: float
                  example: 700
                  description: Used with `TRAILING_STOP_MARKET`, default as latest price
                  x-description-cn: 追踪止损激活价格，仅`TRAILING_STOP_MARKET`需要
                callbackRate:
                  type: number
                  format: float
                  example: 1
                  description: Used with `TRAILING_STOP_MARKET`, min 0.1, max 20 (1 = 1%)
                  x-description-cn: 追踪止损回调比例，范围[0.1, 20]，1代表1%
                clientAlgoId:
                  type: string
                  example: 6B2I9XVcJpCjqPAJ4YoFX7
                  description: Unique id among open orders. Auto-generated if not sent
                  x-description-cn: 用户自定义的条件订单号，不可以重复出现在挂单中
                newOrderRespType:
                  type: string
                  example: ACK
                  enum:
                    - ACK
                    - RESULT
                  default: ACK
                selfTradePreventionMode:
                  type: string
                  example: NONE
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_MAKER
                    - EXPIRE_BOTH
                  default: NONE
                goodTillDate:
                  type: integer
                  format: int64
                  example: 0
                  description: Order cancel time for `GTD` timeInForce, mandatory when timeInForce is `GTD`
                  x-description-cn: TIF为GTD时订单的自动取消时间，当timeInForce为GTD时必传
                recvWindow:
                  type: integer
                  format: int64
                  maximum: 60000
                  example: 5000
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: New UM Algo Order
          x-description-cn: UM条件单下单
          content:
            application/json:
              schema:
                type: object
                properties:
                  algoId:
                    type: integer
                    example: 2146760
                    format: int64
                  clientAlgoId:
                    type: string
                    example: 6B2I9XVcJpCjqPAJ4YoFX7
                  algoType:
                    type: string
                    example: CONDITIONAL
                  orderType:
                    type: string
                    example: TAKE_PROFIT
                  symbol:
                    type: string
                    example: BNBUSDT
                  side:
                    type: string
                    example: SELL
                  positionSide:
                    type: string
                    example: BOTH
                  timeInForce:
                    type: string
                    example: GTC
                  quantity:
                    type: string
                    example: "0.01"
                  algoStatus:
                    type: string
                    example: NEW
                  triggerPrice:
                    type: string
                    example: "750.000"
                  price:
                    type: string
                    example: "750.000"
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
                  activatePrice:
                    type: string
                    example: ""
                    description: TRAILING_STOP_MARKET order
                    x-description-cn: TRAILING_STOP_MARKET order
                  callbackRate:
                    type: string
                    example: ""
                    description: TRAILING_STOP_MARKET order
                    x-description-cn: TRAILING_STOP_MARKET order
                  createTime:
                    type: integer
                    example: 1750485492076
                    format: int64
                  updateTime:
                    type: integer
                    example: 1750485492076
                    format: int64
                  triggerTime:
                    type: integer
                    example: 0
                    format: int64
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
    delete:
      summary: Cancel UM Algo Order (TRADE)
      x-summary-cn: UM撤销条件订单 (TRADE)
      description: Cancel an active UM algo order
      x-description-cn: 撤销条件订单
      tags:
        - trade
      operationId: cancelUmAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-um-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelUmAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_um_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_um_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelUmAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelUmAlgoOrder/CancelUmAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelUmAlgoOrderExample.php
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
            example: 2146760
            format: int64
          description: Algo order ID
          x-description-cn: 系统订单号
        - name: clientAlgoId
          in: query
          required: false
          schema:
            type: string
            example: 6B2I9XVcJpCjqPAJ4YoFX7
          description: Client algo order ID
          x-description-cn: 用户自定义的订单号
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            maximum: 60000
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
            description: >-
              Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time
              and is validated by the server for signed endpoints.
            x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `algoId` or `clientAlgoId` must be sent."
      x-parameters-notes-cn: "- `algoId` 与 `clientAlgoId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel UM Algo Order
          x-description-cn: UM撤销条件订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  complete:
                    type: boolean
                    example: true
  /papi/v1/um/algo/allOpenOrders:
    delete:
      summary: Cancel All UM Algo Open Orders (TRADE)
      x-summary-cn: UM撤销全部条件订单 (TRADE)
      description: Cancel All UM Algo Open Orders
      x-description-cn: UM撤销全部条件订单
      tags:
        - trade
      operationId: cancelAllUmAlgoOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#cancel-all-um-algo-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/cancelAllUmAlgoOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/cancel_all_um_algo_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/cancel_all_um_algo_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/CancelAllUmAlgoOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/CancelAllUmAlgoOpenOrders/CancelAllUmAlgoOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/CancelAllUmAlgoOpenOrdersExample.php
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
          description: Symbol
          x-description-cn: 交易对
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            maximum: 60000
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
            description: >-
              Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time
              and is validated by the server for signed endpoints.
            x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All UM Algo Open Orders
          x-description-cn: UM撤销全部条件订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
  /papi/v1/um/algo/algoOrder:
    get:
      summary: Query Current UM Open Algo Order (USER_DATA)
      x-summary-cn: 查询UM当前条件挂单 (USER_DATA)
      description: >-
        Check an UM algo order's status. Orders will not be found if: status is CANCELED/EXPIRED with no fills and
        created 3+ days ago; or created 90+ days ago.
      x-description-cn: 查询UM条件订单状态。如果订单状态为 CANCELED 或 EXPIRED 且无成交记录且创建时间超过3天，或创建时间超过90天，将不会被查询到。
      tags:
        - trade
      operationId: queryCurrentUmOpenAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-current-um-open-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryCurrentUmOpenAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_current_um_open_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_current_um_open_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryCurrentUmOpenAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryCurrentUmOpenAlgoOrder/QueryCurrentUmOpenAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryCurrentUmOpenAlgoOrderExample.php
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
          required: false
          schema:
            type: integer
            example: 2146760
            format: int64
          description: Algo order ID
          x-description-cn: 系统订单号
        - name: clientAlgoId
          in: query
          required: false
          schema:
            type: string
            example: 6B2I9XVcJpCjqPAJ4YoFX7
          description: Client algo order ID
          x-description-cn: 用户自定义的订单号
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            maximum: 60000
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
            description: >-
              Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time
              and is validated by the server for signed endpoints.
            x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `algoId` or `clientAlgoId` must be sent. `algoId` is self-increment for each specific `symbol`."
      x-parameters-notes-cn: "- 至少需要发送 `algoId` 与 `clientAlgoId` 中的一个。`algoId` 在 `symbol` 维度是自增的。"
      responses:
        "200":
          description: Query UM Algo Order
          x-description-cn: 查询UM当前条件挂单
          content:
            application/json:
              schema:
                type: object
                properties:
                  algoId:
                    type: integer
                    example: 2146760
                    format: int64
                  clientAlgoId:
                    type: string
                    example: 6B2I9XVcJpCjqPAJ4YoFX7
                  algoType:
                    type: string
                    example: CONDITIONAL
                  orderType:
                    type: string
                    example: TAKE_PROFIT
                  symbol:
                    type: string
                    example: BNBUSDT
                  side:
                    type: string
                    example: SELL
                  positionSide:
                    type: string
                    example: BOTH
                  timeInForce:
                    type: string
                    example: GTC
                  quantity:
                    type: string
                    example: "0.01"
                  algoStatus:
                    type: string
                    example: CANCELED
                  actualOrderId:
                    type: string
                    example: ""
                  actualPrice:
                    type: string
                    example: "0.00000"
                  triggerPrice:
                    type: string
                    example: "750.000"
                  price:
                    type: string
                    example: "750.000"
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
                    example: 1750485492076
                    format: int64
                  updateTime:
                    type: integer
                    example: 1750514545091
                    format: int64
                  triggerTime:
                    type: integer
                    example: 0
                    format: int64
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
  /papi/v1/um/algo/openAlgoOrders:
    get:
      summary: Query All Current UM Open Algo Orders (USER_DATA)
      x-summary-cn: 查看UM当前全部条件挂单 (USER_DATA)
      description: Get all UM open algo orders on a symbol. If the symbol is not sent, orders for all symbols will be returned.
      x-description-cn: 查看当前全部条件挂单。不带symbol参数，会返回所有交易对的挂单。
      tags:
        - trade
      operationId: queryAllCurrentUmOpenAlgoOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-all-current-um-open-algo-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryAllCurrentUmOpenAlgoOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_all_current_um_open_algo_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_all_current_um_open_algo_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryAllCurrentUmOpenAlgoOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryAllCurrentUmOpenAlgoOrders/QueryAllCurrentUmOpenAlgoOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryAllCurrentUmOpenAlgoOrdersExample.php
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
        - name: algoType
          in: query
          required: false
          schema:
            type: string
            example: CONDITIONAL
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BNBUSDT
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 2146760
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            maximum: 60000
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
            description: >-
              Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time
              and is validated by the server for signed endpoints.
            x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Weight: 1 for a single symbol; 40 when the symbol parameter is omitted."
      x-parameters-notes-cn: "- 权重：带symbol为1，不带symbol为40。"
      responses:
        "200":
          description: Query All Current UM Open Algo Orders
          x-description-cn: 查看UM当前全部条件挂单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    algoId:
                      type: integer
                      example: 2146760
                      format: int64
                    clientAlgoId:
                      type: string
                      example: 6B2I9XVcJpCjqPAJ4YoFX7
                    algoType:
                      type: string
                      example: CONDITIONAL
                    orderType:
                      type: string
                      example: TAKE_PROFIT
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      example: SELL
                    positionSide:
                      type: string
                      example: BOTH
                    timeInForce:
                      type: string
                      example: GTC
                    quantity:
                      type: string
                      example: "0.01"
                    algoStatus:
                      type: string
                      example: NEW
                    triggerPrice:
                      type: string
                      example: "750.000"
                    price:
                      type: string
                      example: "750.000"
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
                      example: 1750485492076
                      format: int64
                    updateTime:
                      type: integer
                      example: 1750485492076
                      format: int64
                    triggerTime:
                      type: integer
                      example: 0
                      format: int64
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
  /papi/v1/um/algo/allAlgoOrders:
    get:
      summary: Query UM Algo Order History (USER_DATA)
      x-summary-cn: 查询UM条件单历史 (USER_DATA)
      description: "Get all algo orders: ACTIVE, CANCELED, TRIGGERED or FINISHED."
      x-description-cn: 查询UM条件单历史
      tags:
        - trade
      operationId: queryUmAlgoOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#query-um-algo-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/queryUmAlgoOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/query_um_algo_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/query_um_algo_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/QueryUmAlgoOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/QueryUmAlgoOrderHistory/QueryUmAlgoOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/QueryUmAlgoOrderHistoryExample.php
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
          required: true
          schema:
            type: string
            example: BNBUSDT
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 2146760
          description: Only return orders >= this algoId
          x-description-cn: 只返回此orderID及之后的订单，缺省返回最近的订单
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1770130294138
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1770736694138
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            format: int64
            default: 500
            maximum: 1000
            example: 500
          description: Default 500; max 1000
          x-description-cn: 默认值:500 最大值:1000
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            maximum: 60000
            example: 5000
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
            description: >-
              Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time
              and is validated by the server for signed endpoints.
            x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `algoId` is set, it will get orders >= that `algoId`. Otherwise most recent orders are returned.
        - The query time period must be less than 7 days (default as the recent 7 days).
      x-parameters-notes-cn: |-
        - 如果设置了 `algoId`，将返回该 ID 及之后的订单，否则返回最近的订单。
        - 查询时间范围最大不得超过7天。默认查询最近7天内的数据。
      responses:
        "200":
          description: Query UM Algo Order History
          x-description-cn: 查询UM条件单历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    algoId:
                      type: integer
                      example: 2146760
                      format: int64
                    clientAlgoId:
                      type: string
                      example: 6B2I9XVcJpCjqPAJ4YoFX7
                    algoType:
                      type: string
                      example: CONDITIONAL
                    orderType:
                      type: string
                      example: TAKE_PROFIT
                    symbol:
                      type: string
                      example: BNBUSDT
                    side:
                      type: string
                      example: SELL
                    positionSide:
                      type: string
                      example: BOTH
                    timeInForce:
                      type: string
                      example: GTC
                    quantity:
                      type: string
                      example: "0.01"
                    algoStatus:
                      type: string
                      example: CANCELED
                    actualOrderId:
                      type: string
                      example: ""
                    actualPrice:
                      type: string
                      example: "0.00000"
                    triggerPrice:
                      type: string
                      example: "750.000"
                    price:
                      type: string
                      example: "750.000"
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
                      example: 1750485492076
                      format: int64
                    updateTime:
                      type: integer
                      example: 1750514545091
                      format: int64
                    triggerTime:
                      type: integer
                      example: 0
                      format: int64
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
  /papi/v1/um/stock/contract:
    post:
      summary: Futures TradFi Perps Contract (USER_DATA)
      x-summary-cn: 传统金融合约协议 (USER_DATA)
      description: Sign TradFi-Perps agreement contract
      x-description-cn: 签署传统金融合约协议
      tags:
        - trade
      operationId: futuresTradfiPerpsContract
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/trade#futures-tradfi-perps-contract
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/TradeApi/futuresTradfiPerpsContract.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/trade_api/futures_tradfi_perps_contract.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/Trade/futures_tradfi_perps_contract.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/trade/FuturesTradfiPerpsContractExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/TradeAPI/FuturesTradfiPerpsContract/FuturesTradfiPerpsContract.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/trade/FuturesTradfiPerpsContractExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                recvWindow:
                  type: integer
                  format: int64
                  maximum: 60000
                  example: 5000
                timestamp:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Futures TradFi Perps Contract
          x-description-cn: 传统金融合约协议
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                  msg:
                    type: string
                    example: success
  /papi/v1/listenKey:
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
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/userdatastreams/CloseUserDataStreamExample.php
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
        will close after 60 minutes. It's recommended to send a ping about every
        60 minutes.
      x-description-cn: 有效期延长至本次调用后60分钟
      tags:
        - user-data-streams
      operationId: keepaliveUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/userdatastreams/KeepaliveUserDataStreamExample.php
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
    post:
      summary: Start User Data Stream (USER_STREAM)
      x-summary-cn: 生成listenKey (USER_STREAM)
      description: >-
        Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account
        has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.
      x-description-cn: 创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。
      tags:
        - user-data-streams
      operationId: startUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/rest-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin/examples/rest-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin/rest_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin/examples/rest_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin/rest/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomargin/examples/restapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin/userdatastreams/StartUserDataStreamExample.php
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
                    description: Listen Key.
                    x-description-cn: Listen Key.
```